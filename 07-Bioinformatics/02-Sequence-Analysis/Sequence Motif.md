---
aliases:
  - Motif
  - DNA Motif
  - Consensus Sequence
  - Sequence Pattern
  - Motif de séquence
tags:
  - type/concept
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[K-mer]]"
  - "[[Reverse Complement]]"
  - "[[IUPAC Nucleotide Code]]"
  - "[[Regular Expression]]"
  - "[[Exact Pattern Matching]]"
related:
  - "[[Position Weight Matrix]]"
  - "[[Sequence Logo]]"
  - "[[Motif Finding]]"
  - "[[Transcription Factor]]"
  - "[[Promoter]]"
  - "[[Restriction Enzyme]]"
  - "[[Hamming Distance]]"
  - "[[Approximate Pattern Matching]]"
  - "[[GC Skew]]"
projects:
  - "[[01-dna-engine]]"
sources:
  - "[[Das 2007 - A Survey of DNA Motif Finding Algorithms]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Sequence Motif

> [!abstract]
> A sequence motif is a short pattern that recurs in many sequences because it does something, typically being recognized by a protein; you describe it by a consensus word, a set of allowed letters per position or a regular expression, and then scan sequences for it.

## Definition

A **DNA sequence motif** is a nucleic acid sequence pattern with some biological significance, such as being a binding site for a regulatory protein. It is usually short (about 5 to 20 bp) and recurs in different genes or several times within a gene.[^das] A motif is an abstraction over its **instances** (the actual sites): it can be written as an exact word, a **consensus** in which each position lists the allowed bases with [[IUPAC Nucleotide Code|IUPAC codes]],[^iupac] a [[Regular Expression]], or a probabilistic profile ([[Position Weight Matrix]]).

## Why it matters

- **Gene regulation.** [[Transcription Factor|Transcription factors]] bind short motifs;[^das] bacterial [[Promoter|promoters]] carry two consensus sequences, `TATAAT` at the −10 region and `TTGACA` at −35, recognized by the σ factor of RNA polymerase.[^openstax]
- **Replication.** DnaA boxes, 9-mers such as `ATGATCAAG` in *Vibrio cholerae*, mark bacterial replication origins ([[GC Skew]]).[^compeau]
- **Molecular biology tools.** [[Restriction Enzyme|Restriction enzymes]] cut at palindromic motifs such as EcoRI's `GAATTC`.[^alberts]
- **Annotation and discovery.** Scanning known motifs annotates regulatory regions; finding new ones is [[Motif Finding]], from co-regulated promoters or from conserved regions of orthologous sequences.[^das]
- **Lab.** Motif search on both strands, with IUPAC codes, is a core function of [[01-dna-engine]].

## Core (L1)

**From instances to a consensus.** Align the known sites (invented, loosely modelled on a −35 box) and read each column:

```text
site 1   T T G A C A A T
site 2   T T G A C T A T
site 3   T T T A C A A T
site 4   C T G A C A A T
site 5   T T G A C T A T
site 6   T T T A C A A C
         ---------------
strict   T T G A C A A T     most frequent base per column
IUPAC    T T K A C W A T     K = G or T, W = A or T (bases seen in >= 25% of sites)
regex    TT[GT]AC[AT]AT
```

**Four ways to write a motif**, from rigid to flexible:

| Representation | Example | Captures | Loses |
|---|---|---|---|
| Exact word | `TTGACAAT` | one sequence | all variation |
| IUPAC consensus | `TTKACWAT` | a set of allowed bases per position | how often each base occurs |
| Regular expression | `TT[GT]AC[AT]AT`, `ACG.{3,5}CGT` | sets, variable spacers | frequencies, mismatch tolerance |
| Profile ([[Position Weight Matrix]]) | a $4 \times k$ table of probabilities | base frequencies per position | dependencies between positions |

**Special shapes.** A **palindromic** motif equals its own [[Reverse Complement]], such as `CACGTG`; a **spaced dyad** (gapped) motif is two conserved half-sites separated by a non-conserved spacer.[^das] The second regular expression above is an invented dyad.

