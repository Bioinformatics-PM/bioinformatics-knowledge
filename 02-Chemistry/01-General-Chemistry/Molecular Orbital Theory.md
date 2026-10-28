---
aliases:
  - MO Theory
  - LCAO
  - Linear Combination of Atomic Orbitals
  - Bonding Orbital
  - Antibonding Orbital
  - HOMO
  - LUMO
  - Hückel Method
  - Théorie des orbitales moléculaires
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Atomic Orbital]]"
  - "[[Electron Configuration]]"
  - "[[Covalent Bond]]"
  - "[[Orbital Hybridization]]"
  - "[[Lewis Structure]]"
related:
  - "[[Resonance (Chemistry)]]"
  - "[[Aromaticity]]"
  - "[[Spectroscopy]]"
  - "[[Beer-Lambert Law]]"
  - "[[Photon]]"
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Adjacency Matrix]]"
  - "[[Nucleotide]]"
  - "[[Amino Acid]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[University Physics (OpenStax)]]"
---

# Molecular Orbital Theory

> [!abstract]
> Molecular orbital theory builds the orbitals of a whole molecule by combining atomic orbitals: in-phase combinations bond, out-of-phase combinations antibond, and in conjugated molecules the π orbitals spread over many atoms, which sets the ultraviolet absorption of nucleic acids and proteins.

## Definition

In **molecular orbital (MO) theory**, the electrons of a molecule occupy **molecular orbitals** that extend over the whole molecule. Each MO is approximated as a **linear combination of atomic orbitals (LCAO)**, and combining $n$ atomic orbitals gives $n$ MOs. A **bonding** orbital, an in-phase combination, concentrates electron density between the nuclei and lies below the atomic orbitals; an **antibonding** orbital (marked \*), an out-of-phase combination, has a node between the nuclei and lies above them. Electrons fill MOs by the aufbau principle, the Pauli principle and Hund's rule, and the **bond order** is (bonding electrons − antibonding electrons)/2.[^c2e84][^5111]

## Why it matters

- **A260 and A280.** The bases of nucleic acids absorb ultraviolet light near 260 nm and the side chains of Trp and Tyr near 280 nm:[^leh][^berg] electrons jumping between π orbitals of conjugated rings. UV quantification of DNA and of proteins rests on these transitions ([[Beer-Lambert Law]], [[Spectroscopy]]).
- **What Lewis structures miss.** The Lewis structure of O₂ pairs every electron, yet O₂ has two unpaired electrons; MO theory predicts them.[^c2e84] Bonds that need several resonance drawings ([[Resonance (Chemistry)]]) come out of a single set of delocalized orbitals.
- **Linear algebra on molecular graphs.** In the Hückel model, the π orbitals of a conjugated molecule are the eigenvectors of the [[Adjacency Matrix]] of its carbon skeleton, so orbital energies are graph eigenvalues ([[Eigenvalues and Eigenvectors]]).

## Core (L2)

![[mo-h2-and-conjugated-chain-levels.svg]]

### Two atoms: bonding and antibonding

- **H₂.** The two 1s orbitals combine into σ1s (bonding) and σ\*1s (antibonding). Both electrons go into σ1s: bond order (2 − 0)/2 = 1. In He₂, four electrons fill both orbitals: bond order 0, and no stable molecule forms.[^c2e84]
- **Signs decide.** The colors of an [[Atomic Orbital]] drawing (the sign of ψ) decide whether two overlapping orbitals reinforce each other between the nuclei (bonding) or cancel there (antibonding).
- **σ and π.** End-on overlap along the bond axis gives σ and σ\* orbitals; side-by-side overlap of parallel p orbitals gives π and π\* orbitals, with a nodal plane containing the axis ([[Orbital Hybridization]]).[^c2e84][^c2e83]
- **Second-row diatomics.** N₂ has bond order 3. O₂ has bond order 2, and its last two electrons occupy two degenerate π\*2p orbitals singly, so O₂ is paramagnetic. In B₂, C₂ and N₂, mixing of 2s and 2p pushes σ2p above π2p; in O₂ and F₂, σ2p stays below π2p.[^c2e84]
- **HOMO and LUMO.** The highest occupied and lowest unoccupied MOs are the **frontier orbitals**. The lowest-energy electronic excitation moves an electron from the HOMO to the LUMO by absorbing a photon of energy $\Delta E = hc/\lambda$ ([[Photon]]).[^os148][^chem6]

