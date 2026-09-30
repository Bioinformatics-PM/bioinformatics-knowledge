---
aliases:
  - Dotplot
  - Dot Matrix
  - Dot Matrix Plot
  - Diagram Method
  - Matrice de points
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[K-mer]]"
  - "[[Reverse Complement]]"
  - "[[Sequence Homology]]"
related:
  - "[[Sequence Alignment]]"
  - "[[Dynamic Programming]]"
  - "[[Indel]]"
  - "[[Structural Variant]]"
  - "[[Genome Rearrangement]]"
  - "[[Whole-Genome Alignment]]"
  - "[[Low-Complexity Region]]"
  - "[[RNA Secondary Structure]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-visualization]]"
sources:
  - "[[Gibbs 1970 - The Diagram, a Method for Comparing Sequences]]"
  - "[[Needleman 1970 - Search for Similarities in Amino Acid Sequences]]"
---

# Dot Plot

> [!abstract]
> A dot plot puts one sequence along each axis of a grid and marks every cell where they match: shared segments appear as diagonal lines, so repeats, insertions, deletions and inversions can be read by eye before any alignment is computed.

## Definition

A **dot plot** (dot matrix) of sequences $s$ and $t$ is a matrix with the positions of $s$ on one axis and those of $t$ on the other, with a dot in cell $(i, j)$ when $s_i$ matches $t_j$, or, in the filtered version, when the windows or [[K-mer|k-mers]] starting there match. It was introduced by Gibbs and McIntyre in 1970 as "the diagram", and used from the start to measure similarity between proteins (25 cytochromes), to detect repetitions within protein sequences, and to detect regions of possible base pairing in nucleic acids.[^gibbs]

## Why it matters

- **A first look without assumptions.** A dot plot needs no scoring matrix, no gap penalty and no choice between global and local alignment; it shows **all** similar regions at once, including ones an alignment would discard.
- **Structure of the relationship.** Whether two sequences are collinear, share only a domain, contain internal repeats or differ by an inversion is visible at a glance, which guides the choice of [[Sequence Alignment|alignment]] mode (global, local, several local hits).
- **From genes to genomes.** The same picture, with k-mer or anchor matches as dots, compares whole chromosomes and reveals rearrangements ([[Whole-Genome Alignment]], [[Genome Rearrangement]], [[Structural Variant]]).
- **Lab.** A dot plot viewer, with forward and reverse-complement dots, belongs to [[bio-visualization]]; its k-mer engine reuses [[01-dna-engine]].

## Core (L1)

**Building one.** Write $t$ across the top and $s$ down the side. Put a dot where the letters (or the k-mers starting there) are equal. With position $i$ increasing downward and $j$ to the right, a stretch where $s$ and $t$ agree draws a line from top-left to bottom-right.

![[dot-plot-patterns.svg]]

**Reading the patterns** (figure panels, computed from invented sequences):

| Pattern | Meaning |
|---|---|
| a. one long diagonal | the sequences are collinear over that stretch |
| b. off-diagonal segments in a self-plot | an internal repeat; a self-plot is symmetric about the main diagonal |
| c. diagonal broken and shifted sideways | an insertion or deletion ([[Indel]]); the shift equals its length |
| d. anti-diagonal segment of reverse-complement dots | an inversion: that part of $t$ matches $s$ on the other strand |
| many scattered isolated dots | random matches (noise) |
| dense blocks | low-complexity or tandemly repeated sequence ([[Low-Complexity Region]]) |

**Noise.** With single-base matching of DNA, a random cell is a dot with probability about 1/4, so a quarter of the plot is covered by noise; real signal must be separated from it (Deeper).

## Deeper (L2)

**Filtering.** Two classic ways to remove random dots:

1. **Window and threshold.** Put a dot at $(i, j)$ only if the windows of length $w$ starting at $s_i$ and $t_j$ agree in at least $m$ positions. For DNA with $w = 10$, $m = 7$, a random cell passes with probability $P(\mathrm{Bin}(10, 1/4) \ge 7) \approx 0.0035$ instead of 0.25 (Exercise 3). For proteins, "agree" can mean a positive substitution score ([[Substitution Matrix]]).
2. **Exact k-mers.** Dot only when the k-mers are identical: random density $4^{-k}$, about $2.4 \times 10^{-4}$ for $k = 6$. The figure uses $k = 6$.

