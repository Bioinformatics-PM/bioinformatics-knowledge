---
aliases:
  - Amortized Cost
  - Aggregate Method
  - Accounting Method
  - Potential Method
  - Analyse amortie
tags:
  - type/concept
  - domain/computer-science
  - domain/mathematics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Big O Notation]]"
  - "[[Array]]"
  - "[[Stack]]"
  - "[[Summation Notation]]"
  - "[[Loop Invariant]]"
related:
  - "[[Disjoint-Set Data Structure]]"
  - "[[Hash Table]]"
  - "[[Queue]]"
  - "[[Minimizer]]"
  - "[[Longest Common Prefix Array]]"
  - "[[Minimum Spanning Tree]]"
  - "[[Randomized Algorithm]]"
  - "[[Master Theorem]]"
projects:
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.046J - Design and Analysis of Algorithms]]"
  - "[[Roberts 2004 - Reducing Storage Requirements for Biological Sequence Comparison]]"
---

# Amortized Analysis

> [!abstract]
> Amortized analysis bounds the total cost of any sequence of operations on a data structure, so that rare expensive operations are paid for by the many cheap ones around them; it is a worst-case guarantee on sequences, not an average over random inputs.

## Definition

Let a data structure undergo operations $o_1, \dots, o_n$ with actual costs $c_1, \dots, c_n$. Numbers $\hat c_1, \dots, \hat c_n$ are **amortized costs** if every sequence satisfies $\sum_{i=1}^{t} c_i \le \sum_{i=1}^{t} \hat c_i$ for every prefix length $t$: the amortized total is an upper bound on the actual total at every moment. No probability is involved.[^clrs16] Three methods establish such bounds:[^clrs16][^6046-l5]

- **Aggregate**: bound the total cost $T(n)$ of $n$ operations directly; each operation is charged $T(n)/n$.
- **Accounting**: charge each operation a fixed price; the surplus is stored as **credit** on specific objects of the structure and pays for later work; credit may never become negative.
- **Potential**: define a function $\Phi$ of the structure's state with $\Phi(D_i) \ge \Phi(D_0)$ for all $i$, and set $\hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$.

## Why it matters

