# Simple Invoice Manager (SIM) — In App Features Documentation
# Company / Business Setup

## Definition
A feature that lets you set up and manage your business details either during first-time onboarding or later from the app settings (Primary Settings, Invoice Header & Footer).

## When & Who
- Filled by the business owner during initial app setup (onboarding) and updated anytime later from settings whenever business information changes.

## Flows / Navigation:
### A. Flow for Onboarding: 

1. Install the App you can see Onboarding Screen.
2. Upload your **company logo** and **owner signature** (can be added manually).
3. Fill in the required business details (see Field Reference below).
4. Set your preferences (country, currency, financial year, date format).
5. Tap **Save / Update**. Wait a moment for the database to update.
6. Note:- [If you want access this information inside the app]

    1. Go to Settings >> Primary Setting (Transaction No., Tax Identification Type, Country, Financial Year, Currency Format, Number Format, Date Format)

    2. Go to Settings >> Invoice Header/Footer (Logo, Company Name, Address, Phone Number, Email Address, Website, Head Note/Foot Note, Signature and Paid Stamp)

## Key Fields

- **Business / Company Name** — The legal or trade name of the business. Printed on all documents.
- **Country** — Sets regional defaults including currency symbol, tax label, and date format.
- **Currency Format** — How monetary amounts are displayed (e.g., ₹1,000.00 or $1,000.00).
- **Financial Year Range** — TA Financial Year (Fiscal Year) is a 12-month accounting period used for bookkeeping and tax reporting, which may differ from the calendar year. The app uses this period to filter dashboard data and reports
- **Tax Identification Type** — Simply means the kind of tax ID format being used based on a country’s system.
- **Date Format** — How dates appear on documents (e.g., DD/MM/YYYY or MM/DD/YYYY).
- **Company Logo** — Uploaded image that appears on all generated documents for branding.
- **Owner Signature** — Can be drawn manually in the app or uploaded as an image. Appears at the bottom of invoices.
- **Paid Stamp** — When enabled, displays a clear PAID mark on documents to indicate completed payment.

## Alternate Terms

- Company / Business Setup is also called: Company Profile, Business Profile, Organization Setup
- Financial Year is also called: Fiscal Year, Accounting Year, Tax Year
- Owner Signature is also called: Authorized Signature, Signatory

## Video Tutorial
How to Add Company or Business: https://www.youtube.com/watch?v=H8D5DLmF58o

## FAQs

**Q: How to add company details like company name, tax, logo, and signature?**
A: Go to Settings → Invoice Header & Footer. Add business name, address, contact number, email, logo, and owner signature. For country, currency, financial year, and date format, go to Settings → Primary Settings. These details appear on every invoice and document the app generates.

**Q: What is the Financial Year setting?**
A: The Financial Year is a 12-month accounting period used for bookkeeping and tax reporting. In India it runs from April 1 to March 31. SIM uses this range to filter dashboard data and reports.

**Q: What is the Paid Stamp feature?**
A: The Paid Stamp automatically displays a PAID mark on invoices and documents once payment is fully received. It provides a clear visual confirmation of payment status.

**Q: Where do I upload my company logo?**
A: Go to Settings → Invoice Header & Footer → Upload Logo. The logo will appear on all generated documents.

**Q: Can I update company details after initial setup?**
A: Yes. Go to Settings → Primary Settings or Settings → Invoice Header & Footer at any time to update business information.

---

# Clients & Suppliers

## Definition
All business contacts are managed in one place. 

* **Clients** – businesses that receive invoices for sales. 
* **Suppliers** – businesses from whom purchases are made. 

Once a contact is added, it can be selected instantly while creating invoices or purchases, without entering details again. 

## When & Who
This feature is useful for businesses that regularly deal with the same clients or suppliers. 

* Contacts can be added in advance, or 
* Created instantly while making an invoice or purchase. 

## Flows / Navigation
Side Menu (☰) → Client / Supplier → Add Client or Add Supplier

## Important Notes-
- The user cannot add any custom fields other than the fields that are already present in creation form.

## Key Fields

- **Opening Balance** — The outstanding amount that existed between the business and the party before they started using SIM.
  - To Receive: The client owes the business money.
  - To Give: The business owes the client money.
- **GST Number (GSTIN) / Tax ID** — The party's tax identification number. Required for GST-compliant invoicing in India.

## Optional Sub-Features

**Transaction History**
- It shows the sales and payment that were recorded in a table format. 
- User can select the transaction by tapping the rows that he wants to refer to and add changes if necessary 

**Customer / Supplier Insight**
Gives a complete summary of a party's activity including:
- Pending Sale Orders — Orders created but not yet completed, grouped by pending days.
- Pending Estimates — Total value of quotations not yet converted into sales.
- Average Days to Pay — Average time the customer takes to make payments.
- Customer Activity — Graph of monthly or periodic transactions.
- Top Selling Products — Most frequently purchased products by the customer.
- Credit Limit — The maximum credit allowed to the client. App shows a reminder when the client exceeds this threshold.

**Client / Supplier Category**
- Groups clients and suppliers into categories (e.g., Retail, e-Commerce, POS).
- Not visible by default. Enable from Settings → Client/Supplier Categorization Settings.
- Once enabled, a Category option appears in the client/supplier form.

**Receivables / Payables**
- Receivables: Shows a list of clients who owe money and the total receivable amount.
- Payables: Shows a list of suppliers to whom money is owed.

**Export to Excel**
- The client or supplier list can be downloaded using the Export Excel option.

## Alternate Terms

- Client is also called: Customer, Buyer, Party, Consumer, Account
- Supplier is also called: Vendor, Seller, Creditor, Distributor, Wholesaler
- Client/Supplier List is also called: Party Master, Contact Book, Ledger, Account Directory
- Opening Balance is also called: Carried Forward Balance, Prior Balance, Outstanding Balance

## Video Tutorial
How to Add Client & Supplier: https://www.youtube.com/watch?v=hTjFjCd4FKM

## FAQs

**Q: How to add a new client in SIM?**
A: Tap the hamburger menu (☰) → Client / Supplier → Add Client → fill in the details → Save.

**Q: How to add a new supplier in SIM?**
A: Tap the hamburger menu (☰) → Client / Supplier → switch to the Supplier tab → Add Supplier → fill in details → Save.

**Q: What is opening balance in clients and suppliers?**
A: Opening balance is the outstanding amount that existed between the business and the party before using SIM. "To Receive" means the client owes you money. "To Give" means you owe the client money.

**Q: How to add opening balance for a client or supplier?**
A: Go to Side Menu → Clients → tap on the client → Edit → Opening Balance → select To Give or To Receive → enter amount → Update.

**Q: How to get the client statement or ledger?**
A: Go to Reports → Sales → Transaction History / Ledger → tap on the specific client. This shows all invoices, payments, credit notes, and returns along with the outstanding balance.

**Q: Can I upload multiple clients at once?**
A: Yes. Go to Settings → Batch Upload → select Client → download template → fill in client details → upload the file.

**Q: What is the Credit Limit field for a client?**
A: Credit Limit defines the maximum credit you allow a client to carry against unpaid invoices. The app reminds you when a client exceeds this limit.

**Q: Can I group clients into categories?**
A: Yes. Enable Client/Supplier Categorization from Settings. Once enabled, a Category field appears in the client form where you can assign categories like Retail, Wholesale, or e-Commerce.

**Q: How to check Client Statement?**
A: You can check the client statement by following these steps: Go to Reports → Sales → Transaction History / Ledger → Select the Client. You will be able to view the client’s statement

---

# Products & Services

## Definition
The Products & Services section helps you manage all the goods and services your business offers. You can save each item’s key details—like name, description, price, and tax—and reuse them in invoices to make billing faster and more consistent. 

## When & Who
- All business types: physical goods sellers, service providers, SaaS, consultants.
- Set up before creating the first invoice, or products can be added directly while creating an invoice.

## Flow / Navigation:
Dashboard → Side Menu (☰) → Products → Show Product List → Add New Product → Tap Add New Product → Fill required fields (Name, Price, Category, etc.) → Enable or disable inventory tracking as needed → Save.

## Key Fields

- **Sale Rate** — Price at which the item is sold to clients.
- **Purchase Rate** — Price at which the item is bought from suppliers. Used for profit calculation.
- **Tax Rate** — Applicable GST or VAT percentage. Automatically applied when the product is added to an invoice.
- **Opening Stock** — The quantity of the item available at the time of first adding the product to the app.
- **Opening Stock Rate** — The cost price (buy rate) per unit at the time of initial stock entry.
- **Minimum Alert Level** — Stock threshold that triggers a low-stock warning for reordering.
- **HSN Code** — A number that identifies a product.

## Optional Features

**Product Categorization**
- Groups products into categories (e.g., Electronics, Services, Raw Materials).
- Not visible by default. Enable from Settings → Enable / Disable Features → Product Categorization → Enable sub-settings as required
*(Search: "Product Categorization" in Settings search bar)*
- Once enabled, create categories using the Add Category button and assign them to products.
- Option to enable "Group Line Items by Product Category" to automatically group items by category on invoices and documents.

**Manage Product Rates**
- Allows quick update of Sale Rate and Purchase Rate for multiple products.
- Navigation: Products → Manage Product Rates → find product → update rates → Done.

**Export to Excel**
- The product list can be downloaded using the Export Excel option.

**Batch Upload**
- Add multiple products at once using an Excel template.
- Navigation: Settings → Batch Upload → Create New Product → download template → fill details → upload → confirm.

**Online Store**
- Products added to the Product List automatically appear in the Online Store for publishing.

**Reorder Management**
- Reorder Management enables automated stock monitoring against a defined reorder threshold.
- When a product's stock falls below the set minimum alert level, the app alerts the business to restock — preventing stockouts before they occur.
- Not visible by default. Enable from Settings → Enable / Disable Features → Reorder Management → Enable Reorder Feature
*(Search: "Reorder Management" in Settings search bar)*

## Important Notes

- A product cannot be created with the same spelling as a deleted product. The app performs a soft delete — deleted products remain in the system because they may be linked to existing invoices.
- To add a product with a similar name, make a minor change in spelling or add a character (e.g., a comma or dot).
- It is not possible to delete or reset only a specific section of data. Data can only be fully reset or not at all.
- The user cannot add any custom fields other than the fields that are already present in creation form.

## Alternate Terms

- Product is also called: Item, Good, Article, SKU, Stock Item, Commodity
- Service is also called: Work, Task, Job, Offering, Service Item
- Sale Rate is also called: Selling Price, MRP, Unit Price, List Price
- Purchase Rate is also called: Cost Price, Buy Rate, Landed Cost
- HSN Code is also called: Tariff Code, Commodity Code, Product Classification Code
- Product Catalogue is also called: Item Master, Price List, Inventory List, Product Database
- Measurement Unit is also called: Unit of Measure (UOM), Unit

## Video Tutorials
- How to Add Product or Service: https://www.youtube.com/watch?v=EmURS_9WiG4
- Batch Upload Multiple Products: https://www.youtube.com/watch?v=-zSq_ioaw8A
- Setup Product Categorization: https://www.youtube.com/watch?v=Lyt9zfVnRHM

## FAQs

**Q: How to add a product or service in SIM?**
A: Go to Side Menu → Products → Product List → Add New Product. Fill in name, rate, tax, and other details. Enable inventory if tracking stock. Tap Save.

**Q: How to add multiple products at once using Excel?**
A: Go to Settings → Batch Upload → Create New Product → download the template → fill in product details following the column headers → upload the file → confirm and save.

**Q: What is the HSN code field in a product?**
A: HSN (Harmonised System of Nomenclature) is a standardized numeric code that classifies goods for GST and trade purposes. It is mandatory for e-invoicing and e-way bills in India.

**Q: Can I add product images?**
A: Yes, but POS mode must be enabled first. Go to Side Menu → Switch to POS Mode → Enable → OK. Then go to Products → tap on a product → Add Product Image.

**Q: Why can't I create a product with the same name as a deleted product?**
A: SIM uses soft deletion — deleted products remain in the system because they may be linked to existing invoices. To add a similar product, change the spelling slightly or add a character.

**Q: What is Opening Stock Rate?**
A: Opening Stock Rate is the cost price (buy rate) per unit at the time of first entering the product. For example, if 10 items were purchased for ₹1,000, the opening stock rate is ₹100 per unit.

**Q: How to quickly update prices for multiple products?**
A: Side Menu (☰) → Go to Products → Manage Product Rates → find the product → update Sale Rate and Purchase Rate → Done.

**Q: What is Reorder Management in SIM?**
A: Reorder Management monitors stock levels against a defined threshold. When stock falls below the minimum alert level set on a product, the app sends a restock alert.

**Q: How to enable Reorder Management?**
A: Go to Settings → Enable / Disable Features → Reorder Management → Enable Reorder Feature.

**Q: What is the minimum alert level?**
A: The minimum alert level is the stock quantity set per product below which the app triggers a reorder alert.

**Q: How to enable Product Categorization?**
A: Go to Settings → Enable / Disable Features → Product Categorization → enable the required sub-settings.

**Q: What does "Group Line Items by Category" do?**
A: When enabled, products on invoices and documents are grouped under their assigned category heading instead of appearing as a single flat list.

---

# Invoices

## Definition
An invoice is a formal, legally binding document issued by a seller to a buyer, requesting payment for goods delivered or services rendered. It details what was sold, the quantities, prices, applicable taxes, and the total amount due. In India, a GST-registered business must issue a **tax invoice** for all taxable supplies.

## When & Who
- Used by any business that sells goods or services: freelancers, retailers, wholesalers, service providers.
- Raised after a sale is made or a service is delivered.

## Navigation
Dashboard → Side Menu (☰) → Invoice → Add New Invoice

## Actions After Invoice Creation

After creating an invoice, you can perform various actions by clicking on the invoice from invoice list. These actions include:

*   **Edit**: Modify invoice details such as images, notes, items, or names.
*   **Preview**: View the invoice in either image or PDF format.
*   **Send**: Dispatch the invoice using a template to any recipient.
*   **Share**: Directly share the invoice as an image or PDF.
*   **Print**: Print the invoice using either a Normal or Thermal Printer.
*   **Mark as Received**: Record the invoice as paid, specifying the payment method (Cash or Bank).
*   **Make Delivery Note**: Generate a delivery note directly from the invoice.
*   **Create Duplicate**: Create an exact copy of the existing invoice without client.
*   **Make Sales Return**: Initiate a sales return related to the invoice.
*   **Delete**: Permanently remove the invoice.
*   **Cancel Invoice**: Invalidate the invoice.

## Key Fields

- **Due Date** — The deadline by which the client must make payment.
- **Discount** — A reduction applied to the price. Can be a flat amount (e.g., ₹200 off) or a percentage (e.g., 10% off). Applied per item or on the total invoice.
- **Tax** — GST, VAT, or other applicable tax. Applies based on the tax rate set on each product.
- **Shipping Charges** — Additional charges for delivery or freight. Added as a separate line item.
- **Custom Fields** — User-defined labels and values visible at the top of the invoice (e.g., PO Number, Vehicle Number, LR Number).

## Invoice Statuses

- **Not Received** — Payment has not been collected yet.
- **Partially Received** — Some payment has been collected; a balance remains.
- **Fully Received / Paid** — The complete invoice amount has been collected.

## Optional Features

**Recurring Invoice**
- You can set new invoices to repeat automatically weekly or monthly.
- To use this feature, go to the Side Menu (☰) → Invoice

