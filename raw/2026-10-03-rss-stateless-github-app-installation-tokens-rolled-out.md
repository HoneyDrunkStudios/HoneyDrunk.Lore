---
"source": "https://github.blog/changelog/2026-10-02-stateless-github-app-installation-tokens-rolled-out"
"title": "Stateless GitHub App installation tokens rolled out"
"author": "Allison"
"date_published": "2026-10-02"
"date_clipped": "2026-10-03"
"category": "Security & Ethical Hacking"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# Stateless GitHub App installation tokens rolled out

# Stateless GitHub App installation tokens rolled out

The staged rollout of the stateless GitHub App installation token format, which began on April 27, 2026, is complete. By default, all newly minted GitHub App installation tokens will be in the stateless `ghs_APPID_JWT`

format, which makes token issuance and validation faster and improves the reliability of the GitHub API.

[What’s changed](#whats-changed)

Installation tokens still start with the `ghs_`

prefix, but they’re now about 520 characters long instead of 40.

Token permissions, repository scoping, the one-hour expiration, and the installation access token REST API endpoint are unchanged. Tokens minted before the change continue to work until they expire.

[What to expect going forward](#what-to-expect-going-forward)

The temporary `X-GitHub-Stateless-S2S-Token`

request header, which we introduced so you could validate the new format on demand, will be deprecated on November 30, 2026. After that date, GitHub will no longer respect the header, and all eligible apps will always receive stateless tokens. To learn more about the temporary header, see [our original changelog for its release](https://github.blog/changelog/2026-05-15-github-app-installation-tokens-per-request-override-header/).

Once you’ve validated your apps and workflows with both token formats, remove the header from your production code before November 30, 2026.

[Check your integrations](#check-your-integrations)

If you haven’t already, confirm that every system that handles installation tokens treats them as opaque strings. Look for:

- Validation that requires tokens to be exactly 40 characters or patterns written for the legacy format.
- Database columns, secret stores, or environment variables with a fixed or small maximum length.
- Proxies, gateways, or middleware that truncate or reject long
`Authorization`

headers. - Logging and secret redaction rules that only match the legacy token pattern.

To learn more, see [Generating an installation access token for a GitHub App](https://docs.github.com/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app).
