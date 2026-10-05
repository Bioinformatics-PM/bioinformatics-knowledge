---
aliases:
  - Méiose
  - Meiosis I
  - Meiosis II
  - Reduction Division
  - Synapsis
  - Bivalent
  - Tetrad
  - Chiasma
  - Synaptonemal Complex
  - Nondisjunction
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mitosis]]"
  - "[[Chromosome]]"
  - "[[Ploidy]]"
  - "[[Allele]]"
related:
  - "[[Mendelian Inheritance]]"
  - "[[Genetic Recombination]]"
  - "[[Genetic Linkage]]"
  - "[[Haplotype]]"
  - "[[Haplotype Phasing]]"
  - "[[Linkage Disequilibrium]]"
  - "[[Sex-Linked Inheritance]]"
  - "[[Trio Analysis]]"
  - "[[Cell Cycle]]"
  - "[[Poisson Process]]"
  - "[[Mitochondrial DNA]]"
  - "[[Copy Number Variation]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[The Cell (Cooper)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Mangs 2007 - The Human Pseudoautosomal Region]]"
---

# Meiosis

> [!abstract]
> Meiosis is the pair of cell divisions that turns one diploid cell into four haploid cells: homologous chromosomes pair, swap segments and are pulled apart, which is exactly why alleles segregate and assort as Mendel observed.

## Definition

**Meiosis** is the specialized cell division that produces haploid cells, such as gametes, from a diploid cell: one round of DNA replication is followed by two successive divisions. **Meiosis I** separates homologous chromosomes and halves the chromosome number (the reduction division); **meiosis II** separates sister chromatids, as mitosis does. During prophase I, homologs pair and exchange segments by **crossing over**.[^os11][^alberts-m][^cooper]

## Why it matters

- **Mendel's laws are meiosis.** Segregation and independent assortment are the behavior of chromosomes at meiosis I, so every expected genotype ratio, pedigree risk and trio consistency check rests on it ([[Mendelian Inheritance]], [[Trio Analysis]]).[^os-u3]
- **Crossovers make haplotypes.** Each gamete transmits, for each chromosome, a mosaic of the parent's two homologs. The chance of a crossover between two loci measures their genetic distance, and the reshuffling repeated over generations shapes [[Linkage Disequilibrium]], on which association studies and imputation rely ([[Genetic Recombination]], [[Genetic Linkage]], [[Haplotype]]).
- **Meiotic errors show up in genomes.** Nondisjunction yields gametes with an extra or a missing chromosome, and trisomy 21 is a viable result.[^os13] Such aneuploidies appear as whole-chromosome copy-number changes ([[Copy Number Variation]]), and markers near the centromere tell in which parent and which division the error happened (Exercise 2).
- **X and Y pair only at their tips.** In male meiosis, X and Y pair and recombine in the pseudoautosomal regions; deletion of PAR1 prevents X-Y pairing and causes male sterility.[^mangs] Loci there are inherited like autosomal loci and need diploid genotype calls in males ([[Sex-Linked Inheritance]], [[Ploidy]]).

## Core (L1)

![[meiosis-stages.svg]]

In humans: one diploid cell with 46 chromosomes replicates its DNA once (92 chromatids, 4C), meiosis I gives two cells with 23 replicated chromosomes (2C), and meiosis II four cells with 23 single-chromatid chromosomes (1C).

**Meiosis I**, the reduction division:[^os11][^alberts-m]

1. **Prophase I.** Chromosomes condense, and each pair of homologs comes together along its whole length (**synapsis**), held by a protein scaffold, the **synaptonemal complex**. A paired set of homologs is a **bivalent**, or tetrad, since it has four chromatids. Non-sister chromatids exchange segments (**crossing over**); the points of exchange become visible as **chiasmata** when the homologs start to separate.
2. **Metaphase I.** Bivalents line up at the metaphase plate, the two homologs of each pair facing opposite poles. Which homolog faces which pole is random, independently for each bivalent.
3. **Anaphase I.** Homologs separate and move to opposite poles; sister chromatids stay joined at their centromeres.
4. **Telophase I and cytokinesis.** Two cells form, each with one homolog of every pair: haploid, although each chromosome still has two chromatids.

