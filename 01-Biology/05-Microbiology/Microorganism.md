---
aliases:
  - Microorganisms
  - Microbe
  - Microbial World
  - Micro-organisme
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Cell]]"
  - "[[Prokaryote]]"
  - "[[Eukaryote]]"
  - "[[Microscopy]]"
related:
  - "[[Bacteria]]"
  - "[[Archaea]]"
  - "[[Virus]]"
  - "[[Tree of Life]]"
  - "[[Metagenomics]]"
projects: []
sources:
  - "[[Microbiology (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]]"
  - "[[Lloyd 2018 - Phylogenetically Novel Uncultured Microbial Cells Dominate Earth Microbiomes]]"
  - "[[Spang 2015 - Complex Archaea That Bridge the Gap Between Prokaryotes and Eukaryotes]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Goffeau 1996 - Life with 6000 Genes]]"
---

# Microorganism

> [!abstract]
> A microorganism (microbe) is a living thing too small to see without a microscope: bacteria, archaea, microscopic eukaryotes such as yeasts and protists, and, by convention, the acellular viruses. It is a category of size, not a branch of the tree of life.

## Definition

**Microorganisms**, or **microbes**, are organisms that, with a few exceptions, are too small to be seen without magnification; most are single cells. They are **prokaryotic** (bacteria and archaea), **eukaryotic** (protists such as algae and protozoa, fungi such as yeasts and molds, and, by the conventions of the field, parasitic worms whose eggs and larvae are microscopic), or **acellular** (viruses).[^m13]

## Why it matters

- **Most microbes are known from DNA, not from culture.** An estimated 81% of microbial cells on Earth belong to genera with no cultured representative, and about 25% to phyla with none.[^lloyd] Their biology is read from sequences ([[Metagenomics]], [[Microbial Ecology]]).
- **Whole lineages are discovered as genomes.** The Lokiarchaeota were described from a genome reconstructed from environmental metagenomic data, with no cell in culture.[^spang]
- **The kind of microbe decides the method.** Viruses have no ribosomes of their own and multiply with the host cell's machinery,[^osvir] so surveys built on ribosomal RNA genes ([[16S Ribosomal RNA]]) cannot see them. Genome sizes differ many-fold between groups (L3), which biases read counts.
- **Size decides the instrument.** A typical virus (about 100 nm) is below the 0.2 µm resolution limit of light microscopes, a bacterium (about 1 µm) is above it ([[Microscopy]]).[^m13][^alberts]

## Core (L1)

### Four kinds of microbe

| Group | Cell type | Typical size[^m13][^os42] | Note |
|---|---|---|---|
| [[Bacteria]] | prokaryotic cell | about 1 µm (0.1 to 5 µm) | one of the two prokaryotic domains |
| [[Archaea]] | prokaryotic cell | same range as bacteria | the other prokaryotic domain |
| Microbial eukaryotes | eukaryotic cell ([[Eukaryote]]) | 10 to 100 µm for typical eukaryotic cells | fungi, protists |
| [[Virus\|Viruses]] | not a cell | about 100 nm | multiply only inside host cells |

### The size ladder

Each rung is about ten times the previous one: a typical virus (about 100 nm) is ten times smaller than a typical bacterium (about 1 µm), which is at least ten times smaller than a plant or animal cell (10 to 100 µm). An object must measure about 100 µm to be visible without a microscope.[^m13]

![[cell-size-scale.svg]]

"Microbe" is not a taxon. Comparing ribosomal RNA, Woese and Fox found three primary lines of descent, today's three domains;[^woese] microbes occur in all three, and viruses belong to none ([[Tree of Life]], [[Cell]]).

## Deeper (L2)

