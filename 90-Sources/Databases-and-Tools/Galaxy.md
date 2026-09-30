---
aliases:
  - Galaxy Project
  - usegalaxy.org
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
kind: tool
tier: C
authors:
  - Anton Nekrutenko
  - James Taylor
institution: Galaxy Project (open-source community, started at Penn State)
year:
edition:
url: https://galaxyproject.org
access: free
---

# Galaxy

> [!abstract]
> An open web platform for accessible, reproducible and shareable data analysis, deployed worldwide mostly through free public servers, with its own training network.

## Why this source

Galaxy lets a learner run real bioinformatics tools on real data from a browser, then save every step as a history or workflow that others can rerun. It is a way to see a complete analysis working before scripting one, and a reference point for what a reproducible pipeline must record. Tier C: it is a tool; its tutorials are not a primary source for concept claims.

> [!info] History
> Galaxy was started by Anton Nekrutenko and James Taylor at Penn State; the first commit to the repository dates from 1 June 2005. Large public deployments include usegalaxy.org (US), usegalaxy.eu (Europe) and usegalaxy.org.au (Australia).

## Coverage

Key publication: "The Galaxy platform for accessible, reproducible, and collaborative data analyses: 2024 update". *Nucleic Acids Res* (July 2024). It describes tool and reference-data diversity, accessibility and tool discovery (Galaxy Labs, a redesigned ToolShed), GPU access and licensed tools, secure sharing and publishing of data and workflows, the growth of the Galaxy Training Network (learning paths linked to tools), and per-job CO2 estimates.

| Part | Content | Vault notes |
|---|---|---|
| Tools in the browser | Analysis tools and reference datasets | [[Next-Generation Sequencing]], [[Read Mapping]], [[Variant Calling]] |
| Histories and workflows | Recorded, rerunnable analyses | [[Workflow Management System]], [[Reproducibility]], [[10-genomic-pipeline]] |
| Sharing | Publishing data and workflows | [[Research Data Management]] |
| Galaxy Training Network | Tutorials and learning paths | [[Bioinformatics]] |

## How to use it

- **L2**: create an account on a public server, upload a small [[FASTA Format|FASTA]] or [[FASTQ Format|FASTQ]] file, run one tool, and inspect the history it records; follow an introductory training tutorial.
- **L3**: rebuild the steps of [[10-genomic-pipeline]] as a Galaxy workflow (if the tools you need are on the server) and compare it with your scripted version: which parameters and versions does each record?
- **M1**: share a workflow and its history with the results of a project, so another person can rerun it.

## Caveats

- Check the usage limits of the public server you use before uploading large datasets.
- Tool versions change: export workflows with their versions to keep results reproducible.
- Launch year of the public service and the 2024 paper's author list were not verified in this pass.
