---
aliases:
  - Master Method
  - Recursion-Tree Method
  - Substitution Method
  - Akra-Bazzi Method
  - Divide-and-Conquer Recurrence
  - Théorème maître
tags:
  - type/concept
  - domain/computer-science
  - domain/mathematics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Recursion]]"
  - "[[Recurrence Relation]]"
  - "[[Big O Notation]]"
  - "[[Logarithm]]"
  - "[[Infinite Series]]"
  - "[[Mathematical Induction]]"
  - "[[Divide and Conquer]]"
related:
  - "[[Sorting]]"
  - "[[Binary Search]]"
  - "[[Amortized Analysis]]"
  - "[[Randomized Algorithm]]"
  - "[[Fast Fourier Transform]]"
  - "[[Hirschberg Algorithm]]"
  - "[[Suffix Array Construction]]"
projects:
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.046J - Design and Analysis of Algorithms]]"
  - "[[Coursera Stanford - Algorithms Specialization]]"
  - "[[Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction]]"
---

# Master Theorem

> [!abstract]
> The master theorem solves the divide-and-conquer recurrence $T(n) = aT(n/b) + f(n)$ by comparing the work $f(n)$ at the root of the recursion tree with its number of leaves, $n^{\log_b a}$: whichever is polynomially larger dominates, and a tie costs one extra logarithmic factor.

## Definition

Let $a \ge 1$ and $b > 1$ be constants, $f(n)$ an asymptotically nonnegative function, and $T(n) = aT(n/b) + f(n)$ for large $n$, with $n/b$ read as $\lfloor n/b \rfloor$ or $\lceil n/b \rceil$ and $T(n) = \Theta(1)$ for small $n$. Then:[^clrs4]

1. If $f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$.
2. If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for some constant $k \ge 0$, then $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
3. If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$, and the **regularity condition** $a f(n/b) \le c f(n)$ holds for some constant $c < 1$ and all large $n$, then $T(n) = \Theta(f(n))$.

It is one of three methods for such recurrences, with the **substitution method** (guess a bound, prove it by induction) and the **recursion-tree method** (sum the cost level by level), of which it is the packaged general case.[^clrs4][^stanford][^6046-l2]

## Why it matters

- **Predict before implementing.** A design's recurrence gives its $\Theta$ class in one line: three half-size products instead of four turn $\Theta(n^2)$ into $\Theta(n^{1.585})$ ([[Divide and Conquer#Karatsuba multiplication]]).
- **It names the lever.** Fewer subproblems ($a$), smaller subproblems ($b$) or a cheaper split and combine ($f$): the theorem tells which of the three dominates, hence which one is worth optimizing.
- **Reading complexity claims.** The skew suffix-array algorithm recurses on two thirds of the suffixes with linear extra work,[^karkkainen] which case 3 makes linear; a divide and conquer whose combine step sorts ($f(n) = n \log n$) costs $n \log^2 n$, not $n \log n$.
- **Genome scale.** At $n = 3 \times 10^9$, $\log_2 n \approx 31.5$: one extra logarithmic factor is a 30-fold slowdown, the difference between hours and days.

## Core (L2)

### The recursion tree behind the theorem

Take $n = b^L$. Depth $j$ of the recursion tree has $a^j$ subproblems of size $n/b^j$, costing $a^j f(n/b^j)$; the leaves sit at depth $L = \log_b n$ and number $a^{\log_b n} = n^{\log_b a}$ (both equal $b^{\log_b a \cdot \log_b n}$). Hence

$$T(n) = \underbrace{\Theta\!\left(n^{\log_b a}\right)}_{\text{leaves}} + \underbrace{\sum_{j=0}^{L-1} a^j f\!\left(n/b^j\right)}_{\text{internal levels}}.$$

![[master-theorem-level-costs.svg]]

For $f(n) = n^c$ the level cost is $a^j (n/b^j)^c = n^c\,r^j$ with ratio $r = a/b^c$: a geometric series. The three cases are its three behaviors.

