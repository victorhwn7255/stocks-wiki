# Pure-Play Power Semiconductors on the NVIDIA 800VDC / Kyber / Rubin Ultra Transition
**Institutional Equity Research Report — Delta Framework | May 25, 2026**

## TL;DR
- **Vicor (VICR)** is the highest-conviction pure-play exposure to NVIDIA's AI power transition today on the strength of contracted Gen-5 Vertical Power Delivery (VPD) production, a >2.0x book-to-bill, and a $300.6M one-year backlog — but its ~25–26x EV/Sales and ~$205M of trailing-three-month insider Code-S sales demand a staged entry. **Navitas (NVTS)** is the highest-beta pure-play, with a confirmed NVIDIA 800V partnership and singular GaN+SiC focus, but trades at ~83x EV/TTM revenue on only $8.6M Q1'26 revenue — a thematic call option, not a fundamental investment.
- **The 800VDC transition is real and bill-of-materials-expanding**, with NVIDIA's Kyber rack (Rubin Ultra, shipping 2027) framed by Schneider Electric at 1.0–1.2 MW per rack, replacing 54VDC distribution that would otherwise consume 64U of power shelves and ~200 kg of copper busbar per rack (NVIDIA Developer Blog). Per third-party diligence (TheDiligenceStack), power-semiconductor content per rack will rise ~4x from GB200 to Vera Rubin and ~11.5x to Rubin Ultra.
- **Avoid**: pure-SiC commodity exposure (Wolfspeed post-Chapter-11 — AI is still a "modest" share of mix) and diversified incumbents excluded per mandate. **Buy on weakness**: Vicor (top pick), Aixtron (foreign pure-play picks-and-shovels), Power Integrations (highest-quality GAAP earner with credible 800V optionality).

---

## Key Findings

### 1. The 800VDC architectural shift is locked in — not a thesis, a roadmap
- NVIDIA's Kyber rack (successor to Oberon) will house **576 Rubin Ultra GPUs** and is "the first system built natively for 800V DC" (Converge Digest; NVIDIA Developer Blog). NVIDIA explicitly notes that 54VDC distribution at MW-scale would require "up to 200 kg of copper busbar" per rack and "64 U of rack space" for power shelves alone, leaving "no room for compute" (NVIDIA Developer Blog, "NVIDIA 800 V HVDC Architecture Will Power the Next Generation of AI Factories").
- At OCP Global Summit (Oct 13–16, 2025), NVIDIA formally enrolled 14 silicon partners for 800VDC: ADI, AOS, EPC, Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, Rohm, STMicroelectronics, TI (Electronics Weekly). Hyperscaler/operator adopters: CoreWeave, Lambda, Nebius, Oracle Cloud, Together AI, and Foxconn (40 MW Kaohsiung-1) (NVIDIA Blog, "NVIDIA, Partners Drive Next-Gen Efficient Gigawatt AI Factories").
- GTC 2026 (San Jose, March 16, 2026): Jensen Huang confirmed Vera Rubin shipping 2026, Kyber/Rubin Ultra "expected to ship in 2027" (CNBC). NVIDIA + Schneider Electric framed Rubin Ultra Kyber racks at "1 MW to 1.2 MW" (Schneider Electric blog, May 8, 2026). Industry analyst Glenn Lockwood noted Kyber demos at GTC 2026 appeared less power-dense than the 2025 prototype — flagged as unresolved; NVIDIA did not formally restate Kyber power.
- Total data-center semiconductor TAM (compute, memory, networking, power — not AI-only) is projected by Yole Group to expand from $209B in 2024 to ~$492–493B by 2030 ("Data Center Semiconductor Trends 2025"). IDTechEx projects the broader power-electronics market (EVs + data centers + renewables) at US$65.2 billion by 2036, representing a 10% CAGR over the forecast period ("Power Electronics Market 2026–2036", April 2026). MarketsandMarkets places the narrower data-center semiconductor market at $265.8B by 2029 (25.1% CAGR).

### 2. GaN and SiC are complementary — players with both win
- **SiC**: dominates 650V–1700V+ for facility-level conversion (solid-state transformers/SSTs, 13.8kV AC → 800VDC), rack-level high-voltage DC bus, hot-swap, UPS.
- **GaN**: dominates final-stage high-frequency conversion near GPU (800V→50V→12V→6V→core), low- to mid-voltage Power Delivery Boards, DC-DC bricks.
- Per NAND Research: "vendors with both GaN and SiC portfolios, including Infineon and Navitas, have a broader addressable opportunity." That's why Navitas's GeneSiC acquisition (Aug 15, 2022; total consideration ~$270M = $100M cash + 24.9M NVTS shares + up to $25M earn-out, per Navitas press release) matters strategically.
- Wafer/supply dynamics (Jan 2026 commentary, FinancialContent): SiC is in oversupply correction (price wars from Chinese substrate manufacturers), while GaN supply is constrained and ASPs are firm. This favors GaN-heavy pure-plays in the near term and pressures pure-SiC suppliers (Wolfspeed).

