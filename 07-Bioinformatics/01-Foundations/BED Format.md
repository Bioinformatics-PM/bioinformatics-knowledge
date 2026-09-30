---
aliases:
  - Browser Extensible Data
  - BED File
  - BED12
  - bed
  - Format BED
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Genomic Coordinate System]]"
  - "[[Reference Genome]]"
  - "[[Delimited Text Format]]"
related:
  - "[[GFF Format]]"
  - "[[Genome Browser]]"
  - "[[Genomic Interval Arithmetic]]"
  - "[[Genomic File Indexing]]"
  - "[[Interval Tree]]"
  - "[[VCF Format]]"
projects:
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[GA4GH hts-specs]]"
  - "[[UCSC Genome Browser]]"
  - "[[Integrative Genomics Viewer]]"
---

# BED Format

> [!abstract]
> BED is the plain-text table of genomic intervals: one feature per line, a chromosome name and a 0-based, half-open start and end, optionally followed by a name, score, strand, a "thick" coding part and exon blocks.

## Definition

**BED** (Browser Extensible Data) is a whitespace-delimited text format in which each data line describes one genomic feature by its position on a linear chromosome: three mandatory fields (`chrom`, `chromStart`, `chromEnd`) and up to nine optional ones.[^spec] It comes from the [[UCSC Genome Browser]], whose format FAQ describes it; GA4GH BED v1.0 (2022) turns that description into a formal specification.[^spec][^ucscfmt] All positions are **0-based, half-open** ([[Genomic Coordinate System]]).[^spec]

## Why it matters

- **The lingua franca of intervals.** Peaks called from [[ChIP-Seq]] data, transcripts, regions to mask or to analyse: any set of features on a genome can be a BED file,[^spec] which is why interval tools ([[Genomic Interval Arithmetic]]) take BED as input.
- **Display.** BED is one of the formats the UCSC browser accepts as a custom track and IGV loads as a feature track; its optional fields exist to control that display.[^ucscct][^igv]
- **Projects.** [[09-genome-browser]] reads BED tracks; [[10-genomic-pipeline]] uses BED to restrict variant calling or coverage to target regions.
- **Its danger is its simplicity.** A BED file carries no header saying which assembly or which fields it uses: that information must travel with the file.[^spec]

## Core (L1)

### Specification (GA4GH BED v1.0)

Each **data line** has between 3 and 12 BED fields, in this order:[^spec][^ucscfmt]

| # | Field | Type | Allowed values | Meaning |
|---:|---|---|---|---|
| 1 | `chrom` | string | `[A-Za-z0-9_]{1,255}` | chromosome or scaffold name (`chr1`, `21`, `chrUn_KI270435v1`) |
| 2 | `chromStart` | integer | $0 \le$ `chromStart` $\le$ chromosome length | start, 0-based, **included** |
| 3 | `chromEnd` | integer | `chromStart` $\le$ `chromEnd` $\le$ chromosome length | end, **excluded** |
| 4 | `name` | string | 1-255 printable characters | label of the feature |
| 5 | `score` | integer | 0 to 1000 | numeric value (UCSC can shade features by it) |
| 6 | `strand` | character | `+`, `-` or `.` | strand; `.` when unknown or irrelevant |
| 7 | `thickStart` | integer | `chromStart` ≤ `thickStart` ≤ `chromEnd` | start of the part drawn thick (e.g. the coding part) |
| 8 | `thickEnd` | integer | `thickStart` ≤ `thickEnd` ≤ `chromEnd` | end of the thick part |
| 9 | `itemRgb` | `R,G,B` or `0` | each 0 to 255 | display colour |
| 10 | `blockCount` | integer | > 0 | number of blocks (e.g. exons) |
| 11 | `blockSizes` | comma list | `blockCount` integers, optional trailing comma | length of each block |
| 12 | `blockStarts` | comma list | `blockCount` integers, relative to `chromStart` | start of each block |

Rules of the file:[^spec]

