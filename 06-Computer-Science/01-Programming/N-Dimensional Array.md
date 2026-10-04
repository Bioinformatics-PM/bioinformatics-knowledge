---
aliases:
  - ndarray
  - NumPy Array
  - Multidimensional Array
  - Tableau multidimensionnel
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Array]]"
  - "[[Python Object Model]]"
  - "[[Scientific Python Ecosystem]]"
related:
  - "[[Array Indexing]]"
  - "[[Broadcasting]]"
  - "[[Vectorization]]"
  - "[[Array Memory Layout]]"
  - "[[Integer Representation]]"
  - "[[Floating-Point Arithmetic]]"
  - "[[Matrix]]"
  - "[[Count Matrix]]"
  - "[[FASTQ Format]]"
  - "[[Position Weight Matrix]]"
  - "[[Data Frame]]"
  - "[[Sparse Matrix]]"
projects:
  - "[[07-evolution-simulator]]"
sources:
  - "[[Harris 2020 - Array Programming with NumPy]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
---

# N-Dimensional Array

> [!abstract]
> A NumPy array is one block of memory holding values of a single type, plus a shape and strides that say how to walk through it in n dimensions: that design makes reductions along an axis one call, reshapes and transposes free, and slices views rather than copies.

## Definition

An **n-dimensional array** (`numpy.ndarray`) is a fixed-size, homogeneous grid of values indexed by $n$ integers. NumPy stores it as a contiguous or strided **data buffer** described by metadata: the **dtype** (type and size of each element), the **shape** (length of each dimension, or **axis**) and the **strides** (bytes to skip to move one step along each axis), in C (row-major) or Fortran (column-major) order.[^harris] Indexing a subarray returns a **view** that shares the buffer; NumPy can also select elements by a boolean condition or by other arrays.[^harris]

## Why it matters

- **The shapes of sequencing data.** Base qualities of equal-length reads form a reads × positions matrix ([[FASTQ Format]]); expression data a genes × samples [[Count Matrix]]; one-hot encoded sequences a reads × positions × 4 array; [[07-evolution-simulator]] keeps a population's state in arrays.
- **Memory is dtype × size.** A million 150-nt reads hold $1.5 \times 10^8$ qualities: 150 MB as `uint8`, 1.2 GB as `int64` (Deeper). Choosing the dtype is the first optimization.
- **Speed.** Whole-array operations run in compiled loops over the buffer, instead of Python loops over boxed numbers ([[Vectorization]], [[Array]], [[Python Object Model]]).[^mck4]
- **The common currency.** SciPy, pandas, Matplotlib and scikit-learn take and return arrays ([[Scientific Python Ecosystem]]).

## Core (L1)

All outputs in this note come from NumPy 2.4.6 on Python 3.11.

**Create and inspect.** `np.array` converts nested lists; `zeros`, `ones`, `full`, `empty` and `arange` allocate; `np.frombuffer` reinterprets bytes without copying.[^mck4]

```python
import numpy as np

counts = np.array([[10, 0, 25, 7],
                   [200, 150, 310, 95],
                   [3, 8, 0, 1]], dtype=np.int32)      # invented: 3 genes x 4 samples
print(counts.shape, counts.ndim, counts.dtype, counts.size, counts.itemsize, counts.nbytes, counts.strides)
print(np.zeros((2, 3)).dtype, np.arange(6).reshape(2, 3).tolist(), np.full(3, 255, dtype=np.uint8))
```

```text
(3, 4) 2 int32 12 4 48 (16, 4)
float64 [[0, 1, 2], [3, 4, 5]] [255 255 255]
```

![[ndarray-axes-strides.svg]]

**Reshape.** `reshape` rearranges the same elements into a new shape (one dimension may be `-1`, inferred); the total size must match:

```python
a = np.arange(12)
print(a.reshape(3, 4).strides, a.reshape(2, 3, 2).shape, a.reshape(3, -1).shape)
try:
    a.reshape(5, -1)
except ValueError as err:
    print("ValueError:", err)
```

```text
(32, 8) (2, 3, 2) (3, 4)
ValueError: cannot reshape array of size 12 into shape (5,newaxis)
```

**Choose the dtype.** Every element has the same fixed-size type:

