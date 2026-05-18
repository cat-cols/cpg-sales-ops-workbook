># SOP-006 — Daily Sales Order Data Quality Review

## Objective

Identify and resolve data quality issues across sales orders, customers, products, fulfillment, and invoicing before they become customer, compliance, or accounting problems.

## Trigger

Run daily before fulfillment cutoff and again after delivery/invoice updates where workload allows.

## Daily Review Queries / Reports

| Report | Purpose |
|---|---|
| Open Orders Missing Required Fields | Catch incomplete orders before release |
| Orders on Hold | Monitor AR, compliance, inventory, or pricing holds |
| Orders Released Not Fulfilled | Identify aging orders waiting on warehouse action |
| Fulfilled Not Invoiced | Prevent billing delays |
| Delivered With Rejection / Refusal | Ensure credit or correction workflow is started |
| Price Override Report | Review unapproved discount or price exceptions |
| SKU Master Exceptions | Identify inactive, blocked, or unmapped products |
| Customer Master Exceptions | Identify missing license, address, or account status issues |
| Order vs Invoice Variance | Reconcile sales order value to posted invoice value |

## Standard Daily Procedure

1. Export or refresh daily order QC reports.
2. Filter to Oregon market orders.
3. Sort issues by risk:
   - Compliance / license / manifest issues
   - Customer delivery issues
   - Invoice or credit memo issues
   - Inventory or SKU issues
   - Administrative cleanup
4. Assign owner and due date for each open issue.
5. Resolve same-day issues before delivery or invoice cutoff where possible.
6. Update exception log.
7. Send daily summary to Sales Ops / Distribution / Accounting stakeholders.

## Daily Summary Template

**Subject:** Oregon Sales Order QC Summary — [Date]

**Open Orders Reviewed:** [count]
**Orders Cleared for Fulfillment:** [count]
**Orders on Hold:** [count]
**Delivery Exceptions:** [count]
**Invoice/Credit Issues:** [count]
**Highest-Risk Items:**
- [Issue 1]
- [Issue 2]
- [Issue 3]

**Actions Needed Today:**
- [Owner] — [Action] — [Deadline]

---

# SOP Metrics / KPIs

| KPI | Definition | Why It Matters |
|---|---|---|
| Order Entry Accuracy Rate | % orders without required-field or pricing corrections | Measures data quality |
| Same-Day Issue Resolution Rate | % order exceptions resolved same business day | Measures operational responsiveness |
| Fulfilled Not Invoiced Aging | Orders delivered but not invoiced after cutoff | Protects cash collection |
| Order-to-Invoice Variance | Difference between order value and invoice value | Catches pricing/quantity issues |
| Delivery Rejection Rate | % deliveries with customer rejection/refusal | Highlights sales, inventory, or expectation issues |
| Credit Memo Rate | Credit memos as % of invoices | Measures downstream order quality |
| On-Time Fulfillment Rate | % orders delivered on requested/committed date | Measures operational execution |