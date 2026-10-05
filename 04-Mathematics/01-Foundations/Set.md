---
aliases:
  - Set Theory
  - Set Operations
  - Venn Diagram
  - Power Set
  - Ensemble (mathématiques)
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Propositional Logic]]"
  - "[[Predicate Logic]]"
related:
  - "[[Binary Relation]]"
  - "[[Function]]"
  - "[[Probability Space]]"
  - "[[K-mer]]"
  - "[[Jaccard Index]]"
  - "[[MinHash]]"
  - "[[Over-Representation Analysis]]"
projects:
  - "[[05-sequence-search]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]]"
  - "[[GA4GH hts-specs]]"
---

# Set

> [!abstract]
> A set is a collection of distinct objects without order; union, intersection, difference and complement combine sets the way OR, AND, AND NOT and NOT combine statements, which is how gene lists, k-mer collections and genomic regions are compared.

## Definition

A **set** is an unordered collection of distinct elements; $x \in A$ means "$x$ is an element of $A$". Two sets are equal when they have the same elements, so order and repetition do not matter: $\{A, C\} = \{C, A, A\}$. $A \subseteq B$ ($A$ is a **subset** of $B$) when every element of $A$ is in $B$; $\varnothing$ is the empty set and $|A|$ the number of elements of a finite set.[^lehman][^mcs] A set is written by listing, $\{A, C, G, T\}$, or by a property, $\{x \in U : P(x)\}$ ([[Predicate Logic]]).

## Why it matters

- **Gene lists.** Which genes respond in both conditions, in one only, in neither: intersections and differences of lists, drawn as Venn diagrams ([[Differential Expression Analysis]]).
- **Shared k-mers.** Two genomes can be compared without alignment by the k-mers they share. The [[Jaccard Index]] $|A \cap B| / |A \cup B|$ of their k-mer sets measures similarity, and [[MinHash]] estimates it at genome scale ([[K-mer]], [[05-sequence-search]]).
- **Events.** Probability is defined on sets of outcomes; "and", "or", "not" of events are $\cap$, $\cup$ and complement ([[Probability Space]]).
- **Regions.** Genomic intervals are sets of positions; intersecting peaks with genes or removing repeats is set algebra on intervals ([[Genomic Interval Arithmetic]]).

## Core (L1)

### Operations

Inside a **universe** $U$ of all elements under consideration:[^lehman]

| Operation | Notation | Elements | Logic | Python |
|---|---|---|---|---|
| union | $A \cup B$ | in $A$ or in $B$ | $\lor$ | `A.union(B)` |
| intersection | $A \cap B$ | in both | $\land$ | `A & B` |
| difference | $A \setminus B$ | in $A$, not in $B$ | $\land\, \neg$ | `A - B` |
| symmetric difference | $A \,\triangle\, B$ | in exactly one | exclusive or | `A ^ B` |
| complement | $A^c = U \setminus A$ | in $U$, not in $A$ | $\neg$ | `U - A` |
| Cartesian product | $A \times B$ | ordered pairs $(a, b)$ | | `itertools.product(A, B)` |
| power set | $\mathcal{P}(A)$ | all subsets of $A$ | | see code |

![[gene-list-venn-operations.svg]]

### De Morgan's laws

