---
aliases:
  - Matrices
  - Transpose
  - Matrix Transpose
  - Square Matrix
  - Identity Matrix
  - Matrice
  - Transposée
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Vector]]"
  - "[[Dot Product]]"
  - "[[Array]]"
  - "[[Function]]"
related:
  - "[[Matrix Multiplication]]"
  - "[[System of Linear Equations]]"
  - "[[Symmetric Matrix]]"
  - "[[Linear Transformation]]"
  - "[[Count Matrix]]"
  - "[[Distance Matrix]]"
  - "[[Substitution Matrix]]"
  - "[[Transition Matrix]]"
  - "[[N-Dimensional Array]]"
  - "[[Sparse Matrix]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Saitou 1987 - The Neighbor-Joining Method]]"
  - "[[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Dayhoff 1978 - A Model of Evolutionary Change in Proteins]]"
---

# Matrix

> [!abstract]
> A matrix is a rectangular table of numbers that can be read three ways: as a table of entries, as a row of column vectors, and as a machine that turns one vector into another; most biological data tables and models are matrices.

## Definition

An $m \times n$ **matrix** $A$ is a rectangular array of numbers with $m$ rows and $n$ columns; $a_{ij}$ is the entry in row $i$ and column $j$, and $\mathbb{R}^{m \times n}$ is the set of such real matrices.[^strang] Its **transpose** $A^\top$ is the $n \times m$ matrix with $(A^\top)_{ij} = a_{ji}$: rows become columns.[^strang] A matrix acts on vectors: $x \in \mathbb{R}^n$ is sent to $Ax \in \mathbb{R}^m$, the combination of the columns of $A$ with coefficients $x_1, \dots, x_n$.[^strang][^1806]

## Why it matters

Four matrices a bioinformatician meets in the first year, each with its own constraints:

| Matrix | Rows × columns | Entries | Structure |
|---|---|---|---|
| [[Count Matrix]] (RNA-seq) | genes × samples | read counts[^holmes] | nonnegative integers, usually rectangular |
| [[Distance Matrix]] | sequences × sequences | pairwise distances, the input of neighbor joining[^saitou] | square, symmetric, zero diagonal |
| [[Substitution Matrix]] (BLOSUM62) | amino acids × amino acids | log-odds scores for the 210 pairs of the 20 amino acids[^henikoff] | square, symmetric, negative and positive entries |
| [[Transition Matrix]] (Markov chain) | state × next state | $P(\text{next} = t \mid \text{current} = s)$[^durbin3] | square, nonnegative, rows sum to 1 |

Recognizing which kind of matrix you hold tells you which operations make sense: multiplying a transition matrix by itself is meaningful ([[Matrix Multiplication]]), multiplying two count matrices usually is not. In the Lab, [[08-phylogenetic-engine]] builds distance matrices and [[07-evolution-simulator]] uses the transition matrix of the [[Wright-Fisher Model]].

## Core (L1)

### Three readings

1. **A table.** $a_{ij}$ is one number: the count of gene $i$ in sample $j$. Row index first, always.
2. **Columns (or rows).** $A = [\,a_1 \; a_2 \; \cdots \; a_n\,]$ with each column $a_j \in \mathbb{R}^m$ a [[Vector]]: column $j$ of a count matrix is the profile of sample $j$; row $i$ is the profile of gene $i$.[^strang]
3. **A map.** $x \mapsto Ax = x_1 a_1 + \dots + x_n a_n$ turns an $n$-vector into an $m$-vector. Entry $i$ of $Ax$ is also the [[Dot Product]] of row $i$ with $x$ (row picture).[^strang][^1806]

![[matrix-vector-column-combination.svg]]

With the all-ones vector $\mathbf{1}$: $A\mathbf{1}$ adds the columns, giving the row sums (total count of each gene), and $A^\top \mathbf{1}$ gives the column sums (library size of each sample).

### Transpose

$(A^\top)_{ij} = a_{ji}$: an $m \times n$ matrix becomes $n \times m$, the first row becomes the first column. $(A^\top)^\top = A$ and $(A + B)^\top = A^\top + B^\top$.[^strang] A genes × samples table transposed is a samples × genes table: same data, other orientation. Tools disagree on which orientation they expect, so check before passing a matrix to a function.

### Special matrices

