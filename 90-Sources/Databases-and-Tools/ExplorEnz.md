---
aliases:
  - IUBMB Enzyme List
  - Enzyme Nomenclature
  - The Enzyme Database
  - EC List
tags:
  - type/source
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - Andrew G. McDonald
  - Sinéad Boyce
  - Keith F. Tipton
institution: Trinity College Dublin, for the Nomenclature Committee of the IUBMB (NC-IUBMB)
year: 2009
edition:
url: https://www.enzyme-database.org/
access: free
---

# ExplorEnz

> [!abstract]
> The database used to curate and distribute the IUBMB Enzyme List: the official Enzyme Commission (EC) numbers, accepted names and reactions of all classified enzymes.

## Why this source

EC numbers are the identifiers that genome annotation, UniProt entries and pathway databases such as [[KEGG]] use for enzyme function. ExplorEnz is the primary source of that classification: when a textbook, a database and an annotation disagree on an EC number, this is the reference.

> [!info] History
> The first enzyme classification and nomenclature list was approved by the International Union of Biochemistry in 1961, with six classes based on the type of reaction catalysed. In August 2018 the IUBMB added a seventh class, the translocases (EC 7), for enzymes that move ions or molecules across membranes; several of them had been classified as ATPases (EC 3.6.3.-) although hydrolysis is not their primary function.

## Coverage

Key publication: McDonald AG, Boyce S, Tipton KF. "ExplorEnz: the primary source of the IUBMB enzyme list". *Nucleic Acids Research* 37:D593-D597 (2009). PMID 18776214. It describes ExplorEnz as the MySQL database used for the curation and dissemination of the IUBMB Enzyme Nomenclature.

| Part | Content | Vault notes |
|---|---|---|
| Classes | EC 1 oxidoreductases, EC 2 transferases, EC 3 hydrolases, EC 4 lyases, EC 5 isomerases, EC 6 ligases, EC 7 translocases | [[Enzyme]] |
| EC numbers | Four fields: class, subclass, sub-subclass, serial number; enzymes are classified by the reaction they catalyse | [[Enzyme]], [[Functional Annotation]] |
| Entries | Accepted name, systematic name, reaction, comments, history of changes (new, transferred, deleted entries) | [[Enzyme]], [[Metabolic Pathway]] |
| EC 7 subclasses | Translocation of hydrons (7.1), inorganic cations (7.2), inorganic anions (7.3), amino acids and peptides (7.4), carbohydrates (7.5), other compounds (7.6) | [[Membrane Transport]] |

## How to use it

- **L1**: learn the seven classes and how to read an EC number; look up one enzyme of each class.
- **L2**: compare an enzyme's accepted and systematic names; follow a transferred entry to its new number.
- **L3**: check EC annotations in a genome or a pathway map against the current list before trusting them.

## Caveats

- EC numbers classify reactions, not proteins or genes: unrelated proteins can share a number, and one protein with two activities has two.
- The list changes: entries are added, transferred and deleted. Annotations made with an older version may carry obsolete numbers (for example ATPases moved to EC 7).
- Verified in this pass (web search): the 2009 NAR citation and description, the 1961 origin with six classes, and the August 2018 creation of EC 7 with its six subclasses (IUBMB newsletter and the EC 7 list on enzyme-database.org).
