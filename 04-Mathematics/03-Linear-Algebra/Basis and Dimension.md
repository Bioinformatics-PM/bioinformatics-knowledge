---
aliases:
  - Basis
  - Dimension
  - Coordinates
  - Coordinate Vector
  - Change of Basis
  - Base d'un espace vectoriel
  - Dimension d'un espace vectoriel
tags:
  - type/concept
  - domain/mathematics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Vector Space]]"
  - "[[Linear Independence]]"
  - "[[Gaussian Elimination]]"
  - "[[Inverse Matrix]]"
related:
  - "[[Matrix Rank]]"
  - "[[Fundamental Theorem of Linear Algebra]]"
  - "[[Linear Transformation]]"
  - "[[Gram-Schmidt Process]]"
  - "[[Orthogonal Projection]]"
  - "[[Diagonalization]]"
  - "[[Principal Component Analysis]]"
  - "[[Low-Rank Approximation]]"
  - "[[Stoichiometric Matrix]]"
  - "[[K-mer]]"
  - "[[Symmetric Matrix]]"
projects: []
sources:
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Orth 2010 - What Is Flux Balance Analysis]]"
  - "[[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]]"
---

# Basis and Dimension

> [!abstract]
> A basis is a list of independent directions that spans a space, so that every vector has exactly one list of coordinates in it; the number of basis vectors, the dimension, counts the degrees of freedom of the space, whichever basis you choose.

## Definition

A **basis** of a vector space $V$ is a list $b_1, \dots, b_n$ of vectors of $V$ that is linearly independent and spans $V$. Every $v \in V$ is then a combination $v = c_1 b_1 + \dots + c_n b_n$ in exactly one way; the scalars $(c_1, \dots, c_n)$ are the **coordinates** of $v$ in that basis.[^axler][^strang] In a finite-dimensional space all bases have the same length, the **dimension** $\dim V$.[^axler][^1806]

## Why it matters

