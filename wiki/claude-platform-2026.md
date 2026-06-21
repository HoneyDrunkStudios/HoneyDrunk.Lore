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

## 2026-05-20 compile additions

### Claims
- Docker's security writeup cites Claude Code and Claude Cowork among agent tools involved in public filesystem/permission-boundary incidents; treat the incidents as security-design signals rather than vendor-specific proof until primary sources are checked. confidence: 1 vendor roundup source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md; page: [[ai-coding-agent-security]]]
- Microsoft Developer's Cowork video metadata positions Cowork skills as automations for repeatable manual workflows, such as converting a GitHub contribution link into a formatted PowerPoint slide. confidence: 1 YouTube metadata source, last-confirmed 2026-05-20. [source: raw/2026-05-20-youtube-microsoft-developer-youtube-using-cowork-i-automated-my-prompt-of-the-.md]

### Typed entities
- product: Claude Cowork
- product: Claude Code
- product: Microsoft Cowork
- concept: agent skill automation

### Explicit relationships
- Claude/Cowork-style agent products depend-on filesystem and tool permission boundaries when operating beyond chat.
- Cowork skills complement agent harnesses by packaging repeatable workflow automation.

## 2026-05-23 compile additions

### Claims
- Cloudflare and Anthropic integrated Claude Managed Agents with Cloudflare Sandboxes, allowing the Claude agent loop to run on Anthropic while code execution, browser sessions, private-service connectivity, proxies, custom tools, logs, and sandbox control run on Cloudflare. confidence: 1 vendor integration source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-devops-announcing-claude-managed-agents-on-cloudflare-8-minute-re.md]
- Cloudflare describes this as “decoupling the brain from the hands”: model/orchestration can be provider-managed while execution infrastructure remains self-managed for security, compliance, performance, and observability. confidence: 1 vendor source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-devops-announcing-claude-managed-agents-on-cloudflare-8-minute-re.md]
- Andrej Karpathy announced he joined Anthropic for frontier LLM R&D while stating he remains interested in education and may resume that work later. confidence: 1 title/body summary source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-ai-karpathy-joins-anthropic-1-minute-read.md]
- Anthropic joined the Blender Development Fund as a Corporate Patron, with support dedicated to Blender core development and foundational features such as the Blender Python API; Blender later noted the membership shifted to a singular donation. confidence: 1 Blender Foundation source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-blender-releases-anthropic-joins-the-blender-development-fund-as-corpo.md]

### Typed entities
- product: Claude Managed Agents
- platform: Cloudflare Sandboxes
- platform: Cloudflare Developer Platform
- feature/control: customizable proxy
- feature/control: private-service connectivity
- feature/control: browser session recording
- person: Andrej Karpathy
- organization: Blender Foundation
- project/tool: Blender Python API

### Explicit relationships
- Claude Managed Agents can use Cloudflare Sandboxes as execution hands while Anthropic supplies the agent brain.
- Self-managed agent environments depend-on proxy, logging, sandbox-image, browser, email, and private-network controls.
- Anthropic's Blender funding complements its Claude creative-tool connector strategy by supporting the host creative platform's extensibility surface.

### HoneyDrunk implications
- Treat “brain/hands” separation as the preferred architecture for high-trust agents: model provider can reason, but execution should remain sandboxed, logged, and policy-controlled by HoneyDrunk.
- Blender Python API investment is a small but relevant signal that LLM vendors see Blender automation as strategic for creative workflows.

## 2026-05-26 compile additions

### Claims
- TestingCatalog reports leaked/product-surface evidence that Anthropic is preparing a `claude-mythos-1-preview`/Mythos 1 model for Claude Code and Claude Security, with strings referencing "Access to the Claude Mythos model in Claude Code and Claude Security." confidence: 1 secondary leak/reporting source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-ai-anthropic-prepares-mythos-1-for-claude-code-and-claude-securit.md]
- The same source reports Claude Security dashboard work for discovered vulnerabilities, seven-day/thirty-day history, and deeper triage views; current evidence points toward enterprise customers, not broad consumer release. confidence: 1 secondary leak/reporting source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-ai-anthropic-prepares-mythos-1-for-claude-code-and-claude-securit.md]
- Contrary Research claims Anthropic projected $10.9B Q2 revenue, $559M profit, improved compute spend from $0.71 to $0.56 per revenue dollar, October IPO expectations, and Claude Code as a major growth driver; treat as aggressive market-reporting signal requiring primary/financial verification. confidence: 1 business-newsletter source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-ai-anthropic-s-march-to-profitability-3-minute-read.md]

