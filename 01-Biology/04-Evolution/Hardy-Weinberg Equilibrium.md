---
aliases:
  - Hardy-Weinberg Principle
  - Hardy-Weinberg Law
  - Hardy-Weinberg Proportions
  - HWE
  - Équilibre de Hardy-Weinberg
tags:
  - type/concept
  - domain/biology
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Allele Frequency]]"
  - "[[Genotype]]"
  - "[[Mendelian Inheritance]]"
  - "[[Meiosis]]"
  - "[[Chi-Square Test]]"
related:
  - "[[Heterozygosity]]"
  - "[[Inbreeding]]"
  - "[[Genetic Drift]]"
  - "[[Natural Selection]]"
  - "[[Gene Flow]]"
  - "[[Population Structure]]"
  - "[[Fixation Index]]"
  - "[[Linkage Disequilibrium]]"
  - "[[Sex-Linked Inheritance]]"
  - "[[Genotype Likelihood]]"
  - "[[Fisher's Exact Test]]"
  - "[[Variant Filtering]]"
  - "[[Genome-Wide Association Study]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Hardy 1908 - Mendelian Proportions in a Mixed Population]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Wigginton 2005 - A Note on Exact Tests of Hardy-Weinberg Equilibrium]]"
---

# Hardy-Weinberg Equilibrium

> [!abstract]
> Under random mating, genotype frequencies follow from allele frequencies alone, $p^2$, $2pq$ and $q^2$, after a single generation, and stay there while nothing changes the allele frequencies; departures from these proportions point to non-random mating, mixed populations, selection or genotyping errors.

## Definition

In a large population with random mating and no selection, mutation or migration, allele frequencies stay constant from generation to generation, and after one generation of random mating the genotype frequencies at an autosomal locus with allele frequencies $p$ and $q = 1 - p$ are $p^2$ (AA), $2pq$ (Aa) and $q^2$ (aa): the **Hardy-Weinberg proportions**.[^hartl][^griffiths][^os19] The mathematician G. H. Hardy and the physician Wilhelm Weinberg stated the principle independently in 1908.[^os19][^hardy]

## Why it matters

