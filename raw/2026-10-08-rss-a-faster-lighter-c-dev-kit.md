---
"source": "https://devblogs.microsoft.com/dotnet/faster-lighter-csharp-dev-kit"
"title": "A faster, lighter C# Dev Kit"
"author": "Drew Noakes"
"date_published": "2026-10-06"
"date_clipped": "2026-10-08"
"category": ".NET Ecosystem"
"source_type": "rss"
---

We developers know just how fast computers can be, and we want to feel that speed in our tools. Waiting for language support to load, builds to complete and tests to run is time we could better spend in other ways.

As part of .NET 11, C# Dev Kit has been completely rearchitected to deliver huge improvements to performance and memory usage. It also has some great new features.

This is the first in a series of blog posts covering the improvements in C# Dev Kit 11.0. In this post we will cover the improvements at a high level, and future posts will dig into the details for those who are interested.

We are aligning C# Dev Kit’s version with the current release of .NET. The new extension version is 11.0, and the previous was 3.3.

Let’s see what’s new.

## Faster loads

We measured load times on two real solutions: [Orleans](https://github.com/dotnet/orleans) (155 projects) and [Aspire](https://github.com/dotnet/aspire) (407 projects).

| Solution | Projects | What’s ready | C# Dev Kit 3.3 | C# Dev Kit 11.0 | Faster by 🎉 |
| --- | --- | --- | --- | --- | --- |
| [dotnet/orleans](https://github.com/dotnet/orleans) | 155 | Active file | up to 50.3 s | 0.53 s | **up to 95×** |
|  |  | Whole solution | 50.3 s | 2.3 s | **22×** |
| [microsoft/aspire](https://github.com/microsoft/aspire) | 407 | Active file | up to 84.1 s | 0.47 s | **up to 180×** |
|  |  | Whole solution | 84.1 s | 3.0 s | **28×** |

The table shows two moments during load. **Active file ready** is when language support is available in the file you are editing, with completions, diagnostics, go to definition, and quick fixes. This is the point at which you can do real work. **Whole solution ready** is when every project has finished loading, so language support works in any file, tests across the solution are discovered, and find all references works across all projects.

C# Dev Kit’s new project caches contribute to this faster loading. It no longer rebuilds its understanding of every project on every open, so language services, tests, and launch targets are available almost immediately. It now loads the active file first, so you can start working there while the rest of the workspace loads in the background, with performance that’s constant, regardless of the project count. The previous implementation loaded projects in a fixed order, so load times depended on where the file fell in that order.

A project’s cache is built the first time that project is loaded. Every load after that is served from the cache, and is fast. If you commit your cache files to version control, then fresh clones and new git worktrees will have fast tooling support immediately, which is great when working with agents.

We also shortened load time by consolidating several processes into a single one. The previous version launched six managed processes that each had to pass AV checks, load images from disk, perform JIT (minimised via ReadyToRun), then connect to each other. All of this had to happen before they could answer a single question about your code.

This consolidated `CSDevKit` process is a native executable, compiled ahead-of-time using .NET’s [Native AOT](https://learn.microsoft.com/dotnet/core/deploying/native-aot/). It begins running immediately, with no runtime to load and no just-in-time compilation on the startup path.

Cached data, fewer processes, and Native AOT mean a more responsive development experience. Future posts in this series will explore those topics in more detail.

## Faster builds

C# Dev Kit 11.0 has much faster incremental builds thanks to fast up-to-date checks and Build Acceleration, two features that Visual Studio developers have had for a while.

We’ll use the 407-project Aspire solution again, building the whole solution each time.

| Changes to build | C# Dev Kit 3.3 | C# Dev Kit 11.0 | Faster by 🎉 |
| --- | --- | --- | --- |
| Nothing | 34.4 s | 0.88 s | **39×** |
| Single C# file | 36.1 s | 2.1 s | **17×** |

In 11.0 we cut the overhead of working out what changed, and of copying output files.

Build times depend on the structure of the solution, so not every build will see such huge gains. However, it is common to build only a few changes at a time, which is the scenario that sees the greatest improvement in 11.0.

The improved responsiveness is noticeable when running unit tests and when launching apps. Both of these operations perform a build before starting, so in 11.0 they complete sooner.

## Memory

The previous architecture spread C# Dev Kit’s internal services across six interconnected processes. This release consolidates those processes into a single server, compiled with Native AOT.

| Solution | Projects | C# files | C# Dev Kit 3.3 | C# Dev Kit 11.0 | Reduction 🎉 |
| --- | --- | --- | --- | --- | --- |
| [dotnet/orleans](https://github.com/dotnet/orleans) | 155 | 4,010 | 1,307 MB | 208 MB | ~84% |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | 398 | 18,153 | 2,000 MB | 379 MB | ~81% |
| [microsoft/aspire](https://github.com/microsoft/aspire) | 407 | 4,686 | 2,072 MB | 316 MB | ~85% |

Memory use tracks the size of the codebase more than the number of projects. Roslyn has around four times the C# of Aspire, so its server uses more memory even with fewer projects, while the compact project model keeps memory growing far more slowly than the code itself.

These figures represent the memory allocated by the C# Dev Kit server’s process(es). The C# language service (Roslyn) runs in its own process as before, and Visual Studio Code has its own footprint. Neither is represented in this comparison; both are largely unchanged in this release.

Version 11.0 has a more compact in-memory representation of the project, which reduces memory use considerably, especially for large solutions. Native AOT also uses less runtime memory.

## Editing projects and other MSBuild files

C# Dev Kit 11.0 includes a new editing experience for `.csproj`, `.props` and `.targets` files. You get completions, diagnostics, go to definition, quick fixes, and semantic highlighting: the same kind of language support you expect when editing C# code.

Completions are now offered for package names and versions:

[<https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/package-completion.mp4>](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/package-completion.mp4?_=1)

Packages also have a CodeLens entry that offers some convenient actions. It highlights when newer versions are available, and when the version being used has a vulnerability.

MSBuild language support is not limited to packages. Completions cover properties, items, and metadata keys. Go to definition works on several language elements, and can take you into SDK source. Diagnostics flag problems as you type, and quick fixes offer corrections.

## Health checks with the C# Doctor

Also new to C# Dev Kit is the C# Doctor.

When a project fails to load or behaves in a way you did not expect, the cause is often environmental. A required SDK is missing, a runtime is not installed, a target framework is not available, package restore failed, or a referenced package has a known vulnerability. The C# Doctor collects those checks in one place and guides you towards a good solution, rather than leaving you to reconstruct the cause from separate error messages. It simplifies getting the tooling and configuration you need to have your projects work with C# Dev Kit.

## What’s next

The role of the IDE is changing. As developers adopt new workflows, we keep finding where our tools fall short. When developing with agents, we need to get in and out of our tools much faster, and we need to be able to run multiple instances in parallel. The architectural changes we’ve made in C# Dev Kit 11.0 set the extension up for the years ahead.

These are improvements to the fundamental aspects of the tooling, which are helpful to both human developers and the agents they’re waiting for.

We are making longer-term investments in these components, looking to make them available in even more environments, driving more consistency and performance through the ecosystem. Stay tuned for updates in this space.

The next blog posts in this series will dive into the simpler architecture, the Native AOT server, cached project loading, and faster builds.

## Try it out

C# Dev Kit 11.0 is available now in pre-release, so the quickest way to see the difference is to update and open one of your own solutions. We hope you’ll find it faster and easier to use.

[Get C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)

After installing, select **Switch to Pre-Release Version** on the C# Dev Kit page in the Extensions view to opt into the pre-release channel and see these improvements.

We’re working hard to get it ready for release on the stable channel, and your feedback will help shape that effort. You can file bugs and suggestions [on GitHub](https://github.com/microsoft/vscode-dotnettools).
