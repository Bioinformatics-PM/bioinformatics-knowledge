---
aliases:
  - Complex Numbers
  - Imaginary Unit
  - Polar Form
  - Euler's Formula
  - Nombre complexe
tags:
  - type/concept
  - domain/mathematics
  - domain/physics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Exponential Function]]"
  - "[[Taylor Series]]"
  - "[[Function]]"
related:
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Second-Order Linear Differential Equation]]"
  - "[[System of Differential Equations]]"
  - "[[Phase Portrait]]"
  - "[[Lotka-Volterra Model]]"
  - "[[Limit Cycle]]"
  - "[[Fast Fourier Transform]]"
  - "[[Harmonic Oscillator]]"
  - "[[Boolean Algebra]]"
projects: []
sources:
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[Calculus (OpenStax)]]"
  - "[[Nonlinear Dynamics and Chaos (Strogatz)]]"
  - "[[Mathematical Biology (Murray)]]"
  - "[[Spellman 1998 - Comprehensive Identification of Cell Cycle-Regulated Genes of the Yeast Saccharomyces cerevisiae]]"
  - "[[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Python Documentation]]"
---

# Complex Number

> [!abstract]
> A complex number $a + bi$ extends the real line to a plane by adding a number $i$ with $i^2 = -1$; in polar form, multiplying complex numbers rotates and scales them, and Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ turns oscillations into exponentials, which is how eigenvalues reveal oscillating gene circuits and how the Fourier transform finds periodic signals.

## Definition

A **complex number** is $z = a + bi$, with $a, b$ real and $i$ the **imaginary unit**, $i^2 = -1$; $a = \operatorname{Re} z$ is its real part and $b = \operatorname{Im} z$ its imaginary part. Complex numbers are added and multiplied with the usual rules of algebra, replacing $i^2$ by $-1$, and are drawn as points $(a, b)$ of the **complex plane**. In **polar form**, $z = r(\cos\theta + i\sin\theta) = r e^{i\theta}$, where $r = |z| = \sqrt{a^2 + b^2}$ is the **modulus**, $\theta = \arg z$ the **argument**, and **Euler's formula** $e^{i\theta} = \cos\theta + i\sin\theta$ links the two writings.[^1803]

## Why it matters

- **Oscillations in models.** Solutions of linear(ized) dynamical models are built from $e^{\lambda t}$. A complex eigenvalue $\lambda = \alpha + i\omega$ means an oscillation of angular frequency $\omega$ whose amplitude decays ($\alpha < 0$) or grows ($\alpha > 0$): this is how stability analysis reads damped oscillations of gene circuits and predator-prey cycles ([[Eigenvalues and Eigenvectors]], [[Phase Portrait]], [[Lotka-Volterra Model]]).[^1803u4][^strogatz]
- **Second-order equations.** A damped oscillator, chemical or mechanical, oscillates exactly when its characteristic equation has complex roots ([[Second-Order Linear Differential Equation]], [[Harmonic Oscillator]]).[^1803u2]
- **Fourier analysis.** The discrete Fourier transform writes a sampled signal as a sum of complex exponentials: the modulus of a coefficient says how strong a period is, its argument says when the signal peaks. The classic microarray screen for cell-cycle genes in yeast scored periodicity with a Fourier algorithm.[^spellman]
- **Computing.** `complex` is a built-in numeric type of Python and `cmath` its math module;[^python] eigenvalue routines return complex numbers for real matrices (code below).

## Core (L2)

### Arithmetic

$$(a + bi) + (c + di) = (a + c) + (b + d)i, \qquad (a + bi)(c + di) = (ac - bd) + (ad + bc)i.$$

The **conjugate** $\bar z = a - bi$ satisfies $z\bar z = a^2 + b^2 = |z|^2$, a nonnegative real number. Division multiplies by the conjugate of the denominator: $\frac{z}{w} = \frac{z\bar w}{|w|^2}$, for instance $\frac{3 + 2i}{1 - i} = \frac{(3 + 2i)(1 + i)}{2} = \frac{1 + 5i}{2}$.

Quadratics always have roots: $x^2 + 2x + 5 = 0$ gives $x = \frac{-2 \pm \sqrt{-16}}{2} = -1 \pm 2i$. For a polynomial $p$ with real coefficients, $\overline{p(z)} = p(\bar z)$, so non-real roots come in **conjugate pairs**.

### The plane and the polar form

![[complex-plane-polar-form.svg]]

