---
"source": "https://dev.to/remi_bouvant_4fdbf8738ec6/an-escape-game-on-the-tv-played-with-phones-keeping-5-screens-in-sync-3p2i"
"title": "An escape game on the TV, played with phones: keeping 5 screens in sync"
"author": "REMI BOUVANT"
"date_published": "2026-10-17"
"date_clipped": "2026-10-17"
"category": "Game Development / Unity"
"source_type": "rss"
---

# An escape game on the TV, played with phones: keeping 5 screens in sync

Since early October I've had [Nocturne au musée](https://escape-chill.fr/jeux/nocturne?utm_source=devto&utm_medium=article&utm_campaign=tech) online: an escape game you play together in front of the TV. The TV (or a computer) shows the museum, each player joins by scanning a QR code with their phone, and gets documents the others don't have. To move forward, you have to talk to each other. The game is in French, but the architecture isn't.

Here are the technical choices, because the problem is more interesting than it looks: up to five screens must show the same game at the same moment, some screens hold secret information, and nobody should be able to cheat by opening the browser dev tools.

## The setup

* Nothing to install: everything runs in the browser, on the TV and on the phones.
* No account for players: a game code is enough.
* A remote mode: everyone at home, the same video on every screen, and the team talks on a call next to it.

The stack: Next.js (App Router) for the site and API routes, Supabase for the database and realtime, Stripe for payments, Cloudflare R2 for videos, Three.js for the 3D rooms. I designed the game and its architecture, with AI helping me write a good part of the code.

## One referee: the server

The first temptation with realtime is to let each screen publish its actions and let the others update. That works for a chat, not for a game with answers to hide.

I did the opposite: no screen changes the game directly. A player who types a code, turns a dial or puts a weight on a scale sends an **action** to an API route. On the server, a small engine:

1. reads the full game state (answers included);
2. applies the action;
3. saves the new state **with a version number**.

If two players act in the same split second, the second save fails because the version changed. The engine then reloads the fresh state and replays the action on it. It's plain optimistic locking, done by a SQL function that only writes if the expected version is still current. No queue, no lock to release.

## Two states: public and private

The server never broadcasts the full state. It derives a **public state** from it: the current room, solved puzzles, the timer, the documents the team chose to pin on the investigation board. No answer is in there.

What belongs to a single player (their documents, their hints, the piano keys or weights assigned to them) goes through another route, which checks the player's identity before answering. The phone calls it again every time the game moves forward: new room, new hint, new find. To know when, it compares a small key built from the public state (room number, step, number of hints…) with the previous one.

Result: even reading all of their phone's network traffic, a player only sees what their role gives them.

## Broadcasting

After each successful save, the server sends the public state on a Supabase Realtime channel dedicated to the game. The channel is **private**: screens can listen, not publish. So nobody can inject a fake state from the browser console.

The message is sent over HTTP from the API route, without keeping a connection open on the server, which fits serverless hosting well.

## Playing the same video on five screens

Between rooms, videos move the story forward. In remote mode everyone must see the same frame at the same time, otherwise one person laughs at a scene the others haven't seen yet.

Instead of syncing the players with each other, the public state describes the playback:

```
type Playback = { src: string; startedAt: number | null; offset: number; paused: boolean; rate?: number };
```

Each message also carries the server time (`serverNow`). Every screen computes where it should be:

```
function videoPosition(v: Playback, serverNow: number) {
  return v.paused || v.startedAt === null
    ? v.offset
    : v.offset + ((serverNow - v.startedAt) / 1000) * (v.rate ?? 1);
}
```

A screen that falls behind catches up on its own, and a player who reloads the page resumes at the right spot. Pausing and speeding up are just changes to `startedAt`, `offset` and `rate`.

## The timer

The displayed time follows the same idea: it's computed from the start time, minus pauses, minus story sequences (a team shouldn't be penalised because a video lasts two minutes), plus hint penalties. No screen "runs" the timer: each one recomputes it from the state.

## Gestures seen twice

In remote mode, the same gesture can be seen by several screens. For example, the game counts "noise" when the team searches at random: at the third noise, the night guard complains and the timer takes a penalty. If every screen reported the same noise, one gesture would count several times. So each gesture carries an id, and the server only counts an id once.

## Videos and their cost

Videos are heavy and watched by the whole team. They're stored on Cloudflare R2, which doesn't charge for egress. The browser never gets their direct address: it goes through a route that checks the game (and the purchase for paid rooms), then redirects to a temporary signed URL.

One detail that mattered a lot: the signing date is rounded to the hour. The same URL is valid for an hour, so the browser keeps the video in cache between reloads instead of downloading it again.

## The 3D rooms

Each explorable room is a small standalone Three.js page, modelled in Blender. The TV shows it in the dark, and each player moves their own flashlight across it by sliding a finger on their phone, which is why you see several beams on screen. Keeping them separate from the rest of the app means they only load when the team enters the room.

## What I'd keep

* A server referee and screens that only display: less "realtime" on paper, much easier to get right.
* Describing a state (a video started at a given time) rather than events ("play", "pause") avoids almost every desync problem.
* Splitting public and private state from day one, instead of hiding fields afterwards.

If you want to see the result, the first room is free to play, no account needed: [escape-chill.fr](https://escape-chill.fr/jeux/nocturne?utm_source=devto&utm_medium=article&utm_campaign=tech). Happy to answer architecture questions in the comments.
