# Is the high-layer-count / high-speed PCB + CCL supply chain for AI servers an investable chokepoint, and who owns it?

**Tier-3 discovery anchor — value-chain map & market-share angle.** Saved 2026-06-18. Discovery-only; nothing here is citable as vault fact until verified at primary sources. Web-search-sourced (Tier 3 independent analysis + Tier 4 news); figures are analyst/trade-press estimates unless a primary filing is named. Use to seed an ingest verify-list, not to assert canon.

---

## 1. One-paragraph verdict

The AI-server board stack is a **layered chokepoint that gets harder the further upstream you go**, not a single owner. The board itself (PCB fabrication) is high-growth but **competitive and fast-closing** — share is reshuffling rapidly (e.g., Victory Giant from ~1.7% to ~13.8% of AI/HPC PCB revenue in roughly a year per trade press). The durable value migrates **upstream into the materials**: low-loss copper-clad laminate (CCL) grades (M8/M9/M10), and beneath that the **specialty inputs** — fine-weave T-glass fabric (Nittobo), HVLP copper foil (Mitsui Kinzoku, Co-Tech), and — for the substrate-like / advanced-packaging tier — ABF film (Ajinomoto ~97% per trade press). This matches the chokepoint-quality gradient: physics/material-grade + qualification lock-in > precision fabrication > integration/assembly. The strongest "who owns it" answers are at the material-grade nodes, not the board.

---

## 2. The value chain (downstream → upstream)

```
GPU package (ABF substrate)  ← advanced-packaging substrate tier (Ajinomoto ABF film, Ibiden/Unimicron/Kinsus/Nan Ya PCB FCBGA)
        |
OAM accelerator module HDI PCB  ← per-GPU high-density board (Unimicron lead-named)
        |
Universal Baseboard (UBB)  ← carries 2–8 OAM modules (Hushi/Kingdee/Tripod named)
        |
Switch / line-card boards  ← 800G/1.6T networking boards (M9/M10 grades; WUS, Iteq substrates)
        |
=== built from ===
High-speed/low-loss CCL  ← M8 / M9 / M10 grades (EMC/Elite, TUC, Shengyi, Iteq, Panasonic, Doosan)
        |
Specialty material inputs:
   - Low-Dk fine-weave glass fabric / T-glass  ← Nittobo (>50% per trade press)
   - HVLP copper foil  ← Mitsui Kinzoku (~60% HVLP2+, ~98% ultra-thin pkg foil), Co-Tech (~10.3%)
   - Low-Dk/low-Df resin systems
```

**Layer-count escalation is the demand driver.** AI-server layer counts reportedly jumped from 16–20 to 28–36 layers; AI servers' share of total PCB demand rose from ~15% (2025) to >25% (2026) per Digitimes/trade press. Higher layer count + higher signaling speed (448G/1.6T) pushes both CCL grade and material purity, narrowing the qualified supplier set at each upgrade.

---

## 3. Market shares & leaders by tier (Tier-3/4 estimates — VERIFY)

### Tier A — CCL (copper-clad laminate), the highest-conviction node
- **Global CCL market**: ~US$16.0B (2025) → ~US$21.5B (2026F) per trade press; HPC-CCL TAM ~$3.89B (2025) → ~$9.98B (2027F), ~60% 2-yr CAGR.
- **Taiwan firms ~37.4% of global CCL (2025)**; **Elite Material (EMC) ~18.9% — world's largest single share** per trade press.
- **TUC (Taiwan Union Technology) + Iteq ~18% combined** in high-frequency/high-speed CCL.
- **Grade mix is the alpha**: M8 reportedly ~$1.59B (41%) 2025 → ~$6.49B (65%) 2027F (~102% 2-yr CAGR); M9 ramps 2026 (~$240M, 4%) → ~$770M (8%) 2027F.
- **Qualification race**: EMC's M9-grade reportedly passed NVIDIA certification (potential mass production ~Q2, claimed share up to ~70% — promotional, VERIFY); Iteq M9 certified by a "major US AI company," Thailand plant on 800G switch substrates. M9Q in development across EMC, TUC, Doosan, Iteq, Panasonic, Shengyi.

