---
source: "https://www.docker.com/blog/docker-sandboxes-firecrawl-web-access/"
title: "Give sandboxed agents live web access with the Firecrawl kit for Docker Sandboxes"
author: "Jennifer Kohl"
date_published: "2026-11-16"
date_clipped: "2026-11-16"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Give sandboxed agents live web access with the Firecrawl kit for Docker Sandboxes

## Sandboxed agents cannot read the web

A coding agent in Docker Sandboxes runs inside an isolated VM, the sandbox controls which hosts it can reach, and credentials stay on the host behind a proxy. The same controls keep the agent from opening a docs page, reading a changelog, or looking up an API that shipped after its training cutoff, so it writes code against the version it remembers. The usual fix is to widen the allowlist until the agent can fetch anything, which hands back most of what the sandbox took away.

The Firecrawl kit gives the agent web search, page scraping, and site crawling through one added host, `api.firecrawl.dev`, and every page comes back as clean markdown.

In this post, you’ll learn:

- How the Firecrawl sandbox kit plugs into a sandbox you already run
- How to install the sandbox kit and give your agent its first live-web task
- How to check that the SDK, the API key, and the network rule all work
- What the sandbox kit can’t do yet, and what new work it makes possible for your agent

## Why a kit

The Firecrawl kit is a mixin (`kind: mixin`): it extends whichever workload you already run rather than defining a new sandbox. Its descriptor, `firecrawl/firecrawl.yaml`, declares four typed capabilities:

1. **An install step** (`lifecycle@1`). It installs the Firecrawl Python SDK, `firecrawl-py`, pinned to 4.44.0, as the agent user, and fails sandbox creation if the install or import check fails.
2. **A credential** (`credential@1`). It requests a proxy-managed `firecrawl` API key. Inside the sandbox, `FIRECRAWL_API_KEY` holds the placeholder `proxy-managed`; the proxy swaps in the real key on requests to `api.firecrawl.dev`, so the key never enters the image or the sandbox.
3. **Network permissions** (`network-policy@1`), split by phase. The install step may reach `pypi.org` and `files.pythonhosted.org`; at runtime the agent may reach `api.firecrawl.dev`.
4. **Agent instructions** (`agent-context@1`). A context file tells the agent the capability exists, how to call it, and which limits come from the sandbox. The workload indexes it from its own `AGENTS.md`.

The kit adds to the sandbox’s allowlist and does not narrow it, so everything else is set by your global `sbx` policy. Docker’s `balanced` preset allows package registries, GitHub, and a curated list of vendor domains, and returns a 403 for general websites, including most documentation sites, so Firecrawl is the agent’s route to those. Under `deny-all`, it is the agent’s only web host.

Kits are experimental and in Early Access, so the kit format and `sbx` commands may change. The steps below are current for October 2026; the repository README carries the latest.

## The workflow

### Prerequisites

