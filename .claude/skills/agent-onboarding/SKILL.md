---
name: agent-onboarding
description: Load full context for the stocks-wiki vault. Invoke at the start of any new session before other work — reads ALL THREE thesis anchors (AI-datacenter + Defense & Drones + Humanoid Robots), operational conventions (CLAUDE.md), all three analytical frameworks, current state (MEMORY/log/index), and every wiki page catalogued in index.md (currently ~80 companies, 13 chokepoints, ~17 themes, 4 trackers, 1 relationship across wiki/). Skip only if context is already loaded in the current conversation.
---

# Agent onboarding — stocks-wiki

This skill orients a new Claude Code agent on the stocks-wiki vault by directing a complete read of the canonical files. It is a navigation aid, not a content cache. Canonical content lives in the files listed below; this skill specifies read order and meta-principles to apply.

The vault is a personal research vault spanning **three thesis domains**: (1) **AI datacenter supply chain & chokepoint analysis** — the founding/primary thesis (multi-domain scope: compute, photonics, memory, energy, power, equipment, materials, and more — per `_thesis.md` rework + `frameworks.md` v10.1); (2) **Defense & Drones (unmanned systems)** — added Session 123 (drones-first scope — per `_thesis-defense-drones.md` + `frameworks-defense-drones.md` v1.0); and (3) **Humanoid Robots (embodied-AI value chain & chokepoints)** — added Session 136 (humanoid-first, broadening to "physical AI" later — per `_thesis-humanoid-robot.md` + `frameworks-humanoid-robot.md`, **both v0.2 LIVING — the "keep-growing-and-optimizing" version, reworked S145; operative, still evolving**). Each domain has its own human-owned `_thesis` + `frameworks` anchor pair; all three share the same methodology, source hierarchy, and disciplines. The agent maintains the wiki; the human curates sources and asks questions. Read everything below before responding to any task on this project. *(`CLAUDE.md` is currently **v9.9** — Section 1.2 codifies all three domains [bumped at v9.7], and v9.9 added the page-lifecycle + latest-alpha-block conventions described below; trust the file header for the live version.)*

## Read order

Follow this sequence. Each file is canonical for its scope; do not summarize unless asked.

### 1. Anchors and conventions

**The vault holds three thesis domains**, each with its own human-owned `_thesis` + `frameworks` anchor pair. **Read all three pairs** — a company can sit in more than one supply chain (a "dual-/tri-thesis page"; e.g. MP is *triple-thesis* [AI/materials + defense + humanoid], HARMONIC is *tri-thesis* [AI-datacenter equipment + defense + humanoid], and AMD / NVDA / PLTR are dual-thesis). The filenames are deliberately asymmetric: the AI-datacenter anchor is the *unmarked default* (`_thesis.md` / `frameworks.md`) because it is the founding/primary thesis; the Defense and Humanoid anchors are *marked expansions* (`-defense-drones` and `-humanoid-robot` suffixes).

**AI-datacenter domain (the founding/primary thesis):**
- **`wiki/_thesis.md`** — the AI-datacenter anchor: what the project is trying to figure out, current seed positions and conviction levels, disconfirming signals, dual-anchor portfolio reframing (compute + power infrastructure). **Never edited by the LLM by default.** Per CLAUDE.md Section 1.1, a one-time Vic-authorized rework exception was applied during Sessions 32-36 arc (collaborative chat drafting); default ownership convention has resumed for all subsequent sessions. Future similar reworks require explicit Vic-authorized declaration; do not assume permission.
- **`raw/notes/frameworks.md`** — the AI-datacenter analytical scaffolding (currently v10.1; see the file header for the live version). Frameworks 1-11 multi-domain (supply chain flow with 5 sub-domain diagrams; six value-capture layers; control-point analysis; structural-vs-cyclical per-domain; per-domain tier frameworks for photonics / memory / energy-power / equipment / materials; CAPEX flow allocation; cross-chokepoint themes). Human-maintained — propose edits at codification sessions; never silently revise. Same one-time-rework ownership exception as `_thesis.md` per CLAUDE.md Section 1.1.

