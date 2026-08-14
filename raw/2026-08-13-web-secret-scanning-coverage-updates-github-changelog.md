---
source: "https://github.blog/changelog/2026-08-07-secret-scanning-coverage-updates/"
title: "Secret scanning coverage updates - GitHub Changelog"
author: "Allison"
date_published: "2026-08-07"
date_clipped: "2026-08-13"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Secret scanning coverage updates - GitHub Changelog

Source: https://github.blog/changelog/2026-08-07-secret-scanning-coverage-updates/

# Secret scanning coverage updates

This release expands secret scanning’s coverage with more secrets blocked by push protection, one new secret scanning partner, and richer metadata on alerts.

## Secret scanning partnership program

Lovable Labs is now a GitHub secret scanning partner. Secret scanning now automatically detects the following new secret type in your repositories.

| Provider | Secret type |
|---|---|
| Lovable Labs | `lovable_api_key` |

When a Lovable Labs secret is found in a public repository, GitHub forwards it to Lovable Labs so they can take appropriate action. Learn more about the secret scanning partner program.

## Push protection defaults expanded

The following detectors are now included in push protection by default. Repositories with secret scanning enabled, including free public repositories, will automatically block commits containing these secrets.

| Provider | Secret type |
|---|---|
| APIclub | `apiclub_api_key` |
| Mistral AI | `mistral_ai_api_key` |
| PostHog | `posthog_oauth_access_token` |
| Resend | `resend_api_key` |

## Extended metadata support

Extended metadata builds on secret scanning’s validity checks, which confirm whether a detected secret is still active. When information is available from the provider, alerts also surface context (e.g., the secret’s owner, its creation and expiry dates, and the associated project or organization) so you can assess ownership and impact without leaving the alert. The following patterns now include extended metadata when detected.

| Provider | Secret type |
|---|---|
| Cohere | `cohere_api_key` |
| GoCardless | `gocardless_live_access_token` |
| GoCardless | `gocardless_sandbox_access_token` |
| Square | `square_access_token` |

Metadata availability varies by provider, token type, and even by individual secret, so GitHub makes a best effort to display it when present.

## Learn more

Learn more about secret scanning and reviewing extended metadata on an alert, and see the full list of supported secrets in our documentation. Let us know what you think in the community discussion.
