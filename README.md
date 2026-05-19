# Cannabis CPG Sales Data Coordinator Project

A simulated CRM-to-ERP Sales Operations project focused on sales order lifecycle management, ERP/CRM style data quality, fulfillment coordination, invoicing support, credit memo workflows, returns/refusals, exception tracking, and SOP-style process documentation.

This project was built as a portfolio case study for a **Sales Data Coordinator / Sales Operations / CRM-ERP Data Quality** role in a regulated cannabis CPG environment.

---

## Project Purpose

Sales Data Coordinator roles often sit between Sales, Distribution, Inventory, Accounting, Customer Support, and Compliance. The goal of this project is to simulate that operating environment and show how order data can be validated, reconciled, corrected, documented, and reported across CRM-style and ERP-style systems.

The project models a realistic order-to-cash support workflow:

1. CRM-style order intake and customer/account validation
2. ERP-style order creation, order status tracking, and invoice support
3. Fulfillment and warehouse coordination
4. Inventory, SKU, and state-eligibility checks
5. Returns, refusals, rejected orders, and credit memo routing
6. Exception tracking and daily QA/QC review
7. SOP-style documentation for repeatable operational processes

---

## Proof of Concept

The role essentially acts as the "bridge" between these two systems, ensuring that the sales data from the CRM flows accurately into the ERP for fulfillment, invoicing, and accounting.

