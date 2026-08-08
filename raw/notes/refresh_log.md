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

## S202 — PLTR (Palantir Technologies) — 2026-08-07 — Q2 2026 (10-Q, period ended June 30 2026) + Q2 2026 call

- **Sources:** Q2 2026 10-Q (Tier 1; period 2026-04-01→06-30) + Q2 2026 earnings call (Tier 2; Aug 3 2026 — Karp/Sankar/Glazer/Taylor). Section 2.11 N/A (calendar FYE).
- **Prior baseline:** S114 first-canonical (FY2025 10-K + Q1 2026 10-Q + May 4 2026 call). PLTR's **first refresh** — the page had been untouched since 2026-06-02 apart from a provenance-only INOD cross-ref (S135).
- **Headline:** A record quarter (revenue +93%, Rule of 40 155, largest-ever guidance raise) that held the placement — but the session's real product was **three cross-vault connections the S114 baseline could not have had**: a previously unrecorded NVIDIA partnership, a missing `defense_tier`, and a pre-registered trigger firing.
- **Key changes & new developments:**
  - **Q2 2026:** revenue $1,935.5M/+93% (10-Q; beat the $1.797-1.801B guide); US $1,573.0M/+115% = 81% of total; US commercial $764M/+149%, US government $809M/+90% (call); GAAP op income $912.0M/47%; net income to common $1,061.9M, diluted EPS $0.41; adjusted op income $1,194M/62%; adjusted FCF $1.22B/63%; RPO $4.9B/+103%; NDR 157%; Rule of 40 155.
  - **Guidance raised** FY2026 $7.65-7.66B → **$8.15-8.158B** (+82%), the company's largest-ever raise; adj FCF $4.5-4.7B.
  - **NEW — NVIDIA partnership** (Karp: *"we built a partnership with NVIDIA"*; fine-tuning on an NVIDIA stack incl. classified; Nemotron Ultra beating frontier models on five production tasks). PLTR-side only, **no instrument disclosed** → counterparty-attribution-only (§3.5).
  - **`defense_tier: 2` added** — the field was absent despite CLAUDE.md §3.2 and Framework D2 assigning it. Q2 supplied the primary evidence: Maven chosen by a **government program of record**, >25,000 builders, US gov +90%, with management's own scale caveat (Department of War TTM revenue "<25 basis points of the Pentagon's budget").
  - **Moat reframed as "sovereign AI"** (~18 call mentions) with **model portability shipped as product** — positioned against frontier-lab lock-in. Sankar: *"the models are commodities"*; *"the market has created far more intelligence than it has converted into value"*; *"the limiting factor is the rate of AIP deployment."*
  - **Honest counterweights:** SBC-driven GAAP-vs-adjusted margin gap **widened** ~14→~15pts; AIP revenue **still not broken out** at Tier 1 (2 consecutive quarters); RPO disclosed as primarily Commercial (understates the government book); Q2 gross margin absorbed cloud hosting for a Government customer.
