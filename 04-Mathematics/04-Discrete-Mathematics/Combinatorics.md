---
aliases:
  - Counting
  - Enumerative Combinatorics
  - Sum Rule
  - Product Rule
  - Rule of Product
  - Combinatoire
  - Dénombrement
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Set]]"
  - "[[Function]]"
  - "[[Summation Notation]]"
related:
  - "[[Permutation]]"
  - "[[Binomial Coefficient]]"
  - "[[Pigeonhole Principle]]"
  - "[[Inclusion-Exclusion Principle]]"
  - "[[K-mer]]"
  - "[[Genetic Code]]"
  - "[[Probability]]"
projects:
  - "[[01-dna-engine]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
---

# Combinatorics

> [!abstract]
> Combinatorics counts the elements of a finite set without listing them: add the sizes of disjoint cases, multiply the numbers of successive choices, and you know how many DNA sequences, peptides or k-mers exist before writing a single loop.

## Definition

**Enumerative combinatorics** determines the size $|S|$ of a finite set $S$ from its structure. Its two basic rules are:[^lehman][^mcs]

- **Sum rule.** If $A_1, \dots, A_n$ are pairwise disjoint finite sets, $|A_1 \cup \dots \cup A_n| = |A_1| + \dots + |A_n|$.
- **Product rule.** For finite sets $A_1, \dots, A_n$, $|A_1 \times \dots \times A_n| = |A_1| \cdot |A_2| \cdots |A_n|$.

The other counting tools of the [[Discrete Mathematics]] path ([[Permutation|permutations]], [[Binomial Coefficient|binomial coefficients]], the [[Pigeonhole Principle|pigeonhole]] and [[Inclusion-Exclusion Principle|inclusion-exclusion]] principles) are built from these two rules plus bijections.

## Why it matters

- **Size of sequence space.** The number of possible sequences, k-mers or peptides decides whether an exhaustive search is feasible or whether an index, a heuristic or a statistical model is needed ([[Big O Notation]]).
- **Uniqueness.** Whether a 12-mer, a primer or a read seed can identify one place in a genome is first a counting question (Core section below).
- **Probabilities.** On a finite sample space of equally likely outcomes, a probability is a ratio of two counts ([[Probability]]).
- **Data structures.** There are $4^k$ possible k-mers,[^compeau] so a dense table indexed by k-mers needs $4^k$ cells: 16,384 for $k = 7$, about $1.1 \times 10^{12}$ for $k = 20$ ([[K-mer]], [[Hash Function]], [[05-sequence-search]]).

## Core (L1)

**Sum rule.** If every object falls into exactly one of several cases, count each case and add. DNA words of length at most 3 (the empty word included) split by length into $\Sigma^0, \Sigma^1, \Sigma^2, \Sigma^3$, so there are $1 + 4 + 16 + 64 = 85$ of them.

**Product rule.** A DNA sequence of length $n$ is an element of $\Sigma^n = \Sigma \times \dots \times \Sigma$ with $\Sigma = \{A, C, G, T\}$ ([[Set]]): $n$ choices among 4 letters, hence $4^n$ sequences. The same rule gives the 64 codons ($4^3$) and, with the 20 standard amino acids,[^os15] $20^n$ peptides of length $n$: 3,200,000 pentapeptides.

**Generalized product rule.** The options at a step may depend on earlier choices, as long as their *number* does not.[^lehman] DNA strings of length $n$ with no two equal neighbours: 4 choices for the first base, then 3 for each next base (anything but its left neighbour), so $4 \cdot 3^{n-1}$ (Exercise 2).

### Bio: why a 12-mer repeats but a 20-mer is usually unique

A one-strand human assembly has about $G = 3.055 \times 10^9$ positions,[^nurk] hence $G - k + 1$ windows of length $k$.

| $k$ | possible k-mers $4^k$ | windows per possible k-mer | consequence |
|---:|---:|---:|---|
| 12 | 16,777,216 | 182.09 | some 12-mer **must** occur at least 183 times |
| 16 | 4,294,967,296 | 0.71 | about as many possible k-mers as positions |
| 20 | 1,099,511,627,776 | 0.0028 | most possible 20-mers occur nowhere |

