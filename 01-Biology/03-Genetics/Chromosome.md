---
aliases:
  - Chromosomes
  - Chromosome Arm
  - Karyotype
  - Homologous Chromosome
  - Sex Chromosome
  - Autosome
  - Caryotype
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[DNA]]"
  - "[[Gene]]"
  - "[[Mitosis]]"
  - "[[Meiosis]]"
related:
  - "[[Genome]]"
  - "[[Ploidy]]"
  - "[[Allele]]"
  - "[[Chromatin]]"
  - "[[DNA Replication]]"
  - "[[Sex-Linked Inheritance]]"
  - "[[Genetic Linkage]]"
  - "[[Structural Variant]]"
  - "[[Reference Genome]]"
  - "[[Genomic Coordinate System]]"
  - "[[Hi-C]]"
projects:
  - "[[09-genome-browser]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Goffeau 1996 - Life with 6000 Genes]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Ensembl]]"
  - "[[UCSC Genome Browser]]"
  - "[[HTS Format Specifications]]"
  - "[[Mangs 2007 - The Human Pseudoautosomal Region]]"
  - "[[Genome Reference Consortium]]"
---

# Chromosome

> [!abstract]
> A chromosome is one very long DNA molecule packed with proteins; a cell's genome is split among its chromosomes, which are copied and shared out at every cell division.

## Definition

A **chromosome** is a single, very long DNA molecule together with the proteins that fold and pack it. A eukaryotic nuclear chromosome is linear and needs three kinds of DNA sequence to work: **replication origins**, one **centromere** and two **telomeres**.[^alberts-ch4] Bacterial chromosomes are typically single circular molecules.[^alberts] In genetics, the chromosome is the carrier of genes, arranged in a linear order, each at its own locus.[^os-u3]

## Why it matters

- **Every coordinate starts with a chromosome.** A genomic position is a pair (chromosome, position): `chr1:1,000,000` in a browser, the `CHROM` column of a [[VCF Format|VCF]] file, the first column of [[GFF Format|GFF]] and [[BED Format|BED]]. Each record of a reference genome FASTA is usually one chromosome ([[Reference Genome]], [[Genomic Coordinate System]]). Resources name chromosomes differently (`chr1` or `1`), so check naming and assembly before mixing files.[^ensembl][^ucsc]
- **Chromosomes set the expected number of alleles.** Autosomes are present twice in a human cell, but a male carries one X and one Y; the VCF specification writes haploid calls on Y, on the male non-pseudoautosomal X and on the mitochondrion with a single allele ([[Ploidy]], [[Genotype]]).[^hts]
- **Chromosome-scale changes are variants too.** Extra or missing chromosomes and rearrangements of chromosome segments are detected from sequencing data ([[Structural Variant]], [[Copy Number Variation]]).[^os13]
- **Assemblies aim at one sequence per chromosome.** The first gapless human assembly went from telomere to telomere on every chromosome except Y ([[Genome Assembly]], [[Long-Read Assembly]]).[^nurk]

## Core (L1)

![[chromosome-structure.svg]]

**Parts of a chromosome.**

