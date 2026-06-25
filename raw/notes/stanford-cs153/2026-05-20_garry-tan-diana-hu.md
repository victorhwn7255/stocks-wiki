# Stanford CS153 Frontier Systems — Garry Tan & Diana Hu: "The AI Native Company: How One Founder Becomes a 1000x Engineer"

**Speakers:** Garry Tan (President & CEO, Y Combinator) + Diana Hu (General Partner, Y Combinator) · interviewed by Anjney Midha (CS153 co-instructor, a16z)
**Channel:** Stanford Online · **Upload:** 2026-05-20 · **Duration:** 47:14 · **Views:** ~66,937
**URL:** https://youtu.be/Lri2LNYtERM
**Source tier:** Tier 5 (book-talking — YC portfolio + agentic-coding evangelism; Garry demos his own open-source tools G-stack/G-brain). Founder-marketing magnitudes ("1000x," "$1-2M rev/employee," "0→tens of millions in a year") are directional, not data. Discovery-only; spoken numbers soft → verify at primary.

## Transcript (Tier 3/5 — not a primary source)

We are super lucky to have with us today Garry Tan and Diana Hu from YC. >> [applause] >> Um before we dive in, I'm going to do a couple minutes of in uh sort of warm up.

This is a really special lecture because for for a couple of reasons.

One um this class CS 153 which as you know Mike and I started teaching 4 years ago which was security at scale uh small group 50 people was inspired but is sort of a composite of several different classes that have been taught at Stanford by Silicon Valley leaders.

And when I was an undergrad sophomore year Peter taught um Peter Thiel taught taught the first version of how to start zero to one.

That it was CS 183 how to start a startup and that became the book zero to one.

The following year YC taught of a version of that class uh that Sam put together.

And Garry was at YC at the time I or I think I had just started Initialized, right?

And uh and so those are the spiritual descendants of this class and then there's CS 43N which was Terry Winograd's class we've talked about that was computers and the open society which was the first freshman seminar I took.

And so over the years we've tried to you know sort of take the best parts of all those classes and and bring it together in 153.

But I think it's just really poetic to have Garry back because based on many of the you know things Garry learned here at Stanford he went out and sort of took the spirit of Stanford out to Silicon Valley um and to have him back and be able to talk about you know um all of his work and and now with Diana helping to update some of the the the sort of YC philosophy that we're going to we're going to talk about, it's sort of a closed the loop moment.

So, thank you guys for coming back.

It's really appreciated.

Yeah.

Thanks for having us.

Oh, no, this is this is the fun part.

So, um I'm going to let you be- before we sort of dive in, I I'd like to give a couple of minutes of sort of context on why I think this is an important lecture for you guys.

So, as you know, 153 is a systems class.

You know, you've heard up and down the stack from uh land power shell and energy like Scott Nolan at General Matter to the chip layer.

We had Jensen last week.

Um, there's a full rewrite of systems going on to unblock bottlenecks on frontier progress right in the world.

Um one of those things that you need that we need to unblock bottlenecks on is capital.

And uh as you heard from Ben Horowitz a few weeks ago, you know, Mark and Ben came up with a system to try and scale the deployment of capital in Silicon Valley over 10 years ago and are now thinking through how to update that system.

And and YC is very similar and I'd like to connect the dots between lecture one where we talked about the compute bottleneck, right?

And if you remember, one of the reasons I I talked about how bottleneck is uh compute is a bottleneck today is because we're in the pre-standardization of compute era.

And if you zoom back to the Industrial Revolution, one of the things that allowed this very important thing called electricity to become a stable sort of resource uh a piece of infrastructure that lots of people could develop on and access was the development of standards.

Right?

One of them was AC/DC.

And then we had institutions enforce those standards.

Um, one of those institutions was would utility companies that developed a grid to coordinate the production, demand, and supply of electricity.

In the capital world um when I was uh getting showing up when I showed up in Silicon Valley 20 in 2011, we were in the pre-standardization of capital of venture capital.

It was a complete mess.

You know, there were a bunch of VC firms who were all trying to do their own deals and figure out how to negotiate with founders and so on.

And into that mess stepped um Paul Graham and Jessica Livingston and introduced a new standard for how capital should be allocated.

And that was called the SAFE.

How many people have heard of the SAFE?

There we go.

Okay, so this is living proof.

The At the time, it wasn't legible to me how profound the SAFE was.

It was basically a two-page legal document that YC put up online and said, "Here's how we're going to fund startups." It's called the SAFE, Simple Agreement for Future Equity.

And at the time, I was like I was a founder uh sorry, a student here and I saw it and I was like, "Okay, whatever legal document." In hindsight now, it's so obvious to many of us in the ecosystem that that was a pivotal moment in the history of Silicon Valley, where you know, the YC team saw what was going on, realized at that point there was another um we we were living through the rise of the cloud and SaaS era, right?

