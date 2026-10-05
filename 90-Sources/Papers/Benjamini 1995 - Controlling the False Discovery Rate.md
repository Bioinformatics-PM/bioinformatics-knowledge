---
aliases:
  - Benjamini-Hochberg paper
  - BH procedure paper
tags:
  - type/source
  - domain/statistics
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Yoav Benjamini
  - Yosef Hochberg
journal: Journal of the Royal Statistical Society, Series B
year: 1995
url: "https://www.jstor.org/stable/2346101"
access: paid
---

# Benjamini 1995 - Controlling the False Discovery Rate

> [!abstract]
> "Controlling the false discovery rate: a practical and powerful approach to multiple testing": defines the FDR and a simple step-up procedure that controls it.

## Why this source

Genomics tests thousands of hypotheses at once (genes, variants, peaks). Controlling the familywise error rate is too strict there; the FDR, the expected proportion of false discoveries among rejections, is the standard criterion, and the Benjamini-Hochberg procedure is the default adjustment in differential-expression tools.

## Coverage

Citation: Benjamini Y, Hochberg Y. *J R Stat Soc Series B* 57(1):289-300 (1995). JSTOR 2346101.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Multiplicity; faults of familywise error rate control | [[Multiple Testing Correction\|Multiple Testing]], [[Family-Wise Error Rate]] |
| Definition | FDR: expected proportion of falsely rejected hypotheses; equals FWER when all nulls are true, smaller otherwise | [[False Discovery Rate]] |
| Procedure | Sequential Bonferroni-type procedure, proved to control FDR for independent test statistics | [[Benjamini-Hochberg Procedure]], [[P-Value]] |
| Evidence | Simulation study showing substantial gain in power | [[Statistical Power]] |

## How to use it

- L3: read after [[Hypothesis Testing]] and [[P-Value]]; implement the procedure on a vector of p-values and compare with Bonferroni.
- Use it as the citation in [[Differential Expression Analysis]] notes.

## Caveats

- The proof covers independent test statistics; later work extended it to some dependence structures.
- Metadata cross-checked against multiple published bibliographic records; the JSTOR page may require institutional access.
