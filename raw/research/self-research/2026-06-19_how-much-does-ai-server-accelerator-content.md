# AI-Server PCB + CCL Content Uplift — Structural-vs-Cyclical & Cleanest Listed Exposure

> *Tier-3/4 discovery synthesis (web-sourced, 2026-06-19). Trade-press, sell-side relays, and vendor blogs only — no primary filing grounds any figure here. Generates verification questions; **not citable as vault fact** until confirmed at primary sources per Section 2.2 source hierarchy. Maps onto and extends [[pcb-interconnect-substrate-chokepoint]] (S166).*

## 1. Verdict

AI servers carry **materially more PCB content than traditional servers, and the value-uplift outruns the unit-uplift** — TrendForce pegs AI at ~17% of 2026 server *units* but ~74% of server *value*, with AI-server revenue rising +30%+ into 2026 ([TrendForce](https://www.trendforce.com/presscenter/news/20251030-12762.html), Tier 4 ✓). The lift is real and structurally driven: rising SerDes speed (56G→112G→224G PAM4) forces more layers and lower-loss laminate on a roughly annual, architecture-locked ratchet — Morgan Stanley's Rubin BOM teardown puts per-*rack* high-end PCB content up **+233% ($35,100 → $116,700)**, alongside MLCC +182% and ABF +82% (Tier 3 sell-side, multi-relay, math-consistent). **But the durable margin does not sit in the board.** Board fabrication is the most substitutable, best-capitalized, fastest-fragmenting link — China is closing the quality tail at speed (Victory Giant 1.7%→13.8% of AI/HPC PCB share in one year; a mainland CCL maker, Shengyi, already through NVIDIA's M9 gate as of Dec 2025). Durable value **migrates upstream of the board** into a handful of physics-/yield-/concentration-gated material nodes — low-loss glass cloth (Nittobo ~90% T-glass), HVLP copper foil (Mitsui Kinzoku), low-Df resin, ABF film (Ajinomoto >95%), and FCBGA substrate (Ibiden-led). The clinching tell: NVIDIA is reaching *past* board and CCL makers to lock glass cloth and HVLP foil directly — a buyer defending the *material* node. **Net read: the per-unit content lift is durable (a physics + yield moat); the unit-volume leg rides AI-capex cyclicality. Cleanest listed exposure splits by axis — board-fab names (WUS, Victory Giant, TTM) get the volume + mix uplift but compete the margin away; the durable-margin names sit upstream in Japan/Taiwan materials and substrate (Nittobo, Mitsui Kinzoku, Ajinomoto, Ibiden) — most of which are access-gated or only reachable through diversified conglomerates.**

---

## 2. The value chain (downstream → upstream)

```
DOWNSTREAM (cyclical demand) ─────────────────────────────► UPSTREAM (durable scarcity)

Hyperscaler capex          NVIDIA rack         Board fab (PCB)      CCL / laminate        Material inputs           IC substrate
~$600B 2026 (+36%)    →    GB300 / Rubin   →   "quality-but-     →  Megtron M7→M10    →   • Glass cloth         →  ABF film (Ajinomoto
~75% AI-tied              NVL72 rack          competitive"         (CCL = 30–40% of      Nittobo ~90% T-glass       >95%) → FCBGA
                          PCB +233%/rack      China closing        board cost)           • HVLP Cu foil             (Ibiden-led ~35%
                          (MS teardown)       the tail fast        EMC/TUC/ITEQ/         Mitsui ~98% ultra-thin     high-end; top-5 ~82%)
                                              WUS/VGT/TTM/         Shengyi/Doosan        • Low-Df resin (SABIC
                                              Unimicron/Zhen Ding                        PPE ~70%; Resonac/MGC)

  ◄──── revenue tracks unit volume (reverts in a pause) ────┤├──── margin tracks supplier concentration (sticky) ────►
```

**The inversion:** value-per-dollar of difficulty rises as you move *up* the chain. The board is where the visible engineering happens (high-layer-count any-layer HDI, sequential lamination, compounding yield-loss), but it is contested by ~a dozen credible fabricators with active capex. The scarce, single-/few-supplier nodes — glass weaving capacity, HVLP foil yield, ABF film chemistry — set the real gate. This is the same GOES-vs-transformer / chokepoint-quality-gradient logic the vault applies elsewhere (physics > precision-manufacturing > integration).

---

## 3. Analysis by angle — who owns what, where the durable value sits

### 3.1 The BOM delta is real; the dollar figures are vendor-grade *(Angles 1, 10)*

- **Layers:** traditional dual-socket server boards ~12–16 (can sit 8–12); AI training/accelerator boards 20–40, with switch/backplane boards higher. The "average AI-server PCB ~18 (2023) → ~32 (2025)" figure (+78%) reads as a leading-edge mix, not a true fleet average (Tier 4, [Hil Electronic](https://hilelectronic.com/the-ai-server-pcb-revolution-of-2026/) / [UGPCB](https://www.ugpcb.com/news/trade-news/pcb-pcba-cost-ai-server/)).
- **BOM share:** PCB rises from ~2–3% of a traditional-server BOM to ~6–8% in an AI server (GPU+HBM dominates) → a supportable ~2–4× pull-through, with "3–4×" at the upper bound (Tier 4).
- **Solid vs soft:** the *direction* is verified (value-uplift > unit-uplift; high-layer/AI-HDI is the fastest-growing PCB segment; Prismark PCB market $85.1B 2025 → $95.7B 2026 ✓). **Soft / don't quote:** ~$1–2k PCB/card, the 2–3%→6–8% share, the "~32-layer average." **Weakest [unverified]:** the "50–60× content" multiple (Angle 10 — reads inflated; independent estimates run single-to-low-double-digit×) and any single GB300 layer count (one source self-contradicts 28–34 *and* 22).
- **Scope gap (Angle 10):** the vendor narrative jumps M7→M9/M10 and skips M8 — the actual current-volume workhorse.

### 3.2 CCL grade migration is the compounding lever — and it's geometric *(Angles 2, 6, 11)*

- **Driver:** insertion-loss budgets, not board area. As links climb to 224G PAM4, the resin/glass system must absorb less signal, forcing migration up the Megtron-style M-grade ladder. **Corrected Df points:** M6 ≈ 0.002 @1GHz, M7 ≈ 0.0015, M8 ≈ 0.0018 @10GHz — frequency-dependent, so read rankings not point-values ([Panasonic](https://industrial.panasonic.com/ww/products/pt/megtron/megtron7), Tier 1 vendor; [nextpcb](https://www.nextpcb.com/blog/guide-to-panasonic-megtron-8), Tier 4). **M9 (Q-glass) already ships into Rubin; M10 is in qualification targeting Df <0.002 at 448G+** — per Ming-Chi Kuo, NVIDIA + WUS jointly testing M10 with HVLP5 foil + Q-glass ([tspasemiconductor](https://tspasemiconductor.substack.com/p/perspective-on-serdes-and-cpo-pcb), Tier 3).
- **ASP step-up (single Tier-4 source, illustrative):** M6 ≈ 3–5× FR-4, M7 ≈ 6–9×, M8 ≈ 10–15×, M9 ≈ 15–20× ([hilelectronic](https://hilelectronic.com/pcb-manufacturing-cost-2026/)). Treat the top-end multiples as marketing; published low-loss-laminate premiums more typically land ~3–10× FR-4. CCL is ~30–40% of a multilayer server-PCB's cost, so grade migration re-rates dollar content even at flat volume.
- **Why durable:** supply is scarce and qualification is per-generation and NVIDIA-gated — high grades resist deflation while commodity M4/FR-4 stays over-supplied (Tier 3, [Lighthouse Canton](https://www.lighthouse-canton.com/insights/ccls---the-invisible-bottleneck-long-term-investing-thematic)). **The load-bearing risk is the per-gen reshuffle** — a supplier losing a node loses the ASP (maps to the EMC↔Doosan Rubin reshuffle).
- **Cleanest listed high-end CCL exposure:** **Elite Material / EMC (2383 TT)** — #1 AI-server CCL, ~22% high-speed-segment share, +53% YoY ([Prismark](https://www.prismark.com/post/ccl-market-update-october-2025-2024-market-rebound-driven-by-high-speed-and-ai-demand), Tier 3 ✓); **Taiwan Union / TUC (6274 TWO — TPEx, not .TW)**; **ITEQ (6213 TT)**; **Shengyi (600183 SH)** — the CCL *parent* (distinct from listed Shengyi Electronics PCB subsidiary), ~14% global share, NVIDIA M9-qualified Dec 2025. **Doosan (000150 KS)** is a *diversified holding company* (exposure via Electro-Materials division, not a pure-play), reportedly "poised to secure" the Rubin CCL socket after an EMC GB300 qualification failure ([Digitimes](https://www.digitimes.com/news/a20251121PD242/doosan-ccl-nvidia-emc-rubin.html), Tier 4 — `[unverified]`, the per-gen-reshuffle live case).

### 3.3 The chokepoint is upstream of the laminator *(Angles 3, 6, 11)*

Within a low-loss CCL, the laminator's own conversion is the *minority* of value: **copper foil ≈42%, resin ≈26%, glass cloth ≈19%, other ≈13%** ([TrendForce](https://insights.trendforce.com/p/glass-fiber-cloth-shortage), Tier 3 ✓ — methodology-dependent; an alternative cut is foil ~63% / glass ~10% / resin ~7%, but both keep the three materials above conversion, so the "upstream > laminator" conclusion is robust to the split). Laminators are comparatively fragmented and expanding (Panasonic, EMC, ITEQ, TUC, Shengyi, Doosan, Resonac all adding capacity); NVIDIA multi-sources them. The three binding upstream constraints:

| Node | Owner / concentration | Structural durability |
|---|---|---|
| **Glass cloth** | **Nittobo ~90% T-glass, 60–70% NER-glass**; new capacity not before mid-2027; +20% (Aug'25) +20–30% (Apr'26) ([TrendForce](https://insights.trendforce.com/p/glass-fiber-cloth-shortage) ✓) | **Highest — capacity-lead-time-bound.** But on a defined fade clock: Nittobo tripling capacity, outsourcing ~20% to Nan Ya by 2027 ([TrendForce](https://www.trendforce.com/news/2025/11/28/news-nittobo-expands-glass-fiber-output-with-nan-ya-nan-ya-to-handle-20-by-2027-amid-ai-surge/)). Other entrants (Asahi Kasei, Taiwan Glass, Fulltech, Hong Ho) lack premium scale. **`Shin-Etsu` as a glass-cloth entrant is [unverified] — likely misattribution; drop or verify.** |
| **HVLP copper foil** | **Mitsui Kinzoku ~98% ultra-thin / ~60% HVLP2+**; trio Mitsui/Furukawa/Fukuda (or Solus) ~61% revenue. Goldman: HVLP3+ runs **28–39% effective shortfall 2026–28** (Tier 3 ✓) | **High — yield-bound.** ~2 tons of low-end capacity convert to ~1 ton of HVLP grade (capacity ~halves per roughness-class upgrade — market intel, *not* Goldman). |
| **Low-Df resin** | **SABIC ~70% of high-purity PPE (NORYL SA9000 backbone of M4–M7)** | **Lowest of the three — concentration real but event-exposed.** The SABIC Jubail facility went offline **April 7, 2026 (IRGC strike), 6–9-month recovery** ([AtlasPCB](https://www.atlaspcb.com/news/news-sabic-ppe-resin-pcb-laminate-shortage-may-2026/), Tier 4) — but SABIC was *concurrently expanding* PPE capacity, so 2026 scarcity is an **exogenous geopolitical shock, not proof the tier can't add supply.** MGC + Asahi Kasei are smaller backups. **Resonac/MGC raised CCL+prepreg ~30%, effective March 1 2026** ([Resonac/Nasdaq](https://www.nasdaq.com/articles/resonac-increase-sales-prices-copper-clad-laminates-prepregs-30-effective-march-1), Tier 1–2 ✓). |

**Verdict:** the laminator is not the chokepoint; durable scarcity is single-source upstream — **rank Nittobo glass (lead-time) ≈ Mitsui foil (yield) > SABIC resin (event-exposed).** ⚠ **Vault reconciliation flag:** the S166 page pairs *"Resonac HVLP copper foil"* — but the better-supported HVLP-foil owner is **Mitsui Kinzoku**; Resonac is primarily a CCL/prepreg maker. Worth correcting at the next page refresh.

### 3.4 Board-fab capability (any-layer HDI) is a real near-term moat — but the shallower one *(Angle 4)*

GB200-class NVSwitch boards are described as any-layer HDI (ELIC) at 32–40 layers, 4–5 sequential laminations, UV-laser microvias <75µm, large-format panels >400mm — capability ~"a handful of fabricators" hold. The genuinely load-bearing mechanism is **compounding yield-loss** (a defect on any inner layer scraps the whole high-value panel). All Tier 3 vendor-blog (NextPCB/UGPCB/iamfabian); flag as `[unverified]`: the "±25µm backdrill" (implausibly tight), "~40% of factories can't make server boards," "one hand" of fabricators, Zhen Ding "~10 new plants," and the garbled "Kishin" supplier name. **Cleanest listed:** Zhen Ding (4958 TW — largest PCB maker by revenue), Unimicron (3037 TT), WUS, Compeq (2313 TW), Victory Giant (300476 SZ), TTM (TTMI), AT&S (ATS AV), Meiko (6787 JP). Zhen Ding guided 2026 capex ~US$1.58B (+60% YoY) — now a floor (signaled raise to NT$80bn+).

### 3.5 Listed AI-PCB exposure map *(Angle 5)*

- **WUS Printed Circuit (002463 SZ / HK):** datacom >75% of revenue H1'25; HPC/AI guided **>40% of revenue by 2026** ([Digitimes](https://www.digitimes.com/news/a20251212PD213/wus-pcb-revenue-hpc-2026.html) ✓). Note datacom ≠ AI-specific (different baskets). *Vault: S166 killed the activist deck's "~45% of NVIDIA switch PCBs" claim — do not reintroduce.*
- **Victory Giant (300476 SZ):** **13.8% global AI/HPC PCB share, up from 1.7%** (Frost & Sullivan, IPO-commissioned); FY2025 rev RMB19.3bn (+79.8%), net profit +273%, HDI rev +388%, AI-server PCBs 35%→60% of revenue ([SCMP](https://www.scmp.com/business/banking-finance/article/3350801/chinese-circuit-board-supplier-victory-giant-jumps-hong-kong-share-debut) ✓). Direct NVIDIA supplier; fastest share-gainer. ⚠ `[developing, non-supply-chain]`: a June-2026 CEO-scandal headline.
- **TTM Technologies (TTMI):** cleanest US-listed disclosure — **Data Center Computing + Networking = ~36% of FY2025 revenue** (total net sales $2.9bn, +19% *company-wide* — the segment grew much faster: DC computing +57% Q4) ([TTM 4Q-FY2025](https://www.globenewswire.com/news-release/2026/02/04/3232498/0/en/TTM-Technologies-Inc-Reports-Fourth-Quarter-Fiscal-Year-2025-Results.html) ✓). Blended with ~46% aerospace/defense.
- **Substrate tier (durable, lower-disclosed AI%):** **Ibiden (4062 JP)** — leading FC-BGA maker (**~35% of the *high-end* segment, NOT 70–80%** — the latter contradicts the top-5 ≈74–82% total), ¥500bn (~$3.3bn) FY2026–28 substrate capex (board-approved, partly customer-prepaid). **Unimicron (3037 TT)** — AI ~50–60% of 2026 revenue (substrate/ABF-heavy). **Nan Ya PCB (8046 TT)** ABF sold out. **AT&S (ATS AV)** — €500m EU-Chips-Act funding for Leoben FC-BGA `[unverified specifics]`. Concentration: Unimicron + Ibiden + AT&S + Nan Ya PCB + Shinko ≈ **74% of global ABF**.

### 3.6 Switch / networking line-cards = a parallel, additive demand vector *(Angle 8)*

AI fabrics scale networking *faster* than compute — every switch generation doubles bandwidth and forces a board re-spin independent of the GPU cycle. Broadcom Tomahawk 5 = 51.2 Tbps / 64×800GbE ✓; Tomahawk-6 tier moves to 1.6T / 224G SerDes (IEEE 802.3dj ~2026). Switch/networking boards reportedly reach **44 layers on Q-glass with HVLP4/5 foil** — at/above accelerator stackups. **Same upstream-migration logic:** the durable node is low-loss CCL + glass + foil, not the board. **Corrections to carry:** LightCounting "1.6T → $15B by 2030" is *not in source* (actual: 1.6T chipsets >$2B in 2026); the "M9Q part-number list" (EM-896K3, DS-7409DYQ, R-5797Q…) is unverified SKU-grade detail; top-four CCL (Kingboard/Shengyi/EMC/Nan Ya) ≈ 49.7% (EMC is *in* the four; Doosan is *not*).

### 3.7 Rack-scale economics — the Morgan Stanley teardown *(Angles 7, 9)*

⚠ **Attribution: the per-rack dollar figures are Morgan Stanley (~May 2026), not SemiAnalysis** (which covers the co-design *qualitatively*). Both Tier 3. The teardown ([Bitget](https://www.bitget.com/news/detail/12560605422208) and relays, math-consistent):

- **PCB content +233% per rack: ~$35,100 (GB300) → ~$116,700 (Rubin VR200 NVL72)**; full-rack ASP ~doubles ($3.99M → ~$7.8M), with PCB the steepest line (MLCC +182%, ABF +82%, power +32%, cooling +12% — the cross-component breadth itself argues *architecture-driven, not PCB-only spike*).
- **New board types:** a 44-layer **midplane** (~$1,500/unit, ~18/rack — replaces internal cabling) + **ConnectX modules** (~$270/unit, ~72/rack) ≈ +$46,400 of net-new content absent on GB300.
- **Per-gen cadence:** compute board 22L/M7 → 26L/M8; switch tray 24L → 32L; foil HVLP2 → HVLP4 — ~one grade + ~4–6 layer step per generation. **Read board-by-board** (compute ~26L vs backplane 78–104L) — a single "Rubin layer count" is misleading.
- **`[unverified]`/forward:** the 2.3× board-area, 16–20 vs 28–36 layer, $1,970/$204 per-m², the HVLP2→4 exact step, Rubin Ultra "78-layer" (suspiciously clean 3×26) / "104-layer" disagreement, M10/448G. **M9 0.0007 vs M10 <0.002 Df is internally backwards unless quoted at different frequencies.**

### 3.8 China closing the quality tail — competitive-response risk *(Angle 12)*

~20 mainland firms announced >RMB80bn of expansion (AVARY/WUS/Shennan >RMB40bn; Pioneer RMB11bn) aimed at the high-layer tail. **The crossed gate:** Shengyi's M9 ("S9"-branded) passed NVIDIA Rubin/GB300 qualification **Dec 2025** — so the upstream moat is now better framed as **scale / yield / byproduct economics / incumbent displacement, not an uncrossed M9 qualification wall.** ⚠ **Definitional flag:** "China PCB share 34.9%→37.6%" is *mainland-owned-makers'* share, **not** production-located share (~55%). **Verdict:** China closes the board-fab tail fast; durable value-per-board still migrates upstream to M8/M9 CCL, where the competitive response lags ~2+ years (cyclical, back-loaded to 2027–28).

### 3.9 ABF / FCBGA substrate — captures slightly more than half of in-module value *(Angle 13)*

The IC substrate (FCBGA carrier, ABF dielectric) sits *between* silicon and board — finer geometry (~8–12µm L/S production norm, not "single-digit micron"), ~70–100mm square, 14–16+ build-up layers, one per GPU. A (dated, A100-era) teardown put **substrate-level value ~52% vs ~48% PCB-level** within the module. The oligopoly is tighter than commodity PCB (**high-end FCBGA top-5 ~82%, Ibiden-led ~35%**), and **above it sits the single hardest node: Ajinomoto ABF film >95%**. Ibiden's confirmed ¥500bn capex = the structural-not-cyclical tell. ⚠ **Investability change: Shinko (was 6967 JP) delisted June 6, 2025** (JIC take-private) — thins the listed pure-play set to Ibiden + Unimicron + AT&S + Nan Ya PCB, with ABF film reachable only through **Ajinomoto (2802 JP)**, a diversified food/chemicals conglomerate. Demarcation risks (longer-dated): NVIDIA's exploratory **CoWoP** (bypasses ABF substrate) and **glass-core substrates** (now pushed to **2027+** — Samsung 2027 ramp, Intel ~2030 — *widening* the organic-substrate runway).

### 3.10 Falsifiers & risks *(Angle 14)*

1. **Capex air-pocket (demand falsifier, highest-conviction):** uplift rides hyperscaler capex **~$600B 2026 / +36% central** (~75% AI-tied); the $725B/+60–70% figures are the *bullish tail*, not base case. PCB/CCL sits at the cyclical-amplified end (high CCL content per AI server) — demand falls *faster* than units in a pause.
2. **Material-grade plateau (value falsifier):** if signaling tops near 224G or packaging offloads routing, the grade/layer escalator stalls. *Today the constraint is supply, not demand* (Nittobo ~90% T-glass, allocation-only) — but that single-supplier prop is on a defined fade clock (tripling + Nan Ya partner by 2027).
3. **NVIDIA in-sourcing/consignment — label cuts the *other* way:** GB300 *disaggregates* (SXM Puck + Grace BGA only; reverts toward UBB+OAM, opening compute-board build to *more* ODMs) — favorable-to-neutral for board-fabs, not margin compression. The genuine upstream move is NVIDIA **locking HVLP4 foil + T-glass directly** (~1,500-ton 2026 shortfall, Tier 4 estimate) — Framework-12 buyer-defense firing one tier deeper ([[nvidia-supply-chain-commitments]]).
4. **Glass-core substrate disruption (tech falsifier):** real but slower-moving (2027+) than the demand it would reshape — timeline slippage *strengthens* the organic-substrate thesis near-term.

### 3.11 Geography & access lens *(Angle 15)*

| Region | Names | Access |
|---|---|---|
| **Taiwan** (deepest cluster) | Unimicron, Nan Ya PCB, Kinsus, GCE, Zhen Ding, Tripod (board); ITEQ, TUC (CCL) | **Local-market only — no PCB/CCL name carries a US ADR** (only PCB-chain ADR is TSMC) |
| **Korea** (cleanest open access) | **ISU Petasys (007660 KS)** — 18+ layer MLB, AI ~70% of revenue, "global top-3" alongside TTM + WUS (not unambiguous #1); LG Innotek | **KRX freely foreign-investable — cleanest single-name pure-play with open access** |
| **Japan** (durable material nodes) | Nittobo (3110 T), Mitsui Kinzoku (5706 T), MGC (4182 T), Resonac (4004 T), Panasonic (6752 T), AGC (5201 T), Ibiden (4062 T), Ajinomoto (2802 T) | **Fully investable (TSE)** |
| **China** (strongest momentum) | Victory Giant (300476 SZ), Shennan (002916 SZ), WUS (002463 SZ), Shengyi (600183 SH) | **A-shares gated (Stock Connect/QFII); HK proxies the workaround — Victory Giant April-2026 H-share IPO (+57–60% debut)** |
| **US** | **TTM (TTMI)** — only direct US-listed PCB exposure; defense-weighted, DC computing ~28% and fastest-growing | Open |

**Access takeaway:** the durable-margin nodes are disproportionately Japan (open) and Taiwan (local-access only); the highest-AI-mix board names are China (gated → HK proxy). The single hardest chokepoint (ABF film) is reachable only through diversified Ajinomoto.

---

## 4. What to verify at primary sources

Concrete, numbered leads — promote any confirmed item from "structural context to verify at primary" into canon per Section 4.6 discipline:

1. **Ibiden (4062 JP / EDINET)** — confirm the **¥500bn FY2026–28 substrate capex** split (¥220bn Gama + ¥280bn Ono), customer-prepayment terms, and high-end FCBGA share (~35%?) against the filing. *The S166-flagged "Ibiden ingest = promotion path"; cleanest durable-node primary filer.*
2. **TTM (TTMI 10-K/8-K)** — verify **Data Center Computing + Networking = 36% of FY2025 revenue**, the +57% Q4 DC-computing growth, and HLC/UHDI capability claims. Already filing-grade; the cleanest US anchor.
3. **Ajinomoto (2802 JP)** — confirm **>95% ABF film share** framing and test the `[unverified]` ~30% Q3-2026 ABF price-hike rumor (sole source a Medium post) at IR/earnings.
4. **Nittobo (3110 JP)** — verify **~90% T-glass / 60–70% NER-glass**, the capacity-tripling timeline, mid-2027 relief date, and the Nan Ya ~20%-by-2027 outsourcing — the most structurally durable node.
5. **Mitsui Kinzoku (5706 JP)** — confirm **~98% ultra-thin / ~60% HVLP2+ foil** and HVLP4 capacity (~490 t/mo vs ~560 t/mo H2'26 demand). **Reconcile against the S166 page's "Resonac HVLP foil" pairing — Mitsui appears the better-supported owner.**
6. **Resonac (4004 JP) + MGC (4182 JP)** — verify the **~30% CCL/prepreg hike (eff. Mar 1 2026)** at the primary release (already upgraded to Resonac's own filing — confirm scope).
7. **Elite Material / EMC (2383 TT)** — confirm **~22% high-speed CCL share, +53% YoY, record 30%+ gross margin** against TWSE filings (the SWOT/content-mill source is not citable); test the **GB300 qualification-failure / lost-Rubin-socket** narrative.
8. **Doosan (000150 KS / Electro-Materials)** — verify the **"poised to secure Rubin CCL"** win and "GB300 compute-tray supply" at the segment level (it's a diversified holding co., not a pure-play).
9. **Shengyi Technology (600183 SH)** — confirm the **Dec-2025 NVIDIA M9 ("S9") qualification** and ~14% global CCL share — this is the live datapoint tightening the "durable nodes hold to 2027–28" timeline.
10. **Victory Giant (300476 SZ / HK H-share prospectus)** — verify the **1.7%→13.8% AI/HPC share** (F&S is IPO-commissioned/company-adjacent), FY2025 rev RMB19.3bn / +273% NP / HDI +388%, and direct-NVIDIA-supplier status against the HKEX proof.
11. **SABIC PPE outage** — verify the **April 7 2026 Jubail strike**, ~70% high-purity PPE share, and 6–9-month recovery; classify the resin node as **single-source fragility (event-exposed), not durable structural scarcity** — and correct the Indian Chemical News mis-citation (that link is SABIC's *expansion* notice, not the outage).
12. **Megtron Df values & M9/M10 status (Panasonic)** — confirm **M6 ≈0.002@1GHz / M7 ≈0.0015 / M8 ≈0.0018@10GHz**, that **M9 (Q-glass) is the shipping Rubin grade and M10 is in qualification for 448G+** — and the Ming-Chi Kuo NVIDIA+WUS M10/HVLP5 testing lead (fresh primary-verifiable item for the S166 page).
13. **Morgan Stanley Rubin BOM note (paywalled original)** — confirm the **+233% PCB/rack ($35,100→$116,700)**, midplane ($1,500×18) + ConnectX ($270×72), and the MLCC/ABF/power/cooling cross-component spread; **correct the SemiAnalysis→Morgan Stanley attribution** and "per-board"→"per-rack" labeling wherever it propagates.
14. **Shinko delisting** — confirm the **June 6 2025 JIC take-private** (removes the #2 high-end FCBGA name from the investable set; reinforces Ibiden as the cleanest listed substrate exposure) for the chokepoint page's access lens.
15. **Hyperscaler capex** — verify **~$600B 2026 / +36% central** (~75% AI-tied) at GOOGL/MSFT/AMZN/META filings per the standing capex watch; treat $725B/+60–70% as bullish tail. Feeds [[hyperscaler-capex]] + the AI-PCB demand falsifier.

---

*This anchor corroborates and extends the S166 [[pcb-interconnect-substrate-chokepoint]] verdict — durable value migrates upstream of the board to materials/substrate — and surfaces three page-reconciliation items for the next refresh: (1) the **Resonac→Mitsui Kinzoku** HVLP-foil owner correction; (2) the **Shengyi Dec-2025 M9 qualification** tightening the "durable nodes hold to 2027–28" timeline; (3) the **Shinko delisting** thinning the investable substrate set onto Ibiden. The board-fab layer is real-but-competitive demand growth; the deeper, durable nodes are glass cloth (Nittobo), HVLP foil (Mitsui), ABF film (Ajinomoto), and FCBGA (Ibiden). All Tier-3/4 — discovery-grade, not citable as vault fact.*