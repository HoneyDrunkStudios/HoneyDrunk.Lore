---
"source": "https://80.lv/articles/how-to-make-a-stylized-game-ready-minecart-prop-using-hand-painted-textures"
"title": "How to Make a Stylized Game-Ready Minecart Prop Using Hand-Painted Textures"
"author": "Raphael Fabris"
"date_published": "2026-10-08"
"date_clipped": "2026-10-08"
"category": "Technical Art & Creator Tools"
"source_type": "rss"
---

[Raphael Fabris](https://80.lv/author/raphael-fabris)

3D Artist

Interviewed by

[Emma Collins](https://80.lv/author/emma-collins)

08 October 2026

# How to Make a Stylized Game-Ready Minecart Prop Using Hand-Painted Textures

[#Interviews](https://80.lv/articles/interview)[#Props](https://80.lv/articles/props)[#Unreal Engine](https://80.lv/articles/unreal-engine)[#Marmoset Toolbag](https://80.lv/articles/marmoset-toolbag)[#Maya](https://80.lv/articles/maya)[#ZBrush](https://80.lv/articles/zbrush)[#Substance 3D Painter](https://80.lv/articles/substance-painter)

Raphael Fabris shares his tips on saving time and preserving the look of the scene when jumping between 3D applications, and explains why, in some cases, creating a new topology during unwrapping is better than using the one from the blockout stage.

### Introduction

I'm Raphael Fabris, and I've been a self-taught 3D Artist for about 6 years now. Everything started during the quarantine, when I was in my last year in college, in a completely different field. A YouTube video about an indie devlog appeared on my feed, and it really fascinated me to the point where I started looking for ways to do it myself immediately.

During that process, I decided to try to learn the basics of 3D modeling online to help create assets for the small games I was making, but this secondary thing quickly became my main passion. Now my main focus is 3D art for games, and I've been doing it professionally for about 4 years now. I had the pleasure of working on a few games as a freelancer, for instance, The Lord of the Rings: Return to Moria and some others that are still under NDA.

### Getting Started with the Minecart Project

For my next project, I wanted to be able to practice multiple things at once, such as stylized sculpting and stylized texturing, both inspired by Wayfinder, a game that, for me, has really stunning visuals.

One of the materials I struggle with the most when doing both the high poly and textures is wood, so when I saw this concept, I thought to myself that this is a perfect asset to practice both things. The original concept is from [Yuriy Gaber](https://www.artstation.com/artwork/YeZYYV), and I also used [Fenix Xu](https://www.artstation.com/artwork/ZGmNJ0)'s version as a reference for the overall shape.



### Modeling

For any projects, I like to start with Maya; that is because I feel I have more control over the scales and positions of the mesh there.

For this one, it wasn't any different, especially because the model is really boxy and doesn't have any eccentric shapes. Another reason I like to start my blockout in Maya for assets like this, where I have a range of different parts, in this case different wood beams and planks, is that I have more control over the consistency of the bevels.

One of the tricks to achieve that is using bevel in Absolute instead of Fractional; that way, you don't need to guess each one individually by eye.



Another thing I keep in mind during this blockout stage is the complexity of the mesh. For example, in this shovel blade, you can see there are 2 separate sub-meshes instead of one, with good topology that allows me to avoid pinching.

The reason I did this is that I knew I was going to make use of DynaMesh in this piece, and I knew the context around this piece: this is a wooden shovel on a minecart, meaning that this part would be heavily dented and damaged, so there's no reason to make the surface clean.



I highly recommend that everyone who uses the Maya/ZBrush workflow grab an import/export tool. This is probably the best time-saver out there in our field, in my opinion. The one that I use is the GN ZBrush/Maya Import/Export Tool, but I know there are other options out there.

To achieve the style that I wanted on this piece, I made use of masking with moving and DynaMesh for big silhouette changes, Dam Standard for surface detailing, and Knife Curve with Trim for bevel detailing.



In the video below, I also showed how I achieved this organic-like detail on the surface of the metals. I used the Dam Standard for the whole project for these; the key here is to have control of both your brush direction and strength, so that the detail feels organic and not just like an extruded line.

### Unwrapping

For the low poly, I decided to draw a brand new topology instead of reusing the one from the blocking, because I'd changed the silhouette and bevels to a point where it wouldn't be worth adapting the original topology to it.

And since this asset wasn't going to receive any deformation, I didn't worry about making the topology evenly spread; instead, I decided to focus most of the polycount on the silhouette and bevel changes so that the game mesh would still feel really organic and not that low-poly. The rail is an exception, because I knew I would want a bend happening in the final version of the asset.



For the UVs, I wanted to avoid the mirrored look as much as possible, but at the same time, I wanted to keep the texel density good enough for a low resolution. This video shows how I approached UVs with that idea in mind.

### Texturing

Since the beginning of the project, I knew I wanted to achieve a painterly, stylized look mixed with PBR. I decided to do the whole process in Substance 3D Painter instead of trying to mix 3DCoat into it as well; that is because I like to keep my list of software as short as possible so that the overly complex workflow doesn't get in the way of my creative study.

Before doing any manual work, I like to define basic guidelines on my material work first. I achieve this by creating a base color and some fill maps with generators like curvature and AO, and a light direction on the base color to add more volume.



After that, I like to jump straight into hand-painting. Honestly, my workflow around this can become messy, so I highly recommend that you always name and organize your layers for your own sake.

One thing that I like to do is hand-paint on fill layers instead of paint layers; that helps me to avoid getting distracted. If I'm painting shadows, I will not be able to just change colors in the middle of the process to paint highlights, and that helps me keep things organized and not have all sorts of details on different layers.

As you can see in the video, I like to paint any AO contacts between sub-meshes, instead of relying on baked information, as that makes it possible to keep the AO bake clean.

A quick way to create color variation is to use RGB noise. If you Google it, you will find plenty of good textures out there to help you break that flat color look.

Also, I really think it's important to create at least a blueprint of your final scene wherever you're planning to render your asset. Things can change dramatically between your 3D apps.

In my project, I knew I wanted to render it in Unreal Engine, with a yellowish main light source, so I created the blockout of the scene right after the baking process and constantly checked how things were looking in the final scene. As you can see in the image, there's a big difference between Substance 3D Painter and Unreal Engine.



### Lighting & Rendering

I wanted to keep the render scene as simple as possible, so I went for a 3-point light system and a Sky Light, which is Unreal's default lighting source.

But I aimed to achieve that God-ray-like light emphasizing the front of the minecart, and the best solution I found for that was using a Spot Light with the default fog present in Unreal.

For the ember effects, I used this [1-minute tutorial from Royal Skies](https://youtu.be/1n1q4kQ9Ehg) to create one – it's a really simple process.

### Conclusion

This was a really fun project to do, as I was able to study things I was avoiding the most, such as stylized wooden materials and hand-painting. And this is something I highly recommend beginners and everyone else do: pick your projects based on what you know you need to improve.

It's hard, and you may want to give up in the middle of it; I know because I feel the same way, but just keep pushing through it. It's definitely worth it in the end, because you will feel way more satisfied after finishing a project where you learned something new, instead of repeating the process you're already comfortable with.

Thank you so much for reading this, and I hope this can help you with your future projects in some way.



### [Raphael Fabris](https://www.artstation.com/raphafabris), 3D Artist

#### Interview conducted by [Emma Collins](https://www.linkedin.com/in/emma-collins-663070320/)
