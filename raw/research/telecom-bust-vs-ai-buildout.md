# Does the Telecom Bust Rhyme with the AI Buildout? A Mechanism-Level Map

## Executive Summary

The 1996–2003 telecom/fiber cycle is the single most useful historical analog for today's AI infrastructure buildout — but it is useful precisely because parts of it transfer and parts of it break, and the breaks cut in *both* directions. This report extracts five structural mechanisms from the telecom bust and three other capital cycles (railways, the dot-com application layer, 1920s radio), tests each against the specific structure of the AI buildout, and produces a real-time watchlist.

**The headline judgments:**

- **What rhymes (transfers):** (1) *Vendor/circular financing* — Nvidia's equity stakes in OpenAI/CoreWeave and its capacity backstops are structurally close to Lucent/Nortel/Cisco lending customers money to buy their gear. (2) *Narrative-driven demand forecasting* — "AI compute demand could reach 200 GW by 2030" and "$2T of revenue needed by 2030" play the role that "internet traffic doubles every 100 days" played: a real trend extrapolated past the point of evidence. (3) *Aggressive accounting risk* — extended GPU depreciation schedules and off-balance-sheet SPVs echo WorldCom's line-cost capitalization and Enron/Global Crossing's capacity-swap round-tripping in *form*, though not (yet) in proven fraud.

