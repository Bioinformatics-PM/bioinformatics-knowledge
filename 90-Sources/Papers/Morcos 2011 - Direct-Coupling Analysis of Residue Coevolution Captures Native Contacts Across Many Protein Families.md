---
aliases:
  - Morcos 2011
  - mfDCA paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/physics
  - domain/biology
  - level/M1
kind: paper
tier: S
authors:
  - Faruck Morcos
journal: Proceedings of the National Academy of Sciences
year: 2011
url: "https://doi.org/10.1073/pnas.1111471108"
access: free
---

# Morcos 2011 - Direct-Coupling Analysis of Residue Coevolution Captures Native Contacts Across Many Protein Families

> [!abstract]
> A fast direct-coupling analysis (DCA) that separates direct from indirect correlations between alignment columns and predicts residue contacts from sequences alone, across many protein families.

## Why this source

A fast implementation of coevolution-based contact prediction, evaluated across many protein families: a statistical-physics model of a multiple sequence alignment, the multi-state descendant of the [[Ising Model]], applied to structural bioinformatics ([[Coevolution]], [[Contact Map]]).

## Coverage

Citation: Morcos F and colleagues. "Direct-coupling analysis of residue coevolution captures native contacts across many protein families". *PNAS* 108(49):E1293-E1301 (2011). doi:10.1073/pnas.1111471108. Free at PMC3241805.

| Part | Content | Vault notes |
|---|---|---|
| Input | A multiple sequence alignment over a 21-letter alphabet (20 amino acids and the gap), summarized by single-site and pair frequencies | [[Multiple Sequence Alignment]] |
| Method | A fast implementation of DCA, which disentangles direct residue-residue couplings from indirect correlations | [[Direct Coupling Analysis]], [[Ising Model]] |
| Results | Predicted couplings recapitulate the contact map for the majority of the domains examined; further signals reflect alternative conformations, ligand-mediated couplings and interdomain contacts in oligomers | [[Protein Structure Prediction]] |

## How to use it

- M1: read with [[Direct Coupling Analysis]], after [[Ising Model]] and [[Boltzmann Distribution]] (maximum entropy).

## Caveats

- Co-authors are not listed here; the author list was not re-checked in this pass.
- Verified in this pass by web search: journal, volume, issue, pages, year, DOI, PMC record and the abstract-level findings above.
