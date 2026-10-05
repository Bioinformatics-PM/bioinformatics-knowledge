---
aliases:
  - Multivariate Statistics
  - Unsupervised Learning Methods
  - Analyse multivariée
tags:
  - type/moc
  - domain/statistics
  - domain/mathematics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Linear Algebra]]"
  - "[[Probability]]"
  - "[[Descriptive Statistics]]"
projects:
  - "[[08-phylogenetic-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Stanford - Statistical Learning with Python]]"
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[MIT 6.047 - Computational Biology]]"
---

# Multivariate Analysis

> [!abstract]
> Analyzing many variables at once: covariance, distances and similarity, clustering, and dimensionality reduction from PCA to the nonlinear embeddings used for single-cell data.

## Why it matters for bioinformatics

- Omics data have **thousands of variables per sample**. PCA, clustering and heatmaps are the first analyses of almost every expression, methylation or genotype dataset.
- **Distances** are the common currency: between sequences (input to phylogenetic trees), between samples (quality control, batch detection), between genomes (k-mer Jaccard similarity), between microbial communities.
- Single-cell analysis is multivariate analysis at scale: normalization, PCA, a neighbor graph, graph-based clustering and a UMAP embedding.

## Before you start

- [[Linear Algebra]]: [[Eigenvalues and Eigenvectors]], [[Spectral Theorem]], [[Singular Value Decomposition]], [[Positive Definite Matrix]].
- [[Probability]]: [[Covariance]], [[Multivariate Normal Distribution]].
- [[Descriptive Statistics]]: [[Standard Score]], [[Correlation]], [[Data Transformation]], [[Heatmap]].
- [[Discrete Mathematics]]: [[Graph]] (for item 18).

## Learning path

### Stage 2 - Core (L2)

1. [[Covariance Matrix]] (L2): compute the sample covariance and correlation matrices of a data matrix. Bio: gene-gene co-expression; the linkage disequilibrium matrix between SNPs.
2. [[Distance Metric]] (L2): check the metric axioms; choose Euclidean, Manhattan, correlation or Hamming distances. Bio: the choice of distance changes which samples cluster together.
3. [[Distance Matrix]] (L2): compute and store all pairwise distances. Bio: the input of UPGMA and neighbor joining; sample-to-sample distances for quality control.
4. [[Jaccard Index]] (L2): measure set similarity. Bio: k-mer set similarity between genomes, estimated at scale with MinHash sketches.
5. [[Clustering]] (L2): state the goal of grouping without labels and the families of methods. Bio: grouping genes by expression pattern and cells by type.
6. [[Hierarchical Clustering]] (L2): build dendrograms with single, complete and average linkage. Bio: clustered heatmaps; average linkage on a distance matrix is UPGMA.
7. [[K-Means Clustering]] (L2): run Lloyd's algorithm, choose $k$ and know its assumptions. Bio: partitioning cells or expression profiles.
8. [[Dimensionality Reduction]] (L2): explain why and how to project high-dimensional data to a few axes. Bio: 20,000 genes summarized by a handful of components.
9. [[Principal Component Analysis]] (L2): compute principal components by eigen-decomposition or SVD, read scree plots, loadings and biplots. Bio: batch and condition effects in RNA-seq; population structure from genotypes.

### Stage 3 - Advanced (L3)

10. [[Mahalanobis Distance]] (L3): measure distance while accounting for correlations. Bio: multivariate outlier samples.
11. [[Cluster Validation]] (L3): assess clusters with silhouette width, stability and external labels. Bio: how many cell types does the data support?
12. [[Multidimensional Scaling]] (L3): embed a distance matrix in few dimensions (principal coordinates analysis). Bio: beta-diversity ordination of microbial communities.
13. [[Correspondence Analysis]] (L3): analyze contingency tables in a low-dimensional map. Bio: codon usage across genes; species abundance across sites.
14. [[Canonical Correlation Analysis]] (L3): find maximally correlated combinations of two variable sets. Bio: relating expression and methylation in multi-omics integration.
15. [[Non-Negative Matrix Factorization]] (L3): factor a nonnegative matrix into parts. Bio: mutational signatures of cancer genomes; metagenes.

### Stage 4 - Frontier (M1)

16. [[t-Distributed Stochastic Neighbor Embedding]] (M1): produce a nonlinear 2D embedding and know what it distorts. Bio: visualizing single-cell clusters (distances between clusters are not meaningful).
17. [[Uniform Manifold Approximation and Projection]] (M1): compute UMAP embeddings and tune neighbors and minimum distance. Bio: the standard single-cell visualization.
18. [[Graph-Based Clustering]] (M1): cluster a k-nearest-neighbor graph by community detection (Louvain, Leiden). Bio: cell-type clustering in single-cell pipelines.
19. [[Compositional Data Analysis]] (M1): analyze relative abundances with log-ratio transforms. Bio: microbiome profiles, where only proportions are observed.

> [!tip] Order of study
> Learn PCA (item 9) right after the SVD in [[Linear Algebra]], by computing it by hand on a small expression matrix before using a library. Items 16 to 19 belong to curriculum Stage 4 with [[Transcriptomics]].

## Uses from other domains

- [[UPGMA]], [[Neighbor Joining]], [[Phylogenetic Tree]] ([[Phylogenetics]]): tree building from a distance matrix.
- [[Hamming Distance]], [[Edit Distance]] ([[String Algorithms]]): distances between sequences.
- [[Population Structure]] ([[Population Genomics]]): PCA of genotypes.
- [[Metagenomics]] ([[Genomics]]): k-mer similarity, ordination, compositional data.
- [[Single-Cell Clustering]] ([[Transcriptomics]]): PCA, neighbor graphs, clustering and embeddings of single-cell data.
- [[Multi-Omics Integration]] ([[Systems Biology]]): canonical correlation and matrix factorization across data types.
- [[Graph Laplacian]] ([[Discrete Mathematics]]): spectral clustering.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Stanford - Statistical Learning with Python]] | Stanford Online | L3 | Unsupervised part: principal components, k-means and hierarchical clustering (items 5-9)[^slp] |
| [[MIT 18.650 - Statistics for Applications]] | MIT | L3 | Principal component analysis, from the statistical side (item 9)[^18650] |
| [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]] | MIT | L3 | Lecture 6 "Singular Value Decomposition", the computation behind PCA[^18065] |
| [[HarvardX PH525x - Data Analysis for the Life Sciences]] | Harvard (edX) | L3 | High-dimensional data analysis on genomics data (items 1-9)[^ph525] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | Clustering and classification of gene expression[^6047] |

## Reference books

- [[Modern Statistics for Modern Biology (Holmes)]]: mixture models, clustering and multivariate analysis on biological data (Stages 2-3).[^msmb]
- [[An Introduction to Statistical Learning (James)]]: chapter 12 (unsupervised learning: PCA, k-means, hierarchical clustering).[^isl]

## Lab projects

- [[08-phylogenetic-engine]]: distance matrices; UPGMA as average-linkage hierarchical clustering.
- [[bio-algorithms]]: a reusable distance-matrix implementation.

## References

[^slp]: [[Stanford - Statistical Learning with Python]], unsupervised part.
[^18650]: [[MIT 18.650 - Statistics for Applications]], dimension-reduction part.
[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], lecture 6.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.2x to 4x (high-dimensional data analysis).
[^6047]: [[MIT 6.047 - Computational Biology]], networks part.
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], exploration and structure part.
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition; chapter number checked against the official ISLP lab notebooks (Ch12 unsupervised).
