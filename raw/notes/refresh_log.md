# Refresh Ingest Log

Running reference log of **refresh ingests** — re-ingests of an EXISTING vault company page with new primary sources (a newer 10-K / 10-Q / 20-F / 40-F / 6-K plus the matching earnings call). It complements `log.md` (every session, operational) and `index.md` (catalog) by isolating, per refresh, **what changed since the prior baseline, why it mattered, how the placement moved, what propagated across the vault, and what to watch next**. Built up over time, it is a longitudinal reference for how each company's thesis evolves quarter over quarter.

## Scope (what belongs here)

- **In scope:** refresh ingests of existing canonical company pages (new primary source set per Section 4.1 / 4.2).
- **Out of scope:** first-canonical (new ticker) ingests; chokepoint / theme / relationship page creation; codification sessions; in-place Tier-3 substrate refreshes. Those live only in `log.md`.

## Conventions

- **Order:** reverse-chronological — newest entry at the top.
- **Brevity:** Section 3.8 discipline (operational essentials; analytical detail lives on the company page).
- **Maintenance:** appended by the vault agent as a mandatory close-out step of every refresh ingest, per `CLAUDE.md` Section 4.7. Not in `index.md`; updates do not count for accounting.
- **Citations:** numbers carry source + period inline (e.g., "FY2026 10-K", "Q1 FY2027 call"); placement claims name the tier/layer change or state "unchanged" + the reason.

## Per-entry template (copy for each new refresh)

```
## S### — TICKER (Company) — YYYY-MM-DD — <fiscal period refreshed>

- **Sources:** <new primary sources: filing(s) + earnings call, with tiers>
- **Prior baseline:** <session # + the period the page was at before this refresh>
- **Headline:** <one line — the single most important development>
- **Key changes & new developments:**
  - <bullet> ...
- **Placement:** <tier/layer change, or "unchanged" + one-line why>
- **Cross-vault propagation:** <pages updated>
- **Forward watch:** <triggers / open items pre-registered for the next refresh>
- **Key insight:** <one durable takeaway worth remembering across sessions>
```

---

## S186 — AVAV (AeroVironment) — 2026-07-11 — FY2026 (10-K, year ended Apr 30 2026) + Q4/FY2026 call

