---
aliases:
  - Cook's distance paper
tags:
  - type/source
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - R. Dennis Cook
journal: Technometrics
year: 1977
url: "https://doi.org/10.2307/1268249"
access: paid
---

# Cook 1977 - Detection of Influential Observation in Linear Regression

> [!abstract]
> The paper that introduced Cook's distance: a measure, based on confidence ellipsoids, of how much each observation contributes to the least-squares estimate of a linear regression.

## Why this source

An outlier is not necessarily influential, and an influential point need not have a large residual. Cook's measure combines the two ingredients, the size of the residual and the leverage of the point, into one number per observation. It is the primary reference for the influence diagnostic printed by regression software.

## Coverage

Citation: Cook RD. "Detection of influential observation in linear regression". *Technometrics* 19(1):15-18 (1977). JSTOR stable identifier 1268249.

| Part | Content | Vault notes |
|---|---|---|
| Measure | A measure based on confidence ellipsoids for judging the contribution of each data point to the least-squares estimate in full-rank linear regression models | [[Regression Diagnostics]] |
| Decomposition | The measure combines the studentized residuals with the variances of the residuals and of the predicted values | [[Regression Diagnostics]], [[Outlier]] |
| Examples | Two worked examples | none |

## How to use it

- L2: after [[Linear Regression]], read the definition and compute the measure for a small dataset with one extreme point ([[Regression Diagnostics]]).
- L3: derive its expression in terms of studentized residuals and leverages.

## Caveats

- Verified in this pass (web search): author, title, journal, volume, issue, pages, year, JSTOR identifier and the content of the abstract summarized above. The DOI is the JSTOR-based one listed in bibliographic records; the publisher's page was not opened.
- Paid access through JSTOR or the publisher.
