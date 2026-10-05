---
aliases:
  - Hash Map
  - Dictionary (Data Structure)
  - Table de hachage
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Abstract Data Type]]"
  - "[[Array]]"
  - "[[Hash Function]]"
  - "[[Expected Value]]"
related:
  - "[[K-mer]]"
  - "[[Genetic Code]]"
  - "[[Inverted Index]]"
  - "[[Bloom Filter]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Hash Table

> [!abstract]
> A hash table stores key-value pairs in an array, at the slot that the key's hash designates, so that lookup, insertion and deletion take constant expected time while the table is not too full. It is the structure behind Python's `dict`, `set` and `Counter`, and behind every codon table and k-mer counter.

## Definition

A **hash table** implements a dynamic set or map with an array of $m$ slots: key $k$ goes to slot $h(k)$ ([[Hash Function]]). Keys that collide are handled by **chaining**, where each slot holds a list of its items, or by **open addressing**, where all items live in the array and an insertion probes a sequence of slots until it finds a free one; **linear probing** tries $h(k), h(k) + 1, h(k) + 2, \dots$ With $n$ stored items, the **load factor** is $\alpha = n/m$; under uniform hashing, chaining performs search, insertion and deletion in $O(1 + \alpha)$ expected time.[^clrs11] Growing the table by a constant factor when $\alpha$ passes a threshold keeps $\alpha$ bounded, for $O(1)$ expected amortized operations.[^6006-l4] Python's `dict` and `set` are hash tables, which is why membership tests on them take constant time on average, unlike on lists.[^mck3]

## Why it matters

- **Codon tables.** A 64-key map from codon to amino acid translates a coding sequence in one pass ([[Genetic Code]], [[02-sequence-translation]]).
- **k-mer counting and indexing.** `Counter` counts k-mers; a map from k-mer to positions finds exact seeds of a read in a reference ([[K-mer]], [[Inverted Index]], [[05-sequence-search]]). Joining two tables on gene identifiers, or deduplicating read names, is likewise a sequence of hash lookups.

## Core (L1)

![[hash-table-chaining-vs-probing.svg]]

- **Direct addressing** when the key space is small: read as base-4 numbers, the 64 codons index a 64-slot array, and for small $k$ the k-mers index a frequency array of $4^k$ counters, with no collisions at all.[^compeau] A hash table generalizes this to huge key spaces (all strings, all 31-mers) at the price of collisions.
- **Operations.** `get` hashes the key and inspects its slot (its chain, or its probe sequence); `put` updates the existing item or adds one; `delete` removes it, which under open addressing requires a **tombstone** (panel B, Exercise 3).
- **Resizing.** When $\alpha$ passes a threshold, allocate about twice as many slots and reinsert every item; as for dynamic arrays, the occasional $\Theta(n)$ rehash costs $O(1)$ amortized per insertion ([[Array]]).
- **In Python.** `dict` (map), `set` (set), `collections.Counter` (map to counts) and `collections.defaultdict` (map with a default value factory). Keys must be hashable: `str`, `int`, `tuple` and `frozenset` qualify, `list` and `dict` do not.[^mck3]

```python
from collections import Counter

BASES = "TCAG"
CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]
codon_table = dict(zip(CODONS, "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
orf = "ATGGCTAAAGGTGAAGCTTTCTGGAAACTGGGTTAA"      # toy ORF (invented)
codons = [orf[i:i + 3] for i in range(0, len(orf) - 2, 3)]
print("".join(codon_table.get(c, "X") for c in codons), codon_table.get("ANG", "X"))
print(Counter(codons).most_common(3))
seq, k = "GATTACAGATTACACAT", 4                  # toy sequence (invented)
counts = Counter(seq[i:i + k] for i in range(len(seq) - k + 1))
print(counts.most_common(3), len(counts))
```

```text
MAKGEAFWKLG* X
[('GCT', 2), ('AAA', 2), ('GGT', 2)]
[('GATT', 2), ('ATTA', 2), ('TTAC', 2)] 10
```

The 64-letter string is NCBI's standard code (table 1) in TCAG order;[^ncbi] `get(c, "X")` maps a codon containing `N` to the unknown amino acid instead of raising `KeyError`.

## Deeper (L2)

