---
aliases:
  - Unix Data Tools
  - Command-Line Text Processing
  - One-liner
  - awk
  - sed
  - Traitement de texte en ligne de commande
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Unix Shell]]"
  - "[[Regular Expression]]"
  - "[[Delimited Text Format]]"
related:
  - "[[FASTA Format]]"
  - "[[FASTQ Format]]"
  - "[[BED Format]]"
  - "[[GFF Format]]"
  - "[[VCF Format]]"
  - "[[Genomic Coordinate System]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Bioinformatics Data Skills (Buffalo)]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[GNU Coreutils Manual]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[GA4GH hts-specs]]"
---

# Unix Text Processing

> [!abstract]
> A handful of line filters (`grep`, `cut`, `sort`, `uniq`, `join`, `awk`, `sed`) chained in pipelines answer most quick questions about FASTA, FASTQ, BED, GFF and VCF files in one streaming pass, without loading them into memory; the skill lies in knowing their silent failure modes.

## Definition

The Unix text-processing utilities are **filters over lines**: `grep` selects lines matching a pattern, `cut` selects fields, `sort` orders lines by keys, `uniq` collapses adjacent duplicates, `join` merges two files sorted on a common key, `awk` is a small language over records and fields, and `sed` applies editing commands to a stream.[^ms20wrangle][^buffalo] Each reads files or standard input and writes standard output, so they compose in [[Unix Shell|pipelines]].

## Why it matters

- Most bioinformatics files are line-oriented text ([[FASTA Format]], [[FASTQ Format]], [[BED Format]], [[GFF Format]], [[VCF Format]]); one-liners answer "how many, which, where" in seconds, streaming from gzip.[^buffalo][^jhu]
- They are the sanity checks of a pipeline (records in versus records out, chromosomes present, filters applied), available on every server without installing anything ([[10-genomic-pipeline]]).

## Core (L1)

| Tool | Does | Bioinformatics example |
|---|---|---|
| `grep` | select or count lines matching a [[Regular Expression]] | `grep -c '^>'` counts FASTA records; `grep -v '^#'` drops VCF headers |
| `cut` | select fields, TAB-separated by default[^cu] | `cut -f1,4` of a BED or GFF |
| `sort` | order lines by keys | `sort -k1,1 -k2,2n` orders BED intervals |
| `uniq -c` | collapse **adjacent** identical lines, counting them | frequencies, after `sort` |
| `join` | merge two files on a key | add sample metadata to counts |
| `awk` | filter and compute on fields | `awk -F'\t' '$7 == "PASS"'` |
| `sed` | edit a stream | `sed '/^#/!s/^chr//'` strips `chr` from data lines only |

All examples use invented toy files (a 3-record FASTA, a 4-read FASTQ, 5-line BED, GFF3 and VCF files).

**Counting records.** FASTA records are header lines; FASTQ records are blocks of exactly four lines, so count lines and divide:

```console
$ grep -c '^>' toy.fa; grep -c '^@' reads.fq; awk 'END {print NR / 4}' reads.fq
3
5
4
```

`grep -c '^@'` says 5 because read `r3` has the quality string `@@@@`: `@` is a valid quality character ([[FASTQ Format]]).

**Frequencies: `sort | uniq -c`.** PASS variants per chromosome of a VCF:

```console
$ grep -v '^#' calls.vcf | awk -F'\t' '$7 == "PASS"' | cut -f1 | LC_ALL=C sort | uniq -c
      1 chr1
      1 chr10
      2 chr2
```

**Four rules against silent errors.**

