---
source: "https://www.docker.com/blog/harbor-docker-sandboxes-run-safe-reproducible-agent-evals"
title: "Harbor + Docker Sandboxes: Run Safe, Reproducible Agent Evals"
author: "Srini Sekaran"
date_published: "2026-10-14"
date_clipped: "2026-10-16"
category: "AI / LLM Research & Tooling"
source_type: "rss"
date_modified: "2026-10-15"
---

# Harbor + Docker Sandboxes: Run Safe, Reproducible Agent Evals

> ## Key takeaways
>
> * **Harbor can now run every eval task in Docker Sandboxes**
> * Docker Sandboxes are MicroVM environments to run agents like Claude Code, Codex, Cursor, and more safely
> * With Sandboxes, define custom network policies for fair, reproducible evals
> * Run your evals locally or in the cloud: starting for free on Docker Sandboxes on local surfaces and scaling to Cloud Sandboxes

To evaluate an agent, you give it a real task, let it work, and check the result. Along the way, the agent installs packages, edits files, and runs commands. That’s untrusted, AI-written code, and a benchmark runs it thousands of times.

And agents don’t always play fair. An agent can sometimes earn a passing score on an eval by gaming the check instead of doing the work, for example by tampering with tests or overwriting the file that records its score. This is called reward hacking, and it’s a growing concern across the eval community.

So running agent evals needs two things:

1. **An eval framework** that runs each task, lets the agent work, checks the result, and collects the scores and logs.
2. **An environment for every task** that’s clean and isolated, so evaluating agents is safe and consistent.

**[Harbor](https://www.harborframework.com/) gives you the first.** It’s an open-source eval framework. Give it a benchmark like Terminal-Bench, and it simplifies the process of running evals.

**Now, [Docker Sandboxes](https://www.docker.com/products/docker-sandboxes/) gives you the second:** a safe way to run those eval tasks, on your laptop or in the cloud.

## Here’s what this means for you

**Strong isolation by default.** Docker Sandboxes were [designed from the ground up](https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/) for deeper isolation. This means you can run every task in a microVM, not a shared container. A microVM has its own kernel, so whatever the agent does stays inside its sandbox. It can’t break out to reach your machine, other tasks, or anything else outside its environment.

**Fair, reproducible evals.** With Docker Cloud Sandboxes, configurable network policies let a task download dependencies during setup, then restrict internet access while the agent works. This way, every agent can be tested under the same conditions.

**Parallel runs, no machines to manage.** With Docker Cloud Sandboxes, teams can run many tasks at once without needing to manually provision anything. Run dozens of concurrent workers simultaneously.\*

**Develop locally, scale in the cloud.** The same tasks run locally or in Docker Cloud Sandboxes. Build on your laptop, then run your tasks in the background, and at scale, without changing anything.

## Try it

Install Harbor with Docker Sandboxes.

`uv tool install "harbor[sbx]"`

[Activate Cloud access](https://docs.docker.com/agentic-platform/signup/) for your Docker account and [create a personal access token](https://docs.docker.com/security/access-tokens/personal-access-tokens/#create-a-personal-access-token). Select **Cloud Sandboxes** under access permissions. Copy and save your token. It’s shown only once.

1. Set your Docker ID (your Docker login username) and PAT (personal access token), then run a task in Cloud Sandboxes.
2. `export SBX_DOCKER_USERNAME="your-docker-id"`
3. `export SBX_DOCKER_PAT="your-personal-access-token"`
4. `harbor run -t hello-world/hello-world -a oracle -e sbx`

To run locally, install the [Docker Sandboxes CLI](https://docs.docker.com/ai/sandboxes/), run sbx login, and add `--ek target=local` to the command above. Harbor’s local integration currently supports public and no-network modes, subject to the machine’s existing sandbox policy.

This integration is available today on the nightly release of Docker Sandboxes.   
  
`uv tool install --upgrade "harbor[sbx]==0.24.1.dev202610150414"`  
  
It’ll be available in the stable release on 10/23. Docker Compose is supported as part of the release, which means Harbor can run multi-container tasks inside a single Docker Cloud Sandbox, so services and sidecars can share that MicroVM.

To learn more, see the [Docker Sandboxes docs](https://docs.docker.com/ai/sandboxes/) and the [Harbor docs](https://docs.harborframework.com/sandboxes/pre-integrated-sandboxes).

*\*We’ve tested Harbor with 64 concurrent tasks on Docker Cloud Sandboxes.* *For higher limits, we’re happy to help:* *[contact us](https://www.docker.com/company/contact/).*
