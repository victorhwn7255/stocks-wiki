# Liquid Cooling for AI Datacenters: A Structural Primer for Institutional Investors

**As of May 17, 2026 | US-listed and US-investor-accessible names only | 2026–2030 horizon**

## TL;DR

- **Liquid cooling has crossed from "option" to physical and economic precondition for frontier AI compute.** NVIDIA's GB200 NVL72 (120 kW/rack) already mandates direct liquid cooling (DLC); Vera Rubin VR200 NVL144 (H2 2026) and Rubin Ultra "Kyber" NVL576 (600 kW/rack, H2 2027) ship with no air-cooled SKU. Air cooling has hit a hard physics ceiling at ~30 kW/rack, while AI racks are vaulting toward 1 MW. Dell'Oro's January 2026 forecast states verbatim that "Direct Liquid Cooling is forecast to surge, surpassing $8 billion by 2030, as it transitions from an enabling option to a foundational technology for AI factories," inside a Data Center Physical Infrastructure (DCPI) market "projected to grow at a mid-teens CAGR from 2025 to 2030, surpassing $80 billion" (Research Director Alex Cordovil).
- **It is unambiguously one of the top three AI bottlenecks** — co-equal with HBM and grid power. Vertiv (VRT) ended 4Q25 with a $15.0B backlog (+109% YoY, 2.9× book-to-bill); nVent (NVT) ended Q1 2026 with $2.6B backlog (3× year-ago); Comfort Systems (FIX) hit $12.45B backlog (+80.8% YoY); Eaton's CEO Paulo Ruiz disclosed on the Q1 2026 earnings call that the combined data center backlog had "grown to 228 GW, or 12 years of backlog at a 2025 build rate, up from the 11 years in our last update." Per the Financial Times Q1 2026 earnings compilation, Microsoft, Alphabet, Amazon and Meta collectively plan $725 billion of capex in 2026, up 77% from $410 billion in 2025.
- **Best risk-adjusted longs: VRT, ETN, NVT, MOD, FLEX.** We recommend a 12–15% NAV allocation to the theme, weighted to the integrators with cold-plate IP and CDU scale. Key watch items: NVIDIA Rubin shipment timing (H2 2026), hyperscaler 2027 capex guides (Oct–Feb 2027 prints), Dell'Oro quarterly DCPI updates, and PFAS regulatory action against two-phase immersion fluids.

---

## QUESTION 1 — Why Is Liquid Cooling Extremely Crucial for AI Datacenters?

### Thermal physics: a wall, not a curve

The case for liquid cooling is not a marketing thesis; it is thermodynamics. Water has roughly **3,500× the volumetric heat capacity of air** and ~24× the thermal conductivity. In practical terms, ToneCooling's engineering note observes that "air cooling heatsinks top out at 5–15 W/cm² effective heat flux. The GB200 GPU die operates at 500–600 W/cm² — 40–100× beyond air cooling capability," and at the rack level "air cooling is limited to 8–25 kW per standard server rack. The GB200 NVL72 generates 120 kW+ — 5× to 15× beyond this physical ceiling."

Even if one could move enough air, the fan power required would consume 20–30% of the rack's compute budget at 90+ dB of noise. Once chips cross ~700–1,000 W TDP, water (or a closed dielectric loop) becomes the only viable cooling fluid.

### TDP and rack-density trajectory

| Generation | Period | Per-GPU TDP | Rack power | Cooling Required |
|---|---|---|---|---|
| H100 (Hopper) | 2023 | 700 W | 30–40 kW (HGX air) | Air OK |
| H200 | 2024 | ~1,000 W | 40–60 kW | Air/rear-door |
| B200 (HGX air) | 2024–25 | 1,000 W | ~50–60 kW | Air w/ RDHx |
| **GB200 NVL72** | 2024–25 ramp | 1,200 W (Superchip) | **120 kW** | **DLC mandatory** |
| **GB300 NVL72 (Blackwell Ultra)** | 2025–26 | 1,400 W | 132–155 kW | DLC (80%+ heat to liquid) |
| **Vera Rubin VR200 NVL144** | H2 2026 | 1,800–2,300 W | ~180–250 kW | **100% liquid, no air SKU** |
| **Rubin Ultra "Kyber" NVL576** | H2 2027 | ~3,600 W (×4 dies) | **600 kW** | 100% liquid + 800 VDC + warm-water |
| Feynman | 2028+ | TBD | "multi-megawatt per rack" (Huang) | DLC + advanced |

