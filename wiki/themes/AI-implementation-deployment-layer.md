---
type: theme
tickers: [ACN, IBM, EPAM, GLOB, CTSH, INFY, PLTR, CRM, MDB, DDOG, PANW, OKTA, CRWD, ZS]
last_updated: 2026-06-13
---

# AI implementation & deployment layer — who gets paid to put AI into production

*Anchor source.* This page is anchored on a single Tier 3 commissioned research synthesis (`raw/research/ai-implementation-deployment-layer.md`, June 2026). Per the Tier 3-anchored theme convention (CLAUDE.md Section 3.13): the analytical framework is paraphrased in wiki voice; company figures are reproduced as reported in the anchor with the anchor's own evidence labels (**a** = disclosed in filing/release, **b** = management claim/metric, **c** = announcement/marketing); the Open questions section pre-registers the triggers future primary-source ingests test. A Phase 0 spot-verification round was run at construction on six load-bearing claims (results in Source audit notes — one anchor claim falsified, two variances flagged). Living document.

**Theme type:** dynamics. **Scope note:** the vault's second application-layer page, with the same demand-side justification as [[software-AI-moat-durability]] — the capex funding the vault's chokepoints is only justified if AI value is captured downstream. The two pages ask different questions and never share a verdict: that page asks *which incumbent software moats survive AI* (durability verdicts live there); this page asks *who gets paid to move AI from models into production* (chain-link monetization verdicts live here). Names on both pages carry one verdict of each kind, never two of the same kind; rows marked "cross-reference only" defer durability entirely to the moat page.

## Thesis role — the null result leads

**As of mid-2026, no public company can be cleanly verified as earning more than 10% of revenue from disclosed AI-implementation work.** That null result is this page's most load-bearing finding. The deployment layer is forming *structurally* — a $25B acquisition for agent identity, an open protocol commoditizing connectors, consumption meters wired for agent traffic — but the disclosed money has not migrated. Where money is changing hands today, it is reported as **bookings and management constructs, not recognized revenue**: IBM's GenAI "book of business" passed $12.5B inception-to-date while IBM Consulting's full-year 2025 revenue grew 0.4% (IBM Q4 2025 release, Jan 28, 2026); Accenture booked $5.9B of GenAI work in FY25 against a 2–5% local-currency revenue guide. The closest thing to recognized AI-implementation revenue anywhere in the chain is Accenture's ~$1.1B/quarter "Advanced AI" line — ~6% of quarterly revenue, management-labeled (Q1 FY26 call).

The honest framing: this page is a **map with mostly cautionary placements, plus dated instruments for catching the moment the money migrates**. It is not a list of validated positions — the validated implementation names ([[PLTR]], and the consumption leg generally) are already covered at [[software-AI-moat-durability]].

## The six-link deployment value chain

| Link | Market-structure verdict | One-line reasoning |
|---|---|---|
| 1. Integration & orchestration (iPaaS, agent frameworks, MCP) | **Contested → commoditizing** | MCP donated to the Linux Foundation's Agentic AI Foundation (Dec 9, 2025; 10,000+ public servers, 97M+ monthly SDK downloads per the ecosystem update — Tier 3/4) — the protocol layer is a public good; value migrates to governed connectors + the underlying data |
| 2. Enterprise context plumbing (vector/retrieval, catalogs, governance) | **Concentrating** | Consolidating into platform databases (MongoDB Atlas vector search ~doubled YoY) and governance acquisitions (Salesforce closed Informatica ~$8B, Nov 18, 2025); standalone vector DBs squeezed |
| 3. Agent identity, security & governance | **Concentrating — chokepoint-shaped, pre-revenue** | Identity is the natural control point for autonomous agents; PANW's ~$25B CyberArk close (Feb 11, 2026 — the largest cybersecurity acquisition ever, explicitly for "human, machine, and agentic" identity) proves strategic conviction; **zero companies disclose agent-identity or runtime-security revenue** |
| 4. Evaluation & observability | **Contested — feature-or-market unresolved** | Datadog folds LLM/agent monitoring into span-based consumption billing and declined to size its AI cohort (Q4 2025 call); a private eval cohort (Braintrust/Galileo/LangSmith-class) contests pre-production evals |
| 5. Deployment labor (SIs, FDE models, MSP/MSSP accountability absorbers) | **Fragmenting at the arbitrage end / concentrating at the accountability end** | Agentic coding compresses billable hours at labor-arbitrage SIs; the durable position is contractual accountability + regulated-market access |
| 6. Vertical implementation platforms | **Concentrating, thinly public** | Most vertical deployers are private; [[PLTR]] is the clearest public expression (ontology + embedded FDE), and the model labs are copying the FDE shape (reported lab FDE units/acquisitions — c-tier) |

