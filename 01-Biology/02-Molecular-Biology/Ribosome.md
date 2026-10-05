---
aliases:
  - Ribosomes
  - Ribosomal Subunit
  - 70S Ribosome
  - 80S Ribosome
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[RNA]]"
  - "[[Messenger RNA]]"
  - "[[Transfer RNA]]"
  - "[[Amino Acid]]"
related:
  - "[[Translation]]"
  - "[[Genetic Code]]"
  - "[[Non-Coding RNA]]"
  - "[[16S Ribosomal RNA]]"
  - "[[RNA Sequencing]]"
  - "[[Gene Expression]]"
  - "[[Antibiotic]]"
  - "[[Centrifugation]]"
projects: []
sources:
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Anderson 1981 - Sequence and Organization of the Human Mitochondrial Genome]]"
  - "[[Mortazavi 2008 - Mapping and Quantifying Mammalian Transcriptomes by RNA-Seq]]"
  - "[[Nissen 2000 - The Structural Basis of Ribosome Activity in Peptide Bond Synthesis]]"
  - "[[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]]"
  - "[[Ingolia 2009 - Genome-Wide Analysis in Vivo of Translation with Nucleotide Resolution Using Ribosome Profiling]]"
---

# Ribosome

> [!abstract]
> The ribosome is the cell's protein-making machine: a small subunit that holds the mRNA and checks each codon against a tRNA, and a large subunit whose RNA joins the amino acids together.

## Definition

A **ribosome** is a large ribonucleoprotein complex that translates mRNA into protein. It consists of two subunits of unequal size, each made of ribosomal RNA (rRNA) and many proteins. The **small subunit** binds the mRNA and matches tRNAs to its codons; the **large subunit** catalyses the formation of peptide bonds. Three binding sites for tRNA, **A**, **P** and **E**, span the two subunits.[^alberts][^os15] The ribosome is the machine of [[Translation]]; this note describes the machine itself.

## Why it matters

