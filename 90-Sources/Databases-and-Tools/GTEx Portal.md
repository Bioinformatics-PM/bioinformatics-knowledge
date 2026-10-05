---
aliases:
  - GTEx
  - Genotype-Tissue Expression
  - GTEx Project
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - GTEx Consortium
institution: NIH Common Fund
year: 2020
edition:
url: "https://gtexportal.org/home/"
access: free
---

# GTEx Portal

> [!abstract]
> The data portal of the Genotype-Tissue Expression (GTEx) project, an NIH Common Fund atlas of gene expression and its genetic regulation across many tissues of the same post-mortem human donors.

## Why this source

GTEx is the standard reference for the question "in which human tissues is this gene expressed, and do genetic variants change that expression?". Because every donor contributes many tissues, it separates tissue effects from donor effects, which no single-tissue study can do. It is the natural first dataset for [[Tissue]]-level expression, tissue specificity and [[Expression Quantitative Trait Locus|eQTL]] mapping.

## Coverage

Key publication: The GTEx Consortium. "The GTEx Consortium atlas of genetic regulatory effects across human tissues". *Science* 369(6509) (2020). Its analysis used 15,201 RNA-sequencing samples from 49 tissues of 838 post-mortem donors, characterized genetic associations with expression and splicing in cis and trans, reported regulatory associations for almost all genes, and showed that cell type composition is a key factor in interpreting regulatory effects in tissues.

The V8 release behind that paper contains 17,382 RNA-sequencing samples from 54 tissues (including 2 cell lines) of 948 post-mortem donors.

| Part | Content | Vault notes |
|---|---|---|
| Expression atlas | Gene and transcript expression per tissue | [[Tissue]], [[Gene Expression]], [[RNA Sequencing]] |
| Genetic regulation | eQTLs and splicing QTLs per tissue | [[Expression Quantitative Trait Locus]] |
| Composition | Cell type composition of bulk tissue samples | [[Cell-Type Deconvolution]], [[Cell Type]] |

Cited in [[Tissue]], [[Organ System]] and [[Nervous System]].

## How to use it

- L2: look up a few genes in the portal's tissue expression view and decide whether each is broadly or tissue-specifically expressed.
- L3: download the gene-by-sample expression matrix and sample attributes, compute a tissue-specificity score, and compare the eQTLs of one gene across tissues.

## Caveats

- Donors are post-mortem: tissue collection and death circumstances are variables to account for, and some tissues (such as brain) are sampled only this way.
- Bulk tissue mixes cell types; an apparent tissue difference can be a composition difference (the 2020 paper's own conclusion).
- Verified in this pass (web search): the 2020 paper's title, journal, volume and issue, and its sample, tissue and donor counts; the V8 counts; the portal URL; the NIH Common Fund program. The DOI, page numbers and the access conditions of individual-level genotype data were not verified.
