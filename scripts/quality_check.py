"""
quality_check.py
================
Wyld Sales Operations — Data Quality & Compliance Checker

Scans all tables for data integrity issues, business rule violations,
and state compliance problems. Outputs a prioritized QC report to:
  - Console (summary)
  - data/qc_report.csv       (full flagged records, machine-readable)
  - data/qc_summary.csv      (category-level summary, feeds Excel dashboard)

Flag severity levels:
  CRITICAL  — data that will cause an operational or compliance failure
  WARNING   — data that needs review but won't break the system
  INFO      — observations worth monitoring

Check categories:
  1. Order integrity       — missing fields, invalid status, orphaned records
  2. Compliance           — THC limits, license validity, restricted markets
  3. Account health       — credit holds, expiring licenses, overdue AR
  4. Inventory            — stockouts, reorder alerts, allocation overages
  5. Financial            — pricing anomalies, zero-value lines, total mismatches
  6. Fulfillment timing   — overdue open orders, missing fulfillment dates
  7. Duplicate detection  — same account + date + total combinations

Usage:
    python quality_check.py             # run all checks, print report
    python quality_check.py --category compliance   # single category
    python quality_check.py --severity CRITICAL     # critical only
    python quality_check.py --export-excel          # write QC tab to Excel
"""

import argparse
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Optional

import pandas as pd

from database import get_connection, DB_PATH

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

CRITICAL = "CRITICAL"
WARNING  = "WARNING"
INFO     = "INFO"

SEVERITY_ORDER = {CRITICAL: 0, WARNING: 1, INFO: 2}


@dataclass
class QCFlag:
    category:   str
    severity:   str
    check_name: str
    record_id:  str
    detail:     str
    table:      str
    field:      Optional[str] = None
    value:      Optional[str] = None
    recommended_action: str   = ""


@dataclass
class QCReport:
    flags:      list[QCFlag] = field(default_factory=list)
    run_date:   str = field(default_factory=lambda: date.today().isoformat())
    checks_run: int = 0

    def add(self, flag: QCFlag) -> None:
        self.flags.append(flag)

    def summary(self) -> pd.DataFrame:
        if not self.flags:
            return pd.DataFrame()
        df = pd.DataFrame([
            {"category": f.category, "severity": f.severity,
             "check_name": f.check_name}
            for f in self.flags
        ])
        return (df.groupby(["category", "severity", "check_name"])
                  .size()
                  .reset_index(name="count")
                  .sort_values(["severity", "category"]))

    def to_dataframe(self) -> pd.DataFrame:
        if not self.flags:
            return pd.DataFrame()
        return pd.DataFrame([
            {
                "severity":           f.severity,
                "category":           f.category,
                "check_name":         f.check_name,
                "table":              f.table,
                "record_id":          f.record_id,
                "field":              f.field,
                "value":              f.value,
                "detail":             f.detail,
                "recommended_action": f.recommended_action,
            }
            for f in sorted(self.flags,
                            key=lambda x: SEVERITY_ORDER[x.severity])
        ])

    @property
    def critical_count(self) -> int:
        return sum(1 for f in self.flags if f.severity == CRITICAL)

    @property
    def warning_count(self) -> int:
        return sum(1 for f in self.flags if f.severity == WARNING)

    @property
    def info_count(self) -> int:
        return sum(1 for f in self.flags if f.severity == INFO)


# ---------------------------------------------------------------------------
# Individual check functions
# ---------------------------------------------------------------------------

