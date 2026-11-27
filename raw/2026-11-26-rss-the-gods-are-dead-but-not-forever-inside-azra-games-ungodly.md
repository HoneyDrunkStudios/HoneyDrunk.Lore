---
source: "https://unity.com/blog/ungodly-azra-games-mobile-rpg-unity"
title: "The gods are dead. But not forever: Inside Azra Games’ UnGodly"
author: "Philip Bang"
date_published: "2026-11-11"
date_clipped: "2026-11-26"
category: "Game Development / Unity"
source_type: "rss"
---

# The gods are dead. But not forever: Inside Azra Games’ UnGodly

##### *How Azra Games is bringing console-quality combat and dark-fantasy storytelling to mobile and beyond with Unity.*

[UnGodly](https://ungodlygame.com/) *is a dark-fantasy action RPG from Azra Games, built with [Unity](https://unity.com/solutions/mobile) to reach players across mobile, Mac, PC, and Apple Vision Pro with a console-like experience to the device in your pocket. In this guest blog, Philip Bang, vice president and general manager of* UnGodly *at Azra Games, describes the team’s vision, why they bet on a fourth generation of mobile RPGs, what it means to respect the player, and why they’re building with Unity for players across platforms, including the new [iPhone Duo](https://www.apple.com/ca/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo/).*

## **A world without gods**

In the world of *UnGodly*, the gods are dead, betrayed by those they created. In the broken world that remains, you lead the Divine Legion, an ancient order of heroes with god-like power, at the vanguard of the final battle in the eternal war between the Divine, which creates, and the Devouring, which consumes.

You play as Primals, warriors whose blood carries the power of the fallen gods. You recruit them across mortal and immortal realms, then craft teams from their unique powers to fight in brutal real-time combat. Between journeys, you return to the Velvet Shroud, part temple and part tavern, where your companions gather. Their stories unfold through Primal Quests, and Primals who fight together grow closer through romantic and platonic Affinity Quests.

The Primals carry the power of the Divine, but they are still mortals with their own wounds, loyalties, and ambitions, and they can hear the whispers of the Devouring. Through their stories, you confront what their power has cost them and what they still hope to protect, or to gain.

This is the dark-fantasy action RPG we’re building at Azra Games. We built it on [Unity 6.3 LTS](https://unity.com/products/unity-engine) with the [Universal Render Pipeline (URP)](https://learn.unity.com/course/unity-6-universal-render-pipeline), and it now runs on iPhone, iPhone Duo, Mac, Google Play Games on PC, and Apple Vision Pro.

## **Building the fourth generation of mobile RPGs**

When Mark Otero founded Azra Games in 2022, he had a clear conviction: Mobile was ready for its next generational leap. As the creator of *Star Wars: Galaxy of Heroes* at Electronic Arts, Mark helped establish the modern character-collector RPG as one of mobile’s most successful genres.

Since then, the hardware, the audience, and players’ expectations have all moved on. Players who have grown up with rich worlds, responsive combat, and cinematic storytelling on console and PC now expect the same wherever they play.

“When we founded Azra back in 2022, the entire thesis was that mobile was finally ready for a true fourth-generation RPG,” Mark told [PocketGamer.biz](https://www.pocketgamer.biz/azra-games-ceo-mark-otero-on-betting-50m-on-ungodly-and-building-for-iphone-duo/).

Our goal was simple to state and hard to execute: build the fourth generation of mobile RPGs. That means bringing together the accessibility and long-term progression of mobile character collectors with the visceral combat, cinematic storytelling, and visual fidelity of console RPGs, without compromising one experience to accommodate the other.

It also meant choosing technology that could keep up across a growing range of devices. For us, that was Unity.

## **Console quality on mobile hardware, built on Unity**

We want the richness and visual engagement of a modern console game with the convenience of a mobile device, but we also need to reach players on devices with very different performance profiles. That means balancing visual fidelity, memory, rendering cost, and content delivery.

We built *UnGodly* on Unity 6.3 LTS, using URP with Forward+ rendering. Forward+ gives us the flexibility to support the dynamic lighting and visual effects that define the game, from atmospheric environments and imposing architecture to combat encounters filled with spectacular abilities.

We combine baked and real-time lighting to give *UnGodly* its distinctive atmosphere while keeping rendering costs under control. That balance matters most during combat, where multiple Primals, enemies, and visual effects can be active at once.

Our central technical challenge has been maintaining responsive real-time action combat without compromising the visual spectacle. Players need to read enemy attacks, execute precise dodges, switch between Primals, and unleash powerful Essence Bursts, all while the world around them stays visually rich and alive. Unity’s rendering pipeline gives our artists and engineers the tools to make deliberate choices about where visual complexity matters most and where performance must take priority.

But rendering is only half the job. An RPG of this scale carries a large and constantly growing library of characters, environments, animations, and effects. Unity’s [Addressables](https://unity.com/how-to/simplify-your-content-management-addressables) system helps us organize and manage that content, supporting a development pipeline built for both launch and years of ongoing updates. *UnGodly* is a live game, and a shared technology foundation lets our teams spend their time on gameplay and content instead of re-solving the same problems for every device.

## **iPhone Duo: built for where mobile is going**

Apple’s first foldable iPhone changes how a phone can present a game. A device that moves between a compact phone and a larger display opens up new options for gameplay and immersion. For *UnGodly*, it was a natural extension of our original vision: a game that adapts as hardware evolves instead of staying bound by old assumptions about what a mobile RPG should be.

With support for iOS 27 Auto Resizability, *UnGodly* adapts to iPhone Duo’s folded and unfolded configurations. Players can experience combat in both portrait and landscape, while we continue expanding dual-orientation support across the game’s interface. On iPhone Duo and iPhone 18 Pro, the game runs at up to 60 frames per second, helping deliver the responsive action experience at the heart of our design.

Seeing *UnGodly* featured in Apple’s September reveal was a proud moment for the team. As Mark put it: “That wasn’t us chasing new hardware. It validated a bet we made a long time ago.”

The gap between a mobile RPG and a console RPG is now less about what the hardware can do and more about what developers choose to build. That’s an exciting place to be.

## **One universe, many ways to play, on one Unity foundation**

When we started *UnGodly* in 2022, some of the devices we support today didn’t exist yet. The lines between mobile, PC, and new computing platforms are blurring fast, and we want players to experience *UnGodly* wherever they prefer. That has taken us beyond phones and tablets to Mac, Google Play Games on PC, and Apple Vision Pro.

Each platform asks something different. Touch controls need to feel intuitive on a phone. Precision has to carry over to keyboard, mouse, and controller. [Spatial computing](https://unity.com/blog/engine-platform/spatial-apps-for-apple-vision-pro) opens up entirely new ways to interact with a game world. Controls, interface, presentation, and performance each need attention per platform, but [Unity’s multiplatform support](https://unity.com/features/multiplatform) gives us a shared foundation, so we can bring *UnGodly* to new platforms without rebuilding the entire game for each one.

## **Combat and characters built for every screen**

At the heart of *UnGodly* is a simple belief: Combat should be something you experience, not something you watch. Players command a party of four characters called Primals, switching between them in real time, dodging attacks, chaining abilities, and unleashing devastating finishers called Essence Bursts. Combat is fast and deliberately brutal, and it has to stay responsive whether players use touch, a controller, or a keyboard, on a phone or a foldable.

Our visual direction draws heavily on the legendary fantasy illustrator Frank Frazetta: muscular silhouettes, imposing enemies, battered armor, and savage beauty. Internally we call it dark fantasy meets *Mad Max*. We don’t want a game that merely looks impressive on a phone. We want players to forget they’re on one.

The characters matter as much as the combat. Our Primals are scarred survivors with complicated histories and deeply personal reasons for fighting, led by Vander, a mercenary haunted by loss, and Damea, a young woman whose very existence holds the apocalypse at bay. Through the Affinity system, players build relationships between Primals and uncover new stories, rivalries, and romances.

## **Respecting the player**

One phrase has guided our development from the beginning: Respect the player. It’s easy to say and much harder to deliver. Free-to-play games have created extraordinary experiences, but they can also demand too much of players’ time through endless checklists, repetitive chores, and systems that reward obligation over enjoyment.

Our answer is what we call a daily dark adventure. Players with limited time should enjoy meaningful combat, rewarding progression, and a complete, worthwhile session. Those who want to spend hours mastering combat, developing characters, and competing will find that depth in modes like the Nethermaw Descent.

This isn’t about making the game smaller. It’s about making every minute matter.

## **A world built to grow**

Launch is a milestone, not the finish line.

We’re building a dark-fantasy universe meant to grow for years: more of Tarsea to explore, new Primals, and new ways to dig into the relationships and conflicts at the heart of the story.

In December, Conan the Barbarian joins *UnGodly* as a guest character, a fitting collaboration given how much Frank Frazetta’s Conan illustrations shaped our visual identity. We’re also expanding our reach, with releases planned on Galaxy Store and ONE Store, so more players can play on more devices.

## **Into the labyrinth**

Every hero’s journey runs through a labyrinth. You go in to face what’s waiting there, and you come out changed. Our heroes make that descent, and in a way, so did we.

We set out to challenge assumptions about what a mobile RPG can be, combining the depth and spectacle of console games with the reach of mobile free-to-play, and building something that can evolve with the hardware that makes it possible.

With Unity, we’re bringing that vision to life across a growing range of platforms.

The fourth generation of mobile RPGs isn’t something we’re waiting for. We’re building it.

The gods of Tarsea are dead. Their world is broken.

It’s up to the players to bring them back.

***Discover* [UnGodly](https://ungodlygame.com/), *explore [multiplatform development with Unity](https://unity.com/features/multiplatform), and read more developer stories on the [Unity Blog](https://unity.com/blog) and [Unity Resource Hub](https://unity.com/resources).***