- **rRNA dominates cellular RNA.** rRNA is the most abundant RNA in the cell,[^alberts] so sequencing total RNA reads mostly rRNA. Transcriptome libraries therefore enrich for mRNA, for instance by poly(A) selection, as in the first mouse RNA-seq transcriptomes,[^mortazavi] or remove rRNA ([[RNA Sequencing]]).
- **rRNA is the yardstick of the tree of life.** Comparing ribosomal RNA sequences, present in every cell with the same function, Woese and Fox found three primary lines of descent, the discovery of the archaea.[^woese] Microbial community profiling builds on the same molecule ([[16S Ribosomal RNA]], [[Amplicon Sequencing]], [[Tree of Life]]).
- **Ribosome positions are sequencing data.** Ribosome profiling sequences the mRNA fragments protected by ribosomes and maps translation genome-wide with subcodon resolution,[^ingolia] measuring the translation layer of [[Gene Expression]].
- **A drug target.** Bacterial and eukaryotic ribosomes differ, and many antibiotics exploit the difference ([[Translation#Advanced (L3)]], [[Antibiotic]]).

## Core (L1)

![[ribosome-subunits-sites.svg]]

**Two subunits, one division of labour.**[^alberts]

| Subunit | Holds | Job |
|---|---|---|
| Small (30S in bacteria, 40S in eukaryotes) | the mRNA and the anticodon ends of the tRNAs | **decoding**: checks that each anticodon pairs correctly with the codon |
| Large (50S in bacteria, 60S in eukaryotes) | the acceptor ends of the tRNAs and the growing chain | **catalysis**: the peptidyl transferase centre joins amino acids; the chain leaves through an exit tunnel |

The subunits come together on an mRNA at the start of translation and separate after termination, so any ribosome can translate any mRNA.[^alberts]

**Three tRNA sites.**[^alberts][^os15]

| Site | Name | Holds during elongation |
|---|---|---|
| A | aminoacyl | the incoming charged tRNA, paired with the next codon |
| P | peptidyl | the tRNA carrying the growing chain |
| E | exit | the uncharged tRNA about to leave |

Each site spans both subunits: a tRNA's anticodon sits on the mRNA in the small subunit while its 3' end, with the amino acid or the chain, reaches the catalytic centre in the large subunit ([[Transfer RNA]]).[^alberts] The elongation cycle that moves tRNAs from A to P to E is in [[Translation#Core (L1)]].

**RNA at the core.** Most of the functional core is rRNA, and the peptide bond is made by rRNA, not by a protein: the ribosome is a **ribozyme** (L2).[^alberts][^nissen]

**How many.** An *E. coli* cell contains between 10,000 and 70,000 ribosomes; a eukaryotic cell contains millions, free in the cytosol or bound to the endoplasmic reticulum.[^os15][^alberts]

## Deeper (L2)

### Composition

Values from the reference textbook, rounded ("S" is the Svedberg unit of sedimentation):[^alberts]

| | Bacteria | Eukaryotes (cytosol) |
|---|---|---|
| Ribosome | 70S, about 2.5 million daltons | 80S, about 4.2 million daltons |
| Small subunit | 30S: 16S rRNA (about 1,540 nt) and about 21 proteins | 40S: 18S rRNA (about 1,900 nt) and about 33 proteins |
| Large subunit | 50S: 23S rRNA (about 2,900 nt), 5S rRNA (about 120 nt) and about 34 proteins | 60S: 28S (about 4,700 nt), 5.8S (about 160 nt) and 5S (about 120 nt) rRNAs and about 49 proteins |

In eukaryotes the 18S, 5.8S and 28S rRNAs are cut from one long precursor (45S) made by RNA polymerase I in the nucleolus, where ribosomes are assembled; the 5S rRNA is transcribed separately by RNA polymerase III ([[Transcription#Deeper (L2)]]).[^alberts] Mitochondria have their own ribosomes, which resemble bacterial ones; human mitochondrial DNA encodes their two rRNAs, 12S and 16S.[^alberts][^anderson]

### Sedimentation coefficients do not add

A particle spinning in a centrifuge sediments at a rate set by its sedimentation coefficient $s = m(1 - \bar{v}\rho)/f$, which grows with mass but is divided by a frictional coefficient $f$ that depends on size and shape.[^berg] Joining two subunits adds their masses, not their $s$ values: 30S + 50S gives a 70S particle, 40S + 60S an 80S one (derivation in Mathematical representation; see [[Centrifugation]] and [[Stokes' Law]]).

### The ribosome is a ribozyme

In 2000, atomic structures of the large subunit of the archaeon *Haloarcula marismortui* bound to substrate analogues showed that the analogues touch only conserved nucleotides of domain V of the 23S rRNA, and that no protein side-chain atom lies within about 18 Å of the peptide bond being formed.[^nissen] Ribosomal proteins sit mostly at the surface, stabilizing the rRNA core.[^alberts] Catalysis by RNA at the heart of every cell is one of the arguments of the RNA world hypothesis ([[RNA#Advanced (L3)]]).

### Why tRNAs must span both subunits

During elongation the large subunit first shifts relative to the small one, moving the acceptor ends of the two tRNAs into the next sites, then the small subunit moves exactly three nucleotides along the mRNA and the cycle resets.[^alberts] Because the mRNA and anticodons are held by the small subunit and the chemistry happens in the large one, only a molecule long enough to reach both, the L-shaped tRNA, can connect decoding to catalysis.

### Free and bound ribosomes

Ribosomes bound to the endoplasmic reticulum are the same as free ones: whether a ribosome binds the membrane is decided by the protein it is making (a signal sequence at its N-terminus), not by the ribosome ([[Protein Targeting]]).[^alberts]

## Advanced (L3)

**Ribosome profiling.** Digesting the mRNA not covered by ribosomes and sequencing the protected fragments ("footprints") gives the position of every ribosome with subcodon resolution. Ingolia and colleagues introduced it in budding yeast, comparing rich medium and starvation.[^ingolia] Three computational ideas follow directly from the ribosome's geometry:

1. **Site assignment.** A footprint covers the ribosome, so the codon in its P site lies at a fixed offset from the footprint's 5' end, to be estimated for each dataset (Worked example).
2. **Three-nucleotide periodicity.** Because ribosomes move codon by codon, footprint 5' ends pile up in one phase of the reading frame; the phase reveals which frame is translated, including unannotated [[Open Reading Frame|ORFs]] ([[Proteogenomics]]).
3. **Ribosome density.** Footprints per codon, divided by mRNA reads per codon from RNA-seq of the same sample, estimates how intensely each mRNA is translated ([[Gene Expression#Advanced (L3)]]).

**rRNA and phylogeny.** Woese and Fox inferred relationships from rRNA sequence fragments and found three lines of descent: eubacteria, archaebacteria and the ancestors of the eukaryotic cytoplasm.[^woese] The reasons are properties of the ribosome itself: every cell has one, it does the same job everywhere, and its rRNA can be compared across all of life ([[16S Ribosomal RNA]], [[Phylogenetic Tree]]).

**Structures.** The ribozyme result came from atomic structures determined by [[X-ray Crystallography]];[^nissen] ribosome structures can be explored in the [[RCSB Protein Data Bank]] with the tools of [[Structural Bioinformatics]], for instance to see where an [[Antibiotic]] binds.

## Mathematical representation

**Sedimentation.** With $M$ the molar mass, $\bar{v}$ the partial specific volume, $\rho$ the solvent density, $N_A$ Avogadro's number and $f$ the frictional coefficient, $s = M(1 - \bar{v}\rho)/(N_A f)$.[^berg] For a compact sphere of radius $r$ in a solvent of viscosity $\eta$, Stokes' law gives $f = 6\pi\eta r$, and $r \propto M^{1/3}$ at constant density, so
$$s = c\,M^{2/3} \quad\Longrightarrow\quad M \propto s^{3/2}.$$
If two subunits combine into a sphere of the same density, masses add, and
$$s_{12} = \left(s_1^{3/2} + s_2^{3/2}\right)^{2/3}.$$
This gives about 64S for 30S + 50S and about 80S for 40S + 60S (code below): sedimentation values are not additive, and the gap between 64S and the observed 70S measures how far the real particle is from this idealized sphere.

**Footprint mapping.** Let a CDS start at mRNA position $s_0$ (0-based) and let $\delta$ be the P-site offset. A footprint whose 5' end is at $x$ has its P-site nucleotide at $p = x + \delta - s_0$ relative to the start codon. It is in frame if $p \equiv 0 \pmod 3$, and then the P-site codon index is $k = p/3$; the A site holds codon $k+1$ and the E site codon $k-1$.

**Density and translational efficiency.** For a CDS of $L$ codons with $F$ in-frame footprints and $R$ RNA-seq reads per codon, define the footprint density $F/L$ and the translational efficiency $\mathrm{TE} = (F/L)/R$. With non-interfering ribosomes, density is proportional to the initiation rate divided by the elongation speed (Little's law, [[Translation#Mathematical representation]]), so TE mixes both.

## Computational representation

rRNA and footprints are ordinary sequences (FASTA, FASTQ); what is specific is the arithmetic on positions. First the sphere model of sedimentation, then footprint mapping on invented data:

```python
def combined_s(*subunits: float) -> float:
    """Sedimentation coefficient of a compact spherical complex, assuming s proportional to M^(2/3)."""
    return sum(s ** 1.5 for s in subunits) ** (2 / 3)


for small, large, observed in ((30, 50, 70), (40, 60, 80)):
    print(f"{small}S + {large}S: sum {small + large}S, sphere model {combined_s(small, large):.1f}S, observed {observed}S")
```

```text
30S + 50S: sum 80S, sphere model 64.5S, observed 70S
40S + 60S: sum 100S, sphere model 80.2S, observed 80S
```

```python
from collections import Counter

# Invented toy data: a 10-codon ORF starting at mRNA position 15 (0-based), and the 5' ends of
# ribosome footprints mapped to that mRNA. Assumed offset: the P-site codon starts 12 nt downstream.
CDS_START, N_CODONS, OFFSET = 15, 10, 12
footprint_5p = [3, 3, 3, 4, 6, 9, 9, 12, 12, 12, 12, 15, 18, 18, 21, 24, 24, 27, 27, 27, 30, 13, 33]


def p_site_codons(five_prime_ends, cds_start=CDS_START, offset=OFFSET):
    """Codon index (0 = start codon) in the P site, and the reading-frame phase of each footprint."""
    codons, phases = Counter(), Counter()
    for end in five_prime_ends:
        p = end + offset - cds_start
        phases[p % 3] += 1
        if p % 3 == 0 and 0 <= p // 3 < N_CODONS:
            codons[p // 3] += 1
    return codons, phases


codons, phases = p_site_codons(footprint_5p)
print("phase counts:", dict(sorted(phases.items())))
print("footprints per codon:", [codons[i] for i in range(N_CODONS)])
rpf_density = sum(codons.values()) / N_CODONS          # footprints per codon
mrna_density = 0.8                                      # invented RNA-seq reads per codon
print("translational efficiency:", round(rpf_density / mrna_density, 2))
```

```text
phase counts: {0: 21, 1: 2}
footprints per codon: [3, 1, 2, 4, 1, 2, 1, 2, 3, 1]
translational efficiency: 2.5
```

21 of 23 footprints fall in phase 0: the periodicity that identifies the translated frame. One in-frame footprint (5' end at 33) maps beyond the ORF and is discarded.

## Worked example

> [!example] Locating a ribosome from one footprint (invented data)
> A CDS starts at position 15 of an mRNA (0-based), and in this dataset the P-site nucleotide lies 12 nt downstream of a footprint's 5' end.
>
> 1. **P site.** A footprint starting at position 27 has its P-site nucleotide at $27 + 12 = 39$, that is $p = 39 - 15 = 24$ nt after the start of the CDS.
> 2. **Frame.** $24 \equiv 0 \pmod 3$: the footprint is in frame.
> 3. **Codons.** $k = 24/3 = 8$: the P site holds codon 8 (the 9th codon, counting the start codon as 0). The A site holds codon 9, waiting for the next aminoacyl-tRNA, and the E site codon 7.
> 4. **Chain length.** The peptidyl-tRNA in the P site carries the amino acids of codons 0 to 8, so this ribosome had made a 9-residue chain, most of it inside the exit tunnel.
> 5. **Out of frame.** A footprint starting at 13 gives $p = 10$, not a multiple of 3: it is either noise or evidence of translation in another frame.

## Common misconceptions

> [!warning] "30S plus 50S should make 80S"
> Svedberg values measure sedimentation rate, which depends on shape as well as mass. Masses add; S values do not.[^berg]

> [!warning] "Each tRNA site belongs to one subunit, and the large subunit reads the mRNA"
> The A, P and E sites span both subunits. The mRNA is held and decoded by the small subunit; the large subunit makes the peptide bond.[^alberts]

> [!warning] "Ribosomes on the endoplasmic reticulum are a special kind"
> Free and membrane-bound ribosomes are identical; the protein being synthesized, through its signal sequence, sends the ribosome to the membrane.[^alberts]

## Exercises

> [!question] Exercise 1 (L1)
> Name the two subunits of a bacterial and of a eukaryotic cytosolic ribosome, and say which one decodes the mRNA and which one catalyses the peptide bond.

> [!success]- Solution
> Bacteria: 30S (small, 16S rRNA) and 50S (large, 23S and 5S rRNA), forming a 70S ribosome. Eukaryotes: 40S (18S rRNA) and 60S (28S, 5.8S and 5S rRNA), forming 80S. The small subunit decodes (codon-anticodon matching), the large subunit's rRNA catalyses the peptide bond.

> [!question] Exercise 2 (L1)
> A tRNA sits in the P site. Where is its anticodon, where is its 3' end, and what is attached to that end?

> [!success]- Solution
> The anticodon is paired with the P-site codon on the mRNA, in the small subunit. The 3' end is in the large subunit, at the peptidyl transferase centre, and carries the growing polypeptide (the tRNA is a peptidyl-tRNA).

> [!question] Exercise 3 (L2, Python)
> Use `combined_s` to predict the sedimentation coefficient of a complex of two identical 30S particles, and of a 50S subunit alone plus a 5S rRNA considered as a separate sphere. Why is the second calculation physically naive?

> [!success]- Solution
> `combined_s(30, 30)` gives 47.6 and `combined_s(50, 5)` gives 51.0 (`print(round(combined_s(30, 30), 1), round(combined_s(50, 5), 1))`). Two equal spheres merging into one sphere do not double their $s$: the factor is $2^{2/3} \approx 1.59$. The second case is naive because 5S rRNA is part of the 50S particle, not a separate sphere added to it, and a long RNA is not spherical at all: the model only holds for compact particles of equal density.

> [!question] Exercise 4 (L2)
> In the 2000 large-subunit structure, no protein side-chain atom lies within about 18 Å of the peptide bond being formed. Why does this rule out a protein catalyst, and what would you have concluded if a lysine had been found 3 Å from the substrate?

> [!success]- Solution
> Catalysis requires chemical groups in contact with the substrate, at bond distances (a few Å). At 18 Å no protein group can take part in the reaction, so the rRNA nucleotides that contact the substrates must do it.[^nissen] A lysine at 3 Å would have made a protein contribution possible and the question open: proximity is necessary for catalysis, not sufficient, so mutational or biochemical tests would be needed.

> [!question] Exercise 5 (L3, Python)
> Change `OFFSET` to 13 in the footprint code and rerun it. What happens to the phase counts, and how would you choose the offset from real data without knowing it in advance?

> [!success]- Solution
> With offset 13 every $p$ increases by 1: the phase counts become `{1: 21, 2: 2}` and no footprint is counted in frame, so the densities drop to zero. In real data, align footprints on annotated start codons (or stop codons) of many genes and choose, for each footprint length, the offset that puts the P site on the start codon and maximizes the fraction of reads in one phase.

> [!question] Exercise 6 (L3)
> (a) Why does sequencing total cellular RNA without any selection waste most of the reads, and name one way transcriptome libraries avoid it? (b) Give two properties that made rRNA suitable for Woese and Fox's universal comparison.

> [!success]- Solution
> (a) rRNA is the most abundant RNA of the cell, so most reads would be rRNA.[^alberts] Libraries select poly(A) RNA (mRNA) or deplete rRNA ([[RNA Sequencing]]).[^mortazavi] (b) Every cellular organism has ribosomes, and rRNA does the same job in all of them, so homologous sequences can be compared from bacteria to eukaryotes.[^woese]

## Mastery checklist

- [ ] 1 Recognized: I can name the two subunits, their rRNAs, and the A, P and E sites.
- [ ] 2 Understood: I can explain the division of labour (decoding in the small subunit, catalysis by rRNA in the large one), why tRNAs span both subunits, and why S values do not add.
- [ ] 3 Practiced: I can map ribosome footprints to codons, check frame periodicity and compute a translational efficiency in Python.
- [ ] 4 Applied: I processed a public ribosome profiling or rRNA dataset (for example 16S amplicons) and interpreted it with the ribosome's geometry in mind.
- [ ] 5 Explained: I can teach how we know the ribosome is a ribozyme, and why rRNA is both a nuisance in RNA-seq and the backbone of microbial phylogeny.

## References

[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of the ribosome (subunit composition and sizes, rRNA core, A, P and E sites, elongation movements, number per cell), rRNA synthesis in the nucleolus, mitochondrial ribosomes, and free versus membrane-bound ribosomes.
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins", section on ribosomes and protein synthesis (ribosomes per *E. coli* cell, tRNA sites).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of ultracentrifugation and sedimentation coefficients.
[^anderson]: [[Anderson 1981 - Sequence and Organization of the Human Mitochondrial Genome]], *Nature* 290:457-465 (12S and 16S rRNA genes).
[^mortazavi]: [[Mortazavi 2008 - Mapping and Quantifying Mammalian Transcriptomes by RNA-Seq]], *Nature Methods* 5:621-628 (poly(A)-selected RNA).
[^nissen]: [[Nissen 2000 - The Structural Basis of Ribosome Activity in Peptide Bond Synthesis]], *Science* 289:920-930.
[^woese]: [[Woese 1977 - Phylogenetic Structure of the Prokaryotic Domain]], *PNAS* 74:5088-5090.
[^ingolia]: [[Ingolia 2009 - Genome-Wide Analysis in Vivo of Translation with Nucleotide Resolution Using Ribosome Profiling]], *Science* 324:218-223.
