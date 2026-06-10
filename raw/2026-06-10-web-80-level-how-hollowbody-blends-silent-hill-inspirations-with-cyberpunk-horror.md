---
source: "https://80.lv/articles/how-hollowbody-blends-silent-hill-inspirations-with-cyberpunk-horror"
title: "How Hollowbody Blends Silent Hill Inspirations with Cyberpunk Horror"
author: "Headware Games Interviewed by David Jagneaux 04 June 2026"
date_published: "2026-06-04"
date_clipped: "2026-06-10"
category: "Game Development / Unity"
source_type: "web"
---

# How Hollowbody Blends Silent Hill Inspirations with Cyberpunk Horror

Source: https://80.lv/articles/how-hollowbody-blends-silent-hill-inspirations-with-cyberpunk-horror

0

Save

Copy Link

Share

[Headware Games](/author/headware-games)

Interviewed by

[David Jagneaux](/author/david-jagneaux)

04 June 2026

Headware Games discusses Hollowbody's retro-inspired art pipeline, PS2-era visual constraints, Unity-based development, atmospheric lighting workflows, and the challenges of building a modern survival horror game as a solo developer.

Over the past several years, a new wave of indie horror games has emerged with a surprisingly specific source of inspiration: the survival horror classics of the PlayStation 2 era like Silent Hill 2. While modern horror often gravitates toward photorealism, cinematic presentation, and large-scale production values, titles like Signalis, Crow Country, Heartworm, and Hollowbody have found success by embracing the deliberate pacing, environmental storytelling, and oppressive atmosphere that defined an earlier generation of horror games.

