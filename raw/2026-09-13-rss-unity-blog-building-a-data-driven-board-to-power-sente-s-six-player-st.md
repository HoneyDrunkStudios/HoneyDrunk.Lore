---
source: "https://unity.com/blog/data-driven-board-six-player-strategy-sente"
title: "Building a data-driven board to power Sente’s six-player strategy"
author: "Fergus Baird - Unity Technologies"
date_published: "2026-08-13"
date_clipped: "2026-09-13"
category: "Game Development / Unity"
source_type: "rss"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# Building a data-driven board to power Sente’s six-player strategy

Original source: [Building a data-driven board to power Sente’s six-player strategy](https://unity.com/blog/data-driven-board-six-player-strategy-sente)

## Source-content summary

Unity interviews Oxobox Games about Sente, a strategy game that resolves up to six players' selected moves together when all players commit or a timer expires. The team describes repeated playtesting to avoid defensive stalemates.

A logical board representation is separated from scene rendering. The same representation powers templates, randomized boards, editor tools, and in-game editing. Boards can be encoded as strings, allowing a puzzle designer to create layouts through a spreadsheet without installing Unity.

The campaign uses custom Timeline tracks for dialogue, character expressions, camera splines, and animated board-state transitions. Signals and markers support branching and retries, while dialogue clips integrate localization.

HoneyDrunk relevance: reuse a serialized simulation model across authoring and runtime surfaces, and expose narrow content-creation tools to collaborators. This is an implementation interview, not a benchmark of the engine or multiplayer infrastructure.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
