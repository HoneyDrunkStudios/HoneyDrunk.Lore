# Technical Art Community and Talent Signals

## Decision-useful summary
Polycount RSS items are noisy because the capture includes large forum scaffolding, but embedded schema.org snippets still provide usable public signals: active hiring for first-person weapon animation/rigging, artists offering Blender/ZBrush/Substance/Unity skillsets, and recurring environment-art challenges for real-time 3D practice and critique. Treat these as market/community signals, not vetted candidates or procurement data. [sources: raw/2026-05-07-rss-polycount-3d-artist-graphic-designer-fashion-designer.md; raw/2026-05-07-rss-polycount-paid-fps-weapon-animator-rigger-needed.md; raw/2026-05-07-rss-polycount-the-bi-monthly-environment-art-challenge-march-april-101.md]

## Claims
- A Polycount “Artists Looking For Work” post describes a public 3D artist/designer profile with Blender, ZBrush, Substance Painter, Unity, game-asset, and product-design experience. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-polycount-3d-artist-graphic-designer-fashion-designer.md]
- A Polycount freelance posting requests a paid first-person weapon animator/rigger for a tactical FPS project built in s&box / Source 2, with weapon model, rigged first-person arms, materials/textures, and reference examples available. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-polycount-paid-fps-weapon-animator-rigger-needed.md]
- Polycount's 101st bi-monthly environment-art challenge is positioned as a real-time 3D artist skill/practice/critique challenge open to all skill levels and based on provided concepts. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-polycount-the-bi-monthly-environment-art-challenge-march-april-101.md]
- The Polycount RSS captures include substantial forum JavaScript/theme scaffolding, so extracted schema snippets are more reliable than surrounding raw body text for these sources. confidence: 3 sources, last-confirmed 2026-05-07. [sources: raw/2026-05-07-rss-polycount-3d-artist-graphic-designer-fashion-designer.md; raw/2026-05-07-rss-polycount-paid-fps-weapon-animator-rigger-needed.md; raw/2026-05-07-rss-polycount-the-bi-monthly-environment-art-challenge-march-april-101.md]

## Typed entities
- platform/community: Polycount
- role: 3D artist
- role: graphic designer
- role: fashion designer
- role: first-person weapon animator/rigger
- project type: tactical FPS
- engine/platform: s&box / Source 2
- tool: Blender
- tool: ZBrush
- tool: Substance Painter
- engine: Unity
- concept: real-time environment art challenge
- source type: RSS/forum capture

## Explicit relationships
- technical-art hiring depends-on specialized animation, rigging, modeling, texturing, and engine-integration skill.
- Polycount RSS snippets provide public community/talent signals but depend-on follow-up vetting before outreach or hiring decisions.
- environment-art challenges reinforce skill-development/community-feedback channels for real-time 3D artists.
- forum capture scaffolding weakens content quality and should not supersede cleaner direct forum/API extraction.

## HoneyDrunk implications
- Polycount can be a sourcing surface for technical artists and challenge inspiration, but any candidate/job signal needs manual follow-up and portfolio review.
- If HoneyDrunk needs FPS/weapon animation or Source 2/s&box adjacent expertise, the role taxonomy here is worth preserving for future sourcing queries.
- Improve RSS extraction for forum sources by pulling schema.org JSON-LD fields directly and discarding theme scaffolding.

## Confidence and quality notes
- Quality posture: low-to-medium; useful as public market signal, not direct action evidence.
- Weak claims: candidate/job details are public snippets only and may be stale quickly.
- Privacy filter: no contact details copied; public usernames omitted unless needed for a later explicit sourcing query.

## 2026-05-23 compile additions

### Claims
- Anthropic's Blender Development Fund support is earmarked for Blender core development and foundational extensibility such as the Blender Python API; this is a creator-tool ecosystem signal rather than a direct product feature. confidence: 1 Blender Foundation source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-blender-releases-anthropic-joins-the-blender-development-fund-as-corpo.md]
- A RealtimeVFX boat-wake help thread shows continued practitioner demand for better real-time water-interaction approaches beyond simple mesh trails, especially when distance-field shader effects are already in use. confidence: 1 community source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-realtimevfx-looking-for-help-on-my-boat-wake.md]

### Typed entities
- organization: Blender Foundation
- company: Anthropic
- tool/API: Blender Python API
- community: RealtimeVFX
- concept: realtime water interaction
- concept: technical-art community signal

### Explicit relationships
- Blender Python API enables custom workflows for artists and developers.
- AI-lab funding of Blender supports the creative-tool substrate that LLM/MCP automation depends-on.

### HoneyDrunk implications
- Keep Blender automation on the technical-art roadmap; vendor ecosystem money is moving toward extensible creative tools.

## 2026-05-24 compile additions

