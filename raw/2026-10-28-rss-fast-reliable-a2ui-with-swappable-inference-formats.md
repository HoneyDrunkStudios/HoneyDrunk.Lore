---
source: "https://developers.googleblog.com/fast-reliable-a2ui"
title: "Fast, reliable A2UI, with swappable inference formats"
author: "Vishal Motwani; Google A2UI Team"
date_published: "2026-10-27"
date_clipped: "2026-10-28"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Fast, reliable A2UI, with swappable inference formats

Source: https://developers.googleblog.com/fast-reliable-a2ui

![00-header-1600x900 (1)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/00-header-1600x900_1.original.png)

We've heard your concerns about the speed of A2UI and generative UI experiences: people wait while the model generates each screen. This release gives you levers to make that faster, so you can choose the trade-off that fits each screen.

With this release, we’re happy to introduce swappable inference formats and share examples on leveraging decision models with A2UI, which help building faster and more reliable generative UI experiences. Using our new A2UI Express as an inference format you can reduce latency by up to **3x**, and up-to **80x** using decision models like Jev to make layout decisions. Express requires up to 3x fewer tokens to generate the same kinds of UI compared to Direct JSON. We'll dive into the details in this blog post.

---

A2UI is an agent-optimized protocol for generative UI, where a client advertises a catalog of trusted components as a contract, an agent sends A2UI messages describing a bespoke user interface composed from that catalog, and the client's renderer draws the UI (see [Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)).

Initially agents generated A2UI JSON transport messages directly, every curly brace and nested element. It turns out that generating JSON trees constrained by a complex JSON schema is slow and error-prone for LLMs. This coupled A2UI to LLMs, which output text, and made it difficult to integrate faster System One decision models.

Now agents can generate **A2UI Express**, an intermediate format optimized for inference speed and accuracy, and rely on deterministic code in A2UI's Agent SDKs to translate it into the JSON-based transport protocol. Agent builders are also free to swap in any other DSL and its associated compiler for any special use-cases, and our A2UI Agent SDK(s) make it compatible with transports and renders.

The format the model generates is what we call *inference_format*. You set it with one argument when you create the generator. The SDK generates the prompt instructions for that format and compiles the model's reply into standard A2UI messages. This post covers how the swap works, why we developed A2UI Express as the new default inference format, and how a decision model can build screens from layouts you define in advance.

![01-intro-rendering-format](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/01-intro-rendering-format.original.png)

## **Two things no longer true about A2UI**

![Gemini_Generated_Image_3c13f83c13f83c13](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Gemini_Generated_Image_3c13f83c13f83c13.original.jpg)

## **How swappable inference formats work**

An inference format has two parts, and the SDK generates both from your catalog's JSON schema. A prompt section teaches the model the format's syntax, and a compiler compiles the model's reply into validated A2UI messages. Because both come from the schema, a format can't describe a component or property that your catalog lacks.

You choose the format with one argument when you create the generator:

```python
from a2ui.processor import A2uiGenerator, CatalogConfig

from a2ui.inference_formats import ExpressFormatFactory

catalog = CatalogConfig.from_path("catalog.json")

generator = A2uiGenerator(

    [catalog],

    examples=few_shot_examples,  # written once as A2UI JSON

    inference_format_factory=ExpressFormatFactory(),

)

processor = generator.create_processor(renderer_capabilities)

system_prompt = f"{instructions}\n\n{processor.prompt_snippet}"

parts = processor.parse_response(model_reply)  # text parts + validated A2UI messages
```

Python

![02-how-it-works-swap](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/02-how-it-works-swap.original.png)

