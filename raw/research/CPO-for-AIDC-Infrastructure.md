# Co-Packaged Optics for AI Datacenter Infrastructure: A Variant Perception Memo
**Buy-side thematic research • 12-24 month catalyst horizon • May 26, 2026**

---

## 1. Executive Summary

CPO has shifted from "interesting technology" to "production-validated" in 2025-2026 — Broadcom's TH5-Bailly accumulated 1M+ flap-free 400G port-device-hours at Meta (Broadcom PR, Oct 1, 2025: "one million cumulative 400G equivalent port device hours of flap-free CPO operation at Meta"), the TH6-Davisson 102.4T CPO switch is shipping (Oct 8, 2025), TSMC's COUPE platform is in volume production in 2026 (TSMC SEMICON Taiwan disclosures), and NVIDIA invested $4B into Coherent and Lumentum (March 2, 2026) explicitly to secure CPO/photonics supply. **Yet the bullish consensus that this means imminent broad CPO adoption misreads the actual constraint.** Pluggable optics (1.6T DR8 at ~17.5 pJ/bit per Meta-disclosed FiberMall testing; LPO at ~9-11 pJ/bit per Vitex) are not the binding constraint at the *front panel* for scale-out fabrics in 2026-2028; the real binding constraints are (a) the *scale-up* (rack-internal, NVLink/ICI-class) network where copper has run out, and (b) the laser and advanced-packaging supply chain. The market is conflating these.

The investable consequence: the dollar opportunity from CPO over the next 24 months is concentrated in **lasers, advanced packaging, and ODM/CM precision optical assembly** — not in switch silicon margin uplift and not in displacement of merchant DSP vendors at scale-out. Pluggable transceivers (and their suppliers: InnoLight, Coherent, Eoptolink) keep growing in absolute dollars through 2027-2028 even as CPO ramps in parallel. TrendForce's projection of 800G+ shipments rising from 24M units (2025) to 63M (2026) is overwhelmingly pluggable — the pluggable category is *accelerating* even as CPO becomes production-ready.

## 2. Variant Perception (one sentence)

**Consensus treats CPO as a near-term displacement of pluggables; our variant view is that CPO is primarily a *scale-up* (intra-rack/intra-pod) technology that will coexist with — not replace — 1.6T/3.2T pluggables in scale-out for the next 3-5 years, which means the margin-capture pool concentrates in the laser/packaging chokepoint, not in switch ASICs or DSP displacement, and the most-discussed "CPO winners" (merchant switch silicon, NVIDIA, hyperscalers) are not where the *incremental* margin actually accrues.**

Framing the core debate: **CPO adoption is NOT primarily a technology-readiness problem (Broadcom and Meta answered that with 1M flap-free port-device-hours and 5.4W/800G), and it is NOT mainly a timing-arbitrage problem (Davisson is already shipping). It is a (a) hyperscaler-architecture problem — does the customer's network topology want CPO at scale-out, scale-up, or both? — and (b) a margin-capture problem — who actually gets paid?** The right question is not "when does CPO ramp?" but "where in the value chain does the optical content dollar flow?"

## 3. CPO Architecture: Strict Definitions

Confusion across these categories is the single most common analyst error. Strict definitions, tightest integration to loosest:

- **Optical I/O (chiplet-class, e.g., Ayar Labs TeraPHY + SuperNova ELS; Broadcom future XPU CPO):** Optical engine integrated *in-package* with the compute/switch die via 2.5D/3D advanced packaging (CoWoS, SoIC). Light enters/exits the package. Used for chip-to-chip in scale-up. Ayar's TeraPHY is now a UCIe chiplet (March 31, 2025 announcement), 8 Tbps, manufactured on GlobalFoundries 45nm photonics. Ayar's March 2026 Series E ($500M, NVIDIA/AMD-backed) valued the company at $3.75B.
- **CPO (strict, switch-class, e.g., Broadcom TH5-Bailly, TH6-Davisson):** Switch ASIC and *multiple* silicon-photonic optical engines share a *common substrate*. No electrical SerDes leave the package toward the front panel. Lasers are *external* (ELS / Pluggable Laser Source / ELSFP). TH5-Bailly: 51.2T, 8× 6.4T engines, 5.5W per 800G port (~6.9 pJ/bit; Next Platform). TH6-Davisson: 102.4T, 16× 6.4T engines, ~3.5W per 800G port (~4.4 pJ/bit), uses TSMC COUPE. Broadcom 4th-gen (400G/lane) announced in development.
- **NPO (Near-Packaged Optics):** Optical engines placed *centimeters* from the ASIC on the PCB/substrate. Shorter electrical traces than front-panel pluggables but not on the package. Transitional.
- **NVIDIA Quantum-X / Spectrum-X Photonics:** **Hybrid implementation.** TSMC SoIC-X 3D hybrid bonding stacks 65nm EIC on PIC (COUPE), then six (Quantum-X) optical sub-assemblies are integrated on the switch-package *interposer*. Detachable optical sub-assemblies + external CW lasers (Coherent, Lumentum). Closer to strict CPO than NPO, but NVIDIA emphasizes "4× fewer lasers, detachable subassemblies." Power: NVIDIA Developer Blog states 9W per 800G port for Quantum-X (~11.3 pJ/bit) — *worse* than Broadcom TH6-Davisson at ~3.5W (~4.4 pJ/bit). This is a meaningful, under-discussed gap.
- **LRO (Linear Receive Optics):** Removes DSP on receive side only; transmit retains DSP. Pragmatic intermediate at 1.6T given thermal/power.
- **LPO (Linear Pluggable Optics):** Removes DSP entirely; analog TIAs + drivers. Current commercial 800G LPO at 7-8.5W/module (~9-11 pJ/bit per Vitex). Adtran's LiteWave800 announced at OFC 2026 claims 0.8W and 1 pJ/bit — vendor claim, not deployed. LPO MSA published March 25, 2025.
- **Conventional pluggables (OSFP, QSFP-DD, OSFP-XD):** Full DSP. 800G DR8 at ~17.5 pJ/bit (FiberMall testing of DSP modules). 1.6T via OSFP-XD (16× 100G) or OSFP-RHS/IHS — 92% of 2025 hyperscaler 1.6T procurement is OSFP-XD per OCP guidance. 3.2T expected ~2027-2028 on 16× 200G.

