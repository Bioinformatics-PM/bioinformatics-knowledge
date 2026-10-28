---
aliases:
  - TCDB
  - TC system
  - Transporter Classification system
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - Milton H. Saier Jr.
  - Vamsee S. Reddy
  - Gabriel Moreno-Hagelsieb
  - et al.
institution: University of California, San Diego (Saier laboratory)
year: 2021
edition:
url: https://www.tcdb.org
access: free
---

# Transporter Classification Database

> [!abstract]
> The reference classification of membrane transport proteins: every transport system receives a five-part TC number that encodes its mechanism class, subclass, family, subfamily and the system itself.

## Why this source

It is to transporters what the EC list is to enzymes: a stable vocabulary for annotating transport proteins, organized first by mechanism and energy source, then by homology. It lets a student connect the mechanisms of [[Membrane Transport]] (channels, carriers, pumps) to the protein families found by sequence comparison in a new genome.

## Coverage

Key publication: Saier MH Jr, Reddy VS, Moreno-Hagelsieb G, et al. "The Transporter Classification Database (TCDB): 2021 update". *Nucleic Acids Research* 49(D1):D461-D467 (2021). doi:10.1093/nar/gkaa1004. As of 1 October 2020 the database held 20,653 proteins in 15,528 non-redundant transport systems, with 1,567 3D structures and 1,536 transporter families; the update added new channel and group-translocator subclasses and a chemical ontology for substrates.

| Part | Content | Vault notes |
|---|---|---|
| Hierarchy | Class, subclass, family, subfamily, transport system; the first number of the TC identifier is the class | [[Membrane Transport]], [[Protein Family]] |
| Class 1 | Channels and pores (subclass 1.A: α-type channels) | [[Ion Channel]], [[Membrane Transport]] |
| Class 2 | Electrochemical potential-driven transporters: the carriers, which use the electrochemical gradient of a solute or of a co-transported ion | [[Membrane Transport]] |
| Class 3 | Primary active transporters; subclass 3.A, P-P-bond-hydrolysis-driven transporters, holds the ABC and P-type ATPase families | [[Membrane Transport]], [[ATP]] |

## How to use it

- **L2**: browse class 1 to 3 and find where the Na⁺-K⁺ pump, a glucose uniporter and an ABC transporter sit.
- **L3**: search a protein sequence against TCDB to assign it a family, and compare with its EC 7 number in [[ExplorEnz]].

## Caveats

- The classification changes between releases (subclasses and families are added): record the release used in an annotation.
- Verified in this pass (web search): the 2021 citation, the database counts of its abstract, the hierarchy of the TC identifier, the names of classes 1 to 3, subclass 1.A, and subclass 3.A with its ABC and P-type ATPase families (through the IUBMB list of transport proteins). Individual family numbers were not verified.
