# Gamedev Production and Community Signals

## Decision-useful summary
The game-development community feed produced a mix of process advice, tooling experiments, migration methodology, Web3 fairness architecture, job-market signal, AI-assisted production case studies, hybrid app/engine case studies, and novelty projects. Durable points: structured phased production reduces drift; Flash-to-HTML5 migrations should reverse-engineer behavior and rewrite cleanly rather than port decompiled ActionScript; dynamic blockchain games need explicit trust boundaries; small cross-platform libraries, newsletters, and AI-assisted experiments are discovery signals, not adoption proof. [sources: raw/2026-05-04-rss-dev-to-unity-our-4-phase-game-development-process-from-concept-to-laun.md; raw/2026-05-06-rss-dev-to-gamedev-legacy-flash-to-modern-html5-a-developer-s-migration-gu.md; raw/2026-05-06-rss-dev-to-gamedev-when-a-digital-horse-runs-the-fairness-problem-behind-a.md; raw/2026-05-05-rss-dev-to-gamedev-first-release-of-ldl-0-1-a-small-library-with-a-big-sou.md; raw/2026-05-05-rss-dev-to-gamedev-i-built-a-minecraft-mod-where-every-sword-is-an-aws-ser.md; raw/2026-05-04-rss-tech-artists-org-lighting-td-atlantis-animation-santa-cruz-de-tenerife.md; raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md; raw/2026-05-11-rss-dev-to-unity-building-coach-ivy-embedding-a-unity-avatar-inside-a-flut.md; raw/2026-05-11-rss-dev-to-unity-game-dev-digest-issue-330-unity-ai-game-art-and-more.md]

## Claims
- Ocean View Games describes a four-phase game-development process from concept to launch intended to reduce drift, missed deadlines, and budget overruns in messy creative/technical work. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-dev-to-unity-our-4-phase-game-development-process-from-concept-to-laun.md]
- Ocean View Games' Flash migration guide says lost-source Flash projects should use decompiled SWFs as reference evidence, document screens/interactions, then rewrite cleanly for HTML5 rather than directly porting decompiled ActionScript. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-gamedev-legacy-flash-to-modern-html5-a-developer-s-migration-gu.md]
- The same guide positions Phaser + TypeScript as a practical sweet spot for many 2D Flash-to-HTML5 game migrations, with Unity WebGL reserved for complex applications where full-engine weight is justified. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-gamedev-legacy-flash-to-modern-html5-a-developer-s-migration-gu.md]
- Flash migration performance budgets should be set by the weakest target hardware, especially in education deployments; parity testing matters because lesson plans may depend on exact interactions. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-gamedev-legacy-flash-to-modern-html5-a-developer-s-migration-gu.md]
- A Web3 horse-racing design article argues that AI can run dynamic simulations off-chain while blockchain records ownership/rules/final records, but fairness depends on making the trust boundary visible, inspectable, replayable, or challengeable. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-gamedev-when-a-digital-horse-runs-the-fairness-problem-behind-a.md]
- The Web3 horse-racing article frames game uncertainty as structured uncertainty: outcomes should not be fully predictable or fully random, and auditability should constrain excitement tuning. confidence: 1 source, last-confirmed 2026-05-06. [source: raw/2026-05-06-rss-dev-to-gamedev-when-a-digital-horse-runs-the-fairness-problem-behind-a.md]
- LDL 0.1 (Little Directmedia Layer) is presented as a small cross-platform C-oriented library/API intended to run across roughly 30 years of computer history. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-dev-to-gamedev-first-release-of-ldl-0-1-a-small-library-with-a-big-sou.md]
- A Minecraft mod article demonstrates a novelty AI-assisted build where swords represent AWS services such as Lambda, S3, and EC2-like scaling concepts. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-05-rss-dev-to-gamedev-i-built-a-minecraft-mod-where-every-sword-is-an-aws-ser.md]
- Atlantis Animation posted a Lighting TD role in Santa Cruz de Tenerife, indicating ongoing demand for technical art / lighting specialists in animation production. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-tech-artists-org-lighting-td-atlantis-animation-santa-cruz-de-tenerife.md; raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]
- Game Dev Digest issue #329 is a broad newsletter aggregation across game design, tools, AI, programming, and Unity/C# news; it is useful for discovery but weaker as primary evidence. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-04-rss-dev-to-unity-game-dev-digest-issue-329-game-design-tools-ai-programmin.md]
- The CivicSurvival case study shows a large AI-assisted Cities: Skylines II mod using Unity DOTS/ECS, custom RAG/MCP navigation, Roslyn analyzers, logs, and audits; it is useful as process evidence but self-reported and not an independent benchmark. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]
- Coach Ivy shows a product-led architecture decision for mobile game-like UX: use Flutter for normal app/product surfaces and embed Unity only for the reactive 3D avatar layer. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-rss-dev-to-unity-building-coach-ivy-embedding-a-unity-avatar-inside-a-flut.md]
- Game Dev Digest issue #330 reinforces that Unity AI, GPU-driven art/VFX, localization, tagging, virtual file systems, and asset bundles are active Unity discovery topics, but the Digest itself is an aggregator. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-rss-dev-to-unity-game-dev-digest-issue-330-unity-ai-game-art-and-more.md]
- Game Dev Digest issue #331 surfaces Unity discovery topics around Unity AI Assistant quality, Unity MCP, AI UI generation/prototyping, grass systems, GC-spike avoidance with Native Collections/Burst, logging pipeline customization, behavior-tree/editor tools, deterministic voxel grids, floating-origin multiplayer worlds, mesh fracture, runtime sprite baking, prefab thumbnails, and Unity path tracing; treat it as a link queue, not primary evidence. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-17-rss-dev-to-unity-game-dev-digest-issue-331-ai-opinions-grass-system-how-to.md]

