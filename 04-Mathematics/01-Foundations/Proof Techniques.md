---
aliases:
  - Direct Proof
  - Proof by Contrapositive
  - Proof by Contradiction
  - Proof by Cases
  - Exchange Argument
  - Techniques de démonstration
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mathematical Proof]]"
  - "[[Propositional Logic]]"
  - "[[Predicate Logic]]"
related:
  - "[[Mathematical Induction]]"
  - "[[Greedy Algorithm]]"
  - "[[Dynamic Programming]]"
  - "[[Edit Distance]]"
  - "[[Needleman-Wunsch Algorithm]]"
  - "[[Pigeonhole Principle]]"
  - "[[Loop Invariant]]"
projects:
  - "[[04-alignment-engine]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
---

# Proof Techniques

> [!abstract]
> Four patterns cover most proofs you will write: go straight from hypothesis to conclusion (direct), prove that a failed conclusion implies a failed hypothesis (contrapositive), show that denying the claim leads to an absurdity (contradiction), or split into cases that cover everything; together they are how greedy and dynamic-programming algorithms are shown to be correct.

## Definition

A **proof technique** is a standard logical pattern for proving a statement of a given form ([[Mathematical Proof]]).[^lehman1][^mcs]

- **Direct proof** of $P \to Q$: assume $P$, deduce $Q$.
- **Proof by contrapositive** of $P \to Q$: prove the equivalent $\neg Q \to \neg P$.
- **Proof by contradiction** of $\varphi$: assume $\neg \varphi$ and deduce a contradiction, a statement together with its negation.
- **Proof by cases**: split the situation into cases that together cover every possibility, and prove the claim in each.
- An **if and only if** statement $P \leftrightarrow Q$ needs two proofs, $P \to Q$ and $Q \to P$.

Statements "for all $n$" built step by step have their own technique, [[Mathematical Induction]].

## Why it matters

