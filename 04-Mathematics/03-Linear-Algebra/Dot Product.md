---
aliases:
  - Scalar Product
  - Inner Product
  - Cosine Similarity
  - Angle Between Vectors
  - Produit scalaire
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Vector]]"
  - "[[Summation Notation]]"
related:
  - "[[Vector Norm]]"
  - "[[Matrix Multiplication]]"
  - "[[Orthogonal Projection]]"
  - "[[Correlation]]"
  - "[[K-mer]]"
  - "[[Gene Expression]]"
  - "[[Position Weight Matrix]]"
  - "[[Alignment-Free Sequence Comparison]]"
projects: []
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[Karlin 1995 - Dinucleotide Relative Abundance Extremes]]"
---

# Dot Product

> [!abstract]
> The dot product multiplies two vectors component by component and adds the results; that single number measures how much the vectors point the same way, which is how expression profiles and k-mer spectra are compared.

## Definition

The **dot product** of $u, v \in \mathbb{R}^n$ is the number $u \cdot v = u_1 v_1 + \dots + u_n v_n$. It equals $\lVert u \rVert \lVert v \rVert \cos\theta$, where $\lVert \cdot \rVert$ is the length ([[Vector Norm]]) and $\theta$ the angle between the vectors; $u$ and $v$ are **orthogonal** (perpendicular) when $u \cdot v = 0$.[^strang][^1806] The dot product is the standard **inner product** of $\mathbb{R}^n$.[^axler]

## Why it matters

- **Similarity of expression profiles.** The cosine $\frac{u \cdot v}{\lVert u \rVert \lVert v \rVert}$ compares the *shape* of two gene profiles regardless of their overall level, and Pearson [[Correlation]] is the same cosine after centering (Deeper).
- **Similarity of k-mer spectra.** Short-word frequencies are genome signatures,[^karlin] so the cosine of two [[K-mer]] count vectors is a simple alignment-free similarity ([[Alignment-Free Sequence Comparison]]).
- **Hidden in other operations.** Each entry of a matrix product is a dot product ([[Matrix Multiplication]]); a linear model predicts $\hat y = x \cdot \beta$; the score of a k-mer under a [[Position Weight Matrix]] is a dot product (Exercise 5).

## Core (L1)

![[vector-addition-dot-product.svg]]

- **Compute.** Multiply matching components and add: $(1, 2, 3) \cdot (4, -5, 6) = 4 - 10 + 18 = 12$. The vectors must have the same length; the result is a number, not a vector.
- **Rules.** $u \cdot v = v \cdot u$; $u \cdot (v + w) = u \cdot v + u \cdot w$; $(cu) \cdot v = c\,(u \cdot v)$; and $v \cdot v = v_1^2 + \dots + v_n^2 = \lVert v \rVert^2 \ge 0$.[^strang]
- **Angle.** $\cos\theta = \dfrac{u \cdot v}{\lVert u \rVert\,\lVert v \rVert}$. Positive dot product: angle below 90°; zero: perpendicular; negative: above 90°.[^strang]
- **Cosine similarity** is this cosine, between $-1$ and $1$. For vectors with nonnegative components (counts), it lies between 0 and 1.
- **Projection.** $\frac{u \cdot v}{\lVert u \rVert}$ is the signed length of the shadow of $v$ on the direction of $u$ (figure, right).

## Deeper (L2)

**Cauchy-Schwarz inequality.** $|u \cdot v| \le \lVert u \rVert\,\lVert v \rVert$, with equality exactly when one vector is a multiple of the other.[^strang] It guarantees that the cosine formula gives a number in $[-1, 1]$, so the angle is well defined in any dimension, including a space with one axis per gene.

**Cosine ignores scale, not shifts.** Multiplying a profile by $c > 0$ (a deeper library, a brighter array) leaves the cosine unchanged. Adding a constant to every component changes it: cosine compares directions from the origin, so a high baseline makes all profiles look alike.

**Correlation is a centered cosine.** With $\bar u$ the mean of the components and $\tilde u = u - \bar u\,\mathbf{1}$ the centered vector,
$$r(u, v) = \frac{\sum_i (u_i - \bar u)(v_i - \bar v)}{\sqrt{\sum_i (u_i - \bar u)^2}\,\sqrt{\sum_i (v_i - \bar v)^2}} = \frac{\tilde u \cdot \tilde v}{\lVert \tilde u \rVert\,\lVert \tilde v \rVert}.$$
Pearson's $r$ is the cosine of the angle between centered profiles, so it detects anti-correlation that raw cosine on positive data cannot (Worked example).

**Projection onto a line.** The multiple of $u$ closest to $v$ is $\frac{u \cdot v}{u \cdot u}\,u$, and $v$ minus it is orthogonal to $u$.[^strang] This is the first step of [[Orthogonal Projection]] and [[Least Squares]].

