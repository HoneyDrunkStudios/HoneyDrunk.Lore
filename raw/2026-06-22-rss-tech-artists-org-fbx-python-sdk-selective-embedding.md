---
source: "https://www.tech-artists.org/t/fbx-python-sdk-selective-embedding/18416"
title: "FBX Python SDK Selective Embedding"
author: "Tech-Artists.org"
date_published: "2026-06-14"
date_clipped: "2026-06-22"
category: "Technical Art & Creator Tools"
source_type: "rss"
discovered_via: "https://www.tech-artists.org/latest.rss"
---

# FBX Python SDK Selective Embedding

Source: https://www.tech-artists.org/t/fbx-python-sdk-selective-embedding/18416

# [FBX Python SDK Selective Embedding](/t/fbx-python-sdk-selective-embedding/18416)

[Coding](/c/coding/19)

[fbx](https://www.tech-artists.org/tag/fbx),
[codiing](https://www.tech-artists.org/tag/codiing),
[python](https://www.tech-artists.org/tag/python),
[pipeline](https://www.tech-artists.org/tag/pipeline)

[VVVSLAVA](https://www.tech-artists.org/u/VVVSLAVA)

June 14, 2026, 12:46pm

1

Greetings community!  
I’ve been really diving into the FBX Python SDK.  
I wrote, and am continuing to improve, an FBX exporter for 3DEqualizer4 (with advanced embedding capabilities for geometry, textures, plates, and additional lens files).  
Most of the issues that arose while writing the code were resolved, including by modifying the already exported binary FBX file. ![:slight_smile:](https://www.tech-artists.org/images/emoji/twitter/slight_smile.png?v=14 ":slight_smile:")  
However, I couldn’t solve this problem:  
When exporting, if we need to embed into the FBX file, we set the following in IOSettings:  
`fbx_sdk_manager.GetIOSettings().SetBoolProp(fbx.EXP_FBX_EMBEDDED, True)`  
However, this affects all media assets globally.  
I need to exclude certain files (`FbxVideo`) from the embedding procedure.  
However, these objects (`Video`) must retain the correct original file paths for the properties:  
`Filename`, `RelativeFilename` (`Path`, `RelPath`)  
The only guaranteed working solution to this problem is to ensure that the files at the specified paths do not physically exist during export.  
However, this is a very unreliable and extremely risky solution. Furthermore, these files may be locked, or the user may not have the necessary permissions to operate on them.  
I wouldn’t want to resort to complex binary parsing and modification of an already exported file (again).  
The FBX C++ SDK contains classes and methods (possibly) related to my problem. However, I don’t know how to access them from the FBX Python SDK (and will it help?).
