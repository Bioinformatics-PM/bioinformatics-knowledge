---
aliases:
  - Matrix Product
  - Matrix-Vector Product
  - Matrix Power
  - Block Multiplication
  - Produit matriciel
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Matrix]]"
  - "[[Dot Product]]"
  - "[[Vector]]"
related:
  - "[[Markov Chain]]"
  - "[[Transition Matrix]]"
  - "[[Substitution Matrix]]"
  - "[[Inverse Matrix]]"
  - "[[Linear Transformation]]"
  - "[[Matrix Exponential]]"
  - "[[Diagonalization]]"
  - "[[Big O Notation]]"
  - "[[Dynamic Programming]]"
  - "[[Wright-Fisher Model]]"
projects:
  - "[[07-evolution-simulator]]"
sources:
  - "[[Introduction to Linear Algebra (Strang)]]"
  - "[[MIT 18.06SC - Linear Algebra]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Dayhoff 1978 - A Model of Evolutionary Change in Proteins]]"
  - "[[Introduction to Algorithms (Cormen)]]"
---

# Matrix Multiplication

> [!abstract]
> Multiplying two matrices chains two linear maps into one: each entry of $AB$ is a row of $A$ dotted with a column of $B$. The order matters ($AB \ne BA$), the grouping does not ($(AB)C = A(BC)$), and powers of a transition matrix move a Markov chain, or a protein, forward in time.

## Definition

If $A$ is $m \times n$ and $B$ is $n \times p$, their **product** $AB$ is the $m \times p$ matrix with entries
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj},$$
the [[Dot Product]] of row $i$ of $A$ with column $j$ of $B$. It is defined only when the number of columns of $A$ equals the number of rows of $B$.[^strang][^1806] The product represents composition: $(AB)x = A(Bx)$, first apply $B$, then $A$.[^strang]

## Why it matters

- **One step of a Markov chain.** Write the probabilities of the states at time $t$ as a row vector $p_t$ and the transition probabilities $p_{ij} = P(\text{state } j \text{ at } t+1 \mid \text{state } i \text{ at } t)$ as a matrix $P$.[^durbin3] Summing over the current state gives $p_{t+1} = p_t P$, hence $p_t = p_0 P^t$ (Deeper).
- **PAM matrices.** Dayhoff's PAM1 gives amino acid replacement probabilities for an evolutionary distance of 1 accepted point mutation per 100 residues, assuming each change is independent of earlier ones; longer distances are obtained by multiplying PAM1 by itself, so PAM250 comes from the 250th power of PAM1. PAM250 was the matrix for distantly related proteins.[^dayhoff] See [[Substitution Matrix]].
- **Population genetics.** In the [[Wright-Fisher Model]], the distribution of the allele count after $t$ generations is $p_0 P^t$ for the model's transition matrix ([[07-evolution-simulator]]).
- **Statistics and data analysis.** $X^\top X$ and $X^\top y$ of regression ([[Inverse Matrix]]), covariance matrices for [[Principal Component Analysis]], and projections of data onto components are all matrix products.

## Core (L1)

### Four ways to see one product

Strang presents the same product four ways;[^strang] each is useful in a different situation. Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$:

| View | Rule | On the example, $AB = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}$ |
|---|---|---|
| Entries | $(AB)_{ij}$ = row $i$ of $A$ · column $j$ of $B$ | $(AB)_{11} = (1, 2) \cdot (0, 1) = 2$ |
| Columns | column $j$ of $AB$ = $A$ × (column $j$ of $B$), a combination of the columns of $A$ | column 1 = $0 \cdot (1, 3) + 1 \cdot (2, 4) = (2, 4)$ |
| Rows | row $i$ of $AB$ = (row $i$ of $A$) × $B$, a combination of the rows of $B$ | row 1 = $1 \cdot (0, 1) + 2 \cdot (1, 0) = (2, 1)$ |
| Outer products | $AB = \sum_k (\text{column } k \text{ of } A)(\text{row } k \text{ of } B)$ | $\begin{pmatrix} 1 \\ 3 \end{pmatrix}(0 \; 1) + \begin{pmatrix} 2 \\ 4 \end{pmatrix}(1 \; 0)$ |