### Typed entities
- model/product: Claude Mythos / Mythos 1
- product: Claude Security
- initiative: Project Glasswing
- product: Claude Code
- concept: vulnerability-discovery model
- concept: enterprise security dashboard
- business event: Anthropic profitability/IPO rumor
- metric: compute spend per revenue dollar

### Explicit relationships
- Claude Mythos appears to depend-on stronger safeguards before general release, per Project Glasswing framing cited by TestingCatalog.
- Claude Security uses vulnerability discovery/triage surfaces to package model capabilities for enterprise security workflows.
- Anthropic growth claims depend-on Claude coding-tool enterprise adoption in Contrary's reporting, but those claims need verification before investment-grade decisions.

### HoneyDrunk implications
- Track Mythos/Claude Security as a possible security-review/pentest-assist surface, but do not route sensitive repos or security decisions to rumored/preview products without official docs, retention policy, and eval results.
- Claude Code demand is a market signal that coding agents are becoming business-critical; HoneyDrunk should keep provider abstraction and cost telemetry rather than assuming one vendor's capacity/pricing remains stable.

### Quality notes
- TestingCatalog and Contrary are useful early-warning sources, not canonical vendor docs. No leaked UI/source-code strings beyond the reported model/access labels were copied into actionable instructions.

## 2026-05-30 compile additions

### Claims
- Anthropic released Claude Opus 4.8 on 2026-05-28 as a direct Opus 4.7 upgrade with unchanged regular API pricing at $5/M input tokens and $25/M output tokens, and fast mode priced at $10/M input and $50/M output. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-claude-opus-4-8.md]
- Anthropic claims Opus 4.8 improves benchmark performance, agentic task judgment, honesty/uncertainty flagging, and alignment metrics compared with Opus 4.7; customer quotes and vendor evals are useful but require local task validation. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-claude-opus-4-8.md]
- Opus 4.8 launches with effort controls in claude.ai/Cowork, dynamic workflows in Claude Code, Messages API support for `system` entries inside the messages array, and a cheaper/faster Opus fast mode. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-claude-opus-4-8.md]
- Claude Code dynamic workflows are in research preview for Max, Team, and Enterprise plans and can dynamically write orchestration scripts that run tens to hundreds of parallel subagents, verify outputs, save progress, and resume long-running work. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-dynamic-workflows-in-claude-code.md]
- Anthropic reports a Bun Zig-to-Rust rewrite example using dynamic workflows: roughly 750,000 lines of Rust, 99.8% of the existing test suite passing, and eleven days from first commit to merge; the source states this is not yet in production, so treat it as a large-scale demonstration rather than production-proof evidence. confidence: 1 official vendor/product source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-dynamic-workflows-in-claude-code.md]
- Anthropic says Mythos-class models remain constrained by stronger cyber-safeguard requirements and expects broader availability in coming weeks, while Project Glasswing customers use Claude Mythos Preview for cybersecurity work. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-claude-opus-4-8.md]

### Typed entities
- model: Claude Opus 4.8
- model: Claude Opus 4.7
- model/class: Claude Mythos Preview / Mythos-class models
- initiative: Project Glasswing
- feature: effort control
- feature: fast mode
- feature: dynamic workflows
- feature/setting: `ultracode`
- feature/setting: `xhigh`
- API feature: `system` entries inside `messages`
- product: Claude Code CLI
- product: Claude Code Desktop
- product: Claude Code VS Code extension
- product: Claude Cowork
- project/example: Bun Zig-to-Rust rewrite

