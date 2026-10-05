---
aliases:
  - Bash Script
  - Shell Scripting
  - Strict Mode
  - Script shell
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Unix Shell]]"
  - "[[Unix Text Processing]]"
related:
  - "[[Command-Line Interface]]"
  - "[[Process (Computing)]]"
  - "[[Workflow Management System]]"
  - "[[Defensive Programming]]"
  - "[[Reproducibility]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[GNU Bash Reference Manual]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[Bioinformatics Data Skills (Buffalo)]]"
  - "[[Research Software Engineering with Python (Irving)]]"
---

# Shell Script

> [!abstract]
> A shell script is a file of shell commands run as a program; written in strict mode (`set -euo pipefail`), with quoted expansions and checked arguments, it stops loudly at the first error instead of producing plausible garbage.

## Definition

A **shell script** is a text file of shell commands executed by the interpreter named on its first line, the shebang (`#!/usr/bin/env bash`). It receives its arguments as `$1`, `$2`, ... (all of them, each kept intact, as `"$@"`), and its exit status is that of the last command it ran or the value given to `exit`.[^ms20tools][^bash]

## Why it matters

- A script records the exact commands of an analysis, can be versioned ([[Version Control]]) and rerun on new data: the first step of [[Reproducibility]].[^buffalo][^irving]
- By default bash continues after a failed command. The script then produces empty or truncated outputs that look valid, and the next step, a Makefile or a [[Workflow Management System]] trusts its exit status ([[Command-Line Interface]]).[^buffalo]

## Core (L1)

**Strict mode.** `set -euo pipefail` on the line after the shebang. `-e` exits when a command fails (with exceptions, see Deeper); `-u` makes expanding an unset variable an error; `-o pipefail` gives a pipeline the status of its last command to fail, or zero if all succeed.[^bashset] An invented script with a missing input and a typo:

```bash
#!/usr/bin/env bash
mkdir -p results
zcat missing.fq.gz | wc -l > results/n_lines.txt
echo "lines: $(cat "$reslts/n_lines.txt")"     # typo: reslts
echo "finished"
```

```console
$ bash naive.sh; echo "exit=$?"
gzip: missing.fq.gz: No such file or directory
cat: /n_lines.txt: No such file or directory
lines: 
finished
exit=0
$ bash strict.sh; echo "exit=$?"
gzip: missing.fq.gz: No such file or directory
exit=1
```

`strict.sh` is the same file with `set -euo pipefail` on line 2: it stops at the failed pipeline, whereas the naive one lets two errors scroll by and reports success.

**Loops and quoting.** Loop over a glob, never over `$(ls ...)`, and quote the variable. In a directory holding `sample 1.fq.gz` and `sample2.fq.gz`, `for f in $(ls *.fq.gz)` iterates over `sample`, `1.fq.gz` and `sample2.fq.gz`; `for f in *.fq.gz` over the two real names. A glob that matches nothing stays literal (`for f in *.bam` printed `processing *.bam`) unless `shopt -s nullglob` is set.[^bashexp]

**Arguments.** `${THREADS:-4}` substitutes a default; `${1:?usage: script IN.fq.gz}` aborts with that message when the argument is missing; an array keeps multi-word options intact: with `opts=(--min-len 50 --out "my results.tsv")`, `tool "${opts[@]}"` receives four arguments, the last being `my results.tsv`.[^bash]

**`xargs`** builds command lines from its input, splitting on blanks: `find . -name '*.fq.gz' | xargs -n 1 echo` turned `./sample 1.fq.gz` into `./sample` and `1.fq.gz`. With `find ... -print0 | xargs -0`, names are separated by NUL bytes, which no path contains, and `-P` runs several commands at once:[^buffalo] `printf '%s\0' *.fq.gz | xargs -0 -n 1 -P 2 bash -c 'printf "%s\t%d\n" "$1" "$(zcat -- "$1" | wc -l)"' _ | sort` printed `sample 1.fq.gz` with 4 lines and `sample2.fq.gz` with 8. Outputs arrive in completion order, hence the final `sort`.

## Deeper (L2)

**Where `set -e` does not stop.** The shell does not exit for a failure in the condition of `if`, `while` or `until`, in a command of a `&&` or `||` list except the last, in a pipeline stage but the last (unless `pipefail`), or in a command negated with `!`.[^bashset] This reaches into functions called in such a context, and a command substitution counts only when its status becomes the command's:

