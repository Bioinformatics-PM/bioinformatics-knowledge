---
aliases:
  - Asymptotic Notation
  - Big Omega
  - Big Theta
  - Landau Notation
  - Time Complexity
  - Growth of Functions
  - Notation de Landau
  - Complexité asymptotique
tags:
  - type/concept
  - domain/computer-science
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Model of Computation]]"
  - "[[Function]]"
  - "[[Logarithm]]"
  - "[[Exponential Function]]"
  - "[[Limit]]"
  - "[[Summation Notation]]"
related:
  - "[[Space Complexity]]"
  - "[[Loop Invariant]]"
  - "[[Recursion]]"
  - "[[Master Theorem]]"
  - "[[Amortized Analysis]]"
  - "[[Exhaustive Search]]"
  - "[[NP-Completeness]]"
  - "[[Benchmarking]]"
projects:
  - "[[01-dna-engine]]"
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
---

# Big O Notation

> [!abstract]
> Asymptotic notation describes how a cost grows with the size of the input, ignoring constant factors and small inputs: $O(g)$ bounds a function from above, $\Omega(g)$ from below, and $\Theta(g)$ from both sides.

## Definition

For functions $f, g$ from $\mathbb{N}$ to $\mathbb{R}$ that are nonnegative for large $n$:[^clrs3]

$$\begin{aligned}
O(g) &= \{ f : \exists c > 0,\ \exists n_0,\ \forall n \ge n_0,\ 0 \le f(n) \le c\,g(n) \} \\
\Omega(g) &= \{ f : \exists c > 0,\ \exists n_0,\ \forall n \ge n_0,\ 0 \le c\,g(n) \le f(n) \} \\
\Theta(g) &= \{ f : \exists c_1, c_2 > 0,\ \exists n_0,\ \forall n \ge n_0,\ 0 \le c_1 g(n) \le f(n) \le c_2 g(n) \}
\end{aligned}$$

$c$, $c_1$, $c_2$ are positive constants that do not depend on $n$, and $n_0$ is the threshold beyond which the inequalities must hold. "$f(n) = O(g(n))$" means $f \in O(g)$: the equals sign denotes membership, not equality. A function is in $\Theta(g)$ if and only if it is in both $O(g)$ and $\Omega(g)$.[^clrs3]

## Why it matters

- **Feasibility at genome scale.** For $n = 3.055 \times 10^9$ bases (human T2T-CHM13),[^nurk] an $n \log_2 n$ algorithm executes about $10^{11}$ basic steps and a quadratic one about $10^{19}$: minutes against centuries (Core table). The growth rate decides what can run at all, before any code is tuned.
- **Reading methods sections and documentation.** Claims such as "linear in the genome length" or "quadratic in the number of sequences" are statements in this notation, with hidden constants and hidden assumptions (a fixed alphabet, a bounded read length) that you must recover.
- **Designing by successive improvement.** Compeau and Pevzner open their course with a naive frequent-words algorithm and then speed it up, for instance with a frequency array:[^compeau] each step is justified by a better growth rate (Worked example). In the Lab, [[01-dna-engine]] requires linear scans and [[05-sequence-search]] measures how runtime grows from 100 to 1M sequences, where the gap between $\Theta(n)$ and $\Theta(n^2)$ is the whole project.

## Core (L1)

### Why constants and small inputs are dropped

Counting steps in the [[Model of Computation]] gives exact formulas such as $T(n) = 3n^2 + 10n + 7$. At $n = 1000$, the leading term is 99.7 % of the total, and its share keeps growing; its constant 3 depends on the step convention, the language and the machine. Asymptotic notation keeps what survives every such change: the growth rate $n^2$. Analyses of algorithms state running times this way, ignoring constant factors and low-order terms.[^clrs3][^6006]

### Reading O, Ω and Θ

- $f = O(g)$: for large $n$, $f$ grows **at most** like $g$, up to a constant factor (upper bound).
- $f = \Omega(g)$: **at least** like $g$ (lower bound).
- $f = \Theta(g)$: **exactly** like $g$, up to constant factors (tight bound).

