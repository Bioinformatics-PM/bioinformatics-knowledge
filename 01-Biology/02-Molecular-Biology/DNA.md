---
aliases:
  - Deoxyribonucleic Acid
  - ADN
  - Acide désoxyribonucléique
  - dsDNA
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
  - "[[Nucleic Acid]]"
  - "[[Hydrogen Bond]]"
related:
  - "[[RNA]]"
  - "[[Base Pairing]]"
  - "[[DNA Replication]]"
  - "[[Chromatin]]"
  - "[[Gene]]"
  - "[[Genome]]"
  - "[[GC Content]]"
  - "[[Reverse Complement]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-core]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# DNA

> [!abstract]
> DNA is the molecule that stores hereditary information: two long chains of nucleotides wound around each other, where the order of the bases A, C, G, T spells the message and each chain determines the other.

## Definition

**Deoxyribonucleic acid (DNA)** is a polymer of deoxyribonucleotides joined by 3'-5' phosphodiester bonds. In cells it is usually a **double helix**: two antiparallel strands held together by complementary base pairs (A with T, G with C), with the sugar-phosphate backbones outside and the bases inside. Its base sequence carries the hereditary information of the cell.[^alberts][^watson]

## Why it matters

- Reference genomes ([[FASTA Format]]), reads ([[FASTQ Format]]), alignments ([[SAM Format]]) and variants ([[VCF Format]]) are all descriptions of DNA sequence.
- A file stores **one** strand, 5' → 3'; the other is implied by complementarity. A read can come from either strand, so mapping, assembly and motif search must consider each sequence and its [[Reverse Complement]], a core operation of sequence bioinformatics.
- Duplex stability depends on base composition, which links [[GC Content]] to melting temperature, primer design for [[Polymerase Chain Reaction|PCR]] and probe hybridization.[^berg]
- Genome size, from millions to billions of base pairs, sets the computational scale of every analysis ([[Genome]]).[^blattner][^nurk]

## Core (L1)

![[dna-double-helix-schematic.svg]]

- **Double helix.** Watson and Crick (1953) proposed two helical chains coiled around a common axis, bases on the inside, phosphates on the outside. They built the model using X-ray diffraction results of Rosalind Franklin, Maurice Wilkins and co-workers, acknowledged in the paper.[^watson]
- **Complementary base pairing.** A pairs with T through 2 hydrogen bonds; G pairs with C through 3 ([[Base Pairing]]). Each pair joins a purine to a pyrimidine, so every rung of the ladder has the same width.[^openstax][^alberts]
- **Antiparallel strands.** The two strands run in opposite directions: where one reads 5' → 3', its partner reads 3' → 5'.[^watson][^openstax]
- **Chargaff's rules.** In double-stranded DNA, the amount of A equals that of T and the amount of G equals that of C, so purines = pyrimidines; the G+C proportion varies between species. Watson and Crick's pairing explained these ratios.[^griffiths][^watson]
- **Reading the other strand.** Because of antiparallelism, the partner of `5'-AGTCG-3'` is `3'-TCAGC-5'`, which, written in the conventional 5' → 3' direction, is `CGACT`: the **reverse complement**.

## Deeper (L2)

**B-DNA geometry.** In the 1953 model, adjacent bases are 3.4 Å apart along the axis and the structure repeats after 10 residues per chain, i.e. every 34 Å; phosphates lie 10 Å from the axis, giving a diameter of about 20 Å.[^watson] Measured in solution, B-DNA has about 10.4 base pairs per turn.[^alberts] The helix is right-handed; other conformations exist, such as the more compact A-DNA and the left-handed Z-DNA.[^berg]

**Major and minor grooves.** Because the two sugars of a base pair attach on the same side of the pair, the backbones are unevenly spaced and delimit a wide **major groove** and a narrow **minor groove**. The edges of the bases exposed in the major groove differ for each of the four pair orientations (A-T, T-A, G-C, C-G), so proteins can read the sequence without opening the helix, which is how most sequence-specific DNA-binding proteins, such as [[Transcription Factor|transcription factors]], work.[^alberts]

**Stability and melting.** Heating separates the strands (denaturation, or melting); they re-pair on cooling (renaturation, hybridization). DNA richer in G-C melts at a higher temperature.[^berg] The stabilization comes mostly from **stacking** between neighboring base pairs, whose strength depends on the dinucleotide, and less from the hydrogen bonds themselves.[^yakovchuk] See [[GC Content]].