$$(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c.$$

**Proof** (element chasing). For $x \in U$: $x \in (A \cup B)^c \iff \neg(x \in A \lor x \in B) \iff x \notin A \land x \notin B \iff x \in A^c \cap B^c$. The middle step is De Morgan's law of [[Propositional Logic]], and two sets with the same elements are equal. The second law is proved the same way. $\square$ In words: the genes up in neither condition are those not up in condition 1 *and* not up in condition 2.

### Counting

- $|A \cup B| = |A| + |B| - |A \cap B|$, because $|A| + |B|$ counts the intersection twice ([[Inclusion-Exclusion Principle]]).
- $|A \times B| = |A| \cdot |B|$. Over $\Sigma = \{A, C, G, T\}$, the words of length $k$ form $\Sigma^k = \Sigma \times \dots \times \Sigma$, with $4^k$ elements: 16 dinucleotides, 64 codons ([[Codon]]).
- $|\mathcal{P}(A)| = 2^{|A|}$: each element is in or out of a subset (proof below). The $2^4 - 1 = 15$ non-empty subsets of $\{A, C, G, T\}$ are exactly the 15 IUPAC nucleotide codes, from `A` = $\{A\}$ to `N` = $\{A, C, G, T\}$ ([[IUPAC Nucleotide Code]]).[^iupac]

### Bio: overlap of two gene lists

In the figure (invented counts), 450 and 400 genes are up in conditions 1 and 2, with 150 in common, among 20,000 measured genes. Then $|A \cup B| = 450 + 400 - 150 = 700$ genes respond in at least one condition, $|A \setminus B| = 300$ only in condition 1, and $20{,}000 - 700 = 19{,}300$ in neither. That last number depends entirely on $U$: a complement exists only relative to a universe.

### Bio: shared k-mers

The k-mer set of $s = s_1 \dots s_n$ is $K_k(s) = \{s_i \dots s_{i+k-1} : 1 \le i \le n - k + 1\}$ ([[K-mer]]). Two invented 14-mers that differ by one substitution share 9 of their 14 distinct 3-mers but only 3 of their 13 distinct 7-mers (code below). One substitution destroys every k-mer that overlaps it, up to $k$ of them, so the Jaccard index falls as $k$ grows: long k-mers are specific, short ones tolerate differences.

## Deeper (L2)

- **Three lists.** $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$ (Exercise 3).
- **The universe is a modeling choice.** For a gene list, $U$ should be the genes that *could* have appeared in it (measured and tested), not the whole genome. If $B$ were a random subset of $U$ of its size, each gene of $A$ would fall in $B$ with probability $|B|/|U|$, so the expected overlap is $|A||B|/|U|$: 9 genes for the lists of the figure, against 150 observed. A larger $U$ shrinks the expected overlap and makes the same overlap look more surprising: the background decides the significance of overlaps and enrichments ([[Over-Representation Analysis]], [[Hypergeometric Distribution]]).
- **Sets lose multiplicity.** The 3-mer set of `ACGTACGTTACG` forgets that `ACG` occurs three times. Counts need a **multiset** (Python `Counter`), the object behind a [[K-mer Spectrum]]. Strand symmetry is handled by replacing each k-mer with a canonical representative before building the set (Exercise 4, [[Function#Advanced (L3)]]).
- **Sets of sets.** $\mathcal{P}(A)$ and partitions (sets of disjoint non-empty blocks covering $A$) have sets as elements; Python needs the hashable `frozenset` for them. Partitions are the classes of equivalence relations ([[Binary Relation]]).

## Advanced (L3)

- **Estimating the Jaccard index from minima.** Let $h$ be a random injective hash function on $A \cup B$. Each element of $A \cup B$ is equally likely to have the smallest hash, and $\min h(A) = \min h(B)$ exactly when that element lies in $A \cap B$. Hence
$$P\big(\min h(A) = \min h(B)\big) = \frac{|A \cap B|}{|A \cup B|} = J(A, B),$$
and the fraction of agreeing minima over $m$ independent hash functions estimates $J$ with standard error $\sqrt{J(1 - J)/m}$. Comparing $m$ stored minima replaces comparing millions of k-mers: the idea of [[MinHash]] (Exercise 5).
- **Interval sets.** A BED interval is 0-based and half-open, $[\text{start}, \text{end})$,[^bed] so it holds exactly $\text{end} - \text{start}$ positions, and $[a, b)$ and $[b, c)$ are disjoint with union $[a, c)$. Interval sets are intersected by sweeping sorted endpoints, never by listing positions ([[Genomic Interval Arithmetic]], [[BED Format]]).

## Mathematical representation

- $A \cup B = \{x : x \in A \lor x \in B\}$, $A \cap B = \{x : x \in A \land x \in B\}$, $A \setminus B = \{x \in A : x \notin B\} = A \cap B^c$, $A^c = U \setminus A$.
- **Laws**, each proved by element chasing from a law of [[Propositional Logic]]: commutativity, associativity, distributivity $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ and $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$, De Morgan, and $A \subseteq B \iff A \cap B = A \iff A \cup B = B$.
- **Equality.** $A = B \iff (A \subseteq B \land B \subseteq A)$, the standard way to prove two sets equal.
- **Power set size.** For $A = \{a_1, \dots, a_n\}$, map each subset $S$ to its indicator vector $\big(\mathbb{1}[a_1 \in S], \dots, \mathbb{1}[a_n \in S]\big) \in \{0, 1\}^n$. This map is a bijection ([[Function]]), so $|\mathcal{P}(A)| = |\{0, 1\}^n| = 2^n$. The same idea stores an IUPAC code as a 4-bit mask.

## Computational representation

```python
from itertools import combinations, product

U = {f"g{i:02d}" for i in range(1, 13)}       # invented universe: 12 measured genes
A = {"g01", "g02", "g03", "g04", "g05"}        # invented: up-regulated in condition 1
B = {"g04", "g05", "g06", "g07"}               # invented: up-regulated in condition 2

print(sorted(A | B))                                   # union
print(sorted(A & B), sorted(A - B), sorted(A ^ B))     # intersection, difference, symmetric difference
print(len(U - A), (U - (A | B)) == (U - A) & (U - B))  # size of the complement of A; De Morgan
print(len(A | B) == len(A) + len(B) - len(A & B))      # inclusion-exclusion

def power_set(s):
    items = sorted(s)
    return [frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r)]

print(len(list(product("ACGT", repeat=3))), len(power_set("ACGT")))   # |Sigma^3|, |P(Sigma)|

def kmer_set(seq: str, k: int) -> set[str]:
    return {seq[i:i + k] for i in range(len(seq) - k + 1)}

def jaccard(x: set, y: set) -> float:
    return len(x & y) / len(x | y) if x | y else 1.0

s1 = "ATGCGTACGTTAGC"     # invented
s2 = "ATGCGTACGATAGC"     # invented: s1 with its 10th base T changed to A
for k in (3, 5, 7):
    k1, k2 = kmer_set(s1, k), kmer_set(s2, k)
    print(k, len(k1 & k2), len(k1 | k2), round(jaccard(k1, k2), 3))
```

```text
['g01', 'g02', 'g03', 'g04', 'g05', 'g06', 'g07']
['g04', 'g05'] ['g01', 'g02', 'g03'] ['g01', 'g02', 'g03', 'g06', 'g07']
7 True
True
64 16
3 9 14 0.643
5 5 15 0.333
7 3 13 0.231
```

## Worked example

> [!example] Two small gene lists, every operation (invented data of the code above)
> $U = \{g01, \dots, g12\}$, $A = \{g01, \dots, g05\}$, $B = \{g04, \dots, g07\}$.
> 1. $A \cap B = \{g04, g05\}$ and $A \cup B = \{g01, \dots, g07\}$: $7 = 5 + 4 - 2$.
> 2. $A \setminus B = \{g01, g02, g03\}$, $B \setminus A = \{g06, g07\}$, and $A \triangle B$ is their union, 5 genes.
> 3. $(A \cup B)^c = \{g08, \dots, g12\}$. Separately, $A^c = \{g06, \dots, g12\}$ and $B^c = \{g01, g02, g03, g08, \dots, g12\}$, whose intersection is again $\{g08, \dots, g12\}$, as De Morgan says.
> 4. $J(A, B) = 2/7 = 0.286$.
> 5. **Is the overlap surprising?** Random lists of sizes 5 and 4 in a universe of 12 share $5 \times 4 / 12 \approx 1.7$ genes on average; 2 shared genes are unremarkable.

## Common misconceptions

> [!warning] "The complement of a gene list is the rest of the genome"
> A complement exists only relative to a universe. For an expression study the natural universe is the set of genes measured; taking every annotated gene inflates the complement and biases every overlap statistic built on it.

> [!warning] "A large overlap in a Venn diagram is a finding"
> Unrelated lists overlap by $|A||B|/|U|$ on average, which is large for long lists. Judge an overlap against this expectation with a test ([[Over-Representation Analysis]]).

> [!warning] "A set of k-mers records how often each occurs"
> A set records presence only. Use a multiset for abundance, and a set when presence is what matters, as in the Jaccard index.

## Exercises

> [!question] Exercise 1 (L1)
> With $U = \{1, \dots, 10\}$, $A = \{1, 2, 3, 4\}$ and $B = \{3, 4, 5, 6\}$, compute $A \cup B$, $A \cap B$, $A \setminus B$, $A^c \cap B$, $|A \times B|$ and $|\mathcal{P}(A \cap B)|$.

> [!success]- Solution
> $\{1, \dots, 6\}$; $\{3, 4\}$; $\{1, 2\}$; $\{5, 6\}$ (elements of $B$ not in $A$, i.e. $B \setminus A$); $4 \times 4 = 16$; $2^2 = 4$, namely $\varnothing, \{3\}, \{4\}, \{3, 4\}$.

> [!question] Exercise 2 (L1)
> Prove $(A \cap B)^c = A^c \cup B^c$ by element chasing.

> [!success]- Solution
> For $x \in U$: $x \in (A \cap B)^c \iff \neg(x \in A \land x \in B) \iff x \notin A \lor x \notin B \iff x \in A^c \cup B^c$, using De Morgan's law for propositions.

> [!question] Exercise 3 (L2)
> Three genetic screens hit 120, 90 and 60 genes; the pairwise overlaps are 40 (A∩B), 25 (A∩C) and 20 (B∩C), and 10 genes are hit by all three (invented). How many genes are hit at least once? How many by screen A only?

> [!success]- Solution
> $120 + 90 + 60 - 40 - 25 - 20 + 10 = 195$. A only: $120 - 40 - 25 + 10 = 65$; the 10 triple hits were removed twice, once in each pairwise overlap, so they are added back once.

> [!question] Exercise 4 (L2, Python)
> `t = rc(s1)` is the same DNA as `s1`, read from the other strand. Using `kmer_set` and `jaccard` from the code above, compare the Jaccard index of their raw 5-mer sets with that of their canonical 5-mer sets, where each k-mer $w$ is replaced by $\min(w, \mathrm{rc}(w))$.

> [!success]- Solution
> ```python
> def rc(s: str) -> str:
>     return s.translate(str.maketrans("ACGT", "TGCA"))[::-1]
>
> def canonical_set(seq: str, k: int) -> set[str]:
>     return {min(w, rc(w)) for w in kmer_set(seq, k)}
>
> t = rc(s1)
> print(round(jaccard(kmer_set(s1, 5), kmer_set(t, 5)), 3), jaccard(canonical_set(s1, 5), canonical_set(t, 5)))
> ```
> Output: `0.111 1.0`. Raw sets share only 2 of 18 distinct 5-mers (`CGTAC` and `GTACG`, which happen to be each other's reverse complement), although the molecules are identical. Canonical sets are equal: compare DNA k-mer sets on canonical forms ([[Reverse Complement]]).

> [!question] Exercise 5 (L3, Python)
> Generate an invented 2,000 bp sequence and a copy in which about 2 % of positions are redrawn at random. Compare the exact Jaccard index of their 15-mer sets with a MinHash estimate from 200 hash functions, and explain the gap.

> [!success]- Solution
> ```python
> import hashlib
> import random
>
> def h(seed: int, kmer: str) -> int:          # the seed-th hash function (64 bits of SHA-1)
>     return int.from_bytes(hashlib.sha1(f"{seed}:{kmer}".encode()).digest()[:8], "big")
>
> def minhash_jaccard(x: set, y: set, n_hashes: int = 200) -> float:
>     agree = sum(min(x, key=lambda w: h(i, w)) == min(y, key=lambda w: h(i, w))
>                 for i in range(n_hashes))
>     return agree / n_hashes
>
> random.seed(1)
> g1 = "".join(random.choice("ACGT") for _ in range(2000))
> g2 = "".join(random.choice("ACGT") if random.random() < 0.02 else b for b in g1)
> k1, k2 = kmer_set(g1, 15), kmer_set(g2, 15)
> print(len(k1), len(k2), round(jaccard(k1, k2), 3), minhash_jaccard(k1, k2))
> ```
> Output: `1986 1986 0.649 0.625`. The standard error is $\sqrt{0.649 \times 0.351 / 200} \approx 0.034$, so an estimate 0.024 below the truth is within one standard error. Quadrupling the number of hash functions halves the error.

## Mastery checklist

- [ ] 1 Recognized: I can read $\in$, $\subseteq$, $\cup$, $\cap$, $\setminus$, $^c$, $\times$ and $\mathcal{P}$.
- [ ] 2 Understood: I can explain why a complement needs a universe, why sets lose counts, and prove De Morgan's laws by element chasing.
- [ ] 3 Practiced: I compute overlaps, inclusion-exclusion counts and Jaccard indices by hand and with Python sets.
- [ ] 4 Applied: in [[05-sequence-search]], I compared real sequences through their (canonical) k-mer sets and chose $k$ deliberately.
- [ ] 5 Explained: I can teach how the choice of universe drives overlap statistics and why MinHash estimates the Jaccard index.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, proofs part (sets, functions, relations).
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], fundamental-concepts third of the course (sets, functions, relations).
[^iupac]: [[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]], *Nucleic Acids Research* (the 15 one-letter nucleotide codes).
[^bed]: [[GA4GH hts-specs]], `BEDv1` specification (0-based, half-open coordinates).
