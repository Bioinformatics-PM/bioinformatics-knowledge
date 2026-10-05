---
aliases:
  - Frequency Table
  - Relative Frequency
  - Cumulative Frequency
  - Distribution de fréquences
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Level of Measurement]]"
  - "[[Sampling]]"
related:
  - "[[Histogram]]"
  - "[[Probability Distribution]]"
  - "[[Empirical Cumulative Distribution Function]]"
  - "[[Contingency Table]]"
  - "[[GC Content]]"
  - "[[Codon Usage Bias]]"
  - "[[Allele Frequency]]"
  - "[[K-mer]]"
  - "[[Genetic Code]]"
projects:
  - "[[01-dna-engine]]"
  - "[[07-evolution-simulator]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Karlin 1995 - Dinucleotide Relative Abundance Extremes]]"
---

# Frequency Distribution

> [!abstract]
> A frequency distribution counts how often each value (or range of values) occurs in a dataset and turns the counts into proportions: the first summary of any variable, from the bases of a sequence to the alleles of a population.

## Definition

A **frequency distribution** lists the values, or classes of values, of a variable with the number of times each occurs. The **(absolute) frequency** is that number; the **relative frequency** is the frequency divided by the total number of observations; the **cumulative relative frequency** of a value is the sum of the relative frequencies of all values up to and including it.[^os1]

## Why it matters

- **Composition.** Base counts and [[GC Content]] are frequency distributions of a sequence's letters ([[01-dna-engine]]).
- **Codon usage tables** give the frequency of each codon in coding sequences, overall and among the synonymous codons of each amino acid ([[Codon Usage Bias]], [[Genetic Code]]).
- **Allele and genotype frequencies** are the basic data of population genetics ([[Allele Frequency]], [[07-evolution-simulator]]).[^hartl]
- **Histograms** are drawings of grouped frequency tables (read lengths, qualities, insert sizes; [[Histogram]]).
- **Probabilities from data.** Profiles, substitution matrices and k-mer models are relative frequencies turned into probability estimates ([[Probability Distribution]]).

## Core (L1)

**Building a table.**

1. List the distinct values: in any fixed order for nominal data, in increasing order for ordinal and quantitative data ([[Level of Measurement]]).
2. Count each value (absolute frequency $f$).
3. Divide by the number of observations $n$ (relative frequency).
4. If the values are ordered, accumulate (cumulative relative frequency).
5. Check: frequencies sum to $n$, relative frequencies to 1 (up to rounding).

The first four lines of the output in Computational representation are such a table for the bases of a toy 54 nt sequence (columns: base, $f$, relative, cumulative relative, and a text bar of length $f$). Base order is alphabetical by convention; cumulative frequencies of nominal values depend on that arbitrary order and carry no meaning.

**Grouped tables.** For a continuous variable, or a discrete one with many values, group values into classes (bins) of equal width, with a stated boundary rule so that each observation falls in exactly one class. With classes $[a, b)$, a 150 bp read belongs to $[150, 200)$, not to $[100, 150)$ (last three lines of the output below).

## Deeper (L2)

- **Relative frequencies estimate probabilities.** As the number of repetitions grows, the relative frequency of an outcome tends to its probability (law of large numbers).[^os3] A frequency table is the sample counterpart of a [[Probability Distribution]], and the cumulative relative frequency is the sample counterpart of the [[Cumulative Distribution Function]] ([[Empirical Cumulative Distribution Function]]).
- **Frequencies within groups.** Codon usage within an amino acid divides each codon's count by the count of its amino acid. In the toy sequence, alanine uses GCC 2 times out of 5 (0.40); uniform use of its 4 codons would give 0.25 each ([[Codon Usage Bias]]).
- **Allele frequencies from genotypes.** In $N$ diploid individuals, allele `A` is counted twice in each `AA` homozygote and once in each heterozygote: $\hat p_A = \dfrac{2 n_{AA} + n_{Aa}}{2N}$.[^hartl] The denominator is the number of allele copies, $2N$, not the number of individuals.
- **Two variables at once.** Cross-counting two categorical variables (genotype by case/control status) gives a [[Contingency Table]].

