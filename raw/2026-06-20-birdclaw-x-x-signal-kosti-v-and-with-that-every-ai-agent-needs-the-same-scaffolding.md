---
source: "https://x.com/i/web/status/2068374795729916139"
title: "X signal: @kosti_v - And with that... 𝗔𝗴𝗲𝗻𝘁𝗖𝗼𝗿𝗲 𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗶𝘀 𝗻𝗼𝘄 𝗚𝗔! 🎉 Every AI agent needs the same scaffolding"
author: "@kosti_v"
date_published: "2026-06-20"
date_clipped: "2026-06-20"
category: "AI / LLM Research & Tooling"
source_type: "birdclaw-x"
source_role: "early-signal"
source_id: "2068374795729916139"
birdclaw_id: "2068374795729916139"
like_count: 0
reply_count: 0
repost_count: 0
---

# X signal: @kosti_v - And with that... 𝗔𝗴𝗲𝗻𝘁𝗖𝗼𝗿𝗲 𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗶𝘀 𝗻𝗼𝘄 𝗚𝗔! 🎉 Every AI agent needs the same scaffolding

Source: https://x.com/i/web/status/2068374795729916139
Author: @kosti_v
Published: 2026-06-20
Engagement: 0 likes, 0 reposts, 0 replies

## Captured X Signal

And with that... 𝗔𝗴𝗲𝗻𝘁𝗖𝗼𝗿𝗲 𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗶𝘀 𝗻𝗼𝘄 𝗚𝗔! 🎉

Every AI agent needs the same scaffolding underneath: tools to interact with, an environment to work in, a system to manage context, memory to personalize, identity to control access, and observability to understand and course correct. Wrapped in a loop that calls the model, picks a tool, and recovers from failures. This is the agent harness, and until we launched it in preview, every team using AgentCore built it from scratch.

Today, the managed agent harness in AgentCore is generally available. You declare your agent and run it in two API calls. You point to the model, tools, skills, and instructions as configuration, and AgentCore stitches together everything around it to make the agent production-ready. What you get out of the box:

1️⃣ 𝗔𝗻𝘆 𝗺𝗼𝗱𝗲𝗹, 𝘀𝘄𝗶𝘁𝗰𝗵 𝗺𝗶𝗱-𝘀𝗲𝘀𝘀𝗶𝗼𝗻. Bedrock, OpenAI, Gemini, or any LiteLLM-supported provider. Switch providers mid-session without losing context. Plan on one model, code on another, summarize on a third.

2️⃣ 𝗧𝗼𝗼𝗹𝘀, 𝗱𝗲𝗰𝗹𝗮𝗿𝗮𝘁𝗶𝘃𝗲𝗹𝘆. MCP servers, AgentCore Gateway, built-in Browser and Code Interpreter, or your own inline functions. One config line per tool, with no boilerplate to write.

3️⃣ 𝗕𝘂𝗶𝗹𝘁-𝗶𝗻 𝗺𝗲𝗺𝗼𝗿𝘆, 𝘀𝘁𝗮𝘁𝗲𝗳𝘂𝗹 𝗯𝘆 𝗱𝗲𝗳𝗮𝘂𝗹𝘁. Memory is on out of the box, persisting users and conversations across sessions. Each session also runs in its own secure, isolated microVM with a filesystem and shell.

4️⃣ 𝗦𝗸𝗶𝗹𝗹𝘀 𝗼𝗻 𝗱𝗲𝗺𝗮𝗻𝗱. Compose your agent with bundles of markdown and scripts that give it domain knowledge. Pull from git, S3, your own path, or flip on the full AWS-curated catalog with a single 𝚊𝚠𝚜𝚂𝚔𝚒𝚕𝚕𝚜 toggle. The harness loads and executes them only when the task calls for it.

5️⃣ 𝗥𝘂𝗻 𝗶𝗻 𝘁𝗵𝗲 𝗲𝗻𝘃𝗶𝗿𝗼𝗻𝗺𝗲𝗻𝘁 𝘆𝗼𝘂 𝗻𝗲𝗲𝗱. Use the default image, or bring your own container with your source, runtimes, and dependencies. Persist files with managed session storage, or mount EFS or S3 Files for state that outlives a session.

6️⃣ 𝗢𝗯𝘀𝗲𝗿𝘃𝗲, 𝗲𝘃𝗮𝗹𝘂𝗮𝘁𝗲, 𝗼𝗽𝘁𝗶𝗺𝗶𝘇𝗲. Unified observability gives you one view across every primitive the agent touched. Score real traffic with built-in evaluators, get prompt and tool recommendations, and A/B test them on live traffic before you roll out.

7️⃣ 𝗩𝗲𝗿𝘀𝗶𝗼𝗻, 𝗿𝗼𝗹𝗹 𝗯𝗮𝗰𝗸, 𝗮𝗻𝗱 𝗲𝘅𝗽𝗼𝗿𝘁. Every update is an immutable version, so rollback is pointing an endpoint at an earlier one. And when config stops being enough, export to Strands-based code and keep running on the same compute, same microVM, same observability. No re-architecture, no platform tax.

Trying a new model or tool is a config change, not a code rewrite. Managing context, remembering across users, adding a skill, tuning a prompt: again config, not infrastructure. The whole loop (build, connect, optimize, ship) collapses from weeks into minutes.

Read more in our launch blog: https://t.co/seJp4flUOh

## Related Links

- https://t.co/seJp4flUOh