- **Square**: $m = n$. **Diagonal**: zero outside the diagonal $a_{11}, \dots, a_{nn}$.
- **Identity** $I$: ones on the diagonal, zeros elsewhere; $Ix = x$ for every $x$.
- **Symmetric**: $A^\top = A$, so necessarily square ([[Symmetric Matrix]]). Distance and substitution matrices are symmetric; transition matrices generally are not.
- **Zero matrix**: all entries 0.

## Deeper (L2)

**Matrices form a vector space.** Matrices of the same shape add entrywise and scale entrywise, with the same rules as vectors; $\mathbb{R}^{m \times n}$ is a vector space of dimension $mn$.[^axler] The entrywise (Hadamard) product is *not* the matrix product ([[Matrix Multiplication]]).

**Linearity of the map.** $A(cx + dy) = c\,Ax + d\,Ay$ for all vectors $x, y$ and scalars $c, d$.[^strang] Conversely, every linear map from $\mathbb{R}^n$ to $\mathbb{R}^m$ is $x \mapsto Ax$ for exactly one $m \times n$ matrix: its columns are the images of the basis vectors $e_1, \dots, e_n$ ([[Linear Transformation]]).[^axler]

**Constraints as checks.** The structures of the table above are testable invariants, useful as assertions in code:

- distance matrix: $D = D^\top$, $d_{ii} = 0$, $d_{ij} \ge 0$ (and the triangle inequality if it comes from a [[Vector Norm]]);
- transition matrix: $p_{st} \ge 0$ and $P\mathbf{1} = \mathbf{1}$ (each row is a probability distribution);[^durbin3]
- count matrix: integer entries $\ge 0$, column sums equal to the library sizes reported by the quantification tool.

**$A^\top A$ is always symmetric**, because $(A^\top A)^\top = A^\top (A^\top)^\top = A^\top A$ (using $(AB)^\top = B^\top A^\top$, [[Matrix Multiplication]]). For a centered data matrix it is, up to a factor, the covariance matrix, the starting point of [[Principal Component Analysis]].

## Advanced (L3)