**Searching.** Scan the text for the motif and for its reverse complement ([[Reverse Complement#Deeper (L2)]]), allow overlapping matches, and report positions in plus-strand coordinates.

## Deeper (L2)

**Consensus hides the variability.** In the six sites above, the strict consensus `TTGACAAT` occurs only once (site 1): most real sites differ from the consensus somewhere. A consensus with $d$ allowed mismatches ([[Hamming Distance]], [[Approximate Pattern Matching]]) is closer to biology: in *E. coli*, the DnaA box appears only when one mismatch and both strands are allowed.[^compeau] A regular expression cannot say "any one position may differ" without listing every variant, one reason why regular expressions are the wrong tool for mismatch-tolerant motifs ([[Regular Expression]]).

**Chance matches.** Under a uniform random model, a position matches a motif with position sets $S_1, \dots, S_k$ with probability $\prod_j |S_j|/4$. A 6-mer consensus such as `TATAAT` is expected about $4.64 \times 10^6/4096 \approx 1133$ times per strand in a genome the size of *E. coli* K-12, about 2,265 on both strands, and about 43,000 if one mismatch is allowed (Exercise 3). A short consensus match is therefore not a site. Bacterial promoters combine two boxes at defined positions upstream of the transcription start;[^openstax] requiring both, at the right spacing, multiplies two small probabilities and removes most chance matches.

**Counting columns instead of choosing letters.** Keeping the counts of each base in each column, instead of a single letter, gives a count matrix, then a probability profile and log-odds scores: the [[Position Weight Matrix]], displayed as a [[Sequence Logo]]. The IUPAC threshold (here 25%) is an arbitrary cut of that richer information.

## Advanced (L3)

- **Discovery is a statistics problem.** Motif discovery looks for patterns **over-represented** in a set of sequences believed to share regulation, such as promoters of co-regulated genes, or conserved across orthologous regions (phylogenetic footprinting).[^das] Over-representation is judged against a background model of composition ([[GC Content]], [[K-mer]] expectations), and the search space of all $k$-mers with mismatches is huge, hence the greedy, randomized, Gibbs sampling and EM methods of [[Motif Finding]].
- **Motifs are recognized physically.** Proteins read base identity through the edges of base pairs exposed in the DNA grooves without opening the helix ([[DNA#Deeper (L2)]]),[^alberts] so binding tolerates some substitutions better than others; position-specific scores model that graded preference better than a yes-or-no consensus.
- **Protein motifs.** Short conserved patterns also exist in proteins (active sites, binding loops); they are described with the same toolkit (patterns and profiles) and are distinct from [[Protein Domain|domains]], which are larger independently folding units ([[Protein Family]]).

## Mathematical representation

- A **motif language** is a set $M \subseteq \Sigma^k$ (or of variable-length words, for regular expressions); a window $w$ of the text is an **instance** iff $w \in M$ or $\mathrm{rc}(w) \in M$.
- **IUPAC consensus** $S = (S_1, \dots, S_k)$ with $\emptyset \neq S_j \subseteq \{A, C, G, T\}$ defines $M_S = S_1 \times \dots \times S_k$, of size $\prod_j |S_j|$.
- **Hamming ball** around a consensus $c$: $B_d(c) = \{ w \in \Sigma^k : d_H(w, c) \le d \}$, of size $\sum_{i=0}^{d} \binom{k}{i} 3^i$ ($1 + 3k$ for $d = 1$).
- **Chance occurrences.** For a text of length $n$ with i.i.d. uniform bases, the expected number of matches on one strand is $(n - k + 1)\,|M|/4^k$; on both strands, twice that, unless the motif is its own reverse complement.
- **Regular expressions** denote regular languages, recognized by finite automata in $O(n)$ for a fixed pattern (the `re` engine uses backtracking instead, fine for short motifs).

## Computational representation

```python
import re
from collections import Counter

IUPAC = {"A": "A", "C": "C", "G": "G", "T": "T", "R": "AG", "Y": "CT", "S": "CG", "W": "AT",
         "K": "GT", "M": "AC", "B": "CGT", "D": "AGT", "H": "ACT", "V": "ACG", "N": "ACGT"}
CODE = {frozenset(bases): code for code, bases in IUPAC.items()}
COMPLEMENT = str.maketrans("ACGTRYSWKMBDHVN", "TGCAYRSWMKVHDBN")


def consensus(sites: list[str], min_fraction: float = 0.25) -> tuple[str, str]:
    """Strict consensus (most frequent base per column) and degenerate IUPAC consensus
    (all bases reaching min_fraction of the column)."""
    strict, degenerate = [], []
    for column in zip(*sites):
        counts = Counter(column)
        strict.append(counts.most_common(1)[0][0])
        kept = frozenset(b for b, c in counts.items() if c / len(sites) >= min_fraction)
        degenerate.append(CODE[kept])
    return "".join(strict), "".join(degenerate)


def iupac_regex(motif: str) -> str:
    """Translate an IUPAC motif into a regular expression: R -> [AG], N -> [ACGT]."""
    return "".join(IUPAC[c] if len(IUPAC[c]) == 1 else f"[{IUPAC[c]}]" for c in motif)


def search_both_strands(text: str, motif: str) -> list[tuple[int, str, str]]:
    """Overlapping matches of an IUPAC motif on both strands (+ strand coordinates).
    A motif equal to its reverse complement is scanned once and labelled '+/-'."""
    rc_motif = motif.translate(COMPLEMENT)[::-1]
    strands = [("+/-", motif)] if rc_motif == motif else [("+", motif), ("-", rc_motif)]
    hits = []
    for strand, m in strands:
        for match in re.finditer(f"(?=({iupac_regex(m)}))", text):   # lookahead: overlaps allowed
            hits.append((match.start(), strand, match.group(1)))
    return sorted(hits)


sites = ["TTGACAAT", "TTGACTAT", "TTTACAAT", "CTGACAAT", "TTGACTAT", "TTTACAAC"]  # invented aligned sites
strict, degenerate = consensus(sites)
print(strict, degenerate, iupac_regex(degenerate))
text = "GGTTTACTATCCAATAGTCAAGGTTGACAATG"                                         # invented toy text
print(search_both_strands(text, degenerate))
```

```text
TTGACAAT TTKACWAT TT[GT]AC[AT]AT
[(2, '+', 'TTTACTAT'), (13, '-', 'ATAGTCAA'), (23, '+', 'TTGACAAT')]
```

`re.finditer` alone skips overlapping matches; the zero-width lookahead `(?=(...))` reports every start. The hit at 13 is `ATAGTCAA`, the reverse complement of `TTGACTAT`, an instance on the minus strand. A motif equal to its own reverse complement is scanned only once, otherwise every site would be reported twice.

## Worked example

> [!example] How specific is a degenerate consensus?
> For the consensus `TTKACWAT` ($k = 8$) built above:
> 1. **Size of the language**: $|S_3| = |S_6| = 2$, other positions 1, so $|M| = 4$ words.
> 2. **Match probability per position and strand**: $4/4^8 = 6.1 \times 10^{-5}$, against $1/4^8 = 1.5 \times 10^{-5}$ for the strict consensus: degeneracy multiplies chance hits by 4.
> 3. **Expected chance hits** in a random sequence of *E. coli* size (4,639,221 bp), both strands: $2 \times 4{,}639{,}214 \times 4/65{,}536 \approx 566$ for `TTKACWAT`, about 142 for `TTGACAAT`.
> 4. **Consequence**: each extra degenerate position trades specificity for sensitivity. Deciding how much variation to allow is exactly the problem that profiles and scores solve more gracefully ([[Position Weight Matrix]]).

## Common misconceptions

> [!warning] "The consensus sequence is the real binding site"
> The consensus is a summary of many sites; individual sites usually differ from it and the consensus itself may be rare or absent in the genome, as with site 1 being the only exact consensus in the example.

> [!warning] "A match to the motif is a functional site"
> Short motifs match thousands of times by chance in a bacterial genome, and far more in a human genome. Function needs context: position, spacing, conservation, experimental evidence.

> [!warning] "Search one strand, the motif is written 5' to 3'"
> Proteins bind double-stranded DNA; a site on the minus strand appears as the reverse complement in the file. Always scan both strands.

> [!warning] "A regular expression can express any motif"
> It expresses sets and spacers well, but not "up to $d$ mismatches anywhere" or graded preferences; use Hamming neighbourhoods or a [[Position Weight Matrix]] for those.

## Exercises

> [!question] Exercise 1 (L1)
> Give the strict and IUPAC consensus (threshold 25%) of the invented sites `GATTC`, `GACTC`, `GATTC`, `CATTC`.

> [!success]- Solution
> Columns: G,G,G,C (C = 25%) → S; A; T,C,T,T (C = 25%) → Y; T; C. Strict: `GATTC`; IUPAC: `SAYTC`. Every minority base here reaches exactly 25%, so each becomes part of the consensus: thresholds matter.

> [!question] Exercise 2 (L1)
> Which of `TTGACA`, `TTTACA`, `CTGACA`, `TTGCCA` match the IUPAC motif `YTKACA`?

> [!success]- Solution
> Y = C/T and K = G/T. `TTGACA` yes, `TTTACA` yes, `CTGACA` yes, `TTGCCA` no (position 4 must be A).

> [!question] Exercise 3 (L2)
> For `TATAAT` in a random sequence of 4,639,221 bp, compute the expected number of exact matches on both strands, then of matches with at most one mismatch. Why does `TATAAT` not need the palindrome correction?

> [!success]- Solution
> One strand: $(4{,}639{,}221 - 5)/4^6 \approx 1133$; both strands $\approx 2265$. The Hamming ball of radius 1 has $1 + 6 \times 3 = 19$ words, so about $2265 \times 19 \approx 43{,}040$ chance matches. `TATAAT` is not its own reverse complement (`ATTATA`), so its two strands give distinct occurrences and the factor 2 applies.

> [!question] Exercise 4 (L2, Python)
> With `search_both_strands`, scan the invented text `GAATTCGAATTC` for `GAATTC` and explain why each site is reported once. Then scan `ACACGTGTACGT` for the palindromic motif `CACGTG` and the dyad regular expression `ACG.{3,5}CGT` (on the plus strand, with `re.finditer` and a lookahead).

> [!success]- Solution
> ```python
> print(search_both_strands("GAATTCGAATTC", "GAATTC"))
> print(search_both_strands("ACACGTGTACGT", "CACGTG"))
> print([(m.start(), m.group(1)) for m in re.finditer(r"(?=(ACG.{3,5}CGT))", "ACACGTGTACGT")])
> ```
> Output: `[(0, '+/-', 'GAATTC'), (6, '+/-', 'GAATTC')]`, then `[(1, '+/-', 'CACGTG')]`, then `[(2, 'ACGTGTACGT')]`. `GAATTC` and `CACGTG` equal their reverse complements, so the function scans once and labels each site `+/-`; scanning both orientations would report every site twice, once per strand. The dyad expression matches `ACG` + `TGTA` (4 bases) + `CGT`.

> [!question] Exercise 5 (L3)
> A motif-finding tool reports the 8-mer `TTKACWAT` as enriched in 50 promoters of 300 bp each (both strands), with 12 occurrences. Is that surprising under the uniform model? What would make the comparison fairer?

> [!success]- Solution
> Positions: $50 \times (300 - 7) = 14{,}650$ per strand, 29,300 on both. Expected: $29{,}300 \times 4/65{,}536 \approx 1.8$. Observing 12 is about 6.7 times the expectation, and $P(X \ge 12)$ for a Poisson with mean 1.8 is below $10^{-6}$, so it is surprising. Fairer: use the promoters' own base composition rather than a uniform model (promoter regions can be compositionally biased; the −10 box itself is AT-rich[^openstax]), compare with a control set of promoters that are not co-regulated, and correct for the number of motifs tested ([[Multiple Testing Correction]]).

## Mastery checklist

- [ ] 1 Recognized: I can define a sequence motif and give examples (promoter boxes, DnaA box, restriction site).
- [ ] 2 Understood: I can compare exact word, IUPAC consensus, regular expression and profile, and explain palindromic and dyad motifs.
- [ ] 3 Practiced: I can build a consensus from aligned sites, translate IUPAC to regex, and search both strands with overlapping matches.
- [ ] 4 Applied: in [[01-dna-engine]], I scanned a real genome for a known motif on both strands and compared the count with its chance expectation.
- [ ] 5 Explained: I can explain why consensus matches are weak evidence and how profiles and over-representation statistics improve on them.

## References

[^das]: [[Das 2007 - A Survey of DNA Motif Finding Algorithms]], *BMC Bioinformatics*.
[^iupac]: [[Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences]], *Nucleic Acids Research*.
[^openstax]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (prokaryotic transcription: the −10 and −35 promoter consensus sequences, bound by σ; the AT-rich −10 region).
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (DnaA boxes).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002).
