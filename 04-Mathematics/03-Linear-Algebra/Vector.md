---
aliases:
  - Column Vector
  - Row Vector
  - Linear Combination
  - Span
  - Vecteur
  - Combinaison linéaire
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Set]]"
  - "[[Function]]"
  - "[[Summation Notation]]"
  - "[[Array]]"
related:
  - "[[Dot Product]]"
  - "[[Vector Norm]]"
  - "[[Matrix]]"
  - "[[Vector Space]]"
  - "[[Linear Independence]]"
  - "[[K-mer]]"
  - "[[Gene Expression]]"
  - "[[Count Matrix]]"
projects: []
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Karlin 1995 - Dinucleotide Relative Abundance Extremes]]"
---

# Vector

> [!abstract]
> A vector is an ordered list of numbers that you can add to another list of the same length and multiply by a number; drawn as an arrow, it turns a table row such as a gene's expression across samples into a point in space.

## Definition

A **vector** of $\mathbb{R}^n$ is an ordered list of $n$ real numbers, its **components**, written as a column $v = (v_1, \dots, v_n)^\top$. Two operations define the algebra: **addition**, component by component, and **scalar multiplication**, which multiplies every component by the same number. Combining both gives a **linear combination** $c_1 v_1 + \dots + c_k v_k$, the basic construction of linear algebra.[^strang][^1806] More generally, a vector is any element of a vector space, a set where these two operations obey the usual rules (functions and polynomials are vectors too).[^axler]

## Why it matters

- **Expression profiles.** An RNA-seq experiment produces a gene by sample table of counts;[^holmes] one row, a gene across $n$ samples, is a vector of $\mathbb{R}^n$, and one column, a sample across $G$ genes, is a vector of $\mathbb{R}^G$ ([[Gene Expression]], [[Count Matrix]]).
- **K-mer count vectors.** Counting the $4^k$ possible [[K-mer|k-mers]] of a genome in a fixed order gives a vector of $\mathbb{R}^{4^k}$. Short-word frequencies differ between genomes and are fairly stable within one, so these vectors act as genomic signatures for alignment-free comparison.[^karlin]
- Every later object of the [[Linear Algebra]] path is built from vectors: [[Dot Product|dot products]] and [[Vector Norm|norms]] compare them, a [[Matrix]] stacks them, $Ax = b$ asks which combination of columns gives $b$.

## Core (L1)

![[vector-addition-dot-product.svg]]

- **Point or arrow.** $v = (3, 1)$ is the point at coordinates 3 and 1, or the arrow from the origin to that point. Both readings matter: points for data (one sample = one point), arrows for directions and differences.[^strang]
- **Addition.** $u + v = (u_1 + v_1, \dots, u_n + v_n)$, defined only when $u$ and $v$ have the same length. Geometrically, place the tail of $v$ on the head of $u$: the sum is the diagonal of the parallelogram (figure, left).
- **Scalar multiplication.** $c\,v = (c v_1, \dots, c v_n)$ stretches the arrow by $|c|$ and reverses it when $c < 0$. $-v$ points the other way; $u - v = u + (-1)v$ is the arrow from the head of $v$ to the head of $u$.
- **Zero vector.** $0 = (0, \dots, 0)$ satisfies $v + 0 = v$.
- **Linear combination.** $c_1 v_1 + \dots + c_k v_k$ with any real coefficients. The mean of two replicate profiles, $\tfrac12 u + \tfrac12 v$, is one; a difference of conditions, $u - v$, is another.
- **Shape conventions.** Linear algebra writes vectors as columns; a **row vector** is the transpose $v^\top = (v_1 \;\dots\; v_n)$. In code both are one-dimensional lists ([[Array]]); the distinction matters once vectors meet matrices ([[Matrix Multiplication]]).

## Deeper (L2)

**Span.** The set of all linear combinations of $v_1, \dots, v_k$ is their **span**. In $\mathbb{R}^3$, the span of one nonzero vector is a line through the origin, the span of two non-parallel vectors is a plane through the origin, and three vectors that do not lie in one plane through the origin span all of $\mathbb{R}^3$.[^strang] Whether $b$ lies in the span of the columns of $A$ is exactly the question "does $Ax = b$ have a solution?" ([[System of Linear Equations]]). Whether a vector of the list is a combination of the others is [[Linear Independence]].

**The rules.** Addition is commutative and associative, scalar multiplication distributes over both sums, $1v = v$, and every $v$ has an opposite $-v$. These rules, not the lists of numbers, are what the abstract definition of a [[Vector Space]] keeps.[^axler]

**Special combinations.** If all $c_i \ge 0$ and $\sum c_i = 1$, the combination is **convex**: it lies "between" the vectors. A probability distribution over 4 nucleotides is a vector with nonnegative components summing to 1, and the composition of a concatenated sequence is the convex combination of the compositions of its parts, weighted by their lengths (Worked example). The same model, a bulk sample as a weighted combination of cell-type profiles, underlies deconvolution ([[System of Linear Equations]]).

