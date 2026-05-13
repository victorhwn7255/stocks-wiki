# Session types and stop protocol calibration

**Scope.** Reference material for vault session classification and protocol selection. Companion to `.claude/skills/agent-onboarding/SKILL.md`, which covers full vault onboarding (read order, meta-principles, edit discipline). This file holds the meta-content on session-type taxonomy and stop-protocol calibration that has not yet migrated to canonical convention text in `CLAUDE.md`.

**Maintenance.** Updated when session-type taxonomy expands or stop-protocol triggers are revised. Not a state-tracking document; current vault state lives in `MEMORY.md` and `log.md` tail.

**Last updated.** 2026-05-02 (post-Session-37 sync).

---

## Session type taxonomy

The vault has produced the following session types through Session 37. Each has different structural emphasis and protocol requirements. Several emerged or refined post-Session-19; cross-references to canonical examples are inline.

### Ingest types

**Single-company ingest.** Three primary sources for one company → one new company page + cross-reference updates. Two-stop default. Examples: Sessions 1-10, 14, 16, 22 ([[VRT]]), 36 ([[FLEX]] — first canonical AI-datacenter-scope ingest under multi-domain frontmatter convention).

**Paired ingest — substantive paired analytical product variant** (canonical pattern). Six primary sources across two same-tier same-sub-domain companies → two new company pages + dedicated cross-company analytical product. Two-stop default. Often produces new chokepoint pages from paired evidence (`InP-supply.md` from Session 13 origination). Examples: Session 6 ([[AEHR]]+[[ONTO]] equipment-tier functional split), Session 13 ([[AXTI]]+[[VECO]] substrate + epi InP). Codified in `CLAUDE.md` v9 Section 3.14.

**Paired ingest — parallel-but-independent variant.** Two companies under looser thematic adjacency where Stop 1 cross-company analytical-product candidates assessment shows 0 explicit candidates; middle sections allowed to differ; cross-references in Thesis role rather than dedicated cross-company section. Examples: Session 27 ([[CRDO]]+[[ANET]] networking-component adjacency at different layers), Session 28 ([[VIAV]]+[[PLAB]] semi-infrastructure adjacency at same Layer 4 but different photonics-thesis fit). Codified in `CLAUDE.md` v9 Section 3.14 with variant selection criteria.

**Paired ingest — cross-tier variant.** Two companies at different per-domain tiers within the same framework → first-canonical pattern at Session 37 ([[ETN]] Framework 7 Tier 1 + [[GEV]] Framework 7 Tier 3). Middle sections deliberately differ to capture cross-tier framing; cross-company analytical product surfaced in Thesis role + cross-vault positioning subsections on each page. Period-offset-paired-ingest discipline applied (1-quarter offset between companies; honest framing throughout). Convention candidate for Session 38 codification.

**Refresh.** One new primary source for an existing company → updates to existing company page + downstream propagation. Two-stop. Examples: Session 17 (NVDA GTC March 2026 — first refresh; tests venue-specific disclosure patterns when refresh source is non-earnings-call).

**Refresh redirect + factual correction.** Refresh session that surfaces factual correction need across multiple existing pages. Single-stop or two-stop. Example: Session 26 + addendum ([[AEHR]] Q3 FY2026 Option C redirect with grep-verified scope correction across 16 affected references; A6 (g) factual error scope discipline origination).

### Synthesis types

**Theme page build.** Cross-cutting analytical map → one new theme page + cross-reference updates. Two-stop or three-stop depending on scope. **Tier 3-anchored variant** (Session 19 origination of `datacenter-photonics-supply-chain.md`) operates with three-source coordination from Vic-authored synthesis; cross-validated through Sessions 20-22 across three counterparty-attribution-only annotation modes (over-claim / inversion / reciprocal-confirmation per A1 codification in `CLAUDE.md` v9 Section 3.5).

**Multi-source synthesis.** Cross-cutting chokepoint or theme content built from multiple primary-source ingests already on existing company pages → new chokepoint page + cross-reference propagation. Two-stop. Examples: Session 30 (`optical-dsp-phy-supply.md` from MRVL+AVGO+CRDO), Session 31 (`advanced-optical-packaging.md` from FN+LITE+COHR+AAOI).

**Multi-vantage-point synthesis.** Cross-cutting theme content built from ≥7 vault company sources with coordinated analytical product → typically large theme/chokepoint page. Two-stop. Example: Session 32 (`cpo-integration.md` from 9 vault companies; closes Sessions 27-32 photonics arc; first theme-page-overlap discipline application; Option C Scale-up + Scale-out bifurcation handling).

**Multi-source chokepoint synthesis.** Existing provisional chokepoint page promoted to canonical via additional source coverage → page-top disclaimer removed; "Remaining uncertainties" section replaces "What would confirm or weaken this framing." Two-stop. Example: Session 33 (`InP-supply.md` provisional → canonical with Option C bifurcation handling for substrate + epitaxial unified single page).

