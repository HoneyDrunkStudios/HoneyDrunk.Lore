---
source: "https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/"
title: "Write azd hooks in Python, JavaScript, TypeScript, or .NET"
author: "Kristen Womack"
date_published: "2026-04-22"
date_clipped: "2026-05-31"
category: "Azure & Cloud"
source_type: "rss"
---

# Write azd hooks in Python, JavaScript, TypeScript, or .NET

Source: https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/

Hooks are one of the most popular features in azd , and now you can write them in Python, JavaScript, TypeScript, or .NET, not just Bash and PowerShell. 
What’s new? 
The Azure Developer CLI ( azd ) hook system now supports four more languages beyond Bash and PowerShell. You can write hook scripts in Python , JavaScript , TypeScript , or .NET . azd automatically detects the language from the file extension, manages dependencies, and runs the script with no extra configuration required.
Why it matters 
Hooks let you run custom logic at key points in the azd lifecycle before provisioning, after deployment, and more. Previously, hooks supported scripts written in Bash and PowerShell, which meant developers had to context-switch to a shell scripting language even if their project was entirely Python or TypeScript. Now you can write hooks in the same language as your application, reuse existing libraries, and skip the shell scripting.
How to use it 
Point a hook at a script file in azure.yaml , and azd infers the language from the extension. If the extension is ambiguous or missing, you can specify the language explicitly with the kind field:
hooks:
preprovision:
run: ./hooks/setup
run: ./hooks/setup.py
kind: python # explicit — overrides extension inference 
Here’s what a typical setup looks like:
# azure.yaml
hooks:
preprovision:
run: ./hooks/setup.py
postdeploy:
run: ./hooks/seed.ts
postprovision:
run: ./hooks/migrate.cs 
Python hooks 
Place a requirements.txt or pyproject.toml in the same directory as your script or a parent directory. azd walks up the directory tree from the script location to find the nearest project file, creates a virtual environment, installs dependencies, and runs the script.
hooks/
├── setup.py
└── requirements.txt 
Then reference the script in your azure.yaml :
hooks:
preprovision:
run: ./hooks/setup.py 
JavaScript and TypeScript hooks 
Place a package.json in the same directory as your script or a parent directory. azd runs npm install (or the package manager specified in config ) and executes the script. TypeScript scripts run via npx tsx with no compile step or tsconfig.json needed:
hooks/
├── seed.ts
└── package.json 
Then reference the script in your azure.yaml :
hooks:
postdeploy:
run: ./hooks/seed.ts 
.NET hooks 
Two modes are supported:
Project mode : If a .csproj , .fsproj , or .vbproj exists in the same directory as the script, azd runs dotnet restore and dotnet build automatically. 
Single-file mode : On .NET 10+, standalone .cs files run directly via dotnet run script.cs without a project file. 
hooks/
├── migrate.cs
└── migrate.csproj # optional — omit for single-file mode on .NET 10+ 
Then reference the script in your azure.yaml :
hooks:
postprovision:
run: ./hooks/migrate.cs 
Override the working directory 
Use the dir field to set the working directory for a hook. This configuration is useful when the project root differs from the script location:
hooks:
preprovision:
run: main.py
dir: hooks/preprovision 
Executor-specific configuration 
Each language supports an optional config block for executor-specific settings:
hooks:
preprovision:
run: ./hooks/setup.ts
config:
packageManager: pnpm # npm | pnpm | yarn
postdeploy:
run: ./hooks/seed.py
config:
virtualEnvName: .venv # override default naming
postprovision:
run: ./hooks/migrate.cs
config:
configuration: Release # Debug | Release
framework: net10.0 # target framework 
Mixed formats 
You can mix single-hook and multi-hook formats in the same hooks: block, including platform-specific overrides:
hooks:
preprovision:
run: ./hooks/setup.py
predeploy:
windows:
run: ./hooks/build.ps1
posix:
run: ./hooks/build.sh 
Try it out 
To make sure you have this feature, update to the latest azd version:
azd update 
For a fresh install, see Install azd .
We hope you like this new feature for writing azd hooks in your preferred language! Let us know what you think and how you’re using it.
Feedback 
Have questions or ideas? File an issue or start a discussion on GitHub . Want to help shape the future of azd ? Sign up for user research .
🙋‍♀️ New to azd? 
If you’re new to the Azure Developer CLI, azd is an open-source command-line tool that takes your application from local development environment to Azure. azd provides best practice, developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor or CI/CD.
Install azd 
Explore templates: Browse the Awesome azd template gallery and AI App Templates 
Learn more: Visit the official documentation and troubleshooting guide 
Get help: Visit the GitHub repository to file issues or start discussions 
Share your feedback: We’re interested in learning how you’re using azd ! Sign up for user research to help shape the future of the Azure Developer CLI 
This feature was introduced across several PRs: #7451 (Python), #7626 (JS/TS), #7652 (.NET/C#/F#/VB.NET), #7690 (config), #7618 (mixed formats).
