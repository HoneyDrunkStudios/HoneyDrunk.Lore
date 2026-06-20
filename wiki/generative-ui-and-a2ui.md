# Generative UI and A2UI

## Decision-useful summary
A2UI v0.9 is Google's framework-agnostic generative UI standard for letting agents declare UI intent against existing component catalogs and design systems. The useful architectural signal is separation of concerns: agents should stream structured UI declarations while clients render with native React/Flutter/Lit/Angular/custom components, enabling portable generative UI without replacing the frontend stack. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]

## Claims
- A2UI v0.9 defines a framework-agnostic way for local or remote agents to communicate UI intent to client applications, allowing generated UI to use an existing component catalog/design system across web, mobile, and other clients. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]
- A2UI v0.9 includes an Agent SDK for Python, shared web-core client library, official renderers/version bumps for React, Flutter, Lit, and Angular, and a community-renderer path. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]
- A2UI's agent-side flow centers on defining a catalog, initializing a schema manager for spec versions, generating A2UI-aware system instructions, running an LLM agent, then parsing/validating streamed UI parts. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]
- A2UI v0.9 adds client-defined functions, client-to-server data syncing, improved error handling, a modular schema, version negotiation, dynamic catalogs, and resilient streaming that incrementally parses/heals LLM JSON. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]
- A2UI is explicitly transport-flexible: the source names MCP, WebSockets, REST, AG UI, and A2A as possible carriers. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]
- The broader generative UI ecosystem is converging around standards/interoperability signals including AG2, A2A 1.0, Vercel json-renderer, Oracle Agent Spec + AG UI + A2UI, and AG-UI middleware. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]

## Typed entities
- standard/protocol: A2UI v0.9
- concept: generative UI
- concept: UI intent
- concept: component catalog
- concept: dynamic catalogs
- concept: resilient streaming
- SDK: A2UI Agent SDK
- library: shared web-core
- renderer: React renderer
- renderer: Flutter renderer
- renderer: Lit renderer
- renderer: Angular renderer
- protocol: MCP
- protocol: AG-UI
- protocol: A2A 1.0
- framework/community: AG2
- product/tool: Vercel json-renderer
- spec: Oracle Agent Spec

## Explicit relationships
- A2UI decouples UI intent from frontend implementation.
- A2UI uses component catalogs and schema validation to constrain agent-generated UI.
- A2UI depends-on client renderers to turn structured agent output into native interface components.
- A2UI can be transported over MCP, WebSockets, REST, AG UI, or A2A.
- Generative UI production readiness depends-on streaming validation, version negotiation, dynamic catalogs, and error handling.

## HoneyDrunk implications
- For agent-driven dashboards or Grid control panels, avoid raw HTML generation; prefer a catalog/schema approach where agents request known components.
- A2UI is worth tracking as a reference for provider-neutral UI contracts, even if HoneyDrunk starts with a smaller internal JSON schema.
- Existing design systems should remain the rendering authority; agents should provide intent and data, not unreviewed frontend code.

## Confidence and quality notes
- Quality posture: decision-usable architectural scouting from a single vendor-authored announcement.
- Weak claims: ecosystem adoption examples are early and may shift quickly.
- Privacy filter: no secrets or unsafe PII copied.

## 2026-06-05 compile additions

### Claims
- OpenAI's Codex Sites preview lets Business and Enterprise users generate and share interactive hosted websites/apps inside a workspace, including dashboards, planners, review workspaces, project boards, galleries, and lightweight tools. confidence: 1 OpenAI source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-codex-for-every-role-tool-and-workflow.md]
- Codex annotations let users select a specific part of a generated site, document, spreadsheet, slide, or code artifact and ask Codex for a localized refinement rather than restarting the whole artifact. confidence: 1 OpenAI source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-codex-for-every-role-tool-and-workflow.md]

### Typed entities
- product/feature: Codex Sites
- feature: annotations
- artifact: interactive hosted site
- artifact: dashboard
- artifact: review workspace
- artifact: project board

### Explicit relationships
- Codex Sites use generated interactive apps as shared decision artifacts rather than static documents.
- Annotations complement generated UI/artifact workflows by localizing human feedback to a selected component or content region.

### HoneyDrunk implications
- For Grid/Lore dashboards, generated sites are useful as a prototyping signal, but durable internal tools should still use governed component/data schemas, source citations, and reviewable code.

### Quality notes
- Codex Sites are preview product claims; availability, hosting boundaries, sharing permissions, and data retention need verification before private HoneyDrunk use.

## 2026-06-20 compile additions: A2UI plus MCP Apps

### Source-backed claims
- Google positions A2UI and MCP Apps as complementary rather than mutually exclusive: A2UI is declarative, host-rendered, secure-by-default, and design-system-native; MCP Apps allow custom HTML/CSS/JS in iframes for complex stateful experiences but can create visual, performance, and security boundaries. Source: `raw/2026-06-20-web-google-developers-blog-a2ui-mcp-apps-combining-the-best-of-declarative.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-20.
- A2UI-over-MCP can serve static/prescriptive UI through MCP Resources and dynamic/templated UI through MCP Tool calls using `application/a2ui+json`; A2UI-over-A2A remains the more open-ended generative option when full conversational context should drive UI construction. Source: `raw/2026-06-20-web-google-developers-blog-a2ui-mcp-apps-combining-the-best-of-declarative.md`. confidence: 1 source, last-confirmed 2026-06-20.
- The hybrid patterns include event/state synchronization where embedded MCP Apps emit key state transitions through a bridge and the host/agent rehydrates native A2UI components without exposing all micro-state to the broader agent context. Source: `raw/2026-06-20-web-google-developers-blog-a2ui-mcp-apps-combining-the-best-of-declarative.md`. confidence: 1 source, last-confirmed 2026-06-20.

### Typed entities
- framework/spec: A2UI
- concept: MCP Apps
- protocol: MCP
- protocol: A2A
- MIME type: `application/a2ui+json`
- URI scheme: `a2ui://`
- concept: embedded resource
- concept: App Bridge
- concept: state synchronization

### Explicit relationships
- A2UI complements MCP by making tool responses renderable through native component catalogs.
- MCP Apps complement A2UI when bespoke client-side logic is necessary.
- A2UI-over-MCP depends-on host support for A2UI resource handling; A2UI-inside-MCP-App can bridge legacy/non-A2UI hosts.

### HoneyDrunk implications
- For Lore/Grid dashboards, model simple forms, tables, charts, and review cards as declarative components; use iframed app surfaces only for high-interaction tools.
- Keep agent-visible state coarse and intentional. Do not stream raw DOM/app micro-state into model context unless it is decision-relevant.

### Quality notes
- Vendor architecture guidance; useful for design direction, but A2UI/MCP Apps interoperability should be validated against real host clients before adoption.
