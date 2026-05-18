### Wyld Internal Standard Operating Procedure

| **Document Title:** | SOP-OP-003: Processing Customer Returns & Refusals |
| :--- | :--- |
| **SOP Owner:** | Sales Data Coordinator |
| **Version:** | 1.0 |
| **Effective Date:** | 26-May-2026 |
| **Approved By:** | Director of Sales Operations |
| **Related Systems:** | Microsoft Dynamics 365 Business Central (ERP), Salesforce (CRM), State Traceability System (e.g., Metrc) |

---

#### 1.0 Purpose
This Standard Operating Procedure details the end-to-end process for managing and executing customer returns and delivery refusals. Adherence to this SOP ensures that all physical product returns are accurately reflected in financial records (ERP) and remain perfectly synchronized with the state-mandated compliance inventory (Metrc). A failure in this process can lead to inventory shrinkage, incorrect customer billing, and critical state compliance violations.

#### 2.0 Scope
This procedure applies to the Sales Data Coordinator and covers two primary scenarios:
- **Standard Return:** A dispensary requests to return previously delivered and accepted product (e.g., damaged packaging, short-dated product).
- **Delivery Refusal:** A delivery driver is refused acceptance of a shipment at the dispensary's point of receipt, and the product is returned to Wyld without being accepted into the dispensary's inventory.

#### 3.0 Definitions
- **RMA (Return Merchandise Authorization):** An internal or external document that pre-approves a return before the physical product is shipped back to Wyld.
- **Return Order:** The transactional document in Business Central that records the physical receipt of product and initiates the credit process.
- **Credit Memo:** The financial document in Business Central that officially reduces the customer’s outstanding balance.
- **Traceability Manifest:** The digital chain-of-custody record in the state system (Metrc) that tracks the product’s legal movement between licenses.

---

#### 4.0 Procedure: Process Flow

##### 4.1 Phase 1: Initiating the Return (The RMA)

1.  **Receive and Qualify the Request:** The Sales Data Coordinator receives a return request via email from either the Sales Rep (internal) or directly from the dispensary buyer (external). The request must include: the original Wyld Sales Order or Invoice number, a list of products and quantities to be returned, and the explicit reason for return.
2.  **Verify in the ERP (Business Central):**
    a.  Open the original **Posted Sales Invoice** in Business Central.
    b.  Verify that the products and quantities being requested for return are present on the original invoice and that the invoice date is within the allowed return window (e.g., 30 days, per company policy).
    c.  Verify that the product's lot/batch number is not expired, as expired product cannot be legally received back into a cannabis inventory in most states.
3.  **Secure Internal Approval:** If the return value exceeds a defined threshold (e.g., $500.00), forward the request with your verification notes to the Sales Director and Accounting for email approval *before* proceeding. Attach this approval chain to the RMA record.
4.  **Create the RMA in the ERP:**
    a.  In Business Central, navigate to **Sales Orders** > **New**.
    b.  Set the document type to **Return Order**.
    c.  Link the return to the original **Posted Sales Invoice** number. This auto-populates critical financial costing data.
    d.  Enter the exact items and quantities to be returned. Add a line comment clearly stating the "Reason for Return" (e.g., "Customer reports 3 cases of Sour Apple gummies with damaged outer tin. RA approved by Sales Dir. [Name] on [Date].").
    e.  Set the **Return Reason Code** on each line from the pre-defined drop-down (e.g., DAMAGED, SHORT_DATE).

---

##### 4.2 Phase 2: The Digital Compliance Reconciliation (Metrc)

This is the most critical step. The product cannot physically move until the digital traceability record is in place.

1.  **Locate the Original Manifest:** In the state traceability system (Metrc), find the original outgoing manifest from the initial delivery.
2.  **Create a Return Manifest:**
    a.  Initiate a **New Transfer** from the customer's license *back to* Wyld's license.
    b.  Populate the manifest with the exact product tags (UIDs) from the original delivery, if known. If not, select the matching product category.
    c.  In the "Notes" field, directly reference both the original Metrc Manifest ID and your new Business Central Return Order number. **Example:** "Return per Wyld RMA # RO-000452. Orig Manifest # WA-2026-05-15-00123."
