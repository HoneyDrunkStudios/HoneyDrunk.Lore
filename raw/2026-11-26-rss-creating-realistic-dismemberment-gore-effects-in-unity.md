---
source: "https://80.lv/articles/creating-realistic-dismemberment-gore-effects-in-unity"
title: "Creating Realistic Dismemberment & Gore Effects In Unity"
author: "Sylopon Games"
date_published: "2026-11-26"
date_clipped: "2026-11-26"
category: "Game Development / Unity"
source_type: "rss"
---

# Creating Realistic Dismemberment & Gore Effects In Unity

### Introduction

Hello, I'm Kim, the director of indie game studio SYLOPON. Our upcoming game, [THE IRONY](https://store.steampowered.com/app/3164230/THE_IRONY/), is a side-view sci-fi horror action game being developed in Unity. Heavily inspired by Dead Space, our goal is to reinterpret strategic combat centered around dismemberment from a side-view perspective.

However, achieving realistic dismemberment and gore effects came with several technical challenges. In this interview, our team members Han and Min will explain how they overcame those challenges!

When a character's body part is severed during combat, blood sprays from the exposed wound. The bloodstains left on floors and walls vary depending on the character's posture and the surrounding environment. To preserve this level of detail, we designed the system so that bloodstains remain on level surfaces permanently throughout the playthrough rather than disappearing over time.

Of course, optimization was another important consideration. To reduce runtime costs, we pre-generate the severed meshes and spatial search data for surfaces that can receive bloodstains in the Unity Editor. When a dismemberment event occurs during gameplay, the system switches to the pre-prepared meshes. Meanwhile, the movement of the spraying blood and its collision points with level surfaces are calculated at runtime.

### Skinned Mesh Dismemberment & Pose Transitions

We also considered runtime dismemberment similar to that seen in Metal Gear Rising: Revengeance. While distributing the calculations across multiple frames can reduce the per-frame computational load, the exact moment when the dismemberment is completed may vary depending on hardware performance and system load.

However, in THE IRONY's execution sequences, body parts must be severed at precisely timed moments. For this reason, we chose to pre-bake the dismemberment meshes rather than perform the cutting at runtime.

The cutting planes and masks for each body part are defined using the Dismemberment Editor, a custom Unity tool developed by our programmer, Han. Within this tool, we inspect the cross-sections on both the main body and the severed part, adjust their UVs, and then bake the meshes.

Although this process requires additional production time and asset memory for each body part, it allows us to inspect and verify the shape and textures of the exposed surfaces in advance.

On the frame when a dismemberment event occurs, the corresponding body part is retrieved from the object pool and copies the original character's bone pose at the exact moment of severance. Physics simulation then begins from that pose.

This approach eliminates the need to recalculate the mesh when transitioning from animation to physics.

### Blood Spray Curves & GPU Surface Generation

When significant arterial bleeding occurs in real life, blood does not flow at a constant rate. Instead, it spurts in pulses corresponding to pressure changes caused by the heartbeat. However, during the early stages of development, our blood effects appeared as a single continuous stream, making it difficult to visually convey this pulsation in a side-view environment.

To improve this, Min, our modeler and Technical Artist who has a particular obsession with detail, implemented a system that multiplies a pressure curve that decreases over time by a heartbeat curve. This allows both the volume and velocity of the blood spray to fluctuate with each heartbeat.

However, to represent these fluctuations naturally, we also needed to make individual particles appear as a single continuous stream of blood. To achieve this, Han developed a renderer that uses compute shaders to record particle density in a 3D grid, then applies the Marching Cubes algorithm to generate a triangle mesh representing a surface at a given density threshold. This allows particles close to one another to merge visually into a single, organic stream.

However, this approach had its limitations. As the blood stream becomes thinner due to changes in heartbeat and pressure, its diameter can fall below the grid spacing, potentially causing gaps in the generated surface.

To solve this, we implemented an alternative approach for thinner streams that generates a tube-shaped surface along the direction of blood flow. This allows us to maintain a continuous, natural-looking blood stream that responds to heartbeat and pressure changes, without the additional computational cost of increasing the resolution of the entire grid.

### Bloodstain Shape, Color & Spread

In addition to the blood spray itself, we wanted the bloodstains left on the surrounding environment to look as natural as possible. To achieve this, Min carefully adjusted the shape, color, and spreading speed of the bloodstains, taking the side-view camera perspective into account.

First, bloodstains formed as blood grazes along walls are created by repeatedly stamping brushes onto the surface. To prevent identical patterns from appearing, we introduce variations in position, size, and opacity with each brush stamp. Additionally, because the shape of bloodstains on ceilings can be difficult to distinguish from a side-view perspective, we stretch the brushes along the depth axis to make the stains appear sufficiently wide.

We also considered how blood color changes depending on its volume and thickness, rather than focusing solely on the shape of the stains. The color of a bloodstain depends on the underlying surface color and the accumulated blood density. In areas where only a thin layer of blood is present, the original surface color remains partially visible. As more droplets overlap and the blood density increases, the stain gradually becomes a darker shade of red. We also added reflective highlights around the edges of pooled blood to visually convey its thickness.

These details extend to the way blood forms pools on the floor. Immediately after hitting the ground, blood spreads rapidly, but the spreading speed gradually decreases as it approaches its target radius. Additional blood falling nearby accumulates in the existing pool, naturally increasing the area it covers.

### Bloodstain Mask Recording & Spatial Queries

What we wanted to capture was not just the moment blood splashes, but also the traces it leaves behind. Each droplet should create a stain with a different size and outline, and repeated impacts in the same area should gradually darken the stain.

To achieve this, we developed a system that stamps brushes at blood impact points and accumulates their density in a separate bloodstain mask based on lightmap UVs. By adjusting the size and shape of each brush, we can create a variety of bloodstain patterns. Since the affected area is calculated in world space, stains can also extend naturally across adjoining surfaces, such as where a wall meets the floor.

To reduce the computational cost of this process, we organize the bounding boxes of static surfaces into a Bounding Volume Hierarchy (BVH) during the editor stage. At runtime, the system only traverses the branches that overlap with the brush's area of influence, while multiple stains applied to the same surface are grouped together for recording. This allows us to efficiently accumulate new bloodstains while preserving those already present.

### Conclusion

Brutality and gore are essential elements of horror action games. Although THE IRONY is a side-view game, we wanted its violence to feel just as visceral and shocking as what players might experience in a first-person game.

However, achieving realistic gore effects in a game meant overcoming a number of technical challenges. The development process was almost as gruesome as the blood effects themselves, but thanks to the passion and dedication of our two talented team members, we managed to bring our vision to life!

I'd like to take this opportunity to express my sincere gratitude to both of them for their hard work. And I hope this breakdown will be helpful to other horror action game developers facing similar challenges!
