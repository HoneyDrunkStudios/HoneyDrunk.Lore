---
source: "https://devblogs.microsoft.com/dotnet/introducing-dotnetup"
title: "Introducing dotnetup: A toolchain manager for .NET"
author: "Chet Husk"
date_published: "2026-10-15"
date_clipped: "2026-10-16"
category: ".NET Ecosystem"
source_type: "rss"
date_modified: "2026-10-16"
---

# Introducing dotnetup: A toolchain manager for .NET

Getting started with .NET on macOS and Linux has historically meant navigating a plethora of options: system package managers like `apt` or `brew`, platform-specific tarballs, or standalone shell scripts like `dotnet-install.sh`. While those methods have served us well, they often collide with administrative permissions, leave files scattered across root directories, or make keeping multiple runtime versions side-by-side more awkward than it should be.

That’s why we’re introducing the public preview of `dotnetup`, a new .NET toolchain manager built to install, manage, and update .NET SDKs and runtimes directly in your user account.

## Why dotnetup?

If you’ve spent time in ecosystems like Rust (`rustup`) or Node (`nvm`), you’re already familiar with the power of a dedicated toolchain manager. The core goal of `dotnetup` is to drastically reduce concept count and friction when getting a .NET environment running:

* **Consistent ux**: The same commands and tools across every platform, regardless of the details of the installation
* **Non-admin by default**: Everything lives comfortably in user-owned folders, not system-owned – meaning zero need for elevated permissions.
* **Side-by-side runtime management**: Keep multiple servicing versions, preview channels, and daily builds installed at once without them stepping on each other’s toes.
* **Track intent**: Instead of managing versions, track majors or feature bands and let the tools keep you updated each month
* **Respect for project pinning**: Works seamlessly with your existing `global.json` files so team builds remain predictable and deterministic.

Let’s walk through how to get started and how to use `dotnetup` for common day-to-day tasks.

## Installing dotnetup and getting started

To get `dotnetup` on macOS or Linux, run the bootstrap script in your terminal:

**macOS (Zsh):**

```
curl -fsSL https://aka.ms/dotnetup/get-dotnetup.sh | zsh
```

**Linux (Bash):**

```
curl -fsSL https://aka.ms/dotnetup/get-dotnetup.sh | bash
```

**PowerShell (`pwsh`):**

```
irm https://aka.ms/dotnetup/get-dotnetup.ps1 | iex
```

Once the script pulls down the binary, initialize your environment:

```
dotnetup init
```

The `init` command sets up your shell profile so that `dotnet` is immediately available in your terminal sessions and fetches the latest stable .NET SDK.

[<https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/dotnetup-get-started.mp4>](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/dotnetup-get-started.mp4?_=1)

Let’s check what’s installed in our local environment:

```
dotnetup list
```

You’ll see a clean inventory of the SDKs and runtimes currently managed by `dotnetup` right in your home folder.

## Keeping runtimes fresh month-over-month

Every month the .NET team ships servicing updates with security fixes and quality improvements. Keeping your local dev machine up to date helps you build and test against those fixes. For self-contained applications, you also need to republish and redeploy with the updated runtime. Updating your machine does not patch applications you have already shipped.

When using system installs, you may not be in control of your ability to update. With `dotnetup`, staying current is a one-liner:

```
dotnetup update
```

This command resolves your tracked SDK and runtime channels again and installs the latest matching versions. For example, `10.0` tracks updates within .NET 10, while `latest` follows the latest stable SDK, including new major releases. Exact-version requirements stay pinned, so an installation requested as `10.0.3` will not advance during an update.

If you only want to install or refresh a specific runtime flavor, like the ASP.NET Core runtime on .NET 10, you can target it cleanly:

```
dotnetup runtime install aspnetcore@10.0
```

[<https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/dotnetup-update-runtimes.mp4>](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/dotnetup-update-runtimes.mp4?_=2)

After a successful update, `dotnetup` automatically removes installed components that no remaining requirement needs. Versions that another channel or exact-version requirement still needs stay installed.

When you no longer need a tracked channel or exact version, remove that requirement with the corresponding `sdk uninstall` or `runtime uninstall` command. `dotnetup` then cleans up the installations that are no longer needed. See [updating tracked installations](https://learn.microsoft.com/dotnet/core/tools/dotnetup/usecases/update-installations) for more details.

## Testing daily and preview builds

Beyond routine monthly servicing, many developers want to test bug fixes or check out new runtime capabilities before they hit stable release channels. Previously, testing a daily runtime build meant hunting down raw installer tarballs from GitHub, manually unpacking them into custom directories, and tweaking environment variables by hand.

`dotnetup` treats preview and daily builds as first-class citizens. You can install preview SDKs side-by-side with your stable setup:

```
dotnetup sdk install preview
```

[<https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/dotnetup-nightly-install.mp4>](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/10/dotnetup-nightly-install.mp4?_=3)

Or pull down the latest daily runtime build to verify an issue fix:

```
dotnetup runtime install daily
```

Or grab an entire SDK to check out the entire toolchain:

```
dotnetup sdk install daily
```

You get the flexibility to test daily builds across your user account and clean them up easily!

## Updating `dotnetup` itself

We’ll be pushing features and fixes to `dotnetup` over time, and you can get them easily:

```
dotnetup self update
```

## Common questions

Here are quick answers to a few questions you might have:

### I could do all of this with `dotnet-install.[sh|ps1]`

That’s not a question.

But yeah, you could do *most* of this with the install scripts.
What you miss out on is

* *management* of the installed SDKs and Runtimes
* signature and checksum validation of the installed SDKs and Runtimes
* faster installation of multiple SDKs and Runtimes
* a unified CLI surface for doing this on every platform

### Does dotnetup need sudo or root rights?

Nope. `dotnetup` is currently built for non-admin, user-local operation. All SDKs, runtimes, and metadata live entirely within your user directory.

In a future release we’ll be adding support for managing the system-level installs on Windows because of how prevalent those
are on that operating system.

### Can I use dotnetup in CI pipelines?

Absolutely. Because `dotnetup` doesn’t require root privileges and runs smoothly non-interactively, it’s a great fit for containerized or ephemeral CI workers where you need to spin up specific SDK or daily runtime versions on the fly.

### What’s on the roadmap for `dotnetup`?

As mentioned, we’ll be looking into support for Windows admin
installers, but we also want to integrate `dotnetup` into CI/CD systems
like GitHub Actions and Azure DevOps – ideally through replacing parts of the implementations of those tools today that rely on the dotnet-install scripts.

We also want to iterate on the user experience to better fit how
you all use the tool, and flesh out agent skills so that automated
assistants use the tooling more naturally and reach for it by default.

### Where should I go for more details?

For the full CLI reference, advanced configuration options, and deep dives, head over to the [dotnetup documentation on Microsoft Learn](https://learn.microsoft.com/dotnet/core/tools/dotnetup).

If you have feedback, run into bugs, or want to share your thoughts on the experience, please drop by the [dotnet/sdk discussions on GitHub](https://github.com/dotnet/sdk/discussions/categories/dotnetup). We’d love to hear how it works for you, or how we can make it better!
