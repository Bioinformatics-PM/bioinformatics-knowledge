---
aliases:
  - Molecular Diffusion
  - Diffusion Coefficient
  - Diffusivity
  - Diffusion moléculaire
  - Coefficient de diffusion
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Order-of-Magnitude Estimation]]"
  - "[[Variance]]"
  - "[[Normal Distribution]]"
  - "[[Temperature]]"
  - "[[Molar Concentration]]"
related:
  - "[[Brownian Motion]]"
  - "[[Random Walk]]"
  - "[[Fick's Law]]"
  - "[[Stokes-Einstein Relation]]"
  - "[[Diffusion-Limited Reaction]]"
  - "[[Cell Membrane]]"
  - "[[Membrane Transport]]"
  - "[[Molecular Motor]]"
  - "[[Neuron]]"
  - "[[Central Limit Theorem]]"
  - "[[Membrane Potential]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Diffusion

> [!abstract]
> Diffusion is the spreading of molecules by their random thermal motion: each molecule wanders without direction, and the distance it covers grows only as the square root of time, so a protein crosses a bacterium in a fraction of a second but would need centuries to travel along a one-metre axon.

## Definition

**Diffusion** is the net transport of molecules from regions of high to low concentration that results from the random thermal motion of each molecule. For one molecule moving in one dimension, the mean squared displacement grows linearly with time,

$$\langle x^2(t) \rangle = 2Dt,$$

which defines the **diffusion coefficient** $D$, in m² s⁻¹ (in cell biology usually µm² s⁻¹).[^pboc] In $d$ dimensions, $\langle r^2 \rangle = 2dDt$ (Mathematical representation).

## Why it matters

- **Timescales of the cell.** How fast a signal crosses a cell, a transcription factor finds its site or a substrate meets its enzyme is set by $x^2/D$ ([[Diffusion-Limited Reaction]], [[Transcription Factor]]).
- **Measurements.** Fluorescence recovery after photobleaching and single-particle tracking report D values; reading them requires the mean squared displacement relation and its dimensional factor ([[Cell Membrane]], [[Fluorescence Microscopy]]).
- **Simulation.** Brownian dynamics and [[Molecular Dynamics Simulation|molecular dynamics]] estimate D from the slope of the mean squared displacement of simulated trajectories (Exercise 4 uses the same estimator).
- **Cell design.** Diffusion over long distances is slow, so large cells and neurons need active transport ([[Molecular Motor]]), while small bacteria can rely on diffusion ([[Cell]]).

## Core (L1)

### Thermal motion as a random walk

A molecule in water is hit by solvent molecules all the time; each collision changes its direction, so its path is a random walk with no preferred direction.[^pboc] The simplest model, in one dimension: every $\tau$ seconds the molecule steps $+a$ or $-a$ with probability 1/2, independently of earlier steps. After $N = t/\tau$ steps its position is $x = s_1 + \dots + s_N$.

- **Mean**: $\langle x \rangle = \sum_i \langle s_i \rangle = 0$. No net drift.
- **Mean square**: $\langle x^2 \rangle = \sum_i \langle s_i^2 \rangle + \sum_{i \ne j} \langle s_i s_j \rangle = N a^2 + 0$, because independent steps of mean zero have $\langle s_i s_j \rangle = \langle s_i \rangle \langle s_j \rangle = 0$ ([[Variance]] of a sum of independent variables).
- Hence $\langle x^2 \rangle = (a^2/\tau)\,t = 2Dt$ with $D = a^2/(2\tau)$.

The typical distance is $x_\text{rms} = \sqrt{2Dt}$: going 10 times farther takes 100 times longer. Inverted, the time to diffuse a distance $x$ is

$$t \approx \frac{x^2}{2D}.$$

![[random-walk-mean-squared-displacement.svg]]

### From one molecule to a population

