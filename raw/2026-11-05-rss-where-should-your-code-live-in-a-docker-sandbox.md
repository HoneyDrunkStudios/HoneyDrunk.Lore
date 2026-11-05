---
source: "https://www.docker.com/blog/docker-sandbox-code-checkout-workflows"
title: "Where should your code live in a Docker Sandbox?"
author: "David Karlsson"
date_published: "2026-11-02"
date_clipped: "2026-11-05"
category: "DevOps & CI/CD"
source_type: "rss"
canonical_url: "https://www.docker.com/blog/docker-sandbox-code-checkout-workflows/"
source_last_modified: "2026-11-03"
---

# Where should your code live in a Docker Sandbox?

Giving an agent a sandbox also means deciding which files it will work on. You can share a checkout from your host, give it a separate working directory for a task, or keep the repository entirely inside the sandbox. Each arrangement changes how you, the human, participate in the work.

You might want to watch the diff in your local editor and make changes alongside the agent, or give it room to manage several tasks while you review the results. `sbx` supports both. The way you organize the checkout can change as you ask the agent to take on more of the work.

## Mounting a repository from your host

Sharing a checkout puts the agent in the working tree you already use. Run `sbx run` from your project directory, and it mounts that directory at the same absolute path inside the sandbox:

```

$ cd ~/my-project
$ sbx run claude
```

Open a file in your local editor while the agent works on it, and you’ll see changes as they happen. Git works from either side, so you choose whether you want to let the agent make commits or you do it yourself. Development servers on your host can pick up the edits through hot reload, using the runtime and dependencies installed on your host.

This fits close collaboration on one task. The coordination cost comes from sharing that working tree: switching branches changes the files the agent sees, and your edits become part of its ongoing work. If you want to switch to something unrelated while the agent continues, you’ll need another checkout.

**NOTE:** Dependencies written into the shared checkout are shared too. Packages with native binaries, such as [esbuild](https://esbuild.github.io/getting-started/#simultaneous-platforms), may work in the Linux sandbox and fail on a macOS or Windows host. Reinstalling on the host can reverse the problem. Keep separate dependency installations, or run the app consistently in one environment.

## Give each task a separate working tree

Git worktrees give each task a directory and branch. You can mount each worktree in its own sandbox, while your original checkout remains available for other work. The agent’s edits appear in the worktree. You can inspect either with your local editor and development tools. Each task also gets its own running environment, with tools to prepare and a sandbox and worktree to clean up afterward.

![image3 2](https://www.docker.com/app/uploads/2026/10/image3-2.png "- image3 2")

There is a Git limitation with mounting only a linked worktree. Its `.git` file points to metadata outside the mount, which the agent can’t reach. It can edit files, but checking status, branching, and committing have to happen on the host. The future of software development still needs you to run `git status`.

sbx supports a [clone mode](https://docs.docker.com/ai/sandboxes/workflows/git/#clone-mode) that gives the agent a separate checkout with Git available inside the sandbox. You keep your local project, but `sbx` mounts the host source as read-only and creates an independent clone for the agent. Its branch changes and dependency installations stay in its checkout.

![image1 2](https://www.docker.com/app/uploads/2026/10/image1-2.png "- image1 2")

Bringing the result back becomes a handoff. While the sandbox is running, you can fetch committed branches through the Git remote `sbx` adds on your host. Or the agent can push to the repository’s remote and you can retrieve the branch through your usual Git workflow. Your local editor and development server see the changes after you bring them into your checkout.

## Keep the project inside the sandbox

A mountless sandbox has no host workspace directory attached. Clone the repository inside it, and the sandbox holds the checkout and its development environment. Your host copy of the project shares no connection with the sandbox checkout.

![image2 2](https://www.docker.com/app/uploads/2026/10/image2-2.png "- image2 2")

This workflow resembles working on a remote development machine. Agents connect to the project environment, and you can open a shell with `sbx exec` or connect an editor to the sandbox over SSH. Changes and dependency installations stay separate from your host. To bring work back, you push a branch to the Git remote.

One sandbox per project can be a useful mental model here. The project and its tools persist across agent sessions and sandbox restarts. An agent can create worktrees per feature it’s working on, push branches, and create pull requests for review. Starting another task doesn’t require you to prepare another host worktree and sandbox, and the agent has Git access in each working directory. Clone mode supports this internal-worktree approach too.

Those tasks share tools and services, so running servers or changing the environment still needs coordination. Separate sandboxes are useful when tasks need independent environments as well as separate files. Branches alone don’t isolate simultaneous edits in one working directory.

That independence adds some distance when you want to try the result. Your usual local editor isn’t looking at these files, and a development server running inside the sandbox needs a published port to reach it from your browser.

For a web app preview, ask the agent:

Start the development server on port 8080, bound to `0.0.0.0.`

Then publish the port from another terminal on the host:

```

$ sbx ports my-sandbox --publish 8080:8080
```

Open `http://localhost:8080` in your browser. It’s possible to work interactively this way, but there’s more ceremony than opening a project already on your filesystem.

An environment file can make setup repeatable, selecting tools and cloning the repository at creation with something like the community [github-clone kit](https://github.com/docker/sbx-kits-contrib/tree/main/github-clone). Recreating the sandbox then gives you a fresh environment. Push or copy out work you want to retain first: removing a sandbox deletes files held only there.

## Choose the repositories for the job

An API change might need a corresponding frontend change, or another repository might provide useful reference material. You can mount several directories into one sandbox, with read-only access for reference repositories. Local editing and previews remain available, but each writable checkout needs branch and change coordination. Task-specific checkouts also leave directories to clean up afterward.

A workspace manager such as [jganoff/wsp](https://github.com/jganoff/wsp) can assemble selected repositories for a task. Mounting that workspace gives the agent the projects it needs together. These are standard clones with their own Git metadata, so the agent retains Git access, unlike a mounted linked worktree.

The same scope fits inside a mountless sandbox: clone the repositories needed there and keep the whole workspace in the sandbox. The number of repositories and where their files live are separate choices.

## Combine the choices to suit the work

The checkout’s location, the sandbox’s lifetime, and the repositories it contains are choices you can combine. You can keep a project sandbox around for many tasks, or mount a workspace assembled for one job. What suits you may change when you want to work more closely with the agent, or give it more room to manage the work itself.

The [Git workflows documentation](https://docs.docker.com/ai/sandboxes/workflows/git/) covers the mechanics of direct mounts, clone mode, and host worktrees.
