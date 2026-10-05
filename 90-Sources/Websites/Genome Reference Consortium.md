---
aliases:
  - GRC
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - Genome Reference Consortium
institution: Wellcome Sanger Institute, McDonnell Genome Institute (Washington University), EMBL-EBI and NCBI
year:
edition:
url: "https://www.ncbi.nlm.nih.gov/grc"
access: free
---

# Genome Reference Consortium

> [!abstract]
> The consortium that maintains the human, mouse and zebrafish reference assemblies (GRCh37, GRCh38, GRCm38 and their patches), and its website of assembly releases, definitions and patch notes.

## Why this source

The GRC is the producer of the human reference assemblies that most coordinates in human data refer to. It is a collaboration of the Wellcome Sanger Institute, the McDonnell Genome Institute at Washington University, EMBL-EBI and NCBI, which closes gaps, fixes errors and represents complex variation in the references. Its site defines the vocabulary of an assembly release (primary assembly, alternate loci, patches) that file formats reuse: the SAM specification points to the GRC definitions for "alternate locus" and "primary assembly".

## Coverage

Key publication: Schneider VA, Graves-Lindsay T, Howe K, et al. "Evaluation of GRCh38 and de novo haploid genome assemblies demonstrates the enduring quality of the reference assembly". *Genome Research* 27(5):849-864 (2017). doi:10.1101/gr.213611.116. Free full text at PMC5411779. Its abstract states that GRCh38 is the first coordinate-changing update of the human reference since 2009, that it resolved roughly 1,000 issues (from single-base changes to megabase-scale path reorganizations, gap closures and newly localized sequences), that it is the first human reference with sequence-based representations of the centromeres, and that it expanded the alternate loci to represent population variation better; it also finds that the reference still gave the best representation of complex regions and coding sequences compared with the de novo long-read assemblies of the time.

| Part | Content | Vault notes |
|---|---|---|
| Assembly releases | Major releases change coordinates (GRCh37, GRCh38) | [[Reference Genome]], [[Genomic Coordinate System]] |
| Patches | Minor releases (GRCh38.p14, 3 February 2022): FIX patches correct the reference, NOVEL patches add alternate representations; chromosome coordinates do not change | [[Reference Genome]] |
| Definitions | Primary assembly, alternate loci, assembly units | [[Reference Genome]], [[SAM Format]] |
| GRCh38 paper | Changes from GRCh37, centromere models, alternate loci, comparison with long-read assemblies | [[Reference Genome]], [[Genome Assembly]] |

Cited in [[Reference Genome]].

## How to use it

- L1: read the human assembly page to see which release and patch is current, and what a patch is.
- L2: read the abstract and introduction of Schneider et al. (2017) for what changed between GRCh37 and GRCh38.
- L3: compare with [[Nurk 2022 - The Complete Sequence of a Human Genome]], the gapless T2T-CHM13 assembly produced outside the GRC.

## Caveats

- The GRC maintains the GRCh assemblies; T2T-CHM13 is a separate assembly from the Telomere-to-Telomere consortium.
- Patch counts change with each patch release; quote them with the release number.
- Verified in this pass (by web search, the site itself could not be opened): the four member institutes, the scope (human, mouse, zebrafish), the patch definitions and the GRCh38.p14 release date; the citation and abstract of Schneider et al. (2017). Counts of alternate loci were not verified from the GRC site and are not quoted.
