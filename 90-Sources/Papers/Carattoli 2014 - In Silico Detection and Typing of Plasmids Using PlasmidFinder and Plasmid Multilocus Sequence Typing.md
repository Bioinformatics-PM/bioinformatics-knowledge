---
aliases:
  - PlasmidFinder
  - pMLST
  - Carattoli et al. 2014
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
kind: paper
tier: A
authors:
  - Alessandra Carattoli
  - Ea Zankari
  - Aurora García-Fernández
  - Mette Voldby Larsen
  - Ole Lund
  - Laura Villa
  - Frank Møller Aarestrup
  - Henrik Hasman
journal: Antimicrobial Agents and Chemotherapy
year: 2014
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC4068535/"
access: free
---

# Carattoli 2014 - In Silico Detection and Typing of Plasmids Using PlasmidFinder and Plasmid Multilocus Sequence Typing

> [!abstract]
> The paper that introduced PlasmidFinder, a web tool that detects known plasmid replicons in whole-genome sequencing data, and pMLST, which subtypes plasmids by multilocus sequence typing.

## Why this source

It is the reference for replicon typing of plasmids from sequence data, the standard first step to tell which plasmid families a bacterial isolate carries, for example when tracing resistance plasmids in pathogen genomics.

## Coverage

Citation: Carattoli A, Zankari E, García-Fernández A, Voldby Larsen M, Lund O, Villa L, Møller Aarestrup F, Hasman H. *Antimicrobial Agents and Chemotherapy* 58(7):3895-3903 (2014). doi:10.1128/AAC.02412-14. Free at PMC4068535.

| Part | Content | Vault notes |
|---|---|---|
| Database | Replicon sequences collected from 559 fully sequenced plasmids of Enterobacteriaceae (NCBI nucleotide database); 116 replicon sequences that match all replicons of these plasmids with at least 80% nucleotide identity | [[Plasmid]] |
| pMLST | A database generated from pubmlst.org, updated weekly, behind a web tool for plasmid multilocus sequence typing | [[Plasmid]] |
| Evaluation | On 49 *Salmonella enterica* serovar Typhimurium draft genomes: 103 replicons in total, between zero and five different replicons per genome | [[Plasmid]], [[Antimicrobial Resistance]] |

Cited in [[Plasmid]].

## How to use it

- L3: read the abstract and methods before running PlasmidFinder on an assembly; note the identity threshold and the taxonomic scope of the database.
- M1: compare replicon typing with plasmid reconstruction approaches when studying resistance plasmids in pathogen genomes.

## Caveats

- The 2014 database was built from Enterobacteriaceae plasmids; the counts above describe the 2014 release, and the database has grown since (a later chapter by the same group reports more replicon sequences).
- A plasmid whose replicon is not in the database is missed: absence of a hit is not absence of a plasmid.
- Verified in this pass (web search): authors, journal, volume, issue, pages, DOI, PMC record, and the database and evaluation numbers above.
