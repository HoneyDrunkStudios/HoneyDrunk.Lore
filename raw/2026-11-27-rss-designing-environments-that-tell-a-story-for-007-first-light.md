---
source: "https://80.lv/articles/designing-environments-that-tell-a-story-for-007-first-light/"
title: "Designing Environments That Tell a Story for 007 First Light"
author: "Thomas Pulluelo"
date_published: "2026-11-27"
date_clipped: "2026-11-27"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Designing Environments That Tell a Story for 007 First Light

[Thomas Pulluelo](https://80.lv/author/thomas-pulluelo)

Senior Level Designer

Interviewed by

[Emma Collins](https://80.lv/author/emma-collins)

27 November 2026

# Designing Environments That Tell a Story for 007 First Light

[#Environment Art](https://80.lv/articles/environment-art)[#Interviews](https://80.lv/articles/interview)[#Video Games](https://80.lv/articles/video-game)[#Game Development](https://80.lv/articles/game-development)

Thomas Pulluelo talked about building ambient environments for a James Bond story, discussed the intricate process of crafting spaces that subtly guide gameplay, and explained how he used IO Interactive's Glacier engine to create detail-rich areas for the game.

### Introduction

Hey there! I'm Thomas Pulluelo, a Senior Level Designer at IO Interactive in Copenhagen. Like many developers, my love for video games is rooted in childhood. I realized early on that I loved creating experiences even more than just playing them, so I started exploring the modding community and experimenting with tools like Hammer, Garry's Mod, and the Far Cry map editors.

I pursued that passion professionally by studying Game Design at Supinfogame in northern France. Right after graduating, I joined Ubisoft Paris as a World Designer on the Ghost Recon franchise, precisely Wildlands and Breakpoint. Working side by side with a senior-level artist, I learned a lot about macro- and micro-level design, world logic, and architecture. I also got to explore level art, terraforming, and Houdini.

I've always loved learning beyond the job, whether through GDC talks, podcasts like Level Design Lobby, or creators like [GameMaker's Toolkit](https://www.youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw), [Peter Field](https://www.youtube.com/channel/UCNdiEYi38vV5BPi3Ryqvy6Q), and [Steve Lee](https://www.youtube.com/channel/UCRT_DdZnWiUryqrOhLL7gyw).

After five years, I joined IO Interactive to work on the 007 project. I quickly realized that IOI is a studio built around designers, and the Glacier engine really reflects that. It's intuitive to pick up, and it makes prototyping and iteration incredibly fast. Honestly, I keep asking if I can take a version home to play around with (still hoping for a yes).

As a Track Lead on three levels: Against the Odds, Uninvited, and Knightfall, I held creative and technical ownership from initial narrative sketches through to ship, leading multidisciplinary teams across every production gate and deadline.

### Uninvited

When I joined the project, my role was to support the mission on layout creation, implement gameplay, and prototype ideas to highlight story beats. The first thing I made was the MI6 apartment, where Bond stays with the other recruits.

Shortly after, most of the core loops and game mechanics started to click, and the studio decided to work toward a Vertical Slice (VS) prototype. For anyone not familiar with the term, it is a condensed version of the experience that combines every final-quality layer (such as gameplay mechanics, art, audio, UI, story, etc.) to show how the finished product will look, sound, and play. That's the moment I stepped up and took over Uninvited. I was in charge of going through each segment of the level and elevating the experience to meet the VS expectations.

The idea was to create a game level that showcases the IOI DNA as well as the James Bond fantasy and tone we all have enjoyed. The goal was clear: the level needed to show how we can tell a James Bond story, while supporting player agency and a creative approach, meaning they could solve any situation in multiple ways.

We also wanted to prove that a level could go from linear segments to wide-open ones seamlessly without breaking the intensity curve. This mission had a lot of different versions and went through many iterations. Ultimately, it was used as a guiding anchor for what the 007 First Light game structure is today.

### Initial Layout

For context, Uninvited was the very first mission IOI worked on during the 007 project. It was used as a space to prototype ideas and game mechanics, while also iterating on a level structure that would fit IOI's vision for a story-driven game.

Once I took over, I had to make sure each space felt different and highlighted the proper gameplay systems. I started by writing down all the intentions, then I slowly updated the level layout to enhance navigation and define landmarks. Another important thing was to ensure scripted events and important story beats would feel seamless, always experienced from Bond's perspective.

### Crafting the Gameplay

When each segment was defined, I was able to add the proper gameplay set pieces, dialogue, social interactions, trespassing volumes, layout opportunities, etc. I spent a lot of time playing (alone or with other devs) to make sure each problem was explained clearly, along with ways to solve it.

Most of the spaces went through a lot of iterations; I think the Courtyard area was the one that I changed the most. The main challenge was to ensure it shows the creative approach in the best way, all that while still iterating on combat and AI systems at the same time. It became a real scientific lab at some point.

However, the beauty of Glacier is that you can work while the game is playing. Meaning you can update the scene as you go, and the systems around will update accordingly. Is any NPC animation incorrect? Is the distraction set piece placed too far? Should the door be locked instead to create more challenge? Do you want to add another desk for cover? You can do all that without stopping the game engine.

### Gameplay Systems & Scripted Events

Glacier requires level designers to have scripting knowledge. Most of it is done through visual scripting entities (nodes, if you prefer), and anything more complex can be requested from gameplay programmers.

I was able to create a first version of any set piece I had in mind and test it in-game right away. This allowed me to quickly test and iterate multiple ideas to find the ones that worked best with the space I was building. We could also reuse some of the Hitman content to support our designs, which led to a few funny prototypes and a bunch of very polished ones. Once the setpiece gets approved, we send it through a proper creation pipeline where each discipline will contribute to make it final.

Gameplay systems and scripted events are made differently since they require collaboration between multiple departments. Big scripted events like the crane sequence/sniper chase are a group effort, driven by the Tech Art and Tech Design department, while Level Design has more of a supporting role. We make sure the experience stays stable and connects properly.

Any combat spaces like the Exhibition room are driven by level design and supported by the combat team. Together, we talk about archetypes, combat configurations, NPC behaviour, defend areas, and more. All that to make sure I have the necessary tools to create the best combat encounter possible, supporting the mission story beat.

On the other hand, systemic spaces like the Gala or the Courtyard are entirely made by level design using the toolset at our disposal. This type of level design approach is something that gets very close to how Hitman levels were made.

### Environmental Storytelling & Narrative Design

First Light tells the origin story of the James Bond we all know from the movies. As players, we experience and learn at the same time as Bond, which was a great canvas to play with. Narrative Design is something I approach with writers; we usually spend hours talking about each beat and brainstorming about what Bond would say or do. The goal is to nail the fantasy and how the world around should react to him.

Environmental storytelling is a bit different to some extent. While the story will dictate the emotions of a moment, most of it relies on level design to find ways to elevate it. I usually try to come up with a lot of different ideas, then I share these with departments like Audio and Art. Together, we try to bring these to life and see how they can highlight the experience.

### Environments as Guides in the Game

The amazing thing with environmental storytelling is that it can help highlight almost anything gameplay-related, or just bring more lore to those who find it. It helps player engagement and agency, allowing them to experience the world and uncover opportunities without the game telling them exactly what to do.

I was able to use inspectable objects, ambient dialogs, secret passages, and hidden quest items to provide the world with a layer of unknown that is up to the player to discover. The game being set in real, believable world locations helped us to challenge players' common sense. I would sometimes think, "Hey, what would you do?" or "Where would you find this?" if you were actually there, and make sure the player gets rewarded for it. Games like Half-Life 2, BioShock, and The Last of Us were great sources of inspiration for me.

### Collaborating with Other Teams

Level designers are central at IO Interactive. They own the experience from start to finish, ensuring it plays correctly. It means that we have to be able to support any department and answer any question whenever necessary. Anything in the level will at some point be in the hands of the level designer in charge.

Collaboration is key; to some extent, I think I spend as much time talking to other departments as talking to level designers. This constant back-and-forth with other teams is a good way to learn more about other people's craft, facilitating cross-discipline collaboration.

### Creative Challenges

There are a lot of things to take into consideration when you want to create a story-driven game. We wanted to create an experience that inherently breathes IOI, bringing elements that players loved about Hitman. At the same time, we also needed to translate the core pillars of the Bond license through gameplay systems that truly embody him.

We also had a quality bar to meet: the game needed to stand alongside the best of its genre. Games like this usually guide players through a linear structure, which lets developers polish every moment to look its best. By bringing our creative approach and studio DNA to Bond, we wanted every open segment to offer players opportunities that felt equally polished. That pushed us to think outside the box and find solutions that kept us from over-scoping.

### Conclusion

During 007 First Light, I learnt a lot about the genre, how it is structured and what it requires to work. Collaborating closely with every department taught me how to be a better designer. I've always worked closely with environment artists, but it made even more sense on a story-driven game, where there are so many details to get right.

We're a real power duo! I shape the space and the flow, they bring it to life, and each of us pushes the other to make it better. The countless hours with writers gave me the keys to how to tell a good story, and how we can elevate it through gameplay systems.

Level design is all about iteration. You should always take feedback with open hands and never be scared to change and update things. This process isn't easy at first, but it's always worth it in the end. It will allow you to stay on top of things and be able to make better decisions as things evolve.

My advice for other designers would be to stay curious and never stop having fun when designing spaces. It's also important to play games similar to the one you're making to understand what works and what doesn't. It's always easier to come up with good or innovative ideas when you know what the industry has already done.

Last but not least, collaboration is key. If you want your design to shine, make sure every stakeholder around you knows about it. They need to not only understand it but be excited about it. When that happens, you'll see your idea live through the minds of others and become something even better than you imagined.

### [Thomas Pulluelo](https://www.artstation.com/thoms), Senior Level Designer

#### Interview conducted by [Emma Collins](https://www.linkedin.com/in/emma-collins-663070320/ "https://www.linkedin.com/in/emma-collins-663070320/")
