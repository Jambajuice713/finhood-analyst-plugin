---
name: earnings-analysis
description: Post-results analysis on a name under coverage — beat/miss against guidance and consensus, what drove it, earnings quality, revised estimates, and whether the thesis survives. Use for "earnings update", "quarterly results", "what did the quarter say", or any post-print review of a held position.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Earnings Analysis

Answers one question: **did this quarter change what the company is worth?**

Most quarters do not. A note that treats every print as thesis-changing is noise,
and a note that treats none of them that way misses the one that matters. The work
is telling them apart.

---

## Step 1 — Load the prior view

`state.read` for the last note on this name, `portfolio.positions` for size and
cost basis.

Without the prior view you cannot report what **changed**, and change is the
entire content of an earnings note. If no prior view exists, say so — this is an
initiation, not an update, and the framing differs.

## Step 2 — Primary sources first

The release and the filing, then the transcript, then commentary.
`policy/data-integrity.md` §2. Reading the coverage before the release means
inheriting someone else's framing of what mattered.

## Step 3 — Beat or miss against *what*

Two different comparisons that frequently disagree:

- **Against consensus** — requires `research.market_data`. Measures the surprise
  relative to expectations.
- **Against guidance** — from the company's own prior disclosures. Measures
  management's forecasting, and their credibility.

**Under a binding without `research.market_data`, consensus is unavailable and
guidance is the honest comparison.** Say which you used. Never imply consensus you
did not retrieve.

Report the beat/miss on revenue, margin, and EPS separately. A revenue miss with
an EPS beat is a cost story, and the two have different implications for value.

## Step 4 — What actually drove it

Decompose. "Revenue grew 18%" is not analysis until it becomes:

- **Volume vs price vs mix.**
- **Organic vs acquired.**
- **FX contribution**, separated out.
- **One-time items**, identified.

The decomposition is where a quarter becomes information about the business rather
than a number that landed.

## Step 5 — Earnings quality

`methodology/research-report-standard.md` §6. This is where the note earns its
place, because the reported number is the one thing every other reader already
has.

Check, every quarter:

- **Adjusted vs GAAP.** What is excluded, and whether the exclusion recurs. A
  "one-off" appearing for the fourth consecutive quarter is an operating cost.
- **Nonrecurring events** and their treatment.
- **Revenue recognition** changes; **reserve releases** flattering the result.
- **Off-balance-sheet financing.**
- **Depreciation policy** changes, which move earnings without moving cash.
- **Cash conversion.** Earnings that do not become cash are a claim, not a result.
  Receivables growing faster than revenue is the standard tell.

**Automatic red flags** — if either appears, it leads the note:

1. A **qualified audit opinion**.
2. **Material weakness in internal control over financial reporting.**

## Step 6 — Guidance and the forward view

- What did management guide to, and how does it compare to the prior guide?
- What did they say versus what they did? Capital allocation is the revealed
  forecast — a buyback launched into a "cautious outlook" is a contradiction worth
  naming.
- On the call: what did they *not* answer? A dodged question on a metric they used
  to volunteer is information.

## Step 7 — The verdict

Explicit, in one of three states:

| Verdict | Meaning |
|---|---|
| **Intact** | The drivers behind the thesis performed as expected. Estimates may move; the thesis does not. |
| **Weakened** | A driver underperformed. Name it, and state what the next print must show. |
| **Broken** | The mechanism the thesis relied on is not working. Say so plainly and say what it implies for the position. |

Then the falsification update: **what would have to happen next quarter to change
this verdict?** Specific and observable, per `policy/data-integrity.md` §7.

## Step 8 — Hand off and write state

Estimate changes go to `model-update`. The revised view goes to `state.write` —
if private persistence is available. Otherwise return the revised view in chat
or as a private export and state that a later session needs it supplied again.

## Guardrails

- **Do not re-rate on one quarter.** A single print rarely changes intrinsic
  value. If you conclude it does, the reason must be a broken driver, not a missed
  number.
- **Management's characterisation is a fact about management**, not about the
  business. Attribute it.
- **The market's reaction is not a verdict.** A stock down 8% on a good quarter is
  information about positioning, not about value. Analyse both, separately.
- **Symmetry.** Apply the same scrutiny to a beat as to a miss. Beats are where
  earnings-quality problems hide, precisely because nobody looks.
- **Say when the thesis is broken.** The user holds this position. Finding the
  disconfirming evidence before the market does is the point of the agent.

## Output

Written in Spanish, terminology in English:

```
1. Veredicto        — intact / weakened / broken, en la primera línea
2. Resultado        — beat/miss vs [guidance|consensus], por línea
3. Drivers          — descomposición: volumen, precio, mix, FX, one-offs
4. Earnings quality — qué revisaste, qué encontraste, red flags si los hay
5. Guidance         — qué cambió hacia adelante
6. Tesis            — qué se sostiene, qué no, qué la rompería
7. Estimaciones     — cambios, o handoff a model-update
```