**Why this matters:** "Adoption is already happening" depends entirely on which definition is invoked. NVIDIA Spectrum-X Photonics availability is 2H 2026 (Ethernet), but it is not strict Broadcom-class CPO. Genuine strict-CPO production deployment to date is Meta's Bailly characterization cohort of 15 switches — not a 100k-port production fleet.

## 4. Value-Chain Map (6 layers, qualitative H/M/L)

### Layer A — Photonic Die / Optical Engine
- **Players (US-listed):** Broadcom (AVGO), Marvell (MRVL — including Celestial AI Photonic Fabric, acquired Dec 2, 2025 for up to $6B total deal value per Marvell 8-K: ~$3.25B upfront ($1B cash + ~$2.25B in ~27.2M shares) plus up to ~27.2M earnout shares tied to revenue milestones), Coherent (COHR), Lumentum (LITE), Intel (INTC), GlobalFoundries (GFS). Private: Ayar Labs ($3.75B post-money), Ranovus.
- **Margin capture: HIGH** (silicon photonics IP + advanced packaging integration).
- **Commoditization risk: LOW** in next 24 months; rises thereafter as Samsung/UMC/Tower enter (Samsung targeting OE 2027, turnkey CPO 2029).
- **IP defensibility: HIGH** — micro-ring modulator (MRM) integration, hybrid bonding, fiber-to-PIC coupling are deep moats. TSMC filed ~50 SiPh patents in 2024 vs Intel's 26 (Nikkei via MoneyDJ).
- **Volume mfg capability: LOW-MEDIUM today**, scaling. TSMC COUPE in volume production 2026; SoIC monthly capacity reportedly headed to 30-40K wpm by end-2026 (Commercial Times via Borecraft).
- **Beneficiary if CPO early: AVGO, MRVL, COHR, GFS, INTC** (INTC speculative).
- **Beneficiary if CPO delayed: COHR, LITE** (pluggable transceiver content keeps growing).

### Layer B — DSP / SerDes / Switch Silicon Integration
- **Players:** Broadcom (AVGO), Marvell (MRVL), Credo (CRDO), Astera Labs (ALAB), MaxLinear, NVIDIA (NVDA), AMD, Cisco (CSCO), Arista (ANET).
- **Margin capture: MEDIUM-HIGH today, MEDIUM in CPO end-state.** CPO eliminates the standalone optical DSP. CRDO/MRVL optical DSP attach goes away on CPO ports; SerDes IP value remains (still need 200G/400G electrical lanes on package).
- **Merchant-silicon displacement risk for DSP vendors: REAL but BOUNDED.** Optical DSP TAM (~$1.2B 2024, ~11.5% CAGR per Verified Market Reports). If CPO captures even 20-30% of 1.6T+ optical attach by 2028, DSP TAM growth stalls for that subset — but pluggable still dominates volumes in scale-out for 5+ years. CRDO's exposure is concentrated in AECs (ZeroFlap) and SerDes IP — AECs *benefit* from copper retention in scale-up; only CRDO's optical DSP line is at risk. ALAB is mostly PCIe/CXL (Aries), Scorpio fabric, AECs (Taurus) — minimally exposed to CPO displacement; PCIe-over-optics is a growth vector.
- **IP defensibility: HIGH for SerDes IP; MEDIUM for retimers.**
- **Commoditization risk: LOW-MEDIUM** (high-speed SerDes club: NVDA, AVGO, MRVL, Alphawave).
- **Beneficiary if CPO early: AVGO (switch CPO), NVDA (vertical stack).**
- **Beneficiary if CPO delayed: CRDO, MRVL (optical DSP), ALAB (broader ecosystem), MaxLinear.**

