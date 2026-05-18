# SOP-OP-014 — Worker Permit and Delivery Readiness Check

**Document Type:** Standard Operating Procedure — portfolio simulation  
**Process Area:** Sales Operations / Order Lifecycle Management  
**Owner:** Sales Data Coordinator  
**Market Assumption:** Oregon regulated cannabis wholesale / CPG operations  
**Related Systems:** CRM, ERP, inventory/WMS, Metrc / Oregon Cannabis Tracking System (CTS), shared documentation drive, email/Slack  
**Version:** 1.0
**Related SOPs:** SOP-OP-004 Fulfillment, Manifest & Delivery; SOP-OP-007 Manifest Precheck; SOP-OP-008 Delivery Closeout; SOP-OP-013 Audit Packet Assembly

> **Portfolio note:** This SOP is a simulated, role-aligned process document for a cannabis CPG sales operations portfolio project. It is not an official company policy, does not represent any employer's proprietary procedures, and is not legal or regulatory advice. The process language is designed to demonstrate practical order operations, ERP/CRM data quality, documentation control, and compliance-aware escalation.

---

## 1. Purpose

This SOP defines a pre-dispatch readiness check for delivery-related records that support compliant cannabis product transport. The check focuses on required driver, vehicle, route, manifest, documentation, and delivery-window data before product leaves the facility.

The Sales Data Coordinator does not manage HR compliance or approve worker permits. The coordinator verifies that delivery readiness fields are complete according to company workflow and escalates missing information to Distribution or Compliance.

---

## 2. Scope

This SOP applies before outbound delivery when a sales order is ready to move from warehouse staging to dispatch.

Included checks:

- Assigned driver
- Driver license / worker permit readiness indicator according to company process
- Vehicle information
- Delivery route
- Customer receiving location
- Manifest readiness
- Printed or accessible delivery documentation
- Delivery window
- Emergency contact or dispatch contact
- Product security / storage readiness confirmation from Distribution

---

## 3. Regulatory Reference Concepts

Oregon cannabis operations require controlled transport of regulated items. Personnel performing cannabis work may need a valid marijuana worker permit according to role and setting. Vehicle, driver, manifest, origin, destination, product, timing, and documentation details are operational controls used to support compliant transport.

Always defer to Distribution, Compliance, HR, and current Oregon rules for final requirements.

---

## 4. Required Data Fields

| Field | Owner | Review Standard |
|---|---|---|
| Driver name | Distribution | Assigned before dispatch |
| Driver readiness indicator | Distribution / Compliance | Complete according to company process |
| Vehicle make/model | Distribution | Present and matches route plan |
| Vehicle license plate | Distribution | Present and accurate |
| Route / stop sequence | Distribution | Complete before release |
| Origin facility | Compliance / Distribution | Matches manifest/order |
| Destination address | Sales Data Coordinator / Compliance | Matches customer account and manifest |
| Delivery window | Sales / Distribution | Confirmed or documented |
| Manifest number | Compliance / Distribution | Present before dispatch |
| Order number | Sales Data Coordinator | Matches ERP/CRM record |
| Package UID list | Warehouse / Compliance | Present and tied to order |
| Printed/access docs | Distribution | Ready for driver |

---

## 5. Procedure

### Step 1 — Confirm order is dispatch-ready

1. Confirm order has passed intake validation.
2. Confirm order has passed manifest precheck.
3. Confirm no unresolved product hold, customer hold, inventory mismatch, or invoice hold blocks dispatch.
4. If any blocker remains, do not proceed with readiness check until blocker is assigned or cleared.

### Step 2 — Validate driver and route information

1. Confirm assigned driver is listed.
2. Confirm route or delivery stop sequence is assigned.
3. Confirm delivery date, departure window, and estimated arrival window.
4. Confirm customer receiving hours or delivery instructions are attached.
5. Route missing or conflicting route data to Distribution.

### Step 3 — Validate vehicle information

1. Confirm vehicle make/model is present.
2. Confirm license plate is present.
3. Confirm vehicle listed on delivery paperwork matches the planned route record.
4. Escalate any vehicle substitution before dispatch if the manifest or documentation requires update.

### Step 4 — Validate manifest and order references

1. Confirm manifest/CTS reference is present.
2. Confirm order number and customer destination match the manifest.
3. Confirm package UID list matches pick/stage record.
4. Confirm documents are printed or accessible according to company process.

### Step 5 — Confirm release or hold

1. If all readiness fields pass, mark delivery readiness as passed.
2. If any field fails, mark dispatch readiness as failed/pending correction.
3. Assign owner and due time for correction.
4. Notify Distribution and Sales Data Coordinator queue owner if delivery timing is at risk.

---

## 6. No-Dispatch Conditions

Do not clear dispatch readiness if:

- Driver is not assigned
- Driver readiness / permit validation indicator is missing according to company process
- Vehicle information is blank or inconsistent
- Manifest reference is missing
- Destination address differs from customer/manifest record
- Package UID list is missing or mismatched
- Delivery documents are incomplete
- Customer receiving window is unknown for a time-sensitive delivery
- Product hold or inventory exception remains unresolved

---

## 7. Readiness Status Values

Use standardized values:

- READY_FOR_DISPATCH
- PENDING_DRIVER_INFO
- PENDING_VEHICLE_INFO
- PENDING_MANIFEST
- PENDING_ROUTE_CONFIRMATION
- PENDING_CUSTOMER_RECEIVING_WINDOW
- BLOCKED_BY_INVENTORY
- BLOCKED_BY_COMPLIANCE
- BLOCKED_BY_PRODUCT_HOLD
- CANCELLED_OR_RESCHEDULED

---

## 8. Escalation Matrix

| Issue | Escalate To | Required Action |
|---|---|---|
| Missing driver | Distribution | Assign driver or delay route |
| Missing driver readiness indicator | Distribution / Compliance | Confirm required documentation is complete |
| Vehicle change | Distribution + Compliance | Update route/manifest records if required |
| Missing manifest | Compliance / Distribution | Create or provide manifest before release |
| Customer receiving window unknown | Sales / Account Manager | Confirm delivery availability |
| Package UID mismatch | Warehouse + Compliance | Reconcile before driver leaves |
| Route delay threatens delivery window | Distribution + Sales | Notify customer or reschedule |

---

## 9. Evidence / Artifacts

- Dispatch readiness checklist
- Manifest reference
- Route sheet
- Driver assignment
- Vehicle record
- Customer delivery instructions
- Package UID list
- Exception log entry, if applicable
- Final release timestamp

---

## 10. Success Metrics

- Dispatch readiness pass rate
- Number of routes delayed by missing documentation
- Number of missing driver/vehicle exceptions
- Number of delivery failures due to receiving-window mismatch
- Average time to clear dispatch blockers
- Reduction in same-day route corrections
