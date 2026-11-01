---
source: "https://dev.to/chromealex/220000-units-instead-of-4000-and-other-production-stories-from-mushroom-wars-2-8o6"
title: "220,000 Units Instead of 4,000 and Other Production Stories from Mushroom Wars 2"
author: "Alex Silaev"
date_published: "2026-10-31"
date_clipped: "2026-11-01"
category: "Game Development / Unity"
source_type: "rss"
---

# 220,000 Units Instead of 4,000 and Other Production Stories from Mushroom Wars 2

Source: https://dev.to/chromealex/220000-units-instead-of-4000-and-other-production-stories-from-mushroom-wars-2-8o6

Almost every story below started with code that worked until it didn't. These are real cases from Mushroom Wars 2, an RTS where thousands of units run around on a phone screen at once, and which we shipped on PS4, Xbox One, Switch, iOS, Android and PC. For each story: what broke, how we found it, what we did, and what the numbers were.

## 1. Garbage collection in the middle of a battle

**The problem.** Mushroom Wars 2 is a fast-paced strategy game, and any hitch ruins the feel. Garbage collection mid-battle caused noticeable stalls, especially on consoles (PS4, Switch).

**How we found it.** At first the freezes were visible with the naked eye. The Unity profiler and the console's native profiler showed that the stalls lined up with `GC.Collect`. On those platforms a collection could take up to a couple of seconds.

**What we did.**

1. Moved all gameplay code to object pools: not a single managed object is created during a battle.
2. Disabled the GC before a battle, then re-enabled it afterwards and collected manually on the results screen, where the pause goes unnoticed.
3. Back then this required hacks; today there's the built-in `GarbageCollector.GCMode`.

**The numbers.** Before: the heap grew noticeably during battles, because there were allocations mid-gameplay, and every one of them had to be found and removed. Collections took up to ~2 s on PS4 and Switch. After: the heap doesn't grow during a battle, and there are zero collections per battle.

The catch: a single forgotten allocation in battle starts growing the heap again, and with the GC disabled that's no longer a stall but memory running out.

## 2. The premature optimization that saved the release

When we wrote the unit renderer in 2015, Unity couldn't draw much in large numbers, so we optimized and micro-optimized everything we saw. The renderer needs to know the upper bound on the number of units in advance to allocate its buffers. We computed it as the sum of units in all buildings on the map, multiplied by the number of players (in theory, each one can use an ability that duplicates units). If we missed something, the extra units just don't get drawn, and that's fine: with a thousand units on screen you can't tell who's who anyway, let alone with four thousand.

That formula lived for seven years. Then it backfired.

## 3. 220,000 units instead of 4,000

**The problem.** A low-end device crashed while loading one specific map. Every other map worked fine.

**How we found it.** The behavior was typical of running out of memory, and the logs confirmed it.

**The cause.** The same formula from 2015. A level designer had placed 5,000 units in buildings "off the map" so they could be released by a trigger. As a result, instead of a maximum of ~4,000 units (and render buffers for 20,000), the game started reserving and processing ~220,000.

**Why nobody noticed earlier.** We render units with particles, and the extra particles didn't give themselves away. The map shipped like that for about three months: normal devices had enough memory, and only the low-end one crashed. In the end, we found the cause almost by accident while refactoring the unit renderer.

**The fix.** It turned out the particle system was being given a capacity based on that formula, multiplied by the number of layers on top. And it was drawing every particle in the buffer, not just the ones belonging to live units. We fixed the capacity calculation and started drawing only the particles actually in use.

**The lesson.** Code nobody has touched in seven years still enforces limits that everyone has forgotten about. Computed limits need to be checked against real content data. A build-time map validator that reports "this map needs a buffer for N units" would have caught the problem the day it appeared.

## 4. Unit paths that cost almost nothing

Units in Mushroom Wars 2 always move from building to building, and the map is static. That means every path can be built ahead of time in the editor, with no pathfinding at runtime at all. Paths are built in three stages:

