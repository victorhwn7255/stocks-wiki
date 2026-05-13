---
type: chokepoint
tickers: [AEHR]
last_updated: 2026-04-28
---

# Wafer-Level Silicon Photonics Reliability Test

*Single-company exposure note: [[AEHR]] is currently the only public pure-play for wafer-level silicon photonics reliability test in the vault and in the framework Tier 3 source (`raw/research/photonics-chokepoint-table.md` Chokepoint #10 / Ranking Summary Rank 8). Page maintained for portfolio tracking and analytical learning despite weaker multi-company concentration criteria than other vault chokepoint pages ([[InP-supply]], [[datacenter-laser-supply]]). Provisional chokepoint page per CLAUDE.md v6 convention.*

*Expansion triggers (any one would broaden this from single-company to multi-company chokepoint and warrant page promotion from provisional to canonical):*

1. *FormFactor (FORM) entering vault as wafer test participant.*
2. *ASE Technology or Amkor Technology primary-source ingestion producing OSAT-tier wafer test exposure.*
3. *New public entrants emerging in wafer-level photonic reliability test ecosystem (e.g., Onto Innovation expanding metrology into reliability test; Advantest or Teradyne entering photonic reliability test segment).*

*Source-anchored on [[AEHR]] Session 6 ingest (10-K + 10-Q + Q3 FY2026 call). Tier 3 framework reference: `raw/research/photonics-chokepoint-table.md` Chokepoint #10 (Wafer-level SiPh reliability test).*

## Overview

Wafer-level silicon photonics reliability test is a narrow but structurally significant chokepoint in the AI datacenter photonics supply chain. As silicon photonics PICs and optical I/O devices become more expensive after packaging and integration, wafer-level burn-in / reliability screening improves known-good-die (KGD) economics and reduces downstream failure cost.

[[AEHR]] is currently the only public pure-play exposure to this chokepoint at the vault and Tier 3 framework level. The single-company-exposure deviation from typical vault chokepoint criteria (multi-company concentration, e.g., [[InP-supply]] documenting AXTI/Sumitomo/JX three-supplier concentration; [[datacenter-laser-supply]] documenting LITE/COHR cross-validated supplier-side scarcity) warrants the provisional chokepoint page convention with explicit single-company-exposure disclaimer per Option A.

Portfolio tracking purpose: AEHR's wafer-level burn-in positioning is structurally distinct from finished-module test (Keysight, VIAVI, Anritsu) and adjacent metrology ([[ONTO]]). Tracking this chokepoint dynamic supports analytical learning about whether AEHR's narrow positioning broadens into multi-company concentration as silicon photonics / optical I/O production volumes scale through 2026-2028.

## Chokepoint mechanics

### Why wafer-level SiPh reliability test matters

Silicon photonics and optical I/O devices become more expensive after packaging and integration. As CPO and optical I/O move into high-volume AI infrastructure, the cost of packaging a bad photonic die rises substantially. Wafer-level burn-in / reliability screening at the wafer or die level catches weak photonic dies before they enter expensive packaging cycles, improving KGD economics.

The economic logic: catching a defective die at wafer level costs the wafer-level test step. Catching the same defective die after packaging costs the packaging step plus the optical engine integration plus the rework or scrap of the assembled module. As photonic devices migrate into more expensive package architectures (CPO co-packaged with switch ASICs; optical I/O integrated into compute packages), the spread between pre-packaging detection cost and post-packaging detection cost widens.

### Why this becomes a chokepoint

As optical engines become more integrated and expensive, the cost of packaging a bad die rises. Earlier reliability screening becomes more valuable if SiPh / optical I/O moves into high-volume AI infrastructure. The chokepoint potential is structural — wafer-level burn-in attach rate is currently low; if attach rate increases as photonic device costs rise, wafer-level test becomes a binding capacity constraint.

The framework characterization (per `raw/research/photonics-chokepoint-table.md`): "Narrow but clean photonics-specific test exposure. AEHR should be treated as a specialized photonics test-infrastructure name, not a broad optical transceiver company."

### Investment relevance

Narrow but clean photonics-specific test exposure. [[AEHR]] is not a finished-module tester; it is an upstream reliability-screening equipment supplier tied to wafer/die-level photonic IC testing. Per Tier 3 source: "High-upside narrow exposure if wafer-level burn-in becomes standard in SiPh / optical I/O production flows."

## AEHR positioning

[[AEHR]] occupies a narrow but clean photonics-specific test exposure. Per Session 6 ingest:

- Layer 3-4 (per `frameworks.md` v7), photonics_tier 4
- FOX (Final Optical eXamination) wafer-level burn-in system family is the primary product line
- Multi-quarter customer order acceleration documented Session 6 Q3 FY2026 call
- Single-company-customer concentration risk flagged at Session 6 ingest

**Wafer-level burn-in vs. finished-module test distinction.** [[AEHR]] FOX systems test SiPh dies at wafer level before packaging; finished-module testers (Keysight, VIAVI, Anritsu — see Section 4 below) test fully packaged optical modules at the post-assembly stage. The two test stages are structurally distinct supply chain layers — finished-module test cannot substitute for wafer-level burn-in because finished-module test occurs after the expensive packaging step that wafer-level burn-in is designed to protect.

See [[AEHR]] for primary-source canonical framing including FOX system order trajectory, customer concentration analysis, ASE ISE Labs partnership context, and Session 6 Source audit notes. This chokepoint page does not duplicate AEHR.md content; it documents the chokepoint dynamic and adjacent test ecosystem framing in which AEHR operates.

## Adjacent test ecosystem

The wafer-level SiPh reliability test chokepoint is one of three structurally distinct test layers in AI datacenter photonics:

### Wafer-level burn-in / reliability test (this chokepoint)

Primary vault exposure: [[AEHR]]. Pre-packaging reliability screening at wafer or die level. Currently single-company vault exposure; expansion triggers documented in page-top disclaimer.

### Finished-module optical test (Tier 3 framework Chokepoint #9 / Ranking Summary Rank 6)

Non-vault exposures (Tier C future-ingest candidates per Session 24 Integration 4 promotion to Tier C):

- **Keysight (KEYS)** — 1.6T optical and electrical test, 224G measurement, IEEE 802.3dj methodologies. Most prominent test name across all three Session 19 reports.
- **[[VIAV]]** — vault company (Session 28 paired ingest with [[PLAB]]). Framework Rank 6 finished-module optical test (medium-high conviction); paired with Keysight and Anritsu in test-equipment refresh thesis. Per `frameworks.md` v8 Layer 4 / photonics_tier 4 / Framework 2.6 pure bottleneck participant. Spirent acquisition (HSE + network security + channel emulation testing businesses, closed October 16, 2025; $425M from Keysight Technologies) extended NSE data center ecosystem positioning. Multi-quarter visibility extension (one-and-a-half quarters historical → up-to-three quarters ahead) tied to hyperscaler vertical integration patterns.
- **Anritsu** — Framework Rank 6 finished-module optical test; 1.6T module evaluation, 200G/lane sampling oscilloscope.

[[VIAV]] in-vault post-Session 28; Keysight + Anritsu remain plain-text Tier C references per forward-wikilink discipline; over-claim mode annotation pending future primary-source verification for Keysight + Anritsu.

### Adjacent metrology

Vault: [[ONTO]] (Onto Innovation) — wafer-level metrology distinct from reliability test. Different supply chain layer; structurally adjacent but not substitutable for AEHR's wafer-level burn-in positioning. Metrology measures physical/optical properties (dimensions, films, alignment); reliability test verifies device function under accelerated stress conditions.

### OSAT-level test (potential adjacent participant)

ASE Technology and Amkor Technology may participate in wafer-level test integration at OSAT layer; primary-source verification pending. Per Session 24 Integration 3: ASE/AMKR are OSAT-layer photonic packaging participants structurally distinct from foundry layer; whether OSAT-tier wafer test integration emerges as multi-company concentration is open question (see Section 6 below).

### Wafer prober/test infrastructure (potential expansion trigger)

FormFactor (FORM) is the largest wafer prober supplier; not currently in vault. Future FormFactor entry into vault would expand wafer test exposure to multi-company concentration and warrant promotion from provisional to canonical chokepoint page status.

## Cross-references

- [[AEHR]] — primary vault company anchor; full primary-source content from Session 6 ingest
- [[chokepoint-investability-priorities]] — theme page Chokepoint 8 section provides Tier 3 framework canonical reference for wafer-level SiPh reliability test
- [[ONTO]] — adjacent metrology positioning; structurally distinct supply chain layer
- [[datacenter-photonics-supply-chain]] — Section 2.7 (Assembly / packaging / testing) for broader test ecosystem framing including non-vault test equipment vendors

## Open questions

1. Whether wafer-level SiPh reliability test attach rate is increasing or stable as AI photonics production volumes scale through 2026-2028. Current attach rate is low; chokepoint thesis depends on rate increase.
2. Whether OSAT-tier wafer test (ASE Technology, Amkor Technology) emerges as multi-company concentration with primary-source evidence. OSAT participation would expand exposure beyond AEHR single-company.
3. Whether FormFactor enters vault as wafer test participant. FormFactor is the largest wafer prober supplier; vault entry would warrant page promotion from provisional to canonical.
4. Whether Onto Innovation expands metrology positioning into reliability test. Onto Innovation is currently vault metrology exposure; reliability test expansion would broaden vault exposure to two-company concentration.
5. AEHR customer concentration trajectory — narrowing (would weaken chokepoint thesis toward single-customer dependency) or expanding toward multi-customer concentration (would strengthen toward multi-customer chokepoint participant).

## What would confirm or weaken this framing

Per provisional chokepoint page convention, pre-registered tests for cross-validating sources arriving in future ingest sessions:

### Strengthen signals (any would broaden chokepoint to multi-company concentration)

- AEHR FOX system order acceleration accompanied by multi-customer attach disclosure
- ASE Technology or Amkor Technology primary-source confirmation of wafer-level test integration at OSAT layer
- FormFactor entering vault as wafer test participant (highest-leverage expansion trigger)
- Onto Innovation expanding metrology positioning into reliability test (would broaden vault exposure)

### Weaken signals

- AEHR customer concentration narrowing (single-customer dependency increasing rather than multi-customer expansion)
- OSAT primary sources documenting wafer-level test handled in-house without third-party equipment supplier dependency
- Finished-module test (Keysight/VIAVI/Anritsu) capturing demand projected as wafer-level test demand (substitution rather than supply chain layer addition)
- Silicon photonics / optical I/O volumes plateauing rather than accelerating (would reduce KGD economics importance and chokepoint relevance)

## Source attribution

Primary-source anchor: [[AEHR]] Session 6 ingest (AEHR 10-K FY2025; AEHR 10-Q Q3 FY2026; AEHR Q3 FY2026 earnings call). See [[AEHR]] Source audit notes for per-source detail.

Tier 3 framework reference: `raw/research/photonics-chokepoint-table.md` Chokepoint #10 (Wafer-level SiPh reliability test) / Ranking Summary Rank 8. Vic-team-authored chokepoint research framework. Single canonical source per Vic direction at Session 24. Per A2 no-verification convention: framework claims about chokepoint positioning included with attribution at construction time; deviation-based refinement at primary-source ingest cycles.

## Source audit notes

### AEHR Session 6 ingest (Tier 1 + Tier 2, primary-source anchor)

Reference [[AEHR]] Source audit notes for full per-source detail. Wafer-level SiPh reliability test positioning content sourced from Session 6 canonical framing without duplication on this page.

### `raw/research/photonics-chokepoint-table.md` (Tier 3, Vic-team-authored chokepoint research framework)

Single canonical source per Vic direction. Canonical living document model — no date stamp; updates replace in-place. Per A2 no-verification convention: framework characterization of wafer-level SiPh reliability test as "Narrow but clean photonics-specific test exposure" included with attribution; deviation-based refinement at future primary-source ingest. Chokepoint #10 in source / Ranking Summary Rank 8 (Medium-high conviction, narrow).

## Change log

- **2026-04-27 (Session 25 dual-page creation):** Page created as provisional chokepoint page per Option A confirmation. First single-company-exposure chokepoint page in vault history. Single-company-exposure disclaimer + three expansion triggers + portfolio tracking purpose framing applied. Source-anchored on [[AEHR]] Session 6 ingest (no duplication; cross-reference). Tier 3 framework reference per page-top disclaimer. Cross-references to [[AEHR]], [[chokepoint-investability-priorities]] (mutual; theme page Chokepoint 8 section), [[ONTO]] (adjacent metrology), [[datacenter-photonics-supply-chain]] Section 2.7. Forward-wikilink discipline preserved: Keysight, VIAVI, Anritsu, ASE Technology, Amkor Technology, FormFactor, Advantest, Teradyne referenced as plain text per non-vault status.
- **2026-04-28 (Session 26 addendum — factual error correction):** AEHR ingest attribution corrected from "Session 4" to "Session 6" (10 instances) and "Q4 FY2025 call" / "Q4 FY2025 earnings call" to "Q3 FY2026 call" / "Q3 FY2026 earnings call" (3 instances). Original Session 25 page creation propagated kickoff-drafting error: AEHR was ingested at Session 6 (2026-04-20, paired with [[ONTO]]) using AEHR 10-K FY2025 + AEHR 10-Q Q3 FY2026 + AEHR Q3 FY2026 earnings call dated April 7, 2026 — per `log.md` line 280 and `wiki/companies/AEHR.md` Change log line 164. No content edits beyond mechanical text replacement; substantive analytical content unchanged.
- **2026-04-28 (Session 28 paired ingest — [[VIAV]] vault-status promotion):** Adjacent test ecosystem section "Finished-module optical test" subsection updated: VIAVI plain-text → `[[VIAV]]` wikilink. Brief framework positioning context added (Session 28 paired ingest; Layer 4 / photonics_tier 4 / Framework 2.6 pure bottleneck participant; Spirent acquisition + multi-quarter visibility extension framing). Forward-wikilink discipline preserved: Keysight + Anritsu remain plain-text Tier C references (over-claim mode annotation pending future primary-source verification). Frontmatter unchanged; substantive analytical content unchanged.
