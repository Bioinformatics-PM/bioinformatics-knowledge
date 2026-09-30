---
aliases:
  - hts-specs
  - VCF specification
  - SAM specification
tags:
  - type/source
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - GA4GH Large Scale Genomics work stream
institution: Global Alliance for Genomics and Health (GA4GH)
year:
edition:
url: "https://samtools.github.io/hts-specs/"
access: free
---

# HTS Format Specifications

> [!abstract]
> The canonical specifications of the high-throughput sequencing file formats (SAM, BAM, CRAM, VCF, BCF and their indexes), maintained by the GA4GH Large Scale Genomics work stream.

## Why this source

When a tool and a tutorial disagree about a field, the specification decides. The hts-specs repository holds the reference documents for the formats that every sequencing pipeline reads and writes: SAMv1 (SAM, BAM and the BAI index), SAMtags, CRAMv3, VCFv4.x (textual VCF and binary BCF), and quick references for the tabix and CSI indexes.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| VCF and BCF | Variant records, header, per-sample genotype fields | [[VCF Format]], [[Genotype]], [[Allele]] |
| SAM, BAM, CRAM | Alignment records, tags, compressed forms | [[SAM Format]] |
| Indexes | BAI, tabix, CSI | [[Genomic File Indexing]] |

Verified content of the VCF specification (genotype field `GT`):

- alleles are encoded as values separated by `/` (unphased) or `|` (phased, according to the phase set given in `PS`);
- `0` is the reference allele (the `REF` field), `1` the first allele listed in `ALT`, `2` the second, and so on;
- haploid calls, for example on Y, on the male non-pseudoautosomal X or on the mitochondrion, give a single allele value;
- a call that cannot be made is written `.` for each missing allele (`./.` for a diploid genotype, `.` for a haploid one).

Cited in [[Genotype]], [[Allele]], [[Ploidy]] and [[Chromosome]].

## How to use it

- L2: read the VCF specification's description of the fixed columns and of the genotype fields next to a real VCF file ([[VCF Format]]).
- L3: check edge cases (multiallelic sites, haploid regions, phase sets, missing data) in the specification before writing a parser or a filter.

## Caveats

- Versions matter: VCFv4.5 is listed as the canonical VCF specification at the time of this pass, and earlier versions (4.2, 4.3, 4.4) are still produced by many tools. Record the `##fileformat` line of every file.
- The format was developed for the 1000 Genomes Project and described in Danecek P et al., "The variant call format and VCFtools", *Bioinformatics* 27:2156-2158 (2011), doi:10.1093/bioinformatics/btr330.
- Section numbers of the specifications change between versions; cite the version when quoting a rule.
- Verified in this pass: repository scope and maintainers, the list of specifications, and the `GT` encoding rules above.