- **Case 1** ($r > 1$, i.e. $c < \log_b a$): the series increases; its last terms, the leaves, dominate: $\Theta(n^{\log_b a})$. In general, $f(n) \le C n^{\log_b a - \epsilon}$ makes level $j$ cost at most $C n^{\log_b a - \epsilon}\, b^{\epsilon j}$, a geometric series of ratio $b^\epsilon > 1$ whose sum is $O(n^{\log_b a - \epsilon} \cdot b^{\epsilon L}) = O(n^{\log_b a})$.
- **Case 2** ($r = 1$): all $L = \log_b n$ levels cost the same $\Theta(n^{\log_b a})$, hence the extra $\log n$. With $f(n) = \Theta(n^{\log_b a} \log^k n)$, level $j$ costs $\Theta(n^{\log_b a} (L - j)^k)$ and $\sum_{i=1}^{L} i^k = \Theta(L^{k+1})$.
- **Case 3** ($r < 1$): iterating regularity gives $a^j f(n/b^j) \le c^j f(n)$, so the internal levels sum to at most $f(n)/(1 - c)$; the root alone costs $f(n)$, and $f$ dominates the leaves: $\Theta(f(n))$.

### Applying it

| Algorithm | Recurrence | $n^{\log_b a}$ | Case | $T(n)$ |
|---|---|---|---|---|
| [[Binary Search]] | $T(n/2) + \Theta(1)$ | $1$ | 2, $k = 0$ | $\Theta(\log n)$ |
| Merge sort ([[Sorting]]) | $2T(n/2) + \Theta(n)$ | $n$ | 2, $k = 0$ | $\Theta(n \log n)$ |
| Karatsuba | $3T(n/2) + \Theta(n)$ | $n^{1.585}$ | 1 | $\Theta(n^{\log_2 3})$ |
| Strassen[^clrs4] | $7T(n/2) + \Theta(n^2)$ | $n^{2.807}$ | 1 | $\Theta(n^{\log_2 7})$ |
| Skew suffix sorting | $T(2n/3) + \Theta(n)$, so $b = 3/2$ | $1$ | 3 | $\Theta(n)$ |
| Combine step that sorts | $2T(n/2) + \Theta(n \log n)$ | $n$ | 2, $k = 1$ | $\Theta(n \log^2 n)$ |
| Median of medians | $T(n/5) + T(7n/10) + \Theta(n)$ | unequal sizes | none | $\Theta(n)$ (Advanced) |

### The substitution method, and its classic trap

To prove $T(n) = 2T(\lfloor n/2 \rfloor) + n = O(n \log n)$, guess $T(n) \le c\,n \lg n$ for $n \ge 2$ and assume it below $n$:

$$T(n) \le 2c \lfloor n/2 \rfloor \lg \lfloor n/2 \rfloor + n \le c\,n \lg(n/2) + n = c\,n \lg n - (c - 1)\,n \le c\,n \lg n \quad \text{for } c \ge 1.$$

The base cases are $n = 2$ and $n = 3$ (not $n = 1$, where $c \cdot 1 \cdot \lg 1 = 0$): take $c$ large enough for them too. Two rules make such proofs work:

- **Reproduce the exact hypothesis.** "Proving" $T(n) = O(n)$ by $T(n) \le 2c\lfloor n/2 \rfloor + n \le cn + n = O(n)$ is wrong: the hypothesis was $T(n) \le cn$, and $(c + 1)n > cn$. The constant would grow by one at each of the $\lg n$ levels.
- **Strengthen by subtracting a lower-order term.** For $T(n) = 2T(n/2) + 1$, the guess $T(n) \le cn$ fails ($cn + 1$), but $T(n) \le cn - d$ succeeds: $2(cn/2 - d) + 1 = cn - 2d + 1 \le cn - d$ whenever $d \ge 1$.

## Advanced (L3)

### Gaps between the cases

Cases 1 and 3 need a **polynomial** gap $n^{\epsilon}$. Logarithmic gaps fall to case 2 when $k \ge 0$; below that, the theorem is silent. For $T(n) = 2T(n/2) + n/\lg n$ with $n = 2^m$, level $j$ costs $2^j \cdot \frac{n/2^j}{\lg(n/2^j)} = \frac{n}{m - j}$, so

$$T(n) = n\,T(1) + n \sum_{j=0}^{m-1} \frac{1}{m - j} = n\,(1 + H_{\lg n}) = \Theta(n \log \log n),$$

with $H_m$ the $m$-th harmonic number. Regularity, by contrast, never fails for the functions algorithms produce: if $f(n) = n^c \lg^k n$ with $c > \log_b a$, then $a f(n/b) \le \frac{a}{b^c} f(n)$ and $\frac{a}{b^c} < 1$.

### Floors, ceilings and exact solutions

