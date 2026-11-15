---
source: "https://dev.to/codiologism/how-we-made-battles-deterministic-and-server-verified-in-a-telegram-mini-game-26l2"
title: "How we made battles deterministic and server-verified in a Telegram mini-game"
author: "Saleh Nouri"
date_published: "2026-11-15"
date_clipped: "2026-11-15"
category: "Game Development / Unity"
source_type: "rss"
---

# How we made battles deterministic and server-verified in a Telegram mini-game

We are building Seraph Legion, an angel-collector RPG that runs inside Telegram as a Mini App. This is a writeup of the most interesting engineering decision in the project: **how battles work**, and what a farming exploit taught us about trusting clients.

## The constraint

A Telegram Mini App is just a webview. Anything your client computes, a motivated player can fake - the JS is right there, the API is a plain HTTPS endpoint. So the design contract from day one:

> The request body selects *what* the player wants to do. The server decides *how much* they get.

## Deterministic battles

The entire battle simulator lives in a pure TypeScript core ("game-core") shared between client and server:

- **Seeded RNG.** Every fight derives its randomness from a seed generated at battle/start. No Math.random(). The seed, the team composition, and the data tables fully determine the outcome.
- **Pure functions.** Given the same inputs, the sim produces the same turn-by-turn log - on the client, on the server, in tests, everywhere.
- **Replay verification.** When the client calls battle/finish, it reports what it thinks happened. The server re-runs the sim with the same seed and inputs and compares. Report matches the replay? Rewards are computed server-side from the data tables and written to the ledger. Mismatch? Rejected.

The client still runs the full sim for the visual battle experience - animations, turn order, damage numbers. It just does not get to decide the result.

## The exploit that hardened everything

We had one endpoint that broke the contract: a migration importer for players coming from a prototype build. It accepted declared progress and clamped it generously (gold under a big cap, gems under a smaller one).

A farm of ~23 accounts, all from one IP, hit it within a half-hour window and minted themselves millions in currency.

The fix went deeper than closing the endpoint:

- The import route is now **sealed by default** - admin flips a switch for supervised stragglers
- Registration IP is captured at auth; shared-IP cohorts get flagged
- An anomaly scanner watches for plush balances vs account age and ledger drift (stored points vs the ledger sum)
- Everything suspicious lands in a review queue - flag, never silently allow

Every other write path was already server-verified - summons, quests, raids, ads, sweeps. The farm found the one door we had left unlatched.

## Takeaways

1. **Deterministic sims are cheap anti-cheat.** If your game logic can run identically on both sides, replay verification costs almost nothing and defeats result forgery completely.
2. **The body is a wish, not a fact.** Keep every currency/progress column out of reach of request values.
3. **Assume a farm, not a cheater.** The expensive attacks are scripted multi-account, not one player hex-editing.

The game is live at [seraphlegion.com](https://seraphlegion.com) - happy to answer questions about the sim or the TON jetton work.
