---
type: company
tickers: [LSCC]
layer: 3
defense_tier: 4
foreign_issuer: false
last_updated: 2026-06-03
---

# LSCC — Lattice Semiconductor Corporation

## Thesis role

Lattice is the vault's **first dual-thesis-from-creation page** — a low-power FPGA maker that sits in *both* the AI-datacenter supply chain and the Defense & Drones supply chain. It was ingested for the Defense thesis as a candidate **secure-microelectronics chokepoint** (`defense_tier 4`), but the primary sources require an **evidence-led, honest-verdict framing**: LSCC is, right now, **overwhelmingly an AI-datacenter / hyperscaler story**, with defense a small, unquantified slice.

**The honest headline (Section 2.1 host-tensions-honestly):**
- **AI-datacenter is the dominant current lens.** Compute & Communications grew **+86% YoY** in Q1 FY2026, explicitly "driven by data-center AI / hyperscaler demand" (LSCC Q1 FY2026 call, May 4 2026). Total revenue +42% YoY; the AMI acquisition deepens an AI-server system-control platform. `layer 3` (specialized designer).
- **The defense connection is a genuine *capability* chokepoint, but not yet *revenue*.** LSCC's secure-control FPGAs (hardware root-of-trust; post-quantum/CNSA 2.0) are exactly the kind of trusted microelectronics the Defense thesis prizes — but defense/aerospace revenue is **unquantified** (folded into Industrial & Embedded; "aerospace customers" in passing), there is **no Trusted-Foundry / DMEA / NDAA framing**, and **zero drone/UAS disclosure** (LSCC FY2025 10-K + Q1 FY2026 10-Q). `defense_tier 4`, honest-verdict-qualified.
- **The central tension: ~64% of revenue is Greater China,** and LSCC is fabless on TSMC/Samsung/UMC — both of which cut hard against a "trusted *domestic* defense supply chain" narrative.

**Honest-verdict discipline applied.** Per Section 2.1, the page does not construct a defense-relevance narrative the evidence doesn't support. The secure-FPGA chokepoint *capability* is real and worth tracking; the defense *revenue* is thin/undisclosed; the China concentration is a counter-signal. Inclusion is for the secure-microelectronics capability + the dual-thesis cross-cut, with the tensions surfaced plainly.

## AI-datacenter thesis role (the dominant current lens)

Lattice positions its low-power FPGAs as the **"everywhere companion chip"** — silicon-agnostic, ecosystem-neutral parts that *enhance* CPUs/GPUs rather than compete with them, providing Secure Boot, power sequencing, platform management, IO aggregation, sensor bridging, and control across AI servers and advanced compute (LSCC Q1 FY2026 call). This is a Layer 3 specialized-designer position (fabless FPGA design IP).

- **Compute & Communications $106.6M, +86% YoY (62% of Q1 FY2026 revenue),** on hyperscaler / data-center AI demand (Q1 FY2026 10-Q + call). FY2025's Communications & Computing end market grew +28% YoY on "data-center applications, including general-purpose and AI-specific servers" (FY2025 10-K MD&A).
- LSCC declines to treat AI as a separate end market ("AI applications are pervasive across our end markets") but expects AI-related revenue to grow on a building design-win pipeline (FY2025 10-K).
- Management frames the company as evolving into a **"system-level solutions company"** — hardware + firmware + security + management + control — which is the strategic logic of the AMI acquisition (see The AMI acquisition).

**Placement nuance:** LSCC's AI-datacenter role is a server-control / compute-adjacent companion chip, which maps to **none** of the vault's five per-domain `*_tier` frameworks (photonics / memory / energy-power / equipment / materials). So it carries `layer 3` with **no AI `*_tier`** — the first such page — reflecting that the vault has not tier-framed the compute / server-control domain. AI-datacenter exposure is captured in prose, not a tier field.

## Defense & Drones thesis role — connections + honest verdict

The user's focus; handled evidence-led. Mapped onto `frameworks-defense-drones.md`:

**Framework D5 — secure-microelectronics chokepoint (the real connection, at the capability level).** Lattice's "Control & Security" FPGA line is a genuine trusted-microelectronics capability:
- **MachXO5D-NX** — crypto-agile algorithms + **hardware root of trust** with integrated flash + fail-safe secure remote field updates (FY2025 10-K Item 1).
- **MachXO5-NX TDQ** — "industry's first secure control FPGAs with full **CNSA 2.0-compliant post-quantum cryptography** support."
- **Lattice Sentry** — integrated system-level hardware-security solution stack.

This is the secure-control-FPGA capability the Defense thesis prizes (NDAA-compliant secure FPGAs / hardware root of trust per `frameworks-defense-drones.md` D5). `defense_tier 4` (supply-chain enabler / chokepoint capability). On the [[defense-drone-supply-chain]] map, LSCC sits at the upstream secure-microelectronics node — a chokepoint *capability* whose deeper dependence (TSMC fabrication) is the cross-thesis seam with the AI-datacenter vault.

