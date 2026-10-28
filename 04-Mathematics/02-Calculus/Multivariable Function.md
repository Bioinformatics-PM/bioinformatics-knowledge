---
aliases:
  - Function of Several Variables
  - Function of Two Variables
  - Level Curve
  - Contour Map
  - Fonction de plusieurs variables
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Function]]"
  - "[[Continuity]]"
  - "[[Logarithm]]"
  - "[[Vector]]"
related:
  - "[[Partial Derivative]]"
  - "[[Gradient]]"
  - "[[Hessian Matrix]]"
  - "[[Multiple Integral]]"
  - "[[Likelihood Function]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Normal Distribution]]"
  - "[[Parameter Identifiability]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.02SC - Multivariable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
---

# Multivariable Function

> [!abstract]
> A multivariable function assigns one number to each combination of several inputs, like a log-likelihood that scores every pair of parameter values; you read it as a surface over a plane, as a contour map of level curves, or through one-variable slices.

## Definition

A **function of two variables** $f$ assigns to each point $(x, y)$ of a domain $D \subseteq \mathbb{R}^2$ exactly one real number $z = f(x, y)$; its **range** is the set of values taken. More generally $f : D \subseteq \mathbb{R}^n \to \mathbb{R}$. The **graph** of $f(x, y)$ is the surface $z = f(x, y)$ in three-dimensional space. A **level curve** is the set of points of $D$ where $f(x, y) = c$ for a constant $c$, and a **contour map** draws level curves for equally spaced values of $c$. For three variables, the level sets are surfaces.[^os3][^1802]

## Why it matters

- **Every model with several parameters.** A likelihood depends on all parameters at once: mean and standard deviation of a normal model, $V_{max}$ and $K_M$ of an enzyme ([[Michaelis-Menten Kinetics]]), the rate and capacity of a growth curve, the branch lengths of a tree in [[08-phylogenetic-engine]]. Fitting a model means finding the top of a likelihood surface, or the bottom of a loss surface ([[Likelihood Function]], [[Maximum Likelihood Estimation]], [[Loss Function]]).
- **Contour maps show uncertainty.** Wide contours around the optimum mean poorly determined parameters; tilted, elongated contours mean that two parameters can compensate for each other ([[Parameter Identifiability]]).
- **Joint densities.** A density $f(x, y)$ of two measurements is a function of two variables whose volume over a region is a probability ([[Multiple Integral]], [[Multivariate Normal Distribution]]).
- **Heatmaps.** A heatmap of a function evaluated on a grid is a contour map drawn in color.

## Core (L2)

### Domain, range and graph

$f(x, y) = \sqrt{9 - x^2 - y^2}$ needs $x^2 + y^2 \le 9$: its domain is a disk of radius 3, its range $[0, 3]$, its graph the upper half of a sphere.[^os3] Parameters usually have constrained domains: a standard deviation $\sigma > 0$, a probability in $[0, 1]$, a rate constant $> 0$.

### Slices: back to one variable

Fixing $y = y_0$ leaves an ordinary function $g(x) = f(x, y_0)$, the curve where the surface meets the vertical plane $y = y_0$ (a **trace**). Everything known about single-variable functions applies to slices; the slopes of slices are the [[Partial Derivative|partial derivatives]].

### Level curves and how to read a contour map

| Function | Level curves $f = c$ | Shape of the surface |
|---|---|---|
| $x^2 + 4y^2$ | ellipses around the origin | a bowl, steeper in $y$ |
| $2x - y$ | parallel lines | a tilted plane |
| $xy$ | hyperbolas, and the two axes for $c = 0$ | a saddle at the origin |

Reading rules: closed nested contours surround a peak or a pit (the labels tell which); closely spaced contours mean a steep surface; elongated contours mean a ridge or valley along which $f$ hardly changes; contours of one level crossing in an X mark a saddle ([[Hessian Matrix]]). Contours of different levels never meet, since $f$ has one value per point.

### Bio: a likelihood surface over two parameters

Five replicate measurements of the log2 expression of one gene (invented): $x_i$ = 7.9, 8.4, 8.1, 7.6, 8.5. Model them as independent draws from a [[Normal Distribution]] with density $f(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-(x - \mu)^2/(2\sigma^2)}$.[^blitz] With the data fixed, the log-likelihood is a function of the two parameters ([[Likelihood Function]]):[^holmes]

