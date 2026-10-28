---
aliases:
  - Partial Derivatives
  - Partial Differentiation
  - Mixed Partial Derivative
  - Dérivée partielle
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Multivariable Function]]"
  - "[[Derivative]]"
  - "[[Differentiation Rules]]"
related:
  - "[[Gradient]]"
  - "[[Multivariable Chain Rule]]"
  - "[[Jacobian Matrix]]"
  - "[[Hessian Matrix]]"
  - "[[Linear Approximation]]"
  - "[[Sensitivity Analysis]]"
  - "[[Michaelis-Menten Kinetics]]"
  - "[[Finite Difference]]"
  - "[[Partial Differential Equation]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.02SC - Multivariable Calculus]]"
  - "[[Biochemistry (Berg)]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[Mathematical Biology (Murray)]]"
---

# Partial Derivative

> [!abstract]
> A partial derivative measures how a function of several variables changes when one variable moves and all the others stay fixed: the slope of one slice of the surface, and the local sensitivity of a model's output to one of its parameters.

## Definition

For a function $f(x, y)$, the **partial derivative with respect to $x$** at $(a, b)$ is

$$\frac{\partial f}{\partial x}(a, b) = \lim_{h \to 0}\frac{f(a + h, b) - f(a, b)}{h},$$

and $\frac{\partial f}{\partial y}$ is defined in the same way, moving $y$ only. Other notations are $f_x$ and $\partial_x f$. It is computed with the ordinary rules of differentiation, treating every other variable as a constant. Geometrically, $f_x(a, b)$ is the slope at $x = a$ of the slice $z = f(x, b)$ of the surface ([[Multivariable Function]]). For $f(x_1, \dots, x_n)$, $\frac{\partial f}{\partial x_j}$ varies $x_j$ alone.[^os3][^1802]

## Why it matters

- **Sensitivity to one parameter.** $\frac{\partial y}{\partial p}$ tells how much a model output $y$ moves per unit change of the parameter $p$, the others fixed. The relative version $\frac{p}{y}\frac{\partial y}{\partial p}$ is unit-free, so parameters measured in different units can be ranked ([[Sensitivity Analysis]]).
- **Likelihood equations.** Setting each partial derivative of a log-likelihood to zero gives one equation per parameter; solving them together is the job of the [[Gradient]] ([[Maximum Likelihood Estimation]]).
- **Interactions in dynamic models.** $\frac{\partial}{\partial y}\big(\frac{dx}{dt}\big)$ says how species $y$ changes the growth rate of $x$. The table of all such partial derivatives is the [[Jacobian Matrix]], which decides the stability of a steady state ([[Lotka-Volterra Model]]).
- **Equations in space and time.** Equations that relate partial derivatives with respect to time and to position are [[Partial Differential Equation|partial differential equations]].

## Core (L2)

### Computing: freeze the other variables

For $f(x, y) = x^3y^2 - 4xy + e^{xy}$:

$$f_x = 3x^2y^2 - 4y + y\,e^{xy}, \qquad f_y = 2x^3y - 4x + x\,e^{xy}.$$

In $f_x$, $y^2$ is a constant factor and the chain rule on $e^{xy}$ brings out $\frac{\partial}{\partial x}(xy) = y$ ([[Differentiation Rules]]).

### Geometry: slopes of slices

![[partial-derivative-slices.svg]]

Through one point of a surface pass several slices, one per variable. Each partial derivative is the slope of one of them; together they describe the tilt of the surface at that point, which the [[Gradient]] packages as a vector.[^os3]

### Second-order partial derivatives