AWS and GCP and so on had started to make compute uh quite accessible, and that had reduced the marginal cost of innovation in the Valley.

But but venture capital was still hadn't caught up with that era.

You know, it didn't cost much to produce software, and so there was a sort of moment of abundance we knew we were going to go through back then, but to get capital out to innovators like you guys, there was so much there there was a there was sort of a venture capital bottleneck at that time, which now seems cute given the numbers we're we're living through today, but at that time it really did feel like it was hard to get time with VCs and get good deals and so on.

And so when into that mess stepped YC and published the SAFE, it became a standard for how early-stage startups um you know, were going to be funded and then by enforcing it YC became an institution that standardized seed stage funding.

Um, and and I think, you know, the the arc of Silicon Valley would have looked very different without that one document.

Okay?

And so as you as we it's very obvious to me as at Amp, we you know, we live through this every day on the compute side.

We might even at some point open source a standard agreement for future compute.

Um, something like that, but you know, we look to what YC has done as a somewhat of a spiritual uh, ancestor for the work we're doing.

And so it's very cool to have you guys back.

Within that context, I hope, you know, this this gives you a little bit of you know, connect the dots moment for why lecture one and and this lecture are parallels and systems design is not just something you do in engineering.

You you can do it in any uh, domain you're in to try and accelerate the pace of progress and unblock bottlenecks.

Is this making sense to people?

Can I get a yes?

Come on, it's spring quarter, guys.

Can I get a yes?

Yes.

Okay, thank you.

All right.

With that, over to you guys.

Thank you so much for coming.

Why don't we start with, you know, introductions about yourself, how you got here, and then you can dive in.

Actually, hey hey everyone.

I'm Garry Tan.

Uh, I was a Stanford class of '03.

I took a lot of classes in here.

I fell asleep in this lecture hall a great many times.

Thank you so much for bringing me back.

This is it's great to be back to the farm.

And uh, any every time I come back to the farm, I'm like you know, uh, sort of shocked that I get to be up here uh, because like it I feel like I just blinked and I was in your seat.

And uh, you know, zooming out, that's actually desperately what I want for every single one of you.

It's like, how do we like you you know, what we're talking about here is there's a grand shift.

Like all those historical things, like literally the new standards are being established right now.

And there are people in this room who are actually going to be the people who establish those things and then Diana and I and the team at YC we're hoping that we're you know the safe was a legal instrument.

What we're going to talk about today is actually code.

And not just code.

Mark down is code.

Like literally the new in you know we're going to link it all the way over to what a startup is, what people in this room are going to be spending your entire lives uh building the railroad for the rest of society over.

Like you know for our our generation we were building the internet and we were building mobile phones and we were building social networks and your generation is going to create the cognitive layer for all of society and this I mean what we're talking about is just like stuff that we're like these are our hunches even.

Like you guys are going to go and actually build it and so you know thank you for bringing us back.

I mean Diana do you want to introduce yourself?

Uh thank you for having us.

I'm Diana I'm one of the general partners at YC.

And we are living through a exciting time as you all know with what all the capabilities with AI is unlocking and we have a lot of interesting things to share for all of you in this lecture.

We've seen unprecedented growth from a lot of the companies in our portfolio that gone from zero to tens of millions in dollars in revenue one year which is impossible before.

Within a year it would have taken four five years to get to basically series B level traction. >> And like hundreds of millions of dollars in capital.

I mean it's just a different moment right now. >> Different world and we're going to tell you how these founders have done it and we're going to go through really what it means to build a company now to be AI native.

So with that I mean it's a pretty packed lecture so we're going to just get right in.

I mean AI is going to change the unit of production like you know when I was sitting in your seat I knew that I needed to raise money, I needed to hire a lot of people, this is about me learning how to like, you know, create a new cult, like, you know, Palantir was like that.

YC, you know, ultimately it's a religion, right?

Like, this something that we believe that nobody else believes yet, right?

That is still true.

All the things we're going to talk about like, a team is still valuable, human beings are still valuable, but it's not going to be just humans, it's going to be humans in concert with agents, with memory and eval and a customer loop.

So, by the by by the end of this talk, you're going to understand what we're talking about.

Right now, it sounds like a bunch of buzzwords.

We don't want this to be a bunch of buzzwords.

We want you to take these ideas and actually implement them and remake society and we think you will do that.

Um, let's see.

Yeah, in 2010 like, I mean, I'll tell you my personal story.

In 2008, I got into YC, we raised about $4 million, I hired, you know, 10 people, we created Posterous, which is a dead simple blog platform and you know, we sold that to Twitter 3 years later for $20 million and honestly like, I was able to create like everything, all the software we made over 2 years with 10 people and all that capital, but me with a $200 a month Cloud Code Max plan.