$$\ell(\mu, \sigma) = \sum_{i=1}^{n} \ln f(x_i; \mu, \sigma) = -n\ln\sigma - \frac{n}{2}\ln(2\pi) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \mu)^2, \qquad \mu \in \mathbb{R},\ \sigma > 0.$$

![[normal-log-likelihood-contours.svg]]

- **One peak**, at $(\mu, \sigma) \approx (8.1, 0.33)$ with $\ell \approx -1.53$; the [[Gradient]] note finds it exactly.
- **Symmetry in $\mu$.** With $\bar x = 8.1$ and $S = \sum_i (x_i - \bar x)^2 = 0.54$, the sum of squares splits as $\sum_i (x_i - \mu)^2 = S + n(\mu - \bar x)^2$. Every horizontal slice is therefore $\ell(\mu, \sigma_0) = \text{const} - \frac{n(\mu - \bar x)^2}{2\sigma_0^2}$, a downward parabola with vertex at $\bar x$ whatever $\sigma_0$ (right panel): the best mean does not depend on the assumed spread.
- **Asymmetry in $\sigma$.** Contours crowd toward small $\sigma$ and spread out toward large $\sigma$. A too-small $\sigma$ makes the observed spread very improbable, a too-large one only mildly so: with five replicates, the data rule out small standard deviations much more firmly than large ones.

## Advanced (L3)

- **Limits need every path.** $(x, y) \to (a, b)$ can happen along infinitely many paths, and a limit exists only if they all give the same value.[^os3] For $f(x, y) = \frac{xy}{x^2 + y^2}$, the line $y = mx$ gives $f = \frac{m}{1 + m^2}$, a value that depends on $m$: no limit at the origin, although the slices $f(x, 0) = 0$ and $f(0, y) = 0$ are perfectly continuous. Checking slices is not enough (Exercise 4).
- **Beyond two parameters.** A model with $p$ parameters has a likelihood on a $p$-dimensional domain, and contour maps stop at $p = 2$. Two practical views remain: two-dimensional slices through the optimum, and **profiles**, which maximize over the other parameters for each value of the one of interest. For the normal model, maximizing over $\sigma$ gives $\sigma^2(\mu) = \frac{1}{n}\sum_i (x_i - \mu)^2$ and the profile $\ell_p(\mu) = -\frac{n}{2}\ln\sigma^2(\mu) - \frac{n}{2} - \frac{n}{2}\ln(2\pi)$. Locally, the [[Gradient]] and the [[Hessian Matrix]] summarize the surface in any dimension.
- **Ridges and identifiability.** If a model depends on two parameters only through a combination, the surface has a ridge of equally good values: for $y = abx$, only the product $ab$ matters, and the loss is constant along each hyperbola $ab = \text{const}$, so no unique optimum exists (Exercise 5). A long, nearly flat valley is the practical version of the same problem ([[Parameter Identifiability]]).
- **Vector-valued functions.** A system of rate equations maps the vector of all concentrations to the vector of all rates, $F : \mathbb{R}^n \to \mathbb{R}^m$; each component is a multivariable function, and their derivatives assemble into the [[Jacobian Matrix]].

## Mathematical representation

