# SOP-OP-009 — Daily CTS-to-ERP Inventory Reconciliation

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-001 Order Intake & Validation; SOP-OP-004 Fulfillment, Manifest & Delivery; SOP-OP-007 Manifest Precheck; SOP-OP-011 Product Hold & Stop-Ship; SOP-OP-012 SKU / Item Master Control

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines the daily reconciliation process between Metrc / Oregon CTS, ERP inventory, warehouse/WMS records, and sales order allocations. The goal is to identify product, package, quantity, and availability mismatches before they cause order release errors, manifest errors, invoice corrections, compliance risk, or customer service issues.

The Sales Data Coordinator supports this process by comparing operational data, flagging mismatches, documenting owner/action/status, and confirming that unresolved issues are blocked from fulfillment or clearly assigned for resolution.

---

## 2. Scope

This SOP applies to daily review of inventory data used for sales order release and fulfillment, including:

- Available-to-sell inventory
- Allocated inventory
- Picked or staged inventory
- Package UID data
- SKU/item mapping
- Quantity-on-hand differences
- Negative inventory flags
- Product holds, quarantine, and stop-ship flags
- Open order allocation conflicts
- Returns/refusals returning to inventory
- Inventory that appears in ERP but not CTS, or CTS but not ERP

This SOP does not authorize inventory adjustments. Any inventory correction must be handled by the appropriate Inventory, Compliance, or Accounting owner according to company policy.

---

## 3. Regulatory Reference Concepts

Oregon cannabis operations require controlled inventory tracking through CTS/Metrc. Operationally, sales teams should treat CTS inventory, ERP inventory, warehouse inventory, and order allocation records as interdependent controls. When they do not match, orders should not be released until the difference is explained, corrected, or formally approved for exception handling.

Always defer to Compliance for final CTS/Metrc actions and interpretation.

---

## 4. Data Sources

| Source | Typical Fields Reviewed |
|---|---|
| CTS / Metrc export | Package UID, item name, quantity, unit, location, status, source package, destination transfer |
| ERP inventory | Item number, item description, lot/batch, quantity on hand, quantity allocated, blocked quantity, location |
| WMS / warehouse tracker | Picked quantity, staged quantity, bin/location, physical count notes, hold status |
| CRM / open orders | Customer, requested SKU, requested quantity, delivery date, rep, order priority |
| Exception log | Existing mismatch, owner, due date, action, status |
| Product master | SKU, item number, product name, unit size, state eligibility, active/inactive status |

---

## 5. Daily Procedure

### Step 1 — Pull daily exports

1. Pull or receive the CTS/Metrc inventory report according to approved access process.
2. Pull ERP inventory report for sellable, allocated, and blocked inventory.
3. Pull WMS or warehouse pick/staging report.
4. Pull open order allocation report for orders due today and next planned delivery window.
5. Save each export using a consistent naming convention:
   - `YYYY-MM-DD_CTS_inventory_export`
   - `YYYY-MM-DD_ERP_inventory_snapshot`
   - `YYYY-MM-DD_WMS_pick_stage_report`
   - `YYYY-MM-DD_open_order_allocations`

### Step 2 — Validate file completeness

1. Confirm all expected fields are present.
2. Confirm exports are from the current date.
3. Confirm units of measure are understood and comparable.
4. Confirm package UID fields are not blank where required.
5. If an export is missing or stale, note it in the daily QC summary and request a corrected source file.

### Step 3 — Reconcile package UID and SKU mapping

1. Compare package UID records against ERP item numbers and product master records.
2. Confirm each package UID maps to one active SKU/item.
3. Flag package UIDs with missing item numbers, mismatched product names, inactive SKUs, incorrect unit size, or state eligibility issues.
4. Route product master issues to the product/item data owner.

### Step 4 — Reconcile quantities

1. Compare CTS package quantity to ERP available quantity.
2. Compare ERP available quantity to WMS physical/pickable quantity.
3. Compare allocated quantity to open sales order quantity.
4. Identify:
   - negative inventory
   - overallocated inventory
   - available inventory that is on hold
   - picked quantity greater than available quantity
   - inventory in ERP but not CTS
   - inventory in CTS but not ERP
   - returned product not yet dispositioned

### Step 5 — Review near-term fulfillment risk

1. Filter orders due for delivery today and the next delivery cycle.
2. Identify any order line using inventory with an unresolved mismatch.
3. Place order hold or pre-release warning when the mismatch could affect fulfillment.
4. Notify Sales, Warehouse, Distribution, and Compliance as needed.

### Step 6 — Update exception log

For each mismatch, create or update the exception record with:

- Exception type
- SKU/item
- Package UID
- Quantity difference
- Source systems compared
- Impacted order(s)
- Owner
- Priority
- Due date
- Resolution status
- Notes

### Step 7 — Send daily QC summary

Send a concise summary to stakeholders showing:

- Total records reviewed
- Number of mismatches identified
- Critical blockers
- Orders impacted today
- Owners assigned
- Aging unresolved exceptions
- Items cleared from prior day

---

## 6. Reconciliation Tolerances

For cannabis product inventory used in sales order fulfillment, default tolerance is **zero unexplained difference** between physical custody, CTS/Metrc record, ERP inventory, and fulfillment documentation.

Do not treat a variance as acceptable because it is small. Instead, classify it:

- data-entry timing difference
- unit-of-measure mismatch
- open transfer timing issue
- returned product pending disposition
- pick/stage timing issue
- product hold not synced
- true inventory discrepancy
- requires Compliance review

---

## 7. High-Priority Exception Types

- Missing package UID
- Package UID in CTS but not in ERP
- ERP sellable quantity not supported by CTS package quantity
- Negative ERP inventory
- Product allocated to more than one open order
- SKU inactive but present on open order
- Product on compliance hold but released to order
- Quantity staged for shipment differs from manifest quantity
- Return/refusal received physically but not reconciled in systems

---

## 8. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| CTS/ERP package mismatch | Compliance + Inventory | Confirm correct package status and system correction path |
| Negative inventory | Inventory + Sales Operations | Block affected order lines until resolved |
| Overallocated SKU | Warehouse + Sales | Prioritize, split, substitute, or delay affected orders |
| Held/quarantined product allocated | Compliance + Product Owner | Stop release and update item hold status |
| Open order affected today | Sales + Distribution | Notify customer owner and adjust fulfillment plan |
| Repeated mismatch type | Sales Operations Manager | Review root cause and preventive control |

---

## 9. Evidence / Artifacts

- Daily CTS/Metrc export
- ERP inventory snapshot
- WMS/pick-stage report
- Open order allocation report
- Product master extract
- Daily QC summary
- Exception log updates
- Hold/release notes
- Resolution confirmation

---

## 10. Success Metrics

- Daily reconciliation completed before order release cutoff
- Number of inventory mismatches found before fulfillment
- Number of orders blocked due to inventory data issues
- Average age of unresolved inventory exceptions
- Reduction in delivery refusals caused by inventory/order mismatch
- Reduction in invoice corrections caused by incorrect fulfillment quantities
