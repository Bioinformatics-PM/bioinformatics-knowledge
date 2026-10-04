---
aliases:
  - Quantile normalization paper
  - Bolstad et al. 2003
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Benjamin M. Bolstad
  - Rafael A. Irizarry
  - Magnus Åstrand
  - Terence P. Speed
journal: Bioinformatics
year: 2003
url: "https://doi.org/10.1093/bioinformatics/19.2.185"
access: paid
---

# Bolstad 2003 - A Comparison of Normalization Methods for High Density Oligonucleotide Array Data

> [!abstract]
> The paper that compared probe-level normalization methods for Affymetrix-type arrays and popularized quantile normalization, which gives every array the same distribution of intensities.

## Why this source

It is the standard reference for quantile normalization. The authors compared three "complete data" methods, which use all arrays of an experiment to define the normalizing relation, with two methods that normalize each array against a baseline array (a one-number scaling and a non-linear method), judging them by the variance and bias of the resulting expression measures. The simplest and quickest complete-data method, quantile normalization, performed favorably, and the three complete-data methods were made available in the Bioconductor package affy.

## Coverage

Citation: Bolstad BM, Irizarry RA, Åstrand M, Speed TP. "A comparison of normalization methods for high density oligonucleotide array data based on variance and bias". *Bioinformatics* 19(2):185-193 (2003). doi:10.1093/bioinformatics/19.2.185. PubMed 12538238.

| Part | Content | Vault notes |
|---|---|---|
| Methods | Complete-data methods (including quantile normalization) versus baseline-array methods | [[Quantile]], [[Count Normalization]] |
| Evaluation | Variance and bias of expression measures after normalization | [[Microarray]] |
| Software | Implementation in the Bioconductor affy package | [[Bioconductor]] |

Cited in [[Quantile]].

## How to use it

- L2: read the description of quantile normalization after [[Quantile]].
- L3: read the comparison when studying normalization of high-throughput data ([[Transcriptomics]]).

## Caveats

- Written for oligonucleotide microarrays at the probe level; using quantile normalization on other data types (RNA-seq, proteomics) assumes that global distribution differences are technical.
- Verified in this pass: title, authors, journal, volume, pages, DOI, PubMed identifier and the abstract (method classes, the favorable performance of the simplest complete-data method, availability in affy). Open-access status not verified.
