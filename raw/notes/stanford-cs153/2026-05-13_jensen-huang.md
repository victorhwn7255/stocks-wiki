# Stanford CS153 Frontier Systems — Jensen Huang: "The Compute Behind Intelligence"

**Speaker:** Jensen Huang (Founder & CEO, NVIDIA) · **Channel:** Stanford Online · **Upload:** 2026-05-13 · **Duration:** 1:08:24 · **Views:** ~140,461
**URL:** https://youtu.be/tsQB0n0YV3k
**Source tier:** Tier 3, aligned commercial incentive (technical/first-principles talk, higher analytical value than a typical promo).

> **★ FULL ANALYSIS LIVES ELSEWHERE — do not duplicate.** This lecture was worked up before the CS153 corpus existed, at:
> `raw/notes/video-intel/2026-05-13_stanford-cs153_jensen-huang-compute-behind-intelligence.md`
> This file holds the transcript only, for corpus completeness. The CS153 `notes.md` references the existing analysis (Lecture log + the cross-walk in Layer 0). Key takeaways already woven into the corpus: tokens-per-watt 50× (Grace Blackwell NVLink72); rack-scale NVLink72 = "one giant GPU"; Hopper→Blackwell→Vera Rubin→Feynman as a bottleneck-chase; energy ~1,000× short; **xAI 11% MFU = *intentional* overprovisioning** (the cross-video tension vs Vahdat in Layer 0); NVDA seeds open models (Nemotron / BioNeMo / Alpamayo / GR00T); anti-export-control "telecom cautionary tale."

## Transcript (Tier 3/5 — not a primary source)

I would like to welcome back Preacher Huang.

WE HAVE BEEN NOW IN a locked in a global race way faster than NASCAR racing.

And it's partly your fault.

Jensen's been the preacher that's given us all the power we need, all the energy and some more to have what I think has been the craziest 12 months of my life, certainly for many of you, and we're just getting started.

Um the energy with which you approach every single thing you do, including the class last year.

And then all every time I've had the chance to hang out with you, you've given so much time to the students, to the founders.

Thank you.

Should we jump right in? >> Yeah, let's go. >> All right.

We're going to go rapid fire.

What is co-design and why is it so important? >> Uh I'll I'll answer that in a second.

Yes, please.

Um but but uh this is a great time to be in computer science.

And obviously the reason is because computing is being reinvented for the first time as dramatically as as it is for the first time really in about 60 plus years.

Uh the computer that we know of that you all use in our computing model, our mental model of a computer, the architecture of a computer, how you write the program, run the program, how you think about even taking computers to market, what it's used for, for 64 years it has been largely the same since the IBM System 360.

In fact, my first architecture book for learning about computer architecture was the System 360's manual.

And so so a lot has changed as we went from PCs to internet and mobile and cloud and all those things, but the fact of the matter is the computing model, the fundamental part of computer science has largely remained the same.

Until now.

You know, for the first time the way you write the software, how you process the neural network versus the software, and what the applications can do has now dramatically changed.

Everything is fundamentally different.

At the highest level, you know, one simple way to think about it is computing as we knew it before was largely pre-recorded.

It's content that we pre-recorded images, videos, you know, software that we largely pre-recorded, but now everything is generated.

And the nice thing about generating everything in real time is that it could be contextually consistent contextually relevant to what what it is that you're dealing with, and of course it can respond to your intention, not just explicitly to the things that you instruct.

And and so so the computer the computer is is fundamentally different in that way.

Now, the question is what does that mean at every single layer of the stack from from how the computer how the software is now developed, the methodology of it, how you organize your company to be able to develop software of today completely changed.

And so the methodology, the tools we use, the approach that we think about software coding completely changed.

How we run the software, neural network versus compiled binaries, very very different.

And so what does that mean to the computer system, the network, the storage, what does that mean to the software stack and the cloud services that sit on top of that.

And of course, you know, everything about the applications.

What did it open up?

And somebody just somebody just came and said this piece of software we just opened up called Alpaca Mayo.

And I've been working on self-driving cars now for about 13 years.

And and I and I and the and the days of robo taxis are going to be literally everywhere.

Everything that moves will be robotic.

And and that's an example of an application that that we wouldn't consider doing until deep learning and artificial intelligence came along.

That was a such a big unlock that you know, I said, "Hey, aha.

This all of these problems that we wanted to solve in the past that we need a computer vision for really really are now fundamentally unlocked." And so so it's how you think about every single stage of that.

What is you know, what is a software engineer?

How do you organize the company?

What is a computer for the age of AI?

How do you architect that?

All the way to what you can use it for and therefore where you would deploy it.

All of that has fundamentally changed.

And and for me the journey really started about 15 years ago.

And I had the benefit of seeing some early works in in the area.

And as all Stanford students do, you break the problem down, you reason about it from first principles, and you come to the conclusion literally everything has changed.

And so here you are, you know, computer scientist students.

This is really the first generation of AI becoming useful.

And where we a couple years ago was in the generative part of AI.

And and as you guys know, generative AI not only made it made it cool for us to do image generation and text summarization and translation and whatnot.

But generative generative AI also enabled us to think.

And so when I saw generative AI, you know, what other people saw was that it was able to generate images and I and I surely would appreciated that as well.

But the fact that you can generate thoughts it in the form of images, but you can generate thoughts, you can also reason with it.

And the ability for AI to think after GPT was was very very obvious.

Now the question is is how would you train, how would you fine-tune an AI to be able to reason step by step by step and how would you teach it how to do so at at fairly large scale in a kind of semi-supervised way.

And so those are kind of the engineering problems you had to solve, but the moment you see GPT, you say aha, thinking is just around the corner.

And thinking is generating tokens that you consume internally and generating tokens that you consume externally would be called tool use.

And so the idea that that after GPT happened two years ago that we would be at this moment was fairly easy to predict.

Now of course you know, unbelievable amount of technology was invented and a lot of amazing people did amazing work, but you could almost see that moment here.

And so here we are.

You now have agentic systems and so now the question is is what's next?

And what happens in a world where a computer is not not responsive to what you ask it to do.

It's not it's not bought on demand.

You know, today's computing is really on demand computing.

The word on demand was actually created in our generation to talk about how you think about using computers.

Time sharing computers that you would use on demand became cloud computers.

And cloud computing of course is on demand, but in your new world of agentic system, these the computers are now continuously running.

And so, what happens in a world where the computers are continuously running, what happens to cloud services, what happened to your personal computer, what happens to, you know, all of these different systems?

Now, there's a great great opportunity again to rethink all of that.

And so, so what I, you know, is kind of like my my introduction to everything about um computer science has changed, and and everything about every field of science has changed because of the things that we've changed.

And and so, this is a good time to go to school.

