---
aliases:
  - FIFO
  - Deque
  - Double-Ended Queue
  - Circular Buffer
  - File (structure de données)
tags:
  - type/concept
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Abstract Data Type]]"
  - "[[Array]]"
related:
  - "[[Stack]]"
  - "[[Graph Traversal]]"
  - "[[Minimizer]]"
projects: []
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
---

# Queue

> [!abstract]
> A queue releases items in arrival order (first in, first out), and a double-ended queue (deque) adds and removes at both ends in $O(1)$. Breadth-first search runs on the first; sliding windows over a sequence run on the second.

## Definition

A **queue** is a dynamic set in which the element removed is the one that has been in the set longest: **first in, first out (FIFO)**. **Enqueue** inserts at the tail and **dequeue** removes at the head; in an array whose occupied region wraps around the end (a **circular buffer**), both take $O(1)$ time. A **deque** (double-ended queue) allows insertion and deletion at both ends.[^clrs10] Python's `collections.deque` is a double-ended queue optimized for both ends.[^mck3]

## Why it matters

- **Breadth-first search** (BFS) explores a graph in order of distance from the source using a FIFO queue, and so finds shortest paths in unweighted graphs:[^clrs20] mutational paths between codons (below), neighborhoods in k-mer graphs ([[De Bruijn Graph]]), level-order traversal of a tree ([[Graph Traversal]]).
- **Sliding windows** along a sequence (GC content per window, lowest base quality per window, smallest k-mer per window) keep the window, or its candidate minima, in a deque ([[GC Content]], [[Phred Quality Score]], [[Minimizer]]).

## Core (L1)

In Python, `deque.append` enqueues and `deque.popleft` dequeues, both $O(1)$. Never dequeue with `list.pop(0)`: it shifts every remaining reference, so draining $n$ items costs $\Theta(n^2)$ (the [[Array]] note measures the same effect for `insert(0, x)`). A deque created with `maxlen` keeps the last items and silently drops from the opposite end, which is what a fixed window wants (first line of the code below).

**BFS on the codon graph.** Vertices: the 61 sense codons of the standard code (NCBI table 1);[^ncbi] edges: single-base substitutions between sense codons. BFS gives the fewest substitutions from one codon to another without passing through a stop codon, a toy model of mutational paths in a coding gene.

```python
from collections import deque
print(deque([40, 40, 30, 40], maxlen=3))        # deque([40, 30, 40], maxlen=3)
BASES = "TCAG"
CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]
aa = dict(zip(CODONS, "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))

def neighbors(codon):                           # sense codons one substitution away
    for i in range(3):
        for b in "ACGT":
            alt = codon[:i] + b + codon[i + 1:]
            if b != codon[i] and aa[alt] != "*":
                yield alt

def bfs(source):
    dist, prev, queue = {source: 0}, {source: None}, deque([source])
    while queue:
        u = queue.popleft()                     # oldest discovery first
        for v in neighbors(u):
            if v not in dist:                   # first discovery = shortest distance
                dist[v], prev[v] = dist[u] + 1, u
                queue.append(v)
    return dist, prev

dist, prev = bfs("TGG")                         # Trp
path, c = [], "TAT"                             # Tyr
while c is not None:
    path.append(f"{c}({aa[c]})")
    c = prev[c]
print(" <- ".join(path), [list(dist.values()).count(d) for d in range(4)])
```

```text
TAT(Y) <- TGT(C) <- TGG(W) [1, 7, 26, 27]
```

Of the two 2-step routes from TGG to TAT, the one through TAG is closed (stop codon), so BFS returns the route through TGT. All 61 sense codons are within 3 substitutions of TGG.

## Deeper (L2)

**Why BFS is correct.** At any time the queue holds vertices at distance $d$ followed by vertices at distance $d + 1$, so vertices leave in non-decreasing distance and the first discovery of a vertex comes from a shortest path. Each vertex is enqueued once and each edge examined a constant number of times: $O(V + E)$.[^clrs20]

