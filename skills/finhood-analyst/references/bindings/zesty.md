# Zesty — analysis and interactive-order mapping

## Connection

Each user connects their own account in Claude's connector settings and signs in
through Zesty's authorization window. Official public MCP endpoint:
`https://mcp.zestyfinance.com/mcp`.
No account credentials or custom intermediary are provided by Finhood Analyst.

## Discover before use

The names below are candidate mappings documented by the original package, not
a current tool-schema certification. Read the actual exposed tool descriptions
and parameter schemas each session. Prefixes may differ by host. Resolve by tool
purpose plus schema, not a guessed prefix. Never call an unsupported parameter or
infer missing fields. Fail clearly if a response does not support the analysis.

| Capability | Candidate tool | Validation |
|---|---|---|
| `market.clock` | `get_market_status` | US market; timestamp, status and calendar fields |
| `portfolio.balance` | `get_balance` | US/USD; distinguish cash, investments and buying power |
| `portfolio.positions` | `get_positions` | US/USD; empty positions are valid |
| `portfolio.history` | `get_portfolio_history` | Allowed period enum, timestamps and cash-flow treatment |
| `portfolio.transactions` | `get_movements`, `get_orders` | Movement currencies, external flows vs fills; pagination completeness |
| `portfolio.dividends` | `get_dividends` | Currency, date, gross/net definitions and pagination |
| `market.quote` | `get_asset_details` | Symbol, currency, timestamp and quote basis |
| `order.list` | `get_orders` | Read only; include relevant open and closed orders |

Set the market to US where the live schema supports it. Never assume a movement
endpoint is USD-filtered when it has no market field. Keep mixed currencies
separate; if USD external flows cannot be isolated, returns are unavailable.

For the first connection check use only market status, balance and positions.
Do not publish the response as a test fixture. Record pass/fail and field names
only in any maintenance report, never balances or account identifiers.

## Coverage checks inherited from the original mapping

Recheck these against current schemas/responses before depending on them:

- `get_orders` previously used `status: all` for closed orders and `status: pending`
  for open orders. Do not assume one result covers both. Follow current docs.
- `get_movements` previously could not paginate `type: all`. If explicit deposit
  and withdrawal queries are necessary, fetch both to completion. Incomplete
  history makes cash-flow-adjusted performance unavailable.
- A retry must be bounded: on a rate-limit response respect its retry interval,
  attempt at most twice, then report unavailable. Do not retry indefinitely.
- Do not treat an empty list as authorization to fetch a different account.

## Unsupported data

This package does not assume Zesty provides benchmark returns, risk-free history,
per-symbol return series, consensus estimates or company fundamentals. Discover
what is actually available; otherwise use public primary sources or mark missing.
Sharpe needs a valid portfolio return series and matched risk-free returns; a
market index is additionally needed for beta, Jensen alpha and market comparison.

## Optional interactive orders

See `policy/order-workflow.md`; analysis never invokes this path automatically.
Observed tool descriptions on 2026-09-27 include `get_us_trade_options`,
`apps_preview_us_order`, `apps_confirm_us_order`, `preview_us_market_order`,
`preview_us_limit_order` and `confirm_us_order`. Prefixes and host availability
can differ. Interactive preview cards require MCP Apps rendering support.
The apps confirmation is tied to the user's button press; plain-text confirmation
submits after conversational approval, without an additional mandatory window.
Preview IDs are documented as valid for about two minutes; respect actual expiry.
Host policy can prohibit either path. Availability is not authorization.

FX, transfers, cancellation, complex orders, crypto, account changes and feedback
remain excluded. Headless use requires a host-enforced read-tool allowlist.

## Evidence

Endpoint and user-owned authentication verified against Zesty's official guide on
2026-09-27. Core order-tool descriptions/schemas were inspected in the maintenance
environment; market-clock read succeeded. Claude rendering, account reads and
order behavior remain unverified. No order previews or submissions were tested.
No live account payload is included in this package.