Okay.

That's it.

What was your question?

You know what?

I'm just going to turn it over to the kids. >> Co-design, co-design, co-design. >> No, no, let let let's just go into the the students have questions.

They've all been asking questions in Discord.

They're all voting on each other's questions. >> Co-design is really interesting, but it's not it Co-design is super interesting.

And and basically, co-design says, it said, back in the old days, we abstracted computing so that so the people who design microprocessors design microprocessors, people who worked on compilers worked on compilers, and people who worked on languages worked on languages, and so on and so forth.

You guys know that.

And we actually had different fields.

Um but the problem, and in fact, this happened at Stanford, what's the what's the beauty of risk?

What was the beauty of the work that John Hennessy did?

Um it it the beauty of it is that you have to think about compilers and microprocessor architectures harmoniously, co-designed.

Because otherwise, you could end up creating a microprocessor that's super super tight, and you know, everything is is maximally optimized, but unfortunately, it's hard to compile.

It's it's difficult, it's not compilable.

And so, they created a a simpler instruction set that exposed simplicity to compilers so that compilers could do a better job generating code.

And it turns out a simpler machine co-designed with a compiler creates better performance than two systems that were optimized individually.

That's, you know, that's very Stanford.

Okay, this is a this is part of your heritage as all of your and and John Hennessy's, you know, trail of amazing work that's left behind.

And so you take you take that and you think about, well, what happens in in the post world of general-purpose computing?

Why is it that every problem in in computer science would be solvable by a general-purpose instrument?

At some level, you know, you could say, well, if you had a general-purpose instrument, you prefer that.

However, there are some extreme problems, whether it's computer graphics back in the old days or molecular dynamics or quantum chemistry or, you know, you know, fluid dynamics and large multi-scale mesoscale multi-physics problems or deep learning, these problems are so computationally intense, why would you use a general-purpose computer to go do that?

And so there, you the big insight is what if you understood the algorithms, understood the computer systems, understood the, you know, if you will, the compilers, the frameworks, and understood the architecture of chips, and you were optimizing all of it at the same time.

And so the the facts here are the facts.

This is what happens when you do it what I just described.

Nvidia is probably the first computer systems company that's extreme co-design.

I mean, we we literally co-designed across all of that, and including CPUs, GPUs, networking, and switches, and every and storage.

And so the question is, what do you get?

Well, Moore's Law back in the old days, you guys all know about that.

Moore's Law was about uh 2x every 18 months, so call it 10x every 5 years.

Okay, so But every 5 years is 100x every 10 years.

And that's that was in the good old days of Moore's law and for all the computer scientists in the room, you know, you know that Moore's law was underpinned by a concept called Dennard scaling and Dennard scaling ran out of steam um several years ago, probably about a decade ago in fact.

And we we kept squeezing it, we kept squeezing it, but over the course of last 10 years, if you just allowed microprocessors to continue to scale and you just don't touch the software and you just benefit from the speed up of semiconductors and microprocessor design, you at best case you would have gotten 100x, but probably because Dennard scaling slowed down and Moore's law largely ended, you know, you probably got something along the lines of 10x over the course of 10 years.

Well, in the case of Nvidia and Co-design, we got 1 million x over 10 years. 1 million x.

And so, somewhere between 100,000x and a million x, okay?

So, there when you're talking about numbers that big, it really doesn't matter.

And so, a million x over 10 years, it got we we were able to get scaling and computation scale so large so fast that AI researchers say, "Why don't we just take all of the internet?

Why even worry about what data to go curate and what what data to create?

Let's just take all of the world's data and just give it to the computer." And that's really the big breakthrough.

When you're able to to to do something so insanely fast, you know, for example, if you were able to travel at the speed of light, uh where we choose to live is doesn't matter.

Uh if you were able to go from New York to California in 10 minutes, uh you know, uh our freedom everything about society would change, right?

And so, if you were able to do computing a million times faster, everything about computing computing changed.

And that's really the big breakthrough.

Because of Co-design, because of the way Nvidia approached it, we accelerated computing by so so far that it created all this infinite abundance opportunity for everybody to to think about the future.

And so anyways, here we are.

Cool. >> I have a bunch of follow-up questions, but I'm not going to ask them. >> one word led to that. >> GPT-10 >> That's what it's like to work at Nvidia.

You give me one word and you get ranted at for about half an hour.

Because I got too much to too much to share with you. >> The question is how should education evolve in response to the industry as it's changing? >> Yeah, and that's a really excellent question and and I think the answer clearly is AI should be part of your curriculum, not just in learning about AI, but using AI for the curriculum.

The The problem with with textbooks, as you know, it takes an enormous amount of effort to do.

And when I was taking classes at Stanford, Professor Hennessy was still writing his textbook.

It was all handwritten out.

And and each week it seemed like he was writing a chapter.

I don't even know how he writes a chapter a week, but every week he was writing about a chapter.

And and then over time, all of those notes turned into a textbook into the first edition.

And that must have taken several years.

And so I I think I think um it's not it's not possible for universities, for you know, pre-recorded textbooks to keep up with information and knowledge that's being generated in real-time by AI.

And so I think the future probably has to be some union of the two.

And and I I don't know about you guys, but I can't learn anymore without AI.

And so not only do I have the AI read the papers, but I also have once it reads the papers, I might ask it to go read, you know, a whole bunch of the other papers that are associated with it.

And then now it becomes a super researcher, and then I can I can first I ask it to summarize.

I ask it some basic questions, and then after that you interact with that paper as if it's a researcher that's dedicated to you.

And so most people don't realize that, you know, I think a lot of people still think that you you summarize a document, but in the process of summarizing the document, that AI learned a lot.

And so, and I I am uh I think that in the future I I do hope that that curriculums are are tightly integrated.

Um I I will say in defense of the textbooks though, I will say that first principles don't change.

You know, in the final analysis uh a Mead and Conway still a solid uh uh fundamental methodology as as before.

It It is true that the scaling process that led to um constant constant current density, um constant uh power density, all of that all of those design optimizations associated with modern semiconductor design, you know, that the we've we've kind of exhausted all of that.

None of that is ISO anything anymore, and so um but it's still good to know where we came from, you know, and so I I would still encourage that to appreciate the first principles.

And And you know, while while I was going to to Stanford, I was al- already working at AMD, and um and I was designing microprocessors at the time.

And it was still it was still really good to to see simultaneously um how how we design things in practice versus uh the first principle methods associated with learning about eventually uh how to design these things.

And And um I I I really enjoyed having you know, feet on both sides of it, and I I ended up learning a lot more.

And so, what that means is when you're using AI, which is real world, it's contextually relevant now, um it's it's contemporary, and meanwhile you have first principle knowledge that you're learning at the same time.