1. `cut` keeps the file's column order (`cut -f3,1` prints field 1 then field 3); reorder with `awk -F'\t' -v OFS='\t' '{print $3, $1}'`.
2. `uniq` merges only adjacent lines: `printf 'chr1\nchr2\nchr1\n' | uniq -c` reports `chr1` twice, once per run. Sort first.[^cuuniq]
3. `sort -k1` uses a key from field 1 **to the end of the line**, compared as text: `printf 'chr1\t300\nchr1\t1000\n' | LC_ALL=C sort -k1 -k2n` puts `1000` before `300`, since `1` < `3`, and never reaches the second key. Close every key: `sort -k1,1 -k2,2n`, the standard order for BED files.[^cusort]
4. Patterns match substrings: `grep -c chr1 genes.bed` gives 3 because `chr10` contains `chr1`; `grep -cw chr1` and `awk -F'\t' '$1 == "chr1"'` give the correct 2.

## Deeper (L2)

**Locale.** `sort` orders lines according to the current locale; for byte order, reproducible across machines, set `LC_ALL=C` (`names.txt` holds six invented names):[^cusort]

```console
$ LC_ALL=en_US.UTF-8 sort names.txt | paste -s -d ' '; LC_ALL=C sort names.txt | paste -s -d ' '
chr1 chr10 chr2 Chr3 chrX _x
Chr3 _x chr1 chr10 chr2 chrX
```

The same file sorts differently on a laptop and on a cluster with another locale. Tools that require sorted input compare with their own collation, so sort and consume under the same `LC_ALL`.

**`join` needs sorted inputs.** Both files must be sorted on the join field; here `samples.tsv` (sample, condition) and `counts.tsv` (sample, reads) are not:[^cujoin]

```console
$ join -t $'\t' samples.tsv counts.tsv; echo "status=$?"
join: samples.tsv:3: is not sorted: S1	control
join: counts.tsv:3: is not sorted: S10	7
S2	treated	2
join: input is not in sorted order
status=1
$ export LC_ALL=C; join -t $'\t' <(sort -k1,1 samples.tsv) <(sort -k1,1 counts.tsv)
S1	control	4
S10	control	7
S2	treated	2
```

Unsorted, two of three samples vanished from the output; only stderr and the exit status reveal it.

**Counting without sorting.** An `awk` associative array is a [[Hash Table]]: one pass, memory proportional to the number of distinct keys. `awk -F'\t' '!/^#/ && $7 == "PASS" {n[$1]++} END {for (c in n) print n[c], c}' calls.vcf` gives the same three counts as above, in arbitrary order. `sort` must hold or spill all its input: it writes temporary files (`-T` chooses their directory, `-S` the buffer size) and can use several threads (`--parallel`).[^cusort]

**Compressed streams.** `zcat file.gz | ...` feeds any filter. Concatenated gzip files decompress as one stream (`cat reads.fq.gz reads.fq.gz | zcat | wc -l` prints 32), so per-lane FASTQ files can be merged without recompression; BGZF files (BAM, indexed VCF) are such concatenations ([[File Input and Output]]).

**Records that span lines.** `paste - - - -` turns each 4-line FASTQ record into one TAB-separated line, so line tools see whole reads, and `tr '\t' '\n'` restores the format: `zcat reads.fq.gz | paste - - - - | awk -F'\t' 'length($2) >= 8' | cut -f1` prints `@r1`, `@r2`, `@r4`, the reads of at least 8 bases. Multi-line FASTA needs a small state machine instead (Exercise 3).

## Advanced (L3)

**Measure the locale cost.** On this machine (4 cores, GNU sort 9.4), sorting 2,000,000 invented lines `chrN<TAB>position` took 3.2 to 3.5 s under `LC_ALL=en_US.UTF-8` and 1.0 to 1.1 s under `LC_ALL=C` (`time LC_ALL=... sort big.tsv > /dev/null`, three runs each). Byte comparison skips the collation rules: faster and reproducible.

**Line tools do not know formats.** They see lines and fields, not records: a VCF `ALT` may list several alleles separated by commas, so `length($5) == 1` misclassifies `A,G`;[^hts] a CSV field may contain a quoted delimiter that `cut -d,` splits ([[Delimited Text Format]]). When the answer depends on the format's semantics, use a format-aware tool (samtools, bcftools, bedtools) or a parser; keep one-liners for counts, simple filters and sanity checks.

