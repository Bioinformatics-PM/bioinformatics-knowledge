---
aliases:
  - Bisection Search
  - Half-Interval Search
  - Binary Chop
  - Lower Bound Search
  - Recherche dichotomique
tags:
  - type/algorithm
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Loop Invariant]]"
  - "[[Big O Notation]]"
  - "[[Array]]"
  - "[[Logarithm]]"
related:
  - "[[Sorting]]"
  - "[[Suffix Array]]"
  - "[[Binary Search Tree]]"
  - "[[Hash Table]]"
  - "[[Genomic Interval Arithmetic]]"
  - "[[Root Finding]]"
  - "[[Divide and Conquer]]"
projects:
  - "[[05-sequence-search]]"
  - "[[09-genome-browser]]"
  - "[[bio-algorithms]]"
sources:
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Python Documentation]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[GA4GH hts-specs]]"
---

# Binary Search

> [!abstract]
> Binary search finds where a key belongs in a sorted array, or where a monotone yes/no condition switches from "no" to "yes", by halving the candidate range at every step: $\lfloor \log_2 n \rfloor + 1$ comparisons for $n$ items, which is optimal, provided the boundary invariant is stated and kept exactly.

## Problem

- **Input**: a sorted array $a[0..n)$ and a key $x$; more generally, a predicate $P$ on the integers $[\ell, h)$ that is **monotone**: false, ..., false, true, ..., true.
- **Output**: the **lower bound** of $x$, the first index $i$ with $a[i] \ge x$ ($n$ if none), which is also the leftmost position where $x$ could be inserted without breaking the order. In general: the first $i$ with $P(i)$ true, or $h$ if there is none.
- **Biological use**: locating a pattern among the sorted suffixes of a genome ([[Suffix Array]]), the index structure of pattern-matching and read-mapping methods;[^compeau] counting the variants or features of a sorted list that fall in a region ([[Genomic Interval Arithmetic]], [[09-genome-browser]]); looking up a k-mer in a sorted k-mer table ([[05-sequence-search]]); finding the smallest parameter (a k-mer length, a threshold) for which a monotone property starts to hold. Region queries on large files rely on the same precondition: the tabix and CSI index formats are defined for position-sorted files.[^hts]

## Intuition

Compare $x$ with the middle element. If the middle element is already $\ge x$, the answer is at the middle or to its left; otherwise it is strictly to the right. One comparison discards half of the candidates, so $n$ candidates shrink to one after about $\log_2 n$ comparisons: about 32 for the $3.055 \times 10^9$ positions of a human genome ([[Recursion]] uses the same count for the recursive version). Storing items in a sorted array is what makes this fast "find" possible.[^6006-l3]

The difficulty is not the idea but the boundaries: is `hi` included or excluded, does the update use `mid` or `mid + 1`, what is returned when $x$ is absent? Every correct version answers these questions with one invariant.

## Mathematical formulation

**Monotone predicate.** $P : \{\ell, \dots, h - 1\} \to \{\text{false}, \text{true}\}$ with $P(i) \Rightarrow P(i + 1)$. The goal is $i^* = \min \{ i : P(i) \} $ (or $h$). The array case is $P(i) = [a[i] \ge x]$, monotone because $a$ is sorted; $P(i) = [a[i] > x]$ gives the **upper bound**, and the occurrences of $x$ are exactly $a[\text{lower}..\text{upper})$.

**Invariant** (half-open convention, state $(lo, hi)$ with $\ell \le lo \le hi \le h$):

$$I:\quad P(i) = \text{false for all } i \in [\ell, lo), \qquad P(i) = \text{true for all } i \in [hi, h).$$

It holds initially ($lo = \ell$, $hi = h$, both ranges empty). With $mid = \lfloor (lo + hi)/2 \rfloor$, so that $lo \le mid < hi$: if $P(mid)$ is true, monotonicity makes $P$ true on $[mid, h)$, and $hi \leftarrow mid$ keeps $I$; otherwise $P$ is false on $[\ell, mid]$, and $lo \leftarrow mid + 1$ keeps $I$. At exit $lo = hi$, and $I$ says that $lo$ is the first true index ([[Loop Invariant]], where Exercise 4 proves the same loop).[^clrs2]

**Variant and exact cost.** Let $s = hi - lo$. A true answer leaves $mid - lo = \lfloor s/2 \rfloor$ candidates, a false one $hi - mid - 1 = \lceil s/2 \rceil - 1 \le \lfloor s/2 \rfloor$. So after $t$ iterations $s \le \lfloor n / 2^t \rfloor$ with $n = h - \ell$, and the loop stops (at $s = 0$) after at most

