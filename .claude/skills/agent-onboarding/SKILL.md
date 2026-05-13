---
name: agent-onboarding
description: Load full context for the stocks-wiki vault. Invoke at the start of any new session before any other work — reads the anchor document, operational conventions, analytical scaffolding, current state, and all wiki content (24 company pages, 7 chokepoints, 8 themes). Use when starting fresh on this project; do not invoke if context is already loaded in the current conversation.
---

# Agent onboarding — stocks-wiki

This skill orients a new Claude Code agent on the stocks-wiki vault by directing a complete read of the canonical files. It is a navigation aid, not a content cache. Canonical content lives in the files listed below; this skill specifies read order and meta-principles to apply.

The vault is a personal research vault for AI datacenter supply chain and chokepoint analysis (multi-domain scope: compute, photonics, memory, energy, power, equipment, materials, and more — per `_thesis.md` rework + `frameworks.md` v10.1 + `CLAUDE.md` v9 codification). The agent maintains the wiki; the human curates sources and asks questions. Read everything below before responding to any task on this project.

## Read order

Follow this sequence. Each file is canonical for its scope; do not summarize unless asked.

### 1. Anchor and conventions

- **`wiki/_thesis.md`** — what the project is trying to figure out, current seed positions and conviction levels, disconfirming signals, dual-anchor portfolio reframing (compute + power infrastructure). **Never edited by the LLM by default.** Per CLAUDE.md v9 Section 1.1, a one-time Vic-authorized rework exception was applied during Sessions 32-36 arc (collaborative chat drafting); default ownership convention has resumed for all subsequent sessions. Future similar reworks require explicit Vic-authorized declaration; do not assume permission.
- **`CLAUDE.md`** — operational conventions (currently v9). Source hierarchy, citation discipline, page conventions (multi-domain frontmatter; Outside Framework placement generalization; A1 three-mode framing; A4 / A4-bis framing gap conventions; A6 v9 8-pattern verification), four disciplines, scope rules.
- **`raw/notes/frameworks.md`** — analytical scaffolding (currently v10.1). Frameworks 1-11 multi-domain (supply chain flow with 5 sub-domain diagrams; six value-capture layers; control-point analysis; structural-vs-cyclical per-domain; per-domain tier frameworks for photonics / memory / energy-power / equipment / materials; CAPEX flow allocation; cross-chokepoint themes). Human-maintained — propose edits at codification sessions; never silently revise. Same one-time-rework ownership exception as `_thesis.md` per CLAUDE.md v9 Section 1.1.

### 2. Current state

- **`~/.claude/projects/-Users-victor-he-Downloads-Code-stocks-wiki/memory/MEMORY.md`** — auto-loaded at session start. Most recent vault state, monitoring counts, backlog items, process learnings. Treat as time-stamped snapshot — verify against current files where load-bearing.
- **`log.md`** — append-only session-by-session execution log. Tail of file is most recent session's findings and Phase 4 reflection. Backlog and monitoring counts at session-close are canonical here.
- **`index.md`** — catalog of all wiki pages with frontmatter (ticker, layer, photonics_tier, plus optional `memory_tier` / `energy_power_tier` / `equipment_tier` / `materials_tier` per multi-domain expansion per CLAUDE.md v9 Section 3.2; last_updated). Use as wiki navigation map.

### 3. Substantive content (full read required for full context)

Read all pages in each directory. Do not skip; cross-session findings, reciprocal patterns, and chokepoint substantiation only become visible from cross-page reading.

- **`wiki/companies/*.md`** — 24 company pages: AAOI, AEHR, ALAB, ANET, AVGO, AXTI, COHR, COHU, CRDO, CSCO, ETN, FLEX, FN, GEV, GLW, LITE, MRVL, NVDA, ONTO, PLAB, TSM, VECO, VIAV, VRT. Each has frontmatter, Thesis role, Financial snapshot, per-source content sections, Source audit notes, Change log.
- **`wiki/chokepoints/*.md`** — 7 chokepoint pages: advanced-optical-packaging, cpo-integration, datacenter-laser-supply, InP-supply, optical-dsp-phy-supply, TSMC-CoWoS, wafer-level-siph-test.
- **`wiki/themes/*.md`** — 8 theme pages: AI-demand-durability, chokepoint-investability-priorities, CPO-platform-battle, datacenter-photonics-supply-chain, foundry-competition, hyperscaler-custom-ASIC, NVDA-platform-integration, overseas-fab-expansion.

