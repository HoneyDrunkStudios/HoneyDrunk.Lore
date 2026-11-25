---
source: "https://kudelskisecurity.com/research/sandboxing-coding-agents"
title: "Sandboxing AI Coding Agents: nono vs Docker Sandboxes vs Microsandbox vs OpenShell"
author: "unknown"
date_published: "2026-11-23"
date_clipped: "2026-11-24"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-11-24"
---

# Sandboxing AI Coding Agents: nono vs Docker Sandboxes vs Microsandbox vs OpenShell

Source: https://kudelskisecurity.com/research/sandboxing-coding-agents

## Introduction

In this blog post, we compare four major sandboxing tools for AI coding agents in a hands-on approach: nono, Docker Sandboxes, Microsandbox and OpenShell.

We describe what makes a good sandbox and our evaluation criteria. We provide a comparison table at the end that hopefully helps you decide which tool is right for you.

Disclaimer: we are not affiliated with any of the tools discussed in this article.

## Key Findings

- **No tool is perfect:** All four obtained a score between 4 and 4.5 out of 5, and each one has pros and cons
- **Sandboxing primitives:** Docker Sandboxes and Microsandbox use microVMs, OpenShell offers multiple backends, and nono relies on OS-level primitives, which is the fastest option but at the expense of trading some security for speed and simplicity
- **Credential injection:** OpenShell supports the most injection locations, nono and Docker Sandboxes support sandboxed OAuth logins and have vault integrations. Only nono and OpenShell scope credentials to both a domain and endpoint
- **Usability:** Docker Sandboxes is the most polished and nono is the fastest to start. Both Docker Sandboxes and OpenShell have a TUI for live approval of blocked requests, while Microsandbox and OpenShell offer less "coding agent" specific features than the other two because they're more general purpose
- **Gaps all tools have:** No tool can deny a file inside an allowed directory or customize the list of allowed syscalls. No tool comes with a built-in web application for management and monitoring
- **Maturity:** None has reached v1.0 yet, so expect breaking changes and drastic improvements in the near future

## Why AI Coding Agents must be Sandboxed

