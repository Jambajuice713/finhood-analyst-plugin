---
name: model-update
description: Updates a valuation model with new information — quarterly results, revised guidance, macro changes, or new assumptions — recalculates the valuation, and flags what changed materially. Use for "update the model", "plug the quarter", "refresh estimates", or "new guidance".
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Model Update

Takes new information into an existing model and reports what it did to the value.

The discipline that makes this skill useful: **change the inputs, then look at the
output. Never the reverse.** A model updated to preserve a target price is not a
model, and the temptation is strongest exactly when the position is large.

---

## Step 1 — Snapshot before

Record the pre-update state so the delta is measurable:

- Current estimates by year.
- Current valuation output and target.
- The assumptions the value is most sensitive to, and their values.

Without this, "the target moved to X" carries no information about why.

## Step 2 — Update actuals

Replace forecast periods with reported figures. Then reconcile:

- **Where were you wrong, and by how much?** Not to score yourself, but because
  the error pattern is diagnostic. Consistently over-forecasting margin means the
  margin assumption has a structural problem, not that one quarter disappointed.
- Check that historical restatements have not silently changed the base.

## Step 3 — Update the forward view

Only where something actually changed. Each change carries a **reason**:

| Change | Requires |
|---|---|
| Revenue growth | What changed in volume, price, or mix — not "management guided lower" |
| Margin path | The mechanism: scale, mix, pricing, or cost action |
| Capex / reinvestment | What the growth requires, kept consistent with it |
| Working capital | Its relationship to revenue, if that relationship shifted |
| Discount rate | Only if the rate environment or the risk profile actually moved |
| Terminal assumptions | Rarely. If terminal growth is moving quarterly, it was never an estimate |

**Unchanged assumptions stay unchanged.** Resist the urge to refresh everything;
the point of the delta is that it is attributable.

## Step 4 — Recalculate and attribute

Report the change in value **decomposed by source**:

> "Target moves from USD 142 to USD 151. Of the USD 9, roughly 6 comes from the
> higher margin path, 2 from the lower share count after the buyback, and 1 from
> rolling the model forward a quarter."

A target that moves with no attribution is a number that changed for reasons
nobody can audit — including, later, you.

Roll-forward deserves its own line and its own scepticism. Value that appears
purely because time passed is not new information; it is the discount rate
unwinding, and it should be labelled rather than presented as an upgrade.

## Step 5 — Re-run the sensitivity

The assumption the value is most sensitive to may have changed. Re-identify it and
show the range. `skills/dcf-model/` §Sensitivity.

## Step 6 — State what it means

- Did the **thesis** change, or only the estimates? These are different, and the
  distinction is the output. Estimates move every quarter; theses should not.
- Does the new value change the position's attractiveness at the current price?
- Does the falsification condition need updating?

## Step 7 — Audit and persist

Run `skills/audit-xls/` on the updated model — an update is exactly when a link
breaks silently. Then privately persist the revised view if storage is available; otherwise
export it or return it in chat and state that it was not persisted.

## Guardrails

- **Never solve backwards to a target.** If the honest inputs give a lower value,
  the output is a lower value. Reverse-engineering the assumption that preserves
  the target is the single most common way sell-side models lose their meaning,
  and it is invisible to a reader.
- **One quarter is not a trend.** Do not re-base a multi-year forecast on a single
  print. If you do, state explicitly why this print is structural.
- **Flag material changes prominently.** A 15% change in value is the headline,
  not a table cell.
- **Do not extrapolate a cycle.** `methodology/research-report-standard.md` §6. If
  the updated base year is a cycle extreme, normalise it or say you did not.
- **Preserve the audit trail.** What changed, from what to what, and why. A model
  whose history is not reconstructible cannot be trusted six months later.
