---
"source": "https://www.solo.io/blog/announcing-kagent-1-0-ga"
"title": "Agent Substrate in Production: Announcing kagent 1.0"
"author": "Christian Posta"
"date_published": "2026-11-10"
"date_clipped": "2026-11-17"
"category": "DevOps & CI/CD"
"source_type": "rss"
---

# Agent Substrate in Production: Announcing kagent 1.0

We are super excited to announce v1.0 of kagent, an enterprise-ready distribution of [Agent Substrate](https://ate.dev) for running AI agents and Sandboxes on any distribution of Kubernetes (including OpenShift). The project has evolved quite a bit since our [original announcement almost two years ago](https://thenewstack.io/meet-kagent-open-source-framework-for-ai-agents-in-kubernetes/) as we've worked with users to design, build, deploy, and operate AI agents in production.

Originally, we focused on "platform / DevOps" style agents built with frameworks like [CrewAI](https://crewai.com/), [LangChain](https://www.langchain.com/), [ADK](https://adk.dev/), etc configured with a fixed set of tools. We ran agents as a Kubernetes Deployment (Pod replicas), the same way you'd run a microservice, and for that kind of simple agent it worked fine, but that's not what most people are building now. The first pattern we see is the agent [harness](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), a general-purpose loop around a model that gets a goal, a workspace, and some skills/tools/CLIs, and works out the steps on its own (what Anthropic calls [agents rather than workflows](https://www.anthropic.com/research/building-effective-agents)). Those agents run code a model wrote, keep a workspace around between turns, and spend a lot of their time waiting on a model, tools, or a human.

The other pattern we see is the "tool sandbox". A lot of agent work doesn't need a long-running home at all, it needs somewhere safe to run a tool call (run this script, check this code, transform these files, etc) and hand back the result. [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) is a good example, where Anthropic runs the agent loop and the agent's tool calls can run in sandboxes on your own infrastructure (which kagent supports).

[Agent Substrate](https://ate.dev) was built for both of these. [Solo.io](https://solo.io) has spent most of this year designing and building it alongside Google. Substrate is a layer on top of Kubernetes that treats agent-style workloads as "actors" that have their own sandbox, state, and durable identity, and it schedules them onto a pool of warm worker Pods that Kubernetes runs. Agent Substrate just reached 1.0 and is now a [CNCF project](https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf/). Substrate focuses on execution, and kagent 1.0 is the layer on top that knows about your users, conversations, agents, and sandboxes. It's open source (a [CNCF project](https://www.solo.io/blog/bringing-agentic-ai-to-kubernetes-contributing-kagent-to-cncf)), and Solo.io is also shipping enterprise releases of both projects (more on that below).

Solo.io already has customers (and open source users) running kagent 1.0 on Agent Substrate in production at scale. We think it's ready for general availability. Let's start with why a Pod per agent doesn't work.

## Why Not Pods for Agents?

A Pod comes with assumptions that work great for microservices. It runs code you wrote and reviewed, its replicas are stateless and interchangeable, it stays busy, and every replica shares one identity (the ServiceAccount). An AI agent breaks these assumptions.

First, the AI model decides what runs. Ask an agent to "fix this doc" and there's a good chance it writes a sed command or a short Python script to do it, which nobody reviewed and which does whatever the model's context (an issue, a README, a tool response, etc) pushed it toward. This is dangerous. Each session needs a real sandbox with egress controls and [safe credential handling](https://agentgateway.dev/blog/2026-11-02-protecting-token-vault-openbao-credential-injection/). A tool sandbox is the same, since its code is untrusted by definition.

Second, state accumulates within the agent's workspace. An agent could clone a repo, install packages, and edit files, so its environment *is* the work, and a restart, eviction, or node drain throws it away. Third, the agent mostly waits on a model, a person, or another agent, and its Pod holds CPU and memory the whole time, so millions of sessions means a fleet of Pods doing mostly nothing. Tool sandboxes have the opposite problem, where a Pod (or Job) per tool call can spend more time getting reconciled through the Kubernetes API server and scheduler than actually running.

![A grid of 200 squares where six are working and the rest are idle Pods waiting for their next message, next to a list of what a waiting Pod still holds (memory, schedulable capacity on a node, an IP address)](https://cdn.prod.website-files.com/6704482c45ef6ead081645ff/6af20ad1b470f68f7861e111_8e66a812.png)

*Ten thousand sessions, each in its own Pod, and only a few hundred working at any moment.*

Fourth, an agent session acts for a specific user, and one shared ServiceAccount can't tell those sessions apart for policy or audit. Once you start suspending sessions and moving them between Pods to fix the idle problem, an identity tied to the Pod can't follow them either. (I went deeper on this in [Agent Identity and Access Management: can SPIFFE work?](https://www.solo.io/blog/agent-identity-and-access-management---can-spiffe-work).)

## How does Agent Substrate fix this?

Agent Substrate addresses these broken assumptions with a layer on top of Kubernetes purpose built for these workloads. Substrate keeps the worker (a warm Pod in a WorkerPool that Kubernetes runs and scales) separate from the actor(s) running on it. When an actor goes idle, Substrate snapshots its workspace (and optionally its entire memory) and gives the worker back. When a request shows up for an actor that's been paused, Substrate's router finds a free worker and restores the actor into it. If no worker is free yet, the router holds the request for a moment instead of failing it. None of this goes through the Kubernetes API server, which is why it's cheap enough to do on every turn or every tool call.

![An actor suspends off Worker A into an actor snapshot (memory and files) that holds no compute, then resumes on Worker B with the same state when atenet-router sends it the next request](https://cdn.prod.website-files.com/6704482c45ef6ead081645ff/6af20ad1b470f68f7861e114_5bcc79bc.png)

*An idle actor gives its worker back and resumes on whichever eligible worker has room.*

The other half of the story is security. Every actor runs in its own [gVisor](https://gvisor.dev) or microVM sandbox (Substrate doesn't support plain containers). Each actor also gets its own identity (based on [SPIFFE](https://spiffe.io)), which follows the actor from worker to worker instead of belonging to the Pod. Requests coming in hit the ingress router, which authenticates the caller and checks policy before it wakes the actor up. Everything going out goes through the egress gateway, and the sandbox *holds no credentials*. In both directions, the gateways run on [agentgateway](https://agentgateway.dev) which understands LLM, MCP, and A2A traffic, so a policy can say which models, MCP tools, or other agents an actor can call. When the agent calls an API, the egress gateway checks the request against the actor's policy and [injects the API key or token](https://github.com/agent-substrate/substrate/blob/v1.0.0/docs/guides/egress-credential-injection.md) on the way out, so a prompt-injected agent has nothing to steal. Anything the policy doesn't allow is denied.

![Two actors in gVisor sandboxes on one Worker Pod, and a third in a Cloud Hypervisor microVM on another, each treated as untrusted](https://cdn.prod.website-files.com/6704482c45ef6ead081645ff/6af20ad1b470f68f7861e11e_b8103b91.png)

*Every actor gets its own sandbox, even when it shares a worker with other actors*

*.*

![The actor sends a request with a placeholder Authorization header, agentgateway checks its EgressPolicy, fetches the real token from a credential provider like OpenBao using the actor's JWT, and forwards the request upstream](https://cdn.prod.website-files.com/6704482c45ef6ead081645ff/6af20ad1b470f68f7861e124_c90f92a9.png)

*The actor only ever holds a placeholder, and agentgateway swaps in the real token on the way out.*

Kubernetes still does what it's good at here (running and scaling the worker Pods), and everything you already know about operating a cluster still applies. Substrate handles the part that changes too often for the Kubernetes control plane to keep up with. To get an idea of how many agents across how many workers, [checkout this Substrate calculator](https://kagent.dev/substrate-calculator). Agent Substrate is 1.0, it's a CNCF project, and it's what we built kagent 1.0 on.

## What does kagent add on top of Substrate?

Substrate is deliberately low level. Its own README calls it ["a low-opinion runtime, not an agent SDK"](https://github.com/agent-substrate/substrate/blob/v1.0.0/README.md), and it's very good at the things it knows about (actors, workers, snapshots, egress policy, etc). What it doesn't know is what an actor is *for*. It has no concept of a user, a conversation, or an agent, so it can't tell an agent waiting on its user from one halfway through a tool call, and it doesn't know who's allowed to talk to which agent or who owns a sandbox. kagent is the layer we built to answer those questions, and it's how we think you should run Agent Substrate in production. kagent decides what an agent does, and Agent Substrate decides where it runs.

![kagent as the agent platform layer (sessions, credential injection, revisions, suspend, the A2A gateway) on top of Agent Substrate (actors, workers, snapshots, sandboxes, identity, egress) on top of Kubernetes (nodes, worker Pods, networking, storage, autoscaling)](https://cdn.prod.website-files.com/6704482c45ef6ead081645ff/6af20ad1b470f68f7861e121_270921e0.png)

*kagent on top of Agent Substrate, with Kubernetes underneath.*

- **Bring your own harness.** Run kagent's own agent runtime, Claude, Codex, or any container that speaks kagent's A2A contract, all with the same lifecycle, access controls, and sandboxing.
- **Declarative agents.** Define an agent from a model (OpenAI, Anthropic, Gemini, Vertex AI, Azure, Bedrock, Ollama, etc), a prompt, MCP tools, skills, and plugins, and reuse that definition across agents and harnesses.
- **Safe rollouts.** Change a prompt or a model and new conversations pick it up, while the ones already in flight stay on the version they started with.
- **Auto-suspend.** Every conversation suspends when its turn ends and resumes on whatever worker is free when the next message comes in, so an idle conversation holds no compute.
- **Human-in-the-loop.** An agent can stop and ask a person for approval, suspend at exactly that point, and pick up the same operation when they answer (and a webhook can tell your system it's waiting).
- **History, checkpoints, and forks.** Conversation history is readable without waking a sandbox, you can checkpoint a conversation and fork a new one from it to try something different, and idle conversations clean themselves up (after seven days by default).
- **Users, ownership, and sharing.** People sign in through your OIDC provider, every conversation belongs to whoever started it, they can share it with others, and kagent checks all of that before a request reaches an agent.
- **No credentials in the agent.** Model API keys and MCP credentials are injected by the egress gateway, rotate without restarting anything, and everything else is denied unless an EgressPolicy allows it.
- **Sandboxes on demand.** People and agents can grab a short-lived sandbox to run a script or process some files, and kagent can also be the [self-hosted sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) for Claude Managed Agents (experimental for now).
- **Use it from anywhere.** Agents are reachable over A2A and MCP, kagent has its own MCP server for sessions, checkpoints, and sandboxes, and there's a UI (with a view into Substrate), a CLI, and OpenTelemetry traces, metrics, and token usage across harnesses.

Most of that list maps straight back to the assumptions that broke for Pods. Auto-suspend and human-in-the-loop are how an agent that mostly waits stops costing you a Pod, sandboxes and gateway-held credentials are how you run code nobody reviewed, checkpoints and forks treat the agent's state as the work it is, and ownership plus a per-actor identity is how policy and audit know which user an agent is acting for.

## Who's running this in production?

[OutSystems](https://www.outsystems.com) runs a large multi-tenant platform, which is exactly the Pod-per-agent problem at scale. They use kagent and agentgateway for the APIs, lifecycle management, and gateway controls to plug agents into that platform.

"With the number of agents we expect to support, running a dedicated, always-on pod for every agent simply isn't possible. Agent Substrate gives us sandboxed runtimes that suspend when idle and resume on demand." (Ebenezer Schubert, VP Engineering, OutSystems)

[Swissquote](https://www.swissquote.com) runs a sovereign AI stack, with full control over its inference, infrastructure, and AI lifecycle, and Solo's enterprise releases of kagent and Agent Substrate give them infrastructure-level isolation and security along with the low latency their most sensitive agents need.

"Our Codename Diego financial-crime investigation agents and MCP servers are already running in production on kagent GA. In a multi-jurisdictional regulated environment, security, resilience and explainability are non-negotiable." (Andrew Boswell, Head Information Technology, Swissquote)

Solo's [enterprise releases of Agent Substrate and kagent](https://www.solo.io/products/kagent) are generally available today, with agentgateway as the actor's gateway on both ingress and egress. They add what production teams ask for on top of the open source projects. That covers granular access control over agent resources, agent tracing and evaluations built from real execution traces, visibility into Substrate fleet capacity and failures, and air-gapped installs, along with support from the people building both projects.

## See it in action

![__wf_reserved_inherit](https://cdn.prod.website-files.com/6704482c45ef6ead081645ff/6af2142a4a710f529f551fdc_image3.gif)



This is the kagent UI on a cluster running Agent Substrate. A new conversation starts an actor, and once the turn is done, the Substrate view shows that session (and every other one) suspended and holding no compute until the next message comes in (note the ‘Actors Running: 0/20).

## Getting started

You need a Kubernetes cluster, helm, and a model provider key (OpenAI is the default). Install the CLI and run kagent install, which sets up Agent Substrate, PostgreSQL, and kagent in one step.

curl -sL https://raw.githubusercontent.com/kagent-dev/kagent/refs/heads/main/scripts/get-kagent **|** bash -s -- --version v1.0.0  
export OPENAI\_API\_KEY=<your key>  
kagent install

From there, [your first agent](https://kagent.dev/docs/kagent/1.x/get-started/your-first-agent) walks you through defining an agent and talking to it, and the [docs](https://kagent.dev/docs/kagent/1.x) cover installing with the Helm charts directly (e.g. for GitOps). To size things before you go further, the [Agent Substrate calculator](https://kagent.dev/substrate-calculator) estimates wake-up times and the CPU, memory, and storage your agents need, based on our performance and scale testing for GA. If you're running kagent 0.x today, 1.0 is a new API on a new runtime, so plan on a fresh install.

## Get involved

kagent and Agent Substrate are both open source CNCF projects, and both are moving fast. If you're running agents on Kubernetes (or trying to), give it a try and tell us where it breaks, what your agents need that it doesn't do yet, and what you'd want from the layer above Substrate.

- Explore kagent on [GitHub](https://github.com/kagent-dev/kagent) and at [kagent.dev](https://kagent.dev), and join the [Discord](https://discord.gg/Fu3k65f2k3) and the weekly [community meeting](https://kagent.dev/community).
- Explore Agent Substrate on [GitHub](https://github.com/agent-substrate/substrate) and at [ate.dev](https://ate.dev), and find its Helm charts in [kagent-dev/substrate](https://github.com/kagent-dev/substrate).
- At KubeCon in Salt Lake City, come to my talk [Pods Are Not Enough for AI Agents, Meet Agent Substrate](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/program/schedule/?id=1250532) on November 11, and stop by the Solo.io booth to see kagent and Agent Substrate running and talk with the people who build them.
- For the deeper version, read [*Agent Substrate: From Pods to Sandboxes*](https://www.solo.io/resources/report/agent-substrate-from-pods-to-sandboxes-full-2026-edition), and the earlier posts on [kagent and Agent Substrate](https://kagent.dev/blog/kagent-agent-substrate-sandboxes) and [agent sandboxes](https://kagent.dev/blog/agent-sandboxes-four-axes).
