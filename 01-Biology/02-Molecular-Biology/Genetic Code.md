---
aliases:
  - Standard Genetic Code
  - Codon Table
  - Translation Table
  - Code génétique
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Nucleotide]]"
  - "[[RNA]]"
  - "[[Amino Acid]]"
  - "[[Central Dogma]]"
related:
  - "[[Codon]]"
  - "[[Reading Frame]]"
  - "[[Open Reading Frame]]"
  - "[[Transcription]]"
  - "[[Translation]]"
  - "[[Transfer RNA]]"
  - "[[Mutation]]"
  - "[[Mitochondrial DNA]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[03-genome-diff]]"
  - "[[06-mutation-lab]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Nirenberg 1961 - Cell-Free Protein Synthesis and Synthetic Polyribonucleotides]]"
  - "[[Crick 1961 - General Nature of the Genetic Code for Proteins]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Freeland 1998 - The Genetic Code Is One in a Million]]"
---

# Genetic Code

> [!abstract]
> The genetic code is the dictionary cells use to read an mRNA three letters at a time and turn each triplet into one amino acid, or into a "stop" signal.

## Definition

The **genetic code** is the set of rules by which the nucleotide sequence of an mRNA is translated into the amino acid sequence of a protein: consecutive, non-overlapping triplets of nucleotides (**codons**), read 5' → 3' from a fixed starting point, each specify one amino acid or a stop signal.[^os15][^alberts][^berg]

## Why it matters

- **In silico translation.** Every protein sequence in a database that was predicted from a genome was obtained by applying a codon table to a coding sequence ([[02-sequence-translation]]).
- **Choosing the table.** NCBI numbers the known variant codes ("translation tables"); annotated coding features carry the table to use, and tools take it as a parameter. Translating a mitochondrial gene with the standard table gives a wrong protein.[^ncbi]
- **Six-frame search.** Comparing an unannotated DNA sequence with protein databases ([[BLAST]]), or scanning it for genes ([[Gene Finding]]), starts by translating all six [[Reading Frame|reading frames]] and looking for long [[Open Reading Frame|open reading frames]].
- **Variant effect.** Whether a substitution is silent, missense or nonsense is decided by the codon table ([[Mutation]], [[Variant Annotation]], [[03-genome-diff]], [[06-mutation-lab]]).

## Core (L1)

**Why triplets.** With 4 nucleotides, pairs give only $4^2 = 16$ combinations, fewer than the 20 amino acids; triplets give $4^3 = 64$.[^os15] Genetic experiments by Crick, Brenner and colleagues confirmed a triplet code: inserting or deleting one or two nucleotides in a phage gene destroyed its function, but three insertions (or one insertion plus one deletion close together) restored it.[^os15][^crick61]

**The table.** Of the 64 codons, 61 specify amino acids and 3 (UAA, UAG, UGA) are **stop codons**. **AUG** codes for methionine and is also the usual **start codon**.[^os15]

![[codon-table-grid.svg]]

**Three key properties.**[^os15][^berg]

1. **Degenerate (redundant)**: most amino acids have several codons (synonyms), from 1 (Met, Trp) to 6 (Leu, Ser, Arg).
2. **Unambiguous**: each codon means exactly one thing.
3. **Nearly universal**: the same table is used by bacteria, plants and animals, with a few exceptions (see L3).

**The first codon.** In 1961 Nirenberg and Matthaei added a synthetic RNA made only of uracil, poly(U), to a cell-free *E. coli* extract and obtained polyphenylalanine: UUU codes for Phe.[^nirenberg] Later experiments with synthetic RNAs of defined sequence assigned the other codons.[^berg]

## Deeper (L2)

### Reading frames

Because codons do not overlap, a sequence can be read in three frames, starting at its first, second or third nucleotide; the start codon fixes the frame actually used.[^alberts] Double-stranded DNA can encode on both strands, so it has **six** frames: three on the given strand and three on its reverse complement.

```text
frame +1   GAT GGC CAA ATG ACT TAG GGA AAC ATG C
frame +2   G ATG GCC AAA TGA CTT AGG GAA ACA TGC
frame +3   GA TGG CCA AAT GAC TTA GGG AAA CAT GC
```

