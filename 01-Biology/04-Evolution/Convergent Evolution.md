---
aliases:
  - Convergence
  - Homoplasy
  - Analogy
  - Analogous Structure
  - Parallel Evolution
  - Évolution convergente
  - Homoplasie
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Common Descent]]"
  - "[[Natural Selection]]"
  - "[[Adaptation]]"
related:
  - "[[Sequence Homology]]"
  - "[[Phylogenetic Tree]]"
  - "[[Maximum Parsimony]]"
  - "[[Evolutionary Distance]]"
  - "[[Protein Structure]]"
  - "[[Structural Alignment]]"
  - "[[Enzyme Catalysis]]"
  - "[[Horizontal Gene Transfer]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Evolution (Futuyma)]]"
  - "[[Biochemistry (Berg)]]"
---

# Convergent Evolution

> [!abstract]
> Two features can look alike because they were inherited from a common ancestor (homology) or because they evolved separately in response to similar demands (homoplasy); convergent evolution is the second case.

## Definition

**Convergent evolution** is the independent evolution of similar features in lineages whose common ancestor did not have them. Similarity produced this way is **homoplasy**, and such features are called **analogous**; similarity inherited from a common ancestor is **homology**.[^os20][^futuyma] For sequences, the distinction between homology and measured similarity is developed in [[Sequence Homology]].

## Why it matters

- **Similarity is not homology.** Function annotation by similarity assumes homology; analogous proteins with the same function but no common ancestry break that assumption ([[Sequence Homology]]).
- **Same chemistry, unrelated proteins.** Enzymes with the same catalytic mechanism can have unrelated structures, so a search by function or active-site motif can return non-homologous proteins ([[Enzyme Catalysis]], [[Structural Alignment]]).
- **Trees.** Homoplastic characters conflict with the true tree and can mislead reconstruction; at the sequence level they are multiple substitutions that distance corrections and models must account for ([[Evolutionary Distance]], [[Maximum Parsimony]], [[08-phylogenetic-engine]]).
- **Evidence of selection.** Similar features evolving repeatedly in similar environments are among the best evidence that a feature is an [[Adaptation]].

## Core (L1)

| | Homology | Homoplasy (analogy) |
|---|---|---|
| Cause | inheritance from a common ancestor | independent origin |
| Pattern on a tree | gained once, shared by a clade | gained several times, in separate branches |
| Typical detail | same parts and connections, functions may differ | similar function, construction may differ |
| Example | the forelimb bones of bats and birds | the wings of bats and birds, as wings |

**Same organ, two answers.** Bird and bat wings are homologous as forelimbs: both modify the forelimb bones of a four-limbed ancestor. As wings they are analogous: their common ancestor did not fly, and flight evolved separately, with feathers on the bird's arm and a skin membrane between the bat's elongated fingers.[^os20] Homology is always "homologous as what".

![[homology-vs-homoplasy-tree.svg]]

**Molecular convergence.** Chymotrypsin, a digestive protease of mammals, and subtilisin, a bacterial protease, both cut proteins with the same catalytic triad of serine, histidine and aspartate, yet their three-dimensional structures are unrelated: the same chemical solution evolved twice.[^berg]

## Deeper (L2)

**Kinds of homoplasy.**[^futuyma]

| Kind | Starting states | Example in a DNA site |
|---|---|---|
| Convergence | different ancestral states reach the same state | A in one lineage and C in another both become G |
| Parallelism | the same ancestral state changes the same way independently | A becomes G in two lineages separately |
| Reversal | a derived state returns to the ancestral one | A becomes G, then G becomes A again |

**Why sequences are full of homoplasy.** A nucleotide site has only four states. If two lineages each substitute the same site once, starting from the same base, and each new base is one of the three others with equal probability, they end with the same base with probability $1/3$. As divergence grows, more identical sites are identical by chance rather than by descent, and identity between unrelated sequences tends toward $1/4$ (code below). This is the "multiple hits" problem that [[Evolutionary Distance]] corrections address.

**Telling homology from homoplasy.**

1. **Detail.** Homologous structures share position, connections and development; analogous ones often differ in construction (feathers vs skin membrane).[^os20]
2. **Tree.** Map the feature on a tree built from other, independent characters: one origin supports homology, several origins in separate branches show homoplasy.
3. **Sequence.** Significant similarity over whole genes indicates homology; a few residues in the same geometry, without sequence similarity and with different folds, indicate convergence ([[Protein Structure]]).

