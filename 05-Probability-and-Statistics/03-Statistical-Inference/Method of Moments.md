---
aliases:
  - Moment Matching
  - Moment Estimator
  - MoM
  - Méthode des moments
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Estimator]]"
  - "[[Statistical Model]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Law of Large Numbers]]"
  - "[[Negative Binomial Distribution]]"
related:
  - "[[Maximum Likelihood Estimation]]"
  - "[[Overdispersion]]"
  - "[[Dispersion Estimation]]"
  - "[[Size Factor Estimation]]"
  - "[[Gamma Distribution]]"
  - "[[Jukes-Cantor Model]]"
  - "[[Evolutionary Distance]]"
  - "[[Watterson Estimator]]"
  - "[[Empirical Bayes]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Anders 2010 - Differential Expression Analysis for Sequence Count Data]]"
  - "[[Love 2014 - Moderated Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Watterson 1975 - On the Number of Segregating Sites in Genetical Models Without Recombination]]"
---

# Method of Moments

> [!abstract]
> The method of moments estimates parameters by choosing the values for which the model's theoretical moments (mean, variance, ...) equal the ones computed from the data: quick, often in closed form, and a good first answer, though usually less precise than maximum likelihood.

## Definition

For a [[Statistical Model]] with $k$ parameters $\theta$, write the first $k$ moments as functions of the parameters, $m_j(\theta) = E_\theta[X^j]$ (or equivalently the mean, the variance, ...), and compute the corresponding sample moments $\hat m_j = \frac{1}{n}\sum_i X_i^j$. The **method of moments estimator** is the value $\hat\theta$ that solves the $k$ equations $m_j(\hat\theta) = \hat m_j$, $j = 1, \dots, k$.[^18650]

## Why it matters

- **Quick estimates for thousands of genes.** Closed-form moment estimates cost one pass over the data, and they provide starting values for iterative fits by [[Maximum Likelihood Estimation]].
- **Overdispersion of read counts.** Matching the mean and the variance of the negative binomial gives a one-line dispersion estimate; DESeq's original variance estimate subtracted the Poisson part from the sample variance of normalized counts and smoothed the result against the mean across genes.[^anders]
- **Classic corrections in evolutionary genomics are moment estimators.** The Jukes-Cantor distance matches the expected proportion of differing sites;[^yang] Watterson's $\theta$ matches the expected number of segregating sites.[^watterson]

## Core (L2)

### The recipe

1. Write as many moments of the model as there are parameters, as functions of the parameters.
2. Replace them by the sample moments.
3. Solve for the parameters.

| Model | Moments | Moment estimator |
|---|---|---|
| Poisson, rate $\lambda$ | $E[X] = \lambda$ | $\hat\lambda = \bar x$ |
| Normal, $\mu, \sigma^2$ | $E[X] = \mu$, $\mathrm{Var}(X) = \sigma^2$ | $\hat\mu = \bar x$, $\hat\sigma^2 = \frac1n\sum(x_i - \bar x)^2$ |
| Gamma, shape $k$, scale $c$ | $E[X] = kc$, $\mathrm{Var}(X) = kc^2$ | $\hat c = v/\bar x$, $\hat k = \bar x^2/v$ |
| Negative binomial, $\mu, \alpha$ | $E[X] = \mu$, $\mathrm{Var}(X) = \mu + \alpha\mu^2$ | $\hat\mu = \bar x$, $\hat\alpha = (v - \bar x)/\bar x^2$ |

Here $v$ is the sample variance; the gamma moments are those of the [[Gamma Distribution]].[^blitz] Using $S^2$ (divisor $n - 1$) instead of the plug-in second central moment changes little and removes its small-sample bias ([[Estimator]]).

### Bio: a quick estimate of negative binomial dispersion

For a gene measured in $n$ biological replicates, the [[Negative Binomial Distribution]] says $\mathrm{Var}(K) = \mu + \alpha\mu^2$. Matching both moments gives

$$\hat\mu = \bar k, \qquad \hat\alpha = \frac{s^2 - \bar k}{\bar k^2}.$$

Dividing the variance by $\mu^2$ shows the meaning: $\mathrm{CV}^2 = 1/\mu + \alpha$, a Poisson term that vanishes with depth plus the biological term, so $\sqrt{\alpha}$ is the coefficient of variation of true expression between replicates.

