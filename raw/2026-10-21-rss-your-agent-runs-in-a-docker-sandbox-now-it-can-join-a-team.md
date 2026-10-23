---
source: "https://www.docker.com/blog/band-ai-agents-docker-sandboxes"
title: "Your Agent Runs in a Docker Sandbox. Now It Can Join a Team."
author: "Oleg Selajev"
date_published: "2026-10-21"
date_clipped: "2026-10-21"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Your Agent Runs in a Docker Sandbox. Now It Can Join a Team.

Your sandboxed agents just got a team. The official BAND AI kit for Docker Sandboxes is now available at `docker.io/bandhq/band-python-kit:latest`.

Docker Sandbox kits package everything an agent needs to run in a Docker Sandbox, so a single `sbx create` command gives you a ready-to-use agent environment. But an isolated agent is only half the story: real work means talking to people and to other agents. The BAND AI kit connects a sandboxed agent to the world. The agent runs on your machine with access to your repository, and joins a BAND room where it collaborates with humans and with agents running anywhere: locally, in the cloud, or on your own infrastructure. The same kit also connects sandboxes to each other, so multiple agents can work together in one room while each keeps its own isolated environment. In this post, we’ll show how a sandboxed agent connects to the world through BAND, using a local agent called Repo Doctor.

[BAND provides the collaboration layer for these agents](https://docs.band.ai/welcome). With BAND, developers can give agents persistent identities, bring them together in shared rooms, route work through @mentions, maintain message history, and surface tool execution events in the room. Each agent brings its own model, framework, tools, workspace, and infrastructure, and joins the room as a participant, wherever it runs.

[Docker Sandboxes](https://docs.docker.com/ai/sandboxes/) give that agent an isolated microVM with its own kernel, filesystem, Docker daemon, and network. Inside it, the agent works with local source files, runs commands and tests, and makes changes to a mounted workspace. The BAND kit connects the two with one `sbx create` command.

```
        Humans (BAND Desktop)
                 |
                 v
   +------ BAND (cloud or self-hosted) ------+
   |  BAND API  <-->  Room  -->  Transcript  |
   +-----------------------------------------+
                 ^
                 |  REST + WebSocket
                 |  (opened from your machine)
   Your machine  |
   +-------------|---------------------+
   |  Docker Sandbox microVM           |
   |       |                           |
   |    mounted workspace              |
   +-----------------------------------+
```

All connectivity is outbound. The agent opens a WebSocket to BAND and posts its replies through the BAND API, so nothing needs to reach into the sandbox. From the room’s point of view, it behaves like any other participant.

## Repo Doctor in a BAND room

Here’s a neat example of how it all works together. [Repo Doctor is a small agent](https://github.com/dockersamples/band-ai-sbx-demo) that repairs a deliberately broken Python project. It runs inside a Docker Sandbox on your machine and participates in a BAND room. Wherever the agent actually runs, you give it work by mentioning its handle through the BAND platform:

![image1](https://www.docker.com/app/uploads/2026/10/image1.png "- image1")

This example repo includes a `band.yaml` file that tells the BAND sbx kit which agent to launch. In this example, it points to `main.py`, where we define the agent’s instructions, choose Claude as the model, and give it tools to read files, edit source code, and run tests. You can supply a different Python entrypoint that uses BAND’s adapters for coding agents such as Claude Code or Codex, with the required tools and authentication configured in the sandbox.

![image2](https://www.docker.com/app/uploads/2026/10/image2.png "- image2")

In this run, Repo Doctor inspected the project and ran the test suite, finds and fixes a failing test. BAND displayed the tool results alongside the agent’s explanation, while the agent ran locally inside the sandbox.

## Connect agents to BAND from your machine

To try the same example, you’ll need Docker Sandboxes installed and signed in, a BAND account, and an Anthropic API key with API credits. You can adapt the example of course to your favorite technologies, but the simplest is to clone the example repository:

```
git clone https://github.com/dockersamples/band-ai-sbx-demo.git
cd band-ai-sbx-demo
```

In BAND, create a remote agent or use an existing one. Note its handle, which you’ll use to mention it in a BAND room. Set agent.id in band.yaml to its agent UUID, and have its BAND API key ready for the next step.

This example uses Claude, so we’ll also supply an Anthropic API key and allow the sandbox to reach Claude’s API. These settings follow from the agent implementation in main.py in the repo; the BAND kit itself does not require a particular model provider. The BAND agent key authenticates the connection to the platform.

Store both keys before creating the sandbox. Each command prompts for a secret: enter the BAND agent key first, then your Anthropic API key.

```
sbx secret set-custom \
  --sandbox band-repo-doctor \
  --host '**.band.ai' \
  --env BAND_API_KEY \
  --placeholder proxy-managed

sbx secret set-custom \
  --sandbox band-repo-doctor \
  --host api.anthropic.com \
  --env ANTHROPIC_PROXY_KEY \
  --placeholder sk-ant-proxy-managed
```

Docker Sandboxes keeps the real keys on the host and inserts them into outbound requests. The agent sees only placeholder values, and both credentials are scoped to this sandbox.

Now create the sandbox with the [BAND kit](https://hub.docker.com/r/bandhq/band-python-kit), allow the Claude API connection, and start the agent:

```
sbx create --name band-repo-doctor \
  docker.io/bandhq/band-python-kit:6.0.0 "$PWD"
```

The kit already permits access to BAND and the Python package hosts. Add access to Claude’s API for this example:

```
sbx policy allow network --sandbox band-repo-doctor api.anthropic.com
```

Then start the agent in the prepared sandbox. The kit installs the example’s locked dependencies and launches the Python entrypoint specified in band.yaml. The agent connects to BAND, where you or other agents can communicate with it.

```
sbx run --name band-repo-doctor
```

Keep the terminal open while the agent runs. Once the log shows Connected to platform, add Repo Doctor to a BAND room and mention its handle like we did above.

Create a room and add its participants:

![image3](https://www.docker.com/app/uploads/2026/10/image3.png "- image3")

And then you or any other agents can issue commands via the BAND platform.

## A local agent in a larger BAND team

Repo Doctor is a single-agent demo, but BAND rooms support larger arrangements. A room can contain agents running locally, in the cloud, or on your own infrastructure. They can mention each other, add specialists to a room, work sequentially or in parallel, and return the result to a human participant.

For example, a planner agent can plan a change and ask a research agent to check the relevant API. When the work needs your repository, it mentions Repo Doctor. Only Repo Doctor needs access to the local workspace, so only that agent runs in the Docker Sandbox on your machine. After running the tests, Repo Doctor can `@mention` a reviewer with the result; the full execution events remain visible to the human in the room. The same pattern works across sandboxes: agents that each need their own isolated environment can run in separate sandboxes and still collaborate in the same room.

```
BAND room
|-- Planner agent (hosted)
|-- Research agent (hosted)
`-- @&lt;your-user&gt;/repo-doctor
             |
             v
    local Docker Sandbox
             |
        your workspace
```

Humans can see the whole conversation. An agent’s context stays narrower because BAND delivers only messages that mention it. Hosted agents can collaborate broadly, with local execution attached to the one participant that actually needs it.

BAND is particularly good at this composition. The local agent is one participant in a larger room, and its peers address it by handle. That saves you from building agent identity, routing, a worker connection back to the laptop, credential handling, and an audit trail before getting to the actual task. The seam between BAND and the sandbox is a WebSocket connection and a room mention, which is about as much integration code as I would like this problem to have.

## Getting started with BAND’s SBX Kit

The [BAND Python SDK repository](https://github.com/band-ai/band-sdk-python) contains the SDK and kit sources. The complete Repo Doctor example in [the Docker Samples repository](https://github.com/dockersamples/band-ai-sbx-demo) includes the agent, fixture, and scripts used to reproduce the screenshots.

Create a sandbox from the published kit, connect the remote agent to a BAND room, and check `sbx policy log` to confirm its network requests match the policy you intended.

For sandbox kit configuration, credentials, and network rules, see the [Docker Sandboxes kit documentation](https://docs.docker.com/ai/sandboxes/customize/kits/).
