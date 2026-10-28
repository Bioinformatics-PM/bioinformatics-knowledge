---
aliases:
  - Promoter Region
  - Core Promoter
  - Promoteur
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[DNA]]"
  - "[[Gene]]"
  - "[[Transcription]]"
  - "[[Sequence Motif]]"
related:
  - "[[Transcription Factor]]"
  - "[[Enhancer]]"
  - "[[Chromatin]]"
  - "[[Operon]]"
  - "[[Gene Regulation]]"
  - "[[CpG Island]]"
  - "[[Position Weight Matrix]]"
  - "[[Gene Finding]]"
  - "[[ATAC-Seq]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Molecular Cell Biology (Lodish)]]"
  - "[[Carninci 2006 - Genome-Wide Analysis of Mammalian Promoter Architecture and Evolution]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
  - "[[Karlin 1995 - Dinucleotide Relative Abundance Extremes]]"
---

# Promoter

> [!abstract]
> A promoter is the stretch of DNA at the start of a gene where RNA polymerase and its helper proteins bind: it decides where transcription starts, on which strand, and how often.

## Definition

A **promoter** is the DNA sequence to which RNA polymerase binds, together with the σ factor in bacteria or the general transcription factors in eukaryotes, to initiate transcription. It fixes the **transcription start site** (TSS, position +1) and, by its orientation, which DNA strand is used as template.[^os15][^alberts] In eukaryotes the **core promoter** is the short region around +1 where the general factors and RNA polymerase II assemble; **proximal promoter elements** just upstream bind gene-specific [[Transcription Factor|transcription factors]], and [[Enhancer|enhancers]] can act from much farther away.[^alberts][^lodish]

## Why it matters

