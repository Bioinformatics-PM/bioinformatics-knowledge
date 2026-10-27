---
aliases:
  - Symmetric Matrices
  - Gram Matrix
  - Skew-Symmetric Matrix
  - Symmetric Part
  - Matrice symétrique
tags:
  - type/concept
  - domain/mathematics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Matrix]]"
  - "[[Matrix Multiplication]]"
  - "[[Dot Product]]"
  - "[[Inverse Matrix]]"
related:
  - "[[Covariance Matrix]]"
  - "[[Distance Matrix]]"
  - "[[Correlation]]"
  - "[[Adjacency Matrix]]"
  - "[[Substitution Matrix]]"
  - "[[LU Decomposition]]"
  - "[[Positive Definite Matrix]]"
  - "[[Spectral Theorem]]"
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Principal Component Analysis]]"
  - "[[Nucleotide Substitution Model]]"
  - "[[Detailed Balance]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Saitou 1987 - The Neighbor-Joining Method]]"
  - "[[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]]"
  - "[[Barabási 2004 - Network Biology]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Symmetric Matrix

> [!abstract]
> A symmetric matrix equals its transpose, $A = A^\top$: entry $(i, j)$ equals entry $(j, i)$, so the matrix is its own mirror image across the diagonal. Tables of symmetric pairwise relations (distances, covariances, undirected interactions) are symmetric, and so is every product $A^\top A$.

## Definition

A square matrix $A$ is **symmetric** if $A^\top = A$, that is, $a_{ij} = a_{ji}$ for all $i$ and $j$.[^strang] The diagonal and one triangle determine it: an $n \times n$ symmetric matrix has $n(n+1)/2$ free entries. A matrix with $K^\top = -K$ is **skew-symmetric** (antisymmetric); its diagonal is zero, since $k_{ii} = -k_{ii}$.

## Why it matters

- **Pairwise tables of symmetric relations.** A distance matrix, the input of neighbor joining, is symmetric because $d(i, j) = d(j, i)$ ([[Distance Matrix]]).[^saitou] BLOSUM62 gives one score to each unordered pair of amino acids, 210 scores for 20 amino acids ($20 \cdot 21/2$), so the score matrix is symmetric ([[Substitution Matrix]]).[^henikoff] Covariance and correlation matrices are symmetric because $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$ ([[Covariance Matrix]], [[Correlation]]).[^blitzstein] In an undirected network, such as a protein interaction network, a link has no direction and the [[Adjacency Matrix]] is symmetric; a regulatory network, whose links point from regulator to target, is directed and its matrix is not.[^barabasi]
- **Checks, storage, speed.** Symmetry is a free invariant to assert on every computed distance or covariance matrix (an asymmetric one reveals a bug or misaligned labels); it halves storage (SciPy's `pdist` returns only the $n(n-1)/2$ distances above the diagonal, code below); and it unlocks dedicated algorithms such as `eigh` for eigenvalues and Cholesky for solving ([[LU Decomposition#Advanced (L3)]]). In [[08-phylogenetic-engine]], assert symmetry and a zero diagonal on each distance matrix before building a tree.
- **Real spectra.** A real symmetric matrix has real eigenvalues and orthogonal eigenvectors ([[Spectral Theorem]], L3).[^strang][^1806] This is why the principal components of a covariance matrix are real, mutually orthogonal directions ([[Principal Component Analysis]]).

## Core (L2)

### Recognizing symmetry

- Compare $a_{ij}$ with $a_{ji}$ for the $n(n-1)/2$ pairs above the diagonal; the diagonal is unconstrained. Only a square matrix can be symmetric.
- $\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$ is symmetric. The transition matrix $\begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix}$ of [[Matrix]] is not: moving from state 1 to state 2 need not be as likely as the reverse.

![[symmetric-matrix-condensed-storage.svg]]

### Where symmetric matrices come from

