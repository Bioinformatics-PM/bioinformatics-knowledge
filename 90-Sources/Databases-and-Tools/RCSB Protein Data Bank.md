---
aliases:
  - RCSB PDB
  - Protein Data Bank
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - domain/chemistry
  - level/L1
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - Stephen K. Burley
institution: RCSB PDB (US data center of the Worldwide Protein Data Bank)
year: 1971
edition:
url: https://www.rcsb.org
access: free
---

# RCSB Protein Data Bank

> [!abstract]
> The US data center of the single global archive of experimentally determined 3D structures of biological macromolecules; its portal RCSB.org also serves computed structure models.

## Why this source

Every statement about [[Protein Structure]] in the vault eventually points to a PDB entry. RCSB.org lets a learner open a structure, rotate it, and see how the sequence folds, then connect that picture to function and to mutations.

> [!info] History
> The PDB was established in 1971 at Brookhaven National Laboratory with 7 structures. The Research Collaboratory for Structural Bioinformatics (RCSB) has managed it since 1998. In 2003 the Worldwide PDB (wwPDB) was formed to keep a single archive, with RCSB PDB, PDBj (Japan), PDBe (Europe) and BMRB as members.

## Coverage

Key publication: Burley SK et al. "Updated resources for exploring experimentally-determined PDB structures and Computed Structure Models at the RCSB Protein Data Bank". *Nucleic Acids Res* 53:D564-D574 (2025). doi:10.1093/nar/gkae1091. It describes access to the experimental PDB archive alongside more than 1 million Computed Structure Models, results organized in redundancy-reduced groups of similar proteins, and 3D structure motif search with user-provided coordinates.

| Part | Content | Vault notes |
|---|---|---|
| Experimental structures | Atomic 3D structures from the PDB archive | [[Protein Structure]], [[Structural Bioinformatics]] |
| Computed Structure Models | Predicted models shown next to experimental ones | [[AlphaFold Protein Structure Database]], [[Protein Folding]] |
| Groups | Redundancy-reduced groups of similar proteins | [[Sequence Homology]] |
| Motif search | Search by 3D structural motif | [[Protein Structure]] |
| Training | PDB-101 pages (pdb101.rcsb.org) | [[Protein]], [[Amino Acid]] |

## How to use it

- **L1**: search a famous structure (a hemoglobin or a DNA double helix), open it in the 3D viewer and identify the chains.
- **L2**: in each entry, read the experimental method and the resolution before trusting the details; in [[06-mutation-lab]], locate a mutated residue on the structure.
- **L3**: compare an experimental entry with the computed model of the same protein; parse structure files with [[Biopython]].

## Caveats

- Always check whether you are looking at an experimental structure or a computed model: RCSB.org shows both.
- Entry counts differ between RCSB documents depending on date and on what is counted: quote a number only with its source and date.
- Verified in this pass: the 2025 paper (lead author, DOI, abstract) and the PDB history page.
