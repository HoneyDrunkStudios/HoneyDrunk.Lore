# AI for Science and Chemistry

## Decision-useful summary
Anthropic's June 2026 chemistry work suggests frontier multimodal/reasoning models are beginning to help with chemists' translation and analysis work across structures, spectra, literature, and machine-readable notations. The strongest current evidence is narrow: Claude Opus 4.7 was competitive with ChemDraw and MestReNova on a small NMR prediction/evaluation set and could perform limited 1D inverse structure elucidation. Treat this as a domain-eval signal, not as autonomous lab capability. [source: raw/2026-06-09-web-making-claude-a-chemist.md]

## Claims
- Anthropic frames chemistry assistance as translation/integration across hand-drawn structures, instrument outputs, SMILES/database notation, patents, papers, methods sections, and supporting information. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-making-claude-a-chemist.md]
- In Anthropic's NMR white-paper summary, Opus 4.7 was the strongest Claude model on forward 1D NMR prediction across 20 compounds and was competitive with ChemDraw/MestReNova on average. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-making-claude-a-chemist.md]
- Opus 4.7 also performed inverse structure elucidation on 15 tasks, recovering all eight simpler structures across three attempts and recovering most harder hinted structures across repeated attempts. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-making-claude-a-chemist.md]
- The evaluation limitations are material: 20 forward compounds, 15 inverse tasks, only selected scaffold families and solvents, no 2D NMR/stereochemistry scope, and harder inverse tasks needed starting-material hints. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-making-claude-a-chemist.md]

## Typed entities
- organization: Anthropic
- program: AI for Science
- person: David Kamber
- model: Claude Opus 4.7
- model: Claude Opus 4.6
- model: Claude Sonnet 4.6
- software: ChemDraw
- software: MestReNova
- technique: NMR spectroscopy
- notation: SMILES
- task: forward NMR prediction
- task: inverse structure elucidation
- repository/source type: ChemRxiv preprint

## Explicit relationships
- Claude chemistry assistance uses multimodal reading, chemical notation, literature understanding, and reasoning to complement chemist judgment.
- Forward NMR prediction compares model/tool predicted peaks against experimental spectra.
- Inverse structure elucidation uses molecular formula plus NMR spectra, and sometimes starting-material context, to propose structures.
- Small-scaffold chemistry evals do not supersede expert chemist review or dedicated cheminformatics/lab validation.

## HoneyDrunk implications
- Keep AI-for-science claims out of production decision support unless the domain task has holdout evals, expert review, and traceable source data.
- If HoneyDrunk ever evaluates scientific/chemical AI workflows, require explicit scope limits, input provenance, confidence notes, and human expert signoff.

## Confidence and quality notes
- Quality posture: early domain-eval signal; decision-useful for scouting only.
- Privacy filter: no private lab data or unsafe procedural synthesis details were copied.