Larger windows clean the plot but erase short or diverged similarities and blur the ends of segments: the same sensitivity versus noise trade-off as in any search.

**Both strands.** For DNA, also mark cells where the k-mer of $t$ is the [[Reverse Complement]] of that of $s$ (orange in the figure). An inversion is invisible in a forward-only plot: it appears only as a gap in the diagonal.

**Self-comparison.** Plotting $s$ against itself shows repeats as off-diagonal lines. Plotting $s$ against $\mathrm{rc}(s)$, or marking reverse-complement dots in a self-plot, shows **inverted repeats**, the pairs of segments that can base-pair into stems ([[RNA Secondary Structure]]), which is one of the uses Gibbs and McIntyre had in mind.[^gibbs]

**Cost.** The full matrix has $|s| \times |t|$ cells: $O(nm)$ time and memory if stored. Hashing the k-mers of $t$ and looking up each k-mer of $s$ ([[Hash Table]], [[Inverted Index]]) costs $O(n + m + D)$ for $D$ dots, which is how genome-scale plots are made.

## Advanced (L3)

- **From picture to optimization.** An alignment of $s$ and $t$ is a path through this same matrix from the top-left to the bottom-right corner, moving diagonally (align two letters), right or down (a gap in one sequence). Needleman and Wunsch filled such a matrix with partial scores and traced back the best path,[^nw] turning the dot plot's visual search into [[Dynamic Programming]] ([[Sequence Alignment]], [[Needleman-Wunsch Algorithm]]).
- **Local alignments are diagonal runs.** Each diagonal segment of a filtered dot plot is roughly an ungapped local alignment; chaining segments that lie in order is what seed-and-extend and whole-genome aligners do with anchors ([[Seed and Extend]], [[Whole-Genome Alignment]]).
- **Limits.** A dot plot has no score and no significance: it cannot tell whether a faint diagonal is homology or chance ([[Sequence Homology]], [[E-Value]]). At genome scale one pixel covers thousands of bases, so small events vanish, and repeats (such as [[Transposable Element|transposable elements]]) fill the plot with off-diagonal dots that must be masked ([[Repeat Masking]]).

## Mathematical representation

- **Raw dot matrix** $D \in \{0, 1\}^{n \times m}$, $D_{ij} = \mathbb{1}[s_i = t_j]$, for $|s| = n$, $|t| = m$.
- **k-mer dot matrix** $D^{(k)}_{ij} = \mathbb{1}[s_{i+1..i+k} = t_{j+1..j+k}]$ (0-based starts), and the reverse-complement matrix $R^{(k)}_{ij} = \mathbb{1}[s_{i+1..i+k} = \mathrm{rc}(t_{j+1..j+k})]$.
- **Window filter** $D^{(w, m_0)}_{ij} = \mathbb{1}\big[\sum_{l=1}^{w} \mathbb{1}[s_{i+l} = t_{j+l}] \ge m_0\big]$.
- **Diagonals.** A shared segment of length $L$ is a run of $L - k + 1$ ones along a diagonal $j - i = d$. An insertion of $g$ bases in $t$ moves the run from diagonal $d$ to $d + g$ (a deletion to $d - g$). An inverted segment gives ones of $R^{(k)}$ along an anti-diagonal $i + j = \text{const}$.
- **Noise.** Under independent bases with frequencies $p_a$, $P(D_{ij} = 1) = \sum_a p_a^2$ ($= 1/4$ for uniform DNA) and $P(D^{(k)}_{ij} = 1) = \big(\sum_a p_a^2\big)^k$; the expected number of random dots is $nm$ times that.

## Computational representation

