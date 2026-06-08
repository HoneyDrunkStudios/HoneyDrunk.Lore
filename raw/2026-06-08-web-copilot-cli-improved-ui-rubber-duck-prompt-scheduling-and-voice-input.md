---
source: "https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/"
title: "Copilot CLI: Improved UI, rubber duck, prompt scheduling, and voice input"
author: "GitHub"
date_published: "2026-06-02"
date_clipped: "2026-06-08"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Copilot CLI: Improved UI, rubber duck, prompt scheduling, and voice input

Source: https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input/

# Copilot CLI: Improved UI, rubber duck, prompt scheduling, and voice input

GitHub Copilot CLI is getting a major refresh at Microsoft Build 2026. **Rubber duck** and **voice input** are generally available today, and both **prompt scheduling** and a new **experimental terminal interface**—including tabs for working with issues, pull requests, and gists—are available to try via `/experimental`

.

*Editor’s note (June 3, 2026): Updated prompt scheduling to indicate it is part of /experimental, not generally available.*

[A new terminal experience (experimental)](https://github.blog#a-new-terminal-experience-experimental)

We’re previewing a redesigned terminal interface for Copilot CLI. You get a cleaner layout, theme-aware semantic colors, and responsive components that adapt to narrow terminals without truncating the things you need to read.

The biggest visible change is the introduction of tabs. When you use the CLI in a GitHub repository, you can press `Tab` to switch between the default **Session** view, tabs for the repository’s **Issues** and **Pull requests**, and a tab for your personal **Gists**. This lets you view issues, pull requests, and gists without leaving Copilot CLI.

The redesign also makes Copilot CLI more accessible:

- Pick from new color modes (e.g.,
`default`

,`github`

,`dim`

,`high-contrast`

, and`colorblind`

) to match your terminal and your eyes. - Screen reader support is on by default when a screen reader is detected, with labeled icons and animations that automatically disable.
- Dialogs, tables, lists, and headings render consistently across every screen in the CLI.

The new terminal experience is available in `/experimental`

mode. Run `/experimental on`

to opt in. The new experience is still evolving, and we’d love your feedback as we move toward general availability.

[Get a second opinion with rubber duck](https://github.blog#get-a-second-opinion-with-rubber-duck)

Rubber duck is a built-in CLI agent that acts as a constructive critic. While working on a task, the main CLI agent for a session can pass its current plan, design, implementation, or tests over to the rubber duck agent for review. The rubber duck agent looks for blind spots, design flaws, and substantive issues, and reports back with concrete, actionable feedback. Copilot then takes that critique into account before continuing.

For some tasks, two heads are better than one, and the CLI decides when getting a second opinion may be beneficial.

You can also invoke rubber duck with `/rubber-duck`

. [Read more about rubber duck](https://docs.github.com/copilot/concepts/agents/copilot-cli/rubber-duck?utm_source=changelog-cli-rubber-duck-docs&utm_medium=changelog&utm_campaign=msbuild-2026).

[Schedule prompts with /every and /after](https://github.blog#schedule-prompts-with-every-and-after)

The new `/every`

and `/after`

slash commands let you schedule a prompt or skill within the current CLI session.

Use `/every`

to schedule a prompt to run repeatedly at the specified interval:

`/every 30m run the frontend tests`

`/every 1h how many tokens have I used during the past hour`


Use `/after`

to schedule a prompt to run just once, after the specified interval:

`/after 2h /example-skills:docx create a new file summarizing recent changes to this repo`


Run `/every`

or `/after`

with no arguments to open the schedule manager, where you can see active schedules and delete any you no longer want to run.

[Talk to Copilot](https://github.blog#talk-to-copilot)

Copilot CLI now includes hands-free dictation. Hold the space bar on your keyboard and talk to input a prompt. Alternatively, press `Ctrl`+`X` followed by `V` to start recording, speak your prompt, then press any key to stop recording and insert the transcription.

Voice input runs locally, so all audio you record stays on your machine. The first time you enable voice input, the CLI guides you through downloading the runtime and picking a speech-to-text model.

[Update and share feedback](https://github.blog#update-and-share-feedback)

Update GitHub Copilot CLI by running `copilot update`

in your terminal. We’d love to hear what you think—share feedback with the `/feedback`

command in a CLI session or open an issue in [our public repository](https://github.com/github/copilot-cli?utm_source=changelog-cli-repo&utm_medium=changelog&utm_campaign=msbuild-2026).
