---
source: "https://martinfowler.com/fragments/2026-05-14.html"
title: "Fragments: May 14"
author: "Martin Fowler"
date_published: "2026-05-14T17:52:00-04:00"
date_clipped: "2026-05-18"
category: "Software Architecture"
source_type: "rss"
---

# Fragments: May 14

Source: https://martinfowler.com/fragments/2026-05-14.html

Fragments: May 14 
Martin Fowler: 14 May 2026 
Last week I spent a day at a retreat that brought together several people working in software development to talk about the profession’s future with the rise of agentic programming. The event was help under the Chatham House Rule , so I can’t attribute the comments and stories I heard. (If anyone recognizes themselves, and would like attribution, let me know.) Here are a few tidbits that caught my notebook.
❄                ❄
One group developed a behavioral clone of GNU Cobol compiler in Rust. The result is 70K lines of Rust and was built in 3 days. This is yet another sign of the ability of LLMs to do a good job of porting existing code to a new platform. Good regression tests are extremely valuable here (and I don’t know how good GNU Cobol’s are). There’s also the possibility of building a test suite if you have access an existing implementation.
❄                ❄
Large spec documents can be complex for a human to review. One attendee shared the idea of getting the LLM to interview a human expert, asking the human questions to verify the correctness of the specification, a form of Interrogatory LLM .
❄                ❄
Not specifically about AI - but I liked how one attendee commented that the first thing they do when consulting with an organization is to read the guidelines for their change-control board. This is the scar tissue of what’s gone wrong in the past. I’ve often said that to understand why a thing is the way it is, you need to understand the history of how it got there. This seems like an excellent way to tap into important parts of that history.
❄                ❄
My colleagues who work with modernizing legacy systems have long been rather sniffy about “Lift and Shift” - porting a legacy system to a new platform while retaining Feature Parity .
We see this pattern as a huge missed opportunity. Often the old systems have bloated over time, with many features unused by users (50% according to a 2014 Standish Group report) and business processes that have evolved over time. Replacing these features is a waste. Instead, try to muster the energy to take a step back and understand what users currently need, and prioritize these needs against business outcomes and metrics.
But this point of view was developed before LLM’s ability to port code appeared. One attendee who does a lot of work in this field said they believed that lifting and shifting to a new platform should now be always the first step in a legacy migration. The cost is no longer as formidable as it used to be, and a better environment makes further evolution much cheaper. Just don’t stop there.
❄                ❄
Several attendees were from the financial industry, and thus were immersed the problems of complex legacy environments coupled with regulatory controls and significant risk should software do something wrong with money. One of their issues is the complexity we run into when a financial product is offered in multiple jurisdictions, each with their own regulations to satisfy. There’s a lot of software complexity in deciding which jurisdiction applies, and picking the right set of rules at the right point of the workflow.
The question here is whether the rapidity of agentic programming means that we can build individual, simpler systems for each jurisdiction. We would then use LLMs to ensure consistency between them, so that as the product rules change, each system reflects that into its own environment.
A large part of software design is about identifying what is the same and what differs between various business contexts. Where things are the same, and need to be the same, we are rightly wary of duplicating code, since this increases the cost of updates the dangers of inconsistency. The interesting question is what role LLMs can play to give us new tools to tackle this.
❄                ❄
As is usually the case in gatherings like this, folks were concerned about junior developers. When we work with The Genie, our value comes from good judgment - how do we teach that? This group did have one common tool - Pair Programming . One of the key benefits of pairing has always been skills transfer, and here an experienced agentic programmer can pass on their judgment for software design and how to use the genie to get there. And the junior will often have a trick or two to share too - that fresh pair of eyes in particularly valuable in the shift to our agentic future.
❄                ❄
Historically, we use computer systems to bring order to chaotic human processes. Is AI reversing that?
❄                ❄
So much software is involved in data transformation. Those records over there need to be consumed by these APIs over here, but there are differences in how the data is structured, often due to being in different Bounded Contexts , so we have to do some conversion. Agents are particularly adept at writing this kind of transformation code, which is often more tedious than we’d like.
❄                ❄
Chaos Engineering has become a valuable technique to improve resiliency, made famous by Netflix’s Chaos Monkey that randomly breaks live services to see how well the ecosystem reacts and recovers. What would a Chaos Monkey for AI look like? Would it deliberately introduce hallucinations into a pipeline to see if sensors were able to catch them?
❄                ❄                ❄                ❄                ❄
Back at my desk
There’s been a bunch of questions about the article on Structured-Prompt-Driven Development (SPDD) that the authors answered in a Q&A section . One in particular caught my eye:
Have you considered having an agent do the prompt/spec review itself — not a human reviewing the Canvas, but an agent that reads the REASONS Canvas alongside the code diff and verifies alignment?
The reply talks about how there is an available command to do this, but there downsides. In particular one reason not to do this automatically is:
Letting humans learn. Review is also where humans learn from the AI’s choices — patterns, trade-offs, options they had not thought of. Cutting humans out speeds things up, but it blocks the long-term skill growth that SPDD is designed to protect. […] Once enough decision rules build up to give us real confidence, we may shift more of the review to the agent step by step — but the part where humans learn from the AI is something we plan to keep.
One of the ways we should judge the value of an AI tool is how much it helps us humans learn more about the world we inhabit and build.
❄                ❄                ❄                ❄                ❄
In some strange way I injured my elbow last week. No idea how, there was no event where I said “oh shit”. It just gradually started hurting and swelling. My life-long strategy to avoid sports injuries 1 had defied me. I applied ice and ibuprofin, the swelling went down, but my range of motion got worse. I’m glad I learned to use a knife and fork in English childhood, so I normally eat with my left hand.
I noticed that that loss of range of motion occurred after I got home, when I started spending all day at the computer again. I might not use my elbow directly, but my right hand does a lot of typing and mousing. My desk set up is pretty ergonomic, with a good keyboard , a wrist rest for the mouse, and arm rests on my chair. But even so, did my computer use make my elbow get worse once I got home? I can’t imagine not using the computer, for me writing has become an unstoppable habit. But maybe I should use this opportunity to explore voice input - after all most people can speak faster than they can type.
I tried this many years ago, when a colleague told me how good voice recognition was once it trained to you. I tried it, and indeed the voice recognition, even in those pre-AI days, was very good. But it didn’t work for me. When I’m writing I rapidly type words into Emacs, but almost immediately I go back to edit them. Write two sentences, edit them, write another, re-edit the paragraph. The back-and-forth between seeing my words and thinking about them is tight - I can’t just dictate my words.
That made me reflect further. I only started using a computer for my writing in my 20s. At school I had to write longhand, and in university to type on typewriter. But those media don’t support the constant rewriting that I do now. Would I even have become a writer had the text editor not been invented?
❄                ❄                ❄                ❄                ❄
James Pritchard thinks that many developers are over-using agents at run-time in their products, when LLMs are better used as functions .
The problem with agents isn’t that they don’t work. It’s that they work unpredictably. You trade a known execution path for “autonomy” that mostly means “I don’t know what it’s going to do.” When an agent-powered feature breaks in production, you’re debugging a conversation transcript, not a stack trace.
Most “agent” use cases are actually workflows, a known sequence of steps where one or two of those steps happen to involve an LLM. You don’t need autonomy for that. You need a function call.
He points out that functions compose predictably, so if you know the workflow, then composing in a program text is better than agents figuring out how to coordinate themselves. It’s faster, and needs less tokens. It’s usually easier to deal with failures, since the scope of the interaction is smaller.
❄                ❄                ❄                ❄                ❄
Pritchard also thinks that people use skills far more than they should . He thinks people accumulate folders of markdown skill files but LLMs use them inconsistently, often missing them when they’re needed, or bloating context when they are not. Many things that should go in skills should be other parts of a harness , preferably computational. Skills should only be used with deliberate, infrequent workflows.
The skills obsession is a symptom of a deeper pattern: people reaching for configuration when they should be reaching for architecture.
“The LLM doesn’t write good tests.” Don’t write a testing skill. Are your existing tests inconsistent? Is the test setup complex? Fix those things and it’ll write good tests without being told how. Point it at a test file you’re proud of. Code is clearer than English.
[…]
The best setup is one where you barely need to configure the LLM at all. A clean codebase with clear patterns, a short project config for the non-obvious stuff, hooks for automation, and maybe one or two skills for specific workflows you run intentionally. That’s it.
❄                ❄                ❄                ❄                ❄
An oft-stated point about the rise of agentic programming is that we have to start dealing with non-determinism in our work. Of course that’s somewhat of a simplification, because some aspects of software development have long had to face non-determinism. A notable example of this is distributed systems, and a notable figure in helping us probe the truly uncomfortable waters of distributed systems is Kyle Kingsbury (Aphyr).
Last month he dropped a long article (the pdf is 32 pages) on how he sees our LLM-enabled future. The title “ The Future of Everything is Lies, I Guess ” betrays his lack of enthusiasm for this future.
Some readers are undoubtedly upset that I have not devoted more space to the wonders of machine learning—how amazing LLMs are at code generation, how incredible it is that Suno can turn hummed melodies into polished songs. But this is not an article about how fast or convenient it is to drive a car. We all know cars are fast. I am trying to ask what will happen to the shape of cities.
It’s worth the long read, even if it isn’t terribly cheerful. Kingsbury brings up many of worries about AI’s growth from the perspective of someone who is clearly well-informed about their capabilities.
His view is that the best response to all this is that we should stop. He wants to avoid using AIs for his writing, software, or personal life. He thinks those working for the AI companies should quit. And yet he also knows that these tools are useful, and wants to use them.
I’m both a hoper and a doomer when it comes to our AI future. Fundamentally I see any powerful technology as a big bus: we are either on it, or get run over by it. I’m onboard the bus because I don’t think putting up some barriers would stop me being crushed by its wheels. Maybe if I’m on the bus I can join some people to influence the driver a bit. I’m also very reluctant to speculate on the future outcomes of anything, let alone something as powerful as this. Did the early industrialists in the late eighteenth century have any clue what the industrial revolution they unleashed would do? While it created many harms, it also created a massive rise in the living standards of millions of people, at least those whose countries were on the bus. AI may create benefits that I can’t really dream of, although I can glimpse it when it helps a friend stave off Parkinson’s disease. 
Those hopes are there, but Kingsbury’s article shines a light on the darker elements of the here-and-now, asking serious questions of responsibility
a part of my work as a moderator of a Mastodon instance is to respond to user reports, and occasionally those reports are for CSAM, and I am legally obligated to review and submit that content to the NCMEC. I do not want to see these images, and I really wish I could unsee them. On dark mornings, when I sit down at my computer and find a moderation report for AI-generated images of sexual assault, I sometimes wish that the engineers working at OpenAI etc. had to see these images too. Perhaps it would make them reflect on the technology they are ushering into the world, and how “alignment” is working out in practice.
Don’t do sports  ↩