## Advanced (L3)

- **Zero is not impossible.** A value absent from a small sample has relative frequency 0, but its probability need not be 0. Methods that turn counts into probabilities (for example sequence profiles) add **pseudocounts** $\alpha$ to every value before normalizing, $\frac{f(v) + \alpha}{n + \alpha |V|}$, so that unseen values keep a small probability.[^durbin]
- **Observed over expected.** A frequency means more when compared with an expectation. The dinucleotide relative abundance $\rho_{XY} = \hat f_{XY} / (\hat f_X \hat f_Y)$ compares the frequency of the pair $XY$ with the product of its base frequencies; the profile of these 16 values is similar within a genome and differs between genomes, a "genomic signature".[^karlin]
- **Frequencies of frequencies.** Counting how many distinct [[K-mer|k-mers]] occur once, twice, three times... gives a frequency distribution whose values are themselves counts (a k-mer spectrum).
- **Precision depends on $n$.** A relative frequency $\hat p$ from $n$ observations has standard deviation about $\sqrt{\hat p (1 - \hat p)/n}$ ([[Sampling]]). A single gene has too few codons per amino acid to estimate within-amino-acid frequencies well (Exercise 5); codon usage tables pool many genes.

## Mathematical representation

Observations $x_1, \dots, x_n$ take values in a set $V$; $\mathbb{1}[\cdot]$ is 1 if the condition holds and 0 otherwise.

