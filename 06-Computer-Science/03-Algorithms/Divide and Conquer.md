---
aliases:
  - Divide-and-Conquer
  - D&C
  - Karatsuba Multiplication
  - Closest Pair of Points
  - Median of Medians
  - Linear-Time Selection
  - Diviser pour régner
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Recursion]]"
  - "[[Sorting]]"
  - "[[Big O Notation]]"
  - "[[Mathematical Induction]]"
  - "[[Recurrence Relation]]"
related:
  - "[[Master Theorem]]"
  - "[[Randomized Algorithm]]"
  - "[[Radix Sort]]"
  - "[[Dynamic Programming]]"
  - "[[Binary Search]]"
  - "[[Fast Fourier Transform]]"
  - "[[Hirschberg Algorithm]]"
  - "[[Suffix Array Construction]]"
  - "[[External Memory Algorithm]]"
  - "[[Quantile]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.046J - Design and Analysis of Algorithms]]"
  - "[[Coursera Stanford - Algorithms Specialization]]"
  - "[[Karatsuba 1962 - Multiplication of Multidigit Numbers on Automata]]"
  - "[[Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
---

# Divide and Conquer

> [!abstract]
> Divide and conquer solves a problem by splitting it into smaller instances of itself, solving those recursively and combining their answers; the design work is to split and combine so that the cost recurrence beats the obvious algorithm, as Karatsuba multiplication, the closest-pair algorithm and linear-time selection do.

## Definition

A **divide-and-conquer** algorithm solves an instance in three steps:[^clrs4]

1. **Divide** it into subproblems of the same kind, each smaller than the instance;
2. **Conquer** the subproblems recursively, or directly once they are small enough (base cases);
3. **Combine** the sub-solutions into a solution of the instance.

Correctness follows by strong induction on the size ([[Recursion]], [[Mathematical Induction]]); the running time satisfies a [[Recurrence Relation]] that the [[Master Theorem]] solves in the common equal-split case.

## Why it matters

- **Sorting genomic records.** Merge sort's combine step, merging sorted lists, keeps its worst case at $\Theta(n \log n)$ ([[Sorting]]); merging sorted runs is also how data larger than memory gets sorted ([[External Memory Algorithm]]).
- **Alignment in linear space.** Hirschberg's method splits an alignment at the middle row of the dynamic-programming grid and recurses on the two halves, recovering an optimal alignment with linear memory[^jones] (Advanced, [[Hirschberg Algorithm]], [[04-alignment-engine]]).
- **Suffix arrays in linear time.** The skew algorithm sorts the suffixes starting at positions $i \bmod 3 \neq 0$ recursively, sorts the remaining third with that information, then merges[^karkkainen] ([[Suffix Array Construction]]).
- **Order statistics without sorting.** Median coverage, or the N50 of an assembly (a length-weighted median of contig lengths[^lander]), is a selection problem: linear time, no sort needed (Exercise 4, [[Quantile]]).

## Core (L2)

### The template: merge sort

