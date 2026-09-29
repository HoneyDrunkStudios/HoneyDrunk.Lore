---
source: "https://www.thoughtworks.com/insights/blog/architecture/engineering-the-harness-a-practical-pattern-for-reliable-coding-agents"
title: "Engineering the harness: A practical pattern for reliable coding agents"
author: "Jaya Simha Reddy Nandyala, Prabina Pani"
date_published: "2026-09-29"
date_clipped: "2026-09-29"
category: "Software Architecture"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Thoughtworks describes a coding-agent harness with pre-action guidance, post-action checks, and selective human decision points. Guidance includes task-scoped instructions, progressive context loading, explicit defaults, and structurally limited tools. Checks include tests, type analysis, linting, and architecture rules.

The example follows a shared field across multiple services: passing local tests does not establish compatibility with downstream consumers. Impact analysis must identify the wider change before coordinated verification can be meaningful. Repeated failures of written rules are candidates for executable checks, and failed checks should return actionable evidence to the repair loop.

For HoneyDrunk, treat the harness as maintained software: version its rules, justify each constraint, and remove obsolete ones. This is an architectural proposal with an illustrative scenario, not measured proof that the suggested delivery phases improve outcomes. Human-gate placement remains a workflow design choice, not a universal approval mandate.

Source: [Original article](https://www.thoughtworks.com/insights/blog/architecture/engineering-the-harness-a-practical-pattern-for-reliable-coding-agents).