### Layer C — Lasers / Light Source (the CW chokepoint)
- **Players:** Lumentum (LITE), Coherent (COHR), Applied Optoelectronics (AAOI), EMCORE.
- **Margin capture: HIGHEST.** This is the chokepoint. In CPO, modulation moves to silicon photonics; the laser becomes an *external* CW source. Lumentum holds 50-60% global share at 200G/lane EML and is the only volume supplier (anandcapital/MLQ research). NVIDIA's $2B + $2B investments in LITE and COHR (March 2, 2026, both SEC 8-Ks) are *purchase-commitment + equity* — explicit confirmation this is the scarce resource. NVIDIA invested in LITE at $695.31/share (per Lumentum 8-K). Coherent disclosure (Sept 25, 2025): sampling 400 mW CW DFB at 1311 nm, BH DFB platform; volume production Q3 2026; new 6-inch InP fab in Sherman, TX expanding capacity >5x.
- **Commoditization risk: LOW** for next 3-5 years (InP epi capacity is multi-year to build).
- **IP defensibility: HIGH** (BH DFB IP, InP epi).
- **Volume mfg capability: MEDIUM** and expanding. Lumentum committed to +40% 200G EML capacity 2025, +40% again 2026 (mgmt commentary).
- **Beneficiary if CPO early: LITE (CW lasers), COHR (CW lasers + transceivers + InP modulators + own socketed CPO demo at OFC 2026 paired with own ELS module).**
- **Beneficiary if CPO delayed: LITE, COHR, InnoLight, Eoptolink** — same lasers, just inside pluggables instead of ELS modules. **The laser players win in BOTH scenarios.** This is the asymmetric long.

### Layer D — Packaging, Substrate, Fiber Attach, Test
- **Players:** TSMC (TSM) [COUPE, SoIC, CoWoS], Amkor (AMKR), ASE Technology (ASX) [NVIDIA CPO partner], Advantest (test).
- **Margin capture: HIGH for TSMC (chokepoint on COUPE + CoWoS), MEDIUM for AMKR/ASX (outsourced test, fiber attach robotics).**
- **Commoditization risk: LOW (TSMC), MEDIUM (OSATs).**
- **IP defensibility: HIGH (TSMC — SoIC-X hybrid bonding); MEDIUM-LOW for fiber attach.**
- **Volume mfg capability:** TSMC reportedly 30-40K wpm SoIC by end-2026; CoWoS at 5.5-reticle, >98% yield in 2026 (TSMC Symposium 2026).
- **The real risk:** CPO competes with GPU/HBM for CoWoS capacity. Most overlooked supply gating factor.
- **Beneficiary if CPO early: TSM (clearest), ASX, AMKR.**
- **Beneficiary if CPO delayed: TSM (still wins on GPU/HBM).**

### Layer E — ODM / System Integration / Module Assembly
- **Players:** Fabrinet (FN), Celestica (CLS), Jabil (JBL — acquired Intel SiPh transceiver business 2023), Sanmina, Flex (FLEX), Foxconn/Hon Hai, Quanta. Fabrinet made a $32M minority investment in Raytec Semiconductor (FY26 Q3 disclosure) for wafer-level packaging for CPO.
- **Margin capture: LOW-MEDIUM. Revenue: HIGH.** Classic margin trap. Fabrinet Q3 FY26 record $1.21B (+39% YoY) and EPS $3.72; three active CPO customer programs (scale-up + scale-out); two new datacom transceiver programs to a hyperscaler — but Fabrinet's gross margin is ~12-13%, structurally below photonic-die or laser layers. NVIDIA = 27.6% of FY25 revenue, Cisco = 18.2% (10-K).
- **Commoditization risk: MEDIUM-HIGH.**
- **IP defensibility: LOW-MEDIUM** (process know-how in fiber alignment, wafer-level packaging).
- **Beneficiary if CPO early: FN (3 CPO programs, Raytec stake), CLS (Hon Hai partnership for NVIDIA CPO).**
- **Beneficiary if CPO delayed: FN, JBL, CLS** (pluggable assembly).

