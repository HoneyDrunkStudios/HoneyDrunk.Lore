---
source: "https://developer.blender.org/docs/release_notes/5.2/pipeline_io/"
title: "Blender 5.2 LTS: Pipeline & I/O"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-10-28"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.2 LTS: Pipeline & I/O

Source: https://developer.blender.org/docs/release_notes/5.2/pipeline_io/

## glTF

### Exporter

- New feature: Point Cloud export ([153bade6e5](https://projects.blender.org/blender/blender/commit/153bade6e54aee7e591c996a6c2a55ae1eb37215))
- New feature: EXT_meshopt_compression and KHR_meshopt_compression export ([3e6b5cae21](https://projects.blender.org/blender/blender/commit/3e6b5cae21b3723d41851b6c4b431f73887b3299))
- New feature: KHR_materials_iridescence extension export ([0e94cdb502](https://projects.blender.org/blender/blender/commit/0e94cdb502e9d2a07b5227d11ca1352355f84c4c))
- New feature: KHR_materials_dispersion extension export ([ed7e9a7fe3](https://projects.blender.org/blender/blender/commit/ed7e9a7fe354ec45f2f4e8a560db07d104aea1ac))
- New feature: Hooks are now able to stop the export ([6fb868797b](https://projects.blender.org/blender/blender/commit/6fb868797b298c3b45ffca7bc94f3ba7a5cb975f))
- New feature: Export official KHR primitive attributes ([28e89be4ed](https://projects.blender.org/blender/blender/commit/28e89be4edab94bf2fa92cba562eb36988ab6761))
- Performance: Use inline material when possible ([49bff0770c](https://projects.blender.org/blender/blender/commit/49bff0770c42ba57fea3550f59e8a00eccaf87df))
- Performance: Animation export enhancement by disabling viewport ([1a679af4f4](https://projects.blender.org/blender/blender/commit/1a679af4f46b22fab0a6c3de2ce54968f4c9d306))
- Nodes are now sorted by name ([6b583d742c](https://projects.blender.org/blender/blender/commit/6b583d742cdef234a3aa71b327bd03e3f393f888))
- Fix node group traversal ([1edfbc4150](https://projects.blender.org/blender/blender/commit/1edfbc415070b82506f513aa4fca6a9a1e9a5842))
- Fix crash reloading scripts ([694b967967](https://projects.blender.org/blender/blender/commit/694b967967c2fc03705a49e6435180b253d84744))
- Fix Vertex Color export when used only in subset of materials ([bfb768885d](https://projects.blender.org/blender/blender/commit/bfb768885d89630af55537ab877c3a96c40952ff))
- Enable UI filter for glTF Collections (action, variant, animation) ([28bae3297d](https://projects.blender.org/blender/blender/commit/28bae3297d248c902690e37e101e5edc5133ee66))
- Lots of fixes on Animation Pointer ([96c6a14a54](https://projects.blender.org/blender/blender/commit/96c6a14a54d8ef5ace236d6912de0d881c699806))

### Importer

- New feature: Point Cloud import ([d9412b1188](https://projects.blender.org/blender/blender/commit/d9412b1188f9a21df19ab07ccc88c33a37be17cc))
- New feature: Import official KHR primitive attributes ([28e89be4ed](https://projects.blender.org/blender/blender/commit/28e89be4edab94bf2fa92cba562eb36988ab6761))
- New feature: EXT_meshopt_compression and KHR_meshopt_compression export ([3e6b5cae21](https://projects.blender.org/blender/blender/commit/3e6b5cae21b3723d41851b6c4b431f73887b3299))
- New feature: KHR_materials_iridescence extension import ([0e94cdb502](https://projects.blender.org/blender/blender/commit/0e94cdb502e9d2a07b5227d11ca1352355f84c4c))
- New feature: KHR_materials_dispersion extension import ([ed7e9a7fe3](https://projects.blender.org/blender/blender/commit/ed7e9a7fe354ec45f2f4e8a560db07d104aea1ac))
- Fix importing multiple custom attributes that sometimes crash ([74d3d06770](https://projects.blender.org/blender/blender/commit/74d3d06770403ef649e348b7a5139c54d96e9393))
- Lots of fixes on Animation Pointer ([96c6a14a54](https://projects.blender.org/blender/blender/commit/96c6a14a54d8ef5ace236d6912de0d881c699806))

## USD

- [Color space support](https://openusd.org/release/user_guides/color_user_guide.html). On import colors are converted to the blend-file working space. Export tags prims and image textures with their color space. ([PR#157196](https://projects.blender.org/blender/blender/pulls/157196))
- Added new export option to control how frequently to save/flush the USD data to reduce peak memory usage ([aabaffd311](https://projects.blender.org/blender/blender/commit/aabaffd311f11309cffa899e3349c3fe31bea130))
- Blender NURBS Surface objects are now exported (as mesh data) ([1cdf15ae4f](https://projects.blender.org/blender/blender/commit/1cdf15ae4f76eade8c1008812b61039509086d66))

## Images

- OpenEXR: Faster writing of half-precision (FP16) EXRs. ([PR#157874](https://projects.blender.org/blender/blender/pulls/157874))

## Movies

- Stereoscopic metadata is exported. No need to post-process the video for correct playback in video players. ([5635567dad](https://projects.blender.org/blender/blender/commit/5635567dadc5875ba6ed44c4cdf1430cad3cc4ba))
- Panoramic camera metadata is exported. Only full equirectangle cameras are supported. ([0d98bf9ff6](https://projects.blender.org/blender/blender/commit/0d98bf9ff61cc58daa7debd886539982967ba8e9))

## Alembic

- Added support for importing non-animated and animated object visibility. Animations are imported as F-Curves. ([PR#157983](https://projects.blender.org/blender/blender/pulls/157983), [PR#158321](https://projects.blender.org/blender/blender/pulls/158321))
- Added support for importing animated camera data as F-Curves ([PR#158321](https://projects.blender.org/blender/blender/pulls/158321))
- Original coordinates for subdivision meshes are now imported ([PR#159195](https://projects.blender.org/blender/blender/pulls/159195))
- Topological changes for subdivision meshes are now properly detected ([PR#159195](https://projects.blender.org/blender/beldner/pulls/159195))

## STL

- Added option how to eval (Viewport vs. Render) during export ([PR#157127](https://projects.blender.org/blender/blender/pulls/157127)).
