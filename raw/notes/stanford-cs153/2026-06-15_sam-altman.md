# Stanford CS153 Frontier Systems — Sam Altman: "Scale, AGI, and the Future of Everything"

**Speaker:** Sam Altman (CEO, OpenAI) · interviewed by a CS153 co-instructor (Anjney Midha, a16z)
**Channel:** Stanford Online · **Upload:** 2026-06-15 · **Duration:** 41:10 · **Views:** ~62,138
**URL:** https://youtu.be/F_7M4Hc-usM
**Source tier:** Tier 5 (book-talking / OpenAI demand-maximalist) — discovery-only, never cited as vault fact. Every spoken number is soft → verify at primary.

## Transcript (Tier 3/5 — not a primary source)

Please join me in welcoming Sam Altman. >> [applause] >> This class was designed as an inspiration from us, you know, from a set of different experiences while I was a student here.

One of them was Terry Winograd's intro seminar CS 47N computers and open society.

But a second one that was a pretty formative experience for me and a lot of my friends and peers on campus at the time in 2014 was CS 183 How to Start a Startup by Sam.

And so it's really cool to have you back.

What's it like?

How do you How's it feeling to be back? >> I was thinking as I was walking in if I had just a little more time I would do an update to that class because I think everything about starting a startup has changed so much.

And I have not seen anyone do a good version of how you're supposed to make a startup now.

So I had that like just walking in here.

I had that like it'd be fun to do it again. >> So timeline-wise, yeah, you you taught that in '14.

I think OpenAI was founded in 2015.

Is that right? '16 basically. '16, okay.

So So then you went, you know, it was like you were it felt to me from the from an observer perspective that you had like come up with your working theory for how to do it right and then you went and tried to implement it.

Is that Is that a fair assessment or is that not the case? >> OpenAI was like the strangest startup of the last maybe a couple of decades in Silicon Valley cuz it started as a research lab.

It was It was really not a company at all.

Um and that the kind of normal course of of startups is that you start a product company and then it like grows for a while and then growth slows down and then you start a research lab and you like bolt that on and you try to figure out the next thing to do.

And we were the opposite of that.

We were a research lab first that later had to bolt on a startup, right? >> And uh >> I don't really recommend that.

It's kind of an unusual thing.

But that that's not quite what I meant.

What I meant is like we still followed the pre-AI rules of a startup because we were trying to make it out.

We didn't have it yet.

But now like watching what the best startups do is so different than how startups worked even a couple of years ago um that I think someone I'm probably not going to do it.

Someone should do that class again. >> And what would be the biggest updates you'd you'd make based on your data? >> Um you with like an affordable amount of spend on tokens you can do what a 100% incredibly great engineering team would do as a startup.

And that was just totally impossible.

That was like not in the set of options for a startup and now it is.

So So I think what you can take on the level of ambition you can have, the speed of which you can move, the amount of stuff you can do at once is just totally different. >> And does that change the shape of the problems you feel like you'd assign at the end of the class for people to attack, you know, at the end of that quarter if you were teaching it again? >> I don't think assigning problems to attack ever works because if you like if I can think of a problem, if I can think of like a really great startup idea, if it's like obvious enough to me, then it's probably obvious to a lot of people.

When we started OpenAI, we were we were like the you know, one of maybe generously speaking four AI efforts in the world, right?

And you want to find something like that.

And I'm sure that there exists something today that just wasn't possible at all pre- like automated coding era that is totally and not obvious that will be, you know, uh multi-trillion-dollar market soon and that only four companies are working on right now.

But I I know what that is.

It's much more likely you all know what that is than I know what that is.

I just, you know, my brain is like taken over by open AI.

Um but you know, the kind of idea someone can assign you to work on is probably not what you want. >> Yep.

Um okay, so that that's fair.

Um but I I think it'd be helpful, since this is a systems class, to maybe uh reason about a particular problem that you have to reason through so that they can then apply the shape of the techniques you used to break down from a systems perspective that problem into solutions to their own problem.

Yeah.

Um and a and a concept that uh you had started to tease in the class, you know, back in 2014, and then uh clearly you've talked about publicly over the years is um scale.