- For $k = 12$ there are more windows than possible 12-mers, so by the [[Pigeonhole Principle]] some 12-mer occurs at least $\lceil (G - 11)/4^{12} \rceil = 183$ times. This is a theorem, not a statistical tendency: 12-mers cannot, in general, identify a position.
- For $k = 20$ counting no longer forces repeats: there are about 360 times more possible 20-mers than positions. If the genome were a uniformly random sequence, a given 20-mer starting at one position would occur at another position with probability about 0.003, so most 20-mers would be unique. Real genomes contain repeated sequences such as [[Transposable Element|transposable elements]], which carry the same 20-mers many times,[^lander] hence "usually" unique. Expected counts for every $k$ are in [[K-mer#Deeper (L2)]].

## Deeper (L2)

- **Bijection rule.** If there is a bijection $f : A \to B$, then $|A| = |B|$ ([[Function]]).[^lehman] Reading a k-mer as a base-4 number is a bijection $\Sigma^k \to \{0, \dots, 4^k - 1\}$ ([[Hash Function]]); a subset corresponds to its indicator vector, giving $2^n$ subsets of an $n$-set ([[Set#Mathematical representation]]).
- **Division rule.** If $f : A \to B$ is $k$-to-1 (every element of $B$ has exactly $k$ preimages), then $|A| = k\,|B|$.[^lehman] The ordered pairs $(u, v)$ of distinct proteins among $n$ number $n(n-1)$ and map 2-to-1 onto unordered pairs $\{u, v\}$, so an interaction network on $n$ proteins has at most $n(n-1)/2$ edges ([[Graph]], [[Binomial Coefficient]]).
- **Complement rule.** Count what you do not want and subtract (the sum rule applied to $A$ and $U \setminus A$): 8-mers containing at least one G or C number $4^8 - 2^8 = 65{,}280$.
- **Constraints per position.** Coding sequences of $m$ codons with no in-frame stop codon: $61^m$ among $64^m$, a fraction $(61/64)^m$, the starting point of open-reading-frame statistics ([[Genetic Code#Mathematical representation]]).
- **Reverse translation.** A protein $a_1 \dots a_\ell$ followed by a stop is encoded by $3 \prod_i d(a_i)$ DNA sequences, where $d(a)$ is the number of codons of amino acid $a$ in the code used ([[Genetic Code]]); in the standard table Leu, Ser and Arg each have 6.[^ncbi]

## Advanced (L3)

- **Counting decides the algorithm.** A table of $4^{12} \approx 1.7 \times 10^7$ counters is small, but the $20^{10} \approx 10^{13}$ decapeptides cannot be listed one by one. Pairwise alignments and tree topologies grow even faster ([[Binomial Coefficient]], [[Tree (Graph Theory)]]), which is why alignment uses [[Dynamic Programming]] and phylogenetic tree search is heuristic.
- **Double counting.** Counting one set in two ways proves identities: incidences give the handshake lemma ([[Graph]]), subsets split by one element give Pascal's rule ([[Binomial Coefficient]]), and windows grouped by k-mer give $\sum_w \mathrm{Count}_s(w) = n - k + 1$ ([[K-mer#Mathematical representation]]).
- **When the division rule fails.** Circular DNA words up to rotation (a plasmid read from an arbitrary origin) are not $4^n/n$ in general: $4^3/3$ is not even an integer. For $n = 3$, the 4 constant words (`AAA`, ...) are their own rotations, while every other word has 3 distinct rotations (two equal rotations would make it periodic with a period dividing 3, hence constant): $4 + 60/3 = 24$ classes. Classes of unequal sizes are counted with group actions, beyond this note.

## Mathematical representation

- **Product rule from the sum rule.** $A \times B = \bigcup_{a \in A} \{a\} \times B$ is a union of $|A|$ disjoint sets, each in bijection with $B$ via $b \mapsto (a, b)$, so $|A \times B| = \sum_{a \in A} |B| = |A|\,|B|$. Induction on $n$ ([[Mathematical Induction]]) extends it to $A_1 \times \dots \times A_n$.
- **Words and functions.** A word of length $n$ over $\Sigma$ is a function $\{1, \dots, n\} \to \Sigma$, and $|B^A| = |B|^{|A|}$ (one independent choice in $B$ per element of $A$). Hence $|\Sigma^n| = |\Sigma|^n$.
- **Generalized product rule.** If a set $S$ of sequences $(x_1, \dots, x_n)$ has $c_1$ choices for $x_1$ and, for every choice of $x_1, \dots, x_{i-1}$, exactly $c_i$ choices for $x_i$, then $|S| = c_1 c_2 \cdots c_n$.
- **Division rule.** If $f : A \to B$ satisfies $|f^{-1}(b)| = k$ for every $b \in B$, then $|A| = \sum_{b \in B} |f^{-1}(b)| = k\,|B|$ (sum rule over the disjoint preimages).

## Computational representation

`itertools.product` enumerates $\Sigma^n$, so every counting formula can be checked by brute force for small $n$ before trusting it for large $n$.

```python
from itertools import product
from math import ceil, log

DNA = "ACGT"

def count_words(alphabet: str, n: int) -> int:
    """|alphabet^n| by enumeration, to check the product rule."""
    return sum(1 for _ in product(alphabet, repeat=n))

print([count_words(DNA, n) for n in range(1, 6)], [4**n for n in range(1, 6)])
print(f"peptides of length 5: {20**5:,}")

# Sum rule: words of length 0..n form a disjoint union
n = 3
print(sum(4**k for k in range(n + 1)), (4**(n + 1) - 1) // 3)

# k-mers versus positions in a genome of G bp (one strand)
G = 3_055_000_000                      # human T2T-CHM13, about 3.055e9 bp
for k in (12, 16, 20):
    windows = G - k + 1
    forced = ceil(windows / 4**k)      # pigeonhole: some k-mer occurs at least this often
    print(k, f"{4**k:,}", forced, round(windows / 4**k, 4))
print(round(log(G, 4), 2))
```

```text
[4, 16, 64, 256, 1024] [4, 16, 64, 256, 1024]
peptides of length 5: 3,200,000
85 85
12 16,777,216 183 182.0922
16 4,294,967,296 1 0.7113
20 1,099,511,627,776 1 0.0028
15.75
```

A forced multiplicity of 1 means counting forces nothing. $\log_4 G \approx 15.75$ is the length at which possible k-mers start to outnumber positions.

## Worked example

> [!example] How many DNA sequences encode Met-Leu-Ser-Trp-stop?
> 1. **Choices per position** in the standard code:[^ncbi] Met 1 codon (ATG), Leu 6, Ser 6, Trp 1 (TGG), stop 3 (TAA, TAG, TGA).
> 2. **Independence.** The codon chosen for one position does not change the number of options at the others, so the product rule applies: $1 \cdot 6 \cdot 6 \cdot 1 \cdot 3 = 108$.
> 3. **Check by enumeration**, building the synonym lists from the NCBI table string ([[Genetic Code#Computational representation]]):
> ```python
> from itertools import product
> from math import prod
>
> BASES = "TCAG"
> TABLE = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
> CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]
> synonyms = {}
> for codon, aa in zip(CODONS, TABLE):
>     synonyms.setdefault(aa, []).append(codon)
>
> def n_encodings(protein: str) -> int:
>     return prod(len(synonyms[aa]) for aa in protein)
>
> def enumerate_encodings(protein: str) -> set[str]:
>     return {"".join(c) for c in product(*(synonyms[aa] for aa in protein))}
>
> print(n_encodings("MLSW*"), len(enumerate_encodings("MLSW*")))   # 108 108
> ```
> 4. **Interpretation.** A protein of a few hundred residues has an astronomically large set of possible coding sequences; which one an organism uses is a biological question ([[Codon Usage Bias]]).

## Common misconceptions

> [!warning] "Add the counts of the cases"
> Only if the cases are disjoint. Genes found by screen A plus genes found by screen B double-counts the genes found by both: use the [[Inclusion-Exclusion Principle]].

> [!warning] "If $4^k$ exceeds the genome length, every k-mer in it is unique"
> Counting only *allows* uniqueness. Repeats make some 20-mers occur thousands of times;[^lander] uniqueness must be checked on the actual genome.

> [!warning] "The product rule needs the same options at every step"
> Only the *number* of options must be independent of earlier choices (generalized product rule). "No two equal neighbours" has different allowed bases at each step but always 3 of them.

## Exercises

> [!question] Exercise 1 (L1)
> How many DNA words of length 1 to 4 are there? How many DNA 6-mers start with ATG, contain no A, contain at least one A?

> [!success]- Solution
> Sum rule over lengths: $4 + 16 + 64 + 256 = 340$. Starting with ATG: three free bases, $4^3 = 64$. No A: $3^6 = 729$. At least one A, by complement: $4^6 - 3^6 = 3367$.

> [!question] Exercise 2 (L2, Python)
> Prove that there are $4 \cdot 3^{n-1}$ DNA strings of length $n \ge 1$ with no two equal adjacent bases, and check it by enumeration for $n = 1, \dots, 6$.

> [!success]- Solution
> Generalized product rule: 4 choices for $x_1$; for each $i \ge 2$, whatever $x_{i-1}$ is, exactly 3 bases differ from it.
> ```python
> from itertools import product
>
> def no_repeat_neighbours(n: int) -> int:
>     return sum(1 for w in product("ACGT", repeat=n) if all(a != b for a, b in zip(w, w[1:])))
>
> print([no_repeat_neighbours(n) for n in range(1, 7)], [4 * 3**(n - 1) for n in range(1, 7)])
> ```
> Output: `[4, 12, 36, 108, 324, 972] [4, 12, 36, 108, 324, 972]`.

> [!question] Exercise 3 (L2)
> How many DNA sequences encode Met-Lys-Leu-Trp followed by a stop codon in the standard code?

> [!success]- Solution
> Lys has 2 codons (AAA, AAG), so $1 \cdot 2 \cdot 6 \cdot 1 \cdot 3 = 36$; `n_encodings("MKLW*")` and the enumeration of the worked example both return 36.

> [!question] Exercise 4 (L3)
> For the *E. coli* K-12 chromosome (4,639,221 bp)[^blattner] and the human assembly ($3.055 \times 10^9$ bp), find the smallest $k$ with $4^k \ge G$, and the number of times some 12-mer is forced to occur. What changes between the two genomes?

> [!success]- Solution
> $4^{11} = 4{,}194{,}304 < 4{,}639{,}221 \le 4^{12}$, so $k = 12$ for *E. coli*; $4^{15} \approx 1.07 \times 10^9 < 3.055 \times 10^9 \le 4^{16}$, so $k = 16$ for human. Forced multiplicity of 12-mers: $\lceil (G - 11)/4^{12} \rceil$ = 1 for *E. coli* (nothing forced) and 183 for human. A 12-mer probe can in principle be unique in a bacterial genome but never in every case in a human one.

## Mastery checklist

- [ ] 1 Recognized: I can state the sum and product rules and say how many DNA sequences of length $n$ exist.
- [ ] 2 Understood: I can explain why a 12-mer must repeat in the human genome while a 20-mer usually does not, and why "usually".
- [ ] 3 Practiced: I can apply the generalized product, bijection, division and complement rules, and check a count by enumeration in Python.
- [ ] 4 Applied: I sized a k-mer table and chose $k$ for seeds in [[05-sequence-search]] from these counts.
- [ ] 5 Explained: I can teach when each rule applies, including why rotation classes break the division rule.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, treatment of counting: sum and product rules, generalized product rule, bijection and division rules.
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], counting part of the discrete structures third.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (k-mers and their number).
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (the genetic code: 64 codons, 20 amino acids).
[^ncbi]: [[NCBI Genetic Codes]], translation table 1 (standard code).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*.
[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]], *Nature*, analysis of repeats and transposable elements.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science*.