| dtype | Range or precision | Typical use |
|---|---|---|
| `uint8` | 0 to 255 | Phred qualities, base codes, one-hot values |
| `int32` | up to 2 147 483 647 | counts per gene and sample, positions within one chromosome |
| `int64` | up to about $9.2 \times 10^{18}$ | totals, positions on a concatenated genome |
| `float32` / `float64` | about 7 / 16 significant digits | normalized expression, probabilities ([[Floating-Point Arithmetic]]) |
| `bool` | `True` / `False` | masks |

**Reduce along an axis.** `axis=k` aggregates over index $k$ and removes that axis from the result; `keepdims=True` keeps it with length 1:[^mck4]

```python
print(counts.sum(axis=0))      # library size per sample: collapses the gene axis
print(counts.sum(axis=1))      # total per gene: collapses the sample axis
print(counts.sum(axis=1, keepdims=True).shape, counts.max(), counts.mean(axis=0))
```

```text
[213 158 335 103]
[ 42 755  12]
(3, 1) 310 [ 71.          52.66666667 111.66666667  34.33333333]
```

**Views and copies.** A slice is a view: writing through it changes the original. Boolean or integer-array ("fancy") indexing and `astype` return copies.[^mck4][^harris] `np.shares_memory` tells which:

```python
work = counts.copy()
sample0 = work[:, 0]                 # basic slice: view
sample0[0] = 999
print(work[0, 0], np.shares_memory(sample0, work), sample0.base is work)
high = work[work > 100]              # boolean mask: copy
high[:] = 0
print(work.max(), np.shares_memory(high, work))
```

```text
999 True True
999 False
```

Call `.copy()` when you need an independent array, for example before modifying a slice that a caller still uses.

## Deeper (L2)

**Strides explain the views.** In the figure, element $(i, j)$ of the `int32` matrix starts at byte $16i + 4j$. `counts.T` builds a new header with swapped shape and strides over the same buffer; a reshape that needs a different element order cannot be expressed with strides and copies:

```python
t = work.T
print(t.shape, t.strides, np.shares_memory(t, work), t.flags["C_CONTIGUOUS"])
print(np.shares_memory(work.reshape(-1), work), np.shares_memory(t.reshape(-1), work))
```

```text
(4, 3) (4, 16) True False
True False
```

Traversal order then matters for speed: see [[Array Memory Layout]].

**Fixed-width integers wrap.** NumPy integers are not Python integers ([[Integer Representation]]):

```python
x = np.array([250, 5], dtype=np.uint8)
print(x + 10, (x + 10).dtype, x.astype(np.int16) + 10)
print(x.sum(), x.sum().dtype, x.mean().dtype)
```

```text
[ 4 15] uint8 [260  15]
255 uint64 float64
```

`250 + 10` silently becomes 4: the Python integer adopts the array's `uint8`. Reductions are safer (here `sum` accumulates in `uint64` and `mean` returns `float64`), but element-wise arithmetic is not: cast before you compute (`astype(np.int16)`). Integer arrays cannot hold `NaN`, so missing values need a float dtype or a separate mask.

**Memory budget.** For $10^6$ reads of 150 positions: $1.5 \times 10^8 \times 1$ byte = 150 MB in `uint8`, $\times 8$ = 1.2 GB in `int64` (computed in the same script). `np.array(list_of_ints)` defaults to `int64` here, so a careless conversion costs eight times the memory qualities need.

**Next steps.** Selecting with slices, masks and index arrays is [[Array Indexing]]; combining arrays of different shapes (dividing a genes × samples matrix by a per-sample vector) is [[Broadcasting]].

## Advanced (L3)

- **Sequences as 3-D arrays.** Mapping A, C, G, T to rows of an identity matrix turns a read into a positions × 4 array and a batch into reads × positions × 4. Scoring every window against a [[Position Weight Matrix]] becomes an element-wise product summed over two axes; `sliding_window_view` exposes all windows as a strided view, without copying (Exercise 6).
- **Beyond one array in RAM.** Single-cell matrices are mostly zeros and are stored in sparse formats ([[Sparse Matrix]]); arrays larger than memory are processed in chunks or memory-mapped ([[Out-of-Core Computation]]). Array protocols let distributed, GPU or sparse array libraries accept code written against NumPy's API.[^harris]
- **Labels live elsewhere.** An `ndarray` has no row or column names: keep gene IDs and sample names in parallel arrays or in a [[Data Frame]], and never sort one without the other.

