---
source: "https://80.lv/articles/how-to-create-a-haribo-style-translucent-jelly-bear-candy-material"
title: "How to Create a Haribo-Style Translucent Jelly Bear Candy Material"
author: "QiYu Dai (Aiden)"
date_published: "2026-09-08"
date_clipped: "2026-09-08"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# How to Create a Haribo-Style Translucent Jelly Bear Candy Material

Source: https://80.lv/articles/how-to-create-a-haribo-style-translucent-jelly-bear-candy-material

QiYu Dai (Aiden) Lead Texture Artist Interviewed by Emma Collins 08 September 2026 How to Create a Haribo-Style Translucent Jelly Bear Candy Material # Interviews # Materials # Substance 3D Designer QiYu Dai (Aiden) spoke about the creation process behind the Haribo Bear Candy project, explaining how he modeled the bear shape using shapes like ellipsoids, spheres, and cylinders, and detailing how he achieved the translucency with color layering.
Introduction Hello, I am Aiden, and I am a Texture Artist. I have worked at Ubisoft Chengdu and Ubisoft Montreal for many years, and it's been a pleasure to work on Tom Clancy's Rainbow Six Siege and For Honor. Now I am a Lead Texture Artist at Mihoyo.
Haribo Bear Candy This is an interesting thing that I wanted to do, since it reminds me of my time in Montreal. There are two things I wanted to try. The first one is the SDF function, and it is a very good feature that can be used for scattering elements; artists can easily use it to do rotation, scaling, positioning, and so on.
So for this project, in order to have the best result, I decided to use SDF and ZBrush to merge these two workflows for this artwork. For the second one, I wanted to try to do the whole render and post-adjustment in Substance 3D Designer; it would be a nice procedural pipeline to try.
Workflow In Substance 3D Designer, the first important step is making a bear model using the SDF function. I used a 3D Viewer node for previewing the result in the 2D View.
First, I made the head, chest, and waist parts and started with an ellipsoid; then I tweaked the radius and offset to place those elements in the proper position. Then I used a Union Smooth node to merge all of them into a basic body part.
Then, I created the ears, arms, and legs; this step is similar to sculpting, refining the shape and silhouette until it looks nicer and smoother.
I created the hands and the feet, and then I merged them with the previous step.
I used Sphere and Cylinder as the start to create the eyes and the mouth, and then I used Subtraction Smooth to add them to the bear's face.
For the dots on the chest, I used a Rock node as the base. Randomness worked well for shape variation, so for different dots, I just needed to copy this group of nodes and give a different value to Randomness; then the shape would change randomly.
Just in case, and also for a better result, I still made a model in ZBrush, and then I generated a few Height maps, which could be used as a base for the material.
Finally, the basic bear was finished; then I just needed to use Shape Splatter as I normally would to make the material with bear elements. The difference this time is that I used Shape Splatter v2 because of SDF. Shape Splatter v2 has many good new features; it helps a lot by using the SDF function.
Then I started to build the color for this material. My goal was to make it look like a good jelly material, but since it's just a simple plane, achieving a real translucent effect was difficult. So I spent more time on the coloring to create a convincing fake-translucent effect. I built up the color as the base.
Adding AO color.
Adding color variation.
Adding color variation (edge specular).
Adding color variation (fake translucent).
Adding more translucent effect.
Then I created Roughness. I just started by desaturating the Base Color, then blending the Noise map and Grunge map.
Adding extra detail on the Roughness.
The material is finished; now it is time to do the render. I decided to do it with a PBR render and all the post-adjustments in Substance 3D Designer; it will be convenient to adapt other materials using this procedural pipeline.
In this workflow, I used two PBR render nodes. The first one is the base one to have a complete render; the second one is for some extra effects to add to the final render to get a better result. This part can be tricky.
The first one is getting a base render.
And I duplicated another one, but I used AO as the Base Color for rendering. It is prepared for post-adjustment.
Blending with a blue channel from the Normal map.
Blending with the render that is a duplicate.
Blending with the Raw Specular map from the PBR render.
Blending with Raw Specular again, but using a different blending mode to enhance the specular effect.
Finally, I proceeded with some extra adjustments as needed, and then the final render was done.
Because of this procedural pipeline, I can change the shape easily, and all the adjustments update automatically to match the new shape.
Conclusion Overall, I finished this material in a few hours; I think the challenges were in two parts. The first one is creating the bear by using SDF; it is a new feature in Substance 3D Designer, and it's a more procedural pipeline, so it's not as intuitive as painting or sculpting. I had to try different nodes to build them up together, then find the best one.
I usually like to look for special and interesting subjects to practice with, like this bear candy. It's a translucent material, and the challenge is figuring out how to make it look and feel like jelly using only a flat plane, with no modeling involved. I think that's what makes it special: if you can pull it off, your material or artwork becomes much more appealing.
QiYu Dai (Aiden) , Lead Texture Artist Interview conducted by Emma Collins Built for the Game & Digital Art Industry Get Our Media Kit Comments 0 Type your comment here Leave Comment Built for the Game & Digital Art Industry Get Our Media Kit
