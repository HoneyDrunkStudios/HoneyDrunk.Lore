---
source: "https://80.lv/articles/exploring-gpu-accelerated-liquid-solver-paradigm-with-marvel-s-wolverine"
title: "Theory Accelerated's Liquid Solver Tested With Marvel's Wolverine"
author: "unknown"
date_published: "2026-06-16"
date_clipped: "2026-06-17"
category: "Technical Art & Creator Tools"
source_type: "web"
---
0

Save

Copy Link

Share

[Amber Rutherford](/author/amber-rutherford)

Senior Editor

16 June 2026

Check out Joe Raasch's R&D.

For the past week, VFX Artist Joe Raasch has been experimenting with [Paradigm](https://80.lv/articles/gpu-powered-liquid-solver-paradigm-1-0-released), the new GPU liquid solver from Theory Accelerated. Every shot shown here was rendered using Houdini's Karma, and well, even with Wolverine's healing abilities, it's going to take some time for him to recover from that.

Render times were reportedly around one minute per frame for most shots, with the water tank sequence being the most demanding at approximately three minutes per frame. Here's what the artist had to say about his experience working with Paradigm:

"It's a lot of fun. It's a plug-in for Houdini. You can source your fluids from VDBs, points, or particle networks. It runs on the GPU, so it's very fast. The downside is that I 'only' have 24 gigs of VRAM on my home computer, so there's a limit to how far I can push things.

It does all the things you'd expect a modern fluid solver to support. Variable viscosity, surface tension, and whitewater generation.

I wouldn't call myself a master of fluid sims or anything, but from what I can see, it's very cool and worth checking out. Theory Accelerated is the same people who make the Axiom pyro plug-in, so they have experience with making good production tools."

Joe Raasch also explained the workflow behind the dismemberment effect:

"For the dismemberment, I used Houdini's MPM solver. I think of it as 'particles on steroids'. You convert your geometry into points, and the points have different settings on them to mimic different materials. You could have the particles behave as if they're concrete, soil, snow, or rubber, there are a bunch of presets for different material behaviours.

I made some colliders inside his chest, and then had them rapidly fly out of him, which caused him to break apart.

I didn't quite get the look I was going for. I wanted the pieces to be rubbery and have jiggle on them. But if I made them too stiff, they wouldn't break apart at all, but if I made them not stiff at all, they behaved like grains and reduced him to a pile of sand/goo. I think I could fine-tune it more, but I just didn't want to spend a ton of time on it, and I eventually had something that was good enough.

For having the fluid emit, there's an MPM Debris Source, which spawns particles along the parts that break apart. I used that to spawn the fluid sim. That could have been fine-tuned as well. If the pieces hit the ground hard, they would break apart more, and a ton of fluid would be generated, probably too much."

If you'd like to see what else Paradigm is capable of, check out this amazing [boiling water simulation](https://80.lv/articles/this-boiling-water-simulation-looks-real-but-is-actually-3d) by Enrique De la Garza:

> View this post on Instagram
>
> [A post shared by Enrique De la Garza (@edelagarzam)](https://www.instagram.com/reel/DYr-NFNhbVL/?utm_source=ig_embed&utm_campaign=loading)

> View this post on Instagram
>
> [A post shared by Enrique De la Garza (@edelagarzam)](https://www.instagram.com/reel/DVeFoEVFGBL/?utm_source=ig_embed&utm_campaign=loading)

SideFX has [teased](https://80.lv/articles/get-a-first-look-at-houdini-22) Houdini 22, with 3D Gaussian splats as one of the release's headline features. More details are set to be revealed at the online keynote on June 22.

Don't forget to [subscribe to our Newsletter](https://80.lv/subscribe) and join our [80 Level Talent platform](https://80.lv/talent), follow us on [Twitter](https://x.com/80Level), [LinkedIn](https://www.linkedin.com/company/80-lv), [Telegram](https://t.me/LevelEightyNews), and [Instagram](https://www.instagram.com/eighty_level/), where we share breakdowns, the latest news, awesome artworks, and more.

*Are you a fan of what we do here at 80 Level? Then make sure to [**set us as a Preferred Source on Google**](https://www.google.com/preferences/source?q=80.lv) to see more of our content in your feed.*

# Subscribe to 80 Level Newsletters

Latest news, hand-picked articles, and updates

[Privacy Policy](/privacy-policy)[Terms of use](/terms-of-use)

![subscribe mail image](https://cdn.80.lv/static/images/subscribe/subscribe-mail.svg)

Keep reading

You may find these articles interesting

- [Simulating Lava Flow With Houdini's MPM Solver](/articles/simulating-lava-flow-with-houdini-s-mpm-solver)
- [Simulating Watercolor Using Houdini's COPs](/articles/simulating-watercolor-using-houdini-s-cops)

Built for Creators. Read by the Best

[Partner with 80 Level](https://80level.typeform.com/to/B8udrWL5)

### Comments

#### 0

![arrow](https://cdn.80.lv/static/icons/article/arrow-right-plain.svg)

Leave Comment

Built for Creators. Read by the Best

[Partner with 80 Level](https://80level.typeform.com/to/B8udrWL5)
