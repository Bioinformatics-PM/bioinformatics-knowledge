---
aliases:
  - Mendel's Laws
  - Mendelian Genetics
  - Law of Segregation
  - Law of Independent Assortment
  - Hérédité mendélienne
  - Lois de Mendel
tags:
  - type/concept
  - domain/biology
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Meiosis]]"
  - "[[Allele]]"
  - "[[Genotype]]"
  - "[[Phenotype]]"
  - "[[Probability]]"
related:
  - "[[Gene]]"
  - "[[Dominance]]"
  - "[[Sex-Linked Inheritance]]"
  - "[[Genetic Linkage]]"
  - "[[Genetic Recombination]]"
  - "[[Epistasis]]"
  - "[[Pedigree Analysis]]"
  - "[[Chi-Square Test]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Trio Analysis]]"
projects: []
sources:
  - "[[Mendel 1866 - Experiments in Plant Hybridization]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
---

# Mendelian Inheritance

> [!abstract]
> Each parent passes on one of its two copies of a gene, chosen at random, and different genes are passed on independently: these two rules predict the 3:1 and 9:3:3:1 ratios of Mendel's peas, and a chi-square test checks real counts against them.

## Definition

**Mendelian inheritance** is the transmission of genes according to Mendel's two laws.[^os12][^mendel]

1. **Law of segregation**: a diploid individual carries two alleles of each gene; they separate when gametes form, so each gamete receives one of them, each with probability 1/2.
2. **Law of independent assortment**: alleles of different genes are distributed to gametes independently of each other.

The laws hold for nuclear genes on non-homologous chromosomes (or far apart on one chromosome); [[Genetic Linkage]], [[Sex-Linked Inheritance]] and organelle genes depart from them.[^os12-3][^alberts] Observed offspring counts are compared with the predicted ratio by a **chi-square goodness-of-fit test**.[^stats]

## Why it matters

- **Genotype data obey segregation.** A VCF genotype (`0/0`, `0/1`, `1/1`) is an allele count at one site; a child's genotype must combine one allele from each parent. Trio pipelines flag violations as **Mendelian errors**: genotyping errors, sample swaps or real [[Mutation|de novo mutations]] ([[Trio Analysis]], [[Mutation Rate]]).
- **Risk calculations are products and sums of probabilities.** Carrier and recurrence risks in [[Pedigree Analysis]] and [[Genetic Disease]] use exactly the rules below.
- **Departures carry information.** Too many parental combinations mean [[Genetic Linkage]], the basis of genetic maps, [[Haplotype|haplotypes]] and association studies; modified ratios reveal [[Epistasis]].
- **The same goodness-of-fit logic** tests genotype counts against [[Hardy-Weinberg Equilibrium]] proportions; see [[Chi-Square Test]] for the general theory.

## Core (L1)

### Mendel's experiment

Mendel worked with the garden pea, *Pisum sativum*, which normally self-fertilizes and can be crossed by hand. He used **true-breeding** varieties that differed in single characters (seed shape, seed colour, flower colour...), crossed them (the P generation), and let the hybrids (F1) self-fertilize to give the F2.[^os12] The F1 all showed one form, which he called **dominant**; the other form, **recessive**, reappeared in about a quarter of the F2.[^os12][^mendel]

| Character (F2) | Dominant | Recessive | Ratio |
|---|---:|---:|---:|
| Seed shape: round / wrinkled | 5,474 | 1,850 | 2.96 : 1 |
| Seed colour: yellow / green | 6,022 | 2,001 | 3.01 : 1 |
| Flower colour: violet / white | 705 | 224 | 3.15 : 1 |

