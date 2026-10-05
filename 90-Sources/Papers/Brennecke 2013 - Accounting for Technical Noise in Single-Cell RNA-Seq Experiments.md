---
aliases:
  - Brennecke et al. 2013
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L3
kind: paper
tier: A
authors:
  - Philip Brennecke
  - Simon Anders
  - Marcus G. Heisler
journal: Nature Methods
year: 2013
url: "https://doi.org/10.1038/nmeth.2645"
access: partial
---

# Brennecke 2013 - Accounting for Technical Noise in Single-Cell RNA-Seq Experiments

> [!abstract]
> A method to tell genuine cell-to-cell variability of gene expression from the strong technical noise of single-cell RNA-seq, by comparing each gene's squared coefficient of variation with the noise expected at its mean, estimated from spike-ins.

## Why this source

Single-cell counts are noisy, and the noise of a gene depends mainly on its average read count. The authors normalize for library size, compute each gene's mean and squared coefficient of variation ($CV^2$, variance over squared mean), fit the technical $CV^2$-mean relationship from spike-in controls, and test which genes vary more than technical noise predicts. It is a founding reference for the selection of highly variable genes.

## Coverage

Citation: Brennecke P, Anders S, et al., Heisler MG (last author). "Accounting for technical noise in single-cell RNA-seq experiments". *Nature Methods* 10:1093-1095 (2013). doi:10.1038/nmeth.2645.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Technical noise in single-cell RNA-seq, dependent on mean expression | [[Single-Cell RNA Sequencing]], [[Measure of Dispersion]] |
| Method | $CV^2$ against mean, technical noise fitted on spike-ins, gene-wise test for excess variability | [[Highly Variable Gene]], [[Measure of Dispersion#Advanced (L3)]] |

## How to use it

- L3: read it with [[Highly Variable Gene]], after [[Measure of Dispersion]] and [[Variance]].

## Caveats

- Paywalled at the journal; an author copy is hosted on the Huber group website.
- Verified in this pass: title, journal, volume, pages, year, DOI, and the use of $CV^2$ against the mean with spike-in-based technical noise. Only the first, second and last authors are listed here; the middle authors were not checked name by name.