### Explicit relationships
- Claude Opus 4.8 supersedes Opus 4.7 as Anthropic's frontier Opus default, but migration depends-on local benchmark and token-budget measurement.
- Dynamic workflows use parallel subagents and verification loops to handle codebase-scale tasks.
- Effort controls trade response speed/rate-limit use against deeper reasoning and token consumption.
- Messages API mid-task system entries support harness updates to permissions, token budgets, or environment context without breaking prompt cache through a user turn.
- Mythos-class release depends-on stronger cyber safeguards before general availability.

### HoneyDrunk implications
- Benchmark Opus 4.8 against Opus 4.7/GPT/OpenAI/Google models on HoneyDrunk coding, review, browser, and document tasks before changing routing defaults.
- Treat dynamic workflows as high-budget machinery: require scoped tasks, repo sandboxing, test gates, cost telemetry, and human review before using them on important codebases.
- The Messages API system-entry change is relevant for HoneyDrunk agent harnesses that need to update permissions or context mid-run without forcing awkward user-message turns.

## 2026-05-31 compile additions

### Claims
- Claude Code agent view is a research-preview CLI surface for managing multiple Claude Code sessions, available on Pro, Max, Team, Enterprise, and Claude API plans; users can open it with `claude agents` or the left arrow from a session. confidence: 1 vendor product source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-claude-blog-agent-view-in-claude-code.md]
- Agent view shows session status, last response, last interaction time, and whether a session needs user input; users can peek, answer inline, or reattach to a full transcript. confidence: 1 vendor product source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-claude-blog-agent-view-in-claude-code.md]
- Existing Claude Code sessions can be sent to agent view with `/bg`, and new background sessions can launch with `claude --bg [task]`. confidence: 1 vendor product source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-claude-blog-agent-view-in-claude-code.md]
- Anthropic's containment article says Claude products use different isolation patterns for different users and risk profiles: claude.ai code execution uses ephemeral gVisor containers, Claude Code uses human-in-the-loop plus OS-level sandboxing, and Claude Cowork uses VM-backed containment for non-developer knowledge work. confidence: 1 official engineering source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md]
- Anthropic says Claude Cowork keeps credentials in the host keychain, mounts only selected workspace/.claude paths, supports read-only/read-write/read-write-no-delete mount modes, and must resolve symlinks before path validation to avoid escape. confidence: 1 official engineering source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md]

### Typed entities
- product: Claude Code agent view
- command: `claude agents`
- command: `/bg`
- command: `claude --bg`
- product: claude.ai code execution
- product: Claude Cowork
- isolation: gVisor container
- isolation: OS-level sandbox
- isolation: local VM
- control: read-write-no-delete mount
- control: symlink pre-resolution

### Explicit relationships
- Agent view complements dynamic workflows by giving users a session-management surface for many concurrent Claude Code runs.
- Claude platform containment depends-on matching isolation strength to user ability to evaluate risk.
- Claude Cowork's VM isolation depends-on mounted workspace paths, keychain-held credentials, and network/file policy rather than per-command user approval.
- Symlink resolution must precede path validation to prevent mounted-folder escape.

### HoneyDrunk implications
- Parallel Claude sessions need the same cost, status, and review discipline as dynamic workflows; more visible sessions do not remove human attention limits.
- When designing HoneyDrunk desktop agents, choose isolation based on target user expertise. Developers can handle more explicit review than nontechnical operators, but both need hard boundaries.

## 2026-06-05 compile additions

### Claims
- Anthropic says eligible Claude Pro, Max, Team, and Enterprise plan users can claim a separate monthly Claude Agent SDK credit starting 2026-06-15; Claude Platform API-key users continue pay-as-you-go and do not receive this subscription credit. confidence: 1 Anthropic Help Center source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-use-the-claude-agent-sdk-with-your-claude-plan.md]
- Agent SDK credit applies to Claude Agent SDK usage, `claude -p`, Claude Code GitHub Actions, and third-party apps authenticated through the Agent SDK, but not to interactive Claude Code, Claude web/desktop/mobile conversations, or Claude Cowork. confidence: 1 Anthropic Help Center source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-use-the-claude-agent-sdk-with-your-claude-plan.md]
- The credit is per-user, monthly, non-pooled, non-rollover, opt-in once, and drains before usage credits; after the credit is exhausted, additional Agent SDK requests require enabled usage credits or stop until refresh. confidence: 1 Anthropic Help Center source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-use-the-claude-agent-sdk-with-your-claude-plan.md]
- Anthropic explicitly says teams running shared production automation should use Claude Platform API keys for predictable pay-as-you-go billing rather than relying on individual Agent SDK monthly credits. confidence: 1 Anthropic Help Center source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-use-the-claude-agent-sdk-with-your-claude-plan.md]

