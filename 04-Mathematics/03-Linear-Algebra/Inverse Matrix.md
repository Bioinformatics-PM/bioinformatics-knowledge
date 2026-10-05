---
aliases:
  - Matrix Inverse
  - Invertible Matrix
  - Nonsingular Matrix
  - Singular Matrix
  - Normal Equations
  - Matrice inverse
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Matrix Multiplication]]"
  - "[[System of Linear Equations]]"
  - "[[Gaussian Elimination]]"
related:
  - "[[Determinant]]"
  - "[[LU Decomposition]]"
  - "[[Least Squares]]"
  - "[[Linear Regression]]"
  - "[[Linear Independence]]"
  - "[[QR Decomposition]]"
  - "[[Singular Value Decomposition]]"
  - "[[Floating-Point Arithmetic]]"
  - "[[Numerical Linear Algebra]]"
projects: []
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[An Introduction to Statistical Learning (James)]]"
---

# Inverse Matrix

> [!abstract]
> The inverse $A^{-1}$ of a square matrix undoes what $A$ does, so $Ax = b$ has the single solution $x = A^{-1}b$; it exists only when no information is lost, and numerical code, including regression software, gets $x$ without ever computing $A^{-1}$.

## Definition

A square $n \times n$ matrix $A$ is **invertible** (nonsingular) if there is a matrix $A^{-1}$ with $A^{-1}A = I$ and $AA^{-1} = I$; that matrix is unique. A square matrix without an inverse is **singular**. For $2 \times 2$ matrices:[^strang]
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}, \qquad \text{defined iff } ad - bc \ne 0.$$

## Why it matters

- **Regression.** Least-squares coefficients of a linear model with design matrix $X$ (samples × predictors) and response $y$ satisfy the **normal equations** $X^\top X \hat\beta = X^\top y$; when the columns of $X$ are independent, $\hat\beta = (X^\top X)^{-1} X^\top y$.[^strang][^isl] Any least-squares linear fit, from a qPCR standard curve to a regression of expression on genotype, solves these equations ([[Linear Regression]], [[Least Squares]]).
- **Non-identifiable designs.** If one column of $X$ is a combination of others (batch completely confounded with condition), $X^\top X$ is singular and the coefficients are not determined: no software can separate the two effects (Exercise 3, [[Linear Independence]]).

## Core (L1)

**When does $A^{-1}$ exist?** If $A$ sends $x$ to $b$, $A^{-1}$ sends $b$ back: multiplying $Ax = b$ on the left by $A^{-1}$ gives $x = A^{-1}b$.[^strang] For a square $n \times n$ matrix the following are equivalent:[^strang][^1806] (1) $A$ is invertible; (2) elimination finds $n$ pivots ([[Gaussian Elimination]]); (3) the columns of $A$ are independent ([[Linear Independence]]); (4) $Ax = 0$ has only the solution $x = 0$; (5) $Ax = b$ has exactly one solution for every $b$; (6) $\det A \ne 0$ ([[Determinant]]). Rectangular matrices have no inverse. A singular matrix squashes some nonzero vector to 0 (condition 4 fails), so two different inputs give the same output and no map can undo it.

**Rules.** $(A^{-1})^{-1} = A$; $(AB)^{-1} = B^{-1}A^{-1}$ (reverse order: to undo "first $B$, then $A$", undo $A$ first; check: $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = I$); $(A^\top)^{-1} = (A^{-1})^\top$.[^strang] A diagonal matrix with nonzero diagonal entries $d_i$ has inverse $\operatorname{diag}(1/d_i)$.

## Deeper (L2)

**Gauss-Jordan.** Row-reduce the $n \times 2n$ block $[A \mid I]$ until the left half is $I$; the right half is then $A^{-1}$. Each column of $A^{-1}$ is the solution of $Ax = e_j$, so this is elimination with $n$ right-hand sides at once.[^strang] It needs about $n^3$ multiplications, against about $n^3/3$ to solve one system ([[Gaussian Elimination]]).[^strang]