3.  **Validate Sync:** Perform a mental cross-reference check. The quantities on your Business Central Return Order must match the quantities on the Metrc Return Manifest exactly. Any mismatch is a compliance discrepancy that must be resolved before the product can be physically returned.

---

##### 4.3 Phase 3: Physical Receipt and Financial Close

1.  **Coordinate with Inventory/Receiving:** Notify the Warehouse team that a return is expected and provide the Business Central Return Order number. They will physically receive the product, inspect it, and confirm the count.
2.  **Post the Receipt:** Once the warehouse confirms the items are physically in the vault and the Metrc manifest is accepted, post the **Receive** function on the Return Order in Business Central. This adds the inventory back into the system.
3.  **Create and Post the Credit Memo:**
    a.  From the posted Return Receipt, use the **Create Credit Memo** function in Business Central.
    b.  Verify the credit amount matches the original invoiced price exactly.
    c.  Post the Credit Memo. This formally reduces the customer's Accounts Receivable balance.
4.  **Final Communication:**
    a.  Send an email to the Sales Rep, the Accounting team, and the customer (if direct contact is established). Attach the final Posted Credit Memo. The email body should be clear and professional: "Please find the attached credit memo for the approved return of damaged product from your order # SO-001234. This credit has been applied to your account. Please let me know if you have any questions."

---

### Wyld Internal Standard Operating Procedure

| **Document Title:** | SOP-OP-004: Handling On-Site Delivery Refusals |
| :--- | :--- |
| **SOP Owner:** | Sales Data Coordinator |
| **Version:** | 1.0 |
| **Effective Date:** | 26-May-2026 |

---

#### 1.0 Purpose
To define the urgent, real-time procedure for reconciling a shipment that has been refused by a dispensary at the point of delivery. This process prioritizes immediate inventory accuracy and compliance reconciliation to prevent "ghost" inventory and financial errors.

#### 2.0 Procedure: The Real-Time Refusal Workflow

This scenario requires immediate action. The Sales Data Coordinator is the central coordinator between the driver in the field and the systems.

1.  **Receive Immediate Notification:** The delivery driver or Distribution Manager will contact you via phone or urgent message with the following information: the original Sales Order number, the reason for refusal ("vault full," "no buyer on site," "order error"), and confirmation that the physical product is in the driver's possession and returning to Wyld.

2.  **Locate and Halt the Order in the ERP:**
    a.  Immediately pull up the original **Sales Order** in Business Central.
    b.  If the order status is "Released" or "Shipped," you must **Un-Ship** or cancel the posted shipment, which re-opens the order. This reverses the incorrect inventory deduction.

3.  **Reverse the Traceability Manifest (Metrc):**
    a.  In Metrc, locate the active outgoing manifest created for that delivery route.
    b.  Reject or void the manifest in the state system, documenting the reason for refusal in the system notes. **Example:** "Manifest refused at delivery by [Dispensary Name] on 5/26/26. Reason: Vault at capacity. Product returning to Wyld inventory via driver [Driver Name]."
    c.  This step legally documents that the product never transferred custody to the dispensary. This is non-negotiable.

4.  **Reconcile Physical and Digital Inventory:**
    a.  Confirm with the driver/warehouse that the physical product is being re-entered into Wyld's secure storage.
    b.  Ensure the ERP now accurately reflects this quantity as "Available" inventory.
    c.  The original Sales Order is now canceled. Notify the Sales Rep immediately: "Order # SO-001235 for [Dispensary] was refused on-site due to a full vault. The product is safely back in our inventory and the state manifest has been voided. I will cancel this order. Please coordinate with the buyer for a new delivery date, at which point a completely new order will be generated to ensure a fresh audit trail."

5.  **Do Not Issue a Credit Memo:** For a refusal where the product never legally changed hands, you do not issue a credit memo. You simply cancel the transaction completely before it reaches the invoicing stage. If the original order was already invoiced prematurely, you will cancel the invoice, which is handled differently than a return-based credit memo. Consult Accounting if an invoice was already posted.