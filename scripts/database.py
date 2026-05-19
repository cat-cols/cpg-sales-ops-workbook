"""
database.py
===========
Myld Sales Operations — Database Layer

Loads all CSV data into a SQLite database, applies the schema
(tables, indexes, views), and exposes a clean query interface used
by every downstream module.

Usage:
    python database.py              # build DB, run validation report
    python database.py --rebuild    # drop and rebuild from scratch
    python database.py --query "SELECT * FROM vw_revenue_by_market LIMIT 5"
"""

import argparse
import sqlite3
import textwrap
from pathlib import Path

import pandas as pd

DB_PATH   = Path("myld_sales.db")
SCHEMA = Path(__file__).parent.parent / "sql" / "schema.sql"
DATA_DIR = Path(__file__).parent.parent / "data"

# CSV → table name mapping (load order respects FK dependencies)
CSV_TABLES = [
    ("products.csv",         "products"),
    ("sales_reps.csv",       "sales_reps"),
    ("customers.csv",        "customers"),
    ("inventory.csv",        "inventory"),
    ("state_compliance.csv", "state_compliance"),
    ("orders.csv",           "orders"),
    ("order_items.csv",      "order_items"),
]

# ---------------------------------------------------------------------------
# Connection helper
# ---------------------------------------------------------------------------