**The normal equations, derived.** The residual $r = y - X\beta$ is shortest when it is orthogonal to every column of $X$ ([[Orthogonal Projection]]): $X^\top (y - X\hat\beta) = 0$, i.e. $X^\top X \hat\beta = X^\top y$. If $X$ has independent columns then $X^\top X$ is invertible ($X^\top X v = 0 \Rightarrow v^\top X^\top X v = \lVert Xv \rVert^2 = 0 \Rightarrow Xv = 0 \Rightarrow v = 0$).[^strang]

**A fit by hand (invented data).** For the points $(1, 2.1)$, $(2, 3.9)$, $(3, 6.2)$, $(4, 7.8)$ and the model $y = \beta_0 + \beta_1 x$, the rows of $X$ are $(1, x_i)$, $X^\top X = \begin{pmatrix} 4 & 10 \\ 10 & 30 \end{pmatrix}$ (determinant 20), $X^\top y = (20, 59.7)$, and $\hat\beta = \frac{1}{20}\begin{pmatrix} 30 & -10 \\ -10 & 4 \end{pmatrix}\begin{pmatrix} 20 \\ 59.7 \end{pmatrix} = (0.15, 1.94)$: intercept 0.15, slope 1.94 (code below).

## Advanced (L3)

**One-sided is enough.** For a square matrix, $BA = I$ already implies $AB = I$: a linear map from a finite-dimensional space to itself is injective if and only if it is surjective.[^axler] This fails for rectangular matrices: $X^\top X$-based formulas give a *left* inverse $(X^\top X)^{-1}X^\top$ of a tall $X$, which is not a right inverse. The general replacement is the pseudoinverse, built from the [[Singular Value Decomposition]].

**Condition number.** $\kappa(A) = \lVert A \rVert\,\lVert A^{-1} \rVert$ (with the operator norm of [[Vector Norm]]) bounds how much a relative error in $b$ can be amplified in $x$; in double precision ([[Floating-Point Arithmetic]]) one can lose about $\log_{10}\kappa$ significant digits.[^strang] A matrix can be invertible on paper and useless in practice.

**Why numerical code avoids $A^{-1}$.** Three reasons, the last two measured below:

1. **Cost.** $A^{-1}$ costs about $n^3$, a solve about $n^3/3$; with an LU factorization stored, each further $b$ costs $n^2$ either way ([[LU Decomposition]]).
2. **Accuracy.** On the $10 \times 10$ Hilbert matrix ($\kappa \approx 1.6 \times 10^{13}$), `inv(H) @ b` leaves a residual $\lVert Hx - b \rVert \approx 2 \times 10^{-4}$ while `solve(H, b)` reaches $5 \times 10^{-16}$, and its error in $x$ is about 150 times smaller.
3. **Normal equations square the condition number.** $\kappa(X^\top X) = \kappa(X)^2$ in the 2-norm. For a design with two nearly collinear columns, $\kappa(X) \approx 3 \times 10^4$ but $\kappa(X^\top X) \approx 9 \times 10^8$: forming $X^\top X$ throws away about four more digits. QR works on $X$ directly ([[QR Decomposition]]).[^strang]

## Mathematical representation

- $A \in \mathbb{R}^{n \times n}$ invertible $\iff \exists\, B: AB = BA = I$; then $B = A^{-1}$ is unique (if $B$ and $C$ both work, $B = B(AC) = (BA)C = C$).
- Normal equations: $X \in \mathbb{R}^{n \times p}$, $y \in \mathbb{R}^n$, $\hat\beta = \arg\min_\beta \lVert y - X\beta \rVert_2^2$ satisfies $X^\top X\hat\beta = X^\top y$, and $\hat\beta = (X^\top X)^{-1}X^\top y$ when $\operatorname{rank} X = p$.

## Computational representation