## Mathematical representation

- An array of **shape** $(d_0, \dots, d_{n-1})$ is a map $A : I \to T$ from the index set $I = \prod_{k=0}^{n-1} \{0, \dots, d_k - 1\}$ to the values $T$ of its dtype. Its **size** is $|I| = \prod_k d_k$ and it occupies $|I| \cdot b$ bytes, where $b$ is the itemsize.
- **Address.** With strides $(s_0, \dots, s_{n-1})$ in bytes, element $(i_0, \dots, i_{n-1})$ starts at offset $\sum_k i_k s_k$ from the buffer start. For C order, $s_{n-1} = b$ and $s_k = s_{k+1}\, d_{k+1}$: shape $(3, 4)$ with $b = 4$ gives $(16, 4)$; shape $(4, 1000, 3)$ with $b = 8$ gives $(24000, 24, 8)$.
- **Transpose** permutes $(d_k)$ and $(s_k)$ together: a new view, no data moved. **Reshape** to $(d'_0, \dots)$ requires $\prod d'_k = \prod d_k$; it is a view when the elements are already in the required order (always true for a C-contiguous array reshaped in C order).
- **Reduction along axis $k$.** $(R_k A)(i_0, \dots, \widehat{i_k}, \dots, i_{n-1}) = \sum_{i_k = 0}^{d_k - 1} A(i_0, \dots, i_{n-1})$, of shape $(d_0, \dots, \widehat{d_k}, \dots, d_{n-1})$ (the hat marks the removed index). Summing over all axes in any order gives the same total (exactly for integers; floats may differ by rounding).

## Computational representation

From FASTQ quality strings to a quality matrix, without a Python loop over characters. Each quality character encodes $Q + 33$ in Sanger FASTQ:[^cock]

```python
reads = [b"IIIII?5+#", b"IIII?+55#", b"III5?+#+#"]           # invented, equal length
Q = np.frombuffer(b"".join(reads), dtype=np.uint8).reshape(len(reads), -1) - 33
print(Q.dtype, Q.shape)
print(Q)
print(Q.mean(axis=0).round(1))         # mean quality per position
print((Q < 20).sum(axis=1))            # low-quality bases per read
```

```text
uint8 (3, 9)
[[40 40 40 40 40 30 20 10  2]
 [40 40 40 40 30 10 20 20  2]
 [40 40 40 20 30 10  2 10  2]]
[40.  40.  40.  33.3 33.3 16.7 14.  13.3  2. ]
[2 2 4]
```

`np.frombuffer` views the bytes as `uint8` codes, `reshape` cuts them into rows (all reads must have the same length), and subtracting 33 stays in `uint8`, safe here because every code is at least 33. Axis 0 summarizes positions across reads (the per-position quality profile of [[Read Quality Control]]), axis 1 summarizes reads.

## Worked example

> [!example] Library sizes and a gene filter on a count matrix
> `counts` is the invented 3 genes × 4 samples `int32` matrix above.
> 1. **Library sizes**: `lib_size = counts.sum(axis=0)` → `[213 158 335 103]`, one per sample (the gene axis is collapsed).
> 2. **Gene totals**: `gene_total = counts.sum(axis=1)` → `[ 42 755  12]`.
> 3. **Filter**: `keep = gene_total >= 20` → `[ True  True False]`; `counts[keep]` has shape `(2, 4)` and is a **copy** (`np.shares_memory` → `False`), so editing it cannot corrupt `counts`.
> 4. **Proportions**: `counts[keep] / lib_size` divides each column by its sample's total (a preview of [[Broadcasting]]); the result is `float64`:
> ```text
> [[0.047 0.    0.075 0.068]
>  [0.939 0.949 0.925 0.922]]
> ```
> 5. **Check**: the column sums are `[0.986 0.949 1.    0.99 ]`, not 1, because the filtered gene's counts are gone: library sizes must be computed **before** filtering, or recomputed deliberately ([[Count Normalization]]).

## Common misconceptions

> [!warning] "`axis=0` means per row"
> `axis=0` is the axis that disappears: summing over rows gives one value **per column**. Read `sum(axis=k)` as "sum over index $k$".

> [!warning] "Slicing copies, as with lists"
> List and string slices copy ([[String]]); NumPy slices are views, and writing through them changes the original.[^mck4] Boolean and integer-array indexing, by contrast, copy.

> [!warning] "NumPy integers behave like Python integers"
> They have a fixed width and wrap around silently: `uint8` 250 + 10 is 4. Python integers never overflow.

> [!warning] "`reshape` always returns a view"
> Only when the elements are already in the needed order. `a.T.reshape(-1)` copies; check with `np.shares_memory` when it matters.

## Exercises

> [!question] Exercise 1 (L1)
> `counts` has shape `(20000, 12)` (genes × samples). Give the shapes of `counts.sum(axis=0)`, `counts.sum(axis=1)`, `counts.sum(axis=1, keepdims=True)` and `counts.T`, and say what each sum means.

> [!success]- Solution
> `(12,)`: one library size per sample; `(20000,)`: one total per gene; `(20000, 1)`: the same totals kept as a column, ready to divide each row; `(12, 20000)`: samples × genes, a view. (Checked with NumPy: `(12,) (20000,) (20000, 1) (12, 20000)`.)

> [!question] Exercise 2 (L1)
> Choose a dtype for: (a) Phred qualities; (b) read counts per gene and sample; (c) positions on a hypothetical concatenated genome of $3 \times 10^9$ bp; (d) allele frequencies for 10 million variants.

> [!success]- Solution
> (a) `uint8`: qualities fit in 0 to 255.[^cock] (b) `int32` per cell (up to about $2.1 \times 10^9$), `int64` for totals over many samples. (c) $3 \times 10^9 > 2^{31} - 1 = 2\,147\,483\,647$, so `int64` (or `uint32`, up to 4 294 967 295, if you never subtract). (d) `float32` halves the memory of `float64` (40 MB instead of 80 MB); keep `float64` if later computations need the precision.

> [!question] Exercise 3 (L2, Python)
> Simulate (invented data) a quality matrix of 1000 reads × 150 positions whose mean declines along the read, then compute the mean quality per position, the fraction of bases below Q20 per position, and the first position where the mean drops below 25.

> [!success]- Solution
> ```python
> rng = np.random.default_rng(3)
> Qs = np.clip(rng.normal(36, 3, size=(1000, 150)) - np.linspace(0, 14, 150), 2, 41).astype(np.uint8)
> mean_pos = Qs.mean(axis=0)
> frac_low = (Qs < 20).mean(axis=0)              # mean of a boolean = fraction of True
> print(Qs.dtype, Qs.shape, Qs.nbytes)
> print(mean_pos[[0, 74, 149]].round(1), frac_low[[0, 74, 149]].round(3))
> print(np.flatnonzero(mean_pos < 25)[:1], (mean_pos < 25).sum())
> ```
> ```text
> uint8 (1000, 150) 150000
> [35.5 28.6 21.5] [0.    0.001 0.266]
> [113] 37
> ```
> Both statistics reduce along axis 0 (over reads). The mean falls below 25 from position 113 (0-based) on, the last 37 positions: a trimming tool would cut there ([[Read Quality Control]]).

> [!question] Exercise 4 (L2)
> For `a = np.arange(12).reshape(3, 4)`, predict which expressions share memory with `a`: `a[1:3]`, `a[[1, 2]]`, `a[a > 5]`, `a.T`, `a.reshape(-1)`, `a.T.reshape(-1)`, `a.ravel()`, `a.astype(np.float64)`, `a[:, ::2]`.

> [!success]- Solution
> Views: `a[1:3]`, `a.T`, `a.reshape(-1)`, `a.ravel()`, `a[:, ::2]` (a slice with a step is still expressible with strides: column stride doubled). Copies: `a[[1, 2]]` and `a[a > 5]` (fancy and boolean indexing), `a.T.reshape(-1)` (order not expressible with strides), `a.astype(np.float64)` (new dtype). `np.shares_memory` confirms all nine.

> [!question] Exercise 5 (L3, Python)
> For a C-ordered `float64` array of shape `(4, 1000, 3)`, compute the strides and the byte offset of element `(2, 10, 1)`, then verify it through the flattened array.

> [!success]- Solution
> $s_2 = 8$, $s_1 = 3 \times 8 = 24$, $s_0 = 1000 \times 24 = 24\,000$; offset $= 2 \times 24\,000 + 10 \times 24 + 1 \times 8 = 48\,248$ bytes, i.e. flat index $48\,248 / 8 = 6031 = (2 \times 1000 + 10) \times 3 + 1$.
> ```python
> b = np.zeros((4, 1000, 3), dtype=np.float64)
> print(b.strides, 2 * b.strides[0] + 10 * b.strides[1] + 1 * b.strides[2])   # (24000, 24, 8) 48248
> b[2, 10, 1] = 7.0
> print(b.reshape(-1)[(2 * 1000 + 10) * 3 + 1])                               # 7.0
> ```

> [!question] Exercise 6 (L3, Python)
> One-hot encode the invented sequence `GGTTGACAATTGACTATCN` (`N` as all zeros), score every 6-nt window against an invented log-odds matrix favouring `TTGACA` with one array expression, and check against a Python loop.

> [!success]- Solution
> ```python
> from numpy.lib.stride_tricks import sliding_window_view
> lut = np.full(256, 4, dtype=np.uint8)                        # unknown letters -> row 4
> lut[np.frombuffer(b"ACGT", dtype=np.uint8)] = np.arange(4, dtype=np.uint8)
> seq = b"GGTTGACAATTGACTATCN"                                  # invented
> idx = lut[np.frombuffer(seq, dtype=np.uint8)]
> ONEHOT = np.vstack([np.eye(4, dtype=np.int8), np.zeros((1, 4), dtype=np.int8)])
> onehot = ONEHOT[idx]                                          # (19, 4)
> W = np.log2(np.array([                                        # invented 6 x 4 matrix (A, C, G, T)
>     [0.1, 0.1, 0.1, 0.7], [0.1, 0.1, 0.1, 0.7], [0.1, 0.1, 0.7, 0.1],
>     [0.7, 0.1, 0.1, 0.1], [0.1, 0.7, 0.1, 0.1], [0.7, 0.1, 0.1, 0.1]]) / 0.25)
> win = sliding_window_view(onehot, (6, 4))[:, 0]               # (14, 6, 4), a view
> scores = (win * W).sum(axis=(1, 2))
> loop = [sum(W[j, idx[i + j]] for j in range(6) if idx[i + j] < 4) for i in range(len(seq) - 5)]
> print(win.shape, np.shares_memory(win, onehot))
> print(scores.round(2))
> print(np.allclose(scores, loop), int(scores.argmax()), seq[scores.argmax():scores.argmax() + 6])
> ```
> ```text
> (14, 6, 4) True
> [-5.12 -5.12  8.91 -2.32 -5.12 -5.12 -7.93 -5.12 -5.12  6.11 -2.32 -7.93
>  -5.12 -0.99]
> True 2 b'TTGACA'
> ```
> The product of a `(14, 6, 4)` view with the `(6, 4)` matrix multiplies each window by the weights ([[Broadcasting]]); summing over axes 1 and 2 leaves one score per window. The best window, at 2, is the consensus `TTGACA` ($6 \log_2 2.8 \approx 8.91$); the window at 9, `TTGACT`, has one mismatch. `N` contributes 0, a choice to document.

## Mastery checklist

- [ ] 1 Recognized: I can state what shape, dtype, strides and axis mean, and create arrays with `array`, `zeros`, `arange` and `frombuffer`.
- [ ] 2 Understood: I can predict the shape of a reduction along any axis and whether an operation returns a view or a copy.
- [ ] 3 Practiced: I can build a quality matrix from FASTQ strings, choose dtypes and compute per-position and per-read statistics without loops.
- [ ] 4 Applied: [[07-evolution-simulator]] stores population state in arrays with deliberate dtypes, and I can state its memory footprint.
- [ ] 5 Explained: I can teach strides, why transposes are free and some reshapes copy, integer wrap-around, and the one-hot view of sequences.

## References

[^harris]: [[Harris 2020 - Array Programming with NumPy]], *Nature* 585:357-362: the array as data buffer with dtype, shape and strides; C and Fortran order; views on subarrays; indexing by conditions and by arrays; array protocols.
[^mck4]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 4 "NumPy Basics: Arrays and Vectorized Computation": creation functions, dtypes and `astype`, slices as views, fancy indexing as copies, reductions along an axis, reshaping and transposing.
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* 38(6):1767-1771: Sanger FASTQ qualities encoded as Phred + 33 in printable ASCII.
