---
aliases:
  - Static Array
  - Dynamic Array
  - Resizable Array
  - Tableau
  - Tableau dynamique
tags:
  - type/concept
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Abstract Data Type]]"
  - "[[Big O Notation]]"
  - "[[Model of Computation]]"
  - "[[Python Object Model]]"
related:
  - "[[Linked List]]"
  - "[[Amortized Analysis]]"
  - "[[N-Dimensional Array]]"
  - "[[Array Memory Layout]]"
  - "[[Memory Hierarchy]]"
  - "[[Suffix Array]]"
  - "[[Sequencing Coverage]]"
projects: []
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Array

> [!abstract]
> An array stores elements of equal size side by side in one block of memory, so any element is reached in one step from its index; a dynamic array, like Python's `list`, keeps spare room at the end and grows by a constant factor, which makes appending cost $O(1)$ on average.

## Definition

An **array** stores a fixed number of elements of equal size in one contiguous block of memory. If the block starts at address $a$, each element occupies $b$ bytes and the first index is $s$, element $i$ starts at address $a + b(i - s)$, so reading or writing it takes constant time.[^clrs10][^6006-l2] A **dynamic array** stores a sequence in an array with spare capacity and, when that array is full, moves to a new one a constant factor larger; any sequence of $n$ appends then costs $O(n)$, that is $O(1)$ amortized per append. Python's `list` is a dynamic array.[^6006-l2][^clrs16]

## Why it matters

- **Position-indexed data.** Per-base depth, quality or conservation along a chromosome is an array indexed by the 0-based coordinate: the value at any locus is one address computation away ([[Genomic Coordinate System]], [[Sequencing Coverage]]).
- **Counting by direct addressing.** For small $k$, k-mers numbered in base 4 index a frequency array of $4^k$ counters ([[K-mer]]).[^compeau]
- **Genome indexes are integer arrays.** A suffix array is the array of starting positions of the suffixes of a text in sorted order ([[Suffix Array]]).[^compeau]
- **Memory and speed.** A `list` of numbers holds references to separate objects; NumPy stores the values in one contiguous block, uses much less memory and runs its C loops without per-element type checks ([[N-Dimensional Array]]).[^mck4] Measured below: 32.4 versus 8.0 bytes per float.

## Core (L1)

![[dynamic-array-memory-layout.svg]]

- **Contiguity gives $O(1)$ access.** The address of element $i$ is a multiply-add, whatever $n$ (panel A). This is the "random access" of the word-RAM model ([[Model of Computation]]).
- **Contiguity makes the middle expensive.** Inserting or deleting at position $i$ shifts the $n - i$ elements after it: $O(n)$ at the front, $O(1)$ at the end.
- **Static versus dynamic.** A static array's length is fixed at allocation. A dynamic array separates its **length** $n$ from its **capacity** (allocated slots); appending fills a spare slot, and only a full array triggers reallocation and copying (panel B).[^6006-l2]
- **Arrays in Python.** `list` (dynamic array of references), `array.array` (dynamic array of packed machine values: `'d'` doubles, `'i'` ints, `'B'` bytes), `bytes`/`bytearray` ([[String]]), NumPy `ndarray` (fixed-size, n-dimensional).

| `list` operation | Cost | Reason |
|---|---|---|
| `xs[i]`, `xs[i] = v` | $O(1)$ | address arithmetic |
| `xs.append(v)`, `xs.pop()` | $O(1)$ amortized | spare capacity at the end |
| `xs.insert(0, v)`, `xs.pop(0)` | $O(n)$ | every later reference shifts[^mck3] |
| `v in xs` | $O(n)$ | linear scan[^mck3] |
| `xs[i:j]` | $O(j - i)$ | the slice is a new list of $j - i$ references |

Front insertion is quadratic over a loop: doubling $n$ quadruples the time (`timeit`, best of 5, CPython 3.11; indicative):

```python
import timeit
def build_append(n):
    xs = []
    for i in range(n):
        xs.append(i)
def build_front(n):
    xs = []
    for i in range(n):
        xs.insert(0, i)
for n in (10_000, 20_000, 40_000):
    ta = min(timeit.repeat(lambda: build_append(n), number=1, repeat=5))
    tf = min(timeit.repeat(lambda: build_front(n), number=1, repeat=5))
    print(n, f"append {ta * 1e3:.2f} ms", f"insert(0) {tf * 1e3:.1f} ms")
```

```text
10000 append 0.17 ms insert(0) 16.4 ms
20000 append 0.36 ms insert(0) 63.4 ms
40000 append 1.68 ms insert(0) 250.1 ms
```

## Deeper (L2)

