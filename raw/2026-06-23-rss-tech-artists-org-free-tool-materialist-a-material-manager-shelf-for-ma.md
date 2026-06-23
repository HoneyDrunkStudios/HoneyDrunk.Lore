---
source: "https://www.tech-artists.org/t/free-tool-materialist-a-material-manager-shelf-for-maya/18429"
title: "[Free tool] Materialist - a material manager shelf for Maya"
author: "Tech-Artists.org"
date_published: "Mon, 22 Jun 2026 17:05:07 +0000"
date_clipped: "2026-06-23"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# [Free tool] Materialist - a material manager shelf for Maya

Source: https://www.tech-artists.org/t/free-tool-materialist-a-material-manager-shelf-for-maya/18429

[Free tool] Materialist - a material manager shelf for Maya - Tools - Tech-Artists.Org 
Tech-Artists.Org 
[Free tool] Materialist - a material manager shelf for Maya 
Tools 
maya , 
python , 
codiing 
ruxlag 
June 22, 2026, 5:05pm
1 
Hi all! I’m a 3D artist (modeling / lookdev / lighting) and I kept rebuildin the same material-wrangling helpers on every project, so I cleaned them up into one shelf tool and open-sourced it. Sharing in case it’s useful.
Materialist is a single-file Maya tool ([Python 3, Maya 2022+]) for:
searching / filtering materials (by name, namespace, or “has a shading group”) 
assigning a material to a selection, and selecting objects by material 
creating + assigning a material from a type dropdown 
duplicating a shading network with clean, unique names, no `pasted__` prefix and no trailing numbers 
merging duplicate file-texture nodes** onto one shared node 
batch-renaming shading groups, deleting unused nodes 
exporting / importing a shader’s full upstream network 
finding objects with no shader or stuck on the initial shading group 
It’s a single `materialist.py` you drop in your scripts folder. MIT-licensed.
GitHub: [link] 
Feedback / bug reports / PRs very welcome - especially edge cases in the duplicate and merge tools, since those touch a lot of node graphs.
Home 
Categories 
Guidelines 
Terms of Service 
Privacy Policy 
Powered by Discourse , best viewed with JavaScript enabled
