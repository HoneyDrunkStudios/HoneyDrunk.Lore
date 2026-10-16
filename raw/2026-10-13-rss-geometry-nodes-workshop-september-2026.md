---
source: "https://code.blender.org/2026/10/geometry-nodes-workshop-september-2026"
title: "Geometry Nodes Workshop: September 2026"
author: "Jacques Lucke"
date_published: "2026-10-05"
date_clipped: "2026-10-13"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Geometry Nodes Workshop: September 2026

As in previous years, we had a Geometry Nodes workshop during the week after the Blender Conference. This post gives a general overview of the topics we discussed. You can also read [all the notes](https://devtalk.blender.org/t/2026-09-28-geometry-nodes-workshop-notes/45889) we took during the meetings.

Also check out the blog posts about previous workshops: [September 2025](https://code.blender.org/2025/10/geometry-nodes-workshop-september-2025/), [July 2025](https://code.blender.org/2025/07/geometry-nodes-workshop-july-2025/), [October 2024](https://code.blender.org/2024/11/geometry-nodes-workshop-october-2024/), [May 2024](https://code.blender.org/2024/05/geometry-nodes-workshop-may-2024/), [November 2023](https://code.blender.org/2023/11/geometry-nodes-workshop-november-2023/), and [November 2022](https://code.blender.org/2022/11/geometry-nodes-workshop-2022/).

We invited two guests from the community: Brady Johnston, developer of the Molecular Nodes add-on, and Cartesian Caramel.


## Previously in Geometry Nodes

Since the last workshop, a lot of development happened for Blender [5.1](https://developer.blender.org/docs/release_notes/5.1/), [5.2 LTS](https://developer.blender.org/docs/release_notes/5.2/), and [5.3](https://developer.blender.org/docs/release_notes/5.3/).

**Volume Grids**: Many utility nodes have been added, including Cube Grid Topology, Grid to Points, a Poisson Solver, and Rasterize Points.**String to Curves**: The String to Curves node became much more configurable using its input sockets, opening up many possibilities for motion graphics templates.**Bundles**: There are new Get/Store Bundle Item nodes and the concept of a “bundle path” has been introduced.**Bone Info**: A new Bone Info node provides access to various information about armature bones.**Copy & Paste**: Nodes can now be copied between different Blender instances.**Physics**: New experimental Cloth and Hair Dynamics have been added, powered by a new built-in XPBD solver. See the[blog post](https://code.blender.org/2026/07/geometry-nodes-physics/)for more details.**Geometry Bundles**: Any data can be attached to a geometry now, allowing for more decentralized workflows where inputs are configured on multiple objects.**Lists**: Initial support for working with list data has been added.**Collections**: A new Collection Children node gives access to all nested objects and collections.**Sound**: The new Sample Sound Frequencies node allows controlling animations and simulations with sound.**Empties**: Geometry Nodes can be used on Empty objects now.**Merging Points**: More atomic building blocks for clustering and merging points have been added.**Bevel**: A new Mesh Bevel node has been added.**Attributes**: It’s possible to get all attribute names and transfer many at once now.**Curves**: New nodes to set the NURBS order and weight have been added.**Strings**: Various utility nodes have been added and improved. Additionally, string fields are supported now.**Shader Nodes**: Many common utility nodes have been ported from Geometry Nodes to shader nodes, including all the Switch nodes.**Comments**: The new Comment node simplifies documenting a node tree. It also supports basic Markdown syntax.


## Modal Node Tools

[Node tools](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/tools.html) were originally introduced in Blender 4.0 as a way to build custom operators for Blender using Geometry Nodes without requiring Python. Now we are in the process of extending that to support so-called “modal” operators. These can be used to build interactive tools that need continuous user input, like brushes.

The design has already gone through some iteration, but now there is a work-in-progress [PR](https://projects.blender.org/blender/blender/pulls/162819) implementing it. People have already used it to build interactive cloth sculpting and even small games.

In this workshop, we clarified a few details of the design regarding event inputs and how a timer for continuous evaluation should be set up. More specifically, instead of just exposing discrete events like key-down/up, we also want to expose the current state of buttons and other inputs such as pen pressure. Previously, the node tool would have to keep track of all that state manually.


## Exposing Bakes

We and others are starting to build more high-level simulation assets like the new Cloth and Hair Dynamics node groups. A significant usability issue is that the bake button and related settings are buried deep inside nodes that most people should not have to look at.

We want to solve that by allowing node groups to expose the bake functionality so that the bake button appears directly in group nodes and the modifier UI. This will be integrated with the node group interface tree-view so that one or more bake buttons can be inserted in the appropriate place. For example, there could be separate buttons for baking preprocessing, a simulation, and postprocessing. Another common use case might become baking bind information, like for surface deformation.


## Export Nodes

Currently, it is not easily possible to export intermediate geometries to common interchange formats. The compositor supports this using the File Output node. In Geometry Nodes, we’d like to add various export nodes like Export OBJ. Those nodes mainly take a file path, data like geometry or text, and other settings as inputs, and write that data to the file.

Importantly, we do not want the file-write to happen automatically on every re-evaluation, which would have significant performance and security implications. Instead, it can be triggered explicitly with the press of a button, just like baking. Optionally, it might be useful to explicitly turn on automatically writing files at runtime, but that should always be disabled when a new Blender session starts.

Path templates should also be evaluated as part of the node evaluation.

Just like the bake button, it should be possible to expose an export button to a group node or modifier. Therefore, we can probably generalize this a bit and call it “exposing operators”. In the future it could also become possible to expose custom operators. Those could be used to, for example, trigger interactive tools to edit input data in the 3D view.


## Node Group Compatibility

Nowadays, many built-in nodes are shared across Geometry, Shader, and Compositor nodes. Therefore, it becomes ever more important that node groups built out of these common nodes can also be shared. This would avoid the issue we have now that some groups have to be built for each node system separately even though they are practically identical.

Besides sharing node definitions, some [design work](https://devtalk.blender.org/t/2025-09-05-design-session-node-groups-different-editors/42244) has already happened and node menus have become more unified. Also see [#149118](https://projects.blender.org/blender/blender/issues/149118).

The general idea is that by default node groups derive their compatibility automatically based on the nodes they use. The add menu still shows all nodes based on the currently active context, e.g. all geometry or shader nodes.

The user can also choose to explicitly check which contexts the node group should work in. In this case, the node editor can give warnings earlier when incompatible nodes are used. Generally, a node group containing incompatible nodes should still attempt to evaluate because the incompatible node might be disabled by switch nodes, for example.

If an incompatible node is used, a warning should be produced. We might even draw the node and its parent group nodes in red, similar to how unknown built-in nodes are drawn, to clearly indicate that something is wrong.

The Usage panel still only shows the possible usages relevant for the current context.


## Curves Rendering

One significant difference between the legacy Curve and new Curves data-block types is how they are shown in the viewport and in renders. The main ways curves are drawn currently are:

- just as wire in the viewport,
- as strand where the radius is ignored (does not work in Cycles),
- as “hair” in the viewport and in renders, taking the radius into account, or
- as an explicitly tessellated mesh.

The goal is to support all modes for the newer Curves data-block, getting us one step closer to fully replacing legacy curves with it.

A related issue is that the curve drawing type is currently global in the scene instead of per Curves geometry. This might need some reshuffling to achieve the required flexibility. The global setting should be seen more as a Simplify setting.


## Dynamic Socket Types

Currently, many nodes have explicit socket-type menus. This leads to two problems that dynamic socket types can elegantly solve:

- It’s cumbersome to select the right type so often when Blender should be able to choose the type automatically based on what is connected. Link-drag search solves this to some degree, but this is still a common annoyance.
- Since the socket type is hard-coded in the built-in nodes, it’s not possible to build node groups which work on dynamic socket types. This becomes especially apparent when trying to build generic sampling or list processing groups because currently one needs to handle each socket type explicitly.

The first step to solving this is adding a new socket type called “Dynamic”. This will be the default in many built-in nodes. The first connection to the socket changes it to the connected type. Note that this type is then implicitly “pinned”, i.e. removing the link or adding a new link does not automatically change the type anymore. The socket only stays dynamic when the newly linked socket is also dynamic.

It is not entirely obvious why this behavior works best, but it seemed most predictable, especially when multiple sockets on the node need the same type. It also directly solves problem (1). While it works well in the example we played through, it still needs some user testing. It also overrides an older proposal with more [explicit type pinning](https://projects.blender.org/blender/blender/pulls/138701).

There is one important and also somewhat annoying exception to this rule, which is the Math node. Most commonly, when performing primitive math operations, float math is expected, even if the first input is an integer. This was already a problem when the Integer Math node was originally introduced. From what we can tell, this specific problem only affects basic math operations and none of the other nodes, so some special case handling seems fine.

After a socket type is set, it can be changed from the context menu or the sidebar. The type can be set for individual sockets or multiple selected nodes. The type menu should not be shown in the node itself anymore, since it’s mostly redundant now.

Sometimes the socket type also needs a corresponding “dimensions” parameter to differentiate between e.g. 2D, 3D, and 4D vectors. Similarly, two dimension parameters may become necessary for matrices. The dimensions can have similar behavior; they can stay dynamic until explicitly set.

Building a group that works on any type becomes rather simple. One can now just create new dynamic input and output sockets. Blender has to infer how their types are internally connected. To the end user, a group should then feel exactly like a built-in node with dynamic types.

Dynamic sockets could look the same or similar to the existing extend sockets used on e.g. group nodes.


## Graph Processing

It’s common to have to deal with some sort of graph data structure in Geometry Nodes. For example, mesh edge networks, parent-child relationships, or paths along edges.

There are two distinct core problems that we discussed in this regard: ID lookup and graph traversal.

Ideally, the graphs are encoded simply using indices as identifiers. However, often custom IDs are used such as stable integers or bone names. Even the combination of multiple attributes can serve as an ID (for particles, e.g. the combination of emitter index and particle index).

While such IDs can be stored already, there is currently no efficient way to find the element that has a specific ID. This can be solved using new Sample by ID and Index of ID nodes as [proposed previously](https://projects.blender.org/blender/blender/pulls/118092). However, this needs to be generalized a bit to support more types of IDs and potentially list outputs to handle duplicate IDs.

For graph traversal, we ended up with a design for a new Find Graph Neighbors node which can recursively find connected nodes of directed and undirected graphs. Some additional iteration on the design may be necessary to make it use either only IDs or only indices.


## Lists

Lists are still in their infancy in Geometry Nodes. We discussed two important missing features: list fields and reductions.

Currently, lists can only be standalone pure data, while fields can only ever compute single values. The concept of a list field is that we want to support fields that compute a list per element.

This significantly simplifies the design of various nodes. For example, most mesh topology nodes could just output lists. Additionally, the Index of Nearest node could be extended to support outputting the closest n points.

It seems likely that list fields will be supported before list attributes are. That also means that any list has to be reduced to a single value per element before it can be stored as an attribute. The newly proposed Reduce List node is designed so that it can support standalone lists as well as list fields. It can take an arbitrary number of list inputs and compute an arbitrary number of reductions.

Evaluating closures potentially millions of times is not super optimized yet. However, it should be fairly straightforward to detect common cases such as computing the sum and optimize for them explicitly.


## Attached Comments

Recently, a new [Comment](https://projects.blender.org/blender/blender/pulls/163168) node was added. It allows documenting node trees using multi-line comments with basic Markdown support.

One missing feature is the ability to parent a comment to a node or frame such that it stays attached when the node moves. This avoids the problem that free-floating comments can drift away from the nodes they correspond to.

We chose to draw the parented comment node like a speech bubble on top of the node for now, although moving it to other sides could be supported too. The main alternative we had in mind was drawing a relationship line like those used for parenting in the 3D view, but that just doesn’t look as good.

Options for hiding or collapsing the comment when the node is selected were discussed as well, but that can be done separately later if it still seems necessary. Collapsing comments can be useful for both free-floating and attached comments.

Lastly, it seems like using the C shortcut to add a new comment would be perfect. However, currently the key is used for circle select. It’s not clear yet whether we can justify changing the C shortcut or whether some other key should be used. Either way, the shortcut should add a new free-floating or attached comment depending on whether there is an active node.


## Views

Often it is useful for a node group to show additional visualizations to the user, whether for debugging or just to find good parameters. Currently, there are two ways this can be achieved: either the user has to enter the node group to activate a viewer, or the node group has to output additional geometry to be viewed. Neither is ideal: the user should generally not have to enter the group for normal operation, and adding debug data to the output can accidentally affect later nodes and modifiers.

The solution is for groups to explicitly expose prepared views that the user can then optionally disable. These views are built on top of the Viewer node, which bypasses the need to output them as part of the normal output geometry. Note that we previously called this “Debug Views” but the name is still a bit in flux. It might also become something like “Inspection Views”.

Viewer nodes should get a new type menu to choose whether they are temporary (same as existing viewers) or exposed. In the latter case, a Viewer node also gets a new Show boolean input to allow enabling and disabling it dynamically.

The most tricky aspect of the design is deciding where and how the end user configures which of the views should be visible. Related to that is the challenge of how to avoid unused views triggering expensive evaluation accidentally. Generally, we want detailed control as part of the group node and modifier interface using boolean inputs and high-level control per viewport.

A [work-in-progress PR](https://projects.blender.org/blender/blender/pulls/161481) is available already.


## Viewer Overlays

Currently, geometry passed to an active viewer node is just drawn as-is in the viewport, replacing the fully evaluated geometry. We want to have more flexibility for how data can be visualized with the viewer.

The idea is to build on top of typed bundles which can be passed into the viewer. For example, there can be a new `Blender.MeshOverlay`

typed bundle with a geometry and various draw settings like color and screen-space edge width. When that is passed into the viewer instead of a raw geometry, it is drawn as an overlay.

This concept nicely generalizes to other kinds of visualizations that need to be explored further. Some ideas:

- Output text that is drawn next to other stats in the 3D view.
- Configure vector field and grid overlays for the 3D view.
- Pass a closure to the viewer which gets the projection matrix as input, allowing Geometry Nodes to generate screen-space geometry on the fly. Only this closure would need to be re-evaluated when the viewport changes, not the entire Geometry Nodes tree.
- Visualize data in other editor types, and specifically in the node editor right next to the viewer node.

All these different visualization bundles can be combined arbitrarily.

An initial [tech demo](https://projects.blender.org/blender/blender/pulls/164615) is available already.


## Complex Inspection Contexts

In most scenarios, the viewer node and socket inspection can accurately detect the current context and display the correct data. However, with more complex data-flow through closures this is not always possible. This is especially the case when a closure is defined on one object but evaluated on others. Often there are also multiple evaluation contexts that a closure is evaluated in, making inspection features ambiguous.

In these cases, the user needs to be able to explicitly specify which evaluation context the inspection features should work in. In programming terms, that evaluation context would be the stack trace.

We want to support that by allowing the user to explicitly run an operator to find all the possible evaluation contexts for the currently selected node. These then need to be shown in some sort of list and the user needs to choose one.

This functionality can be accessed from the sidebar or directly in the viewer node if the context can’t be detected.


## Asset Workflow

The current workflow for built-in assets is very cumbersome. When one person starts editing an asset, all assets in that .blend file are essentially locked. On top of that, it’s very hard to review changes.

Reviewing arbitrary .blend file changes can be done to some degree with the [standalone blend differ](https://projects.blender.org/blender/blender/pulls/151266). However, this still leaves a lot to be desired when reviewing node group changes.

Multiple alternatives for better reviews have been proposed, such as showing a diff in the Blender node editor as well as converting node groups to a textual format with cleaner diffs.


### Nodes as Code

For textual conversion, the most advanced and promising approach is [ nodebpy](https://github.com/BradyAJohnston/nodebpy), also see the related

[BCON26 talk](https://www.youtube.com/watch?v=EFGEIItdVVY). It supports authoring node trees with a human readable syntax, and importing it can convert from nodes to Python code and back, while the code version is highly readable and editable.

Projects like [Molecular Nodes](https://github.com/BradyAJohnston/MolecularNodes/) now store their node groups as Python code as the ground truth instead of as `.blend`

files and works well for accepting edits and contributions to node groups via PR as Python code. This is proving to be a good workflow for external asset libraries which target specific Blender releases, but it is currently harder to use for Blender’s built-in assets directly as this would require a deeper integration into the build pipeline. While probably possible, it is too early to bet that this is the right solution yet. Additionally, some problems like versioning of the scripts and of assets that depend on the node groups would still need to be solved.

A more promising alternative approach is to wrap nodebpy in git drivers for diffing and merging. This would allow keeping the ground truth as .blend files while still benefiting from better collaboration and review features for node groups. Integration into Gitea might still be a bottleneck, but at least this could be used locally already to merge and rebase changes.

A downside of using nodebpy compared to the generic .blend differ is security. Opening an untrusted .blend in Blender is not safe, but is required with nodebpy. So this functionality needs to be sandboxed well.


### Asset Splitting

Currently, all built-in assets are grouped into a handful of .blend files. This simplifies editing in the current state but otherwise has many downsides when it comes to version tracking and reviews. The plan is to move all assets that are shipped with Blender (excluding online assets) directly into the Blender repository.

On top of that, each asset will be split into a separate .blend file. Each asset .blend file contains its non-asset dependency data-blocks. However, in some cases non-assets are still shared between assets, in which case they can also be in separate files.

Splitting assets into many files has the downside that it requires more space because every .blend file has some overhead. Ongoing work to [reduce the size of simple .blend files](https://projects.blender.org/blender/blender/pulls/164109) will probably solve that in practice though.

The split asset files will not be edited manually. Instead, they are linked into test-files which contain a more complex setup using the assets. There is ongoing work on an add-on to [edit linked data-blocks](https://projects.blender.org/SimonThommes/ID-Dispatch) from these test-files. Some of that functionality may be moved to Blender itself.


## Node Layout

One significant source of wasted time comes from arguing over node group layouts or spending time manually arranging nodes to ‘look nice’. Ideally we can fully automate this process like we alread do with code using [clang-format](https://developer.blender.org/docs/handbook/tooling/clangformat/), and could help enforce standards for the node tree assets that Blender ships.

The community already has a favorite solution for this with the [Node Arrange](https://extensions.blender.org/add-ons/node-arrange/) add-on which has ~250k downloads. It appears to work great, especially when properly using frames and auto-layout from the start.

Everyone agreed that it would be good to port the add-on to C++ and have the functionality built into Blender. This way we can also use it more easily for built-in assets. This is especially important if we want to use the nodebpy tooling.


## Node Filtering

People new to Blender or nodes often find them very overwhelming, understandably. Our main approach to simplifying this is to provide more high-level node groups that people can easily use. However, just adding more to the add menu can never make it less overwhelming initially.

It seems like the only way to simplify the initial experience of using nodes is to present the user with a smaller set of easy-to-understand nodes. So we were thinking of different ways to hide nodes.

The initial idea was to group nodes into high-, mid-, and low-level nodes. However, that does not work well and is very subjective and workflow dependent.

A more promising approach can be found by looking at other visual programming languages like Scratch, designed by teachers for children. They group all blocks (aka nodes) into categories and only the most common ones are visible by default. At the end of the “add menu” there is a button where one can enable more categories of nodes.

The same approach could work for our node editor too. The exact types of categories we’d have need some more design work though. Importantly, node search can always find all nodes, even those in disabled categories. They may be drawn differently though. The search popup could also show the list of filters, including a button to show all nodes all the time in the add menu.

If we manage to come up with good categories, this could also make Blender’s node editors much more teachable, since tutorials can more easily focus on specific categories of nodes and what can be done with them, without overloading the user too much at once.

External asset libraries can also have their own tags of course.

For experienced users, the only downside is that they need to press the button to show all nodes once, which seems like a worthwhile trade-off.


## Physics

We released initial [experimental physics in Blender 5.2](https://code.blender.org/2026/07/geometry-nodes-physics/). Since then, work is going in a few directions.


### Fluids

There have been in-depth experiments with getting fluid simulation to work using volume grids, which led to the new Rasterize Points and Poisson Solver nodes. The main missing feature here is better support for staggered grids in a few built-in nodes, i.e. grids where the values are semantically stored on the faces between voxels. Additionally, for performance it would be good to add a node to spatially order points and other geometry elements.


### Rigid Bodies

There has also been work to get the Jolt library available in Blender. This will be used mainly for rigid body simulations, but maybe more in the future. There have been experiments with a Jolt solve node already, but this likely needs to be redone now.

We also discussed how to set up collision groups for rigid body simulations, i.e. how to determine what can collide with what. If the simulation is layered, e.g. first large rocks are simulated and then debris, it’s best to use two separate simulations. However, often it is necessary to have more fine-grained control within a single simulation. We decided that it would be best if by default no rigid bodies would collide with each other, but only with external colliders. Then one can add collisions between rigid bodies by using e.g. group IDs. Lastly, collisions between individual pairs of objects can be disabled if they have a separate constraint between them that would interfere with collisions.


### Cloth

We still have the same major limitations: no self-collision and a weak bending constraint. Both of these will need to be prioritized soon to get cloth physics out of experimental.


### Hair

The hair solver works reasonably well. While internal collisions would help, they are not absolutely required for many use cases. Better support for guide hair simulation would be great, but there are still some technical hurdles if we don’t want to rely too much on workarounds. Maybe list fields will be able to help.

We do want to improve the Animation mode of the Hair Dynamics node group though. Based on feedback, basic features like noise with a wind direction applied progressively along the curve would already go a long way. On top of that, a normal-based factor to fake wind shadow would help.


### Particles

It would be nice to get some good point-point collision handling working in the XPBD solver for particle simulations. However, it mainly comes down to someone putting in the work of building an initial nice particle system asset that can be iterated upon.


### Physics Framework

As we get more solvers and experiment with combining them, it gets more important to specify precisely how geometries, solvers, and effectors relate. We already do that to some degree by storing a list of tags on geometries and then having a filter on solvers and effectors to choose which geometries they affect. What’s missing so far is a system to determine which effectors should be used by which solvers. We decided that the best approach is to also have tags on the solvers and a second tag filter on each effector.

It was cool to see that our XPBD Simulation node group and related assets were already very usable for building more custom XPBD-based simulations, like this example simulating an unwinding DNA strand. It’s a good indicator that these node groups can become assets after a quick cleanup pass on their interfaces. Those are the same node groups that are already used internally by the hair and cloth solvers.

We found that instead of over-generalizing the XPBD Simulation group to support arbitrary solvers just yet, it is better to have similar groups for the different kinds of solvers (mostly fluids and rigid bodies). A more integrated multi-physics simulation asset can still be built separately. We should just make sure that all built-in solvers use the same or similar effector bundles where possible, and that they support substepping with a repeat zone while interpolating external effectors properly. This is required to be able to substep them interleaved later on.


## GPU Evaluation

Evaluating parts of Geometry Nodes on the GPU is a long-standing goal. It was not prioritized much in the past, but recent advancements in attribute storage, Vulkan support, and the compositor showing what is possible make it more feasible than ever. Significant previous bottlenecks have also been reduced, making it more worthwhile to speed up basic operations.

Bringing Geometry Nodes to the GPU comes with two major challenges: internal support for GPU evaluation and how to present that in the UI.


### GPU Evaluation Internals

Various internal evaluation systems need to be refactored to support GPU evaluation, like field evaluation. Support for storing attributes on the GPU needs to be added. Generally, this seems fairly doable given what we know so far.

One previously unclear topic was how individual threads should communicate with the GPU during depsgraph evaluation, since there is not a good precedent yet. Luckily, if we focus our efforts on Vulkan and Metal, this seems to be much more straightforward compared to supporting it efficiently on OpenGL due to the cost of `GPUContext`

with OpenGL.

If we also focus our efforts on the case where data does not have to be loaded back from the GPU to the CPU, the problem becomes simpler too. This is the case where we benefit most from the GPU anyway. Downloading from the GPU should work of course, but then the overhead of transferring data may make it better to just leave the data on the CPU in the first place.

For a less confusing API for building the compute shader, we may also look into refactoring `GPUMaterial`

into something like `GPUShaderBuilder`

or just add a new abstraction which also works well for the compositor.


### User Interface for Controlling GPU Usage

Ideally, adding support for GPU evaluation “just” makes things faster. However, in practice the situation is more complicated. It’s impossible to support all of Geometry Nodes on the GPU, so typically only some attributes, lists, and grids will be stored and processed on the GPU while other operations stay on the CPU.

This makes it necessary for the user to know when something can run on the GPU. Otherwise users have to guess all the time when building a node group that is supposed to work on the GPU.

Furthermore, even if something can run on the GPU, performance can also become worse if the node tree is built such that data has to be moved back and forth between the CPU and GPU. Fully detecting such cases in advance in production node trees is basically impossible. While Blender could detect some cases, it’s likely that extra user control will be necessary.

This will probably be in the form of menus on various nodes to choose between an Auto and Custom mode, where either Blender decides whether it should run on the GPU or not, or the user attempts to override the behavior. A node to explicitly upload data to the GPU may be necessary, but that remains to be seen.


## Geometry Construction

Constructing arbitrary new geometries like meshes and curves is difficult, especially when the topology of the desired geometry differs significantly from that of the primitives like grid and cube.

There is ongoing work to add new lower-level [Construct Curves](https://projects.blender.org/blender/blender/pulls/161402) and [Construct Mesh](https://projects.blender.org/blender/blender/pulls/160014) nodes which allow directly building geometry with a given topology.

We mainly discussed what inputs these nodes should have. In the end, we agreed that they should just have various list inputs instead of relying on fields here, which cause unnecessary indirection and are generally harder to work with and to inspect when constructing custom topology.

In theory, it should be possible to build all other mesh and curve primitive nodes with these. We are still missing some utility nodes to operate on lists though.


## Image Node

There is a lot of interest in unifying image sampling across node editors. Currently, each node editor has a custom node for that purpose. This topic is tricky to discuss since it affects many other modules.

Overall, the goal is to have a single node to sample images in geometry, shader, and compositor nodes. It should support UDIMs, sampling EXR layers, and a frame input. A higher-level node group could be built which supports features like automatic playback with frame offset, etc.

It’s not clear yet whether any of the existing nodes can be improved into the ideal version or whether it is better to add a new node with a new name that is shared from the beginning. The “Image Texture” name appears to be confusing too. For the compositor, the term “image” is also somewhat ambiguous since there are image data-blocks and a color socket can also contain an image. The best way forward is not clear yet.