- The modulus $r = \sqrt{a^2 + b^2}$ is the distance to 0; the argument $\theta$ is the angle from the positive real axis, computed with the two-argument arctangent $\operatorname{atan2}(b, a)$, which handles the quadrants.[^1803]
- **Multiplication rotates and scales**: $r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2\, e^{i(\theta_1 + \theta_2)}$. Moduli multiply, arguments add (panel B). Multiplying by $i = e^{i\pi/2}$ is a quarter turn.
- **Powers** follow: $(r e^{i\theta})^n = r^n e^{in\theta}$ (de Moivre). Example: $1 + i = \sqrt 2\, e^{i\pi/4}$, so $(1 + i)^8 = 16\, e^{2\pi i} = 16$.

### Euler's formula

Put $x = i\theta$ into the series $e^x = \sum_{k \ge 0} x^k/k!$ ([[Taylor Series]]). The powers of $i$ cycle through $1, i, -1, -i$, so the even terms rebuild the series of $\cos\theta$ and the odd terms $i$ times that of $\sin\theta$:[^os2][^1803]

$$e^{i\theta} = \Big(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\Big) + i\Big(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\Big) = \cos\theta + i\sin\theta.$$

Consequences: $|e^{i\theta}| = \sqrt{\cos^2\theta + \sin^2\theta} = 1$, so $e^{i\theta}$ runs around the unit circle; $e^{i\pi} = -1$; $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$ and $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$. Most important for models:

$$e^{(\alpha + i\omega)t} = e^{\alpha t}(\cos\omega t + i\sin\omega t):$$

the real part $\alpha$ sets growth or decay, the imaginary part $\omega$ sets the rotation, with period $2\pi/\omega$.

### Bio: complex eigenvalues signal oscillations

For a linear system $\mathbf{x}' = A\mathbf{x}$ with a real $2 \times 2$ matrix $A$, the eigenvalues solve $\lambda^2 - (\operatorname{tr} A)\lambda + \det A = 0$ ([[Eigenvalues and Eigenvectors]]). They are complex exactly when $(\operatorname{tr} A)^2 < 4\det A$, and then $\lambda = \alpha \pm i\omega$ with $\alpha = \frac{\operatorname{tr} A}{2}$ and $\omega = \sqrt{\det A - \alpha^2}$. Real solutions combine $e^{\alpha t}\cos\omega t$ and $e^{\alpha t}\sin\omega t$: trajectories spiral in ($\alpha < 0$), spiral out ($\alpha > 0$) or circle ($\alpha = 0$, a center).[^1803u4][^strogatz]

- **Negative feedback in a gene circuit** (linearized, invented): deviations $m$ of an mRNA and $p$ of its protein from steady state, with the protein repressing its own transcription, obey $m' = -\gamma_m m - kp$, $p' = \beta m - \gamma_p p$ ($\gamma$: decay rates, $\beta$: translation, $k$: repression strength). Here $\operatorname{tr} A = -(\gamma_m + \gamma_p)$ and $\det A = \gamma_m\gamma_p + k\beta$, so the eigenvalues are complex exactly when $(\gamma_m - \gamma_p)^2 < 4k\beta$: strong enough feedback produces overshoot and oscillation. Since $\alpha = -(\gamma_m + \gamma_p)/2 < 0$, the oscillation is always damped in this two-variable linear model; sustained oscillators need nonlinearity and are [[Limit Cycle|limit cycles]].
- **Predator-prey cycles.** The Lotka-Volterra model $x' = ax - bxy$ (prey), $y' = -cy + dxy$ (predators), with positive constants, has a coexistence equilibrium $(c/d, a/b)$.[^murray] Linearized there ([[Jacobian Matrix]]), it gives $A = \begin{pmatrix} 0 & -bc/d \\ ad/b & 0 \end{pmatrix}$, with trace 0 and determinant $ac$, hence $\lambda = \pm i\sqrt{ac}$: small oscillations with period $2\pi/\sqrt{ac}$ (Exercises 4 and 5).

### Bio: the Fourier transform finds periodic genes

For samples $x_0, \dots, x_{N-1}$ taken at equal time steps, the **discrete Fourier transform** (DFT) is

$$X_k = \sum_{n=0}^{N-1} x_n\, e^{-2\pi i k n/N}, \qquad k = 0, \dots, N - 1.$$

