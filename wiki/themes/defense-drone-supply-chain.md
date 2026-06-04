---
type: theme
tickers: [MP, LSCC, AVAV, KTOS]
last_updated: 2026-06-04
---

# Defense & drone supply chain — the owner↔consumer map

*Tier-3-anchored map theme (per CLAUDE.md Section 3.13). Anchored on the Vic-curated Tier-3 report `raw/research/US-defense-and-drones-report.md` + the human-owned anchors `_thesis-defense-drones.md` / `frameworks-defense-drones.md` (Framework D1), enriched by the four vault primary-source company pages ([[MP]], [[LSCC]], [[AVAV]], [[KTOS]]). The structural framing (the value-chain spine) is Vic-authored scaffolding paraphrased in wiki voice; company placements are cross-referenced to the primary-source evidence on each company page.*

## The map — value capture is inverted relative to visibility

The defense unmanned-systems supply chain runs, top (upstream) to bottom (downstream), roughly as: **upstream chokepoint inputs → components → platforms → autonomy/AI software → counter-UAS → program integration / demand** (Framework D1, per the Tier-3 anchor). The structural read that organizes this whole theme — and the reason the vault tracks the supply chain at all — is that **value capture is inverted relative to visibility**: the platform (the drone you can photograph) is the *most visible and least defensible* layer, deliberately commoditized toward a price floor; the upstream inputs (magnets, secure chips, seekers, batteries, autonomy) are the *least visible and most defensible*. This is the defense analogue of the AI-datacenter thesis's "money is not the bottleneck" insight — *airframes are not the bottleneck; the magnet, the secure chip, the seeker, and the autonomy stack are.*

| Layer | Examples | Structural attractiveness (per the thesis) |
|---|---|---|
| **Upstream chokepoint inputs** | NdFeB magnets, secure/trusted FPGAs, EO/IR seekers, high-energy batteries, edge-AI compute | **High–very high** — scarce, concentrated, capacity-constrained |
| **Components** | motors, ESCs, datalinks, gimbals, propulsion (NDAA "Blue UAS" sourcing — a *policy* chokepoint whose DoD exemption expires Jan 1 2027) | Mixed |
| **Platforms** | small/tactical/OWA (commoditizing toward ~$2,000); large/CCA/jet (higher barriers) | **Low–moderate** (small) / **moderate–high** (large) |
| **Autonomy & AI software** | swarming, GPS-denied nav, data fusion | **Very high** — but the best capability is private/un-investable (Anduril, Shield AI) |
| **Counter-UAS** | detection, EW/jamming, kinetic interceptors | **High** — persistent, under-served, fragmented |

## Where the four vault pages sit — and the now-demonstrable owner↔consumer links

With four Defense & Drones pages in the vault, **both ends of the chain are represented at once** — and the thesis's central claim stops being an assertion and becomes a set of documented, filing-disclosed links.

**Upstream — the chokepoint owners (the "where value sits" end):**
- **[[MP]]** — rare-earth NdFeB magnet chokepoint **owner** (`defense_tier 4`). The only scaled US producer; the DoW public-private partnership (July 2025) backstops its build-out. The #1 geology/physics chokepoint on the Framework D5 quality gradient. See [[rare-earth-magnet-chokepoint]] for the dedicated treatment.
- **[[LSCC]]** — secure / NDAA-compliant FPGA chokepoint **capability** (`defense_tier 4`). Hardware root-of-trust + post-quantum secure-control FPGAs. Honest caveat (per its page): the *capability* is real but defense revenue is unquantified, and the deeper chokepoint is **TSMC fabrication** — LSCC is fabless and 64% China-revenue, the cross-thesis seam (below).

**Downstream — the platform primes (the visible, commoditizing end):**
- **[[AVAV]]** — platform **consumer** (`defense_tier 1`). Its own FY2025 10-K flags that its motors and batteries rely on China-sourced rare-earth metals, and that China placed it on an export-control list (March 2025) — the **first documented intra-defense supply-chain link in the vault: AVAV → [[MP]]** (magnets). Its page also names the secure-microelectronics dependence — **AVAV → [[LSCC]]** (the second link). AVAV owns *none* of these chokepoints; its moat is scale, breadth, and incumbency.
- **[[KTOS]]** — platform prime + chokepoint **builder** (`defense_tier 1`). The exception that proves the rule: rather than consume the propulsion/energetics chokepoints, KTOS **vertically integrates** them (it builds its own jet engines and, via the Prometheus JV, its own solid rocket motors). And — notably — neither of its filings discloses rare-earth/magnet dependence at all (its "China" references are to China as a *peer adversary driving demand*, not a supply vulnerability). So KTOS sits on the map as a prime that is trying to *move upstream* rather than depend on the upstream.

