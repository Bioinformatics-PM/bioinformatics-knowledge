---
aliases:
  - Limit of a Function
  - Limit of a Sequence
  - Convergence
  - Limite
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Function]]"
  - "[[Exponential Function]]"
  - "[[Logarithm]]"
related:
  - "[[Continuity]]"
  - "[[Derivative]]"
  - "[[Integral]]"
  - "[[Infinite Series]]"
  - "[[Taylor Series]]"
  - "[[Poisson Distribution]]"
  - "[[Binomial Distribution]]"
  - "[[Big O Notation]]"
  - "[[Floating-Point Arithmetic]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
---

# Limit

> [!abstract]
> A limit is the value a sequence or a function gets as close to as we like when its index grows without bound or its input approaches a point: the tool that makes "instantaneous", "infinitely many" and "very rare" exact.

## Definition

A sequence $(a_n)$ **converges** to $L$, written $\lim_{n\to\infty} a_n = L$, if for every $\varepsilon > 0$ there is an $N$ such that $|a_n - L| < \varepsilon$ for all $n > N$.[^calc2] A function $f$ has **limit** $L$ at $a$, written $\lim_{x \to a} f(x) = L$, if for every $\varepsilon > 0$ there is a $\delta > 0$ such that $0 < |x - a| < \delta$ implies $|f(x) - L| < \varepsilon$.[^calc1][^1801] The condition $0 < |x - a|$ means that the value $f(a)$, and even whether $f$ is defined at $a$, plays no role.

## Why it matters

- **Every derivative and integral is a limit**: the slope of a growth curve at one instant ([[Derivative]]) and the area under a density ([[Integral]]) are both defined as limits.
- **Rare events.** A human genome has billions of sites, each mutating with a probability of about $1.2 \times 10^{-8}$ per generation;[^kong] a sequencing run drops reads at random start positions along millions of bases.[^lw] Such counts are binomial with huge $n$ and tiny $p$, and the limit $n \to \infty$ with $np = \lambda$ fixed turns them into the [[Poisson Distribution]].
- **Asymptotics.** Running times ([[Big O Notation]]) and large-sample statistics ([[Law of Large Numbers]], [[Central Limit Theorem]]) are statements about limits as $n \to \infty$.
- **Computers do not take limits.** A program evaluates at a finite point. The limit tells you what the answer should be; [[Floating-Point Arithmetic]] tells you when the evaluation goes wrong (Computational representation).

## Core (L1)

**Reading a limit.** $\lim_{x\to a} f(x) = L$ says: take $x$ close enough to $a$ (but not equal) and $f(x)$ is as close to $L$ as you want. One-sided limits $\lim_{x\to a^-}$ and $\lim_{x\to a^+}$ let $x$ approach only from the left or from the right; the two-sided limit exists exactly when both exist and are equal.[^calc1]

**Limit laws.** If $\lim f = A$ and $\lim g = B$ at the same point, then $\lim (f + g) = A + B$, $\lim (cf) = cA$, $\lim (fg) = AB$, and $\lim (f/g) = A/B$ when $B \neq 0$.[^calc1] For a polynomial, or a rational function whose denominator is not zero at $a$, the limit is obtained by substitution.

**Four techniques.**

| Situation | Technique | Example |
|---|---|---|
| $f$ defined and well behaved at $a$ | substitute | $\lim_{x\to 2} (x^2 + 1) = 5$ |
| substitution gives $0/0$ | factor and cancel | $\lim_{x\to 1}\frac{x^2-1}{x-1} = \lim_{x\to 1}(x + 1) = 2$ |
| $x \to \infty$, ratio of polynomials | divide by the highest power | $\lim_{x\to\infty}\frac{3x^2 + 1}{2x^2 - x} = \lim_{x\to\infty} \frac{3 + 1/x^2}{2 - 1/x} = \frac{3}{2}$ |
| $f$ trapped between two functions | squeeze theorem | $-\frac1n \le \frac{(-1)^n}{n} \le \frac1n$, so $\frac{(-1)^n}{n} \to 0$ |

