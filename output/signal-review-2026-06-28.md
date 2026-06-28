# Lore Daily News Blast - 2026-06-28

## Blast summary

- Send to Discord: yes
- Theme: Agent trust boundaries are today's useful cluster: external tool data, security automation, retrieval structure, and auditability all need sharper controls.
- Coverage: 15 saved web sources reviewed; no fresh X posts were available from the latest X refresh.

## Top stories

1. Public telemetry can become an agent-injection channel
   - Main points: A reported "agentjacking" path uses public Sentry write keys to plant crafted error data that coding agents later consume as remediation context. The practical warning is broader than Sentry: logs, tickets, crash reports, and monitoring data become untrusted input once agents can read them and act.
   - Source: The New Stack
   - Source URL: https://thenewstack.io/agentjacking-sentry-mcp-attack
   - HoneyDrunk angle: Gate commands derived from externally influenced records before wiring agents to telemetry, issue, or support systems.

2. OpenAI is moving AI security from finding bugs toward landing fixes
   - Main points: The report says OpenAI expanded its security automation with code scanning, validation, patch generation, reporting, SARIF/CodeQL export, expert review, and open-source maintainer support. The important shift is operational: security models are being packaged as reviewable fix workflows, not just vulnerability detectors.
   - Source: TestingCatalog
   - Source URL: https://www.testingcatalog.com/openai-launches-new-security-tools-and-updates-gpt-5-5-cyber
   - HoneyDrunk angle: Useful direction for security automation, but capture primary docs or run local evals before changing HoneyDrunk gates.

3. GitHub adds context-aware LLM reasoning to secret scanning
   - Main points: GitHub is using contextual analysis to reduce false positives from generic secret detections by checking how suspicious values are used, such as API calls, auth headers, database clients, or cloud SDKs. It reports a 75.76% false-positive reduction against a 65% target while keeping upstream detection coverage unchanged.
   - Source: GitHub Blog
   - Source URL: https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale
   - HoneyDrunk angle: Prefer scanners that preserve broad coverage while adding auditable context, not scanners that simply suppress noisy findings.

4. Knowledge-agent structure may beat bigger-model brute force for specialized domains
   - Main points: The article argues that source extractions, concept pages, thesis files, primers, hybrid search, and multi-pass retrieval can let smaller or local models perform well on hard specialist tasks. The useful bit is the structure: retrieval quality comes from curated knowledge organization, not embeddings alone.
   - Source: Weighty Thoughts
   - Source URL: https://weightythoughts.com/p/knowledge-agents-beat-frontier-models
   - HoneyDrunk angle: Reinforces keeping Lore source citations, confidence notes, and concept pages as authority before adding heavier retrieval infrastructure.

5. Azure SDK release adds agentic retrieval and agent-hosting previews
   - Main points: Azure AI Search .NET and Python libraries now add knowledge bases and a retrieval client over sources such as Blob storage, search indexes, OneLake, and the web. The same release previews Agent Server libraries with host, health, shutdown, request-ID, and platform-header plumbing, while Azure SDK for Rust reaches stable 1.0.0 for core identity, storage, and Key Vault crates.
   - Source: Azure SDK Blog
   - Source URL: https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-may-2026/
   - HoneyDrunk angle: Track Azure AI Search knowledge bases for future Lore/Knowledge experiments, but keep flat-file sources as authority.

6. codebase-memory-mcp turns codebases into local structural graphs for agents
   - Main points: The project indexes repositories into a local graph of symbols, call chains, routes, services, ADRs, and cross-service relationships, exposed to coding agents through structured tools. Its README claims very fast indexing, large token savings, local processing, and broad language support.
   - Source: GitHub
   - Source URL: https://github.com/DeusData/codebase-memory-mcp
   - HoneyDrunk angle: Worth evaluating for HoneyHub agent-cockpit code navigation, but only after security, freshness, and generated-artifact review.

7. Jcode frames coding-agent harnesses around multi-session performance and memory
   - Main points: Jcode positions itself as a coding-agent harness for multi-session work, emphasizing low RAM use, fast startup, semantic memory, side panels, diagrams, and ambient memory consolidation. The useful signal is not the benchmark claims alone; it is the product shape around agent workflow ergonomics.
   - Source: GitHub
   - Source URL: https://github.com/1jehuang/jcode
   - HoneyDrunk angle: Watch as a HoneyHub comparison point for local cockpit responsiveness, memory, and multi-session UI.

8. Claude Code "Extended Thinking" output is not a full audit trail
   - Main points: The post says local session logs do not expose the actual full reasoning text; they expose signed or summarized reasoning artifacts unless higher-access arrangements apply. That matters for governance because inputs, outputs, tool calls, commands, diffs, and approvals are auditable evidence, while thinking summaries are not the same thing as causality logs.
   - Source: Patrick McCanna
   - Source URL: https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic
   - HoneyDrunk angle: Treat agent run receipts as action logs, not model-reasoning transcripts.

9. Unity/Playrix case study argues for D28 ROAS evaluation in mobile UA
   - Main points: Playrix describes scaling Township campaigns with Unity Ads' D28 IAP ROAS optimizer, especially on Google Play, by accepting higher early CPI when longer-term retention and revenue justified it. The signal is that D7-only campaign reads can miss durable payback behavior.
   - Source: Unity Blog
   - Source URL: https://unity.com/blog/playrix-township-roas-optimization-vector
   - HoneyDrunk angle: For any mobile/user-acquisition experiment, compare D7 and D28 curves before judging campaign quality.

10. Alien: Isolation 2 team says the long wait sharpened sequel expectations
   - Main points: Creative Assembly argues the original game's audience grew over time, making the sequel easier to frame around what players now value about the first game. The source is a trade interview, but the useful production lesson is that time-between-releases can become an asset when the core identity remains durable.
   - Source: Game Developer
   - Source URL: https://www.gamedeveloper.com/design/how-a-12-year-wait-made-alien-isolation-2-a-better-sequel
   - HoneyDrunk angle: Watch only.

## Top X posts

- No fresh X posts available from the latest refresh; older saved X captures were not reused.

## Worth watching

- Sakana Fugu's orchestration-model launch is a useful multi-agent sovereignty and long-horizon workflow signal, but today's capture is a ThreadReader/social source and needs primary docs before weighting heavily: https://threadreaderapp.com/thread/2068862070062485867.html
- Architecture Notes #106 has a useful roundup around AI-written-code incidents, agentic engineering levels, and deny-first agent sandboxing, but it is older roundup material rather than a fresh primary source: https://architecturenotes.co/p/arc-notes-weekly-106-arrowhead
- Materialist, a free Maya material-manager shelf, is a technical-art discovery item only until the linked repository, license, and workflow behavior are inspected: https://www.tech-artists.org/t/free-tool-materialist-a-material-manager-shelf-for-maya/18429

## Parked / low signal

- Polycount's "Learning Blender and Texturing" capture is mostly community-learning context with heavy forum scaffolding, not a production technique source: https://polycount.com/discussion/238683/learning-blender-and-texturing
- Architecture Notes #104 is older roundup material and should not outrank newer primary or near-primary sources today: https://architecturenotes.co/p/arc-notes-weekly-104-telluride

## Review notes

- Files reviewed: latest source summaries, latest X status summary, latest ingest summary, 15 saved web-source captures, 6 relevant compiled wiki pages, current HoneyDrunk focus, and HoneyDrunk charter.
- Blockers: Fresh X refresh failed because the local X capture command was unavailable; no fresh X posts were converted, so the report intentionally does not include stale X posts.
