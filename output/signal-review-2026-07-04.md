# Lore Daily News Blast - 2026-07-04

## Blast summary

- Send to Discord: yes
- Theme: Today's useful cluster is agent systems becoming operational infrastructure: governed tool gateways, deterministic workflows, evidence-backed coding loops, and sharper supply-chain/security controls.
- Coverage: 15 public web sources reviewed; fresh X capture unavailable, so no X posts are included.

## Top stories

1. AI-hallucinated domains are becoming a real supply-chain attack surface
   - Main points: Unit 42 describes "phantom squatting," where attackers register plausible but nonexistent domains produced by LLMs for legitimate brands. Their study covered 913 brands, 685,339 URL queries, 2.1 million generated URLs, 13,229 malicious URLs, and roughly 250,000 unregistered hallucinated domains.
   - Source: Unit 42
   - Source URL: https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains
   - HoneyDrunk angle: Treat AI-suggested domains, docs links, API endpoints, and package/service URLs as untrusted until checked against primary sources or approved registries.

2. SGLang shows what agent-assisted engineering looks like when it is evidence-backed
   - Main points: The SGLang team frames useful coding-agent work as executable procedures with preflight checks, fixed benchmarks, artifact contracts, hard failure gates, and human review. Their kernel and diffusion examples show agents helping with real performance work only when workloads, baselines, correctness, profiling, and review evidence are locked down.
   - Source: LMSYS / SGLang Team
   - Source URL: https://www.lmsys.org/blog/2026-07-02-agent-assisted-sglang-development
   - HoneyDrunk angle: HoneyHub agent workflows should encode repeatable engineering loops as commands, artifacts, and stop conditions, not just long prompt instructions.

3. Google ADK 2.0 argues for deterministic workflow control around agents
   - Main points: Google says production agents fail when LLMs are asked to orchestrate routing, scheduling, and error handling that deterministic code can handle better. ADK 2.0 adds workflow graphs and dynamic workflows so LLM calls can sit inside known business flow, reducing variance, latency, and token cost.
   - Source: Google Developers Blog
   - Source URL: https://developers.googleblog.com/why-we-built-adk-20
   - HoneyDrunk angle: For HoneyHub and NovOutbox flows, use deterministic workflow code for known steps and reserve LLM calls for ambiguous reasoning or drafting nodes.

4. Anthropic publishes Fable 5 cyber-safeguard categories and a jailbreak severity scale
   - Main points: Anthropic says Fable 5 is globally available again and explains cyber classifier behavior across prohibited use, high-risk dual use, low-risk dual use, and benign use. The proposed Cyber Jailbreak Severity scale scores jailbreaks by capability gain, breadth, weaponization effort, and discoverability.
   - Source: Anthropic
   - Source URL: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework
   - HoneyDrunk angle: The severity axes are a useful vocabulary for classifying security-agent findings and jailbreak risk without flattening everything into "bad prompt."

5. Genkit packages full-stack conversational-agent plumbing behind one app interface
   - Main points: Google's Genkit Agents API adds server-managed or client-managed state, snapshots, streamed state/artifacts, remote agents, interrupts, detach/poll/abort support, and subagent delegation. The post positions agents as user-facing app primitives rather than one-off model calls.
   - Source: Google Developers Blog
   - Source URL: https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit
   - HoneyDrunk angle: HoneyHub's IDE direction needs this kind of durable session, artifact, and interrupt model if agent work becomes a first-class UI surface.

6. IBM ContextForge is a concrete MCP/A2A gateway candidate to study
   - Main points: ContextForge is an open-source registry and proxy that federates MCP, A2A, REST, and gRPC services with governance, discovery, auth, rate limiting, Admin UI, plugins, and OpenTelemetry tracing. It also explicitly warns against running untrusted MCP servers directly on the local filesystem.
   - Source: IBM GitHub
   - Source URL: https://github.com/IBM/mcp-context-forge
   - HoneyDrunk angle: Useful scouting for HoneyHub's cross-backend agent/tool routing, but only after reviewing auth, secret custody, tool provenance, and Windows/local behavior.

