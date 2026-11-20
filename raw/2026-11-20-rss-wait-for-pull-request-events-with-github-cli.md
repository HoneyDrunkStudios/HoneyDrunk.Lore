---
source: "https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli/"
title: "Wait for pull request events with GitHub CLI"
author: "Allison"
date_published: "2026-11-18"
date_clipped: "2026-11-20"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-11-20"
---

# Wait for pull request events with GitHub CLI

GitHub CLI now supports [GitHub Event Streams](https://github.blog/changelog/2026-11-17-github-event-streams-is-now-in-preview?utm_source=gh-cli-event-streams-changelog&utm_medium=changelog&utm_campaign=gh-cli-event-streams-nov-2026). With [`gh` v2.105.0](https://github.com/cli/cli/releases/tag/v2.105.0), you and your agents can wait for a pull request to change with a single command instead of polling it in a loop.

Run `gh event listen` with a pull request URL and the events you care about, such as a submitted review. It creates the subscription, opens the stream and prints each event as a line of JSON.

- By default, it exits after the first event, so it slots into scripts and agent loops.
- Use `--count` to wait for several events, `--follow` to keep listening, and `--timeout` to stop waiting.
- Use `--jq` or `--template` to pull out just the fields you need.

You can wait for submitted reviews, pull request state and head changes, merge conflicts and completed check suites. To manage subscriptions directly, use `gh event subscription create`, `list`, `view`, and `delete`.

Agents discover the new commands on their own: `gh pr create`, `gh pr view`, `gh run view`, `gh run watch`, and `gh api` now suggest `gh event listen` instead of polling.

## [Availability](https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli/#availability)

The `gh event` commands are in preview and may change. They require access to Event Streams, which is in preview on GitHub.com. To get access, [sign up for the Event Streams waitlist](https://gh.io/event-streams-signup).

To get started, upgrade to `gh` v2.105.0 or later. For details, see the [`gh event` manual](https://cli.github.com/manual/gh_event) and the [Event Streams documentation](https://docs.github.com/integrations/how-tos/using-github-event-streams?utm_source=gh-cli-event-streams-changelog-docs&utm_medium=changelog&utm_campaign=gh-cli-event-streams-nov-2026), or run `gh event --help`.

Share your feedback in the [GitHub Community discussion](https://github.com/orgs/community/discussions/211595?utm_source=gh-cli-event-streams-changelog-community-discussion&utm_medium=changelog&utm_campaign=gh-cli-event-streams-nov-2026).