**POS Mode Customer Types**
When creating an invoice in POS mode, the customer can be marked as:
- Walk-in Customer — No customer details saved. Used for anonymous one-time buyers.
- Regular Customer — Full details saved (name, address, phone, GSTIN). Used for repeat or wholesale customers.
- This feature will help you keep your regular and one-off customer seperate.
- It can be useful for your business if you use POS mode but sometimes need to invoice a few regular customers (e.g- wholesale customers or repeat loyal customers).

**Sale Return**
- A sale return is created when a customer returns goods from a previously issued invoice.

**B2B Invoice (India)**
- An e-invoice is a digitally created and government-validated invoice used for GST reporting.
- Applicable to GST-registered businesses with turnover above ₹5 crore for B2B transactions.

**B2C Invoice (India)**
- Issued to individual or unregistered customers with no GSTIN.
- Customer cannot claim ITC. E-invoice is generally not required for B2C.

**E-Way Bill**
- A digital document required for transporting goods worth more than ₹50,000.
- Can be generated directly from an invoice.
- Each E-Way Bill carries a unique E-Way Bill Number (EBN) along with shipment and transport details.

  **Required Inputs to Activate**
    - **Disclaimer Checkbox** — Must be accepted before the feature activates.
    - **GSTIN** — The business's GST number for seller validation.
    - **GSP Username & Password** — Credentials from the e-way bill government portal.
    - **City & Pincode** — Business location details required for e-way bill submissions.
    - **Validate Seller GSTIN** — Verifies and auto-fetches legal business details from GST records.

  **Navigation Path**
  Settings → Enable / Disable Features → e-Way Bill Settings → Accept disclaimer → Add GSTIN, Username, Password, City, Pincode → Validate Seller GSTIN → Save
  *(Search: "e-Way Bill" in Settings search bar)*

**Delivery Note**
- A document sent along with goods when they are delivered to a customer.
- Can be created from an existing invoice.

**Credit Note**
- A document issued to a buyer to reduce the amount they owe on a previous invoice.

**Commission**
- Commission can be assigned to an agent on an invoice. It is calculated on the selling price or the discounted selling price. Treated as a business expense.

**Payment Account**
- When Payment Account is enabled, each payment on the invoice can be tagged to a specific account (cash or bank).

**UPI QR Code**
- A scannable QR code linked to the business's UPI ID. Added to invoices so the client can scan and pay instantly.

**Banking Details**
- Bank account information added to the invoice so the client knows how to make a payment.

## E-Invoice:

**E-Invoice (India)**
- The E-Invoice setting enables the app to generate government-registered B2B invoices with an IRN (Invoice Reference Number) and QR code, as required by India's GST portal (IRP). 
- This is a mandatory compliance feature for GST-registered businesses with annual turnover exceeding ₹5 crore.

  **Required Inputs to Activate**
    - **Disclaimer Checkbox** — Must be accepted before the feature activates.
    - **GSTIN** — The business's GST number for seller validation.
    - **GSP Username & Password** — Credentials from the e-way bill government portal.
    - **Validate Seller GSTIN** — Verifies and auto-fetches legal business details from GST records.

**Navigation Path**
Settings → Enable / Disable Features → e-Invoice Settings → Accept disclaimer → Add GSTIN, Username, Password → Validate Seller GSTIN → Save
*(Search: "e-Invoice Settings" in Settings search bar)*

**E-Invoice (Colombia)**
- Enables adding CUFE and DIAN QR codes from third-party validation to invoices for Colombian compliance.
- To use this feature, enable e-invoicing for colombia from the Settings.
- Enable from Settings → Primary Settings → Country = Colombia → Yes → Done.

  - Go to Settings → click on search icon → search E-Invoice Setting → click on that → Enable → Done.
  
- Now, go to Invoice List → Create New → Add client & Product details → E-invoice details → Enter CUFE number → Scan QR → Save.

**E-Invoice (Indonesia)**
- For VAT-registered businesses in Indonesia with turnover above IDR 4.8 billion/year.
- Invoices must be submitted to the tax authority via the e-Faktur / Coretax system.
- SIM supports generating the required XML format for submission.
- How the process works (with your system):
  - Step A — Create Invoice (Your UI) → Create invoices → Store them in the system → Display them in the E-invoice List
  - Step B — Generate XML (Your “Generate XML” button) 
    - When user clicks Generate XML: → System converts invoice data into DJP-required XML format → Includes fields (BuyerName, BuyerTIN, TaxInvoiceDate, Price, Qty, VAT, etc.)

**E-Invoice (Malaysia)**
- A feature that allows you to send invoices using Peppol e-invoicing
- Invoices are sent in a standard XML format instead of traditional formats like PDF
- The XML file can be automatically read and processed by other systems
- This is use by:
  - Businesses (suppliers & buyers) – to send/receive invoices digitally
  - Government bodies – often mandate Peppol for procurement
  - Accounting / ERP Systems: To automate invoice processing
- To Enable: Enable in settings → choose format → save → go to Peppol Invoice List → select invoices → generate XML → send


**ZATCA (Saudi Arabia / UAE)**
- ZATCA refers to the Zakat, Tax and Customs Authority — the government body in Saudi Arabia and UAE responsible for taxes and e-invoicing.
- SIM supports adding a ZATCA-compliant QR code to invoices. The QR code contains seller name, VAT number, date, total, and VAT amount in a secure encoded format for verification.

## Alternate Terms

- Invoice is also called: Bill, Tax Invoice, Sales Invoice, Commercial Invoice, Tax Bill, Sales Bill, Sales Receipt, Sale Record
- Due Date is also called: Payment Deadline, Payment Due Date
- Discount is also called: Rebate, Concession, Price Reduction
- Advance Payment is also called: Partial Payment, Token Amount, Deposit, Down Payment
- Terms & Conditions is also called: Payment Terms, T&C, Conditions of Sale
- Shipping Charges is also called: Freight, Delivery Charges, Logistics Cost

## Video Tutorial

How to Create an Invoice: https://www.youtube.com/watch?v=SurVRuMIkUg

## FAQs

**Q: How to create an invoice in SIM?**
A: From the dashboard, Side Menu (☰) → Invoices → Add New Invoice → select client → add items → apply tax and discount if needed → add payment if received → Preview → Save or Send.

**Q: What is the difference between a B2B and B2C invoice?**
A: A B2B invoice is issued to another GST-registered business. Both parties have GSTINs and the buyer can claim Input Tax Credit (ITC). A B2C invoice is issued to an individual or unregistered buyer with no GSTIN. ITC cannot be claimed by the buyer. E-invoicing in India is required for B2B but generally not for B2C.

**Q: How to show outstanding balance on an invoice?**
A: Go to Settings → Invoice Template Setting → enable Total Outstanding Payment (of the client) → Done. Once enabled, every invoice shows the client's cumulative outstanding balance.

**Q: How to change the font size of invoice PDF?**
A: Go to Settings → Invoice Template Setting → Invoice Theme → Overall Sizes or Individual Sizes → change font size → Done → Save.

**Q: What is a recurring invoice?**
A: A recurring invoice is automatically created and sent at regular intervals (e.g., weekly, monthly). It must be enabled from invoice settings.

**Q: What is a Walk-in Customer in POS mode?**
A: A walk-in customer is an anonymous one-time buyer. No customer details are saved. Walk-in customers appear in an aggregated form in reports, separate from regular customers.

**Q: Can I add banking details and UPI QR code to an invoice?**
A: Yes. Go to Settings → Banking Details and PayPal.Me → add bank account details. For UPI, enable the UPI QR code option. These details appear on the invoice so the client knows how to pay.

**Q: How to enable E-Invoice in SIM?**
A: Go to Settings → Enable / Disable Features → e-Invoice Settings → accept the disclaimer checkbox (this auto-enables the feature) → add GSTIN, GSP Username, and Password → tap Validate Seller GSTIN → Save.

**Q: What is GSTIN in E-Invoice settings?**
A: GSTIN is the business's 15-digit GST Identification Number. It is used to validate the seller's identity on the government portal and auto-fetch the legal business name and address.

**Q: What is GSP Username and Password for E-Invoice?**
A: GSP credentials are created separately on the government e-invoice portal. They authorize the app to connect to the GST system on behalf of the business. They are different from the regular GST portal login.

**Q: Is E-Invoice available for all users?**
A: No. E-Invoice is available only for businesses in India that are GST-registered.

**Q: How to enable E-Way Bill in SIM?**
A: Go to Settings → Enable / Disable Features → e-Way Bill Settings → accept the disclaimer → add GSTIN, GSP Username, Password, City, and Pincode → tap Validate Seller GSTIN → Save.

**Q: What is the EBN?**
A: EBN stands for E-Way Bill Number. It is the unique number assigned to each generated E-Way Bill. It must accompany goods during transport.

**Q: How to add a client’s signature to any form (Invoice, Estimate, Sale Order, etc.)**
A: You can add a client’s signature to documents like invoices, estimates, sale orders, purchase orders, purchase records, and receipts by following these steps: Go to the list of the specific form (Invoice / Estimate / Sale Order / Purchase Order / Purchase Record / Receipt) → Select the document you want to edit → Edit → Scroll down to the Signature / Head Note / Foot Note → '+' Add → Upload/Add → Save.

Currently, the feature to add a client’s signature is only available on the mobile app (Android).

---

# Estimates / Proforma Invoices

## Definition
An estimate is a non-binding price proposal sent to a potential client before work begins or an order is confirmed. It shows what the client will likely be charged, but it has no legal payment obligation and cannot be used for tax claims. It is used to get client approval on pricing before a final invoice is raised.

An estimate in SIM serves the purpose of a Proforma Invoice — issued before delivery to request advance payment or for customs documentation.

## When & Who
- Used by freelancers, contractors, agencies, service providers, and any business that quotes prices before delivery.
- Sent when a client asks for a price before confirming an order.

## Flows / Navigation:
Dashboard → Estimate section → Create Estimate → Add the necessary details.

## Key Fields

- **Estimate Date** — The date the quote is prepared. Used to track the age and validity of the quote.
- **Banking Details** — The business's bank account information added to the estimate so the client knows how to pay.
- **Pay Now Button (PayPal)** — An embedded direct payment link added to the estimate for online payment. For international users.
- **UPI QR Code** — A scannable QR code linked to the business's UPI ID for instant digital payment. For Indian users.

## Key Concept: Estimate vs. Invoice

- Estimate — A quote. Tentative. No legal obligation. A client can reject it.
- Invoice — A bill. Legally binding. Payment is expected once issued.

## Optional Feature: Add Image to Estimate

- An image can be added to an estimate record.
- The user can choose to show or hide it in the PDF — useful for client-facing documents vs. internal references.

## Alternate Terms

- Estimate is also called: Quote, Quotation, Price Quote, Proforma Invoice, Proposal, Price Offer
- Banking Details is also called: Bank Account Details, Payment Information, Beneficiary Details
- UPI QR Code is also called: Payment QR, Scan-to-Pay Code

## Video Tutorial
How to Create an Estimate / Proforma Invoice: https://www.youtube.com/watch?v=J7f9U3ozE4M

## FAQs

**Q: What is an estimate in SIM?**
A: An estimate is a non-binding price proposal sent to a client before work begins. It shows likely charges but has no legal payment obligation. Once the client agrees, it can be converted into a final invoice.

**Q: What is the difference between an estimate and an invoice?**
A: An estimate is a quote — tentative with no legal obligation. An invoice is a bill — legally binding with payment expected. A client can reject an estimate; they cannot reject a valid invoice.

**Q: How to send an estimate to a client?**
A: Go to the Estimate section → Create Estimate → add client, items, taxes, and discounts → Preview → Send via email or other method. You can also customize the email template before sending.

**Q: Can I add a Pay Now button to an estimate?**
A: Yes. When creating or editing an estimate, go to the More section → add your PayPal.Me link to embed a Pay Now button. For Indian users, a UPI QR code can be added instead.

**Q: What is a Proforma Invoice?**
A: A proforma invoice looks like a real invoice but is issued before delivery of goods or services. It is used to request advance payments or for customs purposes. Estimates in SIM serve this function.

---

# Sale Orders

## Definition
A sale order is created when a customer confirms they want to buy from you, but you haven’t delivered the goods or raised the final invoice yet. It serves as an internal record that reserves stock and initiates the fulfillment process.

## When & Who
- Used by wholesalers, distributors, manufacturers, and B2B businesses where orders are placed in advance and fulfilled later.
- Common when a customer sends a formal Purchase Order that the business needs to acknowledge.

## Flows / Navigation:
Dashboard → Side Menu (☰) → Sale Order section → Add Sale Order (Add details.)

## Sale Order Statuses

- **Pending** — Order accepted but goods not yet delivered or invoiced.
- **Completed** — Invoice has been raised and payment received.
- **Manually Completed** — Sale order force-closed manually even if not fully fulfilled.
- **Cancelled** — Sale order completely cancelled and will not be processed.

## Key Concept: Sale Order vs. Invoice

- Sale Order — A commitment to sell. Records the customer's confirmed intent to purchase. Does not affect inventory or accounts.
- Invoice — The formal bill generated after delivery, requesting payment. Affects accounts and inventory.

## Reference Number on Invoice
- When an invoice is created from a sale order, the invoice is automatically assigned the corresponding sale order reference number.
- This allows easy tracking and searching of invoices linked to a specific sale order.
- Two sale orders from the same customer can be combined into a single invoice.

## Alternate Terms

- Sale Order is also called: Sales Order, SO, Customer Order, Work Order, Booking
- Pending is also called: Open, Unfulfilled, In Progress

## Video Tutorial
How to Create a Sale Order: https://www.youtube.com/watch?v=swWyOktSWvg

## FAQs

**Q: What is a sale order in SIM?**
A: A sale order records a customer's confirmed intent to purchase before delivery happens and before an invoice is raised. It tracks the order status and initiates the fulfillment process.

**Q: What is the difference between a sale order and an invoice?**
A: A sale order is a commitment to sell — it does not affect inventory or accounts. An invoice is the formal bill generated after delivery and it does affect accounts.

**Q: How to convert a sale order to an invoice?**
A: Tap on the sale order → tap Make Invoice → save. Once payment is received, the sale order status updates to Completed.

**Q: What does Manually Completed status mean on a sale order?**
A: Manually Completed means the sale order was force-closed by the user even if it was not fully fulfilled or delivered.

**Q: Can two sale orders be merged into one invoice?**
A: Yes. Two sale orders from the same customer can be combined to create a single invoice record.

---

# Expense Management

## Definition
Expense Management is a feature used to record, organize, and track all business spending. Every expense entered is stored and automatically reflected in financial reports — especially the Profit & Loss (P&L) report, where expenses are deducted from income to calculate net profit or loss.

## When & Who

When it is used:
- Paying rent, utilities, or subscriptions
- Purchasing goods or services not tracked as inventory
- Travel, fuel, or operational costs
- Day-to-day business expenses
- Used daily or whenever a business transaction occurs

Who uses it:
- Business owners — to monitor costs and profitability
- Accountants / bookkeepers — for financial records and reporting
- Freelancers — to track business-related spending
- Finance teams / SMEs — for budgeting, audits, and analysis

## Key Components

- **Expense Entry Form** — Records date, expense type, description, and amount for each expense.
- **Expense List / Report** — A consolidated view of all recorded expenses. Accessible from Reports → Other → Expense Report.
- **Expense Type (Category)** — Organizes spending into categories such as Rent, Travel, Utilities, or Supplies.
- **Integration with P&L** — All recorded expenses automatically reflect in Profit & Loss reports and reduce net profit accordingly.