(Mendel's counts.[^mendel][^os12]) His explanation: each plant carries two hereditary "elements" per character, gametes carry one, and fertilization pairs them at random. His work was largely ignored until it was rediscovered around 1900.[^os12]

### Segregation and the Punnett square

An `Rr` plant makes `R` and `r` gametes in equal numbers. Crossing two of them, every egg-sperm pair is equally likely:

```text
            sperm R    sperm r
egg R         RR         Rr
egg r         Rr         rr
```

Genotypes 1 `RR` : 2 `Rr` : 1 `rr`; with `R` dominant, phenotypes 3 round : 1 wrinkled. The ratio is a probability for each offspring, not a guarantee for each family of four.

**Test cross.** To find whether a round plant is `RR` or `Rr`, cross it with a recessive homozygote `rr`: all offspring round means `RR`; about half wrinkled means `Rr`.[^os12]

### Independent assortment: the dihybrid cross

Crossing round-yellow (`RRYY`) with wrinkled-green (`rryy`) gives `RrYy` hybrids. Each makes four gamete types (`RY`, `Ry`, `rY`, `ry`) with probability 1/4 each, and the F2 shows **9 : 3 : 3 : 1**. Mendel counted 315 round yellow, 108 round green, 101 wrinkled yellow and 32 wrinkled green.[^mendel]

![[dihybrid-punnett-square.svg]]

### Probability rules

- **Product rule**: the probability that independent events all happen is the product of their probabilities.
- **Sum rule**: the probability that one of several mutually exclusive events happens is the sum of their probabilities.[^os12]

So $P(\texttt{rryy}) = \frac14 \times \frac14 = \frac1{16}$, and a round F2 plant is `RR` or `Rr` with probability $\frac14 + \frac12 = \frac34$. With many genes, apply the rule gene by gene instead of drawing a 64-cell square.

### Testing a ratio: chi-square

Is 5,474 : 1,850 compatible with 3:1?[^stats]

1. **Null hypothesis**: the true ratio is 3:1.
2. **Expected counts**: $n = 7{,}324$, so $E = (5{,}493,\ 1{,}831)$.
3. **Statistic**: $X^2 = \sum \frac{(O - E)^2}{E} = \frac{19^2}{5493} + \frac{19^2}{1831} = 0.263$.
4. **Degrees of freedom**: $k - 1 = 1$ for $k = 2$ classes.
5. **Decision**: the 5 % critical value for 1 df is 3.841; $0.263 < 3.841$ ($p = 0.61$), so the data give no evidence against 3:1.

The approximation needs every expected count to be at least 5.[^stats]

## Deeper (L2)

### Why the laws hold: meiosis

Mendel's laws are the behaviour of chromosomes in [[Meiosis]].[^os-u3] **Segregation** is the separation of homologous chromosomes at anaphase I: the two alleles of a gene sit at the same locus on the two homologs. **Independent assortment** is the random orientation of each homologous pair at metaphase I, independent of the other pairs. It therefore fails for genes close together on the same chromosome, which travel together unless crossing over separates them ([[Genetic Recombination]], [[Genetic Linkage]]).[^os12-3]

### Many genes at once

For an F1 heterozygous at $n$ independently assorting genes, crossed with an identical F1: $2^n$ gamete types, $3^n$ genotypes, $2^n$ phenotype classes under complete dominance, a fraction $(3/4)^n$ showing every dominant trait, and a phenotype ratio given by the expansion of $(3 + 1)^n$: 3:1, then 9:3:3:1, then 27:9:9:9:3:3:3:1.

### Ratios that tell a story

| Observed pattern | Likely cause | Note |
|---|---|---|
| 1:2:1 phenotypes in an F2 | heterozygote distinguishable | [[Dominance]] (incomplete or codominance)[^os12] |
| 2:1 instead of 3:1 | one homozygous class dies | lethal allele[^griffiths] |
| 9:3:4, 9:7, 12:3:1, 15:1 | two genes act on one trait | [[Epistasis]][^griffiths][^os12-3] |
| excess of parental combinations | genes close on one chromosome | [[Genetic Linkage]][^os12-3] |
| different ratios in sons and daughters | gene on the X chromosome | [[Sex-Linked Inheritance]][^os12] |
| trait passed only through the mother | organelle genome | [[Mitochondrial DNA]][^alberts] |

A significant chi-square says the model is wrong, not which row of this table applies; and since $X^2$ grows with sample size for the same proportions (Exercise 3), always test counts, never percentages.

## Advanced (L3)

- **Mendelian consistency in sequencing data.** At a biallelic site, only 15 of the 27 possible (mother, father, child) genotype combinations are consistent with segregation (Exercise 4). Real de novo mutations are rare, about $1.2 \times 10^{-8}$ per nucleotide per generation in humans,[^kong] so a call set with many inconsistent sites is mostly reporting errors, and their rate is a natural quality metric. The rare real ones are de novo mutations or deletions (a heterozygous deletion in a parent can make a child look homozygous). This check is basic to [[Trio Analysis]].
- **Transmission reveals phase.** If a child is `0/1`, the mother `0/0` and the father `1/1`, the child's `1` came from the father: family genotypes resolve which alleles travel together on one chromosome, a principle used by [[Haplotype Phasing]].
- **Segregation as a likelihood model.** Replacing "independent assortment" by a recombination fraction $r$ between two loci turns the model into a likelihood $L(r)$; maximizing it and comparing with $r = 1/2$ gives the LOD score of linkage analysis ([[Maximum Likelihood Estimation]], [[Genetic Linkage]]).
- **Too good a fit is also a signal.** A $p$-value near 1 for every experiment is itself improbable; Exercise 5 computes how often data would fit Mendel's ratios as closely as his did.

## Mathematical representation

- A genotype at a biallelic locus is an **allele count** $g \in \{0, 1, 2\}$ (copies of the alternative allele).
- **Segregation**: a parent with count $g$ transmits the alternative allele with probability $g/2$. The child's count is $C = X_m + X_f$ with independent $X_m \sim \mathrm{Bernoulli}(g_m/2)$ and $X_f \sim \mathrm{Bernoulli}(g_f/2)$. For $g_m = g_f = 1$: $P(C = 0, 1, 2) = (\frac14, \frac12, \frac14)$.
- **Independent assortment**: for loci $1, \dots, n$, the gamete distribution factorizes, $P(A_1 = a_1, \dots, A_n = a_n) = \prod_{i=1}^{n} P(A_i = a_i)$, where $A_i$ is the allele transmitted at locus $i$.
- **Counts**: $n$ offspring in $k$ classes with predicted probabilities $p_1, \dots, p_k$ give counts $(N_1, \dots, N_k) \sim \mathrm{Multinomial}(n; p_1, \dots, p_k)$ ([[Multinomial Distribution]]).
- **Pearson statistic**: $X^2 = \sum_{i=1}^{k} \frac{(N_i - E_i)^2}{E_i}$ with $E_i = n p_i$. Under $H_0$ and large $E_i$, $X^2$ approximately follows a [[Chi-Square Distribution]] with $k - 1$ degrees of freedom.[^stats]
- **Two classes**: with $p = p_1$, $X^2 = \frac{(N_1 - np)^2}{np} + \frac{(N_1 - np)^2}{n(1-p)} = \left(\frac{N_1 - np}{\sqrt{np(1-p)}}\right)^2 = Z^2$, the square of the standardized [[Binomial Distribution|binomial]] count: the 1-df chi-square test is the two-sided normal approximation to a binomial test.

## Computational representation

Genotypes are strings of allele pairs (`AaBb`) in teaching code and allele counts (0, 1, 2) in real data (the `GT` field of [[VCF Format]]). Enumerating gamete pairs implements both laws directly; the chi-square tail probability needs only the incomplete gamma function.

```python
import math
from collections import Counter
from itertools import product


def gametes(genotype: str) -> list[str]:
    """Equally likely gametes of a multi-gene genotype: 'AaBb' -> ['AB', 'Ab', 'aB', 'ab']."""
    pairs = [genotype[i:i + 2] for i in range(0, len(genotype), 2)]
    return ["".join(alleles) for alleles in product(*pairs)]


def cross(parent1: str, parent2: str) -> Counter:
    """Offspring genotype counts over all equally likely gamete pairs."""
    offspring = Counter()
    for g1, g2 in product(gametes(parent1), gametes(parent2)):
        offspring["".join("".join(sorted(a + b)) for a, b in zip(g1, g2))] += 1
    return offspring


def phenotype(genotype: str) -> str:
    """Complete dominance: a gene shows its uppercase form if at least one uppercase allele."""
    return "".join(genotype[i] if genotype[i].isupper() else genotype[i + 1]
                   for i in range(0, len(genotype), 2))


def chi2_sf(x: float, df: int) -> float:
    """P(X >= x) for X ~ chi-square(df), via the series of the lower incomplete gamma function."""
    a, z = df / 2, x / 2
    if z <= 0:
        return 1.0
    term = total = 1 / a
    k = 0
    while term > 1e-17 * total:
        k += 1
        term *= z / (a + k)
        total += term
    return 1 - total * math.exp(a * math.log(z) - z - math.lgamma(a))


def chi_square_test(observed: list[int], ratio: list[int]) -> tuple[float, int, float]:
    """Pearson goodness of fit of counts to a fully specified ratio: (X2, df, p)."""
    n, parts = sum(observed), sum(ratio)
    expected = [n * r / parts for r in ratio]
    x2 = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    return x2, len(observed) - 1, chi2_sf(x2, len(observed) - 1)


f2 = cross("RrYy", "RrYy")
print(len(f2), "genotypes:", dict(sorted(f2.items())))
print(Counter(phenotype(g) for g in f2.elements()).most_common())
for name, obs, ratio in [("seed shape", [5474, 1850], [3, 1]),
                         ("dihybrid", [315, 108, 101, 32], [9, 3, 3, 1])]:
    x2, df, p = chi_square_test(obs, ratio)          # Mendel's counts
    print(f"{name}: X2 = {x2:.3f}, df = {df}, p = {p:.3f}")
```

```text
9 genotypes: {'RRYY': 1, 'RRYy': 2, 'RRyy': 1, 'RrYY': 2, 'RrYy': 4, 'Rryy': 2, 'rrYY': 1, 'rrYy': 2, 'rryy': 1}
[('RY', 9), ('Ry', 3), ('rY', 3), ('ry', 1)]
seed shape: X2 = 0.263, df = 1, p = 0.608
dihybrid: X2 = 0.470, df = 3, p = 0.925
```

Enumeration costs $4^n$ gamete pairs for $n$ genes: fine for teaching, but real tools work locus by locus with the product rule. The series in `chi2_sf` loses relative precision for very small $p$ (below about $10^{-12}$); report such values as "$p < 10^{-10}$".

## Worked example

> [!example] Mendel's dihybrid counts against 9:3:3:1
> Observed: 315 round yellow, 108 round green, 101 wrinkled yellow, 32 wrinkled green; $n = 556$.[^mendel]
>
> | Class | $O$ | $E = 556 \times p$ | $(O - E)^2 / E$ |
> |---|---:|---:|---:|
> | round yellow (9/16) | 315 | 312.75 | 0.016 |
> | round green (3/16) | 108 | 104.25 | 0.135 |
> | wrinkled yellow (3/16) | 101 | 104.25 | 0.101 |
> | wrinkled green (1/16) | 32 | 34.75 | 0.218 |
> | total | 556 | 556 | **0.470** |
>
> 1. $k = 4$ classes, so 3 degrees of freedom; the 5 % critical value is 7.815.
> 2. $0.470 \ll 7.815$, $p = 0.925$: the counts fit 9:3:3:1.
> 3. **Each gene alone**: shape 423 round : 133 wrinkled ($X^2 = 0.345$, $p = 0.56$), colour 416 yellow : 140 green ($X^2 = 0.010$, $p = 0.92$). Both fit 3:1, so segregation holds for each gene; the joint fit to 9:3:3:1 adds that the two genes assort independently.

## Common misconceptions

> [!warning] "A 3:1 ratio means three of every four children show the dominant trait"
> The ratio is a probability per offspring. In a family of four children of two `Rr` parents, all four are dominant with probability $(3/4)^4 \approx 0.32$, and exactly three with probability $4 \times (3/4)^3 \times (1/4) \approx 0.42$.

> [!warning] "The chi-square test proved the 3:1 ratio"
> A large $p$ only means the data are compatible with the hypothesis. Other ratios may be compatible too, especially with small samples (Exercise 3); and testing thousands of markers produces some significant departures by chance alone ([[Multiple Testing Correction]]).

> [!warning] "Any two genes assort independently"
> Only genes on different chromosomes, or far apart on one. Close genes are linked and break the second law.[^os12-3]

## Exercises

> [!question] Exercise 1 (L1)
> In peas, tall (`T`) is dominant over dwarf (`t`). (a) Give the genotype and phenotype ratios of `Tt` x `Tt`. (b) A tall plant crossed with a dwarf plant gives 48 tall and 52 dwarf offspring. What is the tall parent's genotype?

> [!success]- Solution
> (a) Genotypes 1 `TT` : 2 `Tt` : 1 `tt`; phenotypes 3 tall : 1 dwarf. (b) This is a test cross. About half dwarf means the tall parent passed on `t` half the time: it is `Tt`. A `TT` parent would give only tall offspring.

> [!question] Exercise 2 (L1)
> For `AaBbCc` x `AaBbCc`, with independent genes and complete dominance, compute (a) $P(\texttt{aabbcc})$, (b) the probability of showing all three dominant traits, (c) the probability of being heterozygous at all three genes.

> [!success]- Solution
> Use the product rule gene by gene. (a) $(1/4)^3 = 1/64$. (b) $(3/4)^3 = 27/64 \approx 0.42$. (c) $(1/2)^3 = 1/8$.

> [!question] Exercise 3 (L2)
> A test cross should give 1:1. Experiment A gives 58 : 42, experiment B (same proportions, twice as many offspring) gives 116 : 84. Test both at $\alpha = 0.05$ and explain the difference.

> [!success]- Solution
> A: expected 50 : 50, $X^2 = 8^2/50 + 8^2/50 = 2.56 < 3.841$ ($p = 0.11$), not rejected. B: expected 100 : 100, $X^2 = 16^2/100 \times 2 = 5.12 > 3.841$ ($p = 0.024$), rejected. Same proportions, but $X^2$ scales with $n$: B has enough offspring to detect a 58 % : 42 % imbalance, A does not. The test answers "is this departure larger than chance at this sample size?", not "how large is the departure?".

> [!question] Exercise 4 (L3, Python)
> Genotypes are coded as allele counts 0, 1, 2. Write `possible_children(mother, father)`, count how many of the 27 (mother, father, child) combinations are consistent with segregation, and flag the inconsistent sites of this invented trio: site1 (0, 1, 1), site2 (1, 1, 2), site3 (0, 0, 1), site4 (2, 2, 1), site5 (2, 0, 1), site6 (1, 2, 0).

> [!success]- Solution
> ```python
> from itertools import product
>
>
> def possible_children(mother: int, father: int) -> set[int]:
>     """Alt-allele counts (0, 1, 2) a child can inherit, given the parents' counts."""
>     transmit = {0: {0}, 1: {0, 1}, 2: {1}}           # alleles a parent can pass on
>     return {m + f for m in transmit[mother] for f in transmit[father]}
>
>
> consistent = sum(c in possible_children(m, f) for m, f, c in product(range(3), repeat=3))
> print(consistent, "of 27 genotype trios are consistent")
>
> trio = {"site1": (0, 1, 1), "site2": (1, 1, 2), "site3": (0, 0, 1),   # invented sites:
>         "site4": (2, 2, 1), "site5": (2, 0, 1), "site6": (1, 2, 0)}   # (mother, father, child)
> print([site for site, (m, f, c) in trio.items() if c not in possible_children(m, f)])
> # 15 of 27 genotype trios are consistent
> # ['site3', 'site4', 'site6']
> ```
>
> Site3: two `0/0` parents cannot have a `0/1` child (candidate de novo mutation, or a missed parental allele). Site4: two `1/1` parents must have a `1/1` child. Site6: a `1/1` father always transmits `1`, so the child cannot be `0/0` (error, or a deletion of the father's allele). Each flagged site needs checking in the reads before any biological claim.

> [!question] Exercise 5 (L3, Python)
> (a) Mendel's four experiments above are independent. Add their $X^2$ values and degrees of freedom and compute $P(X^2_{\text{total}} \le \text{observed})$, the probability of a fit at least this good if the ratios are true. (b) An invented test cross `AaBb` x `aabb` gives 245 `AB`, 55 `Ab`, 60 `aB`, 240 `ab` (parental gametes `AB` and `ab`). Test 1:1:1:1 and interpret.

> [!success]- Solution
> Reusing `chi_square_test` and `chi2_sf`:
>
> ```python
> counts = {"seed shape": ([5474, 1850], [3, 1]), "seed colour": ([6022, 2001], [3, 1]),
>           "flower colour": ([705, 224], [3, 1]), "dihybrid": ([315, 108, 101, 32], [9, 3, 3, 1])}
> tests = [chi_square_test(obs, ratio) for obs, ratio in counts.values()]
> x2_total, df_total = sum(t[0] for t in tests), sum(t[1] for t in tests)
> print(round(x2_total, 3), df_total, round(1 - chi2_sf(x2_total, df_total), 3))
>
> x2, df, p = chi_square_test([245, 55, 60, 240], [1, 1, 1, 1])      # invented test cross
> print(round(x2, 1), df, p < 1e-10, round((55 + 60) / 600, 3))
> # 1.139 6 0.02
> # 228.3 3 True 0.192
> ```
>
> (a) Summed $X^2 = 1.139$ on 6 df: only about 2 % of repetitions would fit this well. That is not proof of anything, but a fit much closer than sampling noise predicts deserves the same scrutiny as a bad fit. (b) $X^2 = 228.3$ on 3 df, $p < 10^{-10}$: independent assortment is rejected. The parental classes dominate and the recombinant classes make up $115/600 = 0.19$ of the offspring: the genes are linked, about 19 map units apart ([[Genetic Linkage]]).

## Mastery checklist

- [ ] 1 Recognized: I can state the laws of segregation and independent assortment and the 3:1 and 9:3:3:1 ratios.
- [ ] 2 Understood: I can explain both laws through meiosis, use the product and sum rules, and say when independent assortment fails.
- [ ] 3 Practiced: I can run a chi-square test by hand and in Python, and enumerate crosses of several genes.
- [ ] 4 Applied: I checked Mendelian consistency in a real trio VCF and could explain the inconsistent sites.
- [ ] 5 Explained: I can teach how sample size, linkage, lethality and epistasis change ratios and test results, and what "too good a fit" means.

## References

[^mendel]: [[Mendel 1866 - Experiments in Plant Hybridization]], experiments on seed shape, seed colour and flower colour, and the combination of two characters (English translation on MendelWeb).
[^os12]: [[Biology 2e (OpenStax)]], ch. 12 "Mendel's Experiments and Heredity" (Mendel's crosses, probability rules, test cross, alternatives to dominance, sex-linked traits).
[^os12-3]: [[Biology 2e (OpenStax)]], ch. 12, section "Laws of Inheritance" (segregation, independent assortment, linked genes, epistasis).
[^os-u3]: [[Biology 2e (OpenStax)]], Unit 3 "Genetics" (meiosis and the chromosomal theory of inheritance).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), transmission genetics: lethal alleles and modified dihybrid ratios.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), on the non-Mendelian, maternal inheritance of organelle genes.
[^stats]: [[Introductory Statistics (OpenStax)]], chapter "The Chi-Square Distribution" (goodness-of-fit test and its expected-count condition).
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], Kong A et al., *Nature* 488:471-475.
