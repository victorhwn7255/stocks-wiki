---
type: tracker
tickers: [ETN, VRT, GEV, TSM, NVDA, AVGO, MRVL, ALAB, AAOI, FCEL, MU, SNDK, CSCO, PLAB, CRWV, NBIS, ORCL, AMZN, MP, LSCC, TDY, AVAV, KTOS, HARMONIC, SANHUA, TUOPU, NOVT, VPG]
last_updated: 2026-07-11
---

# Forward-Edge Tracker — Consensus vs. Vault View

This is the vault's **forward-edge layer**: a curated, cross-domain tracker of the places where the vault's structural read **differs from what the market is pricing**, plus the catalyst that would force a re-rate and the falsifier that would prove the vault wrong. It surfaces in one place the variant views already latent in the three theses' "what would prove this thesis wrong" sections and the chokepoint-quality gradient.

**Why this layer exists.** Primary filings (10-K/10-Q/call) are backward-looking and largely priced by the time they're filed. The edge is not being *first* on public news (a speed game the vault can't win) — it's having a *better structural read* of public information: seeing where a chokepoint is more durable, or a constraint more binding, or a narrative more fragile, than consensus assumes.

**Discipline rule (load-bearing).** "Consensus" is described as a **structural narrative** or via an **observable mechanism** (lead times, interconnection queues, bond yields, order-vs-capacity) — **never** as stock price, market cap, valuation multiples, or analyst price targets (those stay "signal only" in the quarantined `latest-alpha` blocks). Describe-don't-recommend; a reader cannot tell what is owned. Honest-verdict: if the vault view is weak or consensus is right, say so — do not manufacture a contrarian take. **Entry contract: every entry must carry a catalyst AND a falsifier.** No falsifier means it's a hot take, not an entry.

**Sibling register.** [[what-could-go-wrong]] is the vault-level risk register (CLAUDE.md Section 3.20): it holds the **consensus-aligned** risks this page's consensus-divergence contract cannot — where the vault and the market could be wrong together. The two pages may share tripwires but answer different questions (where the vault *differs* vs. where the vault could be *wrong*).

## The three layers (filings vs. alpha)

| Layer | Source | Role |
|---|---|---|
| **1 — Canon (verified)** | 10-K/10-Q/call (Tier 1/2) | Backward-looking ground truth; the backbone that keeps the rest honest |
| **2 — Latest alpha (timely)** | 8-K/conference/news (Tier 1-timely / 3 / 4) | Closes the lag; surfaces catalysts between filings; quarantined, discovery-only |
| **3 — Forward edge (this page)** | The vault's own structural analysis vs. consensus | Where we differ + catalyst + falsifier; the actual alpha |

Layer 2 *feeds* the catalysts here; Layer 1 *verifies or falsifies* an entry (a refresh ingest confirms a catalyst or trips a falsifier). Each entry's "Vault view" and "Falsifier" are primary-grounded (cite a thesis / chokepoint / company page); the "Consensus" line is Tier 3/4 (cite, don't treat as fact).

---

## AI datacenter

### Power infrastructure > compute (the binding-constraint inversion)
**Subjects:** [[ETN]] · [[VRT]] · [[GEV]] · transformer/grid chokepoints — **Durability:** physics + 4-yr transformer lead times (high)

