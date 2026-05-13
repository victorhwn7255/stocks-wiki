# CLAUDE.md — stocks-wiki

A personal research vault for AI datacenter supply chain and chokepoint analysis. You maintain the wiki; the human curates sources and asks questions.

## Descriptive language convention

When referencing frameworks, tiers, caveats, or sections in prose content, use descriptive names rather than numerical shorthand. Pair numbers with descriptive scope on first reference (e.g., "Energy/Power Tier 4 specialty component supplier scope"); descriptive name alone on subsequent references. Frontmatter YAML fields retain numerical values. Existing canonical pages from Sessions 1-45 are not retroactively updated; this convention applies to all session outputs from Session 46 onward.

## 1. Foundation

### 1.1 The anchor

`wiki/_thesis.md` is the evaluation point for everything. Every ingest, new page, update should strengthen, challenge, or refine the thesis. If an action does none, flag before proceeding. The human owns `_thesis.md` — never edit yourself. `raw/notes/frameworks.md` is similarly human-owned — frameworks are interpretive scaffolding; primary sources *enrich*, not override. When framework structures and primary-source evidence diverge, raise on the relevant page rather than silently reconciling.

**Ownership exception (codified Session 36).** Both files underwent Vic-authorized reworks via collaborative chat drafting (`_thesis.md` 2026-04-30; `frameworks.md` v10.1 2026-05-01) aligning vault scope to AI datacenter supply chain. **Default ownership convention resumes for all subsequent sessions** — agents must not propose collaborative editing without explicit Vic-authorized rework session declaration.

### 1.2 Vault scope

Current scope: **AI datacenter supply chain — compute, photonics, memory, energy, power, equipment, materials, and more.**

**Primary scope:** Multi-domain chokepoint analysis covering:
- **Compute** — GPU + CPU + custom ASIC; merchant (NVDA/AMD) and hyperscaler-captive (Trainium/TPU/Maia) silicon
- **Photonics** — lasers/EMLs/modulators, optical DSPs/PHYs, fiber/connectors, photonic foundries/packaging/test, optical assembly/CM, InP substrate/epi
- **Memory** — HBM oligopoly + commodity DRAM + NAND; HBM-logic integration via TSM CoWoS
- **Energy/Power** — transformers + GOES steel; high-density power delivery; UPS + on-site generation; switchgear + cables + busways. **Binding 2026 constraint** per _thesis.md rework — ~50% of planned 2026 US datacenter builds delayed/cancelled (Bloomberg/Sightline); 4-year transformer lead times
- **Equipment** — EUV lithography (ASML); advanced packaging metrology + test; broader semi capex
- **Materials** — GOES steel; rare earths; specialty gases; substrate supply (silicon wafers, HBM substrates, InP substrates); copper

Multi-domain framework structures: Framework 5 (photonics); F6 (memory); F7 (energy/power); F8 (equipment); F9 (materials provisional); F10 (CAPEX flow); F11 (cross-chokepoint themes).

