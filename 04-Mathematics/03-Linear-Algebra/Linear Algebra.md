---
aliases:
  - Matrix Algebra
  - Algèbre linéaire
tags:
  - type/moc
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Mathematical Foundations]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
---

# Linear Algebra

> [!abstract]
> Vectors, matrices and the linear maps between them: solving $Ax = b$, projections and least squares, eigenvalues, and the singular value decomposition that sits under most of omics data analysis.

## Why it matters for bioinformatics

- An omics dataset **is** a matrix (genes by samples, cells by genes). Normalization, distances, regression and dimensionality reduction are matrix operations.
- **Eigenvectors** give the axes of [[Principal Component Analysis]] of expression data, the stationary distribution of a [[Markov Chain]], the growth rate of a structured population and the stability of a steady state.
- **Least squares** is linear regression; the **SVD** is PCA, low-rank denoising and the basis of many latent-factor methods; the **matrix exponential** $e^{Qt}$ gives substitution probabilities in phylogenetics.

## Before you start

- [[Mathematical Foundations]]: [[Set]], [[Function]], [[Summation Notation]], [[Complex Number]] (for complex eigenvalues).
- Programming arrays: [[Array]] ([[Data Structures]]), [[N-Dimensional Array]] ([[Programming]]); practice every concept in NumPy after doing it once by hand.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Vector]] (L1): add vectors, scale them, form linear combinations; see them as points and arrows. Bio: the expression profile of a gene across samples; the k-mer count vector of a genome.
2. [[Dot Product]] (L1): compute $u \cdot v$, angles and cosine similarity. Bio: similarity of two expression profiles or two k-mer spectra.
3. [[Vector Norm]] (L1): compute Euclidean ($L_2$), Manhattan ($L_1$) and maximum norms. Bio: distances between samples; the $L_1$ and $L_2$ penalties of lasso and ridge regression.
4. [[Matrix]] (L1): read a matrix as a table, as columns and as a map; transpose it. Bio: count matrices, distance matrices, substitution matrices, transition matrices.
5. [[Matrix Multiplication]] (L1): multiply by rows, columns and blocks; know it is associative but not commutative. Bio: one step of a Markov chain $p_{t+1} = p_t P$; PAM250 as the 250th power of PAM1.
6. [[System of Linear Equations]] (L1): write a problem as $Ax = b$ and interpret solutions geometrically. Bio: steady-state fluxes $Sv = 0$; estimating cell-type proportions of a bulk sample (deconvolution).
7. [[Gaussian Elimination]] (L1): reduce to echelon form, detect no or infinitely many solutions.
8. [[Inverse Matrix]] (L1): compute $A^{-1}$, know when it exists and why numerical code avoids it. Bio: the normal equations of regression $(X^\top X)^{-1} X^\top y$.

### Stage 2 - Core (L2)

9. [[LU Decomposition]] (L2): factor $A = LU$ and solve many right-hand sides cheaply; what numerical libraries actually do.
10. [[Symmetric Matrix]] (L2): recognize $A = A^\top$ and form $A^\top A$. Bio: covariance and distance matrices are symmetric.
11. [[Vector Space]] (L2): check the axioms; work with subspaces and spans.
12. [[Linear Independence]] (L2): test whether vectors are independent. Bio: collinear predictors, such as batch fully confounded with condition, make a model non-identifiable.
13. [[Basis and Dimension]] (L2): find a basis, count dimensions, change coordinates.
14. [[Matrix Rank]] (L2): compute the rank and relate it to solvability. Bio: a rank-deficient design matrix; the low effective rank of expression data.
15. [[Fundamental Theorem of Linear Algebra]] (L2): relate column space, null space, row space and left null space and their dimensions. Bio: the null space of a stoichiometric matrix is the space of steady-state fluxes used by [[Flux Balance Analysis]]; its left null space gives conserved moieties.
16. [[Linear Transformation]] (L2): represent a linear map by a matrix in a chosen basis; compose maps. Bio: rotating data into principal-component coordinates.
17. [[Orthogonal Projection]] (L2): project onto a line and a subspace with $P = A(A^\top A)^{-1}A^\top$. Bio: fitted values of a regression; removing a known batch effect by projecting it out.
18. [[Least Squares]] (L2): solve overdetermined systems by minimizing $\lVert Ax - b \rVert^2$. Bio: fitting a qPCR standard curve; [[Linear Regression]].
19. [[Gram-Schmidt Process]] (L2): build an orthonormal basis; use orthogonal matrices.
20. [[QR Decomposition]] (L2): factor $A = QR$ and solve least squares stably. Bio: how regression software fits linear models.
21. [[Determinant]] (L2): compute it, use it to test invertibility and as a volume scale factor. Bio: the $\lvert \det J \rvert$ term when transforming a density.
22. [[Eigenvalues and Eigenvectors]] (L2): solve $Av = \lambda v$ through the characteristic polynomial; interpret eigenvectors as invariant directions. Bio: PCA of expression data; the stationary distribution of a Markov chain (eigenvalue 1); stability of a steady state.
23. [[Diagonalization]] (L2): write $A = V \Lambda V^{-1}$ and compute $A^k$. Bio: long-run behavior of a Markov chain or of repeated substitution.