- **Placement:** **HELD** — `layer: outside` + all five AI `*_tier: outside` (app-layer-consumer per §3.21; a record quarter is not a supply-chain trigger, §2.1). **Changed:** `defense_tier` added at **2** (index Defense `—`→`2`).
- **Cross-vault propagation:** substantive — [[software-AI-moat-durability]] (row + matrix cell + Q2 validation para; verdict HELD/strengthened, falsifier moved the opposite way on both legs), [[AI-implementation-deployment-layer]] (**dated instrument #7 FIRED/cleared**), [[nvidia-supply-chain-commitments]] (**new application-layer/model-stack modality**; does not increment the reciprocal-confirmation count, still 5). Light — [[AI-earnings-quality-noncash-marks]] (6th instance; SpaceX mark **not fully stripped from non-GAAP** — a new variant), [[what-could-go-wrong]] Entry 2 (NOT FIRED), [[frontier-app-layer-value-capture]] (cross-ref only). Stated no-ops incl. [[defense-drone-supply-chain]] (deferred), [[LEU]]/[[HALEU-fuel-chokepoint]] (zero Centrus mentions this quarter), [[forward-edge-tracker]].
- **Forward watch:** (1) NVDA-side bilateral confirmation of the partnership, or a PLTR disclosure naming an instrument/program/$ figure; (2) does an AIP revenue line ever appear at Tier 1 (now 2 quarters open); (3) does the government mix keep falling below ~51%; (4) does the SBC margin gap stabilize or keep widening; (5) is the government cloud-hosting cost absorption a one-off or a structural gross-margin shift; (6) **`defense_tier` backfill for AMD + NVDA** + adding PLTR to [[defense-drone-supply-chain]] as one consistency pass.
- **Key insight:** The most valuable output of a first refresh is often **not** the numbers — it is the connections the baseline session could not see. Three of the four findings here were relational (an unrecorded NVIDIA partnership, a frontmatter field the frameworks already assigned but the page never carried, a dated trigger coming due), and only one was financial. Also worth carrying: PLTR is the vault's first instance of a company **naming the AI monetization gap from inside the application layer** — and arguing it is bound by deployment rate, not model capability.

## S201 — AMZN (Amazon.com) — 2026-08-04 — Q2 2026 (10-Q, period ended June 30 2026) + Q2 2026 call

- **Sources:** AMZN Q2 2026 10-Q (Tier 1, period ended June 30 2026) + Q2 2026 call (Tier 2, July 30 2026; CEO Andy Jassy / CFO Brian Olsavsky). US-domiciled (Dec 31 FYE) → **§2.11 N/A**.
- **Prior baseline:** S116 (first-canonical, FY2025 10-K + Q1 2026 10-Q + Q1 call). AMZN's **first true primary refresh.** AMZN = the vault's **3rd hyperscaler / 5th demand-side page** (capex-payer, §3.21) — **the LAST mega-cap leg of the Q2-mega-cap-ROI pass (completes the Big-4).**
- **Headline:** A strong operating quarter with a spectacular AWS re-acceleration — but headline net income is a mirage inflated by the vault's LARGEST-ever non-cash mark (~$53.4B Anthropic; operating income $27.5B is the clean read).
- **Key changes & new developments:**
  - **Q2:** net sales $200.6B/+20%; **operating income $27.5B/+43%**; **net income $62.6B/+245%** ($53.4B-mark-inflated); diluted EPS $5.75. **AWS $42.2B/+36.7%** (fastest in 18 qtrs, 5th straight accelerating, **$169B run-rate, 39% margin [+520bps ex-derivative], op income $16.6B/+64%**, **61% of consolidated OI**); backlog $364B→**$496B**; AI run-rate >$25B; chips $25B+ run-rate.
  - **★ The $53.4B Anthropic mark** ("$50.5B upward adjustments primarily on Anthropic preferred," 10-Q); stake carrying value **$16.2B→$122.3B**; net income tripled — largest non-cash mark in the vault, pro-cyclical.
  - **★ Capex $53.1B Q2; stayed QUALITATIVE** on annual $-figure (capacity guide only: "2× power 2025→2027"); **FCF NEGATIVE TTM** (capex ~$173B > OCF ~$161B), debt-funded — most FCF-pressured of the Big-4.
  - **Two ~$600M one-timers** flattered Q2 (tariff refund NA + energy-derivative gain AWS). **NEW: merchant-Trainium** signal (may sell chips to 3rd parties); Kiro/Transform app-layer; Graviton CPU; barbell demand.
- **Placement:** **UNCHANGED** — `layer: outside` + all five `*_tier: outside` (capex-payer, §3.21).
- **Cross-vault propagation:** substantive [[hyperscaler-capex]] (completes Big-4 pass; dynamic #5 — largest mark) + [[what-could-go-wrong]] Entries 1/2/6 (all NOT FIRED; +AMZN; Big-4 all FCF≤capex) + [[AI-earnings-quality-noncash-marks]] (**RESOLVES its OQ#1** — the largest instance) + [[AI-buildout-who-holds-the-risk]] (Structure #3); light [[AI-demand-durability]] + [[hyperscaler-custom-ASIC]] (Trainium + merchant signal). No-op: [[AI-agentic-CPU-orchestration-reemergence]] (Graviton captured on AMZN.md; ARM-letter content unchanged), peers/supplier-warrant names, [[nvidia-supply-chain-commitments]], [[liquid-cooling]], [[software-AI-moat-durability]], [[china-exposure]].
- **Forward watch:** AWS margin durability; Trainium share + merchant-Trainium; clean AI revenue line; the equity-mark reversal test; FCF-turn / total debt required; 4th Amazon supplier warrant.
- **Key insight:** AMZN completes the Big-4 ROI pass with the most extreme version of both cycle signals — the strongest AWS re-acceleration (+36.7%) *and* the biggest mark-distortion ($53.4B) *and* the deepest FCF pressure (negative TTM, debt-funded). The demand is unambiguous; the earnings quality and the financing are where the scrutiny now sits.

## S200 — META (Meta Platforms) — 2026-08-04 — Q2 2026 (10-Q, period ended June 30 2026) + Q2 2026 call

- **Sources:** META Q2 2026 10-Q (Tier 1, period ended June 30 2026) + Q2 2026 call (Tier 2, July 29 2026; CEO Mark Zuckerberg / CFO Susan Li). US-domiciled (Dec 31 FYE) → **§2.11 N/A** (Q2 2026 = calendar Q2).
- **Prior baseline:** S117 (first-canonical, FY2025 10-K + Q1 2026 10-Q + Q1 call). META's **first true primary refresh.** META = the vault's **4th hyperscaler / 6th demand-side page** (capex-payer, §3.21) — **one of the two remaining legs (META + AMZN) of the Q2-mega-cap-ROI pass.**
- **Headline:** A down-bottom-line quarter that is entirely one-time charges — revenue +28% but GAAP OI −8% on a $2.4B legal charge + $1.2B severance (ex-those, OI +9%); the operating ads engine kept compounding and the AI demand signal strengthened (capex floor raised, 2027 "maximizing capacity," a new BlackRock 1GW JV, "sell compute directly" confirmed), while the counterweights grew (FCF collapsed to $784M; increasingly off-balance-sheet financed; new third-party-AI-token cost; youth-litigation risk; RL ~$(4.6)B/qtr).
- **Key changes & new developments:**
  - **Q2:** revenue $60.8B/+28% (FoA ad $59.4B/+27%, price/ad +12%; FoA "other" hit $1B/+73%); **GAAP OI $18.8B/−8%** (ex $2.4B legal + $1.2B severance: **+9%**); net income $15.85B/−14%; diluted EPS $6.18; RL rev $431M/+16%, op loss ~$(4.6)B.
  - **★ FCF collapsed to $784M** (Q2 capex $31.1B ≈ OCF); cash+securities $90.3B / debt $83.7B — META = 4th Big-4 payer with FCF at/below capex.
  - **★ Off-balance-sheet financing:** a NEW BlackRock 1GW El Paso JV + the non-consolidated Hyperion/Blue Owl VIE (10-Q-confirmed) → [[AI-buildout-who-holds-the-risk]] Structure #5.
  - **Guidance:** FY2026 capex → **$130–145B** (floor raised from $125B); expenses → $165–169B (for the legal charge); OI>2025; tax 15–17%; Q3 rev $61–64B; 2027 not guided ("maximizing 2026+2027 capacity").
  - **★ "Sell compute directly" confirmed** ("offers at a premium over what we paid") + model API (Muse Spark on OpenRouter) + Meta Business Agent Platform — graduated from the latest-alpha block (does NOT move `layer: outside`). GEM +8.3% ad-clicks / +15.7% FB conversion; Advantage+ $75B run rate; Meta glasses strong.
- **Placement:** **UNCHANGED** — `layer: outside` + all five `*_tier: outside` (demand-side capex-payer, §3.21). A strong capex/demand quarter reinforces the demand-source role; compute-resale ≠ a chokepoint (§2.1 no-trigger).
- **Cross-vault propagation:** substantive [[hyperscaler-capex]] (row/bullet/aggregate/dynamic-#5) + [[what-could-go-wrong]] Entries 1/2/6 (all NOT FIRED — the Q2-mega-cap-ROI-pass META leg; Entry 6 tripwire moved toward on the FCF collapse; +META ticker); light [[AI-buildout-who-holds-the-risk]] (Structure #5) + [[AI-demand-durability]] + [[hyperscaler-custom-ASIC]]. No-op: [[AI-earnings-quality-noncash-marks]] (META's decline is a real one-time CASH charge, not a mark), peers ([[AVGO]]/[[AMD]]/[[ARM]]/[[GLW]]/[[CRWV]]/[[NBIS]]), [[neocloud-moat-durability]] (no new named-neocloud datapoint), [[telecom-bust-analog]] (captured via who-holds-risk + wcgw), [[HBM-oligopoly]] (memory callout not repeated — nothing to add), [[software-AI-moat-durability]] (not on scorecard), [[AI-agentic-CPU-orchestration-reemergence]] (ARM AGI-CPU still not at Meta primary), [[china-exposure]].
- **Forward watch:** capex-vs-cash-flow gap (FCF trajectory as capex scales); off-balance-sheet-financing size + terms (BlackRock + Hyperion); youth-litigation material-loss risk; RL loss path; memory-pricing re-surfacing; compute-resale revenue line; ARM AGI-CPU.
- **Key insight:** META is the cohort's clearest case that the AI-buildout debate has moved from "is demand real?" (answered: capex floors keep rising, ads-AI compounding) to "how is it financed?" — its Q2 FCF collapsed to $784M and it is now visibly moving the build off its balance sheet (BlackRock + Hyperion), the same funding-intensity shift now visible across all four fortress hyperscalers. Its bottom-line "miss" is the opposite of the mark-flattered cohort — a real one-time charge that *understates* the operating trajectory.

## S198 — BE (Bloom Energy) — 2026-08-04 — Q2 2026 (10-Q, period ended June 30 2026) + Q2 2026 call

- **Sources:** BE Q2 2026 10-Q (Tier 1, period ended June 30 2026) + Q2 2026 call (Tier 2, July 28 2026; CEO/Founder/Chairman K.R. Sridhar / CFO Simon Edwards). US-domiciled (Dec 31 FYE) → **§2.11 N/A** (Q2 2026 = calendar Q2).
- **Prior baseline:** S40 (first-canonical, FY2025 10-K + Q1 2026 10-Q + Q1 call). BE's **first true primary refresh** (94 days stale — oldest page in the vault). BE = the canonical **Framework 7 (energy/power) Tier 2** ingest + **Modality 1 (SOFC)** anchor on [[BTM-grid-bypass-workaround]].
- **Headline:** The BTM grid-bypass workaround thesis (S40 ~85%) MATERIALIZED AT SCALE — a record, first-ever >$1B quarter that is GAAP-profitable and operating-driven (not an equity-mark artifact), guidance raised twice, and the customer base broadened from Oracle-only to "all major US hyperscalers"; honest counterweights hold (FCF guide pulled; financier-intermediated concentration; contra-revenue Oracle warrant; ~$37M IEEPA tariff recovery).
- **Key changes & new developments:**
  - **Record Q2:** revenue $1,065.4M (+166% YoY, first >$1B quarter); product $935.4M (+215%); **GAAP operating income $182.2M** (from a $(3.5)M loss) / GAAP net income $198.9M / GAAP diluted EPS $0.62; non-GAAP op income $240M (22.5% margin); non-GAAP GM 34.3%; adj EBITDA $253M; non-GAAP EPS $0.78. Operating-driven profit (clean vs the AMZN/MSFT mark pattern).
  - **Guidance raised twice off year-start:** FY2026 revenue → $3.9–4.2B (~100% growth); non-GAAP OI → $800–900M (from $425–450M); non-GAAP EPS → $2.55–2.85. **FCF guide WITHDRAWN** (CFOA $375M+ baseline given); $2.7B cash; H1 capex only $77.8M.
  - **Connections:** [[ORCL]] warrant issued Apr 9 / exercised May 1 → 1,905,433 shares (contra-revenue); "all major US hyperscalers validated"; **[[NBIS]] (Nebius) cancelled turbine/reciprocating-engine orders for Bloom** (Modality-4→1 migration); Brookfield $5B→$25B + new IDF/Oaktree/MUFG/MS $2.6B; scandium "not dependent on China" (8-K).
  - **Concentration flipped:** Q2 top-2 = 44% (non-related) + 21% (related party, down from #1/43% at FY2025); CFO flags the named "customer" may be a *financier* (Brookfield/IDF), not the end hyperscaler; delivery-lumpy.
- **Placement:** **UNCHANGED** — `layer 4` + `energy_power_tier 2` (+ photonics/equipment `outside`). A record quarter reinforces the F7 Tier 2 BTM placement (§2.1 honest-verdict-trigger discipline); electricity revenue fell to 0.9% and the PPA economics sit on the financier's books → Layer 4 reinforced, not tripped toward Layer 5.
- **Cross-vault propagation:** substantive [[BTM-grid-bypass-workaround]] (resolved its Open question #2; Modality 1 + Nebius migration evidence; financier-intermediated concentration archetype); light [[forward-edge-tracker]] (power>compute + FCEL "BE converted" anchor) + [[what-could-go-wrong]] Entry 4 (BTM premium expanding, NOT FIRED; +BE ticker) + [[china-exposure]] (scandium non-China) + [[AI-buildout-who-holds-the-risk]] (financier-takes-title, a less-circular structure; resolved a tickers-without-body gap). No-op: [[ORCL]] / [[NBIS]] / peers (refresh doesn't edit peers — reverse cross-refs flagged); [[AI-demand-durability]] / [[transformer-supply]] / [[power-semis]] (BE role unchanged / captured elsewhere).
- **Forward watch:** Oracle delivery cadence; aggregate backlog $ disclosure; FCF-guide reinstatement + trajectory as capex/WC scale; financier-vs-end-customer concentration attribution; AEP phase-2 timeline; service-revenue Layer-5 trigger (margin 22% but share ~6.5%).
- **Key insight:** BE is the vault's cleanest example of a workaround-upstream-of-the-binding-constraint thesis *converting* — record, GAAP-profitable scale with the customer base broadening to all major hyperscalers, and a named turbine-to-fuel-cell substitution (Nebius). The next-order questions are all about *financing structure* (financier-intermediated concentration; pulled FCF guide), not demand.

## S197 — MSFT (Microsoft) — 2026-08-04 — FY2026 (10-K, year ended June 30 2026) + Q4/FY2026 call

- **Sources:** MSFT FY2026 10-K (Tier 1, year ended June 30 2026) + Q4/FY2026 call (Tier 2, July 29 2026; CEO Satya Nadella / CFO Amy Hood). Annual US-filer set (Q4 folds into the 10-K). **§2.11 applies** (June 30 FYE; FY2026 ≈ calendar Jul 2025 – Jun 2026; Q4 FY2026 = calendar Q2 2026).
- **Prior baseline:** S112 (first-canonical, FY2025 10-K + Q3 FY2026 10-Q + Q3 call). MSFT's **first true primary refresh**. MSFT = the vault's **first hyperscaler / demand-side page** (the capex-payer anchor, §3.21) + the anchor scorecard name for [[software-AI-moat-durability]]. **The anchor leg of the Q2-mega-cap-ROI pass.**
- **Headline:** The capex-payer demand signal strengthened decisively — and, crucially, at *expanding* margins (the direct rebuttal to the capex-vs-revenue "disconnect") — while the contested software seat-leg is being actively hybridized to "seats + consumption." Honest counterweights: rising funding intensity, a §2.1 useful-life change, and a ~$5.0B OpenAI-investment gain flattering GAAP.
- **Key changes & new developments:**
  - **★★ Strong + margin-expanding:** FY revenue $331.8B (+18%, accelerating); operating income $155.2B (+21%); **operating margins EXPANDED to 45%** despite AI-infra scaling — margins went UP, not down.
  - **★ GAAP vs adjusted:** GAAP net income $133.7B (+31%) / GAAP diluted EPS $17.95 (+32%) is flattered by **~$5.0B of net OpenAI-investment gains (+$0.67 EPS)** — the adjusted non-GAAP $128.8B (+22%) is the cleaner read. MSFT now holds stakes in BOTH OpenAI and Anthropic (Q4 +$3.2B Anthropic gain).
  - **★★ Cloud + backlog exploded:** Microsoft Cloud $214.4B (+27%); **Azure +41% FY / +43% Q4** (demand>supply, spot-market pricing); **commercial RPO +84% to $678B** (+25% ex-OpenAI).
  - **★ Capex ramp + FCF fell:** FY2026 cash capex $115.9B (+80%); Q4 ~$41B; CY2026 ~$175–190B; **FY2027 growing**; OCF $55.4B/+30% but FCF fell to $19.6B; still FCF-positive + >$43B returned.
  - **★ §2.1 useful-life change** (NEW): extending DC/office building lives, effective FY2027; a finance→operating lease reclassification adjusting CY2026 capex ~$190B→$175B (NOT a spend cut) — flatters future margins + makes capex non-comparable.
  - **★★ Seats → seats + consumption** (the contested-leg answer forming): usage-based billing added to Copilot Cowork; Dynamics 365 usage-credit +4x QoQ; GitHub Copilot to usage-based (June); Copilot >30M seats. The AI-ARR construct ($37B) was **de-emphasized at Q4**; the 10-K still has no discrete AI revenue line.
  - Maia 200 (30% perf/$, 40% perf/watt; supports OpenAI + MAI) + Cobalt 200 (25+ DCs); Q1 FY2027 revenue guide $89.85–90.95B (+16–17%), Azure ~45% cc.
- **Placement:** **unchanged** — `layer: outside` + all five `*_tier: outside` (demand-side capex-payer, §3.21). A strong quarter reinforces the demand-source role, not a supply-side position.
- **Cross-vault propagation:** substantive [[hyperscaler-capex]] (row/summary/aggregate/backlog — RPO $678B, capex reframed, margins expanded, +$5.0B OpenAI mark) + [[what-could-go-wrong]] Entries 1/2/6 (+ Entry 3 freshness) — all NOT FIRED (the MSFT ROI-pass leg) + [[software-AI-moat-durability]] (scorecard → "Contested-but-adapting"; seats+consumption). Light [[AI-demand-durability]] + [[hyperscaler-custom-ASIC]] (Maia 200 / Cobalt 200). No-op: [[frontier-app-layer-value-capture]] (enterprise-moat home is software-AI-moat), [[AI-buildout-who-holds-the-risk]]/[[telecom-bust-analog]] (funding-intensity captured via hyperscaler-capex + what-could-go-wrong-6), [[forward-pe-watch]]/[[AI-credit-spread-watch]] (own skills), peers ([[GOOGL]]/[[AMZN]]/[[META]]/[[ORCL]] etc.), chokepoint pages.
- **Forward watch:** does margin expansion persist as capex intensity climbs; the §2.1 useful-life-change margin/capex impact through FY2027; whether a clean Tier-1 AI revenue line ever appears; whether the seats+consumption hybrid preserves per-customer monetization; the OpenAI RPO share; the META/AMZN legs of the ROI pass (transcripts pending) + NVDA (~late-Aug).
- **Key insight:** MSFT is the single strongest datapoint against the AI-capex-bubble bear this cycle — demand strengthened AND margins *expanded* (op margin to 45%, RPO +84% to $678B, Azure +43%, demand>supply), directly narrowing the capex-vs-revenue disconnect. But the honest reader tracks three things the strong print obscures: the useful-life accounting change (flatters margins, obscures the true capex trajectory), the OpenAI-investment gain flattering GAAP (+22% adjusted is the real growth), and the contested seat-leg the company itself is now hybridizing away from — the moat is durable on infra, adapting on seats.

---

## S196 — TDY (Teledyne Technologies) — 2026-07-29 — Q2 FY2026 (10-Q, quarter ended Jun 28 2026) + Q2 call

- **Sources:** Teledyne Q2 FY2026 10-Q (Tier 1, quarter ended Jun 28 2026) + Q2 FY2026 call (Tier 2, Jul 22 2026; Exec Chairman Robert Mehrabian / President & CEO George Bobb / EVP-CFO Steve Blackwood). **§2.11 N/A** (Sunday-nearest-Dec-31 FYE; week-scope → Q2 FY2026 ≈ calendar Q2 2026).
- **Prior baseline:** S131 (first-canonical, FY2025 10-K + Q1 FY2026 10-Q + Q1 call). TDY's **first true primary refresh** (S132/S133 were cross-refs). TDY = the Defense & Drones domain's **EO/IR sensor / seeker chokepoint owner** (`defense_tier 4`, the highest-conviction tier).
- **Headline:** A record quarter and a 2nd consecutive beat-and-raise — the defense/drone chokepoint thesis strengthened and the broad-cycle commercial short-cycle inflected positive; the honest counterweights all hold (+ one new one, a tariff-refund).
- **Key changes & new developments:**
  - **★ Record Q2:** net sales $1,662.5M (+9.8%); GAAP operating income $333.2M (+19.8%); **GAAP diluted EPS $5.37 (+21.2%)**; non-GAAP EPS +20.8%; total company margin 23.4% (+120bps). Book-to-bill **1.23×** (DI >1.4×), 11th straight quarter orders>sales, **~$5B backlog** (from ~$4.6B).
  - **★★ Guidance raised again (2nd straight):** FY2026 revenue **>$6.53B** (+$120M vs April; ~7% growth); non-GAAP EPS **$24.45–24.65** (+$0.55); Q3 non-GAAP EPS $6.05–6.15.
  - **Cash machine (the KTOS contrast):** OCF $315.2M, FCF $284.7M; net debt $1.69B / **1.1× — lowest since before FLIR** (~6 yrs).
  - **Defense (~30–35% of company):** guided high-single-digit + double-digit pockets; **unmanned ~$575M/+12%** (air+ground+underwater); **missiles/munitions $200–250M run-rate** + >$30M US-government manufacturing-upgrade investment (partial enacted-vs-requested conversion); **Black Hornet 4 selling**; picks-and-shovels IR-detector supply to all drone makers intact.
  - **★ NEW counterweight — a ~$10M net tariff-REFUND** (mostly Digital Imaging) aided DI margin ~120bps (of its 353bps gain) — a trade tailwind that could reverse.
  - **★ China squeeze (OQ#2) did NOT bite** — record results, margins up; the Q2 10-Q abbreviates the disclosure (rare-earth + magnets retained; germanium/gallium dropped; "could disrupt" framing).
  - **Commercial short-cycle inflected** (industrial inspection + healthcare X-ray + T&M) → commercial now guided mid-single-digit (from flat-to-low).
  - **Cleared the FY2025 EPS caveat** ($18.88 off the 10-K). **CEO structure unchanged** (Bobb CEO / Mehrabian Exec Chairman, same as Q1 — the verify-step "new leadership?" flag resolved via the baseline).
- **Placement:** **unchanged** — `defense_tier 4` (no AI tier/layer). A record beat-and-raise reinforces the highest-conviction chokepoint-owner tier; it is not a reframing trigger (honest-verdict-trigger discipline). The AI-adjacent slice (OQ#7) gained mild color (LeCroy datacenter-protocol/power-supply test) but stays broad-cycle.
- **Cross-vault propagation:** substantive [[drone-platform-commoditization]] (the value-migrates-to-sensor-chokepoint prediction quantified — unmanned $575M/+12%, DI margin 25%). Light [[rare-earth-magnet-chokepoint]] (squeeze not biting; disclosure abbreviated), [[china-exposure]] (High held; tariff-refund + not-biting), [[defense-drone-supply-chain]] (node confirmed w/ primary evidence; +TDY to tickers — missing since S131), [[forward-edge-tracker]] ("Chokepoints > platforms" Last moved — confirmation). No-op: [[AMPX]] (Black Hornet 4 = reinforcement not structural; supplier page), [[physical-AI-value-chain]] (positioning unchanged), peers ([[AVAV]]/[[MRCY]]/[[AXTI]]/[[TUOPU]]), [[short-interest]].
- **Forward watch:** does the raised guidance convert; Rogue1/LASSO quantification; ASP durability on cheap counter-UAS sensors; the tariff-refund recurrence; the China rare-earth bite in H2; the KTOS Q2 cross-prime (if ingested).
- **Key insight:** Teledyne is the vault's cleanest live proof of the "value migrates to the sensor chokepoint, not the airframe" thesis — Q2 put numbers on it (DI 25% margin, unmanned $575M/+12%, $5B backlog) on a record beat-and-raise — but the discipline holds: defense is still only ~30–35%, a tariff-refund flattered the margin, and management itself keeps tempering the surge. The profitable, FCF-rich, low-leverage profile is the structural opposite of the platform primes.

---

## S195 — AEHR (Aehr Test Systems) — 2026-07-29 — FY2026 (10-K, fiscal year ended May 29 2026) + Q4/FY2026 call

- **Sources:** AEHR FY2026 10-K (Tier 1, FY ended May 29 2026) + AEHR Q4/FY2026 call (Tier 2, Jul 14 2026; CEO Gayn Erickson / CFO Chris Siu). Annual US-filer set (Q4 folds into the 10-K; no separate Q4 10-Q). **§2.11 applies** (non-calendar filer; FY2026 ≈ calendar Jun 2025 – May 2026).
- **Prior baseline:** S6 (first-canonical, FY2025 10-K + Q3 FY2026 10-Q + Q3 call). AEHR's **first true primary refresh** (S25/S64/May cross-refs were not re-ingests). AEHR = the vault's **anchor Manufacturing-Equipment page** + primary anchor for [[wafer-level-siph-test]] (KGD wafer-level + package-level burn-in upstream of [[TSMC-CoWoS]]).
- **Headline:** The AI/advanced-packaging transition materialized at the Q4 inflection (rev +34%, non-GAAP GM 45%, positive non-GAAP income) with a strong forward setup — but FY2026 full year was still a GAAP loss on −15% revenue, and the guide is a 2.6–3× step-up with lumpiness + HBM-optionality caveats.
- **Key changes & new developments:**
  - **★ Q4 inflection:** revenue $18.8M (+34% YoY); **AI + silicon-photonics burn-in >80% of quarterly revenue** (vs 56%); **non-GAAP GM recovered to 45%** (+1,000bps); **non-GAAP net income +$3.6M / $0.11** (from a small loss); 3 customers >10%.
  - **★★ Honest-verdict crux — FY2026 full year still a GAAP LOSS:** revenue $50.0M (−15%); **GAAP net loss $(7.1)M / $(0.23)**; GAAP operating loss widened to $(14.1)M (R&D +21% to $12.6M / 25.3% of rev); the ~$8M GAAP↔non-GAAP gap is **ordinary SBC (~$6.8M) + Incal amortization — NOT a mark-to-market artifact** (contrast INTC/GEV/NVTS). Non-GAAP FY net income +$0.9M/$0.03; GAAP GM 35.3%.
  - **★★ Forward setup + fortified balance sheet:** record year-end backlog **$80.6M** (from $15.2M; ~$100.6M effective incl. transition-stub bookings); **$130–150M FY2027 guide (+160–200%)**; record **$41M April hyperscale Sonoma PO**; ~$97M FY2026 ATM raise → **cash $116.5M** (from $26.5M), no debt, capex only $2.1M.
  - **OQ6 (DTA valuation-allowance risk) RESOLVED — did not fire:** DTA retained with a $4.6M income-tax benefit despite the pretax loss.
  - **Silicon photonics broadened to TWO ramping customers** (lead + a new "global leader in networking products and solutions"); SiPh guided 15–20% of FY2027; the burn-in "market leader" claim reiterated (unverified).
  - **HBM/memory:** NAND-flash-leader benchmark completed; "sooner but not next year"; **explicitly excluded from the FY2027 guide** (revenue FY2028 at earliest) → [[HBM-oligopoly]] OQ#10 trigger NOT fired.
  - **★ Fiscal year-END change:** moving to the Friday-nearest-June-30 from FY2027 (June 27 2026 – June 25 2027), orphaning a ~4-week transition stub (May 30 – June 26 2026); ~$20M of bookings landed in it — cross-period comparability flag.
  - **Customer concentration EASED:** top customer 26.3% (from 67% two years ago); top-3 ~51%; consistent A–E labels across 3 years this filing. US now 41% of revenue (Asia 46%). SEMI/NEXUSTEST litigation (OQ5): Beijing patent office upheld two of AEHR's Chinese patents; ongoing.
- **Placement:** **unchanged** — `layer 3-4` + `photonics_tier 4`. The Q4 inflection + $130–150M guide + $116.5M war chest do not trip an upgrade (honest-verdict-trigger discipline: AEHR tests-not-makes photonics; still ~$50M FY2026). Photonics-tier-4 "real but indirect" tension strengthened but not resolved; the `equipment_tier`-absence flagged to Vic as optional codification (not a refresh action).
- **Cross-vault propagation:** substantive [[wafer-level-siph-test]] (two-SiPh-customer broadening; OQ#1 attach-rate + OQ#5 concentration-trajectory gained strengthen-direction evidence; provisional single-company status HELD). Light [[HBM-oligopoly]] (OQ#10 not fired), [[TSMC-CoWoS]] (KGD/Taiwan-CM demand echo), [[AI-demand-durability]] (order inflection), [[china-exposure]] (Low held; note refreshed). No-op: [[what-could-go-wrong]] (AEHR is an *excluded* company-level-risk example, not a tripwire), [[datacenter-photonics-supply-chain]] (canonical SiPh-test home updated — avoid duplication), peer pages ([[ONTO]]/[[COHU]]/[[FN]]/[[GLW]]/[[LITE]]).
- **Forward watch:** does the $130–150M FY2027 guide convert (2.6–3× step-up, lumpiness); steady-state margin at AI mix (Q4 45% vs FY 38.5%); an HBM/memory ORDER in FY2027; SiPh breadth beyond two customers; SEMI/NEXUSTEST outcome; FY2026/FY2027 boundary comparability (the transition stub).
- **Key insight:** A textbook equipment-cycle inflection read honestly — the exit-rate and order book turned decisively (Q4 +34%, $80.6M backlog, $130–150M guide) while the *reported* full year was still a GAAP loss on −15% revenue; the bookings-lead-revenue lag + management's own "it's always going to be lumpy / I'll believe it when I see the orders" is the discipline. Well-capitalized now removes the balance-sheet risk but not the execution risk.

---

## S194 — NVTS (Navitas Semiconductor) — 2026-07-29 — Q2 2026 (10-Q, quarter ended Jun 30 2026) + Q2 call

- **Sources:** NVTS Q2 2026 10-Q (Tier 1) + Q2 2026 call (Tier 2, Jul 27 2026; President & CEO Chris Allexandre / CFO Tonya Stevens / VP-IR Brett Perry). Calendar filer → **§2.11 N/A** (§2.11.1 calendar-aligned).
- **Prior baseline:** S92 (first-canonical, FY2025 + Q1 2026). NVTS's **first true primary refresh** (S99 was a cross-reference). NVTS = the vault's **first/anchor power-semiconductor canonical** (GaN + high-voltage SiC on the 800V-DC AI-datacenter transition).
- **Headline:** The Navitas 2.0 pivot is real, now **decisively well-capitalized** (post-$373M raise) and **finally sequentially inflecting** (+22% seq to $10.5M) — but still a **tiny-base, 2027-dependent, GAAP-optics-noisy, litigation-shadowed** story.
- **Key changes & new developments:**
  - **★★ Balance sheet transformed:** $373.2M H1 net ATM proceeds → **cash $557.4M** (from $236.9M year-end), **no debt**, ~50-quarter runway (OQ#7 RESOLVED); dilution ~232M→**261M shares**.
  - **★★ GAAP net loss $(228.2)M / EPS $(0.95) is a non-cash artifact** — a **$(203.1)M de-SPAC earnout-liability fair-value mark** (liability now **$0, fully recognized, no future charges**); read the **~$11.4M non-GAAP op loss** (INTC-escrowed-shares / GEV-Prolec pattern).
  - Revenue $10.5M (**+22% seq**, high-power +>50% YoY) — but **−27% YoY total** (mobile exit dragging the top line); Q3 guide **$13.5M/+28%**; AI-infra targeted >1/3 of revenue by year-end; mobile "insignificant" a quarter early.
  - **800V roadmap (call): four inflection points** (SiC AC/DC PSU H2 2026 → 800V sidecar mid-2027 → native 800V DC/DC in GPU trays late-2027/2028 → grid-to-rack SSTs 2028+); design wins are **2027-ramp pipeline, not revenue**; **NVIDIA still not named** (deflected — §3.6 asymmetry persists). New SAM lever: 1.2kV SiC JFET (~$1B by 2030).
  - **★ Supply DE-RISKED:** SiC now **dual-sourced** — X-Fab + **new Magnachip** (S-Korea; a **related-party** deal, subsequent event); GaN GlobalFoundries 8-inch. (Extraction's TSMC-GaN claim not in the 10-Q → not asserted.)
  - **★ NEW material legal cluster:** **Wolfspeed** patent-infringement (GaN & SiC, Jul 7) + **Renesas** trade-secret misappropriation (Jul 22, **names CEO Allexandre**), coordinated (Renesas ~39%-owns Wolfspeed), after NVTS dropped Wolfspeed as a wafer supplier. Largest customer <10%; single segment; no leadership change (Allexandre already CEO at S92).
- **Placement:** **HELD** — `layer 4` + `energy_power_tier 3` + photonics/memory/equipment/materials `outside` + `foreign_issuer false`. Sequential growth + the war chest do NOT trip an upgrade (Tier 3 = thesis-fit + execution risk on a $10M base; still 2027-dependent, NVIDIA unnamed) — honest-verdict-trigger discipline.
- **Cross-vault propagation:** Substantive — [[power-semis]] (NVTS 5-variant synthesis row: "well-capitalized small base," inflection + de-risked dual-foundry + litigation; runway ~14→~50 qtrs). Light — [[XFAB]] (Magnachip 2nd SiC source; NVTS SiC accelerating but now dual-sourced) + [[china-exposure]] (Low held; foundry base diversifying off Taiwan → US/EU/Korea). No-op — [[short-interest]] (Tier-5 feed-driven), [[NVDA-platform-integration]] (asymmetry unchanged), [[transformer-supply]]/[[MLCC-oligopoly]] (historical 8-K citation), peer power-semi pages (matrix baselines).
- **Forward watch:** does H2 hold the sequential pace + does AI-infra hit >1/3 of revenue (the target→number test); Wolfspeed/Renesas litigation outcome (any injunction risk to the GaN+SiC lines); Magnachip 2nd-source qualification; whether NVIDIA is ever named at primary.
- **Key insight:** The refresh flipped the risk profile without changing the tier: the **liquidity leg is gone** (a fortress $557M cash pile) and revenue finally turned up sequentially — but the **execution leg (design-win-to-revenue conversion, 2027-weighted) is unchanged**, GAAP is dominated by a one-time non-cash earnout mark (now closed), and a coordinated Wolfspeed/Renesas litigation cluster naming the CEO is a genuine new overhang. Well-funded + inflecting ≠ de-risked on execution — Tier 3 holds.

## S193 — GEV (GE Vernova) — 2026-07-28 — Q2 2026 (10-Q, quarter ended Jun 30 2026) + Q2 call

- **Sources:** GEV Q2 2026 10-Q (Tier 1) + Q2 2026 call (Tier 2, Jul 22 2026; CEO Scott Strazik / CFO Ken Parks / VP-IR Michael Lapides). Calendar filer → **§2.11 N/A**. Comments/guides ORGANIC (ex Prolec).
- **Prior baseline:** S37 (first-canonical, FY2025 + Q1 2026). GEV's **first true refresh** (intervening edits were cross-ref notes + a latest-alpha block).
- **Headline:** Strong beat + guidance RAISED again (rev → $45.5-46.5B; FCF → $11.5-12.5B); orders +88% to ~$24.2B; backlog $176.3B → $200B by 2027 — the power-infrastructure durability the vault tracks got STRONGER.
- **Key changes & new developments:**
  - Rev $11.1B (+22%); **adj EBITDA $1.2B (+71%), margin 11.3%**; Power 18.8% margin, **Electrification +68% rev / 18.4% margin (+390bps)** the breakout; **Wind still loss-making** $(275)M Q2 / ~$400M FY (the drag).
  - **Gas contract book: 100→116 GW** (≥125 year-end), SRAs 63 GW, **2031 slots >50% sold**; capacity 20→24 (2028)→30 GW (2030); **pricing +20%** vs Q4 2025.
  - **★ Prolec transformer platform scaling** — ~$900M Q2 revenue (from ~$500M Q1); **$800M H1 US transformer orders now fulfillable** (first-time, Prolec-enabled — directly relieves the US LPT bottleneck); $41B Electrification equipment backlog.
  - **★ SST reconciles the transformer-supply §4.3 flag** — 5 MW prototype built, H2-2026 hyperscaler delivery, 2027 commercial; DISTINCT from the DOE FASST utility demo (two tracks).
  - **Data-center ~36% of H1 orders** (>$5B Electrification + ~$5B Gas of ~$27.5B); ~20% of 116 GW; **on-site/islanded framing strengthened** — but **still no named hyperscaler**, and it's orders not revenue.
  - **Honest-verdict flags:** 6M net income $5.4B is driven by a **~$4.0B non-cash Prolec step-acquisition remeasurement gain** (Q1) + $210M XD-Grid gain (Q2); **6M FCF $9.9B is down-payment-driven** (~$6.4B WC benefit). Read adj/segment EBITDA. Buyback $7B of $10B YTD; China XD Grid exited (~$600M); small Robotech acq.
- **Placement:** **HELD** — `layer 4` + `energy_power_tier 3` + photonics/equipment `outside` + `foreign_issuer false`. The **Tier-2 promotion trigger (>15% DC revenue OR 2+ named hyperscalers) is materially STRONGER but does NOT cleanly fire** (orders≠revenue; no named hyperscaler) → **escalated to Vic as a Framework-7 human-owned call** (MU memory_tier-1 precedent). Layer 4-5 straddle unchanged (SST/EMS still pre-revenue).
- **Cross-vault propagation:** Substantive — [[transformer-supply]] (Prolec scaling + $800M US transformer orders + **§4.3 SST flag RECONCILED** + source-freshness cleared) + [[BTM-grid-bypass-workaround]] (Modality 3 on-site/islanded framing strengthened; freshness cleared). Light — [[what-could-go-wrong]] Entry 4 (power constraint NOT resolving — tripwire moved away; NOT FIRED; +GEV) + [[forward-edge-tracker]] "Power infrastructure > compute" (catalyst landed; vault view strengthened not falsified). No-op — [[commodity-supercycle-chokepoints]] (taxonomy row unchanged), [[hyperscaler-capex]] (GEV supply-side), [[ETN]]/[[CEG]]/[[VRT]] (mutual non-naming preserved), [[HALEU-fuel-chokepoint]] (BWRX-300 barbell only).
- **Forward watch:** a *named* hyperscaler + a disclosed data-center *revenue* share (the Tier-2 trigger); first SST *orders* + magnitude (Layer 5 trigger); the on-site-vs-grid-feed split; Wind H2 recovery; Prolec FY run-rate + Section-232 tariff drag; whether Project Kilby (Chevron→Microsoft) ever surfaces at primary.
- **Key insight:** The *operating* power-infrastructure thesis strengthened decisively (backlog→$200B, SRAs to 2031, pricing +20%, capacity 20→30 GW, guidance raised twice) — but two things stay honest: the eye-popping YTD net income + FCF are one-timer/down-payment-flattered (read adj EBITDA), and the data-center exposure is real in the *order book* (~36% of H1 orders) yet still not a named-hyperscaler, disclosed-revenue story — so Tier 3 holds, strengthened, pending Vic's Framework-7 call.

## S192 — INTC (Intel Corporation) — 2026-07-28 — Q2 2026 (10-Q, quarter ended Jun 27 2026) + Q2 call

- **Sources:** INTC Q2 2026 10-Q (Tier 1) + Q2 2026 call (Tier 2, Jul 23 2026; CEO Lip-Bu Tan / CFO David Zinsner / VP-IR John Pitzer). Non-calendar (Dec-27 FYE) but ~3-day offset = week-scope → **§2.11 N/A** (calendar Q2 2026).
- **Prior baseline:** S78 (first-canonical, FY2025 10-K + Q1 2026 10-Q + Q1 call). The page's **first true refresh** (intervening edits were a humanoid cross-thesis note + a latest-alpha block, not primary re-ingests).
- **Headline:** Operating turnaround real + accelerating (rev $16.1B/+25%, GAAP operating income swung POSITIVE to $1.8B, non-GAAP EPS $0.42 = 7th straight beat, DCAI +59% YoY at ~40% op margin, 18A ahead of internal targets) — BUT GAAP net loss $(11.0)B / EPS $(2.16) is a **non-cash $(12.5)B Escrowed-Shares mark-to-market**, not operating deterioration, and the Foundry-external thesis stays unproven ($(2.1)B loss on ~$293M external / no named customer) on a RAISED capex bet.
- **Key changes & new developments:**
  - **DCAI the standout:** revenue $6.26B (+59% YoY, +24% seq), op income $2.47B at ~40% margin (from 16%). CCPG $8.88B / $2.34B op income; AI PC ~2/3 of client mix (+26% seq).
  - **GAAP loss is a non-cash artifact:** $(12.5)B mark-to-market loss on the Escrowed Shares derivative (US-gov / Secure-Enclave equity structure marking up as the stock rose); non-GAAP EPS $0.42 is the clean read.
  - **Segment rename CCG → "Client Computing and Physical AI Group (CCPG)"** (§2.1 mid-year disclosure shift; prior periods restated; scope materially unchanged).
  - **Foundry execution improved** (18A/3/7 exceeded internal targets, 18A-P risk production, 14A PDK 0.9 on track for October) but **external traction still thin** (~$293M / $(2.1)B loss / no named customer); **capex RAISED** (2026 gross >$20B; 2027 "significantly above").
  - **Substrate/packaging constraint now primary-confirmed** (EMIB-T backlogs "very high"; substrates + T-glass named a "choke point"). Google Cloud "deepened collaboration" thin/call-only (internal AI-first framing; no scope). NVDA-$5B / SoftBank NOT confirmed at Q2. Cash $37.4B→$29.7B; debt →$50.5B (incl. $14.2B Apollo Ireland-SCIP reacquisition). Q3 guide ~flat seq (~$16.3B / ~42% GM / ~$0.38 EPS).
- **Placement:** **UNCHANGED** — `layer: "1, 2"` + photonics/energy_power/equipment/materials_tier `outside` + `foreign_issuer false`. No trigger fires (external Foundry $293M below the OQ#9 tier bar; no photonics; §2.1 no-directional-momentum-upgrade on the strong revenue).
- **Cross-vault propagation:** Substantive — [[foundry-competition]] (first *primary* Intel-foundry datapoint; disconfirming signal untripped; +INTC ticker), [[pcb-interconnect-substrate-chokepoint]] (substrate constraint → 3rd primary demand-echo after NVDA/AVGO; glass-core flag partial-verify; +INTC), [[AI-agentic-CPU-orchestration-reemergence]] (DCAI +59% reinforcement; graduated the qualitative CPU-ratio side). Light — [[what-could-go-wrong]] Entry 9 (buyer-side memory-tightness NOT FIRED; +INTC), [[TSMC-CoWoS]] (EMIB-T demand datapoint; +INTC), [[humanoid-robot-value-chain]] (CCPG "Physical AI" rename note, faint). No-op — [[HBM-oligopoly]] page (INTC not a supplier; captured via Entry 9), [[china-exposure]] (Low-Med unchanged), [[hyperscaler-capex]] (supply-side), [[forward-edge-tracker]] (declined — no high-conviction vault-vs-consensus divergence), [[NVDA-platform-integration]] (no Q2 NVDA re-mention).
- **Forward watch:** 14A PDK 0.9 landing on time (October 2026) + the first *named* external customer (resolves the Layer-2 exit-risk); the Escrowed-Shares mark will keep whipsawing GAAP each quarter (track non-GAAP/operating income); the Google Cloud collaboration's real scope; a named 14A customer would revisit the [[forward-edge-tracker]] decision.
- **Key insight:** This was the quarter the *operating* turnaround became undeniable (positive operating income, DCAI at 40% margin, 18A executing) — but the two things that matter for the *investment* thesis are still unresolved: the Foundry-external bet is bigger (capex raised) yet unproven (no named customer), and GAAP is now dominated by a non-cash government-equity mark that makes the headline EPS meaningless. Read Intel on operating income + non-GAAP + external-Foundry proof, not the GAAP line.

## S191 — NOW (ServiceNow) — 2026-07-28 — Q2 2026 (10-Q, quarter ended Jun 30 2026) + Q2 call

- **Sources:** NOW Q2 2026 10-Q (Tier 1) + Q2 2026 call (Tier 2, Jul 22 2026; McDermott / CFO Mastantuono / CPO Zavery). Calendar filer (§2.11 N/A).
- **Prior baseline:** S113 (first-canonical, Q1 2026). The page's first refresh — **and the first *refresh* of a [[software-AI-moat-durability]] scorecard name** (MSFT/NOW/PLTR/DDOG were creations).
- **Headline:** Strong beat; the research-goal verdict "Contested, leaning durable" HELD and the durable side STRENGTHENED — ServiceNow AI ACV crossed $1B (accelerating), the monetization the Q1 verdict awaited. The contested disclosure gap persists.
- **Key changes:**
  - **★ AI ACV crossed $1B** (+40% QoQ net-new, accelerating; $1.5B end-2026 target); agentic-in-production +9×/9mo; 5+-AI-product deals +5.5× YoY (tripling $1M+ AI deals). The Q1 ">$600M tracking $1B" materialized.
  - 50%-non-seat held; hybrid pricing; AI-native SKU uplift 20-30% / ProPlus >30%; L1 agents auto-close 80-85% of requests.
  - Subscription $3.877B (+23% cc, 150bps beat); cRPO $13.2B (+21.5% cc, 200bps); non-GAAP op margin 29.5% (300bps); renewal 98%; 658 customers >$5M ACV. **Guidance RAISED** (FY26 subscription $15.755-15.770B; op margin 31.5%).
  - **★ Contested side UNCHANGED (honest-verdict):** AI still call-only bookings (no clean Tier-1 line); organic-vs-inorganic deflected again (OQ#1 + #3 stay open). US federal a tailwind (not a DOGE headwind); no new M&A / buyback / leadership change; CEO promotional-not-combative.
- **Placement:** unchanged — `layer: outside` + all-outside (documented §3.21 app-layer-consumer; flag already resolved S189).
- **Cross-vault propagation (tight — single-research-goal app-layer name):** [[software-AI-moat-durability]] (NOW scorecard row + validation para — verdict held/strengthened; first scorecard *refresh*) + light [[what-could-go-wrong]] Entry 2 (seat-leg datapoint; NOT FIRED). No-op: [[china-exposure]] / [[frontier-app-layer-value-capture]] / [[AI-demand-durability]] / [[AI-implementation-deployment-layer]] (NOW not a member of the latter two).
- **Forward watch:** the clean-AI-revenue-line + organic-vs-inorganic disclosure (OQ#1/#3 — the persistent contested items); seat deflation at portfolio scale; Q3 (early Oct).
- **Key insight:** The AI monetization finally showed up in the number (AI ACV crossed $1B, accelerating) — the durable side of the seat-incumbent-converting thesis strengthened. But the two disclosure gaps that *define* the "contested" verdict (no clean AI revenue line; no organic-vs-inorganic split) are unchanged, so the verdict strengthens without resolving. Materialization ≠ transparency.

---

## S190 — GOOGL (Alphabet) — 2026-07-28 — Q2 2026 (10-Q, quarter ended Jun 30 2026) + Q2 call

- **Sources:** GOOGL Q2 2026 10-Q (Tier 1) + Q2 2026 earnings call (Tier 2, Jul 22 2026; Pichai / CFO Ashkenazi / Schindler). Calendar filer (§2.11 N/A).
- **Prior baseline:** S115 (first-canonical, Q1 2026). The page's first refresh.
- **Headline:** Strong, capex-heavy, demand-confirming — the capex-payer signal *strengthened* and several standing-watches were touched (none fired). Capex guide RAISED to $195-205B on demand-pull; Cloud +82% / backlog $514B; external TPU sales began recognizing revenue.
- **Key changes & new developments:**
  - **★ FY2026 capex RAISED to $195-205B** (from $180-190B), attributed to "acceleration in the delivery of capacity to meet growing demand" — a *cleaner* demand-pull signal than Q1's Intersect-energy raise. Q2 capex $44.9B (60/40 server/DC); 2027 "increase significantly."
  - **★ Google Cloud $24.8B/+82%** (accelerating from +63%), op income $8.8B / 35.6% margin (from 20.7%); **backlog $514B** (+>$50B seq); "supply-constrained for multiple quarters" (renting third-party capacity Q3 bridge).
  - **★ External TPU sales began recognizing revenue** — delivered to customer data centers first time in Q2 (majority 2027); captive silicon → merchant offering (milestone; deepens the AVGO partnership + NVDA competition).
  - **★ Financing regime:** debt $16B→$100B TTM + June $80B equity raise; Q2 FCF −$5.9B (capex > OCF) — the FCF-below-capex dynamic now at a 2nd fortress mega-cap, but milder than ORCL (fortress balance sheet). Energy named as forward P&L pressure. Net income again equity-securities-gain-inflated (op income the clean read).
- **Placement:** **unchanged** — `layer: outside` + all-outside; now a DOCUMENTED §3.21 value (capex-payer sub-role); OQ1 placement-codification RESOLVED (S189).
- **Cross-vault propagation (connections-focused):** [[hyperscaler-capex]] (GOOGL row + aggregate ~$655-735B + dynamic-#8 financing rung — the capex watch) · [[what-could-go-wrong]] Entries 1/2/6 (the queued Q2-ROI pass — all NOT FIRED; +GOOGL) · [[AI-demand-durability]] (Q2 demand update) · [[hyperscaler-custom-ASIC]] (TPU-revenue milestone) · light [[forward-edge-tracker]] (custom-silicon entry advances vault view) + [[AI-credit-spread-watch]] (backdrop, not a dial). No-op: [[china-exposure]] / [[frontier-app-layer-value-capture]] / [[software-AI-moat-durability]] / [[nvidia-supply-chain-commitments]].
- **Forward watch:** capex ROIC at the 2027 step-up (FCF now negative); external-TPU scale + NVDA competition; Cloud margin net of the Q3 third-party bridge; the queued Q2-ROI pass's remaining legs (MSFT/META/AMZN ~7/29-30; NVDA ~late-Aug).
- **Key insight:** The demand signal got *stronger*, not weaker, at the exact quarter the bear case (capex-durability / AI-ROI) was being stress-tested — a guidance *raise* on demand-pull, an accelerating +82% Cloud, a $514B backlog, and captive silicon crossing into a merchant business. The only intensifying risk is the funding mix (debt + negative FCF), and on a fortress balance sheet that reads as mix, not stress.

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
