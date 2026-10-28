---
aliases:
  - Gene Interaction
  - Genetic Interaction
  - Epistatic Interaction
  - Modified Mendelian Ratio
  - Épistasie
tags:
  - type/concept
  - domain/biology
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Mendelian Inheritance]]"
  - "[[Dominance]]"
  - "[[Gene]]"
  - "[[Phenotype]]"
  - "[[Chi-Square Test]]"
related:
  - "[[Genetic Screen]]"
  - "[[Biological Pathway]]"
  - "[[Metabolic Pathway]]"
  - "[[Interaction Effect]]"
  - "[[Linear Regression]]"
  - "[[Fitness]]"
  - "[[Genetic Disease]]"
  - "[[Heritability]]"
  - "[[Genome-Wide Association Study]]"
  - "[[Biological Network]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Beadle 1941 - Genetic Control of Biochemical Reactions in Neurospora]]"
  - "[[Phillips 2008 - Epistasis, the Essential Role of Gene Interactions]]"
  - "[[Evolution (Futuyma)]]"
  - "[[Introductory Statistics (OpenStax)]]"
---

# Epistasis

> [!abstract]
> Epistasis is when the effect of one gene depends on the alleles at another gene; when two genes act on one trait, it turns Mendel's 9:3:3:1 into ratios such as 9:3:4, 9:7, 12:3:1 or 15:1, whose merged classes reveal how the genes work together.

## Definition

**Epistasis** is an interaction between genes in which the alleles at one locus mask or modify the phenotypic effect of the alleles at another locus. The masking gene is **epistatic**, the masked one **hypostatic**.[^os12][^griffiths] It is an interaction between loci, whereas [[Dominance]] relates the alleles of one locus. The word has a second, statistical meaning: any departure of multilocus genotype values from the sum of the separate effects of each locus.[^phillips]

## Why it matters

- **Ordering genes in pathways.** The phenotype of a double mutant tells which gene acts first; classical genetics ordered biochemical and developmental pathways this way, and the same logic interprets the mutants of a [[Genetic Screen]] ([[Biological Pathway]]).[^griffiths][^beadle]
- **Modifier genes** change the penetrance and expressivity of disease alleles ([[Genetic Disease]]).[^griffiths]
- **Interaction terms in data analysis.** Statistical epistasis is an [[Interaction Effect]] in a [[Linear Regression]], and testing all pairs of variants in a [[Genome-Wide Association Study]] multiplies the number of tests ([[Multiple Testing Correction]]).
- **Evolution.** The fitness effect of an allele can depend on the alleles at other loci ([[Fitness]]).[^futuyma]

## Core (L2)

### Recognizing epistasis from ratios

In a dihybrid cross `AaBb` x `AaBb` with independent assortment, the four classes `A_B_`, `A_bb`, `aaB_`, `aabb` occur as 9:3:3:1 ([[Mendelian Inheritance]]). If both genes act on the **same** trait, some classes look alike and their numbers add up: the ratio still sums to 16, but it has fewer than four classes.[^griffiths][^os12]

![[epistasis-modified-ratios.svg]]

| F2 ratio | Classes that look alike | Interaction | Pathway reading |
|---|---|---|---|
| 9:3:4 | `aaB_` = `aabb` | Recessive epistasis: `aa` masks B | A acts upstream of B |
| 9:7 | `A_bb` = `aaB_` = `aabb` | Complementary genes: a dominant allele of both is needed | Two steps in series |
| 12:3:1 | `A_B_` = `A_bb` | Dominant epistasis: `A_` masks B | A dominant allele overrides B |
| 15:1 | all classes but `aabb` | Duplicate genes: a dominant allele of either suffices | Two redundant routes |
| 13:3 | all classes but `aaB_` | Dominant suppression: `A_` cancels the effect of `B_` | A suppressor of B |

**A real case: mouse coat colour.** The agouti gene gives banded hairs (`A`, dominant) or solid colour (`aa`). A second gene, C, is needed to make pigment at all: `cc` mice are albino whatever their agouti genotype, so C is epistatic to A.[^os12] Crossing two `AaCc` mice therefore gives 9 agouti (`A_C_`), 3 solid (`aaC_`) and 4 albino (`A_cc` and `aacc`): 9:3:4.

### Why the ratios arise: pathways