**Scale.** Filters are line-local, so a large file can be split (by chromosome, or by line ranges cut at record boundaries) and processed in parallel ([[Parallel Computing]]); only the final merge needs sorted pieces, which `sort -m` merges without re-sorting.[^cusort]

## Mathematical representation

For lines $\ell_1, \dots, \ell_n$, `sort | uniq -c` computes the count function $c(x) = |\{\, i : \ell_i = x \,\}|$ over the distinct lines $x$. With $k$ distinct keys, and $m$ lines in the second file of a `join`:

| Operation | Time | Memory |
|---|---|---|
| `grep`, `cut`, per-line `awk` | $O(n)$ | $O(1)$ |
| `sort` | $O(n \log n)$ comparisons | bounded buffer plus temporary files |
| `uniq -c` on sorted input; `join` of sorted files | $O(n)$; $O(n + m)$ | $O(1)$ |
| `awk` counting with an array | $O(n)$ expected | $O(k)$ |

The algorithms behind them are in [[Sorting]] and [[Hash Table]].

## Computational representation

The Worked example's question in Python: one pass, a `Counter` keyed by (chromosome, type), sorted by code point as under `LC_ALL=C`:

```python
from collections import Counter

def variant_summary(path):
    """Count PASS variants per (chromosome, SNV or indel) in a VCF, one line at a time."""
    counts = Counter()
    with open(path, encoding="ascii") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            chrom, _pos, _id, ref, alt, _qual, filt, *_ = line.rstrip("\n").split("\t")
            if filt == "PASS":
                kind = "SNV" if len(ref) == 1 and len(alt) == 1 else "indel"
                counts[chrom, kind] += 1
    return counts

for (chrom, kind), n in sorted(variant_summary("calls.vcf").items()):
    print(chrom, kind, n, sep="\t")
```

It prints the same four rows as the shell version below.

## Worked example

> [!example] PASS SNVs and indels per chromosome (invented VCF)
> `calls.vcf` has 5 variants, one of them `LowQual`. Classify each PASS variant by allele lengths, count (chromosome, type) pairs, and reformat:
>
> ```console
> $ grep -v '^#' calls.vcf \
>   | awk -F'\t' -v OFS='\t' '$7 == "PASS" {print $1, (length($4) == 1 && length($5) == 1) ? "SNV" : "indel"}' \
>   | LC_ALL=C sort | uniq -c \
>   | awk -v OFS='\t' '{print $2, $3, $1}'
> chr1	SNV	1
> chr10	indel	1
> chr2	SNV	1
> chr2	indel	1
> ```
>
> Check: 4 PASS rows, of which `T>TA` (insertion) and `AG>A` (deletion) are indels; `uniq -c` is safe because `sort` made equal pairs adjacent. Limit: a multi-allelic `A,G` would be called an indel.

## Common misconceptions

> [!warning] "`grep -c '^@'` counts FASTQ reads"
> Quality strings may start with `@`. Count lines and divide by 4, after checking that the line count is a multiple of 4.

> [!warning] "Sorted is sorted"
> Order depends on the keys (`-k1` versus `-k1,1`) and on the locale. A BED file sorted on a laptop may be rejected by a tool on a server.

## Exercises

> [!question] Exercise 1 (L1)
> Compute the GC fraction of all sequences in `toy.fa` with `grep`, `tr` and `wc`, counting and then excluding `N`.

> [!success]- Solution
> `grep -v '^>' toy.fa | tr -d '\n' | wc -c` gives 32 characters; `... | tr -cd 'GC' | wc -c` gives 16; `tr -cd 'ACGT'` gives 30. GC = 16/32 = 0.5 over all characters but 16/30 ≈ 0.533 over called bases: the two `N` must not be in the denominator.

