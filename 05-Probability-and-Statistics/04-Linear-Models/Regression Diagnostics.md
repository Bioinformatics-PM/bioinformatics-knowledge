---
aliases:
  - Residual Analysis
  - Residual Plot
  - Leverage
  - Cook's Distance
  - Influential Observation
  - Diagnostics de régression
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Linear Regression]]"
  - "[[Coefficient of Determination]]"
  - "[[Scatter Plot]]"
  - "[[Outlier]]"
related:
  - "[[Q-Q Plot]]"
  - "[[Orthogonal Projection]]"
  - "[[Data Transformation]]"
  - "[[Variance-Stabilizing Transformation]]"
  - "[[Poisson Distribution]]"
  - "[[Overdispersion]]"
  - "[[Generalized Linear Model]]"
  - "[[Negative Binomial Regression]]"
  - "[[Multiple Linear Regression]]"
  - "[[Pseudoreplication]]"
  - "[[Cross-Validation]]"
projects: []
sources:
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Anscombe 1973 - Graphs in Statistical Analysis]]"
  - "[[Cook 1977 - Detection of Influential Observation in Linear Regression]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Anders 2010 - Differential Expression Analysis for Sequence Count Data]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Experimental Design for Laboratory Biologists (Lazic)]]"
---

# Regression Diagnostics

> [!abstract]
> A least-squares line always exists; regression diagnostics check whether it deserves trust, by examining what the model leaves behind (residuals), which points pull the fit (leverage, influence) and whether the noise has the constant variance that the standard errors assume.

## Definition

**Regression diagnostics** are checks, mostly graphical, of a fitted regression: whether the assumptions behind its standard errors and tests hold (a mean linear in the predictors, independent errors, constant variance, normal errors), and whether a few observations unduly determine the fit. The main tools are residual plots, leverage, studentized residuals and influence measures such as Cook's distance.[^isl3][^cook]

## Why it matters

- **Summaries cannot judge a fit.** Anscombe's four datasets have the same fitted line, correlation and $R^2$, yet one is a curve and two are driven by a single point.[^anscombe] Only diagnostics, or a plot, tell them apart ([[Coefficient of Determination]]).
- **Counts violate constant variance.** A Poisson count has variance equal to its mean,[^blitz] and RNA-seq counts of a gene vary between biological replicates more than Poisson, with a variance that grows with the mean.[^anders] A linear model on raw counts is therefore misspecified, which motivates transformations and the negative binomial [[Generalized Linear Model|GLMs]] of differential expression ([[Negative Binomial Regression]]).[^msmb8]
- **One sample can make an association.** A single contaminated library or swapped sample, if extreme in $x$, can create or erase a gene's apparent association; influence measures flag it before a figure is built on it.[^cook]
- **Hidden dependence.** Technical replicates or repeated measurements of one animal are not independent experimental units; treating them as independent errors understates standard errors ([[Pseudoreplication]]).[^lazic]

## Core (L2)

### Residuals: what the model left

The residual $e_i = y_i - \hat y_i$ is the model's estimate of the error $\varepsilon_i$. Plot residuals against fitted values (or against $x$): if the assumptions hold, the points form an even, patternless band around 0.[^isl3]

![[residual-plot-patterns.svg]]

| Pattern in the residual plot | Problem | Usual response |
|---|---|---|
| Curve, U shape (B) | Mean not linear in $x$ | Transform $x$, add a polynomial term ([[Multiple Linear Regression]]) |
| Funnel, spread grows with fitted value (C) | Non-constant variance | Transform $y$ (log, square root), weights, or a GLM[^isl3] |
| Trend along run order, plate or date | Errors not independent | Model the batch or block; check the design |
| Heavy tails on a [[Q-Q Plot]] of residuals | Non-normal errors | Matters for small $n$ and prediction intervals |
| One point far in $x$ (D) | High leverage | Check the point; compare fits with and without it |

Normality concerns the errors, so it is judged on residuals, not on the raw $y$: a response made of two groups is bimodal even when the errors around each group's fitted value are perfectly normal.

### Leverage: unusual $x$

