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
