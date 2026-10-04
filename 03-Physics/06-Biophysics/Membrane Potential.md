---
aliases:
  - Resting Potential
  - Resting Membrane Potential
  - Transmembrane Potential
  - Potentiel de membrane
  - Potentiel de repos
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - domain/chemistry
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Electric Potential]]"
  - "[[Capacitance]]"
  - "[[Molar Concentration]]"
  - "[[Cell Membrane]]"
  - "[[Diffusion]]"
  - "[[Boltzmann Distribution]]"
related:
  - "[[Nernst Equation]]"
  - "[[Goldman-Hodgkin-Katz Equation]]"
  - "[[Ion Channel]]"
  - "[[Action Potential]]"
  - "[[Neuron]]"
  - "[[Mitochondrion]]"
  - "[[Oxidative Phosphorylation]]"
  - "[[Membrane Transport]]"
  - "[[Chemical Potential]]"
  - "[[Hodgkin-Huxley Model]]"
  - "[[Order-of-Magnitude Estimation]]"
projects: []
sources:
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Membrane Potential

> [!abstract]
> Living cells keep their inside a few tens of millivolts negative relative to the outside: pumps build ion concentration differences across the membrane, and because the resting membrane lets potassium leak out far more easily than other ions, a slight excess of negative charge stays inside until its electrical pull balances the outward push of the gradient.

## Definition

The **membrane potential** $V_m = \phi_\text{in} - \phi_\text{out}$ is the difference in electric potential between the two sides of a membrane, inside minus outside ([[Electric Potential]]). The **resting potential** is its steady value in an unstimulated cell. It arises from ion concentration differences across the membrane combined with a selective permeability to ions, mainly to K⁺ at rest.[^alberts11] A neuron at rest sits at about −70 mV.[^ap]

## Why it matters

- **Neurons and muscle.** An [[Action Potential]] is a brief excursion of $V_m$ driven by voltage-gated channels; electrophysiology recordings are time series of $V_m$ or of the currents that change it ([[Neuron]], [[Ion Channel]]).
- **Energy.** Mitochondria and bacteria store energy as a membrane potential plus a pH difference, the proton-motive force that drives ATP synthase ([[Mitochondrion]], [[Oxidative Phosphorylation]]).[^alberts-en]
- **Transport.** The potential adds an electrical term to the free energy of every charged molecule that crosses a membrane, so it decides the direction of ion fluxes and of ion-coupled transport ([[Membrane Transport]], [[Chemical Potential]]).
- **Models.** The Nernst and Goldman-Hodgkin-Katz equations, then the [[Hodgkin-Huxley Model]], turn concentrations and permeabilities into voltages; their parameters come from tables like the one below and from fits to recordings.

## Core (L1)

### Two ingredients: gradients and selective permeability

Ion concentrations of a typical mammalian cell (mM):[^alberts11]

| Ion | Inside (cytosol) | Outside | Ratio out/in |
|---|---:|---:|---:|
| K⁺ | 140 | 5 | 0.04 |
| Na⁺ | 5-15 | 145 | 10-29 |
| Cl⁻ | 5-15 | 110 | 7-22 |
| Ca²⁺ | 10⁻⁴ | 1-2 | 10⁴-2 × 10⁴ |

- **Gradients.** The Na⁺-K⁺ pump uses the energy of ATP to export 3 Na⁺ and import 2 K⁺ per cycle, keeping K⁺ high and Na⁺ low inside.[^alberts11]
- **Selective permeability.** The bilayer itself is nearly impermeable to ions ([[Cell Membrane]]); at rest, K⁺ leak channels make the membrane far more permeable to K⁺ than to Na⁺.[^alberts11]

### How the potential builds up

1. Start with the gradients above and no potential: both sides are electrically neutral.
2. K⁺ leaks out through its channels, down its concentration gradient ([[Diffusion]]).
3. Each K⁺ that leaves carries a positive charge out; its negative partner, which cannot cross, stays inside. The inside becomes negative.
4. The negative inside pulls K⁺ back, so the net outflow slows down.
5. The outflow stops when the electrical pull balances the concentration push: the **K⁺ equilibrium (Nernst) potential**, $E_K \approx -89$ mV at 37 °C (derived in L2).

