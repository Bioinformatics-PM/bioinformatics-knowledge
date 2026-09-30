---
aliases:
  - Gene Expression Analysis
  - RNA-seq Analysis
tags:
  - type/moc
  - domain/bioinformatics
  - domain/statistics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[NGS Data Analysis]]"
  - "[[Genomics]]"
  - "[[Molecular Biology]]"
  - "[[Statistical Inference]]"
  - "[[Linear Models]]"
  - "[[Multivariate Analysis]]"
  - "[[Experimental Design]]"
projects: []
sources:
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Benjamini 1995 - Controlling the False Discovery Rate]]"
---

# Transcriptomics

> [!abstract]
> Measuring and comparing gene expression from RNA sequencing: from reads to counts, normalization, differential expression with negative binomial models, and the basics of single-cell analysis.

## Why it matters for bioinformatics

RNA-seq is among the most common functional genomics assays and often the first analysis a bioinformatician is asked to run. It is also the best school of applied statistics in the field: count data, overdispersion, generalized linear models, shrinkage and thousands of simultaneous tests, the material that statistics courses for the life sciences build toward.[^msmb][^ph525] Single-cell RNA-seq extends the same ideas to thousands of cells per sample and brings dimensionality reduction and graph clustering into daily practice.

## Before you start

- [[Molecular Biology]]: [[Transcription]], [[Messenger RNA]], [[RNA Processing]], [[Alternative Splicing]], [[Gene Expression]], [[Non-Coding RNA]]; [[Cell Biology]]: [[Cell Type]], [[Cell Differentiation]].
- [[NGS Data Analysis]]: [[Read Quality Control]], [[Read Mapping]], [[Duplicate Read]]; [[Bioinformatics Foundations]]: [[GFF Format]]; [[Biotechnology]]: [[Microarray]].
- [[Probability]]: [[Poisson Distribution]], [[Negative Binomial Distribution]].
- [[Statistical Inference]]: [[Hypothesis Testing]], [[P-Value]], [[Likelihood Ratio Test]], [[Multiple Testing Correction]], [[False Discovery Rate]], [[Benjamini-Hochberg Procedure]].
- [[Linear Models]]: [[Design Matrix]], [[Linear Contrast]], [[Generalized Linear Model]], [[Overdispersion]], [[Negative Binomial Regression]].
- [[Multivariate Analysis]]: [[Principal Component Analysis]], [[Hierarchical Clustering]], [[K-Means Clustering]]; [[Descriptive Statistics]]: [[Heatmap]].
- [[Experimental Design]]: [[Biological Replicate]], [[Batch Effect]], [[Pseudoreplication]], [[Sequencing Experiment Design]].
- [[Scientific Computing]]: [[Sparse Matrix]] (single-cell count matrices).

## Learning path

### Stage 2 - Core (L2)

1. [[Transcriptome]] (L2): describe the set of transcripts of a cell or tissue and why it changes with condition and cell type.
2. [[RNA Sequencing]] (L2): follow an RNA-seq experiment from library preparation (poly-A selection, rRNA depletion, strandedness) to reads.
3. [[Spliced Read Alignment]] (L2): map reads across introns with splice-aware aligners (STAR, HISAT2).
4. [[Count Matrix]] (L2): build the gene by sample count table (featureCounts, HTSeq) and know which reads are discarded.
5. [[Count Normalization]] (L2): explain why raw counts are not comparable and compute CPM and TPM (and why RPKM is discouraged).
6. [[Log Fold Change]] (L2): express expression changes on a log2 scale and read MA and volcano plots.

### Stage 3 - Advanced (L3)

7. [[Pseudoalignment]] (L3): assign reads to compatible transcripts without base-level alignment (kallisto, salmon).
8. [[Transcript Quantification]] (L3): estimate transcript abundances from ambiguous reads with an EM algorithm.
9. [[Transcriptome Assembly]] (L3): reconstruct transcripts de novo (Trinity) or guided by a genome (StringTie).
10. [[Size Factor Estimation]] (L3): correct for library size and composition with median-of-ratios (DESeq2) and TMM (edgeR).
11. [[Variance-Stabilizing Transformation]] (L3): transform counts for PCA, clustering and heatmaps of samples.
12. [[Batch Effect Correction]] (L3): model batches in the design or remove them for visualization (ComBat-style), without erasing biology.
13. [[Dispersion Estimation]] (L3): estimate gene-wise overdispersion of a negative binomial model and shrink it toward a mean-dispersion trend.
14. [[Differential Expression Analysis]] (L3): fit a negative binomial GLM per gene, test contrasts (Wald, likelihood ratio), shrink fold changes and control the FDR.
15. [[Single-Cell RNA Sequencing]] (L3): compare droplet and plate protocols and read a sparse cell by gene count matrix.
16. [[Unique Molecular Identifier]] (L3): use cell barcodes and UMIs to count molecules rather than reads.
17. [[Single-Cell Quality Control]] (L3): filter empty droplets, dying cells (mitochondrial fraction) and doublets.
18. [[Single-Cell Normalization]] (L3): normalize sparse counts (log-normalization, pooling, regularized negative binomial) and know its pitfalls.
19. [[Highly Variable Gene]] (L3): select informative genes before dimensionality reduction.
20. [[Single-Cell Clustering]] (L3): cluster cells on a k-nearest-neighbor graph (Louvain, Leiden) and visualize the result with UMAP.
21. [[Cell Type Annotation]] (L3): find marker genes per cluster and assign cell types with markers and reference atlases.

