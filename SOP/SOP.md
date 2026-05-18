
# THE MYLD WAY
## SALES OPERATIONS PLAYBOOK
### Order Modifications & Reverse Logistics
#### Because even the best trails sometimes require a backtrack.
&nbsp;

---

## MYLD STANDARD OPERATING PROCEDURE

| **Document Title:** | SOP-SO-003: Managing Returns & Refusals |
| :--- | :--- |
| **Document Owner:** | Sales Data Coordinator |
| **Version:** | 1.0 |
| **Last Updated:** | May 26, 2026 |
| **Approved By:** | Director of Sales Operations |
| **Trail Map (Systems):** | Business Central (ERP), Salesforce (CRM), State Traceability (Metrc/BioTrack) |

---

### 1.0 THE WHY: OUR PILLARS IN ACTION

At Myld, we don't just move product; we steward relationships and protect the integrity of every trail we blaze. How we handle a return is just as critical as how we land a new account. A seamless, compliant, and professional reverse logistics process does three things:

- **Protects the Brand:** We make it easy and professional for our dispensary partners, reinforcing that Myld is the best brand to do business with.
- **We Mean Business:** We protect revenue and inventory accuracy. A sloppy return is a financial leak. A precise one is a closed loop.
- **Embraces Our Commitment:** We respect the regulated communities we operate in. Every return must be a perfect, auditable, compliant transaction that honors our responsibility to state regulatory frameworks.

---

### 2.0 THE TRAILHEAD: WHEN THIS SOP APPLIES

This playbook is your guide for two distinct scenarios on the trail:

- **The Planned Return:** A dispensary partner has already accepted a delivery and later requests to send product back. Think damaged packaging, a short-dated product concern, or a mutually agreed-upon stock rotation.
- **The On-Site Refusal:** Our driver is on the dispensary's loading dock, and the shipment is refused in real-time. The product never leaves our custody chain. This requires an immediate, high-urgency response.

---

### 3.0 THE COMPASS: KEY TERMS BEFORE YOU START

| Term | What It Really Means |
| :--- | :--- |
| **RMA (Return Merchandise Authorization)** | A formal, pre-approved agreement to bring product back. Never accept a return without one. This is your permission slip. |
| **Return Order** | The operational document in Business Central that receives the product back into our inventory. It reverses the fulfillment. |
| **Credit Memo** | The financial document that makes our partner whole. It's a negative invoice, reducing what they owe. |
| **Traceability Manifest** | The legal, digital chain-of-custody document in the state system. It's the record that proves to regulators exactly where our product is at all times. Treat it with the seriousness of a legal document, because it is. |

---

### 4.0 BLAZING THE TRAIL: THE PROCEDURES

---

&nbsp;
<p align="center"><strong>:::: TRAIL ONE ::::</strong></p>
<h3 align="center">THE PLANNED RETURN</h3>
<p align="center"><em>"Make a Mark by making it right."</em></p>
&nbsp;

---

