---
aliases:
  - Differentiation
  - Rate of Change
  - Slope of the Tangent
  - Dérivée
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Limit]]"
  - "[[Continuity]]"
  - "[[Exponential Function]]"
related:
  - "[[Differentiation Rules]]"
  - "[[Linear Approximation]]"
  - "[[Extremum]]"
  - "[[Antiderivative]]"
  - "[[Partial Derivative]]"
  - "[[Finite Difference]]"
  - "[[Ordinary Differential Equation]]"
  - "[[Exponential Growth]]"
  - "[[Reaction Kinetics]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Microbiology (OpenStax)]]"
---

# Derivative

> [!abstract]
> The derivative $f'(x)$ says how fast $f$ changes at $x$: it is the slope of the tangent line to the graph and the instantaneous rate of change, measured in units of $f$ per unit of $x$.

## Definition

The **derivative** of $f$ at $a$ is

$$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h},$$

when this limit exists; $f$ is then **differentiable** at $a$. The fraction is the slope of the secant line through $(a, f(a))$ and $(a + h, f(a + h))$; its limit is the slope of the **tangent line** at $a$. The function $x \mapsto f'(x)$ is the derivative of $f$, also written $\frac{dy}{dx}$ or $\frac{df}{dx}$; a time derivative is often written $\dot x = \frac{dx}{dt}$.[^calc1][^1801]

## Why it matters

- **Rates are the language of models.** Growth ($dN/dt$), reaction velocity ($d[P]/dt$), mRNA production and decay ($dm/dt$): an [[Ordinary Differential Equation]] is a statement about a derivative.
- **Estimation.** A maximum likelihood estimate is found where the derivative of the log-likelihood is zero ([[Extremum]], [[Maximum Likelihood Estimation]]).
- **Sensitivity.** $f'(a)$ is the change of a model output per unit change of one input: how much an enzyme's velocity responds to more substrate, the one-variable case of the [[Gradient]].
- **Rates from data.** Growth rates from plate-reader curves or rates from time courses are estimated by finite differences or by fitting; both need to know what the derivative is and how noise affects it (Advanced).

## Core (L1)

**From average to instantaneous rate.** The average rate of change of $f$ on $[a, a + h]$ is $\frac{f(a + h) - f(a)}{h}$, the slope of a secant. Letting $h \to 0$ gives the instantaneous rate at $a$, the slope of the tangent.[^calc1] The tangent line is $y = f(a) + f'(a)(x - a)$, the best straight-line stand-in for $f$ near $a$ ([[Linear Approximation]]).

![[secant-tangent-slope.svg]]

**Units.** $f'$ has the units of $f$ divided by those of $x$. With $N$ in cells/mL and $t$ in hours, $dN/dt$ is in cells/mL/h; with $[P]$ in µM and $t$ in seconds, $d[P]/dt$ is in µM/s. Checking units catches most interpretation errors.

**Signs.** $f' > 0$ on an interval means $f$ increases there, $f' < 0$ that it decreases (proved in Deeper with the mean value theorem); $f'(a) = 0$ means a horizontal tangent, a candidate maximum or minimum ([[Extremum]]).

**Differentiating from the definition.** Three examples, each a limit computation ([[Limit]]):

