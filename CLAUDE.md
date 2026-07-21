# CLAUDE.md — stocks-wiki (v10.3)

A personal research vault for chokepoint and supply-chain analysis across **three thesis domains**: (1) **AI datacenter supply chain** — both photonics and power & energy; (2) **Humanoid Robots** — the embodied-AI value chain; and (3) **Defense & Drones** — unmanned systems. You maintain the wiki; the human curates sources and asks questions.

*Version: v10.3 (Vic-authorized 2026-07-19 per the Section 1.1 ownership-exception mechanism): ONE new rule added — **Section 3.21 demand-side / application-layer placement**, resolving the frameworks app-layer-gap flagged since MSFT S112 → NOW S113 → PLTR S114 → DDOG S188 (paired with frameworks.md Framework 10.1); Vic chose the looser inclusion bound (any material AI-datacenter demand-side participant). NO existing section or rule changed. Prior: v10.2 (structural simplification + ~300-line compaction, Vic-authorized 2026-07-02: micro-rules compressed in place, codification-history tags moved to the ledger (A.19), language conventions merged, duplication removed, paragraph stacks compacted to bullets; ONE new rule added — the Section 5.3 third-instance codification bar). Full history: `raw/notes/conventions-ledger.md` (A.13–A.20) + git.*

## Language conventions

**Descriptive language convention.** When referencing frameworks, tiers, caveats, or sections in prose, use descriptive names rather than numerical shorthand: pair the number with descriptive scope on first reference ("Energy/Power Tier 4 specialty component supplier scope"), descriptive name alone after. Frontmatter YAML fields keep numerical values. Prospective from Session 46 (Sessions 1-45 pages not retroactively updated). **Plain language.** Use simple, everyday words — in chat AND wiki prose. Pick the easy word over the hard one: "backs up / supports / agrees with / matches" not "corroborates"; "the real bottleneck" not "the binding constraint"; "shows" or "proves" not "substantiates / validates" where plainer; "uses" not "leverages"; "about" not "regarding"; "approve / sign off" not "bless"; "group / part of the portfolio" not "sleeve"; "what would prove it wrong" not "falsifier / falsifiable"; "the verified wiki pages / our confirmed knowledge" not "canon" (in chat — "canonical" stays as the technical page-status term where load-bearing, with a plain gloss on first use); "protective" not "defensive" (in the hedging sense). Keep sentences short — one idea each. The wiki keeps its analytical third-person voice, but plain does not mean vague. (Vic-flagged word list, 2026-06-03 → 2026-06-12; sibling to the Section 3.16 word discipline.)

## 1. Foundation

### 1.1 The anchor

`wiki/_thesis.md` is the evaluation point for everything. Every ingest, new page, or update should strengthen, challenge, or refine the thesis; if an action does none, flag before proceeding. The human owns `_thesis.md` — never edit it yourself. `raw/notes/frameworks.md` is similarly human-owned — frameworks are interpretive scaffolding; primary sources *enrich*, not override. When framework structures and primary-source evidence diverge, raise it on the relevant page rather than silently reconciling. **Ownership exception:** both files underwent Vic-authorized reworks via collaborative chat drafting (`_thesis.md` 2026-04-30; `frameworks.md` v10.1 2026-05-01); default ownership resumes for all subsequent sessions — agents must not propose collaborative editing without an explicit Vic-authorized rework-session declaration.

### 1.2 Vault scope

**Three thesis domains**, each with its own human-owned `_thesis` + `frameworks` anchor pair (all human-owned per Section 1.1): (1) **AI datacenter supply chain** — `wiki/_thesis.md` + `raw/notes/frameworks.md` (founding/primary); (2) **Humanoid Robots / embodied-AI** — `wiki/_thesis-humanoid-robot.md` + `raw/notes/frameworks-humanoid-robot.md` (humanoid-first → "physical AI" later; anchors v0.2 LIVING, reworked S145); (3) **Defense & Drones / unmanned systems** — `wiki/_thesis-defense-drones.md` + `raw/notes/frameworks-defense-drones.md` (drones-first; munitions, European rearmament, directed-energy sequenced later). All CLAUDE.md conventions apply to all three.

**Dual-/tri-thesis pages.** When a company sits in more than one chain, add the extra domain's framing + its `*_tier` to the existing page — never duplicate (e.g. [[MP]] tri [AI/materials + defense + humanoid]; [[HARMONIC]] tri; [[AMD]] / [[NVDA]] / [[PLTR]] dual). **`*_tier` asymmetry:** AI uses per-sub-domain `*_tier`; Defense uses `defense_tier`; Humanoid has **no `humanoid_tier` field (YAGNI)** — humanoid names land `outside` the frameworks + theme-anchored to [[humanoid-robot-value-chain]], or carry another domain's tier where cross-thesis (HARMONIC `equipment_tier 4` + `defense_tier 4`; TUOPU `energy_power_tier 4`). Current AI-datacenter scope: compute, photonics, memory, energy, power, equipment, materials, and more. Binding 2026 constraint per _thesis.md: power infrastructure (~50% of planned 2026 US datacenter builds delayed/cancelled; 4-year transformer lead times). Framework structures (frameworks v10.1): F5 photonics, F6 memory, F7 energy/power, F8 equipment, F9 materials (provisional), F10 CAPEX flow, F11 cross-chokepoint themes. Per-domain `*_tier` lets cross-domain participants carry several classifications (examples in Section 3.2). **Outside-scope counterpoint placements:** [[COHU]] + [[PLAB]] (Outside Framework 5); the convention applies to Frameworks 5/6/7/8/9; counterpoint inclusion does not expand scope (see Section 3.10). **Scope expansion** is opportunity-sequenced (source availability, thesis development, time-bounded events), not pre-codified; domain-specific Tier 3 framework sources are Vic-curated as expansion proceeds. *See A.1.*

### 1.3 Structure

```
raw/         # source material — read from, never modify
  filings/<TICKER>/      # SEC filings grouped per ticker (+ flat newly_fetched/ staging)
  transcripts/<TICKER>/  # earnings-call transcripts grouped per ticker
  research/ news/ notes/ references/
wiki/        # your domain — write, update, interlink
  _thesis.md companies/ chokepoints/ themes/ trackers/ relationships/
index.md     # catalog of wiki pages
log.md       # append-only record of activity
```

**Operational layers:** `prompts/` + `scripts/` are operational infrastructure, not vault content — never ingest from them. The `raw/notes/` folder contains human's prior conversations and framework notes: analytical frameworks treated as authoritative until human revises (primary sources enrich, not refute); factual claims from notes treated as working hypotheses — confirm or revise against primary sources.

