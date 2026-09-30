---
aliases:
  - Haploid
  - Diploid
  - Polyploid
  - Polyploidy
  - Ploïdie
  - Chromosome Set
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Chromosome]]"
  - "[[Genome]]"
  - "[[Meiosis]]"
related:
  - "[[Allele]]"
  - "[[Genotype]]"
  - "[[Sex-Linked Inheritance]]"
  - "[[Copy Number Variation]]"
  - "[[Genotype Likelihood]]"
  - "[[Variant Calling]]"
  - "[[K-mer Spectrum]]"
  - "[[Binomial Distribution]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[HTS Format Specifications]]"
  - "[[Mangs 2007 - The Human Pseudoautosomal Region]]"
---

# Ploidy

> [!abstract]
> Ploidy is the number of complete chromosome sets in a cell: one in a haploid cell, two in a diploid cell, more in a polyploid one, and therefore the number of alleles a cell carries at each locus.

## Definition

**Ploidy** is the number of complete sets of chromosomes in a cell. A **haploid** cell contains one set (written $n$) and a **diploid** cell two sets ($2n$).[^os11] A **polyploid** organism has more than the normal number of chromosome sets (more than two for a diploid species): triploid ($3n$), tetraploid ($4n$), and so on.[^os13] Because each set carries one copy of every locus, ploidy fixes how many alleles a genotype contains.

## Why it matters

- **Variant callers need it.** A genotype has as many alleles as the ploidy at that locus; the VCF genotype field writes one allele per copy, and a single allele for haploid calls on the Y, the male non-pseudoautosomal X or the mitochondrion ([[Genotype]], [[VCF Format]]).[^hts] Calling a haploid region with a diploid model invents heterozygotes.
- **Allele fractions in reads follow ploidy.** A heterozygous site is expected at 50% of reads in a diploid, but at 25%, 50% or 75% in a tetraploid; the likelihood of each genotype is computed with the ploidy as a parameter ([[Genotype Likelihood]], [[Variant Calling]], [[10-genomic-pipeline]]).
- **Copy number is local ploidy.** Deletions and duplications change the number of copies of a region, the subject of [[Copy Number Variation]].
- **Genome size is quoted per set.** Genome sizes are haploid (1C) values; a diploid nucleus holds twice as much DNA ([[Genome]]).

## Core (L1)

![[ploidy-chromosome-sets.svg]]

**Haploid and diploid.** Human body cells are diploid: 23 pairs of chromosomes, $2n = 46$, one set from each parent ([[Chromosome]]).[^os11][^os13] Meiosis halves the number of sets, producing haploid gametes ($n = 23$), and fertilization restores the diploid number ([[Meiosis]]).[^os11]

**Alleles per locus.** In a diploid, the two homologs each carry one copy of every locus, so a genotype has two alleles: identical (homozygous) or different (heterozygous) ([[Genotype]]).[^os12] In general, at a locus present on $k$ chromosome sets, a genotype has $k$ alleles:

| Ploidy | Sets | Alleles per genotype | Genotypes with alleles A, a | Expected fraction of a among copies |
|---|---|---:|---|---|
| haploid | $n$ | 1 | A, a | 0, 1 |
| diploid | $2n$ | 2 | AA, Aa, aa | 0, 1/2, 1 |
| triploid | $3n$ | 3 | AAA, AAa, Aaa, aaa | 0, 1/3, 2/3, 1 |
| tetraploid | $4n$ | 4 | AAAA to aaaa (5 genotypes) | 0, 1/4, 1/2, 3/4, 1 |

