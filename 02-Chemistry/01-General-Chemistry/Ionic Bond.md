---
aliases:
  - Ionic Bonding
  - Ion
  - Salt
  - Salt Bridge
  - Liaison ionique
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electron Configuration]]"
  - "[[Periodic Table]]"
  - "[[Electronegativity]]"
  - "[[Chemical Bond]]"
related:
  - "[[Covalent Bond]]"
  - "[[Coulomb's Law]]"
  - "[[Aqueous Solution]]"
  - "[[Water]]"
  - "[[Membrane Potential]]"
  - "[[Nernst Equation]]"
  - "[[Protein Tertiary Structure]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
---

# Ionic Bond

> [!abstract]
> When one atom hands electrons to another, both become ions, and opposite charges attract: that attraction is the ionic bond, which builds salt crystals, and which water weakens enough for cells to move ions around and for proteins to make and break salt bridges.

## Definition

An **ionic bond** is the electrostatic attraction between oppositely charged ions. It forms when electrons are transferred from an atom that loses them easily (typically a metal, which becomes a **cation**) to one that gains them readily (typically a nonmetal, which becomes an **anion**).[^c2e71][^5111] An **ionic compound** is not made of molecules: it is a three-dimensional lattice of cations and anions, and its formula (NaCl, MgCl₂) gives the smallest ratio of ions that is electrically neutral, the **formula unit**.[^c2e71][^c2e2]

## Why it matters

- **Ion gradients power membranes.** Cells keep K⁺ high inside and Na⁺ and Cl⁻ high outside; these gradients set the [[Membrane Potential]] that nerve signals and many transporters use ([[Ion Channel]], [[Membrane Transport]]).[^alberts]
- **Salt bridges in proteins.** At neutral pH the side chains of Lys and Arg are positive and those of Asp and Glu negative; pairs of them attract as **salt bridges**, one of the non-covalent contacts of a folded protein or a complex ([[Protein Tertiary Structure]]).[^berg]
- **Salts in every protocol.** Buffers, NaCl, MgCl₂ and phosphate salts are ionic compounds that dissociate into ions in water, which is why their concentration changes electrostatic interactions between biomolecules ([[Aqueous Solution]]).[^lehninger]

## Core (L1)

**Making ions.** Sodium, $[\text{Ne}]\,3s^1$, loses its single valence electron and becomes Na⁺, with the configuration of neon; chlorine, $[\text{Ne}]\,3s^2 3p^5$, gains one and becomes Cl⁻, with the configuration of argon ([[Electron Configuration]]).[^c2e71] The nucleus does not change: only the electron count does. Position in the [[Periodic Table]] predicts the usual charge: +1 for group 1 (Na⁺, K⁺), +2 for group 2 (Mg²⁺, Ca²⁺), −2 for group 16 (O²⁻, S²⁻), −1 for group 17 (Cl⁻).[^c2e2]

**Polyatomic ions** are covalently bonded groups carrying a net charge: ammonium NH₄⁺, phosphate PO₄³⁻, hydrogen phosphate HPO₄²⁻, bicarbonate HCO₃⁻.[^c2e2] Where the charge sits inside them is a question for the [[Lewis Structure]].

**Formulas from charges.** A neutral compound balances positive and negative charge: Ca²⁺ and Cl⁻ give CaCl₂; Ca²⁺ and PO₄³⁻ need $3 \times (+2) = 2 \times (-3)$, hence Ca₃(PO₄)₂.[^c2e2]

**Lattices.** In solid NaCl each ion is surrounded by ions of the opposite charge, attracting in all directions; there is no individual "NaCl molecule". Ionic solids have high melting points and conduct electricity only when molten or dissolved, once the ions can move.[^c2e71][^c2e2]

**Bio: gradients across the plasma membrane.** Ion concentrations of a typical mammalian cell (mM):[^alberts]

| Ion | Inside | Outside | Ratio out/in |
|---|---:|---:|---:|
| K⁺ | 140 | 5 | 0.04 |
| Na⁺ | 5-15 | 145 | 10-29 |
| Cl⁻ | 5-15 | 110 | 7-22 |

These are the ions of NaCl and KCl, but in water they are separated and hydrated; the membrane, not a lattice, keeps them where they are.

## Deeper (L2)

