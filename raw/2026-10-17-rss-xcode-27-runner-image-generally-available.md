---
"source": "https://github.blog/changelog/2026-10-15-xcode-27-runner-image-generally-available"
"title": "Xcode 27 runner image generally available"
"author": "Allison"
"date_published": "2026-10-15"
"date_clipped": "2026-10-17"
"category": "DevOps & CI/CD"
"source_type": "rss"
---

# Xcode 27 runner image generally available

![](https://github.blog/wp-content/themes/github-2021-child/assets/img/featured-v3-new-releases.svg)

You can now use the generally available Xcode 27 runner image to build and test your Apple applications in GitHub Actions. Previously in public preview, this GitHub-hosted image runs on macOS 27 and includes the Xcode 27 toolchain and Apple SDKs.

## [Xcode-based images](https://github.blog/changelog/2026-10-15-xcode-27-runner-image-generally-available#xcode-based-images)

Each image supports one major Xcode version rather than targeting a specific operating system version. This makes it easier to select the toolchain your project needs and know what each runner provides.

## [Get started](https://github.blog/changelog/2026-10-15-xcode-27-runner-image-generally-available#get-started)

To use the image, set your workflow’s `runs-on:` value to one of these labels:

* `xcode-27`
* `xcode-27-xlarge`

If you already use these labels, you don’t need to change your workflows. The image is available on Apple Silicon (arm64) runners only, not Intel runners.

To view the installed software or report an issue, visit the [runner-images repository](https://github.com/actions/runner-images).
