# Generative UI and A2UI

## Decision-useful summary
A2UI v0.9 is Google's framework-agnostic generative UI standard for letting agents declare UI intent against existing component catalogs and design systems. The useful architectural signal is separation of concerns: agents should stream structured UI declarations while clients render with native React/Flutter/Lit/Angular/custom components, enabling portable generative UI without replacing the frontend stack. [source: raw/2026-05-08-rss-google-developers-blog-a2ui-v0-9-the-new-standard-for-portable-framewo.md]

> superseded-by: [format-specific streaming guidance](#2026-10-28-inference-format-is-separate-from-a2ui-transport-and-streaming); 2026-10-28T10:19:08-04:00. The earlier general streaming recommendation is narrowed by the newer official SDK description: Direct JSON streams incrementally, while Express compilation waits for a complete reply. The prior statement is preserved as historical guidance.

> superseded-by: [A2UI 1.0 release-stage assessment](#2026-11-12-a2ui-10-separates-stable-protocol-from-renderer-and-host-versions); timestamp: 2026-11-12T09:05:18-05:00; reason: the November 11 official announcement supersedes the earlier summary's 0.9 release-stage framing. Preserve its version-specific claims and format-specific streaming limitation; clients are still on mixed versions. [captured source](../raw/2026-11-12-rss-a2ui-1-0-build-delightful-fast-reliable-agentic-experiences.md)

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


## 2026-10-28: Inference format is separate from A2UI transport and streaming

### Typed entities

project: A2UI; library: A2UI Agent SDK; concept: Express inference format; concept: component catalog; project: Jev; project: Apparite.

### Claims and evidence

- Google describes inference formats as prompt-generation and compiler pairs that translate model output into validated A2UI JSON against a component catalog. Express changes the model-facing representation while preserving the transport and renderer contract. confidence: 1 source, last-confirmed 2026-10-28 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-28-rss-fast-reliable-a2ui-with-swappable-inference-formats.md)
- The described Python and TypeScript SDKs stream Direct JSON incrementally but compile Express only after the complete reply. Macros can fetch existing data by identifier; schema validation alone does not establish authorization for those data reads or server actions. confidence: 1 source, last-confirmed 2026-10-28 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-28-rss-fast-reliable-a2ui-with-swappable-inference-formats.md)
- The format evaluation uses 51 tasks on one named model. Apparite's separate decision-model example reports 11 prompts and predefined layout grammar; the agent SDKs do not yet include that decision-model inference format. The advertised speedups are bounded experiments, not universal end-to-end latency guarantees. confidence: 1 source, last-confirmed 2026-10-28 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-28-rss-fast-reliable-a2ui-with-swappable-inference-formats.md)

### Explicit relationships

Express uses a catalog-derived compiler; rendering depends-on standard A2UI messages; controlled layout generation uses predefined grammar. See [[mcp-tool-governance-and-app-surfaces]].

### Decision and quality notes

Official vendor post, dated October 27. Preserve catalog constraints and measure first useful screen separately from completion. Structural validity does not guarantee safe actions, correct data, accessibility, or semantic correctness. Source-specific claims remain provisional; derived summaries add no independent support. Open question: Which UI workload benefits from Direct JSON streaming, complete-reply Express, or predefined decisions after measuring first useful screen, completion, validation failures, accessibility, and action authorization? See [[indexes/gaps]].


## 2026-11-02: CopilotKit transports catalog-based A2UI through AG-UI

### Typed entities

project: A2UI; project: CopilotKit; library: AG-UI; library: Google ADK; library: Zod; concept: component catalog; concept: surface identity. file: raw/2026-11-02-rss-build-generative-ui-apps-with-a2ui-copilotkit-agents.md.

### Claims and evidence

