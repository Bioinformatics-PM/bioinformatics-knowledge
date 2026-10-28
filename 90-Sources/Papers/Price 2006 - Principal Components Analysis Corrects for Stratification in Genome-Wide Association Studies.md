---
aliases:
  - EIGENSTRAT paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L3
kind: paper
tier: A
authors:
  - Alkes L. Price
  - Nick J. Patterson
  - Robert M. Plenge
  - Michael E. Weinblatt
  - Nancy A. Shadick
  - David Reich
journal: Nature Genetics
year: 2006
url: "https://doi.org/10.1038/ng1847"
access: paid
---

# Price 2006 - Principal Components Analysis Corrects for Stratification in Genome-Wide Association Studies

> [!abstract]
> The paper that introduced EIGENSTRAT: principal components of genome-wide genotypes describe ancestry along continuous axes, and adjusting association tests for them removes spurious associations caused by population stratification.

## Why this source

When cases and controls (or high and low values of a trait) differ systematically in ancestry, any variant whose allele frequency differs between ancestral populations looks associated. This paper proposed a correction that works at genome scale: compute the main axes of genetic variation with [[Principal Component Analysis]] and adjust each test for them. It is the landmark reference for the "ancestry components" used as covariates in association models.

## Coverage

Citation: Price AL, Patterson NJ, Plenge RM, Weinblatt ME, Shadick NA, Reich D. "Principal components analysis corrects for stratification in genome-wide association studies". *Nature Genetics* 38(8):904-909 (2006). doi:10.1038/ng1847. PMID 16862161.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Population stratification, ancestry differences between cases and controls, can cause spurious associations | [[Population Stratification]], [[Confounding]] |
| Method | Principal components analysis models ancestry differences along continuous axes of variation; the correction is specific to each marker's variation in frequency across ancestral populations, limiting spurious associations while keeping power | [[Principal Component Analysis]], [[Multiple Linear Regression]] |
| Scale | Applicable to disease studies with hundreds of thousands of markers; implemented in EIGENSTRAT (EIGENSOFT package) | [[Genome-Wide Association Study]] |

## How to use it

- L3: read it with [[Population Stratification]] and [[Multiple Linear Regression]]; the adjustment is a regression on the principal components.
- M1: compare with linear mixed models, which correct for relatedness and structure together ([[Linear Mixed Model]]).

## Caveats

- Verified in this pass (web search): authors (initials), title, journal, volume, issue, pages, year, DOI, PMID and the abstract content summarized above. Methods and results were not read in full.
- Later work refined the method and compared it with mixed models; read it as the landmark, not as current best practice.
- Access marked paid: the journal is subscription-based; the publisher's page was not checked.
