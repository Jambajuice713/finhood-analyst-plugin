# Private state

State is optional for one-off analysis. A baseline exists only if it is actually
available and belongs to the same user, account context, currency and period.
Do not reuse state from another user or assume memory survives a new chat.

Use `schemas/portfolio-snapshot.json` for an optional exported snapshot and
`schemas/watch-list.json` for a private watch list. A per-symbol thesis may be a
private `view-<SYMBOL>.md` file. Omit brokerage account IDs, credentials and tokens.

Ask for a private output destination when persistence is required. Use an opaque
local workspace label chosen by the user to prevent mixing account contexts;
never use a real account number as the folder name. Do not write into the installed
skill, source checkout or a shared/public folder. `.gitignore` is a last safeguard,
not proof that a storage location is private.

If storage is absent, report "No baseline available; this is a point-in-time
review" and offer a download when the host supports it. Say whether the write
actually succeeded. Scheduling additionally requires verified durable storage.

If a snapshot has `session_confirmed: false`, it is an observation, not a certified
market-close baseline. If old or conflicting, show its date and limitation.
Do not silently overwrite a conflicting baseline. A later user can explicitly
resolve the discrepancy and authorize a new private baseline.
