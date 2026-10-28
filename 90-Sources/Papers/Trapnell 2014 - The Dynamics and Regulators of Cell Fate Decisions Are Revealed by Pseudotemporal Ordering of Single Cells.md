---
aliases:
  - Monocle
  - Trapnell 2014
  - Pseudotime paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: S
authors:
  - Cole Trapnell
  - et al.
journal: Nature Biotechnology
year: 2014
url: "https://pubmed.ncbi.nlm.nih.gov/24658644/"
access: free
---

# Trapnell 2014 - The Dynamics and Regulators of Cell Fate Decisions Are Revealed by Pseudotemporal Ordering of Single Cells

> [!abstract]
> The paper that introduced Monocle and the idea of pseudotime: ordering single cells by their progress through a differentiation process, recovered from their transcriptomes alone.

## Why this source

Before it, a time course of differentiation meant averaging cells collected at a few time points, which blurs early and late events. By ordering single cells along a trajectory, it made differentiation a continuous object that can be analyzed computationally, the idea behind [[Trajectory Inference]].

## Coverage

Citation: Trapnell C, et al. "The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells". *Nature Biotechnology* 32(4):381-386 (2014). doi:10.1038/nbt.2859. PMID 24658644; free author manuscript PMC4122333 (titled "Pseudo-temporal ordering of individual cells reveals dynamics and regulators of cell fate decisions").

| Part | Content | Vault notes |
|---|---|---|
| Problem | Bulk time series struggle to separate early and late phases of a transcriptional cascade or to find rare subpopulations | [[Cell Differentiation]] |
| Method | Monocle, an unsupervised algorithm that increases the temporal resolution of transcriptome dynamics from single-cell RNA-seq collected at several time points | [[Trajectory Inference]], [[Single-Cell RNA Sequencing]] |
| Application | Differentiation of primary human myoblasts: switch-like changes in key regulatory factors, sequential waves of gene regulation, regulators not known to act in differentiation | [[Cell Differentiation]], [[Transcription Factor]] |
| Validation | Some predicted regulators confirmed in a loss-of-function screen | [[Genetic Screen]] |

## How to use it

- **L3**: read the abstract and the first figure after [[Cell Differentiation]]; then order a toy data set by hand (exercise in that note).
- **M1**: compare its assumptions (a continuous path, the direction given by time points) with later trajectory-inference methods.

## Caveats

- The original Monocle algorithm has been replaced by later versions of the software; read the current documentation before using the tool.
- Verified in this pass (web search): the citation, DOI, PMID and PMC numbers, both titles, and the abstract (problem, method, myoblast results, validation, possible extension to other processes). The full author list (abbreviated here) and the method details were not verified.