1. **Gram matrices.** For any $m \times n$ matrix $A$, $(A^\top A)^\top = A^\top (A^\top)^\top = A^\top A$, using $(AB)^\top = B^\top A^\top$ ([[Matrix Multiplication]]).[^strang] Entry $(i, j)$ of $A^\top A$ is the [[Dot Product]] of columns $i$ and $j$, and $a_i \cdot a_j = a_j \cdot a_i$. For a genes × samples matrix $X$, $X^\top X$ (samples × samples) and $XX^\top$ (genes × genes) are two different symmetric matrices built from the same data.
2. **Covariance matrices.** Center each variable, then the sample covariance matrix is $S = \frac{1}{n-1}X_c^\top X_c$ for $n$ observations in the rows of $X_c$: a Gram matrix up to a factor, with variances on the diagonal and covariances off it ([[Covariance Matrix]], [[Variance]]).
3. **Distance and similarity matrices** of a symmetric measure: any [[Vector Norm]] distance, correlation, alignment identity. For Euclidean distances, $d_{ij}^2 = g_{ii} + g_{jj} - 2g_{ij}$, where $G$ is the Gram matrix of the points (Exercise 5).
4. **Symmetrization.** For any square $A$, $\tfrac12(A + A^\top)$ is symmetric, $\tfrac12(A - A^\top)$ is skew-symmetric, and $A$ is their sum. Averaging a similarity measured in both directions, or turning a directed graph into an undirected one with $A + A^\top$, uses this.

### Algebra

- Sums, scalar multiples and powers of symmetric matrices are symmetric: symmetric matrices form a subspace of $\mathbb{R}^{n \times n}$, of dimension $n(n+1)/2$ ([[Vector Space]], [[Basis and Dimension]]).
- If $A$ is symmetric and invertible, so is $A^{-1}$: $(A^{-1})^\top = (A^\top)^{-1} = A^{-1}$ ([[Inverse Matrix]]).
- **Products need care.** For symmetric $A$ and $B$, $(AB)^\top = B^\top A^\top = BA$, so $AB$ is symmetric only when $AB = BA$ (code below).
- **Congruence preserves symmetry.** $C^\top A C$ is symmetric for any $C$ of compatible size. For a random vector $x$ with covariance matrix $\Sigma$, the covariance matrix of $Cx$ is $C\Sigma C^\top$, and the variance of a weighted sum $w^\top x$ is $w^\top \Sigma w$ (Exercise 4).[^blitzstein]
- **Quadratic forms only see the symmetric part.** For skew-symmetric $K$, the number $x^\top K x$ equals its own transpose $x^\top K^\top x = -x^\top K x$, so it is 0, and $x^\top A x = x^\top \tfrac12(A + A^\top)\,x$. Quadratic forms $x^\top A x$ are therefore always written with a symmetric $A$ ([[Positive Definite Matrix]]).

### Symmetric elimination: $A = LDL^\top$

If a symmetric $A$ needs no row exchanges, its LU factors are related: $U = DL^\top$, with $D$ the diagonal matrix of pivots, so $A = LDL^\top$ and only $L$ and $D$ need storing ([[LU Decomposition]]).[^strang] Example: $A = \begin{pmatrix} 2 & 4 \\ 4 & 11 \end{pmatrix}$ has $\ell_{21} = 2$ and $U = \begin{pmatrix} 2 & 4 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = DL^\top$.

## Advanced (L3)

### Eigenvalues: use the symmetric solver

The [[Spectral Theorem]] (Stage 3) factors a real symmetric matrix as $A = Q\Lambda Q^\top$, with real eigenvalues in $\Lambda$ and orthonormal eigenvectors in $Q$.[^strang] Libraries have dedicated routines: `np.linalg.eigh` returns real eigenvalues in ascending order and orthonormal eigenvectors (code below). Two consequences:

- **Covariance matrices have no negative eigenvalues.** $w^\top S w = \frac{1}{n-1}\lVert X_c w \rVert^2 \ge 0$ for every $w$: $S$ is positive semidefinite ([[Positive Definite Matrix]]), and the variances along principal components are $\ge 0$.
- **`eigh` trusts you.** It reads one triangle only; given a matrix that is not symmetric, it silently answers for another one:

```python
import numpy as np
M = np.array([[1.0, 3.0], [1.0, 1.0]])     # NOT symmetric
print(np.linalg.eigvals(M).round(3), np.linalg.eigh(M)[0].round(3))
```

```text
[ 2.732 -0.732] [0. 2.]
```

The eigenvalues of $M$ are $1 \pm \sqrt3$; `eigh` returned those of $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, built from the lower triangle. Assert symmetry first (with a tolerance for floats), or symmetrize with $\tfrac12(S + S^\top)$ when round-off has made a matrix that should be symmetric very slightly asymmetric.

