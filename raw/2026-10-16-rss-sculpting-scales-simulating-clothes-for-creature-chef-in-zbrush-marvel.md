---
source: "https://80.lv/articles/sculpting-scales-simulating-clothes-for-creature-chef-in-zbrush-marvelous-designer"
title: "Sculpting Scales & Simulating Clothes for Creature Chef in ZBrush & Marvelous Designer"
author: "Yuriy Barchuk"
date_published: "2026-10-16"
date_clipped: "2026-10-16"
category: "Technical Art & Creator Tools"
source_type: "rss"
date_modified: "2026-10-16"
---

# Sculpting Scales & Simulating Clothes for Creature Chef in ZBrush & Marvelous Designer

Yuriy Barchuk walked us through the workflow behind the Breakfast – Chef Extraordinaire project, discussing clothing simulation for a non-human character in Marvelous Designer, sculpting scales in ZBrush, and rendering in Unreal Engine 5.7.

### Introduction

Hello! I’m Yuriy Barchuk, a 3D Character Artist based in Canada and a recent graduate from Think Tank Training Centre.

I never thought I’d actually be trying to make a living from art, as I originally planned on pursuing a career in chemistry when I graduated from Mount Saint Vincent University in 2022. After completing my degree, I realized that a career in academia wasn’t the right path for me. I decided to follow my passion for video games and my love of creating, which led me to Think Tank Training Centre and 3D character art.

What began as learning the fundamentals at Think Tank Training Centre quickly developed into a passion for character creation. My training continued beyond Think Tank through a mentorship at Zombie Art School, where I focused on developing my skills in clothing and outfit creation, before returning to Think Tank for an additional mentorship.

That journey culminated in Breakfast-Chef Extraordinaire, a project that brought together the skills I had developed along the way and gave me the opportunity to push my character work further. It was an exciting chance to see how all those different pieces of my training could come together in one project.

I’m still at the beginning of my professional journey, and I’m excited to continue learning, developing my artistic voice, and connecting with opportunities where I can grow, contribute, and bring my skills to new projects.

### Start of the Project

