---
aliases:
  - Gradient Vector
  - Directional Derivative
  - Steepest Ascent
  - Nabla
  - Vecteur gradient
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - domain/computer-science
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Partial Derivative]]"
  - "[[Multivariable Function]]"
  - "[[Dot Product]]"
  - "[[Vector Norm]]"
related:
  - "[[Multivariable Chain Rule]]"
  - "[[Hessian Matrix]]"
  - "[[Gradient Descent]]"
  - "[[Stochastic Gradient Descent]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Least Squares]]"
  - "[[Logistic Regression]]"
  - "[[Lagrange Multiplier]]"
  - "[[Newton's Method]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.02SC - Multivariable Calculus]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Convex Optimization (Boyd)]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
---

# Gradient

> [!abstract]
> The gradient of a function of several variables is the vector of its partial derivatives: it points in the direction of steepest ascent, its length is the steepest slope, it is perpendicular to the contour lines, and setting it to zero or stepping against it is how models with many parameters are fitted.

## Definition

For a function $f(x_1, \dots, x_n)$ with partial derivatives, the **gradient** at $\mathbf{x}$ is the vector

$$\nabla f(\mathbf{x}) = \left(\frac{\partial f}{\partial x_1}(\mathbf{x}), \dots, \frac{\partial f}{\partial x_n}(\mathbf{x})\right).$$

For a unit vector $\mathbf{u}$, the **directional derivative** $D_{\mathbf{u}}f(\mathbf{x}) = \lim_{h \to 0}\frac{f(\mathbf{x} + h\mathbf{u}) - f(\mathbf{x})}{h}$ is the rate of change of $f$ in the direction $\mathbf{u}$. When $f$ is differentiable, $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$; hence $\nabla f$ points in the direction of greatest increase, its length $\lVert\nabla f\rVert$ is that greatest rate, and it is perpendicular to the level curve through the point.[^os3][^1802]

## Why it matters

- **Joint maximum likelihood.** A model with several parameters is fitted by maximizing its log-likelihood over all of them at once; at an interior maximum, $\nabla\ell(\boldsymbol\theta) = \mathbf{0}$, one equation per parameter ([[Maximum Likelihood Estimation]]).[^holmes]
- **Fitting by iteration.** When $\nabla\ell = \mathbf{0}$ has no closed-form solution (logistic regression, neural networks, the branch lengths of a tree likelihood in [[08-phylogenetic-engine]]), algorithms move along the gradient. Gradient descent repeats $\boldsymbol\theta \leftarrow \boldsymbol\theta - \eta\nabla L(\boldsymbol\theta)$ on a loss $L$; it is how neural networks are trained ([[Gradient Descent]], [[Stochastic Gradient Descent]]).[^boyd][^isl][^18065]
- **Several parameters changing together.** A mutation can shift both $K_M$ and $V_{max}$ of an enzyme; the directional derivative gives the joint effect from the [[Partial Derivative|partial derivatives]] alone.

## Core (L2)

### Computing the gradient and directional derivatives

For $f(x, y) = x^2y + y^3$, $\nabla f = (2xy,\ x^2 + 3y^2)$, so $\nabla f(1, 2) = (4, 13)$. In the direction $\mathbf{u} = (3, 4)/5$, $D_{\mathbf{u}}f(1, 2) = (4 \times 3 + 13 \times 4)/5 = 12.8$. The formula $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ follows from the [[Multivariable Chain Rule]] applied to the slice $g(t) = f(\mathbf{x} + t\mathbf{u})$: $g'(0) = \sum_j \partial_j f(\mathbf{x})\, u_j$.

### Steepest ascent and contours

With $\varphi$ the angle between $\mathbf{u}$ and $\nabla f$ ([[Dot Product]]),

$$D_{\mathbf{u}}f = \lVert\nabla f\rVert\,\lVert\mathbf{u}\rVert\cos\varphi = \lVert\nabla f\rVert\cos\varphi.$$

- $\varphi = 0$: the largest rate, $\lVert\nabla f\rVert$, in the direction of $\nabla f$ (**steepest ascent**).
- $\varphi = \pi$: the most negative rate, along $-\nabla f$ (**steepest descent**).
- $\varphi = \pi/2$: rate 0. Moving perpendicular to the gradient does not change $f$ to first order, so that direction is tangent to the level curve: **the gradient is perpendicular to the contours**.[^os3]