$X_k$ compares the series with a cosine and a sine making $k$ full cycles over the $N$ samples. If $x_n = m + A\cos(2\pi kn/N - \varphi)$ with $0 < k < N/2$, then $X_k = \frac{NA}{2}e^{-i\varphi}$ (Advanced): the modulus gives the amplitude $A = 2|X_k|/N$ and the argument the phase, hence the peak time. In the yeast cell-cycle study, a periodicity score derived from a Fourier algorithm, together with a correlation criterion, identified 800 cell cycle-regulated genes.[^spellman] The code below applies the same idea to an invented time course: 12 samples 10 min apart cover two 60-min cycles, so the cell-cycle signal sits at $k = 2$.

## Advanced (L3)

- **Roots of unity.** The $N$ numbers $\omega_N^n = e^{2\pi i n/N}$ are equally spaced on the unit circle. For an integer $k$ not divisible by $N$, $\sum_{n=0}^{N-1} \omega_N^{kn} = \frac{1 - \omega_N^{kN}}{1 - \omega_N^k} = 0$ (geometric series). This orthogonality inverts the DFT, $x_n = \frac{1}{N}\sum_k X_k e^{2\pi i kn/N}$, and proves the amplitude formula above: in $x_n = m + \frac{A}{2}(e^{i(2\pi kn/N - \varphi)} + e^{-i(2\pi kn/N - \varphi)})$, only one term survives the sum defining $X_k$.
- **The Fourier matrix and the FFT.** The DFT is multiplication by the matrix $F_{kn} = \omega_N^{-kn}$, whose columns are the eigenvectors of every circulant matrix.[^18065] Computing it from the definition costs $O(N^2)$; the fast Fourier transform splits even and odd samples, using $\omega_N^2 = \omega_{N/2}$, and needs $O(N \log N)$ operations ([[Fast Fourier Transform]]).[^cormen]
- **Real signals and sampling.** For real $x$, $X_{N-k} = \overline{X_k}$, so only $k \le N/2$ carry information: a series sampled every 10 min cannot resolve periods shorter than 20 min.
- **$\mathbb{C}$ as rotation-scaling matrices.** $a + bi \mapsto \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ turns complex multiplication into matrix multiplication. Conversely, if a real $2 \times 2$ matrix has the eigenvalue $\alpha + i\omega$ ($\omega > 0$) with eigenvector $\mathbf{v} = \mathbf{u} + i\mathbf{w}$, then $A\mathbf{u} = \alpha\mathbf{u} - \omega\mathbf{w}$ and $A\mathbf{w} = \omega\mathbf{u} + \alpha\mathbf{w}$: in the basis $(\mathbf{w}, \mathbf{u})$, $A$ acts as $\begin{pmatrix} \alpha & -\omega \\ \omega & \alpha \end{pmatrix}$, a rotation combined with a scaling. This is why trajectories spiral.
- **Linearization is not the last word.** Purely imaginary eigenvalues of a linearization do not by themselves prove closed orbits of the nonlinear model; for Lotka-Volterra a conserved quantity does ([[Multivariable Chain Rule]]).[^strogatz]

## Mathematical representation

- $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$, identified with $\mathbb{R}^2$; it is a field: each $z \neq 0$ has the inverse $z^{-1} = \bar z/|z|^2$.
- $|zw| = |z|\,|w|$, $\arg(zw) = \arg z + \arg w \pmod{2\pi}$, $z + \bar z = 2\operatorname{Re} z$, $z - \bar z = 2i\operatorname{Im} z$.
- For $z = x + iy$: $e^z = e^x(\cos y + i\sin y)$, and $e^{z + w} = e^z e^w$.
- Eigenvalues of $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$: $\lambda = \frac{\operatorname{tr} A \pm \sqrt{(\operatorname{tr} A)^2 - 4\det A}}{2}$, with $\operatorname{tr} A = a + d$ and $\det A = ad - bc$.
- DFT and inverse: $X_k = \sum_{n} x_n \omega_N^{-kn}$, $x_n = \frac{1}{N}\sum_k X_k \omega_N^{kn}$, with $\omega_N = e^{2\pi i/N}$.

## Computational representation

Python writes $i$ as `j`; `abs`, `.conjugate()` and the `cmath` functions cover the operations above:[^python]