**Coulomb's law.** Two point charges $q_1$ and $q_2$ a distance $r$ apart interact with energy $E = \dfrac{q_1 q_2}{4\pi\varepsilon_0\,r}$, negative (attractive) for opposite charges.[^uphys] In a medium the energy is divided by the medium's dielectric constant $\varepsilon_r$; water has $\varepsilon_r = 78.5$, which is why it screens attractions between ions so effectively, while the water dipoles that surround each ion (hydration) stabilize the separated ions.[^lehninger] For a Lys⁺/Asp⁻ pair at an assumed 4 Å (computed below): −347 kJ/mol in vacuum, −4.4 kJ/mol in water, under 2 $RT$ at 37 °C ([[Chemical Bond#Deeper (L2)]]). A salt bridge on a protein surface is a weak, reversible contact, not a crystal bond.

**Lattice energy.** The energy needed to separate one mole of an ionic solid into its gaseous ions grows with the ion charges and falls with the distance between them, following the Coulomb form $U \propto Q_1 Q_2 / R_0$.[^c2e75] At the same distance, a 2+/2− pair (MgO) is bound four times as strongly as a 1+/1− pair (NaCl).

**From gradients to voltage.** An ion gradient across a membrane permeable to that ion is at equilibrium when the electrical potential balances it, the **Nernst equation** $E = \dfrac{RT}{zF}\ln\dfrac{C_\text{out}}{C_\text{in}}$.[^alberts] For K⁺ at 37 °C this gives −89 mV (Exercise 3): the order of magnitude of a resting [[Membrane Potential]].

## Mathematical representation

- Charge neutrality: a compound of cation charge $z_+$ and anion charge $z_-$ contains $n_+ z_+ + n_- z_- = 0$; the smallest solution is $n_+ = L/z_+$, $n_- = L/|z_-|$ with $L = \operatorname{lcm}(z_+, |z_-|)$.
- Coulomb energy per mole of pairs, with charges $z_1 e$, $z_2 e$ at distance $r$: $E = \dfrac{N_A e^2}{4\pi\varepsilon_0} \cdot \dfrac{z_1 z_2}{\varepsilon_r\, r}$. With SI values of $N_A$, $e$ and $\varepsilon_0$ the prefactor is 1389.35 kJ mol⁻¹ Å.
- Nernst: $R$ gas constant, $T$ temperature (K), $z$ ion charge, $F = N_A e$ the Faraday constant (96485 C/mol).

## Computational representation

```python
import math

K_COULOMB = 1389.35   # kJ/mol x Å, = N_A e^2 / (4 pi eps0) for unit charges

def charge(z: int) -> str:
    return f"({abs(z) if abs(z) > 1 else ''}{'+' if z > 0 else '-'})"

def formula_unit(cation: str, z_cat: int, anion: str, z_an: int) -> str:
    """Smallest neutral combination: n_cat * z_cat = n_an * |z_an|."""
    k = math.lcm(z_cat, abs(z_an))
    def part(ion: str, n: int) -> str:
        if n == 1:
            return ion
        polyatomic = sum(ch.isupper() for ch in ion) > 1
        return (f"({ion})" if polyatomic else ion) + str(n)
    return part(cation, k // z_cat) + part(anion, k // abs(z_an))

def coulomb(z1: int, z2: int, r: float, eps_r: float = 1.0) -> float:
    """Energy (kJ/mol) of two point charges r Å apart in a medium of dielectric constant eps_r."""
    return K_COULOMB * z1 * z2 / (eps_r * r)

for c, zc, a, za in [("Na", 1, "Cl", -1), ("Mg", 2, "Cl", -1), ("Ca", 2, "PO4", -3),
                     ("K", 1, "HPO4", -2), ("NH4", 1, "SO4", -2), ("Mg", 2, "O", -2)]:
    print(f"{c}{charge(zc)} + {a}{charge(za)} -> {formula_unit(c, zc, a, za)}")

for medium, eps in (("vacuum", 1.0), ("water", 78.5)):        # Lys+ ... Asp- at an assumed 4 Å
    print(f"{medium:6} {coulomb(+1, -1, 4.0, eps):7.1f} kJ/mol")
print(coulomb(2, -2, 4.0) / coulomb(1, -1, 4.0), coulomb(1, -1, 8.0) / coulomb(1, -1, 4.0))
```

```text
Na(+) + Cl(-) -> NaCl
Mg(2+) + Cl(-) -> MgCl2
Ca(2+) + PO4(3-) -> Ca3(PO4)2
K(+) + HPO4(2-) -> K2HPO4
NH4(+) + SO4(2-) -> (NH4)2SO4
Mg(2+) + O(2-) -> MgO
vacuum  -347.3 kJ/mol
water     -4.4 kJ/mol
4.0 0.5
```

The point-charge model ignores the size of ions, the structured water between them and the low-polarity interior of a protein; it gives orders of magnitude, not binding energies.

## Worked example

> [!example] A salt bridge between Lys and Asp
> 1. **Charges at pH 7.** The Lys side chain ends in –NH₃⁺ (charge +1), the Asp side chain in –COO⁻ (−1).[^berg]
> 2. **In vacuum**, at an assumed 4 Å: $E = 1389.35 \times (+1)(-1)/4.0 = -347$ kJ/mol, comparable to a covalent bond.
> 3. **In water** ($\varepsilon_r = 78.5$): $-347/78.5 = -4.4$ kJ/mol, about $1.7\,RT$ at 37 °C (2.58 kJ/mol).
> 4. **Reading.** On the solvent-exposed surface, the bridge forms and breaks with thermal motion; it contributes to stability only together with many other weak contacts ([[Chemical Bond]], [[Intermolecular Force]]).

## Common misconceptions

> [!warning] "NaCl is a molecule"
> Solid NaCl is a lattice in which every Na⁺ is attracted by several Cl⁻ neighbors. The formula is a ratio, not a molecule.[^c2e71]

> [!warning] "A cation is positive because it gained protons"
> The nucleus never changes in a chemical reaction. Na⁺ has 11 protons like Na, but 10 electrons instead of 11.[^c2e71]

> [!warning] "Phosphate and ammonium are held together by ionic bonds"
> Inside a polyatomic ion the atoms share electrons (covalent bonds); only the group as a whole carries a charge and bonds ionically to counter-ions.[^c2e2]

## Exercises

> [!question] Exercise 1 (L1)
> Write the formulas of magnesium phosphate, potassium chloride, sodium hydrogen phosphate (HPO₄²⁻) and calcium carbonate (CO₃²⁻). Check with `formula_unit`.

> [!success]- Solution
> Mg₃(PO₄)₂ (6+ against 6−), KCl, Na₂HPO₄, CaCO₃. `formula_unit("Mg", 2, "PO4", -3)` returns `Mg3(PO4)2`, and `formula_unit("Na", 1, "HPO4", -2)` returns `Na2HPO4`.

> [!question] Exercise 2 (L2)
> By what factor does the attraction of an ion pair change when (a) both charges double, (b) the distance doubles, (c) the pair moves from vacuum into water?

> [!success]- Solution
> (a) ×4, since $E \propto z_1 z_2$; (b) ×½, since $E \propto 1/r$; (c) ÷78.5. The code prints 4.0 and 0.5 for (a) and (b). Charge matters more than distance, and the solvent matters most.

> [!question] Exercise 3 (L2, Python)
> Compute the Nernst potentials of K⁺, Na⁺ and Cl⁻ at 37 °C from the table above, taking 10 mM (the middle of the 5-15 range, an assumption) for Na⁺ and Cl⁻ inside.

> [!success]- Solution
> ```python
> R, F, T = 8.314, 96485, 310.15
> CONC = {"K+": (1, 140, 5), "Na+": (1, 10, 145), "Cl-": (-1, 10, 110)}  # z, inside, outside (mM)
> for ion, (z, c_in, c_out) in CONC.items():
>     e = 1000 * R * T / (z * F) * math.log(c_out / c_in)
>     print(f"{ion:4} E = {e:+4.0f} mV")
> ```
> Output: `K+   E =  -89 mV`, `Na+  E =  +71 mV`, `Cl-  E =  -64 mV`. Opposite signs for K⁺ and Na⁺: opening K⁺ channels pulls the membrane negative, opening Na⁺ channels pulls it positive, the basis of the [[Action Potential]].

## Mastery checklist

- [ ] 1 Recognized: I can define cation, anion, ionic bond and formula unit.
- [ ] 2 Understood: I can predict ion charges from the periodic table and explain why solid NaCl has no molecules.
- [ ] 3 Practiced: I can write ionic formulas from charges and compute Coulomb energies in vacuum and in water.
- [ ] 4 Applied: I found salt bridges (Lys or Arg near Asp or Glu) in a real protein structure and judged whether they are buried or exposed.
- [ ] 5 Explained: I can explain why water weakens ionic interactions, and how ion gradients become a membrane potential.

## References

[^c2e71]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry", §7.1 "Ionic Bonding" (electron transfer, cations and anions, noble-gas configurations, ionic solids as lattices).
[^c2e75]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.5 "Strengths of Ionic and Covalent Bonds" (lattice energy and its dependence on ion charges and distance).
[^c2e2]: [[Chemistry 2e (OpenStax)]], ch. 2 "Atoms, Molecules, and Ions" (ionic compounds, formulas from ion charges, polyatomic ions; section not verified).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit II "Chemical Bonding & Structure", Lecture 9 "Periodic Table; Ionic and Covalent Bonds".
[^uphys]: [[University Physics (OpenStax)]], Volume 2, treatment of Coulomb's law.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 11, Table 11-1 (ion concentrations inside and outside a typical mammalian cell) and treatment of membrane potentials (Nernst equation).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of amino acids (charged side chains of Lys, Arg, Asp and Glu at neutral pH) and of electrostatic interactions (salt bridges) in proteins.
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of water (dielectric constant 78.5, screening and hydration of dissolved ions).
