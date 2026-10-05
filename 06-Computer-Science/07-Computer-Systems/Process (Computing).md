---
aliases:
  - Process
  - Unix Process
  - Signal (Computing)
  - Exit Code
  - Environment Variable
  - Processus
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Unix Shell]]"
  - "[[Shell Script]]"
related:
  - "[[Command-Line Interface]]"
  - "[[Concurrency]]"
  - "[[Virtual Memory]]"
  - "[[Job Scheduler]]"
  - "[[Secure Shell]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[GNU Bash Reference Manual]]"
  - "[[GNU Coreutils Manual]]"
  - "[[HPC Carpentry - Introduction to High-Performance Computing]]"
  - "[[Python Documentation]]"
---

# Process (Computing)

> [!abstract]
> A process is a running program with its own identity, memory, environment and open streams; exit statuses, signals and environment variables are how the shell, a script or a workflow manager learns what happened to it, and `nohup` or `tmux` keep it alive after you log out.

## Definition

A **process** is a running instance of a program. It has a process ID (PID) and a parent (PPID), its own memory, a current directory, open file descriptors (0, 1 and 2 are the standard streams) and an **environment**, a list of `name=value` strings given to it when it starts.[^bashenv][^ms20cle] When it ends, it returns an **exit status** between 0 and 255 to its parent, 0 meaning success; bash reports a process killed by signal $N$ as $128 + N$.[^bashexit] A **signal** is an asynchronous notification sent to a process, such as an interrupt or a request to terminate.[^ms20cle]

## Why it matters

- Alignments and assemblies run for hours: they must survive a closed laptop or a dropped [[Secure Shell|SSH]] connection or, on a cluster, go through the [[Job Scheduler]].[^ms20cle][^hpc]
- Exit statuses and signals tell a pipeline or a [[Workflow Management System]] whether a step succeeded, failed, timed out or was killed; decoding them is the first step of debugging a failed job ([[Virtual Memory]] for jobs killed for memory).
- Environment variables (`PATH`, `LC_ALL`, `TMPDIR`) silently change how programs run.[^hpcenv]

## Core (L1)

**Seeing processes.** `$$` is the shell's PID and `$!` the PID of the last job started in the background with `&`; `ps -o pid,ppid,stat,comm -p $$,$!` showed the background `sleep` (PID 16150) as a child of the shell (PID 16149).

**Exit statuses.** Values above 125 are used by the shell itself.[^bashexit] Observed in bash 5.2:

| Command | Status | Meaning |
|---|---:|---|
| `bash -c "exit 3"` | 3 | the program's own error code |
| `nosuchtool` | 127 | command not found |
| `./plain.sh` (no execute bit) | 126 | found, not executable |
| `sleep 30 & kill -TERM $!; wait $!` | 143 | 128 + 15, `SIGTERM` |
| `sleep 30 & kill -KILL $!; wait $!` | 137 | 128 + 9, `SIGKILL` |
| `timeout --preserve-status -s INT 1 sleep 30` | 130 | 128 + 2, `SIGINT` |
| `bash -c "exit 300"` | 44 | 300 mod 256 |

`kill -l 129 130 137 141 143` decodes such statuses: `HUP`, `INT`, `KILL`, `PIPE`, `TERM`.

**Signals.** Ctrl-C sends `SIGINT` to the foreground process; `kill PID` sends `SIGTERM`, a request the program may catch to clean up; `SIGKILL` (`kill -9`) cannot be caught and ends the process at once; closing the terminal sends `SIGHUP` to its jobs. Ctrl-Z suspends the foreground job; `bg` resumes it in the background, `fg` brings it back, `jobs` lists them.[^ms20cle][^bash]

**Environment variables.** A child receives a copy of the variables its parent exported; `VAR=value cmd` sets a variable for one command only; a child can never change its parent's environment.[^bashenv][^hpcenv] After `X=1`, a child shell printed `child sees X=unset`, and `child sees X=1` only after `export X`; `LC_ALL=C bash -c '...'` saw `LC_ALL=C` while the shell kept it unset; after `bash -c "export Y=2"`, `Y` was still unset in the shell.