```python
import cmath
import math

z, w = 3 + 2j, 1 - 1j                       # Python writes i as j
print(z * w, z / w, z.conjugate(), abs(z))
r, theta = cmath.polar(z)                   # modulus and argument (radians)
print(round(r, 4), round(math.degrees(theta), 2), cmath.rect(r, theta))
print(cmath.exp(1j * math.pi))              # Euler: e^(i pi) = -1, up to rounding


def eigenvalues_2x2(a, b, c, d):
    """Eigenvalues of [[a, b], [c, d]]: roots of l^2 - (a + d) l + (ad - bc) = 0."""
    tr, det = a + d, a * d - b * c
    root = cmath.sqrt(tr * tr - 4 * det)    # imaginary when tr^2 < 4 det
    return (tr + root) / 2, (tr - root) / 2


lam = eigenvalues_2x2(-1, -4, 1, -1)        # feedback loop of the worked example
print(lam, round(2 * math.pi / lam[0].imag, 4))

# Invented expression time course: 12 samples, one every 10 min; cell cycle of 60 min
x = [1.85, 2.45, 2.35, 1.80, 1.15, 1.25, 1.75, 2.40, 2.45, 1.85, 1.20, 1.15]


def dft(x):
    """X_k = sum_n x_n e^(-2 pi i k n / N), straight from the definition: O(N^2)."""
    N = len(x)
    return [sum(x[n] * cmath.exp(-2j * math.pi * k * n / N) for n in range(N))
            for k in range(N)]


X = dft(x)
print([round(abs(Xk), 2) for Xk in X[:7]])
k = 2                                       # 12 x 10 min = 120 min = 2 cycles
amplitude = 2 * abs(X[k]) / len(x)
peak = (-cmath.phase(X[k]) / (2 * math.pi) * 60) % 60    # minutes after t = 0
print(round(amplitude, 3), round(peak, 1))

import numpy as np

print(np.allclose(X, np.fft.fft(x)), np.linalg.eigvals(np.array([[-1.0, -4.0], [1.0, -1.0]])))
```

```text
(5-1j) (0.5+2.5j) (3-2j) 3.605551275463989
3.6056 33.69 (3+1.9999999999999996j)
(-1+1.2246467991473532e-16j)
((-1+2j), (-1-2j)) 3.1416
[21.65, 0.11, 4.24, 0.25, 0.05, 0.19, 0.15]
0.707 15.0
True [-1.+2.j -1.-2.j]
```

$|X_0| = 21.65$ is $N$ times the mean; among the other frequencies, $k = 2$ (period 60 min) dominates, with amplitude 0.71 and a peak 15 min after the first sample. The rounding residue in $e^{i\pi}$ and in `rect` is [[Floating-Point Arithmetic]], not mathematics.

## Worked example

> [!example] Does a negative feedback loop oscillate? (invented, linearized)
> Deviations from steady state: $m' = -m - 4p$ and $p' = m - p$ (time in units of the mRNA lifetime), so $A = \begin{pmatrix} -1 & -4 \\ 1 & -1 \end{pmatrix}$.
> 1. **Trace and determinant**: $\operatorname{tr} A = -2$, $\det A = (-1)(-1) - (-4)(1) = 5$.
> 2. **Discriminant**: $(\operatorname{tr} A)^2 - 4\det A = 4 - 20 = -16 < 0$, so the eigenvalues are complex.
> 3. **Eigenvalues**: $\lambda = \frac{-2 \pm \sqrt{-16}}{2} = -1 \pm 2i$; `eigenvalues_2x2(-1, -4, 1, -1)` and NumPy agree.
> 4. **Solutions**: by Euler's formula, $m(t) = e^{-t}(c_1\cos 2t + c_2\sin 2t)$, and likewise $p(t)$.
> 5. **Read it**: angular frequency $\omega = 2$, so the period is $2\pi/2 = \pi \approx 3.14$ time units. Over one period the envelope shrinks by $e^{-\pi} \approx 0.043$: one visible overshoot, then the system settles. Feedback strong enough to make the discriminant negative creates the oscillation; the negative real part damps it.

## Common misconceptions

> [!warning] "Imaginary numbers cannot describe anything real"
> A real system with complex eigenvalues has real solutions: the conjugate pair combines as $e^{(\alpha + i\omega)t} + e^{(\alpha - i\omega)t} = 2e^{\alpha t}\cos\omega t$. The imaginary part is a bookkeeping device for rotation and oscillation.

> [!warning] "$\arg z = \arctan(b/a)$"
> Only when $a > 0$. For $z = -1 + i$, $\arctan(-1) = -45°$, but the argument is $135°$. Use $\operatorname{atan2}(b, a)$, which `cmath.phase` implements.

> [!warning] "Complex eigenvalues mean sustained oscillations"
> They mean rotation, damped when $\alpha < 0$ (the worked example), growing when $\alpha > 0$. Sustained oscillations need $\alpha = 0$ exactly or, robustly, a [[Limit Cycle]] of a nonlinear model.