### Claims
- 80 Level highlighted Ju Hwan Jeon's Persian Female Warrior character as a high-detail real-time Unreal Engine 5 render using 3ds Max, ZBrush, Substance 3D Painter, Marmoset Toolbag, Marvelous Designer, and Photoshop in the production stack. confidence: 1 art/trade source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-80-level-this-stunning-3d-persian-warrior-character-was-rendered-in-re.md]
- The source frames the artist goal as reimagining ancient Persian attire with modern ornaments while preserving a strong/elegant character silhouette; use this as art-direction reference signal, not as production-performance evidence. confidence: 1 art/trade source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-80-level-this-stunning-3d-persian-warrior-character-was-rendered-in-re.md]

### Typed entities
- artist: Ju Hwan Jeon
- project/artwork: Persian Female Warrior
- engine: Unreal Engine 5
- tool: 3ds Max
- tool: ZBrush
- tool: Substance 3D Painter
- tool: Marmoset Toolbag
- tool: Marvelous Designer
- tool: Photoshop
- concept: real-time character art
- concept: historically inspired character design

### Explicit relationships
- Real-time character art uses sculpting, modeling, texturing, garment, lookdev, and engine-rendering tools in combination.
- Art-direction reference signals do not supersede technical performance benchmarks for target scenes/devices.

### HoneyDrunk implications
- Preserve this as a character-art reference/toolchain signal for UE5-real-time character work; benchmark separately before assuming similar fidelity is viable in interactive scenes.

## 2026-05-30 compile additions

### Claims
- Black Eye 2.0's product/interview signal frames camera work as a technical-art and production-workflow concern: gameplay, cinematic, trailer, and virtual-production teams need shared camera behaviors rather than isolated code/keyframe systems. confidence: 1 80 Level interview source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-80-level-how-black-eye-2-0-is-rethinking-how-video-game-camera-systems.md; page: [[game-camera-systems]]]
- The source argues smaller teams benefit when camera tools provide subject tracking, adaptive framing, clean blending, collisions, and multi-character support without custom code for every case; treat as product-interview evidence requiring validation. confidence: 1 80 Level interview source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-80-level-how-black-eye-2-0-is-rethinking-how-video-game-camera-systems.md]
- Unity's 2026 render-pipeline strategy is a technical-art pipeline signal: Asset Store and education content are being encouraged toward URP compatibility as Built-In deprecation begins. confidence: 1 Unity source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-unity-render-pipelines-strategy-for-2026.md; page: [[unity-3d-and-realtime-vfx-patterns]]]

### Typed entities
- product/tool: Black Eye 2.0
- prior tool: Cinemachine
- engine: Unreal Engine
- concept: camera authoring
- concept: adaptive framing
- render pipeline: Unity URP
- render pipeline: Unity Built-In Render Pipeline
- content ecosystem: Unity Asset Store

### Explicit relationships
- Camera authoring depends-on both technical-art workflow and runtime systems engineering.
- URP migration affects technical artists because shader/material/content compatibility shifts with render-pipeline defaults.

### HoneyDrunk implications
- Track camera-system authoring as a technical-art competency, not only gameplay engineering.
- Prefer URP-compatible Unity assets and shader references when sourcing new Unity technical-art content.

## 2026-05-31 compile additions

### Claims
- BFX's RealtimeVFX post shows a technical-art portability pattern: bake Maya procedural shader channels driven by animation controls into texture sequences before exporting to other engines or DCC packages. confidence: 1 community/tooling source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-realtimevfx-baking-animated-maya-procedural-shaders-into-texture-seque.md; page: [[unity-3d-and-realtime-vfx-patterns]]]

### Typed entities
- person/source handle: BFX
- toolset: ShapeMesh
- API/tool: ShaderBoy
- concept: animated procedural shader export
- artifact: texture sequence

### Explicit relationships
- Technical-art portability depends-on converting DCC-specific procedural behavior into engine-readable textures when shader graph parity is not available.

### HoneyDrunk implications
- Preserve shader-baking workflows as technical-art sourcing terms for future Maya/Unity/Unreal pipeline research.

## 2026-06-01 compile additions

### Claims
- The image-to-3D for Unity source reinforces a technical-art validation role for AI-generated assets: mesh structure, multi-angle silhouette, UV/material quality, scale/origin, texture organization, polygon budget, and animation readiness must be checked before engine import. confidence: 1 DEV.to source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-image-to-3d-for-unity-what-to-check-before-importing-an-ai-generated-m.md; page: [[unity-3d-and-realtime-vfx-patterns]]]

### Typed entities
- workflow: AI image-to-3D asset review
- engine: Unity
- concept: technical-art import checklist

### Explicit relationships
- Technical-art review gates AI-generated models before Unity import.

### HoneyDrunk implications
- Preserve "AI asset intake checklist" as a future technical-art workflow term.

## 2026-06-02 compile additions

### Claims
- Adobe Photoshop API v2 in Firefly Services adds production creative-automation features relevant to technical art and content operations: linked smart objects, 5GB file support, UXP scripting, customizable action workflows, richer document/layer/artboard metadata, ICC color support, and flexible storage. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md; page: [[creative-automation-and-firefly-services]]]
- Photoshop API v1 end-of-life on 2026-07-31 makes v2 migration a technical-art pipeline concern for any existing server-side Photoshop automation. confidence: 1 Adobe documentation source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-adobe-developer-adobe-photoshop-api-firefly-services.md; page: [[creative-automation-and-firefly-services]]]

