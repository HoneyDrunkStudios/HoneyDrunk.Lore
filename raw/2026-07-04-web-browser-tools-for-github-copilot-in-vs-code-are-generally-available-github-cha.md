---
source: "https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available"
title: "Browser tools for GitHub Copilot in VS Code are generally available - GitHub Changelog"
author: "Allison"
date_published: "2026-07-01"
date_clipped: "2026-07-04"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Browser tools for GitHub Copilot in VS Code are generally available - GitHub Changelog

Source: https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available

# Browser tools for GitHub Copilot in VS Code are generally available

*Editor’s note (July 1, 2026): Added more detail about which permissions stay under your control and the existing network domain controls.*

[Browser tools for GitHub Copilot](https://code.visualstudio.com/docs/debugtest/integrated-browser#_browser-tools-for-agents) in VS Code are now generally available. Agents can now drive a real browser, navigate live web apps, and feed what they find back into the chat. Browser tools are on by default with general availability, shaped by feedback from preview users.

[What agents do in the browser](https://github.blog#what-agents-do-in-the-browser)

Under the hood, agents get the same browser actions a developer would use. They can:

- Open pages and navigate, click, type, hover, drag, and handle dialogs.
- Read page content, capture console errors, and take screenshots.
- Run scripted flows when a sequence of steps is more efficient than tool calls.

DevTools are also right in the browser toolbar so you can inspect elements, view console output, and debug pages yourself.

[You stay in control](https://github.blog#you-stay-in-control)

**Your tabs are private by default:**The agent can’t read or interact with a page you opened until you select**Share with Agent**, and you can revoke that access at any time.**The agent’s tabs are isolated:**Pages the agent opens itself run in fresh sessions with no access to the cookies or storage from your everyday browsing. Agents running in parallel in the Agents window each keep their browser tabs private from one another.**Sensitive permissions stay under your control:**Capabilities like the camera, microphone, location, notifications, and clipboard reads are never granted automatically. Each one needs your explicit approval for a site, and agents can’t approve them on your behalf. Only low-risk actions, such as sanitized clipboard writes, are allowed by default.

[Enterprise controls](https://github.blog#enterprise-controls)

Admins can centrally manage browser tools:

- A new dedicated on/off switch (
`workbench.browser.enableChatTools`

) - Existing agent network domain controls (
`chat.agent.allowedNetworkDomains`

and`chat.agent.deniedNetworkDomains`

, enabled with`chat.agent.networkFilter`

) that restrict which sites agents and the integrated browser can reach. Denied domains take precedence, and both lists support wildcards (e.g.,`*.example.com`

). - Workspace trust and approval prompts still apply

[Get started](https://github.blog#get-started)

Browser tools are available in both the editor window and the [Agents window](https://code.visualstudio.com/docs/agents/agents-window). Update VS Code and ask the agent to open or test a page.

For details, see the [browser tools for agents docs](https://code.visualstudio.com/docs/debugtest/integrated-browser#_browser-tools-for-agents) and the [browser agent testing guide](https://code.visualstudio.com/docs/agents/guides/browser-agent-testing-guide), and share feedback in the [microsoft/vscode](https://github.com/microsoft/vscode/issues) repository.
