---
source: "https://devblogs.microsoft.com/dotnet/delivering-skills-in-nuget-packages"
title: "Delivering Skills in NuGet packages"
author: "Richard Lander"
date_published: "2026-11-03"
date_clipped: "2026-11-05"
category: ".NET Ecosystem"
source_type: "rss"
canonical_url: "https://devblogs.microsoft.com/dotnet/delivering-skills-in-nuget-packages/"
source_last_modified: "2026-11-04"
---

# Delivering Skills in NuGet packages

Agent skills were [introduced by Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) in 2025 and have quickly become commonplace for AI-driven development. [dotnet/skills](https://github.com/dotnet/skills) and [Impeccable skills](https://impeccable.style/) are good examples. Agent skills are typically distributed via git repos. We’ve been working on skill delivery via NuGet packages and found that the approach can be effective. The common thread is that repos and packages are units of development that can be used as distribution vehicles for skills.

Skills solve two main problems: fill in gaps in model knowledge and can prescribe “our way” of approaching a task. New NuGet packages will always be ahead of model training and can benefit from just-in-time skill delivery.

Here’s a quick demo using the [markout](https://www.nuget.org/packages/Markout) package, whch contains a set of skills:

```
$ dotnet-inspect package markout -S Skills
path    size
skills/markout-built-in-shapes/SKILL.md 9457
skills/markout-composite-cells-cards/SKILL.md   6764
skills/markout-conditional-composition/SKILL.md 4978
skills/markout-output-formats/SKILL.md  7744
skills/markout/SKILL.md 8551
```

## Baseline

We’ve done a lot of experimentation. We’ve found that agents (as a baseline behavior) are capable of finding content in the NuGet cache to learn about a package. This includes reading `README.md` files and even writing throwaway programs that reflect over assembly metadata. Agents using frontier models are [impressively creative](https://avelarder.blog/2026/02/25/i-am-a-sad-lobster-now-the-day-an-ai-built-its-own-curl/) and can derive surpising insight, although not necessarily cheaply.

The fundamental question is whether they apply that creativity and capability to reverse-engineering documentation from metadata or working on your actual business problem. We sometimes say “why not both?”. It’s tough when you’re usage has to fit within a monthly token budget.

This is the problem we set out to solve.

## SKILL.md

Skills are markdown files with a YAML header, named `SKILL.md`. [agentskills.io](https://agentskills.io/) is the official spec site for the format. NuGet-delivered skills use the same format.

The following example skill can be used to direct agents to run vulnerability checks on project dependencies.

````
---
name: vulnerable-nuget-package-check
description: Check a .NET project for vulnerable NuGet packages dependencies.
---

The .NET SDK includes a `dotnet package` command, which can list vulnerable direct or indirect package dependencies for a given .NET project.

Run the following command for a project:

```bash
dotnet package list --vulnerable --include-transitive
```

Update vulnerable package references to patched versions.
````

## Conventional delivery

Skills are distributed via git repos, in one of two ways.

The most common approach is to include skills in a typical “code” repo. This approach is a great starting point since everyone working on the repo gets the same experience. Skill composition changes with a PR workflow that the team can review or even revert. The [dotnet/runtime repo](https://github.com/dotnet/runtime/tree/main/.github/skills) uses this approach. It is a great experience working on that repo and seeing a variety of skills automatically used by Copilot depending on prompts.

The other primary approach is skill [marketplace repos](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace), such as [dotnet/skills](https://github.com/dotnet/skills). These repos advertise their skills via [marketplace.json](https://github.com/dotnet/skills/blob/main/.agents/plugins/marketplace.json). Users install the marketplace via `/plugin marketplace add dotnet/skills` (or similar). `add` is just a wrapper on `git clone`. That means a skill marketplace repo should be small.

The advantage of putting skills directly in your repo is that the skills are always there. A good example is using the [Copilot Web Agent](https://github.com/copilot). Locally installed marketplace skills don’t exist off of your machine unless you take the extra step of committing them to your repo. Neither is better or worse, just different options.

## NuGet-package delivery

NuGet packages present a challenge and opportunity for agents. The challenge is that a new package version with new APIs published five minutes ago isn’t part of the model. The opportunity is that updated skills can be co-located with updated binaries. That means that every version of a NuGet package can have perfectly-tailored skills for their use. It’s very similar to package-resident `README.md` files, which are intended for a different purpose and consumer.

The challenge isn’t limited to packages published in the last five minutes. Package registries also have a very long tail. It’s quite likely models know nothing substantive about most packages.

`dotnet restore` already pulls packages to your machine to acquire libraries. That means that package-resident `SKILL.md` files will be on your machine as well.

You can see [markout](https://www.nuget.org/packages/Markout) package skills on my machine.

```
$ pwd
/Users/rich/git/dotnet-inspect/src/DotnetInspect.Cli
$ dotnet build
$ cat ../../artifacts/obj/dotnet-inspect/project.assets.json | grep SKILL.md
        "skills/markout-built-in-shapes/SKILL.md",
        "skills/markout-composite-cells-cards/SKILL.md",
        "skills/markout-conditional-composition/SKILL.md",
        "skills/markout-output-formats/SKILL.md",
        "skills/markout/SKILL.md",
$ find ~/.nuget/packages/markout/0.40.0/ | grep SKILL.md
/Users/rich/.nuget/packages/markout/0.40.0/skills/markout-conditional-composition/SKILL.md
/Users/rich/.nuget/packages/markout/0.40.0/skills/markout/SKILL.md
/Users/rich/.nuget/packages/markout/0.40.0/skills/markout-composite-cells-cards/SKILL.md
/Users/rich/.nuget/packages/markout/0.40.0/skills/markout-built-in-shapes/SKILL.md
/Users/rich/.nuget/packages/markout/0.40.0/skills/markout-output-formats/SKILL.md
$ head -6 /Users/rich/.nuget/packages/markout/0.40.0/skills/markout/SKILL.md
---
name: markout
version: 0.40.0
description: >-
  Use when generating Markdown or other structured output (plain text, ANSI, pretty tables,
  TSV/JSONL) from C# objects, or when diagnosing Markout source-generator errors such as
```

That’s a pretty good start and quite workable for agents. Package skills are listed in `project.assets.json` making it easy to determine if there are any skills available in a given package graph. However, we wanted to offer better UX than that.

We’ve been working on a few tools for discovering `SKILL.md` files.

### dotnet-inspect

The following are example workflows with [`dotnet-inspect`](https://www.nuget.org/packages/dotnet-inspect):

Requesting skills in a package graph:

```
$ dotnet-inspect package markout -S Skills
path    size
skills/markout-built-in-shapes/SKILL.md 9457
skills/markout-composite-cells-cards/SKILL.md   6764
skills/markout-conditional-composition/SKILL.md 4978
skills/markout-output-formats/SKILL.md  7744
skills/markout/SKILL.md 8551
$ dotnet-inspect package markout -S Skills --row 4 --print -12
---
name: markout-output-formats
version: 0.40.1
description: >-
  Use when you need output other than default Markdown — plain text / Unicode, ANSI terminal
  (Spectre), pretty aligned tables, or TSV/JSONL exports — or when one model must serve several
  formats from a single render path (a CLI `--format` switch). Also covers semantic inline code
  that renders as Markdown code spans but decodes to plain text in TSV/JSONL. Pick the format with
  a formatter + MarkoutWriterOptions; never hand-build TSV/JSONL.
  Don't decompile the assembly or web-search the API — the multi-format idioms are all here.
---
```

It can also accept a project file as input:

```
$ dotnet new console
$ dotnet package add Mockly
$ ls *.csproj
scratch.csproj
$ dotnet-inspect project scratch.csproj -S Skills
## Skills

Valid Agent Skills documents from direct package dependencies.

| Package | Version | Path | Size | Name | Description |
| ------- | ------- | ---- | ---- | ---- | ----------- |
| Mockly | 1.13.0 | skills/mockly/SKILL.md | 7409 | mockly | Helps write tests using Mockly — a fluent HTTP mocking library for .NET that intercepts HttpClient calls. Use this skill when writing unit or integration tests that need to mock HTTP requests, configure responses (status codes, JSON, OData, raw content), match headers, capture and inspect requests, limit mock invocations, or assert HTTP interactions with FluentAssertions. |
```

The intended UX with `dotnet-inspect` is that an agent can determine the set of skills available via a project file or directly from the registry. The agent can print those directly to its context or to a file. The file can then be searched or even stored in the repo.

### dotnet-package-skills

[dotnet-package-skills](https://www.nuget.org/packages/dotnet-package-skills) is another tool that is focused on storing skills in a repo.

```
$ dotnet-package-skills install
Source:      /Users/rich/git/dotnet-inspect/dotnet-inspect.slnx
NuGet global-packages directory: /Users/rich/.nuget/packages/
Destination: /Users/rich/git/dotnet-inspect/.agents/skills
Scanned 23 packages (direct).

Copied 5 skills:
  markout (Markout 0.40.1)
  markout-built-in-shapes (Markout 0.40.1)
  markout-composite-cells-cards (Markout 0.40.1)
  markout-conditional-composition (Markout 0.40.1)
  markout-output-formats (Markout 0.40.1)

Ignored 22 packages without valid bundled skills
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .agents/

nothing added to commit but untracked files present (use "git add" to track)
$ git add .
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .agents/skills/.dotnet-package-skills.json
        new file:   .agents/skills/markout-built-in-shapes/SKILL.md
        new file:   .agents/skills/markout-composite-cells-cards/SKILL.md
        new file:   .agents/skills/markout-conditional-composition/SKILL.md
        new file:   .agents/skills/markout-output-formats/SKILL.md
        new file:   .agents/skills/markout/SKILL.md
```

This is an easy way to add skills into your repo and to ensure that they are always available. It is up to you to ensure that the skills stay up to date as matching `PackageRef` entries are udpated. It might be useful to write a skill to do both at the same time.

### NuGet MCP

[NuGet MCP](https://learn.microsoft.com/nuget/concepts/nuget-mcp-server) is a useful tool for giving agents a deep and broad undertanding of NuGet, both for your local project and of your registry. It hasn’t yet been updated for skills. That’s a project we intend to take on soon.

## Learnings

Package-delivered skills are not a special kind of skill. As already stated, skills can already be delivered in multiple ways. Packages are a variation on a theme using the same format. That means that conventional skill eval applies.

Agent skills can be boiled down to delivering two benefits: efficacy (ability to deliver right answers) and efficiency (deliver answers cheaply). That doesn’t mean that agent skills *always* deliver efficacy and efficiency benefits. They *can* deliver those benefits. They can also deliver the opposite if they are badly written or tested.

The challenge with models is that cost is a major factor. If I include a `SKILL.md` in my package and your agent costs increase, that’s bad. That means that maintainers need to perform skill eval. Maintainers should improve or remove skills that their users report as ineffective or costly.

With frontier models, we didn’t find much room to improve efficacy, due to creative capability. With weaker models, we observed significant efficacy underperformance and variability due to lower skill compliance.

We used [Pareto efficiency](https://en.wikipedia.org/wiki/Pareto_efficiency) as a corrective tool for our efforts. Basic idea: “Do no harm”. Our early thinking was using skills to bring “mini”-level models up to frontier. That’s a nice idea, but not generally practical in our experience. The challenge is that one set of skills is delivered to all models. Improving efficiency for Anthropic Haiku by 50% but reducing it for Opus by 10% is a bad trade. You’ve made agent work more expensive for your Opus users and Opus tokens cost a lot more. Your Opus users would be right to complain.

Our primary focus has been testing with frontier models as a result. Testing only with cheap models (as attractive as that might be) is considered (by our findings) an anti-pattern and is not advised.

## Next Steps

We’re working on guidance for maintainers. Maintainers already familiar with skill eval will be a step ahead. Skills delivered via NuGet packages don’t change much. Our focus is figuring out how to deliver high-quality skills on a budget. This includes determining if skills deliver value.

Maintainers have been delivering markdown with packages for a long time. It’s always been an inert asset. Agents change that. We need to update safety guidance for consumers. The same guidance applies as before: “only use packages from maintainers you trust”. Agent consumption of markdown adds a new [threat vector](https://the-agent-report.com/2026/05/protestware-coding-agents-jqwik-supply-chain/) that needs to be considered.

Skill-delivery is an important new option for NuGet packages. We believe it offers the opportunity to make packages self-documenting and efficient to integrate into an app.
