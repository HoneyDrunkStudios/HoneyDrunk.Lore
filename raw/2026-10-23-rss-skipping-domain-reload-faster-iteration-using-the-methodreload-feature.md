---
source: "https://unity.com/blog/skipping-domain-reload-faster-iteration-using-the-methodreload-feature"
title: "Skipping domain reload: faster iteration using the MethodReload feature"
author: "Théo Richart; Mike Geig"
date_published: "2026-10-22"
date_clipped: "2026-10-23"
category: "Game Development / Unity"
source_type: "rss"
---

# Skipping domain reload: faster iteration using the MethodReload feature

Source: https://unity.com/blog/skipping-domain-reload-faster-iteration-using-the-methodreload-feature

We've all been there: you tweak some gameplay code and then wait for the Editor to complete a domain reload. The process can slow down your iteration time and really drain your creativity. Not to mention the extra time spent iterating on a device, where each cycle requires a full build.

Our answer to this is MethodReload. We demoed it on stage at Unite Seoul and it is available now as an experimental package. In this post we’ll cover how to use MethodReload, what its limitations are, and how it compares to hot reload tools you may already have in your project.

## **Why we're stuck reloading**

A little history helps here, because the reason domain reload exists is also the reason it's hard to get rid of.

Play Mode was built on Mono's AppDomains where code changes kicked off a familiar process: tear down the domain, load the new assemblies, re-JIT, and then resume in the same process. For years that was a genuine superpower, and it's a big part of why iterating in Unity felt fast compared to building a player.

It's also a blunt instrument, meaning that during the reload everything goes away and everything comes back, whether you changed one method or one hundred. Furthermore, IL2CPP doesn’t support domain reloads at all, so every change requires rebuilding the entire player.

You might be asking yourself, “won't CoreCLR fix this?” and the answer is: Not magically. While CoreCLR does away with *domain reloads*, it still has to reload assemblies, and MethodReload can help here as well.

## **How to use MethodReload**

As mentioned above, MethodReload is available now and it ships in `com.unity.pipeline`, currently at `0.7.0-exp.1`.

The process of using MethodReload is fairly simple. Just tag one or more methods with the `[MethodReload]` attribute, start the watcher, enter Play Mode or attach a development player, and then edit the body of your methods. The running instance picks up the new body on its next call.

MethodReload doesn't replace domain reloads completely, however. Bigger changes still go through the usual compile. But for the small tweaks that make up most of an iteration loop, it turns a long wait into a matter of seconds, in the Editor and on device alike.

## **Try it out**

The fastest way to understand MethodReload is to run it, so if you’d like to test this out yourself, here are some steps to get you started. Note: since this is an experimental feature, the process may change in the future and be different from what is described here

