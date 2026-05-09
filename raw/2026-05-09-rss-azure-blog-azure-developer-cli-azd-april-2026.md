---
source: "https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/"
title: "Azure Developer CLI (azd) – April 2026"
author: "Azure Blog"
date_published: "Fri, 01 May 2026 00:53:08 +0000"
date_clipped: "2026-05-09"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure Developer CLI (azd) – April 2026

Source: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/

The Azure Developer CLI ( azd ) shipped five releases in April 2026. The biggest theme this month is multi-language hook support: write azd hooks in Python, JavaScript, TypeScript, or .NET alongside the existing Bash and PowerShell options. Here’s what’s in versions 1.23.14 , 1.23.15 , 1.24.0 , 1.24.1 , and 1.24.2 .
To share your feedback and questions, join the April release discussion on GitHub .
Highlights: 
Security improvements including Windows MSI code-signing verification and an environment variable leak fix in extension commands (update azd version) 
Write hooks in Python, JavaScript, TypeScript, and .NET with automatic dependency management 
AI model quota preflight check catches quota issues before provisioning 
azd update graduates to public preview, so you can update with a single command on any platform 
Custom provisioning providers let extension authors plug in alternative infrastructure backends 
Standardized --no-prompt behavior for reliable automation in CI/CD pipelines and AI agents 
New features 
🪝 Multi-language hooks 
Hooks in azure.yaml now support Python, JavaScript, TypeScript, and .NET scripts, alongside the existing Bash and PowerShell options. Each language gets automatic dependency installation and runtime management. Read more in Write azd hooks in Python, JavaScript, TypeScript, or .NET .
Python hooks : Point a hook to a .py script and azd detects it automatically. When requirements.txt or pyproject.toml is present, a virtual environment is created and dependencies are installed before execution. [#7451] 
JavaScript and TypeScript hooks : Point a hook to a .js or .ts script for automatic detection. When package.json is present, azd runs npm install first. TypeScript scripts execute through npx tsx with no compile step required. [#7626] 
.NET hooks : Point a hook to a .cs file and azd executes it with dotnet run , with automatic project discovery and support for single-file scripts on .NET 10+. [#7652] 
Executor-specific configuration : A new config: block for hooks in azure.yaml lets you configure packageManager for JavaScript/TypeScript hooks, virtualEnvName for Python hooks, and configuration / framework for .NET hooks. [#7690] 
Per-layer hooks : Hooks defined under infra.layers[].hooks now execute during azd provision , and azd hooks run supports a new --layer flag for targeted execution. [#7382] 
🔌 Extension Framework 
The Extension Framework (currently in Beta , while azd itself is GA) gains new capabilities for extension authors and a smoother upgrade experience for users.
Custom provisioning providers : Extension authors can register alternative infrastructure providers through WithProvisioningProvider("name", factory) on the ExtensionHost . Users set infra: { provider: name } in azure.yaml to use them. [#7482] 
Smarter extension upgrades : azd extension upgrade now resolves the installed source by default, automatically promotes extensions from a dev registry to the main registry when a newer version is available, and processes --all or --no-prompt batch upgrades non-interactively. [#7841] 
Key Vault secret resolver : The extension framework automatically resolves @Microsoft.KeyVault(...) references in environment variables before passing them to extensions. [#7043] 
🤖 AI and Copilot 
AI model quota preflight check : azd provision now detects Azure Cognitive Services model deployments in the Bicep snapshot and validates quota availability before provisioning, warning on exceeded quota or unrecognized model names. [#7672] 
“Fix this error” in Copilot troubleshooting : The Copilot-assisted error troubleshooting flow adds a “Fix this error” option, allowing the agent to directly apply a fix and collect user feedback. Read more in GitHub Copilot meets Azure Developer CLI: AI-assisted project setup and error troubleshooting . [#7401] 
Improved AI model capacity resolution : The PromptLocation extension framework API adds an allowed_locations filter, and AI model capacity resolution falls back to the highest valid capacity within remaining quota. [#7397] 
🚀 Project setup and initialization 
.azdignore for templates : Template authors can create a .azdignore file in the template root to exclude contributor-only files (such as SECURITY.md , .github/ ) from being copied to consumer projects. [#7685] 
.azdxignore for watch mode : Create a .azdxignore file in the project root (gitignore syntax) to exclude directories such as node_modules/ and dist/ from triggering unnecessary rebuilds during azd x watch . [#7697] 
⚙️ Preflight validation 
Reserved-name preflight check : azd provision now warns before deploying when predicted resource names contain Azure reserved words (such as names with MICROSOFT , WINDOWS , or prefixed with LOGIN ), with color-highlighted output. The check correctly skips Azure Resource Manager (ARM) allow-listed resource types (such as Private Link DNS zones, resource groups, and role assignments) that accept reserved names server-side. [#7746] [#7819] 
🔧 Developer experience 
azd update public preview : azd update no longer requires an alpha feature flag and displays a preview notice on first use. Read more in Stop juggling package managers, run azd update . [#7489] 
--non-interactive flag alias : --non-interactive is now a global alias for --no-prompt , and the AZD_NON_INTERACTIVE environment variable enables non-interactive mode. [#7392] 
Standardized --no-prompt failures : --no-prompt now consistently fails with a structured error when required input (subscription, location, or resource group) can’t be resolved automatically, enabling reliable non-interactive use in continuous integration and continuous deployment (CI/CD) pipelines and AI agents. [#7825] 
docker.network option : A new docker.network field in azure.yaml service configuration passes --network to docker build for services that require host networking (such as builds behind corporate proxies). [#7361] 
Raw azd auth token output : azd auth token now prints the raw access token by default. Use --output json for structured output including expiration metadata. [#7384] 
Reduced pipeline prompts : azd pipeline config no longer prompts for parameters that are outputs of earlier provisioning layers, reducing unnecessary prompts in multi-layer deployments. [#7296] 
Breaking changes 
azd init -t <template> creates a new directory 
Running azd init -t <template> now creates a project directory named after the template (similar to git clone ) instead of initializing in the current directory. Pass an optional [directory] positional argument to override the name, or pass . to restore the previous in-place behavior:
azd init -t <template> . 
[#7290] 
App Service slot targeting 
The automatic slot-selection heuristics for App Service deployments are replaced with explicit slot targeting. Set AZD_DEPLOY_{SERVICE}_SLOT_NAME=production to deploy to the main app, or AZD_DEPLOY_{SERVICE}_SLOT_NAME=<name> for a specific slot.
The previous auto pick behavior (single slot present, no SLOT_NAME set, --no-prompt ) and first-deploy push-to-all-slots behavior are removed. When slots are present and SLOT_NAME isn’t set, azd deploy prompts interactively or errors in non-interactive mode. [#7630] 
🪲 Bugs fixed 
Security 
This release includes several security-related fixes. Users are encouraged to upgrade ( azd update ).
Code-signing verification for Windows MSI installs performed via azd update . The installer now refactors how MSI install script arguments are constructed for stable and daily channels, and rejects MSI packages that aren’t signed by the expected publisher. This closes a path where a tampered or substituted MSI could be silently installed during an in-place update on Windows. [#7298] 
Environment variable leak fix between azd and extension subprocesses. Because extension commands set DisableFlagParsing: true , cobra never parsed the -e/--environment flag, so the DI resolver fell back to the default environment and extensions could receive secrets or configuration from the wrong azd environment. The fix introduces a globalOptions parser that runs before cobra and is used consistently by both the DI resolver and extension invocation. The same change restores broken --debug , --cwd , and -e/--environment flag propagation to extension commands that regressed in an earlier revert. Validation of environment names is intentionally lenient so that extensions reusing -e for non-env-name values (such as URLs) continue to work. [#7314] 
Removed an unsafe global os.Chdir call from Aspire server initialization. The previous implementation mutated the process-wide working directory in InitializeAsync , an ambient-authority pattern that could cause concurrency issues when other goroutines or concurrent operations relied on the working directory. rootPath was already passed explicitly to every consumer, so the call was unnecessary as well as unsafe. [#7362] 
Authentication and identity 
Fix error handling for AADSTS530084 token protection errors to display clear guidance and documentation links instead of an opaque failure message. [#7797] 
Fix tenant-specific authentication guidance for AADSTS70043 and AADSTS700082 errors; azd now returns guidance targeting the correct subscription tenant when a credential fails due to a stale refresh token. [#7578] 
Fix AZURE_PRINCIPAL_ID resolution for guest and business-to-business users by resolving the principal identity in the subscription’s resource tenant, and prefer the ARM token oid claim over a Microsoft Graph call to avoid incorrect role assignments. [#7549] 
Fix panic when azd auth token is called with an unsupported --output format. [#7356] 
Fix azd auth token being cancelled by the background update check when invoked as a subprocess by extension credential providers. Fast-exit commands now skip the update check entirely. [#7629] 
Hooks and configuration 
Fix azure.yaml hook parsing failure when mixing single-hook (map) and multi-hook (list) formats in the same hooks: block. [#7618] 
Fix service-level hooks referencing shared scripts through relative paths (such as ../../hooks/script.ps1 ) failing with “hook script path escapes project root.” The containment boundary is now the project root instead of the service directory (regression in 1.23.15). [#7689] 
Fix service names containing spaces in azure.yaml generating invalid environment variable names (such as SERVICE_API AND FRONTEND_IMAGE_NAME → SERVICE_API_AND_FRONTEND_IMAGE_NAME ). [#7723] 
Fix docker.path and docker.context in azure.yaml being resolved relative to the service directory instead of the project root when user-specified values are provided. [#7600] 
Fix nil pointer panic when azure.yaml contains services, resources, or hooks with empty definitions. Reports all issues in a single actionable error message. [#7343] 
Extensions and deployment 
Fix extension lifecycle event handlers being silently dropped when multiple extensions subscribe to the same lifecycle event. [#7562] 
Fix subscription-scope deployments incorrectly treating preexisting resource groups as deployment-owned during cleanup. Only resource groups explicitly created by the deployment are now returned. [#7698] 
Fix Azure Kubernetes Service postprovision hook to skip gracefully when the cluster isn’t provisioned yet in a multi-phase workflow, instead of failing fatally. [#7501] 
Fix azd pipeline config --provider azdo failing when no agent queue named “Default” exists. azd now queries available queues, automatically selects when only one is present, and prompts the user to choose when multiple queues are available. [#7707] 
Copilot and AI 
Fix Copilot error-handling saved preference ( copilot.errorHandling.fix=allow ) to automatically retry the failed command after applying a fix, instead of only applying the fix without retrying. [#7768] 
Fix Copilot error troubleshooting to skip AI analysis for timeout errors, mark Bicep missing-input and azure.yaml config validation errors as not fixable, and apply a 5-minute guard timeout to AI analysis requests. [#7555] 
User experience 
Fix arrow keys printing escape sequence characters ( [A , [B , [C , [D ) in the filter text of select and multi-select prompts when running azd in PowerShell. [#7642] 
Fix azd update on Windows failing when PowerShell 7 and 5.1 are both installed. Reset PSModulePath before invoking the installer to prevent module path conflicts. [#7703] 
Improve azd update error message when the installation is managed by an administrator, with guidance to suppress update notifications through AZD_SKIP_UPDATE_CHECK=1 . [#7417] 
Other changes 
Improve azd up and azd deploy performance with connection pooling, adaptive ARM poll frequency (5 seconds for deployments, 15 seconds for WhatIf/Validate), per-registry Azure Container Registry login caching, and Container App revision poll frequency (5 seconds). [#7600] 
Update bundled Bicep CLI to v0.42.1. [#7557] 
Update bundled GitHub CLI to v2.89.0. [#7456] 
Update the “update available” banner to a shorter, more actionable format that includes a link to release notes (stable channel) or recent changes (daily channel). [#7767] 
Update azd update success message to a shorter, more actionable format. [#7591] 
Filter deprecated AI model versions and retired stock-keeping units from model selection prompts in the AI model service. [#7536] 
Fix copilot consent list and copilot consent revoke --action flag to display correct valid values ( all , readonly ) in shell completion suggestions. [#7588] 
New docs 
Multi-language hooks (April 24): New documentation covering Python, JavaScript, TypeScript, and .NET hook support in azure.yaml , including dependency management and executor configuration. 
Copilot integration (April 24): New documentation for GitHub Copilot integration with azd , covering AI-assisted project setup and error troubleshooting flows. 
Custom prompts (April 14): New documentation on customizing prompts in azd workflows. 
Azure.yaml schema (April 23): Updated schema documentation covering new fields for hooks, Docker configuration, and infrastructure providers. 
Updated installation instructions (April 14): Refreshed installation instructions for v1.23.14. 
New templates 
Community-driven templates help you get started faster, solve real-world scenarios, and showcase best practices for deploying solutions with Azure Developer CLI.
The Azure Developer CLI template gallery continues to grow with exciting new contributions from the community. Thank you!
awesome-azd 
Azure Functions with Service Bus and VNet (Python) by Anthony Chu : End-to-end Python sample demonstrating secure triggering of a Flex Consumption function app from a Service Bus instance secured in a virtual network, using managed identity and VNet integration. 
Azure Functions EventHub templates (Java, JavaScript, PowerShell): Multiple EventHub-triggered Azure Functions templates added April 10. 
ToDo list: Razor Pages + Azure Functions + Storage Table (Managed Identity access) by Massimo Bonanni : A complete ToDo app with front-end in Razor pages hosted in App Service, backend in Azure Functions hosted in a function app, and data in Azure Table Storage. Uses managed identity to access data. 
Host Model Context Protocol SDK Server on Azure Functions , with four language variants added April 3:
Python 
TypeScript 
.NET/C# 
Java/Quarkus 
AI gallery 
Prior-Authorization-Multi-Agent-Solution-Accelerator , added April 8. 
🙋‍♀️ New to azd? 
If you’re new to the Azure Developer CLI, azd is an open-source command-line tool that accelerates the time it takes to get your application from local development environment to Azure. azd provides best practice, developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor or CI/CD.
Install azd 
Explore templates: Browse the Awesome azd template gallery and AI App Templates 
Learn more: Visit the official documentation and troubleshooting guide 
Get help: Visit the GitHub repository to file issues or start discussions
