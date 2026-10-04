---
aliases:
  - Bland-Altman 1986
  - Bland-Altman plot paper
tags:
  - type/source
  - domain/statistics
  - domain/scientific-practice
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - J. Martin Bland
  - Douglas G. Altman
journal: The Lancet
year: 1986
url: "https://www-users.york.ac.uk/~mb55/meas/ba.htm"
access: free
---

# Bland 1986 - Statistical Methods for Assessing Agreement Between Two Methods of Clinical Measurement

> [!abstract]
> The paper that showed why a correlation coefficient cannot tell whether two measurement methods agree, and proposed analysing the differences between paired measurements instead (the Bland-Altman approach).

## Why this source

Comparing two replicates, two platforms or two pipelines on the same samples is a method-comparison problem. The paper explains, with clinical examples, that correlation measures linear relationship rather than agreement, depends on the range of the true values in the sample, and ignores systematic bias.

## Coverage

Citation: Bland JM, Altman DG. "Statistical methods for assessing agreement between two methods of clinical measurement". *The Lancet* 1(8476):307-310 (1986). The URL is a free copy on Martin Bland's University of York pages.

| Part | Content | Vault notes |
|---|---|---|
| Critique of correlation | Correlation is not agreement; it is scale-independent and depends on the range of values | [[Correlation]] |
| Proposed method | Mean and standard deviation of the differences between paired measurements, plotted against their mean | [[Correlation]], [[Technical Replicate]] |

## How to use it

- L2: read the critique of correlation, then plot differences against means for two replicate expression profiles.
- L3: apply the same logic when comparing two quantification tools on the same libraries.

## Caveats

- Clinical examples, not genomic ones; the log-scale difference-versus-average plot of expression data follows the same idea.
- Verified in this pass: authors, title, journal, volume, issue, pages, year, the free copy, and the main points summarized above.
