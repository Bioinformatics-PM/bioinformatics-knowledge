---
aliases:
  - Pigeonhole Argument
  - Dirichlet's Box Principle
  - Drawer Principle
  - Box Principle
  - Principe des tiroirs
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Function]]"
  - "[[Combinatorics]]"
related:
  - "[[Seed and Extend]]"
  - "[[Read Mapping]]"
  - "[[K-mer]]"
  - "[[Hamming Distance]]"
  - "[[Edit Distance]]"
  - "[[Hash Function]]"
  - "[[Spaced Seed]]"
  - "[[Graph]]"
projects:
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Xin 2016 - Optimal Seed Solver]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Pigeonhole Principle

> [!abstract]
> If more objects than boxes are put into boxes, some box holds at least two: this obvious remark proves that hash collisions are unavoidable, that short k-mers must repeat in a genome, and that a read with $e$ errors cut into $e + 1$ pieces always keeps one piece intact, the guarantee behind seed-based read mapping.

## Definition

**Pigeonhole principle.** If $N$ objects are placed into $n$ boxes and $N > n$, at least one box contains two or more objects. **Generalized form**: some box contains at least $\lceil N/n \rceil$ objects. In the language of functions ([[Function]]): if $A$ and $B$ are finite with $|A| > |B|$, no function $f : A \to B$ is injective.[^lehman][^mcs]

## Why it matters

- **Seeds.** To tolerate $e$ errors, a mapper cuts a read into $e + 1$ seeds; by the pigeonhole principle at least one is error-free, so looking up seeds exactly cannot miss the true location.[^xin] This is the logic of [[Seed and Extend]] and of many short-read mappers ([[Read Mapping]], [[05-sequence-search]]).
- **Collisions are unavoidable.** A [[Hash Function]] from more keys than slots must send two keys to the same slot, so every [[Hash Table]] needs a collision strategy.
- **Forced repeats.** With more positions than possible 12-mers, the human genome must contain some 12-mer many times ([[Combinatorics]]); with 64 codons for 21 meanings, every genetic code is degenerate ([[Function]]).
- **Existence proofs.** The principle proves that something exists without saying where, a pattern used throughout algorithm analysis.

## Core (L1)

### Proof

**Basic form.** Suppose every box held at most one object. Then there would be at most $n$ objects, contradicting $N > n$.

**Generalized form.** Suppose every box held at most $\lceil N/n \rceil - 1$ objects. Since $\lceil x \rceil - 1 < x$, the total would be at most $n(\lceil N/n \rceil - 1) < n \cdot N/n = N$, a contradiction. $\square$

Examples:

