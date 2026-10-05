---
aliases:
  - Coordinate System
  - 0-based Coordinates
  - 1-based Coordinates
  - Half-Open Interval
  - Interbase Coordinates
  - Système de coordonnées génomiques
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Reference Genome]]"
  - "[[String]]"
  - "[[DNA]]"
related:
  - "[[BED Format]]"
  - "[[GFF Format]]"
  - "[[SAM Format]]"
  - "[[VCF Format]]"
  - "[[Genomic Interval Arithmetic]]"
  - "[[Interval Tree]]"
  - "[[Reverse Complement]]"
  - "[[Genome Browser]]"
projects:
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
  - "[[03-genome-diff]]"
  - "[[bio-core]]"
sources:
  - "[[GA4GH hts-specs]]"
  - "[[UCSC Genome Browser]]"
  - "[[Sequence Ontology GFF3 Specification]]"
  - "[[Ensembl]]"
  - "[[Integrative Genomics Viewer]]"
---

# Genomic Coordinate System

> [!abstract]
> Genomic files number positions in two ways: 1-based closed (count the bases, include both ends) or 0-based half-open (count the boundaries between bases, exclude the end); converting between them changes only the start, by one.

## Definition

A **genomic coordinate** locates a base or an interval on a named sequence of a [[Reference Genome]]. Two conventions coexist:[^samterm]

- **1-based, closed** $[s, e]$: the first base is 1 and both ends are included. The bases from the 3rd to the 7th are $[3, 7]$. Used by SAM, VCF, GFF and Wiggle.
- **0-based, half-open** $[s, e)$: the first base is 0, the start is included and the end is not. The same bases are $[2, 7)$. Used by BAM, BCF, BED and PSL.

The 0-based convention is also called "0-start, half-open" or interbase, because its numbers can be read as the boundaries between bases; the 1-based one is "1-start, fully closed".[^ucscblog]

## Why it matters

- **Off-by-one bugs are silent.** A BED interval read as if it were 1-based is shifted by one base: every sequence extracted, every overlap computed, every variant annotated is wrong, and nothing crashes.
- **Formats disagree, and so do layers of one tool.** The UCSC Genome Browser stores 0-based half-open coordinates in its tables and displays 1-based coordinates on the web page; SAM text is 1-based while its binary form BAM stores the same position minus one.[^ucscblog][^sampos]
- **Programs are 0-based.** Python strings and lists use 0-based half-open slices, so `seq[s:e]` is BED-shaped: converting at input, once, is the robust design for [[bio-core]], [[03-genome-diff]] and [[09-genome-browser]].
- **Interval operations depend on it.** Overlap, adjacency, length and merging ([[Genomic Interval Arithmetic]], [[Interval Tree]]) have simpler formulas in half-open form.

## Core (L1)

![[genomic-coordinate-systems.svg]]

**Bases versus boundaries.** In the 1-based system the numbers sit *on* the bases. In the 0-based half-open system they sit *between* the bases: boundary 0 is before the first base, boundary $N$ after the last. The BED specification's own example: in `ACTGCG`, the interval $[2, 4)$ is `TG`.[^bed] In 1-based closed notation the same bases are $[3, 4]$.

**The conversion rule.** Only the start changes:

| From | To | Start | End | Length |
|---|---|---|---|---|
| 1-based closed $[s, e]$ | 0-based half-open | $s - 1$ | $e$ | $e - s + 1$ |
| 0-based half-open $[s, e)$ | 1-based closed | $s + 1$ | $e$ | $e - s$ |

A single base at 1-based position $p$ is $[p - 1, p)$ in 0-based form. The UCSC FAQ's example: the first 100 bases of chromosome 1 are the BED line `1 0 100` and the position `chr1:1-100`.[^ucscfmt]

**Who uses what.**

| Convention | Formats and places |
|---|---|
| 1-based closed | SAM `POS`, VCF `POS`, GFF3 and GTF `start`/`end`, Wiggle, UCSC position notation (`chr1:1-100`)[^samterm][^vcf][^gff3][^ensembl][^ucsctrack] |
| 0-based half-open | BED, BAM (binary `pos`), BCF, PSL, UCSC database tables, Python slices[^samterm][^sampos][^bed][^ucscblog] |

