---
"source": "https://www.thoughtworks.com/insights/articles/quality-is-speed-AI-era"
"title": "Quality is speed: Where engineering discipline moves in the AI era"
"author": "Joe Murray"
"date_published": "2026-10-06"
"date_clipped": "2026-10-08"
"category": "Software Architecture"
"source_type": "rss"
---

# Quality is speed: Where engineering discipline moves in the AI era

A conversation with Martin Fowler

[Articles
Back](https://www.thoughtworks.com/insights/articles)

* [AI and ML](https://www.thoughtworks.com/machine-learning-artifical-intelligence)
* [Agile engineering practices](https://www.thoughtworks.com/insights/topic/agile-engineering-practices)
* [Article](https://www.thoughtworks.com/insights/articles)

By 

[Joe Murray](https://www.thoughtworks.com/profiles/service-line-leads/joe-murray)

Published: October 06, 2026 
| Last updated: October 06, 2026

In our work with clients, we see many organizations still operating on the old clock when it comes to software delivery: multi-year roadmaps, 12 to 18-month modernization programs, releases every quarter if you're lucky. That pace made sense when the tools, the market and the assumptions underneath a project stayed stable long enough to plan around them. They don't anymore.

AI is changing what's buildable and what “done” even means, often faster than a typical planning cycle can keep up with.

We’ve also seen teams treat the need to move faster as permission to loosen engineering discipline. That's the wrong trade. Engineering discipline shouldn't disappear in the face of speed; it should move: closer to where working software meets real conditions and where you can still change course without much cost.

That's the principle behind our new AI-native delivery framework, which we call 3/3/3. It gives teams three days to agree on the opportunity and shape a first move, three weeks to build a working prototype that proves it out and three months to get a production-ready minimum lovable product into the world.

It's not about speed for its own sake, but about reducing uncertainty in stages, testing value, usability, feasibility and viability before committing significant investment. The result is a way to deliver software with lower risk, at a pace most organizations can sustain.

That still leaves us with some hard questions. What does rigor look like as AI changes the way software is built? How do you experiment without mistaking activity for progress? And what can we learn from previous eras of technological change that could help us navigate this one?

**I sat down with Thoughtworks’ Chief Scientist, Martin Fowler, whose work has shaped modern software development, to dive into the answers.**

**Joe Murray: How would you characterize the parallels between what we're facing now and previous periods of technological shift? What wisdom can you share about what we should look out for as we evolve into this next way of building software?**

**Martin Fowler:** We haven't had enough experience with AI tools to have a solid idea of how to best use them yet, so we have to do a lot of experimenting and share our findings, knowing we are very much in a process of discovery.

I remember an [interview with Peter Steinberger](https://lexfridman.com/peter-steinberger-transcript), who built OpenClaw and recently joined OpenAI to work on personal AI agents. He said he only started using AI coding tools in mid-2025, and was struck by how, within a few months, they had evolved enough to change what he could realistically accomplish with them. The tools will continue to gain new capabilities, so we'll have to keep revisiting our assumptions.

### **Relocating discipline**

### 

**Joe: I want to drill into a [quote from software developer Chad Fowler](https://chadfowler.com/regenerative-software/3mbrvhyye4k2e/) that you recently highlighted: “The engineers who thrive in this environment will be the ones who relocate discipline rather than abandon it.” Can you unpack that and connect it to what we're facing now?**

**Martin:** Chad was referencing how [extreme programming](https://martinfowler.com/bliki/ExtremeProgramming.html) (XP) was initially viewed as chaotic because it discarded detailed upfront design and heavy project management ceremonies. But XP didn't abandon discipline; it shifted it toward automated testing and continuous integration.

In high-ceremony, waterfall approaches, you could spend months building unintegrated software without knowing whether it would actually work. That created an illusion of progress. Continuous integration was painful at first, but it forced teams to automate and provided a highly reliable, integrated picture of the software's reality. You monitored progress by looking at what the working software actually did, rather than relying on speculative status reports. It wasn't less rigorous; the rigor simply moved to places people weren't used to looking at.

Chad suggests the same thing will happen with AI. We are going to shift where our rigor applies, and a key point is that we want this discipline and control to be closer to reality, much like what XP achieved.

**Joe: That illusion of progress is what worries me most about AI. Output is now so cheap that activity is even easier to mistake for progress. That's the principle behind 3/3/3: every stage has to end in something real, not a plan. Does that discipline hold up, or are the specific numbers arbitrary?**

**Martin:** The specific numbers don't matter much, what matters is picking points where you're forced to stop and look at evidence. Three days is close enough that you can throw an idea away if it doesn't hold up, nobody's invested enough to be precious about it yet. Three months is long enough to have a minimum lovable product and get it into the world, with the capability to keep evolving it based on the signals that emerge. That timeline can shift depending on the project.



> "We are going to shift where our rigor applies, and a key point is that we want this discipline and control to be closer to reality, much like what extreme programming achieved."

Martin Fowler

Chief Scientist, Thoughtworks

> "We are going to shift where our rigor applies, and a key point is that we want this discipline and control to be closer to reality, much like what extreme programming achieved."

Martin Fowler

Chief Scientist, Thoughtworks

**Joe: On the other hand, there's a common fear among engineering leaders that faster delivery cycles, like 3/3/3, combined with coding agents, mean trading away quality for velocity. How do you respond to that?**

**Martin:** I would argue those aren't in conflict at all. Our long-held assumption is that higher internal software quality [enables you to go faster](https://martinfowler.com/articles/is-quality-worth-cost.html). If that weren't the case, we wouldn't bother with quality; our ultimate interest is rapidly and responsibly delivering value to customers. Quality is an enabler of speed. This is a crucial concept that many in the software world fail to articulate or understand.

The question now is whether that remains true in the world of AI. There are two schools of thought: one suggests LLMs are clever enough to understand and rapidly work with “spaghetti code”. The other argues that the same traits making high-quality software understandable to humans also allow AIs to understand it more quickly. Therefore, building high-quality software enables the AI to move faster as well.

While we don't know for certain which hypothesis will win out, pursuing the idea that quality helps both humans and AI is perfectly reasonable.

**Joe: We're betting on the second hypothesis ourselves. It's actually one of the premises behind Thoughtworks’ new agentic development platform, [AI/works™](https://www.thoughtworks.com/ai/works/). Instead of expecting AI to just push through messy code, it makes that code more structured and legible, giving AI a clearer basis for working with it. Across the engagements where we've used it, we're seeing teams modernize legacy systems 50 to 80% faster than their original estimates because of it.**

**Martin:** There's a good example of that. We recently worked with a manufacturer that needed to modernize a high-risk mainframe that ran a warranty platform, the kind of project that gets scoped for a year and a half because everyone's scared to touch it.

This one took about five months, and it's worth being clear about why. AI/works™ helped the team understand the legacy system before making changes, giving AI agents a clearer picture of what they were working with. They could also check the new version against how the old one actually behaved in production. The speed came from better context and feedback loops, not from doing less of the quality work.



### 

### 

### See how AI/works™ brings rigor into AI-first software delivery

[Explore](https://www.thoughtworks.com/ai)

### **Where the rigor sits with agents**

**Joe: I want to come back to something you mentioned earlier: [OpenClaw](https://www.thoughtworks.com/insights/blog/security/want-run-openclaw). We've been talking about relocating discipline in how we build software. What does that look like when we're working with AI agents, particularly as they move from assisting us to taking autonomous action? Where does the rigor need to sit?**

**Martin:** OpenClaw is a good example to look at. I wrote [a short piece about it](https://martinfowler.com/fragments/2026-02-23.html), mostly pointing to advice from Jim Gumbley, a Business Information Security Officer at Thoughtworks. His view, which I agree with, is that there's no proven safe way to run a high-permission agent like that today. These agents are useful largely because they have broad access to systems and information, and that's exactly what makes them risky.

So the discipline has to move into how you grant and constrain permission: isolating what an agent can touch, restricting what it can reach on the network and running endpoint protection. None of that limits what the agent can do so much as it shrinks the space where it can do damage if something goes wrong.

**Joe: That's how we've approached [Agent/works™](https://www.thoughtworks.com/en-br/agent/works/), treating agent safety as part of the architecture, so observability and auditability are built into the environment the agent operates in rather than bolted on afterwards.**

**But for leaders still experimenting with AI, what's one practical step they can take today to build confidence in using these tools, without waiting for all the answers?**

**Martin:** I agree with Simon Willison, a developer who's written extensively about how AI is changing software development, when he says that there is a practice and a skill to using AI effectively.

My advice is listen to the people around you who are already using these tools. If a colleague found something that worked, try it yourself, even if you're skeptical. These tools aren't easy to use well straight out of the box, so there's a lot to learn from people already figuring it out.

Rahul Garg, a Principal Engineer at Thoughtworks, has done great work on [how to organize context when you're working with AI](https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html). Build on what other people have already learned instead of starting from zero.

### The original spirit of Agile

**Joe: As a final thought, you've written that people have lost the thread on what Agile was actually about. What do you think we can learn from that original spirit as we figure out how to work with AI?**

**Martin:** Thoughtworks' role in Agile was to act as pragmatic experimenters. We tried things out on real projects, discovered new ways of working and rapidly shared our learnings to lead the industry. We were delivering real value for clients while utilizing our core differentiator: our people. [Expert generalists](https://martinfowler.com/articles/expert-generalist.html) come up with interesting solutions to problems and we generalize those solutions by sharing them through articles, books and talks.

That's the role I hope we'll play in AI-oriented software development: trying things, learning what works and then sharing those lessons so others can build on them.

**We've been here before. Not with these tools, not at this speed, but with the same underlying challenge: figuring out how to build software well when the ground is still moving. The organizations that led then were the ones willing to find out rather than wait to be told. The same is true today.**