Real algorithms split into $\lceil n/2 \rceil$ and $\lfloor n/2 \rfloor$; the theorem's conclusion is unchanged.[^clrs4] Exact solutions can still be informative: merge sort's worst-case comparison count satisfies $W(n) = W(\lceil n/2 \rceil) + W(\lfloor n/2 \rfloor) + n - 1$, $W(1) = 0$, whose solution is

$$W(n) = n \lceil \lg n \rceil - 2^{\lceil \lg n \rceil} + 1$$

(Exercise 5). $W(1000) = 8{,}977$ bounds the 8,730 comparisons measured on a random input of 1,000 keys in [[Sorting#Implementation]].

### Change of variables

$T(n) = 2T(\sqrt{n}) + \lg n$ is not of master form, but with $m = \lg n$ and $S(m) = T(2^m)$ it becomes $S(m) = 2S(m/2) + m = \Theta(m \log m)$, so $T(n) = \Theta(\log n \log \log n)$.

### Akra-Bazzi: unequal splits

For $T(x) = \sum_{i=1}^{k} a_i T(b_i x) + g(x)$ with constants $a_i > 0$ and $0 < b_i < 1$, let $p$ be the unique real number with $\sum_i a_i b_i^{\,p} = 1$. Then[^clrs4]

$$T(x) = \Theta\!\left(x^p \left(1 + \int_1^x \frac{g(u)}{u^{p+1}}\, du\right)\right).$$

The master theorem is the case $k = 1$, $p = \log_b a$. For median-of-medians selection, $(1/5)^p + (7/10)^p = 1$ gives $p \approx 0.840 < 1$ and $\int_1^x u^{-p}\,du = \frac{x^{1-p} - 1}{1 - p}$, so $T(x) = \Theta(x^p \cdot x^{1-p}) = \Theta(x)$ (Exercise 6).

## Mathematical representation

- $a$: number of subproblems; $b$: factor by which the size shrinks; $f(n)$: cost of dividing and combining at size $n$; $L = \log_b n$: depth; $n^{\log_b a} = a^{L}$: number of leaves.
- **Exact unrolling** for $n = b^L$: $T(n) = n^{\log_b a}\, T(1) + \sum_{j=0}^{L-1} a^j f(n/b^j)$.
- **Geometric series lemma**: $\sum_{j=0}^{L} r^j$ is $\Theta(1)$ if $0 < r < 1$, equal to $L + 1$ if $r = 1$, and $\Theta(r^L)$ if $r > 1$ ([[Infinite Series]]). With $f(n) = n^c$ and $r = a/b^c$, these are cases 3, 2 and 1.
- **Asymptotic notation** follows [[Big O Notation]]; $\lg = \log_2$, and the base of a logarithm inside $\Theta$ does not matter ([[Logarithm]]).

## Computational representation

A classifier for $f(n) = n^c \log^k n$, checked against exact evaluations of the recurrences (floors included): the ratio $T(n)/g(n)$ must stay bounded when $g$ is the right answer.

```python
import math
from functools import lru_cache

def theta(e: float, k: int) -> str:
    power = "" if math.isclose(e, 0) else "n" if math.isclose(e, 1) else f"n^{e:.4g}"
    logs = "" if k == 0 else "log n" if k == 1 else f"log^{k} n"
    return " ".join(part for part in (power, logs) if part) or "1"

def master(a: float, b: float, c: float, k: int = 0) -> str:
    """Theta class of T(n) = a T(n/b) + Theta(n^c log^k n), with a >= 1, b > 1, k >= 0."""
    e = math.log(a, b)                     # watershed exponent log_b a
    if math.isclose(c, e):
        return theta(e, k + 1)             # case 2: every level costs about the same
    return theta(e, 0) if c < e else theta(c, k)   # case 1: leaves win; case 3: root wins

def evaluate(a: int, shrink, f, n: int) -> float:
    """Exact T(n) = a T(shrink(n)) + f(n), with T(n) = 1 for n <= 1."""
    @lru_cache(maxsize=None)
    def T(m: int) -> float:
        return 1.0 if m <= 1 else a * T(shrink(m)) + f(m)
    return T(n)

lg = math.log2
cases = [  # name, a, b, f as (c, k), shrink, f, guess g(n)
    ("binary search",  1, 2,   (0, 0), lambda m: m // 2,         lambda m: 1,             lambda n: lg(n)),
    ("merge sort",     2, 2,   (1, 0), lambda m: m // 2,         lambda m: m,             lambda n: n * lg(n)),
    ("Karatsuba",      3, 2,   (1, 0), lambda m: m // 2,         lambda m: m,             lambda n: n ** lg(3)),
    ("Strassen",       7, 2,   (2, 0), lambda m: m // 2,         lambda m: m * m,         lambda n: n ** lg(7)),
    ("skew suffix sort", 1, 1.5, (1, 0), lambda m: 2 * m // 3, lambda m: m,           lambda n: n),
    ("2T(n/2)+n lg n", 2, 2,   (1, 1), lambda m: m // 2,         lambda m: m * lg(m),     lambda n: n * lg(n) ** 2),
    ("3T(n/4)+n lg n", 3, 4,   (1, 1), lambda m: m // 4,         lambda m: m * lg(m),     lambda n: n * lg(n)),
]
for name, a, b, (c, k), shrink, f, g in cases:
    ratios = [evaluate(a, shrink, f, n) / g(n) for n in (2 ** 10, 2 ** 20, 2 ** 40)]
    print(f"{name:17} Theta({master(a, b, c, k)}):", " ".join(f"{r:.3f}" for r in ratios))
```

```text
binary search     Theta(log n): 1.100 1.050 1.025
merge sort        Theta(n log n): 1.100 1.050 1.025
Karatsuba         Theta(n^1.585): 2.965 2.999 3.000
Strassen          Theta(n^2.807): 2.328 2.333 2.333
skew suffix sort  Theta(n): 2.980 3.000 3.000
2T(n/2)+n lg n    Theta(n log^2 n): 0.560 0.527 0.513
3T(n/4)+n lg n    Theta(n log n): 2.193 2.870 3.402
```

Each ratio, at $n = 2^{10}, 2^{20}, 2^{40}$, settles near a constant, and the constants can be derived: $T(n) = 3n^{\lg 3} - 2n$ for Karatsuba with $T(1) = 1$ gives 3; the skew recurrence gives $1/(1 - 2/3) = 3$; $2T(n/2) + n \lg n$ gives $\frac{1}{2} n \lg^2 n + O(n \log n)$. The last line converges slowly, which the worked example explains.

## Worked example

> [!example] $T(n) = 3T(n/4) + n \lg n$
> 1. **Identify**: $a = 3$, $b = 4$, $f(n) = n \lg n$; leaves $n^{\log_4 3} = n^{0.792\ldots}$.
> 2. **Compare**: $f(n) = n \lg n \ge n^{0.9925} = n^{\log_4 3 + 0.2}$ for $n \ge 2$, so $f(n) = \Omega(n^{\log_4 3 + \epsilon})$ with $\epsilon = 0.2$: a polynomial gap, candidate case 3.
> 3. **Regularity**: $a f(n/b) = 3 \cdot \frac{n}{4} \lg \frac{n}{4} \le \frac{3}{4}\, n \lg n = \frac34 f(n)$, so $c = 3/4 < 1$.
> 4. **Conclude**: $T(n) = \Theta(n \lg n)$; the root does a constant fraction of all the work.
> 5. **Constant**: level $j$ costs $(3/4)^j n (\lg n - 2j)$; with $\sum_j (3/4)^j = 4$ and $\sum_j j (3/4)^j = 12$, $T(n) \approx 4n \lg n - 24n$. The ratio $T(n)/(n \lg n) \approx 4 - 24/\lg n$ is $3.4$ at $n = 2^{40}$, as measured above: $\Theta$ is right, but the lower-order term is large at realistic sizes.

## Common misconceptions

> [!warning] "Case 3 applies whenever $f(n)$ grows faster than $n^{\log_b a}$"
> It needs a polynomial gap and regularity. In $2T(n/2) + n \lg n$, $f$ exceeds $n$ only by $\lg n$: this is case 2 with $k = 1$, and $T(n) = \Theta(n \log^2 n)$, not $\Theta(n \log n)$.

> [!warning] "The master theorem solves the recurrence of any recursive algorithm"
> It needs $a$ subproblems of the **same** size $n/b$. It says nothing about $T(n) = T(n-1) + n$ (subtract and conquer, $\Theta(n^2)$), about unequal splits such as $T(n/3) + T(2n/3) + n$ (recursion tree or Akra-Bazzi), or about the gap case $2T(n/2) + n/\lg n$.

> [!warning] "$T(n) \le cn + n = O(n)$ completes the induction"
> The induction must reproduce the exact hypothesis with the same constant. Letting the constant grow at each level proves nothing; subtract a lower-order term instead.

## Exercises

> [!question] Exercise 1 (L2)
> Solve, or say why the master theorem does not apply: (a) $4T(n/2) + n^2$; (b) $8T(n/2) + n^2$; (c) $2T(n/4) + \sqrt{n}$; (d) $2T(n/2) + n \lg n$; (e) $2T(n/2) + n/\lg n$; (f) $T(n - 1) + n$.

> [!success]- Solution
> (a) $\log_2 4 = 2$: case 2, $\Theta(n^2 \log n)$. (b) $\log_2 8 = 3 > 2$: case 1, $\Theta(n^3)$, the cost of recursive matrix multiplication with 8 products. (c) $\log_4 2 = 1/2$: case 2, $\Theta(\sqrt{n} \log n)$. (d) case 2 with $k = 1$: $\Theta(n \log^2 n)$. (e) gap below case 2: not covered; $\Theta(n \log \log n)$ by the recursion tree (Advanced). (f) not of the form $aT(n/b)$: unrolling gives $n + (n-1) + \dots + 1 = \Theta(n^2)$.

> [!question] Exercise 2 (L2)
> Prove $T(n) = 2T(\lceil n/2 \rceil) + n = O(n \log n)$ by substitution. Why do ceilings need more care than floors?

> [!success]- Solution
> With ceilings the subproblem can be larger than $n/2$, and $\lg \lceil n/2 \rceil$ can exceed $\lg(n/2)$. Guess $T(n) \le c\,n \lg n$ for $n \ge 3$. For $n \ge 5$, $\lceil n/2 \rceil \le (n+1)/2 \le 3n/5$, so $T(n) \le 2c \cdot \frac{n+1}{2} \lg \frac{3n}{5} + n = c(n+1)(\lg n - \lg \frac53) + n$. Since $\lg \frac53 \approx 0.737$, this is $c\,n\lg n + c\lg n - 0.737\,c(n+1) + n \le c\,n \lg n$ once $c \ge 2$ and $n$ is large enough that $c \lg n \le 0.737cn - n$; the finitely many smaller $n$ go into the base cases. The lesson: ceilings add lower-order terms that the slack $-(c-1)n$ must absorb.

> [!question] Exercise 3 (L2, Python)
> Use a recursion tree to show that $T(n) = T(\lfloor n/3 \rfloor) + T(n - \lfloor n/3 \rfloor) + n$ is $\Theta(n \log n)$, then check the ratio $T(n)/(n \lg n)$ numerically.

> [!success]- Solution
> Every level of the tree has total size at most $n$, so costs at most $n$. The shortest root-to-leaf path follows the $1/3$ branch and has length $\log_3 n$; the longest follows the $2/3$ branch, $\log_{3/2} n$. The first $\log_3 n$ levels are complete and cost exactly $n$ each, so $T(n) \ge n \log_3 n$; there are at most $\log_{3/2} n$ levels, so $T(n) \le n \log_{3/2} n$.
> ```python
> @lru_cache(maxsize=None)
> def U(n: int) -> int:
>     return 0 if n < 3 else U(n // 3) + U(n - n // 3) + n
> for n in (10 ** 3, 10 ** 5, 10 ** 7):
>     print(n, round(U(n) / (n * lg(n)), 3))
> ```
> Output: `1000 1.049`, `100000 1.063`, `10000000 1.07`: bounded, between the two bounds $1/\lg 3 \approx 0.63$ and $1/\lg 1.5 \approx 1.71$.

> [!question] Exercise 4 (L3)
> Solve $T(n) = T(\sqrt{n}) + 1$ and $T(n) = 2T(\sqrt{n}) + 1$ by a change of variables.

> [!success]- Solution
> With $m = \lg n$ and $S(m) = T(2^m)$: $S(m) = S(m/2) + 1 = \Theta(\log m)$, so $T(n) = \Theta(\log \log n)$, the recurrence of structures that recurse on $\sqrt{n}$-sized universes; and $S(m) = 2S(m/2) + 1 = \Theta(m)$ (case 1), so $T(n) = \Theta(\log n)$.

> [!question] Exercise 5 (L3, Python)
> Prove $W(n) = n\lceil \lg n \rceil - 2^{\lceil \lg n \rceil} + 1$ for merge sort's worst case, and check it for every $n < 5000$.

> [!success]- Solution
> Write $m = \lceil \lg n \rceil$ and $F_m(n) = nm - 2^m + 1$. Key fact: if $n = 2^{m-1}$ then $F_{m}(n) = F_{m-1}(n)$, since $n \cdot 1 = 2^m - 2^{m-1}$; so $F_{m'}(n)$ may use either value when $n$ is a power of 2. For $n \ge 2$, $2^{m-1} < n \le 2^m$ gives $2^{m-2} \le \lfloor n/2 \rfloor \le \lceil n/2 \rceil \le 2^{m-1}$, so both halves can use $m - 1$: $W(n) = F_{m-1}(\lceil n/2 \rceil) + F_{m-1}(\lfloor n/2 \rfloor) + n - 1 = n(m-1) - 2^m + 2 + n - 1 = F_m(n)$. Base: $W(1) = 0 = F_0(1)$.
> ```python
> @lru_cache(maxsize=None)
> def W(n: int) -> int:
>     """Worst-case comparisons of merge sort: W(n) = W(ceil(n/2)) + W(floor(n/2)) + n - 1."""
>     return 0 if n <= 1 else W((n + 1) // 2) + W(n // 2) + n - 1
>
> def closed_form(n: int) -> int:
>     m = (n - 1).bit_length()                    # = ceil(lg n) for n >= 1
>     return n * m - 2 ** m + 1
>
> assert all(W(n) == closed_form(n) for n in range(1, 5000))
> print(W(1000), W(1024), W(1025))
> ```
> Output: `8977 9217 9228`. One key past a power of 2 adds a whole level: $W(1025) - W(1024) = 11$.

> [!question] Exercise 6 (L3, Python)
> Compute the Akra-Bazzi exponent $p$ for median-of-medians selection with groups of 3, 5 and 7 (recursive sizes $n/3 + 2n/3$, $n/5 + 7n/10$ and $n/7 + 5n/7$) and conclude.

> [!success]- Solution
> ```python
> def akra_bazzi_p(fractions: list[float]) -> float:
>     """The p with sum(b_i^p) = 1, by bisection (each b_i in (0, 1), one call per term)."""
>     lo, hi = -10.0, 10.0
>     for _ in range(100):
>         mid = (lo + hi) / 2
>         lo, hi = (mid, hi) if sum(b ** mid for b in fractions) > 1 else (lo, mid)
>     return lo
>
> for name, parts in [("groups of 3", [1 / 3, 2 / 3]), ("groups of 5", [1 / 5, 7 / 10]),
>                     ("groups of 7", [1 / 7, 5 / 7])]:
>     print(name, round(akra_bazzi_p(parts), 4))
> ```
> Output: `groups of 3 1.0`, `groups of 5 0.8398`, `groups of 7 0.7632`. With $g(u) = u$: for $p = 1$ the integral is $\ln x$ and $T = \Theta(x \log x)$; for $p < 1$ it is $\Theta(x^{1-p})$ and $T = \Theta(x)$. Groups of 3 are too small, 5 and 7 give linear selection, matching [[Divide and Conquer#Exercises]] (Exercise 3).

## Mastery checklist

- [ ] 1 Recognized: I can state the three cases and identify $a$, $b$ and $f$ in a recurrence.
- [ ] 2 Understood: I can derive the three cases from the recursion tree as the three behaviors of a geometric series.
- [ ] 3 Practiced: I can solve recurrences by substitution (including the lower-order-term trick), recursion trees and the master theorem, and check them by exact evaluation.
- [ ] 4 Applied: before benchmarking a divide-and-conquer routine in [[bio-algorithms]], I predict its growth from its recurrence and compare with measured times.
- [ ] 5 Explained: I can teach the gaps between cases, regularity, floors and ceilings, changes of variables and Akra-Bazzi.

## References

[^clrs4]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 4 "Divide-and-Conquer" (Strassen's algorithm; substitution, recursion-tree and master methods; Akra-Bazzi recurrences).
[^6046-l2]: [[MIT 6.046J - Design and Analysis of Algorithms]], Spring 2015, recitation accompanying lecture 2 "Divide & Conquer: Convex Hull, Median Finding" (master theorem, Strassen's algorithm).
[^stanford]: [[Coursera Stanford - Algorithms Specialization]], course 1 "Divide and Conquer, Sorting and Searching, and Randomized Algorithms" (the master method).
[^karkkainen]: [[Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction]], ICALP 2003, LNCS 2719:943-955 (recursion on the suffixes at positions $i \bmod 3 \neq 0$, linear time).
