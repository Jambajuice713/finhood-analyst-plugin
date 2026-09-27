# Research report standard

The structure every single-name output in this package follows. Taken from CFA
Institute, *Equity Research Report Essentials* (September 2020), which sets out the
elements essential to a thorough research report.

Sections scale with the depth of the work — a morning note carries §1, §4 and §7
compressed; a full initiation carries all of them. **The order does not change**,
and no section is dropped silently: an omitted section is marked as omitted.

---

## 1. Basic information

The identifying frame, before any argument:

- Ticker, primary exchange.
- Primary sector and industry.
- **The investment recommendation.**
- Current price, market capitalisation, and the **target price**.

Two items the guide singles out and that most notes skip:

- **Liquidity** — the degree to which the stock can be bought and sold without
  affecting the price. The guide notes that periods of financial stress affect a
  security's liquidity; a name that trades comfortably today may not when it
  matters.
- **Float** — shares publicly owned and available for trading, generally
  excluding restricted shares and insider holdings. Float can be materially
  smaller than market cap. **A relatively small float deserves mention**, and it
  is good practice to identify the major shareholders.

## 2. Business description

What the company sells and how it makes money. The guide asks for a clear
understanding of the company's **economics**, including the key drivers of
revenues and expenses — not a product catalogue.

Sourced from the company itself, its regulatory filings, and industry publications.

## 3. Industry overview and competitive positioning

Industry dynamics plus a competitive analysis. The guide points to **Porter's Five
Forces** as an effective framework for examining the health and competitive
intensity of an industry, and names production capacity levels, pricing,
distribution, and stability of market share as important considerations.

A peer group is developed here — it is the input to comps in §5.

On competitive advantage, the guide is explicit that there are different paths to
success: **strength of brand, cost leadership, and access to protected technology
or resources.** It quotes Buffett's framing of advantage as an economic *moat* —
"economic castles protected by unbreachable moats."

Name the moat, or say there isn't one. "Strong competitive position" is not a
finding.

## 4. Investment summary

The section that gets read. Brief description, significant recent developments,
earnings forecast, valuation summary, recommended action.

The guide's demand for this section is the standard the package holds itself to:
where a purchase or sale is being advised, there must be **a clear and concise
explanation as to why the security is deemed to be mispriced** — specifically:

> *What is the market currently not properly discounting in the stock's price, and
> what will prompt the market to re-price the security?*

Two distinct questions, and both need an answer:

1. **The variant view.** What do you believe that the price does not reflect?
2. **The catalyst.** What makes the market change its mind, and roughly when?

A thesis with a variant view and no catalyst is a position with no time horizon.
A thesis with a catalyst and no variant view is momentum with a story.

## 5. Valuation

The guide requires **more than one valuation model**, because model outputs vary.

- **Absolute** — intrinsic value, generally discounted cash flow models. See
  `skills/dcf-model/`.
- **Relative** — value relative to another stock, based on metrics including
  price/sales, price/earnings, price/cash flow, price/book. See
  `skills/comps-analysis/`.

State the assumption the output is most sensitive to, and what the value becomes
if that assumption is wrong. A single point estimate with no sensitivity is not a
valuation.

## 6. Financial analysis

Historical performance plus a forecast. The guide's framing of this section is a
warning, and it should be read as one:

> *Financial results are commonly manipulated to portray firms in the most
> favorable light. It is the responsibility of the analyst to understand the
> underlying financial reality.*

Which makes **careful reading of the footnotes an essential part of any
examination of earnings quality.** The items it names as capable of distorting
results:

- Nonrecurring events
- Off-balance-sheet financing
- Income and reserve recognition
- Depreciation policies

On forecasting, a caution the package takes seriously: analysts should be
**especially careful about extrapolating past trends into the future**, most of
all for cyclical firms — *projecting forward from the top or bottom of a business
cycle is a common mistake.*

Industry-specific ratios are informative where they exist: the guide's examples
are proven reserves/share for oil companies, revenue/subscriber for cable and
wireless, revenue/available room for hotels.

## 7. Investment risks

Potential negative industry and company developments that could pose a risk to the
thesis: operational, financial, regulatory, legal.

The guide notes that although companies are obligated to discuss risks in their
disclosures, **risks are often subjective and hard to quantify** — the threat of a
competing technology is its example — and that making these determinations is the
analyst's job, not the issuer's.

Two disclosures it says should be **automatic red flags**:

- A **qualified opinion** from the auditors.
- **Material weakness in internal control over financial reporting.**

This package adds one requirement on top of the guide: each material risk carries
the **observable condition that would confirm it is materialising**. Per
`policy/data-integrity.md` §7, an unfalsifiable thesis is not a thesis.

## 8. ESG

How the company manages environmental, social and governance relationships, where
these have a lasting impact on short- and long-term prospects.

- **Environmental** — climate change and carbon emissions, air and water
  pollution, energy efficiency, waste management.
- **Social** — community relations, human rights, labour standards, customer
  satisfaction, employee engagement.
- **Governance** — board composition, audit committee structure, executive
  compensation, succession planning, leadership experience, bribery and
  corruption policies.

Include what is material to the thesis. Governance in particular is not a
compliance box: board composition and audit committee structure connect directly
to the earnings-quality work in §6.

---

## Professional standards

The guide closes by pointing to two CFA Institute resources that codify the
ethical standards and best practices that are the responsibility of all investment
professionals:

- CFA Institute Code of Ethics and Standards of Professional Conduct
- Best Practice Guidelines Governing Analyst/Corporate Issuer Relations

Relevant to this package in three concrete ways:

1. **Reasonable basis.** A recommendation requires diligence and a reasonable,
   adequate basis. `[UNSOURCED]` figures do not constitute one.
2. **Distinguishing fact from opinion.** Enforced mechanically by the marking
   rules in `policy/data-integrity.md` §1.
3. **Independence.** Sell-side targets and issuer materials are inputs, never
   conclusions adopted wholesale.
