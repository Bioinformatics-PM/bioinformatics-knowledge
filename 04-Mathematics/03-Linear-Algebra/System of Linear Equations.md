---
aliases:
  - Linear System
  - Ax = b
  - Linear Equations
  - Homogeneous System
  - Système d'équations linéaires
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Vector]]"
  - "[[Matrix]]"
  - "[[Matrix Multiplication]]"
related:
  - "[[Gaussian Elimination]]"
  - "[[Inverse Matrix]]"
  - "[[Matrix Rank]]"
  - "[[Fundamental Theorem of Linear Algebra]]"
  - "[[Least Squares]]"
  - "[[Stoichiometric Matrix]]"
  - "[[Flux Balance Analysis]]"
  - "[[Linear Programming]]"
projects: []
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Orth 2010 - What Is Flux Balance Analysis]]"
  - "[[Abbas 2009 - Deconvolution of Blood Microarray Data Identifies Cellular Activation Patterns in Systemic Lupus Erythematosus]]"
---

# System of Linear Equations

> [!abstract]
> A system of linear equations asks for the unknowns $x$ that satisfy $Ax = b$: geometrically, where lines or planes meet, or which combination of the columns of $A$ produces $b$. There is always exactly one solution, none, or infinitely many.

## Definition

A **system of $m$ linear equations in $n$ unknowns** is
$$a_{i1} x_1 + a_{i2} x_2 + \dots + a_{in} x_n = b_i, \qquad i = 1, \dots, m,$$
written compactly as $Ax = b$ with the coefficient [[Matrix]] $A \in \mathbb{R}^{m \times n}$, the unknown vector $x \in \mathbb{R}^n$ and the right-hand side $b \in \mathbb{R}^m$. A **solution** is any $x$ that satisfies all equations; the system is **consistent** if it has at least one. The system is **homogeneous** when $b = 0$.[^strang][^1806]

## Why it matters

- **Steady-state metabolism.** Write a metabolic network as a stoichiometric matrix $S$ (metabolites × reactions) and the reaction rates as a flux vector $v$. At steady state, production and consumption of every compound balance: $Sv = 0$.[^orth] The solutions of this homogeneous system are the feasible flux distributions that [[Flux Balance Analysis]] then optimizes ([[Stoichiometric Matrix]]).
- **Deconvolution.** A bulk tissue sample mixes cell types. If column $k$ of $A$ is the expression profile of cell type $k$ over $G$ marker genes and $x_k$ its amount in the sample, the bulk profile is modeled as $b \approx Ax$; solving for $x$ estimates the composition. Abbas et al. showed that such deconvolution of blood expression data accurately quantified the constituents of real blood samples and of mixtures of immune cell lines.[^abbas]
- **Everywhere else.** Calibration curves, the normal equations of regression ([[Inverse Matrix]], [[Least Squares]]), and every step of Newton's method solve a linear system. [[Gaussian Elimination]] is how they are solved.

## Core (L1)

### Two pictures

Take $x + 2y = 5$ and $3x - y = 1$, i.e. $A = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$, $b = (5, 1)$.[^1806]

- **Row picture.** Each equation is a line in the plane; the solution is their intersection, $(x, y) = (1, 2)$. With 3 unknowns, each equation is a plane in space.
- **Column picture.** Find the combination of the columns that gives $b$: $x\,(1, 3) + y\,(2, -1) = (5, 1)$. Indeed $1 \cdot (1, 3) + 2 \cdot (2, -1) = (5, 1)$.

![[matrix-vector-column-combination.svg]]

The column picture is the one that scales: $Ax = b$ is solvable exactly when $b$ is a combination of the columns of $A$, i.e. lies in their span ([[Vector]]).[^strang]

### Three possible outcomes

| Row picture (2 unknowns) | Example | Solutions |
|---|---|---|
| Lines cross at one point | $x + 2y = 5$, $3x - y = 1$ | exactly one: $(1, 2)$ |
| Parallel distinct lines | $x + y = 1$, $x + y = 2$ | none (inconsistent) |
| The same line twice | $x + y = 1$, $2x + 2y = 2$ | infinitely many: $(t, 1 - t)$ |

