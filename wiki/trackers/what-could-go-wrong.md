---
type: tracker
tickers: [MSFT, NVDA, AVGO]
last_updated: 2026-06-29
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
- **Status:** NOT FIRED. 2026 guidance intact at primary — Big-4 aggregate ~$640–720B; MSFT ~$190B CY2026 and "capacity-constrained through at least the end of the fiscal year" (MSFT Q3 FY2026 call). The bear mechanism (telecom-bubble analogy, earnings-math gap) is named at Tier 3 (video-intel notes 2026-03-16 + 2026-03-24), not at primary.
- **Last checked:** 2026-06-12 (S154).

### 2. AI demand proves non-durable (the monetization gap never closes)
- **Risk:** application-layer AI revenue never grows into the capex; the demand behind the supply-chain thesis was a narrative.
- **Domain(s):** AI; consensus-aligned.
- **Canonical home:** [[AI-demand-durability]] (disconfirming-signal framework); the application-layer test lives at [[software-AI-moat-durability]] (validated consumption leg vs unproven productivity-seat leg).
- **Tripwire:** consumption-metered AI revenue lines (cloud, data, observability, security) decelerating together; the productivity-seat leg failing at 2025-cohort renewals; clean separate AI revenue lines still absent while capex compounds.
- **Status:** NOT FIRED. The consumption leg is growing at primary (Azure +40%, Snowflake +34%, Datadog +28% per the theme page's anchor); the seat leg remains unproven — that split is the page's live verdict, not a tripwire event. Gap-shape mechanisms (Bain ~$800B shortfall; model commoditization / token-price deflation from DeepSeek-class local models) named at Tier 3.
- **Last checked:** 2026-06-12 (S154).

### 3. Inference/compute efficiency compresses demand
- **Risk:** the same AI workloads run on far less hardware; "more demand" stops meaning "more chips, optics, and power."
- **Domain(s):** AI.
- **Canonical home:** `wiki/_thesis.md` (the "AI inference compute requirements compress" entry in what would prove the thesis wrong).
- **Tripwire:** GPU utilization tooling (virtualization, fractional allocation — DRA/MIG-class) cited at a primary venue as a reason to moderate capex; enterprise fleet utilization rising from the ~5% range toward 30%+ in credible telemetry; a hyperscaler framing efficiency as a substitute for new builds rather than a complement.
- **Status:** NOT FIRED. Mechanisms named at Tier 3 only (the 30–40% cluster-utilization claim and the efficiency-stack inventory, video-intel 2026-03-16). Hyperscalers currently frame the constraint as supply, not efficiency (MSFT Q3 FY2026 call).
- **Last checked:** 2026-06-12 (S154).

### 4. The power constraint resolves faster than expected
- **Risk:** the vault's binding-constraint reframing (power over compute) loses its scarcity premise; the power-layer names lose pricing power.
- **Domain(s):** AI energy/power.
- **Canonical home:** [[transformer-supply]] (oligopoly + substrate-bound structural type) + `wiki/_thesis.md` dual-anchor framing.
- **Tripwire:** transformer lead times normalizing from ~4 years toward pre-2022 norms at primary disclosures; interconnection queues clearing; the behind-the-meter premium collapsing ([[BTM-grid-bypass-workaround]]).
- **Status:** NOT FIRED. The constraint is still binding at primary — chips idle for lack of power (Nadella, MSFT Q3 FY2026 call), ~50% of planned 2026 US builds delayed/cancelled per the thesis baseline.
- **Last checked:** 2026-06-12 (S154).

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
- **Status:** NOT FIRED — and reaffirmed at [[ORCL]] FY2026 (S178): Oracle completed ~$34B of FY2026 financing ($28.8B notes + $5B preferred), guides ~$40B more for FY2027 (incl. a $20B ATM program), and held its investment-grade rating; no pulled/impaired structure. Honest counterweight: Oracle's **FCF went to −$23.7B** (capex $55.7B > OCF $32B), so the *FCF-below-capex* dynamic this entry watches is intensifying even as the financing keeps clearing.
- **Last checked:** 2026-06-29 (S178 — ORCL FY2026).

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
- **Status:** NOT FIRED — and the posture *hardened* at [[MU]] Q3 FY2026: supply now explicitly sets shipments (demand >> supply through 2028), SCAs are non-cancelable take-or-pay with price floors ($22B committed / ~$18B cash), and the 10-Q expects even floor-pricing gross margins "well above our peak quarterly margins in any past cycle." Zero oversupply/concession language; HBM TAM $100B pulled forward to 2027.
- **Last checked:** 2026-06-29 (S176 — MU Q3 FY2026).

## Defense & Drones

### 10. The enacted-vs-requested budget gap
- **Risk:** the drone build-out thesis rests partly on budget *requests* that never become law; only enacted money buys drones.
- **Domain(s):** Defense.
- **Canonical home:** `wiki/_thesis-defense-drones.md` (the enacted-vs-requested discipline).
- **Tripwire:** FY2027 DAWG request materially cut in appropriations; continuing resolutions freezing new drone line items; program-of-record cancellations at primary venues.
- **Status:** NOT FIRED. FY2025 reconciliation funding is enacted law; FY2027 remains a request — the thesis already weights only the former.
- **Last checked:** 2026-06-12 (S154).

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

- **2026-06-29 (S178 — freshness):** Entry 6 (Financing-structure / credit shock) — tripwire NOT FIRED, reaffirmed at [[ORCL]] FY2026 (~$34B financing completed, ~$40B FY2027 plan incl. $20B ATM, IG held) but the FCF-below-capex dynamic intensified (Oracle FCF −$23.7B). Status + Last checked updated.
- **2026-06-29 (S176 — freshness):** Entry 9 (HBM/memory cycle rollover) — tripwire confirmed **NOT FIRED** at [[MU]] Q3 FY2026 (sold-out posture *hardened*: supply-sets-shipments, take-or-pay SCAs with floor pricing, no oversupply/concession language); Status + Last checked updated. No new entries; last_updated 2026-06-12 → 2026-06-29.
- **2026-06-13 (S157 — canonical-home re-point):** Entries 5 + 6 re-pointed to the new [[AI-buildout-who-holds-the-risk]] theme as canonical evidence home (the structures→loss-bearers map; IMF circularity quantification; BIS/IMF/FSB sizing); prior homes kept as secondary links. Tripwires, statuses (both NOT FIRED), and entry text unchanged.
- **2026-06-12 (S154 — gap review + reconciliation pass, same session):** Added Entry 6 (financing-structure/credit shock) + Entry 11 (defense de-escalation); entries renumbered to 16 (9 AI / 4 Defense / 3 Humanoid). Reconciled all 32 thesis-file falsifiers against the register (coverage map added): 2 folds — order-vs-capacity into Entry 14's tripwire, precision-grinding capacity-scaling into Entry 16. All entries remain NOT FIRED.
- **2026-06-12 (S154 — creation):** Created as the vault-level risk register at the `wiki/trackers/` folder creation (CLAUDE.md v10.0, Section 3.20). 14 seed entries across the three domains, all NOT FIRED; dashboard-not-duplicate rule applied — every entry links its canonical home and adds only tripwire + status. Tier-3 bear mechanisms from the 2026-03 video-intel notes (capex-bubble/telecom analogy, utilization/efficiency stack, circular financing) recorded as named-not-fired.