- **Consensus (Tier 3/4):** the market prices the AI build-out as a *compute* story — [[NVDA]] and the chip chain are where the value and the constraint sit; power/electrical is treated as adjacent, late-cycle infrastructure.
- **Vault view:** the binding 2026 constraint has shifted from compute supply to **power infrastructure** — ~50% of planned 2026 US datacenter builds delayed/cancelled on power (not chips); large transformers carry 120–210-week lead times; durable pricing power sits with the under-covered power/electrical chokepoint owners. (per `_thesis.md` + [[transformer-supply]] + [[AIDC-cooling-architecture-transition]])
- **Catalyst / re-rate triggers:** hyperscaler capex guidance naming power as the gating item; utility interconnection-queue data; a power-equipment lead-time/order disclosure at the next refresh. *(latest-alpha + [[hyperscaler-capex]] feed these)*
- **Falsifier:** power constraint resolves faster than expected — new transformer capacity (Cleveland-Cliffs, Korean/Chinese US plants), grid-interconnection acceleration — OR hyperscaler capex decelerates broadly. (per `_thesis.md` "what would prove this wrong" #5 / #7)
- **Last moved:** 2026-06-09 (created).

### Custom silicon redirects capex away from merchant compute
**Subjects:** [[TSM]] · [[AVGO]] · [[MRVL]] · [[ALAB]] vs [[NVDA]] — **Durability:** TSM advanced-packaging/foundry = irreplaceable infrastructure (high); NVDA platform = highest capture but custom-silicon threat

- **Consensus (Tier 3/4):** the market prices [[NVDA]] as capturing the bulk of AI-compute capex behind a durable, widening moat.
- **Vault view:** hyperscaler-captive custom silicon redirects capex flow away from merchant Layer-1 ([[NVDA]]) toward Layer-2 manufacturing ([[TSM]]) and Layer-3 designers ([[AVGO]]/[[MRVL]]/[[ALAB]]) — captive silicon could save hyperscalers "tens of billions annually." [[TSM]] is the more durable beneficiary *regardless of which compute brand wins the share war*. (per `_thesis.md` + [[hyperscaler-custom-ASIC]] + [[NVDA-platform-integration]])
- **Catalyst / re-rate triggers:** hyperscaler custom-ASIC ramp disclosures (TPU / Trainium / MTIA / Maia volumes); NVDA datacenter-compute share + margin trajectory; TSM advanced-packaging allocation between merchant and captive silicon. *(latest-alpha + refresh)*
- **Falsifier:** NVDA's platform integration (CUDA + NVLink + networking) keeps custom silicon niche and merchant-compute concentration holds, OR custom-silicon programs stall technically. (per `_thesis.md` "what would prove this wrong" #8)
- **Last moved:** 2026-06-09 (created); **2026-07-01 (Tier-3 datapoint, latest-alpha layer):** SemiAnalysis/Dylan Patel (Sequoia, 2026-06-30 video-intel note) sharpens *both* sides — the *software* "CUDA moat" is partly disentangling (frontier labs fork their own stacks + models write their own kernels), cutting toward the vault view (custom silicon more viable); BUT the durable NVIDIA moat is **relocated, not gone** — it is *ecosystem gravity* (Chinese open models co-designed for GPUs run poorly on TPUs) + general-purpose GPUs at the "global minimum" while ASICs risk a "local minimum" as model architectures shift, which supports the entry's NVDA falsifier. Net: sharpens the *mechanism*, not a directional move. Tier-3; last_updated unchanged.

### [[AAOI]] — market prices a winner; the structure is a fragile assembler (inverse divergence)
**Subject:** [[AAOI]] — **Durability:** Layer-5 pluggable assembler, "minimally differentiated" (its own 10-K), the vault's most extreme customer concentration (weak); sole optionality = the in-house InP laser (an *unproven* Layer-5 → 4 tier-upgrade)

- **Consensus (Tier 3/4):** the market prices AAOI as a core US AI-optics winner — 800G/1.6T ramp, hyperscaler orders, a raised >$1.1B 2026 guide, and laser/CPO optionality — a structural beneficiary of the photonics supercycle.
- **Vault view (less bullish than consensus):** AAOI assembles the exact pluggable form factor CPO is designed to displace; it is "minimally differentiated," carries the vault's most extreme customer concentration, is still loss-making, and funds growth with heavy ongoing dilution — while leaving CPO displacement of its core *unnamed* in filings. The growth is real but cyclical-demand-driven; the structural position is weak. The bull catalysts (orders, guide, datacenter inflection) are largely **already in the price** — this is the market pricing *durability* the structural read doesn't support, not un-priced upside. (per [[AAOI]] Thesis role + Caveat #9 Layer 4/5 straddle + [[cpo-integration]] + [[CPO-platform-battle]])
- **Catalyst / re-rate trigger (the one genuinely un-priced lever):** merchant **laser / ELS revenue** appearing in a 10-Q — the in-house InP laser becoming a standalone CPO/ELS product (a Layer-5 → Layer-4 tier-upgrade), so far evidenced only at conference (OFC 25dBm ELSFP + a live 6.4T on-board-optics demo; a ~350% InP-fab expansion to 2027). *(latest-alpha + the next refresh feed this)*
- **Falsifier (of the cautious vault view):** that merchant laser/ELS line becomes material AND AAOI rides CPO as a *laser supplier* rather than a displaced *module maker* — re-rating it toward a differentiated Layer-4 component-with-IP and vindicating the "winner" framing. (Conversely the vault view is confirmed if CPO eats the pluggable core while merchant laser stays ~0% and dilution continues — per [[AAOI]] Open questions #4 / #5 / #6.)
- **Last moved:** 2026-06-09 (created).

### [[FCEL]] — market now prices the data-center contract before it exists (inverse divergence, 2nd instance)
**Subject:** [[FCEL]] — **Durability:** the BTM grid-bypass terrain is real (demand pull from grid-constrained data centers, high) but FCEL's own position on it is pre-conversion — narrative-outrunning-proof, the weakest seat at the [[BTM-grid-bypass-workaround]] chokepoint (vs [[BE]] converted, [[CAT]]/[[GEV]] shipping at scale)

- **Consensus (Tier 3/4):** post-Q2-FY2026, the narrative flipped bullish — sell-side upgrades and the retail conversation now treat a significant data-center contract before fiscal year-end as the expected outcome, with "the next Bloom Energy" as the standing frame; the proposal pipeline (4 GW, 89% data-center) is read as demand already secured.
- **Vault view (less bullish than consensus):** the order-vs-capacity test applied to FCEL itself says the conversion is an open question, not a likelihood — 4 GW is *submitted proposals* while contracted backlog FELL 9% and revenue fell 5%; zero firm hyperscaler orders at primary (criterion 4 falsified since S47); the funding model is ATM equity issuance, with the shelf machinery renewed the same day as the Q2 earnings; and the capacity chicken-and-egg is structural — the average proposal (130 MW) exceeds a full year of current production (~100 MW/yr), while the expansion that would fix it is self-gated on the very backlog that hasn't arrived. Even a landed contract starts a BE-path test, not a BE outcome (1:25 scale gap; buyer alternatives shipping today). The market is pricing the contract before it exists. (per [[FCEL]] Thesis role + narrative-outrunning-proof section + Q2 FY2026 snapshot + [[BTM-grid-bypass-workaround]])
- **Catalyst / timeline:** management's own dated test — convert submitted proposals into contracted backlog **within fiscal 2026 (by October 31)**; interim read at the Q3 FY2026 report (~September); the Q4 report (~December) is pass/fail. *(latest-alpha feeds this; the 2026-06-13 run found no contract anywhere in the 90-day window)*
- **Falsifier:** a signed, material data-center contract (named counterparty or sized capacity) by fiscal year-end with backlog turning up — the conversion is real, the cautious read was wrong, and FCEL moves onto the BE trajectory test. Conversely the vault view is confirmed if FY2026 closes with the pipeline still unconverted while ATM dilution continues — at which point "next Bloom" was a narrative, not a thesis. (per [[FCEL]] Open question #1)
- **Last moved:** 2026-06-13 (created, at the S153 Q2 FY2026 refresh + same-day latest-alpha/last30days runs).

### Memory shortage — market prices the boom, not the cycle clock
**Subjects:** [[MU]] · [[SNDK]] · the memory-tax victims ([[CSCO]] · [[PLAB]] · device makers) — **Durability:** the HBM reallocation is structural near-term (cleanroom physics, 12-18 months); the standard-memory windfall is cyclical by precedent

- **Consensus (Tier 3/4):** memory tightness is read as a memory-makers' bull story with a long runway — sell-side talk of the rally extending "past 2028"; the shortage framed as proof of durable AI demand; the shipment damage (IDC: smartphones −12.9%, PCs −11.3% in 2026) treated as a side note.
- **Vault view (the cycle-clock half is unpriced):** the same mechanism that makes the boom is already running the bust sequence — the **spot-vs-contract divergence** (DDR5 spot/retail cracked ~30% in segments by late March while contract rose +50-63%) shows the consumer demand leg breaking under the price tax; MLCC channels show documented double-booking with ODM orders falling; the 2017-18 precedent (Yageo −34.5% in the unwind) is the template. The shortage is real AND it is demand-destroying — both halves are true, and the second is not in the narrative. (per [[memory-shortage-winners-losers]] + [[HBM-oligopoly]] + [[MLCC-oligopoly]])
- **Catalyst / timeline:** **MU Q3 FY2026 landed (June 24, 2026)** — the maker side *hardened*, not softened: supply now sets shipments (demand >> supply into 2028), HBM TAM $100B pulled to 2027, and the 10-Q's SCA price-*floors* lock margins "well above any past-cycle peak" → on the *maker* axis this cuts toward the long-runway consensus; the downstream cycle-clock (consumer-shipment damage + contract-price rollover) is still pending. **Both top MLCC makers' full-year actuals also IN** ([[MURATA]] #1 S169 + [[TAIYO]] #3 S170: server-capacitor +85-90% confirmed, the "no industry-wide MLCC hike" double-confirmed, prices still falling — the MLCC half of this entry is primary-grounded at both ends of the oligopoly, and [[MLCC-oligopoly]] is now a canonical chokepoint); TrendForce Q3-Q4 2026 contract-price trajectory — contract following spot down is the clock striking.
- **Falsifier:** contract prices keep rising into 2027 with shipment forecasts *improving* (demand absorbing the tax) — then the long-runway consensus was right and the cycle-clock read was early. Conversely confirmed if contract prices roll while double-booked channel inventory unwinds. (per [[memory-shortage-winners-losers]] falsifiers #1/#2/#4)
- **Last moved:** 2026-06-29 ([[MU]] Q3 FY2026 ingested S176 — record blow-out [$41.5B rev / 84.6% GM]; SCA take-or-pay scaled to 16 deals / $22B with Tier-1 floor-margin-above-peak language → maker-side durability *strengthened*, the downstream cycle-clock still unbroken. Prior S170: [[TAIYO]] MLCC double-confirm; S169 [[MURATA]] actuals).

### AI financing — market reads the mega-deals as demand proof; the funding regime already flipped
**Subjects:** [[AVGO]] · [[NVDA]] · [[CRWV]] · [[NBIS]] · [[ORCL]] · [[AMZN]] — **Durability:** structural while credit stays cheap; by construction a credit-cycle claim (the lowest-durability anchor in the AI section)

- **Consensus (Tier 3/4):** every mega-deal headline (Anthropic racks, Stargate, neocloud capacity) is read as proof of insatiable AI demand; the financing behind the deals is treated as plumbing; lenders price AI credit identically to non-AI credit (the BIS spread finding — the market's own revealed consensus).
- **Vault view (the leverage half is unpriced):** the funding regime has already flipped — big-five free cash flow is BELOW capex (BIS, Jan 2026) and ~$1.5T of the 2025-28 build needs outside capital — so part of the "demand" is simultaneously someone's credit exposure: AVGO carries a $29B backstop on its largest custom-silicon story, NVDA part-funds its own buyers, Amazon is lender+landlord+shareholder to one counterparty, and the IMF quantifies a ~$40B circularity premium in the AI circle's market cap. Either lenders are underpricing the risk or equity is overpricing the cash flows — one of the two markets is wrong. (per [[AI-buildout-who-holds-the-risk]] + `raw/research/ai-buildout-credit-risk-report.md`)
- **Catalyst / timeline:** AVGO Q3 FY2026 10-Q backstop ceiling (~Sept); CRWV vs S&P's FFO/debt-12% threshold; the BIS-style AI-vs-non-AI spread differential opening; any first drawn/impaired/pulled structure.
- **Falsifier:** AI earnings arrive on schedule and FCF climbs back above capex (the flip reverses — financing was bridge, not crutch); or a full GPU depreciation cycle passes with credit losses near zero (the lenders were right). Honest counterweight already on record: as of June 2026 NOTHING has broken — no drawn backstop, no impairment, no failed financing.
- **Last moved:** 2026-06-29 ([[ORCL]] FY2026 ingested S178 — a primary, large-cap example of the entry's thesis: **FCF −$23.7B** [OCF $32B − capex $55.7B], FY2027 capex stepping to ~$70B net + ~$40B fresh financing incl. a $20B ATM-equity program; IG reaffirmed and nothing broke this cycle. The flip is now visible on a hyperscaler's own statements, not just BIS aggregates).

### "The bottleneck game is over" — crowding vs. durability (a counterview to this page's own method)
**Subjects:** the vault's chokepoint roster broadly — [[NVDA]] · [[GEV]] · [[ETN]] · [[MU]] · the photonics chain — **Durability:** meta-entry; per-name durability is exactly what is contested

- **Consensus (Tier 3/4):** a named, high-profile counterview (Gavin Baker, Bg2 Pod, 2026-06-11 — video-intel note): *"finding the next bottleneck — I think that was the last game. That game is over."* The bottleneck-hunting pattern is fully disseminated ("a lot on X about finding the next bottleneck"); scarcity narratives are treated as known and exhausted as a source of edge, and the same conversation expects a consolidation in the names that rode them.
- **Vault view (the distinction consensus skips):** the *discovery* alpha is plausibly gone — the vault concedes that half — but "bottleneck" conflates two different things this page exists to separate: **shortage-cyclical names** (scarcity the market has fully noticed and supply will answer) and **durability-graded chokepoints** (Framework 12 memory-grade scarcity: buyer defense, slow supply response, generational lockout). The counterview's own speakers argue, in the same episode, that the world is watts-constrained, turbine allocation is rationed, and monetization per gigawatt is inflating — constraint claims, all. The game that ended is spotting; the game that remains is grading. (per frameworks Framework 12 + Theme 11.12 stacked bottlenecks + [[transformer-supply]] + [[HBM-oligopoly]] + [[memory-shortage-winners-losers]])
- **Catalyst / re-rate triggers:** divergence at refreshes between Framework 12 verdict classes — durability-graded names holding pricing power and extended lead times through a consolidation while shortage-cyclical names mean-revert (the memory cycle clock and the [[AAOI]]/[[FCEL]] inverse entries are live test cases of exactly this split).
- **Falsifier:** broad, *simultaneous* supply normalization — lead times compressing across power, photonics, and memory together while demand holds — would mean the constraints genuinely resolved and bottleneck analysis is over structurally, not just tactically. Conversely, if the next two quarters of refreshes show durability-graded names extending backlogs while crowded shortage names roll, the spotting-vs-grading distinction is confirmed.
- **Last moved:** 2026-06-13 (created, from the Bg2 2026-06-11 video-intel note).

---

### Inference sustains the chokepoints — market reads the inference shift as relief
**Subjects:** [[HBM-oligopoly]] · [[NVDA]] · [[MU]] · [[TSM]] (CoWoS) · the cooling/power/optics chokepoints — **Durability:** memory-bandwidth + power physics (high); HBM 3-supplier oligopoly generationally locked (high)

- **Consensus (Tier 3/4):** the market reads the training→inference shift as *relief* — inference is the lighter, cheaper, distributable workload that loosens the datacenter constraint once training clusters are built, with edge/on-device AI and efficiency gains pulling demand off the datacenter.
- **Vault view:** inference is **memory-bandwidth-bound** (token decode + reasoning/KV-cache explosion), so the shift **sustains** the chokepoints — HBM demand keeps surging, racks get denser (~370 kW, ~3x training), optics converge on CPO — and the binding constraint migrates *toward* memory bandwidth, not away from the datacenter. Edge is a false dawn for frontier inference; NVIDIA defends *into* inference (Groq). (per [[training-to-inference-shift]] — Tier-3-anchored, 17/25 verified — + [[HBM-oligopoly]] + [[AI-demand-durability]])
- **Catalyst / re-rate triggers:** a hyperscaler breaking out inference capex / inference-rack volumes separately from training; HBM4/4E/5 adoption tracking inference deployment; a first *disclosed* per-vendor inference-ASIC revenue figure. *(latest-alpha + refresh feed these)*
- **Falsifier:** KV-cache compression advances fast enough to *reverse* (not just flatten) the memory-demand slope, OR the inference/training workload mix equalizes and memory bandwidth stops being the binding constraint (frontier inference disperses to edge/client), OR inference capex peaks before ~2028 and training-cycle-completion relief dominates. (per [[training-to-inference-shift]] "What this page does NOT claim" + Open questions)
- **Last moved:** 2026-06-16 (created).

---

## Humanoid Robots

### Investor-access lens — the strongest chokepoints are ownable
**Subjects:** [[HARMONIC]] (reducers, Japan) · [[SANHUA]]/[[TUOPU]] (actuators/thermal, China A-share) · [[MP]] (magnets, US) · [[NOVT]]/[[VPG]] (six-axis sensors, US) — **Durability:** magnets geology (highest); reducers precision-grinding (high, commoditization clock)

- **Consensus (Tier 3/4):** read through a US-only book, the best humanoid chokepoints are private or Chinese — "the strongest chokepoints have the worst US-listed access," so the top value layers look hard to own.
- **Vault view:** with reach across US + foreign-listed (Japan/Germany/Taiwan) + China A-share/HK names, that access constraint largely dissolves — the strongest chokepoints ([[HARMONIC]] reducers, [[SANHUA]]/[[TUOPU]] actuators, [[MP]] magnets) are directly reachable, so the operative ranking is **chokepoint-quality + business health, not the listing flag**. A clean *US* line genuinely is missing at the top value layers (the general-US-book lens still holds), but it is not the binding constraint here. (per `_thesis-humanoid-robot.md` + [[humanoid-robot-value-chain]])
- **Catalyst / re-rate triggers:** a first sizable *confirmed* humanoid OEM order landing at a chokepoint supplier; Chinese suppliers breaking out humanoid/robot revenue; a private name listing (e.g. Unitree STAR IPO) that redraws the access map. *(latest-alpha + refresh)*
- **Falsifier:** humanoid revenue at the cross-over names stays a rounding error and they revert to their primary theses (#9), OR the magnet/reducer chokepoints de-risk — China relaxes rare-earth controls, magnet-free motors advance, precision-grinding capacity scales and compresses lead times (#4 / #5). (per `_thesis-humanoid-robot.md` "what would prove this wrong")
- **Last moved:** 2026-06-09 (created).

### Order-vs-capacity gamble — capacity built ahead of confirmed demand
**Subjects:** the China humanoid-component cohort — [[SANHUA]] · [[TUOPU]] · [[HARMONIC]] · [[HENGLI]] et al. — **Durability:** precision-manufacturing (high, but a commoditization clock)

- **Consensus (Tier 3/4):** the market reads the Chinese suppliers' aggressive capacity build-out as validation that humanoid demand is real and imminent.
- **Vault view:** that capacity was built largely *without binding orders* — a supply-side bet on demand not yet confirmed. If sizable confirmed OEM orders (a Tesla Optimus Gen-3 production order; a Figure BotQ scale-up) do not materialize, the supply side faces margin pressure, not a ramp. Lead every read with "early-innings optionality," not "current revenue." (per `_thesis-humanoid-robot.md` + [[humanoid-robot-value-chain]])
- **Catalyst / re-rate triggers:** the first sizable *confirmed* OEM orders (validates the bet) vs. continued absence into H2 2026 (signals overcapacity) — the order-vs-capacity gap is the testable claim. *(latest-alpha + refresh)*
- **Falsifier:** confirmed orders + proven viability arrive on schedule and the bet pays (consensus right); OR — the larger risk — general-purpose viability stays unproven and orders don't land by H2 2026, forcing margin collapse (#1 / #2, the biggest falsifiers). (per `_thesis-humanoid-robot.md` "what would prove this wrong")
- **Last moved:** 2026-06-09 (created).

---

## Defense & Drones

### Chokepoints > platforms (value-capture inversion)
**Subjects:** [[MP]] (magnets) · [[LSCC]] (secure FPGAs) · [[TDY]] (EO/IR seekers) vs [[AVAV]]/[[KTOS]] (airframe makers) — **Durability:** MP geology/physics (highest); LSCC precision-mfg/IP (high, TSMC-Taiwan dependency); TDY sensor IP (high); platforms deliberately commoditized (low)

- **Consensus (Tier 3/4):** defense/drone spending is surging → the public drone-makers ([[AVAV]], [[KTOS]]) and diversified primes capture the value.
- **Vault view:** value concentrates at the structural chokepoints the supply chain can't route around — magnets, secure chips, seekers, autonomy, compliant supply chains — and **not** at the platform layer, which the Pentagon is *deliberately* commoditizing toward a ~$2,000 one-way-attack-drone ceiling with maintained multi-vendor competition. The supply-side framing is the higher-conviction expression of the thesis. (per `_thesis-defense-drones.md` + [[rare-earth-magnet-chokepoint]] + [[drone-platform-commoditization]] + [[defense-drone-supply-chain]])
- **Catalyst / re-rate triggers:** program-of-record awards naming chokepoint suppliers; magnet/seeker sole-source disclosures; the drone unit-cost trajectory toward the $2k ceiling. *(latest-alpha + refresh)*
- **Falsifier:** airframe makers retain pricing power or vertically integrate the chokepoints (platforms *don't* commoditize), OR the best capability keeps flowing to private players (Anduril / Shield AI / Neros) so the public chokepoint names never capture the economics. (per `_thesis-defense-drones.md` "what would prove this wrong" #2 / #8)
- **Last moved:** 2026-07-11 ([[AVAV]] FY2026 refresh) — a *partial* counter-datapoint on the falsifier: AVAV's blended gross margin recovered to ~30% adjusted / 34% Q4 (from ~24%). Honest read — the recovery is *portfolio-level* (AxS 21% adj EBITDA, lifted by Titan counter-UAS + Switchblade), **not** at the commoditizing OWA line, whose economics stay undisclosed. The vault view stands; the falsifier is *not* tripped (see [[drone-platform-commoditization]] Open Q#2). Prior: 2026-06-09 (created).

### FY2027 budget surge is a request, not enacted law
**Subjects:** the defense-drone universe — [[AVAV]] · [[KTOS]] · [[MP]] · [[LSCC]] · [[TDY]] et al. — **Durability:** policy (contingent — by construction the lowest-durability claim here)

- **Consensus (Tier 3/4):** the market prices the headline FY2027 defense-budget surge as a near-certain, already-in-motion multi-year tailwind.
- **Vault view:** only the FY2025 reconciliation package (~$156.2B mandatory) is *enacted law*; the FY2027 surge (~$54.6B DAWG, ~98% reconciliation-funded) is a *request*, contingent on the November 2026 midterms and a future reconciliation. The *direction* of spending is structural and well-supported; the *magnitude* of the headline figures is a political bet, not a fact — the two must be treated differently everywhere in the vault. (per `_thesis-defense-drones.md`)
- **Catalyst / re-rate triggers:** the November 2026 midterm outcome; FY2027 reconciliation passage or failure; enacted-vs-requested line-item conversion.
- **Falsifier:** a clean FY2027 reconciliation passage converts the request into law (the caution resolves; consensus was right on magnitude) — OR, the risk this entry flags, a divided chamber blocks the surge (per `_thesis-defense-drones.md` "what would prove this wrong" #1, the single biggest falsifier).
- **Last moved:** 2026-07-11 ([[AVAV]] FY2026 refresh) — fresh corroboration of the vault view from a prime's *own* guidance: AVAV set FY2027 revenue (+10%) explicitly assuming a continuing resolution, no full defense budget until "December or January," and cash to the services "until March" — i.e., management itself treats the FY2027 surge as timing-contingent, not banked. Neither falsifier branch has resolved (midterms + reconciliation pending). Prior: 2026-06-09 (created).

---

## Source audit notes

Forward-edge entries are the vault's own variant views, seeded 2026-06-09 from the three human-owned theses' "what would prove this thesis wrong" sections and the chokepoint-quality gradient — not from any single new primary source. The "Consensus" lines are Tier 3/4 characterizations of the prevailing market narrative (described structurally, not via price); the "Vault view" and "Falsifier" lines are primary-grounded and cite the relevant thesis / chokepoint / company pages. No price, valuation, or position data appears by design.

## Change log

- **2026-07-11 (S186 — [[AVAV]] FY2026 refresh; freshness):** Both Defense entries' **Last moved** updated. *Chokepoints > platforms* — AVAV's FY2026 blended gross-margin partial recovery (~24%→~30% adj) logged as a *portfolio-level* counter-datapoint that does **not** trip the falsifier (the OWA line stays undisclosed). *FY2027 request-not-law* — AVAV's own FY2027 guide (+10%, CR-assumed, cash "until March") is fresh corroboration that a prime treats the surge as timing-contingent. No entries added; no thesis files touched; no price data. last_updated 2026-06-29 → 2026-07-11.

- **2026-07-01 (Tier-3 datapoint; last_updated + index unchanged):** "Custom silicon redirects capex" entry — Last moved updated with SemiAnalysis/Dylan Patel's **moat-relocation** framing (CUDA-moat-disentangling on one axis; ecosystem-gravity + ASIC-local-minimum on the other) from the 2026-06-30 Sequoia video-intel note. Bidirectional — sharpens the mechanism, no directional move. Tier-3, NOT a primary ingest; no entry added.
- **2026-06-29 (S178 update):** AI-financing entry — [[ORCL]] FY2026 is now a primary example of the funding-regime flip (FCF −$23.7B; FY2027 ~$70B capex + ~$40B financing incl. $20B ATM; IG held, nothing broke). Last moved updated; no new entries.
- **2026-06-29 (S176 update):** Memory-shortage entry — the **MU Q3 FY2026 catalyst landed** (record blow-out; SCA take-or-pay scaled to 16/$22B with the Tier-1 floor-margin-above-peak disclosure). Maker-side durability *strengthened* (leans toward the long-runway consensus on that axis); the downstream cycle-clock (consumer shipments + contract rollover) still pending. Catalyst + Last moved updated; no new entries; last_updated 2026-06-16 → 2026-06-29.
- **2026-06-16 (S163 update):** Added the AI entry **"Inference sustains the chokepoints"** — consensus reads the inference shift as relief; vault view = inference is memory-bandwidth-bound so it *sustains* HBM/cooling/power/optics (from the new [[training-to-inference-shift]] theme). 11 → 12 entries; last_updated 2026-06-13 → 2026-06-16.
- **2026-06-13 (S159 update):** Added the "bottleneck game is over" meta-entry to the AI section — Gavin Baker's named Tier-3 counterview to this page's own method (Bg2 Pod, 2026-06-11 video-intel note) vs the vault's spotting-vs-grading distinction (Framework 12 durability classes as the live discriminator; the memory, AAOI, and FCEL entries as its test cases). 11 entries total; no ticker changes.
- **2026-06-13 (S157 update):** Added the AI-financing entry to the AI section (consensus reads mega-deals as demand proof; vault view = the funding regime flipped — FCF below capex, ~$1.5T external — and one of two markets is mispricing the risk; catalysts AVGO Q3 ceiling / CRWV S&P thresholds / the spread differential). Created alongside the [[AI-buildout-who-holds-the-risk]] theme. 10 entries total; tickers +CRWV +NBIS +ORCL +AMZN.
- **2026-06-13 (S156 update):** Added the memory-shortage entry to the AI section (consensus prices the memory boom's runway; vault view = the cycle clock is already running via the spot-vs-contract divergence + documented double-booking; catalysts MU June 25 / Murata July / Q3-Q4 contract prices). Created alongside the [[memory-shortage-winners-losers]] theme. 9 entries total; tickers +MU +SNDK +CSCO +PLAB.
- **2026-06-13 (update):** Added the [[FCEL]] entry to the AI section — the 2nd *inverse* divergence (after AAOI): post-Q2 consensus prices a data-center contract before fiscal year-end as the expected outcome; vault view = order-vs-capacity applied to FCEL itself (proposals ≠ orders, backlog falling, ATM-funded, capacity chicken-and-egg), with management's own Oct 31 conversion deadline as the dated catalyst. 8 entries total; tickers +FCEL.
- **2026-06-12 (S154):** Moved to `wiki/trackers/` (`type: tracker`) at the CLAUDE.md v10.0 folder reorganization; added the [[what-could-go-wrong]] sibling-register cross-reference. No entry content changed.
- **2026-06-09 (update):** Added the [[AAOI]] entry to the AI section — an *inverse* divergence (market prices a durable AI-optics winner; vault view = a fragile, minimally-differentiated Layer-5 assembler whose one un-priced lever is the unproven laser→merchant-CPO/ELS tier-upgrade). 7 entries total; tickers +AAOI.
- **2026-06-09 (created):** New cross-vault forward-edge tracker (Layer 3 / consensus-divergence) per CLAUDE.md §3.18. Seeded with 6 high-conviction entries across the three domains (AI: power>compute, custom-silicon→TSM; Humanoid: investor-access lens, order-vs-capacity gamble; Defense: chokepoints>platforms, FY2027 request-not-law), each with a catalyst + falsifier traced to the human-owned theses. Inbound links added from related theme/chokepoint pages. No thesis/frameworks files touched.
