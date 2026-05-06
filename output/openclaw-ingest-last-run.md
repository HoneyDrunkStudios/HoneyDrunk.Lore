# OpenClaw Ingest Last Run

## Timestamp
2026-05-06 09:00 UTC / 2026-05-06 05:00 America/New_York

## Raw sources ingested
28 raw sources ingested:
- `raw/2026-05-06-clipper-discord-anthropic-claude-2.md`
- `raw/2026-05-06-clipper-discord-anthropic-claude.md`
- `raw/2026-05-06-clipper-discord-aspire-2.md`
- `raw/2026-05-06-clipper-discord-aspire.md`
- `raw/2026-05-06-clipper-discord-blender-community.md`
- `raw/2026-05-06-clipper-discord-google-gemini-2.md`
- `raw/2026-05-06-clipper-discord-google-gemini.md`
- `raw/2026-05-06-clipper-discord-hugging-face-2.md`
- `raw/2026-05-06-clipper-discord-hugging-face.md`
- `raw/2026-05-06-clipper-discord-microsoft-community-2.md`
- `raw/2026-05-06-clipper-discord-microsoft-community.md`
- `raw/2026-05-06-clipper-discord-microsoft-foundry-2.md`
- `raw/2026-05-06-clipper-discord-microsoft-foundry.md`
- `raw/2026-05-06-clipper-discord-net-c-2.md`
- `raw/2026-05-06-clipper-discord-net-c.md`
- `raw/2026-05-06-clipper-discord-official-unity.md`
- `raw/2026-05-06-clipper-discord-openai-developer-2.md`
- `raw/2026-05-06-clipper-discord-openai-developer.md`
- `raw/2026-05-06-clipper-x-list-snapshot-2.md`
- `raw/2026-05-06-clipper-x-list-snapshot.md`
- `raw/2026-05-06-podcast-acquired-the-nfl.md`
- `raw/2026-05-06-rss-dev-to-gamedev-legacy-flash-to-modern-html5-a-developer-s-migration-gu.md`
- `raw/2026-05-06-rss-dev-to-gamedev-when-a-digital-horse-runs-the-fairness-problem-behind-a.md`
- `raw/2026-05-06-rss-dev-to-unity-after-genie-3-38-alternatives-for-ai-scene-generation.md`
- `raw/2026-05-06-rss-dev-to-unity-benchmark-webxr-2-0-vs-unity-webgl-vs-unreal-engine-html5.md`
- `raw/2026-05-06-rss-godot-engine-dev-snapshot-godot-4-7-dev-4.md`
- `raw/2026-05-06-rss-martin-fowler-fragments-may-5.md`
- `raw/2026-05-06-rss-unity-blog-games-made-with-unity-march-2026-in-review.md`

## Wiki pages created/updated
- Updated `wiki/browser-snapshot-source-quality.md`
- Updated `wiki/godot-2026-mobile-and-4-7-cycle.md`
- Updated `wiki/gamedev-production-and-community-signals.md`
- Updated `wiki/ai-assisted-software-practice.md`
- Updated `wiki/unity-3d-and-realtime-vfx-patterns.md`
- Created `wiki/web-3d-runtime-tradeoffs.md`
- Created `wiki/creator-business-models.md`
- Updated `wiki/indexes/sources.md`
- Updated `wiki/indexes/topics.md`
- Updated `wiki/indexes/gaps.md`
- Updated `wiki/indexes/audit.md`

## Crystallization from `output/query-*.md`
- Reviewed `output/query-2026-05-05-daily-compiled-signal.md`; its durable facts were already represented in existing wiki pages, so no new crystallized `output/query-*` fact file was needed.

## Contradictions resolved / supersession
- No substantive contradictions required supersession.
- Godot 4.7 beta 1 remains the release-readiness superseding posture for earlier dev snapshots; dev 4 was preserved as feature-detail evidence.
- 2026-05-06 duplicate Discord/X captures reinforce the low-yield source-quality diagnosis rather than superseding prior claims.

## Gaps logged
- Discord announcement body extraction remains unresolved and was reinforced by 18 additional low-yield captures.
- X list post extraction remains unresolved and was reinforced by two additional low-yield captures.
- New idempotency gap: 2026-05-06 sourcing created duplicate `-2` captures for several monitored surfaces.
- New evaluation gaps: reproduce WebXR/Babylon.js vs Unity WebGL vs Unreal HTML5 benchmark on HoneyDrunk target devices; validate AI scene-generation tools for availability/licensing/cost/workflow fit.

## Privacy redactions / filtering
- Did not copy Discord user/chat bodies, unread-count specifics, account labels, or X account/UI profile details into wiki pages.
- Fowler fragment included a defamatory-AI-overview example; wiki retained only high-level AI-responsibility signal, not allegations as facts about the individual.
- No credentials, tokens, or secrets were found in source material written to wiki.

## Quality posture
- Decision-usable: Godot dev 4, Flash migration methodology, AI/Web3 trust-boundary pattern, AI-assisted software-practice additions, browser 3D runtime tradeoff framing.
- Scout-only / weak authority: DEV.to WebXR benchmark until reproduced; AI scene-generation alternatives list until validated; Unity release roundup as ecosystem breadth not engine-selection evidence; Acquired NFL metadata as strategic analogy not full transcript-backed operating model.
- Low-quality sources: 20 new browser clipper raw files were ingested only as source-quality/capture-coverage evidence.

## Blockers
- None blocking safe wiki commit. Existing worktree contains sourcing/raw/.obsidian changes outside this ingest pass; commit should include only safe Lore ingest additions/updates, preserving raw immutability.
