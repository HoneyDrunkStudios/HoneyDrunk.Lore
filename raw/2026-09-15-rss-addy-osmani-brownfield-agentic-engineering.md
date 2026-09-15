---
source: "https://addyo.substack.com/p/brownfield-agentic-engineering"
title: "Brownfield Agentic Engineering"
author: "Addy Osmani"
date_published: "2026-09-14"
date_clipped: "2026-09-15"
category: "Software Architecture"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
discovered_via: "https://tldr.tech/tech/2026-09-15"
---

# Brownfield Agentic Engineering

Source: [Brownfield Agentic Engineering](https://addyo.substack.com/p/brownfield-agentic-engineering)

## Attributed content summary

Addy Osmani proposes making hidden constraints explicit before using agents to modify mature systems. He divides work by risk and evidence: well-isolated, well-tested areas permit tighter autonomous loops; uncertain areas need characterization tests; sensitive areas require close human involvement.

A separate research pass should produce a durable, cited comprehension memo covering entry points, owners, callers, tests, operational signals, and unresolved questions. Planning can then compare scope, preserved invariants, and reversibility. Review should start from acceptance criteria rather than merely confirming the generated implementation.

Document knowledge that is hard to infer from code, such as external commitments and historical tradeoffs. When the same correction recurs, encode it in a lint rule, type, hook, test, or reusable procedure where practical. Reusable research prevents later sessions from repeating the same investigation.

This is practitioner guidance, not a controlled productivity study. The applicable pattern is to expand autonomy with evidence about impact, visibility, and recovery, rather than with the model's stated confidence.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