> [!warning] "A large Fourier coefficient proves that a gene is periodic"
> Noise, trends and a few extreme samples also produce large coefficients, and the frequency grid depends on the sampling. Compare the score with the scores of shuffled time courses before calling a gene periodic.

## Exercises

> [!question] Exercise 1 (L2)
> Compute $(2 + 3i)(1 - i)$, $\frac{2 + 3i}{1 - i}$, $|2 + 3i|$ and $\arg(2 + 3i)$ by hand, then check in Python.

> [!success]- Solution
> $(2 + 3i)(1 - i) = 2 - 2i + 3i - 3i^2 = 5 + i$. $\frac{2 + 3i}{1 - i} = \frac{(2 + 3i)(1 + i)}{2} = \frac{-1 + 5i}{2}$. $|2 + 3i| = \sqrt{13} \approx 3.606$, and $\arg = \arctan(3/2) \approx 56.31°$ (here $a > 0$).
> ```python
> print((2 + 3j) * (1 - 1j), (2 + 3j) / (1 - 1j), abs(2 + 3j), round(math.degrees(cmath.phase(2 + 3j)), 2))
> ```
> Output: `(5+1j) (-0.5+2.5j) 3.605551275463989 56.31`.

> [!question] Exercise 2 (L2)
> Compute $(1 + i)^8$ in polar form, then $(1 + i)^{8}$ in Python. What do the eight values $e^{2\pi i n/8}$, $n = 0, \dots, 7$, look like in the plane?

> [!success]- Solution
> $1 + i = \sqrt 2\, e^{i\pi/4}$, so $(1 + i)^8 = (\sqrt 2)^8 e^{2\pi i} = 16$; Python prints `(16+0j)` for `(1 + 1j) ** 8`. The eight values are the 8th roots of unity: the vertices of a regular octagon on the unit circle, 45° apart.

> [!question] Exercise 3 (L2)
> Using $e^{i(a + b)} = e^{ia}e^{ib}$ and Euler's formula, derive the formulas for $\cos(a + b)$ and $\sin(a + b)$.

> [!success]- Solution
> $e^{ia}e^{ib} = (\cos a + i\sin a)(\cos b + i\sin b) = (\cos a\cos b - \sin a\sin b) + i(\sin a\cos b + \cos a\sin b)$. Compare real and imaginary parts with $e^{i(a + b)} = \cos(a + b) + i\sin(a + b)$: $\cos(a + b) = \cos a\cos b - \sin a\sin b$ and $\sin(a + b) = \sin a\cos b + \cos a\sin b$. Two identities from one rule of exponents.

> [!question] Exercise 4 (L2)
> Lotka-Volterra with invented rates per month: $a = 1.0$, $b = 0.1$, $c = 0.5$, $d = 0.02$. Find the coexistence equilibrium, the eigenvalues of the linearization and the period of small cycles.

> [!success]- Solution
> Equilibrium $(c/d, a/b) = (25, 10)$. Linearization $\begin{pmatrix} 0 & -bc/d \\ ad/b & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2.5 \\ 0.2 & 0 \end{pmatrix}$: trace 0, determinant $0.5 = ac$, so $\lambda = \pm i\sqrt{0.5} \approx \pm 0.707i$. Period $2\pi/0.707 \approx 8.89$ months, with predators lagging a quarter cycle behind prey.

> [!question] Exercise 5 (L3, Python)
> Simulate the model of Exercise 4 with a Runge-Kutta scheme from $(25, 9)$ and from $(25, 2)$, and measure the period between upward crossings of $x = 25$. Compare with $2\pi/\sqrt{ac}$.

> [!success]- Solution
> ```python
> def lotka_volterra(x, y, a=1.0, b=0.1, c=0.5, d=0.02):
>     return a * x - b * x * y, -c * y + d * x * y
>
>
> def period(x, y, dt=0.001, t_max=100.0):
>     """Time between two successive upward crossings of the prey equilibrium x* = c/d = 25 (RK4)."""
>     x_star, crossings, t = 25.0, [], 0.0
>     while t < t_max and len(crossings) < 2:
>         k1 = lotka_volterra(x, y)
>         k2 = lotka_volterra(x + dt / 2 * k1[0], y + dt / 2 * k1[1])
>         k3 = lotka_volterra(x + dt / 2 * k2[0], y + dt / 2 * k2[1])
>         k4 = lotka_volterra(x + dt * k3[0], y + dt * k3[1])
>         nx = x + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
>         ny = y + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
>         if x < x_star <= nx:
>             crossings.append(t + dt * (x_star - x) / (nx - x))
>         x, y, t = nx, ny, t + dt
>     return crossings[1] - crossings[0]
>
>
> print(round(2 * math.pi / math.sqrt(1.0 * 0.5), 3), round(period(25.0, 9.0), 3), round(period(25.0, 2.0), 3))
> ```
> Output: `8.886 8.898 10.757`. Near the equilibrium the linear prediction is accurate to 0.1 %; far from it, the nonlinear cycle is about 20 % slower. Eigenvalues describe small oscillations only.

