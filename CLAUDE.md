# CLAUDE.md — stocks-wiki (v9.3)

A personal research vault for AI datacenter supply chain and chokepoint analysis. You maintain the wiki; the human curates sources and asks questions.

*Version: v9.4 (Section 1.2 two-domain scope + Section 3.2 `defense_tier` field + Section 1.3 raw/ per-ticker subfolder reorg — vault expanded to a 2nd thesis domain, Defense & Drones; Session 123; 2026-06-03). Prior: v9.3 Section 4.7 refresh-ingest-log Session 104.*

## Descriptive language convention

When referencing frameworks, tiers, caveats, or sections in prose content, use descriptive names rather than numerical shorthand. Pair numbers with descriptive scope on first reference (e.g., "Energy/Power Tier 4 specialty component supplier scope"); descriptive name alone on subsequent references. Frontmatter YAML fields retain numerical values. Existing canonical pages from Sessions 1-45 are not retroactively updated; this convention applies to all session outputs from Session 46 onward.

## 1. Foundation

### 1.1 The anchor

`wiki/_thesis.md` is the evaluation point for everything. Every ingest, new page, update should strengthen, challenge, or refine the thesis. If an action does none, flag before proceeding. The human owns `_thesis.md` — never edit yourself. `raw/notes/frameworks.md` is similarly human-owned — frameworks are interpretive scaffolding; primary sources *enrich*, not override. When framework structures and primary-source evidence diverge, raise on the relevant page rather than silently reconciling.

**Ownership exception (codified Session 36).** Both files underwent Vic-authorized reworks via collaborative chat drafting (`_thesis.md` 2026-04-30; `frameworks.md` v10.1 2026-05-01). Default ownership convention resumes for all subsequent sessions — agents must not propose collaborative editing without explicit Vic-authorized rework session declaration.

### 1.2 Vault scope

**Two thesis domains (codified Session 123).** The vault spans **two parallel thesis domains**, each with its own human-owned `_thesis` + `frameworks` anchor: (1) **AI datacenter supply chain** — `wiki/_thesis.md` + `raw/notes/frameworks.md` (scope detailed below); (2) **Defense & Drones (unmanned systems)** — `wiki/_thesis-defense-drones.md` + `raw/notes/frameworks-defense-drones.md` (drones-first; broad munitions, European rearmament, and standalone directed-energy sequenced for future expansion). All CLAUDE.md conventions (source hierarchy, page conventions, disciplines, ingest protocols) apply to both domains. A company may be a **dual-thesis page** when it sits in both supply chains (e.g., [[MP]], [[AMD]], [[NVDA]], [[PLTR]]) — add the second domain's framing + `defense_tier` to the existing page rather than duplicating. Both anchor pairs are human-owned per Section 1.1 (the ownership exception applies equally to the Defense anchors).

Current scope: **AI datacenter supply chain — compute, photonics, memory, energy, power, equipment, materials, and more.** Multi-domain chokepoint analysis. Binding 2026 constraint per _thesis.md rework: power infrastructure (~50% of planned 2026 US datacenter builds delayed/cancelled; 4-year transformer lead times).

Multi-domain framework structures per frameworks v10.1: Framework 5 (photonics); F6 (memory); F7 (energy/power); F8 (equipment); F9 (materials provisional); F10 (CAPEX flow); F11 (cross-chokepoint themes). Per-domain `*_tier` placement enables cross-domain participants to carry multiple classifications (e.g., TSM photonics_tier 1 + memory_tier 1 + equipment_tier 2; VRT photonics_tier 4 + energy_power_tier 1).

**Outside-scope counterpoint placements:** [[COHU]] + [[PLAB]] canonical pair (Outside Framework 5). Outside Framework convention applies to Frameworks 5/6/7/8/9 per frameworks v10.1. Counterpoint inclusion does not expand vault scope.

**Scope expansion mechanism.** Vault scope under ongoing expansion with sequencing per opportunity (source availability, thesis development, time-bounded events) rather than rigid pre-codification. Domain-specific Tier 3 framework sources Vic-curated as expansion proceeds. *See A.1.*

### 1.3 Structure

**Knowledge layers:**

```
raw/         # source material — read from, never modify
  filings/<TICKER>/      # SEC filings grouped per ticker (+ flat newly_fetched/ staging)
  transcripts/<TICKER>/  # earnings-call transcripts grouped per ticker
  research/ news/ notes/ references/
wiki/        # your domain — write, update, interlink
  _thesis.md companies/ layers/ chokepoints/ themes/ relationships/
index.md     # catalog of wiki pages
log.md       # append-only record of activity
```

**Operational layers:** `prompts/` + `scripts/`. Operational infrastructure, not vault content. Never ingest from these directories.

The `raw/notes/` folder contains human's prior conversations and framework notes. Analytical frameworks treated as authoritative until human revises (primary sources enrich, not refute). Factual claims from notes treated as working hypotheses; confirm or revise against primary sources.

**Claude Code operational memory.** Persistent memory file at `~/.claude/projects/.../memory/MEMORY.md` outside vault. Cross-session context continuity (compressed mirror of `log.md`, structural notes, conventions, cumulative monitoring counts per Section 3.8). Must not contain independent analysis affecting wiki pages without Stop 1/Stop 2 protocol. Not in `index.md`/`log.md`; updates do not count for accounting.

**Path discrepancy verification.** Verify path conventions before committing new vault paths. Skill directories use hyphens (`.claude/skills/agent-onboarding/`); raw subdirectories no separators (`raw/filings/`). **`raw/filings/` + `raw/transcripts/` group source files into per-ticker subfolders using uppercase tickers** (`raw/filings/MP/MP-10K-2025-12-31.htm`; codified Session 123); `raw/filings/newly_fetched/` stays flat as the fetch/ingest staging queue, and `scripts/fetch_filings.py`'s skip-check derives the ticker from the filename prefix. File locations: skill files → `.claude/skills/<skill-name>/SKILL.md`; reference docs → `raw/references/`; session prompts → `prompts/`; Vic-authored synthesis → `raw/notes/`. *See A.2.*

## 2. Discipline

### 2.1 Four disciplines

**Host tensions honestly.** When human holds a position and the wiki's analysis suggests weak structural fit, the page states this plainly. Uncomfortable conclusions are the point of the wiki, not a bug.

**Describe, don't recommend.** Pages analyze structural position, competitive dynamics, evidence. They do not prescribe buying, selling, or holding. "Should I sell X" gets reframed to "what would have to be true for X's thesis to still be intact."

**Thesis tool, not portfolio tracker.** No P&L, no position sizes, no cost basis, ever. A reader should not be able to tell what the human owns from reading the pages.

**Honest-verdict discipline.** When a company's thesis fit is weak, the page states the weak fit plainly rather than constructing thesis-relevance narratives from generic positioning. Weak-fit pages may be shorter and verdict-like. Inclusion may be for trajectory or counterpoint rather than thesis centrality. Surface clearly in Thesis role.

