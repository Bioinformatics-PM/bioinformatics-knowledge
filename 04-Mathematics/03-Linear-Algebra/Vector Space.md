---
aliases:
  - Linear Space
  - Subspace
  - Linear Subspace
  - Vector Subspace
  - Espace vectoriel
  - Sous-espace vectoriel
tags:
  - type/concept
  - domain/mathematics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Vector]]"
  - "[[Set]]"
  - "[[Function]]"
  - "[[Matrix]]"
  - "[[System of Linear Equations]]"
related:
  - "[[Linear Independence]]"
  - "[[Basis and Dimension]]"
  - "[[Matrix Rank]]"
  - "[[Fundamental Theorem of Linear Algebra]]"
  - "[[Linear Transformation]]"
  - "[[Orthogonal Projection]]"
  - "[[Symmetric Matrix]]"
  - "[[Stoichiometric Matrix]]"
  - "[[Flux Balance Analysis]]"
  - "[[Linear Programming]]"
  - "[[Compositional Data Analysis]]"
  - "[[Microbiome]]"
projects: []
sources:
  - "[[Linear Algebra Done Right (Axler)]]"
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Orth 2010 - What Is Flux Balance Analysis]]"
  - "[[Gloor 2017 - Microbiome Datasets Are Compositional]]"
---

# Vector Space

> [!abstract]
> A vector space is a set whose elements can be added and scaled without leaving the set, following the usual rules of arithmetic; a subspace is a vector space inside another one, like a line or a plane through the origin. Checking these rules tells you whether linear-algebra tools apply to a set of solutions or of data.

## Definition

A **vector space** over $\mathbb{F}$ ($\mathbb{R}$ or $\mathbb{C}$) is a set $V$ with an addition $V \times V \to V$ and a scalar multiplication $\mathbb{F} \times V \to V$ such that, for all $u, v, w \in V$ and $a, b \in \mathbb{F}$:[^axler]

- **commutativity** $u + v = v + u$; **associativity** $(u + v) + w = u + (v + w)$ and $(ab)v = a(bv)$;
- **additive identity**: some $0 \in V$ satisfies $v + 0 = v$; **additive inverse**: each $v$ has a $w$ with $v + w = 0$;
- **multiplicative identity** $1v = v$; **distributivity** $a(u + v) = au + av$ and $(a + b)v = av + bv$.

Its elements are called vectors. A **subspace** of $V$ is a subset $U$ that is itself a vector space with the same operations; equivalently, $0 \in U$ and $U$ is closed under addition and under scalar multiplication.[^axler][^strang][^1806]

## Why it matters

- **Solution sets described by a few directions.** The steady states $\{v : Sv = 0\}$ of a metabolic network, where $S$ is the stoichiometric matrix, form a subspace: the null space of $S$.[^orth] Every steady state is then a combination of a few basic flux routes ([[Stoichiometric Matrix]], [[Basis and Dimension]]).
- **Knowing where linear tools stop.** Add bounds on fluxes (irreversible reactions run forward only, uptake is limited) and the feasible set is no longer a subspace: $-v$ may be infeasible. [[Flux Balance Analysis]] then optimizes over this constrained set with [[Linear Programming]].[^orth]
- **Data that are not ordinary vectors.** Proportions (relative abundances, cell-type fractions, allele frequencies) are not closed under addition or scaling. Sequencing-based microbiome data are compositions, because the instrument fixes an arbitrary total, and should be analyzed as compositions (Frontier, [[Compositional Data Analysis]]).[^gloor]
- **One vocabulary for the rest of the path.** Column space and null space ([[Fundamental Theorem of Linear Algebra]]), [[Matrix Rank]], [[Orthogonal Projection]] and [[Least Squares]] are statements about subspaces.

## Core (L2)

### Which sets qualify

