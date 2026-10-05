---
aliases:
  - Genotypes
  - Génotype
  - GT
  - Genotype Call
  - Homozygous
  - Heterozygous
  - Allele Dosage
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Allele]]"
  - "[[Ploidy]]"
  - "[[Chromosome]]"
related:
  - "[[Phenotype]]"
  - "[[Mendelian Inheritance]]"
  - "[[Haplotype]]"
  - "[[VCF Format]]"
  - "[[Variant Calling]]"
  - "[[Genotype Likelihood]]"
  - "[[Haplotype Phasing]]"
  - "[[Genotype Imputation]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Trio Analysis]]"
  - "[[Genome-Wide Association Study]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[07-evolution-simulator]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[GA4GH hts-specs]]"
  - "[[Relling 2011 - Clinical Pharmacogenetics Implementation Consortium]]"
---

# Genotype

> [!abstract]
> A genotype is the pair of alleles a diploid individual carries at a locus, one from each parent; bioinformatics writes it as `0/0`, `0/1` or `1/1`, or simply as 0, 1 or 2 copies of an allele.

## Definition

The **genotype** is an organism's genetic makeup, the alleles it carries, whether or not they are visible in its traits.[^os12] At one locus, a diploid genotype is the combination of the two alleles on the two homologous chromosomes: **homozygous** if they are identical, **heterozygous** if they differ.[^os12] More generally, a genotype has as many alleles as the [[Ploidy]] at that locus. The observable traits it contributes to form the [[Phenotype]].[^os12][^griffiths]

## Why it matters

- **Every VCF sample column is a genotype.** The `GT` field of [[VCF Format]] encodes each sample's alleles as indices into `REF` and `ALT`, with `/` for unphased and `|` for phased genotypes.[^hts] Reading it correctly is the first step of any variant analysis ([[10-genomic-pipeline]]).
- **Statistical genetics works on genotype matrices.** Coding each genotype as 0, 1 or 2 copies of an allele turns a cohort into a numerical matrix for association tests, principal component analysis and relatedness ([[Genome-Wide Association Study]], [[Population Structure]], [[Identity by Descent]]).
- **Genotype frequencies test data and models.** Comparing observed genotype counts with [[Hardy-Weinberg Equilibrium]] expectations and checking that a child's genotypes are compatible with its parents' ([[Trio Analysis]]) are two quality controls built on genotypes.
- **Genotypes drive clinical decisions.** Pharmacogenetic guidelines translate a patient's genotype into a prescribing action ([[Pharmacogenomics]]).[^relling]

## Core (L1)

**Three ways to write a diploid genotype** at a biallelic locus with alleles A and a (in VCF: REF = A = 0, ALT = a = 1):

| Allele pair | Zygosity | VCF `GT` (unphased) | Count of allele a |
|---|---|---|---:|
| AA | homozygous | `0/0` | 0 |
| Aa | heterozygous | `0/1` | 1 |
| aa | homozygous | `1/1` | 2 |

The pair is **unordered**: Aa and aA are the same genotype, because nothing distinguishes the two homologs unless we know which parent each came from. The **allele count** (or dosage) summarizes the genotype in one number; for a biallelic diploid site it loses nothing, since 0, 1 and 2 correspond one-to-one to the three genotypes.

**Genotype and phenotype are different things.** In Mendel's cross of yellow-pod and green-pod plants, all hybrid offspring had yellow pods, like the yellow parent, although their genotype differed from it: same phenotype, different genotypes ([[Dominance]], [[Mendelian Inheritance]]).[^os12]

**From parents to child.** Each parent passes one of its two alleles to each gamete ([[Meiosis]]), so a child's genotype takes one allele from the mother and one from the father. A child cannot be `0/0` if a parent is `1/1`: such a combination flags an error or a new mutation ([[Trio Analysis]], [[Mutation Rate]]).

## Deeper (L2)

### The VCF genotype field

In a VCF sample column, `GT` lists allele indices: 0 for the `REF` allele, 1 for the first allele in `ALT`, 2 for the second, and so on. The separator `/` means unphased and `|` phased; a haploid call has a single allele; a missing allele is written `.`.[^hts]

