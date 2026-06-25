# Stanford CS153 Frontier Systems — Ben Horowitz: "Venture Capital Systems, Network Effects"

**Speaker:** Ben Horowitz (Co-founder & General Partner, Andreessen Horowitz / a16z) · interviewed by Anjney Midha (CS153 co-instructor, a16z — Horowitz's former firm)
**Channel:** Stanford Online · **Upload:** 2026-05-11 · **Duration:** 1:06:17 · **Views:** ~12,095
**URL:** https://youtu.be/B8NvdfssGac
**Source tier:** Tier 5 (book-talking) — a16z co-founder on a16z firm-building + portfolio + policy agenda. Heavy a16z lean ("Wall Street's always wrong / the SaaS apocalypse is overdone" talks his own book — a16z owns Navan, Databricks, etc.; the policy view promotes a16z's DC lobbying). ~⅔ off-thesis VC war stories; the investable kernel is the moats taxonomy. Discovery-only; spoken numbers soft → verify at primary.

## Transcript (Tier 3/5 — not a primary source)

Please join me in welcoming Ben Horitz. [applause] So, how many of you heard the song that was playing right before?

Does anyone know the name of that song? >> We Are the World.

Yes, that's correct.

We Are the World is a 1985 single by a super group of musicians that all came together to raise it's a it was a charity single that um was produced to help raise funds for the famine in Ethiopia I believe in 1985. >> Yeah.

Lo Richie made a good documentary on it if you're interested. >> Correct.

The the reason I'm bringing it up is because um Ben is known for many things.

He's the founder of Andre Horowitz, co-founder of Andre Horowitz.

I'm very lucky to have called him my boss for a few years. >> Yeah. >> Um he's also been a founder CEO.

He's built several technology companies.

He's behind one of the reasons venture capital still exists today after many moments when it there were times where it got threatened, including the SVB financial crisis.

But the thing I've learned most about Ben is from a documentary that Ben told me to watch about a year and a half ago. >> Yeah.

Yeah.

Yeah.

Triple OG.

Yeah.

Yeah. >> It's called The Greatest Night in Pop.

And I would really recommend uh folks who haven't read it.

Uh sorry, watched it to go watch it.

We're going to put it in the in the reading assignment for this class.

It's on Netflix, so anyone can go watch it.

But it is the documentary about the making of that song you just heard, We Are the World.

And there's somebody in the documentary that come that that you you'll observe if you watch it by the name of Quincy Jones.

How many people have heard of Quincy Jones?

Okay.

About 30%.

So we need to we need to school the kids a little bit on it.

Um >> yeah, he he he was um he was the greatest.

And I didn't think >> great great human being. >> Great human being >> and more importantly great leader. >> Yeah.

Well, that that was the thing he could do.

He he was the best at handling super talented, difficult to handle people of all times.

No question. >> Yep. >> And you can see it in the dark. >> Yep.

There there's a moment in the documentary where the camera is following Quincy around and he's walking into the studio where the the musicians all are and he points to the top of the door and he says read that and there's a sign above the door that he's scrolled uh on a piece of paper and he's stuck up there.

This is at like around midnight when before the stu the recording session is supposed to start and it says check your ego at the door.

I think it says leave your ego at the door.

Leave your ego at the door.

Sorry. >> Yeah. >> And uh if I had to summarize Ben Horowitz in sort of one line, I would say he's the Quincy Jones of technology. >> That's a lot. >> High [laughter] bar. >> Yeah.

Yeah.

That's hard to take that credit.

He He is amazing.

Yeah. >> Ben, >> thank you. is known for many things, but I think the thing he'll be most known for throughout history will be his leadership, the lessons he's left with a lot of people uh over the years, many many which many leadership lessons wi-i which I think are still not legible to the world yet and will only become clear over time.

But today, Ben, I I think it would be helpful to take everybody here a little bit behind the scenes of what it took for you to become the Quincy Jones of Tech. [laughter] You're not supposed to be blushing this hard, Ben.

I mean, Quincy.

Yeah, having known him, he's he's a very high >> That's a high bar.

Anyway, thank you for being here.

Why don't we start with let's let's zoom back all the way to the founding of Andre Horvitz.

Let's start there. >> Yeah, >> this is a systems class and recre end up being one of the most important innovations in the systems design of venture capital >> of how capital should be deployed. >> Mhm. >> You know where we'd love to contextualize this is the the students have heard that three or four of the largest bottlenecks >> to progress are data.

You know, context feedback, >> right? >> Compute, capital, and culture. >> Mhm.

And we haven't talked that much about capital and culture.

So today I hope you can take us a little bit to the frontier.

What's going on in capital and culture especially in in labs in startups and teams that are pushing the frontier.

But I think to get there we should rewind a little bit and start with what was the system that you created to even allow capital to get to this point. >> Yeah.

So uh you know we started the firm back in 2009 and at that time there there were a couple of ideas about venture capital that I I would say uh we thought were dated.

Um one was like it was mostly an investment idea.

So the product for investors LPs was really good and that they had very high returns but the product for entrepreneurs I thought was like pretty bad and that they didn't do much for you other than uh give you money.

So that was kind of idea one that we thought we could just build a better product for entrepreneurs.

And then the other idea that was very very kind of prevalent in venture capital was this idea that you know in any given year uh there would be and the the historical data really supported this there would only be 15 technology companies that would ever get to $100 million in revenue.

So the whole industry was just about getting invested in, you know, as many of those 15 as you could.

And that kind of just limited the size of the whole industry and and the capital in the in the game.

And we really thought that was going to change because um you know look at that time we thought software was going to eat the world and every company that was going to be interesting every new company was going to be a technology company and therefore there were going to be more like 200 companies a year that would hit that bar not not 15.

And so we decided, you know, the one of the things that um I did as a as kind of the CEO of the operation was to say, "Okay, um how do you scale this?" Because venture capital for firms kind of notoriously uh didn't scale because they didn't have to.

Um you know, it was I remember Dave Swinson who is the most famous LP said, "Yeah, a good venture capital firm is like the size of a basketball team." you know, you know, five five guys and then a six-man or something like that.

And and you know, that that was not going to be enough to have a great product for entrepreneurs and then also invest in, you know, such a large number of companies.

And so, you know, to get to scale there there was a couple of ideas that we had that, you know, are sound very very simple but ended up being important.

The first was um in normally in venture capital uh it's a partnership and the partners share economics and control.

Uh and the problem with that idea and you you you experienced this in your career at uh at other venture capital firms is if you share control um then things get it becomes very very difficult to change the organization because everybody's got to agree.

And if you know anything about like uh running an organization, the one thing about a reorg is some people are going to hate it because it's a redistribution of power.

And it's not necessarily the people who aren't good.

It's just like some people are just going to hate it because nobody likes to lose power.

And if people get a vote, then there's no way to like effectively reorg uh you know, reorg business.

And so you our idea was like you can't share control. we'll share economics but we'll centralize control and that ended up enabling us to reorganize and enabling us to get into many many more kind of categories like American dynamism or crypto or bio or these kinds of things because we could change the organization and scale it and so forth and you know that ended up being like a an important kind of systems idea and then we also kind of decon because investing thing is always a conversation and you need a very very highfidelity conversation to get to the truth.

Um, you never want more people in the room than can have a >> and so you can't have a conversation with 30 people.

It's not possible.

That's a presentation. >> What What is the optimal um over the years?

What do you think is the optimal construct of a truth-seeking conversation when you're trying to understand the future of a technology that's super complex?

Yeah, I think that like if you have really good chemistry and rapport, it can be like seven.

Um, but if you if you don't then then then even that gets problematic.

But yeah, you just can't do it with a large group.

And so you you what we ended up doing is we just kept kind of splitting the firm into smaller and smaller groups over time.

Uh, and each group would address a certain part of the market. uh and that you know that ended up being very effective >> and um to contextualize for folks so when you started the firm the first fund was about 300 something million 320 >> 300 million and you had all these sort of institutional folks like David Swenson and so on who had these like sort of long-held for whatever reason priors and assumptions y >> what did you find was the most effective way to realign them or get them to revisit those assumptions in order or update those priors in a way that was aligned with your mission well, succeed.

I mean, like like that's all it is.

Like I think one thing, you think another thing.

Um we're going to find out if I'm right.

So then the first thing that that happened was was we invested like a quarter of that $300 million fund into um the Skype buyout, which everybody thought was insane.

Uh but um like we we knew there was a bunch of things we knew that other people didn't know.

So the first thing that made it insane was like the deal itself um when it spun out of eBay. eBay didn't own the IP.

They own the company but not the IP which how they ended up there is like a crazy dumb story but by the way never do that.

Never buy the company without buying the IP.

So the founders kind of had this hold on them where they could have sued them and shut down the service.

Uh and so everybody was like, "Oh, that's an unbiable asset." But like we knew the founders, uh Giannis and Nicholas, and we knew like the one thing they had in life that defined them was Skype. >> So they weren't going to shut that thing down.

It was just a matter of like how much money did they want?

How did they want to be on the board?

Like >> the IP at the time was basically the Skype client and the user base.

It wasn't the client, it was the underlying kind of library that controlled the protocol. >> Oh, sure.

Okay.

Um the communications protocol. >> Yeah.

Which was, you know, very hard to replace and all that kind of thing. >> Uh so, so anyway, we bought it and everybody goes, "Okay, well, even though we thought you were nuts, like maybe you're not completely insane." >> Um there's so many interesting parallels to that era and now, but um you know, one property of that era was the explosion of networks. >> Yeah. you know the idea of network effects became legible for the first time as a systems concept.

So can you talk a little take us back you know I think it's hard for people now we just take these for granted but at the time can you talk about why was it novel why were people resistant to it and what were the insights that then led to the architecture of the firm being a network effectdriven firm yeah I mean I think that I think people just didn't understand network effects as well.

So the big era of networking kind of started with the internet and then people thought the internet itself was just like a unique network and and it was weird.

It was different um because nobody like people got value from things built on the internet but the internet was not owned by anybody.

It was like the kind of first real decentralized network.

And so people didn't know what to make of kind of networks that like I mean Facebook early on had you know there weren't like a ton of people giving them money for the first round.

That's why Peter Teal was able to do it you know at a at a really good price.

Um, and then you know kind of the same thing with Twitter and so forth like people just didn't know uh that basically they how invincible those things got when you you kind of got them up to strength.

So that the bigger you know it's basically like an n squared value.

So every node you add kind of um increases the value by you know uh kind of n squared.

So like if you have five people on the network, you know, that's 25, but if you have six, that's a 36 and so forth.

Uh, and the value, you know, if you get up to internet size is just invincible.

Like nobody's going to ever build a rival to the internet or very unlikely.

Um, and so, you know, at that point, you know, us being involved in the internet and Twitter and Facebook and so forth, we we had like a really good understanding of that.

Um and so you know we always uh thought of the firm as a network and so you know from the very beginning we thought okay the more relationships that we have um the stronger our network effect >> and so we ended up doing things that other firms didn't do like we um try to build relationships with like every engineer in Silicon Valley and you know every executive and every everything um and that and then every corporation that bought technology and so forth.

And we were in our minds creating kind of this network effect that would just make us the best place to raise money from because we were like an automatic.

You could tap into that network and become extremely powerful like right off the rip.

Uh and you know, I think a lot of people um didn't understand like how hard that was to do.

And then the bootstrapping of any network is always the most difficult thing.

So like yes, if you have a network with a billion people on it, it's going to be very valuable, but like you know, how did uh Alexander Graanbell sell the first telephone when there was nobody to talk to?

Like that that part is actually really hard.

And so figuring that out and how to bootstrap the network effect, you know, kind of coming from behind in venture capital was was the idea. >> Well, I mean could you say a little bit about how you bootstrapped it?

What were the things that may be now lost to the annals of history where they were individuals or asymmet you know one of the things we talked about in the first class is >> um you know often the students get excited about the speakers like you up here but we reminded them that one of the most valuable assets they have is the people sitting next to them >> right it's it's the relationships they build >> when you were bootstrapping >> I think that's getting more important by the way >> exactly there's anything that's going up it's that value right so but if you zoom back when you were starting that bootstrapping and you didn't you didn't have the largest firm in the valley you didn't have the most capital you didn't have the you no track record as a venture capitalist other than your angel investments.

How did you boot what were the moments where that may not be legible to folks here that you used something that was asymmetric that allowed you to bootstrap the network? >> Well, the really simple idea was we knew like venture capitalists made a lot of money, right?

So, they would take the fee money and then they pay themselves big salaries.

And so, we were like, well, what if we didn't pay ourselves anything?

Um, and we just took all the money and we uh basically spent it on building this network, right?

So we would hire people to like bring people in.

Um we, you know, with our kind of, you know, how do you get relationships with every big corporation, FedEx and this and that and the other.

And the the the trick that we had there was we had um sold uh the previous company to Hillet Packard.

And so we knew the people in their enterprise briefing center.

And so we would call them every week and say, "Who's coming to the briefing center this week?" Um and can we get their numbers?

And we would call those companies and we would have them come to our briefing center uh and we just show them all the startups.

So it would be like you know and we'd have everything they like all the donuts and all that stuff you know so it was like very unventure capital like um but you know the the corporations loved it.

So all of a sudden we knew more big companies than VCs who had been around 50 years because we had this hack through the HP Enterprise Briefing Center.

I think it's very poetic that we're sitting at Huelet 200 by the way.

This is the name of the auditorium. it all comes back full circle.

So um you know when we started doing that usually when somebody new shows up on the block with an insight like that I my from a systems perspective what what we've observed is often the antibodies come out. >> Yeah. >> Right.

The immune the immune response of the existing incumbent system comes out. >> Yeah. >> At the time I was across the street with Mike actually at Kleiner.

I remember, you know, there was a, you know, A16Z was in the headlines all the time >> and like our CMO at the time, great lady, but I, you know, I remember taking one of the headlines to her and saying like, you know, we should do this, too. >> And she said, just executive briefings, I just marketing. [laughter] >> Yeah.

And I said, yeah, that's your job.

This is working. >> Yeah.

And and I've been consistently shocked by the number of times A16Z has done something from a product insight, deliver that to the entrepreneur, and then everybody else just says, "Oh, that's just marketing." Is that am I am I being overly facitious or is that true?

And and what were the immune responses like that that you were experiencing?

And how did you deal with them? >> Yeah.

Well, it was funny because um in every time we'd meet with our investors, our LPs, they would say, "Every time we meet with another venture capital firm, all they want to do is talk about you and and say mean things." And I'm like, "Well, that's fantastic. >> That's great. [laughter] >> That's good." They used to call us A-ho.

Um that was their nickname.

The other VCs, you know, they hated us.

Uh, some of it was my fault though, you know, like because when we started, I was coming from enterprise software, which is like a very competitive bare knuckle kind of there's no such thing as co-opetition in enterprise software.

It's just like kill or be killed.

So, I did a um I did it like I I wrote this blog post called four things that VCs do that I don't like that where I just like attack them all.

And then I um I did this big there was this uh Sarah Lacy had this big big uh event and she interviewed me on it and she's like well you know you seem like kind of you don't like other VCs.

And I I quoted Lil Wayne.

I said um when I see another VC coming at me with the peace sign all I see is the trigger and the middle finger you know and everybody hated me for that.

You know, >> I I >> But but it kind of worked because because they hated me so much.

They weren't willing to copy what we were doing even though what we were doing was working.

So it kind of backed I I don't know if I would have been that antagonistic again.

Uh but you know, it worked.

So you can't argue with it.

Well, I I Okay.

Well, I think we should come back to that later.

What do you do differently?

But yeah, so >> great.

You bootstrap the network effect that allows capital deployment to start scaling into a bunch of startups.

Now it really does feel like a back to the future moment a little bit, right? >> Yeah. >> What's going through your mind right now? >> Yeah.

I mean, I think so.

So, the big the big thing that's changed um is that or or the kind of most fundamental thing that's changed from a VC standpoint in my mind is it used to be I mean, for my entire career, the one thing that you knew about technology companies is you couldn't throw money at the problem.

So, if somebody had a two-year lead on you, you could not hire a thousand engineers and catch them. that like was never going to work because um you know nine women can't have a baby in a month like there were just things you could not parallelize and then the communication overhead would kill you and my favorite joke used to be you know what's a man year it's like 700 IBMmers before lunch right like that you know it's nothing uh you can't you can't catch that that way with AI that's really changed and that you can throw money at the problem because if you have enough GPUs and enough data you can basically solve most problems right now.

Like that that just is what it is.

And so now um you know the capital race becomes a real thing and you have to think through okay code is not really a moat uh the way it was in the past and like user interface isn't really a moat and and so like what is like your barrier to entry like what is the thing that differentiates you over time? um these have become like really really different and it's happening at the same time that you know demand uh for the technology is unlimited because the products work so much better than anything we've built before like these I mean many of you are too young to remember the products of old but like none of them worked this well before like this is like wild how well this >> or even companies didn't always go from 9 to 30 billion in run rate in like six weeks >> well but the reason they go that fast is like you use them and you go wow this works perfectly.

Um, you know, I how can I do more with it?

Uh, whereas in the old day like if you bought Seabil system software, it took two years to deploy the thing in a million dollars or at minimum and like so that's going to limit demand.

Uh there is no limit on demand when technology works as well.

So, so you would say an that the technology is working at at um in a way that collapses >> the the sort of gap that existing incumbents might have as a result of their human capital investments over the last whatever decade of software there's willingness to pay at levels that >> yeah I mean the return is crazy right like so I mean if you make an engineer 20 times as productive >> right >> and you're paying that engineer well if you're a Zeke you're paying that engineer a billion dollars But, you know, like if you you're you're paying whatever, it's going to be at least several hundred,000 a year.

Um, that's a hell of a return, >> right? >> So, that creates this.

So, you know, the final project for the class for the students is the one person Frontier Lab. >> Mhm. >> Because what we're trying to get everybody to realize is there's actually an extraordinary amount they can accomplish with the right tools. >> Yeah. >> Right. >> But we have an entrepreneur like that right now building a global VPN by himself. >> Yeah.

Yeah.

And this this started to become more common I would say on when we were seeing pitches I mean almost a year and a half two years ago now, right? >> What does that mean for folks here who don't have necessarily access to the most capital >> may not have access to a ton of compute either.

What would you say is and but want to make a difference to the frontier? >> Right. >> Well, I mean I think saying um I just be careful a little careful with like people don't have access.

Okay. like anybody with a great idea these days has like trust me you have access uh in that um there there's like unlimited money for good ideas currently um you know maybe that changes over time but like it's definitely there and I I would just say this you you know the world is changing and you can just think of it as like the jobs we had before the industrial revolution are all gone.

And then the and we've been kind of living with the postindustrial revolution and then the postcomputer age jobs um since then.

And we're going to get to like a whole another class of jobs and a whole another class of companies over the next 10 years um that replace most of what we have now.

And so if you're young, like that's the best thing possible uh for your career and for your life because in the opposite scenario where it's all the same companies, then you got to start at the bottom and work 30 years to get yourself to be a mid-level manager, you know, and you've got a politic and then you know the old people who aren't as smart as you like get all the money and like that sucks.

Um, but in this world it's the old people who have the challenge because they know how to do the old thing.

They don't know how to do the new thing and you can walk in and learn anything.

I I I think that you know the main thing is just like understand the future and then the future is yours is the way I would I I would think about it if I was you know 19 or 20 years old.

Well, you you said something pretty important there, which is it for the right ideas, there's unlimited capital, right?

Could you talk a little bit about what do you think is the shape of good ideas today that that's emerging in your mind? >> Well, look, I mean, I think that, you know, it always comes down to like can you build something um a product uh an organization, a culture, an offering that people want?

Um, and then if you don't build it, is it getting built by somebody else or did do they need you to do that?

Does the world need you to do that or or it doesn't exist is always the best entrepreneurial idea?

And so, anything that needs to exist that doesn't otherwise exist is a good idea. >> Uh, and look, that was the whole story with a venture capital firm.

Now, did the world need another venture capital firm? generically.

No.

Did it need a different kind of venture capital firm?

Absolutely it did.

Um, and so that's what we built.

Now, I think that's kind of true for I mean, if you look at Open AI, they weren't the only ones trying to do AI, right?

Like Google like was it was assumed like Google was just going to own AI.

Um, and it was panicking everybody.

And that's why Elon uh, by the way, co-founded it with Sam.

Um, and Elon's still mad about like what Sam did with it, but that's a different longer story.

Uh, but you know, it was one of those things.

Well, we need an AI, we need an alternative, the world needs this alternative to Google and you know that becomes a really really good idea. >> Uh, so anything and look the world the world is changing so fast that the needs are going to the new needs are going to multiply.

There's going to be many many many things that need to be done.

I mean, if you look at um I think you know kind of the old nobody the one thing that's interesting about the SAS apocalypse is it's definitely true that like the barrier to entry on like building software and user interfaces is is getting much smaller.

But by the same token, like kind of the most boring thing in the world is to just like rebuild Salesforce like >> you know no like Salesforce at a half the cost or a quarter of the cost isn't nearly as interesting as like what do you really want for your sales organization because it's not that I mean I don't think you know and then the question is can you build it before they can but um do you really want your sales people like entering data and like a crappy user interface and and then you know most of the things that they work on aren't captured in the system and this and that and the other like so you know going to the future figuring out what like in a world of AI like what what does that look like >> you know one of the traps that um that students often fall into >> Yeah. is I I call it the uh the dorm room problem, right?

Which is you you've got sort of direct visibility into problems. >> Yeah. >> That are in your kind of sort of cone of the light cone, so to speak, of of your visibility, which is quite narrow when you're still a student, right? >> Yeah.

And sometimes like when your friends are high in the dorm room and you have that conversation that sounds really good, it's not actually that good. >> They should at least sleep for one night. >> Yeah.

I've seen a lot of those over the years, right?

Um >> yeah.

Yeah. make sure it's it sinks in and you still think it's a good idea >> at least one night.

Yeah. >> Um but you know this the the as you know this this just because you're a student in a dormant doesn't mean you don't want to have an impact on big problems and and and and work on things that >> have an impact at scale right and sometimes these things are mission critical things healthcare financial services the economy enterprise the excelling to enterprises but these things are not directly in your sort of line of sight right when you're very young um and and how would you advise folks to in in particular as to bring it back to these AI systems.

You know, the context feedback loop we've talked about is quite critical, but getting access to those context feedback loops when they can make a huge difference is is challenging when you're young in your career and you don't have a big network and so on.

So, how how would you go about bootstrapping that problem? >> Yeah.

Look, I think the the main thing is to just solve a problem and and what tends to happen is when you go to solve a problem, particularly if it's a hard problem, you find some other problem that's more important.

I mean, and this is well known in scientific discovery, right? like penicellin was like an accident.

They weren't trying to solve that one.

It just kind of rolled off of the side.

And then by the way, like um Meta was an accident.

He was building Hotter Nut.

And you know, he kind of stumbled into like this much bigger idea.

Uh, and you know, my friend Drew at uh, Dropbox, um, you know, he was like literally tired of having USB where he'd have to move his presentation from one thing to another.

Um, he was just solving a problem for himself.

So, I think the best way to come on a good a really important idea is to go try and solve something.

Not necessarily build a company, just try and solve a problem.

Um, and then in that problem, if it's like a problem that you have, then that that means it's probably real.

And then in solving it, you'll probably or you'll likely find something much bigger.

Uh, and then that may like kind of force you to build the company.

And those are the things that work the best that we've seen are are are these big things.

I mean, it's really hard to um and even like Elon Musk didn't start his career trying to build Tesla, right? he he was solving a much smaller problem.

Uh and you know that's that that's generally how you how you build up to that.

I think trying to swallow the earth from the beginning with no experience is a doesn't usually work.

It's good for your pitch deck but it's it's not good for your company. >> Uh I think Elon's first attempt was like a class yellow pages competitor. >> Yeah.

Yeah.

Yeah.

Yeah.

Exactly. a little bit more mundane. >> Yeah, yellow pages and then PayPal and then you know Tesla and SpaceX. >> Well, so on that point, you know, the the time horizon on which sometimes you find entrepreneurs um sort of have an impact on humanity is that is quite long, right? they bootstrap sort of the impact the I would say or let me put this one of the old ways we've seen the generation of entrepreneurs of that belong to Elon's generation is that they feel like they have to start you know somewhat with a narrow scope >> and then bootstrap like bigger and bigger scope with every successive project >> but just a few minutes earlier you said actually you know things are going through a lot of change >> you can have a lot of impact very quickly >> relative to incumbents who may have had to be a little bit more measured in their approaches Right.

Yeah.

How you resolve these two? >> I I think it's I think thinking of it like how big a thing am I going to do is the wrong way to think about it. >> You have to start with like what problem can I solve? >> Um and then you solve if you can solve that problem um that's where to start like you have to size it to you.

Not everybody is the same.

Um like different people have different capabilities. you you become kind of your full like uh most effective self at a different age.

Like some people are really good when they by the way like Zuck is way different now than he was when he was 20 years old.

Like I knew when he was 20 years old like he was it's a miracle if he didn't have a network effect business like that wouldn't have worked at all.

He just wasn't very good. um you know but he developed that like entirely over the year and because he had that kind of business that had a vertical takeoff he could develop into that uh and like so if he didn't have that like he might have been better off you know finishing Harvard or whatever >> you know that was just one of those things where he happened to solve a problem at that age that was important enough that it created a company.

So I I I want to take it in a slightly different direction which is it or or analogous which is you know when Zuck >> when Facebook was getting started it had a very unique culture. >> Mhm. >> And and >> some good some bad. >> Yes.

And and and and it's not always clear what is good and what's bad until much later. >> I think my friend Sean got in trouble with the law with that culture.

But yeah. [gasps] >> Wait, did he get in trouble for Napster?

Wasn't that one culture earlier? >> He got tr No, he got in trouble at uh Facebook also. >> Facebook as well.

Okay.

There's a different problem with the law at Facebook. >> I see.

Yeah.

He's a generally tends to get into trouble a lot.

But my you know >> he is a genius.

So >> well this this is the thing right with genius sort of where you often find outlier technical andor any kind of outlier capability often you find one of the problems I'm discovering today right in in the field is that you often have really talented teams try to start a new lab or a new company >> and sometimes they fall apart. you just don't get very far from the outside.

You'd be like, "Oh, this is totally going to succeed." Star entrepreneur, lots of capital, you know, great problem.

And then like 6 months in to 12 months in, teams are just struggling a lot to make progress, you know, and sometimes people leave.

They they got to why is that?

You know, what do you think is it is about the right cultural initialization that sets apart teams that can do this and hit that takeoff versus stumble along and how do you skip the painful parts? >> Yeah.

So, so, so I think there's a few things like f first of all, building a company is hard.

Um, and no matter what era or whatever, like the press always makes it seem easy uh because they hate entrepreneurs, but it's not easy.

It's always extremely hard.

So, some are going to fail.

Like, I just say that upfront.

Um but in terms of like the the team and the dynamic and so forth, yeah, it's a combination of leadership and culture and culture is a a very kind of amorphous thing.

Um but it ends up being very important.

So basically the way to think about it is it's not like people think of culture as like you know corporate values or some bull um but it's not that uh you know it's not we have integrity um we have each other's backs or like like some of these like whatever platitudes people say it's like how do we behave exactly like what are the behaviors?

Um the samurai have a great kind of line which is a culture is not a set of beliefs, it's a set of actions.

And so what do we mean by behaviors?

Well, like do we come to the office or not?

Do we like do we go home at 5 or do we stay longer?

Do we if somebody asks me a question, do I get back to them like instantly or in a week? um you know like all those kinds of things end up mattering like do we believe the best idea wins or does it like matter who was the founder? um you know all all that stuff you kind of have to agree on as a team and like very specifically not like just like some high fluting idea and then you have to live by it. >> And then if you have that if you have a standard if you have a cultural standard then if somebody's not living up to that standard that's a simple thing.

If you have no standard uh and people aren't living up the way you want them to, then you're pissed and then but then that just starts infighting.

Then it gets political, right?

Cuz it's like, well, why is he going home?

Well, we never said he needed to be here.

We never agreed on that.

Like he, you know, has a date or whatever.

Um or like, you know, he's got a family, he's got to go home.

Like we never like said what that was.

Uh and then, you know, people stop liking each other.

And then you hit the first hard issue and it's like, you know, f it, I'm out.

Open AAI is going to pay me a lot of money.

Screw you guys.

Screw you guys.

I'm going home as Cartman would say.

Uh so but but what happens if you you started by standardizing on some set of beliefs, set of actions. >> Yeah. >> And then the world changes, >> right?

And what you thought was going to be the right standard six months ago in a world where stuff changes so fast needs to be updated. >> Yeah.

Yeah.

Like cultures can evolve like um but you know you kind of have to evolve together and and you need a leader.

You you need like having this is why I hate the idea of like co-CEOs or like we're all equal or like we're going to run a communist organization.

It doesn't actually work in a company.

Um because you need somebody who's going to break the tie.

Okay.

Yeah.

You want it to be that way.

You want it to be that way.

We're going this way. if you don't like it out like that's that's how you have to run an organization in order for it to succeed and um I think people are you know we culturally got away from that idea in Silicon Valley a little bit um you know in the end of the fat happy network effect era but like it's back now so >> could you say more what do you mean by that >> well you know every everybody wanted like a vote on what the company's values were and this and that and you know And then like CEOs cave to that and that that ended up not working well for any >> right companies are not democracies.

They are they're >> Yeah.

Well, I think a dictatorship always beats a democracy in a competitive battle and so because it takes a long time to to decide things in a democracy.

Now look for a country it's different. you know, there there are things when you have to last several hundred years that, you know, when um no matter how good the the uh the monarch is, um if they die and a worse monarch comes into play, that could be an issue.

Well, I'm going to push a little bit on this assumption that it's different for countries versus companies because something I've learned from you is the way you approach, >> you know, the most exciting the businesses I look up to the most, especially the ones in the A16 portfolio are often with leaders who are thinking so long term, the way they talk about the their impact on humanity is not that different from the time scale sometimes of political leaders.

In fact, arguably some of the entrepreneurs you are are thinking longer term than political leaders these days. >> Well, it is longer term, but um so like if you have a king, let's say you had a king running the United States, >> right? >> If it's a great king who was um not interested in their own like enrichment or their family or their friends and so forth.

That works like >> who cared about the public benefit.

Basically, >> who cares about the public benefit?

We think, you know, that works better than our current system. >> The problem with it is as soon as you get somebody who's not like that, that's just too much power. >> So, you're better off decentralizing power so that the system is resistant to bad leadership.

Like I think a country has to be resilient to bad leadership in that look if a company goes away like okay fine whatever like so you know the well Dave Packard and Bill Hulet you know like they're gone they passed away the new leaders weren't so good like that's the end of the company fine whatever it's a company >> they did their thing they did their job they fulfilled their mission you know a country has to persist beyond that.

And so I like I think we already see that you know here be it like you you know on the nation level on the state level on you know even on the city level you can see like eventually you get politicians who just start giving stuff to their friends and then like everybody suffers.

At least you can vote them out.

At least you can do something.

Whereas, you know, I think in a company, um, you want to be as efficient as possible while, you know, while the sun is shining. >> Um, I know I could keep going forever, but we probably have a bunch of questions piling up.

So, um, I'm going to ask you one more question, then we're going to switch to students.

Yeah.

Which is, >> you know, there you talked about David Swenson, right? and he had some strong assumptions that then you felt these were leaders of the previous generation that you felt just didn't get it. >> Well, I I I just think that you know, not that he like by the way Yale is still like an investor in us today.

Um so I just think like you can't let your investor by the way including us like run your company because you're on the [snorts] ground in real time seeing what's happening. they have knowledge of the past um and they have a light knowledge of what you're doing but not full context.

So they can be like it's an interesting conversation but you know the investor can't run the company and that that's just the way it works with him and us.

Yeah.

Well, so I'm my question for you is what prior do you feel like you now have to update so that you know given that you you felt like Yale at that time needed to update their prior faster today, what do you feel is like the biggest assumption that you've changed about the venture capital industry um that maybe was a strong belief you held you know 10 years ago?

Well, I mean, like I said, I I I think uh well, one, I mean, there's so many things that are changing, but you know, and I I I talked about like you can throw money at the problem.

That's a massive change.

Um I think that uh you know, the bottlenecks have moved.

So, you know, we used to have a bottleneck on software engineers.

I think like you we've got bottlenecks on like things like electricity now.

So, I think that right that changes how we think about investment.

And then you know companies are so big in the private markets that um they now require things that venture capital firms didn't you know previously provide like so when you get up to you know a billion dollars in revenue then you have to be like multi-country multi- channelannel multi-roduct you know these capabilities uh most VCs just have never had >> right >> um but I think now we have to have them and then I think the you know the private capital markets aren't quite don't have all the functions of the of the public markets so you know that needs to be addressed so there's a lot of things that that are changing this is definitely not new question it's a followup to that which is you said a culture is a set of actions right this was by the way this is a on the wall at 816Z and I every day I would go to you know the office in San Francisco and I'd rent one of these we could we could all book our own offices and the one that was my favorite was in the back corner and you're closest to the bathroom cuz I could dash to the bathroom between meetings.

But in that corner, it says, you know, from the Bushidto, you know, culture set of actions, not just beliefs.

Yeah.

And look, I tell people when they come in, like, I don't care what you think.

I don't care how you feel.

I don't care what's in your heart.

I just care what you do and like what you do matters.

And that and that's the way you have to run an organization or like you get into this. >> So, so I mean that's my followup is a culture is often also what you don't do, >> what you say no to, right?

Yeah.

What are the things that you've had to say no to because you're like, "Well, that's just not that that could be an interesting opportunity.

It might have even helped an entrepreneur out, but that's just not in our mission.

That's not that's not us." Yeah.

Well, so I just give you one example.

So, the biggest one that um got proposed to me like 18 times was well, with AI, AI is like um is very much like when the spreadsheet happened that kind of launched private equity, right? because all of a sudden you could go in and make all these big companies much more efficient by like having them adopt this new technology and a AI even more so, right?

You can go in and you can go into an old company and you can make it much more efficient with AI.

Um, and there's like many uh VCs who are kind of going with that idea.

And for me like there's uh I would say two big reasons I didn't want to do it.

One is it's culturally the opposite of venture capital.

So um >> like leverage bios basically. >> Yeah.

LBOS.

So like look venture capital is about investing in entrepreneurs with new ideas and focusing on how they can grow fast.

Um leverage buyouts are about you know entry price making it more efficient firing people.

Um and I I don't really want to grow it.

I just want to make more money out of what it is.

Uh >> and so like if you're in the venture capital mindset, you're looking for the great entrepreneur to um go build something amazing.

If you're in the leverage buyout market, you're caring about like, okay, I'm going to bring in a professional.

I'm going to have them run this more efficiently and so forth.

So it's the opposite motion.

And so for for me, I was like, well, I don't want to split the culture that way.

Like I think that's a, you know, not going to be a good idea.

And then the other thing is like I don't want to do that with my life.

Like I have the opportunity to fund like the greatest new ideas that are going to push humanity forward or like that.

Like I'm not it's not stupid.

I think it's a good business.

Um but it's not a business for me. >> So sometimes you're saying it's okay to impose bottlenecks on your own growth because that's just not what >> Yeah.

You don't Yeah.

Look, you don't have to be in every business um just because there's money there. um you know you look I I I believe in like you you build a company to kind of do something larger than yourself and make the world a better place and then if you do that you will make money.

Um, but if you are in business just for making money, um, like that's not for me.

Like that's uh there are a lot of people who think that way.

Well, like and I'll let them do that, but like I think that great companies don't think like that to to me.

Like companies that you would want to be part of that I would want to be part of don't work that way.

And so, um, I'm not going to build that thing just because like, oh, there's money over there.

Let's go run to the money.

Yeah, >> we're going to switch to questions.

So, the way it's going to work is they've been putting their questions in Discord >> and they're all voting on each other's questions and the top ones that get voted by each other, they get they we'll go through them one by one.

First question, >> the question is, if I was a college student, where would I uh put my energy and effort and what do I think about encouraging people to drop out of college?

Um so like I think that if I was um in college now I would put a tremendous amount of I I I would view AI as like a very powerful tool set.

So almost think of it like I think the best analog is electricity.

So, like, okay, if you knew electricity was coming, um, and you wanted to do something interesting in life and you were in the pre-elect electricity world, right?

Like, you know, where like it's 6:00, we got to be at home because it's going to get dark.

We're not going anywhere.

Like that world >> sounds like San Francisco. [laughter] >> Yeah.

Well, yes.

Um, you know, so, so then, okay, this whole new world is coming. let me really understand this technology and then like what is interesting to me in the world and that could be biology, it could be material science, it could be, you know, rocketry, it could be anything, but like you want to have those tools in your bag um when you go do that or it could be, you know, like by the way, it could be in the creative field.

So, you know, people uh I think misunderstand what's about to happen in in the creative world, but like somebody who used to be like who in my era would have been like a pretty good guitar player can now make a sci-fi motion picture score and everything by himself and like like this.

So, so like the world is really really different.

So, I I would definitely kind of figure out what I'm interested and then master this new tool set and kind of apply it together.

I think that's that that's probably the the, you know, the thing that's definitely going to work.

In terms of dropping out of school, like I I I think that this is very individualbased.

So, um, look, you you'd mature at at different points in life, you know, like I I think that, uh, I finished college myself and that was good for me.

Like I think, you know, it was good for Zuck to drop out given the idea he had um, and given the kind of company he was able to build.

And you know, so I think that with career advice, uh, let me just say this that nobody can give you good career advice, they can give them good career advice.

So I can give you good advice for me.

They can't give you good advice for you.

And particularly your friends are going to give you good advice for them, not for you. >> Uh, and so don't listen to your friends.

Uh, and you know, figure out who you are and you know what the best path for you is.

I would just say on that.

Yeah.

So, by the way, so just on political donations, I also donated $5 million to the Kla Harris campaign.

Um, >> important fact. >> Yeah.

Often not report on >> just just Well, it is reported on on Twitter every time the MAGA people get mad at me.

Um, like on politics, our let me kind of just tell you where that came from and how I'm thinking about it. uh in general um tech had like very little voice in Washington DC and that had extremely severe negative consequences for tech um and uh specifically so I can go through a few things in the Biden administration. one is they uh basically almost ended the crypto industry by uh enforcing things that weren't even in the law um to shut down companies and then uh they were like the same thing was happening with AI.

So the last Biden administration executive order um was uh to require for all sales of GPUs worldwide that they any time you sold one you'd first need government approval US government approval.

So that would have basically taken us out of the AI race entirely.

And the issue behind that was um was basically uh that we had no voice like that the whole industry had no voice in Washington.

So we kind of launched a very very big effort to have a voice in in Washington and I would say that um it's worked very well like so we have much better AI policy, much better energy policy and much better um crypto policy now than we did before we got involved.

So I'd say I'm like very happy about that.

And then all the kind of money and conversations have been about that.

Look, I mean, the other thing is, like I said, I gave money to Kama because I know her.

I've known her for 15 years.

She's been to my house 17 times.

My wife sat next to her in church the whole time.

So, I knew her, so I knew I could talk to her.

Biden, like we never uh could get a meeting with Biden for the whole time he was in office.

And if you speak to Tim Cook or Sundar Pchai or Dave Ricks who runs Eli Lilly, none of them got a meeting with him in four years.

Now we all know why now, but at the time we didn't know.

And the result of that was like tech had no voice in Washington for those times.

So I guess the answer is yes.

I'm happy with that. [laughter] Oh, here we go, man.

That's a good question.

So [laughter] the the question to to repeat the question for the podcast is um how do I think uh being in a rap group in college kind of affected me and then can I rap for us now?

Um so the story of that was uh you know I I had a friend who uh who got shot in the face and and became blind and so we started a and he was very very depressed.

So I would send him rap music and in those days rap had just kind of gotten started.

Um and that kind of cheered him up over time.

So we started a rap group called the Blind and Deaf Crew, DEF.

Uh and uh and we became a group and I wrote some rhymes.

Um so like one of the rhymes was the blind deaf crew you know where fly three of us but we got four eyes.

No he got his >> All right. [applause] Thank you. >> There are so many very memorable and intriguing pitches.

Um well, one of the most memorable was actually data bricks because it was so bad.

Um so the the pitch was that the Jan Stoka who is a professor at Berkeley presented the company and the slides he made it was like going to like a computer science lecture that you couldn't understand um in in college that that's what it that David Rick's uh pitch felt like.

So that was very memor it was memorable because of that and then it was memorable uh because of what it turned into.

Um but uh >> well why' you invest?

If you couldn't make sense of it, why'd you invest? >> Well, the the whole reason I had him come into pitch is cuz Scott Shanker, who was another professor at Berkeley who I knew, had called me and said, "Ben, I have the best distributed systems guy that we've seen in the last 10 years in academia.

Um his name is Mate Saharius.

Um you know, do you want to meet him?" And >> I knew as soon as he said that to me, I was going to invest in the company.

Yeah.

Yeah.

But that that pitch kind of scared my partners. >> Oh, thank God they didn't talk you out of it. >> Yeah.

Yeah.

Yeah. >> Yes. [laughter] It's funny.

Um so, so the question is about Clue and uh you know what do I think about it now and in terms of momentum and this and that and the other.

Look, I think that an easier way to think about it is we invest in founders.

Um, and you know, you want founders who are original thinkers and have kind of breakthrough thinking on on whatever it is they're working on.

And I think those guys, you know, had a bunch of breakthrough ideas, uh, including marketing.

Like I think, you know, they are kind of marketing geniuses in a sense.

I mean, that like you know about them.

They're not, you know, they're they're not the biggest company in the world, but they're the one that said, you know, about there's something to that. [gasps] So, you know, what it becomes um from here and and where it goes, we'll see.

But like I I say, you know, these things are early and the there's only one unforgivable sin in business.

Um and that's running out of money.

And until you've run out of money, like I don't count any of these companies out, by the way.

Like I I've seen >> like Slack was in dire straits. um before he figured it out, you know, he had built a game on Flash called Glitch.

Um and Steve Jobs outlawed Flash on the iPad and it was an iPad game and like that's how dead he was.

Uh you know, and he had like $6 million left and he turned it into Slack.

But that's Steuart Butterfield.

You know, he's a great entrepreneur. >> Um so like companies go through changes and this and that if you've, you know, like if you're a special founder and you don't run out of cash, I'm still for that. and would bet on that question is you know given the SAS apocalypse and given that we have a long time horizon how do you think about like how can you invest in anything because anthropic is just going to oneshot it all this is the Wall Street view by the way anytime Wall Street thinks one thing and Silicon Valley thinks another thing that arbitrage is worth a lot of money and Wall Street's always wrong um so I I think there's actually a lot of opportunity now in that in that case look I um you know for some of these things are you know the whole moat is the the code and the UI and I think that's a difficult position to be in right now for sure um but there's a lot of one like most of the new companies like nobody's coming in with like new SAS companies um at this point like people kind of know like okay that's not that defensible like you know you can build it and so forth.

So that's not the the new idea.

So then if you go to the old ones and you go well you know are they all dead uh like Wall Street thinks I think you know not really.

So like for I'll just give you one example of a company that I'm on the board of.

So I'm on the board of a company called Nanton.

And Non is like a software travel agency um for businesses.

So you know in a company your biggest kind of variable expense is travel.

So you need to have like very tight policies around it and so forth.

And then to build a travel company, um you actually need to have supply chain relationships with not every airline in the United States, but every airline in the world, every hotel in the world.

And like if you scrape their websites and do that kind of thing, they literally cut you off.

They send you a cease and desist and they sue you and like you're out of business instantly.

Um, so it's not that hard to build all those global supply chain uh relationships and then you can't sell to any significant company that travels worldwide if you don't have all of them because like I need to be able to travel everywhere.

Uh, and then you've got to like integrate with all their whatever they're doing for their, you know, uh, cruddy other systems in their in their company. and then the channel to sell it.

Um, you're actually selling to somebody called the travel manager, which by the way, like Anthropic is like the I the chance that Anthropic would build a channel to sell to the travel manager when like there's gold bricks everywhere.

They're not going to pick up a silver brick.

Like they're just not going to do it.

Like I I can tell you an can tell you like that's the last thing on their mind.

In fact, they've got an open wreck now to hire a travel manager at Anthropic to manage the Navan relationship.

Nonetheless, like I think they'll be fine for a very long time.

Uh so, you know, it's just one of those things where uh and there's a saying on Wall Street when the patty wagon backs up to the house of illreute, everybody goes to jail, you know, not just the people who are committing crimes.

And so, in the SAS apocalypse, everybody's in jail whether or not they should be in jail.

So like you just just be aware. >> What do you think it's going to take for the markets to realize that >> time it's just time um >> and education I guess they got >> Yeah.

Well and you learn Paul it's so the way Wall Street works is an uh Warren Buffett always says you know in the short term it's a voting machine the long term it's a weighing machine.

Well why is that?

Well the reason is it's a narrative but they buy the narrative.

They don't buy the facts, they buy the narrative.

So the story, if the story is this is a victim of the SAS apocalypse, barring any new results from that, that's going to be a winning story because it's like such a good story.

And by the way, all the portfolio managers who own SAS companies got fired.

So like nobody wants to jump into that, you know, kind of thing if you got the new job.

And so that story is going to hold for a while.

But eventually when the quarters come in, the weighing machine will go, "Well, maybe that narrative wasn't right for that company because why are they making so much damn money if they're a victim of, you know, if Anthropics can oneshot them?" Like, that doesn't make any sense.

Don't the customers know the oneshot is coming?

Um, and so then the narrative will change and a new narrative will win and that then it becomes a a weighing machine.

And that that's true for, by the way, every company.

What start advice is super overrated today? >> I don't know what advice P that that's a good question.

I'm not sure like what kind of advice are you getting what I get I mean look I I I think you you have to pay much more attention like I think the thing that is true is like you can't ignore AI.

I I remember kind of um before the internet came uh which I was also alive for.

Um you know there were a lot of tech companies um and anyone that ignored the internet was just gone.

Like you you can't ignore a change that big.

Like there's no way that something that worked before AI can ignore AI and survive.

So like that part is true.

And so if you're starting a company and you're not dealing with not only AI today, but what's likely to happen, you know, as the models get bigger and so forth, like it's just not going to be a very interesting company.

So that that part of advice is is very correct.

Um I think the the part of the advice that's wrong is there aren't going to be any employees and there's going to, you know, companies aren't going to hire people and it's just going to be AI bots running everything.

Like by the way like all the data kind of is going in the opposite direction of that.

Like even like software engineering jobs are growing like very fast despite what Daario says.

And by the way they're growing very fast at anthropic.

Um so it's like you know at what point do you call like uh on that idea?

Uh so >> I think sometimes things get taken out of context right like with with the with the political donation question like what was missing context was that your donations to both sides.

I think what one of the things that gets taken out of context with Dario is he's often saying hey during the transition some types of jobs that are low skill will get those will go away and those people will then have to you know take new jobs. >> Yeah.

So there will be a job so Dario is very right on that there will be a job change.

So not the advice Dario gives but how he gets written up.

Right. >> Exactly.

It's the >> Yeah. >> tweets.

It's the tweets.

The tweets are the problem. >> Yeah.

So, so those tweets um turn out to be uh I I would just say like like very overblown and not kind of representative of what's likely going to happen.

Uh so, you know, don't and in general like the the doom and gloom.

Um I I just think that's overstated, you know, a lot on uh AI.

The most, by the way, the the most dangerous thing I think on AI by far is that we kind of fail as a country.

We get too scared.

We overregulate.

We do what Bernie Sanders recommends that some of you are Bernie Sanders fans, but like we put a moratorium on data centers and then China wins.

And um like I think a world where by the way either China has like super intelligence and we don't or we have it and they don't is a much more dangerous world than having some kind of balance to the power.

Uh you know concentrations of power historically have been the worst thing for humanity and so I think that that would be the thing to be scared of.

So I think the fear uh could cause actually a worse problem than what people fear. >> Well, here at AI Coachella, we are rational optimists.

All right. [laughter] So, thank you for coming to AI Coachella, man. >> All right.

Thank you.
