---
aliases:
  - Plasmids
  - Extrachromosomal Replicon
  - R Plasmid
  - Resistance Plasmid
  - F Plasmid
  - Plasmide
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[DNA Replication]]"
  - "[[Bacteria]]"
  - "[[Genome]]"
  - "[[Gene]]"
related:
  - "[[Horizontal Gene Transfer]]"
  - "[[Molecular Cloning]]"
  - "[[Antibiotic]]"
  - "[[Antimicrobial Resistance]]"
  - "[[Transposable Element]]"
  - "[[Bacteriophage]]"
  - "[[Sequencing Coverage]]"
  - "[[Genome Assembly]]"
  - "[[Pangenome]]"
projects: []
sources:
  - "[[Microbiology (OpenStax)]]"
  - "[[del Solar 1998 - Replication and Control of Circular Bacterial Plasmids]]"
  - "[[Smillie 2010 - Mobility of Plasmids]]"
  - "[[Carattoli 2014 - In Silico Detection and Typing of Plasmids Using PlasmidFinder and Plasmid Multilocus Sequence Typing]]"
  - "[[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]]"
  - "[[Korem 2015 - Growth Dynamics of Gut Microbiota Inferred from Single Metagenomic Samples]]"
---

# Plasmid

> [!abstract]
> A plasmid is a DNA molecule that lives beside the chromosome and copies itself with its own origin and controls. The cell can usually do without it, but its accessory genes, resistance genes first among them, can decide whether the cell survives.

## Definition

A **plasmid** is an extrachromosomal DNA molecule that replicates independently of the chromosome.[^m33] It is a **replicon**: an origin of replication (oriV) together with the initiator proteins and regulatory elements that start its replication and control how often it happens.[^delsolar] Plasmids are usually small, circular, double-stranded molecules; most common in bacteria, they also occur in archaea and eukaryotes, and they often carry genes for advantageous traits such as antibiotic resistance.[^m33]

## Why it matters

