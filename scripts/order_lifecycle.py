"""
order_lifecycle.py
==================
Wyld Sales Operations — Order Lifecycle Manager

Simulates and manages the full B2B sales order lifecycle:

    Pending → Processing → Fulfilled → Invoiced
                       ↘ Rejected
                       ↘ Returned  (post-fulfillment)
                       ↘ Refusal   (delivery refused at door)

Key responsibilities mirroring the actual job description:
  - Order entry validation (license, credit hold, minimums, compliance)
  - Order modification (additions, edits, rejections)
  - Return & refusal processing with credit memo generation
  - State-specific compliance enforcement per Wyld's 17 US states + Canada
  - Full audit trail written to order_events.csv + order_events table in DB

Usage:
    python order_lifecycle.py               # process all open orders
    python order_lifecycle.py --order ORD-00001  # process single order
    python order_lifecycle.py --report      # print lifecycle summary
"""

import argparse
import sqlite3
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd

from database import DB_PATH, get_connection, query

# ---------------------------------------------------------------------------
# Status constants
# ---------------------------------------------------------------------------

STATUS_PENDING     = "Pending"
STATUS_PROCESSING  = "Processing"
STATUS_FULFILLED   = "Fulfilled"
STATUS_INVOICED    = "Invoiced"
STATUS_REJECTED    = "Rejected"
STATUS_RETURNED    = "Returned"
STATUS_REFUSAL     = "Refusal"

TERMINAL_STATUSES = {STATUS_INVOICED, STATUS_REJECTED,
                     STATUS_RETURNED, STATUS_REFUSAL}

# Valid forward transitions in the lifecycle state machine
VALID_TRANSITIONS = {
    STATUS_PENDING:    [STATUS_PROCESSING, STATUS_REJECTED],
    STATUS_PROCESSING: [STATUS_FULFILLED,  STATUS_REJECTED],
    STATUS_FULFILLED:  [STATUS_INVOICED,   STATUS_RETURNED, STATUS_REFUSAL],
    STATUS_INVOICED:   [STATUS_RETURNED],   # post-invoice returns allowed
}

# ---------------------------------------------------------------------------
# Validation rules
# ---------------------------------------------------------------------------

class OrderValidationError(Exception):
    """Raised when an order fails a compliance or business rule check."""
    pass


def validate_license(customer: sqlite3.Row) -> None:
    """Reject if customer license is expired."""
    expiry = customer["license_expiry"]
    if expiry and date.fromisoformat(str(expiry)) < date.today():
        raise OrderValidationError(
            f"License expired: {expiry} for account {customer['account_name']}"
        )


def validate_credit_hold(customer: sqlite3.Row) -> None:
    """Reject if account is on credit hold."""
    if customer["on_credit_hold"]:
        raise OrderValidationError(
            f"Account on credit hold: {customer['account_name']}"
        )


def validate_order_minimum(
    customer: sqlite3.Row, items: list[dict]
) -> None:
    """Reject if total cases fall below account minimum."""
    total_cases = sum(i["qty_cases"] for i in items)
    minimum     = customer["min_order_cases"] or 0
    if total_cases < minimum:
        raise OrderValidationError(
            f"Order minimum not met: {total_cases} cases ordered, "
            f"{minimum} required for {customer['tier']} tier"
        )


def validate_thc_compliance(
    items: list[dict], compliance: sqlite3.Row
) -> list[str]:
    """
    Return a list of THC compliance warnings.
    Does NOT raise — compliance flags are logged but orders may still
    proceed depending on state rules (some states allow with proper docs).
    """
    warnings = []
    limit = compliance["thc_per_unit_limit_mg"]
    for item in items:
        if item["thc_per_unit_mg"] > limit:
            warnings.append(
                f"SKU {item['sku']} ({item['product_name']}): "
                f"{item['thc_per_unit_mg']}mg/unit exceeds {limit}mg limit "
                f"for {compliance['market']}"
            )
    return warnings


