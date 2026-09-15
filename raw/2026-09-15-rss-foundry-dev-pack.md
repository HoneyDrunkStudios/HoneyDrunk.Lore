---
source: "https://devblogs.microsoft.com/foundry/foundry-devpack-announcement/"
title: "Introducing Foundry Dev Pack: One Command to Start Building on Microsoft Foundry"
author: "sharonxu"
date_published: "2026-09-15"
date_clipped: "2026-09-15"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
---

# Introducing Foundry Dev Pack: One Command to Start Building on Microsoft Foundry

Source: [Introducing Foundry Dev Pack: One Command to Start Building on Microsoft Foundry](https://devblogs.microsoft.com/foundry/foundry-devpack-announcement/)

## Attributed content summary

Microsoft introduces Foundry Dev Pack as a consolidated environment installer. Its components include Azure CLI, Azure Developer CLI, the Foundry extension for azd, and reusable guidance for coding agents. Editor integrations are conditional: the VS Code toolkit is installed when VS Code is present, and the guided hosted-agent integration depends on GitHub Copilot App being present.

The article supplies installation paths for Windows, macOS, and Linux. On Windows it identifies the winget package Microsoft.FoundryDevPack. After setup, the CLI entry point for a template-based agent is azd ai agent init; editor and coding-agent workflows provide alternatives.

This is actionable onboarding material for standardizing Foundry development machines. It describes installing a toolchain, not an application's complete Azure configuration or production readiness. Validate the selected components and resulting versions against the intended development environment before making the installer part of a reproducible setup process.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
