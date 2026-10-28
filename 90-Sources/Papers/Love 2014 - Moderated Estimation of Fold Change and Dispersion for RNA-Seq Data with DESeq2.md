---
aliases:
  - DESeq2 paper
  - Love, Huber and Anders 2014
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Michael I. Love
  - Wolfgang Huber
  - Simon Anders
journal: Genome Biology
year: 2014
url: "https://doi.org/10.1186/s13059-014-0550-8"
access: free
---

# Love 2014 - Moderated Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2

> [!abstract]
> The paper describing DESeq2: a negative binomial generalized linear model for the read counts of each gene, with shrinkage estimation of dispersions and fold changes to stabilize estimates from few replicates.

## Why this source

It is the primary reference for DESeq2, the successor of DESeq ([[Anders 2010 - Differential Expression Analysis for Sequence Count Data]]). It states the count model used in practice: the count of gene $i$ in sample $j$ is negative binomial with mean $\mu_{ij} = s_j q_{ij}$ (a sample size factor times a quantity proportional to the true fragment concentration) and a gene-specific dispersion $\alpha_i$, with $\log_2 q_{ij}$ linear in the design. Its abstract presents shrinkage of dispersions and fold changes as the way to make estimates stable and interpretable, so that the analysis can focus on the strength of differential expression rather than its mere presence.

## Coverage

Citation: Love MI, Huber W, Anders S. "Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2". *Genome Biology* 15(12):550 (2014). doi:10.1186/s13059-014-0550-8. Free full text at PMC4302049; a bioRxiv preprint with the same title was posted on 19 February 2014.

| Part | Content | Vault notes |
|---|---|---|
| Model | Per-gene negative binomial GLM: $K_{ij} \sim \mathrm{NB}(\mu_{ij}, \alpha_i)$, $\mu_{ij} = s_j q_{ij}$, $\log_2 q_{ij} = x_j \cdot \beta_i$; variance $\mu + \alpha\mu^2$ | [[Negative Binomial Distribution]], [[Generalized Linear Model]], [[Size Factor Estimation]] |
| Shrinkage | Moderated estimates of dispersions and log fold changes, sharing information across genes | [[Empirical Bayes]], [[Overdispersion]] |
| Testing | Wald tests of the model coefficients | [[Differential Expression Analysis]], [[Hypothesis Testing]] |
| Software | The DESeq2 package for R/Bioconductor | [[Bioconductor]] |

## How to use it

- L3: read the model description with [[Negative Binomial Distribution]] open, then run the package vignette on a public dataset and plot the fitted dispersions against the mean counts.
- M1: read the shrinkage sections with [[Empirical Bayes]], and compare shrunken and unshrunken fold changes for weakly and strongly expressed genes.

## Caveats

- The package evolves: check the documentation of the version actually used, whose defaults may differ from the paper.
- Verified in this pass: authors, title, journal, volume, issue, article number, year, DOI, PMC identifier, preprint date, and the abstract's description (shrinkage estimation of dispersions and fold changes). The model formulas, the variance $\mu + \alpha\mu^2$ and the Wald test were checked in the DESeq2 package documentation and Bioconductor support pages, not in the article's methods section.
