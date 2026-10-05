---
aliases:
  - Cytosquelette
  - Actin Filament
  - Microfilament
  - Microtubule
  - Intermediate Filament
  - Centrosome
  - Dynamic Instability
tags:
  - type/concept
  - domain/biology
  - domain/physics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Eukaryote]]"
  - "[[Organelle]]"
  - "[[Protein]]"
  - "[[ATP]]"
related:
  - "[[Molecular Motor]]"
  - "[[Endomembrane System]]"
  - "[[Cell Nucleus]]"
  - "[[Mitosis]]"
  - "[[Cell Cycle]]"
  - "[[Diffusion]]"
  - "[[Protein Quaternary Structure]]"
  - "[[Microscopy]]"
  - "[[Continuous-Time Markov Chain]]"
  - "[[Cell Type Annotation]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[The Cell (Cooper)]]"
  - "[[Gene Ontology]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# Cytoskeleton

> [!abstract]
> The cytoskeleton is a network of protein filaments, constantly built and taken apart, that gives a eukaryotic cell its shape, serves as tracks for transport inside it and pulls it in two when it divides.

## Definition

The **cytoskeleton** is the system of protein filaments that runs through the cytoplasm of eukaryotic cells. It has three kinds of filaments, each a polymer of a different protein: **actin filaments** (microfilaments), **microtubules** and **intermediate filaments**. Accessory proteins control where and when the filaments assemble, and **motor proteins** move along actin filaments and microtubules.[^os45][^alberts16][^cooper]

## Why it matters

- **Cancer drugs target it.** A dividing cell needs a dynamic mitotic spindle; drugs that block microtubule assembly or disassembly arrest cells in mitosis, and some, such as taxol, are used against cancer.[^alberts16] Mechanism-of-action work in [[Drug Discovery]] starts from this biology.
- **Localization annotation.** The Gene Ontology records where a gene product acts in its cellular component aspect;[^go] filaments, the centrosome and cilia are among those locations ([[Gene Annotation]]).
- **Cell-type markers.** Intermediate filament proteins differ between cell types: keratins in epithelia, vimentin in many mesenchymal cells, neurofilaments in neurons.[^alberts16] Their genes are natural candidates for [[Cell Type Annotation]] in single-cell data (Exercise 6).
- **Images show it.** Actin filaments are routinely stained with fluorescent phalloidin, a toxin that binds them tightly,[^alberts16] so cell shape in fluorescence images is largely cytoskeleton ([[Microscopy]]).
- **A classic modeling playground.** Polymerization, dynamic instability and motor transport are textbook cases of rate equations and two-state stochastic processes (Mathematical representation), the tools of [[Systems Biology]].

## Core (L1)

![[cytoskeleton-filament-types.svg]]

| | Actin filaments (microfilaments) | Microtubules | Intermediate filaments |
|---|---|---|---|
| Subunit | actin, a globular protein that binds ATP | αβ-tubulin dimer, which binds GTP | fibrous proteins: keratins, vimentin, neurofilament proteins, lamins |
| Diameter | about 7 nm | about 25 nm, a hollow tube | 8 to 10 nm, ropelike |
| Polarity | yes: a slow minus end, a fast-growing plus end | yes: minus and plus ends | none |
| Motors | myosins | kinesins, dyneins | none |
| Main roles | cortex and shape changes, crawling, muscle contraction, cytokinesis | tracks for organelles and vesicles, mitotic spindle, cilia and flagella | mechanical strength, nuclear lamina |

Diameters and roles from OpenStax,[^os45] subunits, polarity and motors from Alberts.[^alberts16]

**Shape.** A meshwork of actin filaments under the plasma membrane, the **cell cortex**, sets the shape of the cell surface and lets it change.[^alberts16] Intermediate filaments bear tension: in epithelia, keratin networks are anchored at junctions between cells, which spreads mechanical stress across the whole sheet.[^alberts16][^os45] Inside the nucleus, lamins form the nuclear lamina that supports the envelope ([[Cell Nucleus]]).[^alberts16]

