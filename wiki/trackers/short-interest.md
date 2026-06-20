---
type: tracker
last_updated: 2026-06-19
---

# Short Interest Watch — what the crowd is betting against in the vault

Short interest is the cleanest *quantified* read on consensus skepticism: how hard the market is betting **against** a name (shares sold short), and how crowded that bet is (days-to-cover). This tracker crosses that signal against the **vault's own conviction** per name — and the intel falls out of the two cases: where the crowd **agrees** with a vault caution (confirmation), and where the crowd **disagrees** with a vault thesis (an inverse divergence to stress-test). It is the positioning-side companion to [[forward-edge-tracker]] (consensus vs. vault) and [[what-could-go-wrong]] (where the vault could be wrong).

**Source / tier.** FINRA Consolidated Short Interest (official, all US exchanges), joined to SEC shares-outstanding for the `%`. Raw snapshots live in `raw/data/short-interest/`, collected by the `/short-interest-snapshot` skill. This is **Tier-4 sentiment data** — positioning, not fact; never cited as canon, never a buy/sell. Describe-don't-recommend holds throughout.

## How to read this (the reading rule)

- **The signal is the outliers and the movers, never the levels on low-short mega-caps.** NVDA (1.2%), MSFT (1.2%), GOOGL (0.7%) carry almost no short interest — that is noise, not a finding. Lead with the names that clear a threshold.
- **The vault-native frame — confirm vs. challenge:**
  - **CONFIRM** = heavy short on a name the **vault is already cautious on** → the bears agree with us; reinforces the relevant risk.
  - **CHALLENGE** = heavy short on a name the **vault is bullish on** → an *inverse divergence*: either a blind spot or a contrarian confirmation. These carry a catalyst + falsifier and a `/bear-case` pointer — they are the highest-value items.
- **Thresholds (this snapshot):** notable short = **≥8% of shares outstanding**; crowded = **≥5 days-to-cover**; mover = **±15% change vs the prior settlement**.
- **Blind spots.** The `%` is **shares-outstanding basis, not float** — it runs *lower* than the float % traders quote. Data is **twice-monthly with a ~1–2 week lag** (a sentiment gauge, not a timing tool). Positioning ≠ outcome — the shorts are often right, often wrong. A handful of names carry no `%` (META, CRWV, FLNC — share-count tagging) but still have the core fields.

## Current readings

*The data tables below are **auto-refreshed** by `/short-interest-intel` from the latest FINRA snapshot (the settlement date is shown in the block). Everything **outside** the fenced block — the frame, the Intel prose, the watch-list, the change log — is human-curated and preserved across refreshes.*

<!-- SHORT-INTEREST-DATA:START -->
<!-- SETTLEMENT: 2026-05-29 -->

### Most shorted (short interest as % of shares outstanding, ≥8%)

| ticker | short interest | short %out | days-to-cover | Δ vs prior | vault read | thesis |
|---|---|---|---|---|---|---|
| **LEU** | 4.2M | 30.39% | 5.17 | -2.13% | **CHALLENGE** | HALEU enrichment chokepoint |
| **CORZ** | 71.9M | 22.6% | 5.42 | +12.15% | **CONFIRM** | AI-datacenter host / landlord |
| **NVTS** | 36.1M | 19.68% | 1.05 | -6.11% | **CONFIRM** | power semis (800V DC) |
| **AMPX** | 25.6M | 18.1% | 2.35 | +12.98% | — | defense silicon-anode batteries |
| **NBIS** | 44.3M | 17.51% | 2.56 | -1.78% | **CONFIRM** | neocloud (GPU renter) |
| **MP** | 28.1M | 15.78% | 4 | +2.27% | **CHALLENGE** | rare-earth-magnet chokepoint |
| **COHU** | 7.2M | 15.31% | 4.52 | +12.55% | — | semi test (counterpoint) |
| **LITE** | 10.2M | 13.14% | 1.93 | +11.68% | **CHALLENGE** | photonics / CPO laser |
| **AEHR** | 4.1M | 13.04% | 1.77 | -14.31% | — | advanced-packaging test |
| **AAOI** | 10.0M | 12.51% | 1 | +7.53% | **CONFIRM** | transceiver assembler |
| **NOVT** | 4.2M | 11.86% | 10.01 | -1.51% | **CHALLENGE** | humanoid sensor / datacenter |
| **AXTI** | 7.3M | 11.15% | 1 | -11.69% | — | InP substrates |
| **VECO** | 6.2M | 10.16% | 6.09 | +1.38% | — | semi equipment |
| **BE** | 28.6M | 10.04% | 2.74 | -1.52% | — | fuel cells / BTM power |
| **VPG** | 1.2M | 9.58% | 1.51 | +31.72% | **CONFIRM** | humanoid force/torque sensor |
| **AVAV** | 4.6M | 9.23% | 3.03 | -0.3% | **CHALLENGE** | defense drones |
| **OUST** | 5.9M | 9.23% | 1 | -4.79% | **CONFIRM** | lidar / Physical-AI sensing |
| **POWI** | 4.6M | 8.2% | 2.61 | +14.1% | — | power semis |

### Most crowded (days-to-cover ≥4)

NOVT 10.01 · MRCY 7.73 · VECO 6.09 · CORZ 5.42 · LEU 5.17 · AAON 4.74 · COHU 4.52 · TDY 4.15 · MP 4

### Movers (change vs the prior settlement)

- **Skepticism building (rising short):** ONTO +78.53% · VPG +31.72% · PLAB +26.64% · NVT +17.92% · MPWR +17.42% · LSCC +16.68%
- **Bears covering (falling short):** AEHR -14.31% · AAON -13.17% · ENS -12.9% · MOD -12.23% · AXTI -11.69% · INOD -11.5% · TSEM -11.43% · AMZN -11.35% · KTOS -11.01% · ON -11%

