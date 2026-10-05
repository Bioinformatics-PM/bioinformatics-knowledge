---
aliases:
  - Complete Dominance
  - Incomplete Dominance
  - Codominance
  - Dominant and Recessive Alleles
  - Dominance génétique
  - Dominance incomplète
tags:
  - type/concept
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Allele]]"
  - "[[Genotype]]"
  - "[[Phenotype]]"
  - "[[Mendelian Inheritance]]"
related:
  - "[[Gene]]"
  - "[[Mutation]]"
  - "[[Sex-Linked Inheritance]]"
  - "[[Epistasis]]"
  - "[[Genetic Disease]]"
  - "[[Pedigree Analysis]]"
  - "[[Heritability]]"
  - "[[Genome-Wide Association Study]]"
  - "[[Mutation-Selection Balance]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Molecular Cell Biology (Lodish)]]"
  - "[[Mendel 1866 - Experiments in Plant Hybridization]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
---

# Dominance

> [!abstract]
> Dominance describes what a heterozygote looks like: the same as one homozygote (complete dominance), in between (incomplete dominance), or showing the products of both alleles (codominance). The explanation lies in what each allele's product does.

## Definition

For two alleles $A_1$ and $A_2$ of one gene and a given phenotype:[^os12]

- **complete dominance**: the heterozygote $A_1A_2$ has the same phenotype as the homozygote $A_1A_1$; $A_1$ is **dominant**, $A_2$ **recessive**;
- **incomplete dominance**: the heterozygote is intermediate between the two homozygotes;
- **codominance**: both alleles are expressed at the same time in the heterozygote.

Dominance is a relation between two alleles for one phenotype, not a property of an allele on its own: the same pair can look dominant at one level of description and codominant at another.[^griffiths]

## Why it matters

- **A genotype call is not a phenotype.** A `0/1` call in a [[VCF Format|VCF]] predicts disease only once the mode of action is known. Rare-disease filtering follows it: a single heterozygous variant can explain a dominant disorder, a recessive one needs both copies hit (homozygous, or two different variants on the two homologs) ([[Pedigree Analysis]], [[Trio Analysis]]).
- **Loss of function matters only where dosage matters.** Clinical guidelines count a null variant (nonsense, frameshift, canonical splice site...) as very strong evidence of pathogenicity only in a gene where loss of function is a known mechanism of disease.[^richards] That is the molecular view of dominance developed below.
- **Association models encode dominance.** Coding genotypes as 0, 1, 2 in a [[Genome-Wide Association Study]] assumes the heterozygote lies midway between the homozygotes; dominant and recessive codings are alternatives (Exercise 5).

## Core (L1)

![[dominance-gene-products.svg]]

| Pattern | Heterozygote | F2 phenotypes of $A_1A_2 \times A_1A_2$ | Example |
|---|---|---|---|
| Complete dominance | like the dominant homozygote | 3 : 1 | pea seeds, round over wrinkled[^mendel] |
| Incomplete dominance | intermediate | 1 : 2 : 1 | snapdragon (*Antirrhinum majus*): red x white gives pink[^os12] |
| Codominance | both products present | 1 : 2 : 1 | human MN blood group: $L^M L^N$ carries both M and N antigens[^os12] |

With incomplete dominance or codominance, the F2 phenotypes show the genotype ratio directly (1 $C^RC^R$ red : 2 $C^RC^W$ pink : 1 $C^WC^W$ white), and the parental forms reappear: no blending.[^os12]

**Notation.** Upper and lower case ($R$, $r$) are used for complete dominance; superscripts on a shared symbol ($C^R$, $C^W$; $L^M$, $L^N$) when neither allele is simply dominant.[^os12]

**More than two alleles.** One person carries at most two alleles of a gene, but a population can carry many.[^os12] The ABO blood group gene has three common alleles: $I^A$ and $I^B$ are codominant with each other, and both are dominant over $i$.[^griffiths]

| Genotype | $I^AI^A$, $I^Ai$ | $I^BI^B$, $I^Bi$ | $I^AI^B$ | $ii$ |
|---|---|---|---|---|
| Blood type | A | B | AB | O |

One locus shows both codominance and complete dominance: dominance describes pairs of alleles.

## Deeper (L2)

### The gene-product view

Most phenotypes are the output of a gene product, so dominance depends on how much product the heterozygote makes and what it does.[^lodish]

