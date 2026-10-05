---
aliases:
  - Accession
  - Accession.Version
  - Sequence Version
  - Stable Identifier
  - Numéro d'accession
tags:
  - type/concept
  - domain/bioinformatics
  - domain/scientific-practice
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Biological Database]]"
  - "[[String]]"
related:
  - "[[Persistent Identifier]]"
  - "[[Identifier Mapping]]"
  - "[[Data Provenance]]"
  - "[[Metadata]]"
  - "[[FASTA Format]]"
  - "[[GenBank Format]]"
  - "[[Reference Genome]]"
  - "[[Variant Nomenclature]]"
  - "[[Regular Expression]]"
  - "[[Programmatic Database Access]]"
projects:
  - "[[bio-core]]"
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[NCBI GenBank]]"
  - "[[NCBI RefSeq]]"
  - "[[Ensembl]]"
  - "[[UniProt]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[Wilkinson 2016 - The FAIR Guiding Principles for Scientific Data Management and Stewardship]]"
  - "[[Sandve 2013 - Ten Simple Rules for Reproducible Computational Research]]"
---

# Accession Number

> [!abstract]
> An accession number is the permanent "name tag" a database gives a record, such as `NM_000546`; the version after the dot (`.6`) says which exact sequence you used, and that is what an analysis must cite.

## Definition

An **accession number** is the stable identifier a [[Biological Database]] assigns to a record; it stays attached to the record when the record is updated. In the nucleotide archives and RefSeq, a record is cited as **accession.version**: the version number increases by one when the sequence of the record is updated,[^genbank] and it persists through updates that do not touch the sequence, such as new references or source information.[^refseq] The accession therefore names a record; accession.version names one exact sequence.

## Why it matters

- **Reproducibility.** A result computed on `NM_000546.6` can be recomputed only on that sequence; the unversioned accession may point to a different one later.
- **Coordinates.** Positions in a transcript or chromosome are positions in one version of its sequence; a new version can shift them (Exercise 3), which matters for [[Variant Nomenclature]] and [[Genomic Coordinate System]].
- **Joins between databases.** Identifiers from different databases name different objects (a transcript, a gene, a protein); linking them is [[Identifier Mapping]], and a bare identifier can even match the format of two databases (see L2).
- **In the Lab.** Headers of [[FASTA Format]] files and the `ACCESSION`/`VERSION` lines of [[GenBank Format]] carry accessions; [[bio-core]] should store them with their version, and [[10-genomic-pipeline]] should refuse unversioned references (Exercise 4).

## Core (L1)

![[accession-number-anatomy.svg]]

**Reading `NM_000546.6`.** `NM` is a RefSeq prefix meaning mRNA, `000546` the record number, `6` the version: the sixth sequence of this record.[^refseq] It is the RefSeq mRNA of the human *TP53* gene; Ensembl describes the matching transcript under its own identifier, `ENST00000269305.9`.[^refseq][^ensembl]

**RefSeq prefixes** (two letters, an underscore, digits):[^refseq]

| Prefix | Molecule | Record type |
|---|---|---|
| `NC_` | complete genomic molecule (for example a chromosome) | known |
| `NG_` | genomic region | known |
| `NM_` / `NR_` | mRNA / non-coding RNA | known |
| `NP_` | protein | known |
| `NT_`, `NW_` | genomic contig or scaffold | known |
| `XM_` / `XR_` / `XP_` | mRNA / non-coding RNA / protein | model (predicted by an automated pipeline) |

**Formats across databases.**