### Typed entities
- page: [[creative-automation-and-firefly-services]]
- product/API: Adobe Photoshop API v2
- platform: Firefly Services
- scripting runtime: UXP
- concept: linked smart object
- date/decision: 2026-07-31 Photoshop API v1 end of life

### Explicit relationships
- Server-side creative automation depends-on technical-art review for asset governance, color, layout, localization, and brand rules.
- Photoshop API v2 supersedes v1 for new automated content workflows.

### HoneyDrunk implications
- Track Firefly/Photoshop API v2 as a candidate for templated promotional/content-variant pipelines if HoneyDrunk needs scalable asset production.

## 2026-06-03 compile additions

### Claims
- 80 Level reports Sparseal is developing CozyBlanket Pro, a separate product from CozyBlanket focused on geometry cleanup, optimization, retopology, UV unwrapping, GPU-based UV packing, texture baking, and scene/object statistics. confidence: 1 80 Level source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-80-level-sparseal-announces-new-ai-assisted-retopology-tool.md]
- CozyBlanket Pro's topology prediction AI is described as continuously analyzing high- and low-poly meshes to provide real-time autocomplete suggestions, while keeping manual topology/UV tools available. confidence: 1 trade-press/source-author source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-80-level-sparseal-announces-new-ai-assisted-retopology-tool.md]
- Sparseal states CozyBlanket Pro's topology predictor and unwrapping algorithms are proprietary, built in-house, and not based on third-party AI inference services or licensed third-party solutions; this is vendor/product positioning and should be validated before procurement decisions. confidence: 1 source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-80-level-sparseal-announces-new-ai-assisted-retopology-tool.md]

### Typed entities
- company: Sparseal
- product: CozyBlanket Pro
- product: CozyBlanket
- product: Uniform
- product: Wafer
- workflow: AI-assisted retopology
- workflow: UV unwrapping
- workflow: GPU-based UV packing
- workflow: texture baking
- artifact: UDIM
- concept: topology prediction AI

### Explicit relationships
- AI-assisted retopology complements technical-art cleanup by suggesting topology while manual editing remains the authority.
- UV packing, texture baking, retopology, and DCC network bridges are technical-art workflow concerns, not just artist UI features.
- Proprietary in-house AI claims do not supersede licensing, privacy, and output-quality validation.

### HoneyDrunk implications
- Track CozyBlanket Pro as a technical-art scouting candidate for AI-generated or scanned mesh cleanup, but wait for open beta/licensing/platform details before adoption.
- If HoneyDrunk builds AI asset intake, retopology and UV/bake validation should be part of the checklist, not an optional polish step.

### Quality notes
- 80 Level is trade press and the product is closed beta. Claims are useful scouting signals, not tested production evidence.

## 2026-06-04 compile additions

### Claims
- Oscar Sanz's colored-shadow-penumbra UE5 guide, surfaced through 80 Level, is a technical-art shader modification signal: it targets the colored transition edge of dynamic-light shadows to improve visual clarity and stylization. confidence: 1 trade-press source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-80-level-how-to-implement-colored-penumbra-shadows-in-ue5.md; page: [[unity-3d-and-realtime-vfx-patterns]]]
- The same source says the approach is lightweight and supports all light types, but needs dynamic lights, wide penumbras, and global saturation control; baked lighting is outside scope. confidence: 1 trade-press source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-80-level-how-to-implement-colored-penumbra-shadows-in-ue5.md]
- A Tech-Artists.org forum post announces Houdini HDAs for real-world terrain generation after Mapbox-to-Houdini became unavailable, claiming automated terrain plus splatmaps and 1 m/px or 10 m/px USA resolution / 30 m/px global resolution. confidence: 1 forum/product post, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-tech-artists-org-real-world-terrain-for-houdini-replaces-mapbox-to-hou.md]

### Typed entities
- person: Oscar Sanz / Chosker
- engine: Unreal Engine 5
- technique: colored shadow penumbra
- DCC: Houdini
- artifact/tool: Houdini Digital Asset / HDA
- workflow: real-world terrain generation
- artifact: splatmap
- deprecated/missing tool: Mapbox-to-Houdini

### Explicit relationships
- Shader-level lighting modifications depend-on engine-version compatibility and dynamic-lighting constraints.
- Houdini terrain HDAs complement Unity/Unreal terrain workflows by generating engine-importable terrain and splatmaps.
- Forum/product posts require follow-up validation before procurement or pipeline standardization.

### HoneyDrunk implications
- Add "colored penumbra" and "dynamic-light shader edits" to stylized lighting research terms.
- If real-world terrain becomes relevant, validate Houdini HDA source/licensing, geographic data source, resolution, export formats, and engine-import quality before adopting.

## 2026-06-05 compile additions

