# AI Cash Flow Signals — Data Dictionary

**Version:** 0.1
**Status:** Initial Corporate Cash Flow Layer

---

## 1. Purpose

This Data Dictionary defines the initial signals used in the **AI Cash Flow Signals** project.

The project observes a simple question:

> **Can cash continue flowing through the AI economy at its current pace?**

The objective is not to predict an AI bubble, market crash, or stock price.

The objective is to observe:

* where cash is generated,
* where cash is invested,
* how much cash remains after investment,
* when external funding becomes more important,
* and how cash moves from AI infrastructure buyers to suppliers.

---

## 2. Initial Observation Universe

### Hyperscalers

| Company        | Ticker | Role                    |
| -------------- | ------ | ----------------------- |
| Microsoft      | MSFT   | AI infrastructure buyer |
| Alphabet       | GOOGL  | AI infrastructure buyer |
| Amazon         | AMZN   | AI infrastructure buyer |
| Meta Platforms | META   | AI infrastructure buyer |

### Supplier

| Company  | Ticker | Role                       |
| -------- | ------ | -------------------------- |
| Broadcom | AVGO   | AI infrastructure supplier |

The observation universe may be expanded later.

---

## 3. Core Cash Flow Signals

### 3.1 Operating Cash Flow

**Definition:**
Cash generated from a company's core operating activities.

**Purpose:**
Measures the internal cash-generating capacity available to fund investment and other corporate activities.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Company cash flow statement / investor relations materials.

---

### 3.2 Capital Expenditure (CAPEX)

**Definition:**
Cash spent on property, plant, equipment, data centers, servers, infrastructure, and other long-term assets.

**Purpose:**
Measures the amount of cash being reinvested into infrastructure and productive capacity.

For hyperscalers, this is one of the primary signals for observing the scale of AI infrastructure investment.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Company cash flow statement / investor relations materials.

**Important Note:**
Reported CAPEX does not necessarily represent AI investment alone. Company-specific disclosures must be used where available to distinguish AI-related investment from total CAPEX.

---

### 3.3 Free Cash Flow (FCF)

**Definition:**
Cash remaining after capital expenditure.

**Base Calculation:**

Operating Cash Flow
− Capital Expenditure
= Free Cash Flow

**Purpose:**
Measures how much internally generated cash remains after investment.

A decline in FCF does not by itself indicate financial stress. It becomes more informative when observed together with CAPEX growth, cash balances, and external financing.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Calculated from company financial statements or company-reported FCF where definitions are consistent.

---

### 3.4 CAPEX / Operating Cash Flow

**Definition:**
The proportion of operating cash flow consumed by capital expenditure.

**Calculation:**

CAPEX / Operating Cash Flow × 100

**Purpose:**
Measures how much of internally generated operating cash is being absorbed by investment.

A rising ratio indicates that investment is consuming a larger share of internally generated cash.

**Unit:**
Percentage.

**Frequency:**
Quarterly.

**Primary Source:**
Calculated.

---

### 3.5 Cash & Cash Equivalents

**Definition:**
Cash and highly liquid short-term assets available to the company.

**Purpose:**
Measures the company's immediate liquidity buffer.

This signal helps distinguish between:

* declining FCF that can still be absorbed internally, and
* declining FCF that may require additional external financing.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Company balance sheet.

---

### 3.6 Total Debt

**Definition:**
Interest-bearing short-term and long-term borrowings.

**Purpose:**
Measures the company's use of external debt financing.

The signal becomes particularly important when observed together with FCF and CAPEX.

A possible transition to observe is:

FCF pressure
→ increased borrowing
→ higher debt dependence

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Company balance sheet / financial statements.

---

### 3.7 Interest Expense

**Definition:**
Interest cost associated with outstanding debt and other interest-bearing obligations.

**Purpose:**
Measures the cash and earnings burden created by external financing.

This becomes increasingly relevant if AI infrastructure investment requires greater reliance on debt markets.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Company income statement / financial statements.

---

## 4. Supplier Signals — Broadcom

Broadcom is initially included as a supplier-side observation point.

The purpose is not simply to track Broadcom as an AI-related company.

Broadcom provides an observation point for determining whether hyperscaler infrastructure spending is being transmitted into supplier revenue and cash generation.

---

### 4.1 Broadcom AI Revenue

**Definition:**
Revenue identified by Broadcom as related to AI semiconductor or AI infrastructure demand, based on company disclosures.

**Purpose:**
Observes whether hyperscaler AI infrastructure investment continues to flow into the supplier layer.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Broadcom earnings releases, earnings calls, and investor relations materials.

**Important Note:**
The company's definition and disclosure of AI revenue may change over time. The exact reported definition should therefore be recorded for each observation period.

---

### 4.2 Broadcom Free Cash Flow

**Definition:**
Free cash flow generated by Broadcom.

**Purpose:**
Observes whether AI-related revenue growth ultimately translates into cash generation at the supplier level.

**Unit:**
USD million or USD billion.

**Frequency:**
Quarterly.

**Primary Source:**
Broadcom financial statements / investor relations materials.

---

## 5. Initial Cash Flow Observation Chain

The initial observation framework is:

**Hyperscaler Operating Cash Flow**

↓

**Hyperscaler CAPEX**

↓

**Hyperscaler Free Cash Flow**

↓

**Cash Balance / External Funding**

and simultaneously:

**Hyperscaler CAPEX**

↓

**AI Infrastructure Demand**

↓

**Broadcom AI Revenue**

↓

**Broadcom Cash Flow**

The project will observe whether changes at one point in this chain begin to propagate to another.

---

## 6. Signals Reserved for Later Layers

The following indicators are relevant but are **not part of the initial corporate cash flow layer**:

* Corporate bond issuance
* New issue bond spreads
* Bond order-book coverage
* US Treasury 10-year yield
* US Treasury 30-year yield
* Treasury bill issuance
* SOFR
* Federal Funds Rate
* Bank reserves
* Federal Reserve Treasury purchases

These indicators will be added only after the corporate cash flow layer has been established.

Their purpose will be to observe whether corporate cash-flow pressure begins to propagate into funding markets and system liquidity.

---

## 7. Observation Principle

No individual signal should be interpreted as proof of financial stress.

The project focuses on **sequences of change**.

For example:

Operating Cash Flow stable
→ CAPEX rises
→ FCF declines
→ Cash balance declines
→ Debt issuance increases
→ Funding cost rises

would represent a different condition from:

Operating Cash Flow rises
→ CAPEX rises
→ FCF remains strong
→ Cash balance remains stable

The objective is therefore not to classify individual numbers as good or bad.

The objective is to observe **where the constraint moves next**.

---

## 8. Current Version

**Version 0.1**

Initial signals:

* Operating Cash Flow
* CAPEX
* Free Cash Flow
* CAPEX / Operating Cash Flow
* Cash & Cash Equivalents
* Total Debt
* Interest Expense
* Broadcom AI Revenue
* Broadcom Free Cash Flow

Next stage:

**Define the exact source and historical data range for each company and signal before building the dataset.**
