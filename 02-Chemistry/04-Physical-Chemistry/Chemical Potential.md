---
aliases:
  - Partial Molar Gibbs Energy
  - μ
  - Electrochemical Potential
  - Potentiel chimique
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Gibbs Free Energy]]"
  - "[[Chemical Equilibrium]]"
  - "[[Ideal Gas Law]]"
  - "[[Partial Derivative]]"
  - "[[Logarithm]]"
related:
  - "[[Osmotic Pressure]]"
  - "[[Partition Coefficient]]"
  - "[[Nernst Equation]]"
  - "[[Membrane Potential]]"
  - "[[Electric Potential]]"
  - "[[Membrane Transport]]"
  - "[[Ligand Binding]]"
  - "[[Boltzmann Distribution]]"
  - "[[Thermodynamic Entropy]]"
projects: []
sources:
  - "[[IUPAC Gold Book]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Chemistry 2e (OpenStax)]]"
---

# Chemical Potential

> [!abstract]
> The chemical potential μ of a substance is the free energy that one more mole of it brings to a system; matter moves from where μ is high to where it is low until μ is equal everywhere the substance can go, and for a dilute solute μ rises by the same amount, RT ln 10, for every tenfold increase in concentration.

## Definition

The **chemical potential** of a species B in a mixture is the partial derivative of the Gibbs energy with respect to its amount, temperature, pressure and all other amounts being held constant:

$$\mu_B = \left(\frac{\partial G}{\partial n_B}\right)_{T,\,p,\,n_{C \neq B}};$$

for a pure substance it reduces to the molar Gibbs energy.[^iupac] For an ideal dilute solute at molar concentration $c$,

$$\mu = \mu^\circ + RT\ln\frac{c}{c^\circ},$$