**Claude Code operational memory.** Persistent memory file at `~/.claude/projects/.../memory/MEMORY.md` outside vault. Cross-session context continuity (compressed mirror of `log.md`, structural notes, conventions, cumulative monitoring counts per Section 3.8). Must not contain independent analysis affecting wiki pages without Stop 1/Stop 2 protocol. Not in `index.md`/`log.md`; updates do not count for accounting.

**Path discrepancy verification.** Verify path conventions before committing new vault paths (*See A.2*):
- **The filename convention is the load-bearing invariant:** every raw source is `TICKER-FORM-PERIOD.ext` (`AVAV-10Q-2026-01-31.htm`) or `TICKER-earnings-DATE.ext` (`AVAV-earnings-2026-03-10.pdf`). The ticker prefix drives *both* the per-ticker folder grouping *and* `fetch_filings.py`'s skip-check, so naming must hold for every file — including Vic-staged transcripts. (The template `raw/transcripts/AXXX-earnings-YYYY-MM-DD.pdf` is a reference artifact, not data — leave it.)
- **Folder shapes:** skill dirs use hyphens (`.claude/skills/agent-onboarding/`); raw subdirs use no separators. `raw/filings/` + `raw/transcripts/` group into per-ticker uppercase subfolders (`raw/filings/MP/MP-10K-2025-12-31.htm`); `raw/filings/newly_fetched/` stays flat as the fetch/ingest staging queue. Deeper per-year/quarter nesting is deferred (YAGNI) — revisit only if one ticker exceeds ~50 files.
- **File locations:** skills → `.claude/skills/<skill-name>/SKILL.md`; reference docs → `raw/references/`; session prompts → `prompts/`; Vic-authored synthesis → `raw/notes/`.

## 2. Discipline

### 2.1 Four disciplines

