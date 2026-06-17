# The AI-Datacenter PCB & Interconnect-Substrate Chokepoint: Where the Durable Value Actually Sits

## TL;DR
- **The durable value sits UPSTREAM of the board, not in the board itself.** Board fabrication (Layer 1) is a real but competitive moat; the copper-clad laminate / glass-cloth material chain (Layer 2) and the ABF IC-substrate oligopoly (Layer 3) are the physics-and-yield-grade chokepoints. The single hardest, most monopolized node in the entire stack is **Ajinomoto Build-up Film (ABF) plus low-Dk/low-CTE glass cloth (Nittobo)** — both near-sole-source, both gated by chemistry and capacity that cannot be added on a quarters-scale timeline.
- **Verdict: "quality-but-competitive" for the BOARD; "durable/physics-grade" for the MATERIAL and SUBSTRATE.** The popular activist/broker claim that WUS supplies "~45% of NVIDIA's network-switch PCBs" is **NOT verifiable in WUS's own HKEX prospectus**, which instead reports a 12.5% global share of switch/router PCBs and 25.3% of 22-layer-plus PCBs (CIC data, 18 months to June 30, 2025). The board layer has a long, fast-climbing substitution tail (Victory Giant, Shennan, TTM, GCE); the laminate/glass/ABF layers do not.
- **For a 2–3 year horizon, the binding constraints are materials, not boards:** glass cloth (Nittobo), ABF (Ajinomoto), HVLP copper foil (Mitsui/Resonac) and qualified M8/M9 CCL (EMC, Doosan, Shengyi). NVIDIA is already reaching *past* its PCB and CCL suppliers to lock up glass cloth and copper foil directly — the clearest market signal of where the real scarcity is.

---

## Key Findings

1. **The "45% of NVIDIA switch PCBs / #1 in 22+ layer" claim is partially true and partially unverifiable.** WUS's HKEX Application Proof (filed Nov 28, 2025) confirms, citing third-party consultant CIC for the 18 months ended June 30, 2025: #1 globally in data-center PCBs (10.3%), #1 in 22-layer-and-above PCBs (25.3%), #1 in switch/router PCBs (12.5%). There is **no "45% of NVIDIA's switch PCBs" figure anywhere in the primary document** — that number traces to broker/independent-research decks, not a filing.

2. **Board fabrication is fragmenting upward, not consolidating.** Per Prismark/CMBI, the top-40 PCB makers hold only ~50% of the market and WUS itself is ~3% of global PCB. Competitors are climbing the layer-count curve fast: Victory Giant's AI/HPC PCB share leapt from 1.7% (2024) to 13.8% (H1 2025).

3. **CCL is structurally more concentrated than board fab** — top-10 suppliers = 77% of the market (Prismark) — but it is NOT a monopoly, and per-generation qualification gates reshuffle share violently (EMC reportedly failed GB300 compute-tray qualification; Doosan captured the GB300 compute-tray and is positioned for Rubin).

4. **The true single-source chokepoints are one layer deeper than CCL:** Ajinomoto's ABF film (>95% share, two Japanese plants) and Nittobo's T-glass/low-Dk glass cloth (~90% T-glass share). NVIDIA, Apple, AMD, Google and Amazon are physically queuing for this material.

5. **ABF substrate fabrication is a stable five-firm oligopoly** (Ibiden, Shinko, Unimicron, AT&S, Nan Ya) where the leader (Ibiden) is pulling away on yield, and where difficulty is *compounding into economics* — Ibiden's electronics operating margin rose from 13.6% (FY2024) to 18.6% (FY2025), guided toward 22.7% by FY2027.

6. **Buyer-defense behavior is concentrated upstream.** NVIDIA's 10-K discloses prepaid manufacturing and capacity agreements and tens of billions in long-term supply/capacity commitments — but the evidence of *buyers paying to defend specific suppliers* is strongest for glass cloth, copper foil and ABF, weakest for board fabricators. WUS's own prospectus shows trivial customer advance payments (RMB ~29–53m against RMB 8–13bn revenue), i.e., normal purchase orders, not capacity reservations.

---

## Details

### LAYER 1 — High-layer-count PCB fabrication

