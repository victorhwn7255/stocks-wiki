---
type: chokepoint
tickers: [NVDA, AVGO, MKSI, NOVT, ONTO]
related_themes: [AI-demand-durability, hyperscaler-custom-ASIC]
last_updated: 2026-06-17
---

# AI-datacenter PCB / interconnect-substrate chokepoint

***PROVISIONAL** chokepoint page (Pathway 1 per CLAUDE.md Section 3.15). Anchored on a single Tier-3 source — the vault deep-research report `raw/research/ai-datacenter-PCB-interconnect-substrate-research.md` (which itself verified its load-bearing claims against primary sources: WUS Kunshan's HKEX application proof, Ibiden's audited FY2025 results, Ajinomoto/Nittobo data, and the NVDA/AVGO 10-Ks). **No supplier here is a vault company page yet**, so every supplier is named plain-text with its ticker, not wikilinked (wikilink-clean discipline). Figures are Tier-3 unless tagged primary — verify before treating as load-bearing. Provisional because the supplier side has zero vault primary-source pages; promotion to canonical is pre-registered below (first supplier ingest — likely Ibiden). Describe-don't-recommend: this maps structural position, not a trade. The trigger was a Palliser activist deck on WUS, treated as a Tier-3/4 claim to test.*

## The chokepoint — and the one thing that matters

AI accelerator trays and network-switch line cards are built on advanced printed circuit boards (PCBs) and IC substrates. As switch radix and SerDes speed climb (102.4T switches, 224G SerDes), boards need more layers (22+, up to ~108) and lower-loss dielectric material; accelerator packages need ever-larger ABF substrates. That makes this a real, fast-growing demand pocket — but the central finding inverts the popular "own the board-maker" framing:

**The durable value is not in the board. It migrates upstream — to the dielectric material and the IC substrate.** This is the vault's chokepoint-quality gradient applied to PCB (physics/geology > precision-manufacturing > integration), and the same "value sits one layer up" move the vault makes elsewhere: GOES steel over the transformer ([[transformer-supply]]), InP over the laser ([[InP-supply]]), separation/refining over the magnet ([[rare-earth-magnet-chokepoint]]). It is also a clean instance of stacked-bottleneck migration (frameworks Theme 11.12): the AI constraint keeps moving down the stack, and the interconnect-material layer is a node the market has only recently begun to name.

The single best evidence for where the scarcity binds: **NVIDIA is reaching *past* its board and laminate suppliers to lock the underlying glass cloth and copper foil directly** (detailed below) — buyers paying to defend the *material* node, not the board.

## Three tiers (durability rises as you go down)

### Layer 1 — High-layer PCB fabrication (the board) — *quality-but-competitive*

The board fabricators are real, top-bin operators with a genuine yield-learning curve at high layer counts — but a long, fast-closing substitution tail.

- **WUS Kunshan** (Shenzhen 002463; H-share listing pending, sponsors CICC/HSBC). Per its HKEX application proof (filed Nov 28, 2025; CIC data, 18 months to June 30, 2025; primary-in-anchor): **#1 in data-center PCBs at 10.3%**, **#1 in 22-layer-and-above at 25.3%**, **#1 in switch/router PCBs at 12.5%**, #1 in high-end HDI for L2+ ADAS at 15.2%. Proven 108-layer capability; mass production of 44-layer "N+N" and 54-layer "N+M" boards; supplies "all five of the world's largest publicly listed AI-computing-infrastructure companies." Revenue +57.2% in H1 2025; AI-servers/HPC mix RMB 433.7m / 5.2% (FY2022) → RMB 2,975.3m / 22.3% (FY2024); gross margin 27.9% → 32.3%.
- **The "~45% of NVIDIA's switch PCBs" claim is NOT in any primary source** (the WUS prospectus, A-share filings) — it traces to broker/independent research (Citi; an independent supply-chain map puts WUS at ~60% of the GB200 NVSwitch-tray PCB with TTM ~40%). **Quarantined as Tier-3, unverified.** The primary-verified figure is the 12.5% all-customer switch/router share — strong #1, *not* a monopoly.
- **The tail is real and closing fast.** The top-40 PCB makers hold only ~50% of the market; WUS is ~3% of global PCB (Prismark/CMBI; Tier 3). Victory Giant (Shenzhen 300476; HK line listed April 2026) saw its AI/HPC PCB share leap from 1.7% (2024) to 13.8% (H1 2025), HDI revenue +388% in 2025, gross margin 22.7%→35.2%, as a core Google-TPU-v6/v7 board supplier. Shennan Circuits (002916), Unimicron (3037 TT), Nan Ya PCB (8046 TT), Gold Circuit / GCE (2368 TT), and TTM (TTMI; FY2025 record $2.91bn revenue, data-center/networking 36% of Q4) are all credible high-layer makers. Yield-learning gate, yes — but climbable by 5-6 firms within 1-2 generations.