**Why appends are $O(1)$ amortized: aggregate method.** Start from capacity 1 and double when full. Over $n$ appends, copies happen when the length reaches $1, 2, 4, \dots, 2^{j}$ with $2^j < n$, so they total $2^{j+1} - 1 < 2n$; adding the $n$ writes, the whole sequence costs less than $3n$.[^clrs16] The code below counts it.

**Potential method.** Start from an empty table of capacity 0 and let $\Phi = 2\,\mathrm{num} - \mathrm{cap}$, which is $0$ initially and never negative, since the table is always at least half full after the first append. The amortized cost is $\hat{c} = c + \Delta\Phi$.
- Append with spare room: $c = 1$, $\Delta\Phi = 2$, so $\hat{c} = 3$.
- Append into a full table with $\mathrm{num} = \mathrm{cap} = m \ge 1$: copy $m$ and write 1, $c = m + 1$; afterwards $\Phi = 2(m + 1) - 2m = 2$, before $\Phi = m$, so $\hat{c} = m + 1 + 2 - m = 3$.

The very first append allocates one slot: $c = 1$, $\Delta\Phi = 1$, $\hat{c} = 2$. Every append thus has amortized cost at most 3, and since $\Phi_n \ge \Phi_0$, the actual total is at most $3n$ ([[Amortized Analysis]]).

**The growth factor is a trade-off.** Growing by a factor $g > 1$ copies at most $n(1 + 1/g + 1/g^2 + \dots) = n\,\frac{g}{g-1}$ elements, for a total cost of at most $n\left(1 + \frac{g}{g-1}\right)$: $3n$ for $g = 2$, $4n$ for $g = 1.5$, $10n$ for $g = 1.125$. Right after a resize, a fraction up to $1 - 1/g$ of the capacity is empty: 50% for $g = 2$, 11% for $g = 1.125$. Growing by a fixed amount $c$ instead copies $c + 2c + \dots \approx n^2 / (2c)$ elements: $\Theta(n)$ per append.

**What CPython does (observed, not a documented guarantee).** Tracking `sys.getsizeof` while appending shows reallocations at lengths 1, 5, 9, 17, 25, 33, 41, 53, 65, 77, ..., and successive allocation sizes in ratio 1.125 for large lists: a modest growth factor, trading more copies for less slack (code below).

**Shrinking without thrashing.** Halving the capacity as soon as the table is half empty fails: at the boundary, alternating append and pop resizes on every operation, $\Theta(n)$ each. Halving only when the table falls to a quarter full leaves a half-full table after each resize, so $\Theta(n)$ cheap operations separate two resizes and every mix of appends and pops stays $O(1)$ amortized.[^clrs16][^6006-l2]

## Advanced (L3)

- **References versus values** (panel C). A `list` stores 8-byte references to objects allocated elsewhere; each `float` object takes 24 bytes. A typed array (`array('d')`, NumPy `float64`) stores 8-byte values inline: about 4 times less memory, and a loop over the values reads consecutive addresses ([[Python Object Model]], [[Memory Hierarchy]]).[^mck4]
- **Two dimensions.** A $R \times C$ matrix stored row by row (row-major) puts element $(i, j)$ at $a + b(iC + j)$.[^clrs10] Scanning a dynamic programming matrix along rows touches consecutive addresses; scanning along columns jumps $bC$ bytes each step ([[Array Memory Layout]], [[Dynamic Programming]]).
- **Genome scale.** The T2T-CHM13 human genome has about $3.055 \times 10^9$ bp.[^nurk] A per-base depth array costs 6.11 GB as 2-byte integers, 12.22 GB as 4-byte integers, and 24.44 GB for the references alone in a Python `list`. Hence per-chromosome arrays, run-length intervals for sparse signals, or memory-mapped files ([[Virtual Memory]]).
- **Index width.** Positions below $2^{32} \approx 4.29 \times 10^9$ fit in 4 bytes, enough for one copy of the human genome (a 12.2 GB suffix array) but not for both strands ($6.11 \times 10^9$ positions), which need 5- or 8-byte entries ([[Suffix Array]]).

## Mathematical representation

- **Addressing**: $\mathrm{addr}(i) = a + b(i - s)$ for $s \le i < s + n$; row-major matrix: $\mathrm{addr}(i, j) = a + b(iC + j)$ with 0-based $i, j$.
- **Amortized cost**: $\hat{c}_t = c_t + \Phi(D_t) - \Phi(D_{t-1})$, so $\sum_t c_t = \sum_t \hat{c}_t - \Phi(D_n) + \Phi(D_0) \le \sum_t \hat{c}_t$ when $\Phi(D_n) \ge \Phi(D_0)$.
- **Doubling**: $\Phi = 2\,\mathrm{num} - \mathrm{cap}$ gives $\hat{c}_t \le 3$, hence $\sum_t c_t \le 3n$. **Growth factor $g$**: copies $\le n\,g/(g-1)$; slack after a resize $\le 1 - 1/g$ of the capacity.

