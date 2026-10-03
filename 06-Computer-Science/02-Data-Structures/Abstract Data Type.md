---
aliases:
  - ADT
  - Interface (Data Structures)
  - Type abstrait de données
tags:
  - type/concept
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Python Programming]]"
  - "[[Big O Notation]]"
  - "[[Set]]"
related:
  - "[[Array]]"
  - "[[Hash Table]]"
  - "[[Heap]]"
projects:
  - "[[bio-core]]"
sources:
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Coursera Stanford - Algorithms Specialization]]"
---

# Abstract Data Type

> [!abstract]
> An abstract data type says which operations a collection supports and what they mean; a data structure says how they are carried out and at what cost. Fix the interface from the problem, then pick the implementation from the operations you call most.

## Definition

An **abstract data type (ADT)**, or **interface**, specifies a collection by the operations it supports and their meaning, independently of any representation. A **data structure** is a representation of the data together with algorithms that support those operations: it *implements* an interface, and one interface admits many implementations with different costs.[^6006-l2] Most interfaces are variants of the **dynamic set**, a set that algorithms grow, shrink and query (search, insert, delete, minimum, successor).[^clrs]

## Why it matters

- **A handful of interfaces cover most pipelines**: maps (codon → amino acid, k-mer → count), sets (k-mers seen, sample IDs), sequences (reads in file order, depth along a chromosome), priority queues (best hits so far).
- **The implementation decides feasibility.** Membership in a `list` is a linear scan; `set` and `dict` are hash tables that answer in constant time on average.[^mck3] Checking $2 \times 10^6$ reads against $10^4$ flagged IDs costs up to $2 \times 10^{10}$ comparisons with a list, about $2 \times 10^6$ lookups with a set.
- **Interfaces let code survive scale**: a k-mer counter written against an interface moves from a `dict` to a frequency array or a sketch without touching its callers. The Lab's [[bio-core]] defines such interfaces once for all projects.

## Core (L1)

| Interface | Operations | Bioinformatics use | Python |
|---|---|---|---|
| Sequence | `get_at(i)`, `set_at(i, x)`, `insert_at(i, x)`, `delete_at(i)`, iterate in order | reads in file order, per-base coverage | `list`, `collections.deque`, `array.array` |
| Set | `insert(x)`, `delete(k)`, `find(k)`; ordered sets add `find_min`, `find_next(k)` | k-mers seen, sample IDs | `set`, `frozenset` (unordered) |
| Map | (key, value) items: `put(k, v)`, `get(k)`, `delete(k)` | codon table, k-mer counts | `dict`, `collections.Counter` |
| Priority queue | `insert(x)`, `find_min`, `extract_min` | top-k hits, Dijkstra's frontier | `heapq` on a `list` |

A sequence keeps an **extrinsic** order (the position you give each item); a set keeps items by an **intrinsic** property, their key.[^6006-l2] For sequences, arrays give $O(1)$ access but $O(n)$ front insertion, linked lists the reverse, and dynamic arrays add $O(1)$ amortized appends ([[Array]], [[Linked List]]). For sets ("a" amortized, "e" expected),[^6006-l4] while a binary [[Heap]] implements only the priority queue, with `find_min` in $O(1)$ and `insert`, `extract_min` in $O(\log n)$:[^clrs]

| Set implementation | `find(k)` | insert/delete | `find_min` | `find_next(k)` |
|---|---|---|---|---|
| Unsorted array | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| Sorted array | $O(\log n)$ | $O(n)$ | $O(1)$ | $O(\log n)$ |
| [[Hash Table]] (`dict`, `set`) | $O(1)$ e | $O(1)$ a, e | $O(n)$ | $O(n)$ |
| [[Balanced Binary Search Tree]] | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |

## Deeper (L2)

**A contract includes its kind of guarantee.** A balanced search tree bounds every operation in the worst case; a dynamic array bounds a *sequence* of appends, one of which may cost $\Theta(n)$ ([[Amortized Analysis]]); a hash table bounds the *expected* cost over the random choice of hash function ([[Hash Function]]). A latency-critical loop, such as redrawing a genome-browser track, may prefer worst-case bounds at a higher average cost. **Invariants carry the costs.** Each implementation maintains a hidden invariant: sorted order (enables binary search), heap order ($O(1)$ minimum), each key in the slot its hash designates. Modifying operations must restore it, which is where their cost comes from, and correctness proofs are invariant proofs ([[Loop Invariant]]).

**Lower bounds belong to the interface plus the model.** In the comparison model, finding a key among $n$ needs $\Omega(\log n)$ comparisons, because a decision tree with at least $n + 1$ outcomes has height at least $\log_2(n+1)$; hashing escapes the bound by computing an address from the key, which the word-RAM model permits ([[Model of Computation]]).[^6006-l4]

