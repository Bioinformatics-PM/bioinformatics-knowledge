---
aliases:
  - Expectation
  - Mean of a Random Variable
  - E[X]
  - Espérance mathématique
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Random Variable]]"
  - "[[Probability Distribution]]"
  - "[[Summation Notation]]"
related:
  - "[[Variance]]"
  - "[[Bernoulli Distribution]]"
  - "[[Binomial Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Conditional Expectation]]"
  - "[[Law of Large Numbers]]"
  - "[[K-mer]]"
  - "[[E-Value]]"
  - "[[False Discovery Rate]]"
projects:
  - "[[05-sequence-search]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Karlin 1995 - Dinucleotide Relative Abundance Extremes]]"
  - "[[Benjamini 1995 - Controlling the False Discovery Rate]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
---

# Expected Value

> [!abstract]
> The expected value of a random variable is its probability-weighted average: the balance point of its distribution and the long-run mean of many draws. Expectations add, even for dependent variables, so the expected number of times a word occurs in a random sequence takes one line to compute.

## Definition

For a discrete [[Random Variable]] $X$ with probability mass function $p_X$ ([[Probability Distribution]]), the **expected value** (expectation, mean) is

$$E[X] = \sum_x x \, p_X(x),$$

the sum running over the support of $X$, provided $\sum_x |x| \, p_X(x) < \infty$; otherwise $E[X]$ is not defined. For a continuous variable with density $f$, $E[X] = \int x f(x)\, dx$ ([[Probability Density Function]]). It is often written $\mu$ or $\mu_X$.[^blitz4][^1805-4b][^stat110]

## Why it matters

- **Expected counts are the null baseline.** "Is this motif over-represented?", "how many restriction sites should this genome have?", "how many hits would a random database give?" all compare an observed count with its expected value under a random model ([[K-mer]], [[Sequence Motif]], [[Restriction Enzyme]]). [[05-sequence-search]] needs the expected number of random k-mer hits.
- **Linearity makes hard counts easy.** Overlapping occurrences of a word, errors along a read, matches between two sequences: each is a sum of dependent 0/1 variables whose distribution is messy, but whose mean is a plain sum of probabilities.
- **Means are what we estimate.** Mean depth (coverage), mean expression of a gene, allele frequency (the mean of 0/1 allele indicators): sample averages estimate expected values ([[Law of Large Numbers]], [[Measure of Central Tendency]]).

## Core (L1)

### A weighted average

