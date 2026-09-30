---
aliases:
  - hpc-intro
tags:
  - type/source
  - domain/computer-science
  - level/L2
kind: course
tier: B
authors:
  - HPC Carpentry contributors
institution: HPC Carpentry (The Carpentries Incubator)
year:
url: "https://carpentries-incubator.github.io/hpc-intro/"
access: free
---

# HPC Carpentry - Introduction to High-Performance Computing

> [!abstract]
> A one-day Carpentries-style lesson on using a high-performance computing cluster from the command line: connecting, exploring resources, submitting jobs to a scheduler and loading software.

## Why this source

Most genomics analyses outgrow a laptop, and the first cluster session is where many learners get stuck. This lesson teaches the basics of interacting with HPC clusters through the command line, with a gentle introduction to workload managers (queuing systems) and shared resources, using Slurm. It is written in the tested, hands-on Carpentries format and is used by many institutions for their own training.

## Coverage

Episodes listed are those verified in this pass; the lesson has further episodes.

| Episode | Content | Vault notes |
|---|---|---|
| Why use a cluster? | What a cluster offers compared with a laptop | [[High-Performance Computing]] |
| Connecting to a remote HPC system | Logging in with SSH | [[Secure Shell]] |
| Exploring remote resources | Nodes, cores, memory and storage of a cluster | [[High-Performance Computing]], [[Parallel File System]] |
| Scheduler fundamentals | Submitting and monitoring jobs on compute nodes | [[Job Scheduler]] |
| Environment variables | How variables change how programs run | [[Unix Shell]] |
| Accessing software via modules | Loading and unloading software | [[Dependency Management]] |

Cited in [[Computer Systems]].

## How to use it

- L2: follow it on a real cluster account if you have one (university or national center), after the shell basics of [[Bioinformatics Data Skills (Buffalo)]].
- Then run one step of [[10-genomic-pipeline]] as a scheduled job.

## Caveats

- Site-specific details (scheduler, module names, paths) vary; the lesson uses a snippet library to adapt them, so read the version matching your cluster when possible.
- HPC Carpentry is developing in The Carpentries Incubator and is not yet an official Carpentries lesson program.
- Verified in this pass: URL, scope, duration (one day), use of Slurm and the episode titles listed.