**What the primary source actually says (WUS HKEX Application Proof, Nov 28, 2025).** WUS Printed Circuit (Kunshan) — the Shenzhen-listed entity 002463, now filing for a Hong Kong H-share listing with CICC and HSBC as joint sponsors — makes the following CIC-attributed claims for the 18 months ended June 30, 2025:
- #1 globally in data-center PCBs: **10.3%** share
- #1 globally in **22-layer-and-above PCBs: 25.3%** share
- #1 globally in switches/routers PCBs: **12.5%** share
- #1 in high-end HDI for L2+ autonomous-driving domain controllers: **15.2%**

The company reports proven capability for a **108-layer PCB**, mass production of 44-layer "N+N" and 54-layer "N+M" boards, and that it supplies "all five of the world's largest publicly listed AI computing infrastructure companies" (CIC). Revenue grew 57.2% in H1 2025; AI servers & HPC revenue went from RMB 433.7m (5.2% of revenue, FY2022) to RMB 2,975.3m (22.3%, FY2024). Gross margin expanded from 27.9% (FY2022) to 32.3% (H1 2025).

**Verification of the "~45% of NVIDIA switch PCBs" claim.** This specific figure is **not in the prospectus, the A-share filings I reviewed, or any primary source.** It appears in independent research/broker commentary (e.g., Citi called WUS "the first and largest beneficiary" of NVIDIA's inference racks; independent supply-chain researcher GlobalTechResearch maps WUS as the ~60% primary supplier of the redesigned GB200 NVSwitch tray PCB with TTM at ~40%). **I flag "45%" as an unverified claim.** What IS primary-source-verifiable is the 12.5% all-customer global switch/router PCB share and 25.3% 22L+ share.

**Customer concentration & buyer-defense (primary source).** WUS's prospectus shows its largest customer fell from 16.9% (FY2022) to 12.4% (H1 2025) of revenue, and top-5 customers rose from 46.0% to 51.2%. Crucially, **customer contract liabilities (advance payments) were only RMB 34.7m / 22.6m / 28.9m / 52.9m** across the period — trivial against RMB 8–13bn revenue. The prospectus explicitly warns it "cannot assure… future orders or long-term business relationships." **Conclusion: board buyers transact via normal (if sticky, qualification-gated) purchase orders, not equity stakes, prepayments or capacity reservations.**

**The substitution tail is real and closing fast.**
- **Victory Giant (300476 SZ; HK-listed April 2026):** AI/HPC PCB share 1.7% (2024) → 13.8% (H1 2025); HDI revenue +388% in 2025; gross margin 22.7% → 35.2%. Core Google TPU v6/v7 supplier with 30-layer HDI. 2025 revenue ~RMB 19.3bn (+79.8%), net profit +273.5%.
- **Shennan Circuits (002916 SZ), Unimicron (3037 TT), Nan Ya PCB (8046 TT), Gold Circuit Electronics (2368 TT), TTM (TTMI US):** all credible high-layer-count makers. TTM closed FY2025 with record $2.91bn revenue; data-center + networking reached 36% of Q4 revenue, data-center segment +57% YoY, backed by a $1.61bn (mostly A&D) backlog.

**Is the moat a yield-learning curve or commoditizing?** Both. High-layer-count (>40L), tight-registration, hybrid-material boards still impose a genuine yield-learning gate (WUS's 108L capability and "N+N/N+M" lamination are non-trivial). But the gate is being climbed by at least 5–6 credible firms within 1–2 generations, the market is fragmented (~50% in top 40), and HDI margins, while elevated now (~35–39%), are the kind that historically compress. **Layer 1 = quality-but-competitive moat.**

### LAYER 2 — Ultra-low-loss CCL (M8/M9) and the glass-cloth chain beneath it

**Concentration.** Per Prismark (via CMBI, Nov 2025), the top-10 CCL suppliers hold **77%** of the market; the top-4 (Kingboard, Shengyi, EMC, Nan Ya Plastics) ~50%. EMC is the high-speed sub-segment leader (~22% share per CMBI) and grew >50% in 2024. This is materially more concentrated than board fab.

**The material spec gate is real and per-generation.** FR-4 dissipation factor (Df) ≈ 0.02; Panasonic Megtron 8 ≈ 0.0015 (vs. Megtron 7 ≈ 0.002, ~25% lower loss); M9-class for 224G runs below 0.002 — an order of magnitude better than FR-4. M8 is the 2026 mainstream, M9 ramps 2026–27. Qualified M8/M9 suppliers: **EMC (2383 TT), TUC (6274 TT), ITEQ (6213 TT), Doosan (Korea), Panasonic (Japan), Shengyi (600183 SS).**

**Generational lockout in action — the EMC/Doosan reshuffle.** Per DIGITIMES (Nov 21, 2025): "Doosan Electronic Business Group… is on track to become the exclusive supplier of copper-clad laminate (CCL) for Nvidia's next-generation AI chip, Rubin, following Taiwan competitor Elite Material Co. (EMC)'s failure to pass quality certification for the Nvidia Blackwell GB300 compute tray." Korean-press/independent estimates put Doosan's NVIDIA-related revenue at ~KRW 660bn (2025E) rising to ~KRW 1.15tn (2026E), with CCL plants running at 125–130% utilization. **Caveat:** Goldman Sachs channel checks (Sept 2025) argue the EMC downside is limited and that EMC, which held ~70% of the GB300 *switch* tray, could recover to ~100% of the M9 switch-tray in Rubin. The EMC↔Doosan split is genuinely fluid and spec-finalization-dependent (CCL specs expected to be finalized around June–July 2026). This volatility is itself evidence of a hard, per-generation qualification gate.

**Is CCL the deeper bottleneck? Partly — but the REAL bottleneck is one more layer down.** Multiple sources converge: the binding constraint is **upstream glass cloth and copper foil, not CCL fabrication.**
- **Glass cloth:** Nittobo (Nitto Boseki, 3110 JP) holds ~90% of T-glass and ~60–70% of NER-glass. Per TrendForce/industry reporting, "severe supply-demand imbalance has pushed the price of top-tier T-Glass to a historic $80–$100 per kilogram." Per TrendForce, "Nittobo raised prices across its glass fiber product line by 20% in August 2025, and plans another increase of roughly 20%-30% in April 2026"; it announced (Aug 2025) a plan to triple T-glass capacity via a >¥50bn investment over 2026–2027, but meaningful relief of supply constraints is unlikely before mid-2027. (The original 20% hike was announced June 2, 2025, effective Aug 1, 2025, per DIGITIMES.) NVIDIA CEO Jensen Huang personally visited Nittobo in early 2026 to discuss high-end electronic-cloth supply, and Apple intervened to coordinate capacity allocation, per industry reporting — Nittobo's cloth is "a key material for the PCBs of AI chips from companies like NVIDIA, AMD, Google, and Amazon." Second sources are emerging but sub-scale: per a Nittobo press release (Nov 28, 2025, via TrendForce), "Nan Ya Plastics states that by 2027, it will be responsible for weaving 20% of the specialty glass-fiber fabrics that Nittobo supplies to the global market"; Taiwan Glass and Asahi Kasei's Q-glass are also being qualified.
- **Copper foil:** HVLP4 foil capacity roughly halves with each grade upgrade; Resonac reportedly holds >90% of CCL core material used in ABF substrates and announced a 30%+ price hike (March 2026).

**The decisive buyer-defense signal.** Per industry reports, **NVIDIA and its major customers bypassed CCL makers to contract directly with HVLP4 copper-foil and T-glass suppliers, securing capacity >1 year in advance via a consignment model**, while CCL suppliers imposed an unusual quota-allocation system on PCB/substrate makers (CCL lead times hit ~6 months by early 2026). This is buyers paying to defend the *material* node — and it tells you exactly where the scarcity binds. **Layer 2 = durable at the material/glass/foil level; competitive-but-gated at the CCL-fabrication level.**

### LAYER 3 — ABF IC substrate

**The ABF film monopoly (hardest node in the stack).** Per Nikkei (via TrendForce, Apr 1, 2025), Ajinomoto (2802 JP) "holds more than 95% of the global market share for ABF materials used in GPU and CPU substrates" (some industry sources cite ~98%), produced in just two Japanese plants (Gunma and Kawasaki); sole minor competitor Sekisui Chemical (~5%). Ajinomoto "plans to invest at least JPY 25 billion (approximately USD 166 million) by 2030 to boost… ABF capacity by 50%" — capacity growing ~7%/yr against AI-substrate demand compounding far faster (Morgan Stanley ~16% CAGR 2025–27; Goldman ~33% 2025–28). This is the single most asymmetric node: the cheapest monopoly gating the most capital-intensive oligopoly beneath it.

**FCBGA substrate fabrication is a stable five-firm oligopoly.** Approximate shares: Ibiden ~35%, Shinko ~18%, Unimicron ~14%, AT&S ~10%, Nan Ya ~5% (with the five collectively ~60–74% depending on source; none exceeding ~18% on the tighter estimate). ABF-substrate ASPs rose from ~$65 (2024) to ~$82 (2025), +26%; lead times of 20–28 weeks (down from 40+ weeks at the 2022–24 peak) still indicate demand outrunning committed buildout.

**Difficulty is compounding into economics (Ibiden, primary source).** Per Ibiden's FY2025 results (May 12, 2026): electronics operating margin rose 13.6% (FY2024) → 18.6% (FY2025, on ¥243.3bn sales / ¥45.2bn OP), **guided to 22.7% in FY3/27 (¥330.0bn sales / ¥75.0bn OP)**. Ibiden raised its FY2027 group operating-profit target from ¥90bn to ¥150bn and set a new FY2031 vision of ≥¥1trn revenue and ≥¥300bn OP (~30% margin); capex is guided at ~¥100bn/yr FY2025–27, with SAP capacity for AI/ASIC substrates guided to **more than double** by end-FY2027 vs. end-1H FY2024. Management told Goldman the binding constraint "is headcount and engineering talent, not capital," and attributed the new Ono Plant's advantage to "not so much… productivity but… yield." Rising customer advance payments are the leading indicator that buyers are funding capacity.

**Buyer-defense & demand-ramp.** Substrate availability has been one of the most visible AI back-end bottlenecks; building a new substrate fab takes 2–3 years and hundreds of millions in capex. Customers fund expansion via advance payments; multi-year hyperscaler contracts reportedly include dual-source clauses capping annual price increases (~3%). **Layer 3 = durable/physics-and-yield-grade, with ABF film the single hardest sub-node.**

---

## Durability Scorecard (six-question framework)

**Scoring key:** ✅ = strengthens durability; ⚠️ = mixed; ❌ = weakens durability.

| # | Question | Layer 1: Board fab | Layer 2: CCL + glass/foil | Layer 3: ABF substrate |
|---|---|---|---|---|
| 1 | **Buyer-defense** (equity/prepay/LTA/reservation)? | ❌ Normal POs; WUS contract liabilities trivial (RMB ~53m) | ✅ NVIDIA directly reserves glass cloth & HVLP foil >1yr ahead; CCL quota allocation | ✅ Customer advance payments fund Ibiden capacity; hyperscaler LTAs |
| 2 | **Supply-response** (<2yr weak / 3+yr strong) | ⚠️ New high-layer lines ~12–24 mo + qualification | ✅ Glass-cloth capacity 2027+; CCL qual per generation | ✅ New substrate fab 2–3 yr; ABF +50% takes to 2030 |
| 3 | **Generational lockout** (hard gate vs continuous)? | ⚠️ Yield-learning gate, but climbable | ✅ Hard per-gen requalification (EMC GB300 failure proves it) | ✅ Each layer/die-size step narrows qualified field |
| 4 | **Substitution tail** (how many credible rivals)? | ❌ Long tail: WUS, VGT, Shennan, Unimicron, TTM, GCE, Nan Ya | ⚠️ CCL: ~6 qualified; glass: Nittobo near-monopoly | ✅ Only ~5 substrate firms; ABF effectively 1 (Ajinomoto) |
| 5 | **Demand-ramp** (on the binding path)? | ✅ Yes, but not the binding scarcity | ✅ Glass/foil/CCL is the binding scarcity in 2026 | ✅ Substrate gates accelerator packaging |
| 6 | **Geology/policy overlay** | ⚠️ China-heavy (tariff/export risk) | ✅ Japan glass/foil adds durability; ✅ China laggard in M9 | ✅ Japan ABF concentration = durability + single-point geopolitical risk |
| | **Net durability** | **Quality-but-competitive** | **Durable at material level** | **Durable / physics-and-yield-grade** |

---

## Cyclicality: is AI different, or a spike in disguise?

PCB and CCL are historically brutal cyclical industries. Per Prismark/CMBI: global PCB fell ~15% in 2023 (inventory destock), recovered +5.8% in 2024, and is estimated +12.8% in 2025. The 2017–18 episode is the cautionary template: a copper-foil and CCL price spike (driven by capacity tightness and copper) drew in capacity and corrected sharply into 2018–19, punishing laggard fabricators. The structural difference *this* cycle: (1) a genuine per-generation material spec gate (M7→M8→M9) that commoditized FR-4 players cannot follow; (2) value migration from board to material — CCL grew 18% vs PCB 6% in 2024, with high-speed specialty CCL +50%; and (3) copper-led cost inflation (LME +~24% in 2025) that *advantages* CCL leaders with pricing power while squeezing commodity PCB makers. **Net read: the high-end AI segment is structurally stronger than prior cycles, but the names with the least durability (commodity board fabricators) remain cyclical, and a Rubin spec delay or an AI-capex air-pocket would still hit the whole chain. The materials/substrate layers would be the last to crack.**

## China vs. Taiwan vs. Japan/Korea concentration & geopolitics

- **Board fab:** China-heavy (China ≈ 50–56% of global PCB value). Tariff/export-control exposure is highest here; WUS derives 75–83% of revenue from overseas customers and has built a Thai base partly to de-risk.
- **CCL:** split Taiwan (EMC, TUC, ITEQ) / China (Shengyi, Kingboard) / Korea (Doosan) / Japan (Panasonic). Chinese makers lag specifically in qualified M9.
- **Glass cloth & ABF:** Japan-concentrated (Nittobo, Ajinomoto) — this *adds* durability (hard to replicate, US-aligned) but creates a single-geography single-point risk.

## Investability & access (Interactive Brokers)

**Directly accessible on IBKR (US, Japan, Taiwan, Korea, Hong Kong):**
- **US:** TTM Technologies (TTMI), Amphenol (APH), AT&S (Vienna/OTC).
- **Japan:** Ibiden (4062), Shinko (6967 — note pending take-private by a JIC-led consortium), Resonac (4004), Ajinomoto (2802), Nittobo (3110), Panasonic (6752).
- **Taiwan:** EMC (2383), TUC (6274), ITEQ (6213), Unimicron (3037), Nan Ya PCB (8046), Nan Ya Plastics (1303), GCE (2368), WUS Printed Circuit Taiwan parent (2316).
- **Korea:** Doosan (000150).
- **Hong Kong:** Kingboard Laminates (1888), Victory Giant (HK line, listed April 2026), and the **pending WUS Kunshan H-share listing** (joint sponsors CICC/HSBC).

**Access-constrained:** **China A-shares — Shengyi (600183 SS), WUS Kunshan (002463 SZ), Shennan (002916 SZ), Victory Giant A-line (300476 SZ), Shengyi Electronics (688183 SH)** — are generally NOT directly tradable by retail via IBKR (no Stock Connect retail access). The pending WUS Kunshan H-share and the existing Victory Giant HK line are the workarounds to access those names. The Taiwan WUS parent (2316 TT) offers indirect, heavily NAV-discounted look-through exposure to WUS Kunshan (the basis of the Palliser 4.3%-stake and Metrica 1.5%-stake activist campaigns, which cite a ~70–80% discount to NAV).

---

## Recommendations (staged, neutral framing — no buy/sell calls)

1. **Anchor the thesis upstream.** If the goal is exposure to the most durable chokepoint, weight toward the **material/substrate layer** (Ajinomoto, Nittobo, Ibiden, Resonac, EMC/Doosan) over pure board fabricators. The board layer is the most investable in headline terms but the least durable.
2. **Treat the WUS "45%" narrative as marketing until a filing confirms it.** Use the prospectus figures (12.5% switch/router, 25.3% 22L+) as the verified base case. Re-rate only if the final WUS Kunshan prospectus or an audited filing discloses a named NVIDIA-specific share.
3. **Watch three hard thresholds that would change the ranking:**
   - **Rubin CCL spec finalization (June–July 2026):** if EMC regains M9 switch-tray share, the EMC-loss narrative reverses; if Doosan's exclusivity holds, Korean CCL durability is confirmed.
   - **Nittobo capacity online (mid/late 2027):** glass-cloth easing would compress the single most acute 2026 bottleneck and de-rate the glass premium.
   - **Ajinomoto and Ibiden customer-advance-payment trajectory:** rising = capacity still buyer-funded (durable); stalling = reversion to the old cyclical classification.
4. **For China A-share names, use HK-listed proxies** (Victory Giant HK; pending WUS Kunshan H-share; Kingboard) given IBKR access constraints.
5. **Cyclicality hedge:** size positions for the possibility that an AI-capex air-pocket or Rubin delay hits commodity board fabricators first and hardest; materials/substrate names would be the last to crack and the first to re-tighten.

---

## What I Could NOT Verify Against a Primary Source (and how it affects the verdict)

1. **The "WUS supplies ~45% of NVIDIA's network-switch PCBs" claim** — not in the HKEX Application Proof or A-share filings; sourced to broker/independent research. *Affects:* weakens the "WUS = irreplaceable switch-PCB monopoly" sub-thesis; the verified 12.5% switch share is consistent with a strong-but-not-dominant position.
2. **The anonymized customer identities in WUS's prospectus** ("all five of the world's largest publicly listed AI computing infrastructure companies") — NVIDIA is not named; the Business section (pp. 150–223) was not machine-retrievable. *Affects:* customer-dependency analysis relies on the verified concentration ratios (largest 12.4%, top-5 51.2%), which is solid; the specific NVIDIA share is inferential.
3. **Doosan's KRW 660bn→1.15tn NVIDIA revenue and 125–130% plant utilization** — from Korean press / independent threads, not Doosan's audited filings. *Affects:* directionally corroborated by DIGITIMES on the GB300 exclusivity, but the precise figures are unverified.
4. **EMC's GB300 qualification "failure"** — reported by DIGITIMES (secondary trade press), contradicted in part by Goldman channel checks; neither is an EMC primary disclosure. *Affects:* the EMC/Doosan split is genuinely uncertain; I treat it as fluid rather than settled.
5. **ABF ASPs (~$65→$82), substrate lead times (20–28 weeks), and FCBGA market shares** — from independent research/market-research aggregators, not company filings (Ajinomoto's >95% share and Ibiden's margin trajectory ARE primary-source-verified). *Affects:* the qualitative oligopoly/monopoly structure is robust; precise share splits are approximate.
6. **The "NVIDIA bypassing CCL makers to lock glass cloth/foil directly via consignment"** — reported by trade press citing "media reports"; logical and corroborated by Nittobo price action and Jensen Huang's reported Nittobo visit, but not in an NVIDIA filing. NVIDIA's 10-K *does* confirm prepaid manufacturing/capacity agreements in general terms.

**Net effect on verdict:** None of the unverified items overturns the core conclusion. They cluster around *which specific company* wins a given socket (Layer 1 and Layer 2 fabrication), which is exactly where durability is weakest. The durable-chokepoint conclusion — ABF film (Ajinomoto), glass cloth (Nittobo), and the substrate/CCL yield oligopolies — rests on the best-verified facts (Ajinomoto >95%, Ibiden's audited margin trajectory, Prismark CCL concentration, the WUS prospectus, and NVIDIA's 10-K commitments).

---

### Explicit overall verdict
- **The AI-datacenter PCB/interconnect chokepoint is a "split-grade" chokepoint, and the durable value does NOT sit in the board.**
- **BOARD (Layer 1) = "quality-but-competitive":** a real qualification/yield moat with a credible, fast-closing substitution tail and meaningful cyclical exposure. WUS is a genuine leader but not a monopoly; the headline "45%" figure is unverified.
- **LAMINATE (Layer 2) = durable at the material level, competitive at the fabrication level:** the durable value is in **glass cloth (Nittobo) and HVLP copper foil (Mitsui/Resonac)**, not in CCL coating per se, where ~6 firms qualify and per-generation share swings are violent.
- **SUBSTRATE (Layer 3) = "durable / physics-and-yield-grade":** the **ABF film monopoly (Ajinomoto, >95%)** is the single hardest node in the entire stack, followed by the Ibiden-led FCBGA yield oligopoly.
- **Bottom line:** the most durable, hardest-to-replicate value concentrates in the **Japanese materials monopolies (Ajinomoto ABF, Nittobo glass) and the substrate/CCL yield leaders (Ibiden, EMC/Doosan)** — i.e., upstream of, and beneath, the board.