**Sliding-window minimum.** Recomputing the minimum of each window of $w$ values costs $O(w)$. A **monotone deque** keeps only the indices that can still become a window minimum, with increasing values from front to back: a new value removes from the back every value not smaller than it (they can never be minimal again), and the front leaves when it falls out of the window. Each index is pushed once and popped at most once, so the scan costs $O(n)$ whatever $w$, while slicing grows with $w$. Quality characters below are Phred scores plus 33 ([[FASTQ Format]]).[^cock]

```python
import random, timeit

def window_min(values, w):
    """Minimum of every window values[i:i+w]; each index enters and leaves the deque once: O(n)."""
    dq, out = deque(), []                       # indices whose values increase from front to back
    for i, v in enumerate(values):
        while dq and values[dq[-1]] >= v:       # dominated: can never be a window minimum again
            dq.pop()
        dq.append(i)
        if dq[0] <= i - w:                      # the front left the window
            dq.popleft()
        if i >= w - 1:
            out.append(values[dq[0]])
    return out

qual = [ch - 33 for ch in b"II?I5IIIDI"]        # Phred+33 qualities of a toy read (invented)
print(qual, window_min(qual, 4))
rng = random.Random(0)
vals = [rng.randrange(2, 41) for _ in range(100_000)]
for w in (50, 500):                             # best of 3, CPython 3.11; indicative
    t_slice = min(timeit.repeat(lambda: [min(vals[i:i + w]) for i in range(len(vals) - w + 1)], number=1, repeat=3))
    t_deque = min(timeit.repeat(lambda: window_min(vals, w), number=1, repeat=3))
    print(w, f"slice+min {t_slice * 1e3:.0f} ms, deque {t_deque * 1e3:.0f} ms")
```

```text
[40, 40, 30, 40, 20, 40, 40, 40, 35, 40] [30, 20, 20, 20, 20, 35, 35]
50 slice+min 68 ms, deque 19 ms
500 slice+min 471 ms, deque 19 ms
```

## Advanced (L3)

- **0-1 BFS.** If edge weights are 0 or 1, push a vertex reached by a 0-edge at the front of a deque and by a 1-edge at the back: the deque stays sorted by distance and shortest paths cost $O(V + E)$. General weights need a priority queue ([[Heap]], [[Shortest Path]]). A bounded queue between pipeline stages (reader, aligner, writer) caps memory and makes a fast producer wait for a slow consumer; between threads it must also be safe for concurrent access ([[Concurrency]]).

## Mathematical representation

- A queue is a word $s \in X^*$ with $\mathrm{enqueue}(s, x) = sx$ and $\mathrm{dequeue}(xs) = (x, s)$; a deque adds $\mathrm{push\_front}(s, x) = xs$ and $\mathrm{pop\_back}(sx) = (s, x)$. BFS invariant: if the queue is $\langle v_1, \dots, v_r \rangle$, then $d(v_1) \le \dots \le d(v_r) \le d(v_1) + 1$.
- Monotone deque: its indices $i_1 < \dots < i_t$ satisfy $i_t - i_1 < w$ and $a_{i_1} < \dots < a_{i_t}$, so $a_{i_1}$ is the window minimum; $n$ pushes and at most $n$ pops make at most $2n$ deque operations.

## Worked example

> [!example] Window minimum of qualities `[40, 40, 30, 40, 20, 40, 40, 40, 35, 40]`, $w = 4$ (toy read, invented; deque as (index, value))
> | $i$ | value | popped from back | left at front | deque after | window min |
> |---:|---:|---|---|---|---:|
> | 0-2 | 40, 40, 30 | 0 then 1 | | (2, 30) | |
> | 3 | 40 | | | (2, 30) (3, 40) | 30 |
> | 4 | 20 | 3, 2 | | (4, 20) | 20 |
> | 5-7 | 40, 40, 40 | 5 then 6 | | (4, 20) (7, 40) | 20 |
> | 8 | 35 | 7 | 4 (window is 5..8) | (8, 35) | 35 |
> | 9 | 40 | | | (8, 35) (9, 40) | 35 |
>
> The 20 at index 4 stays minimal for four windows, then expires from the front; the 35 takes over at once because every larger value before it was already discarded.

