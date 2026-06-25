# Stanford CS153 Frontier Systems — Scott Nolan: "Energy Bottlenecks"

**Speaker:** Scott Nolan (Founder & CEO, General Matter — a US uranium-enrichment startup; ex-Partner, Founders Fund; early SpaceX propulsion engineer) · interviewed by Anjney Midha (CS153 co-instructor, a16z)
**Channel:** Stanford Online · **Upload:** 2026-05-12 · **Duration:** 1:00:27 · **Views:** ~5,015
**URL:** https://youtu.be/wisccQYTRQc
**Source tier:** Tier 3 (domain operator), HEAVY nuclear-fuel/enrichment lean — Nolan runs an enrichment company + is a Founders Fund investor across the energy stack (SpaceX, Crusoe, Pantalassa), so "enrichment is THE bottleneck to AI" maximally serves his book. The structural facts (US <0.1% enrichment, turbine lead times, the 5-step fuel chain) are verifiable and align with the vault's HALEU page; discount the framing magnitude, trust the structure. Discovery-only; spoken numbers soft → verify at primary.

## Transcript (Tier 3/5 — not a primary source)

We are super lucky to have with us today to talk about energy bottlenecks, Scott Nolan.

Welcome, Scott.

Thanks.

Yeah, thanks for having me.

Excited to be here.

So, if you guys remember, we started the class by talking about how we're going through a great transition.

Right, so we have the old system stack that is transitioning to the new system stack.

And to go back to our organizing mental model and metaphor for the class of the AI factory, you guys remember this?

Right?

This is how intelligence is being manufactured the frontier.

Pre-training, mid-training, post-training.

Deploy to agents, rinse and repeat.

And for the last few weeks as you guys have heard from folks like um you know, Maddie at 11 Labs, Robin Andy at Black Forest Labs, and I'm at at Luma.

Right, those are all different types of intelligence that are being figured out in the field right now.

Today, we're going to zoom out a little bit because sometimes it can get easy to forget that what's happening at AI Labs, sure, it's exciting, right?

We're getting new capabilities that have never been possible before, and that is what's driving so much growth in the industry right now and excitement and revenue and all of that.

Um but that's just one part of what's going on because to deliver new capabilities to the world, it takes a number of things to come together.

Right?

And we talked about how there um some major bottlenecks on that progress of capabilities.

And one of them, as we've talked about before, is compute.

But the point of this class is to try to give you sort of a macro systems view of what's going on in the world, not just in model labs, but up and down the stack.

Okay?

And I find the stack the whole idea of a stack even is quite rigid sometimes because it it kind of presents this view of, you know, how things work.

I mean, ultimately it's just one type of mental model and and scaffolding.

And as you know, we're we've been talking about a different kind of mental model and scaffolding, which is a a frontier AI pipeline.

And what I'd like to do is zoom out a little bit now.

Okay?

This is my uh handywork.

I'm not a professional artist.

Um but this is my my attempt to try and be a little as close to Hayao Miyazaki as I can be.

I grew up watching a a bunch of Studio Ghibli movies.

And um this is sort of a stylized mock-up of what I think, you know, is is a systems level view of how these capabilities factories are working.

And so, if you look, right right at the center of the factory, we've got the pipeline, right?

Data, compute, algorithms, pre-training, foundation models, mid-training, and so on.

But, to make that work, it takes a whole other bunch of systems to come together.

Now, if you look at the right side of the factory, you've got a little box there that I call that that Think about that as analogous to the data center that's providing compute.

You know, and we talked about in lecture one how compute is super critical, it's important, but remember that's just one bottleneck.

Sometimes what gets lost in the conversation is that powering the data centers is a whole other important thing called energy and electricity.

And to keep your compute running on time, well, somebody's got to power the data center.

And we are going through I would say we've been now in 4 years of relentless pressure on that part of the supply chain.

Cuz after ChatGPT came out in late 2022, um you know, that turned out to be this this for a long time before ChatGPT came out and scaling laws had been discovered, the question everybody's mind was what is this stuff what is it going to be useful for?

I mean it's cool technology, but really what how is it going to change the world?

And ChatGPT I would say was the first sort of consumer killer app.

Right, it became this this way to consume the technology of language models that were that were legible to everyday people.

But the supply chain wasn't ready for that.

You know, it takes like 2 years to tape out chips and stand up data centers.

And so in early 2023, a few months after ChatGPT came out, there was a huge compute crunch.

And for a short window of time also a huge energy crunch.

At that moment in time, a bunch of us in the industry who are paying attention to what was going on started realizing, "Wait, if this continues, we're not going to be able to keep the progress going." Because at some point in the future, cool, we had a consumer killer app now with ChatGPT, but at some point somebody's going to figure out an enterprise killer app.

You know, some some tool or way to use this technology that's useful to enterprises and businesses.

And that's what happened, right?

What what happened in December 2025, a few months ago?

Claude 4.6 came out.

Anyone remember that?

How many of you were coding over the over the uh winter break?

Yeah.

Did it feel different?

Right?

And then all the adults, well, you guys were students so you had some free time, but all the adults who were, you know, on on parent duty came back from winter break and started using Claude at work.

And stuff started to change, right?

Cuz now suddenly you've got enterprises and businesses going, "Hey, this is really useful.

We want more of this stuff." And that was a Groundhog Day moment.

Um now, for me it wasn't that surprising cuz as you know, 4 years ago when ChatGPT came out, that's when I realized compute was going to be a bottleneck.

I started working on a version of uh trying to unlock unblock that bottleneck at a16z.

But elsewhere in the industry, there's a guy called Scott who was realizing that energy was going to go through a similar problem because if you just keep going down the supply chain, you realize that that's going to be a huge bottleneck.

And so, the reason I have the electricity part of this map so much bigger than the data center map is actually from a urgency perspective, even if you have a data center ready to go.

If you can't get power to it, doesn't matter.

It's over.

You can't train models.

And so, um for this class, we wanted to make sure you got a a view into that part of the world as well.

And so, for the next um few minutes, we're going to get a sort of an expert deep dive into this part of the factory, right?

Uh ideally all of this is just happening in one place and at some point in the future, maybe we can have modular data centers like on campus next to the lab with a modular reactor or something.

