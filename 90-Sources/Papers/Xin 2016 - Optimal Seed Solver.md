---
aliases:
  - Optimal Seed Solver
  - OSS
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Hongyi Xin
  - Sunny Nahar
  - Richard Zhu
  - John Emmons
  - Gennady Pekhimenko
  - Carl Kingsford
  - Can Alkan
  - Onur Mutlu
journal: Bioinformatics
year: 2016
url: "https://doi.org/10.1093/bioinformatics/btv670"
access: free
---

# Xin 2016 - Optimal Seed Solver

> [!abstract]
> A read-mapping paper that states the pigeonhole argument behind seeds (to tolerate $e$ errors, cut a read into $e + 1$ seeds, one of which is error-free) and then optimizes where to cut.

## Why this source

States the seed pigeonhole argument explicitly in a read-mapping setting, and explains the trade-off it creates: the number of non-overlapping seeds sets sensitivity, their total frequency in the reference sets speed.

## Coverage

Citation: Xin H, Nahar S, Zhu R, Emmons J, Pekhimenko G, Kingsford C, Alkan C, Mutlu O. "Optimal seed solver: optimizing seed selection in read mapping". *Bioinformatics* 32(11):1632-1642 (2016; online 2015). doi:10.1093/bioinformatics/btv670. Preprint: arXiv:1506.08235.

| Part | Content | Vault notes |
|---|---|---|
| Background | $e + 1$ non-overlapping seeds, at least one error-free by the pigeonhole principle | [[Pigeonhole Principle]], [[Seed and Extend]], [[Read Mapping]] |
| Method | Dynamic programming that chooses the seeds with the lowest total frequency | [[Dynamic Programming]] |

Cited in [[Pigeonhole Principle]].

## How to use it

- L2: read the introduction and background with [[Pigeonhole Principle]].
- L3: the optimization, as an example of dynamic programming on a read.

## Caveats

- Focused on hash-table-based short-read mappers; long-read and FM-index mappers choose seeds differently ([[Minimizer]], [[Spaced Seed]]).
- Verified in this pass: authors, title, journal, volume, issue, pages, DOI, arXiv preprint, and the background statements quoted above.
