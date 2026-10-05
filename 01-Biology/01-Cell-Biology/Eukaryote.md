---
aliases:
  - Eukaryotes
  - Eukaryotic Cell
  - Eukarya
  - Eucaryote
  - Cellule eucaryote
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
  - "[[DNA]]"
related:
  - "[[Organelle]]"
  - "[[Cell Nucleus]]"
  - "[[Mitochondrion]]"
  - "[[Endomembrane System]]"
  - "[[Cytoskeleton]]"
  - "[[Chromosome]]"
  - "[[Chromatin]]"
  - "[[Gene]]"
  - "[[Genome]]"
  - "[[RNA Processing]]"
  - "[[Mitosis]]"
  - "[[Meiosis]]"
  - "[[Archaea]]"
  - "[[Spliced Read Alignment]]"
  - "[[Gene Finding]]"
  - "[[GFF Format]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Goffeau 1996 - Life with 6000 Genes]]"
  - "[[IHGSC 2004 - Finishing the Euchromatic Sequence of the Human Genome]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Elliott 2015 - The C-Value Enigma and the Evolution of Eukaryotic Genome Content]]"
  - "[[Anderson 1981 - Sequence and Organization of the Human Mitochondrial Genome]]"
  - "[[Sequence Ontology GFF3 Specification]]"
---

# Eukaryote

> [!abstract]
> A eukaryote is an organism whose cells have a nucleus: the DNA, split into several linear chromosomes wound on histones, sits behind a double membrane, and the cytoplasm is divided into membrane-bound compartments, each with its own job. Animals, plants, fungi and many single-celled organisms are eukaryotes.

## Definition

A **eukaryote** is an organism made of one or more eukaryotic cells: cells with a membrane-bound nucleus, numerous membrane-bound organelles and several rod-shaped chromosomes.[^os43] Eukaryotes form the third primary line of descent of life, next to the two prokaryotic ones,[^woese] and range from single cells such as yeasts and protozoa to plants, animals and fungi.[^alberts1]

## Why it matters

