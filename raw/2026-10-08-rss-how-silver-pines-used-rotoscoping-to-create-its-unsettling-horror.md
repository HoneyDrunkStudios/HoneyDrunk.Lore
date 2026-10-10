---
"source": "https://80.lv/articles/how-silver-pines-used-rotoscoping-to-create-its-unsettling-horror"
"title": "How Silver Pines Used Rotoscoping to Create Its Unsettling Horror"
"author": "Linus Larsson"
"date_published": "2026-10-08"
"date_clipped": "2026-10-08"
"category": "Game Development / Unity"
"source_type": "rss"
---

[Linus Larsson](https://80.lv/author/linus-larsson)

Game Designer

Interviewed by

[David Jagneaux](https://80.lv/author/david-jagneaux)

08 October 2026

# How Silver Pines Used Rotoscoping to Create Its Unsettling Horror

[#Interviews](https://80.lv/articles/interview)[#Animation](https://80.lv/articles/animation)[#Video Games](https://80.lv/articles/video-game)[#Game Development](https://80.lv/articles/game-development)

Wych Elm breaks down Silver Pines’ handmade art pipeline, including 1,800 character frames, rotoscoped monsters, photo-based textures, billboard environments, and a two-person level team.

In case you missed it

More Silver Pines

* [Wych Elm Co-Founder on Creating the Survival Horror Metroidvania Silver Pines](https://80.lv/articles/wych-elm-co-founder-on-creating-the-survival-horror-metroidvania-silver-pines)

[**Silver Pines**](https://store.steampowered.com/app/2333000/Silver_Pines/) brings survival horror into an unusual 2.5D format, combining limited resources, fragile weapons, interconnected exploration, and environmental puzzles with the atmosphere of a decaying American town. Private investigator Red Walker enters the isolated community while searching for a missing musician, only to become entangled in a surreal mystery conveyed through telephone calls, local broadcasts, television programs, NPC encounters, and environmental details.

That distinctive presentation was achieved through a deliberately modest but remarkably labor-intensive pipeline. Wych Elm constructed its environments primarily inside Unity using simple 3D geometry, photographic textures, and layers of billboard props. The levels were produced by only one designer and one artist, making speed and flexibility essential, but the team still ensured that even early blockouts communicated the intended composition, lighting, and atmosphere.

Its character animation demanded considerably more manual work. Red Walker alone required more than 1,800 individually drawn frames. In this new interview, **Wych Elm co-founder Linus Larsson** discusses that handmade production process, the game’s mood-driven lighting, its interconnected world design, and the challenge of balancing horror, mystery, action, and metroidvania progression without losing its identity.

You can also read our **[previous Silver Pines interview](https://80.lv/articles/wych-elm-co-founder-on-creating-the-survival-horror-metroidvania-silver-pines)**, which explores the project’s influences, story, gameplay, and original creative direction.



**Silver Pines combines survival horror, metroidvania structure, and small-town mystery. What was the original creative vision for the game, and how did those different genre pieces come together?**

**Linus Larsson, Wych Elm Co-Founder :** We started this project well over four years ago, and we have done a huge amount of concept development. We knew right from the start what kind of feeling we wanted to evoke, and had ideas about this remote area cut off from the rest of the world by a vast wilderness. We had a lot of X-Files and conspiracy-themed ideas starting out, in combination with psychological elements. As we refined the concept and the story, the conspiracy elements gave way in favor of the surreal. There’s probably three games worth of stuff that we didn’t include, just because we wanted the pieces to fit neatly together. 

**The game is set in a half-abandoned American town with a strong sense of decay and mystery. How did the team define the visual identity of Silver Pines, and what kinds of references shaped its locations, architecture, lighting, and atmosphere?**

**Linus Larsson:** We used a lot of real-world references for the town, but always having a “fantasy first” approach. Obviously we have to take liberties with the layout of the town in favor of gameplay, but never to the point where you’re pulled out of the fantasy. Some of the references came from online searches, and also from places around where we live. Lighting in the game tends to favor mood over realism, but never to the point of pushing the viewer into rejecting the scene as unnatural. We wanted to dramatise the town through light, to reflect Walker’s story as he descends deeper into the mystery.



**From an art direction standpoint, how do you balance the grounded feeling of a recognizable small town with the more surreal, nightmarish elements players encounter as the mystery deepens?**

**Linus Larsson:** With so much of the town being in a believable space, we have a lot of headroom to go louder and make those scenes be felt. A lot of heavy lifting is done through lighting and changes in color, and since these sections are used sparingly we’ve never felt any risk that the player will feel fatigue or that the surreal elements begin to lose their punch. 

**Silver Pines uses a 2.5D side-scrolling perspective rather than a traditional fixed-camera or first-person survival horror format. What made that perspective the right fit, and how did it shape level design, combat, exploration, and environmental storytelling?**

**Linus Larsson:** The project was imagined as a platformer right from the start, even from the earliest concept sketches. We felt the perspective let us put the world and the town in the front seat, and it enabled us to leverage our strengths as game developers to be able to quickly make this town come to life. We have to put a lot of work into making the scenes feel like they were part of a coherent world, where you always can see landmarks in the next area over.



**Can you walk us through the art production pipeline for a typical environment or enemy, from concept and reference gathering to modeling, texturing, animation, lighting, VFX, and final implementation?**

**Linus Larsson:** When we developed our environments, we put a lot of focus on finding reference images and photos mostly. We’re trying to build a world that really feels like a real town, so the typical starting point is to find a suitable reference of a real life place, then we try it out with a level design mockup just to prove that a place like that can deliver the right gameplay.

We want to make sure that we don’t pick a reference that looks cool, but is not fun to play, or that we for example build a level design that can’t be visually dressed to look like a small town building or area.

In the cases where we’ve built something rather surreal, or if a scene is more about the art and composition as opposed to a designed puzzle or combat area, then we’ve done a bit more traditional concept art or other audio visual exploration first.

Since the atmosphere and the world is such an important part of the game, we always made sure that mockup levels showed clear intention in mood, lighting and atmosphere before any real play testing could happen. This is usually a very quick pass getting the broad strokes in place. It should look like the done thing if you squint your eyes a lot.

**Linus Larsson:** On the more technical side of things, all our levels and props are built inside [Unity with ProBuilder](https://80.lv/articles/probuilder-advanced-level-design-in-unity).

The levels in Silver Pines are typically a very simple 3D room or terrain with a ton of billboard props added onto it. Our art style doesn’t require very detailed 3D objects, so we don’t really need a more advanced modelling software than that. Staying inside Unity also just simplifies the production so much and adds a ton of flexibility for level design and art to quickly collaborate. Fast, simple, and flexible have been our priorities, being such a small team of one designer and one artist making levels.

The textures are almost always using some kind of photo that is painted over, or filtered to look a bit more stylized. We think of the style a bit like an old anime in a way, where the characters are cell shaded, but the backgrounds are painted with a higher fidelity and have more detail.

For the animations, we’ve used rotoscoping to a large extent, where we use filmed material and draw the character on top. This approach lends a lot of realism and weight to the characters, while being somewhat restrictive in what designs can be captured this way. There’s quite a bit of dress-up involved as we recorded reference material for monsters and things like that, and tricks like doing the motions backward and reversing the frames to give the animation a subtle uncanny feeling. Other things were animated using bone rigs in combination with a manual edit pass on top to get it to match the style. In a few cases it’s freehand frame animation. The player character alone has over 1,800 hand drawn frames, so it was quite labor intensive to work this way.



**The game mixes survival horror resource management with metroidvania-style exploration and progression. How do you design interconnected spaces that feel tense and dangerous while still encouraging players to backtrack, investigate, and uncover new paths?**

**Linus Larsson:** The player is always driven by a few different motivations, and we try to make sure that these goals stay relevant. There’s the second-to-second goal of just staying alive, getting across some terrain, etc. This typically costs resources either in ammunition, health, or durability of the gear. This in turn becomes the mid-term goal, to resupply and find better tools. We tease some of these upgrades in places, as well as teach the player that they can count on finding something valuable if they go the extra mile of searching every nook and cranny. On top of that we have the larger narrative goals, character encounters, obstacles, and places of interest marked on the map. These play out over longer time scales, and with a relatively open structure of the overall game they feed into a player driver experience, where these obstacles don’t need to be tackled in a particular sequence (if at all). 

**Enemy design is crucial in a horror game, especially when combat and resources are limited. How did you approach creature silhouettes, animation, audio cues, attack tells, and difficulty so encounters remain frightening but readable?**

**Linus Larsson:** We approached this again from a fantasy-first perspective, designing creatures that felt like they would fit this particular kind of setting and story. After that we create a crude first-draft and start playing with different attack strategies. A creature design works the best for us when it keeps a few tricks up its sleeves, an unexpected move or a change in appearance that takes the player off guard. Getting those moments right, in combination with a robust system for attacking and movement, was where we spent most of the effort.



**What software, engine, and tools did the team use to build Silver Pines, and were there any custom tools or workflows created specifically for its 2.5D presentation or interconnected world design?**

**Linus Larsson:** We generally don’t use anything fancy in our workflow. The game is built in Unity, we use [Powersprite Animator](https://powerhoof.itch.io/powerspriteanimator) to handle all the sprite animation, Probuilder for geometry, 2d collision generation, Playmaker for a lot of logic scripting. [Animator’s Toolbar Pro](https://www.animatorstoolbar.com/main/) has been invaluable for working with animation in [Photoshop](https://80.lv/partners/adobe-photoshop). Beyond various little utilities for bits and bobs, we mainly rely on a lot of manual work. Lots of clicking, drawing individual sprites, building individual scenes and hand placing objects. 

**Silver Pines features dynamic narration. How does narration fit into the player experience, and how did it affect the writing, pacing, and implementation of the story?**

**Linus Larsson:** We use a few different ways to convey story throughout the game. One is through the telephone, where Walker will receive calls from his employer, there are NPC encounters, in-world tv shows, lore handouts, a local radio broadcast and the occasional cutscene. Some of these are dynamic in how they trigger, others are placed by us, and they all have their own arcs and conclusions where they provide clues to the central mystery. The story runs in parallel throughout the game, and we have approached this by trusting the player to engage at their own pace with the narrative, never spoon feeding the story.



**For 80 Level’s audience of artists and developers, what has been the hardest part of making a game that needs to function as horror, mystery, action-adventure, and metroidvania all at once without losing its own identity?**

**Linus Larsson:** Finding the balance between gameplay-driven design and the narrative wrapper was hard for us before we ironed out the various storytelling devices we wanted to use. The somewhat outlandish conventions in survival horror for puzzle design and surreal moments don’t always lend themselves to be highlighted explicitly in the story, and once we understood how to balance those things, it became a lot easier, and it allowed us to focus on the things that mattered.



### [Linus Larsson](https://www.linkedin.com/in/linushombre/), Co-Founder of Wych Elm Games

#### Interview conducted by [David Jagneaux](https://www.linkedin.com/in/davidjagneaux/ "https://www.linkedin.com/in/davidjagneaux/")