## Alternate Terms

- Expense Management is also called: Expense Tracking, Expense Management System, Cost Tracking, Spending Tracker, Expense Ledger

## Important Notes
- The user cannot add any custom fields other than the fields that are already present in creation form.

## FAQs

**Q: What is Expense Management in SIM?**
A: Expense Management is a feature to record and track all business spending. Every expense entered automatically reflects in financial reports, especially the Profit & Loss report.

**Q: How to add an expense in SIM?**
A: Go to the Side Menu ( ☰ ) → Expense section → tap Add Expense → enter the date, expense type, description, and amount → Save.

**Q: Where can I view all recorded expenses?**
A: Go to Reports → Other → Expense Report. This shows a consolidated list of all recorded expenses by category and period.

**Q: What is an Expense Type?**
A: Expense Type is the category used to classify a business expense — for example, Rent, Travel, Utilities, or Supplies. It helps organize spending for reporting and analysis.

**Q: Does expense data appear in Profit & Loss reports?**
A: Yes. All recorded expenses are automatically deducted from income in the Profit & Loss report to calculate net profit or loss.

**Q: Who should use the Expense Management feature?**
A: Business owners, accountants, bookkeepers, freelancers, and finance teams — anyone who needs to track and report business spending.

**Q: How often should expenses be recorded?**
A: Expenses should be recorded daily or whenever a business transaction occurs to keep financial records accurate and up to date.

---

# Purchase Orders

## Definition
A Purchase Order (PO) is a document sent by the business to a supplier to formally request goods before they are received. It records what is being ordered, in what quantity, and at what agreed price. It serves as a binding commitment between the buyer and supplier before any physical exchange takes place.

## When & Who
- Used by retailers, wholesalers, manufacturers, and any business that procures stock from suppliers in advance.
- Raised when the business wants to formalize an order before goods are dispatched.
- Common in formal B2B procurement where documentation is required at every step.

## Flow / Navigation:
- **Flow for creating the Purchase Order:**
Dashboard → Side Menu (☰) → Purchase Order section → Add Purchase Order → Save → Status: Pending (order accepted, not yet delivered/invoiced).

- **Flow for creating the Purchase Order to Purchase Record:**
When ready to deliver: tap the Purchase order → Make Purchase Record → Save. (Once payment is paid, Purchase order status updates to Completed.)

## Key Fields

- **Discount** — Any price reduction agreed upon with the supplier for this order.

## Purchase Order Statuses

- **Pending** — Order created and sent but goods not yet received.
- **Completed** — Goods received and a purchase record created against this PO.
- **Manually Completed** — PO force-closed manually even if not fully fulfilled.
- **Cancelled** — Purchase order completely cancelled and will not be processed.

## Key Concepts

**Purchase Order vs. Purchase Record**
- A PO is a request — created before goods arrive. Does not affect inventory or accounts.
- A Purchase Record is the accounting entry made after goods are physically received. Affects inventory and accounts.
- Many small businesses skip POs and go directly to purchase records. Formal procurement workflows use both.

**Why use a Purchase Order**
- The supplier has a documented commitment to fulfill.
- The buyer has a record of the agreed price, quantity, and items — which can be verified when goods arrive.
- Discrepancies between the PO and what is received are caught at the point of entry.

**Reference Number on Purchase Record**
- When a purchase record is created from a purchase order, it is automatically assigned the corresponding PO reference number.
- Two purchase orders from the same supplier can be combined into a single purchase record.

## Alternate Terms

- Purchase Order is also called: PO, Procurement Order, Supply Request, Indent
- Supplier is also called: Vendor, Seller, Distributor, Creditor
- Buy Rate is also called: Agreed Rate, Order Price, Purchase Price

## Video Tutorial
Purchase Order & Record: https://www.youtube.com/watch?v=lKUJ9sprbJU

## FAQs

**Q: What is a purchase order in SIM?**
A: A purchase order is a document sent to a supplier to formally request goods before they arrive. It records the order details but does not affect inventory or accounts until goods are received.

**Q: What is the difference between a purchase order and a purchase record?**
A: A purchase order is sent before goods arrive — it is a formal request. A purchase record is created after goods are received — it is the accounting entry that updates inventory and tracks supplier payment.

**Q: How to convert a purchase order to a purchase record?**
A: Tap on the purchase order → tap Make Purchase Record → save. Once payment is made, the PO status updates to Completed.

**Q: What does Manually Completed mean on a purchase order?**
A: Manually Completed means the purchase order was force-closed by the user even if it was not fully received or fulfilled.

**Q: Can two purchase orders be merged into one purchase record?**
A: Yes. Two purchase orders from the same supplier can be combined to create a single purchase record.

---

# Purchase Records

## Definition
A Purchase Record is the accounting entry created when goods are actually received from a supplier. It formally records the inward movement of stock, updates inventory quantities, and tracks the payment owed to the supplier. It can be created by converting a completed Purchase Order or directly as a standalone entry.

## When & Who
- Used by any business that buys physical goods from suppliers — shops, wholesalers, distributors.
- Created at the moment goods arrive, regardless of whether a PO was raised.

## Flow / Navigation:
Dashboard → Side Menu (☰) → Purchase → Add New Purchase Record

## Key Fields

- **Supplier** — The vendor from whom goods were received.
- **Purchase Date** — The date goods were received.
- **Items** — Products received including name, quantity, buy rate, and tax.
- **Buy Rate / Purchase Rate** — The price paid to the supplier per unit. Used for inventory cost and profit tracking.
- **Opening Stock** — The quantity on hand when the product was first added to the app. Enter this only once during product creation. Never enter it again in a purchase record for an existing product — it will double-count inventory.
- **Opening Stock Rate** — Cost price per unit at the time of first stock entry.
- **Minimum Alert Level** — The reorder threshold for this product.
- **Discount** — Price reduction received from the supplier on this purchase.
- **Payment Status** — Whether the supplier has been fully paid, partially paid, or not yet paid.

## Purchase Record Statuses

- **Unpaid** — Supplier has not yet been paid.
- **Partially Paid** — Some payment made; a balance remains.
- **Paid** — Supplier fully paid.

## Actions Available After Creating a Purchase Record

- **Edit** — Modify purchase record details such as images, notes, items, or names.
- **Preview** — View the purchase record as image or PDF.
- **Send** — Send using a template to any recipient.
- **Share** — Share directly as image or PDF.
- **Print** — Print using Normal or Thermal Printer.
- **Mark as Paid** — Record payment (Cash or Bank).
- **Create Duplicate** — Create an exact copy without client details.
- **Make Purchase Return** — Initiate a purchase return from this record.
- **Delete** — Permanently remove the purchase record.

## Important Rule: Opening Stock
If a product's opening stock was already entered during product creation, do not enter it again in a purchase record. The app will count it twice, resulting in an inflated inventory figure.

## Alternate Terms

- Purchase Record is also called: Purchase Entry, Purchase Invoice, Goods Receipt, GRN, Inward Entry
- Supplier is also called: Vendor, Seller, Distributor, Creditor
- Buy Rate is also called: Cost Price, Purchase Price, Landed Cost
- Unpaid is also called: Outstanding, Due, Payable

## Video Tutorials
- How to Create a Purchase Record: https://www.youtube.com/watch?v=282YfFsveQs
- Purchase Order & Record: https://www.youtube.com/watch?v=lKUJ9sprbJU

## FAQs

**Q: What is a purchase record in SIM?**
A: A purchase record is the accounting entry created when goods are received from a supplier. It updates inventory stock and tracks payment owed to the supplier.

**Q: How to create a purchase record in SIM?**
A: From the dashboard, Side Menu (☰) → Purchase section → Add New Purchase Record → select supplier → add items → apply discount and tax if applicable → add payment if made → Preview → Save.

**Q: Why should I not enter opening stock again in a purchase record?**
A: If opening stock was already entered when creating the product, entering it again in a purchase record will count the same stock twice, inflating your inventory figures. Opening stock is a one-time entry made only at product setup.

**Q: How to mark a purchase as paid in SIM?**
A: Open the purchase record from the purchase list → tap Mark as Paid → select payment method (Cash or Bank) → save.

**Q: What reports are available for purchases?**
A: You can check Purchase/Payment Report, Detailed Purchase Report, and Purchase Order Report from the Reports section.

---

# Inventory Management

## Definition
Inventory management in SIM tracks the quantity of physical goods a business holds at any point in time. Stock levels update automatically — increasing when purchases are recorded and decreasing when sales (invoices) are made. The feature also supports manual adjustments and low-stock alerts.

## When & Who
- Relevant only for businesses dealing in physical goods: shops, wholesalers, distributors, manufacturers.
- Not applicable to pure service businesses.
- Should be enabled as part of initial app setup.

## Flow / Navigation:
Settings → Enable / Disable Features → Inventory → Enable

## What Affects Inventory

Actions that INCREASE stock:
- Purchase Record
- Manual Stock-In adjustment

Actions that DECREASE stock:
- Invoice (Sale)
- Manual Stock-Out adjustment

Actions that DO NOT affect inventory:
- Estimate / Quotation
- Sale Order
- Purchase Order
- Delivery Note

## Key Fields

- **Enable Product Inventory** — Turn this on per product to track its stock. Should be off for services.
- **Opening Stock** — The quantity of the item available at the beginning when the product is first added to the app.
- **Opening Stock Rate** — The cost price per unit at the time of initial stock entry (buy rate).
- **Minimum Alert Level** — The stock threshold below which the app sends a low-stock alert.
- **Stock-In** — When stock quantity increases (e.g., from a purchase or manual addition).
- **Stock-Out** — When stock quantity decreases (e.g., from a sale or manual removal).
- **Inventory Valuation Method** — The accounting rule used to calculate the cost of items when they are sold.

## Manual Inventory Adjustment
Allows stock levels to be updated without creating a sale or purchase transaction. Used for:
- Items consumed internally or personally
- Damaged or expired goods
- Free samples given out
- Inventory corrections after physical stock count
- Lost or stolen goods
- Opening stock adjustments

Navigation: Side Menu (☰) → Inventory → Add Inventory Manually → select Stock In or Stock Out → enter quantity and reason → Save.

## Automatic Inventory Adjustment
When a purchase record is created, stock quantity is automatically updated for the respective products in inventory.

## Inventory Valuation Methods

**1. Actual Average Buy Rate (Weighted Average Cost) — Recommended**
- Calculates the average cost of all units purchased over time.
- When an item is sold, its cost is recorded at this weighted average.
- Example: 10 units at ₹100 + 10 units at ₹120 → average = ₹110 per unit.
- Best for: Most businesses. Smooths out price fluctuations.

**2. FIFO (First In, First Out)**
- Assumes the oldest stock purchased is sold first.
- Example: Batch 1 (10 units at ₹100) → Batch 2 (10 units at ₹120). Sales come from Batch 1 first.
- Best for: Perishable goods (food, medicine, cosmetics).
- Financial effect: In rising-price environments, FIFO results in lower cost of goods sold and higher reported profit.

**3. Fixed Buy Rate**
- Uses a single manually defined cost price regardless of actual purchase price fluctuations.
- Example: Fixed rate ₹100. Even if you later buy at ₹130, cost is still recorded as ₹100.
- Best for: Businesses with stable, predictable purchase prices.

## Key Concept: Negative Inventory
Negative inventory occurs when the system shows stock below zero. This typically happens when a sale (invoice) or stock-out is recorded before the corresponding stock-in (purchase) is entered.

## Optional Sub-Feature: Physical Stock-Take (Reconciliation)
At the end of the day, differences may exist between the app's calculated inventory and the actual physical stock. The Physical Stock-Take feature allows correction of such differences by adding reconciliation edits to products along with their actual current stock.

## Dependencies and Side Effects

- **Reorder Management** — Automatically generates purchase order suggestions when stock falls below the minimum alert level.
- **Batch Upload (Inventory Data)** — Large amounts of product and inventory data can be updated at once using a CSV or Excel file.
- **Cost of Goods Sold (COGS)** — COGS is directly tied to the selected inventory valuation method.

## Alternate Terms

- Inventory is also called: Stock, Goods, Merchandise, Stockroom, Store
- Stock-In is also called: Goods Received, Inward, Purchase Entry, Positive Adjustment
- Stock-Out is also called: Goods Issued, Outward, Sales Deduction, Negative Adjustment
- Minimum Alert Level is also called: Reorder Point, Safety Stock Level, Low Stock Threshold
- FIFO is also called: First In First Out, Queue Method
- Weighted Average is also called: Moving Average, Average Cost Method, WAC
- Inventory Valuation is also called: Stock Valuation, Cost Method
- Physical Stock-Take is also called: Reconciliation

## Sub-Settings
- **Enable Inventory Management Feature:** Master toggle that activates stock tracking across the app.
- **Enable Low Inventory Level Alert:** Sends an alert when a product’s stock goes below its minimum alert level.
- **Enable Inventory Automatically for New Products:**
  - When enabled: inventory tracking is automatically applied to all new products
  - When disabled: inventory must be enabled manually for each product
- **Inventory Valuation Method:** Determines how the cost of sold stock is calculated
  - Options include:
    - Actual Average Buy Rate (recommended)
    - FIFO
    - Fixed Buy Rate (set in Settings)

After enabling inventory, the app prompts you to:
- Select existing products for inventory activation
- Enter opening stock quantity
- Enter opening stock rate
- Set minimum alert level

## Video Tutorials
- How to Enable Inventory: https://www.youtube.com/watch?v=wU3bhD1PhSs
- Add or Remove Inventory Manually: https://www.youtube.com/watch?v=pFQdvYH_mok

## FAQs

**Q: How to enable inventory management in SIM?**
A: Go to Settings → Enable / Disable Features → Inventory → enable the feature and sub-settings as required. Then select which products to track and enter opening stock, opening stock rate, and minimum alert level for each.

**Q: How to check inventory status?**
A: Go to Side Menu (☰) → Inventory → Check Inventory Status. This shows the current stock quantity for all inventory-enabled products.

**Q: What is the difference between Stock-In and Stock-Out?**
A: Stock-In means stock quantity increases (from a purchase or manual addition). Stock-Out means stock quantity decreases (from a sale or manual removal).

**Q: Does creating a sale order reduce inventory?**
A: No. Sale orders, purchase orders, estimates, and delivery notes do not affect inventory. Only actual invoices (sales) and purchase records affect stock levels.

**Q: What is FIFO inventory valuation?**
A: FIFO (First In, First Out) assumes the oldest stock is sold first. It is best for perishable goods like food, medicine, and cosmetics where older stock must be sold before expiry.

**Q: What is the Weighted Average inventory valuation method?**
A: The Weighted Average method calculates the average cost of all units purchased over time. When any unit is sold, its cost is recorded at this average. It is the recommended method for most businesses.

**Q: What is negative inventory?**
A: Negative inventory occurs when the app shows stock below zero. This typically happens when a sale is recorded before the corresponding purchase entry is made.

**Q: How to do a manual inventory adjustment?**
A: Go to Side Menu (☰) → Inventory → Add Inventory Manually → select Stock In or Stock Out → enter quantity and reason → Save.

**Q: What is Physical Stock-Take?**
A: Physical Stock-Take (Reconciliation) is a feature that corrects differences between the app's calculated stock and the actual physical stock in the warehouse by entering reconciliation edits.

