---
aliases:
  - Reverse Complementation
  - Revcomp
  - Opposite Strand
  - Complément inverse
tags:
  - type/concept
  - domain/bioinformatics
  - domain/biology
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[DNA]]"
  - "[[Nucleotide]]"
  - "[[Base Pairing]]"
  - "[[IUPAC Nucleotide Code]]"
  - "[[String]]"
related:
  - "[[GC Content]]"
  - "[[K-mer]]"
  - "[[Sequence Motif]]"
  - "[[Exact Pattern Matching]]"
  - "[[Restriction Enzyme]]"
  - "[[Read Mapping]]"
  - "[[Genomic Coordinate System]]"
  - "[[Rolling Hash]]"
projects:
  - "[[01-dna-engine]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
---

# Reverse Complement

> [!abstract]
> The reverse complement of a DNA sequence is the other strand of the double helix, written in the same 5' to 3' direction as every sequence in a file; computing it, and searching it, is the reflex that stops half of the genome from being missed.

## Definition

The **reverse complement** $\mathrm{rc}(s)$ of a nucleotide sequence $s$ is obtained by replacing each base by its pairing partner (A↔T, C↔G) and reversing the order. Because the two strands of DNA are complementary and antiparallel,[^openstax] $\mathrm{rc}(s)$ is exactly the sequence of the partner strand read 5' → 3'. The formula and its algebraic properties (involution, $\mathrm{rc}(uv) = \mathrm{rc}(v)\,\mathrm{rc}(u)$) are proved in [[DNA#Mathematical representation]]; this note is about using it.

## Why it matters

- **Biology uses both strands.** Different genes use different strands as template,[^alberts] so a gene annotated on the `-` strand of a [[GFF Format|GFF]] file must be reverse-complemented before its codons are read ([[Genetic Code]], [[Reading Frame]]).
- **Signals come in both orientations.** In the replication origin of *Vibrio cholerae*, the 9-mer `ATGATCAAG` occurs three times and its reverse complement `CTTGATCAT` three more times; counting only one strand would hide half of the signal that marks the DnaA boxes.[^compeau]
- **Reads come from either strand.** A sequencing library contains both strands of each fragment, so a read may match the reference or its reverse complement: [[Read Mapping]] and [[Genome Assembly]] try both.
- **Primers.** A reverse primer anneals to the top strand and is extended 5' → 3', so it is written as the reverse complement of the top-strand region it binds ([[Polymerase Chain Reaction]], [[DNA Replication]]).
- **Lab.** `reverse_complement` is a core function of [[01-dna-engine]]; strand-aware search is required in [[05-sequence-search]].

## Core (L1)

```text
top      5'-ATGCGTACC-3'
            |||||||||
bottom   3'-TACGCATGG-5'   (complement, read right to left)
rc(top)  5'-GGTACGCAT-3'   (the bottom strand in file orientation)
```

1. **Two steps, any order.** Complement then reverse, or reverse then complement: the result is the same, since complementing acts base by base.
2. **Neither step alone is enough.** The complement `TACGCATGG` is written 3' → 5'; the reverse `CCATGCGTA` is not the sequence of either strand.
3. **Involution.** $\mathrm{rc}(\mathrm{rc}(s)) = s$: applying it twice returns the original, a useful unit test.
4. **Ambiguity codes and case.** Each [[IUPAC Nucleotide Code|IUPAC code]] has a defined complement (R↔Y, K↔M, B↔V, D↔H; S, W and N are their own complements).[^iupac] Lowercase (soft-masked) letters should stay lowercase.
5. **RNA.** For RNA, A pairs with U: $\mathrm{rc}$(`AUGGCUUAA`) = `UUAAGCCAU`.

## Deeper (L2)

**Searching both strands without copying the genome.** A pattern $p$ occurs on the minus strand exactly where $\mathrm{rc}(p)$ occurs on the plus strand. So a both-strand search scans the text once for $p$ and $\mathrm{rc}(p)$; there is no need to build $\mathrm{rc}(\text{genome})$. This is how [[Exact Pattern Matching]] and motif scans ([[Sequence Motif]]) are made strand-aware.

**Coordinates.** Report every hit in plus-strand coordinates with a strand label, as [[BED Format]] and [[GFF Format]] do. If $p$ (length $k$) starts at 0-based position $j$ of $\mathrm{rc}(s)$, with $n = |s|$, it covers the plus-strand interval $[n - j - k,\ n - j)$ ([[Genomic Coordinate System]]).

**Reverse palindromes.** A site equal to its own reverse complement reads the same on both strands, like the EcoRI site `GAATTC`; many such sites are bound by proteins acting as symmetric dimers, as restriction enzymes do.[^alberts] A both-strand search must report such a hit once, not twice. Palindromes have even length ([[DNA#Mathematical representation]]), and there are $4^{k/2}$ of them among the $4^k$ k-mers (Exercise 5).

**Canonical form.** When the strand is unknown, a k-mer and its reverse complement describe the same double-stranded site; storing the lexicographically smaller one, the **canonical k-mer**, merges both ([[K-mer]]).

## Advanced (L3)

- **Bit-level reverse complement.** With the 2-bit code A=00, C=01, G=10, T=11 ([[Nucleotide#Mathematical representation]]), complementing a packed k-mer is one XOR with all ones; reversing means reversing the order of the 2-bit groups. Fast k-mer counters rely on this.
- **Rolling canonical k-mers.** Sliding along a sequence, the forward k-mer gains a base at its 3' end while the reverse-complement k-mer gains the complement at its 5' end. Both values update in $O(1)$ per position, so canonical k-mers of a whole genome cost $O(n)$, the basis of canonical [[Rolling Hash|rolling hashes]] and [[Minimizer|minimizers]].
- **Strand as metadata, not data.** Aligners and annotation formats keep one reference orientation and record the strand of each feature or read; see [[SAM Format]] for how a read aligned to the reverse strand is stored. Mixing up the two conventions (sequence already reverse-complemented or not) is a classic source of silent errors.

## Mathematical representation

Let $c$ be the complement on $\Sigma = \{A, C, G, T\}$ and $\mathrm{rc}(s)_i = c(s_{n+1-i})$ ([[DNA#Mathematical representation]]). For a pattern $p$ of length $k$, write $\mathrm{Occ}(p, s) = \{ i : s_{i+1} \dots s_{i+k} = p \}$ (0-based starts).

- **Minus-strand occurrences.** $j \in \mathrm{Occ}(p, \mathrm{rc}(s)) \iff n - j - k \in \mathrm{Occ}(\mathrm{rc}(p), s)$. Proof: the window of $\mathrm{rc}(s)$ starting at $j$ is the reverse complement of the window of $s$ starting at $n - j - k$, and $\mathrm{rc}$ is a bijection.
- **Both-strand hits** of $p$ in $s$: $\mathrm{Occ}(p, s) \cup \mathrm{Occ}(\mathrm{rc}(p), s)$, with strand labels; the two sets coincide when $p = \mathrm{rc}(p)$.
- **Counting palindromes.** For even $k$, $p = \mathrm{rc}(p)$ fixes the second half from the first: $4^{k/2}$ palindromic k-mers. For odd $k$ there are none.
- **IUPAC codes** are sets $S \subseteq \Sigma$ with complement $c(S) = \{c(x) : x \in S\}$ ([[Nucleotide#Mathematical representation]]).

## Computational representation

```python
# IUPAC complements (NC-IUB 1984), upper- and lowercase; U complements to A.
DNA_COMP = str.maketrans("ACGTURYSWKMBDHVNacgturyswkmbdhvn",
                         "TGCAAYRSWMKVHDBNtgcaayrswmkvhdbn")


def reverse_complement(seq: str, rna: bool = False) -> str:
    """The partner strand read 5'->3'. With rna=True, A pairs with U."""
    rc = seq.translate(DNA_COMP)[::-1]
    return rc.replace("T", "U").replace("t", "u") if rna else rc


def find_both_strands(text: str, pattern: str) -> list[tuple[int, str]]:
    """0-based start of every occurrence on + or - strand, in + strand coordinates.
    A reverse palindrome (pattern == its reverse complement) is reported once, as '+/-'."""
    rc = reverse_complement(pattern)
    k, hits = len(pattern), []
    for i in range(len(text) - k + 1):
        window = text[i:i + k]
        if window == pattern and window == rc:
            hits.append((i, "+/-"))
        elif window == pattern:
            hits.append((i, "+"))
        elif window == rc:
            hits.append((i, "-"))
    return hits


print(reverse_complement("ATGCRYNacgt"))
print(reverse_complement("AUGGCUUAA", rna=True))
text = "CTTGATCATAGGAATTCCATGATCAAGT"          # invented toy sequence
print(find_both_strands(text, "ATGATCAAG"))
print(find_both_strands(text, "GAATTC"))
```

```text
acgtNRYGCAT
UUAAGCCAU
[(0, '-'), (18, '+')]
[(11, '+/-')]
```

`str.translate` and slicing are both $O(n)$. The naive scan is $O(nk)$; any faster exact matcher ([[Knuth-Morris-Pratt Algorithm]], [[Aho-Corasick Algorithm]] for $\{p, \mathrm{rc}(p)\}$ at once) drops in unchanged.

## Worked example

> [!example] One site, two strands (toy sequence, invented)
> Text `5'-CTTGATCATAGGAATTCCATGATCAAGT-3'` ($n = 28$), pattern $p$ = `ATGATCAAG` ($k = 9$), $\mathrm{rc}(p)$ = `CTTGATCAT`.
> 1. **Plus strand**: $p$ starts at position 18.
> 2. **Minus strand**: $\mathrm{rc}(p)$ starts at position 0, so $p$ lies on the minus strand over $[0, 9)$.
> 3. **Check with the lemma**: $\mathrm{rc}(\text{text})$ = `ACTTGATCATGGAATTCCTATGATCAAG` contains $p$ at $j = 19$, and $n - j - k = 28 - 19 - 9 = 0$.
> 4. **Palindrome**: `GAATTC` at position 11 equals its reverse complement, so it is one site seen from both strands.

## Common misconceptions

> [!warning] "To search the minus strand, reverse-complement the genome"
> Reverse-complement the **pattern** and scan the same text: same result, no copy of a gigabase genome, and hits come out directly in plus-strand coordinates.

> [!warning] "A palindromic site is found twice"
> A reverse palindrome occupies the same interval on both strands. Counting it twice inflates motif counts; report it once with both strands.

> [!warning] "Minus-strand coordinates count from the other end"
> Files report minus-strand features in plus-strand coordinates plus a strand column. A position measured along $\mathrm{rc}(s)$ must be converted with $n - j - k$ before it is written out.

## Exercises

> [!question] Exercise 1 (L1)
> Write the reverse complement of `5'-GARTTNCa-3'` (IUPAC codes, soft-masked last base), then of the RNA `5'-GGCUAC-3'`.

> [!success]- Solution
> Complements: G→C, A→T, R→Y, T→A, T→A, N→N, C→G, a→t; reversed: `tGNAAYTC`. RNA: complement CCGAUG, reversed `GUAGCC`. Check: `reverse_complement("GARTTNCa")` prints `tGNAAYTC`.

> [!question] Exercise 2 (L1)
> A PCR target is `5'-AGCTTGCAGGTCAATGCCTT...GGATCCAAGTGCTAACGTAT-3'` (top strand shown). Write 10-nt forward and reverse primers for its two ends, both 5' → 3'.

> [!success]- Solution
> Forward primer = the first 10 bases of the top strand: `AGCTTGCAGG`. The reverse primer anneals to the last 10 bases `GCTAACGTAT` of the top strand, so it is their reverse complement: `ATACGTTAGC`.

> [!question] Exercise 3 (L2)
> Prove that if $p$ occurs at 0-based position $j$ in $\mathrm{rc}(s)$ then $\mathrm{rc}(p)$ occurs at $n - j - k$ in $s$.

> [!success]- Solution
> Write $s = u\,x\,v$ with $|x| = k$ and $|u| = n - j - k$. Then $\mathrm{rc}(s) = \mathrm{rc}(v)\,\mathrm{rc}(x)\,\mathrm{rc}(u)$, and $|\mathrm{rc}(v)| = n - |u| - k = j$, so the window of $\mathrm{rc}(s)$ at $j$ is $\mathrm{rc}(x)$. It equals $p$ iff $x = \mathrm{rc}(p)$, by the involution.

> [!question] Exercise 4 (L3, Python)
> Write a generator of canonical k-mers that updates the packed forward and reverse-complement values in $O(1)$ per base (2-bit code A=0, C=1, G=2, T=3). Test it on `GATTACA` with $k = 5$.

> [!success]- Solution
> ```python
> TWO_BIT = {"A": 0, "C": 1, "G": 2, "T": 3}
>
>
> def unpack(value: int, k: int) -> str:
>     return "".join("ACGT"[(value >> 2 * (k - 1 - i)) & 3] for i in range(k))
>
>
> def canonical_kmers(seq: str, k: int):
>     """Yield (position, canonical packed k-mer), updating forward and reverse values in O(1) per base."""
>     mask = (1 << 2 * k) - 1
>     fwd = rev = 0
>     for i, base in enumerate(seq):
>         code = TWO_BIT[base]
>         fwd = ((fwd << 2) | code) & mask               # append the base at the 3' end
>         rev = (rev >> 2) | ((3 - code) << 2 * (k - 1))  # prepend its complement at the 5' end
>         if i >= k - 1:
>             yield i - k + 1, unpack(fwd, k), unpack(rev, k), unpack(min(fwd, rev), k)
>
>
> for row in canonical_kmers("GATTACA", 5):
>     print(row)
> ```
> ```text
> (0, 'GATTA', 'TAATC', 'GATTA')
> (1, 'ATTAC', 'GTAAT', 'ATTAC')
> (2, 'TTACA', 'TGTAA', 'TGTAA')
> ```
> The complement of code $x$ is $3 - x$ (that is, $x \oplus 11$). Numeric order of packed values equals lexicographic order with A < C < G < T, so `min` returns the canonical k-mer without decoding.

> [!question] Exercise 5 (L3)
> How many reverse-palindromic 6-mers exist? In a random sequence with uniform, independent bases, how often do you expect the site `GAATTC`, and why does a both-strand search for it not double the rate?

> [!success]- Solution
> $4^{6/2} = 64$ palindromic 6-mers, 1 in 64 of all 4096 6-mers. The probability that a given position starts `GAATTC` is $4^{-6} = 1/4096$, so about one site every 4 kb. Searching for $\mathrm{rc}(p)$ adds nothing because $\mathrm{rc}(p) = p$: the minus-strand occurrences are the plus-strand ones. For a non-palindromic 6-mer, the both-strand rate is $2/4096$.

## Mastery checklist

- [ ] 1 Recognized: I can say why the other strand is the reverse complement and not the complement.
- [ ] 2 Understood: I can explain both-strand search, the coordinate conversion and why palindromes are counted once.
- [ ] 3 Practiced: I can implement reverse complement with IUPAC codes, case and RNA, and a strand-aware search.
- [ ] 4 Applied: in [[01-dna-engine]] and [[05-sequence-search]], my functions return the same hits on a real genome and on its reverse complement (with converted coordinates).
- [ ] 5 Explained: I can explain packed and rolling canonical k-mers, and the strand conventions of annotation and alignment files.

## References

[^openstax]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function".
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002).
[^iupac]: [[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]], *Nucleic Acids Research*.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?".