Least-squares fitted values are linear in the data, $\hat{\mathbf{y}} = H\mathbf{y}$ with the hat matrix $H = X(X^\top X)^{-1}X^\top$, the [[Orthogonal Projection]] onto the columns of $X$. The **leverage** $h_{ii}$ is its diagonal entry, the weight of $y_i$ in its own fitted value. In simple regression

$$h_{ii} = \frac{1}{n} + \frac{(x_i - \bar x)^2}{\sum_j (x_j - \bar x)^2},$$

between $1/n$ and 1, with average $p'/n$ for $p'$ coefficients ($p' = 2$ here).[^isl3] Leverage depends only on $x$. A high-leverage point pulls the line toward itself, so its residual is small even when its $y$ is wrong: $\operatorname{Var}(e_i) = \sigma^2(1 - h_{ii})$ (panel D, leverage 0.78).

### Outliers: unusual $y$ given $x$

Because residuals have unequal variances, compare them on a common scale. The **standardized residual** is $r_i = e_i / \big(s\sqrt{1 - h_{ii}}\big)$; the **studentized residual** $t_i$ replaces $s$ by $s_{(i)}$, the residual standard error of the fit without point $i$. Observations with studentized residuals beyond about 3 in absolute value are possible outliers.[^isl3] An outlier is a question, not a verdict: check the sample record (swap, contamination, failed library) before deciding, and report the fit with and without it.

### Influence: Cook's distance

A point is **influential** when deleting it changes the fit. Cook's distance measures the change in all fitted values,

$$D_i = \frac{\sum_j \big(\hat y_j - \hat y_{j(i)}\big)^2}{p'\,s^2} = \frac{r_i^2}{p'}\,\frac{h_{ii}}{1 - h_{ii}},$$

where $\hat y_{j(i)}$ is the fitted value of point $j$ without point $i$.[^cook] The second form shows that influence needs both ingredients: a large standardized residual and a high leverage. Cook built the measure on confidence ellipsoids:[^cook] if $D_i$ equals the $q$-quantile of the $F_{p',\,n-p'}$ distribution, deleting point $i$ moves the estimated coefficients to the edge of the $q \times 100\,\%$ joint confidence region ([[F-Distribution]]).

### Bio: counts break constant variance

For a gene's read count, the expected value grows with library size, and so does the variance: Poisson sampling contributes a variance equal to the mean,[^blitz] and biological variation between replicates adds more, growing with the square of the mean in the negative binomial model.[^anders][^msmb8] A straight line fitted to raw counts therefore shows a funnel (panel C). Every sample gets the same weight although high-count samples are much noisier, and the standard errors, built on one pooled variance, are too small for some fitted values and too large for others. Transformations reduce the problem (Exercise 5, [[Data Transformation]], [[Variance-Stabilizing Transformation]]); count models solve it by building the mean-variance relationship into the model ([[Poisson Regression]], [[Negative Binomial Regression]]).[^msmb8]

## Advanced (L3)

**Deleting a point without refitting.** The Sherman-Morrison formula ([[Inverse Matrix]]) gives closed forms for the fit without point $i$: the coefficients change by $\hat{\boldsymbol\beta} - \hat{\boldsymbol\beta}_{(i)} = (X^\top X)^{-1}\mathbf{x}_i\, e_i/(1 - h_{ii})$, the deleted residual is $y_i - \hat y_{(i)} = e_i/(1 - h_{ii})$, and $\mathrm{RSS}_{(i)} = \mathrm{RSS} - e_i^2/(1 - h_{ii})$. Three consequences:

- Cook's identity above follows by substituting the first formula into $(\hat{\boldsymbol\beta} - \hat{\boldsymbol\beta}_{(i)})^\top X^\top X (\hat{\boldsymbol\beta} - \hat{\boldsymbol\beta}_{(i)})/(p' s^2)$.
- Leave-one-out cross-validation of a least-squares fit costs a single fit: $\mathrm{CV}_{(n)} = \frac{1}{n}\sum_i \big(e_i/(1 - h_{ii})\big)^2$ ([[Cross-Validation]]).[^isl]
- Since $\mathrm{RSS}_{(i)} \ge 0$, $e_i^2 \le (1 - h_{ii})\,\mathrm{RSS}$, so $|r_i| \le \sqrt{n - p'}$: the standardized residual is bounded and can hide an enormous outlier, while the studentized residual is not (Worked example).

**Masking.** Leave-one-out measures can miss a pair of outliers: if two wrong points sit together far in $x$, deleting either one leaves the other to hold the line, and each looks harmless alone. Robust fits or a plot catch what single deletions miss.

**Unequal variances, done properly.** If $\operatorname{Var}(\varepsilon_i) = \sigma^2/w_i$ with known weights, minimizing $\sum_i w_i e_i^2$ (weighted least squares) restores valid standard errors. For counts the right weights depend on the mean being estimated, which is why it is cleaner to put the mean-variance relationship into the model itself, as a [[Generalized Linear Model]] does ([[Overdispersion]]).

**Diagnostics for 20,000 models.** A genomics analysis fits one model per gene, too many to inspect by eye. The checks become collective: the per-gene variance plotted against the per-gene mean, the relation that DESeq models by local regression,[^anders] and the histogram of p-values across genes, which for a well-calibrated test is flat except for a peak near 0 from true effects ([[P-Value]], [[Multiple Testing Correction]]); a hump elsewhere signals a misspecified model. Individual genes are then inspected on demand, starting with the strongest results.

## Mathematical representation

- $X$: $n \times p'$ design matrix of full rank ([[Design Matrix]]); $H = X(X^\top X)^{-1}X^\top$; $\hat{\mathbf{y}} = H\mathbf{y}$; $\mathbf{e} = (I - H)\mathbf{y}$; $s^2 = \mathrm{RSS}/(n - p')$.
- **Projection properties.** $H$ is symmetric and idempotent ($H^2 = H$), so $\operatorname{Var}(\mathbf{e}) = \sigma^2 (I - H)$ and $\operatorname{Var}(e_i) = \sigma^2 (1 - h_{ii})$. $\operatorname{tr} H = \operatorname{tr}\big((X^\top X)^{-1}X^\top X\big) = p'$, hence mean leverage $p'/n$. From $h_{ii} = \sum_j h_{ij}^2 \ge h_{ii}^2$: $0 \le h_{ii} \le 1$; with an intercept, $h_{ii} \ge 1/n$.
- **Residuals.** Standardized $r_i = e_i/(s\sqrt{1 - h_{ii}})$; studentized $t_i = e_i/(s_{(i)}\sqrt{1 - h_{ii}})$, which under the model with normal errors follows $t_{n - p' - 1}$; the two are linked by $t_i = r_i\sqrt{(n - p' - 1)/(n - p' - r_i^2)}$.
- **Cook's distance.** $D_i = (\hat{\boldsymbol\beta}_{(i)} - \hat{\boldsymbol\beta})^\top X^\top X (\hat{\boldsymbol\beta}_{(i)} - \hat{\boldsymbol\beta})/(p' s^2) = \frac{r_i^2}{p'}\frac{h_{ii}}{1 - h_{ii}}$.[^cook]
- **Variance of transformed counts** (delta method, $\operatorname{Var} g(Y) \approx g'(\mu)^2 \operatorname{Var}(Y)$). With $\operatorname{Var}(Y) = \mu + \phi\mu^2$ (negative binomial, dispersion $\phi$; $\phi = 0$ is Poisson): $\operatorname{Var}\sqrt{Y} \approx \frac{1}{4} + \frac{\phi\mu}{4}$ and $\operatorname{Var}\log Y \approx \frac{1}{\mu} + \phi$. The square root stabilizes Poisson noise, the logarithm the biological part; neither stabilizes both.

## Computational representation

Leverage, standardized residuals and Cook's distance for simple regression, by hand, on Anscombe's data:

```python
import math


def diagnostics(x, y):
    """Simple regression: leverage, standardized residual and Cook's distance per point."""
    n, p = len(x), 2                                   # p coefficients: intercept and slope
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    b1 = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx
    b0 = my - b1 * mx
    e = [b - b0 - b1 * a for a, b in zip(x, y)]
    s = math.sqrt(sum(v * v for v in e) / (n - p))
    out = []
    for a, ei in zip(x, e):
        h = 1 / n + (a - mx) ** 2 / sxx
        if h > 1 - 1e-12:                              # the fit passes exactly through this point
            out.append((h, float("nan"), float("nan")))
            continue
        r = ei / (s * math.sqrt(1 - h))
        out.append((h, r, r * r / p * h / (1 - h)))
    return b0, b1, out


# Anscombe's quartet, sets I, III and IV (Anscombe 1973)
x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
sets = {
    "I": (x, [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "III": (x, [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV": ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
           [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
for name, (xs, ys) in sets.items():
    b0, b1, d = diagnostics(xs, ys)
    i_h = max(range(len(xs)), key=lambda i: d[i][0])
    i_r = max(range(len(xs)), key=lambda i: abs(d[i][1]) if not math.isnan(d[i][1]) else -1)
    print(f"{name:<3} line {b0:.2f} + {b1:.3f}x | max leverage {d[i_h][0]:.3f} at x={xs[i_h]} | "
          f"max |r| {abs(d[i_r][1]):.2f} at ({xs[i_r]}, {ys[i_r]}), Cook's D {d[i_r][2]:.2f}")
```

```text
I   line 3.00 + 0.500x | max leverage 0.318 at x=14 | max |r| 1.78 at (13, 7.58), Cook's D 0.49
III line 3.00 + 0.500x | max leverage 0.318 at x=14 | max |r| 3.00 at (13, 12.74), Cook's D 1.39
IV  line 3.00 + 0.500x | max leverage 1.000 at x=19 | max |r| 1.57 at (8, 8.84), Cook's D 0.14
```

For several predictors, the same quantities come from the diagonal of $H$, computed from a QR decomposition of $X$ in practice ([[QR Decomposition]]).

## Worked example

> [!example] Diagnosing Anscombe's sets III and IV
> All three sets above share the line $\hat y = 3.00 + 0.500x$.[^anscombe]
> 1. **Set I (reference).** Largest standardized residual 1.78, largest leverage 0.318 (mean leverage $2/11 = 0.18$), Cook's $D \le 0.49$, below the median of $F_{2,9}$ (0.75): nothing stands out.
> 2. **Set III, the outlier.** The point (13, 12.74) has a moderate leverage, $1/11 + 16/110 = 0.236$, and a standardized residual of 3.00, exactly the bound $\sqrt{n - p'} = \sqrt 9$. Its Cook's distance, $3.00^2/2 \times 0.236/0.764 = 1.39$, is the 70th percentile of $F_{2,9}$: deleting this single point moves the coefficients to the edge of a 70 % confidence region.
> 3. **Studentized, it is enormous.** Without it, the ten other points lie almost exactly on $y = 4.006 + 0.345x$, which predicts 8.50 at $x = 13$; the studentized residual of 12.74 is about 1,200 (Exercise 3). The standardized residual, capped at 3, hid how extreme it is.
> 4. **Set IV, the lever.** The point at $x = 19$ has leverage $1/11 + 100/110 = 1$: the line goes through it exactly, so its residual is 0 and $r$ and $D$ are undefined. Without it all $x$ equal 8 and no slope can be estimated: this one observation is the whole slope (the design matrix becomes rank-deficient, see [[Design Matrix]]).
> 5. **Decision.** In a real dataset, both points would send us back to the sample records; the fit would be reported with and without them, never silently cleaned.

## Common misconceptions

> [!warning] "Outliers should be deleted"
> An outlier may be an error (swapped sample, failed library) or the most interesting observation. Investigate it, then report both fits; deleting points until the model fits invalidates its p-values.

> [!warning] "A point with a small residual is harmless"
> High leverage drags the line toward the point and shrinks its own residual: $\operatorname{Var}(e_i) = \sigma^2(1 - h_{ii})$. In Anscombe's set IV the decisive point has a residual of exactly 0.[^anscombe]

> [!warning] "The response must be normally distributed"
> The assumption is about the errors, checked on residuals. A response with two groups is bimodal with perfectly normal errors; with large $n$ the coefficients are close to normal anyway ([[Central Limit Theorem]]), and constant variance and independence matter more.

> [!warning] "Log-transforming counts fixes the variance"
> The logarithm stabilizes variation proportional to the mean, but inflates the variance of low counts and needs a pseudocount for zeros (Exercise 5, [[Scatter Plot#Advanced (L3)]]). Count models handle both regimes.[^msmb8]

## Exercises

> [!question] Exercise 1 (L2)
> For each residual-versus-fitted description, name the problem and a response: (a) residuals positive at both ends and negative in the middle; (b) residual spread three times larger at high fitted values; (c) residuals of samples sequenced on day 2 all positive.

> [!success]- Solution
> (a) Curvature: the mean is not linear; transform $x$ or add a quadratic term. (b) Non-constant variance: transform $y$, weight, or use a count model if $y$ is a count. (c) Dependence through batch: the day is a missing predictor; add it to the model, and in future balance conditions across days ([[Batch Effect]], [[Design Matrix]]).

> [!question] Exercise 2 (L2)
> Compute the leverages for $x = 1, 2, 3, 4, 10$ in simple regression. Check that they sum to $p'$ and compare the largest with the mean leverage.

> [!success]- Solution
> $\bar x = 4$, $S_{xx} = 9 + 4 + 1 + 0 + 36 = 50$, $h_i = 0.2 + (x_i - 4)^2/50$: 0.38, 0.28, 0.22, 0.20, 0.92. Sum $= 2.00 = p'$; mean 0.40. The point at $x = 10$ has more than twice the mean leverage: its $y$ largely decides the slope.

> [!question] Exercise 3 (L2, Python)
> With `diagnostics` and `sets` from the code above, refit Anscombe's set III without (13, 12.74). Then compute the studentized residual of that point: its deviation from the prediction of the reduced fit, divided by the prediction standard error ([[Linear Regression#Two intervals for prediction]]).

> [!success]- Solution
> ```python
> x3, y3 = sets["III"]
> keep = [i for i in range(len(x3)) if y3[i] != 12.74]
> xk, yk = [x3[i] for i in keep], [y3[i] for i in keep]
> b0k, b1k, dk = diagnostics(xk, yk)
> print(f"without (13, 12.74): y = {b0k:.3f} + {b1k:.4f}x, largest |r| {max(abs(v[1]) for v in dk):.2f}")
> n_k, mx_k = len(xk), sum(xk) / len(xk)
> s_k = math.sqrt(sum((b - b0k - b1k * a) ** 2 for a, b in zip(xk, yk)) / (n_k - 2))
> se = s_k * math.sqrt(1 + 1 / n_k + (13 - mx_k) ** 2 / sum((a - mx_k) ** 2 for a in xk))
> pred = b0k + b1k * 13
> print(f"predicted at x = 13 without it: {pred:.2f} (observed 12.74), studentized residual {(12.74 - pred) / se:.0f}")
> ```
> ```text
> without (13, 12.74): y = 4.006 + 0.3454x, largest |r| 1.80
> predicted at x = 13 without it: 8.50 (observed 12.74), studentized residual 1204
> ```
> The slope drops from 0.500 to 0.345. The other ten points are almost collinear, so $s_{(i)}$ is tiny and the studentized residual explodes, while the standardized one stayed at its bound of 3.

> [!question] Exercise 4 (L3)
> Prove that $\operatorname{tr} H = p'$ and $0 \le h_{ii} \le 1$. Show that $h_{ii} = 1$ forces $e_i = 0$, and derive $|r_i| \le \sqrt{n - p'}$ from $\mathrm{RSS}_{(i)} = \mathrm{RSS} - e_i^2/(1 - h_{ii})$.

> [!success]- Solution
> $\operatorname{tr}\big(X(X^\top X)^{-1}X^\top\big) = \operatorname{tr}\big((X^\top X)^{-1}X^\top X\big) = \operatorname{tr} I_{p'} = p'$. $H$ symmetric and idempotent gives $h_{ii} = (H^2)_{ii} = \sum_j h_{ij}^2 = h_{ii}^2 + \sum_{j \ne i} h_{ij}^2 \ge h_{ii}^2$, so $0 \le h_{ii} \le 1$. If $h_{ii} = 1$, then $\sum_{j \ne i} h_{ij}^2 = 0$, so $\hat y_i = \sum_j h_{ij} y_j = y_i$ and $e_i = 0$ whatever $y_i$ is. Finally $\mathrm{RSS}_{(i)} \ge 0$ gives $e_i^2/(1 - h_{ii}) \le \mathrm{RSS} = (n - p')s^2$, i.e. $r_i^2 \le n - p'$.

> [!question] Exercise 5 (L3, Python)
> Simulate read counts for 3,000 invented samples: expected count $2 \times$ library size (5 to 50 million reads), biological variation with dispersion $\phi = 0.1$ (gamma-Poisson). Fit count on library size on the raw, square-root and log scales, and compare the residual SD across thirds of the fitted values with the delta-method predictions.

> [!success]- Solution
> ```python
> import numpy as np
>
> rng = np.random.default_rng(11)
> lib = rng.uniform(5, 50, 3000)                     # library sizes, millions of reads (invented)
> mu = 2.0 * lib                                     # expected count: 2 reads per million
> lam = mu * rng.gamma(shape=10, scale=0.1, size=lib.size)   # biological variation, dispersion 0.1
> counts = rng.poisson(lam)
> for name, f in (("raw", lambda v: v), ("sqrt", np.sqrt), ("log", np.log)):
>     X = np.column_stack([np.ones(lib.size), f(lib)])
>     y = f(counts.astype(float))
>     beta, *_ = np.linalg.lstsq(X, y, rcond=None)
>     resid = y - X @ beta
>     thirds = np.array_split(np.argsort(X @ beta), 3)
>     print(f"{name:<4} residual SD by third of fitted values:",
>           [round(float(resid[t].std(ddof=1)), 2) for t in thirds])
> ```
> ```text
> raw  residual SD by third of fitted values: [9.82, 18.85, 28.25]
> sqrt residual SD by third of fitted values: [0.95, 1.27, 1.53]
> log  residual SD by third of fitted values: [0.41, 0.36, 0.35]
> ```
> Raw counts: the spread triples (the funnel). Square root: $\sqrt{1/4 + \phi\mu/4}$ predicts 0.94, 1.28 and 1.54 for the three ranges of $\mu$ (10 to 40, 40 to 70, 70 to 100): it removes the Poisson part only. Log: $\sqrt{1/\mu + \phi}$ predicts about 0.39, 0.35 and 0.34; nearly stable here because counts are at least 10, but it would blow up for counts near 0. No single transformation fits every regime, which is the case for modeling counts with a negative binomial [[Generalized Linear Model]].[^anders][^msmb8]

## Mastery checklist

- [ ] 1 Recognized: I can name the four assumptions of a linear model and the plot that checks each.
- [ ] 2 Understood: I can explain leverage, standardized and studentized residuals and Cook's distance, and why a high-leverage point can have a small residual.
- [ ] 3 Practiced: I can compute these diagnostics by hand and in Python, and read the four residual patterns.
- [ ] 4 Applied: on a real dataset (a qPCR curve or one gene's expression), I produced residual and leverage plots, identified influential samples and reported fits with and without them.
- [ ] 5 Explained: I can teach why counts violate constant variance, what transformations and GLMs each fix, and how diagnostics scale to thousands of per-gene models.

## References

[^isl3]: [[An Introduction to Statistical Learning (James)]], Python edition, ch. 3 "Linear Regression", potential problems of the linear model (chapter number as checked in [[Linear Models]]).
[^isl]: [[An Introduction to Statistical Learning (James)]], Python edition, resampling methods (leave-one-out cross-validation shortcut for least squares); chapter not verified.
[^anscombe]: [[Anscombe 1973 - Graphs in Statistical Analysis]], *The American Statistician* 27(1):17-21.
[^cook]: [[Cook 1977 - Detection of Influential Observation in Linear Regression]], *Technometrics* 19(1):15-18.
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the Poisson distribution (mean and variance).
[^anders]: [[Anders 2010 - Differential Expression Analysis for Sequence Count Data]], *Genome Biology* 11(10):R106.
[^msmb8]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 8 "High-Throughput Count Data" (chapter title as cited in [[Student's t-Distribution]]).
[^lazic]: [[Experimental Design for Laboratory Biologists (Lazic)]], experimental units and pseudoreplication.
