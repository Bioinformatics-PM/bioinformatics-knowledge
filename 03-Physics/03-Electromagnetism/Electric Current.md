---
aliases:
  - Current
  - Ionic Current
  - Ampere
  - Courant électrique
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electric Charge]]"
  - "[[Derivative]]"
  - "[[Integral]]"
related:
  - "[[Ohm's Law]]"
  - "[[Electric Potential]]"
  - "[[Capacitance]]"
  - "[[RC Circuit]]"
  - "[[Ion Channel]]"
  - "[[Membrane Potential]]"
  - "[[Two-State Model]]"
  - "[[Magnetic Field]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Electric Current

> [!abstract]
> An electric current is charge on the move, measured as the charge crossing a surface per second (amperes); in cells and buffers the moving charges are ions, and a single open ion channel carries a few picoamperes, millions of ions per second.

## Definition

The **electric current** $I$ through a surface is the rate at which charge crosses it, $I = dQ/dt$. Its SI unit is the **ampere** (1 A = 1 C/s). By convention its direction is the direction in which positive charge moves; negative charges moving the opposite way make a current in the same direction.[^up9] The **current density** $\vec J$ is the current per unit area; for carriers of charge $q$, number density $n$ and drift velocity $\vec v_d$, $\vec J = nq\vec v_d$.[^up9]

## Why it matters