- **Fields** are separated by one or more spaces or tabs (`[ \t]+`); a single tab throughout is recommended, and a `name` may contain spaces only if the separator is a tab everywhere.
- **Order is binding**: a field can be filled only if all previous ones are. Every line has the same number of fields. A file is called **BED*n*** after its number of fields; **BED10 and BED11 are prohibited** (the three block fields go together).
- **BED*n*+*m***: $n$ standard fields followed by $m$ custom fields (for example BED6+4); which columns are custom is not recorded in the file.
- **Other lines**: comment lines start with `#`, blank lines are allowed anywhere. UCSC `browser` and `track` header lines are allowed only in custom-track files, which are therefore not valid BED.[^spec][^ucscfmt]
- **Zero-length features**: `chromStart = chromEnd` is a point between two bases (an insertion); `0 0` is before the first base.[^spec][^ucscfmt]
- **Out-of-band information**: the genome assembly, the meaning of `score` and of custom fields, and whether the separator is a single tab are *not* in the file and must be documented with it.[^spec]

### Minimal examples

A minimal BED3 file (toy example):

```text
chr1	0	100
chr1	250	300
```

The first line is the first 100 bases of chr1, displayed by a browser as `chr1:1-100`.[^ucscfmt] BED6, three lines of the example in the UCSC FAQ and the BED specification:[^spec]

```text
chr7	127471196	127472363	Pos1	0	+
chr7	127472363	127473530	Pos2	0	+
chr7	127475864	127477031	Neg1	0	-
```

Consecutive features share a boundary (`127472363`) without overlapping: that is the half-open convention at work.

## Deeper (L2)

### BED12: transcripts in one line

![[bed12-feature-anatomy.svg]]

With 12 fields, one line describes a spliced feature. The blocks are the exons; the gaps between them are the introns; the thick part is usually the coding region, and when there is none, UCSC sets `thickStart` and `thickEnd` to `chromStart`.[^ucscfmt] Block constraints:[^spec]

- `blockStarts` are **relative to `chromStart`**; block $i$ spans $[\text{chromStart} + \text{start}_i,\ \text{chromStart} + \text{start}_i + \text{size}_i)$;
- the first block starts at `chromStart` (first `blockStart` = 0) and the last ends at `chromEnd`;
- blocks are sorted and do not overlap.

The specification's check on its own example: `chr22 1000 5000 cloneA 960 + 1000 5000 0 2 567,488, 0,3512` has a last block starting at $1000 + 3512 = 4512$, of size 488, ending at $5000 =$ `chromEnd`.[^spec]

### Custom tracks, extended formats, big files

- **Track lines.** For display, UCSC accepts `browser` lines (initial position, which tracks to show) and a `track` line (name, description, `visibility`, colour, `useScore`, `itemRgb="On"`) before the data.[^ucscct][^ucscfmt] IGV reads a track line for display settings but not several track lines in one BED file.[^igv]
- **Extended formats.** Many formats are BED*n*+*m*: IGV documents ENCODE broadPeak as BED6+3.[^igv] A generic parser must be told $n$.
- **Sorting.** Files should be sorted by `chrom`, then `chromStart`, then `chromEnd` numerically, which `LC_ALL=C sort -k1,1 -k2,2n -k3,3n` does; any chromosome order is acceptable if each chromosome's lines are contiguous.[^spec]
- **Size.** Above about 50 MB, convert a file meant for display to **bigBed**, an indexed binary format from which only the region on screen is transferred, or compress and index it with tabix (which requires tab separators).[^spec][^ucscfmt][^igv] See [[Genomic File Indexing]].

## Advanced (L3)

**A formal specification, late.** BED was used for years from the UCSC web description before GA4GH wrote v1.0. The specification formalizes "reasonable interpretations" of the UCSC text and names the interoperability gaps that remain: which columns are standard, the assembly, the semantics of `score` and of thick and block positions, and the separator are all left to documentation outside the file.[^spec] Consequences for a robust tool: be strict on output (tabs, integer scores, sorted), explicit on input (the caller states $n$ and the assembly), and report violations instead of guessing.

