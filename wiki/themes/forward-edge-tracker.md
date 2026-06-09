---
type: theme
tickers: [ETN, VRT, GEV, TSM, NVDA, AVGO, MRVL, ALAB, AAOI, MP, LSCC, TDY, AVAV, KTOS, HARMONIC, SANHUA, TUOPU, NOVT, VPG]
last_updated: 2026-06-09
---

# Forward-Edge Tracker — Consensus vs. Vault View

This is the vault's **forward-edge layer**: a curated, cross-domain tracker of the places where the vault's structural read **differs from what the market is pricing**, plus the catalyst that would force a re-rate and the falsifier that would prove the vault wrong. It surfaces in one place the variant views already latent in the three theses' "what would prove this thesis wrong" sections and the chokepoint-quality gradient.

**Why this layer exists.** Primary filings (10-K/10-Q/call) are backward-looking and largely priced by the time they're filed. The edge is not being *first* on public news (a speed game the vault can't win) — it's having a *better structural read* of public information: seeing where a chokepoint is more durable, or a constraint more binding, or a narrative more fragile, than consensus assumes.

**Discipline rule (load-bearing).** "Consensus" is described as a **structural narrative** or via an **observable mechanism** (lead times, interconnection queues, bond yields, order-vs-capacity) — **never** as stock price, market cap, valuation multiples, or analyst price targets (those stay "signal only" in the quarantined `latest-alpha` blocks). Describe-don't-recommend; a reader cannot tell what is owned. Honest-verdict: if the vault view is weak or consensus is right, say so — do not manufacture a contrarian take. **Entry contract: every entry must carry a catalyst AND a falsifier.** No falsifier means it's a hot take, not an entry.

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
- **Last moved:** 2026-06-09 (created).

### [[AAOI]] — market prices a winner; the structure is a fragile assembler (inverse divergence)
**Subject:** [[AAOI]] — **Durability:** Layer-5 pluggable assembler, "minimally differentiated" (its own 10-K), the vault's most extreme customer concentration (weak); sole optionality = the in-house InP laser (an *unproven* Layer-5 → 4 tier-upgrade)

- **Consensus (Tier 3/4):** the market prices AAOI as a core US AI-optics winner — 800G/1.6T ramp, hyperscaler orders, a raised >$1.1B 2026 guide, and laser/CPO optionality — a structural beneficiary of the photonics supercycle.
- **Vault view (less bullish than consensus):** AAOI assembles the exact pluggable form factor CPO is designed to displace; it is "minimally differentiated," carries the vault's most extreme customer concentration, is still loss-making, and funds growth with heavy ongoing dilution — while leaving CPO displacement of its core *unnamed* in filings. The growth is real but cyclical-demand-driven; the structural position is weak. The bull catalysts (orders, guide, datacenter inflection) are largely **already in the price** — this is the market pricing *durability* the structural read doesn't support, not un-priced upside. (per [[AAOI]] Thesis role + Caveat #9 Layer 4/5 straddle + [[cpo-integration]] + [[CPO-platform-battle]])
- **Catalyst / re-rate trigger (the one genuinely un-priced lever):** merchant **laser / ELS revenue** appearing in a 10-Q — the in-house InP laser becoming a standalone CPO/ELS product (a Layer-5 → Layer-4 tier-upgrade), so far evidenced only at conference (OFC 25dBm ELSFP + a live 6.4T on-board-optics demo; a ~350% InP-fab expansion to 2027). *(latest-alpha + the next refresh feed this)*
- **Falsifier (of the cautious vault view):** that merchant laser/ELS line becomes material AND AAOI rides CPO as a *laser supplier* rather than a displaced *module maker* — re-rating it toward a differentiated Layer-4 component-with-IP and vindicating the "winner" framing. (Conversely the vault view is confirmed if CPO eats the pluggable core while merchant laser stays ~0% and dilution continues — per [[AAOI]] Open questions #4 / #5 / #6.)
- **Last moved:** 2026-06-09 (created).

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
- **Last moved:** 2026-06-09 (created).

### FY2027 budget surge is a request, not enacted law
**Subjects:** the defense-drone universe — [[AVAV]] · [[KTOS]] · [[MP]] · [[LSCC]] · [[TDY]] et al. — **Durability:** policy (contingent — by construction the lowest-durability claim here)

- **Consensus (Tier 3/4):** the market prices the headline FY2027 defense-budget surge as a near-certain, already-in-motion multi-year tailwind.
- **Vault view:** only the FY2025 reconciliation package (~$156.2B mandatory) is *enacted law*; the FY2027 surge (~$54.6B DAWG, ~98% reconciliation-funded) is a *request*, contingent on the November 2026 midterms and a future reconciliation. The *direction* of spending is structural and well-supported; the *magnitude* of the headline figures is a political bet, not a fact — the two must be treated differently everywhere in the vault. (per `_thesis-defense-drones.md`)
- **Catalyst / re-rate triggers:** the November 2026 midterm outcome; FY2027 reconciliation passage or failure; enacted-vs-requested line-item conversion.
- **Falsifier:** a clean FY2027 reconciliation passage converts the request into law (the caution resolves; consensus was right on magnitude) — OR, the risk this entry flags, a divided chamber blocks the surge (per `_thesis-defense-drones.md` "what would prove this wrong" #1, the single biggest falsifier).
- **Last moved:** 2026-06-09 (created).

---

## Source audit notes

Forward-edge entries are the vault's own variant views, seeded 2026-06-09 from the three human-owned theses' "what would prove this thesis wrong" sections and the chokepoint-quality gradient — not from any single new primary source. The "Consensus" lines are Tier 3/4 characterizations of the prevailing market narrative (described structurally, not via price); the "Vault view" and "Falsifier" lines are primary-grounded and cite the relevant thesis / chokepoint / company pages. No price, valuation, or position data appears by design.

## Change log

- **2026-06-09 (update):** Added the [[AAOI]] entry to the AI section — an *inverse* divergence (market prices a durable AI-optics winner; vault view = a fragile, minimally-differentiated Layer-5 assembler whose one un-priced lever is the unproven laser→merchant-CPO/ELS tier-upgrade). 7 entries total; tickers +AAOI.
- **2026-06-09 (created):** New cross-vault forward-edge tracker (Layer 3 / consensus-divergence) per CLAUDE.md §3.18. Seeded with 6 high-conviction entries across the three domains (AI: power>compute, custom-silicon→TSM; Humanoid: investor-access lens, order-vs-capacity gamble; Defense: chokepoints>platforms, FY2027 request-not-law), each with a catalyst + falsifier traced to the human-owned theses. Inbound links added from related theme/chokepoint pages. No thesis/frameworks files touched.
