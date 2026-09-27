---
name: dcf-model
description: Discounted cash flow valuation — projections, WACC, terminal value, and sensitivity analysis, producing an intrinsic value with its fragility stated. Use for "value this company", "build a DCF", "what is it worth", or "intrinsic value". Produces the absolute half of §5 of the research report standard.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# DCF Model

Absolute valuation. Per `methodology/research-report-standard.md` §5, absolute
models derive intrinsic value and generally take the form of discounted cash flow
models — and the standard requires that **more than one model be used**, so this
output always ships alongside `comps-analysis`.

**What a DCF actually is:** a structured way to state what you believe about a
business, expressed as a number. Its value is in the assumptions, not the output.
A DCF presented as a precise answer has been misunderstood by whoever presented it.

---

## Step 1 — Gather before you build

Filings first: the last three years of financials, the segment detail, the capex
history, the share count and its dilution path. Open this skill only once you have
them — a template opened first gets filled with plausible numbers, and the model
becomes an exercise in cell completion.

## Step 2 — Build free cash flow from drivers

```
Revenue
− Operating costs
= EBIT
− Cash taxes on EBIT
+ D&A
− Capex
− Δ Working capital
= Free cash flow to the firm
```

**Build revenue from mechanisms, not from a growth rate.** Volume × price,
customers × ARPU, capacity × utilisation × price. A single growth rate applied to
a total is an assumption wearing a projection's clothing, and it hides exactly the
question you are trying to answer.

Internal consistency, which is where most DCFs quietly fail:

- Growth requires **reinvestment**. Revenue rising with flat capex and flat
  working capital is a model that has assumed a free lunch.
- Margin expansion requires a **stated mechanism** — scale, mix, pricing, or a
  named cost action. "Margins improve to 24%" with no mechanism is a wish.
- D&A must be consistent with the capex history and the asset base.

## Step 3 — Discount rate

WACC, with every component sourced and dated:

- **Risk-free rate** — current, cited, with its date. A stale rate silently
  revalues the whole model.
- **Equity risk premium** — stated, with its source.
- **Beta** — with the estimation window disclosed. A beta from a short window is
  noise; if that is what you have, say so and consider a peer-set beta instead.
- **Cost of debt** — from actual borrowing costs where disclosed, not a spread you
  chose.
- **Capital structure weights** — market values, not book.

Sanity check: does the resulting WACC make sense against the company's actual cost
of capital, and against the peer set? An 8% WACC on a highly leveraged cyclical is
a defect, however cleanly the CAPM produced it.

## Step 4 — Terminal value

Where most of the value is, and therefore where most of the error is. Say what
share of total value it represents — **if terminal value is more than about 75% of
the total, the model is a statement about the terminal assumption** and should be
presented that way.

Two methods, and running both is the check:

- **Perpetuity growth**: `TV = FCF_n × (1+g) / (WACC − g)`. The constraint is not
  negotiable: **g cannot exceed long-run nominal GDP growth**. A company cannot
  outgrow the economy in perpetuity. A `g` above ~3% for a US company needs an
  argument, and usually does not have one.
- **Exit multiple**: applied to terminal-year EBITDA. Sanity-check by backing out
  the implied `g` and asking whether you would have defended it directly.

When the two methods diverge materially, that gap is a finding about the fragility
of the valuation, and it belongs in the note.

## Step 5 — Bridge to equity value

```
Enterprise value
− Net debt
− Minority interests
− Pension deficit and other debt-like items
+ Non-operating assets
= Equity value
÷ Diluted shares (with the dilution path treated explicitly)
= Value per share
```

Use the same definitional conventions as `skills/comps-analysis/` §2. A DCF and a
comps table on different EV definitions cannot be compared, which defeats the
purpose of running both.

## Step 6 — Sensitivity

**Non-optional.** A point estimate with no sensitivity does not leave this skill.

- A grid on the two assumptions the value is most sensitive to — usually WACC and
  terminal growth, but check rather than assume.
- **Identify the single most sensitive assumption** and state what value it
  implies at the current market price.

That last calculation is often the most useful output of the entire model:

> "At USD 118, the market is implying terminal growth of 1.4% and a steady-state
> EBIT margin of 19%. The margin assumption looks conservative against a five-year
> average of 22%; the growth assumption looks reasonable."

This reframes the exercise from *predicting the value* to *interrogating the
price* — a far more defensible activity, and one where being roughly right is
worth something.

## Step 7 — Audit

`skills/audit-xls/` before it ships. Non-negotiable checks: no hardcodes inside
formula ranges, no unintended circularity, signs consistent, terminal-year cash
flow a sensible steady state rather than a peak or trough.

## Guardrails

- **Every assumption labelled `[assumption]` and defended in one line.**
  `policy/data-integrity.md` §1.
- **`[UNSOURCED]` over invented.** Visible gaps are usable; invented inputs are a
  liability the reader cannot detect.
- **Never solve backwards to a target price.** If the assumptions that produce the
  target are ones you would not defend directly, the finding is "the price implies
  X, which requires Y" — not a target.
- **Do not extrapolate a cycle.** `methodology/research-report-standard.md` §6.
  If the base year is a cycle extreme, normalise it or state that you did not.
- **Precision discipline.** A DCF is accurate to roughly the nearest 10%. Report
  a range, or a value with the range stated. Two decimal places on a share-price
  target is false precision and undermines everything around it.
