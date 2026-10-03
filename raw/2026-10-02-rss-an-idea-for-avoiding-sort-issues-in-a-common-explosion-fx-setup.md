---
source: "https://realtimevfx.com/t/an-idea-for-avoiding-sort-issues-in-a-common-explosion-fx-setup/31785"
title: "An Idea for Avoiding Sort Issues in a Common Explosion FX Setup"
author: "gaonpapa"
date_published: "2026-10-01"
date_clipped: "2026-10-02"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# An Idea for Avoiding Sort Issues in a Common Explosion FX Setup

An Idea for Avoiding Sort Issues in a Common Explosion FX Setup

Let’s assume the **shockwave is red** and the **explosion is blue**.

If the red shockwave has a Sort value of **1** and the blue explosion has a Sort value of **0**, or vice versa, where the red is **0** and the blue is **1**,

it can cause unwanted visual interference between the two effects.



So, I came up with an idea to separate the ring-shaped shockwave into **front and back sections relative to the camera**.

I divided the ring-shaped resource into two halves based on the camera position, and then selectively killed the particles so that one half exists in front of the camera-facing side and the other half exists behind it.


With this setup, if the final Sort order is:

**Red = 2 → Blue = 1 → Green = 0**

the resources are sorted in a consistent order, which prevents them from visually interfering with each other.



This is the approach I came up with so far.

If there are more effective ways to handle this kind of sorting issue, I’d love to hear your ideas and share solutions so we can improve the technique together.

Thank you!