The column view applied to one vector is the matrix-vector product of [[Matrix]]:

![[matrix-vector-column-combination.svg]]

### Rules

- **Shapes**: $(m \times n)(n \times p) = (m \times p)$. Check the inner dimensions before computing anything.
- **Associative**: $(AB)C = A(BC)$, so $ABC$ needs no parentheses. **Distributive**: $A(B + C) = AB + AC$.[^strang]
- **Identity**: $IA = AI = A$.
- **Transpose of a product**: $(AB)^\top = B^\top A^\top$, order reversed (Exercise 3).[^strang]
- **Not commutative**: in general $AB \ne BA$. Above, $BA = \begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}$: multiplying by $B$ on the right swapped the columns of $A$, on the left it swapped the rows.[^strang] Even the shapes may differ: for $A$ of size $2 \times 3$ and $B$ of size $3 \times 2$, $AB$ is $2 \times 2$ and $BA$ is $3 \times 3$.

### Blocks

Cut $A$ and $B$ into blocks whose sizes are compatible; then blocks multiply like numbers, as long as their order is kept:[^strang]
$$\begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix} \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix} = \begin{pmatrix} A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22} \\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22} \end{pmatrix}.$$

## Deeper (L2)

**Markov chains in matrix form.** By the law of total probability, $P(X_{t+1} = j) = \sum_i P(X_t = i)\,p_{ij}$: the row vector $p_{t+1}$ is $p_t P$. Associativity gives $p_t = (\cdots((p_0 P) P) \cdots) P = p_0 P^t$, and $P^{s+t} = P^s P^t$: the probability of going from $i$ to $j$ in $s + t$ steps sums over the state reached after $s$ steps (the Chapman-Kolmogorov equation, [[Transition Matrix]]). Each row of $P^t$ is a probability distribution: if $P\mathbf{1} = \mathbf{1}$ then $P^t\mathbf{1} = \mathbf{1}$.

> [!info] Row or column convention
> This note, Durbin and most of bioinformatics write $p_{ij}$ as "from $i$ to $j$" and multiply a row vector on the left. Some texts use column vectors, $p_{t+1} = P^\top p_t$. Same chain, transposed bookkeeping: check which one a formula uses.

**A toy PAM.** Reduce the alphabet to purine (R) and pyrimidine (Y), and let 1 % of sites change per step (invented numbers):
$$P = \begin{pmatrix} 0.99 & 0.01 \\ 0.01 & 0.99 \end{pmatrix}, \quad P^n = \begin{pmatrix} \frac{1 + 0.98^n}{2} & \frac{1 - 0.98^n}{2} \\ \frac{1 - 0.98^n}{2} & \frac{1 + 0.98^n}{2} \end{pmatrix}$$
(check $n = 1$, then multiply by $P$ to get $n + 1$). After 250 steps, $P(\text{same state}) = \tfrac12(1 + 0.98^{250}) \approx 0.5032$: the chain has almost forgotten where it started, although 250 changes per 100 sites have been "applied", because many hit sites that had already changed, some changing back. Dayhoff's model applies exactly this logic to the 20 amino acids.[^dayhoff]

**Diagonal and triangular shortcuts.** If $D$ is diagonal, $DA$ scales the rows of $A$ and $AD$ scales its columns: normalizing each sample of a count matrix by its library size is $X D^{-1}$ with $D = \operatorname{diag}(N_1, \dots, N_n)$ ([[Count Normalization]]).

## Advanced (L3)