![[asymptotic-bounds-growth-rates.svg]]

Left: $f(n) = 3n^2 + 10n + 7$ is $\Theta(n^2)$ with $c_1 = 3$, $c_2 = 4$, $n_0 = 11$; below $n_0$ the upper bound fails, which the definition allows. Right: on a log scale, each function eventually exceeds every function below it, whatever the constants.

### Ranking the common growth rates

$$1 \prec \log n \prec \sqrt{n} \prec n \prec n \log n \prec n^2 \prec n^3 \prec 2^n \prec n!$$

where $f \prec g$ means $f = o(g)$, "negligible compared with $g$" (Deeper). Values, with the last column at the size of the human genome:

| Growth | Typical operation | $n = 10$ | $n = 10^3$ | $n = 10^6$ | $n = 3.055 \times 10^9$ |
|---|---|---:|---:|---:|---:|
| $\log_2 n$ | binary search in a sorted [[Suffix Array]] | 3.3 | 10 | 20 | 31.5 |
| $n$ | [[GC Content]], [[Reverse Complement]] | 10 | $10^3$ | $10^6$ | $3.1 \times 10^9$ |
| $n \log_2 n$ | sort $n$ reads or k-mers ([[Sorting]]) | 33 | $1.0 \times 10^4$ | $2.0 \times 10^7$ | $9.6 \times 10^{10}$ |
| $n^2$ | compare all pairs of $n$ reads | 100 | $10^6$ | $10^{12}$ | $9.3 \times 10^{18}$ |
| $n^3$ | three nested loops over $n$ items | $10^3$ | $10^9$ | $10^{18}$ | $2.9 \times 10^{28}$ |
| $2^n$ | try every subset of $n$ sequences | 1,024 | $1.1 \times 10^{301}$ | $10^{301\,030}$ | $10^{9.2 \times 10^8}$ |
| $n!$ | try every order of $n$ fragments | $3.6 \times 10^6$ | $4.0 \times 10^{2567}$ | $10^{5.6 \times 10^6}$ | $10^{2.8 \times 10^{10}}$ |

At an assumed round speed of $10^9$ simple steps per second, $n \log_2 n$ steps on the human genome take about 96 s, and $n^2$ steps about 296 years.

### Worst-case running time of nested loops

The rules follow from the definitions:

1. **Sequence and loops**: consecutive blocks cost $\Theta(f_1) + \Theta(f_2) = \Theta(\max(f_1, f_2))$; a loop costs the sum, over its iterations, of the cost of its body, so $m$ iterations of a constant-cost body cost $\Theta(m)$.
2. **Nested loops with independent bounds multiply**: $m_1$ outer iterations of an inner loop of $m_2$ iterations cost $\Theta(m_1 m_2)$.
3. **Dependent bounds are summed**: `for i in range(n): for j in range(i + 1, n)` runs $\sum_{i=0}^{n-1} (n - 1 - i) = n(n-1)/2 = \Theta(n^2)$ times. Halving the work does not change the class.
4. **Multiplicative steps** (`j *= 2` until `j >= n`) give $\lceil \log_2 n \rceil$ iterations.
5. **Worst case**: when a loop can stop early (`break` on the first match), the worst case is the input on which it never does.

Example: all pairwise [[Hamming Distance|Hamming distances]] of $n$ reads of length $L$ cost $\sum_{i<j} L = L\,n(n-1)/2 = \Theta(n^2 L)$, which is why all-against-all comparison does not scale to millions of reads and indexes such as [[K-mer]] tables exist.

## Deeper (L2)

### Proofs with explicit constants