Differentiating again gives $f_{xx}$, $f_{yy}$ and the **mixed** partial derivatives $f_{xy} = \frac{\partial}{\partial y}\big(\frac{\partial f}{\partial x}\big)$ and $f_{yx}$. In the example, $f_{xy} = 6x^2y - 4 + e^{xy} + xy\,e^{xy} = f_{yx}$. This is no accident: if the mixed partial derivatives are continuous near a point, they are equal there (Clairaut's theorem).[^os3] The second derivatives assemble into the [[Hessian Matrix]].

### Bio: sensitivity of an enzyme's velocity to its parameters

The Michaelis-Menten velocity $v = \frac{V_{max}S}{K_M + S}$ is a function of three variables: substrate concentration $S$, maximal velocity $V_{max}$ and Michaelis constant $K_M$ ([[Michaelis-Menten Kinetics]]).[^berg] [[Differentiation Rules]] computed $\frac{\partial v}{\partial S}$; the parameters give

$$\frac{\partial v}{\partial V_{max}} = \frac{S}{K_M + S}, \qquad \frac{\partial v}{\partial K_M} = -\frac{V_{max}S}{(K_M + S)^2}.$$

The relative sensitivities are $\frac{V_{max}}{v}\frac{\partial v}{\partial V_{max}} = 1$ and $\frac{K_M}{v}\frac{\partial v}{\partial K_M} = -\frac{K_M}{K_M + S}$. The velocity is always proportional to $V_{max}$, but it responds to $K_M$ only at low substrate: the relative sensitivity goes from $-1$ when $S \ll K_M$ to 0 when $S \gg K_M$. Measurements at saturating substrate therefore carry almost no information about $K_M$: an enzyme assay meant to estimate $K_M$ needs concentrations around and below it ([[Parameter Identifiability]], [[Nonlinear Least Squares]]).

## Advanced (L3)

- **Partial derivatives are not enough for differentiability.** $f(x, y) = \frac{xy}{x^2 + y^2}$, with $f(0, 0) = 0$, vanishes on both axes, so $f_x(0, 0) = f_y(0, 0) = 0$; yet $f$ is not even continuous at the origin ([[Multivariable Function]]). The right notion is **differentiability**: $f(a + h, b + k) = f(a, b) + f_x h + f_y k + o(\sqrt{h^2 + k^2})$, the tangent-plane approximation ([[Linear Approximation]]). It holds when the partial derivatives exist and are continuous near the point.[^os3]
- **Numerical partial derivatives.** The central difference $\frac{f(\mathbf{x} + h\mathbf{e}_j) - f(\mathbf{x} - h\mathbf{e}_j)}{2h}$ has a truncation error proportional to $h^2$, but rounding errors grow like $1/h$ as $h$ shrinks, so $h$ must balance the two ([[Finite Difference]], [[Floating-Point Arithmetic]]). This is how sensitivities of simulation models without formulas are computed.
- **Sensitivities are local.** $\frac{\partial v}{\partial K_M}$ describes small changes around one point and changes with $S$. For dynamic models the sensitivity of the trajectory changes over time: early logistic growth depends on the rate $r$, the plateau on the capacity $K$ (Exercise 5). When parameters are uncertain over wide ranges, global methods vary them jointly ([[Sensitivity Analysis]]).

## Mathematical representation

- For $f : D \subseteq \mathbb{R}^n \to \mathbb{R}$ and $\mathbf{a}$ inside $D$: $\dfrac{\partial f}{\partial x_j}(\mathbf{a}) = \lim_{h \to 0}\dfrac{f(\mathbf{a} + h\,\mathbf{e}_j) - f(\mathbf{a})}{h} = g_j'(0)$, with $g_j(t) = f(\mathbf{a} + t\,\mathbf{e}_j)$ the slice along the unit vector $\mathbf{e}_j$.
- Notations: $\frac{\partial f}{\partial x_j} = f_{x_j} = \partial_j f$; second order $\frac{\partial^2 f}{\partial x_i \partial x_j}$, symmetric in $i, j$ when continuous.
- Linear approximation of a differentiable $f$: $f(\mathbf{a} + \mathbf{h}) \approx f(\mathbf{a}) + \sum_{j=1}^{n}\partial_j f(\mathbf{a})\, h_j$.
- Relative sensitivity of $y > 0$ to $p > 0$: $S_p = \frac{p}{y}\frac{\partial y}{\partial p} = \frac{\partial \ln y}{\partial \ln p}$ (by the [[Multivariable Chain Rule]]): the percentage change of $y$ per percent change of $p$, for small changes.
- For a system $\mathbf{x}' = F(\mathbf{x})$, the Jacobian entries are $J_{ij} = \partial F_i/\partial x_j$.

## Computational representation

Analytic partial derivatives of the Michaelis-Menten velocity, checked by central differences, with the relative sensitivity to $K_M$:

```python
def v(S, Vmax, Km):
    """Michaelis-Menten velocity: a function of three variables."""
    return Vmax * S / (Km + S)


def partial(f, args, i, h=1e-6):
    """Central-difference estimate of the partial derivative of f in its argument i."""
    up, down = list(args), list(args)
    up[i] += h
    down[i] -= h
    return (f(*up) - f(*down)) / (2 * h)


Vmax, Km = 10.0, 2.0                                   # invented parameters
print(" S   dv/dVmax  dv/dKm  numerical  relative(Km)")
for S in (0.5, 2.0, 8.0):
    d_vmax = S / (Km + S)                              # analytic partial derivatives
    d_km = -Vmax * S / (Km + S) ** 2
    num = partial(v, (S, Vmax, Km), 2)                 # same partial, numerically
    rel = d_km * Km / v(S, Vmax, Km)                   # (Km / v) dv/dKm
    print(f"{S:4.1f} {d_vmax:8.3f} {d_km:8.3f} {num:9.3f} {rel:10.3f}")
```

```text
 S   dv/dVmax  dv/dKm  numerical  relative(Km)
 0.5    0.200   -0.800    -0.800     -0.800
 2.0    0.500   -1.250    -1.250     -0.500
 8.0    0.800   -0.800    -0.800     -0.200
```

The absolute sensitivity $|\partial v/\partial K_M|$ peaks at $S = K_M$, while the relative one decreases steadily with $S$: always say which of the two a "sensitivity" means.

## Worked example

> [!example] Predicting the effect of a mutation on velocity (invented values)
> An enzyme has $V_{max} = 10$ and $K_M = 2$ (arbitrary units), assayed at $S = 2$. A mutation raises $K_M$ by 10 %, to 2.2.
> 1. **Value**: $v = \frac{10 \times 2}{2 + 2} = 5$.
> 2. **Partial derivative**: $\frac{\partial v}{\partial K_M} = -\frac{10 \times 2}{(2 + 2)^2} = -1.25$, the slope of the right slice in the figure.
> 3. **Linear prediction**: $\Delta v \approx \frac{\partial v}{\partial K_M}\,\Delta K_M = -1.25 \times 0.2 = -0.25$, a 5 % drop; equivalently, relative sensitivity $-0.5$ times $+10\,\%$.
> 4. **Exact**: $v = \frac{20}{4.2} = 4.762$, a drop of 0.238 (4.8 %). The partial derivative predicts the change well because 10 % is small.
> 5. **Compare**: a 10 % change in $V_{max}$ changes $v$ by exactly 10 % ($\partial v/\partial V_{max} = 0.5$ and $v$ is linear in $V_{max}$). At this substrate level, $V_{max}$ matters twice as much as $K_M$.

## Common misconceptions

> [!warning] "$\partial f/\partial x$ is how $f$ changes when $x$ changes"
> Only when everything else is held fixed. If $y$ moves with $x$ (along a trajectory, or because one parameter is computed from another), the total change involves all paths of dependence ([[Multivariable Chain Rule]]). In a fitted model, changing one parameter often makes the others re-adjust.

> [!warning] "If the partial derivatives exist, the function is smooth"
> They only probe the axis directions. $\frac{xy}{x^2 + y^2}$ has both partial derivatives at the origin and is discontinuous there; differentiability needs, for example, continuous partial derivatives.

> [!warning] "A large sensitivity means an important parameter"
> $\frac{\partial v}{\partial K_M}$ and $\frac{\partial v}{\partial V_{max}}$ have different units and cannot be compared directly. Compare relative sensitivities, and remember that they depend on the operating point ($S$ here).

## Exercises

> [!question] Exercise 1 (L2, Python)
> For $f(x, y) = x^3y^2 - 4xy + e^{xy}$, compute $f_{xy}$ and $f_{yx}$ by hand and evaluate them at $(1, 2)$. Check with a numerical mixed difference.

> [!success]- Solution
> From $f_x = 3x^2y^2 - 4y + ye^{xy}$: $f_{xy} = 6x^2y - 4 + e^{xy} + xye^{xy}$. From $f_y = 2x^3y - 4x + xe^{xy}$: $f_{yx} = 6x^2y - 4 + e^{xy} + xye^{xy}$, the same. At $(1, 2)$: $12 - 4 + e^2 + 2e^2 = 8 + 3e^2 \approx 30.167$.
> ```python
> import math
>
> f = lambda x, y: x ** 3 * y ** 2 - 4 * x * y + math.exp(x * y)
> h = 1e-4
> fxy = (f(1 + h, 2 + h) - f(1 + h, 2 - h) - f(1 - h, 2 + h) + f(1 - h, 2 - h)) / (4 * h * h)
> print(round(fxy, 4), round(8 + 3 * math.exp(2), 4))
> ```
> Output: `30.1672 30.1672`.

> [!question] Exercise 2 (L2)
> A transcription factor at concentration $x$ activates a gene through the Hill function $h(x; K, n) = \frac{x^n}{K^n + x^n}$.[^8591] Show that the relative sensitivity of $h$ to the threshold $K$ is $-n(1 - h)$. Evaluate it at $x = K$ for $n = 1$ and $n = 4$, and for $n = 4$ at $x = K/2$ and $x = 2K$.

> [!success]- Solution
> $\frac{\partial h}{\partial K} = -\frac{x^n \cdot nK^{n-1}}{(K^n + x^n)^2}$, so $\frac{K}{h}\frac{\partial h}{\partial K} = -\frac{nK^n}{K^n + x^n} = -n(1 - h)$. At $x = K$, $h = \frac12$: $-0.5$ for $n = 1$ (the Michaelis-Menten case), $-2$ for $n = 4$. For $n = 4$: $h(K/2) = 1/17$ gives $-3.765$, and $h(2K) = 16/17$ gives $-0.235$. Cooperativity makes the output four times more sensitive to the threshold at the switch point, which is why mutations in binding sites can matter so much for switch-like genes.

> [!question] Exercise 3 (L2)
> In the Lotka-Volterra model, prey grow at rate $F(x, y) = ax - bxy$ and predators at $G(x, y) = -cy + dxy$.[^murray] Compute the four partial derivatives, give their signs for positive populations, and evaluate them at the equilibrium $(c/d, a/b)$.

> [!success]- Solution
> $F_x = a - by$, $F_y = -bx < 0$, $G_x = dy > 0$, $G_y = -c + dx$. The signs of $F_y$ and $G_x$ are the predator-prey signature: predators lower the prey's growth rate, prey raise the predators'. At $(c/d, a/b)$: $F_x = 0$, $F_y = -bc/d$, $G_x = ad/b$, $G_y = 0$, the entries of the [[Jacobian Matrix]] whose eigenvalues $\pm i\sqrt{ac}$ give the cycles of [[Complex Number]].

> [!question] Exercise 4 (L3)
> For $f(x, y) = \frac{xy}{x^2 + y^2}$ with $f(0, 0) = 0$, show that $f_x(0, 0)$ and $f_y(0, 0)$ exist, and that the tangent plane they suggest is a bad approximation along the diagonal.

> [!success]- Solution
> $f(h, 0) = 0$ for all $h$, so $f_x(0, 0) = \lim_{h \to 0}\frac{0 - 0}{h} = 0$; likewise $f_y(0, 0) = 0$. The candidate tangent plane is $z = 0$. On the diagonal, $f(t, t) = \frac12$ for every $t \neq 0$: the error does not shrink as $t \to 0$, so $f$ is not differentiable at the origin even though both partial derivatives exist.

> [!question] Exercise 5 (L3, Python)
> Logistic growth $N(t) = \frac{K}{1 + \frac{K - N_0}{N_0}e^{-rt}}$ (invented: $N_0 = 0.01$, $K = 1$ in optical density units, $r = 0.8$ per hour).[^murray] Compute the relative sensitivities $\frac{\partial \ln N}{\partial \ln r}$ and $\frac{\partial \ln N}{\partial \ln K}$ at several times by central differences on $\ln r$ and $\ln K$. Which parts of a growth curve inform each parameter?

> [!success]- Solution
> ```python
> import math
>
> def logistic(t, r, K, N0=0.01):
>     """Logistic growth curve N(t)."""
>     return K / (1 + (K - N0) / N0 * math.exp(-r * t))
>
> def relative_sensitivity(f, args, i, h=1e-6):
>     """d ln f / d ln p_i, by central differences on ln p_i."""
>     up, down = list(args), list(args)
>     up[i] *= math.exp(h)
>     down[i] *= math.exp(-h)
>     return (math.log(f(*up)) - math.log(f(*down))) / (2 * h)
>
> r, K = 0.8, 1.0                                        # invented: per hour, OD units
> for t in (2, 5, 8, 12, 16):
>     N = logistic(t, r, K)
>     s_r = relative_sensitivity(logistic, (t, r, K), 1)
>     s_k = relative_sensitivity(logistic, (t, r, K), 2)
>     print(f"t={t:2d} h  N={N:.3f}  S_r={s_r:.3f}  S_K={s_k:.3f}  r*t*(1-N/K)={r * t * (1 - N / K):.3f}")
> ```
> Output:
> ```text
> t= 2 h  N=0.048  S_r=1.524  S_K=0.038  r*t*(1-N/K)=1.524
> t= 5 h  N=0.355  S_r=2.578  S_K=0.349  r*t*(1-N/K)=2.578
> t= 8 h  N=0.859  S_r=0.904  S_K=0.857  r*t*(1-N/K)=0.904
> t=12 h  N=0.993  S_r=0.064  S_K=0.993  r*t*(1-N/K)=0.064
> t=16 h  N=1.000  S_r=0.003  S_K=1.000  r*t*(1-N/K)=0.003
> ```
> The numerical $S_r$ matches the formula $S_r = rt(1 - N/K)$ obtained by differentiating, and $S_K = (1 - e^{-rt})N/K$ similarly. The rate is informed by the growth phase (largest around mid-growth), the capacity by the plateau: a growth curve stopped at 5 h pins down $r$ but barely $K$.

## Mastery checklist

- [ ] 1 Recognized: I can define a partial derivative and compute $f_x$ and $f_y$ of a simple formula.
- [ ] 2 Understood: I can explain a partial derivative as the slope of a slice, state when mixed partials are equal, and interpret a relative sensitivity.
- [ ] 3 Practiced: I compute first and second partial derivatives by hand and check them with central differences in Python.
- [ ] 4 Applied: I computed the sensitivities of a real model (enzyme kinetics or a growth curve fitted to plate-reader data) to each parameter and used them to choose measurement conditions.
- [ ] 5 Explained: I can teach why partial derivatives do not imply differentiability, how numerical step sizes are chosen, and why local sensitivities depend on the operating point.

## References

[^os3]: [[Calculus (OpenStax)]], Volume 3, ch. 4 "Differentiation of Functions of Several Variables": partial derivatives (definition, geometric interpretation, higher-order partial derivatives and the equality of mixed partials), tangent planes, linear approximations and differentiability.
[^1802]: [[MIT 18.02SC - Multivariable Calculus]], differential calculus part (partial derivatives).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of enzyme kinetics (the Michaelis-Menten equation, $K_M$ and $V_{max}$).
[^8591]: [[MIT 8.591J - Systems Biology]], lecture "Input Function, Michaelis-Menten Kinetics, and Cooperativity" (Hill input functions of transcription factors).
[^murray]: [[Mathematical Biology (Murray)]], 3rd ed., Volume I, population models (logistic growth; the Lotka-Volterra predator-prey system).