AMD's parallel cadence: MI300X (750 W) → MI325X (1,000 W) → **MI355X (1,400 W, DLC-only)** shipping 2025 → **MI400 / MI455X "Helios" rack** H2 2026, 2 nm CDNA 5, double-wide OCP rack, 100% liquid-cooled. AMD has explicitly told the market that the MI355X "is primarily targeted towards liquid-cooled deployments."

The Uptime Institute Cooling Systems Survey 2025 — conducted online April–June 2025 with 1,033 respondents — is blunt about how far the installed base lags: 22% of operators use any DLC at all, and **more than 80% of facilities still have no racks above 30 kW**. Only roughly one in eight facilities reports any racks in the 30–59 kW band, and racks above 100 kW remain rare. The gap between what NVIDIA is shipping (120–600 kW racks) and what the installed base can handle is the entire investment thesis.

### Economics: PUE, TCO, and the free-cooling unlock

Air-cooled facilities typically run at PUE 1.4–1.6; well-designed DLC facilities run at PUE ≤1.2, and NVIDIA is targeting **PUE ≤1.15** under its joint design work with Equinix, Digital Realty, and Schneider. At a 100 MW AI campus, the delta between 1.5 and 1.15 PUE is ~35 MW of pure cooling overhead — at $80/MWh that is roughly $24M/year of avoided power, plus stranded compute capacity recovered.

Equally important is NVIDIA's "warm water" mandate. Huang told the CES 2026 audience that with Rubin, "no water chillers are necessary for datacenters" — racks can be cooled with 45 °C supply water, eliminating mechanical chillers entirely in most climates and dramatically reducing Water Usage Effectiveness (WUE). This was the comment that sent JCI –10%, TT –8%, and CARR –5% on January 6, 2026 (Bloomberg/Yahoo Finance, citing Barclays' Julian Mitchell). Free cooling at 30–45 °C inlets converts what was a chiller/evaporative-tower spend into a dry-cooler + CDU spend — a structural mix shift that favors VRT/NVT/MOD/ETN over legacy HVAC.

### Performance and reliability

GPUs throttle aggressively above 75 °C junction temperature. Introl's NVL72 documentation shows that "deviation from [cooling] specifications triggers automatic throttling that can reduce performance by 60%." When a $3M rack is depreciated over 4 years at $0.40+/GPU-hour cloud pricing, even 5–10% throttling destroys the unit economics of an AI factory. Cooling is no longer a facilities line item; it is a revenue lever.

### NVIDIA's explicit guidance

NVIDIA's GB200 NVL72 documentation, the Supermicro/Foxconn/Lenovo reference designs, and the GTC 2025 keynote all state explicitly that GB200 and above are liquid-cooled by design. The NVIDIA technical blog confirms: "The Vera Rubin NVL72 MGX compute tray offers an energy-efficient, 100% liquid-cooled, modular design."

---

## QUESTION 2 — Will Liquid Cooling Become Mandatory?

**It already is, for the SKUs that matter.** The question is no longer "if" but "how fast does the installed base catch up."

### The roadmap is the forcing function

- **2026 (now):** GB200/GB300 NVL72 in volume; DLC mandatory.
- **H2 2026:** Vera Rubin VR200 NVL144 ships. NVIDIA has confirmed there is **no air-cooled SKU**; the compute tray is "100% liquid-cooled."
- **H2 2027:** Rubin Ultra "Kyber" NVL576 — 600 kW per rack, 800 VDC distribution, warm-water mandatory. NVIDIA is now publicly partnering with Vertiv, Schneider, Foxconn, CoreWeave, and Oracle on the 800 VDC / Kyber reference architecture.
- **2028+:** Feynman. Huang has guided informally to "megawatts per rack."

AMD's MI400/MI455X Helios rack lands in the same H2 2026 window with the same physics, locking the entire merchant accelerator market into DLC by year-end 2026.

### Hyperscaler standards converge

