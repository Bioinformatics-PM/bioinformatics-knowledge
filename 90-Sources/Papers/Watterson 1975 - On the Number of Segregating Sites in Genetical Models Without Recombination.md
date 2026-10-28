---
aliases:
  - Watterson 1975
  - Watterson's theta paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - domain/statistics
  - level/L3
kind: paper
tier: S
authors:
  - G. A. Watterson
journal: Theoretical Population Biology
year: 1975
url: "https://doi.org/10.1016/0040-5809(75)90020-9"
access: paid
---

# Watterson 1975 - On the Number of Segregating Sites in Genetical Models Without Recombination

> [!abstract]
> The paper that derived the moments of the number of segregating sites $S$ in a sample of sequences under the neutral infinite-sites model without recombination, and turned its mean into an unbiased estimator of the population mutation parameter $\theta$, now called Watterson's estimator.

## Why this source

It is the origin of $\hat\theta_W = S/a_n$, with $a_n = \sum_{i=1}^{n-1} 1/i$ for $n$ sampled sequences: under the neutral model $E[S] = a_n\theta$, so dividing the observed number of segregating sites by $a_n$ estimates $\theta$ without bias. The variance of $S$, $a_n\theta + b_n\theta^2$ with $b_n = \sum_{i=1}^{n-1} 1/i^2$, shows why adding sequences from one locus improves the estimate only slowly. With nucleotide diversity, it is the basis of neutrality tests that compare two estimators of $\theta$.

## Coverage

Citation: Watterson GA. "On the number of segregating sites in genetical models without recombination". *Theoretical Population Biology* 7(2):256-276 (April 1975). doi:10.1016/0040-5809(75)90020-9. PMID 1145509.

| Part | Content | Vault notes |
|---|---|---|
| Model | Neutral infinite-sites model without recombination, sample of $n$ sequences | [[Coalescent Theory]], [[Mutation]] |
| Moments of $S$ | Mean $a_n\theta$ and variance $a_n\theta + b_n\theta^2$ of the number of segregating sites | [[Watterson Estimator]], [[Estimator]] |
| Estimation | The unbiased moment estimator $S/a_n$ of $\theta$ | [[Watterson Estimator]], [[Method of Moments]] |

## How to use it

- L3: read after [[Coalescent Theory]]; use the mean and variance of $S$ with [[Estimator]] and [[Method of Moments]].
- M1: compare $\hat\theta_W$ with [[Nucleotide Diversity]] in [[Tajima's D]].

## Caveats

- Paid (Elsevier); the PubMed record has no abstract.
- Verified in this pass: author, title, journal, volume, issue, pages, month, year, DOI and PMID, and the paper's role as the origin of the unbiased estimator of $\theta$ built from the moments of the number of segregating sites (reported by secondary sources, including a National Academies text). The mean and variance formulas above are the standard forms attributed to this paper; they were not read in the original text.