A **frameshift** (an insertion or deletion whose length is not a multiple of 3) moves every downstream codon into another frame ([[Frameshift Mutation]]).

### The pattern of degeneracy

Synonymous codons are not scattered: most differ only at the third position. Codons XYU and XYC always encode the same amino acid, and XYA and XYG usually do.[^berg] Counting the table:

| Codons per amino acid | Amino acids | Codons |
|---:|---|---:|
| 6 | Leu, Ser, Arg | 18 |
| 4 | Val, Pro, Thr, Ala, Gly | 20 |
| 3 | Ile | 3 |
| 2 | Phe, Tyr, His, Gln, Asn, Lys, Asp, Glu, Cys | 18 |
| 1 | Met, Trp | 2 |
| stop | UAA, UAG, UGA | 3 |

### Wobble

A tRNA recognizes a codon through its **anticodon**, antiparallel to it ([[Transfer RNA]]). Pairing at the codon's third position is less strict than at the first two (**wobble**): for example G in the first (5') position of the anticodon can pair with U as well as C, and the modified base inosine pairs with U, C or A. One tRNA can therefore read several synonymous codons, and cells need fewer tRNA species than the 61 sense codons.[^alberts]

### Start codons

AUG is the usual start codon, but some organisms also start at other codons, for instance GUG or UUG in bacteria; used as a start, such a codon is read as (formyl)methionine. NCBI lists the allowed start codons for each translation table (the bacterial and plastid table is number 11).[^ncbi]

## Advanced (L3)

### Variant codes

The code is "nearly" universal. The NCBI translation tables document the known variants.[^ncbi]

| NCBI table | Where | Differences from table 1 |
|---:|---|---|
| 1 | Standard code | (reference) |
| 2 | Vertebrate mitochondria | UGA = Trp; AUA = Met; AGA and AGG = stop |
| 4 | Mycoplasma, Spiroplasma; mold and protozoan mitochondria | UGA = Trp |
| 6 | Nuclear code of some ciliates (and others) | UAA and UAG = Gln |
| 11 | Bacteria, archaea, plant plastids | same amino acids as table 1; more start codons |

Most variant tables are mitochondrial: mitochondrial genomes encode only a handful of proteins, so a codon can change meaning without disrupting many genes.[^alberts][^ncbi] A second, context-dependent exception is **selenocysteine**: in some proteins a UGA codon is read as selenocysteine by a dedicated tRNA, guided by a signal in the mRNA.[^alberts] Pipelines that annotate organelle or bacterial genomes therefore pass the table number explicitly ([[02-sequence-translation]] supports several).

### Robustness to mutations

Degeneracy makes many single-base changes harmless: if the code had 20 sense codons and 44 stops, most substitutions would end the protein.[^berg] Because synonyms share their first two bases, third-position changes are mostly silent. In the standard table, of the 183 possible single-base changes at each position of the 61 sense codons, the fraction that keeps the amino acid is 8/183 (position 1), 0/183 (position 2) and 126/183 (position 3) (computed in Exercise 6). Beyond redundancy, similar codons tend to encode chemically similar amino acids: Freeland and Hurst compared the standard code with a million random alternative codes and found that very few minimize the impact of point mutations and mistranslation better, once realistic biases (such as transitions being more frequent than transversions) are included.[^freeland] This property is what [[06-mutation-lab]] makes visible and what [[Molecular Evolution]] exploits when it compares synonymous and non-synonymous substitution rates.

## Mathematical representation

Let $\Sigma = \{A, C, G, U\}$ and $\mathcal{C} = \Sigma^3$ the set of codons, $|\mathcal{C}| = 64$. Let $\mathcal{A}$ be the 20 standard amino acids and $*$ the stop symbol. A genetic code is a function

$$g : \mathcal{C} \to \mathcal{A} \cup \{*\}.$$

The standard code is **surjective** (every amino acid is coded) and **not injective** (degenerate). The degeneracy of $a$ is $d(a) = |g^{-1}(a)|$, with $\sum_{a \in \mathcal{A} \cup \{*\}} d(a) = 64$. Variant codes are other functions $g'$ that differ from $g$ on a few codons.