The real resting potential is less negative than $E_K$ (about −70 mV in neurons[^ap]) because the membrane also lets a little Na⁺ in, whose own equilibrium potential is positive.

![[membrane-potential-ion-gradients.svg]]

**Few ions, strong field.** The charge imbalance is a thin layer on each face of the membrane; the cytosol and the outside stay electrically neutral in bulk. To charge a cell 20 µm across to −70 mV, about $5 \times 10^6$ K⁺ ions must leave, roughly 1 in 60,000 of the K⁺ inside (computed in L2). Yet across a bilayer about 5 nm thick[^alberts-mem] the field is $0.07\ \text{V} / 5 \times 10^{-9}\ \text{m} \approx 1.4 \times 10^7$ V/m, enormous for a film two molecules thick.

## Deeper (L2)

### The Nernst equation from the Boltzmann distribution

At equilibrium, an ion of charge $ze$ has potential energy $ze\phi$, and its concentration follows the [[Boltzmann Distribution]], $c \propto e^{-ze\phi / k_B T}$. The ratio across the membrane is $c_\text{in}/c_\text{out} = e^{-zeV/k_BT}$, which solved for $V$ gives the **equilibrium potential** of the ion:

$$E_\text{ion} = \frac{k_B T}{ze} \ln \frac{c_\text{out}}{c_\text{in}} = \frac{RT}{zF} \ln \frac{c_\text{out}}{c_\text{in}},$$

since $R = N_A k_B$ and $F = N_A e$.[^nist] Equivalently, the electrochemical potential $\mu = \mu^\circ + RT \ln c + zF\phi$ is equal on both sides ([[Chemical Potential]], [[Nernst Equation]]). At 37 °C, $k_B T/e = 26.7$ mV, or 61.5 mV per tenfold concentration ratio for $z = 1$. With the table values (taking 10 mM, the middle of 5-15, for Na⁺ and Cl⁻ inside): $E_K = -89$ mV, $E_\text{Na} = +71$ mV (+61 to +90 mV over 5-15 mM inside) and $E_\text{Cl} = -64$ mV (−53 to −83 mV). Opening K⁺ channels pulls $V_m$ towards −89 mV; opening Na⁺ channels pulls it towards +71 mV.

### The resting potential as a weighted average

Model each ion's channels as a conductance $g_i$, so that the ion current is $I_i = g_i (V - E_i)$ ([[Ohm's Law]]): zero at the ion's own equilibrium potential. At steady state the total current is zero, $\sum_i g_i (V - E_i) = 0$, so

$$V_\text{rest} = \frac{\sum_i g_i E_i}{\sum_i g_i}.$$

The resting potential is a **conductance-weighted average** of the Nernst potentials and lies closest to that of the most permeant ion. With $g_K = 10\,g_\text{Na}$ (illustrative, Cl⁻ ignored), $V = (10 \times (-89.1) + 71.5)/11 = -74.5$ mV. Raising $g_\text{Na}$ moves $V$ towards $E_\text{Na}$: the rising phase of an [[Action Potential]].

### The membrane as a capacitor

A membrane separates charge like a parallel-plate capacitor ([[Capacitance]]), with a specific capacitance of about 1 µF/cm² = $10^{-2}$ F/m².[^pboc] Holding $V$ requires a charge per area $Q/A = c_m |V|$, that is $c_m |V| / e$ monovalent ions per area. At 70 mV: $10^{-2} \times 0.07 / 1.602 \times 10^{-19} \approx 4.4 \times 10^{15}$ ions per m², about 4400 per µm². For a sphere of radius $r$ filled with K⁺ at concentration $c$, the fraction of K⁺ that must leave is

$$\frac{c_m |V|\, 4\pi r^2 / e}{c\, N_A\, \tfrac{4}{3}\pi r^3} = \frac{3\, c_m |V|}{r\, c\, F}.$$

For $r = 10$ µm (assumed), $c = 140$ mM $= 140$ mol/m³ and $V = 70$ mV: $3 \times 10^{-2} \times 0.07 / (10^{-5} \times 140 \times 96\,485) \approx 1.6 \times 10^{-5}$. Setting the potential does not measurably change the bulk concentrations, which is why the Nernst equation can use them.

