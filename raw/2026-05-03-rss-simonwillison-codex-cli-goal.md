---
source: "https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything"
title: "Codex CLI 0.128.0 adds /goal"
author: "Simon Willison"
date_published: "2026-04-30"
date_clipped: "2026-05-03"
category: "Developer Tooling & AI Coding"
source_type: "rss"
---

**[Codex CLI 0.128.0 adds /goal](https://github.com/openai/codex/releases/tag/rust-v0.128.0)**

The latest version of OpenAI's Codex CLI coding agent adds their own version of the [Ralph loop](https://ghuntley.com/ralph/): you can now set a `/goal` and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted.

It looks like the feature is mainly implemented though the [goals/continuation.md](https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/continuation.md) and [goals/budget_limit.md](https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/budget_limit.md) prompts, which are automatically injected at the end of a turn.

Via [@fcoury](https://twitter.com/fcoury/status/2049917871799636201)

Tags: [ai](https://simonwillison.net/tags/ai), [openai](https://simonwillison.net/tags/openai), [prompt-engineering](https://simonwillison.net/tags/prompt-engineering), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [coding-agents](https://simonwillison.net/tags/coding-agents), [system-prompts](https://simonwillison.net/tags/system-prompts), [codex-cli](https://simonwillison.net/tags/codex-cli), [agentic-engineering](https://simonwillison.net/tags/agentic-engineering)