**Honest-verdict trigger discipline (codified Session 61).** When refresh ingest surfaces evidence suggesting a baseline-reframing trigger may fire (Caveat #9 Layer 4-5 straddling upgrade; Outside Framework reframing; framework placement; A1 mode upgrade to reciprocal-confirmation), the trigger fires ONLY when evidence substantively meets the trigger's pre-registered criteria. **Substantive evidence honestly assessed against upgrade threshold; trigger NOT fired despite suggestive evidence** is the canonical methodology — not firing based on directional momentum without threshold satisfaction. Discipline applies bidirectionally: UPWARD reframing (kickoff hypothesis lower than primary evidence supports) follows same threshold satisfaction rigor as non-firing. *See A.10 for per-instance precedent pattern; current count in MEMORY.md.* Cross-reference Section 3.5 A1 three-mode framing for related discipline.

**Mid-fiscal-year disclosure methodology shift pattern (codified Session 79; refined Session 86; 5-instance precedent).** When a company restructures segments/divisions mid-fiscal-year OR retrospectively adjusts prior-period segment data, the canonical page must explicitly document the shift, apply restated comparatives at financial snapshot tables, and flag analytical-product complexity at cross-period comparison scope. 5-instance precedent: [[NVT]] S69 (Q1 2026 vertical disaggregation within continuing-segment scope) + [[MOD]] S70 (Q3 FY2026 Climate Solutions product-group disaggregation) + [[NOK]] S73 (strategic reorganization OLD 5-segment → NEW 2-segment company-wide effective January 1, 2026) + [[AMD]] S77 (Q1 FY2025 4-segment → 3-segment consolidation; "All prior period segment data were retrospectively adjusted") + [[NVDA]] S81 (Q1 FY2027 NEW Hyperscale + ACIE + Edge Computing framework at earnings-call-presentation + investor website with restated comparatives "for the past nine quarters"; SEC 10-Q preserves Compute & Networking + Graphics framework). Honest framing per Section 2.1: do not paper over the shift with blended-period framing; preserve segment-tier comparability boundaries at the shift date.

**Venue-asymmetric sub-pattern (codified Session 86; FIRST INSTANCE).** A shift may appear at one venue (earnings-call-presentation + investor website) while another venue preserves the prior framework (SEC 10-Q segment reporting). NVDA S81 FIRST INSTANCE: NEW Hyperscale + ACIE + Edge Computing framework at earnings-call-presentation + investor website; SEC 10-Q preserves Compute & Networking + Graphics framework. LLM application: document venue-asymmetry at canonical page Source audit notes; cross-reference Section 3.6 cross-venue disclosure gap convention when the shift constitutes a cross-venue gap pattern beyond mere reporting-venue lag.

### 2.2 Source hierarchy

When sources disagree on facts, higher tier wins. On interpretation, triangulate and flag the disagreement on the relevant page.

- **Tier 1 — Primary filings:** 10-K, 10-Q, 20-F, 8-K, proxies. Ground truth.
- **Tier 2 — Primary commentary:** Earnings calls, analyst days, conference appearances. Colored by management incentives.
- **Tier 3 — Independent analysis:** SemiAnalysis, Stratechery, reputable sell-side, industry reports. Cite, don't treat as fact.
- **Tier 4 — News:** Bloomberg, WSJ, Reuters, FT. Reliable for events, shallow on thesis.
- **Tier 5 — Social/forums:** Twitter/X, Reddit, blogs. Signal for generating questions; never cited.

Skip promotional content and aligned commercial incentive.

*Tier 1/Tier 2 calibration.* Factual data (financials, concentration, capacity, legal, geographic) — Tier 1 authoritative. Competitive assessment, strategic intent, management signaling — Tier 2 often more analytically informative than Tier 1's legal-conservative framing. *Analyst silence as signal* — asymmetry between venues (risk in 10-K but unaddressed in analyst Q&A) is meta-signal about investor community processing; document in Source audit notes. *Source unavailability as observation* — when an expected source is unavailable, document explicitly with analytical implications; inability to test patterns requiring that source is itself a finding.

### 2.11 Non-calendar fiscal year-end filer protocol (codified Session 61; refined Session 79)

Vault canonical participants with non-calendar fiscal year-end dates require period-parity discipline at calendar terms.

**Period-parity at calendar terms (primary discipline).** Cross-vault period comparison uses calendar-quarter equivalence regardless of fiscal-year designation (e.g., FLNC Q2 FY2026 = calendar Q1 2026; analytically equivalent recency to vault calendar-Dec-31 peers' Q1 2026 disclosures). Apply at Phase 0 source-set verification; document calendar-equivalence in page Source audit notes per-source entry.

**Fiscal-year-designation honest framing (secondary discipline).** Fiscal-year designation preserved at source filename + financial table headers per filer canonical convention. Honest framing in Thesis role: "Q2 FY2026 = calendar Q1 2026" annotation at first cross-vault comparison.

**7-instance applicability precedent (codified Session 79).** Section 2.11 applies at month+ fiscal-year-end offset scope: [[ENS]] (March 31) + [[FCEL]] (October 31) + [[VIAV]] (late June) + [[FN]] (late June) + [[FLNC]] (September 30) + [[MOD]] (March 31) + [[ARM]] (March 31). 5 distinct fiscal calendars in vault: Dec 31 (most canonical; Section 2.11 N/A) + Mar 31 (ENS + MOD + ARM) + late-June (VIAV + FN) + Sep 30 (FLNC) + Oct 31 (FCEL).

**LLM application:** at kickoff drafting + Phase 0 source-set verification + Source audit notes per-source entry drafting, apply both disciplines per filer fiscal calendar. *See A.11 for 7-instance + 3-instance week-scope baseline combined precedent.*

#### 2.11.1 Substantive-offset threshold methodology (codified Session 79; 3-instance week-scope precedent)

Not every non-calendar fiscal year-end filer warrants Section 2.11 application. Threshold per fiscal-year-end offset from calendar Dec 31:

| Offset scope | Section 2.11 status | Precedent |
|---|---|---|
| **Week-scope (~3 days to ~1 month)** | **N/A** — treat as substantively-calendar fiscal year | 3-instance: [[NVDA]] (last-Sunday-of-January; ~1-month offset) + [[AMD]] S77 (last-Saturday-of-December; ~4-day offset) + [[INTC]] S78 (last-Saturday-of-December; ~4-day offset) |
| **Month+ scope (≥1 month)** | **Applied** — non-calendar fiscal year filer protocol per Section 2.11 primary + secondary discipline | 7-instance: see Section 2.11 applicability precedent above |

**Honest framing.** Week-scope offset substantively edge case — NVDA last-Sunday-of-January ~1-month offset is substantively LARGER than AMD + INTC ~4-day offset but substantively SMALLER than month+ scope baseline; honest interpretation captures NVDA at week-scope baseline per substantively-calendar fiscal year treatment vault precedent. Period-parity scope at week-scope offset = ~3-4 day to ~1-month drift; substantively CLEAN cross-canonical comparative analytical product enabled at substantive scope.

#### 2.11.2 Cross-canonical EXACT-period-parity comparative analytical product methodology (codified Session 79; FIRST INSTANCE)

When two vault canonicals share EXACT-match fiscal calendar structure (identical period-end dates), substantive cross-canonical comparative analytical product enabled at identical-period-end scope.

**FIRST INSTANCE precedent:** [[AMD]] S77 + [[INTC]] S78 both 52/53-week last-Saturday-of-December fiscal year (FY2025 = Dec 27, 2025; Q1 2026 = Mar 28, 2026 — EXACT match). Methodology codified at S79 substantively-distinct from cross-canonical week-scope offset comparative scope; EXACT-period-parity enables direct cross-canonical analytical product at identical period-end scope without offset reconciliation.

**LLM application:** when EXACT-period-parity surfaces between vault canonicals, honest framing in Thesis role + cross-vault adjacency section documents EXACT match; cross-canonical comparative analytical product opportunity flagged at substantive scope.

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
layer: 1-6                          # company pages only
photonics_tier: 1-5 | outside       # per-domain *_tier fields optional
memory_tier: 1-5 | outside
energy_power_tier: 1-5 | outside
equipment_tier: 1-5 | outside
materials_tier: 1-5 | outside       # provisional
defense_tier: 1-4 | outside         # defense/drones domain; see Section 3.2 note (Option A taxonomy)
foreign_issuer: true                # non-US-domiciled filers only
last_updated: YYYY-MM-DD
---
```

`layer` (Framework 2) and per-domain `*_tier` fields (Frameworks 5/6/7/8/9) distinct from source `Tier`. Multi-domain companies carry multiple `*_tier` classifications (TSM photonics_tier 1 + memory_tier 1 + equipment_tier 2; VRT photonics_tier 4 + energy_power_tier 1). For multi-layer exposure, single primary `layer` value; nuance in body prose. For non-company pages, `tickers` lists tickers whose primary sources substantively informed page content (provenance, not relevance tag).

**Frontmatter convention reinforcement (codified Session 46).** (a) `foreign_issuer: true` — apply on company pages for non-US-domiciled filers (foreign private issuers + MJDS Canadian filers); absent on US-domiciled (default; S43 CCJ precedent). (b) `tickers` — single-ticker scope on company pages; multi-ticker scope on chokepoint/theme/relationship pages where multiple tickers' primary sources informed content (provenance, not relevance tag; S44 HALEU-fuel-chokepoint precedent). (c) `*_tier` application — apply per-domain field only when company has substantive exposure to that domain, not derivatively (do not assign memory_tier to NVDA because NVDA buys HBM; do assign to MU/SK Hynix/Samsung as memory-domain operators). `outside` is honest-verdict-correct per Section 3.10 four-criterion test (S36 FLEX precedent).

**`defense_tier` convention (codified Session 123; Option A taxonomy).** `defense_tier` classifies Defense & Drones domain companies per the four investability/structural-position tiers in `raw/notes/frameworks-defense-drones.md` Framework D2: **1 = prime with drone-relevant programs of record; 2 = mid-cap pure-play / specialist; 3 = speculative micro-cap (apply Framework D6 financial-quality screen); 4 = supply-chain / materials enabler (chokepoint owner).** **Semantics note — unlike the AI `*_tier` fields, the `defense_tier` number is NOT a conviction/quality rank:** Tier 4 enablers carry the *highest* structural conviction (they own the chokepoints), not the lowest. Conviction tracks the chokepoint quality gradient (Framework D5: geology/physics > policy), not the tier number. `outside` is honest-verdict-correct for defense-adjacent names with weak unmanned-systems fit. Apply per the (c) substantive-exposure discipline above; dual-thesis pages (MP / AMD / NVDA / PLTR) carry `defense_tier` alongside their AI `*_tier` fields.

### 3.3 Voice, wikilinks, citations

**Voice.** Analytical third person. No first/second person, no investment prescriptions.

**Wikilinks.** Short form `[[TICKER]]` or `[[page-name]]`. Every ticker/chokepoint/theme mention gets linked. Pages do not wikilink to themselves. Forward wikilinks acceptable; do not create stub pages to resolve them. Add at least one inbound link from existing page when creating a new page.

**Citations.** Every numerical claim and non-obvious substantive claim names source and period — e.g. *CoWoS capacity expansion (TSM Q1 2026 call)*. Per-claim citations remain correct as pages accumulate multi-source content; do not substitute header-level citation notes.

*Rhetorical vs. factual.* Factual claims (verifiable numbers, confirmed events) paraphrased in wiki voice with citation. Rhetorical claims (directional assertions, promotional framing) attributed to speaker — "Jensen claimed...", "management characterized...". When in doubt, attribute. Source audit notes + Change log track overall page provenance; cross-source synthesis statements name all involved sources.

*Disclosed/inferable/unknown.* For unnamed entities ("Customer A," "a significant customer"): (1) Disclosed — exact data from filing; (2) Inferable — patterns matching publicly known profiles, hedged language only ("consistent with," "resembles"), never assertive; (3) Unknown — what filing does not disclose.

*Disclosure lifecycle awareness.* Topics may appear in management commentary (Tier 2) before regulatory filings (Tier 1). Same-day divergences are meta-signal about disclosure lifecycle. Document in Source audit notes when observed.

### 3.4 Tier 1/Tier 2 framing gap convention (A4)

Distinct from Disclosure lifecycle awareness. Covers cases where Tier 1 filing and Tier 2 earnings call treat the same risk or commercial topic with materially different framing. Pattern types: (a) filings flag risk that calls dismiss; (b) filings omit commercial detail that calls disclose extensively; (c) filings acknowledge margin compression risk that calls dismiss with rhetorical deflection.

Document prominently in Source audit notes with "Tier 1/Tier 2 framing gap" label. Pattern instances compound; three or more becomes analytically significant beyond any individual disclosure.

**Sub-pattern annotation (4 sub-patterns; formalized Session 61):** risk-framing gap (risk in 10-K Risk Factors but dismissed/minimized in call); customer-concentration gap (customer concentration in 10-K Notes but not addressed on call); technology-content gap (technology details disclosed in 10-K Item 1 but not addressed on call); geographic-concentration gap (geographic concentration in 10-K MD&A or Item 1 but not addressed in call). Codification threshold per sub-pattern is 3+ instances. Cross-venue sub-pattern separately codified per Section 3.6 (A4-bis; distinct convention).

*See A.3 for per-instance evidence; current count canonical in MEMORY.md per Section 3.8 brevity discipline.*

### 3.5 Counterparty-attribution-only annotation (A1 three-mode framing)

When Tier 3 sources cite counterparty-side announcements about ecosystem partnerships, wiki text annotates cross-validation status per three-mode framing:

- **Over-claim:** counterparty-side announcement not bilaterally confirmed. Annotate: *"named in [counterparty] [venue]; not reciprocally confirmed in [target] primary sources."*
- **Inversion:** counterparty-side projection structurally misdirected. Annotate: *"characterized as [framing X]; [target] primary-source disclosure shows [framing Y]."*
- **Reciprocal-confirmation:** counterparty-side claim bilaterally confirmed. Annotate: *"named in [counterparty] [venue]; reciprocally confirmed in [target] primary sources [citation]."*

Apply at first instance during Tier 3-anchored theme page construction; refine at primary-source ingest cross-validation. *See A.4 for canonical examples.*

### 3.6 Cross-venue disclosure gap convention (A4-bis; codified Session 86)

Distinct from Tier 1/Tier 2 framing gap (Section 3.4). Addresses divergence between two non-filing venues — typically conference vs near-concurrent earnings call. Pattern: information selectively disclosed at one venue (industry conference, GTC keynote, technology day, investor day) but not addressed at adjacent earnings calls or 10-Q filings.

**Detection trigger.** When a company discloses material information at one venue (e.g., GTC) but preserves silence at adjacent venues (e.g., next earnings call), the gap is information, not absence. The venue-specific pattern is durable and meaningful — silence at one venue does not indicate retreat if the disclosure venue is itself durable.

**Documentation requirement.** Source audit notes flag venue-specific gaps with "cross-venue gap" label and per-venue disclosure scope.

**Honest framing discipline ("silence ≠ retreat").** Do not interpret venue-specific silence as architectural shift or strategic retreat. If the disclosure venue (GTC, technology day) preserves the topic across cycles, the venue-specific pattern is the canonical framing — not a quarter-over-quarter erosion signal.

**Falsification condition.** Venue-specific pattern preserved IF the durable disclosure venue continues to carry the topic across cycles. IF the durable venue itself stops carrying the topic (e.g., GTC March 2027 zero CPO mentions after GTC March 2026 + GTC March 2025 substantiation), the pattern transitions from venue-specific silence to genuine retreat. Distinct interpretations; the codification reading depends on the durable venue's continued disclosure.

**5-reference precedent (codification threshold over-met):** [[NVDA]] S81 Open Question #3 (venue-specific CPO disclosure persistence verdict; GTC March 2026 carries advanced packaging detail + COUP; Q1 FY2027 earnings call zero CPO mentions across 16 pages) + [[NVDA-platform-integration]] S82 (asymmetric reciprocal naming observation) + [[cpo-integration]] S84 (venue-specific CPO disclosure verdict integrated) + [[CPO-platform-battle]] S84 (Jensen "silence ≠ retreat" framing canonical) + [[advanced-optical-packaging]] S85b (venue-specific pattern reinforcement at advanced packaging chokepoint scope).

**Cross-reference scope.** Ties to Section 2.1 honest-verdict discipline + Section 3.4 Tier 1/Tier 2 framing gap (distinct pattern; cross-venue is venue-asymmetric, framing gap is tier-asymmetric) + Section 2.1 mid-fiscal-year venue-asymmetric sub-pattern (codified Session 86).

### 3.7 CEO combativeness as Tier 2 meta-observation (monitoring)

When CEO responds to structurally reasonable analyst questions with unusually defensive or dismissive language beyond standard corporate deflection, note in Source audit notes as potential indicator of which competitive pressures are most acutely felt. Descriptive, not diagnostic. Document exchange with exact wording per rhetorical claims convention; do not adjudicate underlying cause. Status: monitoring pending third instance; current count in MEMORY.md.

### 3.8 Source audit notes + Change log

**Source audit notes.** Standard section on every company page created or substantively updated from a primary source. Optional on theme/chokepoint pages. Captures observations about the source itself — management tone shifts, analyst framing, conspicuous absences, unanswered questions, what went unquantified. Place before Change log. For multi-source pages, maintain per-source entries (dated, source-attributed).

**Change log.** At bottom of each page. Track what was added/changed in each ingest with dated line. Makes staleness and evolution visible at a glance.

**Brevity discipline (codified Session 38).** Change log entries, source audit notes per-source entries, and log.md session entries must be SHORT — operational essentials only. **Targets:** 1-3 sentences for change log entries; 2-5 sentences for source audit notes per-source entries; ~15-25 lines for log.md session entries.

**Goes in:** date + session number; what was created/updated; canonical placements applied (layer + tier); convention codification observations; one-line key finding if structurally significant. **Does NOT go in:** Phase 4 reflection content; multi-paragraph analytical synthesis; cross-company analytical product detail; full source audit notes content; convention text quotations; per-instance empirical evidence; A1 three-mode application detail.

Canonical analytical content lives in Thesis role + middle sections + Open questions. Change log + source audit notes + log.md track *what changed*, not *what the analysis was*. Phase 4 reflection content belongs in chat session deliverables. **Application:** prospective from S38+; existing oversized entries not retroactively trimmed.

### 3.9 Company page structure

Five sections universal: Thesis role, Financial snapshot, Open questions, Source audit notes, Change log. Middle sections (technology roadmap, capacity, ecosystem, demand, competitive positioning, supply chain) vary by company type and layer. Do not force a rigid universal template; structure follows analytical significance. *Layer 4 differentiation + Layer straddling tension: see A.5.*

### 3.10 Outside Framework placement (per-domain generalization)

`<framework>_tier: outside` is honest-verdict-correct designation when source evidence shows weak fit on a specific per-domain framework. Applies to Frameworks 5/6/7/8/9 per frameworks v10.1.

**Four-criterion test (canonical Framework 5; substitute domain-specific equivalents for F6/F7/F8/F9 per criterion 1):**
1. ZERO domain-specific customer disclosure (photonic foundry / IC / SiPh for F5; named hyperscaler / datacenter-power for F7).
2. Domain mentions appear as broad market enumeration rather than named served segments.
3. AI exposure is broad-cycle subsegment rather than domain-direct.
4. Customer concentration is generic rather than domain-specific.

**Multi-domain Outside.** A single company may carry Outside placement on multiple per-domain frameworks simultaneously (e.g., COHU Outside F5 + F8; TSEM Outside F7 + F8 + F9) — strengthens honest-verdict-correctness.

**Counterpoint role + cross-reference discipline.** Vault inclusion is for trajectory or counterpoint (e.g., equipment-tier split between structurally AI-exposed [[AEHR]]/[[ONTO]]/[[VIAV]] and broad-cycle [[COHU]]/[[PLAB]]) rather than thesis centrality. Outside-placed companies excluded by default from theme-page Future ingest candidates lists where theme is domain-specific. Outside placement justification subsection within Thesis role documents rationale per four-criterion test.

**Promotion mechanism (Outside → Tier 4).** Warranted when source evidence surfaces domain-specific structural exposure meeting per-framework triggers. F5 canonical: 2+ photonic foundry customers named; OR >15% revenue from photonics; OR triggers pre-registered in Open questions. *See A.5 for COHU + PLAB canonical pair.*

### 3.11 Displacement analysis

When a company's core business faces structural displacement from a tracked technology transition (e.g., pluggable transceiver assembler facing CPO displacement), a dedicated displacement analysis section may be warranted. Surface: structural tension, management's threat framing (silent / reframed / acknowledged), analyst coverage patterns, displacement vulnerability factors, timing gaps vs. adjacent companies. Optional — add only when displacement is thesis-central.

### 3.12 Theme page types

Three types from practice: **Dynamics themes** (evolving competitive/market dynamic; e.g., `AI-demand-durability.md`, `foundry-competition.md`); **Mechanism themes** (how a company maintains/challenges structural position; e.g., `NVDA-platform-integration.md`); **Absence themes** (thesis-significant topic primary sources are not yet addressing; e.g., `CPO-platform-battle.md`). Future ingests may surface other legitimate page types.

### 3.13 Tier 3-anchored theme pages (A2)

A theme page may be anchored on Tier 3 synthesis sources when primary-source-anchored creation is premature but cross-cutting analytical content exists. Structural requirements: (1) Vic-authored synthesis as anchor with attribution explicit in body and frontmatter; (2) Counterparty-attribution-only annotation per three-mode framing (Section 3.5); (3) No-verification at construction; deviation-based refinement at ingest; (4) Open questions section pre-registers primary-source verification triggers.

**Multi-domain Tier 3 sources.** Existing canonical: `raw/research/photonics-chokepoint-table.md`. Additional Tier 3 sources anticipated for memory, energy/power, equipment, materials — Vic-curated as expansion proceeds; new sources may anchor theme pages per same A2 conventions. *See A.6 for canonical example.*

### 3.14 Paired ingests

When two companies sit at adjacent positions in the value chain, paired ingest covers both in single session. Use when: thesis roles structurally similar; paired comparison generates content not available from either source alone; source period alignment reasonable. Two-stop protocol typically warranted; middle sections allowed to differ.

**Variant selection criteria.** Stop 1 cross-company analytical product assessment evaluates explicit candidates (shared customers, supplier-customer dependencies, reciprocal partnerships, structural co-positioning):

| Candidates | Variant |
|---|---|
| 2+ explicit | Substantive paired (S6/S13 pattern) |
| 1 explicit | Optional; Vic decides |
| 0 explicit (with co-locations) | Parallel-but-independent (S27/S28 variant) |

**Execution.** Parallel-but-independent: no dedicated cross-company section; brief structural co-location framing in Thesis role; brief cross-references rather than forced cross-company synthesis. *See A.7 for S27/S28 examples.*

### 3.15 Provisional and canonical chokepoint pages

A chokepoint page may be created via two pathways:

**Pathway 1 — Provisional → canonical promotion.** Provisional chokepoint page created from a single company's primary sources when structural constraint evidence is strong but designation is provisional. Requirements: (1) page-top italic disclaimer naming sources + provisional scope; (2) "What would confirm or weaken this framing" section pre-registering cross-validation tests; (3) no Open questions or Source audit notes sections (those belong on company pages). When substantiated by a second source, provisional disclaimer removed.

**Pathway 2 — Canonical-from-first-creation (codified Session 46; 5-instance precedent codified Session 79).** Canonical chokepoint page created at first-creation when multi-source threshold met: Tier 3 anchor source + 3+ primary-source company pages, OR equivalent substantive multi-source coverage. Provisional stage skipped entirely. Standard canonical chokepoint page section structure applied (Open questions + Source audit notes + Change log; NO provisional disclaimer or "confirm/weaken" section).

**5-instance Pathway 2 precedent post-S71 + 4 structural type taxonomy:**

| Instance | Session | Chokepoint | Structural type |
|---|---|---|---|
| 1 | S44 | [[HALEU-fuel-chokepoint]] | Sequential-dependency-chain |
| 2 | S57 | [[BTM-grid-bypass-workaround]] | Competing-technology-base (1st) |
| 3 | S63 | [[transformer-supply]] | Oligopoly + substrate-bound |
| 4 | S64 | [[HBM-oligopoly]] | Upstream-oligopoly with vault-adjacent scope |
| 5 | S71 | [[liquid-cooling]] | Competing-technology-base (2nd; structural-type durability validated) |

**Canonicalization-criteria substantive scope.** Pathway 2 substantiation threshold: (a) Tier 3 anchor source explicitly establishing chokepoint structural framing OR (b) 3+ vault primary-source canonical pages substantively documenting the constraint scope OR (c) equivalent multi-source coverage (e.g., S71 [[liquid-cooling]] = 6-canonical vault participant scope at chokepoint synthesis methodology). Honest framing per Section 2.1: substantive primary-source substantiation drives Pathway 2 application — not directional momentum toward canonical placement without threshold met.

**Pathway selection.** Default to Pathway 1 when source coverage is single-company; Pathway 2 when multi-source threshold met at session start. Verification at Stop 1 Phase 0 per Section 4.5 A6 sub-pattern (b).

**4-canonical sub-domain coverage strengthening (codified Session 86).** Pathway 2 application strengthens when a sub-domain accumulates 4+ canonical participants at a single theme/chokepoint scope. FIRST INSTANCE: [[AI-agentic-CPU-orchestration-reemergence]] theme — S80 creation at 3-canonical threshold (ARM + AMD + INTC); S83 expansion to 4-canonical (NVDA Vera CPU addition). 4-canonical scope does not displace the 3-canonical Pathway 2 threshold; it reinforces methodology applicability. Forward implication: future Pathway 2 applications document with confidence at 3-canonical threshold; 4-canonical strengthening is reinforcement, not threshold-shift.

### 3.16 Language convention — "substantive" / "substantively" discipline (codified Session 86)

Default to direct language. Use "substantive" / "substantively" only where the word distinguishes Tier 1 primary substantiation from Tier 3 hedging or weak-fit assertion. The word should mark something genuinely material vs marginal, not provide emphasis.

**Deletion test at composition.** Each candidate instance asks "does this word add meaning here, or just emphasis?" If emphasis, delete. Pattern observed at S81 baseline; corrected at S82 onward via deletion test discipline.

**Honest framing on drift.** If drift surfaces in a session output, surface honestly as drift in Phase 4 reflection. Do not claim "load-bearing usage" retroactively for instances that fail the deletion test.

**Application.** Prospective from Session 86 onward; existing oversized usage at NVDA.md S81 + log.md S81 + kickoff prompts preserved as historical artifact (forward-only application per Section 3.8 brevity discipline precedent). Cross-reference Section 3.3 voice convention.

## 4. Source ingest

### 4.1 Multi-source ingests

When ingesting multiple sources for the same company in single session, maintain separate financial tables per reporting period rather than blending. Cross-period deltas are analytically valuable and only visible when periods are kept distinct.

For three-source ingests (10-K + 10-Q + earnings call covering two fiscal periods): read sequentially older filing → current-period filing → current-period call. Source audit notes: one per-source entry, ordered by recency and tier.

**Chokepoint refresh protocol — 1-stop vs 2-stop (codified Session 79; 5-instance precedent).** Chokepoint page refreshes default to 1-stop protocol (single Stop; plan + execute combined) when scope is contained; 2-stop protocol required when scope creep risk substantive.

**1-stop chokepoint refresh applicability conditions** (all must hold): (a) single-source-driven update scope (single new canonical ingest propagation OR single Tier 3 analytical product propagation); (b) no NEW chokepoint structural type introduced; (c) vault canonical participant scope stable (no NEW canonical added to chokepoint scope); (d) 5-trigger escalation test all NEGATIVE (no new primary-source ingest at chokepoint scope; no new structural type; no new chokepoint creation; cross-vault analytical product already established; minor cross-vault propagation only).

**2-stop chokepoint refresh required when**: (a) substantive multi-source scope OR (b) NEW chokepoint structural type emerging OR (c) substantive canonical participant scope expansion OR (d) any escalation trigger POSITIVE OR (e) major analytical product addition scope.

**Scope creep prevention discipline.** 1-stop refresh limited to substantive-update scope per source; hard cap ~3-5 files; expansion within Section 3.8 brevity discipline (~12-25 lines per new subsection).

**5-instance Pathway precedent:** S51 [[HALEU-fuel-chokepoint]] (FIRST 1-stop refresh; minor update scope) + S65 [[TSMC-CoWoS]] (SECOND; substantial-content-addition scope ~120 lines; protocol durability at substantial-content scope validated) + S66 [[datacenter-laser-supply]] + S67 [[cpo-integration]] + S68 [[advanced-optical-packaging]]. S65-S68 = 4-chokepoint paired-cluster refresh demonstrating cross-vault propagation cycle methodology at 1-stop refresh scope.

### 4.2 Foreign-issuer ingests

Foreign private issuers file 20-F annually and 6-K interim disclosures rather than 10-K + 10-Q.

**Source-set composition:**

| Domicile | Source structure |
|---|---|
| US-domiciled | 10-K + 10-Q + earnings call transcript (most recent) |
| Foreign private issuer | 20-F + 6-K (most recent earnings disclosure) + earnings call transcript |
| MJDS Canadian (codified S46) | 40-F + 6-K (cover + Ex 99.1 press release + Ex 99.2 financials + Ex 99.3 MD&A) + earnings call = 6-file canonical pattern |

**6-K content variability.** 6-K filings span earnings, press releases, governance, material events. Verify selected 6-K is earnings disclosure at Phase 0. MJDS 6-K cover is wrapper-only; substantive content in three exhibits.

**Fiscal calendar + currency variability.** Foreign-issuer fiscal calendars may differ from US standard (Dec 31 most foreign incl. TSM/TSEM; Mar 31 many Japanese; late-Apr/late-May some Israeli/Indian). Verify period-end dates per A6 (h) at Phase 0. 20-F filings typically USD with supplementary local-currency tables; clarify at Phase 0. Frontmatter `foreign_issuer: true` field applied per Section 3.2. `scripts/fetch_filings.py` may require extension per 20-F + 6-K + 40-F forms. *See A.8 for TSM precedent + multi-domain candidate list; S43 CCJ established MJDS 6-file pattern.*

### 4.3 When sources contradict existing pages

Don't silently overwrite. Add contradiction note showing wiki's prior claim, what new source says, and — for factual disagreements — apply tier hierarchy. For interpretive disagreements, present both positions and flag for human to resolve.

### 4.4 Kickoff hypothesis falsification

Kickoff prompts may include hypotheses about company capability, customer relationships, or strategic direction that source evidence falsifies. Document falsification explicitly on the company page as investigation finding rather than silently omitting. Belongs in Thesis role or Open questions depending on significance: (1) state what was hypothesized; (2) state what sources did/did not find; (3) preserve epistemic humility (absence of evidence ≠ definitive proof of absence); (4) flag for `frameworks.md`/`_thesis.md` review if hypothesis may have propagated into configuration.

### 4.5 Kickoff drafting vault-content verification (A6)

When drafting an ingest kickoff prompt that pre-commits any vault-content reference, verify references against current vault state at Phase 0 BEFORE proceeding to source ingest planning.

**Pattern types (8 accumulated empirically; see A.9 for per-instance evidence):**

- (a) **Framework placement** — Multi-domain framework verification per frameworks v10.1 (Layer per Framework 2; per-domain `*_tier` per Frameworks 5/6/7/8/9; Framework 2.6 control-point; Framework 4 structural/cyclical; Framework 10 CAPEX flow; Framework 11 cross-chokepoint themes). Per-domain Outside placement (Section 3.10) is honest-verdict-correct when domain-specific weak-fit criteria met.
- (b) **Vault page existence** — verify referenced pages exist; plain-text for non-existent, `[[Brackets]]` only for existing.
- (c) **Section numbering** — verify section numbers in target pages before drafting cross-references.
- (d) **Frontmatter convention** — verify proposed fields against current vault convention; no new fields without explicit codification.
- (e) **Wikilink integrity** — verify all `[[Brackets]]` point to existing pages; casing must match target filenames.
- (f) **Session-positioning** — verify which prior session ingested what before referencing prior-ingest baselines.
- (g) **Factual error scope (sub-categorized S46):** (g) Tier 3 source figure variance — verify Tier 3 quantitative claims against primary at Phase 0. (g') Kickoff drafting factual variance — verify kickoff "Codified background" claims against primary at Phase 0; document material falsifications per Section 4.4.
- (h) **Source filename verification** — verify period-end dates in filing headers match source filenames; verify ticker-content match (S59 FN-FNF mislabel precedent).

**Discipline boundary (codified S61).** Section 4.6 marketing-tier non-corroboration at primary (Tier 3/4 marketing-source placed under "Structural context to verify at primary" in kickoff) is EXPECTED Section 4.6 outcome, NOT a Section 4.5 (g') factual variance. (g') increments ONLY when Tier 3/4 content was placed under "Codified background" AND material variance surfaces at Phase 0.

**Application + codification cadence.** Every Phase 0 verification runs all applicable pattern type checks. (b)-(h) universal; (a) only when kickoff pre-commits framework placement. Verification gaps documented per Section 4.4 kickoff hypothesis falsification. A6 codification refinement triggered at 5+ pattern types; revisited at every codification session. Discipline applies to kickoff drafting (chat-side) + Stop 1 Phase 0 verification (vault agent). *Per-instance evidence + cumulative counts in A.9 + MEMORY.md.*

### 4.6 Kickoff drafting source discipline

When drafting an ingest kickoff, distinguish four source tiers and place each in the correct kickoff scope:

- **Primary-source-verified (Tier 1+2):** 10-K / 10-Q / earnings call / 8-K / 6-K / 40-F / 20-F. Eligible for "Codified background from existing vault context."
- **Tier 3 source claims:** Vic-curated analytical research (HALEU report; energy bottleneck report; primer; chokepoint research framework). Eligible for "Codified background" with explicit Tier 3 attribution.
- **Marketing/IR + third-party summary claims:** Web search; company website; investor presentations; press releases; Cervicorn / GuruFocus / Seeking Alpha / news aggregators. NOT eligible. Place under "Structural context per Tier 3/4 sources to verify at primary."

**Application discipline.** Treat the boundary as binding: when uncertain whether a claim is primary-source-verified, default to "Structural context per Tier 3/4 sources to verify at primary." Stop 1 Phase 0 verification per Section 4.5 A6 (g') tests primary-source content against kickoff "Codified background"; falsifications documented per Section 4.4. Empirical motivation: S44-S45 surfaced systemic factual variance from marketing-tier content treated as primary-source-verified.

**Empirical ROI durability (codified Session 61).** Four-tier source discipline produced multi-session zero-falsification streak post-S46 (S47 FCEL = 1 falsification; subsequent sessions all 0; streak spans full ingest-type variety). Pre-codification (S45 ENS) = 6 falsifications; post-codification = 0/session. Marketing-tier non-corroboration at primary is EXPECTED per Section 4.5 discipline boundary, NOT a (g') variance. *See A.12 for streak enumeration; current count in MEMORY.md; frameworks.md Section 11.11 for cross-chokepoint theme framework application.*

### 4.7 Refresh ingest log (`raw/notes/refresh_log.md`) (codified Session 104)

**Mandatory close-out step for every refresh ingest.** When a session re-ingests an EXISTING vault company page with a new primary source set (a "refresh ingest" per Section 4.1 / 4.2 — distinct from first-canonical creation, chokepoint/theme/relationship creation, codification, or in-place Tier-3 substrate refreshes), append a dated entry to `raw/notes/refresh_log.md` as part of the operational close-out, alongside `index.md` + `log.md` + MEMORY.md and before the final verification pass.

`refresh_log.md` is a cumulative, reverse-chronological reference of how each vault company's thesis evolves quarter over quarter — what changed since the prior baseline, why it mattered, placement changes, cross-vault propagation, and forward watch items. It complements `log.md` (every session, operational) by isolating refresh-specific analytical deltas for longitudinal reference; it builds up over time as a standalone resource.

**Per-entry template** (newest at top; canonical format lives in the file header):
`## S### — TICKER (Company) — YYYY-MM-DD — <period refreshed>`, then **Sources** / **Prior baseline** / **Headline** / **Key changes & new developments** / **Placement** (tier/layer change or "unchanged" + why) / **Cross-vault propagation** / **Forward watch** / **Key insight**.

Keep entries to Section 3.8 brevity discipline. Not in `index.md`; `refresh_log.md` updates do not count for accounting.

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

Pre-rework precedents: S22 [[VRT]] + S28 [[VIAV]] adjacent-infrastructure inclusion under photonics scope. S32-S35 codification arc (cpo-integration synthesis + InP-supply promotion + CLAUDE.md v8→v8.1 + log.md aggressive reduction with descending-order convention).

3-file Vic-authorized rework arc (2026-04-30 / 2026-05-01) per ownership exception: `_thesis.md` (AI compute → AI datacenter scope); `frameworks.md` v10 + v10.1 (multi-domain F6/F7/F8/F9/F10/F11; Caveats #1-9); CLAUDE.md v9 (multi-domain frontmatter; Outside generalization; Section 1.1 ownership exception). Detailed revisions in respective file notes.

Key structural observation: power infrastructure displaced compute as binding 2026 constraint (~50% of planned 2026 US datacenter builds delayed/cancelled per Bloomberg/Sightline; transformer 4-year lead times). Thesis reframed photonics-primary → dual-anchor compute + power infrastructure exposure.

VRT structural reclassification canonical: S22 baseline Tier 4 photonics "adjacent infrastructure" → AI datacenter scope reclassified Energy/Power Tier 1 per frameworks v10.1 (photonics_tier 4 preserved; energy_power_tier 1 added). First adjacent-infrastructure-now-primary placement.

### A.2 Path discrepancy verification empirical evidence *(cross-ref Section 1.3)*

Session 21 Phase 4 surfaced `agent_onboarding` directory naming gap (initial underscore creation; Claude Code naming validation required hyphens) and reference document location ambiguity (`raw/notes/` vs. `raw/references/`).

### A.3 Tier 1/Tier 2 framing gap — sub-pattern per-instance evidence *(cross-ref Section 3.4)*

Origination (S9-S10 + S22): MRVL Celestial acquisition gap; AVGO customer-owned tooling dismissal; AVGO rack leasing margin dismissal; CSCO Acacia disclosure gap. Risk-framing sub-pattern most empirically substantive.

Sub-pattern per-instance evidence (post-S75; enumeration formalized S61):
- Risk-framing (5 instances; codification threshold MET): AVGO COT (S10) + AVGO rack leasing (S10) + AXTI competitor risk (S13) + FLNC AI DC commercial structure (S60) + TSEM Intel relationship (S62: $313.5M termination + $300M NM mediation; call ZERO Intel mentions)
- Customer-concentration (1): MRVL Celestial (S9)
- Technology-content (1): CSCO Acacia gap (S22)
- Geographic-concentration (1 NEW post-S62): TSEM Israeli 20-F Item 3D (Feb 2026 Iran attacks operational impact on $920M SiPh capex; call ZERO Israeli commentary)
- Multi-sub-pattern historical attribution (1): BE S40 with 3 labels (customer-concentration + BTM thesis + manufacturing scale)

S52 reconciliation: pre-S46 "6+1" vs "7 counted" framing reconciled at S61 to post-S60 count = 7; post-S62 count = 9 combined. Cross-venue separately codified per Section 3.6. Current count in MEMORY.md.

### A.4 Counterparty-attribution-only annotation canonical examples *(cross-ref Section 3.5)*

Three modes empirically validated S20-S22:
- **Over-claim** — S20 [[GLW]]: NVDA-named partnership initially over-claim; Contour single-core fiber refined per FY2025 10-K
- **Inversion** — S21 [[FN]]: Tier 3 "central LITE/COHR partner" misdirected; primary sources document NVIDIA 27.6% + Cisco 18.2% top-2 concentration
- **Reciprocal-confirmation** — S22 [[VRT]]: NVIDIA partnership reciprocally confirmed at Tier 1 (10-K Item 7) + Tier 2 (Q1 2026 EcoDataCenter Sweden Vera Rubin + Vertiv OneCore)

Cross-domain elevation: S22 [[VRT]] reciprocal-confirmation structurally elevated under AI datacenter scope to F7 Tier 1 (Energy/Power) — first adjacent-infrastructure-now-primary placement (see A.1).

### A.5 Layer differentiation + Outside Framework 5 canonical text *(cross-ref Sections 3.9 + 3.10)*

**Layer 4 differentiation.** Layer 4 pages organize around product capability, capacity constraint, relationship leverage — different from Layer 1-2 (platform position + ecosystem control). Thesis role defines company via relationships to higher layers rather than own platform position. Customer concentration + manufacturing capacity carry more analytical weight at Layer 4.

**Layer straddling tension.** When revenue profile spans two layers (e.g., Layer 5 transceiver assembler with in-house Layer 4 laser manufacturing), maintain dominant-revenue tier in frontmatter; surface straddling as tension in Thesis role. Tier upgrade requires evidence non-dominant capability is commercially material (standalone revenue, merchant customer relationships, separate segment reporting) — not silent upgrade based on positioning evidence.

**Outside Framework 5 canonical pair:** [[COHU]] (S8) broad-cycle test-equipment + [[PLAB]] (S28) photomask supplier with broad semi infrastructure; AI advanced packaging as broad signal not photonics-specific; ZERO photonic foundry customer disclosure across 3 primary sources. Two-instance pattern supports codification per honest-verdict discipline.

### A.6 Tier 3-anchored theme page canonical example *(cross-ref Section 3.13)*

Session 19 `datacenter-photonics-supply-chain.md` creation; Sessions 20-22 cross-validation cycles produced concrete refinements (GLW multicore-fiber → Contour single-core; FN LITE/COHR-centric → NVDA + Cisco-centric; VRT NVIDIA-aligned → reciprocal-confirmation). Convention durability validated across three cycles without structural rewrite of source theme page.

### A.7 Parallel-but-independent paired-ingest variant canonical examples *(cross-ref Section 3.14)*

- **Session 27 [[CRDO]] + [[ANET]]** — networking-component adjacency at different layers (3 vs 5); 0 explicit / 2 structural co-locations
- **Session 28 [[VIAV]] + [[PLAB]]** — semi-infrastructure adjacency at same Layer 4 but different photonics-thesis fit (Tier 4 vs Outside F5); 0 explicit / 2 structural co-locations / 2 divergent / 1 untested

Variant validated across two consecutive paired-ingest sessions; structurally distinct from substantive paired analytical product.

### A.8 Foreign-issuer ingests — TSM precedent + multi-domain candidates *(cross-ref Section 4.2)*

[[TSM]] S1-S2 + S17 NVDA GTC refresh precedent (`scripts/fetch_filings.py` `forms: ["20-F"]`). S62 TSEM first foreign-issuer post-codification.

| Domain | Candidates | Framework placement |
|---|---|---|
| Memory | SK Hynix, Samsung Electronics (KRX) | F6 Tier 1 — HBM oligopoly |
| Photonics | TSEM (Israel ADR; ingested S62), ASE Tech (Taiwanese ADR), Aixtron (Germany XETRA) | F5 Tier 2-3 |
| Energy/Power | ABB (Swiss), Schneider (French SBGSF), HD Hyundai Electric / Hyosung (Korean) | F7 Tier 1-2 |
| Equipment | Anritsu (Japanese), Infineon (German ADR IFNNY) | F8 Tier 3-4 |
| Materials | Sumitomo Electric, JX Advanced Metals, SUMCO, Shin-Etsu, Ibiden (Japanese) | F9 Tier 1-3 |
| Other | Foxconn Interconnect Technology (HK) | F1 — assembly/contract manufacturing |

Foreign-listed candidates require IBKR foreign access decision per portfolio composition. Sequencing per Section 1.2.

### A.9 A6 vault-content-verification — pattern types + (g)/(g') sub-categorization *(cross-ref Section 4.5)*

Per-instance evidence: (a) S21 [[FN]] kickoff anticipated Layer 5; primary placed at Layer 6. (b) S24 ANET vault-presence verification. (c) S24 datacenter-photonics-supply-chain.md Section 2.5/2.6 shift. (d) S25 drift (`tier3_source:` / `related:` proposed fields). (e) S25 wikilink casing gaps. (f) S26 kickoff hypothesis falsification (Session 4 vs actual Session 6 AEHR). (g) S26 (5 stated vs 16 actual); S27 Hyperlume vs Comira naming sub-pattern. (h) S28 PLAB-10Q-2026-02-01.htm header validation + S59 FN filename-correct-content-wrong (2 instances post-S60).

(g)/(g') sub-categorization (S46): (g) Tier 3 figure variance — 8 instances through S45 (S40 BE + S42 BWXT + accumulated). (g') Kickoff drafting factual variance — 2 instances (S45 ENS 6 falsifications pre-codification + S47 FCEL Section 45X post-codification baseline). Discipline boundary canonical (S61): S60 FLNC Sunstack + Edgestack placed under "Structural context to verify at primary" — non-corroboration is EXPECTED outcome, NOT (g') variance.

Combined post-S75: 10 instances (8 (g) + 2 (g')). Current count in MEMORY.md.

### A.10 Honest-verdict trigger discipline precedent pattern *(cross-ref Section 2.1)*

4-non-firing baseline (S54-S59): [[COHU]] + [[ALAB]] + [[VIAV]] + [[GLW]]; 4-UPWARD reframing extensions (S62-S75): [[TSEM]] + [[NOK]] + [[AAON]] + [[MKSI]]. Combined post-S75: 4-UPWARD + 4-non-firing precedent pattern. Per-instance evidence + current count in MEMORY.md.

### A.11 Non-calendar fiscal year-end filer protocol — 7-instance month+ + 3-instance week-scope precedent *(cross-ref Sections 2.11 + 2.11.1 + 2.11.2)*

**Month+ scope baseline (Section 2.11 applied; 7-instance precedent post-S79):**

| Filer | Fiscal year-end | Vault scope |
|---|---|---|
| [[ENS]] (S45) | March 31 | New canonical |
| [[FCEL]] (S47) | October 31 | New canonical |
| [[VIAV]] (S58) | late June | Refresh |
| [[FN]] (S59) | late June | Refresh |
| [[FLNC]] (S60) | September 30 | New canonical |
| [[MOD]] (S70) | March 31 | New canonical |
| [[ARM]] (S76) | March 31 | New canonical (foreign-issuer; DUAL Section 4.2 + 2.11 application FIRST INSTANCE) |

5 new canonical + 2 refresh = 7-instance combined; methodology validated across both ingest type variants. 5 distinct fiscal calendars at month+ scope: Mar 31 (ENS + MOD + ARM) + Sep 30 (FLNC) + Oct 31 (FCEL) + late-June (VIAV + FN). Per-instance evidence at log.md S45/S47/S58/S59/S60/S70/S76.

**Week-scope baseline (Section 2.11 N/A; 3-instance precedent codified Session 79):**

| Filer | Fiscal year-end | Offset |
|---|---|---|
| [[NVDA]] (pre-S62 vault treatment) | Last-Sunday-of-January | ~1 month |
| [[AMD]] (S77) | Last-Saturday-of-December | ~4 days |
| [[INTC]] (S78) | Last-Saturday-of-December | ~4 days (EXACT match with AMD) |

3-instance week-scope precedent at Section 2.11 N/A baseline (substantively-calendar fiscal year treatment). **Cross-canonical EXACT-period-parity FIRST INSTANCE methodology** per Section 2.11.2: AMD + INTC Dec 27, 2025 + Mar 28, 2026 EXACT match enables direct cross-canonical comparative analytical product without offset reconciliation.

### A.12 Section 4.6 source discipline ROI streak *(cross-ref Section 4.6)*

Pre-codification baseline: S45 ENS = 6 material falsifications. Post-codification: S47 FCEL = 1; S48-S75 all 0 = 28 consecutive sessions. 16-instance streak at S61 → 29-instance post-S75 across full ingest-type variety (refresh + relationship creation + chokepoint creation + new canonical creation + theme creation + codification). Per-instance session enumeration + current count in MEMORY.md.