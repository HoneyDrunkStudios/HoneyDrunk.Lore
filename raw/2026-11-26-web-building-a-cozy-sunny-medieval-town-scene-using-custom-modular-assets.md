---
source: "https://80.lv/articles/building-a-cozy-sunny-medieval-town-scene-using-custom-modular-assets"
title: "Building a Cozy, Sunny Medieval Town Scene Using Custom Modular Assets"
author: "Wang Yifan"
date_published: "2026-11-25"
date_clipped: "2026-11-26"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Building a Cozy, Sunny Medieval Town Scene Using Custom Modular Assets

### Introduction

My name is Wang Yifan. I'm currently a senior (fourth-year) student majoring in Digital Media Art at Xihua University in Sichuan Province, China, focusing on 3D game environment art – in other words, game environment production.

I've always enjoyed playing games. While playing the Battlefield series, Red Dead Redemption, and Genshin Impact, I became curious about how the scenes in games are actually made – how buildings, roads, vegetation, materials, and the overall atmosphere come together. That gradually led me to pursue game environment art as my direction.

At the moment, I mainly work with 3ds Max, ZBrush, Substance 3D Painter, Substance 3D Designer, SpeedTree, and Unreal Engine 5. For my training, I attended [Modeng's](https://www.artstation.com/zhanglu) (魔灯) full-pipeline environment art program, where, with the help of Modeng and other instructors, I studied the complete game environment art pipeline in a fairly systematic way, while also practicing with my own projects.

Currently, I mainly create Unreal Engine 5 game scenes and related 3D environment assets, and I hope to enter the game industry in the future, working in 3D game environment art or game level art.

### Catis Town

The main goal of this project was to go through the complete UE5 game scene production pipeline  
once, rather than just making a few individual models.

I chose a medieval town as the theme because it contains a wide variety of asset types – stone walls, timber structures, roof tiles, cobblestone paths, props, vegetation, and so on – which makes it possible to practice many different stages of scene production in a fairly comprehensive way.

For references, I worked in several directions. First, for composition and visual presentation, I mainly recreated a scene by the 3D environment artist [Shannon Welsh](https://www.artstation.com/shannon3dart), studying her composition, building arrangements, and overall presentation.

The Witcher 3: Wild Hunt and Kingdom Come: Deliverance served more as subject and style references. The visual characteristics of medieval architecture, the street environments, and the overall sense of daily life and atmosphere were based on those, but I didn't turn them into exact copies of any specific in-game locations.

I also gathered real-world references of Western European medieval towns and historical architecture, mainly to understand building structures, how stone and timber were used, and how different buildings relate to one another.

The whole reference process wasn't about following one fixed image; instead, I organized references by stage and asset type. Early on, I focused on building layouts, streets, and composition; during production, I searched for references for specific assets such as stone walls, wooden beams, tiles, and cobblestone paths; and when working on materials, I supplemented with real photos of stone, wood, and metal.

### Composition

I consider it one of the more important parts of this project. After locking down the composition, I started working on the blockout (whitebox) to establish the road directions, the approximate placement of buildings, the focal point, and the spatial proportions, and only then began producing the actual assets. This helps avoid the situation where you finish all the models only to find that the overall composition doesn't work and everything needs major rework.

The buildings were mainly built with modular assets. For highly repetitive assets such as walls and wooden beams, I modeled the low-poly versions directly in 3ds Max, created trim sheets and tileable materials in Substance 3D Designer, and then combined them in Unreal Engine 5. Each building was assembled from a large number of modular assets with the help of Blueprints.

For assets with low repetition rates or high visual importance – such as the wooden cart in the lower-left corner and the bell in the center of the scene – I used a full high-to-low-poly workflow: creating the mid-poly model in 3ds Max, sculpting the high-poly model in ZBrush, baking the high-poly details onto the low-poly, texturing in Substance 3D Painter, and finally importing everything into Unreal Engine 5.

Roof tiles are a high-repetition asset, so I didn't model every single tile as an individual mesh. Instead, I mainly created the tile material in Substance 3D Designer and used Displacement in Unreal Engine 5 to create the relief. Only the tiles along the eave edges, where the silhouette needs to read clearly, were actual models.

The cobblestone paths followed a similar approach – I mainly used SD materials with Displacement instead of stacking large numbers of solid rocks. To avoid visual repetition, I made three variations: regular intact slabs, slabs with moss growing in the gaps, and slabs with puddles.

All the vegetation was created in SpeedTree. Grass and small plants were scattered in batches, while larger trees were placed manually according to the compositional relationship between the buildings and the roads.

So throughout the project, I wasn't pursuing maximum fidelity on everything – the production method for each asset was decided based on its repetition rate, its visual importance, and the performance cost.

### Retopology & Unwrapping

Model optimization was done manually in 3ds Max. I don't simply chase the lowest possible polycount – I decide what to keep based on the final visual result. For example, for object silhouettes, prominent curved surfaces, and details visible to the camera, I try to preserve the structure and contours; flat areas, occluded regions, or faces that don't affect the visuals get simplified.

For UVs, I used RizomUV. How I unwrap depends on the asset type and how its materials will be made. Important assets that need dedicated materials get a sensible allocation of UV space, while building modules with high reuse rates rely more on trim sheets or tileable materials, which greatly reduces the workload of UVs and textures that need to be produced.

For baking, I used Marmoset Toolbag. The basic pipeline went like this: low-poly model and topology optimization in 3ds Max, UV unwrapping in RizomUV, high-to-low baking in Marmoset Toolbag, and then texturing in Substance 3D Painter.

Overall, I care about the balance between UV utilization and the final image quality – I wouldn't let the project's texture count and production cost spiral endlessly just for the sake of maximum fidelity.

### Texturing

This project leans toward realism overall. What I wanted to express is natural wear accumulated through long-term use. I didn't want to make everything dirty just to add detail. My material work combines Substance 3D Painter and Substance 3D Designer. Substance 3D Designer is better suited for procedural base materials and reusable material logic, while Substance 3D Painter is mainly responsible for material adjustments and hand-painting on specific assets – things like localized wear, stains, and unique details.

For stone, for example, I consider the color and roughness variation between different blocks and add natural weathering such as rain and wind exposure, dust, and moss. For wood, I focus on grain direction, roughness variation, edge wear, and traces left by long-term use.

One thing I pay attention to is why the wear would appear here. For instance, the base of a building is more likely to come into contact with mud and dust; protruding areas are more prone to bumps; and the gaps between stones tend to collect dust or grow moss. Wear built this way feels more consistent with the real environment.

The wooden cart was one asset I worked on particularly carefully because it combines three different materials: wood, fabric, and metal. The wood mainly shows grain, roughness, and edge wear; the fabric gets some fiber texture, folds, and stain variation; and the metal shows oxidation, rust, and wear from use.

Finally, through overall dust and ambient color variation, these different materials are unified into the scene's environment.

So overall, my approach is a combination of hand-painted and procedural materials.

### Assembling the Scene

Once in Unreal Engine 5, the buildings were still based on modular assets, assembled through Blueprints. This makes it convenient to adjust the size, structure, and arrangement of the buildings, and it also improves asset reuse.

Regular objects in the scene – buildings, barrels, crates, and so on – were placed manually, because this allows for better control over the composition and the visual focus. Some small, irregular objects, such as fruit in the baskets and fallen leaves and twigs on the ground, were handled with gravity simulation so that they would stack up naturally, followed by manual adjustment. This looks more lifelike than placing each one with absolute precision, and it also saves some time.

For obvious repetition in the scene, I introduced variation through rotation, scaling, and different material states. For the walls, for example, I made two states: a fully intact wall and a damaged version with exposed bricks. To control the variation in local areas, I then used vertex painting in Unreal Engine 5, combined with decals to add stains and damage details, reducing the sense of regularity that comes from reusing modular assets.

Overall, I first made sure the core composition and building relationships were right, then I gradually added medium and small details, rather than spending a lot of time on small props right from the beginning.

### Lighting

I went for a sunny afternoon scene, as it's something that allows me to make the scene feel warm overall, while keeping a genuine sense of everyday life. When establishing the mood early on, I also used AI tools such as ChatGPT and Gemini to generate fairly broad mood reference images, mainly to help judge the sunlight direction, color temperature, and overall feeling. But these were only my early references – the actual lighting still had to be readjusted in Unreal Engine 5 based on my own scene's buildings, materials, and camera.

There, I mainly used Directional Light, Sky Light, Post Process Volume, Volumetric Fog, and Lumen. The fog wasn't made particularly dense – it is mainly there to add spatial depth and atmospheric perspective, giving the sunlight a sense of space within the scene. The final renders were produced with Unreal Engine 5's Movie Render Queue.

For post-processing, I first created a LUT in Photoshop and imported it into Unreal Engine 5, then adjusted the overall color temperature, exposure, and the hue of the shadows based on the actual result in the scene. The goal was a warm look without going overly yellow, while avoiding crushing the shadows into dead black.

What I wanted to present in the end is a medieval town that feels sunlit and lived in – natural and believable.

### Conclusion

The whole project took about five months in total. Since this was my first time building a complete Unreal Engine 5 scene, the greatest difficulty actually wasn't not knowing how to use a particular piece of software – it was that when I was studying, most of the topics were relatively isolated, and only after starting a complete project did I realize that modeling, UVs, materials, vegetation, scene assembly, performance, and lighting are all interconnected.

The biggest takeaway from this project is that, for the first time, I gained a fairly complete understanding of the full game environment art pipeline – from early references, composition, and blockout to asset production, UVs, materials, and vegetation, and then to scene assembly, lighting, and final rendering in Unreal Engine 5.

If I could give one piece of advice to people just starting to learn environment art: don't stay too long at the stage of practicing individual software operations. Once you've got the basics, start a small but fully rounded project as early as possible, because many problems only appear when you're actually working on a full-scale project.

Also, don't make the scope of your first project too large. Rather than attempting a huge scene that ends up unfinished, it's better to build something of a manageable scale that still demonstrates the complete pipeline. After finishing one full project, you can then gradually push up asset quality, scene scale, and production efficiency.

### Wang Yifan, 3D Environment Artist

#### Interview conducted by [Emma Collins](https://www.linkedin.com/in/emma-collins-663070320/ "https://www.linkedin.com/in/emma-collins-663070320/")