[[Sorting|Merge sort]] is the reference instance:[^clrs2] divide in $O(1)$ at the middle index, conquer both halves, combine by a $\Theta(n)$ merge, so $T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)$ ([[Recursion#Worked example]]). Two lessons carry over to every design:

- **Each design puts its linear pass somewhere.** Merge sort works in the combine step; quicksort works in the divide step (partitioning) and has nothing to combine.
- **The combine step can compute more than the output.** Counting inversions while merging measures the disorder between two gene orders in $O(n \log n)$ instead of $O(n^2)$ ([[Sorting#Exercises]], Exercise 2).

### Karatsuba multiplication

The schoolbook product of two $n$-digit numbers costs $\Theta(n^2)$ digit products. Split each factor at $m = \lfloor n/2 \rfloor$ digits, $x = a\,10^m + b$ and $y = c\,10^m + d$:

$$xy = ac\,10^{2m} + (ad + bc)\,10^{m} + bd.$$

Four half-size products give $T(n) = 4T(n/2) + \Theta(n) = \Theta(n^2)$: no gain. Karatsuba and Ofman obtained the middle coefficient from **one** extra product,[^karatsuba][^stanford]

$$ad + bc = (a + b)(c + d) - ac - bd,$$

so three half-size products plus $\Theta(n)$ additions and shifts suffice: $T(n) = 3T(n/2) + \Theta(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$ (case 1 of the [[Master Theorem]]). Saving one subproblem out of four changes the exponent, not just the constant.

### Closest pair of points

Given $n$ distinct points in the plane, find the two closest. All pairs cost $\Theta(n^2)$; divide and conquer reaches $O(n \log n)$:[^stanford]

1. **Divide.** Sort by $x$ once (and by $y$ once); split at the median $x$-coordinate, the line $\ell$, into halves $P_L$ and $P_R$.
2. **Conquer.** Recursively find the closest distances $\delta_L$ and $\delta_R$; let $\delta = \min(\delta_L, \delta_R)$.
3. **Combine.** A closer pair must have one point on each side and both points in the strip $|x - \ell| < \delta$. Scan the strip in $y$ order and compare each point $p$ with the next 7 strip points only.

![[closest-pair-strip.svg]]

**Why 7 successors suffice.** A strip point $q$ above $p$ with $q_y - p_y < \delta$ lies in the $\delta \times 2\delta$ box above $p$. Each $\delta \times \delta$ half of the box holds at most 4 points of its own side (Exercise 2), so the box holds at most 8 points, $p$ included, and every candidate is among the 7 strip points that follow $p$ in $y$ order. Splitting the $y$-sorted list in linear time, instead of re-sorting it in every call, makes the combine step $O(n)$: $T(n) = 2T(n/2) + O(n) = O(n \log n)$.

### Linear-time selection

Selection asks for the $k$-th smallest of $n$ keys (the median when $k \approx n/2$). Partitioning around a pivot and recursing into **one** side is linear when the pivot is good; the median-of-medians rule guarantees a good pivot without randomness:[^clrs9][^6046-l2]

1. Split the keys into groups of 5 and take each group's median: $\lceil n/5 \rceil$ medians in $O(n)$.
2. Find the median $x$ of these medians **recursively**.
3. Partition around $x$; recurse into the side that contains rank $k$, or return $x$.

At least half of the $\lceil n/5 \rceil$ groups have a median $\ge x$, and each of them, except possibly the group of $x$ and a last incomplete group, holds 3 keys $\ge x$. So at least $3\left(\lceil \tfrac12 \lceil n/5 \rceil \rceil - 2\right) \ge \tfrac{3n}{10} - 6$ keys are $\ge x$, symmetrically for $\le x$, and the recursive call sees at most $\tfrac{7n}{10} + 6$ keys:[^clrs9]

$$T(n) \le T(\lceil n/5 \rceil) + T(7n/10 + 6) + O(n).$$

The two recursive sizes add up to about $\tfrac{9}{10}n$, so the work shrinks geometrically from level to level and $T(n) = O(n)$ (substitution proof in Exercise 3). Randomized quickselect is simpler and faster on average, but linear only in expectation ([[Randomized Algorithm]]).

## Advanced (L3)

### Divide and conquer inside a dynamic program

A global alignment of $u$ (length $n$) and $v$ (length $m$) by [[Dynamic Programming]] fills an $(n+1) \times (m+1)$ grid: the score needs only two rows, but the traceback needs the whole grid, $\Theta(nm)$ memory. Hirschberg's divide and conquer keeps linear memory:[^jones] score the top half of $u$ against every prefix of $v$ (forward, two rows), the bottom half against every suffix of $v$ (backward, two rows), choose the split $j^*$ of $v$ that maximizes the sum, and recurse on (top half, $v_{1..j^*}$) and (bottom half, $v_{j^*+1..m}$). If one scoring pass over an $n \times m$ grid costs $c\,nm$, substitution of $T \le 2c \cdot$ area gives

$$T(n, m) \le c\,nm + 2c\,\tfrac{n}{2}j^* + 2c\,\tfrac{n}{2}(m - j^*) = 2c\,nm,$$

since the two subproblems cover half of the grid's area: each level costs half the previous one. Twice the time of the plain algorithm buys $O(n + m)$ memory ([[Hirschberg Algorithm]]).

### Unbalanced splits: skew suffix sorting

Splits need not be halves. The skew algorithm recurses on the suffixes starting at positions $i \bmod 3 \neq 0$, renamed as a string of about $2n/3$ integer ranks, sorts the remaining third using those ranks, and merges in linear time, with integer sorting as its only other tool[^karkkainen] ([[Radix Sort]]). Its recurrence $T(n) = T(\lceil 2n/3 \rceil) + O(n)$ is a geometric series of ratio $2/3$, so $T(n) = O(n)$ (Exercise 5): one recursive call on a constant fraction with linear extra work is linear, the same shape as [[Binary Search]] with constant extra work.

### When a split pays, and when it does not

- **Fewer subproblems.** Strassen's algorithm multiplies $n \times n$ matrices with 7 half-size products instead of 8: $T(n) = 7T(n/2) + \Theta(n^2) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$.[^clrs4][^6046-l2] The [[Fast Fourier Transform]] applies the same paradigm to polynomial multiplication.
- **Overlapping subproblems.** When subproblems repeat (edit distance on suffixes, [[Recursion#Overlapping subproblems and memoization]]), plain divide and conquer recomputes them exponentially often; tabulate them instead ([[Dynamic Programming]]).
- **Base cases are an engineering choice.** Recursing down to size 1 is optimal only on paper: below some size the simple quadratic method has the smaller constant, so practical code switches to it at a cutoff that is measured, not derived.
- **Independent subproblems** can run in parallel, and once a subproblem fits in cache it stops paying for memory traffic: two reasons divide and conquer is a default design for large data.

## Mathematical representation

- **Recurrence.** For an instance of size $n$ split into subproblems of sizes $n_1, \dots, n_a < n$, with divide and combine costs $D(n)$ and $C(n)$:
$$T(n) = \sum_{i=1}^{a} T(n_i) + D(n) + C(n), \qquad T(n) = \Theta(1) \text{ for } n \le n_0.$$
- **Equal splits** $n_i = n/b$ give $T(n) = aT(n/b) + f(n)$, solved by comparing $f(n)$ with $n^{\log_b a}$ ([[Master Theorem]]).
- **Shrinking total size.** If $\sum_i n_i \le \alpha n$ for some constant $\alpha < 1$ (up to additive constants) and $D(n) + C(n) \le cn$, the subproblems at depth $j$ have total size at most $\alpha^j n$, so $T(n) \le \sum_{j \ge 0} c\,\alpha^j n = \frac{c}{1 - \alpha}\,n = O(n)$. Selection has $\alpha = 9/10$, skew $\alpha = 2/3$.

## Computational representation

The three algorithms, instrumented with counters and tested against brute force on small random inputs:

```python
import math
import random
from itertools import combinations

# --- Karatsuba: three half-size products instead of four ---------------------
PRODUCTS = 0                                   # base-case multiplications performed

def karatsuba(x: int, y: int) -> int:
    """x * y for non-negative integers, splitting in base 10."""
    global PRODUCTS
    if x < 10 or y < 10:                       # base case: a one-digit factor
        PRODUCTS += 1
        return x * y
    m = max(len(str(x)), len(str(y))) // 2
    a, b = divmod(x, 10 ** m)                  # x = a 10^m + b
    c, d = divmod(y, 10 ** m)                  # y = c 10^m + d
    ac, bd = karatsuba(a, c), karatsuba(b, d)
    middle = karatsuba(a + b, c + d) - ac - bd  # = ad + bc, one product instead of two
    return ac * 10 ** (2 * m) + middle * 10 ** m + bd

# --- Closest pair of points in O(n log n) --------------------------------------
DISTANCES = 0

def dist(p, q) -> float:
    global DISTANCES
    DISTANCES += 1
    return math.hypot(p[0] - q[0], p[1] - q[1])

def closest_pair(px: list, py: list = None) -> tuple:
    """(distance, p, q) for distinct points; px and py: the points sorted by x and by y."""
    if py is None:                             # top call: presort once by x and once by y
        px, py = sorted(px), sorted(px, key=lambda p: (p[1], p[0]))
    if len(px) <= 3:                           # base case: brute force
        return min((dist(p, q), p, q) for p, q in combinations(px, 2))
    mid = len(px) // 2
    x_mid = px[mid][0]                         # vertical dividing line
    left = set(px[:mid])
    best = min(closest_pair(px[:mid], [p for p in py if p in left]),   # y order kept: O(n) split
               closest_pair(px[mid:], [p for p in py if p not in left]))
    delta = best[0]
    strip = [p for p in py if abs(p[0] - x_mid) < delta]               # y-sorted strip
    for i, p in enumerate(strip):
        for q in strip[i + 1:i + 8]:           # at most 7 successors can be closer than delta
            if q[1] - p[1] >= delta:
                break
            best = min(best, (dist(p, q), p, q))
    return best

# --- Worst-case linear-time selection (median of medians) ----------------------
TOUCHED = 0                                    # elements scanned by all partition steps

def select(a: list, k: int):
    """k-th smallest element of a (k = 0 is the minimum), worst-case O(n)."""
    global TOUCHED
    if len(a) <= 5:
        return sorted(a)[k]
    medians = [sorted(a[i:i + 5])[len(a[i:i + 5]) // 2] for i in range(0, len(a), 5)]
    pivot = select(medians, len(medians) // 2)  # median of the group medians
    TOUCHED += len(a)
    lows = [x for x in a if x < pivot]
    highs = [x for x in a if x > pivot]
    n_equal = len(a) - len(lows) - len(highs)
    if k < len(lows):
        return select(lows, k)
    if k < len(lows) + n_equal:
        return pivot
    return select(highs, k - len(lows) - n_equal)

rng = random.Random(1)
for _ in range(300):                           # tests against brute-force oracles
    x, y = rng.randrange(10 ** rng.randint(1, 40)), rng.randrange(10 ** rng.randint(1, 40))
    assert karatsuba(x, y) == x * y
    pts = rng.sample([(i, j) for i in range(30) for j in range(30)], rng.randint(2, 60))
    assert closest_pair(pts)[0] == min(dist(p, q) for p, q in combinations(pts, 2))
    xs = [rng.randrange(50) for _ in range(rng.randint(1, 80))]
    assert all(select(xs, k) == sorted(xs)[k] for k in range(len(xs)))

pts = [(rng.random(), rng.random()) for _ in range(2000)]
DISTANCES = 0
closest_pair(pts)
print("closest pair, n = 2000:", DISTANCES, "distance computations; all pairs:", 2000 * 1999 // 2)

PRODUCTS = 0
print("1234 x 5678 =", karatsuba(1234, 5678), "with", PRODUCTS, "base-case products")
```

```text
closest pair, n = 2000: 2994 distance computations; all pairs: 1999000
1234 x 5678 = 7006652 with 11 base-case products
```

The 300 randomized tests pass silently. For 2,000 random points, the closest-pair recursion computes 2,994 distances instead of the 1,999,000 of the all-pairs method.

## Worked example

> [!example] Karatsuba on $1234 \times 5678$
> 1. **Split** at $m = 2$ digits: $x = 12 \cdot 10^2 + 34$ and $y = 56 \cdot 10^2 + 78$, so $a = 12$, $b = 34$, $c = 56$, $d = 78$.
> 2. **Three products**: $ac = 12 \times 56 = 672$; $bd = 34 \times 78 = 2652$; $(a + b)(c + d) = 46 \times 134 = 6164$.
> 3. **Middle coefficient without a fourth product**: $ad + bc = 6164 - 672 - 2652 = 2840$. Check: $12 \times 78 + 34 \times 56 = 936 + 1904 = 2840$.
> 4. **Recombine by shifts and additions**: $672 \cdot 10^4 + 2840 \cdot 10^2 + 2652 = 6{,}720{,}000 + 284{,}000 + 2{,}652 = 7{,}006{,}652$.
> 5. **Recursion**: each of the three products is computed by the same split until a factor has one digit: 11 base cases in the code above. Note that $c + d = 134$ has one digit more than $c$ and $d$: subproblems of size $n/2 + 1$ instead of $n/2$, which does not change the $\Theta$ class.

## Common misconceptions

> [!warning] "Divide and conquer splits in half, so it runs in $n \log n$"
> The cost depends on the number of subproblems, their sizes and the combine cost. Four half-size products give $n^2$, three give $n^{1.585}$; selection recurses into one side only and is linear, and so is skew suffix sorting with its two-thirds recursion. Write the recurrence before quoting a bound ([[Master Theorem]]).

> [!warning] "The strip of closest pair can hold $\Theta(n)$ points, so the combine step is quadratic"
> The strip can indeed hold every point, but each one is compared with at most 7 successors in $y$ order: the combine step makes at most $7n$ distance computations. Hence 2,994 distances for 2,000 points above.

> [!warning] "Dividing is free"
> Slicing a Python list copies it: $\Theta(n)$ per call. Harmless when the combine step is linear anyway, as in merge sort, but it turns binary search into $T(n) = T(n/2) + \Theta(n) = \Theta(n)$. Pass index bounds, as [[Binary Search]] does.

## Exercises

> [!question] Exercise 1 (L2)
> A colleague proposes a ternary merge sort: sort three thirds recursively, then merge three lists by repeatedly taking the smallest of the three fronts. Write the recurrence and solve it. Does it beat binary merge sort, asymptotically and in comparisons?

> [!success]- Solution
> $T(n) = 3T(n/3) + \Theta(n) = \Theta(n \log n)$: the same class. Comparisons: finding the smallest of three fronts takes up to 2 comparisons per output item, so up to $2n$ per level over $\log_3 n$ levels: $2n\log_3 n = \frac{2}{\log_2 3}\, n \log_2 n \approx 1.26\, n \log_2 n$, worse than the $n \log_2 n$ of binary merge sort. More subproblems only pay when they make the combine step cheaper or the subproblems smaller.

> [!question] Exercise 2 (L2)
> In the closest-pair combine step, prove that a $\delta \times \delta$ square contains at most 4 points of $P_L$ (or of $P_R$). Show that 4 is reachable.

> [!success]- Solution
> Two points of the same half are at distance $\ge \delta$, since $\delta \le \delta_L$ and $\delta \le \delta_R$. Cut the square into four closed cells of side $\delta/2$; each has diameter $\delta/\sqrt{2} < \delta$, so it contains at most one point of that half. Every point of the square lies in some cell, hence at most 4 points. The four corners of the square are pairwise at distance $\delta$ or $\sqrt{2}\,\delta$, so 4 is reachable. Two halves give at most 8 points in the $\delta \times 2\delta$ box, $p$ included: at most 7 candidates.

> [!question] Exercise 3 (L2)
> Prove by substitution that median-of-medians selection is $O(n)$, assuming $T(n) = O(1)$ for $n \le 140$ and $T(n) \le T(\lceil n/5 \rceil) + T(7n/10 + 6) + an$ otherwise. Then explain why groups of 3 fail and groups of 7 work.

> [!success]- Solution
> Assume $T(k) \le ck$ for all $k < n$, with $n > 140$. Then $T(n) \le c(n/5 + 1) + c(7n/10 + 6) + an = cn + (-cn/10 + 7c + an)$. The bracket is $\le 0$ when $c \ge 10a \cdot \frac{n}{n - 70}$; for $n \ge 140$, $\frac{n}{n-70} \le 2$, so $c \ge 20a$ (and large enough for the base cases) completes the induction. **Groups of 3**: the pivot only guarantees about $n/3$ keys on each side, $T(n) = T(n/3) + T(2n/3) + O(n)$; the sizes add up to $n$, every level costs $\Theta(n)$ over $\Theta(\log n)$ levels: $\Theta(n \log n)$. **Groups of 7**: at least $4(\lceil \frac12 \lceil n/7 \rceil \rceil - 2) \ge \frac{2n}{7} - 8$ keys on each side, so $T(n) \le T(n/7) + T(5n/7 + 8) + O(n)$; the sizes add up to $\frac{6}{7}n$: linear.

> [!question] Exercise 4 (L3, Python)
> The N50 of an assembly is the largest length $L$ such that contigs of length $\ge L$ contain at least half of the assembled bases.[^lander] Compute it in $O(n)$ without sorting: take the median length as pivot with `select` (code above) and keep only the side that contains the half-way point. Test against the sorting definition on invented contig lengths.

> [!success]- Solution
> ```python
> def n50_sorted(lengths: list) -> int:
>     total, covered = sum(lengths), 0
>     for length in sorted(lengths, reverse=True):
>         covered += length
>         if 2 * covered >= total:
>             return length
>
> def n50_select(lengths: list) -> int:
>     """N50 in O(n): keep only the side of the median that holds the half-way point."""
>     total, covered, a = sum(lengths), 0, list(lengths)
>     while True:
>         pivot = select(a, len(a) // 2)
>         longer = [x for x in a if x > pivot]
>         equal_sum = pivot * a.count(pivot)
>         if 2 * (covered + sum(longer)) >= total:
>             a = longer                         # half-way point among longer contigs
>         elif 2 * (covered + sum(longer) + equal_sum) >= total:
>             return pivot
>         else:
>             covered += sum(longer) + equal_sum
>             a = [x for x in a if x < pivot]    # half-way point among shorter contigs
>
> rng = random.Random(7)
> for _ in range(500):
>     contigs = [rng.randint(1, 5000) for _ in range(rng.randint(1, 200))]   # invented lengths
>     assert n50_select(contigs) == n50_sorted(contigs)
> toy = [12_000, 800, 45_000, 3_100, 27_500, 950, 8_200, 61_000, 1_500, 19_000]   # invented
> print(n50_sorted(toy), n50_select(toy), sum(toy))
> TOUCHED = 0
> big = [rng.randint(500, 200_000) for _ in range(100_000)]
> print(n50_select(big) == n50_sorted(big), f"{TOUCHED / len(big):.2f} n")
> ```
> Output: `45000 45000 179050`, then `True 6.43 n`. By hand: $61{,}000 < 179{,}050/2 = 89{,}525 \le 61{,}000 + 45{,}000$, so N50 = 45,000. Each round costs $O(|a|)$ and keeps at most half of the contigs, because the pivot is the median: $O(n + n/2 + n/4 + \dots) = O(n)$, measured as $6.43n$ elements scanned for 100,000 contigs.

> [!question] Exercise 5 (L3)
> Show that the skew recurrence $T(n) = T(\lceil 2n/3 \rceil) + cn$ (with $T(n) = O(1)$ for $n \le 2$) gives $T(n) \le 3cn + O(\log n)$. What does it share with Hirschberg's bound $T(n, m) \le 2c\,nm$?

> [!success]- Solution
> The sizes satisfy $n_{j+1} \le \frac23 n_j + 1$, so $n_j \le (\frac23)^j n + 3$, over $O(\log n)$ levels: $T(n) \le c\sum_j \left((\tfrac23)^j n + 3\right) \le 3cn + O(\log n)$.
> Both recurrences shrink the total size (length or grid area) by a constant factor per level, $2/3$ and $1/2$, so the top level dominates and the total is $\frac{1}{1 - \alpha}$ times the top level's work: $3cn$ and $2c\,nm$.

## Mastery checklist

- [ ] 1 Recognized: I can name the three steps and write the recurrences of merge sort, Karatsuba, closest pair and median-of-medians selection.
- [ ] 2 Understood: I can explain Karatsuba's identity, the 7-successor packing argument and why the median of medians guarantees a $3/10$ split.
- [ ] 3 Practiced: I can implement the three algorithms with brute-force test oracles and prove their bounds by substitution.
- [ ] 4 Applied: in [[04-alignment-engine]] I implement linear-space alignment by divide and conquer and check it against the full-traceback version on real sequences.
- [ ] 5 Explained: I can teach when a split pays (fewer subproblems, geometrically shrinking size), when it does not (overlapping subproblems), and why practical code uses base-case cutoffs.

## References

[^clrs2]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 2 "Getting Started" (the divide-and-conquer method, merge sort).
[^clrs4]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 4 "Divide-and-Conquer" (divide, conquer, combine; Strassen's algorithm for matrix multiplication; solving recurrences).
[^clrs9]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 9 "Medians and Order Statistics" (selection in expected linear time and in worst-case linear time).
[^6046-l2]: [[MIT 6.046J - Design and Analysis of Algorithms]], Spring 2015, lecture 2 "Divide & Conquer: Convex Hull, Median Finding", and its recitation (master theorem, Strassen's algorithm).
[^stanford]: [[Coursera Stanford - Algorithms Specialization]], course 1 "Divide and Conquer, Sorting and Searching, and Randomized Algorithms": integer and matrix multiplication, the master method, an $O(n \log n)$ closest-pair algorithm, linear-time selection.
[^karatsuba]: [[Karatsuba 1962 - Multiplication of Multidigit Numbers on Automata]], *Doklady Akademii Nauk SSSR* 145(2):293-294 (English translation in *Soviet Physics Doklady* 7:595-596, 1963).
[^karkkainen]: [[Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction]], ICALP 2003, LNCS 2719:943-955.
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]], divide-and-conquer treatment of space-efficient sequence alignment.
[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]], *Nature* 409:860-921, definition of the N50 length of an assembly.
