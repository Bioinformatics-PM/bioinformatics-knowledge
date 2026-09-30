---
aliases:
  - Codons
  - Triplet
  - Start Codon
  - Stop Codon
  - Nonsense Codon
  - Codon d'initiation
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
  - "[[Transcription]]"
  - "[[Messenger RNA]]"
related:
  - "[[Genetic Code]]"
  - "[[Reading Frame]]"
  - "[[Open Reading Frame]]"
  - "[[Transfer RNA]]"
  - "[[Translation]]"
  - "[[Point Mutation]]"
  - "[[Codon Usage Bias]]"
  - "[[Codon Substitution Model]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[bio-core]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Crick 1961 - General Nature of the Genetic Code for Proteins]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Codon

> [!abstract]
> A codon is one three-letter word of a coding sequence: the ribosome reads an mRNA three nucleotides at a time, and each triplet means one amino acid, or "stop".

## Definition

A **codon** is a sequence of three consecutive nucleotides in a messenger RNA, or in the coding strand of DNA, that specifies one amino acid or the end of translation. Codons are read 5' → 3', one after the other, without overlap and without gaps, starting from a start codon. There are $4^3 = 64$ codons: 61 **sense codons** specify amino acids and 3 **stop codons** (also called nonsense codons), UAA, UAG and UGA, end translation. AUG codes for methionine and is also the usual **start codon**.[^os15][^crick61][^alberts] Which amino acid each codon means is the [[Genetic Code]].

## Why it matters

- **A coding sequence is a list of codons.** Its length is a multiple of 3, it starts with a start codon and ends with its only in-frame stop codon: the first sanity check on any annotated CDS ([[02-sequence-translation]], [[Gene Annotation]]).
- **Variants are interpreted codon by codon.** Whether a substitution is silent, missense or nonsense depends on which codon it hits and at which position ([[Point Mutation]], [[Silent Mutation]], [[Missense Mutation]], [[Nonsense Mutation]]).
- **Codon-level statistics.** Codon counts describe how synonymous codons are used ([[Codon Usage Bias]]), and evolutionary models of coding sequences use the codon as their unit to compare synonymous and non-synonymous changes and detect selection ([[Codon Substitution Model]]).[^yang]
- **A typed object.** [[bio-core]] models the codon as its own type, not as a 3-character string, so that invalid lengths and letters are rejected once.

## Core (L1)

