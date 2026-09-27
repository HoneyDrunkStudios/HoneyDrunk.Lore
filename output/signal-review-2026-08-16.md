# Lore Daily News Blast - 2026-08-16

## Blast summary

- Send to Discord: yes
- Theme: Agent tooling is hardening around portable plugins, stateless MCP, .NET AI building blocks, explicit evaluation, and runtime security controls.
- Coverage: 13 saved public web sources and 0 fresh X posts reviewed

## Top stories

1. Agent Plugins 1.0 is generally available across Copilot surfaces
   - Main points: GitHub says Agent Plugins 1.0 now works in VS Code, Copilot CLI, the GitHub Copilot SDK, and the Copilot app on all Copilot plans. The practical shift is that skills and MCP server configuration can be packaged once while organizations govern plugins and marketplaces through managed settings and MCP allowlists.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/
   - HoneyDrunk angle: Directly relevant to HoneyHub/OpenClaw plugin policy: package portability does not replace provenance, permissions, server allowlists, or profile discipline.

2. MCP C# SDK 2.0 moves .NET MCP to stateless HTTP by default
   - Main points: Microsoft says the official MCP C# SDK v2.0 implements the 2026-07-28 protocol revision with stateless HTTP transport by default, ordinary HTTP routing headers, header/body mismatch rejection, and backward-compatible legacy handshakes. Multi Round-Trip Requests preserve interactive tool flows without long-lived sessions by returning input-required state and retrying with client responses.
   - Source: Microsoft .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/
   - HoneyDrunk angle: Strong signal for new HoneyDrunk .NET MCP servers: prefer stateless-compatible designs, explicit handles, durable task state, telemetry, and migration checks for older task/session behavior.

3. OWASP publishes a broad AI Agent Security Cheat Sheet
   - Main points: OWASP frames agent risk beyond prompt injection: tool abuse, data exfiltration, memory poisoning, goal hijacking, excessive autonomy, approval manipulation, cascading multi-agent failures, denial of wallet, and supply chain attacks. Its recommended controls center on least privilege, parameter-bound approvals, memory isolation, structured monitoring, circuit breakers, and adversarial release tests.
   - Source: OWASP Cheat Sheet Series
   - Source URL: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
   - HoneyDrunk angle: Treat this as the baseline checklist for HoneyHub Loop Console and any mutating agent tools before autonomy increases.

4. OpenAI describes agent-first repository design from a Codex-built product
   - Main points: OpenAI reports building an internal beta product where Codex generated the codebase, shifting engineers toward specifying intent, shaping feedback loops, and making application state legible to agents. The useful details are repository-local knowledge, worktree-local app instances, UI/log/metric/trace access, structural linting, quality grades, and recurring cleanup tasks.
   - Source: OpenAI
   - Source URL: https://openai.com/index/harness-engineering/
   - HoneyDrunk angle: Closely matches HoneyHub's IDE runway: invest in agent-legible state, mechanical invariants, and reviewable cleanup loops before chasing more parallelism.

5. OpenAI unpacks the Codex agent loop and its performance tradeoffs
   - Main points: OpenAI explains how Codex builds Responses API inputs from instructions, tools, environment context, conversation items, reasoning/tool-call outputs, and later turns. The important operational points are stateless request replay for ZDR compatibility, exact-prefix prompt caching, cache-miss risks from changing tools or models mid-thread, and automatic compaction when context grows.
   - Source: OpenAI
   - Source URL: https://openai.com/index/unrolling-the-codex-agent-loop/
   - HoneyDrunk angle: Useful for HoneyHub session design: stable tool sets, predictable environment context, and explicit compaction receipts affect cost, latency, and reproducibility.

6. Microsoft recaps the .NET AI building blocks
   - Main points: Microsoft frames .NET AI around `Microsoft.Extensions.AI` for provider-agnostic model access, `Microsoft.Extensions.VectorData` for semantic storage, Microsoft Agent Framework for agent workflows, and MCP for interoperability. The post highlights typed structured outputs, standardized usage details, logging/OpenTelemetry middleware, and multimodal content abstractions.
   - Source: Microsoft .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/dotnet-ai-essentials-the-core-building-blocks-explained/
   - HoneyDrunk angle: Good stack map for .NET services, but provider-specific gaps still need to be recorded before portability becomes a promise.