- $f : D \subseteq \mathbb{R}^n \to \mathbb{R}$, $\mathbf{x} = (x_1, \dots, x_n) \mapsto f(\mathbf{x})$. Graph: $G_f = \{(\mathbf{x}, f(\mathbf{x})) : \mathbf{x} \in D\} \subset \mathbb{R}^{n+1}$. Level set: $L_c = \{\mathbf{x} \in D : f(\mathbf{x}) = c\}$; superlevel set: $\{\mathbf{x} \in D : f(\mathbf{x}) \ge c\}$.
- Slice through $\mathbf{x}_0$ along coordinate $j$: $g_j(t) = f(\mathbf{x}_0 + t\,\mathbf{e}_j)$, with $\mathbf{e}_j$ the $j$-th unit [[Vector]]; along any unit direction $\mathbf{u}$: $t \mapsto f(\mathbf{x}_0 + t\,\mathbf{u})$.
- Limit: $\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = L$ iff for every $\varepsilon > 0$ there is $\delta > 0$ such that $\mathbf{x} \in D$ and $0 < \lVert \mathbf{x} - \mathbf{a} \rVert < \delta$ imply $|f(\mathbf{x}) - L| < \varepsilon$ ([[Vector Norm]]); $f$ is continuous at $\mathbf{a}$ when the limit equals $f(\mathbf{a})$.
- Log-likelihood of a parameter vector $\boldsymbol\theta \in \Theta \subseteq \mathbb{R}^p$ for fixed data: $\ell(\boldsymbol\theta) = \sum_{i=1}^{n}\ln f(x_i; \boldsymbol\theta)$.
- Decomposition used above: $\sum_i (x_i - \mu)^2 = \sum_i (x_i - \bar x)^2 + n(\bar x - \mu)^2$, because the cross term $2(\bar x - \mu)\sum_i (x_i - \bar x)$ vanishes.

## Computational representation

In code, a function of two variables is a function of two arguments; to see it, evaluate it on a grid. Plotting libraries draw contours and heatmaps from exactly such a grid; here a text map stands in for the plot:

```python
import math

data = [7.9, 8.4, 8.1, 7.6, 8.5]          # invented log2 expression of one gene, 5 replicates


def loglik(mu, sigma):
    """Normal log-likelihood of the data: a function of the two variables (mu, sigma)."""
    n = len(data)
    return (-n * math.log(sigma) - n / 2 * math.log(2 * math.pi)
            - sum((x - mu) ** 2 for x in data) / (2 * sigma ** 2))


# A function of two variables is "seen" through its values on a grid
mus = [7.5 + 0.01 * i for i in range(121)]          # 7.50 ... 8.70
sigmas = [0.10 + 0.005 * j for j in range(181)]     # 0.100 ... 1.000
best = max((loglik(m, s), m, s) for m in mus for s in sigmas)
print([round(v, 3) for v in best])

# Text contour map: one symbol per band of 1 log-likelihood unit below the top
symbols = "@#*+=-:. "
for s in (0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2):
    row = "".join(symbols[min(8, int(best[0] - loglik(m, s)))]
                  for m in [7.5 + 0.05 * i for i in range(25)])
    print(f"sigma={s:.1f} |{row}|")

# Slices: fix sigma, and the best mu stays the same
for s0 in (0.3, 0.6):
    print(s0, round(max(mus, key=lambda m: loglik(m, s0)), 2))

import numpy as np

M, S = np.meshgrid(np.array(mus), np.array(sigmas))   # 181 x 121 arrays of coordinates
x = np.array(data)[:, None, None]                     # broadcast the data over the grid
L = (-len(data) * np.log(S) - len(data) / 2 * np.log(2 * np.pi)
     - ((x - M) ** 2).sum(axis=0) / (2 * S ** 2))
j, i = np.unravel_index(L.argmax(), L.shape)
print(L.shape, round(float(L.max()), 3), round(float(M[j, i]), 2), round(float(S[j, i]), 3))
```

```text
[-1.531, 8.1, 0.33]
sigma=0.9 |++++++++*********++++++++|
sigma=0.8 |++++*****************++++|
sigma=0.7 |+++******#######******+++|
sigma=0.6 |++****#############****++|
sigma=0.5 |=++**####@@@@@@@####**++=|
sigma=0.4 |-==+**##@@@@@@@@@##**+==-|
sigma=0.3 |  :-=+*##@@@@@@@##*+=-:  |
sigma=0.2 |      .-=+*###*+=-.      |
0.3 8.1
0.6 8.1
(181, 121) -1.531 8.1 0.33
```

`@` marks points within one unit of the maximum, `#` within two, and so on: the map reproduces the figure, with its symmetry in $\mu$ and its steep side at small $\sigma$. A grid only locates the optimum to its spacing (here $\sigma = 0.33$ instead of the exact 0.3286), and costs $121 \times 181 = 21{,}901$ evaluations for two parameters; with ten parameters, a grid this fine would be hopeless, which is why optimizers follow the [[Gradient]] instead.

