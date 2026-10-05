---
aliases:
  - Nielsen et al. 2011
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Rasmus Nielsen
  - Joshua S. Paul
  - Anders Albrechtsen
  - Yun S. Song
journal: Nature Reviews Genetics
year: 2011
url: "https://pubmed.ncbi.nlm.nih.gov/21587300/"
access: free
---

# Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data

> [!abstract]
> A review of the statistical methods that turn aligned sequencing reads into SNP and genotype calls, and of how they quantify the uncertainty of each call.

## Why this source

The standard entry point to probabilistic genotype calling: it explains why counting reads with fixed thresholds is unreliable, especially at low depth, and how genotype likelihoods computed from reads and base qualities, combined with priors, give calls with a measure of confidence. It is the bridge between the binomial and Bayesian material of [[Probability]] and the practice of [[Variant Calling]].

## Coverage

Citation: Nielsen R, Paul JS, Albrechtsen A, Song YS. "Genotype and SNP calling from next-generation sequencing data". *Nature Reviews Genetics* 12(6):443-451 (2011). PMID 21587300.

| Part | Content | Vault notes |
|---|---|---|
| From reads to calls | Base calling, read mapping and their errors as inputs to SNP and genotype calling | [[Next-Generation Sequencing]], [[Read Mapping]] |
| Genotype likelihoods | Probability of the reads at a site under each possible genotype, from base qualities | [[Genotype Likelihood]], [[Binomial Distribution]], [[Bernoulli Distribution]] |
| Calling with uncertainty | Probabilistic (Bayesian) SNP and genotype calling; low-coverage data | [[Variant Calling]], [[Bayes' Theorem]] |

## How to use it

- L2: read the parts on genotype likelihoods after [[Binomial Distribution]] and [[Bayes' Theorem]].
- L3: use it as the map of methods before implementing a caller in [[10-genomic-pipeline]].

## Caveats

- 2011: short-read methods of the time; later callers (local haplotype assembly, machine-learning callers) are not covered.
- Metadata (authors, journal, volume, issue, pages, year, PubMed record) verified in this pass; a free author manuscript is in PubMed Central.
