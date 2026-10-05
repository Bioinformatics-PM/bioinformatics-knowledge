---
aliases:
  - mRNA
  - Messenger RNA Structure
  - Transcript
  - ARN messager
  - ARNm
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[RNA]]"
  - "[[Transcription]]"
  - "[[Central Dogma]]"
related:
  - "[[Codon]]"
  - "[[Open Reading Frame]]"
  - "[[Translation]]"
  - "[[RNA Processing]]"
  - "[[Gene]]"
  - "[[Operon]]"
  - "[[Gene Expression]]"
  - "[[Nonsense-Mediated Decay]]"
  - "[[RNA Sequencing]]"
projects:
  - "[[02-sequence-translation]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Messenger RNA

> [!abstract]
> A messenger RNA is the working copy of a gene sent to the ribosome: a protein-coding stretch in the middle, untranslated regions on both sides, and, in eukaryotes, a protective cap at the 5' end and a poly(A) tail at the 3' end.

## Definition

**Messenger RNA (mRNA)** is the RNA that carries the coding sequence of a protein-coding [[Gene|gene]] from DNA to the ribosomes, where it is translated. Read 5' → 3', a mature mRNA consists of a **5' untranslated region (5' UTR)**, the **coding sequence (CDS)** from a start codon to a stop codon, and a **3' untranslated region (3' UTR)**; a eukaryotic mRNA also carries a **5' cap** and a **3' poly(A) tail**.[^os15][^alberts]

## Why it matters