**Strict names versus real names.** BED v1.0 restricts `chrom` to letters, digits and underscore, while the UCSC FAQ accepts aliases such as `NC_000001.11`, which contains a dot.[^spec][^ucscfmt] A strict validator rejects such files; a lenient one should at least flag them.

**What BED cannot say.** One level of structure only: a BED12 line is one transcript, and nothing groups transcripts into genes or says that two lines share an exon. Converting [[GFF Format|GFF3]] to BED12 is lossy (the gene level, attributes and multiple parents disappear); converting back needs a naming convention. BED is the right format for *sets of intervals*; hierarchies belong in GFF3.

## Mathematical representation

A BED file is a finite multiset of records. Record $r$ on chromosome $c_r$ denotes the set of 1-based bases

$$I_r = \{\text{chromStart}_r + 1, \dots, \text{chromEnd}_r\}, \qquad |I_r| = \text{chromEnd}_r - \text{chromStart}_r .$$

For a BED12 record with block starts $b_i$ and sizes $z_i$ ($i = 1, \dots, k$), the covered bases are the disjoint union

$$E_r = \bigcup_{i=1}^{k} \{\text{chromStart}_r + b_i + 1, \dots, \text{chromStart}_r + b_i + z_i\}, \qquad |E_r| = \sum_{i} z_i,$$

with the constraints $b_1 = 0$, $b_k + z_k = \text{chromEnd}_r - \text{chromStart}_r$ and $b_i + z_i \le b_{i+1}$. The thick (coding) bases are $E_r \cap \{\text{thickStart}_r + 1, \dots, \text{thickEnd}_r\}$. Set operations on the $I_r$ (union, intersection, difference) are the subject of [[Genomic Interval Arithmetic]].

## Computational representation

A parser that follows BED v1.0 and handles the edge cases seen in real files: comments, blank lines, `track` and `browser` lines, CRLF line endings, space or tab separators, BED*n*+*m* custom columns, names with spaces (tab-only mode), trailing commas in block lists, and every value constraint of the table above. Standard library only.

