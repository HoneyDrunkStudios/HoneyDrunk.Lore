---
"source": "https://unity.com/blog/echo-weaver-time-loop-unity"
"title": "Echo Weaver: Building a time-loop metroidbrainia in Unity 6"
"author": "Fergus Baird"
"date_published": "2026-10-08"
"date_clipped": "2026-10-08"
"category": "Game Development / Unity"
"source_type": "rss"
---

# Echo Weaver: Building a time-loop metroidbrainia in Unity 6

Oct 8, 2026|8 Min

![Fergus Baird](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2Fae0a4c2559816caf8f145f367d672b71e8ef8b48-96x96.png&w=96&q=75)

##### Fergus Baird - Unity Technologies

Senior Content Marketing Manager

Made with UnityGame design

Made with UnityGame designRendering

![Key art from Echo Weaver by Moonlight Kids and Akupara Games, made with Unity. A neon-soaked cartoon image of a white-eyed, white-haired figure from the shoulders up. They're flanked by several characters including (clockwise) a cat with a piza, a blue-haired person, a lizard person, a skeletal insect, an old woman with grey hair and goggles, a masked figure, and an alien with an exposed brain.](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F9500200ea8f1649bdfbdf576c5407f8cae6d84b1-1538x866.png&w=3840&q=75)

**[Echo Weaver](https://store.steampowered.com/app/2184080/Echo_Weaver/)*, the anticipated metroidbrainia from Moonlight Kids and Akupara Games, launches today on PC and consoles. We interviewed game designer Chris Sumsky and programmer Ankit Trivedi to talk about knowledge-gated design, loop-reset architecture, and the lessons they’d pass on to other small teams making games with Unity.***

When three-person indie studio [Moonlight Kids](https://www.moonlightkids.co/about-us) started work on *Echo* *Weaver*, they thought they’d found a loophole around one of game development’s most notorious systems: the save state.

“If someone loses their save, you become their number one enemy,” says Chris. The team had struggled with save state errors on their debut, the creature-collector [*The Wild at Heart*](https://store.steampowered.com/app/1093290/The_Wild_at_Heart/), so the timeloop premise for *Echo Weaver* seemed like a dream come true: “We were like, no saving! Time travel! Everything resets!”

Of course, things in game development are rarely this straightforward. *Echo Weaver* streams its interconnected world with no loading screens, which means the game must constantly load and unload [chunks](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/components-chunk-introducing.html) of the map as the player navigates the world. This creates situations like: Did the player break the shortcut wall this loop? Did they talk to that NPC? *Echo Weaver*’s world has to maintain some level of persistence, at least until the player runs out of time and the loop restarts. “So it turned out we just had to save everything anyway,” Chris says. “But it’s less detrimental when something goes wrong, because the player can always reset the loop.”

![Echo Weaver](https://unity.com/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FFTJEppg4Kwg%2Fhqdefault.jpg&w=3840&q=75)

## A space parkour detective game

In *Echo Weaver*, there are no ability gates. The world is entirely open from the first minute of gameplay, but it’s up to the player to figure out how to fully explore it. “Our internal pitch was ‘space parkour detective’,” says Ankit.

“Imagine you had to make a game where nothing persisted,” says Chris. “Every sense of progression the player needs to feel is already there, it’s just buried under layers of secrets. This is the big, weird thing we’re doing with *Echo Weaver*. It’s both the coolest thing to me and the biggest challenge, because someone can stumble into any ability at any time.”

During the early phases of development, the team positioned the project as a deliberate reaction to *The Wild at Heart*. “At the time, it hadn’t sold well – fortunately this changed later on – and so we were trying to do everything in opposition to that project. We thought we would make something a little darker, a little harder,” says Chris. “Of course, this meant we were going against what we were good at – and we quickly saw the error of our ways!”

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F3b341b189d0d54d20afdce3c58ab406ade44c697-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

Many of *Echo Weaver*’s carryovers from *The Wild at Heart* are foundational to Moonlight Kids’ identity as a studio, from cofounder and creative director Justin Baldwin’s hand-drawn style (“down to the same brushes and palettes”) to big, interconnected spaces stuffed with secrets, and a commitment to nuanced storytelling in genres where that’s not often the focus.

On the technical side, the team’s internal tools library also made the leap from *The Wild at Heart*, including the dialog system, FMOD interface layer, controller and dynamic input-icon code, and screen shake.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F6f44fbcc06c5427499ba324ec935612e29f7e5f1-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

## Core design principles: The Weaver remembers

With no ability gates and a world that resets with every loop, Moonlight Kids needed to establish rules for what persists between runs. They landed on a narrative solution that wouldn’t break immersion: The player character, the Weaver, retains their memories across loops. “Anything they would remember in their own brain, we’re allowed to bring into the loop. If the Weaver sees it, the player should see it,” explains Chris. “That doesn’t break the metroidbrainia rule.”

This decision informs the entire game, from the progress screen that tracks the knowledge the player has unlocked, to the level presentation. When a hidden area is uncovered, the foreground artwork fades away. During playtesting, this wasn’t persistent across loops, but the team found that players kept forgetting which shortcuts they’d discovered, so they made a concession and permanently faded the foreground in areas players would revisit most frequently.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2Fdbe859580768399546e6114c7302fbe8820c7504-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Unity

## Level design without permanent shortcuts

Choosing to gate progress using player knowledge over specific upgrades removes an important tool from the standard level designer’s kit. Metroidvanias typically lean on one-way walls and permanent shortcuts – break a wall and that path is open for the rest of the playthrough. “In a timeloop game like *Echo Weaver*, when you break a wall and reset the loop, that wall’s just back again,” says Chris. “That wasn’t necessarily in my toolbelt.”

The team’s solution for this problem works at two scales. Within a single loop – which can run for several minutes based on how much time the player has collected – Chris was able to pull off traditional metroidvania design tricks, because anything contained within one loop can pay off in that same loop. The team designed each of the game’s level branches and areas with this constraint in mind.

For bigger and more complex shortcuts – ”Think the Firelink Shrine in *Dark Souls*,” says Ankit – the only real option is concealment. A passageway can be tucked behind foreground art at one end and positioned in the foreground at the other, creating a secret hidden in plain sight. “Games like *Tunic* do this really well with perspective,” he adds.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F26b0f9a69af11674fe09ec4dcf1ad8937f4b1fbc-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

## Managing the player’s time

*Echo Weaver*’s clock is its most prominent system, and is visible to the player at all times. Every loop begins with 1 minute of time on the clock. Players can look for time crystals to extend it, or they can sacrifice crystals to heal; finding the right balance here is crucial to success.

In early versions of the game, the timer would tick down second by second, but playtesters hated it. “It created a lot of stress,” says Chris. “One day we were like, what if we just take the clock away? You don’t really *need* seconds – all you need to know are the minutes.”

The final HUD is a row of time chunks, each representing one minute – in-game these are called “bells” because NPCs saying things like, “Come back at minute 8” broke the fantasy. Nearly everything in the world is carefully timed around these minute-long beats. Playtesters responded positively to this new system, and were soon inventing “boot-up sequences” – heavily optimized opening routes that bank huge amounts of time within the first few seconds of a loop.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F0b9a70495f03f785dd7f38c62e6d84cb05a57eb8-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

## How the time loop works

So what happens when a time loop resets in *Echo Weaver*? Ankit’s architecture divides the gameworld into chunks, each tagged with a chunk script, with a custom build process that strips out expensive content ahead of time.

The heavy, unchanging layer – all of the world geometry and transition markers – is baked into scenes and stays loaded permanently. A lightweight “essentials” scene holds the volatile state: the game manager, the player, and the run-specific data. On a reset, the game unloads the active chunks, discards the essentials scene entirely and reloads it, streaming back in only the chunks needed for the loop’s opening sequence.

“That’s one big way we mitigate what persists and what shouldn’t – we just trash it and redo it,” Ankit says. “It’s such a light scene anyway that trashing and redoing it isn’t a huge concern.”

Run-specific state lives in an in-memory dictionary of string keys; wiping that dictionary is part of the reset. Anything that must survive across loops – the loop count, abilities they’ve seen, characters they’ve spoken to – is serialized to disk. Every object checks its own key when its chunk streams in, often just reading a bool or an int.

The approach hasn’t been completely bug-free. Ankit found that persistent transitional doors weren’t fully resetting their UI state between loops, so he simply stopped persisting them. Now, each door’s interactive component is a clone that gets reinstantiated on every reset. “For maybe 20 objects, it doesn’t matter – it doesn’t have an impact on performance,” he explains.

Carryable items like keys posed a subtler problem: an item that lives in one chunk can be walked anywhere in the gameworld, and chunk-level ownership meant these objects were either vanishing from players’ inventories or being duplicated. To fix this, the team moved items to the persistent scene layer.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2Ffbbdcb73f19ed80fcbfa096463a831138a31ce13-1871x856.png%3Fw%3D1604%26h%3D734%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver’s layered environment assets in-Editor

## Optimizing a detailed, hand-drawn world

Like *The Wild at Heart*, *Echo Weaver* is dense with bespoke, [hand-drawn art](https://unity.com/resources/2d-game-art-animation-lighting-unity-6-3-lts) – which, while visually stunning, can be expensive to load and render. The team implemented several fixes to maximize performance.

### Asset compression

The solution to their first big performance hurdle was anticlimactic. “None of our Atlases had compression on,” laughs Ankit. Enabling [compression](https://docs.unity3d.com/2022.3/Documentation/Manual/SpriteAtlasWorkflow.html) brought everything in memory down to about 1 GB.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F4591a58b46826311106c72c793bca94d061c02a0-1576x915.png%3Fw%3D1576%26h%3D915%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

A look at the Weaver’s animations in the Unity Editor

### Scene loading

Loading the game presented a harder problem. Instantiation lands on the main thread synchronously, so decorative assets are stripped from chunks at build time (with [ManualOverrides](https://docs.unity.com/en-us/engine/6000.7/script-reference/unityengine/adaptiveperformance/performancelevelchangeeventargs/manualoverride) for size, rotation, and sprite settings preserved) and reinstantiated asynchronously, batched by a few objects per frame. Combined with a neighbor system that always keeps adjacent chunks loaded, pop-in remains out of sight.

### Batching

Because Justin’s hand-drawn artwork avoids repeating patterns, batching opportunities were rare, so Ankit wrote a tool that flattens groups of sprites into a single image (and a single draw call). For example, the sky in one of *Echo Weaver*’s biomes is built from dozens of near-identical platforms; using the tool, they collapsed it into two composite sprites along with a handful of unique accents.

### Lighting

*Echo Weaver*’s initial lighting setup was expensive. Sprites originally carried up to four different light types each (background, player, item, and floor variants), and at one point, 16 distinct lighting textures were being rendered at once. Consolidating six light layers into three cuts that down dramatically, “and I don’t think the visuals have suffered for it,” says Ankit.

### Water effects

Water came from the Unity Asset Store: [Game2D Water Kit](https://assetstore.unity.com/packages/2d/textures-materials/water/game-2d-water-kit-118057?srsltid=AU7gw4V1aKKiZHVVeUTbEPLM-3B10PxCMFEYAKyjFqLoGiYxAlAYfPUL), running on the [Universal Render Pipeline](https://unity.com/features/graphics). “Very flexible, produces really good results,” Ankit says – but each water body re-renders the camera, and cost scales with the number of layer groups refracting beneath the surface. The team consolidated underwater layers, and publisher Akupara Games' in-house porting team went further for low-end hardware, splitting the plugin’s fake surface-entry perspective effect from its refraction setting so weaker devices keep the look without the redraw.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F8380fb6133c350c2b8a00fde964602ab6cb1c747-3840x2160.png%3Frect%3D0%2C1%2C3840%2C2159%26w%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

### Debugging

Unity's [Frame Debugger](https://unity.com/how-to/best-practices-for-profiling-game-performance#set-a-frame-budget) played a central role in much of this optimization work, allowing Ankit to step through the frame draw call by draw call and see exactly where batching was breaking – and why. From there, the job was consolidating: unifying materials, converting stray sprites, and rechecking until as much of the frame batched as possible. “You could still see that batching breaks here and there,” he says, “But it's a lot less than it was." Ankit’s advice to other teams is simple: “start using the Frame Debugger liberally, right away!”

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F61d1b81c900d3f3d767d4de166044e559db9b818-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

## From 2021 LTS to Unity 6

*The Wild at Heart* shipped on Unity 2021; *Echo Weaver* ships on [Unity 6](https://unity.com/campaign/unity-6-for-games), locked to one version shortly before release. Asked what’s changed [day to day](https://learn.unity.com/course/unity-6-day-to-day-productivity) between versions, Chris didn’t hesitate: “[Nested Prefabs](https://docs.unity3d.com/2023.2/Documentation/Manual/NestedPrefabs.html) and edit mode – those were life changers.”

Ankit says the team has used [Composite Collider 2D](https://docs.unity3d.com/560/Documentation/Manual/class-CompositeCollider2D.html) liberally, and Unity’s native object pool, which meant he could finally stop maintaining the custom object pool he’d written for *The Wild at Heart*. “It’s nice to use built-in stuff wherever applicable,” he notes.

![](https://unity.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffuvbjjlp%2Fproduction%2F13851ded8e0ed9dc7fc0d6df3a80f4e72a773ee7-1920x1080.png%3Fw%3D1604%26h%3D902%26fit%3Dcrop%26dpr%3D2&w=3840&q=75)

Echo Weaver | Moonlight Kids | Akupara Games

## Parting advice for small teams

Closing out the interview, we asked Chris and Ankit what tips they’d share with other developers looking to make games with Unity.

“I’ll probably get roasted for this,” prefaces Ankit, “But conventional wisdom says don’t optimize early on. I don’t think that’s necessarily true. You can architect in a way that’s performant early on, and that can actually save you a lot of time later.”

The team implemented *Echo Weaver*’s chunk-streaming system early in the project. Particles have been pooled from day one. Ankit always tries to be careful with C#’s convenience, because garbage collection pressure can build up quickly. “If you’re trying to ship a game, it *has* to be performant in the end. Why write yourself into a corner where that seems impossible? Making things performant *later* means giant breaking changes.”

Chris offered some advice about design and the importance of leaning on your studio’s creative identity. “Making a knowledge-gated game like this is hyper-dependent on the big picture,” he says. “We spent years iterating on pieces we could only finish once the whole project came together. A lot of this could have been scripted out early, film-style, while still leaving a lot of room for iteration.”

But the one thing he would do differently is to trust his gut and stick to making what’s familiar and feels right. “In hindsight, it was wrong of us to say, well, no one wanted *The Wild at Heart*, so we’ll do something totally different. What do the people want? No – play to your strengths, truly. We wasted a lot of time figuring out how to play to the market. Eventually we were just like, what are we doing? Do what you’re good at. Make the game you want to make.”

**[Echo Weaver](https://store.steampowered.com/app/2184080/Echo_Weaver/) *launches today on Steam, PlayStation®5, Nintendo Switch™ 2, Nintendo Switch, and Xbox Series X|S. Explore more Made with Unity games on our [Steam Curator page](https://store.steampowered.com/curator/45049063-Made-With-Unity-Official/), and check out more stories from Unity developers on the [Unity Blog](https://unity.com/blog) and [Resource Hub](https://unity.com/resources).***

***Nintendo Switch is a registered trademark of Nintendo.***
