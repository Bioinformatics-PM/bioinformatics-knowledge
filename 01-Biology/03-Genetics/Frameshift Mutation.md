---
aliases:
  - Frameshift
  - Frameshift Variant
  - frameshift_variant
  - Frame-Shift Mutation
  - Mutation décalante
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Indel]]"
  - "[[Reading Frame]]"
  - "[[Codon]]"
  - "[[Genetic Code]]"
related:
  - "[[Mutation]]"
  - "[[Nonsense Mutation]]"
  - "[[Missense Mutation]]"
  - "[[Nonsense-Mediated Decay]]"
  - "[[Open Reading Frame]]"
  - "[[Translation]]"
  - "[[Variant Annotation]]"
  - "[[Variant Nomenclature]]"
  - "[[Variant Classification]]"
projects:
  - "[[06-mutation-lab]]"
  - "[[03-genome-diff]]"
sources:
  - "[[Crick 1961 - General Nature of the Genetic Code for Proteins]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Ensembl]]"
  - "[[den Dunnen 2016 - HGVS Recommendations for the Description of Sequence Variants]]"
  - "[[Nagy 1998 - A Rule for Termination-Codon Position Within Intron-Containing Genes]]"
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Frameshift Mutation

> [!abstract]
> A frameshift mutation inserts or deletes a number of bases that is not a multiple of three in a coding sequence, so the ribosome reads every downstream codon out of register: the protein continues with unrelated amino acids and usually stops early.

## Definition

A **frameshift mutation** is an [[Indel]] in a coding sequence whose net length change is not a multiple of 3. Codons are read three by three from the start codon, so from the site of the indel on, the downstream bases are grouped into different triplets: the [[Reading Frame|reading frame]] is shifted.[^griffiths][^crick61] Ensembl's Variant Effect Predictor defines `frameshift_variant` as a variant that disrupts the translational reading frame because the number of nucleotides inserted or deleted is not a multiple of three, with a HIGH impact.[^ensembl]

## Why it matters

