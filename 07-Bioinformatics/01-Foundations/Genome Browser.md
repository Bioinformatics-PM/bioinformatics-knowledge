---
aliases:
  - Genome Viewer
  - Genomic Data Viewer
  - Navigateur de génome
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Reference Genome]]"
  - "[[Genomic Coordinate System]]"
  - "[[BED Format]]"
  - "[[GFF Format]]"
related:
  - "[[Data Visualization]]"
  - "[[Interval Tree]]"
  - "[[Genomic File Indexing]]"
  - "[[VCF Format]]"
  - "[[SAM Format]]"
  - "[[Gene Annotation]]"
projects:
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[UCSC Genome Browser]]"
  - "[[Ensembl]]"
  - "[[Integrative Genomics Viewer]]"
  - "[[EMBL-EBI - Introductory Bioinformatics]]"
---

# Genome Browser

> [!abstract]
> A genome browser draws genomic data as horizontal tracks stacked under the coordinate axis of one reference assembly, and lets you search, zoom and pan to any locus and add your own files as tracks.

## Definition

A **genome browser** is an interactive graphical tool that displays annotation and data tracks beneath the positions of a [[Reference Genome]], with text and sequence search, zoom and scroll controls, and a details page for each item.[^ucscguide] It needs one reference genome, which serves as the coordinate system for every track.[^igvdocs] This curriculum uses three: the [[UCSC Genome Browser]] (web, thousands of assemblies with curated tracks), [[Ensembl]] (web, Ensembl's own gene models, variation and comparative data) and IGV (a viewer for your own files, on the desktop or in a web page).[^ucsc][^ensembl][^igv]

## Why it matters

- **Seeing is checking.** A peak, a variant call or a gene model is a line in a file until you see it next to the genes, the reads and public variation. Displaying your own variant calls from [[10-genomic-pipeline]] beside public variation tracks is how you notice a known polymorphism, a repeat or an artefact.[^ucsc]
- **Coordinate bugs become visible.** An off-by-one or wrong-assembly error ([[Genomic Coordinate System]], [[Reference Genome]]) shifts every feature relative to the genes around it.
- **Interpretation stays yours.** The UCSC user guide puts it plainly: the browser "does not draw conclusions"; it collates information and leaves interpretation to the user.[^ucscguide]
- **It is a project.** [[09-genome-browser]] rebuilds one: coordinate axis, tracks from FASTA, GFF and VCF, zoom, pan and search.

## Core (L1)

![[genome-browser-tracks.svg]]

**Anatomy.** An assembly selector, a position box, zoom and pan controls, a ruler, then one horizontal band per track: intervals from BED files, variant ticks, coverage signal, and genes, whose coding exons are blocks joined by intron lines, with thinner blocks for UTRs and arrowheads on the intron lines giving the direction of transcription.[^ucscguide]

**Three browsers, three roles.**

| | UCSC Genome Browser | Ensembl | IGV |
|---|---|---|---|
| Runs | web site | web site | desktop application, IGV-Web, igv.js |
| Strength | many assemblies, curated annotation tracks, custom tracks and track hubs | gene-centric views of Ensembl annotation, variation, comparative genomics | your own large files (reads, variants, signal), local or remote |
| Source | [^ucsc][^ucscguide] | [^ensembl][^ebi] | [^igv][^igvdocs] |

**Going to a locus.** Choose the assembly first, then type in the search box: a gene symbol, an mRNA accession, a chromosome band, or a range such as `chr22:1-20000`.[^ucscguide] IGV's locus box takes `chr5:90,339,000-90,349,000` or a gene symbol, and `All` shows the whole genome.[^igvdocs] UCSC positions are 1-based: `chr22:1-20000` is the first 20,000 bases ([[Genomic Coordinate System]]).[^ucscct]

**Display modes.** A UCSC track can be shown in five modes: *hide*; *dense* (all features collapsed into one line); *full* (one line per feature); *pack* (features labelled but sharing lines when they do not overlap); *squish* (as pack, half height, unlabelled). Above 250 lines in the window, full falls back to a more compact mode automatically.[^ucscguide]

**Loading your own tracks.**

- **UCSC custom tracks.** Write the data in a supported format (BED, GFF, GTF, VCF, BAM, bigBed, bigWig and others), optionally preceded by `browser` lines (initial position, tracks to show) and a `track` line (name, description, `visibility`, colour). Select the assembly *on which your data are based*, open "add custom tracks", and paste the data, upload a file (gzip accepted) or give a URL. Custom tracks are visible only from the machine that uploaded them and are deleted 48 hours after last access unless saved in a session; for permanent, shareable data UCSC recommends track hubs, which need remotely hosted, indexed binary files.[^ucscct]
- **IGV.** *File > Load from File* or *Load from URL*; indexed formats need their index (a BAM needs its `.bai`), and remote indexed files need a web server that supports byte-range requests. Switching reference genome clears the session.[^igvdocs]

## Deeper (L2)

**How browsers stay fast.** A whole-genome BAM or signal file is far too large to read for every screen. Indexed binary formats (bigBed, bigWig, BAM with its index) let a browser transfer only the part needed for the displayed region, which is why UCSC requires them to be hosted on a server supporting byte-range requests and why IGV requires sorted, indexed alignments.[^ucscct][^igvdocs] This is [[Genomic File Indexing]] seen from the user side.

**Level of detail.** At chromosome scale one pixel covers hundreds of thousands of bases, so individual features cannot be drawn; browsers switch representation with zoom (dense summaries, then packed features, then bases). UCSC's automatic fall-back above 250 lines is one such rule.[^ucscguide]

**Reading a view critically.** Each track comes from a provider with its own version and terms; read the track description before trusting it, and check assembly, chromosome naming and coordinate convention before mixing UCSC and Ensembl files.[^ucsc][^ensembl] A track "missing" in a region may mean no data, a filter, or a different assembly.

**Gene-centric browsing.** Ensembl organizes views around genes and transcripts: from a gene page you reach its transcripts, exons and variants on the same coordinates, which is the natural way to study one gene rather than one region.[^ebi][^ensembl]

## Advanced (L3)

**What a browser engine does.** For a window $[s, e)$ and a width of $W$ pixels, it (1) queries each track for features overlapping $[s, e)$, through an index or an [[Interval Tree]] rather than a scan; (2) chooses a representation from the density ($(e - s)/W$ bases per pixel); (3) assigns overlapping features to rows; (4) maps coordinates to pixels. Steps (3) and (4) are implemented below. [[09-genome-browser]] adds the tracks' parsers ([[FASTA Format]], [[GFF Format]], [[VCF Format]]).

**Optimal packing.** Assigning each feature, in order of start, to the first row whose last feature has ended is the greedy algorithm for interval partitioning. It uses exactly as many rows as the maximum number of features covering one point, and no packing can use fewer, since those features must all be on different rows. So "pack" mode is both simple and optimal in height.

**Beyond the linear axis.** One axis means one reference. Structural variants and alternate loci strain the model: sequence absent from the reference has no coordinates on which to be drawn. Representing it needs another model, such as a [[Pangenome]] graph, at the cost of the simple coordinate system.

## Mathematical representation

- **Viewport.** Window $[s, e)$ on one sequence, width $W$ pixels. A boundary position $p$ maps to $x(p) = \dfrac{p - s}{e - s}\, W$; the resolution is $r = (e - s)/W$ bases per pixel.
- **Visibility.** Feature $[a, b)$ is drawn iff $a < e$ and $s < b$ (half-open overlap).
- **Packing.** Features are vertices of an interval graph, adjacent when they overlap. A row assignment is a proper colouring; its minimum number of rows equals the maximum depth $\max_p |\{f : a_f \le p < b_f\}|$, reached by the greedy algorithm on features sorted by start.

## Computational representation

A text-mode browser: map positions to character columns, pack features into rows, print a ruler with 1-based end labels.

```python
def to_pixel(pos: int, win_start: int, win_end: int, width: int) -> int:
    """Map a 0-based boundary position to a column of a width-pixel track."""
    return round((pos - win_start) * width / (win_end - win_start))

def pack_rows(features):
    """Greedy row packing ('pack' display): each feature goes to the first row where it fits."""
    row_ends: list[int] = []
    placed = []
    for name, start, end in sorted(features, key=lambda f: f[1]):
        for i, last_end in enumerate(row_ends):
            if last_end <= start:
                row_ends[i] = end
                break
        else:
            i = len(row_ends)
            row_ends.append(end)
        placed.append((i, name, start, end))
    return placed, len(row_ends)

def render(features, win_start: int, win_end: int, width: int = 60) -> str:
    placed, n_rows = pack_rows(f for f in features if f[1] < win_end and f[2] > win_start)
    rows = [[" "] * width for _ in range(n_rows)]
    for row, name, start, end in placed:
        a = max(0, to_pixel(start, win_start, win_end, width))
        b = min(width, max(a + 1, to_pixel(end, win_start, win_end, width)))
        label = (name + "=" * (b - a))[: b - a]
        rows[row][a:b] = label
    ruler = f"{win_start + 1:<{width // 2}}{win_end:>{width - width // 2}}"   # 1-based display
    return "\n".join([ruler, "|" + "-" * (width - 2) + "|"] + ["".join(r) for r in rows])

features = [("peakA", 1000, 1400), ("peakB", 1200, 1900), ("peakC", 1500, 1700),   # invented BED
            ("peakD", 2100, 2600), ("peakE", 2500, 2900), ("far", 9000, 9100)]
print(render(features, 1000, 3000))
print("bp per column:", (3000 - 1000) / 60)
```

Output:

```text
1001                                                    3000
|----------------------------------------------------------|
peakA=======   peakC=            peakD==========            
      peakB================                  peakE=======   
bp per column: 33.333333333333336
```

The feature `far` lies outside the window and is never drawn; the five others need two rows because at most two overlap at any point. The same data are drawn in the figure above.

## Worked example

> [!example] A custom track in the UCSC browser
> The UCSC help gives this "simple annotation file":[^ucscct]
> ```text
> browser position chr22:20100000-20100900
> track name=coords description="Chromosome coordinates list" visibility=2
> #chrom chromStart chromEnd
> chr22 20100000 20100100
> chr22 20100011 20100200
> chr22 20100215 20100400
> chr22 20100350 20100500
> chr22 20100700 20100800
> chr22 20100700 20100900
> ```
> 1. **Assembly.** Nothing in the file names it: you choose it on the gateway page, and the same file drawn on hg19 and on hg38 lands on different sequence ([[Reference Genome]]).
> 2. **Browser line.** `chr22:20100000-20100900` is a 1-based range: the window is $[20{,}099{,}999,\ 20{,}100{,}900)$ in 0-based terms.
> 3. **Track line.** `visibility=2` is full mode (0 hide, 1 dense, 2 full, 3 pack, 4 squish).[^ucscct]
> 4. **Data.** Six BED3 intervals; the first is displayed as `chr22:20100001-20100100`. In pack mode they fit on two rows:
> ```python
> ucsc = [("f1", 20100000, 20100100), ("f2", 20100011, 20100200), ("f3", 20100215, 20100400),
>         ("f4", 20100350, 20100500), ("f5", 20100700, 20100800), ("f6", 20100700, 20100900)]
> print(render(ucsc, 20100000 - 1, 20100900))
> ```
> ```text
> 20100000                                            20100900
> |----------------------------------------------------------|
> f1=====       f3===========                    f5====       
>  f2==========          f4========              f6===========
> ```

## Common misconceptions

> [!warning] "The browser converts my file to the assembly I am viewing"
> It does not: UCSC asks you to select the assembly your data are based on, and IGV draws every track on the loaded reference.[^ucscct][^igvdocs] A file from another release is drawn at wrong positions without warning; convert it first (liftOver, see [[Reference Genome]]).

> [!warning] "My custom track is saved and shared"
> A UCSC custom track is visible only from the machine that uploaded it and expires 48 hours after its last use, unless saved in a session; track hubs are the durable option.[^ucscct]

> [!warning] "Dense mode shows fewer features"
> Dense mode draws all features, collapsed into a single line; nothing is filtered, only the vertical separation is lost.[^ucscguide]

## Exercises

> [!question] Exercise 1 (L1)
> List, in order, the steps to display the APOE variant rs429358 in the UCSC browser on hg38, and give the BED line of that single base (hg38 position chr19:44,908,684).

> [!success]- Solution
> Select human, assembly hg38 (GRCh38); type the range `chr19:44908684-44908684` (or the gene symbol `APOE`, then navigate) in the search box; zoom until single bases are visible. The BED line of that base is `chr19 44908683 44908684`: 0-based start, end unchanged. The position comes from the UCSC FAQ.[^ucscrel]

> [!question] Exercise 2 (L1)
> Write a UCSC custom-track file that opens at `chr1:1000-2000` and shows two invented features named `a` (1-based 1,101-1,200) and `b` (1-based 1,401-1,700) in pack mode.

> [!success]- Solution
> ```text
> browser position chr1:1000-2000
> track name=demo description="two invented features" visibility=3
> chr1	1100	1200	a
> chr1	1400	1700	b
> ```
> The browser line is 1-based; the BED data are 0-based, so each start loses one; `visibility=3` is pack.[^ucscct]

> [!question] Exercise 3 (L2)
> On a 1,000-pixel track, how many bases does one pixel cover when viewing a 250 Mb chromosome, a 2 kb gene region, and a 100 bp window? Which representation suits each?

> [!success]- Solution
> $r = (e - s)/W$: 250,000 bp per pixel, 2 bp per pixel, 0.1 bp per pixel (10 pixels per base). Chromosome: density or dense summaries only; gene region: individual exons and packed features; 100 bp: individual bases and letters. Choosing the representation from $r$ is the level-of-detail rule of any browser.

> [!question] Exercise 4 (L3, Python)
> Show that `pack_rows` is optimal on the UCSC example: compute the maximum number of features covering one point and compare with the number of rows.

> [!success]- Solution
> ```python
> def max_depth(features) -> int:
>     """Largest number of features covering one point (sweep over sorted boundaries)."""
>     events = sorted([(s, 1) for _, s, _ in features] + [(e, -1) for _, _, e in features])
>     depth = best = 0
>     for _, step in events:            # at equal positions, -1 sorts first: half-open ends
>         depth += step
>         best = max(best, depth)
>     return best
>
> placed, rows = pack_rows(ucsc)
> print(rows, max_depth(ucsc))          # 2 2
> ```
>
> Depth 2 means two features must be on different rows somewhere, so at least 2 rows are needed; the greedy packing uses 2. In general the greedy algorithm opens a new row only when every row is still occupied at the new feature's start, that is when depth at that point equals the current number of rows plus one, so the row count never exceeds the maximum depth.

> [!question] Exercise 5 (L3)
> [[09-genome-browser]] must display a 10 GB BAM file and a 2 GB GFF file for any 10 kb window in under 100 ms. Which design choices from this note (and neighbours) make this possible?

> [!success]- Solution
> Never read whole files: sort and index the BAM (random access by region, as IGV requires),[^igvdocs] and convert or index the annotation for region queries (bigBed-like binary index or an [[Interval Tree]] built once); fetch only features overlapping the window; choose the representation from bases per pixel (coverage summary instead of reads when zoomed out); pack rows greedily. See [[Genomic File Indexing]] for the index structures.

## Mastery checklist

- [ ] 1 Recognized: I can name the UCSC, Ensembl and IGV browsers and the parts of a browser view.
- [ ] 2 Understood: I can explain assembly choice, display modes, custom tracks versus track hubs, and why big files must be indexed.
- [ ] 3 Practiced: I can navigate to a locus, load my own BED or VCF file in UCSC and IGV, and implement row packing and the pixel mapping in Python.
- [ ] 4 Applied: I inspect the outputs of [[10-genomic-pipeline]] in IGV, and [[09-genome-browser]] renders real tracks at every zoom level.
- [ ] 5 Explained: I can teach how a browser turns indexed files into a view, and the limits of a single linear reference.

## References

[^ucscguide]: [[UCSC Genome Browser]], "Genome Browser User Guide" (overview, opening the browser at a position, annotation track display modes).
[^ucscct]: [[UCSC Genome Browser]], help page "Displaying Your Own Annotations in the Genome Browser" (custom tracks: formats, browser and track lines, `visibility` values, loading, 48-hour lifetime, sessions, track hubs, remote hosting, the "simple annotation file" example).
[^ucscrel]: [[UCSC Genome Browser]], FAQ "Assembly Releases and Versions" (position of rs429358 on hg38).
[^ucsc]: [[UCSC Genome Browser]], 2025 database update and source note (assemblies, tracks, displaying your own variant calls next to public variation).
[^ensembl]: [[Ensembl]], "Ensembl 2025" and source note (genome browser, gene models, variation, comparative genomics; release versioning).
[^ebi]: [[EMBL-EBI - Introductory Bioinformatics]], module "Finding information about genes with Ensembl".
[^igv]: [[Integrative Genomics Viewer]], Robinson et al., *Nature Biotechnology* 29:24-26 (2011).
[^igvdocs]: [[Integrative Genomics Viewer]], desktop documentation: "Reference genome", "Loading and removing tracks", "Navigating the view", "File Formats" (BAM indexing).
