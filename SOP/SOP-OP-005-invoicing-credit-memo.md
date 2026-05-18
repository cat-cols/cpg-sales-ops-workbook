# SOP-005 — Invoicing and Credit Memo Support

## Objective

Ensure invoices and credit memos accurately reflect fulfilled orders, accepted product, pricing terms, and approved adjustments.

## Trigger

Order is delivered, partially delivered, rejected, returned, or otherwise ready for financial posting.

## Procedure — Invoice Support

1. **Confirm fulfillment status.**
   - Verify delivered quantity and accepted product.
   - Confirm no unresolved rejection, refusal, or return issue exists.

2. **Validate invoice fields.**
   - Customer account
   - Bill-to address
   - Ship-to address
   - Order number
   - Delivery date
   - SKU/item number
   - Quantity
   - Unit price
   - Discount or promo
   - Tax/treatment if applicable by company policy
   - Payment terms

3. **Compare order vs fulfillment vs invoice.**
   - Order quantity should equal fulfilled/accepted quantity unless a partial delivery or rejection occurred.
   - Invoice price should match approved ERP pricing or authorized override.
   - Invoice customer should match order customer and delivery customer.

4. **Release invoice or route issue.**
   - If clean, support Accounting in invoice posting.
   - If discrepant, hold or flag invoice according to company workflow.

## Procedure — Credit Memo Support

1. **Confirm credit memo reason.**
   - Return
   - Refusal
   - Rejection
   - Damaged product
   - Pricing correction
   - Duplicate invoice
   - Short shipment

2. **Collect support.**
   - Original order number
   - Original invoice number
   - Customer account
   - SKU and quantity
   - Dollar amount
   - Reason code
   - Approval notes
   - Delivery/refusal documentation if applicable

3. **Validate against systems.**
   - Confirm product and quantity were originally invoiced.
   - Confirm returned/rejected quantity does not exceed original quantity.
   - Confirm the credit amount uses approved pricing.

4. **Coordinate approval.**
   - Sales approves customer-facing adjustment.
   - Accounting approves financial posting.
   - Compliance / Inventory confirms regulated product handling where applicable.

5. **Close loop.**
   - Update CRM/ERP notes.
   - Update exception log.
   - Confirm customer communication is complete.

## QC Checks

- No invoice posted for undelivered product unless company policy allows pre-billing.
- No credit memo without original invoice reference.
- No credit amount exceeding original line amount.
- No unresolved delivery exception before final invoice close.
- No open order left in contradictory status after credit memo processing.