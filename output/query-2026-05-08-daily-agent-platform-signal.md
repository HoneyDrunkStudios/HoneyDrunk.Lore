# Query: 2026-05-08 Daily Agent Platform Signal

## Question
What durable decision-useful facts emerged from the May 8, 2026 Lore ingest batch?

## Answer
- Claude Opus 4.7 is the current Anthropic Opus upgrade target for hard coding, long-running agent work, finance/document tasks, and high-resolution vision, but prompts/harnesses need re-testing because instruction literalness and token/effort behavior changed. See [[claude-platform-2026]].
- Anthropic is packaging Claude into enterprise workflows: finance agent templates, Microsoft 365 add-ins, creative-tool connectors, Managed Agents, and partner delivery capacity. See [[claude-platform-2026]].
- Google's agent platform signal is production plumbing: Agents CLI, Gemini webhooks, Gemini Embedding 2, ADK structured-output/subagent patterns, and OpenTelemetry/circuit-breaker practices. See [[google-agent-platform-and-gemini-api-2026]] and [[ai-agent-harnesses]].
- Generative UI is moving toward catalog/schema protocols rather than raw UI generation; A2UI v0.9 is the clearest new reference. See [[generative-ui-and-a2ui]].
- Edge and infrastructure sources split into two useful tracks: LiteRT/NPU for on-device features, and Rapid Bucket/MaxText for cloud training/post-training bottlenecks. See [[edge-ai-and-ai-infrastructure-2026]].

## Decision implications
- Benchmark Opus 4.7 on HoneyDrunk's actual hard tasks before changing defaults.
- Design long-running Grid/Lore jobs around push completion semantics where possible.
- For any agent-driven UI, start with an internal component catalog/schema; map outward to A2UI/AG-UI only when needed.
- Treat multimodal embeddings and on-device AI as validation projects, not procurement decisions, until tested on HoneyDrunk data/devices.

## Citations
- raw/2026-05-07-web-anthropic-news-introducing-claude-opus-4-7.md
- raw/2026-05-07-web-anthropic-news-agents-for-financial-services.md
- raw/2026-05-07-web-anthropic-news-claude-for-creative-work.md
- raw/2026-05-08-rss-google-developers-blog-agents-cli-in-agent-platform-create-to-producti.md
- raw/2026-05-08-rss-google-ai-blog-reduce-friction-and-latency-for-long-running-jobs-with-.md
- raw/2026-05-08-rss-google-developers-blog-building-with-gemini-embedding-2-agentic-multim.md
- raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md
- raw/2026-05-07-rss-google-developers-blog-building-real-world-on-device-ai-with-litert-an.md

## Confidence
Medium. Source facts are public vendor announcements/blog posts; architecture direction is decision-useful, but benchmarks/customer quotes should be locally validated.

## Gaps
See `wiki/indexes/gaps.md` for Opus 4.7 benchmarking, generative UI schema, multimodal embedding evaluation, and webhook/push-job candidates.