```bash
set -euo pipefail
check() { false; echo "check: continued after false"; }
check || echo "check reported failure"
f() { local n=$(false); echo "f: local masked the failure"; }
f
g() { local n; n=$(false); echo "g: never printed"; }
g
echo "not reached"
```

Output: `check: continued after false`, `f: local masked the failure`, then exit status 1 inside `g`. In `check`, `false` runs in the context of `||`; in `f`, the status of `local` (0) hides that of `$(false)`; in `g`, the plain assignment carries the failure. Likewise, in the strict version of the typo script fixed to read `reads.fq.gz`, `$reslts` inside `echo "lines: $(cat ...)"` printed `reslts: unbound variable`, yet the script went on to `finished` with status 0: only the subshell died. Assign substitutions to variables first (Exercise 2).

**`pipefail` and early readers.** When a reader stops early, the writer dies of `SIGPIPE`, status 141 ([[Process (Computing)]]). Under `pipefail`, `yes ACGT | head -n 1` returns 141, whereas `zcat reads.fq.gz | head -n 1` returned 0 in three runs on the 4-read toy file, because `zcat` finished writing before `head` exited: the same line fails only on large files. Accept exactly that case:

```bash
zcat reads.fq.gz | head -n 4 > first.fq || { s=("${PIPESTATUS[@]}"); [[ ${s[0]} == 141 && ${s[1]} == 0 ]] || exit 1; }
```

Under `set -euo pipefail`, this line and its `yes ACGT` variant both completed and wrote 4 lines.

**Outputs that cannot lie.** Write to `out.part` and rename it to `out` as the last step: a crash leaves a file that announces itself as incomplete, never a truncated file under the final name ([[File System]]). A `trap '...' ERR` reports the failing line; cleanup of temporary files belongs in a `trap '...' EXIT`, which runs however the script ends.[^bash]

## Mathematical representation

Exit statuses form a Boolean algebra with 0 as true: `a && b` succeeds iff both do and `a || b` iff either does, `b` running only when needed (`false && echo a; echo $?` prints 1; `true || echo b; echo $?` prints 0). With `pipefail`, a pipeline succeeds iff every stage does.[^bashset]

## Computational representation

The script below applies all the Core and Deeper rules (strict mode, usage check, quoted loop, `.part` output, `ERR` trap). Calling it from Python with `subprocess.run(..., check=True)` is covered in [[Process (Computing)]].

```bash
#!/usr/bin/env bash
# Count reads and bases in gzipped FASTQ files; write one TSV row per file.
set -euo pipefail
trap 'echo "${0##*/}: command failed on line $LINENO" >&2' ERR

usage() { echo "usage: ${0##*/} OUT.tsv FILE.fq.gz..." >&2; exit 2; }
(( $# >= 2 )) || usage
out=$1; shift

part="$out.part"                     # an incomplete output keeps a telltale name
printf 'file\treads\tbases\n' > "$part"
for fq in "$@"; do
  zcat -- "$fq" | awk -v f="$fq" -v OFS='\t' '
    NR % 4 == 2 { n++; b += length($0) }
    END { if (NR % 4) { print f ": truncated record" > "/dev/stderr"; exit 1 }
          print f, n + 0, b + 0 }' >> "$part"
done
mv -- "$part" "$out"                 # the final name appears only when complete
```

## Worked example

> [!example] Running `count_reads.sh` on good and bad inputs (invented FASTQ files)
> ```console
> $ bash count_reads.sh counts.tsv sample_*.fq.gz; echo "exit=$?"; cat counts.tsv
> exit=0
> file	reads	bases
> sample_A.fq.gz	4	32
> sample_B.fq.gz	2	10
> $ bash count_reads.sh counts2.tsv sample_A.fq.gz broken.fq.gz; echo "exit=$?"; ls counts2.tsv*
> broken.fq.gz: truncated record
> count_reads.sh: command failed on line 13
> exit=1
> counts2.tsv.part
> $ bash count_reads.sh; echo "exit=$?"
> usage: count_reads.sh OUT.tsv FILE.fq.gz...
> exit=2
> ```
>
> `broken.fq.gz` stops in the middle of a record: `awk` detects that the line count is not a multiple of 4 and exits 1, `pipefail` makes the pipeline fail, `set -e` stops the script, and the `ERR` trap names line 13. A missing file gives the same pattern with `gzip: nope.fq.gz: No such file or directory`. No `counts2.tsv` exists, only the telltale `.part`; usage errors return 2, data errors 1.