def validate_cold_chain(items: list[dict], channel: str) -> list[str]:
    """Warn if cold-chain items are routed through non-cold channels."""
    warnings = []
    cold_skus = [i["product_name"] for i in items if i["cold_chain_required"]]
    if cold_skus and channel == "Platform":
        warnings.append(
            f"Cold chain required for {cold_skus} but channel is 'Platform' "
            f"— verify cold storage compliance"
        )
    return warnings


# ---------------------------------------------------------------------------
# Audit event logging
# ---------------------------------------------------------------------------

EVENTS_CSV = Path("data/order_events.csv")

_event_buffer: list[dict] = []


def log_event(
    order_id: str,
    event_type: str,
    from_status: Optional[str],
    to_status: Optional[str],
    detail: str,
    performed_by: str = "system",
) -> None:
    """
    Append an event to the in-memory buffer.
    Call flush_events() to persist to CSV + DB.
    """
    _event_buffer.append({
        "event_id":      f"EVT-{len(_event_buffer)+1:06d}",
        "order_id":      order_id,
        "event_type":    event_type,
        "from_status":   from_status,
        "to_status":     to_status,
        "detail":        detail,
        "performed_by":  performed_by,
        "timestamp":     datetime.now().isoformat(timespec="seconds"),
    })


def flush_events(conn: sqlite3.Connection) -> int:
    """Write buffered events to CSV and DB. Returns count written."""
    if not _event_buffer:
        return 0

    df = pd.DataFrame(_event_buffer)

    # CSV (append if exists)
    if EVENTS_CSV.exists():
        df.to_csv(EVENTS_CSV, mode="a", header=False, index=False)
    else:
        df.to_csv(EVENTS_CSV, index=False)

    # DB table (create on first write)
    df.to_sql("order_events", conn, if_exists="append", index=False)
    conn.commit()

    count = len(_event_buffer)
    _event_buffer.clear()
    return count


# ---------------------------------------------------------------------------
# Credit memo generation
# ---------------------------------------------------------------------------

def generate_credit_memo(
    order_id: str,
    order_total: float,
    reason: str,
    partial_amount: Optional[float] = None,
) -> dict:
    """
    Generate a credit memo record for returns / refusals.
    Returns a dict suitable for the credit_memos table/CSV.
    """
    memo_amount = partial_amount if partial_amount else order_total
    return {
        "memo_id":       f"CM-{order_id}",
        "order_id":      order_id,
        "memo_date":     date.today().isoformat(),
        "memo_amount":   round(memo_amount, 2),
        "reason":        reason,
        "status":        "Issued",
        "applied_to_ar": False,
    }


CREDIT_MEMOS_CSV = Path("data/credit_memos.csv")


def save_credit_memos(memos: list[dict], conn: sqlite3.Connection) -> None:
    if not memos:
        return
    df = pd.DataFrame(memos)
    if CREDIT_MEMOS_CSV.exists():
        df.to_csv(CREDIT_MEMOS_CSV, mode="a", header=False, index=False)
    else:
        df.to_csv(CREDIT_MEMOS_CSV, index=False)
    df.to_sql("credit_memos", conn, if_exists="append", index=False)
    conn.commit()


# ---------------------------------------------------------------------------
# Core lifecycle engine
# ---------------------------------------------------------------------------