**Selective integration.** Discrete content integration without broader synthesis (e.g., adding Tier 3 research framework reference to existing pages). Single-stop or two-stop. Example: Session 24 (chokepoint research framework integration).

**Dual-page creation.** Two new pages of different types (theme + chokepoint) created in single session under coordinated analytical scope. Two-stop. Example: Session 25 (`chokepoint-investability-priorities.md` + `wafer-level-siph-test.md`).

### Configuration types

**Codification.** `frameworks.md` or `CLAUDE.md` version bump → configuration-file edits + downstream propagation. Two-stop or three-stop depending on backlog magnitude. Triggered by 5+ backlog items OR every ~5 ingests. Examples: Session 15 (frameworks.md v4→v5, two-stop), Session 18 (frameworks.md v6→v7, three-stop — first three-stop session), Session 23 (CLAUDE.md v6→v7), Session 29 (CLAUDE.md v7→v8).

**Pure structural rework.** Reorganizes existing canonical content without modifying it; distinct from codification (which adds canonical content). Single-stop or two-stop. Examples: Session 34 (CLAUDE.md v8 → v8.1 6-section hierarchy reorganization — first vault pure structural rework), Session 35 (`log.md` aggressive reduction + descending-order reorder — second).

**Vault scope rescope codification.** Substantive scope-aligned codification across configuration files following Vic-authorized ownership-exception reworks. Multi-stop. Example: Session 36 (CLAUDE.md v8.1 → v9 aligning vault scope to AI datacenter supply chain post-`_thesis.md` rework + `frameworks.md` v10/v10.1 rework).

### Audit types

**Discovery audit.** Vault state review without primary-source ingest → structured recommendation document, no file writes. Single-stop. Example: Session 11 (promotion candidates / convention candidates).

**Audit execution.** Implements previously-approved audit findings without new analytical synthesis. Single-stop. Often combined with codification (Session 12 precedent — audit execution + CLAUDE.md v5 → v6 codification).

### Finalization types

**Finalization-only execution.** Mechanical apply of pre-specified updates from prior session's Stop 2 deliverable (typically following filesystem or other infrastructure issue blocking initial Stop 2 completion). No new analytical work; no convention decisions; scope-disciplined to specified updates only. Single-stop. Example: Session 37 finalization (post-EPERM-resolution apply of 4 cross-reference updates).

---

## Stop protocol calibration

Two-stop is the default. Three-stop and single-stop apply under specific conditions.

**Two-stop trigger (default).** Standard ingest, refresh, theme page build, single codification item, paired ingest (any variant), multi-source synthesis. Stop 1 produces plan; Stop 2 executes after human approval.

**Three-stop trigger.** Codification with 7+ items OR projected 5+ file cascades. Stop 1 reviews codification scope; Stop 2 reviews wiki page propagation plan; Stop 3 executes. First three-stop session: Session 18 (frameworks.md v6→v7 with 14-item backlog).

**Single-stop trigger.** Audit execution, discovery audit, very lightweight refresh, finalization-only execution, pure structural rework with single-action scope. Default to two-stop when uncertain.

**Mid-Stop-1 clarification escape valve.** If during Stop 1 the agent encounters a source-interpretation question that genuinely blocks plan formation (e.g., framework placement is genuinely 50/50 with material evidence both ways and Stop 1 cannot recommend a default), pause mid-Stop-1 and ask a single clarifying question before completing the plan. Use sparingly. Most ambiguity should be flagged within the Stop 1 plan itself as uncertainty notes or confidence calibrations, not pre-resolved through additional clarification rounds.

---

## Codification candidate

Per CLAUDE.md v9 codification cadence, the following content is candidate for migration to canonical convention text in `CLAUDE.md` at next codification (Session 38 v9 codification per current sequencing):

- **Session-type taxonomy** (this document's primary content) — at least the ingest types + finalization-only type are stable enough for canonical migration; synthesis types may benefit from additional vault accumulation before codification
- **Cross-tier paired ingest variant** (Session 37 first canonical) — codification trigger met (first canonical application; convention candidate flagged in Session 37 Phase 4 reflection)
- **Period-offset paired ingest discipline** (Session 37 origination) — codification candidate
- **Pure structural rework session type vs codification session type distinction** (Sessions 34+35 origination) — codification candidate
- **Stop protocol calibration triggers** — already partially covered in CLAUDE.md v9 Section 3.14 paired-ingest convention; full stop-protocol-calibration table could migrate

If migration occurs at Session 38, this file would be reduced to a residual reference (e.g., Session-by-session example index) or deleted entirely. Decision deferred to Session 38 codification scope.

---

## Cross-reference

For load-bearing operational principles (read order, meta-principles, configuration file edit discipline, active monitoring conventions), see `.claude/skills/agent-onboarding/SKILL.md`. This document is the companion reference, not the primary onboarding artifact.