We're not there yet, and so instead we have data centers in one part of the world and energy power generation in other parts of the world.

Um so, this is a glorified sort of idealized utopia schematic here.

Um but for this lecture, we're going to be zooming in to energy.

So, with that, um why don't we start with you, Scott?

Thank you for coming.

Tell us about yourself.

How did you get here?

Cool.

Yeah, thanks for having me.

Um so Scott Nolan, CEO of General Matter.

We are uh uranium enrichment company for nuclear energy.

I started off as an engineer.

I was mechanical uh undergrad, aerospace masters.

Uh that was Cornell and ended up coming to Stanford for uh second master's degree in business of all things.

Um but I sat in a lot of engineering classes.

They were pretty much all of my electives uh including some CS classes.

So I did that, wrapped that up in 2011, Founders Fund, the VC firm.

Was there for over a decade.

Uh just fully focused on anything hard tech, anything engineering, technology driven.

Um and that included energy.

And so uh you know, one one part of energy I'd always been interested in was nuclear.

It always felt like this branch of energy production that just had gotten completely forgotten and sidelined as you know, it being a massive mistake for like the past 50 years.

And for the for that decade I would meet with so many different nuclear companies and by 2020 there were starting to be some pretty interesting ones.

Um but they all said the same thing that they had no fuel and that they had to get their fuel from Russia.

Which was really shocking to me.

Um I dug into it for the better part of 2023 and realized it was all because of this one missing step which is what we're working on.

So what we'll get into it.

But for today's class I think the interesting thing is just this energy topic in general.

How much of a bottleneck is this?

How do we solve it?

And we'll go through that.

Yeah, that sounds great.

So we're going to you know, you don't have to take my word for it.

We're going to start with three pretty smart people um who talk about energy a bunch as bottlenecks to their to their businesses.

So first one is um is Sam from from OpenAI.

And this is him testifying to the Senate.

So this is uh you know, you you can't you can't you have to tell the truth when you testify to the Senate.

So you know this is true.

Um so everything is going to converge to the cost of energy, to the cost of electricity.

Like, chips are going to um models are going to get cheaper, but energy is fundamentally what you consume when you're running these models.

And, you know, one version of this is Balaji, uh who was a Stanford professor at, you know, for a time also, has argued that everything all costs, all, you know, monetary things should be denominated in joules.

Um and so, this gets back to the same sort of same sort of thing.

And then, you know, then you then you think about Jensen, and probably his his incentive should be to say that chips are the bottleneck, or that something about what he's doing is a bottleneck, but even he would argue or admit on, you know, on the Joe Rogan podcast that energy is actually the bottleneck.

So, that's pretty powerful.

And then, you know, you go to you go to Elon, and um there's, you know, many bottlenecks that he could talk about, but the one that he wants to highlight is is energy.

And I think you're seeing this now in in some of the plans with SpaceX.

Um And so, I guess I left that out of my background.

I was an engineer.

I worked at SpaceX right out of school.

Um and then I did did a bunch of other stuff before Founders Fund.

So, um >> That was before you came back for grad school, right? >> Before.

Yeah, I did everything backwards, basically, but it's okay. >> Um And then, you know, and then it's like, okay, well, these are people at the very forefront of data centers, of of the models, thinking about what's coming next.

Um but then you go mainstream and you realize, well, even the Financial Times is realizing this.

They're realizing that actually what's upstream of data centers and all the compute is power, and you really need power, and then where are we going to get it from?

Um and we'll have some time after these slides to talk about some theories about this.

Um And but you you then might ask, well, okay, how big a problem is this really?

Is this really like something that we can easily tackle?

You know, you mentioned, okay, let's talk about energy, electricity.

It just sounds to most people like so unexciting and boring and oh, it's big metal wires and infrastructure and why do we care about this?

Certainly someone has this solved.

How could that possibly be a problem?

We've been doing it for 100 years.

Um and you know, but then you look at the demand and you realize, wait, this is like way super linear and how are we actually going to keep up with this?

And then you say, well, okay, you know, maybe it gets to a terawatt but you know, in a decade it gets to a terawatt.

That's that's pretty fast, but maybe we can keep up with that.

Maybe it's not so hard.

And then you look at what we've actually done over the past you know, in this chart you've got over 50 years x-axis and you look at like the last 20 years and you realize, wait, we haven't done much of anything and in fact like 1 terawatt's a kind of a problem based on what we've been doing.

Um we need to be much more on a China-like slope where you look at the the yellow portion of this.

Um and you realize, wait, we need to be on a very different slope even than China.

And so we have to go from almost a complete standstill on grid expansion to nearly vertical.

And so that's going to require some very different activities than what we've been doing as a country for a long time.

For longer than pretty much anyone in this room has been around.

So I think with that you you quickly realize you know, okay, it does seem like maybe electricity is the bottleneck to AI.

Maybe maybe Jensen and Sam and Elon are all on the same page because this is so overwhelmingly obvious that you have to solve this.

And then you would say, well, okay, how are we going to solve this?

This is clearly a big problem.

Um you know, we haven't done much.

How do we how do we go really quickly on on ramping production?

And if you rewind to like 5 years ago, um stranded energy was enough.

Uh so there's >> just define stranded energy? >> Yeah, so there's plenty of stranded energy and stranded energy would be things like, you know, a hydroelectric dam in some, you know, rural region that there's no population nearby really consuming it, or maybe it's geothermal.

Um isolated geothermal with existing technologies that no community to consume it, or stranded wind in West Texas.

Um the list goes on and on, but and anything like that, something where there's supply without real demand.

And so what you saw late 2010s, early 2020s, that was completely dominated by companies that said, "Okay, I see that stranded power.

I'm going to go build something there." The very first builds that happened were typically Bitcoin uh Bitcoin mining centers.

Yep.

Um you know, you didn't have the really huge AI data center demand, but you did know that, "Okay, what can I do with stranded power?

I can mine Bitcoin.

I don't need that much connectivity.

I don't need fiber.

I can get by with iridium or something if it's middle of nowhere.

I can get I can get, you know, enough connectivity to actually perform that." And so you saw companies like on the left um is a company called Crusoe, which now has, you know, is doing the Stargate project in West Texas.

And that project is linked up with wind and natural gas and all sorts of things, some of it which was stranded.

