---
source: "https://developer.blender.org/docs/release_notes/5.3/geometry_nodes"
title: "Blender 5.3: Geometry Nodes"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-11"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: Geometry Nodes

## Highlights

Geometry Nodes welcome first building blocks for custom fluid simulations with new volume grid nodes, and a low level
node for constructing curves with custom topology. Curves get Miter Scale support and NURBS inputs, Grease Pencil
data gets dedicated input nodes, and several new utility nodes make everyday setups simpler.

---

### Volume Grids

A few new nodes for working with volume grids have been added, with future custom fluid simulations in mind.

This includes Rasterize Points, Poisson Solver, Grid Topology Boolean, Deactivate Voxels and Get Grid Names, plus new and improved quadratic and cubic modes for grid sampling.

[All Grid changes.](https://developer.blender.org/docs/release_notes/5.3/geometry_nodes/#grids)

[![New volume grid nodes](https://developer.blender.org/docs/release_notes/5.3/images/volume_grid_nodes.png)](https://developer.blender.org/docs/release_notes/5.3/images/volume_grid_nodes.png)

---

### Construct Curves

The new **Construct Curves** node is a low level node for building curves with a custom topology. It expects a list of positions and curve offsets.

The curve offsets describe which positions are connected. The topology is encoded such that neighboring offsets describe the start and end of each curve. For example `[0, 5]` is a single curve with 5 points, starting at index 0 and ending at index 5 exclusive. The list `[0, 3, 10, 12]` describes a list with three curves, the first has 3 points, the second 7 points and the last 2 points.

[All Curves changes.](https://developer.blender.org/docs/release_notes/5.3/geometry_nodes/#curves)

[![Construct Curves node](https://developer.blender.org/docs/release_notes/5.3/images/construct_curves.png)](https://developer.blender.org/docs/release_notes/5.3/images/construct_curves.png)

---

### Miter Scale

The *Curve to Mesh* built-in node and *Curve to Tube* asset have a Miter Scale input now. This keeps the curve radius visually consistent over its entire length.

[All Curves changes.](https://developer.blender.org/docs/release_notes/5.3/geometry_nodes/#curves)

[](../videos/miter_scale.mp4)

Miter Scale keeps the curve radius visually consistent.

---

### Input Nodes

New input nodes for accessing built-in attributes for NURBS curves have been added. Those correspond to the recently added *Set NURBS Order* and *Set NURBS Weight* nodes.

Various input nodes for Grease Pencil data are available now as well. The data was accessible as raw attributes before already.

[![NURBS input nodes](https://developer.blender.org/docs/release_notes/5.3/images/nurbs_input_nodes.png)](https://developer.blender.org/docs/release_notes/5.3/images/nurbs_input_nodes.png)

[![Grease Pencil input nodes](https://developer.blender.org/docs/release_notes/5.3/images/grease_pencil_input_nodes.png)](https://developer.blender.org/docs/release_notes/5.3/images/grease_pencil_input_nodes.png)

---

### New Utility Nodes

The **Combine List** node simplifies creating short lists with a fixed number of elements. The **Get Vector Component** node allows getting the x, y or z component with an integer index, and is also supported in shader and compositor nodes. The **Geometry Materials** node outputs the list of materials used by a geometry.

[All New Nodes changes.](https://developer.blender.org/docs/release_notes/5.3/geometry_nodes/#new-nodes)

[![Combine List node](https://developer.blender.org/docs/release_notes/5.3/images/combine_list_node.png)](https://developer.blender.org/docs/release_notes/5.3/images/combine_list_node.png)

Combine List node

[![Get Vector Component](https://developer.blender.org/docs/release_notes/5.3/images/get_vector_component_node.png)](https://developer.blender.org/docs/release_notes/5.3/images/get_vector_component_node.png)

Get Vector Component

[![Geometry Materials](https://developer.blender.org/docs/release_notes/5.3/images/geometry_materials_node.png)](https://developer.blender.org/docs/release_notes/5.3/images/geometry_materials_node.png)

Geometry Materials

---

## Changelog

### Grids

- **Rasterize Points**: New node for converting points to grids using rasterization. ([83397820](https://projects.blender.org/blender/blender/commit/83397820))
- **Poisson Solver**: New node for solving Poisson equations on grids. ([e0f6bb4fb1](https://projects.blender.org/blender/blender/commit/e0f6bb4fb1d75907af2ad0d538a69cfd2adffbfb))
- **Grid Topology Boolean**: New node for combining active grid voxels with boolean operations. ([9498c3a18c](https://projects.blender.org/blender/blender/commit/9498c3a18c560bd7b8f591e7098b799fbef46d76))
- **Deactivate Voxels**: New node for removing active voxels from volume grids. ([3874a0bb03](https://projects.blender.org/blender/blender/commit/3874a0bb0300d547ff9488b5f8cdf52b77988676))
- **Sample Grid**: New and improved quadratic and cubic modes for grid sampling. ([3e38f8be15](https://projects.blender.org/blender/blender/commit/3e38f8be15a4a8b837d518b218d19407ed9bc733))
- **Get Grid Names**: New node. ([a0baf7ccbb](https://projects.blender.org/blender/blender/commit/a0baf7ccbb4db4567ae79da948a4a2f272cb0e86))

### Curves

- **Curve to Mesh**: New Miter Scale input, also added to the *Curve to Tube* asset. ([b1c96afb78](https://projects.blender.org/blender/blender/commit/b1c96afb78a6), [222c2d501f](https://projects.blender.org/blender/blender/commit/222c2d501fab14b1c07db031c0022c00d5411835))
- **Construct Curves**: New low level node for building curves with a custom topology from positions and curve offsets. ([0e151993db](https://projects.blender.org/blender/blender/commit/0e151993db7e5de43323ec1d0688fe69f8b06ea5))
- **NURBS Inputs**: New input nodes for the built-in attributes of NURBS curves, matching *Set NURBS Order* and *Set NURBS Weight*. ([8be98e47d7](https://projects.blender.org/blender/blender/commit/8be98e47d75100674a28df7445ac74542ffcf13d))

### Grease Pencil

- **Input Nodes**: Various new input nodes for Grease Pencil data. ([70898c5508](https://projects.blender.org/blender/blender/commit/70898c55089dc3a45a23725fbb7b378ece4ee710))

### New Nodes

- **Combine List**: New node for creating short lists with a fixed number of elements. ([cfc10639fb](https://projects.blender.org/blender/blender/commit/cfc10639fb26f5ecbb426eeff8cff2f4c1e8ccef))
- **Get Vector Component**: New node for getting the x, y or z component with an integer index, also supported in shader and compositor nodes. ([216b62e05c](https://projects.blender.org/blender/blender/commit/216b62e05c631930b1b39ca6b1f7f5ed2f0907be))
- **Geometry Materials**: New node that outputs the list of materials used by a geometry. ([b3d62684bc](https://projects.blender.org/blender/blender/commit/b3d62684bc82ef6cebd0102c8d3769579bca0483))

### Node Improvements

- **Realize Instances**: New *Preserve Normals* option for instances with negative transform determinant. ([970e052580](https://projects.blender.org/blender/blender/commit/970e052580a0ba1fb28a4416d8f15187eb5a1c3a))
- **Bone Info**: Output envelope properties. ([8b2e9ffe59](https://projects.blender.org/blender/blender/commit/8b2e9ffe593ed578b4))
- **Bake**: Path template support. ([PR#164240](https://projects.blender.org/blender/blender/pulls/164240))

### Usability

- **Index Switch**: Drag-to-search visibility. ([f5b26e1654](https://projects.blender.org/blender/blender/commit/f5b26e16542ee56b21f4709a1b9b38861196f5ea))
- **Repeat Zone**: Link-drag-search for the iterations input. ([ea28033ce4](https://projects.blender.org/blender/blender/commit/ea28033ce48418985893b071914976a18e8a777c))
