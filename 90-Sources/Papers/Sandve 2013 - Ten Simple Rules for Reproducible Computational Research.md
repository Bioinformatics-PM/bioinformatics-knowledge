---
aliases: []
tags:
  - type/source
  - domain/scientific-practice
  - domain/computer-science
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Geir Kjetil Sandve
  - Anton Nekrutenko
  - James Taylor
  - Eivind Hovig
journal: PLoS Computational Biology
year: 2013
url: "https://doi.org/10.1371/journal.pcbi.1003285"
access: free
---

# Sandve 2013 - Ten Simple Rules for Reproducible Computational Research

> [!abstract]
> Ten short, practical rules that make a computational analysis reproducible, from tracking how every result was produced to publishing scripts and runs.

## Why this source

Short, concrete and written by bioinformaticians (two of the authors led Galaxy), it turns reproducibility into habits you can adopt on your first project. Every rule maps to a tool or practice taught elsewhere in the vault, which makes it the best checklist for the Lab repositories.

## Coverage

Citation: Sandve GK, Nekrutenko A, Taylor J, Hovig E. "Ten Simple Rules for Reproducible Computational Research". *PLoS Computational Biology* 9(10):e1003285 (2013). doi:10.1371/journal.pcbi.1003285. Free at PMC3812051.

| Rules | Content | Vault notes |
|---|---|---|
| 1, 2 | Keep track of how every result was produced; avoid manual data manipulation | [[Data Provenance]], [[Workflow Management System]] |
| 3, 4 | Archive exact versions of external programs; version control all custom scripts | [[Dependency Management]], [[Version Control]] |
| 5, 7 | Record intermediate results in standard formats; store raw data behind plots | [[Computational Reproducibility]] |
| 6 | Note the random seeds of analyses that include randomness | [[Random Number Generation]] |
| 8, 9 | Hierarchical output; connect textual statements to underlying results | [[Research Compendium]] |
| 10 | Provide public access to scripts, runs and results | [[Open Science]] |

Cited in [[Reproducibility]].

## How to use it

- L2: turn the ten rules into a checklist in the README of each Lab repository; start with rules 4 and 6 in [[07-evolution-simulator]].
- L3: audit [[10-genomic-pipeline]] against all ten rules.

## Caveats

- Rules, not tools: it predates the wide use of containers and modern workflow managers, which now implement several rules.
- Metadata (authors, journal, volume, article number, DOI, PMC record) verified in this pass.
