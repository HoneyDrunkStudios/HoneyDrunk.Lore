---
source: "https://incident.io/blog/degrade-gracefully-designing-ai-features-that-keep-working-when-the-model-doesnt"
title: "Degrade gracefully: designing AI features that keep working when the model doesn't"
author: "Komal Ahuja"
date_published: "2026-10-29"
date_clipped: "2026-11-16"
category: "Software Architecture"
source_type: "rss"
---

# Degrade gracefully: designing AI features that keep working when the model doesn't

What does your product do when the model behind it goes down? And the harder one: what does it do when the model stays up but quietly gets worse?

We put that question to [Michael Tweed from Skyscanner](https://www.linkedin.com/in/mtweed/) and [Sahaj Sawhney](https://www.linkedin.com/in/sahajsawhney/) from incident.io in a [recent webinar.](https://incident.io/events/how-do-you-respond-when-your-ai-tooling-and-models-fail) I asked each of them to pick one thing to invest in this quarter: better fallback models, better detection, or graceful degradation. They both picked graceful degradation, with barely any debate. This post will talk about why, and what "graceful" looks like in practice.

## Why this question matters now

When incident.io shipped its first set of AI features, none of them were in anyone's critical path. They were useful, and you could still run an incident perfectly well without them. If one broke, it was a shrug and a bug report.

But that's changed now. Plenty of engineers who use incident.io now expect the chatbot to respond with something helpful, and a lot of them have probably forgotten the old commands for triggering manual actions, because why would you remember them? AI became part of how people work one convenient shortcut at a time, and "what happens when it fails?" stopped being a theoretical question.

Michael sees the same thing at Skyscanner, and he's refreshingly honest about being part of it. He uses AI to debug code, diagnose failures and work out why an alert fired. When a build fails, he'll often skip reading the error and just ask the agent to fix it. He also told us about a point where he'd set up so many loops and agents on his own projects that he couldn't describe exactly what was happening at any given moment. Nothing had gone wrong - he just no longer had the picture in his head.

That's the real shift. Teams have not only added a dependency, they've started delegating the understanding as well as the work. So when the model goes away, you lose the output, plus some of the context you'd have built up by doing the work yourself.

## "Just fail over to another model" is harder than it sounds

If you've done any infrastructure work, you know the reflex. A dependency is flaky, so you add a second one and route around the first. Two incident.io engineers, Patrick and Mike, [turned off Pub/Sub in production and nobody noticed](https://incident.io/blog/we-turned-off-pub-sub-and-nobody-noticed), which is the dream outcome for that kind of work.

Skyscanner took the same approach early, building an LLM gateway so internal clients make a single call and the platform team can switch the model or provider behind it. In principle, that's a model outage handled.

In practice, it's a lot messier than failing over a database. Michael and Sahaj gave a few reasons:

1. **Models don't behave the same way.** You can't reasonably expect the exact same prompt to work the same way on a different model, and plenty of prompts are tuned to one in particular. Sahaj is optimistic here, because frontier models have got much better at following instructions in the last five or six months and he thinks we're converging. But we're not there yet.
2. **Not everything is a technical constraint.** Michael's team has to weigh legal and cost considerations that change depending on the workload: how sensitive is the data, how quick does it need to be, how much can you spend? On the incident.io side, some customers have requirements about which subprocessors are used. If a customer isn't okay with their data going to a particular provider, you can't quietly reroute them just because that provider is having a bad day.
3. **Granularity is a design decision.** Do you give every single prompt a fallback provider, or do you work at the level of a whole feature? Fine-grained fallbacks are more resilient but make development heavier, and nobody wants to add a pile of complexity to every change. Coarse ones are easier to build and blunter when they kick in. There are pros and cons either way.
4. **Fallbacks you don't use go stale.** This one isn't specific to AI, but it bites just as hard. If you rarely exercise a fallback path, you slowly lose confidence in it, and the day you need it is the day you find out whether it works.

Michael's team has tamed some of this by sorting models into tiers: fast, cheap models for lighter workflows and frontier models for heavy ones. The failover rules then apply to a class of model, rather than needing a fresh decision every time a new one comes out. It helps a lot but it doesn't make the problem disappear.

## When the model is up, but getting worse

There's another reason failover isn't enough, which is that an AI system can fail without going down at all.

A model can return a perfectly healthy response that's quietly much worse than yesterday's. Nothing on your uptime dashboard will tell you, but Michael described exactly this after a failover at Skyscanner, when engineers started asking whether something had changed because the responses they were getting seemed "really dumb". It's a good reminder that the quality bar has to be part of what "working" means, alongside latency and availability.

Catching that means measuring quality like any other signal. Sahaj's team traces usage across the incident.io platform the same way it traces any other request. They also run LLMs as judges to grade the quality of an interaction or a response, and those grades become metrics they alert on. (If you want to see how that works for Investigations, we've written about it in [detail here](https://incident.io/blog/building-investigations-what-it-takes-to-build-an-ai-sre).)

Sahaj was upfront about the limits. Those graders lag, because they mostly catch the kinds of failure already seen, and the team would love to get faster at spotting new ones. They're getting a lot more robust over time, but they're not a silver bullet.

So they also lean on much simpler signals, which are surprisingly good. A thumbs up or thumbs down on a chat response gives you more information than you'd expect. So does a user swearing at an agent and telling it that's not what they asked for. If that's happening a lot, something has gone wrong, and no dashboard will say it as clearly.

## So what does "graceful" actually mean?

Michael and Sahaj gave slightly different answers to this, and I think the difference is useful.

Michael's is the one you'd expect from someone running a platform: "Graceful degradation means the end user just doesn't see anything." Engineers carry on as normal. Behind the scenes, someone writes up the post-mortem about the provider failing and the config change that switched traffic over, but nobody on the receiving end ever knows.

Sahaj's comes from building agents, and it's more about outcomes than invisibility. A lot of what our AI products do is take a pile of signals and work out what's gone wrong, and there are usually many paths to the answer. If part of the system is down, the best case is that the agent still finds its way to the root cause. Maybe it takes longer, maybe it costs more, maybe it does more work itself instead of leaning on other agents and falls back to more old-school, deterministic workflows that go and fetch the same information. What matters is that the incident still gets resolved and that responders still get what they need, in the right place, at the right time.

Put the two together and you get a test I find helpful: a system degrades gracefully when the person using it still gets what they came for, even if the route there is slower, pricier or less impressive than usual. Sometimes they won't notice anything. Sometimes they'll notice a lot and still be unblocked. Either is far better than the alternative, where something that has quietly become a core part of someone's workflow just stops.

## Principles for graceful degradation

Nobody has this fully figured out, and there’s plenty of maturity still to be found. But a few principles keep coming up, and they’re the ones we’re trying to build into how incident.io works.

**Give every AI feature a floor.** For each feature, ask what happens if the model isn't there at all, and build that path on purpose. Sometimes it's a deterministic version of the same job. Sometimes it's the old manual action, with a clear message about what's going on. The floor doesn't have to be pretty. It does have to exist. This lines up with what our VP Engineering, Norberto, wrote in [Humans aren't fast enough for 4 9's](https://incident.io/blog/humans-arent-fast-enough-for-4-nines): buy the system time to survive the first few minutes on its own, and usually that's done better by things like circuit breakers and failover than by another layer of AI.

**Compose, so failure is partial.** incident.io's AI products are a composition of lots of smaller bits of agentic work, each with its own mode of fallback. That means there's no single place that, when it breaks, takes the whole feature down. When something fails, the rest keeps contributing and the feature degrades rather than collapses. It costs more design effort up front, but it's worth it.

**Keep the model off the critical path where you can.** Sahaj's team still tries not to put AI on the true critical path of certain parts of the product. He expects that to change over time as models and tooling mature, but for now it's a sensible default. They're also careful about how model output is presented, since a confident-looking wrong answer in the middle of an incident is its own kind of failure.

**Don't use a model where you need determinism.** Michael was building a tool that used a model for some analysis, and by the end he'd written so much Python around it, to force the output into the right shape, that the model was only responsible for a tiny part of the result. His question to himself was whether he'd really needed the model at all. Models are non-deterministic by design, and if you're trying to force 100% determinism out of one, you probably don't need a model there. Some of the most resilient AI features are the ones where someone worked out which part of the job needs a model, and which part doesn't.

**Exercise your fallbacks.** An unexercised failover is a story you tell yourself. Route a share of real traffic through your fallback, break things on purpose, and find out in a quiet week rather than the worst one.

**Pick the quality bar per use case.** Is accuracy more important than speed? It depends. If a model is quickly scoring something to give you a confidence level, you want it fast and you don't want it blocking a workflow. If it's doing something complex and expensive, you'd rather pay for the best answer than get a quick one that feels like wasted money. Deciding that up front tells you what an acceptable fallback looks like.

**Reset expectations, yours included.** Michael made a point I keep coming back to. We've got used to agents giving us answers instantly. An on-call engineer joining an incident used to read through channels and dashboards to catch up, and now they expect a summary the moment they arrive. When the agent's down, it feels like something's broken. But as Michael put it, this doesn't have to happen in seconds or milliseconds, and it's okay to take a little longer if something's degraded. Reading the dashboards yourself was normal not very long ago, and it should still be a perfectly acceptable fallback.

## A short checklist

If you're wondering where to start, these are the questions worth asking about any AI feature:

1. If the model were unavailable right now, what would the user see?
2. If it were available but noticeably worse, how would we find out, and how quickly?
3. Is there a deterministic path to the same outcome, even if it's slower or cruder?
4. When did we last exercise the fallback with real traffic?
5. Are there customers or workloads where we can't switch providers, and what happens to them?
6. Would a person know what to do next if the AI disappeared mid-task?

If you can't answer some of these yet, you're in good company. Neither Michael nor Sahaj could answer all of them cleanly either, and they said so.

Every team's constraints are different, so take what's useful. But if you're putting AI in front of people who depend on it, it's worth spending some of your time on what happens when it breaks, because it eventually will.

If you'd like to see where incident.io has got to, [take a look at Investigations](https://incident.io/investigations) or [book a demo](https://incident.io/demo).
