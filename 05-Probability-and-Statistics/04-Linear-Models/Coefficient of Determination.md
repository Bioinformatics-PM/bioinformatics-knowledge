---
aliases:
  - R-squared
  - R²
  - R2
  - Variance Explained
  - Coefficient de détermination
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Linear Regression]]"
  - "[[Correlation]]"
  - "[[Variance]]"
related:
  - "[[Multiple Linear Regression]]"
  - "[[Analysis of Variance]]"
  - "[[Regression Diagnostics]]"
  - "[[Expression Quantitative Trait Locus]]"
  - "[[Heritability]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Effect Size]]"
  - "[[Overfitting]]"
  - "[[Cross-Validation]]"
  - "[[F-Distribution]]"
projects: []
sources:
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Anscombe 1973 - Graphs in Statistical Analysis]]"
  - "[[Shabalin 2012 - Matrix eQTL]]"
  - "[[GTEx Portal]]"
  - "[[Bustin 2009 - The MIQE Guidelines]]"
  - "[[Principles of Population Genetics (Hartl)]]"
---

# Coefficient of Determination

> [!abstract]
> $R^2$ is the fraction of the variation of a response that a fitted regression accounts for: 0 when the model does no better than the mean, 1 when it passes through every point. It is a useful effect size, such as the share of a gene's expression variance that goes with one variant, but it says nothing about whether the model is right.

## Definition

For a least-squares fit that includes an intercept, the **coefficient of determination** is

$$R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}, \qquad \mathrm{TSS} = \sum_i (y_i - \bar y)^2, \quad \mathrm{RSS} = \sum_i (y_i - \hat y_i)^2,$$

the proportion of the variability of $y$ that is explained by the regression.[^isl3] It lies between 0 and 1, and in simple linear regression it equals $r^2$, the square of the [[Correlation]] between $x$ and $y$.[^isl3][^os12]

## Why it matters

- **eQTL effect size.** For one gene and one variant, $R^2$ of expression on genotype dosage is the share of the gene's expression variance, across the individuals of one tissue, that goes with that variant. eQTL mapping fits this regression, with covariates, for every gene-variant pair,[^shabalin] and atlases such as GTEx map the associations tissue by tissue.[^gtex]
- **Standard curves.** MIQE lists the $r^2$ of a qPCR standard curve among the essential items to report;[^miqe] a value near 1 is easy to reach and weak evidence of quality on its own (Exercise 4).
- **Size versus significance.** $R^2$ measures how much, a p-value how surely: 2 % of variance explained is highly significant with 900 samples, 39 % is not significant with 9 (Exercise 2, [[Effect Size]]).
- **Model comparison.** $R^2$ never decreases when a predictor is added, so models of different sizes need a penalty or new data to be compared ([[Multiple Linear Regression]], [[Overfitting]]).[^isl3]

## Core (L2)

### Partitioning the variation

Each deviation from the mean splits into a part along the fitted line and a residual: $y_i - \bar y = (\hat y_i - \bar y) + (y_i - \hat y_i)$. For a least-squares fit with an intercept the cross terms cancel (proof in Mathematical representation), so the squares add up:

$$\underbrace{\sum_i (y_i - \bar y)^2}_{\mathrm{TSS}} = \underbrace{\sum_i (\hat y_i - \bar y)^2}_{\mathrm{ESS}} + \underbrace{\sum_i (y_i - \hat y_i)^2}_{\mathrm{RSS}}, \qquad R^2 = \frac{\mathrm{ESS}}{\mathrm{TSS}}.$$

TSS measures how far the data are from the simplest model, a constant mean; ESS (the explained, or regression, sum of squares) how far the fitted values move away from that constant; RSS what is left.

![[r-squared-variance-decomposition.svg]]

### Reading $R^2$

- $R^2 = 0.39$ means that the residual sum of squares is 61 % of the total **in this sample**: knowing the predictor reduces the squared prediction error around the mean by 39 %.
- It has no units and does not change when $x$ or $y$ is shifted or rescaled.
- $R^2 = \operatorname{Cor}(y, \hat y)^2$, the squared correlation between the data and the fitted values, a form that also holds with several predictors.[^isl3]
- "Explained" is arithmetic, not causation: whatever is correlated with $x$, a confounder included, is "explained" with it ([[Confounding]]).

### Bio: variance explained by an eQTL

