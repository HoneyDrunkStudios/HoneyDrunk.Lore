---
source: "https://dev.to/rencoreballnotes/preventing-double-merges-in-a-fruit-drop-physics-game-3kla"
title: "Preventing Double Merges in a Fruit-Drop Physics Game"
author: "Ren Coreball Developer"
date_published: "2026-09-20"
date_clipped: "2026-09-20"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# Preventing Double Merges in a Fruit-Drop Physics Game

Source: [Preventing Double Merges in a Fruit-Drop Physics Game](https://dev.to/rencoreballnotes/preventing-double-merges-in-a-fruit-drop-physics-game-3kla)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

The author explains an overlapping-contact bug in a fruit-merging physics game: contacts involving A/B and B/C can both schedule work before B is removed. Checking existence only after deferral does not establish exclusive ownership.

The implementation synchronously reserves both body identifiers before scheduling the mutation, then rechecks that both bodies still exist when the callback runs. A reset can invalidate queued work. Pure rules distinguish ordinary evolution, final-tier clearing, and no action.

Reservations prevent double consumption but do not guarantee deterministic simulation; contact ordering and timing still matter. Browser animation callbacks also are not physics transaction boundaries, so replay or background simulation may require an engine-controlled mutation queue.

The author reports seven passing rule tests while distinguishing them from missing integration evidence for overlapping callbacks and resets. The post discloses AI-assisted drafting.

HoneyDrunk relevance: separate state-transition rules from ownership and scheduling, and test cancellation and competing-event behavior independently.
