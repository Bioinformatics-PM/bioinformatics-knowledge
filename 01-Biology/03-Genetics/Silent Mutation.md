---
aliases:
  - Synonymous Mutation
  - Synonymous Substitution
  - Synonymous Variant
  - synonymous_variant
  - Mutation silencieuse
  - Mutation synonyme
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Point Mutation]]"
  - "[[Genetic Code]]"
  - "[[Codon]]"
related:
  - "[[Mutation]]"
  - "[[Missense Mutation]]"
  - "[[Nonsense Mutation]]"
  - "[[Codon Usage Bias]]"
  - "[[Molecular Evolution]]"
  - "[[Codon Substitution Model]]"
  - "[[McDonald-Kreitman Test]]"
  - "[[Purifying Selection]]"
  - "[[Variant Annotation]]"
  - "[[RNA Processing]]"
projects:
  - "[[06-mutation-lab]]"
  - "[[03-genome-diff]]"
sources:
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Ensembl]]"
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Silent Mutation

> [!abstract]
> A silent mutation changes a codon into another codon for the same amino acid: the DNA and the mRNA change, the protein sequence does not, because the genetic code has several codons for most amino acids.

## Definition

A **silent** (or **synonymous**) mutation is a point mutation in a coding sequence that replaces a codon by a synonymous codon, one that specifies the same amino acid, so the encoded amino acid sequence is unchanged.[^griffiths] It is possible because the [[Genetic Code]] is degenerate: most amino acids are encoded by two to six codons.[^os15] "Silent" describes the **protein sequence** only; annotation tools call such a change a `synonymous_variant`.[^ensembl]

## Why it matters

- **Variant annotation.** Consequence predictors report synonymous variants per transcript ([[Variant Annotation]]).[^ensembl] They are often filtered out first, but clinical guidelines accept a synonymous variant as supporting evidence of benignity only when splicing predictions show no effect on the splice consensus and no new splice site, and the nucleotide is not highly conserved.[^richards]
- **A baseline for selection.** Comparing the rate of synonymous changes with that of amino acid-changing ones, the ratio $\omega = d_N/d_S$, measures selection on proteins ([[Molecular Evolution]], [[Codon Substitution Model]], [[McDonald-Kreitman Test]]).[^yang]
- **Mutation simulation.** [[06-mutation-lab]] shows a silent change as a DNA and codon change with an identical protein; [[03-genome-diff]] must translate before calling a change silent.

## Core (L1)

### Synonymous codons

Codons that differ only at the third position usually encode the same amino acid: XYU and XYC always do, XYA and XYG usually do.[^berg] Examples from the standard code:

| Amino acid | Codons | A silent change |
|---|---|---|
| Ala | GCU, GCC, GCA, GCG | GCU → GCC |
| Glu | GAA, GAG | GAA → GAG |
| Leu | UUA, UUG, CUU, CUC, CUA, CUG | UUA → CUA (first position) |
| Met | AUG only | none possible |

### Degeneracy of a position

A codon position is **n-fold degenerate** when $n$ of the four possible bases there give the same amino acid:

- **fourfold**: any base keeps the amino acid (third position of GCN, Ala);
- **twofold**: two bases do (third position of GAR, Glu, where R is A or G);
- **threefold**: only the third position of the Ile codons (AUU, AUC, AUA);
- **non-degenerate**: every change alters the amino acid (all positions of AUG, and every second position).

![[synonymous-site-degeneracy.svg]]