- Absolute frequency $f(v) = \sum_{i=1}^{n} \mathbb{1}[x_i = v]$, with $\sum_{v \in V} f(v) = n$.
- Relative frequency $\hat f(v) = f(v)/n$, with $\sum_{v} \hat f(v) = 1$.
- Cumulative relative frequency (ordered $V$): $\hat F(v) = \sum_{u \le v} \hat f(u)$, non-decreasing from $\hat f(\min V)$ to 1.
- Grouped: with class boundaries $b_0 < b_1 < \dots < b_K$, $f_k = \#\{i : b_{k-1} \le x_i < b_k\}$.
- Within groups: for a codon $c$ with amino acid $g(c)$ ([[Genetic Code]]), $\hat f(c \mid a) = f(c) \big/ \sum_{c' : g(c') = a} f(c')$.

## Computational representation

`collections.Counter` counts any iterable; the rest is division and accumulation:

```python
from collections import Counter, defaultdict

# Invented toy coding sequence (not a real gene).
CDS = "ATGGCTGCAGCCGCGGCCAAAAAGAAACTGCTCTTATTGCTGGGCGGTGGCTAA"


def frequency_table(items, order=None):
    """Rows (value, absolute, relative, cumulative relative)."""
    counts = Counter(items)
    n = sum(counts.values())
    rows, cumulative = [], 0.0
    for value in order or sorted(counts):
        cumulative += counts[value] / n
        rows.append((value, counts[value], counts[value] / n, cumulative))
    return rows


for base, f, rel, cum in frequency_table(CDS, order="ACGT"):
    print(f"{base}  {f:3}  {rel:.3f}  {cum:.3f}  {'#' * f}")

# Codon usage: count codons, then relative frequency within each amino acid.
BASES = "TCAG"
CODE = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"  # NCBI table 1
TABLE = dict(zip((a + b + c for a in BASES for b in BASES for c in BASES), CODE))
codons = [CDS[i:i + 3] for i in range(0, len(CDS) - 2, 3)]
usage = Counter(codons)
by_aa = defaultdict(int)
for codon, f in usage.items():
    by_aa[TABLE[codon]] += f
for codon in sorted(usage, key=lambda c: (TABLE[c], c)):
    aa = TABLE[codon]
    print(f"{aa} {codon} {usage[codon]}  {usage[codon] / by_aa[aa]:.2f}")

# Allele frequency from invented genotype counts at one biallelic site.
genotypes = {"AA": 36, "Aa": 48, "aa": 16}
n_ind = sum(genotypes.values())
p_A = (2 * genotypes["AA"] + genotypes["Aa"]) / (2 * n_ind)
print(n_ind, p_A, round(1 - p_A, 2))

# Grouped frequency table for a continuous variable (invented read lengths, bins of 50 bp).
lengths = [101, 148, 150, 150, 150, 149, 87, 150, 132, 150, 150, 61, 150, 145, 150, 150]
bins = Counter(50 * (x // 50) for x in lengths)
for start in sorted(bins):
    print(f"[{start}, {start + 50})  {bins[start]:2}  {bins[start] / len(lengths):.3f}")
```

```text
A   13  0.241  0.241  #############
C   13  0.241  0.481  #############
G   17  0.315  0.796  #################
T   11  0.204  1.000  ###########
* TAA 1  1.00
A GCA 1  0.20
A GCC 2  0.40
A GCG 1  0.20
A GCT 1  0.20
G GGC 2  0.67
G GGT 1  0.33
K AAA 2  0.67
K AAG 1  0.33
L CTC 1  0.20
L CTG 2  0.40
L TTA 1  0.20
L TTG 1  0.20
M ATG 1  1.00
100 0.6 0.4
[50, 100)   2  0.125
[100, 150)   5  0.312
[150, 200)   9  0.562
```

`50 * (x // 50)` implements the $[a, b)$ rule. Printed relative frequencies are rounded, so a cumulative value can differ from the sum of displayed values in the last digit (0.481 is $26/54$).

## Worked example

> [!example] From genotype counts to allele frequencies (invented data)
> A biallelic site is genotyped in 100 individuals: 36 `AA`, 48 `Aa`, 16 `aa`.
> 1. **Genotype frequencies**: $36/100 = 0.36$, $0.48$, $0.16$ (sum 1).
> 2. **Allele counts**: `A` appears $2 \times 36 + 48 = 120$ times, `a` appears $48 + 2 \times 16 = 80$ times, out of $2 \times 100 = 200$ copies.
> 3. **Allele frequencies**: $\hat p_A = 120/200 = 0.6$, $\hat p_a = 0.4$, as printed by the code.
> 4. **Comparison**: $\hat p_A^2 = 0.36$, $2 \hat p_A \hat p_a = 0.48$, $\hat p_a^2 = 0.16$ reproduce the genotype frequencies exactly. The toy counts were built to be in [[Hardy-Weinberg Equilibrium]] proportions; real data are compared with these expectations by a test ([[Chi-Square Test]]).

## Common misconceptions

> [!warning] "A relative frequency is the probability"
> It is an estimate of it, with sampling error that is large when $n$ is small (Advanced (L3)). The 0.40 of GCC among 5 alanine codons says little about the organism.

> [!warning] "Allele frequency = fraction of individuals carrying the allele"
> In the worked example, $(48 + 16)/100 = 0.64$ of individuals carry `a`, but the frequency of `a` is 0.4: alleles are counted over $2N$ copies.

> [!warning] "Bin boundaries are a detail"
> Moving the boundary rule from $[a, b)$ to $(a, b]$ moves the nine 150 bp reads from the $[150, 200)$ class into the class below. Grouped tables, and the histograms drawn from them, change with boundaries and widths ([[Histogram]]).

## Exercises

> [!question] Exercise 1 (L1)
> Build the absolute, relative and cumulative relative frequency table of the bases of `GATTACAGATTACA` (order A, C, G, T), and give its GC content.

> [!success]- Solution
> A 6, C 2, G 2, T 4 ($n = 14$); relative 0.429, 0.143, 0.143, 0.286; cumulative 0.429, 0.571, 0.714, 1.0 (checked with `frequency_table`). GC content $= (2 + 2)/14 \approx 0.286$.

> [!question] Exercise 2 (L1)
> Genotype counts: 10 `AA`, 20 `Aa`, 70 `aa`. Compute the frequency of allele `A` and the fraction of individuals carrying at least one `A`.

> [!success]- Solution
> $\hat p_A = (2 \times 10 + 20)/200 = 0.2$. Carriers: $(10 + 20)/100 = 0.3$. The carrier fraction exceeds the allele frequency because heterozygotes carry one copy but count as a whole individual.

> [!question] Exercise 3 (L2, Python)
> Count the overlapping dinucleotides of the toy `CDS`, print the three most frequent with their relative frequencies, and compute the relative abundance $\rho_{CG} = \hat f_{CG} / (\hat f_C \hat f_G)$ using the base frequencies of the table above.

> [!success]- Solution
> ```python
> di = Counter(CDS[i:i + 2] for i in range(len(CDS) - 1))
> n_di = sum(di.values())
> print(n_di, [(d, f, round(f / n_di, 3)) for d, f in di.most_common(3)])
> print(di["CG"], round((di["CG"] / n_di) / ((13 / 54) * (17 / 54)), 2))
> ```
> Output: `53 [('GC', 9, 0.17), ('AA', 7, 0.132), ('TG', 6, 0.113)]`, then `3 0.75`. A sequence of 54 nt has 53 overlapping dinucleotides. CG occurs 3 times, 0.75 of what independent base usage predicts; on a toy sequence this is noise, but genome-wide profiles of $\rho$ are informative.[^karlin]

> [!question] Exercise 4 (L2)
> The toy `CDS` has 18 codons and never uses TGT. Give the relative frequency of TGT among the 64 codons without and with a pseudocount $\alpha = 1$ per codon.

> [!success]- Solution
> Without: $0/18 = 0$. With: $(0 + 1)/(18 + 64 \times 1) = 1/82 \approx 0.0122$. Every codon now has a non-zero estimate, at the price of pulling observed frequencies toward uniform, strongly so when $n$ is small compared with $|V|$.

> [!question] Exercise 5 (L3)
> Estimate the standard deviation of the within-alanine frequency of GCC (0.40, from 5 alanine codons). What does it imply for codon usage tables computed from one gene?

> [!success]- Solution
> $\sqrt{0.4 \times 0.6 / 5} \approx 0.219$: the estimate is compatible with anything from near 0 to about 0.8, including uniform use (0.25). Within-amino-acid frequencies need hundreds of codons per amino acid, which is why codon usage tables pool many genes of an organism ([[Codon Usage Bias]]).

## Mastery checklist

- [ ] 1 Recognized: I can define absolute, relative and cumulative relative frequency.
- [ ] 2 Understood: I can explain when cumulative frequencies make sense, why allele frequencies use $2N$, and why bins need a boundary rule.
- [ ] 3 Practiced: I can build frequency, grouped and within-group tables with `Counter`, and add pseudocounts.
- [ ] 4 Applied: I computed base composition in [[01-dna-engine]] and allele frequency trajectories in [[07-evolution-simulator]] on real or simulated data.
- [ ] 5 Explained: I can teach how relative frequencies estimate probabilities, how precise they are, and how observed-over-expected ratios turn them into signals.

## References

[^os1]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 1 "Sampling and Data" (frequency, frequency tables).
[^os3]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 3 "Probability Topics" (relative frequency and the law of large numbers).
[^hartl]: [[Principles of Population Genetics (Hartl)]], allele and genotype frequencies.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], pseudocounts in the estimation of profile probabilities.
[^karlin]: [[Karlin 1995 - Dinucleotide Relative Abundance Extremes]], *Trends in Genetics* 11(7):283-290.