### Layer F — Hyperscaler Pull
- **Observable signals:**
  - **Meta:** Most committed to CPO. Amiralizadeh et al. paper at ECOC 2025 (with Broadcom) on TH5-Bailly: initially 1,049k 400G port-device-hours across 15 Bailly 51.2T CPO switches, extended at the ECOC talk to 15M 400G port-device-hours, "no failures or uncorrectable codewords (UCWs)"; one FEC bin >10 event in the initial 1,049k-hour run traced to a faulty fiber. Paper conclusion: *"The demonstrated lower bound mean time between failures of (MTBFs) of optical links can readily support a 24K GPU AI cluster with >90 percent training efficiency without interconnect failures being the bottleneck."* 65% optics power savings vs pluggables (5.4W per 800G CPO vs 15W per 800G DSP pluggable).
  - **Google:** Heavily invested in OCS (Apollo/Mission Apollo) for TPU scale-up. *Ironwood TPUv7* uses 3D Torus + Apollo OCS with 9,216-chip superpods (144 4×4×4 cubes, 48 OCS units, 13,824 optical ports). Google is on a *parallel* optical path that is not strict CPO but consumes massive 800G+ transceivers. TrendForce (Feb 10, 2026): InnoLight + Eoptolink (jointly) capture ~80% of Google's 800G+ optical module orders.
  - **NVIDIA:** Spectrum-X / Quantum-X Photonics (hybrid CPO). Quantum-X InfiniBand availability 2H 2025; Spectrum-X Ethernet 2H 2026. The $4B Coherent + Lumentum equity + multi-year purchase commitment (March 2, 2026) is the strongest single signal of NVIDIA's CPO commitment.
  - **AWS:** Building proprietary scale-up via Marvell/Celestial AI Photonic Fabric (Dave Brown, VP Compute & ML Services, on Celestial acquisition: *"we believe optical interconnects will play an important role in the future of AI infrastructure"*).
  - **Microsoft:** Quietest publicly. Maia networking architecture not publicly committed to CPO.
- **Capex backdrop (2026):** Big-Four (MSFT+GOOG+META+AMZN) plan $725B per FT/Tom's Hardware (+77% YoY). Specific guidance: Amazon $200B, Google $175-185B, Meta raised to $125-145B in Q1 2026 (from prior $115-135B per Yahoo Finance, *"raised full-year capex guidance to $125-$145B citing higher component and data center costs"*), Microsoft $190B (Amy Hood, CFO, attributed $25B to rising memory chip/component costs), Oracle ~$50B. Of this, ~75% AI infrastructure (CreditSights). Networking is ~15-20% of AI infra → implied 2026 AI networking spend ~$80-110B.

## 5. Adoption Trigger Framework (ranked by importance × falsifiability)

| Rank | Trigger | Importance | Falsifiability | Status |
|---|---|---|---|---|
| 1 | **Switch radix at 102.4T / 204.8T** | HIGH | HIGH | TH6-Davisson at 102.4T shipping Oct 2025; 204.8T projected ~2028 |
| 2 | **TSMC COUPE / CoWoS capacity** | HIGH | HIGH | COUPE in volume 2026; SoIC at 30-40K wpm by end-2026 |
| 3 | **GPU cluster scale (>100K → >1M XPU)** | HIGH | MEDIUM | NVIDIA Rubin 2H 2026; Anthropic >1M TPU commitment |
| 4 | **224G SerDes reach/power at 1.6T+** | HIGH | HIGH | NVIDIA Blackwell ships 224G; Broadcom 224G sampling late 2024 |
| 5 | **Yield maturity for SiPh-electronic integration** | HIGH | MEDIUM | Bailly: 1M+ port-device-hours flap-free |
| 6 | **Pluggable supply shortfall** | HIGH | MEDIUM | Per McKinsey "Optical Networking: Capturing the Next Wave of Value" (Wiseman/Marcil/Hämäläinen/Sachdeva): *"Production of 800-Gbps transceivers is expected to fall 40 to 60 percent short of demand through 2027, and 30 to 40 percent shortfalls in the supply of 1.6-Tbps transceivers are likely to persist through 2029"* |
| 7 | **Hyperscaler scale-up architecture choice** | HIGH | LOW (opaque) | NVIDIA NVLink-over-fiber for Rubin Ultra unclear; AWS = Celestial; Google = OCS+ICI |
| 8 | **OIF CEI-224G, IEEE 802.3df standards** | MEDIUM | HIGH | CEI-224G ratified; LPO MSA published March 2025 |
| 9 | **Serviceability (LRU)** | MEDIUM | HIGH | TH6-Davisson: field-replaceable ELSFP laser modules — *resolved* |
| 10 | **Power-per-bit inflection** | MEDIUM | HIGH | Already crossed: TH6 ~4.4 pJ/bit vs pluggable ~17.5 pJ/bit |

The 2025-2026 catalyst sequence checks essentially all triggers except #7 (which we cannot directly observe). **The remaining binding constraint is hyperscaler architecture choice, which is heterogeneous: Meta is committed, Google is on an OCS-different path, AWS is on a Marvell/Celestial path, Microsoft is quiet.** Heterogeneity = no single-vendor "CPO wave," which is precisely why the laser/packaging layers (architecture-agnostic) capture the margin.

## 6. Scuttlebutt Signal Dashboard

**Confirmation signals (CPO ramps faster than consensus):**
1. **LEADING:** Lumentum / Coherent quarterly EML and CW laser bookings; gross-margin mix shift to CW DFB / 200G EML. *Today: Coherent sampling 400 mW CW lasers (Sept 25, 2025), $4B NVIDIA injection, 6-inch InP at Sherman TX scaling. STRONG confirm.*
2. **LEADING:** Fabrinet earnings call commentary on CPO customer programs. *Today: three active CPO customer programs, Raytec investment, hyperscale datacom programs — but mgmt explicitly says CPO revenue "small." Modest confirm.*
3. **LAGGING:** Hyperscaler capex breakouts on networking; Meta's Bailly fleet expansion beyond 15 units.

