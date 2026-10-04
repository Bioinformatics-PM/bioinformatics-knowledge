---
aliases:
  - Motion Along a Straight Line
  - Position, Velocity and Acceleration
  - Cinématique
tags:
  - type/concept
  - domain/physics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Dimensional Analysis]]"
  - "[[Derivative]]"
  - "[[Integral]]"
  - "[[Vector]]"
related:
  - "[[Newton's Laws of Motion]]"
  - "[[Momentum]]"
  - "[[Molecular Motor]]"
  - "[[Brownian Motion]]"
  - "[[Diffusion]]"
  - "[[DNA Replication]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 8.01SC - Classical Mechanics]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Schnitzer 1997 - Kinesin Hydrolyses One ATP per 8-nm Step]]"
---

# Kinematics

> [!abstract]
> Kinematics describes motion without asking what causes it: position, velocity and acceleration are each the time derivative of the previous one, so knowing one of them (plus a starting value) gives the others.

## Definition

**Kinematics** is the description of motion by the position $x(t)$ of an object as a function of time, its **velocity** $v(t) = dx/dt$ and its **acceleration** $a(t) = dv/dt = d^2x/dt^2$. The **average velocity** over an interval is the displacement divided by the elapsed time, $\bar v = \Delta x / \Delta t$; the **instantaneous velocity** is its limit as $\Delta t \to 0$.[^up3][^801] In three dimensions the same definitions apply to the position vector $\vec r(t)$, component by component.[^up4]

## Why it matters

- **Molecular machines have speeds.** Polymerases, ribosomes and motor proteins move along their tracks; converting "nucleotides per second" into nm/s or µm/min lets you compare them and estimate how long a process takes ([[DNA Replication]], [[Molecular Motor]]).
- **Trajectories are data.** Single-molecule experiments and cell-tracking microscopy produce position-versus-time tables; velocity is estimated from them by finite differences or fits, and the mean squared displacement tells directed transport from [[Diffusion]] (Advanced).

## Core (L1)

**The derivative chain.** Velocity is the slope of $x(t)$, acceleration the slope of $v(t)$ ([[Derivative]]). Going back, the area under $v(t)$ is the displacement and the area under $a(t)$ the change of velocity ([[Integral]]):[^up3]