**Chaining.** Under uniform hashing, the length $n_j$ of the chain in slot $j$ has expectation $\alpha$. An unsuccessful search hashes the key and scans its whole chain: $\Theta(1 + \alpha)$ expected time. A successful search for the $i$-th inserted key scans that key plus the keys inserted before it into the same slot (new items go to the end of the chain), $1 + (i - 1)/m$ on average; averaging over $i$ gives $1 + \frac{n - 1}{2m}$, also $\Theta(1 + \alpha)$.[^clrs11] With a universal family, these bounds hold in expectation over the choice of $h$ for every fixed set of keys ([[Hash Function]]). Since $n_j$ is a sum of $n$ independent indicators of probability $1/m$, chain lengths follow a binomial distribution, close to Poisson($\alpha$) ([[Poisson Distribution]]). The `ChainedMap` of the Computational representation confirms it: after counting the 8-mers of a random 20-kb toy genome, its $m = 32{,}768$ chains ($\alpha = 0.522$) have lengths 0, 1 and 2 as often as $m e^{-\alpha} \alpha^L / L!$ predicts, within 1%.

**Open addressing.** If every probe sequence were a uniformly random permutation of the slots, the probability that an unsuccessful search makes more than $i$ probes would be at most $\alpha^i$, so its expected number of probes is at most $\sum_{i \ge 0} \alpha^i = \frac{1}{1 - \alpha}$; a successful search needs at most $\frac{1}{\alpha} \ln \frac{1}{1 - \alpha}$.[^clrs11] Linear probing does worse: occupied runs merge and grow (primary clustering). Simulated with $m = 2^{16}$ slots and 20,000 unsuccessful searches:

```python
import random

def probes_unsuccessful(alpha, m=2**16, trials=20_000, seed=0):
    """Mean probes of an unsuccessful search under linear probing; keys hashed to uniform random slots."""
    r = random.Random(seed)
    used = [False] * m
    for _ in range(int(alpha * m)):
        i = r.randrange(m)
        while used[i]:
            i = (i + 1) % m
        used[i] = True
    total = 0
    for _ in range(trials):
        i, probes = r.randrange(m), 1
        while used[i]:
            i, probes = (i + 1) % m, probes + 1
        total += probes
    return total / trials

for a in (0.5, 0.75, 0.9):
    print(a, round(probes_unsuccessful(a), 2), round(1 / (1 - a), 2))
```

```text
0.5 2.51 2.0
0.75 8.35 4.0
0.9 44.76 10.0
```

At $\alpha = 0.5$ linear probing is close to the ideal; at $0.9$ it is 4.5 times worse. Yet its probes read consecutive slots, and hardware caches favor such local accesses, which is why the 4th edition of CLRS emphasizes linear probing.[^clrs11] Linear-probing tables therefore keep $\alpha$ moderate and grow early.

## Advanced (L3)

- **Worst case.** If all keys fall in one slot, every operation is $\Theta(n)$. A fixed hash function always has such inputs; randomizing the function (universal hashing, a salted hash) restores the expected bounds for every input ([[Hash Function]]).[^clrs11]
- **Genome-scale memory.** With `tracemalloc`, a `Counter` of the 199,980 distinct 21-mers of a random 200-kb sequence used about 108 bytes per entry (the string object plus its share of the table). The T2T-CHM13 genome has about $3.055 \times 10^9$ positions,[^nurk] hence at most that many distinct 21-mers per strand: up to about 330 GB as a `Counter`. Packing each k-mer in 8 bytes (2 bits per base, [[String]]) with a 4-byte count in an open-addressing array kept half full costs 24 bytes per k-mer, up to 73 GB. Beyond that come canonical k-mers that merge both strands ([[Reverse Complement]]), approximate structures ([[Bloom Filter]], [[Count-Min Sketch]]) and sorting-based counting on disk ([[External Memory Algorithm]]).
- **No order.** A hash table answers `find_next`, range and prefix queries only by scanning everything, $O(n)$;[^6006-l4] sorted arrays, balanced search trees and tries answer them in logarithmic or $O(|p|)$ time ([[Binary Search Tree]], [[Trie]]).

## Mathematical representation

- $\alpha = n/m$; chain length $n_j = \sum_{x} [h(x) = j] \sim \mathrm{Binomial}(n, 1/m) \approx \mathrm{Poisson}(\alpha)$, with $E[n_j] = \alpha$.
- Chaining: unsuccessful search $\Theta(1 + \alpha)$; successful search $1 + \frac{n-1}{2m} = 1 + \frac{\alpha}{2} - \frac{\alpha}{2n}$ examined items on average.
- Open addressing under uniform permutation hashing: $E[\text{probes, unsuccessful}] \le \frac{1}{1 - \alpha}$, $E[\text{probes, successful}] \le \frac{1}{\alpha} \ln \frac{1}{1 - \alpha}$. Resizing by doubling when $\alpha$ exceeds a constant: total rehashing work $< 2n$ over $n$ insertions.