Never exactly two: if $x_1 \ne x_2$ both solve $Ax = b$, then every point $x_1 + s(x_2 - x_1)$ on the line through them does too, because $A(x_1 + s(x_2 - x_1)) = b + s(b - b) = b$. A homogeneous system $Ax = 0$ is always consistent ($x = 0$ works); the question is whether it has other solutions.

## Deeper (L2)

**Structure of all solutions.** If $x_p$ is one particular solution of $Ax = b$, the full solution set is
$$\{x_p + x_n : Ax_n = 0\},$$
a particular solution plus anything in the **null space** of $A$. A unique solution means the null space is $\{0\}$, i.e. the columns of $A$ are independent ([[Linear Independence]], [[Matrix Rank]]).[^strang]

**Counting equations is not enough.** With fewer equations than unknowns ($m < n$), a consistent system always has infinitely many solutions (free variables remain after elimination), but it can still be inconsistent ($x + y + z = 1$, $x + y + z = 2$). With more equations than unknowns ($m > n$), as in deconvolution with many marker genes, exact solutions usually do not exist for noisy data and one solves for the $x$ that makes $Ax$ closest to $b$ instead ([[Least Squares]]).

**A toy flux balance (invented network).** Reactions: $R_1$: $\to A$ (uptake), $R_2$: $A \to B$, $R_3$: $B \to$ (secretion), $R_4$: $A \to$ (secretion). Each column of $S$ lists what one reaction consumes ($-1$) or produces ($+1$):
$$S = \begin{pmatrix} 1 & -1 & 0 & -1 \\ 0 & 1 & -1 & 0 \end{pmatrix} \begin{matrix} \leftarrow A \\ \leftarrow B \end{matrix}, \qquad Sv = 0 \iff v_1 = v_2 + v_4,\; v_2 = v_3.$$
Two equations, four unknowns: two fluxes are free, and every steady state is $v = v_3\,(1, 1, 1, 0) + v_4\,(1, 0, 0, 1)$. The flux $v = (10, 6, 6, 4)$ balances; $(10, 6, 5, 4)$ does not ($B$ accumulates at rate 1). Genome-scale networks behave the same way: the steady-state equations alone leave a large space of solutions, and flux balance analysis adds bounds and an objective, solved by [[Linear Programming]].[^orth] The null space itself is the subject of [[Fundamental Theorem of Linear Algebra]].

## Advanced (L3)

**Deconvolution as a linear system.** With $A \in \mathbb{R}^{G \times K}$ ($G$ marker genes, $K$ cell types, $G > K$) and a bulk profile $b$, the estimate solves the $K \times K$ system $(A^\top A)\,x = A^\top b$ (the normal equations of [[Least Squares]]). A practical method must also deal with negative estimates and decide whether $x$ holds amounts or proportions summing to 1. Two lessons from the toy below:

- **Exact data are recovered exactly.** With the invented signature matrix $A = \begin{pmatrix} 10 & 1 \\ 8 & 2 \\ 1 & 9 \\ 0 & 7 \end{pmatrix}$ and true amounts $x = (0.3, 0.7)$, $b = Ax = (3.7, 3.8, 6.6, 4.9)$, and solving the normal equations returns $(0.3, 0.7)$.
- **Similar cell types make the system ill-conditioned.** If the two signature columns are nearly proportional, $\det(A^\top A)$ is small and a small error in $b$ produces a large error in $x$ (Exercise 4). Biologically, closely related cell types are hard to separate from bulk data; numerically, this is the condition number ([[Inverse Matrix]]).

**Solving in practice.** Elimination solves a dense $n \times n$ system in about $n^3/3$ multiply-subtract steps ([[Gaussian Elimination]]); the same factorization is reused for many right-hand sides ([[LU Decomposition]]); large sparse systems such as genome-scale stoichiometric matrices call for sparse or iterative methods ([[Sparse Matrix]], [[Numerical Linear Algebra]]).

## Mathematical representation

