---
aliases:
  - Norm
  - Euclidean Norm
  - L2 Norm
  - Manhattan Norm
  - L1 Norm
  - Maximum Norm
  - Infinity Norm
  - p-Norm
  - Euclidean Distance
  - Norme d'un vecteur
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
related:
  - "[[Distance Matrix]]"
  - "[[Count Normalization]]"
  - "[[Regularization]]"
  - "[[Lasso]]"
  - "[[Ridge Regression]]"
  - "[[Clustering]]"
  - "[[Least Squares]]"
projects: []
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Stanford - Statistical Learning with Python]]"
  - "[[Wagner 2012 - Measurement of mRNA Abundance Using RNA-seq Data]]"
---

# Vector Norm

> [!abstract]
> A norm measures the size of a vector, and the norm of a difference measures the distance between two vectors; the three common norms (Euclidean, Manhattan, maximum) give different distances between samples and different penalties in regularized regression.

## Definition

A **norm** on $\mathbb{R}^n$ is a function $v \mapsto \lVert v \rVert$ with, for all vectors $u, v$ and scalars $c$: $\lVert v \rVert \ge 0$ with equality only for $v = 0$; $\lVert c v \rVert = |c|\,\lVert v \rVert$; and the **triangle inequality** $\lVert u + v \rVert \le \lVert u \rVert + \lVert v \rVert$.[^strang] The three standard examples are the **Euclidean** norm $\lVert v \rVert_2 = \sqrt{\sum_i v_i^2}$ (the length, $\sqrt{v \cdot v}$), the **Manhattan** norm $\lVert v \rVert_1 = \sum_i |v_i|$ and the **maximum** norm $\lVert v \rVert_\infty = \max_i |v_i|$.[^strang][^axler] The **distance** induced by a norm is $d(u, v) = \lVert u - v \rVert$.

## Why it matters

- **Distances between samples.** Clustering, quality-control heatmaps and tree building start from a [[Distance Matrix]] of $\lVert x_i - x_j \rVert$ between sample profiles; the choice of norm changes which samples look close.
- **Normalization.** The $L_1$ norm of a count vector is its total. Dividing by it rescales a sample to a fixed total: TPM values are length-corrected counts divided by their own sum, so every sample sums to $10^6$,[^wagner] an $L_1$ normalization ([[Count Normalization]]). Dividing by the $L_2$ norm instead gives unit vectors, whose dot products are cosines ([[Dot Product]]).
- **Regularization.** Ridge regression penalizes the squared $L_2$ norm of the coefficients, $\lambda \sum_j \beta_j^2$; the lasso penalizes the $L_1$ norm, $\lambda \sum_j |\beta_j|$, and can set some coefficients exactly to zero, which selects variables (for example a small biomarker panel among thousands of genes).[^isl][^stanford] See [[Ridge Regression]], [[Lasso]], [[Regularization]].

## Core (L1)

- **Euclidean ($L_2$).** $\lVert (3, 4) \rVert_2 = \sqrt{9 + 16} = 5$: Pythagoras, extended to $n$ components. It is the "straight line" distance.
- **Manhattan ($L_1$).** $\lVert (3, -4) \rVert_1 = 3 + 4 = 7$: the distance walked along a grid of streets, one axis at a time.
- **Maximum ($L_\infty$).** $\lVert (3, -4) \rVert_\infty = 4$: the largest single coordinate difference.
- **Distances.** For samples $x = (5, 1, 2)$ and $y = (2, 5, 2)$ (invented), $x - y = (3, -4, 0)$, so $d_1 = 7$, $d_2 = 5$, $d_\infty = 4$.
- **Unit vectors.** $v / \lVert v \rVert_2$ has length 1 and the same direction as $v$.

![[vector-norm-unit-balls.svg]]

The **unit ball** $\{v : \lVert v \rVert \le 1\}$ has a different shape for each norm: a diamond for $L_1$, a disc for $L_2$, a square for $L_\infty$.[^strang]

## Deeper (L2)

**The $p$-norms.** For $p \ge 1$, $\lVert v \rVert_p = (\sum_i |v_i|^p)^{1/p}$; $p = 1$ and $p = 2$ are the cases above and $\lVert v \rVert_p \to \lVert v \rVert_\infty$ as $p \to \infty$.[^strang]

**Comparing norms.** For every $v \in \mathbb{R}^n$:
$$\lVert v \rVert_\infty \le \lVert v \rVert_2 \le \lVert v \rVert_1 \le \sqrt n\,\lVert v \rVert_2 \le n\,\lVert v \rVert_\infty.$$
(The middle inequality follows from expanding $(\sum |v_i|)^2$, the next one from Cauchy-Schwarz with the all-ones vector.) The unit balls are nested accordingly (figure). Two norms never disagree by more than a factor depending on $n$, but in high dimension that factor is large.

**Scale dominates.** In $d_2(x, y)^2 = \sum_i (x_i - y_i)^2$ each gene contributes its squared difference. A highly expressed gene whose count moves from 10,000 to 11,000 (+10 %) contributes $10^6$, while a gene going from 20 to 60 (threefold) contributes 1,600: raw-count distances mostly measure the few largest genes. A log transform first (Exercise 4), or standardizing each gene, makes distances reflect relative changes ([[Count Normalization]]).