| Step | Action | The Myld Way Mindset |
| :---: | :--- | :--- |
| **1** | **Receive & Qualify the Signal.** A return request comes in via email from a Sales Rep or a partner. It must have: the original Myld order/invoice number, the exact items and quantities coming back, and the *real reason* for the return. A vague reason hides a potential systemic problem we need to fix. | **Be curious.** A return is a signal. Is there a packaging issue we need to escalate to production? Is a partner struggling to sell a specific SKU? Your insight here is valuable. |
| **2** | **Verify in the ERP (Business Central).** Pull up the original **Posted Sales Invoice**. Confirm the products were actually on that invoice and are within our return window (typically 30 days). Critically, check the lot/batch expiration date. We cannot legally bring expired product back into our vault in most states. | **Be precise.** This is your data integrity moment. Approving a return for something that was never on the original invoice is a self-inflicted wound. |
| **3** | **Secure Approval (If Needed).** If the return value is over $500, pause. Forward the verified request to the Sales Director and Accounting for an email blessing. Save that email chain to the RMA record. No exceptions. | **We Mean Business.** This is about shared responsibility and financial controls, not bureaucracy. Protect yourself and the company. |
| **4** | **Build the RMA in Business Central.** Create a new document, setting the type to **Return Order**. Link it to the original **Posted Sales Invoice**. Populate the exact return items and quantities. In the line comments, write the full story: *"Customer return per RA request from Sarah Chen. Reason: 3 cases Sour Apple gummies with dented tins. Approved by Sales Dir. M. Thompson on 5/26/26."* | **Document like an auditor is reading over your shoulder.** Because one day, they might be. |
| **5** | **Reconcile the Compliance Trail (Metrc).** This is the step that protects our license. Go into the state traceability system. Create a return transfer from the partner's license back to ours. In the notes, directly cross-reference your Business Central RMA number. The quantities on the RMA and the Metrc manifest must be a 100% match. | **Own the full lifecycle.** The financial record and the compliance record are two sides of the same coin. They must be perfectly aligned, and you are the guarantor of that alignment. |
| **6** | **Coordinate the Physical Return.** Notify the warehouse team (Distribution) that an RMA is active. Give them the RMA number. They handle the physical receipt and inspection. | **Be the central hub.** You are the information bridge to the physical world of the vault. |
| **7** | **Receive & Credit (Close the Loop).** Once the warehouse confirms the product is back in the vault, post the **Receive** action on the Return Order. Then, use the **Create Credit Memo** function to post the financial credit. This makes the partner whole and corrects our accounts. | **Finish what you start.** A return isn't done when the product is back. It's done when the partner's account is corrected and they have the paperwork in hand. |
| **8** | **Broadcast the Signal.** Send a clean, professional email to the Sales Rep, Accounting, and the partner (if appropriate). Attach the posted Credit Memo. Use this template: *"Subject: Return Complete - Credit Memo Attached for Order SO-001234. Body: Please find the attached credit memo for the approved return of damaged product from your order. This credit has been applied to your account. Thank you for your partnership and patience."* | **Brand First.** Your email is Myld's voice. Make it a moment of trust and professionalism, turning a problem into a proof point of our reliability. |

---

&nbsp;
<p align="center"><strong>:::: TRAIL TWO ::::</strong></p>
<h3 align="center">THE ON-SITE REFUSAL (THE URGENT TRAIL)</h3>
<p align="center"><em>"Adaptability is imperative."</em></p>
&nbsp;

---

This is an audible on the field. The product is on our truck, at a partner's dock, and it's coming back. Speed and accuracy are everything.

| Step | Action | The Myld Way Mindset |
| :---: | :--- | :--- |
| **1** | **Receive the Mayday.** The driver or Distribution lead calls you directly. Take down the Sales Order number and the refusal reason (vault full, no buyer on site, order discrepancy). | **Be calm and be present.** The driver is having a rough moment. Your professional, steady response is the first step to a clean resolution. |
| **2** | **Halt the Order in Business Central.** Immediately find the original Sales Order. If its status is "Released" or "Shipped," you must reverse that status to re-open the order. This prevents inventory from being incorrectly deducted for product that never left our custody. | **Act with urgency.** Every minute this is left un-reconciled is a minute our inventory data is lying to the rest of the business. |
| **3** | **Void the Manifest in the State System (Metrc).** Locate the active outgoing manifest for that delivery. Reject or void it. In the notes, document the story: *"Manifest refused by [Dispensary Name] on [Date]. Reason: Vault at capacity. Product returning to Myld vault with driver [Name]. Never transferred custody."* | **Protect the license.** This single note is the legal proof that we did not commit a diversion event. It is your most critical task in a refusal. |
| **4** | **Confirm Physical Return.** Confirm with the driver and warehouse that the product is physically back in our secure vault and their paperwork matches your system reversal. | **Close the physical-digital loop.** Your system should now perfectly reflect reality on the ground. |
| **5** | **Cancel & Communicate.** The original order is canceled. Notify the Sales Rep clearly: *"Subject: Heads Up - Order SO-001235 Refused on Delivery. Body: No action needed from you right now, just a heads up. This order was refused at the dock by [Dispensary] due to a full vault. The product is safely back in our inventory and the compliance trail is closed. We'll need a new PO and a new order for their next delivery window. The old order is cancelled for a clean audit trail."* | **No surprises.** The Sales Rep needs to manage their partner. Give them the clean, complete information to do so professionally. |
| **6** | **Financial Housekeeping.** Remember: **No Credit Memo.** The order never invoiced, so nothing to credit. If it was prematurely invoiced, flag Accounting immediately to void the invoice—do not process this as a return. | **Think like an accountant.** The financial trail must match the physical reality. Product never left = no sale occurred = no credit needed. |

---

### 5.0 THE LOG BOOK: VERSION HISTORY

| Version | Date | Author | Nature of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | May 26, 2026 | Sales Data Coordinator | Initial playbook created for new hire onboarding. |
| | | | |

---

># BlazeYourOwnTrail

