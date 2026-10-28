---
aliases:
  - LOD score paper
  - Morton LOD criterion
tags:
  - type/source
  - domain/biology
  - domain/statistics
  - level/L3
kind: paper
tier: S
authors:
  - Morton NE
journal: American Journal of Human Genetics
year: 1955
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1716611"
access: free
---

# Morton 1955 - Sequential Tests for the Detection of Linkage

> [!abstract]
> The paper that brought sequential likelihood-ratio tests to human linkage analysis and introduced the criterion of a LOD score of 3 for declaring linkage.

## Why this source

Human families cannot be designed like test crosses, so linkage evidence must be summed across small families. This paper set the statistical framework, base-10 log likelihood ratios summed over families, and the threshold that human linkage studies used for decades.

## Coverage

Citation: Morton NE. "Sequential tests for the detection of linkage". *American Journal of Human Genetics* 7(3):277-318 (September 1955).

| Part | Content | Vault notes |
|---|---|---|
| Method | Sequential probability ratio tests applied to linkage in human family data | [[Genetic Linkage]], [[Likelihood Ratio Test]] |
| Criterion | A base-10 LOD score of 3 as the criterion for detecting linkage | [[Genetic Linkage]], [[Pedigree Analysis]] |

Cited in [[Genetic Linkage]].

## How to use it

- L3: read the introduction and the definition of the scores after the LOD section of [[Genetic Linkage]]; compute a few scores by hand for phase-known families.
- M1: compare the LOD 3 criterion with modern genome-wide significance thresholds ([[Multiple Testing Correction]]).

## Caveats

- Verified in this pass: author, title, journal, volume, issue, pages, date, and that the LOD 3 criterion was introduced in this paper, as stated by a historical review on arXiv (0709.3765, "1953: An unrecognized summit in human genetic linkage analysis"). The PMC record number comes from the PMC article link returned by the search; the full text was not read in this pass.
- The same review argues that the threshold of 3 is better read as controlling the probability that a declared linkage is true (a false discovery rate, in modern terms) than as a type I error rate.
