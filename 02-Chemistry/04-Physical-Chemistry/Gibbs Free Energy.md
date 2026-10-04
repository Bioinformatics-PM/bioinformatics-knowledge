---
aliases:
  - Free Energy
  - Gibbs Energy
  - ΔG
  - Free Enthalpy
  - Enthalpie libre
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Enthalpy]]"
  - "[[Thermodynamic Entropy]]"
  - "[[Laws of Thermodynamics]]"
  - "[[Logarithm]]"
  - "[[Exponential Function]]"
related:
  - "[[Chemical Equilibrium]]"
  - "[[Le Chatelier's Principle]]"
  - "[[Chemical Potential]]"
  - "[[ATP]]"
  - "[[Metabolism]]"
  - "[[Helmholtz Free Energy]]"
  - "[[Boltzmann Distribution]]"
  - "[[Binding Free Energy]]"
  - "[[Free Energy Landscape]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Zuker 1981 - Optimal Computer Folding of Large RNA Sequences]]"
  - "[[Untergasser 2012 - Primer3 New Capabilities and Interfaces]]"
---

# Gibbs Free Energy

> [!abstract]
> The Gibbs free energy change ΔG tells whether a process can run by itself at constant temperature and pressure: it can if ΔG is negative, and ΔG depends both on the reaction (ΔG°) and on how far the current mixture is from equilibrium.

## Definition

The **Gibbs free energy** of a system is $G = H - TS$, where $H$ is its [[Enthalpy|enthalpy]], $S$ its [[Thermodynamic Entropy|entropy]] and $T$ the absolute temperature. At constant temperature and pressure a process is **spontaneous** when $\Delta G = \Delta H - T\Delta S < 0$, nonspontaneous when $\Delta G > 0$, and at **equilibrium** when $\Delta G = 0$.[^chem16][^5111] $\Delta G$ is the energy available to do work during a reaction at constant temperature and pressure.[^lehninger]

## Why it matters

- **The common currency of biology.** Folding stability, binding affinity and the direction of a metabolic step are all free-energy differences, and $\Delta G^\circ = -RT\ln K$ turns them into measurable equilibrium constants ([[Chemical Equilibrium]], [[Ligand Binding]]).
- **RNA structure prediction.** The classic algorithm of Zuker and Stiegler finds the secondary structure of **minimum free energy**, summing stacking and loop contributions with [[Dynamic Programming|dynamic programming]];[^zuker] RNA folding tools still work this way ([[RNA Secondary Structure Prediction]]).
- **Primer design.** Primer3 uses thermodynamic models to predict melting temperatures and to avoid hairpins and primer dimers,[^primer3] which are free-energy calculations ([[Polymerase Chain Reaction]]).
- **Mutation effects.** The effect of a missense variant on stability or binding is a $\Delta\Delta G$ (mutant minus wild type), the quantity that stability predictors estimate ([[Missense Mutation]], [[Binding Free Energy]]).
- **Bioenergetics.** [[ATP]] hydrolysis, the proton gradient of the [[Mitochondrion]] and transport across membranes are compared on one scale, kJ/mol of free energy.

## Core (L1)

### Two tendencies in one number

A reaction is favored by releasing heat ($\Delta H < 0$) and by increasing entropy ($\Delta S > 0$). $\Delta G = \Delta H - T\Delta S$ weighs the two, with temperature setting the weight of entropy.[^chem16]

| $\Delta H$ | $\Delta S$ | $\Delta G = \Delta H - T\Delta S$ | Spontaneous |
|---|---|---|---|
| − | + | always − | at every temperature |
| + | − | always + | never (the reverse is) |
| − | − | − at low $T$ | below $T = \Delta H/\Delta S$ |
| + | + | − at high $T$ | above $T = \Delta H/\Delta S$ |

The table is from the signs alone;[^chem16] the crossover temperature $T = \Delta H/\Delta S$ assumes both are constant.

**Ice and water.** Melting has $\Delta H_{\text{fus}} = +6.01$ kJ/mol[^chem] and $\Delta S_{\text{fus}} = 6.01/273.15 = 22.0$ J mol⁻¹ K⁻¹ (equilibrium at 0 °C). At −10 °C, $\Delta G = 6.01 - 263.15 \times 0.0220 = +0.22$ kJ/mol: water freezes. At +10 °C, $\Delta G = -0.22$ kJ/mol: ice melts. Same $\Delta H$ and $\Delta S$, opposite verdicts.

