# Intel note — SemiAnalysis: "US Grid Constraints: Towards 40GW+ of Behind-The-Meter Datacenter by 2028?"

**⚠️ Source-tier correction (read first):** this is **NOT a Twitter thread** — it is a **SemiAnalysis paid research article** (Substack), so the `/twitter-intel` Tier-5 floor does **NOT** apply. Per CLAUDE.md §2.2 the correct tier is **Tier 3 — independent analysis (SemiAnalysis named explicitly): cite, don't treat as fact.** The file was staged in `twitter-notes/` and the skill was invoked on it; this note follows the discovery-only contract but classifies it honestly as Tier 3. Models are SemiAnalysis-proprietary (Energy Model / Datacenter Model / Tokenomics) and **not independently verifiable** — every figure below is a SemiAnalysis estimate.

- **Authors:** Jeremie Eliahou Ontiveros, Sebastian Orejas, Ellie Holbrook, **Dylan Patel** (SemiAnalysis)
- **Date:** 2026-06-26 · **PAID** (the company-specific "Winners & Losers" section is **paywalled / cut off** in this capture — only the names are given)
- **Source file:** `raw/notes/twitter-notes/us-grid-constraints-semianalysis.pdf` (25pp; text-extracted) · also `.html`
- **Engagement (reach, not truth):** 149 likes / 9 comments / 15 restacks

## TL;DR

The US grid **cannot add firm capacity fast enough** for AI datacenter load — generation (not just transmission) is now the binding bottleneck, and **grid headroom goes negative by 2027.** That pushes the largest buyers **Behind-The-Meter (BTM)**: SemiAnalysis models **BTM powering >50% of new US datacenters from 2028+** and the **BTM equipment TAM crossing ~50GW/year by 2029.** The mechanism: only ~15GW/yr of net-new *firm* (ELCC) capacity is being added vs a datacenter buildout going +21GW (2026) → +84GW (2030); renewables/storage add nameplate but little firm ELCC; gas turbine + grid step-up transformer lead times have stretched to **3–4 years** (vs ~18-month norm). Texas (ERCOT) is codifying hybrid on-site-gen + grid co-location via the **Batch Zero** process. This is, in effect, a quantified model of the vault's existing **[[BTM-grid-bypass-workaround]]** thesis.

## Key claims + numbers (all Tier 3 — SemiAnalysis models)

- **Datacenter buildout:** +21GW (2026) → **+84GW (2030)**. `[forward]`
- **Firm capacity added:** barely **~15GW/yr** net-new ELCC, rising toward 20GW+ by end-decade; nameplate additions **<10GW/yr in 2026–27**, picking up 2028+. `[forward]`
- **Grid headroom approaching zero, turns NEGATIVE by 2027** (UCAP basis); **NERC** flags **13 of 23** NA assessment areas with resource-adequacy shortfalls. `[verifiable — NERC 2025 LTRA is a real doc]`
- **PJM 2027/2028 Base Residual Auction:** cleared ~134,478 MW UCAP → **14.4% reserve margin vs 20% target = ~6,517 MW deficit.** `[verifiable — PJM BRA results]`
- **Lead times:** gas turbine + generator step-up transformer (GSU) **3–4 years** (vs ~18-mo historical norm); CCGT build **4–6 years**. `[verifiable-ish — corroborates [[transformer-supply]]]`
- **PJM queue:** ~57GW cleared studies/IAs; since 2020 ~28GW (incl **13.5GW gas**) with executed agreements **terminated before COD** (permitting 29%, supply-chain 23% of milestone changes Jan-2023→Jan-2026). `[forward/analytical]`
- **BTM in-service dates cluster 2027–28** vs grid slipping toward 2030; **BTM equipment TAM >50GW/yr by 2029.** `[forward]`
- **Renewables/storage:** solar + BESS each adding 20GW+ nameplate/yr but **minimal ELCC** (marginal value saturates — Duck Curve / 4hr-BESS saturation). `[analytical]`
- **Uptime relaxation:** Meta targets just **2 nines**, forgoes backup gensets (Prometheus); **Ohio campus designed never to connect to PJM grid**; El Paso + Louisiana built around dedicated utility-scale gas. `[verifiable — at META]`
- **ERCOT Batch Zero:** NPRR1325 + PGRR145 (approved Jun 1 2026, effective Jul 11). Co-location *metering* constructs: **PUN / WLPUN / PCLR**; *sourcing*: **NMA** (existing gen, pre-Sept-1-2025 SB6 trigger) vs **BYOG** (new gen). `[verifiable — ERCOT/PUCT filings]`
- **FERC/PJM reform:** FERC Dec 2025 order → PJM co-location rules + Docket RM26-4 (faster interconnect of loads >20MW); PJM **Expedited Interconnection Track (~10-month)** accepted Jun 12 2026. `[verifiable — FERC]`
- **Named ERCOT co-location deals (~2,885 MW reported):** `[verifiable at the respective filings]`
  - **Crusoe** — Goodnight (NMA): 265.5+260 = 525.5 MW load → ~1 GW IT campus; TCEQ air permit up to 933 MW gas, ~665 MW = **19× GE Vernova LM2500XPRESS** turbines (~35 MW each).
  - **AWS** — Comanche Peak (NMA): **1,200 MW** co-located adjacent to **Vistra's** Comanche Peak **nuclear**; 20-yr PPA, full by 2032.
  - **CyrusOne** — Thad Hill (NMA): 400 MW adjacent to **Calpine's** plant.
  - **CyrusOne / Constellation** — Freestone (NMA): 760 MW potential (380 contracted + 380 option) via **Calpine/Constellation**.