Um and so that was that was a great strategy for a long time.

At this point, most of those great resources that were stranded without nearby demand have been claimed.

People have gobbled those up.

And you know, the capacity that we need is increasing quite a bit.

And so even those small chunks of electricity that were available would not even be enough today to satisfy things.

And so um things are really moving to ask the questions of, "How can we create massive net new power production?" And so this was something I was starting to think about both the stranded topic and the bigger topic um at Founders Fund late 2010s early 2020s and coincidentally um invested in if the top left is Crusoe uh then invested in all of these companies.

And so top left is uh data center just like Crusoe.

Um I don't actually think it's a Crusoe one.

Uh you've got SpaceX which is now talking about inner orbit power production.

And then you've got a company called Pantalassa doing distributed energy in in the ocean.

And so lots of different angles on this.

People have different theories.

We can talk about inner orbit.

We can talk about other options.

But today we'll talk about on land because that really dominates things and that's what that's the reality that we're living in.

And so you say, "Okay, well, we need to produce a lot of power on land.

What are what are the constraints?

What are we designing for?

Um what are the things that the data centers actually care about?" And one of the big things they care about is uptime.

So, you know, data center can you run it on solar?

Can you run it on wind?

You could.

Um but you're going to need a lot of batteries.

And by the time you got enough batteries to get this uptime, at least as batteries exist today grid scale um your cost is going to be pretty high.

And so people have have gone away from that.

Uh what you're seeing today, the last couple years, is a lot of natural gas powered data centers running on turbines.

Turbines are getting pretty scarce.

The lead time for turbines is a few years now.

Um which has increased drastically and the producers of turbines generally are not ramping production quickly enough to even remotely keep up with this.

Um and so then you say, "Okay, well, we need we need something that's not natural gas, can be base load.

Where do we look?" And you might say, "Well, okay, what are the other factors?

Maybe we don't want to put out a lot of carbon.

Maybe we want it to be pretty safe." And so then you look at the historical statistics factoring in you know, every plant that's ever been built and you realize that um here's here's the base load chart.

Then you realize looking at safety and cleanliness of power source that actually nuclear is pretty good.

Um, it's actually lowest carbon emission of any of them.

And it's essentially tied for safest with wind.

Um, and so those two things together, if you care about safety or or emissions, it's going to push you pretty hard towards nuclear.

And that's why all the hyperscalers are are looking to that.

I think they all realize nuclear is not going to be something where you build a plant overnight.

It's not a one-year project.

It's something that we're going to see ramping in the next 5 to 10 years, truly ramping and moving the needle.

Until then, it's kind of a a race who can find stranded power, who can find enough turbines, who can maybe stand up solar with enough battery storage if they're less cost sensitive.

Um, but I long-term everyone's looking to nuclear.

And so then you say, "Well, okay.

Well, if nuclear is the long-term, you know, scaling limiter to electricity, 5 to 10 year time frame, and electricity is the bottleneck to AI, then you probably realize, well, that's kind of unexpected, but maybe nuclear is actually the bottleneck to AI scaling.

Um, if you're talking about here on land, at least.

And so then you might ask the third question, well, okay, is there a bottleneck to nuclear?

Uh, which brings us to what we're working on and every nuclear reactor runs on fuel.

I think a lot of people hear nuclear and you would think it's a magical technology.

It's like a perpetual motion machine.

But no, you actually need to refuel it every every year or two, depending on the reactor.

For more advanced reactors, there's some that designed for 5 to 10 year refueling cycles, but, um, it does require constant fuel and it constantly burns up fuel, just like any other type of engine.

And that fuel comes from five different steps.

You You start by mining, you turn it into a gas, you enrich it, uh, you turn it back into solid and then you make your fuel pellet.

And you might then think, just like electricity, well, maybe this is a solved problem.

What could be the issue?

Um but you actually look at these five steps and it turns out that the US has less than 0.1% market share today of enrichment, which is the middle step.

And so the US is actually unable to produce its own nuclear fuel at any scale whatsoever and we rely completely on European firms and even to this day Russia.

Um even though there's sanctions, we still we still import uh because we really need to.

And um you know, so there's this missing piece right in the middle.

And so we can't really scale nuclear fuels a country, which means we can't really scale nuclear.

And which will mean that we can't scale uh data centers and AI.

Um and you know, if scaling is one thing, cost is another.

At some point the cost will matter a lot.

People will start being more price sensitive.

It won't just be an arms race for who can stand up a data center the fastest.

There'll be margin compression, cost will matter.

But in fact, cost is the biggest, you know, of the cost of uh advanced nuclear fuel is the biggest cost in many cases and the biggest portion of that is actually enrichment, which is why we're working on it.

And so you you know, you do the build one more time and you realize enrichment is kind of the bottleneck all the way through to to AI on a on a five-year time frame.

And so that's why we're almost in a race against time at General Matter going as quickly as we possibly can to bring enrichment back online in the US at scale like with a highly scalable method that we think can completely win on cost.

Um and we're getting a lot of support from that.

So when we started the company, there was uh no ban on Russian uranium, there was no AI data center boom.

Um it was under Biden administration.

We started by working on advanced fuel for advanced reactors and that was a big push.

And then now this administration is very focused on energy production and there's kind of follow through on that push across administrations and bottom right you can see our August groundbreaking of our facility in Kentucky.

In that image there's people from like the full range of political spectrum all getting together around this and so going from the very beginning you can see the tech leaders are realizing energy is a bottleneck all the way to DC everyone realizes that energy is upstream of everything not just AI but also manufacturing and pretty much any any industry that you want does rely on it and the current state of it in the US is is far worse and far less ready to scale than a lot of people realize.

So that's what we're working on.

Thank you Scott.

Why don't we take a beat there because you said a few things I want to kind of double click on.

Scott mentioned Bitcoin mining.

And he's you know sort of mentioned that in passing but the reason I want to zoom in on that is because um you know sometimes the cultural commentary around a piece of technology can often make the underlying progress that's quite real and you know clearly sort of fundamental um confusing.

Um you know nominally from a memes perspective you know the way this manifests itself on the timeline and so on is people saying SBF funded you know Anthropic SBF was running FTX at the time.