You're kind of getting the same thing that I experienced. >> The question is op- What are your thoughts on open source?

How do we How does open source stay at the frontier? >> Yeah, there's really the question of closed source versus closed proprietary software versus open source.

There's a question of my intentions with open source.

And so I'll start with my intentions of open source.

Um first of all, I Nvidia uses more Anthropic and Open AI tokens than just about anybody.

I And And the reason for that is obviously we do a lot of coding, we do a lot of design.

And 100% of our engineers are now agentic agentically supported.

And so So I want them to be working with agents using the latest generation tools and re- and re-mon- modernize how Nvidia does work all together, okay?

So number one, if you can use uh Open AI and Anthropic, I would highly recommend you use it.

And the reason for that is because it's useful.

It works really well.

It's getting better all the time.

And it's, you know, as a As you know, large language models is the technology inside, but Claude is a product and Claude code is a whole harness around it.

And that harness is getting better all the time.

The model's getting better all the time.

It's not It's not likely that anybody open source go to GitHub, download something that's going to work nearly as well.

Okay?

So So I I highly recommend it and we do um use off-the-shelf frontier AI models.

The question is why is it there that we're advancing and working so hard on open on on open models?

The reason for that is because language models are very important because they represent the the codification of our intelligence.

And And um we want to automate ourselves, especially is very important part.

But you you you need to know that know that AI is about learning the representation, the meaning, the structure of information.

And so the question is where is information?

Well, we're living in information right now as we speak.

The reason why there's structure is the reason why every day you show up is kind of largely the same.

Otherwise be like practically white noise.

And so the fact that biological systems and physical systems have structure and from that structure I must be able to learn higher-level representation.

And if I can learn the representation, then I could manipulate it.

Then I can Does that make sense?

And so, just because I can learn the representation of of language, I can then generate it, I can manipulate it, you know, I can put it to use.

And so, I want to do the same thing for chemicals and proteins and genes and physics and physical systems, robotics, for example.

And so, notice the way you represent all of those things are fundamentally different the structure is And the dimensionality is different.

How you train it is fundamentally different, right?

Because you don't have a whole bunch of internet corpus of human language on it.

And so, you you've got to come up with new new strategies for all of that stuff.

And so, we decided that we would dedicate ourselves in some fundamental pillars of And because we have the company The company has the talent and the scale.

We have the ability to put the first piece of artifact out in the world, data model, how to train it, in several different domains.

And so, some of the domains I care very much about, one of them is called, of course, NeMoTron's language, and I'll come back to that in a second, why does it we're doing it.

And then second is BioNeMo, that's for biology.

And And we have Alpaca Myo, somebody mentioned it earlier for autonomous vehicles.

Basically, artificial intelligence navigation.

And then And then we have Groot, which is a humanoid articulation robotics, general artificial general robotics.

And And And then we have climate science.

You know, basically, mesoscale multi-physics, okay?

And so, all of these different area these different domains, we decided that that we should go and pioneer it.

And the reason for that is because otherwise, the scientists in these different domains, they simply won't have the scale and the technology necessary to go build that foundation model.

And so, we decided that we would do that.

Okay?

So, that And as a result of doing that, we activated healthcare, we activated life sciences, we act We're working with every single self-driving car company in the world.

Doesn't matter which one it is.

You know, there's Nvidia in there somewhere.

And so, we're we we enabled that entire ecosystem to really flourish.

And And we're working with robotics right now.

And you know, so on and so forth.

Okay?

Without us making that first effort and building a foundation model, it's hard to activate the whole industry downstream.

And so, it's about really about expanding AI and and uh democratizing this capability.

The The reason why we do language models is because two reasons.

One, there are too many too many societies where the scale of their language is not big enough for somebody else to decide to make it a high priority.

They'll understand Sweden Swedish.

But, making Swedish a top priority is not not not likely because the country is is big, but not so big.

Uh Chinese, of course, well taken care of.

Uh Indian, certain dialects very well taken care of.

But, as you know, you have like 230 others.

And so, there are too many others.

Unless you deeply care, it's never going to be great.

And human intelligence, no matter the size of your population, uh you somebody should care.

And so, we created a large language model that's near frontier.

NeMo Tron is close to frontier.

And we we make everything available so that if somebody wants to then fine-tune it into whatever of their choice, they got no trouble doing that.

Okay?

And so, And then the second reason is very important is because we want to also take these language models and fuse it with the domain-specific models because of human priors.

So, for example, Alpaca Mayo is a language model fused with a uh world model.

And so, on the one hand, it's really designed to detect cars and roads and things like that, but on the other hand, we also believe that if the AI model if Alpha Mayo, the self-driving car model, can reason, reason like a human, and it could reason with human priors, then the number the amount of experiences it needs to have before it could be an extremely good and safe driving car is dramatically reduced.

The amount of training data is reduced, and we've proven that.

Alpha Mayo is probably one of the most effective self-driving car systems in the world, and it's really only experienced, you know, a few million miles, not billions of miles.

And so, that kind of tells the system actually works.

Okay?

So, anyways, I just gave you a long-winded answer for I broke it all down.

You can't just ask a simple question. >> What we talked about >> But open models is really important.

And then and one one more thing, okay?

If there's not That wasn't enough.

One more thing.

If you want if you care to have AI be safe and secure, it has to be open.

And the reason for that is you can't defend against a black box, and you can't secure a black box, and you can't put a black box of some incredible capability into your system when it's completely completely opaque.

Now, of course, there's a lot of different ways you could solve the opaqueness.

For example, you could say before it do does anything, you have to reason about it to me step by step.

Before you do anything at all, you have to come up with a plan, you have to reason about it step by step, but you could always lie.

And so, so the ability for the the nice thing about transparent systems is that then, you know, we everybody gets to interrogate it.

If you have a transparent system, then researchers get to use it.

If you have a transparent system, open system, then the way you defend against super agentic systems in the future for cybersecurity is obviously not to go into a battle of who gets the better one.

You know, you come up with some model model 7.0, and the only way I combat against that I'm completely vulnerable until I come back with a 8.0 and then you got to come back with a 9.0 and we just go back back and forth driving each other nuts.

And obviously that's not that that's obviously not the smartest way to do it.

The smartest way to do it is you're going to you're going to create these incredible cybersecurity systems and or you're going to these cybersecurity threats and what we're going to do is we're going to have millions, billions, swarms of cheap AIs and we're going to systematically surround it.

And so it's kind of you know if you will a giant dome.

So for example Numenta Nano is being used for cybersecurity.

And so all these cybersecurity firms take Numenta Nano because it's so fast and so so cost effective you can train it to detect cyber cyber attacks and then just deploy trillions of them.

Yeah. >> Um on the topic of open scaling, you know, we hung out in January and we >> I feel like you know that one scene in Thor?