## Advanced (L3)

- **Relaxed contracts.** A [[Bloom Filter]] answers set membership with false positives but no false negatives, in much less memory;[^stanford] a [[Count-Min Sketch]] returns counts that can only overestimate. Substituting one for a `set` or `Counter` changes the interface: downstream code must tolerate or verify the errors.
- **Compressed implementations.** Pattern matching with the Burrows-Wheeler transform answers "how often does this pattern occur in the genome?" from a transformed copy of the text and small count arrays, not from a table of substrings ([[Burrows-Wheeler Transform]], [[FM-Index]]).[^compeau]
- **The cost model moves with the memory level.** When data exceed RAM, costs are counted in block transfers and the ordered set of choice becomes the wide-node [[B-Tree]] ([[External Memory Algorithm]]).[^clrs] Immutability is part of an interface too: only hashable values (`str`, `tuple`, `frozenset`) can be keys or set elements.[^mck3]

## Mathematical representation

- **Set** over a universe $U$: state $A \subseteq U$ finite; $\mathrm{insert}(x): A \leftarrow A \cup \{x\}$, $\mathrm{delete}(x): A \leftarrow A \setminus \{x\}$, $\mathrm{find}(x) = [x \in A]$. A **map** is a partial function $f : K \rightharpoonup V$, a **sequence** a tuple $(x_0, \dots, x_{n-1})$, a **priority queue** a multiset whose $\mathrm{extract\_min}$ returns an element of minimal key.
- **Correct implementation**: representations $R$, an invariant $I \subseteq R$ and an abstraction function $\alpha : I \to$ states such that every operation maps $I$ into $I$ and $\alpha(\mathrm{op}_R(r)) = \mathrm{op}(\alpha(r))$ for all $r \in I$. **Choice**: if a workload calls operation $o$ exactly $c_o$ times, implementation $D$ costs $T_D = \sum_o c_o\, t_D(o)$; choose $\arg\min_D T_D$.

## Computational representation

Python can state an interface structurally with `typing.Protocol`: any class that has the methods satisfies it, without inheriting ([[Type Hint]]). One counting loop written against a protocol, two implementations: a hash table, and direct addressing where each k-mer, read as a base-4 number, indexes a frequency array.[^compeau]

```python
from typing import Protocol

class KmerCounter(Protocol):                    # the interface: what, not how
    def add(self, kmer: str) -> None: ...
    def count(self, kmer: str) -> int: ...

class HashCounter:                              # hash table: memory grows with distinct k-mers
    def __init__(self, k):
        self.table = {}
    def add(self, kmer):
        self.table[kmer] = self.table.get(kmer, 0) + 1
    def count(self, kmer):
        return self.table.get(kmer, 0)

DIGITS = str.maketrans("ACGT", "0123")

class ArrayCounter:                             # direct addressing: one slot per possible k-mer
    def __init__(self, k):
        self.slots = [0] * 4 ** k
    def add(self, kmer):
        self.slots[int(kmer.translate(DIGITS), 4)] += 1   # k-mer read as a base-4 number
    def count(self, kmer):
        return self.slots[int(kmer.translate(DIGITS), 4)]

def count_all(counter: KmerCounter, seq: str, k: int) -> KmerCounter:
    for i in range(len(seq) - k + 1):
        counter.add(seq[i:i + k])
    return counter

seq, k = "ATGCGATACGATGCGATGA", 3                # toy sequence (invented)
h, a = count_all(HashCounter(k), seq, k), count_all(ArrayCounter(k), seq, k)
print(h.count("GAT"), a.count("GAT"), h.count("TTT"), a.count("TTT"))
print(len(h.table), "keys stored vs", len(a.slots), "slots")
```

```text
3 3 0 0
9 keys stored vs 64 slots
```

For $k = 3$ the 64 slots are cheap; for $k = 21$ the array would need $4^{21} \approx 4.4 \times 10^{12}$ slots, so only the hash table is viable ([[K-mer]]). The caller never changes.

## Worked example

> [!example] Structures for a k-mer report (toy workload)
> Task: count the 21-mers of reads totalling $N = 10^8$ bases, report the 10 most frequent, and export the $u$ distinct k-mers in sorted order to merge with another sample.
> 1. **Operation profile**: about $N$ map updates (`get` then `put`), one top-10 query, one ordered traversal.
> 2. **Counting**: a hash map costs $O(1)$ expected per update, $O(N)$ in total. A balanced search tree would pay $O(\log u)$, about 27 steps for $u = 10^8$; a sorted array $O(u)$ per new k-mer.
> 3. **Top 10 and export**: a heap of size 10 over the $u$ entries (`heapq.nlargest`), $O(u \log 10)$, then one sort of the keys, $O(u \log u)$.
> 4. **Total**: $O(N + u \log u)$ expected, against $O(N \log u)$ for a tree that keeps the order all along. Order is needed once, at the end, so maintaining it during counting is wasted work.