### Layer 2 — Low-loss CCL and the chain beneath it — *durable at the material level, competitive at fabrication*

Copper-clad laminate (CCL) is the dielectric+copper sheet the board is built from. The fabrication step is more concentrated than the board (top-10 CCL suppliers ~77%; top-4 — Kingboard, Shengyi, EMC, Nan Ya Plastics — ~50%; Prismark/CMBI Nov 2025, Tier 3), but ~6 firms qualify at the high-speed grade (EMC 2383 TT, Doosan 000150 KS, Shengyi 600183, TUC 6274 TT, ITEQ 6213 TT, Panasonic 6752 JP), and per-generation share swings violently.

- **The material spec gate is real and per-generation.** FR-4 dissipation factor (Df) ≈ 0.02; Megtron-8-class ≈ 0.0015 (~25% lower loss than M7); M9-class for 224G runs below 0.002 — an order of magnitude better than FR-4. M8 is 2026 mainstream; M9 ramps 2026-27.
- **The EMC↔Doosan reshuffle shows the gate biting.** Per DIGITIMES (Nov 21, 2025; Tier-3 trade press), Doosan is on track to be the exclusive CCL supplier for NVIDIA's Rubin after EMC reportedly failed GB300 compute-tray qualification. **But Goldman channel checks (Sept 2025) argue EMC's downside is limited and it could recover ~100% of the M9 *switch*-tray in Rubin.** CCL specs finalize ~June-July 2026. The EMC "failure" and Doosan's reported KRW 660bn→1.15tn NVIDIA revenue / 125-130% utilization are **quarantined as Tier-3, contested/unverified** — but the *volatility itself* is evidence of a hard, per-generation qualification gate.
- **The binding node is one layer deeper — glass cloth and copper foil.** Multiple sources converge that the real 2026 scarcity is upstream of CCL fabrication:
  - **Glass cloth: Nittobo (3110 JP) holds ~90% of T-glass** (~60-70% of NER-glass). Top-tier T-glass reportedly $80-100/kg (TrendForce); Nittobo raised glass-fiber prices ~20% (Aug 2025) with another ~20-30% planned (Apr 2026), and is tripling T-glass capacity via a >¥50bn investment — but meaningful relief is unlikely before mid-2027. NVIDIA's CEO reportedly visited Nittobo in early 2026 and Apple intervened to coordinate allocation. Second sources are emerging but sub-scale (Nan Ya Plastics to weave ~20% of Nittobo's specialty cloth by 2027; Taiwan Glass and Asahi Kasei Q-glass being qualified).
  - **HVLP copper foil:** capacity roughly halves with each grade upgrade; Resonac (4004 JP) reportedly holds >90% of the CCL core material used in ABF substrates and announced a 30%+ price hike (March 2026). Mitsui is the other key HVLP source.

### Layer 3 — ABF IC substrate — *physics-and-yield-grade durable*

The package substrate directly under the die (distinct from the board). This is the hardest tier.

