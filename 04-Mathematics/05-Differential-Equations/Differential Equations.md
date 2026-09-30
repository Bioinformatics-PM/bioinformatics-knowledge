---
aliases:
  - ODEs
  - Dynamical Systems
  - Équations différentielles
tags:
  - type/moc
  - domain/mathematics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Calculus]]"
  - "[[Linear Algebra]]"
projects: []
sources:
  - "[[MIT 18.03SC - Differential Equations]]"
  - "[[Nonlinear Dynamics and Chaos (Strogatz)]]"
  - "[[Mathematical Biology (Murray)]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[Calculus (OpenStax)]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
---

# Differential Equations

> [!abstract]
> Equations for how quantities change in time: solving first-order ODEs, simulating them numerically, and reading the qualitative behavior (steady states, stability, oscillations, switches) of nonlinear systems.

## Why it matters for bioinformatics

- Every **rate law** is a differential equation: enzyme kinetics, mRNA production and decay, population growth, epidemics, drug elimination.
- **Qualitative analysis** answers biological questions without a formula: is there a steady state, is it stable, can the circuit oscillate (circadian clocks) or switch (cell-fate decisions)?
- **Numerical solvers** are how models are used in practice; knowing Euler and Runge-Kutta explains what `solve_ivp` does and when it fails.

## Before you start

- [[Calculus]]: [[Derivative]], [[Integral]], [[Taylor Series]], [[Jacobian Matrix]].
- [[Linear Algebra]]: [[Eigenvalues and Eigenvectors]], [[Diagonalization]], [[Matrix Exponential]].
- [[Mathematical Foundations]]: [[Exponential Function]], [[Complex Number]].

## Learning path

### Stage 2 - Core (L2)

1. [[Ordinary Differential Equation]] (L2): write a rate statement as an ODE; distinguish order, linearity, autonomy; check a proposed solution. Bio: $dN/dt = rN$; $dm/dt = k - \gamma m$ for an mRNA.
2. [[Direction Field]] (L2): sketch slope fields and isoclines to see solutions without solving. Bio: reading growth and decay models at a glance.
3. [[Separable Differential Equation]] (L2): solve by separating variables. Bio: first-order decay and half-lives; the closed form of logistic growth.
4. [[Linear Differential Equation]] (L2): solve first-order linear ODEs with an integrating factor; use superposition. Bio: production-degradation kinetics, which reach steady state with time scale $1/\gamma$.
5. [[Euler Method]] (L2): step an ODE forward numerically and estimate the error from the step size. Bio: simulating any model that has no closed form.
6. [[Dynamical System]] (L2): think in states, flows and trajectories. Bio: a gene circuit or a population as a point moving in state space.
7. [[Fixed Point]] (L2): find steady states by solving $f(x^*) = 0$. Bio: homeostatic concentrations; the disease-free equilibrium of an epidemic.
8. [[Phase Line]] (L2): classify the stability of fixed points of a one-dimensional autonomous ODE. Bio: stable and unstable equilibria of logistic growth; a bistable autoactivating gene.
9. [[Second-Order Linear Differential Equation]] (L2): solve with the characteristic equation; read overdamped, critically damped and oscillating regimes. Bio: vibrations in molecular dynamics; damped oscillations of perturbed systems.

### Stage 3 - Advanced (L3)

10. [[System of Differential Equations]] (L3): write coupled ODEs in vector form and solve linear systems $x' = Ax$ with eigenvalues. Bio: predator-prey, SIR epidemics, two-gene toggle switches, two-compartment pharmacokinetics.
11. [[Phase Portrait]] (L3): classify nodes, saddles, spirals and centers of 2x2 systems from trace and determinant. Bio: reading the dynamics of a two-gene circuit.
12. [[Nullcline]] (L3): draw nullclines and locate fixed points geometrically. Bio: the bistable toggle switch; excitable neuron models.
13. [[Linear Stability Analysis]] (L3): linearize a nonlinear system with the [[Jacobian Matrix]] and decide stability from its eigenvalues. Bio: an epidemic grows when the disease-free equilibrium is unstable ($R_0 > 1$).
14. [[Limit Cycle]] (L3): recognize self-sustained oscillations. Bio: circadian clocks, the repressilator, glycolytic oscillations.
15. [[Bifurcation]] (L3): identify saddle-node, transcritical and Hopf bifurcations and hysteresis. Bio: switch-like cell-fate decisions; the epidemic threshold at $R_0 = 1$; the onset of oscillations.
16. [[Runge-Kutta Method]] (L3): use higher-order and adaptive-step solvers; recognize stiffness. Bio: what standard ODE solvers do when fitting kinetic models.

