---
aliases:
  - Recursive Function
  - Recursive Algorithm
  - Call Stack
  - Récursivité
tags:
  - type/concept
  - domain/computer-science
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Python Programming]]"
  - "[[Mathematical Induction]]"
  - "[[Recurrence Relation]]"
  - "[[Stack]]"
related:
  - "[[Divide and Conquer]]"
  - "[[Dynamic Programming]]"
  - "[[Master Theorem]]"
  - "[[Exhaustive Search]]"
  - "[[Space Complexity]]"
  - "[[Graph Traversal]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[08-phylogenetic-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
---

# Recursion

> [!abstract]
> A recursive function solves a problem by calling itself on smaller instances until it reaches a base case answered directly; its correctness is proved by induction, its running time by a recurrence, and its memory by the depth of the call stack.

## Definition

A **recursive** algorithm solves an instance by solving one or more smaller instances of the same problem and combining their solutions.[^clrs2] It needs **base cases**, solved directly, and **recursive cases** whose calls get closer to a base case, so that every chain of calls ends. Recursive procedures mirror recursive definitions of data (strings, lists, trees): a function written case by case on the definition is proved correct by induction on that structure.[^lehman] At run time, each pending call keeps a **frame** (its local variables and the place to return to) on the call stack, so memory grows with the depth of the recursion.[^clrs-stack]

## Why it matters

- **Trees are recursive.** A rooted [[Phylogenetic Tree]] is a leaf or a node with subtrees; [[Newick Format]] spells that definition with nested parentheses, and computations from the leaves to the root ([[Fitch Algorithm]], [[Felsenstein Pruning Algorithm]]) are recursions over it ([[08-phylogenetic-engine]]).
- **Dynamic programming starts as a recursion.** MIT 6.006 designs dynamic programs with SRTBOT: define Subproblems, Relate them recursively, find a Topological order, give Base cases, solve the Original problem, analyze the Time.[^6006-l15] Alignment is the canonical case (Deeper; [[Edit Distance]], [[04-alignment-engine]]).
- **Enumeration.** All k-mers, or all strings within $d$ mismatches of a pattern, are generated recursively; Compeau and Pevzner build the $d$-neighborhood of a k-mer from the neighborhood of its suffix[^compeau] ([[Exhaustive Search]], [[Approximate Pattern Matching]]).
- **The genome-scale pitfall.** In a naive recursion over a sequence, depth equals length. CPython stops at a depth of about 1000 (measured below), so a recursive scan of a gene, or a recursive walk along a long path of an assembly graph, fails where a loop succeeds.

## Core (L1)

### Base case, recursive case, call stack

```python
def all_kmers(k: int) -> list[str]:
    """All 4^k strings of length k over ACGT, in lexicographic order."""
    if k == 0:                                   # base case: the empty word
        return [""]
    shorter = all_kmers(k - 1)                   # recursive case: a smaller instance
    return [base + w for base in "ACGT" for w in shorter]

def gc(s: str, i: int = 0, depth: int = 0) -> int:
    """GC count of s[i:], printing each call and each return."""
    print("  " * depth + f"gc(i={i})")
    result = 0 if i == len(s) else (s[i] in "GC") + gc(s, i + 1, depth + 1)
    print("  " * depth + f"-> {result}")
    return result

print(len(all_kmers(3)), all_kmers(2)[:6])
gc("GCA")
```

```text
64 ['AA', 'AC', 'AG', 'AT', 'CA', 'CC']
gc(i=0)
  gc(i=1)
    gc(i=2)
      gc(i=3)
      -> 0
    -> 0
  -> 1
-> 2
```

**Correctness by induction on $k$.** Base: for $k = 0$ the only string is the empty word. Step: assume `all_kmers(k - 1)` returns the $4^{k-1}$ strings of length $k - 1$ in lexicographic order. Every string of length $k$ is uniquely a first base followed by a string of length $k - 1$; listing the first bases in the order A, C, G, T, each followed by the sorted shorter strings, gives all $4 \cdot 4^{k-1} = 4^k$ strings in lexicographic order. **Termination**: $k$ decreases by 1 at each call and stops at 0, the recursive analogue of a loop variant ([[Loop Invariant]]).

**The call stack.** In the trace, calls go down until the base case and returns come back in reverse order, last called first finished: a [[Stack]]. At the deepest point 4 frames are alive for 3 bases; a sequence of length $n$ needs $n + 1$ frames.

