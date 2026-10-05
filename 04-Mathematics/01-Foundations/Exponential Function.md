---
aliases:
  - Exponential
  - exp
  - Natural Exponential Function
  - Doubling Time
  - Fonction exponentielle
tags:
  - type/concept
  - domain/mathematics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Function]]"
related:
  - "[[Logarithm]]"
  - "[[Exponential Growth]]"
  - "[[Logistic Growth]]"
  - "[[Derivative]]"
  - "[[Ordinary Differential Equation]]"
  - "[[Polymerase Chain Reaction]]"
  - "[[Bacterial Growth]]"
  - "[[Messenger RNA]]"
  - "[[Taylor Series]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Saiki 1988 - Primer-Directed Enzymatic Amplification of DNA]]"
  - "[[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]]"
  - "[[Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
---

# Exponential Function

> [!abstract]
> An exponential function multiplies its value by the same factor at every step of equal length: PCR doubles its product each cycle, a bacterial culture doubles each generation, and an mRNA population halves each half-life.

## Definition

For a base $a > 0$ with $a \ne 1$, the **exponential function with base $a$** is $f(x) = a^x$, defined for every real $x$; the variable is in the exponent, unlike the power function $x^a$.[^calc] The **natural exponential function** uses the base $e \approx 2.718281828$, the limit of $(1 + 1/m)^m$ as $m \to \infty$, and is written $e^x$ or $\exp(x)$.[^calc] Its domain is $\mathbb{R}$, its image is $(0, \infty)$; it increases when $a > 1$ and decreases when $0 < a < 1$.[^calc]

## Why it matters