FASTA has no coordinates in the file: positions are implied by order ([[FASTA Format]]).

**Strand does not change the numbering.** Coordinates are always counted along the reference sequence as stored (the `+` strand), with start ≤ end; the strand is a separate column. For a `-` strand feature the 5' end is the *larger* coordinate: the GFF3 specification defines the 5' end of a minus-strand CDS as its `end`.[^gff3][^bed]

## Deeper (L2)

**Why half-open intervals are convenient.** For $[a, b)$:

- the length is $b - a$, without "+1";
- two intervals are adjacent exactly when $b_1 = a_2$, and splitting $[a, b)$ at $m$ gives $[a, m)$ and $[m, b)$ with no shared or lost base;
- the empty interval $[a, a)$ exists and names a *point between bases*, which is what an insertion site is.

In closed form the same statements need $\pm 1$ corrections, which is where bugs come from.

**Zero-length features.** Each format encodes "between two bases" differently:[^bed][^ucscfmt][^gff3][^vcf]

- BED: `chromStart = chromEnd`, a feature between `chromStart` and the preceding base (`0 0` is before the first base).
- GFF3: `start = end` for a zero-length feature, the site lying to the right of the indicated base.
- VCF has no empty interval: an insertion or deletion includes the base *before* the event as a padding base, reflected in `POS` (the base after, if the event is at position 1); telomeres are written as positions 0 or $N + 1$.

**Overlap tests.** Half-open: $[a_1, b_1)$ and $[a_2, b_2)$ overlap iff $a_1 < b_2$ and $a_2 < b_1$. Closed: $[s_1, e_1]$ and $[s_2, e_2]$ overlap iff $s_1 \le e_2$ and $s_2 \le e_1$. Mixing the two tests, or mixing conventions between the two intervals, reports adjacent features as overlapping (Exercise 4).

**Display versus storage.** The UCSC browser shows 1-based positions: the browser line `browser position chr22:1-20000` displays the first 20,000 bases.[^ucsctrack] IGV's documentation states the difference between file conventions with one example: `1-2` means the first two bases in a 1-based format (SAM) but only the second base in BED.[^igv]

## Advanced (L3)

**Reverse-strand coordinates.** On a sequence of length $N$, the bases $[s, e)$ of the forward strand occupy $[N - e, N - s)$ on the reverse complement (read 5' → 3'); in closed form $[s, e] \mapsto [N - e + 1, N - s + 1]$. A tool that searches the reverse complement, such as the ORF finder of [[Genetic Code]], converts its hits back with this formula. SAM follows the same rule: a read aligned to the reverse strand is stored reverse-complemented and located by its leftmost position on the forward strand.[^sampos]

**Transcript coordinates.** A spliced transcript defines its own 1-based axis, from its 5' end, through its exons only. Converting a transcript position to the genome walks the exons in transcript order (descending genomic order on the `-` strand). GFF3 defines transcript-relative alignments on this axis.[^gff3] Exercise 5 implements the conversion (see also [[Variant Nomenclature]]).

**Circular sequences.** Linear intervals cannot express a feature that crosses the origin of a plasmid, a mitochondrion or a bacterial chromosome. GFF3 keeps start ≤ end by writing `end = end position + landmark length`: gene II of phage f1 (landmark length 6,407) is `6006 7238`, meaning 6,006 to 6,407 then 1 to 831.[^gff3] SAM uses the same idea: on a circular reference of length `LN`, 1-based position $p > $ `LN` is read as $((p - 1) \bmod \mathrm{LN}) + 1$.[^sampos]

**Indexes are half-open.** The binning scheme of BAM indexes computes bins for 0-based half-open intervals $[beg, end)$,[^sampos] so 1-based positions are converted before indexing ([[Genomic File Indexing]]).

## Mathematical representation

Let the bases of a sequence of length $N$ be numbered $1, \dots, N$ (1-based). An interval is a set of consecutive bases $B = \{s, s + 1, \dots, e\}$.

