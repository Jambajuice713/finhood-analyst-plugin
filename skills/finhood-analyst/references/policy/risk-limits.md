# Risk limits and user profile

## 1. No personal defaults

No risk tolerance, portfolio target, tax residency, occupation, restricted list or
strategic allocation is preconfigured. Read a user-supplied private profile if one
exists. Otherwise report observed concentration and ask for the constraints needed
for a sizing request. Do not call an observation a breach without an agreed limit.

## 2. Optional illustrative thresholds

Only if the user asks for a demonstration, use the following examples and label
every use "illustrative, not the user's investment policy": single position 15%,
top three 40%, sector 35%, cash reserve 5%. These are editable teaching examples,
not suitable allocations inferred for the user. Portfolio weights include cash.
Using the equity sleeve as denominator overstates individual weights when cash
is positive; it describes a different portfolio.

## 3. Drawdown

Use a unitized or cash-flow-adjusted wealth index. A withdrawal can reduce account
value without an investment loss; a deposit can create a false new peak. If flows
or valuations are incomplete, report raw value changes separately and do not
trigger a performance drawdown warning from them. Always disclose the observation
window; one month of history cannot establish a twelve-month drawdown.

Optional illustrative flags: −5% note, −10% flag, −15% review, −20% severe flag.
These describe observed losses. They do not establish a 95% probability objective
or demonstrate a forecast. No automatic trading follows any threshold.

## 4. Scope

USD US-listed equities and ETFs, cash and long-only analysis. No leveraged,
short, derivative, crypto or FX trading. If the account contains unsupported
assets, scope a labelled supported sleeve with user agreement. Do not silently
drop assets then describe the remaining sleeve as the whole portfolio.

## 5. Ask only what the task needs

- Investment horizon and relevant liquidity needs.
- Required/desired return and minimum acceptable return, if relevant.
- Ability and willingness to bear losses; do not infer either from the balance.
- User-approved concentration, reserve and rebalancing rules.
- Benchmark, if a relative-performance question requires one.
- Tax residency and restrictions only when relevant; never assume a jurisdiction.
- Whether this account is the whole portfolio or one sleeve.

Keep answers in the user's private context/output, not in this package. The blank
template is `config/user-profile.example.json`. Without the needed profile,
explain what can be measured and keep allocation suggestions conditional.
