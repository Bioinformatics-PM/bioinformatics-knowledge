---
aliases:
  - VCF
  - Variant Call Format
  - BCF
  - BCF Format
  - Format VCF
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Genomic Coordinate System]]"
  - "[[Reference Genome]]"
  - "[[Allele]]"
  - "[[Genotype]]"
  - "[[Delimited Text Format]]"
related:
  - "[[SAM Format]]"
  - "[[Genetic Variant]]"
  - "[[Variant Calling]]"
  - "[[Variant Normalization]]"
  - "[[Variant Annotation]]"
  - "[[Variant Filtering]]"
  - "[[Genotype Likelihood]]"
  - "[[Haplotype Phasing]]"
  - "[[Ploidy]]"
  - "[[Indel]]"
  - "[[Structural Variant]]"
  - "[[Joint Genotyping]]"
  - "[[Genomic File Indexing]]"
projects:
  - "[[03-genome-diff]]"
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[GA4GH hts-specs]]"
  - "[[Tan 2015 - Unified Representation of Genetic Variants]]"
  - "[[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]]"
  - "[[HTSlib]]"
  - "[[Integrative Genomics Viewer]]"
---

# VCF Format

> [!abstract]
> VCF is the tab-separated text format of genetic variants: `##` header lines declare every field, then each data line describes one site (CHROM, POS, REF, ALT, QUAL, FILTER, INFO) followed by one genotype column per sample, where `0/1` means one copy of the reference allele and one of the first alternate allele.

## Definition

The **Variant Call Format** (VCF) is a text file format, usually stored compressed, made of meta-information lines (prefixed `##`), one header line (prefixed `#`) and data lines, each describing a position in the genome and, optionally, the genotypes of samples at that position; fields are tab-separated and an empty value is written `.`.[^vcf1] The current version is VCFv4.5; **BCF** (BCFv2.2) is its binary, compressed counterpart.[^bcf] Positions are 1-based ([[Genomic Coordinate System]]).[^fixed]

## Why it matters

- **The currency of variation.** [[Variant Calling]] turns alignments ([[SAM Format]]) into VCF, and annotation, filtering and population analyses read it ([[Variant Annotation]], [[Variant Filtering]], [[Genetic Variant]]); IGV displays VCF tracks.[^igv] In the Lab, [[03-genome-diff]] writes VCF, [[09-genome-browser]] draws it and [[10-genomic-pipeline]] produces it from BAM.
- **One variant, several spellings.** The same indel in a repeat can be written at different positions, so two call sets can only be compared after normalization ([[Variant Normalization]]).[^tan]
- **Scale.** The specification itself notes that text VCF is big and slow: a batch of a hundred exomes takes a few gigabytes, thousands of exomes hundreds of gigabytes; hence BCF, compression and indexes ([[Genomic File Indexing]]).[^bcf]
- **Genotypes with uncertainty.** Each sample column can carry, beyond the called genotype, its quality and the likelihood of every possible genotype ([[Genotype Likelihood]]).[^gt]

## Core (L2)

### The specification's example

```text
##fileformat=VCFv4.5
##fileDate=20090805
##source=myImputationProgramV3.1
##reference=file:///seq/references/1000GenomesPilot-NCBI36.fasta
##contig=<ID=20,length=62435964,assembly=B36,md5=f126cdf8a6e0c7f379d618ff66beb2da,species="Homo sapiens",taxonomy=x>
##phasing=partial
##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">
##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
##FILTER=<ID=q10,Description="Quality below 10">
##FILTER=<ID=s50,Description="Less than 50% of samples have data">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
#CHROM POS     ID        REF    ALT     QUAL FILTER INFO                              FORMAT      NA00001        NA00002        NA00003
20     14370   rs6054257 G      A       29   PASS   NS=3;DP=14;AF=0.5;DB;H2           GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
20     17330   .         T      A       3    q10    NS=3;DP=11;AF=0.017               GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3   0/0:41:3
20     1110696 rs6040355 A      G,T     67   PASS   NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ 1|2:21:6:23,27 2|1:2:0:18,2   2/2:35:4
20     1230237 .         T      .       47   PASS   NS=3;DP=13;AA=T                   GT:GQ:DP:HQ 0|0:54:7:56,60 0|0:48:4:51,51 0/0:61:2
20     1234567 microsat1 GTC    G,GTCT  50   PASS   NS=3;DP=9;AA=G                    GT:GQ:DP    0/1:35:4       0/2:17:2       1/1:40:3
```