According to JetBrains' [Developer Ecosystem Survey 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/), 90% of professional developers used AI coding agents at work at least weekly between May and July, and 68% used them daily. Meanwhile, Stack Overflow's [2026 survey](https://survey.stackoverflow.co/2026/ai/data) found that only 7% of respondents trust AI output for important work decisions. What this shows is that AI coding agents are widely used, but at the same time, few of their users trust them for important decisions.

Not only shouldn't they be trusted for important decisions because they can hallucinate or take unwanted actions by mistake, but they also have inherent vulnerabilities that attackers can exploit to manipulate their behavior and force them to take malicious actions. Indeed, prompt injection is still an unsolved problem. The 2025 [CaMeL paper](https://arxiv.org/abs/2503.18813) describes a defense mechanism to solve it but it's impractical to implement in practice.

Meanwhile, Anthropic [reports](https://claude.com/resources/articles/auto-mode-default-in-claude-code) that prompt injection attack success rate (ASR) against Fable 5, Opus 5 and Sonnet 5 is as low as 0.0% and therefore made Auto mode the default mechanism to automatically classify commands to be executed in Claude Code in August. Even though Anthropic claims a 0.0% ASR, Johann Rehberger [showed](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) that he obtained a 60-80% ASR by asking the agent to summarize a website that contained a novel trick not in Anthropic's static benchmark.

One should read AI labs ASR numbers with a pinch of salt and Claude Code's Auto Mode is not a replacement for running the agent in a sandbox. The sandbox is a strong protection for when the agent gets manipulated. Prompt injection shouldn't be underestimated.

There are many different input vectors malicious instructions can be delivered from and they may not always be visible to you. Here are some examples.

Input vectors:

- Source code comments
- README file
- MCP tool name/description/output
- Agent skill
- Web page
- Email
- Calendar invite
- Shared file

Hiding techniques:

- Hidden Unicode characters
- HTML comments
- Spaces/tabs
- New lines

The idea here is that if the agent runs in a sandbox, even if it's manipulated by malicious instructions, there's only so much it can do. The sandbox limits the blast radius. And this is why sandboxing tools are all the rage lately. This also applies to agents that take unwanted actions by mistake or due to a hallucination, regardless of whether the agent is manipulated or not. A sandbox can also limit those unwanted actions.

## Proper Sandboxing

While a sandbox reduces the risk, it's not bulletproof, especially if it's not properly configured or if it lacks the configuration features to do so. Let's remember some recent events that show why.

The [OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/) and [Hugging Face](https://huggingface.co/blog/security-incident-july-2026) incident is a great example of that. In July, OpenAI failed to properly sandbox their fleet of agents running a cybersecurity benchmark (ExploitGym). Because the environment was not properly isolated from the internet, the agents exploited a vulnerability in an Artifactory instance, which had internet access, to obtain network access through it. From there, they exploited 2 vulnerabilities in Hugging Face's dataset upload pipeline to obtain answers to the problem they were trying to solve. This is the perfect example of what a proper sandbox should have been able to block.

In August, Trail of Bits asked GPT 5.6-Cyber to try and escape a QEMU/KVM VM they normally use for sandboxing. It [escaped three times](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/) using 3 different techniques. It wasn't able to escape from a Firecracker MicroVM though. Probably because it has a much smaller attack surface and it's a harder target to escape from. Again, the takeaway is that a strong sandbox is hard to escape from and is a valid mitigation strategy.

Finally, even solutions like Firecracker are not bulletproof, as shown by [pwn.ai](https://pwn.ai/blog/firecracker-escape) and [Coinspect](https://www.coinspect.com/blog/firecracker-escape/). No project will ever be 100% secure, but at least the attack surface is minimal and the risk is reduced.

## Properties of a Good Sandbox

[A few months ago](https://blackhat.com/us-26/summit-sessions/schedule/index.html?track[]=the-ai-summit#ai-challenge-lab-securing-the-vibes-defending-developer-environments-55924), at Black Hat USA 2026's AI Summit, we [talked](https://tome.one/slides/amiet-hamiel-securing-the-vibes-ai-summit-black-hat-2026-slides.pdf) about AI coding agent risks and touched on what makes a good sandbox. Let's see what that is.

The level of security of a sandbox depends on multiple properties, and one of those is the underlying sandboxing primitive used:

| Primitive | Examples | Shared with Host | Security level | Trade-off |
| --- | --- | --- | --- | --- |
| **OS-level sandboxing** | [Landlock](https://landlock.io) + [seccomp](https://en.wikipedia.org/wiki/Seccomp), Seatbelt, namespaces, cgroups | Kernel | Low-Medium | Guest and host share same kernel, not the strongest isolation technique, small performance overhead, super fast start up times |
| **Containers** | Docker, Podman, Kubernetes | Kernel | Medium | Guest and host share same kernel, not the strongest isolation technique, slightly stronger defaults, fast start up times |
| **VMs** | VirtualBox, VMware | Hypervisor and device emulation | High | Strong VM isolation, full hardware support, attack surface larger than MicroVMs due to extra device emulation, slow start up times |
| **MicroVMs** | Firecracker, libkrun | Minimal hypervisor and device emulation | Very High | Strong VM isolation, reduced hardware support, minimal attack surface, fast start up times |

MicroVMs offer the highest level of security with the smallest attack surface, but OS-level sandboxing is the fastest and has the least overhead.

In addition to the sandboxing primitive tradeoff, a good sandbox should be properly configured. And to do so, it should offer enough granularity in what can be restricted through configuration. Here is the full list of criteria we used to evaluate each tool:

- **General:** Sandboxing primitive used, supported platforms (Linux, macOS, Windows), open source or not, account required, backing organization, version and project maturity, whether it's actively maintained, language it's written in, GitHub stars and whether it is also available as a library
- **Filesystem access:** The agent should be able to read and write to the current project directory, but not be able to read SSH keys in ~/.ssh or edit config files that may lead to malicious behavior such as ~/.bashrc or ~/.gitconfig on the host. We looked at read-write access limited to the project directory, read-only and read-write exceptions, denying a file or subdirectory inside an allowed directory, and snapshot and rollback support
- **Network:** Unfiltered outgoing traffic makes it trivial for an attacker to exfiltrate secrets the agent can access. Only normal traffic should be allowed and the rest should be blocked. Filtering by domain name only is not enough: github.com can be used for genuine git work, but the same domain can also be used by an attacker to exfiltrate secrets by pushing a gist or a commit to a repo they can read from. DNS traffic is necessary for an agent to resolve domain names and be able to make network requests, but it's also an exfiltration mechanism that attackers can leverage. Protections should be in place to mitigate this risk. We looked at domain name, IP and CIDR range filtering, HTTP method, path and query params filtering, UDP and other protocols support, DNS exfiltration and rebinding protection, upstream (enterprise) passthrough proxy support, and SSH integration
- **Secrets:** If a secret sits inside the sandbox, then the agent can read it. If the agent is manipulated via prompt injection (malicious instructions), then it can probably exfiltrate that secret since the agent has access to it. The sandbox should support credential injection (explained below). We looked at credential scoping to specific endpoints, where credentials can be injected, secret placeholder format configuration, memory zeroization, password vault integrations (1Password, Bitwarden, etc.), and sandboxed OAuth login support
- **System (process restrictions):** A malicious agent shouldn't be able to exhaust system resources and cause a denial of service, or take malicious actions. We looked at limits on memory, CPU, max process count, max opened files, disk usage, custom syscall allowlist support and various other restrictions
- **Dynamic changes and visibility:** Criteria include: dynamic policy changes while the agent runs, suggestions based on what was blocked, and logging and audit trail support
- **Coding agent support and usability:** If the tool is too hard to use, it will get replaced. We looked at presence of profiles for popular coding agents (marketplace), sandbox awareness agent skills, start-up time, ease of use and installation and documentation clarity

### What is Credential Injection?

AI coding agents typically need to use secrets, including the API token used to authenticate with 3rd party LLM providers. If those secrets enter the sandbox at any time, an attacker who manipulates the agent can probably exfiltrate them. To solve this problem, a technique called credential injection can be used.

The sandbox is configured to route all network traffic through a proxy that sits outside the sandbox. Placeholders for real secrets are stored inside the sandbox, for example in config files. Whenever the agent makes a network request, it goes through the proxy. The proxy intercepts the request and replaces the placeholder with the real secret, and then forwards the request to the endpoint. This is a feature that many dedicated sandboxing tools now support and that we will mention multiple times throughout this blog post.

In order for the credential to never be sent to an attacker, it must be scoped to an endpoint. What would happen if the agent is manipulated to make a request that contains the placeholder secret to attacker.com and the proxy blindly replaces it with the real secret and forwards it to the attacker controlled website? The secret must only be replaced if the destination is an approved one for this specific secret (scoped to domain and endpoint).

![Credential injection: the proxy swaps the placeholder for the real secret only for approved destinations](https://cdn.prod.website-files.com/67711be5796275bf61eaabfc/6afeef2834eaf82e450f1be2_8e022b8b.png)

## Our Methodology

For each tool, we first read its official documentation, then installed the tool on Linux and used it for a short period of time on real work, typically with GitHub Copilot CLI and OpenCode. We used the criteria listed above to evaluate each tool.

Additionally, we gave each tool an overall security score out of 5. This score is based on the isolation primitive used, granularity of restrictions available and the project's maturity and track record of vulnerabilities.

We did not try to escape the sandbox of each of these tools. Our evaluation is only based on the above criteria and this is not a security audit. So our security scores do not account for that.

## What about Built-in Sandboxing Features?

Claude Code, Cursor, Copilot CLI and other AI coding agents come with a built-in sandboxing feature, which is often turned off by default. We tried these features in GitHub Copilot for VS Code and Claude Code. They are definitely better than no sandboxing at all, but they come with a few limitations that dedicated sandboxing tools typically do not have:

- Network filtering is often domain name only
- No credential injection
- No system resources limitation
- Each agent does it differently and must be configured independently so you can't easily switch to another agent and keep it sandboxed

![copilot vscode settings](https://cdn.prod.website-files.com/67711be5796275bf61eaabfc/6afeef2834eaf82e450f1be6_2d7b9fc7.png)

VSCode sandboxing settings

A standalone sandboxing tool is run from the outside, so once configured, it can be used with any AI coding agent.

## Other Tools we did not Evaluate

Not all tools could be reviewed, such as [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) (originally from Alibaba). Raw bubblewrap (Linux) and Seatbelt (macOS) can also be used directly or with a simple wrapper script. These two are the building blocks behind several tools, but bubblewrap has no network filtering. The network is either fully open or fully off. Seatbelt, on the other hand supports network filtering. A few others are also worth mentioning:

- Anthropic's [sandbox-runtime (srt)](https://github.com/anthropics/sandbox-runtime) is the sandbox built into Claude Code. It's OS-level, like nono: bubblewrap on Linux and Seatbelt (`sandbox-exec`) on macOS. It comes with a network proxy, but its features are lacking compared to the full solutions evaluated below.
- Microsoft's [Execution Containers (MXC)](https://github.com/microsoft/mxc) ([announcement](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/)) is supported as a backend by OpenShell on Windows (native binary only).
- [Gondolin](https://github.com/earendil-works/gondolin) is built by the author of the Flask microframework. It's a known team but the project is still early.
- [Capsem](https://github.com/google/capsem) was presented at [un]prompted II ([slides](https://elie.net/static/files/taming-ai-agents-with-capsem/taming-ai-agents-with-capsem.pdf)). The slides mention that "Capsem is 100% AI code generated".

With that in mind, let's now go through the 4 sandboxing tools we decided to evaluate in more depth: nono, Docker Sandboxes, Microsandbox and OpenShell.

## nono

[nono](https://github.com/nolabs-ai/nono) uses OS-level sandboxing primitives like Landlock and seccomp on Linux, and Seatbelt on macOS, so the agent shares the host kernel. It's written in Rust and is open source. It doesn't require an account and it's made by the author of [Sigstore](https://www.sigstore.dev/), Luke Hinds, and his team at nolabs.

It starts instantly with literally no overhead. The documentation is excellent and you can tell it's made for running AI coding agents. They have an official [packs registry](https://registry.nono.sh/packages) where profiles for various popular coding agents can be downloaded from. One should note that since nono uses OS-level sandboxing, whatever agent you run inside it must be already installed on your host. So, for example you'll need to first install GitHub Copilot CLI to be able to run it with nono. If there's no pack for your agent or if it's not supported on your platform (for example, the official nono copilot-cli pack doesn't support Linux), you can create your own pack or profile to support it, which is what we did. Profiles are JSON files that describe your policy and they live in `~/.config/nono/profiles` on Linux. Most packs come with agent skills that tell the agent that they're running inside a sandbox. Indeed, without this, an agent may be confused when it hits a permission error when trying to read or write a file or make a network request. So this is a big plus.

Of course, nono supports filesystem restrictions. Read-write access to specific files or directories can be defined in a profile. It also supports filesystem snapshots and rollback. This is off by default but can be enabled just by passing the `--rollback` CLI flag. When enabled, nono keeps track of every filesystem change during the session, and in case the agent makes unwanted changes to the filesystem, it's then very easy to rollback to an earlier state with this feature. One downside which is actually a Landlock limitation is that it's not possible to deny a sub-directory of an allowed directory.

Nono allows filtering outgoing network traffic by domain name, IP or CIDR range. It also supports filtering traffic by HTTP method and endpoint, including globs. It also supports enterprise proxy passthrough and it prevents DNS rebinding attacks where a malicious DNS server resolves an allowed domain name to an internal IP address. The proxy sitting outside the sandbox first checks all resolved IP addresses against the policy before approving network traffic.

When nono exits, it suggests profile changes based on the network requests and filesystem accesses that were blocked during the session. This is the output after exiting GitHub Copilot CLI running in a nono sandbox:

```
  ╭─╮╭─╮   Changes    +0 -0
  ╰─╯╰─╯   AI Credits 7.8 (17s)
  █ ▘▝ █   Tokens     ↑ 31.1k (31.1k written) • ↓ 31
   ▔▔▔▔    Resume     copilot --resume=fb4d1d58-5a2e-4093-9699-09fa7dfdaaa2

The command succeeded, but stderr showed a likely sandbox-related access issue.

Sandbox denial:
  /home/nils/.gitconfig (read+write)
  Try: --allow-file /home/nils/.gitconfig

Network denials were observed during this session:
  deny connect cafe.example.ghe.com:443 (host cafe.example.ghe.com:443 is not in the allowlist)
  deny connect copilot-telemetry-service.example.ghe.com:443 (host copilot-telemetry-service.example.ghe.com:443 is not in the allowlist)

To allow this traffic, re-run with:
  --allow-domain cafe.example.ghe.com
  --allow-domain copilot-telemetry-service.example.ghe.com

To grant additional access, re-run with:
  --allow <path>     read+write access to directory
  --read <path>      read-only access to directory
  --write <path>     write-only access to directory

Next steps:
  Add permissions: nono run --allow <path> -- copilot
  Query policy: nono why --path <path> --op <read|write|readwrite>
 [nono] Review denied paths
  ↑/↓ move  ·  Space cycle  ·  a grant-all  ·  d deny-all  ·  Enter confirm  ·  Esc cancel

  ▶  grant     ⚠ ~/.ssh  (read dirs)
     grant     ~/.gitconfig  (read+write files)
```

Here nono suggests granting access to `~/.ssh` and `~/.gitconfig`, which were blocked during the session when we tried to access them. Just by selecting an option and pressing Enter, nono directly edits the profile JSON file and adds the selected rule to be granted for future sessions, which is pretty convenient. Note that granting read access to `~/.ssh` is a bad idea, though, and is only shown here to demonstrate the feature. Only grant more permissions if they are really needed.

Credential injection is where nono shines. It supports injecting secrets from various password vaults on the host, including 1Password, Bitwarden, environment variables and custom CLI commands. Credentials can be injected into various locations, including:

- HTTP headers
- HTTP endpoint URL path
- HTTP GET parameters
- HTTP Basic Auth (base64 decode and re-encode)

And the format of credential placeholders can be configured too. This is useful in situations where the agent requires the credential to be in a specific format to be able to login in the first place. For example, GitHub Copilot CLI requires the token to start with "`gho"`. Otherwise, login will fail. Credentials can be scoped to a domain and endpoint, which is a plus.

One of the coolest features of nono is that, not only its proxy supports credential injection in the traditional direction, that means when the agent makes an outgoing request, but it also supports intercepting credentials that are returned in a network response from a server before passing them to the agent. Nono calls this [Sandboxed OAuth Logins](https://nono.sh/docs/cli/features/sandboxed-oauth-logins#sandboxed-oauth-logins). This is super useful when you have to login for the first time with your agent. Typically you would have to type `/login` from inside the sandbox, and if the sandbox doesn't do anything special, you'll end up with credentials stored inside of the sandbox after doing `/login`. But nono can actually intercept this process and securely store the obtained credentials outside of the sandbox, only store a placeholder inside the sandbox, in the format configured, and inject the actual secret when future traffic goes out. This is one of the killer features a sandbox designed to be used with AI coding agents should have. We actually got this setup for GitHub Copilot CLI and made it work with a GitHub Copilot Business account. It worked with the OAuth device code flow.

![Sandboxed OAuth login: the proxy stores the real tokens and only hands placeholder tokens to the agent](https://cdn.prod.website-files.com/67711be5796275bf61eaabfc/6afeef2834eaf82e450f1be9_e131cee3.png)

To run GitHub Copilot CLI with nono with a custom profile called `copilot-custom` and allow read/write to the current directory:

```
nono run --profile copilot-custom --allow-cwd -- copilot
```

Here's the stripped JSON nono profile we used to make that work with only the relevant pieces:

```
{
  "extends": null,
  "meta": {
    "name": "copilot",
    "version": "1.0.0",
    "description": "Copilot CLI profile with example.ghe.com /login support",
    "author": null
  },
  "network": {
    "block": false,
    "allow_domain": [
      "example.ghe.com",
      "copilot-api.example.ghe.com",
      "api.github.com",
      "api.githubcopilot.com",
    ],
  },
  "credential_providers": {
    "github_copilot_ghe": {
      "type": "oauth_capture",
      "token_endpoints": [
        {
          "host": "https://example.ghe.com",
          "path": "/login/device/code",
          "response_fields": [
            {
              "path": "access_token",
              "kind": "opaque"
            },
            {
              "path": "refresh_token",
              "kind": "opaque"
            },
            {
              "path": "id_token",
              "kind": "opaque"
            }
          ],
          "request_body": "auto",
          "request_nonce_fields": [
            "refresh_token"
          ]
        },
        {
          "host": "https://example.ghe.com",
          "path": "/login/oauth/access_token",
          "response_fields": [
            {
              "path": "access_token",
              "kind": "opaque",
              "format": "gho_deadbeef{}"
            },
            {
              "path": "refresh_token",
              "kind": "opaque"
            }
          ],
          "request_body": "auto",
          "request_nonce_fields": [
            "refresh_token"
          ]
        }
      ],
      "api_hosts": [
        "https://api.example.ghe.com",
        "https://copilot-api.example.ghe.com",
      ],
      "inject_header": null,
      "credential_format": null,
      "credential_store": {
        "type": "file_json",
        "path": "~/.github-copilot-ghe/auth.json",
        "phantom_fields": [
          "tokens.access_token",
          "tokens.refresh_token"
        ]
      }
      "helpers": null
    }
  },
  "credential_routes": [
    {
      "name": "github_copilot_ghe_oauth",
      "provider": "github_copilot_ghe",
      "env_var": null,
      "base_url_env_var": null,
      "endpoint_policy": null,
      "upgrades": []
    }
  ],
}
```

‍  
In terms of resource usage limitations, nono supports memory and max process count.

Some downsides include:

- It's OS-level sandboxing, so not the highest level of isolation security in terms of primitive used
- No UDP traffic filtering
- Few configurable process resource usage limits
- Can't edit list of allowed syscalls (hardcoded)
- On Windows, it only works via WSL2, no native support
- Can't filter traffic by HTTP GET request params

Overall, nono is a very impressive open source project with clear documentation, many features and serious maintainers behind it. It's easy to install, configure and use. It hasn't reached v1.0 yet so things may still change before that, but at the current pace of releases it shouldn't be long before it becomes stable. It's open source and feels pretty stable already. The company behind nono also offers a [paid service](https://nolabs.ai/enterprise) that adds governance features. This is a solid candidate.

Because of those reasons we gave nono a security score of 4/5, which is not the highest, but it's a pretty good tradeoff for what you get.

## Docker Sandboxes

Despite what one may think at first because it's made by Docker, [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/) (`sbx`) doesn't isolate agents in Docker containers, but it runs each agent [in its own microVM](https://www.docker.com/blog/why-microvms-the-architecture-behind-docker-sandboxes/). The MicroVM comes with a full Docker daemon inside in case you'd like to run containers inside it. In terms of user experience, we found that it's the most polished of the four tools. The first start takes about 10 seconds because images need to be pulled, but then the next start just takes a couple seconds.

Here, there's no need to install coding agents on the host. Docker Sandboxes provides the agent through OCI images. Many agents and tools are supported through sbx "kits", and those can be browsed on [Docker Hub](https://hub.docker.com/search?type=sbx_kit). Kits support inheritance with mixins. Custom kits can be defined as YAML files. In addition to policy configuration, most kits provide sandbox awareness instructions in an AGENTS.md file.

Since MicroVMs come with their own entire dedicated filesystem, bind mounts are what's really important here and of course, this is supported. Multiple folders can be mounted in a sandbox either read-only or read/write. For example:

```
sbx run copilot ~/project /path/to/docs:ro /path/to/other
```

It's also possible to create a mountless sandbox, with no host directory mounted. Regardless of whether any mounts exist, it's possible to manually copy files between the host and the sandbox with `sbx cp <source> <dest>`.

Docker Sandboxes comes with a really polished TUI that can be started just by running `sbx` or `sbx tui`.

![sbx TUI adding a new rule](https://cdn.prod.website-files.com/67711be5796275bf61eaabfc/6afeef2834eaf82e450f1bec_5e815f25.png)

Docker Sandboxes Terminal UI (TUI)

From there, one can create and manage sandboxes, and edit network rules. A really nice feature is live network rule approval. Whenever a sandbox makes a network request and it gets denied, a corresponding rule appears in the Network rules tab in the TUI and it can be approved with the press of a single button. Restart isn't required for network rules to take effect. A default list of domains is allowed and the rest is denied. Of course, that list can be modified. Filesystem rules can be viewed in the TUI but cannot be modified from there.

Network can be filtered by host, port, HTTP method, path and query parameters. UDP support is experimental and currently disabled by default, but it exists. When enabled, it's possible to allow/block UDP traffic per host and port.

SSH support can be enabled by running `sbx setup ssh` once. This edits `~/.ssh/config` so that a regular SSH client can then be used to SSH into a sandbox with `ssh sandbox-name.sbx`. This works by setting the SSH`ProxyCommand` to `sbx ssh proxy %n` for all hosts ending in `.sbx`. One example where this can be useful is when using Cursor in its GUI version (VSCode based) and remote SSH is configured to run agent commands remotely over SSH and that remote machine is a Docker Sandboxes sandbox. This way the Cursor GUI can run on the host, unsandboxed, but commands run over SSH in a sandbox.

Another feature that exists is an LLM proxy that can be configured to send a request to another LLM provider if the request exceeds the main provider's context size. This is nice to have.

Docker Sandboxes also provides an MCP gateway which is enabled by default for sandboxes. The CLI can be used to dynamically add MCP servers which appear through the gateway. This way, MCP servers can be configured once and passed to various sandboxes in a centralized way. In addition to this dynamic mode, it's also possible to use static mode, which basically pre-loads the list of MCP servers on the sandboxed agent statically and, in that mode, cannot be changed at runtime.

Credential injection is also supported and credentials are scoped to a domain name. They can be injected into HTTP headers and Basic authentication is also supported (base64 decode, inject and re-encode). Options here are more limited than with nono regarding where secrets can be injected. It's still possible to inject secrets from various sources, including 1Password, AWS Secrets Manager and custom CLI commands. Secret placeholders can be custom formatted via the `format` field in a kit YAML file. Sandboxed OAuth logins appear to be supported according to the official Cursor kitv3 documentation, but we haven't tested this feature.

Processes restrictions include: CPU, memory, USB device passthrough (select which device to allow with a selector) and disk size (at sandbox creation time, via setting or env var).

It is possible to view network proxy logs. However, filesystem accesses aren't logged. There are also audit logs that track every policy decision that was taken. These are saved as .jsonl files locally in `~/.local/state/sandboxes/sandboxes/auditkit`.

Some paid services include governance features, MCP access policies, and cloud sandboxes, to name a few. With the latter, sandboxes can easily be moved between local and cloud.

Some downsides:

- It's closed source and the GitHub repository only contains binary releases
- A Docker account is required to use Docker Sandboxes
- Filesystem policies are part of the paid organization governance features
- Host folder bind mounts can't be changed on a running sandbox. It needs to be restarted for changes to apply
- Filesystem logs are not supported yet
- Filesystem rules are not configurable except for what gets mounted. Since this is in a MicroVM, this isn't a huge downside. This would have been a different story if OS-level isolation was used. On the other hand, it appears that restricting what host directories can be mounted is a paid governance feature
- No rollback/snapshot support. However it's possible to mount in `--clone` mode and let the agent work on a copy of the local git repo
- No memory zeroization for secrets on exit (at least not mentioned in the docs)

Since MicroVMs are used for isolation, this provides a high level of security and the tool is backed by a well known organization. However, Docker Sandboxes is not the tool that provides the most network traffic filtering features out of the four evaluated tools, and the project hasn't reached v1.0 yet. Additionally, multiple security issues have been fixed and disclosed in the release notes recently. Also, the tool is closed source so it makes it more difficult to audit. For the aforementioned reasons, we gave Docker Sandboxes a security score of 4.5/5. This is a strong candidate that is already usable and that one should keep an eye on.

## Microsandbox

[Microsandbox](https://github.com/superradcompany/microsandbox) is built by Super Rad Company and uses MicroVMs for isolation. It's open source and written in Rust on top of libkrunfw. It supports running any OCI image and comes with SDKs for various languages to manage sandboxes programmatically.

Microsandbox is more of a general sandboxing solution, not specifically tailored for coding agents. Other use cases they showcase include media processing (for example, transcoding untrusted video) and CI/CD pipelines. There are no pre-built profiles, packs or kits for popular coding agents. However, the docs provide [some examples](https://docs.microsandbox.dev/how-to/agents/opencode) of how to run popular agents including OpenCode, Claude Code and Pi, but there are no examples for GitHub Copilot CLI or Cursor CLI. The command to run it is significantly longer than for the other tools we evaluated. For example, to create a sandbox with OpenCode, wec an run the following command once, which takes a few seconds:

```
msb run -t --name opencode-test --replace \
  --cpus 2 --memory 2G --root-disk 4G \
  --mount-dir ./my-project:/workspace:rw \
  --workdir /workspace \
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g opencode-ai@1.18.4 &&
    exec opencode
  '
```

This creates a sandbox named `opencode-test` based on a `node` OCI image, on top of which opencode is installed. Later, one can run opencode inside this sandbox while keeping all the parameters passed at creation time with:

```
msb exec -t opencode-test -- opencode
```

Microsandbox provides the `msb install` and `msb uninstall` subcommands which can be used to create shell commands that start a specific sandbox directly. This can help reduce typing effort.

The sandbox lifecycle is pretty neat and supports scheduling changes to a sandbox config. For example one can schedule the CPU or memory limits to change after the next restart or force it immediately and cause an immediate restart. Full logs of the sandboxed process' stdout and stderr, plus the sandbox lifecycle events (start, stop) can be viewed.

The documentation is great and it offers some of the best resource limits configuration options: CPU, memory, root disk size, max open files, max file size, mount options, and many more. Labels can be assigned to sandboxes. Those labels can later be used to group sandboxes by specific labels for certain operations such as for showing metrics.

Network can be filtered by domain, IP, CIDR range, port and protocol, but not by HTTP path. DNS rebinding protection is enabled by default and requests to major cloud providers metadata endpoints are denied by default.

Credential injection is supported from environment variables and direct value sources. Secret placeholder format is configurable and secrets can be injected into various locations:

- HTTP headers (can specify which headers are allowed)
- HTTP GET parameters
- Basic Auth
- HTTP request body

It's also possible to configure what action to take if a secret policy violation occurs (a request includes a placeholder secret to a destination that is not allowed).

Some downsides:

- Credentials can only be scoped to a domain name, not to a specific endpoint
- No log of blocked network requests
- No automatic suggestion of network rules when something gets blocked
- Microsandbox doesn't provide a TUI
- Some important network filtering options are missing

Overall, Microsandbox is a solid general-purpose sandboxing tool that uses MicroVMs for isolation and that just works, but lacks a few important network filtering features such as HTTP path filtering. It hasn't reached v1.0 yet but the team takes security very seriously and has published multiple security advisories on GitHub already. Because of those reasons, we gave Microsandbox a security score of 4/5.

## NVIDIA OpenShell

[OpenShell](https://github.com/NVIDIA/OpenShell) is developed by NVIDIA. It's a heavy-weight project that aims to provide a sandboxing solution for running fleets of agents, for multiple teams in an enterprise scenario (concept of workspaces). It does work locally for a single developer too. OpenShell's architecture relies on a gateway server that must run separately. The OpenShell CLI tool is configured to connect to one or more gateways, and the selected gateway takes care of running sandboxes. This architecture works well for local use but also when a remote cluster is used to run sandboxes. Multiple backends (called "runtimes" or "compute drivers") are supported for isolation: Docker, Podman, Kubernetes, MicroVM and Windows MXC. The MicroVM driver uses KVM on Linux and Hypervisor.framework on macOS. It is still experimental for now. The Windows MXC driver is very early. Being able to choose which sandboxing primitive to use is a big plus that the other tools do not offer, but it adds complexity to the project and more work for its maintainers.

There is no marketplace of profiles, packs or kits for coding agents, but any OCI image or rootfs tar archive can be run in a sandbox. For example, to create a sandbox with OpenCode:

```
openshell sandbox create --name opencode-test --from ghcr.io/anomalyco/opencode:latest -- opencode
```

Then one can start and connect to a sandbox with `openshell sb start <sandbox>` and `openshell sb connect <sandbox>`. SSH integration is also supported and the SSH config block for a specific sandbox can be printed with `openshell sb ssh-config <sandbox>`.

Network can be filtered per binary. For example, `curl` may only reach `example.com` but `git` may reach `github.com`. There are specific filters for MCP traffic: filter by MCP tool name, MCP protocol version and MCP method. Obviously, network traffic can also be filtered by domain including globs, port, IP, CIDR range, HTTP method, path and GET parameters. UDP traffic filtering is not supported.

Credential injection is supported. Credentials can be injected in more locations than with any other tool we tested:

- HTTP headers
- Basic Auth
- HTTP URL path
- HTTP GET parameters
- HTTP Request body
- WebSocket text messages
- AWS SigV4 signing is supported (replace placeholder with actual secret, re-compute signature and replace it)

Credentials can be scoped not just to a domain but also to a specific endpoint, including glob support, which is a plus. Sandboxed OAuth logins aren't supported at this point but there's an open GitHub issue that exists. There's no support for dynamic secret sources such as 1Password or Bitwarden. Note that credentials are called "providers" in OpenShell.

Each change to a sandbox's policy is logged. Policies are versioned and can be rolled back easily. The policy can be dumped to a YAML file, edited and set from a file:

```
openshell policy set my-sandbox --policy policy.yaml
```

Host directories can be bind-mounted using some quite cumbersome JSON syntax on the CLI. This is an area for improvement. Logs are stored in OCSF format and can be sent to an OpenTelemetry collector. Logged information includes network connections, sandbox lifecycle events, filesystem policy decisions, configuration changes, command run inside the sandbox, session duration, and more.

Like Docker Sandboxes, OpenShell comes with a TUI that can be started with `openshell term`.

![OpenShell TUI approving a blocked domain](https://cdn.prod.website-files.com/67711be5796275bf61eaabfc/6afeef2834eaf82e450f1bef_aeef4918.png)

OpenShell TUI

Blocked network requests can be approved while the sandbox is running from the TUI. There's an unofficial web app called [openshell-webui](https://github.com/shaharia-lab/openshell-webui) that may help managing policies and sandboxes in a more user-friendly way.

Resource limits can be configured for: CPU, memory and GPU count. Disk space usage can only be restricted globally on specific drivers, such as the MicroVM driver but can't be set per sandbox. Sandbox labels are also supported, like Microsandbox. Labels can be used to filter sandboxes when listing them, for example.

Overall, OpenShell is an impressive project but that still has a few bugs (sandboxes stuck in "starting" status, installation wasn't straightforward) due to its massive scale and that it is still an early project. It provides many configuration options and features, including a concept of "workspaces" for multiple teams, but also works for single developers.

For those reasons, we gave OpenShell a security score of 4.5/5. This score would probably go up once the project matures, but this is also valid for the other tools.

## Comparison Table

The following table compares the four tools side by side.

| **General** | nono | Docker sbx | Microsandbox | OpenShell |
| --- | --- | --- | --- | --- |
| Backed by | nolabs | Docker | Super Rad Company | NVIDIA |
| Version tested | v0.76 | v0.50.0 | v0.7.11 | v0.1.8 |
| GitHub stars | ~5k | ~400 (releases only) | 9k | 21k |
| Language | Rust | Go | Rust | Rust |
| Open source | Yes | ❌ No | Yes | Yes |
| No account required | Yes | ❌ Docker account required | Yes | Yes |
| Sandboxing primitive | OS-level | MicroVM | MicroVM | Container or MicroVM |
| Platform support | Windows (WSL2), macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux |
| Library / SDK | Yes | ❌ No | Yes | Yes |
| **Filesystem** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Read-only and read-write mounts | Yes | Yes | Yes | Yes |
| Deny a path inside an allowed directory | ❌ No | ❌ No | ❌ No | ❌ No |
| Filesystem Rollback | Yes | No (git clone mode) | No (manual snapshots) | No (policy only) |
| **Network** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Domain and CIDR filtering | Yes | Yes | Yes | Yes |
| HTTP method and path filtering | Yes | Yes | ❌ No | Yes |
| HTTP GET parameter filtering | ❌ No | Yes | ❌ No | Yes |
| Per-command policies | Yes | ❌ No | ❌ No | Yes |
| UDP filtering | ❌ No | ⚠️ Experimental | Yes | ❌ No |
| DNS exfiltration protection | Yes | Yes | Yes | ❌ No |
| DNS rebinding protection | Yes | ❌ No | Yes | Yes |
| Upstream (enterprise) proxy support | Yes | Yes | Yes | Yes |
| **Credential injection** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Scoped to endpoint | Yes | ❌ Domain only | ❌ Domain only | Yes |
| Vault integration | 1Password, Apple Password, Bitwarden, Env vars, Custom CLI commands | 1Password, AWS Secrets Manager, Custom CLI commands | ❌ No | ❌ No |
| Sandboxed OAuth login | Yes | Yes (untested) | ❌ No | ❌ No |
| Memory zeroization | Yes | ❌ No | ❌ No | ❌ No |
| **Process restrictions** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Resource limits | Memory, processes | CPU, memory, disk, USB device selector | CPU, memory, disk size, max open files, max file size, mount options & more | CPU, memory, GPU |
| Custom syscall policy | ❌ No | ❌ No | ❌ No | ❌ No |
| **Dynamic changes and visibility** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Live rule changes | ❌ No | ⚠️ Network only | ❌ No | ⚠️ Network only |
| Suggestions after a block | Filesystem, network | ⚠️ Network only | ❌ No | ⚠️ Network only |
| TUI | ❌ No | Yes | ❌ No | Yes |
| Logs | Network, tool calls, file changes | Network | Lifecycle, process output | Network, lifecycle, filesystem, policy change |
| **Agent support** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Coding Agent profiles marketplace | 15+ | 20+ | ❌ Examples only | ❌ Examples only |
| Sandbox awareness for the agent | Yes | Yes | ❌ No | ❌ No |
| Agent must be installed on host | Yes | ❌ No | ❌ No | ❌ No |
| **Overall** | **nono** | **Docker sbx** | **Microsandbox** | **OpenShell** |
| Security rating | 4/5 | 4.5/5 | 4/5 | 4.5/5 |

## What can still go wrong

A sandbox limits the blast radius of the agent. It doesn't verify the agent's output. A few things can still go wrong:

- **The project directory is writable:** The agent can edit files that may later be used on your host or be deployed to production.
- **Too broad network rules enable exfiltration:** Being able to filter traffic by HTTP method and path helps reduce the attack surface, but not all tools support it. DNS is a great way for an attacker to exfiltrate secrets. DNS resolving should be handled from outside the sandbox, otherwise the door is open for exfiltration.
- **Secrets inside the project are readable:** None of the four tools can deny access to a single file inside an allowed directory, so a `.env` file that contains secrets will be visible to the agent. Secrets should never be stored in the project's directory. Use credential injection instead.

## About sandboxing GUI apps

Obviously, running GUI applications in a sandbox is more complicated and we found that none of the sandboxing tools we evaluated supports it so far. Even if they did, this would probably extend the attack surface because some extra plumbing is necessary to make that work (display server socket access).

For example, Docker Sandboxes mentions Cursor is supported, but that only means Cursor CLI, not the GUI version in VS Code. `sbx` has an option for graphical applications (`sandboxOptions.display`), which provisions a display socket and is off by default, but it was not tested here and is still probably very early since no example is described in the docs at the time of writing this.

The remote SSH workaround, where the Cursor GUI (or VS Code) runs on the host and the commands run in the sandbox, doesn't sound as secure either, because not all features of the GUI actually run inside the sandbox that way. One example is the web browser in Cursor.

Because of that, using CLI coding agents is actually a blessing, because they're much easier to sandbox and have a smaller attack surface. That's one more reason to use them.

## Conclusion

Sandboxing coding agents is easier now than ever before. The four tools we evaluated cover multiple use cases and offer different tradeoffs:

- **nono** is the fastest, is open source and has the best secrets handling, but shares the host kernel
- **Docker Sandboxes** provides one of the best user experience, if you don't mind having to use a Docker account and using a closed source tool
- **Microsandbox** is a solid general purpose sandboxing solution but with few "AI coding agent" specific features
- **OpenShell** is the enterprise heavy-weight solution that supports multiple sandboxing primitives and that aims to do it all but that is still early

We'd love to have the combined speed of nono with the user experience of Docker Sandboxes and the flexibility and all the features of OpenShell and Microsandbox, but no such tool exists as of today to our knowledge. In the end, the best sandbox is the one that stays enabled. So, pick one and use it. If it's too complicated to setup for you, just turn on your coding agent's built-in sandboxing options, it will be better than no sandboxing at all.

## References

- nono: <https://github.com/nolabs-ai/nono>
- Docker Sandboxes: <https://docs.docker.com/ai/sandboxes/>
- Microsandbox: <https://github.com/superradcompany/microsandbox>
- NVIDIA OpenShell: <https://github.com/NVIDIA/OpenShell>
- OpenAI and Hugging Face [security incident](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- Hugging Face's [disclosure](https://huggingface.co/blog/security-incident-july-2026)
- Trail of Bits, [VMs won't contain cyber-capable agents](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/)
- [Anthropic, Claude Opus 5 system card](https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf)
- [Johann Rehberger, Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)
- [Anthropic, Auto mode as default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)
- [Containers vs microVMs vs OS-level isolators](https://agentpatterns.ai/security/sandbox-runtime-comparison/)
- JetBrains, [Developer Ecosystem Survey 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/)
- Stack Overflow, [2026 Developer Survey, AI Data](https://survey.stackoverflow.co/2026/ai/data)
- CaMeL: [Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)
- Firecracker escapes: [pwn.ai](https://pwn.ai/blog/firecracker-escape) and [Coinspect](https://www.coinspect.com/blog/firecracker-escape/)
- Black Hat USA 2026 AI Summit: [session](https://blackhat.com/us-26/summit-sessions/schedule/index.html?track[]=the-ai-summit#ai-challenge-lab-securing-the-vibes-defending-developer-environments-55924) and [slides](https://tome.one/slides/amiet-hamiel-securing-the-vibes-ai-summit-black-hat-2026-slides.pdf)
- Tools not evaluated: [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox), [sandbox-runtime (srt)](https://github.com/anthropics/sandbox-runtime), [Microsoft MXC](https://github.com/microsoft/mxc), [Gondolin](https://github.com/earendil-works/gondolin), [Capsem](https://github.com/google/capsem)
