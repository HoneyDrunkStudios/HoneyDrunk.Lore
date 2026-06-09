---
source: "https://80.lv/articles/recreating-nostalgic-3d-alley-of-peace-set-in-italy"
title: "Recreating Nostalgic Alley of Peace Set in Italy"
author: "80 Level"
date_published: "2026-06-08"
date_clipped: "2026-06-09"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Recreating Nostalgic Alley of Peace Set in Italy

Source: https://80.lv/articles/recreating-nostalgic-3d-alley-of-peace-set-in-italy

Alex K. Arabi Environment Artist Interviewed by Gloria Levine 08 June 2026 Recreating Nostalgic 3D Alley of Peace Set in Italy # Environment Art # Interviews # Blender # Unreal Engine # ZBrush # Substance 3D Painter We talked to Alex K. Arabi to learn how he created his Alley of Peace in 3D, what shaders he used to add variety and mood, and how lighting helped him make this nostalgic atmosphere.
Introduction  Hi! I’m Alex Arabi, an Environment Artist studying at The Game Assembly (TGA) in Stockholm, Sweden. I first opened Blender about three years ago, and for the past two years I’ve been focused on game art production during my time at TGA. 
Before getting into 3D, I spent around five years doing graphic design, both as a hobby and freelance. That’s really where I built my eye for composition, color, negative space, and lighting, things I still rely on heavily in my environments today. 
Moving into 3D felt like a natural step. What hooked me wasn’t just making visuals but the idea of building entire worlds. The first time I ran through a level I made in Unreal Engine, I genuinely got excited in a way I hadn’t before. It made me realize this is what I want to do.  
Alley of Peace This project started when I came across a historical image of an alley in Sanremo, Italy, called Vicolo della Pace. The image was from the late 1800s, and it instantly gave me a strong sense of calm nostalgia. 
The more I looked into it, the more it just felt right. And fittingly, when I translated the name, it literally means “Alley of Peace,” which matched the feeling I had perfectly. 
My connection to Italy mainly comes from football. Growing up, most of my time was split between playing football and playing games, so this project naturally turned into a bit of a love letter to that part of my life. I wanted to create something that felt grounded, lived-in, and personal, even without characters in the scene. 
Research & Brainstorming When starting this project, I made a 6-week half-time plan of what I needed to prioritize to reach the goal I had. My goal wasn’t to do a 1:1 recreation, but to capture the feeling of the alley while shaping it into something that fits my own vision. I wanted the scene to tell a story without relying on people being present. 
It all started with me finding the alleyway on Google Maps and looking at it and the neighboring streets to get a rough sense of scale. From that, I built a modular kit early on, which let me work iteratively and made it easier to test different compositions later instead of getting locked into one layout. 
At the same time, I kept asking myself: " Who lives here? What do they do? What time period are we in?" 
That helped me define what kinds of assets actually made sense. I built an asset list from that and then adjusted each piece to fit the narrative I was trying to tell. 
Blockout I start with modeling blockouts of all the modular pieces and assets that I know I will need in Blender. The modular kit is measured approximately based on the references that I gather. I then continue by building a prototype in Unreal Engine with all the blockout meshes whilst also setting up my main camera angles. 
I began by creating blockouts for the modular kit and key assets in Blender. These were then brought into Unreal Engine, where I assembled a rough version of the scene and set up my main camera angles early on. 
What’s important at this stage isn’t that I get everything perfectly, but that I get my ideas across and test that everything measures and works together nicely. 
While the overall structure stayed close to the reference, I made several artistic adjustments. I controlled building rotations, spacing between elements, and the narrowing of the alley to create a more visually balanced composition. One key change was simplifying the end of the alley into a single main door, which helped establish a clear focal point.
Materials & Shaders All tileable materials in the scene, such as plaster, cobblestone, and metal, were created in Substance 3D Designer. 
The materials were built with a focus on subtle variation and natural wear. Instead of aiming for perfect surfaces, I introduced irregularities in height, roughness, and color to better reflect real-world aging. Working my way from the biggest to the smallest details. 
Gathering references was key to understanding how these materials work and function in the real world. I also tried to think about how they were built in Sanremo.
Building the floor as they were meant, pivoting down in the middle to stream water as a drainage solution, plaster subtly peeling, and bricks that are aged. Every material decision builds on world-building and realism .
Shaders To make the world feel alive, I created a few shaders that break perfection. Shaders that adjust color tint based on world position and a grungy vertex painting shader setup. 
Color Tinting World Position Early on, I noticed that repeated elements like doors and windows had identical color values, which created a uniform and artificial look. To address this, I developed a shader that applies subtle color variation based on world position. 
Each asset receives one of several predefined tints, breaking up repetition and making the environment feel more natural without requiring unique textures. 
Vertex Paint For wear and aging, vertex painting was a must. But instead of just painting directly, I added a breakup mask to distort the brush input, which gave me a more natural, peeling look. 
With adjustable contrast controls, I was able to fine-tune how much wear appeared on surfaces, allowing for efficient iteration and better visual results. 
Trimsheet & RGB Masked Windows I decided early on to use trim sheets for efficiency, inspired by their use in modern game production. The windows in Sanremo share a consistent design language, making them ideal candidates for this approach. 
I first modelled the windows as full geometry, then extracted key elements into flat planes. These were sculpted, baked, and textured into a single trim sheet. 
To push variation further, I introduced an RGB mask system using a secondary UV channel. This allowed me to control grime, sun damage, and edge wear independently in Unreal Engine. The result was a flexible system that added variation while maintaining performance efficiency .
Asset Creation When creating assets, I tried to ground everything in reality by thinking about how things would have been built in the late 1800s. 
I made a mix of reusable and hero props, mostly in the medium to small size range, to balance out the scene since its primary shapes are the large building pieces.
The workflow used to create these props was similar. I would work from the blockout to create a model with the general silhouette shapes in place. It's important for me to think about how things were structured in real life during this step.
I would then take the base model into ZBrush and start sculpting a high-poly version to define the shapes with surface details and more refined silhouettes. In this step, I like to think about what is easier to add in the sculpting phase than in the texturing phase. I add all those elements and then take them back into Blender to retopologize.
When it comes to texturing, I try to create shortcuts to save time by avoiding the need to sculpt smaller repeating details.
I sculpted a lot of the bigger stitches and wrinkles but let Substance 3D Painter add most of the micro details that define the leather material. I also did the smaller stitching with Substance 3D Painter's stitching tool.
Bigger grains were sculpted, but most of the wood definition comes in Substance 3D Painter.
Rocks that were textured for the door ended up being used for set-dressing purposes separately.
Unreal Engine  Composition and set dressing were continuously refined throughout the project. Every prop placement was intentional, either to guide the viewer’s eye or to support the narrative.  
Props placed along the walls help break up silhouettes and create transitions between surfaces. Smaller storytelling elements, such as fallen objects, were used to subtly direct the viewer’s attention toward the main focal point, the door at the end of the alley. 
To speed up workflow, I built a more detailed section early on, which I could duplicate and adjust for variation. This significantly reduced repetitive work. 
Decals also played a major role, helping blend modular pieces together while adding storytelling details like dirt streaks, damage, and human presence. 
The floor was originally flat and boring, so I decided to make small cobblestone meshes to add height manually. These cobblestones added a lot of needed height, but the floor still felt a bit unrealistically flat and even. I got feedback from a classmate to make the floor go inwards in the middle, as it is in the reference. It was a very subtle change, but it made the world of difference!  
Another small hack to save time I did was to make use of the rocks that I originally made for the main door as set dressing. It allowed me to add a bit of intentional clutter. 
Lighting & Post-Production The lighting in this scene is arguably the most vital part of the scene and is, in general, one of the strongest tools an environment artist has. The light steers the viewer's eye and can be used to showcase or hide parts of the scene. It allows the artist to control what becomes important in the environment. Therefore, I had to be precise with how I used my directional light, as that is the main force. In accordance with the light, I also played with fog to create better depth between different segments of the scene.
The directional light alone was, however, not enough, so I decided to give the lamps a bit of extra light. Although slightly unrealistic, it helped lead the eye into the alley better. On top of that, I made use of rect and point lights to make the transition from light to dark easier on the eye, while also making sure there were no overly dark areas in the scene.
I furthermore made use of setting the Diffuse value of the lights to 0, which makes it so that the light does not affect the base color. This allowed me to make certain areas pop without them becoming overly exposed.
Post-processing was iterated on throughout the project. I adjusted bloom, vignette, and lens effects in Unreal Engine to enhance the atmosphere.
For the final color grading, I created a LUT in Photoshop by editing a screenshot of the scene. This gave me precise control over the final look, allowing me to push the nostalgic tone I was aiming for. I mainly played around with adjustment layers such as Color Balance, Selective Color, and Curves. I aimed to bring some cooler tones into the shadows while keeping the midtones and highlights on the warmer side. Keeping the contrast high without creating overly dark areas is also what helped push the nostalgic feeling.
Conclusion This project taught me several important lessons that I’ll carry into future work. 
I really learned the value of iteration and the value of asking for feedback during this project. Many of the improvements in this scene came from revisiting and adjusting earlier decisions after asking for opinions from various people rather than trying to get everything right the first time. Being flexible and open to change was essential. I also realized that asking different types of people gets me so much more insight. I would ask anyone, from 2D and 3D artists to my family members who just love video games! Everyone had a unique perspective based on their experience. 
The importance of composition is another lesson. Strong composition can elevate even simple assets, while weak composition can undermine highly detailed work.  Avoid over-detailing too early; focusing too much on small details in the beginning slowed down progress and didn’t always translate well in the final scene. Learning to guide the viewer’s eye intentionally and prioritizing large shapes and overall readability first made a significant difference to the end result. 
However, one of the biggest takeaways from this project is the confidence that it’s okay that the scene doesn’t look good in the beginning. It’s also okay that not everything is set in stone; if anything, it’s more interesting that way! 
My advice for aspiring environment artists would be: f ocus on fundamentals like composition, lighting, and scale before worrying about complex assets. Don’t be afraid to iterate and try to understand why something works rather than just how to create it. 
Overall, this project helped me grow both technically and artistically and gave me a clearer understanding of how to build environments that feel cohesive and intentional. 
Thank you for taking the time to read my process! Lotsa love! 
Alex K. Arabi , Environment Artist Interview conducted by  Gloria Levine Built for Creators. Read by the Best Partner with 80 Level Comments 0 Type your comment here Leave Comment Built for Creators. Read by the Best Partner with 80 Level