```python
from fractions import Fraction


def inverse(A):
    """Gauss-Jordan on [A | I] with exact fractions; raises ValueError if A is singular."""
    n = len(A)
    M = [[Fraction(a) for a in row] + [Fraction(int(i == j)) for j in range(n)]
         for i, row in enumerate(A)]
    for c in range(n):
        p = next((i for i in range(c, n) if M[i][c] != 0), None)
        if p is None:
            raise ValueError("matrix is singular")
        M[c], M[p] = M[p], M[c]
        M[c] = [a / M[c][c] for a in M[c]]            # scale pivot row to make the pivot 1
        for i in range(n):
            if i != c and M[i][c] != 0:               # clear the rest of column c
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return [row[n:] for row in M]

def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

fmt = lambda M: [[str(a) for a in row] for row in M]
A = [[2, 1], [5, 3]]
print(fmt(inverse(A)), fmt(matmul(A, inverse(A))))

# Invented data: fit y = b0 + b1 * x by the normal equations
xs, ys = [1, 2, 3, 4], [2.1, 3.9, 6.2, 7.8]
X = [[1, x] for x in xs]
Xt = [list(c) for c in zip(*X)]
XtX = matmul(Xt, X)
Xty = matmul(Xt, [[y] for y in ys])
beta = matmul(inverse(XtX), [[Fraction(str(v[0]))] for v in Xty])
print(XtX, [round(v[0], 2) for v in Xty], [float(b[0]) for b in beta])

import numpy as np
Xn, yn = np.array(X, float), np.array(ys)
print(np.linalg.inv(Xn.T @ Xn) @ Xn.T @ yn)        # textbook formula
print(np.linalg.solve(Xn.T @ Xn, Xn.T @ yn))       # solve, no inverse
print(np.linalg.lstsq(Xn, yn, rcond=None)[0])      # works on X directly

n = 10
H = np.array([[1 / (i + j + 1) for j in range(n)] for i in range(n)])   # Hilbert matrix
x_true = np.ones(n)
b = H @ x_true
x_inv, x_sol = np.linalg.inv(H) @ b, np.linalg.solve(H, b)
print(f"cond(H) = {np.linalg.cond(H):.1e}")
print(f"residual inv: {np.linalg.norm(H @ x_inv - b):.1e}  solve: {np.linalg.norm(H @ x_sol - b):.1e}")
print(f"error    inv: {np.linalg.norm(x_inv - x_true):.1e}  solve: {np.linalg.norm(x_sol - x_true):.1e}")

t = np.linspace(0, 1, 20)
Xc = np.column_stack([np.ones(20), t, t + 1e-4 * np.sin(7 * t)])   # nearly collinear columns
print(f"cond(X) = {np.linalg.cond(Xc):.1e}, cond(X^T X) = {np.linalg.cond(Xc.T @ Xc):.1e}")
```

```text
[['3', '-1'], ['-5', '2']] [['1', '0'], ['0', '1']]
[[4, 10], [10, 30]] [20.0, 59.7] [0.15, 1.94]
[0.15 1.94]
[0.15 1.94]
[0.15 1.94]
cond(H) = 1.6e+13
residual inv: 2.0e-04  solve: 4.7e-16
error    inv: 1.1e-02  solve: 7.2e-05
cond(X) = 3.0e+04, cond(X^T X) = 9.0e+08
```

## Worked example

> [!example] Inverting a 2 × 2 matrix two ways
> $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.
> 1. **Formula**: $ad - bc = 6 - 5 = 1 \ne 0$, so $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
> 2. **Gauss-Jordan** on $[A \mid I]$: $R_1 \leftarrow R_1/2$ gives $(1, \tfrac12 \mid \tfrac12, 0)$; $R_2 \leftarrow R_2 - 5R_1$ gives $(0, \tfrac12 \mid -\tfrac52, 1)$; $R_2 \leftarrow 2R_2$ gives $(0, 1 \mid -5, 2)$; $R_1 \leftarrow R_1 - \tfrac12 R_2$ gives $(1, 0 \mid 3, -1)$.
> 3. **Check**: $AA^{-1} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I$.