And anyone in this room could do that and it it didn't take like 2 years, it took about 5 days, right?

So, I experienced that speed up recently, you know, I created Gary's List and then that caused me to create Gstack.

We're going to talk about what those things are, but you know, as Diana said, like, we're in 2026 now and so a six-person team can hit 10 million in revenue with just just the things that we're talking about today and a lot of you already know this, so it might be a review, but for some of you, this is like some astonishing good news.

Um, you know, so let's talk about Gstack.

This is something that I discovered, late last year, I saw Steve Yegge, a famous blogger and engineer.

I believe he was an early Googler.

He wrote that, you know, people using AI coding agents are 10x to 100x more productive as engineers using cursor and chat today.

And then at Anthropic, they're about a thousand X as productive as Googlers were in 2005.

And I was like, what is going on?

And so I had to try it.

I opened Claude code and of course I ended up writing I'm around like a million lines of code which is really really crazy.

Everything let's see.

You know, let's just talk about the things that you might read on the internet.

These are all wrong.

It's not just AI slop.

Actually, you know, yes, LLMs are very verbose and some of it is boilerplate, but like when you create your own software factory, this is actually what you're fighting.

This is actually what you're preventing from happening by default.

Yes, there are hallucinations.

Yes, those are actually the things that we're trying to control.

You know, can you make demo code very quickly?

Yes.

But like how do you get it to production?

Well, you actually have to get to 100% or 80 to 90% test coverage.

That's actually one of the main reasons why plan-eng-review as a skill exists.

Like that's the one that that's the number one with a bullet skill that I use about 20 times a day to get to 80-90% test coverage so that I am not shipping slop.

I'm something I'm shipping something that is actually literally usable and that I rely on every day in production.

This is very controversial.

I've gotten in trouble over this.

I apologize to people for you know, who who like you know, took my trolling as serious.

Like, you know, is LOC gameable and something that might be you know, not usable.

Like actually, yes.

Like LOC on its own can be wrong, but on the other hand like if you have tests, if you know, the real measure of whether or not these things work is actually look down and does it work for you?

Does it work for your customers?

Are people actually paying?

That's actually the true metric.

You know, LOC might be a garbage metric, but I might argue that in the age of there's nothing in Claude code or the model or the harness or any or G stack or any of these things that tell the model to write as many lines of code as possible.

Like if anything, the reverse is probably true.

Like we're trying to write as dense and concise code as possible to serve the purpose and you know, I think that that's something that's quite important to talk about.

This is my experience.

Like I got to 87,000 stars.

My other project G brain is 13,000 stars.

So I mean basically for someone who was not coding at all in December of last year, I have more than 100,000 GitHub stars and about 15,000 people use it every single day.

You know, it's 100s of 1000s of skill invocations.

And so I don't know, this is sort of what I'm learning.

You know, last year probably before Claude 4.5 Opus 4.5 came out, about co-pilots.

Today I think we're really talking about a software factory.

And so if you use G stack, you'll understand this is actually what's happening.

What I discovered is that and this is more or less by accident.

As I was writing half a million lines of code for recreating my startup that I created like two other times previously but doing it in about five days or you know, during the course of like several months creating G stack, I realized that it's actually really useful to pull out specific personas of what is already in the latent space.

And so the most famous skill that a lot of people use that I, you know, it's actually interestingly a distillation of what we already do at Y Combinator.

When YC we have 15 partners, 16 partners at YC.

When you have an idea and you're doing office hours with us, we're mainly asking questions about what's the problem, who's the customer, how do you know that, and then what are we building, right?

And so that's what the Office Hour skill is.

We basically took uh actually three, four months of like transcripts across like thousands of conversations, distilled that into something very, very potent, and then I had to distill that down by 90%, and then that's what is shipped in open source in {slash} Office Hours in G stack.

Um but, you know, as I went like uh it turns out there are lots of different things that I like to use um to actually make it easier and, you know, far better to use the product that you can create uh with coding agents can be better if you're literally pulling out the latent space for a particular vibe and like thing that you're trying to go for.

So, plan CEO review, for instance, my favorite thing about that is uh it asks the question, "Okay, well, it has context, it knows what you're trying to build.

Uh what is the 10x version of that?

What is the platonic ideal of that?" And so, you know, when I was a product manager at uh both Palantir and Microsoft and like a founder for my startups, like that was what that when I thought about product, that's what I wanted to do.

I wanted to figure out like what is the perfect manifestation of the thing that we could build, and then when I build a um what I what I'm building right now needs to be on a road map that is a straight line from where we want to go from where we are now.

And then the other thing that I discovered as we were doing this stuff is that you can boil the ocean.

You know, who here remembers that term?

Boil the ocean.