**Reading in triplets.** Crick, Brenner and colleagues showed that the code is read in groups of three bases from a fixed starting point: adding or removing one or two bases garbled the downstream message, but three changes together restored it ([[Genetic Code#Core (L1)]]).[^crick61] A coding sequence is therefore segmented as:

```text
CDS position   1  4  7  10 13
               |  |  |  |  |
codon          ATG CAT GAC TGG TAA
codon number   1   2   3   4   5
amino acid     M   H   D   W   stop
```

**One triplet, four ways to write it.** The codon is defined on the mRNA; the coding strand of the gene has the same letters with T, the template strand carries the complement, and the tRNA recognizes it through an antiparallel anticodon ([[Transcription]], [[Transfer RNA]]):[^os15][^alberts]

| Molecule | Writing | Example |
|---|---|---|
| mRNA (the codon) | 5' → 3' | 5'-AUG-3' |
| DNA coding strand | same letters, T for U | 5'-ATG-3' |
| DNA template strand | complement, antiparallel | 3'-TAC-5' |
| tRNA anticodon | complement, antiparallel | 3'-UAC-5' (written 5'-CAU-3') |

**Start and stop codons.**[^os15][^alberts]

- **AUG** starts translation in almost all genes and codes for methionine, so every protein starts with Met (often removed later). Some organisms also start at other codons, listed by NCBI for each translation table ([[Genetic Code#Deeper (L2)]]).[^ncbi]
- **UAA, UAG, UGA** end translation. No tRNA reads them in the standard code: release factors do ([[Translation]]).

**Spotting them: only in frame.** A start or stop codon counts only if it is one of the triplets being read. In the CDS above, the letters `ATG` also occur at positions 5 to 7 and `TGA` at 6 to 8, but both straddle two codons (CAT GAC TGG): they are not signals in this frame. For a CDS starting at position 1, a triplet starting at position $p$ is a codon of the frame being read exactly when $p - 1$ is a multiple of 3 ([[Reading Frame]]).

**From nucleotide to codon.** Codon $k$ occupies CDS positions $3k - 2$ to $3k$ and encodes residue $k$ of the protein. Conversely, CDS position $p$ lies in codon $\lceil p/3 \rceil$, at position $((p - 1) \bmod 3) + 1$ inside it. Position 12 of the CDS above is the third base of codon 4 (TGG).

## Deeper (L2)

**The three positions are not equal.** Because synonymous codons mostly share their first two bases, a change at the third position is often silent, a change at the second never is, and a change at the first rarely is (counts in [[Genetic Code#Advanced (L3)]]).[^os15] Codon position is therefore the first thing to compute when a variant falls in a CDS.

**Neighbours and nonsense.** Each codon has $3 \times 3 = 9$ neighbours that differ at one position. Only 18 of the 61 sense codons have a stop codon among their neighbours, UGG (Trp) and UAC (Tyr) among them (Exercise 3): a nonsense mutation can arise from a single substitution only at these codons.

**Codons across exon junctions.** A codon is contiguous in the mRNA, not necessarily in the genome: when an exon boundary falls inside a codon, its three bases lie in two exons, separated by an intron ([[Gene#Worked example]], [[Transcription#Exercises]]). Mapping a genome position to a codon must therefore go through the spliced transcript, and, for a gene on the `-` strand, through the reverse complement (Exercise 5).

**Codon and anticodon.** Codon position 1 pairs with anticodon position 3 and codon position 3 with anticodon position 1; pairing at codon position 3 is the loose one (wobble), which is why one tRNA can read several synonymous codons ([[Genetic Code#Deeper (L2)]], [[Transfer RNA]]).[^alberts]

## Advanced (L3)

- **Codons as integers.** Reading a codon as a base-4 number with digits T = 0, C = 1, A = 2, G = 3 gives its index 0 to 63 in the order used by NCBI translation tables, so a whole genetic code fits in a 64-character string and translation becomes array indexing ([[Genetic Code#Computational representation]], [[Array]]).[^ncbi] A codon fits in 6 bits, and a codon count table is a vector of 64 integers, the input of codon usage measures ([[Codon Usage Bias]]).
- **Codon-aware alignment.** When coding sequences are aligned nucleotide by nucleotide, gaps can cut codons and imply frameshifts that never happened. Translating, aligning the proteins and threading the codons back keeps every gap a multiple of 3 and every codon whole ([[Sequence Alignment]]).
- **Codons in evolution.** Codon substitution models describe the evolution of a coding sequence as a process on the 61 sense codons, which lets them separate synonymous from non-synonymous substitution rates; their ratio is used to detect selection on proteins ([[Codon Substitution Model]], [[Molecular Evolution]]).[^yang]
- **Context-dependent meaning.** A codon's meaning can depend on the organism (variant codes) or even on the mRNA context, as when UGA is read as selenocysteine ([[Genetic Code#Advanced (L3)]]).[^ncbi][^alberts] Code that assumes "TGA = stop" everywhere is wrong for some genes.

## Mathematical representation

- The set of codons is $\mathcal{C} = \Sigma^3$ with $\Sigma = \{T, C, A, G\}$ (DNA letters), $|\mathcal{C}| = 64$. The genetic code is a map $g : \mathcal{C} \to \mathcal{A} \cup \{*\}$; sense codons $S = g^{-1}(\mathcal{A})$, $|S| = 61$; stop codons $g^{-1}(*)$, 3 of them in the standard code.
- **Index.** With $r(T) = 0$, $r(C) = 1$, $r(A) = 2$, $r(G) = 3$, the map
$$\iota(c_1 c_2 c_3) = 16\, r(c_1) + 4\, r(c_2) + r(c_3)$$
is a bijection $\mathcal{C} \to \{0, \dots, 63\}$. Example: $\iota(ATG) = 16 \cdot 2 + 4 \cdot 0 + 3 = 35$.
- **Segmentation.** A CDS $x = x_1 \dots x_{3\ell}$ has codons $c_k = x_{3k-2}\, x_{3k-1}\, x_{3k}$, $k = 1, \dots, \ell$. Position $p$ maps to codon $k(p) = \lceil p/3 \rceil$ and in-codon position $j(p) = ((p-1) \bmod 3) + 1$; conversely $p = 3(k - 1) + j$.
- **Minus strand.** If a single-exon CDS occupies genome positions $[a, b]$ (1-based, inclusive) on the `-` strand, genome position $x$ is CDS position $p = b - x + 1$, and the CDS base there is the complement of the genome base.
- **Neighbourhood.** $N(c) = \{c' \in \mathcal{C} : c' \text{ differs from } c \text{ at exactly one position}\}$ has $|N(c)| = 9$, so there are $61 \times 9 = 549$ single-base substitutions from sense codons.

## Computational representation

```python
BASES = "TCAG"
TABLE_1 = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"   # NCBI table 1
RANK = {b: i for i, b in enumerate(BASES)}


def codon_index(codon: str) -> int:
    """0..63: the codon read as a base-4 number with digits T=0, C=1, A=2, G=3 (NCBI order)."""
    c = codon.upper().replace("U", "T")
    return 16 * RANK[c[0]] + 4 * RANK[c[1]] + RANK[c[2]]


def split_codons(cds: str) -> list[str]:
    if len(cds) % 3:
        raise ValueError(f"length {len(cds)} is not a multiple of 3")
    return [cds[i:i + 3] for i in range(0, len(cds), 3)]


def locate(p: int) -> tuple[int, int]:
    """1-based CDS position -> (codon number, position inside the codon), both 1-based."""
    return (p - 1) // 3 + 1, (p - 1) % 3 + 1


def signals(seq: str) -> list[tuple[int, str, str]]:
    """Every ATG or stop triplet in seq (1-based start), flagged in frame or not (frame of position 1)."""
    hits = []
    for i in range(len(seq) - 2):
        t = seq[i:i + 3]
        if t == "ATG" or TABLE_1[codon_index(t)] == "*":
            hits.append((i + 1, t, "in frame" if i % 3 == 0 else "out of frame"))
    return hits


cds = "ATGCATGACTGGTAA"                      # invented coding sequence
print(split_codons(cds))
print("".join(TABLE_1[codon_index(c)] for c in split_codons(cds)))
print(signals(cds))
print(codon_index("ATG"), codon_index("AUG"), TABLE_1[codon_index("UGG")])
print(locate(12), locate(1), locate(15))
```

```text
['ATG', 'CAT', 'GAC', 'TGG', 'TAA']
MHDW*
[(1, 'ATG', 'in frame'), (5, 'ATG', 'out of frame'), (6, 'TGA', 'out of frame'), (13, 'TAA', 'in frame')]
35 35 W
(4, 3) (1, 1) (5, 3)
```

`codon_index` accepts U or T, so the same table serves mRNA and DNA. A dictionary keyed by codon strings ([[Hash Table]]) is equally fast in Python; the integer index pays off in compiled code and in 2-bit packed sequences ([[Nucleotide#Computational representation]]).

## Worked example

> [!example] Reading a toy CDS and placing a variant (invented sequence)
> CDS: `ATGCATGACTGGTAA` (15 nt).
> 1. **Length**: $15 = 3 \times 5$: five codons.
> 2. **Segment**: ATG CAT GAC TGG TAA. First codon ATG (start), last codon TAA (stop), no stop in between: a complete CDS.
> 3. **Translate** with the [[Genetic Code]]: Met-His-Asp-Trp, then stop: a 4-residue peptide.
> 4. **Out-of-frame look-alikes**: ATG at position 5 and TGA at 6 are not codons of this frame ($5 - 1$ and $6 - 1$ are not multiples of 3).
> 5. **A variant at CDS position 12, G → A**: $k = \lceil 12/3 \rceil = 4$, $j = 3$. Codon 4 TGG becomes TGA, a stop: nonsense variant W4*, and the protein is cut to Met-His-Asp.

## Common misconceptions

> [!warning] "Every TAA, TAG or TGA in a gene is a stop codon"
> Only triplets in the reading frame are codons. The same letters straddling two codons, or lying in another frame, mean nothing to the ribosome; in a CDS they are common.

> [!warning] "Every codon codes for an amino acid"
> 61 do. The 3 stop codons code for none: no tRNA reads them in the standard code, and translation ends there. AUG has two roles: start signal and methionine inside the protein.[^os15]

> [!warning] "The codon is on the template strand" or "codon and anticodon are the same"
> The codon is on the mRNA, whose letters match the coding strand (T for U). The template strand and the tRNA anticodon carry complementary, antiparallel triplets.[^os15]

> [!warning] "Codon number = nucleotide position divided by 3"
> Position 12 is in codon 4 but position 13 is in codon 5: use $\lceil p/3 \rceil$ (or `(p - 1) // 3 + 1` with 1-based positions). Off-by-one errors here shift every variant to the wrong residue.

## Exercises

> [!question] Exercise 1 (L1)
> Segment the mRNA `AUGGAACUUUGGUAG` into codons, translate it, and give the number of sense codons.

> [!success]- Solution
> AUG GAA CUU UGG UAG → Met-Glu-Leu-Trp-stop. Four sense codons (AUG included) and one stop codon; the peptide has 4 residues.

> [!question] Exercise 2 (L1)
> In a CDS, which codon contains position 1, 3, 4 and 100, and at which position inside the codon?

> [!success]- Solution
> $p = 1$: codon 1, position 1. $p = 3$: codon 1, position 3. $p = 4$: codon 2, position 1. $p = 100$: $\lceil 100/3 \rceil = 34$, position $((100 - 1) \bmod 3) + 1 = 1$. Check with `locate(100)`, which returns `(34, 1)`.

> [!question] Exercise 3 (L2, Python)
> Find the sense codons of the standard code that are one substitution away from a stop codon, and count the single-base substitutions that turn a sense codon into a stop.

> [!success]- Solution
> ```python
> BASES = "TCAG"
> TABLE_1 = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
> CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES), TABLE_1))
>
> one_step = {}
> for codon, aa in CODE.items():
>     if aa == "*":
>         continue
>     stops = [codon[:p] + b + codon[p + 1:] for p in range(3) for b in BASES
>              if b != codon[p] and CODE[codon[:p] + b + codon[p + 1:]] == "*"]
>     if stops:
>         one_step[codon] = stops
> print(len(one_step), sum(len(v) for v in one_step.values()))
> print(sorted({CODE[c] for c in one_step}))
> print({c: v for c, v in sorted(one_step.items()) if len(v) > 1})
> ```
> Output: `18 23`, then the amino acids `['C', 'E', 'G', 'K', 'L', 'Q', 'R', 'S', 'W', 'Y']`, then the five codons with two routes to a stop: TAC, TAT, TCA, TGG and TTA. So 23 of the 549 possible substitutions (about 4 %) are nonsense; codons for the other 10 amino acids, including Met, can never become a stop in one step.

> [!question] Exercise 4 (L2)
> Compute $\iota$ for AUG, UAA and GGG, and check them against the NCBI table string `FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG` (0-based indexing).

> [!success]- Solution
> AUG: $16 \cdot 2 + 4 \cdot 0 + 3 = 35$, and character 35 is `M`. UAA: $16 \cdot 0 + 4 \cdot 2 + 2 = 10$, character 10 is `*`. GGG: $16 \cdot 3 + 4 \cdot 3 + 3 = 63$, the last character, `G` (glycine).

> [!question] Exercise 5 (L3, Python)
> An invented genome reads `GGTTACCAGTCATGCATCC` on its `+` strand, and a single-exon gene occupies positions 3 to 17 on the `-` strand. Which codon, and which position in it, does genome position 6 fall in? What does a C → T change at genome position 6 (on the `+` strand) do to the protein?

> [!success]- Solution
> ```python
> BASES = "TCAG"
> CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
>                 "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
> COMPLEMENT = str.maketrans("ACGT", "TGCA")
>
>
> def codon_at(genome: str, pos: int, cds_start: int, cds_end: int, strand: str) -> tuple[int, int, str]:
>     """Genome position (1-based) inside a single-exon CDS [cds_start, cds_end] (1-based, inclusive)
>     -> (codon number, position in codon, codon read on the gene's coding strand)."""
>     cds = genome[cds_start - 1:cds_end]
>     if strand == "-":
>         cds = cds.translate(COMPLEMENT)[::-1]
>         p = cds_end - pos + 1
>     else:
>         p = pos - cds_start + 1
>     k, j = (p - 1) // 3 + 1, (p - 1) % 3 + 1
>     return k, j, cds[3 * (k - 1):3 * k]
>
>
> genome = "GGTTACCAGTCATGCATCC"                   # invented; a gene on the - strand, 3..17
> k, j, codon = codon_at(genome, 6, 3, 17, "-")
> print(k, j, codon, CODE[codon])
> mutant = genome[:5] + "T" + genome[6:]           # + strand C>T at position 6
> k, j, codon = codon_at(mutant, 6, 3, 17, "-")
> print(k, j, codon, CODE[codon])
> ```
> Output: `4 3 TGG W`, then `4 3 TGA *`. The CDS read on the `-` strand is `ATGCATGACTGGTAA`, the toy CDS of the worked example. Genome position 6 is CDS position $17 - 6 + 1 = 12$: codon 4, third base. On the coding strand a `+` strand C → T is a G → A change, so TGG (Trp) becomes TGA: a nonsense variant. Reporting it as "C → T" in a codon table would be wrong: the strand must be converted first.

> [!question] Exercise 6 (L3)
> Two homologous coding sequences are aligned. Alignment A, made nucleotide by nucleotide, contains a 2-nt gap; alignment B, made by aligning the proteins and threading the codons back, contains a 3-nt gap in the same region. Assuming both sequences encode full-length, functional proteins, which alignment is biologically plausible, and why?

> [!success]- Solution
> B. A 2-nt gap means one sequence has two extra nucleotides relative to the other, which would shift the reading frame of everything downstream ([[Frameshift Mutation]]); a functional full-length protein in both species makes that unlikely. A 3-nt gap is one whole codon, one amino acid inserted or deleted, which keeps the frame. Nucleotide aligners minimize a score without knowing about codons, so they can prefer the 2-nt gap; codon-aware alignment restricts gaps to whole codons.

## Mastery checklist

- [ ] 1 Recognized: I can define a codon, give the number of codons, name the start codon and the three stop codons.
- [ ] 2 Understood: I can explain triplet reading from a fixed start, the relation between codon, coding strand, template strand and anticodon, and why only in-frame signals count.
- [ ] 3 Practiced: I can segment a CDS, convert between nucleotide positions and codon positions, index codons as integers, and solve the exercises.
- [ ] 4 Applied: in [[02-sequence-translation]] and [[bio-core]], my Codon type validates input and maps real variant positions, on both strands, to codons.
- [ ] 5 Explained: I can teach why codon position matters for variant effects, codon-aware alignment and codon-level evolutionary models.

## References

[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (the genetic code: triplet codons, start codon, nonsense or stop codons).
[^crick61]: [[Crick 1961 - General Nature of the Genetic Code for Proteins]], Crick FHC, Barnett L, Brenner S, Watts-Tobin RJ, *Nature* 192:1227-1232.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of the genetic code, tRNAs and wobble, and translation termination.
[^ncbi]: [[NCBI Genetic Codes]], "The Genetic Codes" (NCBI Taxonomy), translation tables in TCAG codon order and their start codons.
[^yang]: [[Molecular Evolution (Yang)]], codon substitution models and the detection of natural selection.
