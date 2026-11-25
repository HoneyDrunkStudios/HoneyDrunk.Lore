---
source: "https://unity.com/blog/hyper-visor-xreal-aura-physics-scenes"
title: "Tearing through reality: The tech behind Hyper Visor on XREAL AURA"
author: "Bogdan Rybak; Brieyh’leai Simmons"
date_published: "2026-11-23"
date_clipped: "2026-11-24"
category: "Game Development / Unity"
source_type: "rss"
---

# Tearing through reality: The tech behind Hyper Visor on XREAL AURA

Source: https://unity.com/blog/hyper-visor-xreal-aura-physics-scenes

# Tearing through reality: The tech behind Hyper Visor on XREAL AURA

Nov 23, 2026

Bogdan Rybak and Brieyh’leai Simmons  - Owlchemy Labs

Principal Systems Engineer and Expert Art Generalist

Platforms and publishingTarget platforms

Platforms and publishingTarget platforms

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/mTNGYl9nG3YM5OXGWYzGqaWNcERCiffDv_bYONZOoMU/w:833/h:500/r:96,0,833,500/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uL2UyMTQwZTBlYTEyYzUwZjVlMzE0M2VkYzFkZTg4MWM5ZDFlNTI2ZjUtMTAyNHg1MDAucG5n.avif)

