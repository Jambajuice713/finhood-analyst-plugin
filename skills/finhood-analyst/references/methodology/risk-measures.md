# Risk measures

Dispersion, downside risk, and portfolio-level risk. From CFA Program Level I
2025, Volume 1 (*Quantitative Methods*, LM3 *Statistical Measures of Asset
Returns*, LM5 *Portfolio Mathematics*) and Volume 9 (LM1, LM6).

---

## 1. Standard deviation, and its blind spot

Sample standard deviation of returns is the default risk measure and the
denominator of the Sharpe ratio. It has one property that matters for a personal
portfolio: **it counts upside and downside deviations equally.** A position that
doubled and a position that halved contribute to it the same way.

The curriculum's own framing: variance and standard deviation account for returns
above and below the mean — upside and downside risks respectively — but
**investors are typically concerned only with downside risk.**

So report it, and then report something that answers the question the user actually
has.

## 2. Target downside deviation

Also called target semideviation. Dispersion of returns **below a target**, not
below the mean:

```
s_target = √( Σ (X_i − B)² / (n − 1) )   for all X_i ≤ B
```

Where `B` is the target and `n` is the **total** number of observations in the
sample — not the count of observations below the target. The denominator is
`n − 1` over the full sample.

Worked, from the curriculum: twelve monthly returns of 5, 3, −1, −4, 4, 2, 0, 4,
3, 0, 6, 5 (%), against a 3% target. Only the observations at or below 3 that fall
*below* it contribute: −1, −4, 2, 0, 0 → squared deviations of 16, 49, 1, 9, 9,
summing to 84. Then `√(84 / 11) = 2.7634%`.

**Set `B` to the user's minimum acceptable return** once §5 of `policy/risk-limits.md`
is filled in. Until then, use 0% and label the target.

This is the more honest risk number for someone who holds the whole portfolio
himself, and it belongs in any review that reports volatility.

## 3. Coefficient of variation

```
CV = σ / mean
```

Risk per unit of return. Useful for comparing dispersion across positions with
different return levels. **Meaningless when the mean is near zero or negative** —
the ratio explodes or flips sign. Check before reporting.

## 4. Portfolio risk is not the average of position risks

From LM5. Portfolio variance for two assets:

```
σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂
```

The third term is the whole point. **Correlation, not the individual variances,
determines how much diversification a portfolio actually gets.** Two positions
that each look moderate can combine into something concentrated if they move
together.

Practical consequence for the EOD brief and for `portfolio-review`: a
concentration check that only counts position weights is incomplete. Two 12%
positions in the same sector with ρ ≈ 0.9 are closer to one 24% position than to
two independent bets. Say that when it is true, in those terms.

Where a full correlation matrix is not available — no return history, short
history, missing `research.market_data` — use **sector and factor overlap as the
proxy** and state that it is a proxy. A named qualitative concentration beats an
uncomputed quantitative one.

## 5. Value at risk, and what it does not tell you

The curriculum defines VaR as *a money measure of the minimum value of losses
expected during a specified period at a given level of probability*. It is the
natural way to make an absolute risk objective operational: "with 95%
probability, do not lose more than X in any 12-month period."

Two constraints on using it here:

- It requires a distributional assumption, usually normality, which understates
  tail frequency in equity returns.
- It says nothing about **how bad the tail is beyond the threshold**. A 95% VaR
  of 10% is consistent with a 40% loss in the remaining 5%.

Report it with the assumption named, or do not report it.

## 6. Tracking risk

Standard deviation of the differences between portfolio returns and benchmark
returns, stated as a one-standard-deviation measure. It is the natural measure for
a **relative** risk objective.

The curriculum's illustration of how to read it: assuming normally distributed
returns, an expected tracking risk of 2% implies the portfolio return lands within
4% of the index roughly 95% of the time.

Requires a benchmark. None is set — see `policy/risk-limits.md` §5.

## 7. Risk is not only variance

From Volume 9 LM6. The package's quantitative limits cover financial risk. Real
exposures that no variance calculation will surface, and which belong in a review
as prose:

- **Liquidity risk** — can the position be exited in a normal session at
  something like the screen price?
- **Concentration in a shared driver** — several positions exposed to the same
  rate, the same customer, the same regulation.
- **Model risk** — the target price is only as good as the assumption it is most
  sensitive to. Name that assumption.
- **Operational risk** — in this package: a stale binding, an unread snapshot, a
  missed close. `state/README.md` covers the failure modes.

## 8. Behavioural checks

From Volume 9 LM5. These are not decoration — they are the failure modes of a
one-person portfolio, and the agent's job includes naming them when the pattern
appears in the account:

| Bias | What it looks like in the book |
|---|---|
| **Loss aversion** | Winners sold, losers held. Check realised vs unrealised P&L distribution. |
| **Overconfidence** | Position sizes rising with conviction rather than with edge. |
| **Confirmation** | Research requested only on names already held. |
| **Endowment** | A held position defended with arguments that would not justify buying it today. |
| **Status quo** | No rebalancing despite drift past the tolerance band. |
| **Regret aversion** | Crowding into what has already worked. |

The test for **endowment bias** is the one to apply most often, and it is a single
question: *if this position were not already in the book, would the analysis
support opening it today at this price and this size?* If the answer is no, that
belongs in the review — plainly, not softened.