- **Closed form:** $B = [s, e] \cap \mathbb{Z}$, with $1 \le s \le e \le N$ and $|B| = e - s + 1$.
- **Half-open form:** boundaries are numbered $0, \dots, N$, base $i$ lying between boundaries $i - 1$ and $i$. Then $B = \{a + 1, \dots, b\}$ is written $[a, b)$, with $0 \le a \le b \le N$ and $|B| = b - a$; $a = b$ is the empty set, located at boundary $a$.
- **Conversion** is the bijection $\phi(s, e) = (s - 1, e)$ on non-empty intervals; its inverse is $\phi^{-1}(a, b) = (a + 1, b)$.
- **Intersection** of $[a_1, b_1)$ and $[a_2, b_2)$ is $[\max(a_1, a_2), \min(b_1, b_2))$, non-empty iff $\max(a_1, a_2) < \min(b_1, b_2)$.
- **Reverse complement:** $\rho_N([a, b)) = [N - b, N - a)$, an involution ($\rho_N \circ \rho_N = \mathrm{id}$) that preserves length.

## Computational representation

Store one convention internally (0-based half-open, because it matches Python) and convert at the edges of the program, when reading and writing each format.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Interval:
    """A genomic interval stored ONE way: 0-based, half-open [start, end)."""
    chrom: str
    start: int
    end: int

    def __post_init__(self):
        if not 0 <= self.start <= self.end:
            raise ValueError(f"need 0 <= start <= end, got {self.start}, {self.end}")

    @classmethod
    def from_one_based(cls, chrom: str, first: int, last: int) -> "Interval":
        """From 1-based closed [first, last] (GFF, VCF, SAM, 'chr1:1-100')."""
        return cls(chrom, first - 1, last)

    def to_one_based(self) -> tuple[str, int, int]:
        return self.chrom, self.start + 1, self.end

    def __len__(self) -> int:
        return self.end - self.start

    def overlaps(self, other: "Interval") -> bool:
        return self.chrom == other.chrom and self.start < other.end and other.start < self.end

    def on_reverse(self, chrom_length: int) -> "Interval":
        """The same bases, counted on the reverse complement of the chromosome."""
        return Interval(self.chrom, chrom_length - self.end, chrom_length - self.start)