### Claims
- Blender 5.2 LTS beta is a technical-art ecosystem signal because its updates touch texture-heavy rendering, Geometry Nodes simulation, Grease Pencil, mesh editing, audio sampling, and remote asset-library workflows. confidence: 1 80 Level source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-blender-5-2-lts-moves-into-beta.md; page: [[unity-3d-and-realtime-vfx-patterns]]]
- Real Fake Interiors is a Unity technical-art product signal for shader/bake-based environment optimization: fake depth interiors can reduce real geometry needs for building/window scenes while preserving per-instance variation controls. confidence: 1 RealtimeVFX product/community source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-released-real-fake-interiors-unity3d-bake-tool-shader-fake-rooms-that-lo.md; page: [[unity-3d-and-realtime-vfx-patterns]]]

### Typed entities
- DCC/tool: Blender 5.2 LTS
- concept: remote asset libraries
- product/tool: Real Fake Interiors
- technique: fake interior shader
- workflow: room bake

### Explicit relationships
- Blender beta features affect technical artists because DCC-side rendering/simulation/tooling changes can alter engine export and lookdev workflows.
- Fake-interior shaders complement environment art optimization by trading geometry for baked data and shader work.

### HoneyDrunk implications
- Preserve Blender 5.2 and fake-interior shader terms for future technical-art sourcing queries and prototype spikes.

### Quality notes
- Both sources are scouting signals, not validated HoneyDrunk pipeline evidence.

## 2026-06-08 compile additions

### Claims
- Unity's HP Anyware sunset guide says HP has ended new-customer sales of HP Anyware, Anyware Trust Center and Trusted Zero Clients reach end of support on 2026-10-31, and broader HP Anyware support/maintenance continues through 2029-10-31, making unsupported remote postproduction infrastructure a security/compliance risk. confidence: 1 Unity/Parsec source citing HP support dates, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-hp-anyware-is-being-sunset-a-practical-guide-for-postproduction-teams.md]
- The same source positions Parsec as a low-latency remote editorial/finishing option with GPU-side encoding, peer-to-peer encrypted streaming where media remains on the organization's storage, multi-monitor support, tablet input, SSO/SCIM/RBAC/audit logging in enterprise contexts, and High Performance Relay for firewall-constrained deployments. confidence: 1 Unity/Parsec source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-hp-anyware-is-being-sunset-a-practical-guide-for-postproduction-teams.md]
- Parsec does not currently support Linux hosts and is not optimized for fully air-gapped deployments, so Linux-only or isolated postproduction machines may need a hybrid remote-access plan. confidence: 1 Unity/Parsec source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-hp-anyware-is-being-sunset-a-practical-guide-for-postproduction-teams.md]
- Ryan Amos's technical-artist interview frames recurring production inefficiencies as lack of visibility, weak structure, inconsistent naming/folders, poor documentation, late validation, and manual repetitive work; he treats repeated breakage as a pipeline problem rather than an artist problem. confidence: 1 80 Level interview source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-technical-artist-on-building-tools-pipelines-and-blending-art-with-eng.md]
- The same interview recommends making profiling data actionable for artists through automated telemetry, frame reports, graphs/trends, clear targets, editor-integrated tools, inherent documentation, and artist feedback loops. confidence: 1 80 Level interview source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-technical-artist-on-building-tools-pipelines-and-blending-art-with-eng.md]
- Cairn's Unity technical-art deep dive describes a No-Piton Surface workflow that moved from 2D blendmaps to runtime-generated low-resolution Texture3D distance-field/blendmaps, then used a Compute Shader sharing shader logic to sample gameplay-valid piton-placement positions consistently with rendered rock material. confidence: 1 Unity developer deep dive, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-technical-art-deep-dive-how-cairn-renders-gameplay-specific-rock-mater.md; page: [[unity-3d-and-realtime-vfx-patterns]]]

### Typed entities
- product: HP Anyware
- product: HP Anyware Trust Center
- product: HP Trusted Zero Clients
- product: Parsec
- protocol: PCoIP
- control: SAML SSO
- control: SCIM
- control: RBAC
- control: audit logging
- concept: remote postproduction workstation
- role: technical artist
- person: Ryan Amos
- tool: Unreal Insights
- tool: PIX
- workflow: automated performance telemetry
- game: Cairn
- studio: The Game Bakers
- technique: 3D blendmap
- technique: Texture3D distance field
- technique: Compute Shader gameplay sampling

### Explicit relationships
- HP Anyware support sunset causes migration pressure for postproduction teams that depend-on secure remote editorial/VFX/finishing workstations.
- Parsec complements centralized media storage by streaming frames rather than project files, but does not supersede Linux-host or air-gap requirements.
- Technical-art pipeline quality depends-on early validation, visible performance costs, documentation, naming/folder standards, and editor-integrated tools.
- Automated performance telemetry converts low-level profiling data into artist-actionable reports.
- Cairn's No-Piton Surfaces use shared shader/compute logic to align gameplay permissions with material rendering.

### HoneyDrunk implications
- If HoneyDrunk ever supports remote artists/editors, inventory host OS, isolation needs, color/peripheral requirements, identity controls, and audit logging before selecting Parsec or another remote workstation stack.
- Treat technical-art tools as production infrastructure: build validation and visibility early instead of relying on artists to catch pipeline drift manually.
- For gameplay-specific materials, prefer shared data/logic between render shaders and gameplay validation to avoid visual/gameplay mismatch.