def check_order_integrity(conn, report: QCReport) -> int:
    """Check 1 — Order data completeness and relational integrity."""
    count = 0

    # 1a. Orders missing required fields
    df = pd.read_sql_query("""
        SELECT order_id, status, order_date, customer_id,
               fulfillment_date, invoice_date, rejection_reason
        FROM orders
    """, conn)

    for _, row in df.iterrows():
        # Invoiced orders must have both fulfillment and invoice dates
        if row["status"] == "Invoiced":
            if pd.isna(row["fulfillment_date"]) or row["fulfillment_date"] == "":
                report.add(QCFlag(
                    category="Order Integrity", severity=WARNING,
                    check_name="Missing fulfillment date",
                    record_id=row["order_id"], table="orders",
                    field="fulfillment_date", value=None,
                    detail=f"{row['order_id']} is Invoiced but has no fulfillment date",
                    recommended_action="Confirm shipment date with Distribution team"
                ))
                count += 1
            if pd.isna(row["invoice_date"]) or row["invoice_date"] == "":
                report.add(QCFlag(
                    category="Order Integrity", severity=CRITICAL,
                    check_name="Missing invoice date",
                    record_id=row["order_id"], table="orders",
                    field="invoice_date", value=None,
                    detail=f"{row['order_id']} is Invoiced but has no invoice date — AR cannot age",
                    recommended_action="Issue invoice immediately or revert status to Fulfilled"
                ))
                count += 1

        # Rejected orders must have a rejection reason
        if row["status"] == "Rejected" and (
            pd.isna(row["rejection_reason"]) or row["rejection_reason"] == ""
        ):
            report.add(QCFlag(
                category="Order Integrity", severity=WARNING,
                check_name="Missing rejection reason",
                record_id=row["order_id"], table="orders",
                field="rejection_reason", value=None,
                detail=f"{row['order_id']} is Rejected with no recorded reason",
                recommended_action="Contact rep to document rejection reason"
            ))
            count += 1

    # 1b. Orders with no line items
    orphan_df = pd.read_sql_query("""
        SELECT o.order_id FROM orders o
        LEFT JOIN order_items oi ON o.order_id = oi.order_id
        WHERE oi.order_id IS NULL
    """, conn)
    for _, row in orphan_df.iterrows():
        report.add(QCFlag(
            category="Order Integrity", severity=CRITICAL,
            check_name="Order with no line items",
            record_id=row["order_id"], table="orders",
            detail=f"{row['order_id']} has no line items — cannot be fulfilled",
            recommended_action="Add line items or void the order"
        ))
        count += 1

    # 1c. Order total mismatch vs sum of line items
    mismatch_df = pd.read_sql_query("""
        SELECT o.order_id,
               o.order_total                   AS header_total,
               ROUND(SUM(oi.line_total), 2)    AS items_total,
               ABS(o.order_total - SUM(oi.line_total)) AS delta
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY o.order_id
        HAVING delta > 0.02
    """, conn)
    for _, row in mismatch_df.iterrows():
        report.add(QCFlag(
            category="Order Integrity", severity=CRITICAL,
            check_name="Order total mismatch",
            record_id=row["order_id"], table="orders",
            field="order_total",
            value=f"header={row['header_total']:.2f}, items={row['items_total']:.2f}",
            detail=f"Header total ${row['header_total']:.2f} ≠ line items ${row['items_total']:.2f} (Δ${row['delta']:.2f})",
            recommended_action="Recalculate order total from line items"
        ))
        count += 1

    return count