**Reading frames.** For $s \in \Sigma^n$ and frame $f \in \{0, 1, 2\}$, the codons are $c_k = s_{f+3k+1}\, s_{f+3k+2}\, s_{f+3k+3}$ for $k = 0, \dots, \lfloor (n - f)/3 \rfloor - 1$, and the frame's translation is $T_f(s) = g(c_0)\, g(c_1) \cdots$. The six frames are $T_0, T_1, T_2$ applied to $s$ and to $\operatorname{rc}(s)$.

**Random ORFs.** In a random sequence with independent, uniform bases, each codon is a stop with probability $q = 3/64$. The number of codons read until the first stop (included) is geometric with mean $1/q = 64/3 \approx 21.3$, and

$$P(\text{no stop in } k \text{ codons}) = (1 - q)^k = (61/64)^k.$$

$(61/64)^{100} \approx 0.008$: an ORF of 100 codons is unlikely by chance, which is the statistical basis of ORF-based gene detection. With a biased base composition, $q$ changes (Exercise 5).

## Computational representation

The standard way to store a code is the NCBI layout: codons in the order TTT, TTC, TTA, TTG, TCT, ... (bases ordered T, C, A, G) and one 64-letter string of amino acids per table. A dictionary built from it gives $O(1)$ lookup ([[Hash Table]]). Genomic DNA uses T, so tables are keyed on DNA codons; unknown or ambiguous codons (containing N) map to `X`.

```python
BASES = "TCAG"
# NCBI translation tables: one amino acid letter per codon, codons in TCAG order
TABLES = {
    1: "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",  # standard
    2: "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG",  # vertebrate mitochondrial
}
CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]

def codon_table(table_id: int = 1) -> dict[str, str]:
    return dict(zip(CODONS, TABLES[table_id]))

COMPLEMENT = str.maketrans("ACGT", "TGCA")

def reverse_complement(dna: str) -> str:
    return dna.translate(COMPLEMENT)[::-1]

def translate(dna: str, frame: int = 0, table: dict[str, str] | None = None) -> str:
    """Translate from offset frame (0, 1, 2); unknown codons give X, a partial last codon is dropped."""
    table = table or codon_table(1)
    return "".join(table.get(dna[i:i + 3], "X") for i in range(frame, len(dna) - 2, 3))

def six_frames(dna: str) -> dict[str, str]:
    rc = reverse_complement(dna)
    return {**{f"+{f + 1}": translate(dna, f) for f in range(3)},
            **{f"-{f + 1}": translate(rc, f) for f in range(3)}}

def find_orfs(dna: str, min_aa: int = 2):
    """Yield (strand, frame, start, end, protein): ATG ... stop, coordinates 0-based half-open on +."""
    n = len(dna)
    for strand, seq in (("+", dna), ("-", reverse_complement(dna))):
        for frame in range(3):
            protein, first_m = translate(seq, frame), None
            for k, aa in enumerate(protein):
                if aa == "M" and first_m is None:
                    first_m = k
                elif aa == "*" and first_m is not None:
                    if k - first_m >= min_aa:
                        s, e = frame + 3 * first_m, frame + 3 * (k + 1)   # stop codon included
                        if strand == "-":
                            s, e = n - e, n - s
                        yield strand, frame + 1, s, e, protein[first_m:k]
                    first_m = None

dna = "GATGGCCAAATGACTTAGGGAAACATGC"      # invented toy sequence
for name, protein in six_frames(dna).items():
    print(name, protein)
for orf in find_orfs(dna):
    print(orf)
```

Output:

```text
+1 DGQMT*GNM
+2 MAK*LRETC
+3 WPNDLGKH
-1 ACFPKSFGH
-2 HVSLSHLAI
-3 MFP*VIWP
('+', 1, 9, 18, 'MT')
('+', 2, 1, 13, 'MAK')
('-', 3, 14, 26, 'MFP')
```

Two conventions to check in any tool: how minus-strand frames are numbered (here, frame −1 starts at the first base of the reverse complement), and whether an ORF must start with ATG or may run from one stop to the next.

## Worked example

