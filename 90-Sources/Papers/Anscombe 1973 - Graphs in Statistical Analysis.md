---
aliases:
  - Anscombe's quartet paper
tags:
  - type/source
  - domain/statistics
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - Francis J. Anscombe
journal: The American Statistician
year: 1973
url: "https://doi.org/10.1080/00031305.1973.10478966"
access: paid
---

# Anscombe 1973 - Graphs in Statistical Analysis

> [!abstract]
> A short paper arguing that graphs are essential to good statistical analysis, famous for four small datasets (Anscombe's quartet) that share their summary statistics and fitted line but look completely different when plotted.

## Why this source

The classic, citable demonstration that a correlation coefficient or a regression line never replaces a plot. The four datasets are small enough to type in and recompute by hand.

## Coverage

Citation: Anscombe FJ. "Graphs in statistical analysis". *The American Statistician* 27(1):17-21 (1973). doi:10.1080/00031305.1973.10478966.

| Part | Content | Vault notes |
|---|---|---|
| Argument | Graphs are essential; summary statistics alone mislead | [[Exploratory Data Analysis]], [[Data Visualization]] |
| The quartet | Four datasets of 11 points with the same means, variances, correlation and regression line | [[Correlation]], [[Scatter Plot]], [[Linear Regression]] |

## How to use it

- L1: plot the four datasets yourself, then compute their summaries ([[Correlation]] does it in Python).
- L2: use the quartet to test any summary or diagnostic you write.

## Caveats

- Verified in this pass: author, title, journal, volume, issue, pages, year and DOI; the shared summaries (mean of x = 9, mean of y = 7.5, nearly identical variances, correlations and regression lines). The data values used in the vault were recomputed and reproduce these summaries.
- Access marked paid by default: the publisher's page was not checked. The quartet itself is reproduced in many textbooks and software packages.