**US-defense-budget structural positioning (honest framing).** The Defense thesis flags secure microelectronics as a high-conviction chokepoint, and LSCC is *structurally positioned* to benefit from rising US-government secure-microelectronics demand. **But that is thesis-structural, not company-disclosed:** LSCC does **not** cite US-defense-budget tailwinds anywhere; defense/aerospace is not a reported end market (folded into Industrial & Embedded, mentioned only as "aerospace customers" in a recovery comment); and it carries **no Trusted-Foundry / DMEA / NDAA-Section-889 / "trusted supply chain"** framing (FY2025 10-K). The secure-FPGA messaging is pitched broadly (Communications/Computing/Industrial/Automotive/Consumer), not as defense procurement. So LSCC *could* benefit from the US-defense-budget secure-microelectronics push, but the primary sources do not yet show it converting to material defense revenue.

**Drones (Section 3.3 disclosed/inferable/unknown).** **Disclosed:** nothing — *zero* mentions of drones / UAS / unmanned in either filing. **Inferable:** Lattice low-power FPGAs are structurally used across edge/defense systems (including drones) as companion chips, consistent with its "everywhere companion chip" positioning — but this is inferable dual-use, not disclosed. **Unknown:** any drone-specific revenue, design wins, or programs. Per discipline, no drone narrative is asserted.

**Honest verdict (Section 2.1).** The secure-FPGA *capability* is a real chokepoint; LSCC is **not** a defense-revenue chokepoint owner today; and the China concentration (next section) directly undercuts the "trusted domestic supply chain" thesis the capability would otherwise serve.

## The 64% China revenue + Taiwan-fab dependence (the central tension)

This is the honest-verdict centerpiece, and it cuts against the defense/trusted-supply-chain framing:
- **Greater China = 64% of Q1 FY2026 revenue** (LSCC Q1 FY2026 10-Q), up sharply from 48% a year earlier; FY2025 Greater China was 52% (FY2025 10-K). China grew +90.6% YoY in Q1 — i.e., the AI/hyperscaler growth is disproportionately China-channel.
- **~94% of Q1 revenue runs through distributors** (two distributors ≈69% of FY2025 revenue) — concentration on top of concentration (Q1 FY2026 10-Q; FY2025 10-K).
- **Fabless** on **TSMC, Samsung, UMC, Seiko Epson** (Taiwan / Korea / Japan) with **ASE / Amkor** OSAT (Malaysia / Taiwan / Japan) — explicit Taiwan-fab + China-Taiwan geopolitical risk (FY2025 10-K Item 1A).
- The 10-K flags a looming **additional Section 301 tariff on Chinese semiconductors beginning June 23, 2027** (on top of the existing 50% tariff).

**Why this matters to the thesis.** The Defense thesis (per `frameworks-defense-drones.md` D5) notes that secure-FPGA *design/IP* is a defensible Western position, **but the deeper chokepoint is TSMC fabrication in Taiwan, which NDAA rules don't solve.** LSCC embodies exactly that tension: a "secure/trusted" FPGA designer whose revenue is 64% China and whose silicon is fabbed in Taiwan. For a defense secure-microelectronics thesis, this is the structural caveat; for the AI-datacenter thesis, it is concentration + tariff/geopolitical risk.

## Financial snapshot

Separate tables per period (Section 4.1). **Section 2.11 N/A** — Lattice uses a 52/53-week fiscal year ending the Saturday nearest December 31 (FY2025 ended Jan 3 2026, ~3-day offset → week-scope, substantively calendar; joins the AMD/INTC/NVDA precedent).

### FY2025 annual (10-K; fiscal year ended January 3, 2026)

| Metric | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Total revenue | $523.3M (+2.7%) | $509.4M | $737.2M |
| Gross margin | 68.2% | 66.8% | 69.8% |
| Operating income | $11.2M | $34.5M | $212.3M |
| Net income | **$3.1M** | $61.1M | $259.1M |
| Diluted EPS | **$0.02** | $0.44 | $1.85 |

End markets FY2025 (prior 3-segment basis): Communications & Computing $292.7M (55.9%, +28%); Industrial & Automotive $194.0M (37.1%, −18%); Consumer $36.6M (7%). **Honest framing:** FY2025 was a trough/rebuild year — revenue roughly flat off the FY2023 peak ($737M) and **GAAP net income collapsed to $3.1M (−95% YoY)** as R&D + SG&A rose faster than the recovering top line. (FY2025 10-K Item 7 + Item 8.)

### Q1 FY2026 quarterly (10-Q; fiscal quarter ended April 4, 2026)

