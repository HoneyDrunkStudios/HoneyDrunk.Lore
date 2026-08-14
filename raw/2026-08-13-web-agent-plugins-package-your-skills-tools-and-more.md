---
source: "https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/"
title: "Agent Plugins package your skills, tools, and more"
author: "Kevin Hou; Haoyu Wang; Alan Blount"
date_published: "2026-08-06"
date_clipped: "2026-08-13"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Agent Plugins package your skills, tools, and more

Source: https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/

AUG. 6, 2026

Agent Plugins 1.0.0 is an open, vendor-neutral specification for packaging Agent Skills and MCP servers into portable plugins. It was published by a TSC of Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel. Google is joining that group as a Core Maintainer, represented by Kevin Hou, and we're starting to build support into our own products.

You wrote a skill. You wrote a script or an MCP server to go with your skill. Together they do one useful thing well — they know how to query your reporting database and how to turn the results into the weekly summary your team actually reads.

Then you try to ship it to a second client.

The skill is fine. The MCP server is fine. But the wrapper around them is not: the directory layout is different, the manifest wants different top-level metadata, the MCP configuration uses a different shape and infers transports differently. So you fork the package, maintain two copies of components that were never different in the first place, and watch them drift.

The core problem isn't the components. It's the manifest.

Agent Skills already gives agents reusable instructions and resources. MCP already connects agents to tools and services. Both are portable on their own. What has not been portable is the box you put them in — and that box is the thing every client had to invent for itself.

Plugin authors shouldn't have to choose between reaching every client and using what makes each client good. They should get both: one predictable structure for the parts that are genuinely the same, and room for each client to keep innovating on the parts that aren't.

This is why we're joining the Agent Plugins as core maintainers, and starting to integrate into our products.

A plugin is a directory. That's the whole idea, and the restraint is the point.

```
reports-plugin/
├── plugin.json
├── skills/
│ └── summarize/
│ ├── SKILL.md
│ ├── scripts/
│ └── references/
├── mcp.json
└── com.example.client/
```


Plain text

Copied

The manifest is two lines of substance:

```
{
"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
"name": "reports-plugin"
}
```


JSON

Copied

Everything else is found at a fixed location. Skills live in `skills/`

, one subdirectory each, in the format the Agent Skills specification already defines. MCP servers are declared in `mcp.json`

, with an explicit type on every entry. A client never has to guess a transport from the shape of a config object, it will work on stdio, Streamable HTTP, or legacy HTTP+SSE.

Notice what `plugin.json`

cannot do. It cannot relocate components, and it cannot declare them inline. There is no discovery path to configure and no precedence order to learn. If `skills/`

isn't there, the client loads what is there and moves on. A `mcp.json`

server that fails to start doesn't take the plugin's skills down with it — the client skips that entry, keeps loading, and reports the failure. Independent components fail independently.

That last reverse-domain directory is the escape hatch. `com.example.client/`

is an extension namespace owned entirely by one client, for hooks, agents, commands, or anything else that client wants to add. Clients that don't recognize it ignore it. The portable core stays small because the non-portable parts have somewhere legitimate to go.

Before you reach for a plugin, ask whether you need one. If you're shipping a single MCP server to a single client, `mcp.json`

on its own is still the simpler answer. If you have a single skill, you don’t need a plugin. Agent Plugins earns its keep when you have components that belong together and need to travel together.

Agent Plugins v1 is a package format and nothing more. It defines no install mechanism, no distribution protocol, no permission model, no sandboxing requirements, no trust or provenance verification, and no user experience. Those are named openly in the project's future considerations, not quietly omitted.

This is the right call. Installation, policy, enterprise controls, and approval UX are quite different across clients like an IDE, a CLI, and a managed enterprise platform. Each agentic application has genuinely different obligations to their users.

Packaging is one job. Discovering and getting a plugin to a user is a different job, and it's worth being precise about which layer does what.

**Find it —****Agentic Resource Discovery****.**An open discovery protocol that lets a client ask "what is available for this task?" and get back matching resources. ARD already treats a Plugin as a first-class agentic resource type, alongside agents, MCP servers, and Skills. It sits entirely before invocation.**Describe it —****AI Catalog****.**The entry format ARD indexes. A proposed change registers`application/agent-plugins+json`

as a known type, so a catalog entry can point at a`plugin.json`

the way an existing entry points at an agent card or`mcp.json`

.**Package it — Agent Plugins.**One directory, fixed locations, portable across clients.**Run it — MCP and Agent Skills.**The execution contracts that were already portable.

Each layer is independently useful and independently adoptable. You can publish a plugin with no catalog entry, catalog a resource that isn't a plugin, and run skills with no plugin at all. Adopting one never obligates you to the next.

Two Google products support the format as of today.

**Agents CLI** packages Google's expert skills for agent building, evaluation, deployment, observability, and publishing, turning any AI coding agent — Antigravity, Gemini CLI, Claude Code, or Cursor — into an expert at agent building and agent ops. Those skills were already distributable. Now they're distributable in a format that isn't ours alone.

**Data Agent Kit** provides a collection of plugins that bring the power of Google Data Cloud directly into your preferred AI coding agent or IDE. Designed for data engineers and developers, it allows agents to seamlessly manage data assets, run queries, and deploy data pipelines. By adopting the Agent Plugins standard, the Data Agent Kit ensures that its rich set of agentic skills and MCP servers—connecting to BigQuery, Spanner, Cloud SQL, and more—are portably available across any compatible client.

We expect to bring Agent Plugins support to more of our products that already work with Skills and MCP servers.

- Build one. Create a directory, add a
`plugin.json`

with a name, write a quick “hello world” instruction to`skills/greet/SKILL.md.`

That's a valid plugin, and it takes about a minute. - Read the docs. The full spec, the compatible clients (more soon)
- Check out the Data Agent Kit Plugins & Agents CLI Plugin

Packaging is unglamorous infrastructure, and unglamorous infrastructure is exactly the kind of thing that should be shared rather than reinvented five times. Agent Plugins is deliberately small in scope, does one thing well, and is open and interoperable; that's why we're backing it.