**Q: What is Low Inventory Alert?**
A: Low Inventory Alert is a feature that notifies you when a product’s stock falls below a predefined minimum level. For example, if you have 100 apples and set the minimum alert level to 10, you will receive an alert/notification when the stock goes below 10.

**Q: Where can I check Low Inventory Alerts?**
A: You can view all products with low stock by navigating to:
Side Menu (☰) → Inventory → Low Inventory Level Alert

---

# Sale Returns, Refunds & Credit Notes

## Definition

**Sale Return**
A sale return is created when a customer returns goods they bought. The original invoice is never deleted — it records that the sale happened. A sale return is created instead, which connects to the original invoice, records what was returned, keeps the sale record accurate, and puts returned items back into inventory.

**Credit Note**
A credit note records the money value of returned goods. It stores how much is owed back to the customer. The amount can either be refunded in cash or bank, or adjusted against a future invoice.

Credit Note must be enabled in Settings before use.

The user cannot add any custom fields other than the fields that are already present in creation form.

## When & Who
- Any business that accepts returns: retailers, wholesalers, e-commerce sellers.
- Also used for goodwill credits, discount coupons, overcharges, or quality complaint adjustments without any physical goods return.

## Navigation
- Sale Return: Invoice List → tap on an invoice → Make Sale Return
- Credit Note: Side Menu → Credit Note → Create

## Key Fields

- **Return Quantity** — Number of units being returned. Cannot exceed the original invoice quantity.
- **Refund Amount** — The monetary value returned to the client in cash or via bank transfer.
- **Credit Note Amount** — The value of credit issued to the client for future use.
- **Credit Note Status** — Whether the credit has been applied against an invoice yet.
- **Sale Return Status** — Whether the monetary value of returned goods has been refunded.
- **Adjustment Amount** — The portion of a credit note being applied to a specific invoice.
- **Remaining Credit Balance** — The unused portion of a credit note still available for future transactions.

## Statuses

Sale Return statuses:
- **Not Refunded** — Return recorded; money not yet returned to client.
- **Refunded** — Money has been returned to client.

Credit Note statuses:
- **Not Adjusted** — Credit exists but not yet applied to an invoice.
- **Adjusted** — Credit has been fully applied against invoice(s).

## Credit Note Use Cases

A credit note can be issued when:
- A client returns goods (automatically linked to the sale return)
- A client was overcharged on a previous invoice
- A goodwill gesture or loyalty reward is offered
- A quality complaint is being settled
- A promotional discount is applied after a sale

## Credit Note: Refund vs. Adjustment

- **Refund** — Money is physically returned to the client (cash, bank, UPI). Credit note marked as refunded.
- **Adjustment** — No money changes hands. Credit amount reduces the client's next invoice total. Credit note marked as adjusted.
- **Partial Adjustment** — Part of the credit is used on one invoice; the remaining balance carries forward.
- **Multi-Invoice Adjustment** — A single credit note can be split and applied across multiple unpaid or partially paid invoices.

## Key Concept: Why Not Delete the Original Invoice
Deleting an invoice when goods are returned misrepresents financial history. The original sale happened and must stay in the books. A sale return is a contra entry — it offsets the original without erasing it. This is a principle of double-entry bookkeeping.

## Key Concept: Which Invoices Appear in Multi-Invoice Adjustment
Only invoices where payment is not received or partially received are shown. Fully paid invoices do not appear because there is nothing to adjust against.

## Key Concept: Credit Note Feature Toggle
When enabled in Settings, every sale return automatically generates a linked credit note. When disabled, sale returns are recorded without a credit note — only simple refunds are possible.

## Interaction with Other Features

- **Invoice** — Sale return is always linked to the original invoice.
- **Credit Note** — A credit note is created for every sale return to record the refund or adjustment amount.
- **Inventory** — Stock is automatically updated when a sale return is created (items are added back).
- **Reports** — Sale returns are reflected in reports and affect business metrics.
- **Client Transaction History** — Shows the sale return and updates the client's balance (reduces amount they owe).
- **Payment Received** — When recording payments, the sale return amount can be adjusted since it affects total receivable from the client.

## Alternate Terms

- Sale Return is also called: Sales Return, Return Inward, Customer Return, Goods Return
- Credit Note is also called: CN, Credit Memo, Store Credit, Credit Voucher
- Refund is also called: Reimbursement, Cashback, Money Back
- Adjust / Adjustment is also called: Apply, Offset, Set Off, Redeem
- Carry Forward is also called: Roll Over, Defer, Pending Credit

## Video Tutorials
- Record Sale Return & Refund: https://www.youtube.com/watch?v=GamzorLvw1s
- Adjust Sale Return with Credit Note: https://www.youtube.com/watch?v=GamzorLvw1s
- Issue a Credit Note to Client: https://www.youtube.com/watch?v=tIphGNPEiVs
- Adjust Credit Note Against Multiple Invoices: https://www.youtube.com/watch?v=mLJWo9v02Ro

## FAQs

**Q: What is a sale return in SIM?**
A: A sale return is created when a customer returns goods from a previous invoice. It connects to the original invoice, records what was returned, keeps the sale record intact, and adds returned items back to inventory.

**Q: Why should I not delete the original invoice when a customer returns goods?**
A: Deleting an invoice misrepresents financial history. The original sale happened and must stay in the books. A sale return offsets the original invoice without erasing it — this is standard accounting practice.

**Q: What is a credit note?**
A: A credit note records the monetary value owed back to the customer after a return. The amount can either be refunded in cash or bank, or used to reduce a future invoice.

**Q: How to issue a credit note to a client?**
A: First, ensure that the Credit Note feature is enabled from Settings.
Then Go to Side Menu → Credit Note → Create Note List → select client → enter amount → Save. When the client makes a future purchase, create an invoice and the available credit will appear for adjustment.

**Q: How to adjust a credit note against multiple invoices?**
A: Open the credit note → tap Adjust Credit Note Against Invoice. Only unpaid or partially paid invoices appear. Enter the adjustment amount for each invoice → review summary → tap Next to confirm.

**Q: What happens to inventory when a sale return is created?**
A: Returned items are automatically added back to inventory when the sale return is saved.

**Q: What is the difference between a refund and an adjustment on a credit note?**
A: A refund means money is physically returned to the client in cash or via bank. An adjustment means the credit reduces the client's next invoice total without any money changing hands.

---

# Sub Users & Approvals

## Definition
Sub users are separate login accounts created by the business owner for team members (staff, accountants, sales team). Each sub user has a role that defines what they can see and do in the app. The Transaction Approval feature ensures all transactions made by sub users require owner sign-off before becoming live.

## When & Who
- When the business grows beyond a single user.
- When staff create invoices but only the owner finalizes them.
- When different employees handle specific tasks (invoicing, payments) and oversight is needed.
- When managing multiple sales reps and restricting access to sensitive data.

## Navigation
Side Menu (☰) → Sub User Management → Manage Sub Users

## Sub User Limits
- Maximum 5 sub users can be added to an account.
- Only 3 sub users can be active at the same time.
- Sub users can be disabled, re-enabled, edited, or deleted at any time.
- This feature is available only for paid (subscribed) users.

## Predefined Roles
Available built-in roles:
- Partner / Manager
- Sales and Billing
- Purchase Manager
- Payment Collector
- Accountant

## Custom Role
The owner can define a custom role with exactly the permissions required:
- Navigate to Add Sub-User → Role dropdown → + Add Custom Role
- Enter role name, check or uncheck documents and permissions → Save Role

## Key Fields & Settings

- **Sub User Name** — Display name of the team member.
- **Role** — The assigned position that determines the sub user's permission set.
- **Permissions** — Individual access controls specifying what the sub user can view, create, edit, or delete.
- **Transaction Requires Approval** — When enabled, all sub user transactions enter a pending queue and are not live until the owner approves them.
- **Approval Status** — Pending = awaiting owner review. Approved = live in system. Rejected = not accepted.

## Approval Workflow

**Sub User Steps:**
1. Sub user creates an invoice or estimate → it enters Approval Pending status.
2. Sub user can check Approval Pending Transactions for pending documents.
3. Sub user can check Approval Rejected Transactions for rejected documents.
4. Sub user can edit a rejected document → tap Update → document returns to Approval Pending.

**Owner / Main User Steps:**
1. Side Menu (☰) → Cloud Account → Approval Pending Transactions.
2. If the invoice includes a new client or product, approve those first.
3. Approve the invoice → it moves to the main transaction list and becomes live.

## Logical Behaviors

- Maximum 3 active sub users allowed at one time.
- Sub users have limited access to app settings.
- If a client is rejected by the owner, all related documents (invoice, delivery note, etc.) are permanently deleted from the approval list. The sub user must recreate the document.
- Sub user can edit documents in Approval Pending status but cannot modify them after approval.
- Sub users cannot access features not enabled by the main user (e.g., Inventory, Commission, Delivery Note, Cash/Bank Transfer, Other Income).
- If restricted, sub users cannot edit rates in invoices, estimates, sale orders, or purchases.
- The main user can reset or change a sub user's password to revoke access.
- Payment approval depends on the approval of the related invoice.
- Proper device syncing is required to reflect updates across users.

## Key Concept: Role-Based Access Control (RBAC)
Each user is assigned a role, and each role carries a defined set of permissions. This ensures team members only access what is relevant to their function. A salesperson can create invoices but cannot view profit reports or delete records.

## Key Concept: Why Approve New Clients/Products First
When a sub user creates a new client or product during a transaction, those records exist only in a pending state. The owner must validate them before they become permanent records. This prevents duplicate entries, typographical errors, or unauthorized additions.

## Alternate Terms

- Sub User is also called: Staff Account, Employee Login, Team Member, Secondary User
- Role is also called: User Role, Access Level, Permission Level, Profile
- Transaction Requires Approval is also called: Maker-Checker, Dual Control, Approval Workflow, Authorization Workflow
- Approval Pending is also called: Awaiting Review, Under Approval, Pending Authorization

## Video Tutorials
- How to Create Sub Users: https://www.youtube.com/watch?v=rfirjho4Njs
- Transaction Requires Approval: https://www.youtube.com/watch?v=SAFW1J735_s

## FAQs

**Q: What is a sub user in SIM?**
A: A sub user is a separate login account created for a team member with specific roles and permissions. The owner controls what each sub user can see and do in the app.

**Q: How to create a sub user in SIM?**
A: Go to Side Menu (☰) → Sub User Management → Manage Sub Users → tap + → enter details → select role → tap Submit.

**Q: How many sub users can I add?**
A: Up to 5 sub users can be added. Only 3 can be active at the same time.

**Q: What happens when Transaction Requires Approval is enabled?**
A: All transactions created by sub users go into an Approval Pending queue. They are not live until the owner reviews and approves them. Sub users cannot edit or delete transactions after approval.

**Q: Why does the owner need to approve new clients before approving an invoice?**
A: If a sub user creates a new client during a transaction, that client exists only in pending state. The owner must approve the client record first to make it a permanent entry, then approve the related invoice.

**Q: What happens if the owner rejects a client record?**
A: If a client is rejected, all related documents (invoices, delivery notes, etc.) created by the sub user are permanently deleted from the approval list. The sub user must recreate them.

**Q: Can sub users access all app features?**
A: No. Sub users can only access features enabled by the main user. Features like Inventory, Commission, Delivery Note, Cash/Bank Transfer, and Other Income are not accessible to sub users unless the main user has enabled them and granted permission.

**Q: Is the Sub User feature available in the free trial?**
A: No. Sub user management is available only for paid (subscribed) users.

**Q: How to create Delivery Note?**
A: First, ensure that the Delivery Note feature is enabled from Settings.
Then Go to Side Menu → Delivery Note → Create Note → select client → enter amount → Save.

---

# GST Compliance — India

## Definition
SIM integrates directly with India's government GST infrastructure, enabling businesses to generate GST-compliant documents — E-Invoices and E-Way Bills — without logging into government portals separately.

All GST compliance features apply only to GST-registered businesses in India.

## Who It Applies To
- E-Invoice (IRN): Mandatory for GST-registered businesses with annual turnover exceeding ₹5 crore, for all B2B transactions.
- E-Way Bill: Required when transporting goods valued above ₹50,000 within India. Inter-state rules apply universally; intra-state rules vary by state.

## Core GST Concepts

- **GSTIN (GST Identification Number)** — A 15-digit unique identifier assigned to every GST-registered business in India. Encodes state code, PAN number, and entity type. Mandatory on all tax invoices.

- **GSP (GST Suvidha Provider)** — A government-authorized intermediary that provides a secure API channel between third-party apps like SIM and the GST portal. The GSP used by SIM is: BVMIT Consulting Services India Private Limited.

- **GSP Credentials (Username & Password)** — Separate from the regular GST portal login. Created specifically for API-based integration. Entered once in SIM to authorize the app to communicate with the government system.

- **IRP (Invoice Registration Portal)** — The government portal where B2B invoices are submitted and registered to receive an IRN.

- **IRN (Invoice Reference Number)** — A unique 64-character hash generated by the IRP for each registered B2B invoice. Printed on the invoice along with a QR barcode and acknowledgement number.

- **E-Invoice** — A B2B invoice registered with the IRP and assigned an IRN. The invoice is created in SIM; the IRN is fetched from the government portal via the GSP connection.

- **E-Way Bill (EWB)** — A digitally generated document required before transporting goods worth more than ₹50,000. Contains goods details, origin, destination, and transporter information.

- **Input Tax Credit (ITC)** — Allows GST-registered businesses to reduce their GST liability by the GST already paid on purchases. Requires a valid tax invoice with IRN where applicable.

- **UQC (Unique Quantity Code)** — A standardized, mandatory format for measurement units in e-invoice creation. The IRP requires all units to be reported using a fixed UQC list (e.g., NOS for pieces, KGS for kilograms). Free-text units are not accepted.

---

## A. GSP Setup for E-Invoice

### Definition
A one-time setup that creates GSP credentials on the government e-invoice portal and links them to SIM. Without this, SIM cannot communicate with the government system to generate IRNs.

### Key Fields

- **GSTIN** — Your 15-digit GST Identification Number. Used to validate your business on the portal.
- **GSP** — Authorized provider used by SIM: BVMIT Consulting Services India Private Limited.
- **GSP Username** — Created on the e-invoice portal. Always prefixed with API_ (e.g., API_yourusername).
- **GSP Password** — Linked to the GSP username. Must be updated in the app if changed on the portal.
- **Validate Seller GSTIN** — Verifies GSTIN against government records and auto-fills legal business name and address.

Important: GSP credentials are completely separate from your regular GST portal login. They are used only for app-to-portal integration.

### Video Tutorial
GSP Username & Password for E-Invoice: https://www.youtube.com/watch?v=dPSmtTALqQE

---

## B. Generating an E-Invoice (IRN)

### Definition
An e-invoice is a B2B invoice officially registered with the IRP and assigned a unique IRN. Legally required for businesses with annual turnover above ₹5 crore. Once generated, the invoice is locked — it cannot be edited or deleted.

### Key Fields

- **Invoice Type** — Must be set to B2B for e-invoicing. B2B = transaction between two GST-registered businesses.
- **HSN Code** — Mandatory for e-invoice. Classifies the type of goods or services for GST purposes.
- **UQC (Unique Quantity Code)** — Mandatory standardized unit format required by the IRP (e.g., NOS, KGS, LTR).
- **IRN** — The unique 64-character hash generated by the IRP. Printed on the invoice.
- **Acknowledgement Number** — A sequential confirmation number issued alongside the IRN.
- **QR Barcode** — Machine-readable code printed on the e-invoice encoding key invoice data for verification.