An [[Expression Quantitative Trait Locus|eQTL]] analysis asks, gene by gene, whether expression changes with the number of copies (0, 1, 2) of an allele. In the figure's nine invented individuals, $R^2 = 0.39$ of the gene's expression variance goes with genotype (computed by hand in the Worked example).

## Advanced (L3)

**$R^2$ depends on the population, not only on the effect.** For an additive variant with allele frequency $p$ in [[Hardy-Weinberg Equilibrium]], the dosage $G \sim \mathrm{Bin}(2, p)$ has variance $2p(1-p)$, so with per-allele effect $\beta$ and residual variance $\sigma^2$ the population value is

$$R^2 = \frac{2p(1-p)\,\beta^2}{2p(1-p)\,\beta^2 + \sigma^2}.$$

The same effect $\beta = 0.5\,\sigma$ explains 11 % of the variance at $p = 0.5$ and 2.3 % at $p = 0.05$ (Exercise 3): a rare variant explains little variance even with a large effect, and a variant's $R^2$ changes between populations with different allele frequencies. [[Heritability]] is the same kind of ratio, additive genetic variance over phenotypic variance, summed over all loci;[^hartl] the $R^2$ of one variant is its share in one sample. Any predictor behaves alike: widening the range of $x$ raises $R^2$ without changing the slope or the noise ([[Correlation#Deeper (L2)]]).

**From $R^2$ to a test, at scale.** With $p$ predictors, $F = \dfrac{R^2/p}{(1 - R^2)/(n - p - 1)}$; for one predictor $F = t^2 = (n-2)R^2/(1-R^2)$, so the slope test is a monotone function of $R^2$, hence of $|r|$ ([[F-Distribution]]). After standardizing each gene's expression and each variant's genotype, all the correlations of a study come out of one matrix product, the kind of large matrix operation behind the speed of Matrix eQTL.[^shabalin] Within one sample size, ranking associations by $R^2$ is the same as ranking them by p-value.

**Adding predictors.** RSS cannot increase when a column is added, so $R^2$ creeps up even with predictors that are pure noise.[^isl3] Two corrections:[^isl]

- **Adjusted $R^2$** $= 1 - \dfrac{\mathrm{RSS}/(n - p - 1)}{\mathrm{TSS}/(n - 1)}$ compares variance estimates instead of sums of squares; it rises only when a predictor reduces RSS by more than the degree of freedom it costs, and it can be negative.
- **Out-of-sample $R^2$** $= 1 - \sum_{\text{test}} (y_i - \hat y_i)^2 / \sum_{\text{test}} (y_i - \bar y_{\text{train}})^2$ judges predictions on new data; it is negative when the model predicts worse than the training mean (Exercise 5, [[Cross-Validation]]).

**When $R^2$ is meaningless.** Without an intercept the cross term no longer vanishes, TSS $\ne$ ESS + RSS, and $1 - \mathrm{RSS}/\mathrm{TSS}$ cannot be compared with a model that has one. And a high $R^2$ does not show that the model is right: Anscombe's four datasets share the same fitted line and $r = 0.816$, hence $R^2 = 0.67$, but only one of them is a straight line with noise ([[Correlation#Core (L1)]], [[Regression Diagnostics]]).[^anscombe]

## Mathematical representation

- $y_i$ data, $\hat y_i$ fitted values, $e_i = y_i - \hat y_i$ residuals, $\bar y$ their mean; $n$ observations, $p$ predictors plus an intercept.
- **Decomposition.** $\mathrm{TSS} = \mathrm{ESS} + \mathrm{RSS} + 2\sum_i (\hat y_i - \bar y)e_i$. The normal equations give $\sum_i e_i = 0$ and $\sum_i x_{ij} e_i = 0$ for every predictor $j$; $\hat y_i$ is a linear combination of 1 and the $x_{ij}$, so $\sum_i \hat y_i e_i = 0$ and the cross term vanishes. In vectors, $\mathbf{e}$ is orthogonal to the column space of $X$, which contains $\mathbf{1}$ and $\hat{\mathbf{y}}$: $\mathbf{y} - \bar y\mathbf{1} = (\hat{\mathbf{y}} - \bar y\mathbf{1}) + \mathbf{e}$ is a right-angled triangle and Pythagoras applies ([[Orthogonal Projection]]).
- **Simple regression.** $\hat y_i - \bar y = \hat\beta_1(x_i - \bar x)$, so $\mathrm{ESS} = \hat\beta_1^2 S_{xx} = S_{xy}^2/S_{xx}$ and $R^2 = S_{xy}^2/(S_{xx}S_{yy}) = r^2$.
- **Correlation form.** $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{e}$ with zero sample covariance between $\hat y$ and $e$ gives $\operatorname{Cov}(y, \hat y) = \operatorname{Var}(\hat y)$, so $\operatorname{Cor}(y, \hat y)^2 = \operatorname{Var}(\hat y)/\operatorname{Var}(y) = \mathrm{ESS}/\mathrm{TSS}$.
- **Population version.** $R^2_{\text{pop}} = \operatorname{Var}(E[Y \mid X])/\operatorname{Var}(Y)$. For $Y = \beta_0 + \beta G + \varepsilon$ with $\varepsilon$ independent of $G$: $\operatorname{Var}(E[Y \mid G]) = \beta^2\operatorname{Var}(G)$ and $\operatorname{Var}(Y) = \beta^2\operatorname{Var}(G) + \sigma^2$.