7. GitHub Copilot browser tools in VS Code are generally available
   - Main points: Copilot agents in VS Code can now drive isolated browser sessions, click/type/hover, inspect page content, read console errors, capture screenshots, and run scripted flows. GitHub documents tab isolation, explicit sharing for user-opened pages, sensitive-permission prompts, and enterprise domain allow/deny controls.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available
   - HoneyDrunk angle: Directly relevant to HoneyHub browser-probe testing; keep allowed domains and sensitive permission behavior explicit before relying on agent browser tests.

8. .NET 8 and .NET 9 now have the same support deadline
   - Main points: Microsoft says .NET 8 and .NET 9 both reach end of support on November 10, 2026; after that, no servicing updates, security fixes, or technical support will be provided. Microsoft recommends upgrading to .NET 10 LTS, supported through November 2028.
   - Source: .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support
   - HoneyDrunk angle: Inventory HoneyDrunk .NET 8/9 targets before the deadline and plan .NET 10 upgrades where the repos are still active.

9. uv adds preview vulnerability auditing and opt-in malware checks
   - Main points: Astral announced `uv audit` for dependency vulnerability/adverse-status scanning and an opt-in OSV malware check during sync through `UV_MALWARE_CHECK=1`. The malware check targets a lockfile-specific risk where quarantined packages may still be reachable through direct object-storage references.
   - Source: Astral
   - Source URL: https://astral.sh/blog/uv-audit
   - HoneyDrunk angle: Worth a small Python-project pilot before treating uv lockfiles as fully covered by existing dependency scans.

10. Unity adds Android XR glasses support with XREAL AURA
   - Main points: Unity announced support for XREAL AURA, its first XR glasses support and part of Google's Android XR ecosystem. The update highlights hands-first interaction, puck trackpad input, optical see-through design, smaller field of view, no eye tracking, and single APK support across Galaxy XR and XREAL AURA.
   - Source: Unity Blog
   - Source URL: https://unity.com/blog/unity-android-xr-wired-glasses-support
   - HoneyDrunk angle: Watch for the 2027 game-dev runway: hands-first Android XR is becoming more practical, but device constraints need design-time validation.

## Top X posts

Fresh X capture was unavailable today, so no X posts are included.

## Worth watching

- GitHub Copilot CLI can now use `GITHUB_TOKEN` in Actions with `copilot-requests: write`, reducing PAT risk but adding organization-billed AI-credit controls to think about. Source URL: https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions
- WinApp CLI makes .NET desktop package identity easier for local run/debug and MSIX packaging. Source URL: https://devblogs.microsoft.com/dotnet/packaging-dotnet-apps-winapp
- Unity XR Hand Capture and Hands Simulation reduce friction for hands-first interaction design. Source URL: https://unity.com/blog/hand-tracking-tools-for-unity-xr
- Soatok's informal threat-model guide is a useful lightweight checklist for assets, actors, paths, mitigations, assumptions, relationships, and accepted risks. Source URL: https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models
- Martin Fowler's Future of Software Development page is a curated index of AI-era software-development workshop outputs, not a new standalone thesis. Source URL: https://martinfowler.com/bliki/FutureOfSoftwareDevelopment.html

## Parked / low signal

- The failed Cato Networks source was not used because no readable article body was available from the saved capture.
- The Fowler page is useful as a pointer index, but the substantive claims live in linked workshop writeups and should be followed separately.
- ContextForge is promising but project-authored; treat it as scouting evidence until a local fit check is done.

## Review notes

- Files reviewed: latest public-source summary, latest X capture summary, latest wiki update summary, 15 saved public web captures, relevant compiled context pages, current HoneyDrunk focus, and the studio charter.
- Blockers: Fresh X capture was unavailable because local live sync was not usable; no fresh X items were converted, and stale posts were not reused.