- **What breaks (in AI's favor):** *Funding source.* Telecom was built by cash-flow-negative, junk-bond-financed CLECs and over-levered carriers. The core AI buildout is funded largely by the most cash-generative companies in history from operating cash flow. A 2001-style insolvency cascade is therefore *less likely at the center*. The fragility concentrates at the levered margin — Oracle, the neoclouds (CoreWeave, Nebius, Lambda, Crusoe), and the SPV/private-credit structures.

- **What breaks (against AI):** *Asset recoverability.* Stranded fiber was a multi-decade asset; once bandwidth demand caught up, dark fiber became the backbone of broadband, YouTube, and AWS. A stranded GPU depreciates on a 2–6 year obsolescence curve. If an AI overbuild strands capacity, the assets may be far *less* recoverable than fiber was — the "dark fiber became valuable later" consolation may not apply. *Constraint location* also breaks: telecom's binding constraint was capital and right-of-way; AI's is power/grid and advanced packaging (CoWoS/HBM), a physical ceiling that both *limits* runaway overbuild and *concentrates* it where power is available.

**The single most important thing to monitor:** the gap between debt-funded capex and operating-cash-flow-funded capex, and where in the capital structure (hyperscaler vs. neocloud vs. SPV) the marginal debt-funded GPU sits. That is where a demand air-pocket would convert into an insolvency cascade, exactly as it did in 2001.

This report avoids a "bubble: yes/no" verdict. The useful output is the mechanism map and the watchlist, not a binary call.

---

## PART A — What Actually Happened in the Telecom/Fiber Buildout

### A.1 The setup: deregulation + the internet + cheap capital

The Telecommunications Act of 1996 dismantled the local/long-distance monopoly structure and opened the field to new entrants (competitive local exchange carriers, or CLECs, and long-haul builders). It coincided with the commercialization of the web browser and the privatization of the internet backbone (NSFNET was decommissioned in 1995). The result was a wall of capital deployed into network construction.

The most-cited figure: in the five years after the 1996 Act, telecom companies invested **more than $500 billion** — mostly debt-financed — into fiber, switches, and wireless networks [established; widely cited, e.g., Wikipedia "Telecoms crash," Forbes]. USTelecom's retrospective puts 1996–2001 network capex at an average of **$85.6 billion/year** [established; USTelecom 2024 Broadband Capex Report]. M&A piled on top: roughly **$800 billion** of telecom M&A occurred in 1999 alone [interpretation; Fabricated Knowledge, citing contemporary deal flow]. Note a source tension here: the "$500 billion of capex" and "$2.2 trillion cumulative since 1996" (USTelecom) figures measure different things over different windows — the former is the bubble-era buildout, the latter is 28 years of all broadband investment.

### A.2 The demand narrative: "internet traffic doubles every 100 days"

This is the load-bearing myth of the cycle, and its provenance matters because it is the cleanest historical template for an AI demand narrative.

- The claim traces to **Mike O'Dell, chief scientist at WorldCom's UUNET** division, around 1996–97. UUNET ran one of the largest internet backbones in the world, so its pronouncements were taken as proxies for the whole internet [established; Odlyzko, "Internet traffic growth: Sources and implications"].
- The "doubling every 100 days" rate (≈1,000%/year) was *briefly true* for UUNET during 1995–96, when the base was tiny. It was then extrapolated indefinitely [established; Odlyzko].
- It was laundered into authority by the **U.S. Department of Commerce's 1998 report "The Emerging Digital Economy,"** which repeated the doubling claim, citing a November 1997 Inktomi white paper that in turn cited O'Dell [established; Odlyzko]. The *New York Times* repeated it as fact in August 2000.
- One former UUNET employee (Stluka) later said he built the figure as a *best-case* Excel scenario — "we can set those variables to whatever we think is appropriate" — and it escaped into the world as law [established; CNBC/David Faber documentary, NBC News].
- **Actual** backbone traffic was growing closer to **~100% per year (doubling annually), not every 100 days** [established; Odlyzko/Coffman, "The Size and Growth Rate of the Internet"]. AT&T's Mike Armstrong later said the industry was "backfilling that expectation with laying cables... 2,200 miles of cable an hour... Think of all the companies that went out of business that assumed that that was real" [established; NBC News].

The structural lesson: demand was *genuinely* growing fast; the error was in the *magnitude and timing*, amplified by a self-interested party whose network carried the traffic.

### A.3 The builders and their fates

| Company | Role | Fate |
|---|---|---|
| **WorldCom/MCI** | #2 long-distance, owned UUNET backbone | Bankruptcy July 21, 2002 — **$107B in assets**, largest US bankruptcy at the time; ~$11B accounting fraud |
| **Global Crossing** | Undersea/global fiber | Bankruptcy Jan 28, 2002 — **$12.4B debt**; then 4th-largest US bankruptcy |
| **Qwest** | Baby Bell + fiber builder | Avoided bankruptcy via US West cash flow; **>$17B debt**; SEC fraud charges, $250M settlement (2005) |
| **360networks** | Long-haul fiber | Bankruptcy 2001 |
| **Williams Communications** | Pipeline-spinoff fiber | Bankruptcy April 2002 |
| **Level 3** | Long-haul fiber (IP-optimized) | Survived; became the consolidator (see A.7) |
| **Genuity** | Tier-1 ISP (ex-BBN/GTE) | Bankruptcy 2002; assets sold to Level 3 for ~$137M cash (2003) |
| **PSINet** | Early commercial ISP | Bankruptcy 2001 |
| **Enron Broadband** | Bandwidth trading | Collapsed with Enron, late 2001 |
| **Exodus Communications** | Data-center/colocation | Bankruptcy Sept 2001 |
| **Winstar, NorthPoint, Covad, Teligent, Rhythms** | CLECs/fixed-wireless | Bankrupt 2001 |

By mid-2002, at least **23 major telecom firms had filed bankruptcy**; the cumulative total reached **~1,000 by 2003**. Between 2000 and 2003, **47 CLECs** went bankrupt [established; Grokipedia "Telecoms crash," Columbia/Tunguz]. Global telecom equities lost more than **$2 trillion** in market value [established; thebubblebubble.com], and one congressional figure put the broader sector loss at **~$2 trillion in market cap and ~500,000 jobs** [interpretation; House testimony on Global Crossing].

### A.4 The equipment/component layer (the "picks and shovels")

This is the layer most directly analogous to today's Nvidia/semis.

- **Lucent:** Revenue peaked at **$37.92B in 1999**, then crashed ~69% to $11.8B by 2002; never recovered, merged with Alcatel 2006. SEC charged Lucent with improperly recognizing ~$1.148B in revenue [established; Columbia/Tunguz, SEC].
- **Nortel, Cisco, Ciena, JDS Uniphase, Corning** all boomed then collapsed. Cisco hit a **~$450B market cap in March 2000** (briefly world's most valuable company); its stock fell ~89% from peak [established].
- **JDS Uniphase** took a **$50.6B net loss for FY2001** — including a **~$44.8B goodwill write-down** — then the largest in US corporate history, all from overpriced all-stock acquisitions (SDL bought for ~$41–45B, E-Tek ~$15B) [established; NYT, Washington Post, Wikipedia].
- **Corning** (then ~32% of the global fiber market) saw its stock collapse from roughly **$100 in 2000 to ~$1 in 2002**; wrote off ~$5B of goodwill, took a $5.5B loss, and came within a notch of junk [established; Forbes "Corning, Shattered"]. Three-quarters of its fiber sales came from a handful of customers, several of which (360networks, Williams) went bust.
- **Ciena**'s revenue fell from $1.6B to ~$300M; stock fell ~98% from peak [established; Forbes].

### A.5 Vendor financing — the kill-mechanism amplifier

The equipment makers lent their customers the money to buy their equipment. This booked as revenue on the income statement while the dicey loan sat on the balance sheet as an asset.

- **Lucent** committed ~**$8.1B** in vendor financing (≈$7B in commitments, ~$1.6B drawn at one snapshot) [established; Columbia/Tunguz, Fortune, TheStreet].
- **Nortel** extended ~**$3.1B** (~$1.4B outstanding); **Cisco** promised ~**$2.4B** in customer loans [established; TheStreet].
- In the giant **PathNet** deal Lucent agreed to fund **more than 100%** of the customer's equipment purchase — gear at no money down *plus* extra cash [established; Fortune].
- When the customers (Winstar, etc.) defaulted, **33%–80% of vendor loan portfolios went uncollected** [established; Tunguz]. Lucent was left holding ~$500M in bad Winstar loans (out of a $2B commitment).

### A.6 Overcapacity, dark fiber, and price deflation

- The marginal cost of laying additional fiber once a trench is dug is very low, so builders laid far more than was lit. By 2001, an estimated **85%–95% of deployed fiber was "dark"** (unlit); fiber utilization reached only ~2.7% by 2002 [established but contested range; Grokipedia "Dark fibre" citing multiple sources, technostatecraft.com]. Some analysts estimated only ~**one-tenth of installed fiber was lit** by 2004.
- Compounding the glut: **DWDM** (dense wavelength-division multiplexing) kept multiplying the capacity of *existing* fiber — Gerry Butters (Lucent/Bell Labs) observed the data carried per fiber was doubling roughly every nine months — so demand for *new* fiber fell even as traffic grew [established; Wikipedia "Dark fibre"].
- **Wholesale bandwidth prices collapsed** — roughly **55% year-over-year by 2004** on long-haul routes [established; technostatecraft.com citing analyst estimates; Lightwave]. This is the cleanest "overcapacity → price deflation" metric of the cycle and the direct analog to watch for AI (token prices / GPU rental rates).
- Accounting fraud was woven through the overcapacity: Enron and Qwest executed a **>$500M dark-fiber capacity swap** on the last day of Q3 2001 on routes where both already had ample capacity, purely to book revenue [established; House hearing "Capacity Swaps by Global Crossing and Qwest"].

### A.7 The aftermath: value migration

The fiber didn't disappear — it was absorbed, a decade later, by a *different layer*:
- **Level 3** became the consolidator, buying Genuity (2003), Looking Glass, ICG, and others out of bankruptcy for cents on the dollar, assembling one of the world's largest IP backbones.
- **Google** spent years quietly buying dark fiber (from ~2005) and later lit it; by 2016 it was lighting dark fiber nationwide [established; Slashdot, Search Engine Journal].
- Cheap bandwidth enabled **YouTube (2005), AWS (2006), Netflix streaming (2007), and Web 2.0** broadly. The overbuilt capacity became the backbone of the broadband era [established; technostatecraft.com, trmcdonald].

The investors who funded the buildout were largely wiped out; the *users* of the stranded asset, arriving years later, captured the value.

---

## PART B — Base-Rate Panel

The point of this panel is to separate what is *common to all infrastructure cycles* from what was *idiosyncratic to telecom*.

### B.1 Railway Mania (UK, 1840s) and US railroad busts

- The UK 1840s mania peaked in **1846, when Parliament authorized 263 new railway companies** for ~9,500 miles of proposed routes; about **a third of authorized railways were never built** [established; Wikipedia "Railway Mania"]. It was triggered into collapse by Bank of England rate hikes (to 8% in 1847) and a commercial crisis; **200+ railway company failures** [established; Grokipedia, NY Fed Liberty Street Economics].
- Crucially, the mania left a **net tangible legacy**: a national rail network of lasting utility, "though perhaps at an inflated cost" [established; Wikipedia]. Andrew Odlyzko's work emphasizes that the financial debacle was driven by *new line construction* by *established, hitherto-profitable* railways, not just speculative promotions.
- **US railroads** were far more debt-financed and volatile. The **Panic of 1873** (triggered by Northern Pacific's failure to roll over debt) and the **Panic of 1893** — when **roughly a quarter of US railroads went bankrupt and about one-sixth of track entered receivership** — are the canonical "builder insolvency" episodes [established; Grokipedia "Railway Mania"].

### B.2 Dot-com application layer (1998–2001)

The *application* layer that rode on the telecom infrastructure had its own bust, with an instructive split between casualties and survivors:
- **Casualties:** Pets.com (bankrupt 9 months after its Feb 2000 IPO that raised $82.5M; never solved unit economics on shipping dog food); Webvan (raised $375M in its Nov 1999 IPO, burned >$800M building its own infrastructure, bankrupt June 2001); eToys, Boo.com, Kozmo, theGlobe.com.
- **Survivors:** Amazon (fell ~90% from peak but survived; ~10 months of cash at the March 2000 trough; used a *negative cash conversion cycle* — collect from customers before paying suppliers — to fund itself), eBay (profitable marketplace, asset-light).
- **Why survivors survived:** balance-sheet strength, a path to real cash generation, and business models that didn't require continuous external funding into a closed capital window. When VC funding fell ~70% (from >$100B in 1999 to <$30B in 2000), companies that needed cash *just to survive* died, regardless of idea quality [established; HBS Online, begintoinvest, Wikipedia "Dot-com bubble"].

### B.3 1920s radio boom / RCA

The cleanest pre-internet "transformational technology + speculation" analog:
- **RCA** ("the Cisco/Nvidia of its day") rose ~200-fold during the 1920s. Split-adjusted, it **peaked at ~$114.75 in September 1929** and fell to **~$2.50–2.63 by May 1932 — a ~98% decline** [established; Finaeon/Global Financial Data, corroborated by CMT Association and Stanford University Press *Bubbles and Crashes*]. (Non-split-adjusted peak figures of ~$549–568 circulate; the ~97–98% decline holds on either basis.)
- "Radio was the internet and AI of its day. All you had to do was include 'radio' in the name of your company and the price of your stock would shoot up" — e.g., Kolster Radio rose from 10 to 95 (1927–29), then went bankrupt below 1 by 1930 [established; Finaeon].
- US radio stations grew **112x (from 5 to 556) between 1921 and 1923**; equipment sales went from **$60M (1922) to $843M (1929)** — real, explosive demand growth that nonetheless did not protect equity holders from a ~98% drawdown [established; Finaeon]. RCA did not regain its 1929 high until the **1960s** (and then on television, not radio).

### Base-Rate Table

| Cycle | Capital deployed | Demand-forecast error | Who got wiped out | Who captured value (and when) | Tangible legacy? |
|---|---|---|---|---|---|
| UK Railway Mania 1840s | Vast; ~⅓ of authorized lines unbuilt | Over-optimistic traffic/route demand | Equity holders, ~200+ cos | Later rail operators, the economy | Yes — national rail network |
| US railroads (1873/1893) | Heavily debt-financed | Overbuild + leverage | ~25% of railroads (1893) | Consolidators, reorganized lines | Yes — continental network |
| 1920s radio/RCA | Speculative equity, margin | Real demand, insane valuation | RCA equity (−98%), Kolster etc. | TV-era RCA (1960s), broadcasters | Yes — broadcasting |
| Telecom/fiber 1996–2003 | ~$500B+ capex, debt-funded | "Traffic doubles every 100 days" | Carriers, CLECs, equip. makers | Google/AWS/CDNs/Level 3 (2005–2010s) | Yes — broadband backbone |
| Dot-com apps 1998–2001 | VC equity | "Get big fast" / land grab | Pets.com, Webvan, etc. | Amazon, eBay, Google | Mixed — survivors only |

**The recurring pattern (the base rate):** (1) a *genuinely transformational* technology; (2) real but *mis-timed/over-extrapolated* demand; (3) an *overbuild*; (4) *builder/equity insolvency*, almost always amplified by *leverage*; (5) *value migration* to a later-arriving, often different and higher, layer. What is idiosyncratic: the *specific kill mechanism* (junk bonds vs. vendor financing vs. margin debt) and the *recoverability* of the stranded asset.

---

## PART C — The Transferable Mechanisms

1. **DEMAND MIS-FORECAST.** Real secular demand can still produce ruinous overcapacity when near-term magnitude/timing is wrong, amplified by a self-reinforcing narrative carried by a party that benefits from it. *Evidence base:* "traffic doubles every 100 days" (actual ~2x/year); railway traffic projections; radio. The error is rarely "the technology is fake"; it is "the S-curve is slower and lumpier than the straight-line extrapolation."

2. **FINANCING AS THE KILL MECHANISM.** Leverage, high-yield debt, vendor/circular financing, and off-balance-sheet structures convert a demand air-pocket into an insolvency *cascade*. *Evidence base:* telecom's ~$500B mostly-debt buildout, vendor financing (Lucent $8.1B), capacity-swap accounting; US railroads' debt-driven panics. The internet didn't die in 2001 — the *financing structure* did.

3. **VALUE-CAPTURE MIGRATION.** The infrastructure layer commoditizes and often bankrupts; durable value accrues later and to a *different* layer that runs on top of the cheap capacity. *Evidence base:* dark fiber → Google/AWS/Netflix; rail → the wider economy; radio → broadcasters.

4. **OVERCAPACITY → PRICE DEFLATION → LONG ABSORPTION.** Glut shows up first in *price*, and absorption takes years. *Evidence base:* wholesale bandwidth −55% YoY (2004); ~decade to absorb dark fiber. *The price series is the early-warning instrument.*

5. **WHO SURVIVES AND WHY.** Survival correlates with balance-sheet strength, funding *source* (internal cash vs. external dependence), and proximity to real cash-generative demand. *Evidence base:* Amazon/eBay vs. Pets.com/Webvan; Qwest (saved by US West cash flow) vs. Global Crossing (pure speculative build).

---

## PART D — The AI Infrastructure Buildout Today

### D.1 Scale (and the disagreements)

The capex/revenue estimates are large and the sources disagree — surface the disagreement rather than smoothing it:

- **Bain & Company (6th annual Global Technology Report, Sept 23, 2025):** AI needs **~$2 trillion in annual revenue by 2030** to fund the required compute; even with AI-driven cost savings, the industry faces a **~$800B annual revenue shortfall**; ~$500B/yr of data-center capex; incremental compute demand could reach **200 GW by 2030** (half in the US). In David Crawford's (chairman of Bain's Global Technology Practice) words: "By 2030, technology executives will be faced with the challenge of deploying about $500 billion in capital expenditures and finding about $2 trillion in new revenue to profitably meet demand" [established; Bain press release].
- **Morgan Stanley:** ~**$2.9–3 trillion** of global data-center spend through 2028–29 [established; multiple].
- **McKinsey:** ~**$2.7 trillion** on data centers/AI infrastructure in the US by 2030; AI ~71% of North American data-center capacity by 2030 [established; Breckinridge, Empower].
- **Goldman Sachs Global Institute:** baseline ~**$7.6 trillion** cumulative capex 2026–2031 (compute + data centers + power), explicitly flagging *GPU useful life* as the single most impactful assumption [established; Goldman Sachs].
- **Sequoia (David Cahn):** the **"$600B question"** (June 20, 2024), updating his Sept 2023 "$200B question." The framing: take Nvidia's run-rate revenue, ×2 for total cost of ownership (GPUs ≈ half of data-center cost), ×2 again for a 50% end-user margin, to derive the *revenue required* to justify the spend — which dwarfs actual AI revenue [established; Sequoia primary essays].
- Hyperscaler (Amazon, Microsoft, Google, Meta) capex was pledged at **~$320B for 2025**, up ~40% from ~$230B in 2024 [established; Forbes]. By mid-2026, combined "big five" capex was tracking toward **~$690B/year** [interpretation; Penn Capital].

The disagreement is mostly about *replacement cadence* and *useful life* assumptions, not the direction.

### D.2 The builders

- **Hyperscalers** (Microsoft/Azure, Google, Amazon/AWS, Meta): building the bulk, largely from operating cash flow but increasingly with debt and off-balance-sheet structures.
- **Oracle:** the most aggressive *debt* issuer; pivoting hard into AI infrastructure on the back of a reported **~$300B OpenAI cloud deal** and Stargate.
- **Neoclouds** (CoreWeave, Nebius, Lambda, Crusoe): GPU-cloud specialists, debt- and contract-financed, structurally the closest analog to the CLECs.
- **Frontier labs:** OpenAI (Stargate, the $100B Nvidia commitment, ~$300B Oracle deal, ~$250B Azure commitment) and xAI (Nvidia took up to a ~$2B equity stake).

### D.3 Funding structure (who is levered, who is not)

- **Operating cash flow:** still the dominant funding source at the hyperscaler center — but their aggregate **free cash flow is compressing toward zero / negative** as capex exceeds operating cash flow [established; Penn Capital, techtimes citing CreditSights].
- **Debt:** the five largest hyperscalers issued **~$121B of US corporate bonds in 2025** — vs. a 2020–2024 average of ~$28B/yr (>4x) [established; Mellon, M&G, Tunguz]. Meta's October 2025 **$30B** bond sale was the largest corporate bond offering since 2023; Alphabet raised $25B in November; **Microsoft is the only one of the five not recently tapping debt markets** [established; Tunguz]. Morgan Stanley projects AI-related debt issuance >$570B in 2026.
- **Off-balance-sheet SPVs / JVs:** **Meta + Blue Owl Hyperion JV (Oct 2025)** — a **~$27B debt + ~$2.5B equity** structure (≈$29.5B) for the Louisiana megacampus; Meta owns 20%, Blue Owl funds 80%; debt matures 2049, rated A+, priced ~225bps over Treasuries; PIMCO anchor (~$18B) — described as the largest private-credit transaction ever, and explicitly designed to keep the debt off Meta's balance sheet [established; Bisnow, Reuters, DCD, pe-insights]. Morgan Stanley estimates **~$800B of private credit** for AI infrastructure 2025–2028 (~⅓ of total).
- **Circular/vendor financing (the RHYME):** Nvidia agreed to invest **up to $100B in OpenAI** (Sept 23, 2025), with OpenAI deploying ≥10 GW of Nvidia systems; Nvidia holds **~7% of CoreWeave** and agreed to **buy $6.3B** of CoreWeave's unsold cloud capacity; OpenAI's CoreWeave commitments reached **~$22.4B**; Nvidia also took an equity stake (up to ~$2B) in xAI; AMD struck a deal making OpenAI a large potential shareholder [established; Fortune, The Register, Bloomberg, Highline]. Crucially, Nvidia's equity backing also lets these customers **borrow at materially lower rates** — analyst Jay Goldberg likened it to "asking their parents to co-sign a mortgage," compressing neocloud borrowing from ~15% toward the 6–9% a hyperscaler pays [established; Fortune].

### D.4 Demand & monetization (the actuals)

- **OpenAI:** ARR went from ~$2B (2023) → ~$6B (2024) → **>$20B (end 2025)** → **~$25B annualized (early 2026)**; ~$2B/month; enterprise >40% of revenue; >1M business customers. OpenAI announced **900M weekly active users on Feb 27, 2026**, alongside a **$122B raise at an ~$852B valuation**; CFO Sarah Friar confirmed 2025 ARR exceeded $20B [established; OpenAI, Reuters, Sacra]. But the economics remain heavy: ~33% gross margin, inference costs ~$8.4B (2025) rising to ~$14.1B (2026), projected cash burn ~$27B (2026) / ~$63B (2027), not cash-flow-positive until ~2030 [established; Sacra]. Only ~5% of weekly active users pay [established].
- **Anthropic:** ~$9B annualized revenue [established; Reuters].
- **Token prices:** API price per token has fallen sharply (one source cites ~99% since 2023) — the *demand is real and the unit cost is deflating fast*, which is double-edged (drives adoption, compresses provider margins).

### D.5 The binding constraints (different from telecom)

Telecom's binding constraint was *capital and right-of-way* — the cable itself was cheap. AI's binding constraints are *physical*:
- **Power/grid:** the #1 constraint. US interconnection queues exceed ~2,300 GW (more than total installed US capacity); median time from interconnection request to commercial operation now **exceeds 5 years**; queue-to-COD timelines up ~60% since 2017 (>2,100 days for 2025 projects) [established; Lawrence Berkeley National Lab, Enverus]. High-voltage transformer/switchgear lead times run **18–24+ months** [established; Build.inc, EnkiAI].
- **Memory (HBM) and advanced packaging (CoWoS):** **Micron's entire calendar-2026 HBM output is sold out** under agreed price/volume, including HBM4; CEO Sanjay Mehrotra (fiscal Q1 2026 call, Dec 17, 2025): "We have completed agreements on price and volume for our entire calendar 2026 HBM supply"; HBM TAM projected to grow from ~$35B (2025) to ~$100B (2028) [established; Micron IR]. SK Hynix (~62% HBM share) described DRAM/NAND/HBM as "extremely tight" and sold out into 2026 [established; SK Hynix earnings, TechSpot]. **TSMC's CoWoS advanced-packaging capacity is sold out through 2025 into 2026** (C.C. Wei), expanding from ~13k wafers/month (end-2023) toward ~120–130k (end-2026); NVIDIA reportedly holds ~60% of 2026 CoWoS capacity [established for capacity figures via TrendForce/DIGITIMES; exec quotes via secondary compilers — flagged].

These physical ceilings *cap the speed of overbuild* (you cannot lay a GW of power as fast as you can trench fiber) but also *concentrate* it geographically and create their own boom-bust risk in power/equipment supply chains.

### D.6 The asset: GPU depreciation (the central accounting debate)

This is the disanalogy that cuts *against* AI.
- Fiber had a multi-decade useful life. **GPUs are on a 2–6 year obsolescence curve**, and Nvidia's cadence has compressed to roughly annual (Hopper 2022 → Blackwell 2024 → Rubin 2026).
- **Hyperscalers extended useful-life assumptions** from 3–4 years to ~5–6 years, collectively saving an estimated **~$18B/year** in depreciation expense — which *mechanically flatters earnings* [established; Introl, investing.com/Yardeni]. Meta pushed to 5.5 years (some equipment 11–12 yr historically cited); Microsoft/Google/Oracle ~5–6; Amazon ~5 (and in 2025 *shortened* a subset from 6→5, citing AI pace) [established; Yardeni, CNBC, techtimes].
- **Michael Burry** argued the true economic life is ~2–3 years and that the industry is understating depreciation by ~$176B (2026–2028). In his own words on X (Nov 11, 2025): "Understating depreciation by extending useful life of assets artificially boosts earnings — one of the more common frauds of the modern era... By my estimates they will understate depreciation by $176 billion 2026-2028. By 2028, ORCL will overstate earnings 26.9%, META by 20.8%" [established; CNBC]. Microsoft CEO Satya Nadella conceded the worry: "I didn't want to go get stuck with four or five years of depreciation on one generation."
- **Goldman's sensitivity:** shortening GPU useful life from 5 to 3 years swings cumulative 2026–2031 depreciation from ~$3T to ~$4T — a **~$1 trillion** swing from one assumption [established; Goldman, via techtimes].
- **Counter-evidence (the "value cascade"):** CoreWeave reported 2022-vintage H100s re-booking at ~95% of original pricing on contract expiry; used H100s retained ~61–69% of contemporaneous new price in 2024–25; older GPUs cascade from training → inference → batch [established; Introl, Hashrate Index]. But the secondary market is *volatile and repricing downward*: per the Silicon Data H100 Rental Index, rates fell to **$2.36 on June 19, 2025, from a $3.06 peak on Sept 1, 2024 (−23% in under a year)**, and a fuller arc shows H100 rentals dropping from ~$8/hr to ~$2.85–3.50/hr (a ~64% decline from peak); **AWS cut P5 H100 prices ~44% in June 2025**, and **over 300 new GPU-cloud providers entered the H100 market in 2025** [established; Silicon Data, Introl, CloudZero]. This is the **bandwidth-price-collapse analog**, and it is already underway.

---

## Side-by-Side Comparison Table (Telecom vs. AI)

| Dimension | Telecom/fiber (1996–2003) | AI buildout (2023–) | Verdict |
|---|---|---|---|
| **Capital source** | Mostly external: junk bonds, IPO equity, vendor loans | Mostly internal operating cash flow at the center; debt/private credit at the margin | **BREAK (favors AI)** |
| **Leverage** | High; carriers/CLECs deeply levered, cash-flow-negative | Hyperscalers low-levered/net-cash; Oracle & neoclouds levered | **BREAK at center, RHYME at margin** |
| **Demand-forecast basis** | "Traffic doubles every 100 days" (actual ~2x/yr) | "200 GW by 2030," "$2T revenue needed" — real growth, contested magnitude | **RHYME** |
| **Builders** | WorldCom, Global Crossing, Qwest, CLECs; Lucent/Nortel/Cisco/Corning | Hyperscalers, Oracle, neoclouds; Nvidia/TSMC/SK Hynix/Micron | structural twin |
| **Asset life** | Fiber: multi-decade | GPUs: 2–6 yr, obsolescence-driven | **BREAK (against AI)** |
| **Binding constraint** | Capital + right-of-way (cable was cheap) | Power/grid + HBM/CoWoS (physical ceilings) | **BREAK** |
| **Overcapacity metric** | Dark fiber %, wholesale bandwidth price (−55% YoY) | GPU utilization/idle, token & GPU-rental price, power-queue length | analog exists |
| **Value-capture layer** | Migrated to apps/cloud (Google, AWS) a decade later | Likely migrates to app/agent layer; recoverability of hardware uncertain | **RHYME (migration), BREAK (recoverability)** |
| **Accounting risk** | Line-cost capitalization (WorldCom), capacity-swap round-tripping (Enron/Qwest/GX) | Extended GPU depreciation; SPV/round-trip optics; circular revenue | **RHYME (form), unproven (fraud)** |
| **Likely failure mode** | Insolvency cascade via debt + vendor loans | Air-pocket concentrated in levered neoclouds/Oracle/SPVs; equity drawdown at center | partial RHYME |

---

## PART E — Rhyme vs. Break (mechanism by mechanism)

**1. Demand mis-forecast — RHYME (with a caveat).** The structural setup is identical: a genuinely transformational technology, real fast growth, and a round-number extrapolation pushed by interested parties. "200 GW by 2030" and the "$2T revenue needed" framing are this cycle's "doubling every 100 days." The caveat that *favors* AI: monetization is already materially larger and faster than broadband's was at the equivalent stage — OpenAI alone went 0→$20B+ ARR in ~3 years, vs. dedicated internet access that struggled to grow 20–30%/yr. So the demand is *more proven* than 1999's, but the *magnitude/timing* of the required revenue ($2T by 2030) is exactly the kind of straight-line claim that history punishes.

**2. Financing as the kill mechanism — BREAK at the center, RHYME at the margin.** This is the most important distinction in the whole analysis. In 2001, the *builders themselves* were cash-flow-negative and debt-financed; when the capital window slammed shut (Jan→Apr 2001, "billions to zero"), they died. Today the core builders fund capex substantially from the largest operating cash flows in corporate history, entered the cycle net-cash or <1x levered, and could in principle slow capex without insolvency. **That makes a 2001-style cascade at the center unlikely.** But the fragility has *migrated*, not vanished: it concentrates in (a) **Oracle**, whose 5-year CDS rose roughly **310% since the end of June 2025** to a ~16-year high (~128bps in December, the highest since the 2008 crisis), with CDS trading volume climbing to **$9.2B over the 10 weeks ended Dec 5, 2025, from $410M a year earlier** (Barclays strategist Jigar Patel, via Bloomberg/ICE Data) amid a heavily debt-funded, customer-concentrated (OpenAI) buildout; (b) **neoclouds** borrowing at high rates against GPU collateral whose resale value is falling; and (c) **SPV/private-credit** structures (Meta/Blue Owl) where insurers and pensions hold long-duration AI-campus debt and could be forced sellers in a downturn. The kill mechanism is the same (leverage + a funding-window slam); the *location* has moved to the periphery. One important offset Barclays' Andrew Keches flagged (Feb 2, 2026): "Equity financing significantly inhibits the downside for credit" — i.e., the equity cushions beneath this debt are far thicker than the CLECs ever had.

**3. Value-capture migration — RHYME on direction, BREAK on recoverability.** History strongly suggests durable value will accrue to the *application/agent* layer running on top of cheap compute, while the infrastructure layer commoditizes — exactly as value migrated from fiber to Google/AWS. The break: stranded fiber was a 20+ year asset that *waited* for demand to arrive and then became the broadband backbone. A stranded GPU is depreciating on a 2–6 year obsolescence clock. If AI hits an air-pocket, the "it'll be absorbed in a decade like dark fiber" consolation may *not* hold — the asset could be largely worthless before demand catches up. **Argue both ways:** the value-cascade evidence (CoreWeave re-booking H100s at ~95%, inference demand sustaining older GPUs) suggests useful life may be longer than bears claim; but the rapid rental-price deflation and annual Nvidia cadence suggest the *resale* value curve is steep and downward. Net: value migration rhymes; asset recoverability is a genuine disanalogy *against* AI.

**4. Overcapacity → price deflation → absorption — RHYME, and already visible.** The bandwidth-price-collapse analog is the **token price / GPU-rental rate**, and it is *already deflating fast* (H100 rentals −60%+ from peak; token prices down ~99% since 2023). The open question is whether this is healthy (Jevons-style: cheaper compute → more demand, absorbing supply) or the leading edge of a glut. The telecom lesson: price is the early-warning instrument, and a *demand-driven* price decline (volume up) looks very different from a *glut-driven* one (utilization down). **Watch price and utilization together.**

**5. Who survives and why — RHYME.** The survival criteria are unchanged: balance-sheet strength, internal funding, proximity to cash-generative demand. By these criteria the hyperscalers are the Amazon/eBay of this cycle (they will survive a drawdown); the most exposed are the pure-play levered builders dependent on a continuously open capital window and on a single anchor customer — the Global Crossings and CLECs of this cycle.

**6. Narrative & accounting risk — RHYME (form), unproven (fraud).** The accounting *form* rhymes uncomfortably: (a) **extended GPU depreciation** is functionally the inverse of WorldCom capitalizing line costs — both push expense recognition into the future to flatter current earnings, though depreciation extension is a *legal, disclosed estimate*, not fraud; (b) **circular deals** (Nvidia funds OpenAI/CoreWeave which buy Nvidia chips; Nvidia backstops CoreWeave's unsold capacity) carry *round-tripping optics* reminiscent of capacity swaps — the key disclosure question is whether revenue is being recognized on transactions whose economic substance is circular; (c) **SPVs** (Hyperion) move ~$30B of debt off-balance-sheet legally, but reduce transparency exactly as off-balance-sheet vehicles did pre-Enron. *No fraud is established here* — but the structural incentives that produced the telecom/Enron frauds are present, which is why disclosure quality is a top watchlist item.

---

## PART F — Forward-Looking: Signposts & Scenarios

### F.1 Watchlist

| Signal | Source to watch | Warning reading |
|---|---|---|
| **Debt- vs. cash-funded capex mix** | Hyperscaler 10-Qs/10-Ks; bond-issuance trackers (Mellon, CreditSights) | Debt issuance accelerating well past 2025's ~$121B *and* free cash flow turning sustainably negative across multiple hyperscalers |
| **Circular-deal scale & disclosure** | Nvidia/OpenAI/CoreWeave/Oracle filings; Bloomberg circular-deal tracking | Growth in vendor-funded purchase commitments and capacity backstops; revenue recognized on circular transactions without clear end-demand |
| **GPU/fleet utilization & idle capacity** | Neocloud disclosures; CoreWeave guidance; hyperscaler commentary | Falling utilization alongside rising capacity (the dark-fiber tell) |
| **Token price vs. volume** | API price sheets; inference-cost disclosures | Price falling *with* flat/declining token volume (glut), vs. price falling with rising volume (healthy) |
| **GPU rental/resale price** | Silicon Data H100 index; secondary-market trackers | Sustained rental decline below neocloud break-even (~$2.85/hr cited) + collapsing resale multiples |
| **Power-interconnection queue length** | Lawrence Berkeley Lab queue data; ISO reports | Queues lengthening while announced GW keeps rising = paper capacity that can't be energized |
| **Memory/packaging book-to-bill** | Micron/SK Hynix/Samsung earnings; TSMC CoWoS commentary | A swing from "sold out" to cancellations/push-outs = demand rolling over upstream |
| **Oracle / neocloud credit** | Oracle CDS spreads; neocloud bond spreads; rating actions | CDS continuing to widen past its Dec-2025 ~16-yr high; downgrades; refinancing difficulty |
| **SPV/private-credit exposure** | Blue Owl/Apollo/PIMCO disclosures; insurer ABF holdings | Rapid growth in AI-campus private credit + signs of forced selling or markdowns |
| **Depreciation-schedule changes** | 10-K accounting-policy notes | *Shortening* useful lives (Amazon already cut a subset 6→5) = management conceding faster obsolescence |

### F.2 Scenarios

- **Scenario 1 — Orderly absorption ("Jevons wins").** Token-price deflation drives demand that absorbs capacity; hyperscaler cash flows fund the build; power comes online roughly on schedule. *Early evidence:* utilization holds up *as* prices fall; OpenAI/Anthropic revenue keeps compounding toward the $2T-by-2030 trajectory; HBM/CoWoS stays sold out without cancellations. This is the railway/broadband path — painful for some equity holders, durable infrastructure legacy.

- **Scenario 2 — Financing cascade at the margin (the telecom rhyme, localized).** A demand wobble or a single large counterparty stumble (e.g., an OpenAI funding gap) hits the *levered periphery* first: Oracle's debt-funded, customer-concentrated build and the neoclouds borrowing against depreciating GPUs. *Early evidence:* Oracle CDS keeps widening; a neocloud misses guidance/can't refinance; private-credit AI vehicles mark down; GPU resale values gap lower. The center (Microsoft, Google, Meta, Amazon) survives with equity drawdowns but no insolvency — *unlike* 2001, where the center itself failed.

- **Scenario 3 — "Genuinely different."** Monetization (agents, enterprise) scales fast enough that the $2T revenue requirement stops looking absurd; physical constraints (power, HBM, CoWoS) prevent a fiber-style *overbuild* in the first place because you simply cannot build faster than the grid allows. *Early evidence:* AI revenue growth *accelerates* off the >$20B/$9B base; power constraint, not demand, remains the binding limit through 2027.

### F.3 Bottom line

- **Most-applicable lessons:** (a) *financing is the kill mechanism* — watch the levered margin, not the cash-rich center; (b) *vendor/circular financing* is a real rhyme and a real risk to monitor for disclosure quality; (c) *price/utilization is the early-warning instrument*, and it is already deflating.
- **Least-applicable lessons:** the *funding source* at the center (operating cash flow, not junk bonds) makes a 2001-style *systemic* cascade less likely; and the *physical constraint* (power) structurally limits the speed and scale of overbuild relative to trenching fiber.
- **The disanalogy that cuts against AI:** *asset recoverability.* Dark fiber waited a decade and became the internet's backbone. A stranded GPU may not get that luxury. If there is an overbuild, it could be *less* recoverable than telecom's — the optimistic "dark fiber became valuable" narrative is the one part of the analogy investors should *not* lean on.
- **The single most important thing to monitor:** the **debt-vs-cash-funded capex mix and where the marginal debt-funded GPU sits in the capital structure.** That ratio, more than any demand forecast, determines whether a demand air-pocket stays an equity-drawdown story (Scenarios 1/2) or becomes a 2001-style insolvency cascade (the part of the telecom pattern that did the real damage).

---

## Caveats and Source Discipline

- **Established vs. interpretation vs. speculation:** Figures marked [established] are drawn from filings (SEC, Micron/CoreWeave IR), contemporary reporting (NYT, WaPo, Forbes, CNBC, Bloomberg, Reuters), or reputable secondary analysis. [interpretation] marks analytically-derived or single-source figures (e.g., the ~$800B 1999 M&A figure; the ~$690B/yr 2026 hyperscaler capex run-rate). Forward estimates (Bain's $2T/$800B, Goldman's $7.6T, Morgan Stanley's $570B 2026 debt issuance) are **projections**, not facts, and are presented as such.
- **Contested data, flagged in-text:** the share of fiber left "dark" (85–95% vs. "only ~10% lit") varies by source and route; GPU useful life (2–3 yr per Burry vs. 5–6 yr per hyperscaler accounting) is the single most contested variable and is presented two-sided; RCA's 1929 peak price depends on a split-adjusted (~$114.75) vs. nominal (~$549–568) basis, though the ~98% decline holds either way.
- **Secondary-compiler risk:** TSMC/Nvidia CoWoS executive quotes reach this report via secondary compilers rather than primary transcripts and should be treated as lower-confidence than the Micron IR and SEC-sourced figures. Several CoWoS capacity datapoints trace to a small number of sell-side houses reproduced across outlets.
- **No verdict, no advice:** This report deliberately offers no "bubble: yes/no" verdict and no buy/sell/hold guidance or price targets. It maps structure, incentives, mechanisms, and signposts, and presents every structural judgment two-sided. The most important epistemic discipline for the reader: a *demand-driven* price decline and a *glut-driven* one look identical for a quarter or two — the watchlist exists to tell them apart in real time.