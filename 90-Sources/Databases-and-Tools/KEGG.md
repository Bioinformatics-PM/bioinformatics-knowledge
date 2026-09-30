---
aliases:
  - Kyoto Encyclopedia of Genes and Genomes
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
kind: database
tier: A
authors:
  - Minoru Kanehisa
institution: Kanehisa Laboratories
year: 1995
edition:
url: https://www.kegg.jp/kegg/
access: free
---

# KEGG

> [!abstract]
> A database resource that links genes, proteins and chemical substances to "molecular wiring diagrams" of interaction and reaction networks, to interpret genomes at the level of cells, organisms and ecosystems.

## Why this source

KEGG pathway maps are the standard picture of metabolism in bioinformatics: each enzyme box on a map links to the genes that encode it in each sequenced organism. That makes KEGG the bridge between a biochemistry course (a [[Metabolic Pathway]] on paper) and genome data (which enzymes an organism actually has).

> [!info] History
> KEGG was initiated in 1995 by Minoru Kanehisa at the Institute for Chemical Research, Kyoto University, under the Japanese Human Genome Program; its first release was on 1 December 1995. From the start it mapped genomes onto metabolic pathways through EC numbers (metabolic reconstruction).

## Coverage

Key publication: Kanehisa M, Furumichi M, Sato Y, Matsuura Y, Ishiguro-Watanabe M. "KEGG: biological systems database as a model of the real world". *Nucleic Acids Res* 53:D672-D677 (2025). KEGG is described as a computer model of the biological system with three layers: genomic information (genes and proteins), chemical information (substances), and systems information (interaction and reaction networks).

| Part | Content | Vault notes |
|---|---|---|
| Pathway maps (systems information) | Interaction and reaction networks | [[Metabolic Pathway]], [[Metabolic Network]], [[Glycolysis]], [[Citric Acid Cycle]] |
| Genes and genomes (genomic information) | Genes linked to map elements, per organism | [[Genome]], [[Gene Annotation]] |
| Compounds and reactions (chemical information) | Metabolites and the reactions linking them | [[Metabolism]], [[Enzyme]] |
| Diseases and drugs | Disease and drug databases | [[Drug Discovery]] |
| Metabolic reconstruction | Mapping a genome onto pathways via EC numbers | [[Systems Biology]] |

## How to use it

- **L2**: open the glycolysis map while studying [[Glycolysis]] in biochemistry; click an enzyme box and follow it to its genes in human and in a bacterium.
- **L3**: compare the same map across two organisms and list the enzymes one of them lacks; relate this to [[Gene Annotation]] quality.
- **M1**: use KEGG maps to interpret a gene or metabolite list from an omics experiment, alongside [[Gene Ontology]] terms.

## Caveats

- A reference map shows what is known across organisms; check which genes are actually present in yours before drawing conclusions.
- Terms of use for automated or bulk download may differ from free web browsing: read KEGG's licensing page before scripting against it.
- Verified in this pass: the 2025 NAR citation and description, and the 1995 origin (KEGG overview pages and secondary sources).