**Invalidation signals (CPO delayed; pluggable extension wins):**
1. **LEADING — KEY:** **1.6T OSFP-XD pluggable shipment ramp + 200G EML ramp.** TrendForce: 800G+ shipments from 24M units (2025) to 63M (2026) — overwhelmingly pluggable. *STRONG invalidation of the near-term CPO replacement thesis.*
2. **LEADING:** **Arista (ANET) commentary — verbatim Jayshree Ullal Q1 2026 (May 2026):** *"While the industry has been talking a lot about co-packaged optics, these are still science experiments, and they are very proprietary with individual vendors doing their own thing. We embrace open CPO a few years from now, but we think XPO has a ten-year run, especially at 1.6T and 3.2T where you need liquid cooling and you need that kind of capacity."* Andy Bechtolsheim at OFC 2025 Optica Executive Forum: 3nm DSPs at 25W vs CPO/LPO at 10W (60% less) — Arista launched its own XPO module (12 Tb/s, 4× OSFP density) March 2026.
3. **LAGGING:** **Cisco — verbatim Bill Gartner (SVP/GM Optical Systems):** *"the industry is going to go through a learning curve of making [CPO package assembly with 1,000+ optics connections] a very high yield and very highly reliable."* Chuck Robbins (CEO): *"We absolutely believe it's going to happen... but today, they want choice."*

**Reading the dashboard today (May 26, 2026):** Both sides firing. Confirmation signals support CPO production-readiness; invalidation signals confirm pluggable absolute-dollar growth continues. Consistent with our variant view — *coexistence, not displacement.*

## 7. Bottoms-up TAM Model (qualitative, 3 scenarios)

**Dominant variables (ranked by spread contribution):**
1. **Optical attach rate per XPU × ports per cluster** (largest swing).
2. **CPO/pluggable mix at 1.6T+ scale-out** (second-largest).
3. **Scale-up optical attach** (newest, largest *option* value): today mostly copper or NVLink. If NVLink-over-fiber and Marvell-Celestial Photonic Fabric become standard, scale-up creates an optical TAM 2-4× the size of scale-out for the same accelerator count.

Total addressable silicon photonics market context (MarketsandMarkets, Apr 24, 2025, *"Silicon Photonics Market by Product…Global Forecast to 2030"*): *"The global silicon photonics industry was valued at USD 2.65 billion in 2025 and is projected to reach USD 9.65 billion by 2030, growing at a CAGR of 29.5% from 2025 to 2030."*

### Bull Case (CPO 2026-2027 meaningful deployment, ~25% probability)
- **Assumption:** TH6-Davisson + NVIDIA Spectrum-X Photonics drive >20% CPO attach in 51.2T+ switches starting 2H 2026; 1.6T pluggables peak earlier as Rubin Ultra forces scale-up over fiber.
- **Dominant winners:** AVGO (CPO ASIC margins), LITE/COHR (CW lasers), TSM (COUPE), FN (CPO assembly).
- **Damaged:** CRDO optical DSP line; InnoLight/Eoptolink mix (still grow absolute).

### Base Case (CPO 2027-2029 gradual ramp, ~55% probability)
- **Assumption:** TH6-Davisson and Spectrum-X Photonics adoption concentrated in 1-2 hyperscalers (Meta + 1) through 2027; broader adoption awaits 4th-gen CPO (400G/lane, ~2028+). 1.6T/3.2T pluggables default for scale-out; CPO confined to highest-density TOR switches and scale-up trials.
- **Dominant winners:** LITE, COHR (lasers win in both architectures), InnoLight/Eoptolink (pluggable volume), FN, TSM. AVGO captures CPO premium on specific SKUs.
- **Modestly damaged:** None catastrophic; CRDO optical DSP exposure fades only at 1.6T+.

### Bear Case (CPO delayed to 2030+, ~20% probability)
- **Assumption:** 1.6T/3.2T pluggables (incl. LPO/LRO) + Arista-style XPO/AEC extend the conventional roadmap through 2029-2030; CPO niche for scale-up.
- **Dominant winners:** CRDO (DSP/AEC), MRVL (DSP), ALAB (PCIe-over-optics), InnoLight/Eoptolink, LITE/COHR, FN.
- **Damaged:** AVGO Optical Systems Division revenue trajectory disappoints vs guidance; TSMC COUPE underutilized.

**Asymmetry:** Lumentum and Coherent are positively skewed in *all three* scenarios. Fabrinet wins in all three. The only "binary" longs are AVGO (CPO leadership) and TSM (COUPE).

## 8. Public Company Exposure Table