Microsoft, Meta, Google, and AWS have all published liquid-ready rack specs through the **Open Compute Project (OCP)**. Meta's MGX/Open Rack v3 specifies blindmate quick disconnects; Microsoft has standardized on rear-door + DLC retrofits for its Maia/H100/B200 fleet; Google's TPU v5/v6 deployments are liquid; AWS Trainium2/Project Rainier is liquid. Every accelerator that matters ships with a cold plate by 2026 year-end.

### The three flavors of "mandatory"

1. **Physically mandatory** — chips cannot operate without DLC (GB200, GB300, VR200, Kyber, MI355X, MI400). This is binding today.
2. **Economically mandatory** — even where chips can run air-cooled (B200 HGX, MI350X), the rack density tax is 2–3× in real estate and 35–40% in PUE-adjusted power cost. With grid power binding (see Q3), no rational hyperscaler will pay this tax.
3. **Regulatorily mandatory** — the EU Energy Efficiency Directive recast (operative 2024–2026) imposes PUE/WUE reporting for facilities >500 kW and de-facto PUE caps in Ireland, Frankfurt, Amsterdam. Singapore's moratorium and Northern Virginia's water-tap restrictions create regional liquid-cooling pull.

### What about RDHx as a bridge?

Rear-door heat exchangers handle 50–80 kW/rack and remain a viable bridge for 2024–2025 B200 HGX retrofits. They cannot handle >100 kW. By the time GB300 reaches scale (mid-2026), RDHx is a stopgap, not a strategy.

### Retrofit vs. greenfield

MarkSpark Solutions' 2024 U.S. Data Center Coolers Market research finds that **"over 70% of existing U.S. data center floor space was originally designed to accommodate air-cooled densities below 15 kW per rack."** JLL and CBRE both estimate retrofit cost at $5–10M per MW to support GB200 deployments. The math: **most of the GB200/GB300/Rubin cycle will land in greenfield builds**, which is why Comfort Systems' $12.45B backlog matters — it is mechanical contracting for new, liquid-ready facilities. Older colocation stock faces real stranded-asset risk by 2028 unless retrofitted.

### Investment implications

- LC capex is non-discretionary for any operator hosting frontier AI. It is the last spend cut.
- 2026–2028 is a "land grab" window during which incumbents (VRT, Schneider/Motivair, ETN/Boyd, NVT) lock in OEM and hyperscaler specs.
- Operators that cannot deliver liquid-ready capacity by 2027 face customer attrition; cooling suppliers that miss the Rubin reference design face permanent exclusion.

---

## QUESTION 3 — Is Liquid Cooling One of the Major Bottlenecks?

Yes. We rank it alongside HBM, CoWoS packaging, and grid power as a top-tier AI bottleneck. The signal from order books and earnings prints is unambiguous.

### Supply-chain choke points

| Sub-component | Western suppliers | Bottleneck status |
|---|---|---|
| **CDUs (Coolant Distribution Units)** | Vertiv (Liebert XDU + CoolTera), Schneider/Motivair, Boyd/Eaton, nVent, Modine/Airedale, JetCool/Flex, Asetek, CoolIT (private) | Tight; Dell'Oro tracks ~40 vendors but the top 5 take >70% of revenue. Consolidating (Schneider→Motivair Feb 2025; Vertiv→CoolTera + STL April 2026; Eaton→Boyd Q1 2026; Vertiv→ThermoKey 2026) |
| **Cold plates** | Boyd (now ETN), JetCool (now FLEX), CoolIT, Asetek, AVC, Strategic Thermal Labs (now VRT) | Severely tight. 6–12 month lead times. Precision copper micro-channel manufacturing is the new TSMC-like bottleneck. |
| **Quick-disconnect couplings (QDCs)** | Parker (UQD/UQDB/NSG/NSP1/CDT/CDT-X/MQD), CPC, Staubli | Duopoly (Parker/CPC) for OCP/NPN-spec parts. Capacity expansion underway. |
| **Manifolds & rack distribution** | nVent (EPG/Trachte), Vertiv, Schneider | Tight; Asian competition (Auras, AVC) commoditizing low end. |
| **Dielectric fluids (two-phase immersion)** | 3M (exiting Novec by 2025), Chemours, Solvay, Castrol/BP | PFAS regulatory overhang is severe; viable alternatives scaling slowly. |
| **Thermal/mechanical engineering talent** | All players | Acute shortage; STEM PhDs in two-phase boiling are scarce. |

