# SOP-OP-002 — Sales Order Modification Process

**Document Type:** Standard Operating Procedure — portfolio simulation
**Process Area:** Sales Operations / Order Lifecycle Management
**Owner:** Sales Data Coordinator
**Market Assumption:** Regulated cannabis CPG wholesale operations
**Related Systems:** CRM, ERP, inventory/WMS, state traceability system, shared documentation drive, email/Slack
**Related SOPs:** SOP-OP-001 Order Intake & Validation; SOP-OP-003 Returns & Refusals; SOP-OP-004 Fulfillment, Manifest & Delivery; SOP-OP-005 Invoicing & Credit Memo Support; SOP-OP-006 Daily Sales Order Data Quality Review
**Version:** 1.0

> **Portfolio note:** This SOP is a simulated, role-aligned process document. It is not an official policy of any employer. It is written to demonstrate practical understanding of sales order controls, ERP/CRM data quality, regulated fulfillment, and cross-functional order change coordination.

---

## 1. Purpose

The purpose of this SOP is to ensure all sales order modifications are accurate, authorized, documented, and reconciled across CRM, ERP, inventory, fulfillment, accounting, and compliance systems before the order moves further through the lifecycle.

Order modifications create operational risk because one change can affect customer expectations, pick tickets, delivery routes, inventory availability, state traceability manifests, invoices, accounts receivable, and reporting. The Sales Data Coordinator acts as the control point to make sure the requested change is valid, approved, and reflected consistently across systems.

---

## 2. Scope

This SOP applies to customer, sales, inventory, fulfillment, accounting, or compliance-driven changes to an order after initial order submission and before final close.

Common modification types include:

- Adding an item
- Removing an item
- Changing quantity
- Changing requested delivery date
- Updating PO number or customer reference
- Correcting ship-to, bill-to, or contact details
- Correcting pricing or discount information
- Substituting an approved SKU
- Splitting an order into partial shipments
- Reducing an order due to inventory shortage
- Cancelling an order before fulfillment
- Converting an issue to a rejection, refusal, return, invoice correction, or credit memo workflow when the order is too far downstream to edit directly

---

## 3. Guiding Controls

1. **Do not edit an order without a documented request and reason code.**
2. **Do not release modified orders until customer, SKU, quantity, price, inventory, delivery, and compliance impacts are revalidated.**
3. **Do not change picked, packed, manifested, delivered, or invoiced orders without the required team approvals.**
4. **Do not overwrite history.** Preserve notes, timestamps, original order references, and change rationale.
5. **Do not use a simple order edit when a return, refusal, rejection, invoice void, or credit memo process is required.**
6. **Physical inventory, ERP inventory, CRM order status, state traceability records, and customer communication must tell the same story.**

---

## 4. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Sales Data Coordinator | Intake change request, determine order status, validate change, update CRM/ERP records, coordinate stakeholders, update exception log, confirm closure |
| Sales Representative / Account Manager | Confirm customer intent, provide buyer approval, communicate customer-facing impact where needed |
| Inventory / Warehouse | Confirm available inventory, pick status, substitution feasibility, and whether product must be returned to stock |
| Distribution / Driver Team | Confirm delivery route impact, delivery timing, manifest status, and on-truck changes where applicable |
| Compliance | Review license, manifest, package UID, state eligibility, and regulated product movement impacts |
| Accounting / AR | Approve invoice-impacting changes, price corrections, invoice voids, credit memo needs, and AR adjustments |
| Customer / Retailer | Confirms requested changes, delivery timing, accepted substitutions, or cancellation request |

---

## 5. Order Status Decision Matrix

Before making any change, determine the current order status. The status determines whether the order can be edited directly or must move through an exception workflow.