| Ticker | Relevance | Layer | Rev Sens | Margin Capture | Verified Evidence | Risk | 12-24mo Catalyst |
|---|---|---|---|---|---|---|---|
| **AVGO** | DIRECT | A,B | MEDIUM | HIGH | TH6-Davisson shipping 10/8/25; 3rd-gen 200G/lane; 4th-gen 400G/lane in dev; Meta deployment validated | Hyperscalers self-design | TH6 hyperscaler design wins beyond Meta |
| **MRVL** | DIRECT | A,B | MEDIUM | MEDIUM-HIGH | Celestial AI deal Dec 2, 2025 — *Marvell 8-K: ~$3.25B upfront ($1B cash + ~$2.25B / ~27.2M shares) + up to ~27.2M earnout shares, total ~$6B deal value*; AWS endorsement; 3D SiPh Engine; FY26 Q2 revenue record $2.006B (+58% YoY) | Customer concentration; Celestial integration | Celestial integration into custom ASICs; FY27 guide |
| **NVDA** | DIRECT (hybrid) | A,B,F | LOW | HIGH (vertical) | Quantum-X (2H25) + Spectrum-X Photonics (2H26); $4B into LITE+COHR; uses TSMC COUPE | Pluggable ecosystem also serves | Spectrum-X Photonics shipments 2H 2026; Rubin Ultra scale-up architecture |
| **TSM** | DIRECT | D | LOW | HIGH | COUPE volume production 2026; SoIC 30-40K wpm end-2026; CoWoS 5.5-reticle >98% yield 2026; ~50 SiPh patents filed 2024 | CoWoS capacity contention vs GPU | COUPE-on-CoWoS milestone 2026-2027 |
| **COHR** | DIRECT | A,C | HIGH | HIGH | NVIDIA $2B (Mar 2, 2026); 400 mW CW DFB sampling Sept 25, 2025 (volume Q3 2026); Sherman TX 6-inch InP fab; Spectrum-X partner; multiple CPO demos at OFC 2026 (incl. socketed CPO + own ELS) | InP capacity timing | Sherman TX ramp; NVIDIA purchase realization |
| **LITE** | DIRECT | C | HIGH | HIGH | NVIDIA $2B at $695.31/sh (Mar 2, 2026); only volume supplier of 200G/lane EMLs (50-60% share); +40% EML capacity 2025, +40% 2026; new US fab; S&P 500 add Mar 2026 | EML capacity execution; valuation | 200G EML capacity adds; CW laser ramp; Spectrum-X CPO |
| **FN** | DIRECT | E | HIGH | LOW-MED | 3 active CPO programs; Q3 FY26 record $1.21B (+39% YoY); $32M Raytec stake; Building 10 + Chonburi expansion; NVDA 27.6% of FY25 rev | Margin structure capped; customer concentration | CPO revenue line >$50M/quarter; HPC $150M milestone |
| **INTC** | SPECULATIVE | A | LOW | LOW | Exited SiPh transceivers to Jabil Oct 2023; OCI 4Tbps chiplet R&D; Foundry photonics unproven | Strategic dilution | Foundry photonics customer announcements |
| **CRDO** | INDIRECT (RISK) | B | LOW-MED | MEDIUM | FY26 guide >$800M (+85% YoY); AECs (ZeroFlap), 1.6T optical DSP; Q1 FY26 +274% YoY | Optical DSP displaced at 1.6T+ | AEC scale-up adoption (+); CPO erosion of DSP (-) |
| **ALAB** | INDIRECT | B | LOW | MEDIUM | Q1 2025 +144% YoY; Aries PCIe retimers, Scorpio Fabric, Taurus AECs, PCIe-over-optics | Narrow CPO exposure | PCIe 6.x over optics hyperscaler traction |
| **AAOI** | INDIRECT | C,E | MEDIUM | LOW-MED | Multi-million 800G OSFP order from N. American hyperscaler Dec 2025; Q1 2026 first shipments | Below tier-1 in 1.6T | 1.6T qualification; GM recovery |
| **ANET** | COMPETITIVE | B,E | LOW | MEDIUM-HIGH | Q1 2026: Ullal — CPO "science experiments"; XPO (12 Tb/s, 4× OSFP density, March 2026 launch); strong Broadcom switch attach | If CPO ramps faster than expected | XPO production deployment; AI back-end wins |
| **CSCO** | INDIRECT | B,A | LOW | MEDIUM | Gartner cautious on CPO yield/fiber; AI optical biz ~$500M FY25; Robbins: "imminent but customers want choice" | Lagging in merchant switch | AI orders run-rate (now >$2B FY26) |
| **GFS** | INDIRECT | A | LOW | MEDIUM | US-onshore SiPh foundry; licensed by Ayar Labs; AI/photonics R&D push | Capacity vs TSMC | SiPh customer announcements |
| **AMKR** | INDIRECT | D | LOW | MEDIUM | Advanced packaging for SiPh; PIC test/assembly | Less critical than TSMC | OSAT CPO contract wins |
| **ASX** | INDIRECT | D | LOW | MEDIUM | NVIDIA CPO partner; SoIC-class capabilities | TSMC captures upside | Spectrum-X CPO production support |
| **CLS** | INDIRECT | E | MEDIUM | LOW-MED | Hon Hai-aligned NVIDIA systems integrator; AI server ramp | Lower CPO content than FN | NVIDIA Spectrum-X system shipments |
| **JBL** | INDIRECT | E,A | LOW | LOW-MED | Acquired Intel SiPh transceivers 2023; Ayar Labs ELS modules; broad CM exposure | Diversified business dilutes CPO signal | SiPh transceiver revenue disclosure |
| **FLEX** | INDIRECT | E | LOW | LOW | Broad CM exposure; less optical-specific | Limited direct CPO signal | Hyperscaler EMS wins |
| **AMD** | INDIRECT | A,F | LOW | MEDIUM | $280M SiPh R&D center in Taiwan (proximity to TSMC); MI400/MI500 scale-up TBD | Scale-up architecture undisclosed | MI400 scale-up disclosure; UCIe optical I/O |