Columns are aligned with spaces for display; the file uses tabs. The five records are a simple SNP, a SNP filtered out for low quality, a site with two alternate alleles, a site called monomorphic reference, and a microsatellite with a deletion and an insertion allele; the first two samples are phased, the third is not.[^example]

### Meta-information and header line

- `##fileformat=VCFv4.5` is required and must be the first line.[^meta]
- **Structured lines** declare fields: `##INFO=<ID,Number,Type,Description>`, `##FORMAT=<...>` with the same keys, `##FILTER=<ID,Description>`. `Number` is an integer, or `A` (one value per alternate allele), `R` (one per allele, reference included), `G` (one per possible genotype) or `.` (variable). `Type` is Integer, Float, Flag (with `Number=0`), Character or String.[^meta][^info]
- **`##contig=<ID,length,md5,...>`** describes each reference sequence, with an MD5 computed as in SAM; recommended in VCF, required in BCF. Contig names follow the SAM rules for reference names.[^contig]
- The **header line** names the 8 fixed columns, `#CHROM POS ID REF ALT QUAL FILTER INFO`, followed, if genotypes are present, by `FORMAT` and one column per sample, without duplicate sample names.[^headerline]

### The 8 fixed fields

| Field | Content |
|---|---|
| `CHROM` | reference sequence name; all records of one CHROM form a contiguous block |
| `POS` | 1-based position of the first base of REF; sorted within each CHROM; 0 or $N + 1$ for telomeres |
| `ID` | identifiers, such as dbSNP rs numbers, separated by `;`, or `.` |
| `REF` | reference base(s), each A, C, G, T or N |
| `ALT` | comma-separated alternate alleles: bases, `*` (allele missing because of an overlapping deletion), a symbolic `<ID>`, a breakend, or `.` if there is none |
| `QUAL` | Phred-scaled quality of the assertion made in ALT: $-10\log_{10}\Pr(\text{no variant})$ when ALT is not `.` |
| `FILTER` | `PASS`, or the `;`-separated list of filters that failed, or `.` if no filter was applied |
| `INFO` | `;`-separated `key=value` items or flags, declared in the header |

[^fixed]

Some INFO keys are reserved: `AC` (allele count in the genotypes, Number A), `AN` (number of alleles in called genotypes), `AF` (frequency of each ALT allele, *estimated from primary data, not from the called genotypes*), `DP` (combined depth), `NS` (samples with data), `DB` (dbSNP membership).[^fixed]

### Genotype columns

`FORMAT` lists colon-separated keys, `GT` first when present; each sample column gives the values in that order, `.` when missing, and trailing fields may be dropped (but not `GT`).[^gt]

| Key | Number | Meaning |
|---|---|---|
| `GT` | 1 | allele indices, 0 for REF, 1 for the first ALT, 2 for the second...; separated by a slash (unphased) or a vertical bar (phased); one index per chromosome copy; `.` for a missing allele |
| `AD` | R | read depth for each allele |
| `DP` | 1 | read depth at this position for this sample |
| `GQ` | 1 | conditional genotype quality: $-10\log_{10}\Pr(\text{genotype call wrong} \mid \text{site variant})$ |
| `GL` | G | $\log_{10}$ likelihoods of all possible genotypes |
| `PL` | G | Phred-scaled genotype likelihoods, rounded to integers |
| `PS` | 1 | phase set: phased genotypes sharing a PS on one chromosome form one haplotype block |

[^gt]