- **Strand and coordinates.** "Upstream" is defined by the gene's direction: for a `-` strand gene it lies at **higher** genome coordinates. Promoter windows built without the strand are a classic silent bug (Computational representation).
- **Promoter windows in genome analyses.** Peaks of [[ChIP-Seq]] or [[ATAC-Seq]], methylation or motif counts are often summarized "at promoters", meaning a window around annotated TSSs. The window size is an analysis choice, and a gene with several TSSs has several promoters.[^carninci]
- **Sequence alone is weak evidence.** Promoter elements are short and degenerate, so their consensus sequences occur by chance thousands of times per genome ([[Sequence Motif#Deeper (L2)]]); requiring several elements at the right spacing helps but does not suffice (Exercise 4), which is why genome-wide start-site maps are used to locate promoters.[^carninci]
- **CpG islands flag mammalian promoters.** CG-rich islands are associated with the 5' ends of many genes,[^lander][^alberts] and a broad, CpG-rich class of promoters is distinct from TATA-box promoters.[^carninci] The observed/expected CpG ratio is the usual signal ([[CpG Island]], Exercise 5).

## Core (L2)

### Coordinates

The first transcribed nucleotide is **+1**; there is no position 0. Positions upstream (5' on the coding strand) are negative, downstream positive, so −10 is ten nucleotides before +1.[^os15] Promoter elements sit mostly upstream but can extend downstream of +1.

![[promoter-architecture-bacteria-eukaryote.svg]]

### Bacterial promoters

- The σ subunit of the RNA polymerase holoenzyme recognizes two elements, centred near **−35** (consensus `TTGACA`) and **−10** (consensus `TATAAT`); the AT-rich −10 region is where the double helix opens to form the transcription bubble. σ is needed only for initiation.[^os15] Both boxes sit at defined distances from +1, so their spacing is constrained too.[^os15]
- Real promoters match the consensus only approximately,[^os15] and promoters differ in strength.[^alberts]
- **Alternative σ factors** recognize other promoter sequences, so changing σ redirects the polymerase to whole sets of genes, such as the heat-shock genes.[^alberts]
- One promoter can serve several adjacent genes, transcribed into a single mRNA ([[Operon]]), and repressor or activator sites overlap or flank the promoter.[^os16]

### Eukaryotic promoters

Each of the three nuclear RNA polymerases uses its own kind of promoter ([[Transcription#Deeper (L2)]]); RNA polymerase III, for instance, transcribes tRNA genes from promoter elements located **inside** the transcribed region.[^alberts][^lodish] For RNA polymerase II:

- **Core elements**: the TFIIB recognition element (BRE) near −35, the **TATA box** near −30, bound by the TATA-binding protein (TBP) of TFIID, the **initiator** (Inr) spanning +1, and the downstream promoter element (DPE) near +30. Promoters contain different subsets of these elements; many have no TATA box.[^alberts][^carninci]
- **Assembly**: the general transcription factors bind the core promoter, recruit RNA polymerase II, open the DNA and release the polymerase into elongation (sequence of events in [[Transcription#Deeper (L2)]]).[^alberts]
- **Proximal elements**, such as GC boxes bound by Sp1 and CCAAT boxes, bind gene-specific activators that set the rate.[^lodish][^alberts]
- **Chromatin**: the promoter must be accessible; active promoters are depleted of nucleosomes and hypersensitive to DNase I digestion ([[Chromatin]]).[^alberts]

| Feature | Bacteria (σ70) | Eukaryotes (RNA polymerase II) |
|---|---|---|
| Recognized by | σ subunit of the holoenzyme | general transcription factors, then the polymerase |
| Core elements | −35 and −10 boxes, with a spacer | BRE, TATA, Inr, DPE, in varying combinations |
| Opening the DNA | at the AT-rich −10 region | helicase activity of TFIIH, with ATP hydrolysis |
| Nearby control | operators and activator sites next to or overlapping the promoter | proximal elements, plus distant enhancers |
| Genes per promoter | often several (operon) | usually one; one gene can have several promoters |
| DNA packaging | no nucleosomes | nucleosomes must be displaced |

(Table after [^os15][^os16][^alberts][^lodish]; alternative promoters after [^carninci].)

## Advanced (L3)

- **Promoter shape.** Sequencing tags for several hundred thousand start sites in mouse and human, Carninci and colleagues found two broad classes: TATA-box-enriched promoters with a well-defined start site, and broad, CpG-rich promoters that start over a range of positions and evolve more readily; tissues and gene families favour different types.[^carninci] "The" TSS of a broad promoter is a distribution, summarized by its peak.
- **Alternative promoters.** Differentially regulated alternative start sites are common in protein-coding genes and often produce alternative protein N-termini; start sites were also found within most exons and in 3' UTRs.[^carninci] An annotation file therefore lists a TSS per **transcript**, and a promoter window should be built per transcript, not per gene ([[Gene#Advanced (L3)]], [[Alternative Splicing]]).
- **CpG islands.** CG dinucleotides are rare in vertebrate DNA because methylated C deaminates to T ([[DNA Repair#Core (L2)]]), but CG-rich islands that escape methylation surround many promoters, notably those of housekeeping genes.[^alberts][^lander] The observed/expected ratio of a dinucleotide is the relative abundance that Karlin and Burge used as a genomic signature.[^karlin]
- **Promoters in chromatin data.** Because active promoters are nucleosome-depleted,[^alberts] they should appear as accessibility peaks at annotated TSSs in any chromatin-accessibility dataset ([[ATAC-Seq]]). Their regulation by marks and methylation is the subject of [[Epigenetics]].

## Mathematical representation

**Relative to genomic coordinates.** For a gene with TSS at 1-based genomic coordinate $g$, a relative position $x \in \mathbb{Z} \setminus \{0\}$ maps to
$$\gamma_+(x) = g + x - \mathbb{1}[x > 0], \qquad \gamma_-(x) = g - x + \mathbb{1}[x > 0],$$
on the `+` and `-` strands. The window from $-u$ to $+d$ is, as a 0-based half-open ([[BED Format|BED]]) interval, $[g - 1 - u,\; g - 1 + d)$ on `+` and $[g - d,\; g + u)$ on `-`.

**Two-box score.** For a sequence $x$ read 5' → 3' on the coding strand, with Hamming distance $h$, start $i$ of the −35 box and spacer $s$ in an allowed set $\mathcal{S}$:
$$S(i, s) = h\big(x_{i..i+5}, \texttt{TTGACA}\big) + h\big(x_{i+6+s\,..\,i+11+s}, \texttt{TATAAT}\big), \qquad (\hat{\imath}, \hat{s}) = \arg\min_{i,\, s \in \mathcal{S}} S(i, s).$$

**Chance matches.** In a uniform random sequence, a 6-mer lies within $k$ mismatches of a given consensus with probability $P_k = \sum_{m=0}^{k} \binom{6}{m} 3^m / 4^6$. The expected number of chance two-box matches on both strands of a sequence of length $L$ is about $2 L\, |\mathcal{S}|\, P_k^2$ (edges and overlaps ignored): two boxes multiply two small probabilities.

**CpG observed/expected.** With $N_{XY}$ the count of dinucleotide $XY$ over the $n - 1$ positions and $N_X$ the count of base $X$ in a sequence of length $n$,
$$\rho_{CG} = \frac{f_{CG}}{f_C\, f_G}, \qquad f_{CG} = \frac{N_{CG}}{n - 1},\; f_C = \frac{N_C}{n},\; f_G = \frac{N_G}{n},$$
the relative abundance of CG,[^karlin] about 1 when C and G are adjacent as often as their frequencies predict.

## Computational representation

Annotations give the TSS as the 5' end of each transcript, that is its start on `+` and its end on `-` ([[GFF Format]]). Extract the window with the strand, read it on the coding strand, then scan:

```python
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def reverse_complement(dna: str) -> str:
    return dna.translate(COMPLEMENT)[::-1]


def promoter_window(tss: int, strand: str, upstream: int, downstream: int,
                    chrom_len: int) -> tuple[int, int]:
    """BED-style [start, end) covering -upstream..-1 and +1..+downstream around a 1-based TSS."""
    i = tss - 1                                   # 0-based index of +1
    if strand == "+":
        start, end = i - upstream, i + downstream
    else:                                         # minus strand: upstream lies at higher coordinates
        start, end = i - downstream + 1, i + upstream + 1
    return max(0, start), min(chrom_len, end)


def promoter_sequence(genome: str, tss: int, strand: str, upstream: int, downstream: int) -> str:
    """The promoter read 5'->3' on the gene's coding strand."""
    start, end = promoter_window(tss, strand, upstream, downstream, len(genome))
    seq = genome[start:end]
    return seq if strand == "+" else reverse_complement(seq)


def hamming(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))


def sigma70_scan(seq: str, spacers=range(15, 20)) -> tuple[int, int, int, int]:
    """Best (-35 start, spacer, -10 start, total mismatches) over the allowed spacer lengths."""
    best = None
    for i in range(len(seq) - 5):
        m35 = hamming(seq[i:i + 6], "TTGACA")
        for s in spacers:
            j = i + 6 + s
            if j + 6 > len(seq):
                break
            total = m35 + hamming(seq[j:j + 6], "TATAAT")
            if best is None or total < best[3]:
                best = (i, s, j, total)
    return best


# invented toy genome: a promoter for a gene on the minus strand, TSS at coordinate 18
region = "GCATG" + "TTGACA" + "ATTAGCTCGGTACGATC" + "TATAAT" + "GCGCAT" + "ACAGAGCATG"
genome = "CCGTTAGC" + reverse_complement(region) + "GATTACAGG"
print(len(region), len(genome), genome)
print(promoter_window(18, "-", 40, 10, len(genome)))
prom = promoter_sequence(genome, 18, "-", 40, 10)
print(prom, prom == region)
print(sigma70_scan(prom))
wrong = promoter_sequence(genome, 18, "+", 40, 10)
print(wrong, sigma70_scan(wrong))
```

```text
50 67 CCGTTAGCCATGCTCTGTATGCGCATTATAGATCGTACCGAGCTAATTGTCAACATGCGATTACAGG
(8, 58)
GCATGTTGACAATTAGCTCGGTACGATCTATAATGCGCATACAGAGCATG True
(5, 17, 28, 0)
CCGTTAGCCATGCTCTGTATGCGCATT (0, 15, 21, 8)
```

The spacer range 15-19 is a parameter of this sketch. Treating the gene as `+` reads the wrong side of the TSS, is clipped at the chromosome start, and finds nothing better than 8 mismatches. Real scanners replace the consensus by [[Position Weight Matrix|position weight matrices]].

## Worked example

> [!example] A bacterial promoter on the minus strand, by hand (invented sequence)
> The genome FASTA shows `CCGTTAGC CATGCTCTGTATGCGCATTATAGATCGTACCGAGCTAATTGTCAACATGC GATTACAGG` (spaces added). The gene is on `-` with its TSS at coordinate 18.
> 1. **Window.** From −40 to +10 on `-`: $[g - d, g + u) = [18 - 10, 18 + 40) = [8, 58)$, the 50 bases between the spaces.
> 2. **Orient.** Reverse-complement them to read the coding strand 5' → 3': `GCATG TTGACA ATTAGCTCGGTACGATC TATAAT GCGCAT A CAGAGCATG`.
> 3. **Positions.** The window starts at −40, so `TTGACA` occupies −35 to −30, the 17-nt spacer −29 to −13, `TATAAT` −12 to −7, and the `A` after `GCGCAT` is +1.
> 4. **Check on the genome.** Position +1 (index 40 of the oriented window) is plus-strand coordinate $\gamma_-(1) = 18$, whose base `T` pairs with the `A` read on the minus strand.

## Common misconceptions

> [!warning] "The promoter is transcribed"
> The promoter positions the polymerase; transcription starts at +1, so most promoter elements are not in the RNA. The Inr and DPE are exceptions that overlap the transcribed region.[^alberts]

> [!warning] "Every eukaryotic promoter has a TATA box"
> The TATA box is one of several core elements, present in some promoters only; broad, CpG-rich promoters are a separate class.[^alberts][^carninci]

> [!warning] "Upstream means lower coordinates"
> Only for `+` strand genes. For `-` strand genes, upstream is toward higher coordinates, and the promoter must be reverse-complemented to be read 5' → 3'.

> [!warning] "A gene has one promoter"
> Many genes have alternative start sites, regulated differently and sometimes changing the protein's N-terminus.[^carninci] Promoters belong to transcripts.

## Exercises

> [!question] Exercise 1 (L2)
> A gene's TSS is at 1-based coordinate 1,000,000. Give the 1-based coordinate of position −30 if the gene is on `+`, then on `-`. Check with `promoter_window`.

> [!success]- Solution
> `+`: $\gamma_+(-30) = 1{,}000{,}000 - 30 = 999{,}970$. `-`: $\gamma_-(-30) = 1{,}000{,}000 + 30 = 1{,}000{,}030$. With `promoter_window(1_000_000, strand, 30, 0, 2_000_000)`, position −30 is the first base of the `+` window (0-based start 999,969, 1-based 999,970) and the last base of the `-` window (end 1,000,030).

> [!question] Exercise 2 (L2)
> Sort these elements into bacterial and eukaryotic (RNA polymerase II), and order each group 5' → 3' with approximate positions: Inr, `TATAAT` box, DPE, TATA box, `TTGACA` box, BRE.

> [!success]- Solution
> Bacterial: `TTGACA` (−35), `TATAAT` (−10). Eukaryotic: BRE (near −35), TATA box (near −30), Inr (spanning +1), DPE (near +30).[^os15][^alberts] Similar names do not mean homologous elements: the bacterial −10 box is read by σ, the TATA box by TBP.

> [!question] Exercise 3 (L2)
> Why can one bacterial promoter drive several protein-coding genes, while a eukaryotic RNA polymerase II promoter usually drives one?

> [!success]- Solution
> A bacterial mRNA can carry several coding sequences, each with its own start and stop codons, so co-transcribed genes are each translated ([[Operon]]).[^os16][^alberts] A eukaryotic ribosome usually starts from the 5' cap and initiates at the first suitable AUG ([[Translation]]),[^alberts] so a second coding sequence on the same mRNA is rarely translated: each gene needs its own promoter.

> [!question] Exercise 4 (L3, Python)
> In a uniform random sequence the size of the *E. coli* K-12 genome (4,639,221 bp, both strands), estimate the chance matches of: one 6-mer box with at most one mismatch; both boxes with at most one mismatch each and 5 allowed spacer lengths; both boxes exact.

> [!success]- Solution
> ```python
> from math import comb
>
> p_box = sum(comb(6, m) * 3 ** m for m in range(2)) / 4 ** 6      # <= 1 mismatch to a 6-mer
> L, spacers = 4_639_221, 5
> single = 2 * L * p_box
> pair = 2 * L * spacers * p_box ** 2
> print(round(p_box, 5), round(single), round(pair))
> p_exact = 1 / 4 ** 6
> print("exact pair:", round(2 * L * spacers * p_exact ** 2, 2))
> ```
> ```text
> 0.00464 43040 998
> exact pair: 2.77
> ```
> One fuzzy box: about 43,000 chance hits; two fuzzy boxes at a constrained spacing: about 1,000; two exact boxes: about 3. But real promoters are fuzzy too, so a threshold loose enough to catch them also admits about a thousand chance sites: sequence scanning proposes candidates, start-site data decide.

> [!question] Exercise 5 (L3, Python)
> Compute the GC fraction and the CpG observed/expected ratio $\rho_{CG}$ of two invented sequences, `GCGCGGCTCCGCGAGCGCCGGCGTCGCGCATGCGCGGGCTCGCCGCGTACGC` (promoter-like) and `ATGCTCAGTTCCAGGAAGCTTCTGAGCCTAGCACGTGCCATCTGGAGCTTGAACA` (background).

> [!success]- Solution
> ```python
> def cpg_obs_exp(seq: str) -> float:
>     """Observed/expected CpG: f(CG) / (f(C) f(G)), with dinucleotide frequency over n-1 positions."""
>     n = len(seq)
>     f_cg = sum(seq[i:i + 2] == "CG" for i in range(n - 1)) / (n - 1)
>     return f_cg / ((seq.count("C") / n) * (seq.count("G") / n))
>
>
> promoter_like = "GCGCGGCTCCGCGAGCGCCGGCGTCGCGCATGCGCGGGCTCGCCGCGTACGC"   # invented
> background = "ATGCTCAGTTCCAGGAAGCTTCTGAGCCTAGCACGTGCCATCTGGAGCTTGAACA"    # invented
> for name, s in (("promoter-like", promoter_like), ("background", background)):
>     gc = (s.count("G") + s.count("C")) / len(s)
>     print(name, len(s), round(gc, 2), round(cpg_obs_exp(s), 2))
> ```
> ```text
> promoter-like 52 0.85 1.64
> background 55 0.53 0.27
> ```
> The background has an ordinary GC fraction but few CG steps (ratio 0.27), the depletion expected in vertebrate DNA; the promoter-like sequence is GC-rich and has more CG steps than its composition predicts. Island definitions add thresholds on length, GC fraction and this ratio ([[CpG Island]]).

> [!question] Exercise 6 (L3)
> A gene has two annotated transcripts whose TSSs are 5 kb apart, one used in liver, one in brain. A study reports "no change in promoter methylation" from a ±1 kb window around the gene's first TSS. What could it have missed?

> [!success]- Solution
> The window covers only one of the two promoters. If the brain-specific promoter changed, the change lies 5 kb away, outside the window. Alternative start sites are common and differentially regulated,[^carninci] so promoter analyses should use transcript-level TSSs, and expression should be checked per transcript.

## Mastery checklist

- [ ] 1 Recognized: I can define promoter, TSS, core promoter, −35 and −10 boxes, TATA box and proximal elements.
- [ ] 2 Understood: I can explain how σ and the general transcription factors find promoters, and contrast bacterial and eukaryotic promoters point by point.
- [ ] 3 Practiced: I can build strand-aware promoter windows, scan for σ70 boxes with a spacer constraint, and compute CpG observed/expected in Python.
- [ ] 4 Applied: I built per-transcript promoter windows from a real GFF file and checked them against accessibility or start-site data in a genome browser.
- [ ] 5 Explained: I can teach why promoter prediction from sequence fails, how promoter shape and alternative TSSs complicate annotation, and how to choose a promoter window.

## References

[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (prokaryotic promoters, σ factor, −10 and −35 consensus; numbering from +1).
[^os16]: [[Biology 2e (OpenStax)]], ch. 16 "Gene Expression" (operons: one promoter for several genes; repressor and activator sites).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of transcription initiation (bacterial promoters and σ factors, general transcription factors and core promoter elements of RNA polymerase II, RNA polymerase III promoters), chromatin at active genes, CG islands, and eukaryotic translation initiation.
[^lodish]: [[Molecular Cell Biology (Lodish)]], 4th ed. (2000), treatment of eukaryotic promoters (core and promoter-proximal elements, RNA polymerase III promoters).
[^carninci]: [[Carninci 2006 - Genome-Wide Analysis of Mammalian Promoter Architecture and Evolution]], *Nature Genetics* 38:626-635.
[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]], *Nature* 409:860-921, analysis of CpG islands.
[^karlin]: [[Karlin 1995 - Dinucleotide Relative Abundance Extremes]], *Trends in Genetics* 11:283-290.
