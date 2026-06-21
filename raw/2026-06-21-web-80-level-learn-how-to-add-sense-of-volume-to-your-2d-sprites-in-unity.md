---
source: "https://80.lv/articles/how-to-make-your-2d-sprites-look-like-3d-in-unity"
title: "Learn How To Add Sense Of Volume To Your 2D Sprites In Unity"
author: "80 Level"
date_published: "2026-06-18"
date_clipped: "2026-06-21"
category: "Game Development / Unity"
source_type: "web"
---

# Learn How To Add Sense Of Volume To Your 2D Sprites In Unity

Source: https://80.lv/articles/how-to-make-your-2d-sprites-look-like-3d-in-unity

Articles Talents Events Workshops About Promote your game Advertise Log in 0 Save Copy Link Share Amber Rutherford Senior Editor 18 June 2026 How To Make Your 2D Sprites Look Like 3D In Unity # News # Unity Astral Hearts shared a quick tutorial.
This trick isn't new in any way, but if you're not familiar with how to give your 2D sprites a sense of volume using normal maps, Astral Hearts, the developer of Hellcrown , put together a short tutorial to walk you through the process.
The scene includes a character without any normal maps applied, alongside some test lighting. Astral Hearts is using Unity with the Universal Render Pipeline. For the materials, you can use the standard shader.
Astral Hearts Astral Hearts Next, generate normal maps using a free tool called Laigter , created by Azagaya Laigter. Start by importing the character atlas. After that, enable the normal map preview and turn on the Pixelated option. From there, you'll need to tweak the settings manually to get the look you want. Below are the approximate values used by Astral Hearts:
Astral Hearts After exporting the normal map, they adjusted the texture import settings in the engine. When exporting, make sure to check the Normal Map box. Finally, the texture was assigned to the normal map slot, completing the material setup.
Astral Hearts Here's how Astral Hearts set it up in the engine, but you might need to tweak some values depending on your project:
Astral Hearts Go back to the character object and assign it to the slot. That's it, you're done.
Astral Hearts We've got plenty of tutorials and tips on our site, for example, here's how to set up liquid physics using PhysBones in Unity:
Unity developers may find these recently featured tools useful: Real Fake Interiors by Amplify Creations and Adam Napper's RealTransforms , which helps with placing props using physics.
Also, subscribe to our Newsletter , join our  80 Level Talent platform , and follow us on  Twitter ,  LinkedIn ,  Telegram , and  Instagram , where we share breakdowns, the latest news, awesome artworks, and more.
Are you a fan of what we do here at 80 Level? Then make sure to  set us as a Preferred Source on Google  to see more of our content in your feed.
Subscribe to 80 Level Newsletters Latest news, hand-picked articles, and updates
Subscribe I consent to receive emails from 80 Level Privacy Policy Terms of use Keep reading
You may find these articles interesting
Setting Up Liquid Physics Using PhysBones In Unity
Paint Textures Right on Animated Meshes in Unity with This Tool
Unity Dev Open-Sources Production-Ready UI Toolkit Design System
Procedurally Generated Realistic Sea Foam In Unity
Built for the Game & Digital Art Industry Get Our Media Kit Comments 0 Type your comment here Leave Comment Built for the Game & Digital Art Industry Get Our Media Kit Subscribe Start receiving our weekly newsletter
Subscribe Facebook
@LevelEighty Twitter
@80Level YouTube
@80lv Instagram
@eighty_level Podcasts
Round Table © 2026 . 80 level. All rights reserved
About & Contact us Privacy Policy Republishing policy Terms of use Disclaimer We need your consent We use cookies on this website to make your browsing experience better. By using the site you agree to our use of cookies. Learn more
