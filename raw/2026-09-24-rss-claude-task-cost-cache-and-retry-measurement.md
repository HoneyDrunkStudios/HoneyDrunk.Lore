---
source: "https://claude.com/blog/what-a-task-costs-on-opus-5-5"
title: "What a task costs on Opus 5.5"
author: "Addy Osmani"
date_published: "2026-09-22"
date_clipped: "2026-09-24"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_method: "attributed-summary"
discovered_via: "https://tldr.tech/ai/2026-09-23"
---

# What a task costs on Opus 5.5

Attributed summary of the fetched article.

Addy Osmani separates token price from the cost of completing a task. Repeated turns resend growing context; caching, reasoning output, failed approaches, and subagent model choices all affect the bill. Cheaper individual calls can lose their advantage when they require retries.

The article recommends comparing the same tasks using recorded session usage, providing executable checks, and adjusting effort according to observed failure patterns. Cache writes, model changes, and context compaction introduce costs that simplified examples can omit. Compaction also loses detail, so timing and retained instructions matter.

HoneyDrunk application: compare accepted outcomes, turns, cache reads/writes, and output tokens across representative agent jobs. Treat calculator examples and the reported prompt-audit benchmark as illustrations rather than expected savings. Published prices are a dated snapshot; verify billing documentation before budgeting.

Source: [Original article](https://claude.com/blog/what-a-task-costs-on-opus-5-5).