- **Host tensions honestly.** When human holds a position and the wiki's analysis suggests weak structural fit, the page states this plainly. Uncomfortable conclusions are the point of the wiki, not a bug.
- **Describe, don't recommend.** Pages analyze structural position, competitive dynamics, evidence. They do not prescribe buying, selling, or holding. "Should I sell X" gets reframed to "what would have to be true for X's thesis to still be intact."
- **Thesis tool, not portfolio tracker.** No P&L, no position sizes, no cost basis, ever. A reader should not be able to tell what the human owns from reading the pages.
- **Honest-verdict discipline.** When a company's thesis fit is weak, the page states the weak fit plainly rather than constructing thesis-relevance narratives from generic positioning. Weak-fit pages may be shorter and verdict-like. Inclusion may be for trajectory or counterpoint rather than thesis centrality. Surface clearly in Thesis role.
- **Honest-verdict trigger discipline.** A baseline-reframing trigger (Caveat #9 Layer 4-5 straddling upgrade; Outside Framework reframing; framework placement; A1 mode upgrade to reciprocal-confirmation) fires ONLY when evidence meets its pre-registered criteria — **NOT on directional momentum.** Assessing evidence honestly against the threshold and NOT firing despite suggestive evidence is the canonical methodology; UPWARD reframing follows the same rigor. Cross-reference Section 3.5. *See A.10; current count in MEMORY.md.*
- **Mid-fiscal-year disclosure methodology shift pattern.** When a company restructures segments mid-fiscal-year OR retrospectively adjusts prior-period segment data: document the shift explicitly, apply restated comparatives at financial snapshot tables, and flag cross-period comparison complexity — never paper over the shift with blended-period framing; preserve segment-tier comparability boundaries at the shift date. *Precedent: See A.15.* **Venue-asymmetric sub-pattern:** a shift may appear at one venue (call presentation + investor website) while another preserves the prior framework (10-Q segment reporting) — document the venue-asymmetry at Source audit notes; cross-reference Section 3.6 when it constitutes a true cross-venue gap beyond reporting-venue lag.

### 2.2 Source hierarchy

When sources disagree on facts, higher tier wins. On interpretation, triangulate and flag the disagreement on the relevant page. Skip promotional content and aligned commercial incentive.

- **Tier 1 — Primary filings:** 10-K, 10-Q, 20-F, 8-K, proxies. Ground truth.
- **Tier 2 — Primary commentary:** Earnings calls, analyst days, conference appearances. Colored by management incentives.
- **Tier 3 — Independent analysis:** SemiAnalysis, Stratechery, reputable sell-side, industry reports. Cite, don't treat as fact.
- **Tier 4 — News:** Bloomberg, WSJ, Reuters, FT. Reliable for events, shallow on thesis.
- **Tier 5 — Social/forums:** Twitter/X, Reddit, blogs. Signal for generating questions; never cited.

*Tier 1/Tier 2 calibration.* Factual data (financials, concentration, capacity, legal, geographic) — Tier 1 authoritative. Competitive assessment, strategic intent, management signaling — Tier 2 often more analytically informative than Tier 1's legal-conservative framing. *Analyst silence as signal* — asymmetry between venues (risk in 10-K but unaddressed in analyst Q&A) is meta-signal about investor community processing; document in Source audit notes. *Source unavailability as observation* — when an expected source is unavailable, document explicitly with analytical implications; inability to test patterns requiring that source is itself a finding.

### 2.11 Non-calendar fiscal year-end filer protocol

Non-calendar fiscal year-end filers require period-parity discipline at calendar terms. **Primary:** compare cross-vault periods by **calendar-quarter equivalence** regardless of fiscal-year designation (FLNC Q2 FY2026 = calendar Q1 2026); apply at Phase 0; document the equivalence in the Source audit notes per-source entry. **Secondary (honest framing):** preserve the fiscal-year designation at source filenames + financial-table headers; annotate the equivalence ("Q2 FY2026 = calendar Q1 2026") in Thesis role at first cross-vault comparison. *Rosters + fiscal calendars: See A.11.*

#### 2.11.1 Substantive-offset threshold methodology

Threshold by fiscal-year-end offset from Dec 31: **week-scope (~3 days to ~1 month) = N/A** (treat as substantively-calendar — NVDA, AMD, INTC); **month+ (≥1 month) = apply Section 2.11.** *Edge cases + roster: See A.11.*

#### 2.11.2 Cross-canonical EXACT-period-parity comparative analytical product methodology

When two vault canonicals share an EXACT-match fiscal calendar (identical period-end dates), direct cross-canonical comparison is enabled without offset reconciliation; document the match in Thesis role + the cross-vault adjacency section. *See A.11.*

## 3. Page conventions

### 3.1 Page types and creation triggers

Page types: companies / chokepoints / themes / trackers / relationships. (The `layer` page type was retired unused at v10.0 — Framework 2 layer content lives in `frameworks.md` plus the company-page `layer` field; per-instance rationale in the conventions ledger.)

A new page exists because a source informed it, not because a company name came up. Companies not in seed portfolio: first mention gets a note inside primary page; promote to own page when entity referenced by 3+ sources or central to identified chokepoint/theme. Never create empty stub pages. **Filenames:** companies use uppercase tickers (`TSM.md`); chokepoints / themes / trackers / relationships use kebab-case (`TSMC-CoWoS.md`, `CPO-platform-battle.md`, `forward-edge-tracker.md`, `TSM-NVDA-allocation.md`).

### 3.2 Frontmatter

```yaml
---
type: company | chokepoint | theme | tracker | relationship
tickers: [TSM, NVDA]
layer: 1-6                # company pages only
photonics_tier: 1-5 | outside   # per-domain *_tier fields all optional; also:
memory_tier: 1-5 | outside      # energy_power_tier, equipment_tier,
materials_tier: 1-5 | outside   # materials_tier (provisional)
defense_tier: 1-4 | outside     # defense/drones; Option A taxonomy note below
foreign_issuer: true            # non-US-domiciled filers only
last_updated: YYYY-MM-DD
---
```

**`layer` field vs. layer page type.** The `layer: 1-6` company-page field (Framework 2 placement) is load-bearing and unchanged; only the never-used layer *page type* and its folder were retired at v10.0. `layer` (Framework 2) and the per-domain `*_tier` fields (Frameworks 5/6/7/8/9) are distinct from source `Tier`; multi-domain companies carry multiple `*_tier` classifications (TSM photonics_tier 1 + memory_tier 1 + equipment_tier 2; VRT photonics_tier 4 + energy_power_tier 1). For multi-layer exposure, use a single primary `layer` value with nuance in body prose. For non-company pages, `tickers` lists tickers whose primary sources substantively informed page content (provenance, not a relevance tag). **Frontmatter convention reinforcement.** (a) `foreign_issuer: true` — apply on company pages for non-US-domiciled filers (foreign private issuers + MJDS Canadian filers); absent on US-domiciled (default; S43 CCJ precedent). (b) `tickers` — single-ticker scope on company pages; multi-ticker scope on chokepoint/theme/relationship pages where multiple tickers' primary sources informed content (provenance, not relevance tag; S44 HALEU-fuel-chokepoint precedent). (c) `*_tier` application — apply per-domain field only when company has substantive exposure to that domain, not derivatively (do not assign memory_tier to NVDA because NVDA buys HBM; do assign to MU/SK Hynix/Samsung as memory-domain operators). `outside` is honest-verdict-correct per Section 3.10 four-criterion test (S36 FLEX precedent).

**`defense_tier` convention (Option A taxonomy).** Classifies Defense & Drones companies per the four investability/structural-position tiers in `raw/notes/frameworks-defense-drones.md` Framework D2: **1 = prime with drone-relevant programs of record; 2 = mid-cap pure-play / specialist; 3 = speculative micro-cap (apply Framework D6 financial-quality screen); 4 = supply-chain / materials enabler (chokepoint owner).** **Semantics — unlike the AI `*_tier` fields, the number is NOT a conviction/quality rank:** Tier 4 enablers carry the *highest* structural conviction (they own the chokepoints). Conviction tracks the chokepoint-quality gradient (Framework D5: geology/physics > policy), not the tier number. `outside` is honest-verdict-correct for defense-adjacent names with weak unmanned-systems fit. Apply per the (c) substantive-exposure discipline above; dual-thesis pages (MP / AMD / NVDA / PLTR) carry `defense_tier` alongside their AI `*_tier` fields.

### 3.3 Voice, wikilinks, citations

- **Voice.** Analytical third person. No first/second person, no investment prescriptions.
- **Wikilinks.** Short form `[[TICKER]]` or `[[page-name]]`. Every ticker/chokepoint/theme mention gets linked. Pages do not wikilink to themselves. Forward wikilinks acceptable; do not create stub pages to resolve them. Add at least one inbound link from existing page when creating a new page.
- **Citations.** Every numerical claim and non-obvious substantive claim names source and period — e.g. *CoWoS capacity expansion (TSM Q1 2026 call)*. Per-claim citations remain correct as pages accumulate multi-source content; do not substitute header-level citation notes.
- *Rhetorical vs. factual.* Factual claims (verifiable numbers, confirmed events) paraphrased in wiki voice with citation. Rhetorical claims (directional assertions, promotional framing) attributed to speaker — "Jensen claimed...", "management characterized...". When in doubt, attribute. Source audit notes + Change log track overall page provenance; cross-source synthesis statements name all involved sources.
- *Disclosed/inferable/unknown.* For unnamed entities ("Customer A," "a significant customer"): (1) Disclosed — exact data from filing; (2) Inferable — patterns matching publicly known profiles, hedged language only ("consistent with," "resembles"), never assertive; (3) Unknown — what filing does not disclose.
- *Disclosure lifecycle awareness.* Topics may appear in management commentary (Tier 2) before regulatory filings (Tier 1). Same-day divergences are meta-signal about disclosure lifecycle. Document in Source audit notes when observed.

### 3.4 Tier 1/Tier 2 framing gap convention (A4)

Distinct from Disclosure lifecycle awareness. Covers cases where a Tier 1 filing and the Tier 2 earnings call frame the same risk or commercial topic materially differently. Pattern types: (a) filings flag a risk that calls dismiss; (b) filings omit commercial detail that calls disclose extensively; (c) filings acknowledge margin-compression risk that calls dismiss with rhetorical deflection. Document prominently in Source audit notes with the "Tier 1/Tier 2 framing gap" label; instances compound — three or more is analytically significant beyond any individual disclosure. **Sub-pattern annotation (4 sub-patterns):** risk-framing gap (risk in 10-K Risk Factors but dismissed on call); customer-concentration gap (concentration in 10-K Notes but not on call); technology-content gap (10-K Item 1 detail not on call); geographic-concentration gap (10-K MD&A/Item 1 concentration not on call). Codification threshold 3+ instances per sub-pattern. Cross-venue sub-pattern is separately codified per Section 3.6 (A4-bis; distinct convention). *See A.3; current count in MEMORY.md.*

### 3.5 Counterparty-attribution-only annotation (A1 three-mode framing)

When Tier 3 sources cite counterparty-side announcements about ecosystem partnerships, wiki text annotates cross-validation status per three-mode framing. Apply at first instance during Tier 3-anchored theme page construction; refine at primary-source ingest cross-validation. *See A.4 for canonical examples.*

- **Over-claim:** counterparty-side announcement not bilaterally confirmed. Annotate: *"named in [counterparty] [venue]; not reciprocally confirmed in [target] primary sources."*
- **Inversion:** counterparty-side projection structurally misdirected. Annotate: *"characterized as [framing X]; [target] primary-source disclosure shows [framing Y]."*
- **Reciprocal-confirmation:** counterparty-side claim bilaterally confirmed. Annotate: *"named in [counterparty] [venue]; reciprocally confirmed in [target] primary sources [citation]."*

### 3.6 Cross-venue disclosure gap convention (A4-bis)

Distinct from the Tier 1/Tier 2 framing gap (Section 3.4): this addresses divergence between two **non-filing** venues — typically a conference vs a near-concurrent earnings call (information disclosed at an industry conference / GTC keynote / technology day / investor day but not addressed at adjacent earnings calls or the 10-Q).

- **Detection + documentation.** The gap is information, not absence. Flag venue-specific gaps in Source audit notes with the "cross-venue gap" label + per-venue disclosure scope.
- **Honest framing ("silence ≠ retreat") + falsification.** Do not read venue-specific silence as an architectural shift or retreat: if the disclosure venue (GTC, technology day) keeps carrying the topic across cycles, the venue-specific pattern — not a quarter-over-quarter erosion signal — is the canonical framing. Falsification: the pattern holds WHILE the durable venue keeps the topic; IF that venue itself stops (e.g., GTC March 2027 zero CPO mentions after GTC March 2025 + 2026 substantiation), it transitions from venue-specific silence to genuine retreat.
- **Cross-reference scope.** Ties to Section 2.1 honest-verdict + Section 3.4 framing gap (distinct: cross-venue is venue-asymmetric, framing gap is tier-asymmetric) + the Section 2.1 venue-asymmetric sub-pattern. *Precedent: See A.16.*

### 3.7 CEO combativeness as Tier 2 meta-observation (monitoring)

When a CEO answers a structurally reasonable analyst question with unusually defensive or dismissive language beyond standard deflection, note it in Source audit notes (exact wording, per the rhetorical-claims convention) as a signal of which competitive pressures bite — descriptive, not diagnostic; do not adjudicate the cause. Status: monitoring pending third instance; count in MEMORY.md.

### 3.8 Source audit notes + Change log

- **Source audit notes.** Standard section on every company page created or substantively updated from a primary source. Optional on theme/chokepoint pages. Captures observations about the source itself — management tone shifts, analyst framing, conspicuous absences, unanswered questions, what went unquantified. Place before Change log. For multi-source pages, maintain per-source entries (dated, source-attributed).
- **Change log.** At bottom of each page. Track what was added/changed in each ingest with dated line. Makes staleness and evolution visible at a glance.
- **Brevity discipline.** Change-log entries, source-audit per-source entries, and log.md session entries are SHORT — operational essentials only. **Targets:** 1-3 sentences (change log) / 2-5 sentences (source-audit per-source) / ~15-25 lines (log.md session). **Goes in:** date + session; what was created/updated; placements applied (layer + tier); convention-codification observations; one-line key finding if structurally significant. **Does NOT go in:** Phase 4 reflection; multi-paragraph synthesis; cross-company analytical detail; full source-audit content; convention quotations; per-instance empirical evidence; A1 three-mode detail. Canonical analytical content lives in Thesis role + middle sections + Open questions — Change log + source audit + log.md track *what changed*, not *what the analysis was*. Prospective from S38+; existing oversized entries not retroactively trimmed.
- **Enforcement + telemetry relocation.** The 1-3 sentence change-log cap is HARD, enforced at composition (entries had drifted to 40-50-line summaries). Two rules: (1) a company-page change-log entry records only *what changed on this page* (sections added/updated, placement decisions, resolved open questions, the one key finding); (2) **process telemetry never appears on company pages** — streak counts (Section 4.6 ROI, wikilink-clean), A6 sub-pattern counts, framing-gap/CEO-combativeness tallies, protocol meta-notes live ONLY in `log.md` + `raw/notes/conventions-ledger.md`. A reader of a company page should find company knowledge, not vault bookkeeping. Existing oversized entries are trimmed at each page's third-refresh compaction (Section 3.19), not in a retroactive sweep.

### 3.9 Company page structure

Five sections universal: Thesis role, Financial snapshot, Open questions, Source audit notes, Change log. Middle sections (technology roadmap, capacity, ecosystem, demand, competitive positioning, supply chain) vary by company type and layer. Do not force a rigid universal template; structure follows analytical significance. *Layer 4 differentiation + Layer straddling tension: see A.5.*

### 3.10 Outside Framework placement (per-domain generalization)

`<framework>_tier: outside` is honest-verdict-correct designation when source evidence shows weak fit on a specific per-domain framework. Applies to Frameworks 5/6/7/8/9 per frameworks v10.1.

**Four-criterion test (canonical Framework 5; substitute domain-specific equivalents for F6/F7/F8/F9 per criterion 1):**
1. ZERO domain-specific customer disclosure (photonic foundry / IC / SiPh for F5; named hyperscaler / datacenter-power for F7).
2. Domain mentions appear as broad market enumeration rather than named served segments.
3. AI exposure is broad-cycle subsegment rather than domain-direct.
4. Customer concentration is generic rather than domain-specific.

**Multi-domain Outside + counterpoint role.** A company may carry Outside on several per-domain frameworks at once (COHU Outside F5 + F8; TSEM Outside F7 + F8 + F9), strengthening honest-verdict-correctness. Vault inclusion is for trajectory or counterpoint (e.g., the equipment-tier split between AI-exposed [[AEHR]]/[[ONTO]]/[[VIAV]] and broad-cycle [[COHU]]/[[PLAB]]), not thesis centrality; Outside names are excluded by default from a domain-specific theme's Future-ingest list, and the Thesis role carries an Outside-placement justification subsection per the four-criterion test. **Promotion mechanism (Outside → Tier 4):** warranted when source evidence surfaces domain-specific structural exposure meeting per-framework triggers (F5 canonical: 2+ photonic-foundry customers named; OR >15% revenue from photonics; OR triggers pre-registered in Open questions). *See A.5 for the COHU + PLAB canonical pair.*

### 3.11 Displacement analysis

When a company's core business faces structural displacement from a tracked technology transition (e.g., pluggable transceiver assembler facing CPO displacement), a dedicated displacement analysis section may be warranted. Surface: structural tension, management's threat framing (silent / reframed / acknowledged), analyst coverage patterns, displacement vulnerability factors, timing gaps vs. adjacent companies. Optional — add only when displacement is thesis-central.

### 3.12 Theme page types

Three types from practice: **Dynamics themes** (evolving competitive/market dynamic; e.g., `AI-demand-durability.md`, `foundry-competition.md`); **Mechanism themes** (how a company maintains/challenges structural position; e.g., `NVDA-platform-integration.md`); **Absence themes** (thesis-significant topic primary sources are not yet addressing; e.g., `CPO-platform-battle.md`). Future ingests may surface other legitimate page types. **Tracker carve-out (v10.0):** cross-vault status-bearing pages formerly typed as themes (hyperscaler-capex, china-exposure, forward-edge-tracker) are now `type: tracker` per Section 3.20; the three theme types here cover analytical content only.

### 3.13 Tier 3-anchored theme pages (A2)

A theme page may be anchored on Tier 3 synthesis sources when primary-source-anchored creation is premature but cross-cutting analytical content exists. Structural requirements: (1) Vic-authored synthesis as anchor with attribution explicit in body + frontmatter; (2) Counterparty-attribution-only annotation per three-mode framing (Section 3.5); (3) no verification at construction, deviation-based refinement at ingest; (4) Open questions pre-registers primary-source verification triggers. **Multi-domain Tier 3 sources:** existing canonical `raw/research/photonics-chokepoint-table.md`; additional Tier 3 sources (memory, energy/power, equipment, materials) Vic-curated as expansion proceeds, anchoring theme pages per the same A2 conventions. *See A.6 for the canonical example.*

### 3.14 Paired ingests

When two companies sit at adjacent positions in the value chain, paired ingest covers both in single session. Use when: thesis roles structurally similar; paired comparison generates content not available from either source alone; source period alignment reasonable. Two-stop protocol typically warranted; middle sections allowed to differ.

**Variant selection.** Stop 1 evaluates explicit cross-company candidates (shared customers, supplier-customer dependencies, reciprocal partnerships, structural co-positioning): **2+ explicit → substantive paired** (S6/S13 pattern); **1 explicit → optional, Vic decides**; **0 explicit (with co-locations) → parallel-but-independent** (S27/S28 variant: no dedicated cross-company section; brief structural co-location framing in Thesis role; brief cross-references rather than forced synthesis). *See A.7.*

### 3.15 Provisional and canonical chokepoint pages

A chokepoint page may be created via two pathways:

**Pathway 1 — Provisional → canonical promotion.** Provisional chokepoint page created from a single company's primary sources when structural constraint evidence is strong but designation is provisional. Requirements: (1) page-top italic disclaimer naming sources + provisional scope; (2) "What would confirm or weaken this framing" section pre-registering cross-validation tests; (3) no Open questions or Source audit notes sections (those belong on company pages). When substantiated by a second source, provisional disclaimer removed.

**Pathway 2 — Canonical-from-first-creation.** Canonical chokepoint page created at first-creation when the substantiation threshold is met: (a) a Tier 3 anchor source explicitly establishing the chokepoint structural framing OR (b) 3+ vault primary-source canonical pages substantively documenting the constraint scope OR (c) equivalent multi-source coverage (e.g., [[liquid-cooling]] = 6-canonical participant scope). Provisional stage skipped; standard canonical section structure applied (Open questions + Source audit notes + Change log; NO provisional disclaimer or "confirm/weaken" section). Honest framing per Section 2.1: substantive primary-source substantiation drives Pathway 2 — not directional momentum toward canonical placement without threshold met. **4-canonical strengthening:** 4+ canonical participants reinforce Pathway 2; the 3-canonical threshold is unchanged. *Precedent + structural-type taxonomy: See A.17.*

**Pathway selection.** Default to Pathway 1 when source coverage is single-company; Pathway 2 when multi-source threshold met at session start. Verification at Stop 1 Phase 0 per Section 4.5 A6 sub-pattern (b).

### 3.16 Language convention — "substantive" / "substantively" discipline

Default to direct language. Use "substantive" / "substantively" only where the word distinguishes Tier 1 primary substantiation from Tier 3 hedging or weak-fit assertion — marking something genuinely material vs marginal, not for emphasis. **Deletion test at composition:** each candidate asks "does this word add meaning here, or just emphasis?" — if emphasis, delete. If drift surfaces in a session output, surface it honestly in Phase 4 reflection; do not retroactively claim "load-bearing usage" for instances that fail the test. Prospective from Session 86; prior usage preserved as historical artifact (forward-only per Section 3.8). Cross-reference Section 3.3.

### 3.17 Latest-alpha digest block on company pages

A company page MAY carry one quarantined between-filings digest block, written only by a `/latest-alpha` run (never during a canonical ingest). Reference instances: [[AAOI]] + [[GLW]].

- **Format (fixed):** fenced between `<!-- LATEST-ALPHA:START -->` / `<!-- LATEST-ALPHA:END -->` markers, placed immediately before Change log. Header line carries the ⚠️ unverified label + as-of date; body is tier-tagged bullets each with a `[verify: …]` trigger naming where the item gets checked at the next primary source; one explicitly-labeled "signal only (not weighted)" line for price/sentiment items; link to the full discovery note in `raw/notes/latest-alpha/`.
- **Rules (load-bearing):** (1) the block never touches frontmatter — `last_updated` reflects canonical ingests only; (2) wikilinks only to existing pages; (3) **graduation/decay keyed off "already in canon," never the `last_updated` date** — at the next canonical ingest, each item either graduates (verified → absorbed into canonical sections) or is pruned; the block never accumulates across quarters; (4) discovery-only tier discipline per Section 2.2 — nothing in the block is citable as vault fact. **Operational default (US-listed):** run `/latest-alpha` as the pre-refresh scouting step for any name whose refresh is due; the digest block becomes the verify-list the refresh ingest works through.

### 3.18 Forward-edge layer — consensus-divergence tracker

The vault runs on three information layers. (1) **Canon (verified)** — 10-K/10-Q/call primary sources; backward-looking ground truth; the backbone that keeps the rest honest. (2) **Latest alpha (timely)** — 8-K/conference/news between filings; closes the lag; quarantined discovery-only (Section 3.17). (3) **Forward edge (variant view)** — where the vault's structural read differs from what the market prices, with the **catalyst** that forces a re-rate and the **falsifier** that proves the vault wrong. Layer 2 feeds Layer 3's catalysts; Layer 1 verifies or falsifies a Layer 3 entry (a refresh ingest confirms a catalyst or trips a falsifier). **Artifact.** The forward edge lives in ONE cross-vault, canon-grade tracker page — `wiki/trackers/forward-edge-tracker.md` (`type: tracker`; conventions per Section 3.20) — organized by domain, curated to high-conviction divergences only. It **extends, not duplicates**, the three theses' "what would prove this thesis wrong" sections + the chokepoint-quality gradient (already latent there; this surfaces them in one structured place). Agent-maintainable as canon analysis — updated when a latest-alpha run surfaces a catalyst, a refresh ingest confirms/falsifies an entry, or on request; NOT auto-written by the latest-alpha skill.

**Entry format (six fields, fixed order):** subject + durability anchor (chokepoint-quality gradient) → **Consensus** (Tier 3/4) → **Vault view** (primary-grounded, linked) → **Catalyst / timeline** → **Falsifier** → **Last moved** (date + what changed). **Entry contract: every entry MUST carry a catalyst AND a falsifier** — no falsifier means it is a hot take, not an entry. Curated to high-conviction only, not every name.

**Discipline guardrails (load-bearing):**
- **No price/valuation, ever.** "Consensus" is described as a **structural narrative** ("the market prices NVDA as the durable AI winner; treats power as adjacent") or via an **observable mechanism** (lead times, interconnection queues, bond yields, order-vs-capacity) — **never** stock price, market cap, valuation multiples, or analyst price targets. Price action / price targets stay "signal only (not weighted)" in the Section 3.17 latest-alpha blocks, never here. Reinforces Section 2.1 thesis-tool-not-portfolio-tracker + describe-don't-recommend.
- **Tier discipline (Section 2.2 / 4.6).** Tag the Consensus line Tier 3/4 (cite, don't treat as fact); primary-ground the Vault-view + Falsifier lines with citations to thesis / chokepoint / company pages.
- **Honest-verdict (Section 2.1).** If the vault view is weak or consensus is right, say so — do not manufacture a contrarian take to fill a slot.
- **Human-owned anchors untouched.** Reference and link the `_thesis*` files; never edit them (Section 1.1). Cross-reference Section 3.6 (cross-venue gap), Section 3.12 (absence themes), Section 3.15 (confirm/weaken framing), Section 3.17 (latest-alpha digest block).

### 3.19 Page lifecycle conventions — rolling snapshot, open-questions lifecycle, third-refresh compaction

Three rules that keep company pages from growing without bound across refreshes. Scope: applied at each US-listed page's next refresh (no big-bang retroactive sweep); foreign-issuer pages adopt the same rules at their next refresh.

- **(a) Rolling financial snapshot.** Full per-period tables are kept for the **latest annual + latest two quarters** only. At each refresh, periods older than that compress into a one-line-per-period **trajectory strip** (a single table: period × revenue × the page's one or two load-bearing metrics × one-phrase note). Cross-period deltas survive; table accumulation does not. Section 4.1's separate-tables-per-period rule applies to the periods kept in full.
- **(b) Open-questions lifecycle.** At each refresh, questions fully RESOLVED move out of the section into that refresh's change-log entry as a one-line disposition ("OQ2 resolved — 800G first volume shipped Q1"); remaining questions renumber. PARTIALLY RESOLVED questions stay, rewritten to their live remainder. The section is a true watch-list: every item still actionable, each with its pre-registered trigger.
- **(c) Third-refresh compaction.** At a page's third refresh (and every third thereafter), prune superseded analysis: collapse narrative that later periods overtook, merge duplicate cross-reference notes, trim oversized historical change-log entries to the 1-3 sentence cap (the one retroactive trim Section 3.8 authorizes). What is removed is summarized in one change-log line. Mirrors the Section 5.3 forward-only growth discipline at page scope. Compaction never removes: the honest verdict, placement rationale, pre-registered triggers, source audit notes, or anything a current Open question depends on.

### 3.20 Tracker pages — `wiki/trackers/`

A **tracker** is a cross-vault page whose value is *current status*, not narrative analysis. The folder exists because trackers carry a different maintenance obligation than themes — a stale tracker is worse than no tracker (it falsely reassures). **Membership test (all three must hold):** (1) **cross-vault** — spans multiple companies/domains, no single ingest "owns" it; (2) **status-bearing** — entries carry live state (fired / not fired, last-moved dates, signal checklists) that decays if unmaintained; (3) **propagation-updated** — updated when *other* pages' ingests touch a tracked signal, never the subject of its own ingest. Pages failing any criterion are themes (Section 3.12). Folders encode operational difference only; topic/domain stays in frontmatter + index.md — no domain subfolders, here or elsewhere. **Roster at codification:** [[forward-edge-tracker]] (conventions per Section 3.18), [[hyperscaler-capex]], [[china-exposure]], [[what-could-go-wrong]].

**Freshness obligation.** When a canonical or refresh ingest touches a tracked signal or cohort name, the affected tracker entry updates status + last-checked **in the same session** — this is part of cross-vault propagation, not optional polish. Change log required; Source audit notes optional (same as theme pages, Section 3.8 brevity discipline applies). **`what-could-go-wrong` conventions (the vault-level risk register).** Tracks the factors that could break the three theses + frameworks. **Dashboard-not-duplicate rule:** every falsifier has ONE canonical home (a `_thesis*` file, theme, chokepoint, or company page); the register links there and adds only status — never restating the analysis, so the copies can't drift. **Entry format (six fields, fixed order):** Risk (what breaks) → Domain(s) → Canonical home (wikilink) → Tripwire (observable mechanism — guidance cuts, lead-time normalization, utilization shifts, policy expirations; **never price/valuation**, per Section 3.18) → Status (NOT FIRED / PARTIAL / FIRED, with date + primary-source evidence) → Last checked (date + session). **Scope:** thesis-level risks only, curated — not a mirror of every page's Open questions. Distinct from [[forward-edge-tracker]] (which holds *consensus-divergence* views): the register also holds **consensus-aligned risks** (where vault and market could be wrong together — e.g., an AI-capex cycle turn). Tier discipline (Section 2.2): Tier 3/4 may *name* a risk mechanism; only primary sources *fire* a tripwire. Honest-verdict (Section 2.1): a fired tripwire is stated plainly at the top of the page, not buried.

### 3.21 Demand-side / application-layer placement

The AI-datacenter thesis has two sides: a **supply side** (Frameworks 2 + 5–9 — the chokepoint owners the vault primarily tracks) and a **demand side** — the names that **fund, deploy, or consume** the buildout. Demand-side names own no supply-chain chokepoint, so they carry **`layer: outside` + all five `*_tier: outside`**. `layer: outside` is a **documented value** meaning "not an AI-datacenter supply-chain value-capture participant" — it is not a gap in the 1–6 range. Demand-side names are **theme-anchored, not framework-placed**, to the relevant demand-side page ([[hyperscaler-capex]] / [[AI-demand-durability]] / [[software-AI-moat-durability]] / [[neocloud-moat-durability]]); the analytical home is `frameworks.md` Framework 10.1.

**Three sub-roles** (analytical, not frontmatter fields): **capex-payer** (hyperscalers — MSFT/GOOGL/AMZN/META/ORCL; the *source* of the Framework 10 CAPEX flow), **infra-operator** (neocloud / host landlords — CRWV/NBIS/CORZ; buy GPUs, deploy + rent compute), **app-layer consumer** (software — NOW/PLTR/DDOG; monetize/consume compute, the billed-unit test at [[software-AI-moat-durability]]). Demand-side **counterpoints** (AAPL / QCOM — capex-light or edge) are the honest-verdict variant, included to test the thesis rather than confirm it.

**Inclusion scope (Vic-set, looser bound).** A name earns a demand-side page when it is a **material AI-datacenter demand-side participant** — it funds, deploys, or consumes AI compute at thesis-relevant scale — whether as a demand signal, a research-goal test, or an honest-verdict counterpoint. The boundary is the **AI-datacenter thesis itself**: the page must illuminate the buildout's funding, deployment, or monetization; it does not qualify merely by being a large software / mega-cap name. Honest-verdict (Section 2.1) holds — weak supply-chain fit is the default, and the page is verdict-oriented around the demand-side role, not supply-chain centrality (describe-don't-recommend; no P&L / position sizing).

**`layer: outside` spans two documented rationales:** (1) **demand-side** (this rule — AI-datacenter names that fund/deploy/consume); (2) **cross-domain theme-anchor** (humanoid / defense names with no AI-datacenter role and no domain tier — e.g. the humanoid value-chain cohort, theme-anchored to [[humanoid-robot-value-chain]]). Both mean "outside the AI-datacenter Framework-2 supply-chain layers." *4-instance codification roster (MSFT S112 → NOW S113 → PLTR S114 → DDOG S188) + evidence: conventions ledger A.20.*

## 4. Source ingest

### 4.1 Multi-source ingests

When ingesting multiple sources for the same company in a single session, keep separate financial tables per reporting period rather than blending — cross-period deltas are analytically valuable and only visible when periods stay distinct. For three-source ingests (10-K + 10-Q + earnings call covering two fiscal periods): read sequentially older filing → current-period filing → current-period call; Source audit notes carry one per-source entry, ordered by recency and tier.

**Chokepoint refresh protocol — 1-stop vs 2-stop.** Chokepoint page refreshes default to **1-stop** (single Stop; plan + execute combined) when scope is contained: single-source-driven update (one new canonical ingest OR one Tier 3 analytical product propagating) and NONE of the escalation triggers below. **Escalate to 2-stop when ANY of:** (a) substantive multi-source scope; (b) a NEW chokepoint structural type emerging; (c) substantive canonical-participant scope expansion (a NEW canonical added to the chokepoint); (d) a new primary-source ingest at chokepoint scope or new chokepoint creation; (e) major analytical product addition. **Scope-creep prevention:** 1-stop limited to substantive-update scope per source; hard cap ~3-5 files; new subsections within Section 3.8 brevity (~12-25 lines). *Precedent: See A.18.*

### 4.2 Foreign-issuer ingests

Foreign private issuers file 20-F annually and 6-K interim disclosures rather than 10-K + 10-Q. **Source-set composition:** US-domiciled = 10-K + 10-Q + earnings call (most recent); foreign private issuer = 20-F + 6-K (most recent earnings disclosure) + earnings call; MJDS Canadian = 40-F + 6-K (cover + Ex 99.1 press release + Ex 99.2 financials + Ex 99.3 MD&A) + earnings call = the 6-file canonical pattern.

**Variability checks at Phase 0.** 6-K filings span earnings, press releases, governance, material events — verify the selected 6-K is the earnings disclosure (the MJDS 6-K cover is wrapper-only; substantive content in the three exhibits). Foreign-issuer fiscal calendars may differ from US standard (Dec 31 most foreign incl. TSM/TSEM; Mar 31 many Japanese; late-Apr/late-May some Israeli/Indian) — verify period-end dates per A6 (h). 20-F filings are typically USD with supplementary local-currency tables (clarify at Phase 0); apply frontmatter `foreign_issuer: true` per Section 3.2; `scripts/fetch_filings.py` may need extension for 20-F + 6-K + 40-F forms. *See A.8 (TSM precedent + candidate list; CCJ = the MJDS pattern).*

### 4.3 When sources contradict existing pages

Don't silently overwrite. Add contradiction note showing wiki's prior claim, what new source says, and — for factual disagreements — apply tier hierarchy. For interpretive disagreements, present both positions and flag for human to resolve.

### 4.4 Kickoff hypothesis falsification

Kickoff prompts may include hypotheses about company capability, customer relationships, or strategic direction that source evidence falsifies. Document falsification explicitly on the company page as investigation finding rather than silently omitting. Belongs in Thesis role or Open questions depending on significance: (1) state what was hypothesized; (2) state what sources did/did not find; (3) preserve epistemic humility (absence of evidence ≠ definitive proof of absence); (4) flag for `frameworks.md`/`_thesis.md` review if hypothesis may have propagated into configuration.

### 4.5 Kickoff drafting vault-content verification (A6)

When drafting an ingest kickoff prompt that pre-commits any vault-content reference, verify references against current vault state at Phase 0 BEFORE proceeding to source ingest planning.

**Pattern types (8 accumulated empirically; see A.9 for per-instance evidence):**

- (a) **Framework placement** — verify Layer (F2) + per-domain `*_tier` (F5–F9) + F2.6 control-point + F4 structural/cyclical + F10 CAPEX flow + F11 theme placements per frameworks v10.1; Outside placement per Section 3.10.
- (b) **Vault page existence** — verify referenced pages exist; plain-text for non-existent, `[[Brackets]]` only for existing.
- (c) **Section numbering** — verify section numbers in target pages before drafting cross-references.
- (d) **Frontmatter convention** — verify proposed fields against current vault convention; no new fields without explicit codification.
- (e) **Wikilink integrity** — verify all `[[Brackets]]` point to existing pages; casing must match target filenames.
- (f) **Session-positioning** — verify which prior session ingested what before referencing prior-ingest baselines.
- (g) **Factual error scope:** (g) Tier 3 source figure variance — verify Tier 3 quantitative claims against primary at Phase 0. (g') Kickoff drafting factual variance — verify kickoff "Codified background" claims against primary at Phase 0; document material falsifications per Section 4.4.
- (h) **Source filename verification** — verify period-end dates in filing headers match source filenames; verify ticker-content match (S59 FN-FNF mislabel precedent).

**Discipline boundary.** Section 4.6 marketing-tier non-corroboration at primary (Tier 3/4 marketing-source placed under "Structural context to verify at primary" in kickoff) is an EXPECTED Section 4.6 outcome, NOT a Section 4.5 (g') factual variance — (g') increments ONLY when Tier 3/4 content was placed under "Codified background" AND material variance surfaces at Phase 0. **Application:** every Phase 0 verification runs all applicable pattern-type checks ((b)-(h) universal; (a) only when the kickoff pre-commits framework placement); gaps documented per Section 4.4. Applies to kickoff drafting (chat-side) + Stop 1 Phase 0 verification (vault agent). *Per-instance evidence + cumulative counts in A.9 + MEMORY.md.*

### 4.6 Kickoff drafting source discipline

When drafting an ingest kickoff, distinguish four source tiers and place each in the correct kickoff scope:

- **Primary-source-verified (Tier 1+2):** 10-K / 10-Q / earnings call / 8-K / 6-K / 40-F / 20-F. Eligible for "Codified background from existing vault context."
- **Tier 3 source claims:** Vic-curated analytical research (HALEU report; energy bottleneck report; primer; chokepoint research framework). Eligible for "Codified background" with explicit Tier 3 attribution.
- **Marketing/IR + third-party summary claims:** Web search; company website; investor presentations; press releases; Cervicorn / GuruFocus / Seeking Alpha / news aggregators. NOT eligible. Place under "Structural context per Tier 3/4 sources to verify at primary."

**Application discipline + empirical ROI.** Treat the boundary as binding: when uncertain whether a claim is primary-source-verified, default to "Structural context per Tier 3/4 sources to verify at primary." Stop 1 Phase 0 verification (Section 4.5 A6 (g')) tests primary-source content against the kickoff's "Codified background"; falsifications documented per Section 4.4. The four-tier discipline produced a sustained zero-falsification streak. Marketing-tier non-corroboration at primary is EXPECTED per the Section 4.5 discipline boundary, NOT a (g') variance. *Streak evidence: See A.12; current count in MEMORY.md; frameworks.md Section 11.11 for the cross-chokepoint theme framework.*

### 4.7 Refresh ingest log (`raw/notes/refresh_log.md`)

**Mandatory close-out step for every refresh ingest.** When a session re-ingests an EXISTING vault company page with a new primary source set (a "refresh ingest" per Section 4.1 / 4.2 — distinct from first-canonical creation, chokepoint/theme/relationship creation, codification, or in-place Tier-3 substrate refreshes), append a dated entry to `raw/notes/refresh_log.md` at close-out, alongside `index.md` + `log.md` + MEMORY.md and before the final verification pass. It is a cumulative, reverse-chronological record of how each company's thesis evolves quarter over quarter, complementing `log.md` by isolating refresh-specific analytical deltas. **Per-entry template** (newest at top; canonical format in the file header): `## S### — TICKER (Company) — YYYY-MM-DD — <period refreshed>`, then **Sources** / **Prior baseline** / **Headline** / **Key changes & new developments** / **Placement** (change or "unchanged" + why) / **Cross-vault propagation** / **Forward watch** / **Key insight**. Section 3.8 brevity applies. Not in `index.md`; updates do not count for accounting.

## 5. Operational guidance

### 5.1 Early phase

For first few ingests, propose before writing: state which pages will be created/updated and wait for confirmation. Once human confirms things feel right, drop the confirmation step and proceed autonomously.

### 5.2 What to avoid

Avoid: summarizing filings comprehensively (most of a 10-Q is boilerplate; extract material + strategic only); hallucinating relationships (connection not evidenced in source ≠ wiki content); extensive quotation (paraphrase in wiki voice and cite); reorganizing structure unilaterally (propose CLAUDE.md or folder layout changes; don't drift); editing `_thesis.md`.

### 5.3 Evolution

This file is expected to change. When a convention isn't working, flag it at end of session with a concrete proposal; the human decides and commits. **Forward-only growth discipline:** this always-loaded manual holds the **rules and current state**; the **empirical evidence, per-instance precedent rosters, canonical-example detail, and codification history** live in `raw/notes/conventions-ledger.md` (the codification analog of `refresh_log.md`). When a convention is codified, add the **rule** here and append its **supporting evidence / per-instance roster** to the ledger — never accumulate instance enumerations or precedent rosters in this file. Instance counts have a single live home (MEMORY.md per Section 3.8); the ledger holds the evidence behind them. The intent: this file does not grow monotonically. Existing rule text is not retroactively trimmed without explicit Vic authorization (the v10.1/v10.2 compressions were Vic-authorized).

**Third-instance codification bar (NEW at v10.2, 2026-07-02).** A recurring pattern becomes a CLAUDE.md rule at its **third observed instance** — first and second instances are recorded as watch items in the conventions ledger (count in MEMORY.md), not codified here. Vic may override for structurally obvious rules. New rules are written in plain language; established terms of art keep their names.

## 6. Appendix — empirical evidence + per-instance precedents

Moved out of the operating manual to keep it lean (Session 129; v9.6). The empirical evidence base, canonical examples, and per-instance precedent rosters (formerly A.1–A.12) now live in **`raw/notes/conventions-ledger.md`**, which preserves the same A.x labels — so an in-text "*See A.10*" reference resolves to A.10 in the ledger. Live monitoring counts remain in MEMORY.md per Section 3.8.