Um like you know the fact that people in the crypto community were investing in the AI stuff you know you can we we we can disagree on whether crypto ended up delivering on its promises or not but what we have to acknowledge is that um you know Bitcoin mining was was a bit of a dress rehearsal for AI.

Mhm.

Um and sometimes you know I I I get all these questions where there'll be a a team working on a pretty important fundamental bottleneck at the infrastructure layer but just because they've raised money or something or have done some political donation or something with somebody from the crypto community, their underlying progress just gets thrown out.

You know, it's like a baby throw out the baby with the bathwater sort of moment cuz people go, "Oh, if if crypto people are involved or Bitcoin mining is involved because that didn't work out." And yeah, right?

Who knows?

At some point we may have this decentralized you know, sort of um censorship resistance and so on.

And then we we will have truly decentralized computing.

These things take a long time, but the from a first principles perspective, I find it quite sad and and disappointing when people aren't able to decouple those two things.

Um you know, you you might you mentioned Crusoe as an example of of a company that's been that you've worked with before.

Um I think Crusoe was originally a Bitcoin mining company, right?

And then they they sort of some of the many of the innovations that they ended up realizing during the Bitcoin era have ended up translating into to building infrastructure for the AI era.

Um and I and I think those learnings have ended up coming valuable.

Um you know, venture capitalists sometimes like to call these evolutions pivots, and I think there's a unnecessary stigma around that when in fact pivots are just one step of the continuous feedback loop we've talked about before in my view, right?

Um and it's an update, and the best leaders update their priors.

Similarly, as as you've been approaching the sort of energy um discussion, you know, nuclear is is another one of these areas that has been unfortunately uh plagued by a bunch of confusion, politics, yeah, social divisiveness.

Um What advice would you have for people here who are who believe that uh you know, they'd like to work on energy, they'd like to work on nuclear, But for the whatever reason feels like because of the past um uh political climates or social objections to that technology uh the fundamental progress is not legible.

Am I making sense?

My question I mean, you can even go back to that chart.

The emissions and the safety track record of nuclear.

And then we'll talk about nuclear.

But going back to what you were saying before of these pivots, I think you know, pivots is one thing, but I would say if a company is building something that you can think of more like a primitive.

Right.

Like a fundamental building block.

Which you might say, well, utilization of stranded electricity feels like a primitive.

And yes, what we might do with it today is mine Bitcoin.

Right.

Um we think that this is going to be really useful.

And that's what Crusoe's approach was.

And they went from Bitcoin mining to saying, well, actually you know, yeah, we're mining Bitcoin, but we're also massively reducing emissions Right. >> that are occurring just because this this gas was not just stranded.

Because it was stranded, people were just burning off methane straight into the atmosphere with both carbon emissions and particulate emissions.

Right.

And they took it and they ran it through a turbine and made power and mined Bitcoin and reduced emissions.

And so um they felt like, hey, no matter what, even if you discount the value of mining Bitcoin to zero, we're still creating value.

Then we're making money and we can invest in this infrastructure.

And they took that and they built enterprise um you know, cloud deployments.

Slightly larger scale, they would go after bigger projects, not just stranded oil wells in North Dakota, but stranded wind in West Texas.

And then they took that and they leveraged that into something else.

So it's it's really building this up over time, I think um on top of a basic primitive is this probably the way to think about it even more than a pivot, even though maybe the final end state product that people interacted with looked different. >> Yep.

And so you know, I think I think of that as something we're basically doing.

Um it's something lots of companies have done in the past.

It's something SpaceX did.

It was really how can we do how can we reduce the problem of commercializing space into a fundamental piece?

And that fundamental piece was launch capacity and you could denominate that in dollars per kilo to an orbit.

Um and and that was a really powerful thing.

If we can just bring make this cheaper, we can do a lot of really cool stuff with that and make something cheaper, you get more of it and people will build on this and will will push for the commercial space economy.

So, that was that thesis.

For us, our fundamental building block that we're working on is enrichment, which is really just refining.

It's refining a fuel.

It's refining of uranium based on its isotope.

And you want to get the fissile isotope um in enough concentration that you can run a reactor.

And so, that's a very, very fundamental thing to do in a whole sector of energy that's been unfairly uh you know, put on the sidelines.

Uh and we can talk about why that's happened, but if you can enrich, you can make fuel.

If you can make fuel, you can make 5% fuel, you can make HALEU.

You can make these different grades that different reactors run on and you can supply to anyone.

And so, you can supply to the existing reactors that are powering 20% of the grid in the US today with zero carbon emission.

Um and those utilities are very eager for uh you know, to work with new entrants and to support the expansion that's going to happen.

Um or you can work with advanced reactors, which probably are what most people hear about, all the small modular reactors or micro reactors.

And you can make the more enriched fuel that they need to get their smaller form factor.

And so, um I think back to your question of like what should people in the room think about when working on a problem?

Um I wouldn't worry so much about what what the public narrative of it is or what very surface level treatment of it tells you.

I would go a lot of clicks deeper.

Like just go all the way to the bottom and figure out, okay, well, what are we actually solving for here?

If we want base load, if we want it to be clean, if we want it to be a very scalable and safe, let's look at the numbers.

And you look at the numbers and you realize that despite a lot of um you know, not even a lot, a few very famous nuclear accidents um you know, and famous partly because it's a hard thing to understand.

Uh the safety track record of nuclear is so much better than anything else.

Right.

And even accidents like Three Mile Island had uh you know, I think based on all all analysis like no direct measurable deaths from that accident.

Um Um the same thing with even in Japan with Fukushima was, you know, maybe there was one one fatality but thousands from the tsunami that caused it.

And so um nuclear has just been this technology that if you look back to the '50s and '60s, obviously we were supposed to do two things.

We were supposed to go to space and we were supposed to have, you know, energy that was abundant and clean and very power dense.

And we've done one of them but now we're finally doing the second.

And so, you know, I think it's partly the industry's fault.

Uh I think the government gets a lot of blame, the public gets a lot of blame but I think a lot of it was actually the industry um not not making the case for nuclear nearly strongly enough.

Yeah.

And it definitely wasted a lot of time but, you know, no time like the present.

I mean, we're we're old guys now but uh we're going to I'm going to date our ourselves but when you know, in the 2010s there was this meme of the keep calm, don't panic.

Uh mean, do you do you remember that one?