## Typed entities
- organization: Ocean View Games
- game: The Great Fire of London
- platform/runtime: Adobe Flash
- technology: HTML5
- library: Phaser
- language: TypeScript
- tool: JPEXS Free Flash Decompiler
- concept: behavior specification
- concept: parity testing
- concept: structured uncertainty
- concept: trust boundary
- platform: blockchain
- ecosystem: Polkadot / Substrate
- library: LDL / Little Directmedia Layer
- game/platform: Minecraft
- platform: AWS
- service: AWS Lambda
- service: Amazon S3
- service: Amazon EC2
- organization: Atlantis Animation
- role: Lighting TD
- source/series: Game Dev Digest
- project/mod: CivicSurvival
- game: Cities: Skylines II
- concept: AI-assisted gamedev process
- framework/runtime: Flutter
- concept: hybrid mobile app/engine architecture
- source/series: Game Dev Digest issue #330
- source/series: Game Dev Digest issue #331
- tool: Unity AI Assistant
- protocol/tooling: Unity Model Context Protocol / Unity MCP
- library: Native Collections
- compiler/runtime feature: Burst
- library/tool: FishNet floating origin
- concept: deterministic voxel grid
- concept: runtime sprite baking

## Explicit relationships
- Flash-to-HTML5 migration depends-on source-code availability, asset extraction, behavior documentation, target technology choice, responsive UI work, performance optimization, and parity testing.
- Decompilation contradicts direct-port assumptions because decompiled ActionScript should be reference evidence, not the maintainable codebase.
- Phaser + TypeScript uses web-native rendering/runtime patterns to replace Flash display-list style 2D applications.
- Off-chain AI simulation depends-on blockchain settlement/recording for dynamic Web3 game trust.
- Blockchain records final truth but contradicts expectations that it can cheaply run complex AI/race simulations on-chain.
- phased game-development process fixed project drift by giving concept-to-launch structure.
- LDL uses one API to target a wide historical range of platforms.
- Minecraft AWS sword mod uses AI-assisted development as an implementation accelerator and maps AWS services to game mechanics.
- Lighting TD role depends-on technical art and production-lighting skills.
- Game Dev Digest reinforces discovery coverage but depends-on linked sources for primary evidence.
- CivicSurvival uses AI-assisted implementation with RAG/analyzers/logs to constrain large gamedev system changes.
- Coach Ivy uses a Flutter app shell plus embedded Unity avatar layer to separate product state from character/3D rendering.
- Game Dev Digest uses newsletter aggregation to surface discovery queues, but depends-on primary links for evidence.
- Unity AI Assistant/MCP discovery depends-on direct Unity docs and local editor tests before adoption.