## Advanced (L3)

- **Other inner products.** Axler defines an inner product by positivity, definiteness, linearity in the first slot and (conjugate) symmetry; the dot product is one example.[^axler] A weighted version $\sum_i w_i u_i v_i$ with $w_i > 0$ (for instance down-weighting noisy genes) is another, and all the geometry (angles, projections, Cauchy-Schwarz) carries over.
- **High dimension.** For random vectors with independent $\pm 1$ components, $u \cdot v$ is a sum of $n$ independent $\pm 1$ terms with variance $n$, while $\lVert u \rVert \lVert v \rVert = n$; the cosine therefore has standard deviation $1/\sqrt n$. In 10,000 dimensions unrelated vectors are almost orthogonal, so a cosine of 0.1 can already be meaningful, while in 4 dimensions it is noise.
- **Cosine distance is not a metric.** $1 - \cos\theta$ violates the triangle inequality (Common misconceptions); the angle $\theta$ itself, or the Euclidean distance between unit-normalized vectors, are metrics. Clustering code that assumes a metric must be given one ([[Vector Norm]]).

## Mathematical representation

- $u \cdot v = \sum_{i=1}^{n} u_i v_i = u^\top v$ (a $1 \times n$ row times an $n \times 1$ column, [[Matrix Multiplication]]).
- $\lVert v \rVert = \sqrt{v \cdot v}$; $\cos\theta = \frac{u \cdot v}{\lVert u \rVert \lVert v \rVert}$ for nonzero $u, v$; $u \perp v \iff u \cdot v = 0$.
- Projection of $v$ on the line of $u$: $p = \frac{u \cdot v}{u \cdot u}\,u$, with $(v - p) \cdot u = 0$.

## Computational representation

```python
import math
import statistics


def dot(u, v):
    """Sum of componentwise products."""
    if len(u) != len(v):
        raise ValueError("vectors must have the same length")
    return sum(a * b for a, b in zip(u, v))


def norm(v):
    return math.sqrt(dot(v, v))


def cosine(u, v):
    return dot(u, v) / (norm(u) * norm(v))


def angle_degrees(u, v):
    c = max(-1.0, min(1.0, cosine(u, v)))   # guard against rounding just outside [-1, 1]
    return math.degrees(math.acos(c))


def center(v):
    m = sum(v) / len(v)
    return [a - m for a in v]


def pearson(u, v):
    """Pearson correlation = cosine of the centered vectors."""
    return cosine(center(u), center(v))


# Invented expression profiles of three genes across 4 samples
g1, g2, g3 = [2, 4, 6, 8], [1, 2, 3, 5], [8, 6, 4, 2]
print(dot(g1, g2), round(cosine(g1, g2), 3), round(angle_degrees(g1, g2), 1))
print(round(cosine(g1, g3), 3), round(pearson(g1, g3), 3))
print(round(cosine(g1, [10 * a for a in g2]), 3), round(cosine(g1, [a + 100 for a in g2]), 3))
print(round(pearson(g1, g2), 4), round(statistics.correlation(g1, g2), 4))
```

```text
68 0.994 6.3
0.667 -1.0
0.994 0.919
0.9827 0.9827
```

Line 3: scaling `g2` by 10 keeps the cosine; adding 100 to every sample changes it. Line 4: the centered cosine matches the standard library's Pearson correlation. In NumPy, `u @ v` or `np.dot(u, v)` computes the dot product.

## Worked example

> [!example] Two genes that look similar, one that is opposite (invented data)
> $g_1 = (2, 4, 6, 8)$, $g_2 = (1, 2, 3, 5)$, $g_3 = (8, 6, 4, 2)$ across 4 samples.
> 1. $g_1 \cdot g_2 = 2 + 8 + 18 + 40 = 68$.
> 2. $\lVert g_1 \rVert = \sqrt{120} \approx 10.954$, $\lVert g_2 \rVert = \sqrt{39} \approx 6.245$.
> 3. $\cos\theta = 68 / (10.954 \times 6.245) \approx 0.994$, $\theta \approx 6.3°$: almost the same direction.
> 4. $g_1 \cdot g_3 = 16 + 24 + 24 + 16 = 80$ and $\lVert g_3 \rVert = \sqrt{120}$, so $\cos = 80/120 \approx 0.667$: apparently "similar".
> 5. Centered: $\tilde g_1 = (-3, -1, 1, 3)$, $\tilde g_3 = (3, 1, -1, -3) = -\tilde g_1$, so $r = -1$: $g_3$ is perfectly anti-correlated with $g_1$. Raw cosine on positive data hid it.

## Common misconceptions