| Database | Accession format | Example | Version |
|---|---|---|---|
| GenBank, ENA, DDBJ (nucleotide) | 1 letter + 5 digits, 2 letters + 6 digits, or 2 letters + 8 digits[^genbank] | `U49845` (NCBI's sample record) | `.n`, +1 when the sequence changes[^genbank] |
| INSDC protein | 3 letters + 5 digits, or 3 letters + 7 digits[^genbank] | | `.n` |
| INSDC whole-genome shotgun | 4 letters + 2 digits (assembly version) + 6 or more digits[^genbank] | `AAAA01000001` (pattern) | |
| RefSeq | prefix + `_` + digits[^refseq] | `NM_000546.6` | `.n` |
| Ensembl | `ENS` + species code (none for human) + feature type (`G` gene, `T` transcript, `P` protein, `E` exon...) + 11 digits[^ensembl] | `ENSMUSG00000017167.6` (mouse gene) | `.n` = number of times the model has changed[^ensembl] |
| UniProtKB | 6 or 10 characters[^uniprot] | `P04637` | |
| PDB | 4 characters; extended form `pdb_` + 8 characters[^pdb] | `1abc` = `pdb_00001abc` | |

**Accessions are not names.** A gene symbol such as *TP53* is a human-readable label, and UniProt's entry name `P53_HUMAN` is a label too: the stable key is the accession, which UniProt defines as the way to identify an entry from release to release.[^uniprot]

## Deeper (L2)

**What a version pins, and what it does not.** Because the version changes only with the sequence,[^refseq] `NM_000546.6` fixes the sequence but not the annotation around it: references and features may be updated under the same version. Record the database release or download date as well. Ensembl follows a different rule: its version counts how many times the gene or transcript **model** has changed,[^ensembl] and Ensembl annotation is released as numbered versions that must be recorded with the assembly.[^ensembl]

**One entry, several accessions.** In UniProt, one entry can be associated with several accession numbers;[^uniprot] a lookup table keyed on a single accession per entry will miss the others.

**Formats overlap.** Accession formats are [[Regular Expression|regular expressions]], and they are not disjoint. `P04637` matches UniProt's documented pattern `[OPQ][0-9][A-Z0-9]{3}[0-9]` and also the INSDC pattern "1 letter + 5 digits"; `ENST00000269305` matches both Ensembl and the whole-genome shotgun pattern (4 letters followed by at least 8 digits). A bare identifier is ambiguous: store it with its **namespace** (the database) and its version.

**Validate, then normalize.** A parser should (1) check the format for a declared namespace, (2) split accession and version, (3) keep the version as an integer so that `.10` sorts after `.9`, and (4) never silently drop it.

## Advanced (L3)

- **Persistent identifiers and FAIR.** The first FAIR principle asks that data and metadata carry globally unique and persistent identifiers.[^fair] An accession is persistent within its database; prefixing it with the database name makes it globally unambiguous ([[Persistent Identifier]], [[FAIR Principles]]).
- **Formats run out.** Identifier spaces are finite. GenBank expanded its protein accessions to 3 letters + 7 digits and introduced a longer whole-genome shotgun format (6 letters + 2 digits + 7 to 9 digits) at the end of 2018, because nearly all shorter accessions had been assigned.[^genbank] The four-character PDB IDs are expected to be fully assigned before 2028, after which new entries receive only extended IDs such as `pdb_00001abc`.[^pdb] Validators must follow the published patterns and be updatable, not hard-code lengths.
- **Provenance.** Keeping track of how every result was produced is the first rule of reproducible computational research;[^sandve] for data, that means a manifest of namespace, accession.version, release and checksum for every input ([[Data Provenance]]).
- **Identifier or content.** An accession.version names a sequence indirectly, through a database. A checksum of the sequence itself (see [[Biological Database#Computational representation]]) identifies content directly and detects silent changes; robust pipelines record both.

## Mathematical representation

- Let $A$ be the accessions of one database and $t$ time. The **current version** $v(a, t) \in \{1, 2, \dots\}$ of accession $a$ is non-decreasing in $t$. The sequence $s(a, k)$ is fixed for each pair $(a, k)$: accession.version is a key for sequences, the accession alone is not, since $s(a, v(a, t))$ depends on $t$.
- **Coordinate shift.** If version $k+1$ inserts $\ell$ bases after position $p$ of version $k$ (1-based), positions map by
$$\varphi(i) = \begin{cases} i & i \le p \\ i + \ell & i > p \end{cases}$$
A deletion is the case $\ell < 0$ for positions after the deleted block. Any coordinate stored without its version is therefore only defined up to such maps.
- **Format languages.** Each accession format is a regular language $L_{db}$ over letters, digits, `_` and `.`. Classifying an identifier $x$ returns $\{db : x \in L_{db}\}$; since $L_{\text{UniProt}} \cap L_{\text{INSDC}} \neq \emptyset$, the result is a set, not a single database.

## Computational representation

A classifier returning every namespace whose documented format matches, with accession and version split:

```python
import re

VERSION = r"(?:\.(?P<version>\d+))?"
PATTERNS = {   # documented formats, anchored on the whole string
    "RefSeq": r"(?P<acc>(?:NC|NG|NM|NR|NP|NT|NW|XM|XR|XP)_\d+)" + VERSION,
    "Ensembl": r"(?P<acc>ENS(?:[A-Z]{3})?(?:E|FM|G|GT|P|R|T)\d{11})" + VERSION,
    "UniProtKB": r"(?P<acc>[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})",
    "INSDC nucleotide": r"(?P<acc>[A-Z]\d{5}|[A-Z]{2}\d{6}|[A-Z]{2}\d{8})" + VERSION,
    "INSDC protein": r"(?P<acc>[A-Z]{3}\d{5}|[A-Z]{3}\d{7})" + VERSION,
    "INSDC WGS": r"(?P<acc>[A-Z]{4}\d{8,}|[A-Z]{6}\d{9,11})" + VERSION,
    "PDB": r"(?P<acc>[0-9][a-z0-9]{3}|pdb_[a-z0-9]{8})",
}
COMPILED = {db: re.compile(p) for db, p in PATTERNS.items()}


def classify(identifier: str) -> list[tuple[str, str, int | None]]:
    """Every namespace whose format matches, with the accession and its version (None if absent)."""
    hits = []
    for db, rx in COMPILED.items():
        m = rx.fullmatch(identifier)
        if m:
            version = m.groupdict().get("version")
            hits.append((db, m["acc"], int(version) if version else None))
    return hits


for ident in ["NM_000546.6", "NM_000546", "ENST00000269305.9", "ENSMUSG00000017167.6",
              "P04637", "AAAA01000001", "pdb_00001abc", "TP53"]:
    print(f"{ident:22}", classify(ident) or "no known format")
```

```text
NM_000546.6            [('RefSeq', 'NM_000546', 6)]
NM_000546              [('RefSeq', 'NM_000546', None)]
ENST00000269305.9      [('Ensembl', 'ENST00000269305', 9), ('INSDC WGS', 'ENST00000269305', 9)]
ENSMUSG00000017167.6   [('Ensembl', 'ENSMUSG00000017167', 6)]
P04637                 [('UniProtKB', 'P04637', None), ('INSDC nucleotide', 'P04637', None)]
AAAA01000001           [('INSDC WGS', 'AAAA01000001', None)]
pdb_00001abc           [('PDB', 'pdb_00001abc', None)]
TP53                   no known format
```

Two identifiers match two namespaces: format checking validates an identifier **once its namespace is known**; it cannot discover the namespace. The Ensembl and UniProt patterns follow the databases' documentation;[^ensembl][^uniprot] the others encode the formats in the table above.

## Worked example

> [!example] Three identifiers for one gene's products
> A collaborator sends: `NM_000546.6`, `ENST00000269305.9`, `P04637`.
> 1. **Namespaces.** The first is RefSeq (prefix `NM_`, an mRNA); the second Ensembl (`ENS`, no species code so human, `T` for transcript); the third UniProtKB. As the classifier shows, the last two also fit other formats, so the collaborator should have written the database names; [[bio-core]] should store each as a typed value `(namespace, accession, version)`, for example `("UniProtKB", "P04637", None)`.
> 2. **Versions.** `.6`: the sixth sequence of the RefSeq record. `.9`: the Ensembl transcript model has changed several times. The UniProt accession carries no version: record the UniProt release instead.
> 3. **Objects.** Two transcripts (from two annotation sources) and one protein. They describe the same gene's products, but the transcript sequences need not be identical base for base, and a protein is not a transcript: joining them is [[Identifier Mapping]], not string equality.
> 4. **Manifest line** for the pipeline: `RefSeq NM_000546.6 downloaded 2026-09-30 sha256=...`.

## Common misconceptions

> [!warning] "When a record is updated, it gets a new accession"
> The accession stays; the version after the dot increases when the sequence changes.[^genbank] That is what lets old citations still find the record.

> [!warning] "Same version, same record content"
> The version tracks the sequence only: references and other non-sequence data can change under the same version.[^refseq] Record the release or download date too.

> [!warning] "Accession lengths are fixed, so validate by length"
> GenBank and the PDB both introduced longer formats as identifier spaces filled up.[^genbank][^pdb] Validate against documented patterns.

## Exercises

> [!question] Exercise 1 (L1)
> Decode each identifier (database, molecule or object, version): `NM_000546.6`, `XP_` followed by digits and `.1`, `NC_` followed by digits and `.11`, `ENSMUSG00000017167.6`.

> [!success]- Solution
> RefSeq mRNA, known record, version 6; RefSeq protein, **model** (predicted) record, version 1; RefSeq complete genomic molecule (such as a chromosome), version 11;[^refseq] Ensembl mouse (`MUS`) gene (`G`), whose model has changed to version 6.[^ensembl]

> [!question] Exercise 2 (L1)
> For a RefSeq record, which of these updates increase the version: (a) a new publication is added; (b) one base is corrected; (c) the organism description is edited; (d) the 3' end is extended by 40 bases?

> [!success]- Solution
> Only (b) and (d): they change the sequence. (a) and (c) are non-sequence updates, and the version persists.[^refseq]

> [!question] Exercise 3 (L2, Python)
> Version 2 of a transcript inserts 3 bases after position 120 of version 1. A collaborator reports features at positions 100, 120, 121 and 250 of "the transcript" without a version. Where are they in version 2?

> [!success]- Solution
> ```python
> def shift(pos: int, insert_after: int, length: int) -> int:
>     """1-based position in version 1 -> position in version 2 after an insertion of `length` bases."""
>     return pos + length if pos > insert_after else pos
>
>
> print([shift(p, 120, 3) for p in (100, 120, 121, 250)])
> ```
> Output: `[100, 120, 124, 253]`. Positions after the insertion move by 3. Without the version you cannot know whether 250 means base 250 or base 253 of the current sequence.

> [!question] Exercise 4 (L3, Python)
> Write a check for [[10-genomic-pipeline]] that refuses to run when a RefSeq identifier in the configuration has no version. Test it on a toy configuration.

> [!success]- Solution
> ```python
> import re
>
> VERSIONED = re.compile(r"^[A-Z]{2}_\d+\.\d+$")        # RefSeq accession.version
> REFSEQ = re.compile(r"^[A-Z]{2}_\d+(\.\d+)?$")
>
> config = {   # toy pipeline configuration (identifiers chosen for the exercise)
>     "reference_transcript": "NM_000546.6",
>     "control_transcript": "NM_000546",
>     "genome": "NC_000017.11",
>     "sample_name": "liver_01",
> }
>
>
> def unversioned(cfg: dict) -> list[str]:
>     """Keys whose value looks like a RefSeq accession but lacks a version."""
>     return [k for k, v in cfg.items() if REFSEQ.match(v) and not VERSIONED.match(v)]
>
>
> problems = unversioned(config)
> print(problems)
> if problems:
>     print("refusing to run: pin a version for", ", ".join(problems))
> ```
> Output: `['control_transcript']`, then `refusing to run: pin a version for control_transcript`. Failing early is cheaper than discovering months later that two runs used different sequences.[^sandve]

> [!question] Exercise 5 (L3)
> The four-character PDB IDs will run out and new entries will get only `pdb_` + 8 characters.[^pdb] List what breaks in a program that validates PDB IDs with `len(x) == 4`, and how you would test the fix.

> [!success]- Solution
> The validator rejects every new ID; file names, database columns sized for 4 characters and regular expressions such as `^[0-9][a-z0-9]{3}$` fail too. Fix: accept both documented forms and normalize classic IDs to the extended one (`1abc` → `pdb_00001abc`). Test with examples of both forms, round trips (classic → extended → display), and [[Property-Based Testing|property-based tests]] that generate valid and invalid strings.

## Mastery checklist

- [ ] 1 Recognized: I can point to the prefix, number and version in `NM_000546.6` and name the database of common identifiers.
- [ ] 2 Understood: I can explain what a version pins (the sequence) and what it does not (annotation), and why analyses cite accession.version.
- [ ] 3 Practiced: I can validate and split identifiers with regular expressions and detect ambiguous ones.
- [ ] 4 Applied: [[bio-core]] stores identifiers as (namespace, accession, version), and [[10-genomic-pipeline]] refuses unversioned references.
- [ ] 5 Explained: I can teach how identifier formats evolve, why formats overlap, and how identifiers and checksums together give provenance.

## References

[^genbank]: [[NCBI GenBank]], NCBI documentation of accession number prefixes and formats (including the 2018 expanded formats) and of accession.version.
[^refseq]: [[NCBI RefSeq]], NLM documentation of the RefSeq accession format, prefixes and versions; RefSeq record NM_000546.
[^ensembl]: [[Ensembl]], help page "Stable IDs" (format, species and feature-type prefixes, versions) and "Ensembl 2025" (*Nucleic Acids Research*).
[^uniprot]: [[UniProt]], help page on accession numbers (stability across releases, 6- and 10-character formats and their regular expression, several accessions per entry).
[^pdb]: [[RCSB Protein Data Bank]], wwPDB documentation on extended PDB IDs.
[^fair]: [[Wilkinson 2016 - The FAIR Guiding Principles for Scientific Data Management and Stewardship]], *Scientific Data*.
[^sandve]: [[Sandve 2013 - Ten Simple Rules for Reproducible Computational Research]], *PLoS Computational Biology*, rule 1.
