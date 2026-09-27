---
name: portfolio-review
description: Full review of the portfolio — composition, performance, risk, concentration, and a per-position verdict. Use for "review my portfolio", "how am I doing", "is this too concentrated", after a risk-limit breach, or on any periodic review. Produces the analysis that trade proposals are built on.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Portfolio Review

The core skill of this package. Everything else supports it.

A review answers four questions in order, and each depends on the one before it:
**What do I own? How has it done? What risk am I carrying? What should change?**

---

## Step 1 — Load the book

```
state.read("portfolio-snapshot")   # baseline; may be absent
market.clock                       # live or last close
portfolio.balance                  # cash is part of the portfolio
portfolio.positions                # holdings
market.quote  (per position)       # current marks
portfolio.history                  # value series
portfolio.transactions             # REQUIRED before any return figure
portfolio.dividends                # income
```

**Empty portfolio path.** If positions are empty, stop the standard flow. Report
cash available, note that there is no performance or risk to analyse, and use the
space to surface the open IPS questions in `policy/risk-limits.md` §5. That is the
most valuable output at this stage, and it is short.

**Unknown profile path.** Report observed concentration; do not label breaches or
provide personal sizing until relevant limits are supplied. Example thresholds
require explicit selection of an illustrative exercise.

**No baseline path.** If `state.read` returns nothing, every comparative statement
is unavailable. Say so once, produce the point-in-time review, and optionally export a private
snapshot if storage is available.

## Step 2 — Composition

A table, and then the observations the table does not make on its own:

| Symbol | Shares | Price | Market value | Weight | Cost basis | Unrealized P&L | % of P&L |
|---|---|---|---|---|---|---|---|

Weights on **total portfolio value including cash**. Then state:

- Cash as a percentage. This is an allocation decision whether or not it was made
  deliberately, and it should be named as one.
- The **P&L concentration**, which is usually more revealing than the weight
  concentration: if one position is 70% of the gain, the portfolio's result is
  that position's result and the rest is noise.

## Step 3 — Performance

`methodology/returns-and-performance.md` is binding. Follow it exactly.

**The gate, first:** did external cash flows occur in the period?

- **No flows, or flows ruled out** → compute TWR from the value series.
- **Flows present** → break the period at each flow, compute subperiod HPRs, link
  them only if valuations at each flow are available. If those valuations are
  missing, exact TWR is unavailable: label a supported approximation or report
  value change. `R_TW = (1+r₁)(1+r₂)…(1+rₙ) − 1`.
- **Flows possible but not observable** → report a **value change**, labelled as
  such. Not a return. This is not a formatting nicety; an unlabelled figure will
  be read as a return and will be wrong by the size of the deposit.

Then, where the data supports it:

- **TWR** — the portfolio's result.
- **MWR** — the user's result, given his contribution timing.
- **When both exist and differ materially, report both and explain the gap.** The
  difference is a fact about when he added money, and it is often the most useful
  line in the review. If he consistently adds after drawdowns, MWR above TWR is
  evidence that his timing is helping — worth knowing, and worth stating.
- Multi-period aggregation uses the **geometric** mean. The arithmetic mean is
  biased upward, severely so when returns mix signs.
- Decompose into **price return and income** where `portfolio.dividends` allows.

**The default mapping supplies no benchmark or risk-free return series**
(`bindings/zesty.md`). Beta, Jensen alpha, tracking error and market comparison
require independently sourced inputs. Sharpe does not need a market index but
does need matched risk-free returns and a valid portfolio return series. State that
once, plainly, and do not fill the gap with a remembered index level.

## Step 4 — Risk

Four passes, in this order:

**1. Concentration by weight** against the user’s agreed limits, if supplied.
Otherwise report weights without breach labels; numerical example thresholds
apply only if the user explicitly selected an illustrative exercise.

**2. Concentration by driver.** The pass that matters more and gets skipped.
Portfolio variance carries the covariance term, so **correlation, not individual
volatility, determines whether the book is actually diversified**
(`methodology/risk-measures.md` §4). Two 12% positions in the same sector with
ρ ≈ 0.9 are closer to one 24% position than to two bets.

Where correlation is not computable under the active binding, group by sector,
end-market, and shared driver — rates, a single large customer, one regulatory
regime, one commodity — and **say the grouping is a proxy**.

**3. Downside.** Standard deviation of a valid cash-flow-adjusted return series,
and then **target downside deviation** against the user's minimum acceptable return
(`methodology/risk-measures.md` §2, denominator `n − 1` over the full sample). Use
0% and label the target until the MAR is set.

**4. Drawdown.** Use a unitized or cash-flow-adjusted wealth series and disclose
the observed window. Raw account values distorted by flows are not performance
drawdowns. Follow `policy/risk-limits.md` §3.

## Step 5 — Per-position verdict

For each holding, in three or four lines:

1. **What it is** and why it is in the book, from `state` if a prior view exists.
2. **What has happened** since — price, and the reason if findable. `[UNSOURCED]`
   if not.
3. **The endowment test**, run explicitly: *if this were not already in the book,
   would the analysis support opening it today, at this price and this size?*
   `methodology/risk-measures.md` §8.
4. **Verdict** — hold, trim, add, exit, or **needs work**, with what would decide
   it. "Needs work" is a legitimate answer and better than a guess; route it to
   the relevant agent.

The endowment test is the point of this step. It is the one question that
reliably separates a position that is still working from a position that is still
there.

## Step 6 — Actions

Ranked, each with: the action, the size, the post-trade weight, the reason, and
the condition that would change the answer.

**Text proposals only.** Do not preview, submit, confirm or cancel orders.
Read-only order history is allowed when relevant; see `policy/execution.md`.

## Step 7 — Write state

When private persistence is available, write `schemas/portfolio-snapshot.json`.
Otherwise disclose that no baseline was saved and offer an export if supported.

---

## Output shape

Written in Spanish (`manifest.yaml` → `language`), terminology in English.

```
1. Resumen           — 3–5 líneas. Qué pasó, qué importa, qué hacer.
2. Composición       — tabla + concentración de peso y de P&L
3. Performance       — método declarado, TWR/MWR, descomposición
4. Riesgo            — concentración, correlación/proxy, downside, drawdown
5. Posiciones        — veredicto por nombre, con el endowment test
6. Acciones          — propuestas rankeadas, sin ejecutar
7. Supuestos y vacíos — qué falta, qué está [UNSOURCED], qué límites son provisionales
```

Section 7 is not boilerplate. It is where the review earns trust: a reader who
knows exactly what the analysis could not see can judge the rest of it.

## Failure modes

| Mistake | Why it is wrong |
|---|---|
| Value change reported as return | Off by the size of any deposit |
| Weights on the equity sleeve only | Overstates position weights when cash is positive; does not measure total-portfolio performance |
| Arithmetic mean across periods | Biased upward; severely when returns mix signs |
| Concentration by weight alone | Misses correlated exposure, which is the risk that actually shows up |
| Sharpe quoted in isolation | Uninformative without a comparison; and it misranks when excess return is negative |
| Endowment test skipped on favourites | Precisely the positions where it matters |
| No private snapshot available | State that the next session will need a baseline |
