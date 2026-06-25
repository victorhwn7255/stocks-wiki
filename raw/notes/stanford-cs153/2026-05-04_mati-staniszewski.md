# Stanford CS153 Frontier Systems — Mati Staniszewski: "The Future of Voice Systems"

**Speaker:** Mati Staniszewski (Founder & CEO, ElevenLabs — frontier audio/voice AI; ex-Google/Palantir) · interviewed by Anjney Midha (CS153 co-instructor, a16z — ElevenLabs angel)
**Channel:** Stanford Online · **Upload:** 2026-05-04 · **Duration:** 1:06:26 · **Views:** ~4,542
**Source tier:** Tier 5 (founder book-talking ElevenLabs + voice AI; private a16z-network co). Mostly the company story + the cascaded-vs-fused architecture debate; investable kernel = the voice-agent demand profile (low-latency inference) + a couple China/commoditization touches. Discovery-only; spoken numbers soft → verify at primary.

## Transcript (Tier 3/5 — not a primary source)

Welcome to week two of CS 153, also known as AI Coachella.

We are super lucky to be kicking off this week with Mati.

Mati is the founder and CEO of 11 Labs.

How many people here have heard of 11 Labs?

All right, so pretty much everybody.

Mati and I go back a ways about 3 years ago, I think, when I was still running platform at Discord.

Um a friend said, "You know, Anj, there's a a little bot, like a a text-to-speech bot on Discord that's blowing up.

Um you should check it out." Um and you know, we had a lot going on at the time at Discord, and so I I actually didn't, and I should have.

And then a month later, somebody pinged me again and said, "You really should check out this bot." And I I checked it out.

It was called 11 Labs, and it was quite an extraordinary bot.

It It It was a um a Discord bot that allowed you to generate audio clips with just a text prompt.

Uh and within 24 hours, I'd asked one of our mutual friends, Nat Friedman, to introduce us.

Mati was gracious enough to explain what they were working on.

I had You let me come on as an angel investor, so thank you.

Um and since then, Mati has gone on to build one of the most um the fastest-growing, uh one of the most widely-used, and I would say trusted brands and services in frontier audio and speech.

Um so, thank you for joining us, Mati. >> Thank you.

Thank you so much.

Good mor- good morning, everyone.

It was also a crazy thing, Anj Anj, uh when we met for the first time.

It was me and my co-founder, Piotr.

Uh we both came from Google and Palantir before that.

So, we were trying to like redo the company setup from scratch of like what not to do, and we tried to like go against some of the lessons from those days.

Um so, we were allergic to meetings, we um to like any email-based communication internally, but we also want wanted to not do any of the internal communication the standard way.

So, when we started, we actually run a company on Discord. >> I did not know that. >> So, in that conversation, you were you were helping us A on on on on the text-to-speech, and we were trying to like figure out is that the right play for us to base all the company on Discord.

We swapped from to Slack. >> I know Slack was easier I know Slack was >> uh easier for Freddi, but that was that was an interesting few few few first months of trying to build all the bots on Discord to like make it easy and quick for us. >> Th- Th- This was a bit of a thing we talked about last year, too, which is that often gaming ends up being this petri dish for innovation.

Some of the hardest infra, product, design, experience problems that are solved in gaming then become sort of uh leading indicators for the rest of the world.

And the stuff you were doing and a bunch of other our friends were doing on Discord at the time have ended up becoming indicative of you know, value in AI a few years later.

Is that do you feel like that's an a true assessment, or uh am I overfitting? >> Yeah, I think that the the true part there, which, you know, we we were following the journey model at the time of like how they built that community piece on Discord.

And for us at Eleven Labs, when we started, we knew that we wanted to fix two things.

We want to fix the research and foundational models around audio and voice, and then build product around that to to bring that AI into more of an applied AI setting and fix the problems that our customers are facing.

We started on a very PLG-driven motion, so working on the product-led growth with a lot of the the the the creators in the space, of developers in the space.

And we thought that the best way to do it is close the the the loop as close as possible to the people that are using those tools.

And like Discord at the time, and and and and generally keeping access open to a lot of those creators and developers was the best way for us to learn.

Is it good enough?

Is that quality finally there to to serve the needs they have?

Two, what are the use cases we might not predict that people might want to build so we can bring that quicker.

And then three, um and that's still a big issue today of our work across that is um we want to work with the community to find a ways for them to contribute back to the product development.

And of course, whether that's using the models to refine based on the data of of how you use the model all the way through that can you contribute.

In our case, we created a voice marketplace where key people can con- con- contribute their voice to to be used by others.

So, that community aspect was very important and it's always uh a true where I feel the technology adopted by the community will show you use cases that might like diffuse to the rest of the world 6, 12, 18 months later.

So, being like close is is super valuable, but more so more so than not in that early days just uh I think you need to be like extremely problem obsessed.

What is the problem that they are having?

And and the variation of what you think the problem is to what the customer actually thinks is a problem is slightly is slightly different. >> Okay, let's actually stop take a beat there.

Can you go back take us back in time?

What was the problem you guys were obsessed with when you started 11?

What is it today?

How might it evolve?

Give people a bit of a 11 Labs 101.

How do How do you get here? >> The whole chronology.

I will I will I'll give you a zoom in into that first day and then and then and accelerate over last few years.

But when we started, so I'm from Poland, my co-founder is from Poland.

A very peculiar thing that happens in Poland is that if you watch a foreign movie in Polish, all the voices, whether that's a male voice or a female voice, get narrated with one single character.

So, if one voice reading every character.

As you can imagine, a pretty pretty terrible experience.

And you'd think that with the modern technology, this is a problem that would have been fixed.

And no, it's still the case.

So, most of the content is delivered this way.

So, that was >> Whose voice was this?

Who did the >> They have five characters.

There's like five of those voices.

Usually monotone male deep old voices.

Uh and uh the it's also crazy because the part of the thing is they are kind of encouraged to deliver the the movie in a flat delivery so the audience can interpret the emotions for themselves.

Uh which is like another another another level. >> a lot from the audience. >> They do expect a lot.

Um so, if you like any Polish person, if you ask them, they will like account how like not good experience that is.

And when you learn English, you finally get to learn everything in original and that's a an extremely positive one.

So, that was like the first piece and inspiration for us.

We know the future is different.

The future will be where you can access all types of content in any language uh with that incredible tonality, incredible emotions.

So, so uh so we left Google, we left Palantir at the time and >> Were you guys both both in the Bay Area >> at the time?

We are both uh between Warsaw and London.

