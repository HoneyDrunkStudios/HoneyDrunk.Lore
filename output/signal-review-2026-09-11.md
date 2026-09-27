# Lore Daily News Blast - 2026-09-11

## Blast summary

- Send to Discord: yes
- Theme: Today's useful cluster is agent runtime safety, credential boundaries, .NET 11 contract design, and Unity workflows for AI-assisted game development.
- Coverage: 15 saved web sources reviewed; no fresh X posts captured because live X sync was unavailable.

## Top stories

1. Google says adversaries are moving from AI prompting to agentic attack workflows
   - Main points: Google Threat Intelligence Group reports that threat actors are now using AI-enabled automation and multi-agent workflows across credential harvesting, reconnaissance, supply-chain compromise, and cloud abuse. The most decision-useful point is speed: one observed campaign moved from compromised cloud resource to large-scale credential harvesting in under six hours.
   - Source: Google Cloud / Google Threat Intelligence Group
   - Source URL: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai
   - HoneyDrunk angle: HoneyHub's agent surface should treat workspace config, package installs, CI tokens, and AI tool directories as live security boundaries, not developer convenience details.

2. Microsoft argues agent safety belongs in the environment, not the prompt
   - Main points: Microsoft describes production lessons from Azure SRE Agent: sandbox model-authored code, keep real credentials outside the runtime, classify actions by operation-target-evidence, and shape each session by caller authority. The core warning is that an agent will eventually do whatever its environment permits, whether by accident, hallucination, or injection.
   - Source: Microsoft Command Line
   - Source URL: https://commandline.microsoft.com/azure-sre-agent-restricting-environment-ai-safety/
   - HoneyDrunk angle: Directly relevant to HoneyHub's planned loop and cross-backend agent work: authority should be issued per task and enforced outside the agent-controlled workspace.

3. Microsoft publishes Agent Hooks as a testable governance contract for agents
   - Main points: Agent Hooks defines a framework-neutral interception contract with eight lifecycle points, three verdicts, fail-closed host obligations, approval binding, and a conformance kit. The post is useful because it turns "guardrails" into a measurable runtime contract rather than framework-specific callback folklore.
   - Source: Microsoft Command Line
   - Source URL: https://commandline.microsoft.com/agent-hooks-framework-neutral-ai-governance-contract/
   - HoneyDrunk angle: Useful reference material for HoneyHub governance design, especially if loop execution needs provable deny behavior and payload-free audit evidence.

4. GitHub Actions cache-mode is generally available
   - Main points: GitHub now lets workflows or jobs set cache access to read, write, write-only, or none, with job-level settings overriding workflow defaults. The feature is aimed at least-privilege cache access and reducing cache-poisoning risk, especially around lower-trust events.
   - Source: GitHub Changelog
   - Source URL: https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode
   - HoneyDrunk angle: Worth checking CI workflows for explicit cache intent before public launch and release packaging work.

5. LangChain adds managed credentials and per-caller identity for Managed Deep Agents
   - Main points: LangChain's Connections feature stores credentials in a LangSmith workspace and resolves them at runtime as either agent-owned or user-owned credentials. The important shift is per-caller OAuth identity: actions such as searching private repos or filing issues can happen under the asking user's identity rather than a shared service account.
   - Source: LangChain Blog
   - Source URL: https://www.langchain.com/blog/connections-managed-credentials-and-per-caller-identity-for-managed-deep-agents
   - HoneyDrunk angle: Reinforces the "who asked?" boundary for HoneyHub and any future shared agent cockpit or IDE surface.

6. PyRIT matures into a repeatable AI red-teaming toolkit
   - Main points: Microsoft says PyRIT now supports a GUI, scanner CLI, Python framework, and RAMPART agent test framework. The source emphasizes repeatable assessments, evidence collection, multimodal targets, and coverage-oriented risk evaluation rather than one-off jailbreak screenshots.
   - Source: Microsoft Command Line
   - Source URL: https://commandline.microsoft.com/pyrit-python-risk-identification-tool-ai-red-teaming-subject-matter-experts/
   - HoneyDrunk angle: Good candidate to evaluate as a structured test harness for AI-agent release gates, especially where HoneyHub needs recurring confidence instead of ad hoc safety checks.