where $\mu^\circ$ is its value in the standard state ($c^\circ = 1$ M), $R$ the gas constant and $T$ the absolute temperature.[^pboc] It is the per-mole, species-by-species form of [[Gibbs Free Energy]]: $\Delta G = \Delta G^\circ + RT\ln Q$ is a sum of such terms ([[Gibbs Free Energy#Mathematical representation]]).

## Why it matters

- **One rule for every passive process.** Diffusion across a membrane, ion flow through a channel, a drug dissolving into a lipid, water flowing into a cell and a ligand binding a receptor all stop when chemical potentials are equal. Transport models, [[Membrane Potential|membrane potentials]] and binding curves are bookkeeping of $\mu$.
- **Gradients are stored free energy.** The proton gradient of the [[Mitochondrion]] and the Na⁺ and K⁺ gradients of animal cells are differences of electrochemical potential, in kJ/mol, directly comparable with [[ATP]] hydrolysis.
- **Concentrations enter logarithmically.** A tenfold change of any metabolite, ligand or ion is worth the same 5.9 kJ/mol at 37 °C, which is why concentrations and $K_d$ values are compared on log scales ([[Chemical Equilibrium]]).
- **Partitioning and osmosis.** The [[Partition Coefficient]] (log P of drugs, hydrophobicity scales) and [[Osmotic Pressure]] are both equalities of chemical potential between two regions.

## Core (L2)

### Matter flows down its chemical potential

At constant temperature and pressure, $dG = \sum_i \mu_i\,dn_i$ ([[Gibbs Free Energy#Mathematical representation]]). Moving $dn$ mol of one species from region 1 to region 2 changes $G$ by $(\mu_2 - \mu_1)\,dn$: the transfer is spontaneous only if $\mu_2 < \mu_1$, and stops when $\mu_1 = \mu_2$. **Equilibrium is the equality of the chemical potential of each species everywhere it can go**: the minimum of $G$ ([[Gibbs Free Energy#Advanced (L3)]]) stated species by species.

### Concentration sets μ for a dilute solute

Dilute solute particles interact mostly with the solvent, and their chemical potential takes the logarithmic form of an ideal gas ([[Ideal Gas Law#Advanced (L3)]]).[^pboc] Two consequences:

- **Only differences are measured.** For one solute in one solvent, $\mu_2 - \mu_1 = RT\ln(c_2/c_1)$ and $\mu^\circ$ cancels. With $R = 8.314\,462\,618$ J mol⁻¹ K⁻¹,[^nist] a tenfold ratio is worth $RT\ln 10 = 5.71$ kJ/mol at 25 °C and 5.94 kJ/mol at 37 °C (figure, panel a).
- **$\mu^\circ$ holds the chemistry.** It depends on the species, the solvent and $T$. When the solvent differs between two regions (water and a lipid), the $\mu^\circ$ do not cancel, and equal chemical potentials mean *unequal* concentrations ([[Partition Coefficient]]).

![[chemical-potential-ladder.svg]]

### One condition, many equilibria

| Situation | Condition | Result |
|---|---|---|
| Uncharged solute, two water compartments, permeable membrane | $\mu_{\text{in}} = \mu_{\text{out}}$ | $c_{\text{in}} = c_{\text{out}}$ |
| Solute shared between water and oil | $\mu_{\text{w}} = \mu_{\text{o}}$ | $c_{\text{o}}/c_{\text{w}} = e^{-(\mu^\circ_{\text{o}} - \mu^\circ_{\text{w}})/RT}$ ([[Partition Coefficient]]) |
| Reaction $\sum_i \nu_i X_i = 0$ | $\sum_i \nu_i\mu_i = 0$ | $\prod_i (c_i/c^\circ)^{\nu_i} = K = e^{-\Delta_r G^\circ/RT}$ ([[Chemical Equilibrium]]) |
| Ion of charge $z$ across a membrane | $\mu + zF\phi$ equal on both sides | the [[Nernst Equation]] |
| Water across a membrane that holds back solute | $\mu_{\text{water}}$ equal | needs a pressure difference: [[Osmotic Pressure]] |

The third line *is* the law of mass action: substituting $\mu_i = \mu_i^\circ + RT\ln(c_i/c^\circ)$ into $\sum_i \nu_i\mu_i = 0$ gives $\sum_i \nu_i\mu_i^\circ = -RT\ln\prod_i (c_i/c^\circ)^{\nu_i}$, that is $\Delta_r G^\circ = -RT\ln K$.

### Bio: the driving force of transport, binding and osmosis

- **Transport.** Moving one mole of solute from concentration $c_1$ to $c_2$ changes its free energy by $RT\ln(c_2/c_1)$, plus $zF\Delta V$ for an ion of charge number $z$ crossing a potential difference $\Delta V$ ($F$: Faraday constant).[^berg] With about 145 mM Na⁺ outside and 5 to 15 mM inside[^alberts11] (take 10 mM) and a resting potential of −70 mV,[^ap] concentration and voltage each contribute about −7 kJ/mol to Na⁺ entry (figure, panel b; the same numbers in $k_BT$ units are in [[Electric Potential#Worked example]]). A transporter can spend this downhill flow to push another solute uphill (Worked example; [[Membrane Transport]]).
- **Binding.** For $\mathrm{P + L \rightleftharpoons PL}$, equilibrium means $\mu_{\mathrm{PL}} = \mu_{\mathrm{P}} + \mu_{\mathrm{L}}$, which gives back $K_d$ (Exercise 3). Read the other way, a binding site measures its ligand's chemical potential: occupancy is a logistic function of $\mu_{\mathrm{L}}$, half-saturated at $\mu_{\mathrm{L}} - \mu_{\mathrm{L}}^\circ = RT\ln(K_d/c^\circ)$ ([[Ligand Binding]], Mathematical representation).
- **Osmosis.** Dissolved solutes lower the chemical potential of water, so water moves toward the more concentrated side; the pressure that stops it is the [[Osmotic Pressure]].[^pboc]

## Advanced (L3)

- **Electrochemical potential.** For an ion, the quantity that equalizes is $\tilde\mu = \mu^\circ + RT\ln(c/c^\circ) + zF\phi$, with $\phi$ the local [[Electric Potential|electric potential]]. Setting $\tilde\mu_{\text{in}} = \tilde\mu_{\text{out}}$ gives the [[Nernst Equation]], and the proton-motive force of the [[Mitochondrion]] is $\Delta\tilde\mu_{\mathrm{H^+}}/F$. An ion can thus be at equilibrium with very different concentrations on the two sides (Exercise 4).
- **Activities.** The ideal form holds for dilute solutes only. In general $\mu = \mu^\circ + RT\ln a$, with activity $a = \gamma\,c/c^\circ$ and an activity coefficient $\gamma$ that departs from 1 when solute particles interact with each other, for example in concentrated salt solutions; equilibrium constants are, strictly, ratios of activities.[^chem13] The term $RT\ln\gamma$, the excess chemical potential, collects every interaction beyond ideal mixing ([[Binding Free Energy]]).
- **Gibbs-Duhem.** For a homogeneous phase $G = \sum_i n_i\mu_i$ (doubling every amount doubles $G$ at fixed intensive $\mu_i$). Comparing its differential with $dG = \sum_i \mu_i\,dn_i$ gives $\sum_i n_i\,d\mu_i = 0$ at constant $T$ and $p$: the chemical potentials of a mixture cannot change independently. Adding solute raises $\mu_{\text{solute}}$ and *must* lower $\mu_{\text{water}}$ (Exercise 5), the root of osmosis.
- **The Boltzmann reading.** Per molecule, $\mu/N_A = \mu^\circ/N_A + k_BT\ln(c/c^\circ)$. If a molecule also has a potential energy $U(x)$ (gravity, a centrifuge, a voltage), equal total chemical potential everywhere gives $c(x) \propto e^{-U(x)/k_BT}$: equilibrium concentration profiles are [[Boltzmann Distribution|Boltzmann distributions]],[^pboc] and the partition and Nernst results above are their two-region versions.

## Mathematical representation

- $\mu_i = (\partial G/\partial n_i)_{T,p,n_{j\neq i}}$; $dG = -S\,dT + V\,dp + \sum_i \mu_i\,dn_i$; $G = \sum_i n_i\mu_i$; Gibbs-Duhem $\sum_i n_i\,d\mu_i = 0$ at constant $T, p$.
- Ideal dilute solute: $\mu_i = \mu_i^\circ + RT\ln(c_i/c^\circ)$; in general $\mu_i = \mu_i^\circ + RT\ln a_i$.
- Electrochemical potential: $\tilde\mu_i = \mu_i + z_iF\phi$. Transfer from region 1 to region 2: $\Delta\tilde\mu = RT\ln(c_2/c_1) + zF(\phi_2 - \phi_1)$.
- Equilibrium: $\mu_i^{\alpha} = \mu_i^{\beta}$ for every species exchanged between regions $\alpha$ and $\beta$; $\sum_i \nu_i\mu_i = 0$ for every reaction.
- Occupancy of a site of dissociation constant $K_d$: since $c/c^\circ = e^{(\mu_{\mathrm{L}} - \mu_{\mathrm{L}}^\circ)/RT}$,
$$\theta = \frac{c}{c + K_d} = \frac{1}{1 + e^{-(\mu_{\mathrm{L}} - \mu_{1/2})/RT}}, \qquad \mu_{1/2} = \mu_{\mathrm{L}}^\circ + RT\ln\frac{K_d}{c^\circ}.$$
Going from $\theta = 0.1$ to $0.9$ takes $\Delta\mu_{\mathrm{L}} = 2RT\ln 9$, a factor 81 in concentration (Exercise 6).

## Computational representation

Work in kJ/mol with $R$ and $F$ from CODATA[^nist] (with $F$ in kJ V⁻¹ mol⁻¹, $zF\Delta V$ comes out in kJ/mol):

```python
import math

R = 8.314462618e-3   # molar gas constant, kJ/(mol K), CODATA (exact)
F = 96.48533212      # Faraday constant N_A e, kJ/(V mol), CODATA (exact)
T37 = 310.15         # K


def mu_rel(c: float, t: float = T37, c0: float = 1.0) -> float:
    """mu - mu0 (kJ/mol) of an ideal dilute solute at concentration c (M, standard state 1 M)."""
    return R * t * math.log(c / c0)


def transfer(c_from: float, c_to: float, z: int = 0, v_from: float = 0.0,
             v_to: float = 0.0, t: float = T37) -> float:
    """Change of (electro)chemical potential, kJ/mol, for 1 mol moved between compartments.

    Concentrations in any common unit, electric potentials in volts.
    """
    return R * t * math.log(c_to / c_from) + z * F * (v_to - v_from)


def occupancy(mu_ligand: float, kd: float, t: float = T37) -> float:
    """Bound fraction of a site when the free ligand has mu - mu0 = mu_ligand (kJ/mol); Kd in M."""
    mu_half = R * t * math.log(kd)          # mu - mu0 of the ligand at c = Kd
    return 1 / (1 + math.exp(-(mu_ligand - mu_half) / (R * t)))


for c in (1e-6, 1e-3, 1.0):
    print(f"c = {c:g} M: mu - mu0 = {mu_rel(c):6.2f} kJ/mol")
print(f"per tenfold change: {R * T37 * math.log(10):.2f} kJ/mol")

# Na+ entering a mammalian cell: 145 mM outside, 10 mM inside, V_m = -70 mV
chem = transfer(145, 10)
total = transfer(145, 10, z=+1, v_from=0.0, v_to=-0.070)
print(f"Na+ entry: {chem:.2f} (concentration) + {total - chem:.2f} (voltage) = {total:.2f} kJ/mol")

# a binding site with Kd = 1 uM reads the chemical potential of its ligand
for c in (1e-7, 1e-6, 1e-5):
    print(f"[L] = {c:g} M: theta = {occupancy(mu_rel(c), 1e-6):.3f}, c/(c + Kd) = {c / (c + 1e-6):.3f}")

for n in (1, 2):   # ceiling of a symporter coupling n Na+ to one glucose (Worked example)
    ratio = math.exp(-n * total / (R * T37))
    print(f"n = {n}: glucose in/out up to {ratio:.3g}")
```

```text
c = 1e-06 M: mu - mu0 = -35.63 kJ/mol
c = 0.001 M: mu - mu0 = -17.81 kJ/mol
c = 1 M: mu - mu0 =   0.00 kJ/mol
per tenfold change: 5.94 kJ/mol
Na+ entry: -6.90 (concentration) + -6.75 (voltage) = -13.65 kJ/mol
[L] = 1e-07 M: theta = 0.091, c/(c + Kd) = 0.091
[L] = 1e-06 M: theta = 0.500, c/(c + Kd) = 0.500
[L] = 1e-05 M: theta = 0.909, c/(c + Kd) = 0.909
n = 1: glucose in/out up to 199
n = 2: glucose in/out up to 3.96e+04
```

The occupancy computed from $\mu$ matches $c/(c + K_d)$, as the algebra requires. Keep concentrations in one unit per call: only their ratio enters `transfer`, but `mu_rel` needs molar units because of the 1 M standard state.

## Worked example

> [!example] How far can Na⁺ entry concentrate glucose?
> A symporter carries $n$ Na⁺ ions and one glucose molecule into the cell together ($n$ left general). Conditions as above: Na⁺ 145 mM outside, 10 mM inside, $V_m = -70$ mV, 37 °C.
> 1. **Driving force per Na⁺**: $\Delta\tilde\mu_{\mathrm{Na}} = RT\ln(10/145) + F(-0.070\ \mathrm{V}) = -6.90 - 6.75 = -13.65$ kJ/mol.
> 2. **Coupled process**: $n\,\mathrm{Na^+_{out}} + \mathrm{Glc_{out}} \to n\,\mathrm{Na^+_{in}} + \mathrm{Glc_{in}}$ has $\Delta G = n\,\Delta\tilde\mu_{\mathrm{Na}} + RT\ln([\mathrm{Glc}]_{\text{in}}/[\mathrm{Glc}]_{\text{out}})$; glucose is uncharged, so it has no voltage term.
> 3. **Ceiling**: uptake stops when $\Delta G = 0$, at $[\mathrm{Glc}]_{\text{in}}/[\mathrm{Glc}]_{\text{out}} = e^{-n\Delta\tilde\mu_{\mathrm{Na}}/RT} = e^{5.29\,n}$: 199 for $n = 1$ and $4.0 \times 10^4$ for $n = 2$ (code).
> 4. **Read it**: coupling adds free energies, so it multiplies the achievable ratios; each extra Na⁺ per cycle buys a factor of about 200. A cell may stay below this ceiling (uptake competes with leaks and consumption), but no mechanism can exceed it.

## Common misconceptions

> [!warning] "Solutes always move from high to low concentration"
> They move from high to low **chemical potential**. An ion can move against its concentration gradient when the voltage term wins, and a drug accumulates in a lipid phase where its $\mu^\circ$ is lower: equal $\mu$, unequal concentrations ([[Partition Coefficient]]).

> [!warning] "At equilibrium, concentrations are equal on both sides of a membrane"
> Only for an uncharged, unbound solute in the same solvent. Ions follow the [[Nernst Equation]]; a ligand bound to proteins on one side has the same *free* concentration on both sides but a higher *total* concentration where the proteins are (Exercise 2).

> [!warning] "μ° is the chemical potential of the substance"
> It is the value in a chosen standard state (1 M ideal solute, 1 bar gas, pure solvent). Changing the convention shifts $\mu^\circ$ and the logarithmic term together; only the full $\mu$, and differences taken with one convention, are physical.

> [!warning] "The RT ln c term is an interaction energy"
> In an ideal solution nothing changes in the interactions when the solute is diluted: the $RT\ln c$ term is entropic, the entropy of mixing of the solute among the solvent ([[Thermodynamic Entropy]]). That is why it is the same for every solute.

## Exercises

> [!question] Exercise 1 (L2)
> Compute $\mu - \mu^\circ$ of glucose at 5 mM and 37 °C, and how much it changes when the concentration rises tenfold.

> [!success]- Solution
> $\mu - \mu^\circ = RT\ln(0.005) = 2.579 \times (-5.298) = -13.66$ kJ/mol; `mu_rel(0.005)` gives the same. A tenfold rise adds $RT\ln 10 = +5.94$ kJ/mol, whatever the starting concentration.

> [!question] Exercise 2 (L2)
> An uncharged drug crosses a cell membrane freely. Inside the cell, 30 % of the drug molecules are bound to proteins (invented value). At equilibrium, what is the ratio of total drug concentrations inside and outside?

> [!success]- Solution
> Only the free drug has a chemical potential to equalize: $c_{\text{free,in}} = c_{\text{out}}$. Inside, free drug is 70 % of the total, so $c_{\text{total,in}}/c_{\text{out}} = 1/0.7 = 1.43$. Accumulation without any pump: binding lowers the free fraction, not the free concentration.

> [!question] Exercise 3 (L2)
> Starting from $\mu_{\mathrm{PL}} = \mu_{\mathrm{P}} + \mu_{\mathrm{L}}$ with ideal dilute chemical potentials, derive $K_d = [\mathrm{P}][\mathrm{L}]/[\mathrm{PL}]$ and the binding free energy $\Delta G^\circ_{\text{bind}} = RT\ln(K_d/c^\circ)$.

> [!success]- Solution
> Write each $\mu_X = \mu_X^\circ + RT\ln([X]/c^\circ)$. Then $RT\ln\dfrac{[\mathrm{P}][\mathrm{L}]}{[\mathrm{PL}]\,c^\circ} = \mu_{\mathrm{PL}}^\circ - \mu_{\mathrm{P}}^\circ - \mu_{\mathrm{L}}^\circ = \Delta G^\circ_{\text{bind}}$. The left side contains a constant ratio, $K_d/c^\circ$, so $K_d/c^\circ = e^{\Delta G^\circ_{\text{bind}}/RT}$: the result used in [[Chemical Equilibrium#Deeper (L2)]].

> [!question] Exercise 4 (L3, Python)
> Chloride is about 110 mM outside a mammalian cell and 5 to 15 mM inside.[^alberts11] With `transfer`, compute the free energy of Cl⁻ entry at $V_m = -70$ mV for 5, 10 and 15 mM inside, and compare with Na⁺.

> [!success]- Solution
> ```python
> for c_in in (5, 10, 15):
>     print(f"Cl- in = {c_in:2d} mM: dG(entry) = {transfer(110, c_in, z=-1, v_to=-0.070):+.2f} kJ/mol")
> ```
> ```text
> Cl- in =  5 mM: dG(entry) = -1.22 kJ/mol
> Cl- in = 10 mM: dG(entry) = +0.57 kJ/mol
> Cl- in = 15 mM: dG(entry) = +1.62 kJ/mol
> ```
> The concentration term pulls Cl⁻ in (about −6 kJ/mol at 10 mM) and the negative inside pushes the anion out (+6.75 kJ/mol): the two almost cancel. Cl⁻ sits within about 1.6 kJ/mol of equilibrium, against −13.65 kJ/mol for Na⁺, which is why its equilibrium potential lies close to the resting potential ([[Membrane Potential]]).

> [!question] Exercise 5 (L3)
> In a dilute solution of $n_s$ mol of solute in $n_w$ mol of water, use Gibbs-Duhem with $d\mu_s = RT\,dn_s/n_s$ to show that $\mu_w - \mu_w^* \approx -RT\,n_s/n_w$. Express it with the solute concentration $c_s$ and the molar volume of water $\bar V_w$, and compute $-(\mu_w - \mu_w^*)/\bar V_w$ for $c_s = 0.30$ M at 37 °C.

> [!success]- Solution
> $n_w\,d\mu_w + n_s\,d\mu_s = 0$ gives $d\mu_w = -(n_s/n_w)(RT/n_s)\,dn_s = -RT\,dn_s/n_w$; integrating from $n_s = 0$, $\mu_w - \mu_w^* = -RT\,n_s/n_w$. In a dilute solution $n_w \approx V/\bar V_w$, so $\mu_w - \mu_w^* \approx -RT\,c_s\bar V_w$ (with $\bar V_w = 1/55.5$ L/mol, from the 55.5 M of pure water). Dividing by $\bar V_w$: $RT\,c_s = 8.314 \times 310.15 \times 300 = 7.7 \times 10^5$ Pa. This is a pressure: exactly the van 't Hoff osmotic pressure $\Pi = cRT$ ([[Osmotic Pressure]]).

> [!question] Exercise 6 (L3, Python)
> Over what range of ligand chemical potential does a non-cooperative site go from 10 % to 90 % occupancy, and what concentration factor is that?

> [!success]- Solution
> Invert the logistic: $\mu_{\mathrm{L}} - \mu_{\mathrm{L}}^\circ = RT\ln K_d + RT\ln(\theta/(1-\theta))$.
> ```python
> def mu_for(theta, kd, t=T37):
>     return R * t * math.log(kd) + R * t * math.log(theta / (1 - theta))
> lo, hi = mu_for(0.1, 1e-6), mu_for(0.9, 1e-6)
> print(f"mu window 10% -> 90%: {hi - lo:.2f} kJ/mol, concentration factor {math.exp((hi - lo) / (R * T37)):.1f}")
> ```
> Output: `mu window 10% -> 90%: 11.33 kJ/mol, concentration factor 81.0`, independent of $K_d$. A simple site needs an 81-fold change in ligand concentration to switch; sharper responses need [[Cooperativity]].

## Mastery checklist

- [ ] 1 Recognized: I can define μ as the partial molar Gibbs energy and write $\mu = \mu^\circ + RT\ln(c/c^\circ)$.
- [ ] 2 Understood: I can explain why matter flows toward lower μ, why equal μ can mean unequal concentrations (ions, partition, binding), and how $K$ follows from $\sum_i \nu_i\mu_i = 0$.
- [ ] 3 Practiced: I can compute transport free energies with concentration and voltage terms, coupling ceilings and occupancies in Python.
- [ ] 4 Applied: given measured concentrations and potentials from a paper or database, I can decide which fluxes are downhill and by how much.
- [ ] 5 Explained: I can teach the electrochemical potential, activities and Gibbs-Duhem, and show that the Boltzmann, Nernst, partition and osmotic results are all equalities of μ.

## References

[^iupac]: [[IUPAC Gold Book]], entry "chemical potential, $\mu_B$" (C01032): $\mu_B = (\partial G/\partial n_B)_{T,p,n_{C\neq B}}$; for a pure substance, the molar Gibbs energy.
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of the free energy of dilute solutions (chemical potential $\mu = \mu_0 + k_BT\ln(c/c_0)$), of osmotic pressure and of the Boltzmann distribution (chapters not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of membrane transport (free energy of moving a solute between concentrations $c_1$ and $c_2$, $\Delta G = RT\ln(c_2/c_1)$, plus $ZF\Delta V$ for a charged species).
[^alberts11]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 11, Table 11-1 (ion concentrations inside and outside a typical mammalian cell).
[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], nervous tissue chapter (resting membrane potential of a neuron, about −70 mV).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA: molar gas constant $R = 8.314\,462\,618\ldots$ J mol⁻¹ K⁻¹ and Faraday constant $F = N_A e = 96\,485.332\,12\ldots$ C mol⁻¹, both exact since the 2019 SI.
[^chem13]: [[Chemistry 2e (OpenStax)]], ch. 13 "Fundamental Equilibrium Concepts" (equilibrium constants strictly expressed with activities, hence dimensionless).