So, at the time when we started, we started in in in London, then moved to Warsaw for a little bit, then moved back to London. >> Yep. >> So, from Europe uh at the time, which actually was uh for that part was pretty useful because the whole language thing is is a big problem there, less of a problem in US.

So, the kind of the inspiration might might have not occurred uh otherwise. >> Mhm. >> And then we knew that we want to fix that AI dubbing problem.

And as we started going deeper, we knew that we need to understand in two parts.

We need to understand whether there is a uh a research potential for us fixing it and two, whether there's an actual product need, actual problem for the customer.

So, so Piotr, my co-founder, an amazing researcher, started diving in and quickly realized that the current models could potentially create a Frankenstein version of the dubbing.

They're not good enough, but they're almost giving you an experience where you can switch from language A to to B, preserve the voice, preserve the intonation emotions, but still not good enough.

So, there will be research, but possible research to fix.

Now, in that research, a very important part is, as you think about the dubbing problem, from speech, there are three models that need to play a role.

You need to transcribe what's happening, who is the speaker, remove the background sounds, background noise, then you bring it to text, you translate it to the another language, uh you might need to do additional set of corrections, and then you recast it back on the other side of text to speech to produce audio on the other side borrowing from the original performance.

So, there are those three key models: transcription, translation, and and and the text-to-speech on the other side.

And you need to fix all the components to make it good.

While the same time, I was trying to figure out, does anybody need that?

So, we would call the email of creators, of studios, saying like, "Hey, if dubbing was a problem, if Sorry, if dubbing was possible automatically, and you could take your movie and bring it to all international language with your own voice, would you be interested?" Every so often, we would give them uh give them like a early version of the samples.

And um and frequently, the reply we got was, "Yes, interested, but if you can do that, could you also do just a simpler voice-over corrections for me?

Because when I record, let's say even as we record now, after that, some of the parts are not recorded properly, and I want to fix them.

Or could you replace my voice from the from the script just in my original language, so I can narrate that without appearing in the script and screen?" Um and that was like a very clear piece where he dived into the space on research, and we dived into the user problem space.

It was clear that there's other problems that we can fix first.

And we can focus research on one of the components instead of all of those components, and and and actually bring that to the market, and bring that to to >> So, a couple of things.

I mean, the class is called Frontier Systems, right?

Um if you notice what Mady just talked about is the anatomy of what is their intelligence pipeline.

Remember last last week we talked about the anatomy of of how um intelligence is manufactured, but he just gave you a breakdown into the system of of that 11 was trying to build at the time, which was this cascaded workflow.

Right, you had the TTS, you had an LLM in the middle to do some reasoning, essentially.

Right?

And then you have a had a speech-to-text model. >> Exactly. >> the other way around.

You had transcription, you had an LLM, and then >> Exactly. >> model. >> Exactly.

And like it was still 2022, so it was still a year where the topics of the day were crypto and metaverse, so that was still before the GPT moment.

They could the different days, and LLM translation was still relatively poor, so we were like using both attempts.

So, like the whole pipeline didn't produce the right result, which was a great piece for us being close to the users trying to get like what is the actual problem, because we then shifted, "Okay, let's fix the text-to-speech, which is the most common denominator of of all those problems, and let's fix the voice-over for the creators, and then we've noticed that there's other parts of like just reading the scripts, reading articles, reading books that we can deliver." So, in 2022, we decided that the first set of of the biggest potential will be the more basic version, which is just bringing text into audio, making it sound human, making it sound emotional, um in just English. >> So, you decided not to innovate on the transcription part or the LLM part, just the last mile, which is generation.

And you you said the mission there was let's try to improve the state of the art in uh like it had to sound natural. >> It needs to sound natural.

So, there the main things that were not possible at the time is you couldn't really replicate a voice um with the same characteristics, and two, you couldn't make it sound and follow the the the entire delivery in a way you would expect.

So, if you have a fragment of text, it's a say a happy happy sentence, if you are reading it, you know and happy, you'll deliver that in a happy way.

If was a dialogue sequence in the book, you know it's a dialogue, so when you read it or a voice actor would read it, you know you need to read it as a dialogue. >> have context of >> the context of the entire thing.

And another time at the same time the LM break first started occurring where you knew that you could predict the next talk and based on the previous talk and so you could bring that context into account in a smarter way.

So that was the first big thing that we knew we could solve and two, we could recreate the voice characteristics of a lot better.

So instead the common approach at the time was effectively hardcoding parameters of a voice. >> Right. >> The the gender, the accent, the age of the voice and trying to predict those.

Instead, we can keep them more abstracted and let the model try to define what those parameters are.

And and those two innovations we knew will fix the research side potentially.

And then on the product side we know knew that a lot of those people will want to create their longer forms with books and audiobooks, create scripts and turn them into audio, uh do the corrections on the on the voiceover for a video.

So we knew that we'll need to build a product for making that easy and and go all in on helping the creators and of course the API to developers to build to build with that. >> So at at this it's 2022, you've had this clarity now that okay, the the state of the art, the frontier we're going to push is the the this this flexibility of the voice, the generation part, right?

Um but it was just you and Peter.

You hadn't raised any money.

I don't think so. >> Yes, yes. >> What did you do first?

Did you Did you go and look for an open model?

Did you try to go call somebody up and use an API?

What what was step one? >> Step one, we we of course were drawing from our savings to to to to get the models off the ground and and and get that first like are we solving the right problem?

And you know that that I think the the clear thing for for for anyone here is it's it was so valuable for us to be as close to the users as possible to keep that interactive loop pretty quick.

Um but then to your point, like the the main thing as we were like actually trying to do the research was of course look what's available on open source, what's available in closed source, and um and then look for the papers in the space.

Are there other innovations in those papers that might have not been applied to audio?

And that was the case.

Uh there's uh the closed source was still lagging.

Not nothing really good, but at the time the hyperscalers so the Googles of the world were still a kind of leading on the best text-to-speech.

Open source was ahead.

So you had some uh inklings of incredible voice models.

There was a a famous model uh called Tortoise from from an incredible guy uh James Betker. >> Uh we're going to have James come do office hours in the class very soon. >> Okay, amazing.

But it's crazy thing about James.

So he was he was at Google at the time.

Uh he was working I think on infra or something unrelated.

And in his spare time, he was exploring audio loop voice and effectively created the best open source model of that time. >> On nights and weekends.

Basically >> As a side project. >> Uh and uh and it was it was it was finally the model that could produce something that sounded human-like on short fragments.

