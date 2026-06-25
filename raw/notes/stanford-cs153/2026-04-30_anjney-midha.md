# Stanford CS153 Frontier Systems — Anjney Midha: "Frontier Systems" (course-framing lecture)

**Speaker:** Anjney Midha (Founder, AMP PBC; a16z; CS153 co-instructor — the interviewer in every other lecture; founding-investor/co-founder across Anthropic, Mistral, Black Forest, Periodic Labs, etc.)
**Channel:** Stanford Online · **Upload:** 2026-04-30 · **Duration:** 1:05:55 · **Views:** ~17,854
**URL:** https://youtu.be/O5PfU_uDhS0
**Source tier:** Tier 5 (a16z, HEAVY lean — runs AMP PBC compute-provisioning + invested across the lecture companies; "context is where value accrues" + "compute is not a commodity" both serve AMP/a16z's book). BUT this is the framework lecture — the AI-factory stack + four-bottleneck model the whole corpus is organized around — and the infra-cycle history is genuinely informative. Treat like Jensen: discount magnitudes, keep the framework. Discovery-only; spoken numbers soft → verify at primary.

## Transcript (Tier 3/5 — not a primary source)

How many people have been to Coachella?

Oh my god, we've got to do a field trip, Mike.

I know.

Yeah, okay.

Maybe final project, surprise project.

Go off.

Yeah, yeah, off-campus field trip.

So, usually when you have a um uh when you go to a concert, for those of you we will I will we will make sure that you get to a concert, a real one.

Uh when you have a headliner, you need an opening act, right, to warm up the audience.

And so, uh today I'm your opening act for the rest of this quarter.

We're going to have Mike uh in the coming weeks as well, who's going to be doing uh a deep dive into a bunch of confidential computing stuff, but I'm here to give you some context about the speakers and the rest of the class.

And then we're going to do a bit of a deep dive into the area of the world I understand most, which is compute infrastructure.

Okay?

But, both today uh and for the rest of this quarter, these really are your headliners.

Yeah?

Make sense?

Recognize some of these names?

Woo!

All right, woo!

Yeah.

For for um the ones you don't recognize, I I would recommend looking them up cuz over the next few years you're going to hear about them a lot more.

Um One extra thing we are considering, because many of you asked, uh given the um just insane amount of demand we've had both from speakers as well you guys to add more topics and more coverage, we might add a virtual um office hours every Friday from noon to 2:00 p.m., especially for speakers from who are zooming in from around the world and can't make it in person.

That will be optional extra credit.

A quick show of hands, how many people would actually like that?

Oh, okay, I guess we're going to do it, Mike.

All right, cool.

More more details coming.

More work.

More work.

This is the swag for this class.

Uh I forgot who it was, but somebody sent me a tweet a brand new saw.

There was a tweet that went viral yesterday about this class that said um be uh what was it?

Be wary of taking classes that sound like AI Coachella.

Uh and there there's lots more serious AI classes on campus you can take.

Totally agree.

And by the way, I I thought that was pretty fun.

I think AI Coachella is pretty fun.

So, as you guys know, I did my undergrad here, uh did grad school.

And uh look, I I think um we're going to be talking a a lot about technical stuff, but we also get to talk in this class about life and leadership.

And so, um I thought before we jump in to technical stuff, you know, we talked a lot about scaling laws last time, and we're going to talk a lot about that in this quarter, but I thought I'll I'll give you a little less um sort of in preview into Andre's uh life scaling laws.

Um you know, I I think that you should take life seriously, but not so seriously that you forget what's important.

You know, don't forget how to have fun and remember what makes life worth living.

Cuz look, right now you might feel like you have uh all the time in the world.

And sometimes you don't know uh when you don't have that much more time left.

So, enjoy while you can.

Don't take for granted.

It's a really magical time you guys are in right now.

Um my view is it's very simple, actually, to uh live life and scale yourself, scale your impact, which I know many of you want to do.

Uh a lot of times a lot of you the students we've taught over the last few years have come to office hours and asked, "Andre, Mike, you've been so successful, blah blah blah.

How do you plan your future?" Um how you know, it's very similar to how do you plan a training run, right?

You want to you want to really knock it out of the park on capabilities.

You want to scale capabilities and revenue like we talked about last time.

And it's hard to forecast these things.

So, I I've actually found a pretty simple heuristic on how to navigate that journey, which is just have fun with people you enjoy hanging out with.

You know, that's pretty much it.

I found empirically, remember we talked about how scaling laws are empirical, not predictive.

I've found empirically that's worked out pretty well.

So, if there's one thing I'd love for you all to take away from this this quarter, you know, this is the last lecture I'm going to be giving this quarter, we'll have lots of speakers and so on.

Um but this is the I just want to leave you with this one, which is the most important people in this class aren't really Mike or me or the speakers.

It's you guys.

You know, look look around and see uh how special it is.

Really invest in these relationships cuz you won't uh realize how they come in and help you in all kinds of ways in in life.

You know, as you guys saw uh I met my wife here as a sophomore.

Say hi, Viv.

We've been together 13 years.

Um And just uh and I mentioned I have started two companies, both with former roommates from Stanford.

Uh one of them is my current one, Amp.

And you should just uh you know, the world is a uh messy place.

It's a can seem like it's there's a lot of crazy stuff happening in the world.

We're fighting wars.

There's a lot of violence like chaos.

Uh but you guys are in a very special moment in time.

You know, just think about all the things that had to come together for all of you to be sitting in this room.

So, just um generally see how special and lucky you are, you know, to be here.

And uh you know, we talked last time about how it can feel I think somebody asked I forget who it was who asked the question, Andre, you know, with all these AI labs and big companies spending so much on AI and infrastructure, how could we possibly create something interesting or novel or new in science and engineering?

Uh and remember I said like use them, do things that don't scale or be asymmetric about your bets.

And one of those is, you know, obsess over the things you love.

Because uh that doesn't there's some things that don't scale well, especially in large organizations.

And so, throughout this quarter, just remember that you actually do have some special weapons.

And one of those is uh the obsessions, the love, the trust you have for each other, the friendships, the relationships you'll build here and over the next few years cuz that'll come in very handy.

And it'll be things the those kinds of things are assets that don't scale uh as as you join larger and larger companies or organizations.

Okay.

Uh stop being uh an uncle now, and I will say maybe go to the real Coachella while you still can.

Uh one of my biggest regrets is uh when I was on campus we were working so hard and staying so focused on on projects and coursework.

I I've never been to Coachella, turns out.

And so, maybe we we'll go with you guys.

Okay.

Shall we shall we uh proceed?

Yes?

Okay. >> [applause] >> Thank you guys.

Quick recap.

Um Yeah, for those of you who are joining us for the first time, I'm Andre, I'm one of your co-instructors.

There's Mike, he's going to introduce himself during his lecture as well.

Um my full name is pronounced Andre and friends call me Andre.

Uh I was born in India, uh went to high school in Singapore, came over for college here at Stanford many years ago, um and then I ended up staying.

Uh this is now my home.

I live in San Francisco with my wife uh in Presidio Heights, and you guys are all welcome to come by anytime you'd like.

I've been in love with applied machine learning for the better part of of last 15 years.

I came here as an undergrad.

I took a bunch of coursework in economics and a major that I don't think exists anymore called mathematics and computational science.

And then for grad school, I did bioinformatics over at the med school, which is essentially machine learning applied to healthcare.

Um I've always been a very applied thinker.

I've always found that it's really exciting to look at what um machine learning systems when taken out into the real world at scale can tell you about the world, which is often actually a pattern you see not just in computer science, but in physics, right?

Physics is about trying to understand how the world works, looking at large patterns, and empirically trying to figure out are there laws we can derive about the world.

Um this this is the applied physics uh part of of of uh the discipline, of course.

And I still actually spend some of my time on campus uh at the physics department as a visiting scientist, where we've been doing a bunch of benchmarking on frontier models and how they're good or not at physics and science reasoning.

Feel free to ask me about that anytime.

We'll have office hours.

Um over that time I've had a chance over the last 10 15 years to invest, co-found, be part of the early days of over 10 AI labs.

Some of those you guys know, Anthropic, Mistral, Black Forest.

You'll be hearing from many of these in this class.

And um as as we just talked about, I I'm I have a deep deep uh I'm deeply thankful for what Stanford has done for me.

Sometimes I uh should post on Twitter.

Don't uh um believe everything you read on Twitter, but if you're ever ever wondering what my shower thoughts are, that's where you can find me.

My uh handle is Andre Mida.

Okay.

This if you guys remember, for those of you who were here last time, this is a cheat code to the rest of the class and I think the rest of the uh the next 2 years at least in the industry outside of Stanford, okay?

This is not just a CS153 thing.

Hopefully, this will give you a bit of a framework for how to navigate life after college.

Because if you remember, we talked about the goal of this class is preparedness for the real world.

The goal is not internships, goal is preparedness, okay?

Um, what is happening?

In the infrastructure world, in the CS systems world, we are going through a massive change.

Over the last 10-15 years with the rise of um, distributed systems, cloud infrastructure, a some a somewhat stable stack had emerged about how we create, ship, and scale software.

Right?

And these are the different layers of the stack that I would roughly say dominate the industry.

We start with capital, which is quite flexible.

You can put money in everything.

Then you have land power shell, right?

Energy production, data centers construction.

On top of that, you or in the data centers, you put chips.

You then have some software infrastructure called a cloud that makes those chips usable.

And then you start we we hook up all these chips together.

We train a model.

Sometimes we call them agents.

We then put them into an application.

We deploy them as solutions.

And then lastly, um, we try to figure out how to actually govern these things.

What's the safety, the security, the trust, the frameworks we need to actually make sure that these these technologies get deployed to the real world.

When Mike and I started this class 4 years ago, it was called security at scale.

At the time, I was running the platform org at Discord.

How many people have heard of Discord?

Perfect.

Great.

We did our jobs.

Uh, and Mike was running infrastructure at Apple at the time.

And both of us had started that security was becoming an increasingly critical topic in the world, but there just weren't that many places for people like you guys to learn what the frontier or the cutting edge problems of security were because you don't get to see those at on campus.

And so this is this start this class started as the missing systems class that I wish had existed when I was an undergrad.

And so, um, that's where this all started.

Since then, it's evolved.

We started with 50 students.

We're now 500.

Thank you all for for for joining us.

I think we have another 50 waitlisted and a few thousand people following a lot online.

I'm not sure when else we'll get to teach this class again.

So let's try to make the most of it, yeah?

Okay.

We're going through the great transition.

Because we have this new technology called AI, um, that has unlocked extraordinary value and is about to unlock way more value, everybody at every every leader or every major team or or I would say, um, people who care about the future at every layer of the stack are wondering, how do we unblock the bottlenecks?

How do we make this stuff go faster and safer and more secure?

And what we're learning in the industry as it is that it takes revisiting a lot of basic assumptions about how the stack works, where in the value chain you are, what your job is, what your technical function is, what your economic function is.

And I think you should start you will start to see you all are probably all already are feeling what I'm calling the great transition.

Um, to to uh, driven by this this urgent need across all levels of society, right?

You saw the the sort of diversity in names we have.

We have people like Jensen Huang um, and Lisa Su at the chip layer coming in to talk to you guys.

We have um, folks like uh, Satya Nadella who runs Microsoft, right?

Who who's at the cloud layer.

We have Sam Altman.

How many people have heard of Sam?

Sam Altman.

Yeah, there we go.

Okay.

Um, he's coming by, right?

To talk about models and and how they're deploying stuff.

So this is a really big shift that's happening, right?

For the first time at least in my life, I can't remember a time when there was such a big revisiting of assumptions up and down the stack where everyone's trying to figure something out.

And that's really cool.

Because that creates an extraordinary amount of opportunity for you guys.

Because in times of uncertainty, that's when things change.

And people who who understand where the world is going, who have a point of view, get to redesign the systems that have stayed quite static in the past.

Okay?

I don't know what the new world's going to look like.

I don't think anybody does.

But for the next 10 weeks, you are going to hear from some of the most um, I think uh, dynamic, talented, and capable leaders reasoning through how to really unblock the bottlenecks at each part of this ecosystem every week.

Cool?

Sound good?

Should we keep going?

Okay.

No, you don't need to clap for me every time.

Don't worry. >> [laughter] >> I got to I let me let me let me earn my my keep.

Okay, so quick recap.

Remember we we said, what is going on at the frontier?

Right?

The what is this this whole thing about called intelligence?

And a few years ago, uh, when I was starting to get calls from friends who I had gone to grad school with or who were running research at places like OpenAI, I started getting calls saying, "Andre, you know, we think there's an opportunity to really take some of this research out of the lab and turn it into products and services that could impact hundreds of millions of people." And at the time, it was a pretty craft bespoke process, right?

And we talked last time about pretty simple recipe on how to manufacture intelligence.

Compute, data, algorithms.

Pretty simple algorithm, transformer.

Do a little bit of pre-training, some fine-tuning, good to go.

Plug into an app, you got ChatGPT.

Right?

We're going to have Liam Fedus from chat the co-creator of ChatGPT uh, come by and talk to you guys later this quarter.

Things have looked very different now, right?

In four short years, we've taken what was a pretty like, I would say, uh, bespoke process and turned it into an industrial engineering process at scale.

Right?

Back then, 3-4 years ago, uh, it the the the sort of frequency of creating a new model was maybe once a year, twice a year.

And today, we have this industrial scale production process where we do, you know, base model training at least two times a year on 100,000 GB B300 equivalents.

Um, and then we do post-training with about 10% of that compute, right?

Uh, so mid-training, we add more capabilities into that.

And that happens about two to four times a year with about 10% of that compute.

And then we do this thing called continuous post-training, right?

With supervised fine-tuning and RL.

And I won't bore you with all the details that we talked about last time.

We'll have assigned readings.

Slides will be up.

But I'll let you guys go do the math uh, on how much compute and and and money is being spent on these systems.

Um, what's the most recent, of course, development in all of this is that the last mile of this, the reinforcement learning part, is now consuming almost as much compute as all of the rest of the step pipeline combined.

Okay?

And that's very exciting.

Cuz when it's new, but it also means that things are changing fast and resources and strategies are consolidating.

And so our hope over the next 10 weeks is that you get a bit of a window, a front a front row seat into that part of the ecosystem.

Okay?

Okay, so what what does all this mean actually for progress?

This is where we stopped last time and this is where I'm going to pick off pick up today.

Uh, quick disclosure list uh, and sort of like any good scientist, you you start by disclosing uh, the experiments you've run.

Right?

Uh, this is a list of teams that I've been I've had a chance AI lab teams that I've had a chance to work with.

Many of these were literally co-authors on a paper that then we teamed up on to turn into a company or a project out in the real world.

Some of them I was involved in as an angel investor, some as a co-founder.

And you'll hear from any of these people over the rest of this quarter.

Um, but this is also a disclosure list.

I'm biased.

Naturally, all my, you know, when you're when when you're observing an empirical experiment, you are naturally biased by the data that you're fed, right?

And so between Mike and myself, what we've tried to do is at least augment our individual biases and work experiences with a diverse sort of uh, uh, as uncorrelated of a set of perspectives for you all across the ecosystem as as we could for 10 short weeks.

Okay.

Um, so this is the crux of the class, right?

Of of this lecture.

What are the bottlenecks on these capabilities?

Uh, many of you are excited about these capabilities.

I certainly am.

You know, I I as we talked about last time, you can use them for everything from um, you know, having a conversation when you're uh, by yourself doing your homework.

That use case is banned for this one uh, for this class.

Though if you are do use any of the coding models for your assignments, just tell us about them.

That's all fine.

But it's a pretty diverse sort of it's a pretty general purpose technology, right?

AI found these foundation models.

Um, and so for the next, let's say 40 minutes or so, what I'm going to try to do is is break down in detail at sort of a systems level what is going on and what in in in in terms of the the the inputs required to keep these models and these [snorts] systems continuing their blistering pace of progress so we can all benefit, apply these this incredible technology, you know, beyond chatbots to new areas like curing uh, novel diseases, discovering new materials, you know, um, I'm of the opinion that there's like there's an extraordinary number of new frontiers to be explored and developed uh, with AI.

Um, but it it would it's not going to happen without us sort of as a society um, figuring out how to unblock progress in all the domains that we care about.

Okay.

Again, the recipe's pretty simple.

I'm going to break down the bottlenecks into four major areas: context, compute, capital, and culture.

And we'll see how much we can reason through this today.

I'm going to start with context and compute, and then we'll go from there.

Okay?

Might have to do an extra overflow office hours or something.

Okay.

Context.

Couple of pre-reqs you're going to need to understand the next few slides.

Reinforcement learning.

Very simple technique, super powerful, driving a ton of the progress at the frontier today.

We talked about it last time.

If you've had a pet or you've had a sibling who you've had to teach to stay away from your room, you are a successful uh, frontier model trainer of blind reinforcement learning.

The key idea is that when you have a system that you want to improve at a given set of tasks, you don't tell the the agent or the model how to do it.

You just tell it what you what to do, what task you want to reward, and when it completes that successfully, give it a reward.

If it doesn't do it successfully, you would hold the reward, and then you rinse and repeat.

Right?

Very simple idea, it's been around for a long time.

Started really working, I would say in earnest, um at scale about 2 years ago.

And that was because when you initialize a reinforcement learning environment with an agent like an LLM that's smart enough has smart enough priors about the real world, it turns out that these systems learn much faster than usual.

And and the capabilities tend to continue scaling the more compute we throw at them and the more um sort of environmental hardnesses and context we give them, which is pretty novel, pretty new.

Earlier, uh over the last 70 years of computer science as we discussed uh about the bitter lesson, you know, in in lecture one, um RL would would plateau pretty fast in different domains.

Chess, right, Go, etc.

Um it would it would sort of surpass human performance, but then the rate of progress would sort of plateau.

And the reason it seems, again, this is I would say an open area of debate, is that the the the the the priors, the the previous sort of inbuilt reasoning capabilities of of the the models were just not general enough to continue learning.

In a sense, you know, after a while, you you guys know uh you've heard the phrase, you can't teach an old dog new tricks, uh whereas it turns out you you can sometimes teach a Stanford student to come back and teach new classes, right?

That's my dad joke kicking in as well.

I'll I'll try to stay away from from the puns.

But so that this is the core philosophical tension of RL, right?

It's working much better than expected.

It seems to be because LLMs have enabled a new era where the the the models that language models are smart enough to then give us new capabilities when you use post-training to improve them on some specific task, benchmark, or um capability.

Making sense?

Everybody following me?

No, I'm not seeing Okay, we're going to might have to do an RL tutorial, but I would encourage you to uh How many people have taken a machine learning class at Stanford already?

Okay, keep your hands up.

How many of you have at least uh done one piece set with an RL problem?

Uh okay, there's Okay, that's the issue.

All right, we're going to have to about 30% or so.

We'll do an office hours on that.

And and you know, you're going to have some of the coinventors, some of the pioneers around RL actually come talk to you.

So, uh they'll probably do a better job than me.

But to recap, where does where does this fit in to what's going on in the industry?

As we talked about last time, you know, I got a call from some friends, Dario and Tom, who are running research at OpenAI.

Four years ago, they said, "Anj, we want to leave and start a new lab.

Um can we figure out how to build a business around this?" And so we spent some time fleshing out how do we turn the scaling of capabilities into a business, right?

And this was the simple recipe we came up with.

Raise some money, buy some compute, augment it with data, uh pretrain, put out a model that's good enough, considered state of the art that some people like programmers want to use them, deploy it, do inference, you know, run the model, and that gives you two loops.

The inference hopefully gives you enough money to buy your next round of compute and gives you context feedback.

You can observe, in the case of a pair programmer, when is the model actually accomplishing the task you wanted it to or not.

It has your model repo, you'll get uh history, your uh local files, right?

And then you pipe that back, that we call that context the context feedback loop, back through RL hundreds and thousands of as many times as you need, with as much compute as you need, to improve the capabilities of that of that system in that domain.

Pretty simple recipe, right?

As I discussed last time, we made 22 introductions.

Uh I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I to friends up and down Sand Hill Road.

They came back with 21 no's.

A lot of them just said, "Sounds sounds theoretically cool, Anj, as an idea, but do you have any empirical proof?

Do you have proof?" Well, as you guys know, 4 years later, we do have proof.

I won't bore you with all the slides we talked about last time with the um Anthropic revenue, etc.

And I think we do have one slide later when we talk about compute, so I'll come back to that.

Um But it But to fast forward now, I think if you believe, right, that that recipe works, as you know, Anthropic's gone from 9 to 20 billion in revenue, Gemini is doing well, OpenAI's, you know, started to produce extraordinary revenue.

There's lots of proof that this recipe works.

The question I keep getting over and over again is, "Okay, well, who wins?

Who wins in this that's going to If If everybody's going to be applying this scaling recipe around and it's so easy and repeatable, then where does the value accrue?" And at least one opinion I I've started to observe through all those empirical experiences I talked about with you guys earlier, is that context is critical here.

Context or the environment of the agent, right?

We talked If If you're training your dog, it's to to fetch in a park, that park is the context.

It's the environment.

All the people in the park, the kids that may be running around, the grass, the physics of rain coming down.

All of those factors of the environment influence the ability for you to improve and train the system, your pet, to perform better and better in the real world.

Okay?

And so I find myself explaining this pretty frequently to folks, and I hope it'll make sense to you, is that one, where will to to answer the question of where will frontier progress uh continue most rapidly?

And this is relevant for all of your projects cuz many of you must be going, "Okay, coding seems to be well on its way.

And uh image generation is is also well on its way cuz you will have um Andriy uh Andreas from Black Forest Labs who created Stable Diffusion come by.

But where else can I make a difference?" And one question I would ask is, "Well, where is there context, right, that can be reliably measured and verified when you're working with an agent?" And I think wherever in life we have verifiability, you know, code is very ver- verifiable, you can write unit tests, and your code passes or not.

Um material science, it turns out, is quite verifiable.

Again, you'll hear from from you'll you will hear from Liam and Dozh at Periodic Labs about how they're using RL from physical verification to discover new superconductors.

Very cool stuff.

There's a bunch of robots at a 30,000 square foot facility in Menlo Park nearby that maybe we do a field trip or something.

Um But where else is the context and the environment capable of verifying the accuracy of the task as performed by the agent?

That's the question I would be asking if I was you.

The second question that falls out from that is, "Well, who's going to capture that value?" Right?

Cuz you we don't want to just be researchers.

You guys actually want to do sustainable frontier system development, right?

Not just one-off model drops.

You want to scale these things.

Okay.

Well, it's the teams that will have unique and defensible access to some context.

You get there first, or maybe you have some insight.

That's where teams will, I think, capture the most value.

Right?

So that those are the teams I think are going to win.

And then who's going to lose?

Um my view is that the teams that get locked out of context that are essential to improve these models and the capabilities on some some domain will not have a chance.

Now, to bring that to life, I thought I'd just give you a few examples, right, of this context these context loop wars beginning.

Uh I think just about a year ago, uh there was a an uh a news site a news um drop that OpenAI tried to acquire an IDE uh that many of you probably use for your um for your coding work called WinSurf.

How many people have heard of WinSurf?

Oh, okay.

Cool.

I mean, we'll be happy to hear about that.

Um A few days later, right, after it was announced that WinSurf was being acquired by OpenAI, Anthropic shut off model access to WinSurf users.

Doesn't happen often.

You don't You don't In In In our industry, we don't usually shut off an API to users without warning.

But it made total sense, right?

Because if your competitor needs access to your model, the context, and can distill from observing how you help out uh customers that you want to attack, that's leakage, right?

You have context leakage there.

And so to those of us in the industry, this was very clear.

To me, it was very very normal.

I was not surprised.

But I think for a lot of people started updating their mental model.

Again, remember that stack diagram?

If you're a model provider and then you're an application company, you can always rely on your model company to keep giving you intelligence.

Well, that was one assumption that that stopped scaling then.

Okay?

Um and this is happening across the economy in different contexts.

Whether it's consumers, creators, companies, countries, at every part of the economy, there's a battle that's raging for these context feedback loops.

And over the next 10 weeks, you're going to hear from many of these people.

In fact, you're going to hear opposing views.

And uh that's our job here.

As instructors, our job is not to try to convince you of our views, it's to try and educate you uh with an independent uh view as much as possible, so you can you know, derive the conclusions you believe about where the future's going.

Cuz look, this is an open problem.

This is not a This is again, we're we're running the grand experiment of how to keep frontier progress going around the world.

It's making sense?

Yeah.

Okay, good.

People are nodding.

Can I hear a yes?

Okay, thank you.

So, let's deep dive for a second in one of these.

How many people have have uh heard about of Llama?

Great.

One of the the creators of Llama uh was a guy by the name of Guillaume Lample, who spoke in our class last year.

His lecture's up on YouTube, go check it out.

Guillaume and his um college friend Arthur, who are Arthur Mensch, who is going to be speaking here a few weeks, teamed up a few years ago.

Uh and Arthur was uh a researcher at DeepMind.

He was um one of the lead authors on a paper called Chinchilla.

Chinchilla scaling laws have been assigned as reading, so I'm a good professor never asks if students have done the reading.

I'm going to assume you guys have, good faith, honor code.

Definitely read that before uh Arthur shows up.

It'll tell you a lot about his view, but Mistral was a a new frontier lab started in Europe by the co-creators of Llama and Chinchilla.

And their view was very simple.

They said, "Hey, there's going to be an extraordinary amount of progress in closed source models because that context is is not that sensitive.

And people won't mind piping their software engineering context, if you're a developer in Silicon Valley, to a cloud server somewhere.

But if it's a mission critical context, what they call the sovereign context, it matters to a government, it's national records, defense, and so on.

Well, you kind of need to start locking that down locally.

And that means you need models and weights that run locally on your infrastructure that you can control.

And so they started Mistral as a way for um companies, organizations that needed control over their own context to deploy models, open source models locally.

So that and and and and the reason I think this is worth talking about is because it's quite um hard in the world of infrastructure, especially software infrastructure, to beat n- the the relentless sort of uh flywheel of the decreasing marginal cost of production in storage, in networking, in servers.

The history of cloud over the last 15 years has basically been decreasing marginal costs, right?

When Amazon and Google, who both had sort of extraordinary businesses serving consumers, right?

Google in search, Amazon in shopping, they were just piling up lots and lots of servers for their own needs, and they started realizing, "Hey, you know what?

It doesn't cost that much for us to add and another server, another server, and basically just rent that out to other people." Because at some point the scale of your own first party needs is so high that you can pass on the benefits of that scale to third parties.

And that's how we got AWS, GCP, Azure.

Mike helped start Azure.

Sorry to date you, Mike.

Um but that's that you know, basically 15 years of of sort of relentless uh consolidation in the cloud infrastructure world because of the economies of scale.

Right?

For the first time in 15 years, that's changing.

You know, why do you have President Macron, the head of a country, and uh Jensen, the uh world's richest man, or was, I think, last quarter.

Probably still is.

Um sh- showing up on stage in Paris uh next to a 33-year-old scientist who's never run a business before saying, "This is the future of Europe." It's because of context.

There are governments and mission critical, you know, workloads that are just too sensitive to be run on cloud infrastructure overseas.

There's a we talked last year um in the class about the Cloud Act.

How many people have heard of the Cloud Act?

Okay.

Zero.

Hmm.

We got to assign that as reading.

The Cloud Act is a um is policy that says that if you're running workloads on United States uh servers, um whether it's or it's a company run by um or it's servers run by United States company globally, the government has the ability to access that data.

To some people around the world, that's not okay.

And so now suddenly AI workloads have gone from being cool, you know, chatbot assistants to being mission critical systems.

Remember we talked about RL?

RL has started to work with a level of precision and accuracy in mission critical context, and that's why you have a huge um sort of reshuffling of cloud infrastructure globally.

And you'll start to hear this word sovereign AI and infrastructure independence a lot more over the next few years.

Okay.

Uh just to wrap that point, that's what's allowing startups to sort of unbundle monopolies in the infrastructure world, or let me call them oligopolies cuz some of our guests won't be happy when I say monopolies.

Um at scale, at speed and scale.

And it's very exciting cuz you guys get to participate in this revolution, too.

And so, you know, one one clue you could have about where to spend your time is where there's a unique context that hasn't been available to you because you're not at scale, but that you can do something unique and get ahead of and start um sort of being a participant in that re- uh restructuring of of that industry.

Okay.

Make sense?

Yes?

Come on, guys.

It's spring.

Yes.

Okay, thank you.

Okay, so how do you actually get this going?

After doing this for 10 years, and mostly five of intense uh investing, company co-founding, nowadays people call me the founding investor.

Basically means I'm neither the uh the the the CEO, which is all the many of the talented folks I get to work with who are usually scientists, but I'm not sort of traditional venture capitalist.

I don't really write a check.

I typically co-found these companies on day one with these teams, and I do this one at a time.

My current um uh project is Periodic Labs, as we've talked about.

But I've observed a pattern over and over again, which is you you you you you sort of formulate a state-of-the-art mission.

What is a frontier that we really want to advance?

Material science, coding, whatever it might be.

And that you make that your mission.

We want to move the frontier.

We want to create state-of-the-art intelligence in a particular domain.

Okay?

You then get enough compute, that's research compute.

You do some experiments.

You figure out how can we actually get something novel out to the world that doesn't exist.

And often in a new domain, it's that's it's actually not that hard to do because we're early.

Ship it.

Get it out into a context that you have access to.

Run the feedback loop.

And then remember we talked about that scaling the those two flywheels?

Then just keep them going.

Keep them going as long as you can cuz that is the gift that keeps giving cuz they reinforce each other.

Okay.

Eventually, at some point, when these flywheels get good enough, they start propelling themselves.

That's what many people in the industry call recursive self-improvement.

Sometimes people like to call this the path to AGI or ASI.

Um well, I'm an infrastructure guy, so I think more at the level of the system.

I don't necessarily think in terms of a model, but you can often have a company that's, you know, hitting takeoff because they've just figured out as a good execution team on how to keep recursively improving themselves.

It doesn't have to be an actual model that's super intelligent or whatever.

I mean, that's that's one view, that's fine.

You guys should ask our speakers if that's how they they they view it, but I sort of think about recursive self-improvement at the systems level that's that's attacking the state-of-the-art mission, not really at an individual model or API level.

Okay.

Um so the big question, where does this leave us, right?

On the context question, is what are the limits to RL?

Um and this is a very exciting open question.

I don't I hope this will be answered um over my lifetime.

It may not be.

I don't know how much time we have to really figure this out, but there's two views on it today that I hear in the industry.

One is a philosophical, the other's the the empirical view.

The philosophical view is that hey, given the right context, given sufficient compute, these agents should be able to learn anything.

So, once you get that like recursive sort of takeoff happening, why don't you just ask the agent to constr- if it you have a coding agent, right?

And the coding agent's not very good at material science, but at some point, if it's good enough, you just tell the coding agent, "Please build yourself a material science environment, and then go do the RL loop yourself." And so on and so forth.

That's one view.

Um it's not clear right now to me that RL is generalizing outside of task distributions, which means outside of the domain that you started that frontier flywheel in, right?

The context feedback.

It's not clear to me that models are generalizing from, let's say, coding to material science, to biology, etc.

I think within the narrow distribution of coding and so on, what we're seeing is basically relentless progress.

It doesn't look like it's stopping anytime soon.

And look, this is a big area of debate, billions of dollars being invested in trying to figure the answer to this question.

My view is closer to the second one, which is that empirically, what I've observed is that life is messy.

Um progress is fastest in easily verifiable domains.

And so, in domains like coding, which is verifiable, you will start to see sort of the idea of a narrow superintelligence or, you know, exponential progress, but in areas uh in the world where progress is not as easily verifiable, a great example of that is aesthetics, beauty, love.

Like how how What are these How how do you verify, right?

Like what is good a good a a a good uh verifiable construct for beauty or love or aesthetics?

And this is why How many of you have tried writing a uh like a message to your friend like a an extended blog post or something with with Claude or ChatGPT?

Only four or five people.

Okay, clearly you guys have real work to do, unlike me, writing blogs all the time.

Um it's terrible.

These models are not good at long form writing, at creative writing.

They hallucinate, they they make these clichéd hyphens and so on, right?

They They see the M dashes and the It's not It's This is This is a game changer.

Ever ever heard of that phrase or the It's not just X.

It's Y.

I I sent a a blog post I was writing like a bit of a manifest about infrastructure to a friend 3 weeks ago who was a founder you'll hear from in this class.

Said, "Can I get your sanity check on it?" He writes back in 30 seconds. "Did you use Claude for this?" I was like, "No." He's like, "I don't believe you." Well, it turns out I'd written the outline myself and then I'd asked Claude to like flesh it out, you know?

We've all done it, right?

And he could tell immediately.

And since then we have an internal rule at Amp we don't send each other AI-generated uh documents.

We think, we sit, we write, and we share share with each other even if it's uh raw.

So, many of the speakers you're going to hear from at in you know, working in the model level are innovating here trying to answer this question.

And I'd encourage you to do some research on them.

The a lot of people share openly about their strategies online.

So, so do your homework, come prepared, push them on these questions, yeah?

The more you prep you do, the more work uh the the more value you're going to get out of these lectures.

And more importantly, I think you guys can innovate here, too.

Cuz it's early.

And there's so many domains that maybe you only you understand and only you can verify because of your obsession, your love, your taste, your sense of beauty, your your culture.

And I think we're that I think that's the most uh valuable thing you could be doing.

When I When I get a call from a new team that wants to me to invest or help them build a business, that's what I'm often looking for is what is the unique um sort of frontier that they can verify for humanity.

I had one of my uh favorite uh he's he's he he might not like me sharing this, but I'll share it anyway and we we'll publish after getting his um permission.

How many people here have heard of the YouTube channel 3Blue1Brown?

Whoa.

Okay, I did not realize.

I'm going to have to call Grant.

Uh Grant Sanderson, who is the uh the creator of 3Blue1Brown 3Blue1Brown Oh. and I were uh undergrad draw mates.

He lived in Froshco, I lived in Uge.

Uh there were four of us who were good friends and then we drew into Crothers together.

Yeah.

Crothers.

Uh but uh Grant and I have stayed in touch over the years and he came by, he crashed over at my house for the last few days, and um he unfortunately had to fly out this morning at 6:00 a.m., but we you know we're talking late into the night last night about what would it take to create um sort of a truly world-class educational um you know, learning space of the kind 3Blue1Brown does for science and math, but for anything, you know?

And it was so clear to me while talking to him that that what's unique about is is his brilliance of how and his taste for what is is the right way to deconstruct a really technical topic and really understand it from from the first principles.

And that's I would say the true magic of of frontier research.

Is is is distilling the insight of somebody who's really world-class at what they do and being able to share that with the world.

And RL is just one technique to get there.

I think we'll invent many other techniques.

Okay.

Making sense?

Yes.

Oh my god, guys. >> Yes.

Thank you.

Okay.

Now, compute.

This This is the exciting stuff for me.

I'm a compute nerd, I'm an infrastructure nerd.

As you know, guys, as I talked about earlier, I studied both economics and computer science and up statistics and bioinformatics, and I love the intersection of multiple domains.

And compute and infrastructure is really where a lot of that comes together.

How long do we have?

Quick time check. 30. 30 minutes.

Okay.

Where's Anthony?

Uh sorry, Anthony's last year.

Dice, can you keep me honest and give me a heads-up when we have 10 minutes left?

Okay, thank you.

So, what is the big idea with scaling?

It's that scaling works predictably, right?

Capabilities scale predictably with compute.

This is a uh set of public estimates that overlay Anthropic's revenue over the last 4 years correlated with the amount of compute that they brought up at the company.

What do you notice?

Anything Anyone notice something about the shape of the curve?

Exponential.

Every time I you know, I wouldn't even go I wouldn't go that far.

I wouldn't say it's exponential, actually.

It It is It is correlated strongly with the compute.

Right?

Um it's predictable.

Every time the company brought up new compute, roughly 60 to 90 days later there was a capabilities jump and then a revenue jump.

That is quite special.

Dollar in, dollar out.

Dollar of compute in dollar of hard assets, land, power, shell which in the financial markets usually trade at three to four times revenue being turned into a dollar of software revenue, which usually trades at 30 to 40 times revenue.

From a systems perspective, what's going on?

We have developed a predictable way to transform one input into another predictably that humanity considers a lot more valuable than the input.

The output here is roughly 10 times more valuable to the world, to the markets, than the input.

Remember, this class is called frontier systems.

We stopped calling it security at scale and infrastructure at scale for a reason, cuz we are now in the full-stack rewrite, and I need you guys to start thinking up and down the stack, not just as engineers, not just as or computer scientists or electrical engineers.

I need you to start thinking like full-stack thinkers.

Think about the the capital markets.

Think about the business, cuz if you want to keep sustainably doing research at the frontier, you've got to run the whole loop.

Run it back.

Okay?

So, what's an example of that in production?

If you look under the hood, Claude code, these these are commits that uh the agent has been Next year they've announced in their earnings reports they're going to spend 1.2 trillion dollars on capex.

These numbers are kind of hard to fathom.

So, what happens?

What happens when all the big boys start spending?

What do you do?

Step one, acknowledge reality.

For the last 4 years, I have I have lost count of the number of times people have called me and said, "Andre, why are you spending all this time on compute?

It's a commodity.

Just give the company some money, they're going to go be able to rent from GCP, AWS, and so on.

It'll be That's how the world works, right?" Not quite.

This is a chart that we've been aggregating at Amp of rent GPU rental prices quarter by quarter across a number of estimates.

We have an internal system we call the Amp grid, whose job it is to try and understand what's going on in infrastructure and try to forecast intelligently so that our teams and our companies that we work with can get a bit of a empirical view on where infrastructure is going.

What do you observe about the price trend of H100 prices, a chip that's over 2 years old?

Over the last 90 days.

Somebody, come on.

This Yes, thank you.

Going up.

It's pretty simple.

Anybody who told you chips are commodity should probably get a phone call from you and ask them what they think about this.

Because chip prices are not going down.

They're going up. 2 years ago when I was calling friends at clouds up and trying to rent them for our teams you know, I was the the the average H100 price per hour was a dollar 73.

This morning I got a friend message and say Can we give her a quick round of applause? >> [applause] >> The reason I'm doing that is cuz you're going to be thanking him later. is your chief compute intern for this class.

For your final projects, when you need compute credits, he's going to be provisioning them for you.

And so if you have any bugs and so on, please don't come to me, go to who are also married and I think and met at Stanford here, been married longer than Viv and me.

We're our undergrad friends and uh was my master of rituals in AKPsi which I pledged mostly to be able to date Viv.

Okay.

Um And he's my co-founder at Amp.

So you can bother him anytime you want.

Okay.

This morning we had a founder who's raised I think like what, $700 million, billion dollars?

I wish I could show you the screenshot.

Said, "Anj, we're in a compute crunch." Yes.

Need H100s ASAP.

How many do you need and when?

Take them right now.

Price not a problem.

It's a good time to be a drug dealer.

Right?

This is a fundamental assumption the entire industry has been built on that chips are commodity.

All chips depreciate.

Entire publicly traded companies are running on this assumption.

I mean meanwhile here, ground zero in Silicon Valley, I can tell you it's a very very different picture that's emerging.

Okay.

So where what does that mean?

I like to look at history to get clues about where the world is going to go and I'm starting to realize that we've seen this before.

We've lived through cycle after cycle of the invention of new infrastructure, general purpose technologies and then you invent ways to turn that technology into useful products, steam engine right?

Make cars, make shoes, whatever it might be and that results in what is often called the golden age or the gilded age where few people who start hoarding those resources get to profit at scales we've never seen before.

And I think that's roughly where we are relative to the Industrial Revolution.

So what happens next?

Right?

Like I said, let's look at the history of infrastructure for some clues.

This is the econ nerd in me coming out, but I promise we'll bring it back to computer science.

I just thought I'd pull some I asked our friend Claude to pull some charts together.

So if there's some wrong numbers here I'm not to blame.

Though I guess I'm not following my own rules here.

But with steel, 1867 to 1895, right?

There was, if you notice, this increase in prices.

Then there was this panic of 1873 where there was a lot of hoarding of the steel and prices were going up.

Then suddenly there was a panic, "Oh, this steel actually isn't worth very much.

We we hoarded too much steel." Suddenly the prices collapse.

Super annoying for everybody involved.

Companies go down, people are backstabbing each other markets up and down, wars are being fought, blah blah blah.

Eventually, as a society, we get together and say, "Okay, this isn't good.

We don't want panics.

We want stable production of steel, stable consumption of steel.

Let's figure this out." And that's what you what results in this sort of plateauing of steel.

Same with fiber optics.

I'm sure everybody here is tired of hearing the word AI bubble.

Um everybody's asking about the fiber optic overbuild and all these companies like Cisco, Lucent, Nortel, WorldCom.

Is this you know, these chip companies the same?

Why?

Because all the economists, all the people writing op-eds in the Wall Street Journal are just looking at all the same data.

Yeah, okay, prices go up and they come down.

It's a bubble, boom, bust, blah blah blah, right?

Same thing with DRAM.

Very violent semiconductor cycles.

Memory was invented, DRAM was invented, people go, "Okay, this is really important for personal computing." People start hoarding it.

Then there's uh some something happens.

Usually it's a panic, it's some Usually honestly it's not something not that big.

It's it's like some some stupid news or some world event.

There's always world events happening, but triggers a panic and that results in a self-fulfilling sort of sell-off of infrastructure stocks, assets, supplies.

And then you get back up and people realize, "No, actually this there's inherent valuable technology with this.

There's new capabilities here.

We can do something with it." And then you either get another rise or you have a stabilization of that resource.

This is the Baltic Dry Index with shipping.

Same thing.

These slides will be up.

I'm not going to bore you with it.

Uranium.

When we were living through the nuclear energy boom of the 1970s and same thing.

Right?

And often what happens, and with uranium this is very clear you have an uh the intervention of the government to allow the stabilization of that resource.

And so if you look over and over again And okay, and this is our our friend the H100 GPU that we talked about.

Prices were dropping after the chip came out in June all the way till August of 2024 and since then they've steadily been rising.

This is actually a bit out of date, but as you know they're back up, right?

So what does history tell us?

One infrastructure does is cyclical.

So at least we've got some clues, hopefully, unless this time is so different which it may be and which is what I should I would encourage you to to quiz our speakers about cuz many of them are at the frontier of these markets.

Hopefully we as a society can figure out how may ideally we just skip the whole boom and bust thing.

It's not fun for anybody.

But assuming that's we're we're at the start of another sort of like panic run on compute, the question of course, right, is how do you stably get to the other side as fast as possible so we can all start building useful frontier labs and projects without having to go wait at the around the corner and and bother Larry and Sergey for compute.

Now the usual timeline if you just look across the digital era, you know, the internet and bandwidth build-outs between these cycles is about 3 years. 2.8 years.

For physical infrastructure, it was 6.3 years.

And my best guess is that what and this is the thing about AI that's so novel, it's a combination.

AI scaling is a combination of massive you have to marshal massive physical resources, right?

Like land, power, shell um chips to produce this very digital thing called software revenue.

Intelligence is is is is bits.

But but the production is atoms.

Those worlds don't like colliding.

And that's what's new here and scrambling and confusing a lot of people is how do we actually coordinate these two things in a way that's sta- a stable, reliable and so on.

The central question of course, right, is how do we get compute or is compute rather just a commodity?

Right?

That those are the that's the tension we've been talking about over the last 15 minutes.

Is compute a scarcity?

Is it something where all of you should be spending your time wondering should you be making chips?

Should you be making more better interconnect?

Or should you be spending time on distilling your aesthetics your creativity, your intelligence like 3Blue1Brown into how to teach the world new kinds of science and math and physics?

That's the core tension, right?

Good news is this class covers both.

So for those of you who are electrical engineers and want to go into chips, you're getting that uh exposure and for those of you who want to be frontier model researchers, you're going to get that exposure.

You can decide.

Okay?

We're not here to decide for you.

But here's my view on it as one participant.

Macro, I today unlike electricity or coal compute is not fungible.

Electricity is fungible, right?

Megawatts are megawatts are megawatts everywhere.

Pipe into a grid, you get them out.

It wasn't always the case and I'm going to talk about it in a sec, but today compute is not a commodity.

The prices are rising and they are not fungible.

This chart shows that there's varying prices for different chips let for chips from different companies like AMD and Nvidia.

Chips from the same manufacturer are not fungible.

Right?

The H100 is different from the GB200 which is different from the B300.

These numbers may not mean anything to you.

It's what I spend all day talking about with my research teams.

So number one, the problem or the indicator that compute is not a commodity is that compute is not fungible today.

And two forecasting compute at the micro level is very very hard.

Unlike electricity where we've developed pretty stable mechanisms for how to forecast our consumption barring hurricanes and so on there we're generally like we have power here, right?

I grew up in rural India in a boarding school called Rishi Valley and we used to have power outages roughly once in the summer like every other week.

Today, luckily, I think they've put a transmission like a they built a generator backup generator there.

But in the in in most parts of the world, we've had stable forecasting of energy and therefore the stable production of that energy and supply for what?

At least 75 years.

That's not the case with compute.

Because inside of these research labs, one team finds it very hard to reason about their needs.

Training is a is a is a spiky thing.

You think about, "Okay, how do I create a new capability like a frontier model for coding?" You take an algorithm, you play with it on sort of small scale.

If it starts working then you spike up for your hero training runs.

Inference, when you deploy your chatbot, turns out a lot of people you if especially if your chatbot's deployed in the US, a lot of people use it during the day, no one's using it at night.

Inference is like cyclical, too.

And so we're in that part of the of humanity where um not only is the most valuable input to production of intelligence not fungible, it's also super hard to forecast.

And as a result um we have those hoarding cycles going on.

Remember I showed you those uh sort of the the big boys buying up as much land power shell as they can over the next 4 years going "Look, there's a pretty reliable trade we can make, right, for hardware to software revenue.

Not sure which research, which model, which breakthrough will actually do that, but we might as well just buy it all up." So the question I spent a lot of time recently thinking about, and I think you guys should, for those of you who are interested in infrastructure, is what what did it take in history to turn this scarce monopolized production resource into uh a productive sort of accessible commodity for everyone who's working or innovating in the field?

Okay?

And my view is again, history tells us that there's two key things you need to solve the fungibility and the the the access problem.

One, you need standards.

ACDC Right, TCP/IP.

These standards that we convene on over and over again to say, "You know what, this is infrastructure, it should be stable.

Let's all agree on a standard a format for this infrastructure to be produced and so we can all consume it, no matter where it is." And the second is you need institutions to enforce those standards because inevitably humans are misaligned at some scale.

And somebody needs to coordinate and align human beings to adopt those standards at scale.

And that's roughly where we are right now.

So what makes a commodity fungible?

It's pretty simple.

Commodity needs a This is all How many people have taken Econ 1A?

Oh, wow.

Okay.

We're going to do some Econ assignments, too, for those of you who want to work at the frontier.

This is a pretty standard textbook definition of a of of fungibility.

What makes a commodity fungible?

A commodity needs a common unit, it needs a standard delivery interface, needs interconnection and pooling, needs metering, control, and settlement, and the buyers can substitute one supplier's unit for another.

Okay?

You should uh really understand this definition if you intend to train any kind of frontier models.

Cuz this is not the case today.

So this is my point.

Technical standards and fungibility don't come easy.

They need institutions to enforce them to reallocate away power from those who benefit from hoarding and instead prioritize the public benefit.

That's what we need more and more of in these infrastructure cycles is somebody or some group of people need to start stepping in and saying, "You know what, good for you, great, you have enough compute.

Those folks over there don't.

Let's pool and let's figure out an optimal allocation of this resource across society, across a country, across the world." That's what we um call the public benefit.

Yep. 10 minutes.

Okay, perfect.

I will try to zip through this.

We're al- almost at the end.

So the punchline is pretty simple.

We are in the pre-standardization of compute era.

Right?

If you just look at all the previous cycles, railroads from 1886, electrification 19- 1907, telephony, aviation, internet, semiconductors.

New new general purpose technology, huge explosion in in infrastructure needs, usually consolidation amongst three or four players.

Hope sometimes industry step in and self-regulate and they come up with standards if they can get along.

Other times they a government an institution has to come and say, "These are the standards." And we're at that moment roughly in history for for compute.

So food for thought for this quarter, this is your assignment and there'll be some readings, but I'd like you to keep this at the back of your minds.

One, what will it take to ensure a peaceful transition on compute over the next couple of years?

And two, what is your part in this?

You can be a part of this change because remember I said at the start of this lecture, you are extraordinarily lucky to be alive at this moment in time.

It may not be clear to you, and it's always uh you know, it's easier to connect the dots in hindsight, but think of yourselves not just as students, but as act- active participants.

And part of the goal and design of the um the project this quarter is to try to make you more and more active participants in this stack.

You can blog, you can tweet, you can write, you can share your thoughts with the world on what are the standards you wish you know, you emerge so that your job could be easier.

And hopefully >> [clears throat] >> um some of the people in this room who are going to come talk to you, who are running many of these institutions who can can help evangelize these stand- standards, adopt them, coordinate them, will hear from you.

Cool?

All right, that's all I've got.

Um I have a bonus.

This is from last year.

This is a screenshot of RTX 5090 prices in USD over the last 18 months.

Who knows what the RTX 5090 is?

Okay, cool.

Some gamers in the audience.

This is Nvidia's gaming chip.

It was also the grand prize for the best project last year.

When Jensen came by, he signed five 5090s.

I think uh this is whose team made a really cool gaming uh product and and and pretty valuable chip, right?

So I'm not going to ask Jensen this time for for more 5090s cuz they're a little bit more valuable this time around.

But we'll see, maybe there'll be surprises.

Okay, thank you guys.
