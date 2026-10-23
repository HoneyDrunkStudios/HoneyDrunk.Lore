---
source: "https://80.lv/articles/how-to-make-3d-look-like-a-stylized-painting-with-shaders-in-houdini-c4d"
title: "How to Make 3D Look Like a Stylized Painting with Shaders in Houdini & C4D"
author: "Theodore Daley"
date_published: "2026-10-21"
date_clipped: "2026-10-21"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

[Theodore Daley](https://80.lv/author/theodore-daley)

3D Artist

21 October 2026

# How to Make 3D Look Like a Stylized Painting with Shaders in Houdini & C4D

[#Interviews](https://80.lv/articles/interview)[#Marketplace](https://80.lv/articles/marketplace)[#3D Art](https://80.lv/articles/3d-art)[#Houdini](https://80.lv/articles/houdini)[#Cinema 4D](https://80.lv/articles/c4d)[#Shaders](https://80.lv/articles/shaders)

If you click on the links in this post and make a purchase we may receive a commission. Please read our [disclaimer.](https://80.lv/disclaimer)

YMA Painterly is a collection of 12 shaders that add a stylized and painterly look to your 3D artwork in Cinema 4D and Houdini. The developer, Theo Daley, discussed his workflow and explained how he created some of his example setups.

Theo Daley is an artist who shares impressive tutorials and shaders for the 3D community as part of You and Me Academy (YMA) on a [YouTube channel](http://www.youtube.com/@YouAndMeAcademy) with tutorials on motion graphics. Check out some of Theo's work we featured in the past, including a [collection of 100 toon and anime-style shaders](https://80.lv/articles/craft-vibrant-toon-animations-with-this-shader-collection-for-redshift), a [drifting car animation made with those toon shaders](https://80.lv/articles/awesome-drifting-animation-clad-in-custom-toon-shaders-set-up-with-redshift), and a [1:1 shot-for-shot of the Akira anime scene but in the manga's style](https://80.lv/articles/this-akira-animation-looks-as-if-it-was-taken-from-manga.).

YMA Painterly collection is available on [Gumroad](https://youmeacademy.gumroad.com/): for [C4D and Redshift](https://youmeacademy.gumroad.com/l/ofhwqw), for [HOUDINI and Redshift](https://youmeacademy.gumroad.com/l/cpjsly), and for [C4D and Octane](https://youmeacademy.gumroad.com/l/oorva).

### Introduction

Professionally, I am a two-time Emmy-nominated motion graphics art director/designer who has worked on game cinematics such as God of War 3 and God of War: Ascension, where focusing on making 3D look nothing like the original was vital. Similarly, on an ESPN Eurocup sports package in 2016, we took the traditional 3D package and turned it into paint, sketches, and statues, all inspired by France. I always tend to lean more into non-traditional styles with 3D whenever I can, since I come from more of a fine arts background.

### How YMA Painterly Started

Much like YMA Toon Studio was my interest in anime, comics, and manga, YMA Painterly began more as a tool for myself in my own professional work and experiments doing more stylized work. I wanted to be able to paint inside the render and skip multiple steps, if possible, so I could modify normals and set up paint textures directly within my shader.

!

!

At first, it was figuring out how to modify normals for stylized effects, and then working from there; it expanded until I had the features and node flow to allow me to tweak almost like in a compositor, but all in the shader. At one point I had so many nodes I didn’t even know what was going on, so I started grouping, sorting, labeling, and building smaller UIs, turning it into a system with clear areas to modify. I finally felt like I had the right tools to do the work I wanted.

!

!

!

It started with Redshift, but as people kept asking about other options, I began to reach out to the developers of each renderer to make sure the math and nodes were correct, since they all handle it a little differently. As I was improving this system and getting help from devs inside and outside the companies, it kept growing, so there are now complete versions for Redshift, Octane, C4D, and Houdini.

!

!

These are intended for those who love NPR looks and wish they had a set of shaders based on real brushes in render to choose from and immediately see their results. They're also for artists who love experimenting to find new ways to express themselves.

### Features

YMA Painterly is a set of 12 hand-painted shaders that will take in any 3D geometry, paint up to 4 different colors (base + accent colors) based on the brush textures, and most importantly, give you the ability to manipulate the normals strength to add more painterly details, all within Redshift or Octane.

!

!

As each 3D program and renderer is different, I tried my best to work with their preferred workflows. Meaning, in C4D, you have Redshift and Octane versions, and Houdini has a Redshift option (which also works in Solaris).

!

!

!

My biggest goal was to create drag, drop, and with one slider, you can go from your regular base geo normals to painterly stylized normals with control over all the colors like a painter would have. Everything has been referenced from real world art styles and brushes and reached out to developers of each renderer to ensure they work properly everywhere.

Some of the key features in the shaders:

- 12 custom-made Preset Painterly Materials
- 12 custom handcrafted 4 K tileable painterly textures
- Control over Base color + Accent colors
- Scale of brushstrokes
- Painterly normals strength control slider. 0 reverts to regular geo
- OpenPBR pipeline

Once installed, you simply drag and drop your preferred paint style onto your model, and either through nodes or the UI, you can easily work while the IPR is running. Think of these as your 12 favorite brush types, each distinct from one another. Since they are each built per DCC, they integrate seamlessly with your standard workflow and nodes – nothing is locked.

### How It Was Created

The main process came from many experiments, readings, and many more conversations with people way smarter than me. Trying my best to study the work that inspired me and break down their process was essential to the shader workflow. Ultimately, I access object-space normals from any 3D model and perform vector math transformations that let me connect the hand-painted textures into that flow.

!

!

Once I had that working properly, it became more about expanding the tool to give me control over every aspect, like a paint palette: splitting and then connecting into 4 color parameters, adding a contrast controller, a slider so it can be just the base or all the colors together in any amount; scale ratios of the brush textures and controls for how much or how little the hand-painted textures will influence the surface of a model. Even the ability to push more colors into the specular, so instead of just white, you can get all the colors you selected earlier.

!

The textures were all hand-painted using tools such as Rebelle and Photoshop, along with Substance 3D Designer, to create the 4K tileable textures.

!

I then streamlined the node flow as much as possible with color coding, custom groups, and UI so users can immediately change colors, the scale of the brushstrokes, and the painterly normals with a few clicks. Everything is exposed, but anything nonessential is not highlighted.

!

!

!

For each version, I reached out to developers and experts for each renderer to ensure seamless integration. They have also been tested on projects and render farms, so whether you are a solo artist or a large studio, YMA Painterly fits into your workflow.

### Conclusion

You can get the shader collection on the artist's [Gumroad](https://youmeacademy.gumroad.com/):

- [YMA Painterly [C4D | Redshift]](https://youmeacademy.gumroad.com/l/ofhwqw)
- [YMA Painterly [HOUDINI | Redshift]](https://youmeacademy.gumroad.com/l/cpjsly)
- [YMA Painterly [C4D | Octane]](https://youmeacademy.gumroad.com/l/oorva)

   
Also, see some more of Theo's work [here](https://www.instagram.com/theodoredaley_/).

### [Theodore Daley](https://www.theodoredaley.com/), 3D Artist
