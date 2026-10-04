---
source: https://arrangeactassert.com/posts/convention-based-design-for-docs
title: 'One Folder, One Topic: Convention-Based Design for Docs'
author: Jag Reehal
date_published: '2026-09-30'
date_clipped: '2026-10-04'
category: Software Architecture
source_type: rss
capture_method: full-readable-extraction
---

# One Folder, One Topic: Convention-Based Design for Docs

Source: https://arrangeactassert.com/posts/convention-based-design-for-docs

[One Folder, One Topic: Convention-Based Design for Docs](https://arrangeactassert.com/posts/convention-based-design-for-docs/)

30 Sep 2026
Every company I have worked at has had the same documentation problem: teams need information they can find, share and trust.

At most of those companies, the answer has been Confluence, and the pages drift away from the code they describe.

At a payments client, we took a different approach. We created a convention: every repo keeps its docs in the same folder and carries the same GitHub topic. A small build discovers them, and Astro turns them into one site that engineers and AI agents can both read.

## Before: docs in Confluence

You wanted to know how a payment moves through the system. Search returned four Confluence pages. Two contradicted each other, one described a service we had deleted, and none said who owned it.

The code had moved on. The pages had not, because you can’t edit a wiki page in the same pull request as the code it describes.

AI agents had a different problem. An agent working in a repo sees the files in that repo but has no view of Confluence. Ours guessed from the code, or you pasted a page into the chat and hoped the page was current.

## The docs convention

We agreed three things and wrote them down in one README:

- Each repo keeps its docs as Markdown in
`docs/src/content/docs/`

. - Each page has a
`title`

in its frontmatter. - A repo joins the docs site by adding the
`docs`

GitHub topic.

```
any-repo/
src/
docs/
src/content/docs/
architecture.md
runbooks/
restarting-the-processor.md
```


We picked Starlight’s content path over a bare `docs/`

so each repo can build its own docs site from the same files.

A separate docs repo does the rest. Every 30 minutes a GitHub Action lists the repos with the topic, reads the git tree hash of each docs folder, and rebuilds when a hash changes.

flowchart LR A[Repo with docs topic] --> C[Docs repo: check tree hashes] B[Repo with docs topic] --> C C -->|hash changed| D[Sparse clone Markdown and images] D --> E[Astro Starlight build] E --> F[Cloudflare, behind SSO]

Finding the repos takes one API call:

```
gh api --paginate "orgs/$ORG/repos?per_page=100" \
--jq '.[] | select((.archived | not) and (.topics | index("docs"))) | .name'
```


The docs stay in their repos. The site gives you one view of them. The client’s site sits behind SSO, so you can browse [a public version built the same way](https://jagreehal.github.io/cbd-docs-site/) instead.

The docs repo holds no list of repos and no per-repo config. It asks GitHub which repos carry the topic and reads the same path in each. A team makes its repo discoverable, and the GitHub topic is the only registry. The tooling handles the tenth repo with the same code it used for the first.

## Where convention-based design comes from

Ruby on Rails made the idea famous as “convention over configuration”. Name a model `Payment`

, and Rails expects a `payments`

table and a `PaymentsController`

. You write configuration only when you break the convention.

Next.js brought the same idea to React. Add `pages/about.tsx`

and Next.js serves `/about`

. In the newer App Router, `app/dashboard/page.tsx`

becomes `/dashboard`

. If you know the framework, you can open a stranger’s Next.js codebase and find the routes in seconds.

This blog does it too: `foo-bar.md`

in `src/posts/`

publishes at `/posts/foo-bar/`

.

Rails and Next.js use convention to connect the parts of an application without configuration. I call it convention-based design when you use the same idea across repos: a predictable path becomes the contract between a repo and the tools that consume it.

## I have seen this work before

At Cambridge University Press we moved applications onto Kubernetes with the same idea. I wrote about it in [how Cambridge University Press adopted a shift-left culture](https://arrangeactassert.com/posts/how-cambridge-university-press-adopted-a-shift-left-culture/). A folder called `infrastructure`

in the repo root was all a Node.js application needed to run in Kubernetes. The operations team set the constraints, and the engineering teams followed one folder name.

Within a few months we had applications serving production traffic from Kubernetes, and teams built new applications Kubernetes-first. The deploy tooling found each app by its folder, the same way the docs site finds each repo by its topic and path.

## What the convention fixes

### You know where to look

Open any repo and the docs sit in the same place. You can read a service you have never touched without asking in Slack where its docs live.

Starlight checks the frontmatter when the site builds. A page without a `title`

breaks the build, so you find out the day you write it.

### The docs change with the code

A doc now lives in the same pull request as the change it describes. The reviewer reads both. If you rename an endpoint and leave the doc alone, the reviewer can see the gap in the diff.

One internal repo goes further and derives 95 user stories from its Playwright tests and stamps each with the git SHA it ran against. The build regenerates those pages when the tests change, so they match the behaviour the tests describe.

### Agents know where to look

An agent working in a repo reads the same Markdown the site renders, straight from disk. The path matters more than the format: once `docs/src/content/docs/`

is the convention, an agent finds the docs without a prompt telling it where someone decided to put them.

Matt Pocock argues that agents do their best work in codebases [built for them to explore](https://arrangeactassert.com/posts/why-matt-pocock-is-right-about-making-codebases-ai-agents-love/). A fixed docs path is one of the cheapest changes you can make toward that.

### One search box

The site gives each repo a sidebar group and puts every page behind one search. You search once, across the repos that publish, and each result has an owner.

### The team that owns the code owns the doc

The owner of a page is the team that owns the repo. A shared repo can name owners per folder in a `CODEOWNERS`

file. `git blame`

shows who changed a paragraph and in which pull request. When the team deletes a service, the same pull request can delete its docs, and the reviewer sees it. In Confluence, deleting the service leaves the page where it was.

### It took a day

One engineer built the docs repo, wired up a read-only GitHub App and deployed the site in a day. The client adopted it with a README and a topic, without a dedicated platform team or a developer portal.

Teams adopt it one repo at a time. Two repos publish today, and the next one needs a folder and a topic.

## How the Astro build works

[Starlight](https://starlight.astro.build), Astro’s docs theme, does most of the work:

- The build copies each repo’s Markdown into
`src/content/docs/<repo>/`

, and Starlight’s content collection turns each folder into a sidebar group. `docsSchema()`

validates the frontmatter of every page from every repo.- Search comes built in and indexes the whole site at build time.
- The output is static, so it deploys to Cloudflare and sits behind Cloudflare Access with Google SSO.

The docs repo reads other repos through a GitHub App that the organisation owns, with read-only access to contents. Each run mints a token that expires after an hour. The Cloudflare token holds one permission, to edit Workers scripts.

A small plugin rewrites links so a relative link works on GitHub, on the repo’s own Starlight site and on the central site. Each repo can still build its own site from the same folder, and two of them do.

## What comes next

The client rolled this out this week, so I have no numbers on onboarding or search yet. It also has gaps.

A malformed page fails the central build, up to 30 minutes after someone merges it. The author has moved on by then. A per-repo check would fail the pull request instead.

Nothing stops you deleting a page another repo links to. A backlink check fixes that.

Agents only see docs in the repo they work in. For an agent that needs another repo’s docs, the site can serve the same content in forms a machine reads. Markdown pages and `llms.txt`

cover simple discovery. An MCP search endpoint suits targeted lookups. Start with the Markdown and add MCP when plain HTTP falls short.

I built each of these in a set of public example repos. [cbd-handbook](https://github.com/jagreehal/cbd-handbook) holds a reusable docs-check workflow with the backlink guard. [cbd-docs-site](https://github.com/jagreehal/cbd-docs-site) publishes `llms.txt`

and Markdown twins. [cbd-docs-mcp](https://github.com/jagreehal/cbd-docs-mcp) serves the index to Claude.

The same pattern works beyond docs. Each example repo also commits its API and event schemas to `contracts/`

, and [cbd-catalog](https://github.com/jagreehal/cbd-catalog) finds them by topic and path and builds [an EventCatalog](https://jagreehal.github.io/cbd-catalog/) from them.

Each of those follows the argument I made in [AI code needs rules, not rituals](https://arrangeactassert.com/posts/ai-code-needs-rules-not-rituals/): write the standard down as a check the machine runs, then let people and agents work inside it.

If you want to try it this week, pick two repos, move their docs into the same folder and add a topic.

The site can come after.
