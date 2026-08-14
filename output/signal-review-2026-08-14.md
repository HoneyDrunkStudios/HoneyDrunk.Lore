# Lore Daily News Blast - 2026-08-14

## Blast summary

- Send to Discord: yes
- Theme: Agent infrastructure is getting more standardized and more security-sensitive at the same time, with .NET and GitHub ecosystem controls tightening around supply-chain risk.
- Coverage: 14 saved public web/feed sources and 0 fresh X posts reviewed

## Top stories

1. LiteLLM supply-chain compromise exposed AI control-plane blast radius
   - Main points: SecurityWeek reports that the LiteLLM compromise stemmed from a compromised Trivy dependency chain, not a direct attack on LiteLLM. The affected versions were live for about 40 minutes, but CloudSEK reconstructed exposure across more than 2,500 organizations and 434,000 CI/CD pipelines, including package credentials, cloud keys, SSH keys, tokens, environment variables, runtime data, and AI provider keys.
   - Source: SecurityWeek
   - Source URL: https://www.securityweek.com/over-2500-organizations-impacted-by-litellm-supply-chain-attack
   - HoneyDrunk angle: Treat AI libraries and proxies as high-value credential junctions; dependency freshness, CI isolation, and secret rotation matter more when the package can touch agent/provider keys.

2. NuGet is shortening API-key lifetimes and pushing Trusted Publishing
   - Main points: Microsoft says new NuGet.org API keys will be limited to 30 days starting August 17, 2026, and all older keys will expire on November 1, 2026. The recommended path is Trusted Publishing through OIDC so package publish workflows do not store long-lived publishing secrets.
   - Source: Microsoft .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/strengthening-nuget-supply-chain-security-reducing-api-key-lifetime/
   - HoneyDrunk angle: Directly relevant to any HoneyDrunk .NET package publishing path; long-lived package-publish secrets should be treated as technical debt.

3. MCP's 2026-07-28 release candidate makes HTTP deployments stateless
   - Main points: Google describes a new MCP release candidate that removes transport-level session management, replacing handshakes and session IDs with self-describing requests. The change makes load-balanced, serverless, and failure-tolerant deployments simpler, while adding HTTP headers for routing/audit and formalizing long-running task patterns.
   - Source: Google Developers Blog
   - Source URL: https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/
   - HoneyDrunk angle: Important for HoneyHub and private tool surfaces because it changes the cost and reliability model for remote tools, background tasks, and gateway observability.

4. Agent Plugins 1.0.0 standardizes packaging for skills and MCP servers
   - Main points: Google announced support for Agent Plugins 1.0.0, a vendor-neutral directory format maintained with Amazon, Cursor, Microsoft, OpenAI, and Vercel. The format intentionally handles packaging only: skills live in fixed locations, MCP servers live in `mcp.json`, and install, permissions, provenance, sandboxing, and UX remain separate concerns.
   - Source: Google Developers Blog
   - Source URL: https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
   - HoneyDrunk angle: Strong fit for portable HoneyHub/OpenClaw capabilities, but adoption should separate package convenience from trust, approval, and secret-handling policy.

5. Paperclip positions itself as an open-source control plane for teams of AI agents
   - Main points: Paperclip describes a Node.js and React system for managing AI agents with goals, org charts, tickets, budgets, approvals, routines, plugins, secrets, audit logs, and multi-company isolation. It explicitly frames itself as orchestration for agent organizations rather than a chatbot, workflow builder, or code review tool.
   - Source: Paperclip GitHub repository
   - Source URL: https://github.com/paperclipai/paperclip
   - HoneyDrunk angle: Useful competitive and design reference for HoneyHub's operator-facing agent IDE/control-plane direction, especially around budgets, heartbeats, approvals, and durable work state.

6. Meta Muse Glimmer offers a local Apache-2.0 multimodal agentic model option
   - Main points: Hugging Face reports day-zero library support for Meta's Muse Glimmer, a 30B local multimodal model with text, image, and video input support, released under Apache 2.0. The post positions it for privacy-aware coding, document analysis, personal assistants, and local agent setups, with support across Transformers, llama.cpp, vLLM, and hosted inference.
   - Source: Hugging Face Blog
   - Source URL: https://huggingface.co/blog/muse-glimmer
   - HoneyDrunk angle: Worth evaluating as a local/private model candidate only after checking hardware needs, safety posture, and real HoneyHub task quality.

