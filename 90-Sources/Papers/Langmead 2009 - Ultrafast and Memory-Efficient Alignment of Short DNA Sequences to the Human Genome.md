---
aliases:
  - Bowtie paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Ben Langmead
  - Cole Trapnell
  - Mihai Pop
  - Steven L. Salzberg
journal: Genome Biology
year: 2009
url: "https://doi.org/10.1186/gb-2009-10-3-r25"
access: free
---

# Langmead 2009 - Ultrafast and Memory-Efficient Alignment of Short DNA Sequences to the Human Genome

> [!abstract]
> The Bowtie paper: a short-read aligner that indexes the human genome with a Burrows-Wheeler index to keep its memory footprint small.

## Why this source

A landmark case of an index designed around memory: instead of a hash table or a suffix array of the whole genome, Bowtie stores a compressed Burrows-Wheeler index whose footprint for the human genome is about 1.3 GB. It is the reference example for why a genome index must fit in memory, and an entry point to the [[FM-Index]] family of read mappers.

## Coverage

Citation: Langmead B, Trapnell C, Pop M, Salzberg SL. "Ultrafast and memory-efficient alignment of short DNA sequences to the human genome". *Genome Biology* 10(3):R25 (2009). doi:10.1186/gb-2009-10-3-r25. Free at PMC2690996.

| Part | Content | Vault notes |
|---|---|---|
| Abstract | Burrows-Wheeler indexing of the human genome, with a memory footprint of about 1.3 GB | [[Space Complexity]], [[Burrows-Wheeler Transform]], [[FM-Index]] |
| Method | Aligning short reads against the index | [[Read Mapping]] |

Cited in [[Space Complexity]].

## How to use it

- L2: read the abstract and introduction with [[Space Complexity]]: compare the published footprint with the size of a plain suffix array of the same genome.
- L3: read the method with [[Burrows-Wheeler Transform]] and [[FM-Index]], then [[Read Mapping]].

## Caveats

- Verified in this pass: citation metadata, open access at PMC, and the abstract's memory footprint of about 1.3 GB for the human genome. Software descriptions of Bowtie (README-based package pages) quote about 2.2 GB for the human index (2.9 GB for paired-end alignment), presumably for later versions or settings: cite a figure with its source and date.
- 2009: designed for the short reads of that time; read lengths, aligners and their memory figures have changed since.