- The Google/CopilotKit walkthrough separates A2UI declarations from AG-UI typed-event transport and client rendering. A client catalog maps component definitions and prop schemas to trusted renderers; dynamic configuration can supply the generation tool to the backend. The shown in-memory ADK service is a demonstration configuration. confidence: 1 source, last-confirmed 2026-11-02 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-02-rss-build-generative-ui-apps-with-a2ui-copilotkit-agents.md)
- Bound input paths and button action context carry user values back to the agent, which updates the same surfaceId. Client validation can avoid a model call for invalid input. This does not establish server authorization, durable booking, duplicate-action safety, or a complete application transaction. confidence: 1 source, last-confirmed 2026-11-02 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-02-rss-build-generative-ui-apps-with-a2ui-copilotkit-agents.md)
- The integration describes isolated generation context, validation feedback with retries, and a message fallback when retries exhaust. Incremental rendering depends on the actual generation/transport path and does not reverse the existing Direct JSON versus complete-reply Express distinction. confidence: 1 source, last-confirmed 2026-11-02 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-02-rss-build-generative-ui-apps-with-a2ui-copilotkit-agents.md)

### Explicit relationships

CopilotKit uses AG-UI to carry A2UI; declarative generation depends-on a trusted catalog and compatible renderer. Action safety depends-on server validation and authorization beyond prop schemas. See [[mcp-tool-governance-and-app-surfaces]].

### Decision and quality notes

Official joint tutorial, correlated with earlier A2UI vendor guidance. Keep the October 28 streaming supersession in force. Broad portability, security, and self-healing wording is product scope to test, not a guarantee that any AG-UI backend or schema-valid action is safe. No packages or starter app were installed. Source-specific claims remain provisional; repeated summaries and derived queries add no independent support. Open question: Which pinned A2UI/AG-UI/CopilotKit matrix verifies catalog negotiation, streaming latency, exhausted retries, surface continuity, server validation, and authorized idempotent actions? See [[indexes/gaps]].


## 2026-11-12: A2UI 1.0 separates stable protocol from renderer and host versions

### Typed entities

project: A2UI 1.0; library: A2UI Agent SDK; library: Jetpack Compose renderer; project: Gemini Enterprise; project: Lynx; concept: catalog negotiation. file: raw/2026-11-12-rss-a2ui-1-0-build-delightful-fast-reliable-agentic-experiences.md.

### Claims and evidence

- Google's November 11 announcement calls A2UI 1.0 the first stable protocol release, adding bidirectional function calls, accessibility support and metadata extensions. This updates the release-stage summary; existing 0.9 behavior remains historical version-specific evidence. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-a2ui-1-0-build-delightful-fast-reliable-agentic-experiences.md)
- The same post lists React, Angular, Lit, Flutter and SwiftUI renderers but explicitly keeps Jetpack Compose and Gemini at 0.9.1 and Lynx at 0.9 while upgrades are pending. Protocol stability therefore does not imply every client already implements 1.0. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-a2ui-1-0-build-delightful-fast-reliable-agentic-experiences.md)
- The announcement describes Python, TypeScript and Dart agent SDKs and Python macros for programmatic expansion/data binding, while official decision-model support remains roadmap work. The Dart hyperlink points to the Python package page, so it does not establish a usable Dart package installation path. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-a2ui-1-0-build-delightful-fast-reliable-agentic-experiences.md)

### Explicit relationships

A2UI uses registered component catalogs; portability depends-on protocol/renderer/host version negotiation. MCP Apps uses an embedded renderer, which does not supersede server authorization. See [[mcp-tool-governance-and-app-surfaces]].

### Decision and quality notes

Official release account. Broad native-fidelity, security and sensitive-data language is a design claim, not an audit. Keep the October 28 Direct JSON versus complete-reply Express distinction until a pinned implementation proves a change. Examples illustrate flows rather than establish confirmed external actions. Package availability, accessibility and server authorization remain untested. Source-specific claims remain provisional; recaptures and derived queries add no independent support. Open question: Which pinned A2UI 1.0 renderer/host matrix verifies negotiation with 0.9 clients, SDK package identity, first useful render, accessibility, data minimization and authorized idempotent actions? See [[indexes/gaps]].