```python
import re
from dataclasses import dataclass, field

SEP = re.compile(r"[ \t]+")                          # BEDv1 field separator
CHROM = re.compile(r"[A-Za-z0-9_]{1,255}")
HEADER = re.compile(r"(track|browser)([ \t]|$)")    # UCSC custom-track lines

class BedError(ValueError):
    pass

@dataclass
class BedRecord:
    chrom: str
    start: int                                       # 0-based, included
    end: int                                         # excluded
    name: str | None = None
    score: int | None = None
    strand: str = "."
    thick: tuple[int, int] | None = None
    rgb: tuple[int, ...] | None = None
    blocks: list[tuple[int, int]] = field(default_factory=list)   # absolute [s, e)
    extra: list[str] = field(default_factory=list)               # custom fields (BEDn+m)

def _ints(text: str) -> list[int]:
    return [int(x) for x in text.rstrip(",").split(",")]           # trailing comma allowed

def _check(ok: bool, no: int, message: str) -> None:
    if not ok:
        raise BedError(f"line {no}: {message}")

def parse_bed(lines, n_bed=None, tab_only=False, strict_names=False):
    """Yield BedRecord from BED lines. n_bed: number of standard fields when the
    file is BEDn+m (custom columns follow); by default every column is standard."""
    width = None
    for no, raw in enumerate(lines, 1):
        line = raw.rstrip("\r\n")
        if not line.strip() or line.startswith("#") or HEADER.match(line):
            continue                                 # blank, comment, track/browser line
        f = line.split("\t") if tab_only else SEP.split(line.strip())
        n = n_bed or len(f)
        _check(3 <= n <= 12 and n not in (10, 11) and len(f) >= n, no,
               f"{len(f)} fields, need BED3-BED9 or BED12")
        width = width or len(f)
        _check(len(f) == width, no, f"{len(f)} fields, previous lines had {width}")
        _check(not strict_names or bool(CHROM.fullmatch(f[0])), no, f"chrom {f[0]!r} not allowed")
        try:
            r = BedRecord(f[0], int(f[1]), int(f[2]), extra=f[n:])
            _check(0 <= r.start <= r.end, no, "need 0 <= chromStart <= chromEnd")
            if n >= 4:
                r.name = f[3]
            if n >= 5:
                r.score = int(f[4])
                _check(0 <= r.score <= 1000, no, "score must be an integer in [0, 1000]")
            if n >= 6:
                _check(f[5] in ("+", "-", "."), no, "strand must be +, - or .")
                r.strand = f[5]
            if n >= 7:                               # BED7 alone: the whole feature is thick
                r.thick = (int(f[6]), int(f[7])) if n >= 8 else (r.start, r.end)
                _check(r.start <= r.thick[0] <= r.thick[1] <= r.end, no, "thick part outside feature")
            if n >= 9 and f[8] != "0":
                r.rgb = tuple(_ints(f[8]))
                _check(len(r.rgb) == 3 and all(0 <= v <= 255 for v in r.rgb), no, "bad itemRgb")
            if n == 12:
                count, sizes, starts = int(f[9]), _ints(f[10]), _ints(f[11])
                _check(count >= 1 and len(sizes) == len(starts) == count, no, "bad blockCount")
                r.blocks = [(r.start + s, r.start + s + z) for s, z in zip(starts, sizes)]
                _check(starts[0] == 0 and r.blocks[-1][1] == r.end
                       and all(a[1] <= b[0] for a, b in zip(r.blocks, r.blocks[1:])),
                       no, "blocks must be sorted, disjoint and span the feature")
        except BedError:
            raise
        except ValueError as err:                    # a number that does not parse
            raise BedError(f"line {no}: {err}") from None
        yield r

text = ["# BED12 example of the UCSC FAQ and BEDv1, plus a track line, CRLF, blank line\n",
        "track name=demo\n",
        "chr22 1000 5000 cloneA 960 + 1000 5000 0 2 567,488, 0,3512\n",
        "chr22 2000 6000 cloneB 900 - 2000 6000 0 2 433,399, 0,3601\r\n", "\n"]
for rec in parse_bed(text):
    print(rec.name, rec.strand, rec.end - rec.start, rec.blocks)

for bad in ["chr1 10 5", "chr1 0 10 a 2000", "chr1 0 10 a 0 + 0 10 0 1",
            "chr1 0 10 a 0 + 0 10 0 2 3,3 0,5", "chr1 0 10 my peak", "NC_000001.11 0 10"]:
    try:
        list(parse_bed([bad], strict_names=True))
    except BedError as err:
        print("error:", err)

peaks = ["chr7\t100\t250\tpeak one\t0\t+\t4.1\t3.2\t2.5"]      # BED6+3, name with a space
print(next(parse_bed(peaks, n_bed=6, tab_only=True)))
```

Output:

```text
cloneA + 4000 [(1000, 1567), (4512, 5000)]
cloneB - 4000 [(2000, 2433), (5601, 6000)]
error: line 1: need 0 <= chromStart <= chromEnd
error: line 1: score must be an integer in [0, 1000]
error: line 1: 10 fields, need BED3-BED9 or BED12
error: line 1: blocks must be sorted, disjoint and span the feature
error: line 1: invalid literal for int() with base 10: 'peak'
error: line 1: chrom 'NC_000001.11' not allowed
BedRecord(chrom='chr7', start=100, end=250, name='peak one', score=0, strand='+', thick=None, rgb=None, blocks=[], extra=['4.1', '3.2', '2.5'])
```

BED v1.0 allows any run of spaces and tabs as separator, so the fifth bad line, `chr1 0 10 my peak`, is ambiguous: with whitespace separators the name `my peak` becomes two fields and `peak` lands in the score column. The fix is to write tab-separated files and parse them with `tab_only=True`, as the `peak one` example shows.[^spec]

### Pitfalls

