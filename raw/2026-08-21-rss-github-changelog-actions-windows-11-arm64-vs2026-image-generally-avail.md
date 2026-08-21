---
source: "https://github.blog/changelog/2026-08-20-windows-11-arm64-vs2026-image-generally-available"
title: "Windows 11 arm64 VS2026 image generally available"
author: "unknown"
date_published: "2026-08-20"
date_clipped: "2026-08-21"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Windows 11 arm64 VS2026 image generally available

Source: https://github.blog/changelog/2026-08-20-windows-11-arm64-vs2026-image-generally-available

Back to changelog
Improvement
August 20, 2026 •
1 minute read
Windows 11 arm64 VS2026 image generally available
The Windows 11 arm64 image with Visual Studio 2026 is now generally available on standard and larger GitHub-hosted runners. To use it in GitHub Actions, update your workflow file to runs-on: windows-11-vs2026-arm .
Prepare for the upcoming migration
GitHub will gradually update the windows-11-arm image to use Visual Studio 2026 by default beginning September 21, 2026. GitHub will complete the rollout by September 30, 2026. During this period, your workflows will gradually move to the new image.
Breaking change: The move to Visual Studio 2026 may break workflows that depend on Visual Studio 2022.
You don’t need to take any action if you want your workflows to move to Visual Studio 2026. Update the runs-on: target in your workflow file to windows-11-vs2026-arm to test the new image before the migration.
If you no longer want to use the Windows 11 arm64 image:
For standard runners, edit your workflow to target a different runner .
For larger runners, change the image assigned to your runner .
For more information or questions, visit the runner-images repository .
actions
Share
Copied
Shared
Back to changelog
