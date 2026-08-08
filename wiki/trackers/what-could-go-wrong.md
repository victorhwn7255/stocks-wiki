---
type: tracker
tickers: [MSFT, NVDA, AVGO, AVAV, DDOG, GOOGL, INTC, GEV, BE, META, AMZN, PLTR]
last_updated: 2026-08-07
---

# What could go wrong — the vault-level risk register

The single place that tracks the factors that could make the three theses, the frameworks, or the major investment themes wrong. Conventions per CLAUDE.md Section 3.20.

**Current state: no tripwire is FIRED** (as of 2026-06-12, S154). Every entry below is NOT FIRED unless marked otherwise.

**How this page works (the dashboard-not-duplicate rule).** Every risk already has one canonical home — a thesis file, theme, chokepoint, or company page — where the full analysis and the pre-registered "what would prove it wrong" test live. This page does not restate that analysis. Each entry links to its home and adds only what is new: the observable tripwire and its current status. Tier discipline applies: Tier 3/4 sources may *name* a risk mechanism (noted as "named at Tier 3"); only primary sources *fire* a tripwire. No price or valuation tripwires, ever — tripwires are observable mechanisms (guidance cuts, lead-time normalization, utilization shifts, policy events).

**Distinct from [[forward-edge-tracker]].** The forward edge holds views where the vault *differs from consensus*. This register also holds **consensus-aligned risks** — scenarios where the vault and the market could be wrong together (the AI-capex cycle turn is the canonical example: both currently expect the build-out to continue).

---

## AI datacenter supply chain

