---
aliases:
  - Case-control association protocol
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Geraldine M. Clarke
  - Carl A. Anderson
  - Fredrik H. Pettersson
  - Lon R. Cardon
  - Andrew P. Morris
  - Krina T. Zondervan
journal: Nature Protocols
year: 2011
url: "https://doi.org/10.1038/nprot.2010.182"
access: free
---

# Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies

> [!abstract]
> A step-by-step protocol for the basic statistical analysis of a population-based genetic case-control association study: measures of association, tests of association, visualization, multiple testing and replication.

## Why this source

It turns the genotype-by-status tables of a case-control study into a concrete analysis plan, with the standard single-SNP tests (allelic, genotypic, Cochran-Armitage trend) and odds ratios, run with tools that are still in use (PLINK, R, Haploview). It is the bridge between the descriptive [[Contingency Table]] and the inferential side of a [[Genome-Wide Association Study]].

## Coverage

Citation: Clarke GM, Anderson CA, Pettersson FH, Cardon LR, Morris AP, Zondervan KT. "Basic statistical analysis in genetic case-control studies". *Nature Protocols* 6(2):121-133 (2011). doi:10.1038/nprot.2010.182. Free full text at PMC3154648.

| Part | Content | Vault notes |
|---|---|---|
| Measures of association | Odds ratios; disease models (genotypic, allelic, trend) | [[Contingency Table]], [[Effect Size]] |
| Tests of association | Allelic test, genotypic test, Cochran-Armitage trend test on SNP data | [[Chi-Square Test]], [[Genome-Wide Association Study]] |
| Interpretation | Visualization of results, control of multiple testing, replication | [[Multiple Testing Correction]] |

## How to use it

- L2: read the measures and tests of association with the [[Contingency Table]] note open, and redo the tables for one SNP by hand.
- L3: follow the protocol on a public genotype dataset with PLINK, then compare the tests across SNPs.

## Caveats

- Covers basic single-SNP analysis; genotype quality control and advanced methods are outside its scope.
- Verified in this pass: authors, title, journal, volume, issue, pages, year, DOI, PMC identifier, and the scope listed in the abstract (measures of association and disease models, tests of association including the Cochran-Armitage trend test, visualization, multiple testing, replication, tools PLINK, R and Haploview). Section numbers not verified.
