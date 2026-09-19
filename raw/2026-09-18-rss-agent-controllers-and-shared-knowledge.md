---
source: "https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/understanding-agents-their-five-controllers-and-one-graph"
title: "Understanding agents, their five controllers and one graph"
author: "Zichuan Xiong"
date_published: "2026-08-13"
date_clipped: "2026-09-18"
category: "Software Architecture"
source_type: "rss"
---

# Understanding agents, their five controllers and one graph

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Zichuan Xiong proposes a practitioner taxonomy for delegated agent judgment: prompts declare boundaries, instructions express goals, skills package procedures, recipes route those procedures, and loops correct behavior using external evidence.

Textual boundaries do not enforce themselves. Fixed procedures can fail when assumptions change, and routing adds the possibility of selecting the wrong procedure. The author reserves stronger feedback mechanisms for consequential cases.

A meaningful loop closes on an authority outside the agent's own assessment, such as a compiler, test suite, or human review. Weak validation signals can still produce confidently wrong outcomes, so choosing the terminating evidence matters as much as iteration.

Shared durable knowledge is presented as a separate axis: a graph preserves relationships and prior observations across runs, grounding the controllers rather than becoming another controller.

Lore relevance: distinguish guidance, orchestration, verification, and persistent knowledge when designing Honeyclaw workflows. The terminology is the author's conceptual framework, not a standardized agent taxonomy.

Source: [Original article](https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/understanding-agents-their-five-controllers-and-one-graph).