### 1. Hyperscaler capex cycle turn
- **Risk:** the capex stream that funds every picks-and-shovels name in the vault turns down; the founding thesis loses its demand engine.
- **Domain(s):** AI (all sub-domains); consensus-aligned.
- **Canonical home:** [[hyperscaler-capex]] (six disconfirming signals + the "any two together = cycle turning" rule).
- **Tripwire:** any two of the home page's six disconfirming signals firing in the same period — capex guidance cut at a Big-4 payer is the anchor signal.
- **Status:** NOT FIRED — and the anchor signal moved the *wrong way for the bear* at [[GOOGL]] Q2 2026: Alphabet **raised** its FY2026 capex guide to **$195-205B** (from $180-190B) on "an acceleration in the delivery of capacity to meet growing demand," with 2027 "significantly higher" — a guidance *raise*, not a cut, and demand-pull not cost-push. The Big-4 aggregate ticked up to ~$655-735B; GOOGL is the 2nd firm raise (after META). No disconfirming signal fired. The bear mechanism (telecom-bubble analogy, earnings-math gap) remains named only at Tier 3. **[[MSFT]] FY2026 (S197) reaffirms:** Microsoft guided **FY2027 capex to GROW YoY** (FY2026 cash capex $115.9B/+80%; CY2026 ~$175–190B; Q1 FY2027 >$50B) on demand-pull — a 3rd Big-4 payer with the anchor signal pointing the wrong way for the bear. *(A subtlety to watch: MSFT's §2.1 useful-life change reclassifies future DC leases finance→operating, adjusting the headline CY2026 figure ~$190B→$175B — an accounting shift, not a spend cut, but it makes the capex line less comparable — logged at OQ#6 on [[MSFT]].)* **[[META]] Q2 2026 (S200) makes it the 4th:** META *raised* its FY2026 capex floor to **$130–145B** and framed 2027 as "maximizing 2026 and 2027 capacity" — the anchor signal is a raise, not a cut, across all four big payers.
- **Last checked:** 2026-08-04 (S201 — [[AMZN]] Q2 2026; AWS +36.7% re-accel, capex up, "2× power by 2027" — **Big-4 ROI pass COMPLETE, all raised/grew**) + (S200 — [[META]] capex floor raised) + (S197 — [[MSFT]] FY2027 growing).

### 2. AI demand proves non-durable (the monetization gap never closes)
- **Risk:** application-layer AI revenue never grows into the capex; the demand behind the supply-chain thesis was a narrative.
- **Domain(s):** AI; consensus-aligned.
- **Canonical home:** [[AI-demand-durability]] (disconfirming-signal framework); the application-layer test lives at [[software-AI-moat-durability]] (validated consumption leg vs unproven productivity-seat leg).
- **Tripwire:** consumption-metered AI revenue lines (cloud, data, observability, security) decelerating together; the productivity-seat leg failing at 2025-cohort renewals; clean separate AI revenue lines still absent while capex compounds.
- **Status:** NOT FIRED. The consumption leg keeps strengthening at primary — **[[GOOGL]] Q2 2026 Google Cloud +82% to $24.8B with backlog $514B (+>$50B sequential) and "supply-constrained for multiple quarters in a row"** (a hyperscaler consumption/demand read); alongside **[[DDOG|Datadog]]** +28%/accelerating (S188), Azure +40%, Snowflake +34%. The seat leg remains unproven — that split is the page's live verdict, not a tripwire event. **[[META]] Q2 2026 (S200) adds a demand-side read:** the ads engine kept compounding (ad revenue +27%, price/ad +12%, GEM +8.3% ad-clicks / +15.7% FB conversion, Advantage+ >$75B run rate), and META reports "offers for compute at a significant premium over what we paid" (incremental demand for its capacity) — the monetization gap is not widening at the payer. Gap-shape mechanisms (Bain ~$800B shortfall; model commoditization / token-price deflation) named at Tier 3.
  The **seat leg** also got a fresh datapoint (S191): [[NOW]] Q2 2026 — ServiceNow AI ACV **crossed $1B** (+40% QoQ) with 50% of net-new business non-seat, i.e. the seat-billed incumbent's conversion-to-consumption is monetizing — but it's **still call-only bookings, not clean AI revenue**, so it does not resolve the unproven-seat-leg verdict.
  **[[MSFT]] FY2026 (S197)** strengthens the consumption side further: Azure **+43%** (accelerating, demand>supply), Microsoft Cloud **$214.4B/+27%**, commercial RPO **+84% to $678B** — and, most tellingly, **operating margins EXPANDED to 45%**, i.e. the monetization gap did *not* widen this cycle. On the seat leg, MSFT is now hybridizing Copilot (>30M seats) to **seats + consumption** (usage-based billing added; the incumbent moving the billed unit) — adapting, not failing, but still no clean Tier-1 AI revenue line (the AI-ARR construct was de-emphasized at Q4).
  **[[PLTR]] Q2 2026 (S202)** adds the *deal/outcome* app-layer leg — and cuts both ways, which is why it is worth recording honestly. The monetization evidence is strong: revenue **+93%**, US commercial **+149%**, NDR **157%**, RPO $4.9B (+103%), adjusted FCF margin 63%, and the largest guidance raise in the company's history — enterprise buyers converting AI deployments into contracted, multi-year value rather than pilots. But PLTR's own CTO **names the gap this entry watches**: *"the market has created far more intelligence than it has converted into value,"* and *"a more powerful model does not solve this problem. The limiting factor is the rate of AIP deployment"* (Q2 2026 call). Read together: value conversion is real but **deployment-rate-bound**, not model-bound — so the gap closes at the speed of implementation capacity, not compute. That is a *timing* argument, not a tripwire event, and AIP revenue is still not broken out at Tier 1 (two consecutive quarters), so the app-layer signal remains growth-rate-inferred rather than cleanly disclosed.
- **Last checked:** 2026-08-07 (S202 — [[PLTR]] Q2 2026; app-layer conversion strong but deployment-rate-bound) + 2026-08-04 (S201 — [[AMZN]] AWS +36.7% re-accel [fastest in 18 qtrs], backlog $364B→$496B, AI run-rate >$25B, "still early stages") + (S200 — [[META]] ads +27%) + (S197 — [[MSFT]] Azure +43% / RPO $678B).

### 3. Inference/compute efficiency compresses demand
- **Risk:** the same AI workloads run on far less hardware; "more demand" stops meaning "more chips, optics, and power."
- **Domain(s):** AI.
- **Canonical home:** `wiki/_thesis.md` (the "AI inference compute requirements compress" entry in what would prove the thesis wrong).
- **Tripwire:** GPU utilization tooling (virtualization, fractional allocation — DRA/MIG-class) cited at a primary venue as a reason to moderate capex; enterprise fleet utilization rising from the ~5% range toward 30%+ in credible telemetry; a hyperscaler framing efficiency as a substitute for new builds rather than a complement.
- **Status:** NOT FIRED. Mechanisms named at Tier 3 only (the 30–40% cluster-utilization claim and the efficiency-stack inventory, video-intel 2026-03-16). Hyperscalers currently frame the constraint as supply, not efficiency ([[MSFT]] Q4/FY2026 call — Hood: "demand continues to exceed available supply," visible in spot-market asset pricing — efficiency gains are pursued to get *more* out of the fleet, framed as a complement to new builds, not a substitute).
- **Last checked:** 2026-08-04 (S197 — [[MSFT]] Q4/FY2026; supply-constrained, not efficiency).

### 4. The power constraint resolves faster than expected
- **Risk:** the vault's binding-constraint reframing (power over compute) loses its scarcity premise; the power-layer names lose pricing power.
- **Domain(s):** AI energy/power.
- **Canonical home:** [[transformer-supply]] (oligopoly + substrate-bound structural type) + `wiki/_thesis.md` dual-anchor framing.
- **Tripwire:** transformer lead times normalizing from ~4 years toward pre-2022 norms at primary disclosures; interconnection queues clearing; the behind-the-meter premium collapsing ([[BTM-grid-bypass-workaround]]).
- **Status:** NOT FIRED — and the tripwire moved *away* at [[GEV]] Q2 2026: the power-equipment leader is booking longer, not shorter. Orders +88% YoY (~$24.2B), backlog **$176B → $200B by 2027**, gas SRAs signed **into 2031** (>50% of 2031 slots sold), equipment **pricing +20%** vs Q4 2025, and the gas-capacity ramp (20→30 GW) runs to **2030** — i.e. lead times extending and pricing rising, the opposite of the normalization tripwire. Transformer relief is coming only via capacity adds ([[GEV]] Prolec / $800M H1 US transformer orders), not queue-clearing. Still binding at primary (chips idle for lack of power, Nadella MSFT Q3 FY2026; ~50% of planned 2026 US builds delayed/cancelled per the thesis baseline). The tripwire's "behind-the-meter premium collapsing" leg moved *away* too at [[BE]] Q2 2026 — the BTM premium is *expanding*, not collapsing: BE posted a record first-ever >$1B quarter (+166%), raised guidance twice, and reports "all major US hyperscalers validated" + a named [[NBIS]] (Nebius) turbine-cancellation for on-site fuel cells → hyperscalers are paying up to bypass the grid.
- **Last checked:** 2026-08-04 (S198 — [[BE]] Q2 2026; BTM premium expanding, not collapsing — the workaround demand accelerating) + 2026-07-28 (S193 — [[GEV]] Q2 2026; constraint extending, not resolving).

### 5. NVIDIA circular-financing unwind
- **Risk:** the commitment web (supplier equity/warrants, customer investments, lease backstops) turns out to be late-cycle vendor financing — the telecom-bust pattern where the ecosystem anchor absorbs its customers' losses.
- **Domain(s):** AI; touches photonics (LITE/COHR/GLW commitments) and compute.
- **Canonical home:** [[AI-buildout-who-holds-the-risk]] (the full credit-risk map incl. the IMF circularity quantification); instrument detail at [[nvidia-supply-chain-commitments]].
- **Tripwire:** a backstopped counterparty (CRWV/NBIS-class neocloud) entering financial distress; impairment or write-down of commitment instruments in NVDA filings; a lease backstop actually drawn (the [[AVGO]] $29B max AI-rack class).
- **Status:** NOT FIRED. All instruments performing per latest primary sources; the Lucent-style vendor-financing analogy is named at Tier 3 (video-intel 2026-03-24), not evidenced at primary.
- **Last checked:** 2026-06-12 (S154).

### 6. Financing-structure / credit shock
- **Risk:** the build-out is increasingly funded by debt, leases, and SPV structures rather than operating cash flow; a credit-market event halts construction with demand intact — the *involuntary* version of Risk 1 (a voluntary capex cut) and the system-wide version of Risk 5 (NVDA-specific circularity).
- **Domain(s):** AI (all sub-domains); consensus-aligned.
- **Canonical home:** [[AI-buildout-who-holds-the-risk]] (the structures→loss-bearers map + the BIS/IMF/FSB sizing); the financing-shift dynamic also tracked at [[hyperscaler-capex]].
- **Tripwire:** a failed or pulled financing at a major datacenter developer or neocloud; spreads on AI-datacenter debt widening sharply (instrumented at [[AI-credit-spread-watch]]); an SPV impairment or lease default surfacing in primary disclosures; a hyperscaler citing cost of capital as a reason to slow builds.
- **Status:** NOT FIRED — reaffirmed at [[GOOGL]] Q2 2026 (S190) and [[ORCL]] FY2026 (S178). Two datapoints: (1) ORCL completed ~$34B FY2026 financing, guides ~$40B more, held IG; FCF −$23.7B. (2) **GOOGL** expanded debt **$16B→$100B over 12 months** and posted **Q2 FCF −$5.9B** (capex > OCF) — so the *FCF-below-capex* dynamic this entry watches now shows at a **second** name. **Honest counterweight (the reason it hasn't fired):** GOOGL carries a fortress balance sheet (~$242.5B cash+securities), so its version is a funding-*mix* shift, not a solvency stretch — no pulled/impaired structure, no spread event; the mechanism is intensifying but nothing has broken. **[[MSFT]] FY2026 (S197)** adds a 3rd FCF-below-capex name — Q4 FCF fell to **$19.6B** on the capex ramp — but MSFT is the cleanest of the cohort (fortress balance sheet, minimal net debt, still solidly FCF-positive + >$43B returned to shareholders) → the same funding-*mix* shift, not solvency stress; nothing broke. **[[META]] Q2 2026 (S200) is the 4th — and the sharpest yet: FCF collapsed to $784M** (Q2 capex $31.1B ≈ operating cash flow), debt rose to $83.7B, and META is now visibly **moving the build off its balance sheet** (a new BlackRock 1GW El Paso JV + the non-consolidated Hyperion/Blue Owl VIE — the Structure #5 on [[AI-buildout-who-holds-the-risk]]). Still not fired — META holds $90.3B cash + securities, so it too is a funding-*mix* shift, not solvency stress — but the intensity is now unmistakable across all four fortress payers, and the off-balance-sheet share is the thing to watch. **[[AMZN]] Q2 2026 (S201) completes the Big-4 and is the most FCF-pressured of all: FCF is now NEGATIVE on a TTM basis** (TTM capex ~$173B > TTM OCF ~$161B), and Amazon is **issuing debt** to fund AWS — plus it carries the extreme end of the *circular* leg (the $20B Anthropic facility + a $122.3B Anthropic/OpenAI equity stake — [[AI-buildout-who-holds-the-risk]] Structure #3). Still not fired (fortress balance sheet; the ROIC bet Jassy frames openly) — but all four Big-4 payers now run FCF at/below capex, uniformly funding the build with debt/off-balance-sheet capital. The mechanism is intensifying across the entire cohort; nothing has broken.
- **Last checked:** 2026-08-04 (S201 — [[AMZN]] Q2 FCF negative TTM + issuing debt + $122.3B Anthropic stake — **Big-4 all FCF≤capex**) + (S200 — [[META]] FCF $784M) + (S197 — [[MSFT]] FCF $19.6B).

### 7. Photonics as the first casualty of a capex turn
- **Risk:** if Risk 1 fires, the optical layer takes the hardest hit — picks-and-shovels revenue is the capex line itself (the 2000–02 precedent: the optical suppliers, not the carriers, were ground zero).
- **Domain(s):** AI photonics; conditional on Risk 1.
- **Canonical home:** [[datacenter-photonics-supply-chain]] + [[AI-demand-durability]].
- **Tripwire:** optics/transceiver order cuts or push-outs at two or more vault photonics canonicals in the same quarter without a share-shift explanation; hyperscaler optics-attach guidance falling.
- **Status:** NOT FIRED. Order books and NVDA-ecosystem commitments intact at the latest refreshes; the telecom-casualty framing is named at Tier 3 (video-intel 2026-03-24).
- **Last checked:** 2026-06-12 (S154).

### 8. Taiwan / advanced-node concentration event
- **Risk:** a single-point-of-failure event at the foundry layer (TSMC advanced nodes + CoWoS) breaks the compute supply chain the entire AI thesis sits on.
- **Domain(s):** AI compute; cross-domain second-order effects.
- **Canonical home:** [[overseas-fab-expansion]] (the de-risking watch) + [[TSMC-CoWoS]] (capacity concentration).
- **Tripwire:** export-control or blockade-class policy events restricting advanced-node/CoWoS access; cross-strait disruption signals at observable mechanisms (shipping, insurance, fab-utilization disclosures); overseas-fab timelines slipping while concentration persists.
- **Status:** NOT FIRED. Concentration remains the documented baseline; overseas expansion proceeding per the home page's last refresh.
- **Last checked:** 2026-06-12 (S154).

### 9. HBM/memory cycle rollover
- **Risk:** the HBM oligopoly's pricing power breaks on oversupply; the memory leg of the AI thesis reverts to commodity cyclicality.
- **Domain(s):** AI memory.
- **Canonical home:** [[HBM-oligopoly]].
- **Tripwire:** HBM supply language shifting from sold-out/prepaid to spot/oversupply at [[MU]] + peer primary disclosures; pricing concessions or capacity-ramp guidance outrunning demand commitments.
- **Status:** NOT FIRED — and the posture *hardened* at [[MU]] Q3 FY2026: supply now explicitly sets shipments (demand >> supply through 2028), SCAs are non-cancelable take-or-pay with price floors ($22B committed / ~$18B cash), and the 10-Q expects even floor-pricing gross margins "well above our peak quarterly margins in any past cycle." Zero oversupply/concession language; HBM TAM $100B pulled forward to 2027. **Buyer-side corroboration (S192):** [[INTC]] Q2 2026 — a major memory *buyer* — named **memory** among "one of the most severe supply constraints in [industry] history" (CEO), with **rising memory cost/availability** cited as a headwind to PC affordability (CFO); a fresh independent demand-side read that memory tightness is *not* rolling over.
- **Last checked:** 2026-07-28 (S192 — [[INTC]] Q2 2026 buyer-side memory tightness; supplier-side last at S176 MU).

## Defense & Drones

### 10. The enacted-vs-requested budget gap
- **Risk:** the drone build-out thesis rests partly on budget *requests* that never become law; only enacted money buys drones.
- **Domain(s):** Defense.
- **Canonical home:** `wiki/_thesis-defense-drones.md` (the enacted-vs-requested discipline).
- **Tripwire:** FY2027 DAWG request materially cut in appropriations; continuing resolutions freezing new drone line items; program-of-record cancellations at primary venues.
- **Status:** NOT FIRED — but two AVAV FY2026 datapoints touch the tripwire clauses without firing it. (1) **CR-timing:** [[AVAV]]'s FY2027 guidance (+10%) explicitly *assumes a continuing resolution*, no full defense budget until "December or January," cash to the services "until March" — the CR-freeze *mechanism* is live, but AVAV reports no line-item freeze and still guides growth off a $2.7B backlog, so the systemic budget-gap risk has not fired. (2) **Program cancellation:** the Space Force's termination-for-convenience of AVAV's SCAR program is a single-program cancellation at a primary venue — a discrete instance of the "program-of-record cancellations" clause, but program-specific (BADGER/SCAR), not evidence the FY2027 request is failing to become law.
- **Last checked:** 2026-07-11 (S186 — [[AVAV]] FY2026).

### 11. De-escalation — the defense demand engine fades
- **Risk:** the Defense & Drones domain's demand engine is sustained geopolitical tension; a durable Ukraine settlement plus Middle East calm cuts drone-procurement urgency and European rearmament momentum (partly offset by restocking of depleted inventories, per the thesis's own caveat).
- **Domain(s):** Defense; consensus-aligned.
- **Canonical home:** `wiki/_thesis-defense-drones.md` (the de-escalation entry in what would prove the thesis wrong).
- **Tripwire:** a durable ceasefire/settlement at policy venues; European defense-budget retrenchment (NATO spending targets walked back); the FY2028 US request shrinking unmanned-systems lines; export-order contraction at primary disclosures.
- **Status:** NOT FIRED. No settlement-class event; European rearmament direction and US drone-budget momentum intact per the thesis baseline.
- **Last checked:** 2026-06-12 (S154).

### 12. Blue UAS exemption expiry (policy-grade chokepoint decay)
- **Risk:** compliance moats are policy-grade (the weakest rung of the chokepoint quality gradient) — the rules that create them can change on a date certain.
- **Domain(s):** Defense.
- **Canonical home:** `wiki/_thesis-defense-drones.md` (chokepoint quality gradient: geology/physics > policy).
- **Tripwire:** date-certain — the Blue UAS exemption expires January 1, 2027; watch for lapse, extension, or permanence in the FY2027 NDAA cycle. Any outcome re-prices the compliance-moat names.
- **Status:** NOT FIRED — event pending; no legislative action recorded at primary as of last check.
- **Last checked:** 2026-06-12 (S154).

### 13. Rare-earth/magnet chokepoint resolution
- **Risk:** the vault's strongest geology-grade chokepoint loses its scarcity: China relaxes export controls, non-China capacity scales, or magnet-light designs substitute.
- **Domain(s):** Defense + Humanoid + AI/materials (tri-domain).
- **Canonical home:** [[rare-earth-magnet-chokepoint]] (+ [[MP]] as the non-China anchor).
- **Tripwire:** China export-control relaxation at policy venues; non-China separation/magnet capacity reaching volumes that end allocation behavior; OEM design-wins for magnet-free motor architectures at primary disclosures.
- **Status:** NOT FIRED. Export-control regime and non-China scarcity intact per the chokepoint page's last refresh.
- **Last checked:** 2026-06-12 (S154).

## Humanoid Robots

### 14. Humanoid timing/magnitude disappointment
- **Risk:** the early-innings bet stays early forever — the direction is right but volumes arrive years later and smaller than the value-chain build-out assumed.
- **Domain(s):** Humanoid.
- **Canonical home:** `wiki/_thesis-humanoid-robot.md` (the early-innings discipline: direction credible, magnitude and timing speculative).
- **Tripwire:** flagship OEM programs (Optimus-class) slipping by years at primary venues; the cohort-wide humanoid_tier trigger (first *sized* humanoid revenue at any cohort name) still unfired well past OEM-stated production windows; **the order-vs-capacity gamble busting** — the 2H2026 confirmed-OEM-order window passing while built-out Chinese supplier capacity (100k–1M-unit class) sits idle, turning would-be chokepoint pricing into overcapacity margin collapse (the divergence version of this lives on [[forward-edge-tracker]]).
- **Status:** NOT FIRED — and expected at this stage: no cohort name has sized humanoid revenue yet, which is why the cohort is theme-anchored rather than tiered. This entry fires on *disappointment against stated timelines*, not on the present absence.
- **Last checked:** 2026-06-12 (S154).

### 15. China-access policy risk
- **Risk:** the China cohort (7 A-share names) sits behind an access route that policy can close — capital controls, sanctions, or delisting-class actions.
- **Domain(s):** Humanoid (primarily); AI/materials second-order.
- **Canonical home:** [[china-exposure]] (the access-route axis of the exposure matrix).
- **Tripwire:** policy events restricting foreign participation in A-shares; sanctions touching cohort names; cross-border settlement/custody disruptions at observable mechanisms.
- **Status:** NOT FIRED. Access routes open per the home page's baseline.
- **Last checked:** 2026-06-12 (S154).

### 16. Architecture shakeout — or capacity scaling — erodes a tracked chokepoint layer
- **Risk:** two erosion paths for the covered value-chain layers. (a) **Architecture bypass:** humanoid OEMs converge on designs that strand a covered layer (the dexterous-hand route question — tendon vs linkage vs direct-drive — is the named example; roller-screw alternatives are the second). (b) **Capacity scaling:** precision-grinding capacity (the machines behind harmonic gears and roller screws) scales fast, compressing lead times and margins — the chokepoint survives as a product category but loses its pricing power (the thesis's named erosion path; Shuanghuan-vs-Harmonic price pressure is live early evidence).
- **Domain(s):** Humanoid.
- **Canonical home:** [[humanoid-robot-value-chain]] (per-layer certainty-of-technology-choice scores) + `wiki/_thesis-humanoid-robot.md` (the precision-grinding-scales-fast entry).
- **Tripwire:** (a) OEM architecture decisions at primary/Tier-3 venues that strand a tracked layer; a GS-class re-scoring of layer certainty plus design-win evidence pointing one route. (b) Grinding-machine capacity-expansion disclosures plus sustained price cuts at reducer/screw makers *without* share loss — margin compression at stable share is the capacity-erosion signature.
- **Status:** NOT FIRED. Architecture remains contested and reducer pricing pressure is documented but share-linked per the home pages — neither erosion signature is clean yet.
- **Last checked:** 2026-06-12 (S154).

---

## Reconciliation coverage map (thesis falsifiers → register entries)

Verified completeness check against the three human-owned theses' "what would prove this thesis wrong" sections (all 32 falsifiers; reconciled 2026-06-12, S154). Each falsifier maps to a register entry or carries an explicit exclusion reason. Exclusion classes: **company/page-level** (tracked on the named page, below thesis level), **thesis-predicted** (the thesis itself forecasts it; not a risk *to* the thesis), **by-design** (price/valuation — banned from this page), **universe-composition** (about what is listable/ownable, not whether the structure holds), **divergence** (a within-chain reallocation tracked on [[forward-edge-tracker]], not a vault-breaking risk).

**`_thesis.md` (AI — 14 falsifiers):**

| Thesis falsifier | Disposition |
|---|---|
| Hyperscaler CAPEX deceleration | **Entry 1** |
| Demand-side softening from end customers | **Entry 2** |
| AI inference compute requirements compress | **Entry 3** |
| Power constraint resolves faster than expected | **Entry 4** |
| HBM supply catches up to demand | **Entry 9** |
| Macro/geopolitics dominate structural analysis | **Partial:** Taiwan leg → Entry 8; export-control leg → Entry 13 (mirror); pure-macro remainder excluded by-design |
| Datacenter overbuilding correction (2027–2030) | Composite of **Entries 1 + 3** (efficiency × overbuild = stranding); regional nuance stays at [[AI-demand-durability]] |
| Custom silicon disrupts merchant compute | Excluded — **divergence** ([[forward-edge-tracker]] custom-silicon entry + [[hyperscaler-custom-ASIC]]); the vault holds both sides via [[TSM]] |
| CPO adoption stalls or reverses | Excluded — **page-level**, tracked at [[CPO-platform-battle]] + [[cpo-integration]] (both-sides positioning); future-entry candidate if the battle becomes single-sided |
| NVDA loses CPO ecosystem momentum to AVGO | Excluded — **page-level** ([[CPO-platform-battle]]) |
| SiPh startups acquired into hyperscalers | Excluded — **page-level** ([[CPO-platform-battle]] open-platform leg) |
| TSMC packaging advantage narrows | Excluded — **page-level** ([[TSMC-CoWoS]] + [[foundry-competition]]) |
| Advanced packaging test/metrology smaller than expected | Excluded — **company-level** ([[AEHR]]/[[ONTO]]) |
| Liquid cooling adoption stalls | Excluded — **page-level** ([[liquid-cooling]] competing-technology-base test, pre-registered there) |

*(Entry 6, financing-structure shock, has no thesis-file counterpart — its home is [[hyperscaler-capex]]'s financing-shift dynamic; flagged as a candidate addition at the next Vic-authorized thesis pass.)*

**`_thesis-defense-drones.md` (9 falsifiers):**

| Thesis falsifier | Disposition |
|---|---|
| Budget reversal / reconciliation failure | **Entry 10** |
| De-escalation | **Entry 11** |
| Policy chokepoint expiry (Blue UAS) | **Entry 12** |
| China supply normalization | **Entry 13** |
| Airframe commoditization destroys platform margins | Excluded — **thesis-predicted** (chokepoints-over-platforms); platform-name exposure tracked at [[drone-platform-commoditization]] |
| Tech obsolescence / EW | Excluded — **page-level** (platform pages + [[defense-drone-supply-chain]] autonomy/EW nodes); consistent with chokepoints-over-platforms |
| Valuation already priced in | Excluded — **by-design** |
| The capability stays private | Excluded — **universe-composition** (documented in the thesis + theme page) |
| Narrative ahead of financials | Excluded — **company-level** (Framework D6 financial-quality screen) |

**`_thesis-humanoid-robot.md` (9 falsifiers):**

| Thesis falsifier | Disposition |
|---|---|
| Viability never arrives | **Entry 14** |
| The order-vs-capacity gamble busts | **Entry 14** (tripwire leg) + the divergence version on [[forward-edge-tracker]] |
| The magnet chokepoint de-risks (incl. magnet-free motors) | **Entry 13** |
| Precision-grinding capacity scales fast | **Entry 16** (capacity-scaling leg) |
| Vision-only wins | Excluded — **company-level** ([[OUST]]) |
| Maker commoditization is total | Excluded — **thesis-predicted** (value accrues to chokepoints; the vault holds no maker names) |
| The value stays private | Excluded — **universe-composition** (the access-lens discussion lives in the thesis) |
| Valuation already priced in | Excluded — **by-design** |
| Humanoid immaterial to the cross-over names | Excluded — **company-level** (the needle-mover test on the MP/NVDA/NOVT/VPG pages) |

---

## Change log

- **2026-08-07 (S202 — [[PLTR]] Q2 2026 refresh; light):** Entry 2 (AI demand proves non-durable) — reaffirmed **NOT FIRED**, with the *deal/outcome* app-layer leg added: PLTR revenue +93%, US commercial +149%, NDR 157%, RPO $4.9B, largest-ever guidance raise = enterprise AI converting to contracted value. Recorded honestly alongside PLTR's own naming of the gap ("far more intelligence than it has converted into value"; "the limiting factor is the rate of AIP deployment") — a *timing/deployment-rate* argument, not a tripwire event; AIP revenue still not broken out at Tier 1. Status + Last-checked updated; `tickers` +PLTR. last_updated 2026-08-04 → 2026-08-07.
- **2026-08-04 (S201 — [[AMZN]] Q2 2026 refresh; COMPLETES the Big-4 Q2-mega-cap-ROI pass):** Entries 1/2/6 all reaffirmed **NOT FIRED**. **Entry 1** (capex cycle turn): AWS re-accelerated to +36.7%, capex up, "2× power by 2027" → all four Big-4 payers raised/grew capex, the anchor pointing the wrong way for the bear. **Entry 2** (demand non-durable): AWS +36.7% (fastest in 18 qtrs), backlog $364B→$496B, AI run-rate >$25B, barbell demand "still early stages." **Entry 6** (financing stress): **AMZN is the most FCF-pressured — FCF NEGATIVE on a TTM basis** (capex ~$173B > OCF ~$161B), issuing debt + the extreme circular leg ($20B Anthropic facility + $122.3B stake) → all four Big-4 now run FCF at/below capex, uniformly debt/off-balance-sheet-funded; still mix-not-stress. +AMZN ticker; Status/Last-checked updated on all three. **Q2-mega-cap-ROI pass COMPLETE: GOOGL(S190)+MSFT(S197)+META(S200)+AMZN(S201); only NVDA (~late-Aug) remains.** last_updated already 2026-08-04.
- **2026-08-04 (S200 — [[META]] Q2 2026 refresh; the Q2-mega-cap-ROI-pass META leg):** Ran the primary pass across Entries 1/2/6 — all reaffirmed **NOT FIRED**. **Entry 1** (capex cycle turn): META *raised* its FY2026 capex floor to $130–145B + "maximizing 2026+2027 capacity" → 4th Big-4 payer with the anchor pointing the wrong way for the bear. **Entry 2** (demand non-durable): ads +27%, price/ad +12%, GEM/Advantage+ gains, compute-resale "at a premium" → monetization gap not widening at the payer. **Entry 6** (financing stress): **META FCF collapsed to $784M** (4th and sharpest FCF-below/near-capex name; debt $83.7B) + visibly moving the build off-balance-sheet (BlackRock 1GW JV + Hyperion/Blue Owl VIE) — still mix-not-stress ($90.3B cash), but the intensity is now unmistakable across all four fortress payers. Status + Last-checked updated on all three; +META ticker. **Q2-mega-cap-ROI pass: GOOGL(S190) + MSFT(S197) + META(S200) done; AMZN + NVDA (~late-Aug) remain.** last_updated already 2026-08-04 (S197/S198 same day).
- **2026-08-04 (S198 — [[BE]] Q2 2026 refresh; light):** Entry 4 (power constraint resolves faster than expected) — the tripwire's **"behind-the-meter premium collapsing" leg moved *away***: BE Q2 shows the BTM premium *expanding*, not collapsing — record first-ever >$1B quarter (+166%), guidance raised twice, "all major US hyperscalers validated," a named [[NBIS]] (Nebius) turbine-cancellation for on-site fuel cells → the grid-bypass workaround demand is accelerating (hyperscalers paying up to bypass the grid, i.e. the constraint is *more* binding, not resolving). Status stays **NOT FIRED**; Last-checked → 2026-08-04; +BE ticker. last_updated already 2026-08-04 (S197 same day).
- **2026-08-04 (S197 — [[MSFT]] FY2026 refresh; the Q2-mega-cap-ROI pass, MSFT leg):** Ran the queued primary pass across Entries 1/2/6 (+ a freshness touch on Entry 3) — all reaffirmed **NOT FIRED**. **Entry 1** (capex cycle turn): MSFT guided FY2027 capex to *grow* (FY2026 cash capex $115.9B/+80%; CY2026 ~$175–190B) → 3rd Big-4 payer with the anchor moving the wrong way for the bear; noted the §2.1 useful-life-change capex-comparability caveat. **Entry 2** (demand non-durable): Azure +43%, RPO +84% to $678B, **operating margins EXPANDED to 45%** (the gap did not widen); seat leg hybridizing to seats+consumption. **Entry 3** (efficiency): refreshed the MSFT citation to Q4/FY2026 (supply-constrained, efficiency a complement not a substitute). **Entry 6** (financing shock): MSFT Q4 FCF fell to $19.6B (3rd FCF-below-capex name) but cleanest of the cohort (fortress balance sheet, FCF-positive) = funding-mix not stress. Status + Last-checked updated on all four; MSFT already in tickers. **Q2-mega-cap-ROI pass: GOOGL (S190) + MSFT (S197) done; META/AMZN + NVDA (~late-Aug) legs still pending.** last_updated 2026-07-28 → 2026-08-04.
- **2026-07-28 (S193 — [[GEV]] Q2 2026 refresh; light):** Entry 4 (power constraint resolves faster than expected) — the tripwire moved *away*: GEV orders +88%, backlog $176B→$200B, SRAs to 2031, pricing +20%, capacity ramp to 2030 = lead times extending + pricing rising, the opposite of normalization. Status stays **NOT FIRED**; Last-checked → 2026-07-28; +GEV ticker.
- **2026-07-28 (S192 — [[INTC]] Q2 2026 refresh; light):** Entry 9 (HBM/memory cycle rollover) — added a **buyer-side** corroboration: Intel (a major memory buyer) named memory among "the most severe supply constraints in history" + memory cost/availability as a PC-affordability headwind → memory tightness *not* rolling over. Status stays NOT FIRED; Last-checked → 2026-07-28. (Also: INTC's demand-outpacing-supply + raised capex lightly corroborate Entry 1's NOT-FIRED demand strength — noted, not a separate status change.) INTC already in `tickers`.
- **2026-07-28 (S191 — [[NOW]] Q2 2026 refresh; light):** Entry 2 (AI demand non-durable) — added a **seat-leg** datapoint: NOW AI ACV crossed $1B (+40% QoQ) + 50%-non-seat = the seat-billed incumbent's consumption conversion is monetizing, but still call-only bookings → does NOT resolve the unproven-seat-leg verdict. Status stays NOT FIRED; Last-checked appended (+S191). No ticker add (NOW already demand-side cohort).
- **2026-07-28 (S190 — [[GOOGL]] Q2 2026 refresh; the queued Q2-hyperscaler-ROI pass):** Ran the queued primary pass across Entries 1/2/6 together — all reaffirmed **NOT FIRED**. **Entry 1** (capex cycle turn): GOOGL *raised* the FY2026 guide to $195-205B on demand-pull → the anchor signal moved the wrong way for the bear; aggregate ~$655-735B. **Entry 2** (demand non-durable): Google Cloud +82%/$24.8B, backlog $514B, supply-constrained → consumption leg strengthened. **Entry 6** (financing/credit shock): GOOGL debt $16B→$100B + Q2 FCF −$5.9B → FCF-below-capex now at a 2nd name, but fortress balance sheet = funding-mix not solvency (nothing broke). Status + Last-checked updated on all three; `tickers` +GOOGL. **Note:** this is the GOOGL leg of the queued Q2-mega-cap-ROI pass; MSFT/META/AMZN (~7/29-30) + NVDA (~late-Aug) legs still pending. last_updated 2026-07-18 → 2026-07-28.
- **2026-07-18 (S188 — freshness):** Entry 2 (AI demand proves non-durable) — reaffirmed **NOT FIRED**; the consumption leg is now **primary-confirmed** at [[DDOG]] FY2025/Q1 2026 (was Tier-3 "per the theme page's anchor") — Q1 2026 was the strongest existing-customer usage growth since Q1 2022 with the base broadening (ex-AI-native mid-20s%), so the consumption half of the split strengthened; the productivity-seat half stays the unproven leg. Status + Last checked updated; `tickers` +DDOG; last_updated 2026-07-11 → 2026-07-18.
- **2026-07-11 (S186 — freshness):** Entry 10 (enacted-vs-requested budget gap) — reaffirmed **NOT FIRED** at [[AVAV]] FY2026, but two datapoints logged against the tripwire clauses: AVAV's FY2027 guide *assumes a CR* (the CR-freeze mechanism is live, yet AVAV still guides growth off a $2.7B backlog → no systemic freeze) and the SCAR termination-for-convenience is a single-program cancellation (program-specific, not a budget-gap failure). Status + Last checked updated; `tickers` +AVAV; last_updated 2026-06-29 → 2026-07-11.
- **2026-06-29 (S178 — freshness):** Entry 6 (Financing-structure / credit shock) — tripwire NOT FIRED, reaffirmed at [[ORCL]] FY2026 (~$34B financing completed, ~$40B FY2027 plan incl. $20B ATM, IG held) but the FCF-below-capex dynamic intensified (Oracle FCF −$23.7B). Status + Last checked updated.
- **2026-06-29 (S176 — freshness):** Entry 9 (HBM/memory cycle rollover) — tripwire confirmed **NOT FIRED** at [[MU]] Q3 FY2026 (sold-out posture *hardened*: supply-sets-shipments, take-or-pay SCAs with floor pricing, no oversupply/concession language); Status + Last checked updated. No new entries; last_updated 2026-06-12 → 2026-06-29.
- **2026-06-13 (S157 — canonical-home re-point):** Entries 5 + 6 re-pointed to the new [[AI-buildout-who-holds-the-risk]] theme as canonical evidence home (the structures→loss-bearers map; IMF circularity quantification; BIS/IMF/FSB sizing); prior homes kept as secondary links. Tripwires, statuses (both NOT FIRED), and entry text unchanged.
- **2026-06-12 (S154 — gap review + reconciliation pass, same session):** Added Entry 6 (financing-structure/credit shock) + Entry 11 (defense de-escalation); entries renumbered to 16 (9 AI / 4 Defense / 3 Humanoid). Reconciled all 32 thesis-file falsifiers against the register (coverage map added): 2 folds — order-vs-capacity into Entry 14's tripwire, precision-grinding capacity-scaling into Entry 16. All entries remain NOT FIRED.
- **2026-06-12 (S154 — creation):** Created as the vault-level risk register at the `wiki/trackers/` folder creation (CLAUDE.md v10.0, Section 3.20). 14 seed entries across the three domains, all NOT FIRED; dashboard-not-duplicate rule applied — every entry links its canonical home and adds only tripwire + status. Tier-3 bear mechanisms from the 2026-03 video-intel notes (capex-bubble/telecom analogy, utilization/efficiency stack, circular financing) recorded as named-not-fired.
