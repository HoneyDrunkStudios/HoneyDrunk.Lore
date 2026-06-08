---
source: "https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available/"
title: "Copilot SDK is now generally available"
author: "GitHub"
date_published: "2026-06-02"
date_clipped: "2026-06-08"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Copilot SDK is now generally available

Source: https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available/

# Copilot SDK is now generally available

The [GitHub Copilot SDK](https://github.com/github/copilot-sdk) is now generally available. You can embed GitHub Copilot’s agentic engine into your own applications, services, and developer tools with a stable API and production-ready support.

The Copilot SDK gives you direct, programmatic access to the same agent runtime behind GitHub Copilot—planning, tool invocation, file edits, streaming, and multi-turn sessions, so you don’t have to build your own orchestration layer.

Since entering public preview, the SDK has been used to build everything from CI/CD assistants and internal developer tools to customer-facing AI features.

[Available in six languages](https://github.blog#available-in-six-languages)

**Node.js / TypeScript**:`npm install @github/copilot-sdk`

**Python**:`pip install github-copilot-sdk`

**Go**:`go get github.com/github/copilot-sdk/go`

**.NET**:`dotnet add package GitHub.Copilot.SDK`

**Rust**:`cargo add github-copilot-sdk`

— new at General Availability**Java**: Available via Maven and Gradle. — new at General Availability

[Key capabilities](https://github.blog#key-capabilities)

**Custom tools and MCP**: Register tools the agent can invoke autonomously, connect to Model Context Protocol (MCP) servers, or override built-in tools like`grep`

and`edit_file`

.**Fine-grained system prompt customization**: Edit individual sections of the Copilot system prompt (e.g., identity, tone, tool instructions, and safety rules) without rewriting it from scratch.**OpenTelemetry tracing**: W3C trace context propagation across CLI startup, JSON-RPC calls, session operations, and tool execution.**Flexible authentication**: GitHub OAuth, GitHub Apps, environment tokens, and BYOK for OpenAI, Microsoft Foundry, Anthropic, and other providers.**Cloud and remote sessions**: Create cloud-backed sessions with repository metadata or enable remote session URLs on demand.**Hook system**: Intercept agent behavior at pre/post tool use, session start, MCP tool calls, and permission requests.

[What’s new since public preview](https://github.blog#whats-new-since-public-preview)

- A new Rust SDK that bundles the Copilot CLI binary by default.
- The SDK now offers better support for multi-client workflows, so different clients can contribute tools and permissions to the same session.
- Slash commands and interactive input prompts are now available across all SDKs.
- The API surface is now stable and production-ready after coordinated cleanup based on preview feedback.
- Improved diagnostics for debugging slow or failing connections.

[Pricing and availability](https://github.blog#pricing-and-availability)

The GitHub Copilot SDK is available to all existing GitHub Copilot subscribers, including Copilot Free for personal use, and to non-Copilot users via BYOK.

[Get started](https://github.blog#get-started)

- Read the
[Getting Started Guide](https://docs.github.com/copilot/how-tos/copilot-sdk/getting-started?utm_source=changelog-sdk-get-started-docs&utm_medium=changelog&utm_campaign=msbuild-2026)to build your first Copilot-powered app. - Browse the
[cookbook](https://github.com/github/awesome-copilot/tree/main/cookbook/copilot-sdk?utm_source=changelog-sdk-cookbook&utm_medium=changelog&utm_campaign=msbuild-2026)for practical recipes across all languages. - Explore the
[documentation](https://docs.github.com/copilot/how-tos/copilot-sdk?utm_source=changelog-sdk-docs&utm_medium=changelog&utm_campaign=msbuild-2026)for setup, authentication, and feature walkthroughs.