**The structural payoff:** the two primes are the visible names, but the filing-disclosed dependence runs *up* the chain — AVAV explicitly consumes MP's magnets and LSCC's secure chips, while KTOS's response to the same pressure is to build the upstream itself. The value, per the thesis, concentrates with the owners (MP, LSCC) and the builder's in-house chokepoints (KTOS propulsion/SRM), not with the airframes. The platform layer's weakness is the subject of the companion theme [[drone-platform-commoditization]].

## Forward nodes — not yet vault pages (future-ingest candidates)

The map has upstream nodes the vault has not yet substantiated with primary sources (plain-text until they cross the page threshold):
- **EO/IR sensors & seekers** → Teledyne (TDY, via FLIR) — the dominant Western EO/IR position; the report's next-priority chokepoint after the four ingested names.
- **High-energy-density batteries** → Amprius (AMPX) — silicon-anode endurance cells.
- **Trusted microelectronics** → Mercury Systems (MRCY) — a cross-thesis node alongside [[LSCC]].
- **Rare-earth feedstock / refining** → USA Rare Earth, Energy Fuels, American Resources — upstream of [[MP]]'s finished magnets.
- **Autonomy / AI software** → Anduril (Lattice), Shield AI (Hivemind) — *private and un-investable*, which is itself a central structural finding: the best pure drone-autonomy capability is not publicly accessible.

## Cross-thesis seam — the secure-microelectronics node bottlenecks on TSMC

The secure-microelectronics node is the cleanest **cross-domain** link between this thesis and the AI-datacenter vault. [[LSCC]]'s secure FPGAs are NDAA-relevant *and* an AI-server companion chip — but LSCC is fabless on TSMC/Samsung/UMC, so the deeper chokepoint is **TSMC fabrication in Taiwan**, the same bottleneck the AI thesis lives on (see [[TSM]]). NDAA "trusted supply chain" rules govern the *design/assembly* layer but do not solve the *fab* layer — a tension LSCC embodies (64% China revenue, Taiwan fab). Rare-earth magnets are the *other* multi-thesis chokepoint (see [[rare-earth-magnet-chokepoint]] + [[liquid-cooling]]).

## Open questions (primary-source verification triggers)

1. **Sensor / battery / microelectronics nodes.** Do future ingests of TDY (EO/IR), AMPX (batteries), or MRCY (trusted microelectronics) confirm those upstream nodes with primary-source evidence, and do any of the platform primes disclose consuming them?
2. **Does KTOS's vertical integration escape the chokepoints, or relocate them?** Building its own engines and SRMs moves the propulsion/energetics chokepoint *into KTOS's own P&L* — does that defend margin (a genuine chokepoint position) or just absorb the capital intensity (see [[drone-platform-commoditization]])?
3. **MP capacity allocation.** How much of MP's Independence + 10X finished-magnet capacity is allocated to defense offtake vs merchant customers — i.e., how much of the magnet chokepoint actually serves the drone supply chain (drones are <3% of global NdFeB demand)?
4. **The autonomy node stays private.** If the best autonomy keeps flowing to Anduril / Shield AI, does the public-equity map ever capture the most valuable software layer?

## Source audit notes

Tier-3-anchored synthesis; no new primary source ingested at creation. The value-chain spine + the layer-attractiveness ordering are Vic-authored scaffolding (the Tier-3 report + `frameworks-defense-drones.md` Framework D1), attributed and paraphrased. The owner↔consumer links are cross-referenced to primary-source evidence on the company pages: AVAV→MP and AVAV→LSCC from AVAV's FY2025 10-K (China rare-earth + secure-component risk); KTOS's non-disclosure of magnet dependence + its propulsion/SRM vertical integration from KTOS's FY2025 10-K + Q1 FY2026 call. Budget/program/concentration figures are Tier-3 (IEA Nov 2025 via the report; FY2027/DAWG figures are *requests*, not enacted) — to verify against primaries at future ingest. Refinement expected as TDY / AMPX / MRCY cross the page threshold.

## Change log

- **2026-06-04 (Session 128 — creation; the Defense & Drones domain's FIRST theme page):** Created from the four ingested company pages ([[MP]], [[LSCC]], [[AVAV]], [[KTOS]]) + the Tier-3 anchor report. Maps the owner↔consumer spine (MP/LSCC own upstream chokepoints; AVAV consumes them per its own 10-K; KTOS builds its own). Companion to the chokepoint page [[rare-earth-magnet-chokepoint]] and the dynamics theme [[drone-platform-commoditization]]. Tier-3-anchored (Section 3.13/A2); no new primary source; not a refresh.