def get_connection(db_path: Path = DB_PATH) -> sqlite3.Connection:
    """
    Return a SQLite connection with foreign keys enabled and
    row_factory set so results are accessible by column name.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA journal_mode = WAL;")
    return conn


# ---------------------------------------------------------------------------
# Build / rebuild
# ---------------------------------------------------------------------------

def apply_schema(conn: sqlite3.Connection) -> None:
    """Execute schema.sql — creates tables, indexes, views."""
    sql = SCHEMA.read_text()
    conn.executescript(sql)
    conn.commit()
    print("  Schema applied (tables, indexes, views)")


def load_csv(conn: sqlite3.Connection, csv_name: str, table: str) -> int:
    """
    Load a CSV into a table using pandas → to_sql (append mode).
    Booleans from pandas are converted to 0/1 for SQLite.
    Returns row count inserted.
    """
    path = DATA_DIR / csv_name
    df   = pd.read_csv(path)

    # Normalise booleans → integers for SQLite
    for col in df.select_dtypes(include="bool").columns:
        df[col] = df[col].astype(int)

    df.to_sql(table, conn, if_exists="append", index=False)
    return len(df)


def build_database(rebuild: bool = False) -> sqlite3.Connection:
    """
    Build (or rebuild) the SQLite database from CSVs.
    Returns an open connection.
    """
    if rebuild and DB_PATH.exists():
        DB_PATH.unlink()
        print(f"  Dropped existing database: {DB_PATH}")

    conn = get_connection()
    apply_schema(conn)

    print("\n  Loading CSVs into database:")
    total_rows = 0
    for csv_name, table in CSV_TABLES:
        n = load_csv(conn, csv_name, table)
        total_rows += n
        print(f"    {table:<20} {n:>5} rows  ←  {csv_name}")

    conn.commit()
    print(f"\n  Total rows loaded: {total_rows:,}")
    return conn


# ---------------------------------------------------------------------------
# Validation queries — run after load to confirm integrity
# ---------------------------------------------------------------------------

VALIDATION_QUERIES = {
    "Order status breakdown": """
        SELECT status, COUNT(*) AS orders,
               ROUND(SUM(order_total), 2) AS total_value
        FROM orders
        GROUP BY status
        ORDER BY orders DESC
    """,

    "Revenue by top 5 markets": """
        SELECT market, total_orders, total_revenue, invoice_rate_pct
        FROM vw_revenue_by_market
        ORDER BY total_revenue DESC
        LIMIT 5
    """,

    "Rep performance summary": """
        SELECT rep_name, region, total_orders, total_revenue,
               avg_order_value, invoice_rate_pct
        FROM vw_revenue_by_rep
        ORDER BY total_revenue DESC
    """,

    "Top 5 SKUs by revenue": """
        SELECT pp.sku, pp.product_name, pp.total_cases_sold,
               pp.total_revenue, pp.flag_rate_pct, iv.stock_status
        FROM vw_product_performance pp
        JOIN vw_inventory_status iv ON pp.sku = iv.sku
        ORDER BY pp.total_revenue DESC
        LIMIT 5
    """,

    "Compliance flags by market": """
        SELECT market, COUNT(*) AS flagged_line_items,
               ROUND(SUM(line_total), 2) AS flagged_value,
               ROUND(AVG(thc_overage_mg), 2) AS avg_overage_mg
        FROM vw_compliance_flags
        GROUP BY market
        ORDER BY flagged_line_items DESC
        LIMIT 8
    """,

    "Accounts on credit hold": """
        SELECT account_name, tier, market, credit_limit,
               lifetime_revenue, open_ar_amount, license_status
        FROM vw_account_health
        WHERE on_credit_hold = 1
        ORDER BY lifetime_revenue DESC
    """,

    "Inventory reorder alerts": """
        SELECT sku, product_name, available_units,
               reorder_point, stock_status, warehouse_location
        FROM vw_inventory_status
        WHERE stock_status IN ('OUT OF STOCK', 'REORDER NOW', 'LOW STOCK')
        ORDER BY available_units ASC
    """,

    "Open orders pending action": """
        SELECT order_id, account_name, tier, market,
               status, days_open, order_total,
               on_credit_hold, has_compliance_flag
        FROM vw_open_orders
        ORDER BY days_open DESC
        LIMIT 10
    """,

    "AR aging summary": """
        SELECT ar_aging_bucket,
               COUNT(*)                          AS invoices,
               ROUND(SUM(order_total), 2)        AS total_value
        FROM vw_order_summary
        WHERE status = 'Invoiced'
        GROUP BY ar_aging_bucket
        ORDER BY
          CASE ar_aging_bucket
            WHEN 'Current'    THEN 1
            WHEN '16-30 days' THEN 2
            WHEN '31-45 days' THEN 3
            WHEN '46-60 days' THEN 4
            WHEN '60+ days'   THEN 5
            ELSE 6
          END
    """,

    "Monthly revenue trend (2024)": """
        SELECT SUBSTR(order_date, 1, 7)           AS month,
               COUNT(*)                           AS orders,
               ROUND(SUM(order_total), 2)         AS revenue
        FROM orders
        WHERE status IN ('Invoiced', 'Fulfilled')
          AND order_date >= '2024-01-01'
          AND order_date <  '2025-01-01'
        GROUP BY month
        ORDER BY month
    """,
}


def run_validation(conn: sqlite3.Connection) -> None:
    """Run all validation queries and print formatted results."""
    print("\n" + "=" * 62)
    print("  DATABASE VALIDATION REPORT")
    print("=" * 62)

    for title, sql in VALIDATION_QUERIES.items():
        print(f"\n  ── {title} ──")
        try:
            df = pd.read_sql_query(textwrap.dedent(sql), conn)
            if df.empty:
                print("    (no rows)")
            else:
                # Pretty-print with truncated column widths
                print(df.to_string(index=False, max_colwidth=28,
                                   float_format=lambda x: f"{x:,.2f}"))
        except Exception as exc:
            print(f"    ERROR: {exc}")

    print("\n" + "=" * 62)


# ---------------------------------------------------------------------------
# Query helper — used by downstream modules
# ---------------------------------------------------------------------------

def query(sql: str, params: tuple = (),
          db_path: Path = DB_PATH) -> pd.DataFrame:
    """
    Execute a SQL query and return a DataFrame.
    Convenience wrapper for use in pipeline, reporting, dashboard modules.

    Example:
        from database import query
        df = query("SELECT * FROM vw_revenue_by_market WHERE is_canada = 0")
    """
    with get_connection(db_path) as conn:
        return pd.read_sql_query(sql, conn, params=params)


def table_exists(conn: sqlite3.Connection, name: str) -> bool:
    """Check whether a table or view exists in the database."""
    cur = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type IN ('table','view') AND name = ?",
        (name,)
    )
    return cur.fetchone() is not None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Myld Sales Ops — database builder")
    parser.add_argument("--rebuild", action="store_true",
                        help="Drop and recreate the database from scratch")
    parser.add_argument("--query", type=str, default=None,
                        help="Run a custom SQL query and print results")
    parser.add_argument("--validate-only", action="store_true",
                        help="Run validation report on existing DB (no rebuild)")
    args = parser.parse_args()

    print("\n Myld Sales Ops — Database Layer")
    print("=" * 42)

    if args.validate_only and DB_PATH.exists():
        conn = get_connection()
    else:
        if not DB_PATH.exists() or args.rebuild:
            conn = build_database(rebuild=args.rebuild)
        else:
            print(f"  Database already exists: {DB_PATH}")
            print("  Use --rebuild to recreate. Running validation only.\n")
            conn = get_connection()

    # Schema inventory
    cur  = conn.execute("SELECT type, name FROM sqlite_master ORDER BY type, name")
    objs = cur.fetchall()
    tables = [r["name"] for r in objs if r["type"] == "table"]
    views  = [r["name"] for r in objs if r["type"] == "view"]
    print(f"\n  Tables ({len(tables)}): {', '.join(tables)}")
    print(f"  Views  ({len(views)}):  {', '.join(views)}")

    if args.query:
        print(f"\n  Custom query:\n  {args.query}\n")
        df = pd.read_sql_query(args.query, conn)
        print(df.to_string(index=False, float_format=lambda x: f"{x:,.2f}"))
    else:
        run_validation(conn)

    conn.close()
    print(f"\n  Database path: {DB_PATH.resolve()}\n")


if __name__ == "__main__":
    main()