**Meiosis II**, with no DNA replication before it: chromosomes line up individually with sister kinetochores facing opposite poles, as in mitosis; sisters separate at anaphase II, and four haploid cells result, each with one chromatid of every chromosome.[^os11][^alberts-m]

**From meiosis to Mendel**, the chromosomal theory of inheritance:[^os-u3][^os11]

| What Mendel saw | What the chromosomes do |
|---|---|
| The two alleles of a gene go to different gametes, 1:1 (segregation) | Homologs, which carry the two alleles at the same locus, separate at anaphase I |
| Genes on different chromosomes are transmitted independently (independent assortment) | Each bivalent orients at random at metaphase I, independently of the others |
| Genes close together on one chromosome usually travel together | They are on one chromosome; only a crossover between them separates them |

**Three sources of new combinations.** Independent assortment gives $2^n$ combinations of maternal and paternal homologs per gamete with $n$ pairs, $2^{23} = 8{,}388{,}608$ in humans; crossing over creates new combinations of alleles within each chromosome;[^os11] random fertilization of two independent gametes gives $(2^{23})^2 \approx 7.0 \times 10^{13}$ chromosome combinations, before counting crossovers.

**Mitosis versus meiosis.**[^os11][^alberts-m]

| | [[Mitosis]] | Meiosis |
|---|---|---|
| Divisions after one replication | 1 | 2 |
| Products | 2 cells, same ploidy as the parent, genetically identical | 4 haploid cells, genetically different |
| Homolog pairing | no: chromosomes line up individually | yes, prophase I |
| Crossing over | not a regular step | yes, prophase I |
| Separated at anaphase | sister chromatids | homologs (I), then sisters (II) |

## Deeper (L2)

**Prophase I, step by step.** Classical cytology divides prophase I into five stages: **leptotene** (chromosomes condense as thin threads), **zygotene** (synapsis begins), **pachytene** (synapsis complete; crossing over), **diplotene** (the synaptonemal complex disassembles and the homologs stay linked at the chiasmata) and **diakinesis** (further condensation, then metaphase I).[^alberts-m]

**Crossovers start as deliberate DNA breaks.** Meiotic recombination starts with double-strand breaks made on purpose in the chromosomes; the broken ends use the homolog as a template for repair. A break can be repaired with a crossover, which exchanges the flanking chromosome arms, or without one, sometimes leaving a short tract of **gene conversion** ([[Genetic Recombination]], [[DNA Repair]]).[^alberts-recomb]

**Why homologs, not sisters, separate first.** Three features distinguish meiosis I from mitosis: chiasmata physically link the homologs of each bivalent until anaphase I; the two sister kinetochores of each homolog attach to the same pole, so the homologs, not the sisters, are pulled apart; and cohesion between sister arms is released at anaphase I, which frees the chiasmata, while cohesion at the centromeres persists until anaphase II.[^alberts-m] A homolog pair without a crossover lacks the physical link and risks going to one pole.[^alberts-m] The X-Y pair shows the stakes: its pairing depends on PAR1, and without PAR1 X and Y cannot pair.[^mangs]

