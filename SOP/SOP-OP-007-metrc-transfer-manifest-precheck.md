# SOP-OP-007 — Metrc / CTS Transfer Manifest Precheck

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-001 Order Intake & Validation; SOP-OP-002 Order Modification; SOP-OP-004 Fulfillment, Manifest & Delivery; SOP-OP-009 Daily CTS-to-ERP Inventory Reconciliation; SOP-OP-014 Worker Permit & Delivery Readiness Check

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines the pre-dispatch control process for verifying that every regulated outbound transfer has accurate order, customer, product, quantity, package UID, driver, vehicle, destination, route, and manifest details before product leaves the facility.

The Sales Data Coordinator does not act as the final regulatory approver. The coordinator supports the process by validating order data, identifying mismatches, documenting exceptions, and routing unresolved compliance issues to the appropriate Compliance, Distribution, Inventory, or Accounting owner before release.

---

## 2. Scope

This SOP applies to all Oregon outbound wholesale orders that require a transfer manifest or CTS movement record before delivery.

Included scenarios:

- Standard outbound sales order delivery
- Partial shipment
- Split shipment
- Re-delivery after missed delivery
- Replacement shipment
- Transfer involving corrected item, package, or quantity data
- Route change prior to dispatch
- Same-day manifest correction before product leaves the facility

Excluded scenarios:

- Product already delivered and accepted by customer
- Product already rejected/refused at customer location
- Post-delivery return authorization
- Internal non-sale inventory adjustments
- Destruction, testing, or sampling workflows outside the sales order process

---

## 3. Regulatory Reference Concepts

This SOP is based on common Oregon cannabis operations control points, including:

- Regulated cannabis item movement must be tracked in CTS / Metrc.
- Transported product must be associated with accurate package, quantity, origin, destination, and route information.
- The driver, vehicle, departure timing, arrival timing, and receiving location must be controlled before dispatch.
- Printed or accessible transport documentation should accompany the physical movement according to company and regulatory process.
- Large or unusual transfers may require additional review before movement.

Always defer to the employer's Compliance team and current Oregon rules for the final requirement.

---

## 4. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Sales Data Coordinator | Verify CRM/ERP order details against fulfillment and manifest data; log exceptions; coordinate corrections; confirm release readiness |
| Sales Representative / Account Manager | Confirm customer intent, delivery date, substitutions, and customer-facing changes |
| Inventory / Warehouse | Confirm picked product, package UID, lot/batch, quantity, and staging readiness |
| Distribution | Confirm route, driver, vehicle, delivery window, and dispatch readiness |
| Compliance | Review license, CTS, package UID, destination, transfer, and manifest issues |
| Accounting / AR | Confirm invoice hold, invoice timing, or billing impact if manifest/order data changes |
| Customer / Retailer | Receives order and confirms acceptance, rejection, or discrepancy at delivery |

---

## 5. Required Inputs

Before the order is released for dispatch, collect or confirm the following:

- ERP sales order number
- CRM order reference, if different
- Customer legal name and DBA
- Customer license number or approved receiving identifier
- Ship-to address
- Bill-to account
- Delivery date and delivery window
- Sales representative / account owner
- SKU / item number
- Product name and unit size
- Quantity ordered
- Quantity picked
- Package UID / tag ID
- Lot or batch reference, if applicable
- Manifest or CTS transfer number
- Origin license / facility
- Destination license / facility
- Driver name
- Worker permit confirmation, if applicable to the delivery role
- Vehicle make/model/license plate
- Planned departure and estimated arrival times
- Route or delivery stop sequence
- Special handling requirements, if applicable

---

## 6. Procedure

### Step 1 — Confirm the order is eligible for manifest precheck

1. Locate the order in ERP and CRM.
2. Confirm the order status is ready for fulfillment review, not cancelled, rejected, refused, delivered, or invoiced-only.
3. Confirm there are no unresolved holds:
   - AR hold
   - license hold
   - inventory hold
   - compliance hold
   - product hold
   - pricing hold
   - missing required customer data
4. If an unresolved hold exists, stop the release process and update the exception log.

### Step 2 — Validate customer and destination data

1. Compare customer legal name, DBA, customer ID, and ship-to address across CRM, ERP, customer master, and manifest/CTS record.
2. Confirm the destination is active and approved for the Oregon market.
3. Confirm the ship-to location matches the destination on the manifest.
4. Flag any mismatch before dispatch.

