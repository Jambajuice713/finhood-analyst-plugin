# Capability contract

Capabilities are labels for reasoning, not registered functions. Bind them to the
tools actually exposed by the current host; never invoke a fictitious function
named `portfolio.positions`. Use `bindings/zesty.md` and `bindings/research.md`.

| Capability | Use | If unavailable |
|---|---|---|
| `portfolio.positions` | Current symbol, quantity, market value, cost basis | No live portfolio analysis; user may supply a private snapshot |
| `portfolio.balance` | Cash, investments and buying power, distinguished | Do not invent total value or weights |
| `portfolio.history` | Timestamped value history | Point-in-time composition only |
| `portfolio.transactions` | External flows and executed activity | Value change only unless absence of flows is evidenced |
| `portfolio.dividends` | Income detail | Do not invent income attribution; total account value may already include income |
| `market.quote` | Price with currency, timestamp and price basis | Use a sourced historical quote and label its date, or leave unavailable |
| `market.clock` | Market status and session timing | Do not certify a completed session without independent calendar evidence |
| `market.reference` | Comparable benchmark/risk-free series, when separately sourced | No unsupported alpha, beta, tracking error, M² or Sharpe |
| `order.list` | Read-only open/closed activity when relevant | State missing activity coverage |
| `research.web` | Host search and retrieval | Work only from supplied documents; mark freshness limitation |
| `research.news` | News through host search | No invented catalyst |
| `research.filings` | Issuer/regulator filings through host retrieval | No unsupported financial figures |
| `research.market_data` | Optional licensed provider | Build bounded comps from filings and sourced prices |
| `state.read` | User's private baseline, if actually available | One-off review; no historical continuity claim |
| `state.write` | User-selected private file/storage | Say not persisted; offer an export if supported |
| `artifact.write` | Requested report file | Return the report in chat |

The table above is the read-only analytical path. The optional interactive
`order.preview` and `order.confirm` path is defined in `policy/order-workflow.md`:
explicit request, permitted host, live schema, fresh preview and subsequent user
approval are required. Missing capabilities mean manual action in the brokerage
app, never an invented tool or approval. `order.cancel` is outside this edition.
Private report/state writes must never publish account data.

For public company research, portfolio access and persistent state are optional.
For portfolio weights, balance and positions must be observed for a compatible
timestamp and currency. Exact TWR requires cash-flow timing and valuations, not
merely a list of deposits. An unavailable capability limits the claim, not the
entire conversation.
