---
source: "https://80.lv/articles/turning-2d-concept-art-into-a-detailed-painterly-3d-world"
title: "Breakdown: Turning a 2D Concept Into a Detailed & Stylized 3D Scene"
author: "Angelo Ciervo"
date_published: "2026-08-11"
date_clipped: "2026-08-13"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Breakdown: Turning a 2D Concept Into a Detailed & Stylized 3D Scene

Source: https://80.lv/articles/turning-2d-concept-art-into-a-detailed-painterly-3d-world

# Turning 2D Concept Art into a Detailed Painterly 3D World

Angelo Ciervo took us behind the scenes of his process for creating a colorful, immersive stylized environment, from building modular pieces and hand-crafted trees to texturing the scene.

### Introduction

Hello guys, nice to meet you all! My name is Angelo Ciervo, and I am an Environment Artist and 3D Artist specialized in stylized environments. I began my journey in game art by studying at IUDAV, a school focused on video game development and digital arts. After graduating, I joined Art Train Academy, where I was mentored by Sathish Kumar. That experience helped me strengthen both my artistic and technical skills and gave me a deeper understanding of environment design.

I then started my professional career as an Environment Concept Artist at Reply Game Studios, where I worked for nearly two years and contributed to some unannounced projects. Over the past few months, I have been expanding my skill set by focusing on Environment Art and 3D art, specializing in stylized environments. I enjoy combining concept art principles with real-time workflows to create something amazing.

### Environment Art Stylized

For this project, I was inspired by the amazing work of Linawang. I used her concept as a foundation and expanded upon it, aiming to create an environment that felt even more colorful, lively, and immersive while still respecting the original design. With every personal project, I like to challenge myself by taking on something more ambitious than the last. In this case, my goal was to build a larger and more complex environment while keeping the production time relatively short.

### Linawang

It was a great opportunity to improve both my artistic and technical workflow. When it comes to gathering references, I usually start by creating a simple mood board in Miro to organize my ideas. I also collect references for materials, architecture, vegetation, and lighting. Over the years, I have built a large personal reference library that I can quickly draw from whenever I start a new project.

I believe this stage is one of the most important parts of the process because it allows me to study how other artists solve visual and technical challenges, giving me ideas that I can adapt to my own work. Once I have a clear vision, I transfer everything to PureRef, which makes it much easier to manage and access my references throughout the entire production process.

I already had a basic artwork that guided the main direction of the composition. However, when translating the concept into Unreal Engine, one of the most important aspects for me was maintaining coherent proportions between all the elements in the scene, making the environment feel believable and natural to the viewer. I usually start with a rough blockout directly in Unreal Engine using simple shapes like cubes to quickly define the composition, scale, and main volumes.

After that, I export the blockout into Blender, where I begin breaking down each structure into smaller and more manageable elements. I start by giving every structure a consistent nomenclature that carries over into Unreal Engine, keeping everything organized, especially later, when I'm using trimsheets and stretching UVs across each mesh. The number of assets was very high in this case, so I used a mid-poly workflow for most of the assets.

This approach helps me transform a complex problem into multiple smaller problems that are easier to solve. During this phase, I focus on checking proportions, refining shapes, and identifying which parts can be reused to create modular assets. Building simple modular pieces allows me to speed up production while keeping consistency throughout the environment. Since this project was mainly focused on a village environment, architecture was the central element, so I dedicated most of my time to developing and refining the structures.

Throughout the process, I constantly switched between Unreal Engine and Blender to compare proportions and make sure the assets worked correctly from the camera perspective. To make this workflow more efficient, I used a plugin called Blender For Unreal Engine, which helped automate the export process and made the transition between Blender and Unreal Engine much faster and easier.

### UV Unwrapping

Since the environment contained many different assets, I had to carefully manage the UV unwrapping process for each object. During this process, I used some helpful Blender plugins such as ZenUV and RetopoFlow, which greatly improved my workflow. They allowed me to unwrap assets more efficiently, create cleaner topology, and maintain consistent texel density across the entire scene. For example, for the pine trees, I started by sculpting a high-poly base in ZBrush to achieve the main shapes and organic details. After that, I used RetopoFlow in Blender to create a cleaner low-poly version suitable for real-time rendering, and then I used ZenUV to unwrap the mesh.

Once the retopology and UVs were completed, I baked the maps and moved to Substance 3D Painter, where I created the final textures and refined the surface details. For the pine foliage, I focused on creating an effective shape rather than unnecessary detail. Since these trees were placed quite far from the player camera, creating highly detailed leaves would not have provided a visible improvement in the final image. Instead, I used simple sphere-based shapes to create a stylized representation of pine foliage, baked the details in Substance 3D Painter, and added painted color gradients to enhance volume and readability.

After that, I manually assembled the different elements, combining the trunk, branches, and foliage to create the final tree assets while maintaining a good balance between visual quality and performance.

