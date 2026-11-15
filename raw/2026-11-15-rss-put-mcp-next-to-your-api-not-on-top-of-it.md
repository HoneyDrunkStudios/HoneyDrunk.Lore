---
source: "https://naftiko.io/blog/put-mcp-next-to-your-api-not-on-top/"
title: "Put MCP Next to Your API, Not on Top of It"
author: "Jerome Louvel"
date_published: "2026-11-12"
date_clipped: "2026-11-15"
category: "Software Architecture"
source_type: "rss"
---

# Put MCP Next to Your API, Not on Top of It

Most teams add MCP the same way: take the API server they already run, put an MCP server in front of it, and map each tool to an endpoint. It ships fast. It also leaves you with two layers to run, two contracts to keep aligned, and an extra network hop on every agent call.

There’s a deeper problem. **An MCP server stacked on an API server can only do what that API server can do.** And agents are starting to need things REST or GraphQL were never designed for.

## Stacking adds a hop and a second contract

In the stacked setup, every tool call goes agent → MCP server → API server → upstream systems. The MCP server re-serializes what the API server just serialized, handles its own authentication, and needs its own deployment, logs and on-call.

It also adds a second contract. The API server has an OpenAPI description, and the MCP server has tool descriptions that paraphrase it. When a field changes meaning, both need an update, and usually only one gets it.

## A capability exposes both, side by side

An [Ikanos](https://ikanos.io/) capability is built differently. It declares what it **consumes** (the upstream APIs), the flows it **aggregates** them into, and what it **exposes**. REST and MCP are two adapters in the same `exposes` list. Both reference the same flow with `ref`, so neither one sits in front of the other:

```
capability:
  consumes:
    - import: legacy
      from: ./shared/legacy-consumes.yaml

  aggregates:
  - namespace: crew-resolver
    flows:
      resolve-crew-for-ship:
        description: "Resolve crew member names and roles for a given ship"
        steps:
          # call the upstream APIs, join and map the results once

  exposes:
  - type: rest
    namespace: shipyard-api
    resources:
      ship-crew:
        path: "/ships/{{imo}}/crew"
        operations:
          get-ship-with-crew:
            method: GET
            ref: crew-resolver.resolve-crew-for-ship
      voyages:
        path: "/voyages/{{path}}"
        forward:
          targetNamespace: legacy

  - type: mcp
    namespace: shipyard-tools
    tools:
      get-ship-with-crew:
        description: "Get ship details with resolved crew names"
        ref: crew-resolver.resolve-crew-for-ship
```

The upstream calls, credentials, mappings and step logic are written once. One engine runs them for both adapters. An agent’s tool call goes straight to the flow, with no detour through REST.

## Evolve the API you have, and add MCP in the same move

This also gives you a migration path. Put the capability where your current API server is, and move it over one resource at a time:

- **Not migrated yet:** a REST `forward` proxies the request to the existing API, unchanged. Clients see no difference.
- **Migrated:** the resource is an operation backed by a flow. It can now join several upstream systems, reshape the payload, or fix the naming the old API got stuck with.
- **Ready for agents:** the same flow becomes an MCP tool with one `ref`. No second implementation, no second deployment.

Each step is small and reversible, and each one improves both interfaces at the same time. When the last `forward` is gone, the old API is replaced. MCP arrived along the way, not as a separate project.

## MCP is outgrowing REST and GraphQL

Side by side matters for a second reason: the protocols are drifting apart. MCP now has interactions that REST and GraphQL APIs don’t usually offer:

- **Discovery** is built into the protocol. `tools/list` returns every tool with a description written for a model, from the running server. REST relies on an OpenAPI document published separately, if at all. GraphQL introspection returns a schema, not what each operation is for.
- **Elicitation** lets a server stop mid-call and ask the user a question: which account, confirm the amount, pick a date. Neither REST nor GraphQL has a standard way to ask the caller something in the middle of a request.
- **Tasks** let a long-running call return a handle right away, so the client can check its status, get the result later or cancel it. REST and GraphQL leave that contract to each API to invent.

So a stacked MCP server can’t offer elicitation or tasks. The API server below it has nowhere to put the question, and no task to report on. A capability can, because its flows are not limited by REST. Ikanos support for both is [in review](https://github.com/naftiko/ikanos/pull/950): an `elicit` step pauses a flow and asks through MCP, and a flow marked `mode: task` runs as a durable MCP task that survives a restart. Over REST, the same flow answers `501 Not Implemented` and names the step that needed input. The gap is real, and it shows up in the engine itself.

That’s why we think **MCP will become the main interface of the agentic era**, with REST and GraphQL staying alongside it for apps and partners that need them. Stacking MCP on an existing API limits the newer protocol to what the older one can do. Putting them side by side lets each protocol use everything it has.

## The takeaway

- Stacking MCP on an API server adds a hop, a second contract and a second deployment.
- An Ikanos capability exposes REST and MCP side by side, over the same `consumes` and the same flows.
- Use `forward` to take over an existing API server one resource at a time, and add an MCP tool for each flow as you go.
- Built-in discovery, elicitation and tasks have no standard REST or GraphQL equivalent. A stacked MCP server can’t offer elicitation or tasks. A capability can.
- As agents rely on those features, MCP becomes the main interface, and REST one of its siblings.

## Further reading

- 📄 [The Capability Is the Product](https://naftiko.io/blog/the-capability-is-the-product/)
- 📄 [From API-led to Capability-led Connectivity](https://naftiko.io/blog/from-api-led-to-capability-led-connectivity/)
- 📄 [Hire a Capability to Get the Job Done](https://naftiko.io/blog/hire-a-capability-to-get-the-job-done/)
- ⚙️ [Ikanos](https://ikanos.io/) · 🧪 [Playground](https://shipyard.naftiko.io/ikanos/playground/) · 📖 [Documentation](https://shipyard.naftiko.io/ikanos/latest/)