1. **A\* on a grid.** In the editor the whole field is a grid, and A\* easily finds a path from building to building around obstacles. But a grid path is jagged and hugs obstacles.
2. **A chain of colliders.** Along that path we create a chain of box colliders connected by joints. Each collider is the size of a unit in the game. There are up to eight paths between buildings, so up to eight chains at once.
3. **A physics simulation.** We run physics 50 frames ahead. The chains push off each other and off obstacles, tighten and smooth out, like ropes. The result is clean paths through narrow passages, neat curves around buildings, and roads that don't overlap.

We save the collider positions as spline control points. At the start of a battle, a Catmull-Rom spline is built from them, and units simply move along the spline. A squad marches in neat rows and keeps formation, which looks good and has a big effect on how the game feels.

A battle can have up to 4,000 units, and building paths for them at runtime would be expensive; this way it's almost free. The limitation is obvious: the approach only works because the map and the set of routes are known in advance. A dynamic world needs hierarchical pathfinding with flow fields per chunk.

## 5. How a 2D game got real shadows

We built Mushroom Wars 2 for Steam first. Our experience and the hardware would have allowed 3D, but we deliberately chose 2D: any "beautiful 3D" looks dated within a few years, while good hand-drawn 2D ages slowly.

We drew the buildings and units in pixel-perfect 2D, but we wanted real shadows. The solution turned out to be fun. Around the outline of each building we made a low-poly mesh slightly larger than the building itself and placed the 2D sprite inside it, but didn't render the mesh. The mesh only took part in shadow calculations, casting and receiving shadows, while only the sprite was visible on screen. The result was pixel-perfect rendering with real-time shadows.

Later we dropped mesh shadows in favor of sprites and render textures, because we needed to support low-end devices. But the story stuck.

## 6. Players losing their accounts on iOS

**The problem.** Players who hadn't linked a social account complained about losing progress, mostly on iOS.

**How it worked.** We wanted people to be able to play without signing in. To do that, the client sent the server a unique string, and we used `SystemInfo.deviceUniqueIdentifier`. Once upon a time that was a stable hardware identifier; now it can change. On iOS it isn't the advertising IDFA (which requires ATT permission) but identifierForVendor, and it changes if the user deletes all of a developer's apps from the device. So that an OS-side ID change wouldn't affect the player, we stored the first value we received in `PlayerPrefs`. Of course we offered to link a social account to keep progress safe, but that's like asking people to read the readme.

**How we found it.** The complaints all came down to one scenario: the player deleted the game and reinstalled it. `PlayerPrefs` are deleted along with the app, and if there were no other apps of ours on the device, identifierForVendor changed too. New identifier, new account.

**What we did.** We started storing the key in the Keychain, which survives reinstalls. The complaints stopped. The Keychain has its own pitfall: if you transfer the app to a different developer account, you lose access to the data stored there.

## Cheat sheet

| Story | Lesson |
| --- | --- |
| GC mid-battle | Pool all gameplay objects, disable the GC during battles with `GarbageCollector.GCMode`, collect on the results screen |
| Premature optimization | An upper bound for the renderer, set early, saved the release, but its assumptions live on for years |
| 220,000 units | Check computed limits against real maps with a build-time validator |
| Unit paths | If the map is static, build paths in the editor and leave only the spline for runtime |
| Shadows in 2D | An invisible low-poly mesh around the sprite only casts and receives shadows |
| Accounts on iOS | Store the guest account key in the Keychain, not in `PlayerPrefs` |

---

*I'm Alex Silaev, CTO at Zillion Whales, the studio behind Mushroom Wars 2, and I've been building games in Unity for more than 15 years. These stories come from the production chapter of my book on Unity performance, memory and architecture, available in English on [Patreon](https://www.patreon.com/chromealex/posts/book-everything-173962820) and [Boosty](https://boosty.to/chromealex/posts/7d456477-1b06-460d-8cc7-5f8defad2dcb). More of my work: [GitHub](https://github.com/chromealex), [chromealex.com](https://chromealex.com).*
