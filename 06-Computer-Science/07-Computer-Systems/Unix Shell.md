---
aliases:
  - Bash
  - Shell
  - Command Line
  - Bourne-Again Shell
  - Shell Unix
  - Interpréteur de commandes
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites: []
related:
  - "[[Command-Line Interface]]"
  - "[[File System]]"
  - "[[Unix Text Processing]]"
  - "[[Shell Script]]"
  - "[[Process (Computing)]]"
  - "[[Secure Shell]]"
  - "[[Workflow Management System]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[GNU Bash Reference Manual]]"
  - "[[GNU Coreutils Manual]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[Bioinformatics Data Skills (Buffalo)]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[HPC Carpentry - Introduction to High-Performance Computing]]"
  - "[[Python Documentation]]"
---

# Unix Shell

> [!abstract]
> The shell reads your command line, expands it into words, starts programs and wires their standard streams to files and to each other: the glue that turns single-purpose tools into pipelines over files too large to open.

## Definition

A **Unix shell** is a command language interpreter: it reads commands from a terminal or a file, expands them (variables, globs, command substitution), runs the resulting programs and connects their input and output through redirections and pipes.[^bash] **Bash**, the "Bourne-Again SHell", is the GNU Project's shell, largely compatible with the Bourne shell `sh`; it is the shell used in this vault.[^bash]

## Why it matters

- **Servers have no desktop.** Clusters are reached through a remote shell ([[Secure Shell]]),[^hpc] and the tools are command-line programs that read files or stdin and write stdout; genomics courses teach this stack as a unit.[^buffalo][^jhu]
- **Streaming.** `zcat reads.fq.gz | head -n 4` prints the first read of a FASTQ file of any size at once; pipelines need no intermediate files.[^buffalo]
- **Every workflow step is a shell command**, so quoting and exit-status rules also apply inside [[Shell Script|scripts]] and a [[Workflow Management System]] ([[Command-Line Interface]]).

## Core (L1)

Navigation (`cd`, `ls`, `pwd`, `less`, `man`) is assumed.[^ms26] All files below are invented toy data: a 3-record FASTA, a 4-read FASTQ, small BED, GFF3 and VCF files.