## HoneyDrunk implications
- For internal game prototypes, start with a lightweight phase gate: concept, prototype, production, launch/learn.
- If reviving legacy interactive content, specify behavior first and rewrite cleanly; do not treat recovered/decompiled code as architectural truth.
- For any AI+blockchain/game experiment, write the trust-boundary contract before the economy: what is recorded, replayable, independently checkable, and operator-dependent.
- Novel AI/game demos are good marketing and learning artifacts; do not mistake them for product-market validation.
- Track technical-art talent and reusable shader/VFX resources if Lore/Grid visual production ramps up.
- Treat AI-assisted gamedev case studies as process patterns; validate with HoneyDrunk-specific builds and playtests before adopting wholesale.
- Use Game Dev Digest #331 as a scouting queue for Unity MCP/editor-agent experiments and performance tooling, but inspect the linked primary sources before committing time.
- For character-led app concepts, decide early whether Unity is the whole app or a bounded embedded scene; bounded is usually easier to maintain when commerce/navigation/content flows dominate.

## Confidence and quality notes
- Quality posture: mixed; process/migration/trust-boundary claims are decision-useful, Web3 article is architectural opinion, newsletter aggregation is low-authority, and self-reported case studies need local validation.
- Weak claims: AWS Minecraft mod and LDL need repo/docs inspection before technical adoption; Polkadot/Substrate claim is source-author interest, not an independent recommendation.
- Privacy filter: no private person details copied beyond public author/org/role names.

## 2026-05-18 compile additions

### Claims
- Albion Online is a long-running Unity MMO architecture case study: a small team sustained cross-platform PvP by using a single Unity project, strict simulation/visualization separation, platform-specific controls/UI, CI validation, local full-stack dev loops, and community-informed platform/server decisions. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-architecting-albion-online-how-sandbox-interactive-built-a-.md]
- Sandbox Interactive reports that splitting Albion Online from one US global server to Asia and Europe servers improved latency, made combat more reactive, and boosted player numbers, while fragmenting the community somewhat. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-architecting-albion-online-how-sandbox-interactive-built-a-.md]
- Unity for Humanity 2026 is a real-time-3D/social-impact funding signal, with projects spanning self-care games, climate/AR education, VR rehab, MR burn training, language preservation, adaptive sports, and care-worker empathy training. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-unity-blog-unity-for-humanity-2026-winner-announcement.md]

### Typed entities
- game: Albion Online
- studio: Sandbox Interactive
- pattern: community-informed live operations
- pattern: regional server split
- program: Unity for Humanity
- concept: real-time 3D for social impact

### Explicit relationships
- Cross-platform live games depend-on CI validation, input-specific control design, and weakest-device performance baselines.
- Community feedback caused Albion Online server-region expansion, but final product decisions remained with the studio.
- Impact-game funding depends-on measurable audience/problem fit, prototype/distribution plans, and social-good alignment.

## 2026-05-23 compile additions

### Claims
- Game Developer's Patch Notes #53 reports imminent Bungie layoff concerns, a new studio by former BioWare developers, GTA VI still targeting November, Xbox leadership changes, and Nex Playground expansion; the captured article is noisy but useful as industry-market signal. confidence: 1 trade-press source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-game-developer-layoffs-imminent-at-bungie-former-bioware-devs-launch-n.md]
- Game Developer reports Take-Two expects approximately $8B in FY27 revenue, driven by Grand Theft Auto VI, and notes Grand Theft Auto V is nearing 230M lifetime sales. confidence: 1 trade-press source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-game-developer-take-two-expects-to-earn-8b-in-fy27-thanks-to-grand-the.md]

### Typed entities
- company: Bungie
- company: BioWare
- company: Take-Two Interactive
- franchise/game: Grand Theft Auto VI
- franchise/game: Grand Theft Auto V
- product/company: Nex Playground
- concept: game industry layoffs
- concept: AAA launch revenue concentration