## Computational representation

Standard library for one predictor; with several, NumPy's `numpy.linalg.lstsq` computes the fit (Exercise 5, [[Least Squares]]).

```python
import statistics


def simple_fit(x, y):
    """Least-squares intercept and slope."""
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    b1 = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx
    return my - b1 * mx, b1


def sums_of_squares(y, fitted):
    """TSS, ESS, RSS around the mean of y."""
    my = sum(y) / len(y)
    tss = sum((v - my) ** 2 for v in y)
    ess = sum((f - my) ** 2 for f in fitted)
    rss = sum((v - f) ** 2 for v, f in zip(y, fitted))
    return tss, ess, rss


# Invented cis-eQTL: alternative-allele dosage and log2 expression of one gene, 9 individuals
dosage = [0, 0, 0, 1, 1, 1, 2, 2, 2]
expr = [5.1, 5.9, 4.7, 5.6, 6.3, 5.2, 6.0, 6.8, 5.7]
b0, b1 = simple_fit(dosage, expr)
fitted = [b0 + b1 * g for g in dosage]
tss, ess, rss = sums_of_squares(expr, fitted)
r2 = 1 - rss / tss
n = len(expr)
print(f"slope {b1:.4f}  TSS {tss:.4f} = ESS {ess:.4f} + RSS {rss:.4f}")
print(f"R2 {r2:.4f}  r^2 {statistics.correlation(dosage, expr) ** 2:.4f}  "
      f"cor(y, yhat)^2 {statistics.correlation(expr, fitted) ** 2:.4f}")
print(f"F = t^2 = {(n - 2) * r2 / (1 - r2):.3f}")
```

```text
slope 0.4667  TSS 3.3200 = ESS 1.3067 + RSS 2.0133
R2 0.3936  r^2 0.3936  cor(y, yhat)^2 0.3936
F = t^2 = 4.543
```

The three routes to $R^2$ agree, as the Mathematical representation proves.

## Worked example

> [!example] Variance explained by an eQTL, by hand (invented data)
> Dosage 0: 5.1, 5.9, 4.7; dosage 1: 5.6, 6.3, 5.2; dosage 2: 6.0, 6.8, 5.7 (log2 expression).
> 1. **Means.** $\bar y = 51.3/9 = 5.70$ and $\bar x = 1$.
> 2. **Slope.** $S_{xx} = 3 \times 1 + 0 + 3 \times 1 = 6$. Only dosages 0 and 2 contribute to $S_{xy}$: $(-1)(15.7 - 3 \times 5.7) + (+1)(18.5 - 3 \times 5.7) = 18.5 - 15.7 = 2.8$, so $\hat\beta_1 = 0.467$ log2 units per allele, a $2^{0.467} = 1.38$-fold change.
> 3. **Sums of squares.** Deviations from 5.70: −0.6, 0.2, −1.0, −0.1, 0.6, −0.5, 0.3, 1.1, 0.0, so $\mathrm{TSS} = 3.32$. $\mathrm{ESS} = \hat\beta_1^2 S_{xx} = 0.467^2 \times 6 = 1.307$ and $\mathrm{RSS} = 3.32 - 1.307 = 2.013$.
> 4. **$R^2$.** $1.307/3.32 = 0.394$: in these nine individuals, genotype at this variant goes with 39 % of the gene's expression variance.
> 5. **Is it real?** $F = 7 \times 0.394/0.606 = 4.54$ with 1 and 7 degrees of freedom, $p = 0.07$: a large share of variance, not distinguishable from chance with nine individuals. For comparison, the GTEx atlas analyzed 15,201 samples from 49 tissues, about 300 per tissue on average.[^gtex]

