# MLCC supplier landscape — the ownership / exposure map (R3 + adversarial verification)

**Date:** 2026-06-10 · **Tier:** 3 (independent research — company results + industry estimates + trade press; cite, don't treat as fact)
**Produced by:** 3-researcher + 1-adversarial-verifier team · **Seed:** `raw/notes/video-intel/2026-06-07_nico-alpha_mlcc-next-memory.md`
**Companion report:** `raw/research/mlcc-ai-datacenter-bottleneck-report.md` (the bottleneck thesis + bear case + evidence table)

---

## VERDICT (one paragraph)

The high-end AI-server MLCC chokepoint has **one full-stack owner (Murata), one credible volume challenger (Samsung Electro-Mechanics), and one high-elasticity niche specialist (Taiyo Yuden)** — with a long tail (TDK, Kyocera, Yageo, Walsin) that rides spillover but does not own the AI-grade bin, and a Chinese tier (Three-Circle, Fenghua) that is real on volume and domestic-China AI servers but unproven at the NVIDIA-chain frontier. The chokepoint stack runs **powder → high-layer-count process/yield → design-in qualification**, and **Murata is the only company present at all three levels** (in-house + JV barium-titanate powder; ~1,000-layer process at scale; SimSurfing PDN design-tool entrenchment) — its FY2026 guidance of **server-related capacitor sales +85–90% YoY** is also the cycle's best primary-source evidence. Important honesty notes from verification: every **AI-server-segment share figure is a sell-side estimate, not disclosure** (Korean press: SEMCO ~40% / Murata ~45%; Chinese media: Murata ~70% — the weakest figure; Murata's president claims ">50% of advanced MLCC"); and investor **access is asymmetric** — Murata has a workable US ADR (MRAAY), Taiyo Yuden's ADR is illiquid, and SEMCO is KRX-only.

---

## 1. Murata Manufacturing (TSE 6981) — the integrated incumbent (rank #1)

**Financials (FY2025, ended 2026-03-31 — own earnings release deck, 2026-04-30; confirmed-primary, spot-checked by the verifier):**
- Revenue **¥1,830.9B** (record). Operating profit **¥281.8B** (+0.8%) → ~15.4% OP margin (held back by SAW-filter/MEMS impairments + price declines elsewhere).
- **Capacitors: ¥936.4B, +12.6% YoY = 51.1% of revenue** — over half the company. Murata's wording: revenue "mainly servers" increased.
- **FY2026 guidance:** revenue ¥1,960.0B (+7.1%); OP **¥380.0B (+34.8%)** "on stronger data-center-related demand, mainly capacitors"; capacitors ¥1,061.7B (+13.4%).
- **Server-related capacitor sales guided +85–90% YoY** — the single most important primary datapoint in this research.
- Capex **¥250.0B FY2026, which INCLUDES ~¥40B of an ~¥80B additional capacitor program** (~¥40B FY2026 + ~¥40B FY2027) aimed at datacenter capacitors. (Verifier correction: do not state "¥250B + ¥80B" — that double-counts.)
- Capacitor ASP guided **+5–10%, explicitly mix-driven** ("small size and large capacity mix improvement"); the company-wide OP bridge assumes a **¥73B price decline**. See the companion report's evidence table on the contested "15–35% MLCC hike."
- New Izumo building completed April 2026 (¥47B), capacity ramping Q4 2026 (Murata corporate news — primary).

**Structural position:** the only maker controlling all three chokepoint layers — (a) **powder**: in-house barium-titanate plus the MF Material JV (with Ishihara Sangyo + Fuji Titanium, re-established 2023); (b) **process**: world-first 0603 100μF (2024) and 0402 47μF (2025) mass production; (c) **qualification**: SimSurfing design platform (free MLCC SPICE/s-parameter models incl. DC-bias derating) entrenches Murata part numbers in customer PDN designs — once a board is qualified, switching is costly. President Nakajima (May 2026): high-end inquiries ≈ 2× capacity; claims **">50% share of advanced MLCC"**.
**Share (overall MLCC):** ~32–40% depending on source/basis (TrendForce at the high end; methodology undisclosed). **Weakness:** not a pure play — smartphone RF drag and impairments hit FY2025; the AI-server slice, while surging, is still a minority of even the capacitor segment.
**Access:** Tokyo 6981; US OTC ADR **MRAAY** (the most liquid Japanese MLCC ADR — single-source).

