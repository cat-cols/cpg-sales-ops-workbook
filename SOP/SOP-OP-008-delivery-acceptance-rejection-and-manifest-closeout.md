# SOP-OP-008 — Delivery Acceptance, Rejection, and Manifest Closeout

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-003 Returns & Refusals; SOP-OP-004 Fulfillment, Manifest & Delivery; SOP-OP-005 Invoicing & Credit Memo Support; SOP-OP-007 Manifest Precheck; SOP-OP-013 Compliance Documentation & Audit Packet Assembly

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines how delivery outcomes are captured, reconciled, and closed after a regulated cannabis order reaches the customer. It ensures accepted, partially accepted, rejected, or refused orders are reflected consistently across CRM, ERP, inventory/WMS, delivery documentation, CTS/Metrc records, invoice status, and the exception log.

The Sales Data Coordinator supports delivery closeout by collecting outcome data, updating systems, routing discrepancies, and preventing incorrect invoice or inventory records from aging unresolved.

---

## 2. Scope

This SOP applies when a delivery has reached the customer location and one of the following outcomes occurs:

- Full acceptance
- Partial acceptance
- Item-level rejection
- Quantity discrepancy
- Full refusal
- Damaged product observed at delivery
- Missing signature or incomplete receiving documentation
- Delivery attempt failed because customer was unavailable
- Product returned to origin after attempted delivery

This SOP does not replace a formal returns process for product already accepted into customer custody. Post-acceptance returns should follow SOP-OP-003.

---

## 3. Guiding Controls

1. **Delivery outcome must be documented the same day whenever possible.**
2. **Accepted, rejected, refused, and returned-to-origin quantities must reconcile to the manifest, pick record, inventory record, and invoice status.**
3. **Do not invoice refused or rejected product as accepted product.**
4. **Do not create a credit memo automatically unless an invoice was posted or customer balance was affected.**
5. **Do not close a delivery exception until physical custody, system status, and documentation match.**
6. **Compliance owns regulatory interpretation; Sales Data Coordinator owns data-quality follow-through and routing.**

---

## 4. Delivery Outcome Definitions

| Outcome | Definition | Primary Handling |
|---|---|---|
| Full Acceptance | Customer accepts all delivered items and quantities | Close delivery, release invoice process, archive paperwork |
| Partial Acceptance | Customer accepts some but not all delivered items | Split accepted vs rejected quantities and route exception |
| Item Rejection | Customer rejects one or more SKUs/packages | Document reason, reconcile package/quantity, prevent incorrect billing |
| Full Refusal | Customer refuses the entire delivery | Return-to-origin workflow, invoice hold, compliance review |
| Failed Delivery Attempt | Delivery could not be completed because customer unavailable or route issue | Reschedule or cancel according to Sales/Distribution decision |
| Quantity Discrepancy | Customer-received quantity differs from manifest/order/invoice | Investigate pick, manifest, receiving, and invoice records |
| Documentation Defect | Signature, receiving note, manifest, or proof-of-delivery is incomplete | Hold closeout until corrected or escalated |

---

## 5. Required Inputs

- ERP sales order number
- CRM order reference
- Manifest or CTS transfer reference
- Customer legal name / DBA
- Delivery date and time
- Driver name
- Delivery route or stop number
- Accepted SKU/package/quantity details
- Rejected or refused SKU/package/quantity details
- Customer refusal or rejection reason
- Proof of delivery or receiving signature
- Driver notes
- Warehouse return-to-origin confirmation, if applicable
- Invoice number or invoice hold status
- Exception log ID, if applicable

---

## 6. Procedure

### Step 1 — Receive delivery outcome

1. Receive delivery confirmation from driver, Distribution, customer support, or automated delivery record.
2. Determine the delivery outcome category.
3. If the delivery was anything other than full acceptance, create or update an exception log entry.
4. Capture customer comments exactly enough to support operational follow-up without adding unsupported interpretation.

### Step 2 — Validate accepted quantities

1. Compare delivered/accepted quantities against:
   - ERP order lines
   - Warehouse pick record
   - Manifest / CTS reference
   - Driver delivery notes
   - Customer receiving documentation
2. Confirm accepted package UIDs and quantities are consistent across records.
3. If accepted quantities differ, route to Distribution, Warehouse, and Compliance before closing.

### Step 3 — Process full acceptance

For a full acceptance:

