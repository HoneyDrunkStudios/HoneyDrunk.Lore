---
source: "https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/refactoring_the_engine_an_incremental_path_to_AI_assisted_delivery"
title: "An incremental approach to AI-first software development"
author: "Moritz Wilke"
date_published: "2026-11-27"
date_clipped: "2026-11-27"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Refactoring the engine

An incremental path to AI-first software development

[Blogs
Back](https://www.thoughtworks.com/insights/blog)

- [AI and ML](https://www.thoughtworks.com/machine-learning-artifical-intelligence)
- [Blog](https://www.thoughtworks.com/insights/blog)

By 

[Moritz Wilke](https://www.thoughtworks.com/profiles/m/moritz-wilke)

Published: November 27, 2026

Most discussions about AI in software development ignore a basic reality: teams start from fundamentally different baselines. Hand an AI coding assistant to a team with automated testing and continuous deployment and you accelerate delivery. Hand it to a team with manual QA (quality assurance) and slow code reviews, and you just back up inventory at the nearest gate.

The industry loves to showcase and debate the destination, e.g. lights-out AI factories, but offers almost no guidance on the terrain between where most teams actually stand and where they want to be.

While there is no universal map you can follow, this piece invites you to investigate your starting point and follow a sequence of steps to improve your delivery with AI-first software development, built on two core ideas:

- **Apply continuous improvement to your delivery practice:** Measure, improve in a tiny increment and measure again.
- **AI for building the harness:** Lower the activation energy for creating automated safety nets rather than just churning out product code.

## The engineering maturity spectrum

We rarely know upfront what the final product should look like or what users will actually find valuable. Longer planning phases delay discovery, larger changesets make releases fragile and delayed feedback increases the risk of building the wrong thing entirely.

Modern software engineering practices such as XP (Extreme Programming), Agile, CI/CD (continuous integration and continuous delivery) and DevOps address these risks by shrinking batch sizes, automating verification and shortening feedback loops.

These disciplines share a single objective: improving delivery throughput from analysis to production. Per Theory of Constraints, accelerating isolated steps without addressing system bottlenecks yields no overall throughput gain.

Yet the adoption of these practices remains uneven. According to the [2024 DORA Accelerate State of DevOps Report](https://dora.dev/research/2024/dora-report/2024-dora-accelerate-state-of-devops-report.pdf), only 19% of teams reach the "Elite" tier (deploying on demand with sub-day lead times). Meanwhile, 60% of teams sit in the Medium or Low tiers and still deploy anywhere from once a week to twice a year, slowed by manual QA handoffs, heavy approval gates and fragile architectures.

Putting AI on top of these divergent starting points produces fundamentally different outcomes.

## AI-amplified strengths and weaknesses

We can map software teams along a two-dimensional spectrum: engineering maturity on one axis and AI adoption (from tab-complete to AI factory) on the other.

As the [2025 DORA State of AI-Assisted Software Development Report](https://dora.dev/research/2025/) concluded, AI doesn't fix a team, it amplifies what's already there. Where you sit on the maturity axis dictates what AI actually does to your system.

Figure 1: Despite being the focus of industry talk, the AI automation grade of a team is not the important matter, at least not without taking its engineering maturity into consideration.

Figure 1: Despite being the focus of industry talk, the AI automation grade of a team is not the important matter, at least not without taking its engineering maturity into consideration.

**At the high-maturity end:** Coding was never the pacing constraint. Comprehensive automated tests, trunk-based integration and fast deployment guardrails absorb AI-generated micro-changes effortlessly. Freed from implementation overhead, these teams invest in custom harnesses and internal platforms that compound their speed.

**At the low-maturity end:** Coding felt like the bottleneck due to large batches, manual testing, integration problems and fragile design. Generating code faster without automated safety nets chokes downstream bottlenecks. Pull requests balloon, manual QA and review queues collapse under unverified inventory, merge conflicts spike and technical debt compounds.

Jumping straight to autonomous AI agents from the low-maturity end hits a hard wall. But the standard counter-advice: "fix everything first before you touch AI" is equally unrealistic.

## A pragmatic path forward

Teams face intense pressure to deliver features every day. Freezing work for six months to reinvent the delivery engine from scratch is not an option.

Yet you also cannot fix delivery bottlenecks simply by pouring AI on top of them.

The way forward is to apply the philosophy of continuous improvement to your delivery process itself: identify tiny, low-risk interventions, test them with your team, reflect on the outcome and iterate.

### The diagnostic: Mapping path to production

To improve the system without guessing, start with a quick [path-to-production mapping](https://www.thoughtworks.com/radar/techniques/path-to-production-mapping) session. Gather the team to trace your work from initial analysis and story writing all the way to live production. Map the value stream on a board, then ask the team:

- Which phases take the heaviest toll on us?
- Where does work feel uncomfortably high-friction?
- Where does code spend the most time sitting idle or bouncing back for rework?

Vote on pain points with the team to pick a single bottleneck. Once you identify it, do not simply attempt to speed up that specific station but look upstream as well. The intervention must target the point where excess inventory or defective work was generated. Per Theory of Constraints, optimizing outside this pacing constraint provides zero system benefit.

### The cadence: Each sprint as an experiment

Treat each sprint as a bounded workflow experiment. Pick one pacing constraint from your path-to-production map. Deploy one intervention to test against it. Run it for a single sprint. A sprint already exercises every phase of your development lifecycle, making it the ideal boundary for an experiment.

Reflect in the retrospective: Did work flow with less friction? Did releasing feel safer? Did the bottleneck move? If the technique works, adopt it as your new baseline. If it adds friction or feels unhelpful, discard it immediately without guilt or dogma.

### The toolboxes

When tackling a bottleneck, teams can draw from two toolboxes: classical software delivery practices and the modern AI toolbox.

#### Toolbox 1: “Classical” software development practices

These are the proven, ["sensible default" practices](https://www.thoughtworks.com/en-de/insights/topic/sensible-defaults) that shrink batch sizes, shift feedback left and eliminate waiting queues:

- Integration and flow: Frequent and continuous integration, fast and verified automated builds and early, continuous deployment
- Collaboration and quality: Pair programming, TDD (test-driven development) and active technical debt management
- Operational readiness: Building security in, automating deployment pipelines and building for production from day one

#### Toolbox 2: The modern AI toolbox

This is the newer, more experimental layer of AI-native tools and workflows: coding assistants, AI review agents, agentic pipelines and emerging patterns like harness engineering. Because this space moves fast, it helps to treat it as a pool of experiments rather than a fully fleshed-out plan that you can follow. Pull inspiration from places like the Thoughtworks Technology Radar ([Tools](https://www.thoughtworks.com/en-de/radar/tools) and [Techniques](https://www.thoughtworks.com/radar/techniques)), Martin Fowler’s blogsite (e.g. [Harness Engineering](https://martinfowler.com/articles/harness-engineering.html)) or sources such as  [Exponential Engineering](https://exponentialengineering.dev/) or [Impatient Programming](https://impatientprogramming.org/).

These two approaches are often framed as opposing philosophies, traditional engineering discipline versus rapid AI generation, but they work best together. The key is letting AI act as a scaffolding accelerator that lowers the activation energy for the automated safety nets your team needs more than ever.

Many engineering disciplines from toolbox 1 were historically ignored because they carried an immense upfront time tax. Writing property-based tests, parameterized suites and fuzzers requires heavy boilerplate. Scaffolding architectural fitness functions (like ArchUnit tests or module boundary rules) requires understanding niche syntax. Hardening CI/CD pipelines, caching strategies and automated linting scripts takes time away from product features.

By using AI for programming your pipeline over programming (just) your application, Toolbox 2 lowers the activation energy for toolbox 1. AI acts as a scaffolding accelerator, making it economical for everyday teams to build the robust automated safety nets that previously only elite teams had the bandwidth to maintain:

#### Choosing an intervention

Look at the specific constraint and ask:

- **Is this an elimination problem? (Lean/XP):** Can you bypass the waiting queue entirely, for example, replacing an async PR (pull request) review queue with pair programming, replacing manual regression testing with TDD or reducing batch size?
- **Is this worth an AI-native experiment? (Toolbox two):** Can a targeted AI tool or agent remove friction directly and can you test it safely for one sprint?
- **Is this a high-activation-energy problem? (AI scaffolding):** Does the team avoid an essential engineering practice because the upfront syntax and boilerplate tax is too high?

You do not need to choose the "correct" tool on day one. Because each experiment is bound to a single sprint, the cost of an incorrect choice is virtually zero. If your team tests AI-generated PR summaries for two weeks and discovers they produce noise without accelerating review velocity, abandon the experiment in the retro and test batch-size caps or pairing next.

Framing changes as one-sprint experiments offers an added bonus: it defuses polarized debates. Practices like pairing or TDD rarely win unanimous enthusiasm upfront, but a time-boxed experiment invites curiosity instead of resistance.

## In practice: Unclogging the review bottleneck

Consider how one team tackled their primary delivery bottleneck: the code-review queue. Their Path-to-Production mapping revealed that pull requests idled in review queues for days, causing massive inventory pile ups and painful merges.

Open-source ecosystems invented PRs to guard against untrusted contributors. Adopting them as an asynchronous, blocking handoff inside a trusted product team creates an artificial logjam. Introducing AI to write code faster only amplifies the problem: PR sizes and volume explode, overwhelming reviewers.

Rather than attempting an overnight process overhaul, the team ran a sequence of single-sprint experiments to [systematically deconstruct](https://a4al6a.substack.com/p/stop-using-pull-requests) the bottleneck:

- **Sprint one – Bounding the batch:** They capped pull requests at 500 lines and automated baseline linting in CI so reviewers never argued over formatting. Using AI, they scaffolded the CI gate and linting rules in hours
- **Sprint two –  Ship / Show / Ask:** They adopted Rouan Wilsenach’s [framework](https://martinfowler.com/articles/ship-show-ask.html) to categorize changes: merging low-risk changes immediately (Ship), notifying the team without blocking (Show) and reserving blocking reviews exclusively for complex logic (Ask).
- **Sprint three – AI-assisted harnessing:** To gain confidence in fast merging, they used AI to rapidly scaffold architecture tests and contract suites around legacy boundaries.
- **Sprint four – AI Review Agent (toolbox 2):** Next, they tested an AI review agent to automate feedback on remaining PRs. In the retrospective, the team found it generated noise without accelerating review velocity. They dropped it immediately and pivoted to pairing on critical features, reviewing code continuously as they wrote it.

Not every technique stuck and the team didn't need a dashboard to know what worked. The sprint retrospective acted as the arbiter. If an intervention made shipping smoother, it remained. If an experiment felt awkward or ineffective, they dropped it. It may have lacked an essential prerequisite, or it simply wasn't the right fit for them at that moment.

## Rinse and repeat

Continuous delivery is a habit of small, deliberate adjustments.

If your team is struggling to see gains from AI, stop trying to push code through the bottleneck faster. Map your path to production, find the step that hurts the most and use every tool at your disposal, traditional engineering discipline and AI scaffolding alike, to remove friction from that single constraint.

Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
