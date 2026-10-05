---
aliases:
  - GO
  - GO knowledgebase
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
kind: database
tier: A
authors: []
institution: Gene Ontology Consortium
year:
edition:
url: https://geneontology.org
access: free
---

# Gene Ontology

> [!abstract]
> A species-agnostic, structured vocabulary of gene-product functions, with evidence-supported annotations linking genes from across the tree of life to its terms.

## Why this source

GO is the standard way to say *what a gene does* in a form a computer can compare across organisms and databases. It is the working example for the vault's [[Biological Ontology]] note and underlies most functional interpretation of gene lists.

## Coverage

Key publication: Gene Ontology Consortium. "The Gene Ontology knowledgebase in 2023". *Genetics* 224(1) (2023). The knowledgebase has three components: (1) the ontology itself, (2) GO annotations, evidence-supported statements that a gene product has a given function, and (3) GO Causal Activity Models (GO-CAMs), which link several annotations into mechanistic models of biological processes. The GO documentation adds the three aspects and the evidence codes.

| Part | Content | Vault notes |
|---|---|---|
| Ontology | Terms and the relations between them | [[Biological Ontology]] |
| Molecular Function | Activities of gene products (for example "protein kinase activity") | [[Enzyme]], [[Protein]] |
| Cellular Component | Where the function takes place (membrane, mitochondrion) | [[Cell]] |
| Biological Process | Series of events accomplished by ordered molecular functions | [[Metabolic Pathway]], [[Gene Regulation]] |
| Annotations and evidence | Six evidence categories; experimental codes EXP, IDA, IPI, IMP, IGI, IEP | [[Gene Annotation]] |
| GO-CAM | Causal models linking annotations | [[Systems Biology]] |

## How to use it

- **L2**: look up the annotations of one well-studied gene; sort them by aspect and note the evidence code of each.
- **L3**: browse a term's parents and children to see the graph structure; read the GO documentation on how annotations relate to parent terms.
- **M1**: run a term-enrichment analysis on a gene list from an expression study, with [[Multiple Testing Correction|Multiple Testing]] correction, and question every enriched term.

## Caveats

- Knowledge is biased toward a small number of model organisms, where most experiments were done.
- Automatically generated annotations are not experimental evidence: filter by evidence code when it matters.
- The ontology changes between releases; record the release used in any analysis.
- Launch year was not verified in this pass. Verified: the 2023 *Genetics* paper and the GO documentation pages (aspects, evidence codes).
