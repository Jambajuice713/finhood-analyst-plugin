---
name: eod-brief
description: Produce a US-market close brief on request, with sourced portfolio observations and explicit gaps.
---

# End-of-day brief

This procedure runs on request. It does not create a scheduled task. An optional
host scheduler must enforce read-only account tools and private durable state
before use; see `policy/execution.md`.

## 1. Establish the session

Use the actual US equity session date in America/New_York. A market being closed
right now does not prove that a trading session occurred today. Check the last
completed session or an authoritative exchange calendar, including holidays and
early closes. If the tool only reports open/closed and next open/close, those
fields alone may be insufficient. Before today's close, do not present live
prices as closing marks. If session evidence is unavailable, label the result
"point-in-time portfolio review" and set `session_confirmed: false`.

## 2. Read the data

Read an available private baseline, market status, balance and positions. Obtain
quotes, history, external flows, dividends and order history only as needed.
Validate timestamps, currencies and complete pagination. No order previews or
account mutations. An empty account is valid: report observed cash and absence
of positions, with no invented return or research obligation.

## 3. Compute supported measures

- Total value including cash; do not substitute buying power for cash.
- Weights using that same total and observation time.
- Return only when flows and valuation timing support the stated method. Exact
  TWR needs pre/post-flow valuations. Otherwise label a supported approximation
  or report value change. Do not add dividends already included in account value.
- Attribution only from the required holdings, timing, flows and prices. A
  current position's daily price change alone does not explain portfolio P&L.
- Drawdown only from cash-flow-adjusted performance and over the observed window.
- Compare concentration with user-agreed limits, or label examples explicitly.

## 4. Research relevant changes

Retrieve company news and upcoming events using issuer/ticker only; do not send
portfolio balances or quantities in searches. Cite source/date. If no catalyst
is established, say so. Distinguish an earnings expectation from confirmed news.

## 5. Output and optional persistence

Respond in Spanish with: (1) observation/session date and coverage, (2) portfolio
composition and supported performance, (3) relevant company developments,
(4) concentration/risks, (5) next events, (6) assumptions and unavailable data.
Text proposals may be included; the user acts separately in the brokerage app.
Write a private snapshot only where persistence is available and appropriate.
Report success or absence of persistence explicitly.

## Optional scheduling

Use a scheduler that supports `America/New_York`, for example weekdays at 16:30
local time, and always check the exchange calendar inside the run. An early-close
session still gets a later brief at that fixed time. A task that truly runs thirty
minutes after each close needs a calendar-aware scheduler. Do not promise either
behavior from a static UTC cron. This package ships no installed automation.