**Streams and redirection.** Every process starts with standard input (file descriptor 0), standard output (1) and standard error (2). The shell sets up redirections before the command runs, from left to right:[^bash][^ms20tools] `> f` (stdout to `f`, truncating it), `>> f` (append), `2> f` (stderr), `< f` (stdin), `> f 2>&1` (both: stderr joins stdout's *current* target), `a | b` (stdout of `a` into stdin of `b`).

```console
$ ls toy.fa missing.fa > out.txt 2> err.txt; echo "status=$?"; cat out.txt err.txt
status=2
toy.fa
ls: cannot access 'missing.fa': No such file or directory
$ ls toy.fa missing.fa 2>&1 > only.txt; cat only.txt
ls: cannot access 'missing.fa': No such file or directory
toy.fa
```

In the second command `2>&1` points stderr at the terminal, where stdout points at that moment; then stdout moves to `only.txt`.

**Pipes.** Each stage reads the previous one's output as it is produced (the tools are the subject of [[Unix Text Processing]], the format of [[FASTQ Format]]):

```mermaid
flowchart LR
    F[("reads.fq.gz")] --> Z["zcat"] -- "4 lines per read" --> A["awk: length of line 2"] -- "one number per read" --> S["sort -n"] --> U["uniq -c"]
```

```console
$ zcat reads.fq.gz | awk 'NR % 4 == 2 {print length($0)}' | sort -n | uniq -c
      1 4
      1 8
      2 10
```

**Globs.** The shell replaces `*` (any string), `?` (one character) and `[...]` (one character of a set) by the alphabetically sorted matching file names before the command runs; a pattern that matches nothing is left unchanged, and a leading `.` must be matched explicitly. Brace expansion (`{a,b}`, `{1..3}`) generates words whether or not the files exist.[^bashexp]

```console
$ echo sample_*.fq.gz; echo sample_?.fq.gz; echo sample_{1..3}.fq.gz; echo *.bam
sample_1.fq.gz sample_10.fq.gz sample_2.fq.gz
sample_1.fq.gz sample_2.fq.gz
sample_1.fq.gz sample_2.fq.gz sample_3.fq.gz
*.bam
```

The order is lexicographic, `sample_3.fq.gz` does not exist, and `*.bam` reached `echo` literally. Globs are not [[Regular Expression|regular expressions]].

**Quoting.** Single quotes keep every character literal; double quotes keep spaces but expand `$variables` and `$(commands)`; an unquoted expansion is split into words and globbed.[^ms20tools][^bashexp]

```console
$ f="my reads.fq"; printf "@x\nACGT\n+\nIIII\n" > "$f"; wc -l $f; wc -l "$f"; echo '$f' "= $f"
wc: my: No such file or directory
16 reads.fq
16 total
4 my reads.fq
$f = my reads.fq
```

Unquoted, `$f` became two arguments: `wc` failed on `my` and silently counted an unrelated file called `reads.fq`. Quote every expansion.

**Exit status.** Every command returns a status, 0 for success and nonzero for failure, readable in `$?`; `a && b` runs `b` only if `a` succeeded, `a || b` only if it failed.[^bashexit][^ms20tools] `grep -q '^>seq9' toy.fa || echo "absent (status $?)"` prints `absent (status 1)`.

## Deeper (L2)

**Order of expansions.** Brace expansion; tilde expansion; parameter, variable and arithmetic expansion, command and process substitution (left to right); word splitting; filename expansion; quote removal.[^bashexp] A variable's value is therefore split and globbed *after* substitution unless quoted: with `pattern='*.fa'`, `echo $pattern` prints `toy.fa` and `echo "$pattern"` prints `*.fa`.

**Command and process substitution.** `$(cmd)` is replaced by the output of `cmd`, as in `n=$(zcat reads.fq.gz | wc -l)`. `<(cmd)` runs `cmd` and is replaced by a file name connected to its output (such as `/dev/fd/63`), for tools that accept only paths;[^bashexp][^buffalo] here, BED gene names absent from the GFF3 file ([[GFF Format]]):

```console
$ comm -23 <(cut -f4 genes.bed | sort) <(awk -F'\t' '$3 == "gene" {sub(/^ID=/, "", $9); print $9}' ann.gff3 | sort)
geneC
geneD
geneE
```

**Grouping and pipeline status.** `{ printf '#chrom\tstart\tend\n'; sort -k1,1 -k2,2n genes.bed; } > sorted.bed` sends a header and the sorted data through one redirection. A pipeline's status is that of its last command unless `pipefail` is set; the array `PIPESTATUS` keeps every stage's status, and [[Shell Script]] shows how `set -o pipefail` exposes the hidden failure:[^bash][^bashset]

```console
$ zcat missing.fq.gz | wc -l; echo "status=$? PIPESTATUS=${PIPESTATUS[*]}"
gzip: missing.fq.gz: No such file or directory
0
status=0 PIPESTATUS=1 0
```

## Advanced (L3)

Each command of a multi-command pipeline runs in its own subshell, a separate [[Process (Computing)|process]], and all stages run at once, connected by pipes.[^bash] Three consequences:

1. **Variables assigned inside a pipeline are lost**; feed the loop by redirection instead:

   ```console
   $ n=0; grep '^>' toy.fa | while read -r h; do n=$((n+1)); done; echo "after pipe: n=$n"
   after pipe: n=0
   $ n=0; while read -r h; do n=$((n+1)); done < <(grep '^>' toy.fa); echo "after process substitution: n=$n"
   after process substitution: n=3
   ```

2. **Memory stays bounded** for line-by-line stages, whatever the file size. `sort` is the exception: its last input line may be its first output line, so it must consume everything first ([[Unix Text Processing]]).
3. **Stages run in parallel and stop together.** When `head` exits, the writer upstream is killed by `SIGPIPE` at its next write: `yes ACGT | head -n 2; echo "${PIPESTATUS[*]}"` prints two lines, then `141 0`, and 141 is 128 + 13, the number of `SIGPIPE`.[^bashexit]

**Named pipes.** `mkfifo reads.fifo` creates a file-system entry that behaves like `|`, for programs that insist on a path (`zcat reads.fq.gz > reads.fifo & wc -l reads.fifo` printed `16 reads.fifo`).[^buffalo] No pipe can be rewound, so a program that seeks back in its input needs a regular file (Exercise 4).

**Where the shell stops.** Bash arithmetic uses fixed-width integers and its variables are strings or arrays of strings.[^bash] Parsing and statistics belong in a [[Python Programming|Python]] tool that reads stdin and writes stdout ([[Command-Line Interface]]); a dependency graph over many samples belongs in a [[Workflow Management System]].

## Mathematical representation

With $\Sigma$ the set of bytes and each stage a function $f_i : \Sigma^* \to \Sigma^*$, the pipeline `f1 | f2 | f3` computes $f_3 \circ f_2 \circ f_1$. A **line-local** stage (plain `grep`, `cut`, a per-line `awk`) satisfies $f(xy) = f(x)\,f(y)$ whenever $x$ ends at a line boundary: it streams in constant memory, and its input can be split into chunks processed independently and concatenated ([[Parallel Computing]]). `sort` is not line-local.

## Computational representation

The Core pipeline in Python ([[File Input and Output]], [[Iterator]]), checked against the shell:

```python
import gzip
import subprocess
from collections import Counter

def read_lengths(path):
    """Yield the length of each read of a gzipped FASTQ file, streaming."""
    with gzip.open(path, "rt", encoding="ascii") as fh:
        for i, line in enumerate(fh):
            if i % 4 == 1:                     # line 2 of each 4-line record
                yield len(line.rstrip("\n"))

py = Counter(read_lengths("reads.fq.gz"))
cmd = "zcat reads.fq.gz | awk 'NR % 4 == 2 {print length($0)}' | sort -n | uniq -c"
out = subprocess.run(["bash", "-o", "pipefail", "-c", cmd],
                     check=True, capture_output=True, text=True).stdout
sh = {int(length): int(n) for n, length in map(str.split, out.splitlines())}
print(sorted(py.items()), sh == py)
```

Output: `[(4, 1), (8, 1), (10, 2)] True`. With `-o pipefail` and `check=True`, a failure in any stage raises `CalledProcessError` instead of returning partial output.[^pydoc]

## Worked example

> [!example] First look at a delivery of sequencing files (invented)
> `sample_A.fq.gz` (4 reads) and `sample_B.fq.gz` (2 reads) arrive. Reads per file use a glob, a quoted loop variable, command substitution inside arithmetic expansion, and a log for errors; totals use one stream, since `zcat` concatenates files and each holds a multiple of 4 lines:
>
> ```console
> $ for f in sample_*.fq.gz; do
>   printf "%s\t%d\n" "$f" $(( $(zcat "$f" | wc -l) / 4 ))
> done > read_counts.tsv 2> read_counts.log
> cat read_counts.tsv; echo "log lines: $(wc -l < read_counts.log)"
> sample_A.fq.gz	4
> sample_B.fq.gz	2
> log lines: 0
> $ zcat sample_*.fq.gz | awk 'NR % 4 == 2 {n += length($0)} END {print NR / 4, "reads", n, "bases"}'
> 6 reads 42 bases
> ```
>
> Check by hand: 4 + 2 = 6 reads; 8 + 10 + 4 + 10 + 5 + 5 = 42 bases. The empty log shows that every file decompressed.

## Common misconceptions

> [!warning] "`cmd > out 2>&1` and `cmd 2>&1 > out` are the same"
> Redirections apply left to right; only the first form sends both streams to `out`.

> [!warning] "`sort genes.bed > genes.bed` sorts in place"
> The shell truncates `genes.bed` before `sort` starts: the data are lost (Exercise 2).

> [!warning] "A glob that matches nothing expands to nothing"
> The pattern is passed on literally, and a loop runs once on a file that does not exist ([[Shell Script]] shows `nullglob`).

## Exercises

> [!question] Exercise 1 (L1)
> List `sample_1.fq.gz`, `sample_2.fq.gz` and `sample_10.fq.gz` in numeric order, and write a glob matching only the single-digit samples.

> [!success]- Solution
> `printf "%s\n" sample_*.fq.gz | sort -V` prints `sample_1`, `sample_2`, `sample_10` (GNU `sort -V` compares embedded numbers; the glob itself sorts lexicographically). `sample_?.fq.gz` matches exactly one character after the underscore.

> [!question] Exercise 2 (L1)
> Starting from two copies of the 5-line `genes.bed`, explain the outputs `0` and `5` of `sort g1.bed > g1.bed; wc -l < g1.bed; sort -o g2.bed g2.bed; wc -l < g2.bed`.

> [!success]- Solution
> `> g1.bed` is a redirection: the shell truncates `g1.bed` before starting `sort`, which reads an empty file. With `-o`, `sort` opens the output file itself, after reading its input.[^cusort] For any other tool: `tool in > in.tmp && mv in.tmp in`.

> [!question] Exercise 3 (L2)
> With `src="raw data"`, explain why `cp $src/*.fq.gz "$dest"` fails, and fix it.

> [!success]- Solution
> Parameter expansion gives `raw data/*.fq.gz`; word splitting then cuts it into `raw` and `data/*.fq.gz`; filename expansion finds no `data/` and leaves the second word literal. `cp` reports `cannot stat 'raw'` and `cannot stat 'data/*.fq.gz'` and exits 1. The fix, `cp "$src"/*.fq.gz "$dest"`, quotes the variable and leaves the glob outside the quotes, so it is still expanded (it copied `x.fq.gz`).

> [!question] Exercise 4 (L3, Python)
> Show that a program reading its input twice works on `toy.fa` but not on `<(cat toy.fa)`. What does this imply for indexers?

> [!success]- Solution
> `python3 -c 'import sys; f = open(sys.argv[1], "rb"); f.read(); f.seek(0); print(len(f.read()))' toy.fa` prints `73`; with `<(cat toy.fa)` as argument it ends with `io.UnsupportedOperation: File or stream is not seekable.` `<(...)` passes a path such as `/dev/fd/63`, but behind it is a pipe: bytes are read once, in order. Streaming tools accept pipes; a tool that seeks (to index, to make two passes) needs a regular file for that step.

## Mastery checklist

- [ ] 1 Recognized: I can name stdin, stdout and stderr, and read a pipeline with redirections.
- [ ] 2 Understood: I can explain redirection order, globbing, quoting and the order of expansions.
- [ ] 3 Practiced: I write pipelines with process substitution and `PIPESTATUS`, and predict their outputs.
- [ ] 4 Applied: I summarize real gzipped FASTQ, BED and VCF files on a server without decompressing them to disk, for [[10-genomic-pipeline]].
- [ ] 5 Explained: I can teach why pipelines stream in bounded memory, where status 141 comes from, and when to leave the shell for Python or a workflow manager.

## References

[^bash]: [[GNU Bash Reference Manual]] (description of Bash; pipelines, redirections, arrays, arithmetic).
[^bashexp]: [[GNU Bash Reference Manual]], "Shell Expansions" (order of expansions, process substitution, word splitting, filename expansion).
[^bashexit]: [[GNU Bash Reference Manual]], "Exit Status" (0 is success; 128 + N after fatal signal N).
[^bashset]: [[GNU Bash Reference Manual]], "The Set Builtin" (`pipefail`).
[^cusort]: [[GNU Coreutils Manual]], "sort invocation" (`-o`).
[^ms26]: [[MIT - The Missing Semester of Your CS Education]], 2026 lectures "Course Overview + Introduction to the Shell" and "Command-line Environment".
[^ms20tools]: [[MIT - The Missing Semester of Your CS Education]], earlier (2020) edition, lecture "Shell Tools and Scripting".
[^buffalo]: [[Bioinformatics Data Skills (Buffalo)]], Unix pipelines and shell techniques on bioinformatics files.
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]], course "Command Line Tools for Genomic Data Science".
[^hpc]: [[HPC Carpentry - Introduction to High-Performance Computing]], episode "Connecting to a remote HPC system".
[^pydoc]: [[Python Documentation]], `subprocess` module.