### Typed entities
- product: Claude Agent SDK
- command: `claude -p`
- integration: Claude Code GitHub Actions
- plan: Claude Pro
- plan: Claude Max
- plan: Claude Team
- plan: Claude Enterprise
- billing concept: monthly Agent SDK credit
- billing concept: usage credits
- product: Claude Platform API key

### Explicit relationships
- Agent SDK credit separates non-interactive SDK automation from interactive Claude subscription limits for eligible subscription users after 2026-06-15.
- Individual subscription credits contradict pooled team automation budgets because credits are per-user and non-transferable.
- Claude Platform API keys supersede individual plan credits for shared production automation when predictable billing is required.

### HoneyDrunk implications
- Use personal Agent SDK credits for experimentation only; shared HoneyDrunk jobs need service-owned API keys, budgets, logs, and ownership.
- Track `claude -p` and GitHub Actions usage separately from interactive Claude Code usage when estimating team costs.

### Quality notes
- Billing and plan terms are date-sensitive. Recheck Anthropic account docs before changing automation routing or cost policy.

## 2026-06-10 compile additions: Fable 5 and Mythos 5

### Source-backed claims
- Anthropic launched Claude Fable 5 on 2026-06-09 as the first Mythos-class model made generally available; Anthropic positions it as its highest-capability GA model and especially strong for long-running coding, research, and knowledge-work tasks. superseded-by: 2026-06-12 Anthropic statement says a US government directive forced access suspension for all customers; capability/launch history preserved, but availability is no longer current. Source: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`; supersession source: `raw/2026-06-15-web-anthropic-statement-on-the-us-government-directive-to-suspend-access-t.md`. confidence: 2 official sources, last-confirmed 2026-06-15.
- Claude Mythos 5 uses the same underlying model family as Fable 5 but removes some Fable safeguards for trusted-access use cases; Anthropic initially routes it through Project Glasswing for US government partners, with selected biology access planned before broader trusted access. Source: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Fable 5 includes conservative safeguards that can fall back to Claude Opus 4.8 for some biology, chemistry, cyber, distillation, and other sensitive requests; Anthropic reports an average trigger rate under 5% of sessions. Source: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Fable 5 and Mythos 5 are priced at USD 10 per million input tokens and USD 50 per million output tokens, with API developers using the `claude-fable-5` model identifier for Fable. Source: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Mythos-class traffic requires 30-day provider retention for safety-classifier, jailbreak, attack, and false-positive analysis; Anthropic says retained traffic is not used to train models and is deleted after 30 days in almost all cases. Sources: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`, `raw/2026-06-10-web-github-changelog-claude-fable-5-is-generally-available-for-github-copilot-github-changelo.md`. confidence: 2 sources, last-confirmed 2026-06-10.
- GitHub Copilot makes Claude Fable 5 available to Copilot Pro+, Max, Business, and Enterprise users across major Copilot clients, but Business and Enterprise admins must explicitly enable a Fable 5 policy because this model does not follow the Zero Data Retention handling used by other Claude Copilot models. superseded-by: 2026-06-12 Anthropic statement says Fable 5 and Mythos 5 access was suspended for all users; recheck GitHub/Anthropic current access before routing work to Fable 5. Source: `raw/2026-06-10-web-github-changelog-claude-fable-5-is-generally-available-for-github-copilot-github-changelo.md`; supersession source: `raw/2026-06-15-web-anthropic-statement-on-the-us-government-directive-to-suspend-access-t.md`. confidence: 2 sources, last-confirmed 2026-06-15.

### Typed entities
- project: Claude Fable 5
- project: Claude Mythos 5
- project: Project Glasswing
- library/model: Claude Opus 4.8
- project: GitHub Copilot
- decision: whether HoneyDrunk allows non-ZDR Mythos-class model traffic in coding-agent workflows