### E-Invoice Rules
- Once an IRN is generated, the invoice cannot be edited or deleted.
- Cancellation is only possible within 24 hours of IRN generation.
- After 24 hours, the IRN is permanent and cannot be reversed.

### E-Invoice Statuses
- **Ready for E-Invoice** — Invoice saved and eligible; IRN not yet generated.
- **IRN Generated** — E-invoice successfully registered with the government.
- **Cancelled** — IRN cancelled within the 24-hour window.

### Video Tutorial
How to Generate E-Invoice (IRN): https://www.youtube.com/watch?v=nobz4DVwbzc

---

## C. GSP Setup for E-Way Bill

### Definition
Generating e-way bills from SIM requires GSP credentials created on the government e-way bill portal. The process is identical to e-invoice GSP setup but done on a separate portal.

If already an e-invoice portal user, the same portal login credentials can be used to log in to the e-way bill portal. However, GSP credentials (API username/password) must be created separately on each portal.

### Portal Details
- E-Invoice portal: einvoice1.gst.gov.in
- E-Way Bill portal: ewaybill.gst.gov.in

### Video Tutorial
GSP Username & Password for E-Way Bill: https://www.youtube.com/watch?v=dPSmtTALqQE

---

## D. Generating an E-Way Bill

### Definition
An e-way bill is a mandatory digital document required before transporting goods worth more than ₹50,000 within India. Must be generated before goods leave the business premises. Without it, goods can be held at checkpoints and penalties may apply.

### Key Fields

- **Seller GSTIN** — Your GST number. Validated against government records.
- **Buyer GSTIN** — The client's GST number. Both seller and buyer must be GST-validated before an e-way bill can be generated.
- **Legal Name** — Official registered business name of the seller or buyer. Auto-fetched after GSTIN validation.
- **HSN Code** — Mandatory. Classifies the goods being transported.
- **Measurement Unit (UQC)** — Mandatory standardized unit (e.g., KGS, NOS, LTR).
- **Transporter Details** — Vehicle or courier information. Required to complete the e-way bill.
- **E-Way Bill Number** — The unique number generated upon successful submission. Must accompany goods during transport.

### E-Way Bill Generation — Two Ways
- From the E-Way Bill Section: Side Menu → Invoices → E-Way Bill → select invoice → fill details → Generate E-Way Bill.
- From the Invoice Form directly: fill invoice details → tap Generate E-Way Bill → e-way bill form opens and invoice is auto-saved.

### GSTIN Validation — Two Ways
- From Client section: Clients → select client → tap Validate GSTIN → enter details → validate.
- From Invoice form: select client → tap edit icon → enter GSTIN details → validate.

### E-Way Bill Rules
- Required for goods worth more than ₹50,000 being transported.
- Must be generated before goods leave your premises.
- Validity: 1 day per 200 km (or part thereof) for normal cargo vehicles. 1 day per 20 km for over-dimensional cargo.
- If validation fails, the system shows a specific error. Fix the flagged fields and retry. No penalty for failed attempts.

### Video Tutorial
How to Generate E-Way Bill: https://www.youtube.com/watch?v=nobz4DVwbzc

---

## Portal Login vs. GSP Credentials — Key Distinction

- Portal login (GSTIN + password) is for manually accessing the government website.
- GSP credentials (API username + password) are exclusively for app-to-portal integration.
- These are two completely different sets of credentials.

## Alternate Terms

- E-Invoice is also called: Electronic Invoice, IRN Invoice, Tax Invoice with IRN
- E-Way Bill is also called: EWB, Electronic Way Bill, Goods Movement Document
- GSTIN is also called: GST Number, GST ID, Tax ID, GST Registration Number
- GSP is also called: GST Suvidha Provider, API Provider, GST Intermediary
- IRP is also called: Invoice Registration Portal, Government E-Invoice Portal
- IRN is also called: Invoice Reference Number, E-Invoice Number
- HSN Code is also called: Harmonised System Nomenclature, Tariff Code, Product Classification Code
- UQC is also called: Unique Quantity Code, Measurement Unit Code
- ITC is also called: Input Tax Credit, GST Credit, Tax Set-Off
- Acknowledgement Number is also called: ACK Number, Confirmation Number

## FAQs

**Q: What is GST compliance in SIM?**
A: SIM integrates with India's government GST system to let businesses generate E-Invoices (IRN) and E-Way Bills directly from the app without logging into government portals separately.

**Q: Who needs to use e-invoicing in India?**
A: GST-registered businesses with annual turnover exceeding ₹5 crore must generate e-invoices for all B2B transactions.

**Q: What is GSP and why is it needed?**
A: GSP (GST Suvidha Provider) is a government-authorized intermediary that creates a secure connection between SIM and the GST portal. The GSP used by SIM is BVMIT Consulting Services India Private Limited.

**Q: What is the difference between GSP credentials and GST portal login?**
A: GST portal login (GSTIN + password) is for manually accessing the government website. GSP credentials (API username + password) are created separately and are used only for app-to-portal integration. They are completely different.

**Q: What is an IRN?**
A: IRN (Invoice Reference Number) is a unique 64-character code generated by the government's IRP for each registered B2B invoice. It confirms the invoice has been officially registered with the GST system.

**Q: Can an e-invoice be edited after the IRN is generated?**
A: No. Once an IRN is generated, the invoice cannot be edited or deleted. It can only be cancelled within 24 hours of generation.

**Q: How to cancel an e-invoice?**
A: Go to B2B Invoice List → Action column → three dots → Cancel IRN → choose reason → add remarks → tap OK. This must be done within 24 hours of IRN generation.

**Q: What is an E-Way Bill?**
A: An E-Way Bill is a mandatory digital document required when transporting goods worth more than ₹50,000 within India. It must be generated before goods leave the premises.

**Q: What is the validity of an e-way bill?**
A: 1 day per 200 km (or part thereof) for normal cargo vehicles. 1 day per 20 km for over-dimensional cargo.

**Q: What is UQC?**
A: UQC (Unique Quantity Code) is the mandatory standardized format for measurement units required by the government's IRP for e-invoice and e-way bill generation. Examples: NOS for pieces, KGS for kilograms, LTR for litres. Free-text units are not accepted.

**Q: How to set up GSP for e-invoicing?**
A: Log in to the e-invoice portal (einvoice1.gst.gov.in) → Left Menu → API Registration → User Credentials → verify OTP → select Through GSP → choose BVMIT Consulting Services India Private Limited → create GSP username and password → enter these credentials in SIM under Settings → E-Invoice Settings.

---

# Cloud Account

## Definition
The Cloud Account is the online account linked to SIM that stores and synchronizes business data across devices. It provides cross-device access (mobile, tablet, web), data security, and sync status visibility.

## When & Who
Used during initial app setup, when switching to a new device, and by any user who accesses SIM from multiple devices.

## Available Actions

**A. Sync Data with Cloud**
Pushes all device data to the cloud server and pulls updated data from the server.
Navigation: Side Menu → Cloud Account → Sync Data with Cloud

**B. Detailed Sync View**
Shows sync status: number of records synced, any errors, last sync time, records pending to send, and records pending to receive.
Navigation: Side Menu → Cloud Account → Detailed Sync View

**C. Change Password**
Updates the account password from within the app.
Navigation: Side Menu → Cloud Account → Change Password → enter old password, new password, and confirm password → Done

**D. Forgot Password**
Sends a password reset link to the registered email address.
Navigation: Side Menu → Cloud Account → Forgot Password → enter email address → reset link sent → set new password → log in

## Alternate Terms
Cloud Backup, Data Sync, Online Account, Sync Manager, Cloud Storage Settings, Account & Sync

## FAQs

**Q: What is Cloud Account in SIM?**
A: Cloud Account is the online account that stores and synchronizes all business data across devices. It enables access from multiple phones, tablets, and the web version.

**Q: How to sync data with the cloud in SIM?**
A: Go to Side Menu → Cloud Account → Sync Data with Cloud. This pushes device data to the server and pulls any updates.

**Q: How to change the account password in SIM?**
A: Go to Side Menu → Cloud Account → Change Password → enter old password, new password, and confirm → Done.

**Q: How to reset a forgotten password in SIM?**
A: Go to Side Menu → Cloud Account → Forgot Password → enter your email address → click the reset link sent to your email → set a new password.

**Q: What does the Detailed Sync View show?**
A: It shows the number of records synced, any errors, the last sync time, and records pending to send or receive.

---

# Online Store

## Definition
The Online Store is a built-in digital storefront inside SIM that allows businesses to list their products online and receive customer orders directly within the app. The store generates a shareable link that can be sent to customers or posted on social media. When a customer visits the link and places an order, it is automatically received in the app as a Sale Order — no manual entry required.

This is a Beta feature and must be enabled before use.

## When & Who
- Businesses that want a simple online presence without managing a separate e-commerce platform.
- Retailers, small shops, and service providers who share catalogues via WhatsApp, social media, or messaging.
- Any business that wants to automate order collection from walk-in or repeat customers.

## Navigation Path
Settings → Enable / Disable Features or Search → Online Store → Enable Store Feature → Enter store name

## Store Identity Fields

- **Store Name** — The name displayed to customers on the storefront. Should match the business name or brand.
- **Store Logo** — An uploaded image that appears as the store's brand identity on the customer-facing page.
- **Store Link** — A unique URL automatically generated by the app. Shareable directly with customers or on social platforms.

## Product Detail Fields (Online Store)

- **Product Code** — A reference identifier for the product. Helps with internal tracking.
- **Rate** — The selling price displayed to customers on the store.
- **Units** — The measurement unit (e.g., pcs, kg, box).
- **Product Category** — The store category this product belongs to (e.g., Electronics, Clothing).
- **Maximum Order Quantity** — The maximum number of units a single customer can order in one transaction. Useful for managing stock.
- **Offer Price** — A discounted price enabled via a checkbox. When set, both the original rate and offer price are displayed to show the customer the deal.
- **Product Description** — A text description of the product including features, specifications, and usage. Helps customers make informed decisions.
- **Product Image** — A photo of the product. Can be added from the product details form or from the Manage Product Images section in Product Settings.
- **Additional Info** — Free-form field for extra details not covered by standard fields.
- **Product Tag** — A short label displayed as a badge on the product (e.g., "20% OFF", "New Arrival", "Limited Edition"). Requires Show Tag to be enabled in Site Settings.

## Store Settings

**1. Product Settings**
- Manage product details such as name, price, category, description, image, and offers.
- Control product availability and display.
- Set order limits and arrange product sequence.
- Enable or disable adding new products to the store.

**2. Online Store Site Settings**
Controls how the store looks and what customers see.
- Theme — Choose the store design and layout.
- Language — Set the store's display language.
- Show / Hide options — Control visibility of prices, product availability, product tags, and contact details.
- Sale Order Form Fields — Decide what customer information to collect at checkout (name, phone, email, etc.) and add custom fields.

**3. Product Category**
- Organizes similar products into groups.
- Enable or disable categorization, view existing categories, and add new ones with a name and optional thumbnail.
- Categories can be edited or deleted individually or in bulk.

**4. Manage Product Images**
- Assign images to each product using the (+) button.
- Existing images can be removed using the delete icon.
- Multiple product images can be managed at once.

**5. Banner Settings**
- Upload and manage promotional banners displayed at the top of the store as a carousel.
- Up to 5 banner images can be uploaded.
- Each banner can be linked to a specific Product, a Category, or set to None (display only).
- Banners can be removed or reassigned individually or in bulk.


## Alternate Terms

- Online Store is also called: Digital Store, Web Store, E-commerce Store, Online Shop, Customer Portal
- Store Link is also called: Shop URL, Store URL, Share Link
- Published is also called: Active, Live, Visible
- Disabled is also called: Hidden, Inactive, Unlisted
- Product Tag is also called: Label, Badge, Offer Tag, Promo Tag
- Sale Order Form is also called: Checkout Form, Order Form, Customer Details Form
- Banner is also called: Promotional Banner, Hero Image, Carousel Image, Slider

## Video Tutorials
- How to Setup Online Store — Part 1: https://www.youtube.com/watch?v=i-aXeyaAJsk&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=26
- Update Product Details & Categorize — Part 2: https://www.youtube.com/watch?v=B4xzr0MT9lI&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=27
- Store Settings & Banners — Part 3 & 4: https://www.youtube.com/watch?v=cTuf7Zc462g&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=28
&
https://www.youtube.com/watch?v=1UfdbfEZe84&list=PL9NRmuo_lj22dReggkiHIZRUK-b-4kWKz&index=29

## FAQs

**Q: What is the Online Store feature in SIM?**
A: The Online Store is a built-in digital storefront that lets businesses list products online and receive customer orders directly in the app as Sale Orders. It generates a shareable store link without needing a separate e-commerce platform.

**Q: How to enable the Online Store in SIM?**
A: Go to Settings → Enable / Disable Features → Online Store → Enable Store Feature → enter your store name.

**Q: How to share the online store link with customers?**
A: After enabling the store, a unique Store Link is automatically generated by the app. Share this link directly with customers via WhatsApp, social media, or messaging.

**Q: What is a Product Tag in the Online Store?**
A: A Product Tag is a short badge displayed on the product listing (e.g., "20% OFF", "New Arrival"). The Show Tag option must be enabled in Site Settings for tags to appear on the store.

**Q: What is the difference between Offer Price and Rate in the Online Store?**
A: Rate is the regular selling price. Offer Price is a discounted price enabled via a checkbox. When set, both prices are shown to the customer to highlight the deal.

**Q: How many banners can I upload in the Online Store?**
A: Up to 5 banner images can be uploaded. They display as a carousel at the top of the store.

**Q: What happens when a customer places an order through the Online Store?**
A: The order is automatically received in the app as a Sale Order under the Online Store Sale Order list. No manual entry is needed.

**Q: Can I control what information customers fill at checkout?**
A: Yes. Go to Site Settings → Sale Order Form Fields to decide what customer information (name, phone, email, etc.) is collected at checkout. Custom fields can also be added.

**Q: What is the size limit for banner images?**
A: Banner images must be under 2 MB in file size. The aspect ratio defines the shape of the banner. Supported ratios include 5:2, 16:7, 7:2, etc.

**Q: Can I change the logo of my store later?**
A: Yes, you can update or change your store logo at any time from the store settings. The updated logo will be reflected on your storefront.

---

# POS Billing

## Definition
POS (Point of Sale) Billing is a fast checkout mode in SIM designed for retail shops where speed is critical. It changes the app screen into a billing counter optimized for quickly adding items, collecting payments, and generating receipts. It supports hardware like barcode scanners and thermal printers, and also works with the phone's built-in camera for scanning.

## When & Who
- Retail shops, supermarkets, pharmacies, restaurants, and any business with a physical billing counter.
- Ideal for businesses with high sales volume that need fast checkout.

## Navigation Path
Dashboard → Side Menu (☰) → Enable / Switch to POS → Create Invoice page → Select products → Save and Next → Select customer and payment type → Save and Exit

## Product Addition Methods

Three ways to add products to the cart during a POS transaction:
- **Search by Name** — Type the product name to find and add it.
- **Tap Product Icon** — Tap the product tile directly from the visual product grid.
- **Barcode Scan** — Scan the product's barcode using a paired scanner or the device camera.

The cart total updates in real-time as items are added.

## Key Fields During Checkout

