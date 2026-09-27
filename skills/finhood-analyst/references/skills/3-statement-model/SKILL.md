---
name: 3-statement-model
description: Builds or completes an integrated income statement, balance sheet, and cash flow model, with the three statements properly linked and the balance sheet balancing. Use for "build a 3-statement model", "complete this model template", "populate the financials", or when a DCF needs a real operating model behind it.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# 3-Statement Model

The operating engine. A DCF built on a projected FCF line with no balance sheet
behind it cannot check its own internal consistency — the three-statement model is
what makes the projections falsifiable.

**The balance sheet balancing is not a formatting achievement. It is the proof
that the model's assumptions are mutually consistent.** When it does not balance,
the model is telling you something is wrong. Never plug it.

---

## Build order

Order matters — building the balance sheet before the income statement produces
circularity you then have to unwind.

1. **Historicals**, three years minimum, from filings. Tie every line to the
   source document.
2. **Income statement** projections, driven per `skills/dcf-model/` §2 — from
   mechanisms, not growth rates.
3. **Working capital schedule** — receivables, inventory, payables, each as a
   ratio to its natural driver (DSO on revenue, DIO on COGS, DPO on COGS).
4. **Fixed asset schedule** — opening PP&E, capex, depreciation, closing.
5. **Debt schedule** — opening balance, drawdowns, repayments, interest.
6. **Cash flow statement**, built from the above.
7. **Balance sheet**, closing from opening plus the flows.
8. **Check it balances.** Every period.

## The linkages that must hold

| Link | Rule |
|---|---|
| Net income | IS → retained earnings on the BS, and the top of the CF |
| Depreciation | Fixed asset schedule → IS and added back in CF |
| Capex | Fixed asset schedule → investing in CF |
| Working capital changes | WC schedule → operating in CF |
| Debt movements | Debt schedule → financing in CF and the BS balance |
| Interest | Debt schedule → IS |
| Closing cash | CF → BS |
| **Balance check** | Assets = Liabilities + Equity, **every period, exactly** |

## Circularity

Interest depends on debt, debt depends on the cash flow, and the cash flow depends
on interest. Three ways to handle it, in order of preference:

1. **Average balances** for the interest calculation — breaks the circularity
   cleanly and is accurate enough for a valuation model.
2. **Opening balances** — simpler still, slightly less accurate.
3. **Iterative calculation** — enable it deliberately, document it, and be aware
   that it will hide errors: a circular model with a mistake converges on the
   wrong answer silently.

Prefer (1). A model that requires iterative calculation to resolve is harder to
audit and harder to hand to anyone else.

## When it does not balance

Work through it in this order — the cause is almost always in the first two:

1. **Cash flow statement.** Every balance sheet movement must appear somewhere in
   it. A missing line is the most common cause.
2. **Sign conventions.** An increase in receivables is a *use* of cash. Mixed sign
   conventions are the second most common cause.
3. **The retained earnings roll-forward** — opening + net income − dividends.
4. **A hardcode inside a formula range**, from a previous attempt to make
   something tie.

**Never plug the difference.** A plug is a note to your future self saying the
model cannot be trusted, written in a place where nobody will read it.

## Quality checks before it ships

- Balance check on every projected period, not just the first.
- Cash never goes negative without a corresponding revolver draw.
- Margins, working capital ratios, and returns compared to history — a model
  projecting margins the company has never achieved needs a stated mechanism.
- Growth and reinvestment consistent: revenue rising with flat capex requires an
  explanation.
- Terminal year is a plausible **steady state**, not a peak or a trough. The DCF
  will capitalise it in perpetuity.

Then run `skills/audit-xls/`.

## Guardrails

- **Tie historicals to filings.** Every one. A model built on remembered
  historicals is worthless, and the error compounds through the entire forecast.
- **Label assumptions**, keep them in one place, and never bury one inside a
  formula. A reader must be able to change an assumption and see the model
  respond.
- **Document restatements.** If the company restated, say so — the historical base
  changed and any comparison across the restatement is invalid.
- **`[UNSOURCED]` for what you could not find.** A gap is a gap.
