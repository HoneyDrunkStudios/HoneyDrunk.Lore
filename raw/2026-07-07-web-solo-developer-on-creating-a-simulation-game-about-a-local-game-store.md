---
source: "https://80.lv/articles/solo-developer-on-creating-a-simulation-game-about-a-local-game-store/"
title: "Solo Developer on Creating a Simulation Game About a Local Game Store"
author: "80 Level"
date_published: "2026-07-06"
date_clipped: "2026-07-07"
category: "Game Development / Unity"
source_type: "web"
---

# Solo Developer on Creating a Simulation Game About a Local Game Store

Source: https://80.lv/articles/solo-developer-on-creating-a-simulation-game-about-a-local-game-store/

# Solo Developer on Creating a Simulation Game About a Local Game Store

Sia Ding Shen spoke with us about TCG Card Shop Simulator, explaining the core mechanics, some of the card games that inspired it, and detailing how they built different systems that create a cohesive experience.

### Introduction

I'm Ding Shen Sia, a Solo Game Developer from Malaysia. During my time at Passion Republic, I worked on various projects including Shadow of the Beast, The Legend of Korra, Drawn to Death, and GigaBash as a rigger, technical artist, and programmer. As a Solo Dev, I've created 10 mobile games before going into PC game development and creating TCG Card Shop Simulator. I got into game development mainly through self-learning, starting from Macromedia Flash and then Unity.

### Core Mechanics of TCG Card Shop Simulator

The core mechanics of the game are managing the shop, opening card packs, and collecting cards. One of the starting points for me is to capture the excitement of opening a card pack and getting a rare card, and you get to decide whether to keep it for your own collection or sell it to customers in the shop. In the beginning, players have to be quite hands-on in managing the shop and have less time and resources to open packs.

Progressing through the game, they are given a lot of tools to make the management part easier or more automated, so they get more time for the collecting part while earning profit. And if they are not interested in card collection, they can always sell them to maximize profit. Besides that, players can manage tournaments, trade cards, decorate the shop, and with the playable TCG coming soon in 1.0, there will be more gameplay variety.

While the game takes inspiration from real card shops and TCG experiences, my goal was never to create a fully realistic simulator. The game is mostly just a card shop owner's fantasy; there's no way in real life you can rip cases of card packs at the corner of your own pitch-black card shop, hoping to make bank, and forcefully spraying your customers with deodorant.

### Inspirations

The shop management side of the game was inspired by Recettear and Supermarket Simulator. The restocking and selling items mechanics are simple but pretty satisfying when I played them, so it became the base of shop management mechanics. For the card collection aspect, it's definitely inspired by real-life TCG like Pokémon, Yu-Gi-Oh, Digimon, etc. As a kid, I really loved Pokémon and Digimon, and felt really happy when I got to collect the cards with my favourite characters. So in this game, I tried to replicate that feeling in the card's visual style.

### Technical Perspective

The game has a lot of different systems, and all of them have to work well together to have a cohesive experience for the players. Before starting to code, I planned out the features I wanted and how they would interact with one another. After that, I started coding for the core mechanic, which is the item and restocking system. Once I got that working, I moved on to the card pack opening, card collection, and customer system.

Once these are done, the basic gameplay loop is pretty much there, so I proceeded to add in features one by one to make it more interesting. I don't create custom tools and mostly use the Unity Asset Store if I need one, like I2 Localization for localization and A* Pathfinding Pro for customers' walking paths. As a solo developer, it didn't make sense to build these systems from scratch when I can just get them easily on the Asset Store; it really saved me a massive amount of time.

One of the biggest challenges for me is performance. The shop can be filled with an endless amount of items, decorations, customers, workers, and cards. And throughout development, I kept having problems with lag and loading time when the shop got bigger with lots of items in it. I spent a lot of time profiling, culling, and reducing unnecessary rendering throughout Early Access development, and performance and loading have improved significantly compared to the early version.

However, there is still room for improvement, and so optimization is still an ongoing process. Preparing to launch the game across multiple platforms while still finishing up a game that's in Early Access is impossible for me to do alone. And that's why I asked General Arcade to help with the porting; working with them is one of the best decisions, and this freed up a significant amount of time for me to work on the playable TCG for 1.0.

### Promotional Strategies

I use Reddit to promote and get feedback for my game; it's what I've been doing since starting mobile game development until now. It is what worked best for me compared to other social media platforms, so I stuck with it. After launching TCG Sim in Early Access, many YouTubers/streamers picked up the game even though I never contacted any of them, and this brought a lot of attention to the game and made it explode in popularity. At the end of it, I realized how powerful their influence is and would definitely include them as a key part of my marketing strategy next time.

### Current Development

TCG development is going well and on track to exit Early Access this Fall. Players are really excited for the playable TCG, especially when it's coming sooner than expected. Throughout development, I got burned out due to unhealthy work hours, and it taught me an important lesson about taking care of my physical and mental health and how important it is to pace yourself properly during game development.
