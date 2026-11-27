---
source: "https://80.lv/articles/breakdown-designing-large-scale-soviet-era-architectural-system-for-vr-game/"
title: "Breakdown: Designing Large-Scale Soviet-Era Architectural System for VR Game"
author: "Stanislav Petrushin"
date_published: "2026-11-27"
date_clipped: "2026-11-27"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Breakdown: Designing Large-Scale Soviet-Era Architectural System for VR Game

[Stanislav Petrushin](https://80.lv/author/stpetrushin-d6fad097)

Senior/Lead Environment artist

27 November 2026

# Breakdown: Designing Large-Scale Soviet-Era Architectural System for VR Game

[#Environment Art](https://80.lv/articles/environment-art)[#Feature](https://80.lv/articles/feature)[#Blender](https://80.lv/articles/blender)[#Unreal Engine](https://80.lv/articles/unreal-engine)[#Marvelous Designer](https://80.lv/articles/marvelous-designer)[#Megascans](https://80.lv/articles/megascans)[#Substance 3D Designer](https://80.lv/articles/substance-designer)[#Substance 3D Painter](https://80.lv/articles/substance-painter)

Stanislav Petrushin explained how he created authentic-looking Soviet-era brick residential buildings with explorable interiors, covering modular systems, atmosphere, lighting, composition, and practical optimization techniques.

### Introduction

Hi everyone! I'm Stanislav Petrushin, a Senior Environment Artist with nearly eight years of experience in game development. I've worked on a wide range of projects, from Enlisted and Active Matter to AAA titles like Call of Duty and VR games such as Into the Radius 2. I specialize in realistic environments, with a particular focus on architecture, modular systems, and large-scale game environments.

I've already shared more about my background, career path, and experience in my [previous article](https://80.lv/articles/how-to-create-a-nostalgic-and-abandoned-environment-for-vr-survival-shooter) for 80 Level. If you'd like to learn more about me and my work, feel free to check it out.

This time, I'd like to focus on one of the most challenging parts of my work on Into the Radius 2: designing a large-scale architectural system for an entire Soviet-era residential district. I'll explain how multiple interconnected modular systems were designed to work together, how they supported evolving gameplay requirements, and how I optimized the environment for VR.

For this showcase, I built a separate scene in Unreal Engine 5 using the original game-ready assets, Lumen lighting, native-resolution textures, and Nanite for the landscape only. I wanted to show the full visual potential of these assets beyond the rendering limitations of VR. Alongside the production breakdown, I'll also share how I approached the showcase's atmosphere, lighting, and composition.

### Architectural Research, Blockout & VR Testing

The task was to create authentic-looking Soviet-era brick residential buildings with explorable interiors. The challenge was that the exact number of buildings and accessible rooms was still unknown. Game designers needed the flexibility to choose which apartments and rooms players could enter, and to change those decisions as the project evolved.

I started by studying architectural drawings and floor plans of real buildings and adapting them to the project's needs. I created initial grayboxes and tested them directly in VR. Proportions that seemed perfectly reasonable on a monitor could feel very different when I was actually standing inside the space with a headset, so I adjusted the dimensions accordingly.

In the end, I settled on seven building configurations: two different lengths of two-entrance buildings with five, three, or two floors, plus a smaller two-story building with a single entrance. I also planned two roof types: gable and hip, to provide additional variety.

Once the dimensions and configurations were approved, I prepared blockouts for additional architectural elements, including balconies, foundations, entrances, staircases, railings, and other details. I established their pivots and naming conventions, then passed them to other artists for detailing while I continued working on the buildings and interior system.

This initial planning was essential. By thinking through the architecture and its modular structure early on, I could avoid costly redesigns later in production.

### Designing the Modular Kit

With the overall building blockouts in place, I started dividing the main walls, foundations, and roofs into reusable modules. The goal was to turn those large gray boxes into a relatively compact kit of pieces that could be assembled into all seven building configurations without having to model each building separately. I ended up with several modular sets: two variations of ground-floor modules, upper-floor modules with and without balconies, interior wall modules, roof modules, and a separate set for the smaller single-entrance building. Each set was designed to work with the dimensions and architectural requirements of its respective building type.

For the exterior wall modules of the main buildings, I divided the architecture into left and right sections to avoid mirrored textures. I also considered adding a central extension module that would allow buildings of virtually any length. However, such long structures weren't needed, so I decided against adding unnecessary complexity. A system doesn't need to do everything. It needs to solve the project's actual problems efficiently.

However, the exterior architecture was only one part of the challenge. The buildings also needed a flexible interior system, configurable windows and doors, and a way for different specialists to work on the same structures independently. This is where the project became much more interesting than a conventional modular building kit.

### Interconnected Modular Systems

I organized the buildings into four interconnected logical layers, each serving a specific purpose. Each layer could contain multiple Level Instances, all nested within the main building Level Instance.

**The first layer – Essential Building Elements**

This included the main building structure, foundations, roofs, balconies, and other architectural details. The layer also included basic interior wall modules, which established the layout of rooms and corridors on each floor. These elements were present in every building, regardless of whether it was accessible to players.

**The second layer – Interior Spaces**

The interiors were separated from the main building structure. Fully detailed rooms could be added, removed, or replaced with different variations as gameplay requirements evolved. This allowed the team to configure individual apartments and rooms according to their intended purpose and condition.

**The third layer – Configurable Elements**

Windows, doors, and light sources were organized into separate levels so that each building could be configured individually. For example, if a window were part of a reusable room Level Instance, opening it in that source room would affect every instance of the same room. Keeping windows independent made it possible to create different configurations for individual buildings.

**The fourth layer – Gameplay & Supporting Elements**

Gameplay actors, spawners, audio components, and other supporting elements were organized into dedicated levels. This allowed environment artists, level artists, game designers, and sound designers to work on the same buildings in parallel.

When deciding how to separate these elements, I followed a simple principle: does this component always need to be present, and does it need to be replaceable? For example, every building needs a roof, but since there were two roof variations, I kept them separate. On the other hand, stairs and railings were essential parts of a stairwell and had no alternative versions, so there was no reason to separate them. The stairwell module itself, however, could be omitted if the building wasn't accessible to players, so it remained independent.

The result was a flexible system that worked for both the team and the level design. Different specialists could work on the same buildings in parallel, while game designers could quickly configure each building to suit its specific gameplay needs.

### Interior Architecture & Room Variations

Depending on the building type, each floor could potentially contain 36 or 40 individual spaces, including rooms, kitchens, corridors, and bathrooms. However, to cover all this variety, I only needed 16 unique room modules.

I treated each detailed room as a separate Level Instance, with different versions available depending on the needs of the building. The system supported up to five stages of decay, from relatively intact rooms to heavily abandoned interiors. I designed the modular room system and created the geometry and materials, while our Level Artist handled the furnishing and set dressing.

### How to Show a Room That Doesn't Actually Exist

While this system made it possible to configure accessible interiors, many apartments would remain without detailed room modules. This raised an important question: what would players see when looking through their windows from outside?

Players could freely move their heads, approach windows, and look inside from different angles. Even when an apartment was inaccessible and had no detailed room modules, the building still needed to look believable without the cost of a fully detailed interior.

There was also the issue of glass. A fully destructible glass system wasn't feasible within our project's constraints, so simply covering the windows with intact opaque or frosted glass wasn't an option. Fake parallax interiors weren't feasible either, while simple dark boxes would have looked unconvincing.

Since intact glass panes weren't an option, I decided to keep at least small fragments of broken glass in the window frames. However, this still left the interiors visible.

This is where the basic interior wall modules came in. They formed the internal layout of each floor, regardless of whether detailed rooms were present. Simple rectangular floor slabs were scaled to fill the spaces without detailed interiors.

Both the basic walls and floor slabs used extremely simple geometry, low-resolution Base Color textures without Normal or Roughness maps, and very low-resolution lightmaps. The floor materials also used world-aligned mapping, allowing the slabs to be resized easily.

Now, instead of looking into a hollow building, players could see recognizable rooms behind the windows. However, from outside, these spaces still looked like empty boxes. To solve this, some windows were partially covered with curtains, boarded up, or blocked with furniture. There was no need to seal them completely. Even if a small gap remained, the visible walls and depth of the room created the impression of a real interior.

### How Interior Modules & Collision Work Together

But the basic interior walls served another important purpose: they also provided collision for fully detailed rooms.

The detailed room modules were essentially visual boxes with single-sided geometry facing inward. Since the basic interior walls were already behind them, there was no need for additional wall collision. The detailed rooms only required their own floor collision.

Ceiling collision was provided either by the floor of the room above or by the same basic floor-slab modules used to fill empty spaces. I positioned the detailed room surfaces with a minimal offset from the basic interior walls to prevent Z-fighting, while keeping the shared collision close enough for bullet impacts and decals to appear correctly on the visible surfaces.

As a result, the two systems complemented each other. The basic interior walls formed believable empty apartments and provided collision, while the detailed room modules created fully furnished, explorable interiors. Together, they allowed the buildings to feel complete while solving several technical problems without introducing unnecessary collision complexity or visual artifacts.

### Materials & Architectural Details

For the building exteriors and large interior surfaces, I primarily used tiling textures combined through layered materials. Most of the materials started with Normal Maps from Megascans, which I then refined by adding additional surface details and creating my own Base Color and Roughness maps. Many textures also supported tinting, allowing me to create numerous color variations from a single texture set.

For more complex surfaces, I created additional layers using the original textures as a base. Depending on the requirements, these could be simple masks, modified textures, or entirely new texture sets featuring different levels of damage, dirt, or wear. Everything was combined using Unreal Engine's Material Layers system. Given the project's performance requirements, I generally limited materials to no more than four full layers.

**A Small Tip for Brick Architecture: Making Convincing Corners**

One detail I paid particular attention to was the brickwork around building corners. Players can get very close to these areas or peek around them, so flat, poorly aligned brick textures become especially noticeable.

Real brick walls have a characteristic interlocking pattern, with alternating courses wrapping around the corner. Reproducing this with tiling textures can be tricky. Each floor was assembled from left and right building modules, and their brick textures had to align seamlessly where the modules met. In my case, the brickwork also needed to remain consistent across all four corners of each floor.

I wanted to create convincing brick depth without attaching individual bricks that would interrupt the masonry pattern or make the corners protrude unnaturally from an otherwise flat facade. My solution was to create a separate wraparound geometry strip for each corner, extending roughly 40 cm along both adjoining walls. I slightly recessed the outer edges of this strip into the main wall and adjusted the surrounding geometry to create enough room for subtle brick relief without making the corner look bulky.

Next, I divided the strip horizontally along the mortar joints, creating a separate row of geometry for each brick course. I then cut the UVs along these rows and adjusted their alignment to reproduce the staggered brick pattern wrapping around the corner.

However, this introduced another issue: the brick courses on the corner strip didn't always align perfectly with the tiling texture on the main facade. Some bricks appeared to end abruptly where the strip met the wall.

To fix this, I slightly stretched the individual rows, adjusting their ends until the brickwork connected naturally with the surrounding facade. This introduced some minor UV distortion, but it wasn't noticeable with the final textures, while the masonry pattern remained continuous. I also added more detailed brick geometry to the lower sections of the corners, where players could approach them closely. Higher up, I used a simplified version to avoid unnecessary geometry. The result was a continuous brick pattern with convincing depth, without obvious seams, floating brick pieces, or unnaturally protruding corners.

### Practical Optimization Techniques

#### Scene Structure & Actor Count

Early in production, flexibility is essential. But as the level design and architecture become finalized, some of that flexibility is no longer necessary. This was particularly relevant to our modular buildings. Initially, they consisted of many individual pieces that could be freely assembled and replaced. However, once the building configurations were approved, I merged the exterior modules into larger building shells. This reduced the number of individual actors and also helped avoid any visible shadow seams between modular pieces.

The window system was another good example. Initially, I wanted as much flexibility as possible, with separate frames, movable sashes, and interchangeable meshes featuring different patterns of broken glass. I could adjust how far each sash was opened and create different combinations directly in the level. But a single window could contain 11-18 actors. On just one facade of a five-story building, with approximately 50 windows, that meant around 550-900 actors for windows alone.

The thing is, most of them didn't actually need that much flexibility. Closed windows worked perfectly well even when there were fully detailed interiors behind them. So I created three closed variations for each window type, with different broken-glass patterns, all as single Static Meshes. That was enough to avoid noticeable repetition and brought the number of window actors on the same facade down to under 80. More elaborate open-window assemblies remained only in selected key locations, and I applied a similar approach to balcony windows. It was a good example of how simplifying an overly flexible system could save resources without sacrificing much visual variety.

Another small thing worth checking is Blueprint ticking. Environment Artists often use Blueprint Actors to assemble groups of static meshes into reusable compositions. In most cases, such compositions don't require per-frame updates, so there's no reason to leave ticking enabled. In the Blueprint, check Start with Tick Enabled and disable it if unnecessary. It's also worth checking the Tick settings of individual components.

#### Draw Calls, Material Slots & Custom Primitive Data

Another important area is the number of material slots used by individual meshes. For example, imagine a concrete slab with a few metal brackets or lifting loops. A straightforward approach would be to assign separate materials to the concrete and metal parts. However, it's possible to achieve the same result with a single material, using Vertex Colors painted directly onto the mesh.

This slightly increases shader complexity but reduces the number of material sections and associated draw calls. In my experience, this approach often provides better results, especially for small and medium-sized assets repeated throughout the environment.

A similar principle applies to material variations. Let's say you have dozens of identical doors or windows, but you want them to have different colors. Creating a separate Material Instance for every variation is convenient, but it can prevent otherwise identical meshes from being combined into a single instanced draw call.

For this reason, I made extensive use of Custom Primitive Data. Instead of creating multiple Material Instances, I could use the same material and pass individual parameters through CPD. This allowed me to change the color of windows, doors, and many other assets directly on their instances while preserving a shared material setup.

I also incorporated procedural dirt controls into this system. Using the same Material Instance, I could create clean objects, change their colors, or apply different types and color variations of dirt.

One important production detail is keeping the CPD parameter structure consistent across different Master Materials. If certain indices are reserved for tinting, those same indices should serve the same purpose everywhere. Otherwise, managing a large material library quickly becomes confusing and error-prone.

#### Shader Complexity & Material LODs

Material complexity was another major area of optimization. For Into the Radius 2, I used two main approaches: conventional Master Materials for relatively simple props and Layered Materials for architectural surfaces that required more complex blending and weathering.

Layered Materials offered much greater flexibility, but their additional functionality also came with a performance cost. Even a relatively simple layered setup could be slightly more expensive than a conventional material providing the same basic features. This difference might seem insignificant for a single object, but in a large environment with hundreds or thousands of assets, small costs can accumulate.

One particularly interesting example came from our modular interiors. Each room could have several stages of decay, so I initially used universal Layered Materials for its surfaces. For example, the wall material combined wallpaper, damaged plaster, dirt, anomaly ash, and other surface variations, allowing it to cover every stage of wall decay.

However, a relatively well-preserved room might only need the Background Layer with its wallpaper pattern, while a heavily damaged room might primarily use one of the other layers. Despite this, the shader still contained the additional blending operations, even when those layers weren't visibly used. Some of these materials had around 500-600 shader instructions, although the room effectively displayed just one surface type.

I created simplified material versions for rooms that didn't require multiple layers. This made a significant difference. For example, the shader instruction count for one wall material dropped from 608 to 298. A floor material went from 528 to 254, while a ceiling material went from 476 to 254. The full Layered Materials remained in the intermediate stages of decay, where a combination of relatively intact and damaged surfaces actually needed that flexibility.

Of course, using separate materials can increase the number of Material Instances and potentially reduce batching opportunities. However, in this particular case, the reduction in shader complexity was substantial enough to justify the trade-off. A universal material isn't always the most efficient choice, especially when most of its functionality isn't being used.

Another useful technique is overriding materials on distant LODs. If an asset uses an expensive material with multiple texture layers and detailed effects, those features may no longer be visible at a distance. In such cases, I can assign a simplified material to the lower-detail LODs, reducing shader complexity as the object moves farther from the camera. This requires some care when managing material sections and transitions between LODs, but it can be an effective way to preserve close-up quality without paying the same rendering cost at every distance.

#### Shadow Casting

Shadows are another area where small decisions can have a noticeable impact, especially in VR. It's worth reviewing which objects actually need to cast dynamic shadows. Small decorative elements, flat meshes, dirt floaters, and other minor details may contribute almost nothing to the final image through their shadows, while still adding rendering cost.

For most assets, I prefer making these decisions for individual placed actors in the final gameplay level rather than disabling shadows globally. For example, a book lying flat on the floor might not need to cast a dynamic shadow, while the same book on a shelf or standing upright could produce a much more noticeable one. Clearly, flat decorative meshes, such as dirt floaters, are an exception: they generally don't need to cast shadows at all.

There are also less obvious cases. Imagine a single baseboard mesh running around the entire perimeter of a room. Although its bounding box covers a large area, the mesh itself is just a thin strip along the walls. Disabling its dynamic shadows can reduce rendering cost with little to no noticeable visual impact.

For genuinely flat decorative meshes, such as posters or flat debris, even baked shadow casting may be unnecessary. Disabling it can also shorten lighting builds. However, I would be conservative here: an incorrectly disabled static shadow can be difficult to spot until a lengthy lighting bake has finished.

#### Texture Memory & Lightmaps

Texture resolution is another important part of balancing visual quality and performance. I generally prefer creating textures at a sufficiently high resolution first, then adjusting their final resolution inside the game engine based on the target platform and the importance of the surface.

In our project, I often found that reducing the resolution of Normal Maps and packed ORM textures was a good starting point for saving memory. Base Color required more careful adjustments, since even relatively small reductions in its resolution tended to produce more noticeable blurring of surface details.

Although many modern projects rely on dynamic lighting solutions, baked lighting remains a primary approach for many performance-sensitive VR environments. This makes lightmap resolution another important consideration.

Not every asset needs the same Lightmap Density. Large exterior building shells can often use relatively low-resolution lightmaps, while detailed interiors, important gameplay spaces, and areas with complex lighting may benefit from higher density. The goal is to distribute the available lightmap budget where players will actually notice the difference, rather than trying to make every surface appear green in the Lightmap Density visualization.

### Profiling & Optimization Results

Optimization is important, but evaluating its effectiveness by eye alone isn't enough. I wanted to measure the results of my work and make sure that the changes were actually improving performance.

The optimization process involved several areas. I replaced expensive Layered Materials with simpler versions where multiple layers weren't necessary, disabled dynamic shadows on selected objects, reduced texture resolutions, and optimized geometry.

For testing, I used a separate scene containing a palette of all the room variations from our modular interior system. This allowed me to evaluate the rendering cost of a large collection of assets and materials without the additional complexity of a complete gameplay level.

I compared the original and optimized versions using a fixed camera position and forced LOD 0 for all meshes. I wanted to compare the assets at their highest level of geometric detail, without automatic LOD switching affecting the results. The goal was to evaluate the changes made to the environment itself, rather than the performance benefits of the LOD system.

Optimization was an iterative process that ran alongside regular production, so the two versions of the test scene weren't completely identical. The optimized version included additional surface variations, and some room furnishings had been moved or replaced. Importantly, the number of placed assets did not decrease. In some rooms, additional details and dirt meshes were even added.

The goal wasn't to measure how much performance each individual optimization technique contributed. I wanted to evaluate the combined results of these changes as part of regular environment production. Despite the differences between the two versions, the comparison still showed a clear reduction in rendering costs, without reducing the amount of content in the scene.

The measurements were taken directly in the Unreal Editor rather than in packaged builds. My goal was to evaluate the relative differences between these two states of the environment, not to benchmark the absolute performance of the final game.

#### Profiling Tools

For these comparisons, I used ProfileGPU, stat scenerendering, stat RHI, and stat unit. I checked them one at a time rather than displaying all the profiling overlays together, since the overlays themselves can introduce additional overhead.

It's important to use several tools rather than relying on a single statistic. For example, reducing the number of draw calls doesn't necessarily mean the GPU will render the scene faster. Similarly, simplifying shaders might significantly reduce BasePass cost without noticeably affecting texture memory usage.

I didn't use Unreal Insights for this particular task, as ProfileGPU and the stat commands provided all the information I needed for this A/B comparison.

#### Results

The following table compares the measurements before and after optimization

The profiling results showed substantial reductions in the measured costs of BasePass, ShadowDepths, and PrePass. Texture memory usage also decreased significantly, reflecting the changes to texture resolutions and material resources.

The number of mesh draw calls increased slightly. This was partly due to additional art adjustments and material changes made during production. Nevertheless, both Frame Time and Draw Thread time improved, demonstrating why draw call count alone isn't a sufficient measure of performance.

GPU Scene is not the same as total frame time, so the reduction in that measurement shouldn't be interpreted as an equivalent increase in FPS. Overall, the comparison showed meaningful reductions in rendering costs and helped me determine that the optimization work was moving the project in the right direction.

Profiling is essential when investigating specific performance bottlenecks, but optimization shouldn't start only when performance becomes a problem. I believe Environment Artists should keep material complexity, texture resolutions, geometry, and shadow casting under control throughout production, rather than waiting until the end to deal with unnecessary performance costs.

#### Creating the Portfolio Showcase

While the architectural systems were designed for Into the Radius 2, I wanted to present them in a setting that would better reflect my own artistic vision. The primary goal was to demonstrate the scale and complexity of the modular systems, but I also wanted to explore the full visual potential of the assets.

Unlike a gameplay level, this scene didn't need to accommodate player navigation, encounters, or other gameplay requirements. This gave me more freedom to focus on composition, atmosphere, and the overall impression of the environment.

One important thing I'd like to emphasize is that these are the original game-ready assets used in Into the Radius 2, not high-poly versions recreated specifically for the portfolio. The geometry, level of detail, and material systems remain the same as in production, where everything was designed around the demanding performance requirements of VR.

For the showcase, I restored the textures to their original resolutions and replaced baked lighting with Lumen. One of the main reasons for using Lumen was iteration speed. Baking lighting can significantly increase the time required for each adjustment, which was unnecessary for a presentation scene. I also used Nanite for the landscape, but not for the buildings or other assets.

I spent roughly a month assembling and refining the showcase scene, including level art, lighting, atmosphere, and final presentation. I wasn't working against a strict deadline, so I could experiment with different approaches until I was satisfied with the result.

#### Art Direction & Lighting

I deliberately chose a cold, overcast atmosphere. I knew that repetitive Soviet architecture under a grey sky would be less immediately eye-catching than a warm, sunlit scene during the golden hour. However, I wanted to create a contrast with my previous Abandoned Dacha project and, more importantly, convey the feeling of a world that had been abandoned.

I wanted the environment to feel unwelcoming, oppressive, and slightly unsettling. In my opinion, this kind of atmosphere also helps emphasize the massive, repetitive architecture of Soviet residential buildings.

Creating convincing overcast lighting turned out to be a real challenge. There were no dramatic sunlight beams, strong directional shadows, or bright highlights to help define the composition. Instead, I had to rely on subtle tonal differences, atmospheric perspective, and carefully balanced ambient lighting.

If the contrast was too strong, the shadows lost important details. If I brightened everything too much, the scene became flat and uninteresting. Finding the right balance between atmospheric haze and visual clarity required quite a few iterations. I spent a lot of time adjusting lighting, fog, reflections, and shadow values to give the scene enough depth without losing its subdued mood.

#### Composition & Final Presentation

Choosing the final camera angles was another challenge. The buildings were both tall and extremely long, making it difficult to fit their entire structure into a single composition while keeping the architectural details readable.

I experimented with different angles and camera distances, trying to find a balance between showing the overall scale and allowing viewers to appreciate the individual architectural elements. Rather than forcing everything into a single shot, I used several complementary views to present the environment from different perspectives.

In the end, I think the combination of restrained lighting and different camera angles worked well for this scene. It allowed me to show the architecture clearly while preserving the cold, oppressive atmosphere I was aiming for.

### Final Thoughts

Looking back, the most challenging part of this project wasn't creating the buildings themselves, but designing a system that could adapt to requirements that weren't fully defined at the beginning. What started as a relatively straightforward architectural task eventually grew into several interconnected systems supporting different building layouts, interior variations, and gameplay configurations across an entire residential district.

This project is a good example of what I enjoy most about Environment Art: combining artistic decisions with technical problem-solving. Creating believable environments is important, but making them flexible, efficient, and practical for an actual game is just as much a part of the job.

Finally, I'd like to thank my colleagues for their contributions to the assets and materials used throughout this environment. Their work was an important part of bringing this project together.

### [Stanislav Petrushin](https://www.artstation.com/frozishe), Senior Environment Artist
