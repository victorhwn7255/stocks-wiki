# Jensen Huang: Nvidia's Future, Physical AI, Rise of the Agent, Inference Explosion, AI PR Crisis (All-In Podcast)

**Channel:** All-In Podcast (@allin; Chamath / Sacks / Friedberg / Calacanis + guest host Brad Gerstner) · **Guest:** Jensen Huang (CEO, NVIDIA) · **Upload:** 2026-03-19 (recorded at GTC) · **Duration:** 1:06:06 · **Views:** 622,768 · **Likes:** 11,806
**URL:** https://www.youtube.com/watch?v=gwW8GKwHB3I

## Source-tier verdict (read first)

**Tier 3 with MAXIMAL aligned commercial incentive — treat NVDA-strategy facts as Tier-2 management commentary (colored by incentive), everything else as a bull pitch.** This is the CEO of the most valuable company on earth, at his own conference (GTC), talking his own book *and* the entire AI-capex thesis his revenue depends on. The hosts are AI-long investors (Gerstner/Chamath). So: useful as a high-fidelity read of **NVDA's stated strategy and roadmap** (like an earnings call — verify against filings), but every demand/TAM/"million-x" claim is the most incentive-conflicted possible source. Never cite as vault fact.

## TL;DR

- **Confirms the Groq acquisition** (the lead from the Baker video): NVDA bought **Groq** to add LPUs to its disaggregated-inference stack — Jensen says **~25% of the Vera Rubins in a data center** should be a Groq-LPU/GPU combo. NVDA reframes itself from "GPU company" → **"AI factory company,"** lifting its per-rack TAM ~**33-50%** (Bluefield storage processors + Groq + CPUs + networking).
- **The NVDA-vs-custom-ASIC defense, stated plainly:** don't equate factory *price* with token *cost*. A "$50B factory" produces the **lowest-cost tokens** at ~10× throughput; ~$20B of it is just land/power/shell, and the GPU premium is "$50B vs $40B, not $50B vs $30B." *"Even when the chips are free, it's not cheap enough"* if you can't keep NVDA's pace. **CUDA = "the moat nobody talks about."**
- **Inference explosion:** generative→reasoning = 100×; reasoning→agentic = another 100×; *"in two years computation went up 10,000×"* and "we're inference-constrained," heading to "million-x." *"People pay for information, but people mostly pay for work"* — agents get work done.
- **Physical AI / robotics ($50T category, ~$10B/yr for NVDA now, inflecting):** robots "all over the place" in **3-5 years** — but **China is "formidable… their motors, rare earth, magnets are the world's best, foundational to robotics; our robotics industry relies deeply on their ecosystem and supply chain."** (Directly reinforces the vault's humanoid rare-earth/magnet chokepoint.)
- **Nuclear, as a cautionary analog:** *"we see what happened to nuclear — we shut down the entire industry, now there are **~100 fission reactors being built in China and zero in the US**."* He's warning AI not to get regulated like nuclear was — but it's a striking US-nuclear-deployment-lag datapoint for this session's thread.

## Named entities

| Entity | Claim | Vault page |
|---|---|---|
| **[[NVDA]]** | "AI factory company"; ~$350B rev next yr / ~$200B FCF; gaining share; $1T Blackwell+Vera-Rubin visibility; 40% of business needs full CUDA stack | ✓ (CEO talking his book) |
| **Groq** | **Acquired by NVDA**; LPU for disaggregated inference; ~25% of Vera Rubins should be Groq/GPU combo | no (M&A — verify) |
| **[[AMD]]** / custom ASIC | The "$25-30B custom-ASIC alternative" bear case Jensen rebuts (factory price ≠ token cost) | ✓ |
| **[[GOOGL]]** (TPU) / **[[AMZN]]** (Inferentia, Trainium) | "customers trying to out-Nvidia Nvidia" but also huge customers; AWS to buy ~**1M chips** in coming years | ✓ |
| **[[META]]** (Meta SL) | "Meta SL is coming to Nvidia"; cited as share-gain driver | ✓ |
| **[[TSM]]** (Taiwan) | Strategic partner; enabled Arizona/Texas/California fabs "at incredible rates"; re-industrialize + diversify (Korea/Japan/Europe) + restraint | ✓ |
| **[[MP]]** / rare earth | China dominates rare-earth/magnets/motors → "foundational to robotics"; US must not let AI become "like solar, rare earth, magnets, motors" | ✓ (theme reinforce) |
| Anthropic / OpenAI | Anthropic "$5-6B/month in February" ("Oppenheimer moment"); Dario's $1T-by-2030 forecast "very conservative — Anthropic will do way better" | no (private) |
| BYD / Mercedes / Uber / Tesla | Self-driving partners; "Android (NVDA open platform) vs iOS (Tesla/Waymo)"; Tesla buys NVDA training computers | no (TSLA/UBER no page) |
| Dell 6800 | New 750 GB-RAM desktop workstation for local models / "Open Claw" agents | no (DELL no page) |
| Open Evidence / Hippocratic AI | Healthcare AI-agent examples NVDA works with | no (private) |
| Synopsys / Cadence | EDA tools agents will "bang on"; the control surface / ground truth | no (SNPS/CDNS no page) |
| Mellanox / Bluefield / Omniverse / Dynamo | NVDA-internal: networking; storage processor (Bluefield); simulation "gym"; AI-factory OS (Dynamo) | n/a (NVDA products) |

*Auto-caption garbles:* "Grok" (host's joke) vs **Groq** (the LPU acquisition — distinct from xAI's Grok model); "Open Claw / OpenClaw" → likely **"Open Claude" / an open agent harness** (Jensen's "personal AI computer" framing — verify the actual product name); "$50 industry" → **$50 trillion** (physical AI); "Alpaca IO" → NVDA's reasoning-AV stack (name uncertain — verify); "Peter Steinberger" (agent-governance contributor) — name as heard.

## Key claims (by segment, timestamped, tagged)

**Groq + inference (~0:00-0:09)**
- NVDA **acquired Groq**; disaggregated inference (Dynamo OS) puts "the right workload on the right chip" across GPU/CPU/switches/networking/+Groq. `[verifiable — M&A]`
- Vera Rubin: 1-rack → "four more racks" → **NVDA TAM +33-50%** (Bluefield storage + Groq + CPUs + networking). ~**25% of Vera Rubins** = Groq-LPU/GPU combo. `[opinion/forward]`
- **$50B-factory = lowest-cost-tokens** rebuttal to the custom-ASIC-undercut bear case; ~10× throughput; "$20B is land/power/shell." `[opinion]`

**Physical AI / new OS (~0:11-0:17)**
- **Physical AI = $50T category**, ~$10B/yr for NVDA now, growing exponentially; three computers (train / simulate-evaluate [Omniverse] / edge-robotics). Telecom base stations ($2T industry) → edge AI. `[forward]`
- "Open Claw/Claude" as the **"personal AI computer"** OS (memory + scheduling + IO + skills/tools) running "literally everywhere." `[opinion]`

**AI PR crisis (~0:17-0:21)**
- **17% AI popularity in the US**; AI "not conscious, not alien — it's computer software." Anthropic's doom-warnings: *"warning is good, scaring is less good."* `[opinion]`
- **Nuclear analog: US "zero" new reactors vs China "~100" being built** — the cautionary tale for AI over-regulation. `[verifiable-ish / opinion]`

**Inference scaling + token-per-employee (~0:21-0:31)**
- generative→reasoning 100×; →agentic +100×; **10,000× in two years**; "million-x." `[opinion]`
- **Token-per-employee:** a $500k engineer who spent only $5k on tokens → "I'll go ape"; should consume **≥$250k of tokens**; NVDA "trying to" spend **$1-2B** on engineering tokens; every engineer → ~100 agents. NVDA = 43,000 employees / ~38,000 engineers. `[opinion]`
- Anthropic *"$5-6B/month in February"* = the revenue-scaling "Oppenheimer moment." `[verifiable — verify]`

**Open source / China / diffusion (~0:31-0:40)**
- Models = "technology, not a product"; need **both** proprietary AND open; open models "near the frontier." Chinese open-weights "incredible." `[opinion]`
- **China market: NVDA gave up "95% share in the 2nd-largest market, now 0%"**; licenses approved (Sec. Lutnick); Chinese POs coming; ramping supply. `[verifiable]`
- National-security frame: don't let AI become like "solar, rare earth, magnets, motors, telecommunications" (areas the US ceded to China). Goal: **"American tech stack = 90% of the world."** `[opinion]`
- **Helium** "could be a problem" (Iran/Middle East semi supply-chain risk) "but the supply chain has a lot of buffer." `[verifiable-ish]`

**Self-driving + competition (~0:40-0:48)**
- "Android vs iOS" of autonomy: NVDA = open platform (BYD/Mercedes/Uber/dozens) vs Tesla/Waymo = iOS; Tesla buys NVDA *training* computers. `[opinion]`
- **Share-gain defense:** it's the *system* not the chip; only architecture in every cloud + on-prem + car + space; **40% of business needs full CUDA stack**; Anthropic + Meta SL + open-models all "on Nvidia"; **AWS to buy ~1M chips**. Consensus models (NVDA +30%/+20%/+7% to 2029) "don't understand the scale" / "CYA stuff." `[opinion]`

**Space / health / robotics (~0:48-0:56)**
- **Datacenters in space — measured:** "we're already in space" (CUDA in imaging satellites); cooling = radiation-only (large surfaces); "work on the ground first… will take years." *(Notably less bullish than Baker's orbital-compute pitch.)* `[forward]`
- Digital biology "ChatGPT moment"; healthcare inflects in 5 yrs; Open Evidence / Hippocratic. `[forward]`
- **Robotics in 3-5 years**; **China dominance of motors/rare-earth/magnets = "the world's best, foundational to robotics"; US robotics "relies deeply on their ecosystem."** `[opinion — high vault relevance]`

**Moat / application layer (~0:56-1:06)**
- Dario's $1T-by-2030 non-infra AI revenue forecast = "very conservative; Anthropic will do way better." Every enterprise-software company becomes a **value-added reseller of Anthropic/OpenAI tokens.** `[opinion]`
- **Enterprise software NOT destroyed** — "limited by butts and seats," about to get "100× more agents banging on" SQL/vector-DBs/Blender/Photoshop/Synopsys/Cadence; tools = the control surface. `[opinion]`
- **App-layer moat = "deep specialization" / know your vertical**; customization is "5-6× bigger" than the horizontal platform. CUDA = the under-discussed NVDA moat. `[opinion]`

## Vault cross-reference

- **[[humanoid-robot-value-chain]] + [[rare-earth-magnet-chokepoint]] + [[MP]] — CONFIRMS (high value).** Jensen — the most credible possible witness — explicitly states China's **motors/rare-earth/magnets are "the world's best, foundational to robotics,"** and Western robotics "relies deeply on their ecosystem." That's a direct, Tier-3 endorsement of the vault humanoid thesis's central chokepoint. Robotics "3-5 years" is a useful (incentive-laden) timing anchor.
- **Custom-silicon debate — [[NVDA]] / [[AMD]] / [[AVGO]] / Trainium / [[AI-agentic-CPU-orchestration-reemergence]] — adds (NVDA's side).** The "$50B-factory = lowest-cost-tokens" + CUDA-moat + "it's the system not the chip" + AWS-1M-chips defense is NVDA's stated rebuttal to the ASIC-share-loss bear case. Pair with the Baker video's "Trainium doing best" for both sides. The **Groq acquisition** reshapes the inference-silicon map.
- **[[AI-demand-durability]] / [[hyperscaler-capex]] — adds (bull side, discount heavily).** "10,000× in two years," "inference-constrained," AWS 1M chips, $1T visibility, $250k-tokens-per-engineer — all CEO bull framing, but the *token-per-employee* mechanic is a concrete adoption signal worth watching.
- **[[AI-implementation-deployment-layer]] + [[software-AI-moat-durability]] — CONTRASTS Baker.** Jensen: enterprise software is **NOT** destroyed (agents *expand* tool usage 100×); the moat is **deep vertical specialization**; "customization 5-6× bigger than the platform." This *disagrees* with Baker's "AI net-destroyed trillions at the app layer." Two credible Tier-3 sources, opposite reads — a genuine open question for those pages (and Jensen is the more incentive-conflicted of the two on this point — he sells the picks-and-shovels either way).
- **This session's nuclear thread — adds.** "US zero vs China ~100 reactors" is a vivid US-deployment-lag datapoint consistent with the `nuclear-supercycle-assessment` finding (US nuclear leg is lagged). Used by Jensen as an *anti-over-regulation* analog, not an investment call.
- **Defense/geopolitics + [[TSM]] — adds.** Taiwan re-industrialize/diversify/restraint; **helium** as a semi supply-chain risk (Iran); China-market 95%→0%→licenses-restored. Useful supply-chain-risk color.
- **Off-thesis:** the doomer/PR-crisis debate, healthcare/biology, space-colonization riffs.

## Ingest leads (primary-source-verifiable)

1. **NVDA acquired Groq** — now corroborated by *two* Tier-3 sources (Baker + Jensen). **Verify the 8-K / deal terms** — this is the highest-confidence M&A lead and reshapes the inference-silicon competitive map.
2. **AWS to buy ~1M NVDA chips over coming years** → verify in [[AMZN]] capex commentary / any AWS announcement.
3. **NVDA China market: 95%→0%→licenses approved (Lutnick), Chinese POs** → verify in [[NVDA]] filings / 8-K + export-license reporting (material to NVDA China revenue).
4. **Physical AI ~$10B/yr run-rate for NVDA** → verify in [[NVDA]] segment disclosure.
5. **Anthropic "$5-6B/month February"** → verify against any disclosed figure (Tier-3 hearsay).
6. **Vera Rubin / Groq 25%-of-racks + TAM +33-50%** → verify against NVDA roadmap disclosures.
7. **China rare-earth/magnet/motor robotics dependence** → cross-check at [[MP]] / [[rare-earth-magnet-chokepoint]] / the China-robotics ingest names (the vault already has Chinese humanoid-component filers — this is CEO corroboration, not new primary).

## Contradictions / red flags

- **Maximal incentive conflict.** Jensen's revenue *is* the AI-capex thesis. Every TAM/"million-x"/share-gain claim is self-serving. The "$50B-factory = lowest-cost-tokens" argument is a sales rebuttal — directionally reasonable but unfalsifiable as stated.
- **Contradicts Baker on the application layer** (enterprise software destroyed vs expanded) — flag as a live disagreement, not a resolved fact.
- **More measured than Baker on space** — Jensen "work on the ground first, takes years" vs Baker's near-term orbital-compute bull case. Useful calibration: even NVDA's CEO won't pound the table on orbital compute.
- **"Open Claw" naming** is garbled — do not treat as a verified product name without checking.
- **Self-serving China framing** — the 95%→0%→restored arc is real but presented to support NVDA's export-license interests.

## Source-tier verdict (restated)

**Tier 3 / maximal aligned incentive** — do not cite as vault fact; NVDA-strategy statements are CEO commentary (verify against filings like a Tier-2 call); demand/TAM claims are a bull pitch. Discovery-only: nothing in the vault was touched.

---

## Transcript (Tier 3 — not a primary source)

[Full cleaned auto-caption transcript of the 1:06:06 GTC interview follows. Auto-captions: treat names/numbers as approximate; see garble flags (Groq vs Grok, "Open Claw," "$50 trillion," "Alpaca IO"). Chapter markers: Groq + inference 0:26 · Decision-making 8:53 · Physical AI $50T / OpenClaw / new OS 10:47 · AI PR crisis / Anthropic comms 16:38 · Revenue capacity / token allocation / autoresearch / agentic 20:48 · Open source / diffusion / Iran-Taiwan supply chain 30:50 · Self-driving / competition from customers / growth-slowdown 39:45 · Datacenters in space / AI healthcare / Robotics 47:32 · OpenAI-Anthropic revenue / AI moat 56:10 · Advice to young people 59:04.]


---

### Full cleaned transcript

Special episode this week.

We've preempted the weekly show and there's only three people we preempt the show for.

President Trump, Jesus, and Jensen.

And I'll let you pick which order we do that.

But what an amazing run you've had and and a great event.

Uh >> Every industry is here.

Every tech company is here.

Every AI company is here.

Incredible. >> Incredible. >> Extraordinary and one of the great announcements of the past year has been Grok.

When you made the purchase of Grok, did you realize how insufferable Chamath Chamath would become? >> I had a I had an inkling that that that >> We're his friends.

We have to deal with him every week. >> I know it. >> to deal with him for the 6-week close. >> I know it. >> 2 weeks. >> It's all coming back to me now.

It's it's making me rather uncomfortable.

The The thing is many of our strategies are are presented in in broad daylight at GTC years in advance of when we do it. 2 and 1/2 years ago, I introduced the operating system of the AI factory and it's called Dynamo.

Dynamo, as you know, is a piece of instrument, a machine that was created by Siemens to turn essentially water into electricity.

And Dynamo powered the factory of the last industrial revolution.

So I thought it was the perfect name for the operating system of the next industrial revolution, the factory of that.

And so inside Dynamo, the fundamental technology is disaggregated inference.

Jason, I I know you're you're you're super technical. >> Absolutely. >> it. >> I'll let you take this one.

Go ahead and define it for the audience.

I don't want to step on you. >> Yeah, thank you.

I I I knew you wanted to jump in there for a second.

But it's it's disaggregated inference, which means the the pipeline, the processing pipeline of inference is extremely complicated.

In fact, it is the most complicated computing problem today.

Incredible scale, lots of mathematics of different shapes and sizes.

And we came came up with the idea that you would change you would you would disaggregate parts of the processing such that some of it can run on some GPUs, rest of it can run on different GPUs, and that led to us realizing that maybe even disaggregated computing could make sense.

That we could have different heterogeneous nature of computing.

That same sensibility led us to Mellanox. >> Yep. >> You know, today Nvidia's computing is spread across GPU, CPUs, switches, scale-up switches, scale-out switches, networking processors, and now we're going to add Groq to that, and we're going to put the right workload on the right chips.

You know, we just really evolved from a GPU company to an AI factory company. >> I mean, I think that was probably the biggest takeaway that I had.

You're seeing this fundamental disaggregation where we've gone from a GPU, and now you have this complexion of all these different options that will eventually exist.

The thing that you guys said on stage or you said on stage was I I would like the high-value inference people to take a listen to this, and 25% of your data center space you said should be allocated to this Groq LPU GPU combo. >> to about 25% of the Vera Rubins in the in the data center. >> So, can you tell us about how the industry looks at this idea of now basically creating this next generation form of disaggregated prefill, decode, disag, and how people do you think will react to it? >> Yeah.

And take a step back and at the time that we added this, we went from large language model to agentic processing.

Now, when you're running an agent, you're accessing working memory, you're accessing long-term memory, you're using tools, you're really beating up on storage really hard.

You have agents working with other agents.

Some of the agents are very large models, some of them are smaller models, some of them are diffusion models, some of them are auto auto regressive models.

And so there's all kinds of different types of models inside this data center.

We created Vera Rubin to be able to run this extraordinarily diverse workload.

My sense is And so we added what used to be a one rack company, we now add a four more racks. >> Right. >> So Nvidia's TAM, if you will, increased from what it whatever it was to probably something call it, you know, 33% 50% higher.

Now, part of that 33% or 50%, a lot of it's going to be storage processors, it's called Bluefield.

Some of it will be a lot of it I'm hoping will be Groq processors, and some of it will be CPUs.

And they're all going to a lot of it's going to be networking processors.

And so all of this is going to be running basically the computer of the AI revolution called agents.

The operating system of of modern modern industry. >> What about embedded applications?

So, you know, my daughter's teddy bear at home wants to talk to her.

What goes in there?

Is it a custom ASIC or does there end up becoming much more kind of a broader set of TAM with developing tools that are maybe different for different use cases at the edge and in embedded applications? >> that there's three computers in the problem.

At the at the largest at the largest scale when you take a step back.

There's one computer that's really about training the AI model, developing, creating the AI.

Another computer for evaluating it.

Depending on the type of problem you're having, like for example, you look around, there's all kinds of robots and cars and things like that.

You have to evaluate these robots inside a virtual gym that represents the physical world.

So it has to be software that obeys the laws of physics.

And that's a second computer.

We call that Omniverse.

The third computer is the computer at the edge, the robotics computer.

That robotics computer, one of them could be self-driving car, another one's a robot, another one could be a teddy bear.

Little tiny one for a teddy One of the most important ones is one that we're working on that basically turns the telecommunications base stations into part of the AI infrastructure.

So, now all of the It's a $2 trillion industry.

All of that in time will be transformed into an extension of the AI infrastructure.

And so, radios radios will become a edge devices.

Factories, warehouses, you name it.

And so, so there are three these three basic computers, all of them, you know, are going to be necessary. >> Jensen, last uh last year, I think you were ahead of the the rest of the world in in in saying inference isn't going to a thousand >> Just last year. >> Yes.

Is it going to >> feelings. >> Is it going to 1 million X?

Is it going to 1 billion X? >> Yeah. >> Right.

And I think people at the time thought it was pretty hyperbolic because the world was still focused on pre-scaling, on training.

Here we are.

Now inference has exploded.

We're inference constrained.

Um you announced an inference factory that I think is leading edge that's going to be 10X better in terms of throughput to the next factory.

But yet if you if I listen to what the chatter is out there, it's that your inference factory is going to cost 40 or 50 billion and the alternatives, the custom ASICs, AMD, others are going to cost 25 to 30 billion and you're going to lose share.

So, why don't you talk to us?

What have you seen?

How do you think about share?

And does it make sense for all these folks to pay something that's a 2X premium to what others are marketing? >> The big takeaway, the big idea is that you should not equate the price of the factory and the price of the tokens, the cost of the tokens.

It is very likely that the $50 billion factory, and in fact, I can prove it, that the $50 billion factory will generate for you the lowest cost tokens.

And the reason for that is because we produce these tokens at extraordinary efficiency. 10 times, you know, the difference between 50 billion Now, it turns out 20 billion is just land power and shell, right? >> Right. >> And then on top of that, you have storage anyways, networking anyways, you got CPUs anyways, you got servers anyways, you got cooling anyways.

The difference between that GPU being 1X price or half X price >> Right. >> is not between 50 billion and 30 billion.

Pick your favorite number, but let's say between 50 billion and 40 billion. >> Yeah. >> That is not a large percentage when the $50 billion data data center is actually 10 times the throughput. >> Right. >> Jensen, I want >> That's the reason why I said that even for most chips if you can't keep up with the state of the technology and the pace that we're running, even when the chips are free, it's not cheap enough. >> Yeah. >> Can I Can I just ask a general strategy question? >> Yeah. >> I mean, you're running the most valuable company in the world.

This thing is going to do 350 plus billion of revenue next year, 200 billion of free cash flow.

It's compounding at these crazy rates.

How do you decide what to do?

Like, how do you actually get the information?

I mean, it's famous now these sort of emails that are people are meant to send you, but how do you really decide to get an intuition of how to shape the market, where to really double down, where to maybe pull back, where to actually go into a green field?

How How does that information get to you?

How do you decide these things? >> In a final analysis, that's the job of the CEO. >> Yeah. >> And our job is to define the strategy, define the vision, define the strategy.

We're informed, of course, by amazing computer scientists, amazing technologists, great people all over the company, but we have to shape that future.

Well, part of it has to do with is this something that's insanely hard to do?

If it's not hard to do, we should back away from it.

And the reason for that is if if it's easy to do, obviously, >> Um lots of competitors. >> of competitors.

Is this something that has never been done before that's insanely hard to do and that somehow taps into the special superpowers of our company?

And so I have to find this confluence of things to that meets the standard.

And in the end, we also know that a lot of pain and suffering is going to go into it. >> Yeah. >> There are no great things that are invented because it was just easy to do and just like first try, here we are.

And so if it's super hard to do, nobody's ever done it before, it's very likely that you're going to have a lot of pain and suffering.

And so you better enjoy it. >> So can you can you just look at maybe three or four of the more long-tail things you announced and just talk about the long-term viability of whether it's the data center in space or whether it's what you're trying to do with ADAS in autos or, you know, what you're trying to do on the biology side.

Just give us a sense of like how you see some of these curves inflecting upwards and some of these longer tail businesses. >> Excellent.

Um physical AI, large category.

We believe, and as I just mentioned, we have three computing systems, all the software platforms on top of it.

Physical AI as a large category.

It's technology industry's first opportunity to address a $50 industry that has largely been, you know, void of technology until now.

And so we need to invent all of the technology necessary to do that.

I felt that that was a 10-year journey.

We started 10 years ago.

We're seeing inflecting now.

It is a multi-billion dollar business for us.

It's close to $10 billion a year now.

And so it's a big business and it's growing exponentially.

And so that's number one.

I think in the case of digital biology, I think we are literally near the chat GPT moment of digital biology.

We're about to understand how to represent genes, proteins, cells.

We already know how to understand chemicals.

And so, the ability for us to represent and understand the dynamics of the building blocks of biology, that's a couple of two, three, five years from now.

In five years time, I completely believe that the healthcare industry where digital biology is going to inflict.

And so, these are a couple of the really great ones, and you could see they're all around us. >> Agriculture. >> Inflecting now. >> No question.

Yeah. >> Jensen, I I want to take you from the data center to the desktop.

Uh the company was built in large part on hobbyists, video gamers, and and all those graphic cards in the beginning.

And you mentioned in front of, I think, 10,000 people here, just Claude, uh open Claude, Claude code, and what a revolution agents have become.

And specifically, the hobbyists, who are really where a lot of energy, um we see, you know, a lot of the innovation breaks, want desktops.

You announced one here.

Uh I believe it's the Dell 6800.

Uh this is a very powerful workstation to run local models, 750 gigs of RAM.

Obviously, the the Mac Studio sold out everywhere.

In my company, we're moving to open Claude everything.

Freeburg just got Claude peeled.

You got Claude peeled, I understand, and you're obsessed with these.

What is this from the streets movement of creating agents and using open source on the desktop mean to you? >> So great. >> Where is that going? >> Yeah, so great.

First of all, let's take a step back.

Um in the last two years, we saw basically three inflection points.

The first one was generative.

Chat GPT brought AI to the common everybody, to our awareness.

But the fact of the matter is the technology sat in plain sight months before GPT.

It wasn't until ChatGPT put a user interface around it, made it easy for us to use, that generative AI took off.

Now, generative AI, as you know, generates tokens for internal consumption as well as external consumption.

Internal consumption is thinking, which led to reasoning. 01 and continue that wave of ChatGPT grounded information, made AI not only answer questions, but answer questions in a more grounded way, useful.

We started seeing the revenues and the the economic model of OpenAI start to inflect.

Then the third one was only inside the industry that we saw, Claude Code, the first agentic system that was very useful, really revolutionary stuff.

But but Claude Code was only available for enterprises.

Most people outside never saw anything about Claude Code until Open Claw.

Open Claw basically put into the pop popular consciousness what an AI agent can do.

That's the reason why Open Claw is so important from a cultural perspective.

Now, the second second reason why it's so important is that Open Claw is open, but it formulates it structures a type of computing model that is basically reinventing computer altogether.

It has a memory system.

It scratch is a short-term memory file system.

It has It has It has scales.

Did you say skills or scales? >> Skills. >> Oh, skills. >> have scales, theoretically, yeah. >> Yeah, scales.

So So, the first thing first thing it it, you know, it has resources and manages resources.

It's It does scheduling. >> Yep. >> Right?

And cron jobs, it could it could spawn off agents, it could you know, it could decompose a task and and cause and solve problems as does scheduling.

It has IO subsystems.

It could, you know, input, it has output, it connect to WhatsApp.

And also, it has a API that allows it to run multiple types of applications called skills. >> Yeah. >> These four elements fundamentally define a computer. >> Yeah. >> And therefore, what do we have?

We have a personal artificial intelligence computer for the very first time. >> Open source. >> It's open source.

It runs literally everywhere.

And so, this is now the This is the This is basically the blueprint, the operating system of modern computing. >> Yeah. >> And it's going to run literally everywhere.

Now, of course, one of the things that we have to help it do is whenever you have agentic software, you have to make sure that an agentic software has access to sensitive information, it could execute code, it could communicate externally.

We have to make sure that all of it has to be governed, all of it has to be secure, and that we have policies that it that gives these agents two of the three things, but not all three things at the same time. >> Right. >> And so, the governance part of it, we contributed to Peter.

Peter Steinberger was here, and and so, we've got a mound of great engineers working with him to help secure and keep that thing so that it could protect our privacy, protect our security. >> Jensen, that paradigm shift makes some of the AI legislation that has passed around the country to regulate AI, and a lot of the proposed legislation effectively moot, doesn't it?

Can you just comment for a second on how quickly the paradigm shift kind of obviates a lot of the models for regulatory oversight of AI, which is becoming a very hot topic in politics right now? >> Well, this is This is the part that that you know, we just with policy makers, we need to we need to always get in front of them, and Brad, you do a great job doing this.

We have to get in front of them and inform them about the state of the technology, what it is, what it is not.

It is not a biological being.

It is not alien.

It is not conscious.

Um it is computer software. >> Yeah, exactly. >> and it is not something that um we say things like we don't understand it at all.

It is not true we don't understand it all.

We understand a lot of things about this technology.

And and so so I think one we have to make sure that we continue to inform the policy makers and not affect not allow doomerism and extremism to affect how policy makers think and understand about this technology.

However however we still have to recognize this technology is moving really fast and don't get policy ahead of the technology too quickly.

And the risk that we we run as a nation our greatest source of national security concern with respect to AI is that other countries adopt this technology while we are so angry at it or afraid of it or somehow paranoid of it that our industries our society don't take advantage of AI.

And so I'm just mostly worried about the diffusion of AI here in the United States. >> Can you just double click if you were in the seat in the boardroom of Anthropic over that whole scuttlebutt with the Department of War?

It sort of builds on this idea of people didn't know what to think.

It's sort of added to this layer of either resentment or fear or just general mistrust that people have sometimes at the software levels of AI.

What you would do you think you would have told Dario and that team to do maybe differently to try to change some of this outcome and some of this perception? >> The first thing that I I would I would say about Anthropic is first of all the technology is incredible.

We are a large consumer of Anthropic technology.

Really admire their focus on security.

Really admires their focus on safety.

Um the the the the culture by which they went about it the the technology excellence by which they went about it really fantastic.

Um I I would say that that the the desire to warn people about the capability of the technology is is also uh really terrific.

We just have to make sure that we understand that the world has a spectrum and that that warning is good, scaring is less good. >> Right. >> Um and because this technology is too important to us. >> Right. >> And and I think that it is fine to uh predict the future, but we need to be a little bit more circumspect.

We need to have a little bit more humility that in fact we can't completely predict the future.

And the ability and to say things that that are quite extreme, quite catastrophic, that there's no evidence of it happening um could be more damaging than people think.

And and of course we are technology leaders.

I There was there was a time when nobody listened to us. >> Yeah. >> Um but now because technology is so important in the social fabric, such an important industry, so important to national security, our words do matter.

And I think we have to be much more circumspect, we have to be more moderate, we have to be more balanced, we have to be more for more thoughtful. >> Well, I you know, I would nominate you.

I think the industry's got to get together. 17% popularity of AI in the United States.

I mean, we see what happened to nuclear, right?

We basically shut down the entire nuclear industry and now we have 100 fission reactors being built in China and zero in the United States.

Um we hear about moratoriums on data centers, so I think we have to be a lot more proactive about that.

But but I want to go back to this agentic explosion that you're seeing inside your company, the efficiencies, the productivity gains inside your company.

There's a lot of debate whether or not we're seeing ROI, right?

And you and I entering to into this year, the big question was are the revenues going to show up?

Are the revenues going to scale like intelligence?

And then we had this kind of Oppenheimer moment of 5-6 billion dollar month by Anthropic in February.

Um do you think as you look ahead, you announced a trillion dollar, you know, visibility into a trillion dollars of just Blackwell and Vera Rubin over the course of the next couple of years.

When you see this happening at Anthropic and OpenAI, do you think we're on that curve now where we're going to see revenues scale in the way that intelligence is scaling? >> When you look around, when you I'll answer this a couple of different ways.

When you look around this audience, you will see that Anthropic and OpenAI is represented here, but in fact, every but 99% of everything that is here is all AI and it's not Anthropic and OpenAI. >> Right.

Right. >> And the reason for that is because AI is very diverse.

I would say that the second most popular model as a category is open models.

Number one is yeah, open right, open source.

Open weights, open source. >> OpenAI is number one, open source is number two.

Very distant third is Anthropic, and that tells you something about the scale of all of the AI companies that are here.

And so so it's important to recognize recognize that.

Um let me let me come back and say couple things.

One, when we went from generative to reasoning, the amount of computation we needed was about a hundred times. >> Right. >> When we went from reasoning to agentic, the computation is probably another hundred times.

Now we're looking at in just two years computation went up by a fact 10,000 X.

Meanwhile people pay for information, but people mostly pay for work. >> Yes. >> Talking to a chatbot and getting an answer is super great. >> Right. >> Helping me do some research, unbelievable.

But getting work done, I'll pay for >> Indeed. >> And so that's where we are.

Agentic systems get work done.

They're helping our software engineers get work done.

And and so then you take that you got 10,000 x more compute you get probably at this point 100 x more consumption now.

Yeah.

And we haven't even started scaling yet.

We are absolutely at a million x. >> Which is I think a great place to talk about the number of you have 20, 30,000 at the company something >> We have 43,000 employees.

You know, I would say 30 8,000 are engineers. >> Conversation we've had on the pod a number of times is oh my god, look at the token usage in our companies.

It is growing massively and some people are asking, hey when I join a company how many tokens do I get cuz I want to be an effective employee and you postulated I believe during your two and a half hour Pretty long keynote.

Well done.

That you were spending >> well done, it would be shorter. >> Yeah.

You didn't have time to do a >> So so you guys so you guys know so you guys know there is no practice and so it's a grip and a rip. >> Yeah.

Yeah. >> So so I just wanted to let you know I was writing the speech while I was giving the speech. >> But does that mean if we do >> I apologize. >> Do back of the envelope math 75,000 in tokens for each engineer something like that.

So are you spending in Nvidia a billion, two billion dollars on tokens for your engineering team right now? >> We're trying to.

Let me give you a thought experiment.

Let's say you have a software engineer or AI researcher and you pay them $500,000 a year.

We do that all the time.

Okay, this is happening all of the time.

Um that $500,000 engineer at the end of the year I'm going to ask him how many tokens how much did you spend in tokens and that person said $5,000 I will go ape something else.

If that if that $500,000 engineer did not consume at least $250,000 worth of tokens, I am going to be deeply alarmed.

Okay?

And this is no different than one of our chip designers who says, "Guess what?

I'm just going to use paper and pencil.

I don't think I'm going to need any CAD tools." >> And this is a real paradigm shift in thinking about these all-star employees.

It almost reminds me of of what we learned in the NBA when LeBron James started spending a million dollars a year just on his health of his body like in maintaining it.

That's right. >> Here he is at age still playing.

It really is, "Hey, if these are incredible knowledge workers, why wouldn't we give them superhuman abilities?" >> That's exactly what >> Where does that go if we if we extrapolate out two or three years from now, what is the efficiency of that all-star at an Nvidia and what they're able to accomplish? >> They're going to look like >> Well, first of all, things that the the um wow, this is too hard.

That thought is gone.

Uh this is going to take a long time.

That thought is gone.

Uh we're going to need a lot of people.

That thought is gone.

This is no different than in this in the last industrial rev- revolution, somebody goes, "Boy, that building really looks heavy." Nobody says that.

Nobody "Wow, that mountain looks too big." Nobody says that.

Everything that's too big, too heavy, takes too long, those thought those ideas are all gone. >> to creativity. >> That's right. >> What can you come up with? >> Exactly. >> Which means now the question is, how do you how do you work with these agents? >> Well, it's just a new way of doing computer programming.

In the future >> In the past we code, in the future we're going to we're going to write ideas, architectures, specifications.

We're going to organize teams.

We're going to give them We're going to help them define how to evaluate the definition of good versus bad.

What's the What does it look like when something is a great outcome?

How to iterate with you, how to brainstorm.

That's really what you're looking for and I'm I think that every engineer is going to have hundred a hundred agents. >> Back to the PR problem the industry has right now, you have executives like David Freiberg with Ohalo, who's looking at literally taking through the use of technology, your technology and AI, the number of calories produced and making high-quality cal- calories.

What is the factor you think you can bring the cost down, Freiberg, and what impact does this vision have for what you're doing? >> zero-shot genomic modeling, and it works. >> Yeah. >> then you have that moment and you're like, "Holy sh- Honestly, like and and that's after people are replacing entire enterprise software stacks in a night.

I did something in 90 minutes I was telling the guys about.

Replaced the whole software stack and like a whole bunch of workload. 90 minutes on Claude, ran this agentic system, built the whole thing, deployed it, >> On a Sunday >> night. >> Sunday night. 10:00 p.m.

I was done at 11:30, I went to bed. >> As the CEO, you replaced >> Yeah.

And everyone on my management team had to do a similar exercise.

Over the weekend, what we saw on Monday, I was like, "It's over." But, the technical stuff, the science stuff, we did something in 30 minutes using auto research, and I'd love your view on auto research and what that tells us about how far we still have to go in terms of efficiency.

But, using auto research and a chunk of data, something was published internally that we said, "Oh my god." And that would normally be a PhD thesis that would take 7 years.

It would be one of the most celebrated PhD theses we've ever seen in this field, and it would be in the journal Science, and it was done in 30 minutes on a desktop computer running on auto research with all the data we just ingested.

We got it on Friday, and we're like, "Hey, let's try it." Try it.

Boot it up, went to GitHub, downloaded auto research, and ran it.

And you see everyone's face just go like And then the potential of what this is unlocking for us is like the kind of thing that would take 7 years, and it happened in 30 minutes.

And we're experiencing it in genomics, and we're like, "This is unbelievable." So, I I think like the acceleration is widening the aperture for everyone in a way that like you didn't imagine a few years ago.

But just going back to the auto research point, can you just comment on what you think about the fact that this thing got published with 600 lines of code in a weekend and the capacity that it has to run locally and achieve what it can achieve with all of these diverse data sets and what that tells us about the early stages we are in terms of optimization on algorithms and hardware. >> The fundamental reason why Open Claw is so incredible, number one, is it's com- it's confluence, it's timing with the breakthroughs in large language model. >> Yeah. >> It's timing was perfect.

It was impeccable.

Now, in a lot of ways, Peter wouldn't have come up with it probably if not for the fact that Claude and GPT and ChatGPT have reached a level that is really very good. >> Right. >> It is also a new capability that allows these models to tool use.

The tools that we've created over time, web browsers and Excel spreadsheets and, you know, in the case of chip design, Synopsys and Cadence and uh Omniverse and Blender and Autodesk and all of these tools are going to continue to be used.

There's some Some people say that that the enterprise IT software industry is going to get destroyed.

There's it's There's a Let me give you the alternative view.

The enterprise software industry is limited by butts and seats.

It's about to get 100 times more agents banging on those tools.

They're going to be agents banging on SQL, they're going to be agents banging on vector databases, agents banging on Blender, agents banging on Photoshop.

And the reason for that is because those tools are first of all, do a very good job.

Second, those tools are the conduit between us.

In the final analysis, when the work is done, it has to be represented back to me in a way that I can control. >> Right. >> And I know how to control those tools.

And so, I need everything to be put back into Synopsys.

I want everything to be put put back into Cadence, because that's how I control it.

That's how I ground truth. >> Let me ask you a question about open source.

So, we have these closed source models, they're excellent.

We have these open weight models, many of the Chinese models are incredible.

Absolutely Two days ago, you may not have seen this cuz you were busy on stage, but there was a training run that happened in this crypto project called BitTensor subnet 3.

They managed to train a 4 billion parameter llama model totally distributed with a bunch of people contributing excess compute, but they were able to do it statefully and manage a training run, which I thought was like a pretty crazy technical accomplishment. >> Yeah. >> Because it's like random people, and each person gets a little share. >> Our our modern version of folding at home. >> Exactly.

So, what what do you think about the end state of open source?

Do you see this decentralization of architecture as well and decentralization of compute to support open weights and a totally open source approach to making sure AI is broadly available to everyone? >> I believe we fundamentally need models as a first-class product, proprietary product, as well as models as open source.

These two things are not A or B, it's A and B.

There's no question about it.

And the reason for that is because models is a technology, not a product.

Models a technology, not a service.

For the vast majority of consumers, the horizontal layer, the general intelligence, I would really, really love not to go fine-tune my own. >> Right. >> I would really love to keep using ChatGPT.

I love to use Claude.

I love to use Gemini.

I love to use X.

And they all have their own personalities, as you know, which just kind of depends on my mood and depends on what problem I'm trying to solve.

You know, I might, you know, do it on X or I might do it on on ChatGPT.

And so, that that segment of the of the industry is thriving.

It's going to be great.

However, they're all these industries, their domain expertise, their specialization has to be channeled, has to be captured in a way that they can control.

And that it can only come from open models.

The open model industry we're contributing tremendously to.

It is near the frontier.

And quite frankly, even if it reaches the frontier, I think that products as a service, world-class products as as a models as a product is going to continue to thrive. >> Every startup we're investing in now is open source first and then going to the proprietary model. >> Yeah, and the beautiful thing is because you have a great router, you connect the two by on on first day, every single day, you're going to have access to the world's best model.

And and then it gives you time to cost reduce and fine-tune and specialize.

And so you're going to have world-class capabilities out to shoot every single time. >> Let >> Jensen, can I ask a question? >> Nobody wants the US to win the global AI race more than you.

Right?

But a year ago, the Biden era diffusion rule really was an anti-American diffusion of AI around the world.

So here we are a year into the new administration.

Give us a grade.

Where is Where are we in terms of global diffusion and the rate at which we're spreading US AI technology around the world?

Are we an A?

Are we a B?

Are we a C?

What is What's working?

What's not working? >> Well, first of all, President Trump wants American industry to lead.

He wants American technology industry to lead.

He wants American technology industry to win.

He wants us to spread American technology around the world.

He wants the United States to be the wealthiest country in the world.

He wants all of that.

At the current moment, as we speak, Nvidia gave up a 95% market share in the second largest market in the world and we're at 0%.

President Trump That's right.

President Trump wants us to get back in there and and the first thing is to get license license for the companies that we're going to be able to sell to.

We've got many companies who have requested for licenses.

We've applied for licenses for them and we've got approved licenses from Sec- Secretary uh Lutnick.

Uh now we've informed the Chinese companies and many of them have given us purchase orders.

And so we're going to we're going to we're in the process of cranking up our supply chain again to go ship.

I think at the highest level, Brad, um I think one of the things that we should acknowledge is this.

Our national security diminished when we don't have access to miniature motors, rare earth minerals.

It's diminished when we don't control our telecommunications networks.

It's diminished when we can't provide for sustainable energy for our country.

It is fundamentally diminished.

Every single one of these industries is an example of what I don't want the AI industry to be. >> Right. >> When we look forward in time and we say, "What do we want What is the What does it look like when American technology industry, American AI industry leads the world?" We can all acknowledge that there is no way that AI models is won universally.

It is We can all acknowledge that is an outcome that makes no sense.

However, we can all imagine that the American tech stack from chips to computing systems to the platforms are used broadly by the world where they build their own AI, they use public AI, they use private AI, whatever, and they can build their applications in their society.

I would love that the American tech stack is 90% of the world.

Yes.

I would love that.

The alternative, if it looks like solar, rare earth, magnets, motors, telecommunications, I consider that a very bad outcome for national security. >> Agreed. >> Yeah. >> How much are you monitoring the situation with the conflicts around the world right now, and how much does it worry you, Jensen?

So, China and Taiwan, and then helium availability coming out of the Middle East, I understand, can be a supply chain risk to semiconductor manufacturing.

How much do these situations worry you?

How much are you spending on them? >> Well, first of all, I think the in Middle East, I have we have 6,000 families there.

Uh we have a lot of Iranians uh at Nvidia, and their families are still in Iran.

And so, so we have we have a lot of families there.

The first thing is is they're quite anxious, they're quite concerned, quite scared.

Um we're thinking about them all the time.

Uh we're monitoring and keeping an eye on them all the time.

They have 100% of our support.

Uh I've been asked several times, are we still considering uh being in Israel?

We are 100% in Israel.

We are 100% behind the families there.

We are 100% in the Middle East.

I was also asked, you know, given what's happening in the Middle East, uh is that an area where we believe that we can expand artificial intelligence to?

Um I believe that the there's a reason we went to war, and I believe that at the end of the war, Middle East will be more stable than before.

And so, if we were there if we're considering it before, we should absolutely be considering it after.

And so, I'm 100% in on that.

With respect to with with with with respect to to Taiwan, we have to do three things.

One, we have to make sure that we re-industrialize the United States as fast as we can. >> Yeah. >> And whether it's the chip manufacturing plants, the the computer manufacturing plants, or the AI factories, >> on that? >> We're doing excellent.

With by by gaining the strategic support, by gaining the friendship of the supply chain of Taiwan.

By gaining their friendship, by gaining their support, we were able to build Arizona and Texas, California at incredible rates.

They're They are genuinely a strategic partner.

Uh we we we really they deserve our support, they deserve our friendship, they deserve our generosity.

And they're doing everything they can to accelerate the manufacturing process for us.

And so so I think that's number one.

Number two, we ought to diversify the manufacturing supply chain.

And whether it's South Korea, whether it's it's Japan, it's Europe, we ought to we ought to diversify the supply chain, make it more resilient.

And number three, let's be let's let's demonstrate restraint.

And while we're reducing increasing our diversity and resilience, let's not press, push um you know >> unnecessarily >> So we need to be patient. >> It's thoughtful.

Is helium a problem?

A lot of reports out there. >> I I think helium could be a problem, but it's also the case that the supply chain probably has a lot of buffer in it.

Yeah.

These kind of things tend to have a lot of buffer.

Uh but but um you know. >> Yeah. >> You've um made massive progress in self-driving.

Made a big announcement.

You've added many more partners including BYD.

There was just a video of you driving around in a Mercedes.

And uh huge announcement uh with Uber that you're going to have a number of cars on the road from many different manufacturers.

Your bet is I believe that there's going to be an Android type open-source platform that you're going to play a major part in with dozens of uh car providers.

And then maybe on the other side there could be an iOS with Tesla or Waymo.

What's your strategy thinking there and how that chessboard emerges because it feels like you have a a pretty deep stack, and in some ways you're competing, and in other places you're collaborative. >> Yeah.

Um it's taking a step back, we believe that everything that moves will be autonomous completely or partly someday.

Number one.

Number two, we don't want to build self-driving cars, but we want to enable every car company in the world to build self-driving cars.

And so we built all three computers, the training computer, the simulation computer, the evaluation evaluation computer, as well as the car computer.

We develop the world's safest driving operating system.

Uh we also created the world's first reasoning autonomous vehicle so that it could decompose complicated scenarios into simpler scenarios that it knows how to navigate through, just like us, reasoning systems.

And so that reasoning system called Alpaca IO has enabled us to achieve incredible results.

We open this we we vertical optimization, we horizontally innovate, and we let everybody decide.

Do you want to buy one computer from us?

In the case of Elon and Tesla, they buy our training computers.

Um do they want to buy our training computer and our simulation computers?

Or do you want to let us uh work with us to do all three and even put the car computer in your car?

So we, you know, I our attitude is we want to solve the problem.

We're not the solution provider.

And we're delighted however you work with us. >> to build on this question because I think it's like it's so fascinating.

You actually do create this platform.

A thousand flowers are blooming.

But it's also true that some of those flowers want to now go back down in the stack and try to compete with you a little bit.

Google has TPU, Amazon has Inferentia and Trainium.

You know, everybody's sort of spinning up their own version of I think I can out-Nvidia Nvidia.

Even though they also tend to be huge customers.

How do you navigate that?

And what do you think happens over time and where do those things play in the complexion of this kind of video >> Yeah, really great.

You know, first of all, um we're the only AI company We're an AI company.

We build foundation models.

We're at the frontier of many different domains.

We build every single every single layer, every single stack.

Um we're the only AI company in the world that works with every AI company in the world.

They never show me what they're building, and I always show them exactly what I'm building. >> Right. >> Yeah.

And so so the confidence comes from this.

One, uh we are delighted to compete on what is the best technology.

And to the extent that to the extent that we can continue to run fast, I believe that buying from Nvidia still is one of the most economic things they could do.

And I see this incredible confidence there.

Number one, number two, we're the only architecture that could be in every cloud, and that gives us some fundamental advantages.

We're the only architecture you could take from a cloud and put into on prem, in the car, in any >> That's right, in space.

And so there's a whole whole part of our market, about 40% of our of our business, most people don't realize this, 40% of our business, unless you have the CUDA stack, unless you can build an entire AI factory, you have the customers don't know what to do with you.

They're not trying to build they're not trying to buy chips, they're trying to build AI infrastructure.

And so they want you to come in with a full stack, and we've got the whole stack.

And so surprisingly, Nvidia's gaining market share.

If you look at where we are today, we're gaining share. >> happens is these guys try and they realize, "Oh my god, it's too much." And then they come back.

Is that why their share grows? >> Well, we're gaining share for several reasons.

One, um our velocity has gone we help people realize it's not about building the chip, it's about building the system.

And that system's really hard to build.

Uh and and so their their their business with us is increasing.

In the case of AWS, I think they just announced, I think it was yesterday, that they're going to buy a a million chips uh in the next couple years.

I mean, that's a lot of chips from from AWS and that's on top of all the chips they've already bought.

And so we're delighted to do that.

But number one, we're gaining share this last couple years because we now have Anthropic coming to Nvidia.

Meta SL is coming to Nvidia.

And the growth of open models is incredible and that's all on Nvidia.

And so we're growing in share because of the number of models.

We're also growing in share because outs all of these companies are outside the cloud and they're growing regionally, in enterprise, in industries, at the edge.

And that entire segment of growth is, you know, really hard to do if it's just building an ASIC. >> Brad, related to that um and not to get in the weeds on the numbers, but analysts don't seem to believe, right?

So if you look at the consensus forecast, you said compute could 1 million X, right?

And yet they have you growing next year at 30%, the year after that at 20%, and in 2029, which is supposed to be a monster year, at 7%.

Right?

So if you just if you take your TAM and you apply their growth numbers, it suggests that your share will plummet.

Do you see anything in your future order book that would make that correct? >> Yeah, first of all, they they just don't understand the scale and the breadth of AI. >> Yes.

Yeah. >> I think that's true. >> Most people think that AI is in the top five hyperscalers. >> Right. >> That's right. >> There's also an orthodoxy around these law of large numbers where, you know, they have to go back to their investment banking risk committee and show some model.

They're not going to believe in their minds that 5 trillion goes to 15 trillion.

They're like it can go to it can go to it can go to seven. >> Or they need to have a 10 trillion-dollar company. >> It's all just CYA stuff that I think they're >> happened before, so you can't say it will. >> And and because because the you have to redefine what it is that you do.

There was somebody who made an observation recently that Nvidia Jensen how can you be larger than Intel in servers?

And the reason for that is because the CPU market of the entire data center was about 25 billion dollars a year. >> Right. >> We do 25 billion dollars a year, as you guys know, in a very in the time that we were sitting here.

And so obviously obviously that was a joke. >> No, it's but it's >> All in podcast >> No, that was not guidance.

But anyhow anyhow it the point is how big you can be depends on what is it that you make. >> Right. >> Nvidia is not making chips.

Number one, making chips does not help you solve the AI infrastructure problem anymore.

It's too complicated.

Number three, most people think that AI is narrowly in the things that they talk about and hear and see. >> Right. >> It's AI is much Open AI is incredible.

They're going to be enormous.

Anthropic is incredible.

They're going to be enormous.

But AI is going to be much much bigger than that. >> Yeah. >> And we address that segment. >> Tell us about data centers in space for a second. >> Yep. >> Um >> We're already in space. >> How should the layman think about what that business is versus when you hear about these big data center build-outs that's happening in in on the ground? >> Well, we should definitely work on the ground first because we're already here.

And number one, number two, we should prepare to be out in space and obviously there's a lot of energy in space.

Um the challenge of course is that cooling you can't take advantage of conduction and convection.

And so you can only use radiation.

And radiation requires very large surfaces.

And so now that's not an impossible thing to solve and there's a lot of a lot of space in space.

Um, but nonetheless the expense is still quite there is is there.

We're going to go explore it.

We're already there.

We're already radiation hardened.

We have we have Kuda in satellites around the world.

They're doing imaging, image processing, AI imaging.

And and that kind of stuff ought to be done in space instead of sending all the data back here and do imaging down here.

We ought to just do imaging out in space.

And so there's a lot of things that we ought to do in space.

In the meantime, we're going to explore what is the architecture of data centers look like in space.

And it'll take it'll take years.

It's okay.

I got plenty of time. >> I wanted to double click on health care.

I know you've got a big effort there.

We're all of a certain age where we're thinking about lifespan, health span.

I mean, we all look great, I think.

Some better than others.

I think some better than others.

I don't know what your secret is, Jensen. >> Pretty good these these >> I mean, what what are you taking?

What's off the menu?

You got to talk to me when we're backstage.

I want to know in the green room what you got going on. >> Squats and push-ups and sit-ups. >> Perfect.

Okay.

Um, but >> It works. >> what you know in terms of the build out in health care, where is that going?

And what kind of progress are we making?

I was just using Claude to do some analysis and saying like where are all these billing codes?

We spend twice as much money in the US.

We get seem to get half as much.

It seemed like uh, 15 to 25% of the dollars spent were on these first GP visits.

And I think we all know like chat GPT and a large language model does a better job more consistently today at a first visit.

So, what has to happen there to kind of break through all that regulation and have AI have a true impact on the health care system. >> There's several several areas that we're involved in in in health care.

One is AI physics.

And and that's or AI biology.

Using AI to understand, represent, predict biology behavior, biological behavior.

And so that's one, that's very important in drug discovery.

There's second, which is AI agents, and that's where the assistance in helping diagnosis and things like that.

Open evidence is a really good example.

Hippocratics is really good example.

Love working with those companies.

I really think that this is an area where agentic technology is going to revolutionize how we interact with doctors and how do we interact for health care.

The third part that we're involved in is physical AI.

The first one's AI physics, using AI to predict physics.

The second one is physical AI, AI that understand the properties of the laws of physics, and that's used for a robotic surgery.

Huge amounts of activities there.

Every single instrument, whether it's ultrasound or you know, CT or whatever instrument we interact with in a hospital in the future will be agentic. >> Yeah. >> You know, open claw in a safe version will be inside every single instrument.

And so in a lot of ways that instrument's going to be interacting with patients and nurses and doctors in a very unique way. >> so much investment in AI weapons.

It would be wonderful to see some investment in AI EMTs and paramedics and saving lives, not just taking them. >> Yeah. >> Which I think is a great segue into robotics.

You've got dozens of partners.

We had this very weird I I don't know what to call a lost decade or 20 years of Boston Dynamics, Google bought a bunch of companies, they then wound up selling them and spinning them out, where people just thought robotics is just not ready for prime time.

And now here we have the world's greatest entrepreneur at this time, uh tied with you.

Uh Musk doing Well, that was a good save, I hope.

Optimus, uh pretty impressive.

And then, other companies in China How how close is that to actually being in our lives where we might see a chef, a robotic chef, a robotic nurse, a robotic housekeeper, you know, these humanoid factor actually working in the real world?

Knowing what you know with those partners and the fidelity, especially in China where they seem to be doing as good a job as we're doing here, or maybe better? >> Um we invented the industry largely.

America invented We could You could argue we got into it too soon. >> Yeah. >> And and we got exhausted.

We got tired um about 5 years before the enabling technology appeared. >> brain. >> Yeah, yeah.

And we we just got tired of it just a little too soon.

Okay, that's number one.

But, it's here now.

Now, the question is how much longer from the point of high-functioning existence proof, high-functioning existence existence proof to reasonable products, technology never takes more than a couple two, three cycles.

And so, a couple two, three cycles would basically be somewhere around 3 years to 5 years.

That's it. 3 years to 5 years we're going to have robots all over the place.

Uh I think I think um uh China is is a formidable.

And the reason for that is because they're microelectronics, their um motors, their rare earth, their magnets, which is foundational to robotics, they are the world's best.

And so, in a lot of ways, our robotics industry relies deeply on their ecosystem and their supply chain.

Um and uh and and they're, you know, obviously moving very quickly.

Uh we're going to, you know, our robotics industry will have to rely a lot on it.

The world's robotics industry will have to rely on a lot of on it.

And so, so I think um uh you're going I want some fast fast movements here. >> Ultimately, one for one, Elon seems to think we're going to have one robot for every human, 7 billion for 7 billion, 8 billion for 8 billion. >> Well, I'm hoping more.

Yeah, I'm hoping more.

Yeah.

Uh well, first of all, there's a whole bunch of robots that are going to be in factories working around the clock.

There's going to be a whole bunch of factory robots that that don't move.

They move a little bit.

Uh almost everything will be robotic. >> What does the world look like? >> Sorry, let me say I think like this is one of the robotics for me is one of the pieces that I think unlocks uh economic mobility opportunities for every individual.

Everyone now, like when everyone got a car, they could now go and do a lot of different jobs.

When everyone gets a robot, their robot robot could do a lot of work for them.

They can stand up an Etsy store or a Shopify store.

They can create anything they want with their robot.

They could do things that they independently cannot do.

I think the robot is going to end up being the greatest unlock for prosperity for more people on Earth than we've ever seen with any technology before. >> Yeah, no doubt.

I mean, just the the simple math at the moment is we're millions of people short in labor today. >> Right. >> Yeah. >> Right.

We're we're we're actually really desperate in need of robotics.

And so that all of these companies could grow more if they had more labor.

I mean, we're we're no number one.

Some of the things that you mentioned are super fun.

I mean, because of robots, we'll have virtual presence.

Uh you know, I'll be able to go into the robot of my house and virtually operate it.

I'm on a business trip. >> Right. >> Tell it to walk around the house. >> And walk the dog. >> Yeah, walk the dog. >> Rake the leaves. >> Yeah, exactly. >> Rake up the dog. >> Maybe not quite that, but just, you know, just, you know, wander around and just see what's going on in the house, you know, chat with the dogs, chat with the kids.

Yeah. >> Yeah. >> That's an >> Time travel is also we're going to be able to travel at the speed of light, you know, and so, you know, clearly want to send our robots ahead of us. >> Yeah. >> Not going to send myself.

I'm going to send a robot. >> Right. >> You know. >> Check it out. >> Yeah, yeah.

And then I'm going to upload my AI. >> Well, it's inevitable.

It unlocks the moon and it unlocks Mars as targets for for colonization, which gives us infinite resources.

Getting back from the moon is effectively zero energy cost to move material back cuz you can use solar and accelerate.

So, you could have factories that make everything the world needs on the moon, and the robots are going to be the unlock for enabling that. >> This distance no longer matters. >> Distance doesn't matter. >> Yep. >> Yeah. >> The more the more revenue we get out of models and agents, the more we can invest in building the infrastructure, which then unlocks more capabilities on models and agents.

Dario on Dwarkesh's podcast recently said, "By 2027-28, we'll have hundreds of billions of dollars of revenue out of the model companies and the agent companies." And he forecasts a trillion dollars by 2030, right?

This is non-infrastructure AI revenue.

Um >> I think he I think he's he's being very conservative.

I believe Dario and Anthropic is going to do way better than that. >> Wow. >> Way better than that. >> Wow. >> Yeah, and then 30 billion to a trillion. >> Yep.

And not And And the reason for that is the one part that he hasn't considered is that I believe every single enterprise software company will also be a reseller, value-added reseller of Anthropic code, Anthropic's tokens, value-added reseller of OpenAI. >> That's right.

And they're going to that that that part of their >> Get this, logarithmic expansion. >> Yes. >> Yeah. >> Their go-to-market is going to expand tremendously >> you think What do you think in that world is the moat?

What's left over?

I mean, you have some moats that are frankly, I think, as this scales, almost insurmountable.

The best one that nobody talks about is probably CUDA, which is just like an incredible strategic advantage.

But in the future, if a model can be used to create something incredible, then the next spin of a model can be used to maybe disrupt it.

Sort of in your mind, what do you think for these companies that are building at that application layer?

What's their moat?

Like, how do they differentiate themselves? >> Deep specialization.

Deep specialization.

I believe that um these models that they're they're going to have general general models that are connected into the software company's agentic system.

Right.

Many of those models are cloud models and proprietary models, but many of those models are specialized sub-agents that they've trained on their own >> Right.

So, the call to arms for you for entrepreneurs is, look, know your vertical. >> That's right. >> Know it as deep and as better than everybody else. >> That's right. >> And then wait for these tools because they're catching up to you and now you can imbue it with your knowledge. >> That's right.

And the sooner you connect your agent, the sooner you connect your agent with customers, that flywheel is going to cause your agent to get >> It very very much is an inversion of what we do today because today we build a piece of software and we say, what generalizes?

And then let's try to sell it as broadly as possible and then sell the customization around it. >> And we trap In fact, in fact, with exactly right.

We we create a horizontal, but notice there are all these GSIs and all of these consultants who are specialists who then take your horizontal platform and specializes it into >> Exactly.

And that's arguably a five or six time bigger industry is the customization. >> It is.

Absolutely. >> Yeah, the whole That very much is. >> That's right.

So, I think that these platform companies have an opportunity to become that specialist, to become that vertical. >> Right. >> Yeah, domain expert. >> I just want to give you your flowers.

I think it was three years ago you said you're not going to lose your job to AI, you're going to lose your job to somebody using AI.

And here we are, the entire conversation has revolved around this concept of agents making people superhuman and the business opportunity expanding and entrepreneurship expanding.

You actually saw it pretty clearly.

Have you changed your view? >> Well, I I I got this is the the doomer doomer doomer doomer doomer I'm not a doomer. >> I DO HAVE NO, YOU CAN HOLD space for I think two ideas.

One is there are going to be >> That's spiral J Cal we call it. >> No, no.

There you can see >> Well, that's just because he doesn't hang out with me enough. >> Well, we I mean we talk a little bit. >> Be careful what you >> We don't talk about it. >> He will show up at your breakfast TABLE AND HE'LL FOLLOW YOU AROUND. >> I'M NOT asking for it.

I'm just saying. >> He'll follow you around. >> I'm not asking for it. >> You can come with me and Tucker we ski in Japan every January.

We love it. >> Me and Tucker >> road trip. >> Okay. >> There is going to be job displacement and then the question becomes you know, do those people have the fortitude, the resolve to then go embrace these, you know, technologies.

We're We're going to see 100% of driving go away by humans.

That's just It's a That's a beautiful thing and the lives saved, but we have to recognize that's 15 million people in the United States, 10 to 15 million who are employed in that way.

And And so that is going to happen, yes? >> I I think I think that jobs will change.

For example, um there are many chauffeurs today who drives the car.

I believe that though many of those chauffeurs will actually be in the car sitting behind the drive the steering wheel while the car is driving by itself.

And the reason for that is because remember what a chauffeur does.

In the end these chauffeurs they're helping you they're your assistants, they're helping you with your luggage, they're helping you I mean they're helping you with a lot of things.

And And so I would be surprised actually if the chauffeurs of the future become your mobility assistant and they are helping you do a whole bunch of other stuff.

Yeah, and the car's driving by itself. >> The autopilot in planes created a lot more pilots and didn't take any of the pilots out of the cockpit even though the autopilot is flying the plane 90% of the time. >> And by the way, while that car is driving itself, that chauffeur is going to be doing a bunch of other work on his phone and he's going to be making money doing other things. >> doing other stuff.

Coordinating a a of things for you, getting >> It's all the pie just grows in a way >> So one of the things that that that yes, every job will be will be transformed.

Um some jobs will be eliminated.

However, we also know that many many jobs will be will be created.

The one thing that I will say to young people who are coming out of school, who are concerned who are anxious about AI, be the expert of using AI. >> Yes. >> How much Look, we all want our employees to be expert at using AI, and it's not not trivial.

Not trivial.

And so, knowing how to specify, not to over prescribe, leaving enough room for the AI to innovate and create while we guide it to the outcome we want, it All of that requires artistry. >> You had this great advice to when you were at Stanford, I think it was, which is, "I wish to you pain and suffering." Do you remember that? >> Yeah. >> Fantastic.

What's your advice to young people around what they should be studying?

So, if they're sort of about to leave high school.

Because now those are the kids that are at this like really native They haven't made a decision about college, what to study, if at all go to college.

How do you guide those kids?

What would you tell them? >> I I still believe that deep science, deep math, language skills, you know, as you know, language is the programming language of AI now. >> programming language. >> And so, as it turns out, it could be that the English major could be the most successful.

And and so, so I think I I would just advise whatever whatever education you get, just make sure that you're deeply deeply expert in using AIs.

One of the things that I wanted to say with respect to jobs, and I want everybody to hear it, that in fact, at the beginning of the deep learning revolution, one of the the finest computer scientists in the world deeply deeply I deeply respect but that computer vision will completely eliminate radiologists.

And and that the one at the one field he advises everybody to not go into is radiology. 10 years later his prediction was at 100% right.

Computer vision has been integrated into all of the radiology technologies and radiology platforms in the world 100%.

The surprising outcome is the number of radiologists actually went up and the demand for radiologists is skyrocketing.

The reason for that is because everybody's job has a purpose and it's task.

The task that you do is studying the scans.

But your purpose is to diag- helping the doctors helping the patient diagnose disease.

And so what's surprising is because the scans are now being done so quickly they could do more scans improving health care. >> Yes. >> But doing more scans more quickly allows patients to be onboarded a lot more quick treated a lot more quickly and as it turns out because hospitals enjoy making money too >> Yeah. >> Right. >> They're doing more scans. >> Reading more >> They're treating more customers and more and more patients.

The revenue is going up and guess what?

They need more >> And in a in a a country that grows faster productivity increases a wealthier country can put more teachers in the classroom not less teachers in the classroom.

You just give every one of those teachers a personalized curriculum for every student in the room.

It makes them all bionic and leads to a lot more. >> Every single student will be assisted by AI but every single student will need great teachers. >> Yeah. >> Amazing.

Uh Jensen, congratulations on all your success and really this is an incredibly positive uplifting discussion.

We really appreciate you taking the time for us. >> He is the steward we need. >> You are the steward we need. >> I think you need to be more vocal about I'm I'm being very very vocal about the positive side of it.

I think there's too much doomerism. >> But I also think it takes the humility to have this level of success and be humble about we're making software, guys.

Yeah.

And I think that that's actually really healthy for people to hear.

We have done this before.

We have invented categories and industries before.

We don't need to go to this scaremongering place.

It does nothing. >> And we get to choose, right?

We have autonomy and and agency.

We get to pick how to >> We sure do. >> deploy this.

Okay, everybody.

We'll see you next time on the All-In interview.

Okay.

Well done, brother. >> Thanks, man. >> Good job. >> Thank you, sir.

That was awesome. >> Good.

Good. >> You guys are awesome. >> Jason, thank you. >> Look at this.

Look at this big crowd behind you guys. >> Man, I think they're here for you. >> I'm going all in.
