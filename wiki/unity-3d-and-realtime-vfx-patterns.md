# Unity 3D and Realtime VFX Patterns

## Decision-useful summary
Unity-related sources clustered around practical production patterns: planning no-code/interactive 3D projects, reducing 3D-tool adoption friction through Unity Studio, real-time fire/fluid-like VFX in Ignitement, GPU-driven rendering for high-speed racing, reusable/free educational VFX shader resources, AI-scene-generation scouting, web runtime tradeoffs, shipped-game ecosystem signal, and hybrid mobile architecture where Unity owns an embedded 3D/avatar layer inside a conventional app shell. These are useful as inspiration and evaluation inputs, but many are vendor/community posts rather than neutral benchmarks. [sources: raw/2026-05-04-rss-unity-blog-making-fire-feel-alive-real-time-fluid-simulation-in-ignite.md; raw/2026-05-04-rss-unity-blog-the-hidden-costs-of-traditional-3d-tools-and-the-smarter-wa.md; raw/2026-05-05-rss-unity-blog-10-questions-to-ask-before-starting-your-first-3d-project.md; raw/2026-05-05-rss-unity-blog-rendering-at-500-km-h-in-gear-club-unlimited-3.md; raw/2026-05-05-rss-realtimevfx-master-material-vfx-free-use-unity.md; raw/2026-05-06-rss-dev-to-unity-after-genie-3-38-alternatives-for-ai-scene-generation.md; raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md; raw/2026-05-06-rss-unity-blog-games-made-with-unity-march-2026-in-review.md; raw/2026-05-11-rss-dev-to-unity-building-coach-ivy-embedding-a-unity-avatar-inside-a-flut.md; raw/2026-05-11-rss-dev-to-unity-game-dev-digest-issue-330-unity-ai-game-art-and-more.md]

## Claims
- Ignitement uses real-time fluid-simulation-inspired fire/lava VFX to make fire feel reactive and integrated, trading against the cost of full 3D simulations and the limitations of traditional particles. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-unity-blog-making-fire-feel-alive-real-time-fluid-simulation-in-ignite.md]
- Unity argues that no-code 3D tooling such as Unity Studio can reduce financial, operational, and organizational overhead for teams creating interactive 3D experiences. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-unity-blog-the-hidden-costs-of-traditional-3d-tools-and-the-smarter-wa.md]
- Unity's first-3D-project checklist frames planning around audience, objective, assets, interactivity, platform, success metrics, and maintainability before implementation. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-unity-blog-10-questions-to-ask-before-starting-your-first-3d-project.md]
- Gear.Club Unlimited 3 targets 60 fps arcade racing while streaming large environments at up to ~500 km/h, using a matured custom rendering pipeline and GPU-driven architecture across consoles/PC and ray tracing targets. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-unity-blog-rendering-at-500-km-h-in-gear-club-unlimited-3.md]
- A RealTimeVFX community post shares a free educational Unity master material/shader but explicitly warns it is not optimized and may cause project issues. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-realtimevfx-master-material-vfx-free-use-unity.md]
- A DEV.to Unity post lists AI scene-generation alternatives after Google Genie 3, including open/world-model options, 3D asset generators, prompt-to-game tools, NPC tools, payments/hosting options, and budget-based playbooks; treat as scouting rather than validated benchmark. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-unity-after-genie-3-38-alternatives-for-ai-scene-generation.md]
- A DEV.to benchmark claims WebXR/Babylon.js had smaller payloads and faster startup than Unity WebGL and Unreal HTML5 in tested metaverse workloads, while Unity WebGL traded higher payload/memory for familiar tooling and built-in physics/networking. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md]
- Unity's March 2026 “Games made with Unity” roundup lists many shipped/early-access Unity titles and IGF-recognized projects, indicating broad indie/commercial ecosystem activity but not engine suitability by itself. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-unity-blog-games-made-with-unity-march-2026-in-review.md]
- Unity official Discord snapshots for 2026-05-04 through 2026-05-06 were ingested but mostly captured Discord UI scaffolding, not decision-grade announcement content. confidence: 3 sources, last-confirmed 2026-05-06. [sources: raw/2026-05-04-clipper-discord-official-unity.md; raw/2026-05-05-clipper-discord-official-unity.md; raw/2026-05-06-clipper-discord-official-unity.md]
- Coach Ivy's DEV.to case study describes a hybrid Flutter + Unity mobile architecture: Flutter owns onboarding, food logging, subscriptions, analytics, navigation, and app state, while an embedded Unity view owns a reactive 3D avatar, animations, facial expressions, BlendShapes, camera/lighting, and mood reactions. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-rss-dev-to-unity-building-coach-ivy-embedding-a-unity-avatar-inside-a-flut.md]
- Game Dev Digest issue #330 is a newsletter aggregation that points to Unity AI/Open Beta, game-art/VFX/Jobs/shader workflows, GPU mesh particles via compute shaders/Render Graph, and Unity asset/tool links; useful for discovery, not primary evidence. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-rss-dev-to-unity-game-dev-digest-issue-330-unity-ai-game-art-and-more.md]