## Common misconceptions

> [!warning] "BFS with a stack still finds shortest paths"
> A stack explores depth-first: the first discovery of a vertex may come through a long path. Shortest unweighted paths need FIFO order.

> [!warning] "A full `deque(maxlen=w)` refuses new items"
> It silently drops the item at the other end. That is right for a sliding window and wrong for a work queue, where it loses data.

## Exercises

> [!question] Exercise 1 (L1)
> A circular buffer of capacity 4 (array `buf`, index `head`, count `size`) receives: enqueue a, b, c; dequeue; enqueue d, e; dequeue. Give `buf`, `head` and `size` at the end.

> [!success]- Solution
> The tail slot is $(\mathrm{head} + \mathrm{size}) \bmod 4$. After a, b, c: `[a, b, c, _]`, head 0, size 3. Dequeue a: head 1, size 2. Enqueue d at 3, then e at $(1 + 3) \bmod 4 = 0$: `[e, b, c, d]`, size 4. Dequeue b: `[e, _, c, d]`, head 2, size 3.

> [!question] Exercise 2 (L2, Python)
> Check, for every ordered pair of sense codons, whether the BFS distance through sense codons equals the Hamming distance. Can stop codons lengthen a shortest mutational path in this model?

> [!success]- Solution
> ```python
> sense = [c for c in CODONS if aa[c] != "*"]
> worse = 0
> for s in sense:
>     d, _ = bfs(s)
>     worse += sum(d[t] != sum(x != y for x, y in zip(s, t)) for t in sense)
> print(len(sense), worse)
> # 61 0
> ```
> Never in the standard code. For sense codons differing at two positions, the two intermediates differ from each other at both positions; the only stop codons differing at two positions are TAG and TGA, and making both intermediates stops forces an endpoint to be TAA, itself a stop. For three positions, the computation shows that the six shortest routes are never all blocked.

> [!question] Exercise 3 (L3)
> Adapt `window_min` to select, in each window of $w$ consecutive k-mers of a sequence, the start of the smallest k-mer, reporting each selected position once. What changes, and why does the result still take $O(n)$ deque operations?

> [!success]- Solution
> The values become the k-mers (or their integer codes or hashes); ties are broken toward the leftmost occurrence by popping only strictly larger values; and a position is appended to the output only if it differs from the last one reported, since consecutive windows often share their minimum. Each k-mer index is still pushed once and popped at most once. This selection is the core of [[Minimizer]] sampling.

## Mastery checklist

- [ ] 1 Recognized: I can define FIFO and a deque, and say why `list.pop(0)` is the wrong dequeue.
- [ ] 2 Understood: I can explain the circular buffer, the BFS invariant and the monotone-deque invariant.
- [ ] 3 Practiced: I can implement BFS with parent pointers and an $O(n)$ sliding-window minimum, and prove its cost.
- [ ] 4 Applied: I computed window statistics (quality, GC content) along real reads or a real genome in linear time.
- [ ] 5 Explained: I can teach FIFO versus LIFO exploration, 0-1 BFS, and when a queue becomes a priority queue.

## References

[^clrs10]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 10 "Elementary Data Structures": queues in an array with wrap-around, deques.
[^clrs20]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 20 "Elementary Graph Algorithms": breadth-first search with a FIFO queue, shortest-path distances, $O(V + E)$ running time.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": `collections.deque` for insertion at both ends.
[^ncbi]: [[NCBI Genetic Codes]]: the standard code (translation table 1) in the TCAG codon order.
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research*: Phred qualities encoded as ASCII with an offset of 33.
