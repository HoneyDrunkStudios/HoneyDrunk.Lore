# Lore Sourcing - Last Run

Timestamp: 2026-09-24T17:33:40-04:00
Mode: write
Existing raw documents inspected: 1052
Known normalized source URLs at discovery: 1009
Candidates scanned: 636 feed/index entries
Skipped duplicates: 155 candidate URL occurrences
Saved public web/RSS items: 15
Saved Birdclaw items: 0
Birdclaw blocker reported: yes

## Birdclaw

Ran `python tools/lore_source_birdclaw_recent.py --limit 25 --max-pages 1` before public feed discovery. Live refresh failed: xurl was not installed and the configured bird command was unavailable; auth status also timed out. No local-cache conversion was allowed. See [Birdclaw status](lore-birdclaw-sourcing-last-run.md).

## Files written

- raw/2026-09-24-rss-huggingface-tokenizer-v1-benchmark-contracts.md
- raw/2026-09-24-rss-claude-task-cost-cache-and-retry-measurement.md
- raw/2026-09-24-rss-nuget-microsoft-signing-certificate-rotation.md
- raw/2026-09-24-rss-dotnet-meterlistener-observable-metric-semantics.md
- raw/2026-09-24-rss-azure-container-apps-express-ga-boundaries.md
- raw/2026-09-24-rss-azure-sandbox-egress-state-and-telemetry.md
- raw/2026-09-24-rss-github-actions-node24-runtime-cutover.md
- raw/2026-09-24-rss-ci-runtime-variance-and-flaky-test-cost.md
- raw/2026-09-24-rss-github-app-key-lifecycle-and-blast-radius.md
- raw/2026-09-24-rss-agent-local-history-and-credential-exposure.md
- raw/2026-09-24-rss-unity-content-directory-artifact-dependencies.md
- raw/2026-09-24-rss-sprite-animation-export-validation-gates.md
- raw/2026-09-24-rss-docker-kit-versioned-agent-permission-contracts.md
- raw/2026-09-24-rss-queue-worker-local-backpressure-tradeoffs.md
- raw/2026-09-24-rss-procedural-rust-material-structure-and-reuse.md

## Coverage and selection

- AI / LLM Research & Tooling: 2
- .NET Ecosystem: 2
- Azure & Cloud: 2
- DevOps & CI/CD: 2
- Security & Ethical Hacking: 2
- Game Development / Unity: 2
- Software Architecture: 2
- Technical Art & Creator Tools: 1

The 15-item cap takes precedence over sixteen distinct primary-category slots. Technical art has one primary item plus substantive secondary coverage in the sprite-animation and Unity content-pipeline captures, giving every major interest area at least two relevant items. Sources include Microsoft, GitHub, Docker, Hugging Face, Anthropic, Andrew Lock, GitGuardian, Gen Digital, Canva, Unity, Platform Engineering, FrameSprite, and a material-artist interview at 80 Level.

Applied actionability, durability, scope, and depth in that order. Priority .NET/Azure/GitHub/TLDR feeds were scanned alongside the other playbook sources. TLDR discoveries were fetched from original written articles; publication dates come from the articles rather than newsletter issue dates. Fourteen captures were published in September 2026. The February MeterListener article is an explicit evergreen backfill: its aggregation semantics and production caveats are useful beyond a release cycle.

Fetched readable bodies before saving. All fifteen captures are substantive attributed summaries with original source links, not full-text reproductions. License permission for wholesale republication was not established. Azure pages were recovered from public server-delivered Next.js article data. No browser, audio/video metadata sourcing, wiki compilation, repository-tool edits, commits, or pushes were performed.

Quality exclusions: omitted event promotions, media-only posts, shallow news, and stale newsletter roundups. The Ably streaming comparison was rejected after reading because its SSE per-chunk header claim is unreliable and its conclusion is overly categorical. The indie release-pipeline candidate was not selected because its claim that a version-code reset permanently prevents future updates is unreliable. The Docker article page/RSS author discrepancy is recorded in its capture.

## Failed sources

- Polycount (https://polycount.com/discussions/feed.rss): HTTP Error 403: Forbidden
- Scott Brady (https://www.scottbrady91.com/feed): HTTP Error 404: Not Found

Recovered extraction failures: three Azure Community Hub pages initially produced short bodies; reading their public article-data payload recovered them. Two were selected; the third was not needed within the cap. A console encoding error occurred after discovery data had been saved; UTF-8 reads recovered the full results without repeating the harvest.

## Validation

- All 15 files parse as YAML and include the seven required fields, valid dates, substantive bodies, source attribution, and correctly formatted filenames.
- Original, resolved, and canonical URLs were checked against raw frontmatter and the source index immediately before writes; Community Hub article-ID aliases were also normalized.
- SHA-256 checks confirm all 1052 pre-existing raw files are unchanged. Exactly 15 raw files were added.
- Existing unrelated working-tree changes were preserved.
- External wiki changes observed (this sourcing script made no wiki writes): wiki\indexes\audit.md, wiki\indexes\gaps.md, wiki\indexes\sources.md, wiki\indexes\topics.md