1. Mark delivery as accepted/complete in the operational tracker.
2. Confirm proof of delivery is attached or stored.
3. Confirm invoice timing according to company process.
4. Update CRM order status to delivered/complete if applicable.
5. Remove the order from open delivery exception queues.
6. Archive delivery documentation in the order folder.

### Step 4 — Process partial acceptance or item rejection

For partial acceptance or item rejection:

1. Identify accepted lines and rejected lines separately.
2. Confirm whether rejected product remains on vehicle, returns to origin, or requires another compliant handling process.
3. Notify Compliance and Distribution of package UID and quantity impact.
4. Place invoice hold on rejected/refused quantities.
5. Confirm whether accepted quantities should invoice separately.
6. Update CRM/ERP notes with customer reason and next action.
7. Route to Sales for customer communication.

### Step 5 — Process full refusal

For a full refusal:

1. Document refusal reason.
2. Confirm product is returned to origin or routed according to compliant handling instructions.
3. Place invoice hold unless invoice already posted.
4. If invoice already posted, route to Accounting for invoice correction or credit memo determination.
5. Update order status to refused / delivery exception.
6. Escalate recurring customer refusal patterns to Sales Operations.

### Step 6 — Close manifest / CTS delivery workflow

1. Confirm delivery outcome has been entered or routed according to the employer's CTS/Metrc process.
2. Confirm accepted and rejected package/quantity results are reconciled.
3. Confirm any returned product is accounted for in inventory/WMS and CTS/Metrc according to Compliance direction.
4. Do not mark the order closed in the tracker until CTS/Metrc closeout status is confirmed or assigned to Compliance with a due date.

### Step 7 — Complete invoice/credit memo routing

1. If all product was accepted, release invoice process according to normal workflow.
2. If any product was rejected/refused before acceptance and not invoiced, confirm invoice hold/correction.
3. If product was invoiced and later requires financial correction, route to Accounting for credit memo or invoice adjustment review.
4. Update exception log with final financial disposition.

---

## 7. Same-Day Closeout Checklist

- Delivery outcome received
- Proof of delivery stored
- Accepted quantities confirmed
- Rejected/refused quantities documented
- Package UID impact reviewed
- Invoice hold or release decision documented
- Return-to-origin status confirmed, if applicable
- CRM/ERP statuses updated
- Exception owner assigned
- Customer communication owner identified

---

## 8. No-Close Conditions

Do not close the delivery if:

- Proof of delivery is missing
- Rejected/refused package UIDs are not documented
- Accepted quantity does not match invoice quantity
- Returned product physical custody is unclear
- Manifest/CTS closeout status is unknown
- Customer reason is missing for rejection/refusal
- Invoice correction has no Accounting owner
- Compliance review is still pending

---

## 9. Exception Reason Codes

Use standardized reason codes when possible:

- CUSTOMER_NOT_AVAILABLE
- BUYER_NOT_ON_SITE
- VAULT_FULL
- ORDER_NOT_EXPECTED
- WRONG_SKU
- WRONG_QUANTITY
- DAMAGED_PRODUCT
- LABEL_OR_PACKAGE_ISSUE
- LICENSE_OR_DESTINATION_ISSUE
- PRICE_OR_PO_DISPUTE
- DELIVERY_WINDOW_MISSED
- DOCUMENTATION_MISSING
- OTHER_REQUIRES_REVIEW

---

## 10. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| Full refusal | Sales + Distribution + Compliance | Confirm customer reason and product return status |
| Partial rejection | Sales Data Coordinator + Warehouse + Accounting | Separate accepted/rejected quantities and invoice only valid quantity |
| Missing proof of delivery | Distribution | Obtain documentation before closeout |
| Package UID discrepancy | Compliance + Inventory | Reconcile manifest, package, and physical inventory |
| Invoice already posted for refused product | Accounting | Determine invoice void, correction, or credit memo workflow |
| Repeated customer refusal | Sales Operations + Account Manager | Review account process and delivery expectations |

---

## 11. Evidence / Artifacts

- Delivery confirmation
- Proof of delivery / receiving signature
- Manifest or CTS reference
- Driver notes
- Rejection/refusal reason
- Return-to-origin confirmation
- Invoice hold or credit memo routing note
- Exception log entry
- Final CRM/ERP status

---

## 12. Success Metrics

- Same-day delivery closeout rate
- Number of delivery exceptions by reason code
- Average time to resolve refused/rejected orders
- Number of invoices corrected due to delivery outcome mismatch
- Reduction in missing proof-of-delivery issues
- Reduction in unresolved returned-to-origin inventory issues
