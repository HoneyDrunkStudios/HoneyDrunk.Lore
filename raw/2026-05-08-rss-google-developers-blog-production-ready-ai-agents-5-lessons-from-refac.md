---
source: "https://developers.googleblog.com/production-ready-ai-agents-5-lessons-from-refactoring-a-monolith/"
title: "Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith"
author: "Google Developers Blog"
date_published: "unknown"
date_clipped: "2026-05-08"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith

Source: https://developers.googleblog.com/production-ready-ai-agents-5-lessons-from-refactoring-a-monolith/

Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith
- Google Developers Blog
{
"@context": "https://schema.org",
"@type": "BreadcrumbList",
"itemListElement": [{
"@type": "ListItem",
"position": 1,
"name": "Google for Developers Blog",
"item": "https://developers.googleblog.com/"
},{
"@type": "ListItem",
"position": 2,
"name": "Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith",
"item": "https://developers.googleblog.com/production-ready-ai-agents-5-lessons-from-refactoring-a-monolith/"
}]
}
{
"@context": "https://schema.org",
"@type": "Article",
"headline": "Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith",
"description": "The blog post outlines the transition of a brittle sales research prototype into a robust production agent using Google’s Agent Development Kit (ADK). By replacing monolithic scripts with orchestrated sub-agents and structured Pydantic outputs, the developers eliminated silent failures and fragile parsing. Additionally, the post highlights the necessity of dynamic RAG pipelines and OpenTelemetry observability to ensure AI agents are scalable, cost-effective, and transparent in real-world applications.",
"image": "https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/AI_Agent_Clinic_Asset.2e16d0ba.fill-800x400.png",
"datePublished": "2026-04-21",
"author": [
{ "@type": "Person", "name": "Luis Sala", "url": "/search/?author=Luis+Sala" },
{ "@type": "Person", "name": "Jacob Badish", "url": "/search/?author=Jacob+Badish" },
{ "@type": "Person", "name": "Frank Guan", "url": "/search/?author=Frank+Guan" }
]
}
Products
Develop 
Android
Chrome
ChromeOS
Cloud
Firebase
Flutter
Google Assistant
Google Maps Platform
Google Workspace
TensorFlow
YouTube
Grow 
Firebase
Google Ads
Google Analytics
Google Play
Search
Web Push and Notification APIs
Earn 
AdMob
Google Ads API
Google Pay
Google Play Billing
Interactive Media Ads
Solutions
Events
Learn
Community
Groups 
Google Developer Groups
Google Developer Student Clubs
Woman Techmakers
Google Developer Experts
Tech Equity Collective
Programs 
Accelerator
Solution Challenge
DevFest
Stories 
All Stories
Developer Program
Blog
Search
Products
More
Solutions
Events
Learn
Community
More
Developer Program
Blog
Develop
Android
Chrome
ChromeOS
Cloud
Firebase
Flutter
Google Assistant
Google Maps Platform
Google Workspace
TensorFlow
YouTube
Grow
Firebase
Google Ads
Google Analytics
Google Play
Search
Web Push and Notification APIs
Earn
AdMob
Google Ads API
Google Pay
Google Play Billing
Interactive Media Ads
Groups
Google Developer Groups
Google Developer Student Clubs
Woman Techmakers
Google Developer Experts
Tech Equity Collective
Programs
Accelerator
Solution Challenge
DevFest
Stories
All Stories
Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith 
APRIL 21, 2026 
Luis Sala 
Customer Engineer 
Jacob Badish 
Territory Account Manager 
Frank Guan 
Product Marketing 
AI Agents 
Share 
Facebook 
Twitter 
LinkedIn 
Mail 
Building an AI agent that works beautifully on your local machine is easy. Building one that survives contact with reality—handling rate limits, avoiding infinite loops, and scaling beyond hardcoded data—is a completely different beast. This isn't just about elegant code; it's about avoiding runaway cloud bills, reputational damage from hallucinated outputs, and the sheer operational nightmare of a silent failure in production.
To solve these "fragile architecture" patterns, we launched the AI Agent Clinic. Our first mission: a complete teardown of "Titanium"—a promising but brittle sales research agent. In our premiere episode, Luis Sala sat down with Jacob Badish to rebuild it from the ground up. Titanium's original job was to research a target company and draft a personalized outreach email. While the prototype ran, it was slow, relied on a monolithic Python script, and was limited to a hardcoded list of just 12 case studies.
Over the course of an hour, the team tore down and rebuilt the agent for production. Here are the core breakdowns, the fixes, and the engineering lessons from Episode 1.
1. Ditch the Monolith for Orchestrated Sub-Agents The Breakdown: The original agent was running on a massive, linear for loop—a monolithic script. If one sub-task failed (an API timeout or hallucination), the entire process stalled out and failed silently. The Fix: We ripped out the monolith and installed a distributed framework using Google’s Agent Development Kit (ADK). We created a SequentialAgent pipeline, splitting the workload into specialized nodes: a Company Researcher, Search Planner, Case Study Researcher, Selector, and an Email Drafter. The Lesson: Separation of concerns. Specialized agents with narrow tasks run more reliably than a single LLM trying to execute a massive, multi-step prompt.
Architecture: The Orchestrated Pipeline Swap 
2. Force Structured Outputs (via Pydantic) The Breakdown: Originally, Titanium forced JSON outputs out of the model via extensive hard-coding straight inside the prompt string. It resulted in dirty code, fragile parsing, and wasted tokens describing the exact structure over and over again. The Fix: When swapping to ADK, we eradicated schema formatting instructions out of the prompt. Instead, we injected native Pydantic objects directly as explicit schema definitions. ADK uses Structured Outputs dynamically under the hood to abstract the boilerplate and force adherence. By shifting the "contract" from a fuzzy natural language request to a runtime-validated Python object, we guarantee structural integrity and eliminate brittle custom parsing.
# BEFORE: Prompt String Bloat
prompt = """
Give me the answer in this JSON format:
{
"company": "Company Name",
"pain_points": ["point1", "point2"]
}
"""
# AFTER: Pydantic Schema Injection in ADK
class CompanyIntel(BaseModel):
company: str
pain_points: list[str] 
Python
Copied 
3. Replace Hardcoded State with a Dynamic RAG Pipeline The Breakdown: Titanium’s context corpus was artificially tiny. It only knew about 12 hardcoded case studies written directly into the Python file. It couldn't scale or learn without a developer manually updating the code.
The Fix: We built a dynamic data intake system. An async crawler (Playwright) runs in the background to autonomously scrape Google Cloud's customer success website and batch them to Google Cloud Vector Search . Back in the pipeline, the Case Study Researcher runs a true Hybrid Search on the indexed corpus to fetch ideal case studies. (Note: Hybrid Search combines the semantic "meaning" of a query with the precision of exact keyword matching, ensuring the agent doesn't miss specific technical terms). 
The Lesson: Hardcoding is fine for a prototype, but a production pipeline needs to refresh itself. True agentic value comes from giving agents the tools to autonomously fetch, scale, and query via Vector Search. Stop hardcoding your context limits.
Architecture: The RAG Pipeline Intake 
4. Observability is Non-Negotiable The Breakdown: When an LLM gets confused in a standard script, it’s a "black box." You know something failed, but you have no idea which component caused the break.
The Fix: We tapped into ADK’s first-class support for OpenTelemetry on Google Cloud . Out of the box, ADK emits distributed traces for full execution flows, capturing model requests, tokens, and tool executions.
# Bootstrapping OTel in ADK is a one-liner
from adk.observability import configure_telemetry
configure_telemetry(project_id="my-gcp-project", enable_sse_stream=True) 
Python
Copied 
We paired this OpenTelemetry backend with a tailored Server-Sent Events (SSE) streaming app, effectively designing a sleek live-telemetry dashboard for the user.
The Lesson: You cannot put an agent into production without live diagnostics. You need OpenTelemetry traces to resolve ground-truth disputes and debug individual component latencies.
5. Taming the Token Burn (Cost Optimization) The Breakdown: Agentic loops are expensive. If an agent hits an error and continually retries a prompt without strict boundaries, it will burn through your token budget in minutes.
The Fix: By standardizing heavily on ADK's native orchestration, we inherited intrinsic cost optimizations automatically. The framework natively encompasses exponential backoffs, timeout boundaries, and configurable retry loops without writing custom logic into our native Python.
The Lesson: Always install circuit breakers. Let ADK or your orchestration framework handle graceful failures rather than writing complex try-catch retry loops natively.
Want to see the code in action? There is no substitute for watching the engine rebuild happen live. Watch the full Episode 1 of the AI Agent Clinic here to see exactly how Titanium was refactored. You can also fork the Titanium Repo here . 
Is your agent broken, buggy, or stuck in prototype purgatory? We want to help. Submit your agent and its architecture to agent-clinic@google.com for a chance to have it diagnosed and refactored live on the next episode!
posted in:
AI 
Cloud 
Announcements 
Best Practices 
Learn 
Solve 
Previous 
Next 
Related Posts 
Cloud 
Cloud 
Announcements 
Explore 
Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket
APRIL 29, 2026 
Mobile 
AI 
Case Studies 
Announcements 
Building real-world on-device AI with LiteRT and NPU
APRIL 23, 2026 
AI 
Cloud 
Tutorials 
Case Studies 
Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding
MAY 4, 2026 
AI 
How-To Guides 
Learn 
Building with Gemini Embedding 2: Agentic multimodal RAG and beyond
APRIL 30, 2026 
Connect
Blog
Bluesky
Instagram
LinkedIn
X (Twitter)
YouTube
Programs
Google Developer Program
Google Developer Groups
Google Developer Experts
Accelerators
Women Techmakers
Google Cloud & NVIDIA
Developer consoles
Google API Console
Google Cloud Platform Console
Google Play Console
Firebase Console
Actions on Google Console
Cast SDK Developer Console
Chrome Web Store Dashboard
Google Home Developer Console
Android
Chrome
Firebase
Google Cloud Platform
All products
Manage cookies
Terms
Privacy
