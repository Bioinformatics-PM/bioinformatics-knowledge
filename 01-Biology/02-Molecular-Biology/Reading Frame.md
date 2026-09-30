---
aliases:
  - Frame
  - Six-Frame Translation
  - Translation Frame
  - Cadre de lecture
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Codon]]"
  - "[[DNA]]"
  - "[[Base Pairing]]"
related:
  - "[[Genetic Code]]"
  - "[[Open Reading Frame]]"
  - "[[Frameshift Mutation]]"
  - "[[Reverse Complement]]"
  - "[[Translation]]"
  - "[[Gene Finding]]"
  - "[[Modular Arithmetic]]"
projects:
  - "[[02-sequence-translation]]"
sources:
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Crick 1961 - General Nature of the Genetic Code for Proteins]]"
---

# Reading Frame

> [!abstract]
> A reading frame is one way of cutting a sequence into consecutive triplets; each strand can be cut in three ways, so a stretch of double-stranded DNA has six possible readings, and only the start codon tells which one a gene uses.

## Definition

A **reading frame** is a division of a nucleotide sequence into consecutive, non-overlapping triplets ([[Codon|codons]]), fixed by the position of the first codon. A strand can be read in three frames, starting at its first, second or third nucleotide. A double-stranded sequence has **six**: three on each strand, each read 5' → 3'. In a gene, the start codon selects the frame that is translated.[^alberts][^os15][^crick61]

## Why it matters