- **A matrix is a linear map plus two bases.** Axler separates the map $T$ from its matrix $\mathcal{M}(T)$, which depends on the bases chosen in the domain and the target; changing the bases changes the matrix but not the map.[^axler] Principal component coordinates are such a change of basis ([[Basis and Dimension]], [[Linear Transformation]]).
- **Memory layout.** A dense matrix is stored as one block of memory, row after row (row-major, NumPy's default `C` order) or column after column (column-major, Fortran order). Operations that walk along the stored order are faster ([[Array Memory Layout]], [[Memory Hierarchy]]).
- **Sparse storage.** When most entries are zero, store only the nonzero ones: as $(i, j, a_{ij})$ triples (coordinate format, which is also the "long" table format of data frames) or row by row with column indices (compressed sparse row). Memory then grows with the number of nonzeros instead of $mn$ (Exercise 5, [[Sparse Matrix]]).
- **Beyond two indices.** Data with three indices (gene × sample × time) form a tensor, an [[N-Dimensional Array]]; flattening it to a matrix chooses which indices become rows.

## Mathematical representation

$$A = \begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{pmatrix} \in \mathbb{R}^{m \times n}, \qquad (A^\top)_{ij} = a_{ji}, \qquad (Ax)_i = \sum_{j=1}^{n} a_{ij} x_j.$$

- Columns: $a_j = (a_{1j}, \dots, a_{mj})^\top$, so $Ax = \sum_j x_j a_j$. Rows: $r_i^\top = (a_{i1}, \dots, a_{in})$, so $(Ax)_i = r_i \cdot x$.
- Symmetric: $A = A^\top$. Row-stochastic: $a_{ij} \ge 0$ and $\sum_j a_{ij} = 1$ for every $i$.
- Count matrix $X = (x_{gj})$, $g = 1, \dots, G$ genes, $j = 1, \dots, n$ samples; library sizes $N = X^\top \mathbf{1}_G$.

## Computational representation

In pure Python a matrix is a list of rows; NumPy stores it as a two-dimensional array. A count matrix usually arrives as a tab-separated file with a header row and a gene-name column:

```python
import csv
import io

TSV = """gene\tS1\tS2\tS3\tS4
geneA\t10\t0\t5\t7
geneB\t3\t8\t1\t0
geneC\t0\t2\t4\t6
"""                                   # invented count matrix, genes x samples

rows = list(csv.reader(io.StringIO(TSV), delimiter="\t"))
samples, genes = rows[0][1:], [r[0] for r in rows[1:]]
X = [[int(v) for v in r[1:]] for r in rows[1:]]


def shape(A):
    return len(A), len(A[0])


def column(A, j):
    return [row[j] for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def matvec(A, x):
    """Ax computed as x1*(column 1) + ... + xn*(column n)."""
    result = [0] * len(A)
    for j, xj in enumerate(x):
        for i in range(len(A)):
            result[i] += xj * A[i][j]
    return result


print(shape(X), shape(transpose(X)), column(X, 1))
print(transpose(X))
print(matvec(X, [1, 1, 1, 1]))              # row sums: total reads per gene
print(matvec(transpose(X), [1, 1, 1]))      # column sums: library sizes

import numpy as np
Xn = np.array(X)
print(Xn.shape, Xn.T.shape, Xn.sum(axis=0), Xn @ np.ones(4))
print(Xn.flags["C_CONTIGUOUS"])             # row-major storage
```

```text
(3, 4) (4, 3) [0, 8, 2]
[[10, 3, 0], [0, 8, 2], [5, 1, 4], [7, 0, 6]]
[22, 12, 12]
[13, 10, 10, 13]
(3, 4) (4, 3) [13 10 10 13] [22. 12. 12.]
True
```

`zip(*A)` transposes a list of rows in one line. Keep gene and sample names next to the numbers (`genes`, `samples`): a matrix without its labels is the commonest source of silently misaligned data.

## Worked example

> [!example] From a count matrix to a sample distance matrix (invented data)
> The toy count matrix above: 3 genes × 4 samples, $X \in \mathbb{R}^{3 \times 4}$.
> 1. **Columns as samples**: $S_1 = (10, 3, 0)$, $S_2 = (0, 8, 2)$, $S_3 = (5, 1, 4)$, $S_4 = (7, 0, 6)$.
> 2. **Library sizes** $X^\top \mathbf{1} = (13, 10, 10, 13)$; **gene totals** $X\mathbf{1} = (22, 12, 12)$.
> 3. **Transpose**: $X^\top \in \mathbb{R}^{4 \times 3}$ has the samples as rows, the orientation most clustering code expects.
> 4. **Distances** between columns with the Euclidean norm, e.g. $d(S_1, S_2) = \sqrt{10^2 + 5^2 + 2^2} = \sqrt{129} \approx 11.36$. The full $4 \times 4$ matrix:
> ```text
>         S1     S2     S3     S4
> S1    0.00  11.36   6.71   7.35
> S2   11.36   0.00   8.83  11.36
> S3    6.71   8.83   0.00   3.00
> S4    7.35  11.36   3.00   0.00
> ```
> 5. **Check the invariants**: square, symmetric ($D = D^\top$ holds in code), zero diagonal. $S_3$ and $S_4$ are the closest pair: a tree builder would join them first ([[Distance Matrix]]).

## Common misconceptions

> [!warning] "$a_{ij}$: $i$ is the column"
> The row index always comes first, in mathematics and in `A[i][j]` or `A[i, j]`. "$m \times n$" is rows × columns.

> [!warning] "The transpose is the inverse"
> $A^\top$ swaps rows and columns and exists for every matrix; $A^{-1}$ undoes the map and exists only for some square matrices ([[Inverse Matrix]]). They coincide only for orthogonal matrices.

> [!warning] "A substitution matrix is a matrix of probabilities"
> BLOSUM62 holds log-odds scores, rounded to half-bit units: entries are negative or positive and rows do not sum to 1.[^henikoff] A PAM mutation probability matrix, by contrast, is a transition matrix; the PAM *scoring* matrix is derived from it by a log-odds transformation ([[Substitution Matrix]]).[^dayhoff]

> [!warning] "Genes × samples and samples × genes are interchangeable"
> They hold the same numbers but mean different things to a function: a routine that standardizes columns will standardize genes in one orientation and samples in the other.

## Exercises

> [!question] Exercise 1 (L1)
> $A = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix}$. Give its shape, $a_{23}$, its second column, $A^\top$, and $Ax$ for $x = (2, 1, 0)$ using the column picture.

> [!success]- Solution
> $2 \times 3$; $a_{23} = 1$; second column $(0, 3)$; $A^\top = \begin{pmatrix} 1 & -1 \\ 0 & 3 \\ 2 & 1 \end{pmatrix}$. $Ax = 2\,(1, -1) + 1\,(0, 3) + 0\,(2, 1) = (2, 1)$.