Silent changes happen mostly at third positions, sometimes at first positions (Leu and Arg codons), and never at second positions in the standard code ([[Genetic Code#Advanced (L3)]] counts them).

### Stop to stop

UAA → UAG or UAA → UGA keeps a stop codon: the protein is unchanged. Annotation tools report this separately, as a stop retained variant, rather than as synonymous.[^ensembl]

## Deeper (L2)

### Counting synonymous sites

To compare rates, silent changes must be counted relative to how many silent changes were **possible**. Each position of a codon contributes the fraction of its three possible changes that are synonymous; the sum is the codon's number of **synonymous sites** $s$, and $n = 3 - s$ its nonsynonymous sites.[^yang] The figure above gives $s$ for five codons: 1 for GCU, $4/3$ for CUA (its first-position C → U is silent too), 0 for AUG.

A coding sequence of $L$ codons has $S = \sum s$ synonymous and $N = 3L - S$ nonsynonymous sites. Averaged over the 61 sense codons, about a quarter of all possible changes are synonymous (134 of 549, [[Mutation#Mathematical representation]]).

### From counts to $d_N/d_S$

Between two aligned coding sequences, count synonymous differences $S_d$ and nonsynonymous differences $N_d$. The proportions $p_S = S_d/S$ and $p_N = N_d/N$ are corrected for multiple substitutions at the same site to give $d_S$ and $d_N$.[^yang] Their ratio $\omega = d_N/d_S$ reads as: $\omega < 1$, amino acid changes are removed ([[Purifying Selection]]); $\omega \approx 1$, they are as free as silent ones (neutral evolution); $\omega > 1$, they are favoured ([[Positive Selection]]).[^yang]

Transitions are more often silent than transversions ([[Mutation#Mathematical representation]]), so counts of synonymous sites that ignore the transition bias misjudge the silent fraction; codon models include the transition/transversion rate ratio for this reason ([[Point Mutation]]).[^yang]

## Advanced (L3)

"Silent" is a statement relative to three references, and each can change the answer.

- **The genetic code table.** AUA → AUG is Ile → Met (missense) in the standard code, but Met → Met (silent) in the vertebrate mitochondrial code, where UGA → UGG also becomes silent (Trp → Trp).[^ncbi] Using the wrong table misclassifies organelle variants (Exercise 5).
- **The reading frame.** Where two genes or open reading frames overlap in different frames, a change silent in one frame can be missense or nonsense in the other ([[Reading Frame]], Exercise 4).
- **The transcript.** A position can be coding in one isoform and untranslated or intronic in another ([[Alternative Splicing]]); tools therefore give a consequence per transcript.[^ensembl]

**Silent is not neutral.** The DNA and mRNA did change. Beyond the splicing signals that clinical guidelines check,[^richards] synonymous codons are not used equally within genomes ([[Codon Usage Bias]]), and codon models include codon frequencies to account for this unequal use.[^yang] Synonymous sites are therefore a convenient, not a perfect, neutral reference: a low $d_S$ can reflect selection on codon use as well as a low mutation rate.

## Mathematical representation

Let $g : \Sigma^3 \to \mathcal{A} \cup \{*\}$ be the code ([[Genetic Code#Mathematical representation]]) and $c[i \leftarrow b]$ the codon $c$ with base $b$ at position $i$.

- A substitution $c \to c' = c[i \leftarrow b]$, $b \ne c_i$, is **silent** iff $g(c') = g(c) \ne *$.
- **Degeneracy** of position $i$: $D_i(c) = \big|\{ b \in \Sigma : g(c[i \leftarrow b]) = g(c) \}\big| \in \{1, 2, 3, 4\}$.
- **Synonymous sites**: $s(c) = \sum_{i=1}^{3} \frac{D_i(c) - 1}{3}$, $n(c) = 3 - s(c)$; for a CDS, $S = \sum_k s(c_k)$ over its sense codons and $N = 3L - S$. Here changes to a stop codon count as nonsynonymous; published methods differ on this point, so check the convention before comparing numbers.
- **Proportions**: $p_S = S_d / S$, $p_N = N_d / N$, and $\omega = d_N / d_S$ after correction for multiple hits.

## Computational representation

Site degeneracy is computed by trying the three alternative bases at each position; the table is a parameter, as in [[Genetic Code#Computational representation]].

```python
BASES = "TCAG"
CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]
TABLES = {  # NCBI translation tables, amino acids in TCAG codon order
    1: "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
    2: "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG",
}


def code(table_id: int = 1) -> dict[str, str]:
    return dict(zip(CODONS, TABLES[table_id]))


def degeneracy(codon: str, pos: int, table: dict[str, str]) -> int:
    """How many of the 4 bases at this position keep the same amino acid (1 to 4)."""
    return sum(table[codon[:pos] + b + codon[pos + 1:]] == table[codon] for b in BASES)


def synonymous_sites(cds: str, table: dict[str, str]) -> tuple[float, float]:
    """(S, N): each position contributes the fraction of its 3 possible changes that are silent.
    Changes to a stop codon count as nonsynonymous; the final stop codon is excluded."""
    s = 0.0
    codons = [cds[i:i + 3] for i in range(0, len(cds) - 3, 3)]      # drop the stop codon
    for codon in codons:
        s += sum((degeneracy(codon, p, table) - 1) / 3 for p in range(3))
    return s, 3 * len(codons) - s


std = code(1)
cds = "ATGGCTCTAAAGATTTGGTAA"                  # invented: Met Ala Leu Lys Ile Trp stop
for i in range(0, len(cds) - 3, 3):
    codon = cds[i:i + 3]
    print(codon, std[codon], [degeneracy(codon, p, std) for p in range(3)])
S, N = synonymous_sites(cds, std)
print(f"S = {S:.3f}, N = {N:.3f}")
```

```text
ATG M [1, 1, 1]
GCT A [1, 1, 4]
CTA L [2, 1, 4]
AAG K [1, 1, 2]
ATT I [1, 1, 3]
TGG W [1, 1, 1]
S = 3.333, N = 14.667
```

Fourfold-degenerate positions (here the third bases of GCT and CTA) are the sites where every possible change is silent, which makes them the natural candidates when an analysis needs sites that do not touch the protein (with the caveats of L3).

## Worked example

> [!example] All silent options in a toy CDS (invented)
> CDS `ATG GCT CTA AAG ATT TGG TAA` (Met Ala Leu Lys Ile Trp stop), standard code.
>
> 1. **ATG** (Met) and **TGG** (Trp): no silent change possible; 0 synonymous sites.
> 2. **GCT** (Ala): GCC, GCA, GCG are silent (fourfold third position): 1 site. **CTA** (Leu): CTT, CTC, CTG, and also TTA at the first position: $1 + 1/3 = 4/3$ sites.
> 3. **AAG** (Lys): only AAA is silent ($1/3$); AAC and AAT give Asn. **ATT** (Ile): ATC and ATA are silent, ATG gives Met ($2/3$).
> 4. $S = 10/3 \approx 3.33$ of 18 sense-codon sites, matching the code output: under 20 % of the positions of this short gene can change without changing the protein.

## Common misconceptions

> [!warning] "Silent changes only happen at the third codon position"
> First positions can be silent too: UUA ↔ CUA and UUG ↔ CUG (Leu), AGA ↔ CGA and AGG ↔ CGG (Arg).

> [!warning] "A synonymous variant is synonymous everywhere"
> It is synonymous for one transcript, one reading frame and one code table. Change any of the three and the same DNA change can become missense.[^ncbi][^ensembl]

> [!warning] "Synonymous sites evolve neutrally, so $d_S$ is a pure mutation clock"
> Synonymous codons are used unequally and synonymous changes can affect RNA-level signals, so $d_S$ also carries selection.[^yang][^richards]

## Exercises

> [!question] Exercise 1 (L1)
> With the standard code, classify: (a) GCU → GCC, (b) AUG → AUA, (c) UUA → CUA, (d) CGA → AGA, (e) UAC → UAA, (f) UAA → UGA.

> [!success]- Solution
> (a) Ala → Ala: silent (third position). (b) Met → Ile: missense. (c) Leu → Leu: silent (first position). (d) Arg → Arg: silent (first position). (e) Tyr → stop: nonsense. (f) stop → stop: no protein change, reported as stop retained rather than synonymous.

> [!question] Exercise 2 (L1)
> Why can no silent mutation occur in the codons AUG and UGG of the standard code, and why is no second-position change ever silent?

> [!success]- Solution
> Met and Trp each have a single codon, so any change alters the amino acid (or creates a stop: UGG → UGA or UAG). At the second position, the table's columns (fixed second base) never share an amino acid across rows: changing the middle base always moves the codon to a block of a different amino acid.

> [!question] Exercise 3 (L2, Python)
> Two invented aligned coding sequences differ at a few codons, each at one position only: `ATGGCTCTAAAGATTTGGGAAAGCCCGTTCTAA` and `ATGGCCCTGAAGATTTGGGATAGCCCGTTCTAA`. Using `code` and `synonymous_sites` from the code above, count synonymous and nonsynonymous differences and compute $p_N/p_S$ (uncorrected).

> [!success]- Solution
> ```python
> def count_differences(cds1: str, cds2: str, table: dict[str, str]) -> tuple[int, int]:
>     """(synonymous, nonsynonymous) differences, for codons that differ at one position only."""
>     sd = nd = 0
>     for i in range(0, len(cds1) - 3, 3):
>         c1, c2 = cds1[i:i + 3], cds2[i:i + 3]
>         if c1 != c2:
>             assert sum(a != b for a, b in zip(c1, c2)) == 1, "one difference per codon"
>             if table[c1] == table[c2]:
>                 sd += 1
>             else:
>                 nd += 1
>     return sd, nd
>
>
> seq1 = "ATGGCTCTAAAGATTTGGGAAAGCCCGTTCTAA"      # invented aligned coding sequences
> seq2 = "ATGGCCCTGAAGATTTGGGATAGCCCGTTCTAA"
> sd, nd = count_differences(seq1, seq2, std)
> S = (synonymous_sites(seq1, std)[0] + synonymous_sites(seq2, std)[0]) / 2
> N = 3 * (len(seq1) // 3 - 1) - S
> pS, pN = sd / S, nd / N
> print(f"Sd = {sd}, Nd = {nd}, S = {S:.2f}, N = {N:.2f}, pS = {pS:.3f}, pN = {pN:.3f}, pN/pS = {pN / pS:.2f}")
> # Sd = 2, Nd = 1, S = 5.33, N = 24.67, pS = 0.375, pN = 0.041, pN/pS = 0.11
> ```
>
> Two of the three differences are silent (GCT → GCC, CTA → CTG) and one is missense (GAA → GAT, Glu → Asp), yet silent sites are only about 18 % of the sites: per available site, silent changes are about nine times more frequent. On real genes, $p_N/p_S$ well below 1 is the signature of purifying selection. With $p_S$ this high, a multiple-hit correction would matter ([[Jukes-Cantor Model]]).

> [!question] Exercise 4 (L3, Python)
> In the invented sequence `GCTCTGGCAGC`, one gene is read in frame 0 and an overlapping gene in frame +1. Using `std` from the code above, translate both frames before and after the change G → A at position 5 (0-based), and explain the result.

> [!success]- Solution
> ```python
> def translate(seq: str, frame: int, table: dict[str, str]) -> str:
>     return "".join(table[seq[i:i + 3]] for i in range(frame, len(seq) - 2, 3))
>
>
> seq = "GCTCTGGCAGC"                              # invented overlap of two reading frames
> mut = seq[:5] + "A" + seq[6:]                    # G -> A at position 5 (0-based)
> for frame in (0, 1):
>     print(frame, translate(seq, frame, std), "->", translate(mut, frame, std))
> # 0 ALA -> ALA
> # 1 LWQ -> L*Q
> ```
>
> In frame 0 the base is the third position of CTG (Leu), and CTA is still Leu: silent. In frame +1 the same base is the second position of TGG (Trp), which becomes TAG, a stop: nonsense. A third position in one frame is a second position in the frame shifted by +1, and second positions are never degenerate, so overlapping genes leave few truly silent sites.

> [!question] Exercise 5 (L3, Python)
> Using `code`, `CODONS` and `BASES` from the code above, list the single-base changes that keep the codon's meaning in the vertebrate mitochondrial code (table 2) but not in the standard code, and vice versa.

> [!success]- Solution
> ```python
> mito = code(2)
>
>
> def silent_changes(table: dict[str, str]) -> set[tuple[str, str]]:
>     """All single-base codon changes that keep the same meaning (amino acid or stop)."""
>     return {(c, c[:p] + b + c[p + 1:]) for c in CODONS for p in range(3) for b in BASES
>             if b != c[p] and table[c[:p] + b + c[p + 1:]] == table[c]}
>
>
> only_mito = silent_changes(mito) - silent_changes(std)
> only_std = silent_changes(std) - silent_changes(mito)
> print(sorted(only_mito))
> print(sorted(only_std))
> # [('ATA', 'ATG'), ('ATG', 'ATA'), ('TGA', 'TGG'), ('TGG', 'TGA')]
> # [('AGA', 'CGA'), ('AGG', 'CGG'), ('ATA', 'ATC'), ('ATA', 'ATT'), ('ATC', 'ATA'), ('ATT', 'ATA'), ('CGA', 'AGA'), ('CGG', 'AGG'), ('TAA', 'TGA'), ('TGA', 'TAA')]
> ```
>
> In mitochondria, ATA ↔ ATG (Met) and TGA ↔ TGG (Trp) become silent; ATA ↔ ATT/ATC (Ile in the standard code) and the Arg first-position pairs AGR ↔ CGR stop being silent because AGA and AGG are stops there.[^ncbi] A variant annotator must use table 2 for human mitochondrial genes.

## Mastery checklist

- [ ] 1 Recognized: I can define a silent (synonymous) mutation and give examples.
- [ ] 2 Understood: I can explain site degeneracy, why silent changes are mostly at third positions, and why silent does not mean neutral.
- [ ] 3 Practiced: I can compute synonymous sites, $S$, $N$ and $p_N/p_S$ by hand and in Python.
- [ ] 4 Applied: I annotated real variants with the correct transcript and code table and compared my synonymous calls with a consequence predictor.
- [ ] 5 Explained: I can teach how $d_N/d_S$ uses silent changes as a baseline, and the transcript, frame, code-table and RNA-level caveats.

## References

[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of gene mutation (synonymous, or silent, substitutions).
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (the genetic code and its degeneracy).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of the genetic code (synonyms differ mostly at the third base).
[^ensembl]: [[Ensembl]], Variant Effect Predictor: consequence types, reported per transcript.
[^richards]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], Richards S et al., *Genetics in Medicine* 17(5):405-424, benign criterion for synonymous variants.
[^yang]: [[Molecular Evolution (Yang)]], codon substitution models and the estimation of synonymous and nonsynonymous rates.
[^ncbi]: [[NCBI Genetic Codes]], translation tables 1 (standard) and 2 (vertebrate mitochondrial).