The this the red this is like the red poster. >> Yeah.

Like the it's the London underground one, yeah. >> the London underground one.

There's also the dog sitting in the burning building, everything's fine. >> Everything's fine, yeah, yeah.

So so I I think those are two ends of the spectrum, right?

Like st- stuff is burning down, you're saying it's fine and that's cope and that's one spectrum.

But then the other spectrum is you know, so- something happens which always something goes wrong in the physical world and then everybody panics and over corrects and that sets us back for the next decade.

Um, you know, where in the spectrum should should the students how how do you is there a repeatable way for people to calibrate on where the right place is to be so that you're not just over indexing on the memes and instead actually landing at the right place? >> Yeah, I don't think I think it's a mistake to get too caught up in the moment.

You have to be somewhat aware of what's going on and if, you know, if you have an idea that's clearly 20 years too early, I think that's that's not going to be a good thing to work on.

You're probably better off working on something that's more immediately necessary and then come back to that idea later.

Um, but I would just focus on the fundamentals and so like the the the framework I always go back to I've always found it compelling is, you know, what's the really important problem that's that's not getting solved um, that's not going to get solved by someone else that somehow your skill set lines you up to to be really useful for and it's really just work on those things. >> Yep.

Um, that could be an existing company.

It could be at a new company.

You could start your own company.

It could even be uh, in a non-profit, in the government.

It could be in lots of different places.

Um, but I'd say work on whatever you're going to be the most useful for that's actually an important problem and find the right place to do that.

Um, I'm guessing questions are piling up.

So, I'm going to take a I'm going to ask Scott a couple more while people get their questions in.

Um, as a proof point for how powerful it is to truly internalize like when this lecture is live, I would encourage you to go back and listen to every word Scott said, internalize it and then try and practice it because as a proof point of how powerful that framework is, you know, you started um, General Matter in January 2024, was it?

Yep.

Right? >> Yeah, that's when we became a company.

Before that we were working on this in fall of '23.

And I I'd been starting on this even in December of '22.

Right.

So, you spent about a year marinating like truly understanding the problem, doing the five whys Mhm. in 2023.

Mhm.

Scott then started the company General Matter.

He's not Remember, he Scott's never started a hardware business before.

He worked at SpaceX, of course, and got a ton of really great lessons and worked at um Founders Fund.

But really I I cuz this not Is this the first company he's started?

Yeah.

Yeah.

First company Scott started.

Okay.

Uh January 2024. 24 months later. 24 months.

Scott announced, this is January of this year, that General Matter has been awarded a $900 million contract from the DOE to do uranium enrichment.

Can we get a round of applause for that for a second?

The rate of progress that Scott single-handedly and the General Matter How big is the team?

Uh we're close to 100 now. 100 people have accelerated in in such a short amount of time that that's that's so fast that the US government is saying we're going to hand this 100-person company startup almost a billion-dollar contract to help us move the country forward.

And so, you know, sometimes the timelines on which you can make a difference, especially if you do the right systems analysis, and you focus on alignment between your mission, your business model, the technology, are quite extraordinary and can surprise people.

But maybe you could take us behind the scenes a little bit on what it took to go from that moment when you founded the company to that contract. >> Yeah.

And I would I would highlight that, you know, you talk you just mentioned alignment.

And the thing that's really aligning is this is a multi-billion-dollar project, and the DOE has said, "Hey, we want to help.

We want to help accelerate this and help you go even bigger than you would otherwise." >> Right.

And so the the contract itself is to help us build that capacity as quickly as we possibly can.

And so the aligning thing is we'll we'll bring even more private capital to the project than that amount.

Right.

And so I think if you if you ask, "Okay, well, how does this come about?" We we chose to work on a problem that we knew was completely we believed would not be solved and was completely important and required urgent action.

And fortunately, the DOE Congress had already been thinking about this.

They had already funded these programs.

We didn't have to convince them that these programs should exist.

They knew that they should exist.

And they were open to new entrants coming in and helping solve it.

And so what it looked like was identifying the problem in 2023, uh really asking ourselves if if this was the thing to work on.

We concluded that yes, it was.

Um pulled the team together in in late '23 with all the right people from the industry.

We we asked ourselves, "Okay, what does the right team look like for something like this?" Then we handpicked those people from a bunch of different companies that included national labs, other companies in the nuclear energy space, and then people from Tesla and SpaceX because we're going to run a pretty similar playbook to break into a really capital-intensive, incumbent-dominated, stagnant industry.

And so uh we wanted those exact type of people with that DNA and that experience.

And so as pulled the team together, and then then we evaluated, "Should we do we want to, you know, put our hat in the ring for this program?" And it was completely on on on a direct path of what we were going to do anyway, and we said, "Yes, let's put our best effort forward to do this." And so, you know, first few months of the company was legitimately 100-hour weeks, just living and sleeping at the at the headquarters, and and doing all the work that we were going to do over a few years um to get the plan extremely uh buttoned up.

And then then became the search for the right site.

So the other thing with nuclear was we knew yes, we can have the best technology, we can have the best overall plan, but you also need a really supportive community and a supportive location for what you're doing.

And so we're headquartered in LA, but our facility won't be in LA.

Our facility will be in western Kentucky.

And so that's where we're doing construction and actual enrichment and manufacturing.

Um and so we found a a site there that's in the the same city as the last place the DOE that the US did commercial enrichment in 2013 before we shut down.

It's called Paducah, Kentucky.

Right.

There's a DOE site there.

We originally went there looking for some old buildings that we could use, um but then we found that there was 100 acres at the south end of the site that had not ever been developed and was perfect for what we needed.

And so that was the beginning of the partnership with with the DOE.

Um and yeah, like you know, like you said, they've been extremely supportive of someone new coming in to help try and solve this problem.

Uh I'm going to ask you a follow-up sort of last question on this.

You know, there's a lot of anxiety and uh fear, uncertainty, and doubt about the current administration not supporting science and engineering in the country.

Um but what you just I outlined is a direct counter example to that.

Um what is there like how supportive as a was the federal government in this?

You know, DOE, my understanding is there were in the members of DOE that helped sort of smooth things along for you.

Is that true or do you feel like you know, the United States is asleep at the wheel and actually not helping entrepreneurs make progress on a bunch of critical infrastructure like the one you're working on? >> Yeah, I'd say definitely not asleep at the wheel.

