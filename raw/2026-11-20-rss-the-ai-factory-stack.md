---
source: "https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/ai-factory-stack"
title: "The AI factory stack"
author: "Vanitha Kumar"
date_published: "2026-11-19"
date_clipped: "2026-11-20"
category: "Software Architecture"
source_type: "rss"
---

# The AI factory stack

Suppose a leadership team approves an AI budget based on the price per million tokens. The first invoice may come as a surprise; the price that was approved relates to the model while the invoice reflects the actual work.

Agentic workloads consume tokens differently from chat. An agent loop re-reads its context on each pass, and tool output goes back into the context window. Subagents explore, retry and report back. A long system prompt is billed on every call. A cheap model used carelessly can cost more than an expensive one used well. The invoice depends on volume, context size and repetition, and on the infrastructure those requests run through.

This essay is about that infrastructure: *the AI factory*. Its importance is growing to such an extent that we see it as a theme in the most recent volume of the [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar). The lesson, really, is that token economics is infrastructure economics. The per-token price is one line item, and routing, batching, storage, network, scheduling, isolation and failure decide the rest.

## What is the AI factory?

The AI factory is the production system that turns compute, data, storage, networking and models into reliable, priced inference. It has four jobs:

- **Utilization.** Keep expensive accelerators busy with useful work.
- **Latency.** Meet the response time the product promised.
- **Resilience.** Finish long-running work when processes, nodes and networks fail.
- **Attribution.** Know which team, workflow or customer spent the money.

Discussions of AI often treat these as properties of the model, but they belong to the system. A model can't batch a request, route around a failed region or explain why a retrieval job waited 20 minutes for a storage read. The factory does those things.

The request path is easy to draw. A request arrives at a gateway, selects a model, lands on a serving replica, reads from storage and returns a response. Most of the economics sit in the control plane around that path: policy, quotas, routing, observability, isolation and the workflows that keep a task alive for longer than a single call.

## The AI factory stack at a glance

