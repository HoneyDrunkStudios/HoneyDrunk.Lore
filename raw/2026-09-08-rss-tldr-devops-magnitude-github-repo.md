---
source: "https://github.com/magnitudedev/magnitude"
title: "Magnitude (GitHub Repo)"
author: "unknown"
date_published: "2026-09-04"
date_clipped: "2026-09-08"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-09-04"
source_role: "primary-via-tldr"
---

# Magnitude (GitHub Repo)

Source: https://github.com/magnitudedev/magnitude

Magnitude
Local models, tuned for your Mac.
Magnitude is an open source inference server for Apple silicon. It profiles your Mac, recommends the best models for it, then downloads, tunes, and runs them. Plugs into Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline, or use the built-in harness.
⭐ Help us reach more developers and grow the Magnitude community. Star this repo!
Get started
See what your Mac can run:
npm i -g @magnitudedev/cli
magnitude setup
Setup profiles your hardware, ranks models by speed, accuracy, intelligence, and memory, and connects your harness to the one you pick.
Or let your agent handle it. Send this to Pi, Claude Code, OpenCode, or whatever you use:
Set up local models for me with the Magnitude CLI. Install it with `npm i -g @magnitudedev/cli` (or my package manager), then run `magnitude docs onboarding` and follow the instructions.
Your agent will profile your hardware, walk you through the best local models for it, download the ones you pick, and switch itself over to them.
Why Magnitude?
Knows your Mac: profiles your hardware to assess fit and estimate tok/s per model
Recommends the best models: ranked by speed, accuracy, intelligence, and memory
Tuned end to end: speculative decoding and more, all set for your Mac
Easy setup: one command and your agent is running local models
Free to run: no token costs, API keys, or rate limits
Fully private and offline: models, prompts, and files stay on your Mac
Models on demand: loaded on request, unloaded when idle or memory fills
Open source: Apache 2.0, yours to modify
FAQ
What is Magnitude?
An open source inference server for Apple silicon. It profiles your Mac, recommends the best models for it, then downloads, tunes, and runs them. Plug it into the agent you already use.
Why only Mac?
Apple silicon is the best consumer hardware for local models, and building for one platform lets us optimize the whole stack for it, from model selection down to the kernels.
How does it know what my Mac can run?
Magnitude profiles your chip, memory, and bandwidth, then estimates fit and tok/s for every model in the catalog. It ranks them by speed, accuracy, intelligence, and memory so you can pick.
What Mac do I need?
Any Apple silicon Mac (M1 or later, 2020 onward) running macOS 15 or newer. Intel Macs aren't supported. There's no fixed minimum beyond that. More memory lets you run larger models.
Which harnesses work with it?
Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline. During setup, your agent connects your harness to the model you pick. Or use Magnitude's built-in harness.
Do I need to manage it after setup?
No. It runs in the background, loads models when your agent needs them, and unloads them when idle or memory gets tight. Your agent can install or switch models through the CLI anytime.
Is it private?
Yes. Prompts, files, and models stay on your Mac. Once a model is downloaded, no internet connection is needed.
Learn more
Documentation
CLI reference
Discord
Report an issue
License
Magnitude is licensed under the Apache License 2.0 .