def check_compliance(conn, report: QCReport) -> int:
    """Check 2 — State THC limits, packaging requirements, licensing."""
    count = 0

    # 2a. THC compliance violations on active (non-rejected) orders
    df = pd.read_sql_query("""
        SELECT oi.order_id, oi.sku, oi.product_name,
               oi.thc_per_unit_mg, oi.thc_limit_market,
               o.market, o.status, o.account_name
        FROM order_items oi
        JOIN orders o ON oi.order_id = o.order_id
        WHERE oi.thc_compliance_flag = 1
          AND o.status NOT IN ('Rejected', 'Returned', 'Refusal')
    """, conn)

    for _, row in df.iterrows():
        severity = CRITICAL if row["status"] in ("Invoiced", "Fulfilled") else WARNING
        report.add(QCFlag(
            category="Compliance", severity=severity,
            check_name="THC limit exceeded",
            record_id=row["order_id"], table="order_items",
            field="thc_per_unit_mg",
            value=f"{row['thc_per_unit_mg']}mg (limit: {row['thc_limit_market']}mg)",
            detail=(f"{row['order_id']} — {row['product_name']} ships "
                    f"{row['thc_per_unit_mg']}mg to {row['market']} "
                    f"(limit {row['thc_limit_market']}mg) — status: {row['status']}"),
            recommended_action=(
                "URGENT: Contact distribution to halt shipment"
                if severity == CRITICAL
                else "Review with compliance team before advancing order"
            )
        ))
        count += 1

    # 2b. Expired customer licenses on open orders
    df2 = pd.read_sql_query("""
        SELECT o.order_id, o.status, o.market,
               c.account_name, c.license_number, c.license_expiry
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.status IN ('Pending', 'Processing', 'Fulfilled')
          AND c.license_expiry < DATE('now')
    """, conn)
    for _, row in df2.iterrows():
        report.add(QCFlag(
            category="Compliance", severity=CRITICAL,
            check_name="Expired license on open order",
            record_id=row["order_id"], table="customers",
            field="license_expiry", value=str(row["license_expiry"]),
            detail=(f"{row['account_name']} license expired {row['license_expiry']} "
                    f"— order {row['order_id']} is {row['status']}"),
            recommended_action="Halt order immediately. Obtain updated license before proceeding."
        ))
        count += 1

    # 2c. Orders to markets with requires_state_stamp = True
    #     flagged as needing manual stamp verification
    df3 = pd.read_sql_query("""
        SELECT o.order_id, o.market, o.status, o.account_name
        FROM orders o
        JOIN state_compliance sc ON o.market = sc.market
        WHERE sc.requires_state_stamp = 1
          AND o.status IN ('Pending', 'Processing')
    """, conn)
    for _, row in df3.iterrows():
        report.add(QCFlag(
            category="Compliance", severity=INFO,
            check_name="State stamp required",
            record_id=row["order_id"], table="orders",
            field="market", value=row["market"],
            detail=f"{row['market']} requires state excise stamp — verify before fulfillment",
            recommended_action="Confirm state stamp applied before releasing to distribution"
        ))
        count += 1

    return count


def check_account_health(conn, report: QCReport) -> int:
    """Check 3 — Credit holds, expiring licenses, overdue AR."""
    count = 0

    # 3a. Open orders on accounts with credit holds
    df = pd.read_sql_query("""
        SELECT o.order_id, o.status, o.order_total,
               c.account_name, c.tier, c.market
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE c.on_credit_hold = 1
          AND o.status IN ('Pending', 'Processing', 'Fulfilled')
    """, conn)
    for _, row in df.iterrows():
        report.add(QCFlag(
            category="Account Health", severity=CRITICAL,
            check_name="Open order on credit hold account",
            record_id=row["order_id"], table="customers",
            field="on_credit_hold", value="True",
            detail=(f"{row['account_name']} ({row['tier']}, {row['market']}) "
                    f"is on credit hold — order {row['order_id']} "
                    f"(${row['order_total']:.2f}) is {row['status']}"),
            recommended_action="Reject or hold order. Escalate to Accounting."
        ))
        count += 1

    # 3b. Licenses expiring within 60 days with active orders
    df2 = pd.read_sql_query("""
        SELECT DISTINCT c.customer_id, c.account_name, c.market,
               c.license_expiry, c.tier
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.status NOT IN ('Rejected','Returned','Refusal')
          AND c.license_expiry > DATE('now')
          AND c.license_expiry < DATE('now', '+60 days')
    """, conn)
    for _, row in df2.iterrows():
        report.add(QCFlag(
            category="Account Health", severity=WARNING,
            check_name="License expiring within 60 days",
            record_id=row["customer_id"], table="customers",
            field="license_expiry", value=str(row["license_expiry"]),
            detail=(f"{row['account_name']} ({row['market']}) license expires "
                    f"{row['license_expiry']} — has active orders"),
            recommended_action="Request updated license from account. Alert rep."
        ))
        count += 1

    # 3c. High-value open AR (invoiced > 45 days)
    df3 = pd.read_sql_query("""
        SELECT o.order_id, o.order_total, o.invoice_date,
               o.payment_terms, c.account_name, c.tier, c.market,
               CAST(JULIANDAY('now') - JULIANDAY(o.invoice_date) AS INTEGER)
                   AS days_outstanding
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.status = 'Invoiced'
          AND o.invoice_date IS NOT NULL
          AND JULIANDAY('now') - JULIANDAY(o.invoice_date) > 45
          AND o.order_total > 200
    """, conn)
    for _, row in df3.iterrows():
        report.add(QCFlag(
            category="Account Health", severity=WARNING,
            check_name="Overdue AR (45+ days)",
            record_id=row["order_id"], table="orders",
            field="invoice_date", value=str(row["invoice_date"]),
            detail=(f"{row['account_name']} — ${row['order_total']:.2f} "
                    f"outstanding {row['days_outstanding']} days "
                    f"(terms: {row['payment_terms']})"),
            recommended_action="Flag for Accounting collections follow-up"
        ))
        count += 1

    return count


