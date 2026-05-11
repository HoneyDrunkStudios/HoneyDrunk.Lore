# OpenClaw Lore Ingest Last Run

## Run
- Timestamp: 2026-05-11 09:00 UTC
- Runtime: OpenClaw / Honeyclaw
- Operation: daily ingest/compile pass

## Raw sources ingested
- raw/2026-05-11-rss-dev-to-unity-building-coach-ivy-embedding-a-unity-avatar-inside-a-flut.md
- raw/2026-05-11-rss-dev-to-unity-game-dev-digest-issue-330-unity-ai-game-art-and-more.md
- raw/2026-05-11-rss-tldr-infosec-daemon-tools-backdoored-robot-mower-hijacked-38-openemr-c.md
- raw/2026-05-11-web-the-rundown-ai-anthropic-spacex-ai-become-unlikely-compute-partners.md
- raw/2026-05-11-web-the-rundown-ai-openai-s-ai-phone-just-jumped-the-line.md
- raw/2026-05-11-youtube-microsoft-developer-youtube-don-t-build-mcp-apps-from-scratch-use-this.md

## Wiki pages changed
- Created: wiki/ai-hardware-and-companion-devices-2026.md
- Updated: wiki/unity-3d-and-realtime-vfx-patterns.md
- Updated: wiki/gamedev-production-and-community-signals.md
- Updated: wiki/microsoft-dotnet-ai-stack.md
- Updated: wiki/ai-agent-harnesses.md
- Updated: wiki/claude-platform-2026.md
- Updated: wiki/edge-ai-and-ai-infrastructure-2026.md
- Updated: wiki/browser-snapshot-source-quality.md
- Updated indexes: wiki/indexes/sources.md, wiki/indexes/topics.md, wiki/indexes/gaps.md, wiki/indexes/audit.md

## Durable query crystallized
- output/query-2026-05-11-daily-ai-surface-and-compute-signal.md

## Supersession / contradictions
- TLDR InfoSec title-level claims were not treated as evidence because the captured body contained sponsor copy only; this reinforces and extends the existing TLDR RSS extraction-quality gap.
- Rundown web captures were treated as article-level evidence only after readable extraction; public client configuration/site scaffolding from raw captures was not propagated.
- OpenAI AI hardware claims are marked early/low-confidence and do not supersede any primary product documentation.

## Privacy filtering
- Did not copy raw Rundown embedded app globals, public telemetry/client configuration strings, or site JavaScript into wiki pages.
- No private user/chat data copied.

## Quality posture
- Decision-usable for scouting and architecture awareness.
- Coach Ivy is a self-reported case study; useful as a pattern, not benchmark evidence.
- Game Dev Digest is an aggregator; linked primary sources should be inspected before adoption.
- Anthropic/SpaceX compute and OpenAI hardware items are newsletter/analyst-sourced and should be confirmed with primary sources before major decisions.

## Gaps added
- TLDR InfoSec item extraction without sponsor-copy substitution.
- OpenAI/Jony Ive/io AI hardware developer/runtime/privacy surface.
- HoneyDrunk MCP app sample standardization before custom MCP UI/app work.

## Commit / push
- Safe to commit by staging only the 2026-05-11 raw sources and this run's wiki/output/index files; unrelated pre-existing workspace changes intentionally left unstaged.