Do you remember he was just hanging and he kept rotating in that direction?

It's zero gravity.

Here at AI Coachella we got no gravity.

You know in Thor Ragnarok?

Do you guys remember that? >> We can move a little bit back so you can see this.

Okay. >> You guys don't watch movies? >> Well we have a whiteboard too if you want to get off and walk but >> Um >> So in in in January we met we talked about this topic open scaling we talked about bottlenecks.

We talked about um data is one bottleneck, computer is another bottleneck.

Um you know there's at least one experiment that uh we announced at GTC today which was the coalition scaling idea.

The second is on how to improve utilization on compute which is increasingly scarce.

Uh it came out last week that there was a memo at X AI that said their uh Memphis cluster pool is running at 11% MFU utilization which I think like corresponds to something like 11 billion or something of unutilized MFU flops.

Like how can the open space Like maybe you could talk a bit about why Coalition scaling as an experiment we're trying and we have Ryan coming actually in the final office hours to talk about progress and then how do we get utilization to be better for open the open ecosystem when you don't have full like sort of fully integrated companies that can optimize up and down the stack? >> Yeah.

Um Did you guys Do you guys know know what MFU is?

And so MFU, do you guys know?

Do you guys not use that anymore?

So, MFU uh is just simply wrong.

Okay, it's a it's the the amount of the percentage of flops, basically, that you consume while doing your work.

All right.

Model flops utilization. >> Yeah.

And so so it's unfortunately with every metrics, depending on what you measure, you could be measuring the wrong thing.

And so let me tell you why.

Uh if you ask me, do I want to be at at high MFU personally or low MFU?

I would like to be at low MFU.

All the time.

And the reason for that is because I want to be so smart I'm over provisioned for the work.

Okay?

Because I'm over provisioned, I got so many flops and sitting idle. >> Mhm. >> And the reason for that is because the way the computing works in these large-scale data centers is you have flops, you have memory bandwidth, you have memory capacity, you have network capacity.

At any given point in time, something is bottlenecked.

At any given point in time, something is bottom bottlenecked.

And so what you want to do is you want to provision every over provision on everything. >> Mhm. >> So that you could avoid Amdahl's law.

Otherwise, you're fighting Amdahl's law all the time. >> But then if you're provisioning for peak, not your base loads, then you're going to have a bunch of those flops sitting while while over provisioned when you don't need them because it's spiky. >> But there at the right time, it goes to 100% MFU.

But only for a short period of time.

And if that short period of time you don't get you don't get all that over provisioned flops, then during that short period of time becomes becomes a long period of time. >> And so what are you seeing for teams that are trying to optimize >> and and flops are cheap.

Now, flops are cheap. >> H100s are going up in price. >> Well, not because of its flops, but because of H100, Hopper, you know, it's it bandwidth, its architecture, it's everything else, not just its flops. >> What what is So should we think about compute as not a scarce resource? >> No, no, that's not that's not the question.

It's like this. >> All right. >> Uh uh when you when you ask about a car, uh back in the old days when we were unsophisticated, we used to say, "How many horsepower is your car?" >> Right. >> But these days who does that?

So what's the right measure you think we >> Performance. >> Uh and what what when you tell the teams, "Guys, this is the perf we got to hit next year." What are you finding is the eval you're you're reaching for more and more? >> to come up with a real eval, a really serious eval.

And that real because otherwise you'd be like improving your flops, you know, it's it's no you you figure out something that that you guys can improve, and you're improving that number, it doesn't make you smarter.

You're improving that number, it doesn't make you more successful. >> Yeah. >> And so it it's there's nothing wrong There's nothing wrong with having a lot of flops.

Um but it's not the complete necessary, not sufficient, that's all. >> In one sense, you could think about the output of tokens as intelligence.

So it should be some unit of intelligence per watt? >> Yeah, yeah.

Notice Notice the tokens per watt is more than flops. >> And in fact >> we know that now because for a decoding these large language models, the single most important thing for generating tokens per watt is actually the aggregate bandwidth across the NVLink 72.

And the MFU is incredibly low because the prefill is not that much.

It's mostly decode. >> You can decouple decoding and prefill. >> It's disaggregated.

And so notice I just delivered incredibly high tokens per watt with extremely low MFU. >> MFU.

But but but not all tokens are born equal, right?

And so how do we account for that?

Like when you design the systems of the future, how do we How What is the right way to measure without a standard measure of intelligence when you have coding tokens being more valuable for what then I don't know some other kind of token.

Does Does that Does that question make sense? >> Makes perfect sense.

You always have to come back to not just optimizing for SAT scores.

You're optimizing for something bigger.

And so So that's that's basically it.

It's the same idea.

You're You have to decide what evaluation, as you know, eval, how you evaluate success matters a lot in how people perform.

And so what Nvidia does extremely well inside the company is the systems that we create for evaluating architectures.

And And flops is too too contrived.

Because if it was that easy then >> And so do we have >> I wouldn't be here. >> You have a hard job, which is to try to design an index of different intelligences.

Right?

Cuz you got like I think when when I'm building when I'm when our teams are researching on the Nvidia architecture, you've got one lab doing coding and another one pushing the frontier of superconductivity and so on.

And they They all have completely different evals they're measuring for, but they're all using Nvidia chips. >> Yeah. >> So Like how do you How do you solve that problem when your customers all have their own evals? >> Yeah, but the architecture of the underlying platform That's why it's so hard.

And And And here it is true it's that is that hard.

The problem is this, if you if you build something that's too overfit for something, you could be incredibly good at it.

And so you're overfit for this one problem, you're insanely amazing at it, but then the problem is is that market, you know, that problem space may not be good may not be big enough to find a sufficiently large R&D.

Right.

And so you want to be good at many domains, multi-domain.

On the one hand, on the other hand, if you're good at everything, then you're good at nothing.

You became general purpose.

And so that writing that balance, by the way, is our district.

You know, it's that's what I do for a living.

What should we not do?

What should we double down on?

What should we 10x on?

That you know, that's that requires some amount of vision, strategy, you know, some amount of trial and error, some just personal enjoyment and entertainment, uh you know, iteration.

All of that. >> Can we talk about the canvas of Feynman, which is a trip I'm very excited about, but it's been hard to get info on it.

What's the canvas telling you now about what that your art piece is going to look like for the Feynman? >> Well, I can tell you the journey that we came on.

And so So if you look at Hopper, Hopper was designed for a problem space that was rather new.

It was called pre-training.

And so pre-training uh came along and we we get came to the conclusion that that um uh although the generation before it was was uh fairly significant already, that we should build even larger ones, tremendously larger ones, larger than any of the largest science scientific supercomputers in the world. >> Mhm. >> Okay, so that's a very big deal.