I think you know, going back to something I said earlier, the the support for this has been ever since the Biden administration in 2022, 2023.

Um and so I don't think it's a political thing.

I think you know, we can we can get into some of the details there, but it's been something where there's been congressional support for first doing Halo, which is the advanced reactor fuel, and then doing LEU, which is what the grid currently consumes.

Um and so it's a known problem, it's a known opportunity.

We really need to bring this back as a country.

And so, um yeah, there's just been a bunch of support from across the political spectrum.

And then, you know, that's the political side.

Then within the government, you have people who are been putting their whole careers into this.

And I think uh within DOE and the nuclear energy department, those are people that are in it not because nuclear has been growing, because it hasn't since the '90s, but because they really believe in it.

And I think um yeah, there's just been incredible support from across DOE for what we're doing also.

So, I'd say it's it's the type of thing that um you know, to your question of like, should people be worried about what's happening day-to-day and memes and um you know, public opinion, there's there's certainly going to be ups and downs for nuclear over the next few decades.

I think it's going to be drastically ups.

Um but there's been the same sort of support, like very consistent support uh from everyone in the government.

On the topic of jobs, so there's a bunch of jobs you've now created in California.

Mhm.

But you also created a bunch of jobs in Kentucky.

Yep.

Over the next 4 years, how many jobs do you think General Fusion Matters is going to create?

Uh it's probably I mean, it's hard to say.

It's certainly hundreds and hundreds of jobs.

Even in LA, it's probably close to 500 over the next few years.

In Kentucky, it's it's that much or more.

Um you know, if you go back to the really early days of SpaceX, apparently they thought the company would ever only be like 200 people.

Um clearly that's not true.

It's like close to 20,000 now.

So, these things have a way of, you know, when you're working on a really important problem that uh can just keep scaling.

I I think, you know, that's maybe one my one lesson from over a decade at Founders Fund was things can scale much more than you think.

And they often need to scale much more than you think.

Uh which is you know goes back to the SpaceX example off by two orders of magnitude on on what head count would someday be.

And for us, I think just near future we look at you know, hundreds of people in LA, hundreds in Kentucky.

That probably puts you at like a thousand uh for doing what we need to do.

So, a thousand new jobs created by a startup whose path is definitely accelerated by AI, right?

To do the five whys and Scott kind of like walked us through how arguably uranium enrichment is the bottleneck on AI.

As you guys have heard multiple times, there is a there's a narrative that AI you know, eliminates jobs and reduces jobs when in fact Scott is sort of living proof that entirely new jobs are being created in real time in the thousands to unblock the bottlenecks for AI scaling.

And I think this is an important sort of alignment mechanism everyone should be aware of more and more which is this is not some dream that AI can create new jobs.

It is literally creating new jobs both in the sort of knowledge sector in in California, people who are working on engineering systems for you, but also in the construction industry halfway across the country.

And so, I expect to see more and more companies like General Matter assuming the public understands that AI is actually net new.

It is igniting a renaissance in in physical in the physical world that that we will end up in a place where jobs that didn't exist before are going to be created.

But if you agree or if I'm being overly optimistic.

Uh I'm I'm pretty optimistic.

I mean, in our case we we have dozens of open roles and like we're looking for to hire hundreds of people.

We can't find enough good people not quickly enough.

And so, in our experience like you know, it's it's obviously different for every company and every person, but our experience is that we want to find more good people and give them jobs.

And so, we're in a huge we're in a deficit.

And so, how do we find enough great people?

So, for people that want to work hard and are good at what they do, there's plenty of at least at our company tons of opportunity across pretty much every type of engineering, every type of construction type role, finance, like you name it, we'll hire people.

I mean, we could do a quick poll before we go on to questions.

Like, how many people now feel like they'd be interested in a job working on uranium enrichment?

Great.

Pretty good.

All right. >> Looks like 95% I think I saw.

Great.

We'll get We'll get people connected.

Cool.

Okay.

Uh first question. >> Yeah, the question is essentially um DOE contract originally was all the way out through 2034.

That's a long time.

Uh we're here today, you know, almost a decade ahead of that.

What do we do?

People are doing turbines.

How do we scale up to actually make this relevant?

And then, what about space?

And so, uh you know, our timeline is much faster than the 2034 timeline.

So, our whole goal, because the industry needs it, is to be online before the end of the decade, and then to be scaling very rapidly from there.

So, we hope we can be on a useful timeline for any reactor that's trying to launch and scale up.

So, as they're doing the deployments, you know, first criticality in many cases this year, demos next year, it's really scaling 2028, 2029.

Um we hope to be to be really ready for them as they're really scaling.

I think most of the real hockey stick that you'll see on these big picture charts that we looked at, that'll be early 2030s into 2035.

So, we're going to see one-off deployments, you know, I think in the next couple of years, tens, not hundreds of SMRs.

And then, for the really big builds, those do take 5 to 10 years to do.

Um gigawatt scale reactors, and so there's a little bit more time there, but we're trying to be well ahead of everything.

So, our time frame acknowledges that, I think.

You know, getting back to then the the turbine question and and natural gas.

Yeah, it does take 5 years plus to build a gigawatt scale reactor in the US.

Um, you know, and that's probably being optimistic.

And so, in the meantime, you do need to find something else.

And so, people have found the stranded wind.

They found, you know, natural gas pipelines that they can hook up to.

And then you need the turbines.

But now, the turbines are sold out a couple years.

You know, you might need grid interconnect like a lot of that power electronics equipment is is out a couple years at industrial scale.

So, I think the next couple years are almost going to be the hardest of how do we keep scaling?

How do we not hit the wall while we wait for nuclear to come in in a few years time frame?

And then you asked about space.

And I think the space approach is one that really only one company can do.

And it's an answer to all these questions.

And there's some technical challenges that they're going to have to solve.

But I wouldn't bet against SpaceX in solving technical challenges.

But that'll be their solution.

I think it'll be uniquely their solution to just put sun-synchronous, uh, you know, data center satellites in orbit.

Other people really can't do that.

And so, I think everything else will be fought either as like that's the that's by air.

Everything else will be a ground game.

Um, and maybe some some in the ocean.