Right?

Scale is its own beast.

It's it's it's you know, quantity is its own quality.

You know, what what scale as a concept has been something it seems like you've um empirically investigated in all kinds of ways over the last 10 years.

So, um could you help on help us first unpack like what you mean by scale now 10 years later?

How would you deconstruct that as a systems design uh attribute to apply what is it as as a tool?

Um can can we start there?

Yes.

Uh so I don't know why the following observation is true.

I offer no theory that I find satisfying to explain it, and that makes me a little bit nervous suggest you follow it, but I'm going to anyway, because empirically it does seem to be true, which is all of the most interesting things I have observed in my career in watching other uh things happen, all of the most interesting ones uh have had something to do with emergent properties that scale, or scale continuing to provide returns far beyond what the consensus thinks will work.

And this obviously happens with like scaling laws for AI models, um but this happens with uh you know, getting more smart people together to think about one problem.

This in a in a research setting, um this happens with uh companies and the sort of economy of scale you can get all the in all these different ways.

I really learned this at Y Combinator when uh it became clear to me that everybody was saying, "Oh, Y Combinator's gotten too big.

It should shrink.

We should fund less companies per batch, you know.

The best times at Y Combinator were when it was like 10 companies per batch." And a lot of like very smart people were saying this.

And and it was like tempting cuz it would have been like much less work and the theory was that, you know, the best companies are always kind of obvious and then you fund the rest and it's not as helpful.

Um but a huge part of the magic of what made YC work were uh was the sort of the network effects inside of the batch.

And that was an emergent property at scale that just hadn't been discovered before.

No one had tried to fund startups at scale in the same way and and thus no one had ever happened upon this observation of when you do that um there's there's something important that happens that just didn't exist at all at the one at the 100 at the scale.

There's a bunch of other examples like this.

Uh and I'll skip them in the interest of time, but I I would say again, I offer no explanation for why, but empirically speaking, when you find a time that you can push on you can push something to a scale people have not tried before and it's already working in some interesting way at the smaller scale, more often than not, that seems to be a good idea.

And it also seems to be something that most people don't do enough.

Mm.

And I don't have offer an explanation for this either, but like in, you know, when we were like, "We're really going to scale AR models." Um all of the like geniuses in the field, most of them were, "Oh, this isn't really working, you know, that's that's barely a scientific result.

It's not interesting that it gets better at scale.

You've already shown that.

Why keep scaling it?

So, I mentioned the YC example.

Um I've seen a lot of startup founders where they're like, well, you know, there might be something interesting that would happen if I scaled this up, but I'm a little worried about it for non-specific reasons.

And again, looking back at like a huge data set of people that have scaled their companies in all these different ways, there's almost always interesting stuff there.

So, I think directionally that's like an interesting thing to push on and end severely underexplored.

Um on the systems design part of that, uh I think one reason people don't do it as much is stuff breaks uh at an accelerating rate and in an unpredictable way as you scale it.

And if you are going to really scale something, um it's always like a little bit broken.

There are always like very smart people who say why you shouldn't do this, you know, don't get too ambitious, don't get too big, let's try this smaller.

And so, breaking that down as a systems problem, I'll use the thing of when we were like scaling up AI models, there was technically can we do this at all?

This seems crazy.

Like no one ever thought about trying to do a run across 10,000 or 100,000 GPUs and that was going to require stacks of engineering talent.

Um there was the capital requirements and what was going to take to do this and like how is there ever going to be a business?

How going to think about taking this risk?

Uh there was the sort of like cultural stuff of researchers saying, well, if we're going to get all this compute, why do we put it all into this one project?

We're not going to run into something.

Why not divide it up among all these all these projects?

And this also happens in kind of every area I've looked at almost every area for scale.

And breaking it down into the sort of each difficult area or each reason not to do it and trying to address them one at a time.

Yeah, that's been really important.

Um I'm going to push on that a little bit because there's very few people who've been able to so s- repeatedly scale new products and systems the way uh the OpenAI team has over the years, but it seems like one of the issues is there are all these prior conditioning and sort of mental models and expectations humans have, and you said things break.