- **$3n^2 + 10n + 7 = \Theta(n^2)$.** Lower bound: $3n^2 \le 3n^2 + 10n + 7$ for all $n \ge 0$ ($c_1 = 3$). Upper bound: for $n \ge 1$, $10n \le 10n^2$ and $7 \le 7n^2$, so $f(n) \le 20n^2$ ($c_2 = 20$, $n_0 = 1$). The figure uses $c_2 = 4$, $n_0 = 11$, because $10n + 7 \le n^2$ exactly when $n \ge 11$: the constants are not unique, only their existence matters.
- **$n^2 \ne O(n)$.** Suppose $n^2 \le cn$ for all $n \ge n_0$. Take $n = \max(n_0, \lfloor c \rfloor + 1)$: then $n > c$, so $n^2 > cn$, a contradiction.
- **Constants in exponents are not constant factors.** $2^{n+3} = 8 \cdot 2^n = O(2^n)$, but $4^n \ne O(2^n)$, since $4^n / 2^n = 2^n$ is unbounded. The space of k-mers, $4^k = 2^{2k}$, is not $O(2^k)$.
- **Bases of logarithms.** $\log_a n = \log_b n / \log_b a$, so all logarithms are $\Theta$ of each other and the base is omitted inside $O$; it matters in exponents: $n^{\log_2 3} \approx n^{1.585}$ but $n^{\log_4 3} \approx n^{0.792}$.

### Little o and little omega

$o(g) = \{ f : \forall c > 0,\ \exists n_0,\ \forall n \ge n_0,\ 0 \le f(n) < c\,g(n) \}$, and symmetrically $\omega(g)$ with $f(n) > c\,g(n)$.[^clrs3] The quantifier on $c$ changes from "there exists" to "for all": $n = o(n \log n)$ and $n \log n = o(n^2)$, but $n^2 = O(n^2)$ is not $o(n^2)$.

### Algebra of the notations

- **Transitivity**: $f = O(g)$ and $g = O(h)$ give $f = O(h)$, with constant $c_1 c_2$ and threshold $\max(n_1, n_2)$; likewise for $\Omega$, $\Theta$, $o$, $\omega$. **Reflexivity**: $f = \Theta(f)$. **Symmetry**: $f = \Theta(g) \iff g = \Theta(f)$. **Transpose symmetry**: $f = O(g) \iff g = \Omega(f)$.[^clrs3] **Sums and products** of nonnegative functions: $O(f) + O(g) = O(\max(f, g))$, $O(f) \cdot O(g) = O(fg)$.
- **Not a total order**: some pairs of functions are incomparable, neither $O$ nor $\Omega$ of each other; $n$ and $n^{1 + \sin n}$ are an example.[^clrs3]

### Sums that loops produce

- $\sum_{i=1}^{n} i = n(n+1)/2 = \Theta(n^2)$; more generally $\sum_{i=1}^{n} i^d = \Theta(n^{d+1})$ for a fixed $d \ge 0$: the sum is at most $n \cdot n^d$, and its upper half alone is at least $(n/2)(n/2)^d$.
- Harmonic sum: $\ln(n + 1) \le \sum_{i=1}^{n} 1/i \le 1 + \ln n$, by comparing the sum with $\int dx/x$, so it is $\Theta(\log n)$.[^lehman]
- Geometric sum: $\sum_{i=0}^{k} 4^i = (4^{k+1} - 1)/3 = \Theta(4^k)$. A geometric sum is dominated by its largest term: a complete search tree over k-mers has $\Theta(4^k)$ nodes, not many more than its $4^k$ leaves ([[Exhaustive Search]]).
- $\log_2 (n!) = \Theta(n \log n)$, since $(n/2)^{n/2} \le n! \le n^n$; this is the size of the comparison-sorting lower bound ([[Sorting]]).

### Several parameters, expected and amortized bounds

Bioinformatics costs usually depend on several sizes: filling an alignment matrix for sequences of lengths $n$ and $m$ costs $\Theta(nm)$ ([[Sequence Alignment]]); counting k-mers with string keys costs $\Theta(nk)$ expected time, and $\Theta(n)$ with 2-bit codes updated in $O(1)$ per window ([[Rolling Hash]]). State which sizes grow: $O(nm)$ says nothing if $m$ is assumed constant. Constant time per operation is often an **expected** bound (hashing, over the randomness of the hash function) or an **amortized** bound (appending to a dynamic array, over a sequence of operations), not a worst-case bound per operation.[^clrs] See [[Hash Table]], [[Amortized Analysis]] and [[Randomized Algorithm]].