### Stage 3 - Advanced (L3)

24. [[Spectral Theorem]] (L3): diagonalize a symmetric matrix with an orthonormal eigenbasis. Bio: why principal components of a covariance matrix are orthogonal; spectral clustering of networks.
25. [[Positive Definite Matrix]] (L3): test positive definiteness (eigenvalues, pivots, energy $x^\top A x$) and use the Cholesky factorization. Bio: valid covariance matrices; the Hessian at a likelihood maximum; simulating correlated traits.
26. [[Singular Value Decomposition]] (L3): factor any matrix as $U \Sigma V^\top$ and read the singular values. Bio: PCA of a centered count matrix computed via the SVD; pseudoinverse.
27. [[Low-Rank Approximation]] (L3): truncate the SVD and bound the error (Eckart-Young). Bio: denoising and compressing single-cell matrices; imputation; latent factors.
28. [[Matrix Exponential]] (L3): compute $e^{At}$ and solve $x' = Ax$. Bio: transition probabilities $P(t) = e^{Qt}$ of nucleotide substitution models; linear compartment models.
29. [[Perron-Frobenius Theorem]] (L3): state the dominant positive eigenvector of a positive (or irreducible nonnegative) matrix. Bio: uniqueness of the stationary distribution; the growth rate of a Leslie population model; network centrality.

> [!tip] Order of study
> Stages 1 and 2 follow Units I and II of MIT 18.06SC and belong to curriculum Stage 2. Take Stage 3 (Unit III, then the SVD lectures of 18.065) at the start of curriculum Stage 3, right before [[Multivariate Analysis]] and [[Differential Equations]] systems.

## Uses from other domains

- [[Principal Component Analysis]], [[Distance Matrix]] ([[Multivariate Analysis]]): eigenvectors and SVD of data matrices.
- [[Markov Chain]] ([[Stochastic Processes]]): transition matrices, powers and stationary distributions.
- [[Linear Regression]] ([[Linear Models]]): least squares and projections.
- [[Substitution Matrix]] ([[Sequence Analysis]]) and [[Nucleotide Substitution Model]] ([[Phylogenetics]]): matrix powers and $e^{Qt}$.
- [[Stoichiometric Matrix]], [[Flux Balance Analysis]] ([[Systems Biology]]): null space of the stoichiometric matrix, then [[Linear Programming]].
- [[Vectorization]], [[Floating-Point Arithmetic]], [[Numerical Linear Algebra]], [[Sparse Matrix]] ([[Scientific Computing]]): how matrix code runs fast, why it can be inaccurate, and how large sparse count matrices are stored.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.06SC - Linear Algebra]] | MIT | L1-L2 | Unit I "Ax = b and the Four Subspaces" (systems, elimination, vector spaces, subspaces); Unit II "Least Squares, Determinants and Eigenvalues" (projections to diagonalization); Unit III "Positive Definite Matrices and Applications" (symmetric and positive definite matrices, linear transformations, SVD)[^1806] |
| [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]] | MIT | L3 | Lecture 6 "Singular Value Decomposition"; matrix methods for data (SVD, low-rank approximation)[^18065] |
| [[MIT 18.03SC - Differential Equations]] | MIT | L2 | Unit IV "First Order Systems", where eigenvalues solve $x' = Ax$ (matrix exponential)[^1803] |

## Reference books

- [[Introduction to Linear Algebra (Strang)]]: the textbook of 18.06; elimination and subspaces for Stages 1-2, least squares, eigenvalues and SVD for Stages 2-3, final chapters on learning from data.[^strang]
- [[Linear Algebra Done Right (Axler)]]: proof-based second pass on vector spaces, linear maps, eigenvalues, inner product spaces, spectral theorem and SVD (Stage 3).[^axler]

## Lab projects

- [[07-evolution-simulator]]: the Wright-Fisher model as a transition matrix; powers of that matrix.
- [[08-phylogenetic-engine]]: distance matrices; substitution rate matrices and $e^{Qt}$ for likelihood methods.

## References

[^1806]: [[MIT 18.06SC - Linear Algebra]]: three units, in this order, whose titles are verified; they set the overall order of the learning path (linear transformations are moved earlier, as in Axler).
[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], lecture 6.
[^1803]: [[MIT 18.03SC - Differential Equations]], Unit IV: autonomous 2x2 linear systems and phase portraits.
[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed.
[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed.

Scope check: linear algebra is required in computational programs (MIT 6-7 requires Linear Algebra and Optimization;[^mit67] Tsinghua's biology degree requires a 4-credit Linear Algebra course[^thu]) and matrix algebra appears in first-year mathematics for biologists at Cambridge.[^cam] The weight given here (29 concepts, to L3) reflects its role in [[Multivariate Analysis]] and [[Statistical Learning]].

[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]], mathematics and introductory CS block.
[^thu]: [[Tsinghua University - BS Biological Sciences]], mathematics block.
[^cam]: [[University of Cambridge - Natural Sciences Tripos]], Part IA Mathematical Biology.
