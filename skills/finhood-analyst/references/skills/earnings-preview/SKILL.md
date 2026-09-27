---
name: earnings-preview
description: "Pre-results setup on a name under coverage — what to watch, the bull/bear frame, what the market expects, and what would count as a surprise. Use before a company reports: \"earnings preview\", \"what to watch for X\", \"pre-earnings\", or \"X reports Thursday\"."
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Earnings Preview

Written before the print. Its value is that it commits you to what matters
**before** you know the answer — which is the only way to tell afterwards whether
you understood the business or narrated the outcome.

---

## Step 1 — Establish the setup

- **Date and time** of the report, and whether it is before or after the market.
- **The position**: size, cost basis, weight. `portfolio.positions`. A preview on
  a 15% position deserves more work than one on a 2% position.
- **The prior view**: `state.read`. What did we say last quarter would matter?
- **What is expected**: consensus if `research.market_data` is available;
  otherwise the company's own guidance, labelled as such.
- **Positioning**: has the stock run into the print, or sold off? The setup
  determines the reaction function as much as the result does.

## Step 2 — Name what matters, in advance

Three to five metrics, ranked by how much they move the thesis. For each:

| Element | Content |
|---|---|
| The metric | Specific and reportable — not "growth" but "net revenue retention" |
| Expectation | The number, and its source |
| Why it matters | The mechanism connecting it to value |
| Threshold | The level at which the thesis is confirmed or damaged |

**Ranked by thesis impact, not by prominence in the release.** The headline number
is usually the least informative thing in the report, because it is what everyone
else is also watching and therefore what is already priced.

## Step 3 — The bull/bear frame

Both cases, stated before the result, with the specific evidence each would need:

- **Bull:** what has to appear in this print for the thesis to accelerate?
- **Bear:** what would appear if the thesis is quietly failing?
- **Base:** the most likely outcome, and why it probably does not change much.

Write these so that after the print, a reader can check which one happened without
you getting to reinterpret them.

## Step 4 — What would be a genuine surprise

The most useful section, and the hardest.

Not "revenue above consensus" — that is a small surprise the market handles in an
hour. A genuine surprise is something that **changes the structure of the
forecast**: a margin inflection with a stated mechanism, a guidance cut with a
new reason, a disclosure change, a segment reclassification, a management
departure.

If you cannot name something that would genuinely surprise you, you do not
understand the business well enough to have a position sized where it is.

## Step 5 — Pre-commit the reaction

State in advance what each outcome would mean for the position:

> "If NRR comes in below 105%, the expansion assumption in the model is wrong and
> the position should be reviewed for trimming, regardless of the headline."

**This is the point of the whole skill.** Deciding after the print, with the price
moving, is how loss aversion and confirmation bias get their opening
(`methodology/risk-measures.md` §8). A pre-committed reaction function is the
cheapest available defence.

It is a **stated intention, not an instruction to trade.** `policy/execution.md`
still applies: the agent proposes, the user decides, and nothing executes on a
schedule.

## Guardrails

- **Do not predict the print.** The output is a framework for reading it, not a
  forecast of it. Forecasting the number is a low-value activity with a public
  scoreboard.
- **Consensus is other people's estimates.** Cite it as such. Under a binding
  without `research.market_data`, it is unavailable — say so and use guidance.
- **Watch for the metric that quietly disappeared.** A company that stops
  disclosing something it used to volunteer has told you about the trend in it.
  Check the prior release before writing the preview.
- **Write state.** The preview is what `earnings-analysis` reads afterwards to
  judge whether the right things were being watched.