And one of the things it seems often breaks that's hard the hardest to refactor is is human the human side of the the system's design.

All right, wherever there's human implementers or there's uh human participants in that.

And so, what have you learned about humans at scale?

Like organizing humans at scale to participate in a system that may not be uh like just a a redo of some past system that they they get naively on at a priori on first blush.

Um I think like clear a clear goal a clear plan to get there uh and like a clear answer to the way that you're going to get there and kind of how you're going to make decisions along the way.

That's that's very important.

So, um you know, if we go back to the example of when we decided to scale up models, there were a lot of people who are like, "Ah, this isn't really going to work.

It's going to have these problems.

It's also not, you know, we need a more diversified portfolio." But once we say, "No, we're going to make a bet on scaling deep learning.

Like that's our thing.

If we're wrong, we'll fail, but we're going to do that.

Here's why we're going to do that.

Here's what we believe about what the state of the world can be like if we get there." Uh that's very powerful.

And then for whatever reason, um we did not evolve to be good at thinking about exponentials.

People have a hard time imagining that scaling laws are going to continue exponentially, that revenue will grow exponentially, that an organization can take on exponential complexity.

And in my experience, it takes a lot of time to really reason through first principles with people about what what that can happen. >> Can we take two examples to walk through that?

The first being ChatGPT and the second being Codex.

You know, both of these have transformed Can I Can everyone hear?

I'm going to try to project it.

Yeah, okay.

Um so, let let me put in a frame and you can challenge both the assumption and then we can hopefully reason to example what happened.

In the case of ChatGPT, you know, for a long time in skating of models, a big mental block that seemed to be prevalent in the space is what are these things going to be useful for?

This is you know, it's a research uh sort of solution solution chasing a problem research first approach.

It's not a product.

Um and then, you know, ChatGPT came out and it proved to the world that can you know, that chat experience was a killer app for general models um at scale and for consumers.

And then a couple of years later, yes, it's clear that coding has been the killer enterprise app.

So, what what how would you compare and contrast the systems you guys used to discover those use cases, ship them, scale them, monetize them?

Any any salient learnings from those two systems?

Yes.

Um So, we had made GPT-3 and we needed to make money cuz we wanted to go scale up to, you know, billion and multi-billion dollar computers.

And we had GPT-3 and it was kind of interesting.

It was a cool demo, but we couldn't figure out a product to build around it.

And we had been thinking thinking, we just couldn't do it.

We had tried a few things.

They they hadn't worked.

Um and so, we knew the models were going to get better, but we also wanted to like start a revenue engine sooner.

And we said, "Well, since we can't figure out what product to build, we're just going to put this into an API.

And we're going to hope that somebody else can figure out a product to build." And so, we launched in like I I don't know, something in the summer of 2020 the GPT-3 API.

And initially, it kind of got no traction at all.

And then about a month later randomly as far as we can tell, it went viral on Twitter.

On the same day a few different developers kind of found got it to do something cool, posted it, other people started trying.

And and then like a lot of people started trying the API.

Um but it was shockingly bad.

If you go back and use GPT-3 or 3.5, um you will be astonished at how bad the models were then relative to the amount of excitement they generated at the time.

Uh so people tried all these things and really the only business that people got to work in a significant way with GPT-3 was copywriting.

Um and that was like not that great and not that exciting and we were kind of like, you know, ah it's just going to have to wait for a better model.

But although no that was the only business that was working, developers had figured out how to like put in a prompt and got enabled to chat with it.

And we saw this a lot.

Like more people were using they couldn't get the API to work for their business, but they were using their API key to just chat.

And we said, well, we can build a good chatbot.

People clearly want that.

And we had a new model.

We actually had GPT-4 done that we had a new model we were ready to release in between called 3.5.

And we had figured out a new kind of post training where we could get the models to do like a good job with instruction following.

So it could make it easier to chat with.

And we said, well, you know, the API is not working great.

Maybe it was like a 10 or a 20 million dollar run rate kind of business.

But there is this thing that people love uh and under the YC principle of see what your users love and do that, we said, well, we'll build a chatbot around it.

