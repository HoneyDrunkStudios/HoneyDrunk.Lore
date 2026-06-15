---
source: "https://about.gitlab.com/blog/gitlab-transcend-announcements/"
title: "GitLab: Built for the agentic engineering era"
author: "GitLab Blog"
date_published: "2026-06-10"
date_clipped: "2026-06-15"
category: "DevOps & CI/CD"
source_type: "web"
---

# GitLab: Built for the agentic engineering era

Source: https://about.gitlab.com/blog/gitlab-transcend-announcements/

Published on: June 10, 2026

10 min read

What we announced at GitLab Transcend, and how one platform delivers agentic speed with the control enterprises need.

GitLab Transcend, our customer event showcasing our roadmap, success stories, and industry research just wrapped. Here's what we announced and demonstrated:

It's never been easier or faster to write code with agents, our research across more than 1,500 developers and tech leaders showed that 91% of organizations now run two or more AI coding tools, and 54% run three or more. Some of our customers' codebases are growing up to five times in a single year. But unmanaged, that speed creates chaos.

Catch up on all the action from Transcend with our

[on-demand webcast].

For most organizations, the answer to increasing the pace of innovation has been AI coding. But coding agents built on a fragmented software lifecycle isn't agentic engineering, it's a shortcut to inefficiency and risk.

We see it across our customers in recurring forms. Infrastructure built for human pace buckles under machine-scale concurrency in source code management. Agents have context around the code but not the full software development lifecycle (SDLC), so they stall out in large monorepos and give up across repos as the context window fills. Code, dependencies, and deployments change faster than teams can govern them. And fixed contracts force teams to guess at seats and credits a year ahead, in the era hardest to forecast.

The same research shows the strain: 73% worry about maintaining the code, and only 21% see productivity gains across the full SDLC.

None of this is a reason to slow down. It's a reason to build the agentic infrastructure that turns the speed of agentic coding into strong ROI.

GitLab is already the platform where enterprises build and ship software. Source code management (SCM), CI/CD, governance, deployment, and more all live in one place, and our platform currently serves more than 50 million users and 100,000 organizations. We sit in the path of every software team and the agents that touch their code, pipelines, or production.

Think of the platform as a living system, with four parts that work together the same way whether a human or an agent is doing the work. The motor system handles execution at agent scale, the source control, pipelines, and deployments that get software built and shipped. The nervous system gives every agent and human the context to make good decisions. The immune system puts proactive governance and security around every action.

And the orchestration system coordinates the other three, letting teams and their agents plan and carry out work across the full lifecycle. Whether the brain doing the work is human or agentic, it draws on all four.

At Transcend, we announced these innovations and a new buying program, and demonstrated how they come together with intelligent orchestration enabled by GitLab Duo Agent Platform.

SCM is the part of the platform worth focusing on here, because the Git backend buckles under agent load.

Git was built for a distributed workforce. We clone entire repositories to work on them, with branching and code merges scalable enough for hundreds of people around the globe to work in parallel. That model breaks when each team member runs hundreds of agents, resulting in:

That's why we previewed the next-generation SCM, [in private beta](https://about.gitlab.com/early-access-preview/). It runs on the Git protocol for backward compatibility, with a redesigned backend and interfaces built for agents. So you can run agents on any repo, fan them out by the thousands, and let them experiment safely.

Our team has been working to validate the architectural direction: same Git compatibility and auditability, with a different motor underneath, designed for agentic access from the start.

Early internal results are promising: up to 2x fewer tokens, up to 50x faster wall clock time, and up to 1,000x less network traffic.

Agents are adept at writing code and far less deft at navigating the system around it. They can see the code they're touching but not the full lifecycle, and that gap shows up as wasted work.

In a large monorepo, agents can burn too many iterations and too many tokens, and they take too long to get an answer. Across repos, they may fail outright as the context window fills and the agent gives up. The result is work that looks correct but gets reverted, and teams spending more time fixing agent output than the agent saved.