- The `sbx` CLI, version 0.46 or later, signed in with `sbx login`. On macOS: `brew trust docker/tap && brew install docker/tap/sbx`. Docker Desktop is not required.
- A global network policy, set once with `sbx policy init balanced`. Without it, no sandbox starts.
- A Firecrawl API key (`fc-...`) from [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys).
- A workload to add the kit to. This walkthrough uses Docker’s shell workload, `docker/sbx-kit-shell`, with the Claude Code mixin, `docker/sbx-kit-claude-mixin`. Other workloads and agent mixins are on [Docker Hub](https://hub.docker.com/search?type=sbx_kit&badges=verified_publisher).

Kit: `docker.io/firecrawl/sbx-kit-firecrawl:1.0.0` on Docker Hub, for `linux/amd64` and `linux/arm64`. Source: [github.com/firecrawl/firecrawl-docker-sandbox](https://github.com/firecrawl/firecrawl-docker-sandbox).

**1. Store the key once on the host.** The command prompts for the key. Service secrets are global by default, so every sandbox that requests the `firecrawl` service can use it once you approve. The kit never sees the value; the proxy injects it at request time.

```
sbx secret set firecrawl
sbx secret ls
```

**2. Start a sandbox with the kit.** The kit is an ordinary OCI image with its descriptor in the manifest, so a version tag is all you need. Each `--kit` adds a mixin to the workload, and the trailing `.` mounts your project directory.

```
sbx run docker/sbx-kit-shell:1.0.0 \
  --kit docker/sbx-kit-claude-mixin:2.1.285 \
  --kit docker.io/firecrawl/sbx-kit-firecrawl:1.0.0 .
```

On the first run, `sbx` asks you to approve sending the `firecrawl` credential to `api.firecrawl.dev`. Accept the defaults. The credential is required: with no secret stored, `sbx` refuses to create the sandbox instead of letting the agent hit a 401 mid-task. A detached or CI run cannot answer the approval prompt, so approve interactively once or write the binding to `~/.config/sbx/credentials.yaml` first.

**3. Give the agent a task that needs the live web.** Documentation sites are blocked under `balanced`, so this one has to go through Firecrawl.

```
Read <https://docs.pydantic.dev/latest/changelog/> and list what changed in the latest Pydantic release. Quote the page, don't answer from memory.
```

The kit’s instructions tell the agent to scrape blocked hosts through Firecrawl, so it calls `fc.scrape(...)` unprompted. Its response, trimmed:

```
The most recent release listed on the changelog is v2.13.4 (2026-05-06). I fetched the page live through Firecrawl.

Quoted from the page:
> ## v2.13.4 (2026-05-06)
> ### What's Changed
> #### Packaging
> - Bump libc from 0.2.155 to 0.2.185 by @Viicos in #13109
> - Adapt `pydantic-core` linker flags on macOS by @washingtoneg and @Viicos in #13147
> #### Fixes
> - Preserve `RootModel` core metadata by @Viicos in #13129

It's a small patch release with no new features.
```

**4. Verify each layer.** In the same session, `!` runs shell commands inside the sandbox.

```
!python3 -c "import firecrawl, importlib.metadata as m; print('firecrawl-py', m.version('firecrawl-py'))"
```

Expected: `firecrawl-py 4.44.0`.

```
!env | grep FIRECRAWL_API_KEY
```

Expected: `FIRECRAWL_API_KEY=proxy-managed`. A real `fc-...` value here means the key came from somewhere other than the kit.

```
!python3 - <<'PY'
from firecrawl import Firecrawl
fc = Firecrawl()
doc = fc.scrape("<https://docs.pydantic.dev/latest/changelog/>", formats=["markdown"])
print(doc.markdown[:300])
PY
```

Expected: the page as markdown, starting with `# Changelog` and the latest version heading. The same URL returns a 403 to `curl` from inside the sandbox, so output here proves the SDK, the credential, and the network rule at once.

The kit also describes itself inside the sandbox. This prints the published descriptor, and the agent instructions sit next to it as `firecrawl-context.md`:

```
!cat /usr/share/sandbox/kit/firecrawl/kit.yaml
```

**Running from source.** To review or modify the kit before you run it, clone the repository and point `--kit` at the `firecrawl/` directory; `sbx` builds source kits on demand:

```
git clone <https://github.com/firecrawl/firecrawl-docker-sandbox.git>
sbx run docker/sbx-kit-shell:1.0.0 --kit ./firecrawl-docker-sandbox/firecrawl .
```

### Known limitations

- Under `balanced`, general websites return a proxy 403 to `curl`, so a URL found in a scrape result has to be scraped through Firecrawl too.
- Screenshot and other media formats return links on Firecrawl’s storage host, which the allowlist does not include, so those files cannot be downloaded inside the sandbox.
- Under organization governance, managed policy overrides the kit’s allow rule, and scrapes fail with a proxy-side 403 until the organization allows `api.firecrawl.dev`.
- An HTTP 402 means the Firecrawl account is out of credits; the agent is told to stop rather than retry.

## What this unlocks

With the kit installed, the agent can look things up on the web while it works. The sandbox only needs to talk to one new address, `api.firecrawl.dev`, and Firecrawl fetches the pages for it. This matters because the default balanced policy blocks most documentation sites. Without the kit, you’d have to allow each site one by one, and every new site you allow makes the sandbox a little less locked down.

Without the kit, you had a choice to make. The default balanced policy blocks most documentation sites, so you could either leave the agent working from what it remembered, or allow sites one by one and loosen the sandbox a little each time. The kit avoids that choice. Your Firecrawl API key stays on your machine, behind the proxy, and the agent still reads the web as it is today.

Here’s what the agent can do:

- **Code against the current API, not the remembered one**. Before calling a library or SaaS API, the agent scrapes its reference page and changelog. It uses today’s parameter names and spots deprecations that shipped after its training cutoff.
- **Upgrade dependencies with the release notes in hand**. Asked to bump a package, the agent reads the release notes for every version in between, lists the breaking changes, and edits the code to match before running the tests.
- **Load a vendor’s docs into context.** For a new integration, the agent crawls the relevant section of the vendor’s docs and gets it back as markdown, so it can work from the whole guide rather than one page.
- **Research an error it can’t explain.** When a build or test fails with an unfamiliar message, the agent searches for it, reads the matching GitHub issue or forum thread, and applies the documented fix or workaround.
- **Cite its sources**. Because every answer comes from a fetched page, the agent can quote the text and link the URL it used, so you can check its work.

The result is fewer made-up APIs, fewer failed upgrades, and less time spent correcting an agent that was confidently out of date.

## Where the kit comes from

The kit is published under the `firecrawl` organization on Docker Hub as `firecrawl/sbx-kit-firecrawl`, with source, changelog, and CI on GitHub under Apache-2.0. The SDK pin is verified against PyPI’s package hashes at install time, and every release passes Docker’s `kit-tck` conformance suite in CI. Review the descriptor and allowlist before running it, as with any kit.

## Try it

Pull the kit from Docker Hub: [hub.docker.com/r/firecrawl/sbx-kit-firecrawl](https://hub.docker.com/r/firecrawl/sbx-kit-firecrawl). Issues and feature requests go to the [GitHub repository](https://github.com/firecrawl/firecrawl-docker-sandbox/issues).