## Advanced (L3)

- **Lower bounds on problems.** $\Omega$ about an algorithm bounds its cost; $\Omega$ about a **problem** bounds every algorithm. Any algorithm computing GC content must read every base, by an adversary argument (Exercise 5), so the linear scan is optimal up to a constant. Structure in the input changes this: searching a sorted array needs only $\Theta(\log n)$ comparisons ([[Binary Search]]), and sorting by comparisons needs $\Omega(n \log n)$ ([[Sorting]]).
- **Polynomial versus exponential.** The line between polynomial and exponential running time is the working definition of tractability ([[NP-Completeness]]). Exponential algorithms are acceptable when the exponent sits on a small parameter: median-string search costs $\Theta(4^k\, t\, n\, k)$, exponential in the motif length $k$ only ([[Exhaustive Search]], [[Parameterized Complexity]]).
- **When constants beat asymptotics.** A $\Theta(n)$ method with 1000 steps per element is slower than a $\Theta(n \log_2 n)$ method with 1 step per element as long as $\log_2 n < 1000$, that is for $n < 2^{1000}$: for every genome. Asymptotics rank methods for large inputs; [[Benchmarking]] and [[Performance Profiling]] decide for the inputs you have.
- **Empirical exponents.** On a log-log plot, $c\,n^d$ is a line of slope $d$. For $n \ln n$ the local slope is $\frac{d \ln(n \ln n)}{d \ln n} = 1 + \frac{1}{\ln n}$, about 1.09 near $n = 10^5$: a measured slope of 1.1 does not reveal a hidden $n^{1.1}$ (Exercise 4).

## Mathematical representation

- **Quantifier structure.** $O$: $\exists c\ \exists n_0\ \forall n \ge n_0$, $f(n) \le c\,g(n)$. $o$: $\forall c\ \exists n_0\ \forall n \ge n_0$, $f(n) < c\,g(n)$. Swapping the first two quantifiers is the whole difference between "bounded ratio" and "vanishing ratio".
- **Limit criteria.** If $g(n) > 0$ for large $n$ and $L = \lim_{n\to\infty} f(n)/g(n)$ exists: $0 < L < \infty$ implies $f = \Theta(g)$; $L = 0$ implies $f = o(g)$; $L = \infty$ implies $f = \omega(g)$. Proof of the first: for $n$ beyond some $n_0$, $L/2 \le f(n)/g(n) \le 2L$, so $c_1 = L/2$ and $c_2 = 2L$ work. The criteria only apply when the limit exists: $f(n) = n$ for even $n$ and $2n$ for odd $n$ is $\Theta(n)$ although $f(n)/n$ has no limit. In general $f = O(g)$ iff $\limsup f/g < \infty$, and $f \sim g$ (asymptotic equality) iff $f/g \to 1$.[^lehman]
- **Standard limits.** For constants $a > 1$, $b$ and $\varepsilon > 0$: $n^b / a^n \to 0$ and $(\log n)^b / n^\varepsilon \to 0$:[^clrs3] every polynomial is $o$ of every exponential, every power of a logarithm is $o$ of every positive power of $n$. With $a^n / n! \to 0$ and $n! / n^n \to 0$, this justifies the chain of the Core section.

## Computational representation

Two checks of an asymptotic claim: count the iterations exactly, or time a doubling sequence of inputs and read the exponent from $\log_2$ of the time ratio (Worked example). Counting:

```python
def count_pairs(n: int) -> int:
    """Iterations of: for i in range(n): for j in range(i + 1, n)."""
    ops = 0
    for i in range(n):
        for j in range(i + 1, n):
            ops += 1
    return ops


for n in (10, 100, 1000):
    f = 3 * n**2 + 10 * n + 7
    print(f"n={n:>5}  pairs={count_pairs(n):>6}  n(n-1)/2={n * (n - 1) // 2:>6}  f(n)/n^2={f / n**2:.3f}")
```

