---
aliases: []
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
kind: book
tier: A
authors:
  - Vince Buffalo
institution: O'Reilly Media
year: 2015
edition: "1st"
url: "https://www.oreilly.com/library/view/bioinformatics-data-skills/9781449367480/"
access: paid
---

# Bioinformatics Data Skills (Buffalo)

> [!abstract]
> A practical book on the computational and data skills of day-to-day bioinformatics: Unix pipelines, file formats, genomic ranges, R, Git and robust, reproducible scripts.

## Why this source

It fills the gap between knowing a scripting language and actually doing bioinformatics. Written by a bioinformatician from the UC Davis Genome Center's Bioinformatics Core, it teaches with real genomics files and tools, and it treats reproducibility and robustness as part of the skill set rather than an afterthought. It is the most direct book for Stage 1 of [[Computer Systems]].

## Coverage

Citation: Buffalo V. *Bioinformatics Data Skills: Reproducible and Robust Research with Open Source Tools*. O'Reilly Media (2015). Coverage is described by topic; chapter titles were not verified in this pass.

| Part | Content | Vault notes |
|---|---|---|
| Unix and the shell | Unix pipelines and text processing on bioinformatics data, working on remote machines | [[Unix Shell]], [[Unix Text Processing]], [[Secure Shell]] |
| Robust scripts | Bash scripts and Makefiles | [[Shell Script]], [[Workflow Management System]] |
| Reproducibility | Project organization and Git | [[Computational Project Organization]], [[Version Control]] |
| Data | Exploratory data analysis in R | [[R Programming]] |
| Genomics formats | FASTA, FASTQ, SAM and BAM; genomic ranges | [[FASTA Format]], [[FASTQ Format]], [[SAM Format]] |

Cited in [[Computer Systems]].

## How to use it

- L1: read the Unix chapters with a terminal open and redo every command on a small FASTQ file.
- L2: use the formats and genomic ranges chapters when starting [[10-genomic-pipeline]].

## Caveats

- Published in 2015: some tool versions and R packages have changed; the principles have not.
- Needs prior experience with a scripting language such as Python.
- Verified in this pass: title, author, publisher, year, ISBN and topics from the publisher description.
