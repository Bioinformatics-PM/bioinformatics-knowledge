---
aliases:
  - Batch effects review
tags:
  - type/source
  - domain/scientific-practice
  - domain/bioinformatics
  - domain/statistics
  - level/L3
kind: paper
tier: A
authors:
  - Jeffrey T. Leek
  - Robert B. Scharpf
  - Héctor Corrada Bravo
  - David Simcha
  - Benjamin Langmead
  - W. Evan Johnson
  - Donald Geman
  - Keith Baggerly
  - Rafael A. Irizarry
journal: Nature Reviews Genetics
year: 2010
url: "https://doi.org/10.1038/nrg2825"
access: free
---

# Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects

> [!abstract]
> A review showing that batch effects are widespread in high-throughput data and can drive false conclusions, with advice on design, detection and correction.

## Why this source

Measurements in genomics are affected by laboratory conditions, reagent lots, personnel and processing dates. When these batches line up with the biological groups, technical variation masquerades as biology. The authors, biostatisticians behind widely used genomics tools, show the problem across technologies and explain how to detect it and how good design prevents it.

## Coverage

Citation: Leek JT, Scharpf RB, Corrada Bravo H, Simcha D, Langmead B, Johnson WE, Geman D, Baggerly K, Irizarry RA. "Tackling the widespread and critical impact of batch effects in high-throughput data". *Nature Reviews Genetics* 11(10):733-739 (2010). doi:10.1038/nrg2825. Author manuscript free at PMC3880143.

| Part | Content | Vault notes |
|---|---|---|
| The problem | Sources of batch effects and their confounding with outcomes | [[Batch Effect]], [[Confounding]] |
| Detection | Exploratory analysis to reveal batch structure | [[Principal Component Analysis]] |
| Correction | Statistical adjustment when batches cannot be avoided | [[Batch Effect Correction]] |
| Design | Randomization and balanced processing to prevent confounding | [[Randomized Block Design]], [[Randomization]], [[Sequencing Experiment Design]] |

Cited in [[Experimental Design]].

## How to use it

- L3: read it for item 15 of [[Experimental Design]]; then color a PCA plot of a public expression dataset by processing date and by condition.
- Read the design recommendations before planning any sequencing experiment.

## Caveats

- Correction methods have developed since 2010, especially for single-cell data; the design principles have not changed.
- Correction cannot rescue a design where batch and condition are completely confounded.
- Metadata (authors, journal, volume, issue, pages, DOI) verified in this pass.
