---
aliases:
  - X-Linked Inheritance
  - Sex Linkage
  - Hemizygosity
  - X-linked recessive
  - Hérédité liée au sexe
  - Hérédité liée à l'X
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mendelian Inheritance]]"
  - "[[Chromosome]]"
  - "[[Meiosis]]"
  - "[[Dominance]]"
related:
  - "[[Pedigree Analysis]]"
  - "[[Genetic Disease]]"
  - "[[Ploidy]]"
  - "[[Genotype]]"
  - "[[Mitochondrial DNA]]"
  - "[[Epigenetics]]"
  - "[[Variant Calling]]"
  - "[[Hardy-Weinberg Equilibrium]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Mangs 2007 - The Human Pseudoautosomal Region]]"
  - "[[GA4GH hts-specs]]"
---

# Sex-Linked Inheritance

> [!abstract]
> Genes on the X chromosome are inherited differently in the two sexes: a mother passes an X to every child, a father passes his X only to his daughters, and a son, with a single X, shows whatever allele he received.

## Definition

**Sex-linked inheritance** is the transmission of genes carried on a sex chromosome (X or Y in mammals), whose expression therefore depends on the sex of the individual.[^os12] In XY males, each gene of the X-specific region is present in a single copy: males are **hemizygous** for X-linked genes, so the terms dominant and recessive do not apply to them.[^os12] This note is mostly about **X-linked** genes; Y-linked genes simply pass from father to son.

## Why it matters

- **Ploidy is not constant along a genome.** In an XY sample, the X outside the pseudoautosomal regions and the Y are present once ([[Ploidy]]). A variant caller that assumes two copies everywhere can report heterozygous calls there that cannot be real.
- **Sample sex is a quality check.** Heterozygosity on the non-pseudoautosomal X separates XX from XY samples; a mismatch with the recorded sex points to a sample swap or a contamination (Exercise 5).
- **Allele counts differ.** On the X, a population of $N_f$ females and $N_m$ males carries $2N_f + N_m$ copies, not $2N$; allele frequencies, Hardy-Weinberg tests and association tests must be adapted.
- **Clinical genomics.** X-linked recessive disorders mostly affect males, through unaffected carrier mothers ([[Pedigree Analysis]], [[Genetic Disease]]).

## Core (L1)

### Three transmission rules

Every child receives one X from the mother. A daughter receives the father's X; a son receives the father's Y.[^os12] Hence:

1. a **mother** passes each of her two X alleles to a child with probability 1/2, to sons and daughters alike;
2. a **father** passes his X allele to **all his daughters** and to **none of his sons**;
3. a **son's** X-linked phenotype reveals his single allele directly.

### Morgan's white-eyed flies

In 1910, Thomas Hunt Morgan mapped a white-eye mutation of *Drosophila melanogaster* to the X chromosome: eye colour was the first X-linked trait identified. Red eye ($X^W$) is dominant over white ($X^w$); males are $X^WY$ or $X^wY$.[^os12]

| Cross | Daughters | Sons |
|---|---|---|
| red female $X^WX^W$ x white male $X^wY$ | all red ($X^WX^w$) | all red ($X^WY$) |
| F1: $X^WX^w$ x $X^WY$ | all red | 1/2 red, 1/2 white |
| reciprocal: white female $X^wX^w$ x red male $X^WY$ | all red ($X^WX^w$) | all white ($X^wY$) |

In the F2 of the first cross, white eyes appear only in males, and the two reciprocal crosses give different results: the signature of a gene on the X.[^os12] In the reciprocal cross, sons resemble their mother and daughters their father (**criss-cross** inheritance).[^griffiths]

![[sex-chromosomes-par.svg]]

### X-linked recessive traits in humans

Some forms of colour blindness, haemophilia and muscular dystrophy are X-linked in humans.[^os12][^griffiths] For an X-linked recessive allele $X^a$:

```text
carrier mother X^A X^a  x  unaffected father X^A Y
                 X^A (father)         Y (father)
X^A (mother)     X^A X^A  unaffected  X^A Y  unaffected son
X^a (mother)     X^A X^a  carrier     X^a Y  affected son
```

Half the sons are affected, half the daughters are carriers, no daughter is affected. Typical pedigree: many more affected males than females, the trait skips generations through carrier females, and it is never passed from father to son.[^griffiths]

## Deeper (L2)

### Other patterns

| Pattern | Key signature |
|---|---|
| X-linked recessive | mostly males; affected sons of unaffected carrier mothers; no father-to-son transmission |
| X-linked dominant | an affected father has all daughters affected and no son affected; affected mothers pass it to half of their children of each sex |
| Y-linked | father to all sons, never to daughters |