seq = "ACTGCG"                                 # example sequence of the BED specification
bed = Interval("toy", 2, 4)                    # BED-style [2, 4)
print(seq[bed.start:bed.end], len(bed), bed.to_one_based())
gff = Interval.from_one_based("toy", 3, 4)     # GFF-style [3, 4]
print(gff == bed)
print(Interval("chr1", 0, 100).to_one_based())           # UCSC FAQ: chr1:1-100
a, b, c = Interval("c", 10, 20), Interval("c", 20, 30), Interval("c", 19, 21)
print(a.overlaps(b), a.overlaps(c), len(Interval("c", 5, 5)))
rc = "".join({"A": "T", "C": "G", "G": "C", "T": "A"}[x] for x in reversed(seq))
r = Interval("toy", 1, 4).on_reverse(len(seq))
print(seq[1:4], rc, r, rc[r.start:r.end])
```

Output:

```text
TG 2 ('toy', 3, 4)
True
('chr1', 1, 100)
False True 0
CTG CGCAGT Interval(chrom='toy', start=2, end=5) CAG
```

`[10, 20)` and `[20, 30)` touch but do not overlap; `[5, 5)` is a valid empty interval (an insertion point); `CTG` at $[1, 4)$ reappears as its reverse complement `CAG` at $[2, 5)$ of the reverse strand.

## Worked example

> [!example] One sequence, three variants, three formats
> Toy sequence (invented), with 1-based positions: `A1 C2 G3 T4 A5 C6 G7 T8`.
>
> | Event | BED (0-based half-open) | GFF3 (1-based closed) | VCF (1-based, padded) |
> |---|---|---|---|
> | SNV at base 7, G → A | `toy 6 7` | `7 7` | `POS=7 REF=G ALT=A` |
> | Deletion of bases 5-6 (`AC`) | `toy 4 6` | `5 6` | `POS=4 REF=TAC ALT=T` |
> | Insertion of `TT` after base 4 | `toy 4 4` | `4 4`, zero-length | `POS=4 REF=T ALT=TTT` |
>
> 1. **SNV:** one base; BED start = 7 − 1.
> 2. **Deletion:** BED and GFF3 describe the deleted bases; in Python `seq[4:6] == "AC"`. VCF cannot have an empty ALT, so it adds the padding base T at position 4 to both alleles.[^vcf]
> 3. **Insertion:** there is no inserted base in the reference, so BED writes the empty interval at boundary 4 (between T4 and A5),[^bed] GFF3 writes `start = end = 4` (the site to the right of base 4),[^gff3] and VCF again anchors on base 4.
> 4. **Check:** inserting `TT` into the sequence at Python index 4 gives `ACGTTTACGT`, the ALT haplotype of all three rows.

## Common misconceptions

> [!warning] "0-based means both numbers are one lower"
> Only the start changes: 1-based $[3, 4]$ is 0-based $[2, 4)$. Subtracting 1 from the end too silently drops the last base of every feature.

> [!warning] "Converting BED to GFF means adding 1 to both coordinates"
> Same error in the other direction: add 1 to the start, keep the end. The UCSC example `chr1 0 100` is `chr1:1-100`, not `chr1:1-101`.[^ucscfmt]

> [!warning] "A minus-strand feature has start greater than end"
> In BED, GFF3, SAM and VCF, start ≤ end always; the strand is a separate field. Only the biology is reversed: the 5' end of a `-` strand feature is its end coordinate.[^gff3][^bed]

> [!warning] "The browser shows the numbers stored in my file"
> Browsers display 1-based positions; a BED file is 0-based. The same feature appears with a start one higher on screen than in the file.[^ucscblog][^ucscfmt]

## Exercises

> [!question] Exercise 1 (L1)
> The UCSC FAQ example BED line `chr7 127471196 127472363 Pos1 0 +` describes which 1-based range? How many bases does it cover?

> [!success]- Solution
> Start + 1, same end: `chr7:127471197-127472363`. Length $127{,}472{,}363 - 127{,}471{,}196 = 1{,}167$ bases (in closed form, $127{,}472{,}363 - 127{,}471{,}197 + 1$, the same).

> [!question] Exercise 2 (L1)
> A VCF record reports a SNV at `chr2` `POS=1000`. Write the BED line and the GFF3 `start`/`end` for this base.

> [!success]- Solution
> BED: `chr2 999 1000`. GFF3: `start = 1000`, `end = 1000`. VCF and GFF3 share the 1-based closed convention; BED subtracts one from the start only.

> [!question] Exercise 3 (L2, Python)
> A GFF3 feature has `start = 3`, `end = 4` on the sequence `ACTGCG`. A colleague extracts it with `seq[3:4]`. What do they get, what should they get, and what one-line rule prevents the bug?

> [!success]- Solution
> ```python
> seq = "ACTGCG"
> print(repr(seq[3:4]), repr(seq[2:4]))   # 'G' 'TG'
> ```
>
> They get `G` (one base, shifted); the feature is `TG`. Rule: a 1-based closed `[s, e]` is the Python slice `seq[s - 1:e]`, and the conversion is done once, when the file is parsed.

> [!question] Exercise 4 (L2)
> A GFF3 gene spans `100 200`; a BED peak is `chr1 200 300`. A script tests overlap with `gene_end >= peak_start` and `peak_end >= gene_start` on the raw numbers. What does it report, and what is the truth?

> [!success]- Solution
> The script says they overlap ($200 \ge 200$). Convert the gene to half-open: $[99, 200)$. The peak is $[200, 300)$. Test $99 < 300$ and $200 < 200$: the second is false, so they do not overlap; they are adjacent (the gene ends at base 200, the peak starts at base 201). The bug comes from applying a closed-interval test to one closed and one half-open interval.

> [!question] Exercise 5 (L3, Python)
> An invented minus-strand transcript has exons (1-based, closed) at 101-150, 201-260 and 301-330. Write a function mapping a 1-based transcript position to its genomic position, and give the genomic positions of transcript positions 1, 30, 31, 90, 91 and 140.

> [!success]- Solution
> On the `-` strand the transcript starts at the highest coordinate, so the exons are walked in descending order and positions are counted down within each exon.
>
> ```python
> def transcript_to_genome(t: int, exons: list[tuple[int, int]], strand: str) -> int:
>     """1-based transcript position -> 1-based genomic position.
>     exons: 1-based closed genomic intervals, in any order."""
>     ordered = sorted(exons, reverse=(strand == "-"))
>     offset = t
>     for first, last in ordered:
>         size = last - first + 1
>         if offset <= size:
>             return first + offset - 1 if strand == "+" else last - offset + 1
>         offset -= size
>     raise ValueError("position beyond the transcript end")
>
> exons = [(101, 150), (201, 260), (301, 330)]
> print([transcript_to_genome(t, exons, "-") for t in (1, 30, 31, 90, 91, 140)])
> # [330, 301, 260, 201, 150, 101]
> ```
>
> The transcript has $30 + 60 + 50 = 140$ nt; its first base is genomic 330 and its last is 101. Each exon boundary (30/31, 90/91) jumps over an intron.

> [!question] Exercise 6 (L3)
> In the GFF3 specification, phage f1 has a circular landmark of length 6,407 and gene II is written `6006 7238`. Which genomic bases does it cover, and how long is it? Why does GFF3 not simply write `6006 831`?

> [!success]- Solution
> $7238 - 6407 = 831$, so the gene covers 6,006-6,407 (402 bp) then 1-831 (831 bp): 1,233 bp, equal to $7238 - 6006 + 1$. Writing `6006 831` would break the rule start ≤ end that every parser and index relies on; adding the landmark length keeps intervals linear while the `Is_circular` attribute tells tools to wrap.[^gff3]

## Mastery checklist

- [ ] 1 Recognized: I can say which formats are 0-based half-open and which are 1-based closed.
- [ ] 2 Understood: I can explain the conversion rule, why only the start changes, and how each format writes a zero-length feature.
- [ ] 3 Practiced: I can implement an interval type with conversions, overlap and reverse-strand mapping, and solved the exercises.
- [ ] 4 Applied: in [[09-genome-browser]] or [[03-genome-diff]], every parser converts to one internal convention and my tests cover adjacent intervals and insertions.
- [ ] 5 Explained: I can teach the conventions with the insertion example, including circular sequences and transcript coordinates.

## References

[^samterm]: [[GA4GH hts-specs]], `SAMv1`, "Terminology": 1-based and 0-based coordinate systems and the formats using each.
[^sampos]: [[GA4GH hts-specs]], `SAMv1`: `POS` (1-based leftmost position), reverse-strand `SEQ`, BAM `pos` (0-based, `POS` − 1), circular references (`LN`), and BAI bin computation on 0-based half-open intervals.
[^bed]: [[GA4GH hts-specs]], `BEDv1`, "Terminology and concepts" (0-based, half-open; `ACTGCG` example), `chromStart` and `chromEnd`, and `strand`.
[^vcf]: [[GA4GH hts-specs]], `VCFv4.5`, fixed fields: `POS` (1st base is 1, telomeres at 0 or N+1) and padding base for insertions and deletions.
[^ucscfmt]: [[UCSC Genome Browser]], FAQ "Data File Formats", BED format (`chromStart`, `chromEnd`, the chr1:1-100 example, insertions).
[^ucscblog]: [[UCSC Genome Browser]], blog post "The UCSC Genome Browser Coordinate Counting Systems" (2016).
[^ucsctrack]: [[UCSC Genome Browser]], help page "Displaying Your Own Annotations in the Genome Browser", browser lines (`browser position chr22:1-20000`).
[^gff3]: [[Sequence Ontology GFF3 Specification]], version 1.26: columns 4-5 (1-based, start ≤ end, zero-length features), column 7 (strand), column 8 (5' end of minus-strand CDS), "Circular Genomes", "Transcript-Relative Alignments".
[^ensembl]: [[Ensembl]], help page "GFF/GTF File Format" (start and end numbered from 1).
[^igv]: [[Integrative Genomics Viewer]], desktop documentation, "File Formats" (one-based SAM, zero-based BED, with the `1-2` example).