| Set (usual addition and scaling) | Vector space? | What fails |
|---|---|---|
| $\mathbb{R}^n$; matrices $\mathbb{R}^{m \times n}$; polynomials of degree $\le d$; real functions on a set | yes | nothing |
| count vectors (nonnegative integers) | no | $-1 \cdot v$ and $\tfrac12 v$ leave the set |
| proportions ($p_i \ge 0$, $\sum_i p_i = 1$) | no | $0$ is missing; $p + q$ sums to 2 |
| solutions of $Ax = b$ with $b \ne 0$ | no | $0$ is missing |
| polynomials of degree exactly 2 | no | $(x^2 + x) + (-x^2) = x$ |
| unit vectors, $\lVert v \rVert = 1$ | no | $2v$ has norm 2 |

Functions are vectors too: for a set $S$, the functions $f : S \to \mathbb{R}$, added and scaled pointwise, form a vector space $\mathbb{R}^S$.[^axler] A coverage track assigning a number to each position of a chromosome is such a vector, and the sum of two tracks is again a track ([[Vector#Advanced (L3)]]).

### Subspaces

**The test.** $U \subseteq V$ is a subspace if and only if (1) $0 \in U$, (2) $u, w \in U \Rightarrow u + w \in U$, (3) $u \in U, c \in \mathbb{F} \Rightarrow cu \in U$.[^axler] One counterexample disproves; a proof must cover all vectors.

![[vector-space-subspace-tests.svg]]

- **In $\mathbb{R}^3$**, the subspaces are $\{0\}$, the lines through 0, the planes through 0 and $\mathbb{R}^3$ itself.[^strang]
- **Null space.** $N(A) = \{x : Ax = 0\}$ is a subspace: $A0 = 0$; $A(x + y) = Ax + Ay = 0$; $A(cx) = c\,Ax = 0$.
- **Column space.** $C(A) = \{Ax : x \in \mathbb{R}^n\}$ is the set of combinations of the columns of $A$: the right-hand sides $b$ for which $Ax = b$ is solvable ([[System of Linear Equations]]).
- **Span.** $\operatorname{span}(v_1, \dots, v_k)$, the set of all linear combinations ([[Vector#Deeper (L2)]]), is a subspace, and the smallest one containing $v_1, \dots, v_k$.[^axler]
- **Intersections and sums.** An intersection of subspaces is a subspace; a union usually is not (panel d). The sum $U + W = \{u + w : u \in U, w \in W\}$ is the smallest subspace containing both.[^axler]

### Subspace or shifted subspace

If $Ax_p = b$, then $A(x_p + z) = b \iff Az = 0$: the solutions of $Ax = b$ are $x_p + N(A)$, the null space shifted by one particular solution. For $b \ne 0$ this set misses the origin. It is an **affine** set (a line or plane not through 0), not a subspace. In a network, the balanced states $Sv = 0$ form a subspace; fixing one exchange flux to a measured value gives an affine set (Exercise 5).

## Advanced (L3)

- **Cones are not subspaces.** $\{v : Sv = 0,\ v \ge 0\}$ (every reaction irreversible) contains 0 and is closed under addition and under multiplication by $c \ge 0$, but not by $c < 0$: a convex cone, with the same structure as count vectors (panel c). Linear algebra describes the steady-state subspace; the cone and the bounded set of flux balance analysis need [[Linear Programming]].[^orth]
- **Complex scalars.** Over $\mathbb{C}$ the scalars are [[Complex Number|complex numbers]]. A real matrix may have no real eigenvector (a rotation of the plane by 90° moves every nonzero vector off its line), yet always has eigenvectors in $\mathbb{C}^n$; this is why eigenvalue theory works over $\mathbb{C}$ ([[Eigenvalues and Eigenvectors]]).[^axler]
- **Infinite dimension.** The space of all polynomials, or of all real functions on an interval, has no finite spanning list.[^axler] Curve fitting chooses a finite-dimensional subspace (polynomials of degree $\le d$, splines with fixed knots, [[Spline]]) and finds its element closest to the data ([[Least Squares]]). Probability densities, like proportions, do not form a subspace: they must integrate to 1.
- **Direct sums.** $V = U \oplus W$ when every $v$ is $u + w$ in exactly one way; for two subspaces this holds if and only if $U + W = V$ and $U \cap W = \{0\}$.[^axler] Examples: $\mathbb{R}^{n \times n} = \mathrm{Sym}_n \oplus \mathrm{Skew}_n$ ([[Symmetric Matrix]]); later, the row space and the null space of $A$ split $\mathbb{R}^n$ ([[Fundamental Theorem of Linear Algebra]]).

## Frontier (M1)

**Compositions as a vector space.** A composition of $D$ parts lives in the simplex $\mathcal{S}^D = \{x \in \mathbb{R}^D : x_i > 0, \sum_i x_i = 1\}$, which is not a subspace of $\mathbb{R}^D$. With the closure $\mathcal{C}(y) = y / \sum_i y_i$, define new operations, **perturbation** and **powering**:
$$x \oplus y = \mathcal{C}(x_1 y_1, \dots, x_D y_D), \qquad \alpha \odot x = \mathcal{C}(x_1^\alpha, \dots, x_D^\alpha).$$
With them, $\mathcal{S}^D$ satisfies every axiom; its zero is $(\tfrac1D, \dots, \tfrac1D)$ and the opposite of $x$ is $\mathcal{C}(1/x_1, \dots, 1/x_D)$ (Exercise 6). The **centered log-ratio** $\operatorname{clr}(x)_i = \log\big(x_i / g(x)\big)$, with $g(x)$ the geometric mean of the parts, turns $\oplus$ into $+$ and $\odot$ into ordinary scaling, and maps $\mathcal{S}^D$ onto the subspace $\{z \in \mathbb{R}^D : \sum_i z_i = 0\}$, the null space of $\mathbf{1}^\top$, of dimension $D - 1$. A multiplicative change of a microbiome profile becomes a vector addition, and ordinary linear tools apply to the clr coordinates. This geometry underlies the log-ratio methods of [[Compositional Data Analysis]], which sequencing-based microbiome data call for.[^gloor]

## Mathematical representation

- $(V, +, \cdot)$ over $\mathbb{F}$ with the axioms of the Definition. Subspace criterion: $U \subseteq V$ is a subspace $\iff 0 \in U$ and $au + bw \in U$ for all $u, w \in U$, $a, b \in \mathbb{F}$.
- $\operatorname{span}(v_1, \dots, v_k) = \{\sum_{j=1}^{k} c_j v_j : c_j \in \mathbb{F}\}$; $U + W = \{u + w : u \in U, w \in W\}$.
- For $A \in \mathbb{R}^{m \times n}$: $N(A) = \{x \in \mathbb{R}^n : Ax = 0\}$ and $C(A) = \{Ax : x \in \mathbb{R}^n\} \subseteq \mathbb{R}^m$ are subspaces; $\{x : Ax = b\} = x_p + N(A)$ when $Ax_p = b$.
- Simplex: $x \oplus y$, $\alpha \odot x$ as above; $\operatorname{clr}(x) = \log x - \frac1D \big(\sum_i \log x_i\big)\mathbf{1}$, with $\operatorname{clr}(x \oplus y) = \operatorname{clr}(x) + \operatorname{clr}(y)$ and $\operatorname{clr}(\alpha \odot x) = \alpha \operatorname{clr}(x)$.

## Computational representation

Membership tests turn the axioms into code. A failed check disproves the subspace property; passing it on examples proves nothing.

```python
from fractions import Fraction as F

S = [[1, -1, 0, -1],     # toy network of the System of Linear Equations note:
     [0, 1, -1, 0]]      # metabolites x reactions

def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]

def add(u, v):
    return [a + b for a, b in zip(u, v)]

def scale(c, v):
    return [c * a for a in v]

def subspace_checks(member, u, v):
    """Test 0, u + v and (-1) * u for two members u, v. One failure disproves; passing proves nothing."""
    zero = [0] * len(u)
    return member(zero), member(add(u, v)), member(scale(-1, u))

candidates = {   # name: (membership test, two members of the set)
    "steady states, Sv = 0": (lambda v: matvec(S, v) == [0, 0],
                              [1, 1, 1, 0], [1, 0, 0, 1]),
    "irreversible steady states, Sv = 0 and v >= 0": (
        lambda v: matvec(S, v) == [0, 0] and min(v) >= 0, [1, 1, 1, 0], [1, 0, 0, 1]),
    "proportions, p >= 0 and sum 1": (lambda p: min(p) >= 0 and sum(p) == 1,
                                      [F(1, 2), F(1, 4), F(1, 4), 0], [F(1, 4)] * 4),
    "sum-zero vectors": (lambda z: sum(z) == 0, [1, -1, 0, 0], [2, 0, -1, -1]),
}
for name, (member, u, v) in candidates.items():
    print(name, subspace_checks(member, u, v))

import numpy as np
from scipy.linalg import null_space

N = null_space(np.array(S, dtype=float))   # orthonormal basis of {v : Sv = 0}
print(N.shape, np.allclose(np.array(S) @ N, 0))

def clr(p):
    """Centered log-ratio: log of each part over the geometric mean."""
    logp = np.log(p)
    return logp - logp.mean()

p = np.array([0.5, 0.3, 0.15, 0.05])       # invented relative abundances of 4 taxa
z = clr(p)
print(z.round(3), abs(z.sum()) < 1e-12)
```

```text
steady states, Sv = 0 (True, True, True)
irreversible steady states, Sv = 0 and v >= 0 (True, True, False)
proportions, p >= 0 and sum 1 (False, False, False)
sum-zero vectors (True, True, True)
(4, 2) True
[ 1.004  0.494 -0.2   -1.298] True
```

Fractions keep `sum(p) == 1` exact. `null_space` returns 2 orthonormal columns spanning the steady states: a 2-dimensional subspace of $\mathbb{R}^4$ ([[Basis and Dimension]]). The clr vector of a composition sums to 0, as the Frontier section predicts.

## Worked example

> [!example] Four sets from a toy network and a microbiome
> The toy network of [[System of Linear Equations]] has metabolites $A$, $B$ and reactions $v_1$ (uptake of $A$), $v_2$ ($A \to B$), $v_3$ (secretion of $B$), $v_4$ (secretion of $A$), so $S = \begin{pmatrix} 1 & -1 & 0 & -1 \\ 0 & 1 & -1 & 0 \end{pmatrix}$. [[Gaussian Elimination]] (Exercise 3) found the two routes $r_1 = (1, 1, 1, 0)$ and $r_2 = (1, 0, 0, 1)$.
> 1. **Steady states** $\{v : Sv = 0\}$: a null space, hence a subspace. For instance $r_1 + r_2 = (2, 1, 1, 1)$ gives $S(r_1 + r_2) = (2 - 1 - 1,\ 1 - 1) = (0, 0)$, and $-r_1$ is balanced too.
> 2. **Irreversible steady states** $\{v : Sv = 0, v \ge 0\}$: contains 0 and $r_1 + r_2$, but $-r_1 = (-1, -1, -1, 0)$ runs every reaction backwards. Not a subspace: a cone.
> 3. **Proportions of 4 taxa**: $p = (\tfrac12, \tfrac14, \tfrac14, 0)$ and $q = (\tfrac14, \tfrac14, \tfrac14, \tfrac14)$ give $p + q$ with sum 2, and $(0, 0, 0, 0)$ is not a composition. Not a subspace.
> 4. **Sum-zero vectors** $\{z : z_1 + z_2 + z_3 + z_4 = 0\}$: the null space of $(1, 1, 1, 1)$, hence a subspace; the clr coordinates of 4-part compositions live there.
>
> The code above runs the same three checks on each set and reproduces these verdicts.

## Common misconceptions

> [!warning] "Every line or plane is a subspace"
> Only those through the origin. The solutions of $Ax = b$ with $b \ne 0$ form a shifted copy of $N(A)$, which does not contain 0; sums of two solutions solve $Ax = 2b$, not $Ax = b$.

> [!warning] "The union of two subspaces is a subspace"
> The union of the two axes of the plane contains $(1, 0)$ and $(0, 1)$ but not their sum (panel d). The smallest subspace containing both is their sum $U + W$, here the whole plane.

> [!warning] "Closure under addition is enough"
> Count vectors and the flux cone are closed under addition but not under multiplication by negative numbers; both conditions (and $0 \in U$) are needed.

> [!warning] "Proportions can be averaged, subtracted and ordinated like any vectors"
> The arithmetic runs, but it leaves the set and ignores the constraint that the parts sum to 1; on compositional data such analyses can mislead.[^gloor] Move to log-ratio coordinates first (Frontier, [[Compositional Data Analysis]]).

## Exercises

> [!question] Exercise 1 (L2)
> Which subsets of $\mathbb{R}^3$ are subspaces? (a) $x_1 + 2x_2 - x_3 = 0$; (b) $x_1 + 2x_2 - x_3 = 1$; (c) $x_1 x_2 = 0$; (d) $x_1 = x_2 = x_3$; (e) $x_1, x_2, x_3 \ge 0$.

> [!success]- Solution
> (a) Yes: the null space of the $1 \times 3$ matrix $(1, 2, -1)$, a plane through 0. (b) No: $0$ fails the equation. (c) No: $(1, 0, 0)$ and $(0, 1, 0)$ belong, their sum $(1, 1, 0)$ does not (it is the union of two planes). (d) Yes: the line spanned by $(1, 1, 1)$. (e) No: $-1 \cdot (1, 1, 1)$ leaves the set.

> [!question] Exercise 2 (L2)
> Show that the polynomials of degree at most 2 form a subspace of the real functions, but the polynomials of degree exactly 2 do not. Answer the same question for the symmetric $2 \times 2$ matrices and for the invertible $2 \times 2$ matrices.

> [!success]- Solution
> Degree $\le 2$: the zero polynomial belongs, and sums and multiples of polynomials of degree $\le 2$ have degree $\le 2$. Degree exactly 2: no zero polynomial, and $(x^2 + x) + (-x^2) = x$. Symmetric matrices: $0$ is symmetric, $(A + B)^\top = A + B$ and $(cA)^\top = cA$: a subspace. Invertible matrices: $0$ is not invertible, and $I + (-I) = 0$: not a subspace.

> [!question] Exercise 3 (L2, Python)
> Is $(1, 2, 3)$ in $\operatorname{span}\{(1, 0, 1), (0, 1, 1)\}$? Is $(1, 2, 4)$? Describe the span geometrically.

> [!success]- Solution
> $c_1(1, 0, 1) + c_2(0, 1, 1) = (c_1, c_2, c_1 + c_2)$: the span is the plane $x_3 = x_1 + x_2$. $(1, 2, 3)$ lies on it ($c = (1, 2)$); $(1, 2, 4)$ does not ($3 \ne 4$). A least-squares solve confirms it: an exact fit exists only for the first vector.
> ```python
> import numpy as np
> A = np.array([[1, 0], [0, 1], [1, 1]], dtype=float)   # columns (1,0,1) and (0,1,1)
> for b in ([1, 2, 3], [1, 2, 4]):
>     c, *_ = np.linalg.lstsq(A, np.array(b, dtype=float), rcond=None)
>     print(b, c.round(3), np.allclose(A @ c, b))
> # [1, 2, 3] [1. 2.] True
> # [1, 2, 4] [1.333 2.333] False
> ```

> [!question] Exercise 4 (L3)
> Prove that the union of two subspaces $U$ and $W$ is a subspace only if one contains the other.

> [!success]- Solution
> Suppose neither contains the other: pick $u \in U \setminus W$ and $w \in W \setminus U$. If $u + w \in U$, then $w = (u + w) - u \in U$, a contradiction; if $u + w \in W$, then $u = (u + w) - w \in W$, a contradiction. So $u + w \notin U \cup W$ and the union is not closed under addition. Conversely, if $U \subseteq W$, the union is $W$, a subspace.

> [!question] Exercise 5 (L3)
> In the toy network, the uptake flux is measured: $v_1 = 10$. Describe the set $\{v : Sv = 0, v_1 = 10\}$. Is it a subspace? What does it become if all fluxes must be nonnegative?

> [!success]- Solution
> Steady states are $v = a r_1 + b r_2 = (a + b, a, a, b)$, so $v_1 = 10$ means $b = 10 - a$: $v = 10\,r_2 + a\,(r_1 - r_2) = (10, a, a, 10 - a)$, $a \in \mathbb{R}$. It is a line through $10\,r_2 = (10, 0, 0, 10)$ with direction $(0, 1, 1, -1)$, not through 0: affine, not a subspace. With $v \ge 0$, $0 \le a \le 10$: a segment, the bounded feasible set on which flux balance analysis would maximize an objective, here the choice between secreting $B$ and secreting $A$ ([[Flux Balance Analysis]]).

> [!question] Exercise 6 (M1, Python)
> For the compositions $p = (0.5, 0.3, 0.15, 0.05)$ and $q = (0.1, 0.2, 0.3, 0.4)$ (invented), check numerically that $\operatorname{clr}(p \oplus q) = \operatorname{clr}(p) + \operatorname{clr}(q)$, $\operatorname{clr}(-2 \odot p) = -2\operatorname{clr}(p)$, that the uniform composition is the zero of $\oplus$, and that $\mathcal{C}(1/p)$ is the opposite of $p$. Then explain why the closure constant never matters.

> [!success]- Solution
> ```python
> def closure(x):
>     return x / x.sum()
>
> def perturb(p, q):            # p (+) q
>     return closure(p * q)
>
> def power(a, p):              # a (.) p
>     return closure(p ** a)
>
> p = np.array([0.5, 0.3, 0.15, 0.05])     # invented compositions
> q = np.array([0.1, 0.2, 0.3, 0.4])
> e = np.full(4, 0.25)                     # candidate zero element
> print(np.allclose(clr(perturb(p, q)), clr(p) + clr(q)),
>       np.allclose(clr(power(-2.0, p)), -2.0 * clr(p)),
>       np.allclose(perturb(p, e), p),
>       np.allclose(perturb(p, closure(1 / p)), e))
> # True True True True
> ```
> Multiplying a composition by a constant $k$ adds $\log k$ to every log-part and to their mean, which cancel in $\operatorname{clr}$: $\operatorname{clr}(ky) = \operatorname{clr}(y)$. So $\operatorname{clr}(\mathcal{C}(x_i y_i)) = \operatorname{clr}(x) + \operatorname{clr}(y)$ and $\operatorname{clr}(\mathcal{C}(x_i^\alpha)) = \alpha \operatorname{clr}(x)$ follow from $\log(x_i y_i) = \log x_i + \log y_i$ and $\log x_i^\alpha = \alpha \log x_i$. Because clr is a bijection onto the sum-zero subspace that turns the new operations into the usual ones, every vector-space axiom transfers from that subspace to $(\mathcal{S}^D, \oplus, \odot)$.

## Mastery checklist

- [ ] 1 Recognized: I can state what a vector space and a subspace are and give examples beyond $\mathbb{R}^n$ (matrices, polynomials, functions).
- [ ] 2 Understood: I can apply the three-condition subspace test, find a counterexample when it fails, and explain why null spaces are subspaces and solution sets of $Ax = b$ with $b \ne 0$ are not.
- [ ] 3 Practiced: I can prove the subspace property for null spaces, spans, sums and intersections, and check membership conditions in code.
- [ ] 4 Applied: I described the steady states of a real metabolic network as a null space and saw how flux bounds turn it into a cone or polytope; I transformed real relative-abundance data to clr coordinates.
- [ ] 5 Explained: I can explain which data are not vectors under ordinary operations (counts, proportions, densities), why that matters for analysis, and how the simplex becomes a vector space under perturbation and powering.

## References

[^axler]: [[Linear Algebra Done Right (Axler)]], 4th ed. (2024), treatment of vector spaces and subspaces (sums, direct sums, finite-dimensional spaces).
[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces" (vector spaces and subspaces).
[^orth]: [[Orth 2010 - What Is Flux Balance Analysis]], *Nature Biotechnology*.
[^gloor]: [[Gloor 2017 - Microbiome Datasets Are Compositional]], *Frontiers in Microbiology* 8:2224.
