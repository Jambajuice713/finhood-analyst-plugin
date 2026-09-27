---
name: morning-note
description: Short, opinionated note on what matters today for the portfolio — overnight developments, events on the calendar, and anything requiring a decision. Use for "morning note", "what happened overnight", "what should I know today", or as the pre-open counterpart to the EOD brief.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Morning Note

Tight, opinionated, actionable. The counterpart to `schedules/eod-brief.md`: the
brief closes the day, this one opens it.

**Length discipline is the skill.** A morning note that takes ten minutes to read
is not a morning note. If nothing happened, the correct output is three lines
saying so — and that is a legitimate, useful answer, not a failure to find
content.

---

## Inputs

```
state.read("portfolio-snapshot")   # yesterday's close
state.read("watch-list")           # what we said we were watching
market.clock                       # is the market opening today at all
portfolio.positions
market.quote (per position)        # pre-open or last available
research.news                      # overnight, scoped to held names
```

## Structure

```
1. Qué cambió       — overnight, solo lo que afecta a las posiciones
2. Hoy              — earnings, datos macro, eventos con fecha conocida
3. Qué requiere una decisión — si algo la requiere. Con frecuencia, nada.
```

## What goes in

**Only what affects the book.** The filter is not "is this interesting" but "does
this change something about a position the user holds or is considering". General
market commentary is available everywhere and adds nothing here.

- Overnight moves in held names, **with the reason** if findable. `[UNSOURCED]`
  if not — an unexplained move reported as unexplained is honest and useful.
- Events dated today: earnings from held names, macro releases that bear on a
  stated thesis.
- Anything from yesterday's watch list that resolved.
- Any risk-limit threshold that a pre-open move has put in reach.

## What stays out

- Index levels for their own sake.
- Names the user does not hold and is not considering.
- Restating yesterday's brief.
- Speculation about the session ahead. Nobody knows, and a forecast dressed as a
  briefing is worse than silence.

## Tone

Opinionated. "NVDA down 3% overnight on the Reuters report about export
restrictions; this touches the second-order thesis on the on-prem names, worth
watching but not acting on" is a morning note. "NVDA is down 3%" is a price feed.

The value added over a price feed is **judgement about what matters**, and
judgement means being willing to say something is noise.

## Guardrails

- **No execution.** If run on a schedule, `policy/execution.md` §2 applies
  absolutely: read-only. A decision item is flagged for an interactive session.
- **Pre-open prices are not live prices.** Say what you are quoting and as of when.
  `policy/data-integrity.md` §4.
- **Check the calendar before writing.** `market.clock`. A morning note for a day
  the market does not open is a bug.
- **Attribute overnight narratives.** "Reuters reported" is a fact;
  "the market is worried about" is a claim you now own.
- **Silence is a valid output.** Manufacturing content on a quiet morning trains
  the reader to skim, and then they skim on the morning it matters.
