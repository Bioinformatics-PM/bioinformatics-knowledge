---
aliases:
  - Nei 1978
  - Nei's unbiased heterozygosity
tags:
  - type/source
  - domain/biology
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Masatoshi Nei
journal: Genetics
year: 1978
url: "https://doi.org/10.1093/genetics/89.3.583"
access: free
---

# Nei 1978 - Estimation of Average Heterozygosity and Genetic Distance from a Small Number of Individuals

> [!abstract]
> Shows that heterozygosity and genetic distance computed directly from sample allele frequencies are systematically biased when few individuals are sampled, gives unbiased estimators of both, and argues that studying many loci matters more than sampling many individuals.

## Why this source

The standard reference for the small-sample correction of expected heterozygosity (gene diversity): the plug-in value $1 - \sum_k \hat p_k^2$ underestimates the population value, and the unbiased version multiplies it by $2n/(2n-1)$ for $n$ diploid individuals, the same kind of correction as the $n - 1$ of the sample variance. Its sampling argument, that a few individuals per population suffice when many loci are studied and heterozygosity is low, still guides population surveys.

## Coverage

Citation: Nei M. "Estimation of average heterozygosity and genetic distance from a small number of individuals". *Genetics* 89(3):583-590 (1978). doi:10.1093/genetics/89.3.583. PMID 17248844, free full text at PMC1213855.

| Part | Content | Vault notes |
|---|---|---|
| Bias | Systematic bias of sample heterozygosity and sample genetic distance | [[Estimator]], [[Allele Frequency]] |
| Unbiased estimators | Corrected formulas for heterozygosity and genetic distance | [[Estimator]], [[Nucleotide Diversity]] |
| Sampling design | Few individuals suffice when many loci are studied and heterozygosity is low | [[Experimental Design]] |

## How to use it

- L2: read the abstract and the heterozygosity formulas with [[Estimator]]; redo the bias calculation of the plug-in estimator.
- L3: the genetic distance part, after [[Evolutionary Distance]].

## Caveats

- Written for allele-frequency data of the 1970s (protein electrophoresis); sequence diversity is now summarized with [[Nucleotide Diversity]] and the [[Watterson Estimator]].
- Verified in this pass: author, title, journal, volume, issue, pages, year, DOI, PMID and PMCID, and the abstract's statements on the biases, the unbiased estimators and the sample sizes needed. The $2n/(2n-1)$ factor is the form widely reproduced from this paper; it was not read in the PDF.
