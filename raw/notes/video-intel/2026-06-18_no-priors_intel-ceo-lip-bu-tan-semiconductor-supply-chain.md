---
type: video-intel
source_tier: 3
channel: "No Priors (Elad Gil + Sarah Guo)"
guest: "Lip-Bu Tan (Intel CEO; ex-Cadence CEO; Walden International VC)"
upload_date: 2026-06-18
url: https://www.youtube.com/watch?v=asCgCv2XB4s
entities: [INTC, NVDA, TSM, AVGO, AMD, ALAB, AXTI]
new_names: [SNPS, CDNS, ADI]
trackers_touched: [forward-edge-tracker, hyperscaler-capex, what-could-go-wrong, china-exposure]
headline: "Intel CEO confirms the agentic/inference-CPU re-emergence (training CPU:GPU ~1:8 → ~1:4) from the operator's chair, doubles down on a 5-7yr foundry turnaround (NVDA $5B + US-gov + SoftBank balance sheet), and names advanced packaging + new substrate materials (glass/diamond/GaN/SiC/InP) as the next bottleneck"
---

# No Priors — Intel CEO Lip-Bu Tan: re-engineering the semiconductor supply chain

**Channel:** No Priors (Elad Gil + Sarah Guo) · **Guest:** Lip-Bu Tan (Intel CEO; ex-Cadence CEO 13yr + 2yr exec chair; Walden International VC) · **Uploaded:** 2026-06-18 · **Duration:** 45:00 · **Views:** ~36k · **URL:** https://www.youtube.com/watch?v=asCgCv2XB4s

## Source-tier verdict

**Tier 3 channel, but the guest is the Intel CEO talking his own turnaround book — heavy aligned-commercial-incentive lean on every Intel-specific claim.** No Priors is a credible independent tech/VC podcast; the *content* on Intel (6× shareholder return in 14 months, "10× from here," the foundry-by-2030 path) is **CEO promotion** — treat exactly as Tier-2 management commentary at its most self-serving, not ground truth. **But** Tan is also a 30-year semiconductor VC (Walden — 159 IPOs / 126 M&A by his count), so his *industry-structural* and *where-I-invest* observations (bottlenecks, materials, optical, EDA) carry genuine Tier-3 signal, with the lean that he is personally invested in many of the names. Two filters: discount the Intel magnitudes hard; weight the bottleneck/materials map more.

## TL;DR

