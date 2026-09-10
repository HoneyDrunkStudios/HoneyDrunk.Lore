---
source: "https://newsletter.systemdesign.one/p/claude-code-claude-md-best-practices"
title: "If you want to get started with Claude Code, read this"
author: "Neo Kim"
date_published: "2026-09-10"
date_clipped: "2026-09-10"
category: "Software Architecture"
source_type: "rss"
---

# If you want to get started with Claude Code, read this

Source: https://newsletter.systemdesign.one/p/claude-code-claude-md-best-practices

If you want to get started with Claude Code, read this #176: Part 1 - Claude Code 24/7 Neo Kim and Gencay Sep 10, 2026 ∙ Paid 20 3 Share 🚨 SUPER DUPER BIG ANNOUNCEMENT 🚨
One of the best ways to get ahead of most software engineers is to become good at Claude Code…
So today we’re excited to announce that doors are officially open for our brand spanking new newsletter series...
INTRODUCING: Claude Code 24/7
This 5-part newsletter series (running through the end of October) will elevate your software engineering career.
If you’ve ever thought:
“I want to understand Claude Code, but don’t know where to start.”
“I want to master Claude Code so I can get more out of it at work.”
“It’s time. I should learn how to set up subagents, hooks & scheduled automation.”
Then this is for you…
Here’s what you’ll get inside Claude Code 24/7:
A complete setup, from your first session to a fully automated one.
Deep dives into how MCP, subagents, agent orchestration & hooks work.
How real projects handle context, scale, and running without you.
And here’s the best part:
You’ll get 10x the results you currently get with 1/10th of your time, energy & effort.
Subscribe § Autonomous Software Development for the Enterprise (Partner) Blitzy is built for large, complex software projects that other coding agents cannot handle: new feature development, large-scale refactors, scaled vulnerability remediation, and undocumented legacy systems.
Blitzy’s Sandbox lets engineers evaluate Blitzy on their own software estate, at their own pace. Eligible organizations can connect real applications, reverse-engineer up to 1 million lines of code, generate up to 25,000 lines of E2E tested code, and surface prioritized security vulnerabilities across their software estate.
Try Blitzy on your codebase
(Thanks to Blitzy for partnering on this newsletter.)
§ I want to introduce Gencay as the guest author.
He has been building with AI since ChatGPT first shipped in 2022.
For years, he built for clients on Upwork: 7,300+ hours of it.
Now he builds in the open and shares every piece of it on LearnAIWithMe , every Monday, Wednesday & Friday.
Not just theory for its own sake. One real build at a time, from idea to running system.
§ Claude Code is in every feed right now…
YouTube videos, Substack posts, tutorials, screenshots of an app someone built in a single prompt.
But when I sit down with clients, I keep seeing the same install.
Three commands, maybe one skill, that’s it.
So there’s a massive gap between what Claude Code can do & how most people use it.
Let’s get started!
§ Here’s what you’ll find inside this newsletter:
What Claude Code is actually doing after you give it a task. The agentic loop behind how it gathers context, takes action, verifies its work, and uses tools to work directly with your codebase.
The setup mistake that can give Claude far more control than you intended. How permission modes work, when to use Manual, Plan, Auto, or Accept Edits, and why bypassing permissions can become dangerous as your workflow grows.
How to hand Claude a codebase you’ve never seen before. A practical workflow for mapping an unfamiliar repository before touching the code, plus how effort levels change how much thinking Claude spends on harder tasks.
How to stop re-explaining your project every time you open Claude Code. What belongs in CLAUDE.md, what should stay out, and how to make your project rules and preferences survive across sessions.
How to turn something you repeatedly do by hand into a reusable Claude Code skill. You’ll build one from scratch, give it a trigger, test it on real input, teach it from its mistakes, and make those corrections permanent so the workflow improves over time.
Golden members get full access to Claude Code 24/7!…
Subscribe
§ What Claude Code actually is Claude Code 1 is an agent running in your terminal 2 that can do anything you could do from the command line.
When you give Claude Code a task, it collects context, takes action, and verifies the results; this is called an Agentic loop 3 .
But that doesn’t mean all three stages run every time you give it a task…
Let’s say you ask a question about the codebase.
In this case, gathering context could be enough, while fixing a bug would require all three stages of the agentic loop.
Models You can change the model during the conversation.
Each model serves a different purpose.
For instance, Fable 5 is the most “intelligent” model, but you should NOT reach for it on every task 4 .
We’ll return to this in the next parts as we explore subagents…
Tools An agent takes all actions through tools 5 .
And tools are what separate Claude Code from a simple LLM.
It reads your files, searches through them, and executes commands.
Sometimes it asks for your approval first, sometimes not, and permission modes decide which. (We will cover those later in this newsletter.)
It can search the web too.
And code intelligence means Claude sees its own mistakes right after it writes them, without running the code.
Now you know how it works.
So let’s install it & run your first session…
§ If something resonated with you today, share this letter. Because one idea, one action, can change everything.
Share
§ Install it and run your first session To install Claude Code, you should use the terminal.
If you have never used one, here are the basics.
It takes two steps:
Step 1: Paste one of the following commands.
macOS/Linux:
curl -fsSL https://claude.ai/install.sh | bash
===
Windows(powershell):
irm https://claude.ai/install.ps1 | iex
===
Windows(CMD):
curl -fsSL https://claude.ai/install.cmd -o install.cmd
&& install.cmd && del install.cmd Step 2: Log in
After Step 1 is finished successfully, paste the following command.
claude Next, Claude asks you to log in, and you can authenticate with your account/API key.
Also, let’s talk about three more shortcuts before you start.
Esc interrupts Claude mid-task, so you can redirect it without losing the work.
Esc twice opens the rewind menu, which restores your code to an earlier point.
Ctrl+C kills the current input when you change your mind.
Now everything is ready, but the Claude team has also released an app.
For a better experience, you can download it here .
Here’s what it looks like:
Did you notice the mistake I made?
Yes, I bypassed permissions and let Claude do anything without my approval.
It is a serious “mistake”, and it gets worse the longer you work that way.
Let’s explore the permission modes…
§ Permission modes and which one to pick When you work with Claude, it asks for your approval between tasks.
The permission modes control how often Claude asks.
Press shift+tab or click the mode label to see the list.
At the top of the list, you’ll see your current default.
To change it, click on Settings/Claude Code.
You can toggle “Allow bypass permission mode” on & off.
If you’re still learning, leave this option off.
Here are all five options and a single-sentence explanation for each of them:
Manual : Always ask before making any changes.
Accept edits : Automatically accept all file edits.
Plan : Create a plan before making any changes.
Auto : Claude decides the permissions.
Bypass permission : Claude runs everything without asking.
Now you know how much freedom Claude has.
So let’s put it to work on a codebase you have never seen…
§ Read an unfamiliar codebase before you touch it A Claude project usually holds your skills and a Claude.md file 6 .
(We’ll go through these later in this newsletter…)
But first, let me show you mine, using VS Code, because it also shows the files.
Before publishing articles for my newsletter, I use my Claude project to test the code in them.
You can see my project name from the Claude app too.
Let’s turn the permission mode from “Manual” to “Plan” by pressing shift + tab .
(I’ve been building different projects and creating separate folders, which has made my codebase a bit messy.)
Let’s explore those files by creating an artifact 7 .
Here is the prompt to paste:
Read this project and map its structure.
Show every folder and the projects in it.
Return it as an artifact. After pasting it, Claude maps the project & starts writing the plan.
Remember, we’re in “plan” mode.
After the plan, it asks for your approval.
I clicked on “Accept and auto mode,” so it continues building for me.
Here is the artifact in 6 minutes:
I know my repo, but you don’t.
If I show you the report from top to bottom, you’ll understand what was going on.
So this flow also works on a repository you’ve never opened before.
I pointed it at my own messy folder, but it works the same way with a stranger’s codebase.
Now you get the idea…
But what if the job needs “deeper thinking” than this one did?
Then you need to adjust the effort level.
Let’s explore different levels…
§ Effort levels Effort levels adjust how much Claude thinks before doing a task.
You set it by clicking here:
Effort is directly related to token usage 8 .
The default level is High for every model, which is best for most tasks.
If your Claude token limit is low and the task does not require maximum intelligence, you can set it to Medium .
But if the task is critical and you do not care how many tokens it takes, the highest setting is Ultracode .
But what if you don’t want your project to forget your settings & you don’t want to repeat them in every session?
Then you should set up your Claude.md file.
Let me show you how…
§ Your project’s memory Let’s say you have a client project/personal project.
Each day brings a new challenge, and sometimes you realize that you keep copying and pasting the same prompts and/or repeating the same settings.
Starting from scratch every time is wasted work.
With just one command/prompt, your project can gain “permanent memory” of your preferences.
To test it, I created a new folder named Your First Day with Claude Code.
The official way to create Claude.md is using this command:
/init This will automatically create a Claude.md in your folder.
Let’s create it together only by prompting…
Create a new folder & open a new Claude Code session inside your Claude app.
Next, copy everything you have read in this newsletter so far.
And paste this prompt:
Turn this into a Claude.md file.
Assume I’m a beginner, add these as instructions,
and follow them whenever I ask you to do something. Here it is:
Now, whenever you start a new conversation inside this project, the context stays.
i.e., your setup travels with you session after session.
But you must follow a few rules when creating a Claude.md.
Let’s talk about that…
What goes in and what stays out The CLAUDE.md you create should not run too long/too thin.
Claude reads the entire file every time your project starts, so every line either earns its place/wastes it.
So what earns a place?
Write down what you would otherwise re-explain.
Build commands, naming conventions, and the rules you keep repeating.
What stays out matters just as much:
Skip anything Claude can read from the code itself, like folder layouts and dependency lists, since they only burn context on every session.
Long procedures stay out, too, because those belong in a skill.
And two habits from the Claude team keep the file healthy.
Keep it under 200 lines, since longer files get followed less, not more.
Then run /context 9 now & then, and check that your file is listed under memory files. If it is missing there, Claude never saw it.
Now think about the most repetitive task you do… How would it change if you used this?
Claude.md is only half of it.
You can also use Skills alongside Claude.md, which lets you hand each job to a specialist.
Let me show you how…
§ Reminder: this is a teaser of the subscriber-only newsletter, exclusive to my golden members.
When you upgrade, you get:
A complete Claude Code setup, from your first session to a fully automated one.
Deep dives into how MCP, subagents, agent orchestration & hooks actually work inside Claude Code.
How real Claude Code projects handle context, scale & running without you.
Unlock Full Access
(If this newsletter has helped you become a better software engineer, consider subscribing to support my work.)
§ Skills Keep reading with a 7-day free trial Subscribe to The System Design Newsletter to keep reading this post and get 7 days of free access to the full post archives.
Start trial Already a paid subscriber? Sign in Previous A guest post by Gencay The fastest way to learn AI is to build something before you feel ready. Ideas don't compound; things you build do. Subscribe to Gencay