That that the the largest supercomputer in the world was about 350 million dollars and we we thought, you know what, uh pre-training is going to be such a large domain and such an important problem, we should design systems that could be multi-billion dollars.

At the time that we're thinking about doing this, this sounds insane. >> Mhm. >> You know, you you would have precisely zero customers.

And the reason for that is because the most expensive thing that has ever been sold was 350 million dollars and you're building something that's multiple billions of dollars.

So you're you're building for a precisely a marketplace of zero.

But we went and did it anyways on first on first reasoning.

And so Hopper was designed for pre-training and that was a great call.

The second thing that we did was we said, okay, well, after after training, we'll keep we're going to keep making training better, but the goal is not of AI's in training.

The goal of AI is inference. >> Mhm.

And and and what kind of a system would inference really care about?

And so we created a system called NVLink 72.

And the reason we did that was because decode the in in in processing the neural network, there's the prefill, which is really context processing and things like that and attention processing.

And then the decode, which is generating all these tokens.

The generation of the tokens requires really high uh memory bandwidth. >> Mhm. >> And the amount of memory bandwidth you need is way more than one chip can possibly provide.

And so we said, "Why don't we gang up like 72 of these things?" And so we had to invent all kinds of new systems for switching and interconnects and uh create all kinds of new 30s and and we created essentially the world's first rack-scale computer.

It's called Grace Blackwell NVLink 72.

The speedup over the previous generation, 50 times.

In 2 years, we improved something by 50 times.

Moore's law would have improved it by 2x.

Okay?

So the architecture and the insight uh was fantastic.

And decode and inference and large language models and token generation, it you know, all of that kind of landed at exactly the time that Grace Blackwell came out and boom, took off.

So Grace Blackwell, uh another incredible generation.

Now, the question is what happened to Vera Rubin?

And what's the big idea?

Well, the big idea is that that the goal isn't just to think, the goal is to do work.

And so Vera Rubin's design for agents.

And so the question is, what is the compute pattern?

What is the processing pattern of agents? >> Mhm. >> And agents, of course, uh you have to you have to load uh a fair amount of memory, uh long memory, he's got working memory.

So long-term memory we put into storage and we got that storage needs to be able to directly communicate with the GPU.

You can't be copying copying the that the data off of the the the network storage, but you want the storage to be connected right into the processor itself.

And so we we have we have storage that's connected to to the fabric.

We have We have we're going to use a lot of tools and so CPUs are going to be really important, but the CPUs of the last of the current generation was really designed for cloud computing.

And so you have these CPUs with hundreds of cores like, you know, 200 cores.

Well, the CPUs of agents because because the AI is this multi-billion dollar system and it sends off uh an instruction to use a tool and that tool is going to run on the CPU.

Meanwhile, this this computer, this GPU supercomputer, this multi-billion dollar system is waiting for this one CPU.

And so that CPU really wants to have extremely low latency.

So we designed Vera, which is the for for current generation for single-threaded, you know, multiple core single-threaded code, it is by far the most most performant.

And so we created a CPU just for that.

Notice Notice the way you solve this problem intuitively is you you kind of think about what is the computing pattern, how's it different than the past, you have to have some mental model about it and you create a system that you can you can go and go build to run that.

And so So now agents are here.

We're going to run that on Vera Rubin.

And and and hopefully when Feynman gets here it's going to be it's going to be like all software.

Age We call them agents today, but you know, it could be modules in the past or you know, submodules.

And And so in the future you're going to clearly have systems of agents and agents with subagents and subagents with subagents.

And And so you're going to have you know, this swarm of agents.

And And what what kind of computer, you know, does that does that manifest?

And so that's that's likely what Feynman's about.

I have one more follow-up question on that, which is, you know, one of the things you've always done well is kind of spot bottlenecks one generation ahead and then try to sort of pre-solve for that in the supply chain.

A year ago that was photonics and that became a huge solution.

As we look about look at energy as a bottleneck, you know, copper wires, literally copper wires are one of the the transmission sort of bottlenecks.

How does that get solved in your view? >> Energy is just everywhere for well first the first thing that we could do that that is in your our control, you know, as with everything in life, whatever the problem is, whatever the external external concerns are, you should do something that's in your control and in our control is energy efficiency.

So if you look at look at tokens per watt, we improved it by 50x and then we'll have to keep on improving it by you know, by significant factors and it compounds.

So that's that's the first thing we can do.

We can control that through co-designed architectures and things like that.

And the second thing that we could do, the thing we could inspire people to and that's through a lot of education, inspire the ecosystem to get ready for this and and and and I've been over the last last half decade helping people understand the amount of compute that's likely to be coming.

And I just told you guys something about how I reason through how much energy is going to be necessary.

The amount of energy that we need for compute for computing is likely you know, probably a thousand times more than we currently have and that's an enormous amount of energy.

However, the way to think about that is in the future computers are going to be two things.

It's always going to be generated because it's intelligence is contextually aware.

So it's going to be generated and the number two is going to be continuous.

And so you get this generative computing in a continuous way compared to pre-recorded retrieval based computing that is only initiated on you know, per use.

The question is how do you how do you think about the amount of energy necessary for that?

So I I think if you if you say we need a thousand times, I I be surprised if we're off by a couple of orders of magnitude.

And you know, so we need a lot more compute, we need a lot more energy.

And so you got to go and explain this to people.

And so I I you know, I you got to explain it to people in a way that's kind of common sense and and and they can observe it and there are you know, indicators along the way that that in fact this is happening and and notice just as I was breaking it down for you guys, you know, I'm reasoning about it for you so that so it's common sense to you.

And so the amount of energy is is high.

And then lastly, uh the source of energy.

I we there's there's there's a there's all kinds of sources of energy, but unfortunately, because of of great concerns about about um uh the cost of sustainable energy, we under invested in in sustainable energy.

Uh but this is the best time ever in the history of humanity to go and invest in sustainable energy.

And the reason for that is because the market forces are so strong.

Back in the old days, you needed government subsidies to go build solar farms and government subsidies to go build nuclear plants.

And now, you you can just market will pay you to do it.

And so market forces are so powerful right now.

This is our best chance to upgrade our grid, our you know, archaic grid, um add add sustainable energy of all kinds and you know, this is a great time. >> In terms of education, what I've learned as well, we designed the class for the students here.

Turns out a lot more people, especially a lot of investors and capital allocators are watching.

This is what I was expecting. >> Oh, shucks. >> Right, let me put it up.

Yeah.

Um and so if there's >> I'm just kidding. >> If there's education you'd like to do to that audience, feel free to drop in it.

Yeah, I Repeating yourself after a while with with capital allocators can get >> No, I I don't mind. >> So if you'd like to transmit, feel free feel free to um What is the next question we should take?

