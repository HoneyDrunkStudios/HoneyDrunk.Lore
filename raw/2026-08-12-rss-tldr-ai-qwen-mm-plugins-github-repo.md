---
source: "https://github.com/QwenLM/Qwen-MM-Plugins"
title: "Qwen-MM-Plugins (GitHub Repo)"
author: "TLDR AI"
date_published: "2026-08-11"
date_clipped: "2026-08-12"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-08-11"
source_role: "primary-via-tldr"
---

# Qwen-MM-Plugins (GitHub Repo)

Source: https://github.com/QwenLM/Qwen-MM-Plugins

Qwen-MM-Plugins
English · 中文
Native multimodal plugins for Qwen models. Make any agent harness multimodal-native.
Architecture
Install
The guided installer supports Claude Code, Codex, Qoder, OpenClaw, Qwen Code, and Gemini CLI. It
uses each harness's native install command and keeps shared configuration in
~/.qwen-mm-plugins/config .
curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash
Update the capabilities already installed in one harness:
curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash -s -- update
Released capabilities use independent, immutable tags. For local checkout installs, rollback,
manual skill + MCP setup, dependencies, and Windows/WSL2, see the
installation guide .
Capabilities
Each capability is installed independently as a Skill plus an optional MCP server . Its
install name is qwen-mm-plugins-<capability> .
Capability
Use case
Main requirements
Cookbook
core
Read images and video; visualize documents, code, data, 3D files, and more
No API key; ffmpeg for audio/video; format-specific apps as needed
Cookbook
api
Qwen VL/Omni vision, OCR, grounding, ASR, segmentation, and audio-video understanding
DashScope; ffmpeg for local audio/video
Cookbook
search
Web search, page extraction, and reverse-image search
Serper, Exa, or Tavily key; image search requires Serper
Cookbook
video-memory
Build hierarchical memory for long-video QA
DashScope; ffmpeg/ffprobe for builds
Cookbook
video-edit
Image, video, and audio generation with editing workflows
DashScope; ffmpeg + Node/Chromium for full edits
Cookbook
blender
Model, texture, light, and render in Blender
Blender; Xvfb on headless Linux
Cookbook
freecad
Parametric CAD, STEP/STL, and FEM workflows
FreeCAD; CalculiX for FEM; Xvfb on headless Linux
Cookbook
edu-agent
Create Chinese math/science explainer videos and interactive pages
Skill-only; Node/Chromium + ffmpeg; DashScope for narrated video
Cookbook
Try it
After installing a capability, reference a file and ask naturally; the Skill selects the relevant
MCP tool.
@report.pdf Summarize page 3 and extract its table.
@meeting.mp4 Transcribe this with speaker labels and timestamps.
@place.jpg Identify where this photo was taken and verify it on the web.
@lecture-2h.mp4 List the main points with timestamps.
core reads media at dynamic resolution, so manual resizing is normally unnecessary.
Requirements and configuration
uv provides uvx , which installs Python dependencies on demand.
Local core tools need no API key. Cloud and search capabilities need their provider credentials.
Video, document, browser, Blender, and FreeCAD workflows may need system applications.
Run the installer's Configure and Verify actions to set credentials and check dependencies.
See Installation for prerequisites and the
configuration reference for every setting.
Documentation
Installation
Configuration
Contributing · Local development
Add a capability · Testing
License
Apache-2.0 — see LICENSE . Third-party attribution for the Blender and FreeCAD integrations
is recorded in their respective Blender and
FreeCAD notices.
