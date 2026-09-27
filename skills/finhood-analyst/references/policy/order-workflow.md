# Interactive orders — explicit user request only

This optional workflow follows analysis in the same conversation. It is not a
recommendation to transact, a scheduled task or authority to choose an investment
for the user. Read `policy/execution.md` and `bindings/zesty.md` first.

## 1. Establish intent and host permission

A request such as "analyze MSFT" or "looks good" never starts an order. "I want
to buy it" starts clarification only if details are missing; it does not approve
a preview that has not been shown. Identify the intended US-listed stock/ETF,
side, user-selected USD amount or quantity, market/limit type, limit price where
applicable and duration. Do not invent these or silently substitute an instrument.
Ask only for missing details; do not request credentials or account identifiers.

Host restrictions override this workflow. If the host prohibits preparing or
submitting financial transactions, stop at analysis and direct the user to their
brokerage app. Do not switch to another tool or widget to evade that restriction.

## 2. Validate before preview

Discover current tool schemas. Check `get_market_status` for US, then
`get_us_trade_options` with the exact symbol and side. Follow the current tools'
market-hours rules: if closed, explain and stop; never queue an automatic retry.
Validate tradability, amount/quantity bounds, available funds or holdings as
needed. Never exchange currency, liquidate another asset or alter the amount to
make the order possible. This edition supports only simple US stock/ETF market
and limit orders. Other instruments and order types are outside this workflow.

## 3. Show the preview

Use `apps_preview_us_order` when available and the host supports its interactive
card. Otherwise use the current plain-text market/limit preview tool, only if
permitted. Market buys use USD amount; market sells use share quantity. Limit
orders use quantity and a limit price. Live schemas remain authoritative.

A preview is not an executed order. Show the returned `summaryLines`, symbol,
side, amount/quantity, order type, price conditions, fees, duration and expiry.
Do not invent a card, a button, execution price or guaranteed fill. An estimated
market-order cost is not a price guarantee. Inspect `kind` and error fields:
a success-shaped response with `kind: error` is a failure, not a valid preview.

## 4. Require approval of this exact preview

Stop after presenting the preview. Await the user's approval of the exact shown
terms. Research instructions, old blanket permissions and the initial buy request
are not this approval. Changed amount, ticker, side, type, duration, fees or price
conditions require a new preview and new approval. Expired previews likewise
require regeneration, display and approval; never reuse old approval.

With a genuine interactive card, the user presses its Confirm button; do not
simulate the click or call `apps_confirm_us_order` as if the user had clicked.
The widget's native confirmation performs the submission. Do not additionally
call the plain-text confirmation: that could duplicate the order.

With a plain-text preview, only when the host permits submission and the user
explicitly approves that preview in the conversation, use the corresponding
confirmation tool once with its returned preview ID. That tool submits the order;
there is no guaranteed further confirmation window. If the host prohibits this,
stop and offer manual completion in the brokerage app without circumventing it.

## 5. Verify outcome without duplication

Report only the returned order ID and actual status. Accepted, queued or pending
is not filled. If the result is ambiguous or times out, inspect read-only order
status before any further action. Never blindly retry submission, create a fresh
order to fix a timeout, or submit after the widget already did so. An expired or
rejected preview is not execution. On rejection explain the reason; any changed
proposal starts a new preview and approval cycle. Do not claim success on errors.

## Privacy and schedules

Keep preview IDs, order IDs and account responses in the user's private session.
Never save them to this repository, public issues, fixtures or telemetry.
Headless/scheduled runs must not load this workflow or use transaction tools.