So you could have amazing delivery, the right prosody, right intonation, right emotions.

However, two things were impossible with with that model.

One, it took extremely long time to generate anything.

And then two, it was very unstable below the the um above that short sentences.

So that was the a a tricky limitation.

Uh and then on the papers, there was of course a lot of good innovations coming from the space.

The Fusion in 2021 came out.

Um uh the I mean, the transformer was like uh 4 years uh prior to that, but still some of the ideas from transformer were just getting through to the audio space.

So we knew that combining some of those ideas, we can we can potentially take inspiration from open source, take inspiration from those papers, and try a slightly different architecture for text-to-speech and um and for voice creation of higher quality those voices. >> Do you remember by any chance how much compute you spent on the first 11 checkpoint that was inspired by Tortoise? >> I was tiny amounts in comparison.

I was tiny So, one thing that I recommend uh if you are looking to start a side project or a company is uh is look through all the uh accelerator and quotes programs from big companies that give you free compute and free credits. >> Well, that world is gone.

There's no free computer anymore. >> Okay.

Okay. >> Except for maybe in for this class of students actually. >> I should know that before saying this, I guess.

But, there was a great Maybe they still do something.

They So, NVIDIA Inception program and a few others like gave us >> I remember that. >> The So, we we >> GPUs were still available. >> Exactly.

Yeah.

So, like the first ones for us were in like in tens of thousands of dollars and that felt that felt that felt big.

Maybe it was approaching the hundred dollar thousand dollar category, but like still tiny.

Um I remember like you know, you like in in that days you the budgeting and and sayings uh like um like optimizing your budget is so important.

It's not the compute piece, but I remember us arguing whether we should do a patent for our work, which we decided against.

Uh but, I remember that the the lawyer quoted us uh for the entirety of the patent work $6,000 and we said there's no way we are paying that amount of money for for for anything at the stage and decided not to do it. >> But, it seems like not having a patent has not >> No, I don't think >> I think it like we like ultimately like is it is it even valuable that that that you're >> innovating so quickly that it becomes obsolete too.

Like, would you ever want to stop innovation from the other side?

So, so likely not.

Do you do it as a defensive measures?

So, like then we learn about the whole patent trolls industry that other people but will try to attack you with their own patents that aren't great, but just waste your time.

So like do you do that then we decided like no we'll just fight those cases anyway.

So so so it didn't stop us but but bottom line so small models in comparison they were like in hundreds of millions parameter models at the time if not lower and so that was relatively small text to speech models and you asked earlier just to give you like a quick so that was 2022 and then the kind of the common facet across 11 labs is we continued across research over last years.

So the models of course got bigger and that applied across the entirety of audio.

So we did text to speech model to start then built a transcription model or speech to text model to understand what's happening on the audio side.

Um the wider set of how you bring those models together in AI dubbing how you bring those models in interaction so how you bring a conversational tissue around the speech to text the LLM the text to speech together and even expanded to music.

So entirety of audio and how voice models or audio models work together with other modalities and then alongside build a platform that helps businesses and developers um or solo creators transform how they interact with their audience or how they their people through agents and support and sales with creative tools and marketing and storytelling.

So how you can create that interactive tissue between between an entity and the audience it serves and that's like the common common piece as a >> I I forget when it was cuz these timelines are so blurry now but there was a moment where I woke up um to it like a like six different people texting me a link to a tweet by I think um of a speech by Javier Milei >> Mhm. >> which which had been completely dubbed with 11 labs. >> Yes. >> When was Was that a year ago? >> That was uh 3 years year and a half yeah exactly. >> I feel like everything changed after Some something changed.

What What happened? >> Yeah, so it was so we to give you a rough timeline year by year of like how audio models develop.

So 2022 first breakthrough which which I may my co-founder is like the smartest researcher in the space I I got to know was finally able to bring into the field of how you like get that contact get that that penalty 2023 is where you started seeing expansion around the wider voice over wider narration space.

So you could use text to speech model across languages create more voices.

We created that ability for people to recreate their own voice in a high quality created a marketplace around that and the wider set of creative tooling to help you with the audiobooks for authors creative tooling for authors.

Then 2024 finally brought a good transcription models combined with the LM for translation combined with the speech generation.

So you finally had the AI localization version.

So that was the Javier Milei speech.

So the project was there was like few versions of that.

He delivered his speech on UN and and we brought it from from Argentinian into English so people could could could could listen to that while still having his iconic delivery.

And then on the same year we worked with Lex Fridman on on the full conversations that he had with different world leaders.

So Javier Milei of Argentina all the way through to President Zelenskyy of Ukraine to later on with Narendra Modi of India where you could hear both of them speak that language which was which was a new opening.

So that was 2024.

And then 2025 what happened is you could like roughly finally have those models act in the real time basis.

So you could create more of the interactive voice agent experiences where you could you know you mentioned the kind of the frontier system architecture of combining the stock the same kind of stock applies in the voice agents combo where you can have this cascaded architecture of having speech to text transcription that you have LM to generate responses back and text to speech to to narrated.

So if you are speaking a voice agent that it can predict are you stopping the sentence start generating the response and all of those components can work in tandem to create that that experience. >> So that was 2025 and I think 2026 will see an extension of that of how maybe cascaded I'm going too much into detail but cascade go to fused or cascaded continual cutting the latency to be great.

But back to your question that the first great AI dubbing experiences in where in in that static context in 2024 and um >> and we're really good.

We're really >> So thank you for the the the cheat sheet on on how we got here.

About a year ago you and I started talking about okay, where does the space go next?

And I remember you saying I think you know, we've had this cascaded system so far but now we we we're starting to see what people want to do with it and a big a big part of what people want from a capabilities perspective is is sort of a more is deeper reasoning from these systems, right?

Especially an audio agent that can understand the tone the voice the the inflection the accent of what's coming in because you lose all that context when you transcribe just pure audio.

Um I remember you saying um that there were going to be more and I either some some forms of unification of these modalities um or some new breakthrough where we try to combine these into omni models um where are we right now in terms of how far are we from these like the when I talked to you know James Betker's a good example.

Maddie just talked about James shortly after open sourcing Tortoise TTS, James went to Open AI and worked on ChatGPT advanced voice mode.

And when I talked to the ChatGPT advanced voice mode, it still doesn't understand if I'm angry or sad.

If if I said the same word or the same sentence in a really angry way or in a sad way, it just transcribes it and the audio understanding, the semantic understanding of the audio is very limited.

Why is that and what is it going to take to make the systems more capable of understanding what's coming in?

