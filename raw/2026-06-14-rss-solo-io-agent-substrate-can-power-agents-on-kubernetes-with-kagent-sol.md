---
source: "https://www.solo.io/blog/agent-substrate-powers-kubernetes-agents-with-kagent"
title: "Agent substrate can power agents on Kubernetes with kagent | Solo.io"
author: "Solo.io"
date_published: "2026-06-12"
date_clipped: "2026-06-14"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Agent substrate can power agents on Kubernetes with kagent | Solo.io

Source: https://www.solo.io/blog/agent-substrate-powers-kubernetes-agents-with-kagent

About a month ago, we [announced support for NemoClaw on kagent](https://www.solo.io/blog/kagent-nemoclaw) and pointed out a number of challenges for running Agents on Kubernetes including:

“Agents are long-lived, bursty, and idle most of the time. We need lighter-weight isolation primitives: Firecracker microVMs, gVisor, Kata Containers and real lifecycle support: suspend, snapshot, resume, scale-to-zero with state preserved. “

We are happy to share updates to solving these challenges. We have been working with the community on the [Agent Substrate](https://github.com/agent-substrate/substrate/) project as a foundational piece for running “sandboxed” AI agents in kagent on Kubernetes. We are contributing support for running any kind of AI agent in [kagent](https://kagent.dev/) which uses Agent Substrate under the covers.

## Why Agent Substrate?

Kubernetes is a great workload and orchestration engine. It can run all kinds of workloads. But scaling to zero, very fast workload boot times (milliseconds), equally fast tear down, idle workloads, single-tenant sandboxing, etc is not the sweet spot for Kubernetes.

Within Solo.io, for our enterprise kagent offering, we built a custom solution to solve these problems. We built a solution using Bubblewrap/Landlock/seccomp with an option to use Firecracker microVMs and a control plane that ran adjacent to the Kubernetes control plane. Our solution allowed us to pack many agent instances/actors into a single pod/VM/container and provide strict tenant sandboxing. Additionally, we could scale out across many pods and clusters. Or VMs if we wanted. Or other container orchestrators.

Our custom solution locks down all traffic and routes egress through the [AAIF agentgateway project](https://aaif.io/projects/agentgateway/) which can provide sophisticated controls/security/governance for LLM/MCP/Agent communication. We can scale agents to zero, snapshot them to storage, and resume them very fast: 50ms for the Bubblewrap solution or 200ms for Firecracker.

We were about to opensource this technology. Right as we were, we caught wind that a team at Google was working on a similar solution called Agent Substrate. Not similar insofar that it was “another sandbox project”, but rather that it was very close to what we already built. The overlap and architecture were so similar, we decided it was best to bring our experience and work on this with Google.

So what is Agent Substrate built to solve?

- Better utilization of pods – agent-per-pod models where agents sit idle waste compute resources; Agent Substrate can suspend idle agents and swap in agents ready to work
- Avoid Kubernetes API in deployment hot path – Kubernetes API server is not built to handle millions of resources / writes / updates; agent-substrate leverages the Kubernetes API for what is good for and brings a separate but complementary control layer that is better suited for the deploy/suspend/resume workflow of AI agents
- Pods can take seconds to startup – Kubernetes relies on an eventually consistent model that converges on a working pod. This is typically on the order of seconds; Agents need much faster; Agent Substrate reduces this to milliseconds
- State management is difficult – Kubernetes is not designed for millions of volumes being attached/detached; Agent Substrate can snapshot entire agents to storage (ie, GCS, S3, etc) and resume quickly


## How does it work?

At a high level, Agent Substrate schedules/suspends actors (agents) into workers (Pods). You pre-provision a set of Pods (could be configured with autoscaling) to act as generic workers. You configure this in a WorkerPool resource.

AgentSubstrate deploys actors (i.e., AI agents) into the workers. You define actors with an ActorTemplate resource and AgentSubstrate spins up actors from that template.


The actual running actors are managed by the Agent Substrate control plane. Agent Substrate uses a networking layer to route requests from a client to an actor running in a worker. If the actor does not exist, it boots it up (very quickly) and services the request. When the agent becomes idle, it gets snapshotted into storage and scheduled out of the worker.


## How does kagent use Agent Substrate?

Kagent supports running your own agents (Langchain, CrewAI, ADK, etc). declarative agents (no-code with Agent custom resource), and agent harnesses such as OpenClaw / Hermes. Typically these would be deployed to Pods and run as “long-running” services. But with Agent Substrate, we can now deploy these agents into Agent Substrate, taking advantage of the routing, snapshotting, and quick suspend/resume cycles. Each agent runs on the substrate worker in a gVisor or Firecracker VM and is completely locked down.


All network traffic goes through agentgateway and can (future) be locked down with fine-grained egress and ingress policies. For example, an agent trying to make calls out to OpenAI doesn't need to have OpenAI API keys. Credentials can be injected on egress from agentgateway.


Agents can behave with hostility (even out of the kindness of their good intentions) so they should be locked down and finely controlled. Running agents on Kubernetes has been sub-optimal up to this point. With agent substrate and kagent, we’ve solved some of these problems.

## Running agents on kagent

Here’s a quick example. We can run an OpenClaw style agent harness by creating it through the kagent UI:


You can see we pick the *Runtime → Control plane *as “Agent Substrate”. Kagent still supports 1:1 agent to pod. You can then interact with the agent normally (through channels, or the gateway UI, etc). The OpenClaw agent will be scheduled as an actor to a worker in the worker pool.

You can review what actors are deployed to what workers in the Substrate view:

## Where to go from here?

Kubernetes transformed how we run services. Agent Substrate makes running AI agents on top a reality.

If you're building agent platforms, agent harnesses, or autonomous workflows on Kubernetes, now is the time to get involved. Try kagent, experiment with Agent Substrate, and help shape the next generation of cloud-native agentic infrastructure.

[Read the docs](https://kagent.dev/docs/kagent), [join the community](https://kagent.dev/community), and start building with kagent today!!
