---
source: "https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max/"
title: "Agent tasks REST API now available for Copilot Pro, Pro+, and Max"
author: "Allison"
date_published: "2026-06-04"
date_clipped: "2026-06-05"
category: "DevOps & CI/CD"
source_type: "web"
---

# Agent tasks REST API now available for Copilot Pro, Pro+, and Max

Source: https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max/

Release

# Agent tasks REST API now available for Copilot Pro, Pro+, and Max

Copilot Pro, Pro+, and Max users can now programmatically start and track [Copilot cloud agent](https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent) tasks with the Agent tasks REST API, available in public preview.

Copilot cloud agent works in the background in its own development environment, where it can make and validate code changes, then open a pull request.

The API makes it easy to weave Copilot cloud agent into custom automations. For example, you could:

- Fan out refactors or migrations across many repositories from a simple script.
- Set up new repositories in one click from your company’s internal developer portal.
- Automatically prepare a new release each week, including release notes.

Once you’ve started a task, you can also track progress through the API. The API supports authentication with personal access tokens (classic and fine-grained) and OAuth tokens.

To learn more, head to the [agent tasks REST API documentation](https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task).