### Conjugated π systems

A chain of $N$ sp² atoms has $N$ parallel p orbitals, which combine into $N$ π orbitals spread over the whole chain. Butadiene's four p orbitals give ψ₁ to ψ₄, each with one more node than the one below; its four π electrons fill ψ₁ and ψ₂, so ψ₂ is the HOMO and ψ₃\* the LUMO, and its UV band is this π → π\* excitation.[^osdiene] As the chain grows, the levels crowd together and the HOMO-LUMO gap shrinks (figure): λmax moves from 217 nm (butadiene) to 258 nm (hexatriene) and 290 nm (octatetraene).[^os148] Closed rings of p orbitals follow the same algebra with periodic boundaries; [[Aromaticity]] derives their levels and the 4n + 2 rule.

### Bio: why 260 nm and 280 nm

- **Nucleobases.** Purines and pyrimidines are flat conjugated rings ([[Aromaticity]], [[Nucleotide]]) that absorb strongly near 260 nm.[^leh][^berg] A 260 nm photon carries $1240/260 = 4.77$ eV (460 kJ/mol): a π → π\* gap of the same size as in hexatriene (258 nm).
- **Aromatic amino acids.** Trp and Tyr, and to a much lesser extent Phe, absorb ultraviolet light, which is why proteins absorb near 280 nm (4.43 eV).[^leh] Trp's indole, two fused rings, is the largest π system of the three side chains. A protein with neither Trp nor Tyr therefore has almost no A280, whatever its concentration ([[Amino Acid]], [[Beer-Lambert Law]]).

## Advanced (L3)

### The Hückel model is an eigenvalue problem

