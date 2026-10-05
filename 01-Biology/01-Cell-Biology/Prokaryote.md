---
aliases:
  - Prokaryotes
  - Prokaryotic Cell
  - Procaryote
  - Cellule procaryote
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
  - "[[DNA]]"
  - "[[Ribosome]]"
related:
  - "[[Eukaryote]]"
  - "[[Bacteria]]"
  - "[[Archaea]]"
  - "[[Plasmid]]"
  - "[[Horizontal Gene Transfer]]"
  - "[[Operon]]"
  - "[[Chromosome]]"
  - "[[Genome]]"
  - "[[16S Ribosomal RNA]]"
  - "[[Tree of Life]]"
  - "[[Gene Finding]]"
  - "[[GC Skew]]"
  - "[[Sequencing Coverage]]"
  - "[[Pangenome]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Ensembl]]"
---

# Prokaryote

> [!abstract]
> A prokaryote is a single cell without a nucleus: its DNA, usually one circular chromosome plus optional small plasmids, lies in the cytoplasm next to the ribosomes. Bacteria and archaea are the two kinds.

## Definition

A **prokaryote** is a single-celled organism whose cell has no nucleus and no other membrane-bound organelle; its DNA is concentrated in a region of the cytoplasm called the **nucleoid**.[^os42] Prokaryotes make up two of the three domains of life, **Bacteria** and **Archaea**.[^woese][^ospro]

## Why it matters

- **Most sequenced genomes are prokaryotic.** The Ensembl 2025 release served more than 31,300 prokaryotic genomes, against 4,800 eukaryotic ones.[^ensembl]
- **A genome is a set of replicons.** A prokaryotic genome is usually one circular chromosome, often accompanied by plasmids, small circular DNA molecules that replicate on their own and can carry genes such as antibiotic resistance genes.[^os14][^os17] Assemblers must tell these replicons apart, and their read depths reveal copy numbers (Computational representation; [[Plasmid]], [[Antimicrobial Resistance]]).
- **Genes are easy to read off the DNA.** Bacterial genes are densely packed, generally without introns, and often grouped in operons,[^blattner][^alberts][^os16] so open reading frames are good first gene predictions ([[Open Reading Frame]], [[Gene Finding]]).
- **Ribosomal RNA identifies them.** Comparing rRNA sequences is how prokaryotes were classified into two primary lines,[^woese] and the basis of community surveys ([[16S Ribosomal RNA]], [[Metagenomics]]).

## Core (L1)

![[bacterial-cell-plan.svg]]

| Structure | Present in | What it is and does |
|---|---|---|
| Plasma membrane | all | lipid bilayer enclosing the cytoplasm ([[Cell Membrane]]);[^os42] it also holds the respiratory electron transport chain, which eukaryotes keep in mitochondria[^os7] |
| Cytoplasm | all | cytosol with the ribosomes and the nucleoid[^os42] |
| Nucleoid | all | the region that holds the chromosome, with no membrane around it[^os42] |
| Chromosome | all | usually one circular DNA molecule, supercoiled to fit in the cell[^os14] |
| Ribosomes | all | 70S ribosomes, smaller than the 80S ribosomes of the eukaryotic cytosol ([[Ribosome]])[^alberts] |
| Plasmids | many | small circular DNA molecules that replicate independently of the chromosome[^os17] |
| Cell wall | most | rigid layer outside the membrane that protects the cell, keeps its shape and prevents dehydration; made of peptidoglycan in bacteria[^os42] |
| Capsule | many | polysaccharide layer that lets the cell attach to surfaces[^os42] |
| Flagella | some | filaments used to swim[^os42] |
| Pili, fimbriae | some | surface appendages: pili exchange DNA during conjugation, fimbriae attach cells to host cells[^os42] |