**Keeping a long job alive.** Background jobs are children of the terminal's shell and receive `SIGHUP` when it closes. `nohup` runs a command with hangups ignored (writing to `nohup.out` if stdout is a terminal); a terminal multiplexer such as `tmux` keeps whole sessions on the server, to detach (Ctrl-b d) and reattach later (`tmux attach -t NAME`).[^ms20cle][^cunohup] After `kill -HUP` sent to a plain `sleep 30 &` and to a `nohup sleep 30 &`, the first died with status 129 and the second kept running. `tmux new-session -d -s align "for i in 1 2 3; do echo step \$i; sleep 1; done > align.log 2>&1"` ran detached, `tmux ls` listed `align: 1 window`, and the session closed by itself once `align.log` held its three lines. On a cluster, long computations belong to the [[Job Scheduler]], not to the login node.[^hpc]

## Deeper (L2)

**Catching signals.** A script can trap `SIGTERM` (sent by `kill`, `timeout`, or a scheduler at a time limit) to stop its children and report, but nothing can trap `SIGKILL`:

```bash
#!/usr/bin/env bash
# A long "alignment" that stops its child when asked to stop.
part=aln.bam.part
echo "started, writing $part" >&2
sleep 30 > "$part" & child=$!
trap 'kill "$child" 2>/dev/null; wait "$child"; echo "cleanup: child $child stopped" >&2' EXIT
trap 'echo "got SIGTERM" >&2; exit 143' TERM
wait "$child"
```

```console
$ bash job.sh & pid=$!; sleep 0.5; kill -TERM $pid; wait $pid; echo "exit=$?"
started, writing aln.bam.part
got SIGTERM
cleanup: child 16252 stopped
exit=143
$ bash job.sh & pid=$!; sleep 0.5; kill -KILL $pid; wait $pid; echo "exit=$?"; sleep 0.2; ps -o pid=,ppid=,comm= -C sleep
started, writing aln.bam.part
bash: line 1: 16258 Killed                  bash job.sh
exit=137
16260     1 sleep
```

After `SIGKILL` no trap ran: the child `sleep` survived as an orphan adopted by PID 1, and `aln.bam.part` stayed (in both runs; the `.part` name is what marks it as incomplete). Send `SIGTERM` first, `SIGKILL` only if the process does not exit.

## Mathematical representation

Bash reports $s \bmod 256$ for an explicit `exit s` ($300 \bmod 256 = 44$) and $128 + N$ for death by signal $N$. The two ranges overlap above 128, so a program that wants unambiguous statuses uses 1 to 125 for its own errors.[^bashexit]

## Computational representation

`subprocess.run` with a list of arguments starts a program without a shell; `check=True` raises `CalledProcessError` on a nonzero status, and a negative `returncode` $-N$ means death by signal $N$. A pipeline is built by connecting one `Popen`'s stdout to the next one's stdin.[^pydoc]

```python
import signal
import subprocess

r = subprocess.run(["bash", "-c", "kill -TERM $$"])            # child killed by a signal
print(r.returncode, signal.Signals(-r.returncode).name)

try:
    subprocess.run(["zcat", "missing.fq.gz"], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as err:
    print("failed:", err.returncode, err.stderr.strip())

# zcat reads.fq.gz | wc -l, without a shell
p1 = subprocess.Popen(["zcat", "reads.fq.gz"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["wc", "-l"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()                     # p1 gets SIGPIPE if p2 exits early
lines = p2.communicate()[0].strip()
print(lines, "statuses:", p1.wait(), p2.returncode)
```

Output: `-15 SIGTERM`, then `failed: 1 gzip: missing.fq.gz: No such file or directory`, then `16 statuses: 0 0`. Checking both statuses is the Python equivalent of `pipefail`. An `env={...}` argument replaces the child's whole environment (with `env={"LC_ALL": "C", "PATH": "/usr/bin:/bin"}`, `sort` returned `['B', 'a', 'b']`).

## Worked example

> [!example] Three samples in parallel, one walltime limit (invented files)
> `align` stands in for an aligner. Sample B's input is missing; sample C exceeds a 1-second limit enforced by `timeout`. `wait PID` returns each job's status:
>
> ```console
> $ set -o pipefail
> align() {  # stand-in for an aligner: decompress, count, take some time
>   zcat -- "$1.fq.gz" | wc -l > "$1.count" && sleep "$2"
> }
> declare -A pid
> align A 0.1 & pid[A]=$!
> align B 0.1 & pid[B]=$!                       # B.fq.gz is missing
> timeout 1 bash -c "$(declare -f align); align C 5" & pid[C]=$!   # walltime 1 s
> for s in A B C; do
>   if wait "${pid[$s]}"; then echo "$s ok"; else echo "$s failed: exit $?"; fi
> done
> gzip: B.fq.gz: No such file or directory
> A ok
> B failed: exit 1
> C failed: exit 124
> ```
>
> Status 124 is `timeout`'s report that the limit was reached. Without `set -o pipefail`, B was reported `ok`: the pipeline took the status of `wc`.

