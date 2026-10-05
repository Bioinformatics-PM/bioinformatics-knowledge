---
aliases:
  - Zuker algorithm paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - domain/computer-science
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Michael Zuker
  - Patrick Stiegler
journal: Nucleic Acids Research
year: 1981
url: "https://doi.org/10.1093/nar/9.1.133"
access: free
---

# Zuker 1981 - Optimal Computer Folding of Large RNA Sequences

> [!abstract]
> The dynamic programming algorithm that finds the minimum free energy secondary structure of an RNA from thermodynamic parameters.

## Why this source

It brought an efficient dynamic programming method into RNA folding: using published stacking and destabilizing energies, it computes the structure of minimum free energy over all nested base-pairing patterns, faster and for larger molecules than earlier procedures. It also showed how to add auxiliary information such as chemical reactivity and enzyme susceptibility data. Modern folding tools descend from it.

## Coverage

Citation: Zuker M, Stiegler P. "Optimal computer folding of large RNA sequences using thermodynamics and auxiliary information". *Nucleic Acids Research* 9(1):133-148 (1981). doi:10.1093/nar/9.1.133. Free at PMC326673.

| Part | Content | Vault notes |
|---|---|---|
| Energy model | Stacking and destabilizing energies of loops | [[RNA Secondary Structure]] |
| Algorithm | Dynamic programming over nested structures to minimize free energy | [[RNA Secondary Structure Prediction]], [[Dynamic Programming]] |
| Application | Folding a 459-nucleotide immunoglobulin mRNA fragment | [[Messenger RNA]] |
| Auxiliary information | Constraining the fold with experimental data | [[RNA Secondary Structure Prediction]] |

Cited in [[RNA]].

## How to use it

- L2: implement the simpler [[Nussinov Algorithm]] (maximize base pairs) first, as in Exercise 5 of [[RNA]].
- L3: then read the recurrences here and see what changes when you minimize energy instead of maximizing pairs.

## Caveats

- Energy parameters from 1981 are obsolete; current tools use updated nearest-neighbor parameters.
- Pseudoknots are excluded by the nested-structure assumption.
- Metadata (authors, journal, volume, issue, pages, DOI, PMC record) verified in this pass.
