---
aliases:
  - HGVS nomenclature
  - HGVS 2016 update
  - Varnomen
tags:
  - type/source
  - domain/bioinformatics
  - domain/industry
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Johan T. den Dunnen
  - Raymond Dalgleish
  - Donna R. Maglott
  - Reece K. Hart
  - Marc S. Greenblatt
  - Jean McGowan-Jordan
  - Anne-Francoise Roux
  - Timothy Smith
  - Stylianos E. Antonarakis
journal: Human Mutation
year: 2016
url: "https://doi.org/10.1002/humu.22981"
access: free
---

# den Dunnen 2016 - HGVS Recommendations for the Description of Sequence Variants

> [!abstract]
> The 2016 update of the Human Genome Variation Society (HGVS) recommendations, the standard nomenclature used to write sequence variants in reports, papers and databases (`c.20A>T`, `p.Glu7Val`).

## Why this source

Consistent, unambiguous description of variants is what lets laboratories and databases exchange results; clinical reports and the variant databases use HGVS names. The paper presents version 15.11 of the recommendations and summarizes the changes since the 2000 publication; the full, versioned rules live on the HGVS website (varnomen). For a bioinformatician it defines the strings that annotation tools must produce from genomic coordinates.

## Coverage

Citation: den Dunnen JT, Dalgleish R, Maglott DR, Hart RK, Greenblatt MS, McGowan-Jordan J, Roux AF, Smith T, Antonarakis SE. "HGVS Recommendations for the Description of Sequence Variants: 2016 Update". *Human Mutation* 37(6):564-569 (2016). doi:10.1002/humu.22981. Full recommendations: HGVS.org/varnomen.

| Part | Content | Vault notes |
|---|---|---|
| Reference sequences | Genomic (`g.`), coding (`c.`, where `c.1` is the A of the ATG start codon) and protein (`p.`) descriptions | [[Variant Nomenclature]], [[Genomic Coordinate System]] |
| DNA variants | Substitution (`>`), deletion (`del`), duplication (`dup`), insertion (`ins`), deletion-insertion (`delins`); the 3' rule | [[Point Mutation]], [[Indel]] |
| Protein variants | Three-letter amino acid codes, `Ter` or `*` for a stop, frameshifts written `fs` (example `p.Arg97ProfsTer23`) | [[Missense Mutation]], [[Nonsense Mutation]], [[Frameshift Mutation]] |

The **3' rule**: when a variant can be placed at several positions (for example a deletion inside a run of identical bases or a tandem repeat), the most 3' position is the one described.

Cited in [[Missense Mutation]], [[Nonsense Mutation]], [[Indel]] and [[Frameshift Mutation]].

## How to use it

- L2: learn to read `c.` and `p.` descriptions of substitutions, deletions and frameshifts while working through the mutation notes of [[Genetics]].
- L3: generate HGVS strings from VCF records in [[03-genome-diff]], taking care of the 3' rule, which is the opposite of VCF left alignment ([[Tan 2015 - Unified Representation of Genetic Variants]]).

## Caveats

- The recommendations are versioned and keep changing; cite the version used and check the website for the current rules.
- The DNA-level 3' rule has an exception at exon-intron borders.
- Verified in this pass: citation, author list, version 15.11 and the website address. The rules summarized above (the `c.1` convention, the 3' rule, `Ter`/`*`, the `fs` format) were checked in secondary descriptions of the HGVS recommendations, not in the paper text itself.