| Current Order Status | Edit Allowed? | Required Handling |
|---|---:|---|
| Draft / Pending / Open | Yes | Validate requested change, update CRM/ERP, rerun order checks, document reason |
| Released, not picked | Usually yes | Update order, notify warehouse, regenerate pick ticket if needed |
| Picked, not shipped | Controlled edit | Warehouse must confirm picked product changes before ERP update is finalized |
| Packed or staged | Controlled edit | Warehouse + Distribution approval required; may need re-pick or staging correction |
| Manifest created / delivery routed | High-risk edit | Compliance + Distribution review required before changing SKU, quantity, route, or destination |
| Shipped / out for delivery | Do not directly edit lines | Treat as delivery exception, refusal, rejection, or re-delivery issue depending on customer acceptance |
| Delivered / accepted | Do not directly edit lines | Use invoice correction, return, or credit memo workflow as applicable |
| Invoiced / posted | Do not directly edit posted order | Accounting-led correction, invoice void, return order, or credit memo workflow required |
| Cancelled / rejected / refused / returned | No direct edit | Create new order if customer still wants product; preserve audit trail |

---

## 6. Required Inputs for Any Modification

Every change request must include enough information to validate and audit the change.

| Required Field | Description |
|---|---|
| Original order number | CRM and/or ERP order reference |
| Customer account | Legal name, DBA, and account ID if available |
| Requestor | Sales rep, customer, warehouse, distribution, accounting, or compliance |
| Requested change | Add, remove, quantity change, price correction, delivery date change, cancellation, etc. |
| Reason code | Customer request, inventory shortage, pricing error, compliance hold, duplicate order, delivery constraint, etc. |
| SKU/item details | SKU, product name, quantity before and quantity after |
| Financial impact | Net dollar increase/decrease where known |
| Delivery impact | Whether delivery date, route, or driver paperwork changes |
| Compliance impact | Whether license, state eligibility, manifest, package UID, or product movement is affected |
| Approval evidence | Email, CRM note, manager approval, accounting approval, compliance approval, or customer confirmation |

---

## 7. Procedure

### 7.1 Receive and Triage the Change Request

1. Receive the request through an approved channel such as CRM task, email, shared order queue, sales rep request, customer support note, or operations message.
2. Confirm the order number, customer account, requested change, and reason.
3. Check whether the request is time-sensitive due to cutoff, route departure, invoice posting, or customer delivery window.
4. Create or update an exception log entry if the request affects price, quantity, inventory, compliance, fulfillment, invoice value, or customer delivery expectations.

### 7.2 Identify Current Order Status

1. Open the order in the ERP.
2. Check current status: pending, released, picked, packed, manifested, shipped, delivered, invoiced, rejected, refused, returned, or cancelled.
3. Check the CRM order/opportunity/account record for customer request notes or sales rep instructions.
4. Check inventory/WMS or fulfillment tracker for pick, pack, staging, route, or shipment status.
5. Check the state traceability system if a manifest or package movement has already been created.

**Control:** If the order is manifested, shipped, delivered, or invoiced, do not perform a simple line edit. Route the issue through the appropriate exception workflow.

### 7.3 Classify the Modification

Classify the request into one primary type:

| Modification Type | Examples | Primary Approval |
|---|---|---|
| Administrative correction | PO number, contact, internal note, non-regulated reference field | Sales Data Coordinator |
| Customer-requested change | Add/remove SKU, quantity change, delivery date change | Sales Rep / Account Manager |
| Inventory-driven change | Shortage, substitution, partial fulfillment, item hold | Inventory + Sales |
| Pricing correction | Price list error, discount issue, promo correction | Sales Manager + Accounting |
| Compliance-driven change | License issue, SKU not eligible in state, manifest/package issue | Compliance |
| Fulfillment-driven change | Pick discrepancy, route issue, staged product issue | Warehouse / Distribution |
| Financial correction | Invoice value, AR impact, posted invoice issue | Accounting / AR |
| Cancellation | Customer cancellation or order no longer valid | Sales + impacted operations teams |

### 7.4 Validate the Requested Change

Before editing the order, revalidate the following:

- Customer account is active and eligible to receive the product.
- License and ship-to details are still valid.
- Requested SKU is active, sellable, and eligible for the market.
- Requested quantity is available and does not create negative available-to-sell inventory.
- Price, discount, promo, or allowance is approved.
- Delivery date and route can support the change.
- Manifest/package status allows the change without creating a compliance discrepancy.
- Accounting impact is understood if the order has been priced, posted, invoiced, or partially fulfilled.

### 7.5 Secure Required Approvals

