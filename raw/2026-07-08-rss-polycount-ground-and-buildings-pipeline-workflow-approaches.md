---
source: "https://polycount.com/discussion/238759/ground-and-buildings-pipeline-workflow-approaches"
title: "Ground and buildings pipeline/workflow/approaches"
author: "Polycount"
date_published: "2026-06-25"
date_clipped: "2026-07-08"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Ground and buildings pipeline/workflow/approaches

Source: https://polycount.com/discussion/238759/ground-and-buildings-pipeline-workflow-approaches

Ground and buildings pipeline/workflow/approaches — polycount 
You are using an outdated browser. Please upgrade your browser to improve your experience.
Toggle navigation 
Polycount 
News 
Forums 
Patreon 
Challenges 
The BRAWL² Tournament Challenge! 
Bi-Monthly Environment Art Challenge 
Wiki 
Moar 
Recent 
Activity 
Badges 
Drafts 
Store 
Help 
Sign In · Register 
Author: Kevin Johnstone 
Home › Technical Talk 
Ground and buildings pipeline/workflow/approaches 
maaboo 
Online / 
Send Message 
maaboo 
Jun 25 2026 
I was surprised not to find a separate section dedicated to game development, so I'm asking here. While I learned a lot about making game assets recently, there are two topics that absolute mystery to me.
The first one is how to make a ground for a game. Imagine having a road, a sidewalk, a gravel/dirt whatever. E.g. here is from Escape from Duckov:
Or The Ascent:
Or Mutant Year Zero:
Should I use tile approach and create fixed size tiles for every surface as well as transitioning types, create a large non-square areas filled with tileable texture, or something else?
And the second question about architecture. I want to make buildings with navigable interior for the game. I can do the following:
Either create a unique mesh completely in Blender and paint it in the Substance and then make an asset in Unity Or create smaller blocks (like bricks or wall tiles) and build a prefab inside the Unity Or there is another approach? (As usual, a combination of the both) Like again in MYZ:
This example less relevant to my case since I'm planning to have intact buildings (the world is just abandoned), thus this approach might be less efficient. In the other hand, I could use these bricks as debris as well as building blocks. And not paint another building which has the same material.
Any ideas?
0 · Share on Facebook Share on Twitter 
Replies 
Offline / 
Send Message 
poopipe 
grand marshal polycounter 
Jun 25 2026 
The whole forum is about game development, we don't need a section 
The problem with these sort of questions is that the answer depends on what you're making and what your engine and toolchain can cope with. 
and
on top of that - the answer will often be "all of the above" 
Your best bet on the terrain / road stuff is to explain what you're trying to achieve (ideally with some concept art or reference photos) and which engine you want to do it. People will have many ideas and you'll learn terms to search for. 
Your suggested approach could be the best solution in some situations while also being the worst possible solution in others - we need more context.
as far as the building goes.. 
One way to think about this is to consider your range of view distances. 
2m - 200m - you're probably best off using modular pieces cos you get more flexibility and you don't need to worry about what happens at a distance
2m - 5000m - you're probably best off making buildings as one model so you can lod them properly and get less entities overall. 
0 · Share on Facebook Share on Twitter 
Online / 
Send Message 
maaboo 
Jun 25 2026 
Thanks. Well, as for references, I already provided them. It's something similar to any of the ref with more/less same view angle and distance, i.e. it will be top-down action with kind of isometric view (actually perspective but it's very subtle) and the engine is Unity (I mentioned it, but you're right, I should clearly indicate it in the very beginning). LODs are not needed in my case.
I'd prefer the approach that saves me a lot of time (since I'm making it alone) yet providing a good optimisation on resource loading since I don't see that polycount/VRAM is an issue. 
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
poopipe 
grand marshal polycounter 
Jul 6 2026 
In terms of reference... Is it a city with a grid pattern? An older town with winding little streets? What sort of junctions do you need to support, do you need road markings? What are the pavements/roads made of etc.. 
Eg. If you need paving to follow the shape of your street it's a different problem to not needing that. 
0 · Share on Facebook Share on Twitter 
Online / 
Send Message 
maaboo 
Jul 6 2026 
poopipe said: 
In terms of reference... Is it a city with a grid pattern? An older town with winding little streets? What sort of junctions do you need to support, do you need road markings? What are the pavements/roads made of etc.. 
Eg. If you need paving to follow the shape of your street it's a different problem to not needing that. 
There is no any kind of grid definitely. And it's not even a city, more like city areas, e.g. downtown, cargo terminal, shopping mall, factory, etc. that are separated from each other. The closest ref here is Mutant Year Zero (unlike my game it HAS the grid, so imagine it doesn't), where you have points on your map and you choose the area and the you can enter it either from global map or adjacent area but via loading screen.
I need all the stuff: usual crossroads with pavements and crosswalks, T-junctions with gravel road, parking lots, and even ramps and elevated roadways, and also a railways with railway crossings. And, of course, with road markings, cracks and potholes. Just like in real life.
Or imagine a poor man's (i mean VERY poor) Cyberpunk 2077 (also a ref to some extent) with top-down fixed camera. :-)
My first thought was to create a modular roads but it solves only half of the problems, my primary concern is a smooth transition between different surfaces and surface details like mud, puddles and fallen leaves. The idea is to generate procedurally as much as possible to get the unique look for every player/new game (and may be for every raid). I.e. how do I connect modular road to the surrounding grass so it could look natural? Or how do I make areas that don't obviously rectangle shaped (see Escape from Duckov)? 
0 · Share on Facebook Share on Twitter 
Online / 
Send Message 
Thanez 
interpolator 
11:56AM 
You're probably looking for texture blending. 
You can vertex paint, use heightmaps, normals, or even have a dedicated world mask texture that you paint in engine.
I've seen a version of the latter, where they baked onto such a mask texture using the geometry of the world as input.
I can't find the video, but they basically in engine baked AO from trees onto ground and used that as a mask to blend in a "fallen leaves" texture.
These are just ideas. Googling the software you use and the problem you're trying to solve always grants quick insight.
If blender: 
https://www.youtube.com/shorts/noInRltAsXo 
https://www.youtube.com/shorts/M-NJLtwAINg 
World aligned textures (Show texture if normal is pointing in Direction_a = TRUE):
https://www.youtube.com/watch?v=MfJ_1LWe2Q4 
Any method you choose can be filtered or altered by any other methods, and the one you end up with will generally be unique to solve a single type of problem, like: 
Where should grass grow?
Do a big thinkywink about where you'd logically want grass to end up: (not in the ocean, not on walls, not indoors, not on mountain sides so steep that there's no soil, not on top of mount everest, not on the moon)
Separate them and importance weigh them, and roughly plan out how you might wanna achieve that.
I'm trying to be vague here because there's almost an infinite amount of unique ways to decide where do grass ends up.
The best answer is: Go look. Youtube is a great resource for learning. 
https://www.youtube.com/watch?v=GSJFuoerkaw 
Not entirely related, but not entirely unrelated, when texturing, we use all kinds of texture types as input data to decide where different textures go.
Way before there was anything like Substance Painter, I was doing that kinda noise in Photoshop, semi-manually.
My first attempt looked like this:
My (bad) scrapes were supposed to end up where convexity was max. Where concavity was max, I wanted rust or dirt. 
If you pay attention to where my scrapes ended up, you'll be able to find a couple where I mixed up convexity with concavity 
0 · Share on Facebook Share on Twitter 
Sign In or Register to comment. 
© 2026 Polycount. All image rights belong to their authors.
Terms of Service | Privacy Policy
