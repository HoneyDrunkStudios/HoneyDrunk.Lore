---
source: "https://dev.to/nefayran/my-godot-level-load-fell-from-345-s-to-27-s-and-the-best-fix-removed-work-nobody-needed-2e4p"
title: "My Godot level load fell from 34.5 s to 2.7 s, and the best fix removed work nobody needed"
author: "Rodion Kazennov"
date_published: "2026-11-11"
date_clipped: "2026-11-11"
category: "Game Development / Unity"
source_type: "rss"
---

# My Godot level load fell from 34.5 s to 2.7 s, and the best fix removed work nobody needed

On the morning of 2 November the landing in my Godot 4 game, Planet Wanderer, took 34.5 seconds to load. A week later it takes 2.7. The biggest single step was not threads or caching. A footprint calculation went from 8.3 s to 0.3 s because it was walking models with 50,000 to 400,000 triangles when a copy with a few hundred would do. Below are the steps in the order I took them, with the log line that justified each, and one fix that measured as nothing.

All times are from one Windows PC with 8 worker threads, read from a timing line the game prints for each part of the load. Each number comes from a separate run, so treat anything under about half a second as noise.

## What "landing" loads

When the player picks a landing spot and presses "Sit here", the game builds a camp around the rover. It lays out two small camps and a town, places a hundred or so props, places the people who live there, plants grass and flowers, and works out where each thing stands so the grass bends away from it. Props and people are 3D models made from images, so some of them carry 50,000 to 400,000 triangles.

I had been measuring the load as one number. That number only told me it was bad. Splitting it into named parts, each printed with its time, is what made everything below possible. If you do one thing from this post, do that.

## Step 1: a frame that holds for 36 seconds

After "Sit here", one function placed the camps in a single frame: 9.3 s. Then one function planted the ground around them in a single frame: 36.7 s. The loading ring on screen stood still for most of that, because nothing could draw while the frame was busy.

The fix was the boring one: make both steps advance a little each frame and let the ring move. Same total work, the screen alive. This did not make the load shorter, but it made it measurable, because the next steps could now be timed one at a time while the game kept rendering.

## Step 2: plants as one buffer (36.7 s in the part, 92 ms for the plants)

Most of that 36.7 s was the ground plants. I moved them into a single `MultiMesh` buffer and wrote the transforms into it directly. On the Windows PC the plants alone then measured 92 ms. After this and the next step, the whole landing load went from 34.5 s to 21.6 s.

## Step 3: the footprint walk, moved to workers (13.1 s + 4.0 s to 8.3 s)

To make the grass lie flat around a tent, the game needs the tent's footprint: which ground cells its triangles cover. The code walked every triangle in GDScript, twice, once for the footprint and once for the feet of the people. The cost was not reading the mesh surfaces (that took 0.3 s in total). It was the walking: 13.1 s and 4.0 s.

I changed it to one walk that fills both masks, and ran it on `WorkerThreadPool`, one task per ground cell:

```
var gid: int = WorkerThreadPool.add_group_task(func(i: int):
    var jb: Dictionary = jobs[i]
    var wk: Dictionary = _walk(jb["surfs"], jb["pm"] != null)
    jb["mask"] = wk["mask"]
    jb["feet"] = wk["feet"], jobs.size(), -1, true, "camp footprints")
while not WorkerThreadPool.is_group_task_completed(gid):
    await planet.get_tree().process_frame
WorkerThreadPool.wait_for_group_task_completion(gid)
```

Reading scene nodes and meshes must stay on the main thread, so a first pass on the main thread collects each model's vertices and indices into plain arrays, and the workers only do arithmetic on those. The `await` on the frame loop keeps the ring moving while they run. Result: 8.3 s on 8 threads, and the frames kept coming.

## Step 4: the fix that measured as nothing

The camp build was almost entirely props: the "heart" of the camp took 4.2 s of 4.4. A hundred things were each being repainted (materials adjusted, one by one). My idea: paint the first thing of each model path, and let the rest be copies of it.

I added `first_of(path)`, kept the first painted node, and duplicated it for the rest. The heart went from 4.2 s to 4.6 s. Slower, within noise.

The reason was in the data, not the code. At the first camp every prop is the first of its path, so there were no copies to share. I only saw that because I added a per-model timing line next time instead of re-running the stopwatch around the whole function.