Ploidy is read from GT: `1` is a haploid call (Y, male non-pseudoautosomal X, mitochondria), `0/0/1` a triploid one, `./.` a diploid call that could not be made ([[Ploidy]], [[Genotype]], [[Haplotype Phasing]]).[^gt]

### Indels need a padding base

REF and ALT may not be empty, so an insertion or deletion includes the base **before** the event, reflected in POS (the base after, if the event is at position 1). The specification's own example, on the reference `a t C g a` (positions 1 to 5):[^fixed][^repr]

| Event | POS | REF | ALT |
|---|---:|---|---|
| C → G substitution at 3 | 3 | `C` | `G` |
| deletion of the C at 3 | 2 | `TC` | `T` |
| insertion of A after the C | 3 | `C` | `CA` |

The deleted bases therefore start at POS + 1 ([[Indel]], [[Genomic Coordinate System#Worked example]]).

## Advanced (L3)

**One record, one set of haplotypes.** A record lists all segregating alleles at a locus: each ALT haplotype is obtained by replacing the REF bases at POS with the ALT bases.[^hap] Records are "dynamically typed": SNP, indel, mixed or reference site follows from the alleles, as in the microsatellite record `GTC → G,GTCT` (a 2-base deletion and a 1-base insertion).[^repr] The base-level alignment between alleles is not stored, so equivalent placements of an indel in a repeat all describe the same haplotype; Tan et al. define a **normalized** record as left-aligned and parsimonious, which makes representations comparable (Exercise 5).[^tan][^repr]

**Genotype order.** G-numbered fields (GL, PL) list one value per unordered genotype, in a fixed order: for a diploid with $N$ alternate alleles, `00, 01, 11, 02, 12, 22, ...`, the genotype $a/b$ ($a \le b$) sitting at index $b(b+1)/2 + a$.[^gt] Splitting a multiallelic record into biallelic ones must subset every A, R and G field accordingly.

**Symbolic alleles.** Structural variants use `<DEL>`, `<INS>`, `<DUP>`, `<INV>` or `<CNV>` (with subtypes such as `<DUP:TANDEM>`) or breakend notation, and POS is then the base preceding the event ([[Structural Variant]]).[^alt]

**Reference blocks (gVCF).** To report evidence at non-variant positions too, a record can use the unspecified allele `<*>` and a per-sample length `LEN`: the block says "reference, with these likelihoods, against any other allele". `<NON_REF>` is read as an alias of `<*>`, and INFO `END`, now deprecated, was the older way to give the block length. This is what [[Joint Genotyping]] of many samples starts from.[^gvcf]

**BCF and indexes.** BCF2 is a typed binary encoding of VCF in BGZF blocks: all contigs and all INFO and FORMAT fields must be fully declared in its header, and it is indexed with the same scheme as BAM.[^bcf] A bgzip-compressed VCF is indexed with tabix, whose index takes the end of a record as POS plus the size of the deletion ([[Genomic File Indexing]]).[^tabix][^htslib]

## Frontier (M1)

VCF 4.5 answers two pressures of current data:[^changes][^gt]

- **Cohorts of many samples.** A site may accumulate many alternate alleles, while each sample carries one or two; PL then grows quadratically with the allele count. **Local alleles** (`LAA` lists the ALT alleles relevant to a sample; `LAD`, `LPL`... are expressed on them) shrink multi-sample files and allow lossless merging (Exercise 6).
- **Long reads and epigenetics.** FORMAT keys such as `M5mC` give, for the bases of each allele, the fraction carrying a modification (here 5-methylcytosine), the variant-level counterpart of the `MM`/`ML` tags of alignment files ([[SAM Format#Frontier (M1)]]).
- **Sample-specific reference blocks.** FORMAT `LEN` replaces the shared INFO `END`, which forced all samples of a gVCF record to share one block length.

## Mathematical representation

- **Alleles and genotypes.** A record has alleles $A_0$ (REF) and $A_1, \dots, A_N$ (ALT). An unphased genotype of ploidy $P$ is a multiset $\{k_1 \le \dots \le k_P\}$ with $k_i \in \{0, \dots, N\}$; a phased one is an ordered tuple.
- **Number of genotypes** (stars and bars): $|G| = \binom{N + P}{P}$; for diploids $(N+1)(N+2)/2$.
- **Index in G fields:** $\mathrm{idx}(k_1 \le \dots \le k_P) = \sum_{m=1}^{P} \binom{k_m + m - 1}{m}$; for $P = 2$, $\binom{a}{1} + \binom{b+1}{2} = a + b(b+1)/2$.[^gt]
- **Likelihoods.** With data $D$ at the site, $\mathrm{GL}_g = \log_{10} \Pr(D \mid g)$ and $\mathrm{PL}_g = \mathrm{round}(-10\,\mathrm{GL}_g)$: the probability of the reads under each genotype, from base and mapping qualities, as in probabilistic genotype calling.[^gt][^nielsen]
- **Counts from genotypes.** $\mathrm{AC}_j = \sum_{s} \#\{i : k_{s,i} = j\}$ and $\mathrm{AN} = \sum_s \#\{\text{called alleles of } s\}$; $\mathrm{AC}_j / \mathrm{AN}$ is the allele frequency among called genotypes, which may differ from the AF field (Exercise 4).

## Computational representation

A reader in standard-library Python: header definitions drive the typing of INFO and FORMAT values, so `AF` (Number A) becomes a list and `DB` (a Flag) becomes `True`. The example is the specification's, without the header lines the parser does not need.

```python
import re
from math import comb

STRUCTURED = re.compile(r"^##(\w+)=<(.*)>$")
PAIR = re.compile(r'(\w+)=("(?:[^"\\]|\\.)*"|[^,]*)')        # key=value, value possibly quoted
CAST = {"Integer": int, "Float": float, "String": str, "Character": str}

def parse_header(lines):
    """Return (meta, columns); meta maps INFO, FORMAT, FILTER, contig... to {ID: attributes}."""
    meta, columns = {}, None
    for line in lines:
        if line.startswith("##"):
            m = STRUCTURED.match(line)
            if m:
                attrs = {k: v.strip('"') for k, v in PAIR.findall(m.group(2))}
                meta.setdefault(m.group(1), {})[attrs["ID"]] = attrs
            else:
                key, value = line[2:].split("=", 1)
                meta.setdefault(key, value)
        elif line.startswith("#CHROM"):
            columns = line[1:].split("\t")
    return meta, columns

def typed(value: str, definition: dict):
    """Convert an INFO or FORMAT value with its header definition (Number, Type)."""
    if definition["Type"] == "Flag":
        return True
    items = [None if v == "." else CAST[definition["Type"]](v) for v in value.split(",")]
    return items[0] if definition["Number"] == "1" else items

def parse_gt(gt: str):
    """'1|0' -> ([1, 0], True); './.' -> ([None, None], False); True only if no '/' separator."""
    alleles = re.split(r"[/|]", gt.lstrip("/|"))
    return [None if a == "." else int(a) for a in alleles], "/" not in gt.lstrip("/|")

def parse_record(line: str, meta: dict, samples: list[str]) -> dict:
    f = line.rstrip("\r\n").split("\t")
    info = {}
    for item in ([] if f[7] == "." else f[7].split(";")):
        key, _, value = item.partition("=")
        info[key] = typed(value, meta["INFO"][key]) if key in meta.get("INFO", {}) else value or True
    calls = {}
    if len(f) > 8:
        keys = f[8].split(":")
        for name, block in zip(samples, f[9:]):              # trailing fields may be dropped
            calls[name] = {k: parse_gt(v) if k == "GT" else typed(v, meta["FORMAT"][k])
                           for k, v in zip(keys, block.split(":"))}
    return {"chrom": f[0], "pos": int(f[1]), "id": f[2], "ref": f[3], "alt": f[4].split(","),
            "qual": None if f[5] == "." else float(f[5]), "filter": f[6], "info": info, "calls": calls}

def genotype_index(alleles: list[int]) -> int:
    """Position of a genotype in GL/PL order: sum over m of C(k_m + m - 1, m), k sorted."""
    return sum(comb(k + m - 1, m) for m, k in enumerate(sorted(alleles), start=1))

def genotype_order(ploidy: int, n_alt: int) -> list[str]:
    def rec(p, top, suffix):
        for a in range(top + 1):
            yield from ([str(a) + suffix] if p == 1 else rec(p - 1, a, str(a) + suffix))
    return list(rec(ploidy, n_alt, ""))

EXAMPLE = """##fileformat=VCFv4.5
##contig=<ID=20,length=62435964,assembly=B36,md5=f126cdf8a6e0c7f379d618ff66beb2da,species="Homo sapiens",taxonomy=x>
##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">
##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
#CHROM POS ID REF ALT QUAL FILTER INFO FORMAT NA00001 NA00002 NA00003
20 14370 rs6054257 G A 29 PASS NS=3;DP=14;AF=0.5;DB;H2 GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
20 17330 . T A 3 q10 NS=3;DP=11;AF=0.017 GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3 0/0:41:3
20 1110696 rs6040355 A G,T 67 PASS NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ 1|2:21:6:23,27 2|1:2:0:18,2 2/2:35:4
20 1230237 . T . 47 PASS NS=3;DP=13;AA=T GT:GQ:DP:HQ 0|0:54:7:56,60 0|0:48:4:51,51 0/0:61:2
20 1234567 microsat1 GTC G,GTCT 50 PASS NS=3;DP=9;AA=G GT:GQ:DP 0/1:35:4 0/2:17:2 1/1:40:3"""
lines = [l if l.startswith("##") else "\t".join(l.split()) for l in EXAMPLE.splitlines()]
meta, columns = parse_header(lines)
samples = columns[9:]
print(meta["fileformat"], meta["contig"]["20"]["length"], meta["INFO"]["AF"]["Number"], samples)
records = [parse_record(l, meta, samples) for l in lines if not l.startswith("#")]
for r in records:
    alleles = [r["ref"]] + [a for a in r["alt"] if a != "."]
    shown = [("|" if c["GT"][1] else "/").join(alleles[a] for a in c["GT"][0]) for c in r["calls"].values()]
    print(r["pos"], r["ref"], r["alt"], r["qual"], r["filter"], r["info"], shown)
print(records[2]["calls"]["NA00003"])
```

```text
VCFv4.5 62435964 A ['NA00001', 'NA00002', 'NA00003']
14370 G ['A'] 29.0 PASS {'NS': 3, 'DP': 14, 'AF': [0.5], 'DB': True, 'H2': True} ['G|G', 'A|G', 'A/A']
17330 T ['A'] 3.0 q10 {'NS': 3, 'DP': 11, 'AF': [0.017]} ['T|T', 'T|A', 'T/T']
1110696 A ['G', 'T'] 67.0 PASS {'NS': 2, 'DP': 10, 'AF': [0.333, 0.667], 'AA': 'T', 'DB': True} ['G|T', 'T|G', 'T/T']
1230237 T ['.'] 47.0 PASS {'NS': 3, 'DP': 13, 'AA': 'T'} ['T|T', 'T|T', 'T/T']
1234567 GTC ['G', 'GTCT'] 50.0 PASS {'NS': 3, 'DP': 9, 'AA': 'G'} ['GTC/G', 'GTC/GTCT', 'G/G']
{'GT': ([2, 2], False), 'GQ': 35, 'DP': 4}
```

The third sample of record 3 dropped its trailing `HQ`, which the parser tolerates by zipping keys with the values present. Real pipelines read VCF and BCF through HTSlib-based tools (bcftools) or their bindings, and index them with tabix.[^htslib]

## Worked example

> [!example] Record 3 of the specification's example
> `20 1110696 rs6040355 A G,T 67 PASS NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ 1|2:21:6:23,27 2|1:2:0:18,2 2/2:35:4`
> 1. **Site.** Chromosome 20, position 1,110,696 (1-based), dbSNP identifier rs6040355. Alleles: 0 = `A` (REF), 1 = `G`, 2 = `T`.
> 2. **QUAL 67**: probability of no variant $10^{-6.7} \approx 2 \times 10^{-7}$; **FILTER PASS**: every filter applied was passed.
> 3. **INFO.** `AF=0.333,0.667` has two values because AF is Number=A (one per ALT); `AA=T`: the ancestral allele is T, an ALT allele (the specification notes this may reveal an error in the reference); `DB` is a flag.[^example]
> 4. **Samples.** NA00001 `1|2` = G on the first haplotype, T on the second (phased); NA00002 `2|1` = T then G; NA00003 `2/2` = homozygous T, unphased, its trailing HQ dropped.
> 5. **Quality.** NA00002 has DP 0 and GQ 2: no read supports its genotype, consistent with `NS=2` samples with data.
> 6. **Allele counts from GT.** G: 1 + 1 + 0 = 2; T: 1 + 1 + 2 = 4; AN = 6 called alleles, so $2/6 = 0.333$ and $4/6 = 0.667$, equal to AF here (not in general, Exercise 4).

## Common misconceptions

> [!warning] "QUAL is the quality of each sample's genotype"
> QUAL is a site-level statement about ALT; each sample's confidence is GQ (or its PL values). A site with high QUAL can carry individual genotypes with GQ 2, as NA00002 above.[^fixed][^gt]

> [!warning] "`0|1` and `0/1` are the same genotype"
> Both are heterozygous, but `|` asserts phase: `0|1` and `1|0` are different haplotype assignments within the same phase set, while `0/1` makes no claim about which chromosome carries which allele.[^gt]

> [!warning] "A deletion record removes the base at POS"
> POS points to the padding base, which is kept: `POS=2 REF=TC ALT=T` deletes the C at position 3.[^fixed][^repr] Interval tools converting VCF to BED must start the deleted interval at POS, in 0-based form ([[BED Format]]).

> [!warning] "FILTER `.` means the variant passed"
> `.` means no filter was applied; only `PASS` means filters were applied and passed.[^fixed]

## Exercises

> [!question] Exercise 1 (L2)
> With REF = `A` and ALT = `G,T`, give the alleles and the phasing of `0/1`, `1|0`, `./.`, `1`, `0/0/1` and `1/2`.

> [!success]- Solution
> ```python
> for gt in ("0/1", "1|0", "./.", "1", "0/0/1", "1/2"):
>     print(gt, parse_gt(gt))
> # 0/1 ([0, 1], False)
> # 1|0 ([1, 0], True)
> # ./. ([None, None], False)
> # 1 ([1], True)
> # 0/0/1 ([0, 0, 1], False)
> # 1/2 ([1, 2], False)
> ```
> `0/1` = A/G unphased; `1|0` = G then A, phased; `./.` = diploid no-call; `1` = haploid G (with a single allele, the omitted phasing indicator counts as phased); `0/0/1` = triploid with one G; `1/2` = heterozygous G/T with no reference allele.[^gt]

> [!question] Exercise 2 (L2)
> On the invented reference `GATTACAGA` (positions 1 to 9), write POS, REF and ALT for: (a) C at 6 becomes T; (b) deletion of the C at 6; (c) insertion of `GG` after the A at 7; (d) deletion of the first base.

> [!success]- Solution
> (a) `6 C T`. (b) Padding base A at 5: `5 AC A`. (c) Padding base A at 7: `7 A AGG`. (d) No base precedes position 1, so the padding base is the one after: `1 GA A`.[^fixed]

> [!question] Exercise 3 (L2, Python)
> List the PL order for a diploid site with 2 alternate alleles and for a triploid site with 2, and give the index of the genotypes 0/0, 1/2, 2/1, 2/3 and 0/1/1. How many genotypes has a diploid site with 3 alternate alleles?

> [!success]- Solution
> ```python
> print(genotype_order(2, 2), genotype_order(3, 2))
> print([genotype_index(g) for g in ([0, 0], [1, 2], [2, 1], [2, 3], [0, 1, 1])], comb(3 + 2, 2), comb(2 + 3, 3))
> # ['00', '01', '11', '02', '12', '22'] ['000', '001', '011', '111', '002', '012', '112', '022', '122', '222']
> # [0, 4, 4, 8, 2] 10 10
> ```
> Both orders match the specification's examples. 1/2 and 2/1 share index 4 because likelihoods describe unordered genotypes; 2/3 is at $3 \cdot 4/2 + 2 = 8$. A diploid site with 3 ALT alleles has $\binom{5}{2} = 10$ genotypes, and a triploid site with 2 ALT has $\binom{5}{3} = 10$ too.[^gt]

> [!question] Exercise 4 (L3, Python)
> For each record of the example, compute AC and AN from the GT fields and compare $\mathrm{AC}/\mathrm{AN}$ with AF. Explain record 2.

> [!success]- Solution
> ```python
> for r in records:
>     gts = [a for call in r["calls"].values() for a in call["GT"][0] if a is not None]
>     n_alt = len([a for a in r["alt"] if a != "."])
>     ac = [gts.count(i) for i in range(1, n_alt + 1)]
>     print(r["pos"], "AC", ac, "AN", len(gts), "AC/AN", [round(c / len(gts), 3) for c in ac], "AF", r["info"].get("AF"))
> # 14370 AC [3] AN 6 AC/AN [0.5] AF [0.5]
> # 17330 AC [1] AN 6 AC/AN [0.167] AF [0.017]
> # 1110696 AC [2, 4] AN 6 AC/AN [0.333, 0.667] AF [0.333, 0.667]
> # 1230237 AC [] AN 6 AC/AN [] AF None
> # 1234567 AC [3, 1] AN 6 AC/AN [0.5, 0.167] AF None
> ```
> Record 2 has one alternate allele among 6 called alleles (0.167) but AF = 0.017: AF is *estimated from primary data, not called genotypes*, for instance over many more samples or reads than those listed.[^fixed] Never recompute AF and overwrite it without saying so; store genotype-based counts in AC and AN.

> [!question] Exercise 5 (L3, Python)
> On the invented reference `GGCACACACATT`, records `POS=2 REF=GCA ALT=G` and `POS=8 REF=ACA ALT=A` look different. Show that they describe the same haplotype, and give the normalized form.

> [!success]- Solution
> ```python
> def apply(seq: str, pos: int, ref: str, alt: str) -> str:
>     """ALT haplotype of a VCF record on a 1-based reference string."""
>     assert seq[pos - 1:pos - 1 + len(ref)] == ref, "REF does not match the reference"
>     return seq[:pos - 1] + alt + seq[pos - 1 + len(ref):]
>
> toy = "GGCACACACATT"                      # invented reference with a CA repeat
> a = apply(toy, 2, "GCA", "G")             # delete one CA, anchored on the G before the repeat
> b = apply(toy, 8, "ACA", "A")             # delete one CA, anchored inside the repeat
> print(a, b, a == b)
> # GGCACACATT GGCACACATT True
> ```
> Deleting any one `CA` of the repeat gives the same sequence. The normalized record is left-aligned and parsimonious: `POS=2 REF=GCA ALT=G`, which cannot move further left (deleting `GC` would give another sequence) nor lose bases.[^tan] Comparing call sets without this step reports false discordances ([[Variant Normalization]]).

> [!question] Exercise 6 (M1, Python)
> How many PL values does one diploid sample need at a site with 3, 50 and 200 alternate alleles, and how many with local alleles if the sample's `LAA` lists 2 of them?

> [!success]- Solution
> ```python
> for n_alt in (3, 50, 200):
>     print(n_alt, "ALT:", comb(n_alt + 2, 2), "PL values; with 2 local ALT:", comb(2 + 2, 2))
> # 3 ALT: 10 PL values; with 2 local ALT: 6
> # 50 ALT: 1326 PL values; with 2 local ALT: 6
> # 200 ALT: 20301 PL values; with 2 local ALT: 6
> ```
> PL grows as $\binom{N+2}{2} \approx N^2/2$ per sample while the local form stays at $\binom{4}{2} = 6$ (REF plus 2 local alleles): in a cohort where sites accumulate rare alleles, that is the difference between a usable and an unusable file, the motivation the specification gives for local alleles.[^gt][^changes]

## Mastery checklist

- [ ] 1 Recognized: I can name the 8 fixed VCF fields and read a GT such as `0|1`.
- [ ] 2 Understood: I can explain Number A, R and G, the padding base, QUAL versus GQ, phasing, and why AF may differ from genotype counts.
- [ ] 3 Practiced: I can parse VCF with typed INFO and FORMAT values in Python, index genotypes, and check representations by applying records to a reference.
- [ ] 4 Applied: [[03-genome-diff]] writes valid VCF that a standard tool reads back, and [[09-genome-browser]] displays real compressed, indexed VCF files.
- [ ] 5 Explained: I can teach normalization, gVCF reference blocks, BCF and the local-allele extension, with their reasons.

## References

[^vcf1]: [[GA4GH hts-specs]], `VCFv4.5` (The Variant Call Format Specification, VCFv4.5 and BCFv2.2), §1 "The VCF specification" (overview).
[^example]: [[GA4GH hts-specs]], `VCFv4.5`, §1.1 "An example", with its description of the five records.
[^meta]: [[GA4GH hts-specs]], `VCFv4.5`, §1.4 "Meta-information lines" and §1.4.1 "File format".
[^info]: [[GA4GH hts-specs]], `VCFv4.5`, §1.4.2 "Information field format" and §1.4.4 "Individual format field format" (Number and Type).
[^alt]: [[GA4GH hts-specs]], `VCFv4.5`, §1.4.5 "Alternative allele field format" (symbolic structural variant alleles).
[^contig]: [[GA4GH hts-specs]], `VCFv4.5`, §1.4.7 "Contig field format".
[^headerline]: [[GA4GH hts-specs]], `VCFv4.5`, §1.5 "Header line syntax".
[^fixed]: [[GA4GH hts-specs]], `VCFv4.5`, §1.6.1 "Fixed fields" and the table of reserved INFO keys.
[^gt]: [[GA4GH hts-specs]], `VCFv4.5`, §1.6.2 "Genotype fields": reserved keys, GT, GQ, GL, PL, PS, "Genotype Ordering", local alleles (LAA, LPL) and base modifications.
[^hap]: [[GA4GH hts-specs]], `VCFv4.5`, §2 "Understanding the VCF format and the haplotype representation".
[^repr]: [[GA4GH hts-specs]], `VCFv4.5`, "Representing variation in VCF records": creating and decoding VCF entries for SNPs and small indels.
[^gvcf]: [[GA4GH hts-specs]], `VCFv4.5`, "Representing unspecified alleles and REF-only blocks (gVCF)".
[^bcf]: [[GA4GH hts-specs]], `VCFv4.5`, "BCF specification" (motivation, file organization, BGZF blocks and indexing).
[^changes]: [[GA4GH hts-specs]], `VCFv4.5`, "List of changes", changes between VCFv4.5 and VCFv4.4.
[^tabix]: [[GA4GH hts-specs]], `tabix` (The Tabix index file format): region end of a VCF record.
[^htslib]: [[HTSlib]], `tabix(1)` (position-sorted, bgzip-compressed input; `vcf` preset) and the libraries behind bcftools.
[^tan]: [[Tan 2015 - Unified Representation of Genetic Variants]], *Bioinformatics* 31(13):2202-2204: inconsistent representations, and left-aligned, parsimonious, normalized entries.
[^nielsen]: [[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]], *Nature Reviews Genetics* 12:443-451: genotype likelihoods computed from the reads and their qualities.
[^igv]: [[Integrative Genomics Viewer]], desktop documentation, "File Formats" (VCF).