- **Quantity Adjustment** — Increase or decrease item quantities using + and − buttons on the cart screen.
- **Discount** — A discount can be applied to the total before finalizing the bill.
- **Customer Type** — Identifies the type of customer. Options: Walk-in (anonymous), POS, or Regular (linked to a client record).
- **Payment Method** — The mode of payment accepted — Cash, UPI, Credit Card, or other configured methods.

## Transaction Completion Options

- **Save & Next** — Saves the transaction and immediately opens a new blank billing screen for the next customer. No receipt printed.
- **Save & Exit** — Saves the transaction and returns to the main screen. No receipt printed.
- **Print & Exit** — Saves the transaction and triggers the print popup to send a receipt to the connected thermal printer.

## Optional Hardware

These devices are not required but make billing faster:

- **Thermal Printer** — Instantly prints receipts. Supports 58mm and 80mm sizes. Connects via Bluetooth or cable.
- **Barcode Scanner** — Adds products quickly by scanning barcodes. Connects via Bluetooth or cable. If no physical scanner is available, the device camera can be used.

Navigation to configure hardware: Settings → Hardware & Devices → Printer Settings / Scanner Settings

## Key Concepts

- **POS vs. Standard Invoice** — Both create a sales record. POS mode is optimized for speed at a physical counter with product images, barcode scanning, and instant printing. Standard invoicing is for detailed billing, document customization, and client-specific records.
- **Walk-in Customer** — An anonymous customer. No customer details are saved. Used for one-time buyers.
- **Regular Customer** — A customer with full details saved (name, address, phone, GSTIN). Used for repeat or wholesale customers.

## Alternate Terms

- POS Billing is also called: Point of Sale, Retail Billing, Counter Billing, Cashier Mode
- Walk-in Customer is also called: Anonymous Customer, Counter Customer, Cash Customer
- Thermal Printer is also called: Receipt Printer, Bill Printer, POS Printer
- Barcode Scanner is also called: Bar Code Reader, Product Scanner
- Save & Next is also called: New Bill, Next Customer
- Cart is also called: Basket, Order, Bill Items

## Video Tutorials
- Set up Point of Sale (POS Billing): https://www.youtube.com/watch?v=-QyFTJlv-I0

## FAQs

**Q: What is POS Billing in SIM?**
A: POS Billing is a fast checkout mode in SIM for shops with physical billing counters. It optimizes the interface for speed — adding items by scanning or tapping, collecting payment, and printing receipts.

**Q: How to enable POS mode in SIM?**
A: Go to the Side Menu → Switch to POS Mode → Enable → OK.

**Q: What is a Walk-in Customer in POS mode?**
A: A Walk-in Customer is an anonymous buyer. No details are saved. Walk-in customers appear in an aggregated form in reports, separate from regular customers.

**Q: How to add products in POS billing?**
A: Products can be added by searching by name, tapping the product tile on the grid, or scanning the barcode using a paired scanner or the device camera.

**Q: Does POS billing support a thermal printer?**
A: Yes. Thermal printers (58mm or 80mm) can be connected via Bluetooth or cable. Configure from Settings → Hardware & Devices → Printer Settings.

**Q: What is the difference between Save & Next and Save & Exit in POS?**
A: Save & Next saves the current transaction and opens a new blank screen for the next customer. Save & Exit saves the transaction and returns to the main screen. Print & Exit saves the transaction and triggers receipt printing.

**Q: Can I use POS billing without a barcode scanner?**
A: Yes. If no physical scanner is available, the device's built-in camera can be used to scan barcodes.

---

# Reports

## Definition
The Reports section converts all raw transaction data — invoices, purchases, payments, expenses — into structured financial summaries and insights. It covers sales performance, purchase tracking, pending dues, tax summaries, inventory valuation, profit & loss, and more.

## When & Who
- Daily — to check sales figures and payment collections.
- Weekly / Monthly — to track business performance trends.
- During tax filing — to calculate GST, VAT, or other applicable taxes.
- Business owners and freelancers — for overall financial visibility.
- Accountants and finance teams — for reconciliation and tax computation.
- Sales managers — for revenue tracking and client performance.

## Navigation Path
Dashboard → Side Menu (☰) → Reports → Select any report from the list

## Report Categories & Full Report List

### Sales Reports

- **Transaction History / Ledger** — Complete transaction-wise ledger for each client. Shows invoices raised, payments received, and outstanding balance.
- **Sales / Payment Report** — Summary of total sales and payments received within a selected period.
- **Product Report** — Sales performance broken down by product. Shows quantity sold and revenue generated.
- **Sales by Clients — Top 5** — The five highest-value clients by sales amount in the selected period.
- **Sales by Products — Top 5** — The five best-selling products by revenue in the selected period.
- **History of Sales / Payment** — A chronological record of all sales transactions and associated payments.
- **Invoice Aging** — Groups unpaid invoices by how long they have been outstanding (e.g., 0–30 days, 31–60 days, 60+ days). Helps identify overdue collections.
- **Detailed Sales Report** — Line-item level breakdown of all sales showing client, product, quantity, rate, tax, and total for each invoice.
- **Sales Order Report** — Status and value summary of all sale orders — pending and completed.
- **Sales Return Report** — Record of all returned goods showing linked invoices, return quantities, and refund or credit note status.

### Purchase Reports

- **Purchase / Payment Report** — Summary of total purchases and payments made to suppliers within a selected period.
- **Detailed Purchase Report** — Line-item level breakdown of all purchases showing supplier, product, quantity, rate, tax, and total.
- **Purchase Order Report** — Status and value summary of all purchase orders — pending and completed.

### Inventory Reports

- **Check Inventory Status** — Current stock quantity for all inventory-enabled products. Highlights items below the minimum alert level.
- **Inventory Valuation (FIFO)** — Total monetary value of current stock calculated using the First In, First Out method.
- **Inventory Valuation (Average)** — Total monetary value of current stock using the weighted average cost method.
  - Year Wise – COGS Average Method: Shows inventory cost, COGS, and remaining stock for a full financial year.
  - Product Wise – COGS Method: Shows stock quantity, average cost, and value for each individual product.

### Profit & Loss Reports
If you want to check P&L report related to: Opening closing stock, monthly/weekly, Daily the P&L, Product, Invoice and Client you can check the following report:

- **P&L Using COGS** — Profit and loss calculated using Cost of Goods Sold. Formula: Revenue − COGS.
- **P&L Using Opening / Closing Stock** — Profit and loss factoring in stock value at the start and end of a period. Formula: Gross Profit = Sales − (Opening Stock + Purchases − Closing Stock).
- **Monthly / Weekly / Daily P&L — COGS** — P&L broken down by time period using the COGS method.
- **Monthly / Weekly / Daily P&L — Changes in Stock** — P&L broken down by time period using the stock change method.
- **Product-wise Profit / Loss** — Profitability for each individual product showing revenue, cost, and margin.
- **Invoice-wise Profit / Loss** — Profitability shown per invoice. Identifies high-margin and low-margin transactions.
- **Customer-wise Profit / Loss** — Profitability broken down by client. Identifies which clients generate the most profit.

### Tax Reports

- **Sales / Purchase Tax Report** — Total tax collected on sales and tax paid on purchases within a period. Breakdown by tax type (SGST, CGST, IGST, etc.). Used for GST / VAT filing.

### Other Reports

- **Expense Report** — Summary of all business expenses recorded in the app by category and period.
- **Commission Report** — Agent-wise commission earned based on invoices they are assigned to.
- **Payment Account Report** — Summary of payments categorized by payment account or mode (e.g., cash, bank, UPI).

- **Cash / Bank Report** — This report shows the records all transactions and payments involving Cash/bank and other

## Key Concepts

- **COGS (Cost of Goods Sold)** — The direct cost incurred to purchase or produce goods sold in a period. P&L using COGS = Revenue − COGS. It does not account for remaining unsold stock.
- **P&L Using Opening / Closing Stock** — Calculates gross profit as: Sales − (Opening Stock + Purchases − Closing Stock). Accounts for the change in inventory value over the period. Commonly used in trading businesses.
- **Inventory Valuation** — The monetary value assigned to unsold stock at a point in time. Differs depending on the method used (Weighted Average or FIFO) and directly impacts reported profit and balance sheet figures.
- **Invoice Aging** — Classifies unpaid invoices by how long they have been outstanding. A standard tool for prioritizing overdue collections.

## Alternate Terms

- Reports is also called: Analytics, Insights, Financial Summary, Business Reports, MIS Reports
- Transaction History / Ledger is also called: Client Ledger, Account Statement, Party Statement
- Invoice Aging is also called: Aging Report, Overdue Report, Receivables Aging
- P&L is also called: Profit & Loss Statement, Income Statement, P&L Account
- COGS is also called: Cost of Goods Sold, Cost of Sales, Direct Cost
- Inventory Valuation is also called: Stock Valuation, Closing Stock Value
- Sales / Purchase Tax Report is also called: GST Report, VAT Report, Tax Summary
- Expense Report is also called: Expenditure Report, Cost Report
- Commission Report is also called: Agent Report, Salesperson Commission
- Payment Account Report is also called: Payment Mode Report, Collection Report

## FAQs

**Q: Where are reports in SIM?**
A: From the dashboard, Side Menu (☰). Tap on any report category to see the full list.

**Q: How to get a client ledger or statement?**
A: Go to Reports → Sales → Transaction History / Ledger → tap on a specific client. This shows all invoices, payments, credit notes, and returns along with the outstanding balance.

**Q: What is Invoice Aging?**
A: Invoice Aging groups unpaid invoices by how long they have been outstanding (e.g., 0–30 days, 31–60 days, 60+ days). It helps identify overdue collections and prioritize follow-ups.

**Q: What is the difference between P&L Using COGS and P&L Using Opening / Closing Stock?**
A: P&L Using COGS calculates profit as Revenue minus the direct cost of goods sold. P&L Using Opening/Closing Stock calculates gross profit as: Sales − (Opening Stock + Purchases − Closing Stock). The second method accounts for the change in inventory value.

**Q: How to generate a GST tax report in SIM?**
A: Go to Reports → Tax → Sales / Purchase Tax Report. This shows total tax collected and paid, broken down by SGST, CGST, IGST, and other tax types for a selected period.

**Q: How to check the commission report?**
A: Go to Reports → Other → Commission Report. This shows agent-wise commission earned based on invoices they are assigned to.

**Q: What is the Inventory Valuation report?**
A: The Inventory Valuation report shows the total monetary value of current unsold stock. It is available in two methods: Weighted Average and FIFO.

---

# Other Income

## Definition
Other Income is a feature to record money earned outside of regular sales invoices. It captures income that has no linked client, product, or invoice — ensuring all business earnings are reflected in financial reports and P&L.

Examples of Other Income:
- Interest income earned on bank deposits
- Rental income from property or equipment leasing
- Discounts received from vendors
- Miscellaneous or one-time earnings

This feature must be enabled before use. It is disabled by default.

## When & Who
- When income is received without generating a client invoice.
- For one-time or irregular earnings outside the normal sales cycle.
- During accounting or tax preparation to ensure complete financial records.
- Small business owners, shopkeepers, freelancers, and accountants.

## Navigation Path

To enable: Settings → Enable / Disable Features → Other Income → Enable Other Income Feature

To use after enabling: Dashboard → Side Menu (☰) → Other Income → Other Income List → Create Other Income → Enter details → Save

## Key Fields

- **Date** — The date on which the income was received.
- **Name / Description** — A label for the entry (e.g., "Bank Interest", "Rental Income", "Vendor Discount").
- **Amount** — The monetary value of the income received.
- **Note** — Optional free-text field for additional context or remarks.
- **Payment Account** — The cash or bank account through which the income was received. Requires the Payment Account feature to be enabled separately from Settings.

## Optional Sub-Feature

**Payment Account** — To record which cash or bank account the income was received into, the Payment Account feature must be enabled from Settings → Enable / Disable Features. Once enabled, a Payment Account field appears on the Other Income entry form.

## Key Concepts

- **Other Income vs. Sales Income** — Sales income is generated from invoices raised to clients for products or services. Other income is any earning with no linked client, product, or invoice. Keeping them separate ensures clean financial reporting and accurate P&L.
- **Impact on Reports** — Other income entries are reflected in Profit & Loss reports and the dashboard financial summary. They appear under a separate income category, keeping sales and non-sales income distinguishable.

## Alternate Terms

- Other Income is also called: Miscellaneous Income, Additional Income, Non-Sales Income, Indirect Income, Other Receipts, Extra Earnings

## Important Notes-
- The user cannot add any custom fields other than the fields that are already present in creation form.

## FAQs

**Q: What is Other Income in SIM?**
A: Other Income is used to record earnings not linked to any invoice, client, or product — such as interest income, rental income, vendor discounts, or miscellaneous receipts. It ensures all business earnings appear in financial reports.

**Q: How to enable Other Income in SIM?**
A: Go to Settings → Enable / Disable Features → Other Income → Enable Other Income Feature.

**Q: How to add an Other Income entry?**
A: After enabling, go to Dashboard → Side Menu (☰) → Other Income → tap Create Other Income (+) → enter date, name, amount, and note → Save.

**Q: Does Other Income appear in P&L reports?**
A: Yes. Other income entries are reflected in Profit & Loss reports and the overall dashboard financial summary. They appear under a separate income category, distinct from sales income.

**Q: What is the difference between Other Income and Sales Income?**
A: Sales income comes from invoices raised to clients for products or services delivered. Other income is any earning with no linked client, product, or invoice (e.g., bank interest, rent received).

**Q: Can I record which bank account Other Income was received into?**
A: Yes, but the Payment Account feature must be enabled from Settings → Enable / Disable Features first. Once enabled, a Payment Account field appears in the Other Income entry form.

---

# Switch Users

## Definition
Switch Users allows multiple user accounts to be accessed from the same device without uninstalling the app or resetting data. Each user account maintains completely independent data — invoices, clients, products, reports. New users can be created or existing accounts can be logged in through this feature.

There is no limit on the number of user accounts that can be added.

## When & Who
- When multiple people share the same physical device (e.g., a shared billing tablet).
- When one person manages multiple businesses, each with separate books.
- When an accountant handles multiple client accounts on one device.
- Business owners with multiple shops or business entities.
- Accountants managing multiple clients.
- Staff members sharing a single device at a counter.

## Navigation Path
Side Menu (☰) → Cloud Account → Switch User → Add User

From the login screen: log in with an existing registered account or register a new one.

## Managing Multiple Organizations

- Multiple companies or organizations can be managed using the Switch User feature.
- A separate subscription must be purchased for each additional organization.
- To purchase an additional organization: Side Menu → Upgrade → Purchase Additional Organization
- To switch between organizations: Side Menu → Cloud Account → Switch User

## Key Concepts

- **Data Separation** — Each user account in SIM operates as a completely independent instance. Invoices, clients, suppliers, products, and reports of one account are not visible to or shared with another account on the same device. Switching users changes the entire working context of the app.
- **Cloud Account Requirement** — Switch Users works through the Cloud Account system. Each account must be registered and synced with the cloud to be accessible across devices.

## Alternate Terms

- Switch Users is also called: Change User, Switch Account, Account Switch, Multi-User Mode, Profile Switching, User Management

## FAQs

**Q: What is the Switch Users feature in SIM?**
A: Switch Users allows multiple separate user accounts to be accessed from the same device. Each account has its own independent data — invoices, clients, products, and reports.

**Q: How to switch between users in SIM?**
A: Go to Side Menu → Cloud Account → Switch User. Select the account to switch to or add a new one.

