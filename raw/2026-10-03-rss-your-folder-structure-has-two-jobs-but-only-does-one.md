---
"source": "https://blog.sterlingfreeman.net/posts/folder-structure-two-jobs"
"title": "Your Folder Structure Has Two Jobs, but Only Does One"
"author": "Sterling Freeman"
"date_published": "2026-10-01"
"date_clipped": "2026-10-03"
"category": "Software Architecture"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# Your Folder Structure Has Two Jobs, but Only Does One

# Your folder structure has two jobs, but only does one

Finding files and deciding where to put them are different jobs. Your folder structure needs to account for both.

Get one of these jobs wrong and it costs a moment. Get the other wrong and it compounds.

Your folder structure is an information tree, whether it holds code, notes, or documents. Any information tree typically gets asked two things. **Navigation, or finding:** *“where do I look to find X?”* **Classification, or placing:** *“where does X belong when I create it?”*

Finding and placing each have their own way to measure them.

**Tree testing**starts a member of the target group at the top of the tree with a set of instructions and notes the time and points of friction.**Closed card sorting**gives people the same folders, guidance, and files, then checks whether the files land in the same places.**Open card sorting**asks people to create the groups too, which is useful one step earlier, before the structure has been decided.

The names that help you find aren’t the names that help you place.

The notion that names are a poor way to agree on placement is not new. HCI researcher George Furnas and coauthors quantified this in 1987 as the *vocabulary problem*: when two people independently name the same thing, they agree on terminology less than 20% of the time.

A form rendered inside a modal. Does it go in

`forms/`

, or in`modals/`

? Depends who you ask.

