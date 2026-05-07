# Gamedev Production and Community Signals

## Decision-useful summary
The game-development community feed produced a mix of process advice, tooling experiments, migration methodology, Web3 fairness architecture, job-market signal, AI-assisted production case studies, and novelty projects. Durable points: structured phased production reduces drift; Flash-to-HTML5 migrations should reverse-engineer behavior and rewrite cleanly rather than port decompiled ActionScript; dynamic blockchain games need explicit trust boundaries; small cross-platform libraries and AI-assisted experiments are discovery signals, not adoption proof. [sources: raw/2026-05-04-rss-dev-to-unity-our-4-phase-game-development-process-from-concept-to-laun.md; raw/2026-05-06-rss-dev-to-gamedev-legacy-flash-to-modern-html5-a-developer-s-migration-gu.md; raw/2026-05-06-rss-dev-to-gamedev-when-a-digital-horse-runs-the-fairness-problem-behind-a.md; raw/2026-05-05-rss-dev-to-gamedev-first-release-of-ldl-0-1-a-small-library-with-a-big-sou.md; raw/2026-05-05-rss-dev-to-gamedev-i-built-a-minecraft-mod-where-every-sword-is-an-aws-ser.md; raw/2026-05-04-rss-tech-artists-org-lighting-td-atlantis-animation-santa-cruz-de-tenerife.md; raw/2026-05-07-rss-dev-to-gamedev-how-i-knowing-only-if-vibecoded-civicsurvival-a-158k-li.md]

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

## HoneyDrunk implications
- For internal game prototypes, start with a lightweight phase gate: concept, prototype, production, launch/learn.
- If reviving legacy interactive content, specify behavior first and rewrite cleanly; do not treat recovered/decompiled code as architectural truth.
- For any AI+blockchain/game experiment, write the trust-boundary contract before the economy: what is recorded, replayable, independently checkable, and operator-dependent.
- Novel AI/game demos are good marketing and learning artifacts; do not mistake them for product-market validation.
- Track technical-art talent and reusable shader/VFX resources if Lore/Grid visual production ramps up.
- Treat AI-assisted gamedev case studies as process patterns; validate with HoneyDrunk-specific builds and playtests before adopting wholesale.

## Confidence and quality notes
- Quality posture: mixed; process/migration/trust-boundary claims are decision-useful, Web3 article is architectural opinion, newsletter aggregation is low-authority.
- Weak claims: AWS Minecraft mod and LDL need repo/docs inspection before technical adoption; Polkadot/Substrate claim is source-author interest, not an independent recommendation.
- Privacy filter: no private person details copied beyond public author/org/role names.