## Typed entities
- project/engine: Unity
- product: Unity Studio
- game: Ignitement
- game: Gear.Club Unlimited 3
- studio: Eden Games
- concept: real-time fluid simulation
- concept: GPU-driven rendering
- concept: ray tracing
- concept: WebXR
- library/engine: Babylon.js
- platform/export: Unity WebGL
- platform/export: Unreal Engine HTML5
- concept: AI scene generation
- model/tool: Google Genie 3
- model/tool: Tencent HunyuanWorld 2.0
- model/tool: Hunyuan3D 2.1
- model/tool: Rosebud AI
- model/tool: Convai
- asset: free Unity master material VFX shader
- event/award: IGF awards 2026
- platform: Nintendo Switch 2
- framework/runtime: Flutter
- project/app: Coach Ivy
- platform/service: Ready Player Me
- tool/library: SALSA LipSync
- concept: embedded Unity mobile view
- concept: Flutter-to-Unity message bridge
- product/tool: Unity AI
- concept: GPU mesh particles
- technology: Unity Render Graph

## Explicit relationships
- Ignitement uses real-time fluid-simulation-inspired VFX to improve fire/lava responsiveness.
- Unity Studio is positioned as reducing adoption friction for interactive 3D teams.
- Gear.Club Unlimited 3 depends-on GPU-driven rendering and custom streaming/rendering architecture for high-speed environments.
- Free Unity master material VFX shader contradicts production-readiness expectations because the author says it is educational and not optimized.
- WebXR/Babylon.js contradicts Unity WebGL on startup/payload efficiency in the cited benchmark, while Unity WebGL depends-on engine tooling familiarity to justify overhead.
- AI-scene-generation scouting depends-on validating availability, licensing, cost, and quality before adoption.
- Unity release roundup reinforces Unity ecosystem breadth but does not supersede project-specific engine evaluation.
- Flutter + Unity hybrid apps depend-on a clear ownership boundary: native/cross-platform app shell for product flow, Unity for the real-time character/3D layer, and a message bridge for event/state synchronization.
- Unity AI and GPU/VFX items from newsletter aggregations depend-on linked primary sources before adoption decisions.

## HoneyDrunk implications
- Use Unity Studio/no-code claims as a discovery prompt, not as proof of lower total cost; test with a small project before committing.
- For high-speed or VFX-heavy game concepts, capture techniques from Ignitement/GCU3 but budget for custom render/VFX engineering.
- Treat free VFX shader resources as learning/reference material unless profiled and optimized.
- For browser-first 3D/XR prototypes, compare WebXR/Babylon.js against Unity WebGL early; payload and mobile startup may dominate toolchain comfort.
- AI scene-generation lists are useful sourcing queues, not vendor selections; verify licenses and actual workflow fit.
- If HoneyDrunk wants character-led mobile experiences, use the Coach Ivy split as a reference pattern: keep commerce/navigation/app state outside Unity unless the 3D layer truly needs ownership.
- For Unity AI/GPU-particle tooling, follow the Digest links only as a queue; validate Unity version, package maturity, profiling, and licensing before bringing anything into production.

## Confidence and quality notes
- Quality posture: decision-usable as scouting notes; vendor bias likely in Unity blog claims, DEV.to case studies are self-reported, and newsletter/link-roundup items need primary-source follow-up before major decisions.
- Privacy filter: Discord UI dumps summarized without copying user/chat details.

## 2026-05-18 compile additions

### Claims
- Albion Online operates from a single Unity project across PC, Mac, Linux, iOS, Android, and Xbox Series X|S, with platform-specific UI profiles, abstracted input, and identical gameplay logic while visual fidelity scales by platform. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-architecting-albion-online-how-sandbox-interactive-built-a-.md]
- Sandbox Interactive separates Albion Online's client into input, simulation prediction/authoritative-server synchronization, and visualization layers; the core simulation is independent of Unity and rendering should not bottleneck game logic. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-architecting-albion-online-how-sandbox-interactive-built-a-.md]
- Albion Online uses Jenkins daily builds for every platform plus validation for missing references, mesh limits, and game-data errors; every developer can run the full server-client stack locally. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-architecting-albion-online-how-sandbox-interactive-built-a-.md]
- Unity for Humanity 2026 awarded 10 winners and 3 honorable mentions from 515+ applications with a $600,000 prize pool, showing real-time 3D use across health, climate, education, accessibility, rehabilitation, and cultural preservation. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-unity-for-humanity-2026-winner-announcement.md]