*(The other 37 vault names sit below all thresholds — low short interest, nothing notable.)*
<!-- SHORT-INTEREST-DATA:END -->

## Intel — where the crowd agrees vs. disagrees with the vault

### Crowd AGREES with the vault (skepticism confirmed)

- **CORZ (22.6%, rising +12%)** — the vault's host page states the thesis and the central risk are the *same fact*: **CoreWeave is 100% of colocation revenue**. The crowd's heavy and *rising* short is the market pricing exactly that concentration. Reinforces [[CORZ]] honest-verdict + [[AI-buildout-who-holds-the-risk]].
- **NBIS (17.5%)** — a GPU-renting price-taker that holds *no chokepoint*; the short interest agrees with the vault's neocloud-fragility read ([[neocloud-moat-durability]], [[AI-buildout-who-holds-the-risk]]).
- **NVTS (19.7%)** — the vault's honest-verdict already flags substantive execution risk (FY2025 revenue −45%, widening loss); the crowd agrees. (Low days-to-cover, 1.1 — heavy short, but easy to cover.)
- **AAOI (12.5%)** — confirms the vault's "structurally fragile assembler" read. *Refinement to flag for [[forward-edge-tracker]]:* that page frames AAOI as "the market prices a winner"; the short interest shows a meaningful camp is **not** pricing a winner — the cautious vault view has company.
- **OUST (9.2%)** — the vault already grades the camera/LiDAR layer at the bottom of the value-capture map (commoditizing); the short interest is consistent.

### Crowd DISAGREES with the vault (inverse divergence → stress-test)

*Each is a forward-edge-style entry: the vault's bullish read, the likely bear thesis the shorts are pressing, and the falsifier. Not a contrarian buy signal — a flag to go understand the bear case (`/bear-case`).*

- **LEU — 30.4% short (the loudest disagreement in the vault).** Vault view: Centrus is the **sole NRC-licensed Western HALEU enricher**, the standout in [[HALEU-fuel-chokepoint]]. The crowd's *vault-highest* short is almost certainly pressing the pre-revenue / dilution / cash-burn risk and the moat *shelf-life* (the funded supply response — General Matter / Orano / Centrus tri-split — eroding "sole licensed" toward ~2030). **Catalyst (vindicates the vault):** firm HALEU offtake + the operating Phase-II / funded Phase-III lead converting to revenue ahead of new entrants. **Falsifier (vindicates the shorts):** continued dilution funding a pre-revenue ramp while the supply-response compresses the moat faster than the cash runway → run `/bear-case LEU`.
- **MP — 15.8% short, 4.0 days-to-cover.** Vault view: the only scaled US rare-earth producer (materials_tier 1), a vertically-integrated magnet chokepoint central to Defense & Drones. The likely bear thesis: DoD-dependence / price-floor reliance, China dumping/retaliation risk, and a rich valuation on a pre-scale magnet ramp. **Catalyst:** the 10X magnet facility and DoD price-floor de-risking revenue. **Falsifier:** magnet ramp slips while China price pressure resumes → `/bear-case MP`.
- **AVAV — 9.2% short.** Vault view: bullish on AeroVironment within the Defense & Drones priority. Bear thesis likely lumpy procurement / valuation / Blue Halo integration. **Falsifier:** procurement air-pocket or integration drag → `/bear-case AVAV`.
- **NOVT — 11.9% short, *10.0 days-to-cover* (most-crowded short in the vault).** Vault view: a clean US-listed humanoid-sensor / GenAI-datacenter pick Goldman underweights. The extreme crowding says the market disagrees hard — likely pressing that the humanoid + datacenter legs are still a small slice of a mostly medical/industrial compounder. **Falsifier:** the GenAI-datacenter collective (~15% of sales, ~20% YoY) stalls → `/bear-case NOVT`.

## Watch-list (track the delta over snapshots — the real signal compounds)

The contested names to watch the *trend* on as snapshots accumulate: **LEU, MP, CORZ, NBIS, AVAV, MRCY, NOVT** (the confirm/challenge anchors) plus the live movers **ONTO, VPG, PLAB** (rising) and the covering names **AEHR, KTOS, AMZN** (falling). A single reading is a level; the diff between settlements — skepticism building vs. bears covering — is what this page exists to catch.

## Cross-references / boundary

- Feeds [[forward-edge-tracker]] (the inverse divergences — where the vault is more bullish than the crowd) and corroborates [[what-could-go-wrong]] (where the crowd's skepticism aligns with a vault risk).
- Raw data: `raw/data/short-interest/short-interest_<settlement>.csv`, collected by `/short-interest-snapshot`. Schema + coverage in `raw/data/short-interest/README.md`.
- **Tier-4 / describe-don't-recommend:** a heavy short is a *question to investigate* (run `/bear-case`), never a verdict and never a trade signal.

## Change log

- **2026-06-19:** Created. First pass from the 2026-05-29 FINRA snapshot (70/70 vault names). Established the confirm/challenge frame, the reading rule, and the watch-list. Standout findings: **LEU 30.4%** (the loudest disagreement with a vault chokepoint thesis), **CORZ 22.6% + rising** (confirms the 100%-CoreWeave concentration risk), **MP 15.8%** (rare-earth chokepoint inverse divergence), **NOVT** most-crowded short (10.0 days), **ONTO +78.5%** rising. Trend analysis is single-period for now (FINRA's change-vs-prior); the cross-snapshot signal sharpens as more snapshots accumulate.