```text
#CHROM  POS   REF  ALT   FORMAT  mother  father  son      (invented trio, columns simplified)
chr1    1200  A    G     GT      0/1     0/0     0/1
chr1    3400  C    T     GT      1/1     0/1     0/0
chr1    5600  G    A,C   GT      0/2     1/2     2/2
chr1    7800  T    C     GT      0|1     1|1     1|0
chr1    9900  A    G     GT      ./.     0/1     0/0
chrX    9100  G    T     GT      0/1     0       1
```

Reading the records:

- `0/2` at 5600 is heterozygous G/C; `1/2` is heterozygous A/C, with no reference allele; `2/2` is homozygous C.
- At 9900 the mother's genotype is **missing** (`./.`), which is not the same as `0/0`.
- On chrX, outside the pseudoautosomal regions, the father and son have one X: their calls are haploid (`0`, `1`), as the specification requires ([[Ploidy]], [[Sex-Linked Inheritance]]).[^hts]
- At 3400, the son is `0/0` but his mother is `1/1`: a **Mendelian inconsistency**, most often a genotyping error (see the code below).

### Phase

An unphased heterozygote `0/1` says which alleles are present, not which chromosome carries which. With `|`, the order is meaningful: in a phased block, the alleles written first all sit on one chromosome and those written second on the other.[^hts] For two heterozygous sites:

```text
phased    site 1: 0|1   site 2: 1|0   -> chromosome A carries 0-1, chromosome B carries 1-0 (trans)
phased    site 1: 0|1   site 2: 0|1   -> chromosome A carries 0-0, chromosome B carries 1-1 (cis)
unphased  site 1: 0/1   site 2: 0/1   -> either configuration
```

Whether two variants are on the same chromosome (cis) or on different ones (trans) can decide whether both copies of a gene are affected, which is why [[Haplotype Phasing]] matters ([[Haplotype]]).

### Genotype matrices

For $n$ samples and $m$ biallelic sites, the ALT counts form an $n \times m$ matrix with entries in $\{0, 1, 2\}$ and missing values. Column means give allele frequencies ([[Allele Frequency]]), row sums of heterozygous entries measure individual heterozygosity ([[Heterozygosity]]), and the whole matrix is the input of association and structure analyses.

## Advanced (L3)