And we put that out and we still didn't think it was going to do that well.

Uh there was it was really meant as like a research demo uh to convince other people that they should build chat like products and pay us for the API.

But that one like crazy viral.

And another thing I had learned from YC is when something really starts growing and it's not very good, you have like a guaranteed hit on your hands.

And so we had like 5 days where the traffic would shoot up, fall off and everybody be like, "Well, that was just a hype cycle." But then the next day it would get to a higher peak, fall off again later in the day and people would say that's a hype hype cycle.

By the fourth or fifth day I was like, "I know how this works.

I know what's going to happen.

Like we have the potential here >> Mhm. >> at a killer product.

Um and we knew we could make it much better.

We knew we could We knew we had GPT-4.

We knew we could keep scaling.

Um but by that fifth day, we got everybody together and said, "This is an emergency.

This is the good kind of emergency, but we have to build a company and a product all at once." >> Mhm. >> Uh we then had like 2 months of crazy scaling.

Uh and we said, "You know, we have to figure out a business model later.

For now, we're just going to charge people so that we don't like run out of compute bills." But that's obviously not a long-term answer.

That also turned out just to work.

Um and that was the story of ChatGPT.

And then there was so much utility that people just had not gotten over the activation energy of mind that that has worked really well.

Um and then Codex actually the plan before ChatGPT was that we were going to go all in on code. >> Mhm. >> Um we knew these models could write code.

Uh we knew that they could be really and we knew that that would be like a valuable area, but then we had this incredibly exciting thing happen.

Um but our kind of internal belief at the time was that coding was how these models would control things on computers and robots were how these models would control things in the physical world.

And if you made a smart enough model that had sort of the actuators of writing code and robot and driving a robot, you could then kind of actually get this intelligence to do stuff for you in the world.

So, uh then it took us a while to get there.

And then I think Codex got really good by early this year, but with 5.5 is when we saw this real inflection point where people are now like doing just incredible things with it. >> And um you know, that the earlier in the class we've talked about how the capabilities pipeline uh is starting to look it is starting to become somewhat more legibly standard across different research groups.

You've got, you know, pre-training mid-training, post-training, then you've got the RL and the supervised feedback loop.

Is Do you think that's roughly like the shape of the pipeline that allowed Codex to, you know, go through a capability jump and that will basically stay stable now and consistent or are we going to go through a major rewrite of that pipeline?

I think that is definitely the current pipeline.

I expect we will go through a major rewrite.

I don't know when it'll happen or exactly how.

Um but it is a little odd to me that it's so it happens as a pipeline and doesn't quite feel like the optimal solution. >> Um what would be an optimal solution in your head? >> I think that's a research problem for the AIs to figure out.

Um I think we're at a point where we set this goal that by September of this year we will use 500,000 A100 equivalent GPUs, like a lot of computing power, as an AI research intern.

And by March of 2028 that we will have a full end-to-end very talented researcher like figuring out completely new architectures.

Um so I think we are going to get like with the current pipeline, the current architectures, I think we're going to get over the line of when AIs can do incredible incredible work.

Um you know, what one of the things that you you just described there is you you we we've been talking a lot in the class about systems, frameworks, and analogies to make concepts from one domain legible to other people who may not have all the context in another.

And that sometimes because of the translation problem you know, reasoning by analogy is not helpful because then errors compound. >> Yeah. >> Um right there you said, you know, our goal is to try to use it as an AI intern, which obviously is a very useful metaphor within the context of you know, Silicon Valley a a class that understands how these pipelines work and so on and then as as you scale actually that metaphor globally, people who might not have all that context go start analogizing these models in ways that they shouldn't be.

Like how should we think about the limits of of that of of What are the limits to scale of um What are What are the product analogies, the research analogies you find most useful within the Valley and which one of the What have you found about found about the limits of those analogies scaling?

And now how do you navigate between those two problems? >> I I've been very interested in studying how that I I think what is happening is we are we are in the process of creating a new utility.

This doesn't happen very often.

You know, electricity is a utility, internet's a utility.

There water, I guess.

There's not a lot of these.