$$T(n) = \lfloor \log_2 n \rfloor + 1 \quad (n \ge 1)$$

evaluations of $P$, the number of bits of $n$; the bound is reached when $P$ is always true. In recurrence form, $T(s) \le T(\lfloor s/2 \rfloor) + 1$ with $T(0) = 0$.

**Lower bound.** In the comparison model, an algorithm is a decision tree whose internal nodes are two-outcome comparisons and whose leaves are answers.[^6006-l4] Searching $n$ sorted items has $n + 1$ possible answers ($0, \dots, n$), and a binary tree with $n + 1$ leaves has height at least $\lceil \log_2 (n + 1) \rceil$. For $n \ge 1$, $\lceil \log_2(n + 1) \rceil = \lfloor \log_2 n \rfloor + 1$ (Exercise 6): binary search is **exactly** optimal in the worst case, not only up to a constant.

## Algorithm

```text
FIRST-TRUE(P, lo, hi)          // P monotone on [lo, hi); returns min{i : P(i)} or hi
1  while lo < hi
2      // invariant: P false on [lo0, lo), P true on [hi, hi0)
3      mid = floor((lo + hi) / 2)       // lo <= mid < hi
4      if P(mid)
5          hi = mid                     // mid may be the answer: keep it
6      else
7          lo = mid + 1                 // mid is not the answer: drop it
8  return lo

LOWER-BOUND(a, x) = FIRST-TRUE(i ↦ a[i] >= x, 0, n)
UPPER-BOUND(a, x) = FIRST-TRUE(i ↦ a[i] >  x, 0, n)
```

![[binary-search-lower-bound-invariant.svg]]

The two update rules are not interchangeable with other choices of `mid`: `lo = mid` with the lower middle can leave the range unchanged and loop forever ([[Loop Invariant]], Exercise 4).

## Complexity

| | Time | Space |
|---|---|---|
| Binary search on a sorted array | $\lfloor \log_2 n \rfloor + 1$ comparisons worst case, $\Theta(\log n)$ | $O(1)$ (iterative) |
| Linear scan of an unsorted array | $\Theta(n)$ | $O(1)$ |
| Sort once, then $q$ queries | $\Theta(n \log n + q \log n)$ ([[Sorting]]) | $\Theta(n)$ |
| Hash table, exact membership | $O(1)$ expected, but no order, range or nearest-key queries[^6006-l4] | $\Theta(n)$ ([[Hash Table]]) |
| Balanced search tree (insertions interleaved with queries) | $O(\log n)$ per query and update | $\Theta(n)$ ([[Binary Search Tree]]) |

A comparison costs $O(1)$ only for fixed-size keys. Comparing a pattern of length $m$ with a suffix costs up to $m$ character comparisons, so finding a pattern among the $n$ sorted suffixes of a text costs $O(m \log n)$ ([[Suffix Array]]).

## Implementation

Python's `bisect` module implements the two bounds: the insertion point returned by `bisect_left` splits the list into elements $< x$ and elements $\ge x$, which is the invariant above, and `bisect_right` places $x$ after any equal entries.[^py-bisect] Writing the generic version once makes the invariant explicit and works for predicates that are not array lookups.

```python
import bisect
import math
import random

def first_true(pred, lo: int, hi: int) -> int:
    """Smallest i in [lo, hi) with pred(i) true, or hi if there is none.
    Precondition: pred is monotone on [lo, hi): False ... False True ... True."""
    while lo < hi:
        # invariant: pred is False on [lo0, lo) and True on [hi, hi0)
        mid = (lo + hi) // 2                      # lo <= mid < hi
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def lower_bound(a: list, x) -> int:
    """First index i with a[i] >= x (len(a) if none): the leftmost insertion point."""
    return first_true(lambda i: a[i] >= x, 0, len(a))

def upper_bound(a: list, x) -> int:
    """First index i with a[i] > x: the rightmost insertion point."""
    return first_true(lambda i: a[i] > x, 0, len(a))

def count_in_range(sorted_pos: list[int], start: int, end: int) -> int:
    """Number of positions p with start <= p < end (0-based, half-open as in BED)."""
    return lower_bound(sorted_pos, end) - lower_bound(sorted_pos, start)

# Test oracle: bisect and a linear scan, on random sorted lists with duplicates
random.seed(0)
for _ in range(2000):
    a = sorted(random.choices(range(30), k=random.randint(0, 25)))
    x = random.randint(-2, 32)
    assert lower_bound(a, x) == bisect.bisect_left(a, x) == sum(v < x for v in a)
    assert upper_bound(a, x) == bisect.bisect_right(a, x) == sum(v <= x for v in a)
print("agrees with bisect and with a linear scan on 2000 random cases")

def evaluations(n: int) -> int:
    """Predicate calls when pred is always True, the case that shrinks the range least."""
    calls = 0
    def pred(i):
        nonlocal calls
        calls += 1
        return True
    first_true(pred, 0, n)
    return calls

for n in (1, 2, 7, 8, 1000, 3_055_000_000):
    print(n, evaluations(n), math.floor(math.log2(n)) + 1, math.ceil(math.log2(n + 1)))
```