- **Resistance genes travel on plasmids.** Resistance (R) plasmids combine resistance genes with genes for conjugation and can move between species ([[Horizontal Gene Transfer]], [[Antimicrobial Resistance]]).[^m11] Whether a resistance gene sits on the chromosome or on a plasmid is a first question in pathogen genomics, because it changes how the gene can spread.
- **Replicon typing.** PlasmidFinder screens assemblies for known replicons. Its 2014 database held 116 replicon sequences built from 559 sequenced Enterobacteriaceae plasmids, and it found zero to five different replicons per genome in 49 *Salmonella* Typhimurium draft genomes.[^carattoli]
- **Plasmids distort read counts and assemblies.** A plasmid present in several copies per cell yields proportionally more reads than the chromosome (Mathematical representation; [[Sequencing Coverage]]). Transposable elements, which can move between plasmids and chromosomes, are repeats for the assembler ([[Transposable Element]], [[Genome Assembly]]).[^m11]
- **Vectors.** Engineered plasmids are the workhorse vectors of [[Molecular Cloning#Principle|molecular cloning]].[^m12]

## Core (L2)

### A replicon plus cargo

![[plasmid-modules-mobility-classes.svg]]

A plasmid's genes fall into modules:

- **Replication.** oriV and the rep initiator define the replicon, so every plasmid has this module. Circular plasmids replicate by one of three mechanisms: theta-type, strand displacement or rolling circle.[^delsolar]
- **Transfer** (conjugative plasmids only). An origin of transfer (oriT), a relaxase that cuts one strand there, and mating-pair formation (MPF) genes that build the pilus and channel joining donor and recipient.[^smillie][^m11]
- **Cargo.** Accessory genes such as antibiotic resistance genes.[^m33][^m11]

### Copy number and incompatibility

- Each replicon controls its own initiation, which keeps the number of copies per cell, the **copy number**, within a range typical of that plasmid; a cell can hold hundreds of copies of a small plasmid.[^delsolar][^m33]
- **Incompatibility.** Two plasmids that share the same replication control are counted as one pool, so a cell line cannot keep both: one of them is lost in the descendants (Exercise 4 simulates why).[^delsolar] Plasmids are classified into incompatibility (Inc) groups, and sequence-based replicon typing reports which replicon families a genome carries.[^carattoli]

### Accessory genes and the F plasmid

- **R plasmids** carry resistance genes and the genes for their own conjugation, and can be transferred between species.[^m11]
- **The F plasmid** (fertility factor) is the classic conjugative plasmid. An F⁺ cell makes an F pilus that contacts an F⁻ cell; one strand of the plasmid is transferred and copied, and both cells end up F⁺. When F integrates into the chromosome, the cell (called Hfr) can transfer chromosomal genes as well.[^m11] The mechanics are in [[Horizontal Gene Transfer]].

### Mobility classes

| Class | Transfer genes | Moves by |
|---|---|---|
| Conjugative | oriT, relaxase and MPF | itself |
| Mobilizable | oriT and relaxase, no MPF | the MPF of a conjugative plasmid in the same cell |
| Nonmobilizable | none | other routes only ([[Horizontal Gene Transfer]]) |

A survey of 1,730 sequenced plasmids found that about half are nonmobilizable and about half of the rest are conjugative:[^smillie] most plasmids cannot move on their own.

## Advanced (L3)

### Plasmids in sequencing data

1. **Depth reveals copies.** Coverage grows with the number of copies of a sequence in the sample,[^lander] so a contig's depth divided by the chromosome's depth estimates copies per chromosome. Choose the reference with care: in growing cultures, chromosome coverage peaks at the replication origin and falls toward the terminus.[^korem]
2. **Circularity.** A circular molecule has no ends; a contig whose end repeats its start closes on itself and is a candidate plasmid (Computational representation).
3. **Replicon hits.** PlasmidFinder reports replicons that match its database at 80% nucleotide identity or more.[^carattoli] No hit does not mean no plasmid: the replicon may belong to a family missing from the database.
4. **Shared repeats.** A mobile element present on both plasmid and chromosome is a repeat; a read shorter than the repeat cannot contain both of its flanks, so short-read assemblies leave such plasmids fragmented and ambiguously linked, which [[Long-Read Assembly|long reads]] can resolve.

### Replication mode and host range

Strand-displacement replication is associated with the IncQ family of broad-host-range plasmids, and the older idea that theta replication belongs to Gram-negative hosts and rolling-circle replication to Gram-positive hosts is probably wrong.[^delsolar] Host range matters for epidemiology: a broad-host-range plasmid can carry its cargo across distant lineages ([[Horizontal Gene Transfer]]).

## Mathematical representation

**Random segregation.** A cell holds $N$ copies at division, and each copy goes to either daughter independently with probability $\tfrac{1}{2}$. A given daughter receives none with probability $2^{-N}$; both cannot be empty, so the probability that the division yields a plasmid-free daughter is

$$\ell = 2 \cdot 2^{-N} = 2^{1-N}.$$

Without fitness differences, plasmid-bearing cells $P_g$ and plasmid-free cells $F_g$ follow $P_{g+1} = (2 - \ell) P_g$ and $F_{g+1} = 2F_g + \ell P_g$, so the bearing fraction after $g$ generations is

$$p_g = \frac{P_g}{P_g + F_g} = \left(1 - \frac{\ell}{2}\right)^g .$$

With $N = 2$, $\ell = 0.5$: the model implies that a low-copy plasmid persisting in a population must segregate better than at random or be selected for.

**Copy number from depth.** With $n$ reads of length $L$ on a genome of length $G$, the coverage is $c = nL/G$.[^lander] A plasmid present at $k$ copies per chromosome is sampled $k$ times as often, so its depth is $d_p = k\,d_c$ and $\hat{k} = d_p / d_c$.

**Incompatibility as a shared pool.** If one control keeps $A + B = N$, new copies are made from randomly chosen existing ones and the pool is split at random at division: the share of $A$ drifts like a neutral allele ([[Genetic Drift]]) until one type is lost. With separate controls, each type is restored every generation and is lost only by a rare segregation failure.

## Computational representation

```python
import random


def free_daughter_probability(copies: int) -> float:
    """P(a division yields a plasmid-free daughter) when `copies` copies segregate at random."""
    return 2.0 ** (1 - copies)


def fraction_bearing(copies: int, generations: int) -> float:
    """Fraction of plasmid-bearing cells after g generations (random segregation, no fitness cost)."""
    return (1 - free_daughter_probability(copies) / 2) ** generations


print("copies  P(free daughter)  bearing after 100 generations")
for n in (2, 4, 8, 16, 32):
    print(f"{n:6d}  {free_daughter_probability(n):16.2e}  {fraction_bearing(n, 100):.4f}")

# Invented assembly: contig -> (length in bp, mean read depth)
CONTIGS = {"contig_1": (2_950_000, 41.0), "contig_2": (1_850_000, 39.5),
           "contig_3": (48_200, 44.8), "contig_4": (5_400, 236.0)}


def copies_per_chromosome(contigs: dict, chromosome_min_len: int = 1_000_000) -> dict:
    """Depth of each contig divided by the length-weighted depth of the long (chromosomal) contigs."""
    long = [(length, depth) for length, depth in contigs.values() if length >= chromosome_min_len]
    chrom_depth = sum(length * depth for length, depth in long) / sum(length for length, _ in long)
    return {name: round(depth / chrom_depth, 1) for name, (_, depth) in contigs.items()}


print(copies_per_chromosome(CONTIGS))


def end_overlap(seq: str, min_len: int = 20) -> int:
    """Length of the longest suffix that equals a prefix: a contig that closes on itself."""
    for k in range(len(seq) // 2, min_len - 1, -1):
        if seq[-k:] == seq[:k]:
            return k
    return 0


random.seed(7)
molecule = "".join(random.choice("ACGT") for _ in range(400))   # invented circular sequence
circular_contig = molecule + molecule[:55]                      # read across the junction once
print(end_overlap(circular_contig), end_overlap(molecule))
```

```text
copies  P(free daughter)  bearing after 100 generations
     2          5.00e-01  0.0000
     4          1.25e-01  0.0016
     8          7.81e-03  0.6761
    16          3.05e-05  0.9985
    32          4.66e-10  1.0000
{'contig_1': 1.0, 'contig_2': 1.0, 'contig_3': 1.1, 'contig_4': 5.8}
55 0
```

Doubling the copy number roughly squares the failure probability, since $\ell(2N) = \ell(N)^2 / 2$: from 8 to 16 copies, $\ell$ drops from $7.8 \times 10^{-3}$ to $3.1 \times 10^{-5}$.

## Worked example

> [!example] Which contigs are plasmids? (invented assembly)
> An isolate's assembly has four contigs: contig_1 (2.95 Mb, depth 41×), contig_2 (1.85 Mb, 39.5×), contig_3 (48.2 kb, 44.8×) and contig_4 (5.4 kb, 236×).
> 1. **Chromosome depth.** The two megabase contigs are chromosomal; their length-weighted depth is 40.4×.
> 2. **Copies.** contig_4: $236 / 40.4 \approx 5.8$ copies per chromosome; contig_3: about 1.1.
> 3. **contig_4.** Multicopy, and its ends overlap by 55 bp: a circular molecule, very likely a small plasmid. A replicon hit would confirm it.
> 4. **contig_3.** Its depth matches the chromosome: a low-copy plasmid or a chromosomal piece, depth cannot tell. Look for a replicon, transfer genes (relaxase, MPF) and circularity, or link it with long reads.
> 5. **Report.** "contig_4: plasmid, about 6 copies per chromosome; contig_3: unresolved." Not "contig_4: contamination".

## Common misconceptions

> [!warning] "Every plasmid can transfer itself"
> Only conjugative plasmids carry a full transfer module. Mobilizable plasmids need a conjugative helper in the same cell, and about half of sequenced plasmids are nonmobilizable.[^smillie]

> [!warning] "A contig with very high depth is contamination"
> A multicopy plasmid is expected to have several times the chromosome's depth ($\hat{k} = d_p / d_c$). Check circularity and replicon hits before discarding it.

> [!warning] "Plasmids are a bacterial peculiarity"
> They are most common in bacteria, but archaea and eukaryotes carry plasmids too.[^m33]

> [!warning] "A gene on a plasmid is a permanent part of the genome"
> Plasmids can be lost at division. The random-segregation model shows how fast a low-copy plasmid would vanish without better-than-random partitioning or selection for its genes.

## Exercises

> [!question] Exercise 1 (L2)
> Classify three invented plasmids by mobility: P1 carries oriV, rep, oriT, a relaxase gene and a set of MPF genes; P2 carries oriV, rep, oriT and a relaxase gene; P3 carries oriV, rep and a resistance gene. Which can reach a new cell on its own, and what does P2 need?

> [!success]- Solution
> P1 is conjugative and transfers itself. P2 is mobilizable: it can be transferred only if a conjugative plasmid in the same cell provides the mating-pair formation apparatus. P3 is nonmobilizable: its resistance gene can spread only by routes that do not use its own transfer genes ([[Horizontal Gene Transfer]]).[^smillie]

> [!question] Exercise 2 (L2)
> A plasmid has 8 copies at division and segregates at random. Compute the probability that a division yields a plasmid-free daughter, and the fraction of plasmid-bearing cells after 100 generations without selection.

> [!success]- Solution
> $\ell = 2^{1-8} = 2^{-7} \approx 0.0078$, and $p_{100} = (1 - 0.0039)^{100} \approx 0.676$: a third of the population has lost the plasmid. `fraction_bearing(8, 100)` returns 0.676.

> [!question] Exercise 3 (L2)
> A plasmid contig has depth 220×. The chromosome's median depth is 40×, but a window around the replication origin reads 55×. Estimate the copy number with each reference. Which one should you report, and why?

> [!success]- Solution
> $220/40 = 5.5$ versus $220/55 = 4.0$. Report the whole-chromosome value (median or length-weighted mean): in a growing culture, coverage near the origin is inflated relative to the terminus,[^korem] so a local window biases the estimate.

> [!question] Exercise 4 (L3, Python)
> Simulate one cell lineage carrying two plasmid types, A and B, with 10 copies in total. Compare a shared replication control (one pool of 10, new copies made from random existing copies, random split at division) with separate controls (5 copies of each, restored every generation). Report the median number of generations until one type is lost and the fraction of lineages that lose one within 100 generations.

> [!success]- Solution
> ```python
> def generations_to_loss(shared_control: bool, copies: int = 10, max_gen: int = 1000,
>                         rng: random.Random = random.Random(1)) -> int:
>     """Follow one cell lineage carrying plasmids A and B until one type is lost."""
>     a = b = copies // 2
>     for g in range(1, max_gen + 1):
>         if shared_control:                # one control counts A and B together
>             for _ in range(copies):       # each new copy is made from a random existing copy
>                 if rng.random() < a / (a + b):
>                     a += 1
>                 else:
>                     b += 1
>             daughter = rng.sample(["A"] * a + ["B"] * b, copies)
>             a, b = daughter.count("A"), daughter.count("B")
>         else:                             # separate controls: each type doubled, split, restored
>             a = copies // 2 if any(rng.random() < 0.5 for _ in range(2 * a)) else 0
>             b = copies // 2 if any(rng.random() < 0.5 for _ in range(2 * b)) else 0
>         if a == 0 or b == 0:
>             return g
>     return max_gen
>
>
> for shared in (True, False):
>     times = sorted(generations_to_loss(shared) for _ in range(500))
>     print("shared" if shared else "separate", times[len(times) // 2],
>           sum(t <= 100 for t in times) / len(times))
> ```
> ```text
> shared 10 1.0
> separate 339 0.17
> ```
> With a shared control, every lineage loses one type within 100 generations (median 10): the plasmids are incompatible. With separate controls, loss needs all 10 copies of one type to go to the other daughter ($2^{-10}$ per type per division), so the median is over 300 generations.

> [!question] Exercise 5 (L3)
> PlasmidFinder reports no replicon in the assembly of a soil bacterium, yet a 60 kb contig has depth 3× the chromosome's and overlapping ends. What do you conclude, and how would you test it?

> [!success]- Solution
> The contig behaves like a circular multicopy replicon; the missing hit most likely means that its replicon family is not in the database, which was built from Enterobacteriaceae plasmids.[^carattoli] Test it by searching the contig for replication initiator, relaxase and MPF genes ([[Gene Annotation]]), and by confirming circularity with long reads.

## Mastery checklist

- [ ] 1 Recognized: I can define a plasmid as an extrachromosomal replicon and name its modules (replication, transfer, cargo).
- [ ] 2 Understood: I can explain copy number, incompatibility, the F and R plasmids, and the three mobility classes.
- [ ] 3 Practiced: I can compute segregation loss, estimate copy number from depth, and detect a self-overlapping contig in Python.
- [ ] 4 Applied: I identified the plasmids of a real bacterial assembly with depth, circularity and PlasmidFinder, and located its resistance genes on chromosome or plasmid.
- [ ] 5 Explained: I can teach why plasmids are hard to assemble, why replicon databases miss plasmids, and what a segregation model implies for low-copy plasmids.

## References

[^m33]: [[Microbiology (OpenStax)]], section 3.3 "Unique Characteristics of Prokaryotic Cells" (plasmids: extrachromosomal, usually small, circular, double-stranded DNA; often many copies per cell; more common in bacteria but also found in archaea and eukaryotes; genes for advantageous traits such as antibiotic resistance).
[^m11]: [[Microbiology (OpenStax)]], ch. 11 "Mechanisms of Microbial Genetics" (conjugation: F plasmid, F pilus, F⁺ and Hfr cells; R plasmids carrying resistance and conjugation genes and transferable between species; transposons moving between chromosomes and plasmids).
[^m12]: [[Microbiology (OpenStax)]], ch. 12 "Modern Applications of Microbial Genetics" (plasmid cloning vectors).
[^delsolar]: [[del Solar 1998 - Replication and Control of Circular Bacterial Plasmids]], *Microbiology and Molecular Biology Reviews* 62:434-464.
[^smillie]: [[Smillie 2010 - Mobility of Plasmids]], *Microbiology and Molecular Biology Reviews* 74:434-452.
[^carattoli]: [[Carattoli 2014 - In Silico Detection and Typing of Plasmids Using PlasmidFinder and Plasmid Multilocus Sequence Typing]], *Antimicrobial Agents and Chemotherapy* 58:3895-3903.
[^lander]: [[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]], *Genomics* 2:231-239 (coverage as read length times number of reads over genome length).
[^korem]: [[Korem 2015 - Growth Dynamics of Gut Microbiota Inferred from Single Metagenomic Samples]], *Science* 349:1101-1106 (coverage peak at the replication origin and trough at the terminus in growing bacteria).
