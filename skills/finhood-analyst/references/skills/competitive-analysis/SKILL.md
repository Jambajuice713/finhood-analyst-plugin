---
name: competitive-analysis
description: Competitive landscape — who the players are, how they are positioned, what they compete on, and where the moats actually are. Use for "who are the competitors to X", "benchmark X against peers", "build a market map", or any systematic evaluation of competitive dynamics. Produces the landscape half of §3 of the research report standard.
---

**Public-edition preflight:** follow `policy/execution.md` and the parent Finhood Analyst entry skill.
This analytical procedure is read-only. Private state is optional for a one-off run.
An explicit subsequent order request routes separately to `policy/order-workflow.md`.
Use available data and explicit gaps; user limits override illustrative examples.
For a research-only question, a brokerage connection is not required. References
to other agents mean task roles; work in the current session if no delegation
mechanism exists.


# Competitive Analysis

Maps the players and answers one question per name: **what, if anything, protects
their economics?**

---

## Method

### 1. Map the field

For each player in the bounded universe:

| Company | Position in chain | Share (or proxy) | Basis of competition | Recent moves |
|---|---|---|---|---|

Where market share is not disclosed, use a proxy — revenue in the segment, unit
volume, installed base — and **name the proxy**. A share estimate with no stated
basis is a guess wearing a table's clothing.

### 2. Identify the basis of competition

What actually decides who wins a customer here? Price, performance, distribution,
switching costs, ecosystem, regulation, brand. Usually one dominates, and it is
often not the one management talks about.

### 3. The moat question, answered concretely

`methodology/research-report-standard.md` §3 names three paths to durable
advantage: **strength of brand, cost leadership, and access to protected
technology or resources.** Buffett's framing — economic castles protected by
unbreachable moats — is the standard being applied.

For each material player, answer three things:

1. **Is there a moat?** Name it as one of the three, or say there is none.
2. **What is the evidence?** Pricing power sustained through a downturn, margins
   durably above the peer set, retention that holds when a cheaper alternative
   appears. Assertion is not evidence.
3. **What would breach it?** Every moat has a solvent. Name it.

**"No moat" is a finding, and often the most valuable one in the note.** Most
companies do not have one. A landscape where every player has a moat is a
landscape where the word has been used decoratively.

### 4. Recent moves

Capacity additions, pricing actions, M&A, entries and exits, capital raises. These
are the revealed strategy, and they are usually more informative than the stated
one. A company adding capacity into a soft market is telling you what it believes.

### 5. Where the structure is heading

Consolidating or fragmenting? Is the profit pool moving between links in the
chain? Who is positioned for where it is going rather than where it has been?

## Structural considerations to check

From `methodology/research-report-standard.md` §3, the items the research standard
names explicitly and that are easy to skip:

- **Production capacity levels** — and utilisation. Capacity coming online is the
  most reliable predictor of pricing pressure.
- **Pricing** — direction, and whether it is holding.
- **Distribution** — who controls access to the customer.
- **Stability of market share** — share that has been stable for a decade means
  something structurally different from share that moved last year.

## Guardrails

- **Issuer materials are promotional.** A company's competitive positioning slide
  is a fact about its self-presentation. Extract, never adopt.
  `policy/data-integrity.md` §3.
- **Do not confuse scale with a moat.** Being large is not protection unless it
  produces a cost or network advantage that a competitor cannot replicate with
  capital.
- **Do not confuse growth with advantage.** Fast-growing companies in structurally
  bad industries are common and rarely end well.
- **Symmetry.** Apply the same standard of evidence to the name the user holds as to
  the ones he does not. Asymmetric scepticism is how confirmation bias enters a
  research process.

## Output

The landscape section of the note, plus the validated peer set that
`comps-analysis` will spread. A peer set assembled here on structural grounds is
worth more than one assembled from a screen.