[*Hyper Visor*](https://play.google.com/store/apps/details?hl=en_US&id=com.owlchemylabs.hyper_visor) is an [XR](https://unity.com/solutions/xr/games) arcade experience from Owlchemy Labs, built with Unity for [Android XR devices](https://unity.com/solutions/xr/games), that makes the world around you part of the game. In this guest blog, Bogdan Rybak, principal systems engineer at Owlchemy Labs, and Brieyh’leai Simmons, expert art generalist, share how they kept gameplay, pausing, and menus within one interaction model using multiple physics scenes and an energy stream.

## **Meet Hyper Visor**

We’re [Owlchemy Labs](https://unity.com/blog/engine-platform/spatial-computing-with-owlchemy-labs), the team behind *Hyper Visor*, an XR arcade experience where a mysterious pair of living shades reveal vibrant fractures in reality within your everyday surroundings. Using intuitive hand interactions, players wield a powerful energy stream to blast targets, take on challenges, and battle bosses across eight reality-bending levels.

The first feeling we wanted to achieve was a sense of mystery. We introduce windows into other realms early on, and players interact with the gameplay through those windows. They bring together the player’s space and the virtual one without binding us to the dimensions of their environment. We use visuals, not text, to guide the narrative.

Players should also feel powerful. The stream should feel like energy imbued within you, something effortless to achieve. Everything from the freedom in hand position considered “open” to the aiming of the stream itself supports that feeling.

![Hyper Visor](https://img.youtube.com/vi/EmCRzF_VkFE/hqdefault.jpg)

## **Keeping menus inside the gameplay interaction**

Every interaction in *Hyper Visor* is physics-driven. Every target is an object with a [Rigidbody](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/Rigidbody.html) that the player can sphere-cast against using their beam of energy. Targets serve both gameplay and UI, and they float around using physics. We don’t use a separate UI system.

Containing everything within one interaction was a useful design constraint. We never had to teach players anything besides how to use their stream. In the settings menu, we initially considered point-and-pinch interaction, but that would introduce interactions that weren’t present anywhere else. Instead, settings live in a module like the gameplay, where you power each button’s target with your stream.

Each target has a “life ring”: a mesh around its geometry with a colorful texture that depletes in a circular fashion, like a progress bar. UI targets behave just like gameplay targets: They deplete when targeted and regenerate when not.

With hand tracking, pinching can be finicky, whereas “point and wait” is stable, especially since you don’t perform a gesture that throws off your aim. All you need to do is not have your hand in a fist, and the beam shoots out of your wrist. We don’t use finger data for the beam’s direction; its direction depends only on head and wrist position. A closed fist means the beam is inactive, and an open hand means it’s active.

The feedback for shooting targets makes it immediately obvious what players are trying to destroy. For accidental selections, transitions are quick, and players can exit a module almost instantly. Level loads are sub-second.

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/jUzhXhcFNIBy_3cUK0bv6Eo_VOuTPVcSOTpJ_4C2kTM/w:1267/h:986/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uL2Q0NjIwMmQwOTgzNjAxZTU5NTY4NThkNWI4ZGI5OTc1YTAxYjFjMDQtMTI2N3g5ODYucG5n.avif)

An in-Editor screenshot of the Settings menu driven by a simple level script that spawns the controls

## **Separating the player, gameplay, and pause worlds**

Since every interaction is physics-driven, pausing isn’t simply a matter of factoring out a clock. A conventional pause menu could have worked, but we didn’t want a separate navigation scheme – [for both immersion and accessibility](https://unity.com/blog/games/accessible-vr-game-design-tips-from-owlchemy-labs).

The main architectural requirement is that each object can access its world and that world’s clock. Every system calls **\_world.Spawn()** instead of [**Instantiate()**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/Object.Instantiate.html), and every system that needs time asks for its clock from the world.

The world lookup uses the [**gameObject.scene**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/GameObject-scene.html) mapping in [**Awake()**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/MonoBehaviour.Awake.html). Each world lives in its own [physics scene](https://docs.unity3d.com/6000.6/Documentation/Manual/physics-multi-scene.html), so we can use the scene handle for the mapping.

A **GameModule** coordinates the worlds; they don’t need to communicate directly. The player uses the main physics scene that comes with loading a [Unity scene](https://docs.unity3d.com/6000.6/Documentation/Manual/CreatingScenes.html). Anything the player grabs or interacts with directly, like the Hyper Visor itself, also simulates in this scene. It isn’t pausable other than when going to the menus or taking the glasses off.

The main gameplay world and pause-menu world are separate. The energy beam goes through the list of active worlds and performs sphere casts and raycasts against each of them.

When the player destroys the pause target in the pause-menu world, the script listening to its destruction tells the module to pause the game. That spawns a set of targets for retrying the level, returning to the overworld, or resuming gameplay. Each world is responsible for spawning what’s inside it and has its own clock and physics simulation.

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/vzGTi1Iq4ngmJ0J_JVaH0FUDwoT54ncFXCyhBF2IIUs/w:1275/h:971/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzI4NDFjMDJkNGVmMmZhNzcyMWQ4NDE1ZmMzOGMyNjllYmQ2MWZhZGEtMTI3NXg5NzEucG5n.avif)

An in-Editor screenshot of the game with the pause menu state active on the right. Script Debugger visualizes stepping through commands at the bottom

## **Controlling simulation and resuming gameplay**

The **GameModule** ticks all the worlds in a specific order alongside other systems. Its [**FixedUpdate()**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) ticks the main game-logic scripting system, then calls [**PhysicsScene.Simulate()**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/PhysicsScene.Simulate.html) for each world using world-specific clocks. We also control exactly when to call [**Physics.SyncTransforms()**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/Physics.SyncTransforms.html).

We only use [**Time.timeScale**](https://docs.unity3d.com/6000.6/Documentation/ScriptReference/Time-timeScale.html) when the device’s focus state changes. When focus returns, we bring players back in a paused state so they can choose when to rejoin the action.

Nothing jolts or pops on unpause because all systems use their world’s clock. The clocks provide the correct time for each simulation, so everything resumes seamlessly.

We implemented pausing late in development, but the systems already supported it. The game already had a concept of game worlds, and we were strict about not relying on global state.

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/QfVJJF0E4l_qwJfZ_nH_jbNe9nbvDlZ1aVO8Am94tMM/w:1920/h:1200/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzQ2NTUzMTY5YzYwMmI5MzJhYTg1M2YzYzg4Njk4Zjc3ZTIwMGJiYWUtMTkyMHgxMjAwLnBuZw.avif)

Hyper Visor | Owlchemy Labs

## **Rendering separate worlds**

Everything uses regular Unity mesh renderers and particle systems, with an abstraction layer for stencil-buffer-based masking. Each world has its own stencil number, and every shader has a stencil property block that lets us render content within these “tears in reality.”

We chose the stencil buffer for performance reasons: We can have many values and many worlds. The overworld, where players select a module, contains unique portals that display only what’s inside their particular world.

[Our physics scenes](https://unity.com/how-to/enhanced-physics-performance-smooth-gameplay) weren’t too complex: around 100 Rigidbodies at a time, without static geometry. [App time](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.0/manual/features/performance-metrics.html) on [XREAL AURA](https://www.xreal.com/aura), as the [Android XR](https://learn.unity.com/deprecated?type=course&slug=android-xr-with-unity) app stats display showed, was stable at around 7 ms. The physics scenes accounted for only a small portion of that.

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/4O36OuHtrA1h7voh040Q5VcA_a2L4V9vS9YiMMmR57I/w:1920/h:1200/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uL2FiZjI2YjQ0M2JkM2VlYjYwMjBmNGRhZTc1OWRlZTU0MjNkZWRjN2MtMTkyMHgxMjAwLnBuZw.avif)

Hyper Visor | Owlchemy Labs

## **Iterating on levels without recompiling**

A recompile and domain reload, followed by pressing Play, could take up to 40 seconds – even on powerful developer machines. In VR, you also have to juggle a headset and watch the environment switch between [Meta Horizon Link](https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@2.3/manual/get-started/link.html) and the [Unity Editor](https://docs.unity3d.com/6000.6/Documentation/Manual/unity-editor.html).

When tuning an arcade level, immediately playtesting changes is crucial. We have a shortcut for that: “R” reloads the current level.

The core gameplay involves spawning targets in different patterns at different intervals. Originally, we used a component with dozens of serialized properties, but it was too limiting and complicated to revisit and understand. A custom level-scripting system made sense. Coroutines weren’t the right fit either, because every little change still required a recompile.

For level authoring, we avoided using scenes: Every level is a [Prefab](https://docs.unity3d.com/6000.6/Documentation/Manual/Prefabs.html) we can modify while the game is running, then reload to see the changes. We can tweak spawn-point positions, tune particle systems and behavior variables at runtime, and copy those values into Prefabs while the game is still running.

The reload preserves the game round you’re in. Most levels, also known as modules, consist of several rounds and a final boss encounter. Here’s a loop from a level script:

`scroll_to 0,0,0`

`points SpawnPoints Top1,Top2,Top3 cycle_after:1`

`points VirusSpawnPoints Bottom1,Bottom2,Bottom3 cycle_after:1`

`shuffle SpawnPoints`

`loop_until objective_met`

`spawn Network point:SpawnPoints count:6 interval:0.4`

`wait 1`

`spawn Virus point:VirusSpawnPoints count:3 interval:0.5 rotate:45`

`wait 1`

`end`

Changing this text file and pressing “R” makes all the difference. We did this hundreds of times per day while working on levels and bosses. All the variables are right there, immediately tweakable.

We also have direct control over cancellation conditions. An early problem was that waits inside loops had to finish before **objective\_met** could cause the loop to exit. That made gameplay feel off: The game should notify players instantly when they reach the win condition.

Our system always evaluates all parent conditions, so gameplay loops exit on the exact frame the condition changes. Achieving this with coroutines would require extra code or a separate system to declare the logic. That’s what we built – except our system parses its logic from a text file at runtime.

C# hot reload wasn’t the right fit for these reasons. In the future, it might be the right fit: Complex boss scripts could benefit from a fully fledged programming language. For now, we enjoy the terseness of our system, with around 3,000 lines of level-script code in total.

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/iflxf0EtbPDbGc3BV8odkz_KwFKI2UnJtKlS-tk2Bt4/w:2560/h:1440/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzg3YjFlOTVhNjkxNGE3OTY2NzI3M2VjN2IyZDQ2Mzc1NDgxYmMzNzktMjU2MHgxNDQwLnBuZw.avif)

Hyper Visor | Owlchemy Labs

## **Making visuals readable on XREAL AURA**

Most gameplay takes place inside a window where we control the background, targets, and effects together. When visuals appear over the player’s space, a glow behind the portals and the Hyper Visor Shades character helps them stand out.

On XREAL AURA, dark and desaturated visuals naturally appear transparent because the additive display emits no light for dark pixels. In glasses testing, the brightest, most saturated elements were the most opaque and crisp, so our focal points use bright values and high saturation. We redid the targets after noticing they could appear more transparent than their backgrounds.

The Hyper Visor Shades character was also appearing transparent. We introduced a bright glow around it, boosted saturation, and lightened its value so its silhouette would stand out. The darker lenses could stay: Transparency reads nicely on something meant to be transparent.

Although dimming the glasses helps, we targeted a brighter space for legibility. Facing a brightly lit window became a useful test: If the light didn’t interfere with reading the visuals, they were successful.

Maximize performance across platforms with the Universal Render Pipeline

[Universal Render Pipeline](https://unity.com/resources/introduction-to-urp-advanced-creators-unity-6)

## **Testing the field of view across glasses**

Most of our developers didn’t have access to XREAL AURA, but they did have a Meta Quest 3. Representing XREAL AURA’s aspect ratio in Quest builds shared within the company was essential. We cropped visuals outside that aspect ratio, giving us a more accurate view of what players could see.

We used a Renderer Feature in the [Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.6/Documentation/Manual/universal-render-pipeline.html) to crop visuals to XREAL AURA’s aspect ratio, and enabled it on builds we shared internally on Meta Quest 3, since that’s the device most of our developers have access to. Rather than calculating from device specifications, we tweaked values comparatively, switching between XREAL AURA and a Meta Quest 3 headset to get the right feel for the field-of-view limits.

That shaped the layout and scale of visuals. The gameplay window stays within view, the Hyper Visor Shades character animates within frame, and the overworld fits in one viewing angle.

We developed on [Unity 6.2](https://unity.com/releases/unity-6) but shipped on Unity 6.5 for XREAL AURA launch-day support. URP provided the [SRP Batcher](https://docs.unity3d.com/6000.6/Documentation/Manual/SRPBatcher.html), while physics scenes and scene handles enabled simple dependency resolution within game worlds.

We maintain a framework on top of Unity’s [OpenXR plug-in](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.18/manual/index.html) that smooths out platform wrinkles and integrates with our build tool. That abstraction matters when shipping on new platforms with specific edge cases and changing packages.

![Hyper Visor | Owlchemy Labs](https://mip.web.unity.com/img/UpuYUU-tfRThWCWIxXEFow72Jf9uEF7aBFsTkeHzWPQ/w:1920/h:1200/q:75/f:avif/aHR0cHM6Ly9jZG4uc2FuaXR5LmlvL2ltYWdlcy9mdXZiampscC9wcm9kdWN0aW9uLzllN2EwOTY1M2RjNTkwNzNiMTA5OGY2MzJlOTRlZDdhYzJlYjE5YzAtMTkyMHgxMjAwLnBuZw.avif)

Hyper Visor | Owlchemy Labs

## **Closing design tips**

Come up with clear design constraints early and keep them consistent. We knew that every interaction should use the stream, players should interact only with things that looked like targets, and gameplay interactions should happen within windows. Those constraints created a consistent world for players encountering a new device.

Lean into the device’s constraints, too. Darker values gave us free transparency. Keeping everything within XREAL AURA’s view created a comfortable experience without requiring players to move their heads toward something just out of view. It’s a new device with new quirks, but it’s fun and freeing to play within them.

**[Hyper Visor](https://play.google.com/store/apps/details?hl=en_US&id=com.owlchemylabs.hyper_visor) *is available on Android XR devices. Check out more stories from Unity developers on the [Unity Blog](https://unity.com/blog) and [Resource Hub](https://unity.com/resources).***
