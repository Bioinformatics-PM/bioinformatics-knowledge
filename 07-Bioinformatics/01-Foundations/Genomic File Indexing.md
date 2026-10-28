---
aliases:
  - Genomic Index
  - BAI
  - BAM Index
  - Tabix Index
  - TBI
  - CSI Index
  - FAI
  - FASTA Index
  - BGZF
  - bgzip
  - tabix
  - Indexation de fichiers génomiques
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[FASTA Format]]"
  - "[[SAM Format]]"
  - "[[VCF Format]]"
  - "[[BED Format]]"
  - "[[Genomic Coordinate System]]"
  - "[[File Input and Output]]"
related:
  - "[[Data Compression]]"
  - "[[Database Index]]"
  - "[[Interval Tree]]"
  - "[[B-Tree]]"
  - "[[Binary Search]]"
  - "[[Genomic Interval Arithmetic]]"
  - "[[Genome Browser]]"
  - "[[Integer Representation]]"
  - "[[Sorting]]"
projects:
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[GA4GH hts-specs]]"
  - "[[HTSlib]]"
  - "[[Integrative Genomics Viewer]]"
---

# Genomic File Indexing

> [!abstract]
> An index is a small side file that maps genomic coordinates to byte positions in a large sorted file, so that one region is read with a few seeks instead of a full scan: FAI does it for FASTA by arithmetic on line lengths, and BGZF block compression plus a binning index (BAI, TBI, CSI) does it for compressed BAM, VCF and BED files.

## Definition

A **genomic file index** is an auxiliary file that records where the records of each region of the reference start in a large data file, so that a region query reads only the records that may overlap it. Four mechanisms cover the common formats:

- the **FAI** index of a FASTA (or FASTQ) file stores the byte offset and line geometry of each sequence;[^fai]
- **BGZF** compresses a file as independent gzip blocks and addresses any record by a **virtual file offset**;[^bgzf]
- **binning indexes** (BAI for BAM, TBI for tabix-indexed text, CSI as their generalization) map intervals to chunks of virtual offsets, completed by a linear index;[^bai][^tabix][^csi]
- the **CRAI** index lists the slices of a CRAM file.[^cram]

## Why it matters

- **Region queries.** The stated aim of BAM indexing is to retrieve the alignments overlapping a region without going through the whole file; with the binning and linear indexes together, most regions need a single seek.[^bai]
- **Browsing and remote data.** IGV loads indexed formats together with their index file, also from URLs, which requires web servers that support byte-range requests; tabix likewise queries files over the network, downloading the index first.[^igv][^htslib] [[09-genome-browser]] needs the same mechanics for the reference (FAI) and for annotation and variant tracks.
- **Pipelines.** [[10-genomic-pipeline]] sorts, compresses and indexes BAM and VCF files, so that later steps read one region at a time ([[SAM Format]], [[VCF Format]]).
- **Typical failures.** Unsorted input, plain gzip instead of BGZF, an index older than its data file, chromosomes longer than 512 Mbp: each one breaks region queries (Common misconceptions).

## Core (L2)

![[bgzf-virtual-offsets-and-bins.svg]]

### FAI: random access by arithmetic

If every line of a sequence holds the same number of bases (except the last), the byte of any base follows from five numbers per sequence, which is all a `.fai` file stores, one tab-separated line per sequence:[^fai]

| Column | Meaning |
|---|---|
| NAME | sequence name (first word of the `>` line) |
| LENGTH | number of bases |
| OFFSET | byte offset of the first base, counted from 0 |
| LINEBASES | bases per line |
| LINEWIDTH | bytes per line, line terminator included |
| QUALOFFSET | FASTQ only: offset of the first quality character |

