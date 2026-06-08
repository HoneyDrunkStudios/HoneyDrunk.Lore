---
source: "https://unity.com/blog/cairn-technical-art-rendering-gameplay-rock-materials"
title: "Technical art deep dive: How Cairn renders gameplay-specific rock materials using 3D blendmaps"
author: "Anthony Beyer / The Game Bakers"
date_published: "2026-04-17"
date_clipped: "2026-06-08"
category: "Game Development / Unity"
source_type: "web"
---

# Technical art deep dive: How Cairn renders gameplay-specific rock materials using 3D blendmaps

Source: https://unity.com/blog/cairn-technical-art-rendering-gameplay-rock-materials

Pitons are like checkpoints. They are especially helpful when you start to play the game.

# Technical art deep dive: How Cairn renders gameplay-specific rock materials using 3D blendmaps

*Anthony Beyer from The Game Bakers dives into the technical art of developing “No-Piton Surfaces” for their rock-climbing simulation game, *

[Cairn](https://store.steampowered.com/app/1588550/Cairn/)

*. Learn how they overcame the challenge of aligning visuals with gameplay using 3D blendmaps and Compute Shaders in Unity.*

Hello! I'm Anthony Beyer, technical art director at The Game Bakers. I originally come from a background in graphic design (web, print). My first video game experience was on mobile games as a 3D modeler in 2010. At that point, I didn’t know anything about coding, but I was very interested in working with graphics in a video game engine, so I started to learn JavaScript and tinkered away on a few small Unity projects in my free time. Nowadays, I spend more time writing code than I do making 3D models! You can find some of my works on my [ArtStation page](https://www.artstation.com/sinok426).

I started to work with the studio The Game Bakers at the very beginning of [ Furi](https://www.thegamebakers.com/furi/)’s development, around 2014. After

*Furi*released in 2016, we worked on

[(launched in 2020), and in January 2026 we released our new game,](https://www.thegamebakers.com/haven/)

*Haven**Cairn*, a rock climbing simulation video game.

## What is a piton in *Cairn*?

In *Cairn*, you can climb on almost every wall, and we implemented a stamina mechanic to make this experience more challenging. After climbing for some time, Aava (the player character) will eventually grow tired. To get some rest, she can secure herself to the wall with metal spikes called pitons. (* Gameplay note: Pitons are optional, and you can climb without them, but it takes a deeper knowledge of *Cairn

*’s climbing controls*).

To increase difficulty on some walls and force “free solo” routes, we wanted to disallow piton planting in specific areas of the environment. In this blog post, I will explain how we developed this little technical part of the game we call **No-Piton Surfaces**.

*Cairn* protagonist Aava refusing to plant a piton on a No-Piton Surface.

## How to add different types of surfaces to the environment

When you want to make variations on terrain, what’s the first thing that comes to mind? You can…

- add new objects and geometry
- add “vertex color painting”
- Use a “blendmap texture”

*Cairn* is definitely not your typical “heightmap controlled” terrain; it is actually a kitbashed mountain (more on that in this [ArtStation post](https://www.artstation.com/artwork/AZzrJm)).

This made it hard to do variations via additional objects/geometry because it added more constraints to an already complex level design process (and we wanted to level design our No-Piton Surfaces freely on top of actual climbing level design).

Blendmap and Vertex Color are similar techniques, both being masks that are sampled in the shader to make rendering variations.

In our case, we couldn’t use use vertex color painting, because:

- There were too many vertices to paint.
- There were too many instances of overlapping geometry (handhold meshes projected on kitbashed terrain).
- Our modular rocks use LODs, so the vertices’ density is not consistent.

## 2D blendmap

In the end, we decided to go for a blendmap solution!

Helpfully, we already had a custom tool used for Level Art, the **TexturePainter**. This tool allowed us to paint blendmaps in-Editor and assign them to groups of renderers (manually selected renderers or automatically if they are in TexturePainter bounds).

At The Game Bakers, we love making custom tools in Unity – [ExecuteAlways] is generally the first line I add to every script!

We mostly use TexturePainter to paint grass and snow layers on the ground, but since we can rotate freely in the TexturePainter, we can paint on walls.

After a few small shadery tweaks, we created our “No-Piton Surfaces” blendmap, and could dynamically change our texturing/shading.

Since it’s a baked Texture2D, it’s easy to sample a texture’s value at a given world position to determine if the player can plant a piton or not.

The concept worked! But at this stage it was still quite limited because it is a 2D mask projection, and we could only have one of those for the whole mountain, so precision was low.

At this point, we were not sure if “No-Piton Surfaces” would make it into the game. Visually, they were not appealing, and we would need to do a lot of gameplay/level design tests to be sure they added meaningful value to the game.

But we could at least start to iterate on how it should look.

Exposing some rendering parameters allows us to try out different potential looks for this type of surface.

## When your first solution doesn’t work at all

While we were trying to improve rendering on the art direction side, on the level design side, the “2D projection” limitation was becoming increasingly problematic. Because of the nature of our level design, we needed to have 3D control of the following No-Piton Surfaces:

- No-Piton Surfaces that can be found inside the mountain (in caves)
- No-Piton surfaces that can wrap around concave/convex walls/architecture

…

### Timeskip

*There are always a lot of new ideas and new things to do in game development. I like to work like a butterfly – each time I’m stuck on something, I ignore the problem and go do different stuff elsewhere!*

…

### Three to six months later…

For other new features, we use Texture3D for Distance Field representation. We place many volumes (boxes and ellipsoids) and generate a distance field texture from that, with each pixel containing the distance to the closest volume. Each volume can be additive or subtractive.

This is what we call the “Topology View”: a screen-space image effect controlled by a world-space Texture3D.

These 3D distance field textures are low resolution and generated on-demand at runtime (they’re also not baked in-Editor and not readable CPU-side).

## 3D blendmap

At this point it was time to try our 3D blendmap solution for No-Piton Surfaces.

On the shader-side, it’s straightforward to change from a Texture2D to a Texture3D. Now all that was left to do was add some noise to the world coordinates to hide these low resolution texels, and, *voilà!*

Editing No-Piton Surfaces

This solution worked visually, but everything was broken gameplay-wise, because we were unable to detect the player’s location on the texture because the texture was not CPU-readable.

The distance field sampling was performed CPU-side by iterating over each primitive volume (boxes, ellipsoids). However, because we added noise to the world coordinates in the rock shader, there was a visible offset at the edges; clearly, it lacked precision.

## Syncing visuals with gameplay

To fix this, we used a Compute Shader to get the exact same values seen in the rock shader.

When the player wants to plant a piton, we raycast against the wall to find where the piton is going to be positioned, and check if the player is inside a No-Piton Area. If that is the case, we send the request to the Compute Shader at the piton-planting position. When the Compute Shader result comes back (in the same frame or one frame later), we validate or disable the ability to plant a piton.

Now we have a texel-perfect sample: “rock shader” and “No-Piton Checking Compute Shader”, both sharing the exact same code.

As it turned out, this solution was a little *too *precise!

Imagine you are in the middle of regular rock and No-Piton rock, and you want to plant a piton, but you can’t because the game’s world positioning has determined you’re on a No-Piton Surface. This seems very unfair when you can plant a piton just two inches away.

To fix this, we trigger multiple samples around the player in a small range to find a valid spot if one is available.

Here you can see the green line check is on a No-Piton rock, while the upper blue line check is on a regular rock; we will pick this second position to plant the piton.

## There is always something to polish

With everything looking good, it’s time to refine and polish.

We implemented a way to load multiple No-Piton Areas at the same time. Only the closest area is the “real” one, while the others are rendered as LOD decals. This solution is far from perfect because decals are deferred and can’t receive lighting the same way as the rock shader, but it was sufficient for our needs.

No-Piton 3D blendmap transition from LOD0 (rendered inside rock shader) to LOD1 (rendered with a deferred decal)

That’s all about No-Piton Surfaces. If you’re playing *Cairn* and you find a way to plant a piton on a No-Piton Surface, please tell me – there is always something to fix!

Thanks for reading!

[Cairn](https://store.steampowered.com/app/1588550/Cairn/) *is out now on PC and PlayStation®5, with free “On The Trail” DLC coming this summer. Explore more Made with Unity games on our Steam Curator page, and check out more stories from Unity developers on the Unity Blog and Resource Hub.*
