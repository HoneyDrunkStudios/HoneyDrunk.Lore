---
source: "https://devblogs.microsoft.com/dotnet/instructions-hygiene-what-frontier-models-still-need-you-to-say/"
title: "Instructions Hygiene – What Frontier Models Still Need You to Say"
author: ".NET Blog"
date_published: "2026-08-12"
date_clipped: "2026-08-12"
category: ".NET Ecosystem"
source_type: "rss"
---

# Instructions Hygiene – What Frontier Models Still Need You to Say

Source: https://devblogs.microsoft.com/dotnet/instructions-hygiene-what-frontier-models-still-need-you-to-say/

Instructions files have a habit of growing in only one direction.
A model makes a mistake, so somebody adds a rule. A tool changes, so somebody adds a workaround. A new model arrives, but the old guidance stays. Before long, the repository has an instructions file that reads like a combination of onboarding guide, style manual, troubleshooting diary, and prompt-engineering time capsule.
That may feel safer than leaving something out. In practice, it can make an AI coding agent less effective.
Modern frontier models need less procedural coaching than earlier models. They are better at exploring repositories, recognizing common frameworks, following established patterns, and recovering from ordinary errors. But they still cannot know the private decisions, hidden constraints, and hard-won operational knowledge that live in your team’s heads.
The goal of instructions hygiene is NOT to make the file as short as possible. It is to keep the smallest set of high-signal information that reliably changes the outcome .
Treat context like a budget
An instructions file is part of the context available to the model on every applicable request. Every line competes for attention with the developer’s task, the relevant code, tool output, conversation history, and other instructions.
A larger context window does not make every additional token free. Anthropic describes effective context engineering as finding the smallest set of high-signal tokens that maximizes the likelihood of the desired result. GitHub’s own guidance similarly recommends a concise project overview, the technology stack, coding guidelines, project structure, and pointers to important resources.
The useful question is therefore not:
What could we tell the model about this repository?
It is:
What does the model need to know that it cannot reliably discover, infer, or retrieve for itself?
That distinction is the foundation of a healthy instructions file.
What models still need from you
Frontier models are capable, but capability is not the same as local knowledge. Instructions are most valuable when they supply information that is specific, consequential, and difficult to infer.
1. Non-obvious facts about the system
Briefly explain what the repository does and identify architectural boundaries that are easy to misunderstand.
For example:
Billing.Api owns the public HTTP contract; Billing.Worker must not expose endpoints.
Domain rules belong in src/Core , not in controllers or persistence models.
The legacy/ directory is still used in production and is not reference-only code.
Generated clients in src/Clients/Generated must be updated through the generator, never edited manually.
Models can inspect a folder tree. They cannot reliably infer which boundary is intentional, which old-looking component is still critical, or which source file is generated unless the repository makes that clear.
2. The shortest reliable path to validation
Document commands that are authoritative, especially when the obvious command is incomplete or wrong.
## Build and validation
- Run `dotnet restore App.slnx` before the first build.
- Build with `dotnet build App.slnx --no-restore`.
- For API changes, run `dotnet test tests/App.Api.Tests/App.Api.Tests.csproj`.
- Run `./eng/verify-generated.ps1` after changing contracts.
- The integration tests require Docker and should not be run in parallel.
This is some of the highest-value information an instructions file can contain. It prevents wasted exploration, avoids known failures, and gives an agent a concrete definition of done.
Keep only commands you have validated. An incorrect command repeated with confidence is worse than no command at all.
3. Choices the codebase cannot settle consistently
If several reasonable approaches exist, state the one the team has chosen.
Examples include:
- Use MSTest for new tests.
- Add endpoints with Minimal APIs rather than controllers.
- Return `Result<T>` for expected domain failures; reserve exceptions for unexpected failures.
- Use the shared `TimeProvider`; do not call `DateTime.UtcNow` directly.
- Prefer existing repository abstractions over adding a new dependency.
These are not universal programming truths. They are local decisions. That makes them ideal instructions.
4. Hard constraints and expensive mistakes
Tell the model what must not change when violating the rule would create a security, compatibility, compliance, or operational problem.
- Preserve the public JSON contract unless the task explicitly requests a breaking change.
- Never place customer data in logs.
- Database migrations must be backward-compatible with the previous application version.
- Do not modify files under `infra/production` without an explicit deployment task.
Avoid filling the file with generic warnings. Reserve strong language such as always , never , and must for rules that are genuinely absolute.
5. Where the source of truth lives
Instructions do not need to contain every detail if they point to a reliable, focused source.
- API design rules: `docs/api-guidelines.md`
- Supported runtime versions: `global.json` and `Directory.Build.props`
- Deployment workflow: `docs/deployment.md`
- Architecture decisions: `docs/decisions/`
This is progressive disclosure: give the model enough information to find the right context when it needs it instead of loading everything up front.
What models usually do not need
The fastest way to improve an old instructions file is often subtraction.
Generic software engineering advice
Rules such as these rarely add useful repository context:
- Write clean, maintainable code.
- Follow best practices.
- Use meaningful variable names.
- Handle errors appropriately.
- Consider performance and security.
- Write high-quality tests.
A frontier coding model already knows these ideas. More importantly, the statements are too vague to resolve a real decision. Replace them with a local standard or remove them.
Instead of “handle errors appropriately,” say:
Map validation failures to 400 , missing resources to 404 , and concurrency conflicts to 409 using the existing ProblemDetails helpers.
Exhaustive repository inventories
A complete directory listing becomes stale quickly and duplicates information the model can retrieve in seconds. Include only paths whose purpose is non-obvious or whose role materially affects where changes should be made.
Information already enforced by tools
Do not explain formatting rules that the formatter applies automatically or restate every compiler and linter setting. Point to the command that enforces them.
Instead of listing twenty formatting preferences, write:
Run dotnet format --verify-no-changes ; do not manually override repository analyzer rules.
Keep a written rule only when the tool cannot enforce it or when the model needs the rule before it chooses an implementation.
Duplicated documentation
Copying the README, architecture guide, and contribution guide into an instructions file increases maintenance cost and creates opportunities for contradiction. Summarize the decision the model needs and link to the source of truth.
Prompt folklore and model-specific coaxing
Older files often contain instructions such as:
- Take a deep breath.
- Think step by step.
- Act as a world-class senior engineer.
- Be extremely meticulous.
- Read every file before making a change.
- Never stop until the solution is perfect.
These phrases are not project knowledge. Capable reasoning models do not need theatrical encouragement, and rigid procedural directions can cause unnecessary exploration or conflict with the tools available in a particular environment.
Describe the outcome, constraints, and validation instead:
Make the smallest change that addresses the root cause, preserve public behavior, and run the targeted tests for the affected project.
A diary of old failures
A workaround belongs in the instructions file only while it is still necessary. Once the script, dependency, or platform issue is fixed, remove the warning. Otherwise, agents keep routing around problems that no longer exist.
Write for the model class, not one model version
Model upgrades are a good reason to review instructions, but instructions should not become a collection of branches such as:
If using Model A, inspect three files first.
If using Model B, ask for confirmation.
If using Model C, reason step by step.
That approach is brittle because model availability and behavior change faster than repository architecture.
Prefer model-independent statements about the work:
the outcome required
the local constraints
the authoritative commands
the evidence needed before completion
the places where human approval is required
When a newer model succeeds without an old piece of scaffolding, remove the scaffolding. When it fails because it lacks repository knowledge, document that knowledge rather than prescribing a model-specific ritual.
Put instructions at the right scope
Not every rule belongs in the repository-wide file.
GitHub Copilot supports repository-wide instructions in .github/copilot-instructions.md , path-specific files under .github/instructions/ , and agent instructions such as AGENTS.md . When repository-wide and matching path-specific instructions are both present, both are used.
Use the broadest scope that is still accurate:
Repository-wide: architecture, shared commands, universal constraints, and common definitions of done.
Path-specific: framework conventions, test patterns, generated-code rules, or validation that applies only to part of the repository.
Linked documentation: detailed explanations, tutorials, architecture history, and rarely needed procedures.
For example, a rule about React component tests should not consume attention during a database migration. Move it to a path-specific file that applies to the front-end test directories.
Good scoping keeps the global file compact without throwing useful guidance away.
Use a keep, remove, move, verify review
Review the instructions file whenever you adopt a materially more capable model, change the build system, reorganize the repository, or notice agents repeatedly ignoring or misapplying guidance.
For every instruction, choose one action:
Action
Use it when
Keep
The information is still true, consequential, and difficult to infer.
Remove
The model already handles it, a tool enforces it, it is vague, or it is obsolete.
Move
The rule is useful but belongs in a path-specific file or linked document.
Verify
The instruction describes a command, workaround, version, or dependency that may have changed.
Then test the smaller file on representative work:
Ask the current frontier model to complete a common, bounded task.
Observe actual failure modes rather than imagined ones.
Add the minimum instruction needed to prevent a repeated failure.
Test again on a different task.
This reverses a common anti-pattern. Instead of carrying every old instruction forward until somebody proves it is unnecessary, start with the capable model and add context only when evidence shows that context is missing.
A compact example
Here is the kind of repository-wide file many teams can aim for:
# Project context
This repository contains the Contoso Orders API and its background
fulfillment worker. Public API contracts are owned by `src/Orders.Api`.
Business rules belong in `src/Orders.Core`.
## Engineering decisions
- Target the .NET version specified in `global.json`.
- Use Minimal APIs for new endpoints.
- Use the existing `Result<T>` pattern for expected domain failures.
- Use `TimeProvider`; do not call the system clock directly.
- Do not edit files under `src/Generated`; run `./eng/generate.ps1`.
## Validation
- Build: `dotnet build Orders.slnx`
- Unit tests: `dotnet test tests/Orders.UnitTests`
- API changes: also run `dotnet test tests/Orders.Api.Tests`
- Contract changes: run `./eng/verify-generated.ps1`
## Constraints
- Preserve public JSON contracts unless a breaking change is explicit.
- Never log secrets, tokens, or customer payloads.
- Keep migrations compatible with the previous deployed version.
## References
- Architecture decisions: `docs/decisions/`
- Deployment process: `docs/deployment.md`
Notice what is missing: a complete file tree, generic coding advice, a long persona, and detailed instructions for how the model should think. The file concentrates on facts that change implementation choices.
Make instructions part of engineering maintenance
Instructions files should be reviewed like code because they influence code.
A few lightweight practices help:
Include instructions changes in normal pull request review.
Ask reviewers whether a new rule is broadly reusable or only fixes one task.
Add an owner for operational commands and environment requirements.
Remove temporary workarounds in the same pull request that fixes the underlying issue.
Recheck commands after SDK, framework, test runner, or build pipeline upgrades.
Periodically ask a frontier model to identify duplicated, vague, conflicting, or discoverable instructions, then verify its suggestions.
Do not measure quality by line count alone. A 30-line file with incorrect commands is worse than a 100-line file containing necessary monorepo boundaries. Compactness is the result of relevance, not an arbitrary target.
The standard to aim for
A healthy instructions file lets a capable model begin useful work quickly without telling it how to be a capable model.
Keep the information that only your team can provide:
what the system is
where important boundaries are
which local choices are intentional
how to build and validate reliably
what must never be broken
where deeper truth can be retrieved
Remove the information that the model can already infer, the repository can reveal, or tooling can enforce.
As frontier models improve, the best instructions files will not disappear. They will become more focused. The durable value is not in teaching the model how to reason. It is in giving the model the right facts, at the right scope, at the moment those facts matter.
Further reading
Adding repository custom instructions for GitHub Copilot
5 tips for writing better custom instructions for Copilot
Effective context engineering for AI agents
GPT-5 prompting guide