1. $f(x) = x^2$: $\ \frac{(x + h)^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h \to 2x$.
2. $f(x) = 1/x$: $\ \frac{1}{h}\left(\frac{1}{x + h} - \frac1x\right) = \frac{-1}{x(x + h)} \to -\frac{1}{x^2}$ for $x \neq 0$.
3. $N(t) = N_0 e^{rt}$: $\ \frac{N_0 e^{r(t + h)} - N_0 e^{rt}}{h} = N_0 e^{rt} \cdot r \cdot \frac{e^{rh} - 1}{rh} \to r N_0 e^{rt}$, because $\frac{e^u - 1}{u} \to 1$ as $u = rh \to 0$.

The shortcuts that avoid redoing such limits are the [[Differentiation Rules]].

**Bio: growth rate $dN/dt$.** Example 3 says $\frac{dN}{dt} = rN$: the absolute growth rate is proportional to the population. Dividing by $N$ gives the **specific (per-capita) growth rate** $\frac{1}{N}\frac{dN}{dt} = r$, constant during exponential growth, as in the exponential phase of a bacterial culture where the population doubles every generation time.[^micro] The doubling time is $\ln 2 / r$ ([[Exponential Growth]], [[Bacterial Growth]]).

**Bio: reaction velocity $d[P]/dt$.** The rate of a reaction is the change in concentration of a reactant or product per unit time; the instantaneous rate at time $t$ is the slope of the tangent to the concentration-time curve at $t$.[^chem12] For a product it is $d[P]/dt$; for a reactant, whose concentration falls, the rate is written $-d[S]/dt$ so that it is positive. In enzyme kinetics the **initial velocity** $v_0$ is this slope at the start of the reaction, before substrate depletion bends the curve ([[Michaelis-Menten Kinetics]]).[^berg]

## Deeper (L2)

**Differentiable implies continuous, not the converse.** If $f'(a)$ exists, $f(a + h) - f(a) = h \cdot \frac{f(a + h) - f(a)}{h} \to 0 \cdot f'(a) = 0$, so $f$ is continuous at $a$.[^calc1] The converse fails: $|x|$ is continuous at 0, but its difference quotient $|h|/h$ is $+1$ for $h > 0$ and $-1$ for $h < 0$, so no derivative exists (a corner). $\sqrt[3]{x}$ has a vertical tangent at 0: the quotient $h^{-2/3} \to \infty$.

**Higher derivatives.** $f'' = (f')'$ is the rate of change of the rate: acceleration for a position, curvature for a graph. $f'' > 0$ means the slope increases (concave up), $f'' < 0$ that it decreases (concave down); a growth curve's inflection point, where the growth rate peaks, has $N'' = 0$ ([[Logistic Growth]]).

**Mean value theorem (MVT).** If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, there is $c \in (a, b)$ with

$$f'(c) = \frac{f(b) - f(a)}{b - a}:$$

the average rate is attained as an instantaneous rate somewhere.[^calc1] Consequences: $f' > 0$ on an interval implies $f$ strictly increasing; $f' = 0$ implies $f$ constant, which is why two antiderivatives differ by a constant ([[Antiderivative]]); $|f'| \le M$ implies $|f(x) - f(y)| \le M|x - y|$, the bound used to certify root searches in [[Continuity#Advanced (L3)]].

**Specific rates are slopes on a log scale.** By the chain rule ([[Differentiation Rules]]), $\frac{d}{dt}\ln N(t) = \frac{N'(t)}{N(t)}$. The per-capita growth rate is the slope of $\ln N$ against $t$: exponential growth is a straight line on a log plot, with slope $r$ ([[Logarithm]]). This is how growth rates are read from optical-density curves (Exercise 5).

## Advanced (L3)

**Numerical derivatives and the step size.** A program approximates $f'(x)$ by a difference quotient ([[Finite Difference]]). Expanding $f$ around $x$ ([[Taylor Series]]) gives the truncation errors:

$$\frac{f(x + h) - f(x)}{h} = f'(x) + \frac{h}{2}f''(\xi), \qquad \frac{f(x + h) - f(x - h)}{2h} = f'(x) + \frac{h^2}{6}f'''(\eta),$$

for some $\xi, \eta$ near $x$: the forward difference has error of order $h$, the central difference of order $h^2$. But $f$ is computed with a relative error near machine epsilon $\varepsilon \approx 2.2 \times 10^{-16}$, and dividing that by $h$ adds a rounding error of order $\varepsilon|f|/h$ that grows as $h$ shrinks ([[Rounding Error]]). Balancing the two puts the best $h$ near $\sqrt{\varepsilon} \approx 10^{-8}$ for the forward difference and near $\varepsilon^{1/3} \approx 10^{-5}$ for the central one, as the table below shows.

**Derivatives of noisy data.** If each measurement carries independent noise of standard deviation $\sigma$, the difference of two measurements has standard deviation $\sqrt 2\,\sigma$ ([[Variance]]), so a forward difference over a step $h$ carries noise $\sqrt 2\,\sigma/h$: the finer the time grid, the noisier the estimated rate. Rates from noisy time courses are therefore estimated by fitting a line to several points (for example $\ln$ OD over a window, [[Linear Regression]]) or a model, not by differencing neighbouring points.

**The derivative as the best linear map.** Equivalently, $f$ is differentiable at $a$ when $f(a + h) = f(a) + f'(a)\,h + r(h)$ with $r(h)/h \to 0$. This form, "linear part plus a remainder smaller than $h$", is the one that generalizes to several variables: the linear part becomes the [[Gradient]] or the [[Jacobian Matrix]], and the chain rule for compositions becomes the engine of automatic differentiation ([[Differentiation Rules#Advanced (L3)]]).

## Mathematical representation

- Definition: $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$.
- Notations: $f'(x) = \frac{df}{dx} = \frac{d}{dx}f(x)$; second derivative $f''(x) = \frac{d^2 f}{dx^2}$; time derivative $\dot x = \frac{dx}{dt}$.
- Units: $[f'] = [f]/[x]$.
- Tangent line at $a$: $T_a(x) = f(a) + f'(a)(x - a)$.
- Linear-remainder form: $f(a + h) = f(a) + f'(a)h + r(h)$, $\ \lim_{h\to0} r(h)/h = 0$.
- MVT: $f \in C([a, b])$ differentiable on $(a, b)$ $\Rightarrow \exists c \in (a, b): f'(c)(b - a) = f(b) - f(a)$.
- Growth: $N' = rN \iff (\ln N)' = r$; reaction velocity of a product $v(t) = \frac{d[P]}{dt}$, initial velocity $v_0 = \frac{d[P]}{dt}\big|_{t = 0}$.

## Computational representation

Forward and central differences, applied to a growth curve and to $e^x$ at $x = 1$ (where the exact derivative is $e$):

```python
import math

def forward(f, x, h):
    return (f(x + h) - f(x)) / h          # slope of the secant on [x, x + h]

def central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)  # slope of the secant on [x - h, x + h]

# Toy culture (invented): N0 = 1000 cells/mL, doubling time 0.5 h
N0, r = 1000.0, math.log(2) / 0.5
N = lambda t: N0 * math.exp(r * t)
t = 2.0
print(f"N(2) = {N(t):.0f} cells/mL, exact dN/dt = r N = {r * N(t):.1f} cells/mL/h")
for h in (0.1, 0.01, 0.001):
    print(f"h = {h:<6} forward {forward(N, t, h):9.1f}  central {central(N, t, h):9.1f}")

# Step size: truncation error falls with h, rounding error grows as h shrinks
print(" h      forward error  central error   (f = exp, x = 1)")
for k in (1, 3, 5, 6, 8, 10, 12):
    h = 10.0 ** -k
    ef = abs(forward(math.exp, 1.0, h) - math.e)
    ec = abs(central(math.exp, 1.0, h) - math.e)
    print(f"1e-{k:02d}  {ef:.1e}        {ec:.1e}")
```

```text
N(2) = 16000 cells/mL, exact dN/dt = r N = 22180.7 cells/mL/h
h = 0.1    forward   23791.7  central   22251.8
h = 0.01   forward   22335.2  central   22181.4
h = 0.001  forward   22196.1  central   22180.7
 h      forward error  central error   (f = exp, x = 1)
1e-01  1.4e-01        4.5e-03
1e-03  1.4e-03        4.5e-07
1e-05  1.4e-05        5.9e-11
1e-06  1.4e-06        1.6e-10
1e-08  6.6e-09        6.6e-09
1e-10  1.5e-06        6.7e-07
1e-12  4.3e-04        2.1e-04
```

The forward error falls tenfold per tenfold smaller $h$ (order $h$), the central error a hundredfold (order $h^2$), until rounding takes over: below $h \approx 10^{-8}$ (forward) and $10^{-5}$ (central), smaller steps make the result worse.

## Worked example

> [!example] Initial velocity of a reaction (invented values)
> A first-order conversion $S \to P$ starting from 50 µM of $S$ gives $[P](t) = 50\,(1 - e^{-kt})$ µM, from the integrated first-order rate law $[S] = [S]_0 e^{-kt}$;[^chem12] take $k = 0.1\ \text{s}^{-1}$.
>
> 1. **Average rate over the first 10 s** (secant slope): $\frac{[P](10) - [P](0)}{10} = \frac{50(1 - e^{-1})}{10} = 3.16$ µM/s.
> 2. **Instantaneous rate at $t = 0$** from the definition: $\frac{[P](h) - [P](0)}{h} = 5 \cdot \frac{1 - e^{-0.1h}}{0.1h} \to 5$ µM/s, since $\frac{1 - e^{-u}}{u} \to 1$ as $u \to 0$.
> 3. **Numerical check**: secant slopes over shrinking intervals.
> ```python
> P = lambda t: 50 * (1 - math.exp(-0.1 * t))   # product concentration in uM, t in s (invented)
> for h in (10, 5, 1, 0.1, 0.01):
>     print(f"[0, {h}] s: average rate = {(P(h) - P(0)) / h:.4f} uM/s")
> ```
> ```text
> [0, 10] s: average rate = 3.1606 uM/s
> [0, 5] s: average rate = 3.9347 uM/s
> [0, 1] s: average rate = 4.7581 uM/s
> [0, 0.1] s: average rate = 4.9751 uM/s
> [0, 0.01] s: average rate = 4.9975 uM/s
> ```
> 4. **Velocity at any time.** The same computation at $t$ gives $\frac{d[P]}{dt} = 5\,e^{-0.1t}$ µM/s: 5 µM/s at the start, 1.84 µM/s at 10 s, falling as $S$ is consumed.
> 5. **Interpretation.** Reporting the 10 s average as the "initial velocity" would underestimate $v_0$ by 37 %. Initial rates are measured on the early, nearly straight part of the curve, where the secant is close to the tangent.

## Common misconceptions

> [!warning] "The derivative is the change of $f$"
> It is a rate: change per unit of $x$, with units. The change itself is approximately $f'(a)\,\Delta x$, and only for small $\Delta x$ ([[Linear Approximation]]).

> [!warning] "The average rate over an interval is the rate at its start"
> Only for a straight line. In the worked example the 10 s average is 37 % below the initial velocity, because the curve bends.

> [!warning] "Continuous means differentiable"
> $|x|$ is continuous with no derivative at 0. Piecewise models with thresholds have corners where the rate jumps.

> [!warning] "A smaller step always gives a better numerical derivative"
> Below about $10^{-8}$ (forward) or $10^{-5}$ (central), rounding error dominates and the estimate gets worse; on noisy data, small steps amplify the noise.

## Exercises

> [!question] Exercise 1 (L1)
> From the definition, compute $f'(2)$ for $f(x) = 3x^2 - x$, and write the tangent line at $x = 2$.

> [!success]- Solution
> $f(2) = 10$. $\frac{f(2 + h) - 10}{h} = \frac{3(4 + 4h + h^2) - 2 - h - 10}{h} = \frac{11h + 3h^2}{h} = 11 + 3h \to 11$. Tangent: $y = 10 + 11(x - 2)$.

> [!question] Exercise 2 (L1)
> From the definition, show that $\frac{d}{dx}\sqrt x = \frac{1}{2\sqrt x}$ for $x > 0$. What happens at $x = 0$?

> [!success]- Solution
> Multiply by the conjugate: $\frac{\sqrt{x + h} - \sqrt x}{h} = \frac{(x + h) - x}{h(\sqrt{x + h} + \sqrt x)} = \frac{1}{\sqrt{x + h} + \sqrt x} \to \frac{1}{2\sqrt x}$. At 0 the one-sided quotient is $\frac{\sqrt h}{h} = h^{-1/2} \to \infty$: a vertical tangent, no derivative.

> [!question] Exercise 3 (L1)
> $N(t)$ is a cell density in cells/mL, $t$ in hours, with $N(3) = 4 \times 10^5$ and $N'(3) = 2 \times 10^5$. Interpret both numbers, estimate $N(3.1)$, and give the specific growth rate and the doubling time it implies.

> [!success]- Solution
> At 3 h the culture holds $4 \times 10^5$ cells/mL and gains cells at $2 \times 10^5$ cells/mL per hour. Over the next 0.1 h, $N(3.1) \approx 4 \times 10^5 + 0.1 \times 2 \times 10^5 = 4.2 \times 10^5$ cells/mL. Specific rate $N'/N = 0.5$ per hour; if it stays constant, the doubling time is $\ln 2 / 0.5 \approx 1.39$ h.

> [!question] Exercise 4 (L2)
> Show that $f(x) = x|x|$ is differentiable at 0 although $|x|$ is not. What is $f'(0)$?

> [!success]- Solution
> $\frac{f(h) - f(0)}{h} = \frac{h|h|}{h} = |h| \to 0$ from both sides, so $f'(0) = 0$. Multiplying by $x$ flattens the corner: the product of a non-differentiable function and a function vanishing at the point can be differentiable.

> [!question] Exercise 5 (L2, Python)
> Invented plate-reader data: OD 0.050, 0.098, 0.190, 0.350, 0.580 at 0, 1, 2, 3, 4 h. Estimate the specific growth rate $\frac{d \ln N}{dt}$ at 1, 2 and 3 h by central differences of $\ln$ OD (OD taken proportional to $N$), and the corresponding doubling times. What does the trend suggest?

> [!success]- Solution
> ```python
> times = [0, 1, 2, 3, 4]                     # h (invented plate-reader data)
> od = [0.050, 0.098, 0.190, 0.350, 0.580]
> ln_od = [math.log(v) for v in od]
> for i in range(1, 4):
>     rate = (ln_od[i + 1] - ln_od[i - 1]) / (times[i + 1] - times[i - 1])
>     print(f"t = {times[i]} h: specific growth rate ~ {rate:.3f} per h, doubling time ~ {math.log(2) / rate:.2f} h")
> ```
>
> ```text
> t = 1 h: specific growth rate ~ 0.668 per h, doubling time ~ 1.04 h
> t = 2 h: specific growth rate ~ 0.636 per h, doubling time ~ 1.09 h
> t = 3 h: specific growth rate ~ 0.558 per h, doubling time ~ 1.24 h
> ```
>
> The per-capita rate falls over time: growth is slowing, as when a culture leaves the exponential phase and approaches its carrying capacity ([[Logistic Growth]]). With real, noisy data, fit a line to $\ln$ OD over a window instead of differencing single points (Advanced).

> [!question] Exercise 6 (L3)
> Model the total error of the forward difference as $E(h) = \frac{h}{2}M + \frac{2\varepsilon |f(x)|}{h}$, where $M$ bounds $|f''|$ near $x$. Find the step $h^*$ that minimizes $E$ and evaluate it for $f = \exp$ at $x = 1$. Compare with the table.

> [!success]- Solution
> $E'(h) = \frac{M}{2} - \frac{2\varepsilon|f|}{h^2} = 0$ gives $h^* = 2\sqrt{\varepsilon|f|/M}$. For $\exp$ at 1, $|f| = M = e$, so $h^* = 2\sqrt{\varepsilon} \approx 3 \times 10^{-8}$ and $E(h^*) = 2e\sqrt{\varepsilon} \approx 8 \times 10^{-8}$. The table's best forward error, $6.6 \times 10^{-9}$ at $h = 10^{-8}$, is in that region and below the bound: rounding errors partly cancel in practice, but the location of the optimum, near $\sqrt\varepsilon$, is what matters.

## Mastery checklist

- [ ] 1 Recognized: I can write the limit definition of $f'(a)$ and read $\frac{dN}{dt}$ and $\frac{d[P]}{dt}$ as rates with units.
- [ ] 2 Understood: I can explain secant versus tangent, average versus instantaneous rate, and why differentiability implies continuity but not the converse.
- [ ] 3 Practiced: I differentiate polynomials, $1/x$, $\sqrt x$ and $e^{rt}$ from the definition, and compute forward and central differences in Python.
- [ ] 4 Applied: I estimate a specific growth rate or an initial reaction velocity from real time-course data and justify the window I use.
- [ ] 5 Explained: I can teach the mean value theorem and its consequences, and the trade-off between truncation, rounding and noise in numerical derivatives.

## References

[^calc1]: [[Calculus (OpenStax)]], Volume 1 (derivatives: secant and tangent slopes, the limit definition, the derivative as a function and as a rate of change, differentiability and continuity, higher derivatives; the mean value theorem).
[^1801]: [[MIT 18.01SC - Single Variable Calculus]], differentiation part (definition of the derivative, rates of change).
[^chem12]: [[Chemistry 2e (OpenStax)]], ch. 12 "Kinetics" (reaction rates as changes in concentration per unit time, instantaneous rate as the slope of the tangent to the concentration-time curve, integrated first-order rate law).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of enzyme kinetics (initial velocity, Michaelis-Menten model).
[^micro]: [[Microbiology (OpenStax)]], treatment of microbial growth (exponential growth phase and generation time).