Does that make sense? >> sense completely and and it's you know, one of the huge questions and we we kind of changed our own perspective over the last couple of years.

Like what is the what's the right approach across the different domains, across other fields.

So to to adjust find that you know, when you have a cascaded architecture, frequently what would happen in the past you would transcribe just the text element, pass it over to the LM to generate and then of course you would narrate that on the other side.

Now of course that's a relatively poor version of that.

What what what you could theoretically do is is still try to capture a lot more of that information.

And now generally you have those two approaches as you think about the future.

One is you continue on the cascaded side, so you continue with the three different models and and potentially think about how they can be improved to continue bringing the right context, optimize latency, continue reliability or you can think about training a model together where you can of combine all of them together.

And then you can fix in between where maybe you'll try to create a a transcription and LM model at the same time but keep the other side separate.

So there's like everything in the in the middle so it's not a truly binary choice but that's the the big question many people on the audio side will will be alluding to.

Like do you go the fuse approach where you train them all together and generate effectively when I say something that voice agent automatically generates a speech token it doesn't go through text or do you go through text?

Like where we are today as we think about our approach to the space as we think about the enterprise the business use cases where the reliability and the smartness and the intelligence of the model is one of the key things we think the cascaded approach is the right thing for the next for the next few years.

And if you are thinking about places where maybe the reliability isn't as essential but the speed is we think the fused approach will be and us and so many of those cases probably for for within a given customer you will probably want to blend and use a little bit of one model and the other depending on what you are solving for.

Now to the actual question we think so there's a kind of those tricky parameters the quality or the emotionality of the speech and the experience of the interaction two is it does it interact not hallucinate calls the right tools behind the scenes in the right way and then the latency.

We think emotionality is fixable in both approaches so we hope that later this year already when you are speaking of voice agent you're excited the agent can respond in excited way if someone is calling in stressed we the agent can respond in reassuring way and we actually just released a new version in in our air voice agent work which is trying to do that trying to detect the emotions on the transcription side pass that over to the LM uses that as the context and then generate response accordingly and that's one of the big like big breakfast on our side to create this expressivity to be able to have this expressive mode finally work what happened behind the scenes to make this possible and was the hard thing is you didn't have that much data that could tell you is that delivery happy sad stressed so over last year we are effectively investing a lot to create this whole labeling exercise to be able to create a data to train that model and control it.

So, finally, we think you have the expressivity, and the second part is you can actually make it controllable.

So, you can define what type of experiences should happen based on the emotions.

So, we think that expressivity or the emotionality quality is largely fixable in both or like will be very close in par.

Our friends at Sesame are doing like a great example of how you can >> Yeah, but Brendan will be speaking in the class. >> Amazing.

So, he will probably tell you of like how they are trying to like finally get through that that that cusp as well.

So, it's almost a race who will be first between us to pass that like emotional voice Turing test across other any of those circumstances.

Then, the second level is the reliability level, and here in general, you want the smartest model.

You want the smartest model to work in the agent, and and of course, we are seeing so much of the innovation happening across our labs.

Our customers, the businesses, whether it's the telecom or Revolut or Klarna, all of them will have a slightly different models they will want to use depending on their use case that we can empower them to to to use.

And then, the second thing in that reliability, as you think about voice agent, let's say you are calling in to customer support to rebook your ticket for for flying to to Poland.

Um there you will want it to authenticate your account.

You will want it to pull your own details.

If you are to process the payment, you want to make sure it's your details that are attached.

So, it needs to be reliable.

It needs to follow that flow.

And here, you are calling so many different tools in that in that in that in in those steps.

So, you will likely go through some two-factor authentication to get the code.

You'll likely want your your email and the database to be pulled up from the information from that from that email.

So, all of that needs to work reliable.

It will take time.

So, how you orchestrate that part is important.

Cascaded models work already really well on that given the intelligence layer.

We'll be fixing that.

And the fuse, you sacrifice that.

You are kind of you need to then bring all that tooling into the fuse model and and it and it becomes very tricky to track what happened in that each of the steps.

What happened on the transcription step, what happened on the LM step, what happened on text-to-speech side.

And then similarly, you cannot give the guardrails or the safeguards to bring it.

And then latency, the hardest.

I think here fuse models are winning where you can make it very quick.

You can make it like respond and roughly 300 millisecond response.

Um but you sacrifice on the reliability piece.

And what we've seen for for for for like our customers, which is the businesses, you don't want that.

You want the reliability over over lens.

However, on other use cases, let's say like a companion use case that we are not solving, in that equation, maybe that's slightly different. >> Right.

I see. >> Uh and that's that's how I would think about that stack.

Um and maybe like last case, maybe in the next few years, the way we think this will transform is if you are interacting with let's let's take that booking airline example.

Maybe if you're just trying to get information about what are the products and services and what where can I travel?

Like where it doesn't have to execute those actions, maybe for that part of the interaction, there is a version of fused approach.

But then the moment you need to go into account and authenticate you go to cascaded.

So, on our side, what we are exploring internally is trying the both approaches um from research of of of of continuing doing that.

And the reason I mentioned we swapped, we like almost the good set of of examples in the field, there's different companies that will explore both of those approaches.

So, there's a very unclear whether the emotionality is fixable with cascaded approaches, uh but but a lot of the the recent innovation, whether that's great work from Sesame or other companies prove that it it is and and hopefully the recent release that we did brings it to another another level. >> So, I I want to pause for 2 seconds to kind of uh sort of overlay something and highlight something Maddy may not have realized he did.

But, did you notice that twice in his last, you know, two 3 minutes of exposition, he gave a shout-out to multiple other teams, right, including Sesame.

Sesame, how many people have heard of Sesame?

Okay, so about half.

You know, you should you'll We'll have Brendan who's the CEO of Sesame, and he was the former CEO of Oculus.

How many people have heard of Oculus?

Okay, so almost everybody.

Yeah, so so this is an important sort of cultural leadership point with that I learned slowly over time, which is there's two types of leaders in the systems world, right?

There's those who see what they're doing as one part of a greater sort of collective collaborative project as an industry, right?

We're at the frontier of this new space called voice AI and audio AI.

Maddy's got one point of view on how that system should be developed for the customers he cares about, the mission of Eleven.

But, at the same time, he's happy to collaborate with other people have different perspectives, right?

And one of those people teams was Sesame.

And I think it was maybe 3 years ago, um shortly after invested in in uh um in Eleven that I decided, you know, Brendan, Ankit, and I Ankit was my former co-founder and CTO of Ubiquity 6.