## Common misconceptions

> [!warning] "My background job survives logging out"
> Closing the terminal sends `SIGHUP`; the plain job above died with status 129. Use `nohup`, `tmux` or the scheduler.

> [!warning] "`kill -9` is how to stop a job"
> `SIGKILL` skips every cleanup handler and leaves orphans and partial files; send `SIGTERM` first.

## Exercises

> [!question] Exercise 1 (L1)
> `setenv.sh` contains `export LC_ALL=C`. Why does `bash setenv.sh` leave `LC_ALL` unset in your shell, and what works?

> [!success]- Solution
> `bash setenv.sh` starts a child; its exported variable dies with it. `source setenv.sh` runs the file in the current shell. Observed: `after bash: LC_ALL=unset`, then `after source: LC_ALL=C`.

> [!question] Exercise 2 (L2)
> A 6-hour alignment launched over SSH died when the Wi-Fi dropped. Compare three ways to prevent it.

> [!success]- Solution
> `nohup cmd > log 2>&1 &` ignores the hangup but cannot be brought back to a terminal. `tmux` keeps an interactive session on the server, reattachable from anywhere. On a cluster, heavy work must not run on the login node at all: a batch job for the [[Job Scheduler]] also reserves cores and memory and records the exit status.

> [!question] Exercise 3 (L2, Python)
> Call `count_reads.sh` from [[Shell Script]] in Python and turn a failure into an exception carrying its stderr.

> [!success]- Solution
> ```python
> def count_reads(out, *fastqs):
>     try:
>         subprocess.run(["bash", "count_reads.sh", out, *fastqs],
>                        check=True, capture_output=True, text=True)
>     except subprocess.CalledProcessError as err:
>         raise RuntimeError(f"count_reads.sh exited {err.returncode}: {err.stderr.strip()}") from err
>     with open(out, encoding="ascii") as fh:
>         return [line.rstrip("\n").split("\t") for line in fh][1:]
> ```
>
> On the two toy samples it returned `[['sample_A.fq.gz', '4', '32'], ['sample_B.fq.gz', '2', '10']]`; with `nope.fq.gz` it raised `count_reads.sh exited 1: gzip: nope.fq.gz: No such file or directory` plus the script's `command failed on line 13`. The argument list bypasses shell parsing, so names with spaces need no quoting.

## Mastery checklist

- [ ] 1 Recognized: I can name PID, parent, environment, standard streams and exit status.
- [ ] 2 Understood: I can decode statuses above 128, explain `SIGINT`, `SIGTERM`, `SIGKILL` and `SIGHUP`, and environment inheritance.
- [ ] 3 Practiced: I run, wait for and stop background jobs, trap `SIGTERM`, and use `subprocess` with `check=True`.
- [ ] 4 Applied: the long steps of [[10-genomic-pipeline]] run under `tmux` or the scheduler, and failures are diagnosed from their statuses.
- [ ] 5 Explained: I can teach why `kill -9` is a last resort, why a child cannot change its parent's environment, and how statuses travel through pipelines.

## References

[^ms20cle]: [[MIT - The Missing Semester of Your CS Education]], earlier (2020) edition, lecture "Command-line Environment" (job control, signals, `nohup`, terminal multiplexers).
[^bash]: [[GNU Bash Reference Manual]] (job control, `kill`).
[^bashenv]: [[GNU Bash Reference Manual]], "Environment".
[^bashexit]: [[GNU Bash Reference Manual]], "Exit Status".
[^cunohup]: [[GNU Coreutils Manual]], "nohup invocation".
[^hpc]: [[HPC Carpentry - Introduction to High-Performance Computing]], episode "Scheduler fundamentals".
[^hpcenv]: [[HPC Carpentry - Introduction to High-Performance Computing]], episode "Environment variables".
[^pydoc]: [[Python Documentation]], `subprocess` and `signal` modules.