But I think it's going to be dominated almost with every every other company by who can scale power on land and therefore who can scale nuclear.

You you know, you don't think our friend Jeff Bezos is going to find a way to also find a comparable solution in space?

Um, I I think everyone's I think even even SpaceX would say they hope for that.

Certainly in the early days it was like we don't want this whole industry just riding on us.

We want let's the whole goal of SpaceX is make humanity, you know, multi-planetary.

So, end goal is that SpaceX felt like they had to do it.

If other people could chip in, that's something they would want.

But if if you just look at the actual launch volume of SpaceX versus Blue Origin, it's just drastic and and Blue Origin started before SpaceX.

Well, Blue Origin has the advantage of using AI now to accelerate all this engineering operations, which SpaceX didn't.

You You guys had to do it all from Sure.

That's fair.

Yeah.

Okay. >> We'll see how good the AI engineering agents are though.

Yeah.

I guess this is what next year's class is going to be about, Mike.

The space race.

Yeah.

Um, okay.

Next question.

Yeah.

So, question two-part question.

One was What was it like early days SpaceX and how that shaped how I thought about engineering?

And then two, why did I decide to leave SpaceX?

So, uh step one was part part one of the the question.

Really, when I joined, I was an intern at first in college.

The it was like 35 people roughly.

Um, you know, we were just trying to get the very beginning parts built and and working.

And so, it was everything from let's build test stands that we're going to test the the engines on.

My the part I worked on was propulsion systems.

And I was like a structural thermal analyst on the propulsion team, which was low single digits sort of team.

Um, and so, we had to design the test stands.

We had to design our very first most primitive engines.

Um, you know, like heat sink-based engines.

We weren't even doing full nozzles.

It was just, can we get the combustion to work right?

Let's build the test fixtures.

And so, it was relatively scrappy.

It was how can we make a lot of fast progress?

Uh we don't need to make the fanciest test stand ever.

It just has to work.

And so, let's do what's fast and relatively cheap.

Um and optimize for the things you're trying to optimize for.

And so, back then it was purely schedule optimization and some cost optimization with a hard line on safety.

Uh and so, if you satisfied those things, it was, yeah, let's get it built and let's get it out there and let's test it.

And then we'll learn a bunch and then let's we'll do the next thing.

And so, it was really just like, okay, how many of these steps can we just chew through and and get to the finish line?

And so, fast forward all the way um through 20, you know, 2025, 2026, 2027, we got the engines developed, they were working great.

We got the Falcon 1, the first rocket, built, launched a couple times.

First time it didn't make it that far.

It had a fire inside the engine bay area due to a broken like a an aluminum nut on a on a fitting on a on a fuel line that was hooked into a different part of the engine and and that crack led to a a fuel leak which caught on fire and and took down the rocket.

Second one basically worked.

Got all the way to orbit, not not full orbit, but second stage deployed and you had a fuel sloshing issue where a lack of extra baffles allowed basically a spiral to form and and second stage went out.

Um And then at that point everything, you know, shortsightedly to your second question, I felt like, "Okay, the rocket works, the engines work and maybe it's going to be as exciting as it was in the early years.

You know, here's this example of this really important company, SpaceX, founded by someone who's an engineer with some business experience.

Maybe I need to go get business experience." And so that was my conclusion, but I think it was the wrong one.

As it turned out, the company scaled another, you know, over 10x.

Um it got to do like people who have stayed there, a lot of my friends have gotten to work in some of the coolest projects that anyone could work on the past decade.

And it was absolutely the right place to be for a lot of reasons.

So I think at the time though I felt like, "Oh, 100% company, that's that's a big company.

Like you've got to be at startups when they're three people." And you know, I felt the same thing about Palantir at one point, about Square at one point, thought about, you know, dropping out of different things to go work at these places, but felt like, "Oh, maybe maybe 50 or 60 people or 80 people is too big." And again, completely incorrect.

Like 100 people is actually just where you get into the really hard stuff of scaling a business, seeing how you go from ideas and just product market fit to actually operationalizing and executing.

Like the people who I know who were at SpaceX during that window of like 100 people to 1,000 people, those are the real operators.

Like they know how to build and run teams.

They know how to do manufacturing.

Like even the people all the way up to 10,000.

So there's Yeah, there's still Um yeah, two more orders of magnitude to go of learning.

And so uh definitely, you know, ended up doing a lot of cool stuff that I've been excited about, but also really great decision to stay there for everyone who did.

Yeah, uh the question was how do How do you grapple with the perceptions of nuclear power in the US and then anything we can learn from Europe?

Um man, the Europe one is really almost a tragic example of There's plenty of learnings there.

So uh you know, Germany completely shut down its nuclear energy program, shut down its reactors, reactors that were working fine um with the idea being well, we're going to shut these down and we're going to do renewables.

And then if you look at empirically what's occurred, they have not replaced it with renewables.

It's almost entirely replaced with base load, which means uh coal, natural gas, fossil fuels.

And the the um the consequence has been obviously carbon emissions, but even like air quality.

You can look at air quality maps of Germany now with no nuclear versus Germany before versus France, which has a great percentage of nuclear on the grid.

And it's like, you know, you look at their quality and it's like completely blue and and clean over France and then completely red over Germany.

And there's there's other reasons for that, too, but it's like why why you know, it's just completely self-defeating to to turn off affordable energy, very cheap energy once it's built, that's clean, and replace it with, you know, burning biomass and fossil fuels.

Like, no reason for it.

So, I think I think that's a real-life, like, present-day example of what not to do.

And, you know, that doesn't mean that that alone doesn't prove that you should go build as much nuclear as possible, because you could say things like, "Well, um it is expensive to build up front.

Once it's amortized, keep it going.

But, it's expensive to build up front." And I think that's actually the next thing that the industry's going to solve is how do we make it much cheaper to build up front.

And so, that's both on, you know, you see a few startups doing nuclear development businesses, um things like the nuclear company, Elemental, Oppenheimer Energy, the grandson of Robert Oppenheimer I Oppenheimer.

Um and you see all the SMR companies that are saying, "We can build these things in factories, make them much, much cheaper, shippable, install at the site.

And then, all you need is this fuel source that, currently, the US doesn't produce, and you know, on top of not producing the conventional.

