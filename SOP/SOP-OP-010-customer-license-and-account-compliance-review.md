# SOP-OP-010 — Customer License and Account Compliance Review

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-001 Order Intake & Validation; SOP-OP-002 Order Modification; SOP-OP-007 Manifest Precheck; SOP-OP-013 Compliance Documentation & Audit Packet Assembly

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines how customer account and license data is reviewed before a cannabis sales order is released. The process is designed to prevent orders from moving to fulfillment when the customer record, ship-to location, license identifier, bill-to account, AR status, or compliance status is incomplete, inactive, mismatched, or unapproved.

The Sales Data Coordinator supports account compliance by validating data consistency and escalating discrepancies. The coordinator does not make final legal eligibility decisions unless explicitly authorized by company policy.

---

## 2. Scope

This SOP applies to:

- New customer order intake
- Existing customer order review
- New ship-to or bill-to requests
- Account reactivation
- License or address changes
- CRM-to-ERP account crosswalk updates
- Orders blocked by customer master data issues
- Orders placed for customers with AR, compliance, or account holds

---

## 3. Customer Account Data Elements

The following fields should be complete and aligned before an order is released:

- Customer legal name
- DBA / store name
- Customer account ID
- CRM account ID
- ERP customer number
- License number or approved customer identifier
- License type
- License status
- Ship-to address
- Bill-to address
- Receiving contact
- Buyer contact
- Payment terms
- AR status
- Account hold status
- Compliance hold status
- Delivery lane / route
- Sales rep / account owner
- Tax/resale documentation if used by company process
- Market/state eligibility

---

## 4. Review Triggers

Run this review when:

- A new order is submitted
- A customer requests a ship-to change
- CRM and ERP customer names do not match
- Customer has not ordered recently
- An order fails license, address, or account validation
- Delivery destination differs from the established customer record
- Customer is on AR hold, compliance hold, or inactive status
- A new customer is added to CRM or ERP
- A returned/refused order indicates a possible account data issue

---

## 5. Procedure

### Step 1 — Locate account records

1. Locate the customer in CRM.
2. Locate the corresponding customer in ERP.
3. Locate the customer crosswalk record, if available.
4. Confirm the sales rep or account owner.
5. Confirm whether customer is new, active, inactive, on hold, or pending review.

### Step 2 — Validate identity fields

1. Compare customer legal name, DBA, CRM account ID, and ERP customer number.
2. Confirm no duplicate customer records exist.
3. Confirm aliases or DBA names are documented.
4. If account identity is unclear, pause order release and route to Sales Operations or Customer Master owner.

### Step 3 — Validate license and market eligibility

1. Confirm license number or approved receiving identifier is present.
2. Confirm receiving location is approved for the order's market/state.
3. Confirm the product type is eligible for the receiving account according to company compliance process.
4. Route inactive, missing, expired, or mismatched license data to Compliance.

### Step 4 — Validate ship-to and bill-to data

1. Confirm ship-to address matches approved receiving destination.
2. Confirm bill-to account matches customer payment relationship.
3. Confirm delivery instructions and receiving contact are current.
4. If customer requests delivery to a new location, do not update the order until the location is reviewed and approved.

### Step 5 — Validate AR and account hold status

1. Check AR status, credit hold, payment terms, and account hold fields.
2. If AR hold exists, route to Accounting before release.
3. If customer is inactive or blocked, route to Sales Operations and account owner.
4. Do not bypass account holds through manual order notes.

### Step 6 — Update records and document outcome

1. If data is correct, mark customer review as passed.
2. If data requires correction, update the exception log.
3. Assign the correction owner.
4. Note whether the order is blocked, conditionally approved, or released.
5. Attach evidence or reference the source used to validate the customer record.

---

## 6. Customer Account Status Matrix

| Status | Order Handling |
|---|---|
| Active / Approved | Order may proceed if all order-level checks pass |
| Active with AR hold | Hold order pending Accounting review |
| Active with compliance hold | Hold order pending Compliance review |
| Inactive | Do not release order; route to Sales Operations |
| Duplicate record suspected | Hold until customer master is cleaned or crosswalk confirmed |
| New ship-to requested | Hold until destination is validated |
| License mismatch | Hold pending Compliance decision |
| Missing receiving contact | Request update before release if required for delivery |

---

## 7. Common Exceptions

- CRM account name differs from ERP customer name
- ERP customer number missing from CRM
- Duplicate accounts for one customer
- Ship-to address differs from license/destination record
- Customer has multiple stores but order references wrong location
- AR hold present but order submitted as normal release
- Inactive customer receives new order
- Customer license field blank or stale
- New buyer contact not linked to account
- Customer account uses outdated delivery lane or receiving hours

---

## 8. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| License missing/mismatch | Compliance | Confirm eligibility before release |
| Ship-to address change | Compliance + Distribution | Validate destination and delivery route |
| AR hold | Accounting / AR | Approve release, collect payment, or maintain hold |
| Duplicate customer record | Customer Master Owner | Merge, deactivate, or crosswalk records |
| Account inactive | Sales Operations + Account Manager | Confirm reactivation or reject order |
| Bill-to/ship-to mismatch | Accounting + Sales | Correct customer relationship before invoicing |

---

## 9. Documentation Standards

Every customer-account exception must include:

- Customer name
- CRM account ID
- ERP customer number
- Order number
- Issue type
- Source system showing issue
- Corrected value or requested value
- Owner assigned
- Release decision
- Date/time resolved
- Supporting note or approval reference

---

## 10. Quality Control Checklist

- Customer is active
- CRM and ERP account IDs are linked
- Legal name and DBA are understood
- Ship-to address is approved
- Bill-to account is correct
- License field is present and reviewed
- AR/compliance holds are cleared or assigned
- Sales rep/account owner is listed
- Receiving contact is current
- Exception log updated for any mismatch

---

## 11. Success Metrics

- Percentage of orders passing customer review on first attempt
- Number of account-data holds per week
- Average time to resolve customer/account exceptions
- Duplicate account reduction
- Orders blocked due to license/address mismatch
- Delivery failures caused by customer data issues