def check_inventory(conn, report: QCReport) -> int:
    """Check 4 — Stockouts, reorder alerts, allocation overages."""
    count = 0

    df = pd.read_sql_query("""
        SELECT sku, product_name, on_hand_units, allocated_units,
               available_units, reorder_point, below_reorder,
               warehouse_location
        FROM inventory
    """, conn)

    for _, row in df.iterrows():
        # 4a. Out of stock
        if row["available_units"] <= 0:
            report.add(QCFlag(
                category="Inventory", severity=CRITICAL,
                check_name="Out of stock",
                record_id=row["sku"], table="inventory",
                field="available_units", value="0",
                detail=f"{row['product_name']} has 0 available units at {row['warehouse_location']}",
                recommended_action="Trigger emergency reorder. Notify Sales of potential order delays."
            ))
            count += 1

        # 4b. Below reorder point
        elif row["below_reorder"]:
            report.add(QCFlag(
                category="Inventory", severity=WARNING,
                check_name="Below reorder point",
                record_id=row["sku"], table="inventory",
                field="available_units",
                value=f"{row['available_units']} (reorder at {row['reorder_point']})",
                detail=(f"{row['product_name']}: {row['available_units']} available, "
                        f"reorder point is {row['reorder_point']}"),
                recommended_action="Place reorder with production/procurement"
            ))
            count += 1

        # 4c. Allocated exceeds on-hand (data integrity issue)
        if row["allocated_units"] > row["on_hand_units"]:
            report.add(QCFlag(
                category="Inventory", severity=CRITICAL,
                check_name="Allocation exceeds on-hand stock",
                record_id=row["sku"], table="inventory",
                field="allocated_units",
                value=f"allocated={row['allocated_units']}, on_hand={row['on_hand_units']}",
                detail=f"{row['product_name']} has more allocated than physical stock",
                recommended_action="Immediate inventory reconciliation required"
            ))
            count += 1

    return count


def check_financial(conn, report: QCReport) -> int:
    """Check 5 — Pricing anomalies, zero-value lines, negative totals."""
    count = 0

    # 5a. Zero or negative line totals
    df = pd.read_sql_query("""
        SELECT oi.order_id, oi.sku, oi.product_name,
               oi.qty_cases, oi.unit_price, oi.line_total,
               o.status
        FROM order_items oi
        JOIN orders o ON oi.order_id = o.order_id
        WHERE oi.line_total <= 0
    """, conn)
    for _, row in df.iterrows():
        report.add(QCFlag(
            category="Financial", severity=CRITICAL,
            check_name="Zero or negative line total",
            record_id=row["order_id"], table="order_items",
            field="line_total", value=str(row["line_total"]),
            detail=(f"{row['order_id']} — {row['product_name']}: "
                    f"{row['qty_cases']} cases @ ${row['unit_price']:.2f} = ${row['line_total']:.2f}"),
            recommended_action="Investigate pricing or qty data entry error"
        ))
        count += 1

    # 5b. Unit price significantly below wholesale floor (>25% under)
    df2 = pd.read_sql_query("""
        SELECT oi.order_id, oi.sku, oi.product_name,
               oi.unit_price, p.wholesale_price,
               ROUND((p.wholesale_price - oi.unit_price)
                     / p.wholesale_price * 100, 1) AS discount_pct,
               o.status
        FROM order_items oi
        JOIN products p ON oi.sku = p.sku
        JOIN orders o   ON oi.order_id = o.order_id
        WHERE oi.unit_price < p.wholesale_price * 0.75
          AND o.status NOT IN ('Rejected','Returned','Refusal')
    """, conn)
    for _, row in df2.iterrows():
        report.add(QCFlag(
            category="Financial", severity=WARNING,
            check_name="Pricing below floor (>25% discount)",
            record_id=row["order_id"], table="order_items",
            field="unit_price",
            value=f"${row['unit_price']:.2f} vs floor ${row['wholesale_price']:.2f}",
            detail=(f"{row['product_name']} priced at ${row['unit_price']:.2f} "
                    f"({row['discount_pct']}% below wholesale floor)"),
            recommended_action="Verify discount was authorized by Sales Manager"
        ))
        count += 1

    # 5c. Orders with zero total on non-rejected status
    df3 = pd.read_sql_query("""
        SELECT order_id, status, order_total
        FROM orders
        WHERE order_total = 0
          AND status NOT IN ('Rejected','Returned','Refusal')
    """, conn)
    for _, row in df3.iterrows():
        report.add(QCFlag(
            category="Financial", severity=CRITICAL,
            check_name="Zero-value order",
            record_id=row["order_id"], table="orders",
            field="order_total", value="0",
            detail=f"{row['order_id']} has $0.00 total with status {row['status']}",
            recommended_action="Investigate — possible data entry error or missing line items"
        ))
        count += 1

    return count


