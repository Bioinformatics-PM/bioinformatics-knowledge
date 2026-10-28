---
aliases:
  - Mutational signatures in human cancer
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: S
authors:
  - Ludmil B. Alexandrov
  - Serena Nik-Zainal
  - David C. Wedge
  - et al.
  - Michael R. Stratton
journal: Nature
year: 2013
url: "https://doi.org/10.1038/nature12477"
access: partial
---

# Alexandrov 2013 - Signatures of Mutational Processes in Human Cancer

> [!abstract]
> The study that extracted more than 20 mutational signatures from 4,938,362 somatic mutations in 7,042 cancers, and linked several of them to age, mutagen exposure or defects in DNA maintenance.

## Why this source

It turned the list of somatic mutations of a tumour into a readable record of the processes that produced them: each process of DNA damage and failed repair leaves a characteristic spectrum, and a tumour's catalogue is a mixture of such spectra that can be separated computationally. It is the reference point for every later catalogue of signatures and for the tools that fit them to new samples.

## Coverage

Citation: Alexandrov LB, Nik-Zainal S, Wedge DC, et al., Stratton MR. "Signatures of mutational processes in human cancer". *Nature* 500(7463):415-421 (2013). doi:10.1038/nature12477.

| Part | Content | Vault notes |
|---|---|---|
| Data | 4,938,362 somatic mutations from 7,042 cancers | [[Cancer]], [[Somatic Mutation]] |
| Signatures | More than 20 distinct mutational signatures; one attributed to the APOBEC family of cytidine deaminases is present in many cancer types, others are confined to one cancer class | [[DNA Repair]], [[Mutation]] |
| Causes | Some signatures are associated with age at diagnosis, known mutagenic exposures or defects in DNA maintenance; many have no known cause | [[DNA Repair]], [[Mutation Rate]] |
| Kataegis | Hypermutation localized to small genomic regions, found in many cancer types | [[Somatic Variant Calling]] |

Cited in [[DNA Repair]].

## How to use it

- L3: read the abstract and the main signature figure after [[DNA Repair]] and [[Mutation]], to see how a spectrum is built from somatic variant calls.
- M1: entry point to signature extraction and fitting in cancer genomics ([[Somatic Variant Calling]], [[Cancer]]).

## Caveats

- Later studies extended and renumbered the catalogue of signatures: check which signature set a tool or paper uses before comparing results.
- Author manuscripts are available in institutional repositories (for example Harvard DASH); the journal version is paywalled.
- Verified in this pass: citation metadata (first and last authors, journal, volume, issue, pages, DOI) and the abstract findings. The classification of substitutions by trinucleotide context (96 classes) is given as usually described, not re-checked against the full text.