- **Coordinates**: BED is 0-based half-open; add 1 to the start (only) for 1-based display, GFF or VCF ([[Genomic Coordinate System]]).
- **Assembly**: nothing in the file says hg19 or hg38; name it in the file name or accompanying metadata ([[Reference Genome]]).[^spec]
- **Chromosome names**: `chr1` and `1` never match in string comparisons; one file must not mix both.[^spec]
- **Header lines**: `track` and `browser` lines break tools that expect pure BED; UCSC's own converters (bedToBigBed) reject them.[^ucscfmt]
- **Blocks**: `blockStarts` are relative to `chromStart`, not absolute positions.
- **Lexicographic sort**: `chr10` sorts before `chr2` in C-locale order; that is allowed, but two files must use the same order for streaming tools that merge sorted inputs.[^spec]

## Worked example

> [!example] Reading one BED12 line
> `chr22 1000 5000 cloneA 960 + 1000 5000 0 2 567,488, 0,3512` (UCSC FAQ and BED v1.0 example).[^spec]
> 1. **Extent**: `chr22`, $[1000, 5000)$, i.e. 1-based `chr22:1001-5000`, 4,000 bp.
> 2. **Name, score, strand**: `cloneA`, 960, `+`.
> 3. **Thick part**: `1000 5000`, the whole feature. **Colour**: `0`, the default.
> 4. **Blocks**: 2 blocks, sizes 567 and 488, starts 0 and 3512 relative to 1000: $[1000, 1567)$ and $[4512, 5000)$.
> 5. **Checks**: first block starts at `chromStart`; last ends at $4512 + 488 = 5000 =$ `chromEnd`; $1567 \le 4512$, no overlap. Exonic length $567 + 488 = 1{,}055$ bp; the gap $[1567, 4512)$ is 2,945 bp.

## Common misconceptions

> [!warning] "To convert BED to 1-based, subtract 1 from chromEnd too"
> Only the start changes. `chromEnd` is excluded in 0-based counting, and the same number is the last base in 1-based counting: `chr1 0 100` is `chr1:1-100`, 100 bases.[^ucscfmt] Subtracting 1 from the end silently drops the last base of every feature.

> [!warning] "A BED file with a track line is a BED file"
> Track and browser lines belong to UCSC custom-track files; the BED specification excludes them and converters reject them.[^spec][^ucscfmt]

> [!warning] "The score is any number"
> In BED it is an integer from 0 to 1000; a p-value or a float belongs in a custom field of a BED*n*+*m* format with its meaning documented.[^spec]

## Exercises

> [!question] Exercise 1 (L1)
> Write the BED6 line for a feature `peak1` on the minus strand covering the 1-based range `chr2:1001-1500`, with no meaningful score.

> [!success]- Solution
> `chr2	1000	1500	peak1	0	-`. Start minus one, same end; an uninformative score is written `0` in BED6+ files.[^spec] Length check: $1500 - 1000 = 500 = 1500 - 1001 + 1$.

> [!question] Exercise 2 (L1)
> Which of these lines are invalid in BED v1.0, and why? (a) `chr1 100 50` (b) `chr1 0 100 a 1200` (c) `chr1 0 100 a 0 + 0 100 0 1` (d) `track name=peaks` (e) `chr1 0 0 ins1`

> [!success]- Solution
> (a) invalid: `chromEnd` < `chromStart`. (b) invalid: score above 1000. (c) invalid: 10 fields, and BED10 is prohibited. (d) not a data line: allowed only in UCSC custom-track files, not in BED. (e) valid: a zero-length feature before the first base, such as an insertion.[^spec][^ucscfmt]

> [!question] Exercise 3 (L2, Python)
> With `parse_bed`, compute the exonic length and the intron intervals (0-based) of `cloneA`.