### Step 3 — Validate SKU, package, and quantity data

1. Compare ERP order lines to the warehouse pick record.
2. Compare warehouse picked quantities to package UID quantities.
3. Confirm each package UID corresponds to the correct SKU/item, product name, unit size, and unit count.
4. Confirm no expired, quarantined, blocked, or state-ineligible product is included.
5. Confirm partial shipments are intentionally documented and approved.
6. If package UID or quantity data does not match, stop release and escalate to Inventory and Compliance.

### Step 4 — Validate route, driver, and vehicle data

1. Confirm driver is assigned.
2. Confirm delivery vehicle information is complete.
3. Confirm planned departure and arrival window.
4. Confirm route or delivery stop sequence is consistent with the manifest.
5. Confirm printed or accessible delivery documents are ready.
6. Route missing driver, vehicle, or destination information to Distribution before release.

### Step 5 — Confirm invoice and order-status handling

1. Determine whether the order will be invoiced before dispatch, after dispatch, or after delivery confirmation according to company process.
2. Confirm no invoice is generated from an incorrect quantity, SKU, package, or destination record.
3. If the order is partially fulfilled, confirm invoice handling with Accounting.
4. If the manifest requires a quantity reduction or substitution, confirm ERP order lines are corrected before invoice generation.

### Step 6 — Record precheck outcome

1. Update the order status to indicate manifest precheck result:
   - Precheck Passed
   - Precheck Failed — Correction Required
   - Pending Compliance Review
   - Pending Inventory Review
   - Pending Distribution Review
2. Add notes explaining any correction made.
3. Attach or reference the manifest number in the order record or documentation log.
4. Confirm release to Distribution only after all blockers are cleared.

---

## 7. No-Ship Conditions

Do not release the order for dispatch if any of the following are true:

- Customer license or destination cannot be validated
- Manifest destination does not match ERP ship-to address
- Package UID is missing or incorrect
- Picked quantity does not match order or manifest quantity
- SKU/item mapping is unresolved
- Product is blocked, quarantined, expired, recalled, or not eligible for the Oregon market
- Driver or vehicle information is missing
- Route or delivery timing is incomplete
- Compliance hold is unresolved
- Accounting has placed an invoice or AR hold on the order
- Required documentation is missing

---

## 8. Exception Log Requirements

For every failed precheck, log:

- Exception ID
- Date/time identified
- Order number
- Customer
- Manifest or CTS reference, if available
- Exception type
- Field causing mismatch
- Source system of mismatch
- Owner assigned
- Required correction
- Approval required
- Status
- Date/time resolved
- Final release decision

---

## 9. Quality Control Checklist

Before release, confirm:

- Customer and license data match across systems
- Ship-to address matches manifest destination
- All SKUs are active and eligible
- Package UID list is complete
- ERP order quantity equals picked quantity or approved partial quantity
- Manifest quantity equals staged quantity
- Driver and vehicle fields are complete
- Delivery date and route are confirmed
- No unresolved holds remain
- Release decision is documented

---

## 10. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| License or ship-to mismatch | Compliance + Sales | Validate receiving location before release |
| Package UID mismatch | Inventory + Compliance | Correct package record or repick order |
| Quantity mismatch | Warehouse + Sales Data Coordinator | Determine shortage, partial shipment, or pick correction |
| SKU ineligible for market | Compliance + Product Master Owner | Block shipment and correct item eligibility |
| Missing driver/vehicle info | Distribution | Complete dispatch record before release |
| Invoice generated from incorrect data | Accounting | Void/correct invoice or place invoice hold |
| Customer change after manifest created | Sales + Distribution + Compliance | Determine if modification or new manifest is required |

---

## 11. Evidence / Artifacts

- ERP order record
- CRM order record
- Pick ticket or warehouse staging record
- Manifest / CTS reference
- Package UID list
- Customer/license validation notes
- Driver/vehicle readiness confirmation
- Exception log entry, if applicable
- Release approval timestamp

---

## 12. Success Metrics

- Orders released with zero manifest/order mismatches
- Manifest precheck pass rate
- Number of no-ship exceptions caught before dispatch
- Average time to resolve manifest blockers
- Reduction in delivery refusals caused by order or manifest errors
- Reduction in invoice corrections caused by fulfillment data errors