```text
n=   10  pairs=    45  n(n-1)/2=    45  f(n)/n^2=4.070
n=  100  pairs=  4950  n(n-1)/2=  4950  f(n)/n^2=3.101
n= 1000  pairs=499500  n(n-1)/2=499500  f(n)/n^2=3.010
```

The loop count matches $n(n-1)/2$ exactly, and $f(n)/n^2$ tends to the leading constant 3, as the limit criterion predicts for a $\Theta(n^2)$ function.

## Worked example

> [!example] Most frequent 9-mers, two algorithms
> **Problem.** Given a sequence of length $n$, find the most frequent k-mers ([[K-mer]]), the warm-up problem of the replication-origin chapter of Compeau and Pevzner.[^compeau]
> 1. **Naive algorithm.** For each of the $n - k + 1$ windows, count its occurrences by comparing it with all $n - k + 1$ windows, each comparison costing up to $k$ character steps: $\Theta((n - k + 1)^2 k)$, that is $\Theta(n^2 k)$ when $k \le n/2$ (then $n - k + 1 \ge n/2$).
> 2. **Hash-table algorithm.** One pass; each window is sliced and hashed in $\Theta(k)$ and its counter updated in $O(1)$ expected time: $\Theta(nk)$ expected ([[Hash Table]]).
> 3. **Measure** both on random toy sequences ($k = 9$), then extrapolate to the *E. coli* K-12 chromosome, 4,639,221 bp:[^blattner]
> ```python
> import random
> import time
> from collections import Counter
>
> def frequent_words_naive(text: str, k: int) -> tuple[set[str], int]:
>     n = len(text)
>     counts = []
>     for i in range(n - k + 1):                     # n - k + 1 patterns
>         pattern = text[i:i + k]
>         c = 0
>         for j in range(n - k + 1):                 # n - k + 1 windows
>             if text[j:j + k] == pattern:           # up to k character comparisons
>                 c += 1
>         counts.append(c)
>     best = max(counts)
>     return {text[i:i + k] for i in range(n - k + 1) if counts[i] == best}, best
> def frequent_words_dict(text: str, k: int) -> tuple[set[str], int]:
>     counts = Counter(text[i:i + k] for i in range(len(text) - k + 1))
>     best = max(counts.values())
>     return {w for w, c in counts.items() if c == best}, best
>
> random.seed(7)
> k = 9
> for n in (1000, 2000, 4000):
>     text = "".join(random.choices("ACGT", k=n))   # toy sequence
>     t0 = time.perf_counter()
>     naive = frequent_words_naive(text, k)
>     t1 = time.perf_counter()
>     fast = frequent_words_dict(text, k)
>     t2 = time.perf_counter()
>     assert naive == fast
>     print(f"n={n}  naive {t1 - t0:.2f} s  dict {1e3 * (t2 - t1):.2f} ms")
>
> N = 4_639_221                                     # E. coli K-12 genome length
> w, W = n - k + 1, N - k + 1
> print(f"E. coli: naive ~{(t1 - t0) * (W / w) ** 2 / 86400:.0f} days, dict ~{(t2 - t1) * W / w:.1f} s")
> ```
> ```text
> n=1000  naive 0.11 s  dict 0.33 ms
> n=2000  naive 0.34 s  dict 0.51 ms
> n=4000  naive 1.30 s  dict 0.91 ms
> E. coli: naive ~20 days, dict ~1.1 s
> ```
> 4. **Read the result.** Doubling $n$ multiplies the naive time by 3.1 then 3.8 (toward 4, quadratic) and the hash-table time by 1.5 then 1.8 (toward 2, linear once fixed costs fade). Both return the same answer, so the naive version stays useful as a test oracle; at bacterial-genome scale it needs weeks where the linear one needs a second. A frequency array of $4^k$ counters, the book's next step, also runs in linear time plus $\Theta(4^k)$ to initialize, a cost paid in memory ([[Space Complexity]]).

## Common misconceptions