## 9. Consensus Mistakes (Junior-Analyst Traps)

1. **Conflating CPO with NPO / NVIDIA Photonics with strict CPO** — counts Spectrum-X as "CPO adoption" when it is hybrid; conflates announcements with deployments.
2. **Treating press releases as adoption evidence** — Bailly was "delivered" March 2024 (Broadcom PR); Meta's actual fleet was 15 switches at ECOC 2025.
3. **Ignoring pluggable roadmap extension** — 1.6T OSFP-XD is 92% of 2025 hyperscaler procurement; 3.2T on OSFP-XD targets ~2027-2028. McKinsey: 1.6T shortfall 30-40% through 2029 (demand exceeds supply even with CPO contribution).
4. **Overestimating near-term attach rates** — LightCounting and Cignal AI explicitly state CPO will not materially affect pluggable shipments in the next 3 years.
5. **Misreading serviceability resolution** — TH6-Davisson resolved the field-replaceable laser objection with ELSFP modules; both sides of the prior debate are now stale.
6. **Misattributing SiPh IP moats** — Intel exited transceivers; TSMC patent filings now outpace Intel's; Broadcom has the production-ready CPO ASIC.
7. **Ignoring merchant silicon displacement risk — but selectively** — partially real for CRDO at 1.6T+ optical DSP; *not* real for ALAB (PCIe/CXL); *not* real for MRVL (custom silicon + Celestial scale-up).
8. **Treating module assembly revenue as high margin** — Fabrinet revenue prints look spectacular but gross margins ~12-13%.
9. **Treating TAM growth as revenue capture** — SiPh TAM at $9.65B by 2030 (per MarketsandMarkets) does not equate to any one name's revenue.
10. **Ignoring thermal/yield/test complexity** — Gartner correct that 1,000+ fiber attaches per CPO package is a real learning curve. CoWoS-class yield took 5+ years.

## 10. Bull / Base / Bear Risk-Weighted Scenario Table

| | **Bull** (25%) | **Base** (55%) | **Bear** (20%) |
|---|---|---|---|
| **Core assumption** | CPO replaces pluggables at 1.6T+ scale-out by 2027 | CPO and pluggables coexist; CPO concentrated in top-of-stack + scale-up | 1.6T/3.2T pluggables + LPO extend roadmap to 2030+; CPO niche |
| **Adoption timeline** | 2026-2027 broad ramp | 2027-2029 gradual ramp | 2030+ only |
| **Catalysts** | Meta production scale-out on TH6; AWS/MSFT adoption disclosed | TH6 hyperscaler wins continue (Meta+1); Spectrum-X ramps 2H26 | LPO MSA matures; 1 pJ/bit LPO (Adtran-class) proves manufacturable |
| **Most positively exposed** | AVGO, LITE, COHR, TSM, FN | LITE, COHR, TSM, FN, AVGO (modest) | LITE, COHR, CRDO, MRVL, FN, InnoLight (HK) |
| **Most at risk** | InnoLight/Eoptolink mix, CRDO optical DSP, AAOI pluggable | None acute (coexistence) | AVGO Optical Systems guidance; TSM COUPE utilization |
| **Revenue inflection** | AVGO OSD >$5B 2027; LITE+COHR DC photonics >$10B | Mid-teens optical sector growth through 2028 | Pluggable dominates; CPO <10% of optical $ |
| **Margin impact** | AVGO GM +200-400bps; LITE/COHR mix shift up | LITE/COHR GM up modestly; AVGO neutral | DSP vendors maintain margins (CRDO/MRVL) |
| **Key invalidation** | If 1.6T pluggable shipments still grow YoY in 2027 | If Bailly fleet <100 switches across hyperscalers by mid-2027 | If TH6-Davisson achieves >10 hyperscaler design wins |
| **Actionable** | Long AVGO, COHR, LITE, TSM, FN | Long LITE, COHR, TSM, FN; selective AVGO | Long LITE, COHR, CRDO, MRVL; short AVGO Optical premium |