**Size.** Prokaryotic cells measure 0.1 to 5.0 µm across, against 10 to 100 µm for eukaryotic cells. Being small gives them a large surface-to-volume ratio, and molecules that enter spread quickly through the cell ([[Cell#Why cells are small]]).[^os42]

**Bacteria and archaea: one plan, two chemistries.** Archaea look like bacteria, but their membrane lipids are built from branched isoprenoid (phytanyl) chains linked to glycerol by ether bonds, instead of fatty acids linked by ester bonds, and their cell walls contain no peptidoglycan.[^ospro] Ribosomal RNA places them on a line of descent of their own.[^woese] The two envelopes are detailed in [[Bacteria]] and [[Archaea]].

**Division by binary fission.** The single chromosome is replicated from one origin, the two copies move apart, and the cell splits in two; there is no mitosis ([[Mitosis]], [[Bacterial Growth]]).[^os10]

## Deeper (L2)

### One compartment, coupled gene expression

With no nuclear envelope, ribosomes bind an mRNA and translate it while RNA polymerase is still making it.[^os15] There is no processing step between transcription and translation, the step that the eukaryotic nucleus imposes ([[Cell Nucleus#Core (L1)]]).

### A compact chromosome

- **Dense genes.** The *E. coli* K-12 chromosome, one circle of 4,639,221 bp, carries 4,288 protein-coding genes:[^blattner] about 0.92 genes per kilobase, or one gene every 1.08 kb on average. Bacterial chromosomes are mostly coding sequence, with little DNA between genes ([[Genome]]).[^alberts]
- **Operons.** Genes for the steps of one pathway are often grouped and transcribed together from a single promoter into one **polycistronic** mRNA ([[Operon]]).[^os16]
- **Uninterrupted genes.** Bacterial protein-coding genes are generally continuous, without introns ([[Gene#Deeper (L2)]]).[^alberts]
- **One origin, two forks.** The *E. coli* chromosome is copied from a single origin by two forks moving in opposite directions around the circle, in about 42 minutes, which means about 1000 nucleotides added per second.[^os14]
- **Small can be very small.** *Mycoplasma genitalium* lives with about 580 kb and 468 genes.[^alberts1]

### Plasmids and gene exchange

Plasmids replicate independently of the chromosome, and natural plasmids carry genes that can benefit the cell, such as antibiotic resistance.[^os17] Genes also move between cells by **transformation** (uptake of free DNA), **transduction** (transfer by a bacteriophage) and **conjugation** (direct transfer, for instance of a plasmid, through a pilus): this **horizontal gene transfer** can cross species boundaries ([[Horizontal Gene Transfer]], [[Plasmid]]).[^micro11]

## Advanced (L3)

- **"Prokaryote" names a cell plan, not a branch of the tree.** Woese and Fox found that the archaebacteria form a primary line of descent, as distinct from typical bacteria as from the lineage of the eukaryotic cytoplasm.[^woese] At the molecular level, archaea resemble eukaryotes in their machinery for replication, transcription and translation, and bacteria in their metabolism and energy conversion.[^alberts1] "Prokaryote" is defined by an absence (no nucleus) and groups two domains that are not each other's closest relatives ([[Tree of Life]], [[Archaea]]).
- **Circular replicons in data.** Positions on a circular chromosome or plasmid wrap around, so a feature can cross position 1 ([[Genomic Coordinate System]]); the origin and terminus of replication can be located from the GC skew ([[GC Skew]]); and each replicon's read depth reflects its copy number ([[Sequencing Coverage]]).
- **A species is more than one genome.** Because genes and plasmids move between cells,[^micro11] two isolates of one species need not carry the same genes, and a single reference genome can miss part of the species' repertoire ([[Pangenome]]).
- **Mixed communities.** Most environments hold many prokaryotic species at once; sequencing them together is [[Metagenomics]], and sorting the reads back into genomes is [[Metagenomic Binning]].

## Mathematical representation

**Replication timing.** A circular chromosome of length $L$ (bp) is copied from an origin at position $o$ by two forks moving at $v$ nucleotides per second in opposite directions. The whole chromosome is copied in

$$T = \frac{L}{2v},$$

and a locus at position $x$ is reached after $t(x) = \delta(x)/v$, where $\delta(x) = \min\big(|x - o| \bmod L,\; L - |x - o| \bmod L\big)$ is its distance from the origin along the circle. The last locus copied, the terminus, lies opposite the origin, at distance $L/2$.

**Copies per chromosome from read depth.** If read depth is proportional to copy number, a replicon with mean depth $\bar d_p$ is present in

$$c_p \approx \frac{\bar d_p}{\bar d_{\mathrm{chr}}}$$

copies per chromosome copy, $\bar d_{\mathrm{chr}}$ being the chromosome's mean depth (the same reasoning as for mtDNA in [[Mitochondrion#Mathematical representation]]).

**Gene density** is $\rho = N_{\mathrm{genes}}/L$; for *E. coli*, $\rho = 4288 / 4639.221\ \mathrm{kb} \approx 0.92$ genes per kb.[^blattner]

## Computational representation

An assembler reports contigs with a length, a mean read depth and, for long-read assemblies, whether the contig closes into a circle. A first sorting of replicons:

```python
# Invented assembly summary: contig -> (length in bp, mean read depth, circular?)
CONTIGS = {
    "contig_1": (4_612_000, 48.0, True),
    "contig_2": (96_400, 45.5, True),
    "contig_3": (5_870, 392.0, True),
    "contig_4": (2_950, 51.0, False),
}


def replicons(contigs: dict) -> dict:
    """Longest circular contig = chromosome; other circular contigs = plasmid candidates.
    Copies per chromosome = depth ratio (depth assumed proportional to copy number)."""
    circular = [name for name, (_, _, is_circ) in contigs.items() if is_circ]
    chrom = max(circular, key=lambda name: contigs[name][0])
    depth_chrom = contigs[chrom][1]
    report = {}
    for name, (length, depth, is_circ) in contigs.items():
        kind = "chromosome" if name == chrom else ("plasmid" if is_circ else "unplaced")
        report[name] = (kind, length, round(depth / depth_chrom, 1))
    return report


for name, row in replicons(CONTIGS).items():
    print(name, *row)
```

```text
contig_1 chromosome 4612000 1.0
contig_2 plasmid 96400 0.9
contig_3 plasmid 5870 8.2
contig_4 unplaced 2950 1.1
```

`contig_2` is a large plasmid at about one copy per chromosome; `contig_3` a small plasmid at about eight copies; `contig_4` is a linear fragment at chromosomal depth, most likely a piece of the chromosome that the assembler could not join. These rules are a teaching heuristic: real plasmid classification also uses gene content and comparison with plasmid databases.

The replication model of the Mathematical representation, applied to *E. coli*:

```python
def replication_minutes(genome_bp: int, nt_per_s: float = 1000, forks: int = 2) -> float:
    """Time to copy a circular chromosome from one origin, two forks moving apart."""
    return genome_bp / (forks * nt_per_s) / 60


def fork_arrival_minutes(pos: int, origin: int, genome_bp: int, nt_per_s: float = 1000) -> float:
    """Minutes until the nearer of the two forks reaches `pos` on the circle."""
    d = abs(pos - origin) % genome_bp
    return min(d, genome_bp - d) / nt_per_s / 60


L = 4_639_221                                   # E. coli K-12 chromosome, bp
print(round(replication_minutes(L), 1), round(L / 4288), round(4288 / (L / 1000), 2))
origin = 0                                      # invented origin position, for illustration
for pos in (500_000, 2_319_610, 4_400_000):
    print(pos, round(fork_arrival_minutes(pos, origin, L), 1))
```

```text
38.7 1082 0.92
500000 8.3
2319610 38.7
4400000 4.0
```

## Worked example

> [!example] *E. coli* K-12 by the numbers
> 1. **Gene density.** 4,288 protein-coding genes on 4,639,221 bp:[^blattner] 0.92 genes per kb, one gene per 1,082 bp, consistent with a chromosome made mostly of coding sequence.[^alberts]
> 2. **Replication time.** Two forks at about 1000 nt/s:[^os14] $T = 4{,}639{,}221 / 2000 \approx 2320$ s $\approx 38.7$ min, within 10% of the observed 42 minutes.
> 3. **Order of copying.** With the origin placed at position 0 for illustration, a locus at 500,000 is copied after 8.3 min; the terminus, $L/2$ = 2,319,610 bp away, after 38.7 min; a locus at 4,400,000, only 239,221 bp from the origin going the other way around the circle, after 4.0 min.
> 4. **Reading.** Distance along the circle, not the coordinate value, decides when a locus is copied: position 4,400,000 is "close" to position 0.

## Common misconceptions

> [!warning] "Prokaryotic DNA floats loose in the cytoplasm"
> It has no membrane around it, but it is concentrated in the nucleoid and supercoiled to fit.[^os42][^os14]

> [!warning] "Archaea are unusual bacteria"
> They form a separate line of descent,[^woese] with different membrane lipids and walls,[^ospro] and resemble eukaryotes in their information machinery.[^alberts1]

> [!warning] "Plasmids are pieces of the chromosome"
> Plasmids are separate DNA molecules that replicate independently of the chromosome,[^os17] each with its own copy number.

## Exercises

> [!question] Exercise 1 (L1)
> From the figure, list the structures found in every prokaryote and those found only in some.

> [!success]- Solution
> Every prokaryote: plasma membrane, cytoplasm, nucleoid with its chromosome, ribosomes. Only some: plasmids, cell wall (most), capsule, flagella, pili and fimbriae.

> [!question] Exercise 2 (L1)
> Give two differences between archaea and bacteria, and two features they share.

> [!success]- Solution
> Differences: archaeal membrane lipids use branched isoprenoid chains with ether bonds, bacterial ones fatty acids with ester bonds; archaeal walls lack peptidoglycan. Shared: no nucleus (DNA in a nucleoid), and the same prokaryotic cell plan with 70S ribosomes in the cytoplasm.

> [!question] Exercise 3 (L2)
> A human gene, copied from genomic DNA with its introns, is put into *E. coli*. Explain why the bacterium will not make the right protein, and what DNA should be inserted instead.

> [!success]- Solution
> The bacterium transcribes and translates in one compartment, and its genes have no introns to remove:[^os15][^alberts] the introns are translated as if they were coding sequence, which typically introduces stop codons or frameshifts ([[Genetic Code]]). The coding sequence must be inserted without introns, for example as DNA copied from the mature mRNA.

> [!question] Exercise 4 (L2)
> With two forks at 1000 nt/s, how long does a 4.6 Mb circular chromosome take to replicate? How long if a second origin, opposite the first, also fired?

> [!success]- Solution
> $T = 4.6 \times 10^6 / 2000 = 2300$ s $\approx 38$ min. Four forks: each covers a quarter of the circle, so $T = 4.6 \times 10^6 / 4000 = 1150$ s $\approx 19$ min. Each extra origin adds two forks and divides the time accordingly.

> [!question] Exercise 5 (L3, Python)
> Using `replicons` from the Computational representation, classify the invented assembly of another isolate below, and interpret each contig.

> [!success]- Solution
> ```python
> OTHER = {  # invented assembly of another isolate
>     "ctg_A": (2_950_000, 30.0, True),
>     "ctg_B": (210_000, 15.2, True),
>     "ctg_C": (4_100, 600.0, True),
>     "ctg_D": (1_200, 31.0, False),
> }
> for name, row in replicons(OTHER).items():
>     print(name, *row)
> ```
> Output:
> ```text
> ctg_A chromosome 2950000 1.0
> ctg_B plasmid 210000 0.5
> ctg_C plasmid 4100 20.0
> ctg_D unplaced 1200 1.0
> ```
> `ctg_B` is at about 0.5 copies per chromosome: it cannot be present in every cell at one copy, so it may be carried by only part of the population, for instance a plasmid being lost from the culture. `ctg_C` is a small high-copy plasmid. `ctg_D` sits at chromosomal depth: probably a chromosomal fragment the assembler failed to place. Depth alone cannot prove these interpretations; gene content and long reads spanning the junctions can.

## Mastery checklist

- [ ] 1 Recognized: I can define a prokaryote and label the parts of a bacterial cell.
- [ ] 2 Understood: I can explain the nucleoid, plasmids, coupled transcription and translation, and why archaea are a separate domain.
- [ ] 3 Practiced: I can compute replication times on a circular chromosome and plasmid copy numbers from read depths.
- [ ] 4 Applied: I classified the replicons of a real bacterial assembly and checked a plasmid against its annotation.
- [ ] 5 Explained: I can teach why "prokaryote" is a cell plan rather than a clade, and how horizontal transfer complicates the notion of one genome per species.

## References

[^os42]: [[Biology 2e (OpenStax)]], section 4.2 "Prokaryotic Cells" (no nucleus or membrane-bound organelles, nucleoid, cell wall, capsule, flagella, pili and fimbriae, cell size and surface-to-volume ratio).
[^os7]: [[Biology 2e (OpenStax)]], chapter "Cellular Respiration" (the electron transport chain in the plasma membrane of prokaryotes).
[^os10]: [[Biology 2e (OpenStax)]], chapter "Cell Reproduction", section on prokaryotic cell division (binary fission).
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (the circular chromosome in the nucleoid and its supercoiling; replication of the *E. coli* chromosome from one origin in about 42 minutes).
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (coupled transcription and translation in prokaryotes).
[^os16]: [[Biology 2e (OpenStax)]], ch. 16 "Gene Expression" (operons and polycistronic transcripts in prokaryotes).
[^os17]: [[Biology 2e (OpenStax)]], ch. 17 "Biotechnology and Genomics" (plasmids, natural antibiotic resistance genes).
[^ospro]: [[Biology 2e (OpenStax)]], chapter "Prokaryotes: Bacteria and Archaea" (structure of prokaryotes: archaeal membrane lipids and cell walls).
[^micro11]: [[Microbiology (OpenStax)]], ch. 11 "Mechanisms of Microbial Genetics" (horizontal gene transfer: transformation, transduction, conjugation).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of ribosomes (70S and 80S), of gene structure and RNA splicing, and of the compactness of bacterial genomes.
[^alberts1]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 1 "Cells and Genomes", section "The Diversity of Genomes and the Tree of Life" (archaea compared with bacteria and eukaryotes; Table 1-1, *Mycoplasma genitalium*).
[^woese]: [[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]], *PNAS* 74:5088-5090.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* 277:1453-1462.
[^ensembl]: [[Ensembl]], Ensembl 2025 (number of eukaryotic and prokaryotic genomes).
