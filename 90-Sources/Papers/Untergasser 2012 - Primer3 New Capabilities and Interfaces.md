---
aliases:
  - Primer3 paper
  - Primer3
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - Andreas Untergasser
  - Ioana Cutcutache
  - Triinu Koressaar
  - Jian Ye
  - Brant C. Faircloth
  - Maido Remm
  - Steven G. Rozen
journal: Nucleic Acids Research
year: 2012
url: "https://pubmed.ncbi.nlm.nih.gov/22730293/"
access: free
---

# Untergasser 2012 - Primer3 New Capabilities and Interfaces

> [!abstract]
> The reference paper of Primer3, the open-source program that designs PCR primers, describing its thermodynamic models for melting temperature and for hairpin and dimer formation.

## Why this source

Primer3 is the primer-design engine behind many web tools and high-throughput genomics pipelines. The paper states why primer design matters for every PCR application and what a modern design tool computes: melting temperature from thermodynamic models instead of simple counting rules, and the risk that a primer forms hairpins or dimers. It is the natural citation when a note explains computational primer design.

## Coverage

Citation: Untergasser A, Cutcutache I, Koressaar T, Ye J, Faircloth BC, Remm M, Rozen SG. "Primer3, new capabilities and interfaces". *Nucleic Acids Research* 40(15):e115 (2012). PubMed 22730293, free at PMC3424584.

| Part | Content | Vault notes |
|---|---|---|
| Context | PCR in cloning, sequencing, functional analysis, diagnosis, genotyping and variant discovery; reliable primer design is crucial | [[Polymerase Chain Reaction]] |
| Thermodynamic models | More accurate melting temperature prediction; reduced likelihood of hairpins and primer dimers | [[Polymerase Chain Reaction]], [[Base Pairing]] |
| Placement and interfaces | Finer control of where primers are placed; reusable parameter settings; web and command-line interfaces | [[Polymerase Chain Reaction]] |

## How to use it

- L1: read the abstract and introduction after designing a primer pair by hand in [[Polymerase Chain Reaction]].
- L2: run Primer3 on the same template and compare its choices with your own checks.

## Caveats

- Verified in this pass: authors, title, journal, volume, issue, article number, PubMed and PMC identifiers, and the abstract content summarized above.
- Default parameter values (optimal primer length, melting temperature ranges) live in the Primer3 manual, which is tool documentation (tier C) and changes between versions; they are not copied here.
