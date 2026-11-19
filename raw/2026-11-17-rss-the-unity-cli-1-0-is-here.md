---
"source": "https://unity.com/the-unity-cli-1.0-is-here"
"title": "The Unity CLI 1.0 is here!"
"author": "Christopher Addison"
"date_published": "2026-11-17"
"date_clipped": "2026-11-17"
"category": "Game Development / Unity"
"source_type": "rss"
---

# The Unity CLI 1.0 is here!

Nov 17, 2026|5 Min

Christopher Addison - Unity Technologies

Senior Software Developer

AIAI features

AIAI features

![Unity CLI 1.0](https://cdn.sanity.io/images/fuvbjjlp/production/3308f9f8397d3f9eadf3a91ccd3de3754fd82400-1609x978.png?w=3840&auto=format&q=75&fit=max)

On July 15, 2026, we brought Unity to the [terminal](https://discussions.unity.com/t/announcing-the-unity-cli-a-new-way-to-connect-your-tools-and-agents/1731104). Today at Unite Tokyo, the Unity CLI and the [Pipeline package](https://docs.unity.com/en-us/unity-cli/unity-pipeline/unity-pipeline-package) (`com.unity.pipeline`) are out of beta. Version 1.0 is ready for your projects, your build machines and your agents.

### How we got here

We started with a beta: one binary that installs and manages Unity Editors, modules and projects from the terminal, which we introduced in [Meet the Unity CLI](https://unity.com/blog/meet-the-unity-cli). Alongside it, the Pipeline package lets the CLI drive a running Editor on your machine, so a script or an agent could open a project, run a command and check the result.

Next, the Unity Hub started installing the CLI for you, so if you're on the latest Hub, you already have it. Then came official Unity plugins for [Claude Code](https://unity.com/blog/unity-plugin-for-claude-code), [Codex](https://unity.com/blog/unity-plugin-codex), [Grok Build](https://unity.com/blog/unity-plugin-grok) and [Google Antigravity](https://docs.unity.com/en-us/ai/unity-plugin/antigravity), which give those agents skills written by Unity's own teams. The same skills are public in the [Unity skills repository on GitHub](https://github.com/Unity-Technologies/skills), so any agent can use them.

Along the way, we shipped more than 17 beta releases, shaped by what you told us.

### Inside the Unity CLI

Since July 20, more than **350,000** logged-in users have run more than **600 million commands** with the Unity CLI. About 98% of those runs come from coding agents and other automation.

We looked closer at that usage in [what we've learned about how developers use the Unity CLI](https://unity.com/blog/unity-cli-usage-data-ai-coding-agents): people set Unity up, then their agent does the work inside a live Editor.

### What you told us

Many of the changes in 1.0 started as a bug report, a Discussions thread or a message from a studio using the CLI every day.

*"I am not exaggerating when I say the CLI has completely changed how I work with Unity. It is incredible."* Dorado Digital

*"The CLI is crazy good in the most simplistic way. I'm still very much holding the reins for the moment, but it's really positive."* Andy, Kwalee

Studios also sent us detailed reports: commands that said they succeeded when they hadn't, dialogs that blocked a remote session, scripts that broke when output changed shape. That feedback set the priorities for the releases that followed. You can read every change in the [Unity CLI release notes](https://docs.unity.com/en-us/unity-cli/release-notes) or run `unity changelog`.

### What changed since launch

- **One command to set up your agent.** `unity setup` installs the official plugin for Claude Code, Codex, Grok Build or Google Antigravity. `unity skill install --all` gives Unity's skills to every agent on the machine, including VS Code, GitHub Copilot, Qwen Code and OpenCode, and `unity skill sync` keeps them current. The install script now adds Unity's skills to every agent it finds.
- **No more sessions stuck on a hidden dialog.** The CLI can now see the dialog an Editor is waiting on and answer it, so a script or an agent doesn't hang on a popup nobody can see.
- **Builds through the Editor you already have open.** `unity build --target` builds in the Editor that has the project open, and `unity pipeline cloud-build` sets up cloud build targets from the terminal.
- **Version control that reads like a person would.** `unity vcs` names the asset behind each change in a scene or prefab, and can summarize a pull request without switching branches.
- **New projects that are ready from the start.** `unity projects create` adds the Pipeline package to every new project, and can install the Editor the project needs. `unity open --until-ready` waits until the Editor can take commands.
- **Output scripts can rely on.** Every listing and stream now has the same JSON shape. Short flags mean the same thing in every command, `--project-path` works everywhere, and the CLI never prompts in CI. Clear exit codes tell a script when the Editor is busy, when a dialog is blocking it or when the network is down. You can pin a CLI version range per project.
- **A health check for your project.** `unity projects audit` runs Project Auditor and writes a report, with a focus such as upgrades, optimization or URP.
- **Easier to install and keep current.** The CLI is a native binary on macOS, Linux and Windows, available through Homebrew, winget and APT. `unity self-update` keeps your last three versions, so you can roll back. You can also keep the docs offline with `unity docs cache add`.
- **Hardened for teams.** Security fixes across installs, skills and project linking, so a cloned repository can't run its own programs in place of the real ones.

**1.0 is also a commitment:** commands, flags and output stay compatible across 1.x releases. When something has to change, you’ll get a deprecation warning and time to update before anything is removed.

### Use it with your agents

The CLI is how an agent actually works with Unity: it opens the project, runs commands in the Editor, enters Play mode and reads the result. With the official Unity plugin, the agent also gets Unity's own skills for tasks like building UI, setting up lighting or [adding in-app purchases](https://docs.unity.com/en-us/ai/unity-plugin/about-unity-plugin). See the [Unity plugin documentation](https://docs.unity.com/en-us/ai/unity-plugin/about-unity-plugin) for the full list.

Agents without an official plugin still work in Unity through the CLI. So do scripts, test runners and CI jobs with no AI involved at all. To see it in action, watch the [Automate with Unity CLI livestream](https://www.youtube.com/watch?v=Iruqwhn6w-o).

Agents and automation are also getting a supported place to run. The Build Server license now covers agents and automation, not only builds: one license per instance lets you run agents on a headless Editor or in a container, on any computer.

Coming soon: the Linux containerized Editor, a supported headless Unity Editor in a Linux container, built for CI, build machines and agents.

### What’s next?

We’ll keep shipping updates the way we did during the beta. Next, we’re bringing more of Unity to the terminal: commands for AI Generators, Live Games and Build Automation, and accounts built for agents.

### Get started

If you're on the latest Unity Hub, you already have the CLI. Open a terminal and start with the [Unity CLI documentation](https://docs.unity.com/en-us/unity-cli/unity-cli). New to the terminal? Try [A beginner's guide to Unity CLI and the Pipeline package](https://unity.com/resources/a-beginners-guide-to-unity-cli-and-the-pipeline-package), or the [Unity CLI introduction video](https://www.youtube.com/watch?v=DgNrgZeJOxQ).

And keep telling us what you build: your feedback shaped 1.0, and it will shape what comes next.
