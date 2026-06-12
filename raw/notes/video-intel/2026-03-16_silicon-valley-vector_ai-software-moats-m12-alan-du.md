# 硅谷坐标 x 微软战投Alan Du — AI时代软件的护城河 (Software Moats in the AI Era)

**Source:** Silicon Valley Vector 硅谷坐标 (@SiliconValleyVector) · uploaded 2026-03-16 · 56:46 · 31,980 views / 658 likes · https://www.youtube.com/watch?v=8-vKexfJCkg
**Transcript:** mlx-whisper (large-v3-turbo, zh, transcribe mode), translated by the analyst. **No captions existed; this is ASR** — names/numbers carry extra uncertainty, and several startup names are flagged ASR-garbled below. One ASR repetition glitch (~49:30–50:30, the MSSP/compliance passage) lost part of a sentence.
**Tier verdict:** **Tier 3 (independent media interview) + Tier-2-flavored insider guest + ALIGNED-INCENTIVE FLAG.** Same channel as the 2026-04-24 optical-interconnect note (same treatment). The guest is **Alan Du, partner at M12 (Microsoft's strategic/venture fund, invests off Microsoft's balance sheet, ~$150M/yr, $5–10M tickets, A/B rounds)**. He is asked directly "is Microsoft's moat stronger or weaker?" and answers "much stronger" — a Microsoft employee grading Microsoft. He also names "hot" categories that are exactly where M12 has portfolio bets (AI security, agent identity, optical compute, data quality). Treat the *framework* as a well-informed insider map of enterprise-software AI dynamics; treat every Microsoft claim and every "hot category" as partly talking-his-own-book.

## TL;DR

An M12 (Microsoft venture) partner argues the AI-era software moat is **context concentration**: "context is king" — the real moat is workflow know-how plus proprietary enterprise data sitting behind the firewall, which agent startups cannot reach. Most disruptable: data-mover software, **RPA**, single-feature tools, consulting/market research. Most durable: companies that are the **natural focal point of enterprise information flow** (he names ServiceNow, Atlassian) — they don't get replaced by agents, they *feed* agents, and they absorb the accountability (rollback/patching/compliance) that enterprises won't carry themselves. On the macro: he puts the AI capex-vs-revenue gap at **~$800B–1T of revenue needed within 3–5 years** to justify the investment, says **GPU cluster utilization is 30–40% "maybe lower,"** and argues the next 12–18 months should focus on raising existing-datacenter efficiency rather than only building new ones — a demand-side caution coming from *inside* the Microsoft ecosystem.

## Named entities

| Entity | Claim in the video | Vault page |
|---|---|---|
| Microsoft / M12 | Moat "much stronger" (context + data + distribution + enterprise purchase inertia); admits GitHub Copilot UX "has room to improve"; claims "the vast majority" of internal Microsoft coding is now agent-done (~24 min) | [[MSFT]] |
| ServiceNow | "Natural focal point of enterprise information flow… very durable — not replaced by agents, it *enables* agents"; plus accountability-transfer argument (~15–17 min) | [[NOW]] |
| Atlassian (ASR: "Atlasian/Alasian/Elasian") | Same focal-point durability class; cites Atlassian CEO: the real enterprise moat is decades of accumulated process know-how (~18 min) | none (TEAM on [[software-AI-moat-durability]] scorecard) |
| RPA category (UiPath implied, unnamed) | "AI agents will displace the great majority of RPA vendors" — record-and-replay vs reason-and-act (~11 min) | none |
| OpenAI / "Claw" (= Claude/Anthropic, ASR) | All largest AI companies' ARR combined "maybe under 百亿 [~$10B]" vs >$1T invested (~24–27 min; figure looks stale/loose — see red flags) | none |
| JPMorgan / PayPal | Each holds 15–30 PB of data behind the firewall vs "GPT-4 trained on ~1.5PB" (unit suspect) — enterprise data >> training data (~18–19 min) | none |
| Stripe / Visa / Mastercard | Agent-payment stopgaps: Stripe one-time virtual cards; V/MA tokenized credentials = nearest-term viable; true agent-native payment needs new rails (~34–39 min) | none |
| HiddenLayer, Protect AI, Arize, "rich security"(ASR?), "Veza/vesa"(ASR?), "Securiti/security ai"(ASR?) | AI-native security wave; Protect AI "acquired at a high price" [real: Palo Alto, 2025]; agent identity = hottest security topic (~40–45 min) | none ([[software-AI-moat-durability]] covers PANW/CRWD/ZS rows) |
| M12 hardware bets: "neuralfoss"(ASR-garbled), d-Matrix | "Using optics to replace traditional chips" = a very hot lane; d-Matrix named as a successful portfolio company (~31–32 min) | none |
| CodeRabbit, Qodo (ASR "codo"), Graphite (ASR "grap tile") | AI code review wave — machine-written code volume forces machine review (~47 min) | none |
| Claude Code (ASR "clocode/codecode"), Codex, OpenHands, Cline, Kilo, Cursor, Lovable, Replit | Codegen is commoditized by frontier models (Opus/Codex); if Codex went fully closed "like Claude Code," open-source platforms get squeezed (~47–48 min) | none |
| "Clover Security," "Prime Security," "Clearly/cezo/depthfirst" (ASR-garbled list) | Design/planning-stage security+context startups — the durable SDLC position is where Jira/Slack/Notion context concentrates (~48–49 min) | none |
| "microone" (ASR-garbled), "deterreal" (ASR-garbled) | M12 data-quality bet; vertical AI supply-chain-workflow bet | none |

## Key claims + numbers (approx. timestamps; tags: [verifiable] / [opinion] / [forward])