**Q: Is there a limit on how many users can be added?**
A: There is no limit on the number of user accounts that can be added via Switch Users.

**Q: Can I manage multiple businesses from one device?**
A: Yes. Multiple businesses can be managed using Switch Users. Each business needs its own user account and a separate subscription.

**Q: How to purchase an additional organization account?**
A: Go to Side Menu → Upgrade → Purchase Additional Organization.

**Q: Is data shared between different user accounts on the same device?**
A: No. Each user account operates as a completely independent instance. Data from one account is not visible to or shared with another account on the same device.

---

# Receivable & Payable

## Definition

- **Receivable (Accounts Receivable)** — The total amount clients owe the business for invoices issued but not yet paid.
- **Payable (Accounts Payable)** — The total amount the business owes to suppliers for purchases received but not yet paid for.

Both are visible on the dashboard in the Summary Layout. The layout must be switched from the default view to Summary Layout to see these figures.

## When & Who

**Receivable:**
- After invoices are raised but before payment is collected.
- Used by business owners, freelancers, and sales/accounts teams.

**Payable:**
- After purchase records are created but before payment is made to suppliers.
- Used by business owners, procurement teams, and accountants.

## Navigation Path

To view Receivables: Dashboard → Switch to Summary Layout → Receivables section → Balance Receivables

To view Payables: Dashboard → Switch to Summary Layout → Payables section → Balance Payable

## How Balances Change

- Receivable balance increases — when an invoice is created and payment has NOT been marked as received.
- Receivable balance decreases — when payment is recorded against an invoice (Mark as Received).
- Payable balance increases — when a purchase record is created and payment has NOT been marked as paid.
- Payable balance decreases — when payment is made to the supplier (Mark as Paid).

## Optional Features

**Receivable:**
- Payment Reminders — Send reminders to clients for overdue invoices.
- Invoice Aging Report — View overdue invoices grouped by time brackets (0–30 days, 30–60 days, 60+ days).
- Partial Payment Tracking — Track how much has been paid and how much remains outstanding per invoice.

**Payable:**
- Due Date Reminders — Get notified when a supplier payment is due.
- Expense Categorization — Classify payables by expense type.
- Recurring Bills — Track regularly recurring payables like rent and subscriptions.
- Approval Workflow — Route payables through an approval process before payment (linked to Sub User approval feature).

## Key Concepts

- **Accounts Receivable (AR)** — Money owed to the business by customers. It is an asset on the balance sheet. High AR with slow collection indicates cash flow risk.
- **Accounts Payable (AP)** — Money the business owes to suppliers. It is a liability on the balance sheet. Managing AP efficiently helps maintain supplier relationships and avoid late payment penalties.
- **AR vs. AP in Cash Flow** — A business is cash-flow healthy when it collects receivables faster than it pays its payables. Monitoring both in SIM gives the owner a clear picture of net cash position.
- **Summary Layout** — A specific dashboard view in SIM that shows a financial summary including Receivable and Payable balances. Must be selected manually — the default layout does not show these figures.

## Alternate Terms

- Receivable is also called: Accounts Receivable (AR), Outstanding Invoices, Customer Dues, Money to Collect, Debtors
- Payable is also called: Accounts Payable (AP), Outstanding Purchases, Supplier Dues, Money to Pay, Creditors
- Balance Receivable is also called: Total Outstanding, Unpaid Invoices Total, AR Balance
- Balance Payable is also called: Total Dues, Unpaid Purchases Total, AP Balance
- Mark as Received is also called: Payment Collected, Invoice Paid, Clear Receivable
- Mark as Paid is also called: Payment Made, Supplier Paid, Clear Payable

## FAQs

**Q: What is Receivable in SIM?**
A: Receivable (Accounts Receivable) is the total amount clients owe the business for invoices that have been issued but not yet paid.

**Q: What is Payable in SIM?**
A: Payable (Accounts Payable) is the total amount the business owes to suppliers for purchases received but not yet paid for.

**Q: How to view Receivable and Payable balances in SIM?**
A: Switch the dashboard to Summary Layout. Receivables and Payables are visible in their respective sections on this view.

**Q: How does the Receivable balance decrease?**
A: The Receivable balance decreases when a payment is recorded against an invoice using Mark as Received.

**Q: How does the Payable balance decrease?**
A: The Payable balance decreases when payment is made to a supplier using Mark as Paid.

**Q: What is the Summary Layout?**
A: Summary Layout is a specific dashboard view in SIM that shows a financial summary including Receivable and Payable balances. It must be selected manually as the default layout does not show these figures.

---

# Delivery Note

## Definition
A delivery note is a shipping document issued by the seller that physically accompanies goods during transit. It details the items dispatched, quantities, and destination. It is not a request for payment — it is proof of dispatch and proof of delivery.

SIM supports two workflows:

- **Dispatch first, invoice later** — Create a delivery note at the time of dispatch and convert it into an invoice once billing is due.
- **Invoice first, deliver later** — Create the invoice first and generate a delivery note from it at the time of physical dispatch.

This feature must be enabled before use. It is disabled by default.

## When & Who

- When goods are dispatched before the invoice is raised (common in credit sales).
- When a partial delivery is made and billing will follow later.
- When goods need to travel before the customer has approved or inspected them.
- In milestone-based or project billing where invoicing happens in stages.

Who uses it:

- Business Owner / Sales Team — Creates and issues the delivery note at the time of dispatch.
- Warehouse / Dispatch Team — Uses it as the dispatch instruction and packing reference.
- Customer — Signs or acknowledges the delivery note as proof of receipt.
- Accounts Team — Converts the pending delivery note into a final invoice for billing.

## Navigation Path

To enable: Settings → Enable / Disable Features → Delivery Note → Enable

To create from an existing invoice: Invoice List → Tap on an Invoice → Make Delivery Note

To create as a standalone document: Side Menu → Delivery Note → Create Delivery Note
Then to convert to invoice: Delivery Note List → Tap on a Pending Delivery Note → Make Invoice

## Sub-Settings

- **Enable Delivery Note Feature** — Activates delivery note creation and management in the app.
- **Display Rate and Amount** — When enabled, product rates and total amounts are shown on the delivery note. When disabled, only items and quantities appear with no pricing.

### Delivery Note Statuses

- **Invoice Pending** — Goods have been delivered but no invoice has been raised yet.
- **Invoiced** — Goods have been delivered and the invoice has been raised.

## Key Concepts

- **Delivery Note vs. Invoice** — An invoice is a payment request. A delivery note is a dispatch confirmation. In many businesses, goods travel first and billing happens later, making the delivery note the primary document at the point of dispatch.
- **Delivery Note vs. E-Way Bill** — A delivery note is an internal business document. An E-Way Bill is a government-mandated compliance document required for transporting goods worth more than ₹50,000 within India. Both can be used together for the same shipment.
- **Partial Delivery** — When a customer orders 100 units but only 60 are available, a delivery note is raised for 60 units. The remaining 40 are shipped later with a separate delivery note. The final invoice is raised once all deliveries are complete, or separate invoices can be raised per delivery.

## Alternate Terms

- Delivery Note is also called: Delivery Challan, Goods Dispatch Note, Dispatch Challan, Shipment Note, Delivery Slip, Challan

## FAQs

**Q: What is a Delivery Note in SIM?**
A: A delivery note is a shipping document that accompanies goods during transit. It confirms what was dispatched, in what quantity, and to where. It is not a payment request — it is proof of dispatch and delivery.

**Q: How to enable the Delivery Note feature in SIM?**
A: Go to Settings → Enable / Disable Features → Delivery Note → Enable.

**Q: How to create a delivery note from an invoice?**
A: Go to the Invoice List → tap on the invoice → tap Make Delivery Note.

**Q: How to create a standalone delivery note and convert it to an invoice later?**
A: Go to Side Menu → Delivery Note → Create Delivery Note. Later, go to Delivery Note List → tap on a Pending Delivery Note → tap Make Invoice.

**Q: What is the difference between a Delivery Note and an E-Way Bill?**
A: A delivery note is an internal business document confirming dispatch. An E-Way Bill is a government-mandated compliance document required for transporting goods worth more than ₹50,000 in India. Both can be used together.

**Q: What does the Display Rate and Amount setting do on a Delivery Note?**
A: When enabled, product rates and total amounts are shown on the delivery note. When disabled, only item names and quantities appear — no pricing is shown.

**Q: What is the Invoice Pending status on a delivery note?**
A: Invoice Pending means goods have been delivered but no invoice has been raised yet for this delivery note.

---

# Commission

## Definition
Commission is a performance-based payment made to an agent, salesperson, or partner for facilitating a sale or transaction. In SIM, commission can be calculated on the selling price or the discounted selling price. It is excluded from the invoice total and treated as a business expense.

This feature must be enabled before use. It is disabled by default.

## When & Who

- When a sale is generated through an agent or salesperson.
- When a payment is received and commission becomes payable.
- When tracking partner or reseller payouts.

Who uses it:
- Salespersons / Employees — Earn commission on invoices they are responsible for.
- Agents / Brokers — Receive a fee for deals they bring to the business.
- Resellers / Partners — Earn a payout on sales made through them.
- Business Owner — Tracks total commission expense and agent-wise performance.

## Navigation Path

To enable: Settings → Enable / Disable Features → Commission → Enable Commission Feature → Select valuation method

To add an agent: Side Menu → Commission → Add New Agent

To assign commission on an invoice: Create Invoice → Add Agent → Enter commission percentage or flat amount

To view commission report: Dashboard → Reports → Other → Commission Report

## Sub-Settings

- **Enable Commission Feature** — Activates agent creation and commission tracking in the app.
- **Commission Valuation Method** — Determines how commission is calculated: on the full selling price of products, or on the discounted selling price.

## Key Fields

- **Agent Name** — The person or entity receiving the commission. Created as a named profile in the Commission section.
- **Commission Type** — Whether commission is calculated as a percentage of the invoice value or as a flat fixed amount per invoice.
- **Commission Percentage** — The percentage of the invoice total payable as commission (e.g., 5% of ₹10,000 = ₹500).
- **Flat Commission Amount** — A fixed amount paid regardless of invoice value (e.g., ₹200 per invoice).

## Key Concepts

- **Commission as Expense** — Commission paid to agents is an indirect expense. It appears in the Profit & Loss statement as a cost, reducing net profit. SIM tracks this separately so the business can see total commission outgo against revenue earned.
- **Percentage vs. Flat Commission** — Percentage-based commission scales with the sale value (higher sale, higher commission). Flat-amount commission is a fixed predictable amount regardless of deal size — used for fixed-fee services or standard transactions.

## Alternate Terms

- Commission is also called: Sales Commission, Agent Commission, Brokerage, Referral Fee, Incentive, Sales Incentive, Partner Payout
- Agent is also called: Salesperson, Broker, Referral Partner, Reseller, Channel Partner
- Commission Report is also called: Agent Report, Incentive Report, Payout Summary

## FAQs

**Q: What is Commission in SIM?**
A: Commission is a payment made to an agent or salesperson for facilitating a sale. SIM tracks commission per agent, calculates it on selling or discounted price, and treats it as a business expense.

**Q: How to enable Commission in SIM?**
A: Go to Settings → Enable / Disable Features → Commission → Enable Commission Feature → select the commission valuation method (on selling price or discounted selling price).

**Q: How to add a commission agent in SIM?**
A: First ensure, To enable: Settings → Enable / Disable Features → Commission → Enable Commission Feature → Select valuation method.
Go to Side Menu → Commission → Add New Agent → fill in agent details and commission rate → Save. To assign commission on an invoice: Create Invoice → Add Agent → Enter commission percentage or flat amount

**Q: How to assign commission to an invoice?**
A: When creating an invoice, go to the Agent field → select the agent → enter the commission percentage or flat amount.

**Q: What is the difference between percentage-based and flat commission?**
A: Percentage-based commission scales with the sale value — higher sale means higher commission. Flat commission is a fixed amount paid per invoice regardless of the sale value.

**Q: Is commission included in the invoice total?**
A: No. Commission is excluded from the invoice total and treated as a separate business expense.

**Q: How to view the commission report?**
A: Go to Dashboard → Reports → Other → Commission Report. This shows agent-wise commission earned based on assigned invoices.

---

# Receipts

## Definition
A payment receipt is a document issued by the seller to the buyer confirming that payment has been received. It is legal proof of a completed transaction — recording the amount paid, the payment method, and the date. Unlike an invoice which requests payment, a receipt confirms payment already made.

In SIM, receipts can only be generated from received payments. A receipt cannot be created without a corresponding payment entry.

Once the receipt is created you can:- Edit, Preview, Send, Print, Delete.

## When & Who

- When a customer makes a full payment against an invoice.
- When a partial payment is received and needs to be acknowledged.
- When advance payment is collected before an invoice is raised.
- When a single payment covers multiple invoices.

Who uses it:
- Accounts / Admin — Records the payment and generates the receipt.
- Salesperson — Collects payment in the field and issues a receipt.
- Customer — Receives the receipt as proof of payment.

## Navigation Path

To generate a receipt: Dashboard → Payments Section → Payments Received → Tap on a Payment → Make Receipt

To view all generated receipts: Side Menu → Receipts

## Key Information

- A receipt can only be generated from the Payments Received section. It is tied to an actual recorded payment.
- Receipts are stored and accessible at any time from the Receipts section in the side menu.
- A receipt can be shared with the customer directly from the app via WhatsApp, email, etc.
- A receipt can only be generated once the payment has been received.

## Key Concepts

- **Invoice vs. Receipt** — An invoice requests payment from the buyer at the time of sale. A receipt confirms payment has been received after payment is collected. They are two separate distinct documents.
- **Advance Payment Receipt** — When a customer pays before an invoice is created (e.g., a booking advance), a receipt can still be generated for that advance payment. The invoice is raised later when goods are delivered or the service is completed.
- **Receipt for Partial Payment** — If a customer pays ₹3,000 against an invoice of ₹5,000, a receipt is generated for the ₹3,000 received. The invoice remains partially unpaid. A second receipt can be generated when the remaining ₹2,000 is collected.

## Alternate Terms

- Receipt is also called: Payment Receipt, Receipt Voucher, Cash Receipt, Collection Entry, Customer Receipt, Money Received Entry
- Payments Received is also called: Collections, Incoming Payments, Payment Register
- Make Receipt is also called: Generate Receipt, Issue Receipt, Print Receipt

## FAQs

**Q: What is a payment receipt in SIM?**
A: A payment receipt is a document confirming that payment has been received. It records the amount paid, payment method, and date. It is legal proof that a transaction has been completed.

**Q: How to generate a receipt in SIM?**
A: Go to Dashboard → Payments Section → Payments Received → tap on a payment → tap Make Receipt.

**Q: Where can I find all generated receipts?**
A: Go to Side Menu → Receipts. All generated receipts are stored and accessible here.

**Q: What is the difference between an invoice and a receipt?**
A: An invoice requests payment from the buyer at the time of sale. A receipt confirms that payment has already been received. They are two separate documents used at different stages of a transaction.

**Q: Can I generate a receipt for an advance payment?**
A: Yes. A receipt can be generated for advance payment even before an invoice is created. The invoice is raised later when goods are delivered or service is completed.

**Q: Can I generate a receipt for a partial payment?**
A: Yes. A receipt is generated for the amount actually received. If the invoice is partially paid, the invoice remains partially unpaid and a second receipt can be generated when the remaining balance is collected.