**Unequal depths.** Raw counts of samples sequenced at different depths differ for technical reasons. Divide each count by its size factor $s_j$ ([[Size Factor Estimation]]); the normalized counts $q_j = k_j/s_j$ have variance $\mu/s_j + \alpha\mu^2$, so the Poisson part to subtract is $\bar q \cdot \overline{(1/s)}$, not $\bar q$ (Mathematical representation).[^anders] Ignoring depth inflates the dispersion: in the Worked example it more than triples it.

### How good is the quick estimate?

![[dispersion-moment-estimates-replicates.svg]]

Simulating 20,000 genes with mean 100 and true $\alpha = 0.1$ (code below):

| Replicates $n$ | Mean $\hat\alpha$ | SD | $P(\hat\alpha \le 0)$ | Middle 90 % |
|---|---|---|---|---|
| 3 | 0.097 | 0.103 | 0.088 | [−0.005, 0.301] |
| 6 | 0.098 | 0.068 | 0.006 | [0.015, 0.227] |
| 12 | 0.099 | 0.049 | 0.000 | [0.035, 0.188] |
| 48 | 0.100 | 0.024 | 0.000 | [0.065, 0.141] |

The estimate is nearly unbiased here, but with 3 replicates its SD equals the true value, and almost 9 % of genes get a dispersion of 0 or less, although every gene is overdispersed. A sample variance from three numbers is that noisy ([[Variance#Advanced (L3)]]). A negative estimate means "the spread was smaller than Poisson noise in this sample": set it to 0 and do not interpret it. With few replicates per gene, precision has to come from sharing information across genes ([[Dispersion Estimation]], [[Empirical Bayes]]).

## Advanced (L3)

### Moment estimators in sequence analysis

- **Jukes-Cantor distance.** Under the JC69 model, two sequences separated by $d$ expected substitutions per site differ at a site with probability $p(d) = \frac34\left(1 - e^{-4d/3}\right)$.[^yang] Matching it to the observed proportion $\hat p$ of differing sites gives $\hat d = -\frac34 \ln\left(1 - \frac43 \hat p\right)$ ([[Jukes-Cantor Model]], [[Evolutionary Distance]]). For two sequences it coincides with the maximum likelihood estimate ([[Maximum Likelihood Estimation#Core (L2)]]). It is undefined when $\hat p \ge 3/4$: the sequences are saturated and the moment equation has no solution.
- **Watterson's $\theta$.** Matching the observed number of segregating sites $S$ to its expectation $a_n\theta$ gives $\hat\theta_W = S/a_n$ ([[Watterson Estimator]]).[^watterson] Its variance is discussed in [[Estimator#Advanced (L3)]].

Both match the expected value of one observable summary to its observed value: one equation, one parameter.

### Consistency and standard errors

By the [[Law of Large Numbers]], sample moments converge to the true moments; if the map from moments back to parameters is continuous, the moment estimator is consistent. The [[Central Limit Theorem]] makes sample moments approximately normal, and the delta method carries this to $\hat\theta$. For the JC69 distance, $p'(d) = e^{-4d/3} = 1 - \frac43 p$, so

$$\mathrm{Var}(\hat d) \approx \frac{\mathrm{Var}(\hat p)}{p'(d)^2} = \frac{p(1-p)}{n\left(1 - \frac43 p\right)^2},$$

which explodes as $p$ approaches the saturation value 3/4.[^yang]

### Moments versus likelihood

A moment estimator uses only a few summaries of the data; the likelihood uses the whole distribution, so in large samples the maximum likelihood estimator is at least as precise ([[Fisher Information]]). In small samples the comparison involves bias too. For the dispersion with 6 replicates (mean 100, $\alpha = 0.1$, code below):

| Estimator | Mean | SD | RMSE |
|---|---|---|---|
| Moments, negative values set to 0 | 0.0974 | 0.0682 | 0.0682 |
| Maximum likelihood | 0.0814 | 0.0572 | 0.0601 |

The likelihood estimate is less variable and has the lower RMSE, but it is biased downward by about 19 %: like the plug-in variance, it fits the mean to the same few data. Shrinking gene-wise dispersions toward a trend fitted across all genes, as DESeq2 does, attacks both problems.[^love]

## Mathematical representation

- **Equations.** $m_j(\theta) = E_\theta[X^j]$, $\hat m_j = \frac1n\sum_{i=1}^n X_i^j$; $\hat\theta$ solves $m(\hat\theta) = \hat m$, where $m: \Theta \to \mathbb{R}^k$. If $m$ is invertible, $\hat\theta = m^{-1}(\hat m)$.
- **Negative binomial with size factors.** Let $K_j \sim \mathrm{NB}(s_j\mu, \alpha)$ independent and $Q_j = K_j/s_j$. Then $E[Q_j] = \mu$ and $\mathrm{Var}(Q_j) = (s_j\mu + \alpha s_j^2\mu^2)/s_j^2 = \mu/s_j + \alpha\mu^2$. For independent variables with a common mean, the sample variance is unbiased for the average variance (because $\sum_j (Q_j - \bar Q)^2 = \sum_j (Q_j - \mu)^2 - n(\bar Q - \mu)^2$ has expectation $\frac{n-1}{n}\sum_j \mathrm{Var}(Q_j)$), so
$$E[S_Q^2] = \mu\,\overline{(1/s)} + \alpha\mu^2, \qquad \hat\alpha = \frac{S_Q^2 - \bar Q\,\overline{(1/s)}}{\bar Q^2}, \qquad \overline{(1/s)} = \frac1n\sum_j \frac{1}{s_j}.$$
With equal depths ($s_j = 1$) this reduces to $(S^2 - \bar K)/\bar K^2$.
- **Gamma.** $\bar x = kc$ and $v = kc^2$ give $\hat c = v/\bar x$, $\hat k = \bar x^2/v$.

## Computational representation

Each moment estimator is a formula, so the code is short. Standard library first:

```python
import math
import statistics as st


def nb_moments(counts, size_factors=None):
    """Method-of-moments mean and dispersion of negative binomial counts.

    Counts are divided by their size factors; the Poisson part of the variance of the
    normalized counts, mean * average(1/s), is subtracted before solving for alpha."""
    s = size_factors or [1.0] * len(counts)
    q = [k / sj for k, sj in zip(counts, s)]
    m, v = st.fmean(q), st.variance(q)
    shot = m * st.fmean(1 / sj for sj in s)
    return m, (v - shot) / m ** 2


def jc69_distance(p):
    """Jukes-Cantor distance, matching the observed proportion of differing sites to 3/4 (1 - exp(-4d/3))."""
    return -0.75 * math.log(1 - 4 * p / 3) if p < 0.75 else math.inf


counts = [12, 35, 8, 30, 52, 9]                # one low-count gene in 6 replicates (invented)
sizes = [0.6, 1.4, 0.8, 1.0, 1.5, 0.7]        # their size factors (invented)
print("depth ignored     : mean %.2f, alpha_hat %.3f" % nb_moments(counts))
print("size-factor aware : mean %.2f, alpha_hat %.3f" % nb_moments(counts, sizes))
print("JC69, p = 0.12    : d_hat = %.4f" % jc69_distance(0.12))
```

```text
depth ignored     : mean 24.33, alpha_hat 0.488
size-factor aware : mean 22.09, alpha_hat 0.140
JC69, p = 0.12    : d_hat = 0.1308
```

The sampling study of the tables above is array computation, where NumPy draws gamma-Poisson counts for 20,000 genes at once, and SciPy maximizes the negative binomial log-likelihood (the formula of [[Negative Binomial Distribution#Advanced (L3)]]) for the comparison with maximum likelihood:

```python
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gammaln

rng = np.random.default_rng(1)
MU, ALPHA, R = 100.0, 0.1, 20_000
for n in (3, 6, 12, 48):
    k = rng.poisson(rng.gamma(shape=1 / ALPHA, scale=ALPHA * MU, size=(R, n)))   # gamma-Poisson counts
    m, v = k.mean(axis=1), k.var(axis=1, ddof=1)
    a = (v - m) / m ** 2
    lo, hi = np.quantile(a, [0.05, 0.95])
    print(f"n = {n:2d}: mean {a.mean():.3f}, SD {a.std():.3f}, P(alpha_hat <= 0) = {(a <= 0).mean():.3f}, "
          f"90 % of estimates in [{lo:.3f}, {hi:.3f}]")


def nb_loglik(alpha, k, mu):
    r = 1 / alpha
    return np.sum(gammaln(k + r) - gammaln(r) - gammaln(k + 1)
                  + r * np.log(r / (r + mu)) + k * np.log(mu / (r + mu)))


def alpha_mle(k):
    """Maximum likelihood dispersion; the mean's MLE is the sample mean whatever alpha is."""
    res = minimize_scalar(lambda la: -nb_loglik(np.exp(la), k, k.mean()),
                          bounds=(np.log(1e-6), np.log(10.0)), method="bounded")
    return np.exp(res.x)


rng = np.random.default_rng(2)
n, R = 6, 4_000
mom, mle = [], []
for _ in range(R):
    k = rng.poisson(rng.gamma(1 / ALPHA, ALPHA * MU, size=n))
    m, v = k.mean(), k.var(ddof=1)
    mom.append(max((v - m) / m ** 2, 0.0))
    mle.append(alpha_mle(k))
for name, est in (("moments (clipped at 0)", np.array(mom)), ("maximum likelihood", np.array(mle))):
    print(f"{name:22s}: mean {est.mean():.4f}, SD {est.std():.4f}, RMSE {np.sqrt(np.mean((est - ALPHA) ** 2)):.4f}")
```

```text
n =  3: mean 0.097, SD 0.103, P(alpha_hat <= 0) = 0.088, 90 % of estimates in [-0.005, 0.301]
n =  6: mean 0.098, SD 0.068, P(alpha_hat <= 0) = 0.006, 90 % of estimates in [0.015, 0.227]
n = 12: mean 0.099, SD 0.049, P(alpha_hat <= 0) = 0.000, 90 % of estimates in [0.035, 0.188]
n = 48: mean 0.100, SD 0.024, P(alpha_hat <= 0) = 0.000, 90 % of estimates in [0.065, 0.141]
moments (clipped at 0): mean 0.0974, SD 0.0682, RMSE 0.0682
maximum likelihood    : mean 0.0814, SD 0.0572, RMSE 0.0601
```

The dispersion is optimized on the log scale, $\log\alpha$, which keeps it positive and makes the search better conditioned.

## Worked example

> [!example] Dispersion of a low-count gene sequenced at unequal depths
> Counts in 6 replicates: 12, 35, 8, 30, 52, 9; size factors 0.6, 1.4, 0.8, 1.0, 1.5, 0.7 (invented).
> 1. **Raw counts.** Mean 24.33, variance 313.1, so $\hat\alpha = (313.1 - 24.33)/24.33^2 = 0.488$. Most of this spread comes from depth: the deepest library (1.5) has the largest count.
> 2. **Normalize.** $q_j = k_j/s_j$: 20.0, 25.0, 10.0, 30.0, 34.67, 12.86; mean 22.09, variance 93.0.
> 3. **Poisson part.** With unequal depths it is $\bar q \cdot \overline{(1/s)} = 22.09 \times 1.121 = 24.76$, larger than $\bar q$ because shallow libraries add more sampling noise.
> 4. **Dispersion.** $\hat\alpha = (93.0 - 24.76)/22.09^2 = 0.140$ (0.145 if the Poisson part were taken as $\bar q$).
> 5. **Reading.** The biological coefficient of variation is about $\sqrt{0.140} = 0.37$. With 6 replicates the estimate is still rough (SD about 0.07 at $\alpha = 0.1$ for a mean of 100, more at low counts), so this number should be combined with those of other genes of similar expression rather than used alone.

## Common misconceptions

> [!warning] "Moment and likelihood estimates always agree"
> They agree for a Poisson rate, a binomial proportion, a normal mean and the JC69 distance between two sequences, but not in general: for the negative binomial dispersion with 6 replicates, the two estimators average 0.097 and 0.081 on the same simulated genes.

> [!warning] "A negative dispersion estimate means a bug"
> It means the replicates happened to vary less than Poisson noise. With 3 replicates this happens for about 9 % of genes whose true dispersion is 0.1. Report 0, and borrow strength from other genes.

> [!warning] "Library size does not matter for the variance"
> Counts from deeper libraries are larger, which looks like biological variability. In the Worked example, ignoring depth more than triples the dispersion (0.488 against 0.140).


## Exercises

> [!question] Exercise 1 (L2)
> Single-cell protein abundances (arbitrary units, invented) have sample mean 4.0 and sample variance 10.0. Fit a gamma distribution by moments. Is an exponential distribution (a gamma with shape 1) compatible with these moments?

> [!success]- Solution
> $\hat c = v/\bar x = 10/4 = 2.5$ and $\hat k = \bar x^2/v = 16/10 = 1.6$. An exponential with mean 4 would have variance $4^2 = 16$; the observed variance 10 is smaller, giving a shape above 1: less skewed than exponential.

> [!question] Exercise 2 (L2)
> Estimate the dispersion by moments for two genes with 4 replicates each (equal depths): A = 3, 0, 7, 2 and B = 5, 4, 6, 5. Comment.

> [!success]- Solution
> A: $\bar k = 3$, $s^2 = 26/3 = 8.67$, $\hat\alpha = (8.67 - 3)/9 = 0.630$. B: $\bar k = 5$, $s^2 = 0.667$, $\hat\alpha = (0.667 - 5)/25 = -0.173$, reported as 0. At such low counts the Poisson term $1/\mu$ (0.33 and 0.2) is comparable to any plausible dispersion, and 4 replicates cannot separate them: both estimates are unreliable.

> [!question] Exercise 3 (L2)
> Two aligned sequences of 500 sites differ at 60. Compute the p-distance and the JC69 distance. What happens if they differ at 400 sites?

> [!success]- Solution
> $\hat p = 0.12$ and $\hat d = -0.75\ln(1 - 0.16) = 0.1308$: about 9 % more substitutions than visible differences, because some sites changed more than once. With 400 differences, $\hat p = 0.8 \ge 0.75$: the equation has no solution and `jc69_distance` returns infinity. The sequences are saturated and carry no distance information under this model.

> [!question] Exercise 4 (L3)
> Using the delta method, compute the standard error of $\hat d$ in Exercise 3 and an approximate 95 % interval.

> [!success]- Solution
> $\mathrm{Var}(\hat d) \approx \frac{0.12 \times 0.88}{500 \times (1 - 0.16)^2} = \frac{0.1056}{352.8} = 0.000299$, SE 0.0173. Interval: $0.1308 \pm 1.96 \times 0.0173 = [0.097, 0.165]$.

> [!question] Exercise 5 (L3)
> Ten sequences of a 1 kb locus show $S = 16$ segregating sites. Estimate $\theta$ per locus and per site, and its standard error by plugging $\hat\theta$ into the variance $\theta/a_n + b_n\theta^2/a_n^2$ ($a_{10} = 2.829$, $b_{10} = 1.540$).

> [!success]- Solution
> $\hat\theta_W = 16/2.829 = 5.66$ per locus, 0.0057 per site. $\mathrm{Var} \approx 5.66/2.829 + 1.540 \times 5.66^2/2.829^2 = 2.00 + 6.16 = 8.15$, SE 2.86: a relative error of about 50 %, dominated by the genealogy term ([[Estimator#Advanced (L3)]]).

## Mastery checklist

- [ ] 1 Recognized: I can state the method of moments and give the moment estimators of the Poisson, normal, gamma and negative binomial models.
- [ ] 2 Understood: I can derive the dispersion estimate with size factors, and explain why it can be negative and why it is noisy with few replicates.
- [ ] 3 Practiced: I can implement moment estimators, simulate their sampling distribution and compare them with maximum likelihood.
- [ ] 4 Applied: I computed JC69 distance matrices from real alignments in [[08-phylogenetic-engine]], or moment dispersions for a real RNA-seq count table and plotted them against the mean.
- [ ] 5 Explained: I can teach when moment estimators are good enough, how the delta method gives their standard errors, and why likelihood and shrinkage replace them in final analyses.

## References

[^18650]: [[MIT 18.650 - Statistics for Applications]], estimation part (method of moments).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., named continuous distributions (mean and variance of the gamma distribution).
[^anders]: [[Anders 2010 - Differential Expression Analysis for Sequence Count Data]], *Genome Biology* 11:R106: size factors, and variance estimation from normalized counts (sample variance minus the Poisson part, smoothed against the mean by local regression across genes).
[^love]: [[Love 2014 - Moderated Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2]], *Genome Biology* 15:550: shrinkage estimation of dispersions and fold changes.
[^yang]: [[Molecular Evolution (Yang)]], treatment of the JC69 model (expected proportion of differences, the JC69 distance and its variance).
[^watterson]: [[Watterson 1975 - On the Number of Segregating Sites in Genetical Models Without Recombination]], *Theoretical Population Biology* 7(2):256-276.