### Explicit relationships
- Claude Fable 5 depends-on Mythos-class base capability plus additional safeguards and fallback routing.
- Claude Mythos 5 supersedes Mythos Preview for trusted-access partners.
- Claude Fable 5 contradicts the prior operational assumption that all Anthropic models exposed through Copilot can be treated as Zero Data Retention traffic.
- GitHub Copilot uses Claude Fable 5 behind an admin-controlled policy gate.

### HoneyDrunk implications
- Treat Fable 5 as a high-capability but non-ZDR model. It should be disabled for sensitive HoneyDrunk repositories until repo/data classifications and retention policy are explicit.
- Benchmark Fable 5 against existing coding models on HoneyDrunk tasks before adopting vendor benchmark claims for routing.
- For automation, record when Opus 4.8 fallback may change behavior or tool outcomes on sensitive-task boundaries.

### Quality notes
- Anthropic and GitHub are primary/vendor sources. Capability claims are useful routing signals, not local proof of superiority. No private prompts, retained traffic, or customer content were copied.

## 2026-06-15 compile additions: Fable/Mythos suspension and Project Glasswing expansion

### Source-backed claims
- Anthropic says a US government directive on 2026-06-12 required it to suspend access to Fable 5 and Mythos 5 for all customers because the order applied to foreign nationals and foreign national Anthropic employees; Anthropic states other Anthropic models are not affected. Source: `raw/2026-06-15-web-anthropic-statement-on-the-us-government-directive-to-suspend-access-t.md`. confidence: 1 official Anthropic source, last-confirmed 2026-06-15.
- Anthropic says the directive was based on a narrow potential Fable 5 jailbreak concern, not a disclosed universal jailbreak, and that Anthropic disagrees this should recall a commercial model deployed broadly. Source: `raw/2026-06-15-web-anthropic-statement-on-the-us-government-directive-to-suspend-access-t.md`. confidence: 1 official Anthropic source, last-confirmed 2026-06-15.
- Anthropic's prior Fable 5/Mythos 5 access assumptions are superseded operationally by the 2026-06-12 suspension until access is restored or new official terms are published. Source: `raw/2026-06-15-web-anthropic-statement-on-the-us-government-directive-to-suspend-access-t.md`. confidence: 1 official Anthropic source, last-confirmed 2026-06-15.
- Anthropic expanded Project Glasswing from roughly 50 initial partners to approximately 150 additional organizations, prioritizing critical infrastructure, vendors, maintainers, and organizations whose compromised codebases could affect very large populations. Source: `raw/2026-06-15-web-anthropic-expanding-project-glasswing.md`. confidence: 1 official Anthropic source, last-confirmed 2026-06-15.
- Anthropic reports Project Glasswing partners found more than 10,000 high- or critical-severity flaws using Claude Mythos Preview and that the bottleneck is shifting from finding vulnerabilities to verifying, disclosing, fixing, and deploying patches. Source: `raw/2026-06-15-web-anthropic-expanding-project-glasswing.md`. confidence: 1 official Anthropic source citing its own program update, last-confirmed 2026-06-15.

### Typed entities
- model: Claude Fable 5
- model: Claude Mythos 5
- model: Claude Mythos Preview
- program: Project Glasswing
- program: Cyber Verification Program
- actor: US government
- concept: model access suspension
- concept: narrow jailbreak
- concept: cyberdefender access

### Explicit relationships
- The US government directive supersedes prior Fable 5/Mythos 5 availability for all customers as of 2026-06-12.
- Fable 5 and Mythos 5 access depends-on external regulatory/national-security decisions as well as provider safety controls.
- Project Glasswing uses trusted partner access to advanced cyber models to strengthen defensive vulnerability discovery.
- Mythos-class vulnerability discovery causes a downstream patch-verification and disclosure bottleneck when findings exceed human triage capacity.