### Explicit relationships
- Take-Two FY27 outlook depends-on Grand Theft Auto VI launch performance.
- AAA market expectations can distort game-industry revenue signals because one franchise launch dominates annual projections.

### HoneyDrunk implications
- Treat AAA financial headlines as market climate/context, not directly transferable indie revenue evidence.
- Layoff/new-studio signals may matter for talent availability and partner scouting, but need primary/local follow-up before action.

## 2026-05-24 compile additions

### Claims
- Game Developer reports Subnautica 2 sold four million copies within a week of its 2026-05-14 Early Access launch, including two million copies in the first 12 hours per Gematsu/press-release reporting. confidence: 1 trade-press source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-game-developer-subnautica-2-hits-four-million-sales.md]
- The same source notes Subnautica 2 had “very positive” Steam reviews and launched successfully despite a high-profile legal dispute between ousted Unknown Worlds leadership and Krafton. confidence: 1 trade-press source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-game-developer-subnautica-2-hits-four-million-sales.md]

### Typed entities
- game: Subnautica 2
- studio: Unknown Worlds
- company: Krafton
- platform: Steam
- launch model: Early Access
- concept: community-feedback-driven development

### Explicit relationships
- Subnautica 2 Early Access performance reinforces that established IP plus community feedback can produce strong early sales despite corporate/legal turbulence.
- Early Access success depends-on ongoing community feedback, but initial sales also depends-on franchise reputation and launch visibility.

### HoneyDrunk implications
- Treat Subnautica 2 as AAA/established-IP market signal, not indie baseline; the durable lesson is that Early Access must be paired with credible community-feedback loops.

## 2026-05-30 compile additions

### Claims
- The RuneScape networking teardown shows 2004 Jagex optimized multiplayer protocol design around hard dial-up constraints: small opcodes, variable/fixed packet bodies, waypoint deltas, bit-packed movement/update flags, relative coordinates, and cached byte-aligned detail buffers. confidence: 1 reverse-engineering source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md; page: [[realtime-game-network-protocol-design]]]
- The durable production lesson is constraint-driven architecture: tight protocol co-design is right when client/server ship together and bandwidth is binding, while verbose self-describing protocols remain right when independent deployability/debugging/change velocity are binding. confidence: 1 reverse-engineering source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md; page: [[realtime-game-network-protocol-design]]]
- Black Eye 2.0 reinforces camera systems as production infrastructure: fragile special-case camera code slows iteration, while adaptive/directable camera behaviors can support gameplay, cinematic, trailer, and virtual-production work from one system. confidence: 1 80 Level interview source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-80-level-how-black-eye-2-0-is-rethinking-how-video-game-camera-systems.md; page: [[game-camera-systems]]]

### Typed entities
- game: RuneScape
- company: Jagex
- page: [[realtime-game-network-protocol-design]]
- product/tool: Black Eye 2.0
- page: [[game-camera-systems]]
- concept: constraint-driven architecture
- concept: adaptive camera system

### Explicit relationships
- Realtime game protocol design depends-on the binding constraint: bandwidth, latency, server assembly cost, debuggability, or independent deployability.
- Camera systems depend-on iteration-friendly authoring models because gameplay and cinematic needs change throughout production.

### HoneyDrunk implications
- For multiplayer or networked simulation prototypes, choose protocol verbosity/compactness based on actual deployment/versioning constraints.
- Treat cameras and networking as first-order production systems early in game prototypes, not polish-layer details.

## 2026-05-31 compile additions