> [!example] Six frames and ORFs of a toy sequence (invented)
> Sequence: `5'-GATGGCCAAATGACTTAGGGAAACATGC-3'` (28 nt).
>
> 1. **Frame +2** starts at the second base: `ATG GCC AAA TGA` → Met-Ala-Lys-stop. This is an ORF from position 1 to 13 (0-based, stop included).
> 2. **Frame +1** contains `ATG ACT TAG` at positions 9 to 18 → Met-Thr-stop. Its ATG overlaps the stop codon TGA of frame +2 (`AAATGACT`): overlapping ORFs in different frames are common in short sequences.
> 3. **Reverse complement**: `GCATGTTTCCCTAAGTCATTTGGCCATC`. Its frame 3 (offset 2) reads `ATG TTT CCC TAA` → Met-Phe-Pro-stop. On the `+` strand this ORF occupies positions 14 to 26, read right to left.
> 4. **Interpretation**: all three ORFs are 2 to 3 codons long, far below the ~96 codons needed to be surprising in random sequence (see Mathematical representation). None is evidence of a gene.

## Common misconceptions

> [!warning] "Degenerate means ambiguous"
> Degenerate means several codons for one amino acid. The code is unambiguous: one codon never means two amino acids within a given code.

> [!warning] "The genetic code is universal"
> It is nearly universal. Vertebrate mitochondria, some bacteria and some ciliates use variant tables, and UGA can encode selenocysteine in specific contexts. Always record which NCBI table was used.

> [!warning] "Every AUG is a start codon"
> AUG also encodes internal methionines. The start is the AUG chosen by the translation initiation machinery, according to its context ([[Translation]]); in silico, the first ATG of an ORF is only a candidate start.

> [!warning] "A change at the third codon position is always silent"
> Only about 69 % (126/183) of third-position changes are synonymous. AUG → AUA changes Met to Ile, and UGG → UGA turns Trp into a stop.

## Exercises

> [!question] Exercise 1 (L1)
> Translate `5'-AUGUUUGGCAAAUGA-3'` with the standard code.

> [!success]- Solution
> Codons AUG UUU GGC AAA UGA → Met-Phe-Gly-Lys-stop. The protein has 4 amino acids; the stop codon is not translated into an amino acid.

> [!question] Exercise 2 (L1)
> Explain why a code of single nucleotides or of pairs of nucleotides could not encode 20 amino acids, and how many codons a quadruplet code would have.

> [!success]- Solution
> $4^1 = 4$ and $4^2 = 16$ are fewer than 20; $4^3 = 64 \ge 20$ is the smallest length that suffices. A quadruplet code would have $4^4 = 256$ codons.

> [!question] Exercise 3 (L2)
> In the Crick-Brenner style experiment, a gene reads `THE CAT ATE THE RAT` (read as three-letter words). Show what one insertion does, and why an insertion followed by a nearby deletion, or three insertions, restores most of the message.

> [!success]- Solution
> Insert X after the first word: `THE XCA TAT ETH ERA T`: every word after the insertion is wrong (frameshift). Delete the A of `ATE` further on: `THE XCA TTE THE RAT`: only the words between the two changes are wrong, the frame is restored after the deletion. Three insertions add one full word: `THE XXX CAT ATE THE RAT` (if together) or garble only the region between them. This is the logic that showed the code is read in triplets from a fixed start.[^crick61]

> [!question] Exercise 4 (L2, Python)
> Using `codon_table` and `CODONS` from the code above, list the codons whose meaning differs between the standard code (table 1) and the vertebrate mitochondrial code (table 2).

> [!success]- Solution
> ```python
> std, mito = codon_table(1), codon_table(2)
> print({c: (std[c], mito[c]) for c in CODONS if std[c] != mito[c]})
> # {'TGA': ('*', 'W'), 'ATA': ('I', 'M'), 'AGA': ('R', '*'), 'AGG': ('R', '*')}
> ```
>
> Four codons change: UGA stop → Trp, AUA Ile → Met, and AGA and AGG Arg → stop, as in the NCBI description of table 2.[^ncbi]

> [!question] Exercise 5 (L3, Python)
> Under the random model with independent bases, find the smallest ORF length $k$ (in codons) for which $P(\text{no stop in } k \text{ codons}) < 0.01$, for a genome with 50 % GC and for one with 70 % GC (A = T and G = C). What does this imply for ORF-based gene finding?

