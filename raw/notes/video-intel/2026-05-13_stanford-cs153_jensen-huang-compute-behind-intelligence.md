# Stanford CS153 Frontier Systems — Jensen Huang on the Compute Behind Intelligence

**Channel:** Stanford Online (@stanfordonline; CS153 Frontier Systems, hosted by the course lead "at AI Coachella") · **Guest:** Jensen Huang (CEO, NVIDIA) · **Upload:** 2026-05-13 · **Duration:** 1:08:24 · **Views:** 132,388 · **Likes:** 3,580
**URL:** https://youtu.be/tsQB0n0YV3k

## Source-tier verdict (read first)

**Tier 3, aligned commercial incentive — but a *technical/first-principles* talk, higher analytical value than a typical promo.** NVDA's CEO at a Stanford systems course, reasoning from architecture fundamentals. Every demand/energy/share claim still serves NVDA's book (he sells the compute), so discount the magnitudes — but the *framework* (co-design, tokens-per-watt, the Hopper→Blackwell→Vera-Rubin→Feynman logic, why low MFU is intentional) is genuinely informative. Treat as CEO commentary; verify specifics against filings. Never cite as vault fact.

## TL;DR

- **The energy thesis, stated maximally:** *"the amount of energy we need for compute is likely ~**1,000× more than we currently have**… I wouldn't be surprised if we're off by a couple orders of magnitude."* NVDA's first lever is efficiency — **tokens-per-watt improved 50×** (Grace Blackwell NVLink72 vs prior gen). Strong (incentive-laden) confirmation of the vault's power-as-binding-constraint demand side.
- **Architecture roadmap as a bottleneck-chase:** Hopper (pre-training) → **Grace Blackwell NVLink72** (first rack-scale computer, for inference/decode = memory-bandwidth-bound, **50× in 2 years**) → **Vera Rubin** (for *agents*; storage-on-fabric for long memory + a **Vera CPU built for low-latency single-threaded tool-calls**) → **Feynman** (for *swarms* of agents/sub-agents).
- **NVDA seeds open foundation models to "activate" whole industries:** Nemotron (language), BioNeMo (biology), **Alpamayo (autonomous vehicles)**, **GR00T (humanoid / general robotics)**, climate. The robotics + AV "brains" are NVDA software.
- **On the utilization/"bubble" debate:** the xAI Memphis "11% MFU" memo → Jensen says **low MFU is *intentional overprovisioning*** (you provision for spiky peaks to beat Amdahl's law); *"flops are cheap; H100s going up on bandwidth/architecture, not flops."* Nuances the under-utilization-as-bubble worry.
- **Export controls:** strongly against — NVDA "conceded 2/3 of the world market"; GPUs are general-purpose ("not atomic bombs"); **the telecom cautionary tale** — *"America has no telecommunications fundamental technology anymore… it was all policied out of our country."*

## Named entities

| Entity | Claim | Vault page |
|---|---|---|
| **[[NVDA]]** | Co-design → 1,000,000× in 10 yrs (vs Moore 100×); roadmap Hopper→Blackwell→Vera Rubin→Feynman; tokens/watt 50×; seeds open foundation models | ✓ (CEO, his book) |
| **[[AMD]]** | Jensen "was already working at AMD" while at Stanford (designed microprocessors); "Amdahl's law" pun | ✓ |
| **[[GEV]]** / grid / power | "~1000× energy"; "best time ever to invest in sustainable energy — market forces, no subsidy needed"; "upgrade our archaic grid" | ✓ (energy thesis) |
| **[[humanoid-robot-value-chain]]** | **GR00T** = NVDA humanoid/general-robotics foundation model (the robotics "brain" software layer) | ✓ (theme) |
| xAI | Memphis cluster "11% MFU" memo (~11B unutilized flops) — used to discuss overprovisioning | no (private) |
| Anthropic / OpenAI | NVDA "uses more Anthropic & OpenAI tokens than almost anybody"; 100% of engineers agentically supported | no (private) |
| Qualcomm | The 3G→4G modem leader that "locked NVDA out" of mobile (Jensen's strategic-mistake story) | no |
| Alpamayo / Nemotron / BioNeMo | NVDA open foundation models (AV / language / biology); Nemotron Nano for cybersecurity swarms | n/a (NVDA products) |
| Hopper / Grace Blackwell NVLink72 / Vera Rubin / Feynman | NVDA architecture generations | n/a (NVDA products) |

*Auto-caption garbles:* "Alpamo / Elpio / Alamayo / Alpha Mayo" → **Alpamayo** (NVDA AV model); "Groot" → **GR00T**; "Fineman / Flyman / Fman" → **Feynman** (next NVDA architecture); "Neotron / Neimotron / Neatron" → **Nemotron**; "AMD doll's law / AMD's law" → **Amdahl's law**; "dinard/dinar scaling" → **Dennard scaling**; "me and Conway" → **Mead & Conway** (VLSI textbook); "delivering soy sauce" → likely **"delivering [content]"** garble.

## Key claims (by topic; no chapter markers — segmented)

**Compute scaling + energy (early–mid)**
- Co-design (CPU+GPU+networking+switches+storage optimized together) → **1,000,000× over 10 years** vs Moore's law ~100× (Dennard scaling ended ~a decade ago). `[opinion/verifiable-ish]`
- **Energy for compute ~1,000× current, possibly "a couple orders of magnitude" more.** First lever = efficiency: **tokens/watt +50×** (Grace Blackwell). `[forward]`
- **Sustainable energy "best time ever to invest" — market-driven now, "back in old days you needed government subsidies to build solar farms and nuclear plants, now the market will pay you."** *"Best chance to upgrade our archaic grid."* `[opinion]`

**Photonics / interconnect (mid)**
- Host: *"a year ago photonics became a huge solution… copper wires literally are one of the transmission bottlenecks."* Jensen pivots to energy efficiency / tokens-per-watt. Decode is bound by **aggregate NVLink72 bandwidth**, not flops. `[opinion]`

**Architecture roadmap (mid–late)**
- **Hopper** = pre-training ("built a multi-billion-$ system for a market of precisely zero" — first-principles bet; prior record was a $350M supercomputer). **Grace Blackwell NVLink72** = first rack-scale computer, for inference/decode (memory-bandwidth bound), 50× in 2 yrs. **Vera Rubin** = for agents (long memory in storage-on-fabric; **Vera CPU for low-latency single-threaded tool-calls**). **Feynman** = for agent swarms. `[forward]`

**Open models / robotics / cyber (mid)**
- NVDA seeds open foundation models — **Nemotron** (language; near-frontier), **BioNeMo**, **Alpamayo** (AV — "few million miles not billions" via human priors), **GR00T** (humanoid/general robotics), climate — to "activate the whole industry downstream." **Nemotron Nano** → cybersecurity "swarms of cheap AIs." `[forward]`

**Utilization / demand (mid)**
- xAI Memphis "**11% MFU**" memo. Jensen: **low MFU is desirable** — overprovision flops/bandwidth/memory/network for spiky peak loads (beat Amdahl's law). *"Flops are cheap; H100s going up on bandwidth/architecture, not flops."* Metric should be **tokens-per-watt, not flops/MFU.** `[opinion]`

**China / export controls (late)**
- Against export controls: NVDA "conceded 2/3 of the world"; GPUs general-purpose (medical imaging, gaming — "not atomic bombs"); *"there's plenty of chips… not true that people place orders and we don't deliver."* **Telecom cautionary tale:** America lost telecom "fundamental technology" to policy. `[opinion]`
- Stanford-compute aside: the real constraint isn't NVDA supply, it's that universities lack billion-$ centralized-compute budgets (suggested using the ~$40B endowment to fund campus AI supercompute). `[opinion]`

## Vault cross-reference

- **Power/energy thesis (`_thesis.md`) + [[GEV]] + [[transformer-supply]] — CONFIRMS (demand side), with a nuclear-thread twist.** The **~1,000× energy** claim + tokens/watt-50× + "upgrade the archaic grid" is the strongest possible (incentive-laden) statement of the vault's power-as-binding-constraint. **Nuclear twist:** his *"market will pay you to build solar/nuclear, no subsidy needed"* line **softly challenges the vault's "nuclear = policy-contingent" finding** — but it's an optimistic throwaway that *contradicts the deployment-reality evidence* (NuScale cancelled on economics; SMRs aren't yet market-economic). Flag as a mild tension, not a refutation.
- **Photonics ([[CPO-platform-battle]] / [[datacenter-laser-supply]] / copper-vs-optics) — CONFIRMS.** "Photonics became a huge solution; copper is a transmission bottleneck" — supports the photonics chokepoint + Baker's copper-displacement/ALAB-switch point.
- **[[AI-agentic-CPU-orchestration-reemergence]] + [[NVDA]] — CONFIRMS + adds.** **Vera CPU built specifically for low-latency single-threaded agentic tool-calls** is direct support for the agentic-CPU re-emergence theme (CPUs matter again for orchestration). The Hopper→Blackwell→Vera-Rubin→Feynman bottleneck-chase is a clean NVDA roadmap datapoint.
- **[[humanoid-robot-value-chain]] — adds (the AI-brain layer).** NVDA **GR00T** = the humanoid/general-robotics *foundation model* — NVDA positioning as the robotics "brain"/software enabler. Complements the vault's mechanical-chokepoint focus (magnets/reducers/actuators) with the AI-software layer of the same value chain.
- **AI-demand-durability / [[AI-buildout-who-holds-the-risk]] — adds + tension with Baker.** The **low-MFU-is-intentional** framing pushes back on "underutilized compute = bubble." Note the *tension between two infra bulls*: Baker said "every GPU at 100% utilization (vs 99% dark fiber)" as the anti-bubble point; Jensen says low MFU is *fine/intentional* overprovisioning. Both bullish, opposite utilization framings — useful to triangulate.
- **China / de-globalization + [[NVDA]] — adds.** Export-control pushback + the **telecom cautionary tale** (America lost telecom to policy) — the same analogy Baker used, and it ties to NVDA's "2/3 of the world conceded" China-revenue lead from the All-In note.
- **Off-thesis color:** the "pain and suffering" career advice, Denny's nostalgia, the Stanford-endowment riff.

## Ingest leads (primary-source-verifiable)

1. **NVDA Vera Rubin + Vera CPU (agentic tool-call latency) + Feynman roadmap** → verify against [[NVDA]] roadmap/GTC disclosures; sharpens the agentic-CPU theme.
2. **Tokens-per-watt 50× (Grace Blackwell NVLink72)** → verify NVDA technical claims.
3. **NVDA China "2/3 of the world conceded" / export-license status** → cross-check with the All-In note's China-license lead + [[NVDA]] filings (material to China revenue).
4. **GR00T humanoid foundation model** → context for the humanoid AI-brain layer (NVDA software, not a chokepoint MP-style; Tier-3 framing).
5. **NVDA "uses more Anthropic/OpenAI tokens than anybody; 100% engineers agentic"** → adoption signal (consistent with the All-In $250k-tokens-per-engineer claim).

## Contradictions / red flags

- **Aligned incentive.** The 1,000×-energy and "low-MFU-is-fine / overprovision everything" framings both *increase NVDA chip demand* — self-serving. Discount magnitudes.
- **"Market pays for nuclear/solar now, no subsidy"** contradicts the deployment-reality evidence this session surfaced (NuScale cancelled on economics; SMRs not yet market-economic; HALEU/enrichment is government-funded). Optimistic overstatement.
- **Export-control advocacy** is NVDA's commercial interest in China sales — present the telecom analogy as argument, not settled fact.
- **Utilization framing conflicts with Baker** — note both, don't adopt either as fact.

## Source-tier verdict (restated)

**Tier 3 / aligned incentive, first-principles technical talk** — do not cite as vault fact; CEO commentary, verify against filings. Discovery-only: nothing in the vault was touched.

---

## Transcript (Tier 3 — not a primary source)

[Full cleaned auto-caption transcript of the 1:08:24 lecture follows. No chapter markers; auto-captions — treat names/numbers as approximate (see garble flags: Alpamayo, GR00T, Feynman, Nemotron, Amdahl's law, Dennard scaling, Mead & Conway).]


---

### Full cleaned transcript

I would like to welcome back Preacher Huang.

We have been now in a locked in a global race way faster than NASCAR racing and it's partly your fault.

Jensen's been the preacher that's given us all the power we need, all the energy, and some more to have what I think has been the craziest 12 months of my life, certainly for many of you.

And we're just getting started. um the energy with which you approach every single thing you do including the class last year and then all every time I've had the chance to hang out with you, you've given so much time to the students, the founders.

Thank you. >> Should we jump right in? >> Yeah, let's go. >> All right, we're going to rapid fire.

What is code design and why is it so important? >> Uh I I'll answer that in a second. >> Yes, please.

Um but but uh this is a great time to be in computer science and obviously the reason is because computing is being reinvented for the first time as dramatically as as it is for the first time really in about 60 plus years. uh the computer that we know of that you all use and our computing model, our mental model of a computer, the architecture of a computer, how you write the program, run the program, how you think about even taking computers to market, what it's used for.

For 64 years, it has been largely the same since the IBM system 360.

In fact, my first architecture book for learning about computer architecture was the system 360's manual.

And so so a lot has changed um as we went from PCs to internet and mobile and cloud and all those things.

But the fact of the matter is the computing model the fundamental part of computer science has largely remained the same until now.

You know for the first time uh the way you write the software how you process the neuronet network versus the software and what the applications can do has now tra dramatically changed.

Everything is fundamentally different.

At the highest level, you know, one simple way to think about it is is um uh computing as we knew it before was largely pre-recorded.

It's content that we've we pre-recorded, images, videos, you know, software that we largely pre-recorded, but now everything is generated.

And the nice thing about generating everything in real time is that it could be contextually consistent con contextually relevant to what what it is that you're dealing with.

And of course um it can respond uh to your intention not just explicitly uh to the things that you instruct and and so so the computer the computer is is um uh fundamentally different in that way.

Now the question is what does that mean at every single layer of the stack from from uh how the computer how the software is now developed the methodology of it how you organize your company to be able to develop software of today completely changed and so the methodology the tools we use uh the approach that we think about software coding uh completely changed uh how we run the software neuronet network versus compiled binaries um very very different And so what does that mean to the computer system, the network, the storage?

Um what does that mean to the software stack and the cloud services that sit on top of that?

And of course, you know, everything about the applications, what did it open up?

And uh somebody just uh somebody just came and said this piece of software we just opened up called Alpamo.

And I've been working on self-driving cars now for about 13 years. and and um I and the and the and the days of robo taxis are going to be literally everywhere. you know, everything that moves will be robotic.

And and that's an example of an application that that uh we wouldn't consider doing until deep learning and artificial intelligence came along.

That was such a big unlock u that you know I said hey aha uh this all of these problems that we wanted to solve in the past that we needed computer vision for uh really really uh are now fundamentally unlocked.

And so so it's how you think about every single stage of that.

What is you know what is a software engineer?

How do you organize the company?

Uh what is a computer for the age of AI?

How do you architect that?

All the way to what you can use it for and therefore uh therefore um where you would deploy it.

Um all of that has fundamentally changed and and uh for me the journey really started about 15 years ago and uh uh I had the benefit of of seeing some early works in in the area and uh as all Stanford students do uh you break the problem down you reason about it from first principles and you come to the conclusion literally everything has changed and so here you are you know computer scientist students uh this is really the first generation of AI becoming uh useful and um where we a couple years ago was in the generative part of AI and and as you guys know generative AI not only made it made it cool for us to do image generation and text summarization and translation and whatnot but generative generative AI also enabled us to think and so when I saw generative AI uh you know when what other people saw was that it was able to generate images and I and I surely would appreciated that as well.

Uh but the fact that you can generate thoughts it in the form of images but you can generate thoughts uh you can also reason with it and the ability for AI to think after GPT uh was was very very obvious.

Now the question is is uh how would you train how would you fine-tune an AI uh to be able to reason step by step by step and how would you teach it how to do so at at fairly large scale in a kind of semi-supervised way and so those are kind of the engineering problems you had to solve uh but the moment you see GPT you say aha uh thinking is just around the corner and thinking is generating tokens that you consume internally and uh generating tokens that you consume externally uh would be called tool full use.

And so the idea that that after GPT happened two years ago that we would be at this moment was fairly easy to predict.

Now of course an an you know unbelievable amount of technology was invented and a lot of amazing people did amazing work but you could almost see that moment here.

And so here we are you now have agentic systems and so now the question is is what's next?

And what happens in a world where a computer is not uh not responsive to what you ask it to do?

It's not it's not bought on demand.

You know, today's computing is really ondemand computing.

The word on demand was actually gen created in in our generation to talk about how you think about using computers.

Uh timesharing computers that you would use on demand became cloud computers.

And cloud computing of course is on demand but uh in your new world of agentic system uh these the computers are now continuously running.

And so what happens in a world where the computers are continuously running uh what happens to cloud services?

What happened to your personal computer?

What happens to you know all of these differenti systems?

Now there's a great great opportunity again to rethink all of that.

And so so what I you know is kind of my my my introduction to everything about um computer science has changed and and everything about every field of science has changed because of the things that we've changed and and so this good time to go to school. >> Okay, >> that's it.

What was your question? >> You know what?

I'm just going to turn it over to the kids. >> Codeesign code.

Code. >> Let's just go into the the students have questions.

They've all been asking questions in Discord.

Are they all voting on each other? >> Codeesign is really interesting, but it's not it.

Codeesign is super interesting and and basically codeesign says said back in the old days we abstracted computing so that so that um uh the people who designed microprocessors designed microprocessors.

People who uh worked on compilers worked on compilers and people who worked on languages worked on languages and so on so forth.

You guys know that and we actually had different fields.

Um but the problem and in fact this happened at Stanford uh what's the what's the beauty of risk?

What was the beauty of the work that John Hennessy did?

Um it it the beauty of it is that you got to think about compilers and microprocessor architectures harmoniously co-designed because otherwise you could end up creating a microprocessor that's super super tight and you know everything is is maximally optimized but unfortunately it's hard to compile.

It's difficult.

It's not compilable.

And so they created a a simpler instruction set that exposed simplicity to compilers so that compilers could do a better job generating code.

And it turns out a simpler machine co-designed with a compiler creates better performance than two systems that were optimized individually.

That's you know that's very Stanford.

Okay.

And this is this is part of your heritage as all of your in and John Hennessy's you know trail of amazing work that's left behind.

And so you take you take that and you think about well what happens in in the post world of general purpose computing.

Why is it that every problem in in computer science would be solvable by a general purpose instrument?

At some level you know you could say well if you had a general purpose instrument you prefer that.

However, there are some extreme problems whether it's computer graphics back in the old days or molecular dynamics or quantum chemistry or you know you know fluid dynamics and large multiscale mess scale multi-ysics problems or deep learning.

These problems are so computationally intense.

Why would you use a general purpose computer to go do that?

And so there the big insight is what if you understood the algorithms, understood the computer systems, understood the you know if you will the compilers, the frameworks and understood the architecture of chips and you were optimizing all of it at the same time.

And so the the facts here are the facts.

This is what happens when you do it what I just described.

Nvidia is probably the first computer systems company that's extreme code design.

We we literally co-design across all of that and including CPUs, GPUs, networking and switches and everything and storage.

And so the question is what do you get?

Well, Moore's law back in the old days, you guys all know about that.

Moore's law was about uh 2x every 18 months.

So call it 10x every 5 years.

Okay?

So 10x every 5 years is 100x every 10 years.

And that's that was in the good old days of Moore's law.

And for all the computer computer scientists in the room, you know, you know that Moors law was underpinned by a concept called dinard scaling and dinar scaling ran out of steam um several years ago probably about a decade ago in fact and we we kept squeezing it.

We kept squeezing it.

But over the course of last 10 years, if you just allowed microprocessors to continue to scale and you just don't touch the software and just benefited from the speed up of semiconductors and microprocessor design, you at best case you would have gotten 100x but probably because Dinard scaling slowed down and Moore's law largely ended, you know, you probably got something along the lines of 10x over the course of 10 years.

Well, in the case of NVIDIA and code design, we got 1 millionx over 10 years. 1 millionx.

And so somewhere between 100,000x and a millionx.

Okay.

So there when you're talking about numbers that big, it really doesn't matter.

And so a millionx over 10 years, it got we we were able to get scaling and computation scale so large so fast that AI researchers say, why don't we just take all of the internet?

Why even worry about what data to go curate and what what data to create?

Let's just take all of the world's data and just give it to the computer.

And that's really the big breakthrough when you're able to to to do something so insanely fast.

You know, for example, if you were able to travel at the speed of light, uh where we choose to live is doesn't matter. uh if you were able to go from New York to California in 10 minutes uh you know our freedom everything about society would change right and so if you were able to do computing a million times faster everything about computing computing changed and that's really the big breakthrough because of codeesign because of the way Nvidia approached it we accelerated computing by so so far that it created all this infinite abundance opportunity for everybody to to think about the future and so anyways here we Cool.

I have a bunch of follow-up questions, but I'm not going to ask. >> That one word led to that. >> GPT 10.

That's what it's like to work on a video.

You give me one word and you get ranted at for about half an hour >> because I got too much to share with you. >> The question is, how should education evolve in response to the industry?

Is it changing? >> Yeah.

And that's a really excellent question and and I think the answer clearly is uh AI should be part of your curriculum not just in learning about AI but using AI for the curriculum.

The the problem with with textbooks as you know it takes an enormous amount of effort to do and when I was taking classes at Stanford Professor Hennessy was still writing his textbook.

It was all handwritten out and and each week it seemed like he was writing a chapter.

I don't even know how he writes a chapter a week, but every week he was writing about a chapter and and then over time all of those notes turned into a textbook into the first edition.

And that must have taken several years.

And so I I think I think um it's not it's not possible for universities for, you know, pre-recorded textbooks to keep up with information and knowledge that's being generated in real time by AI.

And so I think the future probably has to be some union of the two.

And and I I don't know about you guys, but I can't learn anymore without AI.

And so not only do I have the AI read the papers, um, but I also have once it reads the papers, I might ask it to go read, you know, a whole bunch of the other papers that are associated with it.

And then now it becomes a super researcher.

And then I can I can first I ask it to summarize. um I ask you some basic questions and then after that you interact with that paper as if it's a researcher that's dedicated to you and so most people don't realize that you know I think a lot of people still think that you you summarize a document but in the process of summarizing the document that AI learned a lot and so and I I um I think that in the future I I do hope that that curriculums are are tightly integrated.

Um I I will say in defense of the textbooks though I will say that the first principles don't change you know in the final analysis uh uh me and Conway is still as solid of of fundamental methodology as as before it it is true that the scaling process that led to um constant constant current density um constant uh power density all of that all of those design optimizations associated with modern semiconductors design, you know, the the we've we've kind of exhausted all of that.

None of that is ISO anything anymore.

And so um but it's still good to know where we came from you know and so I I would still encourage that to appreciate the first principles and and you know while while I was going to to Stanford I was al already working at AMD and um and I was designing microprocessors at the time and it was still it was still really good to to see simultaneously um how how we design things in practice versus uh the first principal methods associated with learning about eventually uh how to design these things and and um I I I really enjoyed having you know feet on both sides of it and I I ended up learning a lot more and so what that means is when you're using AI which is real world it's contextually relevant now um it's it's contemporary and meanwhile you have first principle knowledge that you're learning at the same time you're kind of getting the same thing that I experienced >> the question is what are your thoughts on open source how do we how does open source stay at the frontier >> yeah there's really the question of closed source versus closed proprietary software versus open source.

There's a question of my intentions with open source.

And so I'll start with my intentions of open source.

Um first of all, Nvidia uses more anthropic and open AI tokens than just about anybody, right?

And and the reason for that is obviously we do a lot of coding.

We do a lot of design and 100% of our engineers are now agent agentically supported.

And so so I want them to be working with agents using the latest generation tools and re and remod modernize how Nvidia does work altogether.

Okay.

So number one if you can use uh open AI and anthropic I would highly recommend you use it and the reason for that is because it's useful.

It works really well.

It's getting better all the time and it's you know as a as you know large language models is the technology inside but cloud is a product and cloud code is a whole harness around it and that harness is getting better all the time the model is getting better all the time it's not it's not likely that anybody open source go to GitHub download something it's going to work nearly as well okay so so I I highly recommend and we do um use offtheshelf frontier AI models the question is why is it there that we're advancing ing and working so hard on open on on open models.

The reason for that is because language models are very important because they represent the the cotification of our intelligence and and um we want to automate ourselves especially is a very important part but you you you need to know that know that AI is about learning the representation the meaning the structure of information and so the question is where is information well we're living in information right now as we speak the reason why there's structure is the reason why every day you show up it's kind of largely the same otherwise be like practically white noise.

And so the fact that biological systems and physical systems have structure and from that structure I must be able to learn higher level representation.

And if I can learn the representation, then I could manipulate it.

Then I can Does that make sense?

And so just because I can learn the representation of of language, I can then generate it.

I can manipulate it, you know, I could put it to use.

And so I want to do the same thing for chemicals and and proteins and genes and uh physics and physical systems, robotics for example.

And so notice the way you represent all of those things are fundamentally different because the structure is different and the dimensionality is different.

How you train it is fundamentally different, right?

Because you don't have a whole bunch of internet corpus of human language on it.

So you you got to come up with new new strategies for all of that stuff.

And so we decided that we would dedicate ourselves in some fundamental pillars of and because we have the company the company has the talent and the scale we have the ability to put the first piece of artifact out in the world data model how to train it in several different domains.

And so some of the domains I care very much about uh one of them is called of course Neotron's language and I'll come back to that in a second. why it is that we're doing it.

And then second is Bioneo, that's for biology.

And uh um we have Alpamo, somebody mentioned it earlier for autonomous vehicles.

Uh basically artificial intelligence uh navigation and then and then um uh we have Groot, which is uh humanoid articulation, robotics, general artificial general robotics uh and and and then we have climate science, you know, basically messoscale multifysics.

Okay.

And so all of these different area these different domains uh we decided that that we should go and pioneer it.

And the reason for that is because otherwise the scientists in these different domains they simply won't have the scale and the technology necessary to go build that foundation model.

And so we decided that we would do that.

Okay.

So that and and as a result of doing that we activated healthcare, we activated life sciences.

We act we're working with every single self-driving car company in the world.

Doesn't matter which one it is. you know there's Nvidia in there somewhere and so we're we we enabled that entire ecosystem to really flourish and and we're working with robotics right now and you know so on so forth okay without us making that first effort and building a foundation model it's hard to activate the whole industry downstream and so it's about really about expanding AI and and democratizing this capability the the reason why we do language models is because two reasons one there are too many too many societ societies where the scale of their language is not big enough for somebody else to decide to make it a high priority.

They'll understand Sweden, Swedish, but making Swedish a top priority is not not not likely because the country is is big but not so big.

Uh Chinese of course well taken care of. uh Indian certain dialects very well taken care of but as you know you have like 230 others and so there are too many others unless you deeply care it's never going to be great and human intelligence no matter the size of your population uh you somebody should care and so we created a large language model that's near frontier neatron is close to frontier and we we make everything available so that if somebody wants to then fine-tune it into whatever language of their choice they got no trouble doing that.

Okay.

And so and then the second reason is very important is because we want to also take these language models and fuse it with the domain specific models because of human priors.

So for example, Elpio is a language model fused with a uh world model.

And so on the one hand it's really designed to detect cars and roads and things like that.

But on the other hand, we also believe that if the AI model, if Alamayo, the self-driving car model can reason, reason like a human and it could reason with human priors, then uh the number the amount of experiences it needs to have before it could be an extremely good and safe driving car is dramatically reduced. the amount of training data is reduced and we've proven that Alpha Mayo is probably one of the most effective self-driving car systems in the world and it's really only experienced you know a few million miles not billions of miles and so that kind of tell the system actually works okay so anyways I just gave you a long-winded answer for I broke it all down you can't just ask a >> simple question >> what we talked about >> but open models is really important and then and one one more thing okay if there's not that wasn't enough one more Okay, if you want if you care to have AI be safe and secure, it has to be open.

And the reason for that is you can't defend against a black box and you can't secure a black box.

And you can't put a black box of some cap incredible capability into your system with it completely completely opaque.

Now, of course, there's a lot of different ways you could solve the opaqueness.

For example, you could say before it do does anything, you have to reason about it to me step by step. before you do anything at all, you have to come up with a plan.

You have to reason about it step by step, but you could always lie.

And so, so the ability for the the the nice thing about transparent systems is that then, you know, we everybody gets to interrogate it.

Uh if you have a transparent system, then researchers get to use it.

If you have a transparent system, open system, then the way you defend against super agentic systems in the future for cyber security is obviously not to go into a battle of who gets the better one.

You know, you come up with some model, a model 7.0, and the only way I combat against that, I'm completely vulnerable until I come back with a 8.0, and then you got to come back with a 9.0 and just go back back and forth driving each other nuts.

And obviously, that's not that that's obviously not the smartest way to do it.

The smartest way to do it is you're going to you're going to create these incredible cyber security systems and or you're going to these cyber security threats.

And what we're going to do is we're going to have millions, billions, swarms of cheap AIs and we're going to systematically surround it.

And so it's kind of, you know, if you will, a giant dome.

So, for example, Neimotron Nano is being used for cyber security.

And so all these cyber security firms take Neo Neatron Nano because it's so fast and so so cost-effective, you can train it to detect cyber cyber attacks and then just deploy trillions of them.

Yeah.

Um on on the topic of open scaling, you know, we hung out in January and we >> I feel like you know that one scene in Thor, do you remember he was just hanging and he kept rotating in that direction? >> It's zero gravity here at AI Coachella.

We got no gravity Thor Ragnarok.

Do you guys remember that? >> We can move a little bit back so you can hear this.

Okay. >> You guys don't watch movies. >> Well, we had a whiteboard too if you want to get off and walk.

But um so in in January we met we talked about this topic open scaling.

We talk about bottlenecks.

We talked about um data as one bottleneck, comput as another bottleneck.

Um you know there's at least one experiment that uh we announced at GTC together which was the coalition scaling idea.

The second is on how to improve utilization on compute which is increasingly scarce.

Uh it came out last week that there was a memo at XI that said their uh Memphis cluster pool is running at 11% MFU utilization which I think like corresponds to something like 11 billion or something of unutilized MFU flops.

How can the open space well like maybe you could talk a little bit about why coalition scaling is an experiment we're trying and we have Ryan coming actually in the final office hours to talk about progress and then how do we get utilization to be better for open the open ecosystem when you don't have full like sort of fully integrated companies that can optimize up and down the stack. >> Yeah.

Um did you do you guys know know what M MFU is?

And so FU you guys know you guys don't use that anymore.

So, MFU is just simply wrong.

Okay, it's a it's the the amount of of uh the percentage of of uh flops basically uh that you consume while doing your work.

All right. >> Model flops utilization. >> Yeah.

And so, so it it's unfortunately with every metrics uh depending on what you measure, you could be measuring the wrong thing.

And so, let me tell you why.

Uh if you ask me do I want to be at at um high MFU personally or low MFU, I would like to be at low MFU all the time.

And the reason for that is because I want to be so smart I'm overprovisioned for it to work. >> Okay?

Because I'm overprovisioned.

I got so many flops and sitting idle.

And the reason for that is because the way that computing works in these large scale data centers is you have flops, you have memory bandwidth, you have memory capacity, you have network capacity at s any given point in time something is bottlenecked at any given point in time something is bottlenecked.

And so what you want to do is you want to provision every overprovision on everything >> so that you could avoid AMD doll's law >> otherwise you're fighting AMD's law all the time.

But then if you're provisioning for peak and not your base loads, then you're going to have a bunch of those flops sitting while while overprovisioned when you don't need them because it's spiky.

But there at at the right time, it goes to 100% MFU, >> but only for a short period of time. >> And if that short period of time, you don't get you don't get all that overprovisioned flops, right? >> Then during that short period of time, it become becomes a long period of time. >> And so what are you seeing for teams that are trying to >> trans and flops are cheap? >> No, flops are cheap.

H100s are going up in price. >> Well, not because of its flops, but because of H100 Hopper, you know, it's it bandwidth, its architecture, it's everything else, not just its flops. >> What what is so should we think about compute as not a scarce resource? >> No, no, that's not that's not the question.

It's like this uh uh when you when you ask about a car, uh back in the old days when we were unsophisticated, we used to say how many horsepower is your car, >> right? >> But these days, who does that? >> So, what's the right measure you think we should be thinking about? performance >> uh and what when you tell the teams guys this is the perf we got to hit next year what are you finding is the eval you're you're reaching for more and more >> you have to come up with a real eval a really serious eval because otherwise you be like improving your flops you know it's it's no you figure out something that that you guys can improve and you're improving that number doesn't make you smarter you're improving that number doesn't make you more successful >> and so it it's there's nothing wrong >> there's nothing wrong with having a lot of flops.

Um, but it's not the complete necessary, not sufficient.

That's all. >> In one sense, you could think about the output of tokens as intelligence.

So, it should be some unit of intelligence per watt or >> Yeah.

Yeah. >> Notice notice the tokens per watt is more than flops.

And in fact, >> we know that now because for decoding these large language models, the single most important thing for generating tokens per watt, right, is actually the aggregate bandwidth across the MVLink 72 and the MFU is incredibly low because the prefill is not that much.

It's mostly decode, >> but you can decouple decoding and pre-fill. >> It's disagregated.

And so notice I just delivered incredibly high tokens per watt with extremely low MFU.

But but not all tokens are born equal, right?

And so how do we account for that?

Like when you're designing the systems of the future, how do we account how what is the right way to measure without a standard measure of intelligence when you have coding tokens being more valuable per what than I don't know some other kind of token?

Does does that does that question make sense? >> Makes perfect sense.

You always have to come back to not just optimizing for SAT scores, you're optimizing for something bigger.

And so so that's that's basically it.

It's the same idea. you're you have to decide what evaluation as you know eval how you evaluate success matters a lot in how people perform and so what Nvidia does extremely well inside the company is the systems that we create for evaluating architectures and and flops is too too contrived >> because it was that easy then >> and so do we have >> I wouldn't be here >> you have a hard job which is to try to design an index of different intelligences is right because you like I think when when I'm building when I'm when our teams are researching on the NVIDIA architecture we've got one lab doing coding another one pushing the frontier of superc conductivity and so on and they got all they all have completely different evals they're measuring for but they're all using Nvidia chips >> so h like how do you how do you solve that problem when your customers all have their own evals yeah >> but the architecture of the underlying platform >> that's why it's so hard and and here it is true it's that is is that hard the problem is this if you if you build something that's too overfit for something.

You could be incredibly good at it. >> And so you're overfit for this one problem.

You're insanely amazing at it, but then the problem is is that market, you know, that problem space may not be good, may not be big enough to fund a sufficiently large R&D, right? >> And so you want to be good at many domains, multi-dommain on the one hand.

On the other hand, if you're good at everything, then you're good at nothing.

You became general purpose.

And so that writing that balance by the way is artistry you know it's that's what I do for a living.

What should we not do?

What should we double down on?

What should we 10x on that you know that's that requires some amount of vision strategy you know some amount of trial and error some just personal enjoyment and entertainment uh you know iteration all of that.

Can we talk about the canvas of Fineman, which is a trip I'm very excited about, but it's been hard to get info on it.

What's the canvas telling you now about what that your art piece is going to look like for the Fineman? >> Well, I can tell you the journey that we came on.

And so, so if you look at Hopper, Hopper was designed for a problem space that was rather new.

It was called pre-training.

And so pre-training uh came along and we we came to the conclusion that that um uh although the generation before it was was uh fairly significant already that we should build even larger ones tremendously larger ones larger than any of the largest science scientific supercomputers in the world. >> Okay.

Okay, so that's a very big deal that that the the largest supercomputer in the world was about $350 million and we we thought you know what uh pre-training is going to be such a large domain and such an important problem.

We should design systems that could be multi-billion dollars >> at the time that we're thinking about doing this sounds insane.

You know, you you would have precisely zero customers.

And the reason for that is because the most expensive thing that has ever been sold was $350 million and you're building something that's multiple billions of dollars.

So you're pre you're building for a precisely c a marketplace of zero but we went and did it anyways on first on first reasoning and so hopper was designed for pre-training and that was a great call.

The second thing that we did was we said okay well after after training and we'll keep we're going to keep making training better but the goal is not of AI isn't training the goal of AI is inference >> and and um and what kind of a system would inference really care about and so we created a system called MVLink72 and the reason we did that was because decode the in in in processing the neuronet network there's the prefill which is really context processing and things like that and attention processing and then the decode which generating all these tokens, the generation of the tokens requires really high uh memory bandwidth and the amount of memory bandwidth you need is way more than one chip can possibly provide.

And so we said why don't we gang up like 72 of these things and so we had to invent all kinds of new systems for switching and interconnects and uh created all kinds of new certities and and we created essentially the world's first rack scale computer.

It's called Grace Blackwell MVLink72. the speed up over the previous generation 50 times.

In two years, we improved something by 50 times, Moors law would have improved it by 2x.

Okay, so the architecture and the insight uh was fantastic and decode and inference and large language models and token generation it you know all of that kind of landed at exactly the time that Grace Blackwell came out and boom took off.

So Grace Blackwell uh another incredible generation.

Now the question is what happened to Vera Rubin and what's the big idea?

Well, the big idea is that that the goal isn't just to think.

The goal is to do work.

And so, Vera Rubin is designed for agents.

And so, the question is what is the compute pattern?

What is the processing pattern of agents? >> And uh agents of course uh you have to you have to load a fair amount of memory.

Uh long memory.

He's got working memory.

So, long-term memory we put into storage.

And we got that storage needs to be able to directly communicate with the GP. you can't be copying copying that that that the data off of the the uh the network storage, but you want storage to be connected right into the processor itself.

And so we we have we have storage that's connected to to the fabric.

We have we have um we're going to use a lot of tools and so CPUs are going to be really important.

But the CPUs of the last of the current generation was really designed for cloud computing.

And so you have these CPUs with hundreds of cores like you know 200 cores.

Well, the CPUs of agents because because the AI is this multi-billion dollar system and it sends off uh an instruction to use a tool and that tool is going to run on the CPU.

Meanwhile, this a this computer this GPU supercomput this multi-billion dollar system is waiting for this one CPU and so that CPU really wants to have extremely low latency.

So we designed Vera which is the for for current generation for singlethreaded you know multiple core single threaded code it is by far the most most uh performant and so we created a CPU just for that.

Notice notice the way you solve this problem intuitively is you you kind of think about what is the computing pattern.

Um how is it different than the past?

Um you have to have some mental model about it and you create a system uh that you can you can go and uh go build uh to to uh run that.

And so so now agents are here.

We're going to run that on Vera Rubin and and and hopefully when Fman gets here, it's going to be it's going to be like all software uh a we call them agents today, but you know, it could be modules in the past or, you know, subm modules and and so in the future, you're going to clearly have systems of agents and agents with sub aents and sub aents with sub aents and and so you're going to have um you know, this swarm of agents and and what what kind of computer, you know, does that does that manifest?

And so that's that's likely what Flyman's about.

I have one more follow-up question on that which is you know one of the things you've always done well is kind of spot bottlenecks one generation ahead and then try to sort of presolve for that the supply chain a year ago that was um photonics end up becoming a huge solution um as we look about looked to energy as a bottleneck you know copper wires literally copper wires are one of the the transmission sort of bottlenecks how does that get solved in your view >> um energy is just everywhere for well first the first thing that we could do that that um uh that is in our control.

You know, as with everything in life, whatever the problem is uh whatever the external external concerns are uh you should do something that's in your control and in our control is energy efficiency.

So if you look at look at tokens per watt uh we improved it by 50x and then we'll have to keep on improving it by you know by significant factors and it compounds.

So that's that's the first thing we can do. we can control that through code design architectures and things like that.

And the second thing that we could do the thing we could um inspire people to and that's through a lot of education inspire the ecosystem to get ready for this and and um uh and and I've been over the last last half decade uh helping people understand the amount of compute that's likely to be coming and I just told you guys something about how I reason through uh how much energy is going to be necessary.

The amount of energy that we need for compute for computing is likely um you know probably a thousand times more than we currently have and that's an enormous amount of energy.

Um however the way to think about that is in the future computers are going to be two things. is always going to be generated because it's intelligent.

It's contextually aware.

So, it's going to be generated.

And the number two is going to be continuous.

And so, you this generative computing in a continuous way um compared to pre-recorded retrievalbased computing that is only um initiated on, you know, per use.

The question is how do you how do you think about the amount of energy necessarily that?

So, I I think if you if you say we need it a thousand times, uh I I wouldn't be surprised if we're off by a couple of orders of magnitude. and and so we need a lot more compute. we need a lot more energy and so you got to go and explain this to people and so I I you know you got to explain it to people in a way that's kind of common sense and and and they can observe it and there you know indicators along the way that that in fact this is happening and and notice just as I was breaking it down for you guys you know I'm reasoning about it for you so that so it's common sense to you and so the amount of energy is is high and then lastly the source of energy we there there's there's a there's all kinds of sources of energy But unfortunately because of of great concerns about about um uh the cost of sustainable energy, we underinvested in in sustainable energy.

Um but this is the best time ever in the history of humanity to go and invest in sustainable energy.

And the reason for that is because the market forces are so strong.

Back in the old days, you needed government subsidies to go build solar farms and government subsidies to go build nuclear plants.

And now you can just market will pay you to do it.

And so market forces are so powerful right now.

This is our best chance to upgrade our grid, our you know archaic grid.

Um add add sustainable energy of all kinds.

And you know this is a great time >> in terms of education.

What I've learned as well, we designed the class for the students here.

Turns out a lot more people especially a lot of investors and capital allocators are watching this right. >> Oh sh Why don't we put it up? >> Yeah.

Um, and so if there's >> I'm just kidding. >> If there's education you'd like to do to that audience, feel free to drop in.

You know, >> repeating yourself after a while with with capital allocators can get >> repetitive.

I don't mind that. >> So, if you'd like to transmit, feel free feel free to um what is the next question we should take? >> The question is how best to spend their mental faculties over the next few years. >> Yeah.

I so so first of all on the pain and suffering comment um there there's a there's there's some kind of there's some advice that says you should you should choose what you love and what you're passionate about.

That's what your career should be.

And and I think that's terrific.

I think that's terrific.

You know, if you're if you happen to to to know what you're passionate about, if you happen to know what you love.

Um uh uh but I think there are a lot of people who don't know what they're passionate about and they don't know what they love.

And the reason for that is because nobody knows everything.

How could you not how could you know what you don't know?

So in a lot of ways um the idea that you would only do you would only choose careers that give you passion that gives you you know it gives you get makes you happy um is a bar that I think is too too high. number one.

Um, and the reason for that is because whatever you decide to do for a living, whether it's you found something that you're passionate about, uh, or this is your job.

And in my case, you know, it used to be cleaning toilets and busting tables.

It was my job and I will do the best I can in my job.

Whatever you give me as a job, I will do the best I can possibly do.

And I do that today.

And now there's a misunderstanding that that somehow CEOs we love our job and and and you know many co oh I I'm passionate about my job I love my job they're they're lying there there's not there's not one CEO who who I who can say that you know from the moment I wake up to the moment I go to bed is just zippity dooah the fact of the matter is uh I really love doing 10% of my work and 90% of my work is hard and I do it to to the best of my ability anyhow and I suffer through it.

I literally suffer through it.

I prefer to do something else that other 10%.

But that other 10% there's only so much quantity of that and and every company has abundance of problems and there comes in different types and you're going through life you're going to have abundance of problems that going to come in different types and you just have to learn how to condition yourself to want to get to a better state. no matter how hard to get better no matter how hard.

And that's suffering.

You know, you're you don't like doing it, but you're doing it with all your might anyways.

What do you call that?

That's suffering.

And so, so I think that when you when you suffer and you have the benefit of struggle and you you're been presented with many opportunities like that, it teaches you resilience.

And when it when the time comes and and the world or your family or your company or your colleagues, they need you to be tough.

They need you to be resilient.

They just need you to be able to fight through it.

You can't have those.

You don't have that character about you.

You don't have that muscle unless you've gone through it a whole bunch of times.

And so, you know, I'm I'm advising that that that you not you not seek for just joy, that you also seek for some some pain, some suffering, because you're going to need it someday.

And and then lastly, it's also it's just your job.

You know, >> as preacher Hong once said, don't wake up with a loser mindset.

The question is, what's your favorite order of Denny's?

Yeah, Corllis really should have a Dennis.

Um, you know, after all these years, frankly, it's about time, right?

And so, there was that there was that that one Chinese restaurant.

Um, and uh and Woodstocks, of course, right?

Corvalis Woodstocks Pizza.

It's still pretty good, isn't it?

Woodstocks. >> It's all I like American Dream better. >> American Dreams better.

Okay.

All right.

I I'll I'll be back there soon enough.

And so so um uh Denny's I would say surprisingly the fried chicken is really good.

So you know it's a slightly on the on the sweet side.

Uh Superbird is excellent and done right.

And um and then another one if they're willing to make it for you.

Make it like a Superbird.

Okay.

But is a grill ham and cheese with tomato and mustard.

And if they're willing to make it for you that they're willing to make it for me.

And so, but that's because I'm not not because because I'm an alum.

They know that.

Hey, use the bus tables here.

Yeah.

Yeah.

We'll make special for you.

Uh but but those are all good.

You know, the Grand Slam, you know, I enjoy it.

I like a pigs in a blanket.

So, that's pretty good.

Um there's a whole bunch of stuff.

Good.

I go all day.

I at Denny's I had my first fudge hot fudge sandwich.

I had my first uh apple pie with cheese on top.

I that's like for for a Chinese kid, it's like what is that about?

That doesn't make any sense.

And but now you think about it makes perfect sense, you know, apple and cheese.

But anyways, I I had a whole bunch of it was I had my first milkshake when I was at Denny's.

Um I had a whole bunch of firsts.

Yeah, Denny's Denny's was eye opening for me, >> man.

Before we lose you to the to memory lane, next question, please. >> Those are some of the most important questions.

Agreed.

Yes, the questions about your thoughts on adversarial countries getting access to uh Nvidia chips. >> Uh first of all, so you you know what we we make for a living?

We make GPUs and and um uh GPUs are used for uh video games.

Uh they're used for uh delivering soy sauce.

They're used for medical imaging.

Uh if you had a CT scan done yesterday, I'm fine.

Uh but that behind it was Nvidia.

Uh Nvidia is in every single medical imaging system in the world.

And uh and so the question is what is it that you build?

Um what I'm what I'm fundamentally against and it makes no sense.

It makes no sense in this moment is to compare Nvidia GPUs to atomic bombs.

There are billion people with Nvidia GPUs.

I advocate Nvidia GPUs to all of you.

Uh I advocate Nvidia GPUs to my family, to my kids, uh to people I love, but I don't advocate atomic bombs to anybody. >> So that analogy is stupid.

And so, so if you start from there, you can't finish a thought.

If you start from believing that, you can't finish the rest of the thoughts.

Um, the second the second idea that I I consider completely ridiculous.

Uh, why should American companies go compete in foreign countries?

You're You're going to lose it anyways.

So, why go?

Well, if you guys all apply that same philosophy, why wake up in the morning?

And so, I don't I don't prescribe to we are going to lose anyways.

I don't prescribe to that.

If you want me to lose, you're going to have to deal it to me.

But, you know, I'm going to have to put up a fight.

And I put up a lot of fights over the years.

I'm doing okay.

And so, so I think that and and and as you know, the battle, the competition uh serves markets.

It enhances and enhances your company.

I'm not a little bit afraid of having to go and compete in the marketplace, but the idea that I'm going to lose anyway, so why go compete makes no sense to me.

And then lastly, uh the idea that that somehow we should deprive certain countries of general purpose computing and we can all acknowledge now Nvidia is a general purpose computing company.

I just gave you a whole bunch of general purpose use cases.

Is a general purpose computing company to be deprived of that. so that one or two companies uh could benefit from depriving other people of it.

That makes me makes no sense either.

Why should one industry suffer so that another one company benefits, another one or two companies benefit?

Entire American the the American technology industry is one of our national treasures.

You are going to be part of it.

And if I do my job, when you are done graduating, you're going to graduate into the mightiest computer industry and the mightiest industry in the history of humanity.

But if we give it up for some reason or we through policy decide that we can't go and sell and concede twothirds of the market to the twothirds of the world to other companies, by the time that you graduate, you would have gone into a shell of an industry. that shell of an industry we've seen before.

A long time ago, the same arguments went went against America in telecommunications.

Today, America has no telecommunications fundamental technology anymore.

It was all lit.

It was all completely policied out of our country.

And so, somebody has to put up a fight for that. some of these reasoning systems to to to say that AI is AI is going to come and it's going to be a singularity moment that singularity that moment the moment it comes it's going to be the most powerful thing in the world it's come come as a flash we have no idea whether it's going to come on Wednesday or Thursday at 7:00 but when it comes it's going to be game over some percentage chance that it'll be the end of society as we know it come on we all watch Dune we don't have to repeat it.

And and so I think that living living their fantasies out, their science fiction fantasies out uh in in in in public uh demonstration when everybody is relying on their words and believe in the words is irresponsible.

It is not true.

It is not true that we have no idea how these systems work.

It is not true.

It is not true that the technology is going to some somehow uh in some nancond become infinitely powerful and therefore it's going to take over the world.

It is not true.

It is not true.

There's no way to defend against it.

It is not true.

These things are all being made up and it's made up in a way that unfortunately even harms all of you.

You're in computer science.

You're hoping that when you graduate people care about computers.

We want to create a future that is optimistic about the technology that you are learning to master.

We want to create that future.

We want to make sure that America, we want to make sure that everybody benefits from AI.

Everybody should have AI.

Nobody should have nuclear bombs.

Can you guys agree with that? >> And so, okay.

And so, so young man, young man, thank you for triggering me.

I'm just kidding. >> Okay, >> I'm just kidding.

I'm just kidding.

I just wanted to get get it out. >> So, we're rational optimists here on at AI Coachella.

So, we believe in optimism.

I'm gonna push back a little bit on a different angle.

I completely agree.

Reasoning by analogy is a problem.

Once you start with bombs of first principles, what we are observing is that compute, we are computed in America.

Independent teams, startups, universities, they can't get compute.

So from a preference order perspective, shouldn't America get first priority to a scarce resource before we start shipping it off?

Absolutely. >> But that's not happening. >> Absolutely not.

There's the gotcha.

Yeah.

Absolutely and absolutely not.

And the question is why not? >> Uh there's plenty of chips.

You guys, if some if if the president of Stanford places an order, I promise you I'll deliver it. >> I have no absolutely. >> You guys heard it here. >> All right. ahead of this is not funny.

This is not funny.

We are dying out there. >> No.

No.

This is not funny.

That's right.

This is a serious matter.

Um it is not it is not true.

It is not true that people are giving me orders, placing orders, and we're not delivering chips.

It is just not true.

You got to you got to place orders.

The fact of the matter is the fundamental problem is actually something very different. >> The Stanford needs compute.

Science needs compute.

The fundamental problem is the system is no longer built to be able to deliver massive scale compute.

And the reason for that is because just think all of the all of the research departments here at Stanford, they're all in different departments.

You all raise your own funding.

You all get your own grants.

Nobody's going to go share their grants.

But none of the grants are big enough to have a large enough compute that you use some of the time, but when you use it, you need it to be incredible.

You've got the world moved away from those centralized computing environments towards everybody just using laptops.

That's this is today's computing environment and fundamentally these all the universities Stanford is not alone.

You don't have a budget for a billion dollar compute.

It doesn't exist. >> But whose fault is that? >> Stanford's.

And the reason the reason why you have to say that is because I'm empowering.

When somebody is at fault, you empower them to solve it.

Do you agree?

When you Oh, yeah.

It's not your fault, son.

It's not your fault.

You're a failure.

It's >> It's not your fault. >> Talking to me right here, you know.

Uh yeah.

Hey son, you're an idiot.

It's not >> No, it's absolutely your fault.

And and so by saying that it's absolutely your fault, you're also empowering yourself to solve it.

Isn't that right? you're empowering yourself to solve it.

And so the question that you just talked to somebody who kind of feels, you know, I can do something about my future.

You're talking to somebody who who's who believes in that.

Okay?

And so if I were Stanford, you just have to you have to find a way to to to change the way you do budgeting, the way you deal with computing.

You have to find a way to aggregate and build yourself a linear accelerator just like Stanford has done in the past.

We need to build campuswide supercomputers that everybody share.

Now, you could also go and just contract somebody else to do it.

I mean, that's that's all possible.

But you do need to have, you know, a billion dollars.

You need to have some reasonable fund to go be bu build something like this because that's how much it costs.

But that's that's just what it takes. >> I mean, last I checked, we've got a what $40 billion endowment here.

How would you put that to use if you were if you were stepping cut a billion dollars of it right away and give it to somebody as a cloud service and have every single student and every researcher here uh have access to to uh to uh uh AI supercomputers.

I would do that right away.

Now, of course, of course, you've got to go plan things.

You don't if you want to buy a billion dollars worth of tomatoes, you don't show up to the grocery store and hire and then and then and then they don't have a billion dollars of tomatoes and you go, "Aha, you're withholding tomatoes from me.

That's just ridiculous.

And so so you know, so you got to do some planning.

And so what you got to do is you got to say, "Next year we need to have a billion dollars worth of computing for Stanford and and uh we'll go build it." >> All right.

You know what?

We'll move on.

But thank you for that. >> Yeah.

Yeah.

EXACTLY. >> We'll come back to that one. >> Yeah.

What is the best and worst part of your job?

When you're when you're CEO of a company, you you have the benefit you have the benefit of of a lot of uh really fun things.

Like for example, you you're really the person who has to conceive of the intersection between vision and strategy and execution.

Okay?

And so so you have to live in that in that world.

And it gives you and when you're a company with capability and I'm surrounded by amazing computer scientists and many of them from from Stanford and when you're surrounded by people like that when you have a vision it's very realizable and because you're with amazing people your vision is more ambitious.

Okay.

And so so I think I think that's the fun part.

The not fun part.

So and so that fun part I get to do almost all the time.

I'm always constantly um updating my my my view of the future and my vision of the future and and what our role in it and and how we ought to reinvent ourselves so that we could you know contribute more to that future or or go invent that future in the first place and and so as a CEO you have you get to live in that world and that's fun.

You're it's very imaginative.

It's very strategic.

It's you know highly complicated.

There's no right answer. uh and in a lot of ways it's it's creativity at at at its most.

Okay.

On the other hand, what comes with that power is the responsibilities for a bunch of people who joined you in that spaceship that joined you in that in that vessel and they want to be they want to help you create this future and they're part of your team and you feel a deep responsibility for their well-being.

And so when the company's not doing well or the company in the older days, you know, when we were in the beginning trying to find our way, uh, we probably nearly went out of business, you know, four or five times.

I mean, literally almost went out of business and we were on fumes or or we're really flat on our back.

And so during those times, it's embarrassing, it's humiliating, it's hard.

Um, you don't know what the answer is.

Often times you're in the dark.

Uh, you're afraid. uh you know all of those the feelings that that we have as humans just multiplied by you know a thousand a million and and uh uh you know when you're a public CEO uh your face is always out there and when you do well uh people are happy when you don't do well they're fast to tell you and and um and so you're you know and so it's a vulnerable you know for me it's it's a highly vulnerable profession and and so Yeah, you're not naked, but you feel it.

You know, >> question is, what's the biggest mistake you made in the early days of Nvidia and what you learn from it? >> Um, let me let me give you an example of of what somebody might say and and I will say I I won't I'll say that that's not and so so anybody who knows our history would know that the first generation of our products uh the architecture the technology we used was completely wrong.

It's not like a little bit wrong. is like completely wrong.

The fact that that that smart engineers and professionals and we were actually funded and we created this thing and it's like check it out doesn't work at all you know and so uh that that using curved surfaces instead of triangles no Zbuffer instead of Zbuffer forward texture mapping instead of inverse texture mapping we did everything wrong.

We did everything wrong.

No floating point inside.

We did everything wrong.

And so we made a lot of tremendously bad choices.

Um, and I I'll say that that uh those are technical bad choices, but it led to strategic genius moves.

Um, how do you take a company that um had that reputation and wasted a bunch of money and a bunch of time two and a half years doing it the wrong way and surrounded by competition and now here we are the only one remain.

Okay.

And so so that that transformation taught me a lot about the importance of technology is important but strategy is so important and so how you see the world uh how you approach competition how do you approach the market uh how do you conserve resources and apply resources th those decisions um I learned more in my early 30s through that deep failure I and the company almost vaporizing I learned so much about strategy and strategic thinking and and maneuvering and things like that and it's lasted a whole whole long time.

The mistake that I made that I I would say um was a genuinely straightup mistake is when the PC or or when mobile devices took off uh we were approached by very important companies that that are in important in the mobile space uh to work on some mobile devices and and um and the choices that that I made Um I I think the answer when they approached us the answer should have been nah not interested but we decided to shift a bunch of our resources to go build mobile devices and um I and I thought that we could add a lot of value but it turn you know I think if I would have thought through it a couple more clicks uh the amount of value you could really deliver in for for the things that we know how to do and what we're good at is probably marginal. at best.

And so, uh, I shifted the company to go into mobile devices.

Uh, it grew into a billion dollar business and and that kind of positive reinforcement.

And then shortly after, uh, during the 3G to 4G transition, uh, we were just 100% locked out and and, um, uh, Qualcomm was the leader in that 3G to 4G modem mode and that's the most important part of the phone.

Not the SoC, not computer graphics, not even the application processor.

The phone is obviously the most important part.

And so during that transition, uh, they were able to block us out, I could have probably called it, you know, to to if you if that circumstance were to happen again.

I would have said, "Yeah, it's it it would be a really interesting opportunity for a couple years, but we're going to get shut out after that, so what's the point?

Why?

Let's go conserve our resources somewhere else." But the the recovery, so we got shut out.

We built it up to about a billion dollars and it went back to zero.

But the recovery was I took all of that expertise that extreme low power and energy efficiency expertise and I shifted all to um an application that didn't exist at the time called robotics.

And so all of the the somebody mentioned Thor uh Thor is the great great great great grandson of the chip that we were using um uh in mobile devices. and that that entire genealogy and all the teams and all the expertise that we we built up was really helpful to getting here.

And so it doesn't that's rationalization.

Um going into that market in the first place was a waste of time and so that that I think is a strategic mistake.

Um on strategy is there you know sometimes strategy is about forecasting sort of precisely enough.

Is there uh from a systems perspective, what do you think you've updated your priors on or what what is the forecasting mechanism you've developed to give yourself some confidence that like this fog of war here?

Don't quite know where things are going to go, but generally speaking, we're like shooting in the right direction.

Is there any is there sort of a systems piece of systems design advice you'd give folks on when the shape of the future is not entirely clear? >> Yeah, and and in fact in fact you used all this the right words already.

Um the first thing I do is is I what am I observing?

What am what am I observing?

And um based on what I observe, uh let's reason about it back to first principles.

Break it all back down and ask ourselves uh so what's going to happen next and first so what is this a big deal?

Hey, deep learning, computer vision, AlexNet, you know, big deal.

Is that a big deal or not a big deal?

And so the big deal part of it is my goodness. uh in just one you know here here's two engineers right Alex and and Ilia and uh and and Hinton of course and they came up with a neuronet network model and boom it crushed the the computer vision capabilities of all the computer scientists you know decades before them in one shot and so is that a big deal is that a big deal um the the the step up in in quality and performance was a big deal now the next question is so what's going to happen next how far can you take And then if you could do it in this way, what else can you what else can you solve?

Um and if if this was able to solve some really amazing problems, uh what does that mean to computers and computing?

And so you just keep asking yourself these questions, right?

And so you just iterating it like that all the way to first principles.

And then from that you create a mental model about the future of computing and uh where is it going to be?

What can it do?

For example, self-driving cars and robotics. um this uh how large would models become and uh if if so what would computers look like? uh what with processing neuronet networks how's that different than processing you know floatingoint numbers and integers and first principle mathematics you know we express everything in FP64 FP32 but obviously neuronet networks don't have to do that and so so you you reason through it kind of like this and then you build up a mental model of a future you know of the future and then where your your company where you are going to be within it and then you just work backwards from there and and then and then now the question of course is you could be wrong and often times you're, you know, if you reason about things properly, you're not completely wrong, but you're not completely right.

And so I tend to I tend to be very comfortable saying, okay, these are the things that that will likely happen and these are things will absolutely happen and these things may happen.

And based on that, I think we got to go in that general direction.

We'll feel our way through.

And now that now that the the skill of of building companies then of being successful along the way is you're going into this direction and it's going to take energy.

It's going to take time.

It's going to take money and and everything that time, energy and money that takes away from something else, right?

So the cost the the the opportunity cost of pursuing a strategy is the real cost.

And so you just got to ask yourself how can you be smart enough such that the opportunity cost is reduced and your optionality is increased.

And so you're trying to think through all of that stuff all the time.

You know it's no simple answer but but um in a lot of ways uh you're trying to get the journey to pay for itself given uh everybody's going to mob you for more signatures.

That's where we're going to end. >> Thank you.

Thank you very much.
