---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/harness-is-a-product"
title: "The harness is a product"
author: "Cecilia Geraldo"
date_published: "2026-11-04"
date_clipped: "2026-11-05"
category: "Software Architecture"
source_type: "rss"
source_last_modified: "2026-11-04"
---

# The harness is a product

Ask a team which model it runs and you’ll get a name (perhaps a few names). Ask what wraps the model though, from the instructions it loads, the tools it can call, what it’s allowed to touch, how its context is assembled, and the answer is likely to be a tour of half-owned artifacts.

These artifacts appear throughout [**volume 35 of the Thoughtworks Technology Radar**](https://www.thoughtworks.com/radar). However, while they may appear fragmented and disparate, they need to be understood as parts of a cohesive and singular product. Although the industry may have been talking about [harness engineering](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/what-harness-engineering) for the last year, the harness is undergoing an evolution from an implementation detail to a product in its own right which needs to be properly managed and maintained. This is why you see harness engineering at scale as one of this volumes four themes.

Many organizations aren’t at the stage where they’re thinking like this. While they may have a model and platform strategy, few have a harness strategy. Fewer still will have a named person accountable for it. This will need to change; the harness is today the layer where agentic engineering succeeds or fails.

## What is an agent harness?

Before we get deeper into why the harness should now be a product, let’s first look at exactly what it is. There are lots of definitions out there, and the devil really is in the detail when it comes to new agentic practices.

The right way to understand the harness is that it’s everything between the model and the work. It’s neither the model nor the application; it’s the layer that decides how the two meet. It is:

- The instructions and skills the agent loads.
- The tools the agent can call.
- The permissions and sandboxes the agent runs inside.
- The policy that decides what context the agent sees.
- The state the agent carries between steps.
- The orchestration that sequences the agent’s steps.
- The evaluation that tells you whether it was effective.
- The telemetry that tells you what happened when it did not.

None of these are new in the world of software engineering. A decade of application engineering distributed those concerns across a framework, a platform team and a CI pipeline. In an agentic system, though, they collapse into one artifact a small team can change in an afternoon; and, what’s becomes particularly problematic as it's used at scale, one no one may be accountable for.

![Cecilia Geraldo, Thoughtworks](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/thoughtworker-profile/c/pro_cecilia_geraldo_2.jpg "Cecilia Geraldo, Thoughtworks")

> "The harness is the place where engineering judgment is expressed. If it’s not managed properly, it’s also the place where that judgment is lost."

Cecilia Geraldo

Lead Consultant, Thoughtworks

> "The harness is the place where engineering judgment is expressed. If it’s not managed properly, it’s also the place where that judgment is lost."

Cecilia Geraldo

Lead Consultant, Thoughtworks

### A common harness challenge

The consequences of this can be found in a failure mode teams may have recently experienced. A first prototype is built, and then six months later you have a folder of Markdown, a handful of wrapper scripts, a configuration file with three commented-out experiments and one person who knows why the retry logic exists. While it often works, it’s also unlikely you can upgrade it safely, explain it to an auditor, or hand it to another team without a detailed and intricate walkthrough.

In other words, it’s *almost* a product: it’s just not being managed. It needs to be reframed as something that has users, from developers to agents, as well as versions, dependencies, a roadmap, quality gates and, of course, an owner. Without those, what you think of as a harness is really just configuration debt with a system prompt.

A good way of reframing all this is to see the harness as the place where engineering judgment is expressed in an agentic era. If it’s not managed properly, it’s also the place where that judgment is lost.

## Growing standardization and greater interoperability

The foundation of every product is a robust supply chain. In this volume of the Radar we not only see this supply chain becoming more cohesive, we can also see how it's being shaped by a set of platforms, tools and standards enabling interoperability and consistency.

**[Agent Plugins](https://www.thoughtworks.com/radar/platforms/agent-plugins.html)** is the best place to begin. It’s an interoperability standard that packages agent skills and MCP servers into one installable plugin, transforming the way such assets can be shared and used. It could well be seen as the foundation of the emerging harness. Alongside it, **[agent plugin marketplaces](https://thoughtworks.com/radar/techniques/agent-plugin-marketplace.html)** and **[Agent Package Manager](https://thoughtworks.com/radar/tools/agent-package-manager.html)** provide a way to publish, pin and compose capabilities, removing the need to copy and paste prompt fragments between repositories.

This is a significant step change that makes it more important we treat the harness as a product. A copied prompt has no version, no provenance and no upgrade path; a package does. The moment a harness can depend on somebody else's plugin, it becomes something more akin to a piece of software: in turn, this means it needs to be maintained and managed, ensuring compatibility, stability and reliability. This requires ownership and accountability. Without either, the potential benefits of portability and interoperability are almost worthless.

## Your harness needs a test strategy

A product with dependencies needs a way to know whether the last change worked. This is where most teams are still quite immature. However, **[harness quality evaluation](https://thoughtworks.com/radar/techniques/harness-quality-evaluation.html)** is critical to the effectiveness and reliability of the harness.

The question is simple: did this change make the agent better or worse? Most teams struggle to answer this. While they might be able to quote an acceptance rate or point at a pull request where the instructions got clearer, none of those things can really be taken as a true measure of harness quality.

The challenge here is multifaceted. Agent behavior is non-deterministic, tasks vary and an evaluation set that was representative in March could well be misleading by June. Running test suites also costs money and time. This is why teams often measure what’s cheap instead: things like [tokens consumed](https://www.thoughtworks.com/insights/blog/generative-ai/does-every-feature-build-ai-token-budget), suggestions accepted and tests passed. While they’re not irrelevant, they’re activity metrics. They can tell you the system is busy, but not whether it’s actually better.

What’s needed is deliberate and focused test discipline. You could, for example, start with a task-based golden test set drawn from real work rather than public benchmarks. This could be the 20 or 30 jobs the agent is expected to do, with a mechanism for scoring each one. You can then version that set alongside the harness, so a change and its evidence travel together. It may also be helpful to run a regression on every meaningful change, not only on releases.

Cost and latency, meanwhile, should be treated as first-class metrics. A harness that improves output while doubling spend hasn’t improved the product. And keep sampled human review for the qualities an eval cannot score: you may be able to build guardrails for things like tone, judgment or style, but these need to begin with human input.

### Evaluation needs to be owned

Evaluation has its own maintenance problem, and it rarely has a clear owner. However, teams that *do* get value from harness evaluation will typically give the test set an owner and a review cadence, just as they would treat a test suite that gates a release. Without this, the eval becomes an instance of what we call ‘**[human-in-the-loop theater](https://www.thoughtworks.com/radar/techniques/human-in-the-loop-theater)**’. It’s green and it may be comforting, but it’s disconnected from what customers actually experience.

The rule should clear: without an eval, there’s no change. A harness you cannot measure is a harness you cannot safely improve. You'll also find it hard to defend when someone asks why the agent behaved differently last Tuesday.

## Self-improvement needs a brake

While it’s important a harness evolves, the **[self-improving harness](https://www.thoughtworks.com/radar/techniques/self-improving-harness)** raises the stakes and risks. A loop that can rewrite instructions, select its own tools or re-rank can drift. The danger is that it produces changes that look like learning but behave like entropy.

What can make the difference here is whether the loop is connected to something real. A well-managed harness will be; this is something the owner should monitor closely.

This is where the **[feedback flywheel](https://www.thoughtworks.com/radar/techniques/feedback-flywheel)** comes in. It provides a signal of where action needs to be taken. By reviewing findings, incidents, eval failures, cost anomalies and the cases where a human had to take over, it becomes possible for harness owners to ensure that the harness is being properly evolved and that it’s [responding to real requirements, demands and contextual changes](https://www.thoughtworks.com/insights/blog/generative-ai/harness-engineering-agent-feedback-exploring-ai-coding-sensors). Without this signal, self-improvement is a model editing its own job description and calling the result progress.

### Three preconditions for harness self-improvement

There are three preconditions required to make the loop safe enough to run:

- **An** **evaluation harness**, so improvement is measured rather than asserted.
- **Provenance**, so every self-authored change can be attributed, reviewed and reverted.
- **A rollback path,** so a bad iteration costs an afternoon rather than a quarter.

The rule is that you should automate the proposal and keep the approval. Let the system suggest the instruction change, the tool substitution and the context policy, but don’t let it merge to main on vibes alone.

## From building a harness to running one

The critical blip on the latest volume of the Radar that reflects the harness becoming a product is **[enterprise harness](https://www.thoughtworks.com/radar/techniques/enterprise-harness).** It highlights the importance of running a harness at scale but also the challenge such work poses.

To some extent, we are actually beginning to see the first stages of this in some organizations. We've seen some instances of [platform teams](https://www.thoughtworks.com/insights/blog/platforms/the-evolution-of-platform-engineering--lessons-from-the-trenches) being asked to own, alongside everything else, the components that make up the agent runtime. As you'd expect, this means the same expectations that come with platform engineering: ensuring auditability, managing access controls, overseeing lifecycle management and even implementing spend controls.

It's worth taking note of this shift if it's not something that's already on your radar (pun intended). Where building a harness may have been a process of experimentation and even trial and error, running the enterprise harness requires us to tread surprisingly familiar ground. It consists of things like golden paths, developed through **[path-to-production mapping](https://www.thoughtworks.com/radar/techniques/path-to-production-mapping)**, that make the supported route faster than the unsupported one, **[agent sandboxing](https://www.thoughtworks.com/radar/techniques/agent-sandboxing)** with defaults that do not depend on a developer remembering a flag and plugin allow-lists with provenance checks.

It also requires a considered [model routing](https://www.thoughtworks.com/insights/blog/generative-ai/kimi-k3-new-multi-model-era) policy, so cost and residency are enforced in one place rather than negotiated per team, as well as telemetry that can tell you which harness version produced a particular output. It also needs proper deprecation and support; a runtime without a deprecation policy is one that nobody can safely depend on.

Finally, identity is the most pointed and urgent issue to be addressed. An agent acting on someone's behalf needs a clear answer to whose permissions it's using, what it may do without asking and what evidence is left behind. Those are harness decisions, not model decisions; they're exactly the kind of thing an enterprise cannot leave to a per-team configuration file.

While this is arguably next platform-engineering moment, it's also very much a product-management one. Someone has to hold the roadmap, arbitrate between teams, decide what the harness will not do and carry the pager when a plugin update breaks a workflow.

### A poor harness can accelerate shadow IT

There's a caveat to all this that organizations need to take seriously. If the institution's harness is slower and less capable than the one a team can assemble in a weekend, people will route around it. Paved roads only work when they are genuinely faster to travel. [AI-accelerated shadow IT](https://www.thoughtworks.com/radar/techniques/ai-accelerated-shadow-it) is often a symptom of an adoption problem; it could however, quickly become a security problem.

## Owning the harness as a product

There are three questions worth asking about your agent harness that can help you begin to treat it as a product in its own right:

- **Who owns it?** Where do they sit in the org chart? This isn't the team that just *happens* to be maintaining it, but the person who is actually accountable for its quality and its roadmap.
- **How do you know the last change made it better?** If the answer is a demo, an anecdote or an acceptance rate, the harness is not yet a product.
- **What is it allowed to touch?** This includes data, tools, credentials and production. The blast radius is part of the product definition, not an implementation detail discovered during an incident.

Harness engineering only really emerged in 2026, so it's still somewhat immature as a discipline. However, Technology Radar Vol.35 demonstrates the ecosystem is becoming more cohesive. This doesn't mean you should sit still on this; now is the time to take action and to take questions around harness scale and ownership seriously. Decisions are cheaper now than they will be 12 months down the line. Navigating the inevitable changes in this field will also strengthen your chance of success in the long term.

**You don’t get to choose whether your harness is a product. But you do decide whether you manage it with the intention and care your teams and organization need.**