### Capacity vs. demand mismatch — the order book speaks

- **Vertiv (VRT)** ended 4Q25 with a **$15.0B backlog (+109% YoY)**, organic orders +252% in Q4, and 2.9× book-to-bill. The 2026 guide of up to $13.75B sales is gated by manufacturing capacity, not demand.
- **Eaton (ETN)** Q1 2026: Electrical sector backlog +48% YoY; Electrical Americas 12-month orders +42%. CEO **Paulo Ruiz stated on the call that the combined data center backlog has "grown to 228 GW, or 12 years of backlog at a 2025 build rate, up from 11 years"** (CNBC Investing Club, May 5, 2026). This is the single most extraordinary capacity statistic in the cycle.
- **nVent (NVT)** Q1 2026: **$2.6B backlog**, ~3× prior year, with management citing "outstanding growth in Liquid Cooling" and raised FY26 EPS guide to $4.45–$4.55 from $4.00–$4.15. Capex up 40% to $130M for new liquid-cooling capacity (Blaine, MN facility live in Q1).
- **Comfort Systems (FIX)** Q1 2026: **$12.45B backlog (+80.8% YoY)**, technology customers (overwhelmingly data centers) now >50% of quarterly revenue; gross margin >25% all-time high.
- **Modine (MOD)** raised FY26 guide twice — to +20–25% sales and **$455–$475M EBITDA**; data center segment growing 50–70% annually; **$2B FY28 data-center revenue target.**
- **Eaton/Boyd:** Boyd Thermal forecast $1.7B 2026 revenue ($1.5B liquid cooling); Eaton paid $9.5B (22.5× 2026 EBITDA) — the highest multiple in datacenter infrastructure M&A history, validating bottleneck pricing.
- **AAON/BASX:** Q1 2026 BASX sales +72% with **backlog +160%**; CEO Tobolski targeting "roughly $1B" of BASX revenue in 2026 with capacity above $2B.

### Power grid as parallel bottleneck

The 228 GW Eaton number is the punch line: that is more than four times current US peak datacenter demand, and it represents **roughly the entire current installed nuclear fleet of the United States**. Liquid cooling does not solve the grid problem, but it raises compute density per MW by 30–40%, partially mitigating the bind. Texas, Northern Virginia, Phoenix and Atlanta are now hard-capped; the Pacific Northwest and Mid-Atlantic are increasingly soft-capped.

### Pricing power and what equities are pricing

Vertiv trades at ~50–55× forward earnings (~$367 price, ~$141B market cap, May 12, 2026); nVent at ~34× forward EPS with backlog 3× prior year; Modine at ~30× forward with the only mid-cap pure data-center thermal story; AAON doubled in three months after the BASX Q1 print (~$11B market cap by late May from <$8B pre-earnings). These are bottleneck multiples — equity markets are paying for scarcity, not growth alone.

### Risks bottlenecks always create

- **Capacity comes** — by 2028, today's $50M cold-plate factories are $500M factories. Margins normalize.
- **Asian commoditization** — Auras, AVC, Cooler Master, and Chinese players (Sugon, Envicool, InVision) will pressure cold-plate and manifold pricing 2027–2028.
- **Technology disruption** — two-phase DLC (ZutaCore/Carrier), microconvective jet impingement (JetCool/Flex), and in-rack liquid-to-air HDUs all compete with traditional single-phase DLC.

The defensible moats rank: **cold-plate IP & co-design > integrated CDU + service > QDCs > generic chillers**.

---

## QUESTION 4 — Companies Developing & Providing Liquid Cooling Solutions

### A. US-Listed Pure-Plays / High-Purity Exposure

