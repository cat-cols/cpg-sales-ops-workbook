# SOP-OP-011 — Product Hold, Quarantine, and Stop-Ship Control

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-001 Order Intake & Validation; SOP-OP-007 Manifest Precheck; SOP-OP-009 Daily Inventory Reconciliation; SOP-OP-012 SKU / Item Master Control; SOP-OP-015 Exception Escalation & Root Cause Review

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines the process for identifying, documenting, communicating, and controlling product holds, quarantines, and stop-ship restrictions that affect open sales orders. It helps prevent blocked, expired, mislabeled, ineligible, or otherwise restricted product from being released to fulfillment, manifested, shipped, invoiced, or represented as available to sell.

The Sales Data Coordinator supports the process by identifying impacted orders, updating order statuses, coordinating cross-functional communication, and ensuring exception records are closed only after the hold decision is resolved.

---

## 2. Scope

This SOP applies when product is restricted due to:

- Compliance hold
- Quality hold
- Label or packaging issue
- Testing issue
- Batch/lot concern
- Expiration or shelf-life issue
- Product recall or market withdrawal
- Inventory discrepancy
- State eligibility problem
- Product master setup error
- Internal stop-ship decision
- Customer-specific restriction

This SOP does not authorize release from hold. Hold release must come from the designated owner, such as Compliance, Quality, Inventory, Product, or Sales Operations leadership.

---

## 3. Definitions

| Term | Definition |
|---|---|
| Product Hold | Product is temporarily blocked from sale or shipment pending review |
| Quarantine | Product is physically or systematically separated until disposition is determined |
| Stop-Ship | Instruction that affected product may not be released to customers |
| Release from Hold | Approved decision allowing product to return to sellable/shippable status |
| Disposition | Final decision such as release, rework, relabel, return to inventory, destruction, or permanent block |

---

## 4. Hold Reason Codes

Use standardized reason codes:

- COMPLIANCE_HOLD
- QUALITY_HOLD
- LABEL_REVIEW
- PACKAGING_ISSUE
- TESTING_PENDING
- TESTING_FAILED
- EXPIRED_OR_NEAR_EXPIRY
- RECALL_OR_WITHDRAWAL
- INVENTORY_VARIANCE
- CTS_ERP_MISMATCH
- SKU_STATE_INELIGIBLE
- PRODUCT_MASTER_ERROR
- CUSTOMER_SPECIFIC_BLOCK
- MANAGEMENT_STOP_SHIP
- OTHER_REQUIRES_REVIEW

---

## 5. Procedure

### Step 1 — Receive hold notification

1. Receive product hold/stop-ship notice from Compliance, Quality, Inventory, Warehouse, Product, Sales Operations, or management.
2. Confirm the scope of the hold:
   - SKU/item number
   - product name
   - package UID(s)
   - lot/batch
   - market/state
   - affected date range
   - customer-specific restrictions
   - reason code
3. Create an exception or hold control record.

### Step 2 — Identify impacted sales orders

1. Search open CRM/ERP orders for affected SKU/item/package/lot.
2. Identify orders in each status:
   - pending intake
   - released not picked
   - picked/staged
   - manifested/routed
   - out for delivery
   - delivered not invoiced
   - invoiced
3. Prioritize orders closest to dispatch or customer delivery.

### Step 3 — Block affected order movement

1. Place the impacted order lines on hold or update status according to system process.
2. Notify Warehouse to prevent picking/staging if not already staged.
3. Notify Distribution if delivery route or manifest may be impacted.
4. Notify Sales / Account Manager if customer communication may be required.
5. Notify Accounting if invoice should be held or corrected.

### Step 4 — Review substitution or replacement options

1. Check approved sellable inventory for replacement SKU/package.
2. Confirm replacement is eligible for customer, state, price, and order terms.
3. Obtain Sales/customer approval for substitution if required.
4. Update CRM/ERP order according to SOP-OP-002 if substitution is approved.
5. Do not substitute product if product master, compliance, or inventory validation is incomplete.

### Step 5 — Track disposition

1. Wait for designated owner to determine final disposition.
2. Document one of the following:
   - released from hold
   - substitute approved
   - order reduced
   - order cancelled
   - inventory correction required
   - credit memo / invoice correction required
   - destruction or removal from sellable inventory
3. Confirm all impacted systems reflect the final decision.

### Step 6 — Close impacted order exceptions

1. Confirm order status, inventory status, manifest status, and invoice status are consistent.
2. Confirm customer-facing action has been completed or assigned.
3. Update exception log with resolution code.
4. Close the exception only when final owner approval and system updates are complete.

---

## 6. No-Release Conditions

Do not release an affected order if:

- Hold reason is unresolved
- Release owner has not approved
- Package UID remains blocked or mismatched
- Product is not eligible for the Oregon market
- Label/packaging issue is unresolved
- Product is expired or fails internal shelf-life control
- Replacement SKU is not approved by customer/Sales
- Invoice was already created and Accounting has not reviewed correction impact

---

## 7. Communication Template

Use concise internal language:

```text
Subject: Product Hold Impact Review Needed — [SKU] / [Order #]

A product hold has been identified for [SKU/Product/Package UID].
Impacted order(s): [Order #s]
Current status: [Pending / Picked / Manifested / Delivered / Invoiced]
Hold reason: [Reason Code]
Requested action: [Review / Substitute / Hold order / Correct inventory / Invoice hold]
Owner requested: [Team/Name]
Due by: [Date/Time]
```

---

## 8. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| Compliance hold | Compliance | Confirm whether product can sell/ship |
| Quality or label hold | Quality / Product | Confirm disposition and replacement path |
| Product already picked | Warehouse + Distribution | Pull product from staging or confirm route impact |
| Product already manifested | Compliance + Distribution | Determine manifest correction or delivery stop |
| Product already invoiced | Accounting | Determine invoice correction or credit memo path |
| Multiple customer orders impacted | Sales Operations | Coordinate customer prioritization and communication |

---

## 9. Evidence / Artifacts

- Hold notice
- Affected SKU/package/lot list
- Impacted open order list
- Inventory/WMS hold screenshot or report
- CRM/ERP order status notes
- Substitution approval, if applicable
- Compliance/Quality release note
- Invoice hold or correction note
- Final exception log resolution

---

## 10. Success Metrics

- Number of blocked product releases prevented
- Number of orders impacted by product holds
- Average time from hold notice to impacted-order identification
- Average time to final disposition
- Reduction in customer refusals caused by held/incorrect product
- Reduction in invoice corrections tied to stop-ship events
