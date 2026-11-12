---
source: "https://devblogs.microsoft.com/dotnet/modernize-dotnet-apps-for-windows-arm64"
title: "Modernize your .NET apps for Windows Arm64 with GitHub Copilot"
author: "Mika Dumont"
date_published: "2026-11-05"
date_clipped: "2026-11-12"
category: ".NET Ecosystem"
source_type: "web"
---

# Modernize your .NET apps for Windows Arm64 with GitHub Copilot

Arm64 offers the potential for lower compute costs and more efficient infrastructure. But what would it take to get your existing .NET application running on it?

The answer may be scattered across your code, dependencies, and build settings. You need to know what already supports Arm64, what needs updating, and how much work is involved. Finding those answers by hand can become a project of its own.

The GitHub Copilot upgrade agent helps you move from those questions to concrete changes. It assesses your .NET projects for migration from Windows x64 or x86 to Windows Arm64, identifies blockers, creates a migration plan, and helps update your code, dependencies, and configuration.

## Understand what is blocking your migration

An x64 build setting is easy to spot. A package that quietly depends on a native library without an Arm64 binary can take more digging. Before you migrate, you need to know where those assumptions show up in your application.

Common blockers include:

- Code and build settings tied to a specific architecture
- Native dependencies that do not provide Arm64 binaries
- Packages or libraries that need versions compatible with Arm64
- Platform assumptions spread across multiple projects
- Configuration that targets only x64 or x86 environments

The upgrade agent helps with that investigation, assessing your .NET projects and identifying the work needed to move from Windows x64 or x86 to Windows Arm64.

## Move from assessment to working code

The upgrade agent doesn’t stop at telling you what needs to change. It creates a migration plan and gets to work on the code, dependencies, and project settings, bringing you in when a step needs your input.

The agent can:

1. Analyze the application and its dependencies for Arm64 compatibility.
2. Identify assumptions tied to a specific architecture and unsupported components.
3. Create a migration plan based on the codebase.
4. Help update code, dependencies, and project configuration.
5. Build the migrated components for Windows Arm64 and, when matching hardware or CI runners are available, execute tests to help validate runtime behavior.

You can review the plan and proposed changes as the agent works. A successful build is an important checkpoint, but testing on Windows Arm64 is still needed to validate runtime behavior.

The agent takes on migration tasks while your team reviews the changes and makes decisions that need your expertise.

## Focused on compatibility

This scenario focuses on portability and correctness when migrating .NET applications to Windows Arm64, not performance tuning specific to Arm64.

Once you’ve validated your application on Windows Arm64, you can measure how it performs in your own environment and decide whether your workload would benefit from additional tuning.

## Get started

Arm64 migration is available in the GitHub Copilot upgrade agent.

To begin:

1. [Install GitHub Copilot upgrade](https://learn.microsoft.com/dotnet/core/porting/github-copilot-upgrade/install?pivots=github-com) in your preferred development environment.
2. Select the upgrade agent from the agent picker and tell it you want to migrate your .NET application to Windows Arm64.
3. Select the .NET Arm64 migration scenario when prompted.
4. Review the assessment and proposed migration plan.
5. Let the agent make the changes, reviewing its updates and completing any steps that need your input.
6. Validate runtime behavior on Windows Arm64 hardware or CI runners.

Give it a try with your .NET application. We’d love to hear how it goes and what you’d like to see next.

To learn more about the GitHub Copilot upgrade agent and explore other supported modernization scenarios, visit [aka.ms/upgrade-agent](https://aka.ms/upgrade-agent).