Total substantive content has grown materially since Session 19 baseline (~6,000-7,000 lines / 24 wiki pages); current vault is 39 wiki pages post-Session-37. Full read consumes meaningful context budget; that is the cost of full context. Specific line counts and per-page metrics are non-load-bearing — verify against canonical files when relevant.

## Meta-principles to apply

These are not duplications of `CLAUDE.md` — they are cross-cutting principles that aid efficient operation across sessions.

**Cross-session knowledge transfer.** Wiki pages are canonical for cross-session knowledge; raw sources in `raw/filings/`, `raw/transcripts/`, and `raw/notes/` are canonical for the originating ingest only. After a primary source has been ingested and its analytical product landed on a wiki page, future sessions reference the wiki page rather than re-reading the raw source. The raw source remains in `raw/` as audit trail; analytical content lives on the wiki page. This is what prevents context exhaustion across sessions.

**Vault-conflict reconciliation.** When Tier 3 source claims conflict with vault primary-source findings, vault findings win. Reconciliation is via direct reading of vault content covering the same claim, or via spot-check of the cited footnote URL. Frame conflicting claims with appropriate attribution (industry-reporting attribution, derivative-chain disclosure, etc.); preserve vault primary-source silence where it exists. Reference example: TSMC COUPE production claim (Session 19).

**Forward-wikilink discipline.** Use `[[Brackets]]` only for pages that exist. Companies referenced by name without brackets when the company has no wiki page. Vault is wikilink-clean; preserve that status.

**Honest-verdict discipline.** When a company's thesis fit is weak, the page states the weak fit plainly. Weak-fit pages may be shorter and more verdict-like than strong-fit pages. Inclusion may be for trajectory or counterpoint rather than thesis centrality. See `_thesis.md` Four disciplines.

**Tier 3 attribution mechanics.** Tier 3 synthesis sources (Vic-authored research in `raw/notes/`) have distinct citation discipline: structural framework paraphrased in wiki voice (Vic owns the canonical map); company placements cross-referenced to underlying primary-source evidence in vault company pages; external-reporting claims footnote-attributed where verifiable; `citeturn` references treated as Tier 3 attribution without primary-source verification.

**Stop protocol selection.** Two-stop is the default (plan → human approval → execute). Three-stop applies when scope warrants intermediate plan review (codification with 7+ items or 5+ file cascade). Single-stop for audit execution and discovery audits. See `raw/references/agent_onboarding.md` for full session-type taxonomy and protocol-calibration triggers.

## Configuration file edit discipline

- **`_thesis.md`** — never edited by the LLM by default. Vic-side action only. One-time Vic-authorized rework exception applied during Sessions 32-36 arc per CLAUDE.md v9 Section 1.1; default ownership convention has resumed.
- **`frameworks.md`** — human-maintained at v10.1. LLM proposes edits at codification sessions; edits require explicit approval. No silent revisions. Same one-time-rework exception applies (v10/v10.1 collaborative chat drafting Sessions 32-36); default ownership resumed.
- **`CLAUDE.md`** — operational conventions at v9. LLM proposes edits at codification sessions; edits require explicit approval.
- **Wiki pages** — LLM-maintained. Standard editing per CLAUDE.md conventions (Source audit notes, Change log, frontmatter `last_updated`, citations).

## Active monitoring conventions

These conventions track patterns that warrant codification once a third instance accumulates. Current counts live in `MEMORY.md` (snapshot) and `log.md` tail (latest session entry). Verify counts against canonical files before relying on them.

- Tier 1/Tier 2 framing gap (B2 unified)
- Cross-venue gap (structurally distinct from B2)
- CEO combativeness
- Reciprocal non-naming pattern

## After onboarding

Once the read sequence is complete, the agent has full vault context. Confirm onboarding completion to the user with a brief summary (vault state, current backlog items, monitoring conventions at current counts). Then proceed to the user's task.

If the user provides a session kickoff with its own Phase 0 context-loading instructions, those instructions are session-specific and may overlap with this skill's read order — that overlap is acceptable; do not skip kickoff instructions because they were already covered here.

## Maintenance

This skill is a navigation aid. It is updated when the vault's directory structure or canonical-file ownership changes, not on every session. Drift between this skill and `CLAUDE.md` / `frameworks.md` content is expected and acceptable for non-load-bearing items (specific monitoring counts, backlog item lists, vault metrics) because the skill points at canonical sources rather than caching their content. Drift on load-bearing items (read-order, meta-principles, edit discipline) requires correction.

Update this skill at codification sessions if the vault structure or principles change.
