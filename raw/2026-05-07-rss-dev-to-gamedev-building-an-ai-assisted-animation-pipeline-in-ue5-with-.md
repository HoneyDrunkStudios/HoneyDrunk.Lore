---
source: "https://dev.to/domtechgaming/building-an-ai-assisted-animation-pipeline-in-ue5-with-hy-motion-dev-log-13-okb"
title: "Building an AI-Assisted Animation Pipeline in UE5 with HY-Motion (Dev Log #13)"
author: "DEV.to Gamedev"
date_published: "Wed, 06 May 2026 20:53:47 +0000"
date_clipped: "2026-05-07"
category: "Game Development / Unity"
source_type: "rss"
---

# Building an AI-Assisted Animation Pipeline in UE5 with HY-Motion (Dev Log #13)

Source: https://dev.to/domtechgaming/building-an-ai-assisted-animation-pipeline-in-ue5-with-hy-motion-dev-log-13-okb

try {
if(localStorage) {
let currentUser = localStorage.getItem('current_user');
if (currentUser) {
currentUser = JSON.parse(currentUser);
if (currentUser.id === 3862622) {
document.getElementById('article-show-container').classList.add('current-user-is-article-author');
}
}
}
} catch (e) {
console.error(e);
}
DomTech Gaming 
Posted on May 6 
Building an AI-Assisted Animation Pipeline in UE5 with HY-Motion (Dev Log #13)
# gamedev 
# ue5 
# ai 
# animation 
Development continues on the gameplay animation systems for Magickness™.
In Dev Log #13, I showcase the current AI-assisted animation workflow being integrated into the project using HY-Motion (HY Animotion), Blender, and Unreal Engine 5.
The goal of this pipeline is to streamline gameplay animation iteration while maintaining compatibility with the existing Mixamo-based character framework already established in the project.
Current Workflow
Generate animation in HY-Motion
Export FBX
Trim/refine in Blender if needed
Import into UE5 using the existing SMPLH skeleton
Retarget using a custom SMPLH → Mixamo retargeter
Export finalized gameplay animation
One important part of the workflow is that the retarget pose is stored directly inside the UE5 retargeter asset itself, meaning future animations can reuse the same pipeline without rebuilding the setup every time.
This allows future gameplay abilities and combat systems to iterate significantly faster while keeping the animation framework consistent across the project.
Magickness™ is a discovery-driven MMORPG currently in active development.
Website:
https://magickness.com/ 
Support development:
https://ko-fi.com/domtechgaming 
YouTube Dev Log:
https://youtu.be/_BEMC1-BY_I 
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
