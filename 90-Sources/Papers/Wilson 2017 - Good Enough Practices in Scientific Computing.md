---
aliases:
  - Good Enough Practices
tags:
  - type/source
  - domain/scientific-practice
  - domain/computer-science
  - level/L1
  - level/L2
kind: paper
tier: S
authors:
  - Greg Wilson
  - Jennifer Bryan
  - Karen Cranston
  - Justin Kitzes
  - Lex Nederbragt
  - Tracy K. Teal
journal: PLoS Computational Biology
year: 2017
url: "https://doi.org/10.1371/journal.pcbi.1005510"
access: free
---

# Wilson 2017 - Good Enough Practices in Scientific Computing

> [!abstract]
> A minimal set of computing practices that every researcher can adopt, covering data management, programming, collaboration, project organization, tracking changes and writing manuscripts.

## Why this source

It complements [[Wilson 2014 - Best Practices for Scientific Computing]] with what a beginner can apply on day one, and it is explicit about the limits of tools, in particular what should **not** go into version control. Written by experienced Software and Data Carpentry instructors.

## Coverage

Citation: Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK. "Good enough practices in scientific computing". *PLoS Computational Biology* 13(6):e1005510 (2017). doi:10.1371/journal.pcbi.1005510. Free at PMC5480810; preprint arXiv:1609.00037.

| Part | Content | Vault notes |
|---|---|---|
| Keeping track of changes, "What not to put under version control" | Version control is optimized for text; binary files (word-processor files, PDFs) can be stored but their changes cannot be pinpointed; raw data should not change, so it needs no version tracking; intermediate files need none if they can be regenerated; version control systems are not designed for large files (benchmark: GitHub's 100 MB limit per file) | [[Version Control]] |
| Data management, software, collaboration, project organization | Practices for each area of a research project | [[Computational Reproducibility]], [[Research Compendium]] |

Cited in [[Version Control]].

## How to use it

- L1: read the "Keeping track of changes" section before creating the first Lab repository, and decide where the data of each project will live.
- L2: use the whole paper as a checklist when starting [[10-genomic-pipeline]].

## Caveats

- Deliberately minimal ("good enough"): it does not cover testing frameworks, packaging or continuous integration in depth.
- Platform limits quoted in the paper (GitHub file size) are those of 2017.
- Verified in this pass: authors, journal, publication date (22 June 2017), DOI, PMC and arXiv records, and the content of "What not to put under version control" summarized above. Other sections are described by topic only.