- **Growing containers.** `list.append` is $O(1)$ only amortized: a resize copies everything ([[Array#Deeper (L2)]] has the aggregate and potential proofs), and hash tables resize the same way ([[Hash Table]]). Building a list of $10^8$ k-mer codes or a k-mer count dictionary is linear in total despite its $\Theta(n)$ resizes.
- **Union-find.** With union by rank and path compression, connected components and single-linkage clusters cost almost $O(1)$ per operation, amortized ([[Disjoint-Set Data Structure]], [[Minimum Spanning Tree]]): grouping reads that share k-mers is one use (below).
- **Minimizer sketches.** A minimizer is the smallest k-mer of a window of $w$ consecutive k-mers;[^roberts] a monotone deque computes the minimum of every window in $O(1)$ amortized time per window, $O(n)$ for a whole genome (Advanced, [[Minimizer]]).
- **Linear-time string algorithms**, such as the construction of the LCP array of a suffix array, are proved linear by potential arguments (Exercise 5, [[Longest Common Prefix Array]]).
- **Latency is a different question.** An amortized bound says nothing about one operation: an interactive tool or a streaming pipeline with deadlines still meets the occasional $\Theta(n)$ resize or slow find (measured below).

## Core (L2)

### Aggregate method

**Binary counter.** A $k$-bit counter starts at 0; INCREMENT resets the trailing 1s to 0 and sets the next 0 to 1. One increment can flip all $k$ bits (`0111…1` → `1000…0`). But over $n$ increments, bit $j$ flips once every $2^j$ increments, $\lfloor n/2^j \rfloor$ times, so the total is less than $\sum_{j \ge 0} n/2^j = 2n$: amortized cost below 2 per increment.[^clrs16] Exactly, it is $2n$ minus the number of 1 bits of $n$, which the code below checks for every $n \le 4096$.

**Multipop stack.** PUSH and POP cost 1; MULTIPOP($j$) pops $\min(j, \text{size})$ items. One multipop can cost $n$, but each item is popped at most once after being pushed, so any $n$ operations cost at most $2 \times (\text{number of pushes}) \le 2n$.[^clrs16]

![[binary-counter-amortized-cost.svg]]

### Accounting method

**Counter.** Charge 2 per increment: 1 pays for setting a bit to 1, the other is left on that bit as credit. Resetting a 1 to 0 is paid by the credit it carries. **Invariant**: every 1 bit holds one credit, so the credit is never negative and $n$ increments cost at most $2n$.

**Dynamic array with doubling.** Charge 3 per append: 1 writes the element, 1 is saved on it for its own copy at the next resize, 1 is saved on an element of the older half, which already spent its credit at the previous resize. Just after a resize from capacity $m/2$ to $m$, no credit remains; the next $m/2$ appends deposit $2 \cdot m/2 = m$ credits, exactly the cost of copying $m$ elements at the following resize. The [[Array]] note proves the same bound by the aggregate and potential methods.

### Potential method

**Counter.** Let $\Phi$ be the number of 1 bits. An increment that resets $t$ bits costs $c = t + 1$ and changes $\Phi$ by $1 - t$, so $\hat c = (t + 1) + (1 - t) = 2$. Since $\Phi(D_0) = 0 \le \Phi(D_i)$, $n$ increments cost at most $2n$.

| Method | What you write down | Best when |
|---|---|---|
| Aggregate | one sum over the whole sequence | all operations are of one kind |
| Accounting | a price per operation and where its credit is stored | credit attaches naturally to objects (bits, elements) |
| Potential | one function of the state | several operation types interact; the standard for proofs |

## Advanced (L3)

### Sliding-window minima and minimizers

Roberts et al. reduce the storage of seed catalogues by keeping only **minimizers**: for each window of $w$ consecutive k-mers, the smallest k-mer under a fixed order.[^roberts] Two sequences that share a whole window share its minimizer, whatever surrounds it. Computing every window's minimum naively costs $\Theta(w)$ per window. A **monotone deque** of positions does better: before appending position $i$, pop from the back every position whose key exceeds key $i$ (it can never again be a window minimum, since $i$ is smaller and leaves later); pop the front when it falls out of the window; the front is then the minimum (leftmost on ties). One push may trigger many pops, but each position is pushed once and popped at most once, so $N$ k-mers cost at most $2N$ deque operations: $O(1)$ amortized per window (aggregate method; with the potential $\Phi = $ deque length, each step costs at most 2). Random orders, which spread the selected positions evenly, are analyzed in [[Randomized Algorithm]].

### Union-find

A [[Disjoint-Set Data Structure]] keeps each set as a tree with its representative at the root. **Union by rank** hangs the root of smaller rank below the other and increments a rank only when two roots of equal rank are joined. By induction, a root of rank $r$ has at least $2^r$ nodes (two rank-$r$ trees make one of rank $r + 1$ with at least $2^{r+1}$ nodes), so ranks, and tree heights, are at most $\lfloor \lg n \rfloor$: FIND is $O(\log n)$ in the worst case. Adding **path compression** (every node on a find path is re-attached to the root) gives a total of $O(m\,\alpha(n))$ for $m$ operations on $n$ elements, where $\alpha$ is the inverse Ackermann function, at most 4 for any practical $n$.[^clrs19][^6046-l5] The guarantee is amortized: with compression but no ranks, one find on a long chain still costs thousands of steps (measured below).

### What amortization does not survive

- **Oscillation at a boundary.** Alternating increment and decrement on a counter at `0111…1` costs $k$ flips every time (Exercise 3); halving an array as soon as it is half empty thrashes the same way ([[Array]]).
- **Reuse of old states.** With undo, backtracking or persistent versions, the same expensive operation can be replayed from one state many times, while its credit was saved only once.
- **Deadlines.** Amortized $O(1)$ is about throughput. Spreading a resize over later operations (copying a few old elements at each append into a new array allocated early) restores a worst-case $O(1)$ bound at the price of more complex code.

## Mathematical representation

- States $D_0, D_1, \dots, D_n$; operation $i$ turns $D_{i-1}$ into $D_i$ at actual cost $c_i \ge 0$.
- **Potential**: $\Phi : \text{states} \to \mathbb{R}$ with $\Phi(D_i) \ge \Phi(D_0)$ for all $i$; amortized cost $\hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$.
- **Telescoping**: $\sum_{i=1}^{n} \hat c_i = \sum_{i=1}^{n} c_i + \Phi(D_n) - \Phi(D_0)$, hence $\sum_{i=1}^{n} c_i \le \sum_{i=1}^{n} \hat c_i$ ([[Summation Notation]]). The same holds for every prefix, which is why $\Phi(D_i) \ge \Phi(D_0)$ is required for all $i$, not only at the end.
- **Accounting as potential**: the total stored credit is a potential; "credit never negative" is $\Phi(D_i) \ge \Phi(D_0) = 0$.

## Computational representation

Instrumented structures: the binary counter, sliding-window minima with minimizers, and union-find with and without its two heuristics.

```python
import random
from collections import deque

class BinaryCounter:
    """k-bit counter; the cost of an increment is the number of bits it flips."""
    def __init__(self, k: int):
        self.bits, self.cost = [0] * k, 0      # bits[0] is the least significant bit
    def increment(self) -> int:
        i = 0
        while i < len(self.bits) and self.bits[i] == 1:
            self.bits[i] = 0                   # carry: reset a 1 (paid by its stored credit)
            i += 1
        if i < len(self.bits):
            self.bits[i] = 1                   # set one 0 to 1
        flips = i + (i < len(self.bits))
        self.cost += flips
        return flips

counter = BinaryCounter(16)
print("costs of increments 1..16:", [counter.increment() for _ in range(16)])
counter = BinaryCounter(16)
for n in range(1, 4097):                       # aggregate bound: 2n - (number of 1 bits of n)
    counter.increment()
    assert counter.cost == 2 * n - bin(n).count("1") < 2 * n

def window_minima(keys: list, w: int) -> tuple:
    """Index of the minimum (leftmost on ties) of every window of w consecutive keys,
    with a monotone deque; also returns the number of deque operations."""
    dq, picked, ops = deque(), [], 0
    for i, key in enumerate(keys):
        while dq and keys[dq[-1]] > key:       # dominated: can never be a minimum again
            dq.pop(); ops += 1
        dq.append(i); ops += 1
        if dq[0] <= i - w:                     # the front has left the window
            dq.popleft(); ops += 1
        if i >= w - 1:
            picked.append(dq[0])
    return picked, ops

def minimizers(seq: str, k: int, w: int) -> list:
    """Start positions of the (w, k)-minimizers, lexicographic order."""
    picked, _ = window_minima([seq[i:i + k] for i in range(len(seq) - k + 1)], w)
    return sorted(set(picked))

rng = random.Random(5)
for _ in range(300):                           # oracle: brute-force minimum of each window
    keys = [rng.randrange(6) for _ in range(rng.randint(1, 120))]
    w = rng.randint(1, len(keys))
    picked, ops = window_minima(keys, w)
    assert picked == [min(range(j, j + w), key=lambda i: (keys[i], i)) for j in range(len(keys) - w + 1)]
    assert ops <= 2 * len(keys)
print(window_minima([5, 3, 4, 1, 2, 6, 7, 8], 3))   # the worked example
read = "ATGCGATACGCTTGAGGCTAACGTTAGC"           # invented toy read
print([read[i:i + 3] for i in minimizers(read, k=3, w=4)])

class UnionFind:
    def __init__(self, n: int, by_rank: bool = True, compress: bool = True):
        self.parent, self.rank = list(range(n)), [0] * n
        self.by_rank, self.compress, self.steps = by_rank, compress, 0
    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:       # walk up: one step per pointer followed
            root = self.parent[root]; self.steps += 1
        while self.compress and self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]   # path compression
        return root
    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.by_rank and self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx                    # hang the lower-rank root below the other
        self.parent[ry] = rx
        if self.by_rank and self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

n = 2 ** 12
queries = [rng.randrange(n) for _ in range(n)]
for by_rank, compress in [(False, False), (True, False), (False, True), (True, True)]:
    uf, worst = UnionFind(n, by_rank, compress), 0
    operations = [(uf.union, (i + 1, i)) for i in range(n - 1)] + [(uf.find, (q,)) for q in queries]
    for op, args in operations:                # chain of unions, then random finds
        before = uf.steps
        op(*args)
        worst = max(worst, uf.steps - before)
    print(f"rank={by_rank!s:5} compression={compress!s:5} "
          f"mean {uf.steps / len(operations):7.2f} steps, worst operation {worst:4}")

reads = ["ACGTAC", "GTACGG", "TTTTCA", "TACGGA", "CCCCCC", "TTCATT"]   # invented reads
uf, first_read = UnionFind(len(reads)), {}
for r, s in enumerate(reads):                  # reads sharing a 4-mer go to one cluster
    for kmer in (s[i:i + 4] for i in range(len(s) - 3)):
        uf.union(r, first_read.setdefault(kmer, r))
clusters = {}
for r, s in enumerate(reads):
    clusters.setdefault(uf.find(r), []).append(s)
print(list(clusters.values()))
```

```text
costs of increments 1..16: [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5]
([1, 3, 3, 3, 4, 5], 13)
['ATG', 'CGA', 'ATA', 'ACG', 'CGC', 'CTT', 'AGG', 'CTA', 'AAC', 'ACG', 'CGT', 'AGC']
rank=False compression=False mean 1006.40 steps, worst operation 4095
rank=True  compression=False mean    1.00 steps, worst operation    1
rank=False compression=True  mean    1.00 steps, worst operation 1451
rank=True  compression=True  mean    1.00 steps, worst operation    1
[['ACGTAC', 'GTACGG', 'TACGGA'], ['TTTTCA', 'TTCATT'], ['CCCCCC']]
```

Reading the results:

- **Counter**: single increments cost up to 5 flips in the first 16, yet the total never reaches $2n$ (asserted for $n \le 4096$).
- **Minimizers**: 12 of the 26 3-mers of the toy read are selected with $w = 4$; the deque never exceeded $2N$ operations in 300 random tests.
- **Union-find**: the unions build a chain, adversarial for naive linking, whose finds then average about 1,000 steps. Each heuristic alone brings the mean to about 1 step per operation, but compression alone still pays 1,451 steps for one find: an amortized guarantee, not a worst-case one. Union by rank keeps every operation short.
- **Clusters**: single linkage is transitive: ACGTAC and TACGGA share no 4-mer but are joined through GTACGG.

## Worked example

> [!example] The monotone deque on keys `5 3 4 1 2 6 7 8` (invented), window $w = 3$
> ```text
> i  key  pops from back   deque after push   front out?   window minimum (index: key)
> 0   5         -          [0]                    -          -
> 1   3       0 (5)        [1]                    -          -
> 2   4         -          [1, 2]                 no         1: 3
> 3   1     2 (4), 1 (3)   [3]                    no         3: 1
> 4   2         -          [3, 4]                 no         3: 1
> 5   6         -          [3, 4, 5]              no         3: 1
> 6   7         -          [3, 4, 5, 6]           3 leaves   4: 2
> 7   8         -          [4, 5, 6, 7]           4 leaves   5: 6
> ```
> 1. **Invariant**: the keys in the deque increase from front to back, and the front is the minimum of the current window.
> 2. **Expensive step**: at $i = 3$ two pops precede the push, but the popped positions 1 and 2 will never be popped again.
> 3. **Count**: 8 pushes, 3 pops from the back, 2 from the front: 13 operations for 8 keys, below $2 \times 8 = 16$, as the code output `([1, 3, 3, 3, 4, 5], 13)` shows.

## Common misconceptions

> [!warning] "Amortized $O(1)$ means every operation is $O(1)$"
> Only the total is bounded. One append can copy the whole array, one find can walk 1,451 pointers. When single-operation latency matters, amortized bounds are the wrong guarantee.

> [!warning] "Amortized cost is the average-case cost"
> Average-case analysis averages over a distribution of inputs; amortized analysis bounds the worst sequence, with no probability at all. A binary counter costs less than $2n$ for every sequence of $n$ increments.

> [!warning] "Any potential function works"
> $\Phi$ must satisfy $\Phi(D_i) \ge \Phi(D_0)$ at every step. A potential that can dip below its starting value lets the "amortized" total underestimate a prefix of the real cost.

> [!warning] "The bound survives any mix of operations"
> It holds for the operations it was proved for. Adding DECREMENT to the counter, or MULTIPUSH to the stack, breaks it (Exercises 1 and 3).

## Exercises

> [!question] Exercise 1 (L2)
> Prove the multipop-stack bound with the potential $\Phi = $ stack size. Then add MULTIPUSH($j$), which pushes $j$ items at cost $j$: show that $n$ operations can now cost $\Theta(n^2)$.

> [!success]- Solution
> $\Phi(D_0) = 0 \le \Phi(D_i)$. PUSH: $\hat c = 1 + 1 = 2$; POP: $\hat c = 1 - 1 = 0$; MULTIPOP of $j' = \min(j, s)$ items: $\hat c = j' - j' = 0$. So $n$ operations cost at most $2n$. With MULTIPUSH, alternate MULTIPUSH($n$) and MULTIPOP($n$): each costs $n$, so $n$ operations cost $\Theta(n^2)$. A multipush can create up to $n$ items' worth of potential, so it would need an amortized price of $2j$, not a constant.

> [!question] Exercise 2 (L2)
> A queue is built from two stacks: ENQUEUE pushes on `inbox`; DEQUEUE pops from `outbox`, first moving every item of `inbox` onto `outbox` (one pop and one push each) when `outbox` is empty. With $\Phi = 2\,|\texttt{inbox}|$, find the amortized costs, and check that the order is first in, first out.

> [!success]- Solution
> ENQUEUE: $c = 1$, $\Delta\Phi = 2$, $\hat c = 3$. DEQUEUE without transfer: $c = 1$, $\Delta\Phi = 0$, $\hat c = 1$. DEQUEUE with a transfer of $t$ items: $c = 2t + 1$, $\Delta\Phi = -2t$, $\hat c = 1$. $\Phi \ge 0 = \Phi(D_0)$, so any sequence costs at most $3 \times \text{enqueues} + \text{dequeues}$. Order: the transfer reverses `inbox`, so its oldest item ends on top of `outbox`, and `outbox` is emptied before the next transfer: items leave in arrival order. This is a [[Queue]] with $O(1)$ amortized operations from two [[Stack|stacks]].

> [!question] Exercise 3 (L2)
> Add DECREMENT to the $k$-bit counter. Exhibit a sequence of $n$ operations costing $\Theta(nk)$, and say which property used by the potential argument fails.

> [!success]- Solution
> Bring the counter to `0111…1` ($2^{k-1} - 1$), then alternate INCREMENT (`1000…0`, $k$ flips) and DECREMENT (back to `0111…1`, $k$ flips): $n$ operations cost $nk$. With $\Phi$ = number of 1 bits, DECREMENT from `1000…0` costs $k$ and raises $\Phi$ by $k - 2$: its amortized cost is $2k - 2$, not a constant. Each operation undoes the credit the previous one deposited, an oscillation at a boundary.

> [!question] Exercise 4 (L3)
> Prove that the monotone deque returns the leftmost minimum of each window, and that $N$ keys cost at most $2N$ deque operations. What changes if the back-popping condition is `>=` instead of `>`?

> [!success]- Solution
> **Invariant** after step $i$: the deque holds, in increasing order of position, exactly the positions $j$ of the current window $[i - w + 1, i]$ that have no later position $j' \le i$ with a strictly smaller key. Hence the keys along the deque are non-decreasing, the front is a minimum of the window, and among equal minima it is the leftmost, because an equal later key does not remove an earlier one. **Maintenance**: pushing $i$ pops exactly the positions with a key larger than key $i$, which sit together at the back since the keys are non-decreasing; the only position that can leave the window, $i - w$, is the smallest one, hence at the front. A popped position is never needed again: every later window that contains it also contains the strictly smaller key $i$. **Cost**: each position is pushed once and popped at most once (from the back or from the front), so pops $\le$ pushes $= N$: at most $2N$ operations. With `>=`, equal keys are popped too and the front becomes the **rightmost** minimum: a different tie rule, which changes the k-mer selected inside runs of equal k-mers, but not the cost.

> [!question] Exercise 5 (L3, Python)
> The LCP array of a suffix array stores, for each suffix, the longest common prefix with its predecessor in sorted order ([[Longest Common Prefix Array]]). Process the suffixes in **text** order, starting each scan from $h - 1$ matched letters, where $h$ is the previous result. Prove that this makes at most $2n + 1$ letter comparisons, and check it.

> [!success]- Solution
> **Lemma**: if suffix $i - 1$ shares $H \ge 1$ letters with its predecessor $p$ in sorted order, then suffix $p + 1$ sorts before suffix $i$ and shares $H - 1$ letters with it, so the predecessor of suffix $i$ shares at least $H - 1$ letters with it. **Potential argument**: let $H_i$ be the value found for suffix $i$ (0 for the smallest suffix). Step $i$ starts from at least $H_{i-1} - 1$ matched letters and makes (letters matched) $+ 1$ comparisons, at most $H_i - H_{i-1} + 2$. Summing over $i$, the $H$ terms telescope: at most $2n + H_{n-1} \le 2n + 1$, since the last suffix has one letter. The matched-prefix length $h$ acts as the potential: it can drop by only 1 per step, so it cannot rise more than about $2n$ times in total.
> ```python
> def lcp_array(s: str, sa: list) -> tuple:
>     """lcp[j] = longest common prefix of suffixes sa[j-1] and sa[j], and the letter comparisons."""
>     n, rank = len(s), [0] * len(s)
>     for j, i in enumerate(sa):
>         rank[i] = j
>     lcp, h, comparisons = [0] * n, 0, 0
>     for i in range(n):                          # suffixes in text order, not in sa order
>         if rank[i] > 0:
>             p = sa[rank[i] - 1]                 # the suffix just before s[i:] in sorted order
>             while i + h < n and p + h < n and s[i + h] == s[p + h]:
>                 h += 1; comparisons += 1
>             lcp[rank[i]] = h
>             comparisons += 1                    # the mismatch (or end) that stopped the scan
>             h = max(h - 1, 0)                   # the next suffix keeps at least h - 1 matches
>         else:
>             h = 0
>     return lcp, comparisons
>
> for _ in range(200):
>     s = "".join(rng.choices("AC", k=rng.randint(1, 60)))
>     sa = sorted(range(len(s)), key=lambda i: s[i:])
>     lcp, comparisons = lcp_array(s, sa)
>     for j in range(1, len(s)):
>         a, b = s[sa[j - 1]:], s[sa[j]:]
>         assert lcp[j] == next((t for t in range(min(len(a), len(b))) if a[t] != b[t]), min(len(a), len(b)))
>     assert comparisons <= 2 * len(s) + 1
> s = "A" * 500 + "".join(rng.choices("ACGT", k=500))
> print(lcp_array(s, sorted(range(len(s)), key=lambda i: s[i:]))[1], len(s))
> ```
> Output: `1995 1000`. A run of 500 A's has suffixes sharing up to 499 letters with their neighbors, yet the total stays below $2n$: computing each LCP independently would cost $\Theta(n^2)$ comparisons on this input.

## Mastery checklist

- [ ] 1 Recognized: I can state what an amortized bound guarantees, and what it does not (single-operation latency, probabilities).
- [ ] 2 Understood: I can explain the aggregate, accounting and potential methods on the binary counter and the multipop stack.
- [ ] 3 Practiced: I can choose a potential function, check $\Phi(D_i) \ge \Phi(D_0)$, and instrument a structure to count its actual costs.
- [ ] 4 Applied: in [[bio-algorithms]], I compute minimizers with a monotone deque and cluster sequences with union-find, and measure the operations against the proven bounds.
- [ ] 5 Explained: I can teach why union by rank and path compression give near-constant amortized finds, and when amortization breaks (oscillation, persistence, deadlines).

## References

[^clrs16]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 16 "Amortized Analysis" (aggregate, accounting and potential methods; stack operations, binary counter, dynamic tables).
[^clrs19]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 19 "Data Structures for Disjoint Sets" (union by rank, path compression, the $O(m\,\alpha(n))$ bound and the inverse Ackermann function).
[^6046-l5]: [[MIT 6.046J - Design and Analysis of Algorithms]], Spring 2015, lecture 5 "Amortization: Amortized Analysis", and its recitation on union-find.
[^roberts]: [[Roberts 2004 - Reducing Storage Requirements for Biological Sequence Comparison]], *Bioinformatics* 20(18):3363-3369.