So, I think the way that we grapple with perception is you know, fortunately, perception on its own is getting much better because of all these examples, and people caring now about expanding the grid and doing it cleanly, there's only one option, it's nuclear.

Um and and you look at the charts of, like, for and against nuclear, and they've gone from, like, mostly negative on nuclear to just completely crossing the past few years to where public perception is now positive on it.

And so, um fortunately, you know, we're working on something that we felt like was the absolute the right problem, but, you know, the consensus has moved along with that really quickly.

Yeah, so the question was, "Kazakhstan, you know, huge producer of uranium, I think uh 40% um worldwide.

And then, you know, okay, there's that world production, and what what should the future of this look like in the country?

Um And I think like going back to you know the the five steps in the supply chain different countries probably want to focus on the things that they are uniquely able to do.

Uh Kazakhstan, Canada, Australia, a few other countries have incredible uranium ore deposits that put them you know in the lead for production.

They can produce a cost that no one else can with whether it's like existing mining technologies or more modern ones.

Um And then okay, what should these next steps look like?

I think one idea that we have on all these steps is ideally they're co-located.

At least the ones that are involved like chemical processing.

And so why scatter these things across the country?

And right now it's completely you know very scattered across the country due to the the history of it in the US.

Um And then how do we think about our specific step of of enrichment?

Our goal long-term is same goals that SpaceX had.

Like bring back this technology in the US.

Use it to help scale the industry.

Do it at a much lower cost structure.

Um And by doing that we hope you know there's going to be a lot more fuel production, a lot more nuclear energy.

And so our goal is actually for countries that don't do enrichment um you know US first and foremost, let's solve the problem here.

But if we have allies, let's do it for them.

Let's do it at incredibly low cost that you know leaves little room for anyone else to really worry about it.

Which then has a huge downstream proliferation uh benefit of you know fewer countries saying well I need to do this.

Um which then leads to a whole lot of complexity from geo uh geopolitics perspective that's way above my pay grade, but I know if you know if we can help solve this, it seems like a good thing on so many levels both for like power production, more clean energy, less fossil fuel like carbon emissions, um less risk of worldwide like proliferation of nuclear weapons, and on and on and on.

So Um could you actually take a few minutes?

I realize we skipped over the five steps in the supply chain for uranium.

If you could walk people through like step-by-step what's going on.

That's the That would be the the general matter or like the the the the uranium version of the pre-training, mid-training, post-training.

Right?

Could you walk through that for a sec?

Yeah, going back to the reactors, you need to put fuel in them.

They consume the fuel.

They're ultimately burning up U-235.

That's the fissile material.

That's what's going to have the chain reaction that releases neutrons to make heat.

You take the heat, heat water generally, run a steam turbine, and you make electricity off of that.

And so, okay, we need fuel that has relatively dense U you know U-235 content by weight.

And the way you do that is you get the you get the mined product.

You then convert it from U308 to UF6.

You then enrich that UF6 gas, which is again a refining or separation process.

You then have a gas that's not going to help make fuel rods.

You need to turn that back into a solid through a chemical process.

And then you take that solid and you form it into whatever pellet shape you want.

And so, the step that we do is simply working with the gas and separating it.

So, in our facility, there's no nuclear reactions.

We're not a nuclear reactor.

We specifically avoid any nuclear reactions by keeping material spread out enough so that it can't form a critical mass.

And then there's no chemical reactions.

It's a separation process.

Um And can you talk for a second in that five-step process from mining to fabrication?

Why Why is the United States historically done so badly on enrichment?

Whereas on the on all the other parts of that supply chain, you know, there's there's options in the US.

Yeah, well, historically we did really well, actually.

Um in the '80s, we were about 86% of worldwide capacity on enrichment.

And it occurred in a couple you know, a few different sites across the US.

You know, you you take that all the way through the Cold War, that's when we really reach it, you know, our peak.

The US was providing all of its own utility power through enrichment at DOE sites.

Right.

They were government-run.

Um they were former either Manhattan Project or Cold War sites.

And so, with the fall of the Berlin Wall, though, we said, "Okay, you know, there's now more free trade.

We can now trade with Russia." Russia had all these warheads that it was in everyone's best interest to start disarming post-Cold War.

And so, the US had a program called Megatons to Megawatts, nicknamed that, Right. uh where we took the weapons and we we down-blended them and we ran them in our reactors.

Um and as a result, you know, we said, "Okay, we actually have the supply now.

We have more free trade.

We can we can actually get this from Europe." Our technology is actually relatively expensive that we were running at the time, very uneconomical compared to what we could get out of Russia or Europe.

And so, we said, "Let's just let's just do free trade on this." Um you know, the entities that ran uh the enrichment plants in the US had a hard time at that point making money on them and said, "Hey, it's time to sunset these." And so, that was 20 The last of those was 2013.

And so, since then, it's been decommissioning and you know, preparing that site back for other industrial uses, uh which is what we're doing.

Um and so, it was really a path dependency of we had a certain technology, it was not globally competitive, the Berlin Wall fell, we started trading with Russia, Europe even more, shut down what we had, and then, you know, I think there was a People probably had plans of how, you know, we'll bring back enrichment when we need to, and I think the need is just coming much more quickly than people would have expected.

And as a recurring theme, we are now back to the future, basically, of uranium enrichment.

Yep.

It's like we were doing historically well, 20 years of stagnation for whatever reason, and now it seems like AI has reignited the trajectory that basically took a bit of a detour, but we're back on track now.

Yep.

Roughly speaking. >> Yep.

Yeah, very similar to many other industries, similar to the space industry.

It didn't mean that it was as simple as, you know, just reassembling the space shuttle or rebuilding Saturn 5.

You, you know, you want to do things leveraging all the progress of the last few decades.

And so, you are going to always want to start clean sheet and and question everything.

Right.

Um and that's what we did.

And so, many, many very exciting engineering uh challenges and problems to work on.

Um but that's that's the fun.

And and uh to borrow Peter Thiel's how far are we from flying cars now, even though we only got Twitter for a while?

Uh probably closer.

Closer? >> Probably Well, I mean, you look at all There's uh not that far away, actually.

You look at Joby and and all these other companies. >> Flying cars for final project.

Thank you so much, Scott. >> Yeah, thank you, guys.
