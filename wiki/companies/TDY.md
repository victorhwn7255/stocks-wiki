---
type: company
tickers: [TDY]
defense_tier: 4
foreign_issuer: false
last_updated: 2026-06-04
---

# TDY — Teledyne Technologies Incorporated

## Thesis role

Teledyne is the Defense & Drones domain's **EO/IR sensor chokepoint owner** — Teledyne FLIR is the dominant Western position in cooled/uncooled thermal imagers, seekers, and gimbals, decades of export-controlled IP that the supply chain cannot quickly route around. Placement is **`defense_tier 4`** (supply-chain / payload enabler) per `frameworks-defense-drones.md` Framework D2 — the *highest-conviction* tier, where the chokepoint owners sit ([[MP]], [[LSCC]]). Teledyne carries no AI-datacenter supply-chain role (the AI `*_tier` + `layer` fields are not applied); a genuine-but-minor AI-adjacent slice is noted in prose, not tier-framed.

**Why it matters — and the honest verdict.** Teledyne is the cleanest *profitable* way to own the sensor/seeker layer the thesis prizes, and it sits on the **right side of platform commoditization**: as drone airframes are driven toward the ~$2,000 floor (see [[drone-platform-commoditization]]), value migrates *up* to the sensor — Teledyne's layer. But two honest tensions define the page. First, **defense/drones is only ~30–35% of revenue** (~$2B of $6.1B; the majority is broad-cycle commercial — semiconductor imaging, healthcare X-ray, MEMS/networking, marine, environmental, test & measurement), so the EO/IR chokepoint is a high-quality *slice* of a diversified industrial-tech conglomerate, not a pure-play. Second, **Teledyne is itself squeezed from above**: its own 10-K discloses that China's restrictions on rare-earth magnets + germanium + gallium "have in the past delayed" and impact its Digital Imaging + Aerospace & Defense products — so it *owns* the EO/IR chokepoint downstream while *consuming* the rare-earth/germanium chokepoint upstream (see the China section). Per Section 2.1, the page leads with the genuine chokepoint strength and surfaces the diversification + upstream-squeeze tensions plainly.

## Defense-budget exposure — benefit and hurt

Maps onto `frameworks-defense-drones.md` Framework D3 (demand map). All program facts are primary (Teledyne Q1 FY2026 call, Apr 22 2026, unless noted).

**Benefit.** Management sizes defense at **~30–35% of the company** — "approaching almost $2 billion in revenue, between defense, global defense, US defense, drones, EW, missiles, munitions" (Mehrabian). The formal **Aerospace & Defense Electronics segment grew +36% YoY in FY2025** (to $1,058.7M; partly Qioptiq/Micropac acquisitions) and FLIR Defense (inside Digital Imaging) is growing ~9%. Demand signals are strong: **book-to-bill 1.16, the 10th consecutive quarter above 1.0; ~$4.6B backlog**; counter-UAS infrared cameras + subsystems orders of "tens of millions" in Q1/early Q2; SDA space **Tranche programs** ("we've won just about everything") and Golden Dome positioning; munitions-replacement demand from the Middle East; and the US government "making some investments in getting our capacities increased in specific areas" (Mehrabian, on the Iran conflict). Teledyne **raised FY2026 guidance** on this momentum.