## Computational representation

A dynamic array that counts its copies, then an observation of CPython's `list`, then the memory cost of references:

```python
import sys
from array import array
class DynamicArray:
    """Append-only dynamic array that doubles its capacity; counts element copies."""
    def __init__(self):
        self.n, self.cap, self.data, self.copies = 0, 1, [None], 0

    def append(self, x):
        if self.n == self.cap:                  # full: allocate twice the space and copy
            new = [None] * (2 * self.cap)
            for i in range(self.n):
                new[i] = self.data[i]
            self.copies += self.n
            self.data, self.cap = new, 2 * self.cap
        self.data[self.n] = x
        self.n += 1
for n in (10, 1000, 10**6):
    d = DynamicArray()
    for i in range(n):
        d.append(i)
    print(n, d.cap, d.copies, round((n + d.copies) / n, 3))   # writes + copies per append
lst, last, grew_at, sizes = [], sys.getsizeof([]), [], []
for i in range(1, 1_000_001):                   # CPython list: when does its allocation change?
    lst.append(i)
    s = sys.getsizeof(lst)
    if s != last:
        grew_at.append(i)
        sizes.append(s - sys.getsizeof([]))
        last = s
print(grew_at[:10])
print([round(sizes[j + 1] / sizes[j], 3) for j in range(len(sizes) - 4, len(sizes) - 1)])
floats = [float(i) for i in range(10**6)]       # references to float objects
packed = array("d", floats)                     # packed 8-byte values
list_bytes = sys.getsizeof(floats) + sum(sys.getsizeof(x) for x in floats)
print(sys.getsizeof(1.0), round(list_bytes / 10**6, 1), round(sys.getsizeof(packed) / 10**6, 1))
```

```text
10 16 15 2.5
1000 1024 1023 2.023
1000000 1048576 1048575 2.049
[1, 5, 9, 17, 25, 33, 41, 53, 65, 77]
[1.125, 1.125, 1.125]
24 32.4 8.0
```

The cost per append stays below 3, as proved. The `list` measurement counts each float object once; small integers and shared objects would change it.

## Worked example

> [!example] Per-base coverage with a difference array (toy alignments, invented)
> Reads aligned to a 10-bp reference, 0-based half-open intervals: $[0, 5)$, $[2, 8)$, $[3, 6)$, $[7, 10)$.
> 1. **Naive**: add 1 to every covered position, $O(\sum \text{read lengths})$; long reads at high depth make this slow.
> 2. **Difference array** $D$ of length 11: for each read, $D[\text{start}] \mathrel{+}= 1$ and $D[\text{end}] \mathrel{-}= 1$, $O(1)$ per read.
> 3. **Prefix sums**: depth at $p$ is $D[0] + \dots + D[p]$, one pass, $O(L)$. Total $O(L + r)$ for $r$ reads.
> ```python
> from array import array
> from itertools import accumulate
> def coverage(length: int, reads: list[tuple[int, int]]) -> array:
>     """Per-base depth from 0-based half-open [start, end) intervals, O(length + len(reads))."""
>     diff = array("i", [0]) * (length + 1)
>     for start, end in reads:
>         diff[start] += 1
>         diff[end] -= 1
>     return array("i", accumulate(diff[:-1]))
>
> print(list(coverage(10, [(0, 5), (2, 8), (3, 6), (7, 10)])))
> # [1, 1, 2, 3, 3, 2, 1, 2, 1, 1]
> ```
> 4. **Check by hand** at position 4: reads $[0,5)$, $[2,8)$, $[3,6)$ cover it, depth 3. Half-open ends make $D[\text{end}]$ exactly the first uncovered position ([[Genomic Coordinate System]]).

## Common misconceptions

> [!warning] "`list.append` is O(1)"
> Only amortized: the append that finds the array full copies all $n$ references. Over many appends the average is constant; a single call is not.

> [!warning] "A list of numbers is a numeric array"
> It is an array of references to number objects: about 4 times the memory of `array('d')` or NumPy for floats (measured above), and each access goes through an object.

## Exercises

> [!question] Exercise 1 (L1)
> An array of 8-byte elements starts at address `0x1000` (index 0). Where is element 37? Where is element $(3, 7)$ of a $100 \times 100$ row-major matrix of doubles starting at the same address?

> [!success]- Solution
> $\mathtt{0x1000} + 8 \times 37 = 4096 + 296 = 4392 = \mathtt{0x1128}$. Matrix: $4096 + 8(3 \times 100 + 7) = 4096 + 2456 = 6552 = \mathtt{0x1998}$. Python agrees: `hex(0x1000 + 8 * 37)`, `hex(0x1000 + 8 * 307)`.