## Common misconceptions

> [!warning] "`set -e` makes every failure fatal"
> Not in conditions, `&&`/`||` lists, negations, non-final pipeline stages without `pipefail`, `local x=$(...)`, or substitutions inside arguments.

> [!warning] "A `pipefail` failure is always a real error"
> Status 141 from a writer whose reader (`head`) exited early is expected, and it appears only when the input is large enough.

## Exercises

> [!question] Exercise 1 (L1)
> Run on `data/sample 1.fq.gz` and `data/sample2.fq.gz`, this script printed two `gzip: ... No such file or directory` errors, wrote `0`, `0`, `8` and exited 0. List its bugs and fix it.
>
> ```bash
> #!/bin/bash
> out=$1
> for f in $(ls data/*.fq.gz); do
>   zcat $f | wc -l >> $out
> done
> ```

> [!success]- Solution
> No strict mode; `$(ls)` splits `sample 1.fq.gz` in two; unquoted `$f` and `$out`; no file names in the output; `>>` appends to earlier runs' results; no argument check. Fixed:
>
> ```bash
> #!/usr/bin/env bash
> set -euo pipefail
> out=${1:?usage: fixed.sh OUT.tsv}
> for f in data/*.fq.gz; do
>   printf '%s\t%d\n' "$f" "$(zcat -- "$f" | wc -l)"
> done > "$out.part"
> mv -- "$out.part" "$out"
> ```
>
> It writes `data/sample 1.fq.gz` with 16 lines and `data/sample2.fq.gz` with 8, and exits 0.

> [!question] Exercise 2 (L2)
> Under `set -euo pipefail`, does a script stop at `echo "n=$(zcat missing.fq.gz | wc -l)"`? At `n=$(zcat missing.fq.gz | wc -l)`?

> [!success]- Solution
> The first prints `n=0` and continues: the status that counts is `echo`'s. The second stops with status 1: a plain assignment takes the status of its command substitution, which `pipefail` makes 1. Rule: assign first, then use the variable.

> [!question] Exercise 3 (L2)
> You run `count_reads.sh` on 100 files with `xargs -P 8`, one file per call, all with the output `counts.tsv`. What breaks, and what is the safe design?

> [!success]- Solution
> Every call renames its own `counts.tsv.part` over `counts.tsv`, so only the last finisher survives; appending to one shared file instead would interleave rows in completion order. Give each call its own output (`counts/<sample>.tsv`), then concatenate in a fixed order once all have succeeded, checking the exit status of `xargs` itself. Past this point, a [[Workflow Management System]] is the better tool.

## Mastery checklist

- [ ] 1 Recognized: I can explain what the shebang and `set -euo pipefail` do.
- [ ] 2 Understood: I know the contexts in which `set -e` does not exit, and why status 141 appears.
- [ ] 3 Practiced: I write scripts with argument checks, quoted loops over globs, `xargs -0`, `.part` outputs and an `ERR` trap.
- [ ] 4 Applied: the per-sample steps of [[10-genomic-pipeline]] are strict-mode scripts, and a failure stops the run.
- [ ] 5 Explained: I can teach the exceptions to `set -e`, the `pipefail` and `SIGPIPE` interaction, and when to move from a script to a workflow manager.

## References

[^bash]: [[GNU Bash Reference Manual]] (positional parameters, `${var:-default}` and `${var:?message}`, arrays, `trap`).
[^bashset]: [[GNU Bash Reference Manual]], "The Set Builtin" (`-e` and its exceptions, `-u`, `pipefail`).
[^bashexp]: [[GNU Bash Reference Manual]], "Shell Expansions" (filename expansion, `nullglob`).
[^ms20tools]: [[MIT - The Missing Semester of Your CS Education]], earlier (2020) edition, lecture "Shell Tools and Scripting".
[^buffalo]: [[Bioinformatics Data Skills (Buffalo)]], robust Bash scripts, `find` and `xargs`.
[^irving]: [[Research Software Engineering with Python (Irving)]], shell scripts as reusable tools.
