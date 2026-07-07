---
source: "https://martinfowler.com/fragments/2026-07-06.html"
title: "Fragments: July 6"
author: "Martin Fowler"
date_published: "2026-07-06"
date_clipped: "2026-07-07"
category: "Software Architecture"
source_type: "web"
---

# Fragments: July 6

Source: https://martinfowler.com/fragments/2026-07-06.html

# Fragments: July 6

Last week, Thoughtworks ran a second Future of Software Development Retreat, this time in Europe. As with the previous event, Iâll be sharing some fragmentary thoughts on this. There were five parallel streams, so I could, at best, only attend â of sessions. This isnât an event that forms conclusions, rather one that allows those exploring to share what theyâve found, and their visions for the future. The bliki post lists all the writing Iâve run into on this, by myself and others. Iâll be updating it as more posts appear.

Giles Edwards-Alexander ânoticed a real difference between the retreatsâ:

Where Deer Valley had hesitancy and a belief that there was something here even if we werenât yet sure what it was, Engelberg had confidence: the value is here. As I explained to a colleague today, this was not a conference for true believers: the evidence is in.

What does the evidence say? Well, that was less clear. Some patterns and practices are emerging (one attendee had catalogued dozens of agentic engineering pattern libraries) but they are emerging. There is more work to do to truly establish what is effective, and when.


Greg Herlein felt similarly:

Reading the reports of the February event, when a lot of these same folks last got together, the conversation was about what agentic development might look like. Aspirational. More about what was coming.

This time? Everybody in the room was doing it. Shipping it. Not slides - production. The whole debate about whether this changes software engineering is over. People have stopped arguing about whether a while ago. Theyâre arguing about how, and the how is getting real.


On a more micro level, I noted two other things. Firstly, there was much talk now about harness engineering, when that wasnât even a term in Utah - an example of how rapidly things are moving. Secondly people are now worrying about the cost of tokens, where before folks were wanting to do almost anything to incentivize people to talk to The Genie.

Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â â

A question that continued from Utah was whether architecture and design are still important. There seems to be two landmark hypotheses here, one is that The Genie has such a Galaxy Brain that we no longer need to care about such matters, it will handle as much spaghetti as we can throw at it. The other is, in Laura Tachoâs memorable phrase: âthe Venn Diagram of Developer Experience and Agent Experience is a circleâ. The point being that The Genie uses the same constructs to understand a code base that humans do, so things like good modularity and naming help it as much as it helps humans. Adam Tornhillâs writing is a good example of this viewpoint.

Tidbits from our session on this:

- to evaluate the value of architecture we need to focus on desirable outcomes. Internal design quality boils down to ease of change. The question is whether the lessons weâve learned so far will continue for agents.
- a way to measure design quality is to look at token costs. If the same change requires less tokens that indicates a better architecture.
- a good architecture only shows its quality over time, we canât easily measure it in the short term
- why did 3GL languages continue when things like 4GLs, UML etc not take hold? Itâs because these programming languages hit a sweet spot of human comprehension of computation
- weâre at the first time ever where the computers care about code quality
- will future models write machine code directly? If so what will humans review or specify?
- we should beware of speculating about what LLMs may do in the future. Instead we need mechanical sympathy for our LLMs, so we can gain a sense of how they work and how best to use them.
- One workflow:
- take story from backlog
- talk it over with an agent
- once get an agreement, make an ADR for persistent record of spec
- generate a task list
- get agent to complete it

- we need abstractions to communicate with agents
*(echoing Unmesh Joshiâs thoughts on building conceptual models)* - we often find duplication in LLM generated code, together with mixing of concerns (eg intermingled domain and display logic) - even with a good harness
- get agents to generate explanatory documentation at the end of a session
- overnight quality checks with a report for humans to act on in the morning
- LLMs look at existing code, so if that code has problems, the LLM will amplify them
- we should be wary of drawing too many conclusions comparing LLM code with human code - human code varies enormously from team to team.

Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â â

In his account of the retreat, Mathias Verraes goes into the details of his perspective of these issues of software design. He adds another concern: we need good design as a hedge against the risk of dependence on AI. After all, we donât know how high the costs may rise to. We see governments blocking access to models. We see popular opposition to AI campaigning against data centers and calling for regulation. How much can we rely on AI tools being available to maintain and extend our software in the future?

Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â â

