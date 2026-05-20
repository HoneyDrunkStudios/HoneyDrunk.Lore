# OpenClaw Lore ingest last run

- timestamp: 2026-05-20 09:00 UTC / 2026-05-20 05:00 America/New_York
- operator/runtime: Honeyclaw / OpenClaw scheduled ingest

## Raw sources ingested: 8
- raw/2026-05-20-rss-azure-blog-eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-.md
- raw/2026-05-20-rss-dev-to-unity-unity-vs-godot-vs-unreal-for-mobile-games-a-practical-com.md
- raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md
- raw/2026-05-20-rss-opentelemetry-blog-applying-opentelemetry-security-practices-in-legacy.md
- raw/2026-05-20-rss-tldr-ai-qwen-3-7-cursor-composer-2-5-anthropic-acquires-stainless.md
- raw/2026-05-20-rss-tldr-infosec-1-8m-nyc-patients-hit-pixel-10-0-click-exploit-ledger-mai.md
- raw/2026-05-20-web-the-rundown-ai-musk-s-openai-case-runs-out-of-time.md
- raw/2026-05-20-youtube-microsoft-developer-youtube-using-cowork-i-automated-my-prompt-of-the-.md

## Wiki pages created
- wiki/ai-coding-agent-security.md

## Wiki pages updated
- wiki/edge-ai-and-ai-infrastructure-2026.md
- wiki/unity-3d-and-realtime-vfx-patterns.md
- wiki/godot-2026-mobile-and-4-7-cycle.md
- wiki/opentelemetry-genai-observability-and-ecosystem.md
- wiki/ai-agent-harnesses.md
- wiki/claude-platform-2026.md
- wiki/browser-snapshot-source-quality.md
- wiki/indexes/sources.md
- wiki/indexes/topics.md
- wiki/indexes/gaps.md
- wiki/indexes/audit.md
- output/query-2026-05-20-daily-agent-security-mobile-otel-infra-signal.md

## Contradictions resolved / supersession
- No direct claim contradictions required supersession.
- TLDR 2026-05-19 title-level AI/InfoSec claims were explicitly not promoted because raw bodies contained sponsor copy; this reinforces the existing extraction-quality diagnosis.
- Rundown AI 2026-05-19 body claims were not promoted because inspected raw lacked decision-grade article body facts and included public app configuration/site scaffolding.

## Gaps logged
- Agent sandbox/microVM evaluation for OpenClaw/Grid.
- Azure Blob + Run:AI model streaming benchmark only if a real Azure open-weight workload exists.
- TLDR and Rundown extraction failures for 2026-05-19 captures.
- Operational-data classification beyond ordinary PII for OTel/legacy telemetry.
- Local mobile-engine spike for Unity/Godot/Unreal target-device behavior.

## Privacy filtering
- Did not copy Rundown AI public client config, Sentry/Stripe/VAPID-like public keys, CSS, or app scaffolding into wiki facts.
- Docker incident examples were summarized at the security-control level; no secrets, exploit payloads, or unsafe operational details were promoted.

## Quality posture
- Decision-usable additions: OTel legacy security guidance; coding-agent risk taxonomy and guardrail checklist; Azure model-streaming concept; mobile engine selection criteria.
- Weak/vendor-biased claims: Docker Sandboxes mitigation claims and Azure performance numbers are vendor-authored; Ocean View Games source is explicitly Unity-specialist and biased toward Unity.
- Low-yield sources: TLDR AI/InfoSec and Rundown AI captures were recorded as source-quality evidence only.

## Blockers
- None for this compile pass.