**Revenue-reality ranking today** (most → least real as disclosed money): deployment labor (bookings only) → context plumbing (recognized consumption, not isolated as "AI") → eval/observability (real but unsized) → vertical platforms (real but not broken out) → agent identity (strategically validated, $0 disclosed) → integration/orchestration (open standard; least monetized).

## Core thesis (falsifiable)

**Value in the deployment layer concentrates at accountability-absorbing positions and governed-context control points paid on consumption or outcome meters — and commoditizes at labor-arbitrage and open-protocol positions** (anchor §1–2). The thesis fails per the five lane-level conditions in "What would prove this framing wrong" below — most directly if model providers absorb the tooling layer, or if enterprise AI spend never migrates beyond tokens and infrastructure.

## Company scorecard

Figures as reported in the anchor (evidence labels a/b/c; periods per anchor §3); Phase 0 corrections applied where flagged. Names with vault pages are linked; "x-ref" rows defer durability verdicts to [[software-AI-moat-durability]].

| Company | Link(s) | Billed unit | AI-implementation revenue evidence | Chain verdict | Top risk | Single falsifier |
|---|---|---|---|---|---|---|
| Accenture (ACN) | 5 | Project + managed-services hours | GenAI bookings $1.8B Q4 FY25 / $5.9B FY25 (a); Advanced AI ~$2.2B bookings / ~$1.1B revenue Q1 FY26 (b); $865M optimization program with "non-reskillable" exits — reported headcount ranges from ~11k (at announcement) to ~22k (FY25-end coverage; Phase 0 flag) | Contested | Agentic coding compresses hours faster than AI projects scale | Advanced AI quarterly revenue stalls/declines 2+ quarters while bookings stay flat |
| IBM | 5 + 1/2 (watsonx) | Consulting signings + software ACV | GenAI book >$12.5B inception-to-date, >$10.5B of it Consulting (b; Q4 2025 release); Consulting FY25 revenue +0.4% (a). *Anchor's claim that the metric is discontinued from Q1 2026 NOT verified at primary — Phase 0 flag* | Contested | The book is signings, not revenue; conversion gap widening | Consulting segment revenue declines YoY for 2 quarters despite rising AI work |
| EPAM | 5 | Project hours | No clean AI line; FY25 revenue $5.46B +15%, net income −17% (a) | Contested → exposed | Pure engineering labor in a deflating-hours regime | Discloses an AI line >10% of revenue (upgrades), OR organic growth turns negative (confirms) |
| Globant (GLOB) | 5 + 6 | Shifting seat → token subscription | AI Pods exit-rate ARR $20.6M FY25, gross margin 45–60% vs 38% blended (b); **management guides Pods exit ARR $60–100M by end-2026** (b; Phase 0 addition); total FY25 revenue $2.455B +1.6%, Q4 −4.7% (a) | Contested → exposed | Revenue declining; Pods immaterial vs total | Pods ARR misses management's own $60–100M end-2026 guide |
| Cognizant (CTSH) | 5 | Project + managed services | No clean AI line; two >$1B "AI-era" deals (b); TTM bookings $27.8B (a) | Contested | Labor arbitrage; AI deals unquantified | Book-to-bill below 1.0x for 2 quarters |
| Infosys (INFY) | 5 | Project + managed services | 2,500+ GenAI + 200+ agentic projects, no revenue breakout (b). *Anchor's "FY26 guidance cut to 1–3%" FALSIFIED at Phase 0: FY26 guidance was RAISED to 3–3.5% CC (Jan 2026); FY27 guide 1.5–3.5% CC (cautious)* | Contested | Low-single-digit growth amid maximal AI narrative | FY27 actual CC growth lands below ~1.5% |
| [[PLTR]] | 6 + 5 (embedded FDE) | Platform subscription + bundled deployment | Q1 2026 revenue $1.633B +85%; US commercial $595M +133%; FY26 guide ~$7.66B (a; consistent with the vault's S114 baseline). No FDE/services breakout (a — structural disclosure gap) | **Durable** (the chain's only one) | Expectations + concentration; durability verdict at the moat page | US commercial growth below ~40% YoY for 2 consecutive quarters |
| Salesforce (CRM) — x-ref | 1/6 (Agentforce surface) | Consumption ($2/conversation, ~$0.10/action) | Agentforce ARR $800M +169%, 29,000 deals; Agentforce+Data 360 >$2.9B (b; matches the moat page's baseline) | Contested | Consumption ramp vs seat erosion — adjudicated at the moat page | Agentforce ARR growth decelerates sharply |
| MongoDB (MDB) | 2 | Consumption (Atlas) | Q4 FY26 revenue $695.1M +27%; Atlas ~72% of revenue, +29%; vector-search adoption ~doubled YoY (a/b; Phase 0-adjusted figures) | Durable (contested) | Vector commoditized by hyperscalers/pgvector | Atlas growth below ~20% while vector adoption flattens |
| Datadog (DDOG) — x-ref | 4 | Consumption (LLM spans) | LLM Obs >1,000 customers, spans +10x in 6 months (b); **declined to size the AI cohort** (Q4 2025 call) | Contested (feature-or-market) | AI observability may not be separable | Discloses AI cohort >10% of revenue (would confirm separability) |
| PANW — x-ref | 3 | Platform ARR | CyberArk closed Feb 11, 2026, ~$25B, "human, machine, and agentic" identity (a; Phase 0 confirmed); CyberArk standalone FY25 ARR $1.44B +23% (a); no agent-identity revenue line (a) | Concentrating | Integration debt; agent-identity TAM still rhetorical | 2+ years with no disclosed agentic-identity ARR contribution |
| Okta (OKTA) | 3 | Per-user + new-product uplift | "Okta for AI Agents" GA Apr 30, 2026 (c); CEO: agentic AI is "not billions of dollars of token spend right now, it's plumbing" (b, CNBC May 28, 2026); no agent revenue line (a) | Contested | Hyperscaler-native agent identity embeds the capability | Discloses material AI-Agents ARR (>5% of total) — upgrades the verdict |
| CrowdStrike (CRWD) — x-ref | 3/4 | Module ARR | Charlotte AI AgentWorks launched Mar 2026 (c); no disclosed agent-security ARR (a) | Contested | Bundled, not separately monetized | Discloses standalone agent-security ARR |
| Zscaler (ZS) — x-ref | 3 | ARR / consumption | "AI Security" a named pillar, unquantified (b); SPLX acquired (c) | Contested | Pillar rhetoric, no disclosure | Discloses AI-security ARR breakout |

## Honest counterpoints — where the implementation story does not hold up

- **Bookings ≠ revenue is the lane's central deception.** IBM's GenAI book grew $5B → $12.5B across 2025 while Consulting revenue grew 0.4%; Accenture pairs record AI bookings with a 2–5% revenue guide and an $865M restructuring. Bookings are accumulating faster than they convert — the gap *is* the finding.
- **The tools that create the AI projects destroy the billable hours.** The disconfirming SI cohort at primary: EPAM net income −17% (FY25), Globant Q4 revenue −4.7%, Infosys guiding low-single-digit — maximal AI narrative, deflating fundamentals. (The anchor's Accenture market-cap-drop reference is price action — signal only, not weighted.)
- **Agent identity is the chain's biggest hype-vs-disclosure gap:** ~$25B of M&A conviction against zero disclosed agent-identity revenue, with Okta's own CEO calling it "plumbing for the next five and ten years."
- **AI observability may never be a separable market** — Datadog's bundling into span billing plus its refusal to size the cohort cut both ways, and structurally undercut standalone eval pricing.
- **MCP commoditized the layer it was meant to monetize.** An open Linux Foundation standard makes connectors a public good; the "iPaaS gets paid for agent integration" thesis is weakened by the standard's success. Value migrates to governed data and identity.

**Two meta-observations (monitoring, not conventions):** (1) *metric-retirement as disclosure signal* — the anchor claims IBM is retiring its GenAI book metric; unverified at Phase 0, but if any company retires its headline AI metric, that is kin to the vault's cross-venue disclosure-quality patterns and worth logging when observed at primary. (2) *Model-provider encroachment* — reported lab FDE units and enterprise-deployment ventures (c-tier, "reportedly") would make the implementation layer's suppliers its competitors; tracked at lane falsifier #1.

## What would prove this framing wrong (lane-level)

1. **Model providers absorb the tooling layer** — native agent platforms, connectors, and lab FDE units capture deployment; independent orchestration/eval/identity tooling never reaches disclosed scale.
2. **Enterprise AI spend stays in tokens/infra** — dollars never migrate to the deployment/governance layer (Okta's "not billions of token spend" is consistent with this risk *today*).
3. **SI hours deflate faster than AI projects grow** — SI revenue (not just bookings) declines; partially visible already at the disconfirming cohort.
4. **In-housing wins** — agentic dev tools invert today's vendor-success advantage (MIT NANDA: vendor-built ~2x success vs internal, ~5% of pilots reach rapid P&L impact — Tier 3, attributed).
5. **The pilot-to-production gap never closes** — the ~95% stall rate persists and AI budgets get cut before bookings convert.

## Open questions / verification triggers

**Primary-source ingest candidates:** **MDB** + **DDOG** (first-canonical queue — the two consumption-metered names whose figures this page currently carries at Tier 3); ACN optional later as the bookings→revenue conversion test case (counterpoint-role inclusion per Section 2.1).

**Dated triggers (next 2–4 quarters):**
1. **Accenture Q3 FY26 (~late June 2026 — imminent):** does Advanced AI quarterly revenue (~$1.1B base) climb, and does total revenue accelerate? The chain's single best bookings→revenue conversion test.
2. **IBM Q2 2026 (~July):** Consulting revenue inflection or continued sub-1% growth; resolve the metric-discontinuation question at primary (Phase 0 flag).
3. **Salesforce Q1–Q2 FY27:** Agentforce ARR past $800M; consumption-vs-seat adjudication (shared trigger with the moat page).
4. **Datadog FY26 quarters:** any AI-cohort disclosure — the separability test.
5. **Okta FY27 + PANW post-CyberArk reporting:** first disclosed agentic-identity ARR anywhere = the chokepoint's pre-revenue status ends; the page's most important single upgrade trigger.
6. **Globant 2026:** Pods ARR vs management's own $60–100M exit guide.
7. **PLTR Q2 2026** (guide $1.797–1.801B): US commercial momentum (shared with the moat page's validation baseline).

## Source audit notes

- **Anchor provenance.** Single Tier 3 commissioned synthesis (June 2026), built to a vault-specified brief (a/b/c revenue labels, per-name falsifiers, disconfirming cases, no valuation arguments). Source appendix in the anchor tiers all load-bearing claims; vendor-marketing items (Boomi TEI study) and press-tier items flagged there and excluded from scorecard verdicts here.
- **Phase 0 spot-verification (2026-06-13, six checks).** CONFIRMED: PANW/CyberArk close (Feb 11, 2026, ~$25B, agentic-identity rationale); IBM $12.5B book + >$10.5B Consulting GenAI signings; ACN $5.9B FY25 GenAI bookings + $865M program + Advanced AI ~$1.1B quarterly revenue; MDB Q4 FY26 $695.1M +27% (Atlas adjusted to ~72% of revenue, +29%); GLOB Pods ARR $20.6M (+ management's $60–100M end-2026 guide added). **FALSIFIED (documented per Section 4.4):** the anchor's "Infosys FY26 guidance cut to 1–3% CC" — Infosys *raised* FY26 guidance to 3–3.5% CC (January 2026); the cautious figure is the FY27 guide (1.5–3.5%). Scorecard row corrected; the directional point (low-single-digit SI growth) survives. **UNVERIFIED (flagged):** IBM retiring the GenAI book metric from Q1 2026 (Q1 2026 release still carries consulting signings; construct status unclear); ACN headcount (~11k vs ~22k across sources — range shown).
- **Consistency with vault primary:** CRM and PLTR figures match the [[software-AI-moat-durability]] baselines (S111 anchor; S114 validation) exactly; DDOG's disclosure refusal is consistent with the disclosure-quality gap that page already documents.
- **Cross-page observation for the moat page's next refresh:** the MCP/Linux Foundation finding bears directly on that page's falsifier (iii) — open connectors narrow context moats to *governance*; flagged there, not edited now.

## Change log

- **2026-06-13 (S159 — creation):** Created as a Tier 3-anchored dynamics theme on `raw/research/ai-implementation-deployment-layer.md` (Vic-commissioned; Vic-approved two-stop build). Six-link chain map + 14-row scorecard + null-result thesis role + five lane falsifiers + seven dated triggers. Phase 0 round: 4 claims confirmed, 1 falsified (INFY guidance — corrected per Section 4.4), 2 flagged unverified (IBM metric retirement; ACN headcount). MDB + DDOG queued as first-canonical ingest candidates; inbound cross-reference added at [[software-AI-moat-durability]].