| Metric | Q1 FY2026 | Q1 FY2025 |
|---|---|---|
| Total revenue | **$170.9M** (+42% YoY, +17% seq) | $120.2M |
| Gross margin (GAAP) | 68.8% (~70% non-GAAP) | 68.0% |
| Operating income | $26.1M | $7.0M |
| Net income (GAAP) | **$21.8M** | $5.0M |
| Diluted EPS (GAAP) | **$0.16** | $0.04 |
| Diluted EPS (non-GAAP) | $0.41 (+86% YoY) | — |

End markets Q1 FY2026 (new 2-segment basis): Compute & Communications $106.6M (62%, **+86%**) / Industrial & Embedded $64.3M (38%, +2.6%, "aerospace recovery"). Cash $140M, **no debt** (pre-AMI); $15M buyback; GAAP operating cash flow $50.3M; free cash flow $39.7M. **Q2 FY2026 guidance: revenue $175–195M ($185M midpoint, ~+50% YoY); non-GAAP gross margin ~70%; non-GAAP EPS $0.42–0.46.** Honest framing: Q1 FY2026 is the inflection — AI-datacenter demand + operating leverage drove net income +335% YoY off the FY2025 trough. (Q1 FY2026 10-Q + call.)

## The AMI acquisition (mid-year forward event)

On **May 4, 2026** (the earnings-call date; disclosed as a subsequent event in the Q1 10-Q), Lattice announced a definitive agreement to acquire **AMI (AMI TopCo, Inc.; CEO Sanjoy Maity, who joined the call)** for **~$1.65B — $1.0B cash + $0.65B stock** (~5.4M shares at the May 1 price of $120.96), financed via a **$950M 364-day term loan + $200M revolver** (Wells Fargo / Morgan Stanley commitment). AMI is a leader in **platform firmware, secure boot, BIOS, BMC (baseboard management controller), device management, and system-control software** — a software-centric, asset-light model.

**Strategic intent + thesis read:** management frames the deal as creating "the industry's most comprehensive **secure management and control platform**" for **AI servers / advanced compute / communication infrastructure / industrial**, with AMI's firmware remaining processor- and silicon-agnostic alongside Lattice's "everywhere companion chip" FPGAs. It is explicitly **AI-server / system-control oriented — reinforcing the AI-datacenter lens, not the defense one.** The secure-boot / firmware capability has *dual-use* security relevance, but it is pitched for AI servers. Expected accretive to gross margin, free cash flow, and non-GAAP EPS; supports >$1B annual run-rate by end-2026; targeting close ~Q3 2026. Full rationale + pro-forma financials deferred to the Q2 FY2026 10-Q.

## End-market reclassification (reporting shift)

Beginning Q1 FY2026, LSCC streamlined reporting from **three** end markets (Communications & Computing / Industrial & Automotive / Consumer) to **two** (Compute & Communications / Industrial & Embedded), folding Consumer into Industrial & Embedded, with **all prior periods recapped for comparability** (Q1 FY2026 call + 10-Q). A Section 2.1-adjacent reporting reclassification (not a segment/M&A-driven restructuring like the AVAV/BlueHalo case); use restated comparatives and avoid blending the 3-segment FY2025 view with the 2-segment FY2026 view.

## Source audit notes

### LSCC FY2025 10-K (Tier 1; fiscal year ended January 3, 2026; filed February 13, 2026)
Prior 3-end-market basis. The trough/rebuild year (GAAP net income $3.1M, EPS $0.02 vs FY2023 $1.85). Greater China 52% of revenue; distributors 84% (two ≈69%); fabless on TSMC/Samsung/UMC/Seiko Epson. Secure-control FPGA line (MachXO5D-NX root-of-trust; CNSA 2.0 PQC; Sentry). **Defense/aerospace unquantified** (an application within Industrial & Automotive; a "secular tailwind"), **no NDAA/DMEA/Trusted-Foundry framing**, **zero drones/UAS.** Flags the June-2027 additional Section 301 tariff on Chinese semis + China-Taiwan geopolitical risk to its foundry model.

### LSCC Q1 FY2026 10-Q (Tier 1; fiscal quarter ended April 4, 2026; filed May 4, 2026)
The AI-datacenter inflection: revenue $170.9M (+42%), Compute & Communications +86% on hyperscaler/data-center AI; GAAP net income $21.8M, EPS $0.16. **Greater China 64%** (up from 48%); distributors 94%. New 2-end-market reclassification with restated comparatives. **AMI acquisition disclosed as a subsequent event** (full terms deferred to Q2). "No material changes" to FY2025 risk factors.