We had been observing a Discord that there was a there's a really urgent need to have better and better voice models in Discord.

You know, you spend like 60% of your day in Discord and and voice.

And so, I remember calling Maddy up for advice and saying, "Hey, we're thinking about building a new kind of product that has AI sort of a a real-time voice companion built into it.

What do you think?" Right?

And he could have said, "Andre, I don't have time.

I've got a thousand other things going on.

Not something I think about." But, instead, he took the time to really break down for Brendan, for myself, for you know, for Ankit, like what what his perspective would be for Sesame's needs.

And and he had the maturity to say, you know, even though he was a had to fundraise a bunch of money and there's a lots of competitors in the voice industry, you know what, we're all in this together.

You're not really a competitor.

In fact, maybe at some point we could help each other out.

And so I think actually around that time Brendan ended up in Angel investing in Eleven as well.

You subsequently became an Angel in in Sesame.

There's a level of collaboration between now the two teams that is quite rare, I would say in the ecosystem.

I I wish more teams had that approach that Mati took and Brendan took.

Um actually I I think about a year ago, based on some of the insights that Mati had given and Peter had given um Eleven uh sorry, Sesame, they open-sourced a speech model called CSM.

Uh a conversational speech model, which is just different from any of the models that Eleven was working on.

And uh you know that was awesome.

Because that it that model is now on GitHub.

Many of you can use it for your own projects.

In fact, some of the students in last year's project used it.

And that I think is the through line, one of the through lines I want you to take away from this class, too.

You know, you had you heard Andre's life scaling lessons number one last time.

I would say a scaling law from my experience working with Mati has been you know, you can go further together.

Especially in a new space like this, where often what seems like a competitive project just because the VCs or the business ecosystem is trying to create some nice like landscape slide that says, here's audio AI and here are the logos and then here's like, you know, visual AI.

I mean, these these categories and labels are largely artificial constructs, you know, created by non-technical people to try to make progress legible to the world.

But I I I I what I find is really it's people that are driving a lot of this progress and collaborations between people is what drives from the frontier.

And so, I know I'm hyping you up a little bit too much, maybe, but thank you for >> no, this is great.

Keep going.

It's uh You can take as much of it as you can get. >> No, that's that's that's very true.

It's It's very easy to get stuck in this loop of like, you know, like other startups are your competition, and ultimately it like does not matter for the mission you are solving.

It's a long-term game, and and and many of those people will come through different intersections of your path in the future.

So, so keeping that partnership uh or working, exchanging ideas together is is crucial.

And if you are to compete competition, if you are to start a company, you probably want it to be one of the hyperscalers or legacy companies.

It also like will pull you up a little bit.

So, yeah, I think it's >> Well, okay.

So, on that point, let's talk a little bit for a few minutes about the business.

Cuz proof point that you can actually succeed being a nice guy like Matty.

So, when we first met, I think the company had less than a million or two million ARR.

Today, is it public?

What What is it public about where you guys are >> So, we crossed 2025 at 330 million in revenue, and this quarter was our our biggest quarter, and we added 100 over 100 million in additional ARR.

So, now we are over over over 430.

Um >> Over 430 million in revenue in 36 months.

Can we just like pause for a second and acknowledge that? >> [applause] >> This is insane.

How big is the team? >> You know, the it's insane, of course, and and it's crazy that we get the chance to be building and and all of you are building or or developing and learning at like the frontier of the biggest change in the in the world.

Uh where it's like maybe bigger change than the internet or electricity.

Uh the team is Although that in perspective, of course, Anthropic, as maybe many of you have seen, >> Well, they They They had a little bit of a head start, I would say. >> They did They added 11 million 11 billion in additional ARR over last month. >> Yes.

Yes. >> crazy. >> Well, they're they're in the enterprise, but um we'll get there.

But uh well, the the the common thread is like the there's such a clear value that you can provide to your to your customers across in their case knowledge work, in our case how you transform how can any business can interact with their customers.

And um we are 400 over 450 people now.

So, relatively one-to-one.

Um we we have um maybe just to give you like a quick perspective, we have a good amount of people between between uh US and Europe.

So, our biggest bases are in in London, then New York, and then Warsaw and the staff uh are fighting for the third spot.

Um we are all the time actively hiring.

I need to say this.

And um uh we I think that the the the big piece that maybe was slightly different in how we've set up a lot of that that 400 people is we keep it in extremely small teams.

So, each team is less than 10 people, have a big ownership and money to run ahead, make their own independent decisions.

It's okay to be wrong.

The speed and understanding the customer, understanding the problem is much more important than going for this like uh uh uh uh uh process.

And and that's helped us across the journey so often and so much.

That's why we can do across so many different models and then bring them to customers whether that's in the marketing department or whether that's in the uh helping on the customer support side or whether it's growing revenue and helping company figure out how to uh reinvent that with new version of sales or fun engagement.

So, kind of the common thread across all of the product work we do is how you can really iterate >> Right. >> in a different way. >> Well, so uh again, this is my last question cuz I I think um you know, the the final project is the one-person frontier team.

One-person frontier lab, right?

Where the idea is they could now using many of the tools available to them today that weren't around 4 years ago, including 11, can push the frontier or or a state-of-the-art system that uh would have previously needed many tons of people.

And on the business side, what what is it that has allowed you with um such a small group, relatively speaking, to create a repeatable engine where new capability, you know, it results in repeatable revenue.

I think we talked about Anthropic last time where in in that case, you know, uh revenue scales quite predictably with compute.

In your case, what I've observed is revenue scale quite predictably with deployment.

You know, as you built out the deployment team, I would love for you to talk about that for a second.

What what's going on there?

What why why is why have you somehow been able to tell people I'm going to do this much in revenue and just hit it year over year with extraordinary growth, which is quite rare.

Um And two, pricing and let's talk about pricing and packaging for a second because these numbers like ARR, where again, the the the the the accounting of these things was developed in a pre-AI world for software that look quite different. >> Mhm. >> Now people are going, "Should I do token-based pricing?

Annual subscription?

What is the right way to meter intelligence, right?

And meter capabilities of the kind." So, can you talk for a second about those two things? >> 100%.

Yeah, the there's uh and I and I like this ambition of building effectively your final project and uh and it sounds like a fun one, too.

Especially now you can just do so so so much if you if you have that agency and keenness to just to just go after it.

Um I think the two on the two questions on the predictability side, uh it's still hard.

I I it's like actually very I think we you know, we we are uh um happily trying to set a target.

