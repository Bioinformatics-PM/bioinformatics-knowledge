---
aliases:
  - GC Ratio
  - G+C Content
  - GC Percentage
  - Base Composition
  - Contenu en GC
tags:
  - type/concept
  - domain/bioinformatics
  - domain/biology
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[DNA]]"
  - "[[Nucleotide]]"
  - "[[Base Pairing]]"
  - "[[FASTA Format]]"
  - "[[String]]"
related:
  - "[[Reverse Complement]]"
  - "[[K-mer]]"
  - "[[GC Skew]]"
  - "[[CpG Island]]"
  - "[[Codon Usage Bias]]"
  - "[[Genome]]"
  - "[[Horizontal Gene Transfer]]"
  - "[[Binomial Distribution]]"
projects:
  - "[[01-dna-engine]]"
sources:
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
---

# GC Content

> [!abstract]
> GC content is the fraction of a DNA sequence made of guanine and cytosine: one number for a whole genome, or a curve along it when computed in sliding windows, that tells you about the species, the region and the stability of the double helix.

## Definition

The **GC content** of a nucleotide sequence is the proportion of its bases that are G or C, usually reported as a percentage. Because G pairs with C in the double helix, a strand and its partner have the same GC content, and in double-stranded DNA the amounts of G and C are equal (Chargaff's rules); the G+C proportion itself varies between species.[^griffiths] The formal definition and the proof of strand invariance are in [[DNA#Mathematical representation]]; this note adds base composition, sliding windows and what the numbers mean biologically.

## Why it matters

- **A species-level descriptor.** GC content is reported for every sequenced genome: about 41% for the human genome on average, with substantial variation along the chromosomes.[^lander][^griffiths]
- **A map of genome heterogeneity.** Computed in windows, GC content reveals regions whose composition departs from their surroundings. In *E. coli* K-12, such "patches of unusual composition" were read as traces of genome plasticity through [[Horizontal Gene Transfer]].[^blattner] In the human genome, GC-rich regions tend to be gene-rich.[^lander]
- **Duplex stability.** G-C-rich DNA melts at a higher temperature, which matters for [[Polymerase Chain Reaction|PCR]] primers and hybridization probes.[^berg] See [[DNA#Deeper (L2)]] for why stacking, not only the third hydrogen bond, explains it.[^yakovchuk]
- **The background of every statistic.** Expected k-mer counts, random ORF lengths ([[Genetic Code#Mathematical representation]]), motif significance and alignment scores all start from a base composition model ([[K-mer]], [[Sequence Motif]], [[Sequence Alignment]]).
- **Lab.** `gc_content` and a windowed GC profile are the first functions of [[01-dna-engine]].

## Core (L1)

**Composition first, GC second.** The base composition of a sequence is its four counts $\#_A, \#_C, \#_G, \#_T$ (or their fractions). GC content summarizes them in one number; the AT content is its complement, $1 - \mathrm{GC}$.

**What to count in the denominator.** Real FASTA files contain `N` (unknown base), other [[IUPAC Nucleotide Code|IUPAC codes]] and lowercase (soft-masked) letters. The usual choice is to uppercase everything and divide by the number of A, C, G, T only; dividing by the full length would make a sequence with many `N` look AT-rich. State the choice in your code's documentation, because tools differ.

**Both strands, one number.** GC content is the same whatever strand you read, and the same for the [[Reverse Complement]]. Strand-specific composition (G versus C on one strand) is a different quantity, the [[GC Skew]].

**Sliding windows.** One number per genome hides structure. A **window** of $w$ bases is moved along the sequence by a **step** $h$, and each window gives one GC value; plotting them against position gives a **GC profile**.

![[gc-content-sliding-window.svg]]

The figure uses a toy genome (invented): 20 kb at 50% GC with a 2 kb segment at 35% GC inserted at 12 kb. With $w = 1000$, the segment appears as a dip far outside the random fluctuation band. The window size is a trade-off: small windows locate boundaries precisely but are noisy; large windows are smooth but blur or dilute short features (Exercise 4).

## Deeper (L2)

**How noisy is a window?** Under the simplest null model, bases are independent and each is G or C with probability $p$ (the genome-wide GC content). The number of G+C in a window of $w$ bases is then binomial ([[Binomial Distribution]]), so the window GC fraction has mean $p$ and standard deviation $\sqrt{p(1-p)/w}$. For $p = 0.5$: 0.050 at $w = 100$, 0.016 at $w = 1000$, 0.005 at $w = 10{,}000$. A window can be flagged with a [[Standard Score|z-score]] $z = (\mathrm{GC}_{\text{window}} - p)/\sqrt{p(1-p)/w}$.

**Why real genomes are "too variable".** Real GC profiles fluctuate more than this binomial band, because composition is itself heterogeneous: along human chromosomes GC content varies substantially and correlates with gene density,[^lander] and bacterial chromosomes carry patches of atypical composition acquired horizontally.[^blattner] The binomial model is a baseline for spotting such regions, not a description of the genome.

**Efficient windows.** Recounting each window costs $O(w)$, hence $O(nw/h)$ in total. A **prefix sum** $P_i$ (the number of G+C in the first $i$ bases) gives any window in $O(1)$ as $P_{i+w} - P_i$, so a whole profile costs $O(n)$ time; the same trick powers [[Rolling Hash|rolling hashes]] of k-mers.

**Beyond single bases.** The composition of dinucleotides is not the product of base frequencies. In the human genome the dinucleotide CG is rarer than expected from the frequencies of C and G, because the C of CG is typically methylated and methyl-C tends to mutate to T; the regions that escape this depletion are [[CpG Island|CpG islands]].[^durbin3] Measuring such departures is the subject of [[K-mer]] composition.

## Advanced (L3)

- **Composition as a null model.** Durbin and colleagues score an aligned pair of residues against a random model in which each residue appears with its background frequency $q_a$; for DNA, those $q_a$ come from the base composition.[^durbin2] A scoring scheme calibrated on 50% GC sequence overrates matches between two GC-rich sequences, a pitfall that returns in [[Substitution Matrix]] and [[E-Value]].
- **Composition shapes coding sequences.** The three stop codons are AT-rich, so random ORFs are longer in GC-rich genomes and ORF length thresholds must depend on GC content ([[Genetic Code]], Exercise 5; [[Gene Finding]]). Synonymous codon choice is also constrained by composition ([[Codon Usage Bias]]).
- **Segmenting instead of windowing.** Fixed windows impose an arbitrary scale. Treating the sequence as generated by a few hidden compositional states and inferring where the state changes is the hidden Markov model approach used for [[CpG Island|CpG islands]] and [[Gene Finding]].[^durbin3]
- **Strand asymmetry.** GC content ignores which strand carries the G. The difference $G - C$ on one strand changes sign at bacterial replication origins, which is the principle of [[GC Skew]].

## Mathematical representation

Let $s = s_1 \dots s_n$ be a sequence over the IUPAC alphabet and $\#_x(s)$ the number of positions equal to $x$ (after uppercasing).

- **Effective length** $n_{\text{eff}} = \#_A + \#_C + \#_G + \#_T$ (ambiguous symbols excluded).
- **Composition vector** $\hat{\pi} = (\hat{\pi}_A, \hat{\pi}_C, \hat{\pi}_G, \hat{\pi}_T)$ with $\hat{\pi}_x = \#_x / n_{\text{eff}}$, so $\sum_x \hat{\pi}_x = 1$.
- **GC content** $\mathrm{GC}(s) = \hat{\pi}_G + \hat{\pi}_C$, invariant under reverse complement ([[DNA#Mathematical representation]]).
- **Prefix sums** $P_0 = 0$, $P_i = P_{i-1} + \mathbb{1}[s_i \in \{G, C\}]$. The window starting after position $i$ has $\mathrm{GC}_i^{(w)} = (P_{i+w} - P_i)/w$, for $i = 0, h, 2h, \dots$ with $i + w \le n$ (step $h$): there are $\lfloor (n - w)/h \rfloor + 1$ windows.
- **Null model.** If bases are i.i.d. with $P(G \text{ or } C) = p$, then $w \cdot \mathrm{GC}^{(w)} \sim \mathrm{Binomial}(w, p)$, so $\mathbb{E}[\mathrm{GC}^{(w)}] = p$ and $\mathrm{Var}[\mathrm{GC}^{(w)}] = p(1-p)/w$.

## Computational representation

```python
from collections import Counter


def composition(seq: str) -> dict[str, float]:
    """Fractions of A, C, G, T among unambiguous bases (case-insensitive)."""
    counts = Counter(seq.upper())
    n = sum(counts[b] for b in "ACGT")
    return {b: counts[b] / n for b in "ACGT"} if n else {}


def gc_content(seq: str) -> float:
    """(G + C) / (A + C + G + T); N and other IUPAC codes are excluded."""
    comp = composition(seq)
    return comp["G"] + comp["C"] if comp else 0.0


def gc_windows(seq: str, w: int, step: int) -> list[tuple[int, float]]:
    """(0-based start, GC fraction) of every full window, in O(n) with prefix sums."""
    s = seq.upper()
    prefix = [0]                                   # prefix[i] = G+C count in s[:i]
    for base in s:
        prefix.append(prefix[-1] + (base in "GC"))
    return [(i, (prefix[i + w] - prefix[i]) / w) for i in range(0, len(s) - w + 1, step)]


seq = "ATGCGCGATTATAAATATTAGCGGCCGCTANNa"   # invented toy sequence
print({b: round(f, 3) for b, f in composition(seq).items()})
print(round(gc_content(seq), 3))
for start, gc in gc_windows(seq, w=10, step=5):
    print(f"{start:>2}-{start + 10:<2} {seq[start:start + 10]}  GC={gc:.2f}")
```

```text
{'A': 0.323, 'C': 0.194, 'G': 0.226, 'T': 0.258}
0.419
 0-10 ATGCGCGATT  GC=0.50
 5-15 CGATTATAAA  GC=0.20
10-20 ATAAATATTA  GC=0.00
15-25 TATTAGCGGC  GC=0.50
20-30 GCGGCCGCTA  GC=0.80
```

The windowed version divides by $w$, which is correct only for windows free of `N`; a production version keeps a second prefix sum of A/C/G/T counts and divides by it. Windows are reported with 0-based, half-open coordinates, as in [[BED Format]] ([[Genomic Coordinate System]]).

## Worked example

> [!example] Finding the odd region of a toy genome
> The genome of the figure (invented, generated with a fixed seed) has $p = 0.483$. With $w = 1000$, the binomial standard deviation is $\sqrt{0.483 \times 0.517 / 1000} = 0.0158$. Flagging windows with $z < -3$:
> ```text
> window  11500-12500  GC=0.415 z=-4.3
> window  12000-13000  GC=0.342 z=-8.9
> window  12500-13500  GC=0.342 z=-8.9
> window  13000-14000  GC=0.335 z=-9.4
> window  13500-14500  GC=0.405 z=-4.9
> ```
> 1. The three windows fully inside the inserted segment (12,000 to 14,000) have GC near its true value 0.35.
> 2. The two windows straddling a boundary have intermediate values: a window averages whatever it covers, so boundaries are known only to within about one window.
> 3. No window outside the segment is flagged. In a real bacterial genome, several such regions would appear, and the next step would be to check their genes and [[Codon Usage Bias|codon usage]] for signs of [[Horizontal Gene Transfer]].

## Common misconceptions

> [!warning] "The two strands have different GC content"
> GC content is identical on both strands, because every G on one strand faces a C on the other. What differs between strands is the balance of G versus C on each one, which is the [[GC Skew]].

> [!warning] "A gene has the GC content of its genome"
> The genome value is an average. Windows and individual genes can depart strongly from it, and those departures are the informative part: gene-rich human regions are GC-rich,[^lander] and horizontally acquired bacterial segments have atypical composition.[^blattner]

> [!warning] "Divide by the sequence length"
> With `N` runs (gaps in an assembly) in the denominator, GC content is underestimated in proportion to the gaps. Exclude ambiguous symbols, or report them separately.

> [!warning] "A window far from the mean proves a special region"
> Across thousands of windows, some cross $|z| > 3$ by chance (Exercise 5), and neighbouring overlapping windows are not independent. A flagged window is a candidate, to be confirmed by other evidence.

## Exercises

> [!question] Exercise 1 (L1)
> Compute by hand the GC and AT contents of `GATTACAGGC`, then of its reverse complement.

> [!success]- Solution
> G at positions 1, 8, 9 and C at 6, 10: $5/10 = 50\%$ GC, 50% AT. The reverse complement `GCCTGTAATC` has 2 G and 3 C: again 50%, as it must, since G and C swap roles.

> [!question] Exercise 2 (L1)
> A double-stranded genome is 58% GC. Give the percentage of each base. For a single 25-nt strand of it, what can you say?

> [!success]- Solution
> G = C = 29%, A = T = 21% (Chargaff's rules hold for the duplex). For a single strand, only that GC and AT are likely near 58% and 42% if the strand is typical; nothing forces G = C or A = T on one strand.

> [!question] Exercise 3 (L2)
> How many windows does `gc_windows` return for $n = 1{,}000{,}000$, $w = 1000$ and steps $h = 1000$, $h = 100$ and $h = 1$? What is the total work of the naive method and of the prefix-sum method for $h = 1$?

> [!success]- Solution
> $\lfloor (n - w)/h \rfloor + 1$: 1000, 9991 and 999,001 windows. Naive recounting costs about $999{,}001 \times 1000 \approx 10^9$ base checks for $h = 1$; prefix sums cost $n$ additions plus one subtraction per window, about $2 \times 10^6$ operations.

> [!question] Exercise 4 (L2, Python)
> A genome has $p = 0.4$. A 5 kb island has GC 0.1 lower. For $w = 100$, $1000$ and $10{,}000$, compute the window standard deviation and the shift of a window centred on the island, in units of that standard deviation. Which window size would you choose?

> [!success]- Solution
> ```python
> import math
>
> p = 0.4
> for w in (100, 1_000, 10_000):
>     sd = math.sqrt(p * (1 - p) / w)
>     shift = 0.1 * min(w, 5_000) / w          # a 5 kb island 0.1 below p, window centred on it
>     print(f"w={w:>6}  sd={sd:.4f}  shift={shift:.3f}  shift/sd={shift / sd:.1f}")
> ```
> ```text
> w=   100  sd=0.0490  shift=0.100  shift/sd=2.0
> w=  1000  sd=0.0155  shift=0.100  shift/sd=6.5
> w= 10000  sd=0.0049  shift=0.050  shift/sd=10.2
> ```
> At $w = 100$ the island is lost in noise. At $w = 10{,}000$ it is detected strongly, but the window is twice the island, so the shift is halved and its boundaries are invisible. $w = 1000$ is a good compromise: clear signal and boundaries to within about 1 kb.

> [!question] Exercise 5 (L3, Python)
> Cut the *E. coli* K-12 chromosome (4,639,221 bp) into non-overlapping 1 kb windows. Under the binomial null model with a normal approximation, how many windows would show $|z| > 3$ by chance alone? What does it imply when a real genome shows many more?

> [!success]- Solution
> ```python
> import math
>
> n_windows = 4_639_221 // 1_000            # non-overlapping 1 kb windows in E. coli K-12
> p_two_sided = math.erfc(3 / math.sqrt(2))  # P(|Z| > 3) for a standard normal
> print(n_windows, f"{p_two_sided:.5f}", round(n_windows * p_two_sided, 1))
> ```
> Output: `4639 0.00270 12.5`. About 12 windows cross the threshold by chance, so a single flagged window is weak evidence ([[Multiple Testing Correction]]). A real genome shows far more extreme windows than 12 because its composition is genuinely heterogeneous, the null model of independent, identically distributed bases is wrong at the genome scale; that heterogeneity is the biological signal.

## Mastery checklist

- [ ] 1 Recognized: I can define GC content and say why it is the same on both strands.
- [ ] 2 Understood: I can explain the denominator choice, the window trade-off and the link with duplex stability.
- [ ] 3 Practiced: I can compute composition and an $O(n)$ windowed GC profile, and a z-score under the binomial model.
- [ ] 4 Applied: in [[01-dna-engine]], I plotted the GC profile of a real bacterial genome from [[FASTA Format]] and inspected its atypical regions.
- [ ] 5 Explained: I can explain why real genomes break the binomial model, how composition enters k-mer, ORF and alignment statistics, and when to segment rather than window.

## References

[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), Chargaff's rules and base composition of DNA.
[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]], *Nature*, genome landscape: GC content.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science*, abstract.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research*.
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models" (the CpG island example).
[^durbin2]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (random model and log-odds scores).