Like, if you go and work someplace, you're going to go into a meeting where people start saying things that are a little too scary, and then immediately people in that room are going to say, "Whoa, whoa, whoa, let's not boil the ocean." And my response to that, based on my experience with uh coding agents and what's happening right now, is actually let's boil the ocean.

You know, the the things that you can do like uh basically you sitting in front of one of these terminals can you can do the work of about 500 to 1,000 people.

And if that's true, then like all of the expectations that we currently have in society around what a founder can do, what a company can do, what a small team can do, what you can do sitting in front of a computer, they're actually a thousand X wrong, right?

And actually what's funny is that's baked into the model weights.

Like who here has asked Claude code before, like how long is this going to take?

And it'll give you, oh, it's going to take about 3 weeks to code all of this stuff.

And then you press approve on the plan, and then literally it's done in about an hour.

So, I mean, all of us have experienced that.

Like the models themselves have not caught up to this new reality that we can actually boil the ocean.

So, anyway, use G stack.

Like there's a lot of stuff in there.

Uh we have very little time, so I feel like I need to skip ahead.

Like, you know, G stack was basically my understanding of building open source and putting it out there.

I'm still working on it.

Um but the new thing that I've been working that like everyone at YC has been, uh you know, just completely immersed in is open claw and Hermes agent.

And they're actually teaching us brand new primitives on how to think about code, how to think about markdown, and how those things work together to do real work.

Um and so this is like somewhat obvious, but I have to say it because I keep like anytime I would build an agentic system and it broke, it would every single time break because something was wrong about what I was trying to do.

Like I was either trying to do deterministic work, like things that should be in code in my markdown skill, or I was trying to do uh latent stuff, like actually the things that like my agent should be doing using the LLM in the code.

Uh and like a concrete example for instance is, you know, uh we spend a lot of time trying to curate the experience of people at YC events.

I have um you know, anyone, actually, you can just use uh Claude.

You don't even need Claude code.

You could use ChatGPT.

Put in uh you know, bios of like eight people coming to your dinner party, and you can have it go and, you know, Google that person, run a dossier, and then like figure out who should sit next to who.

That's very easy to do in latent space.

But try to do that with an 800-person dinner party, or with uh the 6,000 people that are coming to Startup School.

You can't do it.

Like the model's not big enough.

Like it it hallucinates, it doesn't work.

And so, what do you do?

Well, that's the perfect example of like we you know, you need to make the latent space work with the deterministic space.

Um and so, you know, what how do you actually do that?

Um here's a toy the toy example here is like well, what is a skill?

Who here has like played with a skill or used a skill file?

So, skill file is actually I mean, it sounds facile.

I mean, if you go on Twitter and believe like the haters, they're going to say like, "Haha, it's just a bunch of markdown files.

Who cares, right?" But the big difference now with LLMs is like like you can actually do real work with this stuff.

Um you know, the thing that keeps coming back over and over again is that you can do real investigations about it.

And so, you know, basically, what is a skill?

It's basically just a runbook.

Like you know, even you know, if if you've ever thrown an event, and you need to throw that event over and over again, what do you do?

You go into your notebook, and you just write down, "Well, one, we need to do the secure venue.

Two, like let's figure out who should come." Like it's just this any human being or agent should be able to look at it and say, "Okay, like after I read like 1 2 3 4 5 6, like however many steps it is, maybe it's branching." It could be very complicated, actually.

Um you know, do I know how to do that thing, right?

This you know, this is a very simple concept, but the really cool thing is that you can actually make it call code.

And that's what I find myself doing inside of Open Claw and Hermes all the time.

And this this is where it links to what you guys are doing as founders.

And this is the pattern that we're seeing inside every YC founder or inside every YC startup now.

Like we're not picking up the phone and doing it ourselves.

Just like we're not opening VS Code and writing code ourselves.

Like every like cloud code revolutionized how we write code, and we don't open like I you know, me Karpathy and tons of other people in this room probably don't open the editor at all, right?

Um the same thing is happening with Open Claw and Hermes agent.

So all non-technical or process-oriented things in knowledge work are now you can do it in Open Claw.

Like you can have Twilio call someone.

You can use Gemini live to actually like book a thing or like buy a thing or here's my credit card.

Like all of these things, you know, like that do you Who here remembers that Google demo where like they stood up on one of their conferences and they're like so proud like you know, Gemini can now call and like get you an appointment and then they never shipped that thing.

You you don't need to wait for them to ship that anymore cuz you can have that yourself.

And that's like the most empowering thing.

So code is code.

I mean, the concrete example I have is like who here uses Open Claw and uh it always for some reason thinks that you're in Greenwich uh in the UK.

Like it's always And so this is a perfect example of like uh I had to write code in TypeScript as context-now.mjs and I have tests for it.

And then I have it built into my system so that I don't rely on the latent space to do it.

