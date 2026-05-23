# Daily agent/security/platform signal — 2026-05-23

## Decision-useful facts

- Agent platforms are separating model orchestration from execution infrastructure: Claude Managed Agents can run the brain on Anthropic while Cloudflare Sandboxes provide the hands, proxies, private connectivity, browser recording, logs, and custom tools. confidence: 1 source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-devops-announcing-claude-managed-agents-on-cloudflare-8-minute-re.md; wiki: [[claude-platform-2026]]]
- Self-extending CLIs are now a concrete vendor pattern: AWS Strands/Bedrock/MCP can generate and load new CLI commands at runtime, but generated-command execution needs quarantine, review, sandboxing, and scoped credentials. confidence: 1 source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-devops-building-self-extending-cli-tools-with-strands-agent-9-min.md; wiki: [[ai-agent-harnesses]]]
- Coding-agent supply-chain risk is moving into CI/CD: GitHub Actions cache poisoning, unsafe `pull_request_target`, mutable action tags, release-workflow caches, and broad publish tokens are audit priorities. confidence: 1 practitioner source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-infosec-github-actions-cache-poisoning-is-eating-open-source-18-m.md; wiki: [[ai-coding-agent-security]]]
- Fowler's narrow definition of vibe coding confirms the HoneyDrunk rule: okay for throwaway prototypes; not okay for anything with secrets/users/revenue/production unless it becomes reviewed agentic programming with gates. confidence: 1 source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-martin-fowler-bliki-vibe-coding.md; wiki: [[ai-assisted-software-practice]]]
- Gemini 3.5 Flash should enter the local benchmark shortlist for fast agent/coding/multimodal work, but Google benchmark claims are vendor-authored; Qwen3.7 could not be evaluated from the captured raw. confidence: 1 vendor source plus 1 low-yield capture, last-confirmed 2026-05-23. [sources: raw/2026-05-22-rss-tldr-ai-gemini-3-5-flash-5-minute-read.md; raw/2026-05-23-rss-tldr-ai-qwen3-7-the-agent-frontier-15-minute-read.md; wiki: [[google-agent-platform-and-gemini-api-2026]]]

## Gaps to resolve

- Audit HoneyDrunk GitHub Actions for cache poisoning and release-token risks.
- Decide whether a self-extending CLI is worth prototyping, and define generated-command trust levels first.
- Benchmark Gemini 3.5 Flash/Claude/OpenAI/Qwen on representative HoneyDrunk tasks before route changes.
- Improve Qwen.ai and CNBC extraction; current captures are too scaffold-heavy for detailed model/business claims.

## Privacy and quality posture

No secrets copied. Security incident details were summarized at control/checklist level rather than reproducing payload mechanics. Vendor benchmarks and secondary reports were marked as needing validation.