#### **Vertiv Holdings (NYSE: VRT)** — ~$367/share, ~$141B market cap (May 12, 2026); 52-wk range $101–$380
- **Portfolio:** Liebert XDU CDUs; CoolTera (acq. 2023) advanced CDUs; Strategic Thermal Labs (acq. April 27, 2026) — server-side cold plates and chip-level validation; ThermoKey (announced 2026) — heat exchangers/dry coolers; PurgeRite — coolant flushing services; 360AI integrated power+cooling reference design.
- **Earnings (4Q25 / Q1 2026):** FY25 revenue $10.23B (+28%); Q4 2025 organic orders +252%; backlog $15.0B (+109% YoY); 2026 guide up to $13.75B sales. Q1 2026: sales +30% YoY, +53% in the Americas; FCF $653M in single quarter.
- **Hyperscaler/NVIDIA:** Lead reference partner for GB200 NVL72; named partner on 800 VDC / Kyber MGX. Microsoft and Amazon are anchor customers.
- **Risk:** Valuation (50–55× forward EPS); customer concentration in top-4 hyperscalers; execution on CDU manufacturing capacity.
- **Positioning:** The clearest pure-play. Long.

#### **Eaton (NYSE: ETN)** — ~$399/share (May 15, 2026), ~$157B market cap; P/E ~39
- **Portfolio (post-Boyd):** Boyd Thermal cold plates, CDUs, manifolds, sealing; legacy Eaton power chain (switchgear, busway, UPS); Ultra PCS aerospace mission-critical components.
- **Boyd transaction:** $9.5B, closed Q1 2026, at 22.5× 2026 adj. EBITDA. Boyd Thermal forecast $1.7B 2026 sales of which $1.5B is liquid cooling.
- **Earnings (Q1 2026):** Sales +17% (+10% organic); Electrical Americas 12-mo orders +42%; Electrical backlog +48%. Raised 2026 organic growth guide to 10% (from 8%). **Paulo Ruiz: "data center backlog has grown to 228 GW, or 12 years of backlog at a 2025 build rate, up from 11 years."**
- **Hyperscaler/NVIDIA:** Named NVIDIA Rubin/800 VDC partner via Boyd reference designs; cross-sells power chain into LC customers.
- **Risk:** Boyd integration; Boyd's exposure was previously Goldman Sachs-owned PE asset — execution risk.
- **Positioning:** Best diversified power+cooling play with grid pull-through. Long.

#### **nVent Electric (NYSE: NVT)** — ~$165/share (May 22, 2026), ~$27B market cap; forward P/E ~34
- **Portfolio:** In-rack/in-row CDUs; manifolds; bus-bar; cable management; Trachte and EPG (Electrical Products Group) modular enclosures / engineered buildings. Brands: Schroff (enclosures), Hoffman, ERICO. Launched modular rack-level CDU for SC25 with NVIDIA, Lenovo, HPE, AMD.
- **Earnings (Q1 2026):** Sales $1.24B (+54%, +34% organic); EPS $1.09 (+63%); **backlog $2.6B**; raised FY26 guide to organic +21–23% and EPS $4.45–$4.55. Authorized new $500M share buyback May 16, 2026.
- **Hyperscaler/NVIDIA:** White-space hyperscaler wins; pure-play infrastructure exposure (now ~60%+ of revenue).
- **Risk:** Copper inflation; reliance on Trachte modular ramp.
- **Positioning:** Best mid-cap pure infrastructure exposure. Long.

#### **Modine Manufacturing (NYSE: MOD)** — ~$260/share (late May 2026), ~$13B market cap; forward P/E ~30
- **Portfolio:** Airedale by Modine — TurboChill chillers (1 MW+), 1 MW CDUs, single-phase immersion, Climate by Design AHUs. Investing $100M to expand US capacity (Dallas, Grenada MS, Franklin WI, Jefferson City MO).
- **Earnings (FY26 Q3, Feb 2026):** Raised guide to +20–25% sales and **$455–$475M adjusted EBITDA**; data-center sales +78% YoY; multi-year DC growth guide raised to 50–70%; **$2B+ FY28 DC revenue target**.
- **Hyperscaler/NVIDIA:** Single $180M hyperscaler order announced Feb 2025; NVIDIA-certified Airedale chillers.
- **Risk:** Legacy auto/HVAC drag; spin-off of Performance Technologies into Gentherm announced Jan 2026 (~$1B value; MOD holders get ~40% of combined NewCo).
- **Positioning:** Best mid-cap "second-derivative" play with valuation upside vs. VRT. Long.