**Transport.** In an animal cell, most microtubules grow from the **centrosome** near the nucleus, minus ends anchored there and plus ends toward the cell periphery.[^alberts16] Motor proteins hydrolyze ATP to walk along them, carrying vesicles and organelles: most **kinesins** move toward the plus end (outward), **dyneins** toward the minus end (inward).[^alberts16] This is how vesicles of the [[Endomembrane System]] travel between compartments; myosins carry some cargo along actin filaments.[^alberts16] The mechanics of motors are covered in [[Molecular Motor]].

**Division.** At mitosis the microtubules reorganize into the **mitotic spindle**, which separates the chromosomes ([[Mitosis]]); a **contractile ring** of actin and myosin then pinches an animal cell in two.[^os45][^alberts18] The centrosome is duplicated once per [[Cell Cycle]], before division.[^os45][^alberts18]

**Movement.** Cilia and flagella contain a bundle of microtubules in a "9 + 2" array, nine doublets around two central microtubules, bent by dynein motors.[^os45][^alberts16] A crawling cell pushes its front edge forward by polymerizing actin; muscle contracts as myosin pulls on actin filaments.[^alberts16]

## Deeper (L2)

### Assembly: nucleotides, ends and critical concentration

Each actin subunit carries ATP, each β-tubulin GTP, and the nucleotide is hydrolyzed shortly after the subunit joins a filament; subunits still carrying ATP or GTP bind more tightly than those carrying ADP or GDP.[^alberts16] A filament grows when the free subunit concentration exceeds a **critical concentration** and shrinks below it, and subunits add faster at the plus end.[^alberts16] Without hydrolysis both ends would share one critical concentration; hydrolysis makes them differ, so at intermediate concentrations a filament adds subunits at its plus end while losing them at its minus end. This **treadmilling** is typical of actin filaments.[^alberts16]

### Dynamic instability

Single microtubules switch abruptly between slow growth and rapid shrinkage. A growing end keeps a cap of GTP-tubulin; when hydrolysis catches up and the cap is lost, the end depolymerizes quickly (**catastrophe**), and regaining a cap stops the shrinkage (**rescue**).[^alberts16] This lets microtubules probe the cytoplasm and be stabilized where they meet a target, such as the kinetochore of a chromosome during spindle assembly.[^alberts18]

### Nucleation and motors

Starting a new filament is the slow step, so cells decide where filaments form. The centrosome nucleates microtubules from rings of γ-tubulin; in animal cells it also holds a pair of centrioles.[^alberts16][^os45] At the leading edge of a crawling cell, the ARP complex (Arp2/3) starts new actin filaments as branches on existing ones, building a growing network.[^alberts16] Motors then use the filaments: myosins move along actin filaments, most toward the plus end, and each motor couples ATP hydrolysis to a change of shape; conventional kinesin advances 8 nm per step, the length of one tubulin dimer.[^alberts16]

### Intermediate filaments: strength without polarity

An intermediate filament protein has a central α-helical rod. Two rods wind into a coiled-coil dimer, and two dimers pair in opposite orientations into a tetramer, so the finished filament has no polarity and no motor walks along it.[^alberts16] The families are characteristic of cell types:[^alberts16]

| Family | Found in |
|---|---|
| keratins | epithelial cells, hair and nails |
| vimentin and related proteins (desmin, glial fibrillary acidic protein) | many mesenchymal cells; muscle; glial cells |
| neurofilaments | neurons |
| nuclear lamins | the nucleus of all animal cells |

Mutations in keratin genes make the skin blister under mild mechanical stress (epidermolysis bullosa simplex).[^alberts16]

## Advanced (L3)

