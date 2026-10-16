---
source: "https://unity.com/blog/foxy-dumplings-cross-platform-development"
title: "How Soft Crunch Games built Foxy Dumplings for every platform"
author: "Adam Axler"
date_published: "2026-10-16"
date_clipped: "2026-10-16"
category: "Game Development / Unity"
source_type: "rss"
---

# How Soft Crunch Games built Foxy Dumplings for every platform

Preparing the same game for PC (Windows, macOS, and Linux) via Steam, GOG, the Epic Games Store, and the Microsoft Store with Xbox Play Anywhere, as well as on Nintendo Switch™ 2, Nintendo Switch, PlayStation®4, PlayStation 5, Xbox Series X|S, iOS, and Android at the same time is an ambitious technical challenge for any studio. For the four-person core team at [Soft Crunch Games](https://softcrunch.games/), it meant making cross-platform development part of the game’s architecture from the beginning.

[*Foxy Dumplings*](https://store.steampowered.com/app/4184130/Foxy_Dumplings/) is a cozy cooking and management game about Lisa, a professional chef recovering from burnout by starting over with her family’s dumpling recipe and a food truck. Players travel through 12 locations inspired by real food cultures, grow ingredients, learn regional recipes, run the truck, and invent their own dishes.

Grzegorz Wątroba handles all programming, platform ports, build pipelines, and certification work. With one programmer responsible for that many targets, the project was built around one rule: Every platform gets the same game from the same commit.

## **One project, one branch, one game**

In practice, that meant no compromises: There are no separate branches, no mobile edition arriving half a year later, and no version with half the content.

That became a few rules. That became a few rules. Every control scheme had to be complete on its own, so players can finish the game using only a controller, only a touchscreen, or only a mouse – with or without a keyboard. The save file uses the same binary format everywhere, so moving progress between devices does not require conversion.

The save file uses the same binary format everywhere, so moving progress between devices does not require conversion.

“We also treated certification requirements as design constraints from the start,” says Wątroba. “*Foxy Dumplings* has no text input fields, for example, so we never have to deal with on-screen keyboards on multiple different systems. PC store SDKs such as Steamworks are stripped out of console and mobile builds automatically.”

He wanted every build to come from one menu without anyone touching Project Settings by hand. Today that menu has more than 70 entries across platforms, build types, demos, tester builds, and output configurations.

## **Keeping platform code at the edges**

*Foxy Dumplings* is one Unity project and one branch. Gameplay is always shared. Platform code is only allowed at the edges, where the game talks to the system: saving, user accounts, achievements and trophies, cloud synchronization, DLC checks, system dialogs, and exporting photos.

Wątroba says, “Each system sits behind an interface. We use a facade pattern to give gameplay one entry point, then a small factory selects the correct platform provider at startup. Gameplay might say, ‘unlock this achievement,’ but it does not know whether that ends up on Steam, PlayStation® Network, or nowhere at all.”

Runtime configuration handles most differences, such as whether the player can quit to desktop or open a web link. Scripting define symbols passed in by build scripts handle cases such as excluding Steamworks from a non-Steam PC build. Unity platform defines are the last resort, only where code cannot compile elsewhere.

Text differences are data too. Localization keys have platform variants, so “Achievement” can become “Trophy” on PlayStation® without changing gameplay code.

Foxy Dumplings | Soft Crunch Games

## **Automating anything that happens twice**

The way Wątroba keeps the workload manageable is partly experience and partly refusing to do the same thing twice. Anything repeated across platforms eventually became a script or menu item.

Making a specific build is one click with the correct defines, output folder, and settings. They also run compile checks across roughly 40 platform and store configurations, catching the classic “it compiles on Windows but breaks on PlayStation” problem before QA sees it.

Scope matters too. “We said no to features that multiply platform work: text input, online features we would have to host or moderate, and in-game purchases. We also ship one PlayStation build that runs on both PlayStation 4 and PlayStation 5,” he says.

Contractors do not need to think about platforms. UI is designed once on a 4K canvas and scaled per platform. The sound team works in one FMOD project. The game designer builds content in the same data assets everywhere. He says,“Platform differences are my job, not theirs.”

Foxy Dumplings | Soft Crunch Games

## **Designing input and UI before writing code**

The first step for Wątroba was designing on paper with the *Foxy Dumplings* team’s UX designer.

“I have seen projects suffer because input and UX were not thought through at the beginning,” says Wątroba. “Our approach was essentially: This is our game, make it work on each platform.”

Solving those problems on paper before the first line of code helped the team avoid a lot of trouble later.

Once the UX was complete, they built controls around the Input System with one set of actions and three control schemes: gamepad, keyboard and mouse, and touch. The game switches schemes live based on what players used last, and the UI follows automatically.

The team used a single button-prompt Prefab in almost 200 places. It understands the input for each platform. “Pick up a controller and the prompts change; move the mouse and they change again,” he says.

Cooking minigames were the hardest part because each one must work with every input method. Steam Deck taught them an important rule: Never ask whether a device is present; ask whether it can actually produce the input you need.

Wątroba explains, “Its touchscreen can appear as a mouse and left button, which once made a minigame requiring both mouse buttons impossible to finish. Designing around capabilities rather than devices also helped on older Android hardware.”

Foxy Dumplings | Soft Crunch Games

## **Profiling the weakest hardware first**

*Foxy Dumplings* is a 2D game with Spine characters and unlit materials, so when the GPU struggles it is usually because of too many fullscreen layers or too many pixels.

One example was the kitchen. Some effects were rendered into a 4K render texture and composited over the UI – unnecessary on a 1080p or 720p display. Watroba changed the render textures to follow the actual screen resolution and disabled HDR and depth textures, which the game never used. Visually, nothing changed, but on Steam Deck that layer now fills about 8× fewer pixels every frame, and its render texture dropped from about 32 MB to about 4 MB.

Wątroba’s profiling process is the same one he learned years ago: He makes a development build on the actual device, attaches the [Unity Profiler](https://docs.unity3d.com/6000.3/Documentation/Manual/Profiler.html), finds what is expensive, measures it, fixes it, and measures again. He says, “The device is the king.”

Memory also needs attention. The team supports 14 languages, including Chinese, Japanese, Korean, and Thai, each with its own font atlas. When the team saw memory spikes during language changes, they profiled the allocation path and found that characters missing from the static atlases were rasterized at runtime into oversized 4096×4096 fallback atlases, with a full 16 MB atlas re-upload for every new character.

The fix was regenerating the fallback fonts with 2048×2048 pages and adding glyphs in batches before the switch, which cut the new atlas memory for Japanese from about 48 MB to 4–8 MB per font.

The team used [Addressables](https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.addressables.html) in the project because [Unity Localization](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/index.html) is built on them. String and asset tables for all 14 languages live in Addressable groups and load per language. “Everything still ships locally, but Addressables give us a clean way to manage that data and memory.”

Foxy Dumplings | Soft Crunch Games

## **Testing shared gameplay once, platform behavior many times**

The team does not have a large automated test suite, but they automate some systems, including simulations that check whether the in-game economy can collapse.

What keeps QA manageable for them is that platforms share almost all of their code. Gameplay gets tested deeply on PC, where iteration is fastest. On consoles and mobile, testing focuses on the platform layer: certification requirements, saving and loading, suspend and resume, switching users, controller disconnects, trophies and achievements, and running out of storage.

“Our external QA partner gets release, debug, and a ‘full unlock’ release with debug tools,” says Wątroba. “Testers can jump to any chapter or mission and manipulate money, energy, or time, so they do not have to replay five hours to verify one bug.”

The public demo has also been a major source of testing. More than 18,000 people have played it, and the team received over a thousand survey responses that led to accessibility features, bug fixes, tuning, and quality-of-life improvements.

## **Making cross-platform saves portable first**

Cross-platform progression started with making the save itself portable. Progress is one encrypted binary file, byte for byte the same format on every platform. A save written on mobile can be read on PC.

Synchronization has two layers. The first is each platform’s native cloud save. The second is Unity [Cloud Save](https://docs.unity.com/en-us/cloud-save), which carries progress between ecosystems. Both sit behind the same interface, with merge logic above them.

Each save slot is compared by its last-update timestamp. Deleted slots leave a marker so they do not return from the cloud. Merging only happens in the main menu, never in the middle of a game day, because *Foxy Dumplings* saves when the player goes to sleep. Uploads retry quietly when there is no network and flush when the game is suspended.

The team links a console and PC using [Unity Authentication](https://docs.unity.com/en-us/authentication) code linking, so players do not need another account. Cross-progression is opt-in, and the game remains fully playable offline.

Wątroba says,“The biggest lesson was that storage is the easy part; identity is the hard part. Every ecosystem has its own idea of who the player is, so Authentication has to trust Steam tickets, PlayStation tokens, and Xbox tokens separately.”

Foxy Dumplings | Soft Crunch Games

## **Building Foxtagram without creating another platform problem**

Foxtagram is an app on Lisa’s in-game phone where players compose photos of dishes using plates, tableware, ingredients, dumplings, filters, frames, and stickers, before posting them to build restaurant popularity.

The main architectural decision was to keep the editor in regular Unity UI with no platform-specific code inside it. Wątroba explains, “Its 50 filters are presets of one shader on the photo material rather than overlays. When you take a photo, a dedicated camera renders the photo area into a square render texture at the output resolution. We read it back with AsyncGPUReadback and encode the result as a JPG. That frame looks like a camera flash.”

Output resolution and JPG quality come from per-platform settings. The editor supports mouse, controller, and touch: drag and mouse wheel on desktop; sticks and triggers on controller; and pinch and twist on touch.

Sharing outside the game goes through each platform’s own tools. PC can use the photo folder or Steam media library, consoles use their system albums, and mobile uses the system share sheet. For a small team, using the platform’s existing sharing features removes a lot of certification and moderation work.

Foxy Dumplings | Soft Crunch Games

## **Moving to Unity 6.3 LTS**

“The most valuable thing [Unity 6.3 LTS](https://docs.unity3d.com/6000.6/Documentation/Manual/WhatsNewUnity63.html) brought was an LTS release where everything we depend on lines up and whose support window covers our launch needs,” says Wątroba.

The team found 6.3 more stable in areas such as editing ScriptableObjects, and older Android devices benefited from Vulkan fixes.

Build times improved too. “With IL2CPP, I would estimate our builds are roughly 10–15% faster depending on the platform and type of iteration. Runtime performance also improved by a few percent, especially on weaker hardware.”

The upgrade was mostly smooth. Every [VFX Graph](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@17.4/manual/index.html) effect initially became invisible because shader references were lost during migration; reimporting the graphs quickly fixed that.

## Planning the port before there is a port

The decision with the biggest impact for the team was keeping one branch and being strict about platform differences from the beginning. “Gameplay code never asks what platform it is running on. If something differs, it is data, a quality setting, or a provider behind an interface,” says Wątroba.

The team created a technical architecture document alongside the game design document, art bible, and narrative bible, which they recommend doing. Wątroba notes, “Drawing the game’s technical layers before production helped us keep responsibilities separate and made adding platforms much easier.”

Next time, the team would get builds running on every dev kit much earlier. “The architecture was right, but a lot of real console work still landed in the months before submission, and hardware always finds things the Editor will not.”

Foxy Dumplings | Soft Crunch Games

## **Shipping one game everywhere**

*Foxy Dumplings* is built around a simple technical promise: the same game, from the same codebase, across PC, console, and mobile. For a small team, that only works if cross-platform development is treated as an architectural constraint rather than a porting task saved for the end.

“By keeping gameplay shared, isolating platform integrations, automating repetitive build work, and testing against the weakest targets early, we’re aiming to make simultaneous launch less about maintaining many versions of *Foxy Dumplings* and more about shipping one game everywhere,” says Wątroba.

**[Foxy Dumplings](https://foxydumplings.com/) *will be available on PC (Windows, macOS, and Linux) via Steam, GOG, the Epic Games Store, and the Microsoft Store with Xbox Play Anywhere, as well as on Nintendo Switch 2, Nintendo Switch, PlayStation 4, PlayStation 5, Xbox Series X|S, iOS, and Android in 2027. Check out more stories from Unity developers on the [Unity Blog](https://unity.com/blog) and [Resource Hub](https://unity.com/resources).***

*\*Nintendo Switch is a trademark of Nintendo.*
