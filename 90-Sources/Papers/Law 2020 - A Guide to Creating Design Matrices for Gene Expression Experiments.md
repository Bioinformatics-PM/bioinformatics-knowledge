---
aliases:
  - Design matrices guide
  - RNAseq123 design matrices
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: B
authors:
  - Charity W. Law
  - Kathleen Zeglinski
  - Xueyi Dong
  - Monther Alhamdoosh
  - Gordon K. Smyth
  - Matthew E. Ritchie
journal: F1000Research
year: 2020
url: "https://doi.org/10.12688/f1000research.27893.1"
access: free
---

# Law 2020 - A Guide to Creating Design Matrices for Gene Expression Experiments

> [!abstract]
> A peer-reviewed tutorial on writing the design matrix and the contrast matrix of a differential expression analysis, from one factor to interactions, mixed effects and time series.

## Why this source

In a differential expression analysis, the biology is encoded twice: once in the design matrix, which sets up the linear model, and once in the contrasts, which state the comparisons of interest. Errors there silently answer the wrong question. This guide works through common experimental layouts with code and graphics, which makes it the practical companion of [[Design Matrix]].

## Coverage

Citation: Law CW, Zeglinski K, Dong X, Alhamdoosh M, Smyth GK, Ritchie ME. "A guide to creating design matrices for gene expression experiments". *F1000Research* 9:1444 (2020), version 1. doi:10.12688/f1000research.27893.1. Free full text at PMC7873980.

| Part | Content | Vault notes |
|---|---|---|
| Design and contrast matrices | Design matrices set up the linear model of the analysis; contrast matrices specify the comparisons | [[Design Matrix]], [[Linear Contrast]] |
| Models | From models with a single explanatory variable to several variables, interactions, mixed effects and time series, with code and graphics | [[Dummy Variable]], [[Interaction Effect]], [[Linear Mixed Model]] |
| Scope | Written for a limma-style pipeline; much of it applies to other differential expression packages | [[Differential Expression Analysis]], [[Bioconductor]] |

## How to use it

- L2: read the single-factor and two-factor sections with [[Design Matrix]] open, and rebuild each matrix by hand.
- L3: the interaction, mixed-effects and time-series sections, before designing a real RNA-seq analysis.

## Caveats

- Verified in this pass (web search): authors, title, journal, volume, article number, version, publication date (10 December 2020), DOI, PMC identifier and the scope summarized above. Section titles and the terminology used inside were not checked.
- Code is in R; the matrices themselves are language-independent.