**$L_2$ and least squares.** Minimizing $\lVert Ax - b \rVert_2^2$ gives linear equations (the normal equations, [[Inverse Matrix]], [[Least Squares]]); minimizing $\lVert Ax - b \rVert_1$ is more robust to outliers but needs [[Linear Programming]] or iterative methods.

## Advanced (L3)

- **Why the lasso gives zeros.** The lasso can be written as minimizing the residual sum of squares subject to $\lVert \beta \rVert_1 \le s$, and ridge with $\lVert \beta \rVert_2^2 \le s$. The $L_1$ ball has corners on the axes, so the constrained optimum often lands on a corner, where some $\beta_j = 0$; the round $L_2$ ball has no corners, so ridge shrinks coefficients without zeroing them.[^isl]
- **The "$L_0$ norm"** $\lVert v \rVert_0 = \#\{i : v_i \ne 0\}$, the number of nonzero components, is not a norm: $\lVert 2v \rVert_0 = \lVert v \rVert_0 \ne 2\lVert v \rVert_0$. Best-subset selection penalizes it; the lasso is its convex relaxation.
- **Norms from inner products.** $\lVert v \rVert_2 = \sqrt{v \cdot v}$ comes from the dot product, and in any inner product space $\lVert v \rVert = \sqrt{\langle v, v \rangle}$ is a norm.[^axler] $L_1$ and $L_\infty$ do not come from any inner product, which is why angles and orthogonal projections are $L_2$ notions.
- **Matrix norms.** The same idea measures matrices: the Frobenius norm $\sqrt{\sum_{ij} a_{ij}^2}$ treats a matrix as a long vector, and the operator norm $\max_{x \ne 0} \lVert Ax \rVert / \lVert x \rVert$ measures how much $A$ can stretch a vector. The condition number of [[Inverse Matrix]] and the error bound of [[Low-Rank Approximation]] are stated in these norms.[^strang]

## Mathematical representation

- $\lVert v \rVert_p = \left(\sum_{i=1}^{n} |v_i|^p\right)^{1/p}$ for $p \ge 1$; $\lVert v \rVert_\infty = \max_{1 \le i \le n} |v_i|$.
- Induced distance: $d_p(x, y) = \lVert x - y \rVert_p$; it is symmetric, zero only for $x = y$, and satisfies $d(x, z) \le d(x, y) + d(y, z)$ (a metric).
- Penalized least squares with a design matrix $X$, response $y$ and $\lambda \ge 0$: ridge minimizes $\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_2^2$, lasso minimizes $\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$ (intercept usually not penalized).[^isl]

## Computational representation

```python
import math


def norm_p(v, p=2):
    """L_p norm; p = math.inf gives the maximum norm."""
    if p == math.inf:
        return max(abs(a) for a in v)
    return sum(abs(a) ** p for a in v) ** (1 / p)


def distance(x, y, p=2):
    return norm_p([a - b for a, b in zip(x, y)], p)


x, y = [5, 1, 2], [2, 5, 2]          # invented sample profiles
print([distance(x, y, p) for p in (1, 2, math.inf)])

counts = [150, 0, 850, 9000]         # invented read counts of one sample
lib = norm_p(counts, 1)              # library size = L1 norm
print(lib, [round(1e6 * c / lib) for c in counts])

beta, lam = [0.5, -2.0, 0.0, 1.5], 0.1
print(round(lam * norm_p(beta, 1), 3), round(lam * norm_p(beta, 2) ** 2, 3))   # lasso, ridge penalties

import numpy as np
d = np.array(x) - np.array(y)
print(np.linalg.norm(d, 1), np.linalg.norm(d), np.linalg.norm(d, np.inf))
```

```text
[7.0, 5.0, 4]
10000.0 [15000, 0, 85000, 900000]
0.4 0.65
7.0 5.0 4.0
```

`math.dist(x, y)` gives the Euclidean distance directly. For a whole data set, compute the $n \times n$ matrix of pairwise distances once and reuse it ([[Distance Matrix]]).

## Worked example

> [!example] Three distances between two samples (invented)
> Samples $x = (5, 1, 2)$ and $y = (2, 5, 2)$, three genes.
> 1. Difference: $x - y = (3, -4, 0)$.
> 2. $L_1$: $|3| + |-4| + |0| = 7$.
> 3. $L_2$: $\sqrt{9 + 16 + 0} = 5$.
> 4. $L_\infty$: $\max(3, 4, 0) = 4$.
> 5. Check the chain: $4 \le 5 \le 7 \le \sqrt3 \times 5 \approx 8.66 \le 3 \times 4 = 12$.
> 6. A third sample $z = (9, 1, 2)$ differs from $x$ in one gene only: $x - z = (-4, 0, 0)$, so $d_1 = d_2 = d_\infty = 4$. Under $L_1$ and $L_2$, $z$ is closer to $x$ than $y$ is ($4 < 7$, $4 < 5$); under $L_\infty$ they tie ($4 = 4$). The ranking of neighbours depends on the norm.

