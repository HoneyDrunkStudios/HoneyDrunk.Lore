---
source: "https://80.lv/articles/bluey-s-simple-2d-look-required-gameloft-s-most-technically-challenging-art-pipeline"
title: "Bluey’s Simple 2D Look Required Gameloft’s Most Technically Challenging Art Pipeline"
author: "Gameloft Brisbane"
date_published: "2026-10-23"
date_clipped: "2026-10-23"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Bluey’s Simple 2D Look Required Gameloft’s Most Technically Challenging Art Pipeline

Source: https://80.lv/articles/bluey-s-simple-2d-look-required-gameloft-s-most-technically-challenging-art-pipeline

[Gameloft Brisbane](https://80.lv/author/gameloft-brisbane)

Interviewed by

[David Jagneaux](https://80.lv/author/david-jagneaux)

23 October 2026

# Bluey’s Simple 2D Look Required Gameloft’s Most Technically Challenging Art Pipeline

[#Interviews](https://80.lv/articles/interview)[#Blender](https://80.lv/articles/blender)[#Character Art](https://80.lv/articles/character-art)[#Environment Art](https://80.lv/articles/environment-art)[#Unreal Engine](https://80.lv/articles/unreal-engine)[#Video Games](https://80.lv/articles/video-game)[#Game Development](https://80.lv/articles/game-development)[#Maya](https://80.lv/articles/maya)[#Photoshop](https://80.lv/articles/photoshop)[#Substance 3D Designer](https://80.lv/articles/substance-designer)

Gameloft Brisbane explains how Bluey’s Happy Snaps uses SDF textures, 2D planes, custom shaders, and Unreal Engine Control Rig to recreate the show’s hand-drawn style.

[**Bluey’s Happy Snaps**](https://blueyshappysnapsgame.com/) invites families to explore familiar locations around Brisbane, play alongside Bluey and Bingo, and photograph characters, wildlife, and unexpected moments for a customizable scrapbook. Developed by [**Gameloft Brisbane**](https://www.gameloft.com/gameloft-studios/brisbane) in collaboration with Ludo Studio and BBC Studios, the photography-driven adventure [launched for PC](https://store.steampowered.com/app/3064040/Blueys_Happy_Snaps/), PlayStation, Xbox, Nintendo Switch, and Nintendo Switch 2.

Making the game look like an interactive episode was considerably harder than its clean, approachable visuals might suggest. Bluey’s characters were constructed from layered, camera-facing 2D planes placed inside three-dimensional environments.

The result is a hybrid pipeline designed to preserve the show’s proportions, outlines, poses, and carefully controlled color palette without preventing players from freely exploring its world or looking through a 360-degree camera. We spoke with many members of the development team to learn just how much complexity can hide beneath an apparently simple visual style.

**Bluey has one of the most recognizable visual identities in modern animation. When adapting that 2D style into an interactive 3D game, what were the most important qualities the team knew it had to preserve?**

**Sean Gobey, Technical Artist:** Much of Bluey’s very warm and friendly tone is conveyed through shape language and style. When translating Bluey’s Happy Snaps into a fully interactive video game, we tried as best we could to maintain Bluey’s aesthetic. Each character had to feel authentic to the TV show, as so much of their personalities and actions are rooted in that medium. When building Bluey’s Happy Snaps characters, each decision made was focused on giving the animators as much control and flexibility to bring Bluey’s 2D world to life in 3D.

During our research and development period, we opted to model the characters and create their skeletons in Maya before doing all the rigging in Unreal Engine 5’s control rig. As the characters are essentially “2D” camera-facing flat cards, we had to build quite an elaborate system in order for animators to animate on one angle and then copy that across the remaining 7 angles with the ability to adjust if needed. For the more technical readers, we heavily leveraged Signed Distance Fields to texture our characters, as that gave us the “vector look” with the added benefit of huge texture memory savings.

We used a combination of both geometry and SDF texture flip books for the characters. A good example would be the character’s hands, feet, and mouths. We were able to share the hand and feet textures and geometry across all characters. The eyes are completely done in shader using SDF bezier curves (thanks to resources from the great Inigo Quilez), where we have the option to drive eye darts and blinks either procedurally through a runtime control rig or hand-authored by animators in sequencer.

**Karl Von Der Luhe, Game Manager:** Bluey's Happy Snaps needed to look and feel like an interactive version of the TV show, in terms of art style.

**Hannah Crosby, Lead Artist:** The more we dug into the style and art of Bluey, the more we realised how much thought has gone into the colour palette, shape language and even outlines, to make it look so effortlessly simple. Bluey the TV show is all hand-drawn and painstakingly hand-authored, so although we experimented with some methods to try and automate our art generation, ultimately we needed to go with a hand-painted approach for many of our textures as well as 3D art. For example, painting in specific highlights and hand-placing shadows was the only way to accurately capture the artistic approach to lighting that the show creates.

The distinctive shape language was something we worked hard to hit, as this is something that can become lost among a 3D team as assets get modeled in programs with perfect shapes; hand-crafted intentionality needs to be reintroduced to truly feel Bluey.

Continuing with the theme of hand-crafting, to create a readable background in an unlit game, value and color need specific care and intention to make sure visuals stay readable across a level, and don’t muddy a scene. Replicating the look of the outlines was also a top priority. For this, our tech team developed a unique shading model in Unreal to simulate the effect of inverse hulls in real-time for our 3D assets.  The outlines are authored in the show to be a consistent thickness regardless of the distance of the object from the camera; therefore, our outlines could not decrease in thickness as an asset moved further away from the game camera.

**Dylan Perrett, Associate Lead Animation Artist:** From the beginning, the team knew that we wanted to capture the expression, play & sense of joy that's present in every episode of the series. During pre-production, we dove into a period of reference gathering. From series clips & smear frames to Reddit posts attempting to determine Bluey's height using tomato sauce bottles, there were so many fun examples of the qualities we wanted to capture. We were even lucky enough to get a peek at Ludo Studio's style guides. The hope is that we've done the show justice & those core sensibilities shine through.

**Can you walk us through the art pipeline for Bluey’s Happy Snaps, from reference gathering and style guides to modeling, texturing, rigging, animation, lighting, and final implementation?**

 **Hannah Crosby**: Our pipeline went through many iterations, and we had to take very different approaches for the characters as opposed to the environments, and again for the animals, to achieve the *Bluey* style, so the pipelines are very different. Our reference gathering was always to reference the show above all, but we also went further and looked into the stylistic references that the show uses to help us when creating unique assets that did not have a specific show reference.

Once a show reference or concept is created, our environment artists would model the assets in Blender or Maya, making sure to hit the shape language of the show. Textures are often a simple swatch-color base, with some hand-painted details, combined with a shader that allowed us to add decals, tiling details and shadows using different textures. There is no lighting as such in Bluey’s Happy Snaps, with all lighting information being hand-authored in the texture or material. We do use a customizable directional light within the material to add self-shadowing information to some assets to speed up the process, though.

As with any project, the whole workflow evolved and took many shapes. A good example is outlines, as they were initially tested as post-process effects, then geometry, using inverse hulls for the silhouette and splines for internal lines. With our final approach, the 3D assets, such as the in-game animal assets, use vertex colors to control the placement of the shader-generated outlines. Along with multiple UV sets to control the overlay layers in our environment material, the 3D assets contain a lot of information.

We retained the inverse hull approach for animals in the game, however, as this worked the best for that specific use case.  Assets that will be hand-held by characters have an additional step to “flatten” them when picked up, so our 2D characters can interact with them, and this is done within the shader. The characters themselves are a completely different pipeline, as they are not 3D in the traditional sense. The characters’ bodies are comprised of 2D planes modeled in Maya and textured using SDF ( signed distance field ) textures to render the body parts, which are rigged using a custom in-house 3D rig so our 3D-trained animators can animate them directly in Unreal Engine using Control Rig.

**The show’s characters look deceptively simple, but their shapes, proportions, expressions, and poses are extremely specific. How did the team translate Bluey, Bingo, and the rest of the family into 3D while keeping them faithful to the original designs?**

**Hannah Crosby**: In keeping with the essence of the *Bluey* TV show, we had to develop a method of creating and animating 2D characters that our 3D-trained character artists and animators could work with. This involved several months of R&D where we trialed and tested several approaches, re-inventing our pipeline several times.

Ultimately, our tech artist created a method using SDF textures UV mapped onto layered 3D planes that are skinned to a 3D skeleton that is rigged and animated using Unreal Engine. This way we could exactly match the 2D characters' look whilst having them move around a 3D space. When creating the characters, the first step is reference gathering to replicate all 8 angles.

Then our character artists created the color palette for the characters and used the unique SDF pipeline with custom tools in Maya to preview these angles while creating the maps for the different parts of the body using Photoshop and Substance Designer. The SDF textures are assembled in Maya, where it is also rigged and skinned. Once the model is imported into Unreal Engine, the materials and color curves are set up.

**Dylan Perrett**: With guidance from Ludo Studio, we were constantly on the lookout for the smaller details that make *Bluey* unique. It was vital for us to create animations with the correct sense of weight, line of action and appeal, while keeping movements clear & readable.

Additionally, because Bluey’s Happy Snaps allows players to view characters from various angles, the team created assets for the full 360 degrees of rotation at 45-degree increments. We soon realized that although that makes sense from a video game perspective, the series uses 0/90-degree angles sparingly. So, it became crucial to balance video game logic with the style expectations of the series.

**What were some of the biggest technical or artistic challenges in blending a 2D animated look with 3D environments, camera movement, lighting, and player-controlled exploration?**

 **Dylan Perrett**: Animating characters, as beloved as *Bluey’s*, in Unreal Engine was an immense challenge. Our control rig presented us with a unique set of limitations. For instance, each of the seven angles possessed a unique set of controls. We would animate one hero angle and use various in-house tools to copy, then clean up the animation to the six remaining angles. Additionally, there are obvious limits to characters with these proportions, so finding when & where the rig could break was an interesting exercise. Early on, the process was less about finding where the rig would break, and more about where the rig would work.

One thing we kept in mind was that, during dialogue shots, having the character's mouth open allowed us to identify any poses that would block lip-sync, compromise readability, or break the rig in undesirable ways.

**Sean Gobey**: I would say the biggest challenge was creating tools for both modelers and animators to bring the Bluey’s Happy Snaps characters to life. During production, it quickly became apparent much of the game needed to be designed around what the characters were able to do. An obvious example would be tilting the camera up or down when looking at the characters, as this revealed their 2D look. We discovered many of these constraints during development. This proved difficult as frequent character rig updates at times would render previous animation unusable.

**Hannah Crosby**: Creating 2D characters within a 3D world is a big challenge, and initially we kept many of the game cameras locked off to make them blend more seamlessly. However, when we found out we needed to incorporate a 360-degree player-held polaroid camera into the gameplay, we needed to find a way to flatten the layered 3D planes so the illusion wouldn’t be broken when viewing the characters from unexpected angles.  The characters already switch to different angles as the game camera rotates around them, but this extra step helped avoid seeing the planes that make up our characters be revealed from acute angles.

The animations themselves needed to be authored on up to 8 angles, but we developed a complex rig that allowed us to mostly animate on one angle and transfer this information, which sped up the process immensely. There is also some subtle shader-led tweening going on to prevent the characters appearing to snap between angles, which helps with blending them into their 3D surroundings. Lighting was not dynamic or changing in the scenes, and characters do not react to in-game lighting changes, which simplifies that matter immensely.

Traversing the levels didn’t pose any real problems, but having our characters sit on or interact with the 3D assets still remains one of the most challenging issues. Flattening objects as they are picked up solved some of those interactions; however, allowing assets to fit between the 2D planes that make up the characters.

***Bluey’s* world is full of soft colors, familiar family spaces, and playful environmental details. How did you approach building locations that feel authentic to the show while also supporting discovery, interactivity, and photography gameplay?**

**Karl Von Der Luhe**: *Bluey* is set in Brisbane, as is our development studio. This allowed the team to visit locations inspired by the show like South Bank, New Farm Park and Mt Coot-Tha and make these in-game locations faithful to both the show and our city!

**Hannah Crosby**: We are incredibly lucky that our studio is based in Brisbane, the city where *Bluey* takes place, so we were able to take field trips out to the actual locations seen in the show to get inspiration for fun easter-egg details to drop into the game.  Incorporating elements that only locals would recognize, but which add to the authenticity of the scenes, was a real delight.  We had to balance including elements that were iconic to that area with areas supported free-roaming gameplay, so a lot of thought and collaboration between the Art and Design departments went into designing the level layouts to both be true to their depiction in the show, visually appealing, and also clear and interactive.

**Because Bluey’s Happy Snaps is built around taking photos, the game needs to make every scene feel charming from the player’s perspective. How did the camera mechanic influence environment composition, character staging, animation, and visual storytelling?**

**Karl Von Der Luhe**: Bluey’s Happy Snaps encourages player exploration with many familiar characters to meet and interactive fun to have in each level. Some situations are set up for charming photos; many other photos will be up to player choice, with many authentic Australian fauna to capture. Having a second player pose in the frame also adds to how the players create memorable pictures!

**Hannah Crosby**: The use of the polaroid camera allowed us to hide fun surprises in areas that are not visible from the main game camera, encouraging players to engage with the photography aspects of the game, as well as the open-world toys.

The color palette and lighting were very important in conveying the feel of the show, and every asset was matched to that palette and adjusted depending on whether it was interactive, foreground or background to enhance the readability of the scenes. One lesson we learned from the TV show’s style was to pare back the detail strategically to allow the composition of the scene to be clear and readable.  Value and saturation were used deliberately to push elements into the background or draw attention.  When looking through the viewfinder, this was especially important so that players didn’t get disoriented.

Every scene had to be curated, readable, and appealing from any angle, as the player might pull out their camera at any time to look around.  There are some restrictions on the camera movement that deliberately prevent the player from breaking the 2D/3D illusion, and we had a lot of restrictions placed on us about where we could have NPCs and what objects they could interact with.  Ultimately, I think the game ends up feeling quite unrestricted and free from a player point of view, though. We also hid fun moments in the “macro” camera ability, which allowed us to curate some really pretty close-up scenes that are a call-back to the beautifully rendered close-ups of *Bluey* that heighten the realism and detail briefly.

**How closely did Gameloft Brisbane collaborate with Ludo Studio and BBC Studios on visual direction, approvals, animation references, and making sure the game felt true to the show’s tone?**

**Karl Von Der Luhe**: Ludo Studio and BBC Studios were great partners, sharing references and guidelines regularly. They also gave us the creative freedom as game development experts to push the gameplay loop as we saw fit.

**Hannah Crosby**: Our tech artists and animators spent time with Ludo Studio to better understand how they created their own 2D rig for the *Bluey* characters, and learn the “rules” for animating in the *Bluey* style, so we could translate that to our own animations.

We worked very closely with BBC Studios and Ludo Studio to ensure that the actions of *Bluey* and her family always felt in-character, and reflected the values of the show.  There was an ongoing conversation with approvals for all the assets, interactions, and cinematic moments in the game.  Every asset needed to be true to the world of *Bluey* and make sense in the larger context and chronology of the show.    Especially for cinematic moments where we had the opportunity to match the original show animations in complexity and quality, the approval process meant we went back and forth a lot to really make sure they felt like watching an episode of the show.

**The game is designed for families and young players across many platforms, including Switch, Switch 2, PlayStation, Xbox, and PC. How did performance, readability, and accessibility shape your art and technical decisions?**

**Hannah Crosby**: Performance was a struggle for low-end platforms, but we wanted to support those devices and provide a comparable experience, as so many of our core players would still be enjoying the game on those platforms.  Our outline shader and complex character rigging proved to be one of the biggest performance hits, so we tried to gain some performance back in areas like LODs and texture compression so as not to compromise the characters, which are the stars of the game.  It was important to use the polys wisely as the soft edges of all the shapes required a higher poly count when seen up close, or through the polaroid lens, but would also impact performance.

**What tools, engine workflows, shaders, or custom rendering techniques helped the team capture *Bluey’s* flat, illustrative charm in a real-time 3D game?**

**Sean Gobey**: The characters of Bluey’s Happy Snaps were a team effort in the truest sense. When you play the game, we pull data from modeling, rigging, animation, shaders, and code to build them at runtime. The core of our character art pipeline is Signed Distance Fields and Unreal’s Control Rig. We could not have made this project without both of those technologies. Before we settled on using Control Rig, our Principal Technical Animator Dave Shaw spent a few months grappling with a more traditional approach. Although Dave got a system up and running, it wasn’t flexible enough, nor did it allow for rapid iteration and feature implementation as much of the character pipeline requires tight integration between gameplay code, animation, curves, and materials.

**Hannah Crosby:** Our tools, shaders, and engine customization had to be very bespoke for the needs of this game.  As mentioned before, an entirely new shading model needed to be created to capture the specific unlit look for the textures and add in the dynamic outlines.  There were a lot of custom tools built for Maya as well, to speed up the workflow with adding vertex colors to control the outline shader, along with our standard export and import pipeline tools that have been crafted by our tech artists over many projects.

Our characters are probably the most unique pipeline I’ve seen in my time as a character artist.  Because of the 8 angles that needed to be authored, the artists had specific tools that they could use to preview the models and textures as they were being constructed.

The SDF textures used red, green, blue, and alpha channel masks and so needed a custom material in Maya to preview the intended colors while being constructed, as the final look of the characters would only come together when they were finally in Unreal and the materials and color curves were set up. Our animators retrained from Maya to animating using the Control Rig in Unreal Engine, which also included custom tools to view the animations from all 8 angles as needed, before they were compiled into an animation montage for use in-game.

**For 80 Level’s audience of artists and developers, what has been the biggest lesson from adapting such a beloved 2D animated series into an interactive 3D world that players can explore, photograph, and play inside?**

**Sean Gobey**: Having a strong understanding of the source material is so important. It’s much easier to make intentional decisions when you know why you’re making something, and how it’ll be used within the tapestry of the project. I also feel communication and having a solid understanding of the whole game development process is paramount. Learning about each department and understanding how your work interfaces with them gives you the ability to help innovate and solve problems. Maybe programming could remove an entire step if you did one thing differently? Or maybe design is working around and easily solved problem? Art could be doing something unnecessary because they don’t know any better.

**Hannah Crosby**: The biggest lesson I learned on this project is to never underestimate the tenacity of a tech artist when they are given an impossible problem to solve, and that truly remarkable things are possible when you think outside the box. This is most certainly the most technically challenging project I have ever worked on, and is in direct contrast to how clean and simple the visuals appear. It has also been a great opportunity to dive into the artistic reasoning and carefully curated visuals of such an iconic show, and I think that, as an artist, by breaking down what makes each of the scenes in *Bluey* work so well visually, I have learned a lot about composition, color, and shape language.

So, for your audience, I would say, take the time to try and break down the way the visuals are constructed in your favorite games and shows.  Get into the heads of the artists who made those decisions and see what you can learn.

**Dylan Perrett**: Be willing to adapt. By the end of pre-production, we realized that Maya wasn't equipped to handle the pipeline needed to make this project a reality. Luckily, our technical artist, Sean, had been tinkering with UE's control rig as a potential alternative. I'll admit, I was resistant to stepping away from Maya in favor of another software at first. Thankfully, the animation updates that arrived in UE5.6 made the transition far simpler than I initially feared. Ultimately, tools & workflows are always evolving. It’s less important to be a Maya/Blender/Unreal Engine animator, and far more advantageous to be an animator who uses Maya/Blender/Unreal Engine.

### **[Karl Von Der Luhe](https://www.linkedin.com/in/karl-von-der-l%C3%BChe-7220875a/), Game Manager** **[Hannah Crosby](https://www.linkedin.com/in/hannahcrosby/), Lead Artist** **[Sean Gobey](https://www.linkedin.com/in/seangobey/), Technical Artist** **[Dylan Perrett](https://www.linkedin.com/in/dbperrett/), Associate Lead Animation Artist**

#### Interview conducted by [David Jagneaux](https://www.linkedin.com/in/davidjagneaux/ "https://www.linkedin.com/in/davidjagneaux/")