### Stage 4 - Frontier (M1)

22. [[Differential Splicing Analysis]] (M1): test differential exon and isoform usage between conditions.
23. [[Pseudobulk Differential Expression]] (M1): aggregate cells per sample to test conditions with bulk methods and avoid pseudoreplication.
24. [[Single-Cell Data Integration]] (M1): align datasets across batches, donors and technologies (Harmony, scVI-style).
25. [[Trajectory Inference]] (M1): order cells along a pseudotime for continuous processes such as differentiation.
26. [[RNA Velocity]] (M1): infer the direction of expression change from spliced and unspliced counts.
27. [[Cell-Type Deconvolution]] (M1): estimate cell-type proportions of bulk samples from single-cell references.
28. [[Spatial Transcriptomics]] (M1): analyze expression measured in tissue coordinates and its spatial statistics.

> [!tip]
> Do one complete bulk analysis (items 3 to 14) on a public dataset before starting single-cell. Microarray analysis is historical: learn [[Microarray]] as a technique and skip its specific normalization methods unless a project needs them.

## Uses from other domains

- [[Expectation-Maximization Algorithm]] (from [[Statistical Inference]]): transcript quantification (item 8).
- [[Empirical Bayes]] (from [[Bayesian Statistics]]): dispersion and fold-change shrinkage (items 13 and 14).
- [[Uniform Manifold Approximation and Projection]] and [[t-Distributed Stochastic Neighbor Embedding]] (from [[Multivariate Analysis]]): single-cell visualization.
- [[Graph-Based Clustering]] (from [[Multivariate Analysis]]): the k-nearest-neighbor graph clustering behind item 20.
- [[Over-Representation Analysis]] and [[Gene Set Enrichment Analysis]] (from [[Systems Biology]]): interpreting gene lists after item 14.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L2-M1 | "Transcriptomics" ("Reference-based RNA-Seq data analysis", "1: RNA-Seq reads to counts", "2: RNA-seq counts to genes", "De novo transcriptome reconstruction with RNA-Seq"); "Single Cell" ("Understanding Barcodes", "Pre-processing of 10X Single-Cell RNA Datasets", "Filter, plot and explore single-cell RNA-seq data with Scanpy", "Batch Correction and Integration with Seurat or Scanpy", "Inferring single cell trajectories with Monocle3", "Bulk RNA Deconvolution with MuSiC")[^gtn] |
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard | L3 | Linear models, inference and modeling for high-throughput experiments, high-dimensional data analysis, Bioconductor[^ph525] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins | L3 | "Bioconductor for Genomic Data Science" and "Statistics for Genomic Data Science"[^jhu] |
| [[Coursera UCSD - Bioinformatics Specialization]] | UC San Diego | L3 | V. Genomic Data Science and Clustering (clustering expression data)[^coursera] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | Gene expression, clustering and classification[^mit6047] |

## Reference books

- [[Modern Statistics for Modern Biology (Holmes)]]: count data from high-throughput sequencing and multiple testing for items 5 to 14; clustering and multivariate analysis for items 11 and 19 to 21.[^msmb]
- [[Benjamini 1995 - Controlling the False Discovery Rate]]: the FDR procedure used at the end of item 14.[^bh]

## Lab projects

No Lab project validates this syllabus yet. The natural candidate is a bulk RNA-seq workflow that reuses the QC and mapping stages of [[10-genomic-pipeline]]; it is not planned in [[Bioinformatics Lab]].

## References

Bulk before single-cell, and counting before modeling, follows the Galaxy training sequence (reads to counts, counts to genes, genes to pathways) and its single-cell track;[^gtn] the statistical treatment of counts (negative binomial models, multiple testing) follows the reference text and the life-science statistics courses.[^msmb][^ph525][^jhu]

[^gtn]: [[Galaxy Training Network - Training Material]], topics "Transcriptomics" and "Single Cell" (tutorial titles as listed in the table).
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], material on count data from high-throughput sequencing, multiple testing, clustering and multivariate analysis.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.2x to 4x (linear models, inference for high-throughput experiments, high-dimensional data) and 5x to 7x (Bioconductor, functional genomics case studies).
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]], courses "Bioconductor for Genomic Data Science" and "Statistics for Genomic Data Science".
[^coursera]: [[Coursera UCSD - Bioinformatics Specialization]], course V "Genomic Data Science and Clustering".
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Networks" part.
[^bh]: [[Benjamini 1995 - Controlling the False Discovery Rate]].
