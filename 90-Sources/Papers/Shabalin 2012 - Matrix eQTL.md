---
aliases:
  - Matrix eQTL
  - MatrixEQTL
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Andrey A. Shabalin
journal: Bioinformatics
year: 2012
url: "https://doi.org/10.1093/bioinformatics/bts163"
access: free
---

# Shabalin 2012 - Matrix eQTL

> [!abstract]
> "Matrix eQTL: ultra fast eQTL analysis via large matrix operations": a method and R package that tests every genotype-expression pair with linear regression, made fast by recasting the heavy computation as large matrix operations.

## Why this source

An expression quantitative trait locus (eQTL) study regresses the expression of each gene on the genotype of each variant: millions to billions of small linear models. This paper states the model plainly (linear regression with additive or ANOVA genotype effects, plus covariates) and shows why the linear-model algebra allows all tests to be computed at once.

## Coverage

Citation: Shabalin AA. "Matrix eQTL: ultra fast eQTL analysis via large matrix operations". *Bioinformatics* 28(10):1353-1358 (2012). doi:10.1093/bioinformatics/bts163. PMID 22492648, free full text at PMC3348564.

| Part | Content | Vault notes |
|---|---|---|
| Model | Association between genotype and expression tested with linear regression, with additive or ANOVA genotype effects | [[Expression Quantitative Trait Locus]], [[Linear Regression]], [[Coefficient of Determination]] |
| Covariates and errors | Covariates to account for population stratification, gender and clinical variables; heteroscedastic or correlated errors | [[Multiple Linear Regression]], [[Regression Diagnostics]] |
| Scale | False discovery rate estimation; separate treatment of local (cis) and distant (trans) eQTLs; speed from preprocessing and large matrix operations, reported as 2 to 3 orders of magnitude faster than popular tools of the time, with the same eQTLs found | [[False Discovery Rate]], [[Vectorization]] |

## How to use it

- L2: read the abstract and the model description to see that an eQTL test is a [[Linear Regression]] of expression on genotype dosage.
- L3: follow how covariates are handled and why the test statistics reduce to matrix products, then run the package on a small public dataset.

## Caveats

- Verified in this pass (web search): author, title, journal, volume, issue, pages, year, DOI, PMID, PMC identifier and the abstract content summarized above. The arXiv preprint words the speed-up differently ("thousands of times"); the journal abstract is cited here.
- Implementation details and the package version history were not checked.