## Common misconceptions

> [!warning] "A Python list is a linked list"
> It is a dynamic array.[^6006-l2] `insert(0, x)` shifts every reference after the insertion point,[^mck3] so a loop of front insertions is quadratic; use `collections.deque` ([[Queue]]).

> [!warning] "Hash tables are O(1)"
> Constant time is expected (over the hash function) and amortized (over resizes); a bad or adversarial key set degrades every operation to $\Theta(n)$.[^clrs11]

## Exercises

> [!question] Exercise 1 (L1)
> Name the interface, a Python implementation and the cost of its main operation for: (a) amino acid of a codon; (b) process reads oldest first; (c) k-mers already seen; (d) repeatedly take the best-scoring candidate alignment while new ones arrive.

> [!success]- Solution
> (a) Map, `dict`, $O(1)$ expected. (b) Queue, `collections.deque`, $O(1)$ `append` and `popleft`. (c) Set, `set`, $O(1)$ expected `in`. (d) Priority queue, `heapq`, $O(\log n)$ push and pop.

> [!question] Exercise 2 (L2, Python)
> Implement `KmerCounter` with a sorted list of keys and `bisect`; give its costs, check it against `HashCounter`, and say when a tree-like ordered structure beats a hash table.

> [!success]- Solution
> ```python
> from bisect import bisect_left
> class SortedCounter:                            # count: O(log u); add: O(u) for a new k-mer
>     def __init__(self, k):
>         self.keys, self.counts = [], []
>     def add(self, kmer):
>         i = bisect_left(self.keys, kmer)
>         if i == len(self.keys) or self.keys[i] != kmer:
>             self.keys.insert(i, kmer)
>             self.counts.insert(i, 0)
>         self.counts[i] += 1
>     def count(self, kmer):
>         i = bisect_left(self.keys, kmer)
>         return self.counts[i] if i < len(self.keys) and self.keys[i] == kmer else 0
>
> s = count_all(SortedCounter(k), seq, k)
> print(all(s.count(km) == h.count(km) for km in h.table), s.keys[:4])
> # True ['ACG', 'ATA', 'ATG', 'CGA']
> ```
> With $u$ distinct k-mers, inserting a new one shifts up to $u$ entries. Ordered structures win when ordered queries are *interleaved* with updates (a successor or prefix query after each insertion costs $O(n)$ in a hash table); then use a [[Balanced Binary Search Tree]].

> [!question] Exercise 3 (L3)
> A contamination screen replaces its `set` of contaminant k-mers by a Bloom filter and discards any read sharing a k-mer with it. What changes in the results, and what can the pipeline no longer do?

> [!success]- Solution
> No contaminated read is missed (no false negatives), but some clean reads are discarded (false positives, at a rate set by the filter's size). The stored k-mers can no longer be listed or deleted. If losing clean reads is unacceptable, use the filter as a pre-screen and confirm hits against an exact set.

## Mastery checklist

- [ ] 1 Recognized: I can name the sequence, set, map and priority queue interfaces and give one implementation of each.
- [ ] 2 Understood: I can explain interface versus data structure, and worst-case versus amortized versus expected guarantees.
- [ ] 3 Practiced: I can write code against a `Protocol` and swap implementations, predicting their costs.
- [ ] 4 Applied: I chose the structures of a [[bio-core]] or Lab component from its operation profile and measured the result.
- [ ] 5 Explained: I can teach how invariants create costs, why interfaces plus models give lower bounds, and when relaxed contracts are acceptable.

## References

[^6006-l2]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 2 "Data Structures": interfaces versus data structures, the sequence and set interfaces, arrays, linked lists and dynamic arrays.
[^6006-l4]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 4 "Hashing": comparison-model lower bound, direct access arrays and hash tables.
[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022): dynamic sets and their operations, heaps as priority queues, B-trees.
[^clrs11]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 11 "Hash Tables".
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": list insertion cost, membership in lists versus hash-based dicts and sets, hashable keys.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], 3rd ed.: chapters "Where in the Genome Does DNA Replication Begin?" (k-mers numbered in base 4 to index a frequency array) and "How Do We Locate Disease-Causing Mutations?" (pattern matching with the Burrows-Wheeler transform).
[^stanford]: [[Coursera Stanford - Algorithms Specialization]], course 2 "Graph Search, Shortest Paths, and Data Structures": Bloom filters.
