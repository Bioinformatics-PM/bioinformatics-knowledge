---
aliases:
  - Exploratory Statistics
  - Statistique descriptive
tags:
  - type/moc
  - domain/statistics
  - level/L1
  - level/L2
prerequisites:
  - "[[Mathematical Foundations]]"
projects:
  - "[[01-dna-engine]]"
  - "[[09-genome-browser]]"
  - "[[bio-visualization]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Université Paris-Saclay - Introduction à la statistique avec R]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
---

# Descriptive Statistics

> [!abstract]
> Summarizing and looking at data before modeling it: types of variables, summaries of center and spread, the standard plots, association between variables, and the data-handling habits that make analysis possible.

## Why it matters for bioinformatics

- Every analysis starts with **exploration**: library sizes, quality distributions, replicate agreement and outlier samples are found by plots, not tests.
- Quality control tools are descriptive statistics: per-position box plots of base quality, histograms of read length and insert size, coverage percentiles, the assembly N50 (a length-weighted median).
- Many normalization methods are summaries: median-of-ratios size factors, quantile normalization, z-scores for heatmaps.

## Before you start

- [[Mathematical Foundations]]: [[Summation Notation]], [[Logarithm]].
- [[Python Programming]] with arrays and data frames; see [[Programming]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[Exploratory Data Analysis]] (L1): explore a dataset with summaries and plots before any model. Bio: a first look at a count matrix (library sizes, detected genes, sample relations) catches sample swaps and failed libraries.
2. [[Sampling]] (L1): tell population from sample, random from biased sampling, biological from technical replicates. Bio: cells sequenced versus cells in the tissue; cohort ascertainment bias.
3. [[Level of Measurement]] (L1): classify variables as nominal, ordinal, discrete or continuous and choose summaries accordingly. Bio: genotype (nominal), tumor grade (ordinal), read counts (discrete), expression level (continuous).
4. [[Frequency Distribution]] (L1): build absolute and relative frequency tables. Bio: nucleotide composition; codon usage tables; allele frequencies.
5. [[Measure of Central Tendency]] (L1): compute mean, median and mode and know when each misleads. Bio: median read length; median-of-ratios normalization of RNA-seq libraries.
6. [[Measure of Dispersion]] (L1): compute range, variance, standard deviation, interquartile range, median absolute deviation and coefficient of variation. Bio: selecting highly variable genes in single-cell data.
7. [[Quantile]] (L1): compute percentiles and quartiles. Bio: coverage percentiles; quantile normalization of microarrays; N50 of an assembly.
8. [[Standard Score]] (L1): compute z-scores to compare values on different scales. Bio: row-scaled expression in heatmaps.
9. [[Histogram]] (L1): choose bins and read the shape of a distribution. Bio: read-length, GC-content and insert-size distributions.
10. [[Box Plot]] (L1): compare distributions across groups. Bio: per-position base-quality plots in read quality control.
11. [[Scatter Plot]] (L1): plot two variables and read trends and clusters. Bio: replicate versus replicate expression.
12. [[Data Visualization]] (L1): choose the right chart, encode data honestly, use color-blind-safe palettes and label axes and units. Bio: figures for papers; genome tracks.
13. [[Contingency Table]] (L1): cross-tabulate two categorical variables. Bio: genotype by case/control status in a genetic association study.
14. [[Correlation]] (L1): compute and interpret Pearson's correlation coefficient; know that correlation is not causation. Bio: replicate concordance; co-expression.
15. [[Outlier]] (L1): detect outliers with robust rules and decide what to do with them. Bio: an outlier sample in a PCA of RNA-seq libraries.

### Stage 2 - Core (L2)

16. [[Empirical Cumulative Distribution Function]] (L2): build and compare ECDFs. Bio: comparing expression or p-value distributions between conditions.
17. [[Kernel Density Estimation]] (L2): smooth a distribution and choose a bandwidth. Bio: violin plots of single-cell expression.
18. [[Q-Q Plot]] (L2): compare a sample with a theoretical distribution or with another sample. Bio: the GWAS Q-Q plot of p-values, which reveals inflation.
19. [[Rank Correlation]] (L2): compute Spearman and Kendall correlations. Bio: robust co-expression that tolerates outliers and nonlinearity.
20. [[Data Transformation]] (L2): apply log, $\log(x + 1)$ and variance-stabilizing transformations and see their effect. Bio: log-transforming counts before PCA or clustering.
21. [[Heatmap]] (L2): display a matrix with a sensible color scale, scaling and ordering. Bio: clustered heatmaps of gene expression.
22. [[Tidy Data]] (L2): organize data with one observation per row and one variable per column; reshape between long and wide. Bio: sample metadata tables joined to count matrices.
23. [[Missing Data]] (L2): recognize missing completely at random, at random and not at random, and the consequences of imputation. Bio: missing values in proteomics below the detection limit; missing genotypes.
24. [[Simpson's Paradox]] (L2): recognize an association that reverses when data are pooled across groups. Bio: pooling samples across batches or populations.

> [!tip] How to study it
> Learn items 1 to 15 in curriculum Stage 1 with a real dataset (for example the base qualities of a FASTQ file), making every plot in Python. Return to items 16 to 24 when you meet high-throughput data in [[Transcriptomics]] and [[Genomics]].

## Uses from other domains

- [[Read Quality Control]] ([[NGS Data Analysis]]): histograms and box plots of qualities.
- [[Genome Assembly]] ([[Genomics]]): N50 and other length statistics.
- [[Genome-Wide Association Study]] ([[Population Genomics]]): Q-Q plots of p-values.
- [[Count Normalization]], [[Size Factor Estimation]] ([[Transcriptomics]]): medians, quantiles and transformations of count matrices.
- [[Experimental Design]]: sampling and replicates are planned there.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Université Paris-Saclay - Introduction à la statistique avec R]] | Université Paris-Saclay (FUN) | L1 | Describing variables; associations between variables (items 1-14), in French[^fun] |
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard (edX) | L2 | PH525.1x: exploratory data analysis, robust statistics, on life-science data[^ph525] |

## Reference books

- [[Introductory Statistics (OpenStax)]]: chapter 1 "Sampling and Data" and chapter 2 "Descriptive Statistics" (items 2-11); the linear regression and correlation chapter (item 14).[^openstax]
- [[Modern Statistics for Modern Biology (Holmes)]]: exploration of high-throughput data, with reproducible code (Stage 2).[^msmb]
- [[Python for Data Analysis (McKinney)]]: pandas data frames, reshaping and plotting (items 12, 22).[^mckinney]

## Lab projects

- [[01-dna-engine]]: base counts, frequencies and GC content as descriptive statistics of a sequence.
- [[09-genome-browser]]: data visualization at every scale.
- [[bio-visualization]]: reusable plots for sequences, alignments, trees and population dynamics.

## References

[^fun]: [[Université Paris-Saclay - Introduction à la statistique avec R]]: introduction, description of variables, estimation, association.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x.
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed.
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]].
[^mckinney]: [[Python for Data Analysis (McKinney)]], pandas and visualization parts.

Scope check: a first statistics course starts with sampling and descriptive statistics before probability and inference;[^openstax] first-year mathematics for biologists at Cambridge includes practicals on real biological data with data handling in R.[^cam]

[^cam]: [[University of Cambridge - Natural Sciences Tripos]], Part IA Mathematical Biology practicals.
