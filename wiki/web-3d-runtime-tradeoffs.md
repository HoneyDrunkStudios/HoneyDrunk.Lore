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

## 2026-06-28 compile additions: Miris spatial streaming

### Source-backed claims
- 80 Level's Miris interview reports an internal WebXR car configurator running from a 1.2GB source vehicle asset across desktop browsers, tablets, mobile devices, and headsets without allocating one cloud GPU per viewer. Source: `raw/2026-06-28-rss-80-level-miris-built-a-car-configurator-without-pixel-streaming.md`. confidence: 1 vendor/interview source, last-confirmed 2026-06-28.
- The source contrasts pixel streaming, local glTF web viewers, and Miris spatial streaming: pixel streaming preserves fidelity but scales GPU cost linearly with viewers, glTF removes server GPU cost but often reduces fidelity through compression, and spatial streaming attempts adaptive on-device rendering from a conditioned source asset. Source: `raw/2026-06-28-rss-80-level-miris-built-a-car-configurator-without-pixel-streaming.md`. confidence: 1 source, last-confirmed 2026-06-28.
- Miris says its pipeline conditions an OpenUSD-native source asset once, identifies reflective surfaces, allocates more detail near the viewer and less detail farther away, and avoids rendering content behind the viewer within device/network constraints. Source: `raw/2026-06-28-rss-80-level-miris-built-a-car-configurator-without-pixel-streaming.md`. confidence: 1 vendor/interview source, last-confirmed 2026-06-28.
- The source claims the configurator supports 72 paint/door-state variations and HDR-grade reflections, but those claims need independent performance and visual-quality validation before procurement-grade use. Source: `raw/2026-06-28-rss-80-level-miris-built-a-car-configurator-without-pixel-streaming.md`. confidence: 1 vendor/interview source, last-confirmed 2026-06-28.

### Typed entities
- platform: Miris spatial streaming
- standard: WebXR
- format: OpenUSD
- format: glTF
- approach: pixel streaming
- device: Apple Vision Pro
- concept: HDR reflections
- concept: adaptive 3D delivery
- domain: automotive configurator

### Explicit relationships
- Pixel streaming depends-on server-side GPU rendering and therefore scales cost with concurrent viewers.
- Web-native glTF viewers depend-on local GPU rendering and compressed assets, trading reach and cost for potential material-fidelity loss.
- Spatial streaming complements browser-first 3D by trying to deliver source-asset fidelity adaptively while keeping rendering on device.
- Vendor demonstrations do not supersede local device, network, thermal, cost, and asset-pipeline tests.

### HoneyDrunk implications
- For browser/XR product configurators or showrooms, evaluate adaptive asset streaming alongside WebXR/Babylon.js and pixel streaming rather than treating the choice as only app install vs cloud GPU.
- Require a representative asset test with real target devices, bad-network behavior, material fidelity review, cost model, and fallback plan before relying on Miris or similar platforms.

### Quality notes
- 80 Level source is an interview with the platform team. It is useful for scouting but not neutral benchmark evidence.