## Worked example

> [!example] Reading the likelihood surface with slices (same invented data)
> Here $n = 5$, $\bar x = 8.1$, $S = 0.54$ and $\frac{n}{2}\ln(2\pi) = 4.5947$.
> 1. **Horizontal slice $\sigma = 0.5$**: $\ell(\mu, 0.5) = -5\ln 0.5 - 4.5947 - \frac{0.54 + 5(\mu - 8.1)^2}{0.5} = -2.209 - 10(\mu - 8.1)^2$. At $\mu = 8.1$, $\ell = -2.209$; at $\mu = 7.6$ or $8.6$, $\ell = -4.709$: half a unit off in $\mu$ costs 2.5 log-likelihood units.
> 2. **Vertical slice $\mu = 8.1$**: $\ell(8.1, \sigma) = -5\ln\sigma - 4.5947 - \frac{0.27}{\sigma^2}$. Its derivative $-\frac{5}{\sigma} + \frac{0.54}{\sigma^3}$ vanishes at $\sigma^2 = 0.108$, so $\sigma = 0.3286$ and $\ell = -1.531$, the top of the surface.
> 3. **A level curve**: the contour $\ell = -1.531 - 2 = -3.531$ crosses the vertical line $\mu = 8.1$ twice, at $\sigma = 0.195$ and $\sigma = 0.731$ (solved numerically), and the horizontal line $\sigma = 0.3286$ at $\mu = 8.1 \pm 0.294$.
> 4. **Read it**: the contour extends 0.13 below the best $\sigma$ but 0.40 above it. A symmetric "$\hat\sigma \pm$ error" summary would hide this asymmetry, which the contour map shows at a glance.

## Common misconceptions

> [!warning] "If every slice is continuous, the function is continuous"
> $\frac{xy}{x^2 + y^2}$ (with value 0 at the origin) is continuous along both axes, yet takes the value $\frac12$ all along the line $y = x$, arbitrarily close to the origin. Continuity is about all ways of approaching a point.

> [!warning] "Maximizing one parameter at a time finds the joint maximum"
> It works here only because the best $\mu$ does not depend on $\sigma$. When parameters are correlated (tilted, elongated contours), the best value of one changes with the other, and coordinate-by-coordinate searches crawl along the valley. The joint optimum solves all the equations at once ([[Gradient]]).

> [!warning] "The likelihood surface is a probability density over the parameters"
> $\ell(\mu, \sigma)$ is a function of the parameters for fixed data; it does not integrate to 1 over $(\mu, \sigma)$. Turning it into a distribution over parameters requires a prior ([[Bayesian Inference]]).

## Exercises

> [!question] Exercise 1 (L2)
> Give the domain and range of $f(x, y) = \ln(x - y^2)$ and of $g(x, y) = \sqrt{1 - x^2 - 4y^2}$, and describe their level curves.

> [!success]- Solution
> $f$ needs $x > y^2$: the region to the right of the parabola $x = y^2$; its range is $\mathbb{R}$, and the level curves $x - y^2 = e^c$ are parabolas shifted to the right. $g$ needs $x^2 + 4y^2 \le 1$: the inside of an ellipse; its range is $[0, 1]$, and the level curves $x^2 + 4y^2 = 1 - c^2$ are nested ellipses, shrinking to the point $(0, 0)$ at $c = 1$.

> [!question] Exercise 2 (L2)
> Sketch the level curves of $h(x, y) = x^2 - y^2$ for $c = -1, 0, 1$. What kind of point is the origin, and why can a contour map show it while no single slice through the origin along an axis gives the whole picture?

> [!success]- Solution
> $c = \pm 1$ gives hyperbolas opening along the $x$ axis ($c = 1$) or the $y$ axis ($c = -1$); $c = 0$ gives the two lines $y = \pm x$, crossing in an X. The origin is a saddle: the slice $y = 0$ ($h = x^2$) has a minimum there, the slice $x = 0$ ($h = -y^2$) a maximum. Each slice alone shows only one of the two behaviors.

> [!question] Exercise 3 (L2)
> For the normal log-likelihood, show that the vertical slice $\mu = \bar x$ is maximal at $\sigma^2 = S/n$, and that the maximum over all $(\mu, \sigma)$ is at $(\bar x, \sqrt{S/n})$.