**Defense & Drones domain (second thesis, added Session 123; drones-first scope):**
- **`wiki/_thesis-defense-drones.md`** — the Defense & Drones anchor: the chokepoints-over-platforms thesis for unmanned systems (airframes commoditizing toward ~$2,000; value sits upstream in magnets / secure chips / seekers / autonomy / compliant supply chains); the enacted-vs-requested budget discipline (only FY2025 reconciliation is law; FY2027 DAWG is a request); the chokepoint quality gradient (geology/physics > policy — note the Blue UAS exemption expiry Jan 1 2027); tiered company universe. **Same ownership as the AI anchor** — human-owned; never edited by the LLM by default (created Session 123 via the same Vic-authorized collaborative-drafting exception per CLAUDE.md Section 1.1).
- **`raw/notes/frameworks-defense-drones.md`** — the Defense & Drones analytical scaffolding (v1.0). Frameworks D1-D7: value-chain flow; value-capture tiers → the `defense_tier` field (1 prime / 2 mid-cap pure-play / 3 speculative micro-cap / 4 supply-chain enabler — **the number is NOT a conviction rank**; conviction tracks the D5 quality gradient); demand map / programs of record; structural-vs-cyclical; chokepoint framework + quality gradient; the booked-contract-vs-narrative / financial-quality "LASE discipline" screen (D6); cross-thesis overlap. Human-maintained; same ownership discipline as `frameworks.md`.

**Humanoid Robots domain (third thesis, added Session 136; humanoid-first scope; both anchors v0.2 LIVING — "keep-growing-and-optimizing"):**
- **`wiki/_thesis-humanoid-robot.md`** — the Humanoid Robots anchor: value concentrates at structural chokepoints (rare-earth magnets, harmonic/strain-wave reducers, planetary roller screws, six-axis force/torque sensors, the AI "brain") and **not** at the commoditizing robot-maker layer; the chokepoint-quality gradient (physics/geology > precision-grinding/metallurgy > integration); the early-innings discipline (the *direction* of automation is credible, the *magnitude and timing* are speculative — lead every read with "early-innings optionality"); and the **investor-access lens** (Vic can reach US, foreign-listed, and China A-share/HK names — so rank on chokepoint-quality + business health, not the listing flag). **v0.2 LIVING** — the "keep-growing-and-optimizing" version (promoted from v0.1 DRAFT at S145 via a Vic-authorized rework: investor-access-lens reframe + ingest-progress refresh through S145); operative but deliberately not locked, and **human-owned** (never edited by the LLM by default; propose only at future Vic-authorized passes). The investor-access-lens reconciliation is now **applied in the anchor** — it no longer diverges from the `humanoid-robot-value-chain` theme page. *(Sole remaining human-owned scope item: bump CLAUDE.md Section 1.2 "two → three domains".)*
- **`raw/notes/frameworks-humanoid-robot.md`** — the Humanoid Robots scaffolding (v0.1). Value-chain position, durability scoring, the chokepoint-quality gradient. **No `humanoid_tier` frontmatter field is codified (held under YAGNI):** humanoid names land `outside` the existing per-domain frameworks + **theme-anchored** to `humanoid-robot-value-chain` (the [[INOD]]/[[OUST]] precedent), OR carry another domain's tier where they are cross-thesis (e.g. HARMONIC = `equipment_tier 4` + `defense_tier 4`; TUOPU = `energy_power_tier 4`; NOVT/VPG = `equipment_tier 4`). Human-maintained; same ownership discipline as the other frameworks files.

**Shared across all three domains:**
- **`CLAUDE.md`** — operational conventions (currently **v9.9**; see the file header for the live version). Source hierarchy, citation discipline, page conventions (multi-domain frontmatter incl. `defense_tier`; Outside Framework placement; A1 three-mode framing; framing-gap conventions; non-calendar-fiscal-year + foreign-issuer protocols), four disciplines, scope rules — **plus the v9.9 page-lifecycle conventions (Section 3.19: rolling financial snapshot [latest annual + 2 quarters full], open-questions lifecycle, third-refresh compaction), the Section 3.8 change-log hard cap + telemetry-relocation rule (process counts live ONLY in log.md/conventions-ledger, never on company pages), and the Section 3.17 latest-alpha digest block.** Applies to all three thesis domains.

### 2. Current state