| **Layer** | **Question it answers** | **Vol. 35 blips** |
| --- | --- | --- |
| **Routing and policy** | Which model sees this request, at what cost, latency and residency? | **[LiteLLM](https://www.thoughtworks.com/radar/platforms/litellm) (Trial)**; **[agentgateway](https://www.thoughtworks.com/radar/platforms/agentgateway) (Assess)** |
| **Serving and scheduling** | How much of the accelerator is used, and by what? | **[KServe](https://www.thoughtworks.com/radar/platforms/kserve) (Trial)**; **[KAITO](https://www.thoughtworks.com/radar/platforms/kaito) (Assess)**; **[llm-d](https://www.thoughtworks.com/radar/platforms/llm-d) (Assess)** |
| **Storage** | Can data arrive fast enough to keep the accelerators busy? | [**VAST DataStore**](https://www.thoughtworks.com/radar/platforms/vast-datastore) (Assess) |
| **Network** | Can accelerators talk to each other without waiting? | [**Netris**](https://www.thoughtworks.com/radar/platforms/netris) (Assess) |
| **Observability** | Can you see cost, latency and failure at the cardinality AI produces? | [**VictoriaMetrics**](https://www.thoughtworks.com/radar/platforms/victoriametrics) (Adopt); [**VictoriaLogs**](https://www.thoughtworks.com/radar/platforms/victorialogs) (Trial) |
| **Isolation** | Can teams share the factory without sharing risk? | [**vCluster**](https://www.thoughtworks.com/radar/platforms/vcluster) (Trial); [**Talos Linux**](https://www.thoughtworks.com/radar/platforms/talos-linux) (Trial); [**agent sandboxing**](https://www.thoughtworks.com/radar/techniques/agent-sandboxing) (Adopt) |
| **Workflows and queueing** | What happens when a task takes hours, retries or fails halfway? | **[Temporal](https://www.thoughtworks.com/radar/platforms/temporal)** (Trial) |
| **Resilience** | Which failures does the system survive? | [**Chaos Mesh**](https://www.thoughtworks.com/radar/tools/chaos-mesh) (Trial) |

## Route before you serve

The first economic decision is routing. A request shouldn't go to the most capable model by default. It should go to a model that is fit for the task and can complete it within the budget, latency, and quality requirements. Those are different policies, and the gap between them accounts for a large part of the bill.

[**LiteLLM**](https://www.thoughtworks.com/radar/platforms/litellm), in Trial, is the abstraction and routing layer. It offers one API across providers and moves the choice of model out of application code and into policy. That helps when you manage a portfolio of models: when a team adds a model, retires one or shifts traffic to a cheaper provider, the application shouldn't need a new release. [**agentgateway**](https://www.thoughtworks.com/radar/platforms/agentgateway), in Assess, covers the other half of that layer, enforcing policy at the point where agent traffic enters the serving path.

Without routing, a model portfolio is just a procurement list. The gateway turns it into a set of rules: *this workflow gets the small model, that one gets the frontier model, this tenant has a residency constraint, that batch can wait until off-peak and everything falls back to a known-good route when a provider degrades.*

Routing handles budget, latency and where data is able to go. If you keep those three concerns in one place, you can review them together. If they live in application code, they'll drift apart.

## Keep the accelerators busy

The second economic decision is utilization. **[KServe](https://www.thoughtworks.com/radar/platforms/kserve)**, in Trial, covers model runtimes and serving. [**KAITO**](https://www.thoughtworks.com/radar/platforms/kaito), in Assess, covers accelerator management, and llm-d, in Assess, covers distributed inference and scheduling. The tools matter less than the job, which is to keep expensive hardware doing useful work and to make the scheduling visible when it can't.

KServe's cache-aware routing shows why serving is an economic layer. A request that lands on the wrong replica pays for a cache miss. At chat volume, that's a latency detail. At agent volume, with long prompts and repeated context, it appears as a line item.

Batching is the other lever. Where the latency budget allows, batch requests. Where it doesn't, isolate them so a long-running job can't block a fast one. The latency target is a product decision; the serving layer's job is to meet it without buying capacity for the peak. A factory that runs half-empty doubles the cost-per-token. Utilization therefore works as a unit-cost metric, not only an operations metric. The most expensive GPU is the one that sits idle but reserved.

Right-sizing belongs here too. [Using a small model for a simple task](https://www.thoughtworks.com/radar/techniques/blanket-frontier-model-usage) is sound capacity planning, not a compromise. Which models belong in the portfolio is a separate question, and the serving layer is where the answer turns into a price.

## The layers beyond the demo

Two layers rarely appear in an AI demo, but both can dominate your bill when you scale:

- **Storage.** **[VAST DataStore](https://www.thoughtworks.com/radar/platforms/vast-datastore)**, in Assess, addresses storage throughput for training and retrieval. What matters is less how many terabytes you hold than whether data arrives fast enough to keep the accelerators busy. A slow read leaves an expensive GPU sitting idle.
- **Network.** **[Netris](https://www.thoughtworks.com/radar/platforms/netris)**, in Assess, addresses east-west traffic between accelerators. Distributed inference and training are synchronized work, so the fabric sits on the critical path. A network that handles web traffic well can bottleneck GPU-to-GPU traffic, and the symptom looks like a slow model rather than a slow network.

A demo runs on one node, but production traffic crosses storage and the network fabric. If you can't describe the storage and network path of a request, you can't explain the unit cost of a token.

## 

## See the bill

Attribution depends on observability, because you can't assign a cost you can't see. [**VictoriaMetrics**](https://www.thoughtworks.com/radar/platforms/victoriametrics), in Adopt, is a replacement for [Prometheus](https://www.thoughtworks.com/radar/tools/prometheus) replacement for the cardinality AI platforms generate, where conventional monitoring becomes prohibitively expensive. [**VictoriaLogs**](https://www.thoughtworks.com/radar/platforms/victorialogs), in Trial, applies the same approach to logs.

Telemetry earns its place when it answers financial questions: *Which workflow spent the most this week? Which route has the worst cache hit rate? Which tenant's retries are inflating the queue?*

It's important to remember that observability has a cost. Cardinality and retention have a price, and an AI factory that instruments everything without a retention policy will spend its savings on monitoring.

## Isolate, persist and fail gracefully

The remaining layers have little to do with speed. They cover what happens when the factory is shared, when a task outlives a process and when something breaks.

- **Isolation. [Talos Linux](https://www.thoughtworks.com/radar/platforms/talos-linux)** and**[vCluster](https://www.thoughtworks.com/radar/platforms/vcluster)**, both in Trial, provide isolation for multi-tenant platforms. We usually think of isolation as a security control, and it is one. It also controls cost, because one team's runaway job shouldn't raise every other team's unit cost. Virtual clusters and a minimal node operating system reduce the blast radius of a noisy neighbor, a bad deployment or a compromised workload.
- **Durability. [Temporal](https://www.thoughtworks.com/radar/platforms/temporal)**, in Trial, provides durable workflows. Agentic work runs for a long time, retries and sometimes fails halfway; a durable workflow records where the task is, what it has already done and what to do next after a restart.
- **Resilience. [Chaos Mesh](https://www.thoughtworks.com/radar/tools/chaos-mesh)**, in Trial, injects failures on Kubernetes so teams can learn what the system survives before a customer does. Try losing a GPU node, partitioning the network, delaying storage or killing a worker mid-retry. If a factory has never lost a node, you don't yet know whether it's resilient.

Reliability is a cost lever as well as an availability target. Retries and rework are the most expensive tokens, because you pay for them twice: once when the first attempt fails and again when the retry succeeds.

## 

## The cost model

The number that should be managed is cost per completed task. **Cost per completed task is the sum of compute, storage, network, observability, idle capacity and rework, divided by the number of tasks that finish.** Each layer discussed here moves one of those terms:

- Routing affects compute and latency.
- Serving affects utilization.
- Storage and network affect waiting time.
- Observability makes attribution possible.
- Isolation limits the cost of a noisy neighbor.
- Durability and queueing reduce rework.
- Resilience reduces the cost of the worst cases.

Five measures are enough to start:

1. **GPU-hours per completed task.** The utilization measure that matters.
2. **Cache hit rate, by model and route.** The serving detail that becomes a line item.
3. **Queue time versus run time.** The measure that shows where the factory is constrained.
4. **Cost per successful task, by workflow.** The number the business can act on.
5. **Retry rate.** Failed runs, retries and human review, counted together.

Cost-per-token can fall while cost per completed task rises. A cheaper model with a bloated context saves nothing, and neither does a smaller instance that misses the latency target. A team that cuts cost without measuring quality ends up cheaper but worse.

## Build or buy the AI factory?

Most organizations shouldn't try to rebuild a hyperscaler. They should rent the layers where scale is the only advantage: compute, storage and the physical network. Differentiation should sit higher up, in the routing policy, the data, the evaluation, the workflows and the attribution that tells you which of them is working.

The buy/build boundary is a control decision as much as a cost decision. Residency, sovereignty and lock-in determine which layers you can rent, and unit cost determines which you should. Getting it wrong in either direction is expensive. If you build everything, you fund a platform you can't operate. If you rent everything, you lose the levers that make the factory efficient.

In practice, know which layers you rent and why, and instrument the boundary between what you rent and what you run.

## Start with one workflow

The team in the opening approved a budget on the price of a token. What it has to run is a factory. The gap between those statements is closed by measuring one real workflow, not by a better price list.

Pick a single workflow in production; it should neither be a demo or the whole platform. Instrument the request path, including the route it took, the replica it landed on, the time it waited on storage or the network, the retries it needed and the review it consumed. Then divide by the tasks that completed. That's the unit cost, and it's the only number that can be managed.

The first measurement is usually unflattering and instructive. The constraint is rarely where the budget assumed: a route sending long prompts to a replica that keeps missing cache; a queue that looks busy but is waiting on one storage volume; a retry loop that doubles the token count without changing the answer; a review step that costs more than the inference it checks. Each needs an owner.

Fix one layer, then measure again. A program that changes five things at once cannot tell you which one worked.

## Where to start

You don’t need to build the whole factory. Pick one agentic workflow that already runs in production and measure its cost per completed task for a few weeks, using the five measures above: GPU-hours per completed task, cache hit rate, queue time against run time, cost per successful task and rework rate.

The numbers will point at a layer. A poor cache hit rate sends you to routing and serving. Long queue times send you to scheduling and queueing. A high rework rate sends you to durability and resilience. Fix that layer first, then measure again.

Once you know which layer needs work, the technologies mentioned here that appear on the Thoughtworks Technology Radar are a reasonable place to begin. By then you’ll be choosing them against a number you measured instead of a per-token price.

## Financial oversight and your AI factory go hand in hand

The leadership team in the opening approved a budget on the price per million tokens, which captures only the model used. The invoice is more instructive and reflects the AI factory around it: routing picks the model, the serving layer keeps accelerators busy, and storage and network feed them.

Observability attributes the spend, and isolation, durable workflows and failure testing keep shared, long-running work from turning into rework. It's those layers that decide whether a task finishes, how long it takes and what it costs; this is why the number that really needs to be managed is cost per completed task.

**If your team can’t yet say what one production workflow costs per completed task, start by measuring that.**