We are currently overshooting our targets.

Um But the main part that is contributing to us to figure out where roughly this will place is is the deployment side of uh we get a chance to work with some of the iconic and the biggest companies in the in the world.

We combine a lot of the forward-deployed engineering to work alongside them, which is the team that effectively figure out how to take the AI and and kind of bring it into the applied AI side.

Be the lab version of a lot of those companies and transform their work together.

And um and in those cases, you know, it's it's um we roughly know how much value we can deliver each year, and then that the really the bi- main bottleneck is can you bring incredible people that are passionate, that have that um that level of IQ and EQ, are striving for excellence, but stay humble.

Like how do you bring those people that are really keen to innovate and and and and be incredible at their craft?

Um So, if you if you are able to predict the growth of of of the of the people, of the value, of how much you can deliver, then you can start getting back to that the predictable part of the business.

That's more on our sales side, enterprise side, which is more than 50% of the revenue.

And then 50% is still uh PLG and and continue growing on the self-serve side.

And this one is a little bit harder to predict because it's effectively a big part of can we continue our stride innovation across the models.

And we took the approach um of all the product, all the research we launch is also available to the to the biggest companies in the world, but we try to make it available for everyone.

So, if you are building your one uh person project in the future, you have access to a lot of the superpower that the biggest companies will.

There are some concurrency limits and of course the the the the closer uh compliance elements, but ultimately you get the same uh capacity as the as the company.

Um but what this means for uh frequently for revenue is that part is less predictable.

Um however, we know where our initiatives are lying and roughly can can can estimate like what's the what value of the world.

And happily, frequently we see the value for the world is bigger than than we expected.

Um That's the the first one.

On pricing, always think about the value you deliver to the customer and work backwards from there, never from the cost of how much it runs to do something.

If you deliver the value, you roughly want to capture 1/10 of what you deliver as a value in your packaging.

And any pricing and packaging that accomplishes that, which is the hard piece of like how you calculate the value, how you drive that good uh metric for that is is the problem frequently more than anything else.

So, never start from the cost, start from the value and work backwards from there.

Thank you for the question.

The big question is uh voices with a lot of the technological advancement, you can replicate voices relatively easily.

What does this mean for the future of the of the security and safety in the space?

So, I think there are two parts.

The one we as a company uh given we we develop our own models, we can actually build and and bake in a lot of the safety inside of the models.

And that's something that we've done from from from the start, whether that's being able to like trace back the content that's generated back to who generated it and take action as needed to moderate whether you are abusing and doing a fraud or scam and stop it before it's generated or flag it internally.

And then three, contribute to the wider space, which is where we think it's headed.

It's like, can you have a publicly available system where you can uh drop an audio sample and get information?

Is it AI generated or not?

Have a watermark piece.

And that applies as much to the negative version of the use case, but also on the on the positive side.

If people will want to license their voice, how do you make sure that it was licensed in the right way, which we, you know, we work with people like Sir Michael Caine or Matthew McConaughey.

And you want to have that information in there.

Two, to your second part of the question like a lot of systems today will rely on voice authentication in uh banking systems and other parts.

We think this is not the future and you should step away from this and not use that as an authentication side.

We think that's uh from the security perspective, it's the it's the it's the it's the wrong approach.

Um and every so often we see an interesting way of using voice agents against abusers, too.

We had this amazing charity we worked with for based on IP of a caller could detect where they can be a likely scammer.

And if it was a scammer, so kind of opposite of the usual, they would serve it a voice agent.

And the voice agent would then speak with the scammer, and the whole intention was to waste their time.

And some of the most fun conversations happened from that from that part.

So there is some ways >> Counter offensive. >> Troll the trolls. >> So the question biggest bottlenecks for 11 labs and maybe for wider audience space.

You know, beyond the obvious ones which is which is incredible people, incredible research they kind of continue innovating on the architecture side.

And apart from compute, like the main thing from the research we would love to fix this year is how you combine so we spoke a little bit about cascaded architecture of how you create the speech to text and then text to speech.

How you can make it truly interactive.

Where where where it understands your emotion and understands can pull up any of the knowledge from your systems and become the personalized extension of yourself.

So maybe the non-obvious one it's you know, every every time you interact with different service you interact with different experience, you will have your own preference of of what's good for you and what's good for everybody else.

And we are trying now to figure out how to make that interaction like really custom, really personalized and really good for all those cases.

And just to recap the obvious one so hiring just architecture side compute if we had more compute you can run more expense more models.

There is a version where maybe too much compute is also harmful like the necessity is the matter of invention is also helpful in some cases. >> The optimal amount of compute. and that preference piece of what really works is is going to be helpful.

And like maybe a good example of that in health care space if you are deploying an agent that is taking appointment but then follows up with the person, asks about how they are feeling, um, maybe recommends, uh, additional points.

You need to transcribe very different nomenclature and make it perfect.

Um, there's also different people and how they will communicate.

Some people want the a slower delivery.

Some people want a faster speed.

So, how you cater and make that experience unique and different and deliver the most value is is, uh, is not so much of a bottleneck, but more like thing that we want to solve and we know we need to more collect more data, collect what works and then apply to the industry.

About the the difference, um, and and the other complications, um, on the training side between the cascaded approach, uh, and the fused approach.

So, the, you know, when you work on the cascaded side, of course, you, uh, you get to train the models independently to large extent.

Um, uh, but then you need to figure out how they work in tandem together af- after that.

So, you spend, uh, kind of quite a bit of time on on trying to figure out what will the interaction look like when I combine them together.

And when we actually together, you might need to fine-tune and tweak some of those experiences.

So, we spoke about how you finally got the con- controllability and emotionality of that work.

The pipeline for passing off, uh, on like transcribing the sentiment, is it a stressed speech and then passing that as a parameter and making that the delivery emotional.

You need to bake that in as you're training the model before you combine that in the in the in the in the pipeline.

So, you need to bake that in in the training step before before you bring that across and maybe there is a version of how you do the language control or how you specify the, um, pronunciation in different setups which you all want to make sure it's it's clear.

Um, on the fused approach, there's more of the emergent behavior, of course.

So, so you get that for free to some extent.

But the main thing you need to do in the training side, which is the usual complexity, you need a good open-source intelligent, uh, model for intelligence, an LLM, that you can bake into that model.

And then there's two complexities.

One is how you fuse the tokens from the text space to the audio tokens, super hard, and most people cannot figure that step out.

And then the second part even if you do figure that out, you do rely on the open open models that are out there in the field.