It just tells me here's the time and then actually here's the things that are coming up.

And if I don't do that like left to its own devices, the latent space will be like, oh yeah, it's 3:00 a.m.

Like why are you still up?

And it's like, what are you talking about?

It's the afternoon right now.

The next important thing that we discovered, like anyone who has used Claude code a lot has probably seen this error message at the top of Claude saying, your Claude.md is 40,000 tokens or 40,000 lines or something like that.

Um, and then you Google around, you're like, okay, well, how do I fix that?

Well, how you fix it is actually a resolver.

So, a resolver is actually really important because uh it's amazing how much you have to spend time getting this right.

Um, you know, Claude is a whole bunch of instruc- Claude.md is a whole bunch of instructions of on how to do things that you developed, like you got mad that Claude code did this or that or wrote the change log in a certain way.

You say, hey, I don't want it like that.

Don't do it like that anymore.

Well, turning it into a proper resolver means that you take that instruction and it's like, anytime you have to write to the change log, load change log.md.

And so, suddenly you don't need that in your context, uh like the agent itself knows, oh, okay, here's this master directory of all the things I know how to do and I need to I need to load the instruction only when I actually need it.

Uh it sounds so simple, but it's kind of obvious, but like this is actually the core of having a really great agent, actually.

It's having a resolver.

When I when I need to check signatures, I want it to actually go to my executive assistant skill, um who is a particular person, like, well, I needed to look up in my brain repo how to do that.

And I have a skill, a specific code path, and it's not a code path, it's like a markdown code path, right?

It's a I call it a skill pack.

Um, I have a skill pack specifically for that thing.

I did it once, and then that's where um here's another primitive that I discovered that I I find myself doing about 20 times a day when I'm using open claw or Hermes agent.

Uh it's called skillify.

So, it's you know, you're sort of going up one level in abstraction.

So, let's use one of these examples.

Um you know, save this article.

Well, I do that once.

I'm you know, I look at the input, I look at the output, I get the agent to do exactly what I want.

And then once I have it in a position where I like it, I actually tell it skillify.

And then on the right, that's actually what the skill says.

And in you know, this is a summarized version of it.

I have a article on X about it if you want to see like all the full details.

But long story short, you write the skill, you write the code, and then here's the part that is actually broken in Hermes' agent.

I think they're about to fix this actually.

But um it's not enough to do it once.

You actually need to test it.

Um you have to It's like kind of like uh if you work in a finance organization, like think about all the people like 10 or 20% of people who work in some of these organizations just do compliance.

And you're like, what are all these people doing?

Actually, like in an agentic system, this is exactly the illustration of that.

Like look at all these steps.

Writing the skill and writing the code is only two out of the 10 steps.

All of the rest of it is making sure that this messy system that is kind of more like a human system than perfect, beautiful, beam of light code can still work and do work that you want, right?

Okay, so you want you did it some you did something in Cloud Code you or you sorry, you did something in Open Cloud, you made it work, then you say skillify.

What does it actually do?

Well, you have to write unit tests for the actual code.

You have to write LLM evals for the skill file.

Then you have to write an integration test.

Then you have to make sure that there's a resolver trigger in agents.md.

And then you have to test that.

You need an LLM as judge eval to make sure that when that thing comes up, it's broad enough that it actually gets triggered.

And then there's this other concept that you can look up in G Brain called check resolvable that is very important.

You want it to be dry, don't repeat yourself, otherwise you end up with like a a skills that do all the same thing.

You need end-to-end smoke test and then, you know, ultimately you need a schema.

You need to figure out where does this live in my memory and my repo.

So, we're going really fast, but you know, that's why memory is actually really important.

And so, my next project that is out now that I'm working on is called G brain.

It's actually a three-layer memory system built on top of what Karpathy already talked about with his knowledge wiki.

So, I started with a knowledge wiki as well and then it started falling over because it just uses grep.

And so, I had to add, you know, vector search, you know, ARR fusion, backlinks.

I added a graph database as a type knowledge graph.

I'm about to add an epistemology system so that we know that things are take they're like hunches or beliefs by specific people or world knowledge and I want to track when things sort of, you know, what's funny about maybe this is very specific to me.

Like I'm super fascinated with the idea that people in this room are going to go on to like your your journey as a founder literally is that you have a hunch.

You think that like the world needs X.

Nobody believes that yet.

But, you know, I want my knowledge system to be able to track like, oh, well, I heard so-and-so, this person in this room, this person in red shirt right here.

He tweeted this and nobody else believed that yet, right?

But, he's going to go and spend like a year, two years, five years proving it correct.

And then, if my G brain is actually working properly, it's going to spot that.

It's going to be like, oh, actually like here's at Stanford there's this one person who believed X and then they manifested it.

And so, I don't know.