## Advanced (L3)

**Convergence has a baseline.** Identical substitutions arise by chance in independent lineages at a rate set by the substitution process, so a claim of adaptive molecular convergence (the same amino-acid changes in unrelated species sharing an environment) must show more convergence than this neutral baseline predicts.

**Convergence versus transfer.** Similar genes in distant organisms may also result from [[Horizontal Gene Transfer]]. The two leave different signatures: transfer gives full-length sequence homology with a gene tree that conflicts with the species tree; convergence gives similar function or structure without detectable common ancestry of the sequences.

**Homoplasy and tree building.** Lineages with long branches accumulate many substitutions and therefore many chance identities; methods that count shared states without modelling multiple hits can group such lineages for the wrong reason, one motivation for model-based methods ([[Maximum Parsimony]], [[Maximum Likelihood Phylogenetics]]).

## Mathematical representation

Let a character take states on the leaves of a rooted tree $T$, with $k$ distinct observed states. Any tree needs at least $k - 1$ state changes to explain them. Let $\ell(T)$ be the minimum number of changes on $T$. The character is **homoplastic on $T$** if $\ell(T) > k - 1$, and the excess $\ell(T) - (k - 1)$ counts the extra, independent origins or reversals.

**Chance identity of two changed sites.** Let both lineages start from base $x$ and each make one substitution, uniformly to one of the three other bases. The pairs of outcomes are $3 \times 3 = 9$ equally likely, of which 3 are identical:

$$P(\text{same derived base}) = \frac{3}{9} = \frac{1}{3}.$$

## Computational representation

The simulation evolves two copies of a random ancestral sequence independently and counts identical sites, separating those that kept the ancestral base from those identical in a derived base (homoplasy). Standard library only; data simulated.

```python
import random
from itertools import product

BASES = "ACGT"

def evolve(seq: str, k: int, rng: random.Random) -> str:
    """Apply k substitutions at uniformly random sites, each to one of the 3 other bases."""
    s = list(seq)
    for _ in range(k):
        i = rng.randrange(len(s))
        s[i] = rng.choice([b for b in BASES if b != s[i]])
    return "".join(s)

rng = random.Random(42)
L = 20_000
ancestor = "".join(rng.choice(BASES) for _ in range(L))
print("subst/site  identical  of which derived (homoplasy)")
for d in (0.1, 0.5, 1.0, 2.0):
    x, y = evolve(ancestor, int(d * L), rng), evolve(ancestor, int(d * L), rng)
    same = sum(a == b for a, b in zip(x, y))
    derived = sum(a == b != c for a, b, c in zip(x, y, ancestor))
    print(f"{d:9.1f}  {same / L:9.3f}  {derived / L:9.3f}")

# Exact check: one substitution on each lineage at the same site
anc = "A"
pairs = [(a, b) for a, b in product(BASES, repeat=2) if a != anc and b != anc]
print(sum(a == b for a, b in pairs), "/", len(pairs))
```

Output:

```text
subst/site  identical  of which derived (homoplasy)
      0.1      0.825      0.003
      0.5      0.446      0.043
      1.0      0.296      0.100
      2.0      0.255      0.163
3 / 9
```

At 2 substitutions per site per lineage, identity has fallen to about 0.25, the value expected between unrelated random sequences, and nearly two thirds of the identical sites (0.163 of 0.255) are identical in a derived base: they look shared but are not inherited. Identity in the ancestral base can itself hide reversals.

## Worked example

> [!example] Counting origins of flight on a tree
> Tree: `((lizard,pigeon),(mouse,bat))`, as in the figure. Character "powered flight": present in pigeon and bat, absent in lizard and mouse; $k = 2$ states.
>
> 1. **Minimum possible**: $k - 1 = 1$ change.
> 2. **On this tree**: pigeon's sister (lizard) and bat's sister (mouse) do not fly, so one gain at the root followed by two losses needs 3 changes, while two separate gains need 2. Hence $\ell(T) = 2$.
> 3. **Excess**: $2 - 1 = 1$: flight is homoplastic on this tree, gained twice.
> 4. **Same test for hair** (mouse, bat): one gain on the branch leading to mouse and bat, $\ell(T) = 1 = k - 1$: no excess, consistent with homology.
> 5. **Reading**: the tree comes from other characters (amnion, hair, molecules); against that background, flight is the character that needs two origins, as the different construction of the two wings confirms.[^os20]

## Common misconceptions