### Quality notes
- Unity/Parsec source is vendor-positioned; validate support dates against HP and feature/compliance claims against Parsec docs before procurement. 80 Level interview is practitioner evidence. Cairn is a strong shipped-game technical-art case study but project-specific.

## 2026-06-09 compile additions

### Claims
- Surface Forge's POM silhouette work identifies production pitfalls for POM in Unreal: missing self-shadowing, tangent-space light-direction rotation errors, normal-map rotation mismatch, brute-force step counts, and ineffective distance fades that do not compile out shader work. confidence: 1 80 Level technical-art source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-creating-rich-surface-details-like-crimson-desert-with-pom-silhouettes.md; page: [[unity-3d-and-realtime-vfx-patterns]]]
- The same source recommends heightmap quality, conservative height ratios, step-count dithering with Temporal AA, clean 0-1 face UVs for silhouette clipping, and StaticSwitch material LODs for POM performance. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-creating-rich-surface-details-like-crimson-desert-with-pom-silhouettes.md]
- Alex Arabi's Alley of Peace breakdown shows portfolio-scale environment production discipline: six-week half-time planning, reference/Google Maps scale checks, modular blockout, early Unreal camera composition, asset list from narrative questions, and iterative feedback across artists and non-artists. confidence: 1 80 Level interview source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-recreating-nostalgic-alley-of-peace-set-in-italy.md]
- The Alley source emphasizes technical-art material variation systems: world-position color tinting for repeated assets, vertex-paint breakup masks for wear, trim sheets for windows, secondary-UV RGB masks for grime/sun damage/edge wear, and decals to blend modular pieces. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-recreating-nostalgic-alley-of-peace-set-in-italy.md]
- The Unity manta ray source is a small but useful signal that Shader Graph and VFX Graph can support procedural GPU character/creature systems when mesh topology, randomization, optimization, and LOD swapping are designed together. confidence: 1 80 Level source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-procedural-manta-ray-system-made-with-unity.md]

### Typed entities
- person/creator: ArghanionsPuzzlebox
- product/tool: Surface Forge
- person/artist: Alex K. Arabi
- role: Environment Artist
- school: The Game Assembly
- location/reference: Vicolo della Pace / Sanremo, Italy
- person/artist: Jawad Srour
- technique: POM silhouette clipping
- technique: step-count dithering with TAA
- technique: trim sheet
- technique: RGB mask
- workflow: modular blockout
- workflow: GPU procedural animation

### Explicit relationships
- POM production quality depends-on heightmap authoring, tangent-space correctness, self-shadowing, silhouette UV assumptions, and material-LOD compilation.
- Portfolio environment workflows use modular kits, narrative-driven asset lists, material variation, set dressing, and lighting/post-processing to create cohesive scenes.
- GPU procedural animation depends-on mesh topology and LOD policy, not only shader graph logic.

### HoneyDrunk implications
- Add POM, trim-sheet/RGB-mask variation, world-position tinting, and vertex-paint breakup masks to technical-art reference patterns.
- For art reviews, ask for blockout, scale reference, material variation plan, focal path, lighting plan, and optimization/LOD notes before judging final polish.
- Keep 80 Level artist breakdowns as talent/practice signals, but require local replication before treating any technique as pipeline standard.

### Quality notes
- All three June 9 technical-art sources are public practitioner/trade-press signals. No private portfolio contact data was copied.

## 2026-06-10 compile additions: Hollowbody lighting and solo production signal

