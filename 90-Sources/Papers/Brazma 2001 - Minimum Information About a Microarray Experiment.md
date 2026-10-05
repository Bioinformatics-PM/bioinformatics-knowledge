---
aliases:
  - MIAME paper
tags:
  - type/source
  - domain/scientific-practice
  - domain/bioinformatics
  - level/L3
kind: paper
tier: S
authors:
  - Alvis Brazma
  - Pascal Hingamp
  - John Quackenbush
  - Gavin Sherlock
  - et al.
journal: Nature Genetics
year: 2001
url: "https://doi.org/10.1038/ng1201-365"
access: paid
---

# Brazma 2001 - Minimum Information About a Microarray Experiment

> [!abstract]
> The paper that defined MIAME, the minimum information needed to interpret microarray data unambiguously and to verify results derived from them.

## Why this source

MIAME was the first widely adopted "minimum information" reporting standard in biology, and it became a condition of publication and of submission to archives such as GEO and ArrayExpress. It established the model later copied by many checklists (the MIBBI family), including MINSEQE for sequencing. The idea is general: describe the experiment well enough that someone else could interpret the data and reproduce the analysis.

## Coverage

Citation: Brazma A, Hingamp P, Quackenbush J, Sherlock G, Spellman P, Stoeckert C, et al. "Minimum information about a microarray experiment (MIAME)-toward standards for microarray data". *Nature Genetics* 29(4):365-371 (2001). doi:10.1038/ng1201-365.

| Part | Content | Vault notes |
|---|---|---|
| Goal | Minimum information to interpret microarray data and verify results | [[Minimum Information About a Microarray Experiment]] |
| Content | Description of experimental design, arrays, samples, hybridizations, measurements and normalization | [[Metadata]], [[Microarray]] |
| Model for other standards | A checklist approach reused by later minimum information standards | [[Minimum Information Standard]], [[Minimum Information About a Next-Generation Sequencing Experiment]] |

Cited in [[Research Data Management]].

## How to use it

- L3: read it for item 12 of [[Research Data Management]], then open one GEO series and check which MIAME elements you can find.
- Compare it with the sequencing checklist used by [[Data Submission]] to SRA, ENA or GEO today.

## Caveats

- Microarrays have largely given way to sequencing, but the reporting logic carries over.
- MIAME specifies content, not a file format.
- Metadata (title, journal, volume, issue, pages, DOI) verified in this pass; free full text not verified.