![[gradient-descent-elliptical-contours.svg]]

### Bio: joint maximum likelihood of several parameters

For the five invented replicate measurements of [[Multivariable Function]] (log2 expression 7.9, 8.4, 8.1, 7.6, 8.5) under a normal model,

$$\ell(\mu, \sigma) = -n\ln\sigma - \frac{n}{2}\ln(2\pi) - \frac{1}{2\sigma^2}\sum_{i}(x_i - \mu)^2, \qquad \nabla\ell = \left(\frac{\sum_i (x_i - \mu)}{\sigma^2},\ -\frac{n}{\sigma} + \frac{\sum_i (x_i - \mu)^2}{\sigma^3}\right).$$

Setting both components to zero: the first gives $\sum_i (x_i - \mu) = 0$, so $\hat\mu = \bar x$ whatever $\sigma$; substituting into the second gives $\hat\sigma^2 = \frac{1}{n}\sum_i (x_i - \bar x)^2$. Here $(\hat\mu, \hat\sigma) = (8.1, 0.3286)$ with $\ell = -1.531$: the peak that the grid search located only approximately. The estimate divides by $n$, not by $n - 1$ as the usual sample variance does. Whether a zero of the gradient is a maximum, a minimum or a saddle is decided by second derivatives ([[Hessian Matrix]]).

### Bio: the step of gradient descent

To minimize a loss $L(\boldsymbol\theta)$ (a sum of squares, or $-\ell$), gradient descent iterates

$$\boldsymbol\theta_{k+1} = \boldsymbol\theta_k - \eta\,\nabla L(\boldsymbol\theta_k), \qquad \eta > 0 \text{ the step size (learning rate)}.$$

Why it works: by the first-order approximation, $L(\boldsymbol\theta - \eta\nabla L) \approx L(\boldsymbol\theta) - \eta\lVert\nabla L\rVert^2 < L(\boldsymbol\theta)$, so a small enough step always decreases the loss.[^boyd] How small depends on curvature. In the figure, a straight line $y = a + bx$ is fitted to five invented points with centered $x$ ($\sum_i x_i = 0$, $\sum_i x_i^2 = 40$). Then $\nabla L = (10(a - \hat a),\ 80(b - \hat b))$, and each step multiplies the error in $a$ by $1 - 10\eta$ and the error in $b$ by $1 - 80\eta$. With $\eta = 0.02$ these factors are $0.8$ and $-0.6$: the slope overshoots back and forth (the zigzag) while the intercept creeps in. Above $\eta = 2/80 = 0.025$, the factor for $b$ exceeds 1 in size and the iteration diverges (Exercise 4).

## Advanced (L3)