- **`~/.claude/projects/-Users-victor-he-Downloads-Code-stocks-wiki/memory/MEMORY.md`** — auto-loaded at session start. Most recent vault state, monitoring counts, backlog items, process learnings. Treat as time-stamped snapshot — verify against current files where load-bearing.
- **`log.md`** — append-only session-by-session execution log. Tail of file is most recent session's findings and Phase 4 reflection. Backlog and monitoring counts at session-close are canonical here.
- **`index.md`** — **the authoritative catalog of every wiki page** with frontmatter (ticker, layer, photonics_tier, plus optional `memory_tier` / `energy_power_tier` / `equipment_tier` / `materials_tier` / **`defense_tier`** per multi-domain expansion per CLAUDE.md Section 3.2; last_updated). **There is no `humanoid_tier` column** — the Humanoid domain is theme-anchored, so humanoid exposure shows up as `outside` + a `humanoid-robot-value-chain` theme membership, or via another domain's tier (see Section 1). This is the list Section 3 reads against — trust it over any hard-coded page list.
- **`raw/notes/refresh_log.md`** — reverse-chronological per-company refresh-ingest deltas (what changed since each company's prior baseline; codified Section 4.7). A reference read (not a mandatory full read) for quarter-over-quarter thesis-evolution context; most useful when the session's task is a refresh ingest.
- **`raw/notes/conventions-ledger.md`** — the empirical evidence, per-instance precedent rosters, and codification history behind CLAUDE.md's rules (the codification analog of `refresh_log.md`; moved out of CLAUDE.md's Appendix at v9.6 / Session 129 to keep the rulebook lean — the "forward-only growth discipline," CLAUDE.md Section 5.3). **CLAUDE.md's in-text "*See A.x*" references resolve to the A.x entries here.** A reference read (not a mandatory full read) — pull it up when a task needs the *why / precedent* behind a convention; new precedent evidence is appended here going forward, not back into CLAUDE.md.

### 3. Substantive content (full read = full context; this is the default)

**Read every page in each wiki subdirectory.** Do not skip — cross-session findings, reciprocal patterns, and chokepoint substantiation only become visible from cross-page reading. **`index.md` is the authoritative catalog of what exists; read against it. Do NOT trust any hard-coded page list (it rots) — the directory enumeration below is stable, but the per-page set lives in `index.md`.** Current scope (verify against `index.md`): **~80 companies, 13 chokepoints, ~17 themes, 4 trackers, 1 relationship.** (The three `wiki/_thesis*.md` thesis anchors + the three `raw/notes/frameworks*.md` files are read in Section 1, not counted here — they are scaffolding, not catalogued wiki pages.)

- **`wiki/companies/*.md`** — company pages. Each has frontmatter, Thesis role, Financial snapshot, per-source content sections, Source audit notes, Change log.
- **`wiki/chokepoints/*.md`** — chokepoint pages (provisional or canonical per CLAUDE.md Section 3.15).
- **`wiki/themes/*.md`** — theme pages (dynamics / mechanism / absence types per CLAUDE.md Section 3.12).
- **`wiki/trackers/*.md`** — tracker pages (CLAUDE.md Section 3.20; added v10.0): cross-vault **status-bearing** pages updated by propagation (`forward-edge-tracker` per Section 3.18, `hyperscaler-capex`, `china-exposure`, `what-could-go-wrong` — the vault-level risk register). **Read these — they carry the live signal/falsifier state**, and their freshness obligation means any session touching a tracked signal updates them.
- **`wiki/relationships/*.md`** — relationship pages (currently `nvidia-supply-chain-commitments`): bilateral commercial-commitment + supply-chain-dependency + A1-mode analysis. **Read these — they are canonical cross-vault content.**

*(The former `wiki/layers/` page type was retired unused at CLAUDE.md v10.0 — the company-page `layer` frontmatter field is unchanged.)*

