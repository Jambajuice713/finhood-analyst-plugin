---
name: comps-analysis
description: Trading comparables — peer set construction, operating metrics, valuation multiples on consistent definitions, and statistical benchmarking with outliers flagged. Use for "comps", "peer comparison", "how does X trade versus peers", or relative valuation. Produces the relative half of §5 of the research report standard.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Comps Analysis

Relative valuation. The research standard requires more than one valuation model,
and this is the counterweight to the DCF: **the DCF assumes your assumptions are
right; comps assume the market is right about the peers.** Both are wrong in
different directions, which is why you run both.

---

## Step 1 — The peer set is the analysis

A comps table is only as good as its peer set, and the peer set is where the
judgement lives. Selection criteria, applied and stated:

- **Same business model**, not merely the same sector. A software company selling
  perpetual licences is not comparable to one selling subscriptions, whatever the
  GICS code says.
- **Comparable growth and margin profile.** A 40%-grower and a 4%-grower do not
  trade on the same multiple and should not be averaged together.
- **Comparable capital intensity** — it drives the difference between EV/EBITDA
  and EV/EBIT and free cash flow conversion.
- **Comparable geography and regulatory regime** where either is material.

**Write down who you excluded and why.** An unexplained peer set is an
unfalsifiable one, and peer sets are the easiest place in equity research to
smuggle in a conclusion.

## Step 2 — One definition per metric, stated at the top

The single most common defect in comps work. Before any number goes in the table,
fix and publish:

| Metric | Definition to fix |
|---|---|
| **EV** | Market cap + total debt − cash. Include or exclude: leases, minorities, pensions, preferred? Pick one, apply to all. |
| **EBITDA** | Reported, adjusted, or your own recalculation? If adjusted, adjusted by whom — the company? |
| **Earnings** | GAAP or adjusted. If adjusted, list what is excluded. |
| **Period** | LTM, NTM, or a fiscal year. Fiscal-year-ends differ across peers — calendarise, or say you did not. |
| **Share count** | Basic or diluted, and the treatment of unvested equity. |

**A table built on mixed definitions is worse than no table**, because it looks
rigorous. If a peer's figure cannot be put on the fixed definition, mark it
`[UNSOURCED]` and leave the cell empty rather than substituting the company's own
version.

## Step 3 — Operating metrics before multiples

Multiples without operating context are meaningless — a 30x multiple is
information only alongside the growth and margins behind it.

| Company | Revenue growth | Gross margin | EBITDA margin | FCF conversion | ROIC | Net leverage |
|---|---|---|---|---|---|---|

## Step 4 — The multiples

Per `methodology/research-report-standard.md` §5, relative valuation can be based
on price/sales, price/earnings, price/cash flow and price/book. Choose by what the
business actually is:

| Multiple | Appropriate when | Breaks when |
|---|---|---|
| EV/Sales | Pre-profitability, or margins not yet at steady state | Margin structures differ across the set |
| EV/EBITDA | Capital structures differ; comparing operating performance | Capital intensity differs materially |
| EV/EBIT | Capital intensity differs | D&A policies differ |
| P/E | Mature, stable, similar leverage | Leverage or tax rates differ across peers |
| P/B | Financials, asset-heavy balance sheets | Intangible-heavy businesses |
| FCF yield | Cash generative, steady state | Capex is lumpy or currently elevated |

## Step 5 — Benchmark statistically, and flag outliers

- Report **median** as the central tendency, not the mean. The mean is dragged by
  a single high-multiple name and the peer set is small.
- Report the range and the interquartile spread. A tight set and a dispersed set
  support very different conclusions.
- **Flag every outlier and explain it.** An outlier is either a data error, a
  definitional mismatch, or the most interesting name in the table. All three
  outcomes require investigation; none permits quiet exclusion.

## Step 6 — Position the subject

Where does the subject trade against the set, and **is the difference explained by
fundamentals?**

The useful output is not "it trades at a 20% discount". It is:

> "It trades at a 20% discount to the peer median on EV/EBITDA. Roughly half is
> explained by 300bp lower EBITDA margin; the rest is unexplained by the operating
> metrics in the table, and the candidate explanations are [X] and [Y]."

A discount that is fully explained by fundamentals is not an opportunity. It is
correct pricing, and saying so is a finding.

## Guardrails

- **Definitions before numbers.** Fix them, publish them, apply them uniformly.
- **`[UNSOURCED]` over filled-in.** An empty cell is honest; an inferred one
  contaminates the median.
- **The peer set is not the market's opinion of fair value.** If the whole sector
  is expensive, comps will say the subject is fine. Say so — that is what the DCF
  is for.
- **Any multiple you did not compute carries someone else's definitions**, which
  may not match yours. Do not mix computed and retrieved multiples in one column
  without labelling. `policy/data-integrity.md` §1.

## Building the set by hand

`research.market_data` is not supplied by default (`bindings/research.md` §5), so
the normal path is to build the peer set from filings plus `market.quote`:
market cap from price × diluted shares, net debt and the operating metrics from
the latest filing, multiples computed by you on the definitions fixed in §2.

Slower, narrower, and entirely legitimate — **a hand-built five-name peer set on
consistent definitions beats a twenty-name screen on inconsistent ones.** State
which path was taken.
