# Returns and performance measurement

The authority for every return figure the package publishes. Grounded in CFA
Program Level I 2025, Volume 1 (*Quantitative Methods*, LM1 *Rates and Returns*)
and Volume 9 (*Portfolio Management*, LM2 *Portfolio Risk and Return: Part II*).

Portfolio return is the number the user will trust most and check least. Get it right.

---

## 1. Holding period return

The base unit. For one period:

```
R = (V_end − V_begin + income) / V_begin
```

This formula assumes V_end excludes the distributed income. For total account
value that already includes dividends in cash/reinvestment, do not add them again.
Income belongs in the numerator only when not already included in V_end. A price-only figure is a **price return**, not a
holding period return, and must be labelled as such when
`portfolio.dividends` is unavailable.

Worked arithmetic example: 100 shares bought at USD 34.50, sold at
USD 30.50 after a USD 51.55 dividend →
`R = (3,050 − 3,450 + 51.55) / 3,450 = −10.1%`, which decomposes into a
**dividend yield of +1.49%** and a **capital loss of −11.59%**. Report the
decomposition when it is available; it is more informative than the total.

Across multiple periods with no cash flows, compound rather than add:

```
R = [(1 + R₁)(1 + R₂)…(1 + Rₜ)] − 1
```

## 2. Arithmetic vs geometric mean — and why it matters here

**Arithmetic mean** is the simple average of period returns. **Geometric mean** is
the compound growth rate:

```
R_G = [(1 + R₁)(1 + R₂)…(1 + Rₜ)]^(1/T) − 1
```

The curriculum is unambiguous on the relationship: **the geometric mean is always
less than or equal to the arithmetic mean**, equal only when every observation is
identical, and **the arithmetic mean is biased upward** unless all period returns
are equal. The bias grows with dispersion and is *particularly severe when returns
mix positive and negative*.

Illustrative return series: annual returns of −50%, +35%, +27% give an
arithmetic mean of **+4.0%** and a geometric mean of **−5.0%**. EUR 1.00 invested
becomes EUR 0.8573 — the geometric figure describes what happened; the arithmetic
figure would have implied EUR 1.1249.

**Rule for this package: report the geometric mean when describing what the
portfolio actually did.** The arithmetic mean appears only when the question is
about a single-period expectation, and it is labelled.

## 3. Time-weighted vs money-weighted return

This is the distinction that most often goes wrong in a personal portfolio,
because deposits are frequent and invisible in a value series.

**Money-weighted return (MWR)** is the IRR of the portfolio's cash flows — the
discount rate that sets the NPV of all inflows and outflows to zero. It answers
*"what did the user earn on the money he put in, given when he put it in?"* It is
sensitive to the size and timing of contributions.

**Time-weighted return (TWR)** measures the compound growth of one unit invested
at the start, and — in the curriculum's words — **is the preferred performance
measure for portfolios of publicly traded securities because it neutralises the
effect of cash withdrawals or additions**, which are outside the manager's control.

### Computing TWR

1. Value the portfolio **immediately before** any significant addition or
   withdrawal. Break the period into subperiods at those dates.
2. Compute the holding period return for each subperiod.
3. Link them: `R_TW = (1 + r₁)(1 + r₂)…(1 + rₙ) − 1`.
4. Over more than a year, annualise as the geometric mean of the annual returns:
   `R_TW = [(1 + R₁)…(1 + R_N)]^(1/N) − 1`.

Illustrative linked returns: quarterly HPRs of 20%, 5%, 12%, −10% link to
`(1.20)(1.05)(1.12)(0.90) − 1 = 27.01%`. MWR can differ because it weights the timing and size of contributions.
Do not infer a numerical MWR without the actual dated flows.

### Which one this package reports

- **TWR** for "how did the portfolio perform" — the manager's result.
- **MWR** for "how did the user's money do" — his actual experience.
- When both are available and they differ materially, **report both and explain
  the gap**. The difference is a fact about his contribution timing, and it is
  often the more useful insight of the two.

### The approximation, and its condition