Genes control the steps of biochemical pathways (Beadle and Tatum's one gene, one enzyme), so the structure of a pathway predicts the ratio.[^beadle][^griffiths]

```mermaid
flowchart LR
    P["Precursor<br/>(colourless)"] -->|"enzyme made by gene A"| I["Intermediate"]
    I -->|"enzyme made by gene B"| F["Final pigment"]
```

- **The intermediate looks like the precursor.** A block at either step gives the same colourless phenotype; only `A_B_` makes pigment: **9:7**.
- **The intermediate has its own colour.** `aa` blocks the first step and nothing reaches B, so B's genotype is invisible in `aa` individuals: **9:3:4**, with the upstream gene epistatic.
- **Two redundant enzymes for one step.** Either one works, and only `aabb` lacks the product: **15:1**.

### Confirming the interpretation

A ratio is a hypothesis, checked in two ways. A chi-square goodness-of-fit test compares the counts with the candidate ratios that have the same number of classes, provided every expected count is at least 5 ([[Chi-Square Test]]).[^stats] A **test cross** of the F1 with `aabb` gives the four classes in equal parts, merged as in the F2: 1:1:2 for 9:3:4, 1:3 for 9:7, 2:1:1 for 12:3:1 and 3:1 for 15:1 (Exercise 2).

## Advanced (L3)

### Three meanings of epistasis

The word is used in three senses, which Phillips's review separates:[^phillips]

| Sense | Question | Measured on |
|---|---|---|
| Functional | Do the gene products interact, physically or in one pathway? | Molecules |
| Compositional | Does an allele substitution at one locus have different effects in different genetic backgrounds, as in the masking of one mutant by another (Bateson's sense)? | Defined genotypes |
| Statistical | Do genotype values depart from the sum of separate locus effects, averaged over a population (Fisher's sense)? | Populations, with their allele frequencies |

The senses do not imply each other. Statistical epistasis depends on allele frequencies, so a complete masking interaction can leave almost all the genetic variance attributable to the separate effects of single loci (Exercise 5).[^phillips]

### Measuring interaction quantitatively

For quantitative traits and fitness, epistasis is the departure of a double mutant from a null model built from the single mutants. With fitnesses relative to the wild type ($W = 1$):

- **Multiplicative null model**: $\varepsilon = W_{ab} - W_a W_b$, natural for growth and fitness, where independent effects multiply; it is the additive model on the log scale.
- **Additive null model**: $\varepsilon_{\text{add}} = W_{ab} - (W_a + W_b - 1)$.
- **Negative interaction** ($\varepsilon < 0$): the double mutant is worse than expected. The extreme is **synthetic lethality**: two viable single mutants whose combination is lethal, the expected outcome for redundant genes (the 15:1 logic applied to viability).
- **Positive interaction** ($\varepsilon > 0$): the second mutation hurts less than expected, as when both genes act in one pathway that the first mutation has already broken.

Whether an interaction exists depends on the scale and on the null model (Mathematical representation, Exercise 4).

### Epistasis in population data

In a regression of a trait on two variants coded 0, 1, 2,

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12}\, x_1 x_2 + \varepsilon,$$

statistical epistasis is a non-zero $\beta_{12}$ ([[Interaction Effect]]). Genome-wide, $m$ variants give $m(m - 1)/2$ pairs: about $5 \times 10^{11}$ for $10^6$ variants, hence a Bonferroni threshold near $0.05 / (5 \times 10^{11}) = 10^{-13}$, and little power for small interaction effects ([[Multiple Testing Correction]]).

## Frontier (M1)

- **One quantitative framework.** With high-throughput functional genomics and systems approaches, gene interactions are measured at scale, and Phillips argues for treating their functional, compositional and statistical aspects together.[^phillips] Double-mutant screens extend the [[Genetic Screen]] from single genes to pairs, and their interaction scores can be analysed as a [[Biological Network]].
- **Association studies and gene action.** Population studies mostly estimate separate locus effects; the variance-partition argument of Exercise 5 shows that this says little about whether the genes act independently.[^phillips]

## Mathematical representation

- **Dihybrid classes.** With independent loci, $P(\text{at least one } A) = 3/4$ and $P(aa) = 1/4$, likewise for B, and a class probability is the product of its two parts: 9/16, 3/16, 3/16, 1/16.
- **A two-gene trait** is a function $\varphi$ from the four classes to phenotypes. Its F2 distribution is $P(\varphi = z) = \sum_{c\,:\,\varphi(c) = z} P(c)$: a modified ratio is a merge of $\{9, 3, 3, 1\}$. In a test cross every class has probability 1/4, so the test-cross ratio is the same merge of $\{1, 1, 1, 1\}$.
- **Quantitative traits.** For genotype $i$ at locus 1 and $j$ at locus 2, $y_{ij} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij}$; epistasis means $(\alpha\beta)_{ij} \neq 0$ for some $i, j$ ([[Analysis of Variance]]). With Hardy-Weinberg proportions and independent loci, the interaction variance is $V_I = E\left[(y - E[y \mid g_1] - E[y \mid g_2] + \mu)^2\right]$, where $g_1, g_2$ are the genotypes and $\mu = E[y]$.
- **Scale.** If $W_{ab} = W_a W_b$, then $\log W_{ab} = \log W_a + \log W_b$: no interaction on the log scale, yet $\varepsilon_{\text{add}} = W_a W_b - W_a - W_b + 1 = (1 - W_a)(1 - W_b) > 0$ on the linear scale.

## Computational representation

Enumerating the 16 gamete pairs and mapping each class to a phenotype reproduces any modified ratio; a chi-square fit then compares observed F2 counts with the candidate ratios. For 1 and 2 degrees of freedom, the chi-square tail has closed forms, so no library is needed.

```python
import math
from collections import Counter
from itertools import product


def dihybrid_classes() -> Counter:
    """Counts of the four genotype classes among the 16 gamete pairs of AaBb x AaBb."""
    counts = Counter()
    for (a1, b1), (a2, b2) in product(product("Aa", "Bb"), repeat=2):
        counts[("A_" if "A" in (a1, a2) else "aa") + ("B_" if "B" in (b1, b2) else "bb")] += 1
    return counts


def modified_ratio(phenotype: dict[str, str]) -> dict[str, int]:
    """F2 phenotype counts out of 16 when each genotype class is mapped to a phenotype."""
    out = Counter()
    for cls, n in dihybrid_classes().items():
        out[phenotype[cls]] += n
    return dict(out)


def chi2_p(x: float, df: int) -> float:
    """Upper tail of the chi-square distribution, closed forms for 1 and 2 degrees of freedom."""
    return math.erfc(math.sqrt(x / 2)) if df == 1 else math.exp(-x / 2)


CANDIDATES = {2: [(9, 7), (13, 3), (15, 1)], 3: [(9, 3, 4), (9, 6, 1), (12, 3, 1)]}


def fit_ratios(observed: list[int]) -> list[tuple]:
    """Chi-square fit of F2 phenotype counts to the modified ratios with as many classes,
    matching classes by size (largest observed with largest expected)."""
    n, obs = sum(observed), sorted(observed, reverse=True)
    fits = []
    for ratio in CANDIDATES[len(obs)]:
        expected = [n * r / 16 for r in sorted(ratio, reverse=True)]
        x2 = sum((o - e) ** 2 / e for o, e in zip(obs, expected))
        fits.append((":".join(map(str, ratio)), round(x2, 2), round(chi2_p(x2, len(obs) - 1), 3)))
    return sorted(fits, key=lambda f: f[1])


print(dict(sorted(dihybrid_classes().items())))
mouse = {"A_B_": "agouti", "aaB_": "solid", "A_bb": "albino", "aabb": "albino"}   # B plays C
print(modified_ratio(mouse))
print(fit_ratios([182, 77, 61]))          # invented F2 counts
print(fit_ratios([171, 129]))
```

```text
{'A_B_': 9, 'A_bb': 3, 'aaB_': 3, 'aabb': 1}
{'agouti': 9, 'albino': 4, 'solid': 3}
[('9:3:4', 0.15, 0.927), ('9:6:1', 99.48, 0.0), ('12:3:1', 102.88, 0.0)]
[('9:7', 0.07, 0.793), ('13:3', 115.8, 0.0), ('15:1', 691.49, 0.0)]
```

The mouse rule, with B standing for the pigment gene C, gives 9 agouti, 3 solid and 4 albino. The invented counts 182 : 77 : 61 fit 9:3:4 ($p = 0.93$) and reject the other three-class ratios; 171 : 129 fit 9:7. Matching classes by size is a shortcut for teaching: with real data, match them by phenotype.

## Worked example

> [!example] Two white lines that make purple (invented counts)
> Two true-breeding white-flowered lines are crossed; the F1 is purple. The F2 has 171 purple and 129 white plants.
> 1. **Two genes.** If both lines carried recessive mutations in the same gene, the F1 would be white too. A purple F1 means that each line supplies the dominant allele the other lacks, `aaBB` x `AAbb` giving `AaBb`: the logic of the complementation test ([[Genetic Screen]]).
> 2. **Ratio.** $171/300 = 0.57$, close to $9/16 = 0.5625$. Expected 168.75 : 131.25, so $X^2 = \frac{2.25^2}{168.75} + \frac{2.25^2}{131.25} = 0.07$ and $p = 0.79$: a 9:7 ratio.
> 3. **Interpretation.** Purple needs a dominant allele at both genes: complementary genes, two steps in series of one pathway.
> 4. **A prediction to check.** A test cross of the F1 with `aabb` should give 1 purple : 3 white.

## Common misconceptions

> [!warning] "Epistasis is a kind of dominance"
> Dominance relates the two alleles of one gene and shows in a monohybrid cross ([[Dominance]]); epistasis relates different genes and shows only when two loci are followed together. A monohybrid 1:2:1 or 2:1 ratio is about dominance or lethality, never epistasis.

> [!warning] "A modified ratio means the genes are linked"
> Ratios out of 16 require independent assortment: they are the 9:3:3:1 classes, merged. Linkage changes the class frequencies themselves ([[Genetic Linkage]]).

> [!warning] "No statistical epistasis means the genes do not interact"
> Statistical epistasis depends on allele frequencies: a complete masking interaction can contribute little interaction variance in a population (Exercise 5).[^phillips]

## Exercises

> [!question] Exercise 1 (L2)
> Two dihybrid F2 populations of 300 plants show two phenotypes each: (a) 280 : 20, (b) 246 : 54 (invented). Identify each ratio and the kind of interaction.

> [!success]- Solution
> (a) 15:1 expects 281.25 : 18.75, $X^2 = 0.09$ ($p = 0.77$): duplicate genes, a dominant allele of either gene suffices. (b) 13:3 expects 243.75 : 56.25, $X^2 = 0.11$ ($p = 0.74$): dominant suppression; 15:1 is rejected ($X^2 = 70.7$). `fit_ratios` (Computational representation) gives the same values.

> [!question] Exercise 2 (L2)
> Derive the F1 test-cross ratios (`AaBb` x `aabb`) for 9:3:4, 9:7, 12:3:1, 15:1 and 13:3. Which two cannot be told apart by the ratio, and how would you distinguish them?

> [!success]- Solution
> The test cross gives `AaBb`, `Aabb`, `aaBb`, `aabb` in equal parts, merged as in the F2: 1:1:2, 1:3, 2:1:1, 3:1 and 3:1. 15:1 and 13:3 both give 3:1, but their minority classes differ: `aabb` for 15:1, which breeds true when two minority offspring are crossed, and `aaBb` for 13:3, whose intercross gives 3 coloured : 1 white.

> [!question] Exercise 3 (L3, Python)
> With `fit_ratios`, analyse the three-class F2 counts 95 : 23 : 42 and 29 : 7 : 12 (invented). Are the alternatives excluded equally well in both cases?

> [!success]- Solution
> ```python
> print(fit_ratios([95, 23, 42]), fit_ratios([29, 7, 12]), sep="\n")
> # [('9:3:4', 2.01, 0.366), ('9:6:1', 22.58, 0.0), ('12:3:1', 26.91, 0.0)]
> # [('9:3:4', 0.59, 0.744), ('9:6:1', 7.48, 0.024), ('12:3:1', 7.69, 0.021)]
> ```
>
> Both fit 9:3:4 best. With 160 plants the alternatives are rejected overwhelmingly; with 48, only at $p \approx 0.02$, and their smallest expected class is $48/16 = 3$, below the expected-count condition of the chi-square test,[^stats] so those $p$-values are approximate. A larger F2, or a test cross (1:1:2 expected), settles it.

> [!question] Exercise 4 (L3, Python)
> Invented relative fitnesses of four yeast single mutants are a 0.90, b 0.80, c 0.95, d 0.70, and of double mutants ab 0.73, ac 0.10, bd 0.75, cd 0.00. Compute the interaction under the multiplicative and the additive null models, and classify each pair.

> [!success]- Solution
> ```python
> single = {"a": 0.90, "b": 0.80, "c": 0.95, "d": 0.70}          # invented relative fitnesses
> double = {("a", "b"): 0.73, ("a", "c"): 0.10, ("b", "d"): 0.75, ("c", "d"): 0.00}
> for (x, y), w in double.items():
>     eps = w - single[x] * single[y]                             # multiplicative null model
>     add = w - (single[x] + single[y] - 1)                       # additive null model
>     label = ("synthetic lethal" if w < 0.05 else "negative" if eps < -0.1
>              else "positive" if eps > 0.1 else "no interaction")
>     print(x + y, round(eps, 3), round(add, 3), label)
> # ab 0.01 0.03 no interaction
> # ac -0.755 -0.75 negative
> # bd 0.19 0.25 positive
> # cd -0.665 -0.65 synthetic lethal
> ```
>
> ab is close to multiplicative, but the additive model reports $+0.03$, of which $(1 - 0.9)(1 - 0.8) = 0.02$ is pure scale effect. ac is a strong negative interaction (synthetic sick), cd synthetic lethal, as expected for redundant genes; bd is positive, as expected if b and d act in the same pathway. The thresholds ($\pm 0.1$) are arbitrary: real screens use replicate measurements to judge significance.

> [!question] Exercise 5 (M1, Python)
> Take the masking model $y = 0$ for `aa`, otherwise $y = 2$ if `B_` and $y = 1$ if `bb`. Under Hardy-Weinberg proportions with independent loci and frequency 0.5 for `b`, compute the share of genetic variance not captured by the separate effects of the two loci, for frequencies 0.05, 0.3, 0.5 and 0.9 of `a`.

> [!success]- Solution
> ```python
> def epistatic_fraction(q_a: float, q_b: float) -> float:
>     """Interaction share of genetic variance for y = 0 if aa, else 2 if B_ else 1."""
>     hwe = lambda q: {0: (1 - q) ** 2, 1: 2 * q * (1 - q), 2: q ** 2}   # copies of a or b
>     pa, pb = hwe(q_a), hwe(q_b)
>     y = lambda ga, gb: 0.0 if ga == 2 else (2.0 if gb < 2 else 1.0)
>     cells = [(ga, gb, pa[ga] * pb[gb]) for ga in range(3) for gb in range(3)]
>     mu = sum(w * y(ga, gb) for ga, gb, w in cells)
>     ma = {ga: sum(pb[gb] * y(ga, gb) for gb in range(3)) for ga in range(3)}   # E[y | ga]
>     mb = {gb: sum(pa[ga] * y(ga, gb) for ga in range(3)) for gb in range(3)}   # E[y | gb]
>     v_g = sum(w * (y(ga, gb) - mu) ** 2 for ga, gb, w in cells)
>     v_i = sum(w * (y(ga, gb) - ma[ga] - mb[gb] + mu) ** 2 for ga, gb, w in cells)
>     return v_i / v_g
>
> for q_a in (0.05, 0.3, 0.5, 0.9):
>     print(q_a, round(epistatic_fraction(q_a, 0.5), 3))
> # 0.05 0.002
> # 0.3 0.036
> # 0.5 0.049
> # 0.9 0.057
> ```
>
> Although `aa` completely masks B, at most about 6 % of the genetic variance is interaction variance, and almost none when `a` is rare: a population analysis attributes nearly everything to separate locus effects. Compositional epistasis is a property of genotypes; statistical epistasis is a property of genotypes and allele frequencies together.[^phillips]

## Mastery checklist

- [ ] 1 Recognized: I can define epistasis, epistatic and hypostatic genes, and list the classic modified ratios.
- [ ] 2 Understood: I can explain each modified ratio from a pathway, and distinguish epistasis from dominance and from linkage.
- [ ] 3 Practiced: I can identify a ratio with a chi-square fit, predict test-cross ratios, and compute interaction scores under multiplicative and additive null models, by hand and in Python.
- [ ] 4 Applied: I tested an interaction term between two variants in a real genotype-phenotype dataset, or computed interaction scores from a published double-mutant fitness table.
- [ ] 5 Explained: I can teach the functional, compositional and statistical meanings of epistasis, and why statistical epistasis depends on allele frequencies and on scale.

## References

[^os12]: [[Biology 2e (OpenStax)]], ch. 12, section 12.3 "Laws of Inheritance" (epistasis: one gene masking another, epistatic and hypostatic alleles, mouse coat colour with the agouti and pigment genes).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), gene interaction: modified dihybrid ratios (recessive and dominant epistasis, complementary and duplicate genes, suppressors), their interpretation through biochemical pathways, and modifier genes.
[^beadle]: [[Beadle 1941 - Genetic Control of Biochemical Reactions in Neurospora]], *PNAS* 27(11):499-506.
[^phillips]: [[Phillips 2008 - Epistasis, the Essential Role of Gene Interactions]], *Nature Reviews Genetics* 9:855-867.
[^futuyma]: [[Evolution (Futuyma)]], 5th ed. (2023), fitness and the effects of mutations on fitness (chapter numbers not verified).
[^stats]: [[Introductory Statistics (OpenStax)]], chapter "The Chi-Square Distribution" (goodness-of-fit test and its expected-count condition).