## Computational representation

A map with separate chaining and doubling, checked against `Counter`. It hashes with `zlib.crc32`, deterministic across runs (Python's `hash` of a `str` is salted per process), so the statistics above are reproducible.

```python
import math, zlib

class ChainedMap:
    """Separate chaining; doubles the number of slots when the load factor n/m would exceed 1."""
    def __init__(self, m=8, h=lambda key: zlib.crc32(key.encode())):
        self.slots, self.n, self.h = [[] for _ in range(m)], 0, h
    def _chain(self, key):
        return self.slots[self.h(key) % len(self.slots)]
    def get(self, key, default=None):
        for k, v in self._chain(key):
            if k == key:
                return v
        return default
    def put(self, key, value):
        chain = self._chain(key)
        for i, (k, _) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)         # existing key: update in place
                return
        chain.append((key, value))
        self.n += 1
        if self.n > len(self.slots):            # rehash every item into twice as many slots
            items = [kv for c in self.slots for kv in c]
            self.slots = [[] for _ in range(2 * len(self.slots))]
            for k, v in items:
                self._chain(k).append((k, v))

rng = random.Random(7)
genome = "".join(rng.choice("ACGT") for _ in range(20_000))   # random toy genome (invented)
cm, k = ChainedMap(), 8
for i in range(len(genome) - k + 1):
    km = genome[i:i + k]
    cm.put(km, cm.get(km, 0) + 1)
ref = Counter(genome[i:i + k] for i in range(len(genome) - k + 1))
lengths = Counter(len(c) for c in cm.slots)
m, alpha = len(cm.slots), cm.n / len(cm.slots)
print(cm.n == len(ref) and all(cm.get(x) == c for x, c in ref.items()), m, round(alpha, 3))
print([(L, lengths[L], round(m * math.exp(-alpha) * alpha**L / math.factorial(L))) for L in range(5)])
```

```text
True 32768 0.522
[(0, 19372, 19438), (1, 10248, 10151), (2, 2643, 2650), (3, 446, 461), (4, 55, 60)]
```

## Worked example

> [!example] Seeding a read with a k-mer index (toy sequences, invented)
> 1. **Index the reference** `ACGTTGCATGCATTGCA` with $k = 4$: map each 4-mer to its start positions, $O(n)$ expected.
> 2. **Look up each 4-mer of the read** `TGCATT` and turn each hit at reference position $p$ for read offset $j$ into a candidate alignment start $p - j$ (a diagonal).
> 3. **Vote**: the start supported by most k-mers is the best candidate.
> ```python
> from collections import Counter, defaultdict
> index = defaultdict(list)
> ref_seq, k = "ACGTTGCATGCATTGCA", 4
> for i in range(len(ref_seq) - k + 1):
>     index[ref_seq[i:i + k]].append(i)
> read = "TGCATT"
> hits = Counter(p - j for j in range(len(read) - k + 1) for p in index.get(read[j:j + k], []))
> print(index["TGCA"], hits.most_common(2))
> # [4, 8, 13] [(8, 3), (4, 2)]
> ```
> 4. **Read the result**: `TGCA` occurs three times in the reference, but all three 4-mers of the read agree on start 8, and indeed `ref_seq[8:14] == "TGCATT"`. Each lookup is $O(1)$ expected, so seeding costs time proportional to the number of k-mers and hits, not to the reference length ([[Inverted Index]], [[05-sequence-search]]).

## Common misconceptions

> [!warning] "Dictionary lookups are always O(1)"
> They are $O(1)$ in expectation and amortized over resizes. Colliding keys or a poor hash make individual operations $\Theta(n)$.[^clrs11]

> [!warning] "Deleting from an open-addressing table just empties the slot"
> Emptying a slot cuts the probe sequences that passed through it: keys stored further along become unreachable (Exercise 3). Deletion leaves a tombstone that searches skip and insertions may reuse.

## Exercises

> [!question] Exercise 1 (L1)
> Which of these can be dictionary keys: `"ACGT"`, `["A", "C"]`, `("chr1", 1000)`, `{"A": 1}`, `frozenset({"A", "T"})`? A chained table holds $n = 3000$ items in $m = 1024$ slots: give $\alpha$ and the expected cost of an unsuccessful search.

> [!success]- Solution
> The string, the tuple of immutables and the frozenset are hashable; the list and the dict are not (use `tuple(...)` to key on a list's contents).[^mck3] $\alpha = 3000/1024 \approx 2.93$; an unsuccessful search hashes once and scans about 2.93 items, $\Theta(1 + \alpha)$. A doubling policy at $\alpha > 1$ would already have grown the table to 4,096 slots ($\alpha \approx 0.73$).

> [!question] Exercise 2 (L2)
> Derive the expected number of items examined in a successful search with chaining, $1 + (n - 1)/(2m)$, assuming uniform hashing, insertion at the end of chains, and a search target chosen uniformly among the $n$ keys.

> [!success]- Solution
> Let $x_i$ be the $i$-th inserted key. Searching for it examines $x_i$ plus every earlier key $x_j$ ($j < i$) in the same slot, each with probability $1/m$: $1 + (i - 1)/m$ in expectation. Averaging over $i$: $\frac{1}{n} \sum_{i=1}^{n} \left(1 + \frac{i - 1}{m}\right) = 1 + \frac{1}{nm} \cdot \frac{n(n-1)}{2} = 1 + \frac{n - 1}{2m}$.

> [!question] Exercise 3 (L3, Python)
> Implement a fixed-size linear-probing map with `put`, `get` and `delete`. Insert ATG, TGG, AAA, GCC, TAA with the toy hash values of the figure, delete ATG, then look up AAA: once by emptying the slot, once with a tombstone.

> [!success]- Solution
> ```python
> EMPTY, TOMB = object(), object()
> class LinearProbingMap:
>     def __init__(self, m, h):
>         self.keys, self.vals, self.h = [EMPTY] * m, [None] * m, h
>     def _probe(self, key):                      # h(k), h(k) + 1, ... around the table once
>         start = self.h(key) % len(self.keys)
>         return [(start + j) % len(self.keys) for j in range(len(self.keys))]
>     def put(self, key, value):
>         for i in self._probe(key):
>             if self.keys[i] is EMPTY or self.keys[i] is TOMB or self.keys[i] == key:
>                 self.keys[i], self.vals[i] = key, value
>                 return
>     def get(self, key):
>         for i in self._probe(key):
>             if self.keys[i] is EMPTY:
>                 return None                      # an empty slot ends every probe sequence
>             if self.keys[i] == key:
>                 return self.vals[i]
>     def delete(self, key, tombstone=True):
>         for i in self._probe(key):
>             if self.keys[i] == key:
>                 self.keys[i] = TOMB if tombstone else EMPTY
>                 return
>
> TOY = {"ATG": 3, "TGG": 6, "AAA": 3, "GCC": 1, "TAA": 6}   # toy hash values (invented)
> for tomb in (False, True):
>     lp = LinearProbingMap(8, TOY.get)
>     for key in TOY:
>         lp.put(key, codon_table[key])
>     lp.delete("ATG", tombstone=tomb)
>     print(tomb, ["." if x is EMPTY else "x" if x is TOMB else x for x in lp.keys], lp.get("AAA"))
> # False ['.', 'GCC', '.', '.', 'AAA', '.', 'TGG', 'TAA'] None
> # True ['.', 'GCC', '.', 'x', 'AAA', '.', 'TGG', 'TAA'] K
> ```
> Without a tombstone the search for AAA starts at slot 3, finds it empty and wrongly concludes that AAA is absent. A complete `put` may reuse the first tombstone only after checking that the key is not stored further along its probe sequence; the version above skips that check, which is safe here because each key is inserted once.

## Mastery checklist

- [ ] 1 Recognized: I can define a hash table, a collision, the load factor, chaining and open addressing.
- [ ] 2 Understood: I can explain why operations are $O(1)$ expected and amortized, and what breaks that bound.
- [ ] 3 Practiced: I can implement chaining with resizing and linear probing with tombstones, and derive the expected search costs.
- [ ] 4 Applied: I built the codon table of [[02-sequence-translation]] and the k-mer index of [[05-sequence-search]], and measured their memory.
- [ ] 5 Explained: I can teach load-factor trade-offs, clustering and locality, and when to switch to compact or approximate structures.

## References

[^clrs11]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 11 "Hash Tables": direct addressing, chaining, load factor and expected search times, open addressing with its probe bounds, linear probing presented as efficient on caching hardware, random hashing against bad inputs.
[^6006-l4]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 4 "Hashing": hash tables with resizing, expected and amortized bounds, set operations a hash table does not support efficiently.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": dicts and sets as hash-based containers, constant-time membership, hashable keys.
[^ncbi]: [[NCBI Genetic Codes]]: the standard code (translation table 1) in the TCAG codon order.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], 3rd ed., chapter "Where in the Genome Does DNA Replication Begin?": frequency arrays indexed by k-mers read in base 4.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*: 3.055 Gbp T2T-CHM13 assembly.
