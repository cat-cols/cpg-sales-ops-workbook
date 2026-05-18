# SOP-OP-001 — Oregon Sales Order Intake and Validation

## Objective

Ensure every Oregon sales order is complete, accurate, compliant, and ready for fulfillment before it is released to warehouse, distribution, and accounting workflows.

## Trigger

A new order is submitted through CRM, email, portal, EDI, sales rep request, or other approved intake channel.

## Required Inputs

- Customer legal name and DBA
- Customer account ID
- Oregon license number or approved customer identifier
- Ship-to address
- Bill-to account
- Sales representative
- Requested delivery date
- SKU / item number
- Product name
- Ordered quantity
- Unit price or approved price list
- Discount, promotion, or trade allowance if applicable
- Payment terms or AR status
- Special delivery instructions
- Internal notes or compliance flags

## Procedure

1. **Create or locate the order record.**
   - Confirm whether the order already exists in CRM or ERP.
   - If a duplicate exists, do not create a second order. Update the existing order or escalate for review.

2. **Validate customer account status.**
   - Confirm the account is active.
   - Confirm the ship-to location is approved for the Oregon market.
   - Confirm there are no account holds, AR holds, license holds, or compliance holds.

3. **Validate license and destination details.**
   - Confirm the license number and destination address match approved customer records.
   - Confirm the destination is eligible to receive the product type being ordered.
   - Escalate any license mismatch, inactive account, or address discrepancy before fulfillment.

4. **Validate SKU and product eligibility.**
   - Confirm each SKU is active and sellable in Oregon.
   - Confirm product type, size, unit count, and naming are consistent between CRM, ERP, inventory, and product master data.
   - Confirm discontinued, quarantined, expired, or blocked inventory is not released.

5. **Validate quantity and inventory availability.**
   - Check available-to-sell inventory.
   - Identify shortages, substitutions, partial fulfillment options, or backorder needs.
   - Obtain sales approval before substituting products.

6. **Validate pricing and discounts.**
   - Confirm unit price matches approved price list, contract, or promo authorization.
   - Confirm discounts are within approved limits.
   - Escalate pricing exceptions before invoice creation.

7. **Validate required order fields.**
   - Confirm all required fields are present before moving order status forward.
   - Missing fields must be resolved with the sales rep or customer before release.

8. **Release to fulfillment.**
   - Once validated, update order status to approved/released according to ERP workflow.
   - Notify Warehouse / Distribution if the order is time-sensitive, high-priority, or delivery-constrained.

## QC Checks

- No blank customer account ID
- No blank ship-to address
- No inactive customer accounts
- No inactive SKUs
- No negative or zero order quantities
- No unapproved discounts
- No duplicate order numbers
- No orders released with unresolved license, pricing, or inventory holds

## Evidence / Artifacts

- Validated sales order record
- Order exception log, if applicable
- Pricing approval, if applicable
- Customer/license validation notes, if applicable
- Fulfillment release timestamp

## Escalation Rules

| Issue | Escalate To | Required Action |
|---|---|---|
| License mismatch | Compliance + Sales Manager | Hold order until resolved |
| AR hold | Accounting / AR | Hold order until cleared |
| SKU not active in Oregon | Product Master / Compliance | Remove SKU or correct master data |
| Insufficient inventory | Inventory + Sales Rep | Approve partial, substitute, or delay |
| Pricing exception | Sales Manager + Accounting | Approve or correct before invoice |