I for me like philosophically, I'm I'm fascinated by knowledge systems like truly capturing what's going on.

And that's sort of what we, you know, I think about this like I'm just building software for myself.

Like this is the stuff that we have to think about and um I don't know.

I if you spot in my in my um voice like I'm excited about this because I'm building again and I'm building for myself.

And then we're open-sourcing this stuff because we want all of you to actually be able to do it.

Um, I feel like I need to expand on like, you know, one of the things that gBrain does is like it's a very specific schema for my use case.

But, you know, one of the last things I need to do before I go to V1, hopefully in the next couple weeks, is I actually need to make uh fully dynamic ontology, which is a great buzzword from that I've learned from Palantir back in the day.

I mean, that's what we, you know, right now it's built it's the schema is built for me, but there's no reason why it can't be built for you, whether you're a researcher, whether you're a journalist, whether you're a politician.

Like, each person's going to have a different schema.

We need to support all of those things.

So, zooming out, I'm about to pass it over to Diana to take it all the way home.

Like, I sort of gave you the primitives that we're learning literally like week by week.

Like, I didn't even know about uh skillify until it flew out of my hands at like 3:00 a.m. using open claw.

And then I put it on X and that went viral and I mean, I'm just learning as I go.

I'm not an expert, you know.

Some sometimes it's like uh my favorite line from uh Alan Watts, who if you guys know Alan Watts, is uh he walks, he goes to a room like this, he get he used to give lectures and he would say, "I am not a guru.

I am just an entertainer." So, uh you know, that's uh I want to pass this over.

I mean, we're talking about the agentic company.

Diana's going to tell you a lot more about it.

But, like, the the concepts that I just talked about, like, one of the weirder things we realized is these actually map to the company.

So, a skill is, you know, sort of a squishy human being who's an employee who has a capability.

A resolver is the org chart.

Like, who handles what?

Like, how does it happen?

Like, it's, you know, the filing rules, where it goes in the brain is the internal process.

Where does the information live?

Check resolvable is this thing that makes sure that the resolver works for like the set of things that you want to get done.

And that's like audit and compliance.

Like I you know, when I was sitting in your seat, I had no idea why so many people in so many human organizations had to spend so much time on audit and compliance.

But now at age 45 building a lot of identic systems and looking at Skillify and how much time I spend just trying to make the things like freaking work, you know?

Uh I actually understand now.

Like human systems are very messy and that's what check resolvable is.

And in the end like, you know, the funniest thing is what a trigger eval is.

Like you would think like, oh well, of course it's in the trigger, it's in the result, you know, in in agents.md it should just work, right?

But no, you even have to check that.

Like that itself is its own latent space squishy operation that you have to check.

And that's, you know, in an org, those are performance reviews.

So um with that, I want to hand this over to Diana to take us to the actual applied portion that will actually help you.

So I think a couple of things that Gary went over are a lot of the details on how you could implement it with a lot of the building blocks.

And if we really backtrack and step now couple layers up, one of the key concepts of building a AI native company is you need to change fundamentally how companies are run.

I think normally today pre-AI companies are basically run as a open loop.

People make decisions and a lot of those um decisions take a while to come back and is basically lossy.

There's no concrete tight feedback loop.

If a lot of you have studied control systems, how many of you have taken control systems and know the difference between open loops and closed loops?

Uh the problem with open loop systems is as error accumulates, the systems become more erroneous and then it goes off the rails.

As opposed to let's say closed loop system, very famous closed loop system could be like PID controllers, you have a tight feedback loop into the controller so that a lot of the error stays within check.

And this is how a lot of our robotic systems work a lot better.

So, we're basically now with AI have the capability to take a lot of these lossy information of how companies run into becoming a close-loop system.

So, what that means fundamentally today for old-school companies, information lives in people in people's head in a org.

They have a lot of side conversations, DMs and Slack.

They have a lot of meeting notes that are not written.

They have just vibes, how they feel about a particular decision.

And all very lossy.

This is basically how decision in companies are made.

And now, the ability is to change all of that into a close-loop system where you tie these agents that Gary described and how to implement it into basically the fabric of how you make decisions for a company.

So, the idea is that you would have an agent like a Hermes or open claw embedded into all the decision-making.

And what it means, the agent needs to have read access to every single artifact that the company produces.

So, for some of you that might be working on some projects in school, you could have a small version of this.

You could have an agent that basically connects to your GitHub codebase, connects to your Discord, and even start recording all the meetings you have with your teammates as you make progress.

And as you get all these contacts, the agent can then suggest what are the best next items to work on or bug fixes.

You put it in your G brain.

Put it in your G brain.

And the memory context.

And this is how you start embedding this agentic system that starts building the system and self-healing.