```python
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def reverse_complement(s: str) -> str:
    return s.translate(COMPLEMENT)[::-1]


def dot_plot(s: str, t: str, k: int) -> list[list[str]]:
    """cell [i][j] = '\\' if the k-mers starting at s[i] and t[j] are equal,
    '/' if the k-mer of t is the reverse complement of that of s, '.' otherwise."""
    index: dict[str, list[int]] = {}
    for j in range(len(t) - k + 1):                     # hash the k-mers of t once
        index.setdefault(t[j:j + k], []).append(j)
    grid = [["." for _ in range(len(t) - k + 1)] for _ in range(len(s) - k + 1)]
    for i in range(len(s) - k + 1):
        kmer = s[i:i + k]
        for j in index.get(kmer, []):
            grid[i][j] = "\\"
        for j in index.get(reverse_complement(kmer), []):
            if grid[i][j] == ".":
                grid[i][j] = "/"
    return grid


s = "ACGGTCATTGCAGTTCCGATAGCATGACTG"          # invented toy sequence (30 nt)
t = s[:10] + reverse_complement(s[10:20]) + s[20:]  # same sequence with positions 10-19 inverted
k = 4
print("   " + t[:len(t) - k + 1])
for i, row in enumerate(dot_plot(s, t, k)):
    print(s[i] + "  " + "".join(row))
```

```text
   ACGGTCATTGATCGGAACTGAGCATGA
A  \..........................
C  .\.........................
G  ..\........................
G  ...\..................../..
T  ....\................../...
C  .....\.....................
A  ......\....................
T  ...........................
T  ...........................
G  ...........................
C  ................/........./
A  .............../...........
G  ............../............
T  ............./.............
T  ............/..............
C  .........../...............
C  ........../................
G  ...........................
A  ...........................
T  ...........................
A  ....................\......
G  .....................\.....
C  ......................\....
A  ..../..................\...
T  .../....................\..
G  .........................\.
A  ................\.........\
```

## Worked example

> [!example] Reading the plot above
> 1. **Rows 0 to 6**: a forward diagonal on $j = i$: the first part of $s$ and $t$ is collinear.
> 2. **Rows 7 to 9 are empty**: every 4-mer starting there overlaps the breakpoint at position 10, so it exists in neither orientation in $t$. A breakpoint erases up to $k - 1$ rows of dots.
> 3. **Rows 10 to 16**: reverse-complement dots on the anti-diagonal $i + j = 26$, from $(10, 16)$ to $(16, 10)$. Adding the $k - 1 = 3$ bases of the last k-mer, $s[10{:}20]$ matches the reverse complement of $t[10{:}20]$: an inversion of positions 10 to 19.
> 4. **Rows 20 to 26**: the forward diagonal resumes on $j = i$, so the inversion did not change the length.
> 5. **Isolated dots** at rows 3, 4, 23, 24 and 26 are short chance matches, such as `GTCA`, whose reverse complement `TGAC` also occurs: noise that a larger $k$ would remove.

## Common misconceptions

> [!warning] "Every dot marks a homologous position"
> With single letters, a quarter of all DNA cells are dots by chance. Only runs of dots along diagonals, longer than expected by chance, suggest shared ancestry.

> [!warning] "An inversion shows up as a reversed diagonal in any dot plot"
> Reversing a segment of DNA inverts it **and** swaps the strand. In a forward-only plot an inversion is just a gap; it appears as an anti-diagonal only when reverse-complement matches are plotted.

> [!warning] "A dot plot gives the alignment"
> It shows candidate matching regions; choosing one consistent path, scoring it and judging its significance is the job of [[Sequence Alignment]].

## Exercises

> [!question] Exercise 1 (L1)
> Draw by hand the single-letter dot plot of $s$ = `GATTA` (rows) against $t$ = `ATTAG` (columns). What does the longest diagonal mean?

> [!success]- Solution
> Dots where letters are equal. The run (1,0), (2,1), (3,2), (4,3), in 0-based (row, column) coordinates, is a diagonal $j = i - 1$ of length 4: `ATTA` is shared, shifted by one position (the leading G of $s$ is missing in $t$, and $t$ has an extra G at its end). Other dots, such as (0, 4) for G/G or (1, 3) for A/A, are isolated.

> [!question] Exercise 2 (L1)
> Describe the dot plot of a sequence against itself if the sequence is `ACACACACACAC`, and explain why such regions are masked before searches.