7. Thoughtworks finds little evidence that agent-only TDD improves outcomes
   - Main points: Birgitta Bockeler's exploratory evaluation compared coding-agent runs with and without TDD-style instructions. The small sample did not show clear quality or mutation-score gains from agent-only TDD, while TDD runs used several times more tokens and often produced worse design because upfront modeling was constrained.
   - Source: Martin Fowler
   - Source URL: https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
   - HoneyDrunk angle: Supports prioritizing outcome checks, mutation tests, scenario approval, and review gates over ritualized "write tests first" prompts for agents.

8. Azure Developer CLI keeps moving toward agent-friendly provisioning
   - Main points: Microsoft's July azd roundup adds Azure AI Foundry project/agent modeling in `azure.yaml`, direct extension installation from registry paths, tool uninstall lifecycle support, container deployment to Azure App Service, and automatic non-interactive behavior in CI/CD or AI-agent environments. It also renames the `skill --host` flag to `--agent`, which may affect scripts.
   - Source: Microsoft Azure SDK Blog
   - Source URL: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-july-2026/
   - HoneyDrunk angle: Relevant to Azure-backed agent/server deployments and to avoiding hung automation when agents run cloud provisioning commands.

9. GitHub made centralized CodeQL default setup easier to govern
   - Main points: GitHub now lets organizations apply a custom CodeQL configuration file to code scanning default setup through the `github-codeql-config-file` repository property. The feature gives default setup the central control usually associated with advanced setup, without maintaining workflow files in every repository.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-08-04-customize-code-scanning-default-setup-at-scale/
   - HoneyDrunk angle: Useful for many-repo hygiene if HoneyDrunk wants one security-analysis policy with selected per-repo overrides.

10. Grabbit 2 shows practical Unity editor tooling for physics-driven set dressing
   - Main points: 80 Level's Grabbit 2 breakdown explains how a Unity editor plugin runs isolated manual physics simulation, generates temporary colliders, restores scene state, pools resources, and integrates with native editor tools. The plugin also exposes an optional MCP hook so an assistant can call real placement/scatter operations instead of guessing transforms.
   - Source: 80 Level
   - Source URL: https://80.lv/articles/how-grabbit-2-simulates-physics-inside-the-unity-editor
   - HoneyDrunk angle: Strong signal for the 2027 Unity/Blender runway: AI-directed art tools need real editor operations and cleanup guarantees, not coordinate guessing.

## Top X posts

No fresh X posts were available from the latest review window.

## Worth watching

- GitHub expanded secret scanning push protection for APIclub, Mistral AI, PostHog OAuth access tokens, and Resend API keys; useful for NovOutbox-style email/API surfaces but not a standalone headline today. Source URL: https://github.blog/changelog/2026-08-07-secret-scanning-coverage-updates/
- Foundry Local can run live speech-to-text in C# with local model lifecycle management and no cloud API key; useful for future voice/accessibility experiments. Source URL: https://devblogs.microsoft.com/dotnet/foundry-local-live-speech-to-text-csharp/
- The System Design Newsletter's research-agent walkthrough is a good refresher on loop stopping, tool control, audit, and evaluation, but the saved capture is partly a paid teaser. Source URL: https://newsletter.systemdesign.one/p/how-to-build-an-ai-research-agent-with-mcp
- The 80 Level stylized 3D scene breakdown is a practical production-process reference for modular assets, trim sheets, painterly texturing, and Unreal/Blender/Substance handoff. Source URL: https://80.lv/articles/turning-2d-concept-art-into-a-detailed-painterly-3d-world

## Parked / low signal

- None of the saved public sources were pure filler, but several overlap around agent infrastructure and should be consolidated rather than treated as separate decisions.
- Fresh X capture was unavailable, so no social posts were ranked.

## Review notes

- Files reviewed: latest saved public-source summary, latest social-source status, latest content-update summary, current HoneyDrunk focus, HoneyDrunk charter, 14 saved public source captures, and selected topic notes for context.
- Blockers: Fresh X capture unavailable because the local social refresh command/auth path failed; no stale posts were reused.