**Hurt (and management's own tempering).** The defense tailwind is real but bounded and lumpy, and — unlike [[KTOS]]'s promotional framing — **Teledyne management actively tempers the budget-surge narrative**:
- *Diversification ceiling:* defense is only ~30–35%; the broad-cycle commercial majority (semi imaging, healthcare, MEMS, marine, T&M) drives most of the company.
- *Procurement timing / shutdown risk (Tier 1-disclosed):* the FY2025 10-K Item 1A flags that "**U.S. Government shutdowns**, which in the past have resulted in **delays in anticipated contract awards, delayed payments of invoices** and delays in the issuance" of awards. Mehrabian on the call: "the government cycles are **tedious, even when there's urgent need**."
- *Surge skepticism:* "I'm not going to be the one standing here telling people we're going to **grow 20% a year** like I've heard others do. That's not us." And on Golden Dome specifically: "**We'll see how much budget goes in there in reality.** Asking for increased budgets is one thing. Eventually, there will obviously be some monies." Per Section 3.3, this is Tier 2 management characterization — and it cross-references the `_thesis-defense-drones.md` **enacted-vs-requested budget-contingency caveat**, but with a twist: *Teledyne itself supplies the tempering* (the opposite of KTOS's lean-in).

## Drone supercycle — benefit and hurt

**Benefit (the right side of commoditization).** Teledyne's drone exposure is multi-vector and weighted to the *high-value sensor/payload layer*:
- **Black Hornet** nano-UAS — "Black Hornet 3, now Black Hornet 4, will have revenues of about **$500 million** over that period"; orders in the US, Europe, and the Middle East (Mehrabian).
- **Rogue 1** loitering munition — "full rate production deliveries" underway; "we have our first contracts; those would increase substantially with time" (Bobb / Mehrabian). (The Tier-3 anchor report ties Rogue 1 to the Army's LASSO program — confirm program-naming at a future ingest; the call did not name LASSO.)
- **★ Picks-and-shovels sensor supply** — the structurally important point: Teledyne supplies "cooled, visible, and more importantly, **infrared detectors, not only to our own drone manufacturers, but also to everyone else across the world that's making drones**" (Mehrabian). Teledyne wins at the payload/seeker layer **regardless of which airframe wins** — the inverse exposure to the platform primes [[AVAV]] and [[KTOS]]. As the thesis predicts margin migrates upstream from commoditizing airframes, Teledyne sits at the layer the value migrates *to* (see [[drone-platform-commoditization]]).
- **Counter-UAS** (IR cameras/subsystems, "tens of millions") and **unmanned subsea** (Gavia mine-countermeasure vehicles, long-endurance gliders; Europe orders, +20% in Q1) round out the unmanned franchise — air, ground, and sea.

**Hurt.** Drones are a *slice of the ~$2B defense* (itself a slice of $6.1B). The acute risk is **the upstream squeeze** (next section), not airframe commoditization — the sensor layer is defensible against cheap airframes, but ASP discipline on high-volume cheap counter-UAS sensors is a watch item management did not address (a Source-audit gap). The picks-and-shovels position is strong but not commoditization-*proof*.

## The two-sided China exposure + the chokepoint-consumer finding (honest-verdict centerpiece)

Teledyne *owns* the EO/IR sensor chokepoint, but it is **squeezed from above by the same China concentration [[MP]] is reshoring** — and it says so in its own filings:

> "China has also restricted the export of certain **rare earth minerals and permanent magnets** that are used in our products, which **has in the past delayed** and could in the future limit our ability to sell products that require these components." (Teledyne FY2025 10-K Item 1A; repeated in the Q1 FY2026 10-Q.)

> "...**gallium and germanium**...and **permanent magnets**...which have impacted the **production and pricing** of some of our **digital imaging and aerospace and defense products**." (FY2025 10-K Item 1A.)

Two distinct upstream dependencies fall out:
- **Rare-earth NdFeB magnets** → Teledyne is the **second disclosed defense consumer of the magnet chokepoint** (after [[AVAV]]), naming permanent magnets "used in our products." This substantively meets the pre-registered promotion trigger for [[rare-earth-magnet-chokepoint]], which is promoted from provisional to canonical on this ingest.
- **Germanium (IR-transparent optics) + gallium (semiconductors)** → a *distinct* China-controlled critical-mineral dependence specific to EO/IR optics and compound semiconductors. Germanium is the load-bearing IR-window material for thermal optics; China's export controls bite Teledyne's imaging line directly. This is noted as a forward chokepoint dimension (single-source for now; not yet its own page).

The structural irony is the heart of the page: **China is simultaneously Teledyne's demand driver (the adversary whose threat funds EO/IR and counter-UAS demand) and its supply risk (the controller of the rare-earth/germanium inputs its sensors need).** The benefit and the hurt run through the same country.

## Financial snapshot

Separate tables per reporting period (Section 4.1).

**Section 2.11 status: N/A.** Teledyne's fiscal year ends the Sunday nearest December 31 (FY2025 ended **Dec 28, 2025**; Q1 FY2026 ended **Mar 29, 2026**) — week-scope offset, substantively-calendar (Section 2.11.1); joins [[AMD]] / [[INTC]] / [[LSCC]] / [[KTOS]]. **★ EXACT-period-parity with [[KTOS]]** — both reported a Q1 ended **Mar 29, 2026** (Section 2.11.2; the AMD+INTC pattern), enabling a clean two-defense-prime cross-canonical comparison (a profitable sensor-chokepoint owner vs a dilutive platform prime, same period end).

### FY2025 annual (10-K; fiscal year ended December 28, 2025)

| Metric | FY2025 | FY2024 | YoY |
|---|---|---|---|
| Net sales | $6,115.4M | $5,670.0M | +7.8% |
| — Digital Imaging | $3,163.9M | $3,070.8M | +3% |
| — Instrumentation | $1,457.1M | $1,382.6M | +5% |
| — Aerospace & Defense Electronics | $1,058.7M | $776.8M | +36% |
| — Engineered Systems | $435.7M | $439.8M | −1% |
| Net income (to Teledyne) | $894.8M | $819.2M | +9.2% |
| Diluted EPS (GAAP) | ~$19.1 | — | — |

Segment operating income $1,237.3M (~20.2% margin); R&D $317.3M; acquired-intangible amortization $216.6M; **4 acquisitions in FY2025**. *(FY2025 diluted EPS is computed from $894.8M net income / ~46.9M diluted shares — `python3` was unavailable for a clean per-share extraction this session; confirm the exact statement figure at next touch.)*

### Q1 FY2026 (10-Q; quarter ended March 29, 2026)

| Metric | Q1 FY2026 | Q1 FY2025 | YoY |
|---|---|---|---|
| Net sales | $1,560.1M | $1,449.9M | +7.6% (organic +5.3%) |
| — Digital Imaging | $816.9M | — | +7.9% |
| — Instrumentation | $361.4M | — | +5.3% |
| — Aerospace & Defense Electronics | $277.5M | — | +14.4% |
| — Engineered Systems | $104.3M | — | −2.6% |
| Gross margin | 43.2% | 42.7% | +46 bps |
| Operating income (GAAP) | $294.2M | $259.3M | +13.5% |
| Net income (to Teledyne) | $226.8M | $188.6M | +20.3% |
| Diluted EPS (GAAP) | $4.85 | $3.99 | +21.6% |

Net income +20.3% and diluted EPS $4.85 vs $3.99 verified off the 10-Q MD&A; non-GAAP EPS +17.2% (call). **Book-to-bill 1.16; backlog ~$4.6B.** Operating cash flow $234.0M; **free cash flow $204.3M** (capex $29.7M). **FY2026 guidance (call, raised):** revenue **~$6.415B** (4.9% growth, +70 bps vs January); **GAAP EPS $20.08–$20.44; non-GAAP EPS $23.85–$24.15** (Blackwood). The contrast with the platform primes is stark: Teledyne is **highly profitable, FCF-rich (>$1B/yr, guiding ~$1.1B), low-leverage** — the opposite of [[KTOS]]'s thin-margin / negative-FCF / serial-dilution profile.

## Segment structure — where the defense/EO-IR sits

Four reportable segments (FY2025 weight): **Digital Imaging (52%)** / **Instrumentation (24%)** / **Aerospace & Defense Electronics (17%)** / **Engineered Systems (7%)**. The **EO/IR chokepoint (Teledyne FLIR — thermal imagers, Black Hornet, Rogue 1, counter-UAS) sits inside Digital Imaging** — much of which is *commercial* (machine-vision cameras for semiconductor inspection, medical X-ray, e2v/DALSA imaging, MEMS). The A&D Electronics segment is the formal defense-electronics block (the +36% FY2025 grower, on Qioptiq/Micropac). Honest read: the high-conviction EO/IR sensor chokepoint is a *sub-slice* of the 52% Digital Imaging segment, not the whole of it.

**AI-datacenter-adjacent slice (noted, not tier-framed).** Two genuine-but-broad-cycle touches: **MEMS micromirrors for optical switching in high-speed networking** (Digital Imaging; +20% in Q1) and **Teledyne LeCroy test & measurement** validating datacenter data-transfer protocols (Instrumentation; "data centers increasingly adopt devices utilizing the newest, fastest data transfer protocols"). These are real but broad-cycle (no named hyperscaler; fail the Section 3.10 four-criterion test) → **no AI `*_tier`**; flagged as a forward cross-thesis curiosity (the Teledyne analog of [[KTOS]]'s AI gas-turbine toehold, somewhat more substantive).

## Acquisitive compounder + capital allocation

Teledyne is a disciplined serial acquirer — ~75 acquisitions / ~$12.8B over 25 years (mostly cash-funded), ~$800–900M in the last ~13 months (Qioptiq, Micropac, DD-Scientific). It is FCF-rich (>$1B/yr, guiding ~$1.1B), at a **five-year-low leverage**, with modest buybacks. Currently it is favoring **capex (+35% YoY) and R&D over M&A** because "our demand is larger than our capacity in certain areas" (Mehrabian) — capacity investment into the defense/space demand. On the Framework D6 financial-quality screen, Teledyne is the **healthy end of the spectrum** (profitable, FCF-positive, low-leverage, no going-concern/dilution flags) — the structural opposite of the speculative Tier-3 micro-caps the screen was built for, and of [[KTOS]]'s capital-intensity profile.

## Open questions

1. **FY2025 10-K next-year refresh** + the [[KTOS]] EXACT-period-parity cross-prime comparison (sensor-chokepoint owner vs platform prime, same Mar 29 2026 quarter-end).
2. **Does the rare-earth / germanium supply restriction materially bite FY2026?** The 10-K says it "has in the past delayed" — track whether it constrains Digital Imaging / A&D shipments or pricing.
3. **Rogue 1 / LASSO scale + Black Hornet 4 ramp** — convert the "first contracts" into quantified program scope; confirm the LASSO program-naming.
4. **Golden Dome / SDA Tranche budget conversion** — management-tempered; does the requested budget translate to obligated Teledyne contracts (the enacted-vs-requested caveat)?
5. **Picks-and-shovels ASP durability** — does sensor pricing hold against high-volume cheap counter-UAS demand?
6. **The AI-datacenter-adjacent slice** — does MEMS optical-switching + LeCroy datacenter-test grow into a genuine dual-thesis node, or stay broad-cycle?

## Source audit notes

### Teledyne FY2025 10-K (Tier 1; fiscal year ended December 28, 2025; filed February 20, 2026)

Four segments; net sales $6,115.4M (+7.8%); A&D Electronics +36% YoY (Qioptiq/Micropac). Net income to Teledyne $894.8M (+9.2%). **Material China critical-mineral disclosure** (Item 1A): rare-earth minerals + permanent magnets + germanium + gallium export restrictions "have in the past delayed" and impact Digital Imaging + A&D products — the chokepoint-consumer finding. **Government-shutdown / contract-timing risk** disclosed (delays in awards, delayed payments). 4 acquisitions. EO/IR / FLIR Defense (Black Hornet, Rogue 1, counter-UAS) within Digital Imaging; "unmanned aerial and ground systems" named. (FY2025 diluted EPS computed ~$19.1; clean extraction blocked by a `python3` outage — confirm at next touch.)

### Teledyne Q1 FY2026 10-Q (Tier 1; quarter ended March 29, 2026; filed April 24, 2026)

Net sales $1,560.1M (+7.6%; organic +5.3%); segments DI $816.9M / Instr $361.4M / A&D $277.5M / ES $104.3M. Net income $226.8M (+20.3%); diluted EPS $4.85 vs $3.99 (verified off MD&A). FCF $204.3M. The China rare-earth/magnet supply-restriction disclosure is repeated. No segment restructuring (Section 2.1 N/A).

### Teledyne Q1 FY2026 earnings call (Tier 2; April 22, 2026; Quartr transcript)

Speakers: Jason VanWees (Vice Chairman) + **Robert Mehrabian (Executive Chairman) + George Bobb (President & CEO)** + Steve Blackwood (CFO). **CEO transition** noted: long-time CEO Mehrabian → Executive Chairman; Bobb → President & CEO (Mehrabian still drives the strategy/defense narrative). Beat-and-raise (sales +7.6%, non-GAAP EPS +17.2%, record operating margin, book-to-bill 1.16, guide raised to ~$6.415B). Defense/drone color: Black Hornet ~$500M cumulative; Rogue 1 full-rate production; picks-and-shovels IR-detector supply "to everyone else making drones"; SDA Tranche/Golden Dome; counter-UAS + unmanned subsea. **Notable observations:** (a) **management tempers the defense-surge narrative** ("government cycles are tedious"; "not going to grow 20% like others"; Golden Dome "we'll see how much budget goes in there in reality") — the *inverse* of [[KTOS]]'s DeMarco; documented as honest-framing, cross-ref the enacted-vs-requested caveat. (b) **No Tier-1/Tier-2 framing gap** — the China-mineral + shutdown risks live in the 10-K, the call adds demand color (the call does not dwell on the supply risk — a mild lifecycle note). (c) **CEO-combativeness: assessed, NOT fired — stays at 2** (Mehrabian measured; no hostility). (d) **Report cross-check:** the Tier-3 report's "TDY ~$6.23B TTM; Black Hornet; Rogue 1/LASSO" confirmed/refined against primary ($6,115.4M FY2025; Black Hornet $500M cumulative) → no (g') variance.

## Change log

- **2026-06-04 (Session 131 — first-canonical ingest; Defense & Drones domain's EO/IR sensor chokepoint owner):** Created TDY.md from FY2025 10-K + Q1 FY2026 10-Q + Q1 FY2026 call. **`defense_tier 4`** (EO/IR sensor chokepoint owner; Framework D2/D5; highest-conviction tier); **AI `*_tier` + `layer` OMITTED** (pure-defense; MEMS-optical-switching + LeCroy-datacenter-test AI-adjacency noted prose-only). Centerpiece structured on Vic's two-sided focus: **defense-budget benefit/hurt** (A&D +36%, book-to-bill 1.16, $4.6B backlog, SDA/Golden Dome vs diversification ceiling + shutdown risk + management's own tempering) and **drone-supercycle benefit/hurt** (Black Hornet $500M + Rogue 1 + picks-and-shovels sensor supply to all drone makers = right side of commoditization, vs the upstream squeeze). **★ Honest-verdict centerpiece — two-sided China + chokepoint-consumer finding:** the 10-K discloses China rare-earth-magnet + germanium + gallium export restrictions impacting Digital Imaging + A&D products → Teledyne is the **2nd disclosed magnet consumer** (after [[AVAV]]), promoting [[rare-earth-magnet-chokepoint]] provisional → canonical. **Section 2.11 N/A** (Sunday-nearest-Dec-31; EXACT-period-parity with [[KTOS]], both Q1 ended Mar 29 2026 — Section 2.11.2). Financials verified off the statements (Q1 net income $226.8M / EPS $4.85; FY2026 guidance revenue ~$6.415B / non-GAAP EPS $23.85–24.15; FY2025 EPS ~$19.1 computed, python-outage caveat). Framework D6 read = the *healthy* end (profitable, FCF-rich, low-leverage — opposite of KTOS). CEO transition (Mehrabian → Exec Chairman; Bobb → CEO) noted; CEO-combativeness unchanged at 2; report cross-check clean. NOT a refresh (no refresh_log). Next 10-K pre-registered as the refresh trigger.
