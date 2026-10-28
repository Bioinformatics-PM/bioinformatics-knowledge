---
aliases:
  - Linkage
  - Gene Linkage
  - Linkage Map
  - Genetic Map
  - Centimorgan
  - Map Unit
  - LOD Score
  - Linkage Analysis
  - Liaison génétique
  - Carte génétique
tags:
  - type/concept
  - domain/biology
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Genetic Recombination]]"
  - "[[Mendelian Inheritance]]"
  - "[[Meiosis]]"
  - "[[Chromosome]]"
  - "[[Independence (Probability)]]"
related:
  - "[[Linkage Disequilibrium]]"
  - "[[Haplotype]]"
  - "[[Pedigree Analysis]]"
  - "[[Quantitative Trait Locus]]"
  - "[[Genome-Wide Association Study]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Likelihood Ratio Test]]"
  - "[[Poisson Process]]"
  - "[[Genomic Coordinate System]]"
  - "[[Sex-Linked Inheritance]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Sturtevant 1913 - The Linear Arrangement of Six Sex-Linked Factors in Drosophila]]"
  - "[[Morton 1955 - Sequential Tests for the Detection of Linkage]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
  - "[[Baudat 2010 - PRDM9 Is a Major Determinant of Meiotic Recombination Hotspots in Humans and Mice]]"
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
---

# Genetic Linkage

> [!abstract]
> Genes close together on one chromosome travel together through meiosis and so break Mendel's law of independent assortment; how often they are separated measures how far apart they are, which is how genetic maps in centimorgans are built.

## Definition

Two loci are **linked** when they lie on the same chromosome, close enough that gametes keep their parental allele combinations more often than independent assortment predicts: their [[Genetic Recombination|recombination frequency]] $r$ is below 1/2.[^os13][^griffiths] A **genetic map**, or linkage map, orders loci along a chromosome and spaces them by recombination: one **map unit**, or **centimorgan** (cM), corresponds to 1 % recombination between close loci.[^os13] Alfred Sturtevant drew the first map in 1913 from six sex-linked factors of *Drosophila*, showing that genes lie in a linear order along the chromosome.[^sturtevant][^os13]

## Why it matters

- **Genetic maps were the first genome coordinates.** Loci were ordered by recombination long before sequencing. Today genetic positions (cM) sit beside physical positions (bp), and the two are not proportional, because recombination rates vary along chromosomes ([[Genomic Coordinate System]]).[^lander]
- **Linkage analysis locates disease genes** by following a disease and genetic markers through families ([[Pedigree Analysis]], [[Genetic Disease]]); its statistic, the LOD score, was devised for human family data.[^morton]
- **A linked marker stands in for an unknown gene.** A marker that co-segregates with a trait points to the region holding the causal locus: the logic of [[Quantitative Trait Locus]] mapping in crosses and, through [[Linkage Disequilibrium]] in populations, of the [[Genome-Wide Association Study]].
- **Co-segregation is clinical evidence.** Whether a candidate variant co-segregates with the disease in a family is one of the evidence types used to classify variants in Mendelian disease genes ([[Variant Classification]]).[^richards]
- **It is a likelihood problem.** Estimating $r$, testing $r < 1/2$ and pooling families are textbook [[Maximum Likelihood Estimation]] and [[Likelihood Ratio Test|likelihood ratio testing]].

## Core (L2)

### Linked genes break independent assortment

