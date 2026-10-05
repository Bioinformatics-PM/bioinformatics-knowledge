# Bioinformatics Knowledge

A structured, self-directed curriculum covering the biological, mathematical, statistical and computational foundations of bioinformatics, from first-year university level (L1) to the Master's core (M1). It is an [Obsidian](https://obsidian.md) vault: open this repository as a vault.

> **Learn the scientific concept. Implement it. Apply it to a real biological problem.**

## What is inside

| Folder | Content |
|---|---|
| `00-System/` | Start page, curriculum, conventions, dashboards |
| `01-Biology/` … `09-Industry-and-Innovation/` | Nine domains, each split into subdomains with a syllabus (MOC) and concept notes |
| `70-Exercises/` | Problem sets |
| `80-Projects/` | The code projects of the companion [Bioinformatics Lab](https://github.com/Bioinformatics-PM) |
| `90-Sources/` | Every source: university courses (MIT, Harvard, Stanford, EMBL-EBI, France, China…), textbooks, landmark papers, databases |
| `98-Assets/` | Diagrams |
| `99-Templates/` | Note templates |

Start with [`00-System/Home.md`](00-System/Home.md), then [`00-System/Curriculum.md`](00-System/Curriculum.md).

## How it is built

- **One concept, one note**, written once and deepened from L1 to L3.
- **Everything is sourced**, from tiered academic sources (see [`00-System/Conventions.md`](00-System/Conventions.md)).
- **Theory is bridged to code**: every concept note has a mathematical and a computational representation, and links to the Lab project that implements it.
- **Progress is measurable**: each note has a `mastery` level from 0 (unseen) to 5 (can teach it).
- **Clean by construction**: controlled tag vocabulary and properties, checked in CI by [`scripts/lint_vault.py`](scripts/lint_vault.py).

## Domains

Biology · Chemistry · Physics · Mathematics · Probability and Statistics · Computer Science · Bioinformatics · Scientific Practice · Industry and Innovation

## Contributing workflow

Work on `dev`, open pull requests to `main`, run `python scripts/lint_vault.py` before committing (requires `pyyaml`).

## License

Text and diagrams: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code snippets and scripts: MIT.
