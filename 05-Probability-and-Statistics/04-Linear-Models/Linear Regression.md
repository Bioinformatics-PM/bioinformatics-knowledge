---
aliases:
  - Simple Linear Regression
  - Ordinary Least Squares
  - OLS
  - Regression Line
  - Régression linéaire
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Correlation]]"
  - "[[Scatter Plot]]"
  - "[[Student's t-Distribution]]"
  - "[[Confidence Interval]]"
  - "[[Hypothesis Testing]]"
  - "[[Least Squares]]"
related:
  - "[[Coefficient of Determination]]"
  - "[[Regression Diagnostics]]"
  - "[[Multiple Linear Regression]]"
  - "[[Orthogonal Projection]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Exponential Growth]]"
  - "[[Quantitative Polymerase Chain Reaction]]"
  - "[[Heritability]]"
  - "[[Expression Quantitative Trait Locus]]"
projects: []
sources:
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[Bustin 2009 - The MIQE Guidelines]]"
  - "[[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Shabalin 2012 - Matrix eQTL]]"
---

# Linear Regression

> [!abstract]
> Linear regression fits the straight line $y = \beta_0 + \beta_1 x$ that best predicts a measured response from one predictor, then uses a model of the noise to test the slope and to predict new values with honest error bars: the arithmetic of every calibration curve and the first estimator of heritability.

## Definition

**Simple linear regression** models a quantitative response $Y$ as a linear function of one predictor $x$ plus a random error,

$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \qquad i = 1, \dots, n,$$

where the intercept $\beta_0$ and the slope $\beta_1$ are unknown constants and the errors $\varepsilon_i$ have mean 0. The coefficients are estimated by **least squares**: the fitted line $\hat y = \hat\beta_0 + \hat\beta_1 x$ minimizes the residual sum of squares $\mathrm{RSS} = \sum_i (y_i - \hat y_i)^2$. The slope is the expected change in $Y$ for a one-unit increase in $x$.[^isl3][^os12][^1805]

## Why it matters