The question is how best to spend their mental faculties over the next few years. >> Yeah, I so so first of all on the pain and suffering comment, um there there's a there's there's some kind of so there's some advice that says you should you should choose what you love and what you're passionate about.

That's what your career should be.

And and I think that's terrific.

I think that's terrific, you know, if you're if you happen to to to know what you're passionate about, if you happen to know what you love, um uh but I think there are a lot of people who don't know what they're passionate about and they don't know what they love and the reason for that is because nobody knows everything.

How could you not How could you know what you don't know?

So in a lot of ways um the idea that you would only do you would only choose careers that give you passion, that gives you you know what it gives you get makes you happy um it is a bar that I think is too too high, number one.

Um and the reason for that is because whatever you decide to do for a living, whether it's you found something that you're passionate about uh or this is your job.

And in my case, you know, used to be cleaning toilets and busting tables, it was my job.

And I will do the best I can in my job.

Whatever you give me as a job, I will do the best I can possibly do and I do that today.

And now th- there's a misunderstanding that that somehow CEOs we love our job and and and you know, many say oh I I'm passionate about my job.

I love my job.

They're they're lying.

There there there's not there's not one CEO who who I who can say that, you know, from the moment I wake up to the moment I go to bed is just zippity doo dah.

I The fact of the matter is uh I really love doing 10% of my work and 90% of my work is hard.

And I do it to the to the best of my ability anyhow.

And I suffer through it.

I literally suffer through it.

I prefer to do something else, that other 10%.

But that other 10% there's only so much quantity of that and and every company has abundance of problems and there comes in different types and you're going through life you're going to have abundance of problems that are going to come in different types and you just have to learn how to condition yourself to want to get to a better state no matter how hard.

To get better no matter how hard and that's suffering.

You know, you're you don't like doing it but you're doing it with all your might anyways.

What do you call that?

That's suffering.

And so so I think that when you when you suffer and you have to benefit of struggle and you you're being presented with many opportunities like that it teaches you resilience.

And when it when the time comes and and the world or your family or your company or your colleagues they need you to be tough.

They need you to be resilient.

They just need you to be able to fight through it.

You can't have though you don't have that character about you.

You don't have that muscle unless you've gone through it a whole bunch of times.

And so you know, I'm I'm advising that that that you not you not seek for just joy that you also seek for some some pain some suffering because you're going to need it someday and and then lastly it's also it's just your job.

You know. >> As preacher Juan once said, don't wake up with a loser mindset.

The question is what's your favorite order at Denny's? >> Yeah, Corvallis really should have a Denny's.

Um Well, you know, after all these years frankly it's about time, right?

And so there was that there was that that one Chinese restaurant.

Um and uh and Woodstock's of course, right?

Corvallis Woodstock's Pizza.

It's still pretty good, isn't it?

Woodstock's? >> It's all right.

I like American Dream better. >> American Dream's better?

Okay.

All right.

I'll I'll be back there soon enough.

And so so um Uh Denny's I would say uh surprisingly the fried chicken is really good.

So, you know, it's uh slightly on the on the sweet side.

Uh Superbird is excellent if done right.

And um uh and then another one, if they're willing to make it for you uh make it like a Superbird.

Okay?

But it's a grilled ham and cheese with tomato and mustard.

And if they're willing to make it for you, that they're willing to make it for me.

And so But that's because I'm not not because Because I'm I'm a alum.

They know that hey, you used to bus tables here.

Yeah, yeah.

We'll make special for you.

Uh but but th- those are all good.

You know, the the Grand Slam, you know, I enjoy it.

I like a pigs in a blanket, so that's pretty good.

Um there's a whole bunch of stuff.

Couldn't I go all day?

I I Denny's I had my first fudge hot fudge sand- uh sundae.

I had my first uh apple pie with cheese on top.

I I That's like for for a Chinese kid is like, what is that about?

That doesn't make any sense.

And but now you think about it, makes perfect sense, you know, apple and cheese.

But anyways, I I had a whole bunch of It was I had my first milkshake when I was at Denny's.

Um I had a whole bunch of firsts, yeah.

Denny's Denny's was uh eye-opening for me. >> Man, before we lose it to the to memory lane, next question, please. >> Mhm.

Those are some of the most important questions. >> Agreed, yes.

No questions about your thoughts on adversarial countries getting access to uh Nvidia chips. >> Uh first of all So, you you know what we we make for a living?

We make GPUs.

And and um uh GPUs are used for uh video games.

Uh they're used for uh delivering soy sauce.

They're used for medical imaging.

Uh if you uh I had a CT scan done done yesterday, I'm fine.

Uh but that behind it was Nvidia.

Uh Nvidia's in every single medical imaging system in the world.

Uh and uh and so, the question is what is it that you build?

Um what I'm what I'm fundamentally against, and it makes no sense it makes no sense to this moment is to compare Nvidia GPUs to atomic bombs.

There are billion people with Nvidia GPUs.

I advocate Nvidia GPUs to all of you.

I advocate Nvidia GPUs to my family, to my kids, to people I love, but I don't advocate atomic bombs to anybody.

So, that analogy is stupid.

And so, so if you start from there, you can't finish a thought.

If you start from believing that, you can't finish the rest of the thoughts.

Um, the second the second idea that I I consider completely ridiculous.

Uh, why should American companies go compete in foreign countries?

You're going to lose it anyways.

You're going to lose it anyways, so why go?

Well, if you guys all apply that same philosophy, why wake up in the morning?

And so, I don't I don't prescribe to we are going to lose anyways.

I don't prescribe to that.

If you want me to lose, you're going to have to deal it to me.

But, you know, I'm going to have to put up a fight.

And I put up a lot of fights over the years.

I'm doing okay.

And so, so I think that and and and as you know, the battle, the competition serves markets and enhances enhances your company.

I'm not a little bit afraid of having to go and compete in the marketplace.

But, the idea that I'm going to lose anyways, so why go compete makes no sense to me.

And then lastly, the idea that that somehow we should deprive certain countries of general purpose computing and we can all acknowledge now Nvidia is a general purpose computing company.

I just gave you a whole bunch of general purpose use cases.

Is a general purpose computing company to be deprived of that so that one or two companies could benefit from depriving other people of it.

That makes me makes no sense either.

Why should one industry suffer so that another one company benefits another one or two companies benefit.

Entire American The The American technology industry is one of our national treasures.

You are going to be part of it.

And if I do my job, when you are done graduating, you're going to graduate into the mightiest computer industry and the mightiest industry in the history of humanity.

But, if we give it up for some reason, or we through policy decide that we can't go and sell and concede 2/3 of the market to the 2/3 of the world to other companies, by the time that you graduate, you would have gone into a shell of an industry.

