# Query: 2026-05-09 Daily Agent Automation Signal

## Question
What durable decision-useful facts emerged from the May 9, 2026 Lore ingest batch?

## Answer
- Azure Developer CLI is becoming more agent-operable: April 2026 releases added multi-language hooks, standardized `--no-prompt`/`--non-interactive` failure behavior, `AZD_NON_INTERACTIVE`, AI model quota preflight, custom provisioning providers, and security fixes. See [[azure-agent-automation-and-identity]].
- Least-privilege agent authorization should be handled by short-lived delegated tokens, API-side filtering, gateways, and audit logs rather than by trusting the model or prompt. See [[azure-agent-automation-and-identity]] and [[ai-agent-harnesses]].
- Microsoft Agent Framework now has a decision-usable durable workflow story: typed executors, graph orchestration, Durable Task checkpointing/restart survival, Azure Functions HTTP hosting, human-in-the-loop waits, and optional MCP tool exposure. See [[microsoft-dotnet-ai-stack]].
- Two TLDR AI RSS captures were low-yield: the bodies contained sponsor/ad copy instead of the newsletter news items named by their titles. See [[browser-snapshot-source-quality]].

## Decision implications
- Audit HoneyDrunk `azd` workflows before letting agents run them: every path should be non-interactive, environment-scoped, logged, and fail structurally when input is missing.
- For Grid/Lore/customer-data agents, design token claims and API filters first; prompt-level policy is not enough.
- Candidate long-running or human-gated workflows should be evaluated against MAF durable workflows/Azure Functions hosting instead of bespoke background loops.
- Fix newsletter/RSS extraction before treating TLDR title-level captures as evidence for model/platform announcements.

## Citations
- raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md
- raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md
- raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md
- raw/2026-05-09-rss-net-blog-microsoft-agent-framework-building-blocks-for-ai-part-3.md
- raw/2026-05-09-rss-tldr-ai-claude-self-improving-agents-anthropic-spacex-deal-programbenc.md
- raw/2026-05-09-rss-tldr-ai-gpt-5-5-instant-subq-12m-context-gemini-flash-upgrades.md

## Confidence
Medium-high for Microsoft/Azure product facts; medium for architecture implications because sources are vendor-authored and need local validation. Low for TLDR title-level news claims because the captured body did not include the underlying newsletter items.

## Gaps
See `wiki/indexes/gaps.md` for `azd` non-interactive audit, delegated-token design, durable workflow candidates, and TLDR/RSS extraction quality.