**The moat framework (~10–20 min + the 46:53 deep-link section)**
- "Context is king. 真正的最终护城河 = workflow know-how + 独有的企业级数据 (proprietary enterprise data) behind the firewall — agent companies can't easily get it." `[opinion]` — his single moat discriminator.
- Most disruptable: (1) data-mover software ("搬运工的软件"); (2) **RPA** — record→replay loses to reason→act agents, "will displace the great majority of RPA providers"; (3) single-feature software (anecdote: a friend's MRI CD needed a paid ~$x00 viewer; he threw the file at Claude, which built a reader on the spot); (4) consulting/market research (agents read all secondary material faster). `[opinion]`
- Most durable: enterprise information-flow focal points (ServiceNow, Atlassian): they enable agents with the context agents need; plus **accountability transfer** — build-your-own agent means owning testing, compliance, rollback, patching; buying from NOW/Atlassian transfers that liability. "Enterprises do the math and DIY doesn't make sense." `[opinion]`
- GPT-4 used "~1.5 petabytes" of training data vs 15–30PB behind a single large enterprise's firewall (JPM, PayPal). `[opinion — unit suspect; training corpora are usually counted in tokens]`
- Traditional+AI vs AI-native: split by customer — big enterprises buy the mature incumbent (procurement complexity + regulatory cost of errors); startups buy AI-native tools. "Both can live well." `[opinion]`

**Microsoft (~21–24 min) — aligned-incentive section**
- Moat "much stronger": serves nearly every enterprise on earth → unmatched data/know-how visibility; distribution + enterprise onboarding inertia is "a very hard moat to cross"; concedes Microsoft "may not be the fastest" builder and **GitHub Copilot UX has room to improve**. `[opinion + aligned incentive]`
- "Inside Microsoft, the great majority (绝大多数) of the coding process has been taken over by agents." `[verifiable-ish — much stronger than public statements (~30% AI-written code per Nadella, 2025); verify at the next MSFT venue]`

**The capex-vs-revenue gap (~24–28 min) — the demand-side caution**
- Total AI compute + early-stage investment has passed (or nears) **$1 trillion**; the largest AI companies' combined annualized ARR "可能都不过百亿" (~$10B as said — see red flags). Gap estimate: **~$800B–1T of revenue needed in the next 3–5 years** to justify the spend. "The market may need to rethink early-stage pricing." `[opinion; the shape matches the vault's Bain-framework citation]`
- Refuses the word "bubble": value real, price has FOMO (pre-product seed rounds at ¥/$ hundreds of millions). `[opinion]`
- AI deployment is wildly uneven: coding ≈ fully agentic already; traditional manufacturing/healthcare ≈ zero (regulation, privacy). `[opinion]`

**GPU utilization + the efficiency pivot (~28–31 min) — the most vault-relevant infra claims**
- **GPU cluster utilization is "30–40%, we think maybe lower."** Causes: high failure rates in training/inference; software faults; **cable/connector installation errors between GPUs/blades**; deliberate over-provisioning (idle backup GPUs to shift workloads on failure). `[verifiable-ish vs published cluster-reliability papers]`
- "~10–25% of failures trace to hardware data-line connections." `[opinion/uncorroborated]`
- Optical interconnect is "an expensive substitute" with physical fragility — ±1°C affects performance; bend radius degrades signal. **New approaches: RF/mmWave to replace copper or optical**; GPU virtualization (VM/Docker-style) to lift utilization from ~30% to 60–70% and cut energy demand. `[forward]`
- "The market's next 12–18 months should figure out: keep building new datacenters, or raise the utilization of the ones already built?" `[opinion — a demand-side watch item coming from inside the MSFT ecosystem]`

**M12 portfolio shape (~31–33 min)** — 100+ companies, 15 unicorns, 6 IPOs `[verifiable at Tier 4 / M12 site]`. Heavy lanes: optics-replacing-chips hardware ("neuralfoss" ASR?, d-Matrix), data quality, AI-native security (HiddenLayer; Arize for eval), vertical AI (supply-chain workflow), gaming (world models), blockchain×AI (agent identity/payments).

**Agentic payments (~33–40 min)** — still "narrative/demo stage." PCI compliance bars agents from holding card data; Stripe single-use virtual cards = stopgap; **Visa/Mastercard tokenized credentials = the viable near-term path**; true agent-native commerce (one-to-many-to-many, fraction-of-a-penny streaming payments) needs entirely new rails — stablecoins "have potential" only in that complex scenario. `[opinion/forward]`

**Agent security (~40–46 min)** — agent identity is "the hottest topic"; agents = a **new attack surface**, threat actors now *internal* (prompt injection, hallucinated actions); paradigm shift passive→active defense; **runtime security unsolved at scale** ("no one has reached scale"); "many traditional security companies do NOT have the capability for this." Protect AI acquired at a high price `[verifiable: Palo Alto Networks, 2025]`. `[mixed; he's invested in this lane]`

**AI coding boundary + the durable SDLC position (~46:30–49:30 — the user's deep-link section)**
- Agents cannot yet write infrastructure-level code (DB engines, low-latency/high-throughput systems): probabilistic codegen vs the 100%-reliability bar; failures there are company-destroying. Application layer only, for now. `[opinion]`
- Codegen itself is **commoditized by frontier models** (he names Opus and Codex as already "writing very well"). The durable position is **upstream, at the design/planning stage**, where the natural context focal point sits (Jira + Slack + Notion + org preferences + industry constraints): "whoever captures context accumulation wins." Code *review* (CodeRabbit/Qodo/Graphite) sees only finished output — less context, weaker position. `[opinion — internally consistent with his focal-point thesis]`
- Open-platform risk: if Codex one day goes fully closed "like Claude Code," many open-source coding platforms are threatened. `[forward]`

**Regulated industries (~49:30–50:30, partially ASR-corrupted)** — the blocker is compliance know-how, not technology. **FedRAMP: ~$5–15M and ~3 years** to clear → most startups walk away; MSSP-style middlemen absorb the compliance burden and resell. M12 has an unannounced investment (due "next week," i.e. ~late March 2026) in a platform helping security software sell to government. `[forward/verifiable later at M12 announcements]`

## Vault cross-reference

| Vault page | Relationship |
|---|---|
| [[software-AI-moat-durability]] | **Strongest cross-ref — confirms AND complements.** The guest's verdicts match the vault scorecard: NOW durable-leaning ("very durable… enables agents" — slightly *more* bullish than the vault's "Contested, leaning durable"), MSFT distribution moat real but Copilot contested (his UX admission echoes the 8%-preference counterpoint), proprietary-data/system-of-record archetype amplified. **But his discriminator is different: context concentration + accountability transfer, never the billed unit.** He never mentions seat-vs-consumption pricing — the vault's primary axis. The two lenses agree on outcomes where they overlap; the billed-unit lens makes a sharper falsifiable claim. His **accountability-transfer argument** (rollback/patching/compliance liability) is a *mechanism the vault page doesn't carry* — a genuine addition candidate at a future refresh. His disruptable list **adds RPA, single-feature software, and consulting** to the vault's honest-counterpoints section (which has DocuSign/support tooling/stock media but no RPA row). |
| [[MSFT]] | Confirms the page's split verdict from an insider angle (with the obvious incentive). The "vast majority of internal coding is agent-done" claim is a **cross-venue check item** for the next MSFT refresh — much stronger than public ~30% framings. |
| [[AI-demand-durability]] + [[hyperscaler-capex]] | **The capex-gap + utilization claims feed the demand watch.** His ~$800B–1T revenue-gap estimate matches the shape of the vault's Bain citation ($500B/yr spend needs ~$2T revenue). The **30–40% GPU-utilization claim creates a tension worth tracking**: hyperscalers say "capacity constrained" while an MSFT-ecosystem insider says clusters run at a third of capacity — both can be true (power/space-constrained ≠ efficiently utilized), and the resolution ("efficiency vs new builds, next 12–18 months") is exactly the vault's "AI inference compute requirements compress" falsification candidate in `_thesis.md`. |
| [[cpo-integration]] / [[datacenter-photonics-supply-chain]] | Two fringe touches: (1) his optical-fragility framing (temperature/bend sensitivity as a failure source) is a reliability counterpoint the optical-everywhere narrative rarely carries; (2) **RF/mmWave as a copper/optical alternative** for intra-DC links is a low-probability substitution vector — Tier-3 watch item only, no vault primary source has ever mentioned it. M12's "optics replacing chips" portfolio lane (photonic compute) is adjacent-but-distinct from the vault's interconnect thesis. |
| [[NVDA]] | Indirect: over-provisioning + failure-rate claims align with known large-cluster reliability literature; no new NVDA-specific claim. |

## Ingest leads (what to verify at primary)

1. **"Vast majority of Microsoft internal coding is agent-done"** → check the next MSFT earnings call / Build keynote for an updated AI-coding share figure (public record was ~30%); a real jump would strengthen the Copilot/GitHub leg of [[MSFT]]'s contested verdict. *(Cross-venue gap lens: a conference-only claim like this never appearing in filings is itself the pattern.)*
2. **RPA as a named most-disrupted category** → candidate addition to [[software-AI-moat-durability]]'s honest-counterpoints at a future refresh (needs a second Tier-3 source or a primary signal, e.g. UiPath NRR/guidance deterioration — UiPath is not vault-covered; this does not by itself cross the page threshold).
3. **GPU utilization 30–40%** → look for any hyperscaler primary disclosure on cluster utilization/efficiency programs (MSFT "Maia tokens-per-dollar," GOOGL efficiency framing) at next hyperscaler refreshes; this is the demand-side efficiency falsifier in concrete numeric form.
4. **Protect AI acquisition** → verifiable now (Palo Alto Networks 2025, ~$700M reported) — consistent with the PANW row's "platformization + agent identity" framing; no page edit needed.
5. **Agent-identity/runtime-security gap at traditional vendors** ("many don't have the capability") → a question to hold against CRWD/ZS/PANW rows' "Durable" verdicts when any of them is first ingested at primary.
6. **M12 government-sales-platform investment** (unannounced at recording) → identifiable at Tier 4 via M12's March–April 2026 announcements if the FedRAMP/GovTech angle ever matters to the vault.

## Contradictions / red flags

- **Aligned incentive, twice over:** an M12 partner grading Microsoft's moat "much stronger," and naming as "hot" exactly the lanes M12 owns (AI security, agent identity, optical compute, data quality). His Copilot-UX concession earns some credibility back, but the MSFT verdict should be read as an insider's brief, not evidence.
- **"绝大多数" (vast majority) of MSFT coding agent-done** — materially stronger than any public Microsoft statement; likely loose conversational inflation.
- **"All largest AI companies' combined ARR under 百亿/$10B"** — stale or garbled by March 2026 (single companies were publicly reported above that); the *gap* argument survives, the specific figure doesn't.
- **"GPT-4 trained on 1.5 petabytes"** — wrong unit or garbled; corpora are counted in tokens. The enterprise-data-dwarfs-training-data point is directionally fine.
- **Utilization-vs-constraint tension:** "clusters run at 30–40%" sits awkwardly next to hyperscalers' "capacity constrained" guidance — flag both directions rather than adopting either.
- **ASR quality:** multiple startup names are uncertain (flagged in the table); one passage (~49:30–50:30) partially lost to a Whisper repetition loop. No vault-relevant claim depends solely on a garbled span.

## Source-tier verdict (restated)

Tier 3 interview + aligned-incentive insider guest — do not cite as vault fact; use to generate questions; verify against primary sources before any page edit. The two durable take-aways worth holding: (1) the **accountability-transfer moat mechanism** as a complement to the billed-unit lens on [[software-AI-moat-durability]]; (2) the **utilization/efficiency-vs-new-builds question** as a concrete form of the demand-durability falsifier.

## Verification addendum (2026-06-12 — deep-dive web check, Vic-requested)

The three flagged macro claims were verified against online sources (recent 3 months prioritized). Results:

| Claim | Verdict | Evidence |
|---|---|---|
| **GPU utilization "30–40%, maybe lower"** | **SUPPORTED — and "maybe lower" is dramatically true at the enterprise edge.** The single number hides three metrics: (a) frontier **training MFU** runs 35–45% on Hopper (Llama 3.1 reported 38–43%; <30% "warrants investigation") — partly a physics ceiling (communication/memory-bandwidth waits), not pure waste; (b) **enterprise fleet utilization**: Cast AI's 2026 Kubernetes report (production telemetry, 23,000 clusters) measured **average 5% GPU utilization** — VentureBeat calls it "the $401B problem"; a Rafay case study found 20 inference jobs on 10 A100s = 5% utilized; (c) Meta's >90% "effective training time" is uptime/goodput, a different metric. The guest's blended insider number is fair. | Cast AI 2026 report via VentureBeat/TechRadar; MFU literature (SemiAnalysis 100k-H100 writeup, Llama 3.1 paper figures) |
| **"10–25% of failures at data-line connections"** | **PLAUSIBLE, top end slightly high.** Meta Llama 3 (16,384 H100s, 54 days): 419 unexpected interruptions (~1 per 3 hrs); >50% GPU/HBM3; **network switch/cable = 8.4%** strictly, low-teens including NICs/adapters (software+network-cable+adapter mix = 41.3% of unexpected). Over-provisioning backup GPUs = confirmed standard practice. | Tom's Hardware / DCD coverage of Meta's published Llama 3 reliability data |
| **"$800B–1T revenue gap, 3–5 years"** | **ACCURATE — it is Bain's number restated.** Bain 6th Global Technology Report (Sept 2025): ~$2T/yr new revenue needed by 2030; even with AI savings, **~$800B short**. Goldman (2026) baseline: $765B AI capex in 2026 → $1.6T/yr by 2031 ($7.6T cumulative); hyperscalers would consume ~94% of operating cash flow. Sequoia's $600B-question framing: gap "widening, not closing" in 2026. The guest's ">$1T already invested" is consistent with cumulative capex through 2025–26. | Bain press release; Tom's Hardware; Goldman Sachs insights; CNBC (Apr 30 2026: 2027 big-tech capex seen topping $1T) |
| **"Largest AI companies' combined ARR under 百亿/~$10B"** | **WRONG — stale by ~18 months.** At recording (Mar 2026): OpenAI ~$20–25B + Anthropic ~$20–30B. By Apr–May 2026: Anthropic ~$30B gross ARR (passing OpenAI; OpenAI disputes ~$8B of it as gross-vs-net), OpenAI Q1 revenue ~$6B (~$24B+ annualized). Combined ≈ **$50–78B — 5–8× his figure** (a 2024-vintage datapoint). **The gap argument still survives**: $50–80B ARR vs $725B/yr capex and Bain's $2T requirement. | The Information; SaaStr; Sacra; the-ai-corner |
| **Tension with "capacity constrained" guidance** | **RESOLVED — both true, different layers.** MSFT Apr 29 2026 call: Amy Hood "capacity-constrained through at least the end of the fiscal year"; **Nadella: "a bunch of chips sitting in inventory that I can't plug in"** (power-gated installation). The constraint binds at the **megawatt/shell layer** (can't install chips); utilization is low at the **workload layer** (MFU physics + enterprise idle + failures/over-provisioning). Not a contradiction — and the Nadella quote is the cleanest primary-flavored confirmation yet of the vault's power>compute forward-edge entry. | MSFT Q3 FY2026 call coverage (CIO Dive, Windows Forum, DCD, Introl) |
| **"Next 12–18 months: efficiency over new builds"** | **HALF-RIGHT.** The efficiency wave he predicted is real and very recent — Kubernetes 1.34 **DRA** (fractional GPU allocation), NVIDIA **KAI scheduler**, **MIG GA** in SUSE Virtualization 1.7 (Jan 2026), Run:ai — exactly the "VM/Docker for GPUs" he described. But the industry is doing **both**: 23GW under construction, ~190GW hyperscale capacity announced across 777 projects. No pivot away from new builds is visible. | SUSE/KubeCon EU 2026; AWS builder docs; BNEF; datacenters.com |

**Net read for the vault:** the guest's utilization + gap claims hold up far better than his ARR figure. Two vault hooks strengthen: (1) the **demand-durability falsifier now has named mechanisms** (DRA/KAI/MIG efficiency stack — if enterprise utilization moves from 5% toward 30%+, edge GPU demand softens); (2) **Nadella's "chips I can't plug in"** reinforces the power>compute binding-constraint inversion on [[forward-edge-tracker]] — chips idle in warehouses *because of power* is that entry's catalyst class, surfaced at a Tier-1-adjacent venue (earnings call).

---

## Transcript (Tier 3/5 — not a primary source; mlx-whisper large-v3-turbo ASR, zh original)

你怎么看待微软的护城河
它是变强了还是变弱了
变得非常强了
Context is king
是王道
实际上真正的最终护城河在哪里
是这个workflow的这个knowhow
是独有的这个企业机数据
真正的有用的数据
实际上都是在防火墙后面的
一般做agent的公司
不能轻易能拿到的
整个对AI算力
实际上它已经超过了万亿级的
级别
而你看最大的AI公司
就包括OpenAI Cloud这种公司
它实际上它所有的年化的AR加在一起
可能都不过百亿
阿伦今天欢迎你来到
矽谷坐标的节目
你是微软站头M12的合伙人
微软又是一个最重要的企业软件的玩家
你又在微软的生态里看到的是最前沿的软件的一些变化
你今天的分享将会对我们来说有非常重要的一个指导意义
你可以先给我们介绍一下ARM12吗
可以可以
感谢感谢热情邀请
M12是这个微软的战头基金
我们是直接从资产负债表上做投资的
大概每年的投资额有1.5亿美元左右
基本上去看中的几个方向
包括基础的算力
新一代的这种芯片硬件
再往上会看一些软件类
包括相对来说水平的软件
数据库这方面的科技
然后外加还有一些到后面是垂直的具体的软件
Application
另外这里头还包括比如说网络安全
甚至到后期还会涉及到一些
比如说做gaming游戏产业
还有一些更前沿的技术
基本上就这几个大块
对
你们一般是投哪一个阶段呢
大概你们的ticket size有多大
ticket size基本上是5到10个million吧
我们一般是愿意跟比较头部的
所谓的财务投资人去合作
类似于能叫得出来名字的
基本上都是跟我们有use case的
合同案例的
基本上是focus在A轮和B轮之间
当然也会有时候
有例外会看一些比较早期
或者甚至更后期的项目
这个没有一个特别硬性的规定
但是我们对外说基本上就是A轮B轮为主
明白
所以你们是更加处在一个跟头
不是一个领头的一个角色是吧
对
我觉得其实跟头与领头
实际上怎么说呢
从创业者角度来讲
有一个好的商业投资人
财务投资人作为领头
我觉得是更合适的
因为从这个价格制定
以及他的这个投资条款的制定方面
在商业投资人
财务投资人这边
他们可能会做的专业性更强一点
二
由于颤头基金往往会带一些他们自己商业方面的考虑
这个使得在投资的时候
可能他们考虑的维度不大一样
考虑到这些
实际上作为财务投资人
他们更适合做在领头
这里我觉得其实领头与否
更重要其实要看重
就是说首先
这个战头基金它投多少
多数的战头基金是投相对来说比较小的ticket size
基本上很多
你像这边比较有名的SaaS公司
他们每次投可能就投50万100万
就是大概几百万这样
像微软M12这边能投一次500万到1000万之类的
这种区间的战头基金还是相对少的
我们也愿意提供更多更多的资源
所以我们带来的不光是500万到1000万之间的资金支持
更多的是我们后端庞大的生态系统
以及给他们带来的商业价值
现在如果有一个初创公司
然后他想去融资
你觉得他应该怎么样去思考
我应该去找企业战头部
还是去找像独立的这种VC
财务考虑的VC
我觉得
我的建议是都要去聊
为什么
尤其是现在我们看到
特别多的AI深层科技的创业者
他的技术性非常强
聊的东西也是需要对方
或者投资人的这种技术经验
也需要有一定的门槛的
那么我觉得在这方面
你如果光跟财务投资人聊
可能聊的深度是有限的
比如说你在确定了一个财务投资人领头之外
我的建议是去找一些比较合适
比较懂这个领域的战略投资人
帮你去round out这个round
这样子我觉得
这个combination实际上是
这个组合是非常非常powerful的
而且会给整个市场一个非常强的信号
现在如果有一个初创公司
他出来创业
他很担心的是自己可能做的一个idea
很快就被大厂的一个feature给淹没了
那你会作为这个M12
你会怎么样去考量这个初创公司
他在面对这些大厂
他真正的这个生存空间有多大
我觉得这个担心有点被过度放大化了
为什么呢
就是当我在最早最早开始设计
这个涉入这个VC领域的时候
经常就有人会问
我在做一家公司
经常有投资人问我
为什么Google不能这么做
我觉得其实你觉得Google
或者是微软Amazon这样的公司
它是一个非常非常庞大的公司
但是真正涉及到具体产品的时候
他们其实是很小的一个团队
在做某一个具体的产品
但实际上他们能够调用到的资源
也是有限的
还有更重要的一点
实际上就是你的速度
很多情况下
大的公司由于他的现有的产品
已经非常的赚钱
或者已经卖给了很多很多的客户
他要再做自己的新的产品
自己去革命自己的话
这个是有一定阻力
或者是有一定惯性在里面的
你作为一个初创公司
你是没有全面的那些包袱的
你可以跑得更快
可以用最新的技术
可以去反复的试错
相对来说
你的试错成本又很低
因为你一个初创公司
而不是亚马逊
谷歌微软这样的公司
你这边要出一点错
你的客户是非常不愿意原谅你的
对吧
你作为一个初创公司
你卖给的一般卖给的对象
可能是相对来说比较
也是类似于初创公司
更愿意去试错的这种对象
那么对你来说
你可以迅速的去迭代
迅速的去调整你的产品
你还是有非常大的优势的
除此之外
我觉得还有像类似于这种大的公司
大的平台
他们更多是在专注于建一个通用的技术
比如说针对市场中80%的用户
而你作为一个初创公司
你可以先找到一个相对比较neesh
或者一个比较窄的垂直
这个垂直是你非常非常懂的
对吧
那你不去做这种80%的通用式技术
通用式软件
你可以就做这1%2%的垂直性软件
垂直性技术
这个实际上也可以做的非常非常的大
今天想跟你聊聊
这个软件行业的整个的一个背景吧
软件行业今年是从去年开始
发生了一个很大的变化
你是怎么去看待现在这些公司
哪些是被颠覆的
哪些可能部分颠覆
哪些可能是被错误定价的
或哪些其实是互乘合在这个过程中
是被增强的
这个就是大家在市场经常叫的
这个trillion dollar question
就是万亿级的一个问题
我觉得首先SaaS公司
软件公司不能一概而问
因为软件它分垂直软件
分水平式软件
然后这个里面细分化就层次又非常非常的复杂
我觉得最容易被颠覆的软件属于那种
怎么说那种类似于搬运工的软件
比如说把你的数据从这里搬到那里
它非常的浅
二类似于像比如说RPA软件
叫robotic process automation
这种软件
它从最早的只是说
把你的行为录下来
录下来之后再去用机器
相当于是重复它
这个里面实际上是相对来说
比较简单的一个技术
实际上用现在这种AI的agents
去智能体去代替的话
它是从最早的一个录制
反复到现在是去reason
去推理
然后再去act
再去执行
我觉得这是一个是非常颠覆性的一个技术
这个可能会去在市场上绝大多数提供这RPA服务的公司
除此之外
我觉得类似于单feature的公司
单功能的这种软件公司
肯定是会被颠覆的
一个很好的例子
就是我前一段时间跟一个朋友聊到
他去做核磁
核磁共振
结果他跟他的医生说
你把我的拍出来的片子给我好吗
然后医生就给他寄了一个CD过来
他放进电脑里一看
说现在你现在找能读CD的盒子
现在大家基本上都没有那个东西了
他把它放进去一看
他只需要一个非常特殊的软件
这个软件你要去买
这是一家公司
不知道是可能是美国中西部地区的一家公司提供的软件
你要去花可能几百美金去买一个软件
他说我不可能是花这个钱的
直接就把他把这个文件就扔给了cloud
cloud
cloud实时就造了一个软件去把这个东西读取出来了
所以类似于做这种非常薄
或者是非常非常这个single feature
就是单功能的软件
我觉得是非常容易被颠覆的
除此之外
还有比如说我们经常提到
做consulting
做这个咨询公司
做这个research
市场调研的
我觉得这一块也很可能
很快的
而且我们现在正在看到
他被取代
被颠覆
因为你作为一个consultant
作为一个咨询师
你其实就是读取很多二手的这种市场材料
你可能会做一些一手的这种市场调查
但多数是以二手材料为主
那你肯定跑不过一个agent的速度
他可以在很短的时间内读完所有网上
有限的
网上能够看到的资料
这个你是没法去跟他竞争的
我觉得什么东西是不容易被取代
或者不容易被颠覆的
其实你看去pool agent
去deploy agent的时候
agent首先它是个智能体
但是agent需要大量的context
对吧
他需要大量的数据
真实的数据
我们经常管的叫ground truth
也就是说你的数据的本身的真实性
这个数据的来源
agent是作为一个提供agent的公司
它是没有的
对吧
它是类似于从外到里这么一个motion
那如果你比如说你是一个像
Atlasian或者ServiceNow这种公司
你本身就是一个非常自然的焦点
什么呢
什么自然焦点
就是整个企业信息流的焦点
不管你是从你的ticketing
IT的support这一块
IT的支持
ticketing system到后端的slack
比如说聊天软件
就是整一套它会集中在某一个点
类似于像ServiceNow这种公司
它就变成了一个非常自然的焦点
这种公司我觉得是非常有持久性的
为什么呢
因为它实际上是不会被agent取代
而是它在enable agent
它会给agent真正它需要的信息
这个我觉得是很难取代的
还有一点更重要的就是
首先就像我们最早造汽车
就是从这种作坊式的这种制造
就是你基本上从发动机到后面的轮胎
到后面拧螺丝都要一套一个师傅去做下来
到后面变成非常非常specialized
非常专业化的这种流水线
你的工作就是这么拧这么一个螺丝
如果我作为一个公司
我的核心竞争力是比如说服务给
healthcare服务给健康产业的
我的核心竞争力并不再去搭建一个agent
对吧
我要搭建agent取消在我现在现有的供应商
我是不是还得出去再去招这类的专业的人士
这类人士又很贵
建起来之后我还需要再测试做合规
这一套成本算下来可能是不划算的
对吧
还有就是这个责任的转移
当你出现任何问题的时候
你可以直接去找service now
可以去找了拉线
他们会负责帮你去做回滚
帮你去做patching
如果你是完全自己建立
那你的责任人就是你自己
对吧
甚至你就是说这个责任就在agent这里
你怎么去到后期解决所有support
支持回滚
或者patching remediation这一套流程
这个我觉得企业如果去算一笔账的话
他很快会发现
这边是不make sense的
所以像Atlasian的CEO也是在之前接受采访的时候说
其实企业的真正护城河是他们积累下的几十年的这种流程的经验
这也就是他们的护城河是吧
对说的完全正确
举一个例子我这个数据有点老了
但是我觉得还是非常有代表性的
GPT4这已经是感觉很久以前的一个尖端的model
GPT4整个在训练过程中大概用了1.5个petabyte的数据量
这个数据听起来好像很大
实际上跟真正企业防火墙后边的数据的量来比
这个是微不足道的
首先像类似于JP Morgan
像我之前的公司PayPal
每一家公司防火墙后面都有15 20 30petabyte这种data
它的数据量很明显的
其实你看达到一个GPT4这种GPT4的这种水平的智能
它采用了那么一点点的数据
当企业能够把自己的这个数据利用起来
合理利用起来
这个对性能的提升
对可用性的提升
这个是不是一点点的
会非常非常的客观
所以这个Elasian CEO讲的我觉得完全正确
真正的有用的数据实际上都是在防火墙后面的
那这个东西是一般做agent的公司不能轻易能拿到的
所以真正的model是在那里
所以这些传统的软件公司加上AI的功能
对比于这些AI原生的公司
你更看好哪一个
我觉得要分开来看吧
首先看你针对的客户是什么
传统的公司我觉得卖给大企业
大企业由于它整个购买采购的这个流程是非常非常复杂的
而且涉及到可能非常非常严格复杂的监管程序
那他更愿意去买
比如说类似微软
买Alasian
这种公司的服务
因为它是一套成熟的服务体系已经建成了
那对他们来说
只一旦出现错误
这个成本是非常非常可观的
甚至是不能容忍的
那对于一个相对来说
可能服务于新兴的这种产业
或者是服务给别的startup
别的startup可能更愿意用
这个比较AI native的工具
他们比如说新的小的startup
他招来的人
他可能就是在学校里的时候
就是一直在用这种新的工具
在去试验
对他们来说失措成本很低
而且他们可以跑得更快
我之前讲说你作为一个startup
你怎么觉得怎么才能保证说
不被谷歌的一个feature release
这个发布淹没掉
那你就是比别人跑得更快
那你就要去敢于去试用这种新的工具
新的平台
新的model
那我觉得实际上它是针对不同的市场
都是可以
我觉得活得很好的
你怎么看待微软的护城河
它是变强了还是变弱了
我觉得总体来说是变得强
变得非常强了
怎么说呢
回到我们刚刚的那个话题
就是实际上真正的最终护城河在哪里
就像你说的是这个workflow的这个knowhow
是独有的这个企业机数据
这一块呢
首先微软本身它是服务于整个全世界所有的企业
甚至多数的个人都在都在用微软的服务
那我们能够看到的数据能够看到的人的这种在生产过程中积累的这种knowhow
我觉得是很少公司能够跟我们相媲美的
这一点实际上在搭建agent中可以是虽然我们可能速度没有人跑得快
但是真正搭起来的agent
我觉得从使用体验这一块可以做得非常非常的好
还有更重要一点就是企业其实在购买软件购买服务的时候
它还是存在一定惯性的
它每去onboard一个新的软件进来
它是有非常非常复杂的流程
就是很多这种它的区分并不是发生在技术层面的
而是发生在那种非技术层面
比如说人跟人之间的这种交流
就是你销售团队懂不懂怎么去卖给enterprise
懂不懂卖给这个卖给smb所谓中小企业
它实际上是完全不同的一种甚至讲了不同的语言
所以说是这一块你有现有的这个渠道
现有的distribution
这是一个非常非常难以跨越的一个一个一个互乘河
那当然我觉得微软其实自己做的产品
很多地方也需要提升
在这一块用户体验上
比如说我们的getup copilot
在这一块我们是承认
其实是有一些提升的空间的
但是对我们来说
由于这前面大量的这种积累
由于我们庞大的用户群体生态群体
我们一旦需要去有新的质量性能提升的时候
我们是可以做的非常非常好的
资本市场一直在反复的讨论
像微软这样的大厂资本开支和它的AI收入之间的落差
包括谷歌的CEO也承认会有一些可能AI的这种泡沫的一些元素
那你们从微软的角度上
特别是你们看到的就是企业在真正的部署环境中的有多少的比例
versus像还是在POC探索阶段的这个比例
你觉得趋势是怎么样的
对就是对AI的应用部署
它不是一个齐头并进
它不是一个水平式的前进
它是在某些领域里面跑得非常非常快
某些领域基本为零
很好的一个例子就是在AI写代码这里
基本上现在我们碰到过的公司
甚至就是微软内部绝大多数的就写代码的这个过程是被Agent取代了
就在这一块其实AI的推进是非常非常快的
但有一些领域就稍微慢一些
比如说类似于传统的生产制造业
healthcare
这一类我觉得AI它是相对来说可能还是在慢慢的开始
它有很多这种也是非技术上的原因
监管啊privacy
隐私这个法律上面这一套东西会限制它的进度
那说回到这个投资这一块
其实怎么说呢
不能叫我觉得叫泡沫这个词
其实是一个非常不严谨的叫法
首先泡沫的定义是什么呢
我觉得要区分来看
就是这个东西它的价值和它的价格要分开来看
AI是没有价值
是不是有价值的是绝对有价值的
这个我觉得是没有办法去去质疑它本身的价值
那在价格上面
我觉得是不是有一些存在跟风呢
或者就我们这边叫FOMO啊
这个叫错过恐惧症吧
绝对是有存在的
很多公司
初创公司
由于它创始人背景很厉害
出来之后
我觉得可能都不要说产品成熟与否
就是连技术可能做研发这块是刚刚开始
就可能会容几亿甚至十亿这样的这个种子轮
我觉得这个可能是市场
多少有一些过热
多少有一些FOMO的表现
这个是存在的
而且从具体数字上来看
这个整个对AI算力啊
还有就是包括早期公司的投资
实际上它已经超过了万亿级的级别
或者已经接近万亿级了
而你看最最大的AI公司
就包括OpenAI
Claw这种公司
它实际上它所有的年化的AR加在一起
可能都不过百亿
这个实际上是有一个很大的落差
那么中间这个Gap是可能有人估算是可能1万亿
或者是8000亿美元左右
这么一个Gap
也就是说接下来三年到五年之间
这些公司或者新兴的AI公司
需要产生大概8000亿美元的总体的营收
才能够去justify前面万亿级的投资
我觉得这个Gap还是挺大的
市场可能需要重新考虑一下
就是说早期公司的这种投资定价
二就是硬件
算力中心这块投资方面
可能更需要专注于
比如说不光是建新的Data Center
数据中心
而是要把现有的数据中心的效率提升
通过新的硬件的开发
或者是在软件层面
对现有数据中心的使用率提升
现有数据中心实际上
在看那种GPU集群的时候
它的使用率是非常低的
有的人会说是30%到40%
我们可能觉得可能会更低
你其实花了上万亿的投资
在里面建了这么多的Data Center
你的使用率却那么低
对吧
你那是去继续去建新的Data Center
还是说focus on
就是把现有的Data Center的使用率提升
我觉得这个也是市场可能接下来
12到18个月之间需要去搞清楚的一件事情
为什么它的使用率这么低
这里头原因就很复杂了
首先就是GPU在做训练
或者在做Inference的时候
它的这个Failure就失败率
出错率是非常非常高的
它有时候会出错
是转移出错在软件层面
甚至有时候出错会出错在什么呢
就是在比如说这个GPU跟GPU之间
或者这个Blade跟
就是我们讲板子跟板子之间的这种连接线的
这种安装出错
都是有可能造成整个这个训练过程去出错失败的
它其实出错的原因会有很多
还有一点呢
就是在去做训练的时候
它们会叫over provision
就相当于是会有很多backup的GPU的放在里面
就是空闲着
但是是需要去做一旦出错的时候
马上把这个workload shift到另外一个GPU这边
它是非常非常有益的这种做法
那如果有什么好的办法可以去改进吗
有啊
现在有一些人提出来就是说怎么把GPU像早期的做这个虚拟VM
虚拟机的方式
能够让这个
首先这VM就像Docker Container Kubernetes
实际上最早是提升了这个硬件的使用率嘛
那大家想说是不是可以用同样的VM的方式去解决GPU的使用率
还有呢就是我觉得甚至在硬件方面都有很多新的技术出来
啊去想去tackle这个这个GPU
它比如说70%的这种failure
啊是出错率
其中可能涉及到有大概10%到25%
原因是出在硬件的这个这个数据数据线连接端
这都有可能的
那光铅呢是一个比较昂贵的一个替代品
但是光铅本身自己有一些物理特性
比如说它对温度的敏感可能提升或者降低一摄氏度
都会都有影响它的这个performance
啊甚至就是它的这个弯折呀
就是传光铅的这个管子里面的这个如果有折把它把它弯弯到一定程度
也可能是是它的这个信号衰减
就是它里有很多很多的问题
这个都会导致整个GPU在在跑不管你是training
还是跑inference的时候出错
那么现在有一些新的技术比如说想用这个RF啊就是我们讲的这个叫毫米波啊去去代替这个铜或者是光铅
我的意思想说就是实际上大家都在从不同的角度去解决这个GPU应用率以及降呃应用率低的问题
去降低它的出错率这样子你可以从比如说原来30%甚至更低的应用率提升到比如说60%到70%
而且与此同时还可以提升你的这个energy分量
降低你对能源的这个这个需求
明白那想跟你聊聊你们M12一共投了大概有100多家的背头公司
然后其中有15家是独角兽然后6家已经IPO了
你可不可以给我们提供一张就是你们的portfolio的一张这个投资的画像
哪一些是你们重仓的赛道然后都有一些哪些代表性的公司
重仓的赛道有几个吧我觉得
呃一就是我们讲的新的硬件
呃比如说呃这个用光学
呃去取代传统的传统的硬件传统的芯片
呃这个现在是一个非常非常热的一个赛道
我们在这边也做了一些布局在正硬件层面
我们有比如说类似比较代表性的neuralfoss啊
dmatrix这都是非常非常成功的公司
呃另外呢我觉得一个方还有一个方向就是数据层面
呃大家
我觉得都能看到实际上数据是最终的这个护城河之一
那么我们也投了像microone这类的公司就是帮助企业
呃去有医手的非常有针对性的非常干净的高质量的数据
呃除此之外呢我们也投了比如说类似于像这个做网络安全
而且是在就是比较AI native的情况下提供网络安全呃服务
提供这个呃模型安全类似于像比较代表性就是hidden layer
呃rich security呃这类的公司呢我们还是比较看好
但是对这个这个模型的这种performance的eval
呃类似于arise
这都是比较有代表性的公司
呃除此之外呢我们还看了一些呃
类似于垂直垂直方面的公司呃
比如说我们最近投了一家叫deterreal
它是用AI去替代传统的这个供应链上的一些一些workflow
这家公司我觉得是我们在垂直垂直领域这边还是投的不错的一家公司
呃除此之外呢我们也慢慢再看一些啊
我还有一个领域忘忘提了就是类似于在在gaming这一块
呃gaming实际上我觉得现在慢慢也是在回回暖的一个过程中
就是gaming之前整个产业的投资量是非常非常的低的
呃我觉得现在是在在回暖的过程中
尤其是在大量的世界模型或者物理模型的这种开发的情况下
gaming变成了一个非常自然的使用场景
那使得大家对整个这个游戏产业有一个新的呃
兴奋点吧
呃除此之外呢我们也在慢慢看一些有关区块链的项目
这个领域呢是一个对我们来说相对来说
本身区块链这个这个产业并不新
但对我们来说去寻找他和AI的结合点
这是一个相对来说比较新的课题
呃尤其涉及到对这个agent的管理
agent身份的管理
呃以及甚至涉及到了这个agent的支付
这一块我觉得还是可能会看到一些
区块链技术的应用的
所以这一点我们也在慢慢的去去发掘
讲到支付
因为你之前是背景是在paypal的venture做投资
然后支付的这个赛道其实你投了很多非常经典的一些标的
你看到的在这个
这个ai agent的时代
这个支付的范式跟原来有一些什么样的不一样
非常不一样
首先呃
支付的人变了
这个这个接受这个payment
接受支付的这个对象也变了
那我们最早看到的大家都会讲说这个这个agent支付啊
这个智能体支付
市场现在基本上还停留在一个叙事或者是一个实验的阶段
demo的阶段
呃真正你说智能体去去做支付大量的这种呃
支付还是基本上是看不到的
呃
大家觉得这个会是一个
呃下一个爆发点吧
呃
很多他的这个obstacles他的他的挑战存在于首先法律上规定智能体是不能拿个人的信用卡信息的
这个是就是违反了我们叫叫pci compliance呃
就是你任何个人的信息尤其是涉及到信用卡这种支付信息是不能直接给ai
呃
那这里就就有衍生了几个早期的解决方案
比如说给这个呃
你像stripe就早早期推了一个解决方案是什么的
给你一个叫虚拟卡
相当于就是一次性的
这个卡里头
比如说你可以提前写好这个卡里就只装100块钱
然后你让a点去去去去购物的时候就花到100块钱花完了就就结束了
去从别的维度来限制这个agent的这个呃的自由
那这个呢实际上我觉得不是一个长期的有可持续性的解决方案
首先这个速度非常的慢
而且这个还是在利用原有的真人的身份啊
去去衍生一个新的信用卡
这个成本也很高
嗯
还有呢就是比如说你去让你的agent去买东西之后一旦出现了纠纷或者出现了错误的时候
原本是你跟一对一你跟商家之间的一个一个问题
现在变成了你跟商家在家agent的一个问题
这个就变成了非常复杂的一个一个一个纠纷
这个是很难去解决的
呃另外一种解决方案呢就是像visa mastercard
他们推出了叫tokenized credentials
就实际上是
跳过了虚拟卡这一部分
直接用你个人的credentials
你个人的这个这个背景信息
背景信息去直接跳到你的银行里
然后告诉银行里你是可以放这个这么多的款的
比如说这里可以放5块钱
然后呢他通过你的这个呃叫tokenized credentials去authenticate这个这个payment
这是一种做法
这个我觉得可能是近期来
呃来看我觉得还是相对可行的一个方案
但是涉及到真正的我觉得这都不不能叫完全纯粹的agentic支付
呃为什么呢这个
这个归根到底还是在用一个真人的身份
那么agent如果是比如说我是一家公司的这个采购
那我需要agent去帮我同时采购
比如说我要去做一个大模型的训练
去采购数据去采购算力
甚至采购不知道别的什么一套东西的话
那agent本身他用谁的身份呢
他是用我采购员的身份呢
还是说自己有一个agent native的身份
这是一个很难解决的问题怎么去给agent自己的一个身份
然后这个身份呢怎么能够把它做成一个
呃
呃
去可以去verify可以去审计的一个身份
还有就是涉及到之前我们可能看多数看到支付场景是一对一的
我去这个商店买东西
我给这个商店做支付
那我像我刚刚讲到那个场景
比如说我这个agent要从这里去购买data购买数据
然后从这里购买算力
然后从别的地方再去可能
给这个模型的提供商再付钱
首先涉及到
往往这种的交互场景啊
他不是以就是一个dollar一块钱来做
他可能都不是以一分钱来做单位的
他可能是非常非常小
就是fraction of penny
那这个时候传统的这个轨道是跑不了
这种就是所谓的叫vpayment
v支付
他跑不了的
二呢
我刚刚回到回到我刚刚讲就是他原来是一对一的一个支付关系
现在可能是一对多
甚至一对多再对多
他可能有不同层次的
那整个在这个payment流程中
可能传统的管道还是解决不了
所以说真正要做到这个agent能够自己有自己的身份
然后自己能有自己的这个permission
然后再去跟多个别的agent去交互
这个传统肯定解决不了
他是需要一个完全新的infra
去enable这个场景的
那么现在我们看到有一些初上公司在试着在做
但是应该还没有说跑到非常成熟的这种阶段
所以说在这个刚刚你讲到的这个支付轨道
相比于像visa mastercard
还有paypal这样的老玩家的改造他们已有的轨道
versus这些web3 crypto这样的新玩家去建立他们的这个基建
你会更看好web3 crypto这样的
我觉得还是取决于具体的使用场景
如果是简简单单的
比如说我让我的agent去网上帮我找一双
找一双这个跑步鞋
对吧这个完全不需要用任何的这个stable coin
稳定币去解决这个相对来说是比较简单的一个场景
可能用传统的轨道是更廉价更可靠更安全的这么一套解决方案
但涉及到就是我刚刚描述的相对比较复杂
比如说agent对就是一对多对多
而且是非常微小的
甚至是我们叫不光是微支付甚至叫流支付
就是说你在每次用一定算力的时候
马上去做这个计价
然后再去做支付的时候
这个可能我觉得在这个场景下
可能对这种稳定币啊这个使用
还是我觉得有一些潜力的
再给你探讨一下这个网络安全的问题
我们知道当疫情期间的时候
当时的这个城堡的内外的物理的这种边界被打破
那我们现在的这个网络安全
你从agentic的这个AI开始看到
有没有看到一些新的范式
我觉得目前在agent这一块大家聊的最火的题目之一
就是agent identity
就是agent的身份
从早期的agent
这个智能体借用人的身份去做一些工作
比如说调用API
从早期的agent
这个智能体借用人的身份去做一些工作
比如说调用API
到现在说agent
必须要有自己的agent native identity
然后甚至涉及到就是agent
实际上你看我们早期的这个网络安全
相对来说它是一个简单的描述就是开门
对吧
就是确定你这个人是可以进到这里来的
进到这里来之后做什么
可能会有一些简单的解决方案
但是更多情况就是看你这个知道你这个作为一个有智慧的人是不会去乱调用工具去做一些不该做的事情
实际上人们对agent的这种信任还没有达到那个程度
也就是说现在我决定说agent是可以去接触这些resources
接触不管是data
接触是接触各种各样的工具的时候
我还要看到agent实时他在做什么
我还要后期再能做审计
然后agent出错的时候
我怎么再去做这种回滚去做remediation
这一套系统我觉得现在大家是非常关注的一个领域
也是有一些不错的公司
我觉得一是融了很多钱
二是可能现在都已经达到比如说被收购
你想之前有一家公司叫security ai
有一家公司叫vesa
这都是相对来说比较成功的案例
就是在agent identity这一块
还有一块就是数据安全
这个也是一个比较永恒的话题
当agent在实时的调用数据的时候
数据安全的这一套防御体系要做的非常严密
因为很多数据agent是不能看到的
涉及到比如说个人隐私的东西
这一套东西怎么去做更颗粒化的管理
这也是一个相对来说比较热的话题
除此之外数据安全
我觉得还有非常多的领域
这个是一个相对来说大家永远都会关注的
比如说model security这一块
你像我们之前投的hidden layer
还有之前有一家公司叫protect ai
也是一杯很高的价格收购了
大家对model security不停的去做这种类似于red teaming
或者做pintesting
去确认你的model在投放了之后
不会被比如说叫prompt injection attack
不会被别人提走一些秘密的数据
这一套东西是一个相对来说
比较新的领域
大家都会比较在乎
首先你的model再放在外面
我不会被一个黑客去黑
相当于是让model去leak去泄露
比如说客户的数据
比较隐私的数据这一套东西
这一块也是相对来说比较受关注的
你觉得现在传统的安全类的公司
他们已经具备能力去解决这些新的问题吗
很多都没有
很多都没有
我觉得首先agent的出现
完全创造了一个新的attack surface
一个攻击面
而且传统的cyber security
传统的网络安全
我觉得是以被动防御为主
现在完全要变成主动防御
因为agent他做事的速度
他能够造成的潜在的风险
是这种传统的被动防御是无法预见到的
也没有办法避免
所以怎么去提供这种主动防御
像我之前说的这种模型安全这边
实际上是大家投入了很多的资金
很多资金
很多经历去研究这个方面
这个就是一个主动防御的代表
就做比如说类似于叫
我们经常说的叫
red teaming这一块
这个是很多传统的
比如说做fire wall
做这种human人的identity
这块是无法解决的
实际上除了agent本身作为一个新的attack surface
之外
还有非常多的
比如说数据安全
就是叫data security
就是AI的部署使得
首先我们叫threat actors变了
从原来这种你的威胁全是来自于外部
现在变成了其实内部也可以形成威胁
因为往往agents不管是受外部的这种prompt injection的影响
或者说自己就去做产生一些机器的这种幻觉
它会产生很多就是你无法预见的内部的威胁
这个东西你怎么去解决
现在是很难解决的这个事
agent我们叫运行时 runtime security
现在是非常难解决的一件事
你可以知道ok我是给了agent access
他可以去到这种几个不同的环境里去做事情
但是他实时的在正在做什么
做的这个事是不是我让他做的事
这个事是不是合规的
这个现在是很难真正看到的
有很多公司现在在说我们是在做这个 runtime security
但是真正其实做到规模的我们现在还没有看到
你觉得现在AI它能够胜任去写底层的一些代把吗
比如说数据库的这些引擎
特别是对于这个延迟然后吞吐量以及对于稳定性要求极高的这种环境
我觉得他写底层的代码可能现在还是有一些距离的
我觉得停留在应用层面为主吧
写底层的代码它的复杂程度远远超过于现在现有agent的能力范围
而且底层代码实际上它本身你看在agent写代码的时候
它是一个类似于有一个概率性的元素在里面的
而底层代码99%的可靠度是不行的必须要100%
因为底层代码底层的工具
这个底层的infra一旦出错
整个公司可能面临的是一个可能是毁灭性的打击
所以在这里我觉得首先agent它能力还没有到那一部分
二是人对它的这种信任还没有到那一部分
而在这个application层面就是应用层面出现错误
它有一定的这种概率性是可以容忍的
因为它一旦出错之后它产生的风险
它产生的这种damage实际上是有限的
那这样的一个能力边界对于infra的一些创业公司
有一些什么启发呢
有一些比如说在写代码这一块
你看大家最熟悉的就是codex
然后另外有一项什么open hand open code
这个kilo啊cline这种公司就可以就有很多很多啊
这类相对来说叫open source的platform
然后呢除此之外就是由于这个机器写的代码的这个量在飞速的增长
很多人就说ok那我们做review的时候是不是要用机器来做review
这个是肯定的
因为多数时间这个你把你的code给另外一个一个engineer去review的时候
人家有自己的工作人家可能就是多数看一下
比如说就是很简单的看一下你有没有你的difference啊什么的
基本上就是一个check the box的这么一个motion啊
那另外这一块我觉得就是code review这一块现在有很多比较有趣的公司
你像code rabbit啊codo啊这个这个grap tile这类的公司
其实也是融了不少钱而且是成长还是相对比较快的啊
因为对这个啊机器产生的这个code这个这个这个啊质量啊
大家现在还是存在一定的这种质疑程度的
那除此之外实际上现在很多呃就是你刚刚提到这个基础层面的呃软件或者基础层面的代码去写
因为他出错的成本是非常非常高的
那这个时候呢呃呃就需要在早期做这个计划叫planning stage
或者在做这个设计的时候就需要有一些AI的辅助
啊确定你在早期设计这一套后端怎么写code后端写这个软件的时候
你的合规你的这个风险的控制就已经在最早最早设计层面的时候呃被考虑到了
那现在有一有一些很有趣的公司在这在这个层面已经做出了一些呃小的traction
比如说像那个啊clover security啊这个prime security啊还有啊clearly
cezo啊depthfirst就是这个这个list还是这个这个这个这个这个类还是蛮长的他们实际上的理念是什么呢
就是说在这个codegen就是呃这个代码生成呃这一块呢他们觉得是基本上是用比较前端的模型

比如说用opus用codex去去去去写就已经呃写的可可很好了那真正能够有护城河长期护城河或者长期能站住脚的呢是什么呢是你必须确定你的呃记忆你的context是会集中到你的这层面
那么你看像clocode还有这个codex如果codex有一天决定要变成完全closed的一个system像像codecode一样的话啊
它可能会威胁到很多这个做open open source的这个platform的生存
而且code review 本身这一块呢它是最后review所有的成品
它对本身的这个context它我觉得看到的是非常有限的那很多人现在想法就是说真正能够看到更多的成品
很多人现在想法就是说真正能够看到更多context的地方还是在我刚提到的这个design这一块它的这个软件的设计层面
因为在早期设计的层面你你的这个接触的数据就非常的多
比如说你要看你的Jira里面的这个这个information
然后你要看你的slack你要看你的notion board
这一套就是就变成了一个非常自然的natural的一个一个焦点
就是你在整个software设计软件设计的流程中这个公司对这个软件的preference它的它的这个比如说个人的喜好或者个性化的一些设置设定或者甚至产业具体产业的要求就完全集中在这一点上他们能够看到所有的context
我觉得这一块实际上就回到你刚刚的问题那里是一个非常有趣的领域这个领域我们现在在真的是在看的比较多一些
我觉得其实到最后最简单的一句话就是context is king
context是王道
在整个这个流程中谁是能抓住这个context accumulation的就是context的集中谁我觉得是最终能够能够跑赢的
最后一个问题是想问关于这个合规行业的AI落地比如说像医院还有这个金融行业这种强借管的行业我们知道AI落地的这个难度可能不是在技术本身而是在它的这个合规可审计包括问责合规行业的AI未来应该是怎么样往前推进
我觉得这个实际上它不是一个技术问题这是一个know how的问题首先你必须在这个领域待了很久往往最后卡住这些公司的或者就是让他们有受阻力的地方并不是在技术层面我觉得你能够把整个合规这一套复杂的流程跑通才是真正的重点比如说一个例子就是我们现在在这个
我们现在投了一家我们现在还没有发布这个信息可能下周这个信息就发不出来了我们投了一家软件平台这个软件平台实际上帮助实际上是帮助别的软件尤其是网络安全这一块把它的产品卖给卖给政府的
那涉及到政府这一块就是相对来说是真的是高监管高风险的一些具体应用场景那这一块很多公司是不愿意去去花这个时间花这个精力去研究我怎么把我的产品直接卖给政府卖给政府首先卖尤其是美国联邦政府它是一个相对严格的审核体系叫FedRamp这个东西
基本上除非你是特别特别大的一家公司然后这个钱是很多然后可以去去请很多lawyer帮你做这个然后请审计帮你做这个事儿
他的成本可能下来要基本上到500万到1500万美元才能够跑完这个流程而且这个流程总共的长都是三年时间
那这个过程使得绝大多数的公司对跟这种类似于高监管高风险的这种生意是往而却步的啊他自己首先就是我我自己现有的这个客户都跑不完呢那我干嘛要花这个钱而且是要三年以后才能见到见到效果那实际上就是有这种类似于呃其实你在这个网络安全这一块也会看到类似于叫MSSP叫Managed Security Service Provider
这种公司实际上它是一个类似于像是承包商或者一个中介别人的软件卖给他们的平台然后他们的平台再转卖给比如说后端的这个呃医院系统啊或者政府系统啊或者甚至大的公司啊或者是大的公司啊
这个实际上就把整个合规的这个负担从本身软件公司这一块转嫁到了这个中间商这这层面那中间商实际上他在做了很多很多年的这种积累之后呢他对整个流程是非常了解甚至他已经有现有的群组织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织�
织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织织�
struggle很久很久
如果你要给现在正在创业的小伙伴们指一个你比较看好的方向你会指哪些方向
方向不敢说吧
我觉得其实AI的这种普遍的部署大众化甚至平民化
使得创业的成本或者创业的门槛变得非常非常的低
就像早期cloud云的部署使得软件公司去做创业去赚新的产品也变得很低
你自己不需要建数据中心自己不需要买一堆机器
AI尤其替代了写代码的这些你不需要再去学写代码了
实际上你很简单就可以再利用不管是lovable or replet
这是cursor codex这一套就是非常非常普遍的系统去写一套
相对来说比较完善的小的程序小的产品
那使得创业的门槛变得非常低
那相对来说对你这个门槛低了
对大家门槛都低了
那更重要最后它细分或者差异是出现在哪里
就是对你针对的某一个领域你自己的know how
在这一块可能就是你是来自于比如说传统健康服务产业
你对这个产业是非常非常了解的
它很多细节的东西是别人不知道的
虽然大家用的工具都一样
但是你可以更合理的利用这个工具
而且你在早期在设计这个产品的时候
你就知道哪些东西是我只有在这个产业里待过的人
炮过的人才知道的东西
这个我觉得是真正做出差异化的地方
你在微软的站头部看到了这么多的创业项目
你最想给这些创业圈的小伙伴们一些什么样的建议
我觉得首先在技术层面
我觉得很多很多新的创业者是非常优秀的
但是可能我经常会遇到一些问题
就是在后期的产品化市场化上面还是有一些欠缺的
当然这个东西是很多是需要经验积累的
尤其是针对华人创业者
在这一块我觉得还是有一些小的建议
也就是说早期的时候
不要光考虑在技术层面做事情
我觉得要在整个生态系统里做一些调研
然后去了解你做的技术将来的应用
针对的市场是哪些
把技术的应用具体化一些
除此之外我的建议是在比如说早期融资的过程中
不要光考虑比如说我一定要达到某种估值
或者是我一定要拿非常非常大的投资机构的钱
才算成功
我觉得很多情况下
在早期创业的时候
更注重的是速度
你能够找到相对合理的估值
相对合理的条款
和一个真正能够帮到你的投资人
其实是更重要的
我觉得这会让你的速度提升很多
还有就是我觉得在融资量方面可以做一些考虑
更灵活一些
很多当然我也知道很多
比如说做这个基础模型开发
原来起步价是非常非常高的
现在可能由于这个整个产业的增长
这个起步价降低了
但是你要想做基础模型训练
可能还是需要3000到5000万美元左右
这一块我觉得很多投资人就比较头痛
我怎么第一笔就融这么大的款项
我觉得可以把它拆分开来
比如说我先去融5个million
然后先有一定早期的叫proof of concept
能够做到一些
就是能够给人demo的东西
我觉得把一个很大的一个融资的round
拆分成一个一两个小的融资的round
然后这样你的这个milestone
可以设置的更小一些
这个可能到最后
实际上是让你跑得更快的一种方式
还有我觉得
更多的是
我会看到很多创业者
他在自己的领域他会非常熟悉
我自己的领域内
我认识所有的人
我认识所有的公司
但是往往你做的这个产品
不光是卖给你自己的领域
是要卖给很多别的垂直领域
甚至你可能完全不了解的领域
在这个时候
我觉得早期搭建团队的时候
要在这方面有一些考量
这个人是不是就完全是跟你一样
只做技术的
还是说他在技术层之外
他对别的产业有深度的了解
他知道怎么去帮你做go to market
这一块我觉得可能是在早期
就需要做到一些考虑的
还有就是我觉得
可能不管是在
尤其是华人创业者
我也见到很多华人创业在这
在这上面就是才坑
他们更多不管是因为性格
或者是文化方面
可能更愿意跟别的华人一起创业
我觉得在这个团队上的这种多元化
也可以有一些考量
因为毕竟你做生意卖给的这个对象
不只是华人企业
你可能涉及到一些别的传统产业
还是需要有一些不同背景的人一起来帮你
提供不同的这种perspective
所以在早期团队搭建的时候
我更建议说去跨出自己的这个舒适圈
去了解一些别的背景的人
然后跟你实际上不光是在技术上有认同
但是更多在别的skill的这个gap上面可以有一定互补的
除此之外呢
我也自己打一个小广告
就是我非常非常喜欢跟创业者合作
喜欢跟他们聊天
因为我觉得在这个过程中
对我自己是个很大的提升
我也曾经帮过很多很优秀的创业者们
去融资啊
去考虑后端的这个业务拓展
所以有这个有兴趣做做创业的这个小伙伴们
愿意愿意找我聊天的
我也很很开心很欢迎
谢谢你今天精彩的分享
非常感谢
感谢感谢
感谢感谢
