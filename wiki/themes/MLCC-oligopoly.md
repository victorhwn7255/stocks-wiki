---
type: theme
tickers: [NVDA]
last_updated: 2026-06-10
---

# MLCC oligopoly — the "new memory" claim, tested

*Tier 3-anchored theme (per CLAUDE.md Section 3.13). Anchored on two research reports in `raw/research/` — `mlcc-ai-datacenter-bottleneck-report.md` (the technical case + bear case + evidence table) and `mlcc-supplier-landscape-report.md` (the ownership/exposure map) — built by a multi-researcher + adversarial-verification process from web, company-document, and sell-side-via-media sources, seeded by a Tier-3 video intel note (`raw/notes/video-intel/2026-06-07_nico-alpha_mlcc-next-memory.md`). All figures are Tier-3 — verify against primary filings before treating any claim as load-bearing. Structural framing only, not buy/sell.*

## Thesis role

The AI constraint story keeps moving down the stack: GPU → HBM/memory → power infrastructure — and now, per Goldman Sachs' late-May 2026 framing, MLCC: the tiny multilayer ceramic capacitors that stabilize power to the GPU, HBM, and ASIC. Goldman called MLCC the "new memory" — the 3rd-largest AI-server BOM item after GPU and memory, with AI-server demand growing ~4.3× FY2025→FY2030 against industry capacity "locked at ~10%/yr" (bottleneck report, citing GS coverage via cls.cn / Tencent / 21jingji, May 31–Jun 1 2026 — attribution only; the GS notes are non-public). This is the same stacked-bottleneck pattern the vault tracks at [[HBM-oligopoly]] and [[power-semis]]: each time one constraint clears, the next one down binds.