### Reversible substitution models

A nucleotide rate matrix $Q$ (off-diagonal rates $q_{ij} \ge 0$, rows summing to 0) is generally not symmetric. A model is **time-reversible** when $\pi_i q_{ij} = \pi_j q_{ji}$ for its stationary distribution $\pi$, that is, when $\Pi Q$ is symmetric, with $\Pi = \operatorname{diag}(\pi)$ ([[Detailed Balance]]). The general time-reversible model writes $q_{ij} = s_{ij}\pi_j$ with symmetric exchangeabilities $s_{ij} = s_{ji}$. Then $\Pi^{1/2} Q\, \Pi^{-1/2}$ is symmetric, so $Q$ has real eigenvalues, and $e^{Qt}$ can be computed with a symmetric eigensolver, a standard route to the substitution probabilities of likelihood methods ([[Nucleotide Substitution Model]], [[Matrix Exponential]]).[^yang]

```python
import numpy as np
pi = np.array([0.1, 0.2, 0.3, 0.4])        # invented base frequencies (A, C, G, T)
s = np.array([[0, 1, 4, 1],                # invented symmetric exchangeabilities:
              [1, 0, 1, 4],                # transitions (A-G, C-T) 4 times faster
              [4, 1, 0, 1],
              [1, 4, 1, 0]], dtype=float)
Q = s * pi                                 # q_ij = s_ij * pi_j for i != j
np.fill_diagonal(Q, -Q.sum(axis=1))        # rows of a rate matrix sum to 0
Pi = np.diag(pi)
print(np.allclose(Q, Q.T), np.allclose(Pi @ Q, (Pi @ Q).T), np.allclose(pi @ Q, 0))
Bs = np.diag(pi ** 0.5) @ Q @ np.diag(pi ** -0.5)
print(np.allclose(Bs, Bs.T), np.linalg.eigvalsh(Bs).round(4))
```

```text
False True True
True [-2.8 -2.2 -1.   0. ]
```

$Q$ is not symmetric, but $\Pi Q$ is, $\pi$ is stationary ($\pi Q = 0$), and the symmetrized matrix has the real eigenvalues $0$ (the stationary distribution) and three negative rates of decay toward it.

## Mathematical representation

- $\mathrm{Sym}_n = \{A \in \mathbb{R}^{n \times n} : A^\top = A\}$ has dimension $n(n+1)/2$; $\mathrm{Skew}_n = \{K : K^\top = -K\}$ has dimension $n(n-1)/2$; every $A$ splits uniquely as $A = \tfrac12(A + A^\top) + \tfrac12(A - A^\top)$, and the dimensions add up to $n^2$.
- **Gram matrix** of the columns $a_1, \dots, a_n$ of $A$: $G = A^\top A$, $g_{ij} = a_i^\top a_j$, and $x^\top G x = \lVert Ax \rVert^2 \ge 0$.
- **Centering.** $H = I_n - \frac1n \mathbf{1}\mathbf{1}^\top$ is symmetric with $H^2 = H$; for $X \in \mathbb{R}^{n \times p}$ (observations in rows), $X_c = HX$ and $S = \frac{1}{n-1}X^\top H X$.
- **Linear maps of random vectors.** With $\Sigma = \mathbb{E}\big[(x - \mu)(x - \mu)^\top\big]$, $\operatorname{Cov}(Cx) = \mathbb{E}\big[C(x - \mu)(x - \mu)^\top C^\top\big] = C\Sigma C^\top$.[^blitzstein]
- **Squared distances** between points $x_1, \dots, x_n$ with Gram matrix $G_{ij} = x_i^\top x_j$ and $\mathbf{g} = \operatorname{diag}(G)$: $D^{(2)} = \mathbf{g}\mathbf{1}^\top + \mathbf{1}\mathbf{g}^\top - 2G$, symmetric with zero diagonal.
- **Reversibility.** $\Pi Q = (\Pi Q)^\top \iff \Pi^{1/2} Q\, \Pi^{-1/2}$ is symmetric.

## Computational representation

