---
source: "https://github.blog/changelog/2026-04-24-notice-about-upcoming-new-format-for-github-app-installation-tokens"
title: "Notice about upcoming new format for GitHub App installation tokens"
author: "Allison"
date_published: "2026-04-24"
date_clipped: "2026-05-03"
category: "Security & Ethical Hacking"
source_type: "rss"
---

Starting **April 27th 2026** and over the coming weeks, we will begin a staged rollout that updates the format of newly minted [GitHub App installation tokens](https://docs.github.com/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation), making them more performant and improving the reliability of our API surface. If your application expects or relies on installation tokens being exactly 40 characters long, it may not handle this new token format correctly.

### What is changing?

We’re now supporting a new, stateless token format for GitHub App installation tokens that improves token issuance performance under increased load and helps us deliver higher reliability at scale.

Newly issued GitHub App installation tokens will use an updated format with the changes below:

- The overall length of the tokens will be longer (~520 characters) and will vary based on the data stored within it.

- The token format for installation tokens (`ghs_` tokens) will be changing to `ghs_APPID_JWT`.

Note that the prefixes for any of the [GitHub token types](https://docs.github.com/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#githubs-token-formats) is not changing and installation tokens will still be prefixed with `ghs_`.

The JWT is signed using a GitHub-internal issuer and cannot nor should not be validated by a client app. It contains details about the token such as the target installation, the application, and basic validation details. As with all access tokens, client apps must not take a dependency on the contents of this JWT.

### Scope

- Existing App installation tokens continue to work until they expire.

- This change applies to GitHub Enterprise Cloud and Data Residency environments. GitHub Enterprise Server isn’t impacted by this change.

- Upcoming rollouts will apply the new token format only to [GitHub App installation server-to-server tokens](https://docs.github.com/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app), including [Actions GITHUB_TOKEN](https://docs.github.com/actions/concepts/security/github_token).

- Not in scope yet, but we’ll share more details in the coming weeks on planned format changes for [user-to-server tokens](https://docs.github.com/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user) used in Copilot code review flows.

### What to expect over the next few weeks

In the coming weeks, we will be doing a staged rollout for the format changes to GitHub App installation tokens:

- **April 27 – mid-May 2026**: We’ll begin a staged rollout of the updated format to GitHub Actions-issued `GITHUB_TOKEN` and the GitHub App installation tokens issued to all the other first-party [featured integrations](https://docs.github.com/integrations/concepts/featured-github-integrations) (e.g., Dependabot, Slack, and Teams). This should not impact your existing Actions workflows. Reach out to [GitHub Support](https://docs.github.com/enterprise-cloud@latest/support/learning-about-github-support/about-github-support#scope-of-support) if you see this change affecting your Actions workflows and want to temporarily opt-out of the change.

- 
**Mid-May to late-June 2026**: We’ll begin a staged rollout of the updated format to all the GitHub App installation tokens. We will be providing more guidance over the coming weeks on how to test these new tokens locally to validate that your GitHub Apps continue to work as expected before we roll out the change more broadly. We’ll introduce a brownout period to identify integrations that still depend on token format assumptions, followed by broad enablement of the updated format.

### How to prepare for this change

It’s recommended that you treat tokens as opaque strings and avoid validating them against hardcoded patterns.

To help prepare for this change, ensure that:

- Your apps do not take a dependency on access tokens being a certain length.

- There are no regexes in your codebase such as `ghs_[A-Za-z0-9]{36}` that validate a token. These may not match the new tokens.

- Any database columns for access tokens can fit at least a 520 character string.

Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).

The post [Notice about upcoming new format for GitHub App installation tokens](https://github.blog/changelog/2026-04-24-notice-about-upcoming-new-format-for-github-app-installation-tokens) appeared first on [The GitHub Blog](https://github.blog).