**The honest verdict, up front (from the bottleneck report's verdict):** high-end AI-server MLCC is a **quality-but-cyclical position with one genuinely structural kernel** — the top-bin chip-adjacent and embedded-in-substrate parts. It is **not yet a memory-grade durable chokepoint**, and it is more than a pure theme-spike. The cycle has memory's *story*; so far it has only one quarter of memory's *evidence*. The "new memory" label is a Goldman narrative, carried here under strict Tier-3 attribution — not a vault conclusion.

## What makes high-end AI-server MLCC hard

**The job.** MLCCs are passive stabilizers in the power-delivery network. The critical function for AI silicon is decoupling: GPU load swings cause near-instant current spikes, the voltage regulator is electrically far away, and chip-adjacent capacitors bridge the microsecond gap. Without them: voltage droop, downclocking, crashes (bottleneck report, citing Murata 0603-100μF product release, 2024-07-25 — primary-confirmed).

**The usage jump.** A standard enterprise server uses ~1,000 MLCCs; Samsung Electro-Mechanics' own newsroom says an AI server uses **more than 10× a general-purpose server's** (bottleneck report, citing SEMCO newsroom, 2025-07-21 — a company claim, primary-confirmed). Per-rack counts are weaker: the widely-circulated "~440,000 per NVL72 rack" traces only to anonymous brokerage field research, and the seed video's "~100k/rack" matches a GPU-boards-only count — no teardown or maker unit count exists. The reports' discipline: **use ranges and name the unit** (per-node vs per-rack).

**The five-spec problem.** AI parts must be high-capacitance, low-ESL, small-case, high-voltage-tolerant, and high-reliability at once. The moat is materials plus process: barium-titanate powder at the sub-100nm class, stacked as ~2μm layers up to ~1,000 layers, nickel inner electrodes, sintered without cracking — yield is the chokepoint. Ultra-high-cap AI parts reportedly run ~40% yields and 50+-day cycles, which is why AI servers consume only 2–3% of global MLCC units but ~10% of capacity (bottleneck report, citing CICC via BigGo, 2026-06-06 — single-source).

**The 800V transition (primary-confirmed).** [[NVDA]] announced an 800 VDC rack architecture starting 2027, aligned to Kyber rack systems (576 Rubin Ultra GPUs), to support 1 MW racks (bottleneck report, citing NVIDIA developer blog, 2025-05-20, + Navitas 8-K exhibit, 2025-05-21). High-voltage stages need correspondingly rated parts — but no capacitor maker has quantified the incremental MLCC demand; that link is engineering inference. The chip-adjacent volume story sits on the low-voltage side; these are complementary claims, not the same claim.

**The embedded-MLCC trend (the most chokepoint-like direction).** Capacitors buried in the package substrate, next to the die, to cut loop inductance — the same "move the critical part next to the chip" logic as [[cpo-integration]]. Taiyo Yuden has two embeddable families in mass production for AI-server IC power lines (1005/0402 22μF, Aug 2025; 2012/0805 100μF, Nov 2025 — both primary-confirmed); SEMCO is reportedly building an MLCC-embedded substrate line in Vietnam (bottleneck report, citing DigiTimes, 2026-04-14 — single-source). The direction is confirmed multi-vendor; "requirement for next-gen AI packages" status is not.

## The oligopoly map

No MLCC maker has a vault page; all names below are plain text. Per the landscape report's ranked table (durability × business health — not a buy list):

| Player | Position | Key evidence (all Tier-3 unless marked primary) |
|---|---|---|
| **Murata** (Tokyo 6981) | The only full-stack owner: in-house + JV barium-titanate powder, ~1,000-layer process, SimSurfing PDN design-tool qualification lock-in | FY2025 capacitors ¥936.4B = 51.1% of ¥1,830.9B revenue; **server-related capacitor sales guided +85–90% YoY FY2026** — the cycle's best primary evidence (landscape report, citing Murata earnings deck, 2026-04-30) |
| **Samsung Electro-Mechanics** (KRX 009150) | The scale attacker — Samsung's *components* arm, NOT Samsung Electronics the memory maker | ~99% MLCC utilization Q3/Q4 2025, next year's output reportedly sold out; legally binding long-term supply agreements with AI big-tech (landscape report, citing Seoul Economic Daily 2025-12-10 + SEMCO Q1 2026 call); buys merchant powder — one chokepoint layer unowned; KRX-only, the worst access of the three |
| **Taiyo Yuden** (Tokyo 6976) | The pure-play cycle-taker — purest exposure (~68% capacitors) + embedded-MLCC first-mover | OP margin just ~5.6% (vs Murata 15.4%, SEMCO 8.1%) despite an AI-driven ~5.4× net-profit jump; FY2027 guide: AI-server MLCC revenue +~80% (landscape report, citing company results via earnings digests) |
| TDK / Kyocera / Yageo / Walsin | Spillover, not ownership | MLCC non-core (TDK), conglomerate-diluted (Kyocera), mid-range consolidator (Yageo, AI ~10–12% of revenue), high-cap price-taker (Walsin); trade press is consistent that Japan+Korea hold >80% of AI-server-grade MLCC (landscape report) |
| Three-Circle / Fenghua (China A-share) | Volume share (~10% combined China), domestic-China AI pool, unproven at the NVIDIA frontier | Three-Circle reportedly mass-produces AI high-capacity MLCC for domestic Chinese servers (~1μm layers) — no verified NVIDIA-chain qualification; Fenghua's disclosed expansion is resistors/inductors, not AI MLCC (landscape report) |
| Sakai Chemical (Tokyo 4078) + powder tier | The quiet upstream layer — largest merchant nano-barium-titanate maker (~25–28% share per market-research estimates, not Sakai IR) | The key structural fact: **Murata self-supplies powder** while SEMCO and most others buy merchant — so the powder chokepoint is real, but its biggest potential customer is insulated from it (landscape report) |

**The share-figure warning.** Every AI-server-segment share number is a sell-side estimate, not disclosure, and they conflict outright: Korean press/sell-side puts SEMCO ~40% / Murata ~45%; Chinese media says Murata ~70% (the weakest figure); Murata's president Nakajima claims ">50% of advanced MLCC" (May 2026, company-attributed). No disclosure-grade source exists — any vault use must present the range with provenance (both reports, evidence-table claim #3).

## The HBM comparison

The "new memory" analogy against [[HBM-oligopoly]], tested (bottleneck report, Part 3):

**Where it holds:** (a) concentration at the high end — the AI-grade bin is reported as a Murata+SEMCO near-duopoly (~90% combined per Korean press — estimate, see above); (b) a real vertically-integrated process moat (in-house powder, thousand-layer yield, in-house equipment) — the structure behind GS's ~10%/yr capacity ceiling; (c) qualification lock-in — parts are designed into the PDN with vendor sim models, and switching after board qualification is costly, like HBM qualification on a GPU package; (d) both ride the same NVIDIA platform cadence, with content per rack rising each generation.

**Where it breaks:** (a) **the long tail** — HBM has three makers on earth; MLCC has a second tier and a Chinese tier already making "AI high-capacity" parts for domestic Chinese servers; (b) **dollar stakes** — HBM is ~25% of a Rubin rack's cost (Morgan Stanley estimate); MLCC at $1.5–4.3k/rack is **<0.1% of rack cost**, so buyers have little incentive to defend the oligopoly the way GPU roadmaps defend HBM; (c) **capacity answers faster** — MLCC expansion is buildings, presses, and kilns on known process (12–24 months), not leading-edge DRAM + TSV (3+ years); (d) **no generational lockout** — HBM4-vs-HBM3e creates hard gates; MLCC progress is continuous, so trailing players stay partially substitutable on the less-extreme parts of the BOM.

**Net:** the analogy is directionally fair **only for the top-bin chip-adjacent and embedded parts**. For the rest of the rack BOM, the tail can and will absorb demand.

## The bear case

Argued as hard as the bull, per the bottleneck report (Part 4):

1. **The cycle rhyme is verified.** Standard-spec MLCC spot prices rose 5–10× in the 2017–mid-2018 super-cycle; the 2019 unwind was severe — **Yageo 2019 revenue −34.5%** as hoarded channel inventory cleared (bottleneck report, citing Smith retrospective + Taipei Times, 2019-12-09 — confirmed). Every element of that cycle — hikes, spot surges, lead-time blowouts — is present now.
2. **Double-booking is documented right now.** TrendForce's May 18, 2026 release (confirmed): Taiwan/China distributors hoarding consumer-grade X5R parts, "declining actual orders from ODMs alongside surging orders from channels," explicit double-booking risk. Aggregate MLCC ASPs were still *falling* as of early May — the boom is narrow, and part of the "shortage" is hoarding, not consumption.
3. **The supply wave is funded and dated.** Murata's Izumo building is complete (April 2026, ¥47B; capacity out Q4 2026) plus an ~¥80B AI-capacitor capex program; SEMCO's third Philippines plant produces H2 2027; Walsin, Yageo, and Fenghua are all adding. That wave lands 2027–28 — into hyperscaler capex growth that decelerates on consensus from ~50–64% (2026) to ~13% (2027) and ~5% (2028) (bottleneck report, citing CreditSights + Moody's via MUFG); see [[hyperscaler-capex]] and [[AI-demand-durability]]. If AI-server unit growth disappoints, 2028 looks like 2019.
4. **The Chinese/Taiwanese catch-up is closer than for HBM.** A plausible second-tier path to genuinely AI-grade parts is ~2–3 years, and domestic Chinese AI servers are a parallel demand pool needing no Western qualification.
5. **The narrative arrived before the revenue.** AI-server MLCC is ~$1.3B of a ~$15B market — GS's own numbers; even 4.3× by 2030 leaves AI a minority of industry revenue. GS's notes moved the Chinese MLCC sector +9% in a day, and Three-Circle is +155% since April 2026 — cited here only as evidence the story is already being priced, not as analysis.

**The adversarial-verification correction (prominent by design).** The bull narrative's loudest number — the famous "Murata 15–35% MLCC price hike effective April 1" — is **contested**. The officially-confirmed April-1 action covered four *non-MLCC* categories (ferrite beads, inductors, chokes; silver-cost-driven — TrendForce, 2026-03-17). The 15–35% MLCC version exists only as reported private customer notices in Chinese media, with no source document; Murata's own April 30 deck guides capacitor ASP at just **+5–10%, explicitly mix-driven**, and its operating-profit bridge assumes a **¥73B company-wide price decline**. A narrow AI-bin hike could mathematically coexist with the blended guidance, but the claim is ahead of the evidence. Carry as **"reported, unconfirmed"** (bottleneck report, evidence-table claim #1).

## What would confirm or weaken this framing

Pre-registered tests, from the bottleneck report's "what to watch":

1. **Murata Q1 FY2026 results (~Jul 2026)** — does capacitor ASP realization exceed the +5–10% guide (real top-bin repricing), and does server-capacitor growth track the +85–90% guide?
2. **The Izumo ramp (Q4 2026)** — does new capacity land into still-tight demand, or coincide with a channel inventory unwind?
3. **Japan MOF monthly MLCC export prices (HS 8532.24)** — the cleanest neutral series that exists, but it currently lives only as a GS citation relayed through media (the April 2026 +16% price / +28% value / +10% volume triplet is internally consistent yet unverified); needs a manual customs.go.jp / e-Stat pull before any page treats it as government-confirmed.
4. **TrendForce channel data** — does the consumer-grade double-booking unwind spread to high-end grades (2018-redux signal), or stay quarantined?
5. **2027–28 capacity arrivals vs ODM order trends** — SEMCO Philippines #3 (H2 2027) and the Chinese high-end ramps meet the capex deceleration here; this is where structural-vs-cyclical resolves.
6. **Any first disclosure-grade AI-server MLCC revenue split** from Murata / SEMCO / Taiyo Yuden — would upgrade the whole evidence base a tier.
7. **VR200/Kyber reality check** — when Vera Rubin racks ship, does per-rack MLCC content validate the Morgan Stanley $4,320 channel estimate (made on an unshipped product)?

## Open questions (primary-source verification triggers)

1. **Murata (6981.T) = the recommended first primary-source ingest** — Japan/EDINET filer, the same ingest pattern as the vault's [[HARMONIC]]. The full-stack owner with the best primary disclosure and a workable ADR. What it would have to show: the +85–90% server-capacitor guide tracking at results; capacitor ASP realization vs the +5–10% mix-driven guide; any AI/server capacitor disclosure beyond "mainly servers"; the Izumo ramp landing into demand, not inventory.
2. **Taiyo Yuden (6976.T) second** — the purest exposure (~68% capacitors) plus the embedded-MLCC niche; its results would verify the elasticity story (thin margins amplifying the cycle both ways) and whether embedded parts carry distinct pricing.
3. **Samsung Electro-Mechanics (009150.KS) third** — would be the vault's first Korean filer (a new ingest pattern); worth it once the theme needs the challenger leg substantiated: utilization path, the binding AI big-tech contracts, the Philippines #3 timeline.
4. **Does any maker ever disclose an AI-server MLCC revenue split?** Today every AI-segment figure is sell-side estimation; one disclosure-grade split would re-anchor the whole theme.
5. **Does the Japan MOF export-price series confirm at primary?** A sustained +YoY price series from customs.go.jp would be the strongest neutral confirmation; failure to confirm would weaken the GS narrative's data backbone.
6. **Page promotion:** if 2+ maker primary ingests substantiate the chokepoint (e.g., Murata + Taiyo Yuden confirming top-bin pricing power and qualification lock-in), does this theme spawn a canonical chokepoint page per Section 3.15 Pathway 2? Threshold tracking pre-registered here.

## Source audit notes

- **Provenance.** Anchored on the two Tier-3 reports in `raw/research/` (compiled 2026-06-10 by a multi-agent research + adversarial-verification pipeline; seeded from the 2026-06-07 video intel note). All sell-side figures (GS, Morgan Stanley, TrendForce, Korean/Chinese press) are attributions, not facts; the only primary-confirmed anchors are company documents (Murata's April 30 earnings deck, SEMCO's newsroom and call, the product releases, NVIDIA's 800V blog + Navitas 8-K).
- **The verification process was itself the finding.** The bull narrative's two loudest numbers weakened under attack — the "15–35% Murata MLCC hike" turned out to be a likely conflation with a non-MLCC hike, and the "440k per rack" count traces only to anonymous brokerage field work — while the boring primary evidence strengthened: Murata's own +85–90% server-capacitor guide is the best datapoint in the whole thesis. The unit-count reconciliation (per-node vs per-rack vs GPU-boards-only) and the three-way AI-share conflict (40/45 vs 70% vs ">50% advanced") are carried as standing flags on every figure this page uses.

## Change log

- **2026-06-10:** Created as Tier-3-anchored theme page per Section 3.13, anchored on the two `raw/research/` MLCC reports (bottleneck + supplier landscape); multi-agent research + adversarial-verification pipeline; seeded from the 2026-06-07 video intel note.
