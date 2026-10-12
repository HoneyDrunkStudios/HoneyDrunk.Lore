---
source: "https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration"
title: "GitHub Copilot meets Azure Developer CLI: AI-assisted project setup and error troubleshooting"
author: "Kristen Womack"
date_published: "2026-04-21"
date_clipped: "2026-10-12"
category: "Azure & Cloud"
source_type: "rss"
---

# GitHub Copilot meets Azure Developer CLI: AI-assisted project setup and error troubleshooting

The Azure Developer CLI (`azd`) now integrates with GitHub Copilot in two ways: AI-assisted project scaffolding during `azd init` and intelligent error troubleshooting when commands fail. Both features keep you in the terminal and use Copilot’s reasoning to reduce manual work.

## Prerequisites

To use these features, you need:

* **azd 1.23.11 or later**—Run `azd version` to check, or `azd update` to get the latest
* **GitHub Copilot access**—An active GitHub Copilot subscription (Individual, Business, or Enterprise)
* **GitHub CLI (`gh`)**—`azd` automatically checks and prompts for login if needed

## Copilot-powered project setup with `azd init`

Running `azd init` now presents a “Set up with GitHub Copilot (Preview)” option. Select it, and Copilot analyzes your codebase to scaffold the project, which includes: generating `azure.yaml`, infrastructure templates, and deployment configuration based on your code’s language, framework, and dependencies.

This approach works whether you’re starting fresh or bringing an existing app to Azure. Building a new project? Copilot can help you create it from scratch with the right Azure infrastructure. Have an existing project you want to deploy? Copilot can analyze your codebase and generate the configuration needed to deploy it with `azd` with no need to rewrite or restructure your project.

Before making any changes, the flow runs preflight checks. It verifies your git working directory is clean so no uncommitted work is at risk. It also prompts for Model Context Protocol (MCP) server tool consent upfront, so you know exactly what Copilot can access before it starts.

To use Copilot-powered init:

```
azd init
# Select: "Set up with GitHub Copilot (Preview)"
```

The Copilot agent examines your project structure, proposes an `azure.yaml` configuration, and generates the necessary infrastructure files. You review and approve the changes before anything is written to disk.

### Example: scaffolding a Node.js app

Say you have an Express API with a `package.json`, a `src/` directory, and a PostgreSQL dependency. Normally you’d need to:

1. Reference the docs to determine the right `host` type (Container App vs App Service vs Function)
2. Write an `azure.yaml` with the correct `language`, `host`, and `build` settings
3. Author Bicep modules for the app, the database, and any networking

With Copilot-powered init, Copilot detects your Express framework and PostgreSQL dependency, then generates the `azure.yaml`, a Bicep module for Azure Container Apps, and a Bicep module for Azure Database for PostgreSQL, which is then ready for you to review.

## AI-assisted error troubleshooting

Deployment errors happen. A missing parameter, a permissions issue, a misconfigured resource, and, in these cases, the error message doesn’t always make the fix obvious.

### Troubleshooting with and without Copilot

Without Copilot, when `azd provision` or `azd up` fails, the steps to fix it look something like this:

1. Copy the error message from the terminal
2. Search Azure docs or Stack Overflow for the error code
3. Read through troubleshooting guides to find the relevant fix
4. Run one or more `az` CLI commands to apply the fix
5. Rerun the original `azd` command and hope it works

With Copilot, `azd` can handle that loop for you. When any `azd` command fails, it offers an interactive troubleshooting flow powered by Copilot. You can jump straight to a fix or explore the error first. You choose from four options:

* **Explain**—Get a plain-language explanation of what went wrong
* **Guidance**—Receive step-by-step instructions to fix the issue
* **Diagnose and Guide**—Get troubleshooting steps on what happened, why the error happened, and how to fix it. Let Copilot apply a fix (with your approval), then optionally retry the failed command
* **Skip**—Dismiss and handle it yourself

The troubleshooting runs entirely in your terminal. There’s no need to switch to a browser, search docs, or paste error messages into a chat window. Copilot has context about your project configuration, the command that failed, and the error details, so its suggestions are specific to your situation.

### Set a default error handling behavior

If you find yourself always choosing the same option, you can skip the interactive prompt by setting a default with `azd config`:

```
azd config set copilot.errorHandling.category troubleshoot
```

Available values for `copilot.errorHandling.category`:

| Value | Behavior |
| --- | --- |
| `explain` | Automatically get a plain-language explanation |
| `guidance` | Automatically get step-by-step fix instructions |
| `troubleshoot` | Automatically diagnose and guide |
| `fix` | Automatically apply a fix |
| `skip` | Always skip Copilot troubleshooting |

You can also enable auto-fix and retry, so Copilot applies the fix and reruns the failed command automatically:

```
azd config set copilot.errorHandling.fix allow
```

To reset to the default interactive prompt, unset the config:

```
azd config unset copilot.errorHandling.category
```

### Common Azure deployment errors where Copilot helps

Here are a few common Azure errors that developers run into and how Copilot-assisted troubleshooting turns a wall of text into an actionable fix.

#### `MissingSubscriptionRegistration`—resource provider not registered

A first-time deployment to a subscription often fails with:

```
ERROR: deployment failed: MissingSubscriptionRegistration:
The subscription is not registered to use namespace 'Microsoft.App'.
```

Azure requires resource providers to be registered before you can create certain resource types. If this Container App deployment is the first deployment in a given subscription, `Microsoft.App` isn’t registered yet. Copilot’s **Troubleshoot** option can register the provider for you and run the deployment automatically.

#### `SkuNotAvailable` / `OperationNotAllowed`—SKU or quota limits

You pick a region and hit:

```
ERROR: deployment failed: SkuNotAvailable:
The requested VM size 'Standard_D2s_v3' is not available in location 'westus'.
```

Or a quota variant:

```
ERROR: deployment failed: OperationNotAllowed:
Operation results in exceeding quota limits of Core.
Maximum allowed: 4, Current in use: 4, Additional requested: 2.
```

These errors are common when a region is capacity-constrained or your subscription hits its vCPU limit. Copilot’s **Explain** option clarifies which SKU or quota is blocked, and **Guidance** suggests alternative regions or Virtual Machine (VM) sizes that are available or shows you how to request a quota increase.

#### `StorageAccountAlreadyTaken`—globally unique name collision

```
ERROR: deployment failed: StorageAccountAlreadyTaken:
The storage account named 'myappstorage' is already taken.
```

Storage account names must be unique across all of Azure. Copilot suggests updating your Bicep parameter or `azure.yaml` environment variable with a unique name, often by appending your environment name or a random suffix, and then retrying the deployment.

## What’s next

This integration is just the beginning of Copilot features in `azd`. The team is working on deeper agent capabilities including Copilot-assisted infrastructure customization and smarter multi-service orchestration. If you want to influence what gets built next, [sign up for user research](https://aka.ms/azd-user-research-signup), reach out to us by filing an issue, or start a discussion in the repo.

## Try it out

To check your current version, run:

```
azd version
```

To update to the latest version:

```
azd update
```

For a fresh install, see [Install azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd). For more details on the March 2026 release, read the [full release blog post](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/).

## Feedback

Have questions or ideas? File an issue or start a discussion on [GitHub](https://github.com/Azure/azure-dev). Want to help shape the future of `azd`? [Sign up for user research](https://aka.ms/azd-user-research-signup).