### Source-backed claims
- Hollowbody's retro visual identity uses low-poly assets, diffuse-texture emphasis, selective hero-asset detail, real-time fill/key lighting, and color grading to create a cyberpunk survival-horror mood inside solo-production constraints. Source: `raw/2026-06-10-web-80-level-how-hollowbody-blends-silent-hill-inspirations-with-cyberpunk-horror.md`. confidence: 1 source, last-confirmed 2026-06-10.
- The creator identifies game feel, movement/combat battle-testing, and greybox refinement as areas that should have received more time before atmosphere/art production. Source: `raw/2026-06-10-web-80-level-how-hollowbody-blends-silent-hill-inspirations-with-cyberpunk-horror.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: Hollowbody
- person: Nathan Hamley
- project: Headware Games
- concept: retro survival-horror art direction
- concept: greybox refinement

### Explicit relationships
- Hollowbody art direction depends-on production constraints as much as aesthetics.
- Movement/combat feel should precede final atmosphere work in survival-horror production.

### HoneyDrunk implications
- In portfolio or reference reviews, value evidence of constraint-driven lighting/composition decisions, not only final asset polish.
- For small horror prototypes, make game-feel proof a gate before final art pass.

### Quality notes
- Public trade source only; no private contact or portfolio data was copied.

## 2026-06-12 compile additions: Blender 5.2 assets and Cycles

### Source-backed claims
- Blender 5.2 LTS adds remotely hosted online asset libraries and extends the Essentials asset library with online-hosted assets, available in Blender when Allow Internet Access is enabled. Source: `raw/2026-06-12-web-blender-developer-documentation-assets-blender-developer-documentation.md`. confidence: 1 official Blender source, last-confirmed 2026-06-12.
- Blender 5.2 Cycles adds a texture cache for many-image scenes, generating `.tx` files that can reduce memory use and startup time at the cost of disk usage and some rendering-performance impact. Source: `raw/2026-06-12-web-blender-developer-documentation-cycles-blender-developer-documentation.md`. confidence: 1 official Blender source, last-confirmed 2026-06-12.
- Blender 5.2 Cycles exposes texture-cache controls for viewport simplification, OSL texture use, raycast attributes at intersection points, subsurface anisotropy updates, cast-shadows options for worlds, and geometry-memory/sync improvements. Source: `raw/2026-06-12-web-blender-developer-documentation-cycles-blender-developer-documentation.md`. confidence: 1 official Blender source, last-confirmed 2026-06-12.

### Typed entities
- DCC/tool: Blender 5.2 LTS
- renderer: Cycles
- feature: online asset libraries
- asset library: Essentials
- feature: Cycles texture cache
- artifact: `.tx` file
- feature: Raycast node attributes
- shader feature: subsurface anisotropy
- language/runtime: Open Shading Language / OSL

### Explicit relationships
- Blender online asset libraries depend-on user preference for internet access, so remote asset workflows have an explicit network/privacy control.
- Cycles texture cache trades disk and some render performance for lower image-texture memory pressure and faster startup in texture-heavy scenes.
- Raycast attributes connect geometry-node-style sampling with renderer-specific Cycles behavior; EEVEE does not provide the same output in this source.

### HoneyDrunk implications
- Validate Blender 5.2 texture-cache behavior on representative texture-heavy assets before adopting it as default lookdev/render guidance.
- Treat remote asset libraries as a governed asset-source surface: provenance, licensing, network access, and cache location matter for production work.

### Quality notes
- Official release documentation is high-quality for feature existence. Performance effect remains scene-dependent and requires local measurement.

## 2026-06-15 compile additions: GPU crowd and VFX texture sourcing

### Source-backed claims
- The 80 Level GPU crowd breakdown shows a complete technical-art pipeline spanning Houdini transform extraction, VAT baking, Unreal material logic, HISM spawning, UI-driven per-instance animation state, and performance profiling. Source: `raw/2026-06-15-web-80-level-novel-high-performance-framework-for-gpu-driven-crowd-systems.md`; page: [[unity-3d-and-realtime-vfx-patterns]]. confidence: 1 practitioner/trade source, last-confirmed 2026-06-15.
- VFXParlor is a free browser-based VFX texture tool with node-based editing and PBR map processing surfaced through RealtimeVFX community discussion. Source: `raw/2026-06-15-web-realtimevfx-new-free-online-vfx-procedural-textures-with-node-base-edi.md`; page: [[unity-3d-and-realtime-vfx-patterns]]. confidence: 1 community source, last-confirmed 2026-06-15.

### Typed entities
- page: [[unity-3d-and-realtime-vfx-patterns]]
- DCC/tool: Houdini
- engine: Unreal Engine
- technique: VAT
- technique: HISM
- tool/site: VFXParlor
- community: RealtimeVFX

### Explicit relationships
- Technical-art crowd pipelines depend-on DCC preprocessing, engine data import, shader logic, instancing, profiling, and artist-facing controls.
- Browser procedural texture tools complement community VFX sourcing by lowering setup cost for experimentation.

### HoneyDrunk implications
- Preserve VAT/HISM crowd systems and browser procedural texture editing as technical-art sourcing terms for future prototype spikes.

### Quality notes
- Both sources are public scouting signals. No private portfolio/contact data was copied.

## 2026-06-16 compile additions: Blender weekly technical-art signals

### Source-backed claims
- Blender's 2026-06-15 weekly update lists recent module changes including online asset-browser warning behavior, Geometry Nodes simulation catalog for dynamics assets, Grease Pencil input nodes, profile markers, GPU mipmap-update disable capability, USD normals export based on Blender's internal data model, and Texture Paint `update_pixels` parallelization. Source: `raw/2026-06-16-web-blender-15-june-2026-weekly-updates.md`. confidence: 1 official Blender Developer Forum weekly source, last-confirmed 2026-06-16.

### Typed entities
- DCC/tool: Blender
- module: Geometry Nodes
- module: Grease Pencil
- module: Texture Paint
- module: USD export
- feature: dynamics-assets simulation catalog
- feature: Grease Pencil input nodes
- feature: GPU mipmap-update disable
- feature: `update_pixels` parallelization

### Explicit relationships
- Blender weekly development signals complement release notes by showing near-term implementation movement across modules.
- Geometry Nodes dynamics catalogs and Grease Pencil input nodes reinforce Blender's procedural and 2D/3D hybrid technical-art direction.

### HoneyDrunk implications
- Keep Blender weekly updates as low-weight scouting input; promote only release-note or measured workflow changes into production guidance.

### Quality notes
- Official weekly update source. It is change-list evidence, not a stable-release adoption recommendation.

## 2026-06-19 compile additions: environment art co-development structure

### Source-backed claims
- The 80 Level/Virtuos environment-art co-development source argues that narrow asset-count briefs often produce technically correct but creatively disconnected work because environment art also carries lighting, set dressing, narrative logic, and world-believability decisions. Source: `raw/2026-06-19-web-80-lv-you-re-having-the-wrong-conversation-about-environment-art.md`. confidence: 1 trade/vendor source, last-confirmed 2026-06-19.
- The source describes three engagement levels for environment-art co-development: asset and prop production, modular kit building, and full end-to-end level art ownership, with scope expanding only as mutual trust and shared context grow. Source: `raw/2026-06-19-web-80-lv-you-re-having-the-wrong-conversation-about-environment-art.md`. confidence: 1 source, last-confirmed 2026-06-19.
- The source identifies common co-development failure modes as joining too late, art-direction drift, and underestimating the internal senior creative bandwidth required for review and alignment. Source: `raw/2026-06-19-web-80-lv-you-re-having-the-wrong-conversation-about-environment-art.md`. confidence: 1 source, last-confirmed 2026-06-19.

### Typed entities
- company: Virtuos
- project: Subnautica 2
- project: Dune: Awakening
- project: Kena: Bridge of Spirits
- workflow: environment art co-development
- workflow: modular kit building
- workflow: full end-to-end level art ownership
- concept: art direction drift

### Explicit relationships
- Environment art co-development depends-on shared style guides, lookdev, modular language, and regular art-director alignment.
- Modular kit building complements asset production by leaving reusable infrastructure after the engagement ends.
- Full level-art ownership depends-on trust and embedded creative dialogue; it should not supersede smaller-scope onboarding for a new partner.

### HoneyDrunk implications
- For game/interactive-world work, judge art partners by creative translation and pipeline fit, not only asset throughput.
- Plan internal art-direction review bandwidth before outsourcing or co-development; review time is part of the production cost.
- Use modular kit and lookdev deliverables as early gates before committing to large-scale environment production.

### Quality notes
- Source is vendor/trade content with portfolio examples. Useful as production-structure signal, not neutral procurement evidence.

## 2026-06-21 compile additions: Blender weekly signal

### Source-backed claims
- Blender Devtalk's 2026-06-08 weekly update is a low-weight technical-art signal covering ongoing Blender development work; promote only specific stable release-note items or measured workflow impacts into production guidance. Source: `raw/2026-06-21-web-blender-devtalk-8-june-2026.md`. confidence: 1 official forum weekly source, last-confirmed 2026-06-21.

### Typed entities
- DCC/tool: Blender
- source: Blender Devtalk weekly update
- concept: technical-art weekly signal

### Explicit relationships
- Blender weekly updates complement release notes by showing near-term development movement, but they do not supersede stable documentation.

### HoneyDrunk implications
- Keep Blender weekly updates as scouting input for technical-art tooling; wait for release notes or local tests before changing workflow defaults.

### Quality notes
- Official forum source, but still weekly/status material rather than stable adoption guidance.

## 2026-06-22 compile additions: painterly shaders and DCC bridge constraints

### Source-backed claims
- 80 Level's Lotus Design watercolor lantern source is a stylized technical-art reference: a Blender scene uses a watercolor shader, vertex paint, and multicolored hand-painted-like shadows to create a painterly 3D look. Source: `raw/2026-06-22-rss-80-lv-check-out-painterly-3d-lantern-created-with-a-watercolor-shader-.md`. confidence: 1 trade/art source, last-confirmed 2026-06-22.
- A Tech-Artists.org FBX Python SDK thread surfaces a DCC export limitation: `EXP_FBX_EMBEDDED` globally embeds media, while selectively excluding specific `FbxVideo` assets without losing filenames/relative filenames is not straightforward through the Python SDK. Source: `raw/2026-06-22-rss-tech-artists-org-fbx-python-sdk-selective-embedding.md`. confidence: 1 forum/practitioner source, last-confirmed 2026-06-22.
- A Tech-Artists.org post announces a free Maya-Blender Asset Bridge with a GitHub link, but the capture contains too little detail to evaluate license, quality, security, or pipeline fit. Source: `raw/2026-06-22-rss-tech-artists-org-free-maya-blender-asset-bridge.md`. confidence: 1 low-detail forum source, last-confirmed 2026-06-22.

### Typed entities
- DCC/tool: Blender
- technique: watercolor shader
- technique: vertex paint
- concept: painterly 3D lighting
- SDK: FBX Python SDK
- class/entity: `FbxVideo`
- export flag: `EXP_FBX_EMBEDDED`
- DCC/tool: Maya
- DCC/tool: Blender
- tool: Maya-Blender Asset Bridge

### Explicit relationships
- Painterly 3D looks depend-on shader design, vertex-paint data, lighting, and art direction, not only texture assets.
- FBX media embedding depends-on SDK-level export behavior; missing selective embedding support can force risky filesystem or C++/binary-level workarounds.
- DCC bridge tools complement manual export/import workflows but depend-on license, version support, data fidelity, and security review before pipeline adoption.

### HoneyDrunk implications
- Preserve watercolor shader, vertex-paint shadow coloration, and painterly 3D as stylized-look research terms.
- For asset-pipeline automation, validate FBX media-reference behavior before relying on embedded files in build/release tools.
- Inspect the Maya-Blender bridge repository, license, supported data types, and failure modes before treating it as usable tooling.

### Quality notes
- 80 Level is visual-reference/trade evidence. Tech-Artists threads are practitioner discovery sources and need follow-up before production use.

## 2026-06-23 compile additions: beginner Blender learning and Materialist shelf

### Source-backed claims
- The Polycount "Learning Blender and Texturing" capture is a large forum page with heavy scaffolding and discussion noise; it is useful mainly as a community-learning/source-quality signal rather than a specific production technique. Source: `raw/2026-06-23-rss-polycount-learning-blender-and-texturing.md`. confidence: 1 noisy forum capture, last-confirmed 2026-06-23.
- A Tech-Artists.org post announces Materialist, a free Maya material-manager shelf; the capture is short and should be treated as discovery only until the linked tool, license, compatibility, and workflow behavior are inspected. Source: `raw/2026-06-23-rss-tech-artists-org-free-tool-materialist-a-material-manager-shelf-for-ma.md`. confidence: 1 low-detail forum source, last-confirmed 2026-06-23.

### Typed entities
- DCC/tool: Blender
- community: Polycount
- DCC/tool: Maya
- tool: Materialist
- concept: material manager shelf
- concept: noisy forum capture

### Explicit relationships
- Forum captures complement technical-art scouting by revealing learning pain points and tool discovery, but they rarely supersede tool docs or measured pipeline tests.
- Material-management shelves complement DCC workflow automation, but depend-on license, version support, dependency review, and data-fidelity tests.

### HoneyDrunk implications
- Keep beginner Blender/texturing friction in mind for onboarding and documentation, but do not promote the Polycount capture into workflow guidance.
- Inspect Materialist directly before adding it to any Maya pipeline watchlist or automation backlog.

### Quality notes
- Both sources are community/forum captures; one is noisy and one is low-detail.

## 2026-06-28 compile additions: alien vegetation workflow

### Source-backed claims
- 80 Level's Morgane Muller interview describes a student alien-island vegetation workflow using SpeedTree, Substance 3D Designer, WorldCreator, Unreal Engine PCG, Lumen, Movie Render Queue, and reference research into savannah vegetation and geology. Source: `raw/2026-06-28-rss-80-level-setting-up-vegetation-for-alien-planet-in-3d.md`. confidence: 1 trade/interview source, last-confirmed 2026-06-28.
- The source says the workflow created different plant types with different SpeedTree approaches, used procedural variance for diversity without breaking the overall plant identity, and grouped plants into sub-biomes for Unreal PCG scattering. Source: `raw/2026-06-28-rss-80-level-setting-up-vegetation-for-alien-planet-in-3d.md`. confidence: 1 source, last-confirmed 2026-06-28.
- The texturing workflow used SpeedTree-derived gradient, RGB element, AO, normal, opacity, noise, and ID maps inside Substance 3D Designer to drive color variation, masks, highlights, and volume cues. Source: `raw/2026-06-28-rss-80-level-setting-up-vegetation-for-alien-planet-in-3d.md`. confidence: 1 source, last-confirmed 2026-06-28.
- The final scene used Unreal lighting controls including Lumen, directional light, skylight/HDRI, volumetric fog, sky atmosphere, post-processing, black-and-white composition checks, and cinematic aspect framing. Source: `raw/2026-06-28-rss-80-level-setting-up-vegetation-for-alien-planet-in-3d.md`. confidence: 1 source, last-confirmed 2026-06-28.

### Typed entities
- artist: Morgane Muller
- tool: SpeedTree
- tool: Substance 3D Designer
- tool: WorldCreator
- engine: Unreal Engine
- feature: Unreal PCG
- renderer/lighting: Lumen
- tool: Movie Render Queue
- concept: procedural variance
- concept: sub-biome scattering
- concept: BMS and Gestalt theory

### Explicit relationships
- Believable stylized vegetation depends-on real biome research, procedural variation, texture masks, and composition/lighting discipline.
- SpeedTree-derived maps complement Substance Designer graphs by giving procedural textures plant-structure awareness.
- Unreal PCG scattering depends-on asset grouping and sub-biome rules, not only random placement.

### HoneyDrunk implications
- For environment-art studies, capture technical maps and scattering rules as reusable workflow knowledge, not just final renders.
- Validate whether SpeedTree/Designer/Unreal PCG is overkill for small prototypes; use the workflow as a reference when vegetation diversity matters.
- For stylized alien biomes, preserve a real-world ecological basis so the scene reads as plausible instead of arbitrary.

### Quality notes
- 80 Level is trade/interview evidence and the project is educational. Useful as technical-art reference, not production pipeline proof.