## Advanced (L3)

- **Abstract vectors.** Axler's vector spaces include $\mathbb{F}^n$, polynomials and functions:[^axler] a probability density or a coverage track along a chromosome is a vector in a space of functions, and the operations of this note still apply.
- **Dimension grows fast.** A $k$-mer count vector has $4^k$ components: 16 for $k = 2$, 65,536 for $k = 8$, $16{,}777{,}216$ for $k = 12$. A sequence of length $L$ has only $L - k + 1$ k-mers, so for large $k$ most components are zero (Exercise 4). Such vectors are stored as dictionaries of nonzero entries ([[Hash Table]], [[Sparse Matrix]]), not as dense arrays.
- **Linearity of counting.** Counting is additive: the k-mer vector of a concatenation $st$ is $c(s) + c(t)$ plus the $k - 1$ k-mers that cross the junction (Exercise 3). Additivity is what lets k-mer counts be computed in parallel on chunks of a genome and summed.

## Mathematical representation

- $\mathbb{R}^n = \{(v_1, \dots, v_n)^\top : v_i \in \mathbb{R}\}$; $n$ is the dimension, $v_i$ the $i$-th component.
- For $u, v \in \mathbb{R}^n$ and $c \in \mathbb{R}$: $(u + v)_i = u_i + v_i$ and $(cv)_i = c\,v_i$.
- Linear combination: $w = \sum_{j=1}^{k} c_j v_j$, i.e. $w_i = \sum_{j=1}^{k} c_j (v_j)_i$ ([[Summation Notation]]).
- Span: $\operatorname{span}(v_1, \dots, v_k) = \{\sum_j c_j v_j : c_j \in \mathbb{R}\}$.
- Composition vector of a sequence $s$ over $\Sigma = \{A, C, G, T\}$: $c(s) = (\#_A(s), \#_C(s), \#_G(s), \#_T(s))$; frequency vector $f(s) = c(s)/|s|$. For a concatenation, $c(st) = c(s) + c(t)$, hence $f(st) = \frac{|s|}{|s| + |t|} f(s) + \frac{|t|}{|s| + |t|} f(t)$.

## Computational representation

A vector is a list of numbers in pure Python and a one-dimensional `numpy.ndarray` in numerical code. The k-mer vector fixes the component order once (lexicographic), so that two genomes give comparable vectors.

```python
from itertools import product


def add(u, v):
    """Componentwise sum of two vectors of the same length."""
    if len(u) != len(v):
        raise ValueError("vectors must have the same length")
    return [a + b for a, b in zip(u, v)]


def scale(c, v):
    """Scalar multiple c * v."""
    return [c * a for a in v]


def linear_combination(coeffs, vectors):
    """c1*v1 + ... + ck*vk."""
    result = [0] * len(vectors[0])
    for c, v in zip(coeffs, vectors):
        result = add(result, scale(c, v))
    return result


def kmer_vector(seq, k):
    """Count vector of the 4**k k-mers, components in lexicographic order (AA..A first)."""
    index = {"".join(p): i for i, p in enumerate(product("ACGT", repeat=k))}
    counts = [0] * len(index)
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i + k]
        if kmer in index:            # k-mers containing N are skipped
            counts[index[kmer]] += 1
    return counts


# Invented expression profiles of two genes across 3 samples
gene_a = [2.0, 4.0, 6.0]
gene_b = [1.0, 0.0, 3.0]
print(add(gene_a, gene_b), scale(0.5, gene_a))
print(linear_combination([0.5, 0.5], [gene_a, gene_b]))   # mean profile
v = kmer_vector("ACGTACGT", 2)
print(len(v), v)

import numpy as np                   # the same operations, vectorized
a, b = np.array(gene_a), np.array(gene_b)
print(a + b, 0.5 * a + 0.5 * b)
```

```text
[3.0, 4.0, 9.0] [1.0, 2.0, 3.0]
[1.5, 2.0, 4.5]
16 [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0]
[3. 4. 9.] [1.5 2.  4.5]
```

The 2-mer vector of `ACGTACGT` has AC = 2 (component 1), CG = 2 (component 6), GT = 2 (component 11) and TA = 1 (component 12). In NumPy, `+` and `*` act componentwise; on Python lists, `+` concatenates and `2 * list` repeats, a classic bug.

## Worked example

> [!example] Composition of a concatenation (invented sequences)
> $s$ = `ACGTAC` and $t$ = `GGCA`, components in the order (A, C, G, T).
> 1. **Count vectors**: $c(s) = (2, 2, 1, 1)$, $c(t) = (1, 1, 2, 0)$.
> 2. **Sum**: $c(st) = c(s) + c(t) = (3, 3, 3, 1)$; counting `ACGTACGGCA` directly gives the same.
> 3. **Frequency vectors**: $f(s) = (\tfrac13, \tfrac13, \tfrac16, \tfrac16)$, $f(t) = (\tfrac14, \tfrac14, \tfrac12, 0)$.
> 4. **Convex combination** with weights $\tfrac{6}{10}$ and $\tfrac{4}{10}$: A component $0.6 \cdot \tfrac13 + 0.4 \cdot \tfrac14 = 0.2 + 0.1 = \tfrac{3}{10}$; likewise C $= \tfrac{3}{10}$, G $= 0.1 + 0.2 = \tfrac{3}{10}$, T $= 0.1 + 0 = \tfrac{1}{10}$.
> 5. **Check**: $f(st) = c(st)/10 = (\tfrac{3}{10}, \tfrac{3}{10}, \tfrac{3}{10}, \tfrac{1}{10})$. Averaging the two frequency vectors with equal weights would give G $= \tfrac13$: wrong, because the parts have different lengths.

## Common misconceptions

> [!warning] "A vector is an arrow, so data are not vectors"
> Arrows are one picture. Algebraically a vector is anything that can be added and scaled under the rules above;[^axler] an expression profile or a k-mer count table qualifies, and the geometric picture (distances, angles) then applies to it.

> [!warning] "Vectors of different lengths can be added by padding"
> Addition needs the same dimension *and* the same meaning of each component. Two k-mer vectors built with different component orders, or two expression profiles with genes in different orders, have the right length and still give nonsense when added.

> [!warning] "Averaging frequency vectors gives the frequency of the pooled data"
> Only with weights proportional to the sizes of the parts (Worked example). The unweighted mean of per-sample frequencies is a different quantity.

## Exercises

> [!question] Exercise 1 (L1)
> With $u = (1, -2, 0)$ and $v = (2, 1, 4)$, compute $2u - 3v$.

> [!success]- Solution
> $2u = (2, -4, 0)$, $3v = (6, 3, 12)$, so $2u - 3v = (-4, -7, -12)$.

> [!question] Exercise 2 (L1)
> Is $(3, 5)$ a linear combination of $(1, 1)$ and $(1, 2)$? If so, give the coefficients.

> [!success]- Solution
> Solve $a(1, 1) + b(1, 2) = (3, 5)$: $a + b = 3$ and $a + 2b = 5$, so $b = 2$, $a = 1$. Yes: $(3, 5) = 1\,(1, 1) + 2\,(1, 2)$. Since the two vectors are not parallel, every vector of $\mathbb{R}^2$ is such a combination.

> [!question] Exercise 3 (L2, Python)
> Using `kmer_vector` and `add`, check that for $s$ = `ACGTAC`, $t$ = `GGCA` and $k \in \{2, 3\}$, $c(st) = c(s) + c(t) + c(j)$, where $j$ is the last $k - 1$ bases of $s$ followed by the first $k - 1$ bases of $t$. Explain why.

> [!success]- Solution
> ```python
> s, t = "ACGTAC", "GGCA"
> for k in (2, 3):
>     junction = s[-(k - 1):] + t[:k - 1]
>     print(k, kmer_vector(s + t, k) == add(add(kmer_vector(s, k), kmer_vector(t, k)),
>                                          kmer_vector(junction, k)))
> # 2 True
> # 3 True
> ```
> Every k-mer of $st$ lies inside $s$, inside $t$, or crosses the junction. The crossing ones start in the last $k - 1$ positions of $s$, and they are exactly the $k - 1$ k-mers of the string $j$ of length $2k - 2$.

> [!question] Exercise 4 (L3)
> Give the dimension of the k-mer count vector for $k = 1, 2, 3, 8, 12$. For a sequence of 5,000,000 bp (a round number of bacterial-genome scale), what fraction of the 12-mer components must be zero, at least?

> [!success]- Solution
> $4^k$ = 4, 16, 64, 65,536, 16,777,216. The sequence has $5{,}000{,}000 - 11 = 4{,}999{,}989$ 12-mers, so at most that many nonzero components: at least $1 - 4{,}999{,}989 / 16{,}777{,}216 \approx 0.702$ of the components are zero (more in practice, since some 12-mers repeat). Store such vectors sparsely.

## Mastery checklist

- [ ] 1 Recognized: I can say what a vector, a component and a linear combination are.
- [ ] 2 Understood: I can draw $u + v$, $cv$ and $u - v$, describe a span geometrically, and explain the point and arrow readings.
- [ ] 3 Practiced: I can implement vector operations and k-mer count vectors in pure Python, then in NumPy, and prove the concatenation identity.
- [ ] 4 Applied: I built expression-profile vectors from a real count table and k-mer vectors from real genome FASTA files, with a fixed component order.
- [ ] 5 Explained: I can explain convex combinations, why k-mer vectors are sparse, and why component order and weighting are the usual sources of error.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of vector spaces.
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], material on count data from high-throughput sequencing.
[^karlin]: [[Karlin 1995 - Dinucleotide Relative Abundance Extremes]], *Trends in Genetics*.