- **Search and capture.** Without rescue, a microtubule grows for a random time before a catastrophe, so its chance of reaching a target falls exponentially with distance (Mathematical representation). The spindle exploits this: many short-lived microtubules probe space until kinetochores capture and stabilize them, and the [[Mitosis#Deeper (L2)|spindle checkpoint]] waits for the last attachment.[^alberts18]
- **Mechanics.** The three polymers respond differently to force: microtubules are the stiffest, actin filaments are more flexible, and intermediate filaments bend easily but are very hard to break, which suits their role of absorbing stress.[^alberts16] Physical models treat filaments as elastic beams to quantify these differences.[^phillips]
- **Long-distance transport needs motors.** Diffusion time grows with the square of the distance, motor time only linearly, so beyond a few micrometers motors win, and along an axon diffusion is hopeless (Worked example, [[Diffusion]]). Neurons carry organelles along axonal microtubules with kinesins and dyneins.[^alberts16]
- **Drugs.** Colchicine and vinblastine bind free tubulin and block polymerization; taxol binds microtubules and stabilizes them; cytochalasin caps actin filament plus ends; phalloidin stabilizes actin filaments.[^alberts16] Freezing the spindle and dissolving it both block mitosis, which is why antimitotic drugs hit proliferating cells hardest ([[Cancer]]).[^alberts16]

## Mathematical representation

**Polymerization at one end.** Let $c$ be the free subunit concentration (µM), $k_{\mathrm{on}}$ the association rate constant (µM⁻¹ s⁻¹), $k_{\mathrm{off}}$ the dissociation rate constant (s⁻¹) and $n$ the number of subunits in the filament. By mass action, one end changes as

$$\frac{dn}{dt} = k_{\mathrm{on}}\,c - k_{\mathrm{off}},$$

which vanishes at the **critical concentration** $c_c = k_{\mathrm{off}}/k_{\mathrm{on}}$: the end grows for $c > c_c$ and shrinks for $c < c_c$. With both ends (superscripts $+$ and $-$), the filament is at steady state when

$$c_{ss} = \frac{k^{+}_{\mathrm{off}} + k^{-}_{\mathrm{off}}}{k^{+}_{\mathrm{on}} + k^{-}_{\mathrm{on}}} = \frac{k^{+}_{\mathrm{on}}\,c_c^{+} + k^{-}_{\mathrm{on}}\,c_c^{-}}{k^{+}_{\mathrm{on}} + k^{-}_{\mathrm{on}}},$$

a weighted average of the two critical concentrations, so it lies between them. If $c_c^{+} < c_c^{-}$, at $c_{ss}$ the plus end grows exactly as fast as the minus end shrinks: treadmilling.

**Dynamic instability.** Model a microtubule end as a two-state process ([[Continuous-Time Markov Chain]]): growing at speed $v_g$ or shrinking at speed $v_s$, switching to shrinkage at the catastrophe rate $f_c$ and back at the rescue rate $f_r$. In the long run the end grows a fraction $p_g = f_r/(f_c + f_r)$ of the time, so its mean velocity is

$$V = p_g\,v_g - (1 - p_g)\,v_s = \frac{v_g f_r - v_s f_c}{f_c + f_r}.$$

For $V > 0$ microtubules grow without bound; for $V < 0$ their lengths stay bounded, and changing $f_c$ or $f_r$ moves the system between the two regimes. Without rescue, a growth phase lasts an exponential time of mean $1/f_c$ ([[Exponential Distribution]]), so a microtubule growing toward a target at distance $x$ reaches it with probability

$$P(\text{reach } x) = e^{-f_c x / v_g}.$$

**Diffusion versus motors.** A particle with diffusion coefficient $D$ needs about $t_D = x^2/(2D)$ to travel a distance $x$ in one dimension ([[Diffusion]]); a motor at speed $v$ needs $t_M = x/v$. The ratio $t_D/t_M = xv/(2D)$ exceeds 1 beyond $x^* = 2D/v$.

## Computational representation

The code checks the drift formula and the reach probability by exact simulation, and compares the two transport laws. All parameter values are illustrative, not measurements.

```python
import math
import random


def mean_velocity(v_g: float, v_s: float, f_cat: float, f_res: float) -> float:
    """Long-run drift of a microtubule end in the two-state model."""
    return (v_g * f_res - v_s * f_cat) / (f_cat + f_res)


def simulate_end(v_g, v_s, f_cat, f_res, t_end, rng) -> float:
    """Exact simulation of the two-state model; returns the displacement of the end.
    No boundary at zero length: this checks the drift, not length distributions."""
    t, x, growing = 0.0, 0.0, True
    while t < t_end:
        dwell = min(rng.expovariate(f_cat if growing else f_res), t_end - t)
        x += (v_g if growing else -v_s) * dwell
        t += dwell
        growing = not growing
    return x


def transport_times(x_um: float, D: float, v: float) -> tuple[float, float]:
    """Seconds to cover x by 1D diffusion (x^2 / 2D) and by a motor moving at speed v."""
    return x_um ** 2 / (2 * D), x_um / v


rng = random.Random(1)
v_g, v_s = 1.0, 15.0                      # illustrative speeds, um/min
for f_cat, f_res in [(0.3, 0.1), (0.02, 0.5)]:   # illustrative rates, per min
    V = mean_velocity(v_g, v_s, f_cat, f_res)
    sim = simulate_end(v_g, v_s, f_cat, f_res, 1e6, rng) / 1e6
    print(f"f_cat={f_cat:<4} f_res={f_res:<3}: V = {V:7.3f} um/min, simulated {sim:7.3f}")

# Growth without rescue: P(a microtubule reaches distance x) = exp(-f_cat * x / v_g)
lengths = [v_g * rng.expovariate(0.3) for _ in range(100_000)]
for x in (2, 5, 10):
    print(f"x = {x:2} um: formula {math.exp(-0.3 * x / v_g):.3f}, "
          f"simulated {sum(L >= x for L in lengths) / len(lengths):.3f}")

D, v = 1.0, 1.0                            # illustrative: D in um^2/s, motor speed in um/s
for x in (1, 10, 1_000, 1_000_000):        # 1 um, 10 um, 1 mm, 1 m
    t_d, t_m = transport_times(x, D, v)
    print(f"x = {x:>9,} um: diffusion {t_d:9.3g} s, motor {t_m:9.3g} s")
```

```text
f_cat=0.3  f_res=0.1: V = -11.000 um/min, simulated -11.005
f_cat=0.02 f_res=0.5: V =   0.385 um/min, simulated   0.384
x =  2 um: formula 0.549, simulated 0.549
x =  5 um: formula 0.223, simulated 0.222
x = 10 um: formula 0.050, simulated 0.049
x =         1 um: diffusion       0.5 s, motor         1 s
x =        10 um: diffusion        50 s, motor        10 s
x =     1,000 um: diffusion     5e+05 s, motor     1e+03 s
x = 1,000,000 um: diffusion     5e+11 s, motor     1e+06 s
```

## Worked example

> [!example] Why a long cell cannot rely on diffusion (illustrative values)
> Take a vesicle-sized cargo with $D = 1$ µm² s⁻¹ and a motor speed $v = 1$ µm s⁻¹, round numbers chosen for the arithmetic.
> 1. **Crossover distance.** $x^* = 2D/v = 2$ µm: below it diffusion is faster, above it the motor.
> 2. **Across a 10 µm cell.** Diffusion $10^2/2 = 50$ s; motor 10 s.
> 3. **Along a 1 m axon.** Diffusion $(10^6)^2/2 = 5 \times 10^{11}$ s, about 16,000 years; motor $10^6$ s, about 11.6 days.
> 4. **Conclusion.** Whatever the exact constants, the quadratic law makes diffusion useless beyond a few micrometers, so long cells move material along microtubules with motors ([[Molecular Motor]]).

## Common misconceptions

> [!warning] "The cytoskeleton is a fixed scaffold, like a skeleton"
> Actin filaments and microtubules are continuously assembled and disassembled; treadmilling and dynamic instability let the cell remodel them, for example turning the interphase microtubule array into a spindle at mitosis.[^alberts16][^alberts18]

> [!warning] "Motors walk on all three filaments"
> Intermediate filaments have no polarity, so no motor can tell a direction along them. Motors use actin filaments (myosins) and microtubules (kinesins, dyneins) only.[^alberts16]

> [!warning] "Actin is a muscle protein"
> Muscle is where actin and myosin are most abundant and most ordered, but actin filaments are present in eukaryotic cells generally, where they shape the cortex and drive crawling and cytokinesis.[^alberts16]

> [!warning] "Centrioles are needed to build a spindle"
> Plant cells lack centrosomes and still divide with a spindle.[^os45][^alberts18]

## Exercises

> [!question] Exercise 1 (L1)
> For each process, name the filament and, if there is one, the motor: (a) a vesicle moving from the Golgi apparatus to the plasma membrane; (b) the cleavage furrow of a dividing animal cell; (c) the separation of chromosomes at anaphase; (d) the resistance of skin to stretching; (e) the beating of a cilium; (f) the support of the nuclear envelope.

> [!success]- Solution
> (a) Microtubules, kinesin (toward the plus ends at the periphery). (b) Actin filaments and myosin, the contractile ring. (c) Spindle microtubules, with microtubule motors and depolymerization. (d) Keratin intermediate filaments, no motor. (e) The microtubules of the 9 + 2 axoneme, bent by dynein. (f) Lamins, intermediate filaments, no motor.

> [!question] Exercise 2 (L1)
> Predict the effect on a dividing animal cell of colchicine, taxol and cytochalasin.

> [!success]- Solution
> Colchicine blocks tubulin polymerization: no spindle forms and the cell stays arrested in mitosis. Taxol stabilizes microtubules: the spindle cannot remodel, and the cell also arrests in mitosis. Cytochalasin blocks actin filament growth: chromosomes can still be separated, but the contractile ring fails, so the cell can end up with two nuclei.[^alberts16]

> [!question] Exercise 3 (L2)
> Invented rate constants: plus end $k_{\mathrm{on}} = 10$ µM⁻¹ s⁻¹, $k_{\mathrm{off}} = 1$ s⁻¹; minus end $k_{\mathrm{on}} = 1$ µM⁻¹ s⁻¹, $k_{\mathrm{off}} = 0.6$ s⁻¹. (a) Compute both critical concentrations. (b) At $c = 0.3$ µM, does each end grow or shrink? (c) Find the steady-state concentration and the treadmilling flux.

> [!success]- Solution
> (a) $c_c^{+} = 1/10 = 0.1$ µM and $c_c^{-} = 0.6/1 = 0.6$ µM. (b) Plus end $10 \times 0.3 - 1 = +2$ subunits/s, it grows; minus end $0.3 - 0.6 = -0.3$ subunits/s, it shrinks; the filament gains 1.7 subunits/s. (c) $c_{ss} = (1 + 0.6)/(10 + 1) \approx 0.145$ µM, between the two critical concentrations. There the plus end adds $10 \times 0.145 - 1 \approx 0.455$ subunits/s and the minus end loses the same: the length is constant while subunits flow from the plus end to the minus end.

> [!question] Exercise 4 (L2)
> With $v_g = 1$ µm/min and $v_s = 15$ µm/min (illustrative), compute the fraction of time growing and the mean velocity for (a) $f_c = 0.3$, $f_r = 0.1$ per min and (b) $f_c = 0.02$, $f_r = 0.5$ per min. Which regime keeps lengths bounded? Which rescue rate gives $V = 0$ when $f_c = 0.02$ per min?

> [!success]- Solution
> (a) $p_g = 0.1/0.4 = 0.25$ and $V = (0.1 - 4.5)/0.4 = -11$ µm/min: bounded, microtubules stay short. (b) $p_g = 0.5/0.52 \approx 0.96$ and $V = (0.5 - 0.3)/0.52 \approx 0.385$ µm/min: unbounded growth. $V = 0$ when $v_g f_r = v_s f_c$, i.e. $f_r = 15 \times 0.02 = 0.3$ per min. The simulation in the Computational representation reproduces both drifts.

> [!question] Exercise 5 (L3, Python)
> Search and capture, with invented numbers: microtubules grow at $v_g = 1$ µm/min and undergo catastrophe at $f_c = 0.3$ per min, without rescue; only 1 in 100 nucleated microtubules points toward a given kinetochore 5 µm away. (a) How many nucleations are needed on average before one reaches it? (b) What if the catastrophe rate is halved near the chromosomes? Check by simulation.

> [!success]- Solution
> ```python
> import math
> import random
>
> def attempts_needed(f_cat: float, v_g: float, x: float, aim: float, rng: random.Random) -> int:
>     """Nucleations until one microtubule points at the target (probability aim) and reaches it."""
>     n = 0
>     while True:
>         n += 1
>         if rng.random() < aim and v_g * rng.expovariate(f_cat) >= x:
>             return n
>
> rng = random.Random(7)
> for f_cat in (0.3, 0.15):
>     p = 0.01 * math.exp(-f_cat * 5 / 1.0)
>     sim = sum(attempts_needed(f_cat, 1.0, 5, 0.01, rng) for _ in range(2000)) / 2000
>     print(f"f_cat = {f_cat}: p = {p:.5f}, expected attempts {1 / p:.0f}, simulated {sim:.0f}")
> ```
> ```text
> f_cat = 0.3: p = 0.00223, expected attempts 448, simulated 449
> f_cat = 0.15: p = 0.00472, expected attempts 212, simulated 204
> ```
> Each nucleation succeeds with probability $p = 0.01\,e^{-f_c x / v_g}$, so the number of attempts is geometric with mean $1/p$ ([[Geometric Distribution]]). Halving $f_c$ divides the search by $e^{0.75} \approx 2.1$, more than 2, because the success probability depends exponentially on the catastrophe rate.

> [!question] Exercise 6 (L3, Python)
> Invented mean expression of five intermediate filament genes in three clusters of a single-cell dataset is given below. Assign each cluster to the family with the highest mean expression, first using all families, then excluding lamins. Explain the difference.

> [!success]- Solution
> ```python
> expression = {  # invented mean expression per cluster (arbitrary units)
>     "cluster_1": {"KRT8": 120, "KRT18": 95, "VIM": 4, "NEFL": 0, "LMNA": 60},
>     "cluster_2": {"KRT8": 2, "KRT18": 1, "VIM": 150, "NEFL": 1, "LMNA": 75},
>     "cluster_3": {"KRT8": 0, "KRT18": 3, "VIM": 10, "NEFL": 88, "LMNA": 95},
> }
> FAMILIES = {"keratins: epithelial": ["KRT8", "KRT18"], "vimentin: mesenchymal": ["VIM"],
>             "neurofilaments: neuron": ["NEFL"], "lamins: any nucleus": ["LMNA"]}
>
> def assign(cluster: dict[str, float], families: dict[str, list[str]]) -> str:
>     """Family with the highest mean expression of its genes."""
>     return max(families, key=lambda f: sum(cluster[g] for g in families[f]) / len(families[f]))
>
> specific = {f: g for f, g in FAMILIES.items() if not f.startswith("lamins")}
> for name, cluster in expression.items():
>     print(name, "| all families:", assign(cluster, FAMILIES), "| specific only:", assign(cluster, specific))
> ```
> ```text
> cluster_1 | all families: keratins: epithelial | specific only: keratins: epithelial
> cluster_2 | all families: vimentin: mesenchymal | specific only: vimentin: mesenchymal
> cluster_3 | all families: lamins: any nucleus | specific only: neurofilaments: neuron
> ```
> With lamins included, cluster 3 is labeled by a family present in the nucleus of all animal cells,[^alberts16] which says nothing about cell type. A marker must be both expressed and specific; real annotation combines many genes per type and checks them against references ([[Cell Type Annotation]]).

## Mastery checklist

- [ ] 1 Recognized: I can name the three filament types, their subunits and one role of each.
- [ ] 2 Understood: I can explain polarity, critical concentration, treadmilling, dynamic instability and why intermediate filaments have no motors.
- [ ] 3 Practiced: I can compute critical concentrations and the drift of dynamic instability, and simulate the two-state model.
- [ ] 4 Applied: I used cytoskeletal genes as markers on a real single-cell dataset, or compared the GO cellular component annotations of a kinesin and a myosin.
- [ ] 5 Explained: I can teach how filament dynamics, motors and drugs connect cell shape, transport and division, and where the simple kinetic models stop being accurate.

## References

[^os45]: [[Biology 2e (OpenStax)]], section 4.5 "The Cytoskeleton" (microfilaments, intermediate filaments and microtubules with their diameters and roles; centrosome and centrioles; cilia and flagella).
[^alberts16]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 16 "The Cytoskeleton" (filament structure and polarity, nucleotide hydrolysis, critical concentration, treadmilling, dynamic instability, nucleation by the centrosome and the ARP complex, motor proteins, intermediate filament families and keratin disease, mechanical properties, drugs acting on filaments).
[^alberts18]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), ch. 18 "The Mechanics of Cell Division" (spindle assembly and kinetochore capture, centrosome duplication, the contractile ring, spindles without centrosomes in plants).
[^cooper]: [[The Cell (Cooper)]], 2nd ed. (2000), treatment of the cytoskeleton and cell movement.
[^go]: [[Gene Ontology]], cellular component aspect (where a gene product acts).
[^phillips]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 10 "Beam Theory: Architecture for Cells and Skeletons".
