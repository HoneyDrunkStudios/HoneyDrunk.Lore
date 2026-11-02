---
source: "https://developers.googleblog.com/build-generative-ui-apps-with-a2ui-copilotkit-agents/"
title: "Build Generative UI Apps with A2UI & CopilotKit Agents"
author: "Google A2UI Team; Atai Barkai"
date_published: "2026-10-29"
date_clipped: "2026-11-02"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Build Generative UI Apps with A2UI & CopilotKit Agents

![cover-without-title](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/cover-without-title.original.png)

Agent-User Interactions are now evolving from text exchanges to rich UIs. Until recently, most conversations looked like this:

**User:** "Find me a holiday package to Bali in March."  
 **Agent:** (six packages in prose, each with dates, hotel, flights, price)  
 **User:** "The five-night one with breakfast."  
 **Agent:** "Here's the link. You can book it on the operator's site."

Agents could plan the trip, but everything came back as walls of text. They had no standard way to render a selectable list of packages, a map of the destinations, or a date picker to carry you through the rest of the booking, inside the conversation itself.

Generative UI is the layer that lets agents build interfaces at runtime, shaped by what each request needs - giving users a rich, interactive experience. Implementing that takes two pieces: a way to describe the UI and an agentic stack that connects your agent to your application and renders that UI.