#### **Flex Ltd. (NASDAQ: FLEX)** — ~$130–140/share (mid-May 2026), ~$48B market cap
- **Portfolio:** JetCool (acq. Nov 2024) — microconvective direct-to-chip cold plates and CDUs; Anord Mardix and Crown Technical Systems — critical power and busway; Electrical Power Products (EP², closed May 4, 2026, $1.1B).
- **Strategic event:** May 5, 2026 announcement to spin off **Cloud & Power Infrastructure (CPI) segment** as independent public co. (SpinCo) by **Q1 calendar 2027**. CPI forecast +65–75% growth in FY27 and +80% in FY28.
- **Earnings (FY26 Q4, May 6, 2026):** Adj EPS $0.93 vs $0.87 est; revenue $7.5B (+17%); FY26 revenue $27.9B (+8%).
- **Hyperscaler/NVIDIA/Broadcom:** **March 11, 2026 Broadcom XPU design win** — JetCool single-phase DTC for next-gen Broadcom ASICs at 4 W/mm² heat flux. Also Equinix Co-Innovation Facility partnership.
- **Risk:** EMS legacy margin drag; spin execution risk.
- **Positioning:** Sum-of-parts value as SpinCo reveals AI-data-center segment economics. Long, with spin catalyst.

### B. US-Listed Component / Tier-2 Suppliers

#### **Parker Hannifin (NYSE: PH)** — ~$770/share, ~$113–124B market cap
- **Portfolio:** UQD, UQDB, NSG, NSP1, CDT, CDT-X, MQD, MQDB, CDB, BMQC, RNS quick-disconnect couplings — virtually the entire NVIDIA NPN-approved interconnect set; OCP UQD spec co-developer (with Intel).
- **Earnings (FQ3 FY26, April 2026):** Revenue $5.49B (+10.6%); record backlog $12.5B; raised FY26 adj EPS guide.
- **Risk:** Competition from CPC and Staubli; aerospace cyclicality dominates the broader story.
- **Positioning:** "Picks-and-shovels" tier-2 with QDC duopoly economics. Quality long; expect slower beta than pure plays.

#### **Carrier Global (NYSE: CARR)** — ~$67/share (May 14), ~$55B market cap
- **Exposure:** QuantumLeap thermal suite; Carrier Ventures invested in **ZutaCore** (waterless two-phase DTC, expanded April 29, 2026) and Strategic Thermal Labs (2025; STL since acquired by VRT).
- **Earnings (Q1 2026):** Revenue $5.34B beat; **data center orders +500%**; reaffirmed FY26 $22B / $2.79 EPS.
- **Risk:** Only ~5% DC exposure; "Rubin revelation" CES selloff exposed asymmetric downside; residential HVAC drag.
- **Positioning:** Optionality, not core. Hold or trade.

