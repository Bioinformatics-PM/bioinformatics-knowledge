---
aliases:
  - edgeR paper
  - Robinson, McCarthy and Smyth 2010
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Mark D. Robinson
  - Davis J. McCarthy
  - Gordon K. Smyth
journal: Bioinformatics
year: 2010
url: "https://doi.org/10.1093/bioinformatics/btp616"
access: free
---

# Robinson 2010 - edgeR - A Bioconductor Package for Differential Expression Analysis of Digital Gene Expression Data

> [!abstract]
> The application note introducing edgeR: differential expression testing for replicated count data with an overdispersed Poisson model, whose degree of overdispersion is moderated across genes by empirical Bayes methods.

## Why this source

It is the primary reference for edgeR, a count-based differential expression tool used alongside DESeq ([[Anders 2010 - Differential Expression Analysis for Sequence Count Data]], [[Love 2014 - Moderated Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2]]). Its abstract states the key idea in a few lines: count data carry both biological and technical variation, captured by an overdispersed Poisson model, and borrowing information across transcripts (empirical Bayes moderation) makes the overdispersion estimable even with minimal replication.

## Coverage

Citation: Robinson MD, McCarthy DJ, Smyth GK. "edgeR: a Bioconductor package for differential expression analysis of digital gene expression data". *Bioinformatics* 26(1):139-140 (2010). doi:10.1093/bioinformatics/btp616. PMID 19910308; free full text at PMC2796818.

| Part | Content | Vault notes |
|---|---|---|
| Model | Overdispersed Poisson model of replicated count data, accounting for biological and technical variability | [[Negative Binomial Distribution]], [[Overdispersion]] |
| Moderation | Empirical Bayes methods moderate the degree of overdispersion across transcripts | [[Empirical Bayes]] |
| Replication | Usable with minimal replication, provided at least one condition is replicated | [[Experimental Design]] |
| Software | Bioconductor package, free under the LGPL | [[Bioconductor]], [[Differential Expression Analysis]] |

## How to use it

- L3: read the abstract and the short description with [[Negative Binomial Distribution]]; then follow the edgeR user's guide on a public dataset.
- M1: compare edgeR's moderated dispersions with DESeq2's on the same data, and relate both to [[Empirical Bayes]].

## Caveats

- A two-page application note: statistical details are in the methodological papers it cites and in the package documentation.
- The package has grown since 2010 (generalized linear models, other tests); a later Bioconductor vignette describes the method as empirical Bayes estimation with exact tests based on the negative binomial distribution.
- Verified in this pass: authors, title, journal, volume, issue, pages, year, DOI, PMID, PMC identifier, and the abstract's claims (overdispersed Poisson model, empirical Bayes moderation across transcripts, minimal replication, LGPL licence).
