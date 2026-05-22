# AI Coding Agent Security

## Decision-useful summary
AI coding agents should be treated as high-capability execution principals, not chat helpers. Docker's 2026 security survey/post argues that the recurring failure pattern is architectural: agents inherit the user's filesystem, secrets, network, and production privileges, then act autonomously on probabilistic judgments. The practical HoneyDrunk decision is to put safety in the execution layer: workspace-scoped sandboxes, blocked credential paths, scoped identities, network egress controls, human approval gates for irreversible actions, and audit logs. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]

## Claims
- AI coding agents run an observe-plan-act-repeat loop and may read files, run commands, write/deploy code, query databases, send messages, and call APIs under the permissions available in the launching environment. confidence: 1 source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- Docker identifies six recurring coding-agent risk categories: unrestricted filesystem access, excessive privilege inheritance, secrets leakage via agent context, prompt injection through ingested content, malicious skills/plugin supply chain, and autonomous action without human-in-the-loop. confidence: 1 source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- Natural-language directives such as “do not delete” are not security boundaries; irreversible actions need platform-level enforcement that the model cannot reason around. confidence: 1 source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- The post positions Docker Sandboxes / `sbx` as a microVM-based mitigation layer with workspace scoping, blocked credential-path mounts, network egress policies, git worktree isolation, proxy-injected secrets, resource caps, and audit logs. confidence: 1 vendor source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- The post cites multiple public incidents and studies, but several incident details are secondary/vendor-collected and should be verified from primary reports before being used as procurement-grade evidence. confidence: 1 vendor roundup source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]

## Typed entities
- concept: AI coding agent
- concept: agent execution principal
- concept: workspace-scoped execution
- concept: excessive privilege inheritance
- concept: prompt injection
- concept: agent skill/plugin supply chain
- product: Docker Sandboxes
- CLI/tool: sbx
- isolation type: microVM
- tool/product mentioned: Claude Code
- tool/product mentioned: Claude Cowork
- tool/product mentioned: Cursor
- tool/product mentioned: Replit Agent
- tool/product mentioned: Amazon Kiro
- tool/product mentioned: Google Antigravity
- threat: secrets leakage
- threat: malicious skills
- control: human-in-the-loop approval gate
- control: network egress policy
- control: blocked credential paths

## Explicit relationships
- AI coding agents use the launching user's ambient permissions unless given a separate scoped identity.
- Agent autonomy depends-on execution-layer controls when filesystem, secrets, network, production, or messaging tools are reachable.
- Prompt injection plus private data access plus external communication creates exfiltration risk.
- Malicious skills/plugins exploit the same trust boundary as the agent runtime because they run with agent-level permissions.
- Docker Sandboxes uses microVM isolation to constrain filesystem and network blast radius; this complements, not supersedes, least-privilege identity and human approvals.
- Natural-language safety instructions contradict reliable security enforcement when the underlying tool layer still permits destructive action.

## HoneyDrunk implications
- Default agent work should run in a scoped workspace with recoverable file operations and no ambient access to home-directory credentials.
- Treat agent identity as separate from Oleg/Honeyclaw identity wherever production/cloud access exists; use short-lived scoped tokens and audit logs.
- Require explicit approval gates outside the model for deletion, production database writes, public/external messaging, payments, and deployment.
- If Docker Sandboxes/sbx is evaluated, benchmark it against OpenClaw needs: Windows support, git worktree behavior, network policy ergonomics, secret injection model, and local dev speed.

## Confidence and quality notes
- Quality posture: decision-usable as a threat model and mitigation checklist, but vendor-authored and framed around Docker Sandboxes; validate tooling claims and incident details independently before buying/building around `sbx`.
- Privacy filter: raw contained public incident/person references; wiki retained only decision-relevant public names/tool names and did not copy secrets-like payloads beyond generic control descriptions.

## 2026-05-22 compile additions

### Claims
- Docker Gordon is a local-container workflow agent with broad shell, filesystem, Docker CLI, docs, and web capabilities, but every command/file/Docker operation is shown for explicit approval before running and permissions reset at session close. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- Docker states Gordon does not store code or personal information and says its AI providers do not retain user data, with processing running on SOC 2 Type 2 and ISO 27001 certified infrastructure; this is vendor assurance and should be validated against current terms before sensitive use. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- C#'s planned caller-unsafe model turns memory-unsafety into an explicit compile-time/API-contract surface, which is useful for detecting AI-generated unsafe API calls and dependency surfaces before runtime. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md; page: [[csharp-memory-safety-and-unsafe-code]]]

### Typed entities
- product: Docker Gordon
- control: explicit approval gate
- control: session-scoped permission
- assurance: SOC 2 Type 2
- assurance: ISO 27001
- language/runtime: C# / .NET
- control: compiler-enforced unsafe blocking

### Explicit relationships
- Docker Gordon's approval model mitigates surprise actions but depends-on user judgment and clear command previews.
- Vendor privacy assurances do not supersede HoneyDrunk's need for data-classification and local secrecy rules.
- Compiler unsafe enforcement complements agent sandboxing by blocking a class of unsafe generated code at build time.

### HoneyDrunk implications
- Do not enable auto-approve for Gordon or similar agents on repos with production credentials, broad filesystem access, or destructive Docker commands until sandbox/network/secret policies are proven.
- Add .NET unsafe policy checks to coding-agent review gates when C# 16/.NET 11 tooling becomes available.