- **ABF film is the single most monopolized node in the entire stack: Ajinomoto (2802 JP) holds >95% (some sources ~98%) of ABF build-up film, made in just two Japanese plants** (Gunma, Kawasaki); the only minor competitor is Sekisui (~5%) (Nikkei via TrendForce, Apr 2025; Tier 3). Ajinomoto plans ≥¥25bn (~$166m) by 2030 to lift ABF capacity ~50% — roughly 7%/yr against AI-substrate demand compounding far faster (Morgan Stanley ~16% / Goldman ~33% CAGR). The cheapest monopoly in the stack gates the most capital-intensive oligopoly beneath it.
- **FCBGA substrate fabrication is a stable five-firm oligopoly:** Ibiden (4062 JP) ~35%, Shinko (6967 JP) ~18%, Unimicron ~14%, AT&S ~10%, Nan Ya ~5%. **Difficulty is compounding into economics** — per Ibiden's audited FY2025 results (May 12, 2026; primary-in-anchor), electronics operating margin rose from 13.6% (FY2024) to 18.6% (FY2025) and is **guided to 22.7% by FY3/27**; the group FY2027 operating-profit target was raised ¥90bn→¥150bn, with a FY2031 vision of ≥¥1trn revenue / ≥¥300bn OP. Management told Goldman the binding constraint is "headcount and engineering talent, not capital," and attributed its new-plant edge to yield. (ABF-substrate ASP ~$65→$82 / +26% and 20-28-week lead times are Tier-3 market-research figures — directionally corroborative, quarantined as approximate. Shinko is in a pending JIC-led take-private.)

### Shared bottleneck with HBM — Ibiden's dual substrate role

