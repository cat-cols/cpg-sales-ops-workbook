# SOP-OP-013 — Compliance Documentation and Audit Packet Assembly

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-002 Order Modification; SOP-OP-003 Returns & Refusals; SOP-OP-005 Invoicing & Credit Memo Support; SOP-OP-007 Manifest Precheck; SOP-OP-008 Delivery Closeout

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines how to assemble a complete documentation packet for sales order exceptions involving regulated product movement, order modifications, delivery refusals, returns, invoice corrections, credit memos, inventory discrepancies, or customer/license issues.

The purpose is to create a clear audit trail showing what happened, who reviewed it, what was corrected, and which systems were updated.

---

## 2. Scope

An audit packet should be assembled for:

- Order modification after release
- Manifest or package UID mismatch
- Partial shipment
- Delivery rejection or refusal
- Customer return
- Credit memo request
- Invoice correction
- Inventory discrepancy affecting an order
- Customer/license/address mismatch
- Product hold or stop-ship event
- High-value pricing correction
- Repeated exception or unresolved aged issue

---

## 3. Guiding Principles

1. **Tell the full story.** A reviewer should understand the order lifecycle without asking for scattered emails.
2. **Separate facts from interpretation.** Document what happened, what source shows it, and who approved the correction.
3. **Preserve original references.** Do not overwrite or delete the original order/invoice/manifest evidence.
4. **Link every correction to an owner and date.**
5. **Do not close an exception without final system-status confirmation.**

---

## 4. Required Packet Elements

| Element | Required When |
|---|---|
| Original order | All audit packets |
| Modified order | Order changed after submission |
| CRM record | CRM-originated order or customer issue |
| ERP sales order | All order lifecycle exceptions |
| Invoice | Invoice issued or invoice impact exists |
| Credit memo | Customer balance correction exists |
| Manifest / CTS reference | Regulated product movement or delivery issue |
| Package UID list | SKU/package/quantity issue exists |
| Pick ticket / warehouse record | Fulfillment or quantity issue exists |
| Proof of delivery | Delivery acceptance/rejection/refusal issue exists |
| Customer communication | Customer requested change, disputed order, or refused product |
| Internal approval | Price, credit, compliance, inventory, or management decision |
| Exception log entry | All packets |
| Final resolution note | All packets |

---

## 5. Packet Naming Convention

Use a consistent naming structure:

```text
YYYY-MM-DD_OrderNumber_Customer_ExceptionType
```

Examples:

```text
2026-05-26_SO-10239_GreenPlanet_PartialRefusal
2026-05-26_SO-10244_Kaleafa_InvoiceCorrection
2026-05-26_SO-10251_Cannabliss_ManifestMismatch
```

---

## 6. Procedure

### Step 1 — Determine packet requirement

1. Review the exception type.
2. Determine whether a formal audit packet is required based on scope, value, compliance impact, or management request.
3. If unsure, create a packet. It is better to over-document a material regulated-product exception than leave context scattered.

### Step 2 — Create packet folder

1. Create a folder using the naming convention.
2. Add a `summary.md` or summary note.
3. Link the folder path in the exception log.
4. Assign packet owner and due date.

### Step 3 — Add source records

Collect all relevant records:

- CRM order/request record
- ERP sales order
- Posted invoice or invoice draft
- Credit memo, if applicable
- Manifest/CTS reference
- Warehouse pick/stage record
- Delivery confirmation
- Customer email/approval
- Internal approval notes
- Exception log export

### Step 4 — Create summary timeline

The summary should include:

- original order date
- customer
- order number
- affected SKU/package/quantity
- issue detected date/time
- who detected issue
- root issue category
- systems affected
- actions taken
- approvals received
- final outcome
- open follow-up items

### Step 5 — Validate system closeout

Before closing packet, confirm final status in:

- CRM
- ERP
- inventory/WMS
- CTS/Metrc or assigned Compliance record
- invoice/AR record
- customer communication log
- exception log

### Step 6 — Archive and report

1. Mark packet complete in exception log.
2. Add final resolution code.
3. Include packet in weekly exception review if the issue was high-risk or recurring.
4. Archive according to company document retention process.

---

## 7. Summary Template

```markdown
# Audit Packet Summary

Order Number:
Customer:
Date Opened:
Exception Type:
Detected By:
Affected SKU(s):
Affected Package UID(s):
Invoice Number, if applicable:
Manifest/CTS Reference, if applicable:

## What Happened

## Systems Affected
- CRM:
- ERP:
- Inventory/WMS:
- CTS/Metrc:
- Accounting/AR:

## Actions Taken

## Approvals / Owners

## Final Resolution

## Preventive Follow-Up
```

---

## 8. Common Packet Types

| Packet Type | Required Focus |
|---|---|
| Order Modification | Original request, approval, old vs new order values |
| Manifest Mismatch | Package UID, quantity, destination, correction owner |
| Return / Refusal | Customer reason, custody status, inventory and invoice outcome |
| Credit Memo | Original invoice, credit reason, approval, customer balance impact |
| Inventory Variance | Source reports, quantity difference, impacted orders, final adjustment owner |
| Product Hold | Hold notice, affected orders, release/disposition approval |
| Customer Account Issue | Customer records, license/address validation, correction record |

---

## 9. Escalation Matrix

| Documentation Gap | Escalate To | Required Action |
|---|---|---|
| Missing customer approval | Sales / Account Manager | Obtain written confirmation or document customer call notes |
| Missing proof of delivery | Distribution | Provide signed POD or approved delivery note |
| Missing manifest reference | Compliance | Provide CTS/Metrc reference or disposition note |
| Missing invoice/credit memo support | Accounting | Provide posted document or approval note |
| Conflicting system status | Sales Operations | Assign owner to reconcile systems before closure |
| Packet aging unresolved | Sales Operations Manager | Review blocker and set due date |

---

## 10. Quality Control Checklist

- Folder follows naming convention
- Summary note is complete
- Original order included
- Modified/final order included if applicable
- Invoice/credit memo included if applicable
- Manifest/CTS reference included if applicable
- Package UID list included if applicable
- Proof of delivery included if applicable
- Customer/internal approval included
- Final CRM/ERP/CTS/invoice status documented
- Exception log links to packet

---

## 11. Success Metrics

- Audit packets completed within target timeframe
- Percentage of high-risk exceptions with complete documentation
- Number of packets reopened due to missing evidence
- Average age of incomplete packets
- Reduction in repeated documentation gaps