### Python's limit, and when to rewrite iteratively

CPython refuses to go deeper than `sys.getrecursionlimit()`, and a tail-recursive version (the recursive call as the very last action, with an accumulator) fails just the same:

```python
import sys

def gc_rec(s: str, i: int = 0) -> int:
    return 0 if i == len(s) else (s[i] in "GC") + gc_rec(s, i + 1)

def gc_tail(s: str, i: int = 0, acc: int = 0) -> int:
    return acc if i == len(s) else gc_tail(s, i + 1, acc + (s[i] in "GC"))

print(sys.getrecursionlimit())
for f in (gc_rec, gc_tail):
    try:
        f("ACGT" * 500)                          # 2,000 bases: depth 2,001
    except RecursionError as err:
        print(f.__name__, "RecursionError:", err)
```

```text
1000
gc_rec RecursionError: maximum recursion depth exceeded
gc_tail RecursionError: maximum recursion depth exceeded
```

- **Depth grows with the data** (scanning a sequence, following a path): write a loop. `sys.setrecursionlimit` only moves the wall, and every frame costs memory ([[Space Complexity]]).
- **Depth is logarithmic** ([[Binary Search]], balanced [[Divide and Conquer|divide and conquer]]): keep the recursion. Binary search over $3.055 \times 10^9$ sorted positions goes $\lceil \log_2 (3.055 \times 10^9) \rceil = 32$ levels deep.
- **Depth is the height of a tree or of a search path**: unbounded in the worst case (unbalanced trees, long graph paths), so use an explicit stack (Exercise 3, [[Graph Traversal]]).

## Deeper (L2)

### Recurrences and recursion trees

The running time of a recursive algorithm satisfies a [[Recurrence Relation]]: the cost of its recursive calls plus the work done at its own level. The **recursion-tree method** draws one node per call, labeled with that work, and sums the tree level by level (Worked example).[^clrs4]

| Recurrence | Pattern | Solution |
|---|---|---|
| $T(n) = T(n-1) + c$ | one smaller call (recursive GC count) | $\Theta(n)$ |
| $T(n) = T(n/2) + c$ | one half (binary search) | $\Theta(\log n)$ |
| $T(n) = 2T(n/2) + cn$ | two halves and a linear merge (merge sort) | $\Theta(n \log n)$ |
| $T(n) = 2T(n-1) + c$ | two calls on almost the same size | $\Theta(2^n)$ |

Divide-and-conquer recurrences in general are solved by the [[Master Theorem]]; `all_kmers` costs $\sum_{j=1}^{k} \Theta(j\,4^j) = \Theta(k\,4^k)$, the size of its output.

### Overlapping subproblems and memoization

Edit distance has a natural recursion on suffixes: $d(i, j)$, the distance between `a[i:]` and `b[j:]`, is the minimum of a deletion, an insertion, and a match or substitution, each followed by a smaller instance. The three calls overlap: $d(1, 1)$ is reached from $d(0, 0)$, $d(1, 0)$ and $d(0, 1)$. Caching each result (memoization) evaluates every pair once:

```python
from functools import lru_cache

def edit_calls(a: str, b: str, memo: bool) -> tuple[int, int]:
    """Edit distance of a and b by recursion on suffixes, and the number of evaluated calls."""
    calls = 0
    def d(i: int, j: int) -> int:                # distance between a[i:] and b[j:]
        nonlocal calls
        calls += 1
        if i == len(a) or j == len(b):           # one suffix is empty: insert the rest
            return (len(a) - i) + (len(b) - j)
        return min(d(i + 1, j) + 1, d(i, j + 1) + 1, d(i + 1, j + 1) + (a[i] != b[j]))
    if memo:
        d = lru_cache(maxsize=None)(d)           # each (i, j) is evaluated once
    return d(0, 0), calls

for a, b in [("GATT", "GCAT"), ("GATTACA", "GCATGCT"), ("GATTACAGA", "GCATGCTGA")]:
    print(len(a), edit_calls(a, b, memo=False), edit_calls(a, b, memo=True))
```

```text
4 (2, 481) (2, 25)
7 (4, 72958) (4, 64)
9 (4, 2193844) (4, 100)
```

