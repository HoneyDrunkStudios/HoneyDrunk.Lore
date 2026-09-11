# Agent Context Management and Session Continuity

## Decision-useful summary

Agent context should be treated as a scarce runtime budget and an audit surface. Context Mode's README is strong README evidence for a growing pattern: keep large tool outputs out of the model window, run data-heavy analysis in sandboxed code, index durable context for retrieval, and preserve session continuity through hooks and local state instead of relying on the conversation transcript alone.

## Source-backed claims

- Context Mode is an MCP/server-plus-hook project that claims to reduce context use by routing large tool output through sandbox tools, returning only filtered results, and tracking context savings with `ctx_stats`. confidence: 1 project README source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-tldr-devops-context-mode-github-repo.md]
- The README says session continuity is stored in SQLite: file edits, git operations, tasks, errors, and user decisions are indexed into FTS5 and retrieved after compaction or resume rather than dumped wholesale back into the prompt. confidence: 1 README source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-tldr-devops-context-mode-github-repo.md]
- Context Mode's "think in code" pattern says agents should write small scripts for large-file/log/API analysis and return only the result, instead of using the model as the data processor. confidence: 1 README source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-tldr-devops-context-mode-github-repo.md]
- The README documents support or installation paths across Claude Code, Gemini CLI, VS Code Copilot, JetBrains Copilot, GitHub Copilot CLI, Cursor, OpenCode, KiloCode, OpenClaw, Codex CLI, Qwen Code, Kiro, Zed, Pi, and OMP, with hook coverage varying by host. confidence: 1 README source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-tldr-devops-context-mode-github-repo.md]

## Typed entities

- project/tool: Context Mode
- protocol: MCP
- database: SQLite
- search/index: FTS5
- tool: `ctx_execute`
- tool: `ctx_batch_execute`
- tool: `ctx_index`
- tool: `ctx_search`
- hook: PreToolUse
- hook: PostToolUse
- hook: PreCompact
- hook: SessionStart
- host: Codex CLI
- host: OpenClaw

## Explicit relationships

- Context management depends-on controlling where raw tool output goes, not only telling the model to be brief.
- Sandboxed execution complements retrieval by converting large raw data into small, task-specific outputs before model reasoning.
- Session continuity depends-on durable event capture and relevant retrieval when compaction removes conversational state.
- Hook support varies by host, so context routing depends-on platform-specific enforcement rather than MCP availability alone.

## HoneyDrunk implications

- For OpenClaw/Honeyclaw, prefer tool patterns that summarize or index large outputs before they enter the model context.
- Treat compaction recovery as a product requirement for long-running repository work: persist task state, touched files, errors, decisions, and validation evidence.
- Validate any Context Mode trial by measuring actual context saved, hook reliability, privacy boundaries, and whether retrieved session state is complete enough to resume safely.

## Confidence and quality notes

- Quality posture: README evidence only; claims should be tested locally before HoneyDrunk standardizes on the tool.
- Privacy filter: install tokens, local paths, and credential details were summarized as generic setup/credential-passthrough concepts; no private credentials were promoted.
