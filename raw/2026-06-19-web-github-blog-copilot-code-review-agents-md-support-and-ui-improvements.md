---
source: "https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements/"
title: "Copilot code review: AGENTS.md support and UI improvements"
author: "unknown"
date_published: "2026-06-18"
date_clipped: "2026-06-19"
category: "Developer Tooling & AI Coding"
source_type: "web"
---
# Copilot code review: AGENTS.md support and UI improvements

Copilot code review now supports repository-level `AGENTS.md`

files, and it’s easier to request a review from Copilot on draft pull requests with the **Request** button. These changes are all generally available.

### 📝 `AGENTS.md`

Support

You can now add an `AGENTS.md`

file at the root of your repository to help shape Copilot code review feedback. If your repository already has an `AGENTS.md`

file, Copilot code review will now utilize that context automatically as part of its workflow. This makes it easier to get reviews that better reflect your repository’s conventions and expectations.

With this update, Copilot code review:

- Reads
`AGENTS.md`

from the root of your repository. - Uses relevant instructions from that file when generating review feedback.

### ✨ UI Updates

#### Request draft pull request reviews more easily

You can already request Copilot code review on draft pull requests to get a first pass on your draft before even publishing your pull request. Now, the **Request** button shows up next to Copilot on draft pull requests. This makes that workflow easier by letting you request Copilot directly from the reviewer picker without needing to search for Copilot first.

#### Collapsed Copilot review events on pull request timeline

On the **Conversation** tab of your pull request, Copilot code review events documented in the timeline can get noisy. We’ve collapsed certain Copilot code review timeline events together to help declutter your conversation tab, allowing you to find what matters, quickly.
