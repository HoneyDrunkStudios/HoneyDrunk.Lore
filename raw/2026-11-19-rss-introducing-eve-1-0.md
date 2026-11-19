---
source: "https://vercel.com/blog/eve-is-now-generally-available"
title: "Introducing eve 1.0"
author: "Andrew Barba, Shar Dara, Casey Gowrie, Colton Padden, Rui Conti, Ben Pankow, Owen Kephart, Murat Sutunc, Chad Hietala"
date_published: "2026-11-17"
date_clipped: "2026-11-19"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Introducing eve 1.0

Source: https://vercel.com/blog/eve-is-now-generally-available

Today we're announcing [eve 1.0](https://eve.dev), the open-source framework for building production-ready agents.

Since the [public preview in June](https://vercel.com/blog/introducing-eve), we've worked with early adopters to prepare eve for 1.0, shipping 230+ releases and merging thousands of pull requests. With this release, eve is now generally available.

We've made eve faster, expanded integrations, and improved observability. Security controls let you decide which actions need approval and what data gets collected. We've also made it easier for coding agents to build with, measuring that experience with a rigorous evaluation suite.

With eve handling your harness and infrastructure, you and your agent can focus on building instead.

## Build production agents on a harness you own

The harness in eve is the loop that calls models, runs tools, and delegates work to subagents. You choose the model, add or replace tools, edit instructions, and decide which actions need approval. The open-source [Workflow SDK](https://workflow-sdk.dev/) saves progress as the agent runs, so it can pick up from its last completed step after a crash. Multiplayer sessions and agent-to-agent calls are built in.

For managed hosting, deploy your eve agent to Vercel. [Vercel Workflows](https://vercel.com/workflows) handles durable execution, and [Vercel Sandbox](https://vercel.com/sandbox) runs agent-generated code in isolation.

Build software factories that turn requests into tested pull requests, company brains that answer questions from your business data, or customer-facing agents in your product.

Company brains, software factories, and agentic apps

Thousands of businesses already run eve in production for internal and customer-facing agents. [Rillet](https://vercel.com/customers/how-rillet-ships-3-faster-with-ai-agents-on-vercel) built a software factory on eve that takes in customer requests, converts them into specs, tests the changes, and opens PRs for human review. Rillet tripled its shipping rate in three months. [Clay](https://www.clay.com/blog/building-everyones-personal-data-scientist) built monty, a data agent that answers employees’ questions in Slack. Just over two months in, 30–40% of the company used it every week.

[Lindy](https://www.lindy.ai/blog/ai-agent-frameworks)'s agent framework roundup names eve “Best for durable backend agents”.

> “Custom agents built with eve plus Vercel workflows. I’m biased but I didn’t mandate this, we felt it was the best solution for us.”
>
> [![](https://assets.vercel.com/image/upload/f_auto,c_fill,w_32,h_32,q_75/contentful/image/e5382hct74si/7kOxyecg0uEAMgrec2u7CI/0033f10ec062eafd9441cbbaefbae053/mitchell.jpg)Mitchell Hashimoto↗(opens in new tab)](https://x.com/mitchellh/status/2120237599214506235)

## Collaborate in multiplayer agent sessions

Multiplayer lets several people work with an agent in one shared session. eve keeps track of who said what and directs approvals and sign-ins to the right person. You can set up memory for each user or the whole team.

A shared Slack session with individual approvals

In the native [Slack channel](https://eve.dev/docs/channels/slack), each thread is one shared session. Approvals appear as buttons that only the right person can answer, and a live task card shows progress and timing. You can follow up in the thread without mentioning the agent again, cancel the current turn, or reset the session from Slack.

[Ambient mode](https://eve.dev/docs/patterns/ambient-listening) lets an agent listen in channels you choose, even without being mentioned. Guided by goals you set per channel, it decides when to speak up, help, or take on a task, and when to stay quiet. To limit model costs, a small decision model screens every message first, and only the ones that might be for the agent start a turn.

Slack is one of several native channels, alongside Microsoft Teams, Discord, Telegram, GitHub, Linear, Twilio, Web Chat, and iMessage. The [Chat SDK channel](https://eve.dev/docs/channels/chat-sdk) adds support for any Chat SDK platform adapter, including WhatsApp, Messenger, Google Chat, and email. Each channel is one file, and the same agent can work across all of them. See the [integrations directory](https://eve.dev/integrations?filter=channel) for the full list.

## Build agent UIs with Next.js and other frameworks

eve 1.0 expands our native integrations for Next.js, Nuxt, SvelteKit, TanStack Start, and Vite. The [framework integrations](https://eve.dev/docs/guides/frontend) build your agent alongside your app and set up its routes. On Vercel, you can deploy the agent and your site as one project, or host them separately.

Native integrations for your web framework

The client libraries let you work with tool calls, approval requests, and questions in a consistent way across frameworks. Use that session data to build custom UIs: stream replies into agent chats, embed an agent in a page, or show the agent's tool calls in your own components.

Use `eve add channel/web` to scaffold a chat app with [AI Elements](https://elements.ai-sdk.dev/) components, or add eve's React, Vue, or Svelte bindings to an existing UI.

## Build multi-tenant agents

One support-agent deployment can connect to each customer's ticketing system with their own credentials and apply that customer's approval rules.

Your application authenticates the user and identifies which tenant they belong to. You can then set [memory](https://eve.dev/docs/patterns/multi-tenant-memory), [connection credentials](https://eve.dev/docs/patterns/multi-tenant-auth), and [approval policy](https://eve.dev/docs/patterns/multi-tenant-approvals) for that tenant and user.

Before each model call in the main agent loop, [dynamic definitions](https://eve.dev/docs/guides/dynamic-capabilities) load the agent's capabilities from the session and external data. In 1.0, they cover models, connections, and subagents as well as tools, skills, and instructions.

## Give agents memory across sessions

We added native [memory](https://eve.dev/docs/memory) so agents can carry context from one session to the next. You choose the memory's scope and can use the built-in file memory, a memory provider, or [one you build yourself](https://eve.dev/docs/memory/custom-provider).

Built-in `fileMemory` keeps data in memory in `eve dev` and in a [private Vercel Blob store](https://vercel.com/docs/vercel-blob/private-storage) you configure on Vercel.

Other providers include [claude-mem](https://eve.dev/integrations/claude-mem), [Hindsight](https://eve.dev/integrations/hindsight), [Kybernesis Arcana](https://eve.dev/integrations/arcana), [Memanto](https://eve.dev/integrations/memanto), [memco](https://eve.dev/integrations/memco), [Supermemory](https://eve.dev/integrations/supermemory), and [Upstash AgentKit](https://eve.dev/integrations/upstash-agentkit).

## Trace agents with OpenTelemetry

We rebuilt eve’s tracing around [OpenTelemetry](https://eve.dev/docs/observability/otel), so you can follow an agent’s work in the tracing tools you already use. `eve dev` records traces locally by default. If you host eve yourself, you can export them to an OpenTelemetry backend, including one you run yourself.

Tracing integrations include [Raindrop](https://eve.dev/integrations/raindrop), with more options in the [integrations directory](https://eve.dev/integrations). Add one with `eve add instrumentation/<name>`, or use the [instrumentation APIs](https://eve.dev/docs/observability/instrumentation) to build your own integration.

Traces now show when an agent is waiting for a person, including tool approvals, questions, budget prompts, and sign-ins. They record model selections and approval decisions alongside model usage and cost, and follow calls into MCP servers and remote agents.

You choose what eve collects for tracing. Content you exclude from collection stays out of every destination. You can filter out spans or redact inputs and outputs per destination. Private conversations in production send only metadata by default, without prompts or tool results. The [OpenTelemetry guide](https://eve.dev/docs/observability/otel) explains these controls.

On Vercel, [Agent Runs](https://vercel.com/changelog/agent-runs-vercel-mcp-cli) uses the same traces to show sessions, model calls, tool execution, subagent activity, and approval decisions in the dashboard. When `eve deploy` creates a new Vercel project, it sets up trace sampling automatically. See the [Agent Runs guide](https://eve.dev/docs/observability/agent-runs) for setup and configuration.

Model calls, tools, and costs in Agent Runs

## Lower agent turn latency

At the start of September, our hosted stress test on Vercel Workflows took a median of **3.036s per turn**. In 1.0, the same 100-turn workload took **414ms**. The [test](https://github.com/vercel/eve/blob/1db579adeaa9b150ebf2fc97f8d5b437be9806e6/e2e/fixtures/agent-workflow-stress/evals/sequential-workflow-turns.eval.ts) sends messages one at a time, with one immediate mock-model response and no tool calls per turn. We measure from sending a message until the turn finishes, capturing eve and Workflow overhead without the time a model takes to generate a response.

Median turn latency, 7.3× faster in eve 1.0

Beta3.04s

1.0414ms

Median turn latency fell from 3.04s to 626ms in the mock-model test.

| **Hosted stress run** | **Median turn latency** | **p95** |
| --- | --- | --- |
| [September 1, beta baseline](https://github.com/vercel/eve/blob/fd33944eec/research/turn-performance.md#hosted-experiment-ledger) | 3.036s | 3.692s |
| [November 15, 1.0.0](https://github.com/vercel/eve/actions/runs/43766191789) | 414ms | 633ms |

We worked with the Workflow team on [spec 9](https://workflow-sdk.dev/docs/changelog/spec-9), which gives each run a single orchestrator so background steps no longer replay the workflow. The team also moved event and stream writes to WebSockets and cut redundant history reads. eve agents get these improvements through Workflow SDK.

eve also caches the information it needs to route messages to each session and can move idle sessions to a newer deployment between turns. Web UIs can [prewarm a session](https://eve.dev/docs/guides/frontend/use-eve-agent#prewarming) before the first message arrives, so the first reply starts sooner.

## Lower workflow costs for long agent sessions

For a 50-turn Evo Docs session, the estimated Vercel Workflows cost drops from 5.4¢ to 1.3¢, about 76% lower. That assumes roughly two model steps per turn and 30-day retention. eve now uses Workflow SDK 5.5 and saves only the conversation data that changed between turns. We've also cut repeated work in workflow steps, checkpoints, and sandbox setup:

- Workflow steps save changes and refer back to data already stored, instead of repeatedly copying a growing conversation into each step. Steps that don't need history no longer receive it.
- Checkpoints store references to image files returned by tools, so they don't have to copy the image bytes each time.
- Sandboxes from [prepared snapshots](https://vercel.com/docs/sandbox/concepts/snapshots) skip repeated setup. Stop a sandbox and keep its files for reuse. Cleanup starts when the session ends.

The storage changes are part of the open-source Workflow SDK, so agents you host yourself on other Workflow backends also store less duplicate session data. The cost estimate above uses [Vercel Workflows pricing](https://vercel.com/docs/workflows/pricing).

On Vercel, workflow steps run on [Fluid compute](https://vercel.com/docs/fluid-compute). They need extra storage writes for inputs above the payload size limit, so sending less session data helps keep turn times consistent as sessions grow. Images and files can still require those writes.

For model calls, tool and skill listings can stay out of the initial prompt until they're needed. Connection tools run through `eve__search` and `eve__tool`, so each search no longer has to expand the model's tool list. We also changed how eve marks parts of a prompt for provider caching, so more content can be reused between calls.

During an earlier migration to eve, an engineer at Evisions reported:

> “Transitioning to Eve delivered immediate, high impact results. To name a few, we were able to cut out 25k lines of code, cut our AI costs in half, and improved runtime by 66%.”
>
> ![](https://assets.vercel.com/image/upload/f_auto,c_fill,w_32,h_32,q_75/contentful/image/e5382hct74si/6zGADxPJXVFKlIKHN1TQtq/82836bbf344f5452a1b5aef9bde8b2f8/chris.jpg)Chris Fleissner

## Share agent capabilities with extensions

Since the preview, we've added [extensions](https://eve.dev/docs/extensions) so teams can share tools, skills, instructions, connections, channels, schedules, hooks, and subagents without copying files between agents. You can use extensions from the [extensions directory](https://eve.dev/integrations?filter=extension) or create your own with `npx eve@latest extension init <name>`.

For example, [agent-browser](https://eve.dev/integrations/agent-browser) adds browser automation, [Mux Video](https://eve.dev/integrations/mux-video) adds tools for video assets and clips, and [Link](https://eve.dev/integrations/link) adds wallet and purchase tools.

eve builds workspace extensions from source and reloads changes during development. You can update shared capabilities in one package and try the changes in your agents as you work.

## Build coding agents with eve’s shared tools

The 1.0 [code extension](https://eve.dev/docs/code-extension) builds on eve’s default file tools, adding coding instructions and skills that follow your repository’s `AGENTS.md`. It's included in the `eve` package, so there's nothing extra to install. Give it a repository in its sandbox and your agent can investigate code, edit files, and run the project's checks. It uses the same harness and extension system as your other agents, so you can replace or disable tools, override skills, and add your own instructions.

See the [benchmark results](https://eve.dev/docs/code-extension#benchmark-results) for comparisons with other coding harnesses using the same tasks and model.

Add the coding extension to your agent:

terminal.sh

```
eve add extension/code
```

Add the coding extension to an eve agent

The companion `eve/extensions/git` adds GitHub and pull request workflows, using credentials and authorization you configure. On Vercel, the optional remote self-modification extension lets your agent propose changes to its own source in a draft pull request. You review the changes, merge them, and deploy.

## Build with the same public APIs eve uses

We built eve's subagents, sleep, and question tools on the same workflow system you can use through [`defineWorkflowTool`](https://eve.dev/docs/tools/workflows). Your tools can return a result, start a background task, or keep accepting messages as a resumable task. They can wait for a person, webhook, or timer without keeping compute running, and their runs survive restarts. You don't need a separate background-job system to coordinate that work.

Once you've defined a `reviewer` subagent, this tool returns a receipt immediately. The `task` body waits for the reviewer's result, which is delivered to the model in a later message:

agent/tools/review.ts

```
import { defineWorkflowTool } from "eve/tools";

import { z } from "zod";

export default defineWorkflowTool({

description: "Ask the reviewer to check these notes.",

inputSchema: z.object({ notes: z.string() }),

async task({ notes }, ctx) {

"use workflow";

const response = await ctx.agent("reviewer").send(notes, {

signal: ctx.abortSignal,

});

return await response.result();

},

});
```

Delegate a review to a subagent

> “Been stress-testing crash recovery in @eve, and it's really solid: approvals and finished steps come back cleanly after a restart.”
>
> ![](https://assets.vercel.com/image/upload/f_auto,c_fill,w_32,h_32,q_75/contentful/image/e5382hct74si/2d0aMVFBB7NQepM7UlMrBA/ea88b179291d435fd33db6099e5af31a/george.jpg)George Shostakovych

## Upgrade to eve 1.0

If you already have an eve agent, the [1.0 upgrade guide](https://eve.dev/docs/guides/upgrade) walks through the changes to extension builds, agent APIs, session events, clients, and saved history. Follow it before deploying your upgrade.

eve follows [semantic versioning](https://eve.dev/docs/reference/typescript-api#stability-policy), so breaking changes to stable APIs only happen in major releases. Experimental and internal APIs, including experimental fields, can change between major releases.

To work through the upgrade with your coding agent, copy this prompt:

Prompt for coding agents

Read https://eve.dev/docs/guides/upgrade and inspect this project's eve version and configuration. Upgrade it to eve 1.0, following the guide's order and the sections that apply. Update extensions, agent code, event consumers, clients, and saved history where needed. Run the project's typecheck, eve build, and relevant tests. Summarize the changes and any remaining manual migration or
deployment steps.

Upgrade an existing project with your coding agent

## Create your first eve agent

Start in the terminal to build locally, use the browser builder to create and deploy an agent, or choose a template for your use case.

### Start in the terminal

Create a new agent from the CLI with Node.js 24 or newer:

terminal.sh

```
npx eve@latest init my-agent
```

Create a new eve agent

In an interactive terminal, this installs dependencies and opens the eve terminal UI. If your selected team has [AI Gateway](https://vercel.com/docs/ai-gateway) access, you can start chatting without creating a Vercel project or copying an API key. eve can use your existing [Vercel CLI credentials](https://vercel.com/docs/cli/login) to call models through AI Gateway locally. Use `/login` to sign in to other connections.

In `eve dev`, you can ask the agent to add a tool, change its instructions, or write a skill. With [self-modification](https://eve.dev/docs/guides/self-modification), it edits its own source and reloads the change for the next turn.

### Start in the browser

From the Vercel dashboard, the [agent builder](https://vercel.com/changelog/build-and-deploy-eve-agents-from-the-vercel-dashboard) scaffolds an agent, creates its Git repo, and deploys it. Go to Add New → Agent, pick a model, and add web chat or Slack along the way.

### Start from a template

Choose an [eve template](https://vercel.com/templates/eve) for your use case:

| **Use case** | **Templates** |
| --- | --- |
| Coding | [Coding agent](https://vercel.com/templates/eve/eve-coding-agent-template) · [Software factory](https://vercel.com/templates/eve/eve-software-factory) · [GitHub maintainer](https://vercel.com/templates/eve/eve-github-maintainer) · [Incident response](https://vercel.com/templates/eve/eve-incident-response-agent) |
| Knowledge and data | [Company brain](https://vercel.com/templates/eve/eve-company-brain-template) · [Data analyst](https://vercel.com/templates/eve/eve-data-analyst) · [Shared files with Vercel Drives](https://vercel.com/templates/eve/eve-vercel-drives-starter) |
| Apps and interfaces | [Next.js chat](https://vercel.com/templates/eve/eve-chat-template) · [TanStack Start chat](https://vercel.com/templates/eve/eve-tanstack-agent) · [Voice agent](https://vercel.com/templates/eve/eve-voice-template) · [Agent with Python](https://vercel.com/templates/eve/eve-agent-with-python) |
| Messaging | [Slack](https://vercel.com/templates/eve/eve-slack-agent) · [Discord](https://vercel.com/templates/eve/eve-discord-agent) · [Personal agent](https://vercel.com/templates/nuxt/eve-personal-agent) · [BELL Stack](https://vercel.com/templates/eve/bell-stack) |
| Memory | [Memory agent](https://vercel.com/templates/eve/eve-memory-agent) · [Mem0](https://vercel.com/templates/eve/eve-mem0-agent) |
| Content and marketing | [Contentful](https://vercel.com/templates/eve/eve-contentful-agent) · [Sanity copilot](https://vercel.com/templates/eve/eve-sanity-copilot) · [Content agent](https://vercel.com/templates/eve/eve-content-agent) · [Marketing team](https://vercel.com/templates/eve/eve-marketing-team) |

Learn more in the [eve docs](https://eve.dev).
