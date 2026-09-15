---
source: "https://dev.to/tagkingiodeveloper/two-friends-pressed-play-at-the-same-time-and-both-got-a-bot-lessons-from-building-a-browser-1v1-2f39"
title: "Two friends pressed \"Play\" at the same time and both got a bot: lessons from building a browser 1v1 game"
author: "Thomas Botea"
date_published: "2026-09-14"
date_clipped: "2026-09-14"
category: "Game Development / Unity"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
---

# Two friends pressed "Play" at the same time and both got a bot: lessons from building a browser 1v1 game

Source: [Two friends pressed "Play" at the same time and both got a bot: lessons from building a browser 1v1 game](https://dev.to/tagkingiodeveloper/two-friends-pressed-play-at-the-same-time-and-both-got-a-bot-lessons-from-building-a-browser-1v1-2f39)

## Attributed article summary

A solo developer describes three failures in a small browser multiplayer game. Simultaneous matchmaking requests each created a waiting slot and then received bots because matching happened only at entry. Rechecking on polling, adding a deterministic claim ordering, and delaying bot fallback improved the matching flow.

An unordered WebRTC channel without retransmission still accumulated a send backlog. Checking buffered output and skipping stale position frames prevented delayed state from arriving in bursts. For real-time state, freshness can matter more than delivering every update.

The developer also exhausted a database read allowance with diagnostic queries, disrupting player sign-in. Bounded single-table queries and tracking rows read reduced the debugging footprint.

HoneyDrunk relevance: test concurrent queue entry, bound network buffering, and budget diagnostics alongside production traffic. This is a single-project experience report; any matchmaking implementation still needs atomic claims and explicit concurrency validation.