### Stage 4 - Frontier (M1)

17. [[Partial Differential Equation]] (M1): recognize diffusion and reaction-diffusion equations and their boundary conditions. Bio: morphogen gradients; Turing patterns in development.

> [!tip] What to skip
> Fourier series and the Laplace transform (18.03SC Unit III) are optional on this path. Units I and IV matter most; take Unit IV only after eigenvalues in [[Linear Algebra]]. For nonlinear systems, Strogatz's one- and two-dimensional flows are the better text.

## Uses from other domains

- [[Michaelis-Menten Kinetics]] ([[Biochemistry]]), [[Reaction Kinetics]] ([[Physical Chemistry]]): rate laws to integrate.
- [[Diffusion]], [[Membrane Potential]], [[Hodgkin-Huxley Model]] ([[Biophysics]]): PDEs and excitable dynamics.
- [[Harmonic Oscillator]] ([[Mechanics]]): the physical model of item 9.
- [[Gene Regulatory Network]], [[Feedback Loop]], [[Bistability]] ([[Systems Biology]]): feedback, switches and oscillations.
- [[Logistic Growth]], [[Lotka-Volterra Model]], [[Compartmental Model]] ([[Mathematical Modeling]]): the models these methods analyze.
- [[Numerical Integration]], [[Stiff Differential Equation]], [[Floating-Point Arithmetic]] ([[Scientific Computing]]): accuracy and stability of solvers; implicit methods for stiff kinetic models.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 18.03SC - Differential Equations]] | MIT | L2 | Unit I "First Order Differential Equations" (direction fields, Euler's method, linear ODEs); Unit II "Second Order Constant Coefficient Linear Equations"; Unit IV "First Order Systems" (phase portraits)[^1803] |
| [[MIT 8.591J - Systems Biology]] | MIT | L3 | "Autoregulation, Feedback and Bistability": items 7, 8 and 15 applied to gene circuits[^8591] |

## Reference books

- [[Nonlinear Dynamics and Chaos (Strogatz)]]: one-dimensional flows (fixed points, bifurcations), two-dimensional flows (phase plane, limit cycles), biological examples (SIR, Selkov glycolytic oscillations).[^strogatz]
- [[Mathematical Biology (Murray)]]: population models, biochemical oscillators and epidemics, to see the methods applied.[^murray]
- [[Calculus (OpenStax)]]: Volume 2 introduction to differential equations, as a first contact.[^openstax]

## Lab projects

No Lab project is built on differential equations yet. A natural extension of [[07-evolution-simulator]] compares simulated allele frequencies with the deterministic selection equation $dp/dt = s\,p(1 - p)$.

## References

[^1803]: [[MIT 18.03SC - Differential Equations]]: unit titles and contents as verified in the source note; Units I and IV are marked as the most relevant for biology.
[^8591]: [[MIT 8.591J - Systems Biology]], lecture "Autoregulation, Feedback and Bistability".
[^strogatz]: [[Nonlinear Dynamics and Chaos (Strogatz)]], 3rd ed.
[^murray]: [[Mathematical Biology (Murray)]], 3rd ed., Volume I.
[^openstax]: [[Calculus (OpenStax)]], Volume 2.

Scope check: differential equations are taught in the first-year mathematics for biologists at Cambridge (linear and non-linear differential equations)[^cam] and within the required calculus sequence of CMU's Computational Biology degree.[^cmu] The L3 items follow Strogatz's order: one-dimensional flows, then two-dimensional flows and limit cycles.[^strogatz]

[^cam]: [[University of Cambridge - Natural Sciences Tripos]], Part IA Mathematical Biology.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]], mathematics and statistics core.
