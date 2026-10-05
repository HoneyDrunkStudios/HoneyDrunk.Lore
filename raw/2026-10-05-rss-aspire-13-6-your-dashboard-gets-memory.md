---
"source": "https://devblogs.microsoft.com/aspire/whats-new-aspire-13-6"
"title": "Aspire 13.6: Your dashboard gets memory"
"author": "Maddy Montaquila"
"date_published": "2026-09-29"
"date_clipped": "2026-10-05"
"category": ".NET Ecosystem"
"source_type": "rss"
---

# Aspire 13.6: Your dashboard gets memory

Aspire 13.6 is out today, and it includes potentially the longest awaited Aspire feature ever… [persistent dashboard data](https://github.com/microsoft/aspire/issues/4256)! The Aspire Dashboard now keeps your runs around so you can still see traces and logs after you’ve restarted your full stack. That alone would make this a stellar release, but 13.6 also lets you interact with any container shell from the dashboard, brings Java and Rust hosting into the first-party lineup, and previews a brand-new Azure deployment target.

As usual, these are some of my favorites, but the complete inventory, migration notes, and breaking changes are detailed in the [aspire.dev What’s New](https://aspire.dev/whats-new/aspire-13-6/).

## 🗄️ Your dashboard remembers

Finally!!! The dashboard now automatically stores resource snapshots and telemetry after you stop the apphost. When you start the apphost again, the dashboard starts a fresh “run”, and you can quickly swap between live and past sessions with the run selector.

Filtering, search, paging, and aggregation all work on historical runs, so investigating an old run still gives you all the power of the dashboard. Historical runs are read-only, so you can poke around without worrying about changing anything. The runs are stored on disk as SQLite databases, so you can point your coding agent at them to compare and contrast between runs, too.

The dashboard keeps up to 10 runs per application and prunes the oldest ones as new runs start. If a run captured something you want to hang onto, like the one time you actually reproduced a tricky bug, pin it in the run selector to retain it.

Running the [standalone dashboard](https://aspire.dev/dashboard/standalone/) without an apphost? Give it a stable application name and opt into **Resume** so the same run survives restarts:

`aspire dashboard run --application-name my-app --persistence Resume`


We also raised the default limits for console logs, structured logs, and traces to 100,000 entries each, so a busy run holds a lot more before the oldest entries roll off.

**Protect your telemetry**

Learn more about [dashboard data persistence](https://aspire.dev/dashboard/data-persistence/).

## ⌨️ Exec against your containers from the dashboard

When I want to check what’s actually installed on a container image, I usually drop into my container runtime of choice, find the tab that gives me a terminal, and start typing. If I want to do anything more complicated, like manually clear my cache, I have to copy-paste passwords or the connection string and hope I grabbed the right one.

In 13.6, we created the `WithRepl()`

extension for common container-based integrations:

Now, the resource has a **REPL** command in the dashboard. Click it, and the client bundled in the container opens in the dashboard’s new terminal dock, already authenticated. You can start querying without installing anything, copying credentials, or leaving the dashboard.

REPL support ships in preview for PostgreSQL (`psql`

), MySQL, SQL Server (`sqlcmd`

), MongoDB (`mongosh`

), Redis (`redis-cli`

), and Valkey, and we are excited to add more based on your feedback. Because it uses the resource’s real credentials with full write access, you have to opt in with `WithRepl()`

/ `withRepl()`

, and it only works in run mode.

The new experimental terminal dock APIs are fully accessible to you, so you can create and drive any terminals for any container or executable resource. We have a lot of plans for more built-in functionality with the dock, so we’re super excited to hear your feedback and see what you build!

This complements the [console-app resource support](https://aspire.dev/dashboard/terminals/) that started with `WithTerminal()`

in 13.5. A resource that is a standalone console app still gets its own fully interactive terminal on the Console page; now, you also have a generic shell to exec into any resource type.

Stay tuned for a deep dive blog on how all of this works, aka how @mitchdenny accidentally built the most powerful terminal emulator on the planet!

## ☕🦀 Java and Rust join the first-party lineup

Java and Rust developers have been orchestrating their apps thanks to the [Aspire Community Toolkit](https://github.com/CommunityToolkit/Aspire) for a while. In 13.6, both integrations move into Aspire itself as `Aspire.Hosting.Java`

and `Aspire.Hosting.Rust`

, reworked to match the experience you get with JavaScript, Python, and Go. Huge thanks to [@marshalhayes](https://github.com/marshalhayes) and [@afscrome](https://github.com/afscrome), whose community contributions made this happen.

Here’s a Spring Boot catalog service and a Cargo pricing API in the same apphost:

On the Java side, you also get Quarkus, executable JARs, and Maven or Gradle wrapper tasks. Aspire detects the target Java release from your build, configures OpenTelemetry export so your telemetry lands in the dashboard (add `WithOtelAgent()`

when you want the Java agent’s automatic instrumentation), and generates a multi-stage Dockerfile when you publish. Rust apps get Cargo target, argument, and feature configuration, plus a generated Dockerfile of their own.

Both languages also work with the [Aspire VS Code extension](https://marketplace.visualstudio.com/items?itemName=microsoft-aspire.aspire-vscode), so you can hit **Start Debugging** and set breakpoints in your Spring controller or Rust handler alongside the rest of your app.

**Preview packages**

`Aspire.Hosting.Java`

and `Aspire.Hosting.Rust`

ship as preview packages in 13.6. If you’re coming from the Toolkit, follow the migration guidance in the [Java](https://aspire.dev/integrations/frameworks/java/java-host/)and

[Rust](https://aspire.dev/integrations/frameworks/rust/rust-host/)hosting docs.

And yes, for the adventurous, Java and Rust apphost authoring is also available behind [experimental feature flags](https://aspire.dev/reference/cli/configuration/#toggle-preview-feature-experiences).

## 📂 One volume path, local and deployed

If your app writes files, it needs a directory. Locally that’s a path on your machine, and in a container it’s a mount path like `/data`

. That difference usually ends up as a little bit of environment-sniffing code in your app.

13.6 adds an `env`

argument to any executable’s volume mount, so your app reads one environment variable everywhere:

When you run locally, `DATA_PATH`

points to a stable, workload-specific directory in the apphost’s local store. When you publish to Docker Compose, Kubernetes, or a managed cloud like Azure Container Apps, `DATA_PATH`

is `/data`

. Your app code just reads `DATA_PATH`

and moves on with its life.

See [Persist data with volume resources](https://aspire.dev/fundamentals/persist-data-volumes/) for the details, including how this works with 13.5’s [persistent volume support for Kubernetes](https://aspire.dev/deployment/kubernetes/persistent-volumes/).

## ☁️ Deploy to Azure Container Apps Sandboxes

The new `Aspire.Hosting.Azure.Sandboxes`

package adds [Azure Container Apps Sandboxes](https://aspire.dev/deployment/azure/sandboxes/) as a deployment target, so each of your projects, containers, and Dockerfile resources runs in its own isolated sandbox. Add a sandbox group to your apphost and run `aspire deploy`

. Aspire provisions the group, a container registry, and the identities and role assignments it needs. If the sandbox group is your only compute environment, Aspire assigns your compute resources to it automatically.

When you want more control, pick a tier and configure auto-suspend:

As always, Aspire’s defaults lean safe. Only endpoints marked external get a public HTTPS URL, and those URLs require Microsoft Entra ID authentication unless you opt a specific endpoint into anonymous access. Egress is deny-by-default, and Aspire cleans up stale sandboxes on redeploy and on `aspire destroy`

.

**Preview**

Get started with [Deploy to Azure Container Apps Sandboxes](https://aspire.dev/deployment/azure/sandboxes/). If you’re deploying to regular Azure Container Apps, you can also try the experimental [Express mode](https://aspire.dev/deployment/azure/container-apps/#express-environments) with `AsExpress()`

for faster provisioning and scale-to-zero.

## 🧪 C# devs: help us try the new .NET project experience

If you’re building with C#, 13.6 has something new for you to kick the tires on. `AddDotnetProject`

, from the prerelease `Aspire.Hosting.Dotnet`

package, is the next version of how Aspire builds and runs your .NET projects, bringing it to parity with the modernized experience for every other language resource. You point it straight at a `.csproj`

, so there’s no `ProjectReference`

to wire up in your apphost:

Instead of restoring and building every project on its own, Aspire groups compatible projects and builds them together with one shared NuGet restore. On a new enough .NET 11 SDK, it also turns on MSBuild’s multithreaded task execution. When you change code, hit the resource’s **Rebuild** command, and **Start** and **Restart** reuse the coordinated build output. This also means the Aspire dashboard, and any other resources, will start sooner since Aspire doesn’t have to wait for the entire MSBuild graph to resolve.

Already have an apphost full of `AddProject`

calls? Run `aspire agent init`

and run the `aspire-project-v2-migration`

skill. Your agent assesses each project resource, proposes the exact edits, and waits for your approval before touching anything. This is still prerelease, so now is the perfect time to try it on a real app and tell us what breaks. Learn more about [coordinated builds and restore](https://aspire.dev/integrations/dotnet/project-resources/#coordinated-builds-and-restore) and [migrating from legacy project resources](https://aspire.dev/integrations/dotnet/project-resources/#migrate-from-legacy-project-resources).

## 🏅 Grab bag

Some other things you might be hoping to hear about shipped in 13.6:

`aspire run`

and`aspire start`

accept`--launch-profile`

(or`-lp`

) to pick an apphost launch profile.`aspire stop --force --volumes`

also removes the volumes Aspire created, while leaving bind mounts and pre-existing volumes alone.- Coding agents can start and stop apphosts through the VS Code extension’s lifecycle tools, and the Aspire pane now has
**Deploy**and**Publish**actions right next to**Run**. - Deno 2 can run your TypeScript apphost, and
`AddDenoApp`

/`addDenoApp`

hosts Deno apps. Thanks to[@rickylabs](https://github.com/rickylabs)for both! - TypeScript apphosts load
`appsettings.json`

from the apphost directory, just like C# apphosts. - MongoDB gets an experimental
`WithReplicaSet()`

so you can use transactions and change streams locally.

## 💫 Get Aspire 13.6

Update the CLI, your apps, and your agent skills:

```
aspire update --self
aspire update
aspire agent init
```


Then run your app, restart it a couple of times, and open the run selector in the dashboard. Add `WithRepl()`

to your database while you’re in there, or drop a Spring Boot or Rust service into your apphost and see how it feels.

**New to Aspire?** [Install the CLI](https://get.aspire.dev) with your package manager of choice, and try the [Aspireify](https://aspire.dev/get-started/add-aspire-existing-app-typescript-apphost/) skill on your existing apps.

Share feedback on [GitHub](https://github.com/microsoft/aspire), join us on [Discord](https://aka.ms/aspire-discord), follow [@aspiredotdev on X](https://x.com/aspiredotdev), find us on [BlueSky](https://bsky.app/profile/aspire.dev), or subscribe on [YouTube](https://www.youtube.com/@aspiredotdev).

Happy Aspirifying! 💫