> [!success]- Solution
> ```python
> line = "chr22 1000 5000 cloneA 960 + 1000 5000 0 2 567,488, 0,3512"
> rec = next(parse_bed([line]))
> exonic = sum(e - s for s, e in rec.blocks)
> introns = [(a[1], b[0]) for a, b in zip(rec.blocks, rec.blocks[1:])]
> print(exonic, introns, [e - s for s, e in introns])
> # 1055 [(1567, 4512)] [2945]
> ```
>
> Half-open intervals make both steps free of $\pm 1$: an intron is the gap from one block's end to the next block's start.

> [!question] Exercise 4 (L3, Python)
> Write a function turning a parsed BED12 record into GFF3 `exon` lines (1-based, closed), and apply it to `chr22 2000 6000 cloneB 900 - 2000 6000 0 2 433,399, 0,3601`. What information would a full GFF3 gene model need that BED12 does not provide?

> [!success]- Solution
> ```python
> def bed12_to_gff3_exons(rec, source: str = "bed") -> list[str]:
>     """One GFF3 exon line per block: 0-based [s, e) becomes 1-based [s + 1, e]."""
>     return [f"{rec.chrom}\t{source}\texon\t{s + 1}\t{e}\t.\t{rec.strand}\t.\tParent={rec.name}"
>             for s, e in rec.blocks]
>
> clone_b = next(parse_bed(["chr22 2000 6000 cloneB 900 - 2000 6000 0 2 433,399, 0,3601"]))
> print("\n".join(bed12_to_gff3_exons(clone_b)))
> # chr22	bed	exon	2001	2433	.	-	.	Parent=cloneB
> # chr22	bed	exon	5602	6000	.	-	.	Parent=cloneB
> ```
>
> Missing for a complete model ([[GFF Format]]): a transcript line with `ID=cloneB` for the exons' `Parent` to point to, a gene line grouping transcripts, CDS lines derived from the thick part with their phases, and any attributes. BED12 stores one transcript per line and nothing above it.

> [!question] Exercise 5 (L3)
> The figure's toy line is `chr1 100 1000 txA 0 + 248 900 0 3 200,150,150, 0,400,750`. Compute the coding length (thick part intersected with blocks). Could the thick part be a complete coding sequence?

> [!success]- Solution
> Blocks: $[100, 300)$, $[500, 650)$, $[850, 1000)$. Intersect each with $[248, 900)$: $[248, 300)$ = 52, $[500, 650)$ = 150, $[850, 900)$ = 50. Total 252 = 84 × 3, so it can be a complete CDS of 84 codons (the last one a stop codon). A total that is not a multiple of 3 would reveal an annotation error or a partial CDS.

## Mastery checklist

- [ ] 1 Recognized: I can name the three mandatory BED fields and say that BED is 0-based half-open.
- [ ] 2 Understood: I can explain BED*n*, BED*n*+*m*, blocks, the thick part and what must be supplied out of band.
- [ ] 3 Practiced: I can write and validate BED files in Python and convert BED12 to exon intervals and GFF3.
- [ ] 4 Applied: in [[09-genome-browser]] I load BED tracks, and in [[10-genomic-pipeline]] I restrict analyses to BED target regions without off-by-one errors.
- [ ] 5 Explained: I can teach why BED needs out-of-band metadata and when to prefer bigBed, tabix or GFF3.

## References

[^spec]: [[GA4GH hts-specs]], `BEDv1` (GA4GH BED v1.0, Niu, Denisko and Hoffman): "Terminology and concepts", "Lines", "BED fields", "Coordinates", "Simple attributes", "Display attributes", "Blocks", "Examples", "Recommended practice" (sorting, whitespace, large files), "Information supplied out-of-band", "UCSC track files".
[^ucscfmt]: [[UCSC Genome Browser]], FAQ "Data File Formats", section "BED format" (fields, header lines, chromosome aliases, bigBed above 50 MB).
[^ucscct]: [[UCSC Genome Browser]], help page "Displaying Your Own Annotations in the Genome Browser" (supported custom-track formats, browser and track lines).
[^igv]: [[Integrative Genomics Viewer]], desktop documentation, "File Formats": BED (zero-based, track line, one track line per file), bigBed (only the displayed region is transferred) and broadPeak (BED 6+3).
