---
aliases:
  - AlphaFold 2 paper
  - AlphaFold2
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - domain/industry
  - level/L3
  - level/M1
kind: paper
tier: S
authors:
  - John Jumper
  - Richard Evans
  - et al.
  - Demis Hassabis
journal: Nature
year: 2021
url: "https://doi.org/10.1038/s41586-021-03819-2"
access: free
---

# Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold

> [!abstract]
> The DeepMind paper describing AlphaFold 2, the first computational method to predict protein structures regularly with atomic accuracy, even when no similar structure is known.

## Why this source

AlphaFold 2 was validated in the blind CASP14 assessment and changed structural biology: predicted models became accurate enough to use where experimental structures were missing. The paper describes a deep learning architecture that builds physical and biological knowledge about protein structure into the network and leverages multiple sequence alignments. It is also the reference result behind the "AI in biology" trend.

## Coverage

Citation: Jumper J, Evans R, et al. "Highly accurate protein structure prediction with AlphaFold". *Nature* 596:583-589 (2021). doi:10.1038/s41586-021-03819-2. Free at PMC8371605.

| Part | Content | Vault notes |
|---|---|---|
| Problem and benchmark | Structure prediction from sequence, CASP14 results | [[Protein Structure Prediction]] |
| Inputs | Multiple sequence alignments and templates | [[Multiple Sequence Alignment]] |
| Architecture | Evoformer blocks and a structure module producing atomic coordinates | [[AlphaFold]], [[Neural Network]] |
| Confidence | Per-residue confidence estimates reported with each model | [[Structure Model Quality Assessment]] |
| Impact | Structure prediction as a reference result for AI in biology | [[Artificial Intelligence in Biology]], [[AlphaFold Protein Structure Database]] |

Cited in [[Structural Bioinformatics]] and [[Innovation and Entrepreneurship]].

## How to use it

- M1: read the main text and figures for the architecture overview; the supplementary information holds the algorithmic detail.
- Explore predictions for proteins you know in the [[AlphaFold Protein Structure Database]] and compare the confidence scores with the experimental structures in the [[RCSB Protein Data Bank]].
- L3 in industry context: use it as the case study separating a benchmarked result (CASP14) from general claims about AI.

## Caveats

- Covers AlphaFold 2 for single protein chains; complexes and other molecules are handled by later versions described in separate papers.
- A predicted structure is a model: low-confidence regions are often disordered, and the method does not simulate folding dynamics.
- Metadata (authors, journal, volume, pages, DOI, PMC record) verified in this pass; issue number not checked.