- **Electrophysiology records currents.** A patch-clamp experiment measures the current through a small patch of membrane, down to one channel, as a function of time; those traces are the raw data of [[Ion Channel]] studies.[^alberts]
- **Fluxes are currents.** A rate of ion transport (ions per second, mol per second) and a current are the same quantity in different units, linked by $e$ and $F$ ([[Electric Charge]]).
- **Every electrophoresis run is a circuit.** The power supply drives a current through buffer and gel; current, voltage and resistance are linked by [[Ohm's Law]], and the voltage sets the field that moves the DNA ([[Gel Electrophoresis]]).
- **Moving charges make magnetic fields**, the link to the second half of electromagnetism ([[Magnetic Field]], [[Lorentz Force]]).

## Core (L1)

**Definition in practice.** Over an interval, the average current is $I = \Delta Q/\Delta t$; the instantaneous current is the [[Derivative]] $dQ/dt$. Conversely, the charge transferred is the [[Integral]] of the current, $Q = \int I\,dt$, the area under a current trace.[^up9]

**Direction and sign.** Conventional current follows positive charge.[^up9] In a metal the carriers are electrons, so they move against the conventional current. In a salt solution the carriers are ions of both signs: a cation moving to the right and an anion moving to the left both transfer positive charge to the right, so their contributions **add**.

**Ions and current.** A flux of $\Phi$ ions per second of charge number $z$ carries
$$I = z\,e\,\Phi \qquad\text{or, per mole,}\qquad I = z\,F\,\Phi_\text{mol},$$
with $F$ the Faraday constant and $\Phi_\text{mol}$ in mol/s.

```mermaid
flowchart LR
    P["ion flux Φ (ions/s)"] -- "× z e" --> I["current I (A)"]
    I -- "∫ dt" --> Q["charge Q (C)"]
    Q -- "÷ z F" --> M["moles of ions"]
```

**Scales.**

| Current | Elementary charges per second | Moles of monovalent ions per second |
|---|---:|---:|
| 1 A | $6.24 \times 10^{18}$ | $1.04 \times 10^{-5}$ |
| 1 mA | $6.24 \times 10^{15}$ | $1.04 \times 10^{-8}$ |
| 1 pA | $6.24 \times 10^{6}$ | $1.04 \times 10^{-17}$ |

**Bio: single channels in picoamperes.** As many as $10^8$ ions can cross one open channel per second.[^alberts] For monovalent ions that is $10^8 \times 1.602 \times 10^{-19} = 1.6 \times 10^{-11}$ A, or 16 pA. In a patch-clamp recording a glass micropipette is sealed onto the membrane so that the current through the channels of the patch flows into the pipette; single channels appear as rectangular steps of current, switching abruptly between open and closed.[^alberts]

## Deeper (L2)

**Current density in a solution.** Each species of ion contributes $n_i z_i e\,\vec v_i$, so $\vec J = \sum_i n_i z_i e\,\vec v_i$: the current depends on how many carriers there are, their charge, and how fast they drift in the field. The drift speed is set by friction, the subject of [[Electrophoretic Mobility]].

**Charge conservation at a junction.** Charge does not pile up at a point of a circuit, so the currents entering a junction equal those leaving it (Kirchhoff's junction rule).[^upcirc] Applied to a patch of membrane: the current crossing it is the sum of the ionic currents through each kind of channel plus the current that charges the membrane capacitance, $C\,dV/dt$ ([[Capacitance]], [[RC Circuit]]). This bookkeeping is the starting point of the [[Hodgkin-Huxley Model]].

**From one channel to a cell.** A channel flips randomly between closed and open states.[^alberts] If a cell has $N$ identical channels, each open with probability $p_o$ and carrying $i$ when open, the expected macroscopic current is
$$\langle I \rangle = N\,p_o\,i,$$
a sum of independent two-state contributions ([[Two-State Model]]). With 1,000 channels, $p_o = 0.1$ and $i = 2$ pA, $\langle I \rangle = 200$ pA: whole-cell currents are averages of picoampere events.

## Mathematical representation

- **Current**: $I(t) = \dfrac{dQ}{dt}$, $Q(t_1, t_2) = \displaystyle\int_{t_1}^{t_2} I(t)\,dt$.
- **Ionic current**: $I = z e \Phi = z F \Phi_\text{mol}$, with $\Phi$ in ions/s and $\Phi_\text{mol}$ in mol/s.
- **Current density**: $\vec J = \sum_i n_i z_i e\,\vec v_i$ (A/m²), and $I = \int_S \vec J \cdot d\vec A$ through a surface $S$.
- **Junction rule**: $\sum_k I_k = 0$ for currents counted positive when entering a node.
- **Channel population**: $\langle I \rangle = N p_o i$, from linearity of expectation.

## Computational representation

A recorded current is a sampled time series; the charge it carries is a Riemann sum ([[Integral]]). Constants are exact since the 2019 SI.[^nist]

```python
E_CHARGE = 1.602176634e-19      # C, exact
N_A = 6.02214076e23             # mol^-1, exact
FARADAY = N_A * E_CHARGE


def current_from_rate(ions_per_s, z=1):
    """Current (A) carried by a flux of ions of charge number z."""
    return z * E_CHARGE * ions_per_s


def rate_from_current(current_a, z=1):
    """Ions per second needed to carry a current (A)."""
    return current_a / (z * E_CHARGE)


print(f"1e8 ions/s, z = +1: {current_from_rate(1e8) * 1e12:.1f} pA")
print(f"1 pA = {rate_from_current(1e-12):.3e} K+/s = {rate_from_current(1e-12, 2):.3e} Ca2+/s")

# Charge passed in a toy single-channel record (invented): pA, sampled every 0.1 ms
trace_pA = [0.0, 0.1, -0.1, 2.1, 1.9, 2.0, 2.2, 1.8, 2.0, 0.0, -0.1, 1.9, 2.1, 0.1, 0.0]
dt = 1e-4                                            # s
q = sum(i * 1e-12 for i in trace_pA) * dt            # Q = integral of I dt (Riemann sum)
print(f"Q = {q:.2e} C = {q / E_CHARGE:.0f} elementary charges = {q / FARADAY:.2e} mol")
```

```text
1e8 ions/s, z = +1: 16.0 pA
1 pA = 6.242e+06 K+/s = 3.121e+06 Ca2+/s
Q = 1.60e-15 C = 9986 elementary charges = 1.66e-20 mol
```

The baseline noise ($\pm 0.1$ pA) averages out in the sum; real analyses first detect openings and closings (idealization), then measure the amplitude and duration of each event.

## Worked example

> [!example] Does one channel opening change the ion content of a cell?
> A K⁺ channel opens for 5 ms and passes 3 pA (illustrative values).
> 1. **Charge.** $Q = I\,t = 3 \times 10^{-12} \times 5 \times 10^{-3} = 1.5 \times 10^{-14}$ C.
> 2. **Ions.** $N = Q/e = 9.4 \times 10^4$ K⁺ ions, or $1.6 \times 10^{-19}$ mol.
> 3. **Cell content.** Intracellular K⁺ is about 140 mM.[^alberts] For an assumed spherical cell 10 µm in diameter, $V = \tfrac43\pi(5\ \mu\text{m})^3 = 5.2 \times 10^{-13}$ L, holding $0.140 \times 5.2 \times 10^{-13} \times N_A = 4.4 \times 10^{10}$ K⁺ ions.
> 4. **Fraction.** $9.4 \times 10^4 / 4.4 \times 10^{10} = 2 \times 10^{-6}$. Currents that change the membrane voltage move a negligible fraction of the ions ([[Capacitance]] explains why so few are enough).

## Common misconceptions

> [!warning] "Current is used up as it flows through a channel or resistor"
> Charge is conserved: what enters comes out (junction rule). What is used up is energy, dissipated as heat ([[Ohm's Law]]).

> [!warning] "Current flows in the direction the electrons move"
> Conventional current follows positive charge. In a wire the electrons move the opposite way; in a solution cations move with the current and anions against it.

> [!warning] "Cations and anions moving in opposite directions cancel"
> They add. Opposite charges moving in opposite directions transfer charge the same way.

> [!warning] "A picoampere is too small to matter"
> 1 pA is six million monovalent ions per second. A few picoamperes for a few milliseconds is enough to change a small cell's membrane potential.

## Exercises

> [!question] Exercise 1 (L1)
> How many ions per second make a 2.0 pA current if they are Na⁺? If they are Ca²⁺?

> [!success]- Solution
> $\Phi = I/(ze)$: $2.0 \times 10^{-12}/1.602 \times 10^{-19} = 1.25 \times 10^{7}$ Na⁺/s; half as many, $6.2 \times 10^{6}$ Ca²⁺/s.

> [!question] Exercise 2 (L1)
> Cl⁻ ions flow from outside to inside a cell. In which direction is the conventional current: inward or outward?

> [!success]- Solution
> Negative charge entering is equivalent to positive charge leaving: the conventional current is outward.

> [!question] Exercise 3 (L2)
> A gel power supply delivers 10 mA. How many elementary charges per second cross any section of the gel, and how many moles of monovalent ions per second would carry it?

> [!success]- Solution
> $10^{-2}/1.602 \times 10^{-19} = 6.2 \times 10^{16}$ per second; $I/F = 10^{-2}/96\,485 = 1.0 \times 10^{-7}$ mol/s. By the junction rule, the same current crosses every section of the gel and buffer in series.

> [!question] Exercise 4 (L2)
> A cell has 1,000 channels of single-channel current 2 pA, each open with probability 0.1. Give the mean current. If a drug lowers $p_o$ to 0.02, what is the new mean?

> [!success]- Solution
> $\langle I \rangle = N p_o i = 1000 \times 0.1 \times 2$ pA $= 200$ pA. With $p_o = 0.02$: 40 pA. The single-channel current is unchanged; only the time spent open changed, which a single-channel recording can tell apart.

> [!question] Exercise 5 (L2, Python)
> Modify the code to detect openings in `trace_pA` with a threshold of 1 pA, and report the number of openings, the mean open-channel current and the total open time.

> [!success]- Solution
> ```python
> threshold, events, open_samples = 1.0, 0, []
> previous_open = False
> for value in trace_pA:
>     is_open = value > threshold
>     if is_open and not previous_open:
>         events += 1
>     if is_open:
>         open_samples.append(value)
>     previous_open = is_open
> print(events, round(sum(open_samples) / len(open_samples), 2), f"{len(open_samples) * dt * 1e3:.1f} ms")
> ```
> Output: `2 2.0 0.8 ms`. Two openings, a mean amplitude of 2.0 pA and 0.8 ms of total open time: amplitude gives the single-channel current $i$, open time over total time estimates $p_o$.

## Mastery checklist

- [ ] 1 Recognized: I can define current as $dQ/dt$, give the ampere and the conventional direction.
- [ ] 2 Understood: I can explain why cations and anions add, the junction rule, and the link between ion flux and current.
- [ ] 3 Practiced: I can convert currents to ions per second and moles per second, and integrate a current trace into a charge.
- [ ] 4 Applied: I analyzed a real single-channel recording: detected openings, measured amplitudes and open probability.
- [ ] 5 Explained: I can teach how picoampere events add up to whole-cell currents and why they barely change ion concentrations.

## References

[^up9]: [[University Physics (OpenStax)]], Volume 2, ch. 9 "Current and Resistance" (definition of current, ampere, conventional direction, current density and drift velocity).
[^upcirc]: [[University Physics (OpenStax)]], Volume 2, treatment of direct-current circuits (Kirchhoff's rules); chapter not verified.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values: elementary charge and Avogadro constant (exact), Faraday constant $F = N_A e$.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), section "Ion Channels and the Electrical Properties of Membranes" (up to about 10⁸ ions per second through one open channel, patch-clamp recording, all-or-nothing opening and random gating of single channels) and the table of ion concentrations inside and outside a typical mammalian cell.