### 3. Pure-play universe ranked: Vicor > Power Integrations > Aixtron > Navitas > Wolfspeed > EPC (private)
We exclude Monolithic Power Systems (MPWR) — Enterprise Data is now only **25.2% of FY2025 revenue, down from 32.5% in FY2024** per MPWR's Form 8-K — and we exclude Infineon, ON Semi, STMicro, TI per the user's pure-play mandate. (For reference, onsemi disclosed at its Q1 2026 call that "AI revenue was about $250 million last year" with FY2026 guidance to double that — meaningful, but still well under 10% of total revenue, fitting the diversified-incumbent exclusion.)

---

## Details — Company Deep Dives

### A. Vicor Corp (VICR) — TOP PICK (stage in)
- **Business**: Pure-play modular power conversion (DC-DC bricks, Factorized Power Architecture, Vertical Power Delivery for AI accelerators). Founded 1981; Andover, MA; CEO Patrizio Vinciarelli; 44.6M shares outstanding.
- **Q1 2026 results (Apr 21, 2026 release; SEC Form 10-Q)**: Revenue $112.97M (+20.2% YoY; product $98.0M + royalty $14.97M). One-year backlog **$300.6M (+70% QoQ)**, book-to-bill **>2.0**, gross margin **55.2%** (vs. 47.2% Q1'25), EPS $0.44 (beat $0.40). Q2 guide ~$126M; FY2026 guide ~$570M. Cash $404M; near-zero debt.
- **Lead customer**: CVP Phil Davies on the Q1 2026 call: "Our lead computing customer is continuing a steep production ramp of its wafer scale engine with best-in-class AI inference performance." Third-party analysts (Photoncap) infer this is Cerebras based on the wafer-scale-engine reference; Vicor has not confirmed. CEO Vinciarelli (Q3 2025 call): "Engagement is starting with selected customers comprising a hyperscaler and OEMs who informed us that Vicor's second-generation VPD is the only solution that can meet their processor requirements."
- **IP moat & royalty stream**: Q1 2026 royalty revenue $14.97M vs. $10.76M a year earlier (+39% YoY). ITC Limited Exclusion Order (2025) against competitors enabled a licensing wave. CFO Jim Schmidt: "OEMs and hyperscalers will become Vicor licensees." Second ITC case final determination expected 2027.
- **Capacity**: Second fab under construction; path to $1.5B revenue capacity.
- **Valuation**: Market cap ~$13.5B at current $300+ share level; EV/Sales ~25–26x trailing; P/E ~98–103x trailing; forward P/E 68–115x depending on source. **Insider activity is a clear yellow flag**: insider sales totaled ~$205.5M over the trailing three months per GuruFocus, including CEO/CFO/multiple directors selling between roughly $250–$270/share. All confirmed Code S open-market. CEO Vinciarelli sold 4,000 shares (~$1.09M) but still holds ~9.0M shares.
- **Recommendation**: Top conviction pure-play exposure for the 18–36 month VPD ramp. Initiate at one-third weight; add to full weight on pullbacks to <20x EV/Sales (≈$220 area). Bear case: if Cerebras concentration weakens or NVIDIA-direct competitors (Delta, Compal in-house solutions) gain share, multiple compresses sharply. Insider selling implies management does not see further immediate re-rating from current levels.

### B. Power Integrations (POWI) — HIGHEST-QUALITY PURE-PLAY
- **Business**: $443.5M FY2025 revenue (+6% YoY); diversified across appliances/EV/industrial/communications, but PowiGaN platform + collaboration with NVIDIA at 1250V and 1700V GaN positions it for 800V architectures. POWI is profitable, free-cash-flow positive, dividend-paying ($0.215 quarterly).
- **800V NVIDIA collaboration** (CEO Jennifer Lloyd, Q1 2026 call): "Our ongoing collaboration with NVIDIA includes a variety of sockets utilizing our 1,250 and 1,700-volt GaN technologies in the forthcoming 800-volt DC architectures. We continue to gain share in aux power supplies for today's data centers, winning 2 new designs in Q1 at Taiwan customers serving U.S. equipment makers." She also said higher-voltage opportunities are "a couple years out."
- **Quantification**: POWI does NOT yet break out a discrete data-center revenue $ figure. Forward SAM for combined rack + grid is ">$1 billion by 2030" (Q1 2026 call). PowiGaN revenue grew >40% in FY2025 (POWI 10-K/8-K). Renewables/battery storage/HVDC = ~40% of high-power Q1 2026 revenue.
- **Q1 2026 financials**: Revenue $108.3M; non-GAAP EPS $0.25; non-GAAP GM 53.5%; Q2 guide $115–120M revenue, GM 54–55%. CapEx 5–6% of revenue plan for 2026.
- **Valuation**: Market cap ~$3.95B; P/S ~8.9x; forward P/E ~59–71x; Morningstar fair value $68.29 vs. $70.85 (May 22, 2026) → ~3% premium (not stretched). Sell-side: Susquehanna PT $85 (May 8, 2026), Deutsche Bank PT $65 from $45 (May 8, 2026).
- **Insider activity**: Modest, ordinary-course Code-S — CEO Lloyd 3,322 shares Feb 9, 2026; Director Balakrishnan $532,053; VP Sales Gagan Jain 313 shares Apr 2, 2026.
- **Recommendation**: Strong Buy as the "quality compounder" in the basket. Accept that meaningful 800V revenue is "a couple years out" and benefit from EV, industrial, grid, and aux-power earnings power in the interim.

### C. Aixtron SE (FSE: AIXA / OTC: AIXG) — PICKS-AND-SHOVELS, FOREIGN PURE-PLAY
- **Business**: MOCVD deposition equipment for SiC, GaN, InP — the epitaxy backbone for compound semiconductors. FY2026 guidance: revenue ~€520M (±€30M), GM 41–42%, EBIT margin 16–19%. Per the FY2025 Annual Report (Feb 26, 2026): "Free cash flow increased by over EUR 250 million to EUR 181.9 million (2024: EUR –72.4 million)" — the €250M figure is the YoY improvement, with absolute FY2025 FCF of €181.9M. Equity ratio 87%.
- **AI exposure**: CEO Felix Grawert (FY2025 release): "In 2026, optical data communication for AI applications and GaN power will be the main source of revenue. We expect that AI data centers can become the largest single application for GaN power semiconductors in the near future."
- **Recent catalysts**: May 19, 2026 — multiple G10-AsP MOCVD orders from Lumentum (InP for AI optical interconnect / 800G+). May 7, 2026 — supplied Planetary G5+C systems to Renesas to expand GaN production post-Transphorm. Q2 2026 revenue guided to ~€110M (almost doubling Q1) on optical-pipeline shipments. SiC tool demand recovery expected H2 2026/early 2027.
- **Recommendation**: Buy as a diversified second-derivative play. Every named NVIDIA 800V partner needs GaN/SiC fab capacity → Aixtron supplies the tool. Singapore-based investors can access via OTC ADR (AIXG) or Frankfurt direct (AIXA — preferred for liquidity).

### D. Navitas Semiconductor (NVTS) — SPECULATIVE OPTION; SIZE ACCORDINGLY
- **Business**: Pure-play GaN (GaNFast/GaNSafe) + SiC (GeneSiC, acquired Aug 2022 for ~$270M total consideration). Torrance, CA; ~190 employees; CEO Chris Allexandre (since Sept 1, 2025).
- **NVIDIA 800V partnership** (NVTS 8-K, May 21, 2025): NVIDIA "selected" Navitas to "collaborate on next-generation 800 V HVDC architecture" supporting Kyber rack-scale systems and Rubin Ultra. At GTC 2026 / PCIM 2026, Navitas demonstrated 800V-to-6V and 800V-to-50V power delivery boards plus a 250 kW solid-state transformer.
- **Q4 2025 financials (Feb 24, 2026 release)**: Q4 revenue $7.3M; FY2025 revenue $45.9M (vs. $83.3M FY2024); GAAP net loss $117.0M; non-GAAP net loss $41.6M; cash $236.9M at Dec 31, 2025 (boosted by $95.6M net private placement in Nov 2025).
- **Q1 2026 financials (May 5, 2026)**: Revenue $8.6M (+18% QoQ, –38% YoY); non-GAAP GM 39.0%; cash $223.4M. Guided Q2 2026: $10.0M ±$0.5M revenue, GM 39.25%. Management said profitability requires "revenue in the high 30s [millions]" quarterly — implies a ~4x revenue ramp.
- **SAM/strategy** (Allexandre, Q1'26 call): $3.5B serviceable available market by 2030 across AI data centers, grid/energy infrastructure, performance computing, industrial electrification; targeting "60%+ CAGR" exposure. 8-inch GaN with GlobalFoundries, "an 8-inch pivot in 2027 for GaN manufacturing in the U.S."; TSMC buffer for existing customers.
- **Valuation reality check**: Market cap ~$6.84B at $29.01 (May 24, 2026); **EV/Sales TTM = ~82–83x** per GuruFocus and Financecharts; trailing P/E n/m (net losses). Stock hit all-time high $29.50 on May 22, 2026 vs. $1.52 low on Apr 4, 2025 — nearly 20x in 13 months. Beta 1.33; daily volatility ~21%. Consensus PT $8.15 (vs. Simply Wall St fair value $13).
- **🚨 Insider activity is severely negative — Code S open-market sales, NOT tax withholding**:
  - **Gene Sheridan** (former CEO/co-founder, stepped down Aug 31, 2025): sold 2,155,783 shares on May 23, 2025 at $4.49 weighted-avg ($9.68M) immediately post-NVIDIA announcement; subsequent 600,000-share sale June 13, 2025 (~$5M); holds zero direct shares.
  - **Brian Long** (Director / Atlantic Bridge III LP): sold 4,410,991 shares for ~$30.7M in trailing 6 months; including 1,493,046 shares on Nov 26, 2025 at $8.54 avg (~$12.75M) — an 87% reduction in direct ownership.
  - **Ranbir Singh** (Director): sold 179,354 shares on Dec 12, 2025 for $1.56M.
  - **CFO Todd Glickman**: 78,307 shares on Dec 8, 2025 at $9.77 (Code S, ~$765K); 12,532 shares on Feb 26, 2026 at $9.82 ($123K); 174,965 shares total for ~$1.78M over 6 months.
  - Per Quiver Quantitative: insiders executed 21 open-market trades in the past 6 months — **20 sales, 1 purchase**.
  - Current CEO Chris Allexandre had one 9,236-share Code-S sale on March 3, 2026 ($82,477) coincident with RSU grant settlement.
- **Short interest**: 21.05% of shares outstanding (Stock Analysis) / 28.06% of float (Benzinga, April 28, 2026 settlement).
- **Ownership**: 173.4M float (75.1% of 230.79M shares); institutional ~49% — Vanguard, BlackRock, Davidson Kempner, State Street, Capricorn, Invesco, Geode, Susquehanna, UBS, Slate Path (Fintel 13F roll-up).
- **Recommendation**: Speculative trade only — do NOT treat as a fundamental investment. Thesis is real (NVIDIA enrollment + dual GaN/SiC + working 800V demos) but valuation is the most stretched in the universe at ~83x EV/Sales TTM, the entire prior management+board insider class has been selling aggressively (Code S, not Code F), and 21–28% short interest indicates the cohort. Acceptable position size: ≤1–2% portfolio as call-option exposure. Bull case requires winning dominant socket share at Kyber's 800V→6V PDB AND solid-state transformer — both unproven competitive against Infineon/STM-tier rivals. Bear case to $8.15 (consensus PT) on revenue miss.

### E. Wolfspeed (WOLF) — AVOID until clear EV recovery
- **Status**: Emerged from Chapter 11 on September 29, 2025; Renesas converted unsecured debt into equity + secured convertible debt; CFIUS cleared Jan 30, 2026; Renesas received a board seat (Aris Bolisay) and 16,852,372 shares post-emergence.
- **Q2 FY2026 (Feb 4, 2026)**: Revenue $168.5M; AI data center revenue +50% sequentially but still "a modest but expanding part" of business. Power revenue $118M, Mohawk Valley ~$75M. Cash $1.3B; opex reduced $200M annualized run-rate; CapEx down 90% YoY. Q3 FY2026 guide $140–160M (sequentially declining) sent stock –9% after-hours.
- **Recommendation**: Avoid as a pure-play AI vehicle. Despite genuine 50% QoQ AI growth, WOLF is dominated by an EV/industrial cycle anti-correlated to the AI thematic. Reconsider only if AI data center surpasses 25% of mix or Mohawk Valley utilization unlocks materially.

### F. MPWR — NOT PURE-PLAY (excluded)
Enterprise Data fell to 25.2% of FY2025 revenue (vs. 32.5% in FY2024); NVIDIA Blackwell socket losses to Infineon (~60–70% projected) and Renesas confirmed by Edgewater Research. Excluded per the user's pure-play mandate.

### G. EPC (Efficient Power Conversion) — PRIVATE; track for reference design wins
Listed by NVIDIA as 800VDC partner at OCP 2025. Published 5 kW AC-to-48V GaN reference design (96.5% efficiency, 116 W/in³, OCP ORv3-compliant) and 800VDC-to-12.5V ISOP-topology converter. No public equity vehicle. Privately held; CEO Alex Lidow.

---

## Catalyst Calendar & Monitoring Metrics

| Date | Event | Read-Through |
|---|---|---|
| Q3 CY2026 | Vera Rubin NVL144 production ramp begins; Vertiv 800VDC MGX reference architecture in H2 2026 | First commercial 800VDC volumes |
| **Oct 12–15, 2026** | **OCP Global Summit, San Jose** | Finalized 800VDC mechanical/electrical specs; partner additions |
| Q4 CY2026 | Rubin R100 GPU sampling expected (per Tech-Insider analyst note; not NVIDIA-confirmed) | Validation of Vera Rubin/Kyber timelines |
| Feb 2027 | Navitas FY2026 results — expect first material AI data-center revenue print | Whether 800V demos convert to PO bookings |
| Q1 2027 | Rubin volume production start | Power-content lift in supply-chain financials |
| Mar 2027 | NVIDIA GTC 2027 | Kyber spec finalization |
| 2027 | Kyber/Rubin Ultra production shipments | Crystallization event for the 800VDC thesis |

**Per-name monitoring metrics:**
- **VICR**: book-to-bill (stay >1.5), royalty revenue % of total (target growth toward 25%+), 2nd-source license signings, Cerebras production cadence, hyperscaler design-win disclosure.
- **POWI**: high-power industrial growth %, new 800V design-win disclosures, PowiGaN revenue mix, eventual data-center segment disclosure.
- **NVTS**: high-power revenue mix % of total (target ≥75%), quarterly sequential growth (need acceleration from $10M Q2'26 toward $30M+ within 18 months), gross margin trajectory (toward 45%+), customer concentration commentary, **insider Code-S sales (any halt = positive signal)**.
- **WOLF**: AI data center % of total revenue (currently <10%), Mohawk Valley utilization, opex run-rate, EV demand recovery signals.
- **AIXG**: SiC tool order intake (recovery H2 2026), GaN equipment book-to-bill, AI optical orders.

---

## Risk Framework

1. **Technology disruption**: Direct 48V or interim 400VDC architectures may persist longer than expected. Some hyperscalers (Google TPU, AWS Trainium, Meta MTIA) have proprietary power chains not aligned with NVIDIA Kyber.
2. **Customer concentration / NVIDIA dependency**: Navitas thesis is heavily NVIDIA-anchored; Vicor's lead customer is a single AI accelerator vendor (likely Cerebras per third-party inference). Loss of a single relationship is catastrophic.
3. **Hyperscaler capex cyclicality**: NVDA itself disclosed direct-customer concentration of 61% (vs. 36% one year earlier) in its most recent 10-Q, meaning the marginal AI dollar is highly concentrated. Any deceleration (model commoditization, capex pause, regulatory) compresses multiples violently.
4. **Competitive response from diversified incumbents**: Infineon (CoolGaN, CoolSiC, JFET hot-swap), STMicro (joint 800VDC reference designs with NVIDIA, 12V/6V architectures), TI (Mar 16, 2026 launch of "complete 800VDC architecture"), onsemi (~$250M AI DC revenue in 2025 guided to double in 2026) are not standing still. Pure-plays must execute flawlessly to defend share.
5. **Valuation/sentiment**: NVTS at ~83x EV/Sales TTM; VICR at ~25–26x; POWI at ~9x P/S. The first two embed substantial future growth.
6. **Supply chain**: SiC substrate oversupply (Chinese suppliers) compresses pricing for upstream substrate producers but is positive for device makers buying substrates. GaN-on-Si capacity transition to 8-inch wafers (NVTS+GlobalFoundries; STMicro internal; Renesas-Aixtron) carries execution risk on yield/ramp.
7. **Insider signaling**: Aggressive Code-S selling at NVTS (20 sales vs. 1 buy in 6 months by inside class) and VICR (~$205.5M trailing 3 months) is real, not noise.

---

## Recommendations (Decision-Ready)

### Single best pure-play vehicle: **Vicor Corporation (VICR)** — staged entry, target half-weight at current price (~$300), full weight on pullback to <$240.
- **Thesis**: (1) Sole commercialized vertical power delivery solution for >120A/mm² processor loads; (2) >2x book-to-bill and 70% sequential backlog growth ($300.6M) provides high earnings visibility into 2026–2027; (3) ITC-enforced IP moat now generating accelerating high-margin royalty revenue ($14.97M vs. $10.76M YoY); (4) Capacity expansion to second fab targets $1.5B revenue capability vs. $570M 2026 guide; (5) Gross margin expansion from 47% to 55%+ in twelve months.
- **Catalysts (6–18 mos)**: Q2 2026 earnings (Jul 2026); second ITC final determination (2027) which would catalyze new licensing deals; Cerebras Gen-5 VPD volume ramp through 2H 2026; Vera Rubin NVL144 engagements.
- **PT framework**: Base case 20x 2027E sales of $700M = $14B EV / ~45M shares ≈ $310. Bull case 28x × $750M = ~$465 (~50% upside). Bear case 15x × $570M (2026 guide) = ~$190 (~37% downside).
- **Position sizing**: 2–4% of a focused thematic basket; not larger given insider selling and valuation.

### Second-best pure-play: **Power Integrations (POWI)** — Buy, full weight.
- Higher-quality, lower-volatility, GAAP-profitable, dividend-paying alternative. 800V NVIDIA collaboration uses POWI's unique 1250V/1700V PowiGaN. Sell-side range $65–85 (Susquehanna $85 implies ~12x 2027E P/S). Initiate full weight <$72; trim above $85.

### Third: **Aixtron (AIXG / AIXA)** — Buy, full weight as foreign pure-play picks-and-shovels.
- Every NVIDIA 800V silicon partner needs MOCVD capacity. FY2026 guide €520M ±€30M, 16–19% EBIT margin. Catalysts: SiC tool recovery (H2 2026); incremental GaN MOCVD orders from Renesas, Innoscience, the Navitas-GlobalFoundries 8-inch pivot.

### Speculative: **Navitas (NVTS)** — ≤1–2% portfolio call-option weighting.
- Best thematic vehicle if NVIDIA Kyber 800V→6V GaN PDB ramps fast and Navitas wins outsized share. Multi-bagger upside in perfect-execution scenarios; otherwise reversion to consensus PT $8.15 or below. Insider Code-S avalanche and 83x EV/Sales preclude fundamental sizing.

### Avoid: **Wolfspeed (WOLF)** until AI data center surpasses ~25% of mix or EV demand inflects.
### Avoid (per mandate): MPWR, Infineon, ON Semi, STMicro, TI — diversified incumbents.

---

## Caveats
1. **Forward-looking language**: NVIDIA's Kyber/Rubin Ultra roadmap pronouncements ("576 Rubin Ultra GPUs by 2027", "racks up to 1.0–1.2 MW") are stated plans, not delivered products. Independent observers (Glenn Lockwood) note Kyber demos at GTC 2026 may have been less power-dense than 2025 prototypes; NVIDIA did not formally restate Kyber power at GTC 2026.
2. **Customer name inferences**: Vicor's "lead computing customer" is widely inferred as Cerebras by third-party analysts; Vicor has not confirmed. Do not treat as fact.
3. **Fiscal year conventions**: Vicor, Navitas, POWI, MPWR, Aixtron use calendar year; Wolfspeed FY ends late June (FY2026 = Jul 2025–Jun 2026). All POWI / ON Semi 8-Ks dated FY2026 are CY2026 quarters.
4. **GAAP vs non-GAAP**: All Navitas margin/profit metrics cited are non-GAAP unless explicitly flagged; GAAP losses are materially worse (FY2025 GAAP net loss $117M). All Vicor metrics are GAAP. All Power Integrations gross margin figures are non-GAAP unless noted.
5. **Hyperscaler proprietary architectures**: Google TPU, Meta MTIA, AWS Trainium chains are not necessarily aligned with NVIDIA Kyber 800VDC. AI-native vs. NVIDIA-native power chain bifurcation is a real risk to this thesis.
6. **Singapore-based investors**: AIXG OTC may trade at meaningful liquidity discount vs. direct FSE:AIXA on Frankfurt. German dividend withholding tax should be considered. All other names are US-listed.
7. **Independent research synthesis**: User is responsible for verifying all dollar/share counts in primary 10-Qs, 8-Ks, and Form 4s before transacting.