> [!warning] "O is the worst case, Ω the best case, Θ the average case"
> The notations bound **functions**; best, worst and average case choose **which function** is bounded. [[Sorting|Insertion sort]] takes $\Theta(n^2)$ steps in the worst case (reverse-sorted input) and $\Theta(n)$ in the best case (sorted input).[^clrs2] So "insertion sort runs in $O(n^2)$" is true of every input, "its worst case is $\Theta(n^2)$" is true and tight, and "insertion sort runs in $\Theta(n^2)$" is false as a claim about all inputs.

> [!warning] "f = O(g) says how fast f grows"
> $O$ is only an upper bound: a linear scan is also $O(n^3)$. When you know the growth exactly, say $\Theta$; many texts write $O$ where they mean $\Theta$, and readers should check which is meant.

> [!warning] "Constants never matter, even in exponents"
> Constant **factors** disappear, constant **exponents and bases** do not: $4^k \ne O(2^k)$, $n^2 \ne O(n)$. Each extra base of a k-mer multiplies the candidate space by 4, which is the difference between a search that finishes and one that does not.

## Exercises

> [!question] Exercise 1 (L1)
> Order by growth rate, from slowest to fastest, and mark the functions that are $\Theta$ of each other: $100n$, $n^2$, $n \log_2 n$, $2^n$, $\sqrt{n}$, $\log_2 n$, $1.5^n$, $n!$, $1000$, $\log_{10} n$, $n^2 + 10^6 n$.

> [!success]- Solution
> Writing $\asymp$ for "$\Theta$ of each other": $1000 \prec \log_2 n \asymp \log_{10} n \prec \sqrt{n} \prec 100n \prec n \log_2 n \prec n^2 \asymp n^2 + 10^6 n \prec 1.5^n \prec 2^n \prec n!$. Logarithms in different bases differ by a constant factor; $n^2 + 10^6 n \le 2n^2$ for $n \ge 10^6$; $1.5^n / 2^n = 0.75^n \to 0$, so the two exponentials are not $\Theta$ of each other.

> [!question] Exercise 2 (L1)
> Give the worst-case running time in $\Theta$ form: (a) `for i in range(n): for j in range(i): body` with an $O(1)$ body; (b) `for i in range(n):` then `j = 1; while j < n: j *= 2`; (c) for each of $n$ reads of length $L$, `for i in range(L - k + 1): counts[read[i:i + k]] += 1`; (d) `for x in xs: if x == target: break`.

> [!success]- Solution
> (a) $\sum_{i=0}^{n-1} i = n(n-1)/2 = \Theta(n^2)$. (b) $n$ outer iterations times $\lceil \log_2 n \rceil$ inner ones: $\Theta(n \log n)$. (c) $n(L - k + 1)$ windows, each sliced and hashed in $\Theta(k)$: $\Theta(n(L - k + 1)k)$ expected. (d) The worst case is a target absent from the list: $\Theta(n)$; the best case is $\Theta(1)$.

> [!question] Exercise 3 (L2)
> Prove $5n^3 - 2n^2 + 7 = \Theta(n^3)$ with explicit $c_1$, $c_2$, $n_0$. Then prove that $n \log_2 n = O(n^2)$ but $n \log_2 n \ne \Theta(n^2)$.

> [!success]- Solution
> For $n \ge 1$: $5n^3 - 2n^2 + 7 \le 5n^3 + 7n^3 = 12n^3$, and $5n^3 - 2n^2 + 7 \ge 5n^3 - 2n^3 = 3n^3$. So $c_1 = 3$, $c_2 = 12$, $n_0 = 1$. Next, $\log_2 n \le n$ for $n \ge 1$, so $n \log_2 n \le n^2$ ($c = 1$). If $n \log_2 n \ge c\,n^2$ held for all large $n$, then $\log_2 n \ge cn$, false since $\log_2 n / n \to 0$: not $\Omega(n^2)$, hence not $\Theta(n^2)$.

> [!question] Exercise 4 (L2, Python)
> Count the comparisons that `sorted()` makes on random lists of sizes $10^4 \cdot 2^i$ (wrap the values in a class whose `__lt__` counts its calls), compute the log-log slope between consecutive sizes, and compare it with $1 + 1/\ln n$.