## 11. Final Investment Conclusion

**Recommended positioning (base-case weighted, 12-24 month horizon):**

1. **HIGHEST CONVICTION LONG: Lumentum (LITE) and Coherent (COHR).** Win in all three scenarios. They sell lasers whether the laser sits inside a pluggable, as an ELS module, or in a remote laser module. NVIDIA's $4B commitment in March 2026 is the strongest possible scuttlebutt confirmation that the laser is the chokepoint. **Add threshold:** a quarter where Lumentum's 200G EML revenue line exceeds 25% of datacom laser revenue (already targeted by end-2026 per mgmt). **Trim threshold:** clear evidence of 6-inch InP overcapacity emerging at Coherent's Sherman TX fab.

2. **HIGH CONVICTION LONG: Fabrinet (FN).** Wins in all scenarios; valuation more demanding. **Add threshold:** when CPO revenue line item crosses ~$50M/quarter. **Trim threshold:** if HPC program transition slips a second quarter.

3. **HIGH CONVICTION LONG: TSMC (TSM ADR).** COUPE chokepoint + CoWoS leadership. **Add threshold:** incremental COUPE capacity announcements at Symposium 2027. **Trim threshold:** Samsung or UMC achieves credible 200G/lane SiPh production qualification (Samsung's stated 2029 turnkey CPO is too late to threaten).

4. **MEDIUM CONVICTION LONG: Broadcom (AVGO).** TH6-Davisson is real, but most of AVGO's value is non-CPO (VMware, mainframe security, networking, Tomahawk core). Buy AVGO for the broader story; do not pay a "CPO premium."

5. **PAIR: Long COHR/LITE vs short richly-valued pure pluggable transceiver names** (selective; not InnoLight/Eoptolink, which still grow in absolute dollars — focus on weakest specific transceiver names rather than the category).

6. **AVOID shorts on CRDO and MRVL.** Despite theoretical displacement by CPO, both have multi-year growth runway: CRDO from AEC (copper retention in scale-up is a *positive*), MRVL from custom silicon + Celestial scale-up. Pluggable extension is the bear case for CPO but the *bull* case for these names.

7. **NEUTRAL / monitor: ANET, CSCO.** Arista's XPO ten-year-run thesis is sincere but partly hedging; XPO at 12 Tb/s is impressive but introduces a new proprietary form factor that hyperscalers may resist. Watch XPO procurement signals; if Microsoft or Google qualify XPO, ANET re-rates positively.

8. **AVOID as the "CPO play": INTC and AAOI.** Intel exited SiPh transceivers to Jabil; foundry photonics unproven. AAOI is mid-tier pluggable, late to 1.6T qualification.

**Key 12-24 month invalidation signals to monitor for our base case:**
- (Bull-side risk) Meta announces Bailly fleet expansion beyond the 15-switch test cohort to >100 production switches → upgrade conviction on AVGO.
- (Bear-side risk) 2H 2026 200G EML supply *un-tightens* (LITE and COHR raise inventory commentary) → downgrade lasers; suggests pluggable demand softening.
- (Architecture branch) NVIDIA Rubin Ultra scale-up publicly committed to "NVLink-over-fiber" using CPO/optical I/O → very bullish; LITE/COHR/AVGO/FN all benefit. If Rubin Ultra extends NVLink on copper/AECs through Kyber, CPO scale-up thesis pushes out 2 years.

## Caveats / Source-Quality Notes

- Some figures (TSMC SoIC capacity, hyperscaler capex breakouts) are from secondary sources (Commercial Times via Borecraft, CreditSights, TrendForce, FT-compiled summaries) — directionally correct but not precise.
- Meta Bailly results are from Amiralizadeh et al. (ECOC 2025); we did not fetch the paper directly. Verbatim quotes routed via Next Platform and Semianalysis, both of which had paper access.
- "Production-proven" language is from Broadcom (Margalit), *not* a Meta production-rollout commitment. Meta has not publicly committed to broad CPO production beyond the 15-switch characterization cohort.
- NVIDIA Quantum-X / Spectrum-X power numbers (~9W/800G) are early NVIDIA disclosures; the gap to Broadcom TH6-Davisson (~3.5W/800G) may narrow with future revisions.
- Adtran's 1 pJ/bit LPO is a vendor announcement (OFC 2026), not deployed at volume.
- Forward-looking dates (TH6-Davisson production ramp, Spectrum-X Photonics availability, Rubin shipping 2H FY27 per NVIDIA 10-Q) are vendor-stated and subject to slippage.
- We had no access to private supply-chain scuttlebutt or non-public hyperscaler design wins.
- The 25/55/20 bull/base/bear weights reflect our judgment, not a survey or external source.
- Hyperscaler capex aggregates differ across sources ($600B Big-5 per CreditSights vs. $725B Big-4 per FT/Tom's Hardware), reflecting timing of revisions and different definitions.