The Intel CEO confirms, from the operator's seat, several reads the vault already holds: **(1) the agentic/inference-CPU re-emergence is real** — he puts the training CPU:GPU ratio shifting from ~1:8 toward ~1:4 and says "demand is very high for my CPU"; **(2) advanced packaging + substrate materials are the next bottleneck** — Intel's EMIB, plus new bets on **glass, artificial diamond, GaN, SiC, and InP** substrates (India + New Mexico packaging program); **(3) power, memory, and even helium are the binding supply constraints**, not demand; **(4) compute won't all be centralized** — he bets on edge/client for robotics/defense/home-robots. On Intel itself: balance sheet rebuilt via a **US-government stake + Jensen/NVDA's $5B + SoftBank**, foundry doubled-down as a **5-7-year** "trust business" still "very distant from TSMC," process roadmap 18A → 14A → 10A/7A. Mostly **confirms** vault theses (from a high-credibility but conflicted source); a few **new flags** (helium, glass/diamond substrates, Elon's "Terafab," the EDA blind spot).

## Named entities

| Entity | Speaker | Claim in video | Vault relation | Page? |
|---|---|---|---|---|
| Intel | Tan | Turnaround: agentic-CPU demand high; foundry doubled-down (distant from TSMC, ~2030-32 payoff); 18A→14A→10A/7A; balance sheet via US-gov + NVDA $5B + SoftBank; ~6× return in 14mo, targets 10× | confirms (agentic-CPU); adds (foundry/packaging detail) — **heavy CEO lean** | [[INTC]] |
| NVIDIA | Tan | Jensen "put $5B in" Intel ("became $25B+"); invests in "almost every photonic company"; $2B in Synopsys; owns training | confirms (circularity; photonics) | [[NVDA]] |
| TSMC | Tan | "Great partner," "we have a lot of respect"; Intel "very distant from TSMC"; "we both need more capacity" | confirms (foundry moat intact) | [[TSM]] |
| Broadcom | Tan | "$2 trillion market cap company" (market-cap color) | off-thesis (sizing color) | [[AVGO]] |
| AMD (Lisa Su) | Tan | "almost $800 billion" market cap; "my good friend" | off-thesis (sizing color) | [[AMD]] |
| Astera Labs | Tan | He personally invested ("interconnect become the bottleneck"; garbled "cradle semiconductor / australab") | confirms (interconnect chokepoint); adds provenance | [[ALAB]] |
| Celestial AI | Tan | He invested (optical interconnect; "speed in the cluster") | confirms — vault holds it via MRVL's Celestial AI acquisition | via [[MRVL]] |
| InP / GaN / SiC | Tan | "I invest in all three" new substrate materials | confirms (InP chokepoint) | [[InP-supply]] / [[AXTI]]; GaN/SiC → [[power-semis]] |
| Synopsys / Cadence | Tan | EDA; NVDA $2B in Synopsys; Synopsys bought Ansys; AI-EDA "gold mine" | **blind spot** — no EDA coverage | SNPS / CDNS (no page) |
| ADI / Empower | Tan | "ADI bought Empower" — IVR power management (48V→1V), a bottleneck | adds (power/thermal) | ADI (no page) |

**Auto-caption garble line (YouTube auto-captions — many mangled names; all soft):** "Lehutan/Lipu/Leu" = **Lip-Bu Tan**; "cradle semiconductor / australab" = **Astera Labs**; "e-ip / e-mib" = **EMIB** (Intel embedded multi-die bridge); "guardian nitrite" = **gallium nitride (GaN)**; "Indian fastfite / infi" = **indium phosphide (InP)**; "3DGS" = a **3D-glass-substrate** venture; "synopsis sashin … answers … seaman" = **Synopsys (Sassine Ghazi) / Ansys / Siemens**; "kuda" = **CUDA**; "Terab / terra fab" = **Terafab** (Elon's fab); "Jense / Jensen Hong" = **Jensen Huang**; "SoftBank Master" = **SoftBank / Masa Son**; "Periodic" = **Periodic Labs**. All market caps + return multiples are spoken → soft.

## Key claims + numbers

**Agentic / inference CPU re-emergence (the strongest vault hit):**
- > "right now the agentic AI and inference CPU become highly in demand … versus one to eight in the training CPU to GPU now I can see one to four maybe one to [?] … the demand is very high for my CPU." (~00:51) `[opinion/forward]` — AI-model devs tell him CPUs are better for RL and "the speed of orchestrating all the agents."

**Intel turnaround / balance sheet (CEO book — discount hard):**
- US government became "a big shareholder" — he pitched Trump on the TSMC/Taiwan-government precedent ("Japan, Singapore … US government get to provide the support"). Trump initially asked him to resign over a conflict of interest; he kept the job. `[verifiable]`
- > "Jensen Hong, my old-time friend … put five billion … His five billion become 25 billion now or more." + SoftBank/Masa "lend a hand." (~00:43) `[verifiable]` — the NVDA→Intel $5B + US-gov + SoftBank recap.
- ~6× shareholder return in 14 months; targets **10× over 5-10 years** ("the base is bigger" than Cadence's ~76-85×). Market-cap color: NVDA ~$5.3T, AVGO/TSMC ~$2T, AMD ~$800B, INTC "close to $600B." `[opinion/forward]` — *price/valuation; recorded as his claim, not a vault input.*

**Foundry (doubled-down, multi-year, humble vs TSMC):**
- Decided to double down despite "a lot of voices … very expensive, not going to work" — "critical for the United States and the industry … robust and resilient supply chain … cannot depend on one or two players in one geography." `[opinion]`
- > "we are very distant from TSMC … by 2030 2031 2032 I think it starting to surface up." It's "a trust business — people want to trust you before they give you the wafer." Wants **full-stack** ("some customers ask: give me the whole rack"). `[forward]`
- Process roadmap: "right now we have 18A and going to the production of 14A [~1.4nm], I can see 10 and 7" (1nm, 0.7nm) — "more and more expensive … need partners (substrate vendors, equipment vendors)." `[forward]`

**Advanced packaging + new substrate materials = the next bottleneck (high vault value):**
- > "the other part also really become the bottleneck is packaging the advanced packaging … we all know about CoWoS by TSMC, now we have a really good one called EMIB … starting to run out of steam … so I look at some new material … gallium nitride, silicon carbide and indium phosphide. So I invest in all three." (~18:00) `[opinion/forward]`
- Packaging substrates: investing in **glass** ("a very good heat insulator"; venture "3DGS") and **artificial diamond** (Diamond Foundry; "another very good insulator"); "Intel has ~1,000 patterns on the module." Announced a **big advanced-packaging program with the Indian government** (India + New Mexico, US). `[verifiable/forward]`
- Power/thermal bottleneck: **IVR (integrated voltage regulator)** — "converting from 48 volt down to 1 volt you lose a lot of power"; "ADI bought Empower." `[verifiable]`

**Bottlenecks for AI growth (supply-constrained, not demand):**
- "couple of bottlenecks … one is power constraint … secondly a lot of people didn't realize the **helium** impact can be quite significant for semiconductor … thirdly **memory** is a bigger shortage, everybody scramble … even if you build a fab it takes a couple of years … same for CPU/GPU … pricing also goes up because we pass the cost to the customer." (~11:00) `[opinion/forward]`
- "there's a massive build-up … I don't see anything to slow it down … the question is supply constraint." (~22:00) `[opinion]`

**Where compute lives (edge vs centralized):**
- Bets compute won't all be centralized — edge/client for robotics, defense, "a robot in the home" (he's an investor in robotics/defense cos); application-focused: "not everybody who builds will win … some win big, some go sideways" (Amazon/Netflix analogy). `[opinion/forward]`

**Terafab / Elon (new development):**
- Elon Musk "decided he wants to build his own fab" — **Terafab**; Intel collaborating weekly to "enable him faster to production using some of our technology and process." Elon "questions every step" (the "smoke in the clean room" anecdote). Driven by Tesla/xAI silicon needs (robots, cars). `[forward]`

## Cross-video corpus check

- **Agentic/inference-CPU re-emergence — STRONGEST confirmation yet, from the Intel CEO.** The vault theme [[AI-agentic-CPU-orchestration-reemergence]] (canonicals ARM/AMD/INTC/NVDA-Vera) and the Basis Points note's "CPU-orchestration" thread now get a **primary-CEO datapoint**: training CPU:GPU ~1:8 → ~1:4, "demand very high for my CPU." This is the highest-credibility source the feed has on that specific shift.
- **Upstream-materials bottleneck — agrees with the `2026-06-18 Maverick co-CIOs` note** ("bottleneck migrates upstream to obscure materials"). Tan independently makes the *same* call from the operator's chair — and names the materials (glass, diamond, GaN, SiC, InP) — which is exactly the substrate/packaging layer that note (and [[pcb-interconnect-substrate-chokepoint]] / [[IBIDEN]]) flags.
- **The NVIDIA circularity / photonics web — agrees with the Jensen notes** (Dwarkesh / All-In / CS153) + [[nvidia-supply-chain-commitments]]: Jensen's $5B into Intel, $2B into Synopsys, "invests in almost every photonic company" — more legs of the supplier-funds-its-ecosystem loop, now narrated by a recipient.
- **Memory shortage + power-binding — agrees with the whole feed** (nico-alpha memory/MLCC, the power notes): Tan restates both as top bottlenecks. **NEW wrinkle: helium** as a semiconductor bottleneck — not in any prior note.
- **Foundry-competition — consistent with [[foundry-competition]]:** "very distant from TSMC," multi-year, "we both need more capacity" → the vault's "TSMC moat intact, Intel is a long turnaround" read holds; Tan doesn't claim parity.

## Vault cross-reference (5-type walk)

- **Company:** [[INTC]] (major refresh fuel — foundry/packaging/CPU/balance-sheet), [[NVDA]] (circularity), [[TSM]] (foundry partner-rival), [[ALAB]] (Tan personally invested — interconnect), [[AMD]]/[[AVGO]] (sizing color only), [[AXTI]] (InP). `confirms/adds`.
- **Chokepoint:** [[pcb-interconnect-substrate-chokepoint]] + [[TSMC-CoWoS]] + [[advanced-optical-packaging]] (packaging "the bottleneck"; EMIB; **glass/diamond substrates** — a fresh materials angle), [[InP-supply]] (InP bottleneck), [[cpo-integration]] / [[optical-dsp-phy-supply]] / [[datacenter-laser-supply]] (optical interconnect "very important"). `confirms/adds`.
- **Theme:** [[AI-agentic-CPU-orchestration-reemergence]] (primary-CEO confirm), [[foundry-competition]] (TSMC gap), [[power-semis]] (IVR/GaN/SiC), [[training-to-inference-shift]] + [[physical-AI-value-chain]] (edge compute / agentic+physical AI), [[memory-wall]]/[[memory-shortage-winners-losers]] (memory shortage). `confirms`.
- **Tracker:** forward-edge-tracker, hyperscaler-capex, what-could-go-wrong, china-exposure — block 9.
- **Relationship:** [[nvidia-supply-chain-commitments]] — the NVDA→Intel $5B + NVDA→Synopsys $2B add to the commitment map.

## Tracker signals (discovery-only — never edits)

- **[[forward-edge-tracker]].** Two relevant pairs. (1) **Foundry:** consensus = TSMC dominates and Intel foundry is a value trap; Tan's variant = US-gov + NVDA-backed 5-7yr turnaround with packaging/materials as the wedge. The vault's primary-grounded read sits closer to consensus (TSMC moat intact) — a clean consensus-vs-variant note, *not* a status change. (2) **Agentic-CPU:** reinforces the vault's existing "CPU re-emergence" forward-edge view with a CEO datapoint.
- **[[hyperscaler-capex]].** "Massive build-up … nothing to slow it down … supply-constrained" — a Tier-3 confirm of capex durability from a supplier's seat (no specific $ figure). Light.
- **[[what-could-go-wrong]].** All his bottlenecks are *supply* constraints (power, **helium**, memory, packaging) — consistent with the vault's supply-binding read, **not** a fired tripwire. **Helium** is a new bottleneck *candidate* worth a watch. Light.
- **[[china-exposure]].** The make-in-US / supply-chain-resilience / "can't depend on one geography" framing + the India packaging program = the reshoring/geographic-diversification axis. No direct China P&L; light.

## Framework & chokepoint placement

- **Substrate / advanced-packaging materials (glass, artificial diamond, GaN, SiC, InP)** — sits on the **precision-manufacturing / materials** band of the chokepoint-quality gradient. This *strengthens* the AI-datacenter thesis's packaging-substrate leg ([[pcb-interconnect-substrate-chokepoint]] flagged glass/CCL as the next promotion leg — Tan, an Intel CEO + materials VC, independently names **glass substrates** as a real bet). A `/chokepoint-eval` candidate: **glass-core substrates** as a distinct sub-node.
- **Agentic/inference CPU** — refines [[training-to-inference-shift]] + strengthens [[AI-agentic-CPU-orchestration-reemergence]] (CPU:GPU ratio compressing toward inference/orchestration).

## Ingest leads (the payoff)

1. **[[INTC]] refresh is now well-fueled** (next 10-K/10-Q/call): verify the foundry roadmap (18A→14A in production; 10A/7A planned), the **NVDA $5B + US-government stake + SoftBank** recap (8-K/proxy), the agentic-CPU demand claim against datacenter CPU revenue, the glass/diamond/EMIB packaging program (India + New Mexico), and the ~6×-in-14-months / 10× framing (treat as CEO claim). The two-stop human-gated ingest is where this lands — *not here*.
2. **Glass-core substrate as a chokepoint sub-node** → `/chokepoint-eval` against [[pcb-interconnect-substrate-chokepoint]] (Tan + the IBIDEN substrate work = 2 sources on glass; a 3rd would cross threshold).
3. **Helium as a semiconductor materials bottleneck** → a `/connection-finder` lead (does the vault want a specialty-gases/helium node? `_thesis.md` Materials names Air Products/Linde but not helium specifically). New-name watch, not yet page-worthy.
4. **Astera Labs ([[ALAB]]) provenance** — Tan/Walden as an early backer is color for the next ALAB refresh (interconnect-bottleneck framing), not a primary fact.

## Vault blind spots / coverage gaps

- **EDA (Synopsys / Cadence / Siemens)** — the vault has **zero** EDA coverage despite EDA being a genuine semi-design chokepoint (SNPS/CDNS duopoly gating every advanced chip; NVDA put $2B into Synopsys; Synopsys bought Ansys). Tan (ex-Cadence CEO) calls AI-EDA "a gold mine." A real `/connection-finder` gap.
- **Power-management IC sub-node (IVR / 48V→1V)** — the vault has [[power-semis]] (NVTS/POWI/VICR/ON/MPWR) but the IVR/voltage-regulation angle + the ADI-Empower deal aren't covered; minor.
- **Terafab / xAI-Tesla captive fab** — a new entity (Elon building a fab with Intel's help); worth tracking as it bears on foundry + custom-silicon + "who builds where." No page; watch.

## Contradictions / red flags

- **Heavy promotional lean** (the headline caveat): this is the Intel CEO selling the turnaround — the 6×/10× returns, market-cap figures, and "by 2030-32 we surface up" are book-talking; recorded as his claims, never cited. No buy/sell here.
- **No conflict with vault primary findings** — he *confirms* the vault's reads (foundry gap, packaging bottleneck, CPU re-emergence, supply-constraint). The one place to stay disciplined: his foundry-payoff timeline (2030-32) is a forward CEO claim against the vault's "TSMC moat intact" — keep the vault's more cautious read until primary evidence moves.

## Self-learning hand-offs

- **[[INTC]] → the human-gated two-stop ingest** (the richest lead — foundry/packaging/CPU/balance-sheet all verifiable at the next filing).
- **Glass-core substrate → `/chokepoint-eval`**; **EDA (SNPS/CDNS) + helium → `/connection-finder`** (coverage gaps).
- **No fired tripwire** → no `/calibration-check`.
- **Tier verdict restated:** Tier 3 podcast, Intel-CEO guest talking his book — do not cite as vault fact; the bottleneck/materials map is the useful part, the Intel magnitudes are promotion. Verify against primary sources before any page edit.

## Transcript (Tier 3 — not a primary source)

*Source: YouTube auto-captions (cleaned). Many names are mangled (see the garble line above); all figures soft.*

Nine of the 10 companies I invest, halfway they change their business plan because the market has changed. So I like to have entrepreneurs as a team, not just one person. [Cold open]

[Intro] Welcome to No Priors. Today Elad and I are here with Lip-Bu Tan — the legendary investor from Walden, then CEO of Cadence, now CEO of Intel. We talk about his plan to transform Intel, having the US government as a major shareholder, how to be an amazing semiconductors investor, and whether or not we can make chips in the United States.

[Why take the job] I'm 66 and people said I should retire rather than take on the hottest job in the industry. A couple of reasons: this is an iconic company, so important for the semiconductor ecosystem and for the United States — so I decided to do one more after Cadence. The most surprising thing: one early morning President Trump asked me to resign over a conflict of interest, no exceptions. I had to convince myself — I don't need this job, I do it purely to save Intel. I got a meeting; he listened to me — born in Malaysia, grew up in Singapore, went to MIT, live in the US — and he gave me the chance.

[What "saving Intel" looks like] I just passed 14 months. Change the culture — more accountability, faster decision-making; I'm used to startup speed, not layers of bureaucracy. From day one all engineering reports to me — I'm an engineer by training. Listen to the customer, delight the customer, simplify the product line, build the roadmap and vision for the next 5-10 years.

[10-year vision] Crawl, then walk, then run. First step: strengthen the balance sheet — it was horrible. The US government became a big shareholder — I explained to President Trump that TSMC started with the Taiwan government as a shareholder; Japan, Singapore — this is infrastructure the US government can support. Jensen Huang, my old-time friend, put five billion in — his five billion became 25 billion now or more. And SoftBank/Masa — I used to be on the SoftBank board — lent a hand. Then focus on products, simplify, drive next-generation leadership products. And it's very lucky — right now agentic AI and inference CPU are highly in demand; versus one-to-eight training CPU-to-GPU, now I can see one-to-four. AI model developers tell me for reinforcement learning, for the speed of orchestrating all the agents, the CPU is actually better. So demand is very high for my CPU.

Then the foundry business — capital-intensive, not easy. You need all the right IP to support the customer (mobile needs low-power IP). It's a service business, a trust business: if the yield isn't good they miss revenue. So focus on yield, defect density, cycle time — meet and serve the customer in high quality. Eventually move into full stack — not just silicon; software; some customers ask "give me the whole rack." I'm quietly building, recruiting the best talent — I do all the recruitment myself, no search firm.

[Cadence] I ran Cadence 13 years plus two more as executive chairman — 15 years; I signed up for three months. So now I'm careful when I say "just three months."

[Terafab / Elon] Elon Musk — one of the best entrepreneurs of the century. He and I share the view that semiconductor infrastructure isn't catching up with AI growth — you need capacity, productivity, efficiency. He's unconventional, questions every step — refreshing. He decided to build his own fab — Terafab — and we're delighted to work with him, enable him faster to production using some of our technology and process. He works with me weekly. He talks about wanting to smoke inside the clean room — I don't go that far, but I like the open mind. He needs a lot of silicon for his robots and cars.

[Global supply chain] AI is changing the whole landscape — bigger and more profound than the internet. Most claimed AI layoffs are overstated — mostly 2020-COVID overhiring; the first cuts are outsourced firms (external customer support, external IT), which hits big-BPO countries (Philippines, India). Bottlenecks for AI: power constraint; helium (a lot of people don't realize helium's impact on semiconductor is significant); memory is a bigger shortage — everybody scrambles, and building a fab takes a couple of years; CPU/GPU highly demanded; pricing goes up because we pass the cost to the customer. The companies most impacted are those not embracing AI.

[Foundry domestic / labor] When I decided whether to double down on foundry or get out — a lot of voices said "very expensive, not going to work." But it's critical for the United States and the industry. We all lived through supply-chain challenges — you must have a robust, resilient supply chain; you cannot depend on one or two players in one geography. The most advanced process — 14A is like 1.4 nanometer, and we're already planning 1nm and 0.7nm — it's getting smaller, like our hair, so thin; every step, one mistake and it goes down the drain. We have a lot of respect for TSMC — great partner — and we both need more capacity to serve customers. So we decided to bite the bullet; longer term it's critical.

[Scaling / packaging limits] Right now we have 18A, going to production of 14A — I can see 10 and 7 — but more and more expensive and difficult; that's why we need partners (substrate vendors, equipment vendors). The other bottleneck is packaging — advanced packaging. We all know CoWoS by TSMC; now we have a really good one called EMIB, next-generation, that I have to get to production yield. It's starting to run out of steam, so I'm looking at new materials — going back to the chemical table: gallium nitride, silicon carbide, and indium phosphide. I invest in all three. For packaging I'm investing into glass — glass is a very good heat insulator — a venture called 3DGS. Intel has ~1,000 patterns on the module. We just announced a big program with the Indian government to manufacture in India plus in New Mexico, US. I'm also looking at artificial diamond — another very good insulator — so I invested into a diamond foundry. New material, new substrate material, new design methodology. One good thing about being an engineer: you hit the wall, then find a way to jump over or work around it.

[Semiconductor investing] 18 years ago when I'd talk semiconductors in a VC partners' meeting, half would make an excuse to leave the room and the other half would ask "do you have any software service?" Now Jensen is a $5.3 trillion market-cap company, Broadcom and TSMC are $2 trillion, Lisa at AMD is almost $800 billion, and I'm close to $600 billion. Semiconductor became hot again. On investing, I always look at where the bottleneck is. I backed Astera Labs because interconnect became the bottleneck; I backed Celestial AI — optical — because speed matters in the cluster, so optical is very important. Look at Jensen — he invests in almost every photonic-related company. New materials: indium phosphide (I invested in InP, "well bought it"); gallium nitride and silicon carbide; power management — ADI bought Empower; IVR is a very good area: converting from 48 volt down to 1 volt you lose a lot of power, so power and thermal become the bottleneck. I always target the first customer — usually a hyperscaler; if they like what you have they'll pay millions over the next few years, even give warrants. Talent: US, Silicon Valley, Austin — and Israel (a lot of talent, very disruptive entrepreneurs, resilient even in wartime). Beyond agentic AI, now physical AI is the next big frontier — you need the full stack.

[EDA / AI in design] At Cadence I found and trained my successor — he's a super-great CEO now, driving agentic AI for efficiency. Synopsys (Sassine) also does it well — investment from NVIDIA $2 billion — and acquired Ansys to move into whole-system design. There's also opportunity for startups to do disruptive things and go public or be acquired by Synopsys/Cadence/Siemens.

[10-year winner / full stack] Nine of ten companies I invest in change their plan halfway because the market changed — so I like a team, an open mind. The winning company 10 years from now: articulate and laser-focused on one niche, finds the right partner, and scales — with a full-stack solution. Big platform like Jensen (CUDA), or a startup like Anthropic/OpenAI that changes the game. Hopefully Intel can play the role — we have the XPU, advanced packaging, and foundry; put that together to build purpose-built silicon for different workloads.

[Teams / AI era] Crawl-walk-run: recruit the best semiconductor talent, then software talent for the full stack. My team's average age is late 40s; I need new talent who understand the workload and frontier open-source models. My son became my teacher on AI/ML. Intel used to be an old legacy spreadsheet company; I'm transforming it to embrace AI across design and the whole organization.

[Industrial policy / capital] Capital-intensive infrastructure needs access to capital. Even venture is capital-intensive now — series A over $1 billion valuation is happening. For capital-intensive AI factories and foundry you need government funding, sovereign funds, or very big funds organized to support infrastructure. As a public company I purposefully focus on long-term-growth-oriented investors who help me grow the business, rather than short-term capital-allocation (buybacks) — though that's a fair question, I have to build the business.

[What investors misunderstand about Intel] Quite a few things. After 14 months I'm still crawling, but people are starting to recognize the potential. We need the best products out — PC/client (still have share, need better performance); I'm quietly building CPU/GPU/software architecture to leapfrog. New energy: agentic AI, physical AI — a huge market. Foundry: we're very distant from TSMC on performance, have to be humble, build the IP/yield/defect-density/cycle-time — a trust business, takes longer, but by 2030/2031/2032 I think we start to surface up. In the past we provided servers/PCs for humans; now millions of agents need to access compute and the software stack. The game is not over. In 14 months we made a six-time return to shareholders — just the beginning. At Cadence I made close to 76× (from interim-CEO $2.42) and ~85× by the time I retired as executive chairman. Intel's base is bigger, so I say let's do 10× over 5-10 years — being a venture capitalist at heart, you look for 10×.

[Where compute lives] There's a massive build-up in AI — the right thing; I don't see anything slowing it down except supply constraint. But I focus on the application — identify the humongous application(s). Not everyone who builds will win; some win big, some go sideways or get acquired — like the internet (Amazon, Netflix won; others disappeared). Some applications are better served by client/edge compute than only by the data center — robots in the home, robotics, defense; the compute on the device is a very important choice. My thesis: find a real problem to solve, find the partner, look at how big and sustainable the application is — if it's really big, double/triple down — including betting on applications not yet broadly deployed.

[Outro] Thank you so much for joining us. Find us at No Priors.
