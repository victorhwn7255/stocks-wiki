---
type: theme
tickers: [MSFT, GOOGL, AMZN, META]
last_updated: 2026-06-02
---

# Hyperscaler AI-datacenter CAPEX — the payer/spender tracker

## Thesis relevance

The chokepoint thesis is downstream of one number: how much the hyperscalers spend building out AI datacenters. Their capex is the **demand source** at the top of `frameworks.md` Framework 10 (CAPEX flow) — the cash that ultimately funds every supply-side chokepoint the vault tracks (compute, memory, power, cooling, photonics, fiber). If that capex keeps growing, the constraints stay binding; if it plateaus or is cut, capacity catches up and structural positions erode. This page is the **demand-side PAYER/SPENDER tracker** — the four big hyperscalers' capex drawn into one comparison: what each is committing, how firm/comparable the guidance is, and the dynamics that cut across all four.

As of Session 118, **all four big hyperscalers are primary-sourced** — [[MSFT]] (S112) + [[GOOGL]] (S115) + [[AMZN]] (S116) + [[META]] (S117) — so the ~$640-720B 2026 aggregate the thesis rests on is now anchored to the companies' own filings/calls rather than to NVDA's earlier analyst-estimate framing. (ORCL and CoreWeave are the program's remaining two payers — see Open questions.)

**Boundary vs [[AI-demand-durability]].** That page asks *"is AI demand durable?"* — broad, framed from the supply side (15+ companies across the chain reporting demand exceeding supply), with the hyperscaler-capex subsections as one input among many. This page asks the narrower *"what are the payers actually committing, and how firm is it?"* — the consolidated payer-side comparison + the cross-cutting capex dynamics. The per-hyperscaler figures appear on both pages by design; AI-demand-durability keeps them inside its demand-signal narrative, and this tracker is the side-by-side view they point to.

**Honest framing.** These are demand-side pages (`layer: outside`) — the hyperscalers *fund* the chokepoints; they capture no supply-side rent. This page describes the spending, not whether to buy the spenders; reported figures are paired with their caveats (guidance firmness, reported-net-income noise, the capex-ahead-of-revenue timing risk).

## The four-hyperscaler CAPEX comparison

All figures trace to the four company pages' primary sources (FY2025 10-Ks + Q1 2026 10-Qs + Q1 2026 calls; MSFT on its June fiscal year — Q3 FY2026 = calendar Q1 2026).

| Hyperscaler | FY2025 capex | FY2026 capex guidance | Q1 2026 capex | Guidance style | In-house silicon | Backlog / RPO | Reported-NI caveat |
|---|---|---|---|---|---|---|---|
| [[MSFT]] | June FY (no clean CY2025; $80.1B over 9 mo) | **~$190B CY2026** + Q4 >$40B | $30.9B Q3 FY2026 (+~85%) | point estimate | Maia 200 + Cobalt | RPO **$633B** | — (no large non-operating mark) |
| [[GOOGL]] | $91.4B (+74%) | **$180–190B** (raised from $175-185B; +Intersect energy) | $35.7B (+107%) | precise range | TPU 8t/8i + Axion | Cloud backlog **$462.3B** | equity-securities gain $36.9B |
| [[AMZN]] | $131.8B (+59%) | **qualitative only** (no $-guide; TTM $151B; ~$177B run-rate) | $43.2B cash (+~73%) | qualitative-only | Trainium (>$225B commitments) | AWS backlog **$364B** (+>$100B Anthropic) | Anthropic mark-up $15.6B |
| [[META]] | $72.2B (incl. leases) | **$125–145B** (raised from $115-135B; memory-driven) | $19.8B (+~45%) | precise range | MTIA / Broadcom (>1GW) | — (ad-driven; no contract backlog) | tax benefit ~$5B |

- **[[MSFT]]** — the largest single guide (~$190B CY2026), the deepest contracted backlog (RPO $633B), and the cleanest reported net income of the four. CFO Amy Hood addressed the capex-vs-revenue "disconnect" directly (MSFT Q3 FY2026 call).
- **[[GOOGL]]** — $180-190B (raised, partly for the Intersect Power *energy* acquisition), with 2027 capex guided to "significantly increase"; Cloud backlog $462.3B (nearly doubled QoQ). Reported net income inflated by a $36.9B equity-securities gain (GOOGL Q1 2026 10-Q).
- **[[AMZN]]** — the highest Q1 run-rate ($43.2B cash; TTM $151B) but the *only one without a clean annual dollar-guide* (Olsavsky framed 2026 qualitatively); the ~$200B-2026 figure circulating in the aggregate is a Tier-3/analyst number, not Amazon primary. AWS backlog $364B excludes a recent ">$100B" Anthropic deal.
- **[[META]]** — the smallest of the four ($125-145B) but the steepest *raise* rationale: Zuckerberg attributed it to "higher component costs, particularly memory pricing." No contract backlog (ad-driven). Reported net income inflated by a ~$5B discrete tax benefit.

## The aggregate

Summed, the four guide to roughly **$640-720B of 2026 AI-infrastructure capex** (MSFT ~$190B + GOOGL ~$185B + AMZN ~$177-200B + META ~$135B). The milestone of this tracker: that aggregate is now **primary-sourced across all four**, where the vault previously carried only NVDA's analyst-estimate ~$700B (NVDA Q4 FY2026 call). **Honest firmness note:** three of the four are firm (a precise range or a point estimate); Amazon's component is qualitative-only, so the aggregate's softest input is the largest run-rate. The number is a guide, not a contract — the disconfirming-signals discipline below tracks whether it holds.

## Cross-cutting dynamics

What is visible only when the four are read together:

1. **Guidance-style heterogeneity.** GOOGL and META give precise dollar ranges; MSFT gives a point estimate (~$190B CY); AMZN declines an annual figure entirely. The same "AI capex guidance" line means different things across the group — the aggregate is firmest for MSFT/GOOGL/META and softest for AMZN.
2. **Memory-pricing cost-push.** META named memory pricing as the *dominant driver* of its capex raise ("most of that is due to higher component costs, particularly memory pricing," Zuckerberg). Some of the 2026 capex increases are cost inflation, not only incremental capacity — a cross-cutting tie to [[HBM-oligopoly]] (the same memory-pricing signal CSCO flagged as "unprecedented"). It also complicates read-through from capex dollars to physical capacity.
3. **Capex-ahead-of-revenue / ROIC framing.** All four address the timing risk in their own words: MSFT the capex-vs-revenue "disconnect" (Hood), GOOGL a "robust ROIC framework" for allocating constrained compute, AMZN "CapEx growth meaningfully outpaces revenue growth" with a 6–24-month monetization lag (Jassy), META a ~+87% capex step-up against operating income guided only "above 2025." The shared demand-durability risk is timing, not direction — capacity is being funded ahead of the revenue meant to justify it.
4. **In-house silicon as a capex lever.** Each builds captive accelerators to bend the capex/margin curve — AMZN Trainium ("save us tens of billions of dollars of CapEx each year"), GOOGL TPU 8t/8i, META MTIA (Broadcom), MSFT Maia. The capex tracker and [[hyperscaler-custom-ASIC]] are two views of the same spend: how much, and how much of it routes to merchant GPUs vs captive silicon.
5. **Reported-net-income noise.** Three of the four had reported net income inflated by non-operating items this quarter — GOOGL (a $36.9B equity-securities gain), AMZN (a $15.6B Anthropic-stake mark-up), META (a ~$5B discrete tax benefit). Operating income is the clean read across the group; headline net income / EPS will swing with equity marks and tax discretes.
6. **Backlog as forward-demand proxy.** MSFT RPO $633B, GOOGL Cloud backlog $462.3B, AMZN AWS backlog $364B (+>$100B Anthropic) give a contracted forward read; META has no comparable contract backlog (its demand is ad-driven, not committed cloud spend) — a structural difference in how the four's forward demand is visible.
7. **Build vs rent.** AMZN and META both noted *renting* external cloud capacity alongside building their own (META "signing multi-year cloud deals … over 2026 and 2027"). Hyperscaler capex is not the whole picture — some demand routes to neoclouds (CoreWeave, pending), which are payers in their own right.

## Where the capex flows (Framework 10)

The tracker is the top of the CAPEX-flow diagram; the cash routes down into the supply-side chokepoints the rest of the vault analyzes:

- **Compute** — merchant GPUs ([[NVDA]]) + captive accelerators (Trainium / TPU / MTIA / Maia; see [[hyperscaler-custom-ASIC]]).
- **Memory** — HBM into those accelerators ([[HBM-oligopoly]]) — and, per dynamic #2, the cost line currently pushing the capex *up*.
- **Power** — the binding 2026 constraint; transformers + grid ([[transformer-supply]]) + the energy assets the hyperscalers are now buying directly (GOOGL/Intersect).
- **Cooling** — direct-to-chip liquid cooling at rising rack densities ([[liquid-cooling]]).
- **Networking + fiber** — datacenter interconnect and the fiber feeding it ([[GLW]] — Meta's $6B Corning agreement is one hyperscaler-to-supplier example).

## Disconfirming signals

What would weaken the demand-side thesis this page tracks:

1. **A capex guidance cut or plateau** — any of the four lowering or freezing its FY2026/FY2027 capex (vs the current raise/maintain pattern).
2. **Deceleration in the raises** — the QoQ/YoY capex growth rate rolling over.
3. **A guidance-firmness retreat** — e.g., another hyperscaler dropping from a precise range to qualitative language (the AMZN pattern spreading).
4. **Return failing to converge** — operating income / FCF not catching up to the capex step-up over the build-out window (the timing risk in dynamic #3 widening rather than closing).

**Current status (Q1 2026):** none observed. All four either *raised* (GOOGL, META) or *maintained/grew* (MSFT ~$190B, AMZN run-rate) their 2026 capex; GOOGL guided 2027 "significantly higher." The unanimity is consistent with genuinely strong demand, and is also the expected output from four companies with aligned incentives to project AI-spending durability — recorded with that calibration.

## Open questions

1. **The remaining two payers.** ORCL (a backlog/RPO-driven model; May fiscal year, so Section 2.11 applies) and CoreWeave (a neocloud — the rent-side recipient of hyperscaler/lab demand) are the program's last two ingests; both will extend this comparison.
2. **Does the aggregate keep growing into 2027?** GOOGL has already guided 2027 capex "significantly higher" — whether the others follow is the forward test.
3. **How durable is the memory-pricing cost-push?** If memory pricing normalizes, do the capex raises partially reverse, or does volume sustain them?
4. **Capex-vs-return convergence.** Does operating income / FCF catch up to the capex across the build window, closing the timing gap the four all acknowledge?
5. **Captive-silicon share.** As Trainium / TPU / MTIA / Maia scale, how much of the capex routes away from merchant GPUs — the dynamic tracked on [[hyperscaler-custom-ASIC]]?

## Source audit notes

- **Synthesis methodology.** This is a creation, not an ingest — a Pathway-2-equivalent dynamics theme (Section 3.15, as applied to themes at the [[AI-agentic-CPU-orchestration-reemergence]] S80 precedent): four primary-source vault canonical pages + the `_thesis.md` capex aggregate (Tier-3 anchor) + a cross-canonical analytical product (the four-payer comparison). No new primary source was ingested; every figure traces to the four company pages' already-verified primary sources. Section 4.6 ROI streak N/A (no kickoff); A6 unchanged.
- **Guidance-style heterogeneity as a disclosure observation.** The four disclose capex on materially different bases (precise range / point / qualitative). Documented so the aggregate is read with its firmness caveat rather than as four equivalent figures.
- **frameworks.md demand-side placement gap.** This is the vault's first dedicated demand-side / hyperscaler-payer theme; with six demand-side company pages ([[MSFT]] + [[NOW]] + [[PLTR]] + [[GOOGL]] + [[AMZN]] + [[META]]) now carrying `layer: outside`, whether to add an explicit demand-side / CAPEX-deployer category to `frameworks.md` is re-flagged for a codification session (not edited here, per Section 1.1).

## Cross-references

- [[AI-demand-durability]] — the broad demand-durability thesis (supply-side convergence + demand signals); this tracker is the consolidated payer-side comparison its hyperscaler subsections point to (boundary stated above).
- [[hyperscaler-custom-ASIC]] — the captive-silicon lever; how much of this capex routes to in-house accelerators vs merchant GPUs.
- [[HBM-oligopoly]] — the memory-pricing cost-push currently lifting the capex guides.
- [[software-AI-moat-durability]] — the monetization/return side (whether the deployed capex is monetized at the application layer); the demand-validation counterpart.
- Company pages: [[MSFT]], [[GOOGL]], [[AMZN]], [[META]] (the four payers). Funded chokepoints: [[transformer-supply]], [[liquid-cooling]], [[HBM-oligopoly]].

## Change log

- **2026-06-02 (S118 — creation):** Created the hyperscaler PAYER/SPENDER capex tracker — a dynamics theme synthesizing the four primary-sourced hyperscaler pages ([[MSFT]] + [[GOOGL]] + [[AMZN]] + [[META]]) into a side-by-side capex comparison + the ~$640-720B aggregate (now all four primary-sourced) + seven cross-cutting dynamics (guidance-style heterogeneity; memory-pricing cost-push; capex-ahead-of-revenue/ROIC; captive-silicon-as-lever; reported-NI noise; backlog-as-proxy; build-vs-rent) + a Framework-10 "where the capex flows" map to the supply-side chokepoints. Pathway-2-equivalent creation (4 canonicals + Tier-3 `_thesis.md` anchor; no new primary ingest). Boundary vs [[AI-demand-durability]] stated (consolidated payer comparison vs broad demand thesis). frameworks demand-side placement gap re-flagged (not edited). ORCL + CoreWeave pre-registered as the remaining two payers (Open questions). Inbound links from [[AI-demand-durability]] + the four company pages' CAPEX sections. tickers [MSFT, GOOGL, AMZN, META]; themes 12 → 13.
