# 硅谷坐标 x 中际旭创 — 于让尘: AI 光互连的超级周期 (The Super-Cycle of AI Optical Interconnect)

**Source:** Silicon Valley Vector 硅谷坐标 (@SiliconValleyVector) · uploaded 2026-04-24 · 49:48 · 75,856 views / 2,275 likes · https://www.youtube.com/watch?v=13qOMeSTBYo
**Transcript:** mlx-whisper (large-v3-turbo, zh, transcribe mode), translated by the analyst. No captions existed; this is ASR — names/numbers carry extra uncertainty.
**Tier verdict:** **Tier 3 (independent media interview) + Tier-2-flavored insider guest + ALIGNED-INCENTIVE FLAG.** The channel is independent analysis; the guest is an executive of an optical-interconnect maker whose entire thesis ("optical is a trillion-dollar super-cycle that must grow faster than compute") is exactly what an optical-module vendor wants the market to believe. Treat the *framework* as a high-quality industry-insider map; treat every demand/share claim as talking-his-own-book until primary-verified.

> ✅ **Identity RESOLVED (2026-06-09, web-verified — corrects an earlier assumption):** Guest = **于让尘 / Ryan Yu**, **Vice President of TeraHop** (per 硅谷坐标's own East Money repost). Credentials: PhD solid-state physics (Peking Univ / Univ of Pennsylvania), 30+ yrs Silicon Valley optical-comms / optical-interconnect, former chairman of a Chinese optical society — a genuine domain expert. The Whisper ASR "TeraHub" was **nearly correct (TeraHop)**, NOT a garble of "Innolight." The channel title's "x 中际旭创 (Zhongji Innolight, 300308.SZ)" is a collaboration/topic tag, **not the guest's employer.** NOTE: every "Innolight" reference elsewhere in this note reflects the title/topic framing and should be read as "the channel's topic partner," not "the guest's company"; the guest speaks for **TeraHop**. Bio details are Tier-4 (channel promo / financial-portal repost) — reliable-but-unverified at primary. Expert ≠ unbiased: he's a senior optical-interconnect insider pushing open MSAs (12.8T XPO, OpenCPX), so the "optical super-cycle / open-ecosystem-good / NVIDIA-vertical-bad" thesis is partly his book.

## TL;DR

An optical-interconnect industry leader argues the AI bottleneck has shifted from *compute* to *connect*: AI compute grew ~300x in three years but optical-interconnect bandwidth only ~30x, leaving a ~10x gap that has to be filled. He reframes optics not as a cost to minimize but as "part of compute" (brain white-matter vs gray-matter), insists hyperscalers are *pragmatic not religious* — they buy pluggable + NPO + CPO all at once ("adults don't pick just one") while all building their own accelerators AND buying NVIDIA — and names the laser supply chain (still 3-inch wafers vs semiconductor's 12-inch) as the single biggest bottleneck. Reads as a near-complete tour of the vault's photonics chokepoints from the merchant-optics side.

## Named entities

| Entity | Claim in the video | Vault page |
|---|---|---|
| 中际旭创 / Zhongji Innolight (guest's company; **ASR: "TeraHub"**) | World's largest optical-interconnect maker; claims to lead the **12.8T XPO MSA** + **OpenCPX MSA** + multi-core-fiber MSA; "we don't pick — we give customers all solutions" | none (new-name candidate, 300308.SZ) |
| NVIDIA / 英伟达 | NVL72 (72 chips/rack, all-copper) → NVL576; wants CPO; **$4B into Lumentum + Coherent (early March) to lock laser supply** | [[NVDA]] |
| Lumentum | NVIDIA $4B (w/ Coherent) target = locking **laser** supply for CPO | [[LITE]] |
| Coherent | same $4B strategic deal | [[COHR]] |
| Google / 谷歌 | Leans **pluggable** ("CPO is always 2 years away, every year" at OFC); **9,000-TPU + OCS "super-brain"**; 10-yr OCS lead; strategic-invested a coherent-lite startup (**ASR "Celero"** — uncertain) | [[GOOGL]] |
| Meta | Chose **NPO**; "Manhattan-size" datacenter (scale-across) | [[META]] |
| Amazon / AWS | Chose **NPO**; Trainium | [[AMZN]] |
| Microsoft Maia (**ASR "Maya"**) | Own accelerator | [[MSFT]] |
| OpenAI "Titan" (**ASR-uncertain name**) | Building own AI chip | none (private) |
| xAI / Musk (**ASR "SAI"**) | Building own AI chip | none (private) |
| TSMC COUPE (**ASR "COOP"**) | Built a SiPh + electrical-chip integration platform; other FABs will follow | [[TSM]] |
| Arista XPO (form factor) | The 12.8T XPO MSA the guest co-pushes (>100 companies) — reconciles with vault's ">100-vendor XPO endorsement" | [[ANET]] |

## Key claims + numbers (by chapter; tags: [verifiable]/[opinion]/[forward])

- **(~00:00) The interconnect wall.** AI compute grew ~300x (2022→2026); optical-interconnect bandwidth only ~30x → ~10x gap to fill. [opinion — directional, core thesis]
- **(~03:05) Optical = part of compute.** Brain analogy: gray matter (compute) vs white matter (connectivity); optical is now "single-digit % / a few percent" of datacenter capex but must grow faster than compute (the connect:compute investment ratio should exceed 1). [opinion/forward]
- **(~05:48) Scale-up / out / across.** Scale-out = across a building, ~1-2km, a trillion-param training needs a ~10,000-GPU cluster (ASR "one卡" = 万卡). Scale-up = bigger single "brain," **~10x the bandwidth of scale-out**, meters→tens-of-meters: NVIDIA **NVL72 all-copper → 576**; **Google 9,000-TPU via OCS+optical**. Scale-across = DC-to-DC, km→tens-of-km, **Meta "Manhattan-size"**. Scale-up is "low base but a 10x opportunity." [verifiable — NVL72/576, Google 9000-TPU+OCS, Meta multi-GW]
- **(~11:19) Optical-replaces-copper economics.** "Use copper when you can, use optics when you must." Copper physical limit ~1.5-2m (at 400G even ~1m is hard). Don't compare optics-vs-copper cost; compare **cost-per-token**: a GPU is **$30-50k**, an optical link a **few thousand $** — better optics lifts utilization of thousands of GPUs, so willingness-to-pay for optics is structurally higher. [opinion — the value-capture argument; GPU $30-50k verifiable]
- **(~14:09) Pluggable / NPO / CPO = "how close to the main chip."** CPO = deepest integration, lowest power/latency, highest density, but concentrated heat + deep coupling (one failure can take the board) — "recognized as the ultimate form for next-gen ultra-large AI clusters." NPO = middle. [maps to cpo-integration]
- **(~15:25) Hyperscaler route choices — the big one.** "From public info: Google leans pluggable; Meta + Amazon chose NPO; NVIDIA wants CPO. BUT internet companies are pragmatic, not religious — they pick **all three**, even within one company; '成年人不做选择题' (adults don't pick just one)." Every hyperscaler builds its own chip (**Google TPU, Meta MTIA, AWS Trainium, Microsoft Maia, OpenAI 'Titan', xAI**) AND buys NVIDIA vertically-integrated systems — "walking on two legs" → they *want* an open optical ecosystem. [opinion/[verifiable] — directly a CPO-platform-battle + hyperscaler-custom-ASIC data point]
- **(~20:58) Roadmap.** Bandwidth = lanes × speed/lane. Now **200G/lane; 1.6T mass production this year; 400G/lane "definitely in 2-3 years."** Lanes 8 → 64 (8x); NPO/CPO now 32-lane; future 128-lane. Plus a "**slow and wide**" path once copper exits (lower speed, many more lanes, simpler/lower-power interface). [verifiable/forward — maps to optical-dsp-phy-supply]
- **(~26:10) 12.8T leap.** Driven by the 10x gap + same-rack copper hitting its wall. Feasible because silicon-photonics yield/reliability is mature enough to add lanes (8→16→32→64). [forward]
- **(~27:26) NVIDIA's $4B Lumentum+Coherent.** "Real money to lock the supply chain — specifically the **laser** supply for CPO. Jensen said twice at GTC that optical is core." A clear public signal of how worried NVIDIA is that optical supply can't keep pace. [verifiable — the $4B deal; maps to nvidia-supply-chain-commitments]
- **(~30:36) Open MSAs vs proprietary.** Guest's firm co-leads **12.8T XPO MSA + OpenCPX MSA** (4-8x bandwidth, **100 companies**) + a **multi-core-fiber (SDM/MCF) MSA** (1 fiber = 4 channels; fiber density is itself becoming a bottleneck). Framed against "one or two big suppliers using proprietary/vertically-integrated solutions" (read: NVIDIA) that customers dislike — "why CPO has been discussed so long without scale commercialization: customers don't like vertical-integration lock-in + the technical barrier is high." [opinion — self-interested open-ecosystem framing]
- **(~34:55) OCS.** Google deployed optical-circuit-switching at scale (9,000-TPU super-brain); saves power + latency + cost (no OEO), but OCS is slow (reconfiguration), only for stable/predictable workflows, can't fully replace electrical switching. Google ~10 years ahead; others ~0 OCS today = greenfield. Won't fully replace electrical switching in 5 yrs; maybe larger share in 10-20, never 100%. Pairs with **coherent-lite** (link-budget headroom for OCS insertion loss); Google strategic-invested a coherent-lite startup (ASR "Celero"). [verifiable/opinion — maps to datacenter-photonics-supply-chain §2.5]
- **(~43:36) 400G/lane = 3-way race.** Silicon photonics / **thin-film lithium niobate (TFLN, ASR "伯摩尼酸黎")** / EML (III-V) lasers — "don't know which is mainstream; all in PK; OFC showed early validation of all three. We prefer integratable; even doing **TFLN-grafted-onto-silicon-photonics hybrid**." [forward — maps to datacenter-photonics-supply-chain §2.2]
- **(~45:15) Biggest bottleneck = lasers.** Laser making is "still a niche/small-batch ecosystem." Laser wafers are still **3-inch, vendors 'thumping their chest' to reach 6-inch** — vs semiconductor's 12-inch/300mm. New startups doing **quantum-dot lasers** could make lasers *on silicon* and jump straight to 12-inch → would break the bottleneck. Plus light-electrical co-packaging (TSMC COUPE leads; other FABs follow). [verifiable/forward — maps to datacenter-laser-supply, InP-supply]
- **(~48:44) 5-10yr.** Stop treating optical as "savings to redirect to compute"; treat it as part of compute. Optical's capex share grows much faster, toward the brain white/gray-matter ratio. [opinion]

## Vault cross-reference

- **[[cpo-integration]] + [[CPO-platform-battle]] — CONFIRMS + ADDS.** The hyperscaler route map (Google→pluggable, Meta/Amazon→NPO, NVIDIA→CPO) and the "adults don't pick just one / multi-source all three" framing is a fresh, insider restatement of the vault's five-way-executive-comparison and Murphy bifurcation. The "Google: CPO is always 2-years-away, every year" line corroborates the vault's CSCO/Google deferral framing. NPO is under-covered in the vault relative to how prominent it is here.
- **[[nvidia-supply-chain-commitments]] + [[NVDA-platform-integration]] + [[datacenter-laser-supply]] + [[LITE]]/[[COHR]] — CONFIRMS.** Third-party industry-insider read on NVIDIA's $4B Lumentum+Coherent: "locking *laser* supply for CPO." Matches the vault's reciprocal-confirmation finding, and sharpens *why* (laser is the binding input).
- **[[datacenter-laser-supply]] + [[InP-supply]] — STRONGLY CONFIRMS.** The "lasers are the #1 bottleneck; 3-inch vs 6-inch wafers" point is almost verbatim the vault's [[LITE]] (3-inch InP) vs [[COHR]] (6-inch InP) framing — now echoed by a merchant-optics leader. Quantum-dot-laser-on-silicon is a new falsification/watch item for the InP-scarcity thesis.
- **[[datacenter-photonics-supply-chain]] — CONFIRMS across §2.2/§2.3/§2.5.** 200G→400G/lane + 1.6T 2026; EML/SiPh/TFLN three-way race (incl. TFLN-on-SiPh hybrid); OCS (Google Jupiter/Apollo); multi-core fiber as a density bottleneck. Maps to [[ANET]] XPO (the >100-vendor MSA) and [[GLW]] fiber.
- **[[hyperscaler-custom-ASIC]] — CONFIRMS the multi-modal thesis.** "Every hyperscaler builds own silicon AND buys NVIDIA, two legs" — incl. the rare explicit naming of **OpenAI 'Titan'** and **Microsoft Maia** alongside TPU/MTIA/Trainium.
- **[[TSMC-CoWoS]] / [[TSM]] — touches.** TSMC COUPE as the SiPh+electrical integration platform; "other FABs will follow."
- **[[AI-demand-durability]] — adds a framing.** The "compute grew 300x, optical only 30x → 10x gap" is a demand-durability argument *for optical specifically*.

## Ingest leads (the payoff — what to go verify against primary sources)

1. **Innolight (中际旭创, 300308.SZ) as a new-name candidate.** World's largest transceiver maker, repeatedly central to the vault's photonics chokepoints but not a vault page. Verify the exec/company identity (ASR "TeraHub"), then its 12.8T XPO / OpenCPX / MCF MSA leadership claims at primary (Innolight annual report / OFC 2026 MSA membership lists). A-share filer (the SANHUA/TUOPU non-SEC sub-type applies).
2. **NVIDIA $4B Lumentum+Coherent = laser-supply lock for CPO.** Already in the vault (S50/S110 reciprocal-confirmation) — this adds the insider "it's specifically the *laser*" read. Cross-check against [[LITE]]/[[COHR]] 10-Q language on the supply agreement scope.
3. **Hyperscaler route attributions** (Google pluggable / Meta+Amazon NPO / NVIDIA CPO; all multi-source) — verify against GOOGL/META/AMZN/NVDA primary + OFC 2026 disclosures before treating as fact (this is the guest's read of "public info," not a filing).
4. **400G/lane in 2-3 years + 1.6T mass production 2026** — verify against [[LITE]]/[[COHR]]/[[MRVL]]/[[AVGO]] roadmaps; the vault already tracks 1.6T-2026.
5. **Quantum-dot-laser-on-silicon startups** — new watch item; if real and scaling, it's a falsification candidate for the InP-laser-scarcity ([[datacenter-laser-supply]]/[[InP-supply]]) thesis.
6. **OpenAI "Titan" custom AI chip** — new name; verify whether OpenAI has a named custom-silicon program (would extend [[hyperscaler-custom-ASIC]]).

## Contradictions / red flags

- **Aligned incentive throughout.** Guest is a merchant-optics leader; the "optical super-cycle, open ecosystem good / vertical-integration (NVIDIA) bad" thesis is his book. The open-vs-proprietary framing is self-interested — weight accordingly.
- **"XPO" attribution.** XPO is Arista's ([[ANET]]) form factor in the vault; the guest claims his firm co-leads the "12.8T XPO MSA." Reconciles with the vault's ">100-vendor XPO endorsement," but verify Innolight's specific role vs Arista's.
- **ASR name garbling** (TeraHub/Maya/COOP/Celero/伯摩尼酸黎/SAI/one卡) — every proper noun and figure is ASR-derived; treat as leads, not facts.
- **No hard financials** — it's a thesis interview, not a numbers disclosure; the only sized figures (GPU $30-50k, $4B, 300x/30x, 9,000 TPU) are directional/known.

## Source-tier verdict (restated)

**Tier 3 (independent interview) with a Tier-2 insider source + aligned incentive — do not cite as vault fact. Use to generate questions; verify against primary sources (filings / OFC disclosures / company IR) before any page edit.**

---

## Transcript (Tier 3/5 — not a primary source; raw mlx-whisper ASR, original Chinese)

过去三年多 / AI算力增长了大约300倍 / 但光连接的总带宽只增长了大约30倍 / 这意味着今天限制AI集群继续做大的 / 越来越不是单点的算力 / 而是芯片之间的数据搬运效率 / 换句话说 真正卡住AI系统上线的 / 已经不只是算 而是连 / 而要打穿这堵通信墙 最关键的一类技术就是光互联。

今天这期节目我们请到的嘉宾是全球光互联的龙头、硅谷AI云计算顶级巨头的核心供应商，[公司名 ASR="TeraHub" → 中际旭创] 的副总裁于让诚博士。

[算力发展300倍，光互联才发展30倍，有一个10倍的gap要去填补，必须整个业内一起来努力。] 所有的互联网公司他们是很实际的，他们不会做宗教式的选择。可插拔模块、NPO、CPO，它甚至同一个互联网公司它三项都选，叫做"成人不做选择题"。整个产业链的环节哪边的蛋糕在变大、利润是怎么样重新分配的，这个很快变成一个万亿级别的问题。

[脑灰质/脑白质类比] 其实人的大脑它的算力是在脑灰质……它又是高度连接的，这个高度连接是通过脑白质来连接的……现在从人脑的比例来讲基本上是一比一（也有40到60）……我们今天可能还在小鼠小猫那个阶段，灰质比例还是比较大、白质还是相对比较小……希望光互联作为未来发展方向，这个比例会持续增加，而且增长速度会大于算力的增长速度。光互联现在只能占到总体资本开支的single digit，大概几个percent，但增长很快。

[Scale up/out/across] 我们过去几年发展都叫scale out……做一个大training，一个trillion parameter的training可能需要[万卡]……大脑之间互联叫scale out；把大脑本身做得越强越大就是scale up，它的互联是非常大带宽的，远超过scale out，基本上是10倍带宽的比例。像英伟达的NVL72，一个机架之内72个芯片组成的大脑，完全用铜缆连接，铜缆带宽有限、距离有限，已经在制约大脑发展……英伟达发布已经开始进入576颗，其他互联网公司已经在部署1000颗，甚至谷歌的TPU这个大脑已经建到9000个TPU互联起来——机架内还用铜，机架外用OCS加光互联。ScaleAcross就是一个数据中心物理上都不够（地理限制、供电限制），要通过多个数据中心去互联……Meta最近发布的大数据中心可以是Manhattan size。

[光进铜退经济账] "Use copper when you can, use optics when you must." 铜互联还会持续相当长时间，但有物理局限……不能用光互联去跟铜互联比成本，要看单位算力/单位token的输出。一块GPU是3万到5万美金，一块光互联可能是几千美金；如果把光互联做得更好，能撬动成千上万GPU集群的利用率更高，所以光互联客户的willingness to pay其实可以更高。不要想省钱省在互联，你省在互联，牺牲的是你的算力、是给客户产生token的效率。

[可插拔/NPO/CPO] 三类方案本质上都在回答同一个问题：光接口到底应该离主芯片有多近。可插拔=外挂式、离主芯片最远、功耗偏大，但灵活、供应链最开放；CPO=把光和主芯片做成深度集成的整体，电路径最短、带宽密度最高、延迟最小，但散热更集中、系统耦合更深，CPO坏了可能影响整块板卡——CPO目前是公认最适合下一代超大规模AI集群的终极形态；NPO是介于二者之间的中间路线。这不是一个选择题问题而是一个平衡问题：功耗、成本、带宽、密度、可维护性、可靠性所有维度都要平衡。

[硅谷大厂选择] 各大互联网公司都在建自己的芯片：谷歌的TPU、Meta的MTIA、AWS亚马逊的Trainium、Microsoft的Maia、甚至OpenAI在做自己的Titan、还有马斯克的xAI在做AI芯片；他们同时在买英伟达的垂直整合系统——两条腿走路，所以一定欢迎开放的光互联生态。从公开消息：谷歌比较倾向可插拔模块（在OFC公开讲"CPO总是2年后，而且每年都是2年后"）；私下他们会把所有工具箱都看；Meta跟亚马逊选NPO，英伟达想往CPO发展。但所有互联网公司都很现实，不会做宗教式选择，甚至同一个互联网公司三项都选。

[12.8T] 光模块带宽=每通道速率×通道数。现在200G/lane，1.6T今年开始量产；400G/lane是热点，未来两三年一定会上；通道数从传统8 lane跳到64 lane，NPO/CPO现在32 lane，后面可能128 lane。到一定节点铜走不下去了（铜现在走一米半到两米，到400G可能一米都勉强），就会变成全光，这叫光进铜退；那时整个光的形态可能不同，甚至速度往低走、让接口变简单、功耗降下来、通道数急剧增长——业内在探索"slow and wide"。scale out/across还有"coherent-lite"更高调制技术。Terra Hub提出12.8T是因为需求（10x gap、同轴在单机柜内进入瓶颈）+ 硅光可行性（已出1000多个8通道，自然往16/32/64通道走）。

[英伟达40亿] 今年3月初英伟达向Lumentum跟Coherent投资共计40亿美金，签了战略合作协议——是公开证明英伟达对光互联的重视，担心供应链跟不上X增长的步伐，用真金白银锁定供应链，这个case主要在锁定激光器供应。Jensen已经两次在GTC说光互联是整个算力构建非常重要的组成部分，下一步要用Co-Packaged Optics，需要激光器，所以要锁定激光器提供商。中端客户不愿意被一家锁死，已经在"vote with wallet"，花大把钱赢建自己的算力芯片——做自己的芯片已经不是选项而是必须做的事情。

[OFC开放生态] 今年OFC有多项重大的多元协议和标准推出，Terra Hub是主要推动者：发布了12.8T XPO多元协议、OpenCPX MSA，都是光互联带宽4到8倍的增长，已经有100家公司愿意参与（互联网公司、芯片公司、模块公司）。市面上一两家大客户/大供应商用的方案比较proprietary、垂直整合，对中端客户不是喜闻乐见——变成垂直整合打包卖、溢价能力非常强势，对生态不健康；这也是为什么CPO谈了这么久一直没有规模商用。还有OpenCPX、SDM/MCF多芯光纤多元协议（一根光纤跑四个通道，因为光纤密度本身变成瓶颈）。

[OCS] OCS光交换机不需要像电交换那样一站站处理转发数据包，可以让数据以光的形式沿专用路径直接通过；特别适合AI训练这种大吞吐、相对可预测的场景。谷歌已将OCS大规模用到TPU系统，按公开发布可以用9000个TPU加OCS组建super-brain；好处是取代电交换、省功耗、省时延、省成本，但OCS比较慢、是重新规划路径的工具，工作流稳定可预测时好用；现在还不能完全取代电交换。谷歌大概十年前就开始做，布局比所有互联网公司都靠前；其他公司OCS基本是零（greenfield机会）。未来五年不可能完全取代电交换，十年二十年比例会越来越大但不会完全取代——长期共存。OCS会带来损耗（2-3 dB），对链路预算要求更高，coherent-lite（本征放大）跟OCS是比较好的配对。谷歌战投今年投了一个coherent-lite初创公司[ASR="Celero"]。

[400G/lane三路线] 三种主流技术：硅光、薄膜铌酸锂(TFLN)、EML三五族激光器。现在还不知道谁是主流，都在PK阶段；今年OFC很热闹，三条路线都在做早期验证。我们偏好可集成方向，甚至在做混合基层——把薄膜铌酸锂嫁接到硅光作为混合平台。"成年人不做选项"，三条路都在跑。

[价值链重塑&瓶颈] 整个连接（交换机+光互联）市场价值已基本接近一个trillion dollars。大家会朝半导体集成方向做，光和电会越来越集成——半导体化的光互联是必然方向。最大瓶颈：作为产业还在半导体集成的早期阶段。拿激光器来讲，激光器基本还是小众生产的生态，过去两年被逼着快速增长但还没发展到位。Silicon现在是12英寸/300毫米，激光器厂家现在是3英寸、拍着胸脯要做6英寸，远远落后整个半导体生态。最近有新创企业开始做量子点激光器——如果走到量子点激光器，后面可以在硅片上做激光器，直接从三寸四寸跳到12英寸，瓶颈就可以大大突破。另一个方向是光电集成（封装），TSMC做COUPE，专门做了包括硅光包括电芯片的集成平台，其他FAB也会努力。

[5-10年展望] 以前大家说光互联省的钱应该放在算力上，这个概念需要纠正——应该把光互联看作算力的一部分，取得算力最优化的平衡，是共生、共同成长、共同优化的生态。光互联会在AI算力构建中占越来越大的比重，像人脑白质和灰质的比例还有很大成长空间，成为算力不可分割、势均力敌的组成部分。

*(Full raw line-by-line ASR retained in the engine run; the above is the de-duplicated, paragraph-reflowed version with ASR-uncertain proper nouns bracket-flagged. Original Chinese preserved for all company names per the skill's name-fidelity rule.)*

## Change log
- 2026-06-08 — created by `/youtube-intel` from the no-caption Chinese video (mlx-whisper transcription). Discovery-only; no vault page edited. Tier 3 insider interview; aligned-incentive flagged.