### Claims
- The data-driven ability/combat system source argues that abilities should be first-class data assets with composed primitives for costs, cooldowns, targeting, effects, tags, and instancing rather than bespoke handwritten scripts per ability. confidence: 1 source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-dev-to-gamedev-building-a-data-driven-ability-combat-system.md]
- The source recommends a small canonical runtime model: `AbilityDefinition`, `EffectSpec`, `AttributeSet`, tag taxonomy, and `TargetingDescription`, with runtime components for ability ownership, cooldowns, effect buffers, and targeting. confidence: 1 source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-dev-to-gamedev-building-a-data-driven-ability-combat-system.md]
- For multiplayer combat, the source recommends server-authoritative resolution, client-side prediction for feel-critical actions, sanitized target snapshots, rate limits, batching, reconciliation, and lag-compensated targeting where appropriate. confidence: 1 source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-dev-to-gamedev-building-a-data-driven-ability-combat-system.md]
- The source treats balancing as a telemetry/live-ops loop: every activation, resolve outcome, cancel, tick, rollback, and major attribute change should emit events, and numeric changes should roll out through remote config/experiments with a kill switch. confidence: 1 source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-dev-to-gamedev-building-a-data-driven-ability-combat-system.md]

### Typed entities
- concept: data-driven ability system
- artifact: `AbilityDefinition`
- artifact: `EffectSpec`
- artifact: `AttributeSet`
- artifact: gameplay tag taxonomy
- artifact: `TargetingDescription`
- pattern: server-authoritative combat
- pattern: client-side prediction
- pattern: lag compensation
- product/service: Unity Remote Config
- product/service: PlayFab Experiments
- product/service: GameAnalytics

### Explicit relationships
- Ability systems use data assets to separate designer tuning from engine execution.
- Server-authoritative resolution depends-on sanitized client intents and authoritative attribute mutation.
- Client prediction complements authoritative resolution when feel matters but cannot supersede server validation.
- Live balancing depends-on telemetry, staged rollout, and rollback controls rather than manual guesswork.

### HoneyDrunk implications
- If HoneyDrunk prototypes combat, start with an ability schema, tag taxonomy, telemetry event taxonomy, and server-authority contract before adding many effects.
- Treat designer scripting hooks as curated APIs; direct attribute writes from scripts should be blocked outside the effect system.

## 2026-06-01 compile additions

### Claims
- The mobile reward-economy source defines a reward economy as the system of reward types, timing, value, and behavioral purpose across daily rewards, missions, battle passes, level rewards, rewarded ads, gacha, and events; it distinguishes reward delivery from the currency economy. confidence: 1 DEV.to gamedev source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-how-to-build-a-reward-economy-for-a-mobile-game.md]
- The source argues each reward type should have a distinct behavioral role: daily rewards drive return visits, missions direct behavior, battle passes anchor long-term engagement, level rewards celebrate progress, ads monetize attention, gacha acquires rare items, and events re-engage players. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-how-to-build-a-reward-economy-for-a-mobile-game.md]
- The source recommends balancing reward sources against each other because stacking too many high-value rewards devalues the economy; gacha drop rates and pity systems are framed as trust/ethics requirements. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-how-to-build-a-reward-economy-for-a-mobile-game.md]

### Typed entities
- concept: mobile reward economy
- reward type: daily login reward
- reward type: mission reward
- reward type: battle pass reward
- reward type: level reward
- reward type: rewarded ad
- reward type: gacha
- reward type: event reward
- control: gacha drop-rate disclosure
- control: pity system

### Explicit relationships
- Reward economy depends-on currency economy but is not identical to it.
- Battle pass rewards use season XP and tier structure to create retention loops.
- Gacha trust depends-on published rates and pity rules.
- Events can cause inflation when injected rewards exceed available sinks.

### HoneyDrunk implications
- For mobile/free-to-play concepts, define reward behavioral intent and sink/source balance before implementation.
- Treat gacha, ads, and FOMO events as trust-sensitive systems requiring policy/design review, not only economy math.

## 2026-06-02 compile additions

### Claims
- GameMaker launched GMRT and GM-CLI to support larger teams, broader language backgrounds, preferred external environments, automation, API access, GitHub Actions, MCP Server use, and optional Claude Code-assisted workflows. confidence: 1 Game Developer trade-press source quoting GameMaker, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-game-developer-gamemaker-incorporates-claude-code-to-enable-ai-assiste.md]
- GameMaker head Russell Kay described the AI tooling as opt-in and complementary, with developers deciding whether to use it; the underlying production signal is that game tools are adding CLI/API/MCP automation surfaces around engines that were historically IDE-centric. confidence: 1 Game Developer trade-press source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-game-developer-gamemaker-incorporates-claude-code-to-enable-ai-assiste.md]