**Scale + how to load it.** A full read is now ~31,000+ lines (~250–290k tokens) and grows every session. A **1M-context agent (this project's default) holds the full read comfortably** — load it efficiently with batched/parallel reads, and prefer the full read because rich cross-page context is the point. A **context-limited agent** should: read the orientation layer (Sections 1–2) fully, use `index.md` + `MEMORY.md` as the map, read the pages relevant to the session's task, optionally delegate breadth to domain-cluster sub-agents — and must **explicitly state it is operating with partial context** so the human knows. Per-page line counts are non-load-bearing; verify against canonical files when relevant.

### 4. Verify full coverage

After reading, confirm coverage against `index.md`: the number of pages read per directory should match the catalog. If any catalogued page was skipped, read it before proceeding — or, if operating with partial context by necessity, name the specific pages not yet read. This makes "full context" verified rather than assumed, and guards against silent partial onboarding as the vault grows.

## Meta-principles to apply

These are not duplications of `CLAUDE.md` — they are cross-cutting principles that aid efficient operation across sessions.

**Cross-session knowledge transfer.** Wiki pages are canonical for cross-session knowledge; raw sources in `raw/filings/`, `raw/transcripts/`, and `raw/notes/` are canonical for the originating ingest only. After a primary source has been ingested and its analytical product landed on a wiki page, future sessions reference the wiki page rather than re-reading the raw source. The raw source remains in `raw/` as audit trail; analytical content lives on the wiki page. This is what prevents context exhaustion across sessions.

**Vault-conflict reconciliation.** When Tier 3 source claims conflict with vault primary-source findings, vault findings win. Reconciliation is via direct reading of vault content covering the same claim, or via spot-check of the cited footnote URL. Frame conflicting claims with appropriate attribution (industry-reporting attribution, derivative-chain disclosure, etc.); preserve vault primary-source silence where it exists. Reference example: TSMC COUPE production claim (Session 19).

**Forward-wikilink discipline.** Use `[[Brackets]]` only for pages that exist. Companies referenced by name without brackets when the company has no wiki page. Vault is wikilink-clean; preserve that status.

**Honest-verdict discipline.** When a company's thesis fit is weak, the page states the weak fit plainly. Weak-fit pages may be shorter and more verdict-like than strong-fit pages. Inclusion may be for trajectory or counterpoint rather than thesis centrality. See `_thesis.md` Four disciplines.

**Tier 3 attribution mechanics.** Tier 3 synthesis sources (Vic-authored research in `raw/notes/`) have distinct citation discipline: structural framework paraphrased in wiki voice (Vic owns the canonical map); company placements cross-referenced to underlying primary-source evidence in vault company pages; external-reporting claims footnote-attributed where verifiable; `citeturn` references treated as Tier 3 attribution without primary-source verification.

**Kickoff templates (v9.9).** Session kickoff prompts for US-listed ingests are drafted from the standing templates in `prompts/templates/` (refresh / single first-canonical / paired refresh) — conventions are referenced, not restated, so a filled kickoff is ~60–120 lines carrying only the session's deltas (sources, hypotheses, questions, scope). The legacy 400–600-line kickoffs in `prompts/samples/` are preserved as pre-template-era history, not the pattern to copy.

**Stop protocol selection.** Two-stop is the default (plan → human approval → execute). Three-stop applies when scope warrants intermediate plan review (codification with 7+ items or 5+ file cascade). Single-stop for audit execution and discovery audits. See `raw/references/agent_onboarding.md` for full session-type taxonomy and protocol-calibration triggers.

**Foreign-filer ingest sub-type (now established — mostly via the Humanoid domain).** The vault now includes **non-SEC foreign filers** ingested filings-only: the Chinese A/H-share cohort ([[SANHUA]] / [[TUOPU]] / [[SHUANGHUAN]] / [[ZHONGDA]] — PRC-GAAP/CAS, RMB) and the first Japanese / EDINET filer ([[HARMONIC]] — JGAAP, ¥; 決算短信 *Tanshin* + 半期/有価証券報告書). These carry **readable-identifier filenames** (e.g. `HARMONIC`, not the numeric ticker 6324), are **Vic-staged** (NOT fetchable via `scripts/fetch_filings.py`), and are typically **filings-only — no earnings-call transcript**, so the Tier 1/Tier 2 framing-gap (Section 3.4) and CEO-combativeness (Section 3.7) conventions are **N/A** for those ingests per the Section 2.2 source-availability rule (HARMONIC is the exception — it ships a real transcript). Section 2.11 (non-calendar fiscal year) applies to the March-31 filers (HARMONIC, alongside ENS/MOD/ARM). The foreign-issuer source-set table (CLAUDE.md Section 4.2) has no A-share or Japan row yet — a **live codification candidate** (5 instances accumulated).

## Configuration file edit discipline

- **`_thesis.md` + `_thesis-defense-drones.md` + `_thesis-humanoid-robot.md`** (the three thesis anchors) — never edited by the LLM by default. Vic-side action only. One-time Vic-authorized exceptions applied per CLAUDE.md Section 1.1 (AI anchor reworked Sessions 32-36; Defense anchor created Session 123; Humanoid anchor created Session 136 — all via the same collaborative-drafting exception); default ownership convention resumes after each. **The Humanoid anchors are v0.2 LIVING ("keep-growing-and-optimizing," reworked S145) — operative but the youngest/least-settled of the three; propose, never silently edit (same human-ownership rule).**
- **`frameworks.md` (v10.1) + `frameworks-defense-drones.md` (v1.0) + `frameworks-humanoid-robot.md` (v0.1)** (the three frameworks files) — human-maintained. LLM proposes edits at codification sessions; edits require explicit approval. No silent revisions. Same one-time-exception ownership discipline as the thesis anchors.
- **`CLAUDE.md`** — operational conventions (currently v9.9). LLM proposes edits at codification sessions; edits require explicit approval.
- **Wiki pages** — LLM-maintained. Standard editing per CLAUDE.md conventions (Source audit notes, Change log, frontmatter `last_updated`, citations).

## Active monitoring conventions

These conventions track patterns that warrant codification once a third instance accumulates. Current counts live in `MEMORY.md` (snapshot) and `log.md` tail (latest session entry). Verify counts against canonical files before relying on them.

- Tier 1/Tier 2 framing gap (B2 unified)
- Cross-venue gap (structurally distinct from B2)
- CEO combativeness
- Reciprocal non-naming pattern — note: under reconciliation since the MRVL↔NVDA break (S102/S110; NVDA-platform-integration "Mode 4" is the documentation home); flagged as an open codification item.

For the live accumulation state of these patterns (counts, threshold crossings, MEMORY drift), use the **`learning-monitor`** skill rather than re-deriving by hand.

## After onboarding

Once the read sequence is complete, the agent has full vault context. Confirm onboarding completion to the user with a brief summary that surfaces enough to **continue working immediately**:

- **Current vault state** — scope (companies / chokepoints / themes / trackers / relationships) + most recent session (from the `MEMORY.md` top entry + `log.md` tail).
- **Open Vic-side decision queue** — the "NEW Vic-side decision queue" / codification-candidate items in the latest `MEMORY.md` vault-state entry (these are the threads awaiting Vic's direction).
- **Staging queue** — check `raw/filings/newly_fetched/`; any files there are sources Vic has dropped that are pending ingest (the typical next unit of work).
- **Monitoring conventions** at current counts (defer to `MEMORY.md` / `learning-monitor`).

**Sibling vault skills** (use rather than re-deriving by hand): **`check-recent-earnings`** — what reported recently / what's due for refresh-ingest; **`learning-monitor`** — pattern accumulation + codification readiness + MEMORY drift; **`connection-finder`** — candidate cross-page connections / new chokepoint/theme/relationship candidates.

If the user provides a session kickoff with its own Phase 0 context-loading instructions, those instructions are session-specific and may overlap with this skill's read order — that overlap is acceptable; do not skip kickoff instructions because they were already covered here.

## Maintenance

This skill is a navigation aid. It is updated when the vault's directory structure or canonical-file ownership changes, not on every session. **Page-count and per-page enumeration drift is eliminated by design** — Section 3 points at `index.md` rather than caching page lists, so the catalog stays current without skill edits. The **load-bearing items to keep current** are: the **directory list** (Read order Section 3), the **meta-principles**, the **edit discipline**, the **sibling-skill cross-references**, and the **version references** (CLAUDE.md / frameworks.md / frameworks-defense-drones.md / frameworks-humanoid-robot.md) + the **three-domain anchor set** (all three `_thesis` + all three `frameworks` pairs). Drift on those requires correction; everything else self-updates via the canonical-source pointers.

Update this skill at codification sessions if the vault structure, canonical-file ownership, or sibling tooling changes.
