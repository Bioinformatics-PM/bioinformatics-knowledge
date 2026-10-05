---
aliases:
  - H2O
  - H₂O
  - Water Molecule
  - Eau
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electronegativity]]"
  - "[[Molecular Geometry]]"
  - "[[Intermolecular Force]]"
  - "[[Hydrogen Bond]]"
related:
  - "[[Hydrophobic Effect]]"
  - "[[Aqueous Solution]]"
  - "[[Dielectric Constant]]"
  - "[[Coulomb's Law]]"
  - "[[Acid-Base Reaction]]"
  - "[[pH]]"
  - "[[Molar Concentration]]"
  - "[[Protein Structure]]"
  - "[[Cell Membrane]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
---

# Water

> [!abstract]
> Water is a small bent molecule with a negative oxygen side and two positive hydrogens. That shape makes it a hydrogen-bond network, a screen that weakens attractions between charges, and therefore a solvent for ions and polar molecules, but not for oil.

## Definition

**Water**, H₂O, is a bent molecule: an H–O–H angle of 104.5°, with oxygen sp3 and two lone pairs ([[Orbital Hybridization]]).[^c2e82] Oxygen is much more electronegative than hydrogen, so each O–H bond is polar; because the molecule is bent, the two bond dipoles do not cancel and water is a **polar molecule**.[^c2e7] Each molecule can donate two [[Hydrogen Bond|hydrogen bonds]] and accept two, which links liquid water into a dynamic network.[^lehninger] Its high **dielectric constant**, about 80, weakens electrostatic attractions between dissolved ions,[^uphys][^lehninger] which together with ion-dipole hydration makes water a solvent for salts and polar molecules.[^c2e112]

## Why it matters

- **Every biological constant is a water constant.** Dissociation constants, pKa values and concentrations are measured in aqueous buffer ([[Molar Concentration]], [[pH]]).
- **Structure prediction depends on the solvent.** Which residues are buried or exposed is a consequence of water ([[Hydrophobic Effect]], [[Solvent Accessible Surface Area]]); simulations represent water either as explicit molecules ([[Molecular Dynamics Simulation]]) or as a continuum with a high dielectric constant ([[Poisson-Boltzmann Equation]]).
- **Wet-lab steps are solubility chemistry.** Dissolving, precipitating and separating DNA, proteins and lipids follow from what water does and does not dissolve ([[Aqueous Solution]]).

## Core (L1)

![[water-polarity-hydrogen-bonds-hydration.svg]]

**1. Polar because bent.** O pulls the bonding electrons toward itself: partial charge δ− on O, δ+ on each H ([[Electronegativity]]). Bond polarity alone is not enough: CO₂ has two polar C=O bonds, but it is linear and its bond dipoles cancel. In bent H₂O they add along the bisector of the angle.[^c2e7]

**2. A hydrogen-bond network.** The two O–H groups are donors and the two lone pairs are acceptors, arranged roughly tetrahedrally ([[Molecular Geometry]]). In ice, every molecule makes four hydrogen bonds in an open lattice, which is why ice is less dense than liquid water and floats. In the liquid, each molecule is hydrogen-bonded to about 3.4 neighbours on average, and each bond lasts only about 1 to 20 picoseconds before breaking and re-forming: "flickering clusters", not a fixed structure.[^lehninger] The network explains why water boils far higher than the heavier H₂S, which has no comparable hydrogen bonding.[^c2e101]

**3. A solvent for ions: hydration.** When KCl dissolves, water molecules surround each ion: the δ− oxygens face K⁺, the δ+ hydrogens face Cl⁻ (ion-dipole attractions), and the hydrated ions move off into solution.[^c2e112] Polar molecules such as sugars and amino acids dissolve by hydrogen bonding with water.[^lehninger]

**4. A screen for charges.** Water's dielectric constant, about 80, divides the Coulomb energy between two charges by 80 relative to vacuum ([[Coulomb's Law]], [[Dielectric Constant]]).[^uphys] Ions that would cling together in vacuum or in oil separate easily in water (Worked example).[^lehninger]

**5. Not a solvent for oil.** Nonpolar molecules cannot join the network; the water molecules around them become more ordered, and the system lowers its free energy by clustering the nonpolar molecules together: the [[Hydrophobic Effect]], which drives protein folding, membrane formation and many binding events ([[Lipid]], [[Cell Membrane]], [[Protein Structure]]).[^lehninger][^berg]