def check_fulfillment_timing(conn, report: QCReport) -> int:
    """Check 6 — Overdue open orders, stale processing records."""
    count = 0
    today = date.today().isoformat()

    # 6a. Orders open > 14 days
    df = pd.read_sql_query(f"""
        SELECT order_id, status, order_date, account_name,
               market, order_total,
               CAST(JULIANDAY('{today}') - JULIANDAY(order_date)
                    AS INTEGER) AS days_open
        FROM orders
        WHERE status IN ('Pending', 'Processing')
          AND JULIANDAY('{today}') - JULIANDAY(order_date) > 14
    """, conn)
    for _, row in df.iterrows():
        severity = CRITICAL if row["days_open"] > 30 else WARNING
        report.add(QCFlag(
            category="Fulfillment Timing", severity=severity,
            check_name=f"Order open > {'30' if severity == CRITICAL else '14'} days",
            record_id=row["order_id"], table="orders",
            field="order_date", value=str(row["order_date"]),
            detail=(f"{row['order_id']} has been {row['status']} for "
                    f"{row['days_open']} days "
                    f"(${row['order_total']:.2f}, {row['market']})"),
            recommended_action="Contact rep and distribution to investigate delay"
        ))
        count += 1

    # 6b. Fulfilled orders not invoiced within 3 days
    df2 = pd.read_sql_query(f"""
        SELECT order_id, status, fulfillment_date, account_name,
               order_total, payment_terms,
               CAST(JULIANDAY('{today}') - JULIANDAY(fulfillment_date)
                    AS INTEGER) AS days_since_fulfillment
        FROM orders
        WHERE status = 'Fulfilled'
          AND fulfillment_date IS NOT NULL
          AND JULIANDAY('{today}') - JULIANDAY(fulfillment_date) > 3
    """, conn)
    for _, row in df2.iterrows():
        report.add(QCFlag(
            category="Fulfillment Timing", severity=WARNING,
            check_name="Fulfilled but not invoiced (3+ days)",
            record_id=row["order_id"], table="orders",
            field="invoice_date", value=None,
            detail=(f"{row['order_id']} fulfilled {row['fulfillment_date']} "
                    f"({row['days_since_fulfillment']} days ago) "
                    f"— not yet invoiced (terms: {row['payment_terms']})"),
            recommended_action="Issue invoice immediately to start payment clock"
        ))
        count += 1

    return count


def check_duplicates(conn, report: QCReport) -> int:
    """Check 7 — Potential duplicate orders (same account + date + total)."""
    count = 0

    df = pd.read_sql_query("""
        SELECT customer_id, order_date, order_total,
               COUNT(*) AS order_count,
               GROUP_CONCAT(order_id, ', ') AS order_ids
        FROM orders
        WHERE status NOT IN ('Rejected', 'Returned', 'Refusal')
        GROUP BY customer_id, order_date, order_total
        HAVING COUNT(*) > 1
    """, conn)
    for _, row in df.iterrows():
        report.add(QCFlag(
            category="Duplicate Detection", severity=WARNING,
            check_name="Potential duplicate orders",
            record_id=row["order_ids"], table="orders",
            field="order_date",
            value=f"{row['order_date']} / ${row['order_total']:.2f}",
            detail=(f"Customer {row['customer_id']} has {row['order_count']} "
                    f"orders on {row['order_date']} for ${row['order_total']:.2f}: "
                    f"{row['order_ids']}"),
            recommended_action="Verify with rep whether both orders are intentional"
        ))
        count += 1

    return count


