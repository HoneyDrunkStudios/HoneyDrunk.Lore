---
source: "https://80.lv/articles/how-to-add-colored-shadow-penumbra-in-unreal-engine-5/"
title: "How To Implement Colored Penumbra Shadows In UE5"
author: "Amber Rutherford"
date_published: "2026-06-04"
date_clipped: "2026-06-04"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# How To Implement Colored Penumbra Shadows In UE5

Source: https://80.lv/articles/how-to-add-colored-shadow-penumbra-in-unreal-engine-5/

Amber Rutherford Senior Editor 04 June 2026 How To Add Colored Shadow Penumbra In Unreal Engine 5 # News # Unreal Engine Oscar Sanz, Senior Technical Artist at CD Projekt Red, has written a blog post.
Chosker Even if you don't know the term, you've probably noticed the effect itself, often visible in the penumbra of an image and often exaggerated by artists. It's the soft, transitional edge of a shadow that gets additional color, and it's an important technique artists use to add visual clarity to their work.
3D is no different. If you want to add colored shadow penumbra to your Unreal project, Oscar Sanz, also known as Chosker, has written a guide explaining how to implement it by editing the shaders. He was inspired by this project from Romain Durand :
View this post on Instagram A post shared by Romain Durand (@rdurandart) 
If you're interested in the theory, read this Medium article by Shahriar Shahrabi.
Chosker explains that his approach is fairly simple to implement and avoids the need to guess light and shadow values like a post-process solution, which can be especially tricky with Lumen or day/night cycles. It also works with all light types and is very lightweight in terms of performance. However, the color saturation can only be adjusted globally rather than per light or scene, the effect needs wide penumbras to be noticeable, and it only works with dynamic lights, not baked lighting.
You only need to edit the engine shaders, so you can stick with the launcher version. If you're not familiar with how engine shader files can be edited, check out this Chosker's article to learn more and get started. Read the article on the implementation of colored shadow penumbra here . 
Chosker If you haven't seen what's new in Unreal Engine 5.8, the preview adds the experimental Mesh Terrain system and more : 
Also,  subscribe to our Newsletter  and join our  80 Level Talent platform , follow us on  Twitter ,  LinkedIn ,  Telegram , and  Instagram , where we share breakdowns, the latest news, awesome artworks, and more. 
Are you a fan of what we do here at 80 Level? Then make sure to  set us as a Preferred Source on Google  to see more of our content in your feed. 
Subscribe to 80 Level Newsletters Latest news, hand-picked articles, and updates
Subscribe I consent to receive emails from 80 Level Privacy Policy Terms of use Built for Creators. Read by the Best Partner with 80 Level Comments 0 Type your comment here Leave Comment Built for Creators. Read by the Best Partner with 80 Level
