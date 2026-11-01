---
source: "https://cra.mr/a-little-determinism"
title: "A Little Determinism"
author: "unknown"
date_published: "2026-10-29"
date_clipped: "2026-11-01"
category: "Software Architecture"
source_type: "rss"
discovered_via: "https://tldr.tech/tech/2026-10-30"
---

# A Little Determinism

Source: https://cra.mr/a-little-determinism

![A Little Determinism](https://cra.mr/ai-content/a-little-determinism.png)


Oct 29, 2026  16 min read

One of the biggest challenges I’ve grappled with lately is how to create determinism where it otherwise doesn’t exist. How do I get an agent to behave like I would, without me telling it to? Now we have reasoning agents that can do amazing things, but they often still need to be carefully instructed to do the right thing in the right situation. It’s tiring.

If you’ve tried to tackle this problem you quickly learn how complicated it is. You add a few constraints on the agent to get it to do what you want, then you find it no longer performs well. The challenge with agents is typically when you create constraints, when you take away their *freedom*, they become much less capable. So how do we keep their freedom while enforcing certain kinds of behaviors?

Let’s talk about a few ways we’re addressing that in [Junior](https://junior.sentry.dev) - our open-source Slack-enabled slopware factory.

Spoiler: for those of you who think skills or `AGENTS.md` (or the system prompt in this case) is the answer, it almost never is.

## [#](https://cra.mr/a-little-determinism#working-with-junior)Working with Junior

Junior is an agent that I (and now others at Sentry) have been building to support our internal use cases. It started as a humble way to take some Slack threads and turn them into GitHub issues, and to answer questions often determined by the shape of code. Since then it has evolved to support a large variety of use cases at Sentry, and is now also how I ship software at the company. Today I’m going to talk about that workflow, because it so clearly shows where determinism is needed and how we get there.

Most things start just as you’d expect:

![Triggering Junior in Slack](https://cra.mr/assets/junior/slack-trigger.png)

This spins up a thread where Junior does a bunch of work inside a sandbox, culminating in a pull request. The models carry the meat of the goal here - you quickly find as long as they have the right tools they perform similarly no matter what harness you’re using. Presently that means Opus 5.5 is migrating Sentry to Rust.

The pull request eventually exists. It’s got a little annotation explaining that it was co-authored by David Cramer, and a link back to Junior as well as the trace inside Sentry.

![A pull request from Junior](https://cra.mr/assets/junior/github-pr.png)

From here, if you care about job security at all, you go do a surface level review of what it did. Did it actually complete the task? Does the architecture look sane? If not, leave some comments via the review tab, and click request changes.

Woah woah woah, leaving PR comments and having an agent act on them!? You mean we’re not just prompting the agent over and over again? Yeah, futuristic I know. This is the kind of automation that truly saves you time though. In this case, I expect to be able to review something and have the author of the PR consider my feedback. Just like I expect it to fix its test failures, to make sure CI is passing, you know, the usual. Sometimes, on the rare occasion, Junior will even tell you (yeah you, or Cursor, or Sentry) that your feedback is trash, because sometimes it is!

The question becomes though, how do you ensure it does the right thing in those scenarios? How do you do it so you can *expect* it? How do you do it without removing its freedom?

## [#](https://cra.mr/a-little-determinism#what-should-happen-every-time)What should happen every time

Let’s go back to the creation of the pull request. You see that footer? That’s determinism. We want that to exist 100% of the time.

![Junior's generated footer on pull requests](https://cra.mr/assets/junior/pr-footer.png)

Another thing we want to deterministically enforce: `co-authored-by`:

![Co-Authored-By on commits](https://cra.mr/assets/junior/pr-co-author.png)

If you think about how you’d get both of those behaviors, you’ll come up with a few different options. The most obvious is to use tools (create pull request, commit), but the issue with tools is what if the agent doesn’t call them? If you want your agent to truly be capable you give it a sandbox - you give it a shell. What if it calls the GitHub CLI, or the git binary, to create the commit and pull request?

Sometimes the answer is as simple as a pull request template, other times it’s a complete multi-stage workflow. The challenge is always going to be creating the deterministic behavior while retaining the agent’s freedom to use the best tools for the job.

We found a variety of solutions, but surprisingly most of the predictability came from an unlikely candidate: a man-in-the-middle egress proxy. It comes down to two patterns: forcing behavior by denying actions, and forcing reactions via automated messages.

## [#](https://cra.mr/a-little-determinism#the-network-boundary)The network boundary

Junior has a custom harness, built on Pi’s core SDK and heavily inspired by Codex and Claude Code. It runs on top of Vercel’s infrastructure: Fluid Compute, Sandboxes, Queue, Blob, and a bit of SQL and Redis sprinkled on top. There are *a lot* of moving parts, and because it’s running on a stateless compute platform, we have to deal with the system timing out, pausing, resuming, and recovering from failures *on every session*, not just as an edge case.

How a request flows through Junior: a Slack or GitHub event goes to a queue, which wakes an agent turn backed by a session log. The agent works in a sandbox, and every outbound request goes through the egress proxy before reaching GitHub, Sentry, and other services.

Slack / GitHuba message or webhook
Queuewakes the conversation
Agent turnFluid Compute
Session logSQL · Redis · Blob
Sandboxshell, git, gh, code
Egress proxypolicy + credentials
GitHub, Sentry, …the outside world

Junior has a lot of access to internal systems, and that’s a requirement because without that it lacks capabilities. Every conversation comes down to “how do we give it more access”, and that immediately leads to the security model and tradeoffs. If you’ve spent time in software you know the network boundary is the primary point of contention when it comes to security, so that’s where we focus.

Vercel’s firewall includes a standard man-in-the-middle proxy where you can also specify an endpoint to handle requests. There’s a bit of security that has to go into that (like making sure requests are credentialed), but it allows you to control the behavior of every request the agent is making.

The agent in the sandbox sends requests without any tokens. The proxy checks policy and injects credentials before forwarding to GitHub, and responses flow back the same way.

Agentin the sandbox
ProxyJunior egress
GitHuband friends

+ token
no tokens, no keys
checks policy,injects the token
sees a normalrequest

Initially for us this solved credential security. The easiest way to secure your agent is to remove its ability to see tokens and keys, and the easiest way to do that is via the proxy. Accessing the GitHub API? Securely fetch the bearer token and inject the header automatically. We let plugins define this behavior, instructing the harness on whether it’s OAuth, an MCP connection, or some other model. When credentials are missing for a user (and they’re needed), we halt the turn and send a link to the user to get them to authorize first.

## [#](https://cra.mr/a-little-determinism#making-pr-creation-go-through-a-tool)Making PR creation go through a tool

Going back to our footer, the easiest way to do something like this is to create a tool that performs the behavior you’re looking for. In this case that’s easy: `github_createPullRequest` needs to take in a PR description, augment it with our footer, and then submit the API request.

Except the agent decided to call `gh pr create` via the command line.

That’s where our proxy comes in. We’re not just looking at where the request is going. In many cases we even parse the GraphQL request for the service. So when the agent makes a request we don’t want it to make, or we’d prefer it use a native tool call, we reject it. `gh pr create` sends a `createPullRequest` GraphQL mutation, so it gets rejected:

```
POST https://api.github.com/graphql  →  403

{"error": "GitHub pull request creation must use the github_createPullRequest
tool so Junior can own idempotency and the conversation footer. This is a Junior
tool-routing denial, not a GitHub permission failure. Do not ask the user for
GitHub permissions; retry with the required Junior tool."}
```

When that response comes back, the agent understands that it now needs to use the tool, and the tool then creates that predictable output we were after.

The proxy can tell the difference because requests from the sandbox carry a signed token, and requests from our own tools also say exactly what they’re doing:

```
// Every request out of the sandbox carries a signed, short-lived context
// (x-junior-sandbox-egress-token). It says who the request acts for.
{
  credentials: { actor: { type: "user", userId: "U..." } },
  conversationId: "...",
  egressId: "...",
  expiresAtMs: 1761703600000,
}

// Junior's own tools also declare the exact operation they're performing.
// Requests from the sandbox never have one.
await ctx.egress.fetch({
  provider: "github",
  operation: "github.pull.create",
  request,
});
```

Agents make this boilerplate pretty easy to build and maintain, and it allows us to control so much behavior. It goes beyond simple steering, and lets us determine what level of permissions we want to give the agent, ignoring what the API scopes determine. For example, Junior can’t approve a pull request, even though its GitHub token can.

That tool goes one step further though, because creating the pull request is just one of many steps in the workflow an engineer takes to land a change. It needs to monitor feedback, fix test failures, and address automated code review.

## [#](https://cra.mr/a-little-determinism#keeping-the-conversation-going-through-review)Keeping the conversation going through review

We need the agent to handle feedback, build failures, and other concerns that appear during integration and review. We do most of that via a system we call `watches`.

You can think of this as a simple webhook system, where an agent can subscribe to one of these webhooks (in this case, a set of events that can happen on this PR) and they get injected as user messages with a special demarcation.

```
{
  "resource": {
    "namespace": "github",
    "type": "pull_request",
    "identifier": "getsentry/sentry#12345"
  },
  "events": [
    "pull_request.checks.failed",
    "pull_request.review.changes_requested",
    "pull_request.review_comment.created"
  ],
  "intent": "Fix failing checks and address review feedback on this PR."
}
```

You might have seen something similar in other harnesses. This pattern is becoming more common because “loops” are a horrible way to create automations. “Check this PR every 5 minutes” is an era most of us lived through, and if you were paying per token you know how wasteful that is.

Junior automatically subscribes to a fairly obvious set of concerns when it creates a pull request:

* CI checks failing (`pull_request.checks.failed`)
* Review comments, both inline and top-level (`pull_request.review_comment.created`, `pull_request.comment.created`)
* Reviews that approve, request changes, or leave comments (`pull_request.review.approved`, `pull_request.review.changes_requested`, `pull_request.review.commented`)
* The PR merging or getting closed (`pull_request.merged`, `pull_request.closed_unmerged`)

This goes beyond forced subscriptions though. We allow the agent to subscribe to events on its own, both within a conversation (`watches`) and outside (`automations`), and tool results can suggest events worth watching.

Junior **is not** a coding harness. It is **not a harness** at all. It’s an agent, and yes it has its own harness it’s built on top of, but it’s expected to behave in a certain way. It’s not a tool you configure or decide how it should behave. Its behavior is encoded in markdown, in TypeScript, and in network policy. Our goal is that it should behave like you’d expect someone performing that task to. That’s why I want predictability.

Cursor leaves a comment suggesting there’s a bug. Junior adds a reaction (👀) to the comment to let you know it’s seen it.

![Junior acting on a review comment](https://cra.mr/assets/junior/comment-actioned.png)

Except it’s not a bug. As the conversation context clearly shows, I intentionally chose to break compatibility there. Junior understands that, says so, and adds a reaction (👎).

I go through and leave a handful of comments on the pull request, because it completely misunderstood what I meant to do. It should have been Golang not Rust, obviously. I click request changes, and it actually reads them, comes back, and acks all of my feedback. Oh, and now it needs to be rebased because something else landed in `main` - not a problem, as that event was bundled up with my pull request comments and it has the full scope of what needs to be done next.

This is the way we work, and it’s the way we should expect a product - dare I say, an assistant - that’s intended to help us “build more software” to work as well. So why are we still sitting there saying “go fix the PR” or “verify the feedback and action it but please dear god only if it’s proven by evidence oh and also don’t forget what the intent of this change was”.

## [#](https://cra.mr/a-little-determinism#letting-the-agent-choose-the-repository)Letting the agent choose the repository

You open up Claude Code and you select a repository to work on. I don’t do that in Slack, nor do I want to do that. It’s silly. That seems pretty easy to avoid, right? Just let it implicitly clone whichever repository you need.

Except in the real world our sandboxes are not uniform. When we’re working on Sentry we need a large collection of dependencies, which is completely different from the ones we need for another project. Most importantly, setting up those dependencies is often very slow, so we rely on a cache. This is solved the same way it’s been solved for more than a decade: we snapshot a base image based on some configuration. Sentry and an internal repo we call `getsentry` share a base image with all of their own deps. That’s an extension of our default base image, and completely different from the one `junior` uses to develop itself.

So you end up in a tricky scenario: how do you make sure you’re operating in the right sandbox, when you need a sandbox to operate, and you don’t know the repository up front? The answer for us: throw away the sandbox when you realize you need a different one. We do this once again with a similar pattern:

* expose `github_cloneRepository`
* deny a clone outside of that (easier said than done, btw)
* reject the tool call if the sandbox is wrong

We specifically reject the tool call when it’s on the `default` image. The rejection tells the agent what it should do next:

```
github_cloneRepository({ repo: "getsentry/sentry" })

Error: Repository getsentry/sentry is part of Workspaces "sentry", "getsentry".
Call switchWorkspace with one of those names; the checkout is already present
after the switch. Pass allowAdHoc=true only for an intentional ad-hoc checkout.
```

There’s also a way for the agent to bypass it. We’re not trying to stop it from doing what it needs to do, but we’re trying to guide it in the right direction.

You’ll note it’s not perfect. We’re throwing away a sandbox, but in practice it’s been very effective. In the rare situations where it had local state it needed to preserve, it’s always been able to rebuild it. This is one of the many areas where we find the best compromise: *do what you’d expect* vs *do what is the most technically correct*. Agents error all the time, recover from those errors, and this is no different.

## [#](https://cra.mr/a-little-determinism#making-a-focused-workflow-effective)Making a focused workflow effective

I feel like we’ve still only scratched the surface on automations within our workflows. We’ve solved what I’d consider to be some of the easiest, fairly objective behaviors. It’s been enough though that you miss them when you don’t have them - I’m already sick of having to repeat the same things to agents.

We’re using Vercel for this stack, but there’s nothing unique about Vercel. This same approach could be applied anywhere, and it’s hard to believe that model training or more prompting is going to avoid the need for this kind of thing.

The most important lesson I’ve taken away from this is how such little things can provide the biggest improvements in your workflows. The amount of time I save context switching by having an agent automatically be adversarial, but also addressable on pull requests is huge.

Next for us is more complex workflows, which I think we’ll drive with something like Luna or classifier models. For example, when a change affects a visual interface, I want to run a specific kind of visual QA workflow on top of it, and ensure it captures screencaps and attaches those to the pull request. We’ll likely force it with the same techniques from this post, but the *should it run* question has to move beyond a simple if statement.

If you’re interested in working on things like this, [you know where to find us](https://sentry.io/careers). [Junior itself is open source](https://github.com/getsentry/junior), though unless you’re willing to spend thousands a month on inference and compute, it’s probably not for you.

![A small figure in a Minion costume standing outside a frosted glass front door, waiting to be let in](https://cra.mr/assets/junior/junior-at-the-door.png)

Junior, waiting at the network boundary.