```python
def is_symmetric(A, tol=0.0):
    """Square, and a_ij = a_ji within tol (only the upper triangle needs checking)."""
    n = len(A)
    return all(len(row) == n for row in A) and all(
        abs(A[i][j] - A[j][i]) <= tol for i in range(n) for j in range(i + 1, n))

def transpose(A):
    return [list(col) for col in zip(*A)]

def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

def covariance_matrix(X):
    """Covariances between the rows of X (variables x observations), divisor n - 1."""
    n = len(X[0])
    centered = [[v - sum(row) / n for v in row] for row in X]
    return [[sum(a * b for a, b in zip(u, w)) / (n - 1) for w in centered] for u in centered]

X = [[10, 0, 5, 7],      # invented counts, genes x samples (the Matrix note's table)
     [3, 8, 1, 0],
     [0, 2, 4, 6]]
G = matmul(transpose(X), X)            # 4 x 4: dot products between samples
S = covariance_matrix(X)               # 3 x 3: covariances between genes
print(G)
print([[round(v, 3) for v in row] for row in S])
print(is_symmetric(G), is_symmetric(S, tol=1e-12), is_symmetric([[1, 2], [3, 1]]))

A = [[1, 2], [2, 3]]
B = [[0, 1], [1, 0]]                   # two symmetric matrices
print(matmul(A, B), is_symmetric(matmul(A, B)))

import numpy as np
from scipy.spatial.distance import pdist, squareform

Xn = np.array(X, dtype=float)
print(np.allclose(S, np.cov(Xn)))      # np.cov treats rows as variables
d = pdist(Xn.T)                        # condensed: the 6 distances between the 4 samples
print(d.round(2), squareform(d).shape)
w, V = np.linalg.eigh(np.cov(Xn))      # symmetric eigensolver: real, ascending
print(w.round(3), np.allclose(V.T @ V, np.eye(3)))
```

```text
[[109, 24, 53, 70], [24, 68, 16, 12], [53, 16, 42, 59], [70, 12, 59, 85]]
[[17.667, -10.333, -1.333], [-10.333, 12.667, -5.333], [-1.333, -5.333, 6.667]]
True True False
[[2, 1], [3, 2]] False
True
[11.36  6.71  7.35  8.83 11.36  3.  ] (4, 4)
[ 0.393 10.531 26.076] True
```

The symmetry test needs a tolerance as soon as entries are floats. `np.cov` treats each row as a variable, as the match with `S` shows; for a samples × genes table, transpose it first (or pass `rowvar=False`). `pdist` returns the condensed vector of the figure, here the 6 sample distances of the [[Matrix]] note, and `squareform` rebuilds the full $4 \times 4$ matrix.

## Worked example

> [!example] Gene-gene covariance from a small count table (invented data)
> Genes A, B, C measured in 4 samples: rows $(10, 0, 5, 7)$, $(3, 8, 1, 0)$, $(0, 2, 4, 6)$.
> 1. **Center each gene.** Means $5.5$, $3$, $3$; centered rows $a = (4.5, -5.5, -0.5, 1.5)$, $b = (0, 5, -2, -3)$, $c = (-3, -1, 1, 3)$.
> 2. **Diagonal** (variances, divisor $n - 1 = 3$): $a \cdot a = 53$, $b \cdot b = 38$, $c \cdot c = 20$, giving $17.667$, $12.667$, $6.667$.
> 3. **Off-diagonal** (covariances): $a \cdot b = 0 - 27.5 + 1 - 4.5 = -31$, $a \cdot c = -13.5 + 5.5 - 0.5 + 4.5 = -4$, $b \cdot c = 0 - 5 - 2 - 9 = -16$. Each is computed once and written in two places:
> $$S = \frac13\begin{pmatrix} 53 & -31 & -4 \\ -31 & 38 & -16 \\ -4 & -16 & 20 \end{pmatrix}.$$
> 4. **Read it.** Genes A and B vary in opposite directions across these samples: correlation $-31/\sqrt{53 \cdot 38} \approx -0.691$ ([[Correlation]]).
> 5. **Check.** $S = S^\top$, and its eigenvalues $0.393$, $10.531$, $26.076$ (code above) are real and nonnegative, as for any covariance matrix; here they are even positive, because the three centered gene rows are linearly independent. The sample Gram matrix $X^\top X$ printed above gives back the distance of the [[Matrix]] note: $d(S_1, S_2)^2 = 109 + 68 - 2 \cdot 24 = 129$, $d = 11.36$.