(Derived from the three transmission rules; see [[Pedigree Analysis]] for the full reasoning.[^griffiths])

### X inactivation: dosage compensation in mammals

Females have two X chromosomes, males one. In female mammals, one X is inactivated in each somatic cell early in development, chosen at random, and the choice is kept by all descendants of that cell; the inactive X is condensed (the Barr body) and coated by the non-coding XIST RNA.[^alberts] Consequences:

- expression of most X-linked genes is similar in the two sexes (**dosage compensation**);
- a heterozygous female is a **mosaic** of cell patches expressing one or the other allele, so a carrier has some cells in which only the mutant allele is active ([[Epigenetics]]).[^alberts]

### Pseudoautosomal regions

The X and Y are homologous at their tips: **PAR1** at the end of the short arms and **PAR2** at the end of the long arms. These regions pair and recombine during meiosis, and deletion of PAR1 prevents X-Y pairing and causes male sterility.[^mangs] Genes in the PARs are present in two copies in both sexes; only genes outside them follow the X-linked rules above.

### Other sex-determination systems

In birds, females are the heterogametic sex (ZW) and males ZZ, so it is females that are hemizygous for Z-linked genes and the transmission rules swap sexes.[^griffiths]

## Advanced (L3)

- **Calling variants on X and Y.** A correct pipeline sets ploidy by region: 2 for autosomes, for the X in XX samples and for the PARs; 1 for the rest of the X and for the Y in XY samples, where the VCF genotype is a single allele.[^hts] Because the PARs are homologous copies on X and Y, reads from them can map to either; how the reference represents them decides where the reads land, so check it before interpreting coverage or calls there ([[Variant Calling]], [[Reference Genome]]).
- **Sex inference.** Non-PAR X heterozygosity near zero suggests one X, high heterozygosity two; intermediate values suggest contamination or a mixture. Combined with Y coverage, the same data reveal sex-chromosome aneuploidies (one X without Y, two X with Y). The threshold depends on the sites used: calibrate it on samples of known sex.
- **Population genetics on the X.** Under random mating, male genotype frequencies equal allele frequencies ($p$, $q$), female ones are $p^2, 2pq, q^2$. A recessive X-linked phenotype is therefore $1/q$ times more frequent in males than in females ([[Hardy-Weinberg Equilibrium]]).
- **Mosaicism in data.** Because X inactivation is random per cell lineage, bulk RNA-seq of a female tissue can show both alleles of an inactivated X-linked gene, while single-cell data show one allele per cell (Exercise 6).

## Mathematical representation

- Let $X_m = (x_1, x_2)$ be the mother's X alleles and $x_f$ the father's. For a child:
  - daughter: genotype $(x_i, x_f)$ with $i$ uniform on $\{1, 2\}$;
  - son: genotype $(x_i)$, hemizygous, with $i$ uniform on $\{1, 2\}$.
- **Risks** for an X-linked recessive allele $a$ and carrier mother $X^AX^a$: $P(\text{son affected}) = \frac12$; $P(\text{daughter carrier} \mid \text{father } X^AY) = \frac12$; $P(\text{child affected}) = \frac12 \cdot \frac12 = \frac14$ if sexes are equally likely.
- **Allele frequency** from $N_f$ females with alt counts $g_j \in \{0, 1, 2\}$ and $N_m$ males with $h_k \in \{0, 1\}$:
$$\hat q = \frac{\sum_j g_j + \sum_k h_k}{2N_f + N_m}.$$
- **Hardy-Weinberg on X**: males $P(X^a Y) = q$; females $P(X^aX^a) = q^2$, $P(X^AX^a) = 2pq$; sex ratio of affected $= q / q^2 = 1/q$.

## Computational representation

A male X-linked genotype is one allele, a female genotype two; in a VCF, a haploid call is written with a single allele (`1`, not `1/1`).[^hts]

```python
from collections import Counter


def x_linked_cross(mother: tuple[str, str], father: str) -> dict[str, Counter]:
    """Children of a mother with two X alleles and a father with one X allele (and a Y)."""
    daughters, sons = Counter(), Counter()
    for allele in mother:                                     # each maternal X with prob 1/2
        daughters["".join(sorted(allele + father))] += 1      # X from mother + father's X
        sons[allele] += 1                                     # X from mother + father's Y
    return {"daughters": daughters, "sons": sons}


def eye_colour(genotype: str) -> str:
    """Drosophila white gene: W (red, dominant) and w (white). Males carry one allele."""
    return "red" if "W" in genotype else "white"


crosses = {"red female x white male (P)": (("W", "W"), "w"),
           "F1 x F1": (("W", "w"), "W"),
           "white female x red male": (("w", "w"), "W")}
for name, (mother, father) in crosses.items():
    children = x_linked_cross(mother, father)
    summary = {sex: dict(Counter(eye_colour(g) for g in c.elements())) for sex, c in children.items()}
    print(f"{name:28}", summary)
```