## Common misconceptions

> [!warning] "Distance means Euclidean distance"
> Every norm gives a distance, and the choice changes neighbours, clusters and trees. $L_1$ is less dominated by one large difference; $L_\infty$ is all about the single largest one.

> [!warning] "A distance on raw counts compares expression patterns"
> It mostly compares the most highly expressed genes (Deeper). Transform or standardize first, and decide whether the question is about absolute or relative change.

> [!warning] "Ridge and lasso differ only in strength"
> They differ in shape. The $L_1$ penalty produces exact zeros, the squared $L_2$ penalty does not;[^isl] tuning $\lambda$ cannot turn one into the other.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\lVert v \rVert_1$, $\lVert v \rVert_2$ and $\lVert v \rVert_\infty$ for $v = (1, -2, 2)$, and the unit vector in its direction.

> [!success]- Solution
> $\lVert v \rVert_1 = 5$, $\lVert v \rVert_2 = \sqrt{1 + 4 + 4} = 3$, $\lVert v \rVert_\infty = 2$. Unit vector $v/3 = (\tfrac13, -\tfrac23, \tfrac23)$.

> [!question] Exercise 2 (L1)
> For $v = (0.6, 0.8)$, compute the three norms and locate $v$ on the figure of unit balls.

> [!success]- Solution
> $\lVert v \rVert_1 = 1.4$, $\lVert v \rVert_2 = 1$, $\lVert v \rVert_\infty = 0.8$: $v$ is on the circle, inside the square, outside the diamond.

> [!question] Exercise 3 (L2)
> Prove $\lVert v \rVert_2 \le \lVert v \rVert_1$ and $\lVert v \rVert_1 \le \sqrt n\,\lVert v \rVert_2$. When are they equalities?

> [!success]- Solution
> $\lVert v \rVert_1^2 = \sum_i |v_i|^2 + \sum_{i \ne j} |v_i||v_j| \ge \lVert v \rVert_2^2$, with equality when at most one component is nonzero. With $a = (|v_1|, \dots, |v_n|)$ and $\mathbf{1}$ the all-ones vector, Cauchy-Schwarz gives $\lVert v \rVert_1 = a \cdot \mathbf{1} \le \lVert a \rVert_2 \sqrt n = \sqrt n \lVert v \rVert_2$, with equality when all $|v_i|$ are equal.

> [!question] Exercise 4 (L2, Python)
> Two invented samples have counts $s_1 = (10000, 20, 5)$ and $s_2 = (11000, 60, 1)$. Compute their Euclidean distance on raw counts and on $\log_2(x + 1)$, and say which gene dominates each.

> [!success]- Solution
> ```python
> s1, s2 = [10000, 20, 5], [11000, 60, 1]
> print(round(distance(s1, s2), 1), [b - a for a, b in zip(s1, s2)])
> l1 = [math.log2(c + 1) for c in s1]; l2 = [math.log2(c + 1) for c in s2]
> print(round(distance(l1, l2), 3), [round(b - a, 3) for a, b in zip(l1, l2)])
> # 1000.8 [1000, 40, -4]
> # 2.213 [0.137, 1.538, -1.585]
> ```
> On raw counts the first gene (+10 %) is almost the whole distance; on the log scale the threefold and fivefold changes of genes 2 and 3 dominate.

> [!question] Exercise 5 (L3)
> Show that $\lVert \cdot \rVert_0$ fails one norm axiom, and explain with the figure why minimizing a squared error under $\lVert \beta \rVert_1 \le s$ tends to give exact zeros while $\lVert \beta \rVert_2 \le s$ does not.

> [!success]- Solution
> Homogeneity fails: $\lVert 2v \rVert_0 = \lVert v \rVert_0$. The level sets of the squared error are ellipses around the unconstrained optimum; growing them until they touch the constraint set, they usually first touch the diamond at a corner (a point on an axis, so one coefficient is 0) but touch the disc at a generic point with all coordinates nonzero.[^isl]

## Mastery checklist

- [ ] 1 Recognized: I can name the $L_1$, $L_2$ and $L_\infty$ norms and compute them.
- [ ] 2 Understood: I can state the norm axioms, draw the three unit balls and order the norms of a vector.
- [ ] 3 Practiced: I can implement norms and distances by hand, normalize vectors, and prove the comparison inequalities.
- [ ] 4 Applied: I computed sample distance matrices on real expression data with different norms and transformations, and compared the resulting clusters.
- [ ] 5 Explained: I can explain why raw-count distances mislead, and why the lasso selects variables while ridge does not.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of inner product spaces and norms.
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition (2023), shrinkage methods (ridge regression and the lasso).
[^stanford]: [[Stanford - Statistical Learning with Python]], regularization (ridge, lasso).
[^wagner]: [[Wagner 2012 - Measurement of mRNA Abundance Using RNA-seq Data]], *Theory in Biosciences* 131:281-285.
