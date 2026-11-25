---
source: "https://code.blender.org/2026/11/layered-actions-workshop-september-2026/"
title: "Layered Actions Workshop: September 2026"
author: "dr. Sybren"
date_published: "2026-11-03"
date_clipped: "2026-11-25"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Layered Actions Workshop: September 2026

As is tradition by now, on the day before Blender Conference 2026, the Animation & Rigging module held a day-long workshop to discuss how Layered Actions should work in Blender. In this post, we’ll share the outcomes of that workshop.

For more context on this topic, visit [Animation 2025: Progress & Planning](https://code.blender.org/2024/02/animation-2025-progress-planning/). The progress of the coding work is tracked in [#154504: Layered Actions](https://projects.blender.org/blender/blender/issues/154504).

Joining in the workshop were [Beorn Leonard](https://projects.blender.org/BeornLeonard), [Brad Clark](https://projects.blender.org/BClark), [Christoph Lendenfeld](https://projects.blender.org/ChrisLend), [Falk David](https://projects.blender.org/filedescriptor), [Luciano Muñoz](https://projects.blender.org/LucianoMunoz), [Nacho de Andrés](https://projects.blender.org/nda), [Nathan Vegdahl](https://projects.blender.org/cessen), [Pierrick Picaut](https://projects.blender.org/P2design), [Rik Schutte](https://projects.blender.org/Rikstopher) and [Sybren Stüvel](https://projects.blender.org/dr.sybren).

## Recap of the 2025 Workshop

A year ago there was also a similar workshop. It never resulted in a blog post, but it was [presented at Blender Conference](https://video.blender.org/w/kCANQSR6EyzYmEiuXwPa9U). The most relevant result can be summarized in a single image:

[![](https://code.blender.org/wp-content/uploads/2026/11/animation_workshop_2025-edited-1024x633.webp?x95207)](https://code.blender.org/wp-content/uploads/2026/11/animation_workshop_2025-edited.webp?x95207)

The most important aspect for now is the side panel, which offers a **user interface to see and manage the layers in this particular Action**. This will become relevant later in this blog post.

## Animation Filtering

At the current stage of the *Layered Actions* project, the development is focused on a **replacement for the ‘animation filtering’ system** ([#163813](https://projects.blender.org/blender/blender/issues/163813)). This system determines which animation data is shown in editors, and which data is operated on by tools.

The current system was made 17 years ago, for Blender 2.50, and is showing its age. Now that a much more flexible replacement is underway, the question is: **what do we do with that flexibility?**

These topics were discussed:

- **Channel Box** in Dope Sheet, Action Editor, Graph Editor
- **Pinning** of Channels
- Action & Slot **selection & assignment**

The result of the workshop was also [presented at Blender Conference 2026](https://video.blender.org/w/p/evf2Kp5YZFvmMTaVx45HF9).

### Channels in Animation Editors

This setup was used as a simple case study.

[![Screenshot of Blender's 3D Viewport, showing three cubes and a camera.](https://code.blender.org/wp-content/uploads/2026/11/e3c9da5b-e978-424b-b6d7-7d00c349f7fc-1024x481.png?x95207)](https://code.blender.org/wp-content/uploads/2026/11/e3c9da5b-e978-424b-b6d7-7d00c349f7fc.png?x95207)

- Three objects (`Cube`, `Cube.001`, `Cube.002`) that all share the same Mesh Data (`Cube`)
  - They are animated by one Action `BigAction`.
- One shared Material
  - Has its own Action `MaterialAction`.

#### Issues with Current Blender

Blender 5.2 shows these channels in the Dope Sheet:

![Screenshot of the Blender 5.2 Dope Sheet. The channel tree on the left-hand side is quite cluttered, and repeats the same CubeMat material and Cube mesh data for every cube object. The vertical space is not enough to show everything.](https://notes.blender.org/uploads/7b18b030-5d77-4b84-8281-3bdeec2ebd21.png)

We identified the following issues (nothing shocking, but it helps to make these explicit):

- The Object Data (mesh `Cube`) is repeated under each Object that uses it. This means the same data-block is shown any number of times, and its keys are also over-represented.
- The same is true for the Material, which is repeated under each object as well.
- The name of the Action is only shown for the Object, but not for the Object Data or the Material, even when those are using different Actions.
- There are many ‘summary’ channels that may help to understand the relationships between the shown channels, but that also take up valuable vertical space and unnecessarily show the same keys multiple times.

#### The New Way

With the new system, we propose to not put Objects at the top-level, but to make the channel list more animation-focused, and begin with the Action.

Since Slotted Actions were [introduced in Blender 4.4](https://developer.blender.org/docs/release_notes/4.4/animation_rigging/#slotted-actions), multiple data-blocks can be animated by a single Action. This is typically used to group the animation of object and object data, as well as group together the animation of closely related objects (like characters and props). It thus makes sense to also **show this animation-level relationship in the animation editors**.

In short, the view was that **animation editors should not mirror the Outliner, but should provide an animation-oriented view**.

This is the proposal for the new channel list:

```
⏷ Summary
  ⏷ BigAction
    ⏷ Cube
      ⏷ Object Transforms
        - Location X
        - Location Y
        - Location Z
    ⏷ Cube.001
      ⏵ Object Transforms
    ⏵ Cube.002
    ⏵ CubeMesh
  ⏷ MaterialAction
    ⏵ CubeMat
```

This solves the issues identified above in the following ways:

- Action as the top level item. This not only groups related data together, but also solves the issue that the name of the action was not shown for anything but objects.
- Object data is no longer shown nested underneath each object, but only once, and at the same level as the objects themselves.
- The same is done for Materials and other data-blocks that use the same Action. They are just shown directly underneath the Action, and not underneath their ‘user’.
- A new option, ‘Minimal Grouping’, is introduced, as shown below.

#### Minimal Grouping

Even with the new structure laid out above, there may be too many ‘summary’ channels shown. For example, when there is only one Action in use, it is not that interesting to show its name and summarize its keys. The same goes for objects — they are interesting if there are multiple objects shown, but if you work with only one at a time, you already know which object you have selected.

The new filter option ‘**Minimal Grouping**‘ solves this by removing all summaries/groupings that only group one ‘thing’.

In the following case, there is only one Action, so its channel disappears. Similarly, each Object only shows one F-Curve Group (‘Object Transform’), so that also disappears.

| Minimal Grouping Off | Minimal Grouping On |
| --- | --- |
| `⏷ Summary ⏷ BigAction ⏷ Cube ⏷ Object Transforms - Location X - Location Y - Location Z ⏷ Cube.001 ⏷ Object Transforms - Location X - Location Y - Location Z ⏷ Cube.002 ⏷ Object Transforms - Location X - Location Y - Location Z ⏵ CubeMesh` | `⏷ Summary ⏷ Cube - Location X - Location Y - Location Z ⏷ Cube.001 - Location X - Location Y - Location Z ⏷ Cube.002 - Location X - Location Y - Location Z ⏵ CubeMesh` |

There are some ideas for Blender to provide presets that define how animation data is grouped, with the ability to set up custom groupings. No specifics have been worked out yet.

#### Only Showing Channels With Keys

The new animation filtering system works broadly in two steps:

- Gather the relevant animation data channels (like F-Curves and Grease Pencil layers). Metadata is attached to each of those channels, indicating which Action, Layer, and Group they were found in, or which Object or Bone they are animating.
- Build the channel hierarchy, based on those data channels and their metadata.

By separating those two steps, we have gained the flexibility to implement features like the ‘Minimal Grouping’ described above. However, this also has a side effect that **only things that contain actual keys are shown**.

A concrete example is Action layers. When you add a new layer to an Action (once that’s possible), it will *not* be shown in the Dope Sheet until that layer actually has keys, e.g. animates something. In a sense, this is similar to other channels, where ‘Location X’ is also not shown until it is animated. Of course, all layers are visible in the side-panel for managing those layers (see the image at the start of this blog post).

#### Graph Editor

For the Graph Editor, one of the conclusions was that it should be possible to **toggle between the Graph Editor and the Dope Sheet and that both should show the same channels**. This is currently possible with the Dope Sheet in Dope Sheet mode, but *not* when it is set to Action Editor, Grease Pencil, or any of its other modes.

To make this toggling possible, the Graph Editor should also get modes. Alternatively, but this would be a bigger change, the Dope Sheet and Graph Editor could be merged into one Animation Editor, which could then

- switch between the modes to determine *which* channels to show, and
- switch between Graph and Keys view to determine *how* those channels are shown.

For showing **layered** animation, the Graph Editor should be able to **vertically stack** graphs. Each layer can then be shown separately, as an actual layer.

Once this is possible, a next step could be to include Dope Sheet-like channels in the Graph Editor:

- **Summary keys** make selection and retiming simpler, avoiding the need to zoom out to select all keys on a frame.
- **Non-curve keys** (like Grease Pencil) can also be shown, serving as reference points or allowing retiming the entire animation from within the Graph Editor.

Finally, but this is a long-standing wish, is the ability to show ‘derived/evaluated/effective’ curves. For example, seeing the cumulative result of several additive layers, or seeing the world-space transform of bones and objects. Of course, these curves should be editable as well. It is unclear if/when it will be built, though.

### Pinning of Channels

We defined the desired behavior of pinning as **making the channel visible regardless of any filter settings**. It is meant to be **set up temporarily by the animator**, for example, when the hands of two characters are touching, their animation should always be shown (while working on those hands), regardless of selection. Another example that was brought up is that a channel may be pinned as a reference for spacing.

A channel should be pinned **to the editor**. This means that it is possible to have different Dope Sheets showing, each with their its set of pinned channels. However, toggling an editor between Dope Sheet and Graph Editor should retain the same pins.

### Custom Grouping

Another feature idea that came up in the discussion was the ability to create custom channel groups. This could be set up by the rigger to predefine a structure for a given rig. For example, all controllers for the arm could be put into that group so they show up together once the animator starts working.  
Alternatively, the animator could create such groupings on the fly based on the need of the animation.

```
⏷ Summary
  ⏷ Arm Left
    ⏷ IK Hand
      - Location X
      - Location Y
      - Location Z
    ⏵ IK Pole
```

The key lesson to take away from this is: **Animators care about the structure of the rig, not the data structure of Blender**.  
There are some details to flesh out, since this concept shares many similarities with selection sets and bone collections.

### Action/Slot Selection/Assignment

There are two major limitations with managing Actions in the current animation system:

1. **The Action Editor is the only animation editor that can handle Action assignment.** If you’re using the Dope Sheet or Graph Editor, you can’t manage your Action/Slot assignment right there in context. You have to switch to the Action Editor or go to the Properties editor.
2. **The Action Editor only shows the Action assigned to the currently active Object**. There’s no straightforward way to view the Action assigned to the Scene, the World, a Compositing Node Tree, a Material, etc. Nor is there a way to preview or work with a specific Action’s data without first temp-assigning it to an Object. The Dope Sheet already provides a way to view the animation data of all selected Objects via filtering, so the current behavior is redundant. The Action Editor should let you view and work with any Action.

> Side note: we know the Action Editor is currently the only way to filter on Object selection without also filtering on Bone selection, and that many people find this useful. Making this possible in the Dope Sheet is just a matter of adding more filter options.

#### Action/Slot Assignment in All Animation Editors

To address limitation 1, we want to move Action/Slot assignment into the N-panel of *all* the animation editors.

For example, in the Dope Sheet it might look something like this:

[![Mockup of the dopesheet with an Object channel selected. The right-hand side-panel shows the same Action and Slot selector as the properties panel already has in Blender.](https://code.blender.org/wp-content/uploads/2026/11/c852e95f-aad2-46d0-9778-f8b992ef52bd-1024x660.webp?x95207)](https://code.blender.org/wp-content/uploads/2026/11/c852e95f-aad2-46d0-9778-f8b992ef52bd.webp?x95207)

When you select a channel on the left that corresponds to a data-block (such as an object, material, scene, etc.) then the N-panel on the right displays the familiar Action/Slot dropdowns to manage its Action/Slot assignment. We can add the same thing to the graph editor as well.

This approach can also be expanded to make other aspects of action management easier. For example, if you select an Action channel Blender can provide a UI in the N-panel for managing the data-blocks animated by that Action:

[![Mockup of the dopesheet with an Action channel selected. The right-hand side-panel shows the data-blocks that are animated by this Action, and some buttons to manage those.](https://code.blender.org/wp-content/uploads/2026/11/85c82de5-5477-4360-8afb-245283a61331-1024x614.webp?x95207)](https://code.blender.org/wp-content/uploads/2026/11/85c82de5-5477-4360-8afb-245283a61331.webp?x95207)

This provides a way to assign the Action to data-blocks that aren’t yet animated, which is on its own important. But it also has some other powerful use cases.

For example, with Slotted Actions you may have many data-blocks that are using the Action, and you may want to **swap them all to another Action together**. We already have operators to do this, but they only work on the Actions of the active Object, and there’s no good place for them in the UI. Putting them in the N-panel when an Action channel is selected solves both of those issues, and lets you actually see what happens when you run them.

We also discussed other operators we can put there, such as operators for merging and splitting Actions, moving Slots between Actions (including via drag-and-drop), etc. In general, we think this is a powerful and flexible approach that opens the door for much more straightforward management of animation data across the board.

#### An Action Editor for Editing Actions

Regarding limitation 2, we discussed two possibilities.

One possibility is to simply remove the Action Editor entirely. If you can manage Action and Slot assignment in the Dope Sheet, and filter what you see there based on selection filters, that covers everything the Action Editor currently does. So the Action Editor is redundant.

But we think a better idea is to change the Action Editor to actually be about *editing Actions*. Weird, right?

The core idea is pretty simple: change the Action selector in the Action Editor’s header to be purely about what Action you’re *viewing* in the editor, and not about assigning the Action to a data-block. Then at any time you can view and work on whatever Action you like, regardless of Object selection. In the other animation editors we could even have a right-click menu option “View in Action Editor” that jumps you to the Action Editor, viewing the Action of the clicked-on animation data.

The specifics of this still need to be worked out, but we think this approach can open up the Action Editor to be much more than just a slightly different Dope Sheet, especially with animation layers.

## Conclusion

The workshop gave us quite useful designs:

- **Animation-centric channel organization:** Replaces the Outliner-mirror model with a space-efficient hierarchy that eliminates repeated data and introduces a Minimal Grouping toggle.
- **Graph Editor enhancements:** Per-layer vertical graph stacking and the ability to display non-curve keys, including summary lines.
- **Dynamic view controls:** Pinning and custom grouping let animators tailor the channel list to the current task.
- **In-context Action management:** Direct Action/Slot assignment and manipulation from the Dope Sheet and Graph Editor side panel.

These changes will be implemented incrementally. The module is currently working on [replacing the ‘animation filtering’ system](https://projects.blender.org/blender/blender/issues/163813), which will deliver the first point above and lays the foundation for all the other features. Once that lands, work on [layered Actions](https://projects.blender.org/blender/blender/issues/154504) will progress to the next milestone.

## Stay in the Loop

Keep an eye on the [Animation & Rigging module meeting notes](https://devtalk.blender.org/tag/animation-rigging/37). These are the best source of information on current development and decision-making. Or maybe even [join a meeting](https://stuvel.eu/anim-meetings/)?
