---
source: "https://github.blog/changelog/2026-10-14-github-actions-workflow-lockfiles-in-public-preview"
title: "GitHub Actions workflow lockfiles in public preview"
author: "Allison"
date_published: "2026-10-14"
date_clipped: "2026-10-16"
category: "DevOps & CI/CD"
source_type: "rss"
date_modified: "2026-10-14"
---

# GitHub Actions workflow lockfiles in public preview

GitHub Actions workflow dependency lockfiles are now in public preview for GitHub Enterprise Cloud, GitHub Enterprise Cloud with data residency, Team, and Free plans. Tags and branches can move after you review a workflow, so a later run might execute different code. Lockfiles let you keep those references in your workflow while running the exact commits you locked.

*Editor’s note (October 14th, 2026): Updated which plans have access to this public preview.*

If an action is compromised, a moved tag or branch can introduce malicious code into your workflow without a change to your repository. Lockfiles help protect against unexpected dependency changes by keeping workflow runs tied to the commits you locked. Locking does not determine whether the dependency itself is safe, so review dependencies before locking them.

Install the `gh actions-lock`

extension for the GitHub CLI to create and maintain your workflow lockfile. With the extension, you can:

**Pin your dependencies:**Generate`.github/workflows/actions.lock`

with reviewable commits for actions and their transitive dependencies, as well as reusable workflow dependencies.**Adopt locking gradually:**Onboard workflows individually. Once onboarded, a workflow must have lockfile entries for its dependencies, and GitHub Actions runs the recorded commits.**Keep workflow runs consistent:**GitHub Actions requires each dependency of an onboarded workflow to be in the lockfile and uses its recorded commit, even if a tag or branch moves.**Check for stale lockfiles:**Verify that the lockfile is up to date without modifying files, including in a CI check.

The **Require lockfile** policy is also available in public preview. Enterprise, organization, and repository administrators can require workflows to use lockfiles across their enterprise, organization, or repository.

[Keep locked dependencies up to date with Dependabot](https://github.blog#keep-locked-dependencies-up-to-date-with-dependabot)

Dependabot helps you keep your GitHub Actions dependencies up to date. When it opens a version update for an action in a workflow that is already onboarded, it also regenerates the matching lockfile entry in the same pull request, keeping the updated workflow reference and its locked commit in sync without additional configuration. Read more about [Dependabot updates for actions](https://docs.github.com/code-security/concepts/supply-chain-security/dependabot-version-updates#updates-for-actions).

[Get started](https://github.blog#get-started)

To get started, install the extension from the [public gh-actions-lock repository](https://github.com/github/gh-actions-lock), then review and commit the generated lockfile and workflow changes.

For more details and links to setup instructions, see [workflow dependency lockfiles](https://docs.github.com/actions/concepts/security/workflow-dependency-lockfiles) in GitHub Docs.

Share feedback in the [existing community discussion](https://github.com/orgs/community/discussions/194494) or [open an issue in the gh-actions-lock repository](https://github.com/github/gh-actions-lock/issues).

Thank you to the community members who helped shape this preview through testing and feedback, with special thanks to Andrew Nesbitt, François Proulx, Jesse Houwing, and William Woodruff for their close collaboration and iteration on this solution over the past year.