The substrate tier links this chokepoint to [[HBM-oligopoly]] through a single shared node: **Ibiden makes both the ABF logic substrate under AI accelerators/ASICs *and* the substrate that carries HBM into the package** — and the whole FCBGA oligopoly draws on the same Ajinomoto ABF film. A Vera Rubin-class system therefore pulls on the *same* substrate capacity twice: once for the HBM stack ([[HBM-oligopoly]] scope) and once for the logic die (this page's scope). That makes it a **capacity-allocation tension, not two independent constraints** — if Ibiden / Ajinomoto capacity is the binding limit, memory-side and logic-side substrate demand compete for the same node. The mix tilts memory-heavy in 2026-27 (HBM4 ramp) and logic-heavy into 2028+ (custom-ASIC + GPU package growth), so the watch item is whether Ibiden's expansion (SAP capacity guided to >double by end-FY2027; Ibiden FY2025 results, primary-in-anchor) closes *both* gaps or forces a prioritization. The durable tier of this chokepoint and the durable tier of [[HBM-oligopoly]] are therefore not separable — they share the same physics/yield-grade node. (Cross-ref the [[HBM-oligopoly]] "NOT covered here" scope-boundary bullet.)

### Equipment & chemistry-tier enablers (vault-adjacent)

Three vault company pages sit one step off the stack — the tools and chemistry the board/substrate makers buy. They are *enablers, not chokepoint owners* (the same role ONTO/COHU/AEHR play at [[HBM-oligopoly]]):
- **[[MKSI]]** (chemistry-tier) — its Materials Solutions Division is *"one of the market leaders in the chemistry needed to bond layers to each other"* (plus the plating chemistry that lays the copper lines), with AI-related advanced-PCB-manufacturing chemistry growing ~+22-27% YoY (MKSI Q1 2026 call; Tier 2). The bonding/plating-chemistry layer beneath board + substrate fabrication — yield-critical, and MKSI's highest-margin division (~54% GM).
- **[[NOVT]]** (board-fab equipment) — its Westwind air-bearing spindles (~300k RPM) drill the *"thick (~40-layer) AI-GPU boards"*, where management claims *"the number 1, by far"* (NOVT Q1 2026 call; Tier 2). The drilling tool gating high-layer board fabrication (Layer 1).
- **[[ONTO]]** (metrology-tier) — advanced-packaging metrology + inspection (Dragonfly / JetStep / Firefly), explicitly across the emerging **panel-level substrate** format (up to 650mm); ~50% of revenue from advanced packaging + a $240M+ HBM metrology VPA (ONTO Q4 FY2025 call; Tier 1/2). Substrate-agnostic, but structurally tied to the substrate ramp.

Honest framing: these are enablers the board/substrate makers depend on, not the durable chokepoint owners — included for completeness (the chokepoint economics still concentrate in Ajinomoto / Nittobo / Ibiden, per the scorecard).

## Durability scorecard (the six-question test, per layer)

Reproduced from the deep-research anchor, which scored each layer with cited evidence. ✅ strengthens durability / ⚠️ mixed / ❌ weakens.

| # | Question | Layer 1: Board | Layer 2: CCL + glass/foil | Layer 3: ABF substrate |
|---|---|---|---|---|
| 1 | Buyer-defense (equity/prepay/LTA)? | ❌ normal POs; WUS advance payments trivial | ✅ NVIDIA reserves glass cloth + HVLP foil >1yr ahead | ✅ customer advance payments fund Ibiden capacity |
| 2 | Supply-response (<2yr weak / 3+ strong) | ⚠️ new high-layer line ~12-24mo + qual | ✅ glass capacity 2027+; CCL requal per-gen | ✅ new fab 2-3yr; ABF +50% only by 2030 |
| 3 | Generational lockout | ⚠️ yield gate, climbable | ✅ hard per-gen requal (the EMC/Doosan swing) | ✅ each layer/die-size step narrows the field |
| 4 | Substitution tail | ❌ long (WUS, VGT, Shennan, Unimicron, TTM, GCE, Nan Ya) | ⚠️ CCL ~6 qualified; glass near-monopoly | ✅ ~5 substrate firms; ABF effectively 1 (Ajinomoto) |
| 5 | Demand-ramp (on the binding path?) | ✅ yes, but not the binding scarcity | ✅ glass/foil/CCL is the 2026 binding scarcity | ✅ substrate gates accelerator packaging |
| 6 | Geology/policy overlay | ⚠️ China-heavy (tariff/export risk) | ✅ Japan glass/foil; China lags in M9 | ✅ Japan concentration = durability + single-point risk |
| | **Net** | **quality-but-competitive** | **durable at the material level** | **durable / physics-and-yield-grade** |

## Buyer-defense signal — follow NVIDIA's checkbook

The clearest market tell sits in Q1 of the scorecard. Per industry reports (Tier-3, corroborated by Nittobo's price action and the reported Jensen Huang Nittobo visit, but not in an NVIDIA filing — quarantined as to the specific mechanic), **NVIDIA and major customers bypassed the CCL makers to contract directly with HVLP4 copper-foil and T-glass suppliers, securing capacity over a year in advance via a consignment model**, while CCL suppliers imposed quota allocation on the board/substrate makers (CCL lead times hit ~6 months by early 2026). NVIDIA's 10-K confirms prepaid manufacturing and capacity agreements in general terms (primary). This is the same equity-/commitment-defense pattern the vault tracks at the optics layer ([[nvidia-supply-chain-commitments]]: LITE/COHR/GLW), but one tier deeper — and it fires at the *material* node, not the board. [[AVGO]]'s own disclosure that supply is "fully secured 2026-2028" including "substrates and T-glass" (AVGO Q1 FY2026 call; primary) is the demand-side echo. See [[NVDA]] / [[AVGO]].

## Cyclicality + geopolitics

- **Cyclicality is intact.** PCB/CCL are historically brutal cycles (global PCB −15% in 2023, +5.8% 2024, est. +12.8% 2025; Prismark/CMBI). The 2017-18 copper-foil/CCL spike-then-bust is the cautionary template. What is structurally different this cycle: a genuine per-generation material spec gate (M7→M8→M9) that commodity FR-4 players cannot follow, and value migrating from board to material (CCL +18% vs PCB +6% in 2024; high-speed CCL +50%). Net: the high-end AI segment is structurally stronger than prior cycles, but the **board fabricators stay cyclical**, and a Rubin spec delay or AI-capex air-pocket would hit them first; the material/substrate layers would be last to crack.
- **Geography is bifurcated** ([[china-exposure]]): board fabrication is **China-heavy** (China ≈ 50-56% of global PCB value; highest tariff/export-control exposure — WUS derives 75-83% of revenue overseas and built a Thai base to de-risk), while the durable nodes — glass cloth (Nittobo) and ABF film (Ajinomoto) — are **Japan-concentrated**, which adds durability (hard to replicate, US-aligned) but creates a single-geography single-point risk.

## Investability / access lens

Per the vault's access lens (Vic reaches US, foreign-listed, and China A-share/HK names), the durable nodes are directly reachable:
- **Directly accessible (IBKR):** Japan — Ibiden (4062), Ajinomoto (2802), Nittobo (3110), Resonac (4004), Shinko (6967; pending take-private), Panasonic (6752). Taiwan — EMC (2383), TUC (6274), ITEQ (6213), Unimicron (3037), Nan Ya PCB (8046), GCE (2368), WUS Taiwan (2316). Korea — Doosan (000150). US — TTM (TTMI), Amphenol (APH), AT&S. Hong Kong — Kingboard Laminates (1888), Victory Giant (HK line, April 2026).
- **Access-gated China A-shares** (no clean retail Stock-Connect route): Shengyi (600183), WUS Kunshan (002463), Shennan (002916), Victory Giant A-line (300476). The workarounds are the HK proxies — the **pending WUS Kunshan H-share** and **Victory Giant's HK line**.
- **WUS Taiwan (2316 TT)** is a heavily NAV-discounted look-through to WUS Kunshan (the basis of the Palliser ~4.3% and Metrica ~1.5% activist stakes; reported ~70-80% discount to NAV) — a structure/discount bet on the board layer, not on the durable material/substrate nodes. Describe-don't-recommend.

## What would confirm or weaken this framing

Pre-registered tests (Pathway 1 convention):
- **Rubin CCL spec finalization (~June-July 2026):** if EMC regains M9 switch-tray share, the "EMC lost it" narrative reverses; if Doosan's exclusivity holds, Korean CCL durability is confirmed. Resolves the most contested Layer-2 claim.
- **Nittobo capacity online (mid/late 2027):** glass-cloth easing would compress the single most acute 2026 bottleneck and de-rate the glass premium — testing whether Layer 2's durability is structural or a one-cycle squeeze.
- **Ajinomoto + Ibiden customer-advance-payment trajectory:** rising = capacity still buyer-funded (durable); stalling = reversion to the old cyclical PCB classification.
- **WUS Kunshan final prospectus / audited filing:** if it discloses a named NVIDIA-specific share, re-test the quarantined "45%" against primary. Until then the verified base case is 12.5% switch/router, 25.3% 22L+.
- **AI-capex air-pocket / Rubin delay:** would hit commodity board fabricators first and hardest (Layer 1), with material/substrate (Layers 2-3) last to crack — testing the cyclicality verdict.
- **PROMOTION TRIGGER (provisional → canonical):** the first vault supplier company page — most likely an **Ibiden** ingest (the cleanest durable-node primary-source filer; already named in `_thesis.md` Rank 5 Materials). A supplier-side primary page would lift this from a single-Tier-3-anchor provisional to a multi-source canonical chokepoint, the rare-earth-magnet precedent.

## Honest verdict

**A split-grade chokepoint — and the durable value does NOT sit in the board.**
- **Board (Layer 1) = quality-but-competitive:** a real yield/qualification moat with a credible, fast-closing substitution tail and full cyclical exposure. WUS is a genuine leader, not a monopoly; the headline "45%" is unverified.
- **Laminate (Layer 2) = durable at the material level, competitive at fabrication:** the durable value is in glass cloth (Nittobo) and HVLP copper foil (Resonac/Mitsui), not in CCL coating, where ~6 firms qualify and per-generation share swings are violent.
- **Substrate (Layer 3) = physics-and-yield-grade durable:** the ABF film monopoly (Ajinomoto >95%) is the hardest node in the stack, followed by the Ibiden-led FCBGA yield oligopoly.
- **Bottom line:** the most durable, hardest-to-replicate value concentrates in the **Japanese material monopolies (Ajinomoto ABF, Nittobo glass) and the substrate/CCL yield leaders (Ibiden, EMC/Doosan)** — upstream of, and beneath, the board the activist deck points at.

## Cross-references

- [[HBM-oligopoly]] — the adjacent substrate tier; Ibiden is the shared node (HBM base substrate there, ABF logic substrate here). This page partially addresses HBM-oligopoly's flagged future "HBM-substrate-supply" candidate — see the scope-boundary note there.
- [[MLCC-oligopoly]] — sibling Tier-3-anchored component-oligopoly page; another Japanese-materials "new memory" node and a stacked-bottleneck-migration instance (Theme 11.12).
- [[hyperscaler-custom-ASIC]] — every custom ASIC (and Victory Giant's Google-TPU boards) gates on ABF substrate + high-layer PCB; the demand side of this chokepoint.
- [[NVDA]] / [[AVGO]] — the buyer-defense anchors (NVDA prepaid-manufacturing/capacity; AVGO "substrates + T-glass secured 2026-2028").
- [[nvidia-supply-chain-commitments]] — the architect-defends-supply pattern this extends one tier deeper, into materials.
- [[china-exposure]] — the bifurcated China-board / Japan-material geography.
- [[AI-demand-durability]] — the demand source funding the whole stack.
- [[MKSI]] / [[NOVT]] / [[ONTO]] — vault-adjacent equipment & chemistry-tier enablers (bonding/plating chemistry / high-layer board drilling / advanced-packaging + panel-substrate metrology); the tools-and-chemistry layer the board/substrate makers buy.

## Change log

- **2026-06-17 (same-session connection-deepening):** Added (a) the "Shared bottleneck with HBM — Ibiden's dual substrate role" subsection (the ABF film + Ibiden FCBGA capacity-allocation tension that makes this chokepoint's durable tier inseparable from [[HBM-oligopoly]]'s) and (b) an "Equipment & chemistry-tier enablers" subsection naming the three vault-adjacent pages — [[MKSI]] (bonding/plating chemistry), [[NOVT]] (high-layer-board drilling spindles), [[ONTO]] (advanced-packaging + panel-substrate metrology). Added MKSI/NOVT/ONTO to frontmatter `tickers` (vault-adjacent enabler provenance) + Cross-references. Reciprocal back-links added on the three company pages + a PCB/substrate cohort note added to [[china-exposure]]. From the cross-vault connection sweep; `last_updated` unchanged (same creation day).
- **2026-06-17 (creation; PROVISIONAL):** Created Pathway 1 provisional from the Tier-3 deep-research anchor `raw/research/ai-datacenter-PCB-interconnect-substrate-research.md` (Vic-approved plan). First vault coverage of the PCB / interconnect-material / IC-substrate layer. Three-tier structure (board / CCL+glass+foil / ABF substrate); six-question durability scorecard; honest verdict = split-grade, durable value upstream of the board (Ajinomoto ABF + Nittobo glass + Ibiden substrate). Killed the activist deck's "WUS ~45% of NVIDIA switch PCBs" headline against the WUS HKEX prospectus (verified: 12.5% switch/router, 25.3% 22L+); quarantined the EMC-failure, Doosan-revenue, ABF-ASP, and NVIDIA-consignment claims as Tier-3/unverified. Suppliers plain-text (no vault pages; wikilink-clean). Promotion trigger pre-registered (Ibiden ingest). NOT a primary ingest (no refresh_log; Section 4.6 streak untouched). Inbound cross-refs added at HBM-oligopoly / MLCC-oligopoly / hyperscaler-custom-ASIC.