## Common misconceptions

> [!warning] "A high R² means the model is right"
> $R^2$ summarizes distances to the fitted line, not the shape of the data. Anscombe's four datasets all have $R^2 = 0.67$, including a curve and a line created by a single point.[^anscombe] Look at the residuals ([[Regression Diagnostics]]).

> [!warning] "A low R² means the predictor does not matter"
> $R^2$ mixes effect size with how much the predictor varies in the sample. A rare variant with a large per-allele effect explains little variance (Advanced section), and a small $R^2$ with a precise, reproducible slope can still be biologically important. For the same reason, $R^2$ values from samples with different spreads of $x$, or from models of different sizes, are not directly comparable.

> [!warning] "R² is the fraction of the response caused by x"
> It is the fraction of the sample variance associated with $x$ under the fitted model. Confounders, reverse causation and selection of the sample all change it ([[Confounding]]).

## Exercises

> [!question] Exercise 1 (L2)
> A regression of a quantitative trait on age gives $\mathrm{TSS} = 250$ and $\mathrm{RSS} = 200$. Compute $R^2$ and $|r|$. How is the sign of $r$ determined? Interpret.

> [!success]- Solution
> $R^2 = 1 - 200/250 = 0.2$ and $|r| = \sqrt{0.2} = 0.447$; the sign of $r$ is the sign of the slope. Age goes with 20 % of the trait variance in this sample; 80 % remains around the line.

> [!question] Exercise 2 (L2, Python)
> Using $F = (n-2)R^2/(1-R^2)$ with 1 and $n - 2$ degrees of freedom, compute the p-values for $R^2 = 0.39$ with $n = 9$ and for $R^2 = 0.02$ with $n = 900$.

> [!success]- Solution
> ```python
> from scipy import stats
>
> for r2_obs, n_obs in ((0.39, 9), (0.02, 900)):
>     F = (n_obs - 2) * r2_obs / (1 - r2_obs)
>     print(f"n = {n_obs:<4} R2 = {r2_obs}  F = {F:.2f}  p = {stats.f.sf(F, 1, n_obs - 2):.2g}")
> ```
> ```text
> n = 9    R2 = 0.39  F = 4.48  p = 0.072
> n = 900  R2 = 0.02  F = 18.33  p = 2.1e-05
> ```
> Twenty times less variance explained, yet far more significant: the p-value grows with $n$ for a fixed $R^2$, while $R^2$ does not.

> [!question] Exercise 3 (L3)
> Derive the population $R^2$ of an additive variant (allele frequency $p$, per-allele effect $\beta$, residual variance $\sigma^2$, Hardy-Weinberg proportions). Evaluate it for $\beta = 0.5$, $\sigma = 1$, at $p = 0.5$ and $p = 0.05$.

> [!success]- Solution
> Under Hardy-Weinberg the dosage is the sum of two independent Bernoulli($p$) alleles, so $\operatorname{Var}(G) = 2p(1-p)$. Then $\operatorname{Var}(E[Y \mid G]) = \beta^2 \cdot 2p(1-p)$ and $R^2 = \frac{2p(1-p)\beta^2}{2p(1-p)\beta^2 + \sigma^2}$. At $p = 0.5$: $0.125/1.125 = 0.111$. At $p = 0.05$: $0.02375/1.02375 = 0.023$. Same biology, five times less variance explained.

> [!question] Exercise 4 (L3)
> An invented standard curve has slope $\beta = -1/\log_{10} 1.9 = -3.587$ (efficiency 0.9), with $\log_{10}$ copies 1 to 6 in triplicate (18 wells) and residual SD $\sigma$. Using $R^2 \approx \beta^2 \operatorname{Var}(x)/(\beta^2 \operatorname{Var}(x) + \sigma^2)$, where $\operatorname{Var}(x) = 17.5/6$ is the spread of the design, compare $\sigma = 0.3$ and $\sigma = 0.05$ cycles: $R^2$, $\mathrm{SE}(\hat\beta)$ and the 95 % interval of the efficiency. What should a reader of a qPCR paper look at?