* [**A2UI (Agent-to-UI)**](https://a2ui.org/) is Google's framework-agnostic open standard for Generative UI. The agent describes an interface as data, and your application draws it with the components you already have. It's transport-agnostic by design.
* [**CopilotKit**](https://www.copilotkit.ai/) provides the agent-integration stack to integrate with agent frameworks like “LangChain”, “AWS Strands”, “Google ADK”, etc. for building user-facing agentic apps. It provides a toolkit for building rich applications with A2UI protocol, including the chat surface, runtime, and leverages A2UI renderer, across React and Angular. CopilotKit also provides custom A2UI renderers for Vue and Slack.

![any-framework-any-surface](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/any-framework-any-surface.original.png)

## **What is A2UI?**

Generative UI covers a spectrum of approaches, from using predefined higher order components, to enabling your AI agent to have the flexibility to decide how to build the UI.

At the controlled end, you build each component ahead of time, and the agent picks which one to render and with what data. It's brand-safe but it does not allow for deep customization and personalization based on the user’s intent. At the open end, the agent returns a raw UI program written in HTML, Javascript and/or Dart that renders inside a sandboxed iframe. That covers anything you did not plan for, at the cost of a surface that drifts from your design system and executes code a model wrote.

[A2UI](https://a2ui.org/) works through the entire spectrum. It participates in [controlled generation with decision models](https://developers.googleblog.com/fast-reliable-a2ui/) like Typesafe’s Jev and also open-ended code generation that may output A2UI JSON messages. The declarative mode, where agents assemble pre-declared components and functions, is the most popular. A2UI is the framework-agnostic standard for declaring UI intent, so local or remote agents can generate your UI from your existing component catalog using a common language.

* **Security first.** A2UI is a declarative data format rather than executable code. The client keeps a catalog of trusted components, so anything the agent invents outside that set is caught before it reaches the screen.
* **LLM-friendly and streaming.** The payload is a flat list of small JSON messages that reference each other by ID, so the agent emits it incrementally and the client renders components as they arrive.
* **Framework-agnostic and portable.** The same response renders through [React, Lit, Angular, SwiftUI, Jetpack Compose (Android) or Flutter](https://a2ui.org/reference/renderers/) (multi-platform), and through [community renderers](https://a2ui.org/ecosystem/renderers/) for Vue, or even the terminal.

Frontend developers can now ship the building blocks once, and the agent composes them for each request.

The [Basic Catalog](https://a2ui.org/reference/components/) ships 18 general-purpose primitives across layout, display, input, and containers. The agent can compose entirely different interfaces from the same 18 primitives, depending on what the request needs.

![three-primitives](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/three-primitives.original.png)

The Basic Catalog is deliberately sparse, so most production apps [define their own custom catalog](https://a2ui.org/guides/defining-your-own-catalog/). A custom component can be anything your frontend already renders, including a live map the agent fills with coordinates while your renderer draws the route.

![map-genui](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/map-genui.original.png)

## **How A2UI and CopilotKit work together**

CopilotKit is built on [AG-UI (Agent-User Interaction Protocol)](https://github.com/ag-ui-protocol/ag-ui), which supports A2UI payload and provides Agent SDKs across many agentic backends.

Your agent emits A2UI operations. AG-UI carries them to the client as typed events. When the user takes any action, the values are sent back along the same stream.

**A2UI works with any AG-UI compatible agent.** Frameworks like Google ADK, LangChain, Mastra and Strands are all AG-UI compatible, so the setup is identical whichever one your agent runs on.

![cpk-a2ui-agui](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/cpk-a2ui-agui.original.png)

### **Setting up A2UI in your app**

Setup comes down to two things: connecting your agent to CopilotKit, and defining which components the agent is allowed to use.

Using Google ADK as the example, the `ag_ui_adk` package wraps any ADK agent and serves it as an AG-UI endpoint on FastAPI:

```
from fastapi import FastAPI

from google.adk.agents import LlmAgent

from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint

root_agent = LlmAgent(

    name="flight_agent",

    model="gemini-3.8-flash",

    instruction="Help users find and book flights. Call generate_a2ui to show results.",

)

adk_agent = ADKAgent(

    adk_agent=root_agent,

    app_name="flights",

    user_id="demo_user",

    use_in_memory_services=True,

)

app = FastAPI()

add_adk_fastapi_endpoint(app, adk_agent, path="/")
```

Python


On the app side, you register that endpoint with the CopilotKit runtime at `/api/copilotkit`. It's a few lines of standard setup, covered in the [Google ADK quickstart](https://docs.copilotkit.ai/google-adk/quickstart?agent=bring-your-own#setup-copilot-runtime), and it needs nothing A2UI-specific.

A2UI itself turns on from the client, where your components already are. Define what the agent is allowed to draw, map each definition to a renderer, and pass the catalog to the CopilotKit provider.

```
import { CopilotKit, CopilotChat } from '@copilotkit/react-core/v2';

import {

  createCatalog,

  type CatalogDefinitions,

  type CatalogRenderers,

} from '@copilotkit/a2ui-renderer';

import { z } from 'zod';

const catalogDefinitions = {

  FlightCard: {

    description: 'A flight result with airline, times, and stops.',

    props: z.object({

      airline: z.string(),

      departs: z.string(),

      arrives: z.string(),

      stops: z.number(),

    }),

  },

} satisfies CatalogDefinitions;

const catalogRenderers = {

  FlightCard: MyFlightCard, // your React component

} satisfies CatalogRenderers<typeof catalogDefinitions>;

const catalog = createCatalog(catalogDefinitions, catalogRenderers, {

  catalogId: 'flight-catalog',

  includeBasicCatalog: true,

});

<CopilotKit runtimeUrl="/api/copilotkit" a2ui={{ catalog }}>

  <CopilotChat />

</CopilotKit>
```

JavaScript


The `description` goes into the agent's prompt, so the model knows when to reach for `FlightCard` instead of a generic card. The Zod schema validates the props it sends back.

The A2UI configuration can be set up ahead of time on the server, or it can be created dynamically, shipped from the client to the server with the request. The ADK code above used dynamic configuration which is why it used generate\_a2ui without defining it. The [docs](https://docs.copilotkit.ai/google-adk/generative-ui/a2ui) cover both approaches.

That’s the CopilotKit path. You can also consume the event stream directly with `@ag-ui/client` and hand the A2UI operations to any compliant renderer: [@a2ui/react](https://a2ui.org/reference/renderers/), or the Flutter, Lit, or Angular equivalent.

### **Building bi-directional A2UI surfaces**

Most agent-generated UI is one-shot. The agent draws something, you read it, and it goes stale the moment anything changes.

**A2UI surfaces are bi-directional and the components are reactive**, which makes multi-step flows possible. Any action the user takes on the interface (picking dates, choosing a flight, entering passenger details) travels back along the same stream, and the agent re-emits the surface from there using those values.

Here is a high-level architecture example of an end-to-end booking flow, with an AG-UI agent on Cloud Run streaming A2UI surfaces to a CopilotKit frontend.

![bi-directional surfaces](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/bi-directional_surfaces.original.png)

Two things make the round trip work: inputs bound to a data path, and a button carrying an action that names which paths to send back.

```
{ "id": "cabin", "component": "ChoicePicker", "variant": "mutuallyExclusive",

  "options": [ { "label": "Economy", "value": "eco" },

               { "label": "Business", "value": "biz" } ],

  "value": { "path": "/booking/cabin" } },

{ "id": "confirm", "component": "Button", "child": "confirm_label",

  "action": { "event": { "name": "confirmBooking",

                         "context": { "cabin": { "path": "/booking/cabin" },

                                      "email": { "path": "/booking/email" } } } } }
```

JSON


Validation runs on the client, so a bad email shows an error inline without a model call. Nothing reaches the agent until the button fires.

Then the client sends the bound values, and the agent re-emits against the same `surfaceId`. That is how the whole flow lives on one surface: flight search, results, passenger details, and confirmation.

## **Benefits of running A2UI over AG-UI**

Every AG-UI integration inherets these benefits, so you don't have to build them yourself:

* **Minimal server-side setup:** the catalog reaches the agent on setup, so registering it on the client is all it takes.
* **Generation in a dedicated sub-agent:** the catalog and protocol rules stay out of your main agent's context window, and the surface streams to the client as the sub-agent produces it.
* **Self-healing output:** invalid generations are caught and the specific errors go back for a correction, so nothing broken reaches the screen.
* **Graceful failure:** when retries are exhausted, the surface resolves to a short message and the conversation continues instead of dying in an error state.

---

## **Get Started**

Create a complete A2UI + CopilotKit application. This creates a starter A2UI application with Copilotkit Agent integration.

```
npx copilotkit@latest create --name my-app --framework a2ui
```

Shell


The [CopilotKit Dojo](https://dojo.showcase.copilotkit.ai/) has runnable A2UI demos: fixed server-side schema, dynamic schema against a custom catalog, and an error-recovery example where an invalid first render heals into a valid one.

* [A2UI Composer](https://a2ui-composer.ag-ui.com/)
* [CopilotKit A2UI Docs](https://docs.copilotkit.ai/generative-ui/a2ui)
* [Use A2UI with Any Agent Framework & Harness](https://a2ui.org/guides/a2ui-with-any-agent-framework/)

Explore how to build Generative UI Agents with **CopilotKit**, or dive into [A2UI documentation](https://a2ui.org/) to learn how to integrate A2UI with any framework of your choice.