1. Obtain Sales approval for any customer-requested product, quantity, delivery, or cancellation change.
2. Obtain Inventory/Warehouse approval for any quantity, SKU, substitution, or pick-ticket change.
3. Obtain Distribution approval for any delivery date, route, driver, ship-to, or manifested order change.
4. Obtain Compliance approval for any change affecting regulated product movement, package IDs, manifest details, license status, or state-specific product eligibility.
5. Obtain Accounting approval for any price, discount, invoice, credit, AR, or posted-document impact.
6. Save approval evidence in the order notes, exception log, CRM activity, or shared documentation location.

### 7.6 Update Systems

#### CRM Update

1. Add a note documenting the customer request, sales approval, reason code, and timestamp.
2. Update customer-facing fields if applicable, such as delivery date, PO number, or order status.
3. Preserve the original request history; do not delete previous notes.

#### ERP Update

1. Update the order line, quantity, price, delivery date, PO number, or internal notes as approved.
2. Enter the change reason code at the header or line level where available.
3. Recalculate order total after quantity or price changes.
4. Confirm tax, discount, promo, and payment terms still calculate correctly according to company workflow.
5. If the order was already released, regenerate or reissue the pick ticket after the update.

#### Inventory / Fulfillment Update

1. Notify Warehouse if the order was released, picked, packed, or staged.
2. Confirm whether removed items are returned to available inventory.
3. Confirm whether added items are picked and staged.
4. Confirm substitution notes are visible to the team executing the order.

#### Compliance / Traceability Update

1. If no manifest exists, validate that the updated order remains eligible for manifest creation.
2. If a manifest exists, do not change product, quantity, ship-to, or delivery timing without Compliance approval.
3. If the manifest must be voided or recreated, document the reason and link the new manifest reference to the order.
4. Package IDs, quantities, destination license, and delivery details must match the final ERP order and fulfillment record.

#### Accounting Update

1. If no invoice exists, confirm the modified order total is ready for later invoice support.
2. If an invoice draft exists, notify Accounting to refresh or hold the invoice until the order is reconciled.
3. If a posted invoice exists, do not edit the original order to force a match. Route to invoice void, return order, or credit memo workflow.

### 7.7 Communicate the Change

Send a concise update to impacted teams. Include the order number, customer, change summary, reason, approval status, and next action.

**Internal update template:**

