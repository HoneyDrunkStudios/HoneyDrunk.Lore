---
source: "https://github.blog/changelog/2026-06-11-new-runner-images-in-public-preview/"
title: "New runner images in public preview - GitHub Changelog"
author: "unknown"
date_published: "2026-06-11"
date_clipped: "2026-06-12"
category: "DevOps & CI/CD"
source_type: "web"
---

Two new GitHub-hosted runner images for GitHub Actions are now available in public preview for all users, giving you early access to test your workflows on the latest platforms before they reach general availability.

## [Ubuntu 26.04](#ubuntu-26-04)

The Ubuntu 26.04 image is now available for both x64 and arm64 architectures. To start using it, update your workflow file to use `runs-on: ubuntu-26.04` or `runs-on: ubuntu-26.04-arm`. Ubuntu 26.04 base images are also available for larger runner users.

Some users may notice differences in their workflows as the Ubuntu 26.04 image has different tools and tool versions compared to earlier images. For the full list, head to the [runner-images repository](https://gh.io/actions-image-changes).

## [Windows 11 arm64 with Visual Studio 2026](#windows-11-arm64-with-visual-studio-2026)

A new Windows 11 arm64 image with Visual Studio 2026 is now available under the label `windows-11-vs2026-arm`. This image provides an early, stable environment to validate your CI workloads against the Visual Studio 2026 toolchain on Windows arm64 without disrupting existing pipelines. See the [runner-images repository announcement](https://gh.io/actions-image-changes) for more information.

This image runs in parallel with the existing Windows 11 arm64 image for a limited period, allowing you to adopt and test at your own pace. At the end of the public preview in early September, the existing `windows-11-arm` image label will migrate to the vs2026 image. We will notify users ahead of the migration to give them time to prepare.

---

If you spot any issues with your workflows when using these new images, or if you have feedback on the software installed, head to the [runner-images repository](https://github.com/actions/runner-images).

While these images are in preview, you may experience longer queue times during peak usage hours.
