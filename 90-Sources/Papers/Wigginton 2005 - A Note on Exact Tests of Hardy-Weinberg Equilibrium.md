---
aliases:
  - Wigginton 2005
  - HWE exact test
tags:
  - type/source
  - domain/statistics
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Janis E. Wigginton
  - David J. Cutler
  - Gonçalo R. Abecasis
journal: American Journal of Human Genetics
year: 2005
url: "https://doi.org/10.1086/429864"
access: free
---

# Wigginton 2005 - A Note on Exact Tests of Hardy-Weinberg Equilibrium

> [!abstract]
> Shows that the usual chi-square test of Hardy-Weinberg equilibrium can have inflated type I error, even in fairly large samples, and gives exact tests with efficient computation for genotype data.

## Why this source

Genotyping and sequencing studies test each variant against Hardy-Weinberg proportions. This paper explains why the chi-square approximation is unreliable when the minor allele is rare, and gives an exact test conditioned on the allele counts, with efficient algorithms and freely available code; implementations for R and Python cite it. It also lists what departures can mean: inbreeding, population stratification, genotyping problems and, in samples of affected individuals, association.

## Coverage

Citation: Wigginton JE, Cutler DJ, Abecasis GR. "A note on exact tests of Hardy-Weinberg equilibrium". *American Journal of Human Genetics* 76(5):887-893 (2005). doi:10.1086/429864. PMID 15789306, free full text at PMC1199378.

| Part | Content | Vault notes |
|---|---|---|
| Motivation | Departures from Hardy-Weinberg equilibrium as signals of inbreeding, stratification, genotyping problems, or association in affected individuals | [[Hardy-Weinberg Equilibrium]], [[Variant Filtering]] |
| Problem | Inflated type I error of the chi-square goodness-of-fit test, even in relatively large samples | [[Chi-Square Test]] |
| Method | Exact test based on the probability of each heterozygote count given the allele counts, with efficient computation | [[Hardy-Weinberg Equilibrium]], [[Fisher's Exact Test]] |
| Software | Freely available code for quality assessment of large genotype datasets | [[Genome-Wide Association Study]] |

Cited in [[Hardy-Weinberg Equilibrium]].

## How to use it

- L2: read the introduction and the description of the exact test, then implement it ([[Hardy-Weinberg Equilibrium#Computational representation]]).
- L3: compare the type I error of the chi-square and exact tests for rare alleles (Exercise 5 of [[Hardy-Weinberg Equilibrium]]).

## Caveats

- An exact test never exceeds its nominal level, but with few possible outcomes it can be much more conservative than nominal.
- Verified in this pass: authors, title, journal, volume, issue, pages, year, DOI, PMID and PMCID, the main finding (inflated type I error of the chi-square test) and the availability of the code, from the PubMed Central record, the authors' page and software documentation that cites it. The distribution of heterozygote counts used in the vault was checked by computation (its probabilities sum to 1), not against the paper's equations.