A double heterozygote in coupling (`AB/ab`) makes each parental gamete with probability $\frac{1-r}{2}$ and each recombinant gamete with probability $\frac{r}{2}$ ([[Genetic Recombination#Mathematical representation]]). Independent assortment is the special case $r = 1/2$, where all four gametes have probability $\frac14$. Below 1/2, parental combinations dominate and the ratios of [[Mendelian Inheritance]] no longer hold.[^os13] Selfing `AB/ab` (same $r$ in both sexes) gives the double recessive with probability $x = \left(\frac{1-r}{2}\right)^2$; since each gene alone still segregates 3:1, the four phenotype classes have probabilities $\frac12 + x$, $\frac14 - x$, $\frac14 - x$ and $x$ (Exercise 2):

| Phenotype | Independent, $r = 1/2$ | Linked, $r = 0.1$ |
|---|---:|---:|
| `A_ B_` | 0.5625 (9/16) | 0.7025 |
| `A_ bb` | 0.1875 (3/16) | 0.0475 |
| `aa B_` | 0.1875 (3/16) | 0.0475 |
| `aa bb` | 0.0625 (1/16) | 0.2025 |

### From recombination frequencies to a map

Sturtevant treated recombination frequency as a distance, assuming that genes lie in a fixed linear order and that crossovers can occur anywhere along the chromosome with equal likelihood.[^os13][^sturtevant]

1. **Measure pairwise frequencies** with test crosses ([[Genetic Recombination#Measuring r with a test cross]]).
2. **Order the loci.** For three loci, the pair with the largest frequency are the outer ones. Invented example: $r_{AB} = 0.08$, $r_{BC} = 0.12$, $r_{AC} = 0.19$ gives the order A-B-C.
3. **Add short intervals.** 1 % recombination is 1 cM for short intervals, and distances add: $d_{AC} = 8 + 12 = 20$ cM, while the direct measure $r_{AC}$ is only 19 %, because double crossovers between A and C are invisible to A and C. Maps are built by summing short intervals.[^os13][^griffiths]
4. **Beware the 50 % ceiling.** Loci far apart on one chromosome give $r$ close to 1/2, like loci on different chromosomes, so a single frequency near 1/2 cannot tell the two cases apart.[^os13] A chromosome's map can be much longer than 50 cM: its length is the sum of its intervals.

### The three-point test cross

Crossing a triple heterozygote with a triple recessive gives the order, both intervals and the double crossovers in one experiment.[^griffiths][^os13]

1. The two most frequent classes are **parental**; the two rarest are **double crossovers** (DCO).
2. Compared with the parental classes, a DCO class has swapped only the allele of the **middle** locus.
3. Each interval's recombination frequency counts its single crossovers **plus** the double crossovers.
4. Fewer DCOs than the product of the two frequencies predicts reveals **interference**: the **coefficient of coincidence** is $c = \text{observed DCO} / \text{expected DCO}$ and the interference is $I = 1 - c$.[^griffiths]

The Worked example applies the four steps; its result is this map:

```text
A ------------ 11.8 cM ------------ C -------- 8.4 cM -------- B
0 cM                               11.8 cM                    20.2 cM
```

## Advanced (L3)

### Map functions

Measured frequencies stop adding up over long intervals because double crossovers hide. A **map function** converts $r$ into an additive distance $d$, the expected number of crossovers per chromatid in the interval, in Morgans (1 M = 100 cM) ([[Meiosis#Mathematical representation]]). If crossovers fall independently along the chromosome, as a [[Poisson Process|Poisson process]] without interference, the result is **Haldane's map function**:[^griffiths]

$$r = \tfrac12\left(1 - e^{-2d}\right), \qquad d = -\tfrac12 \ln(1 - 2r).$$

![[map-function-haldane.svg]]

For small $d$, $r \approx d$; as $d$ grows, $r$ tends to 1/2. Interference spaces crossovers more evenly, which moves real data from Haldane's curve toward the line $r = d$. In the three-point example ($c = 0.40$), Haldane applied to $r_{AB} = 0.194$ gives 24.6 cM, more than the 20.2 cM obtained by adding the intervals, because it assumes more hidden double crossovers than occurred. Choose the map function to match the organism's interference, or add short intervals.

### LOD scores: linkage in human families

Human crosses cannot be designed and families are small, so evidence is accumulated across families with likelihoods. For a recombination fraction $\theta$, the **LOD score** (logarithm of the odds) of the family data is

$$Z(\theta) = \log_{10} \frac{L(\theta)}{L(1/2)},$$

the base-10 logarithm of how much more probable the data are under linkage at $\theta$ than under free recombination. Scores of independent families add, and Morton introduced the criterion $Z \ge 3$, odds of 1000 to 1, for declaring linkage.[^morton] Two cases cover most hand calculations:

- **Phase known** (the parent's haplotypes are known, for example from the grandparents): with $k$ recombinants among $n$ informative meioses, $L(\theta) = \theta^k (1 - \theta)^{n-k}$. Ten meioses without a recombinant give $Z(0) = 10 \log_{10} 2 = 3.01$.
- **Phase unknown**: average over the two possible phases, $L(\theta) = \frac12\left[\theta^k(1-\theta)^{n-k} + \theta^{n-k}(1-\theta)^k\right]$, which costs up to $\log_{10} 2 \approx 0.30$ LOD units per family.

The threshold is far stricter than $p < 0.05$ because most marker positions are not linked to the disease locus: a declared linkage should be probably true, not just unlikely under the null (Exercise 6, [[Multiple Testing Correction]]).

### Linkage and linkage disequilibrium

| | Linkage | [[Linkage Disequilibrium]] |
|---|---|---|
| Property of | Two **loci** | Two **alleles** in a population |
| Data | Meioses in families or crosses | Haplotypes of unrelated individuals |
| Detectable range | Tens of cM: few meioses, few crossovers | Short: associations decay as $(1 - r)^t$ over many generations |
| Main use | Map building, family studies | Association studies, imputation |

Linked loci can be in linkage equilibrium in a population, and LD can appear between unlinked loci, for example when two populations mix, although it then halves every generation.[^hartl]

## Frontier (M1)

- **Dense maps as hidden Markov models.** With thousands of markers per chromosome, the grandparental origin transmitted in each meiosis can be modelled as a hidden state that switches at crossovers, with switch probabilities between neighbouring markers given by a map function: a [[Hidden Markov Model]] along the chromosome, which lets all markers be used jointly instead of pair by pair ([[Haplotype Phasing]]).
- **Maps are not universal.** Hotspot usage depends on PRDM9 alleles, so maps estimated in different populations or individuals differ in fine detail.[^baudat]
- **From linkage peak to variant.** With few meioses, a linkage peak spans many megabases. In families with a rare disease, sequencing now finds the candidate variants, and co-segregation with the disease weighs in their classification.[^richards]

## Mathematical representation

- Loci $1, \dots, m$ in map order; $r_{ij}$ is the recombination fraction and $d_{ij}$ the map distance (Morgans) between $i$ and $j$.
- **Distances add, frequencies do not.** For $i < j < k$: $d_{ik} = d_{ij} + d_{jk}$, but $r_{ik} = r_{ij} + r_{jk} - 2\,r_{ijk}$, where $r_{ijk}$ is the probability that a product is recombinant in both intervals (such a product is parental for $i$ and $k$).
- **Interference.** Without interference $r_{ijk} = r_{ij}\, r_{jk}$; in general $c = r_{ijk} / (r_{ij} r_{jk})$ and $I = 1 - c$.
- **Haldane.** $r = \frac12(1 - e^{-2d})$; additivity of $d$ then gives $1 - 2r_{ik} = (1 - 2r_{ij})(1 - 2r_{jk})$, which is the no-interference case $r_{ijk} = r_{ij} r_{jk}$ above.
- **Likelihood.** Phase known: $\ell(\theta) = k \ln\theta + (n - k)\ln(1 - \theta)$, maximized at $\hat\theta = k/n$ ([[Maximum Likelihood Estimation]]). In both phase cases $L(1/2) = 2^{-n}$, so $Z(\theta) = \log_{10} L(\theta) + n \log_{10} 2$. The likelihood ratio statistic for $H_0: \theta = 1/2$ is $2 \ln(10)\, Z(\hat\theta) \approx 4.6\, Z(\hat\theta)$ ([[Likelihood Ratio Test]]): a LOD of 3 corresponds to a statistic of 13.8.

## Computational representation

A three-point cross is a table of eight counts; the analysis only needs to find the parental and double-crossover classes and count recombinants pair by pair. Map functions and LOD scores are one-line formulas.

```python
import math


def differing(u: str, v: str) -> list[int]:
    return [i for i in range(len(u)) if u[i] != v[i]]


def three_point(counts: dict[str, int], loci: str) -> dict:
    """Analyse a three-point test cross. Keys are the gametes of the triple heterozygote,
    one letter per locus in the order of `loci` (upper case = dominant allele)."""
    n = sum(counts.values())
    ranked = sorted(counts, key=counts.get, reverse=True)
    parental, dco = ranked[:2], ranked[-2:]                  # most and least frequent classes
    p = next(p for p in parental if len(differing(dco[0], p)) == 1)
    middle = differing(dco[0], p)[0]                         # the locus a DCO swaps
    left, right = [i for i in range(3) if i != middle]

    def rf(i: int, j: int) -> float:                         # recombinant for loci i and j
        return sum(c for g, c in counts.items()
                   if all((g[i], g[j]) != (q[i], q[j]) for q in parental)) / n

    r1, r2 = rf(left, middle), rf(middle, right)
    coincidence = sum(counts[g] for g in dco) / n / (r1 * r2)
    return {"order": loci[left] + "-" + loci[middle] + "-" + loci[right],
            "r1": r1, "r2": r2, "r_outer": rf(left, right),
            "map_cM": (0, round(100 * r1, 1), round(100 * (r1 + r2), 1)),
            "coincidence": round(coincidence, 3), "interference": round(1 - coincidence, 3)}


def haldane_cm(r: float) -> float:
    """Map distance in cM from a recombination fraction, assuming no interference."""
    return -50 * math.log(1 - 2 * r)


def lod(theta: float, n: int, k: int, phase_known: bool = True) -> float:
    """LOD score for k recombinants among n informative meioses, at recombination fraction theta."""
    like = theta ** k * (1 - theta) ** (n - k)
    if not phase_known:                                      # average over the two phases
        like = 0.5 * (like + theta ** (n - k) * (1 - theta) ** k)
    return math.log10(like / 0.5 ** n)


cross = {"ABc": 404, "abC": 398, "AbC": 58, "aBc": 56,       # invented test-cross counts
         "Abc": 39, "aBC": 41, "ABC": 2, "abc": 2}
print(three_point(cross, "ABC"))
print(round(haldane_cm(0.194), 1), round(haldane_cm(0.118) + haldane_cm(0.084), 1))
print(round(lod(0.0, 10, 0), 2), round(lod(0.1, 10, 1), 2), round(lod(0.1, 10, 1, phase_known=False), 2))
```

```text
{'order': 'A-C-B', 'r1': 0.118, 'r2': 0.084, 'r_outer': 0.194, 'map_cM': (0, 11.8, 20.2), 'coincidence': 0.404, 'interference': 0.596}
24.6 22.7
3.01 1.6 1.3
```

The same A-B interval measures 19.4 cM directly, 20.2 cM as a sum of intervals, 22.7 cM as a sum of Haldane-corrected intervals and 24.6 cM with Haldane on the direct value: the choice of method matters once intervals are long. Ten phase-known meioses without a recombinant reach LOD 3.01; one recombinant drops the maximum to 1.60, or 1.30 with unknown phase.

## Worked example

> [!example] A three-point test cross (invented counts)
> A triple heterozygote is test-crossed with `abc/abc`. The 1,000 offspring are classified by the gamete received from the heterozygote, loci written in the order A, B, C:
>
> | Classes | Counts | Type |
> |---|---:|---|
> | `ABc`, `abC` | 404, 398 | parental (most frequent) |
> | `AbC`, `aBc` | 58, 56 | single crossover |
> | `Abc`, `aBC` | 39, 41 | single crossover |
> | `ABC`, `abc` | 2, 2 | double crossover (rarest) |
>
> 1. **Middle locus.** `ABC` differs from the parental `ABc` only at C, so C is in the middle: the order is A-C-B.
> 2. **Interval A-C.** Recombinant for A and C: `AbC`, `aBc` and the DCOs, $r_{AC} = (58 + 56 + 2 + 2)/1000 = 0.118$.
> 3. **Interval C-B.** `Abc`, `aBC` and the DCOs, $r_{CB} = (39 + 41 + 4)/1000 = 0.084$.
> 4. **Map.** A at 0, C at 11.8 cM, B at 20.2 cM. The direct A-B frequency, $(58 + 56 + 39 + 41)/1000 = 0.194$, is lower by twice the DCO fraction ($2 \times 0.004$).
> 5. **Interference.** Without interference, $0.118 \times 0.084 \times 1000 = 9.9$ DCOs are expected; 4 are observed: $c = 0.40$ and $I = 0.60$. A crossover in one interval cut the chance of one in the other by 60 %.

## Common misconceptions

> [!warning] "Linked genes are always inherited together"
> They are inherited together more often than chance predicts, not always: linked loci give recombinants at frequency $r$, anywhere from 0 to almost 1/2.[^os13]

> [!warning] "A recombination frequency of 50 % means the genes are on different chromosomes"
> Loci far apart on one chromosome also give $r \approx 1/2$.[^os13] Only a chain of shorter intervals, or physical positions in an assembly, places them.

> [!warning] "Map distances cannot exceed 50 cM"
> That holds for recombination frequencies, not for map distance, which is an expected number of crossovers: it adds over intervals and exceeds 50 cM on long chromosomes. Only short intervals have $d \approx r$.

> [!warning] "Linkage and linkage disequilibrium are the same thing"
> Linkage concerns loci and meioses observed in families; linkage disequilibrium concerns alleles in a population. Linked loci can be in equilibrium, and unlinked loci can briefly show disequilibrium.[^hartl]

## Exercises

> [!question] Exercise 1 (L2)
> Pairwise test crosses give $r_{DE} = 0.21$, $r_{EF} = 0.06$ and $r_{DF} = 0.16$ (invented). Order the loci, draw the map, and explain why $r_{DE}$ is smaller than the sum of the two intervals.

> [!success]- Solution
> The largest frequency, $r_{DE}$, joins the outer loci: the order is D-F-E, with D at 0, F at 16 cM and E at 22 cM. The direct $r_{DE} = 0.21 < 0.22$ because a double crossover between D and E leaves D and E in their parental combination; adding the short intervals counts those crossovers.

> [!question] Exercise 2 (L2)
> Prove that selfing a coupling double heterozygote `AB/ab`, with recombination fraction $r$ in both sexes, gives the phenotype classes $\frac12 + x$, $\frac14 - x$, $\frac14 - x$, $x$ with $x = \left(\frac{1-r}{2}\right)^2$. Give the expected counts among 400 offspring for $r = 0.2$ and compare with 9:3:3:1.

> [!success]- Solution
> A double recessive needs an `ab` gamete from each parent: probability $x$. Each gene alone still segregates 3:1, so the class `bb` has probability $\frac14$, split between `aa bb` ($x$) and `A_ bb` ($\frac14 - x$); likewise `aa B_` has $\frac14 - x$, and `A_ B_` takes the rest, $1 - \frac14 - \frac14 + x = \frac12 + x$. For $r = 0.2$, $x = 0.16$: 264 : 36 : 36 : 64 out of 400, against 225 : 75 : 75 : 25 for independent genes. The parental phenotypes (`A_ B_` and `aa bb`) are in excess.

> [!question] Exercise 3 (L2)
> Two loci give $r = 0.48$ (standard error 0.025) in a test cross. Can you conclude that they are on different chromosomes? What would settle it?

> [!success]- Solution
> No: the value is compatible with $r = 1/2$, which unlinked loci and distant loci on one chromosome both produce. Mapping each locus against intermediate markers (a chain of short, additive intervals), or their physical positions in a genome assembly, settles it.

> [!question] Exercise 4 (L3, Python)
> Using `three_point`, analyse this invented test cross of a `PQR` triple heterozygote (2,000 offspring): `pQR` 745, `Pqr` 735, `PQr` 152, `pqR` 148, `pQr` 96, `PqR` 104, `PQR` 9, `pqr` 11. Give the order, the map and the interference.

> [!success]- Solution
> ```python
> cross2 = {"pQR": 745, "Pqr": 735, "PQr": 152, "pqR": 148,
>           "pQr": 96, "PqR": 104, "PQR": 9, "pqr": 11}
> print(three_point(cross2, "PQR"))
> # {'order': 'Q-P-R', 'r1': 0.16, 'r2': 0.11, 'r_outer': 0.25, 'map_cM': (0, 16.0, 27.0), 'coincidence': 0.568, 'interference': 0.432}
> ```
>
> P is in the middle: the DCO `PQR` differs from the parental `pQR` only at P. Map: Q at 0, P at 16 cM, R at 27 cM. Expected DCOs $0.16 \times 0.11 \times 2000 = 35.2$, observed 20: $c = 0.57$, $I = 0.43$.

> [!question] Exercise 5 (L3, Python)
> A father of unknown phase has 8 informative children, one of them recombinant under the better phase. Using `lod`, find $\hat\theta$ and the maximum LOD on a grid of $\theta$ values, compare with the phase-known case, and estimate how many such families would reach $Z = 3$.

> [!success]- Solution
> ```python
> grid = [i / 1000 for i in range(1, 501)]
> best = max(grid, key=lambda t: lod(t, 8, 1, phase_known=False))
> z = lod(best, 8, 1, phase_known=False)
> print(best, round(z, 3), math.ceil(3 / z))   # 0.125 0.798 4
> print(round(lod(best, 8, 1), 3))             # 1.099
> ```
>
> $\hat\theta = 1/8$, with a maximum LOD of 0.80 for unknown phase against 1.10 for known phase: the unknown phase costs $\log_{10} 2 = 0.30$. Four such families at a common $\theta$ give $4 \times 0.80 = 3.2$, enough for Morton's criterion. This is why linkage studies pool families, and why typing grandparents to fix the phase is worth it.

> [!question] Exercise 6 (M1)
> Suppose (hypothetically) that before the study, the probability that a given marker is linked to the disease locus is 0.02. Treating the maximized likelihood ratio as a simple likelihood ratio, compute the posterior probability of linkage after a LOD of 3, and after a likelihood ratio of only 20. What does this say about the LOD 3 criterion?

> [!success]- Solution
> Posterior odds = prior odds x likelihood ratio ([[Bayes' Theorem]]). Prior odds: $0.02/0.98 = 0.0204$. LOD 3 (ratio 1000): posterior odds 20.4, probability 0.95. Ratio 20: posterior odds 0.41, probability 0.29. With a low prior, only strong evidence makes a declared linkage probably true: the LOD 3 criterion protects the reliability of positive findings, the same concern as the false discovery rate in genome-wide testing ([[Multiple Testing Correction]]). Maximizing over $\theta$ inflates the ratio, so these probabilities are optimistic.

## Mastery checklist

- [ ] 1 Recognized: I can define linkage, a genetic map and the centimorgan.
- [ ] 2 Understood: I can explain why linked genes break independent assortment, why only short intervals add, and how linkage differs from linkage disequilibrium.
- [ ] 3 Practiced: I can solve two-point and three-point crosses by hand and in Python, convert with Haldane's function and compute LOD scores.
- [ ] 4 Applied: I plotted genetic (cM) against physical (bp) positions along a real chromosome from a published genetic map, or computed LOD scores on a real family dataset.
- [ ] 5 Explained: I can teach map functions, interference, the LOD 3 criterion and the move from family linkage to population association.

## References

[^os13]: [[Biology 2e (OpenStax)]], ch. 13 "Modern Understandings of Inheritance", section 13.1 "Chromosomal Theory and Genetic Linkage" (linkage, recombination frequencies from 0 to 0.5, Sturtevant's map and its assumptions, map units in centimorgans, additivity and the three-point test cross).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), chromosome mapping by recombination: linkage, map units, three-point test crosses, interference and the coefficient of coincidence, mapping functions.
[^sturtevant]: [[Sturtevant 1913 - The Linear Arrangement of Six Sex-Linked Factors in Drosophila]], *Journal of Experimental Zoology* 14:43-59.
[^morton]: [[Morton 1955 - Sequential Tests for the Detection of Linkage]], *American Journal of Human Genetics* 7(3):277-318.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), linkage disequilibrium: its origins and its decay by recombination.
[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]], *Nature* 409:860-921, key findings on recombination rates along chromosomes.
[^baudat]: [[Baudat 2010 - PRDM9 Is a Major Determinant of Meiotic Recombination Hotspots in Humans and Mice]], *Science* 327:836-840.
[^richards]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], *Genetics in Medicine* 17(5):405-424, segregation evidence.
