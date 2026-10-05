---
aliases:
  - Le Châtelier's Principle
  - Le Chatelier Principle
  - Equilibrium Shift
  - Principe de Le Chatelier
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Chemical Equilibrium]]"
  - "[[Gibbs Free Energy]]"
  - "[[Enthalpy]]"
related:
  - "[[Van 't Hoff Equation]]"
  - "[[Ligand Binding]]"
  - "[[Cooperativity]]"
  - "[[Buffer Solution]]"
  - "[[Blood]]"
  - "[[Catalysis]]"
  - "[[Ideal Gas Law]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Le Chatelier's Principle

> [!abstract]
> Disturb a system at equilibrium (add or remove a species, compress it, heat it) and it shifts in the direction that partly undoes the disturbance; hemoglobin uses exactly this to load oxygen in the lungs and release it in the tissues.

## Definition

**Le Chatelier's principle**: when a system at equilibrium is subjected to a change (a stress) in concentration, pressure or temperature, the equilibrium shifts in the direction that relieves that stress.[^chem13] Changes in concentration or pressure shift the composition at constant $K$; a change in temperature changes $K$ itself; a catalyst changes neither.[^chem13]

## Why it matters

- **Oxygen transport.** Hemoglobin binds $\mathrm{O_2}$ where its partial pressure is high (lungs) and releases it where it is low (working tissues); acid and $\mathrm{CO_2}$ in tissues push the release further.[^berg] The whole physiology of gas transport is mass action plus [[Cooperativity]].
- **Driving metabolic steps.** Removing a product keeps $Q$ below $K$, so pathways run forward through steps with positive $\Delta G^{\circ\prime}$ ([[Gibbs Free Energy#Worked example]]).
- **pH control.** Breathing out $\mathrm{CO_2}$ shifts the carbonic acid equilibria of blood and keeps its pH stable ([[Buffer Solution]]).
- **Lab practice.** Dilution weakens binding, temperature changes duplex and protein stability, excess reagent drives a reaction to completion: everyday consequences when designing assays, PCR programs or purifications ([[Ligand Binding]], [[Polymerase Chain Reaction]]).

## Core (L1)

### The three stresses

| Change | System's response | $K$ |
|---|---|---|
| Add a reactant, or remove a product | shifts toward products | unchanged |
| Add a product, or remove a reactant | shifts toward reactants | unchanged |
| Decrease volume (raise pressure) of a gas reaction | shifts toward the side with fewer moles of gas | unchanged |
| Raise temperature, exothermic reaction ($\Delta H < 0$) | shifts toward reactants | decreases |
| Raise temperature, endothermic reaction ($\Delta H > 0$) | shifts toward products | increases |
| Add a catalyst | no shift; equilibrium reached faster | unchanged |

All rows follow Chemistry 2e.[^chem13] For temperature, treat heat as a product of an exothermic reaction and as a reactant of an endothermic one: adding heat pushes away from the side where heat appears.[^chem13]

### The reason: Q versus K

Le Chatelier's principle is a mnemonic for the rule of [[Chemical Equilibrium]]: after a disturbance, compare $Q$ with $K$.

- Adding reactant lowers $Q$ below $K$, so $\Delta G = RT\ln(Q/K) < 0$ and the reaction runs forward until $Q = K$ again.
- Heating an exothermic reaction lowers $K$ itself; the old composition now has $Q > K$, and the reaction runs backward.

**Partly, not fully.** The shift relieves the stress only in part. For $\mathrm{A \rightleftharpoons B}$ with $K = 4$ (invented), at equilibrium with 0.2 M A and 0.8 M B, adding 0.5 M A gives a new equilibrium at 0.30 M A and 1.20 M B (computed below): [A] ends higher than before the addition, not back at 0.2 M.

### Bio: hemoglobin in the lungs and in the tissues

Each hemoglobin tetramer binds up to four $\mathrm{O_2}$ (Hb + 4 O₂ ⇌ Hb(O₂)₄, in steps). Its fractional saturation $Y$ rises with the partial pressure $p\mathrm{O_2}$ along an S-shaped curve with half-saturation at $P_{50} = 26$ torr; myoglobin, the single-chain storage protein of muscle, has a hyperbolic curve with $P_{50} = 2$ torr.[^berg] $p\mathrm{O_2}$ is about 100 torr in the lungs and about 20 torr in active tissue.[^berg]

![[hemoglobin-myoglobin-oxygen-saturation.svg]]

- **In the lungs**, high $p\mathrm{O_2}$ (a "reactant" added) pushes binding forward: hemoglobin is about 98 % saturated.
- **In the tissues**, low $p\mathrm{O_2}$ (a "reactant" removed) pulls the equilibrium back: saturation falls to about 32 %, so hemoglobin releases about 65 % of its sites' oxygen. Myoglobin, still 91 % saturated at 20 torr, would release only about 7 %.
- **The Bohr effect** adds a second stress. $\mathrm{H^+}$ and $\mathrm{CO_2}$, abundant in metabolically active tissue, bind hemoglobin preferentially in its deoxygenated form and lower its oxygen affinity, so even more $\mathrm{O_2}$ is released where it is needed; in the lungs, $\mathrm{CO_2}$ leaves and affinity rises again.[^berg]

The percentages come from the Hill model computed below, with $P_{50}$ and the Hill coefficient 2.8 from Berg;[^berg] the S shape itself (cooperativity) is explained in [[Cooperativity]].

## Deeper (L2)

### Pressure, quantitatively

For an ideal gas mixture at total pressure $P$, partial pressures are $p_i = x_i P$ (mole fractions $x_i$), so

$$K_P = \prod_i (x_i P)^{\nu_i} = K_x\, P^{\Delta n}, \qquad K_x = K_P\, P^{-\Delta n},$$

with $\Delta n = \sum_i \nu_i$ the change in moles of gas and $P$ in bar. If $\Delta n < 0$ (fewer gas molecules on the product side), raising $P$ raises $K_x$: the mixture shifts toward products. If $\Delta n = 0$, pressure has no effect. Adding an inert gas at constant volume leaves every partial pressure, hence $Q$, unchanged: no shift.

### Dilution in solution

Dilution acts like a pressure change: it favors the side with more dissolved particles. For unbinding $\mathrm{PL \rightleftharpoons P + L}$, $Q = [\mathrm{P}][\mathrm{L}]/[\mathrm{PL}]$ falls tenfold when the solution is diluted tenfold, so the complex dissociates (Exercise 4). Assays that dilute a sample before measuring a complex underestimate it unless binding is much tighter than the concentrations used.

### Temperature, quantitatively

How much $K$ changes is set by $\Delta H^\circ$: assuming it constant, $\ln(K_2/K_1) = -\dfrac{\Delta H^\circ}{R}\left(\dfrac{1}{T_2} - \dfrac{1}{T_1}\right)$, the integrated [[Van 't Hoff Equation]]. An exothermic reaction with $\Delta H^\circ = -50$ kJ/mol and $K = 100$ at 25 °C (invented) has $K \approx 46$ at 37 °C. DNA duplexes melt on heating ([[DNA#Deeper (L2)]]), which by the same rule means that annealing is exothermic; PCR exploits this by cycling between a denaturing and an annealing temperature ([[Polymerase Chain Reaction]]).

## Advanced (L3)

- **Le Chatelier can mislead.** The principle is a heuristic; the Q-versus-K calculation is the rule. Adding $\mathrm{N_2}$ to an equilibrium mixture of $\mathrm{N_2 + 3\,H_2 \rightleftharpoons 2\,NH_3}$ at constant total pressure sounds like "add reactant, shift forward". But $Q = x_{\mathrm{NH_3}}^2/(x_{\mathrm{N_2}} x_{\mathrm{H_2}}^3) \cdot P^{-2}$ depends on mole fractions: adding $dn$ of $\mathrm{N_2}$ changes $\ln Q$ by $dn\,(2/n_{\text{tot}} - 1/n_{\mathrm{N_2}})$, which is positive when $x_{\mathrm{N_2}} > 1/2$. With nitrogen already in majority, adding more shifts the reaction **backward**.
- **Biology tunes the stress, not just the response.** Hemoglobin couples $\mathrm{O_2}$ binding to $\mathrm{H^+}$, $\mathrm{CO_2}$ and 2,3-bisphosphoglycerate binding, each of which shifts the oxygen equilibrium;[^berg] these are linked equilibria, where the binding of one ligand changes the effective constant for another ([[Allosteric Regulation]]). Cooperativity makes the response steep, so a modest pressure difference between lungs and tissues moves a large fraction of oxygen (Exercise 5).
- **Open systems.** A cell is not a closed flask at equilibrium; its "disturbances" are continuous fluxes. Near-equilibrium steps of a pathway still respond to concentration changes in the direction the principle predicts, which is how product removal propagates backward along a pathway ([[Chemical Equilibrium#Advanced (L3)]], [[Metabolism]]).

## Mathematical representation

- At equilibrium $Q = K$. After a disturbance that changes $Q$ to $Q'$ (concentrations, pressure) or $K$ to $K'$ (temperature): net reaction forward if $Q'/K' < 1$, backward if $> 1$, since $\Delta G = RT\ln(Q/K)$.
- **Direction of the response.** Along the extent of reaction $x$, $d\ln Q/dx = \sum_i \nu_i^2/c_i > 0$ ([[Chemical Equilibrium#Mathematical representation]]): the reaction moves $\ln Q$ back toward $\ln K$, and the new equilibrium lies between the disturbed state and the old one for the disturbed species (partial compensation).
- **Temperature.** $\dfrac{d\ln K}{dT} = \dfrac{\Delta H^\circ}{RT^2}$ ([[Van 't Hoff Equation]]): the sign of $\Delta H^\circ$ fixes the direction.
- **Hill model of binding.** $Y(p) = \dfrac{p^n}{P_{50}^n + p^n}$, where $p$ is the ligand partial pressure or concentration, $P_{50}$ the half-saturation value and $n$ the Hill coefficient ($n = 1$: hyperbolic, no cooperativity). It summarizes, but does not explain, cooperative binding ([[Cooperativity]]).

## Computational representation

```python
import math

R = 8.314462618e-3   # kJ/(mol K), CODATA


def shift_a_to_b(a: float, b: float, k: float) -> tuple[float, float]:
    """Re-equilibrate A <-> B (K = [B]/[A]) after a disturbance: the total is conserved."""
    total = a + b
    return total / (1 + k), total * k / (1 + k)


def k_at(k1: float, dh: float, t1: float, t2: float) -> float:
    """K at T2 from K at T1, assuming constant dH (kJ/mol): integrated van 't Hoff equation."""
    return k1 * math.exp(-dh / R * (1 / t2 - 1 / t1))


# Concentration: A <-> B, K = 4 (invented), at equilibrium A = 0.2 M, B = 0.8 M; add 0.5 M A
a, b = shift_a_to_b(0.2 + 0.5, 0.8, 4.0)
print(f"right after adding A: Q = {0.8 / 0.7:.2f} < K = 4; new equilibrium A = {a:.2f} M, B = {b:.2f} M")

# Temperature: exothermic reaction, dH = -50 kJ/mol, K = 100 at 298 K (invented)
for t in (298.15, 310.15, 330.15):
    print(f"T = {t:.2f} K  K = {k_at(100, -50, 298.15, t):.1f}")
```

```text
right after adding A: Q = 1.14 < K = 4; new equilibrium A = 0.30 M, B = 1.20 M
T = 298.15 K  K = 100.0
T = 310.15 K  K = 45.8
T = 330.15 K  K = 14.2
```

The gas constant is the CODATA value.[^nist] Simulating a disturbance means solving the equilibrium again with the new totals (or the new $K$); the general solver is in [[Chemical Equilibrium#Computational representation]].

## Worked example

> [!example] Oxygen delivery by hemoglobin versus myoglobin
> Model each protein with the Hill equation, using $P_{50} = 26$ torr and $n = 2.8$ for hemoglobin, $P_{50} = 2$ torr and $n = 1$ for myoglobin, $p\mathrm{O_2}$ = 100 torr in the lungs and 20 torr in active tissue.[^berg]
> 1. **Hemoglobin, lungs**: $Y = 100^{2.8}/(26^{2.8} + 100^{2.8}) = 0.978$.
> 2. **Hemoglobin, tissues**: $Y = 20^{2.8}/(26^{2.8} + 20^{2.8}) = 0.324$. Delivered: $0.978 - 0.324 = 0.653$ of the sites.
> 3. **Myoglobin**: $Y = 100/102 = 0.980$ in the lungs and $20/22 = 0.909$ in tissues; delivered 0.071.
> 4. **Read it**: both proteins respond to the same "remove a reactant" stress, but only hemoglobin's response is large over the 100 → 20 torr range: high $P_{50}$ places the steep part of its curve between lung and tissue pressures, and cooperativity makes it steep. Myoglobin's job is the opposite: to hold oxygen in muscle.

## Common misconceptions

> [!warning] "The shift restores the original concentrations"
> The response is partial. After adding A, [A] settles above its old value; only $Q/K$ returns to 1.

> [!warning] "Changing concentration or pressure changes K"
> Only temperature changes $K$. Concentration and pressure change $Q$, and the composition adjusts at constant $K$.[^chem13]

> [!warning] "A catalyst shifts the equilibrium toward products"
> A catalyst speeds both directions equally and leaves the equilibrium composition unchanged ([[Catalysis]]).[^chem13]

> [!warning] "Adding any gas raises the pressure, so the equilibrium shifts"
> An inert gas added at constant volume changes no partial pressure, hence no $Q$: no shift. What matters is the change in the terms of $Q$.

## Exercises

> [!question] Exercise 1 (L1)
> For the exothermic synthesis $\mathrm{N_2(g) + 3\,H_2(g) \rightleftharpoons 2\,NH_3(g)}$, predict the shift after: (a) adding $\mathrm{H_2}$; (b) removing $\mathrm{NH_3}$; (c) halving the volume; (d) heating; (e) adding an iron catalyst.

> [!success]- Solution
> (a) Toward $\mathrm{NH_3}$. (b) Toward $\mathrm{NH_3}$. (c) Toward $\mathrm{NH_3}$: 4 moles of gas become 2. (d) Toward $\mathrm{N_2}$ and $\mathrm{H_2}$, and $K$ decreases (heat is a product). (e) No shift; equilibrium is reached faster. Industry compromises: high pressure for yield, moderate temperature and a catalyst for speed.[^chem13]

> [!question] Exercise 2 (L1)
> Explain in terms of Le Chatelier's principle why hemoglobin loads oxygen in the lungs and unloads it in the tissues, and why an active muscle (acidic, rich in $\mathrm{CO_2}$) receives more oxygen than a resting one.

> [!success]- Solution
> $\mathrm{Hb + O_2 \rightleftharpoons HbO_2}$ (per site): high $p\mathrm{O_2}$ in the lungs drives binding; low $p\mathrm{O_2}$ in tissues drives release. In active muscle $p\mathrm{O_2}$ is lower still and $\mathrm{H^+}$ and $\mathrm{CO_2}$, which bind the deoxygenated form preferentially, pull the equilibrium further toward release (Bohr effect).[^berg]

> [!question] Exercise 3 (L2)
> $\mathrm{A \rightleftharpoons B}$ with $K = 4$ (invented) is at equilibrium with 0.2 M A and 0.8 M B. Compute the new equilibrium after adding 0.5 M A, and the fraction of the added A that is converted.

> [!success]- Solution
> Total 1.5 M, so A = 1.5/5 = 0.30 M and B = 1.20 M. Of the 0.5 M added, 0.4 M became B (80 % = $K/(1+K)$): the shift absorbs most, but not all, of the disturbance.

> [!question] Exercise 4 (L2)
> A protein and its ligand are mixed at 10 µM each, with $K_d = 1$ µM (invented). The sample is diluted tenfold, then tenfold again. Compute the fraction of protein in the complex at each step with the exact quadratic $[\mathrm{PL}] = \frac{s - \sqrt{s^2 - 4P_0L_0}}{2}$, $s = P_0 + L_0 + K_d$.

> [!success]- Solution
> 10 µM: 0.730; 1 µM: 0.382; 0.1 µM: 0.084. Each dilution lowers $Q = [\mathrm{P}][\mathrm{L}]/[\mathrm{PL}]$ below $K_d$ and the complex dissociates: one side has two particles, the other one. A pull-down or gel-shift experiment that dilutes a weak complex will lose it.

> [!question] Exercise 5 (L3, Python)
> With the Hill model of the Worked example, compute the fraction of sites unloaded between lungs (100 torr) and tissues (20 torr) for hemoglobin and myoglobin. Then suppose acid and $\mathrm{CO_2}$ in the tissue raise hemoglobin's $P_{50}$ to 35 torr (an illustrative value) there but not in the lungs. How much more oxygen is delivered?

> [!success]- Solution
> ```python
> def hill(p: float, p50: float, n: float) -> float:
>     """Fractional saturation Y = p^n / (P50^n + p^n), p in torr."""
>     return p ** n / (p50 ** n + p ** n)
>
> LUNGS, TISSUE = 100, 20   # torr
> for name, p50, n in (("hemoglobin", 26, 2.8), ("myoglobin", 2, 1)):
>     yl, yt = hill(LUNGS, p50, n), hill(TISSUE, p50, n)
>     print(f"{name:10s} lungs {yl:.3f}  tissues {yt:.3f}  delivered {yl - yt:.3f}")
> yt_bohr = hill(TISSUE, 35, 2.8)   # illustrative right shift in acidic, CO2-rich tissue
> print(f"with P50 = 35 torr in tissues: {yt_bohr:.3f}, delivered {hill(LUNGS, 26, 2.8) - yt_bohr:.3f}")
> ```
> ```text
> hemoglobin lungs 0.978  tissues 0.324  delivered 0.653
> myoglobin  lungs 0.980  tissues 0.909  delivered 0.071
> with P50 = 35 torr in tissues: 0.173, delivered 0.805
> ```
> The Bohr shift raises delivery from 65 % to 80 % of the sites without changing loading in the lungs: a second equilibrium ($\mathrm{H^+}$ and $\mathrm{CO_2}$ binding) modulates the first exactly where oxygen is consumed.

## Mastery checklist

- [ ] 1 Recognized: I can state the principle and the effect of concentration, pressure, temperature and catalysts.
- [ ] 2 Understood: I can derive each prediction from $Q$ versus $K$, and explain why only temperature changes $K$.
- [ ] 3 Practiced: I can compute the new equilibrium after a disturbance and the effect of temperature on $K$ in Python.
- [ ] 4 Applied: I can explain oxygen loading and unloading by hemoglobin, the Bohr effect, and dilution artifacts in binding assays with numbers.
- [ ] 5 Explained: I can teach when the principle fails (the nitrogen example) and how linked equilibria let proteins respond to several signals.

## References

[^chem13]: [[Chemistry 2e (OpenStax)]], ch. 13 "Fundamental Equilibrium Concepts" (Le Châtelier's principle: effects of changes in concentration, pressure or volume, and temperature; catalysts; the Haber process).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of hemoglobin and myoglobin (cooperative oxygen binding, $P_{50}$ of 26 torr for hemoglobin and 2 torr for myoglobin, oxygen partial pressures of about 100 torr in the lungs and 20 torr in active tissue, Hill coefficient, the Bohr effect of $\mathrm{H^+}$ and $\mathrm{CO_2}$, 2,3-bisphosphoglycerate).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA recommended value of the molar gas constant $R$.
