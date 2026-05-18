# SOP-OP-012 — SKU / Item Master and Market Eligibility Control

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-001 Order Intake & Validation; SOP-OP-007 Manifest Precheck; SOP-OP-009 Inventory Reconciliation; SOP-OP-011 Product Hold & Stop-Ship Control

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines how SKU, item, product, and market eligibility data should be reviewed and controlled before products are used in sales orders, fulfillment, manifests, reports, or invoices. The purpose is to reduce order errors caused by mismatched product names, item numbers, unit sizes, case packs, pricing, state eligibility, inactive SKUs, and CRM/ERP/CTS mapping issues.

The Sales Data Coordinator supports item master quality by flagging mismatches, coordinating corrections, and ensuring open sales orders do not rely on unresolved product data.

---

## 2. Scope

This SOP applies to product master data used in:

- CRM product catalog
- ERP item master
- Price list / price book
- Inventory/WMS records
- CTS/Metrc item and package records
- Excel/Google Sheets reconciliation workbook
- Order entry forms
- Sales reporting dashboards
- Exception logs

---

## 3. Controlled Product Data Fields

| Field | Description |
|---|---|
| SKU / Item Number | Unique internal product identifier |
| Product Name | Standard customer-facing name |
| ERP Item Description | System product description used on orders/invoices |
| CRM Product Name | Sales catalog product description |
| CTS/Metrc Item Name | Traceability item reference |
| Unit Size | Size, weight, count, or package description |
| Case Pack | Units per case or saleable unit grouping |
| Product Category | Gummies, beverages, edibles, extracts, etc. |
| Market / State Eligibility | Where SKU may be sold |
| Active Status | Active, inactive, discontinued, pending setup, blocked |
| Price List | Standard or approved price reference |
| Tax / Accounting Category | Finance mapping if applicable |
| Label / Packaging Approval Status | Whether product is eligible for release |

---

## 4. Review Triggers

Run a SKU/item review when:

- New SKU is added
- SKU is discontinued or replaced
- Product is added to a new market
- Product name changes
- Unit size or case pack changes
- Price list changes
- Product is placed on hold
- Order fails due to SKU mismatch
- Package UID maps to unexpected item
- Invoice uses different product description than order
- Customer receives wrong product or rejects product due to mismatch

---

## 5. Procedure

### Step 1 — Identify product data issue or setup request

1. Receive item setup request or mismatch notice.
2. Capture SKU, product name, category, market, and requestor.
3. Determine whether issue affects open orders, inventory, manifests, pricing, or reporting.
4. If open orders are affected, create an exception log entry.

### Step 2 — Compare product records across systems

Compare CRM, ERP, inventory/WMS, CTS/Metrc, and workbook records for:

- item number
- product name
- unit size
- case pack
- category
- active status
- market eligibility
- standard price
- replacement/substitution SKU
- blocked/hold status

### Step 3 — Classify mismatch severity

| Severity | Example | Handling |
|---|---|---|
| Low | Minor naming difference that does not affect order/invoice/manifest | Document and route for cleanup |
| Medium | CRM name differs from ERP invoice description | Correct before future customer-facing docs |
| High | SKU maps to wrong unit size, case pack, price, or market | Block affected order release |
| Critical | SKU/package mismatch affects CTS/manifest or compliance status | Escalate to Compliance and Inventory immediately |

### Step 4 — Validate market eligibility

1. Confirm the SKU is approved for Oregon sales in the product master or approved eligibility table.
2. Confirm SKU is active and sellable.
3. Confirm product is not discontinued, quarantined, expired, blocked, or pending setup.
4. Confirm product type is permitted for the receiving customer/account.
5. If eligibility is unclear, hold impacted order lines pending Compliance/Product review.

### Step 5 — Coordinate correction

1. Determine record owner:
   - CRM product owner
   - ERP item master owner
   - Inventory/WMS owner
   - Compliance/CTS owner
   - Pricing owner
   - Sales Operations
2. Assign correction in exception log.
3. Confirm corrected field values.
4. Validate correction appears in downstream order/invoice/reporting records.

### Step 6 — Update impacted orders

1. Identify open orders using the affected SKU.
2. Confirm whether orders should proceed, hold, substitute, reduce, or cancel.
3. Apply approved order modifications according to SOP-OP-002.
4. Confirm pick tickets, manifests, invoices, and customer communication reflect corrected product data.

---

## 6. New SKU Setup Checklist

Before a new SKU is used on an order, confirm:

- SKU/item number exists in ERP
- CRM product exists and maps to ERP item
- Product name and description match approved naming convention
- Unit size and case pack are correct
- Oregon market eligibility is approved
- Price is loaded or approved
- Inventory is available and not on hold
- CTS/Metrc item/package mapping is available if applicable
- Product category and reporting attributes are populated
- Substitute or replacement SKU is documented if relevant

---

## 7. No-Order Conditions

Do not release an order line if:

- SKU is missing from ERP
- SKU appears active in CRM but inactive in ERP
- Product name/unit size does not match package UID or inventory record
- State eligibility is unknown or blocked
- Price is missing or unapproved
- Product is on hold/quarantine/stop-ship
- Replacement SKU has not been approved
- Customer ordered a discontinued SKU with no approved substitute

---

## 8. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| Product active in CRM but inactive in ERP | Sales Operations + ERP Owner | Align active status before order release |
| SKU/state eligibility unclear | Compliance + Product | Confirm market eligibility |
| Pricing missing | Pricing / Accounting | Load or approve price before invoice |
| Package UID maps to unexpected item | Inventory + Compliance | Verify physical product and system mapping |
| Discontinued SKU on open order | Sales + Product | Approve substitution, reduction, or cancellation |
| Repeated SKU mismatch | Sales Operations Manager | Review master data governance |

---

## 9. Documentation Standards

Every product master correction should include:

- SKU/item number
- Current incorrect value
- Correct value
- Source system requiring correction
- Owner
- Approval source
- Open orders impacted
- Final correction date
- Validation note

---

## 10. Success Metrics

- SKU mismatch exceptions per week
- Orders held due to product master issues
- New SKU setup first-pass completion rate
- Average time to resolve SKU/item mapping issue
- Invoice corrections caused by product master issues
- Customer refusals tied to wrong SKU or product description
