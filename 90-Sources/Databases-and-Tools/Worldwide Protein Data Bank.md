---
aliases:
  - wwPDB
  - PDB format guide
  - PDBx/mmCIF dictionary
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: website
tier: A
authors: []
institution: Worldwide Protein Data Bank (wwPDB)
year: 2026
edition: "PDBx/mmCIF dictionary version 5.417; PDB format guide version 3.3"
url: "https://www.wwpdb.org"
access: free
---

# Worldwide Protein Data Bank

> [!abstract]
> The organization that keeps the single global archive of macromolecular structures (the PDB) and maintains its file formats: the legacy fixed-column PDB format and the PDBx/mmCIF dictionary, the archive's format since 2014.

## Why this source

Structure files are defined by the wwPDB, not by a textbook: the PDB format guide fixes the columns of every field of a coordinate record, and the PDBx/mmCIF dictionary defines every data item of the current format, with its meaning, type and units. The RCSB PDB ([[RCSB Protein Data Bank]]) is one of the wwPDB data centers and the usual portal to the entries.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| PDB format guide, version 3.3 (Atomic Coordinate Entry Format Description), coordinate section | Fixed columns of ATOM and HETATM records: serial 7-11, atom name 13-16, alternate location 17, residue name 18-20, chain 22, residue number 23-26, insertion code 27, x, y, z in columns 31-54 (Real(8.3), in Å), occupancy 55-60 and temperature factor 61-66 (Real(6.2)), element 77-78, charge 79-80 | [[PDB Format]] |
| File-format policy (wwPDB announcements; PDBj help page on large structures) | PDBx/mmCIF the archive format since 2014, the legacy format frozen; PDB-format files produced only for entries it can represent (at most 99,999 atoms and 62 chains, single-character chain identifiers); 2019 announcement making PDBx/mmCIF the only format accepted for crystallographic depositions | [[PDB Format]], [[Structural Bioinformatics]] |
| PDBx/mmCIF dictionary (`mmcif_pdbx_v50`, version 5.417) | `atom_site` category with an example based on entry 5HVP; `Cartn_x/y/z` in Å on orthogonal axes; `occupancy` (fraction, at most 1.0 per site); `B_iso_or_equiv` (isotropic displacement parameter, $B = 8\pi^2 U$); `label_seq_id` (sequential positive integers) versus `auth_seq_id` (author numbering, possibly negative, with gaps or insertion codes); `group_PDB` kept for compatibility with the PDB format; `pdbx_PDB_model_num`; wwPDB recommendation to publish with `auth_*` identifiers | [[PDB Format]], [[Protein Structure]] |

Cited in [[PDB Format]].

## How to use it

- L2: read the ATOM/HETATM table of the format guide and the `atom_site` category of the dictionary side by side, with [[PDB Format]].
- L3: look up each unfamiliar mmCIF category in the dictionary (for instance `pdbx_struct_assembly` for biological assemblies) before parsing it.

## Caveats

- The legacy format is frozen and cannot hold large entries: new code should read PDBx/mmCIF.
- Verified in this pass: the PDBx/mmCIF dictionary, version 5.417, read in the wwPDB dictionary repository (wwpdb-dictionaries/mmcif_pdbx on GitHub); the ATOM/HETATM column layout, through search results quoting the format guide (the wwpdb.org pages could not be opened directly); the 2014 format change, the PDB-format limits and the 2019 deposition announcement, by search (wwPDB announcement list, PDBj help page). Other legacy record types were not checked line by line.
