---
source: "https://devblogs.microsoft.com/dotnet/doing-more-with-github-copilot/"
title: "Doing More with GitHub Copilot as a .NET Developer"
author: ".NET Blog"
date_published: "2026-05-26"
date_clipped: "2026-05-30"
category: ".NET Ecosystem"
source_type: "rss"
---

# Doing More with GitHub Copilot as a .NET Developer

Source: https://devblogs.microsoft.com/dotnet/doing-more-with-github-copilot/

For most .NET developers, the best way to get started with GitHub Copilot is not by learning every feature first. It is by using the right Copilot experience for the work already in front of you.
Inline completions are part of that story, of course. They help with the everyday C# work that is repetitive but still necessary: filling in tests, building out LINQ expressions, wiring up DTOs, or scaffolding a Minimal API endpoint. But the bigger gains usually show up when you start using chat for reasoning and agentic workflows for scoped execution.
That is where the different surfaces matter. Visual Studio, Visual Studio Code, the Copilot CLI, and the cloud coding agent each shine on different kinds of .NET tasks. The question is not which one is “most advanced.” The better question is: which one fits the job I am doing right now? 
Start with the task, not the mode 
The fastest way to get value is to stop asking, “Which Copilot feature should I try?” and start asking, “What part of this task should I delegate?”
Real examples of using chat in .NET work 
Chat becomes useful the moment you need explanation, comparison, planning, or targeted code generation based on your actual project.
Example 1: Understand a service before changing it in Visual Studio 
Suppose you open a legacy ASP.NET Core service and find a class with five dependencies, several feature flags, and business rules buried in a long method. Before you change it, use chat to get oriented.
Prompt:
Explain what this service is responsible for, identify the key dependencies, and point out which parts are business logic versus infrastructure concerns. Then suggest a safe first refactor that does not change behavior. 
That is far better than asking for a blind rewrite. It helps you understand the codebase you already have, which is often the real bottleneck in .NET work.
Example 2: Generate tests for business logic in Visual Studio 
Imagine you have a pricing method that applies discounts, caps, and regional tax rules. You can write the first happy-path test yourself, then use chat to help fill out the edge cases.
Prompt:
Create unit tests for this method using the same test style as this project. Cover discount boundaries, null input handling, and the case where the total is capped. Explain any edge cases you think are easy to miss. 
Bonus: If you are in Visual Studio, use the Test Agent. If you are in VS Code or the CLI, use the dotnet-test skill for the best success. This is a strong use case because you want both output and reasoning. You do not just want test code. You want confidence that the right cases were considered.
Example 3: Plan a refactor before touching the code 
Let us say a controller has too much logic in it and you want to move validation and orchestration into a service. Chat is useful before you edit anything.
Prompt:
Review this controller action and propose a refactor that moves orchestration into a service without changing the HTTP contract. Show the target shape of the controller, service interface, and unit tests I should expect to update. 
Enter Plan Mode before doing this and Copilot will create a detailed plan for either you or Copilot to implement when it’s ready. This works well in Visual Studio because you are already looking at the relevant files and solution structure.
Example 4: Use VS Code when the change crosses code and configuration 
A common .NET scenario is not just changing C# code. It is changing the API, the OpenAPI description, a deployment file, and the documentation in one pass. That is where VS Code often feels especially comfortable.
Prompt:
I am adding a new optional region filter to this endpoint. Update the ASP.NET Core handler, adjust the OpenAPI description, and point out any config, docs, or client code that may also need to change. 
This is where chat starts to feel less like autocomplete and more like a working partner. It can help you think across the whole repo, not just the file in front of you.
Example 5: Use the Copilot CLI to reason about a failing build 
If dotnet test or dotnet build fails, the CLI is a natural place to work because the failure is already in your terminal.
Prompt:
Explain this build failure in plain English, tell me which project likely introduced it, and suggest the next two commands I should run to narrow it down. 
Or:
This xUnit test is failing intermittently. Based on the output and the file paths involved, what are the likely causes, and what should I inspect first? 
That is a better starting point than dumping the error into a search engine because the CLI can stay close to your actual repo and command loop.
What good chat prompts look like 
For .NET work, the best chat prompts usually include four things:
the goal 
the code or command output 
the constraint 
the expected shape of the answer 
For example:
Refactor this background worker to make the retry policy easier to test. Keep the public behavior the same, preserve structured logging, and show me the test cases I should add. 
That is much stronger than:
Improve this code. 
The more the prompt sounds like a real code review comment or engineering task, the more useful the response tends to be.
Real-world agentic flows for .NET developers 
Agentic workflows are most useful when the task is multi-step, bounded, and reviewable. You are no longer asking only for an answer. You are asking Copilot to carry out a piece of work.
Example 1: Fix a test gap across a feature slice 
Suppose a new feature was added to an ASP.NET Core API, but only the happy path was tested. This is a strong agentic task in Visual Studio, VS Code, or the cloud coding agent.
Task:
Add missing unit tests for the CreateOrder flow. Cover validation failures, duplicate order detection, and the downstream payment timeout path. Keep the existing test style, do not rename public APIs, and stop once the new tests pass. 
Why this works:
the scope is clear 
the affected area is bounded 
there is an obvious definition of done 
the output is easy to review in a diff 
Example 2: Clean up a repetitive refactor 
Many .NET repos accumulate the same pattern in several places: inconsistent logging, nullable warnings, repeated guard clauses, or old result-handling code. That kind of work is tedious for a human and often well-suited to an agent.
Task:
Update the notification handlers in this project to use the shared Result<T> pattern instead of throwing validation exceptions. Preserve current behavior, update the affected unit tests, and summarize which handlers changed. 
This is not glamorous work, but it is exactly the kind of task where agentic help can save real time.
Example 3: Use the Copilot CLI for a fix-and-verify loop 
Agentic work does not only belong in the cloud. The CLI is useful when the task naturally involves commands, output, and iteration.
Task:
Investigate why dotnet test is failing in the Notifications.Tests project, make the smallest fix that addresses the root cause, rerun the relevant tests, and summarize the change. 
This is a good CLI task because the whole workflow already lives in the terminal: inspect, run, fix, rerun, and explain.
Example 4: Use the cloud coding agent for a bounded multi-file change 
The cloud coding agent is especially helpful when you have a real task that can run in the background and come back as a draft change for review.
Task:
Add correlation ID propagation to the API and background worker pipeline. Update middleware, logging enrichment, and the integration tests that assert the header flows through. Do not change unrelated logging format, and note any follow-up work if you find gaps outside this slice. 
That is a strong cloud-agent candidate because it is broad enough to benefit from delegation, but still concrete enough to review carefully.
Example 5: Cross-stack work in VS Code 
Some of the best agentic tasks are not purely C#. They touch the API, the deployment config, and the docs together.
Task:
Add support for a new beta environment flag. Update the .NET configuration binding, the Bicep template, the GitHub Actions workflow, and the deployment documentation. Keep naming consistent with the existing environment settings. 
That is the sort of task where VS Code often feels like the right surface because the work is spread across code and adjacent assets.
How to decide between chat and agentic work 
Here is the practical rule:
Use chat when you want help to understand, compare, outline, explain, or draft .
Use agentic workflows when you want help to change, verify, update, rerun, and deliver a reviewable result .
In practice:
“Explain this service and suggest a refactor” is chat. 
“Implement the refactor, update the tests, and keep the public contract unchanged” is agentic. 
“Summarize this failing build and tell me what to inspect” is chat. 
“Fix the root cause, rerun the tests, and summarize the diff” is agentic. 
If you can describe the task with a clear definition of done and you would be comfortable reviewing the resulting diff, it is probably a good candidate for agentic delegation.
A few habits that make Copilot more useful 
Whether you are using chat or agents, a few habits go a long way:
give the task a boundary 
name the constraints explicitly 
tell Copilot what must not change 
ask for the output in a useful shape 
review the result like you would review a teammate’s PR 
For .NET developers, that often means including things like:
keep the public API unchanged 
follow the existing xUnit pattern 
preserve DI registration style 
update nullable annotations only in this project 
rerun the relevant tests, not the whole universe 
Those details matter. They are what turn a generic AI interaction into a genuinely useful engineering workflow.
Final thought 
The real value of Copilot for .NET developers is not that it can suggest a few lines of C#. It is that it can help you reason through real work and, when the task is well-scoped, carry some of that work forward.
Use Visual Studio when you are deep in the solution. Use VS Code when the job crosses code, config, and docs. Use the Copilot CLI when the work lives in your terminal. Use the cloud coding agent when you have a bounded task worth delegating and reviewing. Really, use whatever tool works for you.
Start with a real task from your own backlog: understand a service, add tests around tricky logic, fix a failing build, or hand off a repetitive refactor. That is where Copilot stops feeling theoretical and starts becoming useful.