The 0-based base $i$ sits at byte $\text{OFFSET} + \lfloor i / \text{LINEBASES} \rfloor \cdot \text{LINEWIDTH} + (i \bmod \text{LINEBASES})$, the formula of [[FASTA Format#Mathematical representation]]. The manual's example file, two sequences with 30 and 14 bases per line, is indexed `one 66 5 30 31` and `two 28 98 14 15` with LF line endings, and `one 66 6 30 32`, `two 28 103 14 16` with CR-LF (reproduced in Computational representation).[^fai]

### BGZF: compression that keeps random access

In a plain gzip file, reaching a position means decompressing everything before it. BGZF instead writes a series of gzip blocks, each at most 64 KiB before and after compression, each a complete gzip member whose "extra field" `BC` stores the block size; since concatenated gzip members decompress to the concatenation of their data, any gunzip reads a BGZF file.[^bgzf][^htslib] A record is addressed by a **virtual file offset**:[^bgzf]

$$v = \text{coffset} \ll 16 \;|\; \text{uoffset},$$

where coffset is the byte offset of the block's start in the file and uoffset the offset inside the decompressed block. Virtual offsets can be compared, but not subtracted or incremented. An empty 28-byte block marks the end of the file, so truncation can be detected.[^bgzf] BAM, BCF and tabix-indexed text files are BGZF files.[^bgzf][^bcf][^htslib]

### Binning: which records may overlap a region?

The scheme comes from the UCSC Genome Browser (Kent et al. 2002): the reference is covered by bins on six levels, each bin either containing or disjoint from any other, and each record is filed in the **smallest bin that contains it entirely**.[^bai]

| Level | Bin numbers | Bin size |
|---:|---|---|
| 0 | 0 | $2^{29}$ bp = 512 Mbp |
| 1 | 1-8 | $2^{26}$ = 64 Mbp |
| 2 | 9-72 | $2^{23}$ = 8 Mbp |
| 3 | 73-584 | $2^{20}$ = 1 Mbp |
| 4 | 585-4680 | $2^{17}$ = 128 kbp |
| 5 | 4681-37448 | $2^{14}$ = 16 kbp |

[^bai]

For each bin, the index stores **chunks**, pairs of virtual offsets delimiting runs of its records; because the file is sorted by position, a bin's records cluster into few chunks. A query collects the bins overlapping it on every level and reads their chunks. A **linear index** adds, for each 16 kbp window, the smallest virtual offset of the records overlapping the window: chunks that end before it can be skipped. The file must be sorted by reference, then by leftmost position, before indexing, and the six levels limit BAI to sequences shorter than $2^{29}$ bp.[^bai]

### Index files at a glance

| Index | Data file | Mechanism | Limits |
|---|---|---|---|
| `.fai` (+ `.gzi` if BGZF) | FASTA, FASTQ | line-geometry arithmetic | equal line lengths within each sequence |
| `.bai` | BAM | bins + linear index | sequences up to $2^{29} - 1$ bp |
| `.tbi` | bgzipped TAB-delimited text (VCF, BED, GFF, SAM) | same bins, plus the columns to read | same as BAI |
| `.csi` | BAM, BCF, bgzipped text | bins of configurable size and depth | sequences as long as SAM and BAM allow |
| `.crai` | CRAM | gzipped table of slices | two reads per access |

[^fai][^bai][^tabix][^csi][^cram][^htslib]

### tabix: one index for any sorted table

Tabix indexes a TAB-delimited genome position file that is **position-sorted and compressed with bgzip**.[^htslib] Its TBI index stores the sequence names and the columns holding name, start and end, the comment character and the number of header lines to skip; a flag marks 0-based half-open coordinates (BED) as opposed to 1-based closed ones (GFF). For VCF, a record ends at POS plus the size of its deletion; for SAM, at POS plus the reference length taken from CIGAR.[^tabix] Presets exist for `gff`, `bed`, `sam` and `vcf`, and query regions are written `chr:beg-end`, 1-based and inclusive ([[Genomic Coordinate System]]).[^htslib] A BED file must use a single tab between fields to be indexed this way.[^bed]

## Advanced (L3)

**Why one seek usually suffices.** Candidate bins are few (one range per level), chunks of the same bin that lie close together can be merged to save seeks, and the linear index skips the large bins' records that end before the query: with both indexes, most regions are retrieved with one seek.[^bai] Exercise 4 counts the candidate bins as the query grows.

**Pseudo-bins.** A BAI file may hold, for each reference, an extra bin numbered 37450 with the counts of mapped and unmapped reads, and a final count of unplaced reads, so that per-chromosome read counts are read from the index instead of the data.[^bai]

**CSI for long chromosomes.** CSI keeps the scheme but makes the smallest bin size ($2^{\text{min\_shift}}$) and the number of levels (depth) parameters; BAI is the case min_shift = 14, depth = 5. CSI supports reference sequences of any length that SAM and BAM allow,[^csi][^bai] and tabix produces it for chromosomes longer than 512 Mbp.[^htslib]

**CRAM indexes slices, not records.** A CRAM index is a gzipped table with one line per slice (reference, start, span, container offset, slice offset, slice size); random access reads the container header and compression header, then the slice, two reads instead of one. A BAM-style index can also point into CRAM containers.[^cram]

**Relatives.** The binning scheme is a representation of an R-tree, each bin being a node.[^bai] An [[Interval Tree]] answers the same overlap queries in memory; a [[B-Tree]] or a relational [[Database Index]] orders one key, whereas overlap involves two coordinates, which is why genomic files use bins; bigBed files carry their index inside the binary file ([[BED Format]]).[^bed]

## Mathematical representation

- **Virtual offsets.** $v = c \cdot 2^{16} + u$ with $0 \le u < 2^{16}$ and $c < 2^{48}$. The order of $v$ is the lexicographic order of $(c, u)$, which is the order of records in the file; $v_2 - v_1$ mixes compressed and uncompressed bytes and measures nothing.
- **Bins.** Level $\ell \in \{0, \dots, 5\}$ has bins of $2^{s_\ell}$ bp with $s_\ell = 29 - 3\ell$, numbered from $o_\ell = (8^\ell - 1)/7$ (0, 1, 9, 73, 585, 4681). A record $[b, e)$ (0-based, half-open) goes to $o_{\ell^*} + \lfloor b / 2^{s_{\ell^*}} \rfloor$, where $\ell^*$ is the deepest level with $\lfloor b / 2^{s_\ell} \rfloor = \lfloor (e - 1) / 2^{s_\ell} \rfloor$. There are $\sum_{\ell=0}^{5} 8^\ell = (8^6 - 1)/7 = 37{,}449$ bins.
- **Candidates.** For a query $[b, e)$, the candidate set is $\bigcup_\ell \{o_\ell + \lfloor b / 2^{s_\ell} \rfloor, \dots, o_\ell + \lfloor (e - 1) / 2^{s_\ell} \rfloor\}$. It is complete: a record filed in bin $\beta$ lies inside $\beta$'s interval, so if it overlaps the query, $\beta$'s interval does too, and $\beta$ is a candidate.
- **Linear index.** With windows $w(x) = \lfloor x / 2^{14} \rfloor$ and $L[w] = \min\{v(r) : r \text{ overlaps window } w\}$, a record $r$ with $v(r) < L[w(b)]$ does not overlap window $w(b)$ (otherwise $L$ would be smaller) and, the file being sorted, starts before it: it ends before $2^{14} w(b) \le b$, so it cannot overlap the query.
- **FAI.** $\text{byte}(i) = o + \lfloor i / B \rfloor W + (i \bmod B)$ for line bases $B$ and line width $W$; a region $[a, b)$ costs $O(b - a)$ bytes of reading, whatever the sequence length.

## Computational representation

Two programs in standard-library Python. The first builds and uses an FAI index on the example file of the `faidx(5)` manual.

```python
import os
import tempfile

def build_fai(data: bytes) -> list[tuple]:
    """NAME, LENGTH, OFFSET, LINEBASES, LINEWIDTH for each record of a well-formatted FASTA."""
    out, pos, lines, k = [], 0, data.splitlines(keepends=True), 0
    while k < len(lines):
        header = lines[k]; pos += len(header); k += 1
        name, offset, length, linebases, linewidth = header[1:].split()[0].decode(), pos, 0, None, None
        while k < len(lines) and not lines[k].startswith(b">"):
            bases = len(lines[k].rstrip(b"\r\n"))
            if linebases is None:
                linebases, linewidth = bases, len(lines[k])
            length += bases; pos += len(lines[k]); k += 1
        out.append((name, length, offset, linebases, linewidth))
    return out

def fetch(path: str, entry: tuple, start: int, end: int) -> str:
    """Bases [start, end) (0-based) of one sequence, with one seek."""
    name, length, offset, linebases, linewidth = entry
    byte = lambda i: offset + (i // linebases) * linewidth + i % linebases
    with open(path, "rb") as fh:
        fh.seek(byte(start))
        raw = fh.read(byte(end) - byte(start))
    return raw.replace(b"\n", b"").replace(b"\r", b"").decode()

FASTA = (">one\nATGCATGCATGCATGCATGCATGCATGCAT\nGCATGCATGCATGCATGCATGCATGCATGC\nATGCAT\n"
         ">two another chromosome\nATGCATGCATGCAT\nGCATGCATGCATGC\n")   # example of faidx(5)
for eol in (b"\n", b"\r\n"):
    print(build_fai(FASTA.encode().replace(b"\n", eol)))
path = os.path.join(tempfile.mkdtemp(), "toy.fa")
with open(path, "wb") as fh:
    fh.write(FASTA.encode())
fai = {row[0]: row for row in build_fai(FASTA.encode())}
print(fetch(path, fai["two"], 10, 20), ("ATGCATGCATGCAT" + "GCATGCATGCATGC")[10:20])
```

```text
[('one', 66, 5, 30, 31), ('two', 28, 98, 14, 15)]
[('one', 66, 6, 30, 32), ('two', 28, 103, 14, 16)]
GCATGCATGC GCATGCATGC
```

Both index lines match the manual for both line endings. The second program writes a BGZF file from scratch, checks it against the specification's end-of-file block and against Python's `gzip`, builds a TBI-like index (bins, chunks and linear index) over 20,000 invented sorted intervals, and answers a region query.

```python
import gzip
import os
import random
import struct
import tempfile
import zlib

EOF_MARKER = bytes.fromhex("1f8b08040000000000ff0600424302001b0003000000000000000000")

def bgzf_block(data: bytes) -> bytes:
    """One BGZF block: a gzip member whose 'BC' extra field holds BSIZE (block size - 1)."""
    assert len(data) <= 65536
    deflate = zlib.compressobj(6, zlib.DEFLATED, -15)          # raw deflate, as inside gzip
    cdata = deflate.compress(data) + deflate.flush()
    bsize = 12 + 6 + len(cdata) + 8                            # header, extra field, data, CRC32 + ISIZE
    header = struct.pack("<4BI2BH", 31, 139, 8, 4, 0, 0, 255, 6) + struct.pack("<2B2H", 66, 67, 2, bsize - 1)
    return header + cdata + struct.pack("<2I", zlib.crc32(data), len(data))

def read_block(fh, coffset: int) -> tuple[bytes, int]:
    """Decompressed data of the block starting at byte coffset, and its size on disk."""
    fh.seek(coffset)
    head = fh.read(18)
    size = struct.unpack("<H", head[16:18])[0] + 1                # BSIZE + 1
    return zlib.decompress(fh.read(size - 18)[:-8], -15), size     # drop CRC32 and ISIZE

def voffset(coffset: int, uoffset: int) -> int:
    return coffset << 16 | uoffset

def reg2bin(beg: int, end: int) -> int:
    """Smallest BAI bin containing [beg, end) (0-based, half-open)."""
    end -= 1
    for shift, first in ((14, 4681), (17, 585), (20, 73), (23, 9), (26, 1)):
        if beg >> shift == end >> shift:
            return first + (beg >> shift)
    return 0

def reg2bins(beg: int, end: int) -> list[int]:
    """All bins that may hold records overlapping [beg, end): one range per level."""
    end -= 1
    bins = [0]
    for shift, first in ((26, 1), (23, 9), (20, 73), (17, 585), (14, 4681)):
        bins.extend(range(first + (beg >> shift), first + (end >> shift) + 1))
    return bins

print(bgzf_block(b"") == EOF_MARKER)

random.seed(7)                                     # invented sorted intervals on one toy chromosome
starts = sorted(random.randrange(0, 3_000_000) for _ in range(20_000))
lines = [f"chrT\t{s}\t{s + random.choice([50, 300, 2_000, 40_000])}\tf{k}\n".encode() for k, s in enumerate(starts)]
bgz, block, offsets, n_blocks = bytearray(), bytearray(), [], 1
for line in lines:                                 # blocks of <= 64 KiB; a line never spans two
    if len(block) + len(line) > 65536:
        bgz += bgzf_block(bytes(block)); block = bytearray(); n_blocks += 1
    offsets.append(voffset(len(bgz), len(block)))
    block += line
bgz += bgzf_block(bytes(block)) + EOF_MARKER
print(len(b"".join(lines)), "bytes of text ->", len(bgz), "bytes of BGZF,", gzip.decompress(bytes(bgz)) == b"".join(lines))

index, linear = {}, {}                             # bin -> chunks; 16 kbp window -> smallest offset
for k, line in enumerate(lines):
    _, s, e, _ = line.split(b"\t")
    s, e = int(s), int(e)
    v_beg = offsets[k]
    v_end = offsets[k + 1] if k + 1 < len(offsets) else voffset(len(bgz) - len(EOF_MARKER), 0)
    chunks = index.setdefault(reg2bin(s, e), [])
    if chunks and chunks[-1][1] == v_beg:
        chunks[-1][1] = v_end                      # extend a contiguous chunk
    else:
        chunks.append([v_beg, v_end])
    for w in range(s >> 14, ((e - 1) >> 14) + 1):
        linear[w] = min(linear.get(w, v_beg), v_beg)

path = os.path.join(tempfile.mkdtemp(), "toy.bed.gz")
with open(path, "wb") as fh:
    fh.write(bgz)

def query(path: str, beg: int, end: int):
    """Records overlapping [beg, end): candidate bins, then chunks ending after the linear-index floor."""
    floor = linear.get(beg >> 14, 0)
    candidates = [c for b in reg2bins(beg, end) for c in index.get(b, [])]
    chunks = sorted(c for c in candidates if c[1] > floor)
    hits, decoded, blocks = set(), 0, {}
    with open(path, "rb") as fh:
        for v_beg, v_end in chunks:
            v = max(v_beg, floor)
            while v < v_end:
                c, u = v >> 16, v & 0xFFFF
                if c not in blocks:
                    blocks[c] = read_block(fh, c)
                data, size = blocks[c]
                stop = data.index(b"\n", u) + 1    # lines never span blocks in this writer
                _, s, e, name = data[u:stop].split(b"\t")
                decoded += 1
                if int(s) < end and beg < int(e):
                    hits.add(name.strip().decode())
                v = voffset(c, stop) if stop < len(data) else voffset(c + size, 0)
    return sorted(hits), len(candidates), len(chunks), decoded, len(blocks)

truth = sorted(l.split(b"\t")[3].strip().decode() for l in lines
               if int(l.split(b"\t")[1]) < 1_500_100 and 1_500_000 < int(l.split(b"\t")[2]))
hits, n_cand, n_chunks, decoded, blocks = query(path, 1_500_000, 1_500_100)
print(len(lines), "records in", n_blocks, "blocks;", len(index), "bins used")
print("hits", len(hits), "(brute force agrees:", hits == truth, ") chunks", n_cand, "->", n_chunks,
      "after linear index; records decoded", decoded, "; blocks read", blocks)
```

```text
True
534121 bytes of text -> 181605 bytes of BGZF, True
20000 records in 9 blocks; 211 bins used
hits 78 (brute force agrees: True ) chunks 625 -> 413 after linear index; records decoded 605 ; blocks read 3
```

The empty block written by `bgzf_block` is byte for byte the end-of-file marker of the specification, and `gzip.decompress` reads the whole BGZF file: block compression costs nothing in compatibility. The query decodes 605 of 20,000 records from 3 of 9 blocks and finds the same 78 records as a full scan. This toy writer keeps each line inside one block to keep the reader short; BAM records may span blocks.[^bgzf]

## Worked example

> [!example] The binning example of the SAM specification
> A genome shorter than 144 kbp is binned on three levels: bin 0 (0-144 kbp), bins 1 to 3 (48 kbp each), bins 4 to 12 (16 kbp each), as in the figure.[^bai]
> 1. **Filing.** An alignment over 65-67 kbp fits in bin 8 (64-80 kbp). One over 51-70 kbp crosses the 64 kbp boundary: smallest bin 2 (48-96 kbp). One over 40-49 kbp crosses 48 kbp: only bin 0 contains it.
> 2. **Query** $[65\text{k}, 71\text{k})$: the bins overlapping it are 0, 2 and 8, so the three alignments are candidates.
> 3. **Linear index.** The query lies in the 64-80 kbp window; the 40-49 kbp alignment ends before 64 kbp, so its offset precedes the window's smallest offset and its chunk is skipped: one seek saved.
> 4. **Real BAI numbers** (`reg2bin` of Computational representation): a 100 bp read at 1-based POS 1,000,000, the 0-based interval $[999\,999, 1\,000\,099)$, stays inside one 16 kbp window: bin $4681 + \lfloor 999\,999 / 2^{14} \rfloor = 4681 + 61 = 4742$. A 2,000 bp alignment $[65\,000, 67\,000)$ crosses 65,536, a 16 kbp boundary, and rises to the 128 kbp level: bin $585 + 0 = 585$ (Exercise 3).

## Common misconceptions

> [!warning] "Any .gz file can be indexed"
> Tabix requires bgzip compression: a plain gzip stream has no independent blocks to seek to. Recompress with bgzip; the result still opens with gunzip.[^htslib][^bgzf]

> [!warning] "An index makes an unsorted file searchable"
> Indexing requires coordinate-sorted data (reference, then leftmost position); chunks and the linear index assume it.[^bai][^htslib] Sort first, then compress, then index, and rebuild the index whenever the data file changes, since its offsets point into one exact file.

> [!warning] "A virtual offset is a byte position"
> It packs a compressed block offset and an offset inside the decompressed block; offsets can be compared, but differences or sums are meaningless.[^bgzf]

> [!warning] "BAI and TBI work for every genome"
> Six levels of bins stop at $2^{29}$ bp: chromosomes longer than 512 Mbp need CSI.[^bai][^htslib]

## Exercises

> [!question] Exercise 1 (L2, Python)
> With the index line `two 28 98 14 15` of the example, at which byte is the 20th base of `two`? Check by reading that byte.

> [!success]- Solution
> 0-based $i = 19$: $98 + \lfloor 19/14 \rfloor \cdot 15 + (19 \bmod 14) = 98 + 15 + 5 = 118$.
> ```python
> i = 19                                             # base 20 of "two", 0-based
> name, length, offset, linebases, linewidth = fai["two"]
> byte = offset + (i // linebases) * linewidth + i % linebases
> with open(path_fa := os.path.join(tempfile.mkdtemp(), "toy.fa"), "wb") as fh:
>     fh.write(FASTA.encode())
> with open(path_fa, "rb") as fh:
>     fh.seek(byte)
>     print(byte, fh.read(1), ("ATGCATGCATGCAT" + "GCATGCATGCATGC")[i])
> # 118 b'C' C
> ```
> The 15-byte jump crosses one full line (14 bases and the newline).

> [!question] Exercise 2 (L2)
> A record starts 3,000 bytes into the decompressed data of a block that begins at byte 1,234,567 of a BAM file. Write its virtual offset, decode it back, and explain why $v_2 - v_1$ between two records is not a size.

> [!success]- Solution
> $v = 1\,234\,567 \cdot 2^{16} + 3\,000 = 80\,908\,585\,912$ (`0x12d6870bb8`); decoding is `v >> 16` = 1,234,567 and `v & 0xFFFF` = 3,000. Between two blocks, the difference is $\Delta c \cdot 2^{16} + \Delta u$: compressed bytes times 65,536 plus uncompressed bytes, a number with no unit, hence the rule that offsets may be compared but not subtracted.[^bgzf]

> [!question] Exercise 3 (L2, Python)
> Compute by hand, then with `reg2bin`, the bins of $[65\,000, 67\,000)$ and $[999\,999, 1\,000\,099)$, and check the values the specification gives for an unplaced read, `reg2bin(-1, 0)` and `reg2bins(-1, 0)`.

> [!success]- Solution
> ```python
> print(reg2bin(65_000, 67_000), reg2bin(999_999, 1_000_099), reg2bin(-1, 0), reg2bins(-1, 0))
> # 585 4742 4680 [0, 0, 8, 72, 584, 4680]
> ```
> $65\,000 \gg 14 = 3$ but $66\,999 \gg 14 = 4$: different 16 kbp windows; at level 4 both give 0, so bin $585 + 0$. The read at 1 Mbp stays in window 61: bin 4742. The specification states `reg2bin(-1, 0)` = 4680 and `reg2bins(-1, 0)` = `[0, 0, 8, 72, 584, 4680]`, computed with two's-complement shifts, which Python's `>>` on negative integers reproduces.[^bai]

> [!question] Exercise 4 (L3, Python)
> How many candidate bins does `reg2bins` return for queries of 1 bp, 16,384 bp, 1 Mbp and $2^{29}$ bp starting at 0? Relate the result to the cost of a query.

> [!success]- Solution
> ```python
> print([len(reg2bins(0, n)) for n in (1, 16_384, 1_000_000, 1 << 29)], (8 ** 6 - 1) // 7)
> # [6, 6, 74, 37449] 37449
> ```
> A short query touches one bin per level (6). A 1 Mbp query covers 62 windows of 16 kbp, 8 bins of 128 kbp, and one bin on each upper level: 74 candidates, most of them empty in sparse data. The whole range touches all 37,449 bins. Cost therefore grows with the size of the region queried, not with the size of the file, which is the purpose of the index.

> [!question] Exercise 5 (L3)
> Which index, or which preparation, does each case need? (a) a BED file with fields separated by spaces, to be queried by region; (b) a VCF compressed with gzip; (c) a BAM file of a plant whose largest chromosome is 700 Mbp; (d) a FASTA file whose lines have varying lengths; (e) a CRAM file to be opened at one locus.

> [!success]- Solution
> (a) Convert to single tabs, sort, bgzip and index with tabix: tabix requires single-tab separators.[^bed] (b) Decompress and recompress with bgzip, then index with tabix.[^htslib] (c) CSI, since BAI cannot address positions beyond $2^{29} - 1$ = 536,870,911.[^bai][^csi] (d) Rewrite with a fixed line width before building the FAI, which requires equal lengths within each sequence.[^fai] (e) A `.crai` index, plus the reference sequence that CRAM decoding needs ([[SAM Format]]).[^cram]

## Mastery checklist

- [ ] 1 Recognized: I can name the index file that goes with FASTA, BAM, CRAM and bgzipped VCF or BED files.
- [ ] 2 Understood: I can explain the FAI formula, BGZF blocks and virtual offsets, the binning levels and the linear index, and why sorting is required.
- [ ] 3 Practiced: I can write a BGZF block, compute bins and candidate bins, and implement a region query that agrees with a full scan.
- [ ] 4 Applied: [[09-genome-browser]] reads only the displayed region of a real indexed reference and of indexed tracks, and [[10-genomic-pipeline]] produces sorted, indexed BAM and VCF files.
- [ ] 5 Explained: I can teach why one seek usually suffices, the limits of BAI and TBI, and the trade-offs of CSI and CRAM indexes.

## References

[^fai]: [[HTSlib]], `faidx(5)`: the `.fai` columns, the "well-formatted" FASTA requirement, the LF and CR-LF examples; `samtools-faidx(1)`: BGZF-compressed input with a `.gzi` index.
[^bgzf]: [[GA4GH hts-specs]], `SAMv1`, §4.1 "The BGZF compression format", with "Random access" (virtual file offsets) and "End-of-file marker".
[^bai]: [[GA4GH hts-specs]], `SAMv1`, §5 "Indexing BAM": basic binning index (UCSC scheme, Kent et al. 2002), reducing small chunks, linear index, the conceptual example, the BAI format and its pseudo-bins, and the `reg2bin` and `reg2bins` code.
[^tabix]: [[GA4GH hts-specs]], `tabix` (The Tabix index file format, H. Li): fields of the TBI index, 0-based flag, region ends for SAM and VCF records, GFF and BED settings.
[^csi]: [[GA4GH hts-specs]], `CSIv1`: `min_shift` and `depth`, generalized `reg2bin` and `reg2bins`.
[^cram]: [[GA4GH hts-specs]], `CRAMv3`, "Indexing": the CRAM index, two reads per random access, BAM-style indexes on CRAM.
[^bcf]: [[GA4GH hts-specs]], `VCFv4.5`, "BCF specification": BCF2 records in BGZF blocks, indexed like BAM.
[^bed]: [[GA4GH hts-specs]], `BEDv1`, "Large BED files" (bigBed as an indexed binary format; tabix only with a single tab as separator).
[^htslib]: [[HTSlib]], `bgzip(1)` (BGZF blocks of less than 64K, compatible with gzip) and `tabix(1)` (position-sorted bgzip input, `.tbi` or `.csi`, presets, 1-based query regions, 512 Mbp limit of TBI and BAI, retrieval over the network).
[^igv]: [[Integrative Genomics Viewer]], desktop documentation, "Loading and removing tracks" (index files for indexed formats; byte-range requests for remote files).