- **Genotype quality control.** Departures from Hardy-Weinberg proportions can indicate inbreeding, population stratification and genotyping problems, and, in samples of affected individuals, association with the disease.[^wigginton] Pipelines therefore test every variant, usually in controls, and flag strong departures ([[Variant Filtering]], [[Genome-Wide Association Study]]).
- **Priors for genotype calling.** The proportions $(1-p)^2$, $2p(1-p)$, $p^2$ at the population ALT frequency are a standard prior when reads alone are ambiguous ([[Genotype#Advanced (L3)]], [[Genotype Likelihood]]).
- **From allele to genotype frequencies.** Carrier frequencies of recessive diseases, expected numbers of homozygotes in a cohort, and the genotypes that [[07-evolution-simulator]] draws each generation all come from $p^2, 2pq, q^2$ (Exercise 3).
- **The null model of population genetics.** With nothing acting, nothing changes: each evolutionary force is defined by how it moves a population away from this baseline ([[Natural Selection]], [[Genetic Drift]], [[Gene Flow]], [[Inbreeding]]).[^hartl]

## Core (L2)

### Derivation: random union of gametes

Start from any genotype frequencies $P$, $H$, $Q$ (AA, Aa, aa), with allele frequency $p = P + H/2$ ([[Allele Frequency]]). By segregation, each gamete carries A with probability $p$ ([[Mendelian Inheritance]], [[Meiosis]]); under random mating, the two gametes that form a zygote are independent draws from the gamete pool:

| Egg \ sperm | A ($p$) | a ($q$) |
|---|---|---|
| **A** ($p$) | AA: $p^2$ | Aa: $pq$ |
| **a** ($q$) | aA: $qp$ | aa: $q^2$ |

The offspring are AA with probability $p^2$, Aa with $2pq$ (two cells of the table) and aa with $q^2$, which sum to $(p + q)^2 = 1$. Their allele frequency is $p' = p^2 + pq = p(p + q) = p$: unchanged. One generation of random mating therefore produces the proportions, and every later generation repeats them.[^hartl][^griffiths]

![[hardy-weinberg-genotype-frequencies.svg]]

Two features of the curves matter in practice. Heterozygosity $2pq$ is at most 0.5, reached at $p = 0.5$ ([[Heterozygosity]]). And when an allele is rare, its copies sit almost entirely in heterozygotes: at $q = 0.1$, the fraction of a copies carried by Aa individuals is $2pq / (2pq + 2q^2) = p = 0.9$.

### Hardy's stability condition

Hardy wrote the genotype proportions as $p : 2q : r$ and showed that they are stable under random mating if and only if $q^2 = pr$.[^hardy] In the notation above, $(H/2)^2 = PQ$, which $p^2$, $2pq$, $q^2$ satisfy since $(pq)^2 = p^2 q^2$. His letter answered the argument that a dominant character should become more common simply because it is dominant: under random mating, frequencies stay where they are.[^hardy] A population with $P = Q = 0.36$, $H = 0.28$ is not at equilibrium ($0.14^2 \ne 0.36^2$); one generation of random mating turns it into 0.25, 0.50, 0.25 (Exercise 2).

### What the assumptions mean

| Assumption | Violation | Signature in genotype counts |
|---|---|---|
| Random mating | inbreeding, assortative mating | excess of homozygotes ([[Inbreeding]])[^hartl] |
| One population | pooling subpopulations with different $p$ | heterozygote deficit in the pooled sample, the Wahlund effect ([[Population Structure]])[^hartl] |
| No selection | genotype-dependent survival | departures among survivors; in cases, possible association[^wigginton] |
| Large population, no mutation or migration | drift, mutation, gene flow | allele frequencies change between generations ([[Genetic Drift]], [[Gene Flow]]) |
| Correct genotypes (a data assumption) | heterozygotes called homozygous; reads of two paralogous copies merged into one locus | heterozygote deficit; heterozygote excess[^wigginton] |

### Testing a sample

Estimate $\hat p$ by gene counting, compute the expected counts $n\hat p^2$, $2n\hat p\hat q$, $n\hat q^2$, and compare them with the observed counts.

- **Chi-square test.** The goodness-of-fit statistic has 1 degree of freedom (3 classes, minus 1 for the total, minus 1 for the estimated $p$); it is worked on two invented samples in [[Chi-Square Test#Core (L1)]], with the identity $X^2 = n\hat F^2$ linking it to the heterozygote deficit $\hat F$ ([[Chi-Square Test#Advanced (L3)]]).
- **Exact test.** With a rare minor allele, expected homozygote counts fall far below 5, and the chi-square test can have inflated type I error even in fairly large samples. The exact test conditions on the allele counts and uses the exact probability of each heterozygote count under Hardy-Weinberg proportions; efficient algorithms make it practical for genome-wide data.[^wigginton] The Worked example shows the two tests disagreeing.

## Advanced (L3)

- **Several alleles.** Under random mating, $A_iA_i$ has frequency $p_i^2$ and $A_iA_j$ ($i \ne j$) has $2p_ip_j$.[^hartl] With $k$ alleles there are $k(k+1)/2$ genotypes and $k - 1$ free allele frequencies, so the goodness-of-fit test has $k(k+1)/2 - 1 - (k - 1) = k(k-1)/2$ degrees of freedom.
- **X-linked loci.** Females have $p^2, 2pq, q^2$ and hemizygous males $p, q$ ([[Sex-Linked Inheritance]]). If the frequencies differ between the sexes, a son's X comes from his mother and a daughter's from both parents: $p_m' = p_f$, $p_f' = (p_f + p_m)/2$. The difference $d = p_f - p_m$ becomes $-d/2$ each generation, so equilibrium is approached in damped oscillations rather than in one step.[^hartl]
- **Two loci.** One generation of random mating does not make haplotype frequencies equal to products of allele frequencies: the linkage disequilibrium $D$ decays by a factor $1 - r$ per generation, with $r$ the recombination fraction ([[Linkage Disequilibrium]]).[^hartl]
- **Wahlund effect, quantified.** Pool equal samples of subpopulations, each at Hardy-Weinberg proportions, with allele frequencies $p_s$ of mean $\bar p$ and variance $\sigma_p^2$. The pooled heterozygote frequency is $\overline{2p_sq_s} = 2\bar p\bar q - 2\sigma_p^2$: a deficit of $2\sigma_p^2$ relative to $2\bar p\bar q$ (Exercise 6), which is what $F_{ST}$ standardizes ([[Fixation Index]]).
- **Low depth fakes inbreeding.** At depth $d$, a heterozygote shows only one of its alleles with probability $2 \times 0.5^d$ (ignoring errors): 12.5% at $d = 4$. Hard calls from shallow data therefore produce heterozygote deficits that are technical, one reason to work with genotype likelihoods ([[Genotype Likelihood]]).
- **Scale changes the meaning of p-values.** Since $X^2 = n\hat F^2$, a biobank-sized sample detects departures far too small to matter; QC thresholds are set study by study, and a departure confined to cases can be a real association signal rather than an error.[^wigginton]

## Mathematical representation

- **Random union of gametes.** Gametes carry allele $A_i$ with probability $p_i$, independently; the unordered genotype $\{A_i, A_j\}$ has probability $p_i^2$ if $i = j$ and $2p_ip_j$ otherwise.
- **Recurrence.** $p_{t+1} = P_{t+1} + H_{t+1}/2 = p_t^2 + p_tq_t = p_t$: allele frequencies are a conserved quantity of random mating.
- **Equilibrium set.** With $P + H + Q = 1$, the Hardy-Weinberg genotype frequencies are exactly those with $H^2 = 4PQ$ (Hardy's $q^2 = pr$); in a triangular plot of $(P, H, Q)$, the de Finetti diagram, this set is a parabola.[^hartl]
- **Exact distribution.** For $n$ individuals carrying $n_a$ copies of the minor allele, the number of heterozygotes $n_{Aa}$ has the same parity as $n_a$, and under Hardy-Weinberg proportions[^wigginton]
$$P(n_{Aa} \mid n, n_a) = \frac{n!}{n_{AA}!\,n_{Aa}!\,n_{aa}!}\; 2^{n_{Aa}}\; \frac{n_a!\,(2n - n_a)!}{(2n)!},$$
with $n_{aa} = (n_a - n_{Aa})/2$ and $n_{AA} = n - n_{Aa} - n_{aa}$. The exact p-value is the sum of $P(k \mid n, n_a)$ over all heterozygote counts $k$ with $P(k \mid n, n_a) \le P(n_{Aa}^{\text{obs}} \mid n, n_a)$.[^wigginton]
- **Heterozygote deficit.** $\hat F = 1 - n_{Aa}/(2n\hat p\hat q)$ is 0 at equilibrium, positive for a deficit and negative for an excess ([[Inbreeding]]).

## Computational representation

Both tests in the standard library. The exact probabilities are computed in log space with `lgamma`, because factorials of thousands overflow floating point.

```python
from math import erfc, exp, lgamma, log, sqrt


def hwe_expected(n_AA: int, n_Aa: int, n_aa: int) -> tuple[float, tuple[float, float, float]]:
    """Allele frequency of A and expected genotype counts under Hardy-Weinberg proportions."""
    n = n_AA + n_Aa + n_aa
    p = (2 * n_AA + n_Aa) / (2 * n)
    q = 1 - p
    return p, (n * p * p, 2 * n * p * q, n * q * q)


def hwe_chi2(n_AA: int, n_Aa: int, n_aa: int) -> tuple[float, float]:
    """Pearson statistic (1 df) and its p-value, P(chi2_1 >= x) = erfc(sqrt(x / 2))."""
    _, expected = hwe_expected(n_AA, n_Aa, n_aa)
    x2 = sum((o - e) ** 2 / e for o, e in zip((n_AA, n_Aa, n_aa), expected))
    return x2, erfc(sqrt(x2 / 2))


def het_probabilities(n: int, n_minor: int) -> dict[int, float]:
    """P(n_het | n individuals, n_minor minor-allele copies) under Hardy-Weinberg proportions."""
    probs = {}
    for het in range(n_minor % 2, n_minor + 1, 2):        # n_het has the parity of n_minor
        hom_minor = (n_minor - het) // 2
        hom_major = n - het - hom_minor
        if hom_major < 0:
            continue
        log_p = (lgamma(n + 1) - lgamma(hom_major + 1) - lgamma(het + 1) - lgamma(hom_minor + 1)
                 + het * log(2) + lgamma(n_minor + 1) + lgamma(2 * n - n_minor + 1)
                 - lgamma(2 * n + 1))
        probs[het] = exp(log_p)
    return probs


def hwe_exact(n_AA: int, n_Aa: int, n_aa: int) -> float:
    """Exact test: total probability of heterozygote counts no more likely than the observed one."""
    n = n_AA + n_Aa + n_aa
    n_minor = min(2 * n_AA + n_Aa, 2 * n_aa + n_Aa)
    probs = het_probabilities(n, n_minor)
    return sum(pr for pr in probs.values() if pr <= probs[n_Aa] * (1 + 1e-7))


samples = {"common": (380, 440, 180), "rare_1hom": (489, 10, 1), "rare_0hom": (490, 10, 0)}
for name, counts in samples.items():                     # invented genotype counts AA, Aa, aa
    p, expected = hwe_expected(*counts)
    x2, p_chi2 = hwe_chi2(*counts)
    print(f"{name:10s} p={p:.3f} expected={tuple(round(e, 2) for e in expected)} "
          f"X2={x2:.2f} p_chi2={p_chi2:.2g} p_exact={hwe_exact(*counts):.2g}")
print(round(sum(het_probabilities(500, 12).values()), 12))
print({h: round(pr, 4) for h, pr in het_probabilities(500, 12).items()})
```

```text
common     p=0.600 expected=(360.0, 480.0, 160.0) X2=6.94 p_chi2=0.0084 p_exact=0.0084
rare_1hom  p=0.988 expected=(488.07, 11.86, 0.07) X2=12.25 p_chi2=0.00046 p_exact=0.065
rare_0hom  p=0.990 expected=(490.05, 9.9, 0.05) X2=0.05 p_chi2=0.82 p_exact=1
1.0
{0: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, 8: 0.0014, 10: 0.0631, 12: 0.9354}
```

For the common variant (a heterozygote deficit of 40) both tests agree. The tolerance `1 + 1e-7` keeps heterozygote counts whose probability equals the observed one despite rounding; the probabilities sum to 1, as a distribution must.

## Worked example

> [!example] One rare homozygote among 500 people (invented counts)
> Genotypes at a SNP: 489 AA, 10 Aa, 1 aa.
> 1. **Allele frequency**: the minor allele a has $10 + 2 \times 1 = 12$ copies among 1,000, so $\hat q = 0.012$.
> 2. **Expected counts**: aa $= 500 \times 0.012^2 = 0.072$, Aa $= 500 \times 2 \times 0.012 \times 0.988 = 11.86$, AA $= 488.07$.
> 3. **Chi-square**: the aa cell alone contributes $(1 - 0.072)^2/0.072 = 11.96$; in total $X^2 = 12.25$, $p = 0.00046$. The test "rejects", but an expected count of 0.07 breaks its large-count condition ([[Chi-Square Test#Core (L1)]]).
> 4. **Exact test**: with 12 minor copies fixed, the possible outcomes are (12 Aa, 0 aa) with probability 0.9354, (10, 1) with 0.0631, (8, 2) with 0.0014, and fewer heterozygotes with negligible probability. The observed (10, 1) and every less likely outcome sum to $p = 0.065$.
> 5. **Conclusion**: no evidence against Hardy-Weinberg proportions. A single rare homozygote is what random mating produces about 6% of the time; filtering this variant on the chi-square p-value would discard a good site.

## Common misconceptions

> [!warning] "Hardy-Weinberg proportions are 1:2:1"
> 1:2:1 is the offspring ratio of a cross Aa × Aa ([[Mendelian Inheritance]]). Hardy-Weinberg proportions are $p^2 : 2pq : q^2$ and equal 1:2:1 only when $p = 0.5$.

> [!warning] "A dominant allele spreads because it is dominant"
> Dominance describes the phenotype of heterozygotes ([[Dominance]]); it does not change allele frequencies. This is precisely the argument Hardy's 1908 letter refuted.[^hardy]

> [!warning] "A non-significant test proves random mating and no selection"
> One generation of random mating restores the proportions whatever happened before, so they say little about past drift, selection or migration. And power is low: since $X^2 = n\hat F^2$, detecting $F = 0.05$ at the 5% level needs $n\hat F^2 \ge 3.84$, about 1,500 individuals.

> [!warning] "Every departure is biological"
> In genotype data, strong departures at single sites are often genotyping problems,[^wigginton] which is why they are filters before they are findings. Biological causes (inbreeding, structure) affect all loci of the genome, not one site.

## Exercises

> [!question] Exercise 1 (L2)
> In a randomly mating population, $p = 0.3$. Give the genotype frequencies and the expected counts among 500 individuals.

> [!success]- Solution
> AA $= 0.09$, Aa $= 2 \times 0.3 \times 0.7 = 0.42$, aa $= 0.49$; expected counts 45, 210, 245. Check: $0.09 + 0.42 + 0.49 = 1$.

> [!question] Exercise 2 (L2)
> A population has $P = 0.36$, $H = 0.28$, $Q = 0.36$. Use Hardy's condition to decide whether it is at equilibrium, then give the genotype frequencies after one generation of random mating.

> [!success]- Solution
> $(H/2)^2 = 0.0196 \ne PQ = 0.1296$: not at equilibrium (too few heterozygotes). $p = 0.36 + 0.14 = 0.5$, so the next generation is 0.25, 0.50, 0.25, and it stays there. The allele frequency did not change; only its packaging into genotypes did.

> [!question] Exercise 3 (L2)
> A recessive disease affects 1 newborn in 10,000 (invented incidence). Assuming Hardy-Weinberg proportions, estimate the allele frequency, the carrier frequency and the number of carriers per affected person.

> [!success]- Solution
> $q^2 = 10^{-4}$, so $q = 0.01$; carriers $2pq = 2 \times 0.99 \times 0.01 = 0.0198$, about 1 in 51; carriers per affected $= 0.0198 / 0.0001 = 198$. A fraction $p = 0.99$ of the disease allele copies is in healthy carriers, which is why selection against affected individuals barely changes $q$. Consanguinity raises the number of affected above $q^2$, so the estimate assumes random mating.

> [!question] Exercise 4 (L2, Python)
> Without assuming random union of gametes, enumerate the 9 ordered matings between individuals of genotype frequencies $P$, $H$, $Q$, with Mendelian segregation, and check with exact fractions that a population of 60% AA and 40% aa reaches Hardy-Weinberg proportions in one generation and stays there.

> [!success]- Solution
> ```python
> from fractions import Fraction as Fr
> from itertools import product
>
>
> def next_generation(P: Fr, H: Fr, Q: Fr) -> dict[str, Fr]:
>     """Offspring genotype frequencies when individuals mate at random (9 ordered matings)."""
>     parents = {"AA": P, "Aa": H, "aa": Q}
>     gametes = {"AA": {"A": Fr(1)}, "Aa": {"A": Fr(1, 2), "a": Fr(1, 2)}, "aa": {"a": Fr(1)}}
>     child = {"AA": Fr(0), "Aa": Fr(0), "aa": Fr(0)}
>     for (g1, f1), (g2, f2) in product(parents.items(), repeat=2):
>         for (a1, x1), (a2, x2) in product(gametes[g1].items(), gametes[g2].items()):
>             child["".join(sorted(a1 + a2))] += f1 * f2 * x1 * x2     # 'aA' -> 'Aa'
>     return child
>
>
> gen = {"AA": Fr(3, 5), "Aa": Fr(0), "aa": Fr(2, 5)}      # no heterozygotes, p = 3/5
> for t in range(3):
>     print(t, {g: str(f) for g, f in gen.items()})
>     gen = next_generation(gen["AA"], gen["Aa"], gen["aa"])
> ```
> ```text
> 0 {'AA': '3/5', 'Aa': '0', 'aa': '2/5'}
> 1 {'AA': '9/25', 'Aa': '12/25', 'aa': '4/25'}
> 2 {'AA': '9/25', 'Aa': '12/25', 'aa': '4/25'}
> ```
> $9/25 = 0.6^2$, $12/25 = 2 \times 0.6 \times 0.4$, $4/25 = 0.4^2$: random mating of individuals gives the same result as random union of gametes, because each parent's gamete is drawn independently of the other parent's.

> [!question] Exercise 5 (L3, Python)
> Continuing the code above, take 200 individuals carrying 10 copies of the minor allele. Under Hardy-Weinberg proportions, how often does each test reject at the 5% level? Which heterozygote counts are rejected?

> [!success]- Solution
> ```python
> n, n_minor = 200, 10                       # 200 people, 10 copies of the minor allele
> rejected = {"exact": [], "chi2": []}
> size = {"exact": 0.0, "chi2": 0.0}
> for het, pr in het_probabilities(n, n_minor).items():
>     hom_minor = (n_minor - het) // 2
>     counts = (n - het - hom_minor, het, hom_minor)
>     for test, p_value in (("exact", hwe_exact(*counts)), ("chi2", hwe_chi2(*counts)[1])):
>         if p_value < 0.05:
>             rejected[test].append(het)
>             size[test] += pr
> print(rejected, {t: round(s, 4) for t, s in size.items()})
> ```
> ```text
> {'exact': [0, 2, 4, 6], 'chi2': [0, 2, 4, 6, 8]} {'exact': 0.0039, 'chi2': 0.1089}
> ```
> The chi-square test also rejects 8 heterozygotes with one rare homozygote, and its real type I error is 10.9%, more than twice the nominal 5%. The exact test never exceeds 5% by construction; here it is conservative (0.4%) because only six outcomes are possible. With millions of rare variants, the chi-square inflation turns into thousands of good sites wrongly filtered.

> [!question] Exercise 6 (L3)
> Two subpopulations of equal size are each at Hardy-Weinberg proportions, with $p_1 = 0.2$ and $p_2 = 0.8$. A study samples them together without knowing it. Compute the observed heterozygosity of the pooled sample, the heterozygosity expected from its allele frequency, and check the deficit against $2\sigma_p^2$.

> [!success]- Solution
> Each subpopulation has $2 \times 0.2 \times 0.8 = 0.32$ heterozygotes, so the pooled sample has 0.32. Its allele frequency is $\bar p = 0.5$, which predicts $2 \times 0.5 \times 0.5 = 0.50$. Deficit: 0.18. With $\sigma_p^2 = [(0.2 - 0.5)^2 + (0.8 - 0.5)^2]/2 = 0.09$, $2\sigma_p^2 = 0.18$. The pooled sample looks inbred ($\hat F = 1 - 0.32/0.50 = 0.36$) although every mating was random: a heterozygote deficit is a clue to [[Population Structure]] as much as to [[Inbreeding]].

## Mastery checklist

- [ ] 1 Recognized: I can state $p^2$, $2pq$, $q^2$ and the conditions under which they hold.
- [ ] 2 Understood: I can derive the proportions from random union of gametes, explain why one generation suffices, and say what each violated assumption does to genotype counts.
- [ ] 3 Practiced: I can test a sample with the chi-square and the exact test, implement both, and recognize when the chi-square fails.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I tested real variants in controls, inspected the failing sites, and in [[07-evolution-simulator]] I drew genotypes from allele frequencies each generation.
- [ ] 5 Explained: I can teach the Wahlund effect, the X-linked and two-locus approaches to equilibrium, and why a p-value alone is a poor QC criterion at biobank scale.

## References

[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), treatment of random mating (Hardy-Weinberg proportions and their assumptions, multiple alleles, X-linked loci, de Finetti diagrams, approach to linkage equilibrium, heterozygote deficits from inbreeding and population subdivision).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), population genetics (random mating and Hardy-Weinberg equilibrium).
[^os19]: [[Biology 2e (OpenStax)]], ch. 19 "The Evolution of Populations", section "Population Evolution" (the Hardy-Weinberg principle of equilibrium, Hardy and Weinberg).
[^hardy]: [[Hardy 1908 - Mendelian Proportions in a Mixed Population]], *Science* 28:49-50.
[^wigginton]: [[Wigginton 2005 - A Note on Exact Tests of Hardy-Weinberg Equilibrium]], *American Journal of Human Genetics* 76:887-893.