> [!success]- Solution
> Every A matches every A and every C every C: a checkerboard of dots on all diagonals with even offset, that is, parallel lines every 2 positions. Such low-complexity sequence matches everything similar and floods plots and searches with meaningless hits ([[Low-Complexity Region]]).

> [!question] Exercise 3 (L2)
> For random DNA with uniform bases, compute the probability that a cell passes a window filter with $w = 10$, $m = 7$, and the expected number of random dots in a 1000 × 1000 plot for this filter, for single letters and for exact 6-mers.

> [!success]- Solution
> $P(\mathrm{Bin}(10, 0.25) \ge 7) = \sum_{x=7}^{10} \binom{10}{x} 0.25^x 0.75^{10-x} \approx 0.0035$, about 3,500 dots in $10^6$ cells. Single letters: $0.25 \times 10^6 = 250{,}000$ dots. Exact 6-mers: $4^{-6} \times 10^6 \approx 244$ dots.

> [!question] Exercise 4 (L2, Python)
> Write `diagonal_runs(s, t, k, min_kmers)` returning maximal runs of shared k-mers along diagonals, as (start in $s$, start in $t$, length in bases). Use it on a self-comparison to locate the repeat in `GATTACACCGTTAGCATTTTGGCCCGTTAGCATAAC`.

> [!success]- Solution
> ```python
> def diagonal_runs(s: str, t: str, k: int, min_kmers: int) -> list[tuple[int, int, int]]:
>     """Maximal runs of consecutive shared k-mers along diagonals (j - i constant):
>     (start in s, start in t, length in bases), excluding the main diagonal of a self-comparison."""
>     runs = []
>     for d in range(-(len(s) - k), len(t) - k + 1):          # diagonal index d = j - i
>         i, run = max(0, -d), 0
>         while i + d <= len(t) - k and i <= len(s) - k:
>             if s[i:i + k] == t[i + d:i + d + k]:
>                 run += 1
>             else:
>                 if run >= min_kmers:
>                     runs.append((i - run, i - run + d, run + k - 1))
>                 run = 0
>             i += 1
>         if run >= min_kmers:
>             runs.append((i - run, i - run + d, run + k - 1))
>     return [r for r in runs if not (s is t and r[0] == r[1])]
>
>
> s = "GATTACACCGTTAGCATTTTGGCCCGTTAGCATAAC"   # invented: CCGTTAGCAT occurs twice
> print(diagonal_runs(s, s, k=5, min_kmers=3))
> ```
> Output: `[(23, 7, 10), (7, 23, 10)]`. The 10-nt repeat `CCGTTAGCAT` starts at positions 7 and 23; it appears twice because a self-plot is symmetric. Diagonal runs are the ungapped seeds that alignment programs then extend.

> [!question] Exercise 5 (L3)
> In the computed plot of the Computational representation, suppose $t$ had instead lost positions 10 to 19 (a deletion). Describe the plot and give the diagonal indices $d = j - i$ of the two segments.

> [!success]- Solution
> $t$ would have 20 bases. Rows 0 to 6 would keep dots on $d = 0$; rows for positions 10 to 19 of $s$ would have no partner; rows from 20 onward would match $t$ at $j = i - 10$, a diagonal with $d = -10$. The plot shows two collinear segments offset sideways by the deletion length, with no reverse-complement segment: panel c of the figure, not panel d.

## Mastery checklist

- [ ] 1 Recognized: I can say what a dot plot shows and who introduced it.
- [ ] 2 Understood: I can read diagonals, off-diagonal repeats, indel shifts and inversions, and explain dot-plot noise.
- [ ] 3 Practiced: I can compute filtered dot plots with k-mer hashing on both strands and extract diagonal runs.
- [ ] 4 Applied: in [[bio-visualization]], I plotted two real related genomes or genes and identified a rearrangement or repeat.
- [ ] 5 Explained: I can relate dot plots to alignment paths, seeds and whole-genome anchors, and state their limits (no score, resolution, repeats).

## References

[^gibbs]: [[Gibbs 1970 - The Diagram, a Method for Comparing Sequences]], *European Journal of Biochemistry*, abstract.
[^nw]: [[Needleman 1970 - Search for Similarities in Amino Acid Sequences]], *Journal of Molecular Biology*.
