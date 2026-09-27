# IPS and constraints

How the package thinks about objectives and constraints before it thinks about
positions. From CFA Program Level I 2025, Volume 9, LM4 (*Basics of Portfolio
Planning and Construction*).

The point of this file: **a recommendation is only good relative to an objective.**
Without a stated objective, "this is a good stock" is an assertion about the world,
not advice to the user. Every proposal this package makes traces back to something here.

---

## 1. The portfolio management process

Three steps, and the package touches all three:

| Step | What happens | Where in the package |
|---|---|---|
| **Planning** | Understand circumstances, write the IPS, set the strategic asset allocation | `policy/risk-limits.md` §5 — currently open |
| **Execution** | Analyse, select, size, trade | `agents/`, `skills/`, gated by `policy/execution.md` |
| **Feedback** | Monitor, rebalance, evaluate performance | `schedules/eod-brief.md`, `skills/portfolio-review/` |

The package is strong at execution and feedback and **weak at planning**, because
planning requires answers only the user can give. That asymmetry should be visible in
outputs, not hidden.

## 2. Components of an IPS

There is no single standard format, but the curriculum lists the sections most
IPS documents include:

- **Introduction** — describes the client
- **Statement of Purpose**
- **Statement of Duties and Responsibilities** — client, custodian, managers
- **Procedures** — keeping the IPS current, responding to contingencies
- **Investment Objectives**
- **Investment Constraints**
- **Investment Guidelines** — how policy is executed; permissible use of leverage
  and derivatives; excluded asset types
- **Evaluation and Review** — how feedback on results is obtained
- **Appendices** — (A) Strategic Asset Allocation, (B) Rebalancing Policy

The curriculum notes the sections most closely tied to a client's distinctive
needs, and most important from a planning perspective, are **objectives and
constraints** — an IPS focused on those two is called an *objectives and
constraints* format. That is the shape this package targets.

It also notes an IPS should be reviewed regularly, and **whenever there is a
material change in circumstances** — objectives, time horizon, or liquidity needs.

## 3. Risk objectives

**Absolute** — self-standing, unrelated to market performance. "Do not lose more
than 4% of capital in any 12-month period." The curriculum's key move: such an
objective is only *operational* when restated as a probability — "with 95%
probability, the portfolio does not lose more than 4% in any 12-month period."
Measures: variance, standard deviation, value at risk.

**Relative** — defined against a benchmark. Measure: tracking risk (tracking
error), the standard deviation of the differences between portfolio and benchmark
returns.

## 4. Risk tolerance: ability vs willingness

The distinction the package must never collapse.

**Ability to bear risk** is objective: time horizon, expected income, level of
wealth relative to liabilities. A 20-year horizon carries more ability to bear risk
than a 2-year one, because there is more scope for losses to be recovered.

**Willingness to take risk** is subjective — the client's risk attitude, a matter
of psychology and circumstance.

The curriculum's matrix:

| | **Ability: Below Average** | **Ability: Above Average** |
|---|---|---|
| **Willingness: Below Average** | Below-average risk tolerance | **Resolution needed** |
| **Willingness: Above Average** | **Resolution needed** | Above-average risk tolerance |

Where the two disagree, the curriculum requires **resolution** — not averaging.
The prudent resolution is the lower of the two, and the conflict is discussed with
the client rather than silently resolved by the adviser.

**Applied to this package:** the agent does not infer the user's willingness from his
trades and does not infer his ability from his account balance. Both are asked
for. Where they conflict, the agent names the conflict.

## 5. Return objectives

Also absolute or relative. The distinctions that must be stated explicitly,
because each changes the number:

- **Absolute** — a target percentage, nominal or **real** (inflation-adjusted).
  The curriculum notes nominal is more convenient to measure but real usually
  relates better to the actual objective.
- **Relative** — versus a benchmark, e.g. index + 1% per year. A good benchmark
  must be **investable** — replicable by the investor. The curriculum flags that
  peer-group benchmarks typically fail this test, and adds the obvious
  impossibility of all institutions being above average.
- **Required vs desired** — a *required* return is what the investor needs to earn
  to meet a specific future goal. A desired return is what they would like.
  Confusing the two is how portfolios end up carrying risk that no goal requires.
- **Before or after fees**, and **pre- or post-tax**. For a taxable investor, the
  curriculum's baseline is to state and analyse returns **after tax**.

And an obligation the package inherits: **the adviser must ensure the return
objective is realistic** — consistent with the risk objective and with the current
market environment — and where expectations are unrealistic, must counsel the
client on what is achievable. The curriculum's example: 15% nominal might be
possible with 10% inflation, but not with 3%.

This is a licence to push back on the user's return expectations, and an instruction to.

## 6. Constraints

Five types, each with implications for what may be held:

**Liquidity requirements.** Likely withdrawals from the portfolio. Where a
requirement exists, part of the portfolio is allocated to cover it — in liquid,
low-risk assets whose value is known with reasonable certainty at the time the need
arises.

**Time horizon.** The period over which the portfolio accumulates, or until
circumstances change. Illiquid or risky investments may be unsuitable for a short
horizon because there is not enough time to recover from losses.

**Tax concerns.** Tax status varies; income and capital gains may be taxed at
different rates. Ask about the relevant jurisdiction; do not assume the tax treatment of US-listed
securities, and dividend withholding.

**Legal and regulatory factors.** Including any restriction arising from the user's
professional roles. His call to state, not the agent's to guess.

**Unique circumstances.** Exclusions, ESG preferences, anything else specific.

## 7. Strategic asset allocation and rebalancing

The SAA — the *policy portfolio* — is the baseline allocation to asset classes
given the objectives, together with the policy on rebalancing weights.

The package supplies **no preconfigured SAA**. Use a user-supplied plan if
available; otherwise state the limitation: without one, every
position size is judged against a limit rather than against a plan, and
"rebalancing" has no target to rebalance toward. Position sizing work should say
so where it applies.

## 8. Practical use in this package

Before any recommendation, the agent should be able to answer:

1. Which objective does this serve — required return, or desired?
2. Is the risk it adds consistent with the stated risk objective?
3. Does it breach a constraint (liquidity, horizon, tax, legal, unique)?
4. Where does it sit against the SAA — and if there is none, say so.

If §5 of `policy/risk-limits.md` is still open, the honest answer to several of
these is "no stated objective to check against." **Say that, in the output.** It is
the single most useful thing the package can tell the user until he fills it in.