# ---------------------------------------------------------------------------
# Check registry
# ---------------------------------------------------------------------------

ALL_CHECKS = {
    "order_integrity":    check_order_integrity,
    "compliance":         check_compliance,
    "account_health":     check_account_health,
    "inventory":          check_inventory,
    "financial":          check_financial,
    "fulfillment_timing": check_fulfillment_timing,
    "duplicates":         check_duplicates,
}


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_checks(
    category_filter: Optional[str] = None,
    severity_filter: Optional[str] = None,
) -> QCReport:
    conn   = get_connection()
    report = QCReport()

    checks = ALL_CHECKS
    if category_filter:
        checks = {k: v for k, v in ALL_CHECKS.items()
                  if k == category_filter.lower().replace(" ", "_")}

    print("\n Wyld Sales Ops — Quality Check")
    print("=" * 42)
    print(f"  Run date: {report.run_date}")
    print(f"  Checks:   {', '.join(checks.keys())}\n")

    for name, fn in checks.items():
        n = fn(conn, report)
        print(f"  {name:<22} {n:>4} flags")
        report.checks_run += 1

    conn.close()

    # Apply severity filter after all checks
    if severity_filter:
        report.flags = [f for f in report.flags
                        if f.severity == severity_filter.upper()]

    return report


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

QC_REPORT_CSV  = Path("data/qc_report.csv")
QC_SUMMARY_CSV = Path("data/qc_summary.csv")


def save_outputs(report: QCReport) -> None:
    detail_df  = report.to_dataframe()
    summary_df = report.summary()

    detail_df.to_csv(QC_REPORT_CSV,  index=False)
    summary_df.to_csv(QC_SUMMARY_CSV, index=False)

    print(f"\n  Saved → {QC_REPORT_CSV}  ({len(detail_df)} flags)")
    print(f"  Saved → {QC_SUMMARY_CSV} ({len(summary_df)} check categories)")


def print_report(report: QCReport, severity_filter: Optional[str] = None) -> None:
    print("\n" + "=" * 62)
    print("  QC REPORT SUMMARY")
    print("=" * 62)
    print(f"  Total flags:  {len(report.flags)}")
    print(f"  ● CRITICAL:  {report.critical_count}")
    print(f"  ▲ WARNING:   {report.warning_count}")
    print(f"  ℹ INFO:      {report.info_count}")

    # Print critical flags in full
    criticals = [f for f in report.flags if f.severity == CRITICAL]
    if criticals:
        print(f"\n  ── CRITICAL FLAGS ({len(criticals)}) ──")
        for f in criticals[:20]:   # cap at 20 for readability
            print(f"  [{f.category}] {f.check_name}")
            print(f"    Record: {f.record_id}")
            print(f"    Detail: {f.detail}")
            print(f"    Action: {f.recommended_action}\n")

    # Summary table by category
    summary = report.summary()
    if not summary.empty:
        print("\n  ── FLAGS BY CATEGORY ──")
        print(summary.to_string(index=False))

    print("\n" + "=" * 62)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Wyld Sales Ops — Data Quality Checker"
    )
    parser.add_argument("--category", type=str, default=None,
                        choices=list(ALL_CHECKS.keys()),
                        help="Run a single check category")
    parser.add_argument("--severity", type=str, default=None,
                        choices=["CRITICAL", "WARNING", "INFO"],
                        help="Filter output by severity")
    parser.add_argument("--export-excel", action="store_true",
                        help="Append QC sheet to Excel workbook (requires report.py)")
    args = parser.parse_args()

    report = run_checks(
        category_filter=args.category,
        severity_filter=args.severity,
    )

    print_report(report, args.severity)
    save_outputs(report)

    # Exit code signals CI/monitoring tools
    import sys
    sys.exit(1 if report.critical_count > 0 else 0)


if __name__ == "__main__":
    main()
