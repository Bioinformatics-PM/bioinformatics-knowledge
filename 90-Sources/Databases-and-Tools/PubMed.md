---
aliases: []
tags:
  - type/source
  - domain/scientific-practice
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
  - level/M1
kind: database
tier: A
authors: []
institution: NCBI/NLM/NIH
year: 1996
edition:
url: https://pubmed.ncbi.nlm.nih.gov/
access: free
---

# PubMed

> [!abstract]
> NCBI's free search engine over citations and abstracts of the biomedical and life-science literature, online since 1996.

## Why this source

Every primary paper cited in the vault (the landmark papers in `90-Sources/Papers/`, the database papers in this folder) can be found, checked and linked from PubMed. Learning to search it well is a core skill of [[Scientific Practice]]: it is how a learner moves from a textbook statement to the paper behind it.

## Coverage

Source: the PubMed About page. PubMed contains more than 40 million citations and abstracts. It does not host full text, but links to it when available (publisher sites, PubMed Central). Citations come mainly from biomedicine and health, plus the life, behavioral and chemical sciences and bioengineering. MEDLINE, its largest component, consists mainly of citations from selected journals, indexed with MeSH (Medical Subject Headings) and curated with funding, genetic and chemical metadata.

| Part | Content | Vault notes |
|---|---|---|
| Citations and abstracts | Search over the biomedical literature | [[Scientific Literature]] |
| MEDLINE and MeSH | Controlled-vocabulary indexing of journal articles | [[Biological Ontology]] |
| Full-text links | Publisher sites, PubMed Central | [[NCBI]], [[NCBI Bookshelf]] |
| Programmatic search | NCBI E-utilities | [[Biopython]] |
| Landmark papers | Primary literature already in the vault | [[Altschul 1990 - Basic Local Alignment Search Tool]], [[Watson 1953 - Molecular Structure of Nucleic Acids]] |

## How to use it

- **L1**: look up the landmark papers already listed in `90-Sources/Papers/` and read their abstracts; note the journal, year and DOI.
- **L2**: when writing a concept note, search for a recent review on the topic and compare its framing with your textbook.
- **L3**: combine keyword and MeSH searches to narrow a topic; keep the final query in your notes so you can rerun it later.
- **M1**: script searches with `Bio.Entrez` ([[Biopython]]) to build a small literature dataset.

## Caveats

- PubMed indexes citations and abstracts, not full texts: an abstract is never enough to support a precise claim in a concept note.
- Presence in PubMed is not a quality label; judge a paper by its content, venue and later citations.
- Verified in this pass: the About page (size, scope, MEDLINE, availability since 1996, maintenance by NCBI at the NLM).