### ΔG depends on composition

$\Delta G$ is not a fixed property of a reaction: it depends on the amounts present. For $a\mathrm{A} + b\mathrm{B} \rightleftharpoons c\mathrm{C} + d\mathrm{D}$,[^chem16]

$$\Delta G = \Delta G^\circ + RT\ln Q, \qquad Q = \frac{[\mathrm{C}]^c[\mathrm{D}]^d}{[\mathrm{A}]^a[\mathrm{B}]^b},$$

where $\Delta G^\circ$ is the **standard** free energy change (every species in its standard state: 1 M for solutes, 1 bar for gases), $Q$ the **reaction quotient** of the current mixture, $R$ the gas constant and $T$ in kelvin.[^chem16] With $R = 8.314\,462\,618$ J mol⁻¹ K⁻¹,[^nist] $RT = 2.48$ kJ/mol at 25 °C and 2.58 kJ/mol at 37 °C.

- With little product ($Q$ small), $\ln Q \ll 0$ and the reaction runs forward even if $\Delta G^\circ > 0$.
- As products accumulate, $Q$ rises and $\Delta G$ climbs toward 0. At equilibrium $\Delta G = 0$ and $Q = K$, so $\Delta G^\circ = -RT\ln K$.[^chem16] See [[Chemical Equilibrium]].

![[gibbs-energy-reaction-extent.svg]]

### The biochemical standard state

The chemist's standard state puts $\mathrm{H^+}$ at 1 M (pH 0), absurd for a cell. Biochemistry uses a **transformed** standard state, written $\Delta G^{\circ\prime}$ (Berg) or $\Delta G'^\circ$ (Lehninger): pH 7, other solutes at 1 M, 25 °C, and water (55.5 M) set to activity 1 so that it disappears from $Q$; Lehninger also fixes free $\mathrm{Mg^{2+}}$ at 1 mM.[^berg][^lehninger] Equilibrium constants defined this way are written $K'$ (or $K'_{\text{eq}}$). Tables of metabolic reactions, such as $\Delta G^{\circ\prime} = -30.5$ kJ/mol for ATP hydrolysis, use this convention ([[ATP]]).[^berg]

### Spontaneous does not mean fast

$\Delta G$ says whether a reaction **can** happen, not how fast: the rate is set by the activation barrier ([[Activation Energy]], [[Catalysis]]).[^berg] Glucose in air has a very negative $\Delta G$ of oxidation and yet survives on a shelf.

## Deeper (L2)

### Reading ΔG°′ and ΔG in metabolism

A positive $\Delta G^{\circ\prime}$ does not forbid a step in the cell. In glycolysis, dihydroxyacetone phosphate (DHAP) is isomerized to glyceraldehyde 3-phosphate (GAP) with $\Delta G^{\circ\prime} = +7.5$ kJ/mol: at equilibrium DHAP dominates, but the cell keeps GAP low by consuming it in the next steps, so $Q < K'$ and $\Delta G < 0$ (Worked example).[^berg] What decides direction in vivo is the actual $\Delta G$, set by concentrations ([[Metabolism]]).

### Coupling is addition

$G$ is a state function, so free energies of reactions that share intermediates add: an unfavorable step ($\Delta G_1 > 0$) runs when coupled to a favorable one with $\Delta G_1 + \Delta G_2 < 0$.[^berg] ATP hydrolysis is the standard partner; the [[ATP]] note works out the numbers. Since $K = e^{-\Delta G^\circ/RT}$, adding free energies multiplies equilibrium constants.

### Converting between ΔG° and ΔG°′

For a reaction that releases $n$ protons, $Q$ contains $[\mathrm{H^+}]^n$. Fixing $[\mathrm{H^+}] = 10^{-7}$ M in the transformed standard state gives, at 25 °C,

$$\Delta G^{\circ\prime} = \Delta G^\circ + nRT\ln(10^{-7}) = \Delta G^\circ - 39.96\,n \text{ kJ/mol}.$$

A reaction that releases a proton is about 40 kJ/mol more favorable at pH 7 than at pH 0 (Exercise 4); one that consumes a proton is less favorable. Reactions without $\mathrm{H^+}$ (or water) have $\Delta G^{\circ\prime} = \Delta G^\circ$.

### One scale for all processes