### Several ions: the Goldman-Hodgkin-Katz equation

Conductances themselves depend on voltage and concentrations. The **Goldman-Hodgkin-Katz (GHK) equation** uses permeabilities $P_i$ instead, for monovalent ions:

$$V_\text{rest} = \frac{k_B T}{e} \ln \frac{P_K [\text{K}^+]_\text{out} + P_\text{Na} [\text{Na}^+]_\text{out} + P_\text{Cl} [\text{Cl}^-]_\text{in}}{P_K [\text{K}^+]_\text{in} + P_\text{Na} [\text{Na}^+]_\text{in} + P_\text{Cl} [\text{Cl}^-]_\text{out}}.$$

The Cl⁻ terms are swapped because $z = -1$. It is derived in the Advanced section and developed in [[Goldman-Hodgkin-Katz Equation]]. With illustrative permeability ratios $P_K : P_\text{Na} : P_\text{Cl} = 1 : 0.05 : 0.45$ it gives −65 mV (Computational representation).

## Advanced (L3)

### Deriving GHK under a constant field

Take a membrane of thickness $d$, inside at $x = 0$, outside at $x = d$, $V = \phi(0) - \phi(d)$. An ion's flux combines diffusion and drift in the field, with mobility $D/k_BT$ from the Einstein relation $D = k_BT/\zeta$:[^pboc]

$$J = -D \Big( \frac{dc}{dx} + \frac{ze}{k_B T}\, c\, \frac{d\phi}{dx} \Big).$$