Keep one p orbital per carbon of a planar conjugated hydrocarbon. Call $\alpha$ the energy of an electron in an isolated p orbital and $\beta < 0$ the interaction between bonded neighbours, and neglect all other interactions and overlaps, as in [[Aromaticity#Mathematical representation]]. The π Hamiltonian is

$$\mathbf H = \alpha \mathbf I + \beta \mathbf A,$$

where $\mathbf A$ is the adjacency matrix of the carbon skeleton. The MOs are the eigenvectors of $\mathbf A$ and their energies $E_k = \alpha + x_k\beta$, with $x_k$ the eigenvalues of $\mathbf A$; because $\beta < 0$, a larger $x_k$ means a lower level. For a linear chain of $N$ atoms,

$$x_k = 2\cos\frac{k\pi}{N + 1}, \qquad c_{kj} \propto \sin\frac{jk\pi}{N + 1}, \qquad \Delta E_{\text{HOMO-LUMO}} = 4|\beta|\sin\frac{\pi}{2(N + 1)} \quad (N \text{ even}),$$

for $k, j = 1, \dots, N$: orbital $k$ has $k - 1$ nodes, and the gap tends to 0 as $N \to \infty$.

### Where simple Hückel fails

Fitting $|\beta|$ on butadiene (217 nm) predicts 301 nm for hexatriene and 386 nm for octatetraene, against 258 and 290 nm measured (Computational representation): real gaps shrink more slowly than the model's. A single $\beta$ treats every C–C bond alike, whereas a polyene alternates double and single bonds. Giving the two kinds of bond different interactions keeps a finite gap even for an infinite chain (Exercise 5), and an affine fit through the three measured gaps extrapolates to a long-chain limit near 510 nm, in the visible (Exercise 4). The model ignores σ electrons and electron-electron repulsion: it explains trends and orderings, not absolute energies.

### Bond orders from orbitals

The π bond order between atoms $r$ and $s$ is $p_{rs} = \sum_k n_k\, c_{kr} c_{ks}$ over occupied MOs, with $n_k$ electrons in MO $k$ and normalized coefficients $c_{kr}$. For butadiene, $p_{12} = p_{34} = 0.894$ and $p_{23} = 0.447$ (Exercise 6): the formally single central bond has partial π character, the orbital counterpart of a resonance drawing with C2=C3 ([[Resonance (Chemistry)]]).

## Mathematical representation

- **Two identical atoms (LCAO).** $\psi = c_A\phi_A + c_B\phi_B$ with $H_{AA} = H_{BB} = \alpha$, $H_{AB} = \beta$ and overlap $S = \langle\phi_A|\phi_B\rangle$. The secular equation $\det(\mathbf H - E\mathbf S) = 0$ gives
$$E_\pm = \frac{\alpha \pm \beta}{1 \pm S}, \qquad \psi_\pm = \frac{\phi_A \pm \phi_B}{\sqrt{2(1 \pm S)}}.$$
Since $\beta < 0$, the in-phase $\psi_+$ is bonding and the out-of-phase $\psi_-$, which vanishes midway between the nuclei, is antibonding. With $S = 0$ this is the Hückel case, $E = \alpha \pm \beta$.
- **Bond order** $= \frac12(n_{\text{bonding}} - n_{\text{antibonding}})$; **π energy** $E_\pi = \sum_k n_k E_k$.
- **Absorption.** A photon is absorbed when $hc/\lambda = E_{\text{LUMO}} - E_{\text{HOMO}}$. With $h = 6.626 \times 10^{-34}$ J s and $c = 2.998 \times 10^8$ m/s,[^chem6] $hc = 1240$ eV nm, so $\lambda\,(\text{nm}) = 1240/\Delta E\,(\text{eV})$; 1 eV per molecule is 96.5 kJ/mol (using $e = 1.602 \times 10^{-19}$ C and $N_A = 6.022 \times 10^{23}$ mol⁻¹).[^c2e23][^c2e31]

## Computational representation

Filling a diatomic MO diagram is bookkeeping over an ordered list of levels:

```python
import math
import numpy as np

# Valence MO filling orders: (level, capacity, +1 bonding / -1 antibonding)
ORDER_1S = [("s1s", 2, +1), ("s*1s", 2, -1)]
ORDER_N2 = [("s2s", 2, +1), ("s*2s", 2, -1), ("p2p", 4, +1), ("s2p", 2, +1), ("p*2p", 4, -1), ("s*2p", 2, -1)]
ORDER_O2 = [("s2s", 2, +1), ("s*2s", 2, -1), ("s2p", 2, +1), ("p2p", 4, +1), ("p*2p", 4, -1), ("s*2p", 2, -1)]


def fill(n_electrons: int, order) -> tuple[float, int]:
    """Aufbau, Pauli and Hund: return (bond order, number of unpaired electrons)."""
    bonding = antibonding = unpaired = 0
    for _, capacity, sign in order:
        n = min(capacity, n_electrons)
        n_electrons -= n
        if sign > 0:
            bonding += n
        else:
            antibonding += n
        orbitals = capacity // 2                    # degenerate orbitals at this level
        unpaired += n if n <= orbitals else capacity - n
    return (bonding - antibonding) / 2, unpaired


for name, n, order in [("H2", 2, ORDER_1S), ("He2", 4, ORDER_1S), ("N2", 10, ORDER_N2),
                       ("O2", 12, ORDER_O2), ("F2", 14, ORDER_O2)]:
    print(name, *fill(n, order))
```

```text
H2 1.0 0
He2 0.0 0
N2 3.0 0
O2 2.0 2
F2 1.0 0
```

Hückel levels of a chain, by formula and by diagonalizing the adjacency matrix, then compared with measured spectra:

```python
HC = 6.626e-34 * 2.998e8 / 1.602e-19 * 1e9         # hc in eV nm (about 1240)


def chain_levels(n: int) -> list[float]:
    """x_k in E_k = alpha + x_k beta for a chain of n p orbitals, most bonding first."""
    return [2 * math.cos(k * math.pi / (n + 1)) for k in range(1, n + 1)]


def adjacency_chain(n: int) -> np.ndarray:
    a = np.zeros((n, n))
    for i in range(n - 1):
        a[i, i + 1] = a[i + 1, i] = 1.0
    return a


def gap(n: int) -> float:
    """HOMO-LUMO gap in units of |beta| for n atoms and n pi electrons (n even)."""
    x = chain_levels(n)
    return x[n // 2 - 1] - x[n // 2]


for n in (2, 4, 6, 8):
    agree = np.allclose(sorted(chain_levels(n)), np.linalg.eigvalsh(adjacency_chain(n)))
    print(n, [round(v, 3) for v in chain_levels(n)], agree, round(gap(n), 3))

measured = {4: 217, 6: 258, 8: 290}                  # lambda_max (nm): butadiene, hexatriene, octatetraene
beta = HC / measured[4] / gap(4)                     # |beta| fitted on butadiene only
print(f"hc = {HC:.0f} eV nm, |beta| = {beta:.2f} eV")
for n, lam in measured.items():
    e_obs, e_huckel = HC / lam, beta * gap(n)
    print(f"N={n}: observed {e_obs:.2f} eV ({lam} nm), Huckel {e_huckel:.2f} eV ({HC / e_huckel:.0f} nm)")
```

```text
2 [1.0, -1.0] True 2.0
4 [1.618, 0.618, -0.618, -1.618] True 1.236
6 [1.802, 1.247, 0.445, -0.445, -1.247, -1.802] True 0.89
8 [1.879, 1.532, 1.0, 0.347, -0.347, -1.0, -1.532, -1.879] True 0.695
hc = 1240 eV nm, |beta| = 4.62 eV
N=4: observed 5.71 eV (217 nm), Huckel 5.71 eV (217 nm)
N=6: observed 4.81 eV (258 nm), Huckel 4.11 eV (301 nm)
N=8: observed 4.28 eV (290 nm), Huckel 3.21 eV (386 nm)
```

The same `np.linalg.eigvalsh` call handles any skeleton, rings and branches included: only $\mathbf A$ changes.

## Worked example

> [!example] Butadiene by hand
> 1. **Matrix.** Four carbons in a row: $\mathbf A$ has 1 on the first off-diagonals. Its characteristic polynomial is $x^4 - 3x^2 + 1 = 0$, so $x^2 = (3 \pm \sqrt5)/2$ and $x = \pm 1.618, \pm 0.618$, as `chain_levels(4)` prints.
> 2. **Levels.** $\alpha + 1.618\beta$ (ψ₁), $\alpha + 0.618\beta$ (ψ₂), $\alpha - 0.618\beta$ (ψ₃\*), $\alpha - 1.618\beta$ (ψ₄\*). Four π electrons fill ψ₁ and ψ₂.
> 3. **Delocalization.** $E_\pi = 2(\alpha + 1.618\beta) + 2(\alpha + 0.618\beta) = 4\alpha + 4.472\beta$. Two isolated C=C bonds, each $2(\alpha + \beta)$, give $4\alpha + 4\beta$: conjugation adds $0.472\beta$, a stabilization since $\beta < 0$.
> 4. **Spectrum.** The gap is $1.236|\beta|$. Matching it to the measured 217 nm, 5.71 eV,[^os148] gives $|\beta| = 4.62$ eV.
> 5. **Prediction.** Hexatriene: $0.890 \times 4.62 = 4.11$ eV, that is 301 nm, against 258 nm measured.[^os148] The direction is right (longer than butadiene), the size is not: the reason for the L3 corrections.

## Common misconceptions

> [!warning] "Antibonding orbitals are empty orbitals that do nothing"
> Electrons placed in antibonding orbitals weaken the bond: they enter the bond order with a minus sign. He₂ has as many antibonding as bonding electrons and does not form;[^c2e84] adding electrons to π\* takes O₂ (order 2) to superoxide (1.5) and peroxide (1) (Exercise 1).

> [!warning] "Molecular orbitals belong to one bond"
> MOs belong to the whole molecule. Two-atom bonds are a good description of σ frameworks ([[Orbital Hybridization]]), but the π orbitals of butadiene, benzene or a nucleobase spread over all the conjugated atoms.

> [!warning] "A molecule absorbs only at the wavelength of its HOMO-LUMO gap"
> HOMO → LUMO is the lowest-energy excitation, not the only one, and each electronic transition of a molecule comes with vibrational sublevels that broaden it into a band ([[Spectroscopy]]).[^up]

## Exercises

> [!question] Exercise 1 (L2, Python)
> With `fill`, give the bond order and the number of unpaired electrons of O₂, O₂⁻ (superoxide), O₂²⁻ (peroxide), He₂⁺ and H₂⁺. Which are paramagnetic, and how should the O–O bond length change along O₂, O₂⁻, O₂²⁻?

> [!success]- Solution
> ```python
> for name, n, order in [("O2", 12, ORDER_O2), ("O2-", 13, ORDER_O2), ("O2 2-", 14, ORDER_O2),
>                        ("He2+", 3, ORDER_1S), ("H2+", 1, ORDER_1S)]:
>     print(name, *fill(n, order))
> ```
> Output: `O2 2.0 2`, `O2- 1.5 1`, `O2 2- 1.0 0`, `He2+ 0.5 1`, `H2+ 0.5 1`. Species with unpaired electrons are paramagnetic:[^c2e84] O₂, O₂⁻, He₂⁺ and H₂⁺. Each added electron enters π\*, so the bond order falls from 2 to 1 and the O–O bond should lengthen, as fewer shared pairs mean a longer bond ([[Covalent Bond]]). Unlike He₂, He₂⁺ keeps a net half bond: removing an electron from σ\*1s strengthens the bond.

> [!question] Exercise 2 (L2)
> Convert 217, 260 and 280 nm into eV and kJ/mol, and rank the HOMO-LUMO gaps of butadiene, the nucleobases and Trp/Tyr.

> [!success]- Solution
> $E = 1240/\lambda$: 5.71 eV (551 kJ/mol), 4.77 eV (460 kJ/mol), 4.43 eV (427 kJ/mol). Gaps: butadiene > nucleobases > Trp/Tyr. Larger conjugated π systems have smaller gaps; all three are far above thermal energy, $RT \approx 2.6$ kJ/mol at 37 °C, so the molecules sit in their ground state until a photon arrives ([[Spectroscopy]]).

> [!question] Exercise 3 (L2)
> Using $c_{kj} \propto \sin(jk\pi/5)$, write the signs of the four π MOs of butadiene on C1 to C4 and count their nodes. Between which atoms does the HOMO have a node, and what does that suggest about the C2–C3 bond?

> [!success]- Solution
> ψ₁: + + + + (0 nodes); ψ₂: + + − − (1 node, between C2 and C3); ψ₃\*: + − − + (2 nodes); ψ₄\*: + − + − (3 nodes). Values for ψ₂: 0.951, 0.588, −0.588, −0.951. The HOMO is antibonding between C2 and C3, but ψ₁, bonding everywhere and largest at C2 and C3, outweighs it: the net π bond order of C2–C3 is positive but smaller than that of C1–C2 (Exercise 6).

> [!question] Exercise 4 (L3, Python)
> Fit $\Delta E = E_0 + b\,g$, with $g$ the Hückel gap in units of $|\beta|$ (`gap(n)`), to the three measured polyenes by least squares. Report the residuals and the wavelength of the long-chain limit $E_0$.

> [!success]- Solution
> ```python
> xs = [gap(n) for n in measured]
> ys = [HC / lam for lam in measured.values()]
> slope, intercept = (float(v) for v in np.polyfit(xs, ys, 1))
> residuals = [round(y - (intercept + slope * x), 3) for x, y in zip(xs, ys)]
> print(f"E = {intercept:.2f} eV + {slope:.2f} eV x gap, residuals {residuals}, "
>       f"long-chain limit {HC / intercept:.0f} nm")
> ```
> Output: `E = 2.44 eV + 2.65 eV x gap, residuals [-0.003, 0.007, -0.005], long-chain limit 509 nm`. With an offset, the Hückel shape fits within 0.01 eV, and the effective $|\beta|$ drops to 2.65 eV. Three points and two parameters make this a description, not a test; the offset says the gap does not close for long chains.

> [!question] Exercise 5 (L3, Python)
> Give alternating bonds the interactions $1.1\beta$ (double) and $0.9\beta$ (single). Compute the HOMO-LUMO gap for chains of 4 to 64 atoms and compare with the uniform chain. What is the limit?

> [!success]- Solution
> ```python
> def alternating_gap(n: int, b_double: float = 1.1, b_single: float = 0.9) -> float:
>     """HOMO-LUMO gap (units of |beta|) when bonds alternate double, single, double, ..."""
>     a = np.zeros((n, n))
>     for i in range(n - 1):
>         a[i, i + 1] = a[i + 1, i] = b_double if i % 2 == 0 else b_single
>     x = np.sort(np.linalg.eigvalsh(a))[::-1]
>     return float(x[n // 2 - 1] - x[n // 2])
>
>
> for n in (4, 8, 16, 32, 64):
>     print(n, round(alternating_gap(n), 3), round(gap(n), 3))
> ```
> Output: `4 1.477 1.236`, `8 0.96 0.695`, `16 0.655 0.369`, `32 0.5 0.19`, `64 0.434 0.097`. The uniform gap goes to 0; the alternating one tends to $2|\beta_{\text{double}} - \beta_{\text{single}}| = 0.4|\beta|$, because for an infinite chain the levels form two bands separated by that amount. In this model, alternation is what keeps the gap open, the behaviour that the measured polyenes suggest (Exercise 4).

> [!question] Exercise 6 (L3, Python)
> Compute the π bond orders $p_{rs}$ of butadiene from the occupied eigenvectors of $\mathbf A$. Compare C1–C2 with C2–C3 and relate the result to resonance.

> [!success]- Solution
> ```python
> def pi_bond_orders(adj: np.ndarray, n_electrons: int) -> np.ndarray:
>     """p_rs = sum over occupied MOs of 2 c_kr c_ks (beta < 0: the largest eigenvalue is the lowest MO)."""
>     x, c = np.linalg.eigh(adj)
>     p = np.zeros_like(adj)
>     for k in np.argsort(x)[::-1][: n_electrons // 2]:
>         p += 2 * np.outer(c[:, k], c[:, k])
>     return p
>
>
> p = pi_bond_orders(adjacency_chain(4), 4)
> print(f"C1-C2 {p[0, 1]:.3f}, C2-C3 {p[1, 2]:.3f}, C3-C4 {p[2, 3]:.3f}")
> ```
> Output: `C1-C2 0.894, C2-C3 0.447, C3-C4 0.894`. The terminal bonds keep most, not all, of a full π bond (1), and the central "single" bond gains almost half of one: the delocalization that a resonance description would spread over several drawings, obtained here from one calculation.

## Mastery checklist

- [ ] 1 Recognized: I can define bonding, antibonding, σ, π, HOMO and LUMO, and compute a bond order.
- [ ] 2 Understood: I can explain why He₂ does not exist, why O₂ is paramagnetic, and why conjugation lowers the HOMO-LUMO gap.
- [ ] 3 Practiced: I can fill MO diagrams and diagonalize Hückel matrices in Python, and convert gaps into wavelengths.
- [ ] 4 Applied: I can explain a real UV spectrum of DNA or a protein (A260, A280, the A260/A280 ratio) in terms of the π systems of bases and aromatic residues.
- [ ] 5 Explained: I can teach the Hückel model as an eigenvalue problem on a molecular graph, including where and why it fails.

## References

[^c2e84]: [[Chemistry 2e (OpenStax)]], ch. 8 "Advanced Theories of Covalent Bonding", §8.4 "Molecular Orbital Theory" (LCAO; bonding and antibonding orbitals; σ and π MOs; bond order; H₂ and He₂; s-p mixing in second-period diatomics; paramagnetism of O₂).
[^c2e83]: [[Chemistry 2e (OpenStax)]], ch. 8, §8.3 "Multiple Bonds" (σ and π bonds).
[^chem6]: [[Chemistry 2e (OpenStax)]], ch. 6 "Electronic Structure and Periodic Properties of Elements" (photon energy $E = h\nu = hc/\lambda$, $h = 6.626 \times 10^{-34}$ J s, $c = 2.998 \times 10^8$ m/s).
[^c2e23]: [[Chemistry 2e (OpenStax)]], ch. 2, §2.3 "Atomic Structure and Symbolism" (charge of the electron, $1.602 \times 10^{-19}$ C).
[^c2e31]: [[Chemistry 2e (OpenStax)]], ch. 3, §3.1 "Formula Mass and the Mole Concept" (Avogadro's number, $6.022 \times 10^{23}$).
[^os148]: [[Organic Chemistry (OpenStax)]], §14.8 "Interpreting Ultraviolet Spectra: The Effect of Conjugation" (λmax 217 nm for 1,3-butadiene, 258 nm for 1,3,5-hexatriene, 290 nm for 1,3,5,7-octatetraene; the HOMO-LUMO gap decreases as conjugation increases).
[^osdiene]: [[Organic Chemistry (OpenStax)]], treatment of conjugated dienes and ultraviolet spectroscopy (the four π molecular orbitals of 1,3-butadiene, HOMO and LUMO, π → π\* excitation) (section not verified).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], course description (atomic and molecular electronic structure).
[^leh]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of light absorption by amino acids (Trp and Tyr, and to a much lesser extent Phe, absorb ultraviolet light; proteins absorb near 280 nm) and by nucleotides (bases absorb near 260 nm) (chapter numbers not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition (aromatic amino acids absorb near 280 nm) and of nucleic acid structure (UV absorbance of bases).
[^up]: [[University Physics (OpenStax)]], Volume 3, Unit 2 "Modern Physics" (molecular spectra with rotational and vibrational levels).