That shell of an industry we've seen before.

A long time ago, the same arguments when went against America in telecommunications.

Today, America has no telecommunications fundamental technology anymore.

It was all Look, it was all of completely policy out of our country.

And so, somebody has to put up a fight for that.

Some of these reasoning systems to to to say that AI is AI's going to come and it's going to be a singularity moment.

That singular That moment the moment it comes, it's going to be the most powerful thing in the world.

It's come to come as a flash.

We have no idea where this kind of come come on Wednesday or Thursday at 7:00.

But, when it comes, it's going to be game over.

Some percentage chance that it'll be the end of society as we know it.

Come on.

We all watch Dune.

We don't have to repeat it.

And And so, I think that living living living their fantasies out, their science fiction fantasies out uh in in in in public uh demonstration, when everybody is relying on their words and believe in their words, is irresponsible.

It is not true.

It is not true that we have no idea how these systems work.

It is not true.

It is not true that the technology is going to some somehow in some nanosecond become infinitely powerful and therefore it's going to take over the world.

It is not true.

It is not true there's no way to defend against it.

It is not true.

These things are all being made up.

And it's made up in a way that unfortunately even harms all of you.

You're in computer science.

You're hoping that when you graduate people care about computers.

We want to create a future that is optimistic about the technology that you are learning to master.

We want to create that future.

We want to make sure that America we want to make sure that everybody benefits from Everybody should have AI.

Nobody should have nuclear bombs.

Can you guys agree with that?

And so okay.

And so so young man young man thank you for triggering me.

I'm just kidding.

Okay, so I'm just kidding. >> I'm just kidding. >> I just wanted to get get it out. >> So we're rational optimist here in at AI Coachella.

So believe in optimism.

I'm going to push back a little bit on a different angle.

I completely agree reasoning by analogy is a problem.

Once you start with bombs you should do first principles.

What we are observing is that compute we are compute constrained in America.

Independent teams startups universities they can't get compute.

So from a preference order perspective shouldn't America get first priority to a scarce resource before you start shipping it off? >> Absolutely. >> But that's not happening. >> Absolutely not. >> There's the gotcha. >> Yeah, absolutely and absolutely not.

And the question is why not? >> Mhm. >> Uh there's plenty of chips.

You guys if some if if the president of Stanford places an order I promise you I'll deliver it.

I have No, absolutely. >> heard it here.

All right.

I had a phone.

Ange Ange This is not funny.

This is not funny. >> We are dying out here. >> no.

This is not funny.

That's right.

This is serious matter.

Um it is not it is not true.

It is not true that people are giving me orders, placing orders, and we're not delivering shifts.

It is just not true.

You got to You got to place orders.

The fact of the matter is the fundamental problem is actually something very different.

The Stanford needs compute.

Science needs compute.

The fundamental problem is the system is no longer built to be able to deliver massive scale compute.

And the reason for that is because just think.

All of the All of the research departments here at Stanford, they're all in different departments.

You all raise your own funding.

You all get your own grants.

Nobody's going to go share their grants, but none of the grants are big enough to have a large enough compute that you use some of the time, but when you use it, you need it to be incredible.

You got The world moved away from those centralized computing environments towards everybody just using laptops.

That's This is today's computing environment.

And fundamentally these All the universities Stanford's not alone.

You don't have a budget for a billion-dollar compute.

It doesn't exist. >> But whose fault is that? >> Stanford's.

And the reason The reason why you have to say that is because I'm empowering When somebody is at fault, you empower them to solve it.

Do you agree?

When you say, "Oh, yeah, it's not your fault.

Son, it's not your fault.

Your failure, it's not your fault." It's not your >> It's talking to me right here. >> You know?

Uh you you You know, hey son, uh you're an idiot.

It's not your fault.

No, it's absolutely your fault.

And And so, by saying that it's absolutely your fault, you're also empowering yourself to solve it.

Isn't that right?

You're empowering yourself to solve it.

And so, the question that you just talked to somebody who kind of feels, you know, I can do something about my future.

Um you're talking to somebody who who's who believes in that.

Okay?

And so if I were Stanford, you just have to you have to find a way to to to change the way you do budgeting, the way you deal with computing.

You have to find a way to aggregate and build yourself a linear accelerator just like Stanford has done in the past.

We need to build campus-wide supercomputers that everybody share.

Now, you could also go and just contract somebody else to do it.

I mean, that's that's all possible.

But you do need to have, you know, a billion dollars.

You need to have some reasonable fund to go be a be build something like this because that's how much it costs.

But that's that's just what it takes. >> I mean, last I checked, we've got a what, $40 million endowment here.

How would you put that to use if you were if you were stepping into >> cut a billion dollars of it right away and give it to somebody as a cloud service and have every single student and every researcher here have access to to a to a AI supercomputers.

I would do that right away.

Now, of course of course, you've got to go plan things.

You don't If you want to buy a billion dollars worth of tomatoes, you don't show up to the grocery store and say, "Hi." And then and then and then they don't have a billion dollars worth of tomatoes and you go, "Aha, you're withholding tomatoes from me." That's just ridiculous.

And so so you know, so you got to do some planning.

And so what you got to do is you got to say next year we need to have a billion dollars worth of computing for Stanford.

And and so if we'll go build it. >> All right, you know what?

We'll move on.

But thank you for that. >> Yeah.

Yeah, yeah, exactly. >> We'll come back to that one.

Yeah, what is the best and worst part of your job? >> When you're when you're CEO of a company, you you have the benefit you have the benefit of of a lot of really fun things.

Like for example, Uh, you really the person who has to conceive of the intersection between vision and strategy and execution, okay?

And so, so you have to live in that in that world and it gives you and when you're a company with capability, and I'm surrounded by amazing computer scientists and many of them from from Stanford, and when you're surrounded with by people like that, when you have a vision, it's very realizable and because you're with amazing people, your vision is more ambitious, okay?

And so, so I think I think that's the fun part.

The not fun part So, and so that fun part, I get to do almost all the time.

I'm always constantly updating my my my view of the future and my vision of the future and and our role in it and and how we ought to reinvent ourselves so that we could, you know, contribute more to that future or or go invent that future in the first place.

And and so, as a CEO, you have you get to live in that world and that's fun.

You're it's very imaginative, it's very strategic, it's you know, highly complicated, there's no right answer.

And in a lot of ways, it's it's creativity at its most, okay?

On the other hand, what comes with that power is the responsibilities for a bunch of people who joined you in that spaceship, that joined you in that in that vessel, and they want to be they want to help you create this future and they're part of your team.

And you feel a deep responsibility for their well-being.

And so, when the company's not doing well or the company in the older days, you know, when we were in the beginning trying to find our way, we probably nearly went out of business, you know, four or five times.