```text
agrees with bisect and with a linear scan on 2000 random cases
1 1 1 1
2 2 2 2
7 3 3 3
8 4 4 4
1000 10 10 10
3055000000 32 32 32
```

The predicate is never materialized: `first_true` probes 32 of the 3,055,000,000 indices. An exhaustive check over every key for $n = 1, \dots, 64$ confirms that no input needs more than $\lfloor \log_2 n \rfloor + 1$ evaluations. Python integers do not overflow, so `(lo + hi) // 2` is safe here; with 32-bit integers, `lo + hi` can exceed $2^{31} - 1$ for arrays of more than about $10^9$ elements (a genome), and `lo + (hi - lo) // 2` is the safe form.

## Worked example

> [!example] Lower bound and range count on sorted variant positions (invented)
> Positions (0-based) of variants on one chromosome: `a = [105, 230, 230, 512, 777, 801, 950, 1203]`. Find `lower_bound(a, 700)`.
> ```text
> lo=0 hi=8 mid=4 a[mid]=777 -> hi = mid
> lo=0 hi=4 mid=2 a[mid]=230 -> lo = mid + 1
> lo=3 hi=4 mid=3 a[mid]=512 -> lo = mid + 1
> lower_bound = 4
> ```
> 1. Three comparisons for $n = 8$: $\lfloor \log_2 8 \rfloor + 1 = 4$ is the worst case, this key needed one fewer.
> 2. At every line the invariant holds: `a[:lo]` $< 700 \le$ `a[hi:]` (the figure shows the state before the third step).
> 3. **Region count.** Variants in the half-open region $[200, 800)$: `lower_bound(a, 800) - lower_bound(a, 200)` $= 5 - 1 = 4$ (230, 230, 512, 777). Using `upper_bound` for the end would wrongly include a variant at exactly 800.
> 4. **Duplicates.** `lower_bound(a, 230) = 1`, `upper_bound(a, 230) = 3`: two variants at position 230, at indices $[1, 3)$.

## Limitations

> [!warning] The precondition is the algorithm
> Binary search on unsorted data, or with a predicate that is not monotone, raises no error: it returns a plausible wrong index. The sort order must be the one the comparison uses: chromosome names sorted as text put `chr10` before `chr2`, so a search that compares chromosomes in natural order fails on such a file ([[Sorting]], Exercise 4).

- **Keeping the array sorted costs.** Inserting into a sorted array shifts up to $n$ elements, $O(n)$ per insertion ([[Array]]); with frequent updates, use a balanced [[Binary Search Tree]] or rebuild in batches.
- **Exact membership only?** A [[Hash Table]] answers "is this k-mer present?" in expected $O(1)$; binary search earns its place when order matters: ranges, nearest neighbours, counts, prefixes.
- **Continuous problems.** Bisection on real numbers ([[Root Finding]]) halves an interval instead of an index range; it must stop on a tolerance or an iteration count, since floating-point intervals do not shrink to zero length.

## Variants and successors

- **Lower, upper bound and equal range**: the three questions answered by two calls (above). The last index with $a[i] \le x$ is `upper_bound - 1`.
- **Binary search on the answer**: any monotone property of an integer parameter, such as "all k-mers of length $k$ are distinct" (Exercise 5). The cost is $\lfloor \log_2(\text{range}) \rfloor + 1$ evaluations of the property, each possibly expensive.
- **Exponential (galloping) search**: probe $\ell, \ell + 1, \ell + 3, \ell + 7, \dots$ until the predicate becomes true, then binary-search the last gap. If the answer is at offset $i$, this costs $O(\log i)$ evaluations instead of $O(\log n)$, and it needs no upper bound on the range (Exercise 5).
- **Search in a [[Suffix Array]]**: two binary searches (lower and upper bound of the pattern among the sorted suffixes) give every occurrence of a pattern in $O(m \log n)$; the [[Longest Common Prefix Array]] and the [[FM-Index]] are the successors used at genome scale.[^compeau]
- **Dynamic and spatial versions**: a [[Binary Search Tree]] is binary search made updatable; an [[Interval Tree]] answers "which intervals overlap this position?" when features have lengths, not just positions.

