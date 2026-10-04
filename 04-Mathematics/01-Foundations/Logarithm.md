---
aliases:
  - Log
  - Natural Logarithm
  - ln
  - log2
  - log10
  - Log Scale
  - Logarithme
tags:
  - type/concept
  - domain/mathematics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Exponential Function]]"
  - "[[Function]]"
related:
  - "[[Log Fold Change]]"
  - "[[Phred Quality Score]]"
  - "[[FASTQ Format]]"
  - "[[pH]]"
  - "[[Shannon Entropy]]"
  - "[[Summation Notation]]"
  - "[[Binary Search]]"
  - "[[Big O Notation]]"
  - "[[Numerical Stability]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Information Theory, Inference, and Learning Algorithms (MacKay)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]]"
  - "[[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Logarithm

> [!abstract]
> The logarithm answers "which power?": $\log_2 8 = 3$ because $2^3 = 8$. It turns products into sums and ratios into differences, which is why fold changes, Phred qualities, pH and information are all measured on log scales.

## Definition

For a base $a > 0$ with $a \ne 1$ and a number $x > 0$, the **logarithm** $\log_a x$ is the unique real $y$ such that $a^y = x$. The function $\log_a : (0, \infty) \to \mathbb{R}$ is the inverse of the [[Exponential Function]] $y \mapsto a^y$.[^calc] Three bases dominate: the **natural logarithm** $\ln x = \log_e x$, the **common logarithm** $\log_{10} x$ and the **binary logarithm** $\log_2 x$.[^calc]

## Why it matters