### LSCC Q1 FY2026 earnings call (Tier 2; May 4, 2026; Quartr)
Speakers: Ford Tamer (CEO), Lorenzo Flores (CFO), Rick Muscha (IR); AMI CEO Sanjoy Maity joined for the acquisition. Demand framing centered on **AI servers, data center, networking, industrial automation, and "emerging physical AI"** — *not* defense; "early innings of a multi-year growth cycle." CEO/CFO tone confident but measured (led with results + leverage) → **CEO-combativeness monitoring unchanged at 2.** **Report cross-check:** the Tier-3 anchor report's "LSCC Q1 2026 $170.9M / 64% Greater China / server FPGA +85% YoY" are all CONFIRMED against the primary (server reads as Compute & Comms +86%) — no A6 (g') variance.

## Open questions

1. **AMI close + content.** Does AMI close (~Q3 2026) on terms, and does the secure-boot/firmware/BMC platform add any defense/secure-government angle, or is it purely AI-server system-control? Full terms in the Q2 10-Q.
2. **Defense/aerospace quantification.** Will LSCC ever break out defense/aerospace revenue, or does it stay folded into Industrial & Embedded? Until it does, the defense connection stays capability-not-revenue.
3. **China-revenue trajectory + tariff/export-control exposure.** Does the 64% Greater China concentration keep rising, and how exposed is LSCC to the June-2027 additional Section 301 tariff + any export-control escalation?
4. **Secure-FPGA defense conversion.** Does the secure-control-FPGA capability (root-of-trust, post-quantum) convert into *material* defense design-wins/revenue — or remain a broad-market security feature?
5. **Taiwan-fab dependence.** The deeper chokepoint (per the Defense thesis) is TSMC fabrication; how does LSCC's foundry concentration evolve under geopolitical stress?
6. **Refresh.** Q2 FY2026 (quarter ending ~July 4 2026) + the AMI close are the next refresh triggers (AMI terms + first post-deal view).

## Change log

- **2026-06-05 (Session 134 — cross-ref):** Added a cross-ref to [[MRCY]] (Mercury Systems, now a vault page) — the *trusted-domestic counterpart* at the secure-microelectronics node: LSCC is the China-exposed (64% Greater China) / TSMC-fab secure-FPGA designer; MRCY is the onshore-DMEA-trusted secure-processing integrator. The two poles of the same node. No content change.

- **2026-06-04 (Session 133 — cross-ref):** Added to the new vault-wide [[china-exposure]] theme as a **cross-thesis node** — the standout 64%-Greater-China-revenue name *and* TSMC-fab-dependent (a "trusted-defense" name that is majority-China-revenue). No content change.

- **2026-06-04 (Session 128 — cross-ref):** Added a cross-ref to [[defense-drone-supply-chain]] (LSCC is the upstream secure-microelectronics node; the TSMC-fab dependence is the cross-thesis seam). No content change.

- **2026-06-03 (Session 125 — first-canonical ingest; first dual-thesis-from-creation page; evidence-led):** Created LSCC.md from FY2025 10-K + Q1 FY2026 10-Q + Q1 FY2026 call. **`layer 3`** (AI-datacenter specialized designer) + **`defense_tier 4`** (secure-microelectronics chokepoint capability, honest-verdict-qualified) + **AI `*_tier` fields OMITTED** — first Layer-N page with no AI `*_tier` (server-control/compute-adjacent role maps to none of the vault's per-domain tiers). **Evidence-led dual-thesis framing (Vic decision):** leads with the dominant AI-datacenter/hyperscaler lens (Compute & Comms +86% on data-center AI), with a dedicated honest **defense section** — secure-FPGA capability is a real chokepoint (MachXO5D-NX root-of-trust, CNSA 2.0 PQC, Sentry) but defense revenue is **thin/unquantified**, drones are **inferable-only (zero disclosure)**, and the US-defense-budget connection is **thesis-structural, not company-disclosed.** **Honest-verdict centerpiece: 64% Greater China revenue + Taiwan-fab (TSMC/Samsung/UMC) dependence** cut against the "trusted domestic supply chain" framing. Financials verified off the statements (FY2025 net income $3.1M / EPS $0.02 — trough year; Q1 FY2026 rev $170.9M +42% / net income $21.8M / EPS $0.16 — inflection). **AMI acquisition** ($1.65B; AI-server system-control firmware/BIOS/BMC; ~Q3 close) documented as a forward event reinforcing the AI-datacenter lens. **Section 2.11 N/A** (Saturday-nearest-Dec-31 week-scope). End-market reclassification (3→2) documented. **Second intra-defense supply-chain link:** [[AVAV]] consumes secure microelectronics; LSCC is the secure-FPGA supplier (reciprocal cross-ref). Report cross-check confirmed (64% China, server +86%) — no (g') variance. NOT a refresh (no refresh_log). Q2 FY2026 + AMI close pre-registered as refresh triggers.
