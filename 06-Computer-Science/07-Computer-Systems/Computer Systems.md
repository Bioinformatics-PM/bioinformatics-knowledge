---
aliases:
  - Systems
  - Systèmes informatiques
tags:
  - type/moc
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Programming]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
---

# Computer Systems

> [!abstract]
> The machine under the analysis: the Unix shell and file system, processes, the memory hierarchy and virtual memory, concurrency and parallelism, building software from source, containers, high-performance computing clusters and their schedulers, and cloud computing.

## Why it matters for bioinformatics

Bioinformatics runs on Unix servers and shared clusters, not on laptops. A read-mapping job must be sized in cores, memory and walltime for a scheduler; a tool that works on one machine must be shipped in a [[Container]] to run on another; an analysis over hundreds of samples is [[Parallel Computing|embarrassingly parallel]] and should be written that way; a job killed for memory needs [[Virtual Memory]] to be diagnosed. Workflow managers, the backbone of [[Bioinformatics Engineering]], are schedulers of processes and containers. Systems topics appear in bioinformatics degrees (SJTU's major requires a computer networks course),[^sjtu] but this syllabus targets the practitioner's level: operating a cluster well, not building an operating system.

## Before you start

- [[Programming]]: [[Command-Line Interface]] and [[File Input and Output]], for writing tools that behave well in a shell.
- No other prerequisite. Stage 1 can start on day one, in parallel with [[Programming]].

## Learning path

> [!tip] Order of study
> Stage 1 is daily practice from the first week, alongside the first programming course:[^missing] do the exercises on real sequence files in a terminal, not in a notebook. Stage 2 is needed before [[10-genomic-pipeline]]; ask for an account on a university or national cluster to practice [[Job Scheduler|job submission]].

### Stage 1 - Foundations (L1)

1. [[Unix Shell]] (L1): navigate, redirect, pipe and glob in bash; the working environment of bioinformatics.
2. [[File System]] (L1): reason about paths, permissions, links and quotas, and the roles of home, project and scratch storage.
3. [[Unix Text Processing]] (L1): answer questions on large tabular and sequence files with `grep`, `cut`, `sort`, `uniq`, `join`, `awk` and `sed`, streaming without loading into memory.
4. [[Shell Script]] (L1): write bash scripts that fail loudly (`set -euo pipefail`, quoting, loops, `xargs`).
5. [[Process (Computing)]] (L1): manage processes, signals, exit codes, environment variables and standard streams, and keep long jobs alive with `nohup` or `tmux`.
6. [[Secure Shell]] (L1): log into remote servers with SSH keys, transfer data with `scp` and `rsync`, and verify transfers.

### Stage 2 - Core (L2)

7. [[Memory Hierarchy]] (L2): compare the latency of caches, RAM, SSD, disk and network, and write code with good locality.
8. [[Virtual Memory]] (L2): explain address spaces, paging, swapping and memory-mapped files, and diagnose out-of-memory kills.
9. [[Concurrency]] (L2): distinguish processes from threads, avoid race conditions, and know how the global interpreter lock shapes threading versus multiprocessing in Python.
10. [[Parallel Computing]] (L2): split work by data or by task, estimate speed-up and efficiency with Amdahl's law, and exploit embarrassingly parallel structure (per sample, per chromosome).
11. [[Compilation and Linking]] (L2): build C and C++ tools from source with `make` or CMake, and resolve shared-library errors.
12. [[Container]] (L2): package a tool and its dependencies in a Docker or Apptainer image, pin versions, and reuse community images.
13. [[High-Performance Computing]] (L2): describe a cluster (login and compute nodes, shared storage, interconnect, environment modules) and use it responsibly.
14. [[Job Scheduler]] (L2): submit, monitor and size batch jobs and job arrays with Slurm (cores, memory, walltime).
15. [[Cloud Computing]] (L2): rent compute and object storage, estimate cost including data egress, and work on public datasets hosted in the cloud.

### Stage 3 - Advanced (L3)

16. [[Parallel File System]] (L3): understand why cluster file systems (Lustre, GPFS) favor few large files over millions of small ones, and organize I/O accordingly.
17. [[Single Instruction Multiple Data]] (L3): explain how vector instructions process several cells of a dynamic programming matrix at once, the trick behind fast Smith-Waterman implementations.
18. [[Message Passing Interface]] (L3): read the distributed-memory model (ranks, messages, collective operations) used by large phylogenetics and assembly codes.
19. [[GPU Computing]] (L3): know the GPU execution and memory model, and when host-to-device transfer costs outweigh the speed-up.

## Uses from other domains

- [[Workflow Management System]] ([[Bioinformatics Engineering]]): orchestrates processes, containers and scheduler jobs into pipelines.
- [[Reproducibility]] ([[Scientific Practice]]): containers and pinned environments are its computational side.
- [[Dependency Management]] ([[Software Engineering]]): what goes inside a container image.
- [[Performance Profiling]] ([[Scientific Computing]]): measuring where a job spends its time and memory.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT - The Missing Semester of Your CS Education]] | MIT | L1 | 2026 lectures "Introduction to the Shell" and "Command-line Environment"; the earlier edition goes deeper into shell scripting, tmux, ssh, sed and awk[^missing] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins University | L2 | Course "Command Line Tools for Genomic Data Science": the shell applied to genomic files[^jhu] |
| [[HPC Carpentry - Introduction to High-Performance Computing]] | The Carpentries | L2 | Cluster access, scheduler, environment modules, transferring files, parallel jobs |

## Reference books

- [[Bioinformatics Data Skills (Buffalo)]]: Unix shell and text processing on real bioinformatics files, remote machines and robust scripts; the most direct book for Stage 1.

## Lab projects

- [[10-genomic-pipeline]]: [[Container|containers]], [[Job Scheduler|scheduler]] or cloud execution, and [[Parallel Computing|parallelism]] per sample.
- [[05-sequence-search]]: [[Memory Hierarchy]] effects when the index outgrows the cache and then RAM.

## References

[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: Computer Networks is part of the computer science core of the bioinformatics major.
[^missing]: [[MIT - The Missing Semester of Your CS Education]]: 2026 lectures on the shell and the command-line environment; the earlier edition, still online, covers shell scripting, tmux, ssh, sed and awk in more depth.
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]]: includes a course on command-line tools for genomic data.