Exact TWR requires valuation at every cash flow. The curriculum permits
approximating it by valuing at frequent regular intervals — daily valuation is
commonplace — and notes the approximation is good **particularly if additions and
withdrawals are unrelated to market movements**, and that more frequent valuation
is more accurate. If withdrawals and additions occur only at day's end, linked
daily returns give a *precise* TWR for the year.

**That condition is doing real work.** If the user deposits after a drawdown — buying
the dip — his cash flows are precisely *not* independent of market movements, and
the approximation degrades. Note it when it applies.

## 4. Degradation: what to report when transactions are unavailable

If `portfolio.transactions` is not supplied by the active binding:

| Situation | What may be reported |
|---|---|
| Cash flows can be ruled out for the period | TWR, computed from the value series |
| Cash flows cannot be ruled out | **Value change only**, explicitly labelled. Not a return. |
| Single-day period, no known flows | Daily value change, labelled as such |

Never publish an unlabelled percentage derived from a value series that might
contain a deposit. It will read as a return, and it will be wrong by exactly the
size of the deposit.

## 5. Annualisation

Annualise only when the period is long enough for the figure to mean something.
Annualising a five-day return produces a number that is arithmetically correct
and analytically worthless. As a working rule: **do not annualise a period shorter
than one quarter**, and always show the underlying period return alongside.

## 6. Risk-adjusted performance

Required inputs differ: Sharpe needs a valid portfolio return series and
matched risk-free returns; it does not require a market index. Treynor and
Jensen alpha require a benchmark-based beta, and M² needs benchmark volatility.
Source inputs and align periods/frequencies. If missing, report unavailable.
Reference: CFA Institute, Measures of Risk-Adjusted Return:
https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/gips/measures-risk-adjusted-return.pdf

### Sharpe ratio

```
SR = mean(r_p,t − r_f,t) / stdev(r_p,t − r_f,t)
# For a constant risk-free return per observation, the denominator equals σ_p.
# State sample period/frequency; justify any square-root annualisation.
```

Total risk in the denominator, which makes it the right measure when the portfolio
**is** the investor's total portfolio — only if the user confirms this is the whole portfolio. It is the slope of the capital
allocation line, also called the reward-to-variability ratio.

Two limitations the curriculum names explicitly, both of which must be respected
in output:

1. It uses total risk when only systematic risk is priced.
2. **The ratio in isolation is not informative.** "A Sharpe of 0.4" says nothing
   without a comparison. Always report it against something.

And a trap: **if the numerator is negative, the ratio becomes less negative for
riskier portfolios, producing incorrect rankings.** When excess return is
negative, do not rank on Sharpe. Say why.

### Treynor ratio

```
TR = (R_p − R_f) / β_p
```

Substitutes systematic risk for total risk. **Requires a positive numerator *and* a
positive beta** — it does not work for negative-beta assets.

### M² (risk-adjusted performance)

```
M² = (R_p − R_f) × (σ_m / σ_p) + R_f  =  SR × σ_m + R_f
```

Ranks portfolios identically to Sharpe, but expresses the answer in percentage
return at market-equivalent risk, which is far easier to communicate.
**M² alpha = M² − R_m** is the risk-adjusted out/underperformance in points.

Curriculum example: R_f = 4%, R_p = 14%, σ_p = 25%, σ_m = 20% → SR = 0.4,
M² = 0.4(0.2) + 0.04 = 12.0%. Against a market return of 10%, M² alpha = **+2.0%**.

**Prefer M² over Sharpe in briefs written for the user.** Same ranking, but "+2.0% at
market risk" lands where "0.40" does not.

### Jensen's alpha

```
α_p = R_p − [R_f + β_p(R_m − R_f)]
```

The vertical distance from the SML. Positive is outperformance. By definition the
market's alpha is zero. Uses realised returns throughout; over a long period, R_f
is the average risk-free rate.

### Which to use here

| Question | Measure |
|---|---|
| Is the user being paid for the risk he is taking? | Sharpe — uses total portfolio risk; do not assume this account is the investor’s entire wealth |
| How much did that skill add, in points? | M² alpha |
| Did he beat the market for his systematic exposure? | Jensen's alpha |
| Comparing sleeves inside a diversified whole | Treynor |

Beta estimation requires a return history against a benchmark. If the history is
short, **say how short**. A beta from twenty daily observations is decoration.
