---
name: idea-generation
description: Sources investment ideas — thematic sweeps and screens that surface candidate names with a thesis hook, checked against what the portfolio already holds. Use for "find ideas", "screen for", "what looks interesting", "pitch me something", or "what else expresses this theme".
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Idea Generation

Surfaces three to five candidate names, each with a one-line thesis hook and a
reason it belongs to *this* theme rather than a generic quality screen.

**An idea is not a name. An idea is a name plus a reason the market is wrong about
it.** A list of good companies is not output — good companies are usually priced
as good companies.

---

## Step 1 — Check the book first

Call `portfolio.positions` before anything else.

This changes what counts as an idea:

- A name that overlaps existing exposure is a **concentration question**, not a
  new idea. Say so and route it to `position-sizing`.
- A name that is correlated with a large holding adds less diversification than
  its weight suggests (`methodology/risk-measures.md` §4). Flag it.
- The most valuable idea is often one that expresses a view the user already holds
  through an exposure he does not yet have.

## Step 2 — Start from a structural claim

Every sweep begins with a falsifiable statement about the world, not a screen:

> "Enterprises are moving inference on-premise, which shifts spend from hyperscale
> capacity to owned hardware."

Then: **who is on each side of that?** A theme with no losers is not a structural
change; it is a description.

## Step 3 — Build the candidate list

Two directions, both needed:

- **Top-down** — from the theme to the names that express it. Catches the
  non-obvious beneficiaries: suppliers, toll-takers, the second derivative.
- **Bottom-up** — from screens or the landscape work. Catches names the theme
  framing would have missed.

A list produced by only one direction reliably contains names everyone already
knows.

## Step 4 — Filter to the shortlist

Cut on:

1. **Is the exposure real?** Many "AI plays" have single-digit revenue exposure to
   AI. Quantify the exposure or drop the name.
2. **Is it investable?** In scope per `manifest.yaml` — US-listed, USD, liquid
   enough to exit in a normal session.
3. **Is it already priced?** The hardest and most important filter. If the theme
   is consensus and the multiple already reflects it, the idea is a momentum
   trade, and should be labelled as one rather than dressed as value.
4. **Does the book already own the exposure?** From step 1.

## Step 5 — Write the hook

For each of the three to five survivors:

| Element | Requirement |
|---|---|
| **The name** | Ticker, what it does, in one line |
| **Theme link** | The specific mechanism, with the exposure quantified |
| **The variant view** | What the market is not discounting. `methodology/research-report-standard.md` §4 |
| **The catalyst** | What re-prices it, and roughly when |
| **The kill criterion** | What would tell you the idea is wrong |
| **Overlap** | Correlation with what the user already holds |

**No hook without a variant view.** "Good company, growing fast, reasonable
multiple" is not an idea — it is a description that thousands of analysts share,
which is precisely why it is in the price.

## Step 6 — Hand off

The shortlist is a **research queue**, not a buy list. Each survivor goes to
`model-builder` for valuation, or to `earnings-reviewer` if the question is about
the current quarter. Sizing and the decision belong to `portfolio-analyst` under
`policy/execution.md`.

## Guardrails

- **You do not recommend purchases.** You surface candidates with hooks.
- **Cite the exposure.** "Meaningful exposure to X" without a number is a claim
  about a company you have not checked. `policy/data-integrity.md` §1.
- **Say when the idea is crowded.** Positioning is part of the analysis. An idea
  everyone already owns has a different risk profile regardless of its merits.
- **Do not confuse a theme with a thesis.** The theme is why the sector matters.
  The thesis is why *this name* is mispriced.
- **Present the case against.** For each shortlisted name, one line on the
  strongest argument for not owning it. If you cannot construct one, you have not
  researched it enough to propose it.
