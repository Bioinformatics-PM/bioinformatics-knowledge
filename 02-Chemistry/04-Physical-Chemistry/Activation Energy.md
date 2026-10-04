---
aliases:
  - Ea
  - Energy Barrier
  - Arrhenius Equation
  - Arrhenius Plot
  - Énergie d'activation
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Reaction Kinetics]]"
  - "[[Rate Law]]"
  - "[[Enthalpy]]"
  - "[[Exponential Function]]"
  - "[[Temperature]]"
related:
  - "[[Catalysis]]"
  - "[[Enzyme]]"
  - "[[Transition State Theory]]"
  - "[[Boltzmann Distribution]]"
  - "[[Gibbs Free Energy]]"
  - "[[Linear Regression]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
---

# Activation Energy

> [!abstract]
> Molecules must climb an energy barrier before they can react; the height of that barrier, the activation energy, decides how fast a reaction goes and how strongly its speed rises with temperature.

## Definition

The **activation energy** $E_a$ is the minimum energy that reacting molecules must have for a collision to lead to reaction; at the top of the barrier they form a short-lived, high-energy arrangement called the **activated complex** or **transition state**.[^chem12] The **Arrhenius equation** relates the rate constant to it:[^chem12]

$$k = A\, e^{-E_a/RT},$$

where $A$ is the frequency factor (how often molecules collide with a suitable orientation), $R = 8.314$ J mol⁻¹ K⁻¹ the gas constant and $T$ the absolute temperature. The factor $e^{-E_a/RT}$ is the fraction of collisions energetic enough to react.[^chem12]

## Why it matters

- **Temperature dependence of biology.** Reaction rates, hence enzyme activities and growth, rise with temperature until proteins unfold.[^os6] Arrhenius plots turn such measurements into barrier heights.
- **Why catalysts and enzymes work.** Lowering the barrier is the only way to speed a reaction without heating it ([[Catalysis]], [[Enzyme]]).
- **Lab practice.** Keeping samples on ice and incubating at a fixed temperature are applications of the exponential dependence of $k$ on $T$ (Exercise 4).
- **Models.** Temperature-dependent kinetic models, and the energy landscapes of structural biology, use the same exponential factor ([[Boltzmann Distribution]], [[Transition State Theory]]).

## Core (L1)

**Collisions and barriers.** For two molecules to react they must collide, with the right orientation, and with enough energy to stretch and break bonds; most collisions fail.[^chem12] The energy profile along the reaction coordinate shows the barrier:

![[reaction-energy-profile-activation.svg]]

Reading the diagram:

- $E_a$ (forward) is the climb from reactants to the transition state; $E_a$ (reverse) is the climb from products.
- The difference is the reaction enthalpy, $\Delta H = E_{a,\mathrm{f}} - E_{a,\mathrm{r}}$ ([[Enthalpy]]): an exothermic reaction has a higher reverse barrier.
- Barrier height and $\Delta H$ are independent: a very exothermic reaction can be slow if its barrier is high.

**The Arrhenius equation in log form.** Taking logarithms,[^chem12]

$$\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T},$$

so a plot of $\ln k$ against $1/T$ (an **Arrhenius plot**) is a straight line of slope $-E_a/R$. With two temperatures, the two-point form gives the rate change directly:

$$\ln\frac{k_2}{k_1} = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right).$$

**How much does temperature matter?** Computed with the code below:

| $E_a$ (kJ/mol) | $k(35\,°\mathrm{C})/k(25\,°\mathrm{C})$ | $k(40\,°\mathrm{C})/k(37\,°\mathrm{C})$ | $e^{-E_a/RT}$ at 37 °C |
|---:|---:|---:|---:|
| 25 | 1.39 | 1.10 | $6.2 \times 10^{-5}$ |
| 50 | 1.92 | 1.20 | $3.8 \times 10^{-9}$ |
| 100 | 3.70 | 1.45 | $1.4 \times 10^{-17}$ |

The higher the barrier, the more temperature-sensitive the rate. A barrier near 50 kJ/mol roughly doubles the rate for a 10 °C rise near room temperature; a 3 °C fever speeds such a reaction by about 20 %.

**Bio: enzymes and temperature.** Raising the temperature speeds enzyme-catalysed reactions, but beyond an optimum the enzyme denatures and activity falls; the Arrhenius equation describes only the rising part.[^os6]

## Deeper (L2)

**Where the exponential comes from.** At temperature $T$, the fraction of molecules with energy above a threshold $E$ falls as $e^{-E/RT}$ (per mole; $e^{-\epsilon/k_BT}$ per molecule): the [[Boltzmann Distribution]]. The Arrhenius factor is this tail fraction evaluated at the barrier.

