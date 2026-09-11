---
source: "https://github.com/mksglu/context-mode"
title: "Context Mode (GitHub Repo)"
author: "unknown"
date_published: "2026-09-09"
date_clipped: "2026-09-11"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-09-09"
source_role: "primary-via-tldr"
---

# Context Mode (GitHub Repo)

Source: https://github.com/mksglu/context-mode

Context Mode
The other half of the context problem.
Used across teams at
The Problem
Every MCP tool call dumps raw data into your context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone. And when the agent compacts the conversation to free space, it forgets which files it was editing, what tasks are in progress, and what you last asked for. On top of that, the agent wastes output tokens on filler, pleasantries, and verbose explanations — burning context from both sides.
How Context Mode Solves It
Context Mode is an MCP server that solves all four sides of this problem:
Context Saving — Sandbox tools keep raw data out of the context window. 315 KB becomes 5.4 KB. 98% reduction.
Session Continuity — Every file edit, git operation, task, error, and user decision is tracked in SQLite. When the conversation compacts, context-mode doesn't dump this data back into context — it indexes events into FTS5 and retrieves only what's relevant via BM25 search. The model picks up exactly where you left off. If you don't --continue , previous session data is deleted immediately — a fresh session means a clean slate.
Think in Code — The LLM should program the analysis, not compute it. Instead of reading 50 files into context to count functions, the agent writes a script that does the counting and console.log() s only the result. One script replaces ten tool calls and saves 100x context. This is a mandatory paradigm across all 17 supported clients, plus the OpenClaw gateway integration: stop treating the LLM as a data processor, treat it as a code generator.
// Before: 47 × Read() = 700 KB. After: 1 × ctx_execute() = 3.6 KB.
ctx_execute ( "javascript" , `
const files = fs.readdirSync('src').filter(f => f.endsWith('.ts'));
files.forEach(f => console.log(f + ': ' + fs.readFileSync('src/'+f,'utf8').split('\\n').length + ' lines'));
` ) ;
No prose-style enforcement — context-mode keeps raw data out of context but never dictates how the model writes its final answer. Brevity, completeness, formatting — your model's call (or yours via your own CLAUDE.md / AGENTS.md ). Aggressive brevity prompts have been shown to degrade coding/reasoning benchmarks ( Moonshot AI on kimi-k2.5 ) — the routing block stays focused on where data goes , not on how the model talks .
Install
Platforms are grouped by install complexity. Hook-capable platforms get automatic routing enforcement. Non-hook platforms need a one-time routing file copy.
Claude Code — plugin marketplace, fully automatic
Prerequisites: Claude Code v1.0.33+ ( claude --version ). If /plugin is not recognized, update first: brew upgrade claude-code or npm update -g @anthropic-ai/claude-code .
Install:
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
Restart Claude Code (or run /reload-plugins ).
Verify:
/context-mode:ctx-doctor
All checks should show [x] . The doctor validates runtimes, hooks, FTS5, and plugin registration.
Routing: Automatic. The SessionStart hook injects routing instructions at runtime — no file is written to your project. The plugin registers all hooks (PreToolUse, PostToolUse, UserPromptSubmit, PreCompact, SessionStart, Stop) and 11 MCP tools — six sandbox tools ( ctx_batch_execute , ctx_execute , ctx_execute_file , ctx_index , ctx_search , ctx_fetch_and_index ) plus five meta-tools ( ctx_stats , ctx_doctor , ctx_upgrade , ctx_purge , ctx_insight ).
Slash Command
What it does
/context-mode:ctx-stats
Context savings — per-tool breakdown, tokens consumed, savings ratio.
/context-mode:ctx-doctor
Diagnostics — runtimes, hooks, FTS5, plugin registration, versions.
/context-mode:ctx-index
Index a local file or directory into the persistent FTS5 knowledge base.
/context-mode:ctx-search
Search previously indexed content.
/context-mode:ctx-upgrade
Pull latest, rebuild, migrate cache, fix hooks.
/context-mode:ctx-purge
Permanently delete all indexed content from the knowledge base.
/context-mode:ctx-insight
Opens the hosted Insight dashboard ( context-mode.com/insight ) in your browser — org analytics for AI-assisted engineering teams.
Note: Slash commands are a Claude Code plugin feature. On other platforms, type ctx stats , ctx doctor , ctx index , ctx search , ctx upgrade , or ctx insight in the chat — the model calls the MCP tool automatically. See Utility Commands .
Status line (optional): Claude Code's plugin manifest cannot declare a status line, so this is a one-time manual edit to ~/.claude/settings.json :
{
"statusLine" : {
"type" : " command " ,
"command" : " context-mode statusline "
}
}
After saving, restart Claude Code. The bar shows $ saved this session · $ saved across sessions · % efficient so you can see savings accumulate in real time. The wiring is path-free — context-mode statusline resolves through the bundled CLI regardless of where the plugin cache lives.
Alternative — MCP-only install (no hooks or slash commands)
claude mcp add context-mode -- npx -y context-mode
This gives you all 11 MCP tools without automatic routing. The model can still use them — it just won't be nudged to prefer them over raw Bash/Read/WebFetch. Good for trying it out before committing to the full plugin.
Gemini CLI — one config file, hooks included
Prerequisites: Node.js >= 22.5 (or Bun), Gemini CLI installed.
Install:
Install context-mode globally:
npm install -g context-mode
Add the following to ~/.gemini/settings.json . This single file registers the MCP server and all four hooks:
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode "
}
},
"hooks" : {
"BeforeTool" : [
{
"matcher" : " run_shell_command|read_file|read_many_files|grep_search|search_file_content|web_fetch|activate_skill|mcp__plugin_context-mode|mcp__context-mode|mcp__(?!.*context-mode) " ,
"hooks" : [{ "type" : " command " , "command" : " context-mode hook gemini-cli beforetool " }]
}
],
"AfterTool" : [
{
"matcher" : " " ,
"hooks" : [{ "type" : " command " , "command" : " context-mode hook gemini-cli aftertool " }]
}
],
"PreCompress" : [
{
"matcher" : " " ,
"hooks" : [{ "type" : " command " , "command" : " context-mode hook gemini-cli precompress " }]
}
],
"SessionStart" : [
{
"matcher" : " " ,
"hooks" : [{ "type" : " command " , "command" : " context-mode hook gemini-cli sessionstart " }]
}
]
}
}
Restart Gemini CLI.
Verify:
/mcp list
You should see context-mode: ... - Connected .
Routing: Automatic via SessionStart hook. Optionally copy routing instructions for full model awareness:
cp node_modules/context-mode/configs/gemini-cli/GEMINI.md ./GEMINI.md
Why the BeforeTool matcher? It targets only tools that produce large output ( run_shell_command , read_file , read_many_files , grep_search , search_file_content , web_fetch , activate_skill ) plus context-mode's own tools ( mcp__plugin_context-mode ). This avoids unnecessary hook overhead on lightweight tools while intercepting every tool that could flood your context window.
Full config reference: configs/gemini-cli/settings.json
VS Code Copilot — hooks with SessionStart
Prerequisites: Node.js >= 22.5 (or Bun), VS Code with Copilot Chat v0.32+.
Install:
Install context-mode globally:
npm install -g context-mode
Create .vscode/mcp.json in your project root:
{
"servers" : {
"context-mode" : {
"command" : " context-mode "
}
}
}
Create .github/hooks/context-mode.json :
{
"hooks" : {
"PreToolUse" : [
{ "type" : " command " , "command" : " context-mode hook vscode-copilot pretooluse " }
],
"PostToolUse" : [
{ "type" : " command " , "command" : " context-mode hook vscode-copilot posttooluse " }
],
"SessionStart" : [
{ "type" : " command " , "command" : " context-mode hook vscode-copilot sessionstart " }
]
}
}
Restart VS Code.
Verify: Open Copilot Chat and type ctx stats . Context-mode tools should appear and respond.
Routing: Automatic via SessionStart hook. Optionally copy routing instructions for full model awareness:
cp node_modules/context-mode/configs/vscode-copilot/copilot-instructions.md .github/copilot-instructions.md
Full hook config including PreCompact: configs/vscode-copilot/hooks.json
JetBrains Copilot — hooks with SessionStart
Prerequisites: Node.js >= 22.5 (or Bun), JetBrains IDE with GitHub Copilot plugin v1.5.57+.
Install:
Install context-mode globally:
npm install -g context-mode
Add MCP server via Settings UI: Settings > Tools > AI Assistant > Model Context Protocol (MCP) > Add Server :
Name: context-mode
Command: context-mode
Create .github/hooks/context-mode.json :
{
"hooks" : {
"PreToolUse" : [
{ "type" : " command " , "command" : " context-mode hook jetbrains-copilot pretooluse " }
],
"PostToolUse" : [
{ "type" : " command " , "command" : " context-mode hook jetbrains-copilot posttooluse " }
],
"SessionStart" : [
{ "type" : " command " , "command" : " context-mode hook jetbrains-copilot sessionstart " }
]
}
}
Restart the JetBrains IDE.
Verify: Open Copilot Chat and type ctx stats . Context-mode tools should appear and respond.
Routing: Automatic via SessionStart hook. Optionally copy routing instructions for full model awareness:
cp node_modules/context-mode/configs/jetbrains-copilot/copilot-instructions.md .github/copilot-instructions.md
Full hook config including PreCompact: configs/jetbrains-copilot/hooks.json
Full setup guide: docs/jetbrains-copilot.md
GitHub Copilot CLI — MCP + hooks
Prerequisites: Node.js >= 22.5 (or Bun), GitHub Copilot CLI ( copilot ) installed. Set COPILOT_HOME first if you use an isolated Copilot home.
Install — Option A (plugin, one command — recommended):
npm install -g context-mode # the plugin's MCP server runs the global binary
copilot plugin install mksglu/context-mode:configs/copilot-cli # registers MCP + hooks + routing skill
The bundle's .mcp.json pins CONTEXT_MODE_PLATFORM=copilot-cli , so context-mode self-identifies as Copilot — ctx_upgrade and platform detection resolve copilot-cli even when Claude Code is co-installed (whose ~/.claude/ would otherwise win). No context-mode upgrade / agent call needed. To try it from a local clone before it lands on the default branch, point Copilot at the bundle directory: copilot --plugin-dir /path/to/context-mode/configs/copilot-cli .
Install — Option B (manual, no plugin):
Install context-mode globally:
npm install -g context-mode
Register the MCP server with Copilot CLI's built-in command (writes ~/.copilot/mcp-config.json for you):
copilot mcp add context-mode -- context-mode
Configure hooks in ~/.copilot/hooks/context-mode.json (or $COPILOT_HOME/hooks/context-mode.json ). The config uses flat { "type": "command", "command": "..." } entries; context-mode also writes a top-level "version": 1 , but that field is optional — the Copilot CLI accepts hook configs that omit it (it is pinned only for self-documentation). Copilot CLI fires six events context-mode uses:
{
"version" : 1 ,
"hooks" : {
"preToolUse" : [{ "type" : " command " , "command" : " context-mode hook copilot-cli pretooluse " }],
"postToolUse" : [{ "type" : " command " , "command" : " context-mode hook copilot-cli posttooluse " }],
"preCompact" : [{ "type" : " command " , "command" : " context-mode hook copilot-cli precompact " }],
"sessionStart" : [{ "type" : " command " , "command" : " context-mode hook copilot-cli sessionstart " }],
"userPromptSubmitted" : [{ "type" : " command " , "command" : " context-mode hook copilot-cli userpromptsubmit " }],
"agentStop" : [{ "type" : " command " , "command" : " context-mode hook copilot-cli stop " }]
}
}
Or let context-mode write this hooks file for you: context-mode upgrade (run from a Copilot CLI context, or with CONTEXT_MODE_PLATFORM=copilot-cli ). upgrade writes the hooks file only — register the MCP server with copilot mcp add in step 2.
Restart Copilot CLI.
Plugins: Option A above uses Copilot CLI's plugin system, which registers MCP servers ( .mcp.json ), hooks ( hooks.json ), and skills ( skills/ ) together — not just skills/agents. The shipped bundle is configs/copilot-cli/ ; copilot plugin install owner/repo:path installs it in one command (no clone). Option B is the equivalent without a plugin.
Version note: the hook commands run the global context-mode ( context-mode hook copilot-cli … ), so they need a context-mode version with Copilot CLI support. On an older global the hooks are inert (no routing/capture) until you upgrade — but they do not block your tools (context-mode fails open). Upgrade with npm install -g context-mode@latest .
Verify: In a Copilot CLI session, type ctx stats . Context-mode tools should appear and respond. Run context-mode doctor to confirm hook + MCP registration.
Routing: Automatic via hooks (PreToolUse interception + SessionStart routing block). Auto-detected via MCP clientInfo.name ( GitHub Copilot CLI ) or, in a bare shell, a context-mode-written marker ( ~/.copilot/mcp-config.json or ~/.copilot/hooks/context-mode.json ) — not a bare ~/.copilot/ dir, so a co-installed-but-unconfigured Copilot CLI is not mis-detected as context-mode-on-copilot.
See docs/platform-support.md for the full reference. Tracking: #775 .
Cursor — hooks with stop support
Prerequisites: Node.js >= 22.5 (or Bun), Cursor with agent mode.
🚧 Work in progress — the Marketplace plugin is awaiting Cursor team review . Until it's listed, install via the local-folder path described in Option A. Tracking in #485 / #489 .
Option A — Marketplace plugin (recommended once published)
After Cursor lists context-mode in the Marketplace , install with one click. The plugin auto-registers MCP, hooks ( preToolUse , postToolUse , sessionStart , stop , afterAgentResponse ), rules, and skills. No manual config required.
Until then, use the local-folder path:
Windows (PowerShell) — Cursor does not follow Windows symlinks/junctions, so use robocopy :
git clone https: // github.com / mksglu / context - mode.git
cd context - mode
robocopy . " $ env: USERPROFILE \.cursor\plugins\local\context-mode " / MIR `
/ XD node_modules .git build web tests scripts .vscode `
/ XF * .log .gitignore * .bundle.mjs.map
macOS / Linux:
git clone https://github.com/mksglu/context-mode.git
ln -s " $PWD /context-mode " ~ /.cursor/plugins/local/context-mode
Restart Cursor. The plugin appears in Settings → Plugins as "Context Mode (Local)". To pull updates, re-run the same robocopy / ln -s line.
Note: if .cursor/hooks.json already contains context-mode entries from a prior Option B install, context-mode doctor will warn about duplicate hook firings. Remove one configuration to keep events single-fire.
Option B — Manual install (existing path)
Install context-mode globally:
npm install -g context-mode
Create .cursor/mcp.json in your project root (or ~/.cursor/mcp.json for global):
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode "
}
}
}
Create .cursor/hooks.json (or ~/.cursor/hooks.json for global):
{
"version" : 1 ,
"hooks" : {
"preToolUse" : [
{
"command" : " context-mode hook cursor pretooluse " ,
"matcher" : " Shell|Read|Grep|WebFetch|Task|MCP:ctx_execute|MCP:ctx_execute_file|MCP:ctx_batch_execute "
}
],
"postToolUse" : [
{
"command" : " context-mode hook cursor posttooluse "
}
],
"stop" : [
{
"command" : " context-mode hook cursor stop "
}
]
}
}
The preToolUse matcher is optional — without it, the hook fires on all tools. The stop hook fires when the agent turn ends and can send a followup message to continue the loop. afterAgentResponse is also available (fire-and-forget, receives full response text).
Copy the routing rules file. Cursor lacks a SessionStart hook, so the model needs a rules file for routing awareness:
mkdir -p .cursor/rules
cp node_modules/context-mode/configs/cursor/context-mode.mdc .cursor/rules/context-mode.mdc
Restart Cursor or open a new agent session.
Verify: Open Cursor Settings > MCP and confirm "context-mode" shows as connected. In agent chat, type ctx stats .
Routing: Hooks enforce routing programmatically via preToolUse / postToolUse / stop . The .cursor/rules/context-mode.mdc file provides routing instructions at session start since Cursor's sessionStart hook is currently rejected by their validator ( forum report ). Project .cursor/hooks.json overrides ~/.cursor/hooks.json .
Known limitation: Cursor accepts additional_context in hook responses but does not surface it to the model ( forum #155689 ). Routing relies on the .mdc rules file instead of hook context injection.
Full configs: configs/cursor/hooks.json | configs/cursor/mcp.json | configs/cursor/context-mode.mdc
OpenCode — TypeScript plugin with hooks
Prerequisites: Node.js >= 22.5 (or Bun), OpenCode installed.
Install:
Add to opencode.json in your project root (or ~/.config/opencode/opencode.json for global):
{
"$schema" : " https://opencode.ai/config.json " ,
"plugin" : [ " context-mode " ]
}
The plugin entry registers all 11 ctx_* tools natively and enables hooks — OpenCode calls context-mode's TypeScript plugin in-process, so there is no redundant stdio MCP child per session.
(Optional) Copy the routing rules file. The model needs an AGENTS.md file for routing awareness:
cp node_modules/context-mode/configs/opencode/AGENTS.md AGENTS.md
This tells the model which tools to use and which commands are blocked. Without it, hooks still enforce routing — but the model won't know why a command was denied.
Restart OpenCode.
Verify: In the OpenCode session, type ctx stats . Context-mode tools should appear and respond.
Upgrade note: If an existing config has BOTH plugin: ["context-mode"] AND mcp.context-mode , OpenCode will register zero ctx_* tools — the plugin path correctly suppresses MCP duplicates, but the legacy MCP entry confuses the loader. Run context-mode upgrade to remove the legacy mcp.context-mode entry; your other MCP servers are preserved. v1.0.140+ emits a stderr diagnostic with the same guidance when this happens.
Routing: Hooks enforce routing programmatically via tool.execute.before and tool.execute.after . The optional AGENTS.md file provides routing instructions for model awareness. The experimental.session.compacting hook builds resume snapshots when the conversation compacts. The experimental.chat.system.transform hook injects the routing block and prior-session snapshots at session start, enabling session continuity across restarts. The chat.message hook captures user prompts and decisions (UserPromptSubmit equivalent).
Note: OpenCode lacks a real SessionStart hook ( #14808 , #5409 ). The plugin uses experimental.chat.system.transform as a surrogate — it injects both the routing block and resume snapshots into the system prompt. User-prompt capture uses chat.message instead of the missing UserPromptSubmit hook. AGENTS.md/CLAUDE.md/CONTEXT.md rules are captured automatically on first hook fire per project.
Full configs: configs/opencode/opencode.json | configs/opencode/AGENTS.md
KiloCode — TypeScript plugin with hooks
Prerequisites: Node.js >= 22.5 (or Bun), KiloCode installed.
Install:
Add to kilo.json in your project root (or ~/.config/kilo/kilo.json for global):
{
"$schema" : " https://app.kilo.ai/config.json " ,
"plugin" : [ " context-mode " ]
}
The plugin entry registers all 11 ctx_* tools natively and enables hooks — KiloCode calls context-mode's TypeScript plugin in-process, so there is no redundant stdio MCP child per session.
(Optional) Copy the routing rules file. KiloCode shares the OpenCode plugin architecture, so the model needs an AGENTS.md file for routing awareness:
cp node_modules/context-mode/configs/opencode/AGENTS.md AGENTS.md
Restart KiloCode.
Verify: In the KiloCode session, type ctx stats . Context-mode tools should appear and respond.
Upgrade note: If an existing config has BOTH plugin: ["context-mode"] AND mcp.context-mode , KiloCode will register zero ctx_* tools — the plugin path correctly suppresses MCP duplicates, but the legacy MCP entry confuses the loader. Run context-mode upgrade to remove the legacy mcp.context-mode entry; your other MCP servers are preserved. v1.0.140+ emits a stderr diagnostic with the same guidance when this happens.
Routing: Hooks enforce routing programmatically via tool.execute.before and tool.execute.after . The optional AGENTS.md file provides routing instructions for model awareness. The experimental.session.compacting hook builds resume snapshots when the conversation compacts. The experimental.chat.system.transform hook injects the routing block and prior-session snapshots at session start, enabling session continuity across restarts. The chat.message hook captures user prompts and decisions (UserPromptSubmit equivalent).
Note: KiloCode shares the same plugin architecture as OpenCode, using the OpenCodeAdapter with platform-specific configuration paths ( kilo.json instead of opencode.json , ~/.config/kilo/ instead of ~/.config/opencode/ ). Like OpenCode, it lacks a real SessionStart hook — the plugin uses experimental.chat.system.transform as a surrogate. User-prompt capture uses chat.message instead of the missing UserPromptSubmit hook. AGENTS.md/CLAUDE.md/CONTEXT.md rules are captured automatically on first hook fire per project.
OpenClaw / Pi Agent — native gateway plugin
Prerequisites: OpenClaw gateway running ( >2026.1.29 ), Node.js 22+.
context-mode runs as a native OpenClaw gateway plugin, targeting Pi Agent sessions (Read/Write/Edit/Bash tools). Unlike other platforms, there's no separate MCP server — the plugin registers directly into the gateway runtime via OpenClaw's plugin API .
Install:
Clone and install:
git clone https://github.com/mksglu/context-mode.git
cd context-mode
npm run install:openclaw
The installer uses $OPENCLAW_STATE_DIR from your environment (default: /openclaw ). To specify a custom path:
npm run install:openclaw -- /path/to/openclaw-state
Common locations: Docker — /openclaw (the default). Local — ~/.openclaw or wherever you set OPENCLAW_STATE_DIR .
The installer handles everything: npm install , npm run build , better-sqlite3 native rebuild, extension registration in runtime.json , and gateway restart via SIGUSR1.
Open a Pi Agent session.
Verify: The plugin registers 8 hooks via api.on() (lifecycle) and api.registerHook() (commands). Type ctx stats to confirm tools are loaded.
Routing: Automatic. All tool interception, session tracking, and compaction recovery hooks activate automatically — no manual hook configuration or routing file needed.
Minimum version: OpenClaw >2026.1.29 — this includes the api.on() lifecycle fix from PR #9761 . On older versions, lifecycle hooks silently fail. The adapter falls back to DB snapshot reconstruction (less precise but preserves critical state).
Full documentation: docs/adapters/openclaw.md
Codex CLI — MCP + hooks
Prerequisites: Node.js >= 22.5 (or Bun), Codex CLI installed.
Install:
Add the context-mode marketplace and install the plugin from Codex's plugin UI:
codex plugin marketplace add mksglu/context-mode
Enable plugin-provided hooks while the Codex feature is still gated:
[ features ]
plugin_hooks = true
hooks = true
Feature flag note: Current Codex builds expose hooks under [features].hooks
(or codex --enable hooks ). Prefer [features].hooks ; [features].codex_hooks
remains accepted as a legacy alias in current Codex builds. Bundled plugin hooks
additionally require plugin_hooks until Codex enables plugin hooks by default.
Custom storage location: if Codex cannot write the adapter default storage directory, set
CONTEXT_MODE_DIR to an absolute writable root in the environment that launches Codex. Sessions
and stats use <root>/sessions ; indexed content uses <root>/content .
CONTEXT_MODE_DIR= " $HOME /.codex-context-mode " codex
Restart Codex CLI and verify MCP with ctx stats .
ctx stats proves the plugin MCP server is installed and reachable; it does
not prove hooks are trusted or running.
Review and trust the context-mode plugin hooks if Codex prompts for hook
approval. Plugin hooks are only active after both feature flags are enabled
and Codex has accepted the hook commands.
The Codex plugin manifest provides MCP via .codex-plugin/mcp.json , skills via
skills/ , and bundled hooks via .codex-plugin/hooks.json . No manual
[mcp_servers.context-mode] block or $CODEX_HOME/hooks.json is needed when
plugin_hooks is enabled and the plugin hooks are trusted.
Node/PATH note: context-mode still needs node visible to the Codex process.
The plugin removes manual Codex config, but it does not vendor Node or inherit
login-shell PATH fixes automatically.
Manual fallback for Codex builds without plugin_hooks :
Install context-mode globally:
npm install -g context-mode
Add to ~/.codex/config.toml :
[ features ]
hooks = true
[ mcp_servers . context-mode ]
command = " context-mode "
[ mcp_servers . context-mode . env ]
CONTEXT_MODE_PLATFORM = " codex "
Create $CODEX_HOME/hooks.json (or ~/.codex/hooks.json when CODEX_HOME is unset):
{
"hooks" : {
"PreToolUse" : [{ "matcher" : " local_shell|shell|shell_command|exec_command|Bash|Shell|apply_patch|Edit|Write|grep_files|ctx_execute|ctx_execute_file|ctx_batch_execute|ctx_fetch_and_index|ctx_search|ctx_index|mcp__ " , "hooks" : [{ "type" : " command " , "command" : " context-mode hook codex pretooluse " }] }],
"PostToolUse" : [{ "hooks" : [{ "type" : " command " , "command" : " context-mode hook codex posttooluse " }] }],
"SessionStart" : [{ "hooks" : [{ "type" : " command " , "command" : " context-mode hook codex sessionstart " }] }],
"PreCompact" : [{ "hooks" : [{ "type" : " command " , "command" : " context-mode hook codex precompact " }] }],
"UserPromptSubmit" : [{ "hooks" : [{ "type" : " command " , "command" : " context-mode hook codex userpromptsubmit " }] }],
"Stop" : [{ "hooks" : [{ "type" : " command " , "command" : " context-mode hook codex stop " }] }]
}
}
PreToolUse enforces deny/block routing today and is prepared for input rewrites once Codex supports them. PostToolUse captures session events. PreCompact builds the resume snapshot before compaction. SessionStart restores state after compaction. UserPromptSubmit captures user decisions and corrections. Stop records turn-end state.
Note: Codex PreToolUse routing currently supports deny rules only (blocks dangerous commands). It still needs upstream updatedInput support before context-mode can rewrite tool input; track openai/codex#18491 . Context injection ( additionalContext ) is not supported in Codex PreToolUse — it works via PostToolUse and SessionStart instead. This is handled automatically.
PreCompact support is runtime-gated: it is present in Codex CLI 0.130.0, while the public Codex hooks docs may lag the shipped hook-event list. Older Codex builds that do not emit PreCompact will not create pre-compaction snapshots.
Copy routing instructions (recommended even with hooks for full routing awareness):
CM_ROOT= " $( npm root -g ) /context-mode "
cp " $CM_ROOT /configs/codex/AGENTS.md " ./AGENTS.md
For global use: CM_ROOT="$(npm root -g)/context-mode"; cp "$CM_ROOT/configs/codex/AGENTS.md" ~/.codex/AGENTS.md . Global applies to all projects. If both exist, Codex CLI merges them.
Restart Codex CLI.
Verify: Start a session and type ctx stats to verify MCP. To verify hook routing, confirm Codex lists/trusts the context-mode plugin hooks, then run a command that matches the routing rules.
Routing: MCP tools work after plugin install. Plugin hook routing is active only when hooks and plugin_hooks are enabled and Codex trusts the plugin hook commands. Manual hook routing is active when $CODEX_HOME/hooks.json or ~/.codex/hooks.json is configured. The AGENTS.md file provides routing instructions for model awareness.
Kimi Code — MCP + hooks (TOML config, same JSON wire protocol as Codex)
Prerequisites: Node.js >= 22.5 (or Bun), Kimi Code CLI installed.
Install context-mode:
npm install -g context-mode
Add context-mode as an MCP server. Add to ~/.kimi-code/mcp.json :
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode " ,
"args" : []
}
}
}
Add hooks to ~/.kimi-code/config.toml :
[[ hooks ]]
event = " PreToolUse "
matcher = " Bash|Shell|Read|Edit|Write|WebFetch|Agent|ctx_execute|ctx_execute_file|ctx_batch_execute|ctx_fetch_and_index|ctx_search|ctx_index|mcp__ "
command = " context-mode hook kimi pretooluse "
timeout = 30
[[ hooks ]]
event = " PostToolUse "
command = " context-mode hook kimi posttooluse "
timeout = 30
[[ hooks ]]
event = " SessionStart "
command = " context-mode hook kimi sessionstart "
timeout = 30
[[ hooks ]]
event = " PreCompact "
command = " context-mode hook kimi precompact "
timeout = 30
[[ hooks ]]
event = " UserPromptSubmit "
command = " context-mode hook kimi userpromptsubmit "
timeout = 30
[[ hooks ]]
event = " Stop "
command = " context-mode hook kimi stop "
timeout = 30
Restart Kimi Code CLI and verify MCP with ctx stats .
Note: Kimi Code uses the same JSON stdin/stdout wire protocol as Codex, but accepts additionalContext , updatedInput , and permissionDecision: "ask" in PreToolUse responses (Codex rejects these). The kimi hook normalizes ContentPart[] prompt arrays to strings for downstream extractors.
(Optional) Copy the routing instructions file for your project:
cp " $( npm root -g ) /context-mode/configs/codex/AGENTS.md " ./AGENTS.md
Or for global use:
CM_ROOT= " $( npm root -g ) /context-mode " ; cp " $CM_ROOT /configs/codex/AGENTS.md " ~ /.kimi-code/AGENTS.md
Full documentation: docs/adapters/kimi-code.md
Qwen Code — MCP + hooks (identical wire protocol to Claude Code)
Prerequisites: Node.js >= 22.5 (or Bun), Qwen Code installed ( npm install -g @qwen-code/qwen-code ).
Install context-mode:
npm install -g context-mode
Add context-mode as an MCP server. Add to ~/.qwen/settings.json :
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode " ,
"args" : []
}
}
}
Add hooks for routing enforcement and session tracking. Add to ~/.qwen/settings.json :
{
"hooks" : {
"PreToolUse" : [{ "matcher" : " run_shell_command|read_file|read_many_files|grep_search|web_fetch|agent|mcp__plugin_context-mode_context-mode__ctx_execute|mcp__plugin_context-mode_context-mode__ctx_execute_file|mcp__plugin_context-mode_context-mode__ctx_batch_execute|mcp__(?!.*context-mode) " , "hooks" : [{ "type" : " command " , "command" : " context-mode hook qwen-code pretooluse " }] }],
"PostToolUse" : [{ "matcher" : " " , "hooks" : [{ "type" : " command " , "command" : " context-mode hook qwen-code posttooluse " }] }],
"SessionStart" : [{ "matcher" : " " , "hooks" : [{ "type" : " command " , "command" : " context-mode hook qwen-code sessionstart " }] }],
"PreCompact" : [{ "matcher" : " " , "hooks" : [{ "type" : " command " , "command" : " context-mode hook qwen-code precompact " }] }],
"UserPromptSubmit" : [{ "matcher" : " " , "hooks" : [{ "type" : " command " , "command" : " context-mode hook qwen-code userpromptsubmit " }] }]
}
}
Copy routing instructions (recommended for full routing awareness):
cp node_modules/context-mode/configs/qwen-code/QWEN.md ./QWEN.md
For global use: cp node_modules/context-mode/configs/qwen-code/QWEN.md ~/.qwen/QWEN.md
Restart Qwen Code.
Verify: Start a session and type ctx stats . Context-mode tools should appear and respond.
Note: Qwen Code uses the same hook wire protocol as Claude Code (JSON stdin/stdout, same event names). Auto-detected via MCP clientInfo ( qwen-cli-mcp-client-* ) or QWEN_PROJECT_DIR env var.
Antigravity IDE — MCP-only, no hooks
This is the Antigravity desktop IDE . For the agy command-line tool , see Antigravity CLI ( agy ) below — it installs as a full plugin with hooks.
Prerequisites: Node.js >= 22.5 (or Bun), the Antigravity IDE installed.
Install:
Install context-mode globally:
npm install -g context-mode
Add to ~/.gemini/antigravity/mcp_config.json :
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode "
}
}
}
Copy routing instructions (Antigravity has no hook support):
cp node_modules/context-mode/configs/antigravity/GEMINI.md ./GEMINI.md
Restart Antigravity.
Verify: In an Antigravity session, type ctx stats . Context-mode tools should appear and respond.
Routing: Manual. The GEMINI.md file is the only enforcement method (~60% compliance). There is no programmatic interception. Auto-detected via MCP protocol handshake ( clientInfo.name ) — no manual platform configuration needed.
Full configs: configs/antigravity/mcp_config.json | configs/antigravity/GEMINI.md
Antigravity CLI ( agy ) — plugin (MCP + skill + hooks)
The agy command-line tool , not the Antigravity desktop IDE above.
Prerequisites: Node.js >= 22.5 (or Bun), Antigravity CLI ( agy ) ≥ 1.0.7 ( agy update to upgrade). Verified on agy 1.0.10.
Install:
npm install -g context-mode # the plugin's MCP server + hooks run the global binary
agy plugin install https://github.com/mksglu/context-mode/tree/main/configs/antigravity-cli # registers MCP + rule + skill + hooks
Restart agy .
MCP-only (no plugin, no hooks): if you only want the ctx_* tools, skip the plugin and add context-mode to agy's global MCP profile ~/.gemini/config/mcp_config.json (distinct from the Antigravity IDE's ~/.gemini/antigravity/ path), then restart agy :
{ "mcpServers" : { "context-mode" : { "command" : " context-mode " } } }
Verify: type ctx stats in an agy session, or run any prompt from Try It and check the savings. context-mode doctor confirms MCP + hook registration. Remove with agy plugin uninstall context-mode .
Routing: the routing rule and skill provide the instruction layer; bounded PreToolUse blocks high-flood tools and PostToolUse captures sessions. The bundle pins CONTEXT_MODE_PLATFORM=antigravity-cli so agy is detected even when Claude Code is co-installed ( #774 ).
Kiro — hooks with steering file
Prerequisites: Node.js >= 22.5 (or Bun), Kiro with MCP enabled (Settings > search "MCP").
Install:
Install context-mode globally:
npm install -g context-mode
Add to .kiro/settings/mcp.json in your project (or ~/.kiro/settings/mcp.json for global):
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode "
}
}
}
Create .kiro/hooks/context-mode.json :
{
"name" : " context-mode " ,
"description" : " Context-mode hooks for context window protection " ,
"hooks" : {
"preToolUse" : [
{ "matcher" : " execute_bash|fs_read|@context-mode/ctx_execute|@context-mode/ctx_execute_file|@context-mode/ctx_batch_execute|@(?!context-mode/) " , "command" : " context-mode hook kiro pretooluse " }
],
"postToolUse" : [
{ "matcher" : " * " , "command" : " context-mode hook kiro posttooluse " }
]
}
}
Copy routing instructions. Kiro's agentSpawn (SessionStart) is not yet implemented, so the model needs a routing file at session start:
cp node_modules/context-mode/configs/kiro/KIRO.md ./KIRO.md
Restart Kiro.
Verify: Open the Kiro panel > MCP Servers tab and confirm "context-mode" shows a green status indicator. In chat, type ctx stats .
Routing: Hooks enforce routing programmatically via preToolUse / postToolUse . The KIRO.md file provides routing instructions since agentSpawn (SessionStart equivalent) is not yet wired. Tool names appear as @context-mode/ctx_batch_execute , @context-mode/ctx_search , etc. Auto-detected via MCP protocol handshake.
Full configs: configs/kiro/mcp.json | configs/kiro/agent.json | configs/kiro/KIRO.md
Zed — MCP-only, no hooks
Prerequisites: Node.js >= 22.5 (or Bun), Zed installed.
Install:
Install context-mode globally:
npm install -g context-mode
Add to ~/.config/zed/settings.json (Windows: %APPDATA%\Zed\settings.json ):
{
"context_servers" : {
"context-mode" : {
"command" : " context-mode " ,
"args" : [],
"env" : {}
}
}
}
Note: Zed uses "context_servers" instead of "mcpServers" . args and env are optional for context-mode, but are shown here to match Zed's custom MCP server shape.
Copy routing instructions (Zed has no hook support):
cp node_modules/context-mode/configs/zed/AGENTS.md ./AGENTS.md
Restart Zed (or save settings.json — Zed auto-restarts context servers on config change).
Verify: Open the Agent Panel ( Cmd+Shift+A ), go to settings, and check the indicator dot next to "context-mode" — green means active. Type ctx stats in the agent chat.
Routing: Manual. The AGENTS.md file is the only enforcement method (~60% compliance). There is no programmatic interception. Tool names appear as mcp:context-mode:ctx_batch_execute , mcp:context-mode:ctx_search , etc. Auto-detected via MCP protocol handshake.
Pi Coding Agent — extension with full hook support
Prerequisites: Node.js >= 22.5 (or Bun), Pi Coding Agent installed.
Install:
Install context-mode globally:
npm install -g context-mode
Install the package into Pi:
pi install npm:context-mode
Alternative — add it manually to ~/.pi/agent/settings.json (or .pi/settings.json for project-level):
{
"packages" : [ " npm:context-mode " ]
}
Add to ~/.pi/agent/mcp.json (or .pi/mcp.json for project-level):
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode "
}
}
}
Restart Pi.
Verify: In a Pi session, type ctx stats . Context-mode tools should appear and respond.
Routing: Automatic. The extension registers all key lifecycle events ( tool_call , tool_result , session_start , session_before_compact ), providing full session continuity and routing enforcement.
OMP (Oh My Pi) — plugin with full hook support
Prerequisites: Node.js >= 22.5 (or Bun), Oh My Pi installed.
Install — plugin path (recommended):
Run the OMP plugin install:
omp plugin install context-mode
Restart OMP.
Verify:
omp plugin list
omp plugin doctor
Both should show context-mode as enabled .
The plugin self-registers its MCP server in ~/.omp/agent/mcp.json on first load (spawned as node <plugin>/server.bundle.mjs , since the plugin-install package directory is not on PATH ), so the 11 ctx_* tools become reachable after the restart in step 2 — no manual mcp.json edit needed ( #677 ). An existing context-mode entry is never overwritten; remove it if you want the plugin to re-register the bundled path.
Install — manual plugin path (if omp plugin install is unavailable):
OMP loads anything listed under ~/.omp/plugins/package.json dependencies whose own package.json carries an omp (or pi ) field. New plugins default to enabled — the lock file at ~/.omp/plugins/omp-plugins.lock.json is only consulted when a plugin needs to be explicitly disabled (loader skips runtimeState && !runtimeState.enabled per extensibility/plugins/loader.ts:89-94 ). So the manual install is two commands:
cd ~ /.omp/plugins
bun add context-mode # or: npm install context-mode
Then restart OMP. No lock file edit, no version pin — version is read from the freshly-installed package each time the loader runs (see loader.ts:87 manifest.version = pluginPkg.version ).
Install — MCP-only path (no plugin):
Install context-mode globally:
npm install -g context-mode
Add to ~/.omp/agent/mcp.json (user scope) or <project>/.omp/mcp.json (project scope):
{
"mcpServers" : {
"context-mode" : {
"command" : " context-mode "
}
}
}
Copy routing instructions:
cp node_modules/context-mode/configs/omp/SYSTEM.md ~ /.omp/agent/SYSTEM.md
Project-scoped alternative: cp ... .omp/SYSTEM.md . OMP also auto-discovers any AGENTS.md in the project tree.
Restart OMP.
Verify (any path): In an OMP session, type ctx stats . Context-mode tools should appear and respond.
Routing: Plugin path — programmatic enforcement via four pi.on(...) handlers ( tool_call returns { block: true, reason } for curl / wget /inline-fetch per upstream hooks/types.ts:566 , tool_result captures session events, session_start initializes the per-session DB row, session_before_compact persists a resume snapshot). ~98% compliance, parity with Claude Code hooks. MCP-only path — rule-based via SYSTEM.md , ~60% compliance. Auto-detected via PI_CODING_AGENT_DIR env var or presence of ~/.omp/ . Storage roots at ~/.omp/context-mode/ so OMP and Pi installs never share session DBs, content indices, or stats files.
Full configs: configs/omp/mcp.json | configs/omp/SYSTEM.md | plugin source: src/adapters/omp/plugin.ts
Build Prerequisites (CentOS, RHEL, Alpine)
Context Mode uses better-sqlite3 on Node.js, which ships prebuilt native binaries for most platforms. On glibc >= 2.31 systems (Ubuntu 20.04+, Debian 11+, Fedora 34+, macOS, Windows), npm install works without any build tools.
Linux + Node.js >= 22.5: Context Mode automatically uses the built-in node:sqlite module instead of better-sqlite3 . This eliminates the native addon entirely, avoiding sporadic SIGSEGV crashes caused by V8's madvise(MADV_DONTNEED) corrupting the addon's .got.plt section on Linux. No configuration needed — detection is automatic. Linux + Node < 22.5 is unsupported ( #564 ) — npm install will fail with remediation instructions.
Bun users: No native compilation needed. Context Mode automatically detects Bun and uses the built-in bun:sqlite module via a compatibility adapter. better-sqlite3 and all its build dependencies are skipped entirely.
On older glibc systems (CentOS 7/8, RHEL 8, Debian 10), prebuilt binaries don't load and better-sqlite3 automatically falls back to compiling from source via prebuild-install || node-gyp rebuild --release . This requires a C++20 compiler (GCC 10+), Make, and Python with setuptools.
Windows / missing binding self-heal: if better_sqlite3.node ends up missing after install (e.g. prebuild-install not on cmd.exe PATH, no MSVC toolchain), the postinstall script and the runtime hook automatically re-fetch the prebuild and repair the binding — no manual npm rebuild needed (#408).
CentOS 8 / RHEL 8 (glibc 2.28):
dnf install -y gcc-toolset-10-gcc gcc-toolset-10-gcc-c++ make python3 python3-setuptools
scl enable gcc-toolset-10 ' npm install -g context-mode '
CentOS 7 / RHEL 7 (glibc 2.17):
yum install -y centos-release-scl
yum install -y devtoolset-10-gcc devtoolset-10-gcc-c++ make python3
pip3 install setuptools
scl enable devtoolset-10 ' npm install -g context-mode '
Alpine Linux:
Alpine prebuilt binaries (musl) are available in better-sqlite3 v12.8.0+. With the ^12.6.2 dependency range, npm install resolves to the latest 12.x and works without build tools on Alpine. If you pin an older version:
apk add build-base python3 py3-setuptools
npm install -g context-mode
Tools
Tool
What it does
Context saved
ctx_batch_execute
Run multiple commands + search multiple queries in ONE call. Opt-in concurrency: 1-8 for I/O-bound batches.
986 KB → 62 KB
ctx_execute
Run code in 12 languages. Only stdout enters context.
56 KB → 299 B
ctx_execute_file
Process files in sandbox. Raw content never leaves.
45 KB → 155 B
ctx_index
Chunk markdown into FTS5 with BM25 ranking.
60 KB → 40 B
ctx_search
Query indexed content with multiple queries in one call.
On-demand retrieval
ctx_fetch_and_index
Fetch URL, chunk and index. Cache reuses content within TTL (default 24h, override per-call with ttl: <ms> ). ttl: 0 or force: true to bypass. Pass requests: [{url, source}, ...] + concurrency: 1-8 for parallel multi-URL.
60 KB → 40 B
ctx_stats
Show context savings, call counts, and session statistics.
—
ctx_doctor
Diagnose installation: runtimes, hooks, FTS5, versions.
—
ctx_upgrade
Upgrade to latest version from GitHub, rebuild, reconfigure hooks.
—
ctx_purge
Permanently deletes all indexed content from the knowledge base.
—
How the Sandbox Works
Each ctx_execute call spawns an isolated subprocess with its own process boundary. Scripts can't access each other's memory or state. The subprocess runs your code, captures stdout, and only that stdout enters the conversation context. The raw data — log files, API responses, snapshots — never leaves the sandbox.
Twelve language runtimes are available: JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, Elixir, and C#. Bun is auto-detected for 3-5x faster JS/TS execution.
Authenticated CLIs work through credential passthrough — gh , aws , gcloud , kubectl , docker inherit environment variables and config paths without exposing them to the conversation.
When output exceeds 5 KB and an intent is provided, Context Mode switches to intent-driven filtering: it indexes the full output into the knowledge base, searches for sections matching your intent, and returns only the relevant matches with a vocabulary of searchable terms for follow-up queries.
How the Knowledge Base Works
The ctx_index tool chunks markdown content by headings while keeping code blocks intact, then stores them in a SQLite FTS5 (Full-Text Search 5) virtual table. The SQLite backend is selected automatically at runtime: bun:sqlite on Bun, node:sqlite on Node.js >= 22.5, and better-sqlite3 everywhere else. Search uses BM25 ranking — a probabilistic relevance algorithm that scores documents based on term frequency, inverse document frequency, and document length normalization. Porter stemming is applied at index time so "running", "runs", and "ran" match the same stem. Titles and headings are weighted 5x in BM25 scoring for precise navigational queries.
When you call ctx_search , it returns relevant content snippets focused around matching query terms — not full documents, not approximations, the actual indexed content with smart extraction around what you're looking for. ctx_fetch_and_index extends this to URLs: fetch, convert HTML to markdown, chunk, index. The raw page never enters context. Use the contentType parameter to filter results by type (e.g. code or prose ).
Ranking: Reciprocal Rank Fusion
Search runs two parallel strategies and merges them with Reciprocal Rank Fusion (RRF) :
Porter stemming — FTS5 MATCH with porter tokenizer. "caching" matches "cached", "caches", "cach".
Trigram substring — FTS5 trigram tokenizer matches partial strings. "useEff" finds "useEffect", "authenticat" finds "authentication".
RRF merges both ranked lists into a single result set, so a document that ranks well in both strategies surfaces higher than one that ranks well in only one. This replaces the old cascading fallback approach where trigram results were only used if porter returned nothing.
Proximity Reranking
Multi-term queries get an additional reranking pass. Results where query terms appear close together are boosted — "session continuity" ranks passages with adjacent terms higher than pages where "session" and "continuity" appear paragraphs apart.
Fuzzy Correction
Levenshtein distance corrects typos before re-searching. "kuberntes" becomes "kubernetes", "autentication" becomes "authentication".
Smart Snippets
Search results use intelligent extraction instead of truncation. Instead of returning the first N characters (which might miss the important part), Context Mode finds where your query terms appear in the content and returns windows around those matches.
TTL Cache
Indexed content persists in a per-project SQLite database at ~/.context-mode/content/ . When ctx_fetch_and_index is called for a URL that was already indexed within its TTL window, the fetch is skipped entirely and the model searches the existing index directly.
Default TTL: 24 hours. Override per-call with ttl: <milliseconds> (PR #666). Longer for stable specs, shorter for changelogs you want re-checked often.
Cache hit (within TTL): Returns a cache hint (~0.3KB) instead of re-fetching (48KB+). Model proceeds to ctx_search .
Cache miss (TTL expired): Re-fetches silently. No user action needed.
ttl: 0 or force: true : Bypasses cache and re-fetches regardless of freshness.
14-day cleanup: Content databases and sources older than 14 days are removed on startup.
This means --continue sessions preserve indexed docs across restarts. No re-fetching, no wasted context tokens.
ctx_stats reports cache performance separately: hits, data avoided, network requests saved, and total context savings including cache.
Progressive Throttling
Calls 1-3: Normal results (2 per query)
Calls 4-8: Reduced results (1 per query) + warning
Calls 9+: Blocked — redirects to ctx_batch_execute
Session Continuity
When the context window fills up, the agent compacts the conversation — dropping older messages to make room. Without session tracking, the model forgets which files it was editing, what tasks are in progress, what errors were resolved, and what you last asked for.
Context Mode captures every meaningful event during your session and persists them in a per-project SQLite database. When the conversation compacts (or you resume with --continue , --resume , or /resume ), your working state is rebuilt automatically — the model continues from your last prompt without asking you to repeat anything.
Resuming a non-latest session via /resume <picker> works the same way: the SessionStart hook detects the empty live-event table for the freshly issued session id and falls back to the most recent unconsumed snapshot for the project ( session_resume table). The picker selects the conversation; context-mode rehydrates the prior working state.
Session continuity requires 5 hooks working together:
Hook
Role
Claude Code
Gemini CLI
VS Code Copilot
JetBrains Copilot
GitHub Copilot CLI
Cursor
OpenCode
KiloCode
OpenClaw
Codex CLI
Antigravity
Antigravity CLI ( agy )
Kiro
Zed
Pi
OMP
PreToolUse
Enforces sandbox routing before tool execution
Yes
--
--
--
Yes
Yes
--
--
--
Yes
--
Bounded
Yes
--
✓ (via tool_call event)
✓ (via tool_call event)
PostToolUse
Captures events after each tool call
Yes
Yes
Yes
Yes
Yes
Yes
Plugin
Plugin
Plugin
Yes
--
Yes (capture-only)
Yes
--
✓ (via tool_result event)
✓ (via tool_result event)
UserPromptSubmit
Captures user decisions and corrections
Yes
--
--
--
Yes
--
Plugin (via chat.message)
Plugin (via chat.message)
--
Yes
--
--
--
--
--
--
Stop
Captures assistant turn-end state
Yes
--
--
--
Yes
Yes
--
--
--
Yes
--
Best-effort
--
--
--
--
PreCompact
Builds snapshot before compaction
Yes
Yes
Yes
Yes
Yes
--
Plugin
Plugin
Plugin
Yes
--
--
--
--
✓ (via session_before_compact)
✓ (via session_before_compact)
SessionStart
Resto