**Cross-domain participants.** Companies operating across multiple domains carry multiple tier classifications: TSM (photonics_tier 1 + memory_tier 1 + equipment_tier 2); VRT (photonics_tier 4 + energy_power_tier 1); ETN (energy_power_tier 1; Layer 4-5 straddling per Caveat #9); MU (memory_tier 2). Multi-domain classification captures cross-cutting exposure that single-domain framing obscures.

**Outside-scope counterpoint placements:** [[COHU]] + [[PLAB]] — Outside Framework 5 (photonics) per honest-verdict canonical pair. Per frameworks v10.1, Outside Framework convention applies to Frameworks 5/6/7/8/9. Counterpoint inclusion does not expand vault scope.

**Scope expansion mechanism.** Vault scope under ongoing expansion with sequencing per opportunity (source availability, thesis development, time-bounded events) rather than rigid pre-codification. Active candidates: ETN (F7 Tier 1); MU (F6 Tier 2); MPWR/VICR (F7 Tier 3); foreign-issuer per Section 4.2. Domain-specific Tier 3 framework sources Vic-curated as expansion proceeds. *See A.1.*

### 1.3 Structure

**Knowledge layers:**

```
raw/         # source material — read from, never modify
  filings/ transcripts/ research/ news/ notes/
wiki/        # your domain — write, update, interlink
  _thesis.md companies/ layers/ chokepoints/ themes/ relationships/
index.md     # catalog of wiki pages
log.md       # append-only record of activity
```

**Operational layers:** `prompts/` + `scripts/`. Operational infrastructure, not vault content. Never ingest from these directories.

The `raw/notes/` folder contains human's prior conversations and framework notes. Analytical frameworks treated as authoritative until human revises (primary sources enrich, not refute). Factual claims from notes treated as working hypotheses; confirm or revise against primary sources.

**Claude Code operational memory.** Persistent memory file at `~/.claude/projects/.../memory/MEMORY.md` outside vault. Single purpose: cross-session context continuity (compressed mirror of `log.md`, structural notes, conventions). Must not contain independent analysis affecting wiki pages without Stop 1/Stop 2 protocol. Not in `index.md`/`log.md`; updates do not count for accounting.

**Path discrepancy verification.** Verify path conventions before committing new vault paths. Skill directories use hyphens (`.claude/skills/agent-onboarding/`); raw subdirectories use no separators (`raw/filings/`). File location: skill files → `.claude/skills/<skill-name>/SKILL.md`; reference docs → `raw/references/`; session prompts → `prompts/`; Vic-authored synthesis → `raw/notes/`. *See A.2 for empirical evidence.*

## 2. Discipline

### 2.1 Four disciplines

**Host tensions honestly.** When the human holds a position and the wiki's analysis suggests weak structural fit, the page states this plainly. Uncomfortable conclusions are the point of the wiki, not a bug.

**Describe, don't recommend.** Pages analyze structural position, competitive dynamics, evidence. They do not prescribe buying, selling, or holding. "Should I sell X" gets reframed to "what would have to be true for X's thesis to still be intact."

**Thesis tool, not portfolio tracker.** No P&L, no position sizes, no cost basis, ever. A reader should not be able to tell what the human owns from reading the pages.

**Honest-verdict discipline.** When a company's thesis fit is weak, the page states the weak fit plainly rather than constructing thesis-relevance narratives from generic positioning. Weak-fit pages may be shorter and more verdict-like. Inclusion may be for trajectory or counterpoint rather than thesis centrality. Surface clearly in Thesis role.

### 2.2 Source hierarchy

When sources disagree on facts, higher tier wins. On interpretation, triangulate and flag the disagreement on the relevant page.

- **Tier 1 — Primary filings:** 10-K, 10-Q, 20-F, 8-K, proxies. Ground truth.
- **Tier 2 — Primary commentary:** Earnings calls, analyst days, conference appearances. Rich for thesis work; colored by management incentives.
- **Tier 3 — Independent analysis:** SemiAnalysis, Stratechery, reputable sell-side, industry reports. Cite, don't treat as fact.
- **Tier 4 — News:** Bloomberg, WSJ, Reuters, FT. Reliable for events, shallow on thesis.
- **Tier 5 — Social/forums:** Twitter/X, Reddit, blogs. Signal for generating questions; never cited.

Skip promotional content and aligned commercial incentive.

*Tier 1/Tier 2 calibration.* Factual data (financials, customer concentration, capacity, legal, geographic) — Tier 1 authoritative. Competitive assessment, strategic intent, management signaling — Tier 2 can be more analytically informative than Tier 1's legal-conservative framing.

*Analyst silence as signal.* When a structural risk or opportunity is disclosed in some venue but unaddressed in others (analyst Q&A), the asymmetry is meta-signal about investor community processing. Document in Source audit notes; elevate if thesis-central.

*Source unavailability as observation.* When an expected source is unavailable (call PDF missing, wrong-period file, paywalled), document explicitly with analytical implications. Inability to test patterns requiring that source is itself a finding.

## 3. Page conventions

### 3.1 Page types and creation triggers

Page types: companies / chokepoints / themes / relationships / layers.

A new page exists because a source informed it, not because a company name came up. Companies not in seed portfolio: first mention gets a note inside primary page; promote to own page when entity referenced by 3+ sources or central to identified chokepoint/theme. Never create empty stub pages.

**Filenames.** Companies use uppercase tickers (`TSM.md`). Chokepoints / themes / relationships use kebab-case (`TSMC-CoWoS.md`, `CPO-platform-battle.md`, `TSM-NVDA-allocation.md`). Layers use `layer-N-description.md`.

### 3.2 Frontmatter

```yaml
---
type: company | chokepoint | theme | layer | relationship
tickers: [TSM, NVDA]
layer: 1-6                          # company pages only — value capture layer
photonics_tier: 1-5 | outside       # company pages with photonics exposure
memory_tier: 1-5 | outside          # company pages with memory exposure (optional)
energy_power_tier: 1-5 | outside    # company pages with energy/power exposure (optional)
equipment_tier: 1-5 | outside       # company pages with equipment exposure (optional)
materials_tier: 1-5 | outside       # company pages with materials exposure (optional; provisional)
foreign_issuer: true                # company pages only — non-US-domiciled filers
last_updated: YYYY-MM-DD
---
```

`layer` (Framework 2) and per-domain `*_tier` fields (Frameworks 5/6/7/8/9) distinct from source `Tier`. Multiple `*_tier` fields apply to multi-domain companies (TSM photonics_tier 1 + memory_tier 1 + equipment_tier 2; VRT photonics_tier 4 + energy_power_tier 1; ETN energy_power_tier 1).

For multi-layer exposure, single primary `layer` value reflecting thesis-relevant placement; nuance in body prose. For non-company pages, `tickers` lists tickers whose primary sources substantively informed page content (provenance, not relevance tag).

**Frontmatter convention reinforcement (codified Session 46).**

(a) **`foreign_issuer: true` field.** Apply on company pages for non-US-domiciled filers (foreign private issuers + MJDS Canadian filers). Empirical motivation: Session 43 CCJ first vault application. Field absent on US-domiciled filers (default).

(b) **`tickers` field convention.** Single-ticker scope on company pages (`tickers: [TICKER]`); multi-ticker scope on chokepoint / theme / relationship pages where multiple tickers' primary sources substantively informed page content. Empirical motivation: Session 44 HALEU-fuel-chokepoint precedent (`tickers: [LEU, BWXT, CCJ, BE, GEV]` — provenance, not relevance tag).

(c) **`*_tier` field application discipline.** Apply per-domain tier field only when company has substantive exposure to that domain — not derivatively (e.g., do not assign memory_tier to NVDA solely because NVDA buys HBM; do assign memory_tier to MU/SK Hynix/Samsung as memory-domain operators). `outside` placement is honest-verdict-correct per Section 3.10 four-criterion test when source evidence shows weak fit. Empirical motivation: Session 36 FLEX cross-domain placement (Layer 6 + photonics_tier outside + energy_power_tier 5 + equipment_tier outside).

### 3.3 Voice, wikilinks, citations

**Voice.** Analytical third person. No first/second person, no investment prescriptions.

**Wikilinks.** Short form `[[TICKER]]` or `[[page-name]]`. Every ticker/chokepoint/theme mention gets linked. Pages do not wikilink to themselves. Forward wikilinks acceptable; do not create stub pages just to resolve them. Add at least one inbound link from existing page when creating a new page.

**Citations.** Every numerical claim and non-obvious substantive claim names source and period — e.g. *CoWoS capacity expansion (TSM Q1 2026 call)*. Per-claim citations remain correct as pages accumulate multi-source content; do not substitute header-level citation notes.

*Rhetorical vs. factual.* Factual claims (verifiable numbers, confirmed events) paraphrased in wiki voice with citation. Rhetorical claims (directional assertions, promotional framing) attributed to speaker — "Jensen claimed...", "management characterized...". When in doubt, attribute.

*Multi-provenance.* Claim provenance explicit when synthesizing across sources. Source audit notes + Change log track overall page provenance; cross-source synthesis statements name all involved sources.

*Disclosed/inferable/unknown.* For unnamed entities ("Customer A," "a significant customer"): (1) Disclosed — exact data from filing; (2) Inferable — patterns matching publicly known profiles, hedged language only ("consistent with," "resembles"), never assertive; (3) Unknown — what filing does not disclose.

*Disclosure lifecycle awareness.* Topics may appear in management commentary (Tier 2) before regulatory filings (Tier 1). Same-day divergences are meta-signal about disclosure lifecycle. Document in Source audit notes when observed.

### 3.4 Tier 1/Tier 2 framing gap convention (A4)

Distinct from Disclosure lifecycle awareness. Covers cases where Tier 1 filing and Tier 2 earnings call treat the same risk or commercial topic with materially different framing. Pattern types: (a) filings flag risk that calls dismiss; (b) filings omit commercial detail that calls disclose extensively; (c) filings acknowledge margin compression risk that calls dismiss with rhetorical deflection.

Document prominently in Source audit notes with "Tier 1/Tier 2 framing gap" label. Pattern instances compound; three or more becomes analytically significant beyond any individual disclosure.

**Sub-pattern annotation (3 core sub-patterns):**
- **Risk-framing gap:** Risk in 10-K Risk Factors but dismissed/minimized in call.
- **Customer-concentration gap:** Customer concentration in 10-K Notes but not addressed on call.
- **Geographic-concentration gap:** Geographic concentration in 10-K MD&A or Item 1 but not addressed in call.

Sub-pattern annotation supplements running count threshold. Current count canonical in `MEMORY.md` and recent log entries. *See A.3 for empirical evidence.*

### 3.5 Counterparty-attribution-only annotation (A1 three-mode framing)

When Tier 3 sources cite counterparty-side announcements about ecosystem partnerships, wiki text annotates cross-validation status per three-mode framing:

- **Over-claim:** counterparty-side announcement not bilaterally confirmed. Annotate: *"named in [counterparty] [venue]; not reciprocally confirmed in [target] primary sources."*
- **Inversion:** counterparty-side projection structurally misdirected. Annotate: *"characterized as [framing X]; [target] primary-source disclosure shows [framing Y]."*
- **Reciprocal-confirmation:** counterparty-side claim bilaterally confirmed. Annotate: *"named in [counterparty] [venue]; reciprocally confirmed in [target] primary sources [citation]."*

Apply at first instance during Tier 3-anchored theme page construction; refine at primary-source ingest cross-validation. *See A.4 for canonical examples.*

### 3.6 Cross-venue disclosure gap convention (A4-bis)

Distinct from Tier 1/Tier 2 framing gap. Addresses divergence between two non-filing venues — typically conference vs near-concurrent earnings call. Pattern: information selectively disclosed at one venue (industry conference, GTC keynote, technology day) but not addressed at adjacent earnings calls. Currently 2 observations; third instance triggers convention codification refinement.

### 3.7 CEO combativeness as Tier 2 meta-observation (monitoring)

When CEO responds to structurally reasonable analyst questions with unusually defensive or dismissive language beyond standard corporate deflection, note in Source audit notes as potential indicator of which competitive pressures are most acutely felt. Descriptive, not diagnostic. Document exchange with exact wording per rhetorical claims convention; do not adjudicate underlying cause. Status: monitoring pending third instance (currently 2: MRVL.md + AVGO.md).

### 3.8 Source audit notes + Change log

**Source audit notes.** Standard section on every company page created or substantively updated from a primary source. Optional on theme/chokepoint pages. Captures observations about the source itself — management tone shifts, analyst framing, conspicuous absences, unanswered questions, what went unquantified. Place before Change log. For multi-source pages, maintain per-source entries (dated, source-attributed).

**Change log.** At bottom of each page. Track what was added/changed in each ingest with dated line. Makes staleness and evolution visible at a glance.

**Brevity discipline (codified Session 38).** Change log entries, source audit notes per-source entries, and log.md session entries must be SHORT and CONCISE — operational essentials only. **Targets:** 1-3 sentences for change log entries; 2-5 sentences for source audit notes per-source entries; ~15-25 lines for log.md session entries per Session 35 reduction precedent.

**Goes in:** date + session number; what was created/updated; canonical placements applied (layer + tier); convention codification observations; one-line key finding if structurally significant.

**Does NOT go in:** Phase 4 reflection content; multi-paragraph analytical synthesis; cross-company analytical product detail; full source audit notes content; convention text quotations; per-instance empirical evidence; full Stop 1 deliverables enumeration; A1 three-mode application detail.

**Rationale:** Canonical analytical content lives in Thesis role + middle sections + Open questions. Change log + source audit notes + log.md track *what changed* and *operational essentials*, not *what the analysis was*. Phase 4 reflection content belongs in chat session deliverables, not vault change logs. **Application:** prospective from Session 38+; existing oversized entries (notably FLEX.md Session 36) NOT retroactively trimmed; future ingest sessions may compress legacy entries IF incidental to substantive scope, NOT as standalone trim work.

### 3.9 Company page structure

Five sections universal: Thesis role, Financial snapshot, Open questions, Source audit notes, Change log. Middle sections (technology roadmap, capacity, ecosystem, demand, competitive positioning, supply chain) vary by company type and layer. Do not force a rigid universal template; structure follows analytical significance. *Layer 4 differentiation + Layer straddling tension: see A.5.*

### 3.10 Outside Framework placement (per-domain generalization)

`<framework>_tier: outside` is honest-verdict-correct designation when source evidence shows weak fit on a specific per-domain framework. Applies to Frameworks 5 (photonics), 6 (memory), 7 (energy/power), 8 (equipment), 9 (materials) per frameworks v10.1 generalization.

**Placement decision criteria (per-domain).** Apply same four-criterion test to whichever per-domain framework. Canonical (Framework 5):
1. ZERO domain-specific customer disclosure (photonic foundry / IC / SiPh for F5; named hyperscaler / datacenter-power for F7).
2. Domain mentions appear as broad market enumeration rather than named served segments.
3. AI exposure is broad-cycle subsegment rather than domain-direct.
4. Customer concentration is generic rather than domain-specific.

For other frameworks (6/7/8/9), substitute domain-specific equivalents per criterion 1.

**Multi-domain Outside placement.** A single company may carry Outside placement on multiple per-domain frameworks simultaneously (e.g., COHU is Outside Framework 5 + Outside Framework 8). Multi-domain Outside strengthens honest-verdict-correctness — structural fit is weak across multiple domain assessments.

**Counterpoint role framing.** Vault inclusion is for trajectory (broad-cycle exposure with AI subsegment driver) or counterpoint (analytical reference via contrast — e.g., equipment-tier split between structurally AI-exposed [[AEHR]]/[[ONTO]]/[[VIAV]] and broad-cycle [[COHU]]/[[PLAB]]) rather than thesis centrality.

**Cross-reference discipline.** Outside-placed companies excluded by default from theme-page Future ingest candidates lists where theme is domain-specific to that framework. Outside placement justification subsection within Thesis role documents rationale per four-criterion test.

**Promotion mechanism.** Outside → Tier 4 promotion warranted when source evidence surfaces domain-specific structural exposure meeting per-framework triggers. Framework 5 canonical: 2+ photonic foundry customers disclosed by name; OR >15% revenue attributable to photonics; OR domain-specific triggers pre-registered in Open questions. For other frameworks, substitute domain-specific equivalents. *See A.5 for COHU + PLAB canonical pair (Framework 5 + Framework 8 dual-Outside).*

### 3.11 Displacement analysis

When a company's core business faces structural displacement from a tracked technology transition (e.g., pluggable transceiver assembler facing CPO displacement), a dedicated displacement analysis section may be warranted. Surface: structural tension, management's threat framing (silent / reframed / acknowledged), analyst coverage patterns, displacement vulnerability factors, timing gaps vs. adjacent companies. Optional — add only when displacement is thesis-central.

### 3.12 Theme page types

Three types from practice: **Dynamics themes** (evolving competitive/market dynamic; e.g., `AI-demand-durability.md`, `foundry-competition.md`); **Mechanism themes** (how a company maintains/challenges structural position; e.g., `NVDA-platform-integration.md`); **Absence themes** (thesis-significant topic primary sources are not yet addressing; e.g., `CPO-platform-battle.md`). Future ingests may surface other legitimate page types.

### 3.13 Tier 3-anchored theme pages (A2)

A theme page may be anchored on Tier 3 synthesis sources when primary-source-anchored creation is premature but cross-cutting analytical content exists. Structural requirements: (1) Vic-authored synthesis as anchor with attribution explicit in body and frontmatter; (2) Counterparty-attribution-only annotation per three-mode framing (Section 3.5); (3) No-verification at construction; deviation-based refinement at ingest; (4) Open questions section pre-registers primary-source verification triggers.

**Multi-domain Tier 3 sources.** Existing canonical: `raw/research/photonics-chokepoint-table.md`. Additional Tier 3 sources anticipated for memory, energy/power, equipment, materials — Vic-curated as expansion proceeds; new sources may anchor theme pages per same A2 conventions. *See A.6 for canonical example.*

### 3.14 Paired ingests

When two companies sit at adjacent positions in the value chain, paired ingest covers both in single session. Use when: thesis roles structurally similar; paired comparison generates content not available from either source alone; source period alignment reasonable. Two-stop protocol typically warranted; middle sections allowed to differ.

**Variant: parallel-but-independent paired ingests** (Sessions 27-28). Two companies under looser thematic adjacency than substantive paired analytical product (Sessions 6/13 pattern).

**Variant selection criteria.** Stop 1 cross-company analytical product assessment evaluates explicit candidates (shared customers, supplier-customer dependencies, reciprocal partnerships, structural co-positioning):

| Candidates | Variant |
|---|---|
| 2+ explicit | Substantive paired (Sessions 6/13) |
| 1 explicit | Optional; Vic decides |
| 0 explicit (with co-locations) | Parallel-but-independent (Sessions 27/28) |

**Execution.** Parallel-but-independent: no dedicated cross-company section; brief structural co-location framing in Thesis role; brief cross-references rather than forced cross-company synthesis. *See A.7 for Sessions 27/28 examples.*

### 3.15 Provisional and canonical chokepoint pages

A chokepoint page may be created via two pathways:

**Pathway 1 — Provisional → canonical promotion (existing).** Provisional chokepoint page created from a single company's primary sources when structural constraint evidence is strong but designation is provisional. Requirements: (1) page-top italic disclaimer naming sources + provisional scope; (2) "What would confirm or weaken this framing" section pre-registering cross-validation tests; (3) no Open questions or Source audit notes sections (those belong on company pages). When substantiated by a second source, provisional disclaimer removed; "confirm/weaken" section replaced by "Remaining uncertainties" or similar.

**Pathway 2 — Canonical-from-first-creation (codified Session 46).** Canonical chokepoint page created at first-creation when multi-source threshold met: Tier 3 anchor source + 3+ primary-source company pages, OR equivalent substantive multi-source coverage. Provisional stage skipped entirely. Standard canonical chokepoint page section structure applied (Open questions + Source audit notes + Change log; NO provisional disclaimer; NO "What would confirm or weaken" section).

**Empirical motivation (Pathway 2).** Session 44 HALEU-fuel-chokepoint.md created as first canonical-from-first-creation chokepoint page — anchored by HALEU report Tier 3 (S41) + LEU + BWXT (S42 paired) + CCJ (S43) primary-source company pages = 4 substantiating sources at first-creation.

**Pathway selection.** Default to Pathway 1 when source coverage is single-company; Pathway 2 when multi-source threshold met at session start. Verification at Stop 1 Phase 0 per Section 4.5 A6 sub-pattern (b).

## 4. Source ingest

### 4.1 Multi-source ingests

When ingesting multiple sources for the same company in single session, maintain separate financial tables per reporting period rather than blending. Cross-period deltas are analytically valuable and only visible when periods are kept distinct.

For three-source ingests (10-K + 10-Q + earnings call covering two fiscal periods): read sequentially older filing → current-period filing → current-period call. Source audit notes: one per-source entry, ordered by recency and tier.

### 4.2 Foreign-issuer ingests

Foreign private issuers file 20-F annually and 6-K interim disclosures rather than 10-K + 10-Q.

**Source-set composition:**

| Domicile | Source structure |
|---|---|
| US-domiciled | 10-K + 10-Q + earnings call transcript (most recent) |
| Foreign private issuer | 20-F + 6-K (most recent earnings disclosure) + earnings call transcript |

**6-K content variability.** 6-K filings span earnings, press releases, governance, material events. Verify selected 6-K is earnings disclosure at Phase 0.

**Fiscal calendar variability.** Foreign-issuer fiscal calendars may differ from US standard. Verify period-end dates per A6 (h) at Phase 0. Common: Dec 31 (most foreign — TSM, TSEM); Mar 31 (many Japanese); late-Apr / late-May (some Israeli/Indian).

**Currency + script.** 20-F filings typically USD with supplementary local-currency tables; clarify reporting currency at Phase 0. `scripts/fetch_filings.py` may require extension for 20-F + 6-K forms; TSM precedent uses `forms: ["20-F"]` only. *See A.8 for TSM precedent + multi-domain candidate list.*

**MJDS Canadian foreign-issuer sub-protocol (codified Session 46).** Canadian foreign private issuers using the Multi-Jurisdictional Disclosure System file 40-F annually (Canadian analog to US 10-K) plus 6-K interim disclosures. The 6-K is typically a cover sheet wrapping multiple substantive exhibits.

**Source-set composition (MJDS):**

| Document | Description |
|---|---|
| 40-F | Annual report; MJDS Canadian analog to US 10-K |
| 6-K cover | SEC wrapper metadata sheet (small file; not substantive content alone) |
| 6-K Ex 99.1 | Press release |
| 6-K Ex 99.2 | Financial statements |
| 6-K Ex 99.3 | Management's Discussion and Analysis (MD&A) |
| Earnings call | Tier 2 quarterly commentary |

**Six-file canonical pattern.** Phase 0 source-set verification confirms all six files staged in `raw/filings/` and `raw/transcripts/`; 6-K cover should be small (wrapper-only), with substantive content in three exhibits. Frontmatter `foreign_issuer: true` field applied per Section 3.2.

**Empirical motivation.** Session 43 CCJ established 6-file MJDS canonical pattern. `scripts/fetch_filings.py` extended with `forms: ["40-F", "6-K"]` for CCJ entry; exhibit decomposition handled per file at fetch time.

### 4.3 When sources contradict existing pages

Don't silently overwrite. Add contradiction note showing wiki's prior claim, what new source says, and — for factual disagreements — apply tier hierarchy. For interpretive disagreements, present both positions and flag for human to resolve.

### 4.4 Kickoff hypothesis falsification

Kickoff prompts may include hypotheses about company capability, customer relationships, or strategic direction that source evidence falsifies. Document falsification explicitly on the company page as investigation finding rather than silently omitting. Belongs in Thesis role or Open questions depending on significance: (1) state what was hypothesized; (2) state what sources did/did not find; (3) preserve epistemic humility (absence of evidence ≠ definitive proof of absence); (4) flag for `frameworks.md`/`_thesis.md` review if hypothesis may have propagated into configuration.

### 4.5 Kickoff drafting vault-content verification (A6)

When drafting an ingest kickoff prompt that pre-commits any vault-content reference, verify references against current vault state at Phase 0 BEFORE proceeding to source ingest planning.

**Pattern types (8 accumulated empirically):**

(a) **Framework placement** — Multi-domain framework verification per frameworks v10.1: Layer per Framework 2 (Caveats #1-9); per-domain `*_tier` per Frameworks 5/6/7/8/9; Framework 2.6 control-point; Framework 4 structural/cyclical (4.2 per-domain); Framework 10 CAPEX flow; Framework 11 cross-chokepoint themes. Multi-domain companies may carry multiple `*_tier` classifications. Per-domain Outside placement (Section 3.10) is honest-verdict-correct when domain-specific weak-fit criteria are met.

(b) **Vault page existence** — verify all referenced vault pages exist; plain-text for non-existent, `[[Brackets]]` only for existing.
(c) **Section numbering** — verify section numbers in target pages before drafting cross-references.
(d) **Frontmatter convention** — verify proposed fields against current vault convention; no new fields without explicit codification.
(e) **Wikilink integrity** — verify all `[[Brackets]]` point to existing pages; casing must match target filenames.
(f) **Session-positioning verification** — verify which prior session ingested what before referencing prior-ingest baselines.
(g) **Factual error scope (sub-categorized at Session 46 codification):**

- **(g) Tier 3 source figure variance** — verify Tier 3 source quantitative claims against primary sources at Stop 1 Phase 0; document material variances per company page Section 2.1 honest-verdict + log.md count maintenance. Cumulative count through Session 45: 8 instances (Session 40 BE Reports 39 4 variances; Session 42 BWXT backlog growth rate Tier 3 overstatement; other accumulated). Sub-patterns: scope underestimate; kickoff-prompt acquisition naming.

- **(g') Kickoff drafting factual variance (codified Session 46)** — verify kickoff "Codified background from existing vault context" claims against primary sources at Stop 1 Phase 0; document material falsifications per Section 4.4. Cumulative count through Session 45: 1 instance (Session 45 ENS — 6 material falsifications: Tijuana → Monterrey city; Springfield MO → Richmond KY + Greenville SC state; TPPL data center positioning rationale; DataSafe HX/EnVision Connect/AI rack engineered features absent from regulatory filings; ENS-VRT supplier-customer → competitor relationship; TPPL primary AI datacenter positioning over-attribution).

Combined (g)/(g') count post-Session 45: 9. Sub-categorization preserves analytical clarity — Tier 3 source variance is independent quality assessment of Vic-curated analytical research; kickoff drafting variance is quality assessment of kickoff drafting source discipline (Section 4.6) application.
(h) **Source filename verification** — verify period-end dates in filing headers match source filenames.

**Application discipline.** Every Phase 0 verification block runs all applicable pattern type checks. (b)-(h) apply universally; (a) only when kickoff pre-commits framework placement. Verification result documented at Stop 1 Phase 0 output. When verification gap surfaces, document on relevant page (or Session log entry) as kickoff hypothesis falsification per Section 4.4.

**Codification cadence.** A6 codification refinement triggered at 5+ pattern types accumulated; revisited at every codification session. New pattern types may emerge operationally — documented in `log.md` Session entries and integrated at next codification session. Discipline applies to kickoff drafting (chat-side) and Stop 1 Phase 0 verification (vault agent). *See A.9 for 8 pattern types per-instance evidence.*

### 4.6 Kickoff drafting source discipline

When drafting an ingest kickoff, distinguish four source tiers and place each in the correct kickoff scope:

- **Primary-source-verified (Tier 1+2):** 10-K / 10-Q / earnings call transcript / 8-K / 6-K / 40-F / 20-F. Eligible for "Codified background from existing vault context" section in kickoff.
- **Tier 3 source claims:** Vic-curated analytical research (HALEU report; energy bottleneck report; primer; chokepoint research framework). Eligible for "Codified background" section with explicit Tier 3 attribution.
- **Marketing/IR claims:** Web search results; company website; investor presentations; press releases. NOT eligible for "Codified background" section. Place under "Structural context per Tier 3/4 sources to verify at primary" framing.
- **Third-party summary claims:** Cervicorn; GuruFocus; Seeking Alpha; news aggregators; Motley Fool. NOT eligible for "Codified background" section. Place under "Structural context per Tier 3/4 sources to verify at primary" framing.

**Empirical motivation.** Sessions 44 and 45 surfaced systemic kickoff drafting factual variance from marketing-tier and third-party-summary content treated as primary-source-verified — Session 44 caught 3 frontmatter convention divergences; Session 45 caught 6 material factual falsifications (Tijuana → Monterrey; Springfield MO → Richmond KY + Greenville SC; TPPL data center positioning over-attribution; DataSafe HX/EnVision Connect features absent from regulatory filings; ENS-VRT supplier-customer → competitor relationship type; TPPL primary AI datacenter positioning → primary applications Specialty AGM + Motive Power maintenance-free).

**Application discipline.** Treat the boundary as binding: when a kickoff drafter is uncertain whether a claim is primary-source-verified, default to "Structural context per Tier 3/4 sources to verify at primary" placement. Stop 1 Phase 0 verification per Section 4.5 A6 sub-pattern (g') tests primary-source content against kickoff "Codified background" placements; falsifications documented per Section 4.4.

## 5. Operational guidance

### 5.1 Early phase

For first few ingests, propose before writing: state which pages will be created/updated and wait for confirmation. Once human confirms things feel right, drop the confirmation step and proceed autonomously.

### 5.2 What to avoid

- Summarizing filings comprehensively (most of a 10-Q is boilerplate; extract material + strategic only).
- Hallucinating relationships (connection not evidenced in source ≠ wiki content).
- Extensive quotation (paraphrase in wiki voice and cite).
- Reorganizing structure unilaterally (propose CLAUDE.md or folder layout changes; don't drift).
- Editing `_thesis.md`.

### 5.3 Evolution

This file is expected to change. When a convention isn't working, flag at end of session with concrete proposal. Human decides and commits.

## 6. Appendix — Empirical evidence + canonical examples

### A.1 Vault scope expansion empirical evidence *(cross-ref Section 1.2)*

**Pre-rework precedents.** Sessions 22 ([[VRT]] thermal/liquid cooling) + 28 ([[VIAV]] photonics-adjacent test) demonstrated tolerance for adjacent-infrastructure inclusion under existing photonics scope; Session 22 [[VRT]] Layer 5 / photonics_tier 4 documented adjacent-infrastructure framing.

**Sessions 32-35 codification arc.** Session 32 cpo-integration.md multi-source synthesis; Session 33 InP-supply.md provisional → canonical; Session 34 CLAUDE.md v8 → v8.1 structural rework; Session 35 log.md aggressive reduction (~79%; descending-order convention).

**3-file rework arc (2026-04-30 / 2026-05-01).** Vic-authorized reworks per ownership exception: `_thesis.md` (AI compute → AI datacenter scope expansion); `frameworks.md` v10 + v10.1 (multi-domain framework structures Frameworks 6/7/8/9/10/11; Caveats #1-9; cross-chokepoint themes); CLAUDE.md v9 (multi-domain frontmatter; Outside generalization; Section 1.1 ownership exception clause). Detailed revision content in respective file revision notes.

**Key structural observation.** Power infrastructure has displaced compute as the binding 2026 constraint — ~50% of planned 2026 US datacenter builds delayed/cancelled (Bloomberg/Sightline); transformer 4-year lead times mean compute CAPEX cannot deploy faster than power infrastructure expansion. Investment thesis reframed from photonics-primary to dual-anchor compute + power infrastructure exposure.

**VRT structural reclassification.** Was Tier 4 photonics with "adjacent infrastructure" framing (Session 22). Under AI datacenter scope, VRT became primary chokepoint at Energy/Power Tier 1 (frameworks v10.1). Photonics_tier 4 preserved; energy_power_tier 1 added. First canonical adjacent-infrastructure-now-primary placement.

### A.2 Path discrepancy verification empirical evidence *(cross-ref Section 1.3)*

Session 21 Phase 4 surfaced `agent_onboarding` directory naming gap (initial underscore creation; Claude Code naming validation required hyphens) and reference document location ambiguity (`raw/notes/` vs. `raw/references/`).

### A.3 Tier 1/Tier 2 framing gap multi-session origination *(cross-ref Section 3.4)*

Sessions 9-10 origination: MRVL Celestial acquisition disclosure gap; AVGO customer-owned tooling risk dismissal; AVGO rack leasing margin compression dismissal. Session 22: CSCO Acacia disclosure gap. Risk-framing sub-pattern most empirically substantive.

### A.4 Counterparty-attribution-only annotation canonical examples *(cross-ref Section 3.5)*

Three modes empirically validated across Sessions 20-22:
- **Over-claim** — Session 20 [[GLW]]: NVDA-named partnership initially over-claim; Contour single-core fiber refined per FY2025 10-K
- **Inversion** — Session 21 [[FN]]: Tier 3 "central LITE/COHR partner" structurally misdirected; FN primary sources document NVIDIA 27.6% + Cisco 18.2% top-2 concentration
- **Reciprocal-confirmation** — Session 22 [[VRT]]: NVIDIA partnership reciprocally confirmed at Tier 1 (10-K Item 7) + Tier 2 (Q1 2026 EcoDataCenter Sweden Vera Rubin + Vertiv OneCore)

**Cross-domain elevation.** Session 22 [[VRT]] reciprocal-confirmation example structurally elevated under AI datacenter scope — VRT now Framework 7 Tier 1 (Energy/Power), not Tier 4 adjacent-infrastructure. First canonical adjacent-infrastructure-now-primary placement (see A.1).

### A.5 Layer differentiation + Outside Framework 5 canonical text *(cross-ref Sections 3.9 + 3.10)*

**Layer 4 differentiation.** Layer 4 pages organize around product capability, capacity constraint, relationship leverage — different from Layer 1-2 (platform position + ecosystem control). Thesis role defines company via relationships to higher layers rather than own platform position. Customer concentration + manufacturing capacity carry more analytical weight at Layer 4.

**Layer straddling tension.** When revenue profile spans two layers (e.g., Layer 5 transceiver assembler with in-house Layer 4 laser manufacturing), maintain dominant-revenue tier in frontmatter; surface straddling as tension in Thesis role. Tier upgrade requires evidence non-dominant capability is commercially material (standalone revenue, merchant customer relationships, separate segment reporting) — not silent upgrade based on positioning evidence.

**Outside Framework 5 canonical examples (COHU + PLAB pair):** [[COHU]] (Session 8) — broad-cycle test-equipment with AI photonics as minority segment driver; [[PLAB]] (Session 28) — photomask supplier with broad semi infrastructure; AI advanced packaging as broad signal not photonics-specific; ZERO photonic foundry customer disclosure across 3 primary sources. Two-instance pattern supports codification per honest-verdict discipline.

### A.6 Tier 3-anchored theme page canonical example *(cross-ref Section 3.13)*

Session 19 `datacenter-photonics-supply-chain.md` creation; Sessions 20-22 cross-validation cycles produced concrete refinements (GLW multicore-fiber → Contour single-core; FN LITE/COHR-centric → NVDA + Cisco-centric; VRT NVIDIA-aligned → reciprocal-confirmation). Convention durability validated across three cycles without structural rewrite of source theme page.

### A.7 Parallel-but-independent paired-ingest variant canonical examples *(cross-ref Section 3.14)*

- **Session 27 [[CRDO]] + [[ANET]]** — networking-component adjacency at different layers (3 vs 5); 0 explicit / 2 structural co-locations
- **Session 28 [[VIAV]] + [[PLAB]]** — semi-infrastructure adjacency at same Layer 4 but different photonics-thesis fit (Tier 4 vs Outside F5); 0 explicit / 2 structural co-locations / 2 divergent / 1 untested

Variant validated across two consecutive paired-ingest sessions; structurally distinct from substantive paired analytical product.

### A.8 Foreign-issuer ingests TSM precedent + expanded candidate list *(cross-ref Section 4.2)*

[[TSM]] Sessions 1-2 + Session 17 NVDA GTC refresh precedent (`scripts/fetch_filings.py` line 32: `forms: ["20-F"]`). Session 28.5 TSEM forward reference as canonical first foreign-issuer paired ingest post-codification.

**Future candidates per multi-domain scope expansion:**

| Domain | Candidates | Framework placement |
|---|---|---|
| Memory | SK Hynix, Samsung Electronics (KRX) | F6 Tier 1 — HBM oligopoly |
| Photonics | TSEM (Israel ADR), ASE Tech (Taiwanese ADR), Aixtron (Germany XETRA) | F5 Tier 2-3 — foundry / OSAT / MOCVD |
| Energy/Power | ABB (Swiss ADR), Schneider (French SBGSF), HD Hyundai Electric / Hyosung (Korean) | F7 Tier 1-2 — power infra + transformer expansion |
| Equipment | Anritsu (Japanese), Infineon (German ADR IFNNY) | F8 Tier 3-4 — test + power semi |
| Materials | Sumitomo Electric, JX Advanced Metals, SUMCO, Shin-Etsu, Ibiden (Japanese) | F9 Tier 1-3 — substrate suppliers |
| Other | Foxconn Interconnect Technology (HK) | F1 — assembly/contract manufacturing |

Foreign-listed candidates require IBKR foreign access decision per portfolio composition. Sequencing per opportunity per Section 1.2.

### A.9 A6 vault-content-verification 8 pattern types per-instance evidence *(cross-ref Section 4.5)*

- **(a) Framework placement** — Session 21 [[FN]] kickoff anticipated Layer 5; primary sources placed at Layer 6
- **(b) Vault page existence** — Session 24 ANET vault-presence verification
- **(c) Section numbering** — Session 24 datacenter-photonics-supply-chain.md Section 2.5/2.6 shift
- **(d) Frontmatter convention** — Session 25 drift (`tier3_source:` / `related:` proposed fields)
- **(e) Wikilink integrity** — Session 25 wikilink casing gaps
- **(f) Session-positioning** — Session 26 kickoff hypothesis falsification (Session 4 vs actual Session 6 AEHR)
- **(g) Factual error scope** — Session 26 (5 stated vs 16 actual via grep); Session 27 Hyperlume vs Comira naming sub-pattern (g)'
- **(h) Source filename verification** — Session 28 PLAB-10Q-2026-02-01.htm validated against header