GitLab Orbit, [now in public beta](http://about.gitlab.com/gitlab-orbit), is the context graph for the entire software lifecycle. It continuously maps code, work items, pipelines, deployments, and production signals into a single live graph, so agents reason from first-party context instead of fragmented signals. Engineers query the same graph through the Data Explorer to trace changes and investigate incidents, which means every decision draws from one source of truth.

In our early internal tests, agents grounded with Orbit had up to 11 times faster response, were up to 4.5 times more cost effective, and had up to 45 times fewer hallucinations.

Our customer, Compare the Market, A/B tested GitLab Orbit against a RAG-based approach and a no-context baseline using identical prompts and models, and found: Graph-grounded agents placed inline review comments in the correct location 70% of the time (0.696 accuracy), vs. 58% (0.577) for RAG. Compare the Market validated the approach on 79 real merge requests, where graph-based context outperformed conventional retrieval on comment placement accuracy.


Build on Orbit at the Transcend hackathonWant to put Orbit to work yourself? From June 10-24, 2026, the Transcend hackathon invites the community to build with the lifecycle context graph. Contribute directly to the Orbit codebase, or build agents, flows, and skills on top of it and publish them to the AI Catalog.

Everyone is welcome, from experienced contributors to first-timers, and cash prizes are on the table.

[Learn more]

In the agentic era, the security and compliance exposure every team manages keeps multiplying. The faster agents ship code, the faster they ship the vulnerabilities that come with it. The cycle compounds: the more code agents generate, the more coverage gaps you uncover; the more you scan, the more findings you have to triage and fix; and the more agents you run, the more you need to prove each one did the right thing, under the right policy, to stand behind your risk posture.

That cycle is why, building on [GitLab Ultimate](https://about.gitlab.com/pricing/ultimate/), we've added agents for security and introduced governance for agents.

The agents for security work the exposure side: scanning, triaging, and resolving vulnerabilities as fast as agents create them, so the volume agents generate doesn't bury the teams responsible for securing it.

Governance for agents, [in private beta](https://about.gitlab.com/early-access-preview/), works the trust side. When agents push code, touch dependencies, and trigger deployments at scale, the question shifts from "did we scan?" to "which agent did what, under which policy, and can we prove it?"

Governance for agents puts identity, policy, audit, and approval around every agent action, with real-time visibility into inputs, reasoning, tool calls, and high-risk or anomalous activity across the organization. When something unexpected happens, the full execution context and audit trail are already there: what changed, which policy allowed it, and who signed off.

These capabilities above are infrastructure. [GitLab Duo Agent Platform](https://about.gitlab.com/gitlab-duo-agent-platform/) is the orchestration system that brings them together in the work developers do every day, and adoption has taken off: weekly active users have grown 10 times since we announced general availability in January.

The friction in software delivery was never the work itself, developers know how to write code, review it, and fix a pipeline. It's the context-switching, the waiting, and the handoffs between each of those steps, where time leaks out and focus breaks.

On GitLab Duo Agent Platform, agents work across that full loop: picking up a well-scoped issue and opening a merge request, reviewing it against the team's own rules rather than generic best practices, and resolving the review feedback that comes back.

The quality holds up against independent scrutiny. GitLab Duo Code Review placed in the top five of AI code review tools scored on the [Martian Offline Benchmark](https://codereview.withmartian.com/?mode=offline). And because these flows can run automatically on event triggers, a failing pipeline can be diagnosed and fixed without pulling multiple engineers out of flow, with the platform distinguishing a break that needs a code change from one that just needs a rerun.

The agentic era made your needs harder to predict, and the way you buy software hasn't caught up. Six months out, you don't know how many seats you'll need, how much AI your teams will consume, or which new capabilities you'll want to turn on, yet a traditional contract fixes all three up front and won't budge until renewal. Guess high and you pay for idle seats; guess low and adopting anything new means re-opening procurement.

That's what GitLab Flex, [available now](https://about.gitlab.com/blog/introducing-gitlab-flex/), solves. It's one annual commitment you reshape month to month across seats, AI usage, and new capabilities, all drawing from the same agreement, with no amendment and no new procurement cycle. When a team rolls off a project, you reallocate next month's reservations toward another team or toward AI. When a capability ships after you sign, you turn it on from the commitment you already have. Seats and usage live under one commitment, so you can move budget between them as adoption shifts. (For background on the usage-based foundation Flex builds on, see this introduction to [GitLab Credits](https://about.gitlab.com/blog/introducing-gitlab-credits/).)

**Read more: GitLab Flex: Commit once, reshape your seats and AI spend**

Agentic coding only gets you part of the way. The coding agent generates the change; GitLab's agentic infrastructure checks it against your full context, workflows, and guardrails and makes it safe to ship, at the speed agents work and the scale enterprises run.

GitLab Orbit is available now in public beta: join [the beta program](http://about.gitlab.com/gitlab-orbit). Next-generation SCM and governance for agents capabilities are in private beta, and you can [request early access here.](https://about.gitlab.com/early-access-preview/) Agents for security are available now in [GitLab Ultimate](https://about.gitlab.com/pricing/ultimate/). Duo Agent Platform is [generally available](https://about.gitlab.com/gitlab-duo-agent-platform/). Finally, GitLab Flex is accepting requests for orders now: To learn more, [get in touch](https://about.gitlab.com/pricing/).

Our mission is to unlock every team to ship trusted software at the speed of imagination, and we cannot wait to see what you build.
