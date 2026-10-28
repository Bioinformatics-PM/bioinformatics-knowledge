---
aliases:
  - Inherited Disease
  - Hereditary Disease
  - Mendelian Disease
  - Monogenic Disease
  - Complex Disease
  - Multifactorial Disease
  - Penetrance
  - Expressivity
  - Maladie génétique
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Mendelian Inheritance]]"
  - "[[Dominance]]"
  - "[[Mutation]]"
  - "[[Phenotype]]"
  - "[[Pedigree Analysis]]"
related:
  - "[[Epistasis]]"
  - "[[Genome-Wide Association Study]]"
  - "[[Polygenic Risk Score]]"
  - "[[Heritability]]"
  - "[[Quantitative Trait]]"
  - "[[Variant Classification]]"
  - "[[Somatic Mutation]]"
  - "[[Mitochondrial DNA]]"
  - "[[Newborn Screening]]"
  - "[[Selection Bias]]"
projects: []
sources:
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[MIT 7.03 - Genetics]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[ClinVar]]"
  - "[[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]]"
  - "[[Kay 2016 - Huntington Disease Reduced Penetrance Alleles Occur at High Frequency in the General Population]]"
  - "[[Visscher 2017 - 10 Years of GWAS Discovery]]"
  - "[[Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies]]"
  - "[[Nelson 2015 - The Support of Human Genetic Evidence for Approved Drug Indications]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
---

# Genetic Disease

> [!abstract]
> A genetic disease is caused wholly or partly by variants in the genome: one gene's variants in a monogenic disease, many variants of small effect plus the environment in a complex disease; and carriers of a disease genotype are not all affected (penetrance), nor equally affected (expressivity).

## Definition

A **genetic disease** is a disorder caused wholly or partly by variation in the genome. In a **monogenic** (Mendelian) disease, variants in one gene are sufficient to cause it, so it follows the dominant, recessive or X-linked patterns of [[Pedigree Analysis]]; in a **complex** (multifactorial) disease, many genetic variants contribute together with environmental factors.[^griffiths][^mit703][^visscher] **Penetrance** is the proportion of individuals with a given genotype who show the corresponding phenotype; **expressivity** is the degree to which the phenotype is expressed in those who show it.[^griffiths]

## Why it matters

- **Rare-disease diagnosis** searches a patient's exome or genome for a monogenic cause ([[Exome Sequencing]], [[Variant Prioritization]]). Candidate variants are sorted into five standard classes, from pathogenic to benign, using evidence that includes population frequency, segregation in the family and de novo occurrence ([[Variant Classification]]),[^richards] and classifications are shared in the ClinVar database.[^clinvar]
- **Complex-disease genetics** works with association studies and polygenic scores, because for almost every complex trait studied many loci contribute ([[Genome-Wide Association Study]], [[Polygenic Risk Score]]).[^visscher]
- **Penetrance decides what a variant means.** A "disease allele" carried by many healthy people has low penetrance or is misclassified: population data showed that reduced-penetrance alleles of Huntington disease are far more common than the disease (Core).[^kay]
- **Drug discovery.** Drug targets backed by human genetic evidence for their indication are more frequent among approved drugs than among those in early development.[^nelson]
- **New mutations count.** De novo mutations contribute to disease risk, and each child carries more of them the older the father.[^kong]

## Core (L2)

### Kinds of genetic disease

| Class | Cause | Transmission | Example |
|---|---|---|---|
| Monogenic | Variants in one gene | Dominant, recessive or X-linked ([[Pedigree Analysis]]) | Sickle-cell anemia: homozygosity for the *HBB* variant `c.20A>T` (p.Glu7Val, rs334)[^clinvar] |
| Chromosomal | Gain or loss of a chromosome or of a large segment | Nondisjunction in a parent's meiosis ([[Meiosis]]) | Trisomy 21[^os13] |
| Mitochondrial | Variants in mitochondrial DNA | Maternal | See [[Mitochondrial DNA]] |
| Complex | Many variants plus environment | Raised risk in relatives, no Mendelian ratios (Exercise 5) | Common diseases studied by association[^visscher] |
| Somatic | Variants acquired in body cells | Not transmitted, although a predisposing allele can be | [[Cancer]] ([[Somatic Mutation]])[^alberts] |