### Tier B — PCB fabrication (the board), high-growth but competitive
- **Unimicron**: ~18–22% global AI-server PCB share; >50% in certain ASIC substrates (trade press).
- **Victory Giant (VGT)**: ~1.7% → ~13.8% of global AI/HPC PCB revenue in ~1 year; direct NVIDIA supplier — illustrates how fast share moves (the "fast-closing tail").
- **Other Taiwan fabs**: WUS Printed Circuit, Zhen Ding, Compeq, Gold Circuit Electronics.
- **Other China fabs**: Shennan Circuits, Suntak.
- **OAM/UBB split**: per-GPU OAM HDI lead-named to Unimicron; UBB named to Hushi/Kingdee/Tripod.
- **NVIDIA reaching down**: WUS named as NVIDIA's lead test partner for M10 CCL / 448G+ (HVLP5 foil + Q-glass) per Ming-Chi Kuo (Mar 2026) — signal that the buyer is co-qualifying the board+material, not just buying boards.

### Tier C — substrate-like / advanced-packaging materials, the hardest nodes
- **ABF film: Ajinomoto ~97.1%** of ABF build-up film (trade press) — single-supplier-grade chokepoint for AI chip packaging.
- **FCBGA / ABF substrate fab**: Unimicron, Kinsus, Nan Ya PCB reported "sold out"; Ibiden-led oligopoly (cross-ref vault [[pcb-interconnect-substrate-chokepoint]]).
- **T-glass fabric: Nittobo >50%** of fine-weave low-Dk glass; fully booked through 2026; new entrants (Taiwan Glass) hit yield delays → est. supply gap >40% (2026).
- **HVLP copper foil: Mitsui Kinzoku ~60% of HVLP2+, ~98% of ultra-thin package foil**; each grade upgrade reportedly halves available capacity; Co-Tech ~10.3% (top-3). NVIDIA stepped in directly to secure HVLP4 amid ~1,500-ton projected 2026 shortfall (trade press).

---

## 4. Where is the moat vs. commoditization?

| Node | Moat source | Durability read | Commoditization risk |
|---|---|---|---|
| Board fab (PCB) | Yield, layer-count capability, customer qualification, capex/capacity | **Medium — fast-closing** (VGT 1.7%→13.8%); competitive | High at lagging grades; share reshuffles per generation |
| CCL (M8/M9/M10) | Per-generation NVIDIA/ASIC qualification + material formulation + grade ramp | **Medium-high** — qualification lock-in per generation, margin expansion for M8/M9 producers | Erodes as grade matures; the *next* grade resets the race |
| T-glass fabric | Fine-weave physics, yield, single-leader capacity | **High** — Nittobo >50%, entrants stuck on yield | Low near-term; capacity is the gate |
| HVLP copper foil | Process purity; capacity halves per grade upgrade | **High** — Mitsui Kinzoku concentration; NVIDIA securing directly | Low at leading grade |
| ABF film | Formulation IP + near-monopoly | **Highest** — Ajinomoto ~97% | Very low |

**Pattern:** the moat is strongest where physics + qualification + concentration overlap (T-glass, HVLP foil, ABF). The board is where competition is fiercest. The CCL grade race is the contested middle — real margin expansion for whoever holds the current NVIDIA-qualified grade, but the moat resets each generation.

---

## 5. Investability & access notes (discovery-only)
- Highest-conviction owners are **Japan/Taiwan-listed** (Nittobo, Mitsui Kinzoku, Ajinomoto JP; EMC/TUC/Iteq/Unimicron/Gold Circuit/WUS TW). China fabs (Shennan, Victory Giant, Suntak) sit at the more-competitive board tier and on A-shares.
- The buyer-reaching-upstream signal (NVIDIA directly securing HVLP4 / co-qualifying M10) is a **Framework-12 buyer-defense** marker firing at the *material* node — consistent with vault [[nvidia-supply-chain-commitments]].

## 6. Primary-source verify-list (for a future ingest)
1. EMC ~18.9% / Taiwan ~37.4% CCL share — confirm in EMC, TUC, Iteq filings/IR.
2. "EMC M9 ~70% NVIDIA share" — promotional; verify against EMC disclosures.
3. Ajinomoto ~97% ABF, Mitsui Kinzoku ~60%/~98% foil, Nittobo >50% T-glass — confirm in each company's annual report/segment data.
4. Unimicron 18–22% AI PCB + >50% ASIC substrate — confirm Unimicron filings.
5. Victory Giant 1.7%→13.8% AI/HPC revenue share — confirm VGT (002463) filings.
6. CCL/HPC TAM and M8/M9 grade-mix figures — analyst TAM models (Nomura), not primary; treat as directional.
7. WUS as NVIDIA M10 lead test partner (Kuo, Mar 2026) — Tier-3 analyst claim; verify at WUS IR / NVIDIA disclosures.

