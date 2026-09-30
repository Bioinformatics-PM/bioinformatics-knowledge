---
aliases:
  - Universal Protein Resource
  - UniProtKB
  - Swiss-Prot
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
kind: database
tier: A
authors: []
institution: UniProt Consortium (EMBL-EBI, SIB, PIR)
year:
edition:
url: https://www.uniprot.org
access: free
---

# UniProt

> [!abstract]
> The central knowledgebase of protein sequences and functional annotation, maintained by a consortium of EMBL-EBI, the SIB Swiss Institute of Bioinformatics and the Protein Information Resource (PIR).

## Why this source

UniProt is where a protein is described as a biological object: sequence, function, cross-references to structures, genes and literature. Its split between manually reviewed and automatically annotated entries is also the clearest lesson in the vault on evidence quality in a [[Biological Database]].

> [!info] History
> In 2002 the Swiss-Prot and TrEMBL groups (SIB and EBI) and the PIR group joined as the UniProt consortium. UniProtKB has two sections: **Swiss-Prot** (manually annotated, curator-reviewed) and **TrEMBL** (computationally analysed, awaiting manual annotation).

## Coverage

Key publication: "UniProt: the Universal Protein Knowledgebase in 2025". *Nucleic Acids Res* 53(D1):D609-D617 (2025). doi:10.1093/nar/gkae1010. It describes restricting UniProtKB to high-quality, non-redundant reference proteomes, literature curation assisted by machine learning, community curation, automatic annotation of unreviewed entries, and a new website tab linking proteins to genomic information.

| Part | Content | Vault notes |
|---|---|---|
| Swiss-Prot (reviewed) | Manually curated entries | [[Protein]], [[Gene Annotation]] |
| TrEMBL (unreviewed) | Automatically annotated entries | [[Gene Annotation]] |
| Reference proteomes | Non-redundant protein sets per organism | [[Proteomics]], [[Genome]] |
| Cross-references | Structures, genes, literature | [[RCSB Protein Data Bank]], [[AlphaFold Protein Structure Database]] |

## How to use it

- **L1**: search a protein you meet in biochemistry (for example hemoglobin), and read the function, sequence and cross-reference sections of the reviewed entry.
- **L2**: download reviewed protein sequences in [[FASTA Format]] as test data for [[04-alignment-engine]] and [[05-sequence-search]]; in [[06-mutation-lab]], check what is known about the protein a mutation lands in.
- **L3**: compare a reviewed and an unreviewed entry of related proteins and list which statements are curated and which are predicted.

## Caveats

- Unreviewed (TrEMBL) annotations are predictions: never cite them as established function.
- Because UniProtKB is being limited to reference proteomes, some sequences leave it over time; record accession and release.
- Launch year and the paper's author list were not verified in this pass. Verified: the 2025 paper's citation and abstract, and the 2002 formation of the consortium.