## Exercises

> [!question] Exercise 1 (L1)
> For `a = [2, 3, 3, 3, 7, 9]`, compute by hand `lower_bound` and `upper_bound` for $x = 3$ and $x = 8$, and the number of occurrences of each.

> [!success]- Solution
> $x = 3$: lower bound 1 (one element $< 3$), upper bound 4 (four elements $\le 3$), so 3 occurrences at indices $[1, 4)$. $x = 8$: lower and upper bound both 5 (five elements $< 8$, none equal), 0 occurrences; 5 is where 8 would be inserted.

> [!question] Exercise 2 (L1)
> Variant positions are stored 0-based and sorted. Give the expressions that count the variants in a BED region $[s, e)$ (0-based, half-open) and in a 1-based closed region $[S, E]$ written as `chr:S-E` ([[Genomic Coordinate System]]).

> [!success]- Solution
> BED $[s, e)$: positions $p$ with $s \le p < e$, `lower_bound(a, e) - lower_bound(a, s)`. A 1-based closed region $[S, E]$ is the 0-based half-open region $[S - 1, E)$, so `lower_bound(a, E) - lower_bound(a, S - 1)`. The general rule: a half-open range on both sides needs two lower bounds; mixing a lower and an upper bound is right only when the end is inclusive.

> [!question] Exercise 3 (L2)
> This version returns 2 for `a = [2, 3, 5]`, `x = 9`, instead of 3. Which part of the invariant proof fails, and what is the fix?
> ```python
> def buggy(a, x):
>     lo, hi = 0, len(a) - 1
>     while lo < hi:
>         mid = (lo + hi) // 2
>         if a[mid] < x:
>             lo = mid + 1
>         else:
>             hi = mid
>     return lo
> ```

> [!success]- Solution
> The loop body is the correct half-open loop; the initialization is not. With `hi = n - 1`, the invariant "every element of `a[hi:]` is $\ge x$" requires $a[n - 1] \ge x$, false when $x$ exceeds every element. **Initialization** fails, so the answer $n$ can never be returned. Fix: `hi = len(a)`. (On an empty list the buggy code returns 0 only by accident: `hi = -1` and the loop never runs.) Bugs in binary search are almost always a mismatch between the convention of `hi` (included or excluded) and its initial value or update.

> [!question] Exercise 4 (L2)
> A sorted list of features uses natural chromosome order (`chr1`, `chr2`, ..., `chr10`), and a function binary-searches it comparing chromosome names as strings. Give an input where it fails, and two ways to fix it.

> [!success]- Solution
> As strings, `"chr10" < "chr2"` (character `1` < `2`). In the list `[("chr2", 100), ("chr10", 50)]`, sorted in natural order, the predicate "item $\ge$ (`chr10`, 0)" evaluated with string comparison is already true at index 0, so `bisect_left` returns 0 and the search for `chr10` lands on a `chr2` feature. Fix (a): compare with the same key the list was sorted by, for instance `(int(name[3:]), pos)` for numbered chromosomes. Fix (b): re-sort with the key the search uses. The rule: the search and the sort must share one total order ([[Sorting]]).

> [!question] Exercise 5 (L3, Python)
> Let $u(s)$ be the smallest $k$ such that all k-mers of $s$ are distinct. Prove that "all k-mers are distinct" is monotone in $k$, find $u(s)$ by binary search over $[1, n]$ and by galloping search, and compare the number and size of the probes on a simulated 10,000-base sequence. Why is plain binary search a poor choice here?

