---
source: "https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences"
title: "A2UI 1.0: Build delightful, fast, reliable, agentic experiences"
author: "Vishal Motwani; Google A2UI Team"
date_published: "2026-11-11"
date_clipped: "2026-11-12"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# A2UI 1.0: Build delightful, fast, reliable, agentic experiences

NOV. 11, 2026

[Vishal Motwani](https://developers.googleblog.com/search/?author=Vishal+Motwani)
A2UI PM

[Google A2UI Team](https://developers.googleblog.com/search/?author=Google+A2UI+Team)

- [Twitter](https://twitter.com/intent/tweet?text={url} "Share on Twitter")
- [Mail](mailto:[redacted-email]?subject=Check%20out%20this%20site&body=Check%20out%20{url} "Send via Email")

![01_cover](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/01_cover.original.png)

User interactions with agents today are where computers were in the terminal era: capable, and answering almost everything in text. Users can ask an agent for anything by typing or talking, and what comes back is usually a wall of text, a poor way to compare three products or edit and approve a detailed plan.

Today**,** we're releasing A2UI 1.0, the first stable version of our open protocol for generative UI. It lets AI agents answer with interactive screens, such as a form to confirm or a chart. Developers can use it now with open-source renderer SDKs for the web, Android, and iOS and agent SDKs for Python, TypeScript, and Dart. Companies such as [Atlassian](https://www.atlassian.com/), [Alation](https://www.alation.com/), [Bloomberg](https://www.bloomberg.com/), and [ByteDance](https://www.bytedance.com/) are already building with it.

With A2UI, the agent describes what to show, and every app draws the UI with its own native components. The application receives A2UI messages and each app renders the content securely and at native speed. Users get the same low latency, high trust, and complete native fidelity whether they reach a company's agent in its own app or in a third-party AI assistant that hosts MCP apps, such as Gemini or Claude.

## Why A2UI

- **Personalized in the moment.** Your agent constructs a UI that adapts to each user's unique needs and preferences.
- **Native to your brand.** Agents use your design system and nothing else. They place and configure only the components you register.
- **Fast, reliable, and secure in production.** LLMs compose UI with [A2UI Express](https://a2ui.org/concepts/inference-formats/) or with “system one” decision models that pick components instead of writing text. A2UI reliably binds to your data and child components on the server, so sensitive values never reach the model, and the app streams in the UI as the agent works.

## What developers can build with A2UI

You wake up sick. Getting through the morning takes six apps: book a video visit, move your meetings, tell your team, turn on an out-of-office reply, ask your partner to do school pickup and order soup. Ask a text-only agent instead, and you get a numbered wall of text, then round after round of “which ones?”. A2UI won't handle your sick day, but it gives developers the framework to build an agent that can. That agent could answer with one view of all six apps. Changing your plan is a couple of taps instead of another round of messages, and nothing is sent until you confirm.

The same sick day three ways. The third app shows the kind of agent interfaces developers can build with A2UI (illustration).

The same agent output works on any screen. Ask an agent to “move dinner with Priya to Friday”, and it can answer with one view that lines up your calendar, open tables from a restaurant booking app and prices from a rideshare app, so the time that works for everyone is obvious. The developer builds that view once with A2UI, and it renders natively on your phone and on your laptop.

The same request answered in text and with A2UI, then the same view on a laptop (illustration).

In both examples, A2UI is the framework that simplifies building these experiences across platforms. Developers build the agent and choose the platforms it works with. A2UI gives them the protocol the agent uses to describe each view, a way to combine components from different apps in one view, and renderers that draw it natively on the web, Android, and iOS.

New to A2UI? Start with the [A2UI Playground by CopilotKit](https://go.copilotkit.ai/a2ui-playground) or check out [industry examples](https://a2ui.org/get-help/).

[![Screenshot 2026-11-04 at 3.06.30 PM](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Screenshot_2026-11-04_at_3.06.30PM.original.png)](https://www.google.com/url?q=https://go.copilotkit.ai/a2ui-playground&sa=D&source=docs&ust=1794419044655394&usg=AOvVaw2AXGlAcczdJWejsv3nzO-g)

A2UI Playground by Copilotkit

## What's new in 1.0

- **A stable protocol.** Version 1.0 adds bidirectional function calls, so a flight or reservation picker can check availability on the spot. The protocol also adds support for accessibility and extensions for any additional metadata.
- **Renderer libraries for major platforms.** Open-source renderers draw A2UI screens with [React](https://www.npmjs.com/package/@a2ui/react), [Angular](https://www.npmjs.com/package/@a2ui/angular), and [Lit](https://www.npmjs.com/package/@a2ui/lit) on the web; [Flutter](https://pub.dev/packages/a2ui_flutter) on mobile, web, and desktop; [SwiftUI](https://github.com/a2ui-project/a2ui/tree/main/swift/swiftui) on iOS and [Jetpack Compose](https://developer.android.com/jetpack/androidx/releases/a2ui-compose) on Android (currently v0.9.1, and v1.0 coming soon). The web and Flutter renderers also work inside [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview), so A2UI screens can appear in AI assistants that support MCP Apps, such as [Claude](https://claude.com/blog/interactive-tools-in-claude) and [Gemini](https://cloud.google.com/blog/topics/developers-practitioners/devs-guide-to-mcp-apps-in-gemini).
- **Fast, reliable UI generation with A2UI for Agent SDKs.** New SDKs for [TypeScript](https://www.npmjs.com/package/@a2ui/agent) and [Dart](https://pypi.org/project/a2ui-agent-sdk/) along with [Python](https://pypi.org/project/a2ui-agent-sdk/), simplify integration with your agent harness or framework by generating skills, translating messages, and correcting errors. Swappable inference formats reduce latency, and in Python, [A2UI Macros](https://a2ui.org/guides/macros/) add programmatic component expansion and data binding.

## Teams building with A2UI today

### **Atlassian**

Atlassian is bringing A2UI to Jira, where teams can [assign work items to AI agents](https://www.atlassian.com/software/jira/dev). When an agent needs a follow-up from the team to finish a work item, such as a missing detail or a decision, it asks with an interactive card in the work item, and the team answers right there in Jira.

![06_atlassian_jira](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/06_atlassian_jira.original.png)

Figure 1. An agent asks the team for a follow-up inside a Jira work item.

### **Alation**

The Alation Intelligence Operating System (AIOS) builds its feeds using A2UI: metric cards, charts, and more. Each chart can show the SQL query and data behind it. Ask Claude for a feed about profitable products, and the feed renders in the conversation using A2UI to render metric cards, charts, and custom components. The same feed with the same information can be viewed directly inside Alation with a nearly identical layout.

> “The Alation Intelligence Operating System (AIOS) brings artifacts with data, charts, and insights directly to where teams work with transparency about where each figure comes from. A2UI provides the interactive UI scaffolding that makes these artifacts feel like high-touch, tailored applications, whether they are used in Alation or in the AI Assistants our customers already use.”  
>   
>  - ***GT Volpe, Vice President of Product Management at Alation***

![07_alation](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/07_alation.original.png)

Figure 2. The same Alation feed rendered in Claude (left) and in Alation's Data Products App (right).

### **ByteDance**

ByteDance [released an A2UI renderer for Lynx](https://lynxjs.org/react/genui/a2ui.html), its cross-platform framework, in June 2026. Lynx keeps streamed screens smooth and ships a default set of components built on its `lynx-ui` library. In the [Lynx GenUI Playground](https://lynx-stack.dev/genui/#/a2ui), you can watch A2UI messages rendered natively, for example, as a two-day trip planner for Kyoto. Lynx supports A2UI 0.9 today and is adapting to 1.0 with the A2UI team.

> “A2UI is headed in the right direction: it separates how a model produces an interface from how an app renders it. Swappable inference formats and macros keep generation efficient, and even LLMs can be swapped for a System 1 model. In our playground, a decision model like Jev picks components and values instead of writing text, and then the SDK builds the A2UI screens that Lynx renders natively.”  
>   
>  - **Shouqun Liu** Engineering Lead for Lynx at ByteDance

![08_bytedance_lynx](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/08_bytedance_lynx.original.png)

Figure 3. In the Lynx GenUI Playground, A2UI messages (left) render natively in Lynx as a Kyoto trip planner (right).

## Inside Google

### **Gemini Notebook**

Ask Gemini Notebook for a slide deck and it replies with a card that asks two things: presenter slides or a detailed deck, and which topics to focus on. A review card follows with the format, focus, and visual style, which you can edit before it generates the deck. The same cards guide Video Overviews on the web and on mobile.

![gemini-notebook-blog-figure](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/gemini-notebook-blog-figure.original.png)

Figure 4. Gemini Notebook's options card (left) and review card (right).

## Inside Gemini

Organizations can register their own agents that respond with A2UI. Gemini renders those responses using the components in its A2UI component gallery, and supports A2UI 0.9.1 today. The Google Cloud documentation covers [registering an agent](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent) and hosting one on [Cloud Run](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/tutorial-host-agent-cloud-run).

Several other Google teams, including some behind our largest products, are building features with A2UI.

Several other Google teams, including some behind our largest products, are building features with A2UI that haven’t launched yet. We’ll share more as they ship.

## A2UI and MCP Apps

A2UI and MCP Apps work together. Alation already uses both to show its A2UI feeds in Claude. Our June post, [A2UI + MCP Apps](https://developers.googleblog.com/a2ui-and-mcp-apps/), covers three ways to combine them, and the [A2UI in MCP Apps guide](https://a2ui.org/guides/a2ui-in-mcp-apps/) shows how to run A2UI screens inside an MCP App.

## What's next

Jetpack Compose support for 1.0 is coming soon. Agents in [Gemini Enterprise](https://cloud.google.com/gemini-enterprise) can already use A2UI, and we're working on upgrading Gemini Enterprise to A2UI 1.0. The [A2UI roadmap](https://a2ui.org/roadmap/) covers the rest, from design-system primitives that render natively on every platform to official SDK support for decision models like Jev.

## Get started

- Read the docs and try the [quickstart](https://a2ui.org/quickstart/) at [a2ui.org](https://a2ui.org/).
- Pick a renderer: [React](https://www.npmjs.com/package/@a2ui/react), [Angular](https://www.npmjs.com/package/@a2ui/angular), and [Lit](https://www.npmjs.com/package/@a2ui/lit) on the web; [Flutter](https://pub.dev/packages/a2ui_flutter) on mobile, web, and desktop; and [SwiftUI](https://github.com/a2ui-project/a2ui/tree/main/swift/swiftui) on iOS. The [Jetpack Compose](https://developer.android.com/jetpack/androidx/releases/a2ui-compose) renderer supports 0.9.1 today, with 1.0 coming soon.
- Upgrading from 0.9? The [evolution guide](https://github.com/a2ui-project/a2ui/blob/main/specification/v1_0/docs/evolution_guide.md) covers every change.
- File issues and discuss ideas at [github.com/a2ui-project/a2ui](https://github.com/a2ui-project/a2ui)
