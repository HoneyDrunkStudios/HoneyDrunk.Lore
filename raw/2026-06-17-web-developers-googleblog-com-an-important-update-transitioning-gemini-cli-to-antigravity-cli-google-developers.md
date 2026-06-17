---
source: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
title: "An important update: Transitioning Gemini CLI to Antigravity CLI- Google Developers Blog"
author: "Dmitry Lyalin; Taylor Mullen"
date_published: "2026-05-19"
date_clipped: "2026-06-17"
category: "Developer Tooling & AI Coding"
source_type: "web"
---
# An important update: Transitioning Gemini CLI to Antigravity CLI

MAY 19, 2026

[Dmitry Lyalin](/search/?author=Dmitry+Lyalin)
Group Product Manager

[Taylor Mullen](/search/?author=Taylor+Mullen)
Principal Engineer

Share

- [Facebook](https://www.facebook.com/sharer/sharer.php?u={url} "Share on Facebook")
- [Twitter](https://twitter.com/intent/tweet?text={url} "Share on Twitter")
- [LinkedIn](https://www.linkedin.com/shareArticle?url={url}&mini=true "Share on LinkedIn")
- [Mail](mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20{url} "Send via Email")

![GeminiCLI-AntigravityCLI_1200x600_BlogHeader](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/GeminiCLI-AntigravityCLI_1200x600_BlogHeader.original.png)

When we shipped Gemini CLI last year, our goal was to bring the magic of Gemini directly into your terminal. Along the way, we’ve learned a lot from our community of millions of users, with over 100,000 GitHub stars, 6,000 merged pull requests, and hundreds of contributors, including: you love a good terminal UI, you appreciate that we ship weekly releases, and your workflows have simply outgrown those early days of 2025.

Gemini CLI proved the terminal could be an incredible interface for agentic tasks, but your needs shifted. You now require multiple agents communicating with each other to split up the work and solve complex problems. This means your terminal tools need to share a unified backend with the rest of your workflow.

Listening to your feedback made one thing clear: we can serve you best by pouring our energy into a single product built for today's multi-agent reality. To deliver the single platform you need to build the future, we're unifying our efforts into [Google Antigravity](http://antigravity.google/blog/introducing-google-antigravity-2-0), our premier agent-first development platform, which includes a powerful server-side harness and a brand-new terminal experience: [Antigravity CLI](http://antigravity.google/blog/introducing-google-antigravity-cli).

While there won't be 1:1 feature parity right out of the gate, we made sure Antigravity CLI keeps the most critical features of Gemini CLI: Agent Skills, Hooks, Subagents, and Extensions (now as Antigravity plugins). Whether you use Gemini CLI to get quick, grounded answers, scaffold and build out a new coding project, or help provision your cloud infrastructure, you can still do all of that right in Antigravity CLI. And to make your experience better, we focused on the things that matter most to you, like:

- Faster execution: Built in Go, Antigravity CLI is snappier and more responsive.
- Asynchronous workflows: Antigravity CLI orchestrates multiple agents for complex tasks in the background, letting you run large-scale refactors or research several topics without locking up your terminal session.
- Unified architecture: Antigravity CLI shares the same agent harness as [Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0), the new Antigravity desktop application, ensuring that all future improvements to core agents are automatically applied wherever you use them.

### **Important timeline for Consumers**

Starting today, [Antigravity CLI](https://antigravity.google/download) is available to everyone.

On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop serving requests for Google AI Pro and Ultra, as well as those using it free of charge using [Gemini Code Assist for individuals](https://developers.google.com/gemini-code-assist/docs/overview#supported-features-gca).

We are here to help make the transition to Antigravity CLI and Antigravity 2.0 as smooth as possible. You can get started now with our [technical documentation](http://antigravity.google/docs/gcli-migration), and we will be releasing video walkthroughs in the coming weeks.

For [Gemini Code Assist for GitHub](https://developers.google.com/gemini-code-assist/docs/review-repo-code), this change will also apply and on June 18, 2026, there will be no new installations on Github organizations and requests in the following weeks will stop being served.

### **For enterprise customers**

If your organization uses Gemini CLI or our IDE extensions via a Gemini Code Assist Standard or Enterprise license, or if your organization uses Gemini Code Assist for GitHub through Google Cloud, your access remains unchanged. We’ll continue to support Gemini CLI and Gemini Code Assist with access to the latest Gemini models and other updates. Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys. And if you’re excited to try Antigravity CLI, you can use it now with your [Google Cloud projects](http://antigravity.google/blog/google-antigravity-for-enterprises).

We welcome your feedback in the Antigravity CLI [community forum](https://github.com/google-antigravity/antigravity-cli), especially if there is a feature you’d like to request during this transition. We look forward to seeing what you build next with Antigravity 2.0 and Antigravity CLI.

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content=).

posted in:

- [AI](/search/?technology_categories=AI)
- [Announcements](/search/?content_type_categories=Announcements)
- [Learn](/search/?content_type_categories=Learn)

Previous

Next

Related Posts

[![DiffusionGemma: The Developer Guide](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/diffusion_banner.2e16d0ba.fill-800x400.png)

AI
Announcements
Explore

DiffusionGemma: The Developer Guide

JUNE 10, 2026](/diffusiongemma-the-developer-guide/)
[![Unlocking the Power of the TPU Stack: Introducing our new Developer Hub](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/TPU_v5e_-_Board_4_-_Web.2e16d0ba.fill-800x400.jpg)

AI
Cloud
Announcements
Learn

Unlocking the Power of the TPU Stack: Introducing our new Developer Hub

JUNE 16, 2026](/unlocking-the-power-of-the-tpu-stack-introducing-our-new-developer-hub/)
[![Enhance Security and Trust: New Session Metadata in Sign in with Google](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/banner-usability-safety-updates-go.2e16d0ba.fill-800x400.png)

Mobile
Web
Announcements
Best Practices

Enhance Security and Trust: New Session Metadata in Sign in with Google

JUNE 16, 2026](/enhance-security-and-trust-new-session-metadata-in-sign-in-with-google/)