Assume a linear potential, $d\phi/dx = -V/d$, and write $u = zeV/k_BT$, so $J = -D\,(c' - u\,c/d)$. At steady state $J$ is constant; multiplying by $e^{-ux/d}$ gives $\frac{d}{dx}\big(c\, e^{-ux/d}\big) = -\frac{J}{D} e^{-ux/d}$. Integrating from 0 to $d$, with membrane-edge concentrations $\beta c_\text{in}$ and $\beta c_\text{out}$ (partition coefficient $\beta$) and permeability $P = D\beta/d$:

$$J = P\,u\,\frac{c_\text{in} - c_\text{out}\, e^{-u}}{1 - e^{-u}} \quad (\text{outward positive}).$$

Write $w = e^{-eV/k_BT}$. For a cation ($z = 1$), $J \propto c_\text{in} - c_\text{out} w$; for an anion ($z = -1$, $u \to -u$), the same algebra gives $J \propto c_\text{in} w - c_\text{out}$ with the same prefactor $P u/(1 - w)$. Zero net electric current, $\sum_\text{cations} J - \sum_\text{anions} J = 0$, gives

$$w = \frac{\sum_c P_c c_{c,\text{in}} + \sum_a P_a c_{a,\text{out}}}{\sum_c P_c c_{c,\text{out}} + \sum_a P_a c_{a,\text{in}}},$$

and $V = -(k_BT/e) \ln w$ is the GHK equation. The assumptions are explicit: constant field, ions crossing independently, no pump current. With a single permeant ion it reduces to the Nernst equation (Exercise 5).

### Mitochondria and bacteria

In mitochondria, the respiratory chain pumps H⁺ out of the matrix, leaving it negative and alkaline; the membrane potential and the pH difference together form the proton-motive force that drives ATP synthase. Bacteria build the same force across their plasma membrane and use it for ATP synthesis, transport and the rotation of their flagella.[^alberts-en] The physics is the Nernst relation applied to H⁺: one pH unit is worth $61.5$ mV at 37 °C, and [[Mitochondrion]] adds the two terms into one driving force.

### From rest to signals

Charging the membrane capacitance takes current: $c_m\, dV/dt = -\sum_i g_i (V - E_i)$ per unit area, the circuit form of the weighted average. Letting $g_\text{Na}$ and $g_K$ depend on voltage and time turns this equation into the [[Hodgkin-Huxley Model]] of the action potential. Na⁺, far from equilibrium at rest ($V_m - E_\text{Na} \approx -140$ mV), is the stored driving force that spikes and Na⁺-coupled transporters spend.[^alberts11]

## Mathematical representation

- $V_m = \phi_\text{in} - \phi_\text{out}$ (V); $c_\text{in}$, $c_\text{out}$ concentrations; $z$ valence; $e$ elementary charge; $k_B$ Boltzmann constant; $T$ absolute temperature; $R = N_A k_B$; $F = N_A e$.
- **Nernst**: $E_i = \dfrac{k_B T}{z_i e} \ln \dfrac{c_{i,\text{out}}}{c_{i,\text{in}}}$.
- **Weighted average** (ohmic channels, zero net current): $V_\text{rest} = \sum_i g_i E_i / \sum_i g_i$.
- **GHK** (monovalent ions): $V_\text{rest} = \dfrac{k_BT}{e} \ln \dfrac{\sum_c P_c c_{c,\text{out}} + \sum_a P_a c_{a,\text{in}}}{\sum_c P_c c_{c,\text{in}} + \sum_a P_a c_{a,\text{out}}}$.
- **Capacitor**: $Q = c_m A V$; ions moved $N = c_m A |V| / e$.
- **Membrane equation**: $c_m \dfrac{dV}{dt} = -\sum_i g_i (V - E_i)$ (per unit area).

## Computational representation

Constants are the exact SI values; concentrations in mM (only ratios enter).

```python
import math

K_B = 1.380649e-23        # J/K, Boltzmann constant (exact, CODATA)
E = 1.602176634e-19       # C, elementary charge (exact, CODATA)
N_A = 6.02214076e23       # 1/mol, Avogadro constant (exact, CODATA)
T = 310.15                # K, 37 °C


def thermal_voltage(T: float = T) -> float:
    """k_B T / e in mV."""
    return 1000 * K_B * T / E


def nernst(z: int, c_in: float, c_out: float, T: float = T) -> float:
    """Equilibrium potential V_in - V_out (mV) of an ion of valence z."""
    return thermal_voltage(T) / z * math.log(c_out / c_in)


def ghk(P: dict, c_in: dict, c_out: dict, T: float = T) -> float:
    """Goldman-Hodgkin-Katz resting potential (mV) for monovalent ions.
    Anions (names ending in '-') enter with inside and outside swapped."""
    num = sum(p * (c_in if ion.endswith("-") else c_out)[ion] for ion, p in P.items())
    den = sum(p * (c_out if ion.endswith("-") else c_in)[ion] for ion, p in P.items())
    return thermal_voltage(T) * math.log(num / den)


Z = {"K+": 1, "Na+": 1, "Cl-": -1}
C_IN = {"K+": 140, "Na+": 10, "Cl-": 10}      # mM, mammalian cell; 10 = middle of 5-15
C_OUT = {"K+": 5, "Na+": 145, "Cl-": 110}     # mM

print(f"k_B T / e = {thermal_voltage():.2f} mV, x ln 10 = {thermal_voltage() * math.log(10):.1f} mV per decade")
for ion in Z:
    print(f"E({ion:3}) = {nernst(Z[ion], C_IN[ion], C_OUT[ion]):+6.1f} mV")
rest = {"K+": 1.0, "Na+": 0.05, "Cl-": 0.45}  # illustrative relative permeabilities
print(f"GHK, resting permeabilities : {ghk(rest, C_IN, C_OUT):+6.1f} mV")
print(f"GHK, Na+ permeability x 400 : {ghk({**rest, 'Na+': 20.0}, C_IN, C_OUT):+6.1f} mV")
```

```text
k_B T / e = 26.73 mV, x ln 10 = 61.5 mV per decade
E(K+ ) =  -89.1 mV
E(Na+) =  +71.5 mV
E(Cl-) =  -64.1 mV
GHK, resting permeabilities :  -64.9 mV
GHK, Na+ permeability x 400 :  +53.7 mV
```

The permeability ratios are illustrative, not measurements; in a real analysis they are fitted to recordings. Raising $P_\text{Na}$ 400-fold, as voltage-gated channels do during a spike, flips the potential to positive values close to $E_\text{Na}$.

## Worked example

> [!example] The resting potential of a mammalian cell, step by step
> 1. **Thermal voltage** at 310.15 K: $1.380\,649 \times 10^{-23} \times 310.15 / 1.602\,176\,634 \times 10^{-19} = 26.73$ mV.
> 2. **$E_K$** $= 26.73 \times \ln(5/140) = 26.73 \times (-3.332) = -89.1$ mV.
> 3. **$E_\text{Na}$** (10 mM inside) $= 26.73 \times \ln(14.5) = 26.73 \times 2.674 = +71.5$ mV.
> 4. **GHK** with $P_K : P_\text{Na} : P_\text{Cl} = 1 : 0.05 : 0.45$ (illustrative). Numerator: $1 \times 5 + 0.05 \times 145 + 0.45 \times 10 = 16.75$. Denominator: $1 \times 140 + 0.05 \times 10 + 0.45 \times 110 = 190.0$. $V = 26.73 \times \ln(16.75/190.0) = -64.9$ mV.
> 5. **Interpretation.** The result lies between $E_K$ and $E_\text{Na}$, much closer to $E_K$, and has the order of the −70 mV of neurons.[^ap] The Cl⁻ term changes little because $E_\text{Cl}$ (−64 mV) is already close to $V$.

## Common misconceptions

> [!warning] "The pump makes the potential"
> The potential is set by the K⁺ leak acting on the gradients. The pump maintains the gradients and adds only a small current of its own. In the model, if the pump stops, $V_m$ does not vanish at once: it follows the gradients as the leaks slowly dissipate them.

> [!warning] "A negative potential means the cell is full of negative charge"
> Only about 1 K⁺ in 60,000 has to leave to charge a 20 µm cell, and the unbalanced charge sits in a thin layer at the membrane. The cytosol is electrically neutral in bulk.

> [!warning] "The resting potential equals the K⁺ equilibrium potential"
> It is a weighted average of all permeant ions' Nernst potentials: about −70 mV against −89 mV for $E_K$, because some Na⁺ leaks in.

## Exercises

> [!question] Exercise 1 (L1)
> A neuron rests at −70 mV. Which side of the membrane is positive? For a K⁺ ion at the inner face, in which direction do the electric field and the concentration gradient push? Which wins?

> [!success]- Solution
> The outside is positive. The field pulls the cation inwards, towards the negative inside; the gradient (140 mM inside, 5 mM outside) pushes it out. At −70 mV the field is weaker than at $E_K = -89$ mV, where the two would balance, so the gradient wins: a small net K⁺ efflux, compensated at steady state by Na⁺ influx and by the pump.

> [!question] Exercise 2 (L2)
> Compute the Ca²⁺ equilibrium potential at 37 °C from the table (inside $10^{-4}$ mM, outside 1 to 2 mM). What happens when Ca²⁺ channels open?

> [!success]- Solution
> $z = 2$ halves the prefactor: $E_\text{Ca} = \frac{26.73}{2} \ln(10^4) = +123$ mV for 1 mM outside, and $\frac{26.73}{2} \ln(2 \times 10^4) = +132$ mV for 2 mM. At a resting $V_m$ near −70 mV, Ca²⁺ is about 200 mV from equilibrium: opening Ca²⁺ channels causes a strong influx that raises a tiny cytosolic concentration many-fold, which is why Ca²⁺ works as an intracellular signal.

> [!question] Exercise 3 (L2)
> With the weighted-average formula and $E_K = -89.1$ mV, $E_\text{Na} = +71.5$ mV, compute $V_\text{rest}$ for $g_K/g_\text{Na} = 10$, then for $g_K/g_\text{Na} = 5$. Interpret.

> [!success]- Solution
> $(10 \times (-89.1) + 71.5)/11 = -74.5$ mV; $(5 \times (-89.1) + 71.5)/6 = -62.3$ mV. Doubling the relative Na⁺ conductance depolarizes the cell by 12 mV: small changes in permeability move the potential, the lever that channels pull.

> [!question] Exercise 4 (L3, Python)
> Treat *E. coli* as a spherocylinder 1 µm in diameter and 2 µm long. How many monovalent ions must cross its membrane to set an illustrative potential of −100 mV, and what concentration would that number represent in the cell's volume?

> [!success]- Solution
> ```python
> import math
>
> E, N_A = 1.602176634e-19, 6.02214076e23
> C_M = 1e-2                                   # F/m^2, i.e. 1 µF/cm^2
>
>
> def charging_ions(area_um2: float, v_mV: float) -> float:
>     """Number of monovalent ions whose charge sets a potential v across a membrane area."""
>     return C_M * area_um2 * 1e-12 * abs(v_mV) / 1000 / E
>
>
> d, L = 1.0, 2.0                              # µm, spherocylinder: diameter and total length
> area = math.pi * d * L                       # side + two hemispherical caps
> volume = math.pi * (d / 2) ** 2 * (L - d) + 4 / 3 * math.pi * (d / 2) ** 3
> n = charging_ions(area, -100)                # illustrative potential
> conc = n / (volume * 1e-15 * N_A)            # mol/L
> print(f"area {area:.2f} µm², volume {volume:.2f} µm³, {n:.2e} ions, {conc * 1e6:.0f} µM equivalent")
> ```
> Output: `area 6.28 µm², volume 1.31 µm³, 3.92e+04 ions, 50 µM equivalent`. About 40,000 ions, a 50 µM shift if they all came from one species: small next to the hundreds of millimolar of ions in a cell, so even a bacterium charges its membrane without changing its composition ([[Order-of-Magnitude Estimation]]).

> [!question] Exercise 5 (L3)
> Show that the GHK equation reduces to the Nernst equation when only one ion is permeant, for a cation and for an anion. Check with `ghk` from the code above.

> [!success]- Solution
> Cation only: $V = \frac{k_BT}{e} \ln \frac{P c_\text{out}}{P c_\text{in}} = \frac{k_BT}{e} \ln \frac{c_\text{out}}{c_\text{in}}$, the Nernst potential with $z = 1$. Anion only: $V = \frac{k_BT}{e} \ln \frac{c_\text{in}}{c_\text{out}} = \frac{k_BT}{-e} \ln \frac{c_\text{out}}{c_\text{in}}$, Nernst with $z = -1$: the swap of inside and outside is the sign of the charge. In code, `ghk({'K+': 1.0}, C_IN, C_OUT)` returns −89.1 mV $= E_K$, and `ghk({'Cl-': 1.0}, C_IN, C_OUT)` returns $26.73 \ln(10/110) = -64.1$ mV $= E_\text{Cl}$.

## Mastery checklist

- [ ] 1 Recognized: I can define the membrane potential and its sign convention, and quote typical values (about −70 mV in neurons) and the main ion gradients.
- [ ] 2 Understood: I can explain how a K⁺ leak on top of pumped gradients creates a negative inside, and why only a tiny fraction of ions moves.
- [ ] 3 Practiced: I can derive the Nernst equation from the Boltzmann distribution and compute Nernst, weighted-average and GHK potentials in Python.
- [ ] 4 Applied: I used real concentrations and permeabilities, or a real recording, to compute or interpret a resting potential.
- [ ] 5 Explained: I can teach the GHK derivation and its assumptions, the role of the pump, and the link to proton-motive force and action potentials.

## References

[^alberts11]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 11, Table 11-1 (ion concentrations inside and outside a typical mammalian cell) and treatment of membrane transport and membrane potentials (the Na⁺-K⁺ pump and its 3 Na⁺ / 2 K⁺ stoichiometry, K⁺ leak channels, the Nernst equation, Na⁺-driven transport).
[^alberts-mem]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane structure (lipid bilayer about 5 nm thick).
[^alberts-en]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of energy conversion (proton-motive force across the inner mitochondrial membrane and the bacterial plasma membrane, ATP synthase, proton-driven flagellar rotation in bacteria).
[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], nervous tissue chapter (resting membrane potential of a neuron, about −70 mV).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of biological electricity (membrane capacitance of about 1 µF/cm²) and of diffusion (the Einstein relation).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA: Boltzmann constant, elementary charge $1.602\,176\,634 \times 10^{-19}$ C and Avogadro constant, exact since the 2019 SI; $R = N_A k$ and $F = N_A e$.