I mean, literally almost went out of business.

And we were on fumes or or we're really flat on our back.

And so, during those times, it's embarrassing, it's humiliating, it's hard.

You don't know what the answer is.

Often times, you're in the dark.

Uh, you're afraid.

Uh, you know, all of those the feelings that that we have as humans just multiplied by, you know, a thousand, a million.

And and you know, when you're a public CEO, your face is always out there and when you do well, people are happy.

When you don't do well, they're fast to tell you.

And and so you're you know, so it's a vulnerable, you know, for me, it's it's a highly vulnerable profession.

And and so you're not naked, but you feel it, you know. >> Question is what's the biggest mistake you've made in the early days of Nvidia and what you learned from it? >> Um Let me let me give you an an example of of what somebody might say and and I will say I won't I'll say that that's not.

And so so anybody who knows our history I would know that the first generation of our products the architecture, the technology we used was completely wrong.

It's not like a little bit wrong, it's like completely wrong.

The fact that that that smart engineers and professionals and we were actually funded and we created this thing and it's like check it out, doesn't work at all.

You know?

And so that that using curve surfaces instead of triangles, no Z buffer instead of Z buffer, four texture mapping instead of inverse texture mapping, we did everything wrong.

We did everything wrong.

No floating point inside, we did everything wrong.

And so we made a lot of tremendously bad choices.

Um and I'll say that that those are technical bad choices, but it led to strategic genius moves.

Um how do you take a company that had that reputation and wasted a bunch of money and a bunch of time two and a half years doing it the wrong way and surrounded by competition and now here we are the only one remain.

Okay?

And so so that that transformation taught me a lot about the importance of technology is important, but strategy is so important.

And so, how you see the world, uh how you approach competition, how do you approach the market, uh how do you conserve resources and apply resources, those those decisions um I learned more in my early 30s through that deep failure and the company almost vaporizing, uh I learned so much about strategy and strategic thinking and and uh maneuvering and things like that, and it's lasted a whole whole long time.

The mistake that I made that I I would say um what was a genuinely straight-up mistake is when the PC uh I uh what what or when mobile devices took off, uh we were approached by very important companies that that are in important in the mobile space uh to work on some mobile devices.

And and um And the choices that I that I made um I I think the answer when they approached us, the answer should have been nah, not interested.

But we decided to shift a bunch of our resources to go build mobile devices.

And um I and I thought that we could add a lot of value, but it turned you know, I I think if I would have thought through it a couple more clicks, uh the amount of value you can really deliver in for for the things that we know how to do and what we're good at is probably marginal at best.

And so, uh I shifted the company to go into mobile devices.

Uh it grew into a billion-dollar business, and and that kind of positive reinforcement, and then shortly after uh during the 3G to 4G transition, uh we were just 100% locked out, and and um uh Qualcomm was the leader in that 3G to 4G modem modem, and that's the most important part of the phone, not the SOC, not computer graphics, not even the application processor.

The phone is obviously the most important part.

And so during that transition, they were able to block us out.

I could have probably called it, you know, to to if you if that circumstance were to happen again, I would have said, "Yeah, it's it would be a really interesting opportunity for a couple years, but we're going to get shut out after that, so what's the point?

Why let's go conserve our resources somewhere else." But the the recovery, so we got shut out we built it up to about a million dollars and then went back to zero.

But the recovery was I took all of that expertise, that extreme low power and energy efficiency expertise, and I shifted all to an application that didn't exist at the time called robotics.

And so all of the somebody mentioned Thor.

Thor is the great great great great grandson of the chip that we were using in mobile devices and that that entire genealogy and all the teams and all the expertise that we we built up was really helpful to getting here.

And so it doesn't That's rationalization.

Going into that market in the first place was a waste of time.

And so that that I think is a strategic mistake. >> On strategy, is there Yes, sometimes strategy is about forecasting so precisely enough.

Is there from a systems perspective, what do you think you updated your priors on what is the forecasting mechanism you developed to give yourself some confidence that like this fog of war here, don't quite know where things are going to go, but generally speaking we're hit like shooting the right direction.

Is there any is there sort of a systems piece of a system design advice you'd give folks on when the shape of the future is not entirely clear? >> Yeah, and and in fact in fact you you used all this the the right words already.

Um the first thing I do is is what am I observing?

What am what am I And based on what I observe, let's reason about it back to first principles, break it all back down, and ask ourselves, so what's going to happen next?

And first, so what?

Is this a big deal?

Hey, deep learning, computer vision, AlexNet, you know, big deal.

Is that a big deal or not a big deal?

And so the big deal part of it is, my goodness, in just one, you know, here here's two engineers, right, Alex and and Ilya, and and and Hinton, of course, and they came up with a neural network model, and boom, it crushed the the computer vision capabilities of all the computer scientists, you know, decades before them in one shot.

And so is that a big deal?

Is that a big deal?

Um uh the the the step up in in quality of and performance was a big deal.

Now, the next question is, so what's going to happen next?

How far can you take it?

And then if you could do it in this way, what else can you what else can you solve?

And if if this was able to solve some really amazing problems, what does that mean to computers and computing?

And so you just keep asking yourself these questions, right?

And so you're just iterating it like that all the way to first principles, and then from that you create a mental model about the future of computing.

And where is it going to be?

What can it do?

For example, self-driving cars and robotics.

How large would models become?

And if if so, what would computers look like?

What would processing neural networks?

How's that different than processing, you know, floating point numbers and integers and first principle mathematics?

You know, we express everything in FP64, FP32, but obviously neural networks don't have to do that.

And so so you you reason through it kind of like this.

And then you build up a mental model of a future of a, you know, of the future, and then where your your company, where you are going to be within it, and then you just work backwards from there.

And and then and then now the question, of course, is you could be wrong.

And oftentimes you're, you know, if you reason about things properly, you're not completely wrong, but you're not completely right.

And so, I tend to I tend to be very comfortable saying, "Okay, these are the things that that will likely happen.

And these are things that will absolutely happen.

And these things may happen.

And based on that, I think we ought to go in that general direction, and we'll feel our way through." And now that now that the skill of of building companies then, of being successful along the way, is you're going into this direction, and it's going to take energy, it's going to take time, it's going to take money, and and everything that time, energy, and money, that takes away from something else, right?

So, the cost the the the opportunity cost of pursuing a strategy is the real cost.

And so, you just got to ask yourself, how can you be smart enough such that the opportunity cost is reduced, and your optionality is increased?

And so, you're trying to think through all of that stuff all the time.

You know, there's no simple answer, but but in a lot of ways, you're trying to get the journey to pay for itself. >> Given everybody's going to mob you for more signatures, that's where we're going to end.

Thank you.

Thank you very much.