### Typed entities
- engine/tool: GameMaker
- runtime: GMRT
- command-line tool: GM-CLI
- product: Claude Code
- protocol: MCP Server
- platform: GitHub Actions
- company: Opera

### Explicit relationships
- GameMaker GM-CLI uses command-line/API access to enable automation and AI-assisted workflows outside the IDE.
- Optional AI assistance complements, but does not supersede, conventional engine/runtime/toolchain workflows.

### HoneyDrunk implications
- When evaluating engines, include CLI/API/build automation and MCP/scriptability as first-class criteria because AI-assisted workflows need machine-operable project surfaces.

## 2026-06-03 compile additions

### Claims
- Turnkit's article frames hybrid turn-based multiplayer as a production-speed tradeoff: a generic server owns turn enforcement, hidden-data visibility, reconnects, and event flow while teams avoid duplicating every rule on a custom authoritative server. confidence: 1 self-authored product/source article, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-dev-to-kill-the-double-coding-tax-a-hybrid-approach-to-authoritative-m.md]
- Game Developer's Control Resonant interview describes Remedy's "vision propagation" practice: a creative director and discipline leads workshop core pillars early, then leads translate that vision into team-level ownership and production decisions. confidence: 1 trade-press interview source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-game-developer-how-to-direct-unconventional-games-like-control-resonan.md]
- The Control Resonant source frames production alignment as especially important for unconventional genres/settings because new mechanics and strange worlds have few obvious external references; top-down forcing is presented as less effective than team investment and the ability to drop ideas that do not work. confidence: 1 trade-press interview source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-game-developer-how-to-direct-unconventional-games-like-control-resonan.md]

### Typed entities
- product/service: Turnkit
- game: Control Resonant
- studio: Remedy Entertainment
- person: Mikael Kasurinen
- concept: vision propagation
- concept: discipline leads
- concept: unconventional game production
- concept: hybrid turn-based multiplayer

### Explicit relationships
- Hybrid turn-based server patterns trade strict server-authored game rules for lower duplicated implementation cost and generic authority services.
- Vision propagation depends-on early shared pillar work and lead-level ownership rather than a director repeatedly restating the same top-down instruction.
- Unconventional game production depends-on stronger internal alignment because fewer genre conventions can serve as external decision rails.

### HoneyDrunk implications
- For small turn-based prototypes, consider generic authority services only after deciding what cheating/collusion risk is acceptable for the match type.
- For unusual HoneyDrunk game concepts, write core pillars and ownership boundaries early, then let discipline leads/tool owners translate them into concrete constraints and kill criteria.

### Quality notes
- Turnkit is a self-authored product source; Remedy is a trade-press interview. Both are production-pattern signals, not universal process proof.

## 2026-06-04 compile additions

### Claims
- Ludeo's Indie Program lets Steam developers convert gameplay clips into instantly playable snippets and offers creator marketing support, integration help, creator access, grants up to $10,000, and possible top-campaign support up to $50,000. confidence: 1 trade-press source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-80-level-ludeo-converts-clips-of-your-games-into-instantly-playable-sn.md]
- Ludeo is positioned as a creator-driven discovery funnel: playable snippets reduce the gap between watching a creator clip and trying the game, similar in intent to playable ads, cloud-streamed demos, browser demos, and instant trials. confidence: 1 trade-press source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-80-level-ludeo-converts-clips-of-your-games-into-instantly-playable-sn.md]
- Unity Pipeline Automation reinforces that production scale in 3D/games often shifts bottlenecks from scene creation to repeatable asset processing, validation, format conversion, and notification pipelines. confidence: 1 Unity source, last-confirmed 2026-06-04. [source: raw/2026-06-04-rss-unity-blog-what-is-unity-pipeline-automation.md; page: [[unity-3d-and-realtime-vfx-patterns]]]

### Typed entities
- company/product: Ludeo
- program: Ludeo Indie Program
- platform: Steam
- concept: playable gameplay snippet
- concept: creator-driven discovery
- product: Unity Pipeline Automation
- workflow: asset processing pipeline