> [!warning] "A positive cosine means the profiles go up and down together"
> For count data every vector lies in the positive orthant, so all cosines are at least 0 and often large (0.667 for exactly opposite trends above). Center first, or use [[Correlation]], when the question is co-variation.

> [!warning] "1 − cosine is a distance like any other"
> Take unit vectors at 0°, 45° and 90°: $1 - \cos 90° = 1$, but going through the middle one costs $2(1 - \cos 45°) \approx 0.586 < 1$. The triangle inequality fails, so methods that assume a metric can misbehave.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $u \cdot v$ and the angle between $u = (1, 1, 0)$ and $v = (0, 1, 1)$.

> [!success]- Solution
> $u \cdot v = 0 + 1 + 0 = 1$; $\lVert u \rVert = \lVert v \rVert = \sqrt 2$; $\cos\theta = 1/2$, so $\theta = 60°$.

> [!question] Exercise 2 (L1)
> Find all vectors $(x, y)$ orthogonal to $(3, -2)$, and one of length 1.

> [!success]- Solution
> $3x - 2y = 0$, so $(x, y) = t\,(2, 3)$: a line through the origin. Length 1: $(2, 3)/\sqrt{13}$ (or its opposite).

> [!question] Exercise 3 (L2)
> Show that $r(u, v) = 1$ when $v = a\,u + b\,\mathbf{1}$ with $a > 0$, using the centered-cosine formula. What is $r$ when $a < 0$?

> [!success]- Solution
> Centering removes $b\,\mathbf{1}$: $\tilde v = a\,\tilde u$. Then $\tilde u \cdot \tilde v = a \lVert \tilde u \rVert^2$ and $\lVert \tilde v \rVert = |a|\,\lVert \tilde u \rVert$, so $r = a/|a| = 1$; for $a < 0$, $r = -1$. Cauchy-Schwarz says these are the only cases of $|r| = 1$.

> [!question] Exercise 4 (L2, Python)
> With `cosine` above and the `kmer_vector` function of [[Vector]], compute the cosine of the 2-mer vectors of the invented sequences `ACGTACGTAC` and `ACGTTCGTAC`, then of `ACGTACGTAC` and `GGGCCCGGGC`. Interpret.

> [!success]- Solution
> ```python
> s1, s2, s3 = "ACGTACGTAC", "ACGTTCGTAC", "GGGCCCGGGC"
> for name, t in (("s2", s2), ("s3", s3)):
>     print(name, round(cosine(kmer_vector(s1, 2), kmer_vector(t, 2)), 3))
> # s2 0.901
> # s3 0.087
> ```
> $s_1$ and $s_2$ differ by one base and share most 2-mers (AC, CG, GT, TA). $s_3$ shares only CG with $s_1$: dot product $2 \times 1 = 2$, divided by $\sqrt{21} \times 5$.

> [!question] Exercise 5 (L3, Python)
> A toy position weight matrix (invented) gives a score $W[b][j]$ to base $b$ at position $j$ of a 3-mer. Encode a 3-mer as a one-hot vector of length 12 (4 bases × 3 positions) and show that its score $\sum_j W[x_j][j]$ is a dot product with the flattened weights.

> [!success]- Solution
> ```python
> W = {"A": [1.0, -1.0, 0.5], "C": [-1.0, 2.0, -0.5], "G": [0.0, -1.0, 1.5], "T": [-0.5, 0.0, -1.0]}
>
> def one_hot(kmer):
>     return [1 if kmer[j] == b else 0 for j in range(len(kmer)) for b in "ACGT"]
>
> w_flat = [W[b][j] for j in range(3) for b in "ACGT"]
> for kmer in ("ACG", "TTT"):
>     print(kmer, dot(one_hot(kmer), w_flat), sum(W[kmer[j]][j] for j in range(3)))
> # ACG 4.5 4.5
> # TTT -1.5 -1.5
> ```
> The one-hot vector selects exactly one weight per position, so the dot product adds the selected weights. Scanning a genome with a PWM is a sequence of dot products, which is why it vectorizes well.

## Mastery checklist

- [ ] 1 Recognized: I can compute $u \cdot v$ and say what a zero dot product means.
- [ ] 2 Understood: I can derive the angle and the projection from the dot product and state Cauchy-Schwarz.
- [ ] 3 Practiced: I can implement dot product, cosine and Pearson correlation by hand and match library results.
- [ ] 4 Applied: I compared real expression profiles or k-mer spectra with cosine and with correlation and explained the differences.
- [ ] 5 Explained: I can explain scale versus shift invariance, near-orthogonality in high dimension, and why $1 - \cos$ is not a metric.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of inner product spaces.
[^karlin]: [[Karlin 1995 - Dinucleotide Relative Abundance Extremes]], *Trends in Genetics*.