```text
red female x white male (P)  {'daughters': {'red': 2}, 'sons': {'red': 2}}
F1 x F1                      {'daughters': {'red': 2}, 'sons': {'red': 1, 'white': 1}}
white female x red male      {'daughters': {'red': 2}, 'sons': {'white': 2}}
```

The output reproduces Morgan's table: white F2 flies are all sons, and the reciprocal crosses differ.

## Worked example

> [!example] Risk in a family with haemophilia
> A woman's brother has an X-linked recessive disorder; her parents are unaffected. She has an unaffected partner.
> 1. The affected brother received his $X^a$ from their mother (sons get their X from the mother), so the mother is a carrier $X^AX^a$.
> 2. The woman received one of her mother's two X: $P(\text{carrier}) = \frac12$.
> 3. If she is a carrier, each son is affected with probability $\frac12$. So $P(\text{her first son affected}) = \frac12 \times \frac12 = \frac14$.
> 4. Her daughters cannot be affected (their father gives $X^A$), but each is a carrier with probability $\frac12 \times \frac12 = \frac14$.
> Testing the woman for the family variant replaces the $\frac12$ of step 2 by 0 or 1, which is why carrier testing changes the counselling ([[Pedigree Analysis]]).

## Common misconceptions

> [!warning] "A son can inherit an X-linked disorder from his father"
> A father gives his son a Y, never his X. An affected son of an unaffected mother got the allele from her, or it arose de novo.

> [!warning] "Females cannot have X-linked recessive disorders"
> They can, if both X carry the allele (affected father and carrier mother). And heterozygous females are mosaics, with some cells in which only the mutant allele is active.[^alberts]

> [!warning] "A trait more common in males must be X-linked"
> Other causes can make a trait sex-biased. The transmission pattern decides: no father-to-son transmission and affected sons of unaffected carrier mothers point to the X.

> [!warning] "Males are haploid on the whole X"
> Only outside the pseudoautosomal regions: the PARs are present on both X and Y.[^mangs]

## Exercises

> [!question] Exercise 1 (L1)
> A carrier woman ($X^AX^a$) and an affected man ($X^aY$) have children. Give the probabilities of an affected son, an affected daughter and a carrier daughter.

> [!success]- Solution
> Sons get the mother's X: affected with probability 1/2. Daughters get $X^a$ from the father and either maternal X: $X^aX^a$ (affected) 1/2, $X^AX^a$ (carrier) 1/2. Unlike the classic cross, half the daughters are affected.

> [!question] Exercise 2 (L1)
> In Morgan's reciprocal cross (white female x red male), predict the F1 and then the F2 obtained by crossing F1 females and males. Which sexes show white eyes in the F2?

> [!success]- Solution
> F1: daughters $X^WX^w$ (red), sons $X^wY$ (white). F2 from $X^WX^w \times X^wY$: daughters 1/2 $X^WX^w$ (red), 1/2 $X^wX^w$ (white); sons 1/2 $X^WY$ (red), 1/2 $X^wY$ (white). Both sexes now show white, in equal proportions: the two reciprocal crosses give different F2, unlike autosomal genes.

> [!question] Exercise 3 (L2)
> In a pedigree, an affected man with an unaffected wife has four daughters, all affected, and three sons, none affected. Which mode of inheritance fits best, and why do the others fail?

> [!success]- Solution
> X-linked dominant: the father gives his X to every daughter and to no son. X-linked recessive would need all four daughters to have received an allele from their unaffected mother too. Autosomal dominant would give each child a 1/2 chance regardless of sex, and $(1/2)^7 \approx 0.008$ for this exact split. Y-linked would affect sons, not daughters.

> [!question] Exercise 4 (L2)
> An X-linked recessive allele has frequency $q = 0.05$ in a randomly mating population. What fraction of males and of females are affected, and what fraction of females are carriers?

> [!success]- Solution
> Males: $q = 0.05$ (5 %). Females: $q^2 = 0.0025$ (0.25 %). Carriers: $2pq = 2 \times 0.95 \times 0.05 = 0.095$. Affected males outnumber affected females $1/q = 20$ to 1.