**1. Install the package (Unity 6.0+ required).** You can either install it through the [Unity CLI](https://discussions.unity.com/t/unity-pipeline-package-0-7-0-exp-1-is-available-now/1736536) or use the Package Manager to add the Pipeline [package manually](https://docs.unity3d.com/Packages/Installation/manual/upm-ui-quick.html) using “Install package by technical name” and this string: `com.unity.pipeline@0.7.0-exp.1`.

**2. Tag the methods you iterate on.** The attribute has to be there before you enter Play Mode or build a player, because the dispatch check is woven in at compile time. Tagged methods must be `public` (instance or static) and return `void` or `IEnumerator`; anything else is skipped at build time with a warning.

```
using Unity.Pipeline.MethodReload;

using UnityEngine;

public class Spinner : MonoBehaviour

{

    public float rotationSpeed = 90f;

    [MethodReload]

    public void Update()

    {

        transform.Rotate(Vector3.up, rotationSpeed * Time.deltaTime);

    }

}
```

**3. Start the watcher.** In order for your MethodReload to see your changes live, you will need to start the MethodReload Watcher. Do this by going to Project Settings → Pipeline → Editor, then in the “Method Reload Interpreter Watch” section, click Start Watching.

While the watcher covers the whole Assets tree, a saved `.cs` only compiles if it contains a `MethodReload` attribute, so unrelated saves cost you nothing.

**4. If testing in the editor: enter Play Mode.** Once running, any tagged code change will be compiled and injected in place. Once you leave play mode, your changes will compile and go through the usual domain reload.

**5. If testing on device: plug in a device.** Build a development player with the [runtime Pipeline driver enabled](https://docs.unity3d.com/Packages/com.unity.pipeline@0.7/manual/runtime-setup.html#step-by-step-enable-in-a-dev-build). Connect the device with Autoconnect Profiler, or attach through the Profiler or Console window. From then on, every save compiles in the Editor using the *player's* preprocessor defines and pushes to every connected player. No restart is needed in either direction.

Two workflow details worth knowing up front:

- Auto-refresh is off while the watcher runs, so a save reloads instead of triggering a domain reload; other assets won't import until you hit Ctrl/Cmd+R, and Stop Watching puts your settings back.
- The watch survives domain reloads: it re-applies edits that a Play Mode reload wiped, and re-pushes to a player that reconnects, since a restarted player boots the original compiled code.

### **What about using the CLI?**

If you prefer working in a terminal, want to work through an agent, or want to push every tagged method rather than only what changed since the watch started, the same functionality is exposed as Unity CLI commands:

```
# Reload in the Editor through the interpreter

unity command reload_file_editor_interpreter "Assets/Scripts/Spinner.cs"

# Compile in the Editor, push to connected players (folders work too)

unity command reload_file_player_interpreter "Assets/Scripts" --player 2
```

## **Limitations**

There's no way around domain reload without compromises, and the limitations on MethodReload are in three places: what kinds of change it can apply, what C# it can run, and how fast it runs.

**Only tagged method bodies change.** A reload never touches call sites, fields, or type layout. No new fields, no new classes. That constraint is what makes it safe to apply to a live instance, and it's the one you plan around: decide which methods you'll be iterating on and tag them. A reload *can* declare a new method and call it from a reloaded body, but that method can't be a reload entry point, because nothing compiled knows to call it until your next real compile.

**It runs a C# subset.** The interpreter is hand-built and has to stay small enough to live inside a player, so it doesn't implement all of C#. Inside a `[MethodReload]` body you cannot use:

- `await` and `Task`, `try`/`catch`/`finally`, `lock`, LINQ query syntax, `checked`
- `decimal`, `dynamic`, reflection types, threading types
- `ref`, `out`, and `in` parameters, `ref` returns and locals, multi-dimensional arrays (jagged is fine), generic methods

What *does* work covers most gameplay code : primitives, method calls, loops, delegates, string interpolation, coroutine `yield`, collections. A Roslyn analyzer ships with the package and flags violations in your IDE, on tagged bodies only, so you find out while typing rather than after a push.

**On device, interpreted code can only call what the player exposes.** IL2CPP strips code with no references, so a reloaded body that calls a UnityEngine or BCL member your build never used has nothing to call. In the Editor, missing members bind on demand. On a device, the push checks up front and lists missing members as warnings; if the code reaches one anyway, it throws an exception. Rule of thumb: change what a method *does*, not the set of APIs it *depends on*.

**Interpreted code is slower than compiled code.** That's the nature of an interpreter, whether the comparison is IL2CPP ahead of time or Mono and CoreCLR just in time. It only affects tagged methods in development builds. In release builds there is no prologue and no interpreter; a tagged method just runs its compiled body. Ultimately, it is up to you to decide if the performance hit during iteration is worth the improved iteration speed and convenience.

**Coroutines pick up changes at creation.** A `[MethodReload] IEnumerator` method uses the new body the next time `StartCoroutine` runs. Coroutines already in flight keep the body they started with. Pair it with `[OnMethodReloaded]`, a parameterless instance method that fires on every live instance after a reload lands on its type, and you have a domain-reload-free `OnEnable` for restarting long-lived loops:

```
[OnMethodReloaded]

void OnMethodReloaded()

{

    StopAllCoroutines();

    StartCoroutine(MainLoop());

}
```

## **How it works under the hood**

It's the combination of two ideas: the first is that compiling C# produces IL bytecode, and IL that stays inside a modest subset can be executed by an interpreter instead of being compiled. That interpreter is itself ordinary C#, so IL2CPP compiles it along with the rest of your game, which is what lets it run on device.

The second idea is getting into it. Every `[MethodReload]` method has a wired path to the interpreter. Branching to the interpreter is done by weaving a prologue in the tagged methods at compile time. Decompiled, it looks like this:

```
[MethodReload]

public void TakeDamage(int amount)

{

    // weaved during compilation

    if (MethodReloadRegistry.HasOverride("Player.TakeDamage") &&

        MethodReloadRegistry.TryInvokeMethodReload(

            "Player.TakeDamage", this, amount))

    {

        return;

    }

    // initial code

    hp -= amount;

}
```

The woven check asks the registry whether an override exists for this method. The watcher and the CLI fill that registry with freshly compiled IL. If there's an entry, the interpreter runs it and the original body is skipped. Otherwise the compiled code runs as usual.

## **How this compares**

Good tools already exist for iterating on C# without a domain reload, and we'd rather be precise about where each applies than pretend they don't.

**Packages from the Asset Store** patch methods in a running Mono runtime. That gives them an excellent Editor experience, full C# in the reloaded body, no tagging step, and in Hot Reload's case an on-device mode for Mono player builds. All real advantages. It also means that they don’t work with an IL2CPP player because there's no runtime to patch.

**.NET Hot Reload**, the feature in Visual Studio and Rider for .NET applications, applies edits through the runtime's edit-and-continue path. It's built for CoreCLR and doesn't target Unity's Mono or IL2CPP runtimes.

MethodReload sits in a different spot with its interpreter backend trading language coverage for reach: a subset of C#, but running on the same IL2CPP development build you'd otherwise be redeploying to a phone or a console dev kit, over the cable you already have plugged in, with no extra server in the player and no port to open.

Honest version: if your iteration pain lives in the Editor, the existing tools are mature and you should keep using what works for you. If your iteration pain lives on a device, and especially on IL2CPP, this is the first option that goes there.

## **Final tips**

If you're setting up a workflow for a project right now:

- **Tag your hot spots.** `[MethodReload]` costs nothing in release builds, so tag the `Update`, tuning, and game-feel methods you know you'll be poking at on device.
- **Let the analyzer keep you inside the subset.** If a method needs `try`/`catch` or `await`, move that part into an untagged helper and reload the logic around it. The analyzer will let you know if you’re doing something wrong.
- **Try it in the Editor first.** The watcher, or `reload_file_editor_interpreter` from the CLI, runs your edit through the same interpreter that runs on device. If it works there, it will work on hardware, so you catch subset and missing-API problems without waiting on a build.

## **What's next**

The command reference, the runtime setup page, and the full constraint list are in the `com.unity.pipeline` [docs](https://docs.unity3d.com/Packages/com.unity.pipeline@0.7/manual/code-reload.html).

We encourage you to try this out in your projects and [let us know how it goes](https://discussions.unity.com/t/skipping-domain-reload-faster-iteration-using-the-methodreload-feature/1740090). Feedback is greatly appreciated and experimental packages improve fastest when people push on them.

Domain reload isn't going anywhere for the changes that require it. For the changes that don't, you can stop waiting.