The squeeze theorem: if $g \le f \le h$ near $a$ and $\lim g = \lim h = L$, then $\lim f = L$.[^calc1]

**When there is no limit.** (1) The one-sided limits disagree: $x/|x|$ is $-1$ left of 0 and $+1$ right of 0. (2) Unbounded growth: writing $\lim_{x \to 0} 1/x^2 = \infty$ records *how* the limit fails to exist; $\infty$ is not a real number. (3) Oscillation: $\sin(1/x)$ takes every value in $[-1, 1]$ in every interval around 0.

**The number $e$.** The sequence $a_n = (1 + 1/n)^n$ increases and stays bounded; its limit is the number $e \approx 2.71828$.[^calc1][^calc2] More generally, for every real $x$,

$$\lim_{n\to\infty}\left(1 + \frac{x}{n}\right)^n = e^x .$$

This is a limit of the form "$1^\infty$": the base tends to 1 while the exponent explodes, and the two effects balance. Biological reading: a quantity that grows by a fraction $x/n$ in each of $n$ sub-steps grows by the factor $e^x$ when the steps become continuous ([[Exponential Growth]]).

**Rare events: binomial to Poisson.** With $x = -\lambda$, $(1 - \lambda/n)^n \to e^{-\lambda}$. This is the one non-trivial limit in the proof that the $\mathrm{Bin}(n, \lambda/n)$ probabilities converge to the Poisson ones, $\binom{n}{k}(\lambda/n)^k(1-\lambda/n)^{n-k} \to e^{-\lambda}\lambda^k/k!$; the derivation is in [[Poisson Distribution#Mathematical representation]] and is not repeated here.[^blitz] For $k = 0$ it reads: the probability that none of $n$ independent opportunities, each of probability $\lambda/n$, produces an event tends to $e^{-\lambda}$.

![[poisson-binomial-limit.svg]]

*Exact $\mathrm{Bin}(n, 3/n)$ probabilities approach $\mathrm{Pois}(3)$ as $n$ grows (figure shared with [[Poisson Distribution]]).*

## Deeper (L2)

**Writing ε-δ proofs.** To show $\lim_{x\to 2}(3x + 1) = 7$: given $\varepsilon > 0$, $|(3x + 1) - 7| = 3|x - 2| < \varepsilon$ as soon as $|x - 2| < \varepsilon/3$, so $\delta = \varepsilon/3$ works. To show $1/n \to 0$: given $\varepsilon$, take $N \ge 1/\varepsilon$; then $n > N$ gives $1/n < \varepsilon$. A proof is a recipe that produces $\delta$ (or $N$) from any $\varepsilon$.

**Why $(1 + x/n)^n \to e^x$.** Take logarithms: $n \ln(1 + x/n) = x \cdot \frac{\ln(1 + u)}{u}$ with $u = x/n \to 0$. The fraction is the difference quotient of $\ln$ at 1, so it tends to the [[Derivative]] of $\ln$ at 1, which is $1$. Hence the logarithm tends to $x$, and because $\exp$ is continuous ([[Continuity]]), $(1 + x/n)^n \to e^x$. Two tools did the work: a known derivative, and passing a limit through a continuous function.

**Existence before the value.** An increasing sequence that is bounded above converges (monotone convergence theorem).[^calc2] This property of the real numbers is what guarantees that $(1 + 1/n)^n$ has a limit before anyone calls it $e$.

**How fast.** One more term of the logarithm's expansion ([[Taylor Series]]) gives $n\ln(1 + 1/n) = 1 - \frac{1}{2n} + O(1/n^2)$, so $(1 + 1/n)^n \approx e\,(1 - \frac{1}{2n})$ and $e - a_n \approx \frac{e}{2n}$. The error shrinks like $1/n$, and $n(e - a_n) \to e/2 \approx 1.3591$ (Computational representation). The same expansion gives the error of the Poisson approximation (Exercise 5).

**Comparing growth.** For $a > 1$ and $k > 0$, $\lim_{n\to\infty} \frac{\ln n}{n^k} = 0$ and $\lim_{n\to\infty}\frac{n^k}{a^n} = 0$. These limits order the growth classes $\log n \ll n^k \ll a^n$ of [[Big O Notation]]: an algorithm whose running time is exponential in the input size is eventually slower than any polynomial one.

## Advanced (L3)

**Limits of random quantities.** Statistics takes limits of sequences of random variables. The proportion of successes in $n$ independent Bernoulli($p$) trials converges to $p$ (the [[Law of Large Numbers]]), and the standardized number of successes converges in distribution to a standard normal (the [[Central Limit Theorem]]).[^blitz] The binomial-to-Poisson result is also a convergence in distribution: the probability mass functions converge at every $k$.

**Choosing the limit that matches the data.** A limit is a model of a regime. $\mathrm{Bin}(n, p)$ has two classical limits: $n \to \infty$ with $np$ fixed gives the Poisson (rare events: de novo mutations in a genome, reads starting at one base); $n \to \infty$ with $p$ fixed gives the normal (common events: reads carrying one allele at a deeply covered heterozygous site), see [[Binomial Distribution#Deeper (L2)]].[^blitz] Using the wrong one gives approximations that fail exactly where they are used, often in the tails.

**Limits on a computer.** Evaluated in double precision, $(1 + 1/n)^n$ first approaches $e$, then drifts, then collapses to exactly 1 at $n = 10^{16}$: $1 + 10^{-16}$ rounds to 1 because the spacing of doubles just above 1 is $2.2 \times 10^{-16}$ (machine epsilon, printed below; [[Floating-Point Arithmetic]]). Rewriting the expression as $\exp\big(n \cdot \mathrm{log1p}(1/n)\big)$, where `log1p(u)` computes $\ln(1 + u)$ without forming $1 + u$, keeps full accuracy. The general lesson: find the limit analytically and use the computer to check it over a range of values, never only at an extreme one ([[Rounding Error]], [[Finite Difference]]).

## Mathematical representation

With quantifiers read as in [[Predicate Logic]]:

- Sequence $a: \mathbb{N} \to \mathbb{R}$: $\ \lim_{n\to\infty} a_n = L \iff \forall \varepsilon > 0\ \exists N\ \forall n > N:\ |a_n - L| < \varepsilon$.
- Function at a point: $\ \lim_{x\to a} f(x) = L \iff \forall \varepsilon > 0\ \exists \delta > 0\ \forall x:\ 0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$.
- At infinity: $\ \lim_{x\to\infty} f(x) = L \iff \forall\varepsilon > 0\ \exists M\ \forall x > M:\ |f(x) - L| < \varepsilon$.
- Remainders: $g(n) = O(h(n))$ means $|g(n)| \le C\,|h(n)|$ for some constant $C$ and all large $n$ ([[Big O Notation]]).

Key limits reused across the curriculum (proved in this note or in [[Differentiation Rules]]):

$$\lim_{u\to 0}\frac{\ln(1 + u)}{u} = 1, \qquad \lim_{u\to 0}\frac{e^u - 1}{u} = 1, \qquad \lim_{n\to\infty}\Big(1 + \frac{x}{n}\Big)^n = e^x, \qquad \lim_{n\to\infty} \frac{n^k}{a^n} = 0 \ \ (a > 1).$$

The first two are the derivatives of $\ln$ at 1 and of $\exp$ at 0.

## Computational representation

A limit cannot be computed by substitution, but it can be **checked** by evaluating along points that approach the target from both sides, and by watching the error shrink at the predicted rate.

```python
import math
import sys

def f(x: float) -> float:
    return (math.exp(x) - 1) / x          # undefined at 0; its limit there is 1

for x in (0.1, 0.001, -0.001, -0.1):      # approach 0 from both sides
    print(f"x = {x:>6}  (e^x - 1)/x = {f(x):.6f}")

for n in (1, 10, 100, 1_000, 10_000, 100_000):
    a_n = (1 + 1 / n) ** n
    print(f"n = {n:>6}  a_n = {a_n:.8f}  n(e - a_n) = {n * (math.e - a_n):.4f}")

print(sys.float_info.epsilon, 1 + 1e-16 == 1.0)
for k in (8, 12, 15, 16):
    n = 10 ** k
    naive = (1 + 1 / n) ** n
    stable = math.exp(n * math.log1p(1 / n))   # log1p(u) = ln(1 + u) without forming 1 + u
    print(f"n = 1e{k}  naive = {naive:.10f}  via log1p = {stable:.10f}")

G, N = 5_000_000, 1_000_000               # genome length, number of reads (invented)
lam = N / G
print(f"P(0 starts): binomial {(1 - 1 / G) ** N:.10f}  Poisson {math.exp(-lam):.10f}")
print(f"P(1 start):  binomial {N / G * (1 - 1 / G) ** (N - 1):.10f}  Poisson {lam * math.exp(-lam):.10f}")
```

```text
x =    0.1  (e^x - 1)/x = 1.051709
x =  0.001  (e^x - 1)/x = 1.000500
x = -0.001  (e^x - 1)/x = 0.999500
x =   -0.1  (e^x - 1)/x = 0.951626
n =      1  a_n = 2.00000000  n(e - a_n) = 0.7183
n =     10  a_n = 2.59374246  n(e - a_n) = 1.2454
n =    100  a_n = 2.70481383  n(e - a_n) = 1.3468
n =   1000  a_n = 2.71692393  n(e - a_n) = 1.3579
n =  10000  a_n = 2.71814593  n(e - a_n) = 1.3590
n = 100000  a_n = 2.71826824  n(e - a_n) = 1.3591
2.220446049250313e-16 True
n = 1e8  naive = 2.7182817983  via log1p = 2.7182818149
n = 1e12  naive = 2.7185234960  via log1p = 2.7182818285
n = 1e15  naive = 3.0350352065  via log1p = 2.7182818285
n = 1e16  naive = 1.0000000000  via log1p = 2.7182818285
P(0 starts): binomial 0.8187307367  Poisson 0.8187307531
P(1 start):  binomial 0.1637461801  Poisson 0.1637461506
```

The values of $(e^x - 1)/x$ close in on 1 from both sides; $n(e - a_n)$ settles at $e/2$, confirming the $1/n$ rate; the naive power is already wrong in the 8th decimal at $n = 10^8$, while the `log1p` form is not.

## Worked example

> [!example] Reads starting at one base (invented round numbers)
> A genome of $G = 5{,}000{,}000$ bases is sequenced with $N = 1{,}000{,}000$ reads whose start positions are independent and uniform, the random-placement model of Lander and Waterman.[^lw] How many reads start at a given base?
>
> 1. **Exact model.** Each read starts there with probability $1/G$, so the count is $\mathrm{Bin}(N, 1/G)$ ([[Binomial Distribution]]).
> 2. **Regime.** $N$ is large, $1/G$ is tiny, and $\lambda = N/G = 0.2$ is moderate: the rare-event limit applies.
> 3. **Limit.** Since $1/G = \lambda/N$, $P(0) = (1 - \lambda/N)^N \to e^{-\lambda}$, so $P(0) \approx e^{-0.2} = 0.8187$ and, from the Poisson formula, $P(1) \approx 0.2\,e^{-0.2} = 0.1637$.
> 4. **Check** (last two output lines above): $0.8187307367$ (binomial) against $0.8187307531$ (Poisson); they agree to 7 decimal places.
> 5. **Interpretation.** About 82 % of bases are the start of no read. Combined with the read length, the same reasoning gives the depth of coverage ([[Sequencing Coverage]], [[Lander-Waterman Model]]).

## Common misconceptions

> [!warning] "The limit at $a$ is the value at $a$"
> The definition excludes $x = a$. $\frac{x^2 - 1}{x - 1}$ is undefined at 1 and has limit 2 there. Limit and value coincide only for continuous functions ([[Continuity]]).

> [!warning] "$1^\infty = 1$"
> $(1 + 1/n)^n \to e$, $(1 + 2/n)^n \to e^2$ and $(1 + 1/n)^{n^2} \to \infty$. The forms $1^\infty$, $0/0$, $\infty/\infty$ and $0 \cdot \infty$ are **indeterminate**: the answer depends on how fast each part moves. Rewrite (logarithm, factorization) before concluding.

> [!warning] "Getting closer to $L$ at every step means converging to $L$"
> $1/n$ gets closer to $-1$ at every step, yet its limit is 0. Convergence requires getting *arbitrarily* close, not merely closer.

> [!warning] "Evaluating at a tiny $h$ or a huge $n$ computes the limit"
> In double precision $(1 + 1/n)^n$ returns 3.04 at $n = 10^{15}$ and exactly 1 at $n = 10^{16}$. Numerical evaluation is evidence, not proof, and only in the range where rounding is negligible.

## Exercises

> [!question] Exercise 1 (L1)
> Compute (a) $\lim_{x\to 3} \frac{x^2 - 9}{x - 3}$, (b) $\lim_{x\to\infty} \frac{5x^3 - x}{2x^3 + 4x^2}$, (c) $\lim_{x\to 0} \frac{|x|}{x}$.

> [!success]- Solution
> (a) $\frac{(x - 3)(x + 3)}{x - 3} = x + 3$ for $x \neq 3$, so the limit is 6. (b) Divide by $x^3$: $\frac{5 - 1/x^2}{2 + 4/x} \to \frac52$. (c) The left limit is $-1$ and the right limit is $+1$: the limit does not exist.

> [!question] Exercise 2 (L1)
> Using $(1 + x/n)^n \to e^x$, compute $\lim_{n\to\infty} (1 - 1/n)^n$. Interpret it: $n$ reads each cover a given base independently with probability $1/n$ (mean coverage 1); what fraction of the genome stays uncovered when $n$ is large?

> [!success]- Solution
> With $x = -1$ the limit is $e^{-1} \approx 0.368$. The probability that none of the $n$ reads covers the base is $(1 - 1/n)^n \to e^{-1}$: at mean coverage 1, about 37 % of the bases are not covered. With mean coverage $c$ the same limit gives $e^{-c}$, the uncovered fraction of the Poisson coverage model ([[Poisson Distribution]]).

> [!question] Exercise 3 (L2)
> Prove with the definitions that $\lim_{x\to 1} (2x + 3) = 5$ and that $\frac{n}{n + 1} \to 1$.

> [!success]- Solution
> $|(2x + 3) - 5| = 2|x - 1| < \varepsilon$ whenever $|x - 1| < \varepsilon/2$: take $\delta = \varepsilon/2$. For the sequence, $\left|\frac{n}{n+1} - 1\right| = \frac{1}{n + 1} < \frac1n$, which is below $\varepsilon$ for all $n > N$ with $N \ge 1/\varepsilon$.

> [!question] Exercise 4 (L2)
> A model counts growth once per hour with a rate of 100 % per hour, so the population is multiplied by 2 each hour. If the same nominal rate is applied in $n$ steps of $1/n$ hour, the hourly factor is $(1 + 1/n)^n$. What is the factor in the continuous limit? Which continuous rate $r$ (per hour) gives an exact doubling per hour?

> [!success]- Solution
> The factor tends to $e \approx 2.718$ per hour. A doubling per hour requires $e^{r} = 2$, so $r = \ln 2 \approx 0.693$ per hour. "A rate of 1 per hour" and "doubling every hour" are different statements; growth models must say whether a rate is per step or continuous ([[Exponential Growth]]).

> [!question] Exercise 5 (L3, Python)
> Show that the error of the Poisson approximation for "no event", $e^{-\lambda} - (1 - \lambda/n)^n$, is approximately $\lambda^2 e^{-\lambda}/(2n)$. Use $\ln(1 - u) = -u - u^2/2 + O(u^3)$, then check numerically for $\lambda = 3$.

> [!success]- Solution
> $n\ln(1 - \lambda/n) = -\lambda - \frac{\lambda^2}{2n} + O(1/n^2)$, so $(1 - \lambda/n)^n = e^{-\lambda}\, e^{-\lambda^2/(2n) + O(1/n^2)} \approx e^{-\lambda}\big(1 - \frac{\lambda^2}{2n}\big)$, using $e^{v} \approx 1 + v$ for small $v$ ([[Linear Approximation]]).
>
> ```python
> import math
>
> lam = 3.0
> for n in (10, 100, 1_000, 10_000):
>     exact = (1 - lam / n) ** n
>     gap = math.exp(-lam) - exact
>     print(f"n = {n:>6}  gap = {gap:.3e}  lambda^2 e^-lambda / 2n = {math.exp(-lam) * lam**2 / (2 * n):.3e}")
> ```
>
> ```text
> n =     10  gap = 2.154e-02  lambda^2 e^-lambda / 2n = 2.240e-02
> n =    100  gap = 2.235e-03  lambda^2 e^-lambda / 2n = 2.240e-03
> n =   1000  gap = 2.240e-04  lambda^2 e^-lambda / 2n = 2.240e-04
> n =  10000  gap = 2.240e-05  lambda^2 e^-lambda / 2n = 2.240e-05
> ```
>
> The error is of order $1/n$: ten times more opportunities divide it by ten. With $n$ in the millions or billions (bases of a genome), the Poisson model is exact for practical purposes.

## Mastery checklist

- [ ] 1 Recognized: I can read $\lim_{x\to a} f(x) = L$, say what a one-sided limit is, and state that $(1 + 1/n)^n \to e$.
- [ ] 2 Understood: I can explain why $f(a)$ does not matter, why $1^\infty$ is indeterminate, and why $(1 - \lambda/n)^n \to e^{-\lambda}$ is the heart of the binomial-to-Poisson limit.
- [ ] 3 Practiced: I compute limits by substitution, factoring, highest powers and squeezing, write ε-δ proofs for linear functions, and check limits numerically in Python.
- [ ] 4 Applied: for a real count (reads per base, de novo mutations per genome), I decide whether it is in the Poisson or the normal regime and check the approximation numerically.
- [ ] 5 Explained: I can teach the ε-δ definition, the $1/n$ convergence rate of $(1 + 1/n)^n$, and why floating point breaks the naive evaluation of a limit.

## References

[^calc1]: [[Calculus (OpenStax)]], Volume 1 (limits: intuitive and precise ε-δ definitions, one-sided limits, the limit laws, the squeeze theorem; the number $e$ as the limit of $(1 + 1/m)^m$).
[^calc2]: [[Calculus (OpenStax)]], Volume 2 (sequences: convergence and the monotone convergence theorem).
[^1801]: [[MIT 18.01SC - Single Variable Calculus]], differentiation part (limits).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the Poisson approximation to the binomial and of the limit theorems (law of large numbers, central limit theorem).
[^lw]: [[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]], Lander ES, Waterman MS, *Genomics* 2(3):231-239: clones placed at random along the genome.
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], Kong A et al., *Nature* 488:471-475: $1.20 \times 10^{-8}$ de novo mutations per nucleotide per generation.