[Google Sheets Link](https://docs.google.com/spreadsheets/d/1w1cBCzS5EIMZS9mpNI-3vBf8JUKAd_BcGulS43WQB5o/edit?gid=84316029#gid=84316029)


## Visual Workflow Diagrams

Key process diagrams are stored in the `diagrams/` folder:

- `sales-data-coordinator-hub.mmd` — cross-functional coordination map
- `order-lifecycle-flow.mmd` — end-to-end order lifecycle
- `crm-to-erp-data-flow.mmd` — CRM/ERP data movement and reconciliation
- `exception-escalation-flow.mmd` — order issue routing and resolution
- `metrc-manifest-precheck-flow.mmd` — simulated compliance precheck workflow


## What This Project Demonstrates

### Sales Operations

- End-to-end sales order lifecycle support
- Order intake, order edits, cancellations, rejections, returns, and refusals
- Fulfillment coordination and order status follow-up
- Invoice and credit memo support workflows
- Customer support case tracking and issue escalation
- Cross-functional handoffs between Sales, Distribution, Inventory, Accounting, and Compliance

### Data Quality and Reconciliation

- CRM/ERP account and customer crosswalks
- SKU/item mapping and product lookup controls
- Missing order, orphan invoice, and invoice mismatch checks
- Pricing discrepancy detection
- Inventory shortage and negative inventory flags
- Fulfillment blocker tracking
- Exception reason codes and ownership assignment

### Reporting and Documentation

- Excel-based sales operations workbooks
- Order lifecycle dashboards and reconciliation summaries
- SLA and exception tracking views
- SQL views for revenue, open orders, inventory status, compliance flags, and account health
- SOP-style documentation for repeatable sales operations processes

---

## CRM and ERP Concept Mapping

This project mirrors the **concepts** of Salesforce-style CRM workflows and Business Central-style ERP workflows.

| Business Process Area | Salesforce-style CRM Concept | Business Central-style ERP Concept | Project Artifact |
|---|---|---|---|
| Customer/account management | Account, owner, customer status | Customer, bill-to/ship-to customer | `customer_lookup`, `customer_crosswalk`, `crm_orders` |
| Product and pricing | Product, SKU, price book-style pricing | Item, item price, item availability | `product_lookup`, `field_mapping_crm_to_erp`, `inventory_snapshot` |
| Order intake | CRM order/request | Sales order | `crm_orders`, `sales_orders`, SOP-OP-001 |
| Fulfillment | Order status updates and customer follow-up | Shipment / delivery coordination | `warehouse_shipments`, SOP-OP-004 |
| Invoicing | Customer/order communication | Sales invoice, AR, credit memo | `erp_invoices`, `accounts_receivable`, SOP-OP-005 |
| Returns/refusals | Customer support case / order issue | Return order / credit memo workflow | `returns_credit_memos`, SOP-OP-003 |
| Data quality | CRM hygiene and duplicate/mismatch checks | ERP reconciliation and posting support | `exception_log`, SQL views, `quality_check.py` |

The project intentionally uses terms like **Salesforce-style** and **Business Central-style** because it is a simulated workflow, not a direct configuration of those systems.

---

## Repository Structure

```text
.
├── README.md
├── excel/
│   ├── sales_ops_crm_erp_practice_workbook_enterprise.xlsx
│   ├── wyld_sales_ops_crm_erp_practice.xlsx
│   ├── Wyld_Sales_Order_Tracker.xlsx
│   └── wyld-order-compliance.xlsx
├── sql/
│   ├── schema.sql
│   ├── missing-orders.sql
│   ├── dim_products.sql
│   ├── dim_state_skus.sql
│   └── 00_run_sales_data_coordinator_pipeline.sql
├── scripts/
│   ├── generate_project_data.py
│   ├── database.py
│   ├── quality_check.py
│   ├── order_lifecycle.py
│   ├── build_excel.py
│   └── build_workbook.py
├── SOP/
│   ├── SOP-OP-001-order-intake-validation.md
│   ├── SOP-OP-002-order-modification-process.md
│   ├── SOP-OP-003-process-customer-returns-refusals.md
│   ├── SOP-OP-004-fulfillment-manifest-delivery.md
│   ├── SOP-OP-005-invoicing-credit-memo.md
│   ├── SOP-OP-006-daily-sales-order-dq.md
│   └── _OR_sales_order_sop_assumptions.md
├── docs/
│   ├── source_register.csv
│   ├── exception_reason_codes.csv
│   ├── flowchart.md
│   ├── graph.md
│   └── workflow-ppt-guide.md
├── notes/
│   ├── job-description.md
│   ├── 0-METRC-compliance.md
│   ├── getting-started.ipynb
│   ├── interview-questions.ipynb
│   └── repo-guide.ipynb
└── views/
    └── wyld_order_tracker_mockup.html
```

---

## Key Excel Workbooks

### `excel/sales_ops_crm_erp_practice_workbook_enterprise.xlsx`

Primary reviewer workbook. It includes:

- `executive_summary`
- `dashboard`
- `reconciliation_summary`
- `sla_metrics`
- `crm_orders`
- `erp_invoices`
- `warehouse_shipments`
- `accounts_receivable`
- `order_compliance_review`
- `customer_support_cases`
- `returns_credit_memos`
- `inventory_snapshot`
- `customer_crosswalk`
- `field_mapping_crm_to_erp`
- `compliance_rules`
- `exception_log`
- `customer_lookup`
- `product_lookup`

### `excel/Wyld_Sales_Order_Tracker.xlsx`

A compact sales order tracker mockup with order tracking, discrepancy logging, summary views, and SOP references.

### `excel/wyld-order-compliance.xlsx`

A compliance-focused workbook with raw order data, compliance review logic, cleaned order outputs, rejection logging, and dashboarding.

---

## SOP Documentation

The SOP folder documents repeatable order operations workflows from a Sales Data Coordinator perspective.

| SOP | Process Area | Purpose |
|---|---|---|
| `SOP-OP-001-order-intake-validation.md` | Order intake | Validate customer, SKU, quantity, pricing, and required documentation before order release |
| `SOP-OP-002-order-modification-process.md` | Order edits | Control changes to orders before/after fulfillment milestones |
| `SOP-OP-003-process-customer-returns-refusals.md` | Returns/refusals | Document customer refusals, return handling, credit memo routing, and exception logging |
| `SOP-OP-004-fulfillment-manifest-delivery.md` | Fulfillment | Coordinate warehouse, delivery, manifest, and order status updates |
| `SOP-OP-005-invoicing-credit-memo.md` | Accounting support | Support invoice review, credit memo requests, and billing exception resolution |
| `SOP-OP-006-daily-sales-order-dq.md` | Data quality | Perform daily CRM/ERP order QA, reconciliation, and exception review |
| `_OR_sales_order_sop_assumptions.md` | Compliance assumptions | Documents simulated Oregon cannabis workflow assumptions used in the project |

The SOPs are intentionally written as **SOP-style documentation** for a portfolio project. They are not legal guidance and are not official compliance procedures.

---

## SQL Layer

The SQL files define a lightweight reporting and reconciliation layer for sales operations analysis.

Notable views in `sql/schema.sql` include:

- `vw_order_summary`
- `vw_revenue_by_market`
- `vw_revenue_by_rep`
- `vw_product_performance`
- `vw_account_health`
- `vw_compliance_flags`
- `vw_inventory_status`
- `vw_open_orders`

Example use cases:

- Identify open orders pending action
- Review revenue by market or sales rep
- Flag compliance-sensitive order lines
- Identify accounts on credit hold
- Review inventory status and reorder risks
- Investigate invoice/order mismatches

---

## Python Scripts

| Script | Purpose |
|---|---|
| `scripts/generate_project_data.py` | Generates synthetic sales operations data |
| `scripts/database.py` | Loads CSV data into SQLite and runs validation queries |
| `scripts/quality_check.py` | Performs QA/QC checks and exception analysis |
| `scripts/order_lifecycle.py` | Simulates order lifecycle actions such as processing, fulfillment, invoicing, rejection, returns, refusals, and order modifications |
| `scripts/build_excel.py` | Builds Excel reporting outputs from the database layer |
| `scripts/build_workbook.py` | Builds a standalone workbook-style order operations tracker |

---

## Suggested Reviewer Path

For a quick review, start here:

1. Open `excel/sales_ops_crm_erp_practice_workbook_enterprise.xlsx`
2. Review the `dashboard`, `reconciliation_summary`, and `exception_log` tabs
3. Review `field_mapping_crm_to_erp`, `customer_crosswalk`, and `order_compliance_review`
4. Open `SOP/SOP-OP-001-order-intake-validation.md`
5. Open `SOP/SOP-OP-002-order-modification-process.md`
6. Open `SOP/SOP-OP-006-daily-sales-order-dq.md`
7. Review `docs/exception_reason_codes.csv`
8. Review `sql/schema.sql` for the reporting views

---

## Example QA/QC Scenarios Modeled

The project includes controls and exception categories for:

- Missing ERP customer IDs
- CRM/ERP customer mismatches
- Credit holds
- Inactive customer accounts
- Missing license or compliance documentation
- SKU not available in destination state
- Insufficient inventory
- Short shipments
- Customer refusals
- Damaged returns
- Pricing errors
- Duplicate orders
- Missing invoices
- Invoice amount mismatches
- Negative inventory
- Documentation gaps

---

## Compliance-Aware Design

The project includes Oregon cannabis workflow assumptions and Metrc/OLCC-aware documentation concepts. These are used to model how a Sales Data Coordinator may support regulated order workflows by validating, flagging, documenting, and escalating issues.

The project does **not** provide legal advice, official compliance instructions, or company-specific compliance procedures.

Sales Data Coordinator framing:

- Supports order accuracy and documentation completeness
- Flags compliance-sensitive exceptions
- Maintains CRM/ERP data integrity
- Routes issues to Compliance, Accounting, Inventory, or Distribution
- Documents exceptions and resolution status
- Does not independently approve regulatory compliance decisions

---

## How This Project Maps to a Sales Data Coordinator Role

| Role Responsibility | Project Evidence |
|---|---|
| Execute sales order lifecycle | Order intake, edits, fulfillment, invoicing, returns, refusals, rejected-order workflows |
| Maintain ERP/CRM data integrity | Customer crosswalks, field mapping, quality checks, exception log |
| Support fulfillment coordination | Warehouse shipment data, delivery status, fulfillment SOPs |
| Support invoicing and credit memos | ERP invoice data, AR data, credit memo workflows, invoicing SOP |
| Resolve discrepancies | QA/QC scripts, exception reason codes, mismatch checks |
| Support reporting and dashboards | Excel dashboards, SQL views, SLA metrics, reconciliation summaries |
| Document SOPs | SOP folder covering intake, modifications, fulfillment, returns, invoicing, and daily data quality |
| Work cross-functionally | Process handoffs across Sales, Distribution, Inventory, Accounting, Customer Support, and Compliance |

---

## Skills Demonstrated

- Sales operations process design
- Order lifecycle tracking
- ERP/CRM data quality review
- Excel/Google Sheets-style reporting
- SQL reporting views
- Python/pandas data generation and QA/QC scripting
- Exception tracking and root-cause categorization
- SOP-style documentation
- Cannabis compliance awareness
- Cross-functional workflow mapping

---

## Limitations

This is a simulated project, so it does not include:

- A live Salesforce org
- A live Business Central tenant
- Real customer, order, inventory, or compliance data
- Official company SOPs
- Official Metrc/OLCC compliance procedures
- Production-grade access controls or audit logging

The value of the project is in the workflow design, data model, reconciliation logic, documentation, and operational reasoning.

---

## Author

**Brandon Hardison**
GitHub: [github.com/cat-cols](https://github.com/cat-cols)

---

## Disclaimer

This project is a personal portfolio piece and is not affiliated with, endorsed by, or sponsored by Wyld. All data used is synthetic/mock data created solely to demonstrate technical proficiency for a Sales Data Coordinator role.