- **Recessive alleles are usually loss of function.** One working copy makes enough product for a normal phenotype (the gene is **haplosufficient**), so only the homozygote shows the mutant phenotype.[^lodish]
- **Dominant mutant alleles** arise in three main ways:[^lodish]
  1. **Haploinsufficiency**: half the normal amount of product is not enough, so a loss-of-function allele is dominant;
  2. **Gain of function**: the mutant product does something new, or is made at the wrong time, place or amount;
  3. **Dominant negative**: the mutant product interferes with the normal one, typically when both assemble into one complex (Exercise 4).
- **Incomplete dominance as dosage**: when the phenotype scales with the amount of product (a pigment, for example), a heterozygote with one working copy is intermediate.[^griffiths]
- **Codominance at the product level**: each allele makes a distinguishable product and both are detected. In the ABO system, the $I^A$ and $I^B$ alleles encode enzymes that add different sugars to the same red-cell surface molecule, and $i$ makes no active enzyme; an $I^AI^B$ person has both sugars.[^lodish]

### One allele, three answers

The sickle-cell allele of β-globin shows how the level of observation sets the answer.[^griffiths] For anaemia, it is recessive: heterozygotes are generally healthy. For the shape of red cells at low oxygen, heterozygotes show some sickling: incomplete dominance. For the haemoglobin molecules, heterozygotes carry both normal and sickle haemoglobin: codominance.

### Hemizygous males

For genes on the X chromosome, XY males carry a single copy, so dominance and recessiveness do not apply to them ([[Sex-Linked Inheritance]]).[^os12]

## Advanced (L3)

- **Quantitative genetics.** For a continuous trait, give the genotypes $aa$, $Aa$, $AA$ the values $-a$, $d$, $+a$ around the homozygote midpoint. The ratio $d/a$ measures dominance: 0 for no dominance (additive), $+1$ when $A$ is completely dominant, $-1$ when it is completely recessive, beyond $\pm 1$ for overdominance or underdominance.[^hartl] The dominance deviation is why narrow-sense [[Heritability]] (additive) is smaller than broad-sense heritability.
- **Selection sees phenotypes, not alleles.** With fitnesses $1$, $1 - hs$, $1 - s$ for $AA$, $Aa$, $aa$, the dominance coefficient $h$ decides how exposed a deleterious allele is.[^hartl] If $h = 0$ and the allele is rare, almost all copies sit in healthy heterozygotes: at frequency $q = 0.01$ under [[Hardy-Weinberg Equilibrium]] there are $2pq / q^2 = 198$ carriers per affected person, which is why recessive disease alleles persist ([[Mutation-Selection Balance]]).
- **Mechanism guides interpretation.** In a haploinsufficient gene, any null variant is a candidate cause; in a gene acting by gain of function or dominant negative effect, null variants may be harmless in heterozygotes while specific missense changes are pathogenic.[^lodish][^richards] Variant annotation reports the molecular consequence ([[Mutation]]); linking it to disease needs the gene's mechanism.

## Mathematical representation

- Genotype $g \in \{0, 1, 2\}$ copies of allele $A$; phenotype map $\varphi$.
  - Complete dominance of $A$: $\varphi(1) = \varphi(2) \ne \varphi(0)$.
  - Incomplete dominance (ordered phenotype): $\varphi(0) < \varphi(1) < \varphi(2)$.
  - Codominance (sets of products): $\varphi(A_1A_2) = \varphi(A_1A_1) \cup \varphi(A_2A_2)$.
- **Threshold model.** Product $P(g) = g \cdot u$ ($u$: output of one working copy); normal phenotype iff $P(g) \ge \theta$. If $\theta \le u$, the null allele is recessive; if $u < \theta \le 2u$, it is dominant (haploinsufficiency).
- **Genotypic values**: $G(0) = -a$, $G(1) = d$, $G(2) = +a$; dominance ratio $k = d/a$.
- **Association codings**: additive $x = g$; dominant $x = \mathbb{1}[g \ge 1]$; recessive $x = \mathbb{1}[g = 2]$.
- **Dominant negative with $n$ subunits**: if a heterozygote makes equal amounts of both subunits and complexes assemble at random, the active fraction is $(1/2)^n$, against $1/2$ for a simple loss of function.

## Computational representation

A genotype is a pair of alleles (or an allele count); the phenotype is a function applied to it. Keeping the two separate lets the same cross be read under different dominance models.