Uh and so there are not a lot of examples that we can study for good metaphors or learnings about how to explain this to the world.

Um but I was recently looking at what happened when electricity became a utility.

And it's a good analogy for many reasons.

It's imperfect, of course, too.

But the electricity companies, at least the ones I could find information about, they didn't talk about selling electricity cuz no one knew what that was or why they wanted it.

It sounds like very scary.

It's this thing that's like going to come into your house and it could kill you and it's like very some way and you you know, it feels sort of like very different than the world before.

Uh and maybe they tried to sell electricity or market electricity at first, I don't know.

But at any case, that didn't work.

And then what they started marketing, selling to people was light at nights.

You know, we are going to what you are getting from us is not electricity, it's light at night.

By the way, you can use the same thing that lets you get light for all these other things, but people are like, "Well, why would I want that?" And I'm like, "Well, you know, it'll wash your clothes for you someday." And they're like, "No, no, I won't.

I can't.

That's too far of a jump for me." >> Right. >> Um so, I don't know what our analogy for this should be.

Um but I suspect that even if even if we're totally right and intelligence is going to become this new utility that every company, every customer, every government just needs access to and is going to use in all sorts of incredible and you will have like a OpenAI token subscription that you will plug into everything and use to access everything and you have running for you all the time and doing this amazing stuff.

I kind of don't think, at least right now, the right way for us to analogize that is we're selling intelligence cuz people are just like somehow not resonating.

I don't know what our equivalent of "We're selling you light at night" is going to be, but I think if we're going to become a new utility, we need to find a way to explain to the world what it means to have this like intelligence pipe that you can just do whatever you'd like with. >> It So, um one question that has emerged an emergent property of this class is of having a diversity of different speakers is that the utility analogy has come up several times, but in reference to different things.

So, Jensen likened you to like compute to a utility.

Um and why there should be access and so on and talked about how Stanford should pool budget and so on and and and procure that as a utility for everybody on campus, whereas you just likened the intelligence part to you to are both of these things true?

Is one of them true?

One is one more likely to be true?

How should people reason about compute as a utility versus tokens as a utility?

And and by compute, I mean here chips versus tokens.

Does that Does that make sense? >> I think as a consumer, as like a business or individual, um you will think in something closer to tokens or probably even one level up from tokens.

I don't think you'll care very much about, you know, where the hardware is, what particular chip it is, what's powering it.

I think that stuff will be abstracted out.

And what you will care about is when you're interacting with the system.

Um Can you use it a lot?

Is it cheap?

Is it doing a good job?

Um so right now it's like tokens.

It may get as we move into a world where we all just have like this constant agent running for us, being useful to us all the time, um you may think about it as even one level up.

But yeah, my my guess is is when you like pay for your cell phone bill, you're like, all right, I'm buying access to airtime and some number of gigabytes, and, you know, it's going to do all these things and I'll use all these apps and whatever else, but like what you think about paying for the kind of internet utility in this case is just like access to the whole system.

And the particular hardware at the base station, now it connects to the internet, you don't think about that as much.

Um >> I know I I could nerd out about utility infrastructure for a long time, but I want to make sure we switch a little bit to being relevant for the students.

Usually we have uh questions, but we're not doing those today.

Well, unless you're comfortable.

Oh, okay, great.

How about that?

Improv.

Okay.

Uh So one final question to start getting the creative juices flowing is um the final project for this class or in 5183 is the one-person frontier lab.

So everybody here is working on projects where they're simulating being an individual uh as a lab with access to all the right tools.

They've got hundreds of thousands of dollars of credits from Cloudflare.

I think we've got some open AI tokens, maybe.

But there's a bunch of compute at their disposal.

Um what would you if you were in the class, what would you be working on for your one-person frontier lab project? >> First of all, I think that's an awesome project.

Um I think this is top of mind because uh you we we were just like talking about utility frame frameworks.

I think there's a lot of very smart people working on uh great training ideas and we're going to have incredible models, no matter what you all do.

We're going to have incredible models, I promise you uh like pretty quickly.

But I I I think we have not invested enough in being able to deliver at scale huge amounts of cheap intelligence.

