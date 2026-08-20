---
source: "https://realtimevfx.com/t/nixiefx-a-browser-based-particle-editor-for-three-js-and-pixijs/31492"
title: "NixieFX, a browser-based particle editor for Three.js and PixiJS"
author: "RealtimeVFX"
date_published: "2026-08-20"
date_clipped: "2026-08-20"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# NixieFX, a browser-based particle editor for Three.js and PixiJS

Source: https://realtimevfx.com/t/nixiefx-a-browser-based-particle-editor-for-three-js-and-pixijs/31492

NixieFX, a browser-based particle editor for Three.js and PixiJS - Real Time VFX
General
Resources
References
Jobs -->
Events
Real Time VFX
NixieFX, a browser-based particle editor for Three.js and PixiJS
Personal Work
alma
August 20, 2026, 8:42am
1
Hi everyone. I am part of the team working on NixieFX, and I would like to share the current editor with the community.
NixieFX is focused on real-time effects for web games using Three.js and PixiJS. The editor includes multi-emitter timelines, curves, gradients, shape emission, velocity and forces, noise, plane collision, flipbooks, trails, sub-emitters, and a node-based material workflow.
We wanted the authoring experience to feel familiar to artists coming from engine-style particle systems while still fitting a web development pipeline. Projects remain as plain JSON in a local folder, and exports include backend diagnostics so limitations are visible before integration.
The PixiJS and Three.js runtimes share a deterministic simulation, but each has its own rendering path. The goal is portability where it is practical, not a promise that every 3D material or mesh effect will look identical in 2D.
The editor is free to use here: NixieFX — Particle & VFX Editor
I would be grateful for feedback on the timeline and material workflow, especially from artists who regularly move effects between authoring tools and runtime teams.
1 Like
Niels
August 20, 2026, 11:15am
2
What’s your use case? It works well for little effects, but I guess it’s usefulness kinda depends on what you would use it for.
Home
Categories
Guidelines
Terms of Service
Privacy Policy
Powered by Discourse , best viewed with JavaScript enabled