```python
from collections import Counter
from itertools import product


def cross(parent1: tuple[str, str], parent2: tuple[str, str]) -> Counter:
    """Offspring genotypes (sorted allele pairs) over the 4 equally likely gamete pairs."""
    return Counter(tuple(sorted(pair)) for pair in product(parent1, parent2))


def phenotype_ratio(offspring: Counter, model) -> dict[str, int]:
    ratio = Counter()
    for genotype, n in offspring.items():
        ratio[model(genotype)] += n
    return dict(ratio)


def dose(genotype: tuple[str, str]) -> int:
    """Working copies: '+' is a functional allele, '-' a null (loss-of-function) allele."""
    return genotype.count("+")


models = {
    "complete (1 dose enough)": lambda g: "normal" if dose(g) >= 1 else "mutant",
    "haploinsufficient (2 needed)": lambda g: "normal" if dose(g) >= 2 else "mutant",
    "incomplete (graded product)": lambda g: f"{50 * dose(g)}% product",
}
f2 = cross(("+", "-"), ("+", "-"))
for name, model in models.items():
    print(f"{name:30}", phenotype_ratio(f2, model))


def abo_type(genotype: tuple[str, str]) -> str:
    """A and B alleles each add their own sugar; O adds none."""
    return "".join(sorted({allele for allele in genotype if allele in "AB"})) or "O"


print("A/O x B/O:", phenotype_ratio(cross(("A", "O"), ("B", "O")), abo_type))
```

```text
complete (1 dose enough)       {'normal': 3, 'mutant': 1}
haploinsufficient (2 needed)   {'normal': 1, 'mutant': 3}
incomplete (graded product)    {'100% product': 1, '50% product': 2, '0% product': 1}
A/O x B/O: {'AB': 1, 'A': 1, 'B': 1, 'O': 1}
```

The same null allele is recessive (3:1 normal) or dominant (1:3) depending only on the threshold: dominance is a property of the gene's dosage requirement, not of the DNA change.

## Worked example

> [!example] Parents with blood types A and B, child with type O
> 1. The child is $ii$, so each parent carried an $i$: the type A parent is $I^Ai$, the type B parent $I^Bi$.
> 2. Each parent transmits either allele with probability 1/2, so the four genotypes $I^AI^B$, $I^Ai$, $I^Bi$, $ii$ each have probability 1/4.
> 3. Phenotypes: AB, A, B and O, each 1/4 (the last line of the code output). Four blood types from one pair of parents, because $I^A$ and $I^B$ are codominant while both dominate $i$.[^griffiths]

## Common misconceptions

> [!warning] "Dominant alleles are the common ones"
> Frequency is set by mutation, selection and drift, not by dominance. A dominant disease allele can be rare, and a recessive allele can be the most common one in a population ([[Hardy-Weinberg Equilibrium]]).

> [!warning] "The dominant allele switches off the recessive one"
> Usually both alleles are transcribed. A typical recessive allele simply makes no working product, and one working copy is enough.[^lodish]

> [!warning] "Incomplete dominance is blending"
> Pink snapdragons crossed together give red, pink and white offspring in a 1:2:1 ratio: the alleles stay intact and segregate.[^os12]

> [!warning] "An allele is dominant or recessive, full stop"
> It depends on the other allele ($I^A$ is dominant over $i$ but codominant with $I^B$) and on the phenotype observed (sickle-cell).[^griffiths]

## Exercises

> [!question] Exercise 1 (L1)
> Pink snapdragons ($C^RC^W$) are crossed together. Give the genotype and phenotype ratios, and say which parental phenotypes reappear.

> [!success]- Solution
> Genotypes 1 $C^RC^R$ : 2 $C^RC^W$ : 1 $C^WC^W$; phenotypes 1 red : 2 pink : 1 white. The colours of the original true-breeding lines, red and white, reappear, which rules out blending.

> [!question] Exercise 2 (L1)
> A type A mother and a type AB father have children. Which blood types are possible, with which probabilities, if the mother is (a) $I^AI^A$, (b) $I^Ai$?

> [!success]- Solution
> The father transmits $I^A$ or $I^B$. (a) Children $I^AI^A$ or $I^AI^B$: A 1/2, AB 1/2. (b) Mother transmits $I^A$ or $i$: $I^AI^A$ (A), $I^AI^B$ (AB), $I^Ai$ (A), $I^Bi$ (B): A 1/2, AB 1/4, B 1/4. No type O child is possible in either case, since the father has no $i$.

> [!question] Exercise 3 (L2)
> Explain with gene products why a null allele of a metabolic enzyme is usually recessive, and give two different molecular reasons why a mutant allele can be dominant.

> [!success]- Solution
> One working copy usually produces enough enzyme for normal flux (haplosufficiency), so heterozygotes look normal and only null homozygotes are affected. A mutant allele is dominant if (1) the gene is haploinsufficient, so half the product is not enough; (2) the mutant product gains a new or excessive activity; or (3) it poisons the normal product in a complex (dominant negative).[^lodish]

