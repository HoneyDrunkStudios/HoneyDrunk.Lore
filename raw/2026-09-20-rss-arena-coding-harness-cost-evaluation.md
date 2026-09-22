---
source: "https://arena.ai/blog/coding-agents-harness-tax"
title: "HarnessTax: How Much Does the Harness Matter for Coding Agents?"
author: "Arena Team"
date_published: "2026-09-16"
date_clipped: "2026-09-20"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# HarnessTax: How Much Does the Harness Matter for Coding Agents?

Source: [HarnessTax: How Much Does the Harness Matter for Coding Agents?](https://arena.ai/blog/coding-agents-harness-tax)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

Arena compares seven models across Claude Code, Codex CLI, and Pi on SWE-bench Lite and Terminal-Bench 2.0. Each pairing runs three attempts on the same 30 sampled tasks per benchmark. Costs use a fixed API price list; success uses the benchmarks' evaluators.

The study finds that harness choice can change token cost substantially while measured success stays similar. It therefore recommends evaluating model and harness together. A provider's own harness is not automatically the best measured pairing, and a small tool set can remain competitive.

Interpretation requires the experimental limits: public benchmarks may have appeared in training; effort levels and turn counts follow each harness's definitions; a 100-turn cap affects long attempts. Results do not establish equivalent security, usability, or effectiveness on private, extended projects.

HoneyDrunk relevance: compare cost per successful task using representative repository work and repeated runs before changing agent infrastructure. Keep operational requirements separate from benchmark scores.
