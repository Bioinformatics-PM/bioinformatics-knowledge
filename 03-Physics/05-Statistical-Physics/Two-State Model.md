---
aliases:
  - Two-State System
  - Two-Level System
  - Two-State Approximation
  - Modèle à deux états
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - domain/chemistry
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Boltzmann Distribution]]"
  - "[[Partition Function]]"
  - "[[Gibbs Free Energy]]"
  - "[[Chemical Equilibrium]]"
  - "[[Logarithm]]"
related:
  - "[[Ising Model]]"
  - "[[Helix-Coil Transition]]"
  - "[[Ion Channel]]"
  - "[[Membrane Potential]]"
  - "[[Ligand Binding]]"
  - "[[Protein Folding]]"
  - "[[Cooperativity]]"
  - "[[Hill Function]]"
  - "[[Allosteric Regulation]]"
  - "[[Transcription Factor]]"
  - "[[Logistic Regression]]"
  - "[[Detailed Balance]]"
  - "[[Optical Tweezers]]"
  - "[[Calorimetry]]"
  - "[[Mutation]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Myers 1995 - Denaturant m Values and Heat Capacity Changes]]"
  - "[[Biochemistry (Berg)]]"
  - "[[MIT 8.591J - Systems Biology]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Two-State Model

> [!abstract]
> Many molecules behave as if they had only two states: closed or open, folded or unfolded, empty or bound. Their occupancy is a logistic function of a free-energy difference, and that difference shifts linearly with whatever you control (voltage, denaturant, temperature, force, the logarithm of a concentration): the midpoint of the curve gives the free energy, its slope gives the coupling.

## Definition