> [!question] Exercise 2 (L1)
> Classify each matrix as a possible distance, transition or substitution matrix (or none): $P = \begin{pmatrix} 0.9 & 0.1 \\ 0.3 & 0.7 \end{pmatrix}$, $B = \begin{pmatrix} 4 & -1 \\ -1 & 5 \end{pmatrix}$, $D = \begin{pmatrix} 0 & 2 \\ 3 & 0 \end{pmatrix}$.

> [!success]- Solution
> $P$: nonnegative rows summing to 1, not symmetric: a transition matrix. $B$: symmetric with negative entries and rows not summing to 1: a score (substitution-like) matrix. $D$: zero diagonal but $d_{12} \ne d_{21}$: not a distance matrix.

> [!question] Exercise 3 (L2)
> Prove that $A^\top A$ is symmetric for any $m \times n$ matrix $A$, and give its shape. Check with $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 3 & -1 \end{pmatrix}$.

> [!success]- Solution
> $(A^\top A)^\top = A^\top (A^\top)^\top = A^\top A$; it is $n \times n$. Here $A^\top A = \begin{pmatrix} 10 & -1 \\ -1 & 6 \end{pmatrix}$: entry $(1, 2)$ is the dot product of the two columns, $1 \cdot 2 + 0 \cdot 1 + 3 \cdot (-1) = -1$.

> [!question] Exercise 4 (L2, Python)
> Write `is_transition(P, tol=1e-9)` and `is_distance(D)` that check the invariants of the table, and run them on the matrices of Exercise 2.

> [!success]- Solution
> ```python
> def is_transition(P, tol=1e-9):
>     return all(len(r) == len(P) for r in P) and \
>         all(x >= 0 for r in P for x in r) and all(abs(sum(r) - 1) <= tol for r in P)
>
> def is_distance(D):
>     n = len(D)
>     return all(D[i][i] == 0 for i in range(n)) and \
>         all(D[i][j] == D[j][i] and D[i][j] >= 0 for i in range(n) for j in range(n))
>
> P, B, D = [[0.9, 0.1], [0.3, 0.7]], [[4, -1], [-1, 5]], [[0, 2], [3, 0]]
> print(is_transition(P), is_transition(B), is_distance(D))
> # True False False
> ```
> A tolerance is needed for rows of floats: $0.1 + 0.2$ is not exactly $0.3$ in floating point ([[Floating-Point Arithmetic]]).

> [!question] Exercise 5 (L3)
> A hypothetical single-cell experiment has 30,000 genes × 1,000,000 cells. Estimate the memory of the dense matrix in 64-bit floats, then of a compressed sparse row version if 5 % of entries are nonzero (8 bytes per value and 4 bytes per column index, ignoring the row pointers).

> [!success]- Solution
> Dense: $3 \times 10^4 \times 10^6 \times 8 = 2.4 \times 10^{11}$ bytes = 240 GB. Sparse: $0.05 \times 3 \times 10^{10} = 1.5 \times 10^9$ nonzeros × 12 bytes = 18 GB. The sparse format is mandatory at this scale, and algorithms must avoid operations (like centering) that fill in the zeros ([[Sparse Matrix]]).

## Mastery checklist

- [ ] 1 Recognized: I can read the shape, an entry, a row and a column of a matrix, and transpose it.
- [ ] 2 Understood: I can explain the table, column and map readings, and why $Ax$ is a combination of columns.
- [ ] 3 Practiced: I can load a labeled matrix from TSV, transpose it, compute $Ax$ by columns, and test structural invariants in code.
- [ ] 4 Applied: I loaded a real count matrix, computed library sizes and a sample distance matrix, and fed a distance matrix to [[08-phylogenetic-engine]].
- [ ] 5 Explained: I can explain which operations make sense on count, distance, substitution and transition matrices, and how dense and sparse storage differ.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of linear maps and their matrices.
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], material on count data from high-throughput sequencing.
[^saitou]: [[Saitou 1987 - The Neighbor-Joining Method]], *Molecular Biology and Evolution* 4:406-425.
[^henikoff]: [[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]], *PNAS* 89:10915-10919.
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models".
[^dayhoff]: [[Dayhoff 1978 - A Model of Evolutionary Change in Proteins]], *Atlas of Protein Sequence and Structure* 5(3):345-352.