No molecule "knows" where the concentration is high. But if more molecules sit to the left of a plane than to its right, and each crosses in either direction with equal probability, more cross from left to right than back: a **net flux down the concentration gradient** appears from unbiased individual motion. When the concentration is uniform, molecules keep moving but the net flux is zero.[^pboc] The quantitative form is [[Fick's Law]].

### Typical diffusion coefficients

| Molecule and medium | D (µm²/s) | D (m²/s) |
|---|---:|---:|
| Small molecule in water | ~1000 | ~10⁻⁹ |
| Protein in water | ~100 | ~10⁻¹⁰ |
| Protein in bacterial cytoplasm | ~10 | ~10⁻¹¹ |
| Lipid in a bilayer (two dimensions) | ~1 | ~10⁻¹² |

The first three are rounded values from *Physical Biology of the Cell*;[^pboc] the lipid value is $10^{-8}$ cm²/s.[^alberts] The crowded cytoplasm slows a protein about tenfold compared with water.[^pboc] Unit identity: 1 µm²/s = 10⁻¹² m²/s = 10⁻⁸ cm²/s.

### Fast across a bacterium, hopeless along an axon

With $t = x^2/2D$ (computed below):

| Distance | Small molecule, D = 1000 µm²/s | Protein in cytoplasm, D = 10 µm²/s |
|---|---:|---:|
| 1 µm (across a bacterium) | 0.5 ms | 50 ms |
| 10 µm (across a eukaryotic cell) | 50 ms | 5 s |
| 1 mm | 8 min | 14 h |
| 1 m (an assumed axon length, the scale of a human limb) | 16 years | 1600 years |

Inside a bacterium, diffusion mixes everything in milliseconds. A protein made in the cell body of a [[Neuron]] would never reach the end of a long axon by diffusion: neurons carry cargo along microtubules with motor proteins ([[Molecular Motor]]).[^alberts] The quadratic law is the whole story: a distance $10^6$ times longer costs $10^{12}$ times more time.

## Deeper (L2)

### The diffusion equation and its Gaussian solution

Let $P(x, t)$ be the probability that the walker is at $x$ at time $t$. One step earlier it was at $x - a$ or $x + a$:

$$P(x, t + \tau) = \tfrac{1}{2} P(x - a, t) + \tfrac{1}{2} P(x + a, t).$$

Expanding to first order in $\tau$ and second order in $a$, $P + \tau\,\partial_t P = P + \tfrac{a^2}{2}\,\partial_x^2 P$, so

$$\frac{\partial P}{\partial t} = D\,\frac{\partial^2 P}{\partial x^2}, \qquad D = \frac{a^2}{2\tau},$$

the same $D$ as before. For a walker starting at the origin the solution is

$$P(x, t) = \frac{1}{\sqrt{4\pi D t}}\, \exp\!\Big(-\frac{x^2}{4Dt}\Big),$$

a [[Normal Distribution]] of mean 0 and variance $2Dt$. This also follows from the [[Central Limit Theorem]], since $x$ is a sum of many independent steps. About 68 % of the walkers lie within $\pm\sqrt{2Dt}$. A concentration profile obeys the same equation (Fick's second law), solved in simple geometries in [[Fick's Law]].

### One, two, three dimensions

The coordinates move independently, so $\langle r^2 \rangle = \langle x^2 \rangle + \langle y^2 \rangle + \langle z^2 \rangle = 2dDt$: $4Dt$ for lateral diffusion in a membrane ([[Cell Membrane]]), $6Dt$ in a volume. The time to reach a root-mean-square 3D distance $R$ is $R^2/6D$, three times shorter than the 1D formula; order-of-magnitude reasoning often drops the factor and writes $t \sim x^2/D$.

### Thermal speed versus net progress

Equipartition gives each velocity component $\tfrac{1}{2} m \langle v_x^2 \rangle = \tfrac{1}{2} k_B T$ ([[Equipartition Theorem]]).[^up] For a 30 kDa protein ($m = 5.0 \times 10^{-23}$ kg) at 37 °C, with $k_B = 1.380\,649 \times 10^{-23}$ J K⁻¹,[^nist] $v_{x,\text{rms}} = \sqrt{k_B T / m} \approx 9$ m/s: moving straight, it would cross a bacterium in 0.1 µs. Collisions erase the velocity instead. The Einstein relation links D to the friction coefficient $\zeta$ of the molecule, $D = k_B T / \zeta$,[^pboc] and a velocity decays in a time $m/\zeta = mD/k_BT \approx 10^{-13}$ s (with $D = 10$ µm²/s). Each "step" is therefore about $v\,\tau_v \approx 10^{-12}$ m, a hundredth of an ångström: diffusion is a walk of an enormous number of tiny steps, which is why the Gaussian limit holds so well. For a sphere, $\zeta$ comes from Stokes' drag ([[Stokes-Einstein Relation]]).

### Diffusion versus directed transport

A motor moving at speed $v$ covers $x$ in $x/v$; diffusion needs $x^2/2D$. The two are equal at the crossover length

$$x^* = \frac{2D}{v}.$$

With $D = 10$ µm²/s and an assumed speed $v = 1$ µm/s, $x^* = 20$ µm: below a few tens of micrometres diffusion wins, beyond it directed transport wins, and the advantage grows linearly with distance. A large cargo such as a vesicle diffuses more slowly ($D \propto 1/r$ by [[Stokes-Einstein Relation|Stokes-Einstein]]), so a vesicle ten times larger in radius has $D = 1$ µm²/s and $x^* = 2$ µm: large cargoes need motors even inside an ordinary cell.

## Advanced (L3)

### Measuring D from trajectories

Single-particle tracking records positions $\mathbf{r}(t_k)$. The **time-averaged mean squared displacement** at lag $\Delta = k\tau$ averages over all start times of one trajectory of $n$ points:

$$\overline{\delta^2}(\Delta) = \frac{1}{n - k} \sum_{j=1}^{n-k} \lvert \mathbf{r}(t_{j+k}) - \mathbf{r}(t_j) \rvert^2,$$

and D is fitted from $\overline{\delta^2} = 2dD\Delta$ on **short** lags. At long lags the windows overlap and only about $n/k$ of them are independent, so the estimate becomes noisy (Exercise 4). Two corrections follow from the model: a localization error of variance $\sigma^2$ per coordinate adds a constant $2d\sigma^2$ to every lag (each displacement is the difference of two independently noisy positions), so D is read from the slope and the intercept gives $\sigma$; and a constant drift $v$ adds $v^2 \Delta^2$, since $\langle (x_\text{diff} + v\Delta)^2 \rangle = 2D\Delta + v^2\Delta^2$ per coordinate when the drift is independent of the noise.

### Reading a mean squared displacement curve

On log-log axes, the slope of $\overline{\delta^2}(\Delta)$ diagnoses the motion: 1 for free diffusion ($2dD\Delta$); 2 at long lags for directed transport ($v^2\Delta^2$ dominates); falling towards 0 under confinement, since a particle uniform in a box of side $L$ has $\langle (x_1 - x_2)^2 \rangle = 2 \times L^2/12 = L^2/6$ per coordinate, a plateau. A fitted D means something only if the curve has slope 1 over the lags used. Real tracks mix regimes (a vesicle diffusing, then carried by a motor), which is why trajectory analysis segments tracks before fitting.

## Mathematical representation

- Steps $s_i \in \{-a, +a\}$, independent, equiprobable; position after $N$ steps $x_N = \sum_{i=1}^N s_i$, time $t = N\tau$.
- $\mathbb{E}[x_N] = 0$, $\operatorname{Var}(x_N) = N a^2$, so $\langle x^2 \rangle = 2Dt$ with $D = a^2/(2\tau)$.
- In $d$ dimensions with independent coordinates: $\langle r^2 \rangle = 2dDt$.
- **Diffusion equation**: $\partial_t c = D \nabla^2 c$, with the 1D point-source solution $c(x, t) = \frac{n_0}{\sqrt{4\pi Dt}} e^{-x^2/4Dt}$ for $n_0$ molecules per unit area released at $x = 0$.
- **Einstein relation**: $D = k_B T / \zeta$, with $k_B$ the Boltzmann constant, $T$ the absolute temperature and $\zeta$ the friction coefficient (force per unit velocity).

## Computational representation

A lattice random walk with the standard library: each coordinate moves $\pm a$ at every step, so each coordinate is an independent 1D walk with $D = a^2/2\tau = 0.5$. The seed makes the run reproducible ([[Random Number Generation]]).

```python
import random


def simulate_msd(dim: int, n_walkers: int = 2000, n_steps: int = 200,
                 a: float = 1.0, seed: int = 42) -> list[float]:
    """Mean squared displacement after each step; every coordinate moves +a or -a (tau = 1)."""
    rng = random.Random(seed)
    pos = [[0.0] * dim for _ in range(n_walkers)]
    msd = []
    for _ in range(n_steps):
        for p in pos:
            for k in range(dim):
                p[k] += a if rng.random() < 0.5 else -a
        msd.append(sum(x * x for p in pos for x in p) / n_walkers)
    return msd


D = 0.5                                   # a^2 / (2 tau) with a = tau = 1
for dim in (1, 2):
    msd = simulate_msd(dim)
    print(f"{dim}D:", "  ".join(f"t={t} {msd[t - 1]:.1f} (2dDt={2 * dim * D * t:.0f})" for t in (10, 100, 200)))


def diffusion_time(x_m: float, D_m2_s: float) -> float:
    """Time t = x^2 / (2D) for the root-mean-square 1D displacement to reach x."""
    return x_m ** 2 / (2 * D_m2_s)


def readable(t: float) -> str:
    for unit, s in (("years", 3.156e7), ("h", 3600), ("min", 60), ("s", 1)):
        if t >= s:
            return f"{t / s:.2g} {unit}"
    return f"{t * 1e3:.2g} ms"


distances = {"1 µm": 1e-6, "10 µm": 1e-5, "1 mm": 1e-3, "1 m": 1.0}
for name, D_si in {"small molecule (1000 µm²/s)": 1e-9, "protein (10 µm²/s)": 1e-11}.items():
    print(name, "|", ", ".join(f"{k}: {readable(diffusion_time(x, D_si))}" for k, x in distances.items()))
```

```text
1D: t=10 10.1 (2dDt=10)  t=100 106.8 (2dDt=100)  t=200 205.7 (2dDt=200)
2D: t=10 20.3 (2dDt=20)  t=100 202.9 (2dDt=200)  t=200 398.5 (2dDt=400)
small molecule (1000 µm²/s) | 1 µm: 0.5 ms, 10 µm: 50 ms, 1 mm: 8.3 min, 1 m: 16 years
protein (10 µm²/s) | 1 µm: 50 ms, 10 µm: 5 s, 1 mm: 14 h, 1 m: 1.6e+03 years
```

The simulated values scatter by a few percent around $2dDt$: with 2000 walkers, the ensemble average has a relative error of order $\sqrt{2/2000} \approx 3\,\%$ (the variance of $x^2$ for a Gaussian is $2\langle x^2 \rangle^2$).

## Worked example

> [!example] Crossing a bacterium versus walking down an axon
> A protein with $D = 10$ µm²/s, $t = x^2/2D$.
> 1. **Across *E. coli*,** $x = 1$ µm: $t = 1 / (2 \times 10) = 0.05$ s.
> 2. **Along an axon,** $x = 1$ m $= 10^6$ µm (assumed length): $t = 10^{12} / 20 = 5 \times 10^{10}$ s. One year is about $3.16 \times 10^7$ s, so $t \approx 1600$ years: a distance ratio of $10^6$ costs a time ratio of $10^{12}$.
> 3. **Directed transport** at an assumed 1 µm/s covers 1 m in $10^6$ s, about 12 days: slow, but linear in distance. Long axons depend on motor-driven transport along microtubules.[^alberts]

## Common misconceptions

> [!warning] "A diffusing molecule has a speed"
> The average progress $x_\text{rms}/t = \sqrt{2D/t}$ falls as time goes on: diffusion has no velocity. The instantaneous thermal velocity is large (meters per second) but is randomized about every $10^{-13}$ s.

> [!warning] "The concentration gradient pushes each molecule"
> No force acts on an individual molecule. The net flux is a statistical effect of unbiased motion: more molecules on one side means more crossings from that side.

> [!warning] "$\langle r^2 \rangle = 2Dt$ in any dimension"
> In 2D it is $4Dt$, in 3D $6Dt$. Quoting a D from a mean squared displacement without the dimension creates factor-2 or factor-3 errors between papers and tools.

## Exercises

> [!question] Exercise 1 (L1)
> Using $t = x^2/2D$, how long does a small molecule ($D = 1000$ µm²/s) take to diffuse across a 10 µm cell? A protein in cytoplasm ($D = 10$ µm²/s)?

> [!success]- Solution
> Small molecule: $100 / 2000 = 0.05$ s = 50 ms. Protein: $100 / 20 = 5$ s. A hundredfold smaller D means a hundredfold longer time at the same distance.

> [!question] Exercise 2 (L1)
> A lipid diffuses in a membrane with $D = 10^{-8}$ cm²/s. Convert D to µm²/s, then estimate the time to move 2 µm in the plane of the membrane.

> [!success]- Solution
> 1 cm² = $10^8$ µm², so $D = 1$ µm²/s. In two dimensions $\langle r^2 \rangle = 4Dt$, so $t = 4/(4 \times 1) = 1$ s, as stated in [[Cell Membrane]].

> [!question] Exercise 3 (L2)
> A lattice walker stays put with probability $p$ and steps $\pm a$ with probability $(1-p)/2$ each, every $\tau$. Show that $D = (1-p)\,a^2/(2\tau)$.

> [!success]- Solution
> One step has mean 0 and $\langle s^2 \rangle = (1-p)\,a^2$. Steps are independent, so after $N = t/\tau$ steps $\langle x^2 \rangle = N (1-p) a^2 = \frac{(1-p) a^2}{\tau}\, t = 2Dt$ with $D = (1-p)a^2/(2\tau)$. Pausing slows diffusion in proportion to the time spent moving: the reasoning behind effective diffusion coefficients of molecules that bind transiently.

> [!question] Exercise 4 (L3, Python)
> Simulate one 2D lattice trajectory of 10,000 steps ($D = 0.5$) and estimate D from its time-averaged mean squared displacement at lags 1, 10, 100, 1000 and 5000. Explain the trend.

> [!success]- Solution
> ```python
> import random
>
>
> def trajectory(n_steps: int, dim: int = 2, a: float = 1.0, seed: int = 7) -> list[list[float]]:
>     rng = random.Random(seed)
>     p, path = [0.0] * dim, []
>     for _ in range(n_steps):
>         p = [x + (a if rng.random() < 0.5 else -a) for x in p]
>         path.append(p)
>     return path
>
>
> def time_averaged_msd(path: list[list[float]], lag: int) -> float:
>     """Average of |r(t + lag) - r(t)|^2 over all start times t of one trajectory."""
>     n = len(path) - lag
>     return sum(sum((u - v) ** 2 for u, v in zip(path[t + lag], path[t])) for t in range(n)) / n
>
>
> path = trajectory(10_000)
> print(", ".join(f"lag {lag}: D = {time_averaged_msd(path, lag) / (4 * lag):.3f}" for lag in (1, 10, 100, 1000, 5000)))
> ```
> Output: `lag 1: D = 0.500, lag 10: D = 0.475, lag 100: D = 0.412, lag 1000: D = 0.350, lag 5000: D = 0.193`.
> Short lags recover $D = 0.5$; at lag 1 the estimate is exact because every step has $\lvert \Delta \mathbf{r} \rvert^2 = 2$ on this lattice. At lag 1000 only about 10 independent windows exist, at lag 5000 about 2, so the estimate wanders far from the truth. Fit D on the first few lags only.

## Mastery checklist

- [ ] 1 Recognized: I can define diffusion and D, and quote $\langle x^2 \rangle = 2Dt$ and typical D values for small molecules, proteins and lipids.
- [ ] 2 Understood: I can derive $\langle x^2 \rangle = 2Dt$ from a random walk and explain why diffusion is fast across a bacterium and hopeless along an axon.
- [ ] 3 Practiced: I can simulate random walks, recover D from mean squared displacements and compute diffusion times with the right dimensional factor.
- [ ] 4 Applied: I estimated D from real tracking or simulation data, or checked a published D against the size of the molecule and the timescale of a process.
- [ ] 5 Explained: I can teach the diffusion equation, the crossover with directed transport, and the pitfalls of mean squared displacement fits (long lags, localization noise, mixed regimes).

## References

[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of diffusion: random walks and the mean squared displacement, diffusion coefficients of small molecules and proteins in water and in the cytoplasm, net flux down a gradient, the Einstein relation.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane structure (lateral diffusion of lipids, about $10^{-8}$ cm²/s) and of the cytoskeleton (motor proteins carrying organelles along microtubules, including in axons).
[^up]: [[University Physics (OpenStax)]], Volume 2: kinetic theory (average kinetic energy per molecule and the equipartition of energy).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA: Boltzmann constant $1.380\,649 \times 10^{-23}$ J K⁻¹ and Avogadro constant, exact since the 2019 SI.
