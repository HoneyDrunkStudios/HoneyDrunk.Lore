---
source: "https://unity.com/blog/unite-tokyo-2026-keynote-recap"
title: "Unite Tokyo 2026 Keynote recap: Built for the speed of your ideas"
author: "Adam Smith"
date_published: "2026-11-17"
date_clipped: "2026-11-25"
category: "Game Development / Unity"
source_type: "rss"
---

# Unite Tokyo 2026 Keynote recap: Built for the speed of your ideas

Unite Tokyo 2026 had one idea at its center: [Unity 7](https://unity.com/releases/unity-7) is built for the speed of your ideas.

The Keynote showed this through three main themes. The first is how the Unity Engine enables great performance on every device, with [ECS for All](https://unity.com/ecs) bringing greater compatibility between GameObjects and Entities, and scalable graphics built into the Engine by default. The second theme is faster creation, with [Unity CLI](https://unity.com/the-unity-cli-1.0-is-here) available in 1.0 today, official plug-ins for coding agents, and a new Asset Library plug-in that searches the [Unity Asset Store](https://assetstore.unity.com/?srsltid=AYCX9vLxz4rQIfJOmuYchYDwwk9Qbl4smnFFQyrqRmVXnMZLoTAt-xX2) from inside the Editor. Finally, Unite Tokyo highlighted support for creators, with the announcement that [Synty Studios](https://www.syntystudios.com/) is joining Unity. Two local studios, QualiArts and TVT, came onstage to share how they built their hit games *[hololive Dreams](https://hololive-dreams.org/)* and *[Ratatan](https://store.steampowered.com/app/2949320/Ratatan/)* using Unity tools. The show closed with a look at the new [Unity Fellowship](https://unity.com/fellowship), which will give ten indie teams each year resources, support, and $50,000 in cash to help finish up their games, with no revenue share and no recoup.

The bilingual show at Shibuya Bellesalle Gardens in Tokyo featured speakers in both Japanese and English, with content dubbed in for both audiences in livestreams. You can watch the entire show [here](https://www.youtube.com/watch?v=ZWX5TfR1UAI), or read on for highlights, and stay tuned for English-language videos.

The Keynote from Unite Tokyo 2026

We kicked things off with a sizzle reel showcasing amazing Made with Unity games from Japan. Masaru Agarida, Managing Director of Unity Japan, welcomed the audience to the first Unite since 2019.

I took to the stage next, reflecting on the history of Unity and where we came from and how the present moment in many ways brings us full circle. After all, Unity began with three developers in Copenhagen – Dave, Joachim, and Nicholas – who were building a game called *GooBall* and ended up turning their in-house tools into Unity 1.0, over 20 years ago. Their story reminds me that building a game is still hard, and success today comes from clarity of vision and speed of iteration. Unity 7 answers with faster performance across devices and faster creation, including [official plug-ins](https://docs.unity.com/en-us/ai/unity-plugin) for Claude, Codex, Google Antigravity, and Grok. Those plug-ins ship with skills Unity's own team built, reviewed, and security checked, and millions of Unity developers are already accelerating progress using the Unity CLI.

Made with Unity games

Sangbae Nam shows new graphics tools and the *Atrio* sample scene at Unite Tokyo 2026

Sangbae Nam from the engineering team covered the technical foundation. With ECS for All, every GameObject also becomes an Entity, so existing projects gain performance as engine systems move to the Entity Component System (ECS). In a demo with 5,000 spaceships, the GameObject version slowed as the count grew, while the ECS version held a steady frame rate. Unity 7.0 will also let you view and edit Entity data in the Inspector. You can check out the demo in English [here](https://youtu.be/cAYg3rYUtkQ?si=zP9PF9FbnS_uFAwr).

The new *Atrio* sample scene showcases Unity’s latest graphics features, including Surface Cache GI

On the graphics side, a new sample scene called [*Atrio*](https://youtu.be/QfXsGwrBgVg?si=wXjL1_r26z9yZqU7) showed URP's Surface Cache GI, a dynamic global illumination system that needs no lightmaps or baking. It ran at full resolution and 60 fps and is [available on the Unity Asset Store](https://unity.com/demos/atrio) today.

[Unity Neural](https://youtu.be/gFWJb3YVVE4?si=LibTXQUo8EO280Sm) is a set of AI-powered tools for faster rendering and lower memory use. Neural Texture Compression cut Atrio's texture memory by nearly 30%. It arrives as an experimental feature in Unity 6.7 LTS, with a full release planned for Unity 7. Unity Graphics Kernel (UGK), a new graphics backend built on DirectX 12, Vulkan, and Metal, raised GPU performance in Atrio by more than 62% with ray tracing enabled.

Unity 6.7 LTS also brings customizable [2D graphics](https://youtu.be/MKs5XZl5G9Y), Physics Core 2D authoring components, and a new 2D profiler, with a [Bunny Blitz](https://assetstore.unity.com/packages/templates/packs/bunny-blitz-2d-physics-core-sample-project-426130) physics puzzle sample on the Unity Asset Store today.

Unity welcomed Chris Pruett of Meta, who talked about the [Meta VR Glasses](https://unity.com/blog/build-for-meta-vr-glasses-with-unity) announced at Connect in September and Meta’s new developer tools that allow Unity developers to take advantage of this exciting new platform.

Meta’s Chris Pruett speaks about developer tools for Meta VR Glasses to help Unity developers launch their games on this new device

[Meta VR Glasses](https://developers.meta.com/vr/discover/meta-vr-glasses/?utm_source=web&utm_medium=MVRD&utm_content=UniteTokyo) are fully immersive virtual reality glasses, not augmented reality, weighing about 100 grams with no strap, micro-OLED displays, and compute in a separate puck. Players control them with their hands and eyes, and they run existing Quest apps on the same OS, SDKs, and store. Developers can build for them today on Unity 6.7 or newer with the v209 SDK. Meta VR Glasses ship next spring, and the developer tools are available now.

Next, Keijiro Takahashi walked through one project from first idea to team production and how Unity tools help to streamline that process. He started in the terminal, prompting an agent (Claude Code with Unity's official plug-in) to build a first-person puzzle prototype in a real Unity project. The agent wrote code, compiled, read errors, and playtested. [Unity CLI](https://unity.com/the-unity-cli-1.0-is-here) is generally available today, and you can add your own commands to it.

Keijiro Takahashi takes the audience through an entire project from end to end using the Unity CLI and Pipeline API

The [Unity Pipeline APIs](https://unity.com/features/unity-production-pipeline) then brought the same project into the browser for a wider team. A producer invited collaborators, an artist swapped placeholder assets with a simple drag and drop, then checked the result in Scene Preview, and a tester pinned notes directly to objects that opened in the Editor for the developer. The Unity Pipeline API is in beta with signups open, and general availability is planned for 2027. You can watch the full demo [here.](https://youtu.be/culEkDxK6dY?si=C8lW_E60aL7s1-au)

Synty Studios’s Andrew Stairs and Mike Clephane onstage at Unite Tokyo following the announcement that Synty Studios is joining Unity

I returned to the stage to showcase a new Asset Library plug-in that’s going to make it much easier for you to find and use assets that fit the style of your project. Type what you need, and it finds that single asset across the Unity Asset Store and the assets you already own, then drops it into your scene ready to use. It also adapts assets made for the Built-in Render Pipeline to URP, and the same search works from the CLI with any agent. Materials, animations, and sounds are coming soon.

The bigger news: Synty Studios is joining the Unity family. Cofounders Andrew Stairs and Mike Clephane joined me onstage to celebrate, sharing their vision that building games should be as much fun as playing them. Moving closer to Unity means the Synty team can feed their expertise back into the Engine, making integrations tighter so that assets are even faster and easier to use. Synty assets are available through the [Asset Store](https://assetstore-fallback.unity.com/publishers/5217) and can be accessed through the CLI, and they’ll be available through [Unity Spark](https://unity.com/spark) from day one.

The new Unity Fellowship offers Made with Unity creators in their last year of production support and funding to help complete and launch their game

Aurore Dimopoulos announced the [Unity Fellowship](https://unity.com/fellowship), an annual program for 10 indie teams roughly a year from launch. Each team receives a Unity point of contact, regular expert office hours, industry connections including publisher introductions, a presence at Unity events, PR and marketing support, and $50,000 in cash. There's no revenue share, no recoup, and teams keep their IP and creative control. [Applications are open now](https://unity.com/fellowship), and the first Unity Fellowship studios will be announced at GDC in March 2027.

***Watch the Keynote on [YouTube](https://www.youtube.com/watch?v=ZWX5TfR1UAI).***
