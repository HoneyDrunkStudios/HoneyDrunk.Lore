---
source: "https://unity.com/blog/another-axiom-gorilla-tag"
title: "Keeping a VR giant fresh: Gorilla Tag’s two-week live ops cadence"
author: "unknown"
date_published: "2026-08-18"
date_clipped: "2026-08-26"
category: "Game Development / Unity"
source_type: "rss"
---

# Keeping a VR giant fresh: Gorilla Tag’s two-week live ops cadence

Source: https://unity.com/blog/another-axiom-gorilla-tag

Blog
Keeping a VR giant fresh: Gorilla Tag’s two-week live ops cadence Aug 18, 2026 | 0:00 Min Adam Axler - Unity Senior Content Marketing Manager Target platforms Testing and performance Target platforms Testing and performance Gorilla Tag has grown into one of the biggest social games in VR, built around a hand‑based locomotion system that lets players run, climb, and swing using nothing but their arms. To keep this world feeling alive, Another Axiom delivers updates on an aggressive two-week schedule, with new maps, cosmetics, and gameplay modes launching simultaneously across all VR platforms the game supports.
Maintaining this rhythm consistently across multiple VR platforms brings its own technical demands. The team has to keep performance, comfort, and stability solid, while giving custom map creators the tools to build new content without breaking that consistency.
We spoke with Derek Arabian, producer at Another Axiom, about building and running Gorilla Tag ’s live ops strategy: the technical goals behind a two‑week update cycle, keeping user‑generated content performant across platforms, the making of the space map update, and what it takes to hit consistent VR performance targets.
What were your primary technical goals for running live ops consistently across separate VR platforms?
Derek Arabian: Performance is the most important thing for us, first and foremost, because in VR, a consistent frame rate is critical for comfort – that’s the number one priority in headset. Outside of that, we focus on smooth, easy access into the game: minimizing frustration or pain points before players get to the fun. And beyond that, we hold to the usual live‑service fundamentals – high uptime on services, and minimizing game‑breaking bugs or major issues that stop players from playing the game they love.
What were the biggest technical challenges in keeping your two-week update cadence consistent?
The biggest challenge in keeping our two‑week cadence in sync across VR platforms is making sure everything – functionality and usability – passes consistently across each platform.
On PC platforms specifically, there are meaningful differences in shaders and builds that we have to account for, and because our cadence is so aggressive, our QA time is genuinely minimal. The biggest piece of that is getting testing done across every platform and build, actually in headset, and confirming everything works before it goes live – that’s tough to do well on a two‑week cycle.
Gorilla Tag | Another Axiom
What challenges came up keeping user-generated content (UGC) and custom maps performant and consistent?
There are a lot of challenges with user‑generated content and custom maps. The biggest one is that once you give people the tools to build things, they want to go all out – which is great, because our community is incredibly creative and does amazing things even within constraints.
To keep UGC and custom maps performant and consistent, we built a sandbox with limitations in mind: caps on the number of polygons in a custom map, limits on active objects, and constraints tied to their performance impact.
We also use a form of whitelisting for user‑generated content. Gorilla Tag has a lot of components, and we only allow a subset of those into generated content – the ones we know are stable, safe for all users, and unlikely to cause major configuration issues. As we improve our internal tools, we move more of them into the UGC and custom map pool, so creators keep getting more to work with over time.
How do you plan and prioritize what ships in each two-week update cycle?
The team has big aspirations, so planning each cycle really comes down to how much we can fit in. We make sure every two‑week slice ships some new features and content. Outside of that, we work across a variety of Git branches to assemble different features, fixes, and improvements across the game.
Each cycle breaks down into roughly one week of combining – collating everything that can realistically make it into that cycle and merging it into our release branch – and a second week focuses on stabilization: polishing and making sure everything’s in a good state before it ships.
Beyond the two‑week level, planning also happens strategically: making sure the team plans bigger story beats, narrative events, and seasonal updates planned well ahead of time. So there are really two tracks: a strategic track for the bigger picture, and a tactical track that comes together in each two‑week cycle.
Gorilla Tag | Another Axiom
How did the Universal Render Pipeline (URP) help you iterate on new content?
Switching to URP was a big help – we saw significant performance improvements across several platforms. We moved to a URP shader setup built around one uber shader with a number of variants, which gave us a major performance win by minimizing draw calls and reducing the number of non‑batchable objects.
How did Addressables and Cloud Build Automation help with supporting fast, low-friction updates across platforms?
Addressables are important for us because Gorilla Tag has a massive cosmetic catalog – cosmetics are our only monetization, so it’s all decorative, no pay‑to‑win. As a live game shipping every two weeks, that catalog has grown a lot over the years, and Addressables helps us take all of those assets and package them into an Opaque Binary Blob (OBB).
On Meta Quest, there are limits on APK size, so once you pass a certain size, assets need to move into the OBB. Addressables are helpful for splitting up our APK when building in Unity, and making sure assets load from the right place at the right time to keep performance solid.
Unity Build Automation is close to a requirement for running a live game with turnaround times as short as ours – you need a continuous deployment pipeline, at least for internal use. It’s been important for getting consistent builds across our different branches, all flowing up to release channels so we can load them onto headsets quickly for iteration. For turnaround time, it’s really important.
Gorilla Tag | Another Axiom
What impact did your UGC tools have on community-driven content and social features?
Our UGC tools have been a huge part of Gorilla Tag ’s continued popularity. Tapping into the creativity and passion of our players, and letting that add to our game’s content, is a massive win from a development perspective. UGC is some of our stickiest content – players are genuinely most passionate about it, and they spend a lot of time there.
The impact is significant, and we’re continuously trying to improve the creation and access flow, because it’s some of our best content, and we want it to be as easy as possible for everyone to create and enjoy.
What Unity 6 features or tools made the biggest difference in building and executing your live ops strategy?
The Unity 6 upgrade was a long time coming for us. The Editor usability improvements are substantial, and a lot of tools just generally work better. If I had to pick one that stood out to me personally, it’s the improved search in Unity 6 compared to older versions – it’s noticeably faster and more capable.
Beyond that, there’s a lot of well‑rounded improvement across the board: prefab controls, build profiles, and a bunch of smaller wins that added up to a big overall improvement for us.
Gorilla Tag | Another Axiom
Your space map update changed gameplay by reworking gravity and you later opened it up to custom map creators – what did that unlock, and how did player feedback shape further iteration?
The space map update was long‑awaited. We’d been hinting at it for years, and it was one of our most requested gameplay features. It meant really looking into how playing with gravity would affect the player’s experience in VR. There are a lot of fundamental assumptions VR developers tend to make, and we wanted to challenge some of those.
Digging into the space map and all the ways we could change and manipulate gravity in that playground unlocked a lot of new gameplay possibilities we’re still exploring. Opening that up to our custom map creators sparked a ton of new minigame concepts and gameplay opportunities for them.
Messing with a player’s perspective in a VR headset has always been something we’re careful about, since there are real comfort considerations that come with it. Making sure the world space, in‑game signaling, and visuals all match up with how a player’s perspective shifts was key to solving those comfort issues.
What performance targets did you set per platform, and how did the Unity Profiler help you track and hit them?
We don’t set hard, explicit performance targets, because there’s so much variability in Gorilla Tag – room sizes range from one to twenty players, and players can be in different environments, taking all kinds of actions, and wearing any combination of cosmetics.
Instead, what matters most is keeping frame rate as consistent as possible in VR. We target Quest 2 standalone as our primary performance benchmark, since it’s a large share of our playerbase. For us, that means trying to stay as close to a steady 90 fps as possible in reasonable gameplay situations, with some allowance for dips when a lot is happening on screen. That target is our North Star for performance and gameplay decisions.
We run the Unity Profiler on every release build, and many intermediary builds, monitoring draw calls, garbage collection, and memory usage. It’s critical for tracking down what’s eating your limited frame time. VR needs to hit that high 90 fps target consistently, rendering to both eyes, so your frame time budget is short. The Unity Profiler is what lets us dig into traces and find exactly what part of the game is costing us frames or causing hitches.
Gorilla Tag | Another Axiom
What deployment decisions or optimizations mattered most for shipping live ops updates across platforms?
Improving our build automation system made the biggest impact. Having a consistent, reliable CI/CD pipeline meant everyone could test their work on‑device, in a real environment, and reliably. Getting those pipelines to one hundred percent consistency was the biggest upgrade for us. It massively improved our ability to get updates out on time and at the quality level we wanted.
What’s your top tip for developers running live ops for a multiplatform VR title?
First, listen to your audience. They’ll tell you what they want more of – lean into that excitement, and build a strong sense of what genuinely brings them joy and keeps them coming back.
Second, remember that live ops development is a marathon, not a sprint. There’s always a pull to keep adding more and more to every update, and that passion is genuinely valuable for your game. But you have to balance it against your ability to keep delivering the updates people love, consistently, over the long run.
To read more about projects made with Unity, visit the Resources page .
