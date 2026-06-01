---
source: "https://www.digitalocean.com/blog/digitalocean-opencode-inference-routers"
title: "OpenCode Now Supports DigitalOcean Inference Router for Intelligent Model Routing"
author: "unknown"
date_published: "2026-05-29"
date_clipped: "2026-06-01"
category: "DevOps & CI/CD"
source_type: "web"
---

# OpenCode Now Supports DigitalOcean Inference Router for Intelligent Model Routing

Source: https://www.digitalocean.com/blog/digitalocean-opencode-inference-routers

OpenCode Now Supports DigitalOcean Inference Router for Intelligent Model Routing | DigitalOcean Blog Docs Careers Get Support Contact Sales DigitalOcean Products Featured AI Products
Compute
Build, deploy, and scale cloud compute resources
Containers and Images
Safely store and manage containers and backups
Managed Databases
Fully managed resources running popular database engines
Management and Dev Tools
Control infrastructure and gather insights
Networking
Secure and control traffic to apps
Security
Help protect your account and resources with these security features
Storage
Store and access any amount of data reliably in the cloud
Browse all products Solutions AI/ML
CMS
Data and IoT
Developer Tools
Gaming and Media
GPU
Hosting
Security and Networking
Startups and SMBs
Web and App Platforms
See all solutions Developers Community
Documentation
Developer Tools
Get Involved
Utilities and Help
Partners Become a Partner
Marketplace
Pricing Log in Sign up Log in Sign up Company About Leadership Blog Careers Customers Partners Referral Program Affiliate Program Press Legal Privacy Policy Security Investor Relations Products GPU Droplets Bare Metal GPUs Inference Engine Data & Learning Droplets Kubernetes Functions App Platform Load Balancers Managed Databases Spaces Block Storage Network File Storage API Uptime Cloud Security Posture Management (CSPM) Identity and Access Management (IAM) Cloudways View all Products Resources Community Tutorials Community Q&A CSS-Tricks Write for DOnations Currents Research DigitalOcean Startups Wavemakers Program Compass Council Open Source Newsletter Signup Marketplace Pricing Pricing Calculator Documentation Release Notes Code of Conduct Shop Swag Solutions AI GPU Hosting H100 Cloud GPU AI Training GPU GPU Inference VPS Hosting Website Hosting VPN Docker Hosting Node.js Hosting Web Mobile Apps WordPress Hosting Virtual Machines View all Solutions Contact Support Sales Report Abuse System Status Share your ideas Company About Leadership Blog Careers Customers Partners Referral Program Affiliate Program Press Legal Privacy Policy Security Investor Relations Products GPU Droplets Bare Metal GPUs Inference Engine Data & Learning Droplets Kubernetes Functions App Platform Load Balancers Managed Databases Spaces Block Storage Network File Storage API Uptime Cloud Security Posture Management (CSPM) Identity and Access Management (IAM) Cloudways View all Products Resources Community Tutorials Community Q&A CSS-Tricks Write for DOnations Currents Research DigitalOcean Startups Wavemakers Program Compass Council Open Source Newsletter Signup Marketplace Pricing Pricing Calculator Documentation Release Notes Code of Conduct Shop Swag Solutions AI GPU Hosting H100 Cloud GPU AI Training GPU GPU Inference VPS Hosting Website Hosting VPN Docker Hosting Node.js Hosting Web Mobile Apps WordPress Hosting Virtual Machines View all Solutions Contact Support Sales Report Abuse System Status Share your ideas © 2026 DigitalOcean, LLC. Sitemap . Dark mode is coming soon. Product updates OpenCode Now Supports DigitalOcean Inference Router for Intelligent Model Routing By Musa Malik 
AI/ML Engineer
Updated: May 28, 2026 3 min read <- Back to blog home Coding agents today have a massive spending problem. Every request, whether you’re designing system architecture or writing a single-line docstring, often gets routed to the same expensive frontier model. The result: unnecessary token usage, higher inference costs, and little awareness of task complexity or budget constraints.
This high cost stems from a “one-size-fits-all” approach to model usage, where premium frontier models are utilized for trivial tasks that don’t require such intensive reasoning effort. In multi-agent workflows, where orchestrators delegate work to specialized subagents, this lack of discrimination frequently leads to runaway costs and opaque failure modes. Without intelligent routing, developers can essentially be forced into closed-provider lock-in and high API usage fees, which quickly escalate during exploratory building phases.
DigitalOcean Inference Router , now in Public Preview, was built to solve this problem by dynamically routing requests to the right model for the job. As part of DigitalOcean’s AI-Native Cloud, it gives developers a unified way to control, optimize, and evaluate AI inference across models. And as of today, you can access it through OpenCode , the open-source AI coding agent, in as little as a few seconds.
What is an Inference Router? 
An Inference Router is the auto-mode pattern engineers are used to, but with deliberate control over the tradeoffs that matter: latency, cost, and output quality. Rather than statically pointing your coding agent to a single model, an Inference Router can analyze each request and route it to the model best suited for that specific task. Not the most powerful model available, but the right model. That distinction is what drives real savings without compromising on your desired quality of output.
To use DigitalOcean’s Inference Router: Create an Inference Router from the router catalog —pick a preset or build a custom router via the API or UI. No GPU management, no infrastructure to run. Use it by setting “model”: “router:your-router-name” in any OpenAI-compatible API call.
What Changed for OpenCode 
OpenCode has become one of the most popular AI coding harnesses on GitHub, earning over 160,000 stars by embracing a simple idea: developers should not be locked into a single model provider. Its rise has shown a demand for provider agnostic AI use cases. At Deploy 2026, Tyler Gillam - a core engineer on Inference Router - demoed our integration live on stage , showing exactly how OpenCode and Inference Router work together to make intelligent model selection decisions in real time. If you want to see it before diving in, the full recording is linked at the bottom of this post.
Previously, integrating DigitalOcean models into OpenCode meant manually editing your opencode.json , adding each model by hand, a list that would be outdated within weeks given the pace of new model launches. So, we built a native OpenCode integration that supports Inference Routers and DigitalOcean Serverless Inference models right out of the box.
Now you can run the following steps:
Launch OpenCode (desktop, web or TUI) and run /connect 
Select Login with DigitalOcean 
Your Inference Routers are shown in the Model Selection tab 
That’s it. You’re plugging directly into a routing layer that’s already helping to make the cost & quality tradeoff decisions for you based on your stated needs — with our purpose-build Software Engineering preset.
Beyond Coding Agents 
This integration is part of a broader effort to bring DigitalOcean’s Inference Engine into the tools developers already use, while continuing to invest in open source and upstream contributions. OpenCode is one example of that direction.
The goal is to make intelligent, cost-aware model routing the default for coding agents, not something you have to manually configure and hope for the best. As the OSS model landscape keeps improving, routing intelligence will become more valuable, not less. The gap between “frontier” and “good enough” is closing fast, and developers who take advantage of routing will consistently come ahead on both desired quality and cost.
If you’re using OpenCode, try /connect today. If you want to dig deeper on what Inference Router is and how it works, the full documentation is available below.
Inference Router Resources:
How We Built DigitalOcean Inference Router 
Inference Router Documentation 
OpenCode DigitalOcean Install 
InferenceRouter OpenCode Deploy 2026 Demo 
About the author Musa Malik Author AI/ML Engineer See author profile Musa is an AI/ML Engineer on DigitalOcean's Agentic Inference Cloud team, working on Plano & Inference Router. He joined DigitalOcean in March 2026 through the acquisition of Katanemo Labs, where he was a core engineer. He writes about LLM infrastructure, agentic systems and developer experiences for AI applications.
See author profile Share
Product Updates Start building today From GPU-powered inference and Kubernetes to managed databases and storage, get everything you need to build, scale, and deploy intelligent applications. Sign up Related Articles Product updates Scalable, Cost-Efficient AI: Introducing Unified Batch Inference on DigitalOcean snamdeo May 27, 2026 8 min read Read more 
Product updates Request-Based Autoscaling Is Now Generally Available on App Platform Bikram Gupta
May 22, 2026 4 min read Read more 
Product updates Powering the Inference Era: Inside the DigitalOcean AI-Native Cloud Vinay Kumar, Chief Product & Technology Officer
May 4, 2026 7 min read Read more
