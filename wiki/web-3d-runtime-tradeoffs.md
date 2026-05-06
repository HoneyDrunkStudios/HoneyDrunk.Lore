# Web 3D Runtime Tradeoffs

## Decision-useful summary
For browser-first 3D/XR/metaverse-style workloads, the 2026-05-06 DEV.to benchmark claims WebXR/Babylon.js delivered smaller payloads and faster startup than Unity WebGL and Unreal HTML5 on tested desktop/mobile/Quest workloads. Treat the numbers as directional scouting, not neutral proof: it is a single source with unknown reproducibility. The durable decision frame is stable: web-native stacks tend to win on payload/startup/control, Unity wins on familiar tools and built-in systems, Unreal wins on high-end visual tooling at the highest payload/memory cost. [source: raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md]

## Claims
- The cited benchmark tested WebXR 2.0 via Babylon.js 6.0, Unity 2023.2 WebGL with URP/WebXR plugin, and Unreal Engine 5.3 HTML5/WebXR across social hub, product showcase, and mini-game workloads. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md]
- The benchmark reports WebXR/Babylon.js with the fastest desktop time-to-interactive (1.2s), smallest average payload (~12MB), lower peak memory (1.8GB), and fastest Quest 3 XR startup (0.7s) among the tested options. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md]
- The benchmark reports Unity WebGL with familiar Unity tooling plus physics/networking/asset-management benefits, but larger payloads (~87MB), slower desktop TTI (3.8s), and higher peak memory (3.2GB) than WebXR/Babylon.js. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md]
- The benchmark reports Unreal HTML5 with highest out-of-the-box visual fidelity and robust physics/animation tools, but the largest payloads (~142MB), slowest desktop TTI (5.1s), highest memory (4.7GB), and weaker mobile browser support among tested options. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md]

## Typed entities
- concept: WebXR 2.0
- library/engine: Babylon.js
- engine/export: Unity WebGL
- engine/export: Unreal Engine HTML5
- engine: Unity 2023.2
- engine: Unreal Engine 5.3
- platform/browser: Chrome 124
- device: iPhone 15 Pro
- device: Meta Quest 3
- metric: time to interactive
- metric: average FPS
- metric: peak memory
- metric: payload size
- metric: XR startup time

## Explicit relationships
- WebXR/Babylon.js uses browser-native XR APIs and low-level JavaScript/WebGL tooling to minimize payload/startup.
- Unity WebGL depends-on Unity tooling and built-in systems while trading off larger browser payload and memory overhead.
- Unreal HTML5 depends-on high-end visual/animation tooling while trading off startup, payload, and mobile browser support.
- The benchmark's single-source status contradicts treating its numeric claims as procurement-grade evidence.

## HoneyDrunk implications
- For browser-first demos, prototype the smallest representative scene in WebXR/Babylon.js before defaulting to Unity WebGL.
- Choose Unity WebGL when editor/toolchain velocity and built-in systems matter more than first-load weight.
- Avoid Unreal HTML5 unless visual fidelity/tooling requirements justify heavy payload and mobile risk.

## Confidence and quality notes
- Quality posture: useful decision frame, weak empirical authority until reproduced.
- Gap: reproduce a HoneyDrunk-specific browser 3D benchmark with target devices and target scene complexity.
- Privacy filter: no private data copied.