> [!success]- Solution
> On $\mu = \bar x$, $\ell = -n\ln\sigma - \frac{n}{2}\ln 2\pi - \frac{S}{2\sigma^2}$, with derivative $-\frac{n}{\sigma} + \frac{S}{\sigma^3}$, positive for $\sigma^2 < S/n$ and negative beyond: a maximum at $\sigma^2 = S/n$. For any $(\mu, \sigma)$, $\ell(\mu, \sigma) \le \ell(\bar x, \sigma)$ because the term $n(\mu - \bar x)^2 \ge 0$ is subtracted, and $\ell(\bar x, \sigma) \le \ell(\bar x, \sqrt{S/n})$ by the first part.

> [!question] Exercise 4 (L3, Python)
> Evaluate $f(x, y) = \frac{xy}{x^2 + y^2}$ along the lines $y = mx$ for $m = 0, 1, -1, 2$ as $x \to 0$. Conclude.

> [!success]- Solution
> ```python
> def f(x, y):
>     return x * y / (x ** 2 + y ** 2)
>
> for m in (0, 1, -1, 2):
>     print(m, [round(f(t, m * t), 4) for t in (0.1, 0.001, 1e-6)])
> ```
> Output: `0 [0.0, 0.0, 0.0]`, `1 [0.5, 0.5, 0.5]`, `-1 [-0.5, -0.5, -0.5]`, `2 [0.4, 0.4, 0.4]`. Each line gives the constant $\frac{m}{1 + m^2}$, different for different $m$: the limit at the origin does not exist.

> [!question] Exercise 5 (L3, Python)
> An invented signal model $y = abx$ (cells per well $a$ times signal per cell and per unit dose $b$, dose $x$) is fitted to $x = 1, 2, 3, 4$ and $y = 0.62, 1.18, 1.83, 2.41$ by least squares. Evaluate the loss at $(a, b) = (1, 0.6), (2, 0.3), (0.5, 1.2), (3, 0.2)$. Describe the contour map and propose a fix.

> [!success]- Solution
> ```python
> xs, ys = [1.0, 2.0, 3.0, 4.0], [0.62, 1.18, 1.83, 2.41]
>
> def sse(a, b):
>     return sum((y - a * b * x) ** 2 for x, y in zip(xs, ys))
>
> for a, b in ((1.0, 0.6), (2.0, 0.3), (0.5, 1.2), (3.0, 0.2)):
>     print(a, b, round(sse(a, b), 4))
> ```
> Output: the same loss, `0.0018`, at all four points. The loss depends only on $c = ab$, so every level curve is a hyperbola $ab = \text{const}$ and the minimum is a whole curve, not a point: $a$ and $b$ are not identifiable from these data. Fit $c = ab$ alone, or measure $a$ (count the cells) separately.

## Mastery checklist

- [ ] 1 Recognized: I can state the domain, range, graph and level curves of a function of two variables.
- [ ] 2 Understood: I can read a contour map (peaks, saddles, steepness, ridges) and explain what slices and level curves of a likelihood surface mean.
- [ ] 3 Practiced: I evaluate functions on grids in Python and NumPy, draw text or plotted contour maps, and solve level-curve problems by hand.
- [ ] 4 Applied: I plotted a real two-parameter likelihood surface (for example two branch lengths of a tree in [[08-phylogenetic-engine]]) and interpreted its shape.
- [ ] 5 Explained: I can teach why limits need all paths, how profiles and slices show high-dimensional likelihoods, and how ridges reveal non-identifiable parameters.

## References

[^os3]: [[Calculus (OpenStax)]], Volume 3, ch. 4 "Differentiation of Functions of Several Variables": functions of several variables (domain and range, graphs, level curves and contour maps, vertical traces, functions of three variables and level surfaces) and limits and continuity in several variables.
[^1802]: [[MIT 18.02SC - Multivariable Calculus]], differential calculus part (functions of several variables).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., continuous random variables (the normal distribution and its density).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of statistical modeling (the likelihood as a function of the parameters for fixed data, maximum likelihood).