- **Unknown frame, six candidates.** In a new genome, a contig or a sequencing read, nothing says where codons start or which strand codes. Translating all six frames is the first step of ORF finding, of gene finding and of comparing DNA with protein databases ([[Open Reading Frame]], [[Gene Finding]], [[BLAST]]).
- **Conventions.** Tools number the minus-strand frames in different ways; converting between them is a classic source of off-by-one and strand errors ([[Genetic Code#Computational representation]]).
- **Frameshifts.** An insertion or deletion whose length is not a multiple of 3 moves every downstream codon into another frame, whether it is a mutation in a genome or an indel error in a read ([[Frameshift Mutation]]).
- **Spliced genes.** When an exon boundary falls inside a codon, the next exon starts in the middle of a codon; annotations record this per CDS segment as a phase ([[Gene#Advanced (L3)]]).

## Core (L1)

**Three frames per strand.** Starting the triplets at the first, second or third nucleotide gives three different codon lists; starting at the fourth gives back the first frame minus one codon. With the invented sequence `5'-GATGCCTGATTCAT-3'`:

```text
frame +1 (offset 0)   GAT GCC TGA TTC        D A * F
frame +2 (offset 1)   ATG CCT GAT TCA        M P D S
frame +3 (offset 2)   TGC CTG ATT CAT        C L I H
```

**Three more on the other strand.** The partner strand is also read 5' → 3', so its frames are the frames of the reverse complement, `5'-ATGAATCAGGCATC-3'` ([[Base Pairing]], [[Reverse Complement]]):

```text
frame -1 (offset 0)   ATG AAT CAG GCA        M N Q A
frame -2 (offset 1)   TGA ATC AGG CAT        * I R H
frame -3 (offset 2)   GAA TCA GGC ATC        E S G I
```

![[six-reading-frames.svg]]

**Enumerating the six frames**, the procedure for any double-stranded sequence $s$ of length $n$:

1. Write $s$ 5' → 3' and compute its reverse complement $\mathrm{rc}(s)$.
2. For each offset $f = 0, 1, 2$, cut $s$ into triplets starting at position $f$ (0-based) and drop an incomplete last triplet: frames +1, +2, +3.
3. Do the same on $\mathrm{rc}(s)$: frames −1, −2, −3.
4. Translate each codon with the [[Genetic Code]] if needed.

**Which frame is real?** In the cell, the ribosome starts at the start codon, and that choice fixes the frame for the rest of the coding sequence ([[Translation]]).[^alberts] In the example, frame +2 is the only plus frame that begins with ATG, and frame −1 the only minus frame; each then reads three sense codons and runs off the end without a stop: two short candidates, neither of them evidence of a gene ([[Open Reading Frame]]).

## Deeper (L2)

**Minus frames on plus coordinates.** A codon at 0-based offset $j$ of $\mathrm{rc}(s)$ covers positions $[n - j - 3,\ n - j)$ of $s$. Which plus frame a minus frame lines up with therefore depends on $n \bmod 3$:

| $n \bmod 3$ | −1 shares codon boundaries with | −2 with | −3 with |
|---:|---|---|---|
| 0 | +1 | +3 | +2 |
| 1 | +2 | +1 | +3 |
| 2 | +3 | +2 | +1 |

(Derived in the Mathematical representation.) This is why two tools can disagree on "frame −1" of the same sequence: one counts from the 5' end of each strand, as here, the other assigns every codon a frame from its position on the plus strand. Always state the convention.

**Frameshifts.** Deleting or inserting $d$ nucleotides shifts every downstream codon by $d \bmod 3$ frames. Crick, Brenner and colleagues used exactly this to show that the code is read in triplets from a fixed start: one or two insertions garbled a phage gene, three restored it ([[Genetic Code#Exercises]]).[^crick61] A shifted frame usually meets a stop codon soon, so frameshifts typically produce truncated proteins ([[Frameshift Mutation]]).

**Programmed frameshifting.** The frame is not always fixed for the whole mRNA. Some mRNAs carry signals that make a fraction of ribosomes slip back one nucleotide at a specific site and continue in the −1 frame, producing a longer fusion protein; retroviruses use this translational frameshifting to make their reverse transcriptase as part of such a fusion.[^alberts-reg] Exercise 6 simulates it.

## Advanced (L3)

- **Finding the frame of a coding read.** In a true coding frame there is no stop codon until the end of the CDS, while each codon of a random-looking frame is a stop with probability about $3/64$ ([[Genetic Code#Mathematical representation]]). Over 50 codons, a random frame is stop-free with probability $(61/64)^{50} \approx 0.09$, so a long read usually has a single open frame; a short one often has several (Exercise 5).
- **Cost of six frames.** Every codon start position belongs to exactly one frame, so the six frames hold $2(n - 2)$ codons in total: a six-frame translation of a genome of $n$ bp has about $2n$ amino acids, six times the $n/3$ of a single frame. Translated searches pay this factor compared with searching one frame or annotated proteins.
- **Frames across exons.** In a spliced gene the frame is continuous in the mRNA, not in the genome. If an exon's length is not a multiple of 3, the frame at the start of the next exon differs from the frame at the start of the previous one, and skipping such an exon shifts the frame of everything downstream ([[Transcription#Exercises]], [[Alternative Splicing]]).
- **Frame as a label, not a property.** The same nucleotides can be read in different frames by different ribosomes (frameshifting, alternative starts), so the frame belongs to a reading of the sequence, the translation of one start codon, and not to the sequence itself.[^alberts-reg]

## Mathematical representation

Let $s \in \Sigma^n$ (0-based positions) and $f \in \{0, 1, 2\}$.

- **Frame.** The codons of frame $f$ are $c_k = s[f + 3k,\ f + 3k + 3)$ for $k = 0, \dots, m_f - 1$, with $m_f = \lfloor (n - f)/3 \rfloor$ complete codons. The six frames are the frames $f$ of $s$ (+1 to +3) and of $\mathrm{rc}(s)$ (−1 to −3).
- **Residue classes.** A codon start $i$ belongs to frame $i \bmod 3$: the three frames partition the $n - 2$ possible start positions $\{0, \dots, n-3\}$ into residue classes modulo 3 ([[Modular Arithmetic]]). Hence $m_0 + m_1 + m_2 = n - 2$ for $n \ge 2$, and the six frames hold $2(n - 2)$ codons.
- **Minus frames on plus coordinates.** Codon $k$ of frame $f$ of $\mathrm{rc}(s)$ starts at offset $j = f + 3k$ and covers plus positions $[n - j - 3,\ n - j)$. Its plus-strand start is $n - f - 3(k+1) \equiv n - f \pmod 3$, so minus frame $f$ has the same codon boundaries as plus frame
$$g = (n - f) \bmod 3,$$
which gives the table of the Deeper section.
- **Frameshift.** An indel of length $d$ (positive for insertions) at position $x$ moves the codon starts downstream of $x$ from residue class $r$ to $(r + d) \bmod 3$: the frame is preserved iff $d \equiv 0 \pmod 3$.

## Computational representation

Store codons with plus-strand coordinates, whatever their strand, so that all six frames can be drawn and compared on one axis:

```python
BASES = "TCAG"
CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
                "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def frame_codons(dna: str) -> dict[str, list[tuple[int, int, str]]]:
    """Codons of the six frames as (start, end, codon): + strand coordinates, 0-based half-open.
    Frame +f and -f start f-1 bases from the 5' end of their own strand."""
    n, rc = len(dna), dna.translate(COMPLEMENT)[::-1]
    frames = {}
    for f in range(3):
        frames[f"+{f + 1}"] = [(i, i + 3, dna[i:i + 3]) for i in range(f, n - 2, 3)]
        frames[f"-{f + 1}"] = [(n - j - 3, n - j, rc[j:j + 3]) for j in range(f, n - 2, 3)]
    return frames


def six_frame_view(dna: str) -> str:
    """Amino acids written under the middle base of their codon, all six frames on + coordinates."""
    rows = {}
    for name, codons in frame_codons(dna).items():
        row = [" "] * len(dna)
        for start, _, codon in codons:
            row[start + 1] = CODE[codon]
        rows[name] = "".join(row)
    top = [f"{k}  {rows[k]}" for k in ("+3", "+2", "+1")]
    bottom = [f"{k}  {rows[k]}" for k in ("-1", "-2", "-3")]
    strands = [f"5'  {dna}  3'", f"3'  {dna.translate(COMPLEMENT)}  5'"]
    return "\n".join(top + strands + bottom)


seq = "GATGCCTGATTCAT"                        # invented, n = 14
print(six_frame_view(seq))
for name in ("+1", "-3", "+3", "-1"):
    print(name, [(s, e) for s, e, _ in frame_codons(seq)[name]])
```

```text
+3     C  L  I  H 
+2    M  P  D  S  
+1   D  A  *  F   
5'  GATGCCTGATTCAT  3'
3'  CTACGGACTAAGTA  5'
-1     A  Q  N  M 
-2    H  R  I  *  
-3   I  G  S  E   
+1 [(0, 3), (3, 6), (6, 9), (9, 12)]
-3 [(9, 12), (6, 9), (3, 6), (0, 3)]
+3 [(2, 5), (5, 8), (8, 11), (11, 14)]
-1 [(11, 14), (8, 11), (5, 8), (2, 5)]
```

The minus rows are read right to left: row −1 spells `A Q N M` on the page but the protein is Met-Asn-Gln-Ala. The coordinate lists confirm the table for $n \bmod 3 = 2$: −3 has the codon boundaries of +1, and −1 those of +3. This aligned view is the display planned for [[02-sequence-translation]].

## Worked example

> [!example] Six frames of `5'-GATGCCTGATTCAT-3'` by hand (invented, $n = 14$)
> 1. **Plus frames.** Offsets 0, 1, 2 give 4 complete codons each ($\lfloor 14/3 \rfloor = \lfloor 13/3 \rfloor = \lfloor 12/3 \rfloor = 4$): +1 `GAT GCC TGA TTC`, +2 `ATG CCT GAT TCA`, +3 `TGC CTG ATT CAT`; each frame leaves 2 bases unused, at its start, its end or both.
> 2. **Reverse complement.** Complement `CTACGGACTAAGTA`, reversed `ATGAATCAGGCATC`.
> 3. **Minus frames.** −1 `ATG AAT CAG GCA`, −2 `TGA ATC AGG CAT`, −3 `GAA TCA GGC ATC`.
> 4. **Count.** $6 \times 4 = 24$ codons $= 2(n - 2)$.
> 5. **Map back.** The ATG of frame −1 is the last three bases of the plus strand read backwards: `CAT` at plus positions 11 to 13 (0-based), $[n - 0 - 3, n - 0) = [11, 14)$. Its frame on the plus strand is $(14 - 0) \bmod 3 = 2$, the frame of +3.
> 6. **Candidates.** Frame +2 reads Met-Pro-Asp-Ser without a stop; frame −1 reads Met-Asn-Gln-Ala. Both run off the end of the sequence: without a stop codon they are incomplete ORFs.

## Common misconceptions

> [!warning] "The minus frames are the complement read left to right"
> The complement strand runs 3' → 5' from left to right, so reading it left to right reads it backwards. Minus frames are the frames of the **reverse** complement, read from its 5' end.

> [!warning] "Frame −1 lines up with frame +1"
> Only when $n$ is a multiple of 3. In general minus frame $f$ lines up with plus frame $(n - f) \bmod 3$: trimming one base from the 3' end of a sequence changes which plus and minus frames match.

> [!warning] "A DNA sequence has three reading frames"
> A single strand has three. Double-stranded DNA has six, since either strand may code. Three frames are enough only when the strand is known, as for an mRNA.

> [!warning] "The reading frame is a property of the sequence"
> The frame is set by where reading starts. Different start codons in one sequence, or a ribosome that slips, read the same nucleotides in different frames.[^alberts-reg]

## Exercises

> [!question] Exercise 1 (L1)
> Write the codons and translations of the three plus frames of `5'-ATGCGTACGTTAG-3'` (13 nt).

> [!success]- Solution
> +1: ATG CGT ACG TTA → M R T L (one base left over). +2: TGC GTA CGT TAG → C V R * (TAG is a stop). +3: GCG TAC GTT → A Y V (one base left over). Only +1 starts with ATG, and it has no stop within the sequence.

> [!question] Exercise 2 (L1)
> How many complete codons do the six frames hold for $n = 100$, 101 and 102? Check against $2(n - 2)$.

> [!success]- Solution
> $n = 100$: offsets 0, 1, 2 give 33, 33, 32 codons, $98 \times 2 = 196$. $n = 101$: 33, 33, 33, total 198. $n = 102$: 34, 33, 33, total 200. In each case the six frames hold $2(n - 2)$ codons.

> [!question] Exercise 3 (L2)
> For a sequence of length 20, which plus frame shares its codon boundaries with each minus frame? Same question for length 21.

> [!success]- Solution
> Use $g = (n - f) \bmod 3$ with offset $f$ = frame number − 1. $n = 20$: −1 ↔ $20 \bmod 3 = 2$ (+3), −2 ↔ $19 \bmod 3 = 1$ (+2), −3 ↔ $18 \bmod 3 = 0$ (+1). $n = 21$: −1 ↔ +1, −2 ↔ +3, −3 ↔ +2. One extra base changed the pairing.

> [!question] Exercise 4 (L2)
> In a 300-codon CDS, 2 nucleotides are deleted in codon 10. Which codons change? Under the random-codon model, about how many codons are read in the new frame before a stop?

> [!success]- Solution
> Codon 10 is altered and all downstream codons are read in a frame shifted by $-2 \equiv 1 \pmod 3$. If the new frame behaves like random sequence, the number of codons read until a stop (included) is geometric with mean $64/3 \approx 21$ ([[Genetic Code#Mathematical representation]]), so the protein is expected to end some twenty codons after the deletion, with a wrong C-terminal tail instead of the remaining 290 or so correct residues.

> [!question] Exercise 5 (L3, Python)
> Simulate a coding sequence of 60 random sense codons, take a 150-nt read from the other strand starting at its second base, and count the stop codons in each of the six frames of the read. Repeat with a 30-nt read. Which frame is the coding one, and when can you tell?

> [!success]- Solution
> ```python
> import random
>
> BASES = "TCAG"
> CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
>                 "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
> COMPLEMENT = str.maketrans("ACGT", "TGCA")
>
>
> def stops_per_frame(read: str) -> dict[str, int]:
>     """Number of stop codons in each of the six frames of a read."""
>     rc = read.translate(COMPLEMENT)[::-1]
>     return {f"{sign}{f + 1}": sum(CODE[s[i:i + 3]] == "*" for i in range(f, len(s) - 2, 3))
>             for sign, s in (("+", read), ("-", rc)) for f in range(3)}
>
>
> random.seed(7)                                             # simulated data, not a real gene
> sense = [c for c, aa in CODE.items() if aa != "*"]
> cds = "".join(random.choice(sense) for _ in range(60))     # 180 nt, no internal stop
> read = cds[1:151].translate(COMPLEMENT)[::-1]              # 150-nt read from the other strand
> print(stops_per_frame(read))
> short = cds[1:31].translate(COMPLEMENT)[::-1]              # 30-nt read
> print(stops_per_frame(short))
> ```
> Output: `{'+1': 1, '+2': 4, '+3': 2, '-1': 2, '-2': 1, '-3': 0}`, then `{'+1': 0, '+2': 1, '+3': 0, '-1': 0, '-2': 1, '-3': 0}`. The read comes from the other strand, so the coding frame is a minus frame; the read starts one base into a codon, so the codons begin at offset 2 of $\mathrm{rc}(\text{read})$: frame −3, the only stop-free frame of the long read. The 30-nt read leaves four stop-free candidates: ten codons are too few, as $(61/64)^{10} \approx 0.62$ predicts.

> [!question] Exercise 6 (L3, Python)
> Simulate programmed −1 frameshifting: write `translate(seq, start, slip_after, shift)` in which the ribosome moves back one nucleotide after reading the codon that ends at `slip_after`. Apply it to the invented `ATGGCTTTTTTATAGATCCCTCATCCTCATAA` with and without a slip after the fourth codon.

> [!success]- Solution
> ```python
> BASES = "TCAG"
> CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
>                 "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
>
>
> def translate(seq: str, start: int = 0, slip_after: int | None = None, shift: int = -1) -> str:
>     """Translate from start to the first stop. If slip_after is given, the ribosome moves by
>     shift nucleotides once it has read the codon ending at that position (0-based, exclusive)."""
>     protein, i = "", start
>     while i + 3 <= len(seq):
>         aa = CODE[seq[i:i + 3]]
>         if aa == "*":
>             return protein + "*"
>         protein += aa
>         i += 3
>         if i == slip_after:
>             i += shift
>     return protein
>
>
> mrna = "ATGGCTTTTTTATAGATCCCTCATCCTCATAA"      # invented, written with T as in a cDNA file
> print(translate(mrna))
> print(translate(mrna, slip_after=12))
> ```
> Output: `MAFL*` and `MAFLIDPSSS*`. Without slipping, the stop TAG right after the fourth codon ends translation. A ribosome that steps back one base re-reads the last A and continues in the −1 frame (`ATA GAT CCC TCA TCC TCA TAA`), making a fusion protein that shares its first four residues with the short one. In a real mRNA only a fraction of ribosomes slip, so both proteins are made, in a fixed ratio.

## Mastery checklist

- [ ] 1 Recognized: I can define a reading frame and say why a double-stranded sequence has six.
- [ ] 2 Understood: I can explain how the start codon fixes the frame, why minus frames come from the reverse complement, and what a frameshift does.
- [ ] 3 Practiced: I can enumerate and translate the six frames by hand and in code, with plus-strand coordinates for every codon.
- [ ] 4 Applied: in [[02-sequence-translation]], my six-frame view matches a reference tool on real sequences once the frame-numbering convention is aligned.
- [ ] 5 Explained: I can teach frame numbering conventions, the $n \bmod 3$ correspondence, frames across exons, and programmed frameshifting.

## References

[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of reading frames and of translation initiation setting the frame.
[^alberts-reg]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of posttranscriptional controls, including translational frameshifting in retroviruses.
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (the genetic code, protein synthesis).
[^crick61]: [[Crick 1961 - General Nature of the Genetic Code for Proteins]], Crick FHC, Barnett L, Brenner S, Watts-Tobin RJ, *Nature* 192:1227-1232.