### Typed entities
- game: Albion Online
- studio: Sandbox Interactive
- engine: Unity Built-In Render Pipeline
- engine: Unity Scriptable Render Pipeline / SRP
- tool: Jenkins
- pattern: decoupled simulation and visualization
- pattern: single-project cross-platform Unity build
- event/program: Unity for Humanity 2026 Grant
- fund: Unity Charitable Fund
- project: Project Ember
- project: HandSolo
- project: Reclaim! Azhe-giiwewining
- project: Amaru Reimagined

### Explicit relationships
- Albion Online uses one Unity project with platform-specific UI/input/visual profiles to support cross-platform PvP.
- Decoupled simulation depends-on authoritative server logic and client prediction, and prevents rendering from constraining game-state rules.
- Android/mobile performance baseline constrains cross-platform feature work for Albion Online.
- Unity for Humanity uses grant funding to support real-time-3D social-impact prototypes and distribution.

### HoneyDrunk implications
- For any multiplayer/cross-platform Unity prototype, separate simulation rules from Unity visualization early; do not let scene/render concerns become the game-state authority.
- Pick the weakest target device as the performance baseline if cross-play fairness matters.
- Treat Unity for Humanity projects as sourcing for impact/AR/VR/rehab patterns, not direct technical benchmarks.

## 2026-05-19 compile additions

### Claims
- A DEV.to Unity comparison frames Unity as stronger for fast prototyping, mobile-first development, 2D/stylized 3D, AR/VR, cross-platform deployment, and small-team flexibility; it frames Unreal as stronger for AAA visuals, high-performance 3D, cinematic rendering, complex simulations, structured pipelines, and engine-level control. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-dev-to-unity-unity-vs-unreal-comparison-pros-cons-key-differences.md]
- The same source says engine choice should be driven by target platform, visual direction, team expertise, production timeline/budget, long-term maintenance, monetization, and live-update requirements rather than a generic “best engine” answer. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-dev-to-unity-unity-vs-unreal-comparison-pros-cons-key-differences.md]

### Typed entities
- engine: Unity
- engine: Unreal Engine
- concept: engine selection criteria
- concept: mobile-first development
- concept: AAA visual fidelity
- concept: live updates

### Explicit relationships
- Unity and Unreal Engine contradict one-size-fits-all engine selection; suitability depends-on platform, visuals, team skills, budget, maintenance, and live-ops needs.
- Unity is positioned as supporting fast/mobile/stylized workflows; Unreal is positioned as supporting cinematic/high-end simulation workflows.

### HoneyDrunk implications
- Keep the existing HoneyDrunk engine-selection gap open: this source reinforces evaluation criteria but is not procurement-grade evidence or a benchmark.

## 2026-05-20 compile additions

### Claims
- A DEV.to/Ocean View Games mobile-engine comparison argues Unity is the pragmatic choice for most commercial mobile projects because of mature mobile rendering/URP, smaller baseline build sizes than Unreal, faster iteration than Unreal, C# talent availability, and first-party/vendor monetization and analytics SDK maturity. confidence: 1 biased/self-disclosed Unity-specialist source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-dev-to-unity-unity-vs-godot-vs-unreal-for-mobile-games-a-practical-com.md]
- The same source recommends Godot mainly for indie/solo 2D mobile games where zero license cost, small exports, and rapid iteration matter more than first-party ad/IAP/analytics tooling. confidence: 1 biased/self-disclosed source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-dev-to-unity-unity-vs-godot-vs-unreal-for-mobile-games-a-practical-com.md]
- The same source recommends Unreal for projects prioritizing visual fidelity, PC/console-first production, or teams with strong C++ depth; it flags Unreal mobile tradeoffs around baseline app size, desktop-first workflow, build times, and lack of Lumen/Nanite on mobile. confidence: 1 biased/self-disclosed source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-dev-to-unity-unity-vs-godot-vs-unreal-for-mobile-games-a-practical-com.md]

### Typed entities
- engine: Unity
- renderer: Unity Universal Render Pipeline / URP
- engine: Godot
- engine: Unreal Engine
- feature: Lumen
- feature: Nanite
- language: C#
- language: C++
- language: GDScript
- product/service category: mobile ad mediation SDK
- product/service category: in-app purchase SDK
- product/service category: analytics SDK