> [!success]- Solution
> All three stop codons are AT-rich, so a GC-rich genome has fewer random stops and longer random ORFs.
>
> ```python
> import math
>
> def stop_probability(gc: float) -> float:
>     """P(a random codon is TAA, TAG or TGA) for i.i.d. bases with G+C fraction gc."""
>     p = {"G": gc / 2, "C": gc / 2, "A": (1 - gc) / 2, "T": (1 - gc) / 2}
>     return sum(p[a] * p[b] * p[c] for a, b, c in ("TAA", "TAG", "TGA"))
>
> def min_orf_codons(gc: float, alpha: float = 0.01) -> int:
>     """Smallest k such that P(k stop-free codons in random sequence) < alpha."""
>     q = stop_probability(gc)
>     return math.floor(math.log(alpha) / math.log(1 - q)) + 1
>
> for gc in (0.5, 0.7):
>     print(gc, round(stop_probability(gc), 5), min_orf_codons(gc))
> # 0.5 0.04688 96
> # 0.7 0.01913 239
> ```
>
> A length threshold that works for a 50 % GC genome (about 96 codons) is far too permissive at 70 % GC (about 239 codons needed). ORF thresholds must depend on base composition, and real gene finders use composition-aware statistical models instead ([[Gene Finding]]).

> [!question] Exercise 6 (L3, Python)
> Using `codon_table` and `BASES` from the code above, count for each codon position how many of the single-base substitutions of the 61 sense codons are synonymous in the standard code. Relate the result to wobble and to robustness.

> [!success]- Solution
> ```python
> std = codon_table(1)
> counts = {pos: [0, 0] for pos in range(3)}          # [synonymous, total]
> for codon, aa in std.items():
>     if aa == "*":
>         continue
>     for pos in range(3):
>         for b in BASES:
>             if b != codon[pos]:
>                 alt = codon[:pos] + b + codon[pos + 1:]
>                 counts[pos][0] += std[alt] == aa
>                 counts[pos][1] += 1
> print(counts)   # {0: [8, 183], 1: [0, 183], 2: [126, 183]}
> ```
>
> Position 2 is never silent, position 1 rarely (the 8 cases are Leu and Arg codons such as CUA ↔ UUA and CGA ↔ AGA), and position 3 is silent 69 % of the time. The third position is exactly the wobble position, where tRNA pairing is loose: the table's structure matches the decoding mechanism, and it buffers the most frequent kind of error.

## Mastery checklist

- [ ] 1 Recognized: I can state what a codon is, name the start and stop codons and say that there are 64 codons for 20 amino acids.
- [ ] 2 Understood: I can explain degeneracy, wobble, reading frames and why the code is only nearly universal.
- [ ] 3 Practiced: I can build a codon table from an NCBI string, translate six frames and find ORFs in Python.
- [ ] 4 Applied: in [[02-sequence-translation]], I translate real genes with the correct NCBI table (including a mitochondrial gene) and compare with the database protein.
- [ ] 5 Explained: I can teach why the code is robust to mutations, how ORF statistics depend on composition, and the pitfalls of frame and start-codon conventions.

## References

[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (the genetic code).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of the genetic code, tRNAs and wobble, reading frames, selenocysteine, and mitochondrial genetic systems.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of the genetic code (triplet reading, synonyms and degeneracy).
[^nirenberg]: [[Nirenberg 1961 - Cell-Free Protein Synthesis and Synthetic Polyribonucleotides]], *PNAS* 47(10):1588-1602.
[^crick61]: [[Crick 1961 - General Nature of the Genetic Code for Proteins]], Crick FHC, Barnett L, Brenner S, Watts-Tobin RJ, *Nature* 192:1227-1232.
[^ncbi]: [[NCBI Genetic Codes]], "The Genetic Codes" (NCBI Taxonomy), the numbered translation tables and their start codons.
[^freeland]: [[Freeland 1998 - The Genetic Code Is One in a Million]], Freeland SJ, Hurst LD, *Journal of Molecular Evolution* 47:238-248.
