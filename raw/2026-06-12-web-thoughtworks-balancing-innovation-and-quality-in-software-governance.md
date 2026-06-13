---
source: "https://www.thoughtworks.com/insights/blog/technology-strategy/balancing-innovation-quality-software-governance"
title: "Balancing innovation and quality in software governance"
author: "Lilly Ryan"
date_published: "2026-06-08"
date_clipped: "2026-06-12"
category: "Software Architecture"
source_type: "web"
---

# Balancing innovation and quality in software governance

Tackling AI-accelerated shadow IT

[Blogs
Back](/insights/blog)

Close

- [Technology strategy](https://www.thoughtworks.com/insights/topic/technology-strategy)
- [Generative AI](https://www.thoughtworks.com/what-we-do/emerging-technology/genai)
- [Blog](/insights/blog)

By

[Lilly Ryan](/profiles/l/lilly-ryan)

Published: June 08, 2026

Over the last few years, the narrative surrounding generative AI in enterprise software has largely been one of velocity. We talk about [coding agents](https://www.thoughtworks.com/radar/techniques/team-of-coding-agents), autonomous multi-agent workflows, and [self-serve UI prototyping platforms](https://www.thoughtworks.com/radar/techniques/self-serve-ui-prototyping-with-genai) as the new infrastructure of productivity. However, beneath this veneer of hyper-acceleration, a familiar ghost has returned to haunt enterprise corridors. This time, though, it’s moving at machine speed.

## A new kind of shadow

In the recent editions of the Thoughtworks Technology Radar, a particularly telling entry was placed firmly in the Caution ring: [AI-accelerated shadow IT](https://www.thoughtworks.com/radar/techniques/ai-accelerated-shadow-it).

For decades, IT departments have engaged in a perpetual game of whack-a-mole against unauthorized Excel macros, rogue SaaS subscriptions, and literal servers running in secret under someone’s desk. But as the Radar highlights, we’re not just dealing with shadow tools any longer: because AI makes it trivial for individuals to quickly stitch together complex capabilities, we’re witnessing the evolution of entire shadow systems.

With the rise of standardized integration protocols like the [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) and agentic frameworks, a motivated employee can today construct an autonomous workflow that pulls data from a core repository, processes it through a public LLM, and triggers external APIs, and they can do this with some plain-language prompting over a long weekend.

> "Shadow IT is often a lagging indicator of unmet organizational demand. It’s a mirror reflecting exactly where your internal processes might not be keeping pace with the real-world operational needs of the business."

Lilly Ryan

Principal Cybersecurity Engineer

> "Shadow IT is often a lagging indicator of unmet organizational demand. It’s a mirror reflecting exactly where your internal processes might not be keeping pace with the real-world operational needs of the business."

Lilly Ryan

Principal Cybersecurity Engineer

## Shadow IT is an expression of need

Understanding why this pattern emerges in practically every organisation comes back to human nature: most people just want to get their jobs done. When engineers, product managers, or business analysts bypass formal channels to deploy an AI assistant or wire up an LLM using a personal API key, it’s rarely driven by malice or an active disregard for security; it often comes from a deep (and very human!) frustration with existing friction.

Shadow IT is often a lagging indicator of unmet organizational demand. It’s a mirror reflecting exactly where your internal processes might not be keeping pace with the real-world operational needs of the business.

When an organization makes the ‘official’ path to deploying technology too bureaucratic, teams will inevitably route around it. AI hasn't created this desire to bypass the system, but it has supercharged the capability to do so.

## The shifted bottleneck

This phenomenon highlights an asymmetry that most modern enterprises are currently grappling with. While AI tools have effectively reduced the cycle time of creating functional automation from weeks to minutes, business governance infrastructure like security reviews, procurement cycles, and change advisory boards (CABs) are still evolving to meet this need, and have constraints that mean they can’t always match code generation speed.

This isn’t a simple case of governance being too slow, even if that is how it’s often interpreted. Shadow practices and tools will always be faster because long-term maintenance considerations are not usually as much of a priority for these tools as short-term delivery and output are. While a lot of governance processes can absolutely benefit from streamlining (including looking at their own use of AI tooling), most laws don’t change very quickly, and financial and security realities can’t just be imagined away. Governance speed is not set by the business alone.

For businesses, it’s important not to punish efforts to solve problems and deliver quickly, but instead to listen to these activities as desire signals that should be pragmatically incorporated and accounted for in the way tools are procured and governed. And it’s not a bad time to learn from colleagues who are rapidly prototyping, and look at how to update these procurement and governance frameworks, too.

## Balancing speed with quality and resilience

The danger of AI-accelerated shadow IT extends far beyond data leakage, though the potential compliance and security exposures are undeniably severe. The deeper architectural threat is what the most recent Technology Radar warns against: [codebase cognitive debt](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt).

When functional workflows are spun up at machine speed without human developers building the foundational mental models to understand how they work, the system becomes incredibly brittle. Such shadow systems are often built with:

- Fragile, unversioned prompts acting as implicit business logic
- Zero telemetry, logging, or observability
- An absence of quality gates like automated unit testing, evals, or architectural fitness functions

They work beautifully in the moment, until a foundational model's behavior subtly shifts, or an undocumented API schema changes. Because there’s often no [engineering discipline](https://www.thoughtworks.com/insights/blog/agile-engineering-practices/where-does-the-rigor-go) behind their construction, when these systems fail they often do so silently and catastrophically, leaving organizations reliant on automated processes that no one actually knows how to debug. These are some of the issues that enterprise governance infrastructure exists to anticipate and protect against, but ensuring the existence of those safeguards in systems that are intended to handle sensitive data, or intended to underpin business processes, is also some of why these governance steps add time to deployment.

## From gatekeepers to paved roads

The traditional enterprise reflex to shadow IT is to issue blanket bans, block API access, and write stricter corporate policies. As with any attempt at prohibition, however, this rarely succeeds in stopping the behavior; more often, it drives it deeper underground.

Instead, technology leaders need to transition from a posture of gatekeeping to one of enablement. The most sustainable response to shadow IT is to lower the friction of compliance by building paved roads (sometimes called [golden paths](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/engineering-platforms-golden-paths-building-better-developer-experiences)). The details of these will look different in every organization’s context, but they will regularly take the following three things into consideration:

- Hardened, pre-audited, internal self-service platforms where teams can leverage LLMs, host agents, and use tools like MCP safely. If accessing corporate-approved AI infrastructure is easier than putting a personal credit card down for an external API, teams will choose the approved route.
- Automated quality checks embedded directly into the delivery lifecycle. Wire compilers, linters, and security scanners directly into agentic workflows so that validation happens continuously and programmatically.
- Prioritization of risks by use case. A locally-run utility that summarizes internal meeting transcripts does not normally need the same evaluation process as an autonomous agent interacting with customer financial data.

AI-accelerated shadow IT isn’t, fundamentally, a technology problem, but one of organizational architecture. The individuals building these workarounds are sending a clear signal to their businesses: they possess the drive to innovate, but the company’s official roads are not always leading where they want to go, and they’re sometimes waylaid by administrative checkpoints.

The job of a thoughtful software leader today isn’t to build higher walls to keep the shadow systems out, but to renegotiate the checkpoints and provide more paved roads to guide that creative energy toward safe and resilient infrastructure.

- [Security

  So, you want to run OpenClaw?

  Learn more](/insights/blog/security/want-run-openclaw)
- [Security

  Anthropic Mythos Preview: Faster patching isn't enough

  Learn more](/insights/blog/security/anthropic-mythos-preview-faster-patching-isnt-enough)
- [Generative AI

  Does every feature we build with AI need a token budget?

  Learn more](/insights/blog/generative-ai/does-every-feature-build-ai-token-budget)

[View more](javascript:void(0))

[View less](javascript:void(0))

## Explore a snapshot of today's tech landscape

[Read Technology Radar](/radar)
