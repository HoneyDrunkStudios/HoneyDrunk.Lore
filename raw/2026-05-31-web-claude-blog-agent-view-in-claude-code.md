---
source: "https://claude.com/blog/agent-view-in-claude-code"
title: "Agent view in Claude Code"
author: "unknown"
date_published: "2026-05-11"
date_clipped: "2026-05-31"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Agent view in Claude Code

Source: https://claude.com/blog/agent-view-in-claude-code

Agent view in Claude Code Category Product announcements Product Claude Code Date May 11, 2026 Reading time 5 min Share Copy link https://claude.com/blog/agent-view-in-claude-code Today we're introducing agent view in Claude Code: one place to manage all your Claude Code sessions. 
When running agents in parallel before, you've probably had to manage multiple terminal tabs, a tmux grid, and an overloaded mental ledger of what you need to tackle next.
With agent view in Claude Code, you can kick off new agents, send them to the background, and jump in only when Claude needs you. See at a glance which agents are waiting on you, which are still working, and which are done, so you can easily steer many all at once.
How it works Agent view improves visualizing and interacting with your Claude Code sessions in the CLI.
See everything at once Press the left arrow from any session or run claude agents from the terminal to open agent view. Each row shows the session, whether it needs your input, the contents of its last response, and when you last interacted with it.
Peek and reply without leaving Select a session to peek at the last turn. If a session is waiting on a decision, answer inline and the session picks back up. Press enter to attach directly to sessions where you want to explore the full transcript.
Background anything Lastly, users can take any existing session and add it to agent view using /bg or skip the foreground entirely using claude --bg [task] to launch a fresh session.
How developers are using agent view A few patterns we have seen from early users:
Scaling the number of concurrent sessions: Dispatch several ideas at once, each optionally paired with a skill, and return to a list of pull requests ready for review. Manage long running agents: PR babysitters, dashboard updaters, and other looping jobs show their next run time right in the list. Navigate between separate sessions: When you’re in the middle of a session, press the left arrow, start a related task or quick codebase question, then arrow right back into what you were doing. Peek shows the answer when it lands. See what shipped: Status indicators on each row plus the title in peek make it easy to scan which sessions produced a PR. Getting started Agent view is available today as a Research Preview on Pro, Max, Team, Enterprise, and Claude API plans. Opt-in by running claude agents . Usual rate limits apply. See the docs for more information.
No items found. Prev Prev 0 / 5 Next Next eBook FAQ
No items found. Get Claude Code Desktop VS Code JetBrains On the web Slack 
curl -fsSL https://claude.ai/install.sh | bash Copy command to clipboard irm https://claude.ai/install.ps1 | iex Copy command to clipboard Or read the documentation Try Claude Code Try Claude Code Try Claude Code Developer docs Developer docs Developer docs Related posts Explore more product news and best practices for teams building with Claude.
May 28, 2026 Introducing dynamic workflows in Claude Code Product announcements Introducing dynamic workflows in Claude Code Introducing dynamic workflows in Claude Code Introducing dynamic workflows in Claude Code Introducing dynamic workflows in Claude Code May 26, 2026 Code w/ Claude London 2026: Rethinking how we build Product announcements Code w/ Claude London 2026: Rethinking how we build Code w/ Claude London 2026: Rethinking how we build Code w/ Claude London 2026: Rethinking how we build Code w/ Claude London 2026: Rethinking how we build May 19, 2026 New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels Product announcements New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels May 12, 2026 Code w/ Claude SF 2026 recap: Building on the AI exponential Product announcements Code w/ Claude SF 2026 recap: Building on the AI exponential Code w/ Claude SF 2026 recap: Building on the AI exponential Code w/ Claude SF 2026 recap: Building on the AI exponential Code w/ Claude SF 2026 recap: Building on the AI exponential Transform how your organization operates with Claude See pricing See pricing See pricing Contact sales Contact sales Contact sales Get the developer newsletter
Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.
Subscribe Subscribe Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
Thank you! You’re subscribed. Sorry, there was a problem with your submission, please try again later.
