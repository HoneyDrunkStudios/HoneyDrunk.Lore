---
source: "https://80.lv/articles/how-to-build-an-atmospheric-stylized-lighthouse-scene-with-a-custom-modular-set"
title: "How to Build an Atmospheric Stylized Lighthouse Scene with a Custom Modular Set"
author: "Albert Serrano; interviewed by Stephanie Almogabar"
date_published: "2026-10-09"
date_clipped: "2026-10-12"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# How to Build an Atmospheric Stylized Lighthouse Scene with a Custom Modular Set

[Albert Serrano](https://80.lv/author/albert-serrano)

Environment Artist

Interviewed by

[Stephanie Almogabar](https://80.lv/author/stephanie-almogabar)

09 October 2026

# How to Build an Atmospheric Stylized Lighthouse Scene with a Custom Modular Set

[#Environment Art](https://80.lv/articles/environment-art)[#Interviews](https://80.lv/articles/interview)[#Blender](https://80.lv/articles/blender)[#Unreal Engine](https://80.lv/articles/unreal-engine)[#ZBrush](https://80.lv/articles/zbrush)[#Substance 3D Designer](https://80.lv/articles/substance-designer)[#Substance 3D Painter](https://80.lv/articles/substance-painter)

Albert Serrano explained how he created tileable materials for the scene, shared his tips on ensuring smooth blending between different materials, and talked about how he made an atlas of hand-sculpted plants to create stylized vegetation.

### Introduction

My name is Albert Serrano, and I am a 3D Environment Artist currently working at MercurySteam in Madrid, Spain. I have always been passionate about video games, and over time, that passion grew into curiosity about how they were actually made. This eventually led me to explore the world of 3D art and discover that creating the environments I admired in games could become a career.

I started learning Blender in my spare time while studying Audiovisual Media at the university. Later, I continued my studies in Valencia while also developing my 3D skills independently, aiming to build a strong portfolio and break into the video game industry.

I have now been working at MercurySteam for over three years, and I am proud to have had the opportunity to contribute to a prestigious title for Nintendo.

I have always been drawn to stylized art and the unique visual language it brings to games. Overwatch, World of Warcraft, and Sea of Thieves are some of my biggest inspirations, especially for their strong shapes, attractive colors, and distinctive environments. These influences have naturally shaped my own approach and the kind of worlds I enjoy creating.


### Lighthouse: the Concept

I had gone some time without working on a personal project when I came across this [concept by Gustav Nordgren](https://www.artstation.com/artwork/KalNdG). I immediately loved it and felt it was a great excuse to get back to creating. I gathered references for the visual style and began planning the materials and assets, especially the water, which I considered the key element in achieving the overall look of the scene.


### Blocking Out

I started by creating a simple blockout in Blender and bringing it into Unreal Engine. This helped me establish the proportions, camera distance, and overall composition, while giving me a clear idea of the key elements I needed to focus on for the final scene.


### Materials

At this stage, I identified the elements that could rely on tileable materials, since they would be repeated throughout the scene. I then started developing these materials and trims in Substance 3D Designer, using them to define the stylized look I wanted for the scene.


I also created a modular set of wooden pieces in different sizes, sculpting them in ZBrush and giving them enough texel density to be easily reused and scaled throughout the scene, as they would be applied in many different ways across the environment.


### Water

For the water, I wanted something stylized yet lightweight enough to keep the scene running smoothly in Unreal Engine. Since at that point I didn't have enough experience with Unreal Engine's Material Editor to create something this complex from scratch, I followed a tutorial by [Ghislain Girardot](https://www.youtube.com/watch?v=rV6TJ7YDJY8&t=6s) and made a few small adjustments so that it would fit the look of the scene. The amount of variation you can create by tweaking a few parameters made this one of my favorite parts of the project.


### Props

For the props, I worked mainly in ZBrush, shaping them to match the stylized look I wanted. This is always one of the more enjoyable parts of the process, as it gives me more time to focus on individual assets and add personality to them. I wanted to keep them fairly simple overall, while still giving them enough detail to feel interesting and relevant to the scene.


### Vegetation

For vegetation, I created a simple atlas containing the different types of plants I needed in ZBrush and then textured it in Substance 3D Painter. I also added a few parameters in Unreal Engine to adjust their colors directly in the engine, allowing me to easily create variations and adjust them to fit the scene.


### Modules

Once the main scene looked fairly solid, I decided to explore a second camera angle and expand the environment. I already had most of the necessary assets and materials, so adding a few simple modular elements felt like a good way to give the project more depth without significantly increasing the workload. Since I could reuse the tileable materials I had already created, I was able to build the new area relatively quickly.


**Small Tip**

To better blend the different wall materials, I used the same plaster material with a different tint through an additional Vertex Color channel. This added an extra layer between the plaster and stone, helping the materials blend together more naturally and allowing me to paint it in other areas to add more variation to the walls. It also made it possible for me to control the darkness of the tint.


### Decals

Another small detail that made a big difference was the use of bird-dropping decals, which I created in Photoshop. They might seem insignificant, but they helped give the scene the character I was looking for and added more variation to the environment.


### Making the Scene Feel Alive

One of the things I value most when looking at an environment is the feeling that the world is alive. I think these small touches give a scene character and greatly enhance the atmosphere it conveys. With that in mind, I added a couple of particle systems for the fish underwater, the seagulls, and the subtle wind lines, along with movement in the water and seaweed, and set up a camera shot designed to bring everything together.

### Finishing Touches

For the final touches, I adjusted several post-processing settings to bring out the colours and saturation, as I wanted the scene to have a distinctive, colourful look with slightly stronger contrast in certain areas. I also refined the lighting, using a Directional Light as the main light source, which I kept close to the original concept from the beginning, as I felt it suited the scene perfectly. I added a few Point Lights in specific areas to create more visual interest, and finally introduced water caustics to enhance the underwater atmosphere and complete the look.


### Advice for Beginners

I still feel like I have a lot to learn, especially after only a few years in the industry, but one thing I would encourage any beginner artist to do is to start projects and commit to finishing them. I'm not saying you have to commit 100% to every project you start, since we all have unfinished projects, but it definitely helps to take some of them seriously and push yourself to see them through to the end, until you can look back at the result and feel happy with what you have achieved.

Sometimes you reach a point where you look at your work and feel that something is not working, and it can be very frustrating. It is easy to lose motivation and move on to something else, but learning to work through those moments is an important part of the process. By continuing to work on the piece and figuring out how to solve the problems you are not happy with, you will gradually improve. In my opinion, the process is ultimately more important than the final result, as the finished piece is simply the outcome of everything you have learned and worked through along the way.


### [Albert Serrano](https://www.artstation.com/albertserrano), Environment Artist

#### Interview conducted by [Stephanie Almogabar](https://www.linkedin.com/in/stephanie-almogabar-958b34318/)