> Subject: Order Modification Complete — [Order #] — [Customer]  
> The requested change has been completed for [Order #].  
> Change: [old value] → [new value]  
> Reason: [reason code / short description]  
> Approval: [approver / timestamp]  
> Fulfillment impact: [none / pick ticket updated / route impacted / manifest review required]  
> Accounting impact: [none / invoice hold / price update / credit workflow needed]  
> Current status: [status]

**Customer-facing note, if needed:**

> Hi [Name],  
> Your order update has been completed. We adjusted [brief change] and your current delivery timing is [date/window]. Please let us know if anything else needs to be reviewed before fulfillment.

### 7.8 Close the Exception

1. Confirm the CRM, ERP, inventory/fulfillment tracker, and exception log all show the same final status.
2. Confirm no open hold remains unless the order is intentionally paused.
3. Confirm Warehouse/Distribution has the latest pick ticket or delivery instructions.
4. Confirm Accounting knows whether invoicing should proceed, pause, or be corrected.
5. Mark the exception log as resolved and document the final resolution.

---

## 8. Special Handling Rules

### 8.1 Add Item

- Confirm item is active and eligible in the market.
- Confirm inventory availability.
- Confirm pricing and discount logic.
- Notify Warehouse if order was already released.
- Regenerate pick ticket if needed.

### 8.2 Remove Item

- Confirm whether product was already picked or staged.
- If picked, notify Warehouse to return product to available inventory.
- Confirm order total recalculates correctly.
- If manifest was created, Compliance must confirm whether it must be updated, voided, or recreated.

### 8.3 Quantity Increase

- Confirm available-to-sell inventory.
- Confirm revised order still meets delivery timing.
- Confirm revised invoice value and payment terms.
- If the change occurs after pick, Warehouse must confirm additional product can be picked before release.

### 8.4 Quantity Decrease

- Confirm reason: customer request, inventory shortage, partial fulfillment, or correction.
- If the order was picked, Warehouse must return excess product to stock or hold it according to procedure.
- If invoiced, do not simply reduce the order; route to Accounting for invoice correction or credit memo review.

### 8.5 Price Correction

- Confirm approved price list, contract, promo, or manager approval.
- Document the pricing source.
- Obtain Accounting approval if invoice value changes.
- If invoice was posted, route to invoice adjustment or credit memo workflow.

### 8.6 Delivery Date Change

- Confirm customer request and Sales approval.
- Confirm route capacity and delivery cutoff.
- Confirm product remains eligible and available for the new date.
- Confirm manifest timing if the route has already been prepared.

### 8.7 Substitution

- Confirm the original SKU cannot be fulfilled or the customer explicitly approved the substitution.
- Confirm substitute SKU is active, state-eligible, and available.
- Document approval from Sales/customer.
- Update order lines, pick ticket, and manifest details if applicable.

### 8.8 Cancellation Before Fulfillment

- Confirm cancellation request and authorization.
- Check whether the order was released, picked, packed, or manifested.
- Notify Warehouse, Distribution, Compliance, and Accounting as needed.
- Cancel the order only after confirming no physical, compliance, or financial record remains unresolved.
- If the customer still wants product later, create a new order rather than reopening a cancelled audit trail.

---

## 9. Required Exception Log Fields

| Field | Description |
|---|---|
| Exception ID | Unique issue identifier |
| Order Number | CRM / ERP order reference |
| Customer | Customer account name |
| Market | State or region |
| Request Date | Date/time request was received |
| Requestor | Person/team requesting change |
| Change Type | Add, remove, quantity, price, delivery date, cancellation, etc. |
| Reason Code | Standard reason for change |
| SKU / Item | Affected item, if applicable |
| Quantity Before | Original quantity |
| Quantity After | Revised quantity |
| Dollar Impact | Estimated order value change |
| Status at Request | Pending, released, picked, manifested, shipped, delivered, invoiced, etc. |
| Approval Owner | Sales, Inventory, Compliance, Accounting, Distribution, etc. |
| Resolution | Final action taken |
| Close Date | Date issue was resolved |
| Notes / Evidence | Link to email, CRM note, approval, manifest note, or document |

---

## 10. QC Checklist

Before closing the modification, verify:

- [ ] Request and reason code are documented.
- [ ] Order status was checked before editing.
- [ ] Customer account and license remain valid.
- [ ] SKU/item is active and eligible for the market.
- [ ] Quantity and inventory availability are confirmed.
- [ ] Price/discount/promo is approved.
- [ ] Warehouse/Distribution has been notified if fulfillment is impacted.
- [ ] Compliance has approved any manifest, package, destination, or regulated movement impact.
- [ ] Accounting has approved any invoice, price, AR, or credit impact.
- [ ] CRM and ERP notes match.
- [ ] Exception log is updated and closed.
- [ ] No contradictory order, fulfillment, invoice, or manifest status remains open.

---

## 11. Escalation Rules

| Issue | Escalate To | Required Action |
|---|---|---|
| License, ship-to, or account eligibility issue | Compliance + Sales Manager | Hold order until resolved |
| SKU not active or not eligible in market | Product Master / Compliance | Remove SKU or correct master data before release |
| Inventory shortage | Inventory + Sales Rep | Approve partial, substitute, delay, or cancel |
| Post-pick quantity or SKU change | Warehouse + Sales Data Coordinator | Correct pick ticket and inventory before shipment |
| Manifest already created | Compliance + Distribution | Void/recreate/update according to state system process |
| Price or discount correction | Sales Manager + Accounting | Approve corrected price before invoice |
| Posted invoice already exists | Accounting / AR | Use invoice void, return, or credit memo process; do not force-edit order |
| Customer dispute or repeated change issue | Sales Manager + Customer Support | Document customer communication and next steps |

---

## 12. Common Failure Modes to Avoid

- Editing ERP order lines after the warehouse has picked product without notifying Warehouse.
- Changing quantity after a manifest is created without Compliance review.
- Updating CRM notes but not the ERP order.
- Updating the ERP order but not the customer-facing CRM/order status.
- Forgetting to regenerate the pick ticket after a line change.
- Letting an invoice post from stale order data.
- Creating a credit memo when the issue should have been handled as a cancellation or invoice void.
- Closing an exception before confirming physical inventory, ERP status, and compliance records match.

---

## 13. Metrics / KPIs

| KPI | Definition | Purpose |
|---|---|---|
| Order Modification Rate | Modified orders as % of submitted orders | Identifies order intake quality and customer change patterns |
| Same-Day Modification Resolution | % modifications resolved same business day | Measures responsiveness and operational follow-through |
| Post-Release Change Rate | % changes after order release | Flags downstream risk and warehouse disruption |
| Manifest Rework Rate | % modified orders requiring manifest correction | Measures compliance/fulfillment disruption |
| Price Correction Rate | % orders with pricing changes after submission | Identifies pricing master data or promo approval issues |
| Invoice Hold Rate from Modifications | % modified orders held before invoice | Measures financial close risk |
| Repeat Exception Rate | Recurring issue type by customer, SKU, rep, or process | Supports root-cause improvement |

---

## 14. Version History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| 1.0 | 2026-05-17 | Brandon Hardison | Initial simulated SOP for sales order modification controls in a regulated cannabis CPG order lifecycle project |

---

<!-- >>># SOP-OP-002 — Order Modifications, Rejections, Returns, and Refusals

## Objective

Control changes to Oregon sales orders after submission, ensuring all modifications are authorized, documented, and reconciled across CRM, ERP, fulfillment, accounting, and Metrc where applicable.

## Trigger

An order change is requested after initial submission or after fulfillment has started.

Common change types:

- Add item
- Remove item
- Quantity change
- Price correction
- Delivery date change
- Customer refusal
- Partial rejection at delivery
- Full rejection at delivery
- Return request
- Damaged product claim
- Credit memo request

## Procedure

1. **Identify order status.**
   - Determine whether the order is open, released, picked, packed, manifested, delivered, invoiced, or closed.
   - The later the status, the more documentation and approvals are required.

2. **Classify the change type.**
   - Administrative correction
   - Customer-requested modification
   - Inventory-driven shortage
   - Compliance-driven hold
   - Delivery refusal or rejection
   - Post-invoice billing issue

3. **Confirm authorization.**
   - Sales rep may confirm customer-requested changes.
   - Inventory must confirm inventory-driven changes.
   - Compliance must confirm regulated changes.
   - Accounting must approve invoice or credit memo changes.

4. **Update CRM and ERP.**
   - Enter the change reason.
   - Update order lines, quantities, price, status, and notes.
   - Preserve the original order reference and change history.

5. **Coordinate with warehouse and distribution.**
   - If the order has not been picked, notify warehouse to update pick ticket.
   - If the order has been picked but not shipped, confirm whether product must be returned to inventory.
   - If the order has been manifested, escalate before changing physical delivery quantities.

6. **Handle delivery rejection or refusal.**
   - Document rejected package, SKU, quantity, reason, customer contact, driver notes, and timestamp.
   - Confirm whether the customer rejected the full order or specific packages.
   - Coordinate with Compliance / Inventory to ensure system receipt or rejection actions are completed correctly.
   - Notify Accounting if invoice adjustment or credit memo is needed.

7. **Close the exception.**
   - Confirm systems match after the change.
   - Attach supporting notes or documents.
   - Update the exception log with final status and root cause.

## Required Exception Log Fields

| Field | Description |
|---|---|
| Exception ID | Unique issue identifier |
| Order Number | CRM / ERP order reference |
| Customer | Customer account name |
| Market | Oregon |
| Issue Type | Modification, rejection, refusal, return, billing issue, etc. |
| SKU / Package | Item or package affected |
| Quantity Impact | Units/cases affected |
| Financial Impact | Dollar impact if known |
| Owner | Person/team responsible |
| Status | Open, pending, resolved, closed |
| Root Cause | Data entry, inventory shortage, customer request, delivery issue, compliance issue |
| Resolution | Final correction made |
| Close Date | Date issue was resolved |

## QC Checks

- No order line changes without reason code
- No post-manifest changes without Compliance / Inventory involvement
- No invoice adjustment without Accounting review
- No rejected product left unresolved in order status
- No customer-facing issue closed without documented communication -->
