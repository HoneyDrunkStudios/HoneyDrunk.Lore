---
source: https://dev.to/lumenform/shipping-single-file-html5-playable-ads-my-unity-2022-webgl-pipeline-57pb
title: 'Shipping single-file HTML5 playable ads: my Unity 2022 WebGL pipeline'
author: LUMENFORM
date_published: '2026-10-04'
date_clipped: '2026-10-04'
category: Game Development / Unity
source_type: rss
capture_method: full-readable-extraction
---

# Shipping single-file HTML5 playable ads: my Unity 2022 WebGL pipeline

Source: https://dev.to/lumenform/shipping-single-file-html5-playable-ads-my-unity-2022-webgl-pipeline-57pb

Last month I set out to answer a simple question: how small and how self-contained can a Unity WebGL playable ad actually be?

Three builds later, here's what I ended up with — all playable directly in the browser:

-
**Match-3 playable**(Prism Vein) — chain reactions, three special-match effects, audio end card. 4.7 MiB (EN) / 5.1 MiB (ZH) -
**Idle-growth playable**(Core Forge) — tap-collect, three upgrade tiers, 1,000-unit milestone. ~8.2 MiB with a runtime EN/ZH switch -
**3D product microsite**(Atlas Relay) — orbit camera, three hotspot panels, day/night toggle. 9.61 MiB

Playable here: [https://www.lumenformlab.com](https://www.lumenformlab.com)

## The constraints that shaped everything

Playable ads live inside ad network SDKs (MRAID containers), and networks impose caps: file size, single-file delivery, no external requests, muted audio until first interaction, and a CTA that fires `mraid.open()`

.

That rules out the default Unity WebGL export. The pipeline became: **Unity 2022 → WebGL export → repack**.

### 1. Export settings that matter

- Brotli/gzip compression on the build payload
- Strip engine code, high managed stripping level
- No exceptions, no stack traces (smaller + faster startup)
- IL2CPP + code stripping

### 2. Repack to a single file

The default export ships as `index.html + Build/*.unityweb + TemplateData/*`

. For playable delivery this gets repacked into **one inlined index.html**:

- base64-inline the
`.wasm`

,`.data`

,`.framework.js`

payloads - inline the loader
- zero external requests — verifiable in DevTools: the network tab shows exactly one document request

### 3. Audio discipline

Network rules require muted audio until first tap. I keep an `AudioContext`

suspended until the first pointer event, then resume it — sounds only fire after real interaction.

### 4. CTA through MRAID

The end-card CTA checks for `mraid`

availability:

- inside an MRAID container →
`mraid.open(url)`

- outside (plain web demo) →
`window.open(url)`

fallback

I wrapped the match-3 build in a MRAID 2.0 harness locally (`getVersion()`

returns 2.0) to verify the bridge works.

## Size results

| Build | Size | Languages |
|---|---|---|
| Match-3 | 4.7 MiB | EN / ZH (two separate builds) |
| Idle-growth | ~8.2 MiB | EN+ZH runtime switch in one build |
| 3D microsite | 9.61 MiB (18 files) | EN+ZH |

Most of the match-3 savings came from texture discipline (palette-swapped sprites) and audio compression, not from hacking the engine.

## What I'd tell anyone building playables

- Budget the size cap first, design second
- Test inside a real MRAID harness, not just a browser tab
- Keep one inlined file as the single source of truth for delivery

I'm a solo developer building these end-to-end (Unity 2022 → WebGL → repack), currently taking on small fixed-scope builds. If you work with playable ads or interactive 3D, I'm happy to compare notes — all three demos are live at [https://www.lumenformlab.com](https://www.lumenformlab.com)

## Top comments (0)
