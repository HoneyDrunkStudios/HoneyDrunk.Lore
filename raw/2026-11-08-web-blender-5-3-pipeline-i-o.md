---
source: "https://developer.blender.org/docs/release_notes/5.3/pipeline_io/"
title: "Blender 5.3: Pipeline & I/O"
author: "Blender Developers"
date_published: "unknown"
date_clipped: "2026-11-08"
category: "Technical Art & Creator Tools"
source_type: "web"
capture_note: "Upcoming Blender 5.3 release notes captured before release; details can change."
---

# Blender 5.3: Pipeline & I/O

## Highlights

USD gets a new Collection Importer, which can be configured per collection and stored in the .blend file,
along with support for importing Gaussian Splats. Gaussian Splats can also be imported from glTF, which
additionally gains animation pointers for custom properties, KTX2 textures, import operator presets, and many
exporter fixes. Alembic now handles subdivision, point clouds, velocities, attributes, and color attributes.

### Collection Importer

The USD importer can now be associated with a Collection. The importer can be added and configured in the
Collection's properties panel. Settings are stored in .blend files for easy sharing and persistence across
Blender sessions.

Like the [Collection Exporters](https://docs.blender.org/manual/en/latest/scene_layout/collections/collections.html#exporters), this feature can help streamline the process of re-importing the same asset(s)
repeatedly, or be used for other project organization purposes.

Support is currently limited to the USD file format, and it could be expanded to additional formats in the future.
Learn more about the next steps in the [main design](https://projects.blender.org/blender/blender/issues/132171) of the project.

See all [USD changes](https://developer.blender.org/docs/release_notes/5.3/pipeline_io/#usd).

---

## Changelog

### USD

- **Collection Importer**: The USD importer can now be added to a Collection and configured in its properties panel. ([145d210733](https://projects.blender.org/blender/blender/commit/145d210733b82b78480101950989b98d17fad213), [20ca6d4fc3](https://projects.blender.org/blender/blender/commit/20ca6d4fc3167368488c96c487633fff5f1fbad4), [b53c9f35fa](https://projects.blender.org/blender/blender/commit/b53c9f35fa4bc510bf51ea140ab74ba2ed9726c4), [4e2d6042b9](https://projects.blender.org/blender/blender/commit/4e2d6042b95e8586e1a4ce30e74ba3d2db4f1d95))
- **Import**: Add support for importing the UsdVolParticleField3DGaussianSplat schema, i.e. Gaussian Splats. ([cfd6ba27e0](https://projects.blender.org/blender/blender/commit/cfd6ba27e049ef734824f5771f6c3c4b726ab7f1))
- **Export**: Mesh export now supports writing normals matching Blender's original representation rather than converting them to corner/faceVarying first. ([46d0a7ccd4](https://projects.blender.org/blender/blender/commit/46d0a7ccd4187b064eb9bc4bf6bdf59cd1114b00))
- **General**: Added support for importing and exporting Matrix4d primvar attribute data. ([5ab643bb46](https://projects.blender.org/blender/blender/commit/5ab643bb46a18b6db9f4f2e3cf455bae7659d020))

### Alembic

- **Subdivision**: Import and export support for subdivision parameters from subdivision surface modifiers. During import, a subdivision surface modifier is automatically added to meshes. ([f2a1c2848a](https://projects.blender.org/blender/blender/commit/f2a1c2848a1c19fcf275620dd77c926262de89fb))
- **Point Clouds**: PointCloud objects export is now supported. ([14a042845b](https://projects.blender.org/blender/blender/commit/14a042845b0e94d49c000d095c13bc26412958e0))
- **Velocities**: Curves importer and exporter is extended to read and write the velocity attribute for curves, similar to meshes and points. ([0729fe73e9](https://projects.blender.org/blender/blender/commit/0729fe73e9f0086195f26c53f98a7bcfa3e01ebd))
- **Attributes**: Added export support for arbitrary attributes on meshes, curves, and point clouds. ([19f60a40ff](https://projects.blender.org/blender/blender/commit/19f60a40ff9208fddc013ff92f9882c38c75ec29))
- **Radii**: Curves and points radii can be written as a single value, saving disk space. Radii which are not written in the point domain are now read as well. ([c6447e69c6](https://projects.blender.org/blender/blender/commit/c6447e69c65bae36537fccca4d0d79c944d59fe6))
- **Color Attributes**: The default and active color attributes are now remembered when exporting and importing back into Blender. When importing a file from another software, they are set to the first color layer. ([cc44ebbd24](https://projects.blender.org/blender/blender/commit/cc44ebbd242bda2549574e980bc95fb6bb783ca6))

### glTF 2.0

#### Importer

- **Gaussian Splats**: Import glTF Gaussian Splats. ([d73e2817bb](https://projects.blender.org/blender/blender/commit/d73e2817bb2e714065754a902441be5f325ce19b))
- **Animation Pointer**: Import Animation Pointer for extras (as Custom Properties), for int/float/bool. ([aa6af4df7c](https://projects.blender.org/blender/blender/commit/aa6af4df7c1782a3790ba66dfa289f3b736079b8))
- **Point Cloud**: Import Material and Vertex Color on Point Cloud. ([b765a581e5](https://projects.blender.org/blender/blender/commit/b765a581e5d2bee3b39dd392400244e8ae674e11))
- **Hooks**: Display full traceback when an exception occurs in hooks. ([195256308e](https://projects.blender.org/blender/blender/commit/195256308ea9700054ca5f1c1ca572dd388af666))
- **Presets**: Add operator presets at import. ([d46e658354](https://projects.blender.org/blender/blender/commit/d46e658354e2f551ce734f4eca00ed52096677e2))
- **KTX2**: Import files with the KHR\_texture\_basisu extension (KTX2 management). ([f75ffda597](https://projects.blender.org/blender/blender/commit/f75ffda5977678305f24caa53abf7d77a986275e))

#### Exporter

- **Animation Pointer**: Export Animation Pointer for extras (Custom Properties), for int/float/bool. ([aa6af4df7c](https://projects.blender.org/blender/blender/commit/aa6af4df7c1782a3790ba66dfa289f3b736079b8))
- **Animation Pointer**: Enable Animation Pointer for all animation export modes. ([aa6af4df7c](https://projects.blender.org/blender/blender/commit/aa6af4df7c1782a3790ba66dfa289f3b736079b8))
- **Hooks**: Display full traceback when an exception occurs in hooks. ([195256308e](https://projects.blender.org/blender/blender/commit/195256308ea9700054ca5f1c1ca572dd388af666))
- **KTX2**: Export files with the KHR\_texture\_basisu extension (KTX2 management). ([f75ffda597](https://projects.blender.org/blender/blender/commit/f75ffda5977678305f24caa53abf7d77a986275e))
- **Collection Exporter**: New options for the center of the Collection Exporter. ([e7ddf4c16c](https://projects.blender.org/blender/blender/commit/e7ddf4c16ca52d2bcf185ffad675f61da3bf7122))
- **Instance Collections**: Remove one level when exporting an instance collection. ([e516032021](https://projects.blender.org/blender/blender/commit/e51603202143a1766433897bb3125e132483d783))
- **Materials**: Performance enhancement for material (node tree) export. ([1f262d6832](https://projects.blender.org/blender/blender/commit/1f262d6832021d855a643c5c6afbb0ee60194356))
- **UI**: Capitalize words in the UI. ([806a484e1f](https://projects.blender.org/blender/blender/commit/806a484e1f87018079b4ff8f848647e6d92445c3))

##### Fixes

- **Fixed**: multiple bugs on Point Cloud export. ([f994b8e7ba](https://projects.blender.org/blender/blender/commit/f994b8e7ba1a35835706dfa89d79cf00c94fea55), [49c44d90ea](https://projects.blender.org/blender/blender/commit/49c44d90eacc3ca88eba832522be4990cf910714))
- **Fixed**: filtering in instance collection. ([b6cf4a455d](https://projects.blender.org/blender/blender/commit/b6cf4a455dbc916830ea0797645ce53e8efc9fe3))
- **Fixed**: default file filter in File Browser Editor. ([566591b8ec](https://projects.blender.org/blender/blender/commit/566591b8ec0d15f368e79ee91f33dd01695a3a08))
- **Fixed**: joint cache after reload scripts. ([3f68a3536f](https://projects.blender.org/blender/blender/commit/3f68a3536f19d4451f46e6358646b45e4d4e55d2))
- **Fixed**: light strength export. ([41e992ee8d](https://projects.blender.org/blender/blender/commit/41e992ee8d073c705f647b4ddc2d8470780de6c6))
- **Fixed**: non-mesh export. ([94a7fd639e](https://projects.blender.org/blender/blender/commit/94a7fd639ecc8d54476973b9ee3ddf7a8a71234a))
- **Fixed**: exporting loose edges. ([0daf7223f0](https://projects.blender.org/blender/blender/commit/0daf7223f0c64690aad124a63d65b182bab3eecd))
- **Fixed**: exporting active collection when exporting full collection tree. ([4eeea9f6a0](https://projects.blender.org/blender/blender/commit/4eeea9f6a097f7a2d6a99f173998bb9b5146774b))
- **Fixed**: bone parenting to a skinned mesh. ([288fd2b898](https://projects.blender.org/blender/blender/commit/288fd2b89870b63eaa219537d6ef7a3fcb93d1e7))
- **Fixed**: image name export by keeping suffixes. ([dc04c55a21](https://projects.blender.org/blender/blender/commit/dc04c55a2154d21f0b21ca383c47484ce30c16ea))
- **Fixed**: normalizing image path before existence check. ([8669a33488](https://projects.blender.org/blender/blender/commit/8669a33488b604d1189ba32231c22eb82681af2e))
- **Fixed**: Vertex Color export. ([946fea666e](https://projects.blender.org/blender/blender/commit/946fea666edbeab55aba096ddfa8d9e1f5a0adcd))
- **Fixed**: Custom Props export. ([5bb3bd7e8e](https://projects.blender.org/blender/blender/commit/5bb3bd7e8ebb0fb09c3cb005cbf412ebd9c28756))
- **Fixed**: GPU instances node removal. ([dd3a1f3975](https://projects.blender.org/blender/blender/commit/dd3a1f3975b703d27f9b091b99c0ba192c90c826))

### Images

- **ICC Profile**: Saving sRGB image files now includes an ICC profile. ([#163017](https://projects.blender.org/blender/blender/issues/163017))
- **OpenEXR**: Improved support for display color interop IDs in OpenEXR files and color management. ([#163006](https://projects.blender.org/blender/blender/issues/163006))
- **OpenEXR**: Improved reading and writing of multilayer OpenEXR files with lossy DWA compression. ([#162994](https://projects.blender.org/blender/blender/issues/162994))
