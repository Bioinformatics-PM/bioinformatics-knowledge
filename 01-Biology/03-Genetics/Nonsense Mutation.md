---
aliases:
  - Stop-Gain Mutation
  - Stop Gained
  - stop_gained
  - Mutation non-sens
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
  - "[[Translation]]"
related:
  - "[[Mutation]]"
  - "[[Missense Mutation]]"
  - "[[Silent Mutation]]"
  - "[[Frameshift Mutation]]"
  - "[[Nonsense-Mediated Decay]]"
  - "[[RNA Processing]]"
  - "[[Gene Annotation]]"
  - "[[Variant Annotation]]"
  - "[[Variant Classification]]"
projects:
  - "[[06-mutation-lab]]"
  - "[[03-genome-diff]]"
sources:
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Nagy 1998 - A Rule for Termination-Codon Position Within Intron-Containing Genes]]"
  - "[[Ensembl]]"
  - "[[den Dunnen 2016 - HGVS Recommendations for the Description of Sequence Variants]]"
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
---

# Nonsense Mutation

> [!abstract]
> A nonsense mutation turns a codon for an amino acid into a stop codon: translation ends too early, and the cell usually destroys the faulty mRNA before much truncated protein is made.

## Definition

A **nonsense mutation** is a nucleotide substitution that changes a sense codon into one of the three stop codons, UAA, UAG or UGA (TAA, TAG, TGA in DNA). The new **premature termination codon** (PTC) ends translation early, so the product is truncated.[^griffiths][^os15] Ensembl's Variant Effect Predictor calls the consequence `stop_gained` and gives it a HIGH impact.[^ensembl] It is one effect class of a [[Point Mutation]], next to [[Silent Mutation|silent]] and [[Missense Mutation|missense]] changes.

## Why it matters

- **A loss-of-function class.** Clinical guidelines list nonsense variants among "null" variants (with frameshift, canonical splice-site, start-codon and exon-deletion variants): in a gene where loss of function causes disease, this is very strong evidence of pathogenicity (criterion PVS1), with explicit cautions.[^richards]
- **The outcome depends on the transcript.** Whether the mRNA is destroyed or translated into a short protein depends on where the stop lies relative to the exon-exon junctions,[^nagy] so predicting it needs the exon structure from the annotation ([[Gene Annotation]], [[Variant Annotation]]).
- **Lab.** [[06-mutation-lab]] shows the stop appearing and the protein being cut; [[03-genome-diff]] reports `stop_gained` variants. Both give the **molecular consequence only**, never a clinical prediction.

## Core (L1)

### Which codons are one step from a stop

A sense codon can become a stop by one substitution only if it differs from TAA, TAG or TGA at a single position. Listing the neighbours of the three stops gives 18 such codons, for 10 amino acids:

| Amino acid | Codons one step from a stop | Nonsense substitutions |
|---|---|---:|
| Tyr | TAT, TAC | 4 |
| Leu | TTA, TTG | 3 |
| Ser | TCA, TCG | 3 |
| Trp, Cys, Gln, Arg, Lys, Glu | TGG; TGT, TGC; CAA, CAG; AGA, CGA; AAA, AAG; GAA, GAG | 2 each |
| Gly | GGA | 1 |