Charity Majors has a post on the ethics of working with AI and does an excellent job of articulating how I feel about this topic. She outlines the harms inherent in AI, both in the creation of its models (training on stolen data) and in inference (slop, lack of accountability, skill atrophy). Her conclusion however, like mine, is that thereâs no ethical gain from renouncing the use of AI and castigating those who use it. Such purity provides little practical help with a technology that is so powerful and so useful.

The way you show care is by showing up. The way you make the world a better place is by getting down in the muck and building it, using whatever skills and resources you have on hand. The way you drive change is you engage.

Yes, we are all complicit. Yes, we are all compromised. No argument. But what are you going to do with that feeling of conviction? Will you channel your discomfort into solidarity and action, or try to ease your conscience by removing yourself from the system? Which does more to help those being harmed?


Her suggestions on how to engage arenât striking, but thatâs hardly unusual. At the Future of Software Development Retreat I convened a session on this question, and nothing striking turned up there either. That said, Iâve never been much of an activist, so my imagination may be limited.

Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â â

Gergely Orosz has run into a case where an article of his was erased from Google search by a clearly fraudulent DMCA claim.

It seems that anyone can file a bogus copyright claim to get an article they donât like removed from Googleâs search index. This happened in this case. I have no information on who filed the copyright claim. Even less so on who claims to be the copyright owner? Because I am the only possible copyright owner!


He was able to find the DMCA complaint, it was made by âEllie Pieeâ whose profile listed them as living on Bouvet Island, an uninhabited Norwegian dependent territory near Antarctica. It claimed Gergelyâs article copied a New York Post article entitled âBand Leader Hits Winning Chordâ. But Gergelyâs article is âInside Pollenâs Collapse: â$200M Raisedâ but Staff Unpaidâ, and the two do not share a single sentence. Thereâs an obvious motivation for folks connected with Pollen to have done this, and I hope the resulting Streisand effect bites them where it hurts.

Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â â

404 media have a bunch of (paywalled) reports on the impact of companies realizing that token costs are getting out of control. Theyâve acquired leaked Slack chats, internal dashboards, emails and other material from companies including Citi and Amazon.

Companies are urging staff to use less powerful models, or cutting off frontier models entirely. A dashboard indicates that one company has seen its token bill rise from $5 million in August 2025 to $15 million in May 2026, on track to spend over $120 million in the fiscal year.

404 earlier reported about Accenture taking steps to reduce token usage. The biggest problem wasnât software engineering using agentic programming, but rather staff âchewing tokensâ by using AI to do things like turning PDFs into presentation slides. They saw themselves, and their clients, grappling with exponential increases in token costs. Inevitably, after consulting firms spent time urging their clients to use AI heavily, they are now offering services to control these costs.

Another post says it appears that one way to reduce token costs is to get AI tools to speak like cavemen, using a skill/plugin.

Thereâs a good summary of all this on 404âs freely available podcast: The AI Tokenpocalypse Is Here.

Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â âÂ Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â â

I share these thoughts just after the July 4th weekend here in America, indeed the Semiquincentennial. Historian Bret Devereaux celebrated this event with a careful reading of the Declaration of Independence, a document often talked about more than itâs read. Which is a shame since it is hardly very long, and its impact was remarkable, and not just in what is now the United States.

The Declaration of Independence was recognized as a radical, potentially explosive document at the time of its issuance, as weâll see. And it was explosive: the world of 1775 was one dominated by monarchies with just a tiny handful of traditional republics (which we should not ignore!). It took a long time for the seeds of the declaration to spread, but the world it helped create is one where liberal democracies, while hardly universal (more people have always lived in unfree societies than free ones) represent the most economically and culturally dominant bloc in world affairs â something that had never happened before. The Declaration, in its way, remade not just the Thirteen Colonies, but slowly, surely, as water seeps through the cracks of rocks (or my floorboards, alas), it remade the whole world.


Devereaux shines a light onto the world of this text, illuminating its historic context, a world that is very different to the one anyone reading this grew up in. Itâs assertions of a natural law that there is equality of rights among men and that governments ought to derive their powers from the consent of the governed would seem hardly worth stating now, yet were deeply radical in 1776. Iâve found that reading history like this has helped me understand how the world is, and gives me a broader perspective on the drama of current affairs.
