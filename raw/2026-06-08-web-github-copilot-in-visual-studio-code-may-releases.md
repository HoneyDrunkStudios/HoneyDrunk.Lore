---
source: "https://github.blog/changelog/2026-06-03-github-copilot-in-visual-studio-code-may-releases/"
title: "GitHub Copilot in Visual Studio Code, May releases"
author: "GitHub"
date_published: "2026-06-03"
date_clipped: "2026-06-08"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# GitHub Copilot in Visual Studio Code, May releases

Source: https://github.blog/changelog/2026-06-03-github-copilot-in-visual-studio-code-may-releases/

# GitHub Copilot in Visual Studio Code, May releases

VS Code continues with weekly stable releases. This changelog covers releases [v1.120 through v1.123](https://aka.ms/VSCode/Release), the releases we shipped throughout May and early June 2026.

In May, we made the Agents window available in VS Code Stable as a preview, giving users an agent-first experience focused on completing tasks rather than editing code. We also improved support for remotely controlling longer-running, more complex agent sessions.

VS Code supports bring-your-own-key (BYOK) models, letting you use your own language model API keys. This month, we expanded BYOK to air-gapped environments and added controls to specify which models handle utility tasks like commit message generation.

[Agents window](https://github.blog#agents-window)

**Agents window in Stable (preview)**: Work agent-first across multiple projects with a dedicated surface for faster navigation and change review.**Remote agents (preview)**: Run sessions on remote machines over SSH or Dev Tunnels, with sessions continuing even when the client disconnects.**Agent Host Protocol (AHP)**: Continued investment in an open protocol for synchronizing agent session state across multiple clients.**Session preferences persist in new sessions**: New sessions keep your recent choices, including agent harness and isolation mode.**Sessions and Git flow improvements**: New sessions can pull base branch updates before the agent starts edits, the Agents window refreshes Git state automatically after commits, syncs, and related operations, and agents can trigger tasks on remote machines.**Session sync**: Chat sessions now sync automatically to your GitHub account, giving you a searchable history of your work across machines and workspaces.**Chronicle**: Use`/chronicle`

commands to query past sessions, generate standup reports, and get personalized productivity tips.**Multiple sessions side-by-side**: Open more than one agent session at the same time in the Agents window. Drag, Alt-click, or use Open to the Side to compare or review work in parallel.**Retry network-dependent commands in sandbox**: Terminal commands that require network access are automatically retried with broader network permissions, while keeping filesystem protections in place.

[Language models and BYOK](https://github.blog#language-models-and-byok)

**Air-gapped BYOK**: Bring-your-own-key models can run in isolated environments without GitHub authentication.**Custom Endpoint provider**: Add endpoints compatible with chat completions, responses, or messages from one provider flow.**Model picker by provider**: Find and switch models more easily in multi-provider environments.**BYOK token visibility**: The context window now reports real token usage for bring-your-own-key models.**Reasoning effort controls**: Configure thinking effort directly from the model picker to balance quality, latency, and cost.**Configurable utility models**: Choose which models handle titles, summaries, rename suggestions, commit messages, and intent detection.

[Terminal safety and efficiency](https://github.blog#terminal-safety-and-efficiency)

**Expanded terminal output compression**: More verbose output patterns from tests, builds, linters, Docker, and package managers are compressed before reaching the model to optimize token usage and help reduce costs.**Command risk assessment (experimental)**: Terminal confirmations include AI-generated risk levels and short safety explanations.**Sensitive prompts stay in terminal**: Passwords, passphrases, PINs, and verification codes are entered directly in the terminal and are not shared with the LLM.**Better background command UX**: There are now clearer running-state indicators in chat, plus automatic cleanup of completed background agent terminals to help save resources on your machine and keep things more manageable.**Agent-aware terminal commands**: The`VSCODE_AGENT`

environment variable lets CLIs adapt behavior for agent-initiated commands.

[Also new](https://github.blog#also-new)

**Integrated browser**: Adds device emulation to test your website’s responsiveness. New screenshot options let you capture the viewport, a selected area, or the full page and attach any of them as chat context to help reproduce and explain UI issues. You can also save favorite pages for quick access alongside open tabs.**HTML file preview**: Preview local HTML files directly in the integrated browser without installing an extension. Right-click a file in the Explorer or editor tab and select Open in Integrated Browser.**Search only in changed files**: There’s a new search panel toggle that can scope results to locally modified, uncommitted files.**Markdown preview improvements**: Mermaid diagram rendering and YAML front matter display are now built in, without requiring separate extensions. You can also view Markdown diffs as rendered preview instead of raw source when opening files from Source Control.**Quick suggestions default tuning**: Experience reduced noise when inline completions are available.**Issue reporter wizard**: New issue filing flow with support for screenshots and video recordings.**Accessibility and UX updates**: Ongoing improvements across editor surfaces.

Happy coding!

Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).