### Explicit relationships
- Unity uses mature mobile SDK/tooling ecosystems to reduce commercial mobile integration risk.
- Godot depends-on lighter/community-maintained mobile monetization integrations for many commercial free-to-play needs.
- Unreal's Lumen and Nanite advantages contradict mobile-first assumptions because those headline features do not run on mobile in the cited comparison.
- Engine choice depends-on target hardware, monetization model, team language depth, build-size constraints, and visual goals.

### HoneyDrunk implications
- This strengthens Unity as the default commercial-mobile candidate, but it is not neutral evidence; require a HoneyDrunk prototype benchmark before closing the engine-selection gap.
- For lightweight 2D/mobile experiments with minimal monetization, Godot remains worth testing.
- Avoid Unreal for mobile-first prototypes unless high-end visuals or PC/console-first production is the real target.

## 2026-05-21 compile additions

### Claims
- Unity Studio added collaboration features for direct 3D annotations and real-time multi-user editing so stakeholders, designers, and technical reviewers can give feedback in the actual interactive scene rather than static renders, PDFs, or screen recordings. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-unity-blog-accelerate-3d-workflows-new-collaboration-and-export-tools-.md]
- Unity Studio-to-Editor Export lets teams move no-code/web-created Studio projects into the Unity Editor while preserving hierarchies, materials, lighting setups, and basic logic, positioning Studio as an on-ramp rather than a throwaway prototype tool. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-unity-blog-accelerate-3d-workflows-new-collaboration-and-export-tools-.md]
- Unity frames the addressed 3D scaling bottlenecks as fragmented feedback loops, developer bottlenecks for simple content changes, and disconnected prototype-to-production toolchains. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-unity-blog-accelerate-3d-workflows-new-collaboration-and-export-tools-.md]

### Typed entities
- product: Unity Studio
- feature: direct 3D annotations
- feature: real-time multi-user editing
- feature: Studio-to-Editor Export
- engine/tool: Unity Editor
- concept: no-code 3D creation
- concept: prototype-to-production handoff

### Explicit relationships
- Unity Studio uses collaboration features to reduce fragmented 3D review loops.
- Studio-to-Editor Export connects no-code ideation to advanced Unity Editor production work.
- Unity Studio depends-on Unity Editor handoff when projects need custom C# logic, backend integration, or performance optimization.

### HoneyDrunk implications
- Unity Studio is worth a small spike for collaborative 3D review/prototyping, but vendor claims need validation on HoneyDrunk assets and target devices.
- Treat Studio-to-Editor Export as the key adoption test: if exported hierarchy/materials/logic are clean enough for developers, Studio can reduce throwaway prototype cost; if not, it becomes another conversion layer.

## 2026-05-23 compile additions

### Claims
- Unity and Attain's mobile-gaming ad partnership combines Unity mobile inventory with Attain's permissioned real-time purchase data from 14M+ consumers to target purchase-based audiences and measure incremental sales outcomes; Unity cites approximately 256M unique monthly active U.S. devices running Made with Unity mobile apps. confidence: 1 vendor source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-unity-blog-turning-purchase-data-into-outcomes-in-mobile-gaming-unity-.md]
- Unity Vector now supports D28 Ad Revenue ROAS and D28 Hybrid ROAS campaigns, completing Unity's D28 ROAS suite across IAP, ad-revenue, and hybrid monetization models; beta uplift numbers are vendor/internal and should be treated as directional. confidence: 1 vendor source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-unity-blog-unity-vector-expands-to-d28-roas-ad-revenue-and-hybrid-mone.md]
- A RealtimeVFX boat-wake forum post captures a common realtime-water production problem: mesh-trail wake approaches can conflict with distance-field water-outline/fade controls and force tradeoffs between edge fading and wake density. confidence: 1 forum source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-realtimevfx-looking-for-help-on-my-boat-wake.md]

### Typed entities
- product: Unity Vector
- company: Attain
- concept: D28 ROAS
- concept: D28 Ad Revenue ROAS
- concept: D28 Hybrid ROAS
- concept: purchase-based audience targeting
- concept: boat wake VFX
- technique: mesh trail
- technique: distance-field water shader

### Explicit relationships
- Unity Vector uses 28-day revenue prediction to optimize user acquisition for IAP, ad-revenue, and hybrid mobile-game monetization.
- Attain purchase data complements Unity mobile inventory for sales-outcome measurement.
- Mesh-trail wakes can conflict with distance-field water effects when they share shader/field resources.