### Monogenic versus complex

| | Monogenic | Complex |
|---|---|---|
| Genetic cause | Variants in one gene, sufficient on their own | Many contributing loci[^visscher] |
| Effect of one causal variant | Large | Small: in the liability model, each locus shifts risk slightly (Computational representation) |
| Population frequency of causal alleles | Bounded by the disease frequency: a variant too common for the disorder is evidence against causality[^richards] | Common and rare variants both contribute |
| How genes are found | Linkage in families, sequencing of patients ([[Genetic Linkage]]) | Association in large samples ([[Genome-Wide Association Study]]) |

The environment matters even for monogenic disease: phenylketonuria, a recessive deficiency in converting phenylalanine to tyrosine, causes intellectual disability unless affected children follow a low-phenylalanine diet ([[Newborn Screening]]).[^griffiths]

### Penetrance and expressivity

![[penetrance-expressivity-schematic.svg]]

- **Complete or incomplete penetrance.** With penetrance 1, every carrier is affected; below 1, some carriers are not, and a dominant disorder can skip a generation ([[Pedigree Analysis#Incomplete penetrance]]).[^griffiths]
- **Age-dependent penetrance.** For a late-onset disorder, penetrance is a function of age: the fraction of carriers affected by a given age.
- **Variable expressivity.** Affected carriers differ in severity, or in which features they show.[^griffiths]
- **Causes.** Other genes (modifiers, [[Epistasis]]), the environment and chance.[^griffiths]

**A quantified case: Huntington disease.** This dominant neurodegenerative disorder is caused by an expanded CAG repeat in the *HTT* gene, and its penetrance depends on the repeat length.[^griffiths][^kay] In 7,315 people from three population cohorts, Kay and colleagues found 18 carriers of 36 or more repeats (about 1 in 400), most with 36 to 38. For 37 and 38 repeats, they estimated the penetrance after age 65 at about 0.2 % and 2 %, far below the 10 % and 19 % extrapolated from clinical cohorts.[^kay] The same allele can thus look dangerous in a clinic and nearly harmless in the population (Advanced).

## Advanced (L3)

### Measuring penetrance, and its bias

Penetrance is estimated as the fraction of carriers who are affected, with the uncertainty of a binomial proportion (Computational representation). The hard part is **who the carriers are**. Carriers found through affected relatives belong to families selected because the disease appeared in them, which inflates the estimate; carriers found by genotyping unselected people give the population value, as the Huntington figures show ([[Selection Bias]]).[^kay] For a late-onset disorder, carriers too young to have developed the disease must also be handled, since they are not yet informative.

### One gene, several diseases; one disease, several genes

- **Allelic heterogeneity**: different variants of one gene can cause the same disease, or different ones.[^griffiths]
- **Locus heterogeneity**: variants in different genes can cause the same disease. Two parents with the same recessive disorder can then have unaffected children, when their mutations lie in different genes; this is the logic of the complementation test ([[Genetic Screen]]).[^griffiths]
- **Pleiotropy**: one gene can affect several traits, so one variant can cause a syndrome with several features.[^griffiths]

### The liability threshold model

Complex diseases are yes-or-no outcomes with many small causes. A useful model gives each person a continuous **liability**, the sum of many genetic contributions and an environmental term, and declares disease when liability exceeds a threshold (Mathematical representation). The model explains three observations: no single locus has a large effect; risk concentrates among people with many risk alleles, which is what a [[Polygenic Risk Score]] measures; and relatives of patients have raised risk, the more so the larger the genetic share of liability variance, its [[Heritability]] (Exercise 5).[^hartl]

## Frontier (M1)

- **Polygenicity.** Association studies showed that, for almost any complex trait studied, many loci contribute to the variation, which suggests a large mutational target in the genome.[^visscher] In the simulation below, no locus has an odds ratio above 1.45, yet the top decile of genetic score has a risk of 29 % against 5 % overall.
- **Penetrance at population scale.** Large sequenced cohorts reveal alleles called pathogenic in apparently healthy people; allele frequency is then evidence in its own right, since a variant too common for the disease is likely benign.[^richards][^kay]
- **From genetics to therapeutics.** Drug targets with human genetic support for their indication are enriched among approved drugs, an argument for building drug pipelines on genetic evidence.[^nelson]

## Mathematical representation

- **Penetrance function**: $f_g = P(D = 1 \mid G = g)$ for $g \in \{0, 1, 2\}$ copies of the risk allele. Fully penetrant dominant: $f = (0, 1, 1)$; fully penetrant recessive: $(0, 0, 1)$; incomplete penetrance: $f_1 = f_2 = \phi < 1$ for a dominant disorder; **phenocopies** (the disease without the genotype): $f_0 > 0$.
- **Prevalence** under [[Hardy-Weinberg Equilibrium]], with risk allele frequency $q$: $K = (1 - q)^2 f_0 + 2q(1 - q) f_1 + q^2 f_2$.
- **Age-dependent penetrance**: $f_g(t) = P(\text{onset} \le t \mid G = g)$, a cumulative distribution function in age $t$.
- **Estimation**: with $a$ affected among $n$ carriers, $\hat\phi = a/n$ and $\mathrm{SE} = \sqrt{\hat\phi(1 - \hat\phi)/n}$.
- **Association**: with risk-allele frequencies $f_A$ in cases and $f_U$ in controls, the allelic odds ratio is $\mathrm{OR} = \dfrac{f_A/(1 - f_A)}{f_U/(1 - f_U)}$.[^clarke]
- **Liability threshold model**: $L = \sum_{j=1}^{m} \beta_j X_j + E$, with $X_j \in \{0, 1, 2\}$ the allele count at locus $j$, $\beta_j$ its effect and $E \sim \mathcal N(0, \sigma_E^2)$; disease when $L > T$. For independent loci in Hardy-Weinberg proportions, the genetic variance is $V_G = \sum_j 2p_j(1 - p_j)\beta_j^2$ and the heritability of liability is $h^2 = V_G / (V_G + \sigma_E^2)$.[^hartl] With many small effects, $L$ is approximately normal ([[Central Limit Theorem]]), so $K = 1 - \Phi\left((T - \mu_L)/\sigma_L\right)$ with $\Phi$ the standard normal distribution function.

## Computational representation

Two computations: a penetrance estimate with its interval, and a simulation of the liability model showing how a complex disease looks in case-control data.

```python
import math
import random


def proportion_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    """Estimate and normal-approximation 95% interval for a proportion such as a penetrance."""
    p = k / n
    half = z * math.sqrt(p * (1 - p) / n)
    return round(p, 3), round(p - half, 3), round(p + half, 3)


def simulate_liability(n: int, m: int, p: float, beta: float, h2: float, rng: random.Random):
    """Polygenic liability model: m loci with allele frequency p and effect beta per allele,
    plus a normal environment sized so that a fraction h2 of liability variance is genetic."""
    var_g = m * 2 * p * (1 - p) * beta ** 2
    sd_e = math.sqrt(var_g * (1 - h2) / h2)
    people = []
    for _ in range(n):
        genotype = [(rng.random() < p) + (rng.random() < p) for _ in range(m)]
        score = beta * sum(genotype)
        people.append((genotype, score, score + rng.gauss(0, sd_e)))
    return people


def allelic_odds_ratio(cases, controls, j: int) -> float:
    def freq(group):
        return sum(x[0][j] for x in group) / (2 * len(group))
    fa, fu = freq(cases), freq(controls)
    return (fa / (1 - fa)) / (fu / (1 - fu))


# Monogenic: 30 of 120 carriers affected by age 70 (invented cohort)
print("penetrance", proportion_ci(30, 120))

# Complex: 200 loci of small effect, liability heritability 0.5, prevalence 5 %
rng = random.Random(7)
people = simulate_liability(n=5000, m=200, p=0.3, beta=0.1, h2=0.5, rng=rng)
threshold = sorted(x[2] for x in people)[int(0.95 * len(people))]
cases = [x for x in people if x[2] > threshold]
controls = [x for x in people if x[2] <= threshold]
ors = sorted(allelic_odds_ratio(cases, controls, j) for j in range(200))
print(len(cases), "cases; per-locus odds ratios: median", round(ors[100], 2), "max", round(ors[-1], 2))
ranked = sorted(people, key=lambda x: x[1])                      # by genetic score
for d in (1, 5, 10):
    decile = ranked[(d - 1) * 500:d * 500]
    print(f"score decile {d}: risk {sum(x[2] > threshold for x in decile) / 500:.3f}")
```

```text
penetrance (0.25, 0.173, 0.327)
249 cases; per-locus odds ratios: median 1.18 max 1.45
score decile 1: risk 0.000
score decile 5: risk 0.004
score decile 10: risk 0.290
```

With 120 carriers, the penetrance interval is still 0.17 to 0.33. In the polygenic model, every locus has a modest odds ratio, and none would explain the disease, yet the summed genetic score separates risk sharply. The invented parameters (200 equal loci) are a caricature of real architectures, where effects vary from locus to locus.

## Worked example

> [!example] Risk with incomplete penetrance (hypothetical values)
> An autosomal dominant disorder has penetrance 0.8. A woman's father is affected (heterozygous); she is unaffected, as is her partner, who has no family history.
> 1. **Before her phenotype is used**, she carries the allele with probability 1/2.
> 2. **Being unaffected lowers it** (Bayes, [[Pedigree Analysis#Incomplete penetrance]]): $\frac{1 - f}{2 - f} = \frac{0.2}{1.2} = \frac16$.
> 3. **Her child** inherits the allele with probability $\frac16 \times \frac12 = \frac1{12}$ and is affected with probability $\frac1{12} \times 0.8 = \frac1{15} \approx 0.067$.
> 4. **Compare** with the child of her affected brother: $\frac12 \times 0.8 = 0.4$.
> 5. **Expressivity** does not change these numbers, but it changes what "affected" means in counselling: the child may be mildly or severely affected.

## Common misconceptions

> [!warning] "Genetic means inherited"
> Somatic variants cause genetic disease, such as cancer, without being transmitted, and trisomy 21 arises from an error in a parent's meiosis rather than from a parent's genotype.[^alberts][^os13]

> [!warning] "A pathogenic variant means the person will get the disease"
> Only with complete penetrance. Penetrance can be low, depend on age, and be overestimated by clinical ascertainment: Huntington alleles of 37 repeats had an estimated penetrance of about 0.2 % after 65 in the general population.[^kay]

> [!warning] "Complex diseases are not genetic"
> They are partly genetic, with risk spread over many loci;[^visscher] relatives of patients have raised risk (Exercise 5) although no single variant determines the disease.

> [!warning] "A monogenic disease is fixed destiny"
> The environment can change the outcome: a low-phenylalanine diet prevents the intellectual disability of phenylketonuria.[^griffiths]

## Exercises

> [!question] Exercise 1 (L2)
> Classify each case as monogenic, chromosomal, mitochondrial, complex or somatic: (a) a disorder passed from mothers to all their children, never from fathers; (b) a disease twice as frequent in siblings of patients as in the population, without Mendelian ratios in families; (c) a child with three copies of chromosome 21; (d) a variant found in a tumour and absent from the patient's blood DNA; (e) a disorder affecting half of the children of affected parents, in both sexes, over several generations.

> [!success]- Solution
> (a) Mitochondrial (maternal transmission). (b) Complex: familial clustering without Mendelian segregation. (c) Chromosomal (aneuploidy).[^os13] (d) Somatic: acquired in the tumour lineage. (e) Monogenic, autosomal dominant.

> [!question] Exercise 2 (L2)
> Of 50 carriers of a dominant allele, 35 have the disorder: 20 mildly, 10 moderately and 5 severely (invented). Give the penetrance and describe the expressivity. A carrier has a sign detectable only by a specialist test: is that a penetrance or an expressivity question?

> [!success]- Solution
> Penetrance $35/50 = 0.7$. Expressivity: among the affected, 57 % mild, 29 % moderate, 14 % severe. The specialist-test case shows that both quantities depend on the definition of "affected": with a more sensitive criterion, this carrier counts as affected (higher penetrance) and expressivity shifts toward milder forms. Always report the diagnostic criterion with a penetrance.

> [!question] Exercise 3 (L2)
> Under Hardy-Weinberg proportions and no phenocopies, compute the prevalence of (a) a fully penetrant recessive disorder with $q = 0.01$, and (b) a dominant disorder with risk-allele frequency $q = 0.0005$ and penetrance 0.6 in carriers.

> [!success]- Solution
> (a) $K = q^2 = 0.0001$, 1 in 10,000. (b) $K = (2q(1 - q) + q^2) \times 0.6 = 0.0005999 \approx 0.0006$, 6 in 10,000; homozygotes contribute almost nothing.

> [!question] Exercise 4 (L3)
> Using Kay and colleagues' figures, compute for one million people aged 65 or older the expected number of carriers of 37 and of 38 CAG repeats, and the expected number of affected carriers under the population penetrance (0.2 %, 2.0 %) and under the clinical estimates (10 %, 19 %). Explain the difference.

> [!success]- Solution
> Carriers: $0.082\,\% \times 10^6 = 820$ with 37 repeats and $0.027\,\% \times 10^6 = 270$ with 38.[^kay] Affected, population penetrance: $820 \times 0.002 = 1.6$ and $270 \times 0.02 = 5.4$; clinical estimates: 82 and 51.3. Clinical cohorts are assembled from families in which the disease appeared, so they over-represent carriers who became ill; most carriers of these alleles in the population never come to a clinic. The difference is ascertainment bias, not biology.

> [!question] Exercise 5 (L3, Python)
> In the liability model, full sibs share half of the genetic variance of liability. Simulate pairs of sibs for a disease of prevalence 5 % with liability heritability 0, 0.5 and 0.8, and compute the risk to a sib of a patient and the ratio $\lambda_s$ of this risk to the prevalence.

> [!success]- Solution
> ```python
> from statistics import NormalDist
>
> def sibling_recurrence(h2: float, prevalence: float, families: int, rng: random.Random) -> float:
>     """Liability model for full sibs: half of the genetic variance is shared, half is not."""
>     t = NormalDist().inv_cdf(1 - prevalence)      # threshold on a standard normal liability
>     both = first = 0
>     for _ in range(families):
>         shared = rng.gauss(0, math.sqrt(h2 / 2))
>         l1 = shared + rng.gauss(0, math.sqrt(h2 / 2)) + rng.gauss(0, math.sqrt(1 - h2))
>         l2 = shared + rng.gauss(0, math.sqrt(h2 / 2)) + rng.gauss(0, math.sqrt(1 - h2))
>         if l1 > t:
>             first += 1
>             both += l2 > t
>     return both / first
>
> rng = random.Random(11)
> for h2 in (0.0, 0.5, 0.8):
>     risk = sibling_recurrence(h2, 0.05, 200_000, rng)
>     print(h2, round(risk, 3), round(risk / 0.05, 1))
> # 0.0 0.047 0.9
> # 0.5 0.122 2.4
> # 0.8 0.187 3.7
> ```
>
> Without genetic variance, a sib's risk is the prevalence (0.047 is sampling noise around 0.05). With $h^2 = 0.5$ it rises to 12 % ($\lambda_s \approx 2.4$), with $h^2 = 0.8$ to 19 % ($\lambda_s \approx 3.7$): familial clustering without any Mendelian ratio, as in complex diseases. The model assumes additive effects and no environment shared by sibs.

> [!question] Exercise 6 (M1)
> A variant reported as the cause of a dominant disorder of prevalence 1 in 10,000 is carried by 1 in 300 healthy adults in a population database. What is the largest penetrance compatible with these numbers? Give three explanations and say how the observation should weigh in the variant's classification.

> [!success]- Solution
> Even if the variant caused every case, prevalence $\ge$ carrier frequency $\times$ penetrance gives $\phi \le (1/10{,}000)/(1/300) = 0.03$. Explanations: the variant is benign and was misclassified (for example from one family with another cause); it has very low penetrance, perhaps needing modifiers or a second hit; or the database population differs from the patients' one, with a frequency specific to it. An allele frequency greater than expected for the disorder is evidence for a benign classification in the ACMG/AMP framework.[^richards]

## Mastery checklist

- [ ] 1 Recognized: I can name the classes of genetic disease and define penetrance and expressivity.
- [ ] 2 Understood: I can contrast monogenic and complex diseases (cause, family pattern, allele frequencies, mapping method) and explain why penetrance can be incomplete or age-dependent.
- [ ] 3 Practiced: I can compute prevalences, penetrance estimates with intervals and risks with incomplete penetrance, and simulate the liability model in Python.
- [ ] 4 Applied: I looked up a disease variant in ClinVar, compared its frequency in a population database with the disease prevalence, and judged whether the penetrance is plausible.
- [ ] 5 Explained: I can teach ascertainment bias in penetrance, allelic and locus heterogeneity, and how polygenic architecture shapes association studies and polygenic scores.

## References

[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), human genetics and gene interaction: penetrance and expressivity and their causes (modifier genes, environment), phenylketonuria, genetic heterogeneity and complementation in human pedigrees, pleiotropy, Huntington disease as a dominant disorder.
[^mit703]: [[MIT 7.03 - Genetics]], human genetics part: inherited disease.
[^os13]: [[Biology 2e (OpenStax)]], section 13.2 "Chromosomal Basis of Inherited Disorders" (nondisjunction, aneuploidy, trisomy 21).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), cancer as a disease of somatic mutations, and inherited predisposition through one mutant copy of a tumour suppressor gene.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), quantitative traits: partition of phenotypic variance, heritability.
[^clinvar]: [[ClinVar]], variation 15333, `NM_000518.5(HBB):c.20A>T (p.Glu7Val)`, rs334, the sickle-cell allele.
[^richards]: [[Richards 2015 - Standards and Guidelines for the Interpretation of Sequence Variants]], *Genetics in Medicine* 17(5):405-424: five-tier terminology; population data, segregation and de novo criteria.
[^kay]: [[Kay 2016 - Huntington Disease Reduced Penetrance Alleles Occur at High Frequency in the General Population]], *Neurology* (July 2016) 282-288.
[^visscher]: [[Visscher 2017 - 10 Years of GWAS Discovery]], *American Journal of Human Genetics* 101(1):5-22.
[^clarke]: [[Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies]], *Nature Protocols* 6(2):121-133, measures of association (odds ratios).
[^nelson]: [[Nelson 2015 - The Support of Human Genetic Evidence for Approved Drug Indications]], *Nature Genetics* 47(8):856-860.
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], *Nature* 488:471-475.