> [!question] Exercise 5 (L3, Python)
> Invented genotypes at 12 non-PAR chrX sites are given below. Compute each sample's heterozygous fraction among called sites and infer its sex. Then write a function estimating an X-linked allele frequency from 6 females (alt counts 0, 1, 0, 0, 2, 1) and 4 males (1, 0, 0, 1).

> [!success]- Solution
> ```python
> # Invented genotypes at 12 chrX sites outside the PARs ("./." = no call)
> samples = {
>     "S1": ["0/1", "1/1", "0/0", "0/1", "0/1", "0/0", "1/1", "0/1", "0/0", "0/1", "./.", "0/1"],
>     "S2": ["1/1", "0/0", "0/0", "1/1", "0/0", "1/1", "0/0", "0/0", "1/1", "0/0", "0/0", "1/1"],
>     "S3": ["1/1", "0/0", "0/1", "1/1", "0/0", "1/1", "0/0", "0/0", "1/1", "0/0", "0/0", "1/1"],
> }
>
>
> def het_fraction(genotypes: list[str]) -> float:
>     called = [g for g in genotypes if g != "./."]
>     return sum(g in ("0/1", "1/0") for g in called) / len(called)
>
>
> for name, gts in samples.items():
>     h = het_fraction(gts)
>     call = "XX" if h > 0.2 else "XY" if h == 0 else "check"
>     print(name, round(h, 2), call)
>
>
> def x_allele_frequency(female_counts: list[int], male_counts: list[int]) -> float:
>     """Alt-allele frequency on X: females carry 2 copies (0, 1, 2), males 1 copy (0, 1)."""
>     alt = sum(female_counts) + sum(male_counts)
>     return alt / (2 * len(female_counts) + len(male_counts))
>
>
> print(round(x_allele_frequency([0, 1, 0, 0, 2, 1], [1, 0, 0, 1]), 3))
> # S1 0.55 XX
> # S2 0.0 XY
> # S3 0.08 check
> # 0.375
> ```
>
> S2 behaves as one X: every call is homozygous (a diploid caller wrote `1/1` for a haploid `1`). S3 has one heterozygous call among homozygous ones: a genotyping error, a site in an unannotated PAR-like or duplicated region, or low-level contamination; check read balance and Y coverage before deciding. The allele frequency is $6 / (2 \times 6 + 4) = 0.375$, not $6/20$.

> [!question] Exercise 6 (L3)
> A woman is heterozygous for a coding SNP in an X-linked gene outside the PARs. Predict the allele ratio in (a) her bulk RNA-seq reads from a large tissue sample, (b) single cells from that tissue, (c) her DNA. What would a strong departure from 50:50 in (a) suggest?

> [!success]- Solution
> (a) Roughly balanced if inactivation choice was random over many patches, since the bulk averages cells with either X active. (b) One allele per cell, for a gene subject to inactivation, because each cell expresses only its active X.[^alberts] (c) 50:50, since both X are present in every cell. A strongly skewed bulk ratio suggests skewed inactivation (a tissue derived from few precursor cells, or selection against cells expressing one allele) or an allele-specific expression effect; the single-cell data distinguish the two.

## Mastery checklist

- [ ] 1 Recognized: I can define X-linked inheritance and hemizygosity and state who passes an X to whom.
- [ ] 2 Understood: I can explain Morgan's reciprocal crosses, X-linked recessive and dominant pedigrees, X inactivation and the pseudoautosomal regions.
- [ ] 3 Practiced: I can compute X-linked risks and allele frequencies, and simulate X-linked crosses in Python.
- [ ] 4 Applied: I checked the sex of real samples from chrX heterozygosity and set region-specific ploidy in a variant-calling run.
- [ ] 5 Explained: I can teach how sex chromosomes break the assumptions of diploid genotyping, allele counting and Hardy-Weinberg tests, and how to handle them.

## References

[^os12]: [[Biology 2e (OpenStax)]], ch. 12 "Mendel's Experiments and Heredity", section "Characteristics and Traits" (sex-linked traits: Morgan's white-eyed *Drosophila*, hemizygous males, X-linked human traits).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), sex linkage: X-linked pedigrees and disorders, X-linked dominant and Y-linked patterns, ZW sex determination.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), on X-chromosome inactivation and dosage compensation in mammals.
[^mangs]: [[Mangs 2007 - The Human Pseudoautosomal Region]], *Current Genomics* 8(2):129-136.
[^hts]: [[GA4GH hts-specs]], VCF specification, genotype field `GT` (haploid calls).