### HoneyDrunk implications
- Unity's ad stack is increasingly outcome/ROAS-oriented; useful if HoneyDrunk evaluates mobile UA, irrelevant for prototype engine choice unless monetization is in scope.
- For stylized water, avoid overcommitting to mesh trails until shader resource conflicts with outlines/distance fields are tested.

## 2026-05-30 compile additions

### Claims
- Unity's 2026 render-pipeline strategy concentrates new graphics feature investment in URP, maintains HDRP mainly for stability and Nintendo Switch 2 platform reach, and begins Built-In Render Pipeline deprecation in Unity 6.5. confidence: 1 Unity source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md]
- Unity says URP is used by the vast majority of Unity games released in the past three years and is the default target for faster performance/build time, stability, extensibility, and dynamic 3D lighting improvements. confidence: 1 Unity source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md]
- Planned URP work includes physical light units, pre/auto exposure, physical sky and dynamic sky manager, realtime global illumination, screen-space reflections, and on-tile post-processing for mobile, with scalability/build-size/performance caveats. confidence: 1 Unity source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md]
- HDRP gets no new features in the described strategy, but Unity plans official HDRP support for Nintendo Switch 2 in Unity 6.5 for enrolled Nintendo developers, focused on stability and platform reach. confidence: 1 Unity source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md]
- Built-In Render Pipeline will remain available at least through Unity 6.7 LTS, with official support at least until end of 2028 and 2029 for Unity Enterprise/Industry licenses; final removal version is not yet decided, but Unity strongly discourages Built-In for new titles. confidence: 1 Unity source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md]
- Black Eye 2.0 is an Unreal-targeted camera-system signal, not a Unity tool, but its separation of camera intent from transform execution is relevant to Unity/Cinemachine-style production camera planning. confidence: 1 80 Level interview source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-80-level-how-black-eye-2-0-is-rethinking-how-video-game-camera-systems.md; page: [[game-camera-systems]]]

### Typed entities
- render pipeline: Unity Universal Render Pipeline / URP
- render pipeline: Unity High Definition Render Pipeline / HDRP
- render pipeline: Unity Built-In Render Pipeline
- release: Unity 6.5
- release: Unity 6.7 LTS
- platform: Nintendo Switch 2
- feature: realtime global illumination
- feature: screen-space reflections
- feature: physical light units
- feature: dynamic sky manager
- concept: camera intent
- page: [[game-camera-systems]]

### Explicit relationships
- URP supersedes Built-In Render Pipeline as Unity's recommended default for new projects.
- HDRP maintenance depends-on stability and platform reach rather than new feature expansion.
- Built-In Render Pipeline deprecation depends-on migration feedback before final removal timing.
- Black Eye 2.0 camera-system lessons complement Cinemachine/Unity camera thinking despite targeting Unreal Engine.

### HoneyDrunk implications
- New Unity prototypes should default to URP unless there is a clear reason not to.
- Inventory any Built-In Render Pipeline projects before Unity 6.5/6.7 LTS planning; migration effort should be budgeted before support windows tighten.
- For Switch 2/HDRP ambitions, verify developer-program constraints and HDRP support in Unity 6.5 rather than assuming public availability.

## 2026-05-31 compile additions

### Claims
- The RealtimeVFX ShaderBoy/ShapeMesh source describes baking animated Maya procedural shader/component-color data into image sequences so stylized assets can move to Unity, Unreal, Blender, Houdini, Alembic, or other renderers that cannot use the original Maya shader network. confidence: 1 community/tooling source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-realtimevfx-baking-animated-maya-procedural-shaders-into-texture-seque.md]
- The source covers export controls such as texture resolution, frame range, file extension, output directory, shader-network rewiring, temporary shader swatches, API access, and cleanup of temporary nodes. confidence: 1 community/tooling source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-realtimevfx-baking-animated-maya-procedural-shaders-into-texture-seque.md]

### Typed entities
- DCC: Maya
- toolset: ShapeMesh
- feature/API: ShaderBoy / Bake Shader
- engine: Unity
- engine: Unreal Engine
- DCC: Blender
- DCC: Houdini
- format/workflow: Alembic
- concept: procedural shader baking
- artifact: texture sequence

### Explicit relationships
- Maya procedural shader networks depend-on baking when downstream engines/DCCs cannot reproduce animated procedural color logic.
- Texture sequences supersede nonportable procedural shader graphs for cross-DCC/engine export, at the cost of storage and resolution/frame-range decisions.

### HoneyDrunk implications
- For stylized animated assets, consider bake-to-texture-sequence as an interchange strategy before rebuilding procedural shader logic in every target engine.
- Validate storage size, playback performance, and material rewiring quality on representative Unity/Unreal scenes before using this in production.