> [!question] Exercise 2 (L1)
> Convert `calls.vcf` to BED (chromosome, start, end, `REF>ALT`), covering the reference bases of each variant.

> [!success]- Solution
> VCF `POS` is 1-based and BED 0-based half-open ([[Genomic Coordinate System]]): start = `POS - 1`, end = start + length of `REF`.
>
> ```console
> $ awk -F'\t' -v OFS='\t' '!/^#/ {print $1, $2 - 1, $2 - 1 + length($4), $4 ">" $5}' calls.vcf
> chr1	304	305	A>G
> chr1	419	420	C>T
> chr2	149	150	G>A
> chr2	404	405	T>TA
> chr10	59	61	AG>A
> ```
>
> The deletion `AG>A` spans two reference bases, hence 59 to 61.

> [!question] Exercise 3 (L2)
> Print the length of each record of the multi-line `toy.fa` with `awk`. Why does `grep -v '^>' toy.fa | wc -c` print 36 rather than 32?

> [!success]- Solution
> A state machine: on a header, print the previous record and reset; otherwise add the line length; print the last record at the end. `awk '/^>/ {if (id) print id "\t" len; id = substr($1, 2); len = 0; next} {len += length($0)} END {if (id) print id "\t" len}' toy.fa` prints `seq1 16`, `seq2 10` and `seq3 6` (TAB-separated). `wc -c` also counts the newline ending each of the 4 sequence lines: 32 + 4 = 36.

> [!question] Exercise 4 (L3)
> `grep -v '^#' ann.gff3 | cut -f3 | sort | uniq -c` counts feature types (2 exon, 2 gene, 1 mRNA), and so does a Python `Counter` filled in one pass. Compare their time and memory for $n$ lines and $k$ types, and say when each is preferable.

> [!success]- Solution
> The pipeline sorts all $n$ values: $O(n \log n)$ time, with temporary files beyond the buffer. The `Counter` (or an `awk` array) does $O(n)$ expected work and holds $k$ entries. With a few dozen feature types and millions of lines, hashing wins (the Python version, run on the toy file, gives `[('exon', 2), ('gene', 2), ('mRNA', 1)]`). Sorting remains right when the output must be ordered, when keys are too many to fit in RAM, or when the next step (`join`, `uniq`) needs sorted input.

## Mastery checklist

- [ ] 1 Recognized: I know what each of `grep`, `cut`, `sort`, `uniq`, `join`, `awk` and `sed` does.
- [ ] 2 Understood: I can explain adjacency in `uniq`, closed sort keys, locale collation and sorted input for `join`.
- [ ] 3 Practiced: I write one-liners that count, filter and convert FASTA, FASTQ, BED, GFF and VCF files, and check them by hand on toy data.
- [ ] 4 Applied: I run these checks on real gzipped files before and after each step of [[10-genomic-pipeline]].
- [ ] 5 Explained: I can teach the cost model of streaming versus sorting, and when a format-aware tool must replace a one-liner.

## References

[^ms20wrangle]: [[MIT - The Missing Semester of Your CS Education]], earlier (2020) edition, lecture "Data Wrangling" (`grep`, `sed`, `sort`, `uniq`, `awk`).
[^buffalo]: [[Bioinformatics Data Skills (Buffalo)]], Unix data tools applied to bioinformatics files.
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]], course "Command Line Tools for Genomic Data Science".
[^cu]: [[GNU Coreutils Manual]] (`cut`, `paste`, `tr`).
[^cusort]: [[GNU Coreutils Manual]], "sort invocation" (keys, locale, temporary files, merging).
[^cuuniq]: [[GNU Coreutils Manual]], "uniq invocation" (adjacent lines only).
[^cujoin]: [[GNU Coreutils Manual]], "join invocation" (inputs sorted on the join field).
[^hts]: [[GA4GH hts-specs]], VCF specification.