---

## 7. Named-leader financials, capacity & capex (angle: ground the investability call)

This section adds the financial / capacity / capex signature behind the named leaders — the real-world test of whether the chokepoint is showing up in the numbers (surging AI-mix revenue, margin expansion, repeated price hikes, sold-out advanced capacity, large capex). All Tier 3/4/5 — `[verify: …]` at primary.

### CCL — material-grade layer (hardest moat)

**Elite Material / EMC (2383 TT)**
- Core M8 competitive group with TUC, Iteq, Doosan, Panasonic. EMC M8 share in **Google TPU applications rose ~20% → ~30%** (Tier 3). `[verify: customer concentration / segment]`
- **Capacity roadmap: targeting 9.45 million CCL sheets/month by 2027** (Digitimes 2026-03-30); 2025 expansions completed at Huangshi + Zhongshan (China) + Penang (Malaysia). `[verify: EMC IR capacity table]`
- **Pricing power: EMC + TUC each announced ~10% high-end price increases** for AI servers/switches starting Q2. `[verify: announcement / ASP]`

**Taiwan Union Technology / TUC (6274 TT)**
- **TTM revenue ~US$973M** as of 2025-12-31; **2024 sales ~NT$23.07B** (Tier 4 aggregators). `[verify: TUC annual report]`
- **Capacity >2.2M sheets/month laminate + 1.6M sq ft/month mass lamination.** `[verify: TUC IR]`
- Named (with EMC, Unimicron) as an **AWS Trainium 3 PCB/CCL supplier seeing a sharp revenue jump** (Tier 5 — broker-check via X; lead only). `[verify: revenue-trend proxy; customer % unverifiable]`

**Shengyi Technology (600183 SH) / Shengyi Electronics**
- **Shengyi Electronics ~+343.76% YoY growth** on high-end mix + capacity ramp (Tier 3/4). `[verify: Shengyi annual segment]`
- **RMB 5.2B high-performance CCL project** to deepen upstream high-end material capability. `[verify: SZSE capex disclosure]`

### High-layer-count / high-speed PCB (mid-hard moat)

**Shennan Circuits (002916 SZ)**
- **2025 revenue RMB 23.647B (+32.05% YoY); net profit RMB 3.276B (+74.47% YoY)** (Tier 4 earnings summary). PCB segment **RMB 14.359B (+36.84% YoY), gross margin ~35.53%.** Dividend RMB 24 / 10 shares. `[verify: SZSE 2025 annual report]`
- **Capex: Nantong Phase IV** (high-speed/high-density AI-server + switch PCB) + **RMB 4.6B Wuxi multilayer project**, trial production H2 2026. `[verify: capex filings]`

**WUS Printed Circuit (002463 SZ)**
- **Data-comms PCB revenue +71% YoY to RMB 6.53B in H1 2025**; targets **HPC >40% of total revenue by 2026.** `[verify: interim report / IR]`
- Major supplier of **52-layer PCBs for NVIDIA ultra-low-latency cabinets.** `[verify: HKEX application proof — note vault S166 KILLED an over-stated "WUS ~45% of NVIDIA switch PCBs" claim; verified ~10.3% DC PCB / ~12.5% switch = strong #1, not monopoly]`
- **Capex: new PCB project ~RMB 5.5B total, three phases.** `[verify: WUS IR]`

**Gold Circuit Electronics / GCE (2368 TT)**
- Among networking/server PCB makers posting **double-digit YoY growth** as IC-substrate orders spread downstream (Tier 3). `[verify: GCE monthly revenue / annual report]`

### ABF / advanced substrate (hardest-moat adjacent — overlaps [[pcb-interconnect-substrate-chokepoint]])

**Unimicron (3037 TT)**
- **H1 2025 revenue NT$62.556B (+15.25% YoY)**; June 2025 NT$10.929B (+23.2% YoY). **AI projected ~half of 2026 revenue.** `[verify: Unimicron monthly/quarterly + guidance]`
- Converted 2 Taiwan + 1 China fabs to AI-specific OAM, all profitable. Sell-side: **~35% ABF share for NVIDIA high-end GPUs, >50% for ASICs** (Google TPU, AWS Trainium); ABF a persistent structural bottleneck with pricing power (Tier 3 BofA/MS). `[verify: vs Ibiden/Nan Ya/Kinsus]`

