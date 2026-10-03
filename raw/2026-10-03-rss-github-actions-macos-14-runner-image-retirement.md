---
"source": "https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement"
"title": "GitHub Actions: macOS 14 runner image retirement"
"author": "Allison"
"date_published": "2026-10-01"
"date_clipped": "2026-10-03"
"category": "DevOps & CI/CD"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# GitHub Actions: macOS 14 runner image retirement

Retired

# GitHub Actions: macOS 14 runner image retirement

The macOS 14 runner image will be retired on November 2, 2026. To raise awareness of the upcoming removal, jobs using macOS 14 will temporarily fail during the following scheduled brownout periods:

- October 5, 14:00 UTC to October 6, 00:00 UTC
- October 12, 14:00 UTC to October 13, 00:00 UTC
- October 16, 14:00 UTC to October 17, 00:00 UTC
- October 19, 14:00 UTC to October 20, 00:00 UTC
- October 23, 14:00 UTC to October 24, 00:00 UTC
- October 26, 14:00 UTC to October 27, 00:00 UTC
- October 29, 14:00 UTC to October 30, 00:00 UTC
- October 30, 14:00 UTC to October 31, 00:00 UTC

This deprecation includes the following labels:

`macos-14`

`macos-14-large`

`macos-14-xlarge`


During the lead-up to retirement, GitHub may reduce macOS 14 runner capacity, which could result in longer queue times for jobs that continue to use these labels.

[What you need to do](#what-you-need-to-do)

Update your workflow files to use one of the following macOS arm64 labels:

`macos-latest`

(`macos-26`

)`macos-15`

`macos-latest-xlarge`

(`macos-26-xlarge`

)`macos-15-xlarge`


For up-to-date information about available tools and software, see the [runner images repository](https://github.com/actions/runner-images). If you run into problems or need help, contact [GitHub Support](https://support.github.com/contact?form%5Bsubject%5D=Re%3A+GitHub+Actions&tags=dotcom-contact-params).