**Arrhenius versus Eyring.** [[Transition State Theory]] rewrites the rate constant with the activation *free* energy, $k = (k_BT/h)\,e^{-\Delta G^\ddagger/RT}$, which separates enthalpic and entropic parts of the barrier; Arrhenius's $E_a$ and $A$ are their empirical counterparts. For enzymes, lowering $\Delta G^\ddagger$ is the language of [[Enzyme Catalysis]].

**Fitting $E_a$.** $E_a$ comes from the slope of $\ln k$ against $1/T$ ([[Linear Regression]]). Because biological temperatures span a narrow range (a few tens of kelvin), $1/T$ varies by only a few percent: the slope is sensitive to noise, and extrapolating far outside the measured range is risky. A curved Arrhenius plot means that more than one process, or a change of the system itself (unfolding, a change of rate-limiting step), is involved.

## Mathematical representation

With $x = 1/T$ and $y = \ln k$, the Arrhenius law is the line $y = \ln A - (E_a/R)\,x$. Its sensitivity to temperature is

$$\frac{d \ln k}{dT} = \frac{E_a}{RT^2},$$

so a small change $\Delta T$ multiplies $k$ by about $\exp(E_a \Delta T/RT^2)$. Symbols: $k$ rate constant, $A$ frequency factor (same units as $k$), $E_a$ activation energy (J/mol), $R$ gas constant, $T$ temperature in kelvin ($T = \theta + 273.15$ for $\theta$ in °C).

## Computational representation

```python
import math
import statistics

R = 8.314  # J mol^-1 K^-1

def rate_ratio(ea_kj: float, t1_c: float, t2_c: float) -> float:
    """k(T2)/k(T1) from the Arrhenius equation; temperatures in degrees Celsius."""
    t1, t2 = t1_c + 273.15, t2_c + 273.15
    return math.exp(ea_kj * 1000 / R * (1 / t1 - 1 / t2))

def boltzmann_fraction(ea_kj: float, t_c: float) -> float:
    """exp(-Ea/RT): the Arrhenius factor, a fraction of encounters energetic enough."""
    return math.exp(-ea_kj * 1000 / (R * (t_c + 273.15)))

def fit_arrhenius(temps_c: list[float], ks: list[float]) -> tuple[float, float]:
    """Ea (kJ/mol) and A from a straight-line fit of ln k against 1/T."""
    x = [1 / (t + 273.15) for t in temps_c]
    slope, intercept = statistics.linear_regression(x, [math.log(k) for k in ks])
    return -slope * R / 1000, math.exp(intercept)

for ea in (25, 50, 100):
    print(ea, "kJ/mol: 25->35 C x", round(rate_ratio(ea, 25, 35), 2),
          "| 37->40 C x", round(rate_ratio(ea, 37, 40), 3),
          "| exp(-Ea/RT) at 37 C =", f"{boltzmann_fraction(ea, 37):.1e}")

# invented rate constants (per s) measured at four temperatures
temps, ks = [20, 25, 30, 37], [0.0125, 0.0200, 0.0316, 0.0580]
ea, a = fit_arrhenius(temps, ks)
print(f"fitted Ea = {ea:.1f} kJ/mol, A = {a:.2e} per s")
```

```text
25 kJ/mol: 25->35 C x 1.39 | 37->40 C x 1.097 | exp(-Ea/RT) at 37 C = 6.2e-05
50 kJ/mol: 25->35 C x 1.92 | 37->40 C x 1.204 | exp(-Ea/RT) at 37 C = 3.8e-09
100 kJ/mol: 25->35 C x 3.7 | 37->40 C x 1.45 | exp(-Ea/RT) at 37 C = 1.4e-17
fitted Ea = 68.3 kJ/mol, A = 1.83e+10 per s
```

Always convert to kelvin and keep $E_a$ and $R$ in the same energy unit (J, not kJ): these two slips account for most wrong Arrhenius results.

## Worked example

> [!example] How much faster at 35 °C than at 25 °C, for $E_a = 50$ kJ/mol?
> 1. Kelvin: $T_1 = 298.15$ K, $T_2 = 308.15$ K.
> 2. $1/T_1 - 1/T_2 = 3.3540 \times 10^{-3} - 3.2452 \times 10^{-3} = 1.088 \times 10^{-4}$ K⁻¹.
> 3. $\ln(k_2/k_1) = (50{,}000/8.314) \times 1.088 \times 10^{-4} = 0.654$.
> 4. $k_2/k_1 = e^{0.654} = 1.92$: the rate almost doubles for a 10 °C rise.
> 5. Check the meaning: only about $4 \times 10^{-9}$ of encounters at 37 °C clear a 50 kJ/mol barrier (table), so a few degrees, which shift that tiny tail fraction, change the rate noticeably.