**Nondisjunction.** If homologs fail to separate at anaphase I, or sisters at anaphase II, gametes receive an extra or a missing chromosome, and fertilization gives a trisomy or a monosomy. Most aneuploidies are lethal to the embryo; trisomy 21 is a viable exception ([[Chromosome#Deeper (L2)]]).[^os13] An error in meiosis I gives four abnormal gametes, an error in meiosis II two normal and two abnormal ones (Exercise 2).

**Two sexes, two schedules.** In males each meiosis yields four sperm. In females the divisions are asymmetric: one large egg and small polar bodies that degenerate. Human oocytes enter meiosis before birth and stay arrested in prophase I for years, until ovulation.[^alberts-g]

## Advanced (L3)

- **Why the recombination fraction never exceeds 1/2.** A crossover involves two of the four chromatids. One crossover between two loci therefore yields two recombinant and two parental products, and with more crossovers the expected share stays one half (Computational representation). This is the cellular reason why distant loci on one chromosome look unlinked ([[Genetic Linkage]]).
- **Crossovers as a point process.** Modeling crossovers as a Poisson process along the chromosome ([[Poisson Process]]) gives Haldane's map function between the recombination fraction and map distance. Real crossovers are more evenly spaced than Poisson points, a property called interference,[^griffiths] which Exercise 4 pushes to its extreme.
- **Inheritance in sequencing data.** Each transmitted chromosome is a mosaic of the parent's two haplotypes, switching at crossovers. In trio data the switch points appear as changes in which parental haplotype the child carries (Exercise 5); over many generations crossovers erode the associations between nearby alleles ([[Haplotype Phasing]], [[Linkage Disequilibrium]]).
- **Outside meiosis.** Mitochondria are passed on through the cytoplasm, not shared out by meiosis, so mitochondrial genes do not follow Mendel's laws ([[Mitochondrial DNA]]).[^alberts14]

## Mathematical representation

- **Gametes without crossing over.** Write the diploid genome as pairs $(M_i, P_i)$, $i = 1, \dots, n$, of maternal and paternal homologs. A gamete is $G = (X_1, \dots, X_n)$ with independent $X_i \in \{M_i, P_i\}$, each value with probability 1/2. The $2^n$ gametes are equally likely; for humans ($n = 23$), $P(G = (M_1, \dots, M_{23})) = 2^{-23} \approx 1.2 \times 10^{-7}$.
- **Recombination fraction.** For two loci on one chromosome, let $N$ be the number of crossovers between them on the bivalent, and assume each crossover joins one random chromatid of each homolog, independently of the others. A given chromatid takes part in each crossover with probability 1/2, so it undergoes $\mathrm{Binomial}(N, 1/2)$ exchanges between the loci, and it is recombinant when that number is odd, which has probability exactly 1/2 whenever $N \ge 1$. Hence the recombination fraction is
$$r = \tfrac12\, P(N \ge 1) \le \tfrac12.$$
- **Haldane's map function.** Let the map distance $d$ (in Morgans) be the expected number of crossovers per chromatid between the loci; since each crossover involves two of the four chromatids, $E[N] = 2d$. If crossovers form a Poisson process, $P(N \ge 1) = 1 - e^{-2d}$ and
$$r = \tfrac12\left(1 - e^{-2d}\right), \qquad d = -\tfrac12 \ln(1 - 2r).$$
For small $d$, $r \approx d$: 1 centimorgan (0.01 Morgan) corresponds to a recombination fraction of 1 %.[^griffiths]
- **Complete interference.** If every bivalent of map length $1/2$ Morgan has exactly one crossover at a uniform position, then $P(N \ge 1) = 2d$ and $r = d$ for $d \le 1/2$: a linear map, the opposite extreme to Haldane's.

## Computational representation

A meiosis can be simulated chromatid by chromatid: four chromatids per bivalent, each crossover exchanging the segments to the right of a point between one maternal and one paternal chromatid. Each product records, locus by locus, whether its allele is maternal (M) or paternal (P).

```python
import random
from collections import Counter


def tetrad(crossovers: list[tuple[float, int, int]], loci: list[float]) -> list[str]:
    """Four products of one meiosis. Chromatids 0, 1 are maternal, 2, 3 paternal; a crossover
    (x, i, j) exchanges everything right of position x between chromatids i and j."""
    chromatids = [["M"] * len(loci), ["M"] * len(loci), ["P"] * len(loci), ["P"] * len(loci)]
    for x, i, j in sorted(crossovers):
        for k, position in enumerate(loci):
            if position > x:
                chromatids[i][k], chromatids[j][k] = chromatids[j][k], chromatids[i][k]
    return ["".join(c) for c in chromatids]


def random_crossovers(length: float, rng: random.Random) -> list[tuple[float, int, int]]:
    """Poisson crossovers, rate 2 per Morgan on the bivalent, random non-sister pair each."""
    events, x = [], rng.expovariate(2.0)
    while x < length:
        events.append((x, rng.choice((0, 1)), rng.choice((2, 3))))
        x += rng.expovariate(2.0)
    return events


loci = [0.1, 0.4]                      # loci A and B, positions in Morgans (invented)
cases = {
    "no crossover": [],
    "one crossover": [(0.25, 1, 2)],
    "two, same two chromatids": [(0.2, 1, 2), (0.3, 1, 2)],
    "two, three chromatids": [(0.2, 1, 2), (0.3, 0, 2)],
    "two, three chromatids (bis)": [(0.2, 1, 2), (0.3, 1, 3)],
    "two, four chromatids": [(0.2, 1, 2), (0.3, 0, 3)],
}
for name, crossovers in cases.items():
    products = tetrad(crossovers, loci)
    print(f"{name:28} {products}  recombinant {sum(p[0] != p[1] for p in products)}/4")

rng = random.Random(1)                 # two loci on different chromosomes: independent assortment
counts = Counter()
for _ in range(10_000):
    first = rng.choice(tetrad(random_crossovers(1.0, rng), [0.5]))
    second = rng.choice(tetrad(random_crossovers(1.0, rng), [0.5]))
    counts[first + second] += 1
print(sorted(counts.items()))
```

```text
no crossover                 ['MM', 'MM', 'PP', 'PP']  recombinant 0/4
one crossover                ['MM', 'MP', 'PM', 'PP']  recombinant 2/4
two, same two chromatids     ['MM', 'MM', 'PP', 'PP']  recombinant 0/4
two, three chromatids        ['MM', 'MP', 'PM', 'PP']  recombinant 2/4
two, three chromatids (bis)  ['MM', 'MP', 'PM', 'PP']  recombinant 2/4
two, four chromatids         ['MP', 'MP', 'PM', 'PM']  recombinant 4/4
[('MM', 2485), ('MP', 2572), ('PM', 2488), ('PP', 2455)]
```

The four ways of placing two crossovers are equally likely and give 0, 2, 2 and 4 recombinant products: on average 2 of 4, the 1/2 of the Mathematical representation. Loci on different chromosomes give the four combinations in equal proportions (within sampling error), which is independent assortment.

## Worked example

> [!example] Two genes, two arrangements
> A diploid individual is heterozygous `A`/`a` and `B`/`b`.
> 1. **Genes on different chromosomes.** At metaphase I, the bivalent carrying `A`/`a` and the one carrying `B`/`b` orient independently. Half of the meioses put `A` and `B` on the same side and yield gametes `AB` and `ab`; the other half yield `Ab` and `aB`. Overall: 1/4 each, the basis of 9:3:3:1 ([[Mendelian Inheritance]]).
> 2. **Genes on one chromosome**, `A` and `B` on the maternal homolog, `a` and `b` on the paternal one. A meiosis without a crossover between them gives only parental gametes, `AB` and `ab`. A meiosis with one crossover between them gives `AB`, `Ab`, `aB`, `ab`: two parental, two recombinant.
> 3. **Recombination fraction.** If one crossover falls between the genes in 30 % of meioses and none in the rest (invented numbers), $r = 0.30 \times 2/4 = 0.15$: 15 % recombinant gametes, a map distance of about 15 centimorgans.

## Common misconceptions

> [!warning] "Meiosis I separates sister chromatids, as mitosis does"
> Meiosis I separates homologs; sisters separate only at meiosis II.[^os11]

> [!warning] "Crossing over happens between sister chromatids"
> It happens between non-sister chromatids of homologous chromosomes.[^os11] Sisters are identical copies, so exchanging segments between them would create no new combination.

> [!warning] "A gamete carries either the maternal or the paternal set"
> Each homolog pair is shared out independently, so a human gamete carries an all-maternal set with probability $2^{-23}$, about 1 in 8.4 million, and crossovers make each chromosome itself a mixture.

## Exercises

> [!question] Exercise 1 (L1)
> An invented species has $2n = 8$. Give the number of bivalents in prophase I, and the numbers of chromosomes and chromatids per cell at metaphase I, after telophase I, at metaphase II and in a gamete. How many gamete combinations are possible without crossing over?

> [!success]- Solution
> 4 bivalents. Metaphase I: 8 chromosomes, 16 chromatids. After telophase I: 4 chromosomes, 8 chromatids per cell. Metaphase II: 4 and 8. Gamete: 4 and 4. Combinations: $2^4 = 16$.

> [!question] Exercise 2 (L2)
> (a) List the chromosome content of the four gametes when one chromosome pair fails to separate at meiosis I, then at meiosis II (in one of the two cells). (b) For a marker next to the centromere of chromosome 21, the mother is 1/2 and the father 3/4. A trisomic child is 1/2/3, another 1/1/4. In which parent and which division did each error occur? Assume no crossover between the marker and the centromere.

> [!success]- Solution
> (a) Meiosis I: $n + 1$, $n + 1$, $n - 1$, $n - 1$: all four abnormal. Meiosis II: $n + 1$, $n - 1$, $n$, $n$: two normal. (b) Child 1/2/3: both maternal alleles, so both maternal homologs were transmitted: maternal error at meiosis I. Child 1/1/4: two copies of one maternal allele, so two sister chromatids were transmitted: maternal error at meiosis II. Because centromere-linked markers do not recombine away from the centromere, they follow homologs and sisters faithfully.

> [!question] Exercise 3 (L2)
> (a) If exactly one crossover falls between loci A and B in 30 % of meioses and none in the others, what is $r$? (b) Under Haldane's map function, which map distance gives $r = 0.3$? (c) Why do two loci 150 cM apart look unlinked?

> [!success]- Solution
> (a) $r = \frac12 \times 0.3 = 0.15$. (b) $d = -\frac12 \ln(1 - 0.6) \approx 0.458$ Morgan, about 46 cM, more than the naive 30 cM because some crossovers are hidden by double exchanges. (c) $r = \frac12(1 - e^{-3}) \approx 0.475$, almost indistinguishable from the 0.5 of independent assortment.

> [!question] Exercise 4 (L3, Python)
> Using `tetrad` and `random_crossovers` from the code above, estimate $r$ for $d$ = 0.05, 0.2, 0.5, 1 and 2 Morgans and compare with Haldane's function. Then simulate complete interference, one crossover per bivalent of map length 0.5 Morgan, and compare $r$ with $d$.

> [!success]- Solution
> ```python
> import math
> import random
>
> rng = random.Random(2)
> n = 20_000
> for d in (0.05, 0.2, 0.5, 1.0, 2.0):
>     rec = sum(len(set(rng.choice(tetrad(random_crossovers(d + 0.1, rng), [0.0, d])))) == 2 for _ in range(n))
>     print(f"d = {d:4}: simulated r = {rec / n:.3f}, Haldane {0.5 * (1 - math.exp(-2 * d)):.3f}")
>
>
> def one_crossover(length, rng):     # complete interference: exactly one crossover per bivalent
>     return [(rng.uniform(0, length), rng.choice((0, 1)), rng.choice((2, 3)))]
>
>
> r_one = {d: round(sum(len(set(rng.choice(tetrad(one_crossover(0.5, rng), [0.0, d])))) == 2
>                       for _ in range(n)) / n, 3) for d in (0.05, 0.2, 0.4)}
> print("one crossover per 0.5-Morgan bivalent:", r_one)
> ```
> ```text
> d = 0.05: simulated r = 0.048, Haldane 0.048
> d =  0.2: simulated r = 0.166, Haldane 0.165
> d =  0.5: simulated r = 0.321, Haldane 0.316
> d =  1.0: simulated r = 0.437, Haldane 0.432
> d =  2.0: simulated r = 0.489, Haldane 0.491
> one crossover per 0.5-Morgan bivalent: {0.05: 0.051, 0.2: 0.204, 0.4: 0.398}
> ```
> Without interference, $r$ follows Haldane's curve and saturates at 0.5, because double crossovers hide each other. With complete interference no double crossover occurs, and $r = d$. Real chromosomes lie between the two, which is why mapping software offers several map functions ([[Genetic Linkage]]).

> [!question] Exercise 5 (L3, Python)
> In an invented trio, the mother's two haplotypes are phased (known from her own parents), the father and child are genotyped as alternative-allele counts. Using only sites where the father is homozygous and the mother heterozygous, find which maternal haplotype the child inherited along the chromosome, and locate the maternal crossover.

> [!success]- Solution
> ```python
> positions = [1, 4, 9, 13, 18, 22, 27, 31, 36, 40, 45, 49]      # Mb, invented
> mother_h1 = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]                # mother's phased haplotypes
> mother_h2 = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1]
> father = [0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 2]                   # alt-allele counts (unphased)
> child = [0, 2, 1, 0, 1, 2, 0, 0, 1, 1, 1, 2]
>
> origin = []                                                     # (position, maternal haplotype)
> for pos, h1, h2, f, c in zip(positions, mother_h1, mother_h2, father, child):
>     if f == 1 or h1 == h2:
>         continue                    # father heterozygous or mother homozygous: uninformative
>     maternal = c - f // 2           # child's allele from the mother
>     origin.append((pos, "h1" if maternal == h1 else "h2"))
> print(origin)
> for (p1, o1), (p2, o2) in zip(origin, origin[1:]):
>     if o1 != o2:
>         print(f"maternal crossover between {p1} and {p2} Mb")
> ```
> ```text
> [(1, 'h1'), (4, 'h1'), (13, 'h1'), (22, 'h1'), (27, 'h1'), (31, 'h2'), (36, 'h2'), (40, 'h2'), (49, 'h2')]
> maternal crossover between 27 and 31 Mb
> ```
> A homozygous father transmits a known allele, so the child's other allele is maternal; where the mother is heterozygous, it identifies her haplotype. The child received `h1` up to 27 Mb and `h2` from 31 Mb: one crossover in the maternal meiosis, located only to the interval between informative sites. A single switch between distant sites is a crossover; isolated switches at single sites would point to genotyping errors instead ([[Haplotype Phasing]], [[Trio Analysis]]).

## Mastery checklist

- [ ] 1 Recognized: I can name the stages of meiosis I and II and define synapsis, bivalent, chiasma and nondisjunction.
- [ ] 2 Understood: I can map segregation, independent assortment and linkage onto anaphase I, metaphase I and crossing over.
- [ ] 3 Practiced: I can count chromosomes through meiosis, derive $r \le 1/2$ and Haldane's function, and simulate tetrads.
- [ ] 4 Applied: I located crossovers in a real trio, or compared recombination fractions with a published genetic map.
- [ ] 5 Explained: I can teach why homologs separate first, how meiotic errors are traced to a parent and a division, and how interference changes map functions.

## References

[^os11]: [[Biology 2e (OpenStax)]], section 11.1 "The Process of Meiosis" (meiosis I and II, synapsis, the synaptonemal complex, tetrads, chiasmata and crossover between non-sister chromatids, random alignment at metaphase I, comparison with mitosis).
[^os-u3]: [[Biology 2e (OpenStax)]], Unit 3 "Genetics" (meiosis and the chromosomal theory of inheritance).
[^os13]: [[Biology 2e (OpenStax)]], section 13.2 "Chromosomal Basis of Inherited Disorders" (nondisjunction, aneuploidy, trisomy 21).
[^alberts-m]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), section "Meiosis" (homolog pairing and the synaptonemal complex, the stages of prophase I, chiasmata, sister kinetochores attached to the same pole in meiosis I, release of arm cohesion at anaphase I and of centromeric cohesion at anaphase II).
[^alberts-recomb]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of general recombination (meiotic recombination initiated by double-strand breaks, crossing over and gene conversion).
[^alberts-g]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of eggs and sperm (asymmetric meiotic divisions and polar bodies, the long arrest of oocytes in prophase I, four sperm per meiosis).
[^alberts14]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 14 "Energy Conversion: Mitochondria and Chloroplasts" (cytoplasmic, non-Mendelian inheritance of mitochondrial genes).
[^cooper]: [[The Cell (Cooper)]], 2nd ed. (2000), section "Meiosis and Fertilization" (meiosis as a specialized cell cycle that halves the chromosome number and produces haploid cells).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), transmission genetics: crossing over, map units, mapping functions and interference.
[^mangs]: [[Mangs 2007 - The Human Pseudoautosomal Region]], *Current Genomics* 8(2):129-136.
