---
source: "https://github.blog/changelog/2026-06-02-expanded-technical-preview-availability-for-the-github-copilot-app/"
title: "Expanded technical preview availability for the GitHub Copilot app"
author: "GitHub"
date_published: "2026-06-02"
date_clipped: "2026-06-08"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Expanded technical preview availability for the GitHub Copilot app

Source: https://github.blog/changelog/2026-06-02-expanded-technical-preview-availability-for-the-github-copilot-app/

# Expanded technical preview availability for the GitHub Copilot app

*Editor’s note (June 5, 2026): Removed the waitlist link and updated the links to the GitHub Copilot app.*

The GitHub Copilot app technical preview is now available to all existing Copilot Pro, Pro+, Business, and Enterprise customers. [Download the Copilot app](https://github.com/features/ai/github-app?utm_source=changelog-github-copilot-app&utm_medium=changelog&utm_campaign=github-copilot-app-ms-build-2026) for Windows, macOS, or Linux to get started.

Access for Copilot Free users and new subscribers will be opening soon. Existing Pro+ customers can upgrade to the new Copilot Max plan for greater included usage.

This release is also where the app’s center of gravity shifts. As agents do more per session, the work that falls to you changes into managing their output: reading chat transcripts, hunting for the diff that matters, and repeating yourself to course-correct. The headline addition in this release, canvases, is our answer to that shift. Canvases give agent work a place to take shape, become visible, and get verified. All this happens alongside the chat where you steer it.

[A quick recap](https://github.blog#a-quick-recap)

The Copilot app is the desktop home for agent-native software development on GitHub. In one app you can:

- Start a session from an issue, pull request, prompt, or prior session, across all your connected repositories from a single My work view.
- Run parallel agent sessions, each on its own git worktree and branch, with isolated files, conversation, and task state.
- Start from any local folder, not just a git repository, and use it as context for new agent sessions, prototypes, explorations, or workflows.
- Review the plan and diff, then validate behavior in an integrated terminal and browser.
- Open a pull request that uses your team’s existing reviews, checks, and merge requirements, and let Agent Merge address review comments, fix failing checks, and merge when your conditions are met.
- Choose the model behind each session, connect external tools via MCP servers, and package recurring work as reusable skills and scheduled automations.

[What’s new in this release](https://github.blog#whats-new-in-this-release)

[🎨 Canvases](https://github.blog#%f0%9f%8e%a8-canvases)

Canvases are bidirectional work surfaces for humans and agents. The agent updates the canvas as it works, and you can edit, reorder, approve, or redirect work directly on that same surface.

This is the beginning of agent experience (AX) in the Copilot app: interfaces designed not only for people to use, but for people and agents to operate together. The agent session remains where you instruct, discuss, and reason through ambiguity. Canvases are where that intent becomes visible work you can inspect, steer, and verify.

A canvas is a structured, interactive surface over a work object. That work object might be a plan, pull request, browser session, terminal, release checklist, migration board, incident, spreadsheet, dashboard, cloud console, or workflow state. The canvas does not replace the conversation. It gives the conversation somewhere to land.

Three participants share a canvas:

**Users**inspect state, steer direction, make edits, and verify progress.**Agents**read canvas state, take structured actions, update the surface, and use it as evidence of completion.**The app**connects the canvas to the underlying artifact or runtime and enforces what actions are allowed.

That loop makes agentic work more grounded, more steerable, more inspectable, and more continuous. Progress is no longer buried in a transcript. It is visible as changes to the work object itself.

[More in this release](https://github.blog#more-in-this-release)

**Voice conversations:**Talk to Copilot using on-device speech-to-text, so no audio leaves your machine. This is the same approach we shipped in Copilot CLI.**Cloud sessions:**Run an agent session in the cloud directly from the app, the same capability behind`copilot --cloud`

, now in the app UI.**Cloud automations:**Schedule an automation to run in the cloud, so recurring work doesn’t depend on your machine being awake.**Copilot CLI sessions in the app:**Sessions started in Copilot CLI now appear in your My work view, so both surfaces share one source of truth.**Agentic browsing:**The agent can now drive the integrated browser (e.g., click, type, take screenshots) to verify its own UI changes end to end.**Rubber duck:**A built-in skill that talks through a problem with you before you commit to an approach. Useful for the moments when the issue is your thinking, not your code.Query data from any of your Copilot agent sessions, including ones you started outside the app. Useful when you need something from a session that isn’t in front of you.`/chronicle`

:

[Get started today](https://github.blog#get-started-today)

[Download the Copilot app](https://github.com/features/ai/github-app?utm_source=changelog-github-copilot-app&utm_medium=changelog&utm_campaign=github-copilot-app-ms-build-2026) to start your first agent session.

[Read the docs](https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started?utm_source=changelog-github-copilot-app-docs&utm_medium=changelog&utm_campaign=msbuild-2026) to get started quickly.

Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/197303?utm_source=changelog-github-copilot-app-docs&utm_medium=changelog&utm_campaign=msbuild-2026).