As with any project, the first thing I wanted to do was find a concept that piqued my interest while also giving me an opportunity to grow in a particular area. After a few hours of searching, I came across [Ana Fedina’s Breakfast the Chef](https://www.artstation.com/artwork/0lRGWy) concept and instantly fell in love with it. I just knew I had to take it on.

I had three main goals when working on Breakfast: to improve my general prop-creation skills, explore creating a more realistic creature character, and develop my skills in scale creation as a whole. Each goal brought its own unique challenges throughout the process. To help minimize these challenges, my first step was to gather references and set clear goals for the project in terms of style, fidelity, polygon count, number of texture sets, and the software I would be using.

My main references when creating Breakfast were the Kobolds from Larian Studios’ Baldur’s Gate 3, along with bearded dragons, which I used as a reference for the character’s overall feel and coloration.

### Modeling

#### Blockout

I began the model in ZBrush, blocking everything out with DynaMesh spheres and basic shapes. As I was unable to start with a base mesh, this allowed me to establish the general proportions and feel before refining and tweaking it further. When creating Breakfast, I knew the mouth would have to open, so I blocked out the top and bottom of the mouth separately before DynaMeshing them together. Once the body was created and DynaMeshed together, I ZRemeshed it to ensure I had relatively clean topology to sculpt on before creating a layer and moving the mouth closed on it, allowing me to work on both views of her.

The clothing was originally blocked out by extracting meshes from masks on the main body and using different tools to move them into place and ensure they would have a good silhouette to follow when I moved to Marvelous Designer to start the outfit.

Outside of using simple shapes in ZBrush to get a general feel for the props, I moved to Maya 2025 to start working on some of the hard-surface props, such as the backpack and her cooking utensils. This blockout was overall quite quick, as I was lucky that Ana Fedina included multiple images of Breakfast along with all her props, and even different variations of them, from different angles and views.

#### Marvelous Designer

When my mentor and I were satisfied with the feel of Breakfast, we moved to Marvelous Designer to start doing some clothing simulations and getting an outfit ready for her, using the blockout I made as our main reference.

This was my first time using Marvelous Designer on a non-human character, which definitely brought a unique set of challenges I didn’t fully foresee. The primary challenge was having to work around her tail and legs, as traditional clothing patterns didn’t work and had to be modified to accommodate her. I also came to the realization that some parts of the outfit, such as the inner skirt, would have to be made in different software to make them match the concept.

Once the outfit was completed and the UVs were created in Marvelous Designer, I exported the flat patterns into ZBrush, where I ZRemeshed them down to a lower topology that was easier to use before exporting this new mesh into Maya along with the full 3D outfit and the old flat pattern.

Overlaying the flat patterns, I fixed up the topology on the newer mesh with Quad Draw before transferring the UVs to it from the older mesh using the Transfer Attributes tool in Maya. From there, using the same method of transfer but just using UV space rather than world space, the retopologized mesh was moved to the same place as the 3D one before I smoothed it three times and hit Transfer Attributes once again to allow the mesh to conform to my Marvelous Designer simulation better. Doing this allowed me to sculpt on much cleaner topology and avoid any weird pinched points.

#### High Poly & Scales

Once everything was retopologized and good to go, I imported the clothes back into ZBrush and started the cleanup process. I began by smoothing out any issues that occurred from the transfer process and adjusting the clothing to better match the original silhouette before using the Panel Loops feature in ZBrush to add thickness to the clothes, making sure to turn Polish and Bevel to 0 and set the number of loops to 16. Because I smoothed it out three times earlier, I was able to reconstruct the subdivision levels on the clothes, which allowed me to make bigger changes more easily if I had to.

For the secondary details, I focused on sharpening up some of the folds and adding additional ones where I believed it would help the flow or help with making the character believable when it was rigged and moving, such as the folds on the elbows being more compressed rather than flowing like the rest of the sleeves. I completed the tertiary details with a mix of memory fold alphas along with very light strokes of the Standard Brush. Having the AccuCurve feature toggled on the Standard Brush allowed me to create some straight and sharp folds that still looked natural.

As I worked on sculpting secondary and tertiary details onto the clothing, I bounced back and forth between the main body and the props, making sure that everything was being done to roughly the same level throughout. The majority of the props were either continued in Maya or finished with a sculpting pass in ZBrush, such as the backpack itself.

Now for arguably the hardest and most time-consuming part of the project: making the scales. I started by splitting up the body into parts and deleting the parts that were hidden, such as the chest and most of the legs, before subdividing a few more times to get it dense enough to start making the scales without bogging down my computer with unnecessary parts that wouldn’t be sculpted on. I started by creating a new layer for each part of the body and the type of scale on it, so I could delete it if I was unhappy with it or simply tweak the intensity to get the effect I wanted. I also set a morph target to the body before I started placing down any scales so I could adjust the intensity of separate parts of the scales and highlight specific areas that I wanted.

To get a base for the scales, I used the [scale brush pack from Pablander Academy](https://www.pablander.academy/premium-pack/scales-brushes-pack) with different sizes. It allowed me to get a good start on all the different types of scales throughout the body. After the base was placed, I did a pass of cleanup for any parts of the brush that overlapped unnaturally before doing a pass to deepen some of the grooves of the scales and make them pop a bit more. I ran the Elastic Brush with a lower intensity over the top of the individual scales to make them a bit taller and stand out more without affecting the underlying base I got from the brushes. With the Morph Brush, I was able to tone down areas that I didn’t want highlighted, such as the flat parts at the top of her head and the front of her nose, while keeping the important “Hero” scales around the cheeks and eyes quite visible.

I followed a similar process with the hands and feet and simply highlighted the edges of the sharper, raised scales using the Gio Brush. I also cleaned up the palms of the hands, where there aren’t supposed to be any of the individual small scales.

#### Storytelling

One of the best parts about this project was the amount of storytelling that could be added to it. This ranged from simple things, such as cuts on her left-hand fingers and the wear and tear of her equipment, to bigger things, such as her logo being burnt into the top of her backpack or the mimic prop I thought would be fun. The mimic prop allowed me to play around with some more fun shots, such as the one at the end of my ArtStation post, where she realizes that she has a stowaway and decides to get rid of it in the most appropriate way possible: a bonk on the head.

### Retopology & UVs

The retopology and UVs were all completed entirely inside Maya using the built-in tools and Quad Draw. A good chunk of the topology for the props and smaller objects could be reused with just a little bit of cleanup, while I had to create the topology from scratch for the clothes and the body itself.

I started by getting the body parts completed so I could line up my edges based on the body topology. I did the fingers and toes first to establish the edge flow and tried to keep everything as low and clean as possible before adding more cuts once the base topology was in place.

For the head topology, I had to use a similar process to when sculpting, splitting up the jaw from the rest of the head before decimating so I could retopologize each part separately and then reconnect them once they were done. My main goal throughout all of this was still to get as clean an edge flow as I could, giving me the flexibility to add or remove edge loops without creating more work for myself.

The UVs in this project were overall quite simple, as the majority of things were either cylindrical or square in shape, which allowed me to straighten them easily using pinning and regular scaling tools in Maya. My original plan was to try to get both the body and head into a single 4K texture set, but my mentor and I decided that, due to how important they are to the character, we would split them up into two separate 4K maps, even if the texel density was different from the rest of the model.

### Texturing

With the retopology and UVs being completed, it was time to move on to baking my high poly onto my low poly. For this, I used Marmoset Toolbag 5 for the main bakes due to being able to tweak the cage and skew easily in the software, and partially in Substance 3D Painter to be able to get the material ID to make my life easier during the texturing process.

With the bakes completed, I returned to Maya to quickly open the backpack and set that part of the scene up so I could import the character as is, with the backpack open beside it, which allowed me to work on everything in a single save file, as all the maps were shared between the two.

All of the texturing was done in Substance 3D Painter with a variety of different techniques. The base for some materials, such as the metals, was started as a smart material, with me adding further breakup, color variation, and storytelling details, while others, like the clothes, body, and wood, were made from scratch using the different maps obtained during baking (AO, curvature, cavity, thickness, etc.) to highlight various details.

Due to scales blending together smoothly with a variety of different shades, I had to take a different approach by blending in hand painting along with the procedural textures to get a more organic feel to it. After pushing as far as I could with procedural texturing, I created a variety of new layers of different colors set to lighten or multiply and hand-painted over individual scales to break them up from the base colors. I had to do a similar process for the transition between the white and orange scales, in which I had to find colors that would fit in the middle and create similar variation as with the orange and the white scales.

One of the most difficult parts of texturing this project was creating the food textures and trying to make them believable. Due to all the natural variation in height, color, and roughness, it’s hard to replicate the natural feel and look of food in the real world.

### Rigging

To make sure I was able to get the best possible result from my model, I used the Maya Quick Rig tool to create a basic rig and skin weights as a base. Once that base was completed, I went further and added joints for the fingers, tail, jaw, tongue, and ears to give me extra freedom when posing Breakfast. Due to this being a non-human character and the rig being somewhat limited, I had to come up with different ways to add expressions to her. This led me to create additional joints, such as the ears, allowing me to mimic animals in the real world showing emotions, such as cats doing “airplane ears” when threatened or displeased.

### Lighting

The entire scene was set up and rendered in Unreal Engine 5.7 using different assets I obtained through FAB, such as the trees and other foliage. My main goal when creating both the scene and lighting was to evoke a feeling of a new adventure and get a bit more of a cheerful atmosphere. My main reference for this was the first LotR movie when the hobbits were just starting to leave the shire/are leaving Bree. To set the scene up, I first created a new level and went into landscape mode to be able to sculpt out some hills, ensuring the center arena is a bit flatter to pose my model and make the area seem like a natural forest.

Using the foliage mode, I selected the tree models I obtained from FAB, setting my density to 0.05 and painting on the trees around the map and carving out a small clearing in the center for the Breakfast to be posed. I did the same process with the smaller foliage and painted the area with a density of 0.5, followed by clearing up and individually placing the foliage I wanted at specific places.

The lighting setup was quite simple, trying to mimic natural outdoor lighting, with most of it being driven by a directional light. With the trees having built-in movement and leaves, it created a fantastic effect of the light coming in through the leaves and lazily moving with the wind. I tweaked the direction and angle of the directional light, and when I was happy with it, I added a basic three-light setup with the key light being one of my main lights to highlight the front and get good shadows across the model, a weak fill light to just lighten the darker areas slightly, and a blue-tinted rim light coming from the back, which let me keep a more natural look to the scene and character.

Once my light setup was completed, I added a post-process volume with infinite bounds to tweak the values and do post-production right in the engine. The primary values I tweaked were the contrast and shadow values, both of which I increased slightly to help me get more of a happy high fantasy feel to the piece. I also played around with the exposure to make sure that nothing was overblown. Lastly, I played around with the color temp settings, giving it a warmer tone to the images, which helped me develop that more cozy and inviting feeling.

### Final Words

After about three and a half months and countless hours working on this project, I was finally able to complete it earlier than expected! That said, it still came with some challenges along the way. The primary ones were learning and creating non-human anatomy, developing the scales to a level I was happy with, and figuring out how to make all of the food props look convincing. These challenges pushed me to grow as an artist more than ever before, so I’m glad I faced them. They also taught me new ways to speed up my workflows and improve my planning at the start of a project.

For those starting out on the journey that is 3D art, I highly recommend pacing yourself and trying to learn things one step at a time. When I first started doing 3D art, I wanted to go too far too fast before learning all the necessary tools and skills, or I would take on projects that were simply outside my skill level. Taking the time to plan and prepare for a project and everything it entails has helped me tremendously. Just be sure to keep pushing yourself further with each project!

Big thanks to Emma and 80 Level for reaching out to me and allowing me to discuss the making of this project. Thanks as well to my mentor throughout this project, Thiago Vannuchi, all the global mentors at Think Tank Training Centre, and my friends and classmates, without whom this project wouldn’t be what it is. If you’d like to see more of my work or want to connect, check out my [ArtStation](https://www.artstation.com/yuriy_barchuk), [Instagram](https://www.instagram.com/yuriy_barchuk/), or [LinkedIn](https://www.linkedin.com/in/yuriybarchuk/)!

[Yuriy Barchuk](https://www.artstation.com/yuriy_barchuk), 3D Character Artist

#### Interview conducted by [Emma Collins](https://www.linkedin.com/in/emma-collins-663070320/)