## 2. Samsung Electro-Mechanics / SEMCO (KRX 009150) — the scale attacker (rank #2)

⚠️ **Disambiguation:** Samsung's **components** affiliate (MLCC, FC-BGA substrates, camera modules) — NOT Samsung Electronics, the memory maker.

**Financials (CY2025 — own newsroom release, Jan 2026; confirmed-primary):**
- Revenue **KRW 11.3145T (+10%, record)**; OP **KRW 913.3B (+24%)** → ~8.1% OP margin.
- Q4 2025: revenue +16%, OP +108%; **Component Solution (MLCC) division Q4 revenue KRW 1.3203T, +22% YoY**, driven by "expanded supply of MLCCs for AI/servers and power applications."
- 2026 outlook (own words): increase high-value AI/industrial supply; growth "fueled by expanding global AI infrastructure investment." Q1 2026 call: demand exceeding capacity; **legally binding long-term MLCC supply agreements with AI big-tech customers**; ~$1.2B Vietnam capex.

**Utilization (verified):** **~99% MLCC utilization Q3/Q4 2025** with next year's output reportedly sold out (Seoul Economic Daily 2025-12-10; trough **59% Q1 2023** per Korean press citing SEMCO's own quarterly disclosures). Capacity: Busan + Tianjin (full) + Philippines; **third Calamba (Philippines) plant → mass production 2027**; reportedly building an MLCC-embedded substrate line in Vietnam for AI packaging (DigiTimes 2026-04-14 — single-source). Weighing 5–10% MLCC price hikes, partly to curb channel hoarding (DigiTimes; TrendForce).
**Share:** overall ~23–24% (secondary). The **"~40% of AI-server MLCC"** figure traces to Korean press/sell-side (vs Murata ~45%), NOT a SEMCO filing — flag as estimate; it conflicts with Chinese-media "Murata ~70%."
**Weaknesses:** conglomerate mix (substrates + camera modules dilute the MLCC signal); ~8% OP margin (half Murata's); merchant powder dependence (one chokepoint layer not owned).
**Access:** **KRX 009150 only** (common; 009155 pref). No US ADR/GDR found — the worst access of the three majors for a US-account investor.

## 3. Taiyo Yuden (TSE 6976) — the pure-play with the thinnest cushion (rank #3)

**Financials (FY ended 2026-03-31 — results via company library + earnings digests; confirmed-secondary):**
- Net sales **¥355.3B (+4.1%)**; OP **¥19.9B (+91.2%)** → ~5.6% OP margin; net profit **¥14.8B (~5.4×)** — explicitly AI-server-MLCC-driven.
- **Purity: highest of the three — capacitors ≈ 68% of revenue** (own segment data, FY ended Mar 2025: ¥232.1B of ¥341.4B).
- Momentum: Jan–Mar 2026 orders **¥111.1B (+23% YoY; first >¥100B quarter in ~5 years); MLCC book-to-bill 1.31**. FY2027 guidance: sales ¥384B (+8.1%); OP ¥30B (+50%); **AI-server MLCC revenue +~80%**.
- Price increases effective **May 1, 2026** across MLCC/inductors/RF (customer notice via trade press; TrendForce sizes 6–13% on consumer/low-mid + some auto grades — note: smaller than the contested Murata high-end figure).

**Structural position:** the **embedded/substrate-buried MLCC first-mover** — 1005/0402 22μF (MP Aug 2025) and 2012/0805 100μF (MP Nov 2025), both explicitly for AI-server IC power lines (primary). This is its most chokepoint-like niche (the CPO-analogous "move the part next to the die" direction). Low-ESL portfolio fits GPU decoupling.
**Weaknesses:** thinnest margins (~5.6% OP vs Murata 15.4% / SEMCO 8.1%); smallest scale; no large disclosed capex program found this cycle (gap, not negative finding) — the **cycle-taker, not the chokepoint-setter**. Elasticity is the inverse of durability.
**Access:** Tokyo 6976; US OTC **TYOYY exists but is very illiquid** (single-source) — practical access is the Tokyo line.

## 4. The second tier (spillover, not ownership)

- **TDK (TSE 6762; ADR TTDKY):** top-5 MLCC maker but MLCC is a minority business (batteries, HDD heads, sensors dominate); automotive-reliability-led MLCC strategy; embeds thin-film capacitors (TFCP) in substrates (primary). Great company, diluted MLCC thesis — wrong vehicle for this chokepoint.
- **Kyocera (TSE 6971; ADR KYOCY):** mid-single-digit share; reportedly **doubled low-ESL MLCC capacity for AI-server demand** (single-source); sprawling conglomerate — relevant niche, immaterial to group earnings.
- **Yageo (TWSE 2327; LSE GDR unverified):** global **#3 in MLCC** (TrendForce DataTrack ranking). 2025 revenue NT$132.93B (+9.3%); **AI-related revenue 10–12%** and rising; KEMET/Pulse acquisitions moved it up-market — but trade press is consistent that **Japan+Korea hold >80% of AI-server-grade MLCC**; Yageo is the mid-range consolidator riding spillover.
- **Walsin Technology (TWSE 2492):** Q1 FY2026 (own call, 2026-05-27): revenue NT$9.56B (+9.5%); GM ~17.9%; **MLCC = 46.4% of revenue**; utilization ~80% (deliberately held back for pricing leverage); capex only NT$0.5–1B/yr; president: price hikes "inevitable," AI-server passive usage to ~4× 2025→2027. High MLCC mix + honest cycle leverage, but tiny capex and mid-range positioning = **price-taker**.

## 5. The Chinese tier (volume share, not yet the AI-grade frontier)

Combined China-maker global share ~**10%** (2H 2024, TrendForce-derived) — overwhelmingly consumer/mid-range.

- **Chaozhou Three-Circle / 三环 (300408.SZ):** the most vertically capable Chinese ceramics platform (own materials); reportedly mass-producing **AI high-capacity MLCC for domestic Chinese servers** with ~1μm dielectric layers; stock +155% since April 2026 (market cap >¥250B) — the re-rating has already happened. Closest Chinese name to real materials depth; **no verified NVIDIA-chain qualification**.
- **Fenghua Advanced (000636.SZ):** H1 2025 revenue ¥2.391B (+15.2%), net profit +143.6%; Xianghe high-end base completed April 2026 — but disclosed expansion is in **resistors/inductors, not AI-server MLCC**; stock +138% in 20 trading days (early June 2026) — the hype tail of the trade.
- **EYANG:** consumer/mid-range; the "002841" ticker could NOT be verified — check before any vault mention.
- **Catch-up timeline:** no credible source gives one. The structural tells (sub-100nm powder, thousand-layer yield, multi-year server qualification) argue **years (~2–3 plausible for the 2nd tier's best)**; domestic Chinese AI servers are a parallel demand pool needing no Western qualification — the bear-case vector.
- **Most chokepoint-relevant Chinese name is upstream:** **Sinocera / 国瓷材料 (300285.SZ)** — described as the world's #2 barium-titanate powder producer with >80% of China's domestic powder market (single-source).

## 6. Upstream — the powder layer (the quiet second chokepoint)

- **Merchant barium-titanate powder is concentrated:** **Sakai Chemical (TSE 4078)** is the largest merchant maker (~25–28% global share per market-research estimates — not from Sakai IR; financials not pulled, gap), followed by Ferro (US, ~20%), **Nippon Chemical Industrial (TSE 4092, ~14%)**, Fuji Titanium (unlisted), KCM, and China's Sinocera. Hydrothermal-synthesis nano-BT is the high-end gate.
- **The key structural fact:** **Murata self-supplies** (in-house + the MF Material JV) while SEMCO and most others buy merchant powder — so the powder layer is a real chokepoint, but its biggest potential customer is insulated from it. That caps merchant pricing power against the #1 maker while preserving it against everyone else.

## 7. Ranked chokepoint-quality table (durability × business health — NOT a buy list)

| Rank | Name | Chokepoint quality | Business health | Access |
|---|---|---|---|---|
| 1 | **Murata (6981.T)** | Highest — powder + process + PDN-qualification, all three layers; ">50% advanced MLCC" (self-claimed) | Strong: record revenue, 15.4% OP → guided ~19.4%; funded capacity adds | Tokyo + MRAAY ADR |
| 2 | **Samsung Electro-Mechanics (009150.KS)** | High in the AI bin (share contested 40% vs Murata's 45/50/70 claims); merchant powder = one layer unowned | Strong: record results, 99% utilization, binding AI big-tech contracts, Philippines expansion | KRX only (worst access) |
| 3 | **Taiyo Yuden (6976.T)** | Medium-high niche — embedded-MLCC first-mover, low-ESL | Weakest of the three (5.6% OP); purest exposure (~68% capacitors) = biggest elasticity both ways | Tokyo; TYOYY illiquid |
| 4 | **Sakai Chemical (4078.T)** | Real layer-chokepoint (largest merchant nano-BT powder) — but Murata self-supplies | Not assessed from IR (gap — verify before vault use) | Tokyo small-cap |
| 5 | **Kyocera (6971.T)** | Niche (low-ESL capacity doubled) | Conglomerate-diluted | Tokyo + KYOCY |
| 6 | **TDK (6762.T)** | Modest — MLCC non-core | Strong company, wrong vehicle | Tokyo + TTDKY |
| 7 | **Yageo (2327.TW)** | Low-medium — #3 scale, below the AI-grade line | Solid | TWSE (+GDR unverified) |
| 8 | **Walsin (2492.TW)** | Low-medium — high-cap mid-range price-taker | OK; highest-beta Taiwan expression | TWSE |
| 9 | **Three-Circle (300408.SZ)** | Low today at the frontier; real ceramics depth; domestic-AI pool | Healthy; already +155% since April | A-share / Stock Connect |
| 10 | **Fenghua (000636.SZ)** | Low — expansions aren't AI-MLCC | Improving but small; hype tail | A-share |

## 8. Claims that could not be verified (or that conflict) — carry these flags

1. **AI-server-segment shares conflict outright** (Korean 40/45 vs Chinese-media "Murata ~70%" vs Nakajima ">50% advanced") — no disclosure-grade source exists; always present as a provenance-labeled range.
2. **Murata overall share spread** ~32–40% — methodology (value vs units) never disclosed.
3. **SEMCO utilization path** — endpoints solid (59% Q1'23 trough, 99% late-2025); the intermediate ">80% in 2024" leg unpinned.
4. **MRAAY/TYOYY liquidity specifics** — single Substack source.
5. **EYANG ticker/financials** — unverified.
6. **Murata "100nm powder vs Korean 300–500nm"** — single-source.
7. **Taiyo Yuden capex program this cycle** — not found (gap).
8. **Sakai / Nippon Chemical financials from their own IR** — not pulled; powder shares rest on market-research reports.

## 9. Recommended sequencing for vault primary-source ingests

1. **Murata (6981.T)** first — the full-stack owner, the best primary disclosure (the Apr 30 deck already verified), a workable ADR, and the +85–90% server guide as the testable claim. Japan/EDINET filer — same ingest pattern as [[HARMONIC]].
2. **Taiyo Yuden (6976.T)** second — purest exposure + the embedded-MLCC niche; results verify the elasticity story.
3. **Samsung Electro-Mechanics (009150.KS)** third — the Korean-filer ingest pattern is new for the vault (first KRX name); worth it once the theme page needs the challenger leg substantiated.
4. Sakai Chemical only if the powder layer becomes load-bearing.

*Report compiled 2026-06-10 from researcher R3 + adversarial verifier V. All share figures are estimates unless tied to a company document. Tier-3 anchor per CLAUDE.md §3.13/§4.6 — primary-source verification required before any claim becomes load-bearing on a canonical page.*