Among them, Hollowbody stands out for its distinctive blend of classic survival horror design and futuristic technoir worldbuilding. Developed largely by solo creator **Nathan Hamley of [Headware Games](https://www.headwaregames.com/)**, the game draws inspiration from genre staples such as Silent Hill 2 and Resident Evil while placing players inside a decaying cyberpunk city filled with abandoned streets, retro-futuristic technology, and psychological unease.

In this interview, Hamley discusses the core design pillars that guided Hollowbody's development, such as intentionally limiting the visual pipeline to diffuse textures and low-poly assets inspired by PlayStation 2-era hardware and recreating the grounded environmental layouts that made classic survival horror locations feel believable and unsettling.

**Hollwbody** is available now on Steam with a "Very Positive" user review average and out on PlayStation 5 and Xbox Series X|S on **June 5, 2026.**

![]()

![zoom-icon](https://cdn.80.lv/static/icons/zoom-icon.svg)

**Hollowbody has been praised for capturing the feel of classic PS2-era survival horror while still feeling modern and distinct. What were the core design pillars guiding the project from the beginning?**

**Nathan Hamley, Founder of Headware Games:** There are a few core aspects of design that I wanted to stick to, not only for aesthetic reasons but also to keep scope manageable when it came to the art pipeline. As most folks are aware, the PS2 did not have support for any kind of normal map or PBR-based shader workflow out of the box; the vast majority of games used only diffuse texture maps.

This itself saved a huge amount of time as I was able to source most of my textures from photographs I had taken myself or sourced from sites like Textures.com. I also tried to keep all of my models as low poly as possible, adding geometric detail only on hero assets such as those used for puzzles or inventory items. Outside of visuals, I also wanted to stick to a similar grounded level design and layout as seen in the Silent Hill games. In those games, environments tended to lean more towards real-world layouts than typical video game map structure. This came with its own set of challenges, and I think it is something I would strive to refine moving forward with future projects.

**Many players compare the game to classics like Silent Hill and Resident Evil, but with a technoir cyberpunk edge. How did you approach balancing nostalgia with creating an original identity?**

**Nathan Hamley:** This was a fine line to tread, and I still get the occasional comment about the game being too derivative of the Silent Hill games, so I’m not sure if I really found the perfect balance! It’s a double-edged sword because you tend to get two types of players: those who get a kick out of picking up on the subtle throwbacks and those who see them as an opportunity to lambast the game when they’re not gelling with other aspects.

Steam players can be brutal, man! So yeah, with these homages to other popular titles, it's a bit like playing with fire. In retrospect, I think Hollowbody mostly got it right. I went into the project knowing that the game telling its own unique story in a very different (futuristic) setting would differentiate it enough, I think I pulled that off. There are some aspects of design (combat in particular) that I was too focused on trying to replicate and could cause frustrations for the newer generations of players who didn’t grow up with things like tank controls.

![]()

![zoom-icon](https://cdn.80.lv/static/icons/zoom-icon.svg)

**From an art direction standpoint, what specifically defines the visual language of Hollowbody—particularly its mix of grimy realism, PS2-inspired aesthetics, and modern rendering techniques?**

**Nathan Hamley:** I pulled a lot of references from urban decay photography, picking up and getting inspired by various books from urban exploration photographers. Alongside that, there was a lot of ‘cassette-futurism’ or ‘retro futurism’ stuff in my mood board, the sort of computer terminals you’d see in older 70s and 80s science fiction films.

These are quite often shown in clean, bright environments, and I thought it would be fun to juxtapose that with settings where they have been left to weather or gather dust in Hollowbody, surrounded by messy, dilapidated homes and streets. Speaking of the streets, this was something of a core visual in Hollowbody. I really wanted to explore environments that felt somewhat familiar, places we could relate to, and in turn help make the horror aspects hit deeper. That was the main reason the game ended up taking place in a long-abandoned city.

**The game uses classic survival horror conventions like fixed camera angles and deliberate pacing. How did those choices influence your level design and environmental storytelling workflows?**

**Nathan Hamley:** As I touched on in an earlier question, this is something that had quite a big impact on level design as I was trying to keep the locations mostly accurate to their real-life counterparts. It did pose some interesting challenges, as in the real world, layouts are mostly designed to be functional and make optimised use of space, not necessarily to guide someone through those layouts.

To give an example of where this caused a bit of friction to gameplay design, I modelled the residential streets to similar scale and structure as they are here in the UK but when it came to testing I found that the streets were far too wide and long to accommodate the sort of gameplay seen in survival horror games (typically very cramped), my fix ended up being a bit of a band-aid solution where I added various road blocks and rusted cars to funnel the player and force them to confront enemies. It’s all a learning process for me and something I’ll take on board for future projects.

![]()

![zoom-icon](https://cdn.80.lv/static/icons/zoom-icon.svg)

**From a technical standpoint, what engine and core technologies are powering Hollowbody, and what made them the right fit for this kind of retro-inspired horror experience?**

**Nathan Hamley:** The game uses the Unity engine. This was my second 3D game and the second time I had used Unity to develop something. As with most of my projects, I was still learning a lot about the tools as I went. Unity’s built-in renderer lets you get away with using a lot of dynamic lights, and thanks to that, I was able to create Hollowbody without having to bake big lightmaps or worry too much about performance.

This is one of many benefits of going with a retro-inspired look. I also used [PlayMaker](https://assetstore.unity.com/packages/tools/visual-scripting/playmaker-368), which is a visual scripting solution for Unity. This helped out a great deal as I am more of an artist than a programmer.

**One of the game’s strengths is atmosphere and lighting. What does your lighting workflow look like, and how do you achieve that oppressive, moody tone while still maintaining gameplay readability?**

**Nathan Hamley:** As mentioned, I’m able to get away with using quite a lot of real-time lights in Unity without it having too much of an impact on performance. I would typically light my environments with non-shadow-casting lights tinted to various subtle colours to act as fill lights, then use some key lights to add visual focal points and emphasise interactable areas.

Hollowbody uses a very heavy post-process colour grading, so a lot of my lighting work was done whilst that post-process was active. It’s an iterative process, and I found myself tweaking lighting right up until the game’s release.

![]()

![zoom-icon](https://cdn.80.lv/static/icons/zoom-icon.svg)

**Hollowbody has become part of a broader resurgence of retro survival horror games alongside titles like Signalis, Heartworm, and Crow Country. Why do you think this style of horror has resonated so strongly with modern audiences?**

**Nathan Hamley:** Honestly, I think there was simply an audience for traditional survival horror that had been long neglected by mainstream big studio projects. Players who enjoy these games aren’t desperate for visual fidelity or huge game worlds but just really enjoy the design staples of the genre.

I myself am, of course, one of those players and have been spoiled rotten by the breadth of amazing indie titles filling that niche. It’s a great time to be a traditional survival horror fan!

**As a largely solo-developed project, how did you structure your production pipeline across art, design, writing, and technical implementation?**

**Nathan Hamley:** Structure? What’s that? :) No, but honestly, I am a very chaotic designer, and things are constantly changing throughout development. I think this is one of the biggest strengths of being a solo (or small team) developer: you have the option to pivot and sidestep things that could otherwise be huge roadblocks or timesinks for the project.

I typically go into the project with a rough outline for the narrative and locations I want to feature; a lot of the rest of the process is ‘feeling it out’ and adapting design as I go. This does, of course, mean making a lot of sacrifices, and I think most of Hollowbody’s shortcomings aren’t necessarily things I didn’t consider but stuff that was too demanding for a solo developer to pull off.

![]()

![zoom-icon](https://cdn.80.lv/static/icons/zoom-icon.svg)

**Sound design plays a huge role in survival horror. How did you approach audio and music to reinforce tension and psychological unease throughout the experience?**

**Nathan Hamley:** For sound and music, I am again leveraging the benefits of working on these projects solo. I am able to switch my creative discipline whenever inspiration hits me and chase that. I often found myself working on a scene or environment and mulling over in my head what sort of mood I was looking to achieve, then after some time I could jump on my MIDI keyboard and start throwing around various samples and VST synths until I had a bed of ‘music’ that fitted how I was feeling whilst creating the art.

Horror is a bit easier in this sense, as more often than not, the scene benefits from beds of atmospheric sounds rather than melody-driven songs. I used [Omnisphere 3 by Spectrasonic](https://www.spectrasonics.net/products/omnisphere/overview.php), which has an insane amount of choice when it comes to synths and samples. It also features a few sample packs that were used on survival horror classics like Silent Hill and Resident Evil, etc.

**Looking back, what were the biggest lessons learned while developing Hollowbody, and how has the response to the game influenced your thinking about future projects?**

**Nathan Hamley:** Above all else, I think my biggest lesson was that I needed to dedicate a lot more time to improving my approach to ‘game feel’ and ensuring that the code and systems supporting stuff like player movement and combat were a lot more battle-tested. This seemed to be the biggest sticking point for players who didn’t gel with the game. I’m very much an art guy, as those aspects (art, writing, music, etc) are where I’m most confident, so moving forward I’ve been spending a lot more time in the greybox stage and refining how my game feels to play before any of the atmosphere or art assets.

![]()

![zoom-icon](https://cdn.80.lv/static/icons/zoom-icon.svg)

## **Nathan Hamley of [Headware Games](https://www.headwaregames.com/), Developer of Hollowbody**

### Interview conducted by [David Jagneaux](https://www.linkedin.com/in/davidjagneaux/ "https://www.linkedin.com/in/davidjagneaux/")

# Subscribe to 80 Level Newsletters

Latest news, hand-picked articles, and updates

[Privacy Policy](/privacy-policy)[Terms of use](/terms-of-use)

![subscribe mail image](https://cdn.80.lv/static/images/subscribe/subscribe-mail.svg)

Keep reading

More developer interviews

- [How an Indie Studio Portrayed Alien Abductions and Depression in a Horror Game](/articles/how-an-indie-studio-portrayed-alien-abductions-and-depression-in-a-horror-game)
- [Creating a Narrative-Driven First-Person Psychological Horror Game Set on an Isolated British Island](/articles/creating-a-narrative-driven-first-person-psychological-horror-game-set-on-an-isolated-british-island)
- [Wych Elm Co-Founder on Creating the Survival Horror Metroidvania Silver Pines](/articles/wych-elm-co-founder-on-creating-the-survival-horror-metroidvania-silver-pines)

Built for Creators. Read by the Best

[Partner with 80 Level](https://80level.typeform.com/to/B8udrWL5)

### Comments

#### 0

![arrow](https://cdn.80.lv/static/icons/article/arrow-right-plain.svg)

Leave Comment

Built for Creators. Read by the Best

[Partner with 80 Level](https://80level.typeform.com/to/B8udrWL5)