## Common misconceptions

> [!warning] "To solve Ax = b, compute inv(A) @ b"
> It works on paper and in toy code, but costs about three times more and is less accurate than solving directly (Advanced). The three routes in the code agree on a well-conditioned toy problem and disagree on ill-conditioned ones: default to `solve` for square systems and `lstsq` (or a QR-based fit) for regression.

> [!warning] "A small determinant means nearly singular"
> $\det(0.1\,I_{10}) = 10^{-10}$, yet $0.1\,I$ is perfectly conditioned ($\kappa = 1$): its inverse is just $10\,I$. Nearness to singularity is measured by the condition number, not the determinant.

## Exercises

> [!question] Exercise 1 (L1)
> Invert $\begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}$ and check the product. Which of $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ and $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is invertible?

> [!success]- Solution
> $ad - bc = 24 - 14 = 10$, inverse $\frac{1}{10}\begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix}$. The first matrix has $ad - bc = 0$ (second column twice the first): singular. The second has $-1 \ne 0$ and is its own inverse (it swaps two coordinates, and swapping twice does nothing).

> [!question] Exercise 2 (L2, Python)
> Invert $B = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 0 \\ 1 & 0 & 3 \end{pmatrix}$ with Gauss-Jordan and verify $BB^{-1} = I$.

> [!success]- Solution
> ```python
> B = [[1, 0, 2], [0, 1, 0], [1, 0, 3]]
> print(fmt(inverse(B)), fmt(matmul(B, inverse(B))))
> # [['3', '0', '-2'], ['0', '1', '0'], ['-1', '0', '1']] [['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]
> ```
> By hand: $R_3 \leftarrow R_3 - R_1$ gives pivot 1 in position (3, 3) with right half $(-1, 0, 1)$; then $R_1 \leftarrow R_1 - 2R_3$ gives $(3, 0, -2)$.

> [!question] Exercise 3 (L3, Python)
> Four invented samples: two controls processed in batch 1, two treated samples in batch 2. Build $X$ with columns intercept, treatment $(0, 0, 1, 1)$ and batch $(0, 0, 1, 1)$, and try to invert $X^\top X$. Then move one treated sample to batch 1 and try again. What does this say about experimental design?

> [!success]- Solution
> ```python
> for batch in ([0, 0, 1, 1], [0, 0, 0, 1]):
>     X = [[1, t, bt] for t, bt in zip([0, 0, 1, 1], batch)]
>     XtX = matmul([list(c) for c in zip(*X)], X)
>     try:
>         print(batch, fmt(inverse(XtX)))
>     except ValueError as e:
>         print(batch, "ValueError:", e)
> # [0, 0, 1, 1] ValueError: matrix is singular
> # [0, 0, 0, 1] [['1/2', '-1/2', '0'], ['-1/2', '3/2', '-1'], ['0', '-1', '2']]
> ```
> With batch identical to treatment, the columns are dependent and the effects cannot be separated by any method. Balancing batches across conditions makes $X^\top X$ invertible: a design decision, not a computational one.

## Mastery checklist

- [ ] 1 Recognized: I can state what $A^{-1}$ is and invert a $2 \times 2$ matrix.
- [ ] 2 Understood: I can list the equivalent conditions for invertibility and derive the normal equations.
- [ ] 3 Practiced: I implemented Gauss-Jordan inversion, fitted a line through the normal equations, and checked it against `solve` and `lstsq`.
- [ ] 4 Applied: I fitted a linear model to real data with a QR- or `lstsq`-based solver, and detected a confounded design through a singular $X^\top X$.
- [ ] 5 Explained: I can explain why numerical code avoids $A^{-1}$ (cost, residuals, squared condition number) and what replaces it for rectangular or singular matrices.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of invertible linear maps.
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition (2023), linear regression.