- **Switch Datacenter** closed a multi-billion-$ **performance letter-of-credit facility (2026)** to back take-or-pay grid obligations — example of buyer-funded grid risk. `[verifiable]`
- **Winners/losers (PAYWALLED — names only):** turbine mfrs like **GEV**; fuel-cell + RICE vendors like **Bloom (BE)** + **INNIO**; IPPs like **NRG**. SemiAnalysis "first called **Bloom** in Dec 2024 as the biggest beneficiary." `[opinion — analysis cut off]`
- **Risk flag (SemiAnalysis's own):** "**temporary peak gas turbine orders**" risk + "**surging secondary-market turbine availability**" — a nuance *against* a naive turbine-tightness bull. `[opinion]`

## Named entities

| Entity | Claim | Vault page | Note |
|---|---|---|---|
| GE Vernova (GEV) | Turbine mfr; LM2500XPRESS for Crusoe; "peak gas turbine orders" risk | [[GEV]] | confirms + nuances |
| Bloom Energy (BE) | Fuel cells aggressively secured for onsite gen; "biggest beneficiary" (SemiAnalysis Dec 2024) | [[BE]] | confirms BTM positioning |
| Constellation | Freestone co-location (Calpine/Constellation) | [[CEG]] | nuclear/IPP co-location |
| AWS / Meta / Oracle / Microsoft | BTM/co-location buyers; Meta 2-nines + grid-skip | [[AMZN]] [[META]] [[ORCL]] [[MSFT]] | demand-side |
| Vistra (VST) | Comanche Peak nuclear; AWS 1,200 MW co-lo | none | new-name candidate (IPP) |
| Calpine | Thad Hill + Freestone host gen | none | new-name candidate (IPP, private/merging) |
| NRG | IPP, named winner/loser | none | new-name candidate |
| INNIO | RICE engine vendor | none | new-name candidate (BTM engines) |
| Crusoe / CyrusOne / Switch / Fluidstack / Cipher | BTM datacenter developers | none (Crusoe noted in [[neocloud-moat-durability]] prose) | private |
| OpenAI / Anthropic | the demand drivers (directly + via AMZN/MSFT/ORCL) | none | private |

## Vault cross-reference

- **[[BTM-grid-bypass-workaround]]** — **CONFIRM + EXTEND (strongest).** This article is essentially a quantified model of that page's thesis: grid headroom red by 2027; BTM >50% of new DCs 2028+; the ERCOT **Batch Zero / NMA / BYOG / WLPUN / PCLR** regulatory codification (NEW detail); the ~2,885 MW of named co-location deals; Meta's grid-skip campuses. Materially deepens the page's regulatory + deal-level evidence.
- **[[transformer-supply]]** — **CONFIRM.** GSU transformer lead times 3–4 yrs (vs ~18-mo norm); the "utility pushes a 2027 load-ramp to 2029" mechanism; deferrals = power shortage not demand destruction ("delays headlines overblown"). Aligns with the page's tiered-easing + "book-to-bill not deferrals" falsifier.
- **[[GEV]]** — **CONFIRM + CHALLENGE.** Turbine demand (LM2500XPRESS named) but the **"temporary peak gas turbine orders / surging secondary-market availability"** flag is a counterweight to a turbine-tightness bull — matches the vault's "turbines easier to flex than transformers" read.
- **[[BE]]** — **CONFIRM.** Bloom named SemiAnalysis's "biggest beneficiary" of BTM fuel-cell demand since Dec 2024.
- **[[FCEL]]** — **EXTEND.** Fuel-cell + RICE onsite generation aggressively secured by DC operators = the BTM Modality-2 demand backdrop FCEL sits in (the Fit Energy deal context).
- **[[CEG]]** — **EXTEND.** Constellation's Freestone co-location; nuclear/IPP baseload co-location as a BTM-adjacent structure.
- **[[neocloud-moat-durability]]** — **CONFIRM.** Crusoe Goodnight (merchant-gas, GE Vernova turbines) corroborates the just-added "energy-first narrows but doesn't flip the verdict" read; Meta's owned-gas campuses support "owned power = a better seat at the bottom of the gradient."
- **[[CAT]]** — possible EXTEND (reciprocating-engine / Solar Turbines BTM onsite gen).
- **[[what-could-go-wrong]] / [[forward-edge-tracker]] / [[hyperscaler-capex]]** — CONFIRM the power-as-binding-constraint thesis; the +21→+84GW buildout; nothing *fires* a falsifier (it reinforces the existing not-fired power-shortage state).

## Ingest leads (verify at primary)

1. **GEV turbine order book + peak-order risk** — does the next GEV 10-Q/call show backlog still climbing or the "temporary peak orders / secondary-market availability" softening SemiAnalysis flags? (The single most decision-relevant verify.)
2. **BE (Bloom) data-center / BTM bookings** — next BE 10-Q/call: is the "biggest beneficiary" call showing in firm orders?
3. **Named co-location deals** — verify at primary where a vault name is involved: Constellation/[[CEG]] (Freestone), [[AMZN]] (Comanche Peak/Vistra), [[META]] (Ohio/El Paso/Louisiana grid-skip campuses).
4. **Transformer/GSU 3–4yr lead times** — corroborates [[transformer-supply]] (Tier 3 → already primary-grounded there).
5. **New-name candidates** (watch for 3+ sources / chokepoint-centrality): **Vistra (VST)**, **Calpine**, **NRG**, **INNIO** — IPPs + BTM-engine vendors recurring in the BTM/power-constraint story; **CyrusOne** (BTM developer). None warrant a page yet on this single source.

## Contradictions / red flags

- **Paywall:** the actual differentiated winners/losers calls are **cut off** — only the names (GEV/Bloom/INNIO/NRG) are given, not SemiAnalysis's verdicts. Do not infer the company-level conclusions from this capture.
- **Proprietary, unverifiable models:** every headline number is a SemiAnalysis Energy/Datacenter/Tokenomics model output — Tier 3, cannot be checked against a primary filing. Treat the *mechanism* as credible and the *point estimates* as one analyst's model.
- **Subscription incentive:** SemiAnalysis sells these models — framing leans toward "our model is industry-leading"; weight the analysis, discount the self-promotion.
- **Internal consistency:** the title says "40GW+ BTM by 2028" while the body says BTM TAM ">50GW/yr by 2029" and BTM ">50% of new DCs 2028+" — consistent (stock of BTM by 2028 vs annual TAM by 2029), but note the different units.

## Source-tier verdict (restated)

**Tier 3 (independent analysis — SemiAnalysis), NOT Tier 5.** Do not cite the point estimates as vault fact; use the mechanism + named deals to generate primary-source verification. The strongest, most decision-relevant nuance is the **"temporary peak gas turbine orders / secondary-market availability"** flag — verify at the next GEV refresh. Discovery-only; no canon touched.