7. .NET 11 Release Candidate 1 ships with a go-live license
   - Main points: Microsoft released .NET 11 RC1 with go-live support, Visual Studio 2026 Insiders support, C# 15 stabilization work, SDK/test improvements, reproducible container publishing, ASP.NET Core updates, and MAUI testing improvements. This is the point where trialing selected features in production-shaped paths becomes reasonable.
   - Source: .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/dotnet-11-rc-1/
   - HoneyDrunk angle: Watch for low-risk probes in HoneyHub/NovOutbox infrastructure, especially test, container, and API contract areas.

8. C# 15 unions and closed hierarchies land in ASP.NET Core scenarios
   - Main points: The .NET team explains how native unions and closed hierarchies work with System.Text.Json, Minimal APIs, MVC, SignalR, Blazor, and OpenAPI. The most useful distinction: use unions for fixed alternative shapes you do not control or discriminator-free legacy contracts, and closed hierarchies with discriminators for new related models you own.
   - Source: .NET Blog
   - Source URL: https://devblogs.microsoft.com/dotnet/unions-and-closed-hierarchies-in-aspnetcore/
   - HoneyDrunk angle: Useful for future API envelope and event-model design where exhaustive handling would reduce drift.

9. Unity ships an official Claude Code plugin
   - Main points: Unity's first-party plugin installs Unity-specific skills, the Unity CLI, and Unity's MCP server for live Editor control. The initial skill set covers project setup, UI systems, sprite workflows, URP/rendering, audio, gameplay, monetization, multiplayer, web builds, and localization.
   - Source: Unity Blog
   - Source URL: https://unity.com/blog/unity-plugin-for-claude-code
   - HoneyDrunk angle: Strong signal for the 2027 Unity/game-dev runway: first-party engine skills may be safer and more repeatable than general-purpose agent guesses.

10. DrakkenRidge shows a two-person open-world mobile VR production pattern
   - Main points: The Unity guest post explains how a two-person team used ECS for distant world rendering, texture atlasing, distance-based culling, entity LODs, Burst jobs, impostors, and traditional GameObjects for close VR interactions. The practical lesson is selective ECS adoption: use it where scale demands it and keep iteration-friendly workflows where player interaction is tight.
   - Source: Unity Blog
   - Source URL: https://unity.com/blog/drakkenridge-building-open-world-mobile-vr-rpg-unity-ecs
   - HoneyDrunk angle: Useful pattern library for future small-team Unity work, especially "optimize the world, keep interaction authoring humane."

## Top X posts

- No fresh X posts captured in the latest review window; omitted rather than reusing stale posts.

## Worth watching

- Cohere's North Mini Code serving post claims a decode megakernel can beat vLLM by 1.25x to 1.41x end-to-end on a single H100, with an OpenAI-compatible server and tool calling: https://cohere.com/blog/megakernels
- Gen Digital's Sage repo is a lightweight security layer for AI coding assistants, with URL reputation, local heuristics, prompt-injection detection, package checks, plugin scanning, AMSI support, and audit logs: https://github.com/gendigitalinc/sage
- Thoughtworks argues for micro-increment AI collaboration: ask for tiny formal artifacts, validate through tests and fitness functions, and keep feedback loops low-latency: https://www.thoughtworks.com/insights/blog/generative-ai/how-to-talk-with-ai

## Parked / low signal

- The Claude Code newsletter is useful as mainstream adoption context, but much of the saved capture is tutorial and promotional material: https://newsletter.systemdesign.one/p/claude-code-claude-md-best-practices
- The Maya Python API thread is niche and currently a troubleshooting seed rather than a broad strategic signal: https://www.tech-artists.org/t/array-attributes-in-maya-python-api-2-mpxnode/18533

## Review notes

- Files reviewed: 15 saved public web sources, latest X capture status, latest source-processing summary, current HoneyDrunk focus, and the HoneyDrunk charter.
- Blockers: Fresh X capture was unavailable in this run, so no X posts were ranked.