> [!success]- Solution
> $\beta^2\operatorname{Var}(x) = 12.87 \times 2.917 = 37.5$, so $R^2 = 37.5/37.6 = 0.9976$ for $\sigma = 0.3$ and $0.99993$ for $\sigma = 0.05$: both look perfect. But $\mathrm{SE}(\hat\beta) = \sigma/\sqrt{S_{xx}}$ with $S_{xx} = 3 \times 17.5 = 52.5$ is 0.041 against 0.007. By the delta method $dE/d\beta = 10^{-1/\beta}\ln 10/\beta^2 = 0.34$, so with $t_{0.975,16} = 2.12$ the efficiency is known to about $\pm 0.030$ against $\pm 0.005$: six times less precisely for the same "excellent" $r^2$. Read $r^2$ with the efficiency and its interval (a desirable MIQE item[^miqe]) and with the residuals.

> [!question] Exercise 5 (L3, Python)
> Draw an invented training sample and a test sample of 9 individuals each (true slope 0.45 per allele). Fit dosage alone, then dosage plus 5 noise predictors, and compare $R^2$, adjusted $R^2$ and out-of-sample $R^2$.

> [!success]- Solution
> ```python
> import numpy as np
>
> rng = np.random.default_rng(3)
>
>
> def make_sample(m):
>     """Invented eQTL sample: intercept, dosage, 5 noise columns; true slope 0.45."""
>     d = rng.integers(0, 3, m).astype(float)
>     X = np.column_stack([np.ones(m), d, rng.normal(size=(m, 5))])
>     return X, 5.2 + 0.45 * d + rng.normal(0, 0.55, m)
>
>
> X_train, y_train = make_sample(9)
> X_test, y_test = make_sample(9)
> tss = ((y_train - y_train.mean()) ** 2).sum()
> for cols, name in ((slice(0, 2), "dosage only"), (slice(0, 7), "dosage + 5 noise")):
>     Xc = X_train[:, cols]
>     beta, *_ = np.linalg.lstsq(Xc, y_train, rcond=None)
>     rss = ((y_train - Xc @ beta) ** 2).sum()
>     p = Xc.shape[1] - 1
>     adj = 1 - (rss / (9 - p - 1)) / (tss / 8)
>     r2_out = 1 - ((y_test - X_test[:, cols] @ beta) ** 2).sum() / ((y_test - y_train.mean()) ** 2).sum()
>     print(f"{name:<17} R2 {1 - rss / tss:.3f}  adjusted {adj:.3f}  out-of-sample {r2_out:.3f}")
> ```
> ```text
> dosage only       R2 0.227  adjusted 0.117  out-of-sample 0.041
> dosage + 5 noise  R2 0.877  adjusted 0.508  out-of-sample -1.589
> ```
> Five noise columns lift $R^2$ from 0.23 to 0.88, and with only 2 residual degrees of freedom left even the adjusted value is fooled (0.12 to 0.51). New individuals expose the noise model: it predicts them far worse than the training mean, and a negative out-of-sample $R^2$ is the signature of [[Overfitting]].

## Mastery checklist

- [ ] 1 Recognized: I can define $R^2$ as $1 - \mathrm{RSS}/\mathrm{TSS}$ and state its range.
- [ ] 2 Understood: I can explain TSS = ESS + RSS, why $R^2 = r^2$ in simple regression, and why $R^2$ is not a test of the model.
- [ ] 3 Practiced: I can compute $R^2$, adjusted $R^2$ and out-of-sample $R^2$ by hand and in Python, and convert $R^2$ to $F$.
- [ ] 4 Applied: I computed the variance explained by a few known eQTLs in public expression and genotype data and compared it across allele frequencies or tissues.
- [ ] 5 Explained: I can teach why $R^2$ depends on allele frequency and range, why it rises with useless predictors, and how it relates to heritability and to p-values at genome scale.

## References

[^isl3]: [[An Introduction to Statistical Learning (James)]], Python edition, ch. 3 "Linear Regression" (chapter number as checked in [[Linear Models]]).
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition, treatment of linear model selection (adjusted $R^2$) and validation; chapter not verified.
[^os12]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 12 "Linear Regression and Correlation".
[^anscombe]: [[Anscombe 1973 - Graphs in Statistical Analysis]], *The American Statistician* 27(1):17-21.
[^shabalin]: [[Shabalin 2012 - Matrix eQTL]], *Bioinformatics* 28(10):1353-1358.
[^gtex]: [[GTEx Portal]], GTEx Consortium atlas (*Science*, 2020): 15,201 RNA-seq samples from 49 tissues of 838 donors.
[^miqe]: [[Bustin 2009 - The MIQE Guidelines]], *Clinical Chemistry* 55(4):611-622, checklist items on calibration curves.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed., quantitative traits part (heritability); not verified at chapter level.