7. .NET AI evaluation adds tool-use agent quality metrics
   - Main points: Microsoft added `IntentResolutionEvaluator`, `TaskAdherenceEvaluator`, and `ToolCallAccuracyEvaluator` for conversational agents using tools, plus BLEU, GLEU, and F1 evaluators for reference-based text comparison. The agent-quality evaluators depend on an LLM judge and were tuned against OpenAI model families, while the NLP metrics do not need an LLM.
   - Source: Microsoft .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/exploring-agent-quality-and-nlp-evaluators/
   - HoneyDrunk angle: Relevant to the HoneyHub eval gate, but scores should be calibrated against HoneyDrunk human labels before they block releases.

8. Copilot weekly release adds more agent workflow controls
   - Main points: GitHub's weekly release notes include new model availability, easier plugin management, side-chat for agent questions, Copilot CLI `/tasks`, queued prompts and shell commands while a turn runs, headless `--plan` plus autopilot, `/rewind`, JetBrains memory, local Ollama support, and VS Code session/model-switching updates. The trend is toward multi-surface agent operation with more built-in task and recovery controls.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-08-13-github-copilot-weekly-releases-august-10/
   - HoneyDrunk angle: Watch for HoneyHub UX ideas around queued turns, subagent task visibility, and recoverable changes without weakening git/review discipline.

9. Azure Functions gets a Fluent API for UI-backed MCP Apps
   - Main points: Microsoft introduced a fluent configuration API that promotes an MCP tool into an MCP App by wiring an HTML view, title, permissions, Content Security Policy, static assets, visibility, and protocol metadata. It abstracts the resource/view plumbing so developers can focus on tool behavior and UI while still declaring security boundaries.
   - Source: Microsoft Azure SDK Blog
   - Source URL: https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/
   - HoneyDrunk angle: Useful for future HoneyHub tool panels, but UI-backed tools need ordinary embedded-web-app review: CSP, clipboard permissions, static asset hygiene, and model visibility.

10. Claude text watermarking and file provenance are rolling out for EU AI Act compliance
   - Main points: Anthropic says future Claude models will include text watermarking that changes the randomness source for low-stakes token choices without visible text changes, extra tokens, user identifiers, or practical quality impact. For supported generated files, Claude will attach C2PA-style content credentials rather than hidden metadata.
   - Source: Anthropic
   - Source URL: https://www.anthropic.com/news/claude-text-watermark
   - HoneyDrunk angle: Relevant to public writing, docs, and generated media provenance policy; watch for detector API details before relying on it operationally.

## Top X posts

No fresh X posts were available from the latest review window.

## Worth watching

- .NET MCP server publishing to NuGet is now a practical distribution pattern with templates, `.mcp/server.json`, environment declarations, generated client config, and searchable MCP Server package metadata. Source URL: https://devblogs.microsoft.com/dotnet/mcp-server-dotnet-nuget-quickstart/
- MCP C# SDK v1.0 remains useful migration background for protected-resource metadata discovery, incremental scopes, URL-mode elicitation, sampling tools, and experimental Tasks. Source URL: https://devblogs.microsoft.com/dotnet/release-v10-of-the-official-mcp-csharp-sdk/
- Thoughtworks' agentic transformation lens is broad strategy framing, but its emphasis on embedded governance, AI-ready data, transparent decision systems, and human oversight matches the direction of HoneyHub agent work. Source URL: https://www.thoughtworks.com/insights/looking-glass/looking-glass-2026/preparing-for-agentic-transformation

## Parked / low signal

- No filler items added. The lower-ranked sources were parked because they were background, broad strategy framing, or superseded by a stronger source in the same stack.

## Review notes

- Files reviewed: latest public-source summary, latest X-source status, latest content-update summary, current HoneyDrunk focus, HoneyDrunk charter, 13 public source captures from the latest saved window, and selected compiled topic notes for novelty/relevance context.
- Blockers: Fresh X capture was unavailable because the local X refresh/auth command path failed; no stale X posts were reused.