## Common misconceptions

> [!warning] "An exothermic reaction is fast"
> $\Delta H$ and $E_a$ are independent. A reaction that releases much energy can still have a high barrier and proceed imperceptibly slowly.

> [!warning] "Heating speeds a reaction because molecules have more energy on average"
> The average rises only slightly; what grows is the small high-energy tail above $E_a$, exponentially. That is why a 10 °C rise can double a rate while the absolute temperature rises by about 3 %.

> [!warning] "Temperature always speeds biological processes"
> Only until the machinery fails: enzymes denature above their optimum.[^os6]

## Exercises

> [!question] Exercise 1 (L1)
> A reaction has $E_a = 60$ kJ/mol. By what factor does its rate constant increase from 20 °C to 30 °C?

> [!success]- Solution
> $\ln(k_2/k_1) = (60{,}000/8.314)(1/293.15 - 1/303.15) = 0.812$, so $k_2/k_1 = 2.25$.

> [!question] Exercise 2 (L1)
> A rate doubles between 25 °C and 35 °C. What is $E_a$?

> [!success]- Solution
> $E_a = R \ln 2 / (1/298.15 - 1/308.15) = 8.314 \times 0.693/1.088 \times 10^{-4} = 52.9$ kJ/mol. The "doubling per 10 °C" rule of thumb corresponds to barriers near 50 kJ/mol at room temperature, not to all reactions.

> [!question] Exercise 3 (L1)
> A reaction has $E_a$ (forward) = 80 kJ/mol and $\Delta H = -30$ kJ/mol. Sketch the profile and give $E_a$ (reverse).

> [!success]- Solution
> Products lie 30 kJ/mol below reactants, and the transition state 80 above reactants, hence 110 above products: $E_{a,\mathrm{r}} = E_{a,\mathrm{f}} - \Delta H = 80 + 30 = 110$ kJ/mol.

> [!question] Exercise 4 (L2)
> Why keep a sample on ice? Estimate $k(4\,°\mathrm{C})/k(37\,°\mathrm{C})$ for a degradation reaction with $E_a = 50$ kJ/mol.

> [!success]- Solution
> $\ln(k_4/k_{37}) = (50{,}000/8.314)(1/310.15 - 1/277.15) = -2.31$, so $k_4/k_{37} = 0.099$: about ten times slower. For enzymatic degradation (nucleases, proteases) the slowdown also depends on each enzyme's own temperature profile, but the order of magnitude explains the practice.

> [!question] Exercise 5 (L2, Python)
> With `fit_arrhenius` and the invented data above, predict $k$ at 42 °C, then refit without the 37 °C point. How stable is $E_a$, and when would you distrust the prediction?

> [!success]- Solution
> ```python
> k42 = a * math.exp(-ea * 1000 / (R * (42 + 273.15)))
> print(f"k(42 C) = {k42:.4f} per s")
> ea3, a3 = fit_arrhenius(temps[:3], ks[:3])
> print(f"without 37 C: Ea = {ea3:.1f} kJ/mol")
> # k(42 C) = 0.0884 per s
> # without 37 C: Ea = 68.5 kJ/mol
> ```
>
> The invented data are nearly exact, so $E_a$ barely moves (68.3 versus 68.5 kJ/mol) and a 5 °C extrapolation is reasonable. With real noise over a narrow temperature range the slope is much less certain, and for an enzyme near its optimum the extrapolation can be wrong in sign, because unfolding is not in the model.

## Mastery checklist

- [ ] 1 Recognized: I can define activation energy and transition state and write the Arrhenius equation.
- [ ] 2 Understood: I can read an energy profile (forward and reverse barriers, $\Delta H$) and explain why rate rises exponentially with temperature.
- [ ] 3 Practiced: I can compute rate ratios between two temperatures and extract $E_a$ from an Arrhenius plot, by hand and in Python.
- [ ] 4 Applied: I can analyse temperature-dependent rate data and say when the Arrhenius model stops applying.
- [ ] 5 Explained: I can teach the Boltzmann origin of the exponential factor and the link to transition state theory.

## References

[^chem12]: [[Chemistry 2e (OpenStax)]], ch. 12 "Kinetics" (collision theory, activation energy and the activated complex, the Arrhenius equation and its graphical and two-point forms, the gas constant $R = 8.314$ J mol⁻¹ K⁻¹).
[^os6]: [[Biology 2e (OpenStax)]], ch. 6 "Metabolism" (activation energy; enzymes and the effect of temperature on enzyme activity, including denaturation above the optimum).
