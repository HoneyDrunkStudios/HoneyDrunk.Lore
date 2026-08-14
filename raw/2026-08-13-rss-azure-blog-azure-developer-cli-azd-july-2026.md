---
source: "https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-july-2026/"
title: "Azure Developer CLI (azd) July 2026"
author: "Azure Blog"
date_published: "2026-07-30"
date_clipped: "2026-08-13"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure Developer CLI (azd) July 2026

Source: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-july-2026/

This is the July round-up for the Azure Developer CLI ( azd ). Five releases shipped since the last post: 1.27.0 , 1.27.1 , 1.28.0 , 1.28.1 , and 1.29.0 . Below is what’s new, what changed, and what we fixed, with links to the pull requests if you want to dig in.
Have feedback or questions? Join the release discussion on GitHub .
Highlights:
A new azd tool uninstall command completes the tool install, upgrade, and uninstall lifecycle.
Extensions can install directly from a registry location with -s/--source , and skip dependency resolution with --no-dependencies .
Model Azure AI Foundry projects, agents, and related resources directly in azure.yaml .
Container deployment for Azure App Service lets you push an image and run Web App for Containers with host: appservice and language: docker .
azd automatically switches to non-interactive mode when it detects a CI/CD or AI-agent environment, so commands fail fast instead of hanging on a prompt.
Breaking change: the skill --host flag on azd tool commands is renamed to --agent .
🌐 Microsoft Foundry at the AI Engineer World’s Fair
In Pablo Castro’s (Microsoft) “On AI and Knowledge” session at the AI Engineer World’s Fair, the Microsoft Foundry team showed their command-line experience built on top of the azd extension platform. It’s a great example of what teams can deliver on the extension framework, and it’s the kind of CLI story the platform is designed to enable. Watch the demo segment on YouTube to see it in action. Thanks to the Microsoft Foundry team for building on azd !
New features
🔌 Extensions
We continued to smooth out the extension install and authoring experience across these releases.
azd extension install , azd extension upgrade , and azd extension list now accept a registry location directly with -s/--source (a URL or local path), so you no longer need to run azd extension source add first. Direct locations are validated and registered as persisted sources before resolution continues. [#8792]
Add a --no-dependencies flag to azd extension install that installs only the named extension without resolving or installing its declared dependencies. [#8927]
Expose expanded service-level env values from azure.yaml to the extension service configuration, so extensions can read the same environment values azd resolves. [#8936]
🧰 Tool management
Add the azd tool uninstall command to complete the tool install, upgrade, and uninstall lifecycle. It supports --all , --dry-run , interactive multi-select, per-agent skill removal, and --output json . [#8794]
🤖 Azure AI Foundry modeling
Add support for modeling Azure AI Foundry projects, agents, and related resources directly in azure.yaml , including $ref file includes, secure-by-default networking, and Bicep-less and Terraform-less init paths. [#8818]
🏗️ Provisioning and deployment
These changes broaden what azd can deploy and let extensions participate in provisioning validation regardless of the provider.
Add container deployment support for Azure App Service. Services configured with host: appservice and language: docker (or docker.path ) now push the container image to Azure Container Registry (ACR) and update the site’s container configuration, enabling Web App for Containers scenarios. [#8847]
Add a provider-agnostic provision validation check that runs before provisioning for every provider. Extensions with the validation-provider capability can now contribute client-side checks that run regardless of the provisioning provider (Bicep, Terraform, or an extension-provided provider), not just during Bicep local preflight. [#9019]
🤖 CI/CD and agent environments
Automatically enable non-interactive (no-prompt) mode when azd detects a continuous integration and delivery (CI/CD) or AI-agent environment, so commands fail fast with a clear error instead of hanging on a prompt. Set AZD_NON_INTERACTIVE=false to opt out. Confirmation prompts now also honor their default value when there is no more input on standard input. [#9125]
Breaking changes
The skill --host flag is now --agent . On azd tool install , azd tool upgrade , and azd tool uninstall , the --host flag is renamed to --agent . Installed skills in azd tool list --output json and azd tool check --output json now expand into one row per agent and include an agent field. Update any scripts or JSON consumers that pass --host or read the previous shape. [#9045]
🪲 Bugs fixed
Extensions and tools
Fix azd tool install azure-skills mistaking the Visual Studio Code Copilot Chat launcher stub for a working Copilot Command Line Interface (CLI) host. Host selection now uses a functional probe, so installs no longer silently no-op on macOS or get stuck on a PATH prompt on Linux. [#8805]
Fix azd tool uninstall failing for Visual Studio Code extensions that have dependents (for example, vscode-azure-tools ) and for the GitHub Copilot CLI when installed via Homebrew cask on macOS and Linux. Uninstall now detects which package manager owns the install and removes it accordingly, with guidance when a self-managed install requires manual removal. [#8875]
Fix generated azd extension install completions to offer extension IDs and .zip file paths. [#8887]
Fix azd extension install intermittently failing on Windows with an “Access is denied” error when replacing an extension executable held by a transient file lock. [#9161]
Fix concurrent extension updates to azure.yaml losing service fields by serializing project configuration writes. [#9211]
Fix and improve automatic installation of project extension requirements so azd resolves every missing provider declared or inferred from azure.yaml before project commands run, instead of failing on the first unsupported one. [#9218]
Provisioning and configuration
Fix azd env refresh for projects using extension-provided service hosts or provisioning providers, and report success when no deployment exists yet. [#9017]
Fix azure.yaml serialization writing empty project and language fields for services using code-less resource hosts such as azure.ai.project , azure.ai.connection , and microsoft.foundry ; these fields are now omitted when empty. [#8937]
Exclude deprecated models by default from the model catalog and quota prompts. [#8842]
Stop forwarding dynamic linker and loader control variables (such as LD_PRELOAD , LD_LIBRARY_PATH , LD_AUDIT , and DYLD_INSERT_LIBRARIES ) defined in an environment’s .env file into tool subprocesses like docker, npm, and python. [#8949]
Fix azd deploy for container-based Azure App Service services overwriting unrelated site configuration; the container image is now updated through the dedicated App Service configuration endpoint. [#9281]
Continuous integration and updates
Fix azd down --no-prompt hanging in CI/CD for Terraform-based projects by auto-approving the destroy when running non-interactively, and fix azd down --force failing with a backend initialization error on a fresh agent. [#9143]
Fix the azd update follow-up command to use azd version . Thanks @rguptar for the contribution! [#9083]
Other changes
Expose a service’s uses (dependency) list on the extension Software Development Kit (SDK) ServiceConfig , so extensions can read service and resource dependencies directly instead of via SetServiceConfigValue . [#8838]
Add an extension SDK helper that validates provider declarations in extension.yaml against the providers registered by extension code. [#9033]
Send Azure Resource Manager (ARM) request correlation IDs as a canonical hyphenated globally unique identifier, derived losslessly from the OpenTelemetry trace ID, instead of an undecorated 32-character string. This covers both the x-ms-correlation-request-id header on azd ‘s direct ARM calls and the ARM_CORRELATION_REQUEST_ID value passed to the Terraform AzureRM provider, aligning azd with the ARM spec and other Azure tooling. [#9141]
Stop showing the automatic azd tool first-run install prompt and periodic update notifications. Explicit azd tool commands are unchanged. [#9261]
Emit the infra.provider telemetry attribute on provision , up , and down so provisioning runs can be segmented by infrastructure provider. [#9091]
Recognize azd invocations from Microsoft Foundry Skill in the execution.environment telemetry field. [#9167]
Report the GitHub Copilot app separately from the GitHub Copilot CLI in the execution.environment telemetry field. [#9288]
Update the bundled GitHub CLI to v2.96.0. [#9245]
New docs
New and updated azd docs on Microsoft Learn:
Manage Azure development tools with azd tool (July 27) — Updated to reflect the 1.28.1 change that removes the automatic azd tool first-run install prompt and periodic update notifications, so the reference now matches the current on-demand behavior.
Configure a pipeline and push updates using Azure Pipelines (July 28) — Corrected the OpenID Connect (OIDC) and federated credential guidance for azd pipeline config with Azure DevOps, plus refreshed sample links for GitHub Actions and Azure DevOps.
Set up a Copilot cloud agent development environment (July 17) — Updated for the rebrand of “Copilot coding agent” to “cloud agent”, including file and link updates throughout the article.
azure.yaml schema reference (July 16) — Refreshed with the Azure AI Foundry azure.yaml unification changes, documenting the Microsoft Foundry hosts for modeling Foundry projects, agents, and related resources directly in azure.yaml .
New templates
Community templates help you get started faster, cover common scenarios, and show how to deploy real solutions with Azure Developer CLI.
Azure Functions Timer trigger quickstarts by Azure Functions Team , extending the Timer trigger pattern across five languages. Each sample deploys to Azure Functions Flex Consumption with azd , using managed identity and a virtual network to be secure by default:
Python : An Azure Functions Timer trigger quickstart written in Python.
JavaScript : An Azure Functions Timer trigger quickstart written in JavaScript.
TypeScript : An Azure Functions Timer trigger quickstart written in TypeScript.
Java : An Azure Functions Timer trigger quickstart written in Java.
PowerShell : An Azure Functions Timer trigger quickstart written in PowerShell.
Durable Functions fan-out/fan-in quickstarts by Azure Functions Team , demonstrating the fan-out/fan-in orchestration pattern in five languages, each deployed to Azure Functions Flex Consumption with azd , managed identity, and a virtual network:
Java : A Durable Functions fan-out/fan-in quickstart written in Java.
JavaScript : A Durable Functions fan-out/fan-in quickstart written in JavaScript.
TypeScript : A Durable Functions fan-out/fan-in quickstart written in TypeScript.
Python : A Durable Functions fan-out/fan-in quickstart written in Python.
PowerShell : A Durable Functions fan-out/fan-in quickstart written in PowerShell.
Remote Model Context Protocol (MCP) Functions samples by Azure Functions Team , showing how to build and deploy custom remote MCP servers on Azure Functions:
Remote MCP Functions with JavaScript : This scenario demonstrates how to build and deploy a custom remote MCP server to the cloud using Azure Functions and JavaScript, with built-in authentication using Microsoft Entra as the identity provider.
Long-running MCP tools using Durable Functions (.NET) : A .NET isolated Azure Functions MCP server that runs long-running MCP tools by backing them with Durable Functions and a budgeted start-and-poll pattern, deployed with azd using the Durable Task Scheduler backend and managed identity.
Azure Functions C# HTTP trigger using Azure Developer CLI (Terraform) by Azure Functions Team : An Azure Functions HTTP trigger quickstart written in C# (isolated worker) and deployed to Azure Functions Flex Consumption with azd using Terraform as the infrastructure-as-code provider, with managed identity and a virtual network for secure-by-default deployment.
mTLS with Azure API Management and Application Gateway by Ronald Bosma : A demo of mutual Transport Layer Security (mTLS) with Azure API Management and Application Gateway. It shows how to validate client certificates when calling API Management directly and when it sits behind an Application Gateway, and how to secure connections from API Management to backend systems using mTLS. Thanks Ronald Bosma for the contribution!
The Azure Developer CLI template gallery keeps growing thanks to contributions from the community. Thank you!
🙋‍♀️ New to azd?
If you’re new to the Azure Developer CLI, azd is an open-source command-line tool that helps you get your application from your local development environment to Azure faster. It provides developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor, or CI/CD.
Install azd
Explore templates: Browse the Awesome azd template gallery and AI App Templates
Learn more: Visit the official documentation and troubleshooting guide
Get help: Visit the GitHub repository to file issues or start discussions