> [!question] Exercise 4 (L2, Python)
> A protein works as a complex of $n$ identical subunits; a heterozygote makes equal amounts of normal and mutant subunits, which assemble at random, and one mutant subunit inactivates a complex. Compute the active fraction for $n = 1, 2, 4$ and compare with a plain loss-of-function allele.

> [!success]- Solution
> ```python
> def active_fraction(subunits: int, mutant_share: float = 0.5) -> float:
>     """Fraction of complexes with no mutant subunit, if subunits assemble at random."""
>     return (1 - mutant_share) ** subunits
>
> for n in (1, 2, 4):
>     print(n, active_fraction(n))
> # 1 0.5
> # 2 0.25
> # 4 0.0625
> ```
>
> A loss-of-function allele leaves 50 % activity; a poisoning subunit in a dimer leaves 25 %, in a tetramer about 6 %. The larger the complex, the more a mutant subunit behaves as dominant, even in a gene that tolerates losing one copy.

> [!question] Exercise 5 (L3, Python)
> Invented trait values for five individuals per genotype (copies of allele $A$): $g=0$: 9.6, 10.3, 10.1, 9.9, 10.1; $g=1$: 13.5, 14.1, 13.9, 13.6, 13.9; $g=2$: 14.4, 14.0, 14.3, 14.1, 14.2. Estimate $a$, $d$ and $d/a$, then fit the trait on the additive, dominant and recessive codings and compare residual sums of squares.

> [!success]- Solution
> ```python
> from statistics import linear_regression, mean
>
> trait = {0: [9.6, 10.3, 10.1, 9.9, 10.1], 1: [13.5, 14.1, 13.9, 13.6, 13.9],
>          2: [14.4, 14.0, 14.3, 14.1, 14.2]}
> means = {g: round(mean(v), 2) for g, v in trait.items()}
> a = (means[2] - means[0]) / 2                 # half the homozygote difference
> d = means[1] - (means[0] + means[2]) / 2      # heterozygote deviation from the midpoint
> print(means, f"a = {a:.2f}, d = {d:.2f}, d/a = {d / a:.2f}")
>
> codings = {"additive": lambda g: g, "dominant": lambda g: int(g >= 1),
>            "recessive": lambda g: int(g == 2)}
> genotypes = [g for g, v in trait.items() for _ in v]
> values = [y for v in trait.values() for y in v]
> for name, code in codings.items():
>     x = [code(g) for g in genotypes]
>     slope, intercept = linear_regression(x, values)
>     rss = sum((y - intercept - slope * xi) ** 2 for xi, y in zip(x, values))
>     print(f"{name:9} RSS = {rss:6.2f}")
> # {0: 10.0, 1: 13.8, 2: 14.2} a = 2.10, d = 1.70, d/a = 0.81
> # additive  RSS =  10.25
> # dominant  RSS =   1.02
> # recessive RSS =  36.72
> ```
>
> $d/a = 0.81$: $A$ is nearly completely dominant. The dominant coding fits ten times better than the additive one, which forces the heterozygote to the midpoint (12.1) instead of 13.8. The additive model still detects the association, but underestimates the effect of carrying one copy.

## Mastery checklist

- [ ] 1 Recognized: I can define complete dominance, incomplete dominance and codominance and give one example of each.
- [ ] 2 Understood: I can explain dominance through gene products (haplosufficiency, haploinsufficiency, gain of function, dominant negative) and why it depends on the phenotype observed.
- [ ] 3 Practiced: I can predict ratios for multiple-allele crosses such as ABO and compute dominance ratios and genotype codings in Python.
- [ ] 4 Applied: I filtered the variants of a real family under dominant and recessive models and justified each candidate by the gene's mechanism.
- [ ] 5 Explained: I can teach why dominance is a relation, not a property of an allele, and how it enters heritability, selection and variant interpretation.

## References

[^os12]: [[Biology 2e (OpenStax)]], ch. 12 "Mendel's Experiments and Heredity", section "Characteristics and Traits" (alternatives to dominance and recessiveness, multiple alleles, X-linked traits).
[^mendel]: [[Mendel 1866 - Experiments in Plant Hybridization]], seed shape experiment.
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), extensions of Mendelian analysis: dominance relations, multiple alleles (ABO), levels of dominance of the sickle-cell allele.
[^lodish]: [[Molecular Cell Biology (Lodish)]], 4th ed. (2000), on recessive and dominant mutant alleles (loss of function, haploinsufficiency, gain of function, dominant negative) and on the ABO blood group antigens.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), dominance in fitness and in quantitative traits.
[^richards]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], Richards S et al., *Genetics in Medicine* 17(5):405-424, criterion for null variants.