### Explicit relationships
- Playable snippets use creator content as a direct acquisition funnel rather than only awareness media.
- Creator discovery depends-on reducing friction from watch intent to playable experience.
- 3D production pipelines depend-on asset validation, conversion, processing, and collaboration automation as projects scale.

### HoneyDrunk implications
- For small game launches, evaluate playable-snippet marketing only after checking SDK/integration cost, player-data/privacy terms, platform constraints, and whether the game has compelling short moments.
- Treat creator marketing support as distribution signal, not proof that a game concept will retain players after the snippet.

## 2026-06-10 compile additions: Hollowbody solo-production lessons

### Source-backed claims
- Hollowbody's production shows a solo developer using retro visual constraints, fixed-camera survival horror conventions, Unity, and PlayMaker to keep a cyberpunk horror project shippable. Source: `raw/2026-06-10-web-80-level-how-hollowbody-blends-silent-hill-inspirations-with-cyberpunk-horror.md`. confidence: 1 source, last-confirmed 2026-06-10.
- The creator's strongest postmortem lesson is to spend more time battle-testing movement, combat, game feel, and greybox layout before investing heavily in atmosphere and finished art. Source: `raw/2026-06-10-web-80-level-how-hollowbody-blends-silent-hill-inspirations-with-cyberpunk-horror.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: Hollowbody
- person: Nathan Hamley
- project: Headware Games
- concept: solo game production
- concept: survival-horror greyboxing

### Explicit relationships
- Solo production depends-on disciplined scope constraints and fast pivoting.
- Survival-horror atmosphere depends-on movement/combat/layout fundamentals being tested first.

### HoneyDrunk implications
- For HoneyDrunk game prototypes, require playable feel and navigation evidence before art-complete milestones.
- Retro constraints can be a production strategy, not just a nostalgic art choice.

### Quality notes
- Source is practitioner/trade press. The lesson is useful as production guidance, not a universal rule.

## 2026-06-18 compile additions: Epic Lore version control and UE6 interoperability direction

### Source-backed claims
- Epic's Lore version control system is described as an open-source, centralized, content-addressed system optimized for projects that combine code with large binary assets, using Merkle trees, immutable revision chains, binary-first storage, deduplication, and sparse/on-demand hydration. Source: `raw/2026-06-18-web-80-lv-epic-games-presented-open-sourced-version-control-system.md`. confidence: 1 trade-press source quoting Epic positioning, last-confirmed 2026-06-18.
- Epic positions Lore against Git-plus-LFS and proprietary binary-asset systems by emphasizing first-class chunked storage, offline/sparse workflows, multi-tenant isolation, open specifications, and extensibility across C/C++, C#, Rust, Go, Python, and JavaScript. Source: `raw/2026-06-18-web-80-lv-epic-games-presented-open-sourced-version-control-system.md`. confidence: 1 source, last-confirmed 2026-06-18.
- Game Developer reports Epic's UE6 direction as merging UE5 and UEFN into a unified engine, shifting toward Verse, interoperable content/code/economies, AI pipeline features, first-class glTF/USD formats, and open specifications where standards do not exist; early access is described for late 2027. Source: `raw/2026-06-18-web-gamedeveloper-com-unreal-engine-6-will-merge-ue5-and-uefn-into-one-eng.md`. confidence: 1 trade-press source, last-confirmed 2026-06-18.

### Typed entities
- product: Epic Lore version control
- engine: Unreal Engine 6 / UE6
- tool/platform: Unreal Editor for Fortnite / UEFN
- language: Verse
- standard: glTF
- standard: USD
- concept: binary-first version control
- concept: smart asset interoperability
- concept: cross-game economy portability

### Explicit relationships
- Binary-first version control depends-on content-addressed chunk storage, deduplication, sparse hydration, and locking/replication workflows for large asset teams.
- Epic Lore complements or competes with Git LFS and proprietary game-asset version-control systems.
- UE6 interoperability depends-on Verse APIs, asset conventions, open formats, and ecosystem/economy rules, not only renderer/editor features.
- Fortnite integration may complement UE6 distribution for some projects while contradicting a fully platform-neutral strategy for others.

