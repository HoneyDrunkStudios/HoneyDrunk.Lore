---
source: "https://dev.to/timmyzinin/after-genie-3-38-alternatives-for-ai-scene-generation-51i7"
title: "After Genie 3 — 38 alternatives for AI scene generation"
author: "DEV.to Unity"
date_published: "Tue, 05 May 2026 12:22:24 +0000"
date_clipped: "2026-05-06"
category: "Game Development / Unity"
source_type: "rss"
---

# After Genie 3 — 38 alternatives for AI scene generation

Source: https://dev.to/timmyzinin/after-genie-3-38-alternatives-for-ai-scene-generation-51i7

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3781639) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
Tim Zinin 
Posted on May 5 
After Genie 3 — 38 alternatives for AI scene generation
# gamedev 
# ai 
# unity3d 
# webgl 
Ok so Google's Genie 3 is locked behind US geo and $250/month. VPN gets detected. The rest of us get nothing. Or so I thought.
I've been slowly making a small Unity game, and at some point got curious what we actually can use outside the US. Spent a week digging around.
World models
Tencent HunyuanWorld 2.0 with open weights. Marble from Fei-Fei Li's World Labs. Odyssey-2 in free preview right now. Decart Oasis streaming 360p in real time. Alibaba Wan 2.2 on Apache 2.0.
3D assets
Hunyuan3D 2.1 generates 4K PBR meshes on 6 GB VRAM. Ran it on my home GPU, no issues. Meshy and Tripo as commercial fallback. UnityGaussianSplatting by Aras-P turns a phone room scan into a playable WebGL iframe on a client site.
Prompt-to-game
Rosebud AI ships a playable Three.js prototype from a prompt. Phaser 4 with Claude Code skills if you want full IP and pay only in LLM tokens.
NPCs
Convai gives you a voiced character through an npm widget in an evening. AI Town from a16z-infra embeds via iframe, MIT license, runs on a home Hetzner GEX44.
Payments
fal.ai takes USDC and covers Kling, Wan, Hailuo, Seedance, Hunyuan Video through one endpoint.
Infra
Hetzner GEX44 at €184/month with 20 GB VRAM runs 80% of the open-source inventory locally.
Three playbooks by budget, from $50/month on fast browser demos to $5–15K per premium Web3 scene.
Full breakdown of 38 models across 7 categories: https://timzinin.com/after-genie3/?utm_source=devto&utm_medium=blog&utm_campaign=after-genie3&utm_content=apr18 
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
