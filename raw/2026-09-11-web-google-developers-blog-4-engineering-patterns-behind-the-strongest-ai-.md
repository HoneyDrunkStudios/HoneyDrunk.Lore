---
source: "https://developers.googleblog.com/4-engineering-patterns-behind-the-strongest-ai-agents-challenge-submissions/"
title: "4 engineering patterns behind the strongest AI Agents Challenge submissions"
author: "Sergio Villani"
date_published: "2026-09-02"
date_clipped: "2026-09-11"
category: "AI / LLM Research & Tooling"
source_type: "web"
---

# 4 engineering patterns behind the strongest AI Agents Challenge submissions

Source: https://developers.googleblog.com/4-engineering-patterns-behind-the-strongest-ai-agents-challenge-submissions/

# 4 engineering patterns behind the strongest AI Agents Challenge submissions

SEPT. 2, 2026

[Sergio Villani](https://developers.googleblog.com/search/?author=Sergio+Villani)
Technical Solutions
Google Cloud AI

We just wrapped the [Google for Startups AI Agents Challenge](https://cloud.google.com/blog/topics/startups/startups-are-building-the-agentic-future-with-google-cloud?e=48754805) with thousands of builders shipping agents from around the world, and our panel scored submissions across three tracks.

The “multi-agent-system” was probably the most frequent claim across the submissions, and on closer inspection, some actually were truly sophisticated multi-agent solutions while some others turned out to be a single model working through a chain of prompts with agent names attached.

Across this spectrum though the entries that [actually ranked at the top of each track](https://lnkd.in/p/eVKZNj77) kept showing the same handful of engineering decisions and patterns. Here are four of them, worth stealing for your own build. They're pulled from real code submissions and described without names, because this isn't about any one team:

- **Bidirectional MCP:** an agent that's both a client of its own tools and a server other agents can call.
- **Event-driven concurrency:** agents reacting to a shared signal in parallel instead of waiting in a call chain.
- **Same-bar fallback:** a smaller model standing in for an overloaded one without a lower quality check.
- **Tiered routing:** cheap, deterministic checks running before the model gets touched at all.

## **Pattern 1: The tools you built for yourself can serve other agents too**

Most submissions used MCP one direction: the agent calls out to a tool server for data. However, one team extended it both ways. Their agent consumed a telemetry database through its own MCP tool layer internally, then exposed that same reasoning as an MCP server other agents could call, so another agent could ask it a question directly, no chat UI built for humans required.

The internal half of this matters on its own, before you even get to the external half. A naive version of this agent would run a SQL query against the telemetry store and dump every row straight into the model's context, and that on a real production database is exactly how a single request blows through your token budget. Going through an MCP tool layer means the agent gets tools to inspect and filter the data programmatically, pulling back a job's execution plan or a specific stack trace rather than an entire table, so the context stays small enough to actually reason over. Mediating database access through tools rather than a raw connection is also what makes the external half of the pattern possible at all. Exposing a tool that only ever returns a bounded, purpose-built answer is safe to hand to a caller you don't control while a raw SQL connection never would be.

That's the decision that changes what the product is. Once the agent's own reasoning already sits behind a tool interface, exposing it externally just means standing up an MCP server in front of the same tools. In this case, that meant a coding agent working in a terminal or an IDE could call the performance agent directly and ask about a specific job, the same way it calls any other tool. A human doesn't have to open a dashboard, describe the problem in a chat box, and copy the answer back into their own workflow. A chat interface is a destination while an MCP server can be infrastructure other agents build on, without anyone writing a second integration for them.

The part that's easy to skip: once you're serving a caller you don't control, that server needs real access control. Anyone who can reach it can now call your reasoning layer directly. A tool surface only your own agent ever calls doesn't need to think about that. A tool surface the outside world can call does.

**Do this today:** if your agent already talks to its own data over MCP internally, check how much extra work it'd take to expose those same tools externally, before you build a second, human-only API that does the same job.

## **Pattern 2: Let agents react to the same event in parallel**

One team's first version was a linear pipeline: a sensor-monitoring agent called a compliance agent, which called a resident-messaging agent, which called a dispatch agent. It worked fine as a demo. It fell apart on the real use case: catching a fall risk from a change in gait, cross-referencing it against a live drug-interaction database, and getting a message to the right person before the window to act closed.

The fix was an async event bus built on four separate asyncio.Queue instances, one per agent, each with its own worker coroutine pulling from it. Instead of Agent A calling Agent B and waiting for a return value, agents publish typed events to named topics and subscribe to whichever ones they care about. A gait-velocity drop of 15 percent or more publishes a `CLINICAL.ANOMALY_DETECTED` event. The compliance agent is already parked on that topic, so it picks the event up the instant it fires, cross-references it against the drug-interaction database, and publishes its own `CLINICAL.COMPLIANCE_REPORT_READY` event the moment it's done, not on a polling interval, not waiting for anything upstream to explicitly hand it off. The messaging and dispatch agents work the same way downstream, each one woken by the topic it subscribes to rather than a direct call from whoever ran before it.

That's the actual difference in a call chain versus an event bus: in a call chain, total latency is additive, agent one's time plus agent two's plus agent three's, because each one is holding the stack open waiting on the next. On a topic-based bus, two agents that don't depend on each other's output run at the same moment, because neither one is blocking on the other's return. You want this shape wherever your agents run on genuinely different tempos: one polling every few seconds, one making a network call that takes half a second, one that only fires once at the very end. Chain all of that into a single call stack and your fastest agent is still bottlenecked behind whichever one takes longest.

**Do this today:** check whether two of your agents ever need to react to the same signal. If your architecture makes one wait behind the other to do it, that's a single-threaded system wearing a multi-agent label.

## **Pattern 3: A fallback model still has to clear your bar**

A different team's clinical-reasoning agent ran on Gemini 3.1 Pro. Under real load, Pro started returning 503s. Most other entries would bolt on a retry loop against the same model and move on. Instead, this team built a fallback to Gemini 3.6 Flash with backoff, and ran the response from either model through the exact same validation function before accepting it: a citation check confirming the answer actually named a real clinical guideline, not just plausible-sounding medical language.

The detail worth stealing here isn't the existence of a fallback, it's where the validation lives. It isn't duplicated once for the primary path and once for the fallback path, where it's easy to update one copy and forget the other. There's a single `validate_clinical_response()` function that both the Pro path and the Flash path are forced to call before either result can leave the agent. Once a response hits that function, it doesn't matter which model produced it, neither one gets a shortcut, and neither can ship an answer that fails the check just because it happened to be the one available when the request came in.

That's what actually prevents a fallback from quietly lowering your bar: not remembering to apply the same standard twice, but making it structurally impossible to apply it only once.

**Do this today:** go find the code path that runs after your fallback fires. If it skips a validation step the primary path has, you're shipping two different products while only testing one.

## **Pattern 4: Tiered routing before the expensive call**

Inference cost is probably the most argued-about constraint in AI right now: everyone wants frontier-model reasoning without frontier-model prices on every request. This is one of the cost patterns we actually saw working in production this cycle.

One team measured what was actually eating their inference budget and found it wasn't the hard questions, it was the easy ones: "where's my order," "cancel my appointment," going through the same full model call as genuinely ambiguous requests. Their fix was a three-layer classifier in front of the agent: a local regex pass catches navigational intent at zero tokens, an ambiguous case gets a cheap Gemini call at ten tokens and temperature 0.1 just to classify intent, and only what survives both reaches the full reasoning model. That first pass alone handled more than 40 percent of incoming messages, by their own measurement, before a real model call ever happened. A separate entry applied the same idea to a different pipeline: a fast, cheap model gates and triages an incoming case, escalating only what needs deep reasoning to a slower, pricier model. Don't spend your most expensive model on a decision a cheaper one can already make.

**Do this today:** look at your own traffic distribution before assuming you need a bigger model. A cheaper first pass usually gets you further.

Looking back at this round of the Challenge, the entries built on [Agent Development Kit (ADK)](https://adk.dev/) and driven through the [Agents CLI](https://github.com/google/agents-cli) were the ones where these patterns showed up most often, mostly because the framework doesn't fight you on concurrency, fallback, or handing a tool to another agent.

Across all these four patterns none of them truly require bigger teams or newer models. They represent sound engineering practices that are frequently overlooked. Also, they compose nicely and complement each other. One team in particular that stood out combined pattern one and pattern three together in the same build: a root agent fanning specialist agents out concurrently, then exposing that whole reasoning layer as an MCP server other agents could call directly.

That's the bar we'll be looking for in the next round: a system that follows these four patterns. But you don’t need to be completing a challenge. Use these patterns in your next build.

posted in:

- [AI](https://developers.googleblog.com/search/?technology_categories=AI)
- [Cloud](https://developers.googleblog.com/search/?technology_categories=Cloud)
- [Case Studies](https://developers.googleblog.com/search/?content_type_categories=Case+Studies)
- [Best Practices](https://developers.googleblog.com/search/?content_type_categories=Best+Practices)
- [Learn](https://developers.googleblog.com/search/?content_type_categories=Learn)

Previous

Next

Related Posts

[AI
Cloud
How-To Guides
Learn

Autonomous LLM post-training with Tunix on TPUs

SEPT. 11, 2026](https://developers.googleblog.com/autonomous-llm-post-training-with-tunix-on-tpus/)
[AI
Case Studies
Community

Decoding cosmic signals with deep learning and Keras

AUG. 27, 2026](https://developers.googleblog.com/decoding-cosmic-signals-with-deep-learning-and-keras/)
[Mobile
AI
Announcements

Announcing ADK for Kotlin 1.0: Building Production-Ready AI Agents in Kotlin, Android, and Beyond

SEPT. 9, 2026](https://developers.googleblog.com/announcing-adk-for-kotlin-10-building-production-ready-ai-agents-in-kotlin-android-and-beyond/)
[AI
Cloud
Case Studies
Learn

HeyGen x Google Cloud: Bringing Avatar IV to TPUs

AUG. 13, 2026](https://developers.googleblog.com/heygen-x-google-cloud-bringing-avatar-iv-to-tpus/)
