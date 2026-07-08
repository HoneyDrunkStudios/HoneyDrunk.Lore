# Lore Ingest - Last Run

Timestamp: 2026-07-08T10:09:17.4901151-04:00

## Raw sources ingested

Count: 15

- raw/2026-07-08-rss-80-level-new-copernicus-node-for-testing-uv-layouts-on-3d-models.md
- raw/2026-07-08-rss-dev-to-unity-choosing-a-genre-specific-optimization-strategy-for-unity.md
- raw/2026-07-08-rss-martin-fowler-experiences-with-local-models-for-coding.md
- raw/2026-07-08-rss-martin-fowler-viability-of-local-models-for-coding.md
- raw/2026-07-08-rss-polycount-ground-and-buildings-pipeline-workflow-approaches.md
- raw/2026-07-08-rss-polycount-how-to-create-a-realistic-landscape.md
- raw/2026-07-08-rss-tldr-ai-a-global-workspace-in-language-models-26-minute-read.md
- raw/2026-07-08-rss-tldr-ai-bringing-pytorch-monarch-to-amd-gpus-single-controller-distrib.md
- raw/2026-07-08-rss-tldr-ai-closing-the-verification-loop-14-minute-read.md
- raw/2026-07-08-rss-tldr-ai-hy3-1-minute-read.md
- raw/2026-07-08-rss-tldr-ai-jamesob-s-guide-to-running-sota-llms-locally-12-minute-read.md
- raw/2026-07-08-rss-tldr-devops-claude-video-github-repo.md
- raw/2026-07-08-rss-tldr-devops-cube-sandbox-github-repo.md
- raw/2026-07-08-rss-tldr-infosec-claude-mythos-and-saas-security-what-you-need-to-know-8-m.md
- raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md

## Wiki pages created/updated

Created:
- wiki/ai-agent-identity-and-workload-auth.md

Updated:
- wiki/ai-assisted-software-practice.md
- wiki/ai-agent-harnesses.md
- wiki/agent-evaluation-and-benchmarks.md
- wiki/ai-coding-agent-security.md
- wiki/edge-ai-and-ai-infrastructure-2026.md
- wiki/claude-platform-2026.md
- wiki/unity-3d-and-realtime-vfx-patterns.md
- wiki/technical-art-community-and-talent-signals.md
- wiki/mcp-tool-governance-and-app-surfaces.md
- wiki/llm-wiki-and-knowledge-formats.md
- wiki/indexes/sources.md
- wiki/indexes/topics.md
- wiki/indexes/gaps.md

## Contradictions resolved

- No direct contradictions required supersession.
- Fable/Mythos availability volatility remains captured in existing Claude Platform supersession notes; the Reco SaaS source was treated as vendor/practice framing and did not supersede Anthropic primary access/status claims.

## Gaps logged

Count: 8

- Local coding model benchmark requirements.
- Browser-backed dogfood report criteria for product PR readiness.
- Agent identity model selection and static-key replacement.
- SaaS/NHI exposure path inventory.
- CubeSandbox/Docker SBX/E2B sandbox evaluation criteria.
- Third-party video skill policy.
- Genre-specific Unity profiling fixtures.
- Environment-art workflow spike criteria.

## Crystallization from output/query-*.md

- No new `output/query-*.md` files were present beyond previously ingested historical query outputs.
- Existing `output/signal-review-2026-07-05.md`, `output/signal-review-2026-07-06.md`, and `output/signal-review-2026-07-07.md` were reviewed as daily blast artifacts but not crystallized separately because their durable source facts were already represented by the cited raw sources/pages.

## Blockers

- The Thinkroom "Closing the Verification Loop" raw capture is incomplete/truncated after the fix-loop section and contains large Excalidraw JSON. Only captured prose claims were promoted, with explicit capture caveats.
- Fresh X/Birdclaw sourcing still reports live sync unavailable, so no X/social material was included in this ingest pass.

## Quality posture

- Pages rewritten/flagged: no full rewrites; append-only compile sections were added to established pages plus one new identity page.
- Weak claims: project README claims for CubeSandbox and `claude-video`, practitioner local-model experiences, Polycount forum advice, vendor SaaS-security framing, and hardware/model-watch claims all retain validation caveats.
- Privacy redactions: no secrets, tokens, private PII, exploit payloads, phishing domains, or credential values were copied into wiki pages. Public API key environment variable names from README documentation were retained as config surface names only.
- Decision-usefulness: high for agent identity vocabulary, local-model eval design, verification-loop evidence, sandbox/skill security review, Unity profiling setup, and technical-art spike planning; low-authority community/vendor claims were kept as scouting signals.

## Validation

- Markdown/index consistency reviewed manually during compile.
- `python -m py_compile tools/lore_source_public.py` passed.
- `git diff --cached --check -- . ':!raw/**'` passed for non-raw staged content.
- `git diff --cached --check -- raw` reported trailing whitespace in newly captured raw source files; raw evidence was left unmodified under the repo's immutable-raw contract. The sourcing tool was updated to trim body-line trailing whitespace on future captures.
- All 15 `raw/2026-07-08-*.md` sources are represented in `wiki/indexes/sources.md`.
