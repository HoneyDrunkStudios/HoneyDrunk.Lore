# Claude Platform 2026

## Decision-useful summary
Anthropic's 2026 platform direction is enterprise/workflow-heavy: Claude Opus 4.7 improves long-running software, finance, document, multimodal, and agent workflows; Claude is being packaged into finance agents, Microsoft 365 add-ins, creative-tool connectors, managed agents, and partner delivery channels. Anthropic is also positioning Claude as an ad-free thinking/work surface and scaling compute aggressively to raise Code/API limits. A later Rundown article reframed the SpaceX/xAI compute deal as evidence that scarce frontier compute can turn model rivals into infrastructure customers/suppliers. [sources: raw/2026-05-07-web-anthropic-news-introducing-claude-opus-4-7.md; raw/2026-05-07-web-anthropic-news-agents-for-financial-services.md; raw/2026-05-07-web-anthropic-news-claude-for-creative-work.md; raw/2026-05-07-web-anthropic-news-claude-is-a-space-to-think-anthropic.md; raw/2026-05-07-web-anthropic-news-higher-usage-limits-for-claude-and-a-compute-deal-with-.md; raw/2026-05-11-web-the-rundown-ai-anthropic-spacex-ai-become-unlikely-compute-partners.md]

## Claims
- Claude Opus 4.7 is a direct upgrade to Opus 4.6 with reported gains in advanced software engineering, long-running task reliability, instruction following, high-resolution vision, document/finance work, and professional creative output. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-introducing-claude-opus-4-7.md]
- Opus 4.7 pricing is stated as unchanged from Opus 4.6 at $5/M input tokens and $25/M output tokens, with availability through Claude products/API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-introducing-claude-opus-4-7.md]
- Opus 4.7 introduces `xhigh` effort, task budgets in API public beta, higher-resolution image support, Claude Code `/ultrareview`, and broader auto-mode availability; migration may increase token counts because of tokenizer and higher-effort behavior, so real traffic should be measured. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-introducing-claude-opus-4-7.md]
- Anthropic released ten finance agent templates packaged as Claude Cowork/Claude Code plugins and Claude Managed Agents cookbooks; the templates combine skills, connectors, and subagents for research, modeling, close, audit, valuation, and KYC workflows. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-agents-for-financial-services.md]
- Claude's finance workflow integrations include Excel, PowerPoint, Word, Outlook add-ins, governed connectors to market/research/internal systems, and MCP apps such as Moody's; users remain expected to review/approve work before external action. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-agents-for-financial-services.md]
- Anthropic's creative-tool strategy uses connectors/MCP to let Claude operate beside Ableton, Adobe, Affinity, Autodesk Fusion, Blender, Resolume, SketchUp, Splice, and Canva/Claude Design workflows; the Blender connector is framed as MCP-based and accessible to other LLMs. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-claude-for-creative-work.md]
- Anthropic states Claude will remain ad-free because advertising incentives conflict with the goal of a trusted assistant for deep thinking/work; it prefers subscriptions/enterprise revenue and user-initiated commerce/integrations. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-claude-is-a-space-to-think-anthropic.md]
- Anthropic announced higher Claude Code/API limits tied to new compute capacity, including a SpaceX Colossus 1 deal described as over 300 MW and over 220,000 NVIDIA GPUs, plus other Amazon/Google/Broadcom/Microsoft/NVIDIA/Fluidstack capacity plans. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-higher-usage-limits-for-claude-and-a-compute-deal-with-.md]
- Anthropic is expanding delivery capacity through a new AI services company with Blackstone, Hellman & Friedman, and Goldman Sachs for mid-sized companies, plus continued Claude Partner Network systems-integrator partnerships. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-building-a-new-enterprise-ai-services-company-with-blac.md]
- Anthropic opened a Sydney office and appointed Theo Hourmouzis as GM for Australia/New Zealand, with regional enterprise, government, Canva/Xero, YMCA SA, and research partnership signals. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-web-anthropic-news-anthropic-sydney-office.md]
- The Rundown reports that Anthropic is renting compute from SpaceX/xAI's Colossus 1 cluster, reinforcing that compute scarcity can create pragmatic infrastructure partnerships between otherwise competing AI labs. confidence: 1 newsletter source plus earlier Anthropic announcement context, last-confirmed 2026-05-11. [source: raw/2026-05-11-web-the-rundown-ai-anthropic-spacex-ai-become-unlikely-compute-partners.md]

## Typed entities
- company: Anthropic
- model: Claude Opus 4.7
- model: Claude Opus 4.6
- product: Claude Code
- product: Claude Cowork
- product: Claude Managed Agents
- feature: `xhigh` effort
- feature: task budgets
- feature: `/ultrareview`
- concept: ad-free AI assistant
- concept: finance agent templates
- concept: creative-tool connectors
- protocol: Model Context Protocol (MCP)
- partner/company: SpaceX
- company/platform: xAI
- infrastructure/cluster: Colossus 1
- partner/company: Blackstone
- partner/company: Hellman & Friedman
- partner/company: Goldman Sachs
- person: Theo Hourmouzis
- region: Australia/New Zealand

## Explicit relationships
- Claude Opus 4.7 supersedes Claude Opus 4.6 for Anthropic's default frontier Opus workflows, while migration depends-on token/effort measurement.
- Claude finance templates use skills, connectors, and subagents to package domain workflows.
- Claude Managed Agents depend-on long-running sessions, per-tool permissions, managed credential vaults, and audit logs for regulated workflows.
- Claude creative connectors use MCP/connectors to bridge Claude with existing creative tools and design systems.
- Anthropic's ad-free positioning contradicts ad-supported AI assistant monetization for private work conversations.
- Higher Claude usage limits depend-on expanded compute partnerships.
- Anthropic's Claude capacity depends-on third-party hyperscale and AI-cluster supply, including SpaceX/xAI Colossus capacity per newsletter reporting.

## HoneyDrunk implications
- Opus 4.7 is worth testing for hard code review, long-running repo work, multimodal inspection, and finance/document tasks, but token/effort defaults need measured budget impact before broad routing.
- Watch Claude capacity/limit changes as infrastructure risk, not just model-roadmap news; compute partnerships may affect availability, pricing, and routing options.
- Claude's connector strategy validates HoneyDrunk's MCP-first integration posture: useful agents are increasingly expected to work inside existing tools, not replace them.
- For creative workflows, Blender/Adobe/Affinity/Fusion/SketchUp connectors are directly relevant to technical-art and prototype pipelines.
- Anthropic's ad-free stance is a useful product principle for HoneyDrunk agent UX: avoid hidden incentives inside trusted work surfaces.

## Confidence and quality notes
- Quality posture: decision-usable but vendor-authored; treat customer benchmark quotes as directional, not independently audited.
- Supersession: Opus 4.7 supersedes Opus 4.6 for Anthropic's own model recommendation, but existing Opus 4.6 prompts/harnesses should be re-tested rather than blindly migrated.
- Privacy filter: no secrets or private data copied; public customer/person names retained only where decision-useful.