class OrderLifecycleManager:
    """
    Manages order state transitions with full validation, audit logging,
    and compliance enforcement.
    """

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    # -- Data fetchers -------------------------------------------------------

    def _get_order(self, order_id: str) -> sqlite3.Row:
        cur = self.conn.execute(
            "SELECT * FROM orders WHERE order_id = ?", (order_id,)
        )
        row = cur.fetchone()
        if not row:
            raise ValueError(f"Order not found: {order_id}")
        return row

    def _get_customer(self, customer_id: str) -> sqlite3.Row:
        cur = self.conn.execute(
            "SELECT * FROM customers WHERE customer_id = ?", (customer_id,)
        )
        return cur.fetchone()

    def _get_items(self, order_id: str) -> list[dict]:
        cur = self.conn.execute(
            "SELECT * FROM order_items WHERE order_id = ?", (order_id,)
        )
        return [dict(r) for r in cur.fetchall()]

    def _get_compliance(self, market: str) -> sqlite3.Row:
        cur = self.conn.execute(
            "SELECT * FROM state_compliance WHERE market = ?", (market,)
        )
        return cur.fetchone()

    # -- State machine -------------------------------------------------------

    def _assert_valid_transition(
        self, order_id: str, from_status: str, to_status: str
    ) -> None:
        if from_status in TERMINAL_STATUSES:
            raise OrderValidationError(
                f"Order {order_id} is in terminal status '{from_status}' "
                f"— no further transitions allowed"
            )
        allowed = VALID_TRANSITIONS.get(from_status, [])
        if to_status not in allowed:
            raise OrderValidationError(
                f"Invalid transition for {order_id}: "
                f"'{from_status}' → '{to_status}'. "
                f"Allowed: {allowed}"
            )

    def _update_order_status(
        self,
        order_id: str,
        new_status: str,
        rejection_reason: Optional[str] = None,
        fulfillment_date: Optional[str] = None,
        invoice_date: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> None:
        self.conn.execute(
            """UPDATE orders SET
                status           = ?,
                rejection_reason = COALESCE(?, rejection_reason),
                fulfillment_date = COALESCE(?, fulfillment_date),
                invoice_date     = COALESCE(?, invoice_date),
                notes            = COALESCE(?, notes)
               WHERE order_id = ?""",
            (new_status, rejection_reason, fulfillment_date,
             invoice_date, notes, order_id),
        )
        self.conn.commit()

    # -- Lifecycle transitions -----------------------------------------------

    def advance_to_processing(self, order_id: str) -> dict:
        """
        Pending → Processing
        Runs full validation: license, credit hold, order minimum, compliance.
        """
        order    = self._get_order(order_id)
        customer = self._get_customer(order["customer_id"])
        items    = self._get_items(order_id)
        comp     = self._get_compliance(order["market"])

        self._assert_valid_transition(order_id, order["status"], STATUS_PROCESSING)

        warnings = []
        try:
            validate_license(customer)
            validate_credit_hold(customer)
            validate_order_minimum(customer, items)
        except OrderValidationError as exc:
            # Hard failure → reject immediately
            return self.reject_order(order_id, str(exc))

        # Soft warnings — log but allow to proceed
        warnings += validate_thc_compliance(items, comp)
        warnings += validate_cold_chain(items, order["distribution_channel"])

        self._update_order_status(order_id, STATUS_PROCESSING)

        detail = "Order validated and moved to Processing"
        if warnings:
            detail += " | WARNINGS: " + "; ".join(warnings)

        log_event(order_id, "STATUS_CHANGE", STATUS_PENDING,
                  STATUS_PROCESSING, detail)
        return {"order_id": order_id, "status": STATUS_PROCESSING,
                "warnings": warnings}

    def fulfill_order(self, order_id: str) -> dict:
        """
        Processing → Fulfilled
        Checks inventory availability before confirming fulfillment.
        """
        order = self._get_order(order_id)
        items = self._get_items(order_id)

        self._assert_valid_transition(order_id, order["status"], STATUS_FULFILLED)

        # Inventory check
        shortfalls = []
        for item in items:
            cur = self.conn.execute(
                "SELECT available_units FROM inventory WHERE sku = ?",
                (item["sku"],)
            )
            row = cur.fetchone()
            if row and row["available_units"] < item["qty_cases"]:
                shortfalls.append(
                    f"{item['sku']}: need {item['qty_cases']}, "
                    f"have {row['available_units']}"
                )

        today = date.today().isoformat()
        self._update_order_status(
            order_id, STATUS_FULFILLED, fulfillment_date=today
        )

        detail = f"Order fulfilled on {today}"
        if shortfalls:
            detail += " | INVENTORY SHORTFALLS: " + "; ".join(shortfalls)

        log_event(order_id, "STATUS_CHANGE", STATUS_PROCESSING,
                  STATUS_FULFILLED, detail)
        return {"order_id": order_id, "status": STATUS_FULFILLED,
                "shortfalls": shortfalls}

    def invoice_order(self, order_id: str) -> dict:
        """
        Fulfilled → Invoiced
        Stamps invoice date and locks the order for AR.
        """
        order = self._get_order(order_id)
        self._assert_valid_transition(order_id, order["status"], STATUS_INVOICED)

        today = date.today().isoformat()
        self._update_order_status(
            order_id, STATUS_INVOICED, invoice_date=today
        )
        log_event(order_id, "STATUS_CHANGE", STATUS_FULFILLED,
                  STATUS_INVOICED,
                  f"Invoice issued on {today} — "
                  f"terms: {order['payment_terms']}")
        return {"order_id": order_id, "status": STATUS_INVOICED,
                "invoice_date": today}

    def reject_order(self, order_id: str, reason: str) -> dict:
        """
        Pending/Processing → Rejected
        Records rejection reason; no credit memo needed (never shipped).
        """
        order = self._get_order(order_id)
        from_status = order["status"]

        # Allow rejection from Pending or Processing only
        if from_status not in (STATUS_PENDING, STATUS_PROCESSING):
            raise OrderValidationError(
                f"Cannot reject order {order_id} in status '{from_status}'"
            )

        self._update_order_status(
            order_id, STATUS_REJECTED, rejection_reason=reason
        )
        log_event(order_id, "REJECTION", from_status,
                  STATUS_REJECTED, f"Rejected: {reason}")
        return {"order_id": order_id, "status": STATUS_REJECTED,
                "reason": reason}

    def return_order(
        self,
        order_id: str,
        reason: str,
        partial_amount: Optional[float] = None,
    ) -> dict:
        """
        Fulfilled/Invoiced → Returned
        Generates a credit memo for the return amount.
        """
        order = self._get_order(order_id)
        self._assert_valid_transition(order_id, order["status"], STATUS_RETURNED)

        memo = generate_credit_memo(
            order_id, order["order_total"], reason, partial_amount
        )
        save_credit_memos([memo], self.conn)

        self._update_order_status(
            order_id, STATUS_RETURNED,
            notes=f"Return: {reason} | Credit memo: {memo['memo_id']}"
        )
        log_event(order_id, "RETURN", order["status"],
                  STATUS_RETURNED,
                  f"Return processed: {reason} | "
                  f"Credit memo {memo['memo_id']} for ${memo['memo_amount']:.2f}")
        return {"order_id": order_id, "status": STATUS_RETURNED,
                "credit_memo": memo}

    def process_refusal(self, order_id: str, reason: str) -> dict:
        """
        Fulfilled → Refusal (delivery refused at point of delivery)
        Generates a credit memo and flags for re-delivery or write-off.
        """
        order = self._get_order(order_id)
        self._assert_valid_transition(order_id, order["status"], STATUS_REFUSAL)

        memo = generate_credit_memo(
            order_id, order["order_total"],
            f"Delivery refusal: {reason}"
        )
        save_credit_memos([memo], self.conn)

        self._update_order_status(
            order_id, STATUS_REFUSAL,
            notes=f"Refusal at delivery: {reason} | "
                  f"Credit memo: {memo['memo_id']}"
        )
        log_event(order_id, "REFUSAL", STATUS_FULFILLED,
                  STATUS_REFUSAL,
                  f"Delivery refused: {reason} | "
                  f"Credit memo {memo['memo_id']} for ${memo['memo_amount']:.2f}")
        return {"order_id": order_id, "status": STATUS_REFUSAL,
                "credit_memo": memo}

    def modify_order(
        self,
        order_id: str,
        changes: dict,
    ) -> dict:
        """
        Edit an order (Pending or Processing only).
        Supported changes: qty adjustments, notes, po_number.
        Re-validates after modification.
        """
        order = self._get_order(order_id)
        if order["status"] not in (STATUS_PENDING, STATUS_PROCESSING):
            raise OrderValidationError(
                f"Order {order_id} cannot be modified in status '{order['status']}'"
            )

        change_log = []
        if "notes" in changes:
            self.conn.execute(
                "UPDATE orders SET notes = ? WHERE order_id = ?",
                (changes["notes"], order_id)
            )
            change_log.append(f"notes updated")

        if "po_number" in changes:
            self.conn.execute(
                "UPDATE orders SET po_number = ? WHERE order_id = ?",
                (changes["po_number"], order_id)
            )
            change_log.append(f"PO# set to {changes['po_number']}")

        # Qty adjustments — recalculate order total
        if "qty_adjustments" in changes:
            new_total = 0.0
            for sku, new_qty in changes["qty_adjustments"].items():
                self.conn.execute(
                    """UPDATE order_items
                       SET qty_cases  = ?,
                           line_total = qty_cases * unit_price
                       WHERE order_id = ? AND sku = ?""",
                    (new_qty, order_id, sku)
                )
                change_log.append(f"{sku} qty → {new_qty}")
            # Recalculate order total from line items
            cur = self.conn.execute(
                "SELECT SUM(line_total) FROM order_items WHERE order_id = ?",
                (order_id,)
            )
            new_total = cur.fetchone()[0] or 0.0
            self.conn.execute(
                "UPDATE orders SET order_total = ? WHERE order_id = ?",
                (round(new_total, 2), order_id)
            )

        self.conn.commit()
        log_event(order_id, "MODIFICATION", order["status"], order["status"],
                  "Order modified: " + "; ".join(change_log))
        return {"order_id": order_id, "status": order["status"],
                "changes": change_log}


# ---------------------------------------------------------------------------
# Batch processor — advance all open orders one step
# ---------------------------------------------------------------------------

def process_open_orders(conn: sqlite3.Connection) -> dict:
    """
    Advance all Pending and Processing orders through the lifecycle.
    Simulates a nightly batch run — the kind of job a Sales Data
    Coordinator would monitor and exception-handle each morning.
    """
    mgr = OrderLifecycleManager(conn)

    pending_df    = pd.read_sql_query(
        "SELECT order_id FROM orders WHERE status = 'Pending'", conn
    )
    processing_df = pd.read_sql_query(
        "SELECT order_id FROM orders WHERE status = 'Processing'", conn
    )

    results = {"advanced": 0, "rejected": 0, "warnings": 0, "errors": 0}

    print(f"\n  Processing {len(pending_df)} Pending orders...")
    for order_id in pending_df["order_id"]:
        try:
            result = mgr.advance_to_processing(order_id)
            if result["status"] == STATUS_REJECTED:
                results["rejected"] += 1
            else:
                results["advanced"] += 1
                if result.get("warnings"):
                    results["warnings"] += 1
        except Exception as exc:
            results["errors"] += 1
            print(f"    ERROR {order_id}: {exc}")

    print(f"  Processing {len(processing_df)} Processing orders...")
    for order_id in processing_df["order_id"]:
        try:
            result = mgr.fulfill_order(order_id)
            results["advanced"] += 1
            if result.get("shortfalls"):
                results["warnings"] += 1
        except Exception as exc:
            results["errors"] += 1
            print(f"    ERROR {order_id}: {exc}")

    n_events = flush_events(conn)
    print(f"  Flushed {n_events} audit events")
    return results


# ---------------------------------------------------------------------------
# Lifecycle summary report
# ---------------------------------------------------------------------------

def print_lifecycle_report(conn: sqlite3.Connection) -> None:
    print("\n" + "=" * 62)
    print("  ORDER LIFECYCLE REPORT")
    print("=" * 62)

    # Status distribution
    df = pd.read_sql_query("""
        SELECT status,
               COUNT(*)                        AS orders,
               ROUND(SUM(order_total), 2)      AS total_value,
               ROUND(AVG(order_total), 2)      AS avg_value
        FROM orders
        GROUP BY status ORDER BY orders DESC
    """, conn)
    print("\n  Status distribution:")
    print(df.to_string(index=False, float_format=lambda x: f"{x:,.2f}"))

    # Rejection breakdown
    df2 = pd.read_sql_query("""
        SELECT rejection_reason,
               COUNT(*) AS count
        FROM orders
        WHERE status = 'Rejected'
          AND rejection_reason IS NOT NULL
        GROUP BY rejection_reason
        ORDER BY count DESC
    """, conn)
    print("\n  Rejection reasons:")
    print(df2.to_string(index=False))

    # Avg fulfillment time by market
    df3 = pd.read_sql_query("""
        SELECT market,
               COUNT(*) AS fulfilled_orders,
               ROUND(AVG(JULIANDAY(fulfillment_date)
                         - JULIANDAY(order_date)), 1) AS avg_days_to_fulfill
        FROM orders
        WHERE fulfillment_date IS NOT NULL
        GROUP BY market
        ORDER BY avg_days_to_fulfill DESC
        LIMIT 10
    """, conn)
    print("\n  Avg days to fulfill by market (top 10):")
    print(df3.to_string(index=False))

    # Credit memos
    if Path("data/credit_memos.csv").exists():
        memo_df = pd.read_csv("data/credit_memos.csv")
        print(f"\n  Credit memos issued: {len(memo_df)}")
        print(f"  Total credit value:  ${memo_df['memo_amount'].sum():,.2f}")

    # Audit events
    if Path("data/order_events.csv").exists():
        ev_df = pd.read_csv("data/order_events.csv")
        print(f"\n  Audit events logged: {len(ev_df)}")
        breakdown = ev_df["event_type"].value_counts()
        for evt, cnt in breakdown.items():
            print(f"    {evt:<20} {cnt}")

    print("\n" + "=" * 62)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Wyld Sales Ops — Order Lifecycle Manager"
    )
    parser.add_argument("--order",   type=str, help="Process a single order ID")
    parser.add_argument("--report",  action="store_true", help="Print lifecycle report")
    parser.add_argument("--action",  type=str,
                        choices=["process", "fulfill", "invoice",
                                 "reject", "return", "refusal"],
                        default="process",
                        help="Action to take on --order (default: process)")
    parser.add_argument("--reason",  type=str, default="Customer request",
                        help="Reason for reject/return/refusal")
    args = parser.parse_args()

    print("\n Wyld Sales Ops — Order Lifecycle Manager")
    print("=" * 42)

    conn = get_connection()
    mgr  = OrderLifecycleManager(conn)

    if args.order:
        order_id = args.order.upper()
        try:
            if args.action == "process":
                result = mgr.advance_to_processing(order_id)
            elif args.action == "fulfill":
                result = mgr.fulfill_order(order_id)
            elif args.action == "invoice":
                result = mgr.invoice_order(order_id)
            elif args.action == "reject":
                result = mgr.reject_order(order_id, args.reason)
            elif args.action == "return":
                result = mgr.return_order(order_id, args.reason)
            elif args.action == "refusal":
                result = mgr.process_refusal(order_id, args.reason)

            flush_events(conn)
            print(f"\n  Result: {result}")
        except (OrderValidationError, ValueError) as exc:
            print(f"\n  ERROR: {exc}")

    elif args.report:
        print_lifecycle_report(conn)

    else:
        # Default: run batch processor on all open orders
        results = process_open_orders(conn)
        print(f"\n  Batch complete:")
        print(f"    Advanced:  {results['advanced']}")
        print(f"    Rejected:  {results['rejected']}")
        print(f"    Warnings:  {results['warnings']}")
        print(f"    Errors:    {results['errors']}")
        print_lifecycle_report(conn)

    conn.close()


if __name__ == "__main__":
    main()