## Deeper (L2)

**The low-dielectric interior.** A folded protein packs nonpolar side chains into its core.[^berg] That core is a low-polarity medium: a charge moved from water into it loses most of its screening and of its hydration shell, which costs energy, unless a partner of opposite charge or hydrogen-bonding groups are buried with it ([[Intermolecular Force#Deeper (L2)]]). This is why charged side chains are found mostly at the surface.[^berg]

**Water is also a reactant.** It is consumed in hydrolysis and produced in condensation reactions, such as the formation of peptide and phosphodiester bonds ([[Hydrolysis]], [[Peptide Bond]]).[^berg] It also ionizes slightly: $2\,\mathrm{H_2O} \rightleftharpoons \mathrm{H_3O^+} + \mathrm{OH^-}$, with $K_w = [\mathrm{H_3O^+}][\mathrm{OH^-}] = 1.0 \times 10^{-14}$ at 25 °C, so pure water contains $1.0 \times 10^{-7}$ M of each ion ([[Acid-Base Reaction]], [[pH]]).[^c2e14]

**How much water is there?** With a density close to 1.0 g/mL[^c2e1] and $M = 18.015$ g/mol, pure water is about 55.5 mol/L (computed below): in a 150 mM salt solution there are about 370 water molecules per Na⁺ ion, and every reaction in a cell happens in a crowd of solvent ([[Molar Concentration]]).

## Mathematical representation

- **Molecular dipole.** Two equal bond dipoles $\mu_{OH}$ at angle $\theta$ sum to
$$\mu = 2\,\mu_{OH} \cos\frac{\theta}{2},$$
so $\mu = 1.22\,\mu_{OH}$ for $\theta = 104.5°$ and $\mu = 0$ for a linear molecule ($\theta = 180°$).
- **Screened Coulomb energy.** For charges $z_1 e, z_2 e$ at distance $r$ in a medium of relative permittivity $\varepsilon_r$, per mole: $U = \dfrac{k e^2 N_A\, z_1 z_2}{\varepsilon_r\, r}$, with $k e^2 N_A = 1389.4$ kJ mol⁻¹ Å ([[Intermolecular Force#Computational representation]]).
- **Thermal distance.** Setting $|U| = RT$ for two unit charges gives the distance beyond which thermal motion wins (the Bjerrum length), with $R$ the gas constant[^gas] and $T$ the absolute temperature:
$$\ell_B = \frac{k e^2 N_A}{\varepsilon_r R T}.$$
- **Concentration of a pure liquid.** $c = \rho / M$, with $\rho$ the density (g/L) and $M$ the molar mass (g/mol).

## Computational representation

```python
import math

R = 8.314                   # J mol^-1 K^-1, gas constant
KE2 = 1389.4                # kJ mol^-1 Å, Coulomb energy of two unit charges 1 Å apart (Intermolecular Force)
WEIGHT = {"H": 1.008, "O": 15.999, "Na": 22.990, "Cl": 35.45}   # standard atomic weights, g/mol


def net_dipole(bond_dipole: float, angle_deg: float) -> float:
    """Magnitude of the sum of two equal bond dipoles separated by angle_deg."""
    return 2 * bond_dipole * math.cos(math.radians(angle_deg / 2))


def bjerrum_length(eps_r: float, temp_k: float = 298.0) -> float:
    """Distance (Å) at which two unit charges have |energy| = RT in a medium of relative permittivity eps_r."""
    return KE2 / (eps_r * R * temp_k / 1000)


for name, angle in [("H2O (bent)", 104.5), ("CO2 (linear)", 180.0)]:
    print(f"{name:13s} net/bond = {net_dipole(1.0, angle):.3f}")

for medium, eps in [("vacuum", 1), ("nonpolar solvent (assumed)", 2), ("protein interior (assumed)", 4), ("water", 80)]:
    print(f"{medium:27s} eps_r = {eps:2d}  Bjerrum length = {bjerrum_length(eps):6.1f} Å")

m_water = 2 * WEIGHT["H"] + WEIGHT["O"]
c_water = 1000 / m_water           # mol/L, taking 1000 g of water per litre
print(f"M(H2O) = {m_water:.3f} g/mol; pure water = {c_water:.1f} M; "
      f"water molecules per Na+ in 0.15 M NaCl = {c_water / 0.15:.0f}")

for medium, eps in [("vacuum", 1), ("nonpolar solvent (assumed)", 2), ("water", 80)]:
    print(f"Na+/Cl- at 2.8 Å in {medium:27s}: {-KE2 / (eps * 2.8):7.1f} kJ/mol")
print(f"RT at 298 K = {R * 298 / 1000:.2f} kJ/mol")
```

```text
H2O (bent)    net/bond = 1.224
CO2 (linear)  net/bond = 0.000
vacuum                      eps_r =  1  Bjerrum length =  560.8 Å
nonpolar solvent (assumed)  eps_r =  2  Bjerrum length =  280.4 Å
protein interior (assumed)  eps_r =  4  Bjerrum length =  140.2 Å
water                       eps_r = 80  Bjerrum length =    7.0 Å
M(H2O) = 18.015 g/mol; pure water = 55.5 M; water molecules per Na+ in 0.15 M NaCl = 370
Na+/Cl- at 2.8 Å in vacuum                     :  -496.2 kJ/mol
Na+/Cl- at 2.8 Å in nonpolar solvent (assumed) :  -248.1 kJ/mol
Na+/Cl- at 2.8 Å in water                      :    -6.2 kJ/mol
RT at 298 K = 2.48 kJ/mol
```

Atomic weights from Chemistry 2e;[^c2eaw] the permittivities 2 and 4 are illustrative assumptions, and treating water as a uniform continuum with $\varepsilon_r = 80$ fails at the scale of one or two molecules, where its structure matters.

## Worked example

> [!example] Why salt dissolves in water and not in oil
> 1. **Ion pair at contact** (2.8 Å, toy distance): $-496$ kJ/mol in vacuum, $-248$ kJ/mol in a nonpolar solvent ($\varepsilon_r = 2$, assumed), $-6.2$ kJ/mol in water (code output).
> 2. **Compare with thermal energy**, $RT = 2.48$ kJ/mol at 25 °C: the pair is held by about $200\,RT$ in vacuum, $100\,RT$ in the nonpolar solvent, but only $2.5\,RT$ in water.
> 3. **Add hydration.** In water each separated ion is also stabilized by its shell of oriented water molecules (ion-dipole), which oil cannot offer.[^c2e112]
> 4. **Conclusion**: in water, thermal motion and hydration pull the ions apart, so NaCl dissolves as Na⁺(aq) and Cl⁻(aq); in oil, the ions stay together in the crystal. Beyond $\ell_B \approx 7$ Å, two ions in water barely feel each other.

## Common misconceptions

> [!warning] "Water is polar because its bonds are polar"
> Polar bonds are necessary, not sufficient: CO₂ also has polar bonds and is nonpolar because it is linear. Water's bent shape is what leaves a net dipole.[^c2e7]

> [!warning] "Liquid water is a fixed, ice-like structure"
> The hydrogen bonds of liquid water break and re-form on a picosecond timescale; only ice has a fixed lattice.[^lehninger]

> [!warning] "Water repels nonpolar molecules"
> Water and a nonpolar molecule do attract weakly (dispersion). The problem is the cost of ordering water around the nonpolar surface, which clustering reduces ([[Hydrophobic Effect]]).[^lehninger]

## Exercises

> [!question] Exercise 1 (L1)
> Which of H₂O, CO₂, NH₃ and CH₄ are polar? Justify with geometry.

> [!success]- Solution
> H₂O: bent, polar. CO₂: linear, the two C=O dipoles cancel, nonpolar. NH₃: trigonal pyramidal (three bonds and a lone pair), the N–H dipoles add, polar. CH₄: tetrahedral and symmetric, with nearly nonpolar C–H bonds, nonpolar ([[Molecular Geometry]]).

> [!question] Exercise 2 (L1)
> How many hydrogen bonds can one water molecule make, and through which atoms? Draw how a water molecule orients next to Na⁺ and next to Cl⁻.

> [!success]- Solution
> Up to four: it donates two through its H atoms and accepts two through the lone pairs of O (four in ice, about 3.4 on average in the liquid).[^lehninger] Next to Na⁺ the oxygen (δ−) faces the ion; next to Cl⁻ one hydrogen (δ+) points at the ion (figure, panel 3).

> [!question] Exercise 3 (L2)
> Using the Bjerrum lengths above, explain why an isolated charged side chain is rarely buried in a protein core, while a buried pair of opposite charges can be tolerated.

> [!success]- Solution
> In water, a charge interacts with others only within about 7 Å and is stabilized by its hydration shell. Buried in a medium with $\varepsilon_r \approx 4$ (assumed), it loses the shell and its field is screened 20 times less ($\ell_B \approx 140$ Å): alone, it costs a large free energy. With a partner of opposite charge next to it, the strong unscreened attraction pays back part of that cost, so buried salt bridges occur, at specific positions.

> [!question] Exercise 4 (L2, Python)
> With `c_water` from the code, how many water molecules are there per solute particle for Na⁺ in 0.15 M NaCl, for a protein at 1 µM, and for H₃O⁺ in pure water at 25 °C ($1.0 \times 10^{-7}$ M)?

> [!success]- Solution
> ```python
> for solute, c in [("Na+ in 0.15 M NaCl", 0.15), ("protein at 1 uM", 1e-6), ("H3O+ in pure water, 25 C", 1.0e-7)]:
>     print(f"{solute:26s} {c_water / c:.2e} water molecules per solute")
> ```
> Output: `3.70e+02`, `5.55e+07` and `5.55e+08`. A ratio of concentrations is a ratio of numbers of particles: even at 150 mM, salt ions are surrounded by hundreds of water molecules, and a micromolar protein by tens of millions.

## Mastery checklist

- [ ] 1 Recognized: I can describe water as bent (104.5°), polar, with two donors and two acceptors.
- [ ] 2 Understood: I can explain hydration of ions, the role of the dielectric constant, and why nonpolar molecules do not dissolve.
- [ ] 3 Practiced: I can compute the molecular dipole from bond dipoles, screened Coulomb energies, the Bjerrum length and the molarity of water.
- [ ] 4 Applied: I related the surface exposure of charged and nonpolar residues in a real protein structure to water.
- [ ] 5 Explained: I can teach how water's shape leads to the hydrophobic effect, and where the continuum ($\varepsilon_r = 80$) picture fails.

## References

[^c2e82]: [[Chemistry 2e (OpenStax)]], ch. 8 "Advanced Theories of Covalent Bonding", §8.2 "Hybrid Atomic Orbitals" (water: sp3 oxygen, H–O–H angle 104.5°).
[^c2e7]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry" (bond polarity and molecular polarity: polar H₂O, nonpolar CO₂).
[^c2e101]: [[Chemistry 2e (OpenStax)]], ch. 10, §10.1 "Intermolecular Forces" (hydrogen bonding and the boiling points of the hydrides).
[^c2e112]: [[Chemistry 2e (OpenStax)]], ch. 11, §11.2 "Electrolytes" (ion-dipole attractions, hydration of K⁺ and Cl⁻ when KCl dissolves).
[^c2e14]: [[Chemistry 2e (OpenStax)]], ch. 14 "Acid-Base Equilibria" (autoionization of water, $K_w = 1.0 \times 10^{-14}$ at 25 °C).
[^c2e1]: [[Chemistry 2e (OpenStax)]], treatment of density (water, about 1.0 g/mL).
[^c2eaw]: [[Chemistry 2e (OpenStax)]], standard atomic weights (H 1.008, O 15.999, Na 22.990, Cl 35.45).
[^gas]: [[Chemistry 2e (OpenStax)]], treatment of the ideal gas law (gas constant $R$).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of water: hydrogen bonding in ice and liquid water (about 3.4 hydrogen bonds per molecule, lifetimes of 1 to 20 ps), dielectric constant and the dissolution of salts and polar molecules, ordered water around nonpolar solutes.
[^uphys]: [[University Physics (OpenStax)]], Volume 2: dielectrics (dielectric constant, representative values).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), §1.3 "Chemical Bonds in Biochemistry" treatment of the peptide bond (formed with loss of water) and of protein folding (nonpolar side chains buried, polar ones on the surface).