- **Coordinates are a choice.** An expression profile has coordinates in the gene basis (the measured values) and in the principal-component basis (its scores). [[Principal Component Analysis]] is a change to an orthonormal basis whose directions are ordered by the variance of the data along them.[^isl]
- **Dimension counts degrees of freedom.** The steady states of a metabolic network form the null space of its stoichiometric matrix ([[Vector Space]]);[^orth] its dimension, the number of reactions minus the rank of $S$, is the number of independent routes the network can combine ([[Stoichiometric Matrix]], [[Fundamental Theorem of Linear Algebra]]). A design matrix with $p$ independent columns produces a $p$-dimensional space of possible fitted values ([[Design Matrix]]).
- **Sizing feature spaces.** k-mer count vectors live in dimension $4^k$ ([[K-mer]]); a symmetric $20 \times 20$ amino-acid score matrix has $20 \cdot 21/2 = 210$ free entries, the number of BLOSUM scores ([[Symmetric Matrix]]);[^henikoff] compositions of $D$ parts have $D - 1$ degrees of freedom ([[Vector Space#Frontier (M1)]]).
- **Data rarely fill their space.** $n$ samples measured on $G \gg n$ genes span at most $n$ dimensions of $\mathbb{R}^G$, and at most $n - 1$ after centering: an RNA-seq experiment with 6 samples has at most 5 principal components with nonzero variance (Advanced).

## Core (L2)

### Bases

- The **standard basis** $e_1, \dots, e_n$ of $\mathbb{R}^n$: coordinates are the components themselves.
- Any $n$ independent vectors of $\mathbb{R}^n$ form a basis, for example the columns of an invertible $n \times n$ matrix ([[Inverse Matrix]]).[^strang]
- **Coordinates are unique** because of independence: if $\sum_j c_j b_j = \sum_j c'_j b_j$, then $\sum_j (c_j - c'_j)\, b_j = 0$, so $c = c'$. Spanning guarantees that they exist.
- **A basis of a subspace.** In the plane $x_1 + x_2 + x_3 = 0$ of $\mathbb{R}^3$, $x_1 = -x_2 - x_3$ with $x_2, x_3$ free. The choices $(x_2, x_3) = (1, 0)$ and $(0, 1)$ give $(-1, 1, 0)$ and $(-1, 0, 1)$: a basis, and the plane has dimension 2.

### Finding a basis

- **Of a span.** Put the vectors in the columns of $A$ and eliminate; the **pivot columns of $A$ itself** (not of its echelon form) are a basis of the span. Every spanning list contains a basis, and every independent list can be extended to one.[^axler][^strang]
- **Of the column space** $C(A)$: the same pivot columns. Their number is the rank $r$ ([[Matrix Rank]]).
- **Of the null space** $N(A)$: one special solution per free variable (set it to 1 and the other free variables to 0, then solve for the pivot variables), so $\dim N(A) = n - r$ for $A$ with $n$ columns.[^strang] [[Gaussian Elimination]] (Exercise 3) built the two routes of a toy network this way.

### Dimension

All bases of a space have the same length.[^axler]

| Space | Dimension | A basis |
|---|---|---|
| $\mathbb{R}^n$ | $n$ | $e_1, \dots, e_n$ |
| polynomials of degree $\le d$ | $d + 1$ | $1, x, \dots, x^d$ |
| $m \times n$ matrices | $mn$ | the matrices with a single entry 1 |
| symmetric $n \times n$ matrices | $n(n+1)/2$ | $E_{ii}$, and $E_{ij} + E_{ji}$ for $i < j$ |
| k-mer count vectors | $4^k$ | one indicator per k-mer |
| $\{z \in \mathbb{R}^D : \sum_i z_i = 0\}$ | $D - 1$ | $e_1 - e_D, \dots, e_{D-1} - e_D$ |
| $\{0\}$ | 0 | the empty list |

**Counting rules**, in a space of dimension $n$: more than $n$ vectors are dependent; fewer than $n$ cannot span; a list of exactly $n$ vectors is a basis as soon as it is independent, or as soon as it spans, since each property implies the other. A subspace $U$ of $V$ has $\dim U \le \dim V$, with equality only when $U = V$.[^axler]

### Coordinates and change of basis

Put the basis vectors in the columns of $B$. Then $x = Bc$: the coordinates are the solution of $Bc = x$, computed by solving, not by inverting $B$.

![[change-of-basis-coordinates.svg]]

- **Example.** $b_1 = (2, 1)$, $b_2 = (-1, 1)$, $x = (3, 3)$: $2c_1 - c_2 = 3$ and $c_1 + c_2 = 3$ give $c = (2, 1)$, so $x = 2b_1 + 1b_2$ while its standard coordinates are $(3, 3)$.
- **Between two bases** $B$ and $B'$: $Bc = B'c'$ gives $c' = B'^{-1}Bc$ (Exercise 6).
- **Orthonormal basis** (columns $q_i$ with $Q^\top Q = I$): $c = Q^\top x$, each coordinate a dot product $c_i = q_i \cdot x$, with no system to solve ([[Gram-Schmidt Process]], [[Orthogonal Projection]]). Principal-component scores are such dot products with orthonormal loading vectors.[^isl]

## Advanced (L3)

### Data dimension versus ambient dimension

```python
import numpy as np

rng = np.random.default_rng(7)
Y = rng.poisson(20, size=(1000, 5)).astype(float)      # invented: 1000 genes x 5 samples
Yc = Y - Y.mean(axis=1, keepdims=True)                 # center each gene across samples
print(np.linalg.matrix_rank(Y), np.linalg.matrix_rank(Yc), np.allclose(Yc.sum(axis=1), 0))
```

```text
5 4 True
```

Five sample vectors span at most 5 of the 1000 dimensions. After each gene is centered, the five sample columns add up to the zero vector, a dependency, so they span only 4: principal component analysis of $n$ samples yields at most $n - 1$ components with nonzero variance. Real expression data have an even lower **effective** dimension: a few directions carry most of the variance, which is what [[Low-Rank Approximation]] and [[Matrix Rank]] quantify.

### Dimension formulas

- **Rank and nullity.** For $A \in \mathbb{R}^{m \times n}$, $\dim C(A) + \dim N(A) = n$: pivot columns plus free columns ([[Fundamental Theorem of Linear Algebra]]).
- **Sum of subspaces.** $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.[^axler] Two planes through the origin of $\mathbb{R}^3$ therefore always share at least a line: $3 \ge 2 + 2 - \dim(U \cap W)$.

### Infinite dimension and model complexity

The space of all polynomials, or of all functions on an interval, has no finite basis.[^axler] Curve fitting works in a finite-dimensional subspace chosen in advance: polynomials of degree $\le d$ (dimension $d + 1$) or splines with fixed knots ([[Spline]]). Choosing the dimension is choosing the number of parameters, the complexity of the model.

### Change of basis for linear maps

If $y = Ax$ in standard coordinates and $x = Bc$, $y = Bd$, then $d = B^{-1}ABc$: in the basis $B$ the same map has the matrix $B^{-1}AB$ ([[Linear Transformation]]). Choosing a basis of eigenvectors makes this matrix diagonal ([[Diagonalization]]), the idea behind fast matrix powers and behind principal components.

## Mathematical representation

- **Basis**: $b_1, \dots, b_n$ independent with $\operatorname{span}(b_1, \dots, b_n) = V$. **Coordinate map** $v \mapsto (c_1, \dots, c_n)$, linear and bijective from $V$ to $\mathbb{F}^n$: once a basis is fixed, every $n$-dimensional real space behaves exactly like $\mathbb{R}^n$.[^axler]
- **Dimension**: $\dim V = n$, the common length of all bases; $\dim \mathcal{P}_d = d + 1$, $\dim \mathbb{R}^{m \times n} = mn$.
- **Formulas**: $\dim C(A) + \dim N(A) = n$; $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.
- **Coordinates**: $c = B^{-1}x$ (solve $Bc = x$); $c' = B'^{-1}Bc$; for orthonormal $Q$, $c = Q^\top x$; a map with matrix $A$ in standard coordinates has matrix $B^{-1}AB$ in the basis $B$.

## Computational representation

Exact elimination gives bases of column and null spaces and the coordinates of a vector in any independent list.

```python
from fractions import Fraction

def rref(M):
    """Reduced row echelon form in exact arithmetic; returns (R, pivot columns)."""
    R = [[Fraction(a) for a in row] for row in M]
    m, n = len(R), len(R[0])
    pivots, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        R[r] = [a / R[r][c] for a in R[r]]
        for i in range(m):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return R, pivots

def column_space_basis(A):
    """The pivot columns of A itself (not of its echelon form)."""
    _, pivots = rref(A)
    return [[row[j] for row in A] for j in pivots]

def null_space_basis(A):
    """One special solution per free column: that variable 1, the other free ones 0."""
    R, pivots = rref(A)
    n = len(A[0])
    basis = []
    for f in (j for j in range(n) if j not in pivots):
        x = [Fraction(0)] * n
        x[f] = Fraction(1)
        for i, p in enumerate(pivots):
            x[p] = -R[i][f]
        basis.append(x)
    return basis

def coordinates(basis, x):
    """Coordinates c of x in an independent list (x = sum c_j b_j); ValueError if x is outside the span."""
    k = len(basis)
    aug = [[b[i] for b in basis] + [x[i]] for i in range(len(x))]
    R, pivots = rref(aug)
    if pivots != list(range(k)):
        raise ValueError("x is not in the span, or the list is dependent")
    return [R[i][-1] for i in range(k)]

fmt = lambda vs: [[str(v) for v in vec] for vec in vs]
S = [[1, -1, 0, -1],      # toy network: metabolites x reactions
     [0, 1, -1, 0]]
routes = null_space_basis(S)
print(fmt(routes), len(routes))                         # dim N(S) = 4 - 2
print([str(c) for c in coordinates(routes, [5, 2, 2, 3])])
print([str(c) for c in coordinates([[2, 1], [-1, 1]], [3, 3])])   # skewed basis of R^2

import numpy as np

B = np.array([[2.0, -1.0], [1.0, 1.0]])                # basis vectors as columns
print(np.linalg.solve(B, [3.0, 3.0]))                  # solve B c = x, never inv(B)
Q = np.array([[1.0, -1.0], [1.0, 1.0]]) / np.sqrt(2)   # orthonormal basis (45 degrees)
c = Q.T @ np.array([3.0, 3.0])                         # coordinates = dot products
print(c.round(4), np.allclose(Q @ c, [3, 3]))
```

```text
[['1', '1', '1', '0'], ['1', '0', '0', '1']] 2
['2', '3']
['2', '1']
[2. 1.]
[4.2426 0.    ] True
```

`coordinates` handles a basis of a subspace (here 2 vectors of $\mathbb{R}^4$) as well as a basis of the whole space, and refuses a vector outside the span. In the orthonormal basis rotated by 45°, $x = (3, 3)$ lies along the first basis vector: coordinates $(3\sqrt2, 0)$.

## Worked example

> [!example] A steady state in the basis of routes (toy network, invented flux values)
> The toy network of [[System of Linear Equations]]: reactions $v_1$ (uptake of $A$), $v_2$ ($A \to B$), $v_3$ (secretion of $B$), $v_4$ (secretion of $A$), with $S = \begin{pmatrix} 1 & -1 & 0 & -1 \\ 0 & 1 & -1 & 0 \end{pmatrix}$.
> 1. **Dimension.** $S$ has 2 pivots (columns 1 and 2) for 4 reactions, so the steady-state space $N(S)$ has dimension $4 - 2 = 2$.
> 2. **Basis.** The special solutions are $r_1 = (1, 1, 1, 0)$, the route through $B$, and $r_2 = (1, 0, 0, 1)$, direct secretion of $A$.
> 3. **A measured steady state** $v = (5, 2, 2, 3)$: $Sv = (5 - 2 - 3,\ 2 - 2) = (0, 0)$. Since $c_1 r_1 + c_2 r_2 = (c_1 + c_2, c_1, c_1, c_2)$, its coordinates are $c = (2, 3)$.
> 4. **Reading.** Of 5 units of $A$ taken up, 2 flow through $B$ and 3 are secreted directly: two numbers describe what the four fluxes say, because the space has only two degrees of freedom.
> 5. **Another basis, same space.** In the basis $r_1$, $r_1 + r_2$, the same $v$ has coordinates $(-1, 3)$, since $-r_1 + 3(r_1 + r_2) = 2r_1 + 3r_2$. Coordinates change with the basis; the dimension does not.

## Common misconceptions

> [!warning] "A space has one basis"
> A space other than $\{0\}$ has infinitely many bases (any invertible $B$ turns one into another); what is unique is the dimension. The standard basis is a convenience, not a property of the data.

> [!warning] "Take the pivot columns of the echelon form"
> Row operations change the column space. The basis of $C(A)$ is made of the columns of $A$ in the pivot positions; the echelon form only tells you which positions.

> [!warning] "Coordinates are dot products with the basis vectors"
> Only for an orthonormal basis. For $b_1 = (2, 1)$ and $x = (3, 3)$, $b_1 \cdot x = 9$, while the first coordinate of $x$ in the basis $b_1, b_2$ is 2.

> [!warning] "A dataset with 20,000 genes is 20,000-dimensional"
> The samples live in $\mathbb{R}^{20000}$ but span at most as many dimensions as there are samples (one fewer after centering), and usually far fewer carry signal.

## Exercises

> [!question] Exercise 1 (L2)
> Find a basis and the dimension of the plane $x_1 - 2x_2 + x_3 = 0$ in $\mathbb{R}^3$.

> [!success]- Solution
> $x_1 = 2x_2 - x_3$ with $x_2$, $x_3$ free. $(x_2, x_3) = (1, 0)$ gives $(2, 1, 0)$; $(0, 1)$ gives $(-1, 0, 1)$. These two independent vectors span the plane: dimension 2.

> [!question] Exercise 2 (L2)
> Find the coordinates of $x = (1, 5)$ in the basis $b_1 = (1, 1)$, $b_2 = (1, -1)$.

> [!success]- Solution
> $c_1 + c_2 = 1$ and $c_1 - c_2 = 5$ give $c_1 = 3$, $c_2 = -2$. Check: $3(1, 1) - 2(1, -1) = (1, 5)$.

> [!question] Exercise 3 (L2)
> Give the dimension of: (a) symmetric $4 \times 4$ matrices; (b) polynomials of degree $\le 3$; (c) 3-mer count vectors; (d) skew-symmetric $3 \times 3$ matrices; (e) $\{x \in \mathbb{R}^5 : x_1 = x_2 = x_3\}$.

> [!success]- Solution
> (a) $4 \cdot 5/2 = 10$. (b) 4 ($1, x, x^2, x^3$). (c) $4^3 = 64$. (d) $3 \cdot 2/2 = 3$: zero diagonal, one free entry per pair above it. (e) 3: a common value for $x_1 = x_2 = x_3$, plus free $x_4$ and $x_5$; a basis is $(1, 1, 1, 0, 0)$, $e_4$, $e_5$.

> [!question] Exercise 4 (L3, Python)
> For $A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}$, find bases of $C(A)$ and $N(A)$ and check that their dimensions add up to the number of columns.

> [!success]- Solution
> ```python
> A = [[1, 2, 0, 1],
>      [2, 4, 1, 4],
>      [3, 6, 1, 5]]
> print(fmt(column_space_basis(A)), fmt(null_space_basis(A)))
> # [['1', '2', '3'], ['0', '1', '1']] [['-2', '1', '0', '0'], ['-1', '0', '-2', '1']]
> ```
> Pivots fall in columns 1 and 3: $C(A)$ has basis $(1, 2, 3)$, $(0, 1, 1)$ and dimension 2 (column 2 is twice column 1, column 4 is column 1 plus twice column 3). $N(A)$ has the two special solutions shown, which encode exactly these two relations. $2 + 2 = 4$ columns.

> [!question] Exercise 5 (L3)
> An RNA-seq experiment has 6 samples and 20,000 genes. What is the largest possible number of principal components with nonzero variance? What if two of the samples are technical duplicates with identical counts?

> [!success]- Solution
> After centering each gene, the 6 sample vectors add up to zero, so they span at most 5 dimensions: at most 5 components. With two identical samples, the centered vectors take only 5 distinct values, and the zero-sum relation still links them, so they span at most 4 dimensions: at most 4 components.

> [!question] Exercise 6 (L3, Python)
> A vector has coordinates $c = (3, -2)$ in the basis $(1, 1)$, $(1, -1)$. Find its coordinates in the basis $(2, 1)$, $(-1, 1)$, with $c' = B'^{-1}Bc$ computed by a solve.

> [!success]- Solution
> ```python
> B1 = np.array([[1.0, 1.0], [1.0, -1.0]])               # basis (1, 1), (1, -1) as columns
> B2 = np.array([[2.0, -1.0], [1.0, 1.0]])               # basis (2, 1), (-1, 1)
> c1 = np.array([3.0, -2.0])                             # coordinates of x in basis 1
> x = B1 @ c1
> c2 = np.linalg.solve(B2, B1 @ c1)                      # change of basis: c2 = B2^-1 B1 c1
> print(x, c2.round(4), np.allclose(B2 @ c2, x))
> # [1. 5.] [2. 3.] True
> ```
> The vector is $x = (1, 5)$ (Exercise 2), and $2(2, 1) + 3(-1, 1) = (1, 5)$.

## Mastery checklist

- [ ] 1 Recognized: I can define a basis, coordinates and dimension, and give the dimension of common spaces ($\mathbb{R}^n$, polynomials, matrices, symmetric matrices).
- [ ] 2 Understood: I can explain why coordinates are unique, why all bases have the same length, and why the pivot columns of $A$ (not of its echelon form) span $C(A)$.
- [ ] 3 Practiced: I can compute bases of column and null spaces, coordinates in any basis and changes of basis, by hand and in code.
- [ ] 4 Applied: I computed the steady-state dimension of a real metabolic network and expressed a flux distribution in a basis of routes, or measured the rank of a real centered expression matrix before PCA.
- [ ] 5 Explained: I can explain how many principal components a dataset can have, why model complexity is a dimension, and how a change of basis changes the matrix of a linear map.

## References

[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of bases, dimension and finite-dimensional spaces.
[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition (2023), principal components analysis.
[^orth]: [[Orth 2010 - What Is Flux Balance Analysis]], *Nature Biotechnology*.
[^henikoff]: [[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]], *PNAS* 89:10915-10919.