### HoneyDrunk implications
- Do not assume availability of frontier cyber/coding models is stable. Routing plans need fallback models and explicit failure behavior when a provider disables access.
- Treat Mythos/Fable-class security work as operationally volatile: even if capability is high, access, retention, and legal constraints can change abruptly.
- If HoneyDrunk uses AI vulnerability discovery at scale, plan the full pipeline: reproducibility, reachability triage, disclosure, patching, regression tests, and deployment tracking.

### Quality notes
- Anthropic is a primary source for its own posture but is also a party to the dispute. Government reasoning was not independently available in the raw source. No jailbreak technique or exploitable detail was copied.

## 2026-06-20 compile additions: Claude Code artifacts

### Source-backed claims
- Anthropic announced Claude Code artifacts as beta live, shareable web pages generated from a Claude Code session's full context, including codebase context, connectors, conversation, reasoning, diffs, dashboards, PR walkthroughs, incident timelines, release checklists, and design variations. Source: `raw/2026-06-20-web-anthropic-claude-code-now-supports-artifacts-5-minute-read.md`. confidence: 1 Anthropic product source, last-confirmed 2026-06-20.
- Artifacts update in place at the same link with version history, are private to the author by default, can be shared inside the organization, cannot be made public, and are governed by org-level toggles, role-based scoping, retention policies, and compliance API visibility. Source: `raw/2026-06-20-web-anthropic-claude-code-now-supports-artifacts-5-minute-read.md`. confidence: 1 source, last-confirmed 2026-06-20.

### Typed entities
- product: Claude Code
- feature: artifacts
- artifact type: PR walkthrough
- artifact type: incident page
- artifact type: release checklist
- control: organization-only sharing
- control: retention policy
- control: compliance API

### Explicit relationships
- Claude Code artifacts complement agent-run receipts by turning session state and evidence into a shared review surface.
- Artifact sharing depends-on organization authentication, role scoping, retention policy, and version history.
- Live artifacts can reduce status handoff cost but do not supersede source citations, test evidence, or repo-local run summaries for durable HoneyDrunk records.

### HoneyDrunk implications
- If Claude Code artifacts are used for HoneyDrunk reviews/incidents, keep canonical evidence in repo/GitHub/run summaries and use artifacts as collaborative views.
- Treat artifact retention and access as data-governance settings before sharing private repo or incident context.

### Quality notes
- Vendor product announcement. Availability, retention, export, and compliance behavior should be verified in the active Anthropic tenant before operational use.

## 2026-06-21 compile additions: Claude Design brand controls and workload identity federation

### Source-backed claims
- Anthropic says Claude Design can now stay on brand for daily work by using brand assets, style guidance, and reusable design context when producing work artifacts; treat as product-positioning evidence until tenant behavior and export controls are tested. Source: `raw/2026-06-21-web-anthropic-claude-design-now-stays-on-brand-for-daily-work.md`. confidence: 1 Anthropic product source, last-confirmed 2026-06-21.
- Anthropic announced Workload Identity Federation as generally available on the Claude Platform, reducing reliance on long-lived static API keys for workloads that can exchange identity assertions for platform access. Source: `raw/2026-06-21-web-anthropic-workload-identity-federation-wif-is-now-generally-available-.md`. confidence: 1 Anthropic product source, last-confirmed 2026-06-21.

### Typed entities
- product: Claude Design
- concept: brand-context reuse
- feature: Workload Identity Federation / WIF
- concept: workload identity
- credential pattern: static API key
- credential pattern: federated token exchange

### Explicit relationships
- Claude Design brand controls depend-on curated brand assets and style context; they do not supersede human brand review for public-facing assets.
- Workload Identity Federation supersedes static API keys for supported automation where workload identity can be asserted and scoped.
- Federated workload access complements existing agent credential guidance by moving secret custody from stored keys toward short-lived derived credentials.

### HoneyDrunk implications
- If Claude Design is used for HoneyDrunk brand work, keep source assets, review approvals, dimensions, and final artifacts in repo or asset storage; generated work is not canonical by itself.
- Prefer WIF-style authentication for shared Claude automation where supported, but document subject, audience, scope, expiry, logs, and fallback behavior.

### Quality notes
- Anthropic product sources are authoritative for feature positioning, but tenant availability, billing, retention, and exact identity-provider support should be verified before automation changes.
