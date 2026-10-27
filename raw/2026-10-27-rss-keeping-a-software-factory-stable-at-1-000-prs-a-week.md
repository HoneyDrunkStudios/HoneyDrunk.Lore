---
source: "https://kiro.dev/blog/software-factory-stability"
title: "Keeping a software factory stable at 1,000 PRs a week"
author: "Zejiang (Joe) Guo; Bolin Chen; Zezhen Xu"
date_published: "2026-10-26"
date_clipped: "2026-10-27"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/tech/2026-10-27"
---

# Keeping a software factory stable at 1,000 PRs a week

Source: https://kiro.dev/blog/software-factory-stability

In our [last post](https://kiro.dev/blog/software-factory-1000-prs/), we described how three engineers and a crew of agents merged 1,000 pull requests in one week. The most common question we got back was how we keep that from breaking everything. But we think there’s a better question to ask. Can a human be responsible for every PR they shipped, which includes code they did not write and did not read line by line? Could you even speak confidently about any one of those PRs if a tech leader asked you about it?

An agent can write a code change in minutes, so speed is the easy part. Keeping a high quality bar at that speed is hard, because we must know each change is correct, safe, and worth merging without a human reading every line.

## Where confidence comes from

Before AI, confidence did not come only from someone reading and approving every if/else in review. Manual review was necessary, but not sufficient. It was followed by many more tests, and usually by someone running the change by hand in a real or simulated environment. Testing is where the confidence came from.

But human testing alone is not enough. A person can only try a few cases, usually the happy path or the obvious edge cases. That is why, on a production service that one of our three engineers ran before, every change still went through automated tests in the release pipeline after careful manual testing. It shows humans relied on automated testing harnesses to gain high confidence even before AI.

So “how can a human be responsible for AI-written code?” becomes a different question. How do we build automatic tests and checks strong enough that we trust them more than our own reading? A human cannot read every change, but a pipeline can test all of them, every time, the same way. That is why, on the Kiro Crew team, we spend around 20% of our time on infrastructure that lets us automate more.

This also changes what “knowing a PR” means. If someone hands us a PR number, we do not recite the diff from memory. We ask our crew and get back a plain-language summary in a minute, grounded in the code, in test evidence such as screenshots, videos, and data, and in the review record. The review record is the trail CI (continuous integration) writes on every pull request: every reviewer’s finding, how each one was fixed or answered with evidence, every check result, and the final readiness verdict. It shows that every change went through the same reviews, tests, and gates. That record is what we are responsible for.

This makes quality a CI/CD and testing problem. We pushed test coverage above 90% and plan to reach 100%, guarded against regressions in the test suite, and added agentic testing, where an agent drives the real app the way a user would.

## How we got here

Quality increased in five stages alongside our coding speed. We did not plan the whole system up front. Each stage worked toward the same two goals, higher quality and more automation, and solving one problem usually revealed the next. None of the stages is finished, and we still improve each one every week. If you run coding agents against a real codebase, you will likely meet the same walls in the same order.

Loading image...![Diagram titled 'The code got faster every stage. The checks had to catch up.' showing five cards joined by arrows: Stage 1 'Review bot' — bot review, with e2e by hand and hot fixes marked as missing — labeled 'manual'; Stage 2 'Severity tiers' — blocking, concern, nit (skip), and a multi-pass agent — labeled 'still manual'; Stage 3 'GitHub CI' — builds and tests, auto screenshots, AI reviewers, and model families — labeled 'automated'; Stage 4 'Full loop' — a grid of checks feeding one checkmark — labeled 'agent to green'; Stage 5 'Beyond code' — release tests, security scans, pen testing, refactoring, and own hosts — labeled 'layered' and highlighted.](https://kiro.dev/images/blogs/software-factory-stability/quality-stages.png?h=9ce318b5)

Figure 1: Each stage added checks to keep pace with faster code.

## Before the stages: human review

In early March, the team set up a basic code review mechanism and tried to review every change by hand, an approach that lasted less than a day. Kiro Crew was only a side project with far fewer changes then, and it was still too much for human review. That forced us to automate review.

## Stage 1: an automated reviewer, a human pipeline

Kiro Crew started via our internal build and review system, which runs an automated review bot on every change. We added a strict rule: every AI comment, no matter its priority, had to be resolved before merge. The rule sounded like quality, but it became friction, and three problems showed up quickly.

- **No real end-to-end test.** The pipeline had no end-to-end tests for Kiro Crew and no real usage of the product, so a change could break the app even after every comment was resolved. A human had to test everything by hand and attach screenshots as proof, and whatever slipped through came back as a hot fix.
- **Comments arrived round after round.** You fixed five comments, pushed, and got four new ones on code you had not touched, then three more. Because every comment had to be resolved, a small change could take a day of back-and-forth. Worse, each fix often added new code, such as an extra check or code path, which drew comments of its own. A small fix could grow into a much bigger change than anyone planned.
- **Limited control over the reviewer.** We could add our own rules, but we could not see whether a rule fired, why, or why it missed. Without that feedback, we could not tune the reviewer to the problems we kept hitting.

**What we learned.** A strict rule only helps when the reviewer gives complete and tunable feedback. The changes also need to be tested end to end in the real product. Without both, review turned into churn, and real bugs still reached users.

## Stage 2: severity tiers and a second reviewer

First we tiered comments by severity. Blocking findings and real concerns must be fixed in the same PR. Minor comments and style nits become follow-up issues for future PRs. This keeps each PR small and keeps review focused on the change in front of it.

Tiering can look like lowering the bar, and it does not stop the loop where each fix draws new comments. So we also added our own review agent next to the existing bot. It scans the change in several passes, each told to skip what earlier passes found. The goal is to surface every real comment in one round, so a contributor fixes once instead of multiple times. Reading those reviews carefully during this stage also surprised us. The AI reviewers found issues deeper than a human reader would have usually caught. This finding also leads us to give up reviewing code line by line manually.

The additional AI reviewer helped, but a human still drove every round of fix. Crew running locally can do the actual fix based on the review comments but a human still needs to push the updated code for online review, then wait for some time to bring the new comments back to the local Crew for the next fix. This progress can take multiple rounds and spend long time, so some contributors stopped contributing due to these tedious steps after a few loops. To close that gap, we shipped built-in skills that let anyone run the test and the same AI review locally, so they can get required comments to make the fix quickly on local machine before sending out the PR.

**What we learned.** A strict review helps build the good software, but long human driven loop can get contributors away. Automation is the solution, and we still lacked the CI to run it.

## Stage 3: open source, real CI, and many reviewers

Moving Kiro Crew to GitHub gave us strong CI/CD support for an open-source project. Every pull request now gets builds, unit tests, and end-to-end tests automatically. Kiro Crew’s built-in test pod runs the updated code in an isolated environment, captures screenshots and videos of related features, and attaches them to the pull request. Work that used to eat an engineer’s afternoon now runs on every change. With CI automatic, we could afford to add much richer checks.

Loading image...![Diagram titled 'Fork code runs with no secrets. The judge always comes from main.' split by a dashed vertical line labeled 'Workflow boundary'. Left panel 'Fork PR · untrusted' flows top to bottom: 'Stranger's code' (branch, files, symlinks), then 'Build + tests' (no credentials in reach), then 'Outputs only' (results handed across as data), with the note 'Every path the PR controls is hostile.' Right panel 'Trusted workflow' flows top to bottom: 'Secrets' (model keys, cloud access), then 'Review rules' (loaded from main, never from the PR), then 'Verdict' (AI reviewers, integration tests), with the note 'A PR never writes its own judge.'](https://kiro.dev/images/blogs/software-factory-stability/fork-isolation.png?h=2bff02d8)

Figure 2: Untrusted fork code and the trusted review workflow run on opposite sides of a boundary.

**Reviewers with different jobs.** One AI reviewer looking at everything cannot dive deep enough, so we split review by role. A design reviewer asks whether the change fits the architecture, and whether a much simpler solution exists. A first-principles reviewer asks whether the change fixes the root cause, and whether users really need it. A UX reviewer evaluates user-facing changes. The code is also scanned by reviewers on different model families, because a model reviewing its own family’s code shares its blind spots.

**A full set of tests.** Unit tests, integration tests, frontend tests, desktop packaging, bundle-size budgets, coverage floors, and end-to-end tests each catch a different class of failure. Integration is where agents most often go wrong, because each change looks correct in isolation.

**One definition of blocking.** A block finding needs a concrete location, quoted evidence, a trigger, and a consequence. If a reviewer cannot name what breaks and how, the finding is advisory. Specifically, design concerns are advisory unless they describe a one-way door, a choice we cannot undo later. For a reversible choice, we accept the risk because refactoring later is easy too.

**What we learned.** Automation lets you check far more than people ever could. But more checks meant more results for a human to read and act on, and the human became the bottleneck.

## Stage 4: closing the loop

In Stage 3, a human still drove every round of code fix. Each round, an engineer checks which CI steps have failed, copy CI failure details, including AI review suggestions, to Crew and ask it to fix issues. We do not treat an AI suggestion as something we have to trust, but as input for deeper local analysis. Kiro Crew checks it against the code, runs the tests, and CI checks the fix again on the next round. Compared with these additional works behind each fix, a human driving every call added little value.

So we shipped a built-in skill, `prepare-pr`, that drives the loop until the pull request is green. It needed one clear signal to read, because it is costly to scan 80+ checks for every pull request. We added a single PR Readiness check that rolls all CI/CD action results into one verdict. It must mean every expected CI/CD action has run and passed, not just that nothing is red yet, because on a new pull request “no failing checks” and “nothing has run yet” look the same.

`prepare-pr` reads that verdict, pulls the failing CI/CD actions and review findings, fixes what is real, replies with evidence to what is not, and pushes again. CI checks the new revision, and the loop reads the result. When the verdict is green, the skill stops, and the same verdict tells a human the pull request is ready. The human and the agent share one definition of “done”.

Loading image...![Diagram titled '80+ checks, one verdict. Humans and agents read the same signal.' Two columns of checks on the left — Reviewers: Design (simpler way?), First principles (needed at all?), UX (user-facing), Code on model family 1, and Code on model family 2, labeled 'same blocking bar'; Tests: Unit, Integration, Frontend, End-to-end, and Bundle size and coverage, labeled 'moving to our own hosts' — feed an arrow into a central 'PR Readiness' card with a checkmark that reads 'Every expected lane ran and every lane passed' and the note '“Nothing failed” is not “everything ran”'. A second arrow leads to two cards: Human (merge or not, at a glance) and Agent loop (knows what to fix next), labeled 'one definition of done'.](https://kiro.dev/images/blogs/software-factory-stability/pr-readiness-signal.png?h=f119060f)

Figure 3: Every reviewer and test rolls up into a single PR Readiness verdict.

With agents driving pull requests to green automatically, clicking the approve button became time consuming when there are many PRs. To automate this step, we first classify each pull request with a tier. Simple tier PRs are approved and merged automatically, and for the rest, AI drafts review suggestions for the human. To make human review fast, the agent writes the pull request description and rewrites it every time to match actual code changes. It uses a fixed template, easy to understand language, and even diagrams related to the change, so a human can understand the pull request in a few seconds. There is also a CI check that verifies the description strictly matches the code.

**What we learned.** Once checks and fixes share one signal, the agent can run the loop, and humans only make the calls that need them. The loop also creates its own problems though, mainly over-engineering and security fixes that go too far. We cover both after the last stage.

## Stage 5: things after merge

Our code reviews still miss some bugs, so code merging is not the last step. The overall quality is usually not only about the code in one pull request.

### Release gates

Before each release, extra tests run on the built product, including agentic tests. An agent installs and drives the real app through core flows, such as starting a session, running a task, using memory, and scheduling a job. Unit tests check that a specific feature works, and agentic tests check that the product core procedure still does what users expect.

### Security after merge

Merged code keeps getting checked in several layers, so a problem that slips past one layer does not live long.

- Hourly compliance checks on the merged code and on whether it went through the required review and follow core security rules.
- Daily scans from an internal security agent, applied to our open-source codebase as they are to other internal services.
- Always-on security bot that performs actual operations on the tool and tries to penetrate the security guardrails to find the issues to fix.
- A managed security inbox to receive external reports with quick turn around.

### Periodic refactoring

Fast changes leave rough edges, such as large files, duplicated logic, and dead code. We refactor on a regular schedule to keep the codebase easy for both humans and agents to change. This periodical refactoring also allows us to use latest models to write better code.

### Scaling the checks themselves

With dozens of automatic checks on every pull request and a hundred pull requests a day, we hit GitHub rate limits and our resource limit. To mitigate the issue, we split CI actions into groups then run group by group. As an example, a fast gate now runs the cheap checks first, and the slow checks start only once the fast gate passes. We also moved review to AWS CodeCommit and a few test workloads onto our own hosts, so our hardware sets the limit.

### The development process

When coding is easy, saying yes to a feature is easy too. But too many features getting merged at once can easily lead to implicit unexpected conflicts. Cheap code can also pull the team toward fancy technical solutions instead of focusing what is the right way to build. To handle this issue, every feature request is now classified before anyone builds it. A simple change can be built directly, a medium level feature needs a one-page design, and a complicated one needs a review by the whole team.

**What we learned.** Passing every check before merge is not the same as staying healthy over time. Quality needs checks that keep running on the product code. It also needs a process that decides what features get built, because the most expensive bugs are those from features users never need.

## Two critical problems we had to overcome

### Over-engineering

This is the biggest source of waste once the review-and-fix loop runs on its own. A reviewer flags an edge case, and the agent adds a mechanism. The next review flags an edge case in the new mechanism, and the agent adds another. After five rounds, a ten-line fix has become a small subsystem that wasn’t needed.

So we added retrospectives, both in the `prepare-pr` skill and in the CI. After several rounds on the same area, the loop looks back at its own history: what changed, what reviewers said, and whether the change is growing instead of converging. It then recommends a stop, a revert, or a simpler approach. The first move is usually to subtract mechanisms that are no longer needed, and the remaining findings shrink too.

We also check every suggested fix for proportion. A finding can be correct and still ask for too much. The fix should be the direct code change that solves the issue described in the pull request description, and anything bigger becomes a follow-up. The one exception is a reachable crash, security hole, or data loss, which are always fixed.

But the retrospective also created a new problem that it requires human actions to decide what coding strategy changes should be made even though strategy recommendations are usually clear. Asking for more human input might seem like the best way to get higher quality code, but each question stops the automation. To handle the issue, a second agent, the conductor, reads the retrospective’s recommendation and makes the first call itself. The human is pulled in only when the conductor cannot decide.

Loading image...![Diagram titled 'Every review round added a mechanism. So the loop learned to look back.' Left panel 'Without a look-back': a bar chart of lines added across review rounds R1 to R5 that grows each round, with findings per round of 2, 3, 3, 4, and 4, captioned 'A 10-line fix becomes a small subsystem. New code, new findings.' and labeled 'Growing, not converging'. An arrow leads to the right panel 'With retrospective + conductor', which flows top to bottom: 'Same area, 3rd round' (loop stops itself), then 'Retrospective' (past changes + comments), then three options — subtract, revert, rethink — then 'Conductor agent' (makes the first call, loop keeps going), labeled 'Human only when the conductor can't decide.'](https://kiro.dev/images/blogs/software-factory-stability/over-engineering-retrospective.png?h=babd846d)

Figure 4: A retrospective and a conductor agent stop the review loop from growing a fix into a subsystem.

### Security considerations

AI is eager about security. Given one real finding, it will add three layers of defense, a new configuration flag, and a validation step that never runs. Each addition is new code that can break, and new surface for the next review round to flag. Below are two interesting cases that were detected in our development.

- **A sandbox that blocks normal work.** Every review round tightened the agent sandbox a little more. Each step looked reasonable alone, but together they made ordinary tasks fail, like running a build or reading a project file. The product got safer on paper but not usable in practice.
- **Guarding against an attacker who already won.** A classic security suggestion is to copy an executable into its own folder and lock it down, so an attacker on the machine cannot replace it. This guard adds copying, permission checks, and update paths that can each break, and protects against a super rare case.

Therefore, our security fixes follow a simple rule: fix the actual user reachable problem with the smallest code changes.

## What you can apply today

Below are suggestions that worked for us, but every codebase is different, so adjust them to make them work for your product.

- **Tier your review comments.** “Resolve every comment” sounds rigorous but often produces churn.
- **Ask for all comments in one round.** A slower, complete reviewer costs less than one that drips findings across rounds.
- **Split reviewers by role and by model.** Different questions and model families catch different problems.
- **Compress your checks into a single readiness flag** that means “all ran and passed”, not “none failed yet”.
- **Test the whole product, not just the parts,** with at least one step driving real flows before release.
- **Put a retrospective in your agent loop,** and let a second agent make the first call so the pause does not always require a human.
- **Keep security fixes reasonable.** Use strict checks to reveal actual issues, but make small, direct fixes.

Kiro Crew is open source. The workflows, review prompts, and the `prepare-pr` skill described here are all in the [repository on GitHub](https://github.com/kirodotdev/KiroCrew). [Try Crew](https://kiro.dev/crew/) to see them in action.