- **Why viruses are included.** They are counted among microbes although they are not cells:[^m13] no plasma membrane, no metabolism of their own, no division ([[Virus]]).[^osvir]
- **Volume grows as the cube.** A tenfold difference in length is a thousandfold difference in volume (Mathematical representation), so roughly a thousand virus-sized particles fit in a bacterium, and a thousand bacteria in a 10 µm eukaryotic cell. Small size also means a large surface-to-volume ratio ([[Cell#Why cells are small]]).
- **Not all microbes are pathogens.** No archaeon is currently known to cause an infectious disease,[^micro46] although archaea live in almost every habitat ([[Archaea]], [[Pathogen]]).

## Advanced (L3)

**Sequence space has its own scale.** Physical size and genome size are different ladders. From the reduced bacterium *Mycoplasma genitalium* (about 580 kb)[^alberts] to *Escherichia coli* K-12 (4,639,221 bp)[^blattner] and the yeast *Saccharomyces cerevisiae* (12,068 kb),[^goffeau] genome sizes differ twentyfold across these three cellular microbes ([[Genome]]). In a metagenome, the number of reads from an organism is roughly proportional to its abundance **times** its genome length, so read fractions overweight large genomes. Estimating how many cells or genomes are present requires dividing by genome length (Exercise 4; [[Taxonomic Classification]]).

**Culture-independent biology.** Because most lineages lack cultured members,[^lloyd] much of microbial diversity is accessible only through genomes assembled from mixed samples ([[Metagenomic Binning]]), and such genomes have changed the tree of life itself ([[Archaea#Advanced (L3)]]).[^spang]

## Mathematical representation

- **Order of magnitude.** For a length $L$ in metres, its order of magnitude is $\lfloor \log_{10} L \rfloor$; two objects of lengths $L_1 > L_2$ differ by $\log_{10}(L_1/L_2)$ orders of magnitude ([[Logarithm]]).
- **Volume ratio.** Two objects of the same shape scale as $V \propto L^3$, so
$$\frac{V_1}{V_2} = \left(\frac{L_1}{L_2}\right)^3 .$$
A factor 10 in length gives $10^3$ in volume.
- **Reads and genome copies.** If organism $i$ contributes $c_i$ genome copies of length $G_i$, its expected share of reads is $r_i = \dfrac{c_i G_i}{\sum_j c_j G_j}$; inverting, the share of genome copies is
$$\frac{c_i}{\sum_j c_j} = \frac{r_i / G_i}{\sum_j r_j / G_j}.$$

## Computational representation

```python
import math

# Typical linear sizes in metres (values sourced in the note)
TYPICAL_SIZE_M = {
    "virus": 100e-9,
    "bacterium or archaeon": 1e-6,
    "eukaryotic cell, small": 10e-6,
    "eukaryotic cell, large": 100e-6,
}
NAKED_EYE_M = 100e-6          # smallest object visible without a microscope
LIGHT_LIMIT_M = 0.2e-6        # resolution limit of the light microscope

def instrument(size_m: float) -> str:
    """Least powerful instrument that shows an object of this size."""
    if size_m >= NAKED_EYE_M:
        return "naked eye"
    if size_m >= LIGHT_LIMIT_M:
        return "light microscope"
    return "electron microscope"

def volume_ratio(big_m: float, small_m: float) -> float:
    """Volume ratio of two objects of the same shape: cube of the length ratio."""
    return (big_m / small_m) ** 3

for name, size in TYPICAL_SIZE_M.items():
    print(f"{name:24s} log10(m) = {math.log10(size):5.1f}  {instrument(size)}")
print(round(volume_ratio(1e-6, 100e-9)), round(volume_ratio(10e-6, 1e-6)))
```

```text
virus                    log10(m) =  -7.0  electron microscope
bacterium or archaeon    log10(m) =  -6.0  light microscope
eukaryotic cell, small   log10(m) =  -5.0  light microscope
eukaryotic cell, large   log10(m) =  -4.0  naked eye
1000 1000
```

## Worked example

> [!example] How many viruses would fill a bacterium?
> 1. **Lengths**: typical virus 100 nm, typical bacterium 1 µm = 1000 nm.[^m13]
> 2. **Length ratio**: $1000 / 100 = 10$, one order of magnitude.
> 3. **Volume ratio**: $10^3 = 1000$, treating both as spheres: about a thousand virus-sized particles fit in the volume of one bacterium; packing and shape make the real number smaller, but not by an order of magnitude.

## Common misconceptions

> [!warning] "Microbes are a group of related organisms"
> Microbes are defined by size. They include members of all three domains and the viruses, which belong to no domain.[^m13][^woese]

> [!warning] "Microbes are germs"
> Pathogens are a minority of microbes; no archaeon is known to cause an infectious disease.[^micro46]

> [!warning] "A microbe is always invisible and always unicellular"
> Some unicellular microbes are visible to the naked eye, and some multicellular organisms are microscopic.[^m13]

## Exercises

> [!question] Exercise 1 (L1)
> Classify as prokaryotic, eukaryotic or acellular: *E. coli*, baker's yeast, a methanogen, influenza virus, an amoeba.

> [!success]- Solution
> Prokaryotic: *E. coli* (a bacterium), the methanogen (an archaeon). Eukaryotic: yeast (a fungus), the amoeba (a protist). Acellular: influenza virus.

> [!question] Exercise 2 (L1)
> Using the size ladder, which of a virus, a bacterium and a 50 µm protist can you see with a light microscope, and which with the naked eye?

> [!success]- Solution
> Light microscope: the bacterium (1 µm) and the protist (50 µm), both above 0.2 µm. Naked eye: none of them clearly, since 50 µm is below about 100 µm. The virus (100 nm) needs an electron microscope.

> [!question] Exercise 3 (L2)
> A 16S rRNA gene survey of seawater reports bacteria and archaea only. Give two reasons why viruses and microbial eukaryotes are missing.

> [!success]- Solution
> Viruses have no ribosomes of their own, hence no rRNA genes to amplify.[^osvir] Microbial eukaryotes have ribosomes, but their cytosolic ribosomes are the larger 80S type, built on a different small-subunit rRNA (18S) than the 70S ribosomes of prokaryotes (16S),[^alberts] so primers designed for the prokaryotic gene are not meant to capture them ([[16S Ribosomal RNA]]). Absence from the survey is not absence from the sample.

> [!question] Exercise 4 (L3, Python)
> Invented read counts from a metagenome are assigned to an *E. coli*-like bacterium (460,000 reads), a *Mycoplasma*-like bacterium (58,000) and a yeast-like fungus (120,000), using the genome sizes of the L3 section. Compute the read fractions and the genome-copy fractions. Which organism is most misjudged by read counts?

> [!success]- Solution
> ```python
> SAMPLE = {  # taxon: (reads assigned, genome size in bp)
>     "E. coli-like bacterium": (460_000, 4_639_221),
>     "Mycoplasma-like bacterium": (58_000, 580_000),
>     "yeast-like fungus": (120_000, 12_068_000),
> }
>
> def fractions(sample: dict) -> dict:
>     """Read fraction and genome-copy fraction (reads / genome length, renormalized)."""
>     total_reads = sum(reads for reads, _ in sample.values())
>     copies = {t: reads / size for t, (reads, size) in sample.items()}
>     total_copies = sum(copies.values())
>     return {t: (round(sample[t][0] / total_reads, 3), round(copies[t] / total_copies, 3))
>             for t in sample}
>
> for taxon, (read_frac, copy_frac) in fractions(SAMPLE).items():
>     print(f"{taxon:26s} reads {read_frac:.3f}  genomes {copy_frac:.3f}")
> ```
> ```text
> E. coli-like bacterium     reads 0.721  genomes 0.474
> Mycoplasma-like bacterium  reads 0.091  genomes 0.478
> yeast-like fungus          reads 0.188  genomes 0.048
> ```
> The small-genome *Mycoplasma*-like organism has 9% of the reads but about 48% of the genomes; the yeast-like fungus is overestimated fourfold. This assumes one genome copy per cell and equal sequencing efficiency, both false in general (yeast can be diploid; [[Ploidy]]).

## Mastery checklist

- [ ] 1 Recognized: I can name the four kinds of microbe and give the typical size of each.
- [ ] 2 Understood: I can explain why "microbe" is a size category spread over three domains plus viruses.
- [ ] 3 Practiced: I can compute order-of-magnitude and volume ratios and pick the instrument for an object.
- [ ] 4 Applied: I converted read counts of a real metagenomic profile into genome-copy fractions.
- [ ] 5 Explained: I can explain why culture-independent sequencing dominates microbiology and what each survey method cannot see.

## References

[^m13]: [[Microbiology (OpenStax)]], section 1.3 "Types of Microorganisms" (prokaryotic, eukaryotic and acellular microorganisms; most microbes unicellular and too small to see without magnification, with exceptions; typical virus about 100 nm, bacterium about 1 µm, plant or animal cell 10 to 100 µm; about 100 µm needed to be seen without a microscope).
[^os42]: [[Biology 2e (OpenStax)]], section 4.2 "Prokaryotic Cells" (prokaryotic cells 0.1 to 5.0 µm, eukaryotic cells 10 to 100 µm).
[^osvir]: [[Biology 2e (OpenStax)]], chapter "Viruses" (viruses as acellular entities that replicate only inside host cells, using the host's machinery).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002): ch. 1 "Cells and Genomes" (*Mycoplasma genitalium*, about 580 kb); treatment of microscopy (the 0.2 µm resolution limit of light microscopes); treatment of ribosomes (70S prokaryotic and 80S eukaryotic ribosomes and their rRNAs).
[^woese]: [[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]], *PNAS* 74:5088-5090.
[^lloyd]: [[Lloyd 2018 - Phylogenetically Novel Uncultured Microbial Cells Dominate Earth Microbiomes]], *mSystems* 3(5):e00055-18.
[^spang]: [[Spang 2015 - Complex Archaea That Bridge the Gap Between Prokaryotes and Eukaryotes]], *Nature* 521:173-179.
[^micro46]: [[Microbiology (OpenStax)]], section 4.6 "Archaea" (no archaea currently known to be associated with infectious diseases).
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* 277:1453-1462.
[^goffeau]: [[Goffeau 1996 - Life with 6000 Genes]], *Science* (12,068 kb genome of *Saccharomyces cerevisiae*).