#### **Johnson Controls (NYSE: JCI)** — ~$138/share, ~$90B market cap
- **Exposure:** Silent-Aire CDU and modular DC business; legacy chillers; YORK air-side. Low-double-digit % data center exposure (Barclays' Julian Mitchell).
- **Risk:** Most exposed to chillerless Rubin design; –10% on Jan 6, 2026.
- **Positioning:** Avoid as pure LC play; only own for broader buildings story.

#### **Chart Industries (NYSE: GTLS), Flowserve (FLS), Watts Water (WTS)** — adjacent fluid-handling and heat-exchanger suppliers; smaller, less direct exposure.

### C. US-Listed Adjacent / Facility Cooling Beneficiaries

#### **AAON / BASX (NASDAQ: AAON)** — ~$134/share, ~$11B market cap (post-Q1 surge)
- BASX: custom-engineered fan walls, CRAH units, evaporative coolers, packaged mechanical rooms, **liquid-cooling CDU products**. Memphis facility commissioned 2025.
- Q1 2026: sales +54% to $497M; backlog $2.13B (+107%, BASX backlog +160%); BASX revenue +72% YoY. CEO Tobolski guides "roughly $1B" BASX revenue 2026, capacity above $2B.
- **Positioning:** Best small-cap with explicit DC liquid cooling pull. Long.

#### **Comfort Systems USA (NYSE: FIX)** — ~$1,825/share, ~$64B market cap; ATH $2,074 May 14
- The mechanical contractor — designs and installs the LC piping, manifolds, CDUs, modular plant rooms. **Q1 2026 backlog $12.45B**, technology customers >50% of revenue, GM >25%.
- **Positioning:** Best installer beneficiary. Long; lower multiple than VRT (~40× forward).

#### **SPX Technologies (NYSE: SPXC), Trane Technologies (NYSE: TT), Lennox (NYSE: LII)** — facility-side beneficiaries with rising DC exposure but partial substitution risk from chillerless Rubin.

### D. US-Investor-Accessible Non-US Names (OTC ADRs)

#### **Schneider Electric (OTC: SBGSY)** — ADR ~$62, ~$175B market cap
- **Motivair** acquired Feb 2025; full liquid-cooling portfolio unveiled Sept 29, 2025 (CDUs, ChilledDoor RDHx, HDU, cold plates, chillers). **MCDU-70 2.5 MW CDU** launched Jan 21, 2026, scalable to 10 MW+ via EcoStruxure. NVIDIA gigawatt-AI-factory validated blueprint partner.
- Motivair CDU technology powers 6 of the world's top 10 supercomputers and is NVIDIA-certified.
- **Positioning:** Closest non-US pure-play; constrained for US investors to OTC ADR liquidity.

#### **ABB (OTC: ABBNY), Munters (OTC: MTRSY), Alfa Laval (OTC: ALFVY)** — meaningful exposure, primarily power (ABB), evaporative (Munters), and brazed-plate heat exchangers (Alfa Laval). Smaller AI-DC purity, broader industrial exposure.

### E. Notable Private / Pre-IPO

| Company | Tech | Note |
|---|---|---|
| **CoolIT Systems** | Single-phase DLC, CDUs, cold plates | Major hyperscale supplier; sponsored by KKR. Top IPO candidate. |
| **Iceotope** | Precision immersion (UK) | HPE partnership |
| **Submer** (Spain) | Immersion | OCP-aligned |
| **LiquidStack** | Two-phase immersion | Bitmain spin-out |
| **Green Revolution Cooling** | Single-phase immersion | Texas-based |
| **Boyd** | DLC, cold plates | **Now ETN as of Q1 2026** |
| **Strategic Thermal Labs** | Cold plate IP | **Now VRT as of April 2026** |
| **Asetek (OB: ASTK)** | Sealed DLC, PC-dominant | Norway listed; micro-cap |

---

## FINAL SECTION — Investment Synthesis

### The Five Best Risk-Adjusted Longs

1. **VRT** — purest play, largest backlog, dominant integrator. Premium multiple but the franchise is in place. Core position.
2. **ETN** — best diversified power+cooling franchise post-Boyd; the 228 GW datacenter backlog is the single most striking statistic in industrial earnings season. Strongest moat versus future commoditization.
3. **NVT** — pure mid-cap infrastructure exposure with the cleanest organic growth print (Q1 +34% organic), 3× backlog growth, raised guide. Less crowded trade than VRT.
4. **MOD** — best second-derivative play. Trades at a meaningful discount to VRT despite comparable DC growth; PT spin-off into Gentherm catalyzes pure-thermal valuation.
5. **FLEX** — CPI spin-off (Q1 2027) is a near-term sum-of-parts catalyst; JetCool gives genuine cold-plate IP; Broadcom XPU win validates non-NVIDIA AI exposure.

### Portfolio Construction

- **~12–15% NAV** dedicated to AI Liquid Cooling / DC Infrastructure thematic.
- Weighting: VRT 25% / ETN 25% / NVT 20% / MOD 15% / FLEX 15% of the bucket.
- Pair-trade considerations: **Long NVT, short TT or JCI** to express the chillerless-Rubin transition; **Long MOD, short LII** for similar reason in mid-cap.
- Watch AAON and FIX as add-on small-caps once positions are established.

### Key Risks

1. **AI capex digestion.** Per the Financial Times Q1 2026 earnings compilation, Microsoft, Alphabet, Amazon and Meta plan $725B of capex in 2026, up 77% from $410B in 2025. If hyperscaler 2027 capex flatlines, the bottleneck premium compresses 30–40% in equity multiples within two quarters. Meta's –7% extended-trading reaction (and roughly –10% intraday on April 30) to its own raised 2026 capex guide of $125–145B (CNBC/Fortune, April 29–30, 2026) was the first warning shot.
2. **Technology disruption.** Two-phase immersion (Carrier/ZutaCore) or microconvective jet impingement (Flex/JetCool) could displace standard cold-plate DLC at the high end. Conversely, PFAS regulation could kill two-phase fluids — a tail risk that cuts both ways.
3. **Asian commoditization.** Auras, AVC, Cooler Master, and Chinese players (Sugon, InVision, Envicool) are competitive on cold plates and manifolds by 2027. Margin compression starts at the component layer.
4. **Regulatory.** PFAS-bans accelerating in EU and US states; WUE caps tightening in Ireland, Frankfurt, Singapore, Virginia.
5. **NVIDIA single-point dependency.** If AMD MI400/MI455X Helios racks meaningfully take share in H2 2026, reference-design hegemony shifts — historically a smaller transition but one that re-rates winners (FLEX/JetCool gain; Schneider/Vertiv compete more aggressively).
6. **Capacity catches up.** By 2028–2029, today's bottleneck pricing normalizes. Returns from this thematic will be front-loaded 2026–2028.

### 12–18 Month Watch Items

- **Hyperscaler 2027 capex guides** (October 2026 – February 2027 earnings prints). A combined number above $850B confirms the cycle is uninterrupted; below $700B signals digestion.
- **NVIDIA Rubin VR200 shipment timing.** Any slip from H2 2026 into 2027 is a catalyst for cooling-name de-rating on near-term order conversion concerns.
- **Dell'Oro quarterly DLC and DCPI updates.** Watch for upward revision of the $8B 2030 DLC TAM and CDU market-share movement.
- **PFAS rulemaking** at EPA and ECHA, especially for two-phase coolants.
- **Vertiv, nVent, Modine Q2 2026 backlog prints.** A 3× backlog/forward-revenue ratio is the bottleneck signal; compression below 2× is the early warning of normalization.
- **Eaton/Boyd integration progress.** First clean LC quarter (likely Q3 2026) sets the bar for ETN re-rating.
- **AMD MI400 Helios ship rate** and any AWS / Meta hyperscaler win-rates against Rubin.

---

## CAVEATS

- Stock prices and market caps as of approximately May 12–25, 2026; the cohort has been highly volatile and intraday moves of 5–10% have been common.
- The 228 GW Eaton datacenter backlog figure is a CEO disclosure on the Q1 2026 earnings call (CNBC Investing Club, May 5, 2026); it is cumulative pipeline including non-binding interest and should not be interpreted as firm orders.
- NVIDIA's CES 2026 "no water chillers needed" statement (Jensen Huang) is a directional design preference applicable to Rubin and beyond at 45 °C supply; chillers remain relevant in hot/humid climates and for Blackwell-era retrofits.
- Dell'Oro DLC market sizing ($8B+ by 2030 within $80B DCPI) is from the January 2026 5-Year Forecast Report (Alex Cordovil, Research Director, February 10, 2026 press release) and may be revised upward given the 2Q25 +156% YoY growth print.
- The 70%+ legacy U.S. data-center floorspace figure designed for <15 kW per rack is sourced to MarkSpark Solutions' 2024 U.S. Data Center Coolers Market study; broker estimates from JLL/CBRE corroborate the directional point but specific percentages vary.
- Private comparables (CoolIT, Iceotope, Submer) are listed for thematic context only; they are not investable for US institutional investors absent IPO.
- The Uptime Institute Cooling Systems Survey 2025 (n=1,033 respondents, fielded April–June 2025) shows DLC adoption at only 22% of operators — the dispersion between this slow installed-base adoption and NVIDIA's mandatory DLC roadmap is precisely the source of the bottleneck and the investment thesis.
- This report is not investment advice. Valuation multiples disclosed (VRT 50–55× forward, NVT 34×, MOD 30×) embed substantial growth assumptions that may not realize if hyperscaler capex declines.