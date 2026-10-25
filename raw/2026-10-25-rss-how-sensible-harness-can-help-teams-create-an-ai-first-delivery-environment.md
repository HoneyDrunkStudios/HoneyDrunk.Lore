---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/how-sensible-harness-help-teams-create-ai-first-delivery-environment"
title: "How Sensible Harness can help teams create an AI-first delivery environment"
author: "Vitória Regina Ragazzon Toebe, Amy Pellegrini, María José Lalama"
date_published: "2026-10-22"
date_clipped: "2026-10-25"
category: "Software Architecture"
source_type: "rss"
---

# How Sensible Harness can help teams create an AI-first delivery environment

* [Generative AI](https://www.thoughtworks.com/what-we-do/emerging-technology/genai)
* [Blog](https://www.thoughtworks.com/insights/blog)

By 

[Vitória Regina Ragazzon Toebe](https://www.thoughtworks.com/profiles/v/vitoria-regina-ragazzon-toebe)
,

[Amy Pellegrini](https://www.thoughtworks.com/profiles/a/amy-pellegrini)
 and

[María José Lalama](https://www.thoughtworks.com/profiles/m/maria-lalama)

Published: October 22, 2026

Unchecked AI code generation doesn’t reduce technical debt; it compounds it faster than review can absorb. The gap isn't a lack of generation capability, it's the absence of a governance harness to safely guide it. Sensible Harness aims to address that gap: it’s a single command-line interface (CLI) that transforms standard repositories into safe, governed AI-First software delivery and maintenance environments, by embedding Thoughtworks’ sensible defaults in a robust agentic workflow, plus a code audit feature that evaluates under Thoughtworks code quality standards.

The overarching vision for Sensible Harness is to become the tool to allow enterprises to scale AI adoption without compromising on software quality, security, or financial predictability.

Built during the Thoughtworks AI/works™ Global Hackathon 2026, Sensible Harness earned second place in the European regional semi-finals. It stood out for its innovative approach to team enablement in the Agentic AI software delivery era, integrating Thoughtworks' rigorous engineering standards into the tool capabilities.

In this blog post, we’ll take an in-depth look at its core capabilities and explore what makes Sensible Harness unique from existing market solutions.

## From zero to AI-FSD with a single command

At its core, an AI agent consists of two components: a model and a harness. Harness engineering treats this second component as a primary engineering artifact, one that is versioned, rigorously tested and peer-reviewed with the same diligence as application code. Sensible Harness takes that literally. Skills are not loose prompt files, they have a single source of truth in templates, a renderer that compiles them, committed outputs, a CI job that fails on template drift and unit tests that assert on the prose itself.

Designed to deliver immediate value across software engineering projects, one command scaffolds everything the agents need: agent guidelines that don't depend on any one runtime, skills files and a shared state manifest that acts as the single source of truth. It works with the AI-assisted tooling and issue trackers teams already use, and the onboarding capability walks new users, technical and non-technical, through the agents, the skills and the codebase context.

What sets Sensible Harness apart from other market tools is its built-in code audit capability. Grounded in Thoughtworks' three decades of software engineering expertise, it delivers precise evaluations and actionable reports that identify clear gaps, effectively guiding teams toward improved code quality.

It grades the codebase from A to F across 10 dimensions, from documentation and test quality to security, observability and AI governance. Each dimension gets its own Markdown report, plus interactive HTML diagnostics. The scores measure the repository against its own documented standard instead of generic defaults. The result answers a practical question: *is this codebase ready to hand over to AI agents, and what should we fix first?*

## Three agents that ask before they act

Sensible Harness equips teams with three agents with specialized skills, ready to use with a command in their terminal.

The **business analyst** agent turns findings, notes and requirement refinement transform into complete user stories. Every Jira operation routes through named primitives in the jira skill rather than reconstructed CLI commands. And when a ticket lacks sufficient detail, the delivery process brings [humans in the loop](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html) using the [socratic prompting method](https://arxiv.org/abs/2303.08769) to gather the missing information instead of on guesswork.

![María José Lalama, Thoughtworks](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/thoughtworker-profile/m/pro_maria_jose_lalama2.jpg "María José Lalama, Thoughtworks")

> "Seeing codebase assessment findings automatically converted into structured Jira stories is time-saving, and when the BA agent uses socratic prompting to clarify requirements prior to writing the user story, makes this tool valuable for technical and non-technical team members”"

María José Lalama

AI/works™ Product Researcher, Thoughtworks

The **developer agent** picks up a ticket and drafts a plan whose steps name the primitive, the model and the execution mode, with each acceptance criteria quoted verbatim. The human approves the plan before any code exists, and the approved plan is posted as a comment on the issue, where it survives the session as the handoff artifact. The implementation executes a TDD cycle per acceptance criteria, one atomic conventional commit per cycle, then pull request, CI check, review-comment handling and close. Nine gates run across the loop, including acceptance-criteria verification against the diff and a CI checkpoint after the pull request opens and again after comments are addressed.

The **quality analyst agent** checks the branch, builds a test plan from the acceptance criteria, runs the feature and posts its assessment with a recommendation on both the issue and the pull request. If it can't execute a scenario, it marks it blocked, never passed and comes back to the human for review.

The boundaries between the three agents are enforced strictly through the Sensible Harness framework itself. By embedding these boundaries directly into the architecture rather than relying on only system prompts, the framework guarantees that all requirements refinement, code changes and test cycles strictly keeps human-in-the-loop approval checkpoints.

## How we keep AI agent costs visible, ticket by ticket

Agentic delivery that nobody can price won't scale.

Sensible Harness pins a model to every skill. Work that needs complex reasoning, such as creating tests or verifying acceptance criteria, gets a high-capability model. Routine actions, such as committing, pushing and opening pull requests, get a lightweight one. Main agents plan and sub-agents execute, which keeps that routing correct. After each task, the harness calculates the cost from model rates and posts a cost report to the ticket.

![Vitória Toebe, Thoughtworks](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/thoughtworker-profile/v/pro_vitória_toebe.jpeg "Vitória Toebe, Thoughtworks")

> "Splitting tickets into small tasks does more than save money. The report shows what each task costs, so we know where the money goes, and that becomes feedback we use to improve the harness."

Vitória Toebe

AI-First Maintenance and Operations Lead, Thoughtworks

In contrast to other solutions on the market, Sensible Harness embeds cost tracking as a core feature from day one, giving product managers and business analysts actionable data to evaluate both ticket estimations and actual per-ticket work expenses.

## What we’ve learned building Sensible Harness

Since the Thoughtworks AI/works™ Global Hackathon 2026, we’ve conducted tool demonstrations across various repositories to onboard Thoughtworkers to it. Feedback gathered from every session continuously drives enhancements, incorporating new capabilities, specialized skills and guardrails tailored to the practical needs of our delivery teams.

We’ve learned that standards hold when they’re enforced as gates the agent can’t skip, not offered as guidelines it might follow. That’s key if you are also building your own harnesses. Teams also trust the output much more when a human approves the plan before any code is written. And keeping token spend visible per task turns AI cost from a guess into a number teams can manage.

Sensible Harness is how we put those lessons into practice. We use it internally to deliver software with AI while holding to Thoughtworks engineering standards, from the first requirement through to a reviewed, tested pull request.

**If you’d like to see it in action, we run walkthroughs of the tool and talks about AI-First delivery for technical and non-technical teams.**
