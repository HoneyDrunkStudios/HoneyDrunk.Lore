---
source: "https://polycount.com/discussion/238751/clayform-sculpting-app"
title: "Clayform Sculpting App"
author: "Polycount"
date_published: "2026-06-23"
date_clipped: "2026-06-29"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Clayform Sculpting App

Source: https://polycount.com/discussion/238751/clayform-sculpting-app

Clayform Sculpting App — polycount 
You are using an outdated browser. Please upgrade your browser to improve your experience.
Toggle navigation 
Polycount 
News 
Forums 
Patreon 
Challenges 
The BRAWL² Tournament Challenge! 
Bi-Monthly Environment Art Challenge 
Wiki 
Moar 
Recent 
Activity 
Badges 
Drafts 
Store 
Help 
Sign In · Register 
Author: shinobik 
Home › Coding, Scripting, Shaders 
Clayform Sculpting App 
Noth 
polycounter lvl 17 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 23 2026 
2x playback speed
Hey all. Started this over xmas break as an experiment and just kept poking at it.. The original question was how far I could get on top of open-source libraries -- there's a good number of them out there to build on. It's getting close to the point where I can actually use it to make stuff..!? I'm calling it Clayform.
What it is: a GPU based 3D sculpting tool built in Godot. So we get real-time viewport, post processing, modern material workflow, UI toolkit for free, then I've workshopped the brush engine & sculpting toolset for good feel (I come from zbrush). The ui/ux is a mix of maya + zbrush with opinionated brush-hotkey defaults. (alt + q,w,e,r,a,s,d,f)
First clip is just sculpting around to show the general feel. Second is the part I'm working on now: a setup for sculpting tileable textures, where the center tile repeats in a grid around it so you can see how well it's tiling as you go. I'm thinking I'll approach it sort of like how 3DCoat does, at the start you choose what mode you want the program to be in, then I can customize the UI to fit that space.
In now:
8 core brushes with good feel (clay, trench, trim, standard, flatten, pinch, smooth, inflate) 
brush masking (zbrush-style UX: ctrl to mask, ctrl+alt to erase mask, ctrl+alt off-mesh to clear mask) 
brush context panel (space) opens brush-specific settings like strength, spacing, etc. 
symmetry sculpting (x, y, z) 
transform gizmo in local + world space (w/e/r hotkeys like maya, q is sculpt mode) 
undo/redo (ctrl+z / ctrl+shift+z; works across sculpting and gizmo transforms) 
mesh import/export 
sculptmesh palette / subtools (alt+click to switch, like zbrush) 
.clay file format that stores undo history per sculptmesh (no masking or camera history yet) 
tiling texture wrap sculpting (the second clip) made a cute clayform logo.. may have done that very early on.. 
Planned:
posable armature sculpting -- I always hated zspheres being a destructive conversion into geo 
tiling texture previews on 3D shapes instead of a grid listen to the community and add stuff based on what we think is cool.. 
Got the windows build process working and tested an installed build on my own machine. Still a fair bit to go, but figured I'd put up a post and keep updating it as I go. Happy to answer anything about how it works.
It's alive!
What do you guys think of the logo? The idea is a play on words of lifeform -- clayform.
Curious to hear about feature requests! 
-AM
4 · Share on Facebook Share on Twitter 
Tagged:
sculpting 
Realtime 
PBR 
Replies 
Online / 
Send Message 
Eric Chadwick 
admin 
Jun 23 2026 
Wow this is great. How do you handle tessellation, and do you have some sort of retopo to add more detail when surfaces are stretched out? 
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 23 2026 
@Eric Chadwick Hey! It's all just fixed densities now set dynamically via sliders/input boxes, I don't have subdivision levels yet but that's on the short list. I did some early experiments with instant meshes  as an external tool dependency but the quality wasn't quite there, and you can't use the field/curve guides headless, only in the GUI. iirc I landed on QuadWild being the best bet (it takes explicit feature edges + a guide cross-field as files, so you could drive it from painted curves), but there's some licensing stuff to consider there. So I shelved retopo in general — I didn't have the brush engine side solid yet, so figured I'd go focus on that first.
I've also got a branch with an SDF experiment — an adaptive octree SDF, which is basically the DynaMesh-style answer to your second question: the tessellation follows the field and re-grids as you add/cut, so stretched areas get fresh, evenly-sized topology instead of smearing. I first meshed it out with Transvoxel, but the LOD transition-cell stuff got nasty (seam cracks at the octree level boundaries), and I came around to Surface Nets being the better extraction method — it's a dual method so it outputs all-quads directly, no ambiguous cases, no transition tables, ~half the verts of marching cubes, and it's nicely GPU-parallel. Sharp edges get a selective QEF solve (the dual-contouring trick) only on the cells that need it. So it basically collapses MC → retopo into one step. I shelved it to get the core brush feel locked first, but that's where I'd pick the volumetric side back up. 
1 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 24 2026 
Figured I'd pull a few folks I talked to recent in here. 
@gnoop Since you mentioned tiling textures, what you think of this tiling texture mode? bit simpler than setting it up in ZBrush?
@fallenskyzero this will work on Linux out of the box 
@Neox I've got proper 3D camera here, undos on mesh + gizmo edits + masking edits. Curious where you think camera movements should live, it's own undo history track similar to maya?
@zetheros Won't have any tool managment issues here. I plan to design the sculptmesh palette more similar to maya, create, move, parent, export directly from it, etc
@iam717 can write shaders for use while sculpting, since it's in Godot.. lots of potential since it's in godot, can likely write a C# plugin API to extend the software.
@Vexod14 pretty sure I can support some version of retopo manually, I'd really like to be able to model the base subdivision level and just reproject that back to the higher without even needing to retopo, you'd just use your edited base mesh..
What would you guys put in your ideal modelling/sculpting workflow? Some room for procedrual rock mesh generation as a headstart? Pie in the sky ideas welcome. 
1 · Share on Facebook Share on Twitter 
Online / 
Send Message 
Eric Chadwick 
admin 
Jun 24 2026 
Also @pior was talking recently about issues with Flatten brushes, and how MudBox got it right.
1 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
zetheros 
insane polycounter 
Jun 24 2026 
I was always wondering if there was a weighted, procedural method of imprinting 3d voronoi geometry on highpoly subdiv meshes. Something to achieve details like scales or sculpted feathers, fur and intricate details that have a 'flow' to them on characters and creatures that can't be done with tiling textures alone. Scales aren't uniform on a creature; some scales are large, others small. You can get a lot done with alpha brushes, but there's no clean way of achieving this (to my knowledge). So, maybe by using a method similar to weight painting, one could paint a weightmap with weighted vertices dictating the size of scales (or whatever other pattern you'd use), as well as designate their directional flow, possibly by using edge normals, onto subdivision level 1. Ideally this could be achieved without requiring a lowpoly with a UV map, since during sculpting, the lowest subdivision sometimes needs changes on the fly which would disrupt UVs.
Sculpting for me has always been making geometry that wouldn't be possible to do with texturing; so anything that is tiling or that can be procgen is textures/materials work. Tiling 3d geometry is very cool, but I don't see why I would use tiling geometry when I could use substance designer, entirely bypassing the need for sculpting. Maybe for architecture/environment props? But then I would use a trimsheet and modular assets 
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 24 2026 
@zetheros hey cool ideas, the first thing that came to mind was scaling UVs to edit tiling density, but you might also be able to do something like HP sculpt layers like ZB has, but then scale the detail in those layers via a scaling brush (up or down) before projecting to the mesh.
as for sculpting tiling textures, imo sculpting organic textures is way more efficient in ZBrush than Substance.. I find myself noodling with nodes way longer on something that I could just sculpt directly. Designer is great for hardsurface stuff, especially if you have heightmaps to bring in. My intention with this tiling sculpt mode is to sculpt -> preview it's tile-ability over large areas -> export for baking in marmoset. 
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Vexod14 
sublime tool 
Jun 25 2026 
@Noth I'd say it depends on what you want to achieve ; I often use retopo just to draw polygons and refine an existing shape by adding it as a detail, it's especially useful when doing hardsurface. I also use 3dsmax basic retopo tools 99.99% of the time, they do the job and stay in the modeling loop within the same software, which is important since I also rely on UVs and other modifiers to get a model done. I use ZBrush when I have to design complex shapes, as well as hairstyles, or if I want to craft assets that will later require a bake, or simply if I just want to have fun because sculpting is fun ^^ 
About your app maybe you could add "normal/AO/Curvature matcaps" and find way to directly output the center tile as separate textures of a chosen size and format ? So we wouldn't need an extra jump in another app to get the texture we want =D
Either way you're doing amazing stuff, I find it impressive as I'm an artist quite lost when it comes to coding ^^" I'd be curious to try your app one day !  
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Neox 
grand marshal polycounter 
Jun 25 2026 
Noth said: 
Figured I'd pull a few folks I talked to recent in here. 
@Neox I've got proper 3D camera here, undos on mesh + gizmo edits + masking edits. Curious where you think camera movements should live, it's own undo history track similar to maya?
dayum! need to check when i have the time 
in max its also its own undo track, i think that makes sense, you like dont wanna clutter your actions undos with camera movements. 
from now switching to blender (and not testing your tool) what i dearly miss there is a proper alt smooth behaviour like in zbrush i can go a little into depth, but dont wanna clutter your thread for this tool with my possible lack of blender knowledge   
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 25 2026 
@Vexod14 that's part of why I want to build something, I wanted to go back to Zbrush and didn't have a license, I never bought a persistent one, I just had them from work but that changed eventually. I couldn't go sculpt for then fun. I couldn't justify the subscription for an occasional use, since I wasn't using it for work either. I really want a low cost option in the space. I do want to support something like retopo, but again yeah I think if you could just edit the base mesh model then you wouldn't really even need retopo.. you know? skip retopo but offer UVs then export base + HP for baking in Marmo.
@Neox still happy to hear your thoughts on the sculpting there and going back and forth from modelling/sculpting there. I haven't got into that, it's been on my todo list for ages.. I've read plenty about Blenders geo cap and lag in higher targets since it's all on the CPU -- have you ran into that yet? I imagine it's more of a, switch to modelling your low poly to sort things out, switch back to sculpting after once you've lowered things -- not sure if it works like that but seems like a good bet for a software that has it all.
Also I set this up to feel like ZBrush so alt is masking, ctrl+alt out of the mesh is discard mask, I just need to setup invert mask. Smooth is shift (is that what you mean?) I build mask and smooth to be their own brushes too, but they have special alternate hotkeys that mirror ZBrush so the muscle memory for some is just there. 
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
pior 
grand marshal polycounter 
Jun 26 2026 
How cool is that !
Indeed, a solid and predictable Flatten would make a world of difference 
Also, having intuitive control on the center of viewport rotation is probably quite important.
2 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Neox 
grand marshal polycounter 
Jun 26 2026 
Noth said: 
@Vexod14 that's part of why I want to build something, I wanted to go back to Zbrush and didn't have a license, I never bought a persistent one, I just had them from work but that changed eventually. I couldn't go sculpt for then fun. I couldn't justify the subscription for an occasional use, since I wasn't using it for work either. I really want a low cost option in the space. I do want to support something like retopo, but again yeah I think if you could just edit the base mesh model then you wouldn't really even need retopo.. you know? skip retopo but offer UVs then export base + HP for baking in Marmo.
@Neox still happy to hear your thoughts on the sculpting there and going back and forth from modelling/sculpting there. I haven't got into that, it's been on my todo list for ages.. I've read plenty about Blenders geo cap and lag in higher targets since it's all on the CPU -- have you ran into that yet? I imagine it's more of a, switch to modelling your low poly to sort things out, switch back to sculpting after once you've lowered things -- not sure if it works like that but seems like a good bet for a software that has it all.
Also I set this up to feel like ZBrush so alt is masking, ctrl+alt out of the mesh is discard mask, I just need to setup invert mask. Smooth is shift (is that what you mean?) I build mask and smooth to be their own brushes too, but they have special alternate hotkeys that mirror ZBrush so the muscle memory for some is just there. 
it might be just my lack of knowledge but no matter which smooth brush i used, extension/addon or built in the first pic is the best i could manage inside blender, also using edge flow, relax and other per vert/edge/face methods. But zbrush's alt smooth is just far superior as shown in the second image 
2 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
sacboi 
grand marshal polycounter 
Jun 26 2026 
@Neox I've only just started learning Blender's sculpting functionality cos can't afford zbrush atm so curious if you tried this method? (found it online) 
Setting Up ZBrush-style Alt-Smooth in Blender
1.  Activate the Smooth brush: Hold Shift to temporarily switch to the Smooth brush.
2.  Access Brush Settings: Press Ctrl + Spacebar to open the Brush Settings pie menu.
3.  Change the Operation: In the brush settings, ensure the operation is set to Smooth. (By default, holding Ctrl with the Smooth brush activates the Sharpen tool).
4.  Preserve Volume: Check the Relax option (or change the Deformation mode) and set the Smooth brush strength to a lower value (e.g., around 0.3 to 0.5) to prevent it from shrinking your sculpt.
5.  Adjust Brush Curves: If you want a falloff that mimics ZBrush's Alt-Smooth, adjust the curve under Brush Settings > Falloff to something more linear or custom. 
2 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 26 2026 
@Neox ah I see, you literally just want a nice smooth bound to the familiar shift key? I see -- yeah me too, all the hotkeys in Clayform are ZBrush inspired. I did change the zoom though because I think that's one that most people won't miss/will get tripped up on initially. (Alt + RMB drag)
As for the smooth, I'm also trying to make it more flexible -- I really dislike having to switch the smooth brush for different behaviors, instead you can just hit space bar while smoothing to get the settings for it -- focus/falloff can be set with the (z, x) hotkeys while brush size is (a, s) then the smooth behavior is in that dropdown at the bottom. The Strength is probably the main one I was after, in ZB the smooth always feels so weak, I have to keep switching to SmoothStronger -- I plan to add a retain volume option later, I have a this already added to the pinch brush so you can slide geo toward an edge to make it crisper without editing the shape, I just need to add the option to disable it for pinch and add it into smooth. 
0 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Neox 
grand marshal polycounter 
Jun 27 2026 
Its not so much about the hotkey, ideally this can be edited to be honest.
But the functionality of the alt smooth. That is actually evening out the surface based on the surroundings, its sort of a topo smooth but not just that
@sacboi will check those settings out!
2 · Share on Facebook Share on Twitter 
Offline / 
Send Message 
Noth 
polycounter lvl 17 
Jun 27 2026 
yeah I see the difference in the geo you shared, surprised it doesn't actually get you to the nice highlight falloff -- I might try to recreate that situation and see how my smooth handles it, mine is pretty nice so far and super flexible in terms of dialing in the feel you want. 
0 · Share on Facebook Share on Twitter 
Online / 
Send Message 
iam717 
ngon master 
11:37AM 
Congrats, = What do you guys think of the logo? its cute, the play on words works for me. Looks great as a project to fulfill your needs. 
0 · Share on Facebook Share on Twitter 
Sign In or Register to comment. 
© 2026 Polycount. All image rights belong to their authors.
Terms of Service | Privacy Policy

