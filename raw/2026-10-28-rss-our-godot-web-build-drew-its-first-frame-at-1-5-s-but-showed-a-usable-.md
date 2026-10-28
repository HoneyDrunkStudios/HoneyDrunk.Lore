---
source: "https://dev.to/cgtrocketx_dev/our-godot-web-build-drew-its-first-frame-at-15-s-but-showed-a-usable-screen-at-103-s-heres-14lj"
title: "Our Godot web build drew its first frame at 1.5 s but showed a usable screen at 10.3 s — here's what moving things around did"
author: "CGT Rocket X Racer"
date_published: "2026-10-28"
date_clipped: "2026-10-28"
category: "Game Development / Unity"
source_type: "rss"
---

# Our Godot web build drew its first frame at 1.5 s but showed a usable screen at 10.3 s — here's what moving things around did

Source: https://dev.to/cgtrocketx_dev/our-godot-web-build-drew-its-first-frame-at-15-s-but-showed-a-usable-screen-at-103-s-heres-14lj

Fan-made · Free in PC browser · Android on Google Play · iOS coming soon · Not affiliated

A Godot web build can draw early and still feel slow. Our first WebGL frame came at a median 1,527 ms on a first visit, but a player saw nothing they could click until 10,344 ms. So the engine was ready to draw for almost nine seconds while the player waited behind a loading overlay.

Article 9 looked at where the startup time goes. This one is about decisions: what has to load before the first frame, what can wait, and whether moving it actually helps.

## Two finish lines, timed separately

"Loaded" hides two different moments, so we timed them separately:

- **First real UI visible:** the first engine-drawn screen with something the player can interact with (a button), with no HTML overlay covering it.
- **Playable:** the game scene is running, its streamed level content has finished loading, and the overlay is gone. In our build the game prints a console line at exactly that point, and the intro with SKIP and the menu with PLAY follow from there.

Speeding up one can slow down the other.

## The before-first-frame checklist

Our web export already uses two packs. `index.pck` (4,381,724 bytes) loads with the engine. `main.pck` (50,860,652 bytes) is downloaded and mounted by the boot scene at runtime. A boot pack should contain only what the first screen needs: the boot scene, its script, a font, and the menu UI. Our rule for everything else: **if the player can't see or use it in the first seconds, it doesn't go in the boot pack.**

When we opened our boot pack with GDRE Tools, it failed that rule. Its biggest file was a 2,035,057-byte video that the boot scene played underneath an HTML overlay, so no player ever saw it. Next came 1,736,096 bytes of tutorial and guide textures. `main.pck` contains 27,385,814 bytes of imported 3D models and 11,835,266 bytes of textures. The first menu needs none of it.

## Three levers, and what each one costs

**1. Split packs with export filters and `load_resource_pack()`.** Export presets can include or exclude files by filter, and `ProjectSettings.load_resource_pack()` mounts a PCK at runtime ([exporting projects](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html), [exporting packs](https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html)). The cost is that you now maintain two dependency lists, and a missing file only shows up at runtime.

**2. `ResourceLoader.load_threaded_request()` + `load_threaded_get_status()`.** This is the documented way to load in the background and poll progress ([background loading](https://docs.godotengine.org/en/stable/tutorials/io/background_loading.html)). Our export is **single-threaded**, so we measured what the call actually does there instead of assuming.

**3. When the overlay comes off.** Our HTML shell removed its overlay only after the scene was ready **and** its loader video had finished. Removing it as soon as the scene is ready means the branding clip gets cut off, and players may see a plain engine loading screen.

## The experiment

Every variant used the same public files (Godot 4.7.2 web export), served locally. These variants were built and measured locally; the public build hasn't been changed yet.

- **A:** the current build, unchanged.
- **B:** only the overlay change. The page calls `reveal()` at scene-ready instead of waiting for the video. Two lines of HTML.
- **C:** B plus a new boot scene. It draws the real menu (title, PLAY button, status line) on its first frame. After that frame is drawn (`RenderingServer.frame_post_draw`), it fetches `main.pck`, mounts it with `load_resource_pack()`, and loads the main scene with `load_threaded_request()`, then `change_scene_to_packed()` once PLAY has been pressed. The hidden boot video was removed, which brought the boot pack down to 2,570,428 bytes. `main.pck` was left byte-identical.

**Environment:** local headless Chrome 156 on a Linux box (8 vCPU), driven by Puppeteer over the Chrome DevTools Protocol. There was no GPU, so WebGL ran on SwiftShader. The files came from a local server on loopback, with **no network throttling**. A first visit used an empty profile, and a repeat visit used the same profile with cache. Each variant got 3 runs, and every number below is the **median**. In C, the test script clicked PLAY as soon as the menu appeared, like an impatient player.

**First visit (ms from navigation, median of 3):**

|  | A | B | C |
| --- | --- | --- | --- |
| First WebGL frame | 1,527 | 1,527 | 1,646 |
| First real UI visible | 10,344 | 5,444 | 1,647 |
| Playable | 11,196 | 8,002 | 5,972 |
| Longest freeze between UI and playable | 383 | 2,150 | 1,200 |

**Repeat visit:**

|  | A | B | C |
| --- | --- | --- | --- |
| First WebGL frame | 1,047 | 1,012 | 1,095 |
| First real UI visible | 9,768 | 4,836 | 1,105 |
| Playable | 10,612 | 6,608 | 5,439 |
| Longest freeze between UI and playable | 400 | 1,700 | 817 |

Before running anything, we set a success criterion: C must show real UI at least 2 s earlier than A, and C's playable time must be no more than 10% later than A's. **It passed.** On first visits, C's UI came 8,697 ms earlier and C was playable at 0.533 of A's time. On repeat visits, the figures were 8,663 ms and 0.513.

## What actually moved the numbers

**The two-line overlay fix did most of the work.** On first visits, B alone brought real UI forward by 4,900 ms and playable by 3,194 ms. The rest of the pipeline was fine; the delay came from an overlay waiting for a video to finish.

**The boot menu was the second step.** Going from B to C brought real UI forward by another 3,797 ms and playable by 2,030 ms. The menu showed up 7 ms after the first WebGL frame. We did not isolate why C also became playable sooner than B, because C changed several things at once.

**On a single-threaded build, `load_threaded_request()` blocked anyway.** After mounting, the call took a median 413 ms to return, the page went without a new frame for 467 ms, and the scene already reported LOADED on the first poll. The progress API still worked, but loading was not happening in the background. A threaded export may behave differently. We didn't test one.

**Costs we measured:**

- C's first WebGL frame came 119 ms later than A's on first visits. Its boot scene also loads a 220,634-byte menu texture; we did not isolate the cause.
- C shows the menu early, and then the menu can freeze for up to 1,200 ms while the game scene starts. In A, nothing on screen is interactive before 10.3 s, but once it is, the longest freeze is 383 ms.
- On repeat visits, C mounted `main.pck` at 4,130 ms against 2,729 ms for A. We haven't found out why.

## When it's not worth it

- If your HTML or engine loading screen waits for an animation, change that first. It took two lines for us and gave the largest single gain.
- A boot scene plus a separate pack is two dependency lists to keep in sync. For a small game that ships one pack, our numbers don't show a reason to split.
- Showing a menu that freezes after the first click can feel worse than an honest progress bar. We didn't measure how players perceive it.
- These numbers come from local headless Chrome with software WebGL and no throttling. They tell us about this build's startup pipeline. They are not predictions for real GPUs, real networks, or other devices.

What's in your boot scene that the first frame doesn't need?

PC browser: <https://cgt.monster/x/devto10>
