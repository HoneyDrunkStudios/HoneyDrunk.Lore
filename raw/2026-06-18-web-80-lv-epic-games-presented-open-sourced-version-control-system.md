---
source: "https://80.lv/articles/epic-games-presented-its-open-sourced-version-control-system"
title: "Epic Games Presented Open-Sourced Version Control System"
author: "80 Level"
date_published: "2026-06-18"
date_clipped: "2026-06-18"
category: "Game Development / Unity"
source_type: "web"
---

# Epic Games Presented Open-Sourced Version Control System

Source: https://80.lv/articles/epic-games-presented-its-open-sourced-version-control-system

Gloria Levine Senior Editor 18 June 2026 Epic Games Presented Its Open-Sourced Version Control System # News # Unreal Engine # Game Development Lore is optimized for projects that combine code with large binary assets.
Epic Games State of Unreal unveiled more details about Unreal Engine 6 , but this and UE 5.8 are not the only exciting news Epic Games prepared. The company behind Fortnite released Lore, its open-source version control system that any game developer or other entertainment studio can benefit from.
Lore optimized for projects that combine code with large binary assets. Epic promises an easy setup and vast scalability, with the ability to extend, customize, and integrate the system via C/C++, C#, Rust, Go, Python, or JavaScript.
"Lore is a centralized, content-addressed version control system that represents repository state as Merkle trees and an immutable revision chain, optimized for binary-first storage, deduplication, and sparse/on-demand data hydration at scale."
You might wonder what makes it different from other systems, such as Git. Epic Games says that no other system was designed "for the combination of constraints that large game and entertainment projects require: arbitrary content types, multi-axis scale, multi-tenant safety, and a fully open specification and license."
"Git’s content-addressed revision graph is excellent, but it treats binary files as second-class citizens—large files require bolted-on LFS rather than first-class chunked storage, sparse checkouts have sharp edges in offline use, and there is no native multi-tenant isolation."
Meanwhile, systems designed for large binary content "typically require server round trips for everyday operations, use proprietary wire protocols that foreclose third-party implementation, and offer limited deduplication at the binary level."
Lore solves all these problems and offers a convenient tool that other developers can improve further.
For now, Epic is planning to add expanded large-repository workflows like VFS and Windows Service, OAuth integration, scalable locking, multi-server replication, client and server-side hooks, a VS Code plugin, and an open-source desktop and web client.
Lore is available on Windows, macOS (ARM64), and Linux (x86-64, ARM64).
Don't forget to   subscribe to our Newsletter  and join our  80 Level Talent platform , follow us on  Twitter ,  LinkedIn ,  Telegram , and  Instagram , where we share breakdowns, the latest news, awesome artworks, and more.
Are you a fan of what we do here at 80 Level? Then make sure to  set us as a Preferred Source on Google  to see more of our content in your feed.
Keep reading
You may find these articles interesting
Unreal Engine 5.8 is Out Today With Big Optimization Improvements and Mesh Terrain
Unreal Engine 6 Will Combine UEFN and UE Into a "Unified Engine"
Built for Creators. Read by the Best Partner with 80 Level Comments 0 Type your comment here Leave Comment Built for Creators. Read by the Best Partner with 80 Level