## Step 5: it was the disk read, 180 to 300 ms per model

The per-model line said the time was almost all the first read of each model from disk: 180 to 300 ms for each of about 30 models. Painting was 0 ms. Copies and far copies cost 2 to 35 ms.

So the fix was to start reading them earlier. The screen where you choose a landing spot comes before the build, and `ResourceLoader` can load in the background while it is open:

```
static func warm(paths: Array) -> void:
    for p in paths:
        if _warm.has(p) or not ResourceLoader.exists(p):
            continue
        _warm[p] = true
        ResourceLoader.load_threaded_request(p, "", true)
```

The place-selection screen requests all 59 files (the models and their far copies, and the people). When the camps are built the requests are already finished and the "read" is a lookup. Measured: camp near the landing 6,957 ms to 479, town 3,378 to 617, heart props 4,924 to 29. Whole landing load 22.8 s to 13.6 s.

One trap here: `warm()` keeps the requests, and something has to collect them afterwards or they pile up in memory. A `forget_firsts()` call frees them once the camps are up.

## Step 6: stop walking the big model (8.3 s to 0.3 s)

The footprint walk was still the largest part, 8.3 s on 8 workers. I looked at which triangles it walked and found it went through every mesh under every prop, including the full 50,000 to 400,000 triangle model, and also the model's far copy: the low-triangle stand-in the game shows at a distance.

For a footprint on the ground, the far copy is enough. Now when a thing has a node called `far`, the walk takes that and stops:

```
var fc: Node = nd.get_node_or_null("far")
if fc != null:
    todo.append(fc)
    continue
```

The footprint walk went from 8.3 s to 0.3 s. I checked that the result stayed the same: plants removed 6,026 against 6,041 before, plants trampled 850 against 836. The footprints are nearly the same, because a few hundred triangles at the right silhouette give the same ground cells as 300,000 at the same silhouette. Whole load: 13.6 s to 5.7 s.

This is the step I would have missed if I had stopped at "use more threads". Eight threads took 17 s of work down to 8.3 s. Doing less work took it to 0.3.

## Step 7: a release that came too early (1.7 s to 0.3 s)

The locals' camps took 1.7 s in one frame, and the per-model line showed they were reading their people's models from disk again. The cause: `forget_firsts()` freed the pre-read models right after the camps were built, before the locals, which use the same files. I moved the call to after both locals' camps. Locals' camps 1,762 ms to 321. Whole load 6.3 s to 4.7 s (a different run from the 5.7 above, so the baselines differ).

## Step 8: the town's free-ground calculation, and the last models

Two smaller things took the load from 4.7 s to 2.7 s:

- The town's locals spent 816 ms in a free-ground calculation per cell, almost all of it on the main thread. I collected the data on the main thread and ran the triangle walk on workers, one cell per worker. 816 to 329 ms, camps 321 to 209. I compared the logged places of the locals before and after: identical to the hundredth of a metre.
- The camp and town cell models and the wounded person with the blanket were still read at the moment of use. Reading them early too: camp 617 to 244 ms, town 736 to 97, the wounded figure 348 to 28. Whole load 4.2 s to 2.7 s.

## The table

| Step | What changed | Whole landing load |
| --- | --- | --- |
| start (2 Nov) | one 36.7 s frame | 34.5 s |
| 1 to 3 | frames split, plants in one buffer, footprint walk on workers | 21.6 s |
| 5 | models read ahead during place selection | 13.6 s |
| 6 | walk only the far copy | 5.7 s |
| 7 | locals' models kept until used | 4.7 s |
| 8 | town on workers, last models read ahead | 2.7 s |

## What I would do again, and the part I still do not understand

Three habits made this go quickly. Print a named time for every part and keep the line in the log permanently. When a fix does not help (step 4), go to a finer-grained measurement before inventing the next fix. And check that a speed-up did not change the result: I compared plants removed and the locals' positions each time.

What I cannot explain yet is the other machine. In the game's log from my Linux PC, slicing the ground after the load costs 39 s of CPU, against 5.8 s on the Windows PC. The numbers above are all from the Windows PC. Is that gap fewer fast cores free at that moment, a different Godot build, or something in how the workers are scheduled there? I have not measured it, and I would like to know where else a seven-fold difference like that could come from.