**Packaging.** A eukaryotic cell must fit meters of DNA into a nucleus: DNA wraps around histone proteins into nucleosomes, which fold further into [[Chromatin]].[^alberts] Bacterial [[Chromosome|chromosomes]] are typically single circular molecules; eukaryotic chromosomes are linear (see [[DNA Replication]] for the consequence at chromosome ends).[^alberts]

**Genome sizes** (one copy of each chromosome):

| Organism | Size | Source |
|---|---|---|
| *Escherichia coli* K-12 | 4,639,221 bp (≈ 4.6 Mb) | complete sequence, 1997[^blattner] |
| *Homo sapiens* (T2T-CHM13) | ≈ 3.055 × 10⁹ bp (≈ 3.1 Gb) | first gapless assembly (all chromosomes except Y), 2022[^nurk] |

## Advanced (L3)

- **Strand symmetry as a data problem.** Sequencing reads, [[K-mer]] counts and motif scans come from both strands. A double-stranded site is really the pair $\{s, \mathrm{rc}(s)\}$, so a k-mer counter can store a single **canonical** representative (the lexicographically smaller of the two), which halves memory and merges counts from both strands.
- **Reverse palindromes.** Sequences equal to their own reverse complement (e.g. `GAATTC`, the EcoRI restriction site) are recognized by proteins acting as symmetric dimers, like many restriction enzymes and gene regulatory proteins.[^alberts] Finding them is a classic string exercise (Exercise 6).
- **DNA is dynamic.** Opening the helix for [[DNA Replication]] or [[Transcription]] over- or under-winds the flanking DNA (supercoiling), which topoisomerases relieve by cutting and rejoining strands.[^alberts]
- **Genes live on both strands.** Different genes use different strands as template, so a genome FASTA's single strand is an arbitrary reference orientation, not "the coding strand".[^alberts] Annotations therefore record a strand (`+` or `-`) for each feature (see [[GFF Format]]).
- **More than the sequence.** Cytosine methylation and chromatin state add a regulated layer of information on top of the base sequence ([[Epigenetics]], [[Epigenomics]]).[^alberts] Mutation, repair and replication asymmetries leave statistical signatures in genome composition (see [[DNA Replication#Advanced (L3)]]).

## Mathematical representation

- A strand is a word $s = s_1 s_2 \dots s_n \in \Sigma^n$ over $\Sigma = \{A, C, G, T\}$, written 5' → 3'; $n = |s|$ is its length.
- With the complement $c$ of [[Nucleotide#Mathematical representation]], the **reverse complement** is
$$\mathrm{rc}(s)_i = c(s_{n+1-i}), \quad i = 1, \dots, n.$$
- Properties: $\mathrm{rc}(\mathrm{rc}(s)) = s$ (involution) and $\mathrm{rc}(uv) = \mathrm{rc}(v)\,\mathrm{rc}(u)$ for concatenated words $u, v$.
- A duplex is the unordered pair $\{s, \mathrm{rc}(s)\}$. Writing $\#_x(s)$ for the count of base $x$ in $s$, complementarity gives $\#_A(\mathrm{rc}(s)) = \#_T(s)$, so the duplex totals satisfy $\#_A = \#_T$ and $\#_G = \#_C$: **Chargaff's parity rule is a theorem of the model**, true for the duplex, not for each strand separately.
- **GC content** $\mathrm{GC}(s) = \dfrac{\#_G(s) + \#_C(s)}{n}$, and $\mathrm{GC}(\mathrm{rc}(s)) = \mathrm{GC}(s)$ because $c$ swaps G and C.
- A **reverse palindrome** satisfies $s = \mathrm{rc}(s)$. Its length is even: if $n$ were odd, the middle position $m = \frac{n+1}{2}$ would need $s_m = c(s_m)$, impossible since $c$ has no fixed point.

## Computational representation

A FASTA record stores one strand as text, 5' → 3'; lowercase letters and IUPAC codes may appear ([[Nucleotide#Computational representation]]). The core operations fit in a few lines of standard-library Python:

```python
# Complement table covering IUPAC codes and lowercase (soft-masked) letters.
COMPLEMENT = str.maketrans("ACGTRYSWKMBDHVNacgtryswkmbdhvn",
                           "TGCAYRSWMKVHDBNtgcayrswmkvhdbn")


def reverse_complement(seq: str) -> str:
    """The other strand, read 5'->3'."""
    return seq.translate(COMPLEMENT)[::-1]


def gc_content(seq: str) -> float:
    """(G + C) / (A + C + G + T), ignoring ambiguous symbols such as N."""
    s = seq.upper()
    acgt = sum(s.count(b) for b in "ACGT")
    return (s.count("G") + s.count("C")) / acgt if acgt else 0.0


def canonical(kmer: str) -> str:
    """One representative for a k-mer and its reverse complement."""
    return min(kmer, reverse_complement(kmer))


top = "ATGCGTACCN"  # toy sequence
print(reverse_complement(top))
print(round(gc_content(top), 3), round(gc_content(reverse_complement(top)), 3))
print(reverse_complement("GAATTC") == "GAATTC", canonical("TTAC"))
```

```text
NGGTACGCAT
0.556 0.556
True GTAA
```

`str.translate` runs in $O(n)$; slicing `[::-1]` reverses in $O(n)$. Excluding `N` from the GC denominator is a choice: document it, because tools differ.

## Worked example

> [!example] From one strand to the duplex, and back
> Toy strand (invented): `5'-ATGCGTACC-3'`.
> 1. **Pair each base** (A↔T, G↔C) under it, keeping positions aligned:
> ```text
> 5'-ATGCGTACC-3'
>    |||||||||
> 3'-TACGCATGG-5'
> ```
> 2. **Read the partner 5' → 3'** (right to left): `GGTACGCAT` = $\mathrm{rc}(s)$.
> 3. **Check Chargaff on the duplex.** Top strand: A2 T2 G2 C3. Bottom strand: A2 T2 G3 C2. Duplex: A4 = T4, G5 = C5. Neither strand alone has G = C.
> 4. **GC content.** Top: (2 + 3)/9 = 0.556; bottom: (3 + 2)/9 = 0.556, equal as proved above.
> 5. **Palindrome check.** For the EcoRI site `GAATTC`: complement `CTTAAG`, reversed `GAATTC`, identical to the site, so both strands read `GAATTC` 5' → 3'.

## Common misconceptions

> [!warning] "The other strand is the complement"
> The base-by-base complement of `5'-ATGCG-3'` is `TACGC`, but that string is written 3' → 5'. Every sequence in a file is read 5' → 3', so the other strand is the **reverse** complement, `CGCAT`. Forgetting the reversal is the most common bug in sequence code.

> [!warning] "G-C pairs are more stable only because they have three hydrogen bonds"
> G-C-rich DNA does melt at higher temperature, but measurements show that base **stacking** between neighbors contributes most of the duplex stability, and stacking is itself strongest for G-C-containing steps.[^yakovchuk]

> [!warning] "Chargaff's rules hold for any DNA sequence"
> A = T and G = C hold for the **double-stranded** molecule (a consequence of pairing, see the Mathematical representation). A single strand, such as a gene sequence in a FASTA file, generally has A ≠ T and G ≠ C.[^watson]

> [!warning] "The strand in the reference FASTA is the coding strand"
> Genes lie on both strands; the reference just picks one orientation per chromosome.[^alberts] A gene annotated on the `-` strand must be reverse-complemented before reading its codons ([[Genetic Code]]).

## Exercises

> [!question] Exercise 1 (L1)
> Write the strand complementary to `5'-AGCTTAGC-3'` with its 5' and 3' labels, then write it in the conventional 5' → 3' direction.

> [!success]- Solution
> Complement under each base: `3'-TCGAATCG-5'`. Read from its 5' end: `5'-GCTAAGCT-3'`. Check with `reverse_complement("AGCTTAGC")`, which prints `GCTAAGCT`.

> [!question] Exercise 2 (L1)
> A sample of double-stranded DNA contains 30% adenine. Give the percentages of T, G and C. Could you answer for single-stranded DNA?

> [!success]- Solution
> A = T = 30%, so A + T = 60% and G + C = 40%, with G = C = 20%. For single-stranded DNA, no: nothing forces A = T on one strand.

> [!question] Exercise 3 (L2)
> Prove that a reverse palindrome has even length, and list all reverse palindromes of length 2.

> [!success]- Solution
> See the Mathematical representation: an odd length would force the middle base to equal its own complement, but $c$ has no fixed point. Length 2: $s_1 s_2$ with $s_2 = c(s_1)$, giving `AT`, `TA`, `CG`, `GC`.

> [!question] Exercise 4 (L2)
> Using the B-DNA geometry of the 1953 model, how long is one turn containing 10 base pairs, and how many turns does a 4,639,221 bp *E. coli* chromosome contain at 10.4 bp per turn?

> [!success]- Solution
> $10 \times 3.4$ Å = 34 Å = 3.4 nm per turn. Turns: $4{,}639{,}221 / 10.4 \approx 446{,}079$, about $4.5 \times 10^5$ turns, each of which must be unwound during replication.

> [!question] Exercise 5 (L3, Python)
> Count canonical 3-mers in the toy sequence `ACGGATTCGAATTCTG` and in its reverse complement. Show that the two counts are identical and explain why.

> [!success]- Solution
> ```python
> from collections import Counter
>
> COMPLEMENT = str.maketrans("ACGT", "TGCA")
>
>
> def reverse_complement(seq):
>     return seq.translate(COMPLEMENT)[::-1]
>
>
> def canonical_kmer_counts(seq: str, k: int) -> Counter:
>     counts = Counter()
>     for i in range(len(seq) - k + 1):
>         kmer = seq[i:i + k]
>         counts[min(kmer, reverse_complement(kmer))] += 1
>     return counts
>
>
> s = "ACGGATTCGAATTCTG"
> print(canonical_kmer_counts(s, 3) == canonical_kmer_counts(reverse_complement(s), 3))
> print(canonical_kmer_counts(s, 3).most_common(3))
> ```
> Output: `True`, then `[('AAT', 3), ('GAA', 3), ('CGA', 2)]`. The k-mers of $\mathrm{rc}(s)$ are exactly the reverse complements of the k-mers of $s$ (by $\mathrm{rc}(uv) = \mathrm{rc}(v)\mathrm{rc}(u)$), and a k-mer and its reverse complement share one canonical form.

> [!question] Exercise 6 (L3, Python)
> Write `palindromic_sites(seq, k)` returning the 1-based start positions of all length-$k$ reverse palindromes. Run it on `ACGGATTCGAATTCTG` for $k = 6$ and $k = 4$. Then estimate the physical length of a diploid human genome, $2 \times 3.055 \times 10^9$ bp, at 3.4 Å per base pair.

> [!success]- Solution
> ```python
> COMPLEMENT = str.maketrans("ACGT", "TGCA")
>
>
> def reverse_complement(seq):
>     return seq.translate(COMPLEMENT)[::-1]
>
>
> def palindromic_sites(seq: str, k: int) -> list[tuple[int, str]]:
>     """1-based start positions of length-k windows equal to their own reverse complement."""
>     return [(i + 1, seq[i:i + k]) for i in range(len(seq) - k + 1)
>             if seq[i:i + k] == reverse_complement(seq[i:i + k])]
>
>
> s = "ACGGATTCGAATTCTG"
> print(palindromic_sites(s, 6), palindromic_sites(s, 4))
> print(round(2 * 3.055e9 * 0.34e-9, 2), "m")
> ```
> Output: `[(6, 'TTCGAA'), (9, 'GAATTC')] [(7, 'TCGA'), (10, 'AATT')]`, then `2.08 m`. The 4-mers found are the centers of the 6-mers: a palindrome's core is itself a palindrome. About 2 m of DNA per nucleus is why packaging into [[Chromatin]] is unavoidable.

## Mastery checklist

- [ ] 1 Recognized: I can describe DNA as an antiparallel double helix with A-T and G-C pairs.
- [ ] 2 Understood: I can explain antiparallelism, Chargaff's rules, the grooves and why the second strand is the reverse complement.
- [ ] 3 Practiced: I can implement reverse complement, GC content and canonical k-mers, and prove their properties.
- [ ] 4 Applied: I used these operations in [[01-dna-engine]] and modeled DNA as a typed object in [[bio-core]], on a real genome FASTA.
- [ ] 5 Explained: I can explain duplex stability (stacking vs hydrogen bonds), strand conventions in genome files, and the scale of real genomes.

## References

[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature*.
[^openstax]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function".
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000).
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research*.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science*.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*.