The same logic applies to anything with a free energy: moving a solute across a membrane from concentration $c_1$ to $c_2$ costs $RT\ln(c_2/c_1)$ (plus an electrical term for ions, [[Membrane Potential]]); the proton-motive force of the [[Mitochondrion]] is such a $\Delta G$; and each tenfold change in $Q$ shifts $\Delta G$ by $RT\ln 10 = 5.71$ kJ/mol at 25 °C (5.94 at 37 °C). This "5.7 kJ/mol per factor of 10" is the most useful number of the topic.

## Advanced (L3)

- **G is minimized.** At constant $T$ and $P$, a closed system evolves until $G$ reaches its minimum. Plotting $G$ against the extent of reaction $\xi$ (figure above) shows why equilibrium is a mixture: the mixing term $RT\sum x_i \ln x_i$ makes the curve dip below the straight line between pure reactants and pure products. The slope $\partial G/\partial \xi$ is $\Delta G$; it is zero at the minimum, which is $Q = K$ (Mathematical representation). Physical Biology of the Cell treats equilibrium in cells as such a free-energy minimization.[^pboc]
- **Free energy is a log probability.** For two states A and B in equilibrium, $\Delta G^\circ = -RT\ln([\mathrm{B}]/[\mathrm{A}])$: a free-energy difference is a population ratio on a log scale, the macroscopic face of the [[Boltzmann Distribution]].[^pbocsm] A protein that is 99 % folded has $\Delta G_{\text{unfold}} = RT\ln 99 \approx 11$ kJ/mol at 25 °C; folding stability, binding affinity and RNA structure probabilities are all populations in disguise ([[Free Energy Landscape]]).
- **Additive energy models.** Zuker's algorithm scores an RNA structure as a sum of stacking and loop free energies and finds the minimum by dynamic programming;[^zuker] nearest-neighbor models of duplex stability use the same additivity for primers and probes.[^primer3] Additivity is an approximation: it ignores long-range interactions and assumes that the parameters, measured on small model systems, transfer.
- **Temperature dependence.** $\Delta H$ and $\Delta S$ themselves vary with $T$ through the heat-capacity change ([[Enthalpy#Deeper (L2)]]); the exact temperature dependence of $K$ is the [[Van 't Hoff Equation]]. A two-state protein whose $\Delta G_{\text{unfold}}$ crosses zero at $T_m$ melts over a narrow range (Exercise 5), because $\Delta H$ is large: the signature of a cooperative transition ([[Helix-Coil Transition]]).

## Mathematical representation

- $G = H - TS$. Its differential for a mixture of species $i$ with amounts $n_i$ is $dG = V\,dP - S\,dT + \sum_i \mu_i\,dn_i$, where $\mu_i = (\partial G/\partial n_i)_{T,P,n_{j\ne i}}$ is the **chemical potential** of species $i$ ([[Chemical Potential]]).
- A reaction $\sum_i \nu_i X_i = 0$ (stoichiometric coefficients $\nu_i$, positive for products) advancing by $d\xi$ changes $n_i$ by $\nu_i\,d\xi$. At constant $T$ and $P$:
$$\Delta_r G \equiv \left(\frac{\partial G}{\partial \xi}\right)_{T,P} = \sum_i \nu_i \mu_i .$$
- With $\mu_i = \mu_i^\circ + RT\ln a_i$ ($a_i$: activity, approximately $[X_i]/1\,\mathrm{M}$ for dilute solutes, $p_i/1\,\mathrm{bar}$ for gases, 1 for solvent and pure solids):
$$\Delta_r G = \Delta_r G^\circ + RT\ln Q, \qquad Q = \prod_i a_i^{\nu_i}, \qquad \Delta_r G^\circ = \sum_i \nu_i \mu_i^\circ .$$
- The minimum of $G$ has $\Delta_r G = 0$, hence $Q_{\text{eq}} = K$ and $\Delta_r G^\circ = -RT\ln K$, so $\Delta_r G = RT\ln(Q/K)$: the sign of $\Delta_r G$ is the sign of $\ln(Q/K)$.
- Spontaneity: $\Delta G < 0$ ⇔ $Q < K$ (forward); $\Delta G > 0$ ⇔ $Q > K$ (backward).

## Computational representation

A free-energy calculator needs one constant, $R$, which is exact since the 2019 SI ($R = N_A k$).[^nist] Keep energies in kJ/mol and $R$ in kJ mol⁻¹ K⁻¹ so units never mix:

```python
import math

R = 8.314462618e-3          # molar gas constant, kJ/(mol K), CODATA (exact)
T25, T37 = 298.15, 310.15   # K


def delta_g(dh: float, ds: float, t: float) -> float:
    """dG = dH - T dS, with dH in kJ/mol and dS in kJ/(mol K)."""
    return dh - t * ds


def delta_g_actual(dg0: float, q: float, t: float = T25) -> float:
    """dG = dG0 + RT ln Q (Q dimensionless, from activities or molar concentrations)."""
    return dg0 + R * t * math.log(q)


def k_from_dg0(dg0: float, t: float = T25) -> float:
    """K = exp(-dG0 / RT)."""
    return math.exp(-dg0 / (R * t))


def dg0_from_k(k: float, t: float = T25) -> float:
    """dG0 = -RT ln K."""
    return -R * t * math.log(k)


# Ethene hydrogenation from Appendix G data: dHf (kJ/mol) and S0 (J/(mol K))
dh = -84.0 - 52.4
ds = (229.2 - 219.3 - 130.7) / 1000
print(f"dH = {dh:.1f} kJ/mol, dS = {ds * 1000:.1f} J/(mol K)")
print(f"dG(298 K) = {delta_g(dh, ds, T25):.1f} kJ/mol; from dGf: {-32.0 - 68.4:.1f} kJ/mol")
print(f"dG changes sign at T = {dh / ds:.0f} K")

# DHAP -> GAP, dG0' = +7.5 kJ/mol; concentrations are illustrative
dg0p = 7.5
print(f"K' = {k_from_dg0(dg0p):.4f}, check dG0' = {dg0_from_k(k_from_dg0(dg0p)):.2f}")
q = 3e-6 / 2e-4
print(f"Q = {q:.3f}, dG = {delta_g_actual(dg0p, q):.1f} kJ/mol")
print(f"RT ln 10 = {R * T25 * math.log(10):.2f} (25 C), {R * T37 * math.log(10):.2f} (37 C) kJ/mol")
```

```text
dH = -136.4 kJ/mol, dS = -120.8 J/(mol K)
dG(298 K) = -100.4 kJ/mol; from dGf: -100.4 kJ/mol
dG changes sign at T = 1129 K
K' = 0.0485, check dG0' = 7.50
Q = 0.015, dG = -2.9 kJ/mol
RT ln 10 = 5.71 (25 C), 5.94 (37 C) kJ/mol
```

The thermodynamic data ($\Delta H_f^\circ$, $S^\circ$ and $\Delta G_f^\circ$ of $\mathrm{C_2H_4}$, $\mathrm{C_2H_6}$ and $\mathrm{H_2}$) come from Chemistry 2e;[^appg] computing $\Delta G$ through $\Delta H - T\Delta S$ and through formation free energies gives the same $-100.4$ kJ/mol, a useful consistency check. Hydrogenation loses a gas molecule ($\Delta S < 0$), so it stops being favorable above about 1130 K.

## Worked example

> [!example] Why DHAP → GAP runs forward in glycolysis
> Data: $\Delta G^{\circ\prime} = +7.5$ kJ/mol at 25 °C.[^berg] Concentrations, illustrative of a cell: [DHAP] = 2 × 10⁻⁴ M, [GAP] = 3 × 10⁻⁶ M.
> 1. **Equilibrium constant**: $K' = e^{-7.5/2.479} = 0.0485$. At equilibrium [GAP]/[DHAP] ≈ 0.05: about 95 % of the triose phosphate is DHAP.
> 2. **Current quotient**: $Q = 3 \times 10^{-6} / 2 \times 10^{-4} = 0.015$, below $K'$.
> 3. **Actual free energy**: $\Delta G = 7.5 + 2.479 \ln 0.015 = 7.5 - 10.4 = -2.9$ kJ/mol.
> 4. **Read it**: the standard value says "backward", the actual value says "forward". The next enzyme consumes GAP and keeps $Q < K'$, so the isomerization keeps running toward GAP, close to equilibrium.

## Common misconceptions

> [!warning] "A negative ΔG means a fast reaction"
> $\Delta G$ is about direction and extent, not rate. A reaction with very negative $\Delta G$ can be immeasurably slow without a catalyst; enzymes change the rate, never $\Delta G$.[^berg]

> [!warning] "A positive ΔG°′ means the reaction cannot happen in cells"
> $\Delta G^{\circ\prime}$ describes 1 M of everything at pH 7. The actual $\Delta G = \Delta G^{\circ\prime} + RT\ln Q$ can be negative when products are kept low, as for DHAP → GAP.[^berg]

> [!warning] "ΔG = 0 means nothing is happening"
> At equilibrium the forward and reverse reactions continue at equal rates; only the net change stops ([[Chemical Equilibrium]]).

> [!warning] "ΔG° is the free energy change of my reaction"
> $\Delta G^\circ$ refers to the standard state, which a real mixture rarely matches. It fixes $K$; the actual $\Delta G$ also needs $Q$.

## Exercises

> [!question] Exercise 1 (L1)
> Predict at which temperatures each process is spontaneous: (a) $\Delta H < 0$, $\Delta S > 0$; (b) $\Delta H > 0$, $\Delta S > 0$; (c) $\Delta H < 0$, $\Delta S < 0$. Which case is the hydrogenation of ethene?

> [!success]- Solution
> (a) At all temperatures. (b) Only above $\Delta H/\Delta S$. (c) Only below $\Delta H/\Delta S$. Hydrogenation is case (c): $\Delta H = -136.4$ kJ/mol, $\Delta S = -120.8$ J mol⁻¹ K⁻¹, spontaneous below about 1129 K.

> [!question] Exercise 2 (L1)
> Using $\Delta H_{\text{fus}} = 6.01$ kJ/mol and $\Delta S_{\text{fus}} = 22.0$ J mol⁻¹ K⁻¹, compute $\Delta G$ of melting at −10, 0 and +10 °C and interpret each sign.

> [!success]- Solution
> $\Delta G = 6.01 - T \times 0.0220$: +0.22 kJ/mol at 263.15 K (ice is stable), 0 at 273.15 K (ice and water coexist), −0.22 kJ/mol at 283.15 K (ice melts). The entropy term grows with $T$ and overtakes the enthalpy cost exactly at the melting point.

> [!question] Exercise 3 (L2)
> For DHAP → GAP ($\Delta G^{\circ\prime} = +7.5$ kJ/mol, 25 °C), what [GAP]/[DHAP] ratio makes $\Delta G = 0$? What ratio makes $\Delta G = -5$ kJ/mol?

> [!success]- Solution
> $\Delta G = 0$ when $Q = K' = e^{-7.5/RT} = 0.0485$. For $\Delta G = -5$: $Q = K' e^{-5/RT} = 0.0485 \times e^{-2.017} = 0.0065$. The cell must keep GAP about 150 times below DHAP for that driving force; every factor of 10 in $Q$ is worth 5.7 kJ/mol.

> [!question] Exercise 4 (L2)
> A reaction $\mathrm{A \to B + H^+}$ has $\Delta G^\circ = +10.0$ kJ/mol at 25 °C (invented values). Compute $\Delta G^{\circ\prime}$. Is the reaction more or less favorable at pH 7 than in the chemist's standard state, and why?

> [!success]- Solution
> $\Delta G^{\circ\prime} = \Delta G^\circ + RT\ln(10^{-7}) = 10.0 - 39.96 = -30.0$ kJ/mol. Much more favorable: at pH 7 the product $\mathrm{H^+}$ is $10^7$ times more dilute than in the standard state, which pulls the reaction forward (a [[Le Chatelier's Principle|Le Chatelier]] effect written as a free energy).

> [!question] Exercise 5 (L3, Python)
> A two-state protein (invented values) unfolds with $\Delta H_u = 300$ kJ/mol and melting temperature $T_m = 330$ K, where $\Delta G_u = 0$. Ignoring $\Delta C_P$, compute $\Delta G_u$ and the unfolded fraction $f = K/(1+K)$ at 298, 320, 330 and 340 K, using `delta_g` and `k_from_dg0`.

> [!success]- Solution
> ```python
> dh_u, tm = 300.0, 330.0             # invented two-state protein
> ds_u = dh_u / tm                    # dG_u(Tm) = 0
> for t in (298.0, 320.0, 330.0, 340.0):
>     dg = delta_g(dh_u, ds_u, t)
>     k = k_from_dg0(dg, t)
>     print(f"T = {t:.0f} K  dG_unfold = {dg:6.1f} kJ/mol  fraction unfolded = {k / (1 + k):.3g}")
> ```
> ```text
> T = 298 K  dG_unfold =   29.1 kJ/mol  fraction unfolded = 7.96e-06
> T = 320 K  dG_unfold =    9.1 kJ/mol  fraction unfolded = 0.0318
> T = 330 K  dG_unfold =    0.0 kJ/mol  fraction unfolded = 0.5
> T = 340 K  dG_unfold =   -9.1 kJ/mol  fraction unfolded = 0.961
> ```
> A stability of only 29 kJ/mol at room temperature keeps the protein unfolded less than once in $10^5$ molecules, and the whole transition happens within about 20 K: a large $\Delta H$ makes $\Delta G$ change quickly with $T$, so the melt is sharp.

> [!question] Exercise 6 (L3, Python)
> Three conformations A, B, C of a molecule have free energies 0, 2.5 and 5.0 kJ/mol (invented). Compute their equilibrium populations at 37 °C with $p_i \propto e^{-G_i/RT}$, and check that $\Delta G^\circ_{A \to B} = -RT\ln(p_B/p_A)$.

> [!success]- Solution
> ```python
> levels = {"A": 0.0, "B": 2.5, "C": 5.0}  # invented free energies, kJ/mol
> w = {s: math.exp(-g / (R * T37)) for s, g in levels.items()}
> z = sum(w.values())
> print({s: round(v / z, 3) for s, v in w.items()})
> ```
> Output: `{'A': 0.657, 'B': 0.249, 'C': 0.094}`. $-RT\ln(0.249/0.657) = -2.579 \times (-0.970) = 2.5$ kJ/mol, as required. A conformation 2.5 kJ/mol (about $RT$) above the ground state is still populated a quarter of the time: in cells, states within a few $RT$ of each other all matter ([[Boltzmann Distribution]]).

## Mastery checklist

- [ ] 1 Recognized: I can state $\Delta G = \Delta H - T\Delta S$ and the sign rule for spontaneity.
- [ ] 2 Understood: I can explain the difference between $\Delta G$, $\Delta G^\circ$ and $\Delta G^{\circ\prime}$, and why a positive $\Delta G^{\circ\prime}$ step can run in a cell.
- [ ] 3 Practiced: I can compute $\Delta G$ from $\Delta H$ and $\Delta S$, from $\Delta G^\circ$ and $Q$, and convert $\Delta G^\circ \leftrightarrow K$ in Python with a cited value of $R$.
- [ ] 4 Applied: I can read the free energies reported by an RNA folding or primer design tool, or a $\Delta\Delta G$ of a variant, and translate them into population ratios.
- [ ] 5 Explained: I can teach $G$ as the function minimized at constant $T$ and $P$, its link to the Boltzmann distribution, and the limits of additive energy models.

## References

[^chem16]: [[Chemistry 2e (OpenStax)]], ch. 16 "Thermodynamics", §16.4 "Free Energy" ($G = H - TS$, sign of $\Delta G$ and spontaneity, the four combinations of signs of $\Delta H$ and $\Delta S$, $\Delta G = \Delta G^\circ + RT\ln Q$, $\Delta G^\circ = -RT\ln K$).
[^chem]: [[Chemistry 2e (OpenStax)]] (enthalpy of fusion of water).
[^appg]: [[Chemistry 2e (OpenStax)]], Appendix G "Standard Thermodynamic Properties for Selected Substances".
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], course description (thermodynamics among the course topics).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA recommended value of the molar gas constant, $R = 8.314\,462\,618\ldots$ J mol⁻¹ K⁻¹ (exact).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of free energy in enzymes and metabolism (spontaneity versus rate, $\Delta G^{\circ\prime}$ at pH 7, the DHAP to GAP isomerization, additivity of free energies of coupled reactions, $\Delta G^{\circ\prime}$ of ATP hydrolysis).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of bioenergetics (Gibbs free energy as energy capable of doing work at constant $T$ and $P$; transformed standard constants $\Delta G'^\circ$ and $K'_{\text{eq}}$ at pH 7, water activity 1 and 1 mM $\mathrm{Mg^{2+}}$) (chapter number not verified).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell".
[^pbocsm]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., treatment of statistical mechanics (Boltzmann distribution, free energy and probabilities of states).
[^zuker]: [[Zuker 1981 - Optimal Computer Folding of Large RNA Sequences]], *Nucleic Acids Research* 9(1):133-148.
[^primer3]: [[Untergasser 2012 - Primer3 New Capabilities and Interfaces]], *Nucleic Acids Research* 40(15):e115.