- **A genotype call is an inference.** Sequencing observes reads, not genotypes. A caller computes, for each possible genotype, the probability of the observed bases ([[Genotype Likelihood]]), may combine it with a prior such as Hardy-Weinberg proportions at the population allele frequency, and reports the most probable genotype with a confidence ([[Variant Calling]], [[Bayes' Theorem]]). At low depth the prior can decide the call (Exercise 5).
- **Joint calling.** A caller can also genotype many samples together, which is the subject of [[Joint Genotyping]]; a VCF must then say, for every sample at every site, whether it carries the variant, lacks it (`0/0`) or has no data (`./.`).
- **Dosages instead of calls.** When genotypes are uncertain, for example after [[Genotype Imputation]], the expected count $E[g] = P(1) + 2P(2)$ keeps the uncertainty that a hard call would discard.
- **Beyond one locus.** A multilocus genotype (all the loci of an individual) is what association studies, relatedness estimation and polygenic scores use ([[Polygenic Risk Score]]). Mapping a genotype to a phenotype is rarely a lookup: it depends on dominance, on other loci and on the environment ([[Phenotype]], [[Epistasis]]).

## Mathematical representation

- Ploidy $k$, allele set $\{0, 1, \dots, A-1\}$. An **unphased genotype** is a multiset $g = \{a_1, \dots, a_k\}$; a **phased genotype** is an ordered tuple $(a_1, \dots, a_k)$, one allele per chromosome copy. There are $\binom{A + k - 1}{k}$ unphased and $A^k$ phased genotypes ([[Ploidy]]).
- **Dosage** of allele $a$: $x_a(g) = \#\{i : a_i = a\}$, so $\sum_a x_a(g) = k$. For a biallelic diploid site, $x = x_1(g) \in \{0, 1, 2\}$.
- **Genotype matrix**: $X \in \{0, 1, 2, \varnothing\}^{n \times m}$, where $X_{ij}$ is the ALT count of sample $i$ at site $j$ and $\varnothing$ marks a missing call. The additive model of an association test is $y_i = \beta_0 + \beta X_{ij} + \varepsilon_i$ ([[Linear Regression]], [[Genome-Wide Association Study]]).
- **Mendelian consistency** (autosomal, diploid): with child $\{c_1, c_2\}$, mother $M$ and father $F$ (as sets of alleles), the trio is consistent if and only if $(c_1 \in M \wedge c_2 \in F) \vee (c_2 \in M \wedge c_1 \in F)$.
- **Genotype posterior.** With reads $D$ and a prior $P(g)$, $P(g \mid D) = \dfrac{P(D \mid g)\,P(g)}{\sum_{g'} P(D \mid g')\,P(g')}$; under Hardy-Weinberg proportions at ALT frequency $p$, $P(0/0) = (1-p)^2$, $P(0/1) = 2p(1-p)$, $P(1/1) = p^2$ ([[Hardy-Weinberg Equilibrium]]).

## Computational representation

The code parses the invented trio VCF above, converts each `GT` to alleles, ALT count and zygosity, and checks Mendelian consistency.

```python
# Invented trio VCF (genotype column only; QUAL, FILTER and INFO left as ".").
TOY_VCF = """\
##fileformat=VCFv4.3
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tmother\tfather\tson
chr1\t1200\t.\tA\tG\t.\t.\t.\tGT\t0/1\t0/0\t0/1
chr1\t3400\t.\tC\tT\t.\t.\t.\tGT\t1/1\t0/1\t0/0
chr1\t5600\t.\tG\tA,C\t.\t.\t.\tGT\t0/2\t1/2\t2/2
chr1\t7800\t.\tT\tC\t.\t.\t.\tGT\t0|1\t1|1\t1|0
chr1\t9900\t.\tA\tG\t.\t.\t.\tGT\t./.\t0/1\t0/0
chrX\t9100\t.\tG\tT\t.\t.\t.\tGT\t0/1\t0\t1
"""


def parse_gt(gt: str) -> tuple[tuple[int | None, ...], bool]:
    """'0/1' -> ((0, 1), False); '1|0' -> ((1, 0), True); './.' -> ((None, None), False)."""
    phased = "|" in gt
    return tuple(None if a == "." else int(a) for a in gt.replace("|", "/").split("/")), phased


def alt_count(alleles: tuple) -> int | None:
    """Number of non-reference alleles (the 0, 1, 2 coding of a diploid); None if missing."""
    return None if None in alleles else sum(a != 0 for a in alleles)


def zygosity(alleles: tuple) -> str:
    if None in alleles:
        return "missing"
    if len(alleles) == 1:
        return "haploid"
    return "homozygous" if len(set(alleles)) == 1 else "heterozygous"


def mendel_ok(child: tuple, mother: tuple, father: tuple) -> bool | None:
    """Diploid child: one allele from each parent. None when a call is missing or not diploid."""
    if None in child + mother + father or not len(child) == len(mother) == len(father) == 2:
        return None
    a, b = child
    return (a in mother and b in father) or (b in mother and a in father)


samples = []
for line in TOY_VCF.splitlines():
    if line.startswith("##"):
        continue
    fields = line.split("\t")
    if line.startswith("#"):
        samples = fields[9:]
        continue
    chrom, pos, ref, alt = fields[0], fields[1], fields[3], fields[4]
    calls = {s: parse_gt(gt) for s, gt in zip(samples, fields[9:])}
    summary = [f"{s}={gt}:{alt_count(calls[s][0])}:{zygosity(calls[s][0])[:3]}"
               for s, gt in zip(samples, fields[9:])]
    ok = mendel_ok(calls["son"][0], calls["mother"][0], calls["father"][0])
    print(chrom, pos, ref, alt, *summary, "Mendel:", ok)
```

```text
chr1 1200 A G mother=0/1:1:het father=0/0:0:hom son=0/1:1:het Mendel: True
chr1 3400 C T mother=1/1:2:hom father=0/1:1:het son=0/0:0:hom Mendel: False
chr1 5600 G A,C mother=0/2:1:het father=1/2:2:het son=2/2:2:hom Mendel: True
chr1 7800 T C mother=0|1:1:het father=1|1:2:hom son=1|0:1:het Mendel: True
chr1 9900 A G mother=./.:None:mis father=0/1:1:het son=0/0:0:hom Mendel: None
chrX 9100 G T mother=0/1:1:het father=0:0:hap son=1:1:hap Mendel: None
```

Two simplifications to keep in mind: `alt_count` counts all non-reference alleles together (at the multiallelic site 5600 a per-allele count is often needed), and the Mendelian check skips haploid calls, which need a sex-aware rule (the son's X comes from his mother: `1` is compatible with her `0/1`).

## Worked example

> [!example] Reading one record for three samples
> Record `chr1 5600 G A,C` with genotypes mother `0/2`, father `1/2`, son `2/2` (invented).
> 1. **Alleles.** 0 = G, 1 = A, 2 = C.[^hts]
> 2. **Genotypes.** Mother G/C (heterozygous), father A/C (heterozygous, no reference allele), son C/C (homozygous).
> 3. **Counts.** Counting copies of each allele: mother G1 A0 C1, father G0 A1 C1, son G0 A0 C2. A single "ALT count" (1, 2, 2) hides that the father's two ALT alleles are different.
> 4. **Inheritance.** The son's two C alleles must come one from each parent: the mother has a C, the father has a C, so the trio is consistent, and each parent transmitted its C allele.
> 5. **Phenotype?** Nothing in the record says what the son looks like: that needs the function of the alleles and the other factors of [[Phenotype]].

## Common misconceptions

> [!warning] "`0/1` means allele 0 is on chromosome 1"
> Unphased `0/1` only says the sample carries one REF and one ALT allele; the order carries no information, so `0/1` and `1/0` are the same genotype. Only `|` makes the order meaningful.[^hts]

> [!warning] "A missing genotype is homozygous reference"
> `./.` means no call could be made.[^hts] Replacing missing calls by `0/0` inflates homozygous-reference counts and biases allele frequencies; treat them as missing or impute them.

> [!warning] "Heterozygous means REF/ALT"
> At a multiallelic site, `1/2` is heterozygous without any reference allele. "Heterozygous" means two different alleles, whichever they are.

> [!warning] "The genotype determines the phenotype"
> The same genotype can give different phenotypes in different environments, and different genotypes can give the same phenotype (a heterozygote and a dominant homozygote).[^os12][^griffiths] See [[Phenotype]].

## Exercises

> [!question] Exercise 1 (L1)
> For a biallelic locus with alleles B (REF) and b (ALT), write each genotype BB, Bb, bb as a VCF `GT` and as a count of b. Which gametes can each genotype produce?

> [!success]- Solution
> BB = `0/0` = 0, gametes B only; Bb = `0/1` = 1, gametes B or b (half each); bb = `1/1` = 2, gametes b only ([[Mendelian Inheritance]]).

> [!question] Exercise 2 (L1)
> A record has `REF` = T and `ALT` = C,G. Give the alleles of the genotypes `0/0`, `1/1`, `0/2`, `1/2`, `2/2` and say which are heterozygous.

> [!success]- Solution
> `0/0` T/T, `1/1` C/C, `0/2` T/G (heterozygous), `1/2` C/G (heterozygous, no REF allele), `2/2` G/G.[^hts]

> [!question] Exercise 3 (L2)
> A sample is heterozygous at two nearby sites of one gene, each variant destroying the gene's function. (a) If the phased genotypes are `0|1` and `1|0`, how many functional copies of the gene does the sample carry? (b) And if they are `0|1` and `0|1`? (c) What can you say from `0/1` and `0/1`?

> [!success]- Solution
> (a) Trans: each chromosome carries one damaging variant, so no functional copy remains. (b) Cis: one chromosome carries both variants, the other none, so one functional copy remains. (c) Nothing: both configurations are possible; phasing is needed ([[Haplotype Phasing]]).

> [!question] Exercise 4 (L2, Python)
> Reusing `TOY_VCF`, `parse_gt` and `alt_count` from the code above, build the genotype matrix (ALT counts) of the biallelic chr1 sites, and count heterozygous calls per sample.

> [!success]- Solution
> ```python
> rows, names = [], []
> for line in TOY_VCF.splitlines():
>     if line.startswith("#"):
>         if not line.startswith("##"):
>             names = line.split("\t")[9:]
>         continue
>     f = line.split("\t")
>     if f[0] == "chr1" and "," not in f[4]:              # autosomal, biallelic
>         rows.append([alt_count(parse_gt(gt)[0]) for gt in f[9:]])
> print(names)
> for r in rows:
>     print(r)
> het = {n: sum(1 for r in rows if r[i] == 1) for i, n in enumerate(names)}
> print(het)
> ```
> Output: `['mother', 'father', 'son']`, then the rows `[1, 0, 1]`, `[2, 1, 0]`, `[1, 2, 1]`, `[None, 1, 0]`, then `{'mother': 2, 'father': 2, 'son': 2}`. Rows are sites here (a VCF is sites by samples); analysis libraries often transpose to samples by sites. The `None` must stay missing.

> [!question] Exercise 5 (L3, Python)
> A site has 1 ALT read out of 4 (error rate 1%). Compute the posterior probabilities of `0/0`, `0/1`, `1/1` with a Hardy-Weinberg prior when the ALT allele frequency is 0.3 and when it is 0.001. Repeat with 6 ALT reads out of 20. What do you conclude?

> [!success]- Solution
> ```python
> from math import comb
>
>
> def posterior(alt: int, depth: int, p: float, error: float = 0.01) -> list[float]:
>     """P(0/0), P(0/1), P(1/1) given ALT reads, with a Hardy-Weinberg prior at ALT frequency p."""
>     prior = [(1 - p) ** 2, 2 * p * (1 - p), p ** 2]
>     like = []
>     for j in range(3):
>         q = j / 2 * (1 - error) + (1 - j / 2) * error
>         like.append(comb(depth, alt) * q**alt * (1 - q) ** (depth - alt))
>     joint = [a * b for a, b in zip(prior, like)]
>     return [round(x / sum(joint), 3) for x in joint]
>
>
> for p in (0.3, 0.001):
>     print(p, posterior(1, 4, p), posterior(6, 20, p))
> ```
> Output: `0.3 [0.153, 0.847, 0.0] [0.0, 1.0, 0.0]` and `0.001 [0.987, 0.013, 0.0] [0.0, 1.0, 0.0]`. With 4 reads, the prior decides: the same single ALT read is called heterozygous for a common allele and dismissed as an error for a rare one. With 20 reads, the data dominate and both priors give `0/1`. Low-coverage genotypes depend on the population model; deep ones barely do ([[Genotype Likelihood]], [[Bayes' Theorem]]).

> [!question] Exercise 6 (L3)
> After imputation, a sample has $P(0/0) = 0.1$, $P(0/1) = 0.6$, $P(1/1) = 0.3$ at a site. Give the best-guess genotype and the expected dosage. Why do association studies often prefer the dosage?

> [!success]- Solution
> Best guess `0/1` (probability 0.6). Expected dosage $0 \times 0.1 + 1 \times 0.6 + 2 \times 0.3 = 1.2$. A hard call would treat this sample exactly like a certain heterozygote; the dosage keeps the 30% chance of `1/1` and the 10% chance of `0/0`, information that a hard call throws away when many genotypes are uncertain ([[Genotype Imputation]], [[Genome-Wide Association Study]]).

## Mastery checklist

- [ ] 1 Recognized: I can define genotype, homozygous and heterozygous, and write a genotype as an allele pair, a VCF `GT` and an allele count.
- [ ] 2 Understood: I can explain phased versus unphased genotypes, missing and haploid calls, multiallelic genotypes and Mendelian consistency.
- [ ] 3 Practiced: I can parse `GT` fields, build a genotype matrix and check a trio in Python.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I read the genotypes of a real multi-sample VCF, count missing and heterozygous calls per sample and flag Mendelian errors; in [[07-evolution-simulator]], I represent individuals by their genotypes.
- [ ] 5 Explained: I can explain why a genotype is an inference from reads, how priors and imputation create uncertain genotypes, and why genotype does not determine phenotype on its own.

## References

[^os12]: [[Biology 2e (OpenStax)]], ch. 12 "Mendel's Experiments and Heredity" (genotype, phenotype, homozygous and heterozygous; the pod-colour cross).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of genotype, phenotype and their relation to the environment.
[^hts]: [[GA4GH hts-specs]], VCF specification, genotype field `GT` (allele indices, `/` and `|`, haploid and missing calls).
[^relling]: [[Relling 2011 - Clinical Pharmacogenetics Implementation Consortium]], *Clinical Pharmacology and Therapeutics* 89(3):464-467.
