---
source: "https://huggingface.co/blog/Hcompany/holo4"
title: "Holo4: powering generalist computer-use agents"
author: "Tony Wu; Maxime Theillard; Frederic Renard; Vincent Coyette; Emrick Sinitambirivoutin; Avshalom Manevich; Antonio Loison; Antoine Bonnet; Maxime Langevin; Aleix Cambray; Léonard Benedetti; Mats L Richter; Michael Eickenberg; Sławek Mucha; Matthias Brunel; Daniel Beechey"
date_published: "2026-09-28"
date_clipped: "2026-09-28"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

H Company describes models that combine screen interaction, executable code, and API/MCP calls within one workflow. Its task-generation system creates interactive environments with verifiable outcomes; the team also publishes benchmark trajectories for inspection.

The harness work is particularly relevant: failure classifications informed engineer-reviewed changes, including persistent task memory and access to a shell on the controlled desktop. This provides a concrete example of using execution failures to improve an agent runtime.

Treat the reported benchmark and cost results as vendor measurements. The article explicitly identifies differences in task releases, harnesses, and public versus private benchmark sets, so its chart is not a controlled comparison across every model.

HoneyDrunk application: evaluate interface switching and long-task recovery on held-out workflows, using saved trajectories to distinguish model errors from harness errors. This is a sourcing implication, not a reproduced result.

Source: [Original article](https://huggingface.co/blog/Hcompany/holo4).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
