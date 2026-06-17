---
source: "https://developers.googleblog.com/gemini-api-io-updates/"
title: "Gemini API I/O updates- Google Developers Blog"
author: "Shrestha Basu Mallick; Logan Kilpatrick; Alisa Fortin"
date_published: "2025-05-23"
date_clipped: "2026-06-17"
category: "AI / LLM Research & Tooling"
source_type: "web"
---
[Gemini](/search/?product_categories=Gemini) / [Google AI Studio](/search/?product_categories=Google+AI+Studio)

# Gemini API I/O updates

MAY 23, 2025

[Shrestha Basu Mallick](/search/?author=Shrestha+Basu+Mallick)
Product
Google DeepMind

[Logan Kilpatrick](/search/?author=Logan+Kilpatrick)
Group Product Manager

[Alisa Fortin](/search/?author=Alisa+Fortin)
Product Manager

[Ivan Solovyev](/search/?author=Ivan+Solovyev)
Product Manager

Share

- [Facebook](https://www.facebook.com/sharer/sharer.php?u={url} "Share on Facebook")
- [Twitter](https://twitter.com/intent/tweet?text={url} "Share on Twitter")
- [LinkedIn](https://www.linkedin.com/shareArticle?url={url}&mini=true "Share on LinkedIn")
- [Mail](mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20{url} "Send via Email")

![Gemini_API_banner](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/banner.original_lC607xu.png)

The Gemini API offers developers a streamlined way to build innovative applications with cutting-edge generative AI models. [Google AI Studio simplifies this process](https://developers.googleblog.com/en/google-ai-studio-native-code-generation-agentic-tools-upgrade) of testing all the API capabilities allowing for rapid prototyping and experimentation with text, image, and even video prompts. When developers want to test and build at scale they can leverage all the capabilities available through the Gemini API.

## New models available through the API

**Gemini 2.5 Flash Preview** - We’ve added a new 2.5 Flash preview (gemini-2.5-flash-preview-05-20) which is better over the previous preview at reasoning, code, and long context. This version of 2.5 Flash is currently #2 on the LMarena leaderboard behind only 2.5 Pro. We’ve also improved Flash cost-efficiency with this latest update reducing the number of tokens needed for the same performance, resulting in 22% efficiency gains on our evals. Our goal is to keep improving based on your feedback, and make both generally available soon.

**Gemini 2.5 Pro and Flash text-to-speech (TTS)** - We also announced 2.5 Pro and Flash previews for text-to-speech (TTS) that support native audio output for both single and multiple speakers, across 24 languages. With these models, you can control TTS expression and style, creating rich audio output. With multispeaker, you can generate conversations with multiple distinct voices for dynamic interactions.

**Gemini 2.5 Flash native audio dialog** - In preview, this model is available via the Live API to generate natural sounding voices for conversation, in over 30 distinct voices and 24+ languages. We’ve also added proactive audio so the model can distinguish between the speaker and background conversations, so it knows when to respond. In addition, the model responds appropriately to a user's emotional expression and tone. A separate thinking model enables more complex queries. This now makes it possible for you to build conversational AI agents and experiences that feel more intuitive and natural, like enhancing call center interactions, developing dynamic personas, crafting unique voice characters, and more.

**Lyria RealTime -** Live music generation is now available in the Gemini API and Google AI Studio to create a continuous stream of instrumental music using text prompts. With Lyria RealTime, we use WebSockets to establish a persistent, real-time communication channel. The model continuously produces music in small, flowing chunks and adapts based on inputs. Imagine adding a responsive soundtrack to your app or designing a new type of musical instrument! Try out Lyria RealTime with the [PromptDJ-MIDI](https://aistudio.google.com/app/apps/bundled/promptdj-midi) app in Google AI Studio.

**Gemini 2.5 Pro Deep Think** - We are also testing an experimental reasoning mode for 2.5 Pro. We’ve seen incredible performance with these Deep Thinking capabilities for highly complex math and coding prompts. We look forward to making it broadly available for you to experiment with soon.

**Gemma 3n -** Gemma 3n is a generative AI open model optimized for use in everyday devices, such as phones, laptops, and tablets. It can handle text, audio and vision inputs. This model includes innovations in parameter-efficient processing, including Per-Layer Embedding (PLE) parameter caching and a MatFormer model architecture that provides the flexibility to reduce compute and memory requirements.

## New functionality in the API

### **Thought summaries**

To help developers understand and debug model responses, we’ve added thought summaries for 2.5 Pro and Flash in the Gemini API. We take the model’s raw thoughts and synthesize them into a helpful summary with headers, relevant details and tool calls. The raw chain-of-thoughts in Google AI Studio has also been updated with the new thought summaries.

### **Thinking budgets**

We launched 2.5 Flash with thinking budgets to provide developers control over how much models think to balance performance, latency, and cost for the apps they are building. We will be extending this capability to 2.5 Pro soon.

```
from google import genai

from google.genai import types



client = genai.Client(api_key="GOOGLE_API_KEY")

prompt = "What is the sum of the first 50 prime numbers?"

response = client.models.generate_content(

  model="gemini-2.5-flash-preview-05-20",

  contents=prompt,

  config=types.GenerateContentConfig(

    thinking_config=types.ThinkingConfig(thinking_budget=1024,

      include_thoughts=True

    )

  )

)



for part in response.candidates[0].content.parts:

  if not part.text:

    continue

  if part.thought:

    print("Thought summary:")

    print(part.text)

    print()

  else:

    print("Answer:")

    print(part.text)

    print()
```

Python

Copied

Sample code to enable and retrieve thought summaries without streaming, returning a final thought summary with the response.

### **New URL Context tool**

We added a new experimental tool, URL context, to retrieve more context from links that you provide. This can be used by itself or in conjunction with other tools such as [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding). This tool is a key building block for developers looking to build their own version of research agents with the Gemini API.

```
from google import genai

from google.genai.types import Tool, GenerateContentConfig, GoogleSearch



client = genai.Client()

model_id = "gemini-2.5-flash-preview-05-20"



tools = []

tools.append(Tool(url_context=types.UrlContext))

tools.append(Tool(google_search=types.GoogleSearch))



response = client.models.generate_content(

    model=model_id,

    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",

    config=GenerateContentConfig(

        tools=tools,

        response_modalities=["TEXT"],

    )

)



for each in response.candidates[0].content.parts:

    print(each.text)

# get URLs retrieved for context

print(response.candidates[0].url_context_metadata)
```

Python

Copied

Sample code for Grounding with Google Search and URL Context

### **Computer use tool**

We're bringing [Project Mariner's](https://deepmind.google/models/project-mariner/) browser control capabilities to the Gemini API via a new computer use tool. To make it easier for developers to use this tool, we are enabling the creation of Cloud Run instances optimally configured for running browser control agents via one click from Google AI Studio. We’ve begun early testing with companies like Automation Anywhere, UiPath and Browserbase. Their valuable feedback will be instrumental in refining its capabilities for a broader experimental developer release this summer.

### **Improvements to structured outputs**

The Gemini API now has broader support for JSON Schema, including much-requested keywords such as "$ref" (for references) and those enabling the definition of tuple-like structures (e.g., prefixItems).

### **Video understanding improvements**

The Gemini API now allows YouTube video URLs or video uploads to be added to a prompt, enabling users to to summarize, translate, or analyze the video content. With this recent update, the API supports video clipping, enabling flexibility in analyzing specific parts of a video. This is particularly beneficial for videos longer than 8 hours. We have also added support for dynamic frames per second (FPS), allowing 60 FPS for videos like games or sports where speed is critical, and 0.1 FPS for videos where speed is less of a priority. To help users save tokens, we have also introduced support for 3 different video resolutions: high (720p), standard (480p), and low (360p).

### **Async function calling**

The cascaded architecture in the Live API now supports asynchronous function calling, ensuring user conversations remain smooth and uninterrupted. This means your Live agent can continue generating responses even while it's busy executing functions in the background, by simply adding the behavior field to the function definition and setting it to NON-BLOCKING. Read more about this in the Gemini API developer [documentation](https://ai.google.dev/gemini-api/docs/live#async-function-calling).

### **Batch API**

We are also testing a new API, which lets you easily batch up your requests and get them back in a max 24 hour turnaround time. The API will come at half the price of the interactive API and with much higher rate limits. We hope to roll that out more widely later this summer.

## Start building

That’s a wrap on I/O for this year! With the Gemini API and Google AI Studio, you can turn your ideas into reality, whether you're building conversational AI agents with natural-sounding audio or developing tools to analyze and generate code. As always, check out the Gemini API [developer docs](https://ai.google.dev/gemini-api/docs) for all the latest code samples and more.

Explore this announcement and all Google I/O 2025 updates on [io.google](https://io.google/2025/?utm_source=blogpost&utm_medium=pr&utm_campaign=event&utm_content=).

posted in:

- [Gemini](/search/?product_categories=Gemini)
- [Google AI Studio](/search/?product_categories=Google+AI+Studio)
- [AI](/search/?technology_categories=AI)
- [Announcements](/search/?content_type_categories=Announcements)
- [AI models](/search/?tag=AI models)
- [Generative AI](/search/?tag=Generative AI)
- [Google I/O 2025](/search/?tag=Google I/O 2025)
- [Developer Tools](/search/?tag=Developer Tools)
- [video generation](/search/?tag=video generation)
- [text-to-speech](/search/?tag=text-to-speech)
- [audio generation](/search/?tag=audio generation)

Previous

Next

Related Posts

[![DiffusionGemma: The Developer Guide](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/diffusion_banner.2e16d0ba.fill-800x400.png)

AI
Announcements
Explore

DiffusionGemma: The Developer Guide

JUNE 10, 2026](/diffusiongemma-the-developer-guide/)
[![Unlocking the Power of the TPU Stack: Introducing our new Developer Hub](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/TPU_v5e_-_Board_4_-_Web.2e16d0ba.fill-800x400.jpg)

AI
Cloud
Announcements
Learn

Unlocking the Power of the TPU Stack: Introducing our new Developer Hub

JUNE 16, 2026](/unlocking-the-power-of-the-tpu-stack-introducing-our-new-developer-hub/)
[![Turn creative prompts into interactive XR experiences with Gemini](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Gemini_Generated_Image_gasezsgasez.2e16d0ba.fill-800x400.png)

Gemini
Web
AI
Tutorials
How-To Guides

Turn creative prompts into interactive XR experiences with Gemini

FEB. 19, 2026](/turn-creative-prompts-into-interactive-xr-experiences-with-gemini/)
[![How we built the Google I/O 2026 Save the Date experience](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/mbu-svd-hero.2e16d0ba.fill-800x400.png)

Gemini
Google AI Studio
AI
Events

How we built the Google I/O 2026 Save the Date experience

MARCH 3, 2026](/how-we-built-the-google-io-2026-save-the-date-experience/)
[![Enhance Security and Trust: New Session Metadata in Sign in with Google](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/banner-usability-safety-updates-go.2e16d0ba.fill-800x400.png)

Mobile
Web
Announcements
Best Practices

Enhance Security and Trust: New Session Metadata in Sign in with Google

JUNE 16, 2026](/enhance-security-and-trust-new-session-metadata-in-sign-in-with-google/)