And today at least the open source will lag behind the closed source in the intelligence space.

Good day.

Question was around the future of 11 Labs and what what's what's going how is it going to look like in the five years between the models, between the platform, between the the the application side of our work.

At the core five years is an interesting time and because there's so much research that we know we'll need to have in two three years and we think there will be still still improvements you can make beyond that.

But at the core we know we want to continue leading the space in all foundational research around audio.

So whether that's the conversational models and the future whether that's how you fuse it with other modalities is going to be a one of the big part things that we want to be the best at.

So like truly be able to pass that voice during testing any conversation and potentially extend it to any interaction.

So on the research side what this means for the text space already to potentially visual avatar space.

We want to be that lead that leading frontier continuously specifically figuring out the conversational or in the interactive side.

So step beyond voice and that The platform it's effectively where we see the the biggest value we can provide in that five-year time frame.

So as the models start becoming more incremental, you need to really understand in depth what the business what the what the what the creator or the developer is trying to solve and give them the tools to to do that.

And for us it's going to be the the effectively the go-to platform and in some ways we imagine in the future the same time the same way you have three or four clouds that serve all the compute needs on the on the cloud stack, we imagine there will be likely three to five platforms that's that help on that conversational setup between any business and their audience.

And we want to be one of those those platforms, whether that's in the in the in the conversational setup in the support and sales and in in in in that in that part of the business or whether that's the marketing and how you engage your customers on on on on on being able to deliver the better story all the way through to the internal of how you hire people to scale and train them to then to then let them continue get that expertise.

So, if we can be that for the for for the businesses and in some way everybody will be that maybe one-person business, we we we we we will do that.

And maybe last part on your question because that's definitely something that's back in our mind.

It's where does the platform and application start and end?

We think this will blur in the future of AI where you will be able to create those applications on the platform much easier than you were in the past.

And and we hope to provide all the different modules for the builders of the future to be able to build to build that seamlessly.

One of the proudest work we do at 11 Labs is actually working with people that lost their voice and we can bring it back.

So, people with ALS or throat cancer and and so far we've been able to work with almost 10,000 people that lost it and we could synthesize it back so they could communicate naturally, which is uh which is we hope like something that can be available for anyone anyone in in need.

Um And similarly on the question around around Ukraine.

So, maybe to give you a quick context what happened there.

So, of course in that when the war started, the government didn't need to figure out how to provide a lot of the usual services to people everywhere around the country.

And as you can imagine, all of the people will just not have the usual access points.

They will not be able to go to uh to a local administrative office to get help on um on you know, where can you travel?

What benefits can I have because I'm being displaced?

How can I get additional support for uh for food or benefits?

So, it's like a lot of different problems that you need to face.

And that stretches across the entire economy.

And education is the same thing.

People cannot go to a school in the usual way.

How do you deliver that education to the people that that need it?

How does the government send messages around the country efficiently if you don't have that access in the same way?

How does it send it outside of the country so people know what's happening in Ukraine?

So, the way one of the many initiatives they've done uh was creating a central citizen app called Diia, where every person can access a lot of those services going directly through their mobile device and and and gets access to information what's happening, uh some of the educational courses, or or some of the guidance.

And um and one thing that that was missing in that equation is how can you open up even further where people uh that might not have that technical acumen to to to be able to get that?

How can people um that might not have the internet call a number and get that information um in an easier in an easier way?

Um so, we worked with them effectively on adding that voice side inside of um uh inside of the app and outside of the app so people can make it a lot easier.

So, I traveled to to to to Kyiv at the time to to work and understand those problems and and and work with different set of their ministries on on that work.

And you know, one very clear thing that came out it an an incredible model of how they were running it.

So, every ministry had their own technical resources to try to innovate and bring that across, not go through the red tape, go independently, go quickly, and bring that across.

And so far we've seen an incredible way of people being able to engage with the government and something we think might be a version of the future of government services.

How incredible if everybody here could could could could open an app and have access to your to your passport, to your driving license, all the way through to access saying the best educational courses maybe like the Coachella course directly from the app, too.

Now to your second part of the question, which is important on like how we think about approaching our work with um with governments in the in the war zone.

Ultimately, as a company, we are choosing to be Western allied and and countries plus their allies and support their work in in in a way that's of course following the the legal the legal guidances and something that that we'll continue continue to do. >> Can we Can we talk for a second about since we're in the zone of sort of sovereign scale deployments?

Um how are you thinking about China?

I mean I I are there distillation attacks you're seeing?

Um you know, there's a bunch of news this week about how uh a number of nation-states have been trying to run distillation attacks on Western companies that produce models like 11.

Um is that a concern?

How do you reason about the ecosystem in China, which historically has been very collaborative with the Western ecosystem, but there's tensions on various fronts.

How How should they think about that topic? >> Yeah, I I think in general there's a clear race in AI of of, you know, uh the Western world and the and the developments on the on the China front.

Um from our side, we we try to stop all types of distillation attacks, uh period, but of course uh with with any any any of the kind of IP coming from that region, we we are taking that as additional strong signal of how we can build that into the the the protection.

Um the truth is there's and I'm I'm thinking about some of the other questions that were asked that there's a lot of great models coming from that especially as you need to optimize for that language layer, too.

So, you need to you need to really get the nuance of the dialect, of the accent, of the different voices.

There will be models in the region that will be better than 11 Labs models for their use case in the remit.

Um Uh and and to large extent, um we try to outcompete them on that on that level and provide a better service to to the companies on the other side. >> And you know, as it relates to the open ecosystem, because one of the things as we've talked about is having a good open base model allows you to then customize it for various enterprises, for very specific regions, deployments.

What we're starting to see at least in some of the other modalities coming out of China, like video models, a year ago, lots and lots of innovation, lots of open video models.

Now, not so much as they It seems like as several labs start to catch up to the frontier, you know, See Dance is a great example.

It was a soda video model that came out.

It's not open source.

Uh or it's not open weight.

Is that a trend that you think is going to continue?

What does that imply for a team like 11?

And what do you wish more participants in the ecosystem like the students here, other labs in the space, would be thinking more about or doing that would collectively help? >> Yeah, that great question.

I I think that So, there are two parts.

Um like as we look at the models in in that space, frequently we take slightly different approach in general because there's the the research element we spoke about, the product element, and there is the ecosystem of how you become a trusted brand that people can can work with.

We briefly skimmed across one of those examples of like how you can create and give ability for people to create their voice, share that voice, and earn possibly on that voice, and figure out how people can participate in that model innovation, too.