- **Calibration curves.** A qPCR standard curve regresses the threshold cycle $C_t$ on $\log_{10}$ of known template amounts; the slope gives the amplification efficiency and the line converts the $C_t$ of an unknown into copies ([[Exponential Growth#Deeper (L2)]]). The MIQE reporting guidelines ask for exactly the regression outputs: slope and intercept, efficiency calculated from the slope, $r^2$ and linear dynamic range, with confidence intervals for the efficiency as a desirable item.[^miqe] Relative quantification by $2^{-\Delta\Delta C_t}$ assumes efficiencies close to 100 %,[^livak] an assumption that a slope test checks (Worked example).
- **Heritability.** Regressing offspring phenotype on the mean of the two parents (the midparent) gives a slope that estimates the narrow-sense [[Heritability]] $h^2$, the share of phenotypic variance due to additive genetic effects.[^hartl]
- **Association.** An [[Expression Quantitative Trait Locus|eQTL]] test regresses a gene's expression on the genotype coded additively (0, 1 or 2 copies of an allele): the slope is the effect per allele, and the test is repeated for every gene-variant pair of the study.[^shabalin]
- **The template of linear models.** [[Multiple Linear Regression]], [[Analysis of Variance]] and the [[Generalized Linear Model|generalized linear models]] of differential expression keep the same ingredients: a linear predictor, estimated coefficients with standard errors, and tests on them.

## Core (L2)

### Fitting the line

Least squares has a closed form (derived in Mathematical representation):[^isl3][^os12]

$$\hat\beta_1 = \frac{S_{xy}}{S_{xx}} = r\,\frac{s_y}{s_x}, \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x,$$

with $S_{xx} = \sum_i (x_i - \bar x)^2$, $S_{xy} = \sum_i (x_i - \bar x)(y_i - \bar y)$, $s_x, s_y$ the standard deviations and $r$ the [[Correlation]] of $x$ and $y$. Three consequences: the line passes through $(\bar x, \bar y)$; the residuals $e_i = y_i - \hat y_i$ sum to zero; they are uncorrelated with $x$. The geometry (the fitted values are the [[Orthogonal Projection]] of $\mathbf{y}$ onto the span of the constant vector and $\mathbf{x}$) and the matrix solution belong to [[Least Squares]].

### The noise model

A line can be drawn through any cloud. To attach uncertainty to it, assume that the mean of $Y$ is **linear** in $x$ and that the errors are **independent**, with **equal variance** $\sigma^2$, and **normal** for exact small-sample tests; these assumptions are checked on the residuals ([[Regression Diagnostics]]).[^isl3][^os12] The predictor is treated as fixed and known without error, as in a dilution series of known amounts. $\sigma$ is estimated by the **residual standard error**

$$s = \sqrt{\frac{\mathrm{RSS}}{n - 2}},$$

with $n - 2$ degrees of freedom because two coefficients were estimated.[^isl3]

### Testing the slope

The slope's standard error is $\mathrm{SE}(\hat\beta_1) = s / \sqrt{S_{xx}}$, and under $H_0: \beta_1 = b$

$$t = \frac{\hat\beta_1 - b}{\mathrm{SE}(\hat\beta_1)} \sim t_{n-2},$$

a [[Student's t-Distribution|$t$ distribution]] with $n - 2$ degrees of freedom; the 95 % [[Confidence Interval]] is $\hat\beta_1 \pm t_{0.975,\,n-2}\,\mathrm{SE}(\hat\beta_1)$.[^isl3][^os12] The default null value is $b = 0$ (no linear association), and that test is the same as the test of $r = 0$ in [[Correlation#Advanced (L3)]]. Other null values are often the interesting ones: $b = -3.32$ for a perfectly efficient qPCR assay, $b = 1$ for two methods that should agree.

$\mathrm{SE}(\hat\beta_1)$ shrinks with less noise ($s$), more points, and a wider spread of $x$ ($S_{xx}$): a dilution series spanning five orders of magnitude pins the slope far better than one spanning two. That is design, decided before any measurement.

### Two intervals for prediction

At a new value $x_0$, the fitted value $\hat y_0 = \hat\beta_0 + \hat\beta_1 x_0$ answers two different questions; a prediction interval is always wider than a confidence interval because it adds the scatter of an individual observation.[^isl3] The formulas are derived in Mathematical representation:

| Question | 95 % interval |
|---|---|
| Where is the **mean** response at $x_0$? (confidence interval) | $\hat y_0 \pm t_{0.975,\,n-2}\; s\sqrt{\dfrac{1}{n} + \dfrac{(x_0 - \bar x)^2}{S_{xx}}}$ |
| Where will **one new** observation at $x_0$ fall? (prediction interval) | $\hat y_0 \pm t_{0.975,\,n-2}\; s\sqrt{1 + \dfrac{1}{n} + \dfrac{(x_0 - \bar x)^2}{S_{xx}}}$ |

More data shrink the first toward zero width, never the second. Both are narrowest at $\bar x$ and widen toward the edges of the data. Beyond the data, linearity is unchecked and neither interval covers that risk: extrapolation is an assumption, not a result.

![[regression-confidence-prediction-bands.svg]]

### Bio: midparent regression and heritability

For a quantitative trait, write each phenotype as an additive genetic value (the breeding value) plus everything else; the **narrow-sense heritability** is $h^2 = V_A / V_P$, additive genetic variance over phenotypic variance. Under random mating, with no environment shared by parents and offspring and ignoring interactions between loci, the offspring-midparent covariance is $V_A/2$ while the midparent variance is $V_P/2$, so the regression slope is[^hartl]

$$b_{O \cdot MP} = \frac{\operatorname{Cov}(O, MP)}{\operatorname{Var}(MP)} = \frac{V_A/2}{V_P/2} = h^2 .$$

On a single parent the slope is $h^2/2$ (Exercise 5). The figure shows 40 invented families simulated with $h^2 = 0.6$: the fitted slope is 0.60, but its 95 % interval, 0.26 to 0.94, shows how little 40 families pin down. The slope below 1 is **regression to the mean**: children of parents 10 units above average are expected to be $10\,h^2$ units above average, because the part of the parents' advantage that came from environment is not transmitted.

## Advanced (L3)

**Least squares is maximum likelihood.** With normal errors the log-likelihood is $\ell(\beta_0, \beta_1, \sigma^2) = -\frac{n}{2}\ln(2\pi\sigma^2) - \mathrm{RSS}(\beta_0, \beta_1)/(2\sigma^2)$, maximized over the coefficients by minimizing RSS ([[Maximum Likelihood Estimation]]). The likelihood estimate of $\sigma^2$ is $\mathrm{RSS}/n$, biased low; $s^2 = \mathrm{RSS}/(n-2)$ corrects it. Replacing the normal by a Poisson or negative binomial likelihood, with the mean linked to $\beta_0 + \beta_1 x$, is the step to [[Generalized Linear Model|GLMs]] for read counts.

**Errors in $x$ flatten the slope.** If the predictor is observed as $W = x + u$, with an error $u$ of variance $\sigma_u^2$ independent of everything else, then $\operatorname{Cov}(Y, W) = \beta_1\sigma_x^2$ and $\operatorname{Var}(W) = \sigma_x^2 + \sigma_u^2$, so the slope of $Y$ on $W$ tends to $\lambda\beta_1$ with $\lambda = \sigma_x^2/(\sigma_x^2 + \sigma_u^2) < 1$. The midparent regression is exactly this case: the expected offspring value has slope 1 on the parents' mean breeding value, but we observe phenotypes, which add environmental noise, and $\lambda = (V_A/2)/(V_P/2) = h^2$. A standard curve avoids attenuation by design: the precisely known quantity goes on $x$, the noisy reading on $y$.

**Calibration runs the line backwards.** To quantify an unknown, regress $C_t$ on $\log_{10}$ copies, then solve $\hat x_0 = (\bar y_0 - \hat\beta_0)/\hat\beta_1$, where $\bar y_0$ is the mean of $m$ new wells; regressing $\log_{10}$ copies on $C_t$ gives a different line (Exercise 4). The delta method gives a first-order standard error

$$\mathrm{SE}(\hat x_0) \approx \frac{s}{|\hat\beta_1|}\sqrt{\frac{1}{m} + \frac{1}{n} + \frac{(\hat x_0 - \bar x)^2}{S_{xx}}} .$$

**Regression to the mean follows every selection.** In standard units the fitted line is $\hat z_y = r\, z_x$. Whenever $|r| < 1$, units selected for extreme $x$ are on average less extreme in $y$, with no mechanism at work. Genes selected as the most changed in one experiment, or variants selected as the strongest associations in one cohort, look weaker when measured again: discoveries need independent replication to estimate their size.

**One predictor is the special case.** In matrix form $\mathbf{y} = X\boldsymbol\beta + \boldsymbol\varepsilon$ with $X = [\mathbf{1}\ \mathbf{x}]$, the estimate is $\hat{\boldsymbol\beta} = (X^\top X)^{-1}X^\top\mathbf{y}$ ([[Inverse Matrix#Deeper (L2)]]) and $\operatorname{Var}(\hat{\boldsymbol\beta}) = \sigma^2 (X^\top X)^{-1}$: the formulas of this note are entries of these two expressions, and they carry over unchanged to several predictors ([[Multiple Linear Regression]], [[Design Matrix]]). Numerical code prefers a [[QR Decomposition]] of $X$ to forming $X^\top X$, which squares the condition number ([[Inverse Matrix#Advanced (L3)]]).

## Mathematical representation

- **Model.** $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ with $E[\varepsilon_i] = 0$, $\operatorname{Var}(\varepsilon_i) = \sigma^2$, independent errors (normal for exact tests). $\bar x, \bar y$: means; $S_{xx}$, $S_{xy}$ as above; $\hat y_i$: fitted values; $e_i = y_i - \hat y_i$: residuals.
- **Normal equations.** $\partial\,\mathrm{RSS}/\partial\beta_0 = -2\sum_i e_i = 0$ and $\partial\,\mathrm{RSS}/\partial\beta_1 = -2\sum_i x_i e_i = 0$. Substituting $e_i = y_i - \beta_0 - \beta_1 x_i$ and solving gives $\hat\beta_1 = S_{xy}/S_{xx}$ and $\hat\beta_0 = \bar y - \hat\beta_1\bar x$.
- **Linear in the data.** $\hat\beta_1 = \sum_i w_i y_i$ with $w_i = (x_i - \bar x)/S_{xx}$, where $\sum w_i = 0$, $\sum w_i x_i = 1$ and $\sum w_i^2 = 1/S_{xx}$. Hence $E[\hat\beta_1] = \beta_1$ and $\operatorname{Var}(\hat\beta_1) = \sigma^2/S_{xx}$; with normal errors $\hat\beta_1$ is exactly normal.
- **Mean response.** $\operatorname{Cov}(\bar Y, \hat\beta_1) = \frac{\sigma^2}{n}\sum_i w_i = 0$, so $\operatorname{Var}(\hat\beta_0 + \hat\beta_1 x_0) = \operatorname{Var}\big(\bar Y + \hat\beta_1 (x_0 - \bar x)\big) = \sigma^2\big(\frac{1}{n} + \frac{(x_0 - \bar x)^2}{S_{xx}}\big)$; $x_0 = 0$ gives $\operatorname{Var}(\hat\beta_0)$. A new observation $Y_0$ is independent of the fit, so $\operatorname{Var}(Y_0 - \hat y_0)$ adds $\sigma^2$: the prediction interval.
- **From $z$ to $t$.** With normal errors, $\mathrm{RSS}/\sigma^2 \sim \chi^2_{n-2}$ independently of $(\hat\beta_0, \hat\beta_1)$, so replacing $\sigma$ by $s$ turns each standardized estimate into a $t_{n-2}$ statistic ([[Chi-Square Distribution]]).[^18650]
- **Efficiency.** From $C_t = a + \beta_1 \log_{10} N_0$ with $\beta_1 = -1/\log_{10}(1 + E)$: $E = 10^{-1/\beta_1} - 1$, a monotone function of $\beta_1$, so a confidence interval for $\beta_1$ maps endpoint by endpoint to one for $E$ ([[Exponential Growth#Mathematical representation]]).

## Computational representation

By hand with the standard library; SciPy supplies the $t$ quantiles and a cross-check (`scipy.stats.linregress` also returns the slope's standard error).

```python
import math
from scipy import stats   # t quantiles and the cross-check only


def fit_line(x, y):
    """Least-squares fit of y = b0 + b1*x, with what inference needs."""
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    b1 = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx
    b0 = my - b1 * mx
    rss = sum((b - b0 - b1 * a) ** 2 for a, b in zip(x, y))
    s = math.sqrt(rss / (n - 2))                      # residual standard error, n - 2 df
    return dict(n=n, mx=mx, sxx=sxx, b0=b0, b1=b1, s=s, se_b1=s / math.sqrt(sxx))


def band(fit, x0, level=0.95, new_obs=False):
    """CI for the mean response at x0, or (new_obs=True) prediction interval for one new y."""
    t = float(stats.t.ppf((1 + level) / 2, fit["n"] - 2))
    se = fit["s"] * math.sqrt(new_obs + 1 / fit["n"] + (x0 - fit["mx"]) ** 2 / fit["sxx"])
    y0 = fit["b0"] + fit["b1"] * x0
    return round(y0 - t * se, 2), round(y0 + t * se, 2)


# Invented tenfold dilution series of [[Exponential Growth]]: log10 copies -> Ct
x = [6, 5, 4, 3, 2, 1]
ct = [15.99, 19.30, 22.86, 26.25, 29.77, 33.12]
f = fit_line(x, ct)
t_crit = float(stats.t.ppf(0.975, f["n"] - 2))
print(f"slope {f['b1']:.4f} (SE {f['se_b1']:.4f}), intercept {f['b0']:.3f}, s {f['s']:.4f}")
lo, hi = f["b1"] - t_crit * f["se_b1"], f["b1"] + t_crit * f["se_b1"]
print(f"95% CI slope [{lo:.3f}, {hi:.3f}] -> efficiency [{10 ** (-1 / lo) - 1:.3f}, {10 ** (-1 / hi) - 1:.3f}]")
t_100 = (f["b1"] + 1 / math.log10(2)) / f["se_b1"]          # H0: slope = -3.3219, E = 100%
print(f"H0 E = 100%: t = {t_100:.2f}, p = {2 * stats.t.sf(abs(t_100), f['n'] - 2):.4f}")
print("at 10^2.5 copies: mean Ct", band(f, 2.5), " one new well", band(f, 2.5, new_obs=True))
check = stats.linregress(x, ct)
print(f"scipy linregress: slope {check.slope:.4f}, stderr {check.stderr:.4f}")
```

```text
slope -3.4414 (SE 0.0149), intercept 36.593, s 0.0621
95% CI slope [-3.483, -3.400] -> efficiency [0.937, 0.968]
H0 E = 100%: t = -8.04, p = 0.0013
at 10^2.5 copies: mean Ct (27.91, 28.07)  one new well (27.8, 28.18)
scipy linregress: slope -3.4414, stderr 0.0149
```

## Worked example

> [!example] Testing a qPCR standard curve (invented data)
> The tenfold dilution series of [[Exponential Growth]] (invented): $\log_{10}$ copies 6, 5, 4, 3, 2, 1 gave $C_t$ = 15.99, 19.30, 22.86, 26.25, 29.77, 33.12.
> 1. **Fit.** $\bar x = 3.5$, $S_{xx} = 17.5$; $\hat\beta_1 = -3.441$ cycles per tenfold dilution, $\hat\beta_0 = 36.59$. Residuals 0.045, −0.086, 0.032, −0.019, 0.060, −0.032 (sum 0), so $s = 0.062$ cycles with 4 degrees of freedom.
> 2. **Which null?** $\mathrm{SE}(\hat\beta_1) = 0.062/\sqrt{17.5} = 0.0149$. Against $\beta_1 = 0$, $t = -232$: a pointless question for a standard curve. Against perfect doubling, $\beta_1 = -1/\log_{10} 2 = -3.322$: $t = (-3.441 + 3.322)/0.0149 = -8.0$ with 4 df, $p = 0.0013$.
> 3. **Efficiency with its interval.** 95 % CI for the slope: $-3.441 \pm 2.776 \times 0.0149 = [-3.483, -3.400]$, which maps to $E \in [0.937, 0.968]$ around the point estimate 0.952. The assay is clearly below 100 %, so converting $\Delta C_t$ with base 2 would bias ratios ([[Exponential Growth#Deeper (L2)]]).
> 4. **An unknown sample.** One well reads $C_t = 27.30$: $\hat x_0 = (27.30 - 36.593)/(-3.441) = 2.700$, i.e. 502 copies. The formula of the Advanced section ($m = 1$) gives $2.700 \pm 0.055$ in $\log_{10}$ units: 442 to 569 copies. Three wells averaging 27.30 ($m = 3$) narrow it to 461 to 546.
> 5. **What the fit cannot say.** $r^2 = 0.9999$ ([[Coefficient of Determination]]) says nothing about linearity outside $10^1$ to $10^6$ copies; a sample beyond that range is quantified by extrapolation (Exercise 3).

## Common misconceptions

> [!warning] "A significant slope means a strong relationship"
> The $t$ test asks whether $\beta_1 = 0$ is plausible, not whether $x$ predicts $y$ well. With many observations a tiny slope is significant while individual predictions stay poor: report the slope with its units, the prediction interval and $R^2$ ([[Coefficient of Determination]], [[Effect Size]]).

> [!warning] "The confidence band shows where the data should fall"
> It covers the mean response. Single observations scatter around the mean by about $\sigma$; most of them fall outside the confidence band, and about 5 % fall outside even the prediction band (figure above).[^isl3]

> [!warning] "Regressing x on y gives the same line"
> The slope of $x$ on $y$ is $r\,s_x/s_y$, not the inverse of $r\,s_y/s_x$; the two lines coincide only when $|r| = 1$ (Exercise 4). The response, the variable measured with error, goes on $y$.

> [!warning] "Regression to the mean is a biological force"
> Children of tall parents are on average less tall than their parents without any mechanism pulling toward the mean, and the population variance need not shrink between generations. It follows from $|r| < 1$; in the heritability model the shrinkage factor is $h^2$ because the parents' environmental deviations are not transmitted.[^hartl]

## Exercises

> [!question] Exercise 1 (L2)
> Cell viability (invented, arbitrary units) at inhibitor doses 0, 1, 2, 3, 4 µM was 10.1, 8.8, 8.3, 6.9, 5.9. Fit the line by hand, test the slope and give its 95 % CI ($t_{0.975,3} = 3.182$). What does the line predict at 10 µM?

> [!success]- Solution
> $\bar x = 2$, $\bar y = 8.0$, $S_{xx} = 10$, $S_{xy} = (-2)(2.1) + (-1)(0.8) + 0 + (1)(-1.1) + (2)(-2.1) = -10.3$, so $\hat\beta_1 = -1.03$ per µM and $\hat\beta_0 = 8.0 + 1.03 \times 2 = 10.06$. Residuals 0.04, −0.23, 0.30, −0.07, −0.04; $\mathrm{RSS} = 0.151$, $s = \sqrt{0.151/3} = 0.224$, $\mathrm{SE} = 0.224/\sqrt{10} = 0.0709$, $t = -14.5$ ($p = 0.0007$, 3 df). CI: $-1.03 \pm 3.182 \times 0.0709 = [-1.26, -0.80]$. At 10 µM the line predicts $10.06 - 10.3 = -0.24$, a negative viability: the straight line is supported only on 0 to 4 µM.

> [!question] Exercise 2 (L2)
> In 200 invented families, the midparent height has variance 18 cm² and its covariance with the child's height is 10.8 cm². Estimate $h^2$, $V_P$ and $V_A$, and predict the mean height deviation of children whose midparent is 8 cm above the population mean. Why not 8 cm?

> [!success]- Solution
> $h^2 = 10.8/18 = 0.6$. $\operatorname{Var}(MP) = V_P/2$, so $V_P = 36$ cm² and $V_A = 0.6 \times 36 = 21.6$ cm². Prediction: $0.6 \times 8 = 4.8$ cm above the mean. The parents' 8 cm include environmental (and non-additive) deviations that are not transmitted, so only the additive share, $h^2$, is expected to reappear in the children.[^hartl]

> [!question] Exercise 3 (L2, Python)
> With `fit_line` and `band` from the code above, compute the 95 % CI of the mean $C_t$ and the 95 % prediction interval for one new well at $\log_{10}$ copies 3.5, 1.0 and 7.5. Explain the widths. Can the value at 7.5 be trusted?

> [!success]- Solution
> ```python
> for x0 in (3.5, 1.0, 7.5):
>     print(x0, "mean", band(f, x0), "new well", band(f, x0, new_obs=True))
> ```
> ```text
> 3.5 mean (24.48, 24.62) new well (24.36, 24.73)
> 1.0 mean (33.03, 33.28) new well (32.94, 33.36)
> 7.5 mean (10.6, 10.96) new well (10.53, 11.03)
> ```
> Widths grow with $(x_0 - \bar x)^2$ from the center $\bar x = 3.5$ (0.14 cycles) to the last dilution (0.25) and beyond (0.36); the prediction interval adds the scatter of one well. At $10^{7.5}$ copies the arithmetic still works, but no dilution there was measured: the interval assumes that linearity continues, which is why the linear dynamic range is reported with a standard curve.[^miqe]

> [!question] Exercise 4 (L3)
> Show that the least-squares slope of $x$ on $y$ is $r\,s_x/s_y$, that the product of the two slopes is $r^2$, and conclude when the two lines coincide. Check on the dilution series.

> [!success]- Solution
> Swapping roles, $b_{x\cdot y} = S_{xy}/S_{yy} = r\,s_x/s_y$, so $b_{y\cdot x}\,b_{x\cdot y} = S_{xy}^2/(S_{xx}S_{yy}) = r^2$. Drawn in the $(x, y)$ plane, the $x$-on-$y$ line has slope $1/b_{x\cdot y}$, equal to $b_{y\cdot x}$ only if $r^2 = 1$; both lines pass through $(\bar x, \bar y)$. On the dilution series, `fit_line(ct, x)["b1"]` is −0.29056, against $1/\hat\beta_1 = -0.29058$: the product of slopes is $r^2 = 0.99993$, so the lines nearly coincide here, but not for a noisier assay.

> [!question] Exercise 5 (L3, Python)
> Simulate 5,000 invented families with $V_A = 0.6$ and $V_E = 0.4$: each offspring's breeding value is the parents' mean plus an independent term of variance $V_A/2$ (which keeps $V_A$ constant across generations). Regress offspring on midparent and on the father alone, and explain both slopes.

> [!success]- Solution
> ```python
> import random
>
> rng = random.Random(2024)
> VA, VE = 0.6, 0.4                       # invented variance components: h2 = 0.6
> mid, off, dad = [], [], []
> for _ in range(5000):
>     af, am = rng.gauss(0, VA ** 0.5), rng.gauss(0, VA ** 0.5)            # parents' breeding values
>     pf, pm = af + rng.gauss(0, VE ** 0.5), am + rng.gauss(0, VE ** 0.5)  # parents' phenotypes
>     ao = (af + am) / 2 + rng.gauss(0, (VA / 2) ** 0.5)                  # offspring breeding value
>     off.append(ao + rng.gauss(0, VE ** 0.5))
>     mid.append((pf + pm) / 2)
>     dad.append(pf)
> for name, xs in (("midparent", mid), ("father", dad)):
>     g = fit_line(xs, off)
>     print(f"{name:<9} slope {g['b1']:.3f}  95% CI +/- {1.96 * g['se_b1']:.3f}")
> ```
> ```text
> midparent slope 0.607  95% CI +/- 0.035
> father    slope 0.291  95% CI +/- 0.026
> ```
> Midparent: $\operatorname{Cov}(O, MP) = \operatorname{Var}\big((A_f + A_m)/2\big) = V_A/2$ and $\operatorname{Var}(MP) = V_P/2$, slope $h^2 = 0.6$. Father: $\operatorname{Cov}(O, P_f) = V_A/2$ but $\operatorname{Var}(P_f) = V_P$, slope $h^2/2 = 0.3$. Doubling the father slope estimates $h^2$ as $0.58 \pm 0.05$, less precisely than the midparent design ($\pm 0.035$).

## Mastery checklist

- [ ] 1 Recognized: I can write $y = \beta_0 + \beta_1 x + \varepsilon$ and say what the slope, the intercept and the residuals mean.
- [ ] 2 Understood: I can explain least squares, the four assumptions, the $t$ test of the slope and the difference between confidence and prediction intervals.
- [ ] 3 Practiced: I can fit a line by hand and in Python with standard errors and both intervals, and test a slope against a non-zero value (qPCR efficiency).
- [ ] 4 Applied: I analyzed a real qPCR standard curve and reported the slope, the efficiency with its interval and quantified unknowns with intervals, as MIQE asks.
- [ ] 5 Explained: I can teach regression to the mean, attenuation by errors in $x$, why calibration regresses the reading on the known amount, and why significance is not predictive strength.

## References

[^isl3]: [[An Introduction to Statistical Learning (James)]], Python edition, ch. 3 "Linear Regression" (chapter number as checked in [[Linear Models]]).
[^os12]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 12 "Linear Regression and Correlation".
[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], linear regression part.
[^18650]: [[MIT 18.650 - Statistics for Applications]], linear regression part (distribution of least-squares estimates under normal errors).
[^miqe]: [[Bustin 2009 - The MIQE Guidelines]], *Clinical Chemistry* 55(4):611-622, checklist items on calibration curves.
[^livak]: [[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]], *Methods* 25(4):402-408, assumptions of the $2^{-\Delta\Delta C_T}$ method.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed., quantitative traits part (heritability, resemblance between relatives); not verified at chapter level.
[^shabalin]: [[Shabalin 2012 - Matrix eQTL]], *Bioinformatics* 28(10):1353-1358.