### Read on the financials
The numbers corroborate the layered-chokepoint thesis: the **CCL + substrate tier shows margin expansion, price increases, and sold-out advanced capacity** (qualification-gated), while the **board-fab tier shows fast top-line growth but the share volatility of a more competitive layer** (VGT, Shennan, WUS all growing 30–70%+ but share reshuffling). Trade press also flags a **>RMB 80B / ~20-company high-end capacity wave landing in 2–3 years** — the main glut risk, and it hits the board tier before the material tier.

---

## Sources
- Digitimes — Elite Material 9.45M sheets/month by 2027, 2026-03-30: https://www.digitimes.com/news/a20260330PD241/elite-material-emc-capacity-ccl-2027.html
- Digitimes — AI surge / PCB material shortages, EMC + Co-Tech, 2025-10-27: https://www.digitimes.com/news/a20251027PD204/pcb-ccl-demand-co-tech-elite-material.html
- Digitimes — AI server tracker (PCB/CCL/interconnect demand), 2026-03-13: https://www.digitimes.com/news/a20260313VL219/demand-ai-server-ccl-pcb-revenue.html
- Digitimes — AI server supply chain tracker (PCB/CCL lead, ASIC/testing diverge), 2026-02-12: https://www.digitimes.com/news/a20260212VL212/ai-server-supply-chain-pcb-ccl-asic-2026.html
- Digitimes — AI server PCB demand fuels CCL material supply battle, 2025-10-22: https://www.digitimes.com/news/a20251022PD234/ai-server-pcb-ccl-demand-nvidia.html
- Digitimes — ABF substrate sells out for Unimicron, Kinsus, Nan Ya PCB, 2026-04-20: https://www.digitimes.com/news/a20260420PD216/revenue-pcb-abf-substrate-unimicron-ai-chip.html
- Digitimes — Taiwanese firms secure M9-grade CCL certifications, 2025-08-15: https://www.digitimes.com/news/a20250815PD206/ccl-asic-capacity-production-market.html
- Digitimes — Nvidia takes PCB material competition upstream (HVLP4 gap), 2026-06-11: https://www.digitimes.com/news/a20260611PD218/pcb-copper-foil-demand-high-end-infrastructure.html
- Digitimes — Taiwan PCB capex; Unimicron/Zhen Ding SEA, 2025-09-01: https://www.digitimes.com/news/a20250901PD220/pcb-capex-supply-chain-taiwan-unimicron-zhen-ding.html
- Digitimes — IC substrates & networking PCBs grow; material shortages, 2026-01-02: https://www.digitimes.com/news/a20260102PD223/ic-substrate-pcb-equipment-supply-chain-taiwan.html
- Digitimes — Unimicron bets on AI boom, substrate demand, 2025-06-18: https://www.digitimes.com/news/a20250618PD230/unimicron-demand-substrate-ic-high-end.html
- Digitimes — WUS targets >40% AI HPC revenue by 2026, 2025-12-12: https://www.digitimes.com/news/a20251212PD213/wus-pcb-revenue-hpc-2026.html
- Futunn — Shennan Circuits 2025 net profit +74%: https://news.futunn.com/en/post/69988384/riding-the-wave-of-ai-computing-power-shennan-circuits-2025
- Futunn — 20 firms / >RMB 80B PCB capacity, glut risk: https://news.futunn.com/en/post/74359632/twenty-companies-have-expanded-production-within-the-year-with-investments
- Futunn — NVIDIA steps in to secure HVLP4 copper foil (~1,500-ton 2026 shortfall): https://news.futunn.com/en/post/74502051/ai-material-shortages-spread-nvidia-steps-in-directly-to-secure
- Bamboo Works — WUS Printed Circuit Hong Kong IPO: https://thebambooworks.com/wus-printed-circuit-hong-kongs-ipo/
- martini.ai — Taiwan Union Technology profile/financials: https://martini.ai/pages/research/Taiwan%20Union%20Technology-e6dfc0c1f8edd32e0063aa8e6241ce70
- Investing.com — Morgan Stanley upgrades Unimicron/NYPCB on ABF up-cycle: https://www.investing.com/news/stock-market-news/morgan-stanley-upgrades-unimicron-nypcb-on-ailed-abf-substrate-upcycle-4519224
- X (Tier 5, broker-summary) — AWS Trainium 3 PCB/CCL supplier revenue jump (EMC/TUC/Unimicron): https://x.com/QQ_Timmy/status/1996744929629163735
- UGPCB — AI Server PCB Revolution: High-Frequency Materials & Market Trends 2026: https://www.ugpcb.com/news/trade-news/ai-server-pcb/
- UGPCB — PCB Raw Material Prices Surge Up to 40%: https://www.ugpcb.com/news/trade-news/pcb-raw-material-prices-surge-up/
- TrendForce — What Is Glass Fiber Fabric / T-Glass for AI Servers, 2025-11-24: https://www.trendforce.com/news/2025/11/24/news-what-is-glass-fiber-fabric-and-why-is-t-glass-critical-for-ai-servers-a-deep-dive/
- Taiwan News — Taiwan's CCL makers track growing AI needs, 2025-11-07: https://www.taiwannews.com.tw/news/6238704
- I-Connect007 — AI Demand Drives PCB Material Market Growth: https://iconnect007.com/article/149934/ai-demand-drives-pcb-material-market-growth/149931/aep
- iamfabian (Substack) — The AI Supercycle and the Global PCB & EMS Market 2025: https://iamfabian.substack.com/p/the-ai-supercycle-and-the-global
- Creating Nanotech — One server is worth seven (Gold Circuit / Unimicron growth): https://www.creating-nanotech.com/en-US/newsc244-one-server-is-worth-seven-ai-server-upgrades-boost-pcb-production-with-golden-image-electronics-and-unimicron-enjoying-significant-growth
- abhay (Substack) — The Board Beneath the Chip: AI's Next Bottleneck: https://abhayterminal.substack.com/p/the-board-beneath-the-chip

