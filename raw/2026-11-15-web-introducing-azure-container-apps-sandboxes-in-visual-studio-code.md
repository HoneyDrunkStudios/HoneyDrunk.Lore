---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-sandboxes-in-visual-studio-code/4573296"
title: "Introducing Azure Container Apps Sandboxes in Visual Studio Code"
author: "Fiveisprime"
date_published: "2026-11-13"
date_clipped: "2026-11-15"
category: "Azure & Cloud"
source_type: "web"
---

# Introducing Azure Container Apps Sandboxes in Visual Studio Code

## Create a sandbox, run a command, take a snapshot, and manage its lifecycle without leaving your editor.

We're introducing support for **Azure Container Apps Sandboxes in the Azure Container Apps extension for Visual Studio Code**. The new experience brings sandbox groups and individual sandboxes into the Azure Resources view, putting everyday sandbox operations alongside your development workflow.

Instead of switching tools to create and manage sandbox resources, you can work with them directly in VS Code, see their current state, and follow operation results in the Azure output channel.

## Your sandboxes, alongside your code

The new **Container Apps Sandboxes** node gives sandbox resources a dedicated home in the Azure Resources tree. Expand a sandbox group to find its sandboxes and see status labels such as **Running** and **Stopped**.

Start with **Create Sandbox Group...** and follow the guided workflow, including choosing an existing resource group or creating a new one. Once your sandbox group appears in the tree, right-click it and select **Create Sandbox...** to create a sandbox within that group.

The result is a straightforward path from creating a group to working with a running sandbox, all from your editor.

## Execute commands without switching tools

With **Execute Command in Sandbox...**, you can run a command against a sandbox directly from VS Code. This brings command execution into the same resource-management experience you use to find and inspect your sandboxes.

*Enter a command to run in the sandbox without leaving VS Code.*

The Azure output channel reports operation results, helping you keep track of what happened without leaving the editor.

## Create named snapshots

Use **Snapshot Sandbox...** to create a named snapshot of a sandbox. Snapshot creation is available alongside the other sandbox actions, so you can create a snapshot as part of your workflow rather than switching to a separate management tool.

*Give your snapshot a name directly in the editor.*

## Stop and resume from the resource tree

Sandbox lifecycle controls are available directly in the extension:

- **Stop Sandbox** to stop a running sandbox.
- **Resume Sandbox** to resume a stopped sandbox.
- **Delete Sandbox** to remove a sandbox you no longer need.

Inline status labels make it easy to see the transition between running and stopped states. Operation results also appear in the Azure output channel.

*Access sandbox actions from the resource tree.*

Sandbox groups include familiar management actions such as **Edit Tags...**, **View Properties**, **Open in Portal**, and **Refresh**, as well as an option to delete a sandbox group.

## Get started

To explore the new experience:

1. Install or update the [Azure Container Apps extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurecontainerapps) to a release that includes Sandbox support, then sign in to Azure.
2. Open the Azure Resources view and find **Container Apps Sandboxes** under your subscription.
3. Use **Create Sandbox Group...** and follow the prompts to create a group.
4. Right-click the group and select **Create Sandbox...**.
5. Explore command execution, named snapshots, and stop/resume controls from your sandbox's available actions.

**Less context switching. More time in your development workflow.** Azure Container Apps Sandbox support brings creation and day-to-day management into VS Code, right where you're already working.

Have feedback? Share it in the [Azure Container Apps extension repository](https://github.com/microsoft/vscode-azurecontainerapps/issues).