Let $X$ be the number of A in a random 3-mer with independent, uniform bases; its PMF is $27/64, 27/64, 9/64, 1/64$ for $0, 1, 2, 3$ ([[Probability Distribution#Core (L1)]]). Then

$$E[X] = 0 \cdot \tfrac{27}{64} + 1 \cdot \tfrac{27}{64} + 2 \cdot \tfrac{9}{64} + 3 \cdot \tfrac{1}{64} = \tfrac{48}{64} = \tfrac{3}{4}.$$

- **Balance point**: put weights $p_X(x)$ at positions $x$ on a ruler; it balances at $3/4$.
- **Long-run average**: the average of $X$ over many independent random 3-mers approaches $3/4$ ([[Law of Large Numbers]]), although $3/4$ is neither a possible value nor the most likely one (0 and 1 tie at $27/64$).

### Linearity

For any random variables $X$ and $Y$, **dependent or not**, and constants $a, b, c$:[^blitz4][^1805-4b]

$$E[aX + bY + c] = a\,E[X] + b\,E[Y] + c.$$

In the 3-mer, $X = I_1 + I_2 + I_3$ where $I_j = 1$ if position $j$ is A and $0$ otherwise. Each $E[I_j] = 1/4$, so $E[X] = 3/4$ without writing the PMF.

### Indicators: from probabilities to expected counts

The **indicator** $\mathbf{1}_A$ of an event $A$ is 1 if $A$ occurs and 0 otherwise. Its expectation is $E[\mathbf{1}_A] = P(A)$, which Blitzstein and Hwang call the *fundamental bridge* between probability and expectation.[^blitz4] Any count is a sum of indicators, so **an expected count is a sum of probabilities**.

### Expected occurrences of a k-mer

Slide a window of length $k$ along a sequence of length $n$: there are $n - k + 1$ windows, and the count $N_w$ of a word $w$ is the sum of one indicator per window.

```text
sequence    A C G A C G T A C G      n = 10
window i    1 2 3 4 5 6 7 8          n - k + 1 = 8 windows of length k = 3
I_i (ACG)   1 0 0 1 0 0 0 1          N = I_1 + ... + I_8 = 3
```

With independent, uniform bases, each window equals $w$ with probability $(1/4)^k$, hence

$$E[N_w] = \sum_{i=1}^{n-k+1} P(I_i = 1) = \frac{n - k + 1}{4^k}.$$

The indicators are **dependent** (if window 1 reads ACG, window 2 starts with CG and cannot), yet linearity does not care. For GAATTC in 10 kb: $9995/4096 = 2.44$, the value the simulation in [[Probability Distribution#Computational representation]] recovers (2.452). The formula assumes a random model; real genomes are the data it is compared with.

## Deeper (L2)

### Functions of a random variable

The expectation of $g(X)$ is computed from the PMF of $X$ directly (the *law of the unconscious statistician*, LOTUS):[^blitz4]

$$E[g(X)] = \sum_x g(x)\, p_X(x).$$

For nonlinear $g$, in general $E[g(X)] \ne g(E[X])$. With invented counts 1, 10 and 100, equally likely: $E[X] = 37$ and $\log_{10} 37 = 1.57$, but $E[\log_{10} X] = 1$. For a concave $g$ such as the logarithm, $E[g(X)] \le g(E[X])$ (Jensen's inequality):[^blitz] averaging log-expression values gives the log of a geometric mean, smaller than the arithmetic mean ([[Data Transformation]]). The gap between $E[X^2]$ and $E[X]^2$ is the [[Variance]].

**Products need independence.** If $X$ and $Y$ are independent, $E[XY] = E[X]\,E[Y]$; linearity of sums needs nothing, products do.[^blitz4] In a random 3-mer, let $X$ count A and $Y$ count T. A position cannot be both, so $XY$ sums $\mathbf{1}\{\text{pos } i = A\}\mathbf{1}\{\text{pos } j = T\}$ over the 6 ordered pairs $i \ne j$: $E[XY] = 6/16 = 3/8$, while $E[X]E[Y] = 9/16$. The difference, $-3/16$, is their [[Covariance]].

### Tail sums and waiting times

For $X$ with values in $\{0, 1, 2, \dots\}$, $X = \sum_{j \ge 1} \mathbf{1}\{X \ge j\}$, so

$$E[X] = \sum_{j \ge 1} P(X \ge j).$$

This gives waiting times without the PMF: the number of codons read until the first stop in random sequence has $P(X \ge j) = (61/64)^{j-1}$, hence $E[X] = 64/3$ (Exercise 4, [[Genetic Code]], [[Geometric Distribution]]).

### Same mean, different distributions

The words ACGT and AAAA have the same expected count, $(n-3)/256$. But AAAA overlaps itself (AAAAA contains two copies), so its occurrences come in clumps: in the simulation below both means are near 39, while the standard deviations are 6.08 and 7.97. The mean says nothing about spread; the [[Variance]] note computes the difference exactly.

## Advanced (L3)

### Better null models change $P(I_i = 1)$, not the method

- **Composition and dependence.** With base probabilities $\pi_A, \pi_C, \pi_G, \pi_T$, $E[N_w] = (n - k + 1) \prod_{j=1}^{k} \pi_{w_j}$. Under a stationary [[Markov Chain]] with stationary distribution $\pi$ and transition probabilities $P(b \mid a)$, $E[N_w] = (n - k + 1)\, \pi_{w_1} \prod_{j=1}^{k-1} P(w_{j+1} \mid w_j)$; [[Higher-Order Markov Chain|higher-order chains]] condition on longer contexts.
- **Observed over expected.** Karlin and Burge's dinucleotide relative abundance $\rho_{XY} = f_{XY}/(f_X f_Y)$ divides the observed frequency of $XY$ by its expectation from base composition; the profile of the 16 ratios is a genomic signature.[^karlin] CG is rarer in the human genome than the frequencies of C and G predict, because methylated C mutates to T at a high rate (Exercise 3).[^durbin3]

### Expectations behind significance

- A BLAST-style **E-value** is the expected number of chance alignments scoring at least as well as the hit, in a search of that size ([[E-Value]]).[^durbin2]
- The **false discovery rate** is $E[V/R]$, with $V$ the number of false rejections, $R$ the number of rejections and $V/R := 0$ when $R = 0$.[^bh] By linearity, $m$ tests at level $\alpha$ with all null hypotheses true produce $m\alpha$ false positives on average, however dependent the tests are ([[Multiple Testing Correction]]).

### When the expectation misleads or does not exist

- **Ratios.** $E[X/Y] \ne E[X]/E[Y]$ in general: an expected ratio (the FDR, a mean fold change) is not a ratio of expectations. If a count $X$ has $P(X = 0) > 0$, then $E[1/X]$ is infinite or undefined: ratios with a count in the denominator need a pseudocount or a model ([[Data Transformation]]).
- **Measure theory.** $E[X] = \int_\Omega X \, dP$ is a Lebesgue integral over the [[Probability Space]]; linearity of expectation is linearity of the integral, and the discrete sum and the density integral are two special cases.

## Mathematical representation

- **Over outcomes.** On a countable $\Omega$, $E[X] = \sum_{\omega \in \Omega} X(\omega) P(\{\omega\})$; grouping outcomes with the same value gives $\sum_x x\, p_X(x)$.
- **Linearity.** $E[aX + bY] = \sum_\omega \big(aX(\omega) + bY(\omega)\big) P(\{\omega\}) = aE[X] + bE[Y]$. No independence is used.
- **Indicator.** $E[\mathbf{1}_A] = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)$.
- **LOTUS and products.** $E[g(X)] = \sum_x g(x)\, p_X(x)$, or $\int g(x) f(x)\, dx$ for a density; for independent $X, Y$, $E[XY] = \sum_{x, y} xy\, p_X(x) p_Y(y) = E[X]\,E[Y]$.
- **Word counts.** For $s = s_1 \dots s_n$ and $w = w_1 \dots w_k$, $N_w = \sum_{i=1}^{n-k+1} I_i$ with $I_i = \mathbf{1}\{s_i \dots s_{i+k-1} = w\}$. With i.i.d. bases of probabilities $\pi$, $E[N_w] = (n - k + 1)\prod_{j=1}^{k} \pi_{w_j}$, which is $(n - k + 1)/4^k$ for uniform bases. On a circular sequence every position starts a window: $n \prod_j \pi_{w_j}$.

## Computational representation

An expectation is a weighted sum over a PMF; an expected count is checked by simulating sequences and counting. Counting needs care: `str.count` counts **non-overlapping** occurrences, which undercounts self-overlapping words.

```python
import random
from fractions import Fraction


def expectation(pmf: dict) -> Fraction:
    """E[X]: the sum of x * p(x) over the support."""
    return sum(x * p for x, p in pmf.items())


def count_overlapping(seq: str, word: str) -> int:
    """Occurrences of word in seq, overlapping ones included."""
    count, i = 0, seq.find(word)
    while i != -1:
        count += 1
        i = seq.find(word, i + 1)
    return count


# X = number of A in a random 3-mer (i.i.d. uniform bases): from the PMF, then by linearity
q = Fraction(1, 4)
X = {0: (1 - q) ** 3, 1: 3 * q * (1 - q) ** 2, 2: 3 * q ** 2 * (1 - q), 3: q ** 3}
print("E[X] =", expectation(X), "| linearity: 3 x 1/4 =", 3 * q)

# Count of a 4-mer in 2,000 random 10 kb sequences: simulation against (n - k + 1) / 4^k
rng = random.Random(9)
n, k, reps = 10_000, 4, 2_000
seqs = ["".join(rng.choices("ACGT", k=n)) for _ in range(reps)]
print("formula:", round((n - k + 1) / 4 ** k, 2))
for word in ("ACGT", "AAAA"):
    counts = [count_overlapping(s, word) for s in seqs]
    mean = sum(counts) / reps
    sd = (sum((c - mean) ** 2 for c in counts) / (reps - 1)) ** 0.5
    print(f"{word}: mean {mean:.2f}, SD {sd:.2f}, range {min(counts)}-{max(counts)}")
print("AAAAAA:", "AAAAAA".count("AAAA"), "with str.count,", count_overlapping("AAAAAA", "AAAA"), "with overlaps")
```

```text
E[X] = 3/4 | linearity: 3 x 1/4 = 3/4
formula: 39.05
ACGT: mean 39.17, SD 6.08, range 20-62
AAAA: mean 38.91, SD 7.97, range 11-73
AAAAAA: 1 with str.count, 3 with overlaps
```

Both simulated means sit within sampling noise of $9997/256 = 39.05$; the wider range of AAAA is the clumping discussed in Deeper (L2). With `str.count`, AAAA would appear rarer than ACGT although both have the same expectation.

## Worked example

> [!example] How many EcoRI sites should *E. coli* have by chance?
> EcoRI cuts DNA at the site GAATTC.[^alberts] The *E. coli* K-12 chromosome is one circular molecule of 4,639,221 bp.[^blattner]
> 1. **Model.** Independent, uniform bases: a null model to compare the genome with, not a description of it.
> 2. **Indicators.** On a circle each of the $n$ positions starts a window, so $N = \sum_{i=1}^{n} I_i$ with $P(I_i = 1) = 4^{-6} = 1/4096$.
> 3. **Expectation.** $E[N] = 4{,}639{,}221 / 4096 \approx 1132.6$. The linear formula, $(n - 5)/4096$, gives the same value to one decimal: end effects are negligible for genomes.
> 4. **Strands.** GAATTC is its own reverse complement (a reverse palindrome, see [[DNA]]), so scanning one strand counts each double-stranded site once. A non-palindromic 6-mer must be counted on both strands: $2n/4096 \approx 2265$.
> 5. **Fragments.** Cutting a circle at $N$ sites gives $N$ fragments of total length $n$, so the mean fragment length is $n/N \approx 4096$ bp: one site per $4^k$ bases for a $k$-base site. Strictly $E[n/N] \ne n/E[N]$ (Deeper (L2)), but $N$ stays close to 1133, so the approximation is good.
> 6. **Reading an observation.** A count far from 1133 says that, for this word, the genome departs from the uniform model (composition, dependence between neighbouring bases, or biology acting on the word). Deciding what "far" means requires the [[Variance]] or the whole distribution of $N$, not its mean alone.

## Common misconceptions

> [!warning] "Linearity of expectation needs independence"
> It never does. Overlapping windows are dependent, yet the expected count of a word is the sum of the window probabilities. Independence is needed for $E[XY] = E[X]E[Y]$ and for adding variances ([[Variance]]), not for adding means.

> [!warning] "The expected value is the value to expect"
> 2.44 GAATTC sites in 10 kb is not a possible count, and in the 3-mer example the mean $3/4$ is not the most likely value. For skewed counts the mean can sit far from the typical value ([[Measure of Central Tendency]]).

> [!warning] "The mean of the logs is the log of the mean"
> For counts 1, 10 and 100, the mean of $\log_{10}$ is 1 while $\log_{10}$ of the mean is 1.57. $E[g(X)] = g(E[X])$ holds for linear $g$ only.

## Exercises

> [!question] Exercise 1 (L1)
> A 150-base read has error probability 0.001 at each of its first 100 bases (Phred quality 30) and 0.01 at each of its last 50 (quality 20). What is the expected number of sequencing errors in the read? Did you need the errors at different positions to be independent?

> [!success]- Solution
> Phred quality $Q$ means error probability $10^{-Q/10}$ ([[Phred Quality Score]]).[^cock] Write the number of errors as $\sum_{i=1}^{150} E_i$ with $E_i$ the error indicator of base $i$. By linearity, $E\left[\sum E_i\right] = 100 \times 0.001 + 50 \times 0.01 = 0.1 + 0.5 = 0.6$. No independence is needed. It would be needed for the distribution of the number of errors, for instance $P(\text{no error})$ ([[Bernoulli Distribution]]).

> [!question] Exercise 2 (L1)
> In a random 2 Mb sequence with independent, uniform bases, what is the expected number of occurrences of the 6-mer TTGACA on the given strand, and on both strands? What is the expected count of a given 8-mer and of a given 12-mer on one strand? What does the 12-mer value say about exact matches as evidence?

> [!success]- Solution
> One strand: $(2{,}000{,}000 - 5)/4^6 = 488.3$. TTGACA is not its own reverse complement (that is TGTCAA), so both strands give $2 \times 488.3 = 976.6$. A given 8-mer: $(2 \times 10^6 - 7)/65{,}536 = 30.5$; a 12-mer: $(2 \times 10^6 - 11)/16{,}777{,}216 = 0.12$. A 6-mer match is everywhere by chance, while an exact 12-mer match is unexpected at this scale, which is why exact matches of a dozen or more bases are informative ([[Seed and Extend]]).

> [!question] Exercise 3 (L2)
> An invented 1 kb sequence contains 220 C, 230 G and 12 occurrences of the dinucleotide CG. Compute the expected number of CG under independent bases with these frequencies, the observed/expected ratio, and interpret it.

> [!success]- Solution
> There are 999 dinucleotide windows, each equal to CG with probability $0.22 \times 0.23 = 0.0506$: $E = 999 \times 0.0506 = 50.5$. Observed/expected $= 12/50.5 = 0.24$, which is Karlin and Burge's $\rho_{CG}$ computed from frequencies.[^karlin] CG is about four times rarer than base composition predicts, the kind of depletion seen in the human genome, where methylated C is lost by mutation to T.[^durbin3] Regions with much higher ratios stand out as candidate [[CpG Island|CpG islands]].

> [!question] Exercise 4 (L2, Python)
> In a random sequence with independent, uniform bases, codons are read until the first stop codon (included). Use the tail-sum formula to show that the expected number of codons is $64/3$, then check by simulation.

> [!success]- Solution
> Each codon is a stop with probability $q = 3/64$, independently, so $X \ge j$ means the first $j - 1$ codons are not stops: $P(X \ge j) = (1 - q)^{j-1}$. Then $E[X] = \sum_{j \ge 1} (1-q)^{j-1} = 1/q = 64/3$ (a geometric series, [[Infinite Series]]).
>
> ```python
> import random
>
> STOPS = {"TAA", "TAG", "TGA"}
> q = len(STOPS) / 64                      # P(a random codon is a stop)
>
>
> def codons_until_stop(rng: random.Random) -> int:
>     """Number of random codons read up to and including the first stop."""
>     j = 1
>     while "".join(rng.choices("ACGT", k=3)) not in STOPS:
>         j += 1
>     return j
>
>
> tail_sum = sum((1 - q) ** (j - 1) for j in range(1, 2_000))      # sum of P(X >= j)
> rng = random.Random(3)
> draws = [codons_until_stop(rng) for _ in range(100_000)]
> print(round(1 / q, 3), round(tail_sum, 3), round(sum(draws) / len(draws), 3))
> # 21.333 21.333 21.304
> ```
>
> Formula, truncated tail sum and simulation agree. Random open reading frames are therefore short, which is why long ORFs are evidence of genes ([[Genetic Code#Mathematical representation]]).

> [!question] Exercise 5 (L3, Python)
> Let $D_k$ be the number of **distinct** k-mers in a random sequence of length $n$. Write $D_k$ as a sum of indicators over the $4^k$ possible words, approximate $E[D_k]$, and compare with a simulated sequence of $n = 100{,}000$ bases for $k = 6, 8, 10, 12$. When do k-mers become nearly unique?

> [!success]- Solution
> $D_k = \sum_{w} \mathbf{1}\{N_w \ge 1\}$, so $E[D_k] = \sum_w P(N_w \ge 1)$. Approximating each $N_w$ by a Poisson count of mean $\lambda = (n-k+1)/4^k$ ([[Poisson Distribution]]) gives $E[D_k] \approx 4^k (1 - e^{-\lambda})$; the approximation ignores the clumping of self-overlapping words.
>
> ```python
> import math
> import random
>
> rng = random.Random(5)
> n = 100_000
> seq = "".join(rng.choices("ACGT", k=n))
> for k in (6, 8, 10, 12):
>     lam = (n - k + 1) / 4 ** k                       # expected count of each k-mer
>     expected = 4 ** k * (1 - math.exp(-lam))         # sum over all k-mers of P(present)
>     observed = len({seq[i:i + k] for i in range(n - k + 1)})
>     print(k, n - k + 1, round(expected), observed)
> # 6 99995 4096 4096
> # 8 99993 51285 51320
> # 10 99991 95371 95311
> # 12 99989 99692 99688
> ```
>
> At $k = 6$ every possible word is present (saturation); at $k = 12$, 99.7 % of the windows carry a k-mer seen nowhere else. Uniqueness needs $4^k \gg n$, i.e. $k$ well above $\log_4 n$ (8.3 here, about 15.7 for $3 \times 10^9$ bases). This is a lower bound from the random model: any repeat longer than $k$ in a real genome makes its k-mers non-unique, which drives the choice of $k$ in [[De Bruijn Graph|de Bruijn assembly]] and [[K-mer Spectrum|k-mer spectra]].

## Mastery checklist

- [ ] 1 Recognized: I can define $E[X]$ as a probability-weighted average and compute it from a PMF.
- [ ] 2 Understood: I can explain why linearity holds without independence, why $E[1_A] = P(A)$, and why $E[g(X)] \ne g(E[X])$.
- [ ] 3 Practiced: I can derive expected counts with indicators (k-mers on one or both strands, dinucleotides, errors per read) and check them by simulation, counting overlapping occurrences correctly.
- [ ] 4 Applied: in [[05-sequence-search]], I compare observed k-mer or motif counts in real sequences with their expected counts under a composition-matched model.
- [ ] 5 Explained: I can teach why equal means can hide different distributions (self-overlapping words), how observed/expected ratios work, and how expectations define E-values and the FDR.

## References

[^blitz4]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 4 "Expectation" (definition, linearity, indicator random variables and the fundamental bridge, LOTUS).
[^1805-4b]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 4b "Discrete Random Variables: Expected Value".
[^stat110]: [[Harvard Stat 110 - Probability]], random variables, expectation and indicator random variables.
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of inequalities (Jensen's inequality).
[^durbin2]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (significance of local alignment scores).
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models" (the CpG island example: CG rarer than expected from the frequencies of C and G).
[^karlin]: [[Karlin 1995 - Dinucleotide Relative Abundance Extremes]], Karlin S, Burge C, *Trends in Genetics* 11(7):283-290: relative abundance as observed over expected from base composition, a genomic signature.
[^bh]: [[Benjamini 1995 - Controlling the False Discovery Rate]], Benjamini Y, Hochberg Y, *J R Stat Soc B* 57(1):289-300: the FDR as the expected proportion of falsely rejected hypotheses.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* 277:1453-1462: one circular chromosome of 4,639,221 bp.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), restriction enzymes and the EcoRI site.
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* 38(6):1767-1771: Phred quality $Q = -10 \log_{10} p$.