> [!success]- Solution
> ```python
> import math
> import random
>
> class Counted:                  # a float whose comparisons are counted
>     calls = 0
>
>     def __init__(self, v: float):
>         self.v = v
>
>     def __lt__(self, other: "Counted") -> bool:
>         Counted.calls += 1
>         return self.v < other.v
>
> random.seed(0)
> previous = None
> for n in (10_000 * 2**i for i in range(5)):
>     data = [Counted(random.random()) for _ in range(n)]
>     Counted.calls = 0
>     sorted(data)
>     c = Counted.calls
>     if previous:
>         n0, c0 = previous
>         print(f"{n0:>6} -> {n:>6}: comparisons {c0} -> {c}, slope {math.log(c / c0) / math.log(n / n0):.3f}"
>               f", 1 + 1/ln n = {1 + 1 / math.log(n0):.3f}")
>     previous = (n, c)
> ```
> ```text
>  10000 ->  20000: comparisons 119823 -> 259822, slope 1.117, 1 + 1/ln n = 1.109
>  20000 ->  40000: comparisons 259822 -> 559158, slope 1.106, 1 + 1/ln n = 1.101
>  40000 ->  80000: comparisons 559158 -> 1198555, slope 1.100, 1 + 1/ln n = 1.094
>  80000 -> 160000: comparisons 1198555 -> 2557031, slope 1.093, 1 + 1/ln n = 1.089
> ```
> The slopes track $1 + 1/\ln n$ and slowly decrease toward 1: the signature of $n \log n$, not of a power $n^{1.1}$, whose slope would stay constant. Counting operations removes the timing noise of the machine.

> [!question] Exercise 5 (L3)
> Prove that every algorithm that computes the GC content of every DNA string of length $n$ must read all $n$ positions in the worst case (an $\Omega(n)$ lower bound for the problem). Why does the same argument fail for deciding whether a value occurs in a sorted array?

> [!success]- Solution
> Adversary argument. Suppose an algorithm, on some input $s$, never reads position $i$. Build $s'$ equal to $s$ except at $i$, where an A or T is replaced by G, or a C or G by A. The algorithm reads exactly the same values on $s'$, so it behaves identically and returns the same output, but $\mathrm{GC}(s') \ne \mathrm{GC}(s)$: it is wrong on one of the two. Hence it reads all $n$ positions on every input, and the problem is $\Omega(n)$; the linear scan is optimal. For a **sorted** array, the promise of order links positions: after reading the middle element, a whole half is known to be too small or too large without reading it, so $\Theta(\log n)$ comparisons suffice ([[Binary Search]]). Changing an unread element could break the sortedness, so the adversary is not allowed to do it.

## Mastery checklist

- [ ] 1 Recognized: I can state what $O$, $\Omega$ and $\Theta$ mean and rank the common growth rates.
- [ ] 2 Understood: I can write the formal definitions with their quantifiers and explain why constant factors and small inputs are ignored, but not constant exponents.
- [ ] 3 Practiced: I can derive the worst-case $\Theta$ of nested loops, prove bounds with explicit constants or limits, and check an exponent by counting or doubling experiments.
- [ ] 4 Applied: in [[05-sequence-search]] or [[bio-algorithms]], I predicted how a real search scales, measured it, and explained the gap between prediction and timing.
- [ ] 5 Explained: I can teach lower bounds for problems (adversary arguments), the polynomial versus exponential divide, and when constants beat asymptotics.

## References

[^clrs3]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 3 "Characterizing Running Times" (O, Ω, Θ, o and ω notation; properties of the notations; standard notations and common functions).
[^clrs2]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 2 "Getting Started" (best and worst case of insertion sort).
[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed., treatment of hash tables and of amortized analysis.
[^6006]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, models and data structures part (performance measures and asymptotic analysis).
[^lehman]: [[Mathematics for Computer Science (Lehman)]], treatment of sums and asymptotics (asymptotic notation through limits, asymptotic equality, bounding sums by integrals).
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (the frequent words problem, a naive algorithm and a faster one with a frequency array).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* 376:44-53.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science*.
