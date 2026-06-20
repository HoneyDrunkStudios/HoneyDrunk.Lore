---
source: "https://vercel.com/blog/introducing-eve"
title: "Introducing eve"
author: "Vercel"
date_published: "2026-06-18"
date_clipped: "2026-06-20"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Introducing eve

Source: https://vercel.com/blog/introducing-eve

Today, we are proud to introduce eve , an open-source agent framework for building, running, and scaling agents. eve is designed around the idea that building an agent should mean defining what it does without assembling all of the pieces that it needs to run in production. Instead, eve comes with production already built in:
Durable execution
Sandboxed compute 
Human-in-the-loop approvals
Subagents
Evals
And more
eve is the framework that we build and run our own agents on.
Agents today are where the web was before frameworks, with everyone hand-rolling the same plumbing and nothing carrying over to the next one. Next.js ended this for the web, and eve is doing the same for agents.
Link to heading An agent is a directory This is an eve agent.
agent/ agent.ts # the model it runs on instructions.md # who it is tools/ run_sql.ts # what it can do post_chart.ts skills/ revenue-definitions.md # what it knows subagents/ investigator/ # who it delegates to channels/ slack.ts # where it lives schedules/ monday-summary.ts # when it acts on its own A data analyst agent, readable at a glance
Each file describes one component of the agent, so at a glance, the tree tells you what an agent is, what it does, where it lives, and when it acts on its own.
Link to heading Create an eve agent in minutes Every agent starts with its definition.
agent/agent.ts 1 import { defineAgent } from "eve" ; 2 
3 export default defineAgent ( { 4 model : "anthropic/claude-opus-4.8" , 5 } ) ; Configuring the agent and its model in one file
The agent.ts file is where you configure the agent itself. You can define the model with one line, with provider fallbacks supported through AI Gateway , and compaction, model options, and other optional fields are there when you need them.
Giving your agent a job and personality is as simple as creating an instructions.md file, which serves as the system prompt that eve puts in front of every model call.
agent/instructions.md You are a senior data analyst. You answer questions about the team's data. 
- Prefer exact numbers to hand-waving. If you can compute it, compute it. - State the assumptions behind any number you report (date range, filters, grain). - Use the tools available to you rather than guessing. If you cannot answer from the data, say so plainly. The agent's identity and standing rules, prepended to every model call
You create files for what your agent does, like post_chart.ts and revenue-definitions.md for tools and skills, and eve wires them into a working agent without any boilerplate or plumbing to manage. You can just focus on what your agent does instead of how it does it.
Link to heading Why we built eve We had built agents for years at Vercel, v0 among them. But once coding agents made building one something anyone could do, everyone did. We shipped hundreds of agents and internal apps, and it looked like a productivity revolution.
But underneath it, every team was building and rebuilding the same plumbing before their agent could do anything, and none of it carried over from one use case to the next. Each agent was designed for a different task, but they all had the same needs, and the same structure kept emerging to meet them. Agents have a shape.
eve is that shape made into a framework. Every generation of software earns its abstractions once enough people have built the same thing the hard way, and agents are there now.
Link to heading Batteries included Everything an agent needs in production ships with the framework.
Link to heading A durable session for every conversation Agents wait on people, call slow systems, and run for hours, days, or weeks. In eve, every conversation is a durable workflow with each step checkpointed, so a session can pause, survive a crash or a deploy, and resume exactly where it stopped. This durability is built on the open-source Workflow SDK .
Link to heading A sandbox for every agent The code your agents write should be treated as untrusted, so eve keeps agent-generated code out of your application runtime entirely. Every agent gets its own sandbox, an isolated environment for shell commands, scripts, and file reads and writes, running in a separate security context from the harness that controls the agent. The backend behind this sandbox is an adapter. When deployed, it runs on Vercel Sandbox . Locally, it runs on Docker, microsandbox, or just-bash , and you can write an adapter for any other provider.
Link to heading Human-in-the-loop approvals Agents act on real systems, and some of those actions should require a person to approve them. Any action in eve can be configured to require approval, and the agent will pause there and wait, indefinitely if it has to, without consuming any compute. Once approved, eve continues the task right from where it left off.
Link to heading Secure connections to tools, data, and services Agents need to connect to your backends, data, and other third-party services. In eve, a connection is a file that points at an MCP server or any API with a compatible OpenAPI document.
agent/connections/linear.ts 1 import { defineMcpClientConnection } from "eve/connections" ; 2 
3 export default defineMcpClientConnection ( { 4 url : "https://mcp.linear.app/sse" , 5 description : "Linear workspace: issues, projects, cycles, and comments." , 6 auth : { 7 getToken : async ( ) => ( { token : process . env . LINEAR_API_TOKEN ! } ) , 8 } , 9 } ) ; A connection to an MCP server, in one file
eve discovers the remote tools, hands them to the model, and brokers the auth, and the model never sees the connection's URL or credentials. Vercel Connect handles interactive OAuth with consent and token refresh built in. At launch, eve agents can connect to Slack, GitHub, Snowflake, Salesforce, Notion, and Linear, plus anything else you can reach over OAuth, an API key, or an MCP server.
Connect to the tools you already use. Link to heading The same agent on every channel Most agents live in exactly one place because every new surface is its own integration to build. In eve, the same agent serves every surface, and each channel is just a small adapter file. The HTTP API is on by default, with Slack, Discord, Teams, Telegram, Twilio, GitHub, and Linear included, and defineChannel covers custom channels. One channel can also hand off to another, so an incident webhook can open an investigation thread in Slack.
Link to heading Tracing and evals built in When an agent gets something wrong, the first question is what the agent actually did. In eve, every run produces a trace. Each model call and tool call appears in order with its inputs and outputs, down to the commands the agent ran in its sandbox, so you can replay the run instead of piecing it together from logs.
ai.eve.turn # one span per turn ├── ai.streamText # the model call │ └── ai.streamText.doStream └── ai.toolCall # run_sql, with inputs and outputs The OpenTelemetry span tree a single turn produces
The spans are standard OpenTelemetry and export to any tracing service you already run, whether that is Braintrust, Honeycomb, Datadog, or Jaeger. On Vercel, they surface in an Agent Runs tab under Observability, giving you one place to watch every session and drill into any run. Evals let you go further, with scored test suites you can run locally or wire into CI.
Exactly what the agent did, one turn at a time That leaves the part no framework can write for you: what your agent actually does.
Link to heading Extend an agent one file at a time The most common way to give an agent capabilities is to give it tools, and to teach it how to do things with skills. Today that means building the tool, writing the skill, and then wiring both into whatever runs your agent loop. With eve, a tool is one TypeScript file and a skill is one markdown file.
agent/tools/run_sql.ts 1 import { defineTool } from "eve/tools" ; 2 import { z } from "zod" ; 3 import { runReadOnlySql } from "../lib/sample-db" ; 4 
5 export default defineTool ( { 6 description : "Run a read-only SQL query against the orders and customers tables." , 7 inputSchema : z . object ( { 8 sql : z . string ( ) . describe ( "A single read-only SELECT statement." ) , 9 } ) , 10 async execute ( { sql } ) { 11 const { columns , rows } = await runReadOnlySql ( sql ) ; 12 return { columns , rows : rows . slice ( 0 , 500 ) , truncated : rows . length > 500 } ; 13 } , 14 } ) ; A typed tool in one file, where the filename becomes the tool name
agent/skills/revenue-definitions.md --- description : How this team defines revenue. Load before answering any revenue question. --- 
Revenue is recognized net of refunds, over the subscription term. Weeks are Monday-anchored, in UTC. Exclude trial and internal accounts from every number. A skill in one markdown file, loaded only when the topic comes up
Notice what is missing. Instead of writing all of the boilerplate to wire these up and register them with your agent, eve handles it for you.
A file's name and place in the tree are its definition. eve picks up the tool and skill at build time, hands the model their descriptions, and the model takes it from there. Just as Next.js turns a folder into a route by owning the routing, eve turns a file into an ability by owning the agent loop.
Link to heading Add human-in-the-loop approval Requiring approval for an action is one field on the tool.
agent/tools/run_sql.ts 1 export default defineTool ( { 2 description : "Run a read-only SQL query against the warehouse." , 3 inputSchema : z . object ( { sql : z . string ( ) } ) , 4 needsApproval : ( { toolInput } ) => estimateScanGb ( toolInput . sql ) > 50 , 5 async execute ( { sql } ) { 6 // unchanged 7 } , 8 } ) ; Requiring approval when a query would scan more than 50GB
Now you can guard the expensive query, the destructive write, or anything else you would not want running unsupervised.
Link to heading Let the agent write its own code The tools you define aren't the ceiling. eve gives your agent a real computer with a shell, so it can run bash, grep, and anything else you'd run in a terminal. When a job calls for code that doesn't exist yet, the agent writes and runs it.
> Break last week's revenue down by region and chart it 
⦿ write_file analysis/by_region.py ⦿ bash python analysis/by_region.py 
Revenue by region for the week of June 1. AMER $2.1M, EMEA $1.6M, APAC $0.5M. Chart saved to analysis/by_region.png. The agent writing and running its own code in its own sandbox
Your agent can solve problems on its own in a secure sandbox, reshaping a dataset, running a one-off analysis, or writing whatever code a job needs that no tool covers.
Link to heading Delegate work to a subagent An eve agent can also delegate. A subagent is the same shape one level down, a directory inside subagents/ with its own instructions, tools, and sandbox. The parent calls it just like it calls a tool.
agent/subagents/investigator/agent.ts 1 import { defineAgent } from "eve" ; 2 
3 export default defineAgent ( { 4 description : "Investigates anomalies in the data before the analyst reports them." , 5 model : "anthropic/claude-opus-4.8" , 6 } ) ; A subagent the analyst can hand work to
The child starts with a clean context window and only the tools you gave it, does the work, and hands the result back to the parent.
Link to heading Start and interact with your agent Now comes the part every developer looks forward to, testing their agent. That used to mean starting the process, asking a question, and reading logs, with no simple view of which tools were used, what the model loaded, or why it answered the way it did. You wanted to talk to your agent and watch it work, and what you got was stdout . With eve, the dev loop is one command.
Link to heading Run the agent locally To start an eve agent, you run its dev server.
eve dev Starting the agent locally, with a terminal UI to talk to it
> What was revenue last week? 
⦿ load_skill revenue-definitions ⦿ run_sql SELECT date_trunc('week', created_at) ... 
Revenue for the week of June 1 was $4.2M net of refunds, up 6% from the prior week. Every step of the run, visible as it happens
Everything the agent did is visible in the TUI. The agent loaded the skill, ran the query, answered by the team's rules, and each of those lines is a checkpointed step in the durable session. The terminal UI is just a client, and the agent serves the same structured events over HTTP, so curl , a test script, or CI can drive it and check exactly what it did.
Link to heading Test the agent with evals Talking to the agent proves one run at a time. Evals test your agent the way you test the rest of your software, with scored checks written in files like everything else in the project.
evals/revenue.eval.ts 1 import { defineEval } from "eve/evals" ; 2 import { includes } from "eve/evals/expect" ; 3 
4 export default defineEval ( { 5 description : "The analyst answers revenue questions by the team's rules." , 6 async test ( t ) { 7 await t . send ( "What was revenue last week?" ) ; 8 t . completed ( ) ; 9 t . calledTool ( "run_sql" ) ; 10 t . check ( t . reply , includes ( "net of refunds" ) ) ; 11 } , 12 } ) ; A suite that checks whether the analyst used its tool and followed the team's definitions
You can run eve eval locally or point it at a deployed app, so a prompt change or a model swap shows you what it broke before your users do.
Link to heading Ship it The agent has lived on your laptop long enough. Shipping it is normally the step where the agent work stops and the infrastructure work begins. With eve there is nothing to provision, because the agent is an ordinary Vercel project, and it deploys the way any other frontend or backend does.
vercel deploy Deploying the agent
Nothing about your agent changes when you deploy, because eve was designed from the ground up with adapters in mind. At launch eve deploys to Vercel, with support for other platforms on the way. The same directory runs in production exactly as it ran on your laptop. The sandbox swaps to Vercel Sandbox without a code change, and the agent you were talking to in dev is now reachable at a public URL. Deploying does not even interrupt the agent; a session that is mid-task when you push finishes on the version it started on.
There is no dashboard step required in any of this. The same coding agent that built your agent can ship it and verify its work.
But deployed is not the same as done. In production, an agent has users to meet and work to do on its own schedule.
Link to heading Introduce the agent to your team Getting an agent into Slack used to mean building a Slack app first, including the app config, bot token, event subscriptions, webhook endpoint, and signing secret, all before the agent said a word. With eve, a channel is one command.
eve channels add slack Scaffolding the Slack channel file
The command writes channels/slack.ts , a single file that ships like any other code change, and the agent you just deployed now answers in Slack. The platform affordances come with the channel, so approvals render as Slack buttons, questions as select menus, and the agent posts typing indicators while it works. Route the credentials through Vercel Connect and there is no bot token to copy into a .env file. Run the command again with discord or teams , and the same agent is there too, one file per channel.
Channels are the user interface of your agents, and sessions move between them. A question asked in Slack can continue on the web, and an incident webhook arriving over HTTP can open an investigation thread in Slack and finish the work where the team already is.
Link to heading Put the agent on a schedule The Monday revenue report should not wait for someone to ask. A schedule is one more file, a cron expression and a handler that starts the agent on its own clock.
agent/schedules/monday-summary.ts 1 import { defineSchedule } from "eve/schedules" ; 2 import slack from "../channels/slack.js" ; 3 
4 export default defineSchedule ( { 5 cron : "0 9 * * 1" , 6 async run ( { receive , waitUntil , appAuth } ) { 7 waitUntil ( 8 receive ( slack , { 9 message : "Summarize last week's revenue and post it to the team channel." , 10 target : { channelId : "C0123ABC" } , 11 auth : appAuth , 12 } ) , 13 ) ; 14 } , 15 } ) ; Posting the Monday revenue report through the Slack channel, on a cron
On Vercel, each schedule deploys as a Vercel Cron Job , so the report posts every Monday with nobody on the hook to remember it.
Link to heading Run the agent like the rest of your software An agent your team depends on is production software, and a change to its instructions can break it as surely as a change to its code. Because an eve agent is files in a directory, it lives in Git like the rest of your code, and a new prompt, tool, or skill is a commit with a diff, a review, and a history.
Wire eve eval into CI and the suites you wrote become the deploy gate, scoring every commit so a regression stops in CI rather than in production.
Every commit also gets its own preview deployment, and it carries the agent's channels with it. The team can talk to the next version of your Slack bot before it replaces the one they use every day.
And when a change goes bad in a way no eval caught, you can roll production back to the previous version instantly.
Link to heading How we run Vercel on eve We run more than a hundred agents in production at Vercel, and they are part of how the company operates every day, each one taking on a role in the business. Here are a few of them.
Link to heading The data analyst The most-used internal tool at Vercel is an agent, handling more than 30,000 questions a month. Anyone can ask d0 anything in Slack and get an answer from the warehouse. Every query is scoped to the asker's own permissions, so d0 can never show you a table you could not already see.
Link to heading The autonomous SDR Lead Agent runs the playbook of our best rep around the clock. It works every new lead the moment it comes in and follows up on its own, so none go cold overnight. It costs about $5,000 a year to run, returns 32 times that, and one engineer maintains it part-time.
Link to heading The sales cockpit RevOps built Athena in six weeks without engineers. It answers pipeline and forecast questions from Snowflake and Salesforce in plain language, and pipeline coverage nearly doubled after it went live.
Link to heading The support engineer Vertex is our support agent that handles tickets across the help center, docs, and Slack around the clock, ensuring people get a fast response no matter when they ask. It reads the ticket, finds the right answer, and responds, solving 92% of tickets on its own and escalating the rest to the support team so they can focus on the problems that most need their attention.
Link to heading The content agent Anyone at Vercel can write, not just the content team. draft0 runs a full review pipeline, catching the most glaring issues and building up an analysis of what the piece is actually about before it ever reaches us. By the time it does, the obvious work is done and we have a much clearer picture of what it needs. That means smaller pieces move fast, and we can give our full attention to the ones that demand it, like this one.
Link to heading Routing agent We rely on hundreds of agents every day, but keeping track of which one handles what workloads is not efficient. So instead of routing tasks ourselves, everything goes to V in Slack first. V figures out which agent can actually answer the task and routes it there, which means the whole fleet works like one agent instead of a hundred different options.
These agents all began as separate projects on separate stacks, each with its own way of holding state, brokering credentials, and emitting logs, which is where most teams find themselves after their second or third agent. Today they live in one monorepo, and are built, observed, and upgraded the same way, no matter which team owns them. Because they all share the same shape, a hundred agents run with the same tools and the same conventions as one.
Link to heading Get started A year ago, agents triggered less than 3% of the deployments on Vercel. Now, they trigger around 29%, and we expect half of all deployments to come from agents soon. You have probably built an agent already, and the next one does not have to start from scratch.
The public preview is open today, and the CLI wizard walks you through your first agent, from picking a model to a running dev server, in under a minute.
npx eve@latest init my-agent Your first eve agent
Coding agents just need a prompt:
Set up an Eve agent for the user. Eve is a filesystem-first TypeScript framework for durable agents, published as the npm package eve. Read its docs: once eve is installed they are bundled in the package at node_modules/eve/docs; before eve is installed, read the published Introduction and Getting Started pages. If the project has no Eve app, scaffold one with `npx eve@latest init <name>` ; add `--channel-web-nextjs` only when the user wants Web Chat. The init command installs dependencies, initializes Git, and starts the dev server, so run it in a controllable process and stop it before editing. To add Eve to an existing app, run `npm install eve@latest` . Make sure agent/agent.ts and agent/instructions.md exist, then add a first typed tool at agent/tools/get_weather.ts using defineTool from eve/tools with a Zod inputSchema and an inline execute. Start the dev server again, then exercise the HTTP API: create a session with POST /eve/v1/session, attach to GET /eve/v1/session/:id/stream, and send a follow-up with the returned continuationToken. Verify with the project's typecheck, adapt model and provider choices to the project, and do not commit unless the user asks. A starting prompt for your coding agent
Everything eve can do is at eve.dev/docs and development happens in the open at github.com/vercel/eve , where issues, discussions, and contributions are welcome.
Hundreds of agents already run on eve at Vercel. What will you build?
Build your first agent 
An agent is a directory of files, and eve runs it with durable execution, a sandbox, approvals, and evals built in. Works with any model, any MCP server, and channels like Slack, Discord, and GitHub.
Get started
