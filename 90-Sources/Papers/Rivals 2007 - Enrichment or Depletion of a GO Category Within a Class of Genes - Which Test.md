---
aliases:
  - Rivals et al. 2007
  - Which test for GO enrichment
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Isabelle Rivals
  - L. Personnaz
  - L. Taing
  - M.-C. Potier
journal: Bioinformatics
year: 2007
url: "https://doi.org/10.1093/bioinformatics/btl633"
access: partial
---

# Rivals 2007 - Enrichment or Depletion of a GO Category Within a Class of Genes - Which Test

> [!abstract]
> A review of the statistical tests used to decide whether a Gene Ontology category is enriched or depleted in a class of genes, showing that the hypergeometric test and Fisher's exact test are the same test.

## Why this source

Enrichment tools offer several tests for the same 2×2 question (is this category over-represented among my genes?). This paper compares them directly: the binomial test, the chi-square test, the test of equality of two probabilities, Fisher's exact test and the hypergeometric test. It shows that the hypergeometric and Fisher's exact tests are equivalent, that the other tests are valid only for large samples, and it discusses one- and two-sided p-values and the discreteness and conservatism of exact tests. It is the reference for the statistics behind [[Over-Representation Analysis]].

## Coverage

Citation: Rivals I, Personnaz L, Taing L, Potier MC. "Enrichment or depletion of a GO category within a class of genes: which test?". *Bioinformatics* 23(4):401-407 (2007). doi:10.1093/bioinformatics/btl633.

| Part | Content | Vault notes |
|---|---|---|
| Tests reviewed | Binomial, chi-square, equality of two probabilities, Fisher's exact, hypergeometric | [[Hypergeometric Distribution]], [[Fisher's Exact Test]], [[Chi-Square Test]] |
| Main result | Hypergeometric and Fisher's exact tests are equivalent; the others are large-sample approximations | [[Contingency Table]], [[Over-Representation Analysis]] |
| p-values | One- and two-sided p-values; discreteness and conservatism | [[P-Value]], [[Hypothesis Testing]] |

## How to use it

- L2: read the comparison of tests with [[Hypergeometric Distribution]] and redo one enrichment p-value with both the hypergeometric and Fisher's exact formulas.
- L3: use the discussion of one- and two-sided p-values and discreteness when choosing the test of an enrichment tool.

## Caveats

- Covers the single-category test; multiple testing across categories and the dependence between GO terms are separate questions ([[Multiple Testing Correction]]).
- Verified in this pass: authors' surnames and initials (first name for the first author), title, journal, volume, issue, pages, year, DOI, and the content summarized above. Open access on the publisher site was not verified; a full-text copy is hosted on an Ohio State University course page.