Without the cache the number of calls explodes (2,193,844 for two 9-mers); with it, exactly $(n + 1)(m + 1)$ subproblems are evaluated and the cost becomes $\Theta(nm)$. Recursion plus memoization, evaluated in a good order, is [[Dynamic Programming]];[^6006-l15] for alignment it becomes the grid of [[Needleman-Wunsch Algorithm]].

## Advanced (L3)

- **Structural recursion.** On recursively defined data (strings, lists, trees, Newick expressions) the shape of a function follows the shape of the type, and correctness follows by structural induction on it.[^lehman] A Newick parser written as recursive descent nests as deep as the tree.
- **Tail calls.** When the recursive call is the last action, its frame could be reused and the recursion is a loop in disguise; CPython does not perform this transformation (Core), so such functions are rewritten as loops by hand. The same idea bounds the stack of quicksort: recursing on the smaller part and looping on the larger keeps the depth logarithmic.[^clrs-stack]
- **Depth in graphs.** Recursive depth-first search goes as deep as the path it follows. If all k-mers of a genome are distinct, the graph linking each k-mer to the next is a single path of $n - k + 1$ nodes, so a recursive search along it needs millions of frames for a bacterial genome: assembly graphs ([[De Bruijn Graph]]) call for explicit stacks ([[Graph Traversal]]).

## Mathematical representation

- A recursive definition over $\mathbb{N}$: $f(0) = a$, $f(n) = h(n, f(n - 1))$, well defined by induction. In general a recursion terminates if a measure $\mu : \text{instances} \to \mathbb{N}$ strictly decreases from each call to its recursive calls.
- **Proof scheme** (strong induction on $\mu$): prove $P(x)$ for the base cases, and $P(x)$ for a recursive case assuming $P(y)$ for every instance $y$ with $\mu(y) < \mu(x)$.
- **Cost**: $T(x) = \sum_{y \in \mathrm{calls}(x)} T(y) + w(x)$, with $w(x)$ the work outside the calls; the recursion tree sums $w$ over its nodes. **Stack space**: $\Theta(D \cdot F)$ for a maximal depth $D$ and frame size $F$.

## Computational representation

Python implements each call with a frame object, bounded by `sys.getrecursionlimit()` (1000 by default, measured above). `functools.lru_cache` adds memoization to a recursive function in one line; a `list` used with `append` and `pop` is the explicit stack that replaces the call stack when depth can grow with the input. In files, recursion appears as nesting: the parentheses of a Newick tree are a recursive definition written out.

## Worked example

> [!example] Solving the merge sort recurrence with a recursion tree
> Merge sort splits $n$ items into two halves, sorts each recursively and merges in $cn$ steps: $T(n) = 2T(n/2) + cn$, $T(1) = c$.[^clrs2] For $n = 8$:
> ```text
> level 0                    8c                      level cost  8c
> level 1             4c            4c               level cost  8c
> level 2         2c     2c     2c     2c            level cost  8c
> level 3        c  c   c  c   c  c   c  c           level cost  8c
>                                                    total      32c
> ```
> 1. **Shape.** Each level halves the size, so there are $\log_2 n + 1$ levels (4 for $n = 8$).
> 2. **Cost per level.** Level $i$ has $2^i$ calls of size $n/2^i$, each costing $c\,n/2^i$: $cn$ per level.
> 3. **Total.** $T(n) = cn(\log_2 n + 1) = \Theta(n \log n)$; for $n = 8$, $8c \times 4 = 32c$.
> 4. **Check by substitution.** $T(n/2) = c\frac{n}{2}(\log_2 \frac{n}{2} + 1) = c\frac{n}{2}\log_2 n$, so $2T(n/2) + cn = cn\log_2 n + cn$: the formula satisfies the recurrence, which is the induction step of a proof for powers of 2.

## Common misconceptions

> [!warning] "Recursion is slower than iteration"
> A linear recursion and the equivalent loop have the same asymptotic cost; recursion adds a constant per call and a frame per level. What makes some recursions explode is recomputing overlapping subproblems (2,193,844 calls instead of 100 above), which memoization removes.

> [!warning] "Python optimizes tail recursion, or a higher limit fixes RecursionError"
> Neither: `gc_tail` fails at the same depth as `gc_rec`, and a recursion whose depth grows with the input fails again on a larger input after using $\Theta(n)$ frames of memory. Rewrite it as a loop or with an explicit stack.

## Exercises

