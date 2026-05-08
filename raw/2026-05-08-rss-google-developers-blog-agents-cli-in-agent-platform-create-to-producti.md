---
source: "https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/"
title: "Agents CLI in Agent Platform:  create to production in one CLI"
author: "Google Developers Blog"
date_published: "unknown"
date_clipped: "2026-05-08"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Agents CLI in Agent Platform:  create to production in one CLI

Source: https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/

Agents CLI in Agent Platform: create to production in one CLI
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
"name": "Agents CLI in Agent Platform: create to production in one CLI",
"item": "https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/"
}]
}
{
"@context": "https://schema.org",
"@type": "Article",
"headline": "Agents CLI in Agent Platform: create to production in one CLI",
"description": "Google Cloud has introduced the Agents CLI, a specialized tool designed to bridge the gap between local development and production-grade AI agent deployment. The CLI provides coding assistants with machine-readable access to the full Google Cloud stack, reducing context overload and token waste during the scaffolding process. By streamlining evaluation, infrastructure provisioning, and deployment into a single programmatic backbone, the tool enables developers to move from initial concept to a live service in hours rather than weeks.",
"image": "https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/hero_image_1.2e16d0ba.fill-800x400.jpg",
"datePublished": "2026-04-22",
"author": [
{ "@type": "Person", "name": "Ivan Cheung", "url": "/search/?author=Ivan+Cheung" },
{ "@type": "Person", "name": "Pier Paolo Ippolito", "url": "/search/?author=Pier+Paolo+Ippolito" },
{ "@type": "Person", "name": "Elia Secchi", "url": "/search/?author=Elia+Secchi" }
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
Agents CLI in Agent Platform: create to production in one CLI 
APRIL 22, 2026 
Ivan Cheung 
Software Engineer 
Pier Paolo Ippolito 
GenAI Field Solutions Architect 
Elia Secchi 
Solutions Specialist 
Share 
Facebook 
Twitter 
LinkedIn 
Mail 
APRIL 22, 2026 Developer Relations Engineering Agent Ecosystems 
AI agents are transitioning from experimental scripts to production services. But while models get smarter, the infrastructure required to build, evaluate, and deploy them remains stubbornly fragmented. Developers and their coding assistants often struggle with isolation, wasting time and tokens ingesting massive amounts of documentation just to bridge the local-to-cloud gap.
Today, we are thrilled to introduce Agents CLI in Agent Platform , the unified programmatic backbone for the Agent Development Lifecycle (ADLC) on Google Cloud.
Agents CLI is a specialized tool designed specifically for AI coding agents (like Gemini CLI, Claude Code, and Cursor). It gives your AI assistant a direct, machine-readable line to the full Google Cloud agent stack (including Agent Platform, Cloud Run, and A2A Integration) turning a fragmented ecosystem into a seamless assembly line.
Let’s take a look at how the Agents CLI streamlines the journey from idea to production in hours, not weeks.
Build Agents with Agents The biggest hurdle in agent development is context overload. When your coding agent has to guess how disparate cloud components fit together, it leads to endless loops and token waste.
With Agents CLI in Agent Platform, you simply run one command (uvx google-agents-cli) to inject bundled skills directly into your coding environment.
This provides coding assistants the exact sensory input and API references they need to scaffold functional, standard-compliant projects immediately.
# Installing the CLI 
uvx google-agents-cli setup 
Plain text
Copied 
If you want to, you can run the CLI commands directly yourself. However, you can even use your favorite coding agent to use the CLI commands via Agents CLI Skills.
For example, you could prompt your coding agent: "I want to create a travel expense agent that can help me auto-approve expenses under $50 and require HITL to approve anything over $50, or any expense that might look out of the norm."
# Your coding agent seamlessly scaffolds the project using automatic defaults
agents-cli create finance-agent -y --deployment-target agent_runtime
# Move into the directory
cd finance-agent 
Plain text
Copied 
Local Simulation and Rigorous Evaluation Building the logic is only half the battle, ensuring it behaves correctly is the other. Before going live, developers need to know their agents meet accuracy thresholds.
Agents CLI can run rigorous evaluation harnesses. By using native commands, your coding assistant can orchestrate unit tests, validate data retrieval, and contrast different evaluation runs to guarantee quality.
# Run evaluations against your ground-truth datasets
agents-cli eval run
# Compare the trajectory scoring and metrics of two runs
agents-cli eval compare evals/run_v1.json evals/run_v2.json 
JSON
Copied 
Seamless Deployment to Production Going from a local prototype to a secure, globally distributed service shouldn't take 70 days. Agents CLI can automate the entire deployment phase. It seamlessly injects Infrastructure as Code (IaC), sets up CI/CD pipelines, and deploys directly to Agent Runtime / Cloud Run/ GKE.
# Provision the production infrastructure
agents-cli infra single-project 
# Ship the agent to Google Cloud
agents-cli deploy
# Register the deployed agent with Gemini Enterprise for distribution
agents-cli publish gemini-enterprise 
Plain text
Copied 
Human Intent + Agent Execution While the Agents CLI is optimized for agent consumption ( Agent Mode ), we know developers need deterministic control. That's why the CLI fully supports a Human Mode . You can run these commands directly in your terminal or scripts for immediate, deterministic execution: stepping in whenever you want to guide the "hands and eyes" of the AI.
What's Next? Get started today by downloading Agents CLI in Agent Platform and running uvx google-agents-cli in your terminal. Dive into our Documentation and GitHub repository to see how your coding assistant can build the next generation of production-grade AI.
Don't forget to join our community on Reddit or the Agent Ecosystems Google Group and share what you're building.
The Agentic Internet is here. Let your agents build it.
Link to Youtube Video 
(visible only when JS is disabled)
POSTED IN: AI • Cloud • Announcements • Problem-Solving
posted in:
AI 
Cloud 
Announcements 
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