So, that's one of the things that we're seeing companies do where they can pull this crazy stats of one employee making in the revenue per company at at least like one or two million dollars, which now the public comp says I don't know, take like a like a sales force, maybe the employee comps of how much revenue they bring in is under six figures.

So, this is this is huge.

It's at least a 10x based on what we're seeing in the startups.

And what does this look specifically is when agents are able to read the full state.

In practice, we actually implemented this also at YC with our engineering team.

We're basically able to cut the sprint time in half and produce 10x amount of work.

And some of you may have read this blog post from Jack Dorsey about the agent organization.

How many of you read that post?

Some of you are familiar with this concept.

And I think he talks a lot about now making an organization very flat.

And basically getting less need for middle management because middle management used to be just all about this lossy information routing.

You end up basically having three roles in a company.

One is everyone starts building, so everyone becomes effectively an individual contributor that ships something, and even people that are non-technical, you now have the power to build with all these tools.

So, even a salesperson could be building their whole pipeline of calls and meetings and automate all of that.

And then the other person is the DRI, who tends to be Some of you're familiar with this term from Apple.

How many of you know DRI?

The concept of a direct responsible individual that every outcome in a company trace down to a particular owner that owns the outcome.

And the way it works is that the DRI orchestrates with the IC to make sure something gets done.

For example, a goal for a company might be we need to increase the revenue by 3x by the end of the week.

They're responsible to orchestrate all the things that need to happen to get there.

They work with the sales team to get all the calls booked, the engineering team to ship all of these, and that tends to be often times the founder.

Now, the new role that comes into this AI native uh organization is sort of a we call it a AI founder.

I mean, this is kind of a If If you hear Gary, he be really much embodies this.

It's you're living at the edge of the future with all the tools in order to get your company to run fast, you've got to be trying all the tools.

Everything is changing and moving so quickly.

I mean, literally we had this big revolution with agentic coding that just happened end of last year with a Claude 4.5 when it came out.

That's when things started to work.

But, if you were not building, if you were not at the edge, you would not be able to bring all those innovations into your company.

So, that's one of the things that we're seeing the best founders at YC do.

Yeah, there are people who are still uh operating like co-pilot level from last year.

It's like, not going to make it, bro.

They're not going to make it.

Now, the other thing that it gets talked a lot about is in order to build all these agentic systems to avoid quote-unquote the AI slop is you What cannot be delegated is really this concept of a taste.

How many of you been hearing a lot on the taste is what's going to be durable.

I think that and a lot of you agree with this, right?

Coding, let's just call it shipping code is going to zero, the cost of it.

But, what is not going to zero is the taste to build something good, the taste to discern what's good or bad.

And as part of that, that really manifests in terms of evals into the systems for how you build all these agents.

And what that means is that generic benchmarks won't make it whether your product works.

I know sometimes people are trying to just hit some generic public benchmark MMLU.

Doesn't tell you whether your product or or agents are really working or upsetting the user.

A lot of the product that a lot of you if some of you want to hopefully start companies, raise your hand, maybe?

Yeah?

All right.

Great.

So, part of it, the actual judge ultimately of whether something is good is whether users really want it.

And with that is going to be different in every single domain.

There's no way to automate that.

And how can you tell?

I think the agent you will have to go into all the details deep.

Did it follow the instructions?

Was the answer correct?

Did it preserve the customer trust?

Was it something that was spewing correctly or incorrectly?

Did it actually hit the business goals?

Did it comply with the domain rules?

So, a lot of these things that Gary talked about in terms of resolvers and skillifying it and improving the system apply here.

But in order to do that, you still need the human in the loop to tell when something goes wrong and to basically label a particular interaction or pipeline or workflow that is incorrect.

And that is something that is that you're going to have to own and do and painstakingly actually look through all the traces.

I mean, this is how Gary, you go through a lot of the system, too.

You like read through the traces and click when it's wrong or right and decide to skillify it, right?

Yeah.

Well, what's cool though is like once you get like the basics going, my favorite thing that I haven't released yet, but I will release is a cross-modal eval.

So, you know, I'm going to about to add the skillify where you can actually have the frontier models of Opus, GPT-5.5, and DeepSeek-V4 all evaluate the inputs and the outputs and then rate it and then feed it back to the original sub-agent saying, you know, this is the rating and here's what you need to do for the next try.

And then you actually iterate. you can meta prompt to get something that is 10 times better than the first version of what it is.

I mean, this what's weird is like these abstractions are basically stacking cuz that's what I learned that from G stack.

A lot of YC founders said, "Well, I like Claude code, but that's like my ADHD CEO.

And then Codex is my you know, nearly non-verbal 200 IQ CTO.

And I need both of them to do cross-modal analysis and then it ships with zero bugs." So, these are all things that are like stacking.

Like we're just discovering these things like week to week right now.