So, maybe I would go work on like the inference part of the stack. >> Mhm. >> And how are we going to get this incredible intelligence to be cheap and abundant?

Uh I think that's under invested in and and I think all of the frontier labs are going to have to become inference companies to a significant degree. >> Um okay.

It might be too late to pivot your projects, but better late than never.

Work on whatever you want to work on. >> [laughter] >> Uh okay, let's start taking questions and I'm going to moderate and try to be not you know, please try to be productive and not spicy, et cetera.

Remember, it's a CS class, but up to you, Sam.

If you want >> Spicy is fine. >> Oh, we got questions.

Oh, perfect.

All right, first one.

The question's about your views on Yann LeCun's view that LLMs are a dead end. >> Um first of all, in terms of achieving human-level intelligence, these models have already far surpassed human intelligence in some ways and then they're wildly worse than others.

Like for example, they seem much worse than people are at very long horizon kind of high judgment signal and tasks.

Um on the other hand, yesterday we had one of our models uh discover uh disprove a conjecture, one of the Erdős problems that had smart people had worked on for a long time.

And a lot of people, a lot of smart scientists, I don't know if LeCun is one of them or not, had even quite recently said something like that was not going to happen.

Uh and then like the model just did it and you know, now you have all these mathematicians saying like, is math over?

What does this mean for our field?

So, clearly LLMs are capable of figuring out new knowledge, and clearly they are capable of doing some things that some intelligence tasks that humans just can't do.

Um they are going to scale much further.

So, how much better and what distribution of the tasks they can do better than humans, we'll find out, but I suspect it's a lot.

And the, you know, in terms of this like lack of a belief in the exponential we were talking about earlier, um I think the field was honestly held back by a generation of scientists who just were way too certain on what wouldn't what what scaling was not going to produce.

And then some people just looked at the graphs and said, "Well, it looks like it's continuing beautifully.

Let's keep going." Um I think world models are clearly important, and to we'll need that for things like robotics, uh but betting against LLM scaling at this point uh feels quite misguided to me. >> Does it Does it get annoying to be the I told you so guy? >> No.

I mean there are these like Twitter trolls that, you know, for years have just been like, "It's not going to work.

It's not going to work.

This is so dumb." Like, you know, "This is a fraud.

This company's going to fail.

This research approach is going to fail." And I used to get more bothered by them, but I don't even like feel the I told you so at this point.

It's like, you were just here like she's never going to You're still going on about it.

Like the data is right, quite strong on our side.

And I don't need to be that fun to say I told you so, and also the fact that you're like still saying we're wrong doesn't really bother me. >> I think there's that kind of move on.

There's that saying that like insanity is doing the same thing over and over again when presented with data that is not working, and they keep repeating that.

And in a sense, it's it's it's a form of insanity, I think. >> I I think there's something that happens, which is if you make your identity about a particular thing is going to work or not work.

And you associate yourself with that belief, and then the science or the empirical results disprove you, and you're like too hung up on your identity, you can't let it go, you can't see the truth. >> Yeah. >> And I think this is like a important reminder in both directions. >> Yeah.

How do you see education? >> Um it clearly has to super adapt, and I am worried I I thought by now it would have.

Um the the I think if we continue to teach and evaluate students as if we were in a pre-AGI world, um it's not going to work, and it is going to lead to like atrophy of learning how to think or whatever.

And I thought that was going to be obvious enough that I wasn't that worried.

You know, when ChatGPT launched, I was like, yeah, we're going to have 1 year of like students like cheating and not learning that much, and then the educational system is just going to redesign itself, and there's and we're going to teach people so much better.

You know, people are going to really get projects where they have to they have to use AI to be able to do it, but they still have to like stretch their brain more and think more and figure out new things to do.

And honestly, I struggle to point to any significant systemic change that I've seen in the education system at large in the 3 and 1/2 years since ChatGPT launched, and I that was a prediction I had for me.

I thought I thought that would have happened.

So, I have no doubt that we can uh likely have done what every other technology we before redesign how education works so that you still have to learn how to think.