- **Gradients of vector expressions.** $\nabla(\mathbf{a}\cdot\mathbf{x}) = \mathbf{a}$ and $\nabla(\mathbf{x}^\top A\mathbf{x}) = (A + A^\top)\mathbf{x}$. For least squares, $L(\boldsymbol\beta) = \lVert X\boldsymbol\beta - \mathbf{y}\rVert^2$ has $\nabla L = 2X^\top(X\boldsymbol\beta - \mathbf{y})$, and $\nabla L = \mathbf{0}$ is the system of normal equations $X^\top X\boldsymbol\beta = X^\top\mathbf{y}$ ([[Least Squares]]). For logistic regression, $\nabla\ell(\boldsymbol\beta) = X^\top(\mathbf{y} - \mathbf{p})$ (Exercise 5) has no closed-form zero, so the fit is iterative ([[Logistic Regression]], [[Newton's Method]]).
- **Step size and curvature.** On a quadratic loss with Hessian $H$, the error evolves as $\mathbf{e}_{k+1} = (I - \eta H)\mathbf{e}_k$, so gradient descent converges iff $0 < \eta < 2/\lambda_{max}(H)$, and the flattest direction then contracts only by $1 - \eta\lambda_{min}$ per step. Elongated contours (a large ratio $\lambda_{max}/\lambda_{min}$, the [[Condition Number]]) mean slow, zigzagging descent; rescaling the parameters or using curvature ([[Newton's Method]]) fixes it.
- **Stochastic gradients.** When the loss is a sum over millions of reads or cells, $L = \sum_i L_i$, the gradient of a random mini-batch, rescaled, has expectation $\nabla L$: a cheap, noisy but unbiased direction ([[Stochastic Gradient Descent]]).[^18065] Exact gradients of complex programs come from [[Automatic Differentiation]].
- **Constraints.** At a maximum of $f$ on the curve $g = c$, the level curve of $f$ is tangent to the constraint, so $\nabla f = \lambda\nabla g$ for some $\lambda$ ([[Lagrange Multiplier]]).[^os3] Maximizing the multinomial log-likelihood $\sum_j n_j\ln p_j$ under $\sum_j p_j = 1$ this way gives allele frequencies $\hat p_j = n_j/n$ (Exercise 6).

## Mathematical representation

- $\nabla f(\mathbf{x}) = (\partial_1 f, \dots, \partial_n f)^\top \in \mathbb{R}^n$. $f$ is differentiable at $\mathbf{x}$ when $f(\mathbf{x} + \mathbf{h}) = f(\mathbf{x}) + \nabla f(\mathbf{x})\cdot\mathbf{h} + o(\lVert\mathbf{h}\rVert)$.
- Directional derivative: $D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u}$, and by the Cauchy-Schwarz inequality $|D_{\mathbf{u}}f| \le \lVert\nabla f\rVert$, with equality iff $\mathbf{u} = \pm\nabla f/\lVert\nabla f\rVert$.
- Orthogonality to level sets: if a curve $\mathbf{r}(t)$ stays in $\{f = c\}$, differentiating $f(\mathbf{r}(t)) = c$ gives $\nabla f(\mathbf{r}(t))\cdot\mathbf{r}'(t) = 0$.
- Critical point: an interior extremum $\mathbf{x}^*$ of a differentiable $f$ has $\nabla f(\mathbf{x}^*) = \mathbf{0}$ (the converse is false).
- Gradient descent on $L(\boldsymbol\theta) = \frac12(\boldsymbol\theta - \boldsymbol\theta^*)^\top H(\boldsymbol\theta - \boldsymbol\theta^*) + c$: $\nabla L = H(\boldsymbol\theta - \boldsymbol\theta^*)$. In the example, $L(a, b) = L_{min} + 5(a - \hat a)^2 + 40(b - \hat b)^2$, so $H = \operatorname{diag}(10, 80)$: the ellipses of the figure.

## Computational representation

The analytic gradient of the normal log-likelihood checked against central differences, steepest ascent, one ascent step, the closed-form zero, then gradient descent on the least-squares loss of the figure, by hand and with NumPy:

```python
import math

data = [7.9, 8.4, 8.1, 7.6, 8.5]          # invented log2 expression (as in Multivariable Function)
n = len(data)


def loglik(mu, sigma):
    return (-n * math.log(sigma) - n / 2 * math.log(2 * math.pi)
            - sum((x - mu) ** 2 for x in data) / (2 * sigma ** 2))


def grad_loglik(mu, sigma):
    """Analytic gradient (dl/dmu, dl/dsigma)."""
    ss = sum((x - mu) ** 2 for x in data)
    return sum(x - mu for x in data) / sigma ** 2, -n / sigma + ss / sigma ** 3


def numerical_gradient(f, p, h=1e-6):
    """Central differences, one coordinate at a time."""
    g = []
    for i in range(len(p)):
        up, down = list(p), list(p)
        up[i] += h
        down[i] -= h
        g.append((f(*up) - f(*down)) / (2 * h))
    return g


p0 = (7.9, 0.5)
g = grad_loglik(*p0)
print([round(v, 4) for v in g], [round(v, 4) for v in numerical_gradient(loglik, p0)])
norm = math.hypot(*g)
print(round(norm, 3), [round(v / norm, 3) for v in g])                   # steepest ascent
u = (1 / math.sqrt(2), 1 / math.sqrt(2))
print(round(g[0] * u[0] + g[1] * u[1], 3))                              # directional derivative

eta = 0.02                                                              # one ascent step
p1 = (p0[0] + eta * g[0], p0[1] + eta * g[1])
print([round(v, 4) for v in p1], round(loglik(*p0), 3), round(loglik(*p1), 3), round(eta * norm ** 2, 3))

mu_hat = sum(data) / n                                                  # solve grad = 0
sigma_hat = math.sqrt(sum((x - mu_hat) ** 2 for x in data) / n)
print(round(mu_hat, 4), round(sigma_hat, 4), [abs(round(v, 9)) for v in grad_loglik(mu_hat, sigma_hat)])

# Gradient descent on a least-squares loss (the figure): straight line y = a + b x
xs = [-4.0, -2.0, 0.0, 2.0, 4.0]          # invented, centered predictor
ys = [1.0, 2.1, 2.9, 4.2, 4.8]


def loss_grad(a, b):
    """Gradient of L(a, b) = sum (y - a - b x)^2."""
    res = [y - a - b * x for x, y in zip(xs, ys)]
    return -2 * sum(res), -2 * sum(r * x for r, x in zip(res, xs))


a, b = 1.2, 1.1
for k in range(60):
    if k < 3:
        print(k, round(a, 4), round(b, 4), [round(v, 2) for v in loss_grad(a, b)])
    ga, gb = loss_grad(a, b)
    a, b = a - 0.02 * ga, b - 0.02 * gb
print(round(a, 4), round(b, 4))

import numpy as np

X = np.column_stack([np.ones(5), xs])     # design matrix: intercept column, x column
y = np.array(ys)
beta = np.array([1.2, 1.1])
for _ in range(200):
    beta -= 0.02 * 2 * X.T @ (X @ beta - y)                 # gradient 2 X^T (X beta - y)
print(beta.round(4), np.linalg.lstsq(X, y, rcond=None)[0].round(4))
```

```text
[4.0, -4.08] [4.0, -4.08]
5.714 [0.7, -0.714]
-0.057
[7.98, 0.4184] -2.609 -1.986 0.653
8.1 0.3286 [0.0, 0.0]
0 1.2 1.1 [-18.0, 49.2]
1 1.56 0.116 [-14.4, -29.52]
2 1.848 0.7064 [-11.52, 17.71]
3.0 0.485
[3.    0.485] [3.    0.485]
```

The second component of $\nabla L$ changes sign at every step (49.2, −29.52, 17.71): the zigzag of the figure. Both implementations reach the least-squares solution $(\hat a, \hat b) = (3.0, 0.485)$ returned by `np.linalg.lstsq`.

## Worked example

> [!example] One step uphill on the likelihood surface (same invented data)
> Start at $(\mu, \sigma) = (7.9, 0.5)$.
> 1. **Gradient by hand**: $\sum_i (x_i - 7.9) = 40.5 - 39.5 = 1.0$, so $\partial\ell/\partial\mu = 1.0/0.25 = 4.0$. The deviations $0, 0.5, 0.2, -0.3, 0.6$ have squares summing to $0.74$, so $\partial\ell/\partial\sigma = -5/0.5 + 0.74/0.125 = -10 + 5.92 = -4.08$. Hence $\nabla\ell = (4.0, -4.08)$, as the code confirms numerically.
> 2. **Steepest ascent**: $\lVert\nabla\ell\rVert = 5.714$, direction $(0.700, -0.714)$: raise the mean and lower the standard deviation by similar amounts.
> 3. **Another direction**: along $\mathbf{u} = (1, 1)/\sqrt2$, $D_{\mathbf{u}}\ell = (4.0 - 4.08)/\sqrt2 = -0.057$, almost zero: this direction is nearly tangent to the contour through the point.
> 4. **One step** with $\eta = 0.02$: $(7.9 + 0.08,\ 0.5 - 0.0816) = (7.98, 0.4184)$. The log-likelihood rises from $-2.609$ to $-1.986$, a gain of 0.623, close to the first-order prediction $\eta\lVert\nabla\ell\rVert^2 = 0.653$.
> 5. **Stop where?** Iterating, the steps shrink with the gradient and approach $(8.1, 0.3286)$, where $\nabla\ell = \mathbf{0}$; here the closed form gets there directly.

## Common misconceptions

> [!warning] "The gradient points toward the optimum"
> It points in the direction of steepest local change, perpendicular to the contour. On elongated contours that direction can be almost at right angles to the line toward the optimum, which is why gradient descent zigzags in the figure.

> [!warning] "$\nabla f = \mathbf{0}$ means a maximum (or a minimum)"
> It means a critical point: maximum, minimum or saddle. For $f = x^2 - y^2$, $\nabla f(0, 0) = \mathbf{0}$ at a saddle. Check with the [[Hessian Matrix]] or with the function itself.

> [!warning] "A larger learning rate always converges faster"
> Only up to $2/\lambda_{max}$. Beyond it the iterates oscillate with growing amplitude (Exercise 4).

> [!warning] "The gradient does not depend on how parameters are measured"
> Rescaling a parameter ($\theta = c\,\phi$, for instance µM instead of mM) multiplies its partial derivative by $c$ ($\partial L/\partial\phi = c\,\partial L/\partial\theta$), which changes the direction of $\nabla L$ and the path of gradient descent. Centering and scaling predictors is part of fitting, not cosmetics.

## Exercises

> [!question] Exercise 1 (L2)
> For $f(x, y) = x^2y + y^3$ at $(1, 2)$, compute $\nabla f$, the directional derivative along $(3, 4)/5$, and the maximal rate of increase.

> [!success]- Solution
> $\nabla f = (2xy, x^2 + 3y^2) = (4, 13)$. $D_{\mathbf{u}}f = (4 \times 3 + 13 \times 4)/5 = 64/5 = 12.8$. The maximal rate is $\lVert\nabla f\rVert = \sqrt{16 + 169} = \sqrt{185} \approx 13.60$, in the direction $(4, 13)/\sqrt{185}$; the chosen direction is close to it ($12.8 / 13.6 = \cos\varphi \approx 0.94$).

> [!question] Exercise 2 (L2)
> Check that $\nabla f$ is perpendicular to the level curve of $f(x, y) = x^2 + 4y^2$ through $(2, 1)$.

> [!success]- Solution
> $\nabla f(2, 1) = (2x, 8y) = (4, 8)$. On the level curve $x^2 + 4y^2 = 8$, differentiating implicitly gives $2x\,dx + 8y\,dy = 0$, i.e. $4\,dx + 8\,dy = 0$ at $(2, 1)$: a tangent direction is $(2, -1)$. The dot product $(4, 8)\cdot(2, -1) = 0$.

> [!question] Exercise 3 (L2)
> Two populations are genotyped for one SNP (invented counts): 30 of 100 alleles carry the variant in population 1, 45 of 120 in population 2. Write the joint log-likelihood $\ell(p_1, p_2)$ of the two allele frequencies, compute its gradient at $(0.35, 0.35)$ and find the joint maximum likelihood estimate.

> [!success]- Solution
> $\ell = 30\ln p_1 + 70\ln(1 - p_1) + 45\ln p_2 + 75\ln(1 - p_2)$ (binomial constants dropped). $\nabla\ell = \left(\frac{30}{p_1} - \frac{70}{1 - p_1},\ \frac{45}{p_2} - \frac{75}{1 - p_2}\right) = (-21.98, 13.19)$ at $(0.35, 0.35)$: lower $p_1$, raise $p_2$. Each component involves one parameter only, so $\nabla\ell = \mathbf{0}$ splits into two one-variable equations: $\hat p_1 = 0.30$ and $\hat p_2 = 0.375$, the observed frequencies ([[Extremum]]).

> [!question] Exercise 4 (L2, Python)
> Run gradient descent on the least-squares loss of the figure (`loss_grad` from the code above) for 100 steps from $(1.2, 1.1)$ with $\eta = 0.01, 0.02, 0.024, 0.026$. Explain the result with the factors $1 - 10\eta$ and $1 - 80\eta$.

> [!success]- Solution
> ```python
> for eta in (0.01, 0.02, 0.024, 0.026):
>     a, b = 1.2, 1.1
>     for _ in range(100):
>         ga, gb = loss_grad(a, b)
>         a, b = a - eta * ga, b - eta * gb
>     print(eta, round(a, 4), round(b, 4))
> ```
> Output: `0.01 3.0 0.485`, `0.02 3.0 0.485`, `0.024 3.0 0.4851`, `0.026 3.0 1353.3382`. The error in $b$ is multiplied by $1 - 80\eta$ each step: $0.2$, $-0.6$, $-0.92$ (slow, oscillating convergence) and $-1.08$ (divergence). The intercept converges in all four runs, since $|1 - 10\eta| < 1$ throughout: the steepest direction alone sets the speed limit, $\eta < 2/80$.

> [!question] Exercise 5 (L3)
> Show that $\nabla_{\boldsymbol\beta}\lVert X\boldsymbol\beta - \mathbf{y}\rVert^2 = 2X^\top(X\boldsymbol\beta - \mathbf{y})$. For logistic regression, with $p_i = \sigma(\mathbf{x}_i^\top\boldsymbol\beta)$, $\sigma(z) = 1/(1 + e^{-z})$ and $\ell(\boldsymbol\beta) = \sum_i [y_i\ln p_i + (1 - y_i)\ln(1 - p_i)]$, show that $\nabla\ell = X^\top(\mathbf{y} - \mathbf{p})$.

> [!success]- Solution
> $\lVert X\boldsymbol\beta - \mathbf{y}\rVert^2 = \sum_i (\mathbf{x}_i^\top\boldsymbol\beta - y_i)^2$; its partial derivative in $\beta_j$ is $\sum_i 2(\mathbf{x}_i^\top\boldsymbol\beta - y_i)x_{ij}$, the $j$-th entry of $2X^\top(X\boldsymbol\beta - \mathbf{y})$. For the logistic case, $\frac{d}{dz}\ln\sigma(z) = 1 - \sigma(z)$ and $\frac{d}{dz}\ln(1 - \sigma(z)) = -\sigma(z)$, so the chain rule gives $\frac{\partial\ell}{\partial\beta_j} = \sum_i [y_i(1 - p_i) - (1 - y_i)p_i]\,x_{ij} = \sum_i (y_i - p_i)\,x_{ij}$: residuals weighted by the predictors, as for least squares.

> [!question] Exercise 6 (L3)
> Three alleles of a gene are observed 50, 30 and 20 times (invented). Maximize $\ell(p_1, p_2, p_3) = \sum_j n_j\ln p_j$ under $p_1 + p_2 + p_3 = 1$ with the condition $\nabla\ell = \lambda\nabla g$, where $g = p_1 + p_2 + p_3$.

> [!success]- Solution
> $\nabla\ell = (n_1/p_1, n_2/p_2, n_3/p_3)$ and $\nabla g = (1, 1, 1)$, so $n_j/p_j = \lambda$ for every $j$: $p_j = n_j/\lambda$. The constraint gives $\lambda = n_1 + n_2 + n_3 = 100$, hence $(\hat p_1, \hat p_2, \hat p_3) = (0.5, 0.3, 0.2)$: the observed proportions. At the optimum, the contour of $\ell$ touches the constraint plane.

## Mastery checklist

- [ ] 1 Recognized: I can write the gradient of a function and state that it points uphill, perpendicular to the contours.
- [ ] 2 Understood: I can derive $D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u}$, explain steepest ascent with the cosine, and explain why gradient descent decreases the loss for small steps.
- [ ] 3 Practiced: I solve $\nabla\ell = \mathbf{0}$ for simple likelihoods, check analytic gradients numerically, and implement gradient descent with a sensible step size.
- [ ] 4 Applied: I fitted a real model by gradient-based optimization (for example branch lengths in [[08-phylogenetic-engine]] or a logistic regression on real data) and diagnosed its convergence.
- [ ] 5 Explained: I can teach how curvature limits the step size, why scaling matters, why stochastic gradients work, and the geometry of Lagrange multipliers.

## References

[^os3]: [[Calculus (OpenStax)]], Volume 3, ch. 4 "Differentiation of Functions of Several Variables": section "Directional Derivatives and the Gradient" (directional derivative as a dot product, direction of greatest increase, gradient perpendicular to level curves), and the treatment of Lagrange multipliers in the same chapter.
[^1802]: [[MIT 18.02SC - Multivariable Calculus]], differential calculus part (gradient and directional derivatives).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of statistical modeling (maximum likelihood estimation).
[^boyd]: [[Convex Optimization (Boyd)]], algorithms part (unconstrained minimization: descent methods, gradient descent and steepest descent).
[^isl]: [[An Introduction to Statistical Learning (James)]], deep learning chapter (fitting a neural network by gradient descent).
[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], lecture 25 "Stochastic Gradient Descent".