- **Sources:** AVAV FY2026 10-K (Tier 1) + Q4 & FY2026 year-end call (Tier 2, Jun 29 2026; prepared remarks + Q&A). Annual refresh — no separate Q4 10-Q.
- **Prior baseline:** S124 (first-canonical, Q3 FY2026; the page's first refresh).
- **Headline:** Demand validated (record Q4 $642M/+31% organic; FY26 ~$2.0B/+30% organic; $2.7B backlog), but the BlueHalo deal's execution/acquisition-quality flags worsened — a $240.7M full-year Space-unit goodwill impairment (SCAR terminated for convenience), a Q3-FY2026 restatement, three material weaknesses (disclosure controls *not effective*), a securities class action, and a CFO change.
- **Key changes & new developments:**
  - **The GAAP↔adjusted split is the story:** GAAP net loss $(265.1)M / EPS $(5.40) (impairment + purchase-accounting amortization) vs positive adj EBITDA $286M (14%, beat) / adj EPS $3.31. Adj gross margin recovered to ~30% FY26 / 34% Q4 (from ~24% low) — still below legacy ~40%.
  - **★ Governance cluster (new):** restatement of Q3 FY2026 (10-Q/A, Jun 22 2026) from a goodwill-impairment control weakness; **three** material weaknesses (BlueHalo IT GCs, goodwill-reconciliation control, BlueHalo close process); *Norrell v. AeroVironment* (E.D. Va.) re: SCAR statements; CFO McDonnell → Sean Woodward.
  - **SCAR fully terminated** (was "intended" in Q3); ~$291M Space goodwill remains; ~$30M Q1 FY27 hole; BADGER/WASP pivoting to a commercial product.
  - Segments: **AxS $1,358.1M (21% adj EBITDA)** executing well; **SCDE $618.8M still ~$(3)M adj-EBITDA** loss. US-Gov concentration rose to ~85% (DoD 63%); international 52%→28%; Ukraine not separately disclosed.
  - **FY2027 guide $2.125–2.225B (+10%) = deliberate CR/budget-timing conservatism**, not demand softness (assumes CR; full budget Dec/Jan; cash ~March); deep FY26 award slate (P550 $117M, laser-comms ~$240M, FE-1 $96M, Red Dragon $17M, LOCUST $43M).
- **Placement:** **unchanged** — `defense_tier 1`; no AI `*_tier` / no `layer`; `foreign_issuer false`. Write-off/restatement/suit are Framework D6 acquisition-quality flags, not a tier-defining structural break; §2.1 no-directional-trigger on the strong-revenue momentum either.
- **Cross-vault propagation:** [[drone-platform-commoditization]] (margin partial-recovery datapoint + honest portfolio-level caveat + Red Dragon $17M; OQ#2 sharpened) · [[forward-edge-tracker]] (both Defense entries' Last moved — margin counter-datapoint that doesn't trip the falsifier + FY27-guide corroboration of request-not-law) · [[what-could-go-wrong]] Entry 10 (freshness: CR-assumption + SCAR cancellation touch the tripwire clauses but don't fire it). No-op (unchanged China/supply language): [[rare-earth-magnet-chokepoint]] / [[defense-drone-supply-chain]] / [[china-exposure]].
- **Forward watch:** OQ triggers — SCDE profitability + residual $291M Space-goodwill risk; gross-margin path to legacy; BADGER/WASP commercial-pivot award; FY2027 reconciliation/CR outcome + IDIQ-ceiling conversion; Red Dragon OWA unit economics vs the $2,000 ceiling; **material-weakness remediation + *Norrell* docket**.
- **Key insight:** A transformational acquisition (BlueHalo, closed May 1 2025) delivered the demand it promised *and* a first-year acquisition-quality bill — $240.7M goodwill write-off, restatement, three control weaknesses, a securities suit — while the legacy core (AxS, 21% adj EBITDA) executed cleanly. The tension moved from "is the demand real" to "was the deal well-run."

---

## S178 — ORCL (Oracle Corporation) — 2026-06-29 — FY2026 (10-K, year ended May 31 2026) + Q4/FY2026 call

- **Sources:** ORCL FY2026 10-K (Tier 1, filed June 22 2026) + Q4/FY2026 earnings call (Tier 2, June 10 2026; prepared remarks + Q&A).
- **Prior baseline:** S119 (Q3 FY2026; the page's first refresh).
- **Headline:** RPO exploded to $638B (+363%) while capex $55.7B drove FCF to −$23.7B — Oracle is the cohort's clearest funding-regime-flipped hyperscaler.
- **Key changes:**
  - **§2.1 revenue-presentation recast** (Cloud / Software / Hardware / Services; FY25/24 restated — new "Cloud" $33,989M ≠ old "Cloud services & license support" $44,029M).
  - FY2026: rev $67.4B/+17%, net income $17.1B, GAAP EPS $5.83; **capex $55.7B/+162% → FCF −$23.7B**; RPO **$638B/+363%**.
  - FY2027 guide: **~$70B net capex (~$90-95B reported)**, +34% rev, $8.05 EPS; 31%/28% CAGR to FY2030; ~$40B financing (incl. $20B ATM); IG reaffirmed; $75B BYOH/prepaid "uncoupling."
  - **[[BE]] Bloom fuel cells** power the Doña Ana NM data center; NEW CFO Hilary Maxson; OpenAI/Stargate still zero (both venues).
- **Placement:** UNCHANGED — `layer: outside` + all-`outside` (demand-side payer).
- **Cross-vault propagation:** [[hyperscaler-capex]] (row + prose) + [[AI-demand-durability]] (ORCL subsection) + tracker freshness [[forward-edge-tracker]] (AI-financing entry) + [[what-could-go-wrong]] (#6). **[[BE]] Bloom back-reference DEFERRED** (light; context-bounded — captured on ORCL.md). Light set (hyperscaler-custom-ASIC / neocloud-moat-durability / agentic-CPU) skipped — no framing shift.
- **Forward watch:** the −$23.7B FCF deficit vs ~$70B+ FY2027 capex + the ~$40B financing cadence; RPO counterparty (still unnamed); the §2.1 recast comparability.
- **Key insight:** Oracle's AI-infra demand is now backed by a $638B contracted backlog, but FY2026 is the year its build visibly outran its cash flow — the cohort's cleanest live case of the "funding regime flipped" thesis.

## S176 — MU (Micron Technology) — 2026-06-29 — Q3 FY2026 (10-Q, quarter ended May 28 2026) + Q3 call

- **Sources:** MU Q3 FY2026 10-Q (Tier 1, filed June 27 2026) + Q3 FY2026 earnings call (Tier 2, June 24 2026 — analyst Q&A).
- **Prior baseline:** S87 (Q2 FY2026; the page's first refresh).
- **Headline:** Record blow-out (rev $41,456M / +74% QoQ / +346% YoY; GAAP GM 84.6%; EPS $24.67 — ~24% above the $33.5B guide) — and the SCA "take-or-pay" durability machine moved to Tier 1.
- **Key changes & new developments:**
  - Q3 financials + 4-segment table (CMBU 33% / CDBU 28% / MCBU 28% / AEBU 11%; segment op margins 75-86%); debt $14.6B→$5.7B; 9-mo FCF ~$26.1B; FY2026 capex ~$27B.
  - **SCAs scaled to 16 deals / $22B committed / ~$18B cash / ~½ revenue targeted**, non-cancelable take-or-pay with price floors; the 10-Q (Tier 1) expects floor-pricing GMs "well above our peak quarterly margins in any past cycle" → advances OQ#8's structural pole from Tier-3 to primary (~$422M recognized as contract liabilities so far — early in revenue).
  - "Supply, not demand, determines bit-shipment growth"; demand visibility beyond 2028; HBM TAM $100B pulled to 2027.
  - Monitoring: CEO Mehrotra ABSENT from the Q&A (CBO Sadana led); no combativeness (count 2); analyst-silence meta-signal (bear case un-probed); NVIDIA un-named in the Q&A (§3.6 not assessable from a Q&A-only source); 4-segment framework unchanged (no new §2.1 instance).
- **Placement:** UNCHANGED — Layer 2 / memory_tier 2 HELD. memory_tier 1 evidence strengthened but it's a Vic-side Framework 6 decision (§1.1), escalated via OQ#2, not auto-applied.
- **Cross-vault propagation:** [[HBM-oligopoly]] + [[memory-shortage-winners-losers]] + [[AI-demand-durability]] (the S87-deferred propagations, now done; +MU to AI-demand-durability tickers) + tracker freshness [[forward-edge-tracker]] (memory catalyst landed) + [[what-could-go-wrong]] (entry #9 NOT FIRED confirmed). Light set ([[NVDA-platform-integration]] / [[TSMC-CoWoS]] / [[SNDK]]) consciously skipped — no framing shift.
- **Forward watch:** SCA-floor durability vs the cyclical-vs-structural re-rating (OQ#8); SCA counterparty identity (16 deals, still unnamed); HBM4E qual → volume; CXMT/YMTC; Tongluo/greenfield ramp cost; whether NVIDIA naming returns at the prepared-remarks venue.
- **Key insight:** the quarter the memory-durability argument stopped being only a sell-side story — MU put **take-or-pay floor pricing above any past-cycle peak into a Tier-1 filing**. The open question shifts from "is the boom real" to "does the SCA model hold revenue-share and survive a normalization."

## S171 — CRDO (Credo Technology) — 2026-06-24 — FY2026 (10-K, year ended May 2 2026) + Q4/FY2026 call

- **Sources:** CRDO 10-K FY2026 (Tier 1, filed Jun 15 2026) + Q4/FY2026 earnings call (Tier 2, Jun 1 2026). No intervening 10-Q (Q4 lives in the 10-K). First refresh of the page.
- **Prior baseline:** S27 (2026-04-28) — anchored at Q3 FY2026 (10-K FY2025 + 10-Q Q3 FY2026 + Q3 call).
- **Headline:** Blow-out year (rev $1,335.1M / +206%; non-GAAP NI $662M) with the growth engine pivoting copper→optical and a +80% FY2027 guide leaning on a new ~$600M optical ramp.
- **Key changes & new developments:**
  - FY2026 GAAP NI $472.3M (accumulated deficit wiped); GAAP GM 68.0% / op margin 33.3%; R&D+SG&A 33.6%/22.6% → 20.9%/13.8% (operating leverage); cash $1.4B, no debt; capex $57.3M; inventory $250.8M.
  - The ~$600M FY2027 optical ramp — 3 legs each >$100M (discrete DSPs / SiPho PICs / ZeroFlap, the largest). DustPhotonics (SiPho PIC, closed late-May 2026) → "direct path to CPO/NPO," initial revenue FY2028.
  - Three acquisitions untangled: Hyperlume (MicroLED, Sept 2025) / CoMira (protocol-IP, Feb 2026) / DustPhotonics (SiPho, post-year-end) — corrected the old "Comira misID" note (CoMira is a real, separate deal).
  - Customer concentration broadening: Customer A 67%→49% (AR 86%→53%); 2nd ≥10% customer (32%); Q4 end-customer 34/27/16/10 (four ≥10%); xAI named "fully deployed"; neoclouds → ~20%.
  - Geographic de-concentration: Hong Kong revenue 56%→28%, assets 43%→2%; destination NA 58%/RoW 42%; new US-outbound-investment-in-China risk factor.
- **Placement:** UNCHANGED — Layer 3 / photonics_tier 3. Optical/CPO revenue is FY2027-28 forward; honest-verdict trigger not met. Upgrade trigger pre-registered (realized optical + CPO/NPO + scale-up revenue).
- **Cross-vault propagation:** [[optical-dsp-phy-supply]] + [[cpo-integration]] + [[CPO-platform-battle]] (CRDO now straddles CPO displacement + SiPho participation) + [[china-exposure]] (HK de-concentration; freshness obligation met). Light set (datacenter-photonics-supply-chain / chokepoint-investability-priorities / advanced-optical-packaging / nvidia-supply-chain-commitments) consciously deferred (context-bounded; no materially stale facts — a follow-up sweep).
- **Forward watch:** does the ~$600M optical ramp land (re-concentration by product?); the +80% FY2027 bar; DustPhotonics CPO/NPO FY2028; scale-up FY2027→28; customer broadening vs re-concentration; TSMC 3nm supply.
- **Key insight:** the thesis question flipped from "can it grow" to "does the optical pivot land + is the +80% bar too high" — customer-broadening's de-risking is partly offset by a new single-vector (optical) dependency.

---

## S155 — PLAB (Photronics) — 2026-06-13 — Q2 FY2026 (quarter ended May 3, 2026)

- **Sources:** Q2 FY2026 10-Q (Tier 1; quarter ended May 3 2026) + Q2 FY2026 earnings call (Tier 2; May 28 2026; Vic-staged, full transcript). October 31 fiscal year per Section 2.11 — Q2 FY2026 ≈ calendar Q1/Q2 2026.
- **Prior baseline:** S28 first-canonical (FY2025 10-K + Q1 FY2026 10-Q + call), Apr 28 2026; first refresh of this page.
- **Headline:** The AI boom HURT the mask maker — revenue $209.9M flat YoY and below guide on both lines because elevated fab utilization + the memory price surge suppressed design releases (photomask demand follows tape-outs, not wafer starts); FPD (+13%, high-end +21%) was the offset.
- **Key changes:** Q2 snapshot with full disaggregation (IC high-end record streak broke: $71M → $56.7M); AI crowd-out mechanism added to Thesis role; Allen qualification masks in production (initial revenue late FY26) + Korea 8nm installs later FY26; gross margin −560 bps; Q3 guided flat-to-down ($207-215M); Tier 1/Tier 2 framing gap documented (call names Iran/memory/fab-utilization; 10-Q MD&A says only "delayed design releases"); OQ3 rewritten to design-release recovery timing, OQ9 (visibility) resolved-confirmed, OQs renumbered.
- **Placement:** Unchanged — Layer 4 / photonics_tier outside (Outside Framework 5), re-tested: zero photonics/CPO mentions across both Q2 sources; no escalation trigger fired.
- **Cross-vault propagation:** None written (Outside-placement default exclusion); the AI-crowd-out + memory-constraint observation noted as a candidate enrichment for [[AI-demand-durability]] / [[HBM-oligopoly]] at their next refreshes (second-order demand-suppression evidence).
- **Forward watch:** Q3 report (~September) — does the early-May tape-out recovery hold; Allen initial revenue late FY2026; the undefined "additional investment opportunities" capex teaser; G8.6 AMOLED adoption broadening later in calendar 2026.
- **Key insight:** PLAB is the vault's cleanest second-order AI counterpoint — inside the semiconductor supply chain yet *hurt* by the AI boom near-term, because full fabs and scarce memory delay the design releases photomask demand actually follows.

## S153 — FCEL (FuelCell Energy) — 2026-06-13 — Q2 FY2026 (period ended April 30, 2026)

- **Sources:** Q2 FY2026 10-Q (Tier 1; period ended Apr 30 2026) + Q2 FY2026 earnings call (Tier 2; Jun 8 2026; full transcript, Vic-staged). October 31 fiscal year per Section 2.11 — Q2 FY2026 ≈ calendar Q1/Q2 2026.
- **Prior baseline:** S47 first-canonical (FY2025 10-K + Q1 FY2026 10-Q + call), May 10 2026.
- **Headline:** The narrative-vs-proof gap WIDENED — pipeline jumped 1.5 → 4 GW (89% data-center; avg proposal 65 → 130 MW) and Torrington target raised 350 → 500 MW/yr ($200-275M, gated on contracted backlog), while reported revenue fell 5% to $35.6M and a $42.6M Groton impairment doubled the net loss to $78.7M.
- **Key changes:** Q2 snapshot table with full segment disaggregation; adjusted EBITDA −$17.1M (improved 12%); cash $440.9M built by ~$156M gross ATM dilution in/just after Q2; backlog $1.14B (−9%); narrative-outrunning-proof re-test (all 5 falsification triggers still unmet); Rotterdam carbon-capture modules en route (June delivery); OQ7 (dilution) + OQ12 (segment mix) resolved, OQs renumbered, Groton post-impairment economics added as new OQ11.
- **Placement:** Unchanged — Layer 4 / energy_power_tier 4 at ~65-70%; criterion 4 (named hyperscaler) still falsified at primary: 4 GW is proposals, zero firm hyperscaler orders.
- **Cross-vault propagation:** None — no escalation trigger fired; BTM-grid-bypass-workaround chokepoint propagation deferred to a conversion event.
- **Forward watch:** Management's own dated test — convert proposals to contracted backlog within FY2026 (by Oct 31, 2026); also the ">250% pipeline increase" arithmetic vs the Q1 1.5 GW base (~167% computed), SDCL one-quarter venue silence, and Torrington firm capex commitment.
- **Key insight:** FCEL is now the vault's cleanest live case of the order-vs-capacity test: management raised capacity targets on proposal momentum but self-gated the spend on contracted backlog — the within-FY2026 conversion goal turns the thesis question into a dated, checkable event.

## S152 — TSEM (Tower Semiconductor) — 2026-06-13 — Q4 2025 call gap-fill (LIGHT; no new fiscal period)

- **Sources:** Q4/FY2025 earnings call (Tier 2; Feb 11 2026; Vic-staged) — the one source outside the S62 set. The staged 20-F + Q1 2026 call were verified as ALREADY in canon (S62 created the page from them); the freshness-queue 20-F listing was a file-archive gap, now closed (file archived + filename normalized).
- **Prior baseline:** S62 first-canonical (20-F FY2025 + Q1 2026 call), May 14 2026.
- **Headline:** NVIDIA 1.6T scope IS management-confirmed — Ellwanger Q4-call prepared remarks: Tower "by far the majority supplier of 1.6T silicon PICs"; the S62 "1.6T analyst-introduced, not management-confirmed" annotation is superseded.
- **Key changes:** A1 reciprocal-confirmation-LIMITED rationale updated (1.6T confirmed at Tier 2; module role scoped to PIC/TIA/driver content per Hosseini Q&A); OQ3 partially resolved; Q4-call source audit note added.
- **Placement:** Layer 2 / photonics_tier 2 UNCHANGED.
- **Forward watch:** next real refresh = Q2 2026 results (~Aug call + 6-K); Intel NM mediation; $1.3B 2027 SiPh contract execution.
- **Key insight:** venue-sampling matters — an A1 mode classification drawn from one call flipped when the adjacent quarter's call entered the sample; worth checking both adjacent calls when classifying naming modes.

---

## S151 — AVGO (Broadcom) — 2026-06-13 — Q2 FY2026 (10-Q + earnings call; COMPLETE — call staged and ingested same day)

- **Sources:** Q2 FY2026 10-Q (Tier 1; quarter ended May 3, 2026) + Q2 FY2026 earnings call (Tier 2; June 3, 2026; full Quartr transcript, Vic-staged same day). Initially executed Tier-1-only (trigger 5 noted); completed by same-day call addendum.
- **Call addendum highlights:** AI semi $10.8B +143% (49% of revenue); **FY2026 AI guide $56B (+~180%)**; Q3 AI $16B +200%; **>$30B AI bookings in the quarter, visibility to 2028**; FY2027 ">$100B" reiterated. Customer map: Anthropic **+5 GW next-gen TPU from 2027** (April agreement), Meta MTIA 3 GW thru 2028 (1 GW order received), OpenAI 1.3 GW 2027 contractual, Google multi-generation LTA ("very substantial dollars," diversity-of-sources accepted). **$29B backstop structure identified = Apollo/Blackstone "AI XPU platform"** (>20 GW thru 2028; $35B first tranche; customer inferably Anthropic per the 8-K Hock cited). **CPO reversal: "bright, shiny objects" (Q1) → "we are the de facto standard" (Q2)** — propagated to [[CPO-platform-battle]] (pre-registered verification fired). CFO transition Spears → Thuener (June 12).
- **Prior baseline:** S10 canonical + 2026-05-27 in-place Tier-3 substrate refresh (page was at Q1 FY2026).
- **Headline:** NEW $29B maximum-exposure backstop on a single customer's AI-rack lease obligations (investor-partner structure) — the rack-leasing risk both prior filings flagged generically, now quantified at ~1.3× a quarter's revenue.
- **Key changes & new developments:** Revenue $22.19B +48% YoY (semi $15.0B +79%, now 68% of revenue; software $7.2B +9%); GAAP op margin 49% (vs 39%); EPS $1.91 (vs $1.03). Inventory $2,270M → $4,328M in two quarters (+91%) — the ramp signal accelerating. Distributor concentration STABLE at 42% (first non-acceleration after 21→28→32→42); top-5 end customers ~45%. ~95% TSMC restated + new "TSMC has raised, and may in the future raise, their prices" language. Zero CPO mentions (Tier-1 silence persists vs Tier-3 TH6-Davisson shipping record — widest cross-venue gap in vault).
- **Placement:** Layer 1 / photonics_tier 3 UNCHANGED (straddling tension stands; no trigger met).
- **Cross-vault propagation:** none this pass (rack-backstop customer unnamed; [[hyperscaler-custom-ASIC]] + [[CPO-platform-battle]] candidates deferred to the call addendum).
- **Forward watch:** Q2 call transcript (the $100B-claim restatement + any backstop commentary vs Hock Tan's Q1 "hallucinating" dismissal); which customer sits behind the $29B backstop (OpenAI the natural unconfirmed candidate); whether the backstop ceiling grows.
- **Key insight:** AVGO is now carrying quantified, single-customer credit exposure to make its XPU ramp financeable — platform-definer economics increasingly entangled with customer balance-sheet risk, exactly the pattern the rack-leasing risk language foreshadowed.

---

## S109 — ENS (EnerSys) — 2026-05-29 — FY2026 (10-K + Q4 FY2026 call)

- **Sources:** FY2026 10-K (Tier 1; fiscal year ended March 31, 2026) + Q4 FY2026 earnings call (Tier 2; May 21, 2026; **full 23-page Quartr transcript**).
- **Prior baseline:** S45 (FY2025 10-K + Q3 FY2026 10-Q + Q3 FY2026 *GuruFocus summary*). Page advanced Q3 → FY2026 annual.
- **Headline:** ENS's **first AI-datacenter-direct products** (lithium DC UPS battery + warehouse BESS) entered customer commissioning with hyperscaler validation underway — alongside the full transcript **resolving the S45 Section 2.2 source-unavailability constraint**.
- **Key changes & new developments:**
  - Record *adjusted* results despite a Motive Power / transportation recession: adj diluted EPS $10.56 (+4%); ex-45X record $6.41; ex-45X record adj op profit $382M / 10.2% margin. FY2026 net sales $3,751.4M (+3.7%); Energy Systems $1,651.3M (+7.8%); book-to-bill 1.1 (4-yr high).
  - **GAAP net earnings $293.6M (−19.3% YoY)** on restructuring $51.0M (vs $14.4M) + lower **Section 45X $158.6M (vs $184.6M, −14%)**. CFO bridged GAAP→adjusted transparently → no Tier 1/Tier 2 framing gap fires.
  - **Lithium DC UPS + warehouse BESS** in customer commissioning (finished product shipped; OEM UPS handoffs + hyperscaler validation in progress; **revenue not until FY2028**). First AI-datacenter-direct product motion.
  - **TPPL-for-datacenter Tier-2-substantiated** — high-rate sub-5-min discharges; data-center lead-acid +high teens FY2026; data-center orders +36% YoY; "leading market position" in lead-acid where greenfield trends lithium.
  - **Tijuana lead-acid closure announced March 25 2026 → Springfield MO** (~$20M incremental 45X from FY2028); distinct from Monterrey→Richmond KY (substantially completed; ~$19M FY2027 savings). **Greenville SC re-scoped to A&D/FEOC** (DOE grant final stages). **Rebel acquisition** ($12.7M; defense hybrid power / drone charging).
  - **Section 4.3 reconciliation** — FY2026 sources partially vindicate S45 Falsifications 1/2 (Tijuana/Springfield premature-but-real, distinct events) + 4/6 (TPPL-datacenter Tier-2-substantiated). S45 falsification record preserved; A6 (g') count NOT retroactively edited (forward-only).
  - **Section 2.2 RESOLVED** — full transcript unlocks A1 (hyperscaler-validation-referenced-not-named; diversified archetype holds) / CEO combativeness (O'Connell confident, non-combative — count unchanged 2) / framing-gap (none) / analyst-silence.
- **Placement:** **HELD** — Layer 4 + energy_power_tier 4. Honest-verdict-trigger discipline: products are commissioning-stage (revenue FY2028), no separate DC revenue disclosure, no named hyperscaler, Energy Systems 43% of consolidated. **4→3 trigger pre-registered** = DC sub-segment revenue disclosed OR lithium DC UPS material/named-hyperscaler revenue OR DC majority of Energy Systems.
- **Section 2.11:** ENS = canonical first month+ instance (already coded). FY2026 ≈ calendar-2025/early-2026; Q4 FY2026 ≈ calendar Q1 2026.
- **Cross-vault propagation:** [[AI-demand-durability]] (datacenter-backup-power signal — a distinct buildout layer from compute/networking/generation; + ticker). No VRT edit (no new ENS↔VRT competitive data).
- **Forward watch:** energy_power_tier 4→3 trigger; lithium DC UPS revenue ramp (FY2028 inflection) + named hyperscaler; Investor Day June 11 2026 readout; Greenville DOE award completion; A&D / munitions backlog → revenue translation; Motive Power recovery timing.
- **Key insight:** ENS made its first move from *battery-cell-supplier-to-the-buildout* to *AI-datacenter-product-vendor* (lithium UPS + BESS shipped, hyperscaler-validating) — but it is deliberately pre-revenue (FY2028), so the right read is trajectory, not a re-tier. The refresh also shows a kickoff claim can be "false-at-T, substantiated-at-T+1": two S45 "falsifications" (Tijuana/Springfield) became real ~11 months later as a genuinely distinct restructuring.

---

## S108 — CSCO (Cisco Systems) — 2026-05-29 — Q3 FY2026 (10-Q + Q3 FY2026 call)

- **Sources:** Q3 FY2026 10-Q (Tier 1; period ended April 25, 2026) + Q3 FY2026 earnings call (Tier 2; May 13, 2026).
- **Prior baseline:** S16 (FY2025 10-K + Q2 FY2026 10-Q + Q2 FY2026 call). Page advanced Q2 → Q3 FY2026.
- **Headline:** AI-orders acceleration + the **first named Silicon One hyperscaler design wins** (Q2 had named none).
- **Key changes & new developments:**
  - Record Q3: revenue $15.8B (+12%), product +17%, non-GAAP EPS $1.06 (+10%), both above guidance; FY2026 guide $62.8-63B / EPS $4.27-4.29.
  - Hyperscaler AI orders **$1.9B Q3** (vs $600M yr-prior), YTD $5.3B; **FY2026 hyperscaler AI order target raised to ~$9B** (4.5x FY2025) + ~$4B AI revenue; FY2027 ≥$6B early signal.
  - **Acacia >$1B Q3 orders / >200% FY2026**; >750k 400G + >40k 800G shipped. Still buried in Networking; litigation-only at Tier 1 → the widest-technology-disclosure-gap widens.
  - **Silicon One hyperscaler design wins:** P200 scale-across ×2 + G200 scale-out ×1; +3rd P200 early Q4. "Half of AI orders = systems = Silicon One." Purchase commitments surged to $16.0B (from $7.6B Jul 2025).
  - Restructuring "Fiscal 2026 Plan" — realign to silicon/optics/security/AI; up to $1B pre-tax ($450M Q4 FY2026, rest FY2027); "not savings-driven."
  - Non-GAAP GM 66% (-260bps) — mix (bigger factor) + memory ("unprecedented" pricing; cross-ref [[HBM-oligopoly]]).
  - CPO not re-litigated at Q3 (Chatterjee asked security/Mythos) → acknowledged-deferral stance stands.
- **Placement:** **HELD** — Layer 3 (Layer 3/5 straddling maintained: design wins strengthen capability, not the captive-system revenue model) + photonics_tier 4 (Acacia strong but buried; CPO deferred; 4→3 trigger pre-registered = separate Acacia revenue + merchant optical sales + sustained >$1B).
- **Section 2.11:** applied for the first time (page predates S61). Q3 FY2026 ended April 25 2026 ≈ calendar Q1 2026; **CSCO = 8th month+ instance** — flagged for a CLAUDE.md A.11 codification update.
- **Cross-vault propagation:** [[CPO-platform-battle]] (Q3 deferral note; no new data point) + [[hyperscaler-custom-ASIC]] (Silicon One design-win "silicon diversity" note + ticker) + [[AI-demand-durability]] (networking-side signal + ticker).
- **Forward watch:** photonics_tier 4→3 trigger; Silicon One → merchant switching-silicon share vs [[AVGO]] Tomahawk; scale-up product (still unannounced); FY2027 AI ≥$6B realization; Acacia separate revenue disclosure; memory-cost GM trajectory.
- **Key insight:** the AI story is **systems/Silicon-One-led, not photonics-led** — the first named hyperscaler Silicon One design wins (P200/G200) are the bigger Q3 development than Acacia, and the silicon (not the optics) is what Robbins frames as existential to hyperscaler relevance. A >$1B Acacia business remains invisible at Tier 1 — the vault's widest tech-disclosure gap, now wider.

---

## S106 — ARM (Arm Holdings plc) — 2026-05-29 — FY2026 20-F (LIGHT Tier-1-firming refresh)

- **Sources:** FY2026 20-F (Tier 1 annual; period-end March 31, 2026) — single new source. No new earnings call: the May 6 2026 Q4 FY2026 call + the Q4 FY2026 6-K shareholder letter were ingested at S76.
- **Prior baseline:** S76 (FY2025 20-F as annual placeholder + Q4 FY2026 6-K letter + May 6 2026 call). The page was already on FY2026 financials/strategy; only the 20-F-exclusive disclosures sat on year-old FY2025 figures.
- **Headline:** Tier-1-firming — the FY2026 20-F the page anticipated at S76 arrived; upgrades the controlling-shareholder / customer-concentration / royalty-concentration disclosures FY2025→FY2026. No placement change, no new thesis development.
- **Key changes & new developments:**
  - Mobile-apps-processor royalty 46%→43% (data-center-royalty mix growth; >99% mobile share maintained).
  - Arm China largest-customer 17%→16% (declining trend 24→21→17→16 FY2023-FY2026); customer concentration four-at-49% → three-at-42% (16% / 14% / 12%).
  - SoftBank beneficial ownership 87.1% (May 2025) → 86.4% (May 21 2026) — modest dilution, still a clear majority.
  - Aggregate related-party revenue (Arm China + SoftBank) rose to 30% of total FY2026 ($1,499M) from 21% FY2025 — driven by the SoftBank related-party licensing + design-services agreement.
  - FY2026 audited totals match the Q4 FY2026 6-K letter exactly (no Tier 1/Tier 2 variance); FY2025 financial table completed (royalty $2,168M confirmed; FY2024 total $3,233M added).
  - Qualcomm/Nuvia litigation still pending; single operating segment unchanged.
- **Placement:** UNCHANGED — Layer 1 + ALL `*_tier outside`; Caveat #3(b) Layer 1-2 hybrid notation still deferred (AGI CPU production revenue first-window Q4 FY2027, after this annual's period-end).
- **Cross-vault propagation:** NONE — refreshed items are ARM-page-internal; no chokepoint/theme cites ARM's concentration figures.
- **Forward watch:** Caveat #3(b) hybrid-notation revert when AGI CPU production revenue is material (fiscal 2027+); SoftBank ownership trajectory; Arm China share trend; Qualcomm/Nuvia resolution; next earnings refresh (Q1 FY2027, ~late July/early Aug 2026).
- **Key insight:** for a non-calendar-cadence filer, the comprehensive 20-F can lag the earnings 6-K/call by weeks — so a recently-created page (S76) can still carry year-old 20-F-only disclosures until the annual catches up. This refresh closes that gap; the concentration figures all trend the right way (mobile + Arm China declining as data-center royalty scales).

---

## S105 — AXTI (AXT, Inc.) — 2026-05-29 — Q1 FY2026 (10-Q + Q1 FY2026 call)

- **Sources:** Q1 FY2026 10-Q (Tier 1; period ended March 31, 2026) + Q1 FY2026 earnings call April 30, 2026 (Tier 2, full transcript).
- **Prior baseline:** S13 (FY2025 10-K + Q3 FY2025 10-Q + Q4 FY2025 call); later touches were the [[InP-supply]] promotion (S33) + the [[SOI]] peer cross-ref (S101).
- **Headline:** **Profitability inflection** — the long-loss-making InP-substrate supplier guides Q2 FY2026 to GAAP + non-GAAP profitability; the order-book early-signal converts to results.
- **Key changes & new developments:**
  - Q1 2026 revenue +39% YoY to $26.9M; non-GAAP GM rebounded to 29.9% (21.5% Q4 / −6.1% Q1'25); non-GAAP net loss narrowed to ~$585K; InP now >50% of revenue. Q2 guided to profitability ($0.05-0.08 EPS) and the largest InP quarter in AXT history (beats the $17.7M COVID high).
  - **$632.5M April-2026 capital raise** (8.56M base + 1.28M over-allotment at $64.25/share, exercised in full Apr 22; ~6.6× the Dec-2025 $95.2M raise; priced ~5× the December level) — funds the capacity roadmap; subsequent event in the 10-Q.
  - **InP backlog $60M+ → $100M+.** Capacity roadmap escalated and funded: ~$35M/qtr by end-2026 (ahead of plan) → ~$65-70M/qtr by end-2027 ("double, double") → 2028 greenfield (possibly outside China); management says demand "is 10x" the planned doubling.
  - **China-demand leg (new):** China InP-laser revenue >2× QoQ in Q1, 2× again guided Q2; ~30%→40% of the global InP demand AXTI sees; in-China shipments are export-permit-exempt.
  - Customer base broadening — "nearly all leading customers," hyperscalers engaging directly; long-term supply agreements discussed but unsigned/unnamed (A1 over-claim preserved); no customer >10% of revenue (top-5 ~32%).
  - **Export-control Section 4.3 update:** prior "first US permit denials" reframed to "still pending" + China Ministry of Commerce requesting more data on US applications; non-US permits flow readily.
  - JinMei high-purity-indium refining (vertical-integration deepening); 6-inch InP progress (iron-doped/sulfur-doped).
- **Placement:** layer 6 unchanged; **photonics_tier 3 HELD** (honest-verdict-trigger discipline — Layer-6 substrate input, LTSAs unsigned/unnamed, no pre-registered trigger; strengthening documented in prose; 3→2 trigger now pre-registered: signed+named LTSA + sustained GAAP profit + InP-specific Tier-1 revenue disclosure). **materials_tier 2 ADDED** (engineered-substrate + raw-materials operator incl. indium refining; parallels [[SOI]]; classification predates the multi-domain `*_tier` convention).
- **Cross-vault propagation:** [[InP-supply]] substrate-tier update (primary); light [[SOI]] (peer note + exact tier symmetry) / [[datacenter-photonics-supply-chain]] (Section 2.9) / [[CPO-platform-battle]] (amplifier-section 4x-6x sizing, no new data point). Tier D [[cpo-integration]] / [[datacenter-laser-supply]] skipped per scope.
- **Forward watch:** photonics_tier 3→2 trigger; profitability durability across H2 2026 vs permit-timing volatility; US export-permit resolution; realized capacity output vs the $35M (end-2026) / $65-70M (end-2027) targets; Tongmei IPO / $49M contingent redemption; a named customer or signed LTSA.
- **Key insight:** the vault's earliest-stage demand signal (the AXTI InP order book) has reached the income statement — substrate-tier AI demand is now confirmed at results, not just backlog. The April raise priced at $64.25 vs $12.25 five months earlier (~5×) is itself a market re-rating of the substrate-tier thesis.

---

## S104 — MOD (Modine Manufacturing) — 2026-05-29 — FY2026 (10-K + Q4 FY2026 call)

- **Sources:** FY2026 10-K (Tier 1; FYE March 31, 2026) + Q4 FY2026 earnings call May 27, 2026 (Tier 2, full transcript).
- **Prior baseline:** S70 (FY2025 10-K + Q3 FY2026 10-Q + Q3 FY2026 call).
- **Headline:** A **>$4B single-customer data-center cooling agreement** (CY2027-2029) plus the PT spin restructured as a **Reverse Morris Trust with Gentherm**.
- **Key changes & new developments:**
  - FY2026 net sales ~$3.2B (+23%); Q4 sales +47%, adj EPS +53%; Climate Solutions +87%; **Data Centers +$246M / +158% YoY**; Climate Solutions adj EBITDA +63%; Performance Technologies −3%.
  - **>$4B single-customer DC cooling agreement** (10-K; CY2027-2029; explicit no-assurance language; customer unnamed) — major demand visibility AND a new concentration vector (top-10 customers 49% vs 43% FY2025).
  - **PT spin = Reverse Morris Trust w/ Gentherm** — definitive agreements Jan 2026; Gentherm S-4 + shareholder approval + IRS determination letter completed; close by end CY2026; PT → discontinued operations on close. Resolves the S70 Open Q#1.
  - **Section 2.11 period-parity** with [[NVT]] Q1 2026 now satisfied (resolves S70 Open Q#2): MOD Q4 FY2026 = calendar Q1 2026, DC +158% vs NVT Infrastructure +118.9% (same window).
  - **FY2027 forward segment split:** Climate Solutions → **Data Centers + Commercial HVAC** reportable segments (first standalone DC segment; Section 2.1 forward shift).
- **Placement:** energy_power_tier **HELD at 3** (Layer 4 maintained). 3→2 trigger pre-registered (PT-spin completion → pure-play + $4B converting to disclosed revenue); held this session per honest-verdict-trigger discipline (spin incomplete; $4B is future single-customer; ~$3.2B Layer-4 vs VRT/ETN incumbents; avoid 2nd upgrade in 2 sessions after the S70 Tier 5→3).
- **Cross-vault propagation:** `liquid-cooling` (participant row) + `AIDC-cooling-architecture-transition` (spin row). NVT light cross-ref skipped (comparison lives on MOD.md).
- **Forward watch:** 3→2 at spin completion + $4B revenue conversion; $4B customer identity / 10%-threshold; FY2027 standalone Data Centers segment revenue + margin.
- **Key insight:** MOD's PT spin + [[FLEX]]'s CPI spin = **two parallel cooling/infra pure-play spins** in the same window — a 2-instance cross-vault pattern; codification candidate if a 3rd appears.

---

## S103 — FLEX (Flex Ltd.) — 2026-05-29 — FY2026 (10-K + Q4 FY2026 call)

- **Sources:** FY2026 10-K (Tier 1; FYE March 31, 2026) + Q4 FY2026 earnings call May 6, 2026 (Tier 2, full transcript — replaced the incomplete S36 GuruFocus/Motley Fool summary).
- **Prior baseline:** S36 (FY2025 10-K + Q3 FY2026 10-Q + incomplete Q3 call summary).
- **Headline:** Full **segment restructuring** (FAS/FRS → ITS/RMS/CPI) + **CPI spin-off** + **CEO transition** + **energy_power_tier 5 → 3**.
- **Key changes & new developments:**
  - **Segment restructuring** FAS/FRS → **ITS + RMS + CPI**; prior periods recast (Section 2.1 mid-fiscal-year disclosure-shift, **6th vault instance**).
  - **CPI (Cloud and Power Infrastructure) breakout** $6,614M / **24%** of net sales (12% → 19% → 24% FY24-26); **highest-margin segment (9.2%), +38% YoY**.
  - **CPI spin-off** (May 5, 2026; SpinCo = grid-to-chip AIDC pure-play; Q1 CY2027; tax-free) + **CEO transition** (Advaithi → SpinCo, Hartung → Flex) + **EP² acquisition** (May 2026) + named **Google** multi-year CPI customer.
  - FY2026 net sales $27.9B (+8%); adj EPS $3.30 (+25%); FY2027 outlook $32.3-33.8B / adj EPS $4.21-4.51 (+32%).
  - Full Q4 transcript resolved the prior Open Q#9 + the Section 2.2 source-unavailability observation.
- **Placement:** energy_power_tier **5 → 3 UPWARD reframing** (Section 2.1 honest-verdict trigger — CPI named segment clears the Section 3.10 >15% threshold; 3rd+ UPWARD instance after TSEM/NVT). Layer 6 + photonics/equipment outside unchanged. Honest calibration: FLEX-entity still ~76% non-CPI EMS → Tier 3 not Tier 2; the AIDC pure-play concentrates in SpinCo.
- **Cross-vault propagation:** `liquid-cooling` (T5→T3 participant row) + `AIDC-cooling-architecture-transition` (CPI spin row) + `power-semis` (light grid-to-chip adjacency).
- **Forward watch:** SpinCo dedicated-page candidate post-spin (Q1 CY2027); energy_power 3→2 if CPI scales (+65-75% FY27 / >80% FY28); NVIDIA (Flag 1 over-claim) + JetCool-Broadcom (Flag 2 reciprocal-pending) at future NVDA/AVGO refreshes; RemainCo de-tier question.
- **Key insight:** NVIDIA + Broadcom remain **Tier-1-silent** (10-K zero mentions) — over-claim preserved; **Google** is the concrete named hyperscaler. CPI spin parallels MOD's PT spin (see S104).

---

## S102 — MRVL (Marvell Technology) — 2026-05-29 — Q1 FY2027 (10-Q + Q1 FY2027 call)

- **Sources:** Q1 FY2027 10-Q (Tier 1; period ended May 2, 2026) + Q1 FY2027 earnings call May 27, 2026 (Tier 2). First primary refresh of the **oldest vault page** (S9 baseline).
- **Prior baseline:** S9 (10-K FY2026 + Q3 FY2026 10-Q + Q4 FY2026 call) + accumulated cross-refs.
- **Headline:** Expanded **NVIDIA partnership + a $2.0B NVIDIA convertible-preferred investment** — which **reverses the page's prior "reciprocal non-naming" observation**.
- **Key changes & new developments:**
  - **NVIDIA $2.0B Series A Convertible Preferred** (issued March 31, 2026; ~$91.84 conversion, max ~21.8M shares; 10-Q Tier 1) + **NVLink Fusion** ("bridge between custom and merchant") + optics/silicon-photonics + AI-RAN. Reverses reciprocal non-naming (NVDA "never named" → named throughout); documented as `NVDA-platform-integration` **Mode 4 (FIRST INSTANCE: equity + partnership + competitor)**.
  - **Polariton acquisition** (plasmonics; >1 THz modulator bandwidth; 3.2T roadmap; call-only, not in 10-Q).
  - Guidance raised again: FY2027 ~$11.5B (+40%), FY2028 ~$16.5B (~+45%); interconnect FY27 >70%; custom "more than double" FY2028 toward >$10B FY2029.
  - **Celestial PPA finalized $3.5B** + consolidated; $331.8M earn-out remeasurement drove GAAP EPS $0.04 vs non-GAAP $0.80.
  - Q1 FY2027 revenue $2,417.8M (+28%); GAAP GM 52.1% / non-GAAP 58.9%; data center 76%; distributors 51%; record OCF $639M; now one reportable segment; bifurcation → scale-out / scale-up / **scale-across** trifurcation.
- **Placement:** Layer 3 + photonics_tier 3 **unchanged** (Layer 3→2 triggers still unmet — GAAP GM 52.1% < 60%; CPO revenue < $500M; trajectory strengthened, documented in prose).
- **Cross-vault propagation:** `NVDA-platform-integration` (Mode 4) + `hyperscaler-custom-ASIC` + `cpo-integration` + `optical-dsp-phy-supply` (Tier B); `CPO-platform-battle` + `advanced-optical-packaging` + `AI-demand-durability` (Tier C); `AI-agentic-CPU-orchestration-reemergence` + `datacenter-photonics-supply-chain` (light).
- **Forward watch:** NVDA-side reciprocal confirmation of the NVLink-Fusion/optics scope (A1 pending); Polariton deal terms; reciprocal-non-naming convention reconciliation (codify the partner-and-competitor case); photonics_tier 3→2 as scale-up optics + NVIDIA SiPh collaboration scale.
- **Key insight:** **NVIDIA now takes equity stakes in its supply chain** — COHR ($2B) + LITE ($2.02B) + MRVL ($2.0B preferred) = a 3-instance cross-vault pattern worth synthesizing.
