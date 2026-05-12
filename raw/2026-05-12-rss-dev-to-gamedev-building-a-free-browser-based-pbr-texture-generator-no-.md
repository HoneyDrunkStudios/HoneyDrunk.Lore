---
source: "https://dev.to/tools_crazy_e6532397d4aa8/building-a-free-browser-based-pbr-texture-generator-no-plugins-no-uploads-38db"
title: "Building a Free Browser-Based PBR Texture Generator (No Plugins, No Uploads)"
author: "DEV.to Gamedev"
date_published: "Tue, 12 May 2026 02:50:16 +0000"
date_clipped: "2026-05-12"
category: "Game Development / Unity"
source_type: "rss"
---

# Building a Free Browser-Based PBR Texture Generator (No Plugins, No Uploads)

Source: https://dev.to/tools_crazy_e6532397d4aa8/building-a-free-browser-based-pbr-texture-generator-no-plugins-no-uploads-38db

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3920366) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Tools Crazy 
Posted on May 12 
Building a Free Browser-Based PBR Texture Generator (No Plugins, No Uploads)
# ai 
# gamedev 
# showdev 
# tooling 
I built NormalMap AI — a free, browser-based tool that generates complete PBR texture sets (Normal, Roughness, AO, Metallic, Height, ORM) from any uploaded image. Here's what I learned building it.
Demo Video
Screenshots
The Problem
Game devs and 3D artists have always needed PBR texture maps. The traditional tools:
Photoshop 3D filter: removed in newer versions, never great 
Substance Painter: $49.99/month per seat — a lot for hobbyists or small studios 
Free desktop tools: slow, require installs, inconsistent results 
My goal: make the full PBR workflow free, instant, and browser-native.
Technical Approach
Core pipeline: WebGL compute shaders for all map generation.
Normal map: Sobel operator on height-converted luminance, GPU-computed 
Roughness: variance + high-frequency detection across local neighborhoods 
AO: SSAO-style hemisphere sampling in screen space 
Height: multi-scale luminance integration with gamma correction 
Metallic: saturation + specular estimation from luminance 
Real-time 3D preview uses Three.js + custom HDRI loader, running at 60fps.
The Seamless Texture Maker
This was the hard part. Auto seam repair uses a 3-algorithm cascade:
Optimal offset search: finds the best tile offset to minimize edge discontinuity 
Min-cut seam repair: graph-cut algorithm to find the minimum-cost seam path 
Structural patch repair + low-frequency balance: handle remaining artifacts 
Plus clone and healing brushes for manual touch-up, and a delight pass to remove uneven lighting before tiling.
AI Integration
Added AI texture generation from text prompts (FLUX + other models via Runware). Users can generate a source texture from a prompt, which automatically feeds the PBR pipeline. Credit-based pricing: 5 free credits/day, paid plans from $19.90/month.
Results
The free tier covers 90% of use cases for hobbyists and indie devs 
AI generation is where the revenue comes from 
Biggest surprise: transparent PNG maker (black + white matte removal for VFX) became a top use case I didn't anticipate 
Tech Stack
Frontend: Astro + TypeScript 
Rendering: WebGL / Three.js 
Auth + DB: Supabase 
Payments: Creem 
AI providers: Runware + Kie 
Questions for IH:
How do you price free-tier limits to convert without annoying power users? 
Anyone else building browser-native GPU tools? What's your WebGL/WebGPU strategy? 
Try it: https://normalmap.ai 
Try it out here: NormalMap AI 
NormalMap AI main interface: AI Generate panel, real-time 3D sphere preview, and full PBR map thumbnails (Normal, Roughness, AO, Metallic, Height, ORM). 
A full-resolution tangent-space normal map (blue-purple) ready for Unity, UE5, or Blender. 
Top comments (0) 
Subscribe 
Personal 
Trusted User 
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit 
Preview 
Dismiss 
Code of Conduct 
• 
Report abuse 
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
