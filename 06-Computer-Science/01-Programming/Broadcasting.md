---
aliases:
  - Broadcasting Rules
  - NumPy Broadcasting
  - Array Broadcasting
  - np.newaxis
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[N-Dimensional Array]]"
  - "[[Vectorization]]"
  - "[[Array Indexing]]"
related:
  - "[[Distance Matrix]]"
  - "[[Vector Norm]]"
  - "[[Hamming Distance]]"
  - "[[Matrix Multiplication]]"
  - "[[Floating-Point Arithmetic]]"
  - "[[Count Normalization]]"
  - "[[Standard Score]]"
  - "[[Data Frame]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[Harris 2020 - Array Programming with NumPy]]"
---

# Broadcasting

> [!abstract]
> Broadcasting lets NumPy combine arrays of different shapes by aligning their shapes from the right and stretching length-1 axes without copying: a genes × samples matrix divided by a per-sample vector, or all $n \times m$ pairwise distances from an $(n, 1, d)$ and a $(1, m, d)$ array, each in one expression.

## Definition

**Broadcasting** is the rule by which an element-wise operation applies to arrays of different shapes. Two arrays are compatible if, for each trailing dimension (comparing the shapes from the end), the axis lengths match or one of them is 1; the operation is then performed over the missing or length-1 dimensions as if they were repeated.[^mcka] It is part of NumPy's vectorized computation, for instance in the multiplication of two-dimensional arrays of different shapes, and the same rule aligns index arrays in advanced indexing ([[Array Indexing]]).[^harris] The repetition is virtual: a stretched axis gets stride 0 and no data is copied (Core).

## Why it matters