> [!success]- Solution
> **Monotone**: if two $(k+1)$-mers are equal, their first $k$ letters are two equal k-mers at different positions. So "distinct at $k$" implies "distinct at $k + 1$", and `first_true` applies.
> ```python
> import random
>
> def all_kmers_distinct(seq: str, k: int) -> bool:
>     n_windows = len(seq) - k + 1
>     return len({seq[i:i + k] for i in range(n_windows)}) == n_windows
>
> def galloping_first_true(pred, lo: int, hi: int) -> int:
>     """Probe lo, lo+1, lo+3, lo+7, ... until pred is true, then binary search the last gap."""
>     step, prev, probe = 1, lo - 1, lo
>     while probe < hi and not pred(probe):
>         prev, probe = probe, probe + step
>         step *= 2
>     return first_true(pred, prev + 1, min(probe, hi))
>
> def min_unique_k(seq: str, search) -> tuple[int, int, int]:
>     probes = []
>     def pred(k):
>         probes.append(k)
>         return all_kmers_distinct(seq, k)
>     return search(pred, 1, len(seq) + 1), len(probes), max(probes)
>
> random.seed(4)
> seq = "".join(random.choices("ACGT", k=10_000))   # simulated: uniform i.i.d. bases
> print("binary   ", min_unique_k(seq, first_true))
> print("galloping", min_unique_k(seq, galloping_first_true))
> rep = "ACGTACGTTT" + "GATTACA" * 3 + "CCC"        # invented, with a tandem repeat
> print(min_unique_k(rep, galloping_first_true)[0], len(rep))
> ```
> Output:
> ```text
> binary    (13, 13, 5001)
> galloping (13, 8, 16)
> 15 34
> ```
> Both find $u = 13$. The answer is small: the expected number of equal pairs among $\binom{n}{2} \approx n^2/2$ windows is about $n^2 / (2 \cdot 4^k)$, close to 1 for $k \approx 2 \log_4 n \approx 13$. Plain binary search starts in the middle of $[1, n]$: its first probe, $k = 5001$, builds 5,000 strings of 5,001 letters (about 25 MB), and on a bacterial genome the same probe would not fit in memory. Galloping probes $k = 1, 2, 4, 8, 16$ and then searches $[9, 16)$, never building k-mers longer than 16. When the cost of a probe grows with the probed value, search from the cheap end. The repetitive sequence needs $k = 15$ because `GATTACAGATTACA` (14 letters) occurs twice: repeats, not length, set $u$.

> [!question] Exercise 6 (L3)
> Prove that $\lceil \log_2(n + 1) \rceil = \lfloor \log_2 n \rfloor + 1$ for every integer $n \ge 1$, and conclude that no comparison-based algorithm searches $n$ sorted items with fewer worst-case comparisons than binary search.

> [!success]- Solution
> Let $b = \lfloor \log_2 n \rfloor$, so $2^b \le n < 2^{b+1}$, and then $2^b < n + 1 \le 2^{b+1}$, which gives $\lceil \log_2(n+1) \rceil = b + 1$. A comparison-based search is a binary decision tree with at least $n + 1$ leaves (one per possible insertion point, each reachable by some input), so its height, the worst-case number of comparisons, is at least $\lceil \log_2(n+1) \rceil$.[^6006-l4] Binary search uses at most $\lfloor \log_2 n \rfloor + 1$ (Mathematical formulation), the same number. Faster lookups must leave the comparison model: hashing reads the key's bits directly ([[Hash Table]]).

## Mastery checklist

- [ ] 1 Recognized: I can state the lower-bound problem and the precondition (sorted array or monotone predicate).
- [ ] 2 Understood: I can prove the half-open loop correct with its invariant and variant, and derive $\lfloor \log_2 n \rfloor + 1$.
- [ ] 3 Practiced: I can write `first_true`, lower and upper bound from memory, and test them against `bisect` and a linear scan on random inputs.
- [ ] 4 Applied: I answer region queries on sorted positions in [[09-genome-browser]] and look up k-mers or suffixes in a sorted index in [[05-sequence-search]].
- [ ] 5 Explained: I can teach why binary search is exactly optimal in the comparison model, when galloping search is better, and how sort order and coordinate conventions break it.

## References

[^6006-l3]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 3 "Sets and Sorting" (a set stored as a sorted array supports find by binary search in $O(\log n)$).
[^6006-l4]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 4 "Hashing": comparison-model lower bound (decision trees), direct access arrays and hash tables, set operations a hash table does not support efficiently.
[^clrs2]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 2 "Getting Started" (loop invariants: initialization, maintenance and termination).
[^py-bisect]: [[Python Documentation]], Library Reference, `bisect` module: the insertion point returned by `bisect_left` partitions the list into elements $< x$ and elements $\ge x$; `bisect_right` returns the insertion point after existing entries equal to $x$.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?" (suffix arrays for pattern matching, read mapping).
[^hts]: [[GA4GH hts-specs]], `tabix.tex` and `CSIv1.tex`: index formats for position-sorted files.
