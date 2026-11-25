---
source: "https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/"
title: "Project Setup: What’s In and What’s Next"
author: "Anastasia Rudina"
date_published: "2026-11-13"
date_clipped: "2026-11-24"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Project Setup: What’s In and What’s Next

Source: https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/

Blender’s preferences used to be shared across all projects, and it was up to users and teams to keep related files and resources tidy and organized.

Blender 5.3 introduces Project Setup, an opt-in system that lets users define settings, asset libraries and shared variables unique to each project they work on.

> Employee of the month [pic.twitter.com/rkQlmx8JTy](https://t.co/rkQlmx8JTy)
>
> — Momo (@momodraws) [November 11, 2026](https://x.com/momodraws/status/2120569588450812261?ref_src=twsrc%5Etfw)

[## What is a project?](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#what-is-a-project)

A project is a root directory that groups related files, lets them share resources, and keeps its settings separate from other projects. The root directory is identified by there being a `.blender_project` folder inside it, which contains a configuration file (`project.toml`) created and managed by Blender.

When you open a `.blend` file, Blender searches up the `.blend` file’s folder tree for a `.blender_project folder`. If it finds one, that project becomes active. Otherwise it considers the current session to not be part of a project.

It is also possible to open a project by either supplying a folder path to Blender on startup that lies within a project. I.E. `blender /path/to/my/project`. This can be done from within Blender itself via the File > Project > Open menu.

[![](https://code.blender.org/wp-content/uploads/2026/11/projects_menu_file-1135x1280-1-908x1024.webp?x95207)](https://code.blender.org/wp-content/uploads/2026/11/projects_menu_file-1135x1280-1.webp?x95207)

The new **File** → **Project** menu, to create, open and access projects.

Project system design principles establish that project settings always take precedence over user preferences (I.E. asset libraries and add-ons are available). Also, the project settings themselves are built to be easy to read and edit as plain files. That way they can be created or edited by external scripts and diffed or tracked in version control along with the rest of the production.

[## **What’s in Blender 5.3**](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#whats-in-blender-53)
[### **Project variables and path templates**](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#project-variables-and-path-templates)

Output file paths can now use the `{project_root}` and `{project_name}` variables, so references stay valid when the project folder moves to another drive, another machine or another artist’s computer without having to use `.blend` file relative paths everywhere.

Users can also define **custom project variables**, such as a character name, a sequence code or a frequently used folder, and use them in path templates across the project. Change a value once, and every path that uses it follows.

[### ****Per-project asset libraries****](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#per-project-asset-libraries)

Each project can define its own asset libraries. When you work inside the project, its assets appear alongside your other asset libraries, in the Asset Browser, the Asset Shelves and the Add menus.

[### ******Per-project color management******](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#per-project-color-management)

A project sets its own OpenColorIO configuration: the default Blender configuration, ACES 1.3, ACES 2.0, or a custom one. Everyone working on the project gets the same color pipeline, without having to change their preferences when switching between different projects.

[### **A custom splash screen**](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#a-custom-splash-screen)

Projects can have custom splash artwork. The splash screen also lists recent files from the same project, so it’s easy to navigate among frequently used files.

[![](https://code.blender.org/wp-content/uploads/2026/11/projects_splash_blender53-1-1280x1108-1-1024x886.webp?x95207)](https://code.blender.org/wp-content/uploads/2026/11/projects_splash_blender53-1-1280x1108-1.webp?x95207)

Project-specific splash and color management configuration.

[## ****What’s next****](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#whats-next)

Work continues in Blender 5.4. You can follow the progress in the [Project Setup 5.4 targets task](https://projects.blender.org/blender/blender/issues/166064).

[### **Per-project extension repo folder**](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#per-project-extension-repo-folder)

The top priority for Blender 5.4 is letting a project ship its own add-ons (extension repo) folder, equipping everyone working on the project with the same tools. Add-on settings can be defined per project, so the same add-on can have different settings in different projects.

[### ****Variables on (almost) every path****](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#variables-on-almost-every-path)

Path templates and project variables are much less useful if only some fields accept them. The ultimate goal is to support them on (nearly) all paths in Blender. Built-in variables such as `{project_root}` should be also shown in the project’s Variables list for discoverability.

[### ******Multi-project workflows******](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#multi-project-workflows)

Several smaller improvements are planned for those who move between projects:

- A project selector in the File Browser
- Limiting **Save As** to the current project
- Keeping variables unresolved when using **Save As Copy**, so paths in the copy stay live

Core

[## [Project Setup](https://fund.blender.org/?roadmap_project=project-setup)](https://code.blender.org/2026/11/project-setup-whats-in-and-whats-next/#project-setup)
[![](https://code.blender.org/wp-content/uploads/2026/11/spring-project-compressed.png?x95207)](https://fund.blender.org/?roadmap_project=project-setup)

Shared “project” environment for different blend-files.

[See more roadmap projects](https://www.blender.org/roadmap/)

---