And that's like a stark different approach between like some of the work we do on that front versus some of the the the the wider models that um uh players in China will take.

And the same will apply to video, of course.

You've probably seen the the work on like how people approach the IP from Disney or Netflix on that side, and how they approach it on on the on the western side.

So, I think that's kind of the big dichotomy, and I wish they didn't, and I think um on the security level question, it's going to be a like almost a big combination of the work that everybody needs to do, where you uh you you can contribute your work, but then you need to figure out the watermarking system, and you need to figure out how to have the the the models coming from China follow that paradigm.

Right.

Or at least if not, then you don't serve the content or don't give the same content um permissioning on some of the platforms.

So, there's a I think the two different parts.

One is how you think about the wider ecosystem participating in a model.

Two, how you bring um uh bring the safety parameters around uh I see. around around around the models in in tandem.

And three, uh in general, of course, very helpful that open source ecosystem continues, and I can hear you think phenomenal work to help nurture that across the the companies out there, where um where ultimately you will have always incredible set of builders that need access to the weights, whether it's to fuse the models, whether it's to fine-tune the models for different cases.

Um and I hope our open source our meaning western open source models are at least at par or better than the the the ones coming from there, um which which I think we have a chance to do. >> I I hope so. >> Some great speakers coming from here as well from Australian broadcast labs that will speak about this.

Effectively, why do studios not adopt um still like why they're hesitant of of switching to a lot of the AI voice-overs and is it is it because of the fear of AI slop or the backlash itself?

In general, as we think about a lot of the creative tooling that we provide for for studios or creators, uh we heavily believe in this concept where um you want to use the tools effectively middle-to-middle rather than end-to-end, meaning you will have the story you want to tell, then you will use the tool to create a narration in this case, then you will want to refine it, then maybe recreate, and then you can get a great output at the end.

So, there's this this um big iterative step that needs to happen and why we think about this like this kind of mid middle-to-middle AI part that it will replace.

Uh as I think about AI slop version of that, I think about the kind of end-to-end version like can I type a prompt and get a voice-over or video or any any any of that way.

And that doesn't carry it doesn't have either the initial input of the story or doesn't have this great interact iterative spirit of that.

And I think studios realize that.

So, so I think studios realize that, but at the same time you'll have very different set of studios and I think you know the the high end of [snorts] the version of Hollywood version is just getting there where the quality became good enough where you could go through those iterations and finally get what you intended.

So, to make it more specific, um until very recently, you were in the speech side at least, you would give a model a text, you would rely on the model to read out the text in the way the model uh thought is best and you could regenerate it, it would understand the context, but ultimately, it would be down to the model to decide how to narrate it.

Until 6 months ago roughly, we finally figured out how to control it like the director would do in those studios where you tell it, "Redeliver this in a slightly more dramatic way while slowing down a little bit." That was a big breakthrough and bottleneck for that to happen.

And and in the last months as that started happening, we started seeing more studios finally adopt that technology in their work to to bring that.

Of course, too, there is definitely understanding from the studios that if you are to bring that technology, you need to figure out how the wider economic model will will work.

Like you want to respect the IP of the people you work with.

Um and the economics of that haven't been figured out.

Like how much do you charge for AI voiceover of a person that would not otherwise go to the studio?

It's um so I think studios from our conversations and and ourselves are trying to figure out what's the right balance in those economics.

Um but frequently what we see like actually happening is you will have AI replace parts of the work that um that uh that you wouldn't want to do in the first place.

So, frequently in a studio you have a scratch work that you read and want to listen to.

Post-production is almost where it's stuck there where you repair the lines.

And then ultimately the actual delivery you want the the additional art coming coming coming out in the in the top end.

Um and then of course there will be like other things that that they will start with which is AI localization or interactive experience of how you can bring experience and and and and and and interact with that with the movie.

So, that's where we see like most of the the use case and as we think about the future, the the two pieces that will be stopping at is figuring out the economics model that's backlash related.

If you don't figure it out in the right way.

And then two, um the step changes that were impossible to make that really high quality versions are just becoming possible.

Uh but I think there still needs more needs to happen as you figure out like high enough that kind of that content.

So, will the models be on the device and and and how we think about 11 Labs future in that context?

But anyway, when is this when will put it on uh stream? >> Uh I think tomorrow. >> Okay, tomorrow.

So quick.

Um I guess I can still say it, but we finally figured out how to bring our models on device.

So, we will we will um So, we we we found a way to constrain it to a given language and uh potentially bring it to any device out there, uh which will be selectively working with with bringing that and opening it up to a to wider side of the audiences, which which is the big innovation there.

Um But, it's still the quality There's There's the There's definitely quality difference between on-device version and of course on-cloud version and the wider set of things you want to do.

So, the on-device version will do text-to-speech, but you still won't have the wider transcription interactivity, how you transfer the emotions from one side to the other, um how you make it uh with additional kind of reliability elements built built in.

So, there's a gap definitely that will will will exist between those for for a long while.

And you still haven't fixed them on that side.

Um And maybe as a quick side note here, our approach in general as we think about on device was we need to fix quality first.

We want to make it as good as possible.

Only when we do that, we'll consider bringing that on device or on prem.

So, like instead of trying to go on device with lower quality, we want to deliver the best experience to everybody there in that context.

And I think that's like starting to happen, but still not happening in everywhere.

We think it happens on the text-to-speech narration, less so on the interaction.

Um the role of ElevenLabs in that future will continue being the the platform of how you really go deeper in the problem that the customer is facing or the enterprise is facing and delivering not only the models, but delivering the wider tooling that's required for you to bring that technology in the field.

So, how you bring that applied AI to your local So, to your to your Exactly.

To your custom context work.

So, you know, if you are deploying that in a um in and a any any interactive support or sales contact, you will need the entire knowledge base of how you want the the interaction to work with your customer.

You want the piping of how it calls the phone number or it goes through chat or WhatsApp or email.

Um you will want additional tool calling to get and pull data from the database um from Salesforce or ServiceNow to to deliver that experience.

And then the whole framework of how you evaluate, monitor, test that is essential.

You it's like is it working?

Can I self-improve based on that?

Um what is the domain test that I bring?

So, well, we spoke about the the the the route scheduling for airlines.

How do I know that there is additional space seats available in that route?

You need the the the the test for always checking for that primary being true.

And if you left customer happy.

So, in that future where models become more available, we know there is a still a huge gap of what the models can do and what you need to bring that in that um enterprise context or even creator context for question earlier earlier on. >> We are out of time.

But thank you, Maddy.
