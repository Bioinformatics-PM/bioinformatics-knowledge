---
aliases:
  - DESeq paper
  - Anders and Huber 2010
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L1
  - level/L3
kind: paper
tier: A
authors:
  - Simon Anders
  - Wolfgang Huber
journal: Genome Biology
year: 2010
url: "https://doi.org/10.1186/gb-2010-11-10-r106"
access: free
---

# Anders 2010 - Differential Expression Analysis for Sequence Count Data

> [!abstract]
> The paper that introduced DESeq: a negative binomial model for RNA-seq and other sequencing count data, with the variance linked to the mean by local regression, and sample depths estimated by the median-of-ratios size factors.

## Why this source

It is the primary reference for the median-of-ratios normalization. Each sample's size factor is the median, over genes, of the ratio of its count to a pseudo-reference sample made of the per-gene geometric means across samples. The authors motivate it by the unreliability of total read counts as a measure of depth, which a few highly and differentially expressed genes can dominate, and argue that the median remains a reasonable estimate as long as no more than half of the genes are differentially expressed.

## Coverage

Citation: Anders S, Huber W. "Differential expression analysis for sequence count data". *Genome Biology* 11(10):R106 (2010). doi:10.1186/gb-2010-11-10-r106. PMID 20979621, free full text at PMC3218662.

| Part | Content | Vault notes |
|---|---|---|
| Normalization | Size factors as the median of count ratios to the per-gene geometric mean | [[Measure of Central Tendency]], [[Size Factor Estimation]], [[Count Normalization]] |
| Model | Negative binomial counts, variance linked to the mean by local regression | [[Negative Binomial Distribution]], [[Overdispersion]], [[Differential Expression Analysis]] |
| Software | The DESeq package for R/Bioconductor | [[Bioconductor]] |

## How to use it

- L1: read the size-factor paragraph of the methods with [[Measure of Central Tendency#Advanced (L3)]]; it needs only medians and geometric means.
- L3: read the whole paper with [[Differential Expression Analysis]], after [[Variance]] and [[Overdispersion]].

## Caveats

- Describes the original DESeq package; check the documentation of the package version actually used, whose defaults may differ.
- Verified in this pass: authors, title, journal, volume, issue, article number, year, PMID and PMCID; the description of the size-factor estimator (median of ratios to a geometric-mean pseudo-reference) and its motivation.