- **Centromere**: the region that controls chromosome segregation at mitosis and meiosis, where the chromosome is attached to the microtubules of the spindle.[^alberts-ch4] It divides the chromosome into two **arms**: the short arm **p** and the long arm **q**.[^os13]
- **Telomeres**: the two ends, made of long tandem arrays of a short repeated sequence bound by proteins; they seal the end of the chromosome.[^alberts-ch4] In humans the repeat is `TTAGGG`, present 100 to 1000 times.[^os14] The enzyme that maintains them, and why linear ends need it, are explained in [[DNA Replication#Deeper (L2)]].
- **Replication origins**: many along each eukaryotic chromosome ([[DNA Replication]]).

**One chromatid or two.** After DNA replication, a chromosome consists of two identical **sister chromatids** joined at the centromere; mitosis separates them into the two daughter cells ([[Cell Cycle]], [[Mitosis]]).[^os-u2] The familiar X shape is this replicated, condensed state; for most of the cell cycle a chromosome is a single, decondensed DNA molecule packed as [[Chromatin]].[^alberts-ch4]

**Karyotype.** The **karyotype** is the number and appearance of an individual's chromosomes: their length, banding pattern and centromere position. Human autosomes are numbered roughly by decreasing size, from chromosome 1 to chromosome 22, and the X and Y chromosomes form the 23rd pair.[^os13] A human body cell therefore holds 22 pairs of autosomes plus XX or XY: 46 chromosomes.

**Homologous chromosomes.** In a diploid cell chromosomes come in pairs, one inherited from each parent ([[Ploidy]]). The two **homologs** have the same size, centromere position and banding pattern,[^os13] and carry the same genes in the same order, which align precisely when homologs pair during meiosis.[^os11] They may carry different [[Allele|alleles]] at a locus. Sister chromatids, by contrast, are copies made by replication and are identical.

**Sex chromosomes.** Chromosomes other than the sex chromosomes are **autosomes**.[^os13] Human females are XX and males XY. X and Y share only two small **pseudoautosomal regions**, PAR1 at the tips of their short arms and PAR2 at the tips of their long arms, which pair and recombine at male meiosis.[^mangs] Genes in the rest of the X, the differential region, are present once in males, who are **hemizygous** for them ([[Sex-Linked Inheritance]]).[^griffiths]

**Chromosome numbers differ between organisms.**

| Organism | Chromosomes | Source |
|---|---|---|
| *Escherichia coli* K-12 | one circular chromosome, 4,639,221 bp | [^blattner] |
| *Saccharomyces cerevisiae* | 16 nuclear chromosomes | [^goffeau] |
| *Homo sapiens* | 24 different nuclear chromosomes (22 autosomes, X, Y), about 3.2 × 10⁹ nucleotides per haploid set | [^alberts-ch4] |

## Deeper (L2)

### Changes in chromosome number and structure

- **Aneuploidy**: gain or loss of individual chromosomes, usually from **nondisjunction** (chromosomes failing to separate at meiosis). Aneuploidies are typically lethal to the embryo; a few trisomies are viable, such as trisomy 21 (Down syndrome).[^os13]
- **Polyploidy**: whole extra chromosome sets ([[Ploidy]]).[^os13]
- **Structural rearrangements**: deletions, duplications, inversions and translocations of chromosome segments ([[Structural Variant]]).[^os13][^griffiths]

### Chromosomes and inheritance

Genes on different chromosomes are inherited independently of each other, because homolog pairs are distributed independently at meiosis; genes on the same chromosome tend to travel together unless crossing over separates them ([[Mendelian Inheritance]], [[Genetic Recombination]], [[Genetic Linkage]]).[^os-u3] The chromosome is the physical unit behind both rules.

### Centromere position

The position of the centromere is one of the features used to identify chromosomes.[^os13] It can be summarized by the **centromeric index**, the fraction of the chromosome length in the p arm (see Mathematical representation). In **acrocentric** chromosomes the centromere lies close to one end and the p arm is very short: humans have five, and their short arms were among the last regions of the genome to be sequenced.[^nurk]

### Chromosomes in genomic files

- A reference FASTA stores one record per sequence; the header name (such as `chr1` or `1`) is what every other file must match ([[FASTA Format]]).
- Ensembl and UCSC files can differ in chromosome naming for the same assembly; mixing them without converting names mismatches records.[^ensembl][^ucsc]
- Positions are only comparable within one chromosome. Files are sorted by chromosome, then position, and the order of chromosomes must be the same in every file of an analysis (Exercise 4).
- Per-chromosome ploidy appears in genotype calls: `0/1` on an autosome, `1` on the male non-pseudoautosomal X.[^hts]

## Advanced (L3)

- **Telomere to telomere.** Two decades after the draft human genome, about 8% of it was still missing, mostly repeat-rich regions. The T2T-CHM13 assembly (2022) filled all centromeric satellite arrays, recent segmental duplications and the short arms of the five acrocentric chromosomes, corrected errors in earlier references, and added nearly 200 million base pairs; the Y chromosome was completed later.[^nurk] Reads from sequence missing from a reference cannot be placed correctly, so the choice of assembly changes which chromosome regions an analysis can see ([[Reference Genome]], [[Read Mapping]]).
- **Centromeres are repeats.** Human centromeres are built on long satellite arrays, the hardest sequences to assemble and to map reads to ([[Genome Assembly]], [[Repeat Masking]]). GRCh38 was the first human reference with sequence-based representations of the centromeres,[^grc] and T2T-CHM13 the first to assemble all centromeric satellite arrays.[^nurk]
- **Chromosomes in three dimensions.** In the nucleus, chromosomes are folded [[Chromatin]];[^alberts-ch4] their 3D organization is the subject of [[Hi-C]] (M1).
- **DNA outside the nuclear chromosomes.** Mitochondria carry their own small genome ([[Mitochondrial DNA]]),[^alberts] and an assembly FASTA can include it as an extra record next to the chromosomes ([[Genome]]); see [[Plasmid]] for bacterial DNA outside the chromosome.

## Mathematical representation

- A haploid genome with $m$ chromosomes is a list of words $C_1, \dots, C_m$, with $C_i \in \{A, C, G, T, N\}^{L_i}$ and length $L_i$. Its size is $\sum_{i=1}^{m} L_i$ ([[Genome]]).
- A **locus** is a pair $(i, x)$ with $1 \le x \le L_i$. Loci on different chromosomes have no distance; a sort order on all loci is the lexicographic order on (rank of chromosome, position), where the rank comes from a fixed list of chromosome names.
- The **centromere** is an interval $[a, b]$ of $C_i$. The arms are $p = [1, a-1]$ and $q = [b+1, L_i]$, with lengths $\ell_p = a - 1$ and $\ell_q = L_i - b$. By convention $\ell_p \le \ell_q$. The **centromeric index** is
$$\mathrm{CI} = \frac{\ell_p}{\ell_p + \ell_q} \in \left[0, \tfrac{1}{2}\right],$$
close to $\tfrac12$ when the centromere is central and close to 0 for an acrocentric chromosome.
- A **circular** chromosome of length $L$ has positions in $\mathbb{Z}/L\mathbb{Z}$: an interval may wrap around the origin, e.g. $[L - 99, L] \cup [1, 100]$ for a 200 bp feature crossing position 1.
- A diploid human cell contains the multiset $\{1, 1, 2, 2, \dots, 22, 22\} \cup \{X, X\}$ or $\{X, Y\}$: $2 \times 22 + 2 = 46$ chromosomes.

## Computational representation

A chromosome is a named sequence plus metadata (length, topology, ploidy, centromere interval). The code parses a multi-record FASTA, sorts chromosome names in karyotype order and locates positions on arms.

```python
import re

# Invented toy genome (not real sequence): a multi-record FASTA, one record per chromosome.
TOY_FASTA = """>chr2
ACGTTGCAAGGCTTACGATCNNNNNNNNNNGGATCCATTAGCATGCAATCCG
>chr10
TTGACCATGCAGTACGTACCTAG
>chr1
GATTACAGCTTACAGGGCCCTTTAAACCCGGGTTTAAACGTACGTATGCATTAGCAGTTC
>chrX
ACGTACGTTTGACCAGTCCATG
"""
# Invented centromere intervals, 1-based inclusive (chr2 uses its run of N).
CENTROMERES = {"chr1": (24, 29), "chr2": (21, 30), "chr10": (3, 5), "chrX": (8, 10)}


def parse_fasta(text: str) -> dict[str, str]:
    """Map each record name (first word of the header) to its sequence."""
    records, name = {}, None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            records[name] = ""
        elif name is not None:
            records[name] += line.strip()
    return records


def natural_key(name: str) -> tuple[int, str]:
    """Sort chr1, chr2, ..., chr10, then X, Y, M (string order would put chr10 before chr2)."""
    core = re.sub(r"^chr", "", name)
    if core.isdigit():
        return (int(core), "")
    return ({"X": 1000, "Y": 1001, "M": 1002, "MT": 1002}.get(core, 2000), core)


def arm(chrom: str, pos: int, length: int) -> str:
    """Arm of a 1-based position: 'p' before the centromere, 'q' after it."""
    if not 1 <= pos <= length:
        raise ValueError(f"{chrom}:{pos} is outside 1..{length}")
    start, end = CENTROMERES[chrom]
    return "p" if pos < start else "q" if pos > end else "centromere"


def centromeric_index(chrom: str, length: int) -> float:
    """Length of the p arm over the total length of both arms."""
    start, end = CENTROMERES[chrom]
    p, q = start - 1, length - end
    return p / (p + q)


genome = parse_fasta(TOY_FASTA)
print(sorted(genome))                      # string order
print(sorted(genome, key=natural_key))     # karyotype order
for name in sorted(genome, key=natural_key):
    seq = genome[name]
    print(f"{name:6} length={len(seq):3} N={seq.count('N'):2} CI={centromeric_index(name, len(seq)):.2f}")
print(arm("chr1", 5, len(genome["chr1"])), arm("chr1", 26, len(genome["chr1"])), arm("chr1", 40, len(genome["chr1"])))
```

```text
['chr1', 'chr10', 'chr2', 'chrX']
['chr1', 'chr2', 'chr10', 'chrX']
chr1   length= 60 N= 0 CI=0.43
chr2   length= 52 N=10 CI=0.48
chr10  length= 23 N= 0 CI=0.10
chrX   length= 22 N= 0 CI=0.37
p centromere q
```

The toy `chr10` has the lowest centromeric index: it is the "acrocentric" chromosome of this invented genome.

## Worked example

> [!example] Counting chromosomes, chromatids and DNA molecules in human cells
> 1. **Body cell in G1.** 46 chromosomes (22 autosome pairs + XX or XY), each a single chromatid: 46 DNA molecules.
> 2. **Same cell after S phase (G2).** Still 46 chromosomes, because sister chromatids stay joined at the centromere, but 92 chromatids, i.e. 92 DNA molecules. Chromosomes are counted by centromeres, not by chromatids.
> 3. **Mitosis.** Sisters separate: each daughter cell again has 46 single-chromatid chromosomes, identical to the mother cell.
> 4. **Gamete after meiosis.** One chromosome of each pair: 23 chromosomes, 22 autosomes plus one X (egg), or plus X or Y (sperm).
> 5. **A heterozygous locus (alleles A and a).** In G2 the cell carries four copies of the locus: A on both sister chromatids of one homolog, a on both sisters of the other.

## Common misconceptions

> [!warning] "A chromosome is X-shaped"
> The X shape is a replicated chromosome (two sister chromatids) condensed for division. For most of the cell cycle each chromosome is a single, decondensed DNA molecule packed as chromatin.[^alberts-ch4]

> [!warning] "Sister chromatids and homologous chromosomes are the same thing"
> Sister chromatids are identical copies made by replication. Homologs come from the two parents: same genes in the same order, but possibly different alleles at many loci.[^os11]

> [!warning] "A male has no second copy of any X-linked gene"
> The pseudoautosomal regions are shared by X and Y and pair at meiosis;[^mangs] only genes in the differential region of the X are hemizygous in males.[^griffiths] A heterozygous call in a male's pseudoautosomal region is therefore expected.

> [!warning] "Sort chromosomes as strings"
> String order puts `chr10` before `chr2`. Sort by a fixed list of chromosome names, the order of the reference sequences, and use that same order in every file of an analysis.

## Exercises

> [!question] Exercise 1 (L1)
> A human cell has 46 chromosomes in G1. Give the number of chromosomes, chromatids and DNA molecules (a) in G1, (b) in G2, (c) in a sperm cell. How many autosomes does a sperm cell carry?

> [!success]- Solution
> (a) 46, 46, 46. (b) 46, 92, 92: chromosomes are counted by centromeres, and each now has two sister chromatids. (c) 23, 23, 23. A sperm cell carries 22 autosomes plus either an X or a Y.

> [!question] Exercise 2 (L1)
> A person is heterozygous Bb at a locus on chromosome 7. After S phase, where are the copies of B and b? Which pairs of structures carry identical sequences?

> [!success]- Solution
> One homolog of chromosome 7 carries B, the other b. After replication each homolog has two sister chromatids: B on both sisters of one homolog, b on both sisters of the other. Sister chromatids are identical; homologs differ at this locus.

> [!question] Exercise 3 (L2)
> A chromosome is 1,000 kb long, with its centromere at 480-520 kb (1-based, inclusive). (a) On which arm is a variant at 250 kb? (b) Compute its centromeric index. (c) Another chromosome of 1,000 kb has its centromere at 20-30 kb: compute its index and name its type. Why were such short arms hard to sequence in humans?

> [!success]- Solution
> (a) 250 kb is before the centromere: p arm. (b) $\ell_p = 479$ kb, $\ell_q = 480$ kb, CI $= 479/959 \approx 0.50$: a central centromere. (c) $\ell_p = 19$ kb, $\ell_q = 970$ kb, CI $\approx 0.019$: acrocentric. In humans, the short arms of the five acrocentric chromosomes are repeat-rich and were completed only by the telomere-to-telomere assembly.[^nurk]

> [!question] Exercise 4 (L2, Python)
> Using `natural_key` from the code above, sort the invented records `("chrX", 150), ("chr10", 7), ("chr2", 40), ("chr1", 900), ("chr2", 3), ("chr1", 12)` by chromosome then position, and compare with plain `sorted`.

> [!success]- Solution
> ```python
> records = [("chrX", 150), ("chr10", 7), ("chr2", 40), ("chr1", 900), ("chr2", 3), ("chr1", 12)]
> print(sorted(records))
> print(sorted(records, key=lambda r: (natural_key(r[0]), r[1])))
> ```
> Output:
> ```text
> [('chr1', 12), ('chr1', 900), ('chr10', 7), ('chr2', 3), ('chr2', 40), ('chrX', 150)]
> [('chr1', 12), ('chr1', 900), ('chr2', 3), ('chr2', 40), ('chr10', 7), ('chrX', 150)]
> ```
> Plain sorting places `chr10` between `chr1` and `chr2`. Within a chromosome, positions must be compared as integers, never as strings.

> [!question] Exercise 5 (L3)
> In a VCF from a male sample, you find heterozygous genotypes `0/1` at some chrX positions and `1` at others. Which is expected where? Give two explanations for a `0/1` call in the non-pseudoautosomal part of chrX.

> [!success]- Solution
> In the pseudoautosomal regions a male has two copies (X and Y), so diploid calls such as `0/1` are expected. In the rest of the X he is hemizygous, and the VCF specification writes a haploid call with a single allele, `0` or `1`.[^hts][^griffiths] A `0/1` there suggests (1) a caller run with a diploid model everywhere, or (2) reads from a similar sequence elsewhere (for example on the Y or an autosome) mapped to the X, or a sequencing artefact. Such calls are usually flagged for review.

> [!question] Exercise 6 (L3, Python)
> An invented XY species has haploid chromosome lengths `chr1` 60, `chr2` 52, `chr10` 23, `chrX` 22, `chrY` 9 bp. Compute the DNA content of a diploid female cell and of a diploid male cell, and the size of a haploid reference that contains every chromosome once.

> [!success]- Solution
> ```python
> lengths = {"chr1": 60, "chr2": 52, "chr10": 23, "chrX": 22, "chrY": 9}
> autosomes = sum(v for k, v in lengths.items() if k not in ("chrX", "chrY"))
> female = 2 * autosomes + 2 * lengths["chrX"]
> male = 2 * autosomes + lengths["chrX"] + lengths["chrY"]
> haploid_reference = autosomes + lengths["chrX"] + lengths["chrY"]
> print(autosomes, female, male, haploid_reference)
> print(f"male/female DNA content: {male / female:.3f}")
> ```
> Output: `135 314 301 166`, then `male/female DNA content: 0.959`. The male cell has less DNA because the Y is smaller than the X. A reference that contains X and Y once each (166 bp here) describes no real cell: it is a coordinate system, not a karyotype.

## Mastery checklist

- [ ] 1 Recognized: I can name the centromere, telomeres, p and q arms, and define homologs, autosomes and sex chromosomes.
- [ ] 2 Understood: I can explain sister chromatids versus homologs, the human karyotype, hemizygosity and aneuploidy.
- [ ] 3 Practiced: I can parse a multi-record FASTA, sort chromosomes in karyotype order and locate positions on arms.
- [ ] 4 Applied: in [[09-genome-browser]], I display the chromosomes of a real assembly with their lengths, and I reconcile chromosome names between two resources.
- [ ] 5 Explained: I can explain per-chromosome ploidy in variant calls, why centromeres and acrocentric arms were missing from references, and what telomere-to-telomere assemblies changed.

## References

[^alberts-ch4]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 4 "DNA and Chromosomes", section "Chromosomal DNA and Its Packaging in the Chromatin Fiber" (one DNA molecule per chromosome, the 24 human chromosomes, centromeres, telomeres and replication origins).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002).
[^os-u2]: [[Biology 2e (OpenStax)]], Unit 2 "The Cell" (cell division: chromosomes, sister chromatids, mitosis).
[^os-u3]: [[Biology 2e (OpenStax)]], Unit 3 "Genetics" (chromosomal theory of inheritance).
[^os11]: [[Biology 2e (OpenStax)]], section 11.1 "The Process of Meiosis" (haploid and diploid cells, homolog pairing).
[^os13]: [[Biology 2e (OpenStax)]], section 13.2 "Chromosomal Basis of Inherited Disorders" (karyotype, p and q arms, autosomes and sex chromosomes, aneuploidy, polyploidy, rearrangements).
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (telomere replication).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of sex chromosomes (pairing and differential regions, hemizygosity) and of chromosome rearrangements.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science*.
[^goffeau]: [[Goffeau 1996 - Life with 6000 Genes]], *Science*.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*.
[^ensembl]: [[Ensembl]], assembly and chromosome naming conventions.
[^ucsc]: [[UCSC Genome Browser]], assembly and chromosome naming conventions.
[^hts]: [[HTS Format Specifications]], VCF specification, genotype field `GT`.
[^mangs]: [[Mangs 2007 - The Human Pseudoautosomal Region]], *Current Genomics* 8(2):129-136.
[^grc]: [[Genome Reference Consortium]], GRCh38 paper (Schneider et al. 2017, *Genome Research*).