- **One of the most drastic small variants.** HIGH impact in annotation;[^ensembl] frameshifts are "null" variants in clinical guidelines, very strong evidence of pathogenicity (PVS1) in a gene where loss of function causes disease.[^richards]
- **The historical proof of the triplet code.** Frameshifts induced with proflavin showed that the code is read in groups of three from a fixed start.[^crick61]
- **Frame arithmetic everywhere.** Translating assemblies, predicting genes and checking gene models all rely on the same modulo-3 reasoning ([[Open Reading Frame]], [[Genetic Code#Reading frames]]).
- **Lab.** [[06-mutation-lab]] shows the shifted codons and the new stop; [[03-genome-diff]] classifies each coding indel as frameshift or in-frame. Both report the **molecular consequence only**, never a clinical prediction.

## Core (L1)

### Arithmetic modulo 3

Let $\Delta$ be the net length change (inserted minus deleted bases). A base that sat at position $p$ downstream of the indel moves to $p + \Delta$, so its place in the codon changes from $p \bmod 3$ to $(p + \Delta) \bmod 3$. The phase shift is

$$\varphi = \Delta \bmod 3 \in \{0, 1, 2\}.$$

| $\Delta$ | $\varphi$ | Downstream reading |
|---|---:|---|
| −3, +3, −6, ... | 0 | in frame: codons regrouped only at the site |
| +1, −2, +4, −5 | 1 | shifted: every downstream codon changes |
| −1, +2, −4, +5 | 2 | shifted the other way: every downstream codon changes |

![[frameshift-reading-frame.svg]]

In the figure, deleting one base of codon 2 turns `GCT GAA CGT CTG` into `CTG AAC GTC TGA`: Leu-Asn-Val and a stop at codon 5, where the reference continued for ten codons. The downstream bases are all still there; they are simply read in the wrong groups of three.

### The Crick-Brenner experiment

Crick, Brenner and colleagues used proflavin to add or remove single bases in a gene of bacteriophage T4. One addition or one deletion destroyed the gene's function; an addition combined with a nearby deletion, or three additions together, restored it.[^crick61] The only simple explanation is a code read in triplets from a fixed starting point, the same arithmetic as the table above: the effects add up modulo 3. The sentence version is Exercise 3 of [[Genetic Code]].

### What the protein becomes

Upstream of the site, nothing changes. From the site on, the amino acids are those of another frame, unrelated to the protein, until the first stop codon of that frame: a frameshift usually creates a premature stop a few codons downstream.

## Deeper (L2)

### How far is the new stop?

In a sequence with independent, equiprobable bases, each codon of the new frame is a stop with probability $q = 3/64$, so the number of codons read until the first stop (included) is geometric with mean $1/q = 64/3 \approx 21.3$ ([[Genetic Code#Mathematical representation]]). Base composition changes $q$: at 70 % GC it is about 0.019 and the mean about 52 codons (Exercise 5). A frameshift early in a gene therefore typically adds a short tail of wrong residues and ends with a premature stop, which puts it under the same rule as a [[Nonsense Mutation]]: if that stop lies more than 50-55 nt upstream of the last exon-exon junction, the mRNA is expected to be degraded by [[Nonsense-Mediated Decay]].[^nagy]

### Notation

HGVS writes a frameshift at the protein level as the first changed amino acid, its position, the new amino acid, `fs`, then `Ter` and the position of the new stop in the new frame, as in `p.Arg97ProfsTer23`.[^hgvs] In the code below, the stop position is counted with the first changed residue as 1.

### +1 and −2 give the same frame

$+1 \equiv -2 \pmod 3$: an insertion of one base and a deletion of two bases at the same place read the downstream sequence in the same shifted frame. Only the bases at the site differ (compare `MAESSDR*` and `MAESDR*` in the output below). This is why the direction of a frameshift is described by $\varphi$, not by the sign of $\Delta$.

## Advanced (L3)

### Compensation and suppression

Two indels whose net changes add up to a multiple of 3 restore the frame after the second one: only the codons between them are read in the shifted frame (third row of the figure).[^crick61] The result is a protein with a local stretch of wrong residues, which may or may not work, and it is a full-length protein only if the shifted stretch contains no stop codon. In the Crick-Brenner experiments, such second-site changes acted as suppressors of the first mutation.[^crick61]

### Interpretation

PVS1 applies to frameshifts as to nonsense variants: in a gene where loss of function is a known disease mechanism, with caution near the 3' end of the gene, where the shifted tail is short and decay may not occur, and when several transcripts exist.[^richards] A frameshift that removes the normal stop can also **extend** the protein if the new frame has no stop before the old one; annotation reports the frameshift in both cases.

### Not every frame change is a mutation

Some genes are translated with a deliberate ribosomal frameshift: retroviruses, for instance, make part of their proteins by a programmed frameshift of the ribosome at a specific site, producing a fusion protein.[^alberts] Apparent frameshifts in a new assembly can also be indel errors in homopolymers ([[Indel#Why indels are harder to call than substitutions]]). A gene model with a frame change is therefore a question, not an answer.

## Mathematical representation

- Coding sequence $s$ with the start codon at position 0; codon $k$ (0-based) is $s_{3k}\, s_{3k+1}\, s_{3k+2}$, and position $p$ has phase $p \bmod 3$.
- An indel with net change $\Delta$ at position $i$ moves every base $p > i$ to $p + \Delta$. Its phase becomes $(p + \Delta) \bmod 3$, which equals $p \bmod 3$ for all $p$ if and only if $\varphi = \Delta \bmod 3 = 0$.
- **Several indels** with changes $\Delta_1, \dots, \Delta_m$ at increasing positions: downstream of event $r$ the phase shift is $\left(\sum_{t \le r} \Delta_t\right) \bmod 3$; the frame is restored after event $r$ if and only if $\sum_{t \le r} \Delta_t \equiv 0 \pmod 3$.
- **Length of the shifted tail** under the i.i.d. model: $T \sim \text{Geometric}(q)$ codons, $E[T] = 1/q$, $P(T > k) = (1 - q)^k$. With $q = 3/64$, $P(T > 50) = (61/64)^{50} \approx 0.091$.

## Computational representation

```python
BASES = "TCAG"
CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
                "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
THREE = dict(zip("ACDEFGHIKLMNPQRSTVWY*",
                 "Ala Cys Asp Glu Phe Gly His Ile Lys Leu Met Asn Pro Gln Arg Ser Thr Val Trp Tyr Ter".split()))

def translate_to_stop(seq: str) -> str:
    """Translate from the first base up to and including the first stop ('*')."""
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        protein += CODE[seq[i:i + 3]]
        if protein[-1] == "*":
            break
    return protein

def apply_edits(seq: str, edits: list[tuple[int, str, str]]) -> str:
    """Apply (0-based pos, ref, alt) edits, right to left so positions stay valid."""
    for pos, ref, alt in sorted(edits, reverse=True):
        assert seq[pos:pos + len(ref)] == ref
        seq = seq[:pos] + alt + seq[pos + len(ref):]
    return seq

def protein_change(mrna: str, edits: list[tuple[int, str, str]]) -> str:
    """HGVS-style protein consequence of indels in an mRNA that starts at the ATG."""
    before, after = translate_to_stop(mrna), translate_to_stop(apply_edits(mrna, edits))
    shift = sum(len(alt) - len(ref) for _, ref, alt in edits) % 3
    k = next((i for i, (a, b) in enumerate(zip(before, after)) if a != b), None)
    if k is None:
        return "no change"
    ref_aa, new_aa = THREE[before[k]], THREE[after[k]]
    if shift == 0:
        return f"frame kept, first change at {ref_aa}{k + 1}: {before} -> {after}"
    if not after.endswith("*"):
        return f"p.{ref_aa}{k + 1}{new_aa}fsTer?  (no stop before the mRNA ends)"
    ter = len(after) - k            # new stop, counting the first changed residue as 1
    return f"p.{ref_aa}{k + 1}{new_aa}fsTer{ter}: {before} -> {after}"

mrna = "ATGGCTGAACGTCTGACCGATAAAGGCTAA" + "GCATTAGC"   # invented CDS + 3' UTR
print(translate_to_stop(mrna))
print(protein_change(mrna, [(3, "G", "")]))                 # -1 in codon 2
print(protein_change(mrna, [(9, "", "T")]))                 # +1 before codon 4
print(protein_change(mrna, [(9, "CG", "")]))                # -2 at the same place
print(protein_change(mrna, [(3, "G", ""), (12, "", "T")]))  # -1 then +1: frame restored
print(protein_change(mrna, [(15, "ACC", "")]))              # -3: in-frame
```

Output:

```text
MAERLTDKG*
p.Ala2LeufsTer4: MAERLTDKG* -> MLNV*
p.Arg4SerfsTer5: MAERLTDKG* -> MAESSDR*
p.Arg4SerfsTer4: MAERLTDKG* -> MAESDR*
frame kept, first change at Ala2: MAERLTDKG* -> MLNVLTDKG*
frame kept, first change at Thr6: MAERLTDKG* -> MAERLDKG*
```

The mRNA includes a 3' UTR because a shifted frame can read past the original stop. Real tools work from genomic VCF records and transcript models, and must also handle indels that touch splice sites or the stop codon itself.

## Worked example

> [!example] Frame arithmetic on one toy gene (invented)
> CDS `ATG GCT GAA CGT CTG ACC GAT AAA GGC TAA` → Met-Ala-Glu-Arg-Leu-Thr-Asp-Lys-Gly-stop (9 residues).
>
> 1. **Delete the G at position 3** (0-based, first base of codon 2). $\Delta = -1$, $\varphi = 2$. New codons: `ATG CTG AAC GTC TGA` → Met-Leu-Asn-Val-stop. `p.Ala2LeufsTer4`: 3 wrong residues, then the stop, 4 residues instead of 9.
> 2. **Insert T before codon 4** (position 9). $\Delta = +1$, $\varphi = 1$: `ATG GCT GAA TCG TCT GAC CGA TAA` → Met-Ala-Glu-Ser-Ser-Asp-Arg-stop, `p.Arg4SerfsTer5`.
> 3. **Delete CG at position 9** instead. $\Delta = -2$, $\varphi = 1$ again: Met-Ala-Glu-Ser-Asp-Arg-stop. Same downstream frame as the +1 insertion (…Asp-Arg-stop), different residues at the site.
> 4. **Combine −1 at position 3 with +1 at position 12.** $\Delta_1 + \Delta_2 = 0$: codons 2 to 4 read Leu-Asn-Val, then the frame is restored and the protein ends as the reference (…Leu-Thr-Asp-Lys-Gly-stop).
> 5. **Delete ACC (codon 6).** $\Delta = -3$: in-frame, one residue (Thr) lost, the rest unchanged.

## Common misconceptions

> [!warning] "A frameshift changes the amino acid at the site"
> It changes the grouping of every downstream base into codons, so every downstream residue belongs to another frame until the new stop.

> [!warning] "A 1-base insertion and a 2-base deletion are opposite frameshifts"
> $+1 \equiv -2 \pmod 3$: they put the downstream sequence in the same shifted frame. Only the local bases differ.

> [!warning] "A frameshift always shortens the protein"
> Usually, because stops are frequent in a random frame. But near the 3' end, or if the new frame has no stop before the old one, the protein can be extended into the 3' UTR.

> [!warning] "A frame change in a gene model proves a mutation"
> It may be a sequencing or assembly indel error, often in a homopolymer, or a programmed ribosomal frameshift that the gene uses on purpose.[^alberts]

## Exercises

> [!question] Exercise 1 (L1)
> In a coding sequence, which net changes cause a frameshift, and with which phase shift $\varphi$: −1, +3, −4, +2, −6, +5?

> [!success]- Solution
> −1: $\varphi = 2$; −4: $\varphi = 2$; +2: $\varphi = 2$; +5: $\varphi = 2$. All four are frameshifts, and all in the same shifted frame. +3 and −6: $\varphi = 0$, in-frame.

> [!question] Exercise 2 (L1)
> In the toy CDS of the worked example, delete the A at position 7 (0-based). Translate the new sequence by hand.

> [!success]- Solution
> `ATGGCTG` + `ACGTCTGACC...` gives `ATG GCT GAC GTC TGA`: Met-Ala-Asp-Val-stop, `p.Glu3AspfsTer3`. Check with `protein_change(mrna, [(7, "A", "")])`.

> [!question] Exercise 3 (L2)
> Explain with the phase formula why the +1 insertion and the −2 deletion of the worked example end with the same residues (…Asp-Arg-stop).

> [!success]- Solution
> A downstream base at position $p$ lands at phase $(p + 1) \bmod 3$ after the insertion and $(p - 2) \bmod 3$ after the deletion, and these are equal for every $p$ because $3$ divides $(p+1) - (p-2)$. The downstream bases are grouped into the same triplets, so the same codons (`GAC CGA TAA`) and residues follow. Only the codons that contain the site differ.

> [!question] Exercise 4 (L2, Python)
> Using `protein_change` and `mrna` from the code above, give the HGVS-style description of an insertion of `T` at position 5 and of a deletion of `G` at position 6. Which one is a frameshift that immediately creates a stop?

> [!success]- Solution
> ```python
> print(protein_change(mrna, [(5, "", "T")]))
> print(protein_change(mrna, [(6, "G", "")]))
> # p.Glu3TerfsTer1: MAERLTDKG* -> MA*
> # p.Glu3AsnfsTer3: MAERLTDKG* -> MANV*
> ```
>
> The insertion turns codon 3 into `TGA`: the first changed "residue" is already a stop, and the protein ends after Met-Ala as with a nonsense change. The output `fsTer1` is correct arithmetic but says little: a nomenclature needs a special rule for this case (check the current HGVS recommendations before writing it). The deletion gives two wrong residues (Asn-Val), then the stop, at position 3 counting Asn as 1.

> [!question] Exercise 5 (L3, Python)
> Simulate random sequences (50 % and 70 % GC) and measure the mean number of codons read until the first stop in frame 0. Compare with $1/q$ and discuss what it implies for frameshift tails and NMD.

> [!success]- Solution
> ```python
> import random
> from statistics import mean
>
> def codons_to_stop(seq: str) -> int | None:
>     """Number of codons read in frame 0 up to and including the first stop."""
>     for k, i in enumerate(range(0, len(seq) - 2, 3), start=1):
>         if CODE[seq[i:i + 3]] == "*":
>             return k
>     return None
>
> def random_seq(n: int, gc: float, rng: random.Random) -> str:
>     weights = [(1 - gc) / 2, gc / 2, (1 - gc) / 2, gc / 2]           # T, C, A, G
>     return "".join(rng.choices(BASES, weights, k=n))
>
> rng = random.Random(1)
> for gc in (0.5, 0.7):
>     runs = [codons_to_stop(random_seq(3000, gc, rng)) for _ in range(20000)]
>     print(gc, round(mean(runs), 1))
> print(round(64 / 3, 1))
> # 0.5 21.3
> # 0.7 52.1
> # 21.3
> ```
>
> At 50 % GC the tail averages about 21 codons ($64/3$); at 70 % GC, stops (AT-rich) are rarer ($q \approx 0.019$, $1/q \approx 52$). Real sequences are not random, but the order of magnitude explains why most frameshifts end at a premature stop within a few dozen codons, often upstream of the last exon-exon junction and so predicted to trigger NMD.[^nagy]

> [!question] Exercise 6 (L3)
> A gene carries a 1-base deletion in codon 3 and a 1-base insertion in codon 8. (a) Which codons are read in a shifted frame? (b) Under the random model, what is the probability that the 5 shifted codons between the two events contain a stop? (c) What would the Crick-Brenner logic predict about function?

> [!success]- Solution
> (a) From the deletion to the insertion: codons 3 to 8 are regrouped (the net change is 0 after the insertion, so codon 9 onward is normal). (b) For 5 shifted codons, $1 - (61/64)^5 \approx 0.21$: in about one case in five the double mutant still ends early. (c) If no stop intervenes, the protein has the right length with a few wrong residues; function may be restored if that stretch tolerates changes, which is what the suppressor experiments observed.[^crick61]

## Mastery checklist

- [ ] 1 Recognized: I can define a frameshift and tell it apart from an in-frame indel.
- [ ] 2 Understood: I can explain with $\Delta \bmod 3$ why every downstream codon changes, why +1 and −2 are equivalent, and how two indels can restore the frame.
- [ ] 3 Practiced: I can compute the new protein and an HGVS-style `fs` description in Python, and the distribution of tail lengths.
- [ ] 4 Applied: in [[06-mutation-lab]] and [[03-genome-diff]], I annotate the frameshifts of a real gene with the new stop and an NMD prediction.
- [ ] 5 Explained: I can teach the Crick-Brenner logic, when a frameshift escapes decay or extends the protein, and why a frame change in a gene model is not always a mutation.

## References

[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of gene mutation (frameshift mutations and acridine mutagens).
[^crick61]: [[Crick 1961 - General Nature of the Genetic Code for Proteins]], Crick FHC, Barnett L, Brenner S, Watts-Tobin RJ, *Nature* 192:1227-1232.
[^ensembl]: [[Ensembl]], Variant Effect Predictor, "Calculated variant consequences" (`frameshift_variant`).
[^richards]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], criterion PVS1 (null variants) and its cautions.
[^nagy]: [[Nagy 1998 - A Rule for Termination-Codon Position Within Intron-Containing Genes]], the 50-55 nucleotide rule.
[^hgvs]: [[den Dunnen 2016 - HGVS Recommendations for the Description of Sequence Variants]], protein-level frameshift descriptions.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), on translational frameshifting in retroviruses.
