---
name: audit-xls
description: Audits a spreadsheet or financial model for formula errors, broken links, hardcodes, and integrity failures — balance sheet balancing, cash tie-out, sign consistency, and logic sanity. Use for "audit this model", "check my formulas", "QA this spreadsheet", "the model won't balance", or before any model ships.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Audit Spreadsheet

Runs before any model leaves the package. An unaudited model that reaches a
conclusion is worse than no model, because the conclusion carries unearned
authority.

---

## Scope

State the scope before starting: a selected range, one sheet, or the whole model
including integrity checks. A full model audit is a different exercise from a
formula check on one block.

## Pass 1 — Mechanical errors

- **Error values**: `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`. Any one of
  them means a broken calculation, and `#REF!` specifically means a deleted
  precedent — the model no longer computes what it was built to compute.
- **Broken links** to external workbooks.
- **Inconsistent formulas across a row.** The highest-yield check in this entire
  skill: a row that should be uniform where one cell differs is almost always a
  manual override someone made and forgot. Scan every projection row.
- **Hardcodes inside formula ranges.** A number typed into a cell that should
  contain a formula. These survive assumption changes and silently break the
  model's responsiveness — an analyst changes an input, the output does not move,
  and nobody notices.
- **Circular references** that are not deliberate. See
  `skills/3-statement-model/` §Circularity.

## Pass 2 — Structural integrity

For a financial model:

| Check | Requirement |
|---|---|
| **Balance sheet balances** | Assets = Liabilities + Equity, **every period**, not just year 1 |
| **Cash ties out** | Closing cash on the CF equals cash on the BS, every period |
| **Retained earnings rolls** | Opening + net income − dividends = closing |
| **Debt schedule ties** | Opening + draws − repayments = closing, and interest is consistent |
| **Fixed assets tie** | Opening + capex − depreciation = closing |
| **Sign conventions** | An increase in working capital is a *use* of cash. Consistent throughout. |
| **No plugs** | Any cell whose purpose is to force a tie is a defect, not a solution |

## Pass 3 — Logic sanity

Errors that are arithmetically valid and analytically wrong. The spreadsheet will
not flag any of these:

- **Margins outside historical range** with no stated mechanism.
- **Growth without reinvestment** — revenue rising, capex and working capital flat.
- **Negative cash** with no revolver.
- **Terminal growth above long-run GDP growth.** Check it explicitly; it is the
  single most common valuation error and it is invisible in the output.
- **Terminal year at a cycle extreme**, being capitalised in perpetuity.
- **Discount rate inconsistent** with the cash flows: FCFF discounted at cost of
  equity, or nominal cash flows at a real rate. Both produce a confident, wrong
  number.
- **Units and scale.** Thousands mixed with millions. Rare, catastrophic, and
  easy to check by scanning magnitudes across a row.
- **Date and period alignment.** Fiscal versus calendar years across a peer set;
  a quarter offset propagating through a comparison.

## Pass 4 — Presentation

- Assumptions in one place, clearly labelled, none buried inside formulas.
- Inputs visually distinguished from calculations.
- Sources cited on historical figures.
- `[UNSOURCED]` markings present wherever data was unavailable —
  `policy/data-integrity.md` §1. **A model with no `[UNSOURCED]` markings and
  incomplete data is worse than one that shows its gaps**, and the audit should
  ask where the gaps went.

## Output

```
1. Veredicto        — ships / needs fixes / do not use
2. Errores críticos — lo que hace que el output esté mal
3. Errores menores  — lo que hay que arreglar pero no cambia la conclusión
4. Observaciones    — lógica cuestionable, supuestos sin defender
5. Qué no revisé    — alcance de la auditoría
```

Section 5 matters. An audit that does not state its own scope will be read as
comprehensive.

## Guardrails

- **Do not fix silently.** Report, then fix on instruction. An audit that quietly
  changes numbers destroys the audit trail and the reader's ability to judge what
  happened.
- **Distinguish "wrong" from "I would have done it differently."** Both are worth
  saying; conflating them buries the errors that matter under stylistic
  preference.
- **Check every period.** Models routinely balance in year 1 and break in year 4,
  and year 4 is where the terminal value comes from.
- **Verdict first.** If the model should not be used, that goes in the first line,
  not at the end of a list.
