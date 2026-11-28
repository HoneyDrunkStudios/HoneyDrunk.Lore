---
source: "https://80.lv/articles/faking-a-spherical-planet-with-a-tileable-texture-in-ue5"
title: "Faking a Spherical Planet with a Tileable Texture in UE5"
author: "Alina Ledeneva"
date_published: "2026-11-04"
date_clipped: "2026-11-28"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Faking a Spherical Planet with a Tileable Texture in UE5

Alina Ledeneva explored a material-based pseudo-sphere technique that makes it possible to use regular tileable textures without custom spherical UV mapping.

### Introduction

What if I told you this planet is actually just a flat card with a regular tileable texture? There is no spherical mesh in the scene and no texture prepared in advance as a spherical map. The geometry never bends or turns into a hemisphere. The entire illusion of volume is created in the material: World Position Offset keeps the flat card facing the camera, while transformed UVs make the image look as if it were mapped onto a curved surface. This effect came out of R&D for [TYBALT](https://store.steampowered.com/app/4916030/TYBALT/), an upcoming single-player narrative-driven shooter by Kamishibai Interactive inspired by Destiny, Marathon, Witchfire, SOMA, and System Shock.

One of the goals for the planet visuals was to let artists work with procedural and tileable textures without having to convert them into spherical maps or prepare each variation specifically for a spherical UV layout. While exploring ways to make that workflow more flexible, I developed this material-based technique. In this article, I'll break down the material and Blueprint logic behind the experiment.

### Creating the Pseudo-Sphere in the Material

To distort the texture, I use a stereographic projection of a hemisphere. First, the card UVs are remapped around the center of the card and treated as the X and Y coordinates of a hemisphere facing the camera. From those two coordinates, the material reconstructs the third coordinate: the depth that point would have on a hemisphere.

That 3D hemisphere position is then stereographically projected into the 2D coordinates used to sample the texture. The coordinates change only slightly near the center, but the distortion becomes stronger toward the edges. Near the edges, this compresses the image and makes it look as if it is wrapped around a convex surface curving away from the viewer. The mesh itself is not deformed. The material only changes the coordinates used to sample a regular tileable 2D texture. That alone is enough to create the basic illusion of volume.

### What World Position Offset Does

World Position Offset has only one job: keeping the flat card facing the camera. The material uses the camera orientation to rebuild the vertex positions in the corresponding camera basis. The card stays flat and parallel to the screen even when the planet is off-center in the frame. I described this technique in more detail in my article, [Material-Based Mesh Rotation in UE5: Math and Logic](https://80.lv/articles/understanding-material-based-mesh-reorientation-in-unreal-engine-5).

### Handling Texture Movement

The camera needs to orbit freely around the planet while the texture behaves as if it were actually attached to a 3D surface. The planet itself can also rotate, so the system has to respond consistently to both camera movement and changes in the planet's orientation.

Away from the poles, this movement is fairly easy to break down into two UV offsets. Movement along the equator can be represented by a horizontal offset, while movement along a meridian becomes a vertical offset. Near the poles, however, offsets alone are no longer enough. The image also has to rotate on the card.

Texture movement uses a combination of offset and rotation. The vertical offset handles movement along the meridian. Near the equator, horizontal movement is also handled mostly by an offset, but as the camera approaches a pole, that offset gradually loses influence while rotation around a calculated pivot takes over.

### Why the Transform Has to Accumulate

The camera can travel from point A to point D along two different paths.

In the first case, it moves directly along the equator. Horizontal offset does most of the work along the entire path, and at point D we see a particular area of the texture.

In the second case, the camera first moves from A to B along a meridian. This part is represented mostly by vertical offset, so the texture gradually shifts. It then moves from B to C along an upper parallel, close to the pole. Here, rotation around the visible pole position starts to dominate. Finally, the camera moves down another meridian from C to D.

Although this last section again corresponds to vertical movement, the texture has already been shifted and rotated by the previous parts of the path. The new vertical movement cannot simply be applied to the original UVs. It has to be added in the already rotated coordinate system while preserving the current texture position.

Both paths end with the camera at the same point D, but they show different parts of the texture. This is not a true 3D rotation of a sphere, but an approximation built from a tileable 2D texture.

Because the final texture state depends on the path, the system has to remember the current state and apply each new change on top of it.

A material does not preserve this kind of state between frames, so I split the process between Blueprint and the material. Blueprint keeps the movement history, while the material receives the final accumulated 2D transform.

### Determining Texture Movement

Blueprint stores two kinds of information. First, the accumulated texture offset and rotation. Second, data from the previous camera position relative to the planet: how far above or below the equator the camera was, and which side of the planet it was viewing. On every update, Blueprint compares the previous state with the current one, determines how the viewpoint changed, and adds the corresponding offset or rotation to the accumulated transform.

Blueprint first calculates the direction from the center of the planet to the camera and transforms it into the actor's local space. This makes the texture movement depend not only on the camera position, but also on the planet's current orientation. That direction is then split into latitude and longitude.

Latitude is based on how far the camera direction points up or down relative to local +Z. The difference between the current and stored latitude becomes the vertical texture offset.

For longitude, the camera direction is first projected onto the equatorial plane by removing its component along the pole axis. What remains is a horizontal direction showing which side of the planet the camera is viewing from. Blueprint compares it with the direction from the previous update and measures the angle between them around local +Z. The sign of that angle gives the direction of movement, while its magnitude gives the change in longitude.

*Near a pole, the equatorial projection becomes very short, and at the pole itself it disappears completely. All meridians meet there, so longitude can no longer be determined reliably. In that region, the system temporarily stops updating longitude and keeps the last valid equatorial direction instead. Keeping the last valid direction prevents random texture jumps while the camera passes through the polar area.*

The longitude change is used differently depending on latitude. Away from the poles, it produces a mostly horizontal offset. As the camera approaches a pole, the influence of that offset decreases, and the longitude component gradually turns into texture rotation.

### Vertical Offset Sign

In the current version, local +Z is used as the north-south pole axis, while local +X defines the initial longitude direction. When the camera orbits over the top or bottom of the planet, its screen-space up direction can end up pointing against the planet's local +Z axis. If the latitude change keeps the same sign, the texture starts moving across the screen in the wrong direction.

Blueprint compares CameraUp with the world-space direction of the planet's local +Z axis. When they point in opposite directions, it inverts the vertical offset. This keeps the movement along the meridian visually continuous after the camera crosses a pole.

### Finding the Rotation Pivot

For the texture rotation to look correct, the system needs to know where the pole is located on the card. By comparing the direction from the center of the planet to the camera with the planet's Local Z, it determines which hemisphere the camera is in. From that, it selects the visible pole direction: either the north or south pole around which the texture should rotate.

The selected pole direction is first transformed into the camera basis, which is built directly from the camera orientation and always remains parallel to the screen. The resulting point corresponds to the pole's position on screen. It is then projected into the card's 2D space using the same stereographic projection principle that the material uses to create the pseudo-spherical UVs.

The result is a 2D point representing the current position of the visible pole on the card, which becomes the texture rotation pivot. The pivot is not fixed. It is recalculated continuously as the camera moves or the actor rotates, taking the accumulated offset and rotation into account.

### Combining Offset and Rotation

New offset and rotation cannot simply be added to the previous values independently. If the texture has already been rotated, the next offset has to follow its current orientation. The visible pole position can also change because of camera movement, actor rotation, and the offset that has already been accumulated.

The system stores the entire movement history as a single accumulated 2D transform. It consists of a total rotation angle and a total translation relative to the UV origin.

For example, the texture can be rotated by 30° around some point A. The same result can also be represented by rotating it by 30° around (0, 0), then applying a translation that moves it back into the same final position.

First, the system determines where the current pole lies inside the texture after the existing rotation and translation have been applied. It then calculates the small longitude and latitude changes for the current frame.

The new offset is initially calculated in the original UV axes. Since the texture may already be rotated, that offset direction is rotated by the accumulated angle before being added to the total Translation.

If part of the longitude change needs to become rotation near the pole, the system adds a small rotation angle and adjusts the translation at the same time so that the rotation happens around the calculated pole position.

After each update, the result is stored again in the same unified form, and the material receives the final state:

- RotationTurns: the total accumulated rotation around the UV origin;
- Translation: the total 2D offset, including both regular texture movement and the translation introduced by all previous rotations around different pole positions.

### A Simplified Version

The effect is split into several independent layers:

- World Position Offset keeps the flat card facing the camera.
- The UV transformation in the material creates the illusion of volume.
- Blueprint handles continuous surface movement: it tracks camera movement and actor rotation, stores the accumulated surface state, and passes LocalOffset and RotationTurns to the material.

I also have a simplified version that uses only horizontal and vertical offsets. It does not accumulate state, does not rotate the texture near the poles, and does not need any separate Blueprint logic. All movement is calculated directly in the material.

The simplified version works well for distant background planets, decorative objects, UI scenes, and other cases where the camera moves within a limited range and never passes over the poles. It is also useful when you only need a slight sense of surface movement and do not need the texture to preserve its exact previous trajectory.

The full version is more suitable when the camera can orbit freely around the object, approach the poles, or when rotating the planet itself has to preserve continuous texture movement. The simplified version is less flexible, but much easier to set up and stays entirely inside the material.

### Where This Effect Can Be Useful

The texture does not need to be prepared as a spherical map in advance.

With a regular sphere, the surface image has to match the sphere's UV layout. Here, the material can use any regular tileable 2D texture. It does not need to be converted into an equirectangular map or specially adapted for poles and meridians. You can use an existing tileable texture, a procedural pattern, or a quickly built material directly as the planet surface.

The camera can still orbit the object and view it from different sides. As the texture shifts and rotates, it creates the impression that the image is actually attached to a 3D surface.

The effect simulates changes in the visible side of the planet by moving the texture, but it does not create real spherical geometry. The final texture state therefore depends on the camera movement history. Two different paths can end at the same camera position while showing different areas of the texture. That path dependence is part of the underlying 2D simulation.

### [Alina Ledeneva](https://www.linkedin.com/in/aledeneva/), UE5 Technical Artist
