---
source: "https://www.docker.com/newsletter-subscription/2026-05-11-ai-workflows-breaking-builds-container-security/"
title: "Docker Navigator: AI Workflows, Container Security, and Build Reliability"
author: "Payal Sharma"
date_published: "2026-05-14"
date_clipped: "2026-06-08"
category: "DevOps & CI/CD"
source_type: "web"
---

# Docker Navigator: AI Workflows, Container Security, and Build Reliability

Source: https://www.docker.com/newsletter-subscription/2026-05-11-ai-workflows-breaking-builds-container-security/

## Stay in the know

Stay up to date on the latest Docker news, opinions and tools.

**Welcome to the May edition of Docker Navigator. Missed an issue? Read past issues in our collection. **

AI is moving from generating code to executing it, changing what developers need from the systems around it. This issue looks at what that means in practice, from hardening container images without breaking real builds to isolating untrusted workloads and responding to supply chain attacks. Those same constraints show up as teams run agent-driven workflows, build AI systems locally, and move from blocked deployments to production-ready environments.

[Why We Chose the Harder Path: Docker Hardened Images, One Year Later](https://www.docker.com/blog/why-we-chose-the-harder-path-docker-hardened-images-one-year-later/)

Hardening images sounds straightforward until stripping packages starts changing how they behave in real builds. Hardened Images took a different path: reduce real risk without breaking developer workflows. A year in, here’s where those tradeoffs landed.

[Why MicroVMs: The Architecture Behind Docker Sandboxes](https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/)

Some workloads need stronger isolation than containers alone can provide. Docker Sandboxes use microVMs to give each workload its own kernel and environment. A stronger boundary for running code locally without exposing the host.

## Docker News

[Trivy, KICS, and the Shape of Supply Chain Attacks So Far in 2026](https://www.docker.com/blog/trivy-kics-and-the-shape-of-supply-chain-attacks-so-far-in-2026/)

A malicious image was pushed to a trusted Docker Hub namespace and pulled before it was caught. It’s part of a growing pattern in 2026: attackers targeting repositories developers already trust. The risk isn’t just unknown images, it’s the ones that look familiar.

[Precision Container Security with Docker and Black Duck](https://www.docker.com/blog/precision-container-security-with-docker-and-black-duck/)

Black Duck now recognizes Docker Hardened Images and uses VEX data to suppress CVEs that don’t actually affect your application. Less noise in scan results, shorter triage, and no changes to your build process.

## Dive Deep: Running AI Agents Safely and Moving Local AI into Real Workflows

AI agents are moving beyond assisted coding into environments where they execute code, interact with systems, and operate inside CI pipelines. At the same time, more AI workloads are moving local to improve control, performance, and reliability. These deep dives look at what it takes to run those workflows safely, from isolated execution to production-ready deployments.

### Running AI Agents in Real Workflows

Docker’s coding agent sandboxes team is already [running fleets of agents](https://www.docker.com/blog/a-virtual-agent-team-at-docker-how-the-coding-agent-sandboxes-team-uses-a-fleet-of-agents-to-ship-faster/) to test, triage, and modify code in parallel. That shift raises new questions around execution control and isolation in CI environments.

Running Models Locally

Running models locally brings more control over performance, cost, and data, but also introduces new constraints around compatibility and environment setup. [Generating images locally with Docker Model Runner and Open WebUI](https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/) shows how those workflows come together.

From Experiment to Production

Getting from a working setup to production often comes down to security constraints and image compatibility. [ClickHouse moved from blocked to production-ready using Docker Hardened Images](https://www.docker.com/blog/from-security-blocked-to-prod-ready-clickhouse-on-docker-hardened-images/), showing how those constraints get resolved in practice.

### Watch: Agent Workflows in Practice

Agents don’t just change how code is written, they change how it runs. Agent workflows behave differently in real environments, especially as they scale and interact with shared systems.

The latest episode of [Docker’s AI Guide to the Galaxy](https://www.youtube.com/watch?v=tdmqL3mEneo) explores sandbox isolation in practice. On the [Ship Happens Podcast](https://www.youtube.com/watch?v=FTzr7MtkpqI&list=PLkA60AVN3hh9GgYST8lldjM-AhC8szC6c&index=1), host Per Krogslund sits down with Harness Field CTO Jignesh Patel to unpack why CI/CD pipelines break down at scale and what it takes to make them more reliable.

## Around the Community

The Docker community is active across forums and events. Check the [Docker Forum](https://forums.docker.com/) for the latest discussions, and the [Docker Events page](https://www.docker.com/events/) to find upcoming meetups and conferences near you.

[In this forum thread about Docker Desktop on Ubuntu 24.04.4](https://forums.docker.com/t/docker-desktop-on-ubuntu-24-04-4/151423), an architectural best practice emerged: Docker Desktop on Linux runs inside a Virtual Machine using a custom`desktop-linux`

context, meaning your containers, volumes, and daemon all live in the VM rather than the familiar /var/lib/docker paths you’d expect from Docker CE, making it the better fit for headless Linux servers.- Check out the newly launched
[Labs](https://docs.docker.com/guides/?tags=labs)within Docker docs, where developers can complete hands-on workshops across AI apps, containers, and real-world development workflows.

## On the Calendar

Meet our Product and Engineering teams at leading tech conferences, where they share expertise, explore Docker’s latest advancements, and collaborate with the global tech community to shape the future of innovation.

[LeadDev London (LDX3)](https://leaddev.com/leaddev-london)— London, UK — June 2-3

Docker is heading to LeadDev London with speaking sessions, live demos, and engineering leadership discussions focused on secure, AI-native software development.**Visit Booth #314**to see how teams are building with agents safely at scale.- Connect and chat with Docker ahead of the conference at our
[June 2 meetup in London](https://luma.com/o9i3yqns). [AI Engineer World’s Fair 2026](https://www.ai.engineer/worldsfair)— San Francisco, USA — June 29 – July 2

Docker will be at AI Engineer’s World’s Fair with workshops, lightning talks, demos, and hands-on sessions focused on secure, production-ready AI systems. Visit the Docker team to explore agent-ready workflows and governed AI infrastructure built for scale.

**Can’t make it in person? Join upcoming Docker webinars live or on demand.**

Explore our [on-demand webinar library](https://www.docker.com/resources/?types=video) for sessions from Product and Engineering teams, including:

[The State of AI Agents: Insights From 800+ Builders and Leaders](https://www.docker.com/resources/the-state-of-ai-agents-webinar/)Explore insights from the State of AI Agents report and what the shift to autonomous systems means for infrastructure, workflows, and developer control.[From Zero to Agentic: Build Your First Agentic App with Docker](https://www.docker.com/resources/build-your-first-agentic-app-with-docker-on-demand-webinar/)Watch this demo for a working prototype of how to build your first AI agentic app with Docker.[Running Hardened Images in Prod: Beyond CVE Counts](https://www.docker.com/resources/prove-your-base-images-dhi-enterprise-webinar/)How teams validate, roll out, and operate Docker Hardened Images in production, with DHI Enterprise support for patching, compliance, and customization at scale.

## That’s a Wrap

Thank you for reading Docker Navigator! If you enjoyed this issue, please share it with your friends so they can [subscribe now](http://www.docker.com/newsletter-subscription/).

Got any feedback or suggestions for our next issue? Send comments to [newsletter@docker.com](mailto:newsletter@docker.com).
