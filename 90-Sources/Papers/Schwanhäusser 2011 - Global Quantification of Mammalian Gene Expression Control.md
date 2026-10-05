---
aliases:
  - Schwanhausser 2011
  - mRNA and protein turnover study
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Björn Schwanhäusser
  - Matthias Selbach
  - et al.
journal: Nature
year: 2011
url: "https://doi.org/10.1038/nature10098"
access: paid
---

# Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control

> [!abstract]
> The first genome-scale measurement of both abundance and turnover of mRNAs and proteins in the same mammalian cells, with a kinetic model of how much each step contributes to protein levels.

## Why this source

The authors measured absolute mRNA and protein abundance and turnover by parallel metabolic pulse labelling for more than 5,000 genes in mouse fibroblasts (NIH3T3). mRNA and protein levels correlated better than previously thought (a coefficient of determination of about 0.41), whereas mRNA and protein half-lives were not correlated. Fitting a model of synthesis and degradation for each gene, they concluded that protein abundance is predominantly controlled at the level of translation. It is the standard reference for the question "how well does mRNA predict protein?" in [[Gene Expression]].

## Coverage

Citation: Schwanhäusser B, Busse D, Li N, Dittmar G, Schuchhardt J, Wolf J, Chen W, Selbach M. "Global quantification of mammalian gene expression control". *Nature* 473(7347):337-342 (2011).

| Part | Content | Vault notes |
|---|---|---|
| Measurements | Abundance and half-lives of mRNAs and proteins, more than 5,000 genes, NIH3T3 cells | [[Gene Expression]], [[Proteomics]], [[RNA Sequencing]] |
| Correlations | mRNA versus protein levels (R² about 0.41); half-lives uncorrelated | [[Gene Expression]], [[Correlation]] |
| Model | Synthesis and degradation rates of mRNA and protein per gene | [[Ordinary Differential Equation]], [[Biochemical Kinetic Model]] |

Cited in [[Gene Expression]].

## How to use it

- L3: read the abstract and the figure comparing mRNA and protein levels; then read the reanalysis [[Li 2014 - System Wide Analyses Have Underestimated Protein Abundances]] before quoting the 0.41.

## Caveats

- A corrigendum (*Nature*, 2013) corrected a scaling error in the conversion of protein intensities into absolute copy numbers, after it was identified by Mark Biggin.
- A reanalysis argued that measurement error makes mRNA levels look less predictive than they are ([[Li 2014 - System Wide Analyses Have Underestimated Protein Abundances]]).
- One cell line in steady-state culture; other cell types and changing conditions can behave differently.
- Metadata (title, journal, volume, issue, pages, year), the abstract findings, the cell line and the R² verified in this pass; the full author list is given as usually cited.
