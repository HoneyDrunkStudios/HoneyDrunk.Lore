---
source: "https://80.lv/articles/creating-a-thriller-animated-series-with-hand-drawn-textures-in-blender"
title: "Creating a Thriller Animated Series with Hand-Drawn Textures in Blender"
author: "BONI IS SCARED; interviewed by Amber Rutherford"
date_published: "2026-10-12"
date_clipped: "2026-10-18"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Creating a Thriller Animated Series with Hand-Drawn Textures in Blender

### Introduction

**Boris:** We jokingly refer to the approach to this project as a "guerrilla production". Starting work on the thing, I knew I could ask Nico to help me, and that's it. I did not know anyone. When we proceeded with the initial idea and made the first storyboards, the approach was that if we encountered an issue, we tried to solve it, and if we couldn't do it ourselves, we solved it by finding someone somewhere to help us with it. Step by step, with this approach, we grew into a collective of around 15 artists around the globe. All of them, very generously, agreed to support this project and helped us along the way with very different kinds of things. Thus, this is the first piece that we created as a team.   
  
When scheduling and planning the production, we had a clear understanding that Nico, having vast experience in the animation industry, could invite people he knew to help us. But that privilege covered only animators.   
  
Since I did not know anyone, if we needed help with anything else, I would go on Instagram and check my "saved" stuff to see if maybe I saved a sculptor, a sound designer, or a concept artist I like. If not, sometimes I just scrolled reels or the For You page until I saw someone I'd like to ask to help us. Depending on what we needed at the time.