- **Scaling and centering.** Dividing each sample (column) by its library size or subtracting each gene's (row's) mean is one broadcast ([[Count Normalization]], [[Standard Score]]); so is scoring sequence windows against a weight matrix ([[N-Dimensional Array#Advanced (L3)]]).
- **All pairs at once.** Sample-to-sample distances for quality control and clustering ([[Distance Matrix]], [[Hierarchical Clustering]]), Hamming distances between barcodes ([[Hamming Distance]]) and p-distances between aligned sequences for [[08-phylogenetic-engine]] are each one expression.
- **Silent errors and hidden costs.** An axis that broadcasts by accident produces plausible values and no error, and an $(n, m, d)$ intermediate is real memory: $n = m = 1000$ samples and $d = 20\,000$ genes would need $8 \times 10^6 \times 2 \times 10^4$ B = 160 GB in `float64` (Advanced).

## Core (L2)

Outputs come from NumPy 2.4.6 and SciPy 1.17.1 on Python 3.11.

![[broadcasting-shape-alignment.svg]]

**The rule in three steps.** Right-align the two shapes; pad the shorter one with 1s on the left; on each axis the lengths must be equal or one of them must be 1, and the result takes the larger.[^mcka] To act along an axis that is not the last, give the smaller array an explicit length-1 axis.[^mcka]

```python
import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform

counts = np.array([[120, 100, 90, 400, 380, 420],
                   [30, 45, 38, 10, 12, 9],
                   [0, 2, 1, 1, 0, 3],
                   [50, 53, 47, 0, 60, 55]])                 # invented: 4 genes x 6 samples
lib = counts.sum(axis=0)                                      # (6,): one total per sample
cpm = counts / lib * 1e6                                      # (4, 6) / (6,) -> (4, 6)
print(lib, cpm.shape, cpm.sum(axis=0))
try:
    counts - counts.mean(axis=1)                              # (4, 6) - (4,): per-gene means, wrong axis
except ValueError as err:
    print("ValueError:", err)
centered = counts - counts.mean(axis=1, keepdims=True)       # (4, 6) - (4, 1)
print(np.allclose(centered.mean(axis=1), 0), np.broadcast_shapes((5, 1, 3), (1, 7, 3)))
```

```text
[200 200 176 411 452 487] (4, 6) [1000000. 1000000. 1000000. 1000000. 1000000. 1000000.]
ValueError: operands could not be broadcast together with shapes (4,6) (4,)
True (5, 7, 3)
```

Dividing by `lib` rescales every sample to a total of one million (counts per million; which scaling to use is the subject of [[Count Normalization]]). The per-gene means have shape `(4,)`, which lines up with the 6 samples, not the 4 genes: `keepdims=True` keeps them as a `(4, 1)` column.

**Adding an axis, and why nothing is copied.** `v[:, None]` makes a column and `v[None, :]` a row (`None` is `np.newaxis`); `np.expand_dims` does the same by axis number. The stretched operand exists only as strides:

```python
print(np.newaxis is None, lib[:, None].shape, lib[None, :].shape, np.expand_dims(lib, 0).shape)
v = np.broadcast_to(lib, (4, 6))
print(v.shape, v.strides, v.flags.writeable, np.shares_memory(v, lib))
```

```text
True (6, 1) (1, 6) (1, 6)
(4, 6) (0, 8) False True
```

Stride 0 on axis 0 means every row of `v` is the same 48 bytes of `lib`; the view is read-only because writing one element would change all four rows. A column against a row, `x[:, None] - y`, is an outer operation, like the ufunc method `np.subtract.outer` ([[Vectorization#Advanced (L3)]]).

**All pairwise distances in one expression.** With samples as the rows of `X` ($n \times d$), `X[:, None, :] - X[None, :, :]` has shape $(n, n, d)$ and holds every difference vector $x_i - x_j$. Squaring, summing over the last axis and taking the square root gives the Euclidean [[Distance Matrix]] ([[Vector Norm]]). On log-scaled values of the genes with at least 20 reads (a mask, [[Array Indexing]]):

```python
keep = counts.sum(axis=1) >= 20                               # drop the low-count gene g3
X = np.log2(cpm[keep] + 1).T                                  # samples x genes: (6, 3)
diff = X[:, None, :] - X[None, :, :]                          # (6, 1, 3) - (1, 6, 3) -> (6, 6, 3)
D = np.sqrt((diff ** 2).sum(axis=-1))                         # (6, 6)
print(D.round(2))
print(np.allclose(D, cdist(X, X)), np.allclose(D, D.T), np.diag(D).max())
print((D + np.diag(np.full(len(D), np.inf))).argmin(axis=1))  # nearest other sample
```

```text
[[ 0.    0.65  0.58 18.14  2.7   3.27]
 [ 0.65  0.    0.07 18.32  3.33  3.89]
 [ 0.58  0.07  0.   18.32  3.27  3.83]
 [18.14 18.32 18.32  0.   17.02 16.79]
 [ 2.7   3.33  3.27 17.02  0.    0.57]
 [ 3.27  3.89  3.83 16.79  0.57  0.  ]]
True True 0.0
[2 2 1 5 5 4]
```

The matrix agrees with SciPy's `cdist`, is symmetric with a zero diagonal, and its nearest neighbours pair the control samples S1 to S3 together and S5 with S6. S4 is far from everything: its 0 reads for g4 become $\log_2 1 = 0$ against 16.8 to 18.0 for the others, an outlier to inspect before any test.

## Advanced (L3)

**Silent broadcasts.** Broadcasting checks shapes, not meaning:

```python
M = np.array([[1., 2., 3.], [10., 20., 30.], [100., 200., 300.]])   # invented 3 genes x 3 samples
wrong = M / M.sum(axis=1)                                     # runs: divides column j by the total of row j
right = M / M.sum(axis=1, keepdims=True)
print(wrong.sum(axis=1).round(3), right.sum(axis=1))
yv = np.array([1.0, 2.0, 3.0])
yhat = np.array([[1.1], [1.9], [3.2]])                       # predictions stored as a column
print((yv - yhat).shape, ((yv - yhat) ** 2).mean().round(4), ((yv - yhat.ravel()) ** 2).mean().round(4))
```

```text
[ 0.205  2.05  20.5  ] [1. 1. 1.]
(3, 3) 1.42 0.02
```

With a square matrix the row totals, shape $(3,)$, line up with the columns, and the "row fractions" do not sum to 1. With predictions stored as a column, $(3,) - (3, 1)$ is an outer difference: the "mean squared error" averages 9 pairs instead of 3 residuals and is 70 times too large. Defenses: `keepdims=True` on every reduction you divide by, a shape comment on every broadcast, `assert result.shape == expected`, and labeled axes when the data has labels ([[Data Frame]] aligns by label, not position).

**In-place operations keep the dtype.** `counts / lib` allocates a new `float64` array, but `counts /= lib` would have to store floats in the integer buffer and fails; convert first (`counts.astype(np.float64)`), then divide in place:

```python
c = counts.copy()
try:
    c /= lib
except TypeError as err:
    print(type(err).__name__, err)
```

```text
UFuncTypeError Cannot cast ufunc 'divide' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

**Memory, chunks and the Gram identity.** The $(n, m, d)$ difference array costs $8nmd$ bytes in `float64`. Processing $b$ rows at a time bounds it by $8bmd$; expanding the square, $\lVert x - y \rVert^2 = \lVert x \rVert^2 + \lVert y \rVert^2 - 2\, x \cdot y$, needs only the $(n, m)$ result and one [[Matrix Multiplication]]. The price of the Gram form is cancellation when two points are close compared with their norms ([[Floating-Point Arithmetic]]):

```python
sq = (X ** 2).sum(axis=1)
D2 = sq[:, None] + sq[None, :] - 2 * X @ X.T                  # (6, 6): no (6, 6, 3) temporary
print(np.abs(np.sqrt(np.clip(D2, 0, None)) - D).max(), D2.min(), np.allclose(np.einsum("ik,jk->ij", X, X), X @ X.T))
P = np.array([[1e6, 1e6], [1e6 + 1e-3, 1e6]])                 # invented: two close points far from the origin
sqP = (P ** 2).sum(axis=1)
gram = sqP[:, None] + sqP[None, :] - 2 * P @ P.T
direct = np.sqrt(((P[:, None, :] - P[None, :, :]) ** 2).sum(axis=-1))
print(direct[0, 1], gram[0, 1])
print(np.allclose(squareform(pdist(X)), D), pdist(X).shape)
```

```text
4.76837158203125e-07 -2.2737367544323206e-13 True
0.0010000000474974513 0.0
True (15,)
```

On the toy data both forms agree to within $5 \times 10^{-7}$, but the smallest Gram "squared distance" is slightly negative: always clip before the square root. For the two close points, the Gram form returns exactly 0 where the true distance is $10^{-3}$ (see the error bound below). `pdist` returns the condensed upper triangle, $n(n-1)/2 = 15$ values, which `squareform` expands; `np.einsum("ik,jk->ij", X, Y)` spells the product $X Y^\top$ of the Gram form. Use the direct form, chunked, when points may be close relative to their norms; the Gram form is safe after centering, which shrinks the norms.

## Mathematical representation

- Let $a = (a_1, \dots, a_p)$ and $b = (b_1, \dots, b_q)$ be shapes and $r = \max(p, q)$. Pad on the left: $\hat a_k = 1$ for $k \le r - p$ and $\hat a_k = a_{k - (r - p)}$ otherwise; same for $\hat b$.
- **Compatibility**: for every $k$, $\hat a_k = \hat b_k$ or $\hat a_k = 1$ or $\hat b_k = 1$. The result has shape $c_k = \max(\hat a_k, \hat b_k)$.
- **Element rule**: for an index $i$ of the result, $C(i) = f\big(\hat A(\pi_a(i)), \hat B(\pi_b(i))\big)$ with $\pi_a(i)_k = i_k$ if $\hat a_k = c_k$ and $0$ if $\hat a_k = 1 < c_k$. In memory, $\pi$ is implemented by a stride of 0 on the stretched axes.
- **Pairwise distances**: $D_{ij} = \sqrt{\sum_{k=1}^{d} (X_{ik} - Y_{jk})^2}$ broadcasts $\tilde X$ of shape $(n, 1, d)$ against $\tilde Y$ of shape $(1, m, d)$ to $(n, m, d)$, then reduces over $k$. Direct form: $nmd$ operations and $nmd$ intermediate values; Gram form: the same operation count inside one matrix product and $nm$ values.
- **Gram identity and its error**: $\sum_k (x_k - y_k)^2 = \sum_k x_k^2 + \sum_k y_k^2 - 2 \sum_k x_k y_k$. Each term carries a rounding error of relative size about $\varepsilon = 2^{-52} \approx 2.2 \times 10^{-16}$, so the computed squared distance has an absolute error of order $\varepsilon \left(\lVert x \rVert^2 + \lVert y \rVert^2\right)$, a relative error of order $\varepsilon \left(\lVert x \rVert^2 + \lVert y \rVert^2\right) / \lVert x - y \rVert^2$. For the points $P$: $2.2 \times 10^{-16} \times 4 \times 10^{12} / 10^{-6} \approx 900$, so no correct digit can survive.
- **Hamming distances**: $H_{ij} = \sum_{k} [B_{ik} \ne B_{jk}]$, the same broadcast with $\ne$ in place of the squared difference ([[Hamming Distance]]). If $d_{\min} = \min_{i \ne j} H_{ij} \ge 2t + 1$, a barcode read with at most $t$ errors stays closer to its true barcode than to any other: by the triangle inequality, $H(r, b_{\text{other}}) \ge d_{\min} - t \ge t + 1 > t \ge H(r, b_{\text{true}})$.

## Computational representation

| Goal | Expression | Shapes |
|---|---|---|
| scale columns (per sample) | `M / v` | $(g, s) / (s,)$ |
| scale rows (per gene) | `M / v[:, None]` or `keepdims=True` | $(g, s) / (g, 1)$ |
| center rows | `M - M.mean(axis=1, keepdims=True)` | $(g, s) - (g, 1)$ |
| outer operation | `x[:, None] - y`, `np.subtract.outer(x, y)` | $(n, 1) - (m,) \to (n, m)$ |
| all pairs of vectors | `X[:, None, :] - Y[None, :, :]` | $(n, 1, d) - (1, m, d) \to (n, m, d)$ |
| stretched view, no copy | `np.broadcast_to(v, shape)` | stride 0, read-only |
| check before computing | `np.broadcast_shapes(a, b)` | raises if incompatible |

## Worked example

> [!example] Why the low-count gene was filtered before computing distances
> Same invented matrix, but all four genes kept.
> 1. **Log-scaled g3**: its counts `[0, 2, 1, 1, 0, 3]` over library sizes of about 200 reads become `[0, 10000, 5682, 2433, 0, 6160]` counts per million, so $\log_2(\mathrm{CPM} + 1)$ jumps from 0 to between 11.2 and 13.3 as soon as a sample has 1 to 3 reads.
> 2. **Distances with g3**: one expression as above, on `np.log2(cpm + 1).T`.
> ```python
> X_all = np.log2(cpm + 1).T                                    # samples x all 4 genes
> D_all = np.sqrt(((X_all[:, None, :] - X_all[None, :, :]) ** 2).sum(axis=-1))
> print(D_all[0].round(2), (D_all + np.diag(np.full(6, np.inf))).argmin(axis=1))
> ```
> ```text
> [ 0.   13.3  12.49 21.34  2.7  13.01] [4 2 1 5 0 2]
> ```
> 3. **Read the result**: S1 (control) now has S5 (heat) as nearest neighbour, at 2.70, because both have 0 reads for g3; S1 and S2 are 13.30 apart, almost all of it from g3's 0 versus 2 reads.
> 4. **Fix**: drop genes too poorly measured to inform a distance (here the total ≥ 20 mask), which restores the within-condition neighbours of the Core section.
> 5. **Scale matters**: these toy libraries hold about 200 reads, so one read is about 5,000 counts per million. With $10^7$ reads, one read is 0.1 counts per million and $\log_2 1.1 \approx 0.14$, a small jump. The general lesson stands: check which coordinates drive a distance before trusting the neighbours.

## Common misconceptions

> [!warning] "Broadcasting copies the smaller array"
> The stretched operand is a stride-0 view (`np.broadcast_to` shows strides `(0, 8)`), so it costs nothing. The result and any intermediate, such as the $(n, m, d)$ differences, are allocated in full.

> [!warning] "If NumPy accepts the shapes, the operation is the intended one"
> A square matrix divided by its row sums, or a `(n,)` array minus a `(n, 1)` array, runs without error and gives wrong numbers. Shape compatibility is not a correctness check.

> [!warning] "The Gram formula gives the same distances, faster"
> It gives them in less memory, but with cancellation: small negative squared distances, and distance 0 for close points far from the origin. Clip at 0, center first, or use the direct form.

## Exercises

> [!question] Exercise 1 (L2)
> Give the result shape, or say that the operation fails: $(3, 4) + (4,)$, $(3, 4) + (3,)$, $(3, 4) + (3, 1)$, $(5, 1, 4) \times (3, 1)$, $(2, 1) \times (1, 3)$, $(6,) \times (6, 1)$.

> [!success]- Solution
> Right-align and compare: $(3, 4)$; fails ($4 \ne 3$ on the last axis); $(3, 4)$; $(5, 3, 4)$ ($(3, 1)$ is padded to $(1, 3, 1)$); $(2, 3)$; $(6, 6)$, an outer product that is often a bug. `np.broadcast_shapes` returns exactly these shapes and raises for the second.

> [!question] Exercise 2 (L2, Python)
> Compute per-gene z-scores of `np.log2(cpm + 1)` (genes × samples) in one expression and check that every gene has mean 0 and standard deviation 1 ([[Standard Score]]).

> [!success]- Solution
> ```python
> Lg = np.log2(cpm + 1)                                         # genes x samples
> z = (Lg - Lg.mean(axis=1, keepdims=True)) / Lg.std(axis=1, ddof=1, keepdims=True)
> print(z.mean(axis=1).round(12), z.std(axis=1, ddof=1), z[3, 3].round(2))
> ```
> ```text
> [-0. -0.  0.  0.] [1. 1. 1. 1.] -2.04
> ```
> Both reductions keep their axis, so $(4, 6)$ is combined with $(4, 1)$ twice; S4's zero for g4 stands out at $z = -2.04$. `ddof=1` divides by $n - 1$; whichever you choose, use the same value in the check.

> [!question] Exercise 3 (L3, Python)
> A pool of samples is tagged with the invented 8-nt barcodes `ACGTACGT`, `TGCATGCA`, `GATCCTAG`, `ACGAACGT`, `CTAGGATC` ([[Demultiplexing]]). Compute all pairwise Hamming distances in one expression, the minimum distance, and the pairs closer than 3. How many sequencing errors per barcode can be corrected unambiguously?

> [!success]- Solution
> ```python
> barcodes = [b"ACGTACGT", b"TGCATGCA", b"GATCCTAG", b"ACGAACGT", b"CTAGGATC"]   # invented
> B = np.frombuffer(b"".join(barcodes), dtype=np.uint8).reshape(len(barcodes), -1)
> H = (B[:, None, :] != B[None, :, :]).sum(axis=-1)
> print(H)
> iu = np.triu_indices(len(B), k=1)
> print(H[iu].min(), [(int(i), int(j), int(H[i, j])) for i, j in zip(*iu) if H[i, j] < 3])
> ```
> ```text
> [[0 8 8 1 8]
>  [8 0 8 7 8]
>  [8 8 0 8 8]
>  [1 7 8 0 8]
>  [8 8 8 8 0]]
> 1 [(0, 3, 1)]
> ```
> Barcodes 0 and 3 differ at one position, so $d_{\min} = 1$: a single error in `ACGTACGT` can produce `ACGAACGT`, another valid barcode, and even detection fails. Correcting $t$ errors needs $d_{\min} \ge 2t + 1$ (Mathematical representation); without barcode 3 every remaining pair is at distance 8, enough for $t = 3$.

> [!question] Exercise 4 (L3, Python)
> For the invented alignment below, compute the matrix of p-distances (proportion of differing sites) between all pairs, ignoring every site where either sequence has a gap, as a first step towards a tree in [[08-phylogenetic-engine]] ([[Evolutionary Distance]]).
> ```text
> s0  ATGCTAGC-TTA
> s1  ATGCTAGCATTA
> s2  ATGATAGC-TCA
> s3  TTGATAGCATCA
> s4  ATG-TAGCATTA
> ```

> [!success]- Solution
> ```python
> aln = [b"ATGCTAGC-TTA", b"ATGCTAGCATTA", b"ATGATAGC-TCA", b"TTGATAGCATCA", b"ATG-TAGCATTA"]   # invented
> S = np.frombuffer(b"".join(aln), dtype=np.uint8).reshape(len(aln), -1)
> ok = S != ord("-")
> both = ok[:, None, :] & ok[None, :, :]                        # (5, 5, 12): no gap in either sequence
> mism = (S[:, None, :] != S[None, :, :]) & both
> p = mism.sum(axis=-1) / both.sum(axis=-1)
> print(p.round(3))
> ```
> ```text
> [[0.    0.    0.182 0.273 0.   ]
>  [0.    0.    0.182 0.25  0.   ]
>  [0.182 0.182 0.    0.091 0.1  ]
>  [0.273 0.25  0.091 0.    0.182]
>  [0.    0.    0.1   0.182 0.   ]]
> ```
> The gap mask is broadcast pairwise like the sequences, so each pair has its own number of comparable sites (10 to 12 in `both.sum(axis=-1)`). s0 and s1 differ only at s0's gap, which is excluded, hence distance 0. This "pairwise deletion" is a choice: dropping every column with a gap in any sequence is the other common convention, and it changes the distances.

## Mastery checklist

- [ ] 1 Recognized: I can state the broadcasting rule and give the result shape of two compatible shapes.
- [ ] 2 Understood: I can explain why a stretched array costs no memory, why shapes align from the right, and when broadcasting silently does the wrong thing.
- [ ] 3 Practiced: I can scale, center and z-score a count matrix and compute Euclidean, Hamming and p-distance matrices in one expression each, checking them against SciPy or a loop.
- [ ] 4 Applied: [[08-phylogenetic-engine]] builds its distance matrix from an alignment by broadcasting, within a stated memory budget.
- [ ] 5 Explained: I can teach the memory cost of pairwise broadcasts, the chunked and Gram alternatives, and the cancellation error of the Gram form.

## References

[^mcka]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), appendix "Advanced NumPy", broadcasting: the trailing-dimension compatibility rule, broadcasting over missing or length-1 dimensions, and `np.newaxis` to broadcast along an axis other than the last.
[^harris]: [[Harris 2020 - Array Programming with NumPy]], *Nature* 585:357-362, Fig. 1: broadcasting in the multiplication of two-dimensional arrays; index arrays are broadcast before the lookup.
