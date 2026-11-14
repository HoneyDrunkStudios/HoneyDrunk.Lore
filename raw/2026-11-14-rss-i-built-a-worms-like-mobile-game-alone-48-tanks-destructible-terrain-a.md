---
source: "https://dev.to/cpcai_studio/i-built-a-worms-like-mobile-game-alone-48-tanks-destructible-terrain-and-the-parts-that-actually-3mg7"
title: "I built a Worms-like mobile game alone: 48 tanks, destructible terrain, and the parts that actually took the time"
author: "Youngjun Yoon"
date_published: "2026-11-14"
date_clipped: "2026-11-14"
category: "Game Development / Unity"
source_type: "rss"
---

# I built a Worms-like mobile game alone: 48 tanks, destructible terrain, and the parts that actually took the time

Turn-based artillery looks like a simple genre from the outside. You have a tank, you have a bar for angle, a bar for power, and a wind arrow. You fire. That's the whole interface.

It is also the genre where the shot *is* the game. Nothing else you build matters if the first twenty shots don't feel readable — if the player can't tell why a shell landed short, they won't take a second shot. So most of my work went into making the shot explain itself, and only then into content.

I shipped **Cannon King: Wind Tank Battle** on Google Play and the App Store this month. One person, one Flutter codebase, no team, no publisher. Here is what that actually involved.

## What the game is

- **48 tanks**, from Normal through Rare, Epic, Legend, up to a top grade called MAGNUM, each with its own shell and its own skill, and step-by-step evolution between grades.
- **20+ maps** with destructible terrain — Volcano Island, Sky Islands, Moon Base, Steel Fortress, and more.
- **53 stages** of a single-player adventure following the legend of the ancient kingdom of Abinus, plus trial sorties that let you borrow a tank before you unlock it.
- **Real-time 1v1**: Quick Match, rooms with friend invites, free-for-all, team modes, and a no-item mode. If the connection drops mid-match, the match resumes instead of ending.
- A **4-slot item loadout** you set before each battle: teleport, power shot, heal, shield.
- Credits, gacha, and coupon redemption.

Three to five minutes per match, on a phone, held vertically.

## 1. Making the shot readable

In a Worms-style game, wind is the whole tutorial. If the player has to guess what a 12 km/h crosswind will do to a heavy shell at full power, the game is a coin flip with extra steps.

What made the difference was not the trajectory math. It was the *preview* — showing the arc before the shot, with the wind already in it — plus keeping the numbers small enough that a human can reason about them. Angle, power, and wind are three dials; if any of them has a range of 400, none of them is a dial anymore. Constraining the ranges is a design decision that a physics engine won't make for you.

The second half is a consistent lie: every shell has to behave the way its visual suggests. A heavy shell that ignores wind visually but not mechanically destroys trust faster than bad balance does.

## 2. Destructible terrain is a content multiplier

The first time a map is played, the terrain is decoration. By turn three, it is the board: a crater opens a firing line, a tower of dirt disappears and the tank standing on it falls, cover that existed at the start is gone.

That means 20 maps is not 20 maps. It is closer to "20 starting positions", and the level design job changes: instead of asking "does this layout look good", the question becomes "does this layout produce interesting terrain after two exchanges". Some of my early maps looked great in the editor and turned into a flat field by turn four, which makes every tank identical and every match a dice roll.

The maps that survived are the ones with layered terrain — something to destroy above, something solid below, and a reason to want the high ground.

## 3. Turn sync that survives a subway

A real-time 1v1 turn-based game has an awkward constraint: the game is turn-based, but two people are connected live. A dropped connection must not cost a turn, and it must not let a player fire twice.

The model I use is an ordered event log per match. A shot is an event with a sequence number; applying it twice is the same as applying it once, and a client that reconnects replays from the last sequence it acknowledged. Physics stays deterministic on both sides, so no one has to ship the whole world state across the wire — just the input and the seed.

The nice side effect: replays are free. The log *is* the replay.

## 4. 48 tanks without power creep

Gacha games drift. Every new grade has to be stronger than the last one or nobody pulls, and after ten of those the bottom half of the roster is decoration.

What I tried to do instead: grades unlock *versatility*, not raw damage. A lower-grade tank with a specific skill (a lobbed shell that clears cover, a wide blast that punishes clustering) stays useful in the modes and maps where that skill is the answer. The trial sortie exists for the same reason — you should be able to feel whether a tank solves a problem you have before spending anything on it.

Whether that holds at the top of the ladder is the part I can't answer alone yet. It's the kind of thing that shows up in real match data, not in my spreadsheet.

## 5. The iOS part is not the code

One Flutter codebase shipping to Android and iOS is real, and it's the reason this was possible for one person. The build was nearly free. What isn't free is everything around it:

- Store metadata in several languages, written by hand, several times as I reworded things.
- Screenshots per device size, each one cropped to show the game rather than the UI chrome.
- Two review processes that ask questions in different vocabularies, and a review queue that doesn't care that you're one person.

The Android side had been live for a while, so iOS was mostly a second pass through a checklist I already knew. If I had started on both at once, it would have been roughly one checklist done twice at the same time instead of twice at different times. That is the whole trick, and it isn't clever.

## What's next

The game is free, both stores are live, and my next job is the least glamorous one: watching where players actually stop — which stage, which map, which tank they never touch — and fixing that before adding anything new.

If you play it, the feedback I can use most is this: **which map is the hardest to read?** Not the hardest to win. The one where you couldn't tell what your shot would do.

- Google Play — <https://play.google.com/store/apps/details?id=com.cpcai.potanwang>
- App Store (iOS) — <https://apps.apple.com/kr/app/id6827588104>
- Launch coupon: **POTANKING2027** — 5,000 credits + 10 Premium Draw Tickets, once per account, valid until 2027-12-31. Enter it in the game's coupon screen.

In Korea the game also runs as a mini app inside Toss.

One last practical note, since I'm a one-person studio and someone always asks how: I keep the backlog and the dev log with an AI assistant called Pickle, which is how a game, a store submission and a support inbox stay in one head. Invite if you want one: <https://pickle.com/i/SJWDRVNKFDSY>