> [!question] Exercise 6 (L3, Python)
> Prove that the 12th roots of unity sum to 0 and that $X_{N-k} = \overline{X_k}$ for a real series. Check both on `X` from the code above.

> [!success]- Solution
> The roots form a geometric series of ratio $\omega_{12} \ne 1$ with $\omega_{12}^{12} = 1$: $\sum_{n=0}^{11}\omega_{12}^n = \frac{1 - \omega_{12}^{12}}{1 - \omega_{12}} = 0$. For real $x_n$, $\overline{X_k} = \sum_n x_n e^{2\pi i kn/N} = \sum_n x_n e^{-2\pi i (N - k)n/N} = X_{N-k}$, because $e^{-2\pi i n} = 1$.
> ```python
> N = 12
> roots = [cmath.exp(2j * math.pi * n / N) for n in range(N)]
> print(abs(sum(roots)) < 1e-12, all(abs(X[N - k] - X[k].conjugate()) < 1e-12 for k in range(1, N)))
> ```
> Output: `True True`.

## Mastery checklist

- [ ] 1 Recognized: I can write $z = a + bi$ in polar form and state Euler's formula.
- [ ] 2 Understood: I can explain why multiplication rotates and scales, why complex eigenvalues mean oscillation, and what the modulus and argument of a Fourier coefficient measure.
- [ ] 3 Practiced: I compute with complex numbers by hand and in Python, find the eigenvalues of a $2 \times 2$ system and implement the DFT from its definition.
- [ ] 4 Applied: I scored the periodicity and peak time of real time-course expression data (for example the yeast cell-cycle series) with the DFT, and checked the oscillation period of a published model against its eigenvalues.
- [ ] 5 Explained: I can teach roots of unity, why the FFT is fast, the sampling limit $k \le N/2$, and why linearization alone cannot prove sustained oscillations.

## References

[^1803]: [[MIT 18.03SC - Differential Equations]], Unit I session "Complex Arithmetic and Exponentials" (complex arithmetic, Euler's formula and its justification, polar form, $n$-th roots).
[^1803u2]: [[MIT 18.03SC - Differential Equations]], Unit II "Second Order Constant Coefficient Linear Equations" (characteristic equation, complex roots, oscillating solutions).
[^1803u4]: [[MIT 18.03SC - Differential Equations]], Unit IV "First Order Systems" (autonomous $2 \times 2$ linear systems, eigenvalues and phase portraits).
[^os2]: [[Calculus (OpenStax)]], Volume 2, power series (Maclaurin series of $e^x$, $\sin x$ and $\cos x$).
[^strogatz]: [[Nonlinear Dynamics and Chaos (Strogatz)]], 3rd ed., two-dimensional flows (linear systems and their classification, phase plane analysis, limit cycles).
[^murray]: [[Mathematical Biology (Murray)]], 3rd ed., Volume I, population models (predator-prey interactions, the Lotka-Volterra system).
[^spellman]: [[Spellman 1998 - Comprehensive Identification of Cell Cycle-Regulated Genes of the Yeast Saccharomyces cerevisiae]], *Molecular Biology of the Cell* 9(12):3273-3297: periodicity score from a Fourier algorithm, correlation criterion, 800 cell cycle-regulated genes.
[^18065]: [[MIT 18.065 - Matrix Methods in Data Analysis, Signal Processing, and Machine Learning]], lecture "Eigenvectors of Circulant Matrices: Fourier Matrix".
[^cormen]: [[Introduction to Algorithms (Cormen)]], 4th ed., treatment of polynomials and the FFT (complex roots of unity, the DFT, the $\Theta(n \lg n)$ FFT).
[^python]: [[Python Documentation]], 3.13, Library Reference: numeric types (`complex`, imaginary literals with `j`) and the `cmath` module.