A **two-state model** groups the microstates of a molecule into two macrostates $A$ and $B$, with partial partition functions $Z_A$ and $Z_B$ and free-energy difference $\Delta G = G_B - G_A = -k_BT\ln(Z_B/Z_A)$ ([[Partition Function#Core (L2)]]). At equilibrium
$$p_B = \frac{1}{1 + e^{\Delta G/k_BT}},$$
and the biology enters through the way $\Delta G$ depends on a control variable: ligand concentration for a receptor, voltage or membrane tension for an ion channel, temperature or denaturant for a protein.[^pboc7]

## Why it matters

- **One curve fits a large part of biophysics.** Binding curves ($K_d$), channel gating curves, denaturation and melting curves are fitted with this function; the fit returns a free energy and a coupling constant, the quantities that databases of stabilities and affinities report ([[Ligand Binding]], [[Ion Channel]], [[Protein Folding]]).
- **Variant effects on stability.** A destabilizing mutation is a change $\Delta\Delta G$ of the two-state free energy; its effect on the folded fraction follows from the formula (Worked example, [[Mutation]]).
- **Building block of cooperativity.** Couple two-state units and you get the [[Ising Model]], the [[Helix-Coil Transition]] and allosteric models; the input functions of gene regulation are two-state occupancies made steeper by cooperativity ([[Hill Function]], [[Transcription Factor]]).[^8591]
- **It is logistic regression.** $\ln[p_B/(1 - p_B)]$ is linear in the control variable, exactly the model of [[Logistic Regression]]; a position weight matrix score turned into a binding probability is the same function ([[Boltzmann Distribution#Exercises]]).

## Core (L2)

### One formula, many control variables

When the control variable $x$ couples linearly to the state, $\Delta G(x) = \Delta G_0 - m x$, and the occupancy becomes
$$p_B(x) = \frac{1}{1 + e^{-m(x - x_{1/2})/k_BT}}, \qquad x_{1/2} = \frac{\Delta G_0}{m}.$$
The midpoint $x_{1/2}$ is where $\Delta G = 0$; the coupling $m$ measures how much the free-energy difference moves per unit of $x$:

| System | $B$ state | Control $x$ | Coupling $m$ | Result |
|---|---|---|---|---|
| Receptor or DNA site | bound | $\ln(c/K_d)$ | $k_BT$ per ligand | $p = c/(c + K_d)$ |
| Voltage-gated channel | open | voltage $V$ | gating charge $ze$ | $p_{\text{open}}(V)$ |
| Protein in denaturant | unfolded | concentration $[D]$ | $m$ value | denaturation curve |
| Protein heated | unfolded | temperature $T$ | $\Delta S$ ($= \Delta H/T_m$) | melting curve |
| Hairpin under force | unfolded | force $F$ | extension change $\Delta x$ | $p_{\text{open}}(F)$ |

The binding row is the lattice result of [[Boltzmann Distribution#Core (L1)]]. For a channel, opening moves an effective charge $ze$ through the membrane field, which adds $-zeV$ to $\Delta G$ ([[Membrane Potential]]); ion channels are the textbook two-state systems of physical biology.[^pboc7] For a protein, the free energy of unfolding decreases linearly with denaturant concentration, and the slope, the **m value**, grows with the surface the protein exposes on unfolding.[^myers] Temperature enters through $\Delta G = \Delta H - T\Delta S$ ([[Boltzmann Distribution#Exercises]]).

### Steepness: the 10 to 90 % width

Solving $p_B = 0.1$ and $p_B = 0.9$ gives $m(x - x_{1/2})/k_BT = \mp\ln 9$, so the transition spans
$$x_{90} - x_{10} = \frac{k_BT}{m}\ln 81 \approx 4.39\,\frac{k_BT}{m}.$$
A strong coupling gives a sharp switch. For simple binding ($m = k_BT$ per unit of $\ln c$) the occupancy goes from 10 % to 90 % over an **81-fold** change of concentration, whatever the affinity. A channel with $z = 6$ switches over 19 mV, one with $z = 1$ over 113 mV:

![[two-state-gating-steepness.svg]]

### Bio: channels, binding sites, folded proteins

- **Ion channel gating.** Fitting $p_{\text{open}}(V)$ gives $V_{1/2}$ and the gating charge $z$; the free-energy difference at 0 mV is $-zeV_{1/2}$ (Computational representation).[^pboc7]
- **Ligand and transcription factor binding.** Occupancy $c/(c + K_d)$ is hyperbolic in $c$ and sigmoidal in $\ln c$, with half-occupancy at $c = K_d$ (Exercise 2).
- **Folded and unfolded proteins.** For a protein that unfolds without populated intermediates, the denaturation curve gives $\Delta G$ in water by linear extrapolation, $\Delta G_{\text{H}_2\text{O}} = m\,[D]_{1/2}$ (Worked example).[^myers]

## Advanced (L3)

### Is it really two-state?

If only two states exist, any measured signal is $S = (1 - p_B)S_A + p_BS_B$, and after normalization between the two baselines every probe (fluorescence, circular dichroism, activity) must give the **same** curve. A populated intermediate makes probes disagree (Exercise 4). Two further tests: in calorimetry, the van 't Hoff enthalpy from the curve's shape equals the calorimetric enthalpy only for a two-state transition ([[Partition Function#Advanced (L3)]]); in kinetics, relaxation is a single exponential.

### Kinetics and detailed balance

With rate constants $k_{AB}$ and $k_{BA}$, $\frac{dp_B}{dt} = k_{AB}(1 - p_B) - k_{BA}p_B$ relaxes to equilibrium with the single rate $k_{\text{obs}} = k_{AB} + k_{BA}$, and the equilibrium condition $k_{AB}/k_{BA} = e^{-\Delta G/k_BT}$ ties kinetics to thermodynamics ([[Detailed Balance]]). A perturbation (temperature jump, voltage step) followed by an exponential return is the kinetic signature of two states.

### States within states: the MWC model

Each macrostate can hold internal states. In the Monod-Wyman-Changeux model, a protein with $n$ identical sites is either relaxed (R) or tense (T), all subunits switching together; ligands bind R with dissociation constant $K_R$ and T with $K_T = K_R/c$ ($c < 1$), and $L = [T]/[R]$ without ligand. With $x = [\text{ligand}]/K_R$:
$$p_R = \frac{(1 + x)^n}{(1 + x)^n + L(1 + cx)^n}.$$
Ligand binding pulls the molecule into R, which raises the affinity of the remaining sites: cooperativity without any direct contact between ligands. It is the standard two-state treatment of cooperative binding,[^pboc7] and this concerted model is one of the two classic models of hemoglobin's cooperative oxygen binding.[^berg] Exercise 5 computes its steepness.

### How steep can binding be?

For $n$ sites with weights $\propto x^N$, the Hill slope $n_H = d\ln[\theta/(1 - \theta)]/d\ln x$ of the fractional saturation $\theta = \langle N\rangle/n$ equals $\operatorname{Var}(N)/[n\,\theta(1 - \theta)]$, because $d\langle N\rangle/d\ln x = \operatorname{Var}(N)$ ([[Partition Function#Core (L2)]]). At half saturation $\operatorname{Var}(N) \le n^2/4$, so $n_H \le n$: the all-or-none limit, the Hill function $\theta = x^n/(1 + x^n)$, is the steepest possible. Hemoglobin, with four sites, has a Hill coefficient of about 2.8.[^berg]

## Frontier (M1)

- **One molecule at a time.** In an optical trap, a nucleic-acid hairpin held near its midpoint force hops between folded and unfolded states. Because a single molecule's time average equals the ensemble average at equilibrium ([[Statistical Ensemble]]), the fraction of time spent unfolded at each force is $p_B(F)$, and the curve gives $\Delta G_0$ and $\Delta x$ directly (Exercise 6, [[Optical Tweezers]]).
- **Fitting is a statistical problem.** Linearizing with the logit (Computational representation) overweights noisy points near 0 and 1; maximum-likelihood fitting of the logistic model ([[Logistic Regression]], [[Maximum Likelihood Estimation]]) uses binomial errors correctly when the data are counts (open channels, bound reads).

## Mathematical representation

- Macrostates $A$, $B$: $\Delta G = -k_BT\ln(Z_B/Z_A)$; $p_B = 1/(1 + e^{\Delta G/k_BT})$; $\operatorname{logit}(p_B) = \ln\frac{p_B}{1 - p_B} = -\Delta G/k_BT$.
- Linear coupling: $\Delta G(x) = \Delta G_0 - mx$; $\operatorname{logit}(p_B) = m(x - x_{1/2})/k_BT$; $x_{1/2} = \Delta G_0/m$; width $x_{90} - x_{10} = (k_BT/m)\ln 81$.
- Ligand: $x = \ln(c/K_d)$, $m = k_BT$: $p = c/(c + K_d)$. All-or-none $n$-mer: $\theta = c^n/(c^n + K^n)$.
- Kinetics: $\dot p_B = k_{AB}(1 - p_B) - k_{BA}p_B$, $k_{\text{obs}} = k_{AB} + k_{BA}$, $k_{AB}/k_{BA} = e^{-\Delta G/k_BT}$.
- MWC: $p_R = (1 + x)^n/[(1 + x)^n + L(1 + cx)^n]$; fractional saturation $\theta = \dfrac{x(1 + x)^{n-1} + Lcx(1 + cx)^{n-1}}{(1 + x)^n + L(1 + cx)^n}$.
- Hill slope: $n_H = \operatorname{Var}(N)/[n\,\theta(1 - \theta)] \le n$ at $\theta = \frac12$.

## Computational representation

A gating curve is fitted by linear regression of $\ln[p/(1 - p)]$ on $V$, with $k_BT/e = 25.69$ mV at 25 °C from the exact $k_B$ and $e$:[^nist]

```python
from math import log
from statistics import linear_regression

KT_E = 25.69                    # kT/e in mV at 25 C

volts = [-70, -60, -50, -40, -30, -20, -10, 0]                    # mV
p_open = [0.008, 0.021, 0.075, 0.19, 0.45, 0.70, 0.90, 0.96]      # invented measurements

# two-state: ln(p_open / p_closed) = z (V - V_half) / (kT/e), a straight line in V
logit = [log(p / (1 - p)) for p in p_open]
slope, intercept = linear_regression(volts, logit)
z = slope * KT_E
v_half = -intercept / slope
print(f"z = {z:.2f} elementary charges, V_half = {v_half:.1f} mV")
print(f"10-90 % width = {log(81) / slope:.1f} mV")
print(f"dG(0 mV) = {-intercept:.2f} kT")
```

```text
z = 2.98 elementary charges, V_half = -27.9 mV
10-90 % width = 37.9 mV
dG(0 mV) = -3.24 kT
```

The channel carries about 3 gating charges and is open-favored by $3.2\,k_BT$ at 0 mV: $\Delta G(0) = -zeV_{1/2}$, i.e. $-2.98 \times 27.9/25.69$. `statistics.linear_regression` needs Python 3.10 or later.

## Worked example

> [!example] Denaturation, stability and a mutation (invented data)
> A protein unfolds in urea at 25 °C ($RT = 2.479$ kJ/mol) with midpoint $[D]_{1/2} = 4.0$ M and $m = 6.0$ kJ mol⁻¹ M⁻¹.
> 1. **Model.** $\Delta G(D) = \Delta G_{\text{H}_2\text{O}} - m[D]$ (unfolding free energy), $p_U = 1/(1 + e^{\Delta G/RT})$.
> 2. **Stability in water.** $\Delta G = 0$ at the midpoint, so $\Delta G_{\text{H}_2\text{O}} = m[D]_{1/2} = 24$ kJ/mol, and $p_U(0) = 1/(1 + e^{24/2.479}) = 6.2\times 10^{-5}$.
> 3. **Inside the transition.** At 3 M, $\Delta G = 6$ kJ/mol and $p_U = 0.082$; the 10 to 90 % width is $\ln 81 \times 2.479/6 = 1.8$ M.
> 4. **A mutation** that destabilizes by $\Delta\Delta G = 5$ kJ/mol (same $m$) moves the midpoint to $19/6 = 3.17$ M and raises $p_U(0)$ to $4.7\times 10^{-4}$, 7.5 times more unfolded protein, although the protein remains 99.95 % folded.
> 5. **Reading.** The midpoint alone does not give the stability; midpoint times slope does. A larger protein exposes more surface on unfolding, hence a larger $m$,[^myers] so the same midpoint means more stability.

## Common misconceptions

> [!warning] "Two-state means two microstates"
> Each state is a macrostate with many microstates; $\Delta G$ includes their entropy ([[Partition Function#Core (L2)]]). An unfolded protein is one state in the model and an astronomical number of conformations in reality.

> [!warning] "A sigmoidal binding curve proves cooperativity"
> On a logarithmic concentration axis every binding curve is sigmoidal, including simple $c/(c + K_d)$. Cooperativity is a Hill slope above 1 on that axis (a range narrower than 81-fold), or a sigmoid on a **linear** axis.

> [!warning] "The midpoint measures stability"
> $\Delta G_0 = m\,x_{1/2}$: two proteins with the same denaturation midpoint can differ in stability if their $m$ values differ.

> [!warning] "A good fit proves two-state behavior"
> Data from one probe are often fitted well by a two-state curve even when an intermediate is populated. Compare normalized curves from several probes (Exercise 4).

## Exercises

> [!question] Exercise 1 (L2)
> A channel has $V_{1/2} = -30$ mV and $z = 4$ at 25 °C ($k_BT/e = 25.69$ mV). Compute $p_{\text{open}}$ at $-60$, $-30$ and $0$ mV, and the 10 to 90 % width.

> [!success]- Solution
> $p = 1/(1 + e^{-z(V - V_{1/2})/(k_BT/e)})$. At $-60$ mV the exponent is $4 \times 30/25.69 = 4.671$, so $p = 1/(1 + e^{4.671}) = 0.0093$; at $-30$ mV, $p = 0.5$; at 0 mV, $p = 0.9907$. Width: $25.69 \times 4.394/4 = 28.2$ mV.

> [!question] Exercise 2 (L2)
> A transcription factor binds its site with $K_d = 10$ nM. Compute the occupancy at 1, 10 and 100 nM, and the concentrations giving 10 % and 90 % occupancy. Over which range would a Hill function with $n = 2.8$ switch?

> [!success]- Solution
> $c/(c + K_d)$ = 0.091, 0.5 and 0.909. $p = 0.1$ at $c = K_d/9 = 1.1$ nM and $p = 0.9$ at $9K_d = 90$ nM: an 81-fold range. For $\theta = c^n/(c^n + K^n)$ the range is $81^{1/n}$: 4.8-fold for $n = 2.8$, the hemoglobin value,[^berg] which is why cooperative binding behaves as a switch.

> [!question] Exercise 3 (L2)
> Show that for any two-state system, $\operatorname{logit}(p_B)$ is a straight line in the control variable, and give the meaning of its slope and intercept for the urea data of the Worked example.

> [!success]- Solution
> $\operatorname{logit}(p_B) = -\Delta G/k_BT = (m x - \Delta G_0)/k_BT$: slope $m/k_BT$, intercept $-\Delta G_0/k_BT$. For the Worked example, slope $6/2.479 = 2.42$ per molar urea and intercept $-24/2.479 = -9.68$; the line crosses 0 at 4.0 M. A curved logit plot is a sign that the model or the linear coupling fails.

> [!question] Exercise 4 (L3)
> A protein unfolds through an intermediate: $G_N = 0$, $G_I = 10 - 3[D]$ and $G_U = G_I + 14 - 3[D]$ kJ/mol (invented, $RT = 2.479$ kJ/mol). Probe 1 changes on leaving N (it reports $p_I + p_U$); probe 2 changes only for U (it reports $p_U$). Compute both at 3, 4 and 5 M urea. What would a single-probe two-state analysis miss?

> [!success]- Solution
> Weights $1$, $e^{-G_I/RT}$, $e^{-G_U/RT}$. At 3 M: probe 1 = 0.431, probe 2 = 0.051; at 4 M: 0.764 and 0.236; at 5 M: 0.949 and 0.569. The normalized curves do not coincide, so the system is not two-state. Each curve alone looks sigmoidal and would be fitted by a two-state model with wrong midpoints and $m$ values; the disagreement between probes reveals the intermediate.

> [!question] Exercise 5 (L3, Python)
> For the MWC model with $n = 4$ and $c = 0.01$, find the ligand concentration of half saturation and the Hill slope there, for $L = 1$, 100, $10^4$ and $10^6$. Which $L$ gives the steepest response, and why is the slope always below 4?

> [!success]- Solution
> ```python
> from math import log
>
>
> def mwc_occupancy(x, n=4, L=1000.0, c=0.01):
>     """Fraction of n sites bound; x = conc/K_R, K_R/K_T = c, L = [T]/[R] without ligand."""
>     r, t = (1 + x) ** n, L * (1 + c * x) ** n
>     bound = x * (1 + x) ** (n - 1) + L * c * x * (1 + c * x) ** (n - 1)
>     return bound / (r + t)
>
>
> def hill_slope(f, x, h=1e-5):
>     """d ln(theta / (1 - theta)) / d ln x, by central differences."""
>     def logit(v):
>         th = f(v)
>         return log(th / (1 - th))
>     return (logit(x * (1 + h)) - logit(x * (1 - h))) / (2 * h)
>
>
> for L in (1.0, 100.0, 1e4, 1e6):
>     f = lambda v, L=L: mwc_occupancy(v, L=L)
>     lo, hi = 1e-4, 1e6                          # bisection for half saturation
>     for _ in range(200):
>         m2 = (lo * hi) ** 0.5
>         lo, hi = (m2, hi) if f(m2) < 0.5 else (lo, m2)
>     print(L, round(m2, 2), round(hill_slope(f, m2), 2))
> ```
>
> ```text
> 1.0 1.11 1.15
> 100.0 2.85 2.36
> 10000.0 10.0 3.01
> 1000000.0 35.08 2.36
> ```
>
> Cooperativity peaks at intermediate $L$ ($L = 10^4 = c^{-n/2}$ here): if $L$ is small the protein is already in R, if it is huge ligands rarely manage to switch it, and in both limits binding is nearly independent. The slope stays below $n = 4$ because the molecule is not all-or-none: partially liganded states keep a finite weight, and $n_H = 4\operatorname{Var}(N)/n < n$.

> [!question] Exercise 6 (M1)
> A hairpin held in an optical trap unfolds with $\Delta G_0 = 25\,k_BT$ and lengthens by $\Delta x = 18$ nm (invented; $k_BT = 4.116$ pN nm). Compute the midpoint force, the 10 to 90 % force width and the fraction of time spent unfolded at 5.0, 5.72 and 6.5 pN.

> [!success]- Solution
> $\Delta G(F) = \Delta G_0 - F\Delta x$, so $F_{1/2} = 25 \times 4.116/18 = 5.72$ pN and the width is $\ln 81 \times 4.116/18 = 1.0$ pN. $p_U = 1/(1 + e^{(\Delta G_0 - F\Delta x)/k_BT})$ = 0.042, 0.504 and 0.968: within one piconewton the molecule goes from mostly folded to mostly unfolded, and near $F_{1/2}$ a time trace shows it hopping between the two states.

## Mastery checklist

- [ ] 1 Recognized: I can write $p_B = 1/(1 + e^{\Delta G/k_BT})$ and name the two states of a channel, a binding site and a protein.
- [ ] 2 Understood: I can explain why $\Delta G$ is linear in voltage, denaturant, force or $\ln c$, and what the midpoint and the slope of a two-state curve measure.
- [ ] 3 Practiced: I can fit a gating or denaturation curve, extract $\Delta G$ and the coupling, and compute 10 to 90 % widths.
- [ ] 4 Applied: I can estimate the effect of a mutation's $\Delta\Delta G$ on the folded fraction and test two-state behavior with several probes or calorimetry.
- [ ] 5 Explained: I can teach the MWC model, the bound $n_H \le n$ and why single-molecule time traces measure equilibrium occupancies.

## References

[^pboc7]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 7 "Two-State Systems: From Ion Channels to Cooperative Binding" (ion channel open probability, ligand binding, MWC models).
[^myers]: [[Myers 1995 - Denaturant m Values and Heat Capacity Changes]], *Protein Science* 4(10):2138-2148 (denaturant m values of two-state proteins correlate with the surface exposed on unfolding).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of hemoglobin (cooperative oxygen binding, Hill coefficient, concerted and sequential models).
[^8591]: [[MIT 8.591J - Systems Biology]], lecture "Input Function, Michaelis-Menten Kinetics, and Cooperativity".
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA values of the Boltzmann constant and the elementary charge (exact since the 2019 SI revision).
