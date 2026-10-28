---
aliases:
  - GOseq paper
  - Young et al. 2010
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - M. D. Young
  - M. J. Wakefield
  - Gordon K. Smyth
  - A. Oshlack
journal: Genome Biology
year: 2010
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC2872874"
access: free
---

# Young 2010 - Gene Ontology Analysis for RNA-Seq - Accounting for Selection Bias

> [!abstract]
> The paper introducing GOseq: Gene Ontology enrichment for RNA-seq that corrects the bias caused by the easier detection of differential expression in long and highly expressed transcripts.

## Why this source

Standard enrichment tests assume that every gene has the same chance of being called differentially expressed. The paper shows that this fails for RNA-seq: differential expression is over-detected in long and highly expressed transcripts, so standard GO methods give biased results. GOseq weights each gene by a probability of selection that depends on its length; applied to a prostate cancer dataset, the correction changed the results noticeably, with categories that fit the known biology better. It is the reference for selection bias in [[Over-Representation Analysis]].

## Coverage

Citation: Young MD, Wakefield MJ, Smyth GK, Oshlack A. "Gene ontology analysis for RNA-seq: accounting for selection bias". *Genome Biology* 11(2):R14 (2010). Free full text at PMC2872874.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Over-detection of differential expression in long and highly expressed transcripts biases GO analysis | [[Over-Representation Analysis]], [[Differential Expression Analysis]] |
| Method | GOseq: probability weighting of genes by length; null distribution of category counts approximated by Wallenius' noncentral hypergeometric distribution (default method) | [[Hypergeometric Distribution]], [[Gene Ontology Annotation]] |
| Application | Prostate cancer RNA-seq dataset | [[RNA Sequencing]] |
| Software | The goseq package for R/Bioconductor | [[Bioconductor]] |

## How to use it

- L3: read the introduction and the description of length bias with [[Hypergeometric Distribution]] open.
- M1: run goseq and a standard hypergeometric test on the same gene list, and compare the categories that change.

## Caveats

- Verified in this pass: authors (surnames and initials), title, journal, volume, issue, article number, year, PMC identifier, and the abstract (length and expression bias, prostate cancer application). The Wallenius approximation as the default method comes from the goseq package documentation, which notes that it assumes genes within a category share one selection probability; the article's methods were not read.