## Common misconceptions

> [!warning] "The product of two symmetric matrices is symmetric"
> Only when they commute. $\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$ is not symmetric. Sums and powers, by contrast, always are.

> [!warning] "$A^\top A$ and $AA^\top$ are the same matrix"
> For a genes × samples $X$, $X^\top X$ is samples × samples and $XX^\top$ genes × genes: different sizes and meanings. They do share their nonzero eigenvalues: if $A^\top A v = \lambda v$ with $\lambda \ne 0$, then $AA^\top (Av) = \lambda (Av)$ and $Av \ne 0$. PCA can therefore work with whichever of the two is smaller ([[Singular Value Decomposition]]).

> [!warning] "Every table of pairwise values is symmetric"
> Directed relations are not: transition matrices, regulatory networks, substitution rate matrices, similarity scores computed in one direction only. Check before using tools that assume symmetry (`eigh`, Cholesky, condensed storage), which do not complain.

> [!warning] "A matrix that is symmetric on paper is symmetric in memory"
> Two mathematically equal entries computed by different sequences of floating-point operations can differ in the last digits ([[Floating-Point Arithmetic]]). Exact `==` tests then fail; compare with a tolerance, and symmetrize before calling a symmetric solver.

## Exercises

> [!question] Exercise 1 (L2)
> Which are symmetric: (a) the $4 \times 4$ distance matrix of the figure; (b) $\begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix}$; (c) $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 6 \\ 3 & 6 & 9 \end{pmatrix}$; (d) any $2 \times 3$ matrix? Then complete $\begin{pmatrix} 4 & ? & 1 \\ -2 & 0 & ? \\ ? & 5 & 7 \end{pmatrix}$ into a symmetric matrix.

> [!success]- Solution
> (a) Yes. (b) No: $0.1 \ne 0.3$. (c) Yes. (d) No: not square. The missing entries mirror their partners: $a_{12} = a_{21} = -2$, $a_{23} = a_{32} = 5$, $a_{31} = a_{13} = 1$.

> [!question] Exercise 2 (L2)
> Split $A = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix}$ into a symmetric and a skew-symmetric part, and check that $x^\top A x$ only depends on the symmetric part.

> [!success]- Solution
> $\tfrac12(A + A^\top) = \begin{pmatrix} 1 & 3 \\ 3 & 3 \end{pmatrix}$ and $\tfrac12(A - A^\top) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Then $x^\top A x = x_1^2 + 4x_1x_2 + 2x_2x_1 + 3x_2^2 = x_1^2 + 6x_1x_2 + 3x_2^2$, the same as with the symmetric part, while the skew part gives $x_1x_2 - x_2x_1 = 0$.

> [!question] Exercise 3 (L2)
> Prove: (a) $A^\top A$ is symmetric with a nonnegative diagonal; (b) the inverse of an invertible symmetric matrix is symmetric; (c) for symmetric $A$ and $B$, $AB$ is symmetric if and only if $AB = BA$.

> [!success]- Solution
> (a) $(A^\top A)^\top = A^\top A$, and $(A^\top A)_{ii} = a_i \cdot a_i = \lVert a_i \rVert^2 \ge 0$. (b) $(A^{-1})^\top = (A^\top)^{-1} = A^{-1}$, using $(A^{-1})^\top A^\top = (AA^{-1})^\top = I$. (c) $(AB)^\top = B^\top A^\top = BA$, which equals $AB$ exactly when the two commute.

> [!question] Exercise 4 (L3, Python)
> With the covariance matrix $S$ of the worked example, compute the variance of the summed expression of genes A and B as $w^\top S w$ for $w = (1, 1, 0)$, and check it against the variance of the summed rows.

> [!success]- Solution
> $w^\top S w = s_{AA} + s_{BB} + 2s_{AB} = (53 + 38 - 62)/3 = 29/3 \approx 9.667$. With `Xn` from the code above:
> ```python
> Sn = np.cov(Xn)
> w2 = np.array([1.0, 1.0, 0.0])             # expression of gene A + gene B
> print(round(w2 @ Sn @ w2, 3), round(np.var(Xn[0] + Xn[1], ddof=1), 3))
> # 9.667 9.667
> ```
> The negative covariance makes the sum less variable than the two genes separately ($17.667 + 12.667$): their fluctuations partly cancel.

