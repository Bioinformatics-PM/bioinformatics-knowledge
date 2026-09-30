---
aliases:
  - IUPAC Code
  - IUPAC Ambiguity Code
  - Nucleotide Ambiguity Code
  - Degenerate Base
  - Code IUPAC des nucléotides
tags:
  - type/concept
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Nucleotide]]"
  - "[[DNA]]"
  - "[[Set]]"
related:
  - "[[FASTA Format]]"
  - "[[Reverse Complement]]"
  - "[[GC Content]]"
  - "[[Sequence Motif]]"
  - "[[Regular Expression]]"
  - "[[Genetic Code]]"
  - "[[Base Calling]]"
  - "[[Shannon Entropy]]"
  - "[[Sequence Logo]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-core]]"
  - "[[02-sequence-translation]]"
sources:
  - "[[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]]"
  - "[[NCBI BLAST]]"
  - "[[NCBI Genetic Codes]]"
---

# IUPAC Nucleotide Code

> [!abstract]
> Sequence files use more letters than A, C, G and T: R means "A or G", Y means "C or T", N means "any base". A good program reads these letters as sets of possible bases instead of rejecting the sequence.

## Definition

The **IUPAC nucleotide codes** are the one-letter symbols recommended by the Nomenclature Committee of the International Union of Biochemistry (1984) for bases in nucleic acid sequences, including **incompletely specified** bases: besides A, C, G and T, eleven symbols each stand for a set of two, three or four bases (for example R = A or G, Y = C or T, N = any base), and each symbol has a defined complement.[^iupac] NCBI expects sequences in these standard codes, lists U (uracil) with them, and accepts a hyphen for a gap of indeterminate length.[^ncbi]

