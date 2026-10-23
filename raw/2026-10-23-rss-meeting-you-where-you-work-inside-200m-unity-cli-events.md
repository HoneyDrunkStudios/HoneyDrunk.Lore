---
source: "https://unity.com/blog/unity-cli-usage-data-ai-coding-agents"
title: "Meeting you where you work: Inside 200M+ Unity CLI events"
author: "Christopher Addison"
date_published: "2026-10-22"
date_clipped: "2026-10-23"
category: "Game Development / Unity"
source_type: "rss"
---

# Meeting you where you work: Inside 200M+ Unity CLI events

Source: https://unity.com/blog/unity-cli-usage-data-ai-coding-agents

Developers start in the agent they already use, in the editor they already like, with the terminal they already have open. **The [Unity CLI](https://unity.com/blog/meet-the-unity-cli) meets you there**. It’s a single binary that installs and manages Unity from the terminal and, with the Pipeline package, drives a running Editor, so scripts, CI, and coding agents all reach Unity the same way.

Since July, more than **226,000** logged-in users have used the Unity CLI, and it has logged more than **200 million events** (and growing)**.** Almost all of them are commands being run. What those commands show is a simple habit: people set Unity up, then their agent does the work.

## People set it up, then hand it off

From July 20 to October 13, 2026, about 98% of CLI runs come from coding agents and other automation. People typing at a terminal account for 0.2%, and CI pipelines for 0.3%. A small share of runs falls outside those three groups.  
When people do type, they are getting ready. They install the Pipeline package, open a project on the right Editor version, sign in, point their agent at Unity, and install the CLI skill. Then they hand the work over. That is what meeting developers where they work looks like in practice: Unity shows up inside the agent they already chose, and the agent takes it from there.

## Most of the work happens inside a live Editor

The three commands run most:

1. **`unity command`** about **124 million runs**: runs a command on a connected Editor, either a built-in one or one you defined yourself.
2. **`unity status`** about **6.7 million**: shows the live state of every connected Editor, including its project and version.
3. **`unity pipeline list`** about **1.4 million**: lists Editor instances and whether each one has the Pipeline package.

## Unity’s plugins bring official skills to agents

Most of the CLI's usage came after Unity released official plugins for [**Claude Code**](https://unity.com/blog/unity-plugin-for-claude-code) and [**Codex**](https://unity.com/blog/unity-plugin-codex), and most recently, [**Grok**](https://unity.com/blog/unity-plugin-grok). Each plugin gives the agent skills written by Unity's own teams, including one that drives the CLI, so the agent works in Unity the way Unity intends. **`unity setup claude`** installs the Claude Code plugin for you, and the plugin also works in the Claude Code extension for VS Code. Agents that are not integrated with Unity’s official plugin can still work in Unity through the CLI, so you keep the agent you already use.

Claude Code is the agent used most with the CLI, followed by Codex, then other agents such as Cursor and Grok. The rest come from scripts and tools that do not identify an agent.

## Where it is being used

By signed-in users, the CLI's largest audiences are in the **United States, Japan, South Korea**, followed by **Germany** and **Turkey**.

## What’s next

We will keep adding agents, and keep publishing what we learn. To get started, see the [Unity CLI documentation](https://docs.unity.com/en-us/unity-cli) and the [Unity plugin documentation](https://docs.unity.com/en-us/ai/unity-plugin/about-unity-plugin).

#### How we measured this

All CLI figures come from aggregated Unity CLI telemetry, July 20 to October 13, 2026. Agent usage by user covers September 1 to October 13, 2026, with each user counted once. Unity employees are excluded, and users who opt out of telemetry are not counted. Each event is counted once, so retries do not inflate totals. Country is based on the location attached to each event, and some events have no location. A run counts as CI when a CI environment variable is set, and as a person when both input and output are a terminal. Runs in MCP mode, runs from a known AI tool, and other piped or scripted runs count as agents and automation. Command counts are based on the command name recorded with each event.