And there will be some things like I I I am a person who thinks by writing, and I write a lot of stuff that I never show anyone else, but it's still important to me to figure something out, and so I'm grateful that I I learned to write.

People say the same thing about programming.

Um so there will be some things that we teach people to do that machines can do better just because it's helpful to teach them the meta skill of thinking and learning and that makes sense, but there are a lot of other things where we should just totally teach totally change how we teach or how we learn or how we evaluate and if we don't do that, I think there will be like significant atrophy in people's critical thinking skills. >> Uh question is what was your favorite class and what what do you wish you'd taken while when you were at Stanford? >> Does Stanford still do intro sims?

I did like all the I did like three intro sims a quarter in my freshman year.

Like and I loved all of them.

Uh they were all super different.

Uh I but looking back, the fact that I was able to get such a broad exposure to stuff and have like a a very shallow understanding of lots of different fields was an incredible thing.

If it had not been for that, I just would have taken like CS and physics classes, which still would have been great, but um I think more about the stuff the classes I took that were like totally random and unrelated to what I do now, but in some important way gave me a perspective than I do I think I would have like learned to program no matter what.

Uh so and I didn't think that at the time.

I was like kind of like, "Yeah, you know, this is this stuff is all cool, but it's mostly going to be about like learning CS." Um I only did 2 years of school.

Uh so there was a lot of stuff I wanted to take that I didn't get to.

Um but that's kind of the surprising thing. >> My question is What is your spiciest take of all? >> All right.

I I think with more time to think, uh I could come up with a much spicier one, but um I think AI is just going to keep going and I think this is considered I don't I don't I this is like widely believed yet.

And I think if this were widely believed, there would be like significantly more reverberations than are happening through society right now.

And maybe I don't have the space or take.

Actually, maybe this is the high order bit that if AI progress continues on the exponential that it's on for another It's been 3 and 1/2 years since ChatGPT came out.

Even if we're another 3 and 1/2 years on that same trajectory, the world the potential, the way that society, what's society is capable of are just completely different. >> Well, let let me try to prompt you with more thinking tokens on that one.

Um You you have if we treated you as a model, like as a frontier model and you have some inherent capabilities and we're going to we're going to try to elicit capabilities that people don't know about for the next 2 minutes.

Um one of them is that you've been post trained now on you you've been continuously RL'd on OpenAI as well as the external feedback loop of the world on what doesn't work and what works and doesn't work.

So now, if we're going to treat you as a prediction engine for a sec the prompt is what are the three most likely forks of the universe you see over the next 10 years?

And what is your what is your probability assessment on each of those?

Does that make sense? >> One that feels very important is uh like how much is this technology going to be very widely democratized versus how much is it going to sit in a few companies.

I I think a world There are all of these reasons why you could imagine the default is that this gets concentrated to a few companies and they become like you know, a significant fraction of the wealth on Earth.

That would obviously be terrible and we work super hard to push against that.

But I think that's going to require like the will of the world to to really avoid um because there is a sort of attractor state there.

And I think part of the reason that we need to push to this kind of utility model of the world is that A, it's quite unstable and quite bad and will feel quite unfair if a few companies have all of this, but be I think there's a real alignment failure in a very fragile world and the best way to get to a world we want that represents like everybody winning and everybody's values being represented everybody having agency is to just put push this technology out into the world.

Um but there will be a very strong argument against that around sort of safety and stability.

And I think that will be a big fork and it's very important.

I encourage all of you in your careers to push hard that this is a technology.

It can bring us an incredible sci-fi future.

Life can be unbelievably much better.

We are going to incur some risk to get there but the risk of keeping this concentrated in a handful of companies even though we would be one of these companies is not something we should tolerate.

So I think that will be a big fork.

Uh in terms of probability I think it's the world should have such an interest in it happening this way that I think it's like 80% we end up on the democratic path.

But there will be a very strong safety message and you know, there will be a lot of power seeking people who who want to concentrate the power.

And >> What one of the problems with forecasting this or that you have and we all have as humans is once you make that forecast then you have agency to affect the forecasts.