- **Transcript models.** Every protein-coding transcript in an annotation is an mRNA model: exon coordinates plus the CDS boundaries inside them ([[Gene Annotation]], [[Gene#Advanced (L3)]]). Translating a transcript from its first nucleotide instead of its CDS start gives a wrong protein ([[02-sequence-translation]]).
- **cDNA and RNA-seq.** mRNA is usually sequenced after being copied into cDNA; the poly(A) tail lets an oligo(dT) primer start that copy on mRNAs specifically ([[Reverse Transcription]], [[RNA Sequencing]]).[^alberts]
- **Isoforms.** Transcripts of one gene can differ in their UTRs as well as in their CDS, which matters when reads are assigned to isoforms ([[Transcript Quantification]]).[^alberts-reg]
- **Variant effects.** A variant in a UTR leaves the protein sequence unchanged but can alter regulation; one in the CDS can change the protein ([[Variant Annotation]], [[Codon]]).

## Core (L1)

![[mrna-anatomy-eukaryote-bacteria.svg]]

**The parts, from 5' to 3'.**[^os15][^alberts][^alberts-reg]

| Part | What it is | Main role |
|---|---|---|
| 5' cap | a 7-methylguanosine joined to the first nucleotide by a 5'-5' triphosphate bridge (eukaryotes) | protects the 5' end, helps export from the nucleus and recruits the ribosome |
| 5' UTR | transcribed nucleotides before the start codon | scanned by the small ribosomal subunit (eukaryotes); carries the ribosome-binding site (bacteria) |
| start codon | usually AUG | fixes where translation begins and the [[Reading Frame]] |
| CDS | codons from the start codon to the stop codon | translated into the protein ([[Codon]], [[Translation]]) |
| stop codon | UAA, UAG or UGA | ends translation |
| 3' UTR | transcribed nucleotides after the stop codon | signals that control stability, localization and translation; contains the AAUAAA polyadenylation signal (eukaryotes) |
| poly(A) tail | about 200 adenosines added after cleavage (eukaryotes) | protects the 3' end, helps export and translation |

**Only the CDS is translated.** The UTRs are transcribed and kept in the mature mRNA, but ribosomes do not turn them into protein. Transcription starts upstream of the start codon and ends downstream of the stop codon, which is why both UTRs exist ([[Transcription#Common misconceptions]]).[^os15]

**Cap and tail are not in the gene.** Both are added to the pre-mRNA during [[RNA Processing]], together with splicing, which removes introns: the genome encodes the UTRs and the CDS (in exons) and the AAUAAA signal, not the cap or the tail.[^os15]

**Bacteria versus eukaryotes.**[^alberts][^os15]

| | Bacteria | Eukaryotes |
|---|---|---|
| Ends | no cap, no protective poly(A) tail | 5' cap and poly(A) tail |
| Coding sequences per mRNA | often several (**polycistronic**, from an [[Operon]]) | usually one (**monocistronic**) |
| How the ribosome finds the start | Shine-Dalgarno sequence in the 5' UTR pairs with the 16S rRNA | small subunit binds the cap and scans to the first suitable AUG |
| Processing and timing | translated while still being transcribed | processed and exported from the nucleus first |
| Lifetime | short | much longer half-life |

## Deeper (L2)

**Finding the start codon.** In eukaryotes, the small subunit loaded at the cap scans 5' → 3'. The nucleotides around an AUG influence how efficiently it is recognized: an AUG in a poor context is sometimes skipped, and ribosomes start at a later AUG instead (**leaky scanning**), which makes proteins that differ at their N-terminus from one mRNA.[^alberts] In bacteria, each CDS of a polycistronic mRNA has its own Shine-Dalgarno site a few nucleotides upstream of its start codon, so each is initiated independently ([[Translation#Deeper (L2)]]).[^alberts] A consequence of scanning: an AUG in the 5' UTR (an upstream AUG) is met first and can start a short upstream [[Open Reading Frame]] instead of the main CDS.

**Cap and tail work together.** The cap and the poly(A) tail are bound by proteins that promote translation initiation and protect the mRNA. In eukaryotes, degradation of many mRNAs starts with gradual shortening of the poly(A) tail (deadenylation), followed by removal of the cap and exonuclease digestion of the body.[^alberts-reg]

**The 3' UTR is a regulatory region.** Sequences in the 3' UTR determine how long an mRNA lasts, where it goes in the cell and how often it is translated.[^alberts-reg] Cleavage and polyadenylation occur downstream of the AAUAAA signal ([[Transcription#Deeper (L2)]]).[^os15] Some genes have several polyadenylation sites; choosing one or another produces mRNAs with different 3' ends, sometimes with different C-terminal coding sequences.[^alberts-reg]

**Lifetime.** Eukaryotic mRNAs have a much longer half-life than bacterial ones.[^os15] Because each mRNA is made and destroyed continuously, its level in a cell reflects both its synthesis and its decay rate, which is why mRNA abundance, what RNA-seq measures, is not a direct readout of transcription ([[Gene Expression]]).[^alberts-reg]

## Advanced (L3)

- **What a transcript sequence contains.** Transcript records are usually written in DNA letters ([[RNA#Common misconceptions]]). The cap cannot be written in the four-letter alphabet, and the poly(A) tail, added after transcription, is absent from the genome from which transcript models are built. A transcript sequence is therefore 5' UTR + CDS + 3' UTR, and its CDS starts at position $|5'\text{UTR}| + 1$, not at 1.
- **Capture bias.** Any method that captures RNA through its poly(A) tail with oligo(dT) sees only polyadenylated molecules: it enriches eukaryotic mRNAs and misses RNAs without a tail.[^alberts] Library type is part of the metadata every transcriptomic analysis must check ([[RNA Sequencing]]).
- **Isoforms at both ends.** Alternative promoters and alternative polyadenylation change the UTRs, and [[Alternative Splicing]] can change both UTRs and CDS. Two isoforms with identical proteins can still be regulated differently through their 3' UTRs.[^alberts-reg]
- **Quality control.** A stop codon located well before the end of the CDS can trigger degradation of the mRNA in eukaryotes ([[Nonsense-Mediated Decay]], [[Translation#Advanced (L3)]]), so the position of a premature stop relative to the mRNA's exon structure predicts whether a truncated protein is made at all.[^alberts]

## Mathematical representation

**Anatomy as a word.** Let $\Sigma = \{A, C, G, U\}$ and $T = \{UAA, UAG, UGA\}$. A mature eukaryotic mRNA, without its cap $\gamma$ (not a letter of $\Sigma$), is a concatenation

$$m = u \cdot c \cdot v \cdot A^{k},$$

where $u$ is the 5' UTR, $v$ the 3' UTR, $k$ the tail length, and the CDS $c$ satisfies:

- $|c| = 3\ell$, with $c_1 c_2 c_3 = AUG$;
- its last codon is in $T$ and none of its first $\ell - 1$ codons is;
- under the strict scanning model, the first occurrence of $AUG$ in $m$ starts at position $|u| + 1$.

The protein has $\ell - 1$ residues and $|m| = |u| + 3\ell + |v| + k$. These conditions are checked codon by codon from left to right, so recognizing this anatomy needs only a finite-state scan ([[State Machine]], [[Regular Expression]]).

**Level of an mRNA.** If mRNA molecules are made at a constant rate $k_s$ (molecules per unit time) and each is degraded with probability rate $k_d$, the number $M(t)$ follows

$$\frac{dM}{dt} = k_s - k_d M, \qquad M^* = \frac{k_s}{k_d}, \qquad t_{1/2} = \frac{\ln 2}{k_d},$$

and after a change in $k_s$, $M$ approaches the new steady state $M^*$ exponentially with the same half-life ([[Ordinary Differential Equation]]). Stable mRNAs accumulate to higher levels but respond more slowly.

## Computational representation

A dissection of a mature mRNA under the model above: strip the tail, scan to the first AUG, read codons to the first stop.

```python
import re

STOPS = {"UAA", "UAG", "UGA"}


def dissect(mrna: str, min_tail: int = 10) -> dict:
    """Split a mature eukaryotic mRNA (5'->3', cap not written) into its parts.
    Model: first AUG = start (scanning rule), first in-frame stop = end of CDS,
    a terminal run of at least min_tail A = poly(A) tail."""
    s = mrna.upper().replace("T", "U")
    tail = re.search(f"A{{{min_tail},}}$", s)
    body = s[:tail.start()] if tail else s
    start = body.find("AUG")
    if start < 0:
        return {"error": "no AUG"}
    end = next((i + 3 for i in range(start, len(body) - 2, 3) if body[i:i + 3] in STOPS), None)
    if end is None:
        return {"error": "no in-frame stop: incomplete CDS"}
    utr3 = body[end:]
    return {
        "5'UTR": body[:start],
        "CDS": body[start:end],
        "3'UTR": utr3,
        "polyA": len(s) - len(body),
        "codons": (end - start) // 3,
        "AAUAAA_in_3'UTR": utr3.find("AAUAAA"),
    }


mrna = ("ACUUCGCAGCC" "AUGGCUAGCAAAGGUUGA" "CCUGCAGUAAUAAAGCCUUGCC" + "A" * 25)   # invented
for part, value in dissect(mrna).items():
    print(f"{part:16}{value}")
```

```text
5'UTR           ACUUCGCAGCC
CDS             AUGGCUAGCAAAGGUUGA
3'UTR           CCUGCAGUAAUAAAGCCUUGCC
polyA           25
codons          6
AAUAAA_in_3'UTR 8
```

`codons` includes the stop codon. The function accepts T or U, since transcript files usually use T. Real annotations do not infer the CDS this way: they record its coordinates, and code such as this is a consistency check on them.

## Worked example

> [!example] Reading a toy mature mRNA (invented, 76 nt without the cap)
> `5'-(cap) ACUUCGCAGCC AUG GCU AGC AAA GGU UGA CCUGCAGUAAUAAAGCCUUGCC AAA...A (25)-3'`
> 1. **Cap**: a 7-methylguanosine attached 5'-5' to the first A; it is not part of the letter sequence.
> 2. **5' UTR**: `ACUUCGCAGCC`, 11 nt, no AUG, so the scanning subunit reaches the start codon without stopping earlier.
> 3. **CDS**: `AUG GCU AGC AAA GGU UGA`, 6 codons = 18 nt, a multiple of 3. It encodes Met-Ala-Ser-Lys-Gly: 5 residues, $\ell - 1$ with $\ell = 6$.
> 4. **3' UTR**: `CCUGCAGUAAUAAAGCCUUGCC`, 22 nt. It contains `UAA` at offset 7, which does not matter: translation has already stopped. `AAUAAA` starts at offset 8: the polyadenylation signal.
> 5. **Tail**: 25 A. A real tail would be longer; its exact length is not encoded anywhere in the genome.
> 6. **Check**: $11 + 18 + 22 + 25 = 76$ nt.

## Common misconceptions

> [!warning] "An mRNA is translated from its first nucleotide"
> Translation starts at the start codon, after the 5' UTR, and stops before the 3' UTR. A transcript sequence must be cut at its CDS coordinates before translation.[^os15]

> [!warning] "The poly(A) tail is encoded in the gene"
> The gene encodes the AAUAAA signal; the tail is added by a poly(A) polymerase after the RNA is cut. Searching the genome for the tail finds nothing, and genomic and transcript sequences differ at the 3' end for this reason.[^os15]

> [!warning] "UTRs are useless leftovers"
> UTRs carry the signals that position ribosomes (5' UTR) and control mRNA stability, localization and translation (3' UTR). Variants there can change how much protein is made without changing the protein.[^alberts-reg]

> [!warning] "Every mRNA encodes one protein"
> Bacterial polycistronic mRNAs encode several proteins, one per CDS, and in eukaryotes leaky scanning can produce several N-terminal variants from one mRNA.[^alberts]

## Exercises

> [!question] Exercise 1 (L1)
> For the toy mRNA `5'-GGCAAGCAUG UUU GGC UGA CCAAUAAAGG AAAAAAAAAAAAAAA-3'` (spaces for readability, cap not written), identify the 5' UTR, CDS, 3' UTR and tail, give their lengths and the encoded peptide.

> [!success]- Solution
> The first AUG is at positions 8 to 10 (1-based) of `GGCAAGCAUG`, so the 5' UTR is `GGCAAGC` (7 nt). CDS: `AUG UUU GGC UGA` (12 nt, 4 codons) encoding Met-Phe-Gly. 3' UTR: `CCAAUAAAGG` (10 nt), containing AAUAAA. Tail: 15 A.

> [!question] Exercise 2 (L1)
> Which parts of a eukaryotic mRNA are present in (a) the genomic DNA of the gene, (b) the cDNA made from the mature mRNA with an oligo(dT) primer, (c) the protein?

> [!success]- Solution
> (a) The 5' UTR, CDS and 3' UTR (split by introns), including the AAUAAA signal; not the cap or the tail. (b) The complement of everything from the 5' end to the tail: UTRs, CDS without introns, and a stretch of T copied from the tail; no cap. (c) Only the CDS, translated from the start codon to the codon before the stop.

> [!question] Exercise 3 (L2)
> A eukaryotic mRNA has a CDS whose codons 1 and 5 are both AUG, in the same frame. The first AUG lies in a poor context. What proteins can the mRNA make, and how do they differ? What would a second, *out-of-frame* AUG located inside the CDS produce under leaky scanning?

> [!success]- Solution
> Most ribosomes start at codon 1 and make the full protein; those that skip the poorly recognized first AUG start at codon 5 and make the same protein without its first four residues. Both end at the same stop. An out-of-frame AUG would start translation in a different reading frame: a different peptide, usually short because a stop codon soon occurs in that frame ([[Reading Frame]]).[^alberts]

> [!question] Exercise 4 (L2, Python)
> An invented bacterial mRNA is `GAUUCAGGAGGUAACAUGAAAGCUCGUUAAGCCAGGAGGCUAUCAUGUCUGGUGAAUAGCCU`. Using `AGGAGG` as a toy stand-in for the Shine-Dalgarno sequence, find each CDS as the first AUG within 12 nt after the motif, read to its stop codon.

> [!success]- Solution
> ```python
> import re
>
> BASES = "UCAG"
> CODE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES),
>                 "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
>
>
> def cistrons(mrna: str, sd: str = "AGGAGG", max_gap: int = 12) -> list[tuple[int, int, str]]:
>     """CDSs of a bacterial mRNA: an AUG at most max_gap nt after a Shine-Dalgarno-like motif,
>     read to the first in-frame stop. Returns (start, end, protein), 0-based, stop included."""
>     found = []
>     for m in re.finditer(sd, mrna):
>         window = mrna[m.end():m.end() + max_gap + 3]
>         k = window.find("AUG")
>         if k < 0:
>             continue
>         start, protein = m.end() + k, ""
>         for i in range(start, len(mrna) - 2, 3):
>             aa = CODE[mrna[i:i + 3]]
>             if aa == "*":
>                 found.append((start, i + 3, protein))
>                 break
>             protein += aa
>     return found
>
>
> operon = ("GAUUCAGGAGGUAACAUGAAAGCUCGUUAAGCCAGGAGGCUAUCAUGUCUGGUGAAUAGCCU")   # invented
> print(cistrons(operon))
> ```
> Output: `[(15, 30, 'MKAR'), (44, 59, 'MSGE')]`: two CDSs, each 4 nt downstream of its motif, as in the polycistronic panel of the figure. Real ribosome-binding sites are variable, so tools score a family of purine-rich motifs rather than one exact string ([[Sequence Motif]]).

> [!question] Exercise 5 (L3)
> With the model $dM/dt = k_s - k_d M$ and invented rates, a gene is transcribed at $k_s = 10$ mRNAs per minute. Compare an mRNA with a 30-minute half-life and one with a 5-minute half-life: steady-state levels, and time to reach 75 % of the new steady state after the gene is switched on (starting from $M = 0$).

> [!success]- Solution
> $k_d = \ln 2 / t_{1/2}$: 0.0231 and 0.1386 per minute. $M^* = k_s / k_d$: about 433 and 72 molecules. The solution from zero is $M(t) = M^*(1 - e^{-k_d t})$; 75 % is reached when $e^{-k_d t} = 1/4$, i.e. $t = 2\,t_{1/2}$: 60 minutes and 10 minutes. The stable mRNA reaches a 6-fold higher level but responds 6 times more slowly.

> [!question] Exercise 6 (L3, Python)
> Run `dissect` on these invented mRNAs and explain each result: (a) `GCCACC AUGUCUGAAUAA GCAAUAAAUC` + 30 A; (b) the same with `AAA` appended to the 3' UTR; (c) `GCCACC AUGUCUGAAUCA` + 30 A; (d) `GAUGACC AUGUCUGAAUAA GCAAUAAAUC` + 30 A.

> [!success]- Solution
> ```python
> tests = {                                                   # all invented
>     "complete":        "GCCACC" "AUGUCUGAAUAA" "GCAAUAAAUC" + "A" * 30,
>     "UTR ends in A":   "GCCACC" "AUGUCUGAAUAA" "GCAAUAAAUCAAA" + "A" * 30,
>     "no stop":         "GCCACC" "AUGUCUGAAUCA" + "A" * 30,
>     "uAUG in 5'UTR":   "GAUGACC" "AUGUCUGAAUAA" "GCAAUAAAUC" + "A" * 30,
> }
> for name, m in tests.items():
>     d = dissect(m)
>     print(f"{name:15}", d.get("error") or (d["5'UTR"], d["CDS"], d["3'UTR"], d["polyA"]))
> ```
> ```text
> complete        ('GCCACC', 'AUGUCUGAAUAA', 'GCAAUAAAUC', 30)
> UTR ends in A   ('GCCACC', 'AUGUCUGAAUAA', 'GCAAUAAAUC', 33)
> no stop         no in-frame stop: incomplete CDS
> uAUG in 5'UTR   ('G', 'AUGACCAUGUCUGAAUAA', 'GCAAUAAAUC', 30)
> ```
> (a) The intended parts. (b) A 3' UTR ending in A cannot be told apart from the tail: the boundary is ambiguous from sequence alone, which is why annotations use the genome to place the polyadenylation site. (c) Without an in-frame stop the CDS is incomplete, as in a truncated transcript. (d) The upstream AUG is 6 nt before the intended one, in the same frame, so the strict first-AUG rule predicts an N-terminally extended protein (Met-Thr-Met-Ser-Glu); whether cells use it depends on its context (Exercise 3).

## Mastery checklist

- [ ] 1 Recognized: I can name the parts of an mRNA in order: cap, 5' UTR, start codon, CDS, stop codon, 3' UTR, poly(A) tail.
- [ ] 2 Understood: I can explain what each part does, which parts are encoded in the genome, and how bacterial and eukaryotic mRNAs differ.
- [ ] 3 Practiced: I can dissect a transcript sequence into UTRs and CDS by hand and in code, and handle incomplete or ambiguous cases.
- [ ] 4 Applied: in [[02-sequence-translation]], I extract CDS and UTRs of real transcripts from their annotation and check them (start codon, stop codon, length multiple of 3).
- [ ] 5 Explained: I can teach how scanning, cap, tail and 3' UTR control translation and decay, and what this means for RNA-seq and variant interpretation.

## References

[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (eukaryotic transcription, RNA processing in eukaryotes, protein synthesis).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of mRNA processing, translation initiation in bacteria and eukaryotes (Shine-Dalgarno pairing, cap binding and scanning, leaky scanning), mRNA surveillance, and cDNA synthesis with oligo(dT) primers.
[^alberts-reg]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of posttranscriptional controls (alternative polyadenylation, 3' UTR control of stability and localization, deadenylation-dependent mRNA decay).