> [!question] Exercise 1 (L1)
> Write a recursive `count(s, base)` returning the number of occurrences of `base` in `s`, with its base case and recursive case. How deep does it recurse on a 10 kb gene, and what happens in Python?

> [!success]- Solution
> Base case: the empty string contains 0 occurrences. Recursive case: `(s[0] == base) + count(s[1:], base)`. Depth: $n + 1 = 10{,}001$ frames, beyond the default limit of 1000, so `RecursionError`. It is also quadratic, since `s[1:]` copies the rest of the string at each call: pass an index instead, or better, use a loop or `s.count(base)`.

> [!question] Exercise 2 (L2)
> Solve with recursion trees: (a) $T(n) = T(n-1) + n$; (b) $T(n) = 2T(n-1) + 1$ with $T(0) = 1$; (c) $T(n) = 3T(n/2) + n$.

> [!success]- Solution
> (a) A chain of $n$ nodes with costs $n, n - 1, \dots, 1$: $n(n+1)/2 = \Theta(n^2)$ (a recursive insertion sort). (b) Level $i$ has $2^i$ nodes of cost 1, for $i = 0, \dots, n$: $2^{n+1} - 1 = \Theta(2^n)$. (c) Level $i$ has $3^i$ nodes of size $n/2^i$, total cost $(3/2)^i n$: an increasing geometric series dominated by its last level, $3^{\log_2 n} = n^{\log_2 3} \approx n^{1.585}$, so $T(n) = \Theta(n^{\log_2 3})$ ([[Master Theorem]]).

> [!question] Exercise 3 (L3, Python)
> Compute the height of a tree given as nested tuples (leaves are strings) recursively, then with an explicit stack. Test both on a caterpillar tree of 10,000 leaves, `(((L0, L1), L2), L3) ...`.

> [!success]- Solution
> ```python
> def height_rec(tree) -> int:                     # a leaf is a string, a node a tuple
>     return 0 if isinstance(tree, str) else 1 + max(height_rec(child) for child in tree)
>
> def height_iter(tree) -> int:
>     best, stack = 0, [(tree, 0)]                 # explicit stack of (node, depth)
>     while stack:
>         node, depth = stack.pop()
>         if isinstance(node, str):
>             best = max(best, depth)
>         else:
>             stack.extend((child, depth + 1) for child in node)
>     return best
>
> caterpillar = "L0"
> for i in range(1, 10_000):                       # (((L0, L1), L2), L3) ...
>     caterpillar = (caterpillar, f"L{i}")
> print(height_rec((("A", "B"), "C")), height_iter((("A", "B"), "C")), height_iter(caterpillar))
> try:
>     height_rec(caterpillar)
> except RecursionError:
>     print("height_rec(caterpillar): RecursionError")
> ```
> Output: `2 2 9999`, then `height_rec(caterpillar): RecursionError`. The explicit stack lives in ordinary memory; the recursive version needs a frame per level and the caterpillar has 9,999 levels. Unbalanced trees have exactly this shape, so tree code in [[08-phylogenetic-engine]] must not depend on the recursion limit.

## Mastery checklist

- [ ] 1 Recognized: I can identify the base case, the recursive case and the progress measure of a recursive function.
- [ ] 2 Understood: I can trace the call stack, prove a recursive function correct by induction, and explain Python's recursion limit.
- [ ] 3 Practiced: I can solve recurrences with recursion trees, memoize a recursion, and rewrite a recursion with a loop or an explicit stack.
- [ ] 4 Applied: in [[08-phylogenetic-engine]] or [[04-alignment-engine]], my tree and alignment code handles deep inputs without hitting the recursion limit.
- [ ] 5 Explained: I can teach when recursion is the right expression (trees, divide and conquer, memoized subproblems) and when its depth makes it the wrong one.

## References

[^clrs2]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 2 "Getting Started" (recursive algorithms, the divide-and-conquer method, merge sort and its recurrence).
[^clrs4]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 4 "Divide-and-Conquer" (recurrences; the recursion-tree method).
[^clrs-stack]: [[Introduction to Algorithms (Cormen)]], 4th ed., treatment of the stack depth of quicksort (stack frames, tail recursion).
[^6006-l15]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 15 "Dynamic Programming, Part 1" (the SRTBOT framework).
[^lehman]: [[Mathematics for Computer Science (Lehman)]], treatment of recursive definitions, recursive data types and structural induction.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (generating the neighborhood of a string recursively).
