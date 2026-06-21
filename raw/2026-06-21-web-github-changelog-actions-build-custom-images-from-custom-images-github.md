---
source: "https://github.blog/changelog/2026-06-18-actions-build-custom-images-from-custom-images"
title: "Actions: Build custom images from custom images - GitHub Changelog"
author: "GitHub Changelog"
date_published: "2026-06-18"
date_clipped: "2026-06-21"
category: "DevOps & CI/CD"
source_type: "web"
---

# Actions: Build custom images from custom images - GitHub Changelog

Source: https://github.blog/changelog/2026-06-18-actions-build-custom-images-from-custom-images

Back to changelog
Improvement
June 18, 2026 •
1 minute read
Actions: Build custom images from custom images
Custom images for GitHub-hosted runners are getting new capabilities that give you more flexibility over how you compose and manage your image-generation pipelines.
You can now build custom images on top of other custom images, enabling layered image workflows for GitHub Actions. Teams can maintain a shared base image with common tooling and let individual teams build on top of it with their own dependencies. This reduces duplication and speeds up image builds.
Additionally, you can now use conditional logic around the snapshot keyword in your workflows to control when a new image version is generated. This gives you more flexibility over your testing and rollout strategy for your images.
For more information, check out our docs about custom images for GitHub Actions
actions
Copied
Shared
Back to changelog
Related Posts
Jun.18 Release
Safer pull_request_target defaults for GitHub Actions checkout
actions
supply chain security
Jun.18 Release
Control who and what triggers GitHub Actions workflows
actions
supply chain security
Jun.12 Retired
GitHub Actions: Minimum version enforcement timeline for self-hosted runners
actions
Jun.11 Improvement
Bot-created pull requests can run workflows if approved
actions
Jun.11 Release
New runner images in public preview
actions
Jun.11 Release
GitHub Agentic Workflows is now in public preview
actions
copilot
May.14 Improvement
GitHub Actions: Upcoming image migrations
actions
May.07 Improvement
GitHub Actions concurrency groups now allow larger queues
actions
Apr.27 Improvement
Copilot cloud agent starts 20% faster with Actions custom images
actions
copilot
Subscribe to our developer newsletter
Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.
Enter your email *
By submitting, I agree to let GitHub and its affiliates use my information for personalized communications, targeted advertising, and campaign effectiveness. See the GitHub Privacy Statement for more details.
Back to top
