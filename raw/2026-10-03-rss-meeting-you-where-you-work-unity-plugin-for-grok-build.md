---
"source": "https://unity.com/blog/unity-plugin-grok"
"title": "Meeting you where you work: Unity Plugin for Grok Build"
"author": "Rachel Zhao"
"date_published": "2026-10-01"
"date_clipped": "2026-10-03"
"category": "Game Development / Unity"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# Meeting you where you work: Unity Plugin for Grok Build

# Meeting you where you work: Unity Plugin for Grok Build

##### Rachel Zhao - Unity

Over the last few weeks, we've announced the launch of the Unity CLI followed by the release of the official Unity Plugin, all to support the singular idea that Unity should meet developers in the tools they have already chosen and in the places where they work. There are [3 billion Unity powered games downloaded monthly](https://unity.com/our-company), and because our CLI and plugins now sit inside the agents where a growing number of you start your projects, we can see something no one else can, which is game development increasingly beginning in a terminal with an agent already open rather than in a browser on a download page.

Our goal is to make sure you can create amazing games that delight your audiences. That means making the creation experience better and easier. As such, we don’t get to decide which coding agent you will use, but we’ll make sure to support you, whatever you choose. In the AI space, the tools you reach for keep changing as models evolve and improve, and the leaders are already large enough that none of them is a safe bet to be the only one: in August, OpenAI reported that [Codex had reached 15 million active users](https://x.com/i/trending/2087905863906263074), while [Claude Code held its position as the most widely used](https://lnkd.in/p/d3pjMwxt) AI coding agent.

There are also now great examples of what people are creating with their AI tool of choice and the Unity editor. A couple of notable examples are highlighted here:

- Cam Ayres, Sr. Manager of Industry Solutions, at Unity who built a
[Simon Says game using Claude Code and the Unity CLI](https://lnkd.in/p/gprHtP_2) - Andrew Walko, Applied AI at Open AI who built an amazing
[Unity city scape with Codex GPT-6 Astra and the Unity CLI](https://www.linkedin.com/posts/andrewswalko_a-few-people-have-asked-how-i-built-the-unity-ugcPost-7501754427762982914-E8Mn/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAFW_hoBgW0gxMNLyMqCXmyXq2tYjrmbRng)

This is why we’re making our tools present and easy to use wherever you do your best work. We believe in this so much, we’re excited to share with you our learnings and more product and feature releases over the next few weeks that exemplify our conviction of meeting you where you work, and helping you unlock your ability to make stunning games that captivate the world.

## Unity's Official Plugin is available for Grok Build

Today we're excited to announce that the official Unity Plugin is available for Grok Build, making it the third coding agent to carry Unity's own engineering guidance. Grok Build gets [the same 30+ skills](https://github.com/Unity-Technologies/unity-agent-plugin/tree/main/skills) our engineers wrote for Claude Code and Codex, covering UI Toolkit and uGUI, 2D and tilemaps, URP and Shader Graph, audio, navigation and physics, IAP and LevelPlay, multiplayer, web, and localization. We maintain all three plugins from a single repository, so updates flow to three agents. Getting started takes one command in your terminal, with nothing to configure yourself and nothing to copy across when you move to a new machine. It works with Unity 6 and above, and [the documentation](https://docs.unity.com/en-us/ai/unity-plugin/grok) covers the rest. We’ve already seen[ some awesome examples](https://x.com/tetsuoai/status/2080038493594734780) of how people have been using Grok Build with Unity so we’re hoping to see what you can do next!

The skills in our [official plugin for Claude Code](https://unity.com/blog/unity-plugin-for-claude-code), [Codex](https://unity.com/blog/unity-plugin-codex), and Grok Build are identical. If you’re on a team, or if you simply like using multiple agents, your Claude Code, Codex, or Grok Build will follow the same Unity guidance for the same Unity question. Our job is to give you the ability to choose your coding agent based on your personal preference. These skills are written by the Unity feature teams who own each system and revised as those systems ship. Check out our [documentation](https://docs.unity.com/en-us/ai/unity-plugin/grok) for Grok build so you can get started. Simply include the CLI command `grok plugin install Unity-Technologies/unity-agent-plugin --trust`

in the Grok Build CLI to install the plugin.

## Next time, we’ll show you the data

In October we'll publish what our own data shows about how you're using the CLI and plugin with these agents. We’re also exploring other agents that we may make the plugin available to and will share those updates soon. [In July we promised](https://unity.com/blog/meet-the-unity-cli) that you could point your preferred coding agent at Unity and we'd meet you there. Extending our official plugin to multiple coding agents means we cover most of the terminals you’re likely to have open, and the evolution will continue so that your agent of choice is never a constraint for your creativity with the Unity engine.

Install the plugin for Grok Build today, and tell us what you ship with it.
