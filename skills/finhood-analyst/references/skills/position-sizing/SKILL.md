---
name: position-sizing
description: Decides how much of a name to hold, given conviction, risk limits, correlation with the existing book, and available cash. Use after a thesis exists and before any order is proposed. Turns "I like this" into a specific quantity with the reasoning attached.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Position Sizing

A thesis without a size is not a decision. This skill turns one into the other.

Sizing is where most of the realised risk in a personal portfolio actually gets
set — more than security selection, because a good name at 40% of the book and the
same name at 4% are different portfolios with different outcomes.

---

## Inputs required

Do not size without all of these:

1. **The thesis**, with its falsification condition. If it does not exist, the
   answer is "no size" — send it back to research.
2. **The current book** — `portfolio.positions`, `portfolio.balance`.
3. **The limits** — user-agreed constraints per `policy/risk-limits.md`; otherwise stop personalised sizing and ask.
4. **The correlation picture** — what in the book already carries this driver.

## Method

### 1. Start from the limit, not from conviction

The maximum is the lower of:

- The single-position limit in `policy/risk-limits.md` (illustrative only: 15%).
- What leaves cash above the reserve (illustrative only: 5%).
- What keeps the relevant sector under its limit (illustrative only: 35%).
- What keeps the top-3 concentration under its limit (illustrative only: 40%).

**Conviction moves the size down from the cap, never up through it.** A limit that
bends for a good idea is not a limit, and the ideas that bend it are always the
ones that felt strongest at the time.

### 2. Adjust for correlated exposure already held

This is the step that gets skipped. If the book already holds a name with the same
driver, the *incremental* exposure is larger than the position weight suggests —
portfolio variance carries the covariance term
(`methodology/risk-measures.md` §4).

Illustrative stress lens: group correlated positions as one exposure and show
the group weight. Do not silently replace the user’s single-name rule with a
group rule; apply a group cap only if the user has agreed to one. Two names at 10%
each with the same end-market are a 20% bet on that end-market, and should be
compared with any user-agreed driver/sector cap; do not assume a 15% group cap.

### 3. Adjust for the shape of being wrong

- **How far can this fall before the thesis is disproven?** That distance, times
  the weight, is the loss being underwritten. State it in the proposal.
- **Is the downside bounded or open?** A name whose thesis breaks slowly, on a
  data point months away, is a different risk from one that can gap on a single
  print.
- **Liquidity.** Can the position be exited in a normal session at something like
  the screen price? If not, size down regardless of conviction — an exit you
  cannot take is not a stop.

### 4. Adjust for what the size implies about certainty

The honest question, and the useful one to put to the user: *at this size, what
fraction of the portfolio's outcome does this one thesis determine?* If the answer
is "most of it", the size is a claim about certainty that the analysis probably
does not support.

### 5. Check against the user’s plan, if supplied

`methodology/ips-and-constraints.md` §7: the package has **no preconfigured strategic
asset allocation**. Read the user’s own allocation if supplied. Sizing is therefore being judged against limits rather than
against a plan, which is a materially weaker test. Say so in the proposal when it
applies. It is a real gap and repeating it is how it gets closed.

## Output

Every sizing decision states:

| Element | Example |
|---|---|
| Action and size | Comprar USD X (≈ N acciones al precio actual) |
| Resulting weight | Y% del portafolio total, incluyendo caja |
| Post-trade limits | Sector Z pasa a W%; caja queda en V% |
| Correlated exposure | Junto con [nombre], la exposición a [driver] queda en U% |
| Loss underwritten | Si la tesis se rompe en −30%, el impacto en el portafolio es −A% |
| Falsification | La tesis se rompe si [condición observable] |
| Limits status | Los umbrales son defaults provisionales, no política declarada |

Then stop. `policy/execution.md`: proposals only.

## Analytical scope

Express scenarios as USD exposure and estimated shares at a sourced price.
Obtain user limits before personalised sizing. The numerical examples in this
procedure apply only when the user explicitly selects an illustrative exercise.
No trade-options, previews or order tools are part of this procedure.

## Failure modes

| Mistake | Consequence |
|---|---|
| Sizing on conviction alone | Largest positions end up in the strongest narratives, not the best risk-reward |
| Ignoring correlated holdings | True concentration is a multiple of what the weight table shows |
| Sizing before a falsification condition exists | No exit discipline, because there is nothing to be wrong about |
| Averaging down without re-underwriting | Turns a sizing decision into a sunk-cost decision |
| Treating the cap as a target | Every conviction name arrives at the maximum |