- **Greedy algorithms need a proof.** A greedy rule that looks reasonable can be wrong (making change with coins 1, 3, 4: Deeper); when it is right, the standard argument is an **exchange argument**, usually by contradiction ([[Greedy Algorithm]]).[^clrs-greedy]
- **Dynamic programming rests on two proofs.** Optimal substructure is proved by contradiction ("cut and paste"), and the recurrence comes from a proof by cases on the last step, such as the last column of an alignment ([[Dynamic Programming]], [[Edit Distance]], [[Needleman-Wunsch Algorithm]], [[04-alignment-engine]]).[^clrs14][^compeau]
- **Filters must not lose answers.** Seed-based search finds approximate matches through exact pieces; the guarantee that no match is missed is a short proof by contrapositive (Core) ([[Sequence Alignment]]).
- **Impossibility results.** Counting arguments prove that something cannot exist, such as an injective genetic code ([[Function#Core (L1)]], [[Pigeonhole Principle]]).

## Core (L1)

| To prove | Technique | Assume | Then show |
|---|---|---|---|
| $P \to Q$ | direct | $P$ | $Q$ |
| $P \to Q$ | contrapositive | $\neg Q$ | $\neg P$ |
| $\varphi$ | contradiction | $\neg \varphi$ | some $R$ and $\neg R$ |
| $Q$ | cases $C_1, \dots, C_k$ | each $C_i$ in turn, with $C_1 \lor \dots \lor C_k$ true | $Q$ in every case |
| $\neg \forall x\, P(x)$ | counterexample | (nothing) | one $x$ with $\neg P(x)$ |

### Direct proof

**Theorem.** If $n$ is odd, then $n^2$ is odd.
*Proof.* $n = 2k + 1$ for an integer $k$, so $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which is odd. ∎

### Contrapositive

**Lemma.** If $n^2$ is even, then $n$ is even.
*Proof.* The contrapositive is "if $n$ is odd, then $n^2$ is odd", just proved directly. ∎ A direct attempt would start from "$n^2 = 2k$" and get stuck: nothing says how to take the square root of $2k$.

**Bio: lossless seeds.** Let a read $r$ and a reference window $w$ have the same length, and cut $r$ into $e + 1$ disjoint pieces (with $w$ cut at the same positions). *Claim:* if the Hamming distance $d(r, w) \le e$, then at least one piece of $r$ matches $w$ exactly.
*Proof by contrapositive.* Suppose no piece matches exactly. Then each of the $e + 1$ pieces holds at least one mismatch, and the pieces are disjoint, so $d(r, w) \ge e + 1 > e$. ∎
Consequence: searching exactly for the $e + 1$ pieces finds **every** occurrence with at most $e$ mismatches, an application of the [[Pigeonhole Principle]].

### Contradiction

**Theorem.** $\sqrt{2}$ is irrational.
*Proof.* Suppose, for contradiction, $\sqrt{2} = p/q$ with integers $p, q$ having no common factor. Then $p^2 = 2q^2$ is even, so $p$ is even by the lemma: $p = 2k$. Then $4k^2 = 2q^2$, so $q^2 = 2k^2$ is even and $q$ is even. Both are even, contradicting "no common factor". ∎[^lehman1]

### Cases

**Theorem.** For every integer $n$, $n(n + 1)$ is even, so the number of pairs among $n$ sequences, $n(n-1)/2$, is always an integer.
*Proof.* Case 1, $n$ even: $n = 2k$ and $n(n+1) = 2k(n+1)$ is even. Case 2, $n$ odd: $n + 1$ is even, so the product is even. Every integer is even or odd, so the cases are exhaustive. ∎ (Apply it to $n - 1$ for the pair count.)

## Deeper (L2)

### Greedy algorithms: the exchange argument

**Problem** (interval scheduling): given intervals $[s_i, e_i)$ on a sequence, such as candidate amplicons or features, choose as many pairwise disjoint ones as possible. **Greedy rule**: sort by end and keep each interval that starts at or after the end of the last one kept.[^clrs-greedy]

**Lemma (greedy choice).** Some optimal solution contains the interval $g$ with the earliest end.
*Proof (exchange).* Take any optimal solution $O$ and its interval $o$ with the earliest end. If $o = g$, done. Otherwise replace $o$ by $g$: since $e_g \le e_o$, $g$ ends no later than $o$ and so overlaps none of the other intervals of $O$, which all start at or after $e_o$. The new set is disjoint and has the same size: it is optimal and contains $g$. ∎

**Theorem.** The greedy rule returns a maximum set. *Proof sketch:* by the lemma, keep $g$; the rest of an optimal solution is an optimal solution of the intervals starting at or after $e_g$, which the greedy rule solves in the same way; induction on the number of intervals finishes ([[Mathematical Induction]]).

**Without a proof, greedy fails.** To pay 6 with coins 1, 3, 4, "largest coin first" gives $4 + 1 + 1$ (3 coins), while $3 + 3$ uses 2. One counterexample refutes the algorithm. The reasonable-looking "shortest interval first" fails as well (Exercise 4).

### Dynamic programming: cut-and-paste and cases

Let $D(i, j)$ be the edit distance between the prefixes $u_1 \dots u_i$ and $v_1 \dots v_j$ ([[Edit Distance]]).[^compeau]

1. **Cases on the last column.** An alignment of the two prefixes ends in exactly one of three ways: $u_i$ aligned with $v_j$, $u_i$ against a gap, or a gap against $v_j$.
2. **Optimal substructure, by contradiction.** Suppose an optimal alignment of the prefixes ends with column $(u_i, v_j)$, but what precedes it is **not** optimal for $u_1 \dots u_{i-1}$ and $v_1 \dots v_{j-1}$. Cut it out and paste in a cheaper alignment of those prefixes, then re-append the last column: the result is cheaper than the optimum, a contradiction. The same holds in the two other cases.[^clrs14]
3. **Recurrence.** Combining the cases, with $\delta(x, y) = \mathbb{1}[x \ne y]$:
$$D(i, j) = \min\big\{ D(i-1, j-1) + \delta(u_i, v_j),\ D(i-1, j) + 1,\ D(i, j-1) + 1 \big\},$$
with $D(i, 0) = i$ and $D(0, j) = j$. Filling the table in increasing $i + j$ is correct by induction ([[Needleman-Wunsch Algorithm]]).

## Advanced (L3)

- **Contradiction or contrapositive?** A proof by contradiction of $P \to Q$ assumes $P \land \neg Q$; if it never uses $P$ until the end, it is really a contrapositive and reads better written that way. Contradiction is worth it when the negation hands you an object to work with: an optimal solution without the greedy choice, a fraction in lowest terms, a counterexample.
- **Minimal counterexample.** "Suppose the claim fails; take the smallest $n$ for which it fails and derive a smaller failure" is the well-ordering principle, equivalent to induction.[^lehman2]
- **Constructive or not.** A constructive existence proof builds the object, so it is an algorithm; the pigeonhole principle only guarantees that two keys share a slot of a [[Hash Function]] without saying which. Bioinformatics favors constructive proofs because they can be run.

## Mathematical representation

Each technique is a tautology of [[Propositional Logic]], true under every assignment of truth values:

- contrapositive: $(P \to Q) \leftrightarrow (\neg Q \to \neg P)$;
- contradiction: $\big(\neg \varphi \to (R \land \neg R)\big) \to \varphi$;
- cases: $\big((C_1 \lor C_2) \land (C_1 \to Q) \land (C_2 \to Q)\big) \to Q$;
- iff: $(P \leftrightarrow Q) \leftrightarrow \big((P \to Q) \land (Q \to P)\big)$;
- counterexample: $\neg \forall x\, P(x) \leftrightarrow \exists x\, \neg P(x)$ ([[Predicate Logic]]).

The converse $(P \to Q) \leftrightarrow (Q \to P)$ is **not** a tautology.

## Computational representation

Truth tables check the laws; brute force checks algorithms on small inputs and finds counterexamples:

```python
import random
from itertools import combinations, product

# 1. The logical laws behind each technique, checked on every truth assignment.
implies = lambda p, q: (not p) or q
laws = {
    "contrapositive": lambda p, q, r: implies(p, q) == implies(not q, not p),
    "contradiction": lambda p, q, r: implies(implies(not p, q and not q), p),
    "cases": lambda p, q, r: implies((p or q) and implies(p, r) and implies(q, r), r),
    "converse (not a law)": lambda p, q, r: implies(p, q) == implies(q, p),
}
for name, law in laws.items():
    print(name, all(law(p, q, r) for p, q, r in product([False, True], repeat=3)))


# 2. A greedy algorithm without a proof: making change.
def greedy_change(amount: int, coins: tuple[int, ...]) -> list[int]:
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            amount -= c
            used.append(c)
    return used


def min_coins(amount: int, coins: tuple[int, ...]) -> int:
    best = [0] + [amount + 1] * amount              # dynamic programming over amounts
    for m in range(1, amount + 1):
        best[m] = min([best[m - c] + 1 for c in coins if c <= m] + [amount + 1])
    return best[amount]


coins = (1, 3, 4)
print(greedy_change(6, coins), min_coins(6, coins))


# 3. A greedy algorithm with a proof: maximum set of disjoint intervals.
def earliest_end_first(intervals):
    """Half-open intervals [start, end); keep each one that starts after the last kept end."""
    chosen, last_end = [], float("-inf")
    for start, end in sorted(intervals, key=lambda iv: iv[1]):
        if start >= last_end:
            chosen.append((start, end))
            last_end = end
    return chosen


def brute_force_size(intervals) -> int:
    for k in range(len(intervals), 0, -1):
        for subset in combinations(sorted(intervals), k):
            if all(a[1] <= b[0] for a, b in zip(subset, subset[1:])):
                return k
    return 0


amplicons = [(1, 30), (10, 20), (25, 45), (40, 60), (50, 55), (58, 80), (70, 95)]  # invented
print(earliest_end_first(amplicons), brute_force_size(amplicons))
random.seed(1)
trials = []
for _ in range(300):
    ivs = [(s, s + random.randrange(1, 15)) for s in random.sample(range(50), 8)]
    trials.append(len(earliest_end_first(ivs)) == brute_force_size(ivs))
print(sum(trials), len(trials))
```

```text
contrapositive True
contradiction True
cases True
converse (not a law) False
[4, 1, 1] 2
[(10, 20), (25, 45), (50, 55), (58, 80)] 4
300 300
```

300 agreements on random instances are evidence; the exchange argument is the proof.

## Worked example

> [!example] Exchange argument on invented amplicons
> Candidate amplicons (half-open, invented): `[1,30) [10,20) [25,45) [40,60) [50,55) [58,80) [70,95)`.
> 1. **Sort by end**: `[10,20) [1,30) [25,45) [50,55) [40,60) [58,80) [70,95)`.
> 2. **Scan**: keep `[10,20)`; skip `[1,30)` (starts before 20); keep `[25,45)`; keep `[50,55)`; skip `[40,60)`; keep `[58,80)`; skip `[70,95)` (starts before 80). Four amplicons.
> 3. **Exchange in action**: `{[1,30), [40,60), [70,95)}` is a disjoint set of size 3 starting with `[1,30)`. Swapping `[1,30)` for `[10,20)`, which ends earlier, keeps it disjoint; the lemma guarantees such swaps never lose optimality.
> 4. **Check**: brute force over all subsets also finds 4 (code above).

## Common misconceptions

> [!warning] "Proving the converse proves the statement"
> $Q \to P$ is a different statement: "if $n$ is even then $n^2$ is even" is true, but it does not prove "if $n^2$ is even then $n$ is even"; the contrapositive does. The truth table above shows the converse is not equivalent.

> [!warning] "A greedy algorithm that works on my examples is correct"
> "Largest coin first" works for coins 1, 5, 10, 25 on every amount below 100 (Exercise 3) but fails for 1, 3, 4. Greedy correctness is a property of the problem, established by an exchange argument or refuted by one counterexample.

> [!warning] "Cases may overlap or leave gaps if each is proved"
> Overlap is harmless, gaps are fatal: the cases must cover every possibility. In the alignment recurrence, forgetting "gap against $v_j$" silently forbids insertions.

## Exercises

> [!question] Exercise 1 (L1)
> Prove by contrapositive: if $n^2 + 2n$ is odd, then $n$ is odd.

> [!success]- Solution
> Contrapositive: if $n$ is even, then $n^2 + 2n$ is even. With $n = 2k$: $n^2 + 2n = 4k^2 + 4k = 2(2k^2 + 2k)$, even. ∎

> [!question] Exercise 2 (L1)
> (a) Prove by cases that $n^2$ leaves remainder 0 or 1 when divided by 4. (b) Prove by contradiction that any 65 codons read from a gene contain two identical codons.

> [!success]- Solution
> (a) $n$ even: $n = 2k$, $n^2 = 4k^2$, remainder 0. $n$ odd: $n = 2k + 1$, $n^2 = 4(k^2 + k) + 1$, remainder 1. ∎ (b) Suppose the 65 codons are pairwise distinct. There are only $4^3 = 64$ codons, so 65 distinct ones cannot exist: contradiction. ∎ ([[Pigeonhole Principle]].)

> [!question] Exercise 3 (L2, Python)
> Using `greedy_change` and `min_coins`, list the amounts below 20 where "largest coin first" is suboptimal for coins (1, 3, 4), and check coins (1, 5, 10, 25) below 100.

> [!success]- Solution
> ```python
> print([m for m in range(1, 20) if len(greedy_change(m, coins)) != min_coins(m, coins)])
> print([m for m in range(1, 100)
>        if len(greedy_change(m, (1, 5, 10, 25))) != min_coins(m, (1, 5, 10, 25))])
> ```
> Output: `[6, 10, 14, 18]`, then `[]`. For (1, 3, 4) each failure takes a 4 where two 3s do better (10 = 4 + 3 + 3). For (1, 5, 10, 25) no failure below 100: evidence, not a proof for every amount.

> [!question] Exercise 4 (L2)
> Show that "keep the shortest interval first" is not optimal for interval scheduling, using three intervals. Where does the exchange argument break for this rule?

> [!success]- Solution
> `[0,10) [9,12) [11,20)`: the shortest, `[9,12)`, overlaps both others, so the rule keeps 1 interval; `earliest_end_first` keeps `[0,10)` and `[11,20)`, which is 2. The exchange step needs the greedy interval to **end** no later than the one it replaces; a short interval can end later than an optimal one's first interval, so swapping it in may create overlaps.

> [!question] Exercise 5 (L3, Python)
> Implement the edit-distance recurrence of the Deeper section and compare it with an independent definition, the fewest single-letter edits found by breadth-first search over strings, for all pairs of words of length 0 to 4 over {A, C}. What does agreement show, and what does it not?

> [!success]- Solution
> ```python
> from collections import deque
>
>
> def edit_distance(u: str, v: str) -> int:
>     n, m = len(u), len(v)
>     D = [[i + j if i * j == 0 else 0 for j in range(m + 1)] for i in range(n + 1)]
>     for i in range(1, n + 1):
>         for j in range(1, m + 1):
>             D[i][j] = min(D[i - 1][j - 1] + (u[i - 1] != v[j - 1]),   # last column: (u_i, v_j)
>                           D[i - 1][j] + 1,                            # u_i against a gap
>                           D[i][j - 1] + 1)                            # gap against v_j
>     return D[n][m]
>
>
> def bfs_distance(u: str, v: str, alphabet: str = "AC") -> int:
>     """Fewest single-letter edits from u to v, by breadth-first search over strings."""
>     dist, queue = {u: 0}, deque([u])
>     while queue:
>         s = queue.popleft()
>         if s == v:
>             return dist[s]
>         edits = {s[:i] + s[i + 1:] for i in range(len(s))}
>         edits |= {s[:i] + a + s[i + 1:] for i in range(len(s)) for a in alphabet}
>         edits |= {s[:i] + a + s[i:] for i in range(len(s) + 1) for a in alphabet}
>         for t in edits:
>             if t not in dist and len(t) <= max(len(u), len(v)) + 1:
>                 dist[t] = dist[s] + 1
>                 queue.append(t)
>
>
> words = ["".join(p) for k in range(5) for p in product("AC", repeat=k)]
> print(len(words) ** 2, all(edit_distance(a, b) == bfs_distance(a, b) for a in words for b in words))
> ```
> Output: `961 True`. The 961 pairs show that the code implements the recurrence without an indexing bug on small inputs, against a definition that shares none of its logic ([[Graph Traversal]]). They say nothing about longer words; the cases-plus-contradiction argument does, for every length.

## Mastery checklist

- [ ] 1 Recognized: I can name the direct, contrapositive, contradiction and cases techniques and say what each assumes.
- [ ] 2 Understood: I can explain why the contrapositive is equivalent and the converse is not, and when contradiction is the natural choice.
- [ ] 3 Practiced: I can write short proofs with each technique and refute a claim with a counterexample.
- [ ] 4 Applied: in [[04-alignment-engine]], I justified the alignment recurrence by cases and optimal substructure, and tested it against brute force.
- [ ] 5 Explained: I can teach the exchange argument for a greedy algorithm and the cut-and-paste argument for dynamic programming.

## References

[^lehman1]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, ch. 1 "What is a Proof?", sections "Proving an Implication", "Proving an 'If and Only If'", "Proof by Cases" and "Proof by Contradiction".
[^lehman2]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, ch. 2 "The Well Ordering Principle" and section 5.3 "Strong Induction vs. Induction vs. Well Ordering".
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], fundamental-concepts third of the course (proofs).
[^clrs-greedy]: [[Introduction to Algorithms (Cormen)]], 4th ed., greedy algorithms chapter (activity selection, greedy-choice property).
[^clrs14]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 14 "Dynamic Programming" (optimal substructure).
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Compare Biological Sequences?" (dynamic programming, edit distance and alignment).