[Which job does your tree do?](#which-job-does-your-tree-do)

The comparison below uses UI components, but the same tradeoff applies to folder structures for other kinds of code, notes, or documents.

[Role-based navigation](#role-based-navigation)

A common shape, this one from a [blog post](https://insight.akarinti.tech/best-practices-for-using-shadcn-ui-in-next-js-2134108553ae):

```
components/
├── ui/ # shadcn primitives
├── layout/ # Navbar, footer, sidebar
├── forms/ # Reusable form components
├── modals/ # Dialogs, popups
└── shared/ # General reusable components
```


A folder called `forms/`

doesn’t need much explaining. Developers, designers, copywriters, and product managers can scan the tree and know where to look.

Role-based structure optimizes for finding at the cost of placing. It defers the vocabulary problem to the moment a file is created.

The tell is the catch-all folder, whatever it is called here: `shared/`

, `utils/`

, `misc/`

. It exists because the other folders have edges, and edges mean things fall through. It catches everything that doesn’t fit. Left untended, it becomes the majority of the codebase.

Role-based is a taxonomy, not an architecture. It organizes by appearance, not by rules. For instance, a modal can import from forms, forms from layout, layout from shared. Nothing enforces dependency direction or structure.

[Layer-based classification](#layer-based-classification)

The other shape, three layers decided by a mechanical rule:

```
components/
├── core/ # Untouched vendor components (e.g. shadcn, private registry)
├── elements/ # Enriched UI vocabulary
└── patterns/ # Composed, purpose-specific combinations
```


This is the layout I find myself reusing in solo projects and proposing in team settings: core, elements, patterns (CE Pattern, said “see pattern”).

**Core** — unmodified vendor source. Never hand-edited. If you need to change behaviour, wrap it in elements.

**Elements** — one source file in, same or more exports out. The exports are enriched or restyled variants of what was imported. A single shadcn Button that re-exports ButtonPrimary, ButtonGhost, ButtonLoading is an element. You expanded one thing into a vocabulary.

**Patterns** — two or more sources in, fewer exports out. The collapse is the signal: you’re combining parts into something specific and purposeful. A SearchBar that imports Input, Button, and Label and exports only SearchBar is a pattern. Three in, one out.

Each layer makes a specific promise about the files inside. A file in `elements/`

adds to a stable, reusable UI vocabulary. A file in `patterns/`

combines lower-layer pieces for a specific purpose.

Classification follows a count, not a judgment call, and dependencies only flow downward: nothing in core or elements imports from patterns.

*What this gives up.* Finding gets weaker. `elements/`

tells a user less at a glance than `forms/`

does. The names are precise but less evocative.

*What this gains.* Placement becomes unambiguous. You never debate which folder a component belongs in — you apply the rule.

| Finding (navigation) | Placing (classification) | |
|---|---|---|
| Role-based | High (names match mental categories) | Low (edges are fuzzy, shared/ fills the gap) |
| Layer-based | Low (names describe structure, not role) | High (rule is mechanical, no judgment needed) |

[Placement mistakes add up](#placement-mistakes-add-up)

A wrong guess at finding costs one look, once per file per developer. A wrong guess at placing stays: the component lands in the wrong folder, future developers follow the pattern, the misclassification becomes a convention, and refactoring it later costs more than getting it right early. In a codebase that grows, placement ambiguity compounds. Navigation ambiguity doesn’t.

Some people need to find and place files. Others only need to find them. They might just be looking for a `.md`

file near a component. The second group feels the cost of weaker finding without getting the benefit of clearer placement. Once the rule is learned, both groups can navigate the structure predictably, even if the names remain less obvious at a glance.

[Where to go from here](#where-to-go-from-here)

So the question to ask is not “which structure is better?” but rather “which friction dominates your context?”

For cross-functional teams, small codebases, early stage: finding matters more, and role-based is defensible. Where a shared component library exists or the team is growing: placing matters more, and layer-based pays off more clearly.

For any codebase expected to grow, the layer-based cost comes first (learning the rule) and the role-based cost comes later (refactoring accumulated misclassification), and most teams only feel the later one after it’s too late to fix cheaply.

When in doubt, **default to a deterministic rule** rather than a familiar taxonomy. That could mean a ruleset a script can check, or just a question you can answer through testing.

A good default should work broadly without requiring customization, while still leaving room to adapt it. It should not come optimized for a particular team or niche. You should not feel pressure to customize it on day one, and it should not be hard to evolve once the need arises.

Nothing stops you from treating it as a starting point and optimizing from there. Just stay above the floor it sets:

- two people given the same guidance and the same files still land on the same folder every time
- the people using the tree can still find things at least as quickly, with no more friction than under a sane default

[What AI changes, and what it doesn’t](#what-ai-changes-and-what-it-doesnt)

To be clear, **there is no quick answer** here, unless you can adopt something you already know has worked for a close-to-identical use case and team. AI can make the front-loaded work easier, but only after you have explored and clearly defined the use cases the structure needs to serve. AI doesn’t fix poor judgment. Good decisions still take time, and [garbage in, garbage out](https://en.wikipedia.org/wiki/Garbage_in,_garbage_out) still applies.

[Try the CE Pattern](#try-the-ce-pattern)

If your tree holds UI components, the CE Pattern folder structure and ruleset above are available as a [public agent skill](https://github.com/SterlingJF/ce-pattern-kit). It copies, configures, and records the provenance of the tooling in any target repository. After that, the vendored files are yours to maintain and make your own.

[References](#references)

- Furnas et al. (1987):
[The vocabulary problem in human-system communication](https://doi.org/10.1145/32206.32212) - Pirolli & Card (1999):
[Information foraging](https://doi.org/10.1037/0033-295X.106.4.643) - Page Laubheimer (2023):
[Tree testing: Evaluate menu labels and categories](https://www.nngroup.com/articles/tree-testing/) - Samhita Tankala & Katie Sherwin (2024):
[Card sorting: Uncover users’ mental models for better information architecture](https://www.nngroup.com/articles/card-sorting-definition/) - Rokhmad Setiawan (2025):
[Best practices for using shadcn/ui in Next.js](https://insight.akarinti.tech/best-practices-for-using-shadcn-ui-in-next-js-2134108553ae)
