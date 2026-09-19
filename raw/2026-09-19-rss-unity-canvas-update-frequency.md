---
source: "https://dev.to/gameoptim/optimizing-canvasbuildbatch-cost-via-staticdynamic-ui-separation-5a1h"
title: "Optimizing Canvas.BuildBatch Cost via Static/Dynamic UI Separation"
author: "GameOptim"
date_published: "2026-09-17"
date_clipped: "2026-09-19"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# Optimizing Canvas.BuildBatch Cost via Static/Dynamic UI Separation

Source: [Optimizing Canvas.BuildBatch Cost via Static/Dynamic UI Separation](https://dev.to/gameoptim/optimizing-canvasbuildbatch-cost-via-staticdynamic-ui-separation-5a1h)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

GameOptim reports a Unity UI case where rotating decorations and static weapon icons shared a Canvas. Frequent transform changes caused batching work that included otherwise unchanged content.

The proposed fix separates frequently changing elements into a small dynamic Canvas and keeps stable icons, frames, and backgrounds in a static Canvas. The author reports a reduction in the measured main-thread rendering marker from 0.43 ms to 0.09 ms in this scenario.

The article connects that marker to waiting for Canvas.BuildBatch work and recommends device-side profiling. These measurements and the diagnostic interpretation come from the tool vendor's case study; they are not universal thresholds or a substitute for inspecting a project's actual timeline.

HoneyDrunk implication: group UI elements by update frequency when profiling shows batching pressure. Measure the result alongside draw calls: separate Canvases cannot batch together and add their own overhead, so CPU savings must be weighed against rendering cost and complexity.
