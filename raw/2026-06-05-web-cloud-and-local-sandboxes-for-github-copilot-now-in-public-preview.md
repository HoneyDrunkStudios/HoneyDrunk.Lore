---
source: "https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/"
title: "Cloud and local sandboxes for GitHub Copilot now in public preview"
author: "Allison"
date_published: "2026-06-02"
date_clipped: "2026-06-05"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Cloud and local sandboxes for GitHub Copilot now in public preview

Source: https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/

# Cloud and local sandboxes for GitHub Copilot now in public preview

GitHub Copilot can now run inside secure, isolated sandboxes, both locally on your machine and in the cloud. Sandboxed Copilot experiences provide isolated environments for Copilot’s tool execution locally as well as fully isolated cloud sandboxes hosted by GitHub.

This gives Copilot a safe place to interact with your code, tools, filesystem, and network, all within the policies you define, so developers and enterprises can adopt agentic workflows without giving up isolation or control.

[Why it matters for agentic development](https://github.blog#why-it-matters-for-agentic-development)

Copilot is evolving from an in-editor assistant into an agentic coding partner that runs tools, executes commands, and modifies files on a developer’s behalf. As Copilot takes more actions, developers and enterprises need stronger guarantees around security, isolation, and control.

Agentic development is interactive, stateful, and parallel, and it needs an execution layer built for that reality. Cloud and local sandboxes for GitHub Copilot provide that layer natively, with consistent identity, governance, and policy controls built in. As AI agents become a larger part of the software development lifecycle, secure execution environments become foundational infrastructure, and sandboxes provide that layer for Copilot.

[Local sandboxes for GitHub Copilot](https://github.blog#local-sandboxes-for-github-copilot)

Inside any Copilot session, enable sandboxing with `/sandbox enable`

. Shell command execution initiated by Copilot for that session runs with restricted access to your filesystem, network, and system capabilities, so you can experiment with agentic workflows while staying in control of what Copilot can touch on your machine. Local sandboxing is built on [Microsoft MXC technology](https://www.npmjs.com/package/@microsoft/mxc-sdk) for a consistent isolation experience across macOS, Linux, and Windows. Enterprise teams can also centrally configure and enforce local sandbox policies through Microsoft Intune and other MDM platforms. Local sandboxes are included in the standard GitHub Copilot seat.

This release focuses on isolating shell command execution initiated by Copilot, laying the foundation for broader CLI-level isolation as agentic workflows mature.

[Key use cases developers and teams can unlock](https://github.blog#key-use-cases-developers-and-teams-can-unlock)

- Safely run agent-generated code on your machine through isolated tool execution, without giving Copilot unrestricted access to the filesystem, network, or system.
- Standardize isolation across macOS, Linux, and Windows with a consistent sandboxing experience built on Microsoft MXC.
- Apply enterprise policy to local Copilot execution by centrally configuring and enforcing sandbox policies through Microsoft Intune and other MDM platforms.

[Cloud sandboxes for GitHub Copilot](https://github.blog#cloud-sandboxes-for-github-copilot)

Launch a fully isolated, ephemeral Linux sandbox hosted by GitHub directly from Copilot with `copilot --cloud`

. Each session inherits your existing Copilot cloud agent policies, so the security controls your org already trusts apply on day one with no additional setup.

[Key use cases developers and teams can unlock](https://github.blog#key-use-cases-developers-and-teams-can-unlock)

- Run Copilot tasks in fully isolated cloud environments for stronger security boundaries around agent execution.
- Continue Copilot sessions across devices, picking up where they left off regardless of where a session was started.
- Offload compute-intensive workflows and run multiple Copilot tasks in parallel without consuming local resources.

[Get started](https://github.blog#get-started)

To get started, read the docs for sandboxes for GitHub Copilot in [local environments and cloud environments](https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes?utm_source=changelog-sandbox-docs&utm_medium=changelog&utm_campaign=msbuild-2026), see [pricing](https://github.com/pricing?utm_source=changelog-sandbox-pricing&utm_medium=changelog&utm_campaign=msbuild-2026) for sandboxes for GitHub Copilot in cloud environments, or join the discussion in the [GitHub Community](https://github.com/orgs/community/discussions/197220?utm_source=changelog-sandbox-discussion&utm_medium=changelog&utm_campaign=msbuild-2026). Learn more at our [Microsoft Build demo session](https://build.microsoft.com/en-US/sessions/DEM305?source=sessions).