**Q: Can I share a receipt with the customer from the app?**
A: Yes. Receipts can be shared directly from the app via WhatsApp, email, or other sharing options.

**Q: Could I get the receipt without payment?**
A: No, a receipt is generated only when a customer makes a full or partial payment. It serves as proof of payment.

**Q: Can I edit or preview receipts?**
A: Yes, you can edit or preview receipts, but only after a payment has been created. Once a payment is recorded, the receipt becomes available for preview and editing.

---

# Batch Upload

## Definition
Batch Upload (also called Bulk Upload) is a feature that allows importing multiple records — products, clients, or suppliers — into SIM all at once using an Excel or CSV file. It also supports updating existing records in bulk, such as updating prices for a large product list or refreshing client details.

Navigation: Settings → Batch Upload

## When & Who

- During initial app setup to migrate an existing product catalogue or client list.
- When migrating data from another billing system or spreadsheet.
- When adding a large number of new records (typically 100+ items) at once.
- When updating prices, rates, or details across many existing products or clients.

Who uses it:
- Business Owner — Initial data setup, periodic price updates.
- Accountant — Migrating financial records from a previous system.
- Data Entry Operator — Handling large-volume data imports.

## Workflow A: Creating New Records in Bulk

Used when adding products or clients that do not yet exist in SIM.

1. Go to Settings → Batch Upload → Create New Clients / Products
2. Download the template file (Excel format with required column headers)
3. The template can be sent to email or saved directly on the device
4. Fill in the data in the Excel file following the column headers exactly
5. Return to Settings → Batch Upload → Create New Clients / Products → Upload & Create
6. Select the filled file → Upload

## Workflow B: Updating Existing Records in Bulk

Used when modifying details of products or clients already in SIM.

1. Go to Settings → Batch Upload → Update Existing Clients / Products
2. Download the existing data file — this exports current records from the app into an Excel sheet
3. Edit the required fields in the downloaded file
4. Return to Settings → Batch Upload → Update Existing Clients / Products → Upload Existing
5. Select the edited file → Upload

## Template Column Reference

Common columns in the download template:
- Product Name / Client Name — Record name as it appears in the app
- Sale Rate — Selling price of the product
- Purchase Rate — Cost price / buy rate
- Tax Rate — GST or VAT percentage
- Opening Stock — Initial stock quantity (products only)
- Measurement Unit — Unit of quantity (pcs, kg, etc.)
- HSN Code — Product classification code for GST
- Email / Contact / Address — Client or supplier contact details

The column headers in the template must not be modified. Data must be entered under the exact headers provided.

## Key Concepts

- **Template-Based Import** — SIM uses a fixed template with predefined column headers to ensure data is imported correctly. Each column header maps to a specific field in the app. Modifying headers or using a different format will cause the import to fail or produce incorrect data.
- **Create New vs. Update Existing** — Create New adds records that do not yet exist in SIM. Update Existing modifies records already present. Do not use Create New to update existing records — it will create duplicate entries.

## Dependencies and Side Effects

What must exist before a batch upload works:
- The Products module must be set up before product uploads.
- The Clients module must be set up before client uploads.
- Any measurement units or product categories used in the file must already exist in the app.

What changes after a successful upload:
- Inventory — Opening stock quantities are applied immediately.
- Reports — New products and clients become part of sales, stock, and valuation reports.
- Invoice Creation — Newly uploaded products and clients are immediately available for selection in invoices.
- App Performance — Very large uploads (1000+ records) may temporarily slow down the app while processing.

## Alternate Terms

- Batch Upload is also called: Bulk Upload, Data Import, Mass Upload, Bulk Import, CSV Import, Excel Import
- Template File is also called: Import Template, Upload Format, Data Sheet
- Create New is also called: Add in Bulk, New Import, Fresh Upload
- Update Existing is also called: Bulk Edit, Mass Update, Data Refresh

## FAQs

**Q: What is Batch Upload in SIM?**
A: Batch Upload is a feature that allows importing multiple products, clients, or suppliers at once using an Excel or CSV file, instead of adding them one by one.

**Q: How to upload multiple products at once using Excel?**
A: Go to Settings → Batch Upload → Create New Clients / Products → download the template → fill in product details following the column headers → upload the file → confirm.

**Q: How to update existing products in bulk?**
A: Go to Settings → Batch Upload → Update Existing Clients / Products → download the existing data file → edit the required fields → upload the edited file.

**Q: Can I modify the column headers in the template file?**
A: No. The column headers must not be modified. Data must be entered exactly under the provided headers. Changing headers will cause the import to fail.

**Q: What happens if I use Create New to update an existing product?**
A: Using Create New on a record that already exists in SIM may create a duplicate entry. Use Update Existing for modifying existing records.

**Q: What happens to inventory after a batch upload?**
A: Opening stock quantities entered in the upload file are applied immediately to product inventory once the upload is completed.

**Q: Can I upload clients and suppliers using Batch Upload?**
A: Yes. Batch Upload supports uploading products, clients, and suppliers. Select the appropriate option (Clients / Suppliers) from the Batch Upload section.

---

# Payment Management

## Definition
Payment is a transaction used to record money against an existing invoice or purchase record. It reduces pending amounts or dues. A payment does not create a new transaction — it settles an existing one.

Two primary types of payments:

- **Payment Received** — Occurs when a customer pays for a sales invoice.
- **Payment Paid** — Occurs when the business pays a supplier for a purchase record.

## When & Who

- After creating an invoice and receiving payment from a customer.
- When clearing outstanding supplier purchase records.
- When partial or full payment is made against an invoice or purchase record.

Who is involved:
- Customers — Involved in Payment Received scenarios.
- Suppliers / Vendors — Involved in Payment Paid scenarios.

Note: Payment Mode Setting must be enabled to create payments via cash or bank accounts.

## Navigation Paths

**Flow 1 — Direct Marking**

1. Invoice / Purchase List → tap on the record
2. Open action menu → tap Mark as Received (for sales) or Mark as Paid (for purchases)
3. Select cash/bank account, date, and amount → Save

**Flow 2 — Via Edit Option**

1. Invoice / Purchase List → tap on the record
2. Open action menu → tap Edit
3. Scroll down to the Payment section → expand it → tap Full Paid Now button
4. Update the record

**Flow 3 — From Dashboard**

1. Dashboard → Side Menu (☰) → Payment section → Add New
2. Select customer (for sales) or supplier (for purchases)
3. Choose Payment against invoice or purchase
4. Check the checkbox for the relevant invoice or purchase record
5. Tap Next → Done

## Optional Payment Features

**1. Advance Payment**
- Advance payments can be created for clients or suppliers from the payment section.
- They can be adjusted against invoices later.
- Advance payments are only adjustable against invoices — they cannot be refunded.
- Advance payments appear in the Payment list only and are not shown on Sale/Purchase Invoices.

To create an advance payment: Payment → Add Payment → select Client / Supplier → select Lumpsum Amount → enter amount → Next

**2. Write Off (Sales Invoices Only)**
- The Write Off option is available exclusively for sales invoices to account for unrecoverable amounts.

Steps: Invoice List → tap on the invoice → action menu → Mark as Received → remove the amount from the amount field → check Write Off checkbox → Add

**3. Opening Balance Adjustment**
- Allows adjustment of opening balances against invoices or purchase records.

Steps: Invoice / Purchase List → tap on the record → action menu → Manage Advance to this Invoice (for sales) or Manage Advance to this Purchase (for purchases) → Opening balance adjustment screen appears → check the invoice/purchase checkbox → Done

**4. Partial Payments**
- Allows payments to be made in installments against an invoice or purchase record.

**5. Payment Allocation**
- Enables a single payment to be allocated across multiple invoices or purchase records.

## Dependent Modules

Payment functionality is integrated with:
- Sale Return and Purchase Return Refund — For processing refunds for returns.
- Other Income Payment — For handling payments for miscellaneous income.

## Alternate Terms

- Payment Received is also called: Receive Payment, Invoice Settlement, Collections, Accounts Receivable Entry
- Payment Paid is also called: Make Payment, Bill Payment, Disbursement, Accounts Payable Entry

## FAQs

**Q: What is Payment in SIM?**
A: Payment is a transaction that records money received from a customer or paid to a supplier against an existing invoice or purchase record. It reduces the pending amount without creating a new transaction.

**Q: How to record a payment received from a customer?**
A: Go to the Invoice List → tap on the invoice → action menu → Mark as Received → select account, date, and amount → Save.

**Q: How to record a payment made to a supplier?**
A: Go to the Purchase List → tap on the purchase record → action menu → Mark as Paid → select account, date, and amount → Save.

**Q: How to record payment directly from the dashboard?**
A: Dashboard → Side Menu (☰) → Payment section → Add New → select customer or supplier → choose Payment against invoice or purchase → check the relevant invoice → Next → Done.

**Q: What is an Advance Payment in SIM?**
A: An advance payment is a payment created before an invoice is raised. It is stored in the Payment list and can be adjusted against a future invoice. Advance payments cannot be refunded.

**Q: What is Write Off in SIM?**
A: Write Off is an option available for sales invoices to account for amounts that cannot be recovered. It is applied by removing the amount from the payment field and checking the Write Off checkbox when marking an invoice as received.

**Q: What is Payment Allocation?**
A: Payment Allocation enables a single payment to be distributed across multiple invoices or purchase records.

**Q: What is Opening Balance Adjustment?**
A: Opening Balance Adjustment allows the outstanding opening balance of a client or supplier to be applied against an invoice or purchase record to reduce the pending amount.

---

# Cash / Bank Fund Transfer

## Definition
Cash / Bank Fund Transfer is a feature to record movement of money between payment accounts — either transferring funds between cash and bank accounts, or recording standalone manual transactions (income, expenses, adjustments) against a single account.

Prerequisite: Payment Account feature must be enabled before this feature is available.

## When & Who
- When moving funds between cash and bank accounts.
- When recording cash inflows or outflows not linked to an invoice or purchase.
- Used by accountants, finance teams, and business owners.

## Navigation Path
Settings → Enable Payment Account Settings → Side Menu → Payments → New Cash/Bank Transfer or New Manual Transfer → Enter details (account, amount, date, notes) → Save

## Transaction Types

- **Cash / Bank Transfer** — Records the movement of funds from one account (e.g., Cash) to another (e.g., Bank). Both account balances are updated automatically.
- **Manual Transfer** — Records a standalone transaction against a single account — for example, a cash expense, a deposit, or a balance adjustment. Does not involve a second account.

## Interaction with Other Features

- Cash / Bank Report — Shows all fund transfer and manual transactions with edit and delete options.
- Payment Section — Displays all recorded transactions with edit and delete support.

## Alternate Terms

- Cash / Bank Fund Transfer is also called: Fund Transfer, Account Transfer, Internal Transfer, Balance Transfer, Cash Flow Transfer, Money Movement

## FAQs

**Q: What is Cash / Bank Fund Transfer in SIM?**
A: It is a feature to record movement of money between payment accounts. It supports transfers between cash and bank accounts, and also standalone manual transactions like expenses or deposits.

**Q: What is the difference between Cash/Bank Transfer and Manual Transfer?**
A: Cash/Bank Transfer records movement between two accounts (e.g., from Cash to Bank). Manual Transfer records a standalone transaction against a single account — such as an expense, deposit, or adjustment — without involving a second account.

**Q: What must be enabled before using Cash/Bank Fund Transfer?**
A: The Payment Account feature must be enabled first. Go to Settings → Enable / Disable Features → Payment Account → Enable.

**Q: How to create a Cash/Bank Transfer?**
A: Go to Side Menu → Payments → New Cash/Bank Transfer → enter account, amount, date, and notes → Save.

**Q: Where can I view all fund transfer records?**
A: All fund transfer and manual transactions are visible in the Cash / Bank Report and in the Payments section, both of which support editing and deletion.

---

# Thorough Syncing

## Definition
Thorough Syncing is an enhanced synchronization mechanism that ensures complete, accurate, and conflict-aware data consistency between local device storage and cloud storage. It goes beyond basic synchronization by performing a comprehensive data alignment.

Thorough Syncing differs from basic sync in the following ways:
- Syncs all modules — including invoices, clients, payments, settings, and reports. No data category is skipped.
- Performs deep comparison — conducts an in-depth analysis of data rather than simply overwriting with the latest version.
- Handles conflicts intelligently — identifies and resolves data conflicts to maintain data integrity.
- Guarantees data integrity — prevents data duplication or loss.

## When & Who

When it is used:
- First-time login on a new device — to populate the new device with all existing data.
- After reinstalling the app — to restore and synchronize all data post-reinstallation.
- When switching devices — to ensure seamless data transfer and consistency.
- After long offline usage — to reconcile changes made offline with cloud data.
- Before backup or restore operations — to ensure the most current data is used.

Who uses it:
- Business owners and freelancers — to ensure complete data accuracy and reliability.
- Multi-device users — for consistent data access across phones and tablets.
- Teams — to synchronize shared invoice data among team members.
- Accountants — requiring verified, up-to-date records for financial management.

## Navigation Path
Side Menu → Maintenance → Thorough Syncing → Start Syncing

Note: This process may take some time depending on the volume of data.

## Alternate Terms

- Thorough Syncing is also called: Full Sync, Deep Sync, Complete Sync, Smart Sync, Advanced Sync, Data Reconciliation Sync, Full Backup & Sync, Master Sync, Integrity Sync

## FAQs

**Q: What is Thorough Syncing in SIM?**
A: Thorough Syncing is an advanced sync that ensures complete and accurate data consistency between the device and the cloud. It compares all data deeply, handles conflicts, and prevents duplication or data loss.

**Q: How is Thorough Syncing different from regular sync?**
A: Regular sync does a basic data update. Thorough Syncing performs a deep comparison across all modules — invoices, clients, payments, settings, reports — resolves conflicts, and guarantees full data integrity.

**Q: How to start Thorough Syncing?**
A: Go to Side Menu → Maintenance → Thorough Syncing → Start Syncing.

**Q: When should I use Thorough Syncing?**
A: Use Thorough Syncing when logging in on a new device for the first time, after reinstalling the app, when switching devices, after long periods of offline usage, or before performing a backup or restore.

**Q: How long does Thorough Syncing take?**
A: The time depends on the volume of data. It may take some time to complete for large datasets.

**Q: Does Thorough Syncing prevent data loss?**
A: Yes. Thorough Syncing is designed to prevent data duplication and data loss by performing intelligent conflict resolution and a full data alignment between local and cloud storage.

---

# Purchase Return
A purchase return is created when goods purchased from a supplier are returned. The original purchase invoice is never deleted — it records that the purchase happened. A purchase return is created instead, which connects to the original purchase invoice, records what was returned, keeps the purchase record accurate, removes returned items from inventory, and adjusts the supplier balance accordingly.

## When and Who
- A purchase return is created when purchased goods need to be returned to the supplier, such as when items are damaged, defective, incorrect, expired, or excess quantity was received.

- A purchase return is usually created by the business that purchased the goods, typically through the purchasing department, store manager, warehouse staff, or accounts team.

## FAQs

**Q: Why should I not delete the original purchase invoice when goods are returned to the supplier?**
A: Deleting a purchase invoice misrepresents financial and inventory history. The original purchase happened and must remain in the records. A purchase return offsets the original purchase invoice without erasing it — this is standard accounting practice.

**Q: How to create Purchase Return?**
A: Dashboard >> Purchase Record >> Click on the Purchase >> Make Purchase Return >> Select the products that you want to return >> save