For the other types of trees and bushes, I used a free open-source tool called TreeIt. This allowed me to generate additional vegetation assets more efficiently, saving production time and allowing me to focus more on the overall composition and artistic direction of the environment.

For the foliage shader, I used a technique from Viktoriia Zavhorodnia's Unreal Engine foliage shader tutorial, which helped me achieve a more stylized and dynamic vegetation look!

### Texturing

I think one of the most important aspects of creating a stylized environment is the texturing process. Substance 3D Designer makes the workflow much more efficient, especially when creating reusable materials and maintaining consistency across the entire scene. I usually start by building the main texture components in this order: normal, base color, and roughness. For this project, I also created a trim sheet that I could reuse throughout the environment to decorate and add more details to specific areas of the architecture. This is how the nodes look:

During production, there was a lot of back and forth between Substance 3D Designer and Unreal Engine. A texture might look correct inside 3D Designer, but that does not always mean it will work well in the final environment, because the lighting setup, camera angle, and overall composition can completely change the way the material is perceived. This is what came out of 3D Designer:

To achieve a more painterly look, I usually work with custom brush-stroke alphas that mimic the feeling of traditional painting. I combine them with nodes like the Tile Sampler to generate more organic variations and experiment with different patterns.

I often apply this approach both to the Normal map, to create subtle surface details, and to the Base Color, to give the texture a more hand-painted appearance. I also use Roughness variation as an additional artistic tool. By changing the Roughness values, the way light interacts with the surface changes, which can influence the perceived color and create more interesting variations when combined with brush-stroke details, especially on elements like roof tiles.

During the final stages of the environment, I also used decals from Jan Wyss' Alpha Collection on ArtStation to further enhance the painterly feeling of the scene and add additional hand-painted details where needed. For example, on one of the wall materials, I used vertex painting to reveal the plaster underneath and create more variation on the surface. I added small brick details on top to create a stronger sense of depth and layered decals over the plaster to introduce additional color variation, especially in the shadowed areas where these details are more visible and help break up the material.

For the rainy mood, I used a combination of different plugins like EasyFog and also a plugin called SoStylized, which includes pre-built VFX systems. For the clouds, instead, I used another plugin called SkyCard with some custom alpha that I got from an online photo of clouds, so the art direction and the creativity are my main focus, avoiding all the boring technical parts!

### Composition

I usually approach environment composition by dividing the scene into foreground, middle ground, and background. One of the main principles I follow is that the farther an element is from the player, the less detail it needs, so for example, regarding the vegetation, I usually disable shadows for distant objects like trees on the distant mountains. I concentrate the highest contrast, color variation, and visual complexity around the main focal point, which in this case is the largest building.

If I notice that a specific area of the shot becomes too dense with visual information, I usually introduce a fog card to soften the details and improve the overall readability of the composition for the viewer. This helps guide the eye and maintain a clear visual hierarchy. For the mountains in the distance, I generated the terrain using height maps created in World Creator.

It is a very efficient tool because it allows me to quickly create complex natural shapes while maintaining a good level of control over the final result. For the landscape Master Material, I used four paintable layers combined with Virtual Texturing and an RGB Mask on the Grass Texture that I also created in Substance 3D Designer, which gave me more flexibility in blending colors and controlling each layer individually. This allowed me to create more variation and achieve a more natural-looking environment.

One of the most interesting technical aspects of this environment was the implementation of a custom outline shader inside the Post Process Volume.

The effect was driven by the Custom Depth Pass, where I assigned specific values to selected objects to control which assets received the outline effect. I mainly used this technique on foreground elements and on objects with overlapping silhouettes, because it helped improve visual separation and create more depth between different layers of the scene while keeping the effect controlled and intentional.

### Conclusion

The entire project took approximately one and a half months to complete, from the initial blockout to the final presentation. However, it is worth mentioning that I reused some foliage assets from previous projects, such as the ivy, as well as a few trim sheets for simpler elements like wooden props. This allowed me to optimize the production time and dedicate more effort to the unique aspects of the environment, including the architecture, composition, and overall art direction.

The biggest challenge was the texturing phase. Since the environment contained a large number of assets, every material needed to feel cohesive and work well together to maintain a consistent stylized look. One of the biggest lessons I learned from this project was the importance of staying organized. Maintaining a clear folder structure, using well-organized subfolders, and establishing a solid workflow from the beginning were essential for managing a complex environment with a large number of assets efficiently.

If I could give one piece of advice to someone just starting, it would be to take things one step at a time and stay as organized as possible. Large environments can quickly become overwhelming if your assets and files are not properly structured. I also recommend thinking of every asset as a long-term investment. Well-made materials, trim sheets, foliage, and modular pieces can often be reused in future projects, helping you work more efficiently while maintaining consistent quality across your portfolio. Best of luck to everyone!