And this is effectively this section on all the founders here would be the ones building the evals and exactly that as part of a doing this cross-modal evaluation.

You have to start with being able to capture a lot of the traces.

And the way you capture the traces is going to be very contest dependent on the product you build.

And uh if you're building a let's say a video application is very different than a speech application, consumer model, B2B SaaS, all very different.

And then you need to convert a lot of the failure cases and you have to detect when they fail into actually evals that you use.

And then the step three is to be able to replay this constantly into the system to in order to self-heal and improve the system and improve the prompts automatically, which is exactly what Garry's describing that he's going to ship.

He's doing like a general version, but for each of you you can build all of these.

These are still the same principles.

Can we meta prompt here for a second?

Like you're sitting here listening to a lecture about this stuff, but the lecture is totally useless if you don't go and open your own Hermes agent and open Claude and like load up your own G brain and like actually use the like there are 40 skills that you can test out and try inside G brain.

And some of it is like make your own.

Like basically do stuff and then skillify your own stuff and then release it open source, too, and see what other people want, you know?

Like that's we're we're sort of like getting there together.

And so the exhortation is like not only are we meta prompting um the machines themselves, we we need to meta prompt one another to be better and to be able to fuse with the machines in a new and more profound way every single day.

Now, the last section we're going to go over is that for some of you here in the audience that are excited to start a company, this is probably one of the best times in history ever to start a company.

And this is not an overstatement.

You might have heard this from other lectures that came here.

Is that right?

The times right now are are unprecedented.

And part of it is we're seeing this a lot of the wedge in practices.

You pick a painful workflow.

You go inside deep into the customers and you basically become the forward deploy engineer.

And what that looks like, we've seen it across many industries.

And these are examples of companies that done this crazy growth that I'm telling you that gone zero to eight figures in revenue within a year.

For example, Salient is this company that's doing uh voice agents for loan services.

They closed some of the top banks in the US.

And the way they did it is they built agents how Gary described it.

Other companies, Happy Robot as well, that closed a series B recently last year and 10x the revenue in a year.

Same thing.

They embedded themselves with freight forwarders and built the best agents to automate a lot of that crowdy work with truckers and coordinating timelines.

And then the other one is uh Reductem.

I don't know how many of you might have heard of this company.

This is uh doing document processing.

The other opportunity is there's just so much tooling that needs to be built for all these tools.

Just the fact of doing better document processing is making all of the other agents better.

Because they all need to not read documents, but if you increase this, it improves rag and memory and brain to be a lot better.

So, Reduct is another these teams that are growing.

So, what what this means is that a lot of these companies are seeing all these impressive growth is they're they're not just demoing like AI or or some sort of side project.

They're actually deploying full solutions.

And part of it, if you want to start a company in this fashion, you basically go undercover because some of you a lot of you probably don't have necessarily a background like the founders of Scale AI or Happy Robot did not come from a finance background or logistics. >> training set.

Not in the training set.

But the way they became experts is they actually shadowed or took a job and learned the depths of everything that had to be done with it.

And then they were able to automate a lot of the repetitive labor and handle a lot of messy domains into this latent space that Gary described.

And all these workflows before were just done by like phone or email, spreadsheets, and all very random places where agent embedded into all the system could just create a solution that would just work.

And I guess the other thing is we want to show you this this graph that Anthropic posted in terms of the deployment in different industries.

And we're seeing that right now, I think a lot of you I don't know if a lot of you in computer science.

How many of you are a little bit afraid of the CS jobs after you graduate?

I mean it's a real fear because yeah, for this chart taken by Anthropic, 50% penetration into the usage of these tools.

But what is interesting this is giant white space in all these other domains in terms of like back office, finance, data, academics, cybersecurity, customer service.

This is like a huge white space that has room for hundreds and hundreds of AI unicorns that are waiting to be started perhaps by some of you in the room.

I guarantee it.

Because some of you may feel like all the ideas are done, but what we're seeing is that is not the case.

Yeah, we're at like the first pitch of the first inning on the revolution and you guys are the shock troops.

And one other stat I want to give you from the last batches at YC is that in the past only the best top 1% of the companies grew 10% week over week.

That was the metric that PG set.

And in the past perhaps the batch of Airbnb only maybe Airbnb and another company hit it.

But now what we're seeing things have dramatically changed where on average this is the growth of companies that within 3 months they basically 3x.

Yeah, in the history of YC this has never happened before.

So we get to live in this moment where like people in this room can create something that actually has a real impact and you can see it and you can tell because uh your customers are going to say, "I can't believe this exists and thank you." And they'll pay you and then every week 10% more people will be paying you.

And what we would like to close off here, I know a lot of the lecture theme has been about how you could build a one-person frontier lab.

This whole lecture was about that lab can become a one-person company and that could be you.

We just gave you all the secrets here.

Thank you everyone.