- **Cost.** The definition costs $mnp$ multiply-adds; $n^3$ for two $n \times n$ matrices ([[Big O Notation]]). A matrix power $P^t$ by repeated multiplication costs $t - 1$ products, by **repeated squaring** about $2\log_2 t$: $250 = 11111010_2$, so 7 squarings give $P^2, P^4, \dots, P^{128}$ and 5 more products combine $P^2 P^8 P^{16} P^{32} P^{64} P^{128}$, 12 products instead of 249.
- **Grouping changes the cost, not the result.** For $X$ of size $n \times p$ and $v \in \mathbb{R}^p$, $(X^\top X)v$ costs $np^2 + p^2$ multiplications, $X^\top (Xv)$ only $2np$. Choosing the cheapest parenthesization of a chain $A_1 A_2 \cdots A_k$ is the classic matrix-chain problem of [[Dynamic Programming]].[^cormen]
- **Faster than $n^3$.** Strassen's algorithm multiplies $2 \times 2$ block matrices with 7 block products instead of 8; the recurrence $T(n) = 7T(n/2) + O(n^2)$ gives $O(n^{\log_2 7}) \approx O(n^{2.81})$.[^cormen] Block multiplication also lets an implementation work on sub-blocks that fit in fast memory ([[Memory Hierarchy]], [[Numerical Linear Algebra]]).
- **From steps to continuous time.** A discrete chain has $P^t$ for integer $t$; nucleotide and amino acid substitution models in phylogenetics use a rate matrix $Q$ and $P(t) = e^{Qt}$ for any real $t \ge 0$ ([[Matrix Exponential]], [[Nucleotide Substitution Model]]). Powers are computed fastest through [[Diagonalization]], $P^t = V \Lambda^t V^{-1}$.

## Mathematical representation