Right on the fork. >> Well, I mean we're clear on what we're going to use our agency for like this is what we believe in we think that uh you know, we're going to do everything we can to push it in this direction.

We just we see the forces in the other direction.

Maybe a related fork uh there's a lot of talk about like future economic models and are we going to do universal basic income are we going to have everybody gets to like own a slice of every company like are we going to is it capitalism and no change is it like full on communism?

There's like a lot of talk about this.

One thing that I think is not talked about much is how specifically how we distribute compute.

Mhm.

So maybe a lot of the economy can in a way that it's going to work.

And I've actually I've become much less of a even short-term jobs doomer.

I've always been optimistic we find new things to do, but this may not even be as disrupt as disrupted as I originally thought in the short term.

Um but we are seeing compute shortages now.

I can imagine them getting much worse, and I can imagine compute being like the most important utility that people need.

Uh so, if the price of compute from a supply and demand perspective gets way out of whack, then I think there will be a very interesting fork about what it means to equitably distribute compute. >> So, you said two very interesting things there, which you said on the economic side we might have need universal basic income, everybody owns a piece of shares.

You know, one of the speakers in this class is um Nicolai Tangen, who runs the Norwegian Sovereign Wealth Fund.

He's awesome.

You know, this Norwegian Sovereign Wealth Fund owns 1.5% of all publicly traded companies on the planet.

They also have effectively universal basic income.

You could argue there's flavors of this already today because, you know, the largest employer now in the United States is the government, and you could argue like large sections of that are a way for the government to redistribute income from taxpayers.

So, are these solutions that actually need to be novel or just reimplemented for this era?

How do you think about the novelty of those solutions where we often, you know, in Silicon Valley make have this tendency to be like reinvent, you know, old things from first principles.

And so, should we just look to existing systems and tweak >> Yeah, I don't think that these things require deeply new ideas.

Although, I will say um I am much more excited about people having some sort of ownership stake than a fixed monthly cash dividend. >> Right. >> Um and I I funded like a big universal basic income study a while ago.

I've also watched what happens when people like invest in startups, and I know which model I think like hits human psychology better.

So, what I would love to see is as leverage in the world shifts from labor to capital, which I think is going to keep happening, that we find a way to have something like a citizen's wealth fund in the country or in the world eventually, where you like you basically own a slice of capitalism, right?

Own a slice of these companies. >> And then on the second fork there on compute bottlenecks, you said uh at some point when compute prices Between January and this year, my my current understanding is based on data we've seen that H100 prices and Blackwell prices the spreads between long-term reservations and spot is like 5x. >> I don't know if it's that high anymore.

I think it got a little better, but yeah, it's high. >> Or if you can even find H100s cuz they're pretty much all gone for this year.

Does that sound right? >> No argument.

There's a gigantic computer shortage, yeah. >> So, that's a good example of an of a systems problem right now that's live.

At least to some folks, it feels like COVID, you know, for the computer era.

Like all the toilet paper's gone.

Yeah.

Why are people not freaking out about this? >> Well, I think people assume we will make big inference gains on the hardware we have.

I also think there is a tsunami of hardware coming. >> Mhm. >> But maybe the demand tsunami is even bigger and I think people should be freaking out somewhat. >> And And would you say it's fair Like how long are we going to exist in a computer shortage at least you know, based on current data you have? >> I think like other you know, you can't talk really about like worldwide demand for electricity without talking about the price.

Like it's there's an extremely different demand about how much energy people need to use in the world if the price comes down by a factor of 10 or goes up by a factor of 10.

And I think AI is like that, too.

Uh the if we can make models sufficiently smart and it's a sufficiently low cost, I think demand is like kind of uncapped.

And so in some sense, as long as we can sit continue to make progress on this, there will be a shortage forever.

And things will be bid among above what the price we think we think the price should be, even though people are getting better, smarter, more, whatever intelligence.

Just because you can use like if we make really great personal agents, then you can have 10 of them running and working through all the time or 100 and you know, you'll want 100, I think. >> It's a lot of inference.

A lot of compute.

Awesome.

With that, I'm going to give you the swag for the class, which is >> [applause] >> Thank you for coming. >> Thank you.