---

## Angle: Materials moat & qualification — where switching costs actually live

*Added 2026-06-18 (materials-moat & qualification angle). Tier-3/4 web-sourced; verify at primary. Complements the value-chain/market-share and financials sections above.*

### The M-grade cost ladder = the moat mechanism
Each grade step changes resin chemistry, copper-foil profile AND glass-cloth grade *simultaneously*, so cost **multiplies, not adds** ([hilelectronic](https://hilelectronic.com/ai-server-pcb-demand/), [UGPCB](https://www.ugpcb.com/news/trade-news/ai-server-pcb/)). Industry-estimate multipliers vs FR-4 (Tier-3, directional): M6 ~3–5×; M7 ~6–9×; M8 ~10–15×; M9 (Q-glass) ~15–20×; M10 highest, in qual.

| Grade | Loss class | Df | AI use |
|---|---|---|---|
| M4–M6 | LL/VLL | ~0.005–0.01 | prior-gen / inference / networking (commoditizing) |
| M7 | ULL | <0.005 | H100/A100-era AI |
| M8 | ULL | <0.005 | current mainstream AI, 224G lanes |
| M9 | ELL/SLL | lowest in volume | GB200/GB300, 800G/1.6T switches |
| M10 | next-gen | <~0.002 (448G+) | Rubin-era, in qualification |

**Non-fungible capacity:** standard FR-4 CCL lines *cannot* be redirected to M-grade — resin chemistry, glass spec, lamination, and qualification all differ ([hilelectronic](https://hilelectronic.com/ai-server-pcb-demand/)). That is the supply-side half of the chokepoint; the OEM qualification cycle is the demand-side half.

### The qualification cycle is the gatekeeper — and the buyer controls how wide it opens (★ key nuance)
This is the sharpest moat finding and the one the sibling sections underweight:
- **M9 = single qualified supplier (Elite Material / EMC).** Resin formulation is "core IP," "years of R&D + enormous investment" to pass NVIDIA/Google qual ([aminext](https://www.aminext.blog/en/post/ccl-for-ai-hardware-the-definitive-guide)). EMC M9 reportedly ~70% potential share ([Taiwan News](https://www.taiwannews.com.tw/news/6238704)) — a qualification-driven near-monopoly.
- **M10 = qualified across THREE suppliers by design** (EMC + Shengyi + Taiwan Union; WUS the lead PCB dev partner), *explicitly* to improve NVIDIA bargaining power + supply resilience vs M9 single-source ([ic-pcb](https://www.ic-pcb.com/next-gen-ccl-m10-enters-testing-for-nvidia-platforms-chinese-pcb-maker-wus-reportedly-involved.html); [Technetbook/Kuo](https://www.technetbooks.com/2026/03/nvidia-m10-ai-server-material-testing.html)).
- **Implication:** the CCL incumbent moat **resets and compresses each generation** — M9 monopoly → M10 engineered oligopoly. The qualification barrier is real but it is a *per-generation gate the buyer decides how many suppliers clear*. Mass production M10 ~H2 2027. This is the de-moating mechanism to watch, and it argues the *most durable* moat is NOT the resin maker but the node below it (glass cloth) where the buyer has no second source to qualify.

### Glass cloth = the narrowest, most durable node (qualification can't manufacture a second supplier overnight)
- **Nittobo ~90% T-glass, ~60–70% NER-glass** ([TrendForce](https://insights.trendforce.com/p/glass-fiber-cloth-shortage), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/glass-cloth-could-be-the-next-great-ai-shortage-as-major-manufacturers-scramble-to-secure-critical-material-japanese-manufacturer-courted-by-apple-nvidia-google-and-amazon)) — note this is HIGHER than the sibling section's ">50%" figure; the two estimates bracket the same near-monopoly read (verify at primary).
- **Pricing power proven:** +20% (Aug 2025), planned +20–30% (Apr 2026); propagates to BT substrate ~1 qtr later, ABF ~2 qtrs later ([TrendForce](https://insights.trendforce.com/p/glass-fiber-cloth-shortage)).
- **Capacity lag protects the moat:** 3× T-glass expansion (>¥50bn, Aug-2025 announced) online from late 2026, full impact 2028, "no meaningful relief before mid-2027" (~6-mo equipment-stabilization) ([Digitimes](https://www.digitimes.com/news/a20250901PD242/fiberglass-cloth-capacity-ai-server-packaging-production.html)).
- **Next-gen:** Q-glass/quartz (Shin-Etsu) + Nittobo NEZ-glass (2027) — extreme hardness/weave difficulty keeps the entrant set tiny.

### Qualification-moat verdict (materials angle)
Durable value ranks, hardest→softest, by *how hard the buyer can manufacture a second qualified source*: **glass cloth (Nittobo — can't) > ABF film (Ajinomoto — can't) > HVLP foil (Mitsui — barely) > CCL resin per-generation (EMC — buyer actively widening) > board fab (many, buyer spreading freely) > FR-4 (commodity).** The qualification cycle creates the switching cost, but it protects the *material chemistry/physics* nodes far more durably than the *board* — because at the board the buyer can and does qualify many suppliers, while at glass cloth there is physically no second ~90% supplier to qualify. The investable chokepoint is real, and it is the materials, not the board.

### Additional sources (materials/qualification angle)
- aminext — The Definitive Guide to CCLs for AI Hardware: https://www.aminext.blog/en/post/ccl-for-ai-hardware-the-definitive-guide
- TrendForce Insights — Glass Fiber Cloth: The Underlying Material Shortage: https://insights.trendforce.com/p/glass-fiber-cloth-shortage
- Tom's Hardware — Glass cloth could be the next great AI shortage: https://www.tomshardware.com/tech-industry/artificial-intelligence/glass-cloth-could-be-the-next-great-ai-shortage-as-major-manufacturers-scramble-to-secure-critical-material-japanese-manufacturer-courted-by-apple-nvidia-google-and-amazon
- TrendForce — Nittobo Plans 2028 Next-Gen T-Glass, 2026-02-04: https://www.trendforce.com/news/2026/02/04/news-nittobo-reportedly-plans-2028-next-gen-t-glass-customers-may-include-nvidia-apple-and-others/
- Digitimes — Nittobo to triple T-Glass capacity by 2027: https://www.digitimes.com/news/a20250901PD242/fiberglass-cloth-capacity-ai-server-packaging-production.html
- IC&PCB Union — Next-gen CCL M10 enters testing for NVIDIA, WUS involved: https://www.ic-pcb.com/next-gen-ccl-m10-enters-testing-for-nvidia-platforms-chinese-pcb-maker-wus-reportedly-involved.html
- Technetbook — Nvidia M10 AI Server Material Testing (Ming-Chi Kuo): https://www.technetbooks.com/2026/03/nvidia-m10-ai-server-material-testing.html
- hilelectronic — AI Server PCB Demand in 2026 (M-grade ladder + cost multipliers): https://hilelectronic.com/ai-server-pcb-demand/