**Polyploidy versus aneuploidy.** Polyploidy adds whole sets. **Aneuploidy** changes the number of individual chromosomes (for example a trisomy, $2n + 1$), usually with severe consequences; most aneuploidies are lethal to the embryo ([[Chromosome#Deeper (L2)]]).[^os13] Polyploids with an odd number of sets are rare because they are sterile: one set has no partner, so meiosis cannot proceed normally.[^os13]

## Deeper (L2)

### Ploidy varies along one genome

Ploidy is a property of each locus as much as of a cell. In a human male, the X and Y share only two small pseudoautosomal regions, which pair at meiosis;[^mangs] for genes in the differential region of the X he has one copy (**hemizygous**), and the same holds for the Y ([[Sex-Linked Inheritance]]).[^griffiths] The VCF specification reflects this with haploid calls on the Y, on the male non-pseudoautosomal X and on the mitochondrion.[^hts] A variant-calling pipeline therefore needs the sex of each sample and a map of the pseudoautosomal regions.

### Counting genotypes

With $k$ copies and $A$ possible alleles, a genotype is an unordered choice of $k$ alleles with repetition (a multiset), so there are
$$N(k, A) = \binom{A + k - 1}{k}$$
genotypes: 3 for a diploid biallelic site, 6 for a diploid site with three alleles, 5 for a tetraploid biallelic site (see the code below). The allele **dosage**, the number of copies of the alternative allele, runs from 0 to $k$.

### Reading ploidy from sequencing data

If a locus has $k$ copies, $j$ of them carrying the alternative allele, reads sample copies at random, so the number of ALT reads among $d$ is approximately **binomial** with probability $j/k$ ([[Binomial Distribution]]). The same observation, say 12 ALT reads out of 40, supports different dosages depending on $k$ (Worked example): ploidy is a prior assumption of the genotype model, not something the reads at one site reveal.

## Advanced (L3)

- **K-mer spectra.** In the reads of a diploid genome sequenced at coverage $c$, k-mers present on both homologs appear at depth about $c$, while k-mers that overlap a heterozygous site are present on one homolog only and appear at about $c/2$. The histogram of k-mer depths therefore has a peak at $c/2$ whose height grows with heterozygosity; in a tetraploid, peaks can appear at $c/4$, $c/2$, $3c/4$ and $c$. Reading ploidy and heterozygosity from these peaks is the idea behind k-mer profiling of raw reads ([[K-mer Spectrum]]).
- **Mixtures of cells.** A tissue sample can mix cells with different copy numbers, as in a tumour sample containing normal cells ([[Somatic Mutation]]). If a fraction $\pi$ of cells has $P$ copies of a locus, $m$ of them carrying a variant, and the rest are normal diploid cells without it, the expected ALT fraction is
$$\mathrm{VAF} = \frac{\pi m}{\pi P + 2(1 - \pi)}.$$
Purity $\pi$ and local ploidy $P$ are confounded in this expression, which is why copy-number and purity estimation come before interpreting allele fractions ([[Copy Number Variation]], [[Somatic Variant Calling]]).
- **Beyond the nucleus.** Mitochondrial calls are written as haploid in VCF;[^hts] how variation among mitochondrial DNA copies is described is a separate topic ([[Mitochondrial DNA]]).

## Mathematical representation

- Ploidy at a locus: $k \in \{1, 2, 3, \dots\}$. Allele set $\mathcal{A} = \{0, 1, \dots, A-1\}$, with 0 the reference allele.
- An unphased genotype is a multiset $g$ of size $k$ over $\mathcal{A}$; the number of genotypes is $\binom{A+k-1}{k}$. A phased genotype is an ordered $k$-tuple, $A^k$ possibilities ([[Haplotype]]).
- The dosage of allele $a$ is $x_a(g) = $ number of copies of $a$ in $g$, with $\sum_a x_a(g) = k$.
- Read model: $X \mid j \sim \mathrm{Binomial}(d, p_j)$ with $p_j = \frac{j}{k}(1 - \varepsilon) + \left(1 - \frac{j}{k}\right)\varepsilon$, where $X$ is the number of ALT reads among $d$, $j$ the ALT dosage and $\varepsilon$ a per-read error rate. The likelihood of dosage $j$ is $\binom{d}{X} p_j^X (1 - p_j)^{d - X}$.

## Computational representation

```python
from itertools import combinations_with_replacement
from math import comb


def genotypes(ploidy: int, n_alleles: int) -> list[tuple[int, ...]]:
    """All unordered genotypes: multisets of `ploidy` allele indices (0 = REF)."""
    return list(combinations_with_replacement(range(n_alleles), ploidy))


def likelihoods(alt: int, depth: int, ploidy: int, error: float = 0.01) -> list[float]:
    """Binomial likelihood of `alt` ALT reads out of `depth`, for each ALT dosage 0..ploidy."""
    out = []
    for j in range(ploidy + 1):
        p = (j / ploidy) * (1 - error) + (1 - j / ploidy) * error
        out.append(comb(depth, alt) * p**alt * (1 - p) ** (depth - alt))
    return out


for k in (1, 2, 3, 4, 6):
    fractions = [round(j / k, 2) for j in range(k + 1)]
    print(f"ploidy {k}: {len(genotypes(k, 2))} biallelic genotypes, "
          f"{len(genotypes(k, 3))} triallelic, expected ALT fractions {fractions}")
print(genotypes(2, 3))
for k in (2, 4):
    L = likelihoods(12, 40, k)
    print(k, [f"{x:.1e}" for x in L], "best dosage:", max(range(k + 1), key=L.__getitem__))
```

```text
ploidy 1: 2 biallelic genotypes, 3 triallelic, expected ALT fractions [0.0, 1.0]
ploidy 2: 3 biallelic genotypes, 6 triallelic, expected ALT fractions [0.0, 0.5, 1.0]
ploidy 3: 4 biallelic genotypes, 10 triallelic, expected ALT fractions [0.0, 0.33, 0.67, 1.0]
ploidy 4: 5 biallelic genotypes, 15 triallelic, expected ALT fractions [0.0, 0.25, 0.5, 0.75, 1.0]
ploidy 6: 7 biallelic genotypes, 28 triallelic, expected ALT fractions [0.0, 0.17, 0.33, 0.5, 0.67, 0.83, 1.0]
[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
2 ['4.2e-15', '5.1e-03', '5.0e-47'] best dosage: 1
4 ['4.2e-15', '1.1e-01', '5.1e-03', '3.9e-09', '5.0e-47'] best dosage: 1
```

The diploid genotypes `(0, 1)`, `(1, 2)` and so on are exactly the unphased VCF genotypes `0/1`, `1/2` ([[Genotype]]).

## Worked example

> [!example] Twelve ALT reads out of forty, under two ploidies
> A site has 40 reads, 12 of them (30%) with the alternative allele; error rate 1%.
> 1. **Diploid model.** Expected fractions 0, 0.5, 1. Only dosage 1 (heterozygous, `0/1`) is plausible: its likelihood, $5.1 \times 10^{-3}$, beats the homozygous genotypes by more than 10 orders of magnitude. The 30% is read as sampling noise around 50%.
> 2. **Tetraploid model.** Expected fractions 0, 0.25, 0.5, 0.75, 1. Dosage 1 (one ALT copy of four) has likelihood 0.11, about 21 times that of dosage 2 ($5.1 \times 10^{-3}$).
> 3. **Conclusion.** The same reads give genotype "one ALT copy of two" or "one ALT copy of four". The ploidy must come from outside the site: the species, the chromosome (autosome, X, Y), or a copy-number analysis.

## Common misconceptions

> [!warning] "Diploid means two chromosomes"
> Diploid means two complete **sets**: 46 chromosomes in a human body cell, in 23 homologous pairs.[^os13]

> [!warning] "Polyploidy and aneuploidy are the same thing"
> Polyploidy adds whole chromosome sets; aneuploidy adds or removes single chromosomes, such as a trisomy.[^os13] A triploid ($3n$) and a trisomic ($2n + 1$) cell are very different.

> [!warning] "A heterozygous site shows 50% ALT reads"
> 50% is the expectation for a diploid; sampling makes observed fractions scatter around it, and other ploidies, copy-number changes or mixtures of cells shift the expectation itself (Advanced).

> [!warning] "A human is diploid at every locus"
> Gametes are haploid,[^os11] and males carry one copy of most of the X and of the Y; the VCF specification writes those calls, and mitochondrial calls, as haploid.[^hts][^griffiths]

## Exercises

> [!question] Exercise 1 (L1)
> For humans ($2n = 46$), give the chromosome number of (a) a gamete, (b) a triploid cell, (c) a tetraploid cell, (d) a cell with trisomy 21, (e) a cell with a single X and no other sex chromosome. Classify each as euploid (whole sets) or aneuploid.

> [!success]- Solution
> (a) 23, haploid, euploid. (b) 69, euploid (polyploid). (c) 92, euploid (polyploid). (d) 47, aneuploid ($2n + 1$). (e) 45, aneuploid ($2n - 1$).

> [!question] Exercise 2 (L1)
> Why are triploid organisms usually sterile, while tetraploids can form gametes more easily?

> [!success]- Solution
> At meiosis, homologs pair. With three sets, each chromosome has an odd number of homologs: one has no partner and segregation is unbalanced, giving aneuploid gametes.[^os13] With four sets, homologs can form two pairs, so balanced gametes with two sets each are possible.

> [!question] Exercise 3 (L2, Python)
> Using `genotypes` from the code above, count the genotypes for (a) a diploid site with 4 alleles, (b) a hexaploid biallelic site, (c) a tetraploid site with 3 alleles, and check each against $\binom{A+k-1}{k}$.

> [!success]- Solution
> ```python
> for k, a in [(2, 4), (6, 2), (4, 3)]:
>     print(k, a, len(genotypes(k, a)), comb(a + k - 1, k))
> ```
> Output: `2 4 10 10`, `6 2 7 7`, `4 3 15 15`. For a biallelic site the formula reduces to $k + 1$: the genotype is fully described by its ALT dosage.

> [!question] Exercise 4 (L3)
> A tumour sample has purity $\pi = 0.6$. At a locus, a variant is present on one copy in tumour cells. Compute the expected ALT fraction if tumour cells have (a) 2 copies of the locus, (b) 4 copies. (c) In case (b), what fraction would you expect if the variant were on 2 of the 4 copies? What does this imply for reading allele fractions in tumours?

> [!success]- Solution
> With $\mathrm{VAF} = \pi m / (\pi P + 2(1 - \pi))$: (a) $0.6 / (1.2 + 0.8) = 0.30$; (b) $0.6 / (2.4 + 0.8) = 0.1875$; (c) $1.2 / 3.2 = 0.375$. A 30% allele fraction can mean "heterozygous in a diploid tumour at 60% purity" or something else entirely: allele fractions cannot be interpreted without purity and local copy number.

> [!question] Exercise 5 (L3, Python)
> With `likelihoods`, find the ALT read counts out of 40 for which a tetraploid model prefers dosage 2 over dosages 1 and 3 (error 1%). Compare the width of that range with the range where a diploid model prefers dosage 1.

> [!success]- Solution
> ```python
> def preferred(depth, ploidy, dosage):
>     return [x for x in range(depth + 1)
>             if max(range(ploidy + 1), key=likelihoods(x, depth, ploidy).__getitem__) == dosage]
>
> tetra, di = preferred(40, 4, 2), preferred(40, 2, 1)
> print(tetra[0], tetra[-1], di[0], di[-1])
> ```
> Output: `15 25 6 34`. A tetraploid "half ALT" call needs 15 to 25 ALT reads of 40 (11 values), while the diploid heterozygous call accepts 6 to 34 (29 values): higher ploidy packs more genotypes into the same interval of allele fractions, so polyploid genotyping needs much deeper coverage.

## Mastery checklist

- [ ] 1 Recognized: I can define haploid, diploid, polyploid and aneuploid, with the human numbers.
- [ ] 2 Understood: I can explain why ploidy fixes the number of alleles per genotype, and why ploidy varies along a genome (X, Y, mitochondrion).
- [ ] 3 Practiced: I can count genotypes for any ploidy and number of alleles and compute read-count likelihoods per dosage.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I set the ploidy of each sample and region correctly (sex chromosomes, mitochondrion) and check allele-fraction distributions.
- [ ] 5 Explained: I can explain how ploidy, copy number and sample purity shape allele fractions and k-mer spectra, and their limits for genotyping.

## References

[^os11]: [[Biology 2e (OpenStax)]], section 11.1 "The Process of Meiosis" (haploid and diploid cells, gametes and fertilization).
[^os12]: [[Biology 2e (OpenStax)]], ch. 12 "Mendel's Experiments and Heredity" (homozygous and heterozygous genotypes).
[^os13]: [[Biology 2e (OpenStax)]], section 13.2 "Chromosomal Basis of Inherited Disorders" (human karyotype, polyploidy, aneuploidy).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of sex chromosomes and hemizygosity.
[^hts]: [[HTS Format Specifications]], VCF specification, genotype field `GT` (haploid calls).
[^mangs]: [[Mangs 2007 - The Human Pseudoautosomal Region]], *Current Genomics* 8(2):129-136.