> [!warning] "Similar structures mean shared ancestry"
> Similarity can arise independently under similar demands. Only detailed, nested similarity that fits a tree built from independent data indicates homology.

> [!warning] "An organ is either homologous or analogous"
> It depends on the level of comparison: bird and bat wings are homologous as forelimbs and analogous as wings.[^os20]

> [!warning] "Convergence is rare"
> At the sequence level, with four bases, chance identities are frequent and grow with divergence (code above).

> [!warning] "Proteins with the same function have similar sequences"
> Chymotrypsin and subtilisin share their catalytic mechanism but have unrelated structures.[^berg] Same function does not imply homology.

## Exercises

> [!question] Exercise 1 (L1)
> Homology or homoplasy? (a) The bones of a human arm and of a whale flipper. (b) The wings of a bat and of a pigeon, as organs of flight. (c) The catalytic triads of chymotrypsin and subtilisin. (d) The feathers of a pigeon and of an eagle.

> [!success]- Solution
> (a) Homology: one forelimb plan inherited from a common tetrapod ancestor. (b) Homoplasy: flight evolved separately. (c) Homoplasy: same active-site chemistry in unrelated structures. (d) Homology: feathers were inherited from the common ancestor of birds.

> [!question] Exercise 2 (L2)
> Two proteins share 85 % identity over their full length of 300 residues. Two other proteins share three catalytic residues in the same spatial arrangement, have no significant sequence similarity and have different folds. Classify each pair and justify.

> [!success]- Solution
> The first pair is homologous: full-length identity of 85 % is far beyond chance ([[Sequence Homology]]). The second pair is convergent: a few residues in the same geometry can be reached independently when the chemistry demands it, and different folds give no sign of common ancestry.

> [!question] Exercise 3 (L2)
> On the tree `((A,B),(C,D))`, a binary character is present in A and C only. Compute the minimum number of changes and the excess. Is there another tree on which the character shows no homoplasy?

> [!success]- Solution
> On `((A,B),(C,D))`, two gains (in A and in C) are needed, or one gain plus one loss: $\ell = 2$, excess $2 - 1 = 1$. On `((A,C),(B,D))`, one gain on the branch to A and C suffices: no excess. Choosing between the trees requires other characters; a single homoplastic-looking character cannot decide.

> [!question] Exercise 4 (L3, Python)
> From the simulation output, compute the fraction of identical sites that are identical in a derived base at each divergence, and explain why sequence identity alone underestimates divergence.

> [!success]- Solution
> $0.003/0.825 = 0.4\,\%$, $0.043/0.446 = 9.6\,\%$, $0.100/0.296 = 34\,\%$, $0.163/0.255 = 64\,\%$. As divergence grows, more matches are chance identities, and other sites changed several times or reverted. Counting differences therefore misses hidden changes and saturates near 75 % difference; models of substitution correct for this ([[Evolutionary Distance]]).

> [!question] Exercise 5 (L3)
> A gene in a bacterium and a gene in an archaeon perform the same reaction. Describe what you would expect if the similarity came from convergence, and what you would expect if it came from horizontal gene transfer.

> [!success]- Solution
> Convergence: no significant full-length sequence similarity, possibly different folds, perhaps a similar active site. Transfer: significant full-length similarity (homology), with the archaeal gene nested among bacterial sequences in a gene tree, in conflict with the species tree; sometimes also atypical composition or codon usage in the recipient genome ([[Horizontal Gene Transfer]]).

## Mastery checklist

- [ ] 1 Recognized: I can define homology, homoplasy and analogy, and give an example of each.
- [ ] 2 Understood: I can explain why bird and bat wings are both homologous and analogous, and distinguish convergence, parallelism and reversal.
- [ ] 3 Practiced: I can count the minimum changes of a character on a tree and simulate chance identities between sequences.
- [ ] 4 Applied: I check whether functional similarity between proteins is backed by sequence or structural homology before transferring annotations.
- [ ] 5 Explained: I can teach why homoplasy grows with divergence, how it misleads trees, and how to tell convergence from horizontal transfer.

## References

[^os20]: [[Biology 2e (OpenStax)]], ch. 20 "Phylogenies and the History of Life" (homologous and analogous structures; bird and bat wings).
[^futuyma]: [[Evolution (Futuyma)]], 5th ed. (2023), phylogenetics and homoplasy (chapter numbers not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of catalytic strategies (serine proteases: chymotrypsin and subtilisin).