- $A \in \mathbb{R}^{m \times n}$, $x \in \mathbb{R}^n$, $b \in \mathbb{R}^m$; $Ax = b \iff \sum_{j=1}^{n} x_j a_j = b$ with $a_j$ the columns of $A$.
- Solution set: $\varnothing$, or $x_p + N(A)$ with $N(A) = \{x : Ax = 0\}$ the null space; unique iff $N(A) = \{0\}$.
- Augmented matrix $[A \mid b] \in \mathbb{R}^{m \times (n+1)}$: the object that elimination works on.
- Flux balance: $S \in \mathbb{R}^{M \times R}$ ($M$ metabolites, $R$ reactions), $v \in \mathbb{R}^R$, steady state $Sv = 0$.[^orth] Deconvolution: $b \approx Ax$, $A \in \mathbb{R}^{G \times K}$, $x \in \mathbb{R}^K$.

## Computational representation

Checking a candidate is easy; finding solutions is the job of [[Gaussian Elimination]]. The residual $b - Ax$ is the universal check:

```python
def matvec(A, x):
    return [sum(a * xj for a, xj in zip(row, x)) for row in A]


def residual(A, x, b):
    """b - Ax: all zeros exactly when x solves Ax = b."""
    return [bi - axi for bi, axi in zip(b, matvec(A, x))]


# Invented network. Reactions: R1: -> A, R2: A -> B, R3: B ->, R4: A ->
S = [[1, -1, 0, -1],    # metabolite A
     [0, 1, -1, 0]]     # metabolite B
for v in ([10, 6, 6, 4], [10, 6, 5, 4]):
    print(v, matvec(S, v))


def solve_normal_2(A, b):
    """Least-squares x for a G x 2 matrix A: solve the 2 x 2 system (A^T A) x = A^T b."""
    a11 = sum(r[0] * r[0] for r in A); a12 = sum(r[0] * r[1] for r in A)
    a22 = sum(r[1] * r[1] for r in A)
    c1 = sum(r[0] * bi for r, bi in zip(A, b)); c2 = sum(r[1] * bi for r, bi in zip(A, b))
    det = a11 * a22 - a12 * a12
    return [(c1 * a22 - a12 * c2) / det, (a11 * c2 - a12 * c1) / det], det


A = [[10, 1], [8, 2], [1, 9], [0, 7]]  # invented signatures: 4 marker genes x 2 cell types
x_true = [0.3, 0.7]
b = matvec(A, x_true)
x, det = solve_normal_2(A, b)
print([round(v, 2) for v in b], [round(v, 4) for v in x], det)
b_noisy = [3.9, 3.6, 6.8, 4.7]         # invented noisy measurement
x, _ = solve_normal_2(A, b_noisy)
print([round(v, 3) for v in x], round(sum(x), 3))
```

```text
[10, 6, 6, 4] [0, 0]
[10, 6, 5, 4] [0, 1]
[3.7, 3.8, 6.6, 4.9] [0.3, 0.7] 21050
[0.304, 0.701] 1.004
```

With noise, the estimate stays close to $(0.3, 0.7)$ but no longer sums exactly to 1: an overdetermined system has no exact solution, only a best fit.

## Worked example

> [!example] One system, two pictures, one check
> Solve $x + 2y = 5$, $3x - y = 1$.
> 1. **Eliminate** $x$: subtract 3 × (equation 1) from equation 2: $-7y = -14$, so $y = 2$; back in equation 1, $x = 5 - 4 = 1$.
> 2. **Row picture**: the lines $y = (5 - x)/2$ and $y = 3x - 1$ have different slopes ($-\tfrac12$ and 3), so they meet once, at $(1, 2)$.
> 3. **Column picture**: $1 \cdot (1, 3) + 2 \cdot (2, -1) = (1 + 4, 3 - 2) = (5, 1) = b$.
> 4. **Residual**: `residual([[1, 2], [3, -1]], [1, 2], [5, 1])` gives `[0, 0]`.

## Common misconceptions

> [!warning] "As many equations as unknowns means exactly one solution"
> $x + y = 1$, $2x + 2y = 2$ has two equations, two unknowns and infinitely many solutions; replace the 2 on the right by 3 and there are none. What counts is the number of independent equations ([[Matrix Rank]]).

> [!warning] "Sv = 0 determines the fluxes"
> The steady-state condition leaves free directions whenever there are more independent reactions than independent balance equations (two free fluxes in the toy network). Flux balance analysis needs extra constraints and an objective to pick one solution.[^orth]

## Exercises

