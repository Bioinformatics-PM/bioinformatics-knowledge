---
aliases:
  - Luecken and Theis 2019
  - scRNA-seq best practices
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: B
authors:
  - Malte D. Luecken
  - Fabian J. Theis
journal: Molecular Systems Biology
year: 2019
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6582955/"
access: free
---

# Luecken 2019 - Current Best Practices in Single-Cell RNA-Seq Analysis - A Tutorial

> [!abstract]
> A peer-reviewed tutorial that walks through the steps of a typical single-cell RNA-seq analysis, from quality control to cell- and gene-level downstream analysis, with recommendations for each step.

## Why this source

It is the most widely used map of the single-cell workflow for newcomers, written by a leading single-cell group, and it comes with a case-study repository. It explains why each step exists, which makes it the right citation when a biology note needs to say how a cellular state shows up in single-cell data.

## Coverage

Citation: Luecken MD, Theis FJ. "Current best practices in single-cell RNA-seq analysis: a tutorial". *Molecular Systems Biology* 15(6):e8746 (2019). doi:10.15252/msb.20188746. PMC6582955.

| Part | Content | Vault notes |
|---|---|---|
| Pre-processing | Quality control, normalization, data correction, feature selection, dimensionality reduction | [[Single-Cell Quality Control]], [[Single-Cell Normalization]], [[Dimensionality Reduction]] |
| Quality control | Cells with few detected genes and a high fraction of mitochondrial counts can be cells whose cytoplasmic mRNA leaked out through a broken membrane; a high mitochondrial fraction can also be biological (for example high respiration), so thresholds need care | [[Single-Cell Quality Control]], [[Apoptosis]] |
| Downstream analysis | Cell-level and gene-level analyses after pre-processing | [[Single-Cell Clustering]], [[Differential Expression Analysis]] |

## How to use it

- **L3**: read the quality-control section before filtering any single-cell data set, and follow the case study once.
- **M1**: use it as a checklist when reviewing a single-cell analysis: which step, which tool, which parameters were justified.

## Caveats

- Single-cell methods move fast; tools recommended in 2019 may have been superseded. The authors maintain an updated online book of best practices (not reviewed here).
- Verified in this pass (web search): the citation, DOI, PMC number and the scope of the abstract. The quality-control statements were verified through excerpts of a case-study notebook that reproduces the tutorial's wording, not through the full text; downstream sections were not read.
