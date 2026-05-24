---
source: "https://x.com/athleticKoder/status/2057091692235481560"
title: "On Building Agents From First Principles (15 minute read)"
author: "TLDR AI"
date_published: "Thu, 21 May 2026 00:00:00 GMT"
date_clipped: "2026-05-24"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-05-21"
source_role: "primary-via-tldr"
---

# On Building Agents From First Principles (15 minute read)

Source: https://x.com/athleticKoder/status/2057091692235481560

Mishra strips away the TRL, Unsloth, and PRIME-RL framework abstractions to show that every agent-training system reduces to the same loop: prompt to model action to environment to reward to gradient update. He builds a toy tldraw-style text-to-diagram agent in pure Python where the model emits JSON create_shape and connect actions against a validating canvas, then layers a reward function combining JSON validity, schema compliance, layout quality, and semantic coverage of prompt keywords.