- 64 codons sent to 20 amino acids and stop: some meaning receives at least $\lceil 64/21 \rceil = 4$ codons.
- 1.5 million distinct k-mers stored in a table of $2^{20} = 1{,}048{,}576$ slots: some slot receives at least 2 of them, whatever the hash function.
- $3.055 \times 10^9$ windows of the human assembly[^nurk] and $4^{12} \approx 1.7 \times 10^7$ possible 12-mers: some 12-mer occurs at least 183 times ([[Combinatorics#Core (L1)]]).

### Bio: one piece of the read is exact

**Seed lemma.** Let a read $r$ of length $L$ match a reference segment $t$ of the same length with at most $e$ mismatches. Cut $r$ into $e + 1$ non-overlapping pieces. Then at least one piece equals the corresponding piece of $t$ exactly.

**Proof.** Boxes are the $e + 1$ pieces, objects the mismatch positions. Pieces do not overlap, so each mismatch lies in exactly one piece and at most $e$ pieces contain a mismatch. At least one of the $e + 1$ pieces contains none. $\square$

Toy example (invented), $L = 12$, $e = 2$, three pieces of 4:

```text
reference  GATTACAGCTAG
read       GATTCCAGCTTG
               *     *      two mismatches
pieces     GATT|CCAG|CTTG
           exact  1mm  1mm
```

**From lemma to mapper.** Index the reference once (a hash table of k-mers or a compressed index), look up each piece exactly, turn each hit into a candidate start (hit position minus the piece offset), and verify each candidate by comparing or aligning the whole read. The lemma guarantees that the true location is among the candidates.[^xin] For a 100-bp read with up to 4 mismatches, the five 20-bp pieces are long enough to be usually unique in a human-sized genome ([[Combinatorics]]), so few candidates need verification.

## Deeper (L2)

- **$e + 1$ is optimal.** With only $e$ pieces, put one mismatch in each piece: no piece is exact. The exhaustive check below confirms it for $L = 12$, $e = 3$.
- **Insertions and deletions.** Charge each edit operation to one piece (an insertion falling between two pieces is charged to either neighbour). At most $e$ pieces are charged, so some piece still occurs exactly in the reference; but indels before it shift its position by up to $e$, so verification must use an alignment in a small band around the candidate ([[Edit Distance]]).
- **Sensitivity versus speed.** More tolerated errors means more, shorter pieces of length $s = \lfloor L/(e+1) \rfloor$, and short pieces hit the reference by chance. In a uniformly random genome of length $G$, a given $s$-mer is expected at about $2G/4^s$ positions on the two strands:

| read $L$ | errors $e$ | seed length $s$ | expected random hits per seed, $G = 3.055 \times 10^9$ |
|---:|---:|---:|---:|
| 100 | 4 | 20 | $5.6 \times 10^{-3}$ |
| 100 | 9 | 10 | $5.8 \times 10^{3}$ |
| 150 | 5 | 25 | $5.4 \times 10^{-6}$ |

The number of seeds sets the sensitivity of a mapper and their total frequency in the reference sets its speed.[^xin]
- **Several exact seeds.** Cutting into $e + s$ pieces leaves at least $s$ exact pieces. Requiring two seed hits per candidate filters many random hits.
- **Overlapping k-mers (q-gram bound).** A mismatch at position $x$ destroys only the k-mer windows containing $x$, at most $k$ of the $L - k + 1$ windows. With $e$ mismatches, at least $L - k + 1 - ek$ windows match exactly. K-mer-counting filters discard candidates that share fewer k-mers than this bound (Exercise 3).

## Advanced (L3)

- **Where to cut.** Pieces need not have equal length. Xin and colleagues choose $e + 1$ non-overlapping seeds that minimize their total frequency in the reference, by [[Dynamic Programming]] over the read, which keeps the pigeonhole guarantee while reducing candidates.[^xin]
- **Other seed designs.** [[Spaced Seed|Spaced seeds]] (patterns with "don't care" positions) and [[Minimizer|minimizers]] trade the exact guarantee for sensitivity or memory; seeing why requires the lemma above as a baseline.
- **The guarantee is about recall, not uniqueness.** The true location is always among the candidates, but a read from a repeat produces many equally good candidates; reporting how sure the mapper is of its choice is the job of [[Mapping Quality]].
- **Beyond sequences.** In any simple graph with $n \ge 2$ vertices, two vertices have the same degree (Exercise 4): the principle is a general proof tool, not a trick for strings ([[Graph]]).

## Mathematical representation

- **Fibers.** For $f : A \to B$ with $A, B$ finite, $|A| = \sum_{b \in B} |f^{-1}(b)| \le |B| \max_b |f^{-1}(b)|$, so $\max_b |f^{-1}(b)| \ge |A|/|B|$; being an integer, it is at least $\lceil |A|/|B| \rceil$. If $|A| > |B|$ this maximum is $\ge 2$: $f$ is not injective.
- **Seed lemma.** Partition $\{0, \dots, L-1\}$ into intervals $I_1, \dots, I_{e+1}$. Let $M = \{x : r_x \ne t_x\}$ with $|M| \le e$ and $\pi : M \to \{1, \dots, e+1\}$ send a mismatch to its interval. Then $|\pi(M)| \le |M| \le e < e + 1$, so some $j \notin \pi(M)$, i.e. $r[I_j] = t[I_j]$.
- **Equal pieces** have length $\lfloor L/(e+1) \rfloor$ or $\lceil L/(e+1) \rceil$; the shortest one sets the seed length.
- **q-gram bound.** With $W_x = \{i : i \le x < i + k\}$ the windows covering $x$, $|W_x| \le k$, so the intact windows number at least $(L - k + 1) - \sum_{x \in M} |W_x| \ge L - k + 1 - ek$.

## Computational representation

```python
from itertools import combinations
import random

def split_pieces(read, e):
    """Cut read into e + 1 non-overlapping pieces; returns (offset, piece) pairs."""
    L, parts = len(read), e + 1
    bounds = [L * i // parts for i in range(parts + 1)]
    return [(bounds[i], read[bounds[i]:bounds[i + 1]]) for i in range(parts)]

def always_one_exact(L, e, parts):
    """Exhaustive check: does every set of e mismatch positions leave a piece untouched?"""
    bounds = [L * i // parts for i in range(parts + 1)]
    piece_of = [next(p for p in range(parts) if bounds[p] <= x < bounds[p + 1]) for x in range(L)]
    return all(len({piece_of[x] for x in mm}) < parts for mm in combinations(range(L), e))

print(always_one_exact(12, 2, 3), always_one_exact(20, 4, 5), always_one_exact(12, 3, 3))

rng = random.Random(7)
genome = "".join(rng.choice("ACGT") for _ in range(5000))     # invented random reference
start, L, e = 1234, 40, 3
read = list(genome[start:start + L])
for x in rng.sample(range(L), e):                              # introduce e mismatches
    read[x] = rng.choice([b for b in "ACGT" if b != read[x]])
read = "".join(read)

pieces = split_pieces(read, e)
k = min(len(p) for _, p in pieces)
index = {}
for i in range(len(genome) - k + 1):                           # k-mer index of the reference
    index.setdefault(genome[i:i + k], []).append(i)

exact = [off for off, piece in pieces if genome[start + off:start + off + len(piece)] == piece]
candidates = {hit - off for off, piece in pieces for hit in index.get(piece[:k], [])}

def mismatches(pos):
    return sum(a != b for a, b in zip(read, genome[pos:pos + L]))

print(k, exact, [(c, mismatches(c)) for c in sorted(candidates) if 0 <= c <= len(genome) - L])

G = 3_055_000_000
for L, e in ((100, 4), (100, 9), (150, 5)):
    s = L // (e + 1)
    print(L, e, s, f"{2 * G / 4**s:.2e}")
```

```text
True True False
10 [20, 30] [(1234, 3)]
100 4 20 5.56e-03
100 9 10 5.83e+03
150 5 25 5.43e-06
```

The 40-bp read with 3 mismatches has two exact 10-bp pieces (offsets 20 and 30); together they propose a single candidate, position 1234, verified with 3 mismatches. Real mappers also search the reverse complement of the read.

## Worked example

> [!example] Seeds for 100-bp reads with up to 4 mismatches
> 1. **Pieces**: $e + 1 = 5$ pieces of $100/5 = 20$ bp.
> 2. **Guarantee**: 4 mismatches can spoil at most 4 pieces, so at least one 20-mer of the read occurs exactly at its true location.
> 3. **Cost**: each 20-mer is looked up in the index. Against a random genome of $3.055 \times 10^9$ bp, a 20-mer is expected at $2G/4^{20} \approx 0.006$ other positions, so almost all candidates are true ones; repeats in a real genome add more.
> 4. **Changing the error budget**: allowing 9 mismatches forces 10 pieces of 10 bp, each expected at about 5,800 random positions: the guarantee remains, but verification now dominates the run time.

## Common misconceptions

> [!warning] "Any $e + 1$ k-mers of the read will do"
> The pieces must not overlap. One mismatch can destroy up to $k$ overlapping k-mers, so $e + 1$ overlapping k-mers can all be hit by $e$ mismatches. For overlapping k-mers use the q-gram bound instead.

> [!warning] "An exact seed hit is a mapping"
> A seed hit only proposes a candidate. Random hits and repeats produce false candidates, so every candidate is verified on the whole read.

> [!warning] "With indels, the exact piece sits at its predicted offset"
> An insertion or deletion upstream shifts it by up to $e$ positions; verification must allow for that shift.

## Exercises

> [!question] Exercise 1 (L1)
> A k-mer counter stores 1.5 million distinct 21-mers in a hash table of $2^{20}$ slots. Show that some slot holds at least two k-mers. How many at least, in the fullest slot?

> [!success]- Solution
> $1{,}500{,}000 > 1{,}048{,}576$, so some slot holds two or more keys; generalized form: at least $\lceil 1{,}500{,}000/1{,}048{,}576 \rceil = 2$. No choice of hash function avoids it.

> [!question] Exercise 2 (L2)
> Show that cutting the read into only $e$ pieces gives no guarantee, and confirm with `always_one_exact`.

> [!success]- Solution
> Place one mismatch in each of the $e$ pieces: all are spoiled, yet the read has only $e$ mismatches. `always_one_exact(12, 3, 3)` prints `False`, while `always_one_exact(12, 2, 3)` and `always_one_exact(20, 4, 5)` print `True`.

> [!question] Exercise 3 (L2, Python)
> Prove that a read with at most $e$ mismatches shares at least $L - k + 1 - ek$ exact k-mer windows with its true location, and check by enumeration that the bound is attained for $L = 12, k = 3, e = 2$ and $L = 15, k = 4, e = 2$. What does it give for $L = 100$, $e = 4$, $k = 20$ and $k = 11$?

> [!success]- Solution
> Proof in the Mathematical representation. Enumeration:
> ```python
> from itertools import combinations
>
> def min_intact_windows(L, k, e):
>     """Minimum number of k-windows free of mismatches, over all placements of e mismatches."""
>     best = L
>     for mm in combinations(range(L), e):
>         intact = sum(1 for i in range(L - k + 1) if not any(i <= x < i + k for x in mm))
>         best = min(best, intact)
>     return best
>
> print(min_intact_windows(12, 3, 2), 12 - 3 + 1 - 2 * 3, min_intact_windows(15, 4, 2), 15 - 4 + 1 - 2 * 4)
> ```
> Output: `4 4 4 4`: the bound is attained (mismatches far from each other and from the ends). For $L = 100$, $e = 4$: $k = 20$ gives $81 - 80 = 1$, consistent with the single exact piece guaranteed by the seed lemma; $k = 11$ gives $90 - 44 = 46$ shared 11-mers, a much stronger filter.

> [!question] Exercise 4 (L3, Python)
> Prove that every simple graph with $n \ge 2$ vertices has two vertices of equal degree, and verify it on all graphs with 5 vertices.

> [!success]- Solution
> Degrees lie in $\{0, \dots, n-1\}$: $n$ values for $n$ vertices, not yet enough. But 0 and $n - 1$ cannot both occur: a vertex of degree $n - 1$ is adjacent to every other vertex, so none has degree 0. The $n$ degrees therefore take at most $n - 1$ values, and two coincide.
> ```python
> from itertools import combinations, product
>
> pairs = list(combinations(range(5), 2))
> ok = True
> for mask in product((0, 1), repeat=len(pairs)):        # every graph on 5 labelled vertices
>     deg = [0] * 5
>     for (u, v), bit in zip(pairs, mask):
>         if bit:
>             deg[u] += 1
>             deg[v] += 1
>     ok &= len(set(deg)) < 5
> print(len(pairs), 2 ** len(pairs), ok)
> ```
> Output: `10 1024 True`.

## Mastery checklist

- [ ] 1 Recognized: I can state the pigeonhole principle and its generalized form.
- [ ] 2 Understood: I can prove the seed lemma and explain why the pieces must not overlap and why $e + 1$ is the minimum.
- [ ] 3 Practiced: I can implement seed splitting, an exact seed lookup and the q-gram bound, and verify them by enumeration.
- [ ] 4 Applied: I chose seed lengths for a real read length and error budget in [[05-sequence-search]] and measured candidates per read.
- [ ] 5 Explained: I can teach the sensitivity-speed trade-off of seeds, the effect of indels, and why the guarantee says nothing about uniqueness.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, treatment of counting (the pigeonhole principle and its generalized form).
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], counting part.
[^xin]: [[Xin 2016 - Optimal Seed Solver]], *Bioinformatics* 32(11):1632-1642: background on $e + 1$ seeds and the pigeonhole principle, seed number versus seed frequency, and optimal seed selection.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*.