The full table, with mnemonics and a bit-mask implementation of matching and complement, is in [[Nucleotide#Computational representation]]; this note is about **using** the codes: validating, interpreting and computing with them.

## Why it matters

- **Real data contain them.** NCBI's own advice for an unknown base is to write N,[^ncbi] so genome and read files contain N and other codes. A validator that accepts only `ACGT` rejects valid data: getting this right is the first task of [[01-dna-engine]].
- **Every computation needs a policy.** [[GC Content]], [[K-mer]] counting, motif search, [[Reverse Complement]] and translation all have to decide what an ambiguous symbol means. The choice must be explicit and documented.

## Core (L1)

Each code is a non-empty set of bases; ordering the sets by inclusion gives four levels, from the concrete bases to N:[^iupac]

![[iupac-code-lattice.svg]]

- **1 base**: A, C, G, T. **2 bases**: R, Y, S, W, K, M. **3 bases**: B, D, H, V, each meaning "not" one base (B = not A, D = not C, H = not G, V = not T). **4 bases**: N.[^iupac]
- $2^4 - 1 = 15$ non-empty subsets of $\{A, C, G, T\}$, hence exactly 15 symbols.

**Validating a nucleotide sequence** means sorting every character into one of four classes, not two:

| Character | Class | Action |
|---|---|---|
| `A C G T` | concrete base | accept |
| `R Y S W K M B D H V N` | ambiguity code | accept, count, report |
| `a c g t n ...` | lowercase | accept; NCBI reads lowercase as uppercase[^ncbi] |
| `U` | uracil | accept for RNA (or map to T when comparing with DNA)[^ncbi] |
| `-` | gap | accept only where gaps are allowed (alignments)[^ncbi] |
| digits, spaces | not sequence | reject; NCBI asks for digits to be removed or replaced by N[^ncbi] |
| `E F I L P Q X *` ... | not a nucleotide code | reject: probably a protein sequence or a corrupted file |

**Interpret, do not delete.** An N is a real position whose base is unknown. Removing it would shorten the sequence and shift every later coordinate by one; keeping it preserves positions, and the code states exactly what is known.

## Deeper (L2)

**Operations on codes.** Writing $\delta(c)$ for the set a code stands for:

- a concrete base $x$ **matches** $c$ if $x \in \delta(c)$;
- two codes are **compatible** (they could denote the same base) if $\delta(c) \cap \delta(c') \neq \emptyset$: R and K are (both allow G), R and Y are not;
- the **consensus** of an alignment column is the smallest code containing every observed base, the union: A and G give R, all four give N;
- the **complement** of a code is the code of the complemented set: R ↔ Y, K ↔ M, B ↔ V, D ↔ H, while S, W and N are their own complements.[^iupac]

**Statistics with ambiguity.** Three policies for a quantity such as GC content:

1. **Exclude** ambiguous positions (the choice made in [[DNA#Computational representation]]): simple, but undefined when no position is concrete.
2. **Expected value**: each code shares its weight equally among its bases (S counts 1 toward G+C, R counts 1/2, N counts 1/2).
3. **Bounds**: the minimum and maximum over all resolutions of the ambiguous positions.

The three can differ widely (Worked example): two programs can both be right and still disagree on a sequence with many N, unless each states its policy.

**Pattern search.** An IUPAC pattern such as `GAYNRTC` (an invented motif) becomes a [[Regular Expression]] by replacing each ambiguity code with a character class: `GA[CT][ACGT][AG]TC`. Search both strands, since the complement of a pattern is again an IUPAC pattern ([[Sequence Motif]]).

**Ambiguous codons.** Because the [[Genetic Code]] is degenerate, some ambiguous codons still translate to one amino acid: every codon of `GCN` codes for alanine, and `TAR` (TAA or TAG) is always a stop, while `ATN` mixes isoleucine and methionine and must become `X`.[^ncbi-gc] Translating codon by codon over the expanded set, and emitting `X` only when meanings disagree, loses less information than turning every ambiguous codon into `X` (Exercise 5).

## Advanced (L3)

- **A code says what, not why.** The 1984 recommendations name *incompletely specified* bases:[^iupac] a symbol records the set of possible bases, not the cause. R can mean an unresolved signal, a heterozygous A/G position in a diploid sample, or a mixture of sequences. Formats built for sequencing data keep the cause explicitly: per-base qualities ([[Phred Quality Score]], [[FASTQ Format]]) or alleles and genotypes ([[VCF Format]], [[Genotype]]).
- **From sets to probabilities.** A code is the special case of a probability distribution over $\{A, C, G, T\}$ that is uniform on a subset. Its information content, $\log_2 (4 / |S|)$ bits, equals $2 - H$ where $H = \log_2 |S|$ is the [[Shannon Entropy]] of that uniform distribution. Position weight matrices and [[Sequence Logo|sequence logos]] generalize this to arbitrary distributions per position ([[Sequence Motif]]).
- **Alphabets overlap.** Every nucleotide symbol except B also appears as a one-letter amino acid code in NCBI translation table 1 (A, C, G, T, N, R, Y and the others).[^ncbi-gc] A string such as `MKVLAAGG` is valid under both alphabets. Alphabet detection is therefore a heuristic: tools and formats should be told the molecule type rather than guess it.
- **Storage.** Compact encodings trade ambiguity away: a 2-bit code cannot store N, so a compact representation must keep ambiguous positions separately, for example as a list of intervals ([[Nucleotide#Exercises]]); a 4-bit set encoding keeps all 15 codes ([[Data Compression]]).

## Mathematical representation

- Let $\Sigma = \{A, C, G, T\}$ and $\mathcal{I}$ the 15 codes, with the decoding bijection $\delta : \mathcal{I} \to \mathcal{P}(\Sigma) \setminus \{\emptyset\}$.
- A code string $s = s_1 \dots s_n \in \mathcal{I}^n$ denotes the set of concrete sequences
$$L(s) = \delta(s_1) \times \dots \times \delta(s_n), \qquad |L(s)| = \prod_{i=1}^{n} |\delta(s_i)|.$$
- **Information**: $I(c) = \log_2 \dfrac{4}{|\delta(c)|}$ bits, and $\sum_i I(s_i) = \log_2 \dfrac{4^n}{|L(s)|}$: the information of a pattern is the log of how much it narrows down the $4^n$ possible sequences.
- **Order**: $(\mathcal{P}(\Sigma) \setminus \{\emptyset\}, \subseteq)$ is the partial order drawn above; the consensus of observed bases $B$ is its least upper bound, $\delta^{-1}(\bigcup_{x \in B} \{x\})$.
- **Expected GC** under the uniform-within-set model: $\mathbb{E}[\mathrm{GC}] = \dfrac{1}{n} \sum_i \dfrac{|\delta(s_i) \cap \{C, G\}|}{|\delta(s_i)|}$; the bounds are $\frac{1}{n}\#\{i : \delta(s_i) \subseteq \{C, G\}\}$ and $\frac{1}{n}\#\{i : \delta(s_i) \cap \{C, G\} \neq \emptyset\}$.
- **Ambiguous codon**: with a genetic code $g$, the codon $c_1 c_2 c_3$ translates to $a$ if $g(\delta(c_1) \times \delta(c_2) \times \delta(c_3)) = \{a\}$, and to `X` otherwise.

## Computational representation

A validator that reports instead of failing on the first unexpected letter, and the set operations of L2 (a `frozenset` per code; the bit-mask version is in [[Nucleotide]]):

```python
import math
import re
from collections import Counter

IUPAC = {   # NC-IUB codes: symbol -> set of bases it stands for
    "A": "A", "C": "C", "G": "G", "T": "T",
    "R": "AG", "Y": "CT", "S": "CG", "W": "AT", "K": "GT", "M": "AC",
    "B": "CGT", "D": "AGT", "H": "ACT", "V": "ACG", "N": "ACGT",
}
CODE_OF = {frozenset(bases): code for code, bases in IUPAC.items()}


def validate(seq: str, rna: bool = False, gaps: bool = False) -> dict:
    """Classify every symbol: concrete base, ambiguity code, gap, or invalid (with 1-based position)."""
    report = {"length": len(seq), "ambiguous": Counter(), "gaps": 0, "invalid": []}
    for i, raw in enumerate(seq, start=1):
        c = raw.upper()                      # lowercase is accepted, read as uppercase
        if rna and c == "U":
            c = "T"                          # RNA uracil plays the role of T
        if c in "ACGT":
            continue
        if c in IUPAC:
            report["ambiguous"][c] += 1
        elif gaps and c == "-":
            report["gaps"] += 1
        else:
            report["invalid"].append((i, raw))
    return report


def information_bits(code: str) -> float:
    """Bits of information a symbol carries about the base: log2(4 / |S|)."""
    return math.log2(4 / len(IUPAC[code]))


def expected_gc(seq: str) -> float:
    """Expected G+C fraction, each code sharing its weight equally among its bases."""
    return sum(sum(b in "CG" for b in IUPAC[c]) / len(IUPAC[c]) for c in seq.upper()) / len(seq)


def consensus(bases: str) -> str:
    """Smallest code containing every base observed in an alignment column."""
    return CODE_OF[frozenset(bases.upper())]


def compatible(x: str, y: str) -> bool:
    """Two symbols can denote the same base iff their sets intersect."""
    return bool(set(IUPAC[x]) & set(IUPAC[y]))


def to_regex(pattern: str) -> str:
    """IUPAC pattern -> regular expression with character classes."""
    return "".join(c if len(IUPAC[c]) == 1 else f"[{IUPAC[c]}]" for c in pattern.upper())


print(validate("ACGTNNRYacgt"))
print(validate("ACGU"), validate("ACGU", rna=True)["invalid"])
print(validate("ACG-TTX1", gaps=True))
print([round(information_bits(c), 3) for c in "ARBN"], round(expected_gc("ACGTNNRY"), 3))
print(consensus("AAG"), consensus("CT"), consensus("ACGT"), compatible("R", "Y"), compatible("R", "K"))
rx = to_regex("GAYNRTC")                                  # invented motif
print(rx, [m.start() + 1 for m in re.finditer(f"(?=({rx}))", "TTGACAATCGGATGGTCAA")])
```

```text
{'length': 12, 'ambiguous': Counter({'N': 2, 'R': 1, 'Y': 1}), 'gaps': 0, 'invalid': []}
{'length': 4, 'ambiguous': Counter(), 'gaps': 0, 'invalid': [(4, 'U')]} []
{'length': 8, 'ambiguous': Counter(), 'gaps': 1, 'invalid': [(7, 'X'), (8, '1')]}
[2.0, 1.0, 0.415, 0.0] 0.5
R Y N False True
GA[CT][ACGT][AG]TC [3, 11]
```

The lookahead `(?=(...))` reports overlapping motif matches, which a plain `finditer` would skip; positions are 1-based.

## Worked example

> [!example] GC content of a toy sequence with ambiguity (invented)
> Sequence: `GGCCNNNN` (8 positions: 4 concrete, 4 unknown).
> 1. **Validate**: length 8, no invalid character, 4 × N. Keep the Ns: they hold positions 5 to 8.
> 2. **Exclude policy**: GC over the 4 concrete bases = 4/4 = **1.0**.
> 3. **Expected policy**: G, G, C, C count 1 each; each N counts 2/4 = 0.5; $(4 + 4 \times 0.5)/8 = $ **0.75**.
> 4. **Bounds**: minimum when every N is A or T, 4/8 = 0.5; maximum when every N is G or C, 8/8 = 1.0: GC $\in [0.5, 1.0]$.
> 5. **Report**: "GC = 0.75 (expected; 4 of 8 positions ambiguous, range 0.5 to 1.0)". Reporting 1.0 alone would hide that half the sequence is unknown.

## Common misconceptions

> [!warning] "N is a gap, so it can be deleted"
> N is a base of unknown identity; a gap has its own symbol, the hyphen.[^ncbi] Deleting Ns changes the length and every downstream coordinate.

> [!warning] "A sequence containing R or Y is corrupted"
> Ambiguity codes are part of the standard nomenclature[^iupac] and of what NCBI expects in sequence input.[^ncbi] Reject only characters outside the codes, and report where they are.

> [!warning] "U is an ambiguity code"
> U is uracil, a concrete RNA base listed with the nucleotide codes.[^ncbi] Map it to T only when comparing RNA with DNA sequences, and say so.

> [!warning] "Only A, C, G, T in a file proves it is DNA"
> The same letters are amino acid codes.[^ncbi-gc] Molecule type is metadata to be declared, not inferred with certainty from the letters.

## Exercises

> [!question] Exercise 1 (L1)
> Give the bases for R, Y, S, W, B and N, and the code for {A, T}, for {C, G, T} and for {A, C, G}.

> [!success]- Solution
> R = A/G, Y = C/T, S = C/G, W = A/T, B = C/G/T (not A), N = any. {A, T} = W; {C, G, T} = B; {A, C, G} = V (not T).[^iupac]

> [!question] Exercise 2 (L1)
> Classify each string as a valid DNA sequence, valid with ambiguity, valid only as RNA, or invalid, and point to the offending characters: `ACGTRYKM`, `acgtn`, `ACGU`, `ACG TTA`, `ACGT1234`, `MKVLAAGG`.

> [!success]- Solution
> `ACGTRYKM`: valid with ambiguity (R, Y, K, M). `acgtn`: valid, lowercase read as uppercase, one N. `ACGU`: valid as RNA only. `ACG TTA`: invalid space at position 4 (strip whitespace when reading files, not inside a sequence string). `ACGT1234`: digits at positions 5 to 8 must be removed.[^ncbi] `MKVLAAGG`: L is not a nucleotide code (position 4): this is probably a protein, although M, K, V, A and G alone would have been valid nucleotide codes.

> [!question] Exercise 3 (L2)
> For the invented motif `GAYNRTC`, compute the number of concrete sequences it denotes and its information content in bits, and check that $\sum_i I(s_i) = \log_2(4^n / |L(s)|)$.

> [!success]- Solution
> Set sizes 1, 1, 2, 4, 2, 1, 1: $|L| = 16$. Bits: $2 + 2 + 1 + 0 + 1 + 2 + 2 = 10$. Check: $\log_2(4^7 / 16) = 14 - 4 = 10$. A fully specified 7-mer carries 14 bits; the ambiguity costs 4 bits.

> [!question] Exercise 4 (L2, Python)
> Implement the three GC policies (exclude, expected, bounds) and apply them to the toy sequence `SSWWNNAC`.

> [!success]- Solution
> With `IUPAC` from the Computational representation:
> ```python
> def gc_policies(seq: str) -> dict:
>     sets = [set(IUPAC[c]) for c in seq.upper()]
>     n = len(sets)
>     concrete = [s for s in sets if len(s) == 1]
>     return {
>         "exclude": sum(s <= {"C", "G"} for s in concrete) / len(concrete) if concrete else None,
>         "expected": sum(len(s & {"C", "G"}) / len(s) for s in sets) / n,
>         "min": sum(s <= {"C", "G"} for s in sets) / n,       # every ambiguous base resolved to A/T if possible
>         "max": sum(bool(s & {"C", "G"}) for s in sets) / n,  # resolved to C/G if possible
>     }
>
>
> print(gc_policies("SSWWNNAC"))
> ```
> Output: `{'exclude': 0.5, 'expected': 0.5, 'min': 0.375, 'max': 0.625}`. The exclude policy throws away S and W although they fix the GC status exactly: S is always strong (G or C) and W always weak (A or T). Only N is truly unknown here, which the bounds show: the range 0.375 to 0.625 comes from the two Ns alone.

> [!question] Exercise 5 (L3, Python)
> Using `IUPAC` from the Computational representation, write `translate_ambiguous(codon)` for the standard code (NCBI table 1) that returns the amino acid when every concrete codon agrees and `X` otherwise. Test `GCN`, `YTR`, `MGR`, `TAR`, `TRA`, `ATN`, `NNN` and explain the results with the structure of the code.

> [!success]- Solution
> ```python
> from itertools import product
>
> BASES = "TCAG"   # NCBI table order; standard code (table 1)
> STANDARD = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
> CODE = {a + b + c: aa for (a, b, c), aa in zip(product(BASES, repeat=3), STANDARD)}
>
>
> def translate_ambiguous(codon: str) -> str:
>     """Amino acid if every concrete codon the ambiguous codon stands for agrees, else X."""
>     meanings = {CODE["".join(p)] for p in product(*(IUPAC[c] for c in codon.upper()))}
>     return meanings.pop() if len(meanings) == 1 else "X"
>
>
> print(" ".join(f"{c}={translate_ambiguous(c)}" for c in ["GCN", "YTR", "MGR", "TAR", "TRA", "ATN", "NNN"]))
> ```
> Output: `GCN=A YTR=L MGR=R TAR=* TRA=* ATN=X NNN=X`. `GCN` is a four-fold degenerate family (all Ala). `YTR` and `MGR` cross the boundary between codon families but stay inside the six-codon sets of Leu (CTA, CTG, TTA, TTG) and Arg (AGA, AGG, CGA, CGG). `TAR` and `TRA` are pairs of stop codons. `ATN` mixes Ile and Met.[^ncbi-gc]

> [!question] Exercise 6 (L3)
> Design the validation policy of [[01-dna-engine]]: which modes, which defaults, and what a report contains. Justify each choice.

> [!success]- Solution
> Two modes. **Strict** (default for reference sequences): accept the 15 codes in either case, reject everything else with a list of (position, character). **Permissive** (for user input): additionally strip whitespace and line breaks and accept U for RNA. Never silently change or drop a character: uppercasing is reported, and N is kept. The report gives length, counts per ambiguity code, the longest run of N, and invalid positions. Ambiguity policies (exclude, expected, bounds) are parameters of each statistic, not of the validator, so one validated sequence can serve every analysis.

## Mastery checklist

- [ ] 1 Recognized: I can name the 15 codes and read R, Y, S, W and N without a table.
- [ ] 2 Understood: I can explain why codes are sets, what "compatible" and "consensus" mean, and why N must not be deleted.
- [ ] 3 Practiced: I can write a validator that reports positions, an IUPAC-to-regex converter and ambiguity-aware GC statistics.
- [ ] 4 Applied: [[01-dna-engine]] validates real sequences containing N and other codes, with documented policies, and [[bio-core]] stores them without loss.
- [ ] 5 Explained: I can teach the link between codes, information content and position weight matrices, and the limits of guessing molecule type from letters.

## References

[^iupac]: [[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]], *Nucleic Acids Research* (NC-IUB recommendations 1984: symbols and complements).
[^ncbi]: [[NCBI BLAST]], BLAST documentation "Query Input and database selection", FASTA format section (accepted nucleic acid codes, lowercase, hyphen for gaps, digits, N and X for unknown residues).
[^ncbi-gc]: [[NCBI Genetic Codes]], "The Genetic Codes", translation table 1 (standard code, one-letter amino acid string).