### HoneyDrunk implications
- Keep Epic Lore on the watchlist for future large-binary game/film repositories, but do not migrate without testing Windows workflows, locking, offline behavior, Git interop, hosting, backups, and editor integration.
- Treat UE6/Verse/UEFN convergence as strategic direction, not immediate production guidance. Any HoneyDrunk Unreal planning should preserve exit options until tooling, licensing, and interoperability details are concrete.

### Quality notes
- 80 Level and Game Developer are trade-press sources summarizing Epic announcements. Validate against Epic's primary docs before tool or engine commitments.

## 2026-06-20 compile additions: UE6 reaction signal

### Source-backed claims
- 80 Level's State of Unreal reaction roundup reinforces that Epic's UE6 direction is being interpreted as a production-ecosystem shift, not only an engine feature release: UE5/UEFN convergence, Verse, interoperable content, MCP/AI editor workflows, Epic Lore version control, faster iteration, lower cook times, and broader mobile/Fortnite-connected distribution are grouped as one strategic direction. Source: `raw/2026-06-20-web-80-level-state-of-unreal-ue6-reactions-hype-skepticism-and-what-it-mea.md`. confidence: 1 trade-press reaction roundup, last-confirmed 2026-06-20.
- The same roundup records skepticism around Blueprint/Actor deprecation, Verse/Scene Graph migration, accessibility for non-programmer creators, authorship expectations, and disruption to existing Unreal teams; Epic's roadmap language says early UE6 versions keep Actors and Blueprints while conversion tools mature, with early access targeted for late 2027. Source: `raw/2026-06-20-web-80-level-state-of-unreal-ue6-reactions-hype-skepticism-and-what-it-mea.md`. confidence: 1 source, last-confirmed 2026-06-20.

### Typed entities
- engine: Unreal Engine 6 / UE6
- platform: Unreal Editor for Fortnite / UEFN
- language/runtime: Verse
- framework: Scene Graph
- feature: Blueprints
- feature: Actors
- protocol/tooling: Model Context Protocol / MCP
- product/tool: Epic Lore version control
- concept: interoperable content
- concept: AI-assisted editor workflow

### Explicit relationships
- UE6 depends-on Verse, Scene Graph, interoperable content conventions, and UEFN convergence to become a unified creation ecosystem.
- Blueprint deprecation contradicts Unreal's existing accessibility story unless conversion tools, editor affordances, and training paths preserve creator productivity.
- MCP-powered editor workflows complement engine automation but increase the need for source-control, authorship, and production-policy decisions.

### HoneyDrunk implications
- Treat UE6 as a late-2027+ strategic watchlist item. Do not anchor current production plans on UE6-specific promises without primary Epic docs and migration tests.
- If HoneyDrunk evaluates Unreal for future work, include Verse readiness, Blueprint migration, Epic Lore/Git interop, AI tool policy, and non-programmer workflow impact in the spike criteria.

### Quality notes
- 80 Level is secondary/trade-press reaction coverage. Useful for sentiment and risk mapping, not sufficient for engine migration decisions.

## 2026-06-21 compile additions: Epic Lore primary repository reinforcement

### Source-backed claims
- The GitHub capture for `EpicGames/lore` reinforces the prior Epic Lore entry with a primary repository surface: Epic describes Lore as an open-source next-generation version-control system. Source: `raw/2026-06-21-web-epic-games-github-epicgames-lore-lore-is-a-next-generation-open-source.md`. confidence: 1 primary repository capture, last-confirmed 2026-06-21.

### Typed entities
- repository: `EpicGames/lore`
- product: Epic Lore version control
- platform: GitHub

### Explicit relationships
- The primary GitHub repository complements the earlier 80 Level/trade-press source for Epic Lore, but repository maturity, docs, releases, hosting, and client tooling still require direct inspection before adoption.

### HoneyDrunk implications
- If large-binary version control becomes relevant, inspect the Epic Lore repository directly rather than relying on trade-press summaries.

### Quality notes
- Primary repository capture is stronger than trade press for project existence, but adoption still needs local workflow testing.
