---
aliases:
  - Lander-Waterman 1988
  - Lander and Waterman 1988
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Eric S. Lander
  - Michael S. Waterman
journal: Genomics
year: 1988
url: "https://doi.org/10.1016/0888-7543(88)90007-9"
access: paid
---

# Lander 1988 - Genomic Mapping by Fingerprinting Random Clones

> [!abstract]
> The mathematical analysis of mapping a genome from randomly chosen, overlapping clones: the origin of the Lander-Waterman model of coverage, islands and gaps.

## Why this source

Physical maps were then assembled by fingerprinting many clones picked at random from a library and joining clones whose fingerprints overlap. Lander and Waterman gave the theory that predicts, from the number of clones, the clone length, the genome length and the minimum overlap needed to detect a join, how many "islands" (groups of joined clones, the analogue of contigs) and gaps to expect. The same formulas were later applied to shotgun sequencing, where reads replace clones, and remain a standard first estimate.

## Coverage

Citation: Lander ES, Waterman MS. "Genomic mapping by fingerprinting random clones: a mathematical analysis". *Genomics* 2(3):231-239 (April 1988).

| Part | Content | Vault notes |
|---|---|---|
| Model | Clones placed at random along the genome; redundancy (coverage) as clone length times number of clones over genome length | [[Sequencing Coverage]], [[Poisson Distribution]] |
| Islands and gaps | Expected number of islands and of gaps as functions of coverage and of the overlap needed for detection | [[Lander-Waterman Model]], [[Genome Assembly]] |

Cited in [[Poisson Distribution]].

## How to use it

- L2: read the model and the expected-number-of-islands result alongside [[Poisson Distribution]] and [[Lander-Waterman Model]].
- L3: compare its assumptions (uniform placement, exact overlap detection) with real read depth and assemblies, where GC bias and repeats break them.

## Caveats

- Written for clone-based physical mapping, before high-throughput sequencing; applying it to reads is a later reuse of the same mathematics.
- Authors, title, journal, volume, issue, pages and month verified by web search in this pass; the DOI is the one attached to this article in bibliographic records; the publisher page was not opened and open-access status was not verified.