This way, we got to know and work with amazingly proficient and talented artists around the globe, who worked on countless big, cool-sounding projects. We have credits in the descriptions, so if you want to learn more about the people behind it, [check it out](https://www.youtube.com/watch?v=FaQTVHGIsMo).

### EUTHANAZIES

I pitched the thing to Nico, I think, in September or October of 2024, so we started working on it around that time. Nico and I were our own producers, so we tried to approach everything as programmatically as we could.

I believe a person can successfully impersonate proficiency in most art fields on a limited scale if they're willing to invest enough time in studying, redoing the work, and coming up with sometimes weird approaches until it looks like they know what they're doing. In cases where the technical bar is set too high (read: 3D sculpting or rigging), you can find someone who will help you. If, of course, they find interest in what you do.  
  
The plan was to try our best to come up with how we could tackle things we are not experts in or have never done before, and if we understand that we can not solve it, ask for help. I think this approach made the whole production take as long as it took, but at the same time, made it financially feasible to finish, since a lot of the things one usually would need a budget for, we learned how to do on the go. Not well enough to be experts, of course, but well enough to make it work on this particular occasion.  
  
We started with the storyboard (which I had never done before), then did the animatic (which we had never done before), and so on. Step by step.  
  
The animatic is actually a good example of such an approach. I am not good at gesture drawing and very bad with perspective and such. I started drawing at the end of 2021, only 3 years prior. I knew I would not be able to draw characters in perspective properly and at an appropriate pace. So what we came up with was that we built 3D spaces, put in 3D heads, and animated them a bit to have a reference for each shot. Then, I went in and, having this reference, drew the characters above, adding emotions and expressions. So everything is in perspective, and the gesture is there, but it did not take me forever to painfully, not having any fine arts education prior, draw each shot for weeks until it looks at least "bearable."

#### Plot & Themes

**Boris:** I came up with the general idea for the series in July 2024. At the time, I was looking into Fritz Lang's work as part of my broader research into German anti-Nazi artists. I started by revisiting the big one, Metropolis. To be honest, I am not a fan of the film. But the idea of a dark, gothic, and highly stylized industrial authoritarian "city" really stuck with me. In some way, it came not from the film itself, but from my own impression of what it could be if done now and in animation. 

There are a lot of themes and opinions in EUTHANAZIES, which I find very important to convey. But I really wish the viewer would find them on their own, if we have a chance to actually produce it.

#### Visual Language

When we came to actually making the trailer, we did not have any references or inspirations from the animation field. I had a Pinterest board with weird photos, a bunch of scary, weird images, that we could not use as a direct inspiration for the visuals. Forests, fog, buildings, body bags, masks, people.

So, working on every bit, I took as a base things that I already knew from both 2D and 3D fields and experimented with them. And then, at some point in creating an asset, environment, or such, I looked at my collection of weird images, and if I could say, "I guess it's there," it meant that the visual language was at least remotely where I wanted it to be. And if not, Ctrl+A -> Shift+Delete -> start over.

At the same time, the whole trailer was produced without any budget, so we could not do whatever we wanted. It's always a compromise between what you would like it to be and what you are actually capable of creating on the scale with your own hands.

### Pipeline, Combining 2D & 3D, Custom Tools

**Nico:** The general idea was to use the best of both worlds. We use 3D characters, rigs, cameras, environments, and animation to establish the movement and composition. From there, we bring in 2D elements to push the look and add details. 3D gives us a solid foundation, and 2D gives us the freedom to exaggerate and stylize the result.

We built most of the project in Blender but also used software like Substance 3D Painter, Marvelous Designer, or Photoshop. The 2D elements were used for a lot more than just adding details on top of the renders. We used hand-drawn textures and normals to help merge the 2D and 3D, as well as smear frames and hand-drawn motion blur. We also wanted to break some of the physical rules of the 3D world. We worked with hand-painted shadows and distorted perspectives, sometimes deforming entire environments to get the composition we wanted.

There were quite a few custom setups to make this practical in production. For example, we made Geometry Nodes setups for the cables and snow. The cable setup in particular saved us a lot of time, since we had to place huge numbers of cables across different scenes. Or we placed whole environments on curves with the curve modifier to deform them.

We also spent quite a bit of time setting up our own Blender pipeline with version control and Kitsu for production tracking and reviews. This was really important because we had artists working from different parts of the world. In animation, we needed a reliable way for artists to publish playblasts, get reviews, and keep different versions of their work without accidentally overwriting or losing anything.

The hardest part of the whole production was probably combining the 3D with the 2D shadows. The artistic decision was the easy part. The difficult part was figuring out how to make it work technically without turning every shot into a huge manual process.

After a lot of testing, we ended up pre-rendering each shot from a static camera without depth of field. We could then draw the shadow masks by hand and reproject them back onto the 3D models. After that, we rendered the shot again from the actual animated camera, this time with depth of field. It sounds a bit complicated, and it actually was a bit complicated. But once we had the process figured out, it was just a matter of persistence.

There was definitely a lot of experimentation involved in the whole process. We weren't trying to make the 2D and 3D follow the same rules. The whole point was to take whatever was useful from each medium and combine them.

### Conclusion

#### What to Expect from the Pilot

**Boris:** A story! Working on the trailer, we thought about it as a "proof of concept." Upon completing the trailer, we created a technical and visual foundation on which we can build an actual world.  
  
The pilot introduces an environment where we can work with complicated things we could not include in the trailer. Writing, voice-acting, actual storytelling. This is what we focus on. If we have the budget, we can focus on improving and taking the visual aspects further, of course. But the story is the most important.

#### Marketing

As you probably can tell, we do not have access to any marketing budget. We are very thankful to people like yourself who are interested in our work and want to talk about it.  
  
All indie animators are different. Everyone has their own backgrounds, their difficulties, and privileges.  
  
I got very lucky with my stuff on Instagram, which led to having a platform that, in theory, can help a lot with the marketing of our campaign. Though not everyone has something like that. So, if you, reader, are trying to figure out how to market as an indie animator, I have no clue. I just post stuff with closed eyes and hope it will work.

#### Advice for Aspiring Developers

I don't consider myself to be in a position to give advice. But I was asked, so here we go.  
  
If you are not from LA or London or whatever art centers there are, if your parents can't afford to pay for your animation school, if you struggle to pay your bills as it is, you are fucked. People say "just be yourself and have fun," but if a person gives such advice and does not proceed with paying for your rent, it's worthless hypocrisy. Making art for a living is a privilege. If you don't have it in the first place, it's not about 'having fun' anymore.   
  
Find what you can realistically do in a situation you are in, no matter how small it will be. Ask people to help you if you know someone who can help you. Try to share the result with people, show it to your friends, post it somewhere. It will fail. It's ok. Find the strength to do it again. And again. And again.

Hope is a prison.

### [BONI IS SCARED](https://www.kickstarter.com/projects/boniisscared/euthanazies-pilot-animatic), Animation Studio

#### Interview conducted by [Amber Rutherford](https://www.linkedin.com/in/allowedcolors/)
