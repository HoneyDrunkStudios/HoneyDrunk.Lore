---
"source": "https://80.lv/articles/inside-marvel-rivals-character-art-vfx-destruction-pipeline/"
"title": "Behind the Scenes: How the Marvel Rivals Art Team Builds a Character"
"author": "Marvel Rivals Art Team"
"date_published": "2026-10-02"
"date_clipped": "2026-10-03"
"category": "Technical Art & Creator Tools"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# Behind the Scenes: How the Marvel Rivals Art Team Builds a Character

# Behind the Scenes: How the Marvel Rivals Art Team Builds a Character

Marvel Rivals combines decades of comic history with custom NPR/PBR rendering, hero-specific VFX, alternate costumes, and scalable destruction. The game's Art Team explains how those systems come together.

[ Marvel Rivals](https://www.marvelrivals.com/) brings together characters with decades of history across comics, films, animation, games, and merchandise. That familiarity is enormously valuable, but it also creates a difficult artistic challenge: every hero must remain immediately recognizable while feeling original within the game’s stylized universe.

In this interview, the **Marvel Rivals Art Team** (including Dino Ma, Art Director; Dongyang, Art Supervisor; Weitai Luo, Art Supervisor; Yuzhen Zhang, Lead Character Designer; Zhen Li, Lead 3D Character Artist; Zhuo Yuqi, Lead Animator; Peng Weifeng, Lead VFX Artist) explains how it identifies the visual anchors that define each character, reinterprets familiar designs for contemporary players, and carries those ideas from reference gathering through concept art, modeling, animation, and VFX.

Using Cyclops as a detailed example, the team also discusses its custom NPR/PBR shading model, controlled destruction system, cross-platform asset tiers, alternate costumes, and the technical work required to maintain visual clarity during chaotic multiplayer battles.

**Marvel Rivals features some of the most recognizable characters in pop culture, but they also need to feel fresh within the game’s own visual identity. How does the team approach redesigning an iconic Marvel Super Hero or Super Villain while still preserving what makes them instantly recognizable?**

**Marvel Rivals Art Team: **When players encounter an impressive Super Hero character, they are often drawn in by the visual traits these characters exhibit—such as the unique design of each Super Hero's costume, their superpowers, or the distinctive and recognizable logos on their suits, as well as the unique weapons they wield in battle.

This includes the first impression they create upon making their entrance: the massive green Hulk or the agile red Spider-Man, for instance. These captivating traits that excite fans are the core design elements we need to preserve and build upon. Strengthening and maintaining these elements is essential to ensuring that players can instantly recognize and call out the character's name at first glance.

**When beginning work on a new character, where does the process usually start: comic history, gameplay role, silhouette exploration, narrative context, or something else entirely?**

**Marvel Rivals Art Team: **The story of Marvel Rivals is set against the backdrop of the Marvel Comics universe, so our first step is to delve into the storylines and specific character representations within that realm. The Marvel Comics universe is expansive, and the characters and their narratives offer a wealth of rich and inspiring ideas that are crucial for establishing a superhero's brand identity. Additionally, we focus on how these characters are portrayed across various artistic mediums—such as movies, games, animations, and toys. We firmly believe that exploring these "extracurricular readings" adds depth and multidimensionality to our character designs. By gathering this material, our understanding and interpretation of the characters become increasingly comprehensive.

**Can you walk us through the full character art pipeline for Marvel Rivals, from early reference gathering and concept art to final modeling, texturing, rigging, animation, VFX, and in-game implementation?**

**Marvel Rivals Art Team: **

**Concept: **Cyclops is a highly representative character. As a significant figure in the X-Men and the broader Marvel universe, fans are very familiar with his more classic designs in animation and on the big screen. Thus, our biggest challenge is to reimagine and reinterpret the commanding presence of Cyclops. Our goal is to create a version of Cyclops that differs from any previous iterations. We began by drawing inspiration from Scott's design in the classic comic series and aimed to incorporate a sense of futurism and fashion into a streamlined and cohesive design language, while keeping the outfit simple and fluid. This includes details like the costume cut, Cyclops' gold tactical straps, and his iconic energy-suppressing visor, all aimed at making this new Cyclops more aligned with modern aesthetics and uniqueness.

**Modeling/Texturing: **In terms of rigging and animation, Cyclops' rigging setup is relatively standard. However, his default skin features a visor, so we ensured that the rigging for the eye area was well-crafted to allow animators the freedom to be creative, especially considering alternate costumes may not include the visor. Animation development typically starts with designing basic actions such as idle, running, and jumping to establish Cyclops' movement style, followed by the creation of skill animations based on that style. For skill animations, we prioritize functionality while amplifying animation details, often drawing from Cyclops' signature moves in the comics as inspiration.

**Effects: In-Game:** During the skill effect design process, we encounter various design challenges. Cyclops' core mechanism involves firing lasers through his visor, and the available visual elements from the franchise are somewhat limited. To create a visually fresh experience while maintaining the character's recognizable image, we designed differentiated visual expressions for each set of skill effects. The left mouse button corresponds to a B-level common skill, featuring a slender cylindrical laser profile with a subdued overall visual to avoid distractions. The Shift key represents an A-level mobility skill with a wide, flattened laser cross-section, optimizing visual impact to match the skill mechanics. The Q key activates an S-level ultimate ability that creates a large area effect with splintering debris and Kirby Crackle particles, clearly defining the skill's impact range while highlighting the character's formidable power from the source material.

**Out-of-Game Effect: **For character display animations, we maintain a consistent visual design approach. The ruby visor serves as Cyclops' core visual anchor, with the showcase and MVP highlight effects centered around it. The main visual features a laser shockwave complemented by Kirby dots and black lightning to enhance the energy detail. The showcase adopts a progressive charging rhythm, with energy converging towards the visor, and a dramatic black-and white flash added at the critical charging point, culminating in a massive laser blast that visually demonstrates the character's destructive capability. The MVP highlight focuses on showcasing the character's combat mobility, with dynamic laser effects interwoven throughout, concluding with a freeze-frame of Cyclops unleashing a laser, reinforcing the character's iconic visuals and leaving a lasting impression on players.

**Marvel characters often have decades of visual history across comics, films, animation, toys, and games. How does the team decide which elements to honor, which to reinterpret, and which to leave behind for a specific Marvel Rivals design?**

**Marvel Rivals Art Team: **As mentioned earlier, it is essential to inherit and preserve the iconic visual traits of characters, while recognizing that their representations can vary across different artistic expressions. Instead of focusing on what to reinterpret or discard, we aim to integrate various storylines to highlight specific traits. This is similar to different versions of the same character existing in alternate timelines within the same universe; they share similarities but each shines independently.

In our Marvel Rivals battlefield, characters embody a vibrant timeline within the vast Marvel Comics universe. Here, the world is engulfed by a blood moon due to Dracula's resurrection, prompting superheroes to enter a heavily guarded New York to save the day. Invited by Krakoa to attend the Hellfire Gala, they team up with Emma Frost to face the supervillain Ultron. After their heroic efforts, they also enjoy rare moments to shed their battle armor and experience a vacation like ordinary people. These unique interpretations are what we strive to achieve.

**What are some of the biggest technical challenges when creating characters for Marvel Rivals, especially when they need to support expressive animations, destructible environments, unique abilities, skins, and strong performance across platforms?**

**Marvel Rivals Art Team: **

**Technical Art: **To create a destructible environment, we developed a sophisticated shattering system that includes automated building cutting tools, debris drop effects, and adaptations for hero skills. Our focus is on ensuring that the shattering effects are both natural and visually appealing, with distinct cross-sectional structures for concrete and wooden debris. Our algorithms for fragment segmentation achieve natural proportions for various sizes of debris while meeting gameplay needs for cover. To ensure smooth performance, debris drops are simulated through visual effects rather than physical calculations, allowing designers to control the rhythm of falling debris and integrate details like smoke, tiles, and glass, resulting in a unique artistic style and a dynamic visual experience.

**Marvel Rivals Art Team: **For cross-platform performance compatibility, our strategy involves asset tiering and strict rendering budget management. We create different asset tiers, including high and low-quality lighting for scenes and varying levels of effects. Additionally, we developed engine features such as mask box culling for lighting and overlay effects for character buffs to enhance overall performance.

**From a modeling and texturing standpoint, what software and tools does the character team use most often? Are there any specific workflows, shaders, material systems, or stylization techniques that help define the Marvel Rivals look?**

**Marvel Rivals Art Team: **We customized a character shading model that combines Non-Photorealistic Rendering (NPR) with the highlights of Physically Based Rendering (PBR). This allows character production to freely control color tendencies in shading, stylized highlight shapes, and more. As a result, the characters reflect realistic textures while retaining a 2D, flat brushstroke feel, showcasing our unique artistic style that blends 2D and 3D elements.

To seamlessly integrate stylized characters into relatively realistic environments, we developed various rendering features to manage the brightness of direct and ambient light on the characters, as well as automatic exposure adjustments within their local range. This ensures that the overall light ratio remains stable, allowing the characters to maintain clear, sharp outlines and a strong sense of volume.

**Some Marvel characters have very specific physical traits, such as Hulk’s mass, Spider-Man’s agility, Venom’s fluid symbiote form, or Magneto’s imposing presence. How do you translate those qualities into character art and animation?**

**Marvel Rivals Art Team: **When it comes to these iconic features and highly recognizable visual anchors, our focus is on how to effectively inherit them by blending contemporary aesthetics with market trends and player preferences, rather than making intentional or forced modifications. For instance, Magneto may be portrayed as an older general, differing from the robust middle-aged depictions commonly seen in comics, but any changes to his appearance are designed to enhance the character's inherent authority and gravitas.

**How do VFX factor into character identity? For example, how do you approach powers like magic, symbiote effects, energy blasts, portals, shields, or transformations so they feel unique to each hero while still fitting the game’s overall visual language?**

**Marvel Rivals Art Team: **In Marvel Rivals, visual effects are central to representing each character's identity. Our design approach combines a unified comic rendering framework with materials, IP elements, and dynamic rhythm to differentiate characters while ensuring IP fidelity and visual clarity in multiplayer combat.

Each hero's entrance and MVP highlight segment tells a mini-narrative that conveys the story behind their costumes, integrating character animations with environmental elements to express their unique traits.

**Marvel Rivals Art Team: **We use color and atmospheric rendering to reflect the emotional states of heroes in various contexts. For instance, the wedding of Gambit and Rogue features a sweet and gentle overall atmosphere in the effects.

For character animations in storyboard sequences, we utilize effects to enhance the dynamic rhythm and amplify the impact of keyframes. For instance, the scene featuring Black Cat riding a motorcycle and destroying obstacles relies on rhythmic manipulation to elevate the satisfaction of each action.

In certain slow-motion shots, we apply customized stylistic treatments to emphasize character emotions. In a dark fairy tale theme, Moon Knight's struggle against encroaching darkness conveys a sense of madness and oppression, while Iron Man's samurai-like chop of a wooden post features a striking black-and-white freeze-frame effect, creating distinctive visual signatures for the superheroes within the current narrative context.

**Marvel Rivals also includes alternate costumes and skins. How does the team approach variant designs in a way that lets players recognize different eras or interpretations of a character while maintaining gameplay readability?**

**Marvel Rivals Art Team: **Similarly, we prioritize preserving the core visual traits of the characters—such as their body silhouette, hero logos, signature weapons, and unique color schemes. These elements serve as a foundation, ensuring that changes in era or worldview do not affect the characters' uniqueness or players' recognition, while also allowing us creative space to explore different design ideas.

For example, in a Western cowboy setting, we could dress the Hulk in cowboy pants and a hat, or give Rogue a stylish cowboy outfit.

**Are there any characters that were especially difficult to adapt because their comic design, powers, or silhouette did not immediately translate into a multiplayer shooter-style format?**

**Marvel Rivals Art Team: **Thanks to the groundwork established during the project initiation phase, we were able to complete a systematic game adaptation process ahead of time, standardizing and optimizing the comic outlines, character traits, and ability systems for all Marvel Super Heroes and Super Villains. As a result, during the character design process, we could retain the original core characteristics and recognizability of heavy armor types, and superpowered characters. Furthermore, we adjusted their ability logic, physical traits, and combat rhythm to align with the rules of multiplayer shooting battles. This approach aims to ensure that the unique traits of the comic characters seamlessly integrate into real combat scenarios, effectively minimizing potential issues such as stylistic dissonance and ability mismatches.

**For artists hoping to work on licensed characters or large-scale multiplayer games, what advice would you give about building production-ready character art that respects an established IP while still bringing something new to it?**

**Marvel Rivals Art Team: **When designing classic characters, it is essential to respect the original design while thoroughly preserving the core IP identifiers. Additionally, we must adhere to the project's artistic standards, which define the scope for incorporating innovative elements on top of the classic foundation. Striking a proper balance between these two aspects provides a solid starting point for production design.

**Marvel Rivals **Art Team, [NetEase Games](https://www.neteasegames.com/)

#### Interview conducted by [David Jagneaux](https://www.linkedin.com/in/davidjagneaux/)

# Subscribe to 80 Level Newsletters

Latest news, hand-picked articles, and updates

[Get Our Media Kit](https://80lv.info/partnership)
