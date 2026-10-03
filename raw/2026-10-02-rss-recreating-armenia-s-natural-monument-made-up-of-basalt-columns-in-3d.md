---
source: "https://80.lv/articles/recreating-armenia-s-natural-monument-made-up-of-basalt-columns-in-3d/"
title: "Recreating Armenia's Natural Monument Made up of Basalt Columns in 3D"
author: "Artur Artinian"
date_published: "2026-10-02"
date_clipped: "2026-10-02"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Recreating Armenia's Natural Monument Made up of Basalt Columns in 3D

# Recreating Armenia's Natural Monument Made up of Basalt Columns in 3D

Artur Artinian explains how the iconic organ-shaped natural monument from his homeland inspired his latest project, Sonata of the Stones.

### Introduction

My name is Artur Artinian. I'm a 3D Artist working primarily in real-time engines like Unreal Engine, creating environments and digital sets for cinematics, films, and games.

Since [my last interview](https://80.lv/articles/creating-a-vibrant-scene-inspired-by-armenian-culture-with-ue5-maya), when I was still a student studying at Gnomon, I've graduated and had the opportunity to work on various AAA game cinematics, digital sets for film, and commercial projects with companies like EDGLRD, AGBO, and Workproduct as both an Environment and a Lighting Artist. It's really been a dream to make that transition from school and use all the knowledge I gained in my classes at Gnomon while working alongside amazing people in a professional pipeline. I'm incredibly grateful for the opportunities I got and the people I met along the way.

Outside of professional work, I've continued to put my free time into personal projects. One of those projects is Sonata of the Stones, which I'm excited to talk about here.

### Getting Started with Sonata of the Stones

The inspiration for this environment came from my visit to the Symphony of the Stones natural monument located in Garni, Armenia. When I was a kid, I remember seeing the structure in person and being shocked at how something like this was possible, purely as a result of nature doing its thing.

The colossal structure of these pipe-organ-like basalt columns towering over one another was a visual that’s stuck with me ever since, and it felt like it was finally the perfect time to use the awe-inspiring site as a source of visual inspiration.

Upon finishing my previous project, [Path of the Pomegranates](https://80.lv/articles/creating-a-vibrant-scene-inspired-by-armenian-culture-with-ue5-maya), I had the itch to build another space that would fit into the same world as the one presented there. I wanted to add on and build another location that fits right into this same visual universe, inspired by Armenian architecture, mythology, and visual identities, with a dark fantasy twist. My goal for this project was to create something eye-catching and dramatic, while being resourceful by using a very small number of unique assets to create the whole thing.

### Concepts & References

I try to approach my environments with the idea that this place existed long before the viewer ever stumbled upon it. There is a history behind this place that we don't fully understand, and we're only being shown the remnants of it. I think that sense of an unknown past makes a space feel much larger than what we see on screen. It’s as if the environment has succumbed to the passage of time, but it still stands and wears its age proudly.

This philosophy became the foundation for Sonata of the Stones, with reference gathering playing a huge role in shaping the project. I tried to get many images of basalt formations from the Garni region in Armenia, and basalt column formations in general. This was a crucial step because these basalt columns are formed in a very specific way; I had to look carefully at the way the stones were harmonizing with each other because arranging them in the engine could very easily fall into the 'visual noise' category if I failed to capture how these basalt stones blended into each other naturally.

For the blockout, I tried to keep the shapes as simple as possible. At this point, I was testing how the rock silhouettes were looking and focusing on the big forms, checking how the pillars would interact with one another. I created 4 separate meshes that used the same base mesh: one singular pillar, another mesh that had a group of 3 pillars together, and one more that had 4 pillars at different scales and sizes.

Since the whole environment revolves around these repeating vertical forms, getting their proportions and rhythm right was the most important part; there needed to be this sense of repetition since that's what made the original monument I was referencing so striking, but I also had to be careful not to make the scene seem like there were just a few assets duplicated dozens of times.

I would hand-place these assets I made to get an idea of the shape I was trying to go for in the structure and create a composition based on that. Because I had singular rock basalt assets along with their grouped variations, it allowed me to art-direct in-engine very quickly to get a taste of what I had in mind for the scene.

A big challenge of this project was that I wanted to create a very limited amount of assets; not only to save time, but also to try to train my creative muscles and see how far I could push these few assets to create a visually striking space. It was a constraint I was designing around that became its defining property. It forced me to be more intentional about how I used them, when to use bigger pillars, medium-sized pillars, small-sized pillars, and how they would overlap.

I sculpted only one pillar. Since the pillar has six faces, I sculpted a unique surface on each side so that I could rotate it in the environment. This allowed a single asset to give me six distinct faces to work with, saving me time while giving me variety with one single mesh since I would be rotating the pillars around.

The differences between each face also needed to be subtle enough that obvious repeating patterns would not show up throughout the structure. This helped the repetition feel natural and intentional, just like in the formations I was referencing.

For smaller assets like the candles, I just made simple ZBrush sculpts that were then decimated to a low poly count. The high poly of the sculpt was baked onto these decimated meshes to bring all that detail back while retaining a low polygon count. The same was done for the basalt rock columns.

### Texturing

For texturing, I had to find ways to bring a sense of variety because so much of the environment used the same stone texture for its main structure. The stones were textured using a tileable material I created in Substance 3D Designer. I knew I needed to introduce some variation across the columns, so I knew that a simple flat tiling texture wouldn't be enough.

To achieve this, I created an RGB mask for the stone texture in Substance 3D Painter, which allowed me to control and introduce different variations across the surface.

Each color value has its own generator in Substance 3D Painter – for example, R is edgewear, G is a dirt generator, and B is some surface variation masks that I then bring into the engine. This allows me to introduce texture variation to the columns, giving edgewear, surface variety, and dirt buildup that would help ground the stones and give that extra bit of detail. Below is a video showing the RGB material shader that I created in Unreal Engine and how it was applied to the stone.

The challenge wasn't necessarily creating a huge library of different surfaces, but rather figuring out how much variation I could get out of the same material without losing the visual identity of the stones. I wanted the material to support the sculpt of the stone, so the RGB mask of the texture was here to just introduce a smaller breakup.

If you look closely, you can see hints of gold paint spreading near the golden sun emblem and the environment around it. This was both an artistic and narrative decision to break up the uniformity of the rock texture that also ties back to the thematic elements; these bits of gold were created with decals I made that were then dressed on top of the stone.

It introduced varying roughness and specularity while also adding pops of color that tied in with the grey of the stones without overpowering the rest of the color palette or overall mood of the scene, introducing some extra roughness variation as well.

### Assembling the Scene

I wasn't trying to build a perfectly realistic geological formation; I was much more interested in creating a striking image that felt grounded in reality yet fantastical. With this in mind, the composition organically came to be through some trial and error. I wanted the environment to feel grandiose, so I knew the camera had to be placed low to the floor, in addition to a low focal length, which helped sell the scale of the structure.

I had a variety of iterations in the blockout process, which is where I constantly refined my composition; for example, how the overall shape of the columns read altogether. I realized there needed to be a split in the middle of the structure to give the composition some balance and create visual interest.

Doing so created much-needed asymmetry in the structure, which I personally feel like makes the structure look more natural and creates some breathing space in the composition. With one side being heavier and slightly taller, and the other one being thinner, I achieved an interesting offset between the two sides of the column structure, with an open split in the middle to really draw our eye to the golden sun emblem and the flame gate that burns underneath it.

For the breakup, aside from the ones I mentioned for the main rock structure, I tried to use the candles in the foreground and the ash-sand dunes for the floor to give visual variety. These visuals also tied into the theme of the environment, reinforcing that sense of light and holiness. The candles worked alongside the glow of the gate, creating smaller points of interest that guide the viewer's eye throughout the

scene without overpowering the main focal point.

### Lighting

Lighting is always one of the biggest focal points in my environments. It's usually one of the first things I think about when starting a project. With Sonata of the Stones, there was this idea of a marriage between light and shadow, and how the two need each other to create an impact. This was the theme that was at the forefront of my project as I was developing the original concept and reference. The concept is that this light carries more significance when it's surrounded by darkness.

I feel like I tend to gravitate a bit toward darker-toned environments, but I always have a point where light breaks through the darkness and illuminates the surroundings. It gives the light an emotional quality and creates drama and a story that sets the scene, pulling viewers in rather than just being there purely for technical reasons.

For the light shining through the crack, I used a simple plane with a scrolling emissive texture that glows and gives the effect of an otherworldly light being cast into the environment. The material was simple enough, with just a noise going along a coordinate.

To top it off, I used Light Shafts to create the God ray effect, giving the light a sense of holiness, as if the space itself had become a place of liturgy. Since the bounce light from the emissive gate wasn't strong enough on its own, I added additional Spot and Point lights to push that warm orange glow across the stone and the sandy ash beneath it.

I went for a more contrasty approach with lighting, where one side of the structure was more engulfed in shadow compared to the other, which really helped create tone and add drama to the environment and set up a visual divide and separation between the two column-like structures.

### Creative Challenges

One of the main challenges was the limitation I had set for myself with the unique asset count. As I mentioned earlier, there are only around five truly unique meshes making up the environment. It was a fun challenge, but it also meant I couldn't solve every visual problem by simply creating another asset. I had to constantly find new ways to reuse what I already had and make it feel fresh through composition, scale, rotation, lighting, and set dressing.

That brings up the issue with repetitiveness too; I had to find ways to subtly break up the repetition of the assets, including the roughness and general color of the main structure. One way I did this was by trying to think about how I could narratively introduce some elements of color to break up all the overpowering grey of the rocks. So the huge lesson for me that I took away from this environment was that you can indeed create an interesting image with a very small amount of assets if you use them correctly; not every visual challenge has to be solved by creating a whole new asset, and in certain scenarios, cleverly reusing assets can really help you focus on the bigger picture.

Since the environment, specifically the rocks, resembled the pipes of a church organ, I wanted to amplify the visual resemblance between the rock formations and the pipes of a church organ, so I knew I wanted to have a custom piece of music created for it. With the title of the piece being called Sonata of the Stones, it only felt right to do so. I was very lucky to work with the talented composer [Grigor Abgaryan](https://www.grigorabgaryan.com), who created the original score for the environment. I think the music he created really tied the whole piece together and gave the world a greater sense of weight, capturing the age of the stones as if echoes were still trapped within them.

### Advice for Beginners

My advice for beginner artists would be to lean into your originality as much as possible; don't be afraid to dig deep into your interests and what makes you unique, and share that with the world. It's really easy when you're starting to look at successful artists and feel like you need to make the same kind of art, environments, or match someone's style.

We can all see the same painting or listen to the same song, yet what it sparks in each of us can be completely different. Those individual interpretations can lead to entirely different and original concepts in your own work, which will separate you from others. This is even more important now than ever before with the rise of AI.

Of course, learn all the technical aspects and fundamentals needed; these are extremely important and are constantly changing with new tools coming out. But don't forget why people learn these things to begin with – to tell their stories, to share their ideas, and to convey emotions to the audience. Technical proficiency is increasingly accessible, so having a personal taste, cultural influences, ideas, and perspective becomes even more valuable.