$$x(t) = x_0 + \int_0^t v(t')\,dt', \qquad v(t) = v_0 + \int_0^t a(t')\,dt'.$$

**Constant acceleration.** Integrating twice with $a$ constant:[^up3]

$$v = v_0 + a t, \qquad x = x_0 + v_0 t + \tfrac{1}{2} a t^2, \qquad v^2 = v_0^2 + 2a(x - x_0).$$

**Signs.** Velocity has a sign (direction along the axis); **speed** is its magnitude. Acceleration opposite to velocity slows the object down. Distance travelled is $\int |v|\,dt$, which differs from displacement when the motion reverses.[^up3]

**Speeds of molecular machines.** A bacterial replication fork adds about 1000 nucleotides per second.[^os14] With 0.34 nm per base pair along B-DNA,[^watson] that is $1000 \times 0.34 = 340$ nm/s, or about 3 s per micrometre of DNA. The motor kinesin walks along microtubules in discrete 8-nm steps, one ATP per step, and takes about 100 steps before letting go.[^schnitzer] Its position is therefore a staircase, not a smooth line:

![[kinesin-stepping-position-trace.svg]]

The useful "speed" of a stepping motor is the average velocity, step size divided by mean dwell time: $\bar v = d / \langle\tau\rangle$. With an assumed mean dwell of 10 ms (an illustrative value), $\bar v = 8\ \text{nm} / 0.010\ \text{s} = 800$ nm/s.

## Deeper (L2)

**Vectors.** In 3D, $\vec v = d\vec r/dt$ and $\vec a = d\vec v/dt$ component by component, so the 1D formulas apply to each axis separately ([[Vector]]).[^up4] Speed is $|\vec v|$. An object moving at constant speed on a curve still accelerates, because the direction of $\vec v$ changes.[^up4]

**Velocity from sampled data.** Measured positions $x_i = x(t_i)$ come at intervals $\Delta t$. A Taylor expansion gives the error of the two usual estimates:

$$\frac{x_{i+1} - x_i}{\Delta t} = v_i + O(\Delta t), \qquad \frac{x_{i+1} - x_{i-1}}{2\Delta t} = v_i + O(\Delta t^2).$$

The central difference is more accurate for smooth motion, but derivatives amplify noise: if each position has independent noise of standard deviation $\sigma$, the central difference has noise $\sigma / (\sqrt{2}\,\Delta t)$, which grows as the sampling gets faster (Exercise 6). Fitting a line to many points, or averaging over long windows, is the robust way to get a speed.

## Advanced (L3)

**Mean squared displacement (MSD).** For a trajectory, $\mathrm{MSD}(\tau) = \langle [x(t + \tau) - x(t)]^2 \rangle$, averaged over $t$. For motion at constant velocity, $\mathrm{MSD} = v^2 \tau^2$. For a random walk of independent steps $\pm d$, displacements add like independent random variables, so after $n$ steps $\mathrm{MSD} = n d^2$, linear in time. A log-log plot of MSD against $\tau$ therefore has slope 2 for directed transport and 1 for diffusion ([[Random Walk]], [[Brownian Motion]]); motor-driven cargo in cells shows a mixture, $\mathrm{MSD} \approx v^2\tau^2 + 2D\tau$ in one dimension. This is how tracking data separate active transport from diffusion (Exercise 5).

**Stepping as a stochastic process.** Because dwell times are random, the number of steps in a window fluctuates; the size of those fluctuations, not only the mean speed, carries mechanistic information. Schnitzer and Block used such statistics to show that kinesin uses one ATP per step.[^schnitzer]

## Mathematical representation

Position is a function $x : [0, t_{\max}] \to \mathbb{R}$ (or $\vec r : [0, t_{\max}] \to \mathbb{R}^3$) with dimension L; $v = \dot x$ has dimension L T⁻¹ and $a = \ddot x$ has L T⁻². Kinematics is the pair of first-order equations

$$\frac{dx}{dt} = v, \qquad \frac{dv}{dt} = a,$$

which [[Newton's Laws of Motion]] close by giving $a = F/m$. For a stepping motor with step $d$ and independent dwell times of mean $\langle\tau\rangle$, the position after a long time $t$ is $x(t) \approx d\, t / \langle\tau\rangle$, so $\bar v = d/\langle\tau\rangle$.

## Computational representation

A trajectory is two arrays, times and positions. The script below builds an invented kinesin-like trace (8-nm steps after random dwells of mean 10 ms, sampled every 1 ms) and estimates its speed three ways.

```python
import random

random.seed(1)
STEP_NM, MEAN_DWELL_S, DT = 8.0, 0.010, 0.001     # invented dwell time; 1 ms sampling

# Toy trace (invented): a motor that waits a random dwell time, then jumps 8 nm.
t_next, x, times, xs = random.expovariate(1 / MEAN_DWELL_S), 0.0, [], []
for i in range(201):                               # 0 to 0.2 s
    t = i * DT
    while t >= t_next:
        x += STEP_NM
        t_next += random.expovariate(1 / MEAN_DWELL_S)
    times.append(t)
    xs.append(x)

# 1. average velocity = displacement / elapsed time
v_avg = (xs[-1] - xs[0]) / (times[-1] - times[0])

# 2. least-squares slope of x(t)
n = len(xs)
tm, xm = sum(times) / n, sum(xs) / n
v_fit = sum((t - tm) * (x - xm) for t, x in zip(times, xs)) / sum((t - tm) ** 2 for t in times)

# 3. central differences: instantaneous velocity estimates
v_cd = [(xs[i + 1] - xs[i - 1]) / (2 * DT) for i in range(1, n - 1)]

print(f"steps: {xs[-1] / STEP_NM:.0f}, average v = {v_avg:.0f} nm/s, fitted v = {v_fit:.0f} nm/s")
print(f"central differences: {sum(v == 0 for v in v_cd)} of {len(v_cd)} are 0, max {max(v_cd):.0f} nm/s")
```

```text
steps: 22, average v = 880 nm/s, fitted v = 874 nm/s
central differences: 164 of 199 are 0, max 12000 nm/s
```

## Worked example

> [!example] Reading the toy trace
> 1. **Average velocity.** 22 steps of 8 nm in 0.2 s: $\bar v = 176\ \text{nm} / 0.2\ \text{s} = 880$ nm/s, close to the 800 nm/s set by the 10 ms mean dwell; the difference is chance, since 22 steps is a small sample.
> 2. **Fitted slope.** The least-squares slope, 874 nm/s, uses every point and is less sensitive to where the window starts and ends ([[Linear Regression]]).
> 3. **Instantaneous velocity.** Central differences are 0 most of the time (dwells) and up to 12,000 nm/s when two steps fall within 2 ms. The derivative of a staircase is a series of spikes: for a stepping motor, "the speed" means the average.

## Common misconceptions

> [!warning] "Zero velocity means zero acceleration"
> At the turning point of a motion, $v = 0$ while $a \ne 0$: the velocity is changing sign. Acceleration is the rate of change of velocity, not velocity itself.

> [!warning] "Faster sampling gives a better velocity"
> With noisy positions, the finite-difference velocity gets noisier as $\Delta t$ shrinks (noise $\propto 1/\Delta t$). Fit over a window instead.

## Exercises

> [!question] Exercise 1 (L1)
> $x(t) = 5 + 2t - t^2$ (x in m, t in s). Find $v(t)$ and $a(t)$, the time when the object is at rest, and compare displacement and distance travelled between $t = 0$ and $t = 2$ s.

> [!success]- Solution
> $v = 2 - 2t$ m/s, $a = -2$ m/s². At rest when $t = 1$ s. $x(0) = 5$, $x(1) = 6$, $x(2) = 5$: displacement 0 m, distance $1 + 1 = 2$ m, because the motion reverses at $t = 1$ s.

> [!question] Exercise 2 (L1)
> A replication fork adds about 1000 nucleotides per second.[^os14] Express its speed in µm/min (0.34 nm per bp) and compute how long it takes to copy a 10 kb stretch.

> [!success]- Solution
> $1000 \times 0.34 = 340$ nm/s $= 0.34$ µm/s $= 20.4$ µm/min. 10 kb at 1000 nt/s takes 10 s; it is 3.4 µm of DNA.

> [!question] Exercise 3 (L2)
> Derive $v^2 = v_0^2 + 2a(x - x_0)$ from the two other constant-acceleration equations and check its dimensions.

> [!success]- Solution
> From $v = v_0 + at$, $t = (v - v_0)/a$. Substitute into $x - x_0 = v_0 t + \frac{1}{2}at^2$: $x - x_0 = \frac{v_0(v - v_0)}{a} + \frac{(v - v_0)^2}{2a} = \frac{v^2 - v_0^2}{2a}$. Dimensions: L² T⁻² on both sides.

> [!question] Exercise 4 (L2)
> Kinesin takes about 100 steps of 8 nm before releasing its microtubule.[^schnitzer] What run length does that give? With an assumed mean dwell time of 10 ms (illustrative), how long does a run last and what is the average speed?

> [!success]- Solution
> Run length $\approx 100 \times 8 = 800$ nm. Duration $\approx 100 \times 10$ ms $= 1$ s, so $\bar v \approx 800$ nm/s. The run length is a kinematic number independent of the dwell time; the duration is not.

> [!question] Exercise 5 (L3, Python)
> Compute the MSD at lags of 1, 10 and 100 steps for a directed track (always +8 nm) and for a random walk of ±8 nm steps, 10,000 steps each. How does each scale with the lag?

> [!success]- Solution
> ```python
> import random
>
> random.seed(2)
> STEP_NM, STEPS = 8.0, 10_000
> directed = [STEP_NM * k for k in range(STEPS + 1)]
> walk = [0.0]
> for _ in range(STEPS):
>     walk.append(walk[-1] + random.choice((-STEP_NM, STEP_NM)))
>
> def msd(track, lag):
>     """Mean squared displacement over all pairs of points `lag` steps apart."""
>     d = [(track[i + lag] - track[i]) ** 2 for i in range(len(track) - lag)]
>     return sum(d) / len(d)
>
> for lag in (1, 10, 100):
>     print(lag, round(msd(directed, lag)), round(msd(walk, lag)))
> # 1 64 64
> # 10 6400 645
> # 100 640000 7237
> ```
>
> Directed: $64\,n^2$ (×100 per factor 10 of lag, slope 2 on a log-log plot). Random walk: about $64\,n$ (640 and 6400 expected; 645 and 7237 differ by sampling noise), slope 1. The two coincide at one step and separate quickly.

> [!question] Exercise 6 (L2)
> Positions are measured with independent noise of standard deviation 2 nm every 1 ms. What is the noise of a central-difference velocity? Compare with an 800 nm/s motor.

> [!success]- Solution
> $\mathrm{Var}\left[\frac{x_{i+1} - x_{i-1}}{2\Delta t}\right] = \frac{2\sigma^2}{4\Delta t^2}$, so the noise is $\frac{\sigma}{\sqrt{2}\,\Delta t} = \frac{2}{1.414 \times 0.001} \approx 1400$ nm/s, larger than the motor's speed. Velocities must come from fits over many points.

## Mastery checklist

- [ ] 1 Recognized: I can define position, velocity, acceleration, displacement and distance.
- [ ] 2 Understood: I can explain why velocity is a slope and displacement an area, and why a stepping motor's speed is an average.
- [ ] 3 Practiced: I can solve constant-acceleration problems and estimate velocities from sampled positions in Python.
- [ ] 4 Applied: I converted real polymerase or motor rates into nm/s and times, and computed an MSD from a trajectory file.
- [ ] 5 Explained: I can teach the noise amplification of numerical derivatives and how MSD scaling separates directed motion from diffusion.

## References

[^up3]: [[University Physics (OpenStax)]], Volume 1, ch. 3 "Motion Along a Straight Line".
[^up4]: [[University Physics (OpenStax)]], Volume 1, ch. 4 "Motion in Two and Three Dimensions".
[^801]: [[MIT 8.01SC - Classical Mechanics]]: kinematics.
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (replication of the *E. coli* chromosome, about 1000 nucleotides added per second).
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature* (bases 3.4 Å apart along the helix axis).
[^schnitzer]: [[Schnitzer 1997 - Kinesin Hydrolyses One ATP per 8-nm Step]], *Nature* 388:386-390 (8-nm steps, about 100 steps per run, one ATP per step, statistics of step intervals).