- **PCR.** Each cycle of denaturation, primer annealing and extension can copy every target molecule, so the product grows by a factor of up to 2 per cycle ([[Polymerase Chain Reaction]]).[^saiki] Quantitative PCR reads the starting amount off this exponential phase ([[Quantitative Polymerase Chain Reaction]]).[^livak]
- **Bacterial growth.** Binary fission doubles a population every generation time; *E. coli* can double in as little as 20 minutes under optimal laboratory conditions ([[Bacterial Growth]]).[^micro]
- **mRNA decay.** Degradation at a constant rate gives exponential decay with a half-life; in mouse fibroblasts the median mRNA half-life was measured at about 9 h, against 46 h for proteins ([[Messenger RNA]], [[Gene Expression]]).[^schwan]
- **Undoing a logarithm.** Data are often stored on a log scale, and the exponential brings them back: a Phred quality $Q$ becomes an error probability $p = 10^{-Q/10}$ ([[FASTQ Format]], [[Phred Quality Score]], [[10-genomic-pipeline]]).[^cock]
- **Search spaces.** $4^k$ k-mers, $2^n$ subsets, $(2n-5)!!$ tree topologies: exponential sizes are why exhaustive search fails beyond small inputs ([[K-mer]], [[Exhaustive Search]], [[Mathematical Induction#Advanced (L3)]]).

## Core (L1)

### Rules

For $a, b > 0$ and real $x, y$:[^calc]

| Rule | Formula | Example |
|---|---|---|
| product | $a^x a^y = a^{x+y}$ | $2^3 \cdot 2^2 = 2^5 = 32$ |
| quotient | $a^x / a^y = a^{x-y}$ | $e^5 / e^3 = e^2$ |
| power | $(a^x)^y = a^{xy}$ | $(2^{10})^3 = 2^{30}$ |
| same exponent | $(ab)^x = a^x b^x$ | $10^x = 2^x 5^x$ |
| zero, negative | $a^0 = 1$, $a^{-x} = 1/a^x$ | $2^{-3} = 1/8$ |
| roots | $a^{p/q} = \sqrt[q]{a^p}$ | $8^{2/3} = 4$ |

### Graphs

![[exponential-linear-vs-log-axis.svg]]

Every graph of $a^x$ passes through $(0, 1)$, stays strictly above the horizontal axis and approaches it on one side (the asymptote $y = 0$). For $a > 1$ it rises ever faster; $(1/a)^x = a^{-x}$ is its mirror image across the vertical axis, a decay.[^calc] On a linear axis (left panel) growth looks flat and then explosive. On a logarithmic axis (right panel) the same curves are straight lines, the reason growth data are plotted on log scales ([[Logarithm]]).

### Doubling time and half-life

If a quantity doubles every $T_d$, after time $t$ it has doubled $t/T_d$ times:
$$N(t) = N_0 \cdot 2^{t/T_d}, \qquad M(t) = M_0 \cdot \left(\tfrac{1}{2}\right)^{t/t_{1/2}},$$
the second for a quantity that halves every half-life $t_{1/2}$. What matters is the number of doublings or half-lives elapsed, not the clock time: after 3 half-lives, $1/8$ is left, whatever the molecule.

### Bio: three exponentials

- **PCR** ($t$ counted in cycles, $T_d = 1$ cycle): $N_0 \cdot 2^n$ copies after $n$ ideal cycles, so 30 cycles turn one molecule into $2^{30} \approx 1.07 \times 10^9$ (see [[DNA Replication#Mathematical representation]]). With efficiency $E$, the factor per cycle is $1 + E$, and $N_n = N_0 (1 + E)^n$.[^livak]
- **Bacteria**: with 20-minute doublings, one cell gives $2^{3} = 8$ cells per hour and $2^{18} = 262{,}144$ cells in 6 hours. Real cultures leave this regime: a growth curve has lag, exponential (log), stationary and death phases.[^micro]
- **mRNA**: with a 9-hour half-life, $(1/2)^{24/9} \approx 0.157$ of the molecules present at time 0 remain after 24 hours.

## Deeper (L2)

**Why $e$.** Growth at rate $r$ per unit time, applied in $m$ equal steps, multiplies by $(1 + r/m)^m$ per unit time; as $m \to \infty$ this tends to $e^r$, so continuous growth for a time $t$ multiplies by $e^{rt}$.[^calc] Any base reduces to $e$: $a^x = e^{x \ln a}$, where $\ln$ is the natural [[Logarithm]].

**The derivative.** $\frac{d}{dx} e^x = e^x$ and $\frac{d}{dx} a^x = (\ln a)\, a^x$: the slope of an exponential is proportional to its value ([[Derivative]]).[^calc-v1] Conversely, the solutions of
$$\frac{dN}{dt} = kN \qquad \text{are} \qquad N(t) = N_0 e^{kt},$$
which is the model of [[Exponential Growth]] ($k > 0$) and of first-order decay ($k < 0$) ([[Ordinary Differential Equation]]). The **relative rate** $\frac{1}{N}\frac{dN}{dt} = k$ is constant: that, not "fast", is the signature of an exponential.

**Rate constant and doubling time.** From $e^{k T_d} = 2$: $T_d = \frac{\ln 2}{k}$; likewise $t_{1/2} = \frac{\ln 2}{|k|}$ for decay. A 20-minute doubling time is $k = \ln 2 / 20 \approx 0.0347$ per minute. The synthesis and degradation model of mRNA, $dM/dt = k_s - k_d M$, relaxes to its steady state with half-life $\ln 2 / k_d$ ([[Messenger RNA#Mathematical representation]]); genome-wide studies estimate these rates gene by gene.[^schwan]

**Discrete and continuous.** A per-generation factor $R$ (PCR: $1 + E$) and a continuous rate $k$ describe the same curve when $k = \ln R$ per generation. Models of populations with separated generations use $R^n$; models with overlapping births and deaths use $e^{kt}$.

## Advanced (L3)

- **Series.** $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$ for every real $x$, the [[Taylor Series]] of $\exp$ at 0 ([[Summation Notation]]). The series extends $\exp$ to complex arguments, giving Euler's formula $e^{i\theta} = \cos\theta + i \sin\theta$ ([[Complex Number]]).
- **Rare events.** $(1 + x/n)^n \to e^x$ also gives $(1 - \mu)^L \approx e^{-\mu L}$ for a small per-site probability $\mu$ over many sites $L$: the probability of zero events in the [[Poisson Distribution]] (Exercise 5). The lifetime of a molecule degraded at constant rate $k$ follows the [[Exponential Distribution]], $P(T > t) = e^{-kt}$.
- **Exponential beats polynomial.** For every fixed $d$, $x^d / e^x \to 0$: an algorithm with $2^n$ steps is eventually slower than any polynomial one ([[Big O Notation]]). Counting phylogenetic trees by [[Mathematical Induction]] shows this growth in tree space.
- **Finite precision.** In double precision, $e^x$ overflows for $x$ above about 709.78 and underflows to 0 below about $-745$: probabilities and likelihoods are therefore stored as logarithms and exponentiated only at the end, if at all ([[Floating-Point Arithmetic]], [[Numerical Stability]]).
- **Exponential phases end.** Nutrients, primers and nucleotides run out: PCR reaches a plateau and cultures a stationary phase.[^micro] Models that include the limit are logistic ([[Logistic Growth]]).

## Mathematical representation

- For $a > 0$: $a^0 = 1$, $a^{n+1} = a^n \cdot a$ for integers $n \ge 0$, $a^{-n} = 1/a^n$, $a^{p/q} = (\sqrt[q]{a})^p$, extended to real $x$ by continuity.
- $\exp(x) = \sum_{n \ge 0} x^n / n! = \lim_{m \to \infty} (1 + x/m)^m$, $e = \exp(1)$, and $a^x = \exp(x \ln a)$.
- For $a \ne 1$, $x \mapsto a^x$ is a bijection $\mathbb{R} \to (0, \infty)$ whose inverse is $\log_a$ ([[Function]], [[Logarithm]]).
- **Growth model.** $N(t) = N_0 e^{kt} = N_0 \cdot 2^{t/T_d}$ with $T_d = \ln 2 / k$. Proof of the second form: $2^{t/T_d} = e^{(t/T_d)\ln 2} = e^{kt}$.
- **Ratio form.** $N(t + \Delta) / N(t) = e^{k\Delta}$ does not depend on $t$: equal time steps give equal ratios, which is what a log axis turns into equal distances.

## Computational representation

`math.exp`, `math.e` and the `**` operator cover everything; integer powers such as `2 ** 30` are exact in Python, real exponents are floating point:

```python
import math

a, x, y = 2.0, 3.0, 1.5
print(math.isclose(a**x * a**y, a**(x + y)), math.isclose((a**x) ** y, a**(x * y)))
print(math.e, 2 ** -3, round(8 ** (2 / 3), 10))


def pcr_copies(n0: float, cycles: int, efficiency: float = 1.0) -> float:
    """Copies after some cycles: n0 * (1 + E)^cycles; E = 1 is perfect doubling."""
    return n0 * (1 + efficiency) ** cycles


def grow(n0: float, t: float, doubling_time: float) -> float:
    return n0 * 2 ** (t / doubling_time)


def fraction_left(t: float, half_life: float) -> float:
    return 0.5 ** (t / half_life)


print(f"{pcr_copies(1, 30):.4g} {pcr_copies(1, 30, 0.9):.3g}")
print(grow(1, 6 * 60, 20))                  # 6 h of 20-min doublings
print(round(fraction_left(24, 9), 3))       # 9 h half-life, after 24 h
k = math.log(2) / 20                        # rate constant per minute
print(round(k, 5), math.isclose(math.exp(k * 360), 2 ** 18))
print([10 ** (-q / 10) for q in (10, 20, 30)])   # Phred Q back to error probability

for m in (1, 10, 1000, 10**6):
    print(m, (1 + 1 / m) ** m)
print(round(sum(1 / math.factorial(n) for n in range(18)), 12))

print(f"{math.exp(709):.3e}", math.exp(-746))
try:
    math.exp(710)
except OverflowError as err:
    print("OverflowError:", err)
```

```text
True True
2.718281828459045 0.125 4.0
1.074e+09 2.3e+08
262144.0
0.157
0.03466 True
[0.1, 0.01, 0.001]
1 2.0
10 2.5937424601000023
1000 2.7169239322355936
1000000 2.7182804690957534
2.718281828459
8.218e+307 0.0
OverflowError: math range error
```

$(1 + 1/m)^m$ approaches $e$ slowly (6 correct digits need $m = 10^6$), the series fast (18 terms). `math.exp` raises an error on overflow but returns `0.0` silently on underflow, which is the more dangerous failure.

## Worked example

> [!example] Doubling time of a culture from two readings (invented data)
> Optical density of a culture in exponential phase: 0.05 at $t = 0$ and 0.40 at $t = 90$ min.
> 1. **Ratio**: $0.40 / 0.05 = 8 = 2^3$, so the culture doubled 3 times.
> 2. **Doubling time**: $T_d = 90 / 3 = 30$ min.
> 3. **Rate constant**: $k = \ln 2 / 30 \approx 0.0231$ min⁻¹; check: $e^{0.0231 \times 90} = e^{2.08} \approx 8$.
> 4. **Prediction**: at 150 min, $0.05 \cdot 2^{150/30} = 0.05 \cdot 32 = 1.6$, valid only if the culture is still in exponential phase. A plateau below that value means the stationary phase has started, not that the model is wrong about the earlier points.[^micro]
>
> When the ratio is not a power of 2, the number of doublings is $\log_2$ of the ratio ([[Logarithm#Worked example]]).

## Common misconceptions

> [!warning] "Exponential means very fast"
> $e^{0.001t}$ grows slowly for a long time, and $e^{-kt}$ decreases. An exponential is defined by a **constant relative rate** (equal ratios over equal times), not by speed.

> [!warning] "PCR always gives $2^n$ copies"
> $2^n$ is the ideal. With efficiency $E < 1$ the factor is $1 + E$ per cycle,[^livak] and late cycles plateau as reagents run out. At $E = 0.9$, 30 cycles give $1.9^{30} \approx 2.3 \times 10^8$ copies per template, not $1.07 \times 10^9$.

> [!warning] "$a^{x+y} = a^x + a^y$"
> Exponents add when powers **multiply**: $a^{x+y} = a^x a^y$. For example $2^{3+2} = 32$, while $2^3 + 2^2 = 12$.

> [!warning] "After two half-lives nothing is left"
> Each half-life halves what remains: $1/2$, then $1/4$, then $1/8$. An exponential decay never reaches exactly zero; a population of molecules ends when the last one is degraded, a random event ([[Exponential Distribution]]).

## Exercises

> [!question] Exercise 1 (L1)
> Simplify: (a) $2^5 \cdot 2^{-3}$; (b) $(e^2)^3 / e^4$; (c) $8^{2/3}$; (d) $10^{-3} \cdot 10^{5}$.

> [!success]- Solution
> (a) $2^{5-3} = 4$. (b) $e^{6-4} = e^2 \approx 7.39$. (c) $(\sqrt[3]{8})^2 = 2^2 = 4$. (d) $10^{2} = 100$. Each uses one rule of the table: add exponents for products, multiply them for powers.

> [!question] Exercise 2 (L1)
> A PCR starts from 1,000 template copies. How many copies after 25 ideal cycles? And with an efficiency of 0.9?

> [!success]- Solution
> Ideal: $1000 \cdot 2^{25} = 33{,}554{,}432{,}000 \approx 3.4 \times 10^{10}$. At $E = 0.9$: $1000 \cdot 1.9^{25} \approx 9.3 \times 10^9$. A 10 % loss of efficiency per cycle costs a factor $(2/1.9)^{25} \approx 3.6$ after 25 cycles: small per-step differences compound.

> [!question] Exercise 3 (L2)
> Starting from one *E. coli* cell with a 20-minute doubling time, how many cells after 6 hours of exponential growth? Give the rate constant $k$ per hour. Why can the same growth not continue for 24 hours?

> [!success]- Solution
> 6 h = 18 doublings, so $2^{18} = 262{,}144$ cells. $k = \ln 2 / T_d = \ln 2 / (1/3\ \text{h}) = 3 \ln 2 \approx 2.08$ h⁻¹. 24 h would be 72 doublings, $2^{72} \approx 4.7 \times 10^{21}$ cells: long before that, nutrients run out and the culture enters the stationary phase.[^micro]

> [!question] Exercise 4 (L2)
> An mRNA has a 9-hour half-life, the median measured in mouse fibroblasts.[^schwan] Without new synthesis, what fraction remains after 27 h? After 24 h? How long until only 10 % remains?

> [!success]- Solution
> 27 h is 3 half-lives: $1/8 = 12.5\%$. 24 h: $(1/2)^{24/9} \approx 0.157$. For 10 %: $(1/2)^{t/9} = 0.1$ gives $t = 9 \log_2 10 \approx 29.9$ h, a step that needs the [[Logarithm]].

> [!question] Exercise 5 (L3, Python)
> A process makes an error with probability $\mu = 10^{-6}$ per site, independently over $L = 3 \times 10^6$ sites (invented values). Compare $P(\text{no error}) = (1 - \mu)^L$ with $e^{-\mu L}$, and explain the approximation.

> [!success]- Solution
> ```python
> import math
>
> mu, L = 1e-6, 3_000_000                     # invented
> exact = (1 - mu) ** L
> approx = math.exp(-mu * L)
> print(f"{exact:.10f} {approx:.10f} {abs(exact - approx) / exact:.2e}")
> print(f"{math.exp(L * math.log1p(-mu)):.10f}")
> ```
> Output: `0.0497869937 0.0497870684 1.50e-06`, then `0.0497869937`. Writing $(1 - \mu)^L = (1 + x/L)^L$ with $x = -\mu L = -3$ shows the limit $e^{x} = e^{-3}$; the relative error is about $10^{-6}$. `math.log1p(-mu)` computes $\ln(1 - \mu)$ accurately for tiny $\mu$, the safe way to evaluate such powers. This is the zero class of the [[Poisson Distribution]] with mean $\mu L = 3$.

## Mastery checklist

- [ ] 1 Recognized: I can tell $a^x$ from $x^a$, sketch $2^x$, $e^x$ and $2^{-x}$, and state the rules of exponents.
- [ ] 2 Understood: I can explain doubling time and half-life, why $e$ appears in continuous growth, and why an exponential is a straight line on a log axis.
- [ ] 3 Practiced: I can compute PCR yields with an efficiency, growth and decay over time, and $k$ from $T_d$ in Python.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I converted Phred qualities to error probabilities and reasoned on amplification and growth data from real experiments.
- [ ] 5 Explained: I can teach the link between $dN/dt = kN$, $e^{kt}$ and $2^{t/T_d}$, the limits of exponential models, and overflow in floating point.

## References

[^calc]: [[Calculus (OpenStax)]], Volume 1, section 1.5 "Exponential and Logarithmic Functions" (exponential functions $b^x$, the number $e$, logarithms, change of base).
[^calc-v1]: [[Calculus (OpenStax)]], Volume 1 (derivatives of exponential functions).
[^micro]: [[Microbiology (OpenStax)]], section 9.1 "How Microbes Grow" (binary fission, generation time, *E. coli* doubling in about 20 minutes under optimal conditions, the growth curve and its phases).
[^saiki]: [[Saiki 1988 - Primer-Directed Enzymatic Amplification of DNA]], *Science* 239:487-491 (cycles of denaturation, annealing and extension with Taq polymerase).
[^livak]: [[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]], *Methods* 25:402-408 (exponential amplification with efficiency, threshold cycle).
[^schwan]: [[Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control]], *Nature* 473:337-342 (median half-lives in NIH3T3 cells: about 9 h for mRNAs, 46 h for proteins; synthesis and degradation rates per gene).
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* 38:1767-1771 (Phred quality $Q = -10 \log_{10} p$).
