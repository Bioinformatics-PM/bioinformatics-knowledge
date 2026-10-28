---
aliases:
  - MIQE
  - MIQE guidelines
  - Minimum Information for Publication of Quantitative Real-Time PCR Experiments
tags:
  - type/source
  - domain/biology
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Stephen A. Bustin
  - et al.
journal: Clinical Chemistry
year: 2009
url: "https://doi.org/10.1373/clinchem.2008.112797"
access: paid
---

# Bustin 2009 - The MIQE Guidelines

> [!abstract]
> "The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments": the reporting standard for qPCR, with a checklist of what a publication must state about samples, assays, calibration and data analysis.

## Why this source

qPCR results are easy to produce and easy to over-interpret. MIQE sets out what must be reported so that a reader can judge and repeat an experiment, which makes it the reference for what a **standard curve** must document: its slope and intercept, the amplification efficiency derived from the slope, its $r^2$ and its linear dynamic range. These are exactly the outputs of a [[Linear Regression]] and its [[Coefficient of Determination]].

## Coverage

Citation: Bustin SA, et al. "The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments". *Clinical Chemistry* 55(4):611-622 (2009).

| Part | Content | Vault notes |
|---|---|---|
| Purpose | Reporting standard to make qPCR experiments transparent, comparable between laboratories and repeatable | [[Quantitative Polymerase Chain Reaction]] |
| Calibration and validation | Checklist items marked essential: calibration curves with slope and y-intercept, PCR efficiency calculated from the slope, $r^2$ of the standard curve, linear dynamic range, Cq variation at the lower limit; marked desirable: confidence intervals (or standard error) for the efficiency and confidence intervals throughout the range | [[Linear Regression]], [[Coefficient of Determination]] |

## How to use it

- L2: read the checklist next to a standard-curve fit; each calibration item maps to one regression output.
- L3: use the full checklist when designing or reviewing a qPCR validation of RNA-seq results.

## Caveats

- Verified in this pass (web search): title, journal, volume, issue, pages and year; the calibration items and their essential or desirable status, from reproductions of the checklist; a 2010 follow-up stating that calibration curves must be available for review while slopes, intercepts, linear dynamic range and limit of detection are reported in the publication. The DOI is the one under which the paper is usually cited; it was not resolved in this pass.
- The efficiency formula $E = 10^{-1/\text{slope}} - 1$ follows from the exponential model of PCR; it is derived in [[Exponential Growth]], not taken from this paper.
- Access marked paid by default: the publisher's page was not checked. The full author list (twelve authors as usually cited) was not checked author by author.