A2UI Express is available in the Python agent SDK ([a2ui-agent-sdk](https://pypi.org/project/a2ui-agent-sdk/) 0.9.0 on PyPI), in the TypeScript agent SDK ([@a2ui/agent](https://www.npmjs.com/package/@a2ui/agent) on npm), and in the Dart SDK ([a2ui_agent](https://pub.dev/packages/a2ui_agent) 0.0.1-wip004 on pub.dev). In TypeScript, you pass `new ExpressFormatFactory()` as the generator's third argument. The Python and TypeScript SDKs can both stream Direct JSON chunk by chunk, and they compile Express from the complete reply.

## **Express: the same screens in a third of the tokens**

Express writes one statement per line, in a style close to Python. Each line assigns a component to a variable, and the variable name becomes the component ID. Arguments are positional: the compiler maps them to property names in the order your catalog schema declares them, and _ skips one. $/title binds a value to the data model, and `Event("accept")` declares a server action. This is the A2UI gallery's notification card in Express:

```plaintext
surface("gallery-notification-permission")

$/description="Get alerts for order status changes"

$/icon="check"

$/title="Enable notification"

root=Card(main_column)

main_column=Column([icon, title, description, actions], _, "center")

icon=Icon($/icon)

title=Text($/title)

description=Text($/description, "body")

actions=Row([yes_btn, no_btn], "center")

yes_btn_text=Text("Yes")

yes_btn=Button(yes_btn_text, _, Event("accept", {}))

no_btn_text=Text("No")

no_btn=Button(no_btn_text, _, Event("decline", {}))
```

Plain text

![03-express-same-card](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/03-express-same-card.original.png)

Swappable Inference formats including A2UI Express also work with macros in the Python agent SDK, which help when a screen shows data your systems already hold. The model writes a call with only an ID, such as `OrderStatus("ord_42")`, and your macro fetches the order and fills in the values, so every value on screen comes straight from your data. The [macros README](https://github.com/a2ui-project/a2ui/blob/main/python/a2ui_agent/src/a2ui/transformers/macros/README.md) shows the setup.

## **How we devised A2UI Express**

Customer feedback uncovered latency and accuracy issues with direct JSON generation. To fix this, we started devising a new inference format. We experimented with four options:

- **Direct JSON**: This was our existing baseline that we launched with back in December 2025.
- **Express**: The final `python` syntax inspired format that we picked as the new default.
- **Atom**: Writes Lisp-style S-expressions with no assignments and no closing tags.
- **Elemental**: Writes HTML with custom elements, betting on how well models already write HTML.

We ran all four formats through the same 51-task eval on gemini-3.5-flash and compared them for thinking modes: on and off.

![04-how-we-chose-express-eval](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/04-how-we-chose-express-eval.original.png)

We observed that Express inference format works just as well even with thinking off; which can give you the fastest inference times when working with A2UI Express.

## **Controlled generation with Jev**

Some screens have a known shape, such as a settings page, a checkout or a confirmation. For those, the model doesn't need to design a layout. It needs to choose among layouts you have already defined, and a different kind of model is built for that. For this, you would not need the full expressivity provided by A2UI Express.

[Jev](https://docs.typesafe.ai/), from TypeSafe, is what is called a *System One model*, built to make fast, structured decisions that code can use directly. Jev doesn't generate text or JSON. You send it a state and a set of typed questions, and it answers each one with calibrated probabilities. A question can ask whether a statement is true (Noul), which option from a list fits (Choice), or how something scores on a rubric (Score). Jev answers many questions in one request, in roughly 100 to 300 ms.

[Apparite](https://github.com/dglazkov/jev2ui)(jev2ui), an open-source design tool, shows one way to connect a System One model to A2UI. Jev decides the structure of each screen, code builds the A2UI components from those decisions, and a small model, gemini-3.5-flash-lite, writes only the text. The questions live in a Markdown grammar written ahead of time. A blockquote asks a question, and the bullets are its options, each with criteria. This block from `grammar/screen.md` decides which control a settings row gets:

```plaintext
#### row_control (of each row in rows, within each group in groups)

Material: a switch for one on/off setting that takes effect at once. HIG: a disclosure indicator for a row that opens another page.

> `{row}` is a row in the supplied screen and section. Grouped rows can represent content, navigation, settings or actions; use their actual text and context to decide.

>

> What kind of row is {row}?

- **switch** — A setting that is simply on or off and takes effect at once: notifications, dark mode, autoplay, sync.

- **value** — A setting with one current value picked from several, changed on another page: language, quality, theme, frequency, units.

- **nav** — A link to another page: a content item, details, account, privacy, help, about, or managing something. Its text and section identify what it opens.

- **check** — One of several alternative options listed together, of which one is chosen: the choices of a single setting, such as '10 seconds', '30 seconds', 'High', 'Low'.

- **danger** — A final or destructive account action: sign out, delete account, clear data, reset.
```

Plain text

![05-controlled-row-control](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/05-controlled-row-control.original.png)

On a podcast app's settings screen, Jev answers `Skip forward` → value, `Auto-download` → switch and `Log out` → danger, each at p ≈ 1.00. Apparite builds a whole screen in three steps:

1. One Jev request answers the grammar's layout questions, about 30 for a screen.
2. Code builds the component tree from the catalog and sends `createSurface` and `updateComponents` at about 200 ms, with placeholders where the text will go.
3. gemini-3.5-flash-lite streams the text into `updateDataModel`. As each part arrives, small follow-up Jev requests settle what depends on it, such as the row controls above.

![06-controlled-timeline](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/06-controlled-timeline.original.png)

In one run of 11 prompts, the component tree was on screen in 92 to 298 ms and each screen was complete in 0.8 to 1.7 s. The text writer generated 101 to 341 tokens per screen, and both of Apparite's Jev pipelines produced valid A2UI on all 11 prompts. The project treats these numbers as a first look, since the sample is small.

Controlled generation can only produce the layouts its grammar describes. Apparite's grammar covers nine screen archetypes and twelve blocks, so screens without a known shape are a better fit for Express. A2UI Agent SDKs, don’t include a decision model inference format yet; [apparite(jev2ui)](https://github.com/dglazkov/jev2ui) project is an example on how A2UI messages could be assembled given a batch of independent decisions from a decision model.

## **Which mode to use**

A2UI Express is fast and keeps the full expressivity of A2UI, but a decision model making multiple independent decisions is still faster. Choose by how much of the screen you can define ahead of time:

- **Controlled, when a decision model can produce what you need.** If your screens follow set and defined layouts, a decision model may be the fastest option.
- **Express for full expressivity.** When a screen needs more expressivity based on your catalog, fall back to A2UI Express. It's fast, and the model still writes the whole component tree.
- **Your own format for anything new.** Because inference formats are swappable, a new use case or a future syntax needs only a prompt generator that teaches the model your DSL and a converter that converts between your DSL and A2UI messages. Your catalog and renderers stay the same.

## **Try it**

**Use Express in your agent.** Install the Python SDK with `pip install a2ui-agent-sdk` or the TypeScript SDK with `npm install @a2ui/agent`, pass `ExpressFormatFactory()` when you create the generator, and run the model with thinking off. Your catalog and renderers stay as they are, and the [Express specification](https://a2ui.org/specification/proposals/express/a2ui_express/) documents the syntax.

To teach Gemini, or any other model that loads skills, to write Express with only your components, generate skills from your catalog with the Python SDK's `SkillGenerator`:

```python
import json

from a2ui.core import Catalog

from a2ui.inference_formats.express import ExpressFormat

from a2ui.skill import SkillGenerator

catalog = Catalog.from_json(json.load(open("catalog.json")))

skills = SkillGenerator(ExpressFormat([catalog])).generate_skillset()

skills.export_to_directory("skills")  # a2ui-core plus one skill per catalog
```

Python

![07-try-it-skills](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/07-try-it-skills.original.png)

**Try controlled generation.** Clone the [example jev2ui repository](https://github.com/dglazkov/jev2ui), and follow the instructions there to get started. A hosted version of [Apparite(jev2ui)](https://github.com/dglazkov/jev2ui) runs at [apparite.cnfg.ai](https://apparite.cnfg.ai/).

## **Sources**

Earlier A2UI posts: [Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) (December 2025), [A2UI v0.9](https://developers.googleblog.com/a2ui-v0-9-generative-ui/) (April 2026) and [A2UI + MCP Apps](https://developers.googleblog.com/en/a2ui-and-mcp-apps/) (June 2026).

- [A2UI Express specification](https://a2ui.org/specification/proposals/express/a2ui_express/)
- [A2UI Elemental specification](https://github.com/a2ui-project/a2ui/blob/main/specification/proposals/elemental/a2ui_elemental.md) and [A2UI Atom specification](https://github.com/a2ui-project/a2ui/blob/main/specification/proposals/atom/a2ui_atom.md)
- [Inference format baselines](https://github.com/a2ui-project/a2ui/tree/main/eval/iterative_format_optimizer/baselines) in the A2UI eval
- [a2ui-agent-sdk changelog](https://github.com/a2ui-project/a2ui/blob/main/python/a2ui_agent/CHANGELOG.md) (0.9.0, October 17, 2026) and [@a2ui/agent](https://www.npmjs.com/package/@a2ui/agent) on npm (0.0.1)
- [Skill generator](https://github.com/a2ui-project/a2ui/blob/main/python/a2ui_agent/src/a2ui/skill/generator.py) in the Python agent SDK
- [Jev documentation](https://docs.typesafe.ai/) from TypeSafe
- [Apparite (jev2ui) README](https://github.com/dglazkov/jev2ui), "Results so far" and "Known limits", and its [screen grammar](https://github.com/dglazkov/jev2ui/blob/main/grammar/screen.md)