- $A \in \mathbb{R}^{m \times n}$, $B \in \mathbb{R}^{n \times p}$: $(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$, $AB \in \mathbb{R}^{m \times p}$.
- Column view: $AB = [\,Ab_1 \;\cdots\; Ab_p\,]$ with $b_j$ the columns of $B$. Outer-product view: $AB = \sum_{k=1}^{n} a_{:k}\, b_{k:}$ (column $k$ of $A$ times row $k$ of $B$).
- Powers: $P^0 = I$, $P^{t+1} = P^t P$. Markov chain: $p_{t+1} = p_t P$, $p_t = p_0 P^t$, $P^{s+t} = P^s P^t$.
- PAM: $\mathrm{PAM}_n = (\mathrm{PAM}_1)^n$ for the mutation probability matrices.[^dayhoff]

## Computational representation

```python
def matmul(A, B):
    """C = AB for lists of rows; C[i][j] = sum_k A[i][k] * B[k][j]."""
    n, m, p = len(A), len(B), len(B[0])
    if len(A[0]) != m:
        raise ValueError(f"inner dimensions differ: {len(A[0])} != {m}")
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = A[i][k]
            for j in range(p):            # row i of C += a_ik * (row k of B)
                C[i][j] += aik * B[k][j]
    return C


def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matpow(P, t):
    """P**t by repeated squaring."""
    result, base = identity(len(P)), P
    while t:
        if t & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        t >>= 1
    return result


A, B = [[1, 2], [3, 4]], [[0, 1], [1, 0]]
print(matmul(A, B), matmul(B, A))          # AB != BA

# Invented 2-state chain: purine (R) or pyrimidine (Y), 1 % change per step
P = [[0.99, 0.01],
     [0.01, 0.99]]
p0 = [[1.0, 0.0]]                          # row vector: start in state R
print(matmul(p0, P), matmul(matmul(p0, P), P))
P250 = matpow(P, 250)
print([[round(x, 4) for x in row] for row in P250])
print(round(0.5 + 0.5 * 0.98 ** 250, 4))   # closed form

import numpy as np
An, Bn = np.array(A), np.array(B)
print((An @ Bn).tolist(), (An * Bn).tolist())   # matrix product vs entrywise product
print(np.round(np.linalg.matrix_power(np.array(P), 250), 4).tolist())
```

```text
[[2, 1], [4, 3]] [[3, 4], [1, 2]]
[[0.99, 0.01]] [[0.9802, 0.0198]]
[[0.5032, 0.4968], [0.4968, 0.5032]]
0.5032
[[2, 1], [4, 3]] [[0, 2], [3, 0]]
[[0.5032, 0.4968], [0.4968, 0.5032]]
```

The loop order `i, k, j` walks along rows of `B` and `C`, the order in which a list of rows is stored. In NumPy, `@` is the matrix product and `*` the entrywise product: confusing them gives a result of the right shape and the wrong values.

## Worked example

> [!example] Three steps of a Markov chain (invented)
> Three states (say, low, medium and high expression of a gene in a cell lineage), transition matrix
> $$Q = \begin{pmatrix} 0.5 & 0.5 & 0 \\ 0.25 & 0.5 & 0.25 \\ 0 & 0.5 & 0.5 \end{pmatrix}, \qquad p_0 = (1, 0, 0).$$
> 1. **Step 1**: $p_1 = p_0 Q$ = row 1 of $Q$ = $(0.5, 0.5, 0)$.
> 2. **Step 2**, row view (a combination of the rows of $Q$ with weights $p_1$): $p_2 = 0.5\,(0.5, 0.5, 0) + 0.5\,(0.25, 0.5, 0.25) = (0.375, 0.5, 0.125)$.
> 3. **Step 3**: $p_3 = 0.375\,(0.5, 0.5, 0) + 0.5\,(0.25, 0.5, 0.25) + 0.125\,(0, 0.5, 0.5) = (0.3125, 0.5, 0.1875)$.
> 4. **Check by powers**: `matmul([[1.0, 0.0, 0.0]], matpow(Q, 3))` returns `[[0.3125, 0.5, 0.1875]]`, as associativity requires.
> 5. **Sanity**: each $p_t$ sums to 1. The middle state keeps probability 0.5 from step 1 on; the chain drifts toward its stationary distribution $(0.25, 0.5, 0.25)$, the left eigenvector of $Q$ for eigenvalue 1 ([[Eigenvalues and Eigenvectors]]).

## Common misconceptions

> [!warning] "AB = BA, as with numbers"
> False in general, and not even shape-compatible for rectangular matrices. Applying "first $B$ then $A$" differs from "first $A$ then $B$", as rotating then scaling differs from scaling then rotating along one axis.

> [!warning] "(AB)ᵀ = AᵀBᵀ"
> The order reverses: $(AB)^\top = B^\top A^\top$. In code, `T(matmul(A, B)) == matmul(T(A), T(B))` is `False` for the matrices above; with `T(B), T(A)` it is `True`.

> [!warning] "PAM250 means that 250 % of positions differ"
> PAM250 is 250 accepted point mutations per 100 residues, applied as 250 steps of a Markov chain.[^dayhoff] Many changes hit the same site, some revert, so the observed difference is far lower: in the two-state toy, 250 steps leave 50.3 % of sites in their original class.

> [!warning] "`A * B` multiplies matrices in NumPy"
> It multiplies entrywise (and broadcasts). The matrix product is `A @ B` or `np.matmul(A, B)`.

## Exercises

> [!question] Exercise 1 (L1)
> $A = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 2 & 1 \\ 1 & 0 \end{pmatrix}$. Give the shapes of $AB$ and $BA$ and compute both.

> [!success]- Solution
> $AB$ is $2 \times 2$: $\begin{pmatrix} 5 & 1 \\ 4 & 2 \end{pmatrix}$ (e.g. $(AB)_{11} = 3 + 0 + 2 = 5$). $BA$ is $3 \times 3$: $\begin{pmatrix} 2 & 3 & 7 \\ 1 & 3 & 5 \\ 1 & 0 & 2 \end{pmatrix}$. `matmul` confirms both.

> [!question] Exercise 2 (L1)
> With $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, describe in words what $BA$ and $AB$ do to any $2 \times 2$ matrix $A$, using the row and column views.

> [!success]- Solution
> Row view: row 1 of $BA$ is $0 \cdot (\text{row 1 of } A) + 1 \cdot (\text{row 2 of } A)$, so $BA$ swaps the rows of $A$. Column view: $AB$ swaps the columns. $B$ is a permutation matrix; [[Gaussian Elimination]] uses such matrices for row exchanges.

> [!question] Exercise 3 (L2)
> Prove $(AB)^\top = B^\top A^\top$ entry by entry.

> [!success]- Solution
> $((AB)^\top)_{ij} = (AB)_{ji} = \sum_k a_{jk} b_{ki} = \sum_k (B^\top)_{ik} (A^\top)_{kj} = (B^\top A^\top)_{ij}$.

> [!question] Exercise 4 (L2, Python)
> Split the $4 \times 4$ matrices $M = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 1 & 3 & 0 \\ 2 & 0 & 1 & 1 \\ 1 & 1 & 0 & 2 \end{pmatrix}$ and $N = \begin{pmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 1 \end{pmatrix}$ into $2 \times 2$ blocks and check that the top-left block of $MN$ is $M_{11}N_{11} + M_{12}N_{21}$.

> [!success]- Solution
> ```python
> M = [[1, 2, 0, 1], [0, 1, 3, 0], [2, 0, 1, 1], [1, 1, 0, 2]]
> N = [[1, 0, 2, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 2, 1, 1]]
> blk = lambda X, r, c: [row[c:c + 2] for row in X[r:r + 2]]
> addm = lambda X, Y: [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]
> C11 = addm(matmul(blk(M, 0, 0), blk(N, 0, 0)), matmul(blk(M, 0, 2), blk(N, 2, 0)))
> print(C11, blk(matmul(M, N), 0, 0))
> # [[1, 4], [3, 4]] [[1, 4], [3, 4]]
> ```

> [!question] Exercise 5 (L3)
> (a) How many matrix products does repeated squaring need for $P^{250}$, and why? (b) For $X$ of size $1000 \times 50$ and $v \in \mathbb{R}^{50}$, count the multiplications of $(X^\top X)v$ and of $X^\top(Xv)$.

> [!success]- Solution
> (a) $250 = 11111010_2$ has 8 binary digits and six 1s: 7 squarings ($P^2, \dots, P^{128}$) and 5 products to combine the six needed powers, 12 in total. (b) $X^\top X$ costs $1000 \times 50^2 = 2{,}500{,}000$, then $\times v$ costs 2,500: 2,502,500. $Xv$ costs 50,000 and $X^\top(\cdot)$ another 50,000: 100,000, 25 times fewer, same result.[^cormen]

> [!question] Exercise 6 (L3, Python)
> In the two-state toy PAM, find the smallest number of steps $n$ after which fewer than 60 % of sites are in their original class. Check against the closed form.

> [!success]- Solution
> ```python
> P = [[0.99, 0.01], [0.01, 0.99]]
> Pn, n = identity(2), 0
> while Pn[0][0] >= 0.6:
>     Pn, n = matmul(Pn, P), n + 1
> print(n, round(Pn[0][0], 4))
> # 80 0.5993
> ```
> Closed form: $\tfrac12(1 + 0.98^n) < 0.6 \iff 0.98^n < 0.2 \iff n > \ln 0.2 / \ln 0.98 \approx 79.7$, so $n = 80$. Observed similarity saturates long before the number of changes does, the reason distances in phylogenetics need multiple-hit corrections ([[Nucleotide Substitution Model]]).

## Mastery checklist

- [ ] 1 Recognized: I can check whether a product is defined and give its shape.
- [ ] 2 Understood: I can compute a product by entries, columns, rows and outer products, and explain associativity, non-commutativity and $(AB)^\top = B^\top A^\top$.
- [ ] 3 Practiced: I can implement `matmul` and `matpow` by hand, verify block multiplication, and use `@` correctly in NumPy.
- [ ] 4 Applied: I propagated a real or simulated Markov chain (for example the Wright-Fisher model in [[07-evolution-simulator]]) with matrix powers and checked the distributions sum to 1.
- [ ] 5 Explained: I can explain PAM extrapolation and its Markov assumption, the cost of products and of their grouping, and the link to $e^{Qt}$.

## References

[^strang]: [[Introduction to Linear Algebra (Strang)]], 6th ed. (2023).
[^1806]: [[MIT 18.06SC - Linear Algebra]], Unit I "Ax = b and the Four Subspaces".
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models".
[^dayhoff]: [[Dayhoff 1978 - A Model of Evolutionary Change in Proteins]], *Atlas of Protein Sequence and Structure* 5(3):345-352.
[^cormen]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022): ch. 14 "Dynamic Programming" (matrix-chain multiplication) and the divide-and-conquer treatment of Strassen's algorithm.
