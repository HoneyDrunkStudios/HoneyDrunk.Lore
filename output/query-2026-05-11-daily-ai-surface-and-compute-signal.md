# Query: 2026-05-11 Daily AI Surface and Compute Signal

## Question
What durable decision-useful facts emerged from the May 11, 2026 Lore ingest batch?

## Answer
- Hybrid mobile/app experiences can keep normal product flows outside the game engine: Coach Ivy uses Flutter for onboarding, food logging, subscriptions, analytics, navigation, and app state, while embedded Unity owns the reactive 3D avatar layer. See [[unity-3d-and-realtime-vfx-patterns]] and [[gamedev-production-and-community-signals]].
- Unity AI/game-art/GPU-particle links in Game Dev Digest #330 are useful discovery queues, but the newsletter itself is not primary evidence. Follow linked sources before adopting tooling.
- Microsoft is pushing developers toward reusable MCP/OpenAI app samples with widgets, previews, and docs; HoneyDrunk should inspect samples before custom MCP app/UI work. See [[microsoft-dotnet-ai-stack]] and [[ai-agent-harnesses]].
- Claude/Anthropic compute capacity is now part of infrastructure risk: a Rundown article reinforces the SpaceX/xAI Colossus compute dependency and the broader scarcity of frontier AI compute. See [[claude-platform-2026]] and [[edge-ai-and-ai-infrastructure-2026]].
- OpenAI/Jony Ive/io AI hardware remains early analyst/newsletter signal only. Track it as a possible future agent surface, not an implementation target. See [[ai-hardware-and-companion-devices-2026]].
- TLDR InfoSec RSS extraction is still broken/low-yield for title-level news: the 2026-05-11 body was sponsor copy, not the Daemon Tools/robot mower/OpenEMR items. See [[browser-snapshot-source-quality]].

## Decision implications
- For character-led mobile prototypes, prefer a bounded engine scene embedded in the app shell unless the whole product is game-native.
- Before building MCP app/client UI from scratch, audit Microsoft/open-source samples for conventions, auth, manifests, widgets, and cross-client behavior.
- Keep provider-routing abstractions where possible; compute supply shocks may affect model availability/limits/pricing.
- Do not treat OpenAI hardware rumors as specs; wait for primary docs/privacy/developer surface.
- Fix newsletter extraction before using TLDR title-level items as evidence.

## Citations
- raw/2026-05-11-rss-dev-to-unity-building-coach-ivy-embedding-a-unity-avatar-inside-a-flut.md
- raw/2026-05-11-rss-dev-to-unity-game-dev-digest-issue-330-unity-ai-game-art-and-more.md
- raw/2026-05-11-rss-tldr-infosec-daemon-tools-backdoored-robot-mower-hijacked-38-openemr-c.md
- raw/2026-05-11-web-the-rundown-ai-anthropic-spacex-ai-become-unlikely-compute-partners.md
- raw/2026-05-11-web-the-rundown-ai-openai-s-ai-phone-just-jumped-the-line.md
- raw/2026-05-11-youtube-microsoft-developer-youtube-don-t-build-mcp-apps-from-scratch-use-this.md

## Confidence
Medium for Coach Ivy architecture and Microsoft sample availability as source-reported facts; medium-low for Anthropic/SpaceX compute framing because it is newsletter-sourced but consistent with prior Anthropic compute-limit context; low for OpenAI hardware timing/speculation; low for TLDR title-level security claims because the captured body did not contain them.

## Gaps
See `wiki/indexes/gaps.md` for TLDR extraction, OpenAI hardware developer surface, and MCP app sample standardization gaps.