- **Genes come in pieces.** Eukaryotic genes are interrupted by introns that are spliced out of the RNA in the nucleus, and one gene can give several mRNAs by alternative splicing.[^os15][^os16] RNA-seq reads must therefore be aligned across splice junctions, and gene finders must model exons and introns ([[Spliced Read Alignment]], [[Gene Finding]], [[Alternative Splicing]]).
- **Big genomes, little of it coding.** Protein-coding exons make up about 1.2% of the human euchromatic genome,[^ihgsc] and eukaryotic genome sizes vary more than 60,000-fold without tracking gene number ([[Genome]]).[^elliott]
- **Several genomes per cell.** Besides the nuclear chromosomes, mitochondria (and the chloroplasts of plants and algae) keep small genomes of their own ([[Mitochondrion]]),[^alberts14] which appear as extra records in an assembly, with their own copy number and genetic code ([[Genetic Code#Advanced (L3)]]).
- **Compartments must be addressed.** Every protein made in the cytosol has to reach its compartment, guided by signals in its sequence; localization annotations and predictors rest on this ([[Protein Targeting]], [[Organelle]]).[^alberts12]

## Core (L1)

![[eukaryotic-cell-organelles.svg]]

Like a prokaryotic cell, a eukaryotic cell has a plasma membrane, cytoplasm and ribosomes; but it is typically larger, its DNA is enclosed in a nucleus, and other membrane-bound organelles divide its interior into compartments with separate functions.[^os43] The main systems, each with its own note:

- the [[Cell Nucleus|nucleus]]: chromosomes, transcription and RNA processing;
- the [[Endomembrane System|endomembrane system]] (endoplasmic reticulum, Golgi apparatus, lysosomes, vesicles): making, modifying and shipping proteins and lipids;
- [[Mitochondrion|mitochondria]], and chloroplasts in plants: energy conversion;
- the [[Cytoskeleton|cytoskeleton]]: shape, internal transport and division.

[[Organelle]] maps every compartment to its function.

### Eukaryote versus prokaryote, down to the genome

| Feature | Prokaryote | Eukaryote |
|---|---|---|
| Nucleus | none: DNA in the nucleoid[^os42] | DNA enclosed by the nuclear envelope[^os43] |
| Membrane-bound organelles | none[^os42] | many: ER, Golgi, lysosomes, peroxisomes, mitochondria, chloroplasts in plants[^os43] |
| Typical size | 0.1 to 5 µm | 10 to 100 µm[^os42] |
| Chromosomes | usually one, circular[^os14] | several, linear[^os43][^alberts4] |
| DNA packaging | supercoiled in the nucleoid | wound around histones into nucleosomes: chromatin[^os14][^alberts4] |
| Cytosolic ribosomes | 70S | 80S[^alberts] |
| Transcription and translation | coupled in one compartment | separated by the nuclear envelope, with RNA processing in between[^os15] |
| Genes | dense, generally without introns, often in operons | often split by introns, usually one gene per mRNA, much DNA between genes[^os16][^alberts] |
| Example gene density | *E. coli*: 4,288 protein-coding genes in 4.64 Mb[^blattner] | human: 20,000 to 25,000 protein-coding genes in 3.1 Gb[^ihgsc][^nurk] |
| Division | binary fission | mitosis, and meiosis for sexual reproduction[^os10] |

Per megabase, *E. coli* carries about 924 protein-coding genes and the human genome 6.5 to 8.2: two orders of magnitude apart.

## Deeper (L2)

### Why compartments?

- **Surface.** A cell 20 µm across has 8,000 times the volume of a 1 µm cell but only 1/20 of its surface-to-volume ratio ([[Cell#Mathematical representation]]). Internal membranes give a eukaryotic cell far more membrane area than its plasma membrane alone.[^alberts12] Membrane-bound processes that a prokaryote runs in its plasma membrane move inside: the respiratory electron transport chain sits in the inner membrane of mitochondria.[^os7]
- **Specialization.** Each compartment holds its own set of enzymes and conditions, so incompatible processes run side by side; in exchange, the cell must deliver every protein to the right compartment ([[Protein Targeting]]).[^alberts12]

### Genome organization

- **Linear chromosomes** need two telomeres, one centromere and many replication origins each ([[Chromosome]], [[DNA Replication]]).[^alberts4]
- **Chromatin.** DNA wraps around histone proteins into nucleosomes, which fold further; packaging controls which genes are accessible ([[Chromatin]]).[^alberts4]
- **Split genes.** Transcripts are capped, spliced and polyadenylated in the nucleus before export; alternative splicing multiplies the products of a gene ([[RNA Processing]], [[Cell Nucleus]]).[^os15][^os16]
- **Size without genes.** Genome size varies more than 60,000-fold and is not explained by gene number: most of a large genome is non-coding DNA ([[Genome#Deeper (L2)]]).[^elliott]
- **Ploidy.** Many eukaryotes alternate between diploid cells and haploid cells produced by meiosis ([[Ploidy]], [[Meiosis]]).[^os11]

### Two kinds of ancestry

Mitochondria descend from bacteria taken up by an ancestral eukaryotic cell ([[Mitochondrion]]),[^alberts14] while the eukaryotic machinery for replication, transcription and translation resembles that of archaea.[^alberts1] The eukaryotic cell thus carries traces of both prokaryotic domains ([[Archaea]], [[Tree of Life]]).

## Advanced (L3)

- **From genome to transcripts.** Because genes are split, a transcript is a path through exons: aligning RNA-seq reads is a splice-aware problem, and expression is quantified per isoform ([[Spliced Read Alignment]], [[Transcript Quantification]]).
- **Gene prediction is harder.** In a eukaryote, an open reading frame on the genome is interrupted by introns, so the ORF scan that works on a bacterial chromosome is replaced by models of exons, introns and splice sites ([[Gene Finding]], [[Open Reading Frame]]).
- **One genome, many cell types.** The cells of one individual share essentially the same genome and differ in the genes they express;[^alberts] cell types are defined from these expression programs ([[Cell Differentiation]], [[Cell Type]]).
- **Annotation files encode the difference.** In GFF3, a split gene is a hierarchy: a gene feature, its transcripts, and their exons and CDS segments, linked by `Parent` attributes ([[GFF Format]], [[Gene Annotation]]).[^gff3] The summary statistics below read organization straight from such records.

## Mathematical representation

**Size.** For spheres of diameters $d_e$ and $d_p$, the volume ratio is $(d_e/d_p)^3$ and the surface-to-volume ratio scales as $d_p/d_e$: with $d_p = 1$ µm and $d_e = 20$ µm, 8,000 times the volume and 1/20 of the $S/V$.

**Gene organization in an annotated region.** Let a region of length $L$ hold $N$ non-overlapping genes; gene $g$ has strand $s_g$ and $k_g$ exons $[a_{g,i}, b_{g,i}]$ (1-based, inclusive), genes sorted by start. Then

$$\rho = \frac{N}{L}, \qquad f_{\mathrm{exon}} = \frac{1}{L}\sum_{g=1}^{N}\sum_{i=1}^{k_g}\left(b_{g,i} - a_{g,i} + 1\right), \qquad \bar{n}_{\mathrm{intron}} = \frac{1}{N}\sum_{g=1}^{N}(k_g - 1),$$

and the number of **operon-like pairs** is the number of consecutive genes $g, g+1$ with $s_g = s_{g+1}$ and a gap $a_{g+1,1} - b_{g,k_g} - 1 \le \Delta$ for a chosen threshold $\Delta$.

## Computational representation

Gene models are stored as features with coordinates and strands ([[GFF Format]]). The function below summarizes organization for two invented regions, one bacterium-like and one eukaryote-like:

```python
# Invented toy annotations: gene -> (strand, exons as 1-based inclusive intervals)
TOY_BACTERIUM = {"length": 10_000, "genes": {
    "geneA": ("+", [(101, 1000)]), "geneB": ("+", [(1021, 1800)]),
    "geneC": ("+", [(1815, 2700)]), "geneD": ("-", [(3000, 3900)]),
    "geneE": ("+", [(4100, 5600)]), "geneF": ("-", [(5650, 6900)]),
    "geneG": ("-", [(7000, 7800)]), "geneH": ("-", [(7820, 9900)]),
}}
TOY_EUKARYOTE = {"length": 100_000, "genes": {
    "geneX": ("+", [(5001, 5200), (8001, 8150), (15001, 15400)]),
    "geneY": ("-", [(40001, 40300), (42001, 42100), (47001, 47120), (52001, 52500)]),
    "geneZ": ("+", [(80001, 81500)]),
}}


def organization(region: dict, max_gap: int = 50) -> dict:
    """Summary statistics of gene organization in an annotated region."""
    genes = sorted(region["genes"].values(), key=lambda g: g[1][0][0])
    exonic = sum(end - start + 1 for _, exons in genes for start, end in exons)
    introns = sum(len(exons) - 1 for _, exons in genes)
    # operon-like neighbours: same strand, at most max_gap bp between them
    close_pairs = sum(1 for (s1, ex1), (s2, ex2) in zip(genes, genes[1:])
                      if s1 == s2 and ex2[0][0] - ex1[-1][1] - 1 <= max_gap)
    return {"genes_per_10kb": round(len(genes) / region["length"] * 1e4, 1),
            "exonic_fraction": round(exonic / region["length"], 3),
            "introns_per_gene": round(introns / len(genes), 2),
            "close_same_strand_pairs": close_pairs}


for name, region in (("toy bacterium", TOY_BACTERIUM), ("toy eukaryote", TOY_EUKARYOTE)):
    print(name, organization(region))
```

```text
toy bacterium {'genes_per_10kb': 8.0, 'exonic_fraction': 0.91, 'introns_per_gene': 0.0, 'close_same_strand_pairs': 3}
toy eukaryote {'genes_per_10kb': 0.3, 'exonic_fraction': 0.033, 'introns_per_gene': 1.67, 'close_same_strand_pairs': 0}
```

The toy values only illustrate the contrast; the real *E. coli* and human numbers are in [[Genome]].

## Worked example

> [!example] Prokaryote or eukaryote? Reading the evidence in sequencing data
> 1. **An assembly of 16 linear chromosomes totalling about 12 Mb.** Several linear chromosomes point to a eukaryote; budding yeast has exactly this layout, 12,068 kb on 16 chromosomes.[^goffeau]
> 2. **RNA-seq reads that align with gaps of hundreds of bases**, the gaps starting with GT and ending with AG: introns spliced out of the RNA,[^alberts] a eukaryotic signature.
> 3. **One circular contig of 4.6 Mb with about 0.9 genes per kb**: a prokaryotic chromosome, like that of *E. coli*.[^blattner]
> 4. **A circular contig of 16,569 bp at very high depth in a human sample.** Circular and small, yet not a bacterium: it is the human mitochondrial genome,[^anderson] present in many copies per cell. A circular molecule alone does not prove a prokaryote.

## Common misconceptions

> [!warning] "Eukaryotes are multicellular"
> Many are single cells, such as yeasts and protozoa.[^alberts1]

> [!warning] "Eukaryotes evolved from 'the prokaryotes'"
> Prokaryotes are two separate primary lines, not one ancestral group.[^woese] Eukaryotes resemble archaea in their information machinery, and their mitochondria descend from bacteria.[^alberts1][^alberts14]

> [!warning] "A bigger genome means a more complex organism"
> Eukaryotic genome size varies more than 60,000-fold independently of gene number; most of a large genome is non-coding.[^elliott]

## Exercises

> [!question] Exercise 1 (L1)
> For a prokaryote and a eukaryote, state: where the DNA is, the shape and number of chromosomes, the type of cytosolic ribosome, and whether translation can start before transcription ends.

> [!success]- Solution
> Prokaryote: DNA in the nucleoid; usually one circular chromosome; 70S ribosomes; yes, translation starts on the growing mRNA. Eukaryote: DNA in the nucleus; several linear chromosomes; 80S ribosomes; no, the mRNA is processed and exported first.

> [!question] Exercise 2 (L1)
> Cell 1 has 80S ribosomes, histones and a 12 Mb genome on 16 linear chromosomes. Cell 2 has 70S ribosomes and one circular 4.6 Mb chromosome. Classify each and suggest an organism.

> [!success]- Solution
> Cell 1 is eukaryotic, consistent with budding yeast, *Saccharomyces cerevisiae* (12,068 kb, 16 chromosomes). Cell 2 is prokaryotic, consistent with *E. coli*.

> [!question] Exercise 3 (L2)
> Explain why scanning a bacterial genome for long open reading frames finds most of its genes, while the same scan on a human chromosome fails for most genes.

> [!success]- Solution
> Bacterial genes are dense and generally uninterrupted, so each is one long ORF. Human coding sequences are split into exons separated by introns, often long ones; read straight on the genome, the reading frame is interrupted, and intron sequence soon hits a stop codon in one frame or another. The coding sequence exists continuously only in the spliced mRNA, so eukaryotic gene finders model exons, introns and splice sites.

> [!question] Exercise 4 (L2)
> A spherical eukaryotic cell is 20 µm across, a bacterium 1 µm. Compute the ratio of their volumes and of their surface-to-volume ratios, and explain how compartmentalization helps the large cell.

> [!success]- Solution
> Volume ratio $20^3 = 8000$; $S/V$ ratio $1/20$. The large cell has relatively little plasma membrane per unit volume; internal membranes (ER, mitochondrial inner membrane) add the membrane area that membrane-bound processes need, and compartments keep incompatible reactions apart.

> [!question] Exercise 5 (L3, Python)
> Using `organization` and the toy regions above: (a) count operon-like pairs in the toy bacterium for `max_gap` = 10, 50 and 100; (b) add an invented gene `geneW` on `+` with exons (60001, 60100), (61001, 61100), (62001, 62100) to the toy eukaryote and recompute. What do the results say about rule-based operon calls?

> [!success]- Solution
> ```python
> for gap in (10, 50, 100):
>     print(gap, organization(TOY_BACTERIUM, max_gap=gap)["close_same_strand_pairs"])
> TOY_EUKARYOTE["genes"]["geneW"] = ("+", [(60001, 60100), (61001, 61100), (62001, 62100)])
> print(organization(TOY_EUKARYOTE))
> ```
> Output:
> ```text
> 10 0
> 50 3
> 100 4
> {'genes_per_10kb': 0.4, 'exonic_fraction': 0.036, 'introns_per_gene': 1.75, 'close_same_strand_pairs': 0}
> ```
> The operon-like count goes from 0 to 4 with the threshold: a distance rule alone is fragile, and real operon predictions add evidence such as conservation of gene order or co-expression ([[Operon]]). The eukaryotic region stays sparse and intron-rich whatever gene is added.

## Mastery checklist

- [ ] 1 Recognized: I can define a eukaryote and name its main compartments.
- [ ] 2 Understood: I can contrast eukaryotic and prokaryotic cells feature by feature, down to chromosomes, chromatin, introns and gene density.
- [ ] 3 Practiced: I can compute size ratios and summarize gene organization from annotation records in code.
- [ ] 4 Applied: I compared a real bacterial and a real eukaryotic annotation file (genes per Mb, exons per gene) and explained the differences.
- [ ] 5 Explained: I can teach the two ancestries of the eukaryotic cell and why its genome organization changes alignment, gene finding and annotation.

## References

[^os42]: [[Biology 2e (OpenStax)]], section 4.2 "Prokaryotic Cells" (the prokaryotic cell plan; prokaryotic and eukaryotic cell sizes).
[^os43]: [[Biology 2e (OpenStax)]], section 4.3 "Eukaryotic Cells" (nucleus, membrane-bound organelles and several rod-shaped chromosomes; components shared with prokaryotes).
[^os7]: [[Biology 2e (OpenStax)]], chapter "Cellular Respiration" (the electron transport chain in the inner mitochondrial membrane of eukaryotes and the plasma membrane of prokaryotes).
[^os10]: [[Biology 2e (OpenStax)]], chapter "Cell Reproduction" (mitosis in eukaryotes, binary fission in prokaryotes).
[^os11]: [[Biology 2e (OpenStax)]], section 11.1 "The Process of Meiosis" (haploid and diploid cells).
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (DNA packaging in prokaryotes and eukaryotes: supercoiling, histones and nucleosomes).
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (transcription in prokaryotes and eukaryotes, RNA processing and introns).
[^os16]: [[Biology 2e (OpenStax)]], ch. 16 "Gene Expression" (operons; alternative RNA splicing).
[^alberts1]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 1 "Cells and Genomes", section "The Diversity of Genomes and the Tree of Life" (the range of eukaryotes; archaea compared with eukaryotes and bacteria).
[^alberts4]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 4 "DNA and Chromosomes" (linear chromosomes with replication origins, a centromere and two telomeres; nucleosomes and chromatin).
[^alberts12]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 12 "Intracellular Compartments and Protein Sorting" (the compartmentalization of cells, internal membranes, protein sorting).
[^alberts14]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 14 "Energy Conversion: Mitochondria and Chloroplasts" (organelle genomes and their bacterial origin).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of ribosomes (70S and 80S), of gene structure and RNA splicing (introns beginning with GU and ending with AG), and of the constancy of the genome across the cells of an organism.
[^woese]: [[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]], *PNAS* 74:5088-5090.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* 277:1453-1462.
[^goffeau]: [[Goffeau 1996 - Life with 6000 Genes]], *Science* 274(5287) (12,068 kb on 16 chromosomes).
[^gff3]: [[Sequence Ontology GFF3 Specification]], the canonical gene (gene, transcripts, exons and CDSs linked by `Parent`).
[^ihgsc]: [[IHGSC 2004 - Finishing the Euchromatic Sequence of the Human Genome]], *Nature* 431:931-945 (gene count, protein-coding exons as 1.2% of the euchromatic genome).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* 376:44-53.
[^elliott]: [[Elliott 2015 - The C-Value Enigma and the Evolution of Eukaryotic Genome Content]], *Philosophical Transactions of the Royal Society B*.
[^anderson]: [[Anderson 1981 - Sequence and Organization of the Human Mitochondrial Genome]], *Nature* 290:457-465.
