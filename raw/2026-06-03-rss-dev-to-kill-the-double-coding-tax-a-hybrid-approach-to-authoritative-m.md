---
source: "https://dev.to/turnkit-dev/kill-the-double-coding-tax-a-hybrid-approach-to-authoritative-multiplayer-turn-based-games-1pn8"
title: "Kill the Double Coding Tax: A Hybrid Approach to Authoritative Multiplayer Turn-Based Games"
author: "Nenad Nikolić"
date_published: "2026-05-29"
date_clipped: "2026-06-03"
category: "Game Development / Unity"
source_type: "rss"
---

# Kill the Double Coding Tax: A Hybrid Approach to Authoritative Multiplayer Turn-Based Games

Source: https://dev.to/turnkit-dev/kill-the-double-coding-tax-a-hybrid-approach-to-authoritative-multiplayer-turn-based-games-1pn8

Making a multiplayer turn based game means making client side code (Unity, Godot, or whatever engine you use) and the server side. This leads to remaking same systems for all turn based games, turn enforcment and for most games some hand hiding system, in addition to networking, authentication and other must have features. Also validating every function on server side, so doubling the work.

Using Mirror, FishNet or similar frameworks helps reusing code, but it forces you into one game server for every game and that becomes expensive fast. Turn based server could handle thousands of games if its well optimised.

Using Relay servers can speed up development, but you still implement turn enforcment, hand hiding and they leave you open to hacking and players ruining your games.

**A Hybrid Approach That Cuts the Workload**

Here’s how it works:

- A specialized turn-based server handles the generic but critical parts that every game needs. Your client can simply react to clean events like “your turn started” or “turn changed”.
- Hand hiding (and other hidden data) is solved in a generic way: you define lists and visibility rules via client-side configuration. The server automatically creates and filters those lists so each player only sees what they’re allowed to see.
- Reconnecting players and other core features are handled reliably by the server.

This leaves you with only the specific game rules, which some simple games might not even need on the server. For more complex rules, you can use client voting consensus:

- Every client validates moves in the background (players don’t have to click anything). When a move arrives as an event, other clients check if it’s legal based on the game rules you already wrote for the client. The server accepts the move if enough clients agree.

I haven’t seen any solution that supports this hybrid pattern, so I built my own. It’s probably too niche for big companies, but it fits indie and solo developers really well.

You can try it yourself with the live demo:

https://turnkit.dev/live-demo

Or check the docs at: https://turnkit.dev/docs

This aproach, like any, does have its trade offs. Multiple client can hack together and outvote an honest player, but a match with multiple hackers is rare and already ruined usually. In a 1x1 match hacker can vote fail at end of the game when he is about to lose, so some reputation tracking system would be needed in this case.
