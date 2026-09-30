---
aliases:
  - Lazic
tags:
  - type/source
  - domain/scientific-practice
  - domain/statistics
  - level/L2
  - level/L3
kind: book
tier: A
authors:
  - Stanley E. Lazic
institution: Cambridge University Press
year: 2016
edition: "1st"
url: "https://doi.org/10.1017/9781139696647"
access: paid
---

# Experimental Design for Laboratory Biologists (Lazic)

> [!abstract]
> A practical guide to designing reproducible laboratory experiments with low bias and high precision, with analyses in R.

## Why this source

Written for lab-based biomedical researchers by a statistician who works in drug discovery, it uses examples from cell culture and model organisms instead of agricultural field trials. It explains how to identify the experimental unit, control biological and technical sources of bias and noise, and choose a design, and it covers topics rarely taught: graphical data exploration, choosing outcome variables, data quality checks and preprocessing. It assumes no prior experience with R.

## Coverage

Citation: Lazic SE. *Experimental Design for Laboratory Biologists: Maximising Information and Improving Reproducibility*. Cambridge University Press (2016). doi:10.1017/9781139696647. Coverage is described by topic; chapter titles were not verified in this pass.

| Part | Content | Vault notes |
|---|---|---|
| Key ideas | Experimental units, replication, pseudoreplication | [[Experimental Unit]], [[Biological Replicate]], [[Technical Replicate]], [[Pseudoreplication]] |
| Bias and noise | Controlling biological and technical factors | [[Randomization]], [[Blinding]], [[Confounding]] |
| Designs | Common designs and how to plan an experiment | [[Randomized Block Design]], [[Paired Design]], [[Factorial Design]] |
| Data | Exploration, outcome variables, quality control, preprocessing | [[Exploratory Data Analysis]] |
| Analysis | Matching analyses in R | [[Analysis of Variance]], [[Linear Regression]] |

Cited in [[Experimental Design]] and [[Scientific Practice]].

## How to use it

- L2: the main text for items 2 to 13 of [[Experimental Design]]; read it after [[Hurlbert 1984 - Pseudoreplication and the Design of Ecological Field Experiments]] and redo its examples in R.
- L3: use it to plan the replicates and randomization of any wet-lab or simulation study before collecting data.

## Caveats

- Focused on lab experiments; high-throughput designs (batches, sequencing depth) are covered better in [[Modern Statistics for Modern Biology (Holmes)]] and [[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]].
- Paid book; an accompanying website provides the R code, datasets and the labstats R package.
- Verified in this pass: title, author, publisher, year, ISBNs and Cambridge Core DOI.