> [!question] Exercise 2 (L1)
> A script drains a `list` of $n$ reads with `reads.pop(0)`. How many reference moves does it perform in total, and what should it use instead?

> [!success]- Solution
> Removing the first of $m$ elements shifts $m - 1$ references, so the total is $\sum_{m=1}^{n} (m - 1) = n(n-1)/2$, about $5 \times 10^{11}$ for $n = 10^6$. Use `collections.deque.popleft()`, $O(1)$ ([[Queue]]), or iterate over the list without removing.

> [!question] Exercise 3 (L2)
> Prove with the aggregate method that $n$ appends to a dynamic array growing by factor $g = 1.5$ cost at most $4n$ element writes and copies. What fraction of the capacity can be empty right after a resize?

> [!success]- Solution
> Resizes happen at capacities $c_0 g^j < n$; the last one copies fewer than $n$ elements, the previous ones $1/g$, $1/g^2$, ... of that. Total copies $< n \sum_{j \ge 0} g^{-j} = n\,\frac{g}{g-1} = 3n$; with the $n$ writes, $< 4n$. Right after a resize from $c$ to $1.5c$ with $c + 1$ elements, the empty fraction is about $1 - 1/1.5 = 1/3$.

> [!question] Exercise 4 (L2, Python)
> Add `pop` with shrinking to `DynamicArray`: halve the capacity when the load factor $n/\mathrm{cap}$ falls to a threshold. Fill 1,024 elements, then alternate `append` and `pop` 1,000 times; count copies for thresholds $1/2$ and $1/4$.

> [!success]- Solution
> ```python
> class ShrinkingArray(DynamicArray):
>     def __init__(self, threshold):
>         super().__init__()
>         self.threshold = threshold
>     def pop(self):
>         self.n -= 1
>         x, self.data[self.n] = self.data[self.n], None
>         if self.cap > 1 and self.n <= self.threshold * self.cap:
>             self.cap //= 2
>             self.data = self.data[:self.cap]      # copies the n live elements
>             self.copies += self.n
>         return x
> for threshold in (1 / 2, 1 / 4):
>     a = ShrinkingArray(threshold)
>     for i in range(1024):                      # now full: n = cap = 1024
>         a.append(i)
>     before = a.copies
>     for _ in range(1000):
>         a.append(0)
>         a.pop()
>     print(threshold, a.copies - before)
> # 0.5 2048000
> # 0.25 1024
> ```
> With $1/2$, each append doubles and each pop halves: 1,024 copies per operation. With $1/4$, the first append doubles to 2,048 slots and the table then oscillates between 1,024 and 1,025 elements without resizing.

> [!question] Exercise 5 (L3)
> Plan memory for the T2T-CHM13 genome ($3.055 \times 10^9$ bp): a per-base depth array with 2- and 4-byte counters, and a suffix array over one strand and over both strands. Which integer width does each index need?

> [!success]- Solution
> Depth: $3.055 \times 10^9 \times 2$ B $= 6.11$ GB (`uint16`, saturating above 65,535) or 12.22 GB (`uint32`); a Python `list` would need 24.44 GB of references before counting any object. Suffix array, one strand: $3.055 \times 10^9 < 2^{32}$, so 4-byte entries suffice, 12.2 GB. Both strands: $6.11 \times 10^9 > 2^{32}$, so entries need at least 33 bits, in practice 5 or 8 bytes (30.6 or 48.9 GB).

## Mastery checklist

- [ ] 1 Recognized: I can say why array access is $O(1)$ and why front insertion is $O(n)$.
- [ ] 2 Understood: I can explain capacity versus length and why multiplicative growth gives amortized $O(1)$ appends.
- [ ] 3 Practiced: I can prove the amortized bound with the aggregate and potential methods and implement a dynamic array with safe shrinking.
- [ ] 4 Applied: I stored a per-position genomic signal (coverage, quality) in a typed array and measured its memory against a `list`.
- [ ] 5 Explained: I can teach growth-factor trade-offs, references versus values, and genome-scale memory planning.

## References

[^clrs10]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 10 "Elementary Data Structures": array-based structures, address computation, matrices.
[^clrs16]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 16 "Amortized Analysis": aggregate, accounting and potential methods, dynamic tables.
[^6006-l2]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 2 "Data Structures": static arrays in the word-RAM, dynamic arrays (Python `list`), amortized resizing.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": cost of `insert` versus `append`, linear membership tests on lists.
[^mck4]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 4 "NumPy Basics: Arrays and Vectorized Computation": contiguous storage and memory use of NumPy arrays.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], 3rd ed.: chapters "Where in the Genome Does DNA Replication Begin?" (frequency array of k-mers numbered in base 4) and "How Do We Locate Disease-Causing Mutations?" (suffix arrays).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*: 3.055 Gbp T2T-CHM13 assembly.