> [!question] Exercise 1 (L1)
> Write as $Ax = b$: $2x - z = 1$, $x + y + z = 4$, $y - 3z = 0$. Then check whether $(1, 2, 1)$ is a solution.

> [!success]- Solution
> $A = \begin{pmatrix} 2 & 0 & -1 \\ 1 & 1 & 1 \\ 0 & 1 & -3 \end{pmatrix}$, $b = (1, 4, 0)$. $A(1, 2, 1) = (1, 4, -1) \ne b$: the third equation fails, so it is not a solution.

> [!question] Exercise 2 (L1)
> Classify each system (one, none, infinitely many solutions) and draw the row picture: (a) $x - y = 0$, $x + y = 2$; (b) $2x + 4y = 6$, $x + 2y = 3$; (c) $2x + 4y = 6$, $x + 2y = 4$.

> [!success]- Solution
> (a) One solution, $(1, 1)$: crossing lines. (b) Infinitely many: the first equation is twice the second, same line, solutions $(3 - 2t, t)$. (c) None: parallel lines ($x + 2y$ cannot equal both 3 and 4).

> [!question] Exercise 3 (L2)
> In the toy flux network, add reaction $R_5$: $B \to A$. Write the new $S$, and show that $v = (0, 1, 0, 0, 1)$ is a steady state. What does it mean biologically, and why is it a problem for flux analysis?

> [!success]- Solution
> New column $(1, -1)$: $S = \begin{pmatrix} 1 & -1 & 0 & -1 & 1 \\ 0 & 1 & -1 & 0 & -1 \end{pmatrix}$. $Sv = (-1 + 1, 1 - 1) = (0, 0)$. It is a cycle $A \to B \to A$ carrying flux with no uptake: mathematically allowed by $Sv = 0$, thermodynamically impossible without energy input, so models add bounds or loop-removal constraints.

> [!question] Exercise 4 (L3, Python)
> Replace the signatures by two very similar cell types, $A' = \begin{pmatrix} 10 & 9 \\ 8 & 7 \\ 1 & 1 \\ 0 & 0.5 \end{pmatrix}$, with the same $x = (0.3, 0.7)$. Using `solve_normal_2`, compare $\det(A^\top A)$ and the estimates when the error $(0.2, -0.2, 0.2, -0.2)$ is added to $b$, for $A$ and for $A'$.

> [!success]- Solution
> ```python
> e = [0.2, -0.2, 0.2, -0.2]
> for M in (A, [[10, 9], [8, 7], [1, 1], [0, 0.5]]):
>     b = matvec(M, x_true)
>     x_exact, det = solve_normal_2(M, b)
>     x_noisy, _ = solve_normal_2(M, [bi + ei for bi, ei in zip(b, e)])
>     print(round(det, 2), [round(v, 4) for v in x_exact], [round(v, 3) for v in x_noisy])
> # 21050 [0.3, 0.7] [0.304, 0.701]
> # 47.25 [0.3, 0.7] [0.411, 0.579]
> ```
> Both recover $x$ from exact data. With the same small error, the well-separated signatures move the estimate by less than 0.01; the similar ones move it by more than 0.1, because $\det(A'^\top A')$ is about 450 times smaller. Deconvolution of closely related cell types is intrinsically unstable.

## Mastery checklist

- [ ] 1 Recognized: I can write a set of linear equations as $Ax = b$ and check a candidate solution.
- [ ] 2 Understood: I can draw the row and column pictures and explain why there are 0, 1 or infinitely many solutions.
- [ ] 3 Practiced: I can describe the full solution set as particular solution plus null space, and build $S$ for a small reaction network.
- [ ] 4 Applied: I set up $Sv = 0$ for a real pathway, or deconvolved a bulk profile with a published signature matrix, and checked residuals.
- [ ] 5 Explained: I can explain why steady state does not fix fluxes, why deconvolution of similar cell types is unstable, and when least squares replaces exact solving.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^orth]: [[Orth 2010 - What Is Flux Balance Analysis]], *Nature Biotechnology*.
[^abbas]: [[Abbas 2009 - Deconvolution of Blood Microarray Data Identifies Cellular Activation Patterns in Systemic Lupus Erythematosus]], *PLoS ONE* 4(7):e6098.