> [!question] Exercise 5 (L3, Python)
> Prove $d_{ij}^2 = g_{ii} + g_{jj} - 2g_{ij}$ for points with Gram matrix $G$, then compute all distances between the 4 samples from $X^\top X$ in one vectorized expression and compare with `pdist`.

> [!success]- Solution
> $\lVert x_i - x_j \rVert^2 = (x_i - x_j) \cdot (x_i - x_j) = x_i \cdot x_i + x_j \cdot x_j - 2\,x_i \cdot x_j$.
> ```python
> Gr = Xn.T @ Xn                             # Gram matrix of the samples (columns)
> g = np.diag(Gr)
> D2 = g[:, None] + g[None, :] - 2 * Gr      # all squared distances at once
> print(np.allclose(np.sqrt(np.maximum(D2, 0)), squareform(pdist(Xn.T))), np.allclose(D2, D2.T))
> # True True
> ```
> One matrix product replaces a double loop over pairs. `np.maximum(D2, 0)` guards against tiny negative values that round-off can produce on the diagonal.

> [!question] Exercise 6 (L3, Python)
> Test detailed balance for the general time-reversible $Q$ of the Advanced section and for the invented cyclic model $Q_2 = \begin{pmatrix} -1.5 & 1 & 0 & 0.5 \\ 0.5 & -1.5 & 1 & 0 \\ 0 & 0.5 & -1.5 & 1 \\ 1 & 0 & 0.5 & -1.5 \end{pmatrix}$ (A → C → G → T → A at rate 1, backwards at 0.5). First show that the uniform distribution is stationary for $Q_2$.

> [!success]- Solution
> The columns of $Q_2$ sum to 0, so $\mathbf{1}^\top Q_2 = 0$ and $\pi = (\tfrac14, \tfrac14, \tfrac14, \tfrac14)$ is stationary.
> ```python
> Q2 = np.array([[-1.5, 1.0, 0.0, 0.5],      # invented cyclic model A -> C -> G -> T -> A
>                [0.5, -1.5, 1.0, 0.0],
>                [0.0, 0.5, -1.5, 1.0],
>                [1.0, 0.0, 0.5, -1.5]])
> u = np.full(4, 0.25)
> print(np.allclose(u @ Q2, 0), np.allclose(np.diag(u) @ Q2, (np.diag(u) @ Q2).T))
> # True False
> ```
> The flux A → C, $\tfrac14 \cdot 1$, differs from C → A, $\tfrac14 \cdot 0.5$: the chain circulates around the cycle at equilibrium, so $\Pi Q_2$ is not symmetric and the symmetric shortcut does not apply. The time-reversible $Q$ passed the same test above.

## Mastery checklist

- [ ] 1 Recognized: I can tell whether a matrix is symmetric and name symmetric matrices of bioinformatics (distance, covariance, substitution score, undirected adjacency).
- [ ] 2 Understood: I can prove that $A^\top A$, $A^{-1}$ and $C^\top A C$ are symmetric when they should be, and explain why a product of symmetric matrices may not be.
- [ ] 3 Practiced: I can build Gram, covariance and distance matrices in code, test symmetry with a tolerance, and store a distance matrix in condensed form.
- [ ] 4 Applied: I checked the symmetry and zero diagonal of a real distance matrix in [[08-phylogenetic-engine]], and computed a covariance matrix of real expression data with its eigenvalues.
- [ ] 5 Explained: I can explain why symmetric matrices have real spectra and dedicated solvers, how `eigh` fails silently on asymmetric input, and how reversible substitution models are symmetrized.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit III "Positive Definite Matrices and Applications" (symmetric matrices).
[^blitzstein]: [[Introduction to Probability (Blitzstein)]], 2nd ed., covariance and joint distributions.
[^saitou]: [[Saitou 1987 - The Neighbor-Joining Method]], *Molecular Biology and Evolution* 4:406-425.
[^henikoff]: [[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]], *PNAS* 89:10915-10919.
[^barabasi]: [[Barabási 2004 - Network Biology]], *Nature Reviews Genetics* 5:101-113.
[^yang]: [[Molecular Evolution (Yang)]], models of nucleotide substitution (time reversibility and the general time-reversible model).