Met, Phe, Pro, His, Asn, Asp, Ile, Val, Ala and Thr can never become a stop in one step. Overall, 23 of the 549 single-base changes of sense codons (4.2 %) are nonsense ([[Mutation#Mathematical representation]]).

### What happens to the protein

If a PTC replaces codon $k$ (Met = 1) and the mRNA is translated, the ribosome releases a chain of $k - 1$ amino acids: the N-terminal part of the protein, without everything downstream ([[Translation]]). The earlier the stop, the less of the protein remains. HGVS writes the change `p.Trp3Ter` or `p.Trp3*`.[^hgvs]

```text
reference   ATG GAA TGG AAA TAC TAA      Met-Glu-Trp-Lys-Tyr-stop
TGG > TAG   ATG GAA TAG AAA TAC TAA      Met-Glu-stop            p.Trp3Ter
```

(Invented toy sequence.) Compare with a [[Missense Mutation]] (one residue changed, length kept) and a [[Frameshift Mutation]] (a stretch of wrong residues, then usually a premature stop).

## Deeper (L2)

### Nonsense-mediated decay

In eukaryotic cells, an mRNA that carries a PTC is recognized during translation and degraded by **nonsense-mediated decay** (NMD), which limits the production of truncated proteins.[^alberts] Nagy and Maquat summarized where a stop must lie to trigger it: only stops located **more than 50-55 nucleotides upstream of the last exon-exon junction** mediate decay.[^nagy] The mechanism behind the rule: splicing leaves protein complexes near each exon-exon junction; the first ribosome removes those it passes; if it stops while a complex remains downstream, decay follows ([[Nonsense-Mediated Decay]], [[RNA Processing]]).[^alberts]

![[nmd-premature-stop-position.svg]]

Three consequences follow directly from the rule:

- a normal stop codon in the last exon has no junction downstream, so it never triggers decay;
- a PTC in the last exon, or in the last 50-55 nt of the second-to-last exon, **escapes** NMD: a truncated protein is made, which may be inactive, partly active or harmful depending on what it lost;
- a PTC further upstream usually removes most of the product of that allele, whatever the protein would have looked like.

### Transcripts and hotspots

- **One variant, several transcripts.** A genomic variant can lie in the last exon of one transcript and in an internal exon of another, so the NMD prediction is made per transcript; guidelines ask for caution with nonsense variants at the extreme 3' end of a gene and in genes with several transcripts.[^richards]
- **CpG hotspots.** Deamination of 5-methylcytosine makes C → T transitions frequent at CpG sites ([[Mutation#Where mutations come from]]). The arginine codon CGA contains a CpG, and a C → T transition at that CpG gives TGA, a stop: CGA codons are candidate nonsense hotspots. Of the 23 nonsense substitutions, only 5 are transitions, all C → T or G → A (Exercise 4).

## Advanced (L3)

### From consequence to interpretation

PVS1 applies to a null variant **in a gene where loss of function is a known disease mechanism**; a nonsense variant in a gene where disease comes from gain of function says little. The guidelines' cautions match the biology above: loss-of-function variants at the extreme 3' end of a gene, and the presence of multiple transcripts.[^richards] A pipeline that labels a variant `stop_gained` has only done the first step: the interpretation needs the transcript model, the NMD prediction and the disease mechanism ([[Variant Classification]]).

### Related stop classes

Annotation distinguishes `stop_gained` from `stop_lost`, where the normal stop becomes a sense codon and the ribosome reads on into the 3' UTR, and from `start_lost`, where the start codon is destroyed.[^ensembl] A [[Frameshift Mutation]] also creates a premature stop downstream of the indel, but it is classified as a frameshift, not as nonsense.

## Mathematical representation

Let $g$ be the genetic code and $S = g^{-1}(*) = \{TAA, TAG, TGA\}$. A substitution $c \to c'$ is **nonsense** if and only if

$$g(c) \ne * \quad \text{and} \quad c' \in S.$$

- The sense codons one step from a stop are $N(S) \setminus S$, with $N$ the Hamming-1 neighbourhood; $|N(S) \setminus S| = 18$, and there are 23 nonsense substitutions among the $61 \times 9 = 549$ single-base changes of sense codons.
- A PTC at codon $k$ leaves a protein of $k - 1$ residues if translated.
- **NMD rule.** Let $J_1 < \dots < J_m$ be the transcript positions of the last base of each exon except the last, and $e$ the position of the last base of the PTC. With threshold $\theta \approx 50\text{-}55$,

$$\text{NMD predicted} \iff m \ge 1 \ \text{and}\ J_m - e > \theta.$$

## Computational representation

```python
BASES = "TCAG"
CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
                "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
THREE = dict(zip("ACDEFGHIKLMNPQRSTVWY*",
                 "Ala Cys Asp Glu Phe Gly His Ile Lys Leu Met Asn Pro Gln Arg Ser Thr Val Trp Tyr Ter".split()))

def nonsense_snvs(cds: str) -> list[tuple[int, str, str, str]]:
    """Every single-base substitution that turns a sense codon of the CDS into a stop.
    Returns (0-based position, ref base, alt base, protein change)."""
    hits = []
    for k in range(len(cds) // 3 - 1):                  # the last codon is the normal stop
        codon = cds[3 * k:3 * k + 3]
        for j in range(3):
            for b in BASES:
                new = codon[:j] + b + codon[j + 1:]
                if b != codon[j] and CODE[new] == "*":
                    hits.append((3 * k + j, codon[j], b, f"p.{THREE[CODE[codon]]}{k + 1}Ter"))
    return hits

def nmd_predicted(ptc_codon: int, junctions: list[int], threshold: int = 50) -> bool:
    """50-55 nt rule. ptc_codon: 1-based codon number of the premature stop.
    junctions: transcript positions (1-based) of the last base of every exon but the last.
    Coordinates here start at the A of ATG (no 5' UTR), which does not change distances."""
    if not junctions:
        return False                                    # intronless: no junction downstream
    stop_end = 3 * ptc_codon                            # last base of the stop codon
    return junctions[-1] - stop_end > threshold

cds = "ATGTGGCAACGATACGGTTAA"                            # invented: Met-Trp-Gln-Arg-Tyr-Gly-stop
for hit in nonsense_snvs(cds):
    print(hit)

junctions = [90, 210]                                   # invented 3-exon gene, CDS of 100 codons
for codon in (20, 60, 80):
    print(codon, "NMD" if nmd_predicted(codon, junctions) else "escapes NMD")
```

Output:

```text
(4, 'G', 'A', 'p.Trp2Ter')
(5, 'G', 'A', 'p.Trp2Ter')
(6, 'C', 'T', 'p.Gln3Ter')
(9, 'C', 'T', 'p.Arg4Ter')
(14, 'C', 'A', 'p.Tyr5Ter')
(14, 'C', 'G', 'p.Tyr5Ter')
20 NMD
60 escapes NMD
80 escapes NMD
```

Real annotation works in transcript coordinates that include the 5' UTR and takes junction positions from the annotation file ([[GFF Format]]); only differences of positions matter for the rule.

## Worked example

> [!example] Three premature stops in one invented gene
> A coding sequence of 100 codons (300 nt, stop included) is split over three exons: exon 1 holds nt 1-90, exon 2 nt 91-210, exon 3 nt 211-300. The last junction is after nt 210 (see the figure).
>
> 1. **PTC at codon 20** (nt 58-60): $210 - 60 = 150 > 50$. NMD predicted: little or no protein from this allele.
> 2. **PTC at codon 60** (nt 178-180): $210 - 180 = 30$, below the threshold. The mRNA escapes decay and makes a protein of 59 residues instead of 99.
> 3. **PTC at codon 80** (nt 238-240): in the last exon, no junction downstream. Escapes; protein of 79 residues.
>
> The same class (`stop_gained`) gives opposite molecular outcomes: loss of the product in case 1, a truncated protein in cases 2 and 3. Which is worse for the cell depends on the protein, and neither is a clinical verdict.

## Common misconceptions

> [!warning] "A nonsense mutation produces a truncated protein"
> Only if the mRNA escapes decay. For most premature stops upstream of the last exon, NMD destroys the mRNA and little truncated protein is made.[^alberts][^nagy]

> [!warning] "Every premature stop is a nonsense mutation"
> Frameshifts also lead to premature stops, a few codons after the indel. Annotation calls them `frameshift_variant`, not `stop_gained`, because the reading frame changed first ([[Frameshift Mutation]]).

> [!warning] "A stop is a stop, wherever it is"
> A stop in the last codons removes a few residues; one near the start removes almost everything; and the position relative to the junctions decides decay. Guidelines ask for caution at the 3' end of genes for this reason.[^richards]

## Exercises

> [!question] Exercise 1 (L1)
> Which of these codons can become a stop by one substitution, and how: TGG, TTT, CGA, GCC, TAC, CAG?

> [!success]- Solution
> TGG → TAG or TGA (Trp); CGA → TGA (Arg); TAC → TAA or TAG (Tyr); CAG → TAG (Gln). TTT (Phe) and GCC (Ala) cannot: every stop differs from them at two or three positions.

> [!question] Exercise 2 (L1)
> Toy CDS `ATG GAA TGG AAA TAC TAA` (invented). Give the protein change and the length of the product for G → T at position 3 and C → G at position 14 (0-based).

> [!success]- Solution
> Position 3: GAA → TAA, `p.Glu2Ter`, product Met only (1 residue). Position 14: TAC → TAG, `p.Tyr5Ter`, product Met-Glu-Trp-Lys (4 residues). `nonsense_snvs("ATGGAATGGAAATACTAA")` lists both among its 6 nonsense changes.

> [!question] Exercise 3 (L2)
> A gene's CDS spans three exons with the junctions after nt 120 and nt 250. Predict NMD for PTCs at codons 30, 66, 70 and 95, with the 50 and the 55 nt thresholds.

> [!success]- Solution
> Distances from the last base of the stop to the last junction (250): codon 30 ends at 90, distance 160: NMD. Codon 66 ends at 198, distance 52: NMD with 50, escape with 55: the rule is a range, and this case is undecided. Codon 70 ends at 210, distance 40: escapes. Codon 95 ends at 285, in the last exon: escapes. With `nmd_predicted(66, [120, 250])` and `threshold=55` the answer flips.

> [!question] Exercise 4 (L2, Python)
> Using `CODE`, `BASES` and `THREE` from the code above, count the nonsense substitutions of the whole code per amino acid, and how many are transitions. Relate the transitions to CpG sites.

> [!success]- Solution
> ```python
> from collections import Counter
>
> PURINES = set("AG")
> routes, kinds = Counter(), Counter()
> for codon, aa in CODE.items():
>     if aa == "*":
>         continue
>     for j in range(3):
>         for b in BASES:
>             if b != codon[j] and CODE[codon[:j] + b + codon[j + 1:]] == "*":
>                 routes[THREE[aa]] += 1
>                 kinds["Ts" if (codon[j] in PURINES) == (b in PURINES) else "Tv"] += 1
> print(sum(routes.values()), dict(routes.most_common()))
> print(dict(kinds))
> # 23 {'Tyr': 4, 'Leu': 3, 'Ser': 3, 'Cys': 2, 'Trp': 2, 'Gln': 2, 'Arg': 2, 'Lys': 2, 'Glu': 2, 'Gly': 1}
> # {'Tv': 18, 'Ts': 5}
> ```
>
> The 5 transitions are CAA → TAA, CAG → TAG, CGA → TGA (C → T) and TGG → TAG, TGG → TGA (G → A). Of these codons only CGA carries a CpG, so C → T transitions at methylated CpG sites can turn Arg CGA codons into TGA stops ([[Mutation#Where mutations come from]]).

> [!question] Exercise 5 (L3)
> A variant creates a stop at codon 410 of transcript 1, where it lies in the last exon, and at codon 410 of transcript 2, where exon 9 of 12 contains it, far from the last junction. What do you predict for each transcript, what does [[06-mutation-lab]] report, and what would a clinical interpretation need?

> [!success]- Solution
> Transcript 1: no junction downstream, escapes NMD, truncated protein. Transcript 2: more than 55 nt upstream of the last junction, NMD predicted. The lab reports `stop_gained` with both molecular predictions, per transcript. A clinical interpretation needs to know which transcript matters in the relevant tissue, whether loss of function causes the disease, and the other evidence types; the guidelines ask for caution precisely with 3'-end variants and multiple transcripts.[^richards]

## Mastery checklist

- [ ] 1 Recognized: I can define a nonsense mutation and name the three stop codons.
- [ ] 2 Understood: I can list the codons one step from a stop and explain NMD and the 50-55 nt rule.
- [ ] 3 Practiced: I can enumerate nonsense substitutions of a CDS and predict NMD from exon junctions in Python.
- [ ] 4 Applied: in [[06-mutation-lab]] and [[03-genome-diff]], I report `stop_gained` variants of a real gene with the truncated length and an NMD prediction per transcript.
- [ ] 5 Explained: I can explain why the same class gives decay or a truncated protein, the CpG hotspot, and why PVS1 depends on the disease mechanism.

## References

[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of gene mutation (nonsense mutations and their effect on the protein).
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (stop codons and termination of translation).
[^ensembl]: [[Ensembl]], Variant Effect Predictor, "Calculated variant consequences" (`stop_gained`, `stop_lost`, `start_lost` and impact categories).
[^richards]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], criterion PVS1 (null variants) and its cautions.
[^nagy]: [[Nagy 1998 - A Rule for Termination-Codon Position Within Intron-Containing Genes]], the 50-55 nucleotide rule.
[^hgvs]: [[den Dunnen 2016 - HGVS Recommendations for the Description of Sequence Variants]], protein descriptions (`Ter` and `*`).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), on nonsense-mediated mRNA decay and its link with splicing.