- **Fold changes.** Expression changes are compared as $\log_2$ ratios: a doubling is $+1$, a halving $-1$, no change $0$ ([[Log Fold Change]], [[Gene Expression]]).[^holmes]
- **Base qualities.** A FASTQ quality is $Q = -10 \log_{10} p$, with $p$ the probability that the base call is wrong ([[FASTQ Format]], [[Phred Quality Score]], [[10-genomic-pipeline]]).[^cock]
- **pH.** $\mathrm{pH} = -\log_{10}[\mathrm{H_3O^+}]$ ([[pH]]).[^chem]
- **Information.** An outcome of probability $p$ carries $\log_2(1/p)$ bits; entropy averages it ([[Shannon Entropy]]).[^mackay]
- **Likelihoods and scores.** $\log \prod = \sum \log$ turns a likelihood over thousands of sites into a sum that does not underflow ([[Summation Notation#Core (L1)]], [[08-phylogenetic-engine]]); substitution matrix entries are log-odds scores, BLOSUM ones in half-bits ([[Substitution Matrix]]).[^henikoff]

## Core (L1)

### Logarithm as inverse

$\log_a(a^y) = y$ and $a^{\log_a x} = x$. Examples: $\log_2 64 = 6$, $\log_{10} 0.001 = -3$, $\ln e^3 = 3$, $\log_2 \frac{1}{8} = -3$, and $\log_a 1 = 0$ in every base. The logarithm of 0 or of a negative number is undefined: no power of a positive base reaches them.

### Rules

For $x, y > 0$ and real $r$:[^calc]

| Rule | Formula | Comes from |
|---|---|---|
| product | $\log_a(xy) = \log_a x + \log_a y$ | $a^u a^v = a^{u+v}$ |
| quotient | $\log_a(x/y) = \log_a x - \log_a y$ | $a^u / a^v = a^{u-v}$ |
| power | $\log_a(x^r) = r \log_a x$ | $(a^u)^r = a^{ur}$ |
| change of base | $\log_a x = \dfrac{\log_b x}{\log_b a}$ | $x = a^{\log_a x}$ |

There is no rule for $\log_a(x + y)$. By change of base, $\log_2 1000 = \log_{10} 1000 / \log_{10} 2 = 3 / 0.30103 \approx 9.97$: logarithms in different bases differ only by a constant factor.

### Graph

The graph of $\log_a x$ is the mirror image of $a^x$ across the line $y = x$: it passes through $(1, 0)$, is defined only for $x > 0$, plunges to $-\infty$ near 0 (vertical asymptote $x = 0$) and rises without bound, but slowly.[^calc] It is negative for $0 < x < 1$, which is why $\log p < 0$ for a probability and Phred and pH carry a minus sign.

### Linearizing exponentials

![[exponential-linear-vs-log-axis.svg]]

Taking $\log_2$ of $N(t) = N_0 \cdot 2^{t/T_d}$ gives
$$\log_2 N(t) = \log_2 N_0 + \frac{t}{T_d},$$
a straight line in $t$ with slope $1/T_d$ doublings per unit time. On a log axis (right panel), exponential growth and decay become lines, and the slope gives the doubling time or half-life. A **power law** $y = c x^b$ becomes a line on **log-log** axes, $\log y = \log c + b \log x$ ([[Power Law]]).

### Reading a log scale

On a log axis, **equal distances are equal ratios**: 1 to 10 is as far as 10 to 100. One unit of $\log_{10}$ is an order of magnitude, one unit of $\log_2$ a doubling. Quantities that range from thousands to billions, such as genome sizes, are plotted this way ([[Genome]]).

### Bio: four log scales

| Quantity | Definition | One unit means | Example |
|---|---|---|---|
| log2 fold change | $\log_2(B/A)$ | a factor 2 | $+2$ = four times more; $-1$ = half[^holmes] |
| Phred quality | $Q = -10 \log_{10} p$ | 10 units = a factor 10 in error probability | $Q = 20$: $p = 0.01$; $Q = 30$: $p = 0.001$[^cock] |
| pH | $-\log_{10}[\mathrm{H_3O^+}]$ | a factor 10 in $[\mathrm{H_3O^+}]$ | pH 7 at $10^{-7}$ M[^chem] |
| information | $\log_2(1/p)$ bits | halving the probability | one of 4 equiprobable bases: 2 bits[^mackay] |

Each scale replaces a multiplicative question ("how many times more?") by an additive one ("how many units apart?"). Details of quality encoding live in [[FASTQ Format]]; this note only supplies the logarithm.

## Deeper (L2)

**Natural logarithm and calculus.** $\frac{d}{dx} \ln x = \frac{1}{x}$, and $\ln x = \int_1^x \frac{dt}{t}$.[^calc-v1] For small $x$, $\ln(1 + x) \approx x$: a log difference is close to a relative change ($\ln 1.05 \approx 0.049$), so changes of a few percent read directly on the natural-log scale ([[Linear Approximation]]).

**Log-transforming data.** Biological effects are often multiplicative (a drug halves expression whatever its baseline), and on the log scale they become additive and comparable across genes. Positive, right-skewed data such as counts and intensities also become more symmetric. Because $\log 0$ is undefined, analysts add a **pseudocount** $c$ and compute $\log_2\frac{y_B + c}{y_A + c}$; the choice of $c$ dominates the result for low counts (Exercise 3).[^holmes] See [[Gene Expression#Mathematical representation]].

**Averaging ratios.** The mean of $\log$ ratios is the log of their **geometric mean**: $\frac{1}{n}\sum_i \log r_i = \log \big(\prod_i r_i\big)^{1/n}$. A 4-fold increase and a 4-fold decrease average to $\log_2$ ratio 0 (no net change), whereas the arithmetic mean of the ratios, $(4 + 0.25)/2 = 2.125$, suggests a doubling.

**Units of information.** With base 2 the unit is the **bit**, with base $e$ the **nat**; $1\ \text{nat} = 1/\ln 2 \approx 1.443$ bits. The entropy $H = -\sum_x p(x) \log_2 p(x)$ is the average information per outcome: 2 bits for a uniform nucleotide, less for a biased composition ([[Shannon Entropy]]).[^mackay]

**qPCR cycles are a log scale.** With perfect doubling, the threshold cycle is $C_T = \log_2(N_\theta / N_0)$ for threshold amount $N_\theta$ and starting amount $N_0$, so a sample with 8 times more template crosses the threshold $\log_2 8 = 3$ cycles earlier. The $2^{-\Delta\Delta C_T}$ method converts cycle differences back to fold changes (Worked example).[^livak]

## Advanced (L3)

- **Halvings and algorithms.** $\log_2 n$ counts how many times $n$ can be halved before reaching 1: [[Binary Search]] in a sorted array of $n$ items needs about $\log_2 n$ comparisons, 32 for $3 \times 10^9$ positions, and a balanced binary tree of $n$ leaves has depth about $\log_2 n$. In [[Big O Notation]] the base is omitted because changing it multiplies by a constant.
- **Bits and k-mers.** Indexing one of $m$ items needs $\lceil \log_2 m \rceil$ bits; a k-mer over 4 letters carries $2k$ bits. A random k-mer is expected about $L / 4^k$ times in a sequence of length $L$, so a k-mer is likely to point to a single place only once $4^k \gtrsim L$, that is $k \gtrsim \log_4 L$ (Exercise 4) ([[K-mer]]).
- **Log-space arithmetic.** Products of probabilities are computed as sums of logs; sums of probabilities need log-sum-exp ([[Summation Notation#Advanced (L3)]], [[Numerical Stability]]). `math.log1p(x)` computes $\ln(1 + x)$ accurately when $x$ is tiny, where `math.log(1 + x)` loses digits ([[Floating-Point Arithmetic]]).
- **Log-odds.** A score $\log \frac{P(\text{data} \mid \text{related})}{P(\text{data} \mid \text{random})}$ is positive when the data favor relatedness and adds over independent positions; BLOSUM matrices store $2 \log_2$ of such ratios, rounded.[^henikoff] The same form underlies [[Position Weight Matrix|position weight matrices]] and [[Bayes' Theorem|Bayesian]] log-odds.

## Mathematical representation

- $\log_a : (0, \infty) \to \mathbb{R}$ with $a^{\log_a x} = x$ and $\log_a(a^y) = y$: a bijection, inverse of $y \mapsto a^y$ ([[Function]]).
- **Product rule, proved.** Let $u = \log_a x$ and $v = \log_a y$. Then $a^{u+v} = a^u a^v = xy$, so $\log_a(xy) = u + v$. The quotient and power rules follow the same way.
- **Change of base, proved.** Apply $\log_b$ to $x = a^{\log_a x}$: $\log_b x = \log_a x \cdot \log_b a$.
- **Fold changes.** $\mathrm{LFC}(A \to B) = \log_2(B/A)$ is antisymmetric, $\mathrm{LFC}(B \to A) = -\mathrm{LFC}(A \to B)$, and additive along a series, $\log_2(C/A) = \log_2(C/B) + \log_2(B/A)$.
- **Phred.** $Q = -10\log_{10} p \iff p = 10^{-Q/10}$; $Q + 10$ corresponds to $p/10$.[^cock]
- **Information.** $I(p) = -\log_2 p$; for independent events $I(pq) = I(p) + I(q)$. Additivity over independent events is the reason information is measured with a logarithm.[^mackay]
- **Semi-log fit.** If $N(t) = N_0 e^{kt}$, then $\ln N(t) = \ln N_0 + kt$: a linear regression of $\ln N$ on $t$ estimates $k$, and $T_d = \ln 2 / k$ ([[Least Squares]]).

## Computational representation

`math.log(x)` is $\ln x$, `math.log(x, b)` any base; `math.log2` and `math.log10` are more accurate for their bases. `statistics.linear_regression` (Python 3.10+) fits the semi-log line:

```python
import math
from statistics import linear_regression

print(math.log2(64), math.log10(0.001), math.log(math.e ** 3), math.log2(1 / 8))
print(round(math.log(1000, 2), 4), round(math.log10(1000) / math.log10(2), 4))   # change of base


def log2_fold_change(a: float, b: float, pseudocount: float = 0.0) -> float:
    """log2(b / a): +1 = doubled, -1 = halved, 0 = unchanged."""
    return math.log2((b + pseudocount) / (a + pseudocount))


def phred(p: float) -> float:
    return -10 * math.log10(p)


def ph(h: float) -> float:
    """pH from the hydronium concentration in mol/L."""
    return -math.log10(h)


def bits(p: float) -> float:
    """Information content of an outcome of probability p."""
    return -math.log2(p)


print(log2_fold_change(50, 200), log2_fold_change(200, 50), log2_fold_change(80, 80))
print([round(phred(p), 1) for p in (0.1, 0.01, 0.001, 1 / 2000)])
print(round(ph(1e-7), 2), round(ph(4.0e-8), 2))
print(bits(1 / 4), bits(1 / 64), round(bits(1 / 20), 3))

t = [0, 30, 60, 90, 120]                       # minutes
od = [0.051, 0.098, 0.205, 0.396, 0.81]        # invented optical densities
slope, intercept = linear_regression(t, [math.log2(v) for v in od])
print(round(slope, 5), round(1 / slope, 1))    # doublings per minute, doubling time

try:
    math.log(0)
except ValueError as err:
    print("ValueError:", err)
print(math.log1p(1e-12), math.log(1 + 1e-12))
```

```text
6.0 -3.0 3.0 -3.0
9.9658 9.9658
2.0 -2.0 0.0
[10.0, 20.0, 30.0, 33.0]
7.0 7.4
2.0 6.0 4.322
0.03331 30.0
ValueError: math domain error
9.999999999995e-13 1.000088900581841e-12
```

A codon of 64 equiprobable values carries 6 bits, an amino acid among 20 equiprobable ones 4.32 bits. The fit on $\log_2$ OD gives a slope of 0.0333 doublings per minute, a 30-minute doubling time. `math.log(0)` raises an error instead of returning $-\infty$, so zero counts must be handled explicitly. The last line shows `log(1 + x)` wrong from the fifth digit for $x = 10^{-12}$, while `log1p` is exact.

## Worked example

> [!example] From qPCR cycles to a fold change (invented Ct values)
> A target gene and a reference gene are measured by qPCR in a control and a treated sample, assuming perfect doubling ([[Quantitative Polymerase Chain Reaction]]).
>
> | Sample | $C_T$ target | $C_T$ reference | $\Delta C_T$ = target − reference |
> |---|---:|---:|---:|
> | control | 24.0 | 18.0 | 6.0 |
> | treated | 21.5 | 18.2 | 3.3 |
>
> 1. **Cycles are $\log_2$ units.** Each cycle doubles the product, so crossing the threshold one cycle earlier means twice as much starting template.
> 2. **Normalize** to the reference gene: $\Delta C_T$ removes differences in input amount between samples.
> 3. **Compare** to the control: $\Delta\Delta C_T = 3.3 - 6.0 = -2.7$.
> 4. **Back to a ratio**: fold change $= 2^{-\Delta\Delta C_T} = 2^{2.7} \approx 6.5$, so the $\log_2$ fold change is $+2.7$.[^livak]
> 5. **Sanity check**: a 6.5-fold increase is between $2^2 = 4$ and $2^3 = 8$, consistent with a target crossing about 2.5 cycles earlier while the reference barely moves.

## Common misconceptions

> [!warning] "$\log(x + y) = \log x + \log y$"
> Logarithms turn **products** into sums: $\log(xy) = \log x + \log y$. $\log_{10}(10 + 10) = 1.30$, not $2$.

> [!warning] "A log2 fold change of −2 is a small decrease"
> $-2$ means $2^{-2} = 1/4$: the gene lost three quarters of its expression. Each unit is a factor 2, so $-1$ is already a halving.

> [!warning] "Q40 is a third better than Q30"
> Phred is logarithmic: Q30 means $p = 10^{-3}$, Q40 $p = 10^{-4}$, ten times fewer expected errors.[^cock] Averaging Q values hides bad bases for the same reason (see [[FASTQ Format]]).

> [!warning] "Averaging ratios directly is fine"
> The arithmetic mean of fold changes is pulled up by increases: 4 and 1/4 average to 2.125. Average on the log scale (mean $\log_2$ ratio 0), which treats a doubling and a halving symmetrically.

## Exercises

> [!question] Exercise 1 (L1)
> Compute without a calculator: $\log_2 64$, $\log_{10} 0.001$, $\ln e^3$, $\log_2 \frac{1}{8}$, $\log_3 1$. Then express $\log_2 1000$ with $\log_{10}$, given $\log_{10} 2 \approx 0.301$.

> [!success]- Solution
> $6$, $-3$, $3$, $-3$, $0$ (by inversion: which power of the base gives the number?). $\log_2 1000 = \log_{10} 1000 / \log_{10} 2 = 3 / 0.301 \approx 9.97$, so $1000 \approx 2^{10} = 1024$.

> [!question] Exercise 2 (L1)
> (a) Which Phred score corresponds to an error probability of 1 in 2,000? (b) Which error probabilities do Q20 and Q35 encode? (c) A solution has $[\mathrm{H_3O^+}] = 4.0 \times 10^{-8}$ M; give its pH. How many times more $\mathrm{H_3O^+}$ does a solution at pH 6.4 contain?

> [!success]- Solution
> (a) $Q = -10 \log_{10}(1/2000) = 10 \log_{10} 2000 \approx 33.0$. (b) $10^{-2} = 0.01$ and $10^{-3.5} \approx 3.2 \times 10^{-4}$. (c) $\mathrm{pH} = -\log_{10}(4.0 \times 10^{-8}) = 8 - \log_{10} 4 \approx 7.40$. One pH unit lower is $10^{1} = 10$ times more $\mathrm{H_3O^+}$.

> [!question] Exercise 3 (L2)
> (a) Gene X goes from 100 to 400 normalized counts and gene Y from 400 to 100. Compare the mean of their fold changes with the mean of their $\log_2$ fold changes. (b) Gene Z goes from 0 to 5 counts and gene W from 100 to 300. Compute their $\log_2$ fold changes with pseudocounts 0.5 and 1.

> [!success]- Solution
> (a) Ratios 4 and 0.25: arithmetic mean 2.125, an apparent doubling; $\log_2$ ratios $+2$ and $-2$: mean 0, no net change, the symmetric answer. (b) Z: $\log_2(5.5/0.5) = 3.46$ with $c = 0.5$, $\log_2(6/1) = 2.58$ with $c = 1$. W: $1.585$ and $1.575$. The pseudocount barely affects well-expressed genes but changes a low-count fold change by almost one unit, which is why low counts need statistical shrinkage rather than raw ratios ([[Log Fold Change]]).[^holmes]

> [!question] Exercise 4 (L2)
> The T2T-CHM13 human genome assembly is about $3.055 \times 10^9$ bp.[^nurk] (a) How many bits does it take to name one position? (b) How many steps does a binary search over all positions need? (c) What is the smallest $k$ with $4^k$ at least the genome length?

> [!success]- Solution
> (a) $\lceil \log_2(3.055 \times 10^9) \rceil = 32$ bits: a 32-bit integer suffices. (b) The same, about 32 halvings ([[Binary Search]]). (c) $k \ge \log_4 L = \log_2 L / 2 \approx 15.75$, so $k = 16$. Below that length, a random k-mer is expected to occur by chance somewhere in the genome; this is a lower bound, since real genomes are repetitive.

> [!question] Exercise 5 (L3, Python)
> Invented optical densities every 30 minutes: `0.051, 0.098, 0.205, 0.396, 0.81, 1.2, 1.3`. Estimate the doubling time by regressing $\log_2$ OD on time using the first 5 points, then using all 7. Explain the difference and how a log plot reveals it.

> [!success]- Solution
> ```python
> import math
> from statistics import linear_regression
>
> t2 = [0, 30, 60, 90, 120, 150, 180]
> od2 = [0.051, 0.098, 0.205, 0.396, 0.81, 1.2, 1.3]   # invented: plateau after 120 min
> for n in (5, 7):
>     s, _ = linear_regression(t2[:n], [math.log2(v) for v in od2[:n]])
>     print(n, round(1 / s, 1))
> ```
> Output: `5 30.0`, then `7 36.2`. The last two points belong to the stationary phase: on a $\log_2$ axis they bend away from the line, and including them flattens the slope and inflates the doubling time by 20 %. Fit only the range where $\log N$ is linear in $t$, which a semi-log plot shows at a glance and a linear plot hides ([[Exponential Function#Worked example]]).

## Mastery checklist

- [ ] 1 Recognized: I can define $\log_a x$ as the inverse of $a^x$ and name ln, $\log_{10}$ and $\log_2$.
- [ ] 2 Understood: I can explain why log scales turn ratios into distances and read log2 fold changes, Phred scores, pH and bits.
- [ ] 3 Practiced: I can apply the rules and change of base, linearize growth data and compute fold changes with pseudocounts in Python.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I converted between qualities and error probabilities and computed log-likelihoods on real reads.
- [ ] 5 Explained: I can teach why information and likelihoods use logarithms, why the base does not matter in Big O, and the pitfalls of $\log 0$ and averaging ratios.

## References

[^calc]: [[Calculus (OpenStax)]], Volume 1, section 1.5 "Exponential and Logarithmic Functions" (logarithmic functions as inverses of exponentials, properties, change of base).
[^calc-v1]: [[Calculus (OpenStax)]], Volume 1 (derivative of the natural logarithm; the logarithm defined as an integral).
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* 38:1767-1771 (Phred quality $Q = -10 \log_{10} p$).
[^chem]: [[Chemistry 2e (OpenStax)]], ch. 14 "Acid-Base Equilibria" (pH as $-\log[\mathrm{H_3O^+}]$).
[^mackay]: [[Information Theory, Inference, and Learning Algorithms (MacKay)]], probability and entropy material (Shannon information content, entropy, bits).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], material on count data from high-throughput sequencing (log transformations, fold changes, differential expression).
[^livak]: [[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]], *Methods* 25:402-408 (threshold cycle and the $2^{-\Delta\Delta C_T}$ method).
[^henikoff]: [[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]], *PNAS* 89:10915-10919 (log-odds scores in half-bit units).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* 376:44-53 (T2T-CHM13 assembly, 3.055 Gbp).
