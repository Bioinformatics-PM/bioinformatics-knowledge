---
aliases:
  - Loop Invariant Proof
  - Invariant
  - Invariant Principle
  - Invariant de boucle
tags:
  - type/concept
  - domain/computer-science
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mathematical Induction]]"
  - "[[Proof Techniques]]"
  - "[[Model of Computation]]"
related:
  - "[[Recursion]]"
  - "[[Binary Search]]"
  - "[[Sorting]]"
  - "[[State Machine]]"
  - "[[Dynamic Programming]]"
  - "[[Property-Based Testing]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
---

# Loop Invariant

> [!abstract]
> A loop invariant is a property of a loop's variables that holds every time control reaches the top of the loop; showing that it holds at the start, survives each iteration and, combined with the exit condition, implies the desired result proves an iterative algorithm correct for every input.

## Definition

A **loop invariant** is a predicate on the program state that is true before each iteration of a loop, that is, each time the loop test is evaluated. A correctness proof with it has three parts:[^clrs2]

1. **Initialization**: it is true before the first iteration.
2. **Maintenance**: if it is true before an iteration, it remains true before the next one.
3. **Termination**: the loop terminates, and the invariant, together with the reason the loop stopped, gives a property that shows the algorithm correct.

The first two parts are an induction on the number of iterations (base case, inductive step); unlike ordinary induction, the argument stops when the loop does.[^clrs2] For any state machine, the same idea is the **Invariant Principle**: a property that holds in the start state and is preserved by every transition holds in every reachable state.[^lehman][^mit6042]

## Why it matters

- **Scans without off-by-one errors.** GC content, k-mer counts, sliding windows and running maxima are loops whose bounds are where bugs live. The invariant says exactly which prefix or window the variables describe (Exercise 2).
- **Index structures.** Binary search in a sorted [[Suffix Array]] is correct only if its boundary invariant holds ("if the pattern occurs, it lies in `[lo, hi)`"); see [[Binary Search]] and Exercise 4.
- **Dynamic programming.** Filling an alignment matrix is a loop whose invariant is "every cell already filled holds the optimal score of its two prefixes": with the recurrence, that is the correctness proof of [[Needleman-Wunsch Algorithm]] ([[Dynamic Programming]]).
- **Testing.** An invariant is checkable: written as an `assert` and run on random inputs, a proof idea becomes a test ([[Property-Based Testing]], [[Defensive Programming]]), the standard for every routine of [[bio-algorithms]].

## Core (L1)

### The three parts on GC counting

```text
GC-COUNT(s[1..n])
1  g = 0
2  for i = 1 to n
3      if s[i] = G or s[i] = C
4          g = g + 1
5  return g
```

**Invariant**: at the start of the iteration with index $i$, $g$ equals the number of G and C in $s[1..i-1]$.

- **Initialization.** For $i = 1$, $s[1..0]$ is empty and $g = 0$.
- **Maintenance.** Assume $g = \mathrm{GC}(s[1..i-1])$. Lines 3 and 4 add 1 exactly when $s[i]$ is G or C, so afterwards $g = \mathrm{GC}(s[1..i])$; then $i$ increases by 1 and the invariant holds for the new $i$.
- **Termination.** $i$ starts at 1 and increases by 1 per iteration, so the loop stops with $i = n + 1$. Substituting into the invariant: $g = \mathrm{GC}(s[1..n])$, the required result.

### Insertion sort

The textbook example: for the outer loop of insertion sort, the invariant is "at the start of the iteration with index $i$, $A[1..i-1]$ holds the elements originally in $A[1..i-1]$, in sorted order".[^clrs2] Each iteration inserts $A[i]$ at its place in the sorted prefix; at exit $i = n + 1$, so the whole array holds the original elements in sorted order (Worked example). The maintenance step relies on the inner loop doing its job, which is proved with an invariant of its own (Deeper).

## Deeper (L2)

> [!tip] Finding an invariant
> Generalize the postcondition by replacing a constant with the loop variable: "$g$ counts G and C in $s[1..n]$" becomes "$g$ counts G and C in $s[1..i-1]$". Then check that it is strong enough: "$g \ge 0$" is also invariant, but it implies nothing useful at exit.

**Nested loops, inside out.** In 0-based Python, the inner loop of insertion sort is `while j >= 0 and a[j] > key: a[j + 1] = a[j]; j -= 1`, started with `key = a[i]`, `j = i - 1`. Its invariant, at each evaluation of the test: `a[0..j]` is unchanged since the outer iteration began (so still sorted), and `a[j+2..i]` holds the original `a[j+1..i-1]` shifted one slot right, every element of it greater than `key`. It holds initially (`a[i+1..i]` is empty); each shift preserves it; at exit, either `j = -1` or `a[j] <= key`, so writing `key` into `a[j+1]` leaves `a[0..i]` sorted. That lemma is exactly what the outer loop's maintenance step needs. (The slot `a[j+1]` holds a stale copy while the loop runs: the invariant deliberately says nothing about it.)

**Termination needs a variant.** A **variant** is a natural-number-valued function of the state that strictly decreases at every iteration; since a strictly decreasing sequence of natural numbers is finite, the loop stops.[^lehman] Examples: $n + 1 - i$ for a counting loop, $j + 1$ for the inner loop above, `hi - lo` for binary search. An invariant plus the exit condition gives **partial correctness** (if the loop stops, the result is right); the variant adds **termination**; together they give total correctness.[^lehman]

**Constant-time window updates.** A sliding GC window keeps the invariant "$g$ is the GC count of the current window" and updates it in $O(1)$ per shift, adding the entering base and removing the leaving one (Exercise 3): the invariant is what makes the shortcut provably equal to recounting.

## Advanced (L3)

- **Representation invariants.** A data structure carries an invariant that every operation must preserve: the order property of a [[Heap]] or a [[Binary Search Tree]], the sortedness of a suffix array. This is the Invariant Principle with operations as the transitions: if each operation preserves the property, every reachable state of the structure satisfies it.[^lehman]
- **Dynamic programming tables.** With the invariant "every cell before $(i, j)$ in fill order holds the optimal score of its prefixes", the recurrence proves the next cell correct. The fill order must put each cell after the cells it depends on, a topological order of the subproblem graph ([[Dynamic Programming]], [[Topological Sort]]).
- **Streams and merges.** A k-mer counter over a FASTQ stream maintains "the table counts exactly the records consumed so far"; partial tables from several files can be merged (summed) because the invariant composes. Code that breaks it silently, for instance by mutating a list while iterating over it, is where real pipelines fail.

## Mathematical representation

- State $\sigma \in S$, loop guard $B \subseteq S$, body $f : S \to S$. The run is $\sigma_0$, $\sigma_{k+1} = f(\sigma_k)$ while $\sigma_k \in B$.
- An **invariant** $I \subseteq S$ satisfies $\sigma_0 \in I$ (initialization) and $\forall \sigma \in I \cap B : f(\sigma) \in I$ (maintenance). By induction on $k$: $\sigma_k \in I$ for every iteration $k$ reached.
- A **variant** $v : S \to \mathbb{N}$ satisfies $\forall \sigma \in I \cap B : v(f(\sigma)) < v(\sigma)$. Then $v(\sigma_k) \le v(\sigma_0) - k$, and since $v \ge 0$ the loop runs at most $v(\sigma_0)$ iterations.
- **Correctness**: if $I \cap \overline{B} \subseteq Q$, the final state lies in the postcondition $Q$. As an inference rule: from "$\{I \wedge B\}$ body $\{I\}$" conclude "$\{I\}$ while $B$ do body $\{I \wedge \neg B\}$".

## Computational representation

An invariant becomes an `assert` at the top of the loop, and random inputs exercise it:

```python
import random

def gc_count(seq: str) -> int:
    g = 0
    for i, base in enumerate(seq):
        assert g == sum(b in "GC" for b in seq[:i])   # invariant (checking it costs O(i))
        if base in "GC":
            g += 1
    return g

def insertion_sort(a: list) -> list:
    original = list(a)
    for i in range(1, len(a)):
        assert a[:i] == sorted(original[:i])          # invariant of the outer loop
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:                  # shift larger items one slot right
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    assert a == sorted(original)                      # postcondition
    return a

random.seed(0)
for _ in range(1000):
    s = "".join(random.choices("ACGT", k=random.randint(0, 40)))
    assert gc_count(s) == s.count("G") + s.count("C")
    insertion_sort([s[i:i + 3] for i in range(len(s) - 2)])
print("invariants held on 1000 random inputs")
```

```text
invariants held on 1000 random inputs
```

Checking an invariant can cost more than the loop itself (here $O(i)$ per iteration, so the checked GC count is quadratic). Keep such checks for tests: `python3 -O` strips `assert` statements (`python3 -O -c "assert False; print('stripped')"` prints `stripped`).

## Worked example

> [!example] Insertion sort of toy k-mers, invariant at each step
> Input (invented): `["GAT", "ACA", "TTG", "ACC", "CGT"]`, sorted lexicographically. Printing the state at the top of each iteration (left of `|` is the prefix the invariant talks about):
> ```text
> before i=1: ['GAT'] | ['ACA', 'TTG', 'ACC', 'CGT']
> before i=2: ['ACA', 'GAT'] | ['TTG', 'ACC', 'CGT']
> before i=3: ['ACA', 'GAT', 'TTG'] | ['ACC', 'CGT']
> before i=4: ['ACA', 'ACC', 'GAT', 'TTG'] | ['CGT']
> exit, i=5: ['ACA', 'ACC', 'CGT', 'GAT', 'TTG']
> ```
> 1. **Initialization** ($i = 1$): a one-element prefix is sorted.
> 2. **Maintenance**: at $i = 3$, `ACC` moves left past `TTG` and `GAT` and stops after `ACA` (`ACA` ≤ `ACC`), so the prefix of length 4 is sorted and holds the first 4 original items.
> 3. **Termination**: the loop exits with $i = 5 = n$ (0-based), and the invariant for the prefix of length 5 is the postcondition. Sorting all suffixes of a text this way is the naive construction of a [[Suffix Array]].

## Common misconceptions

> [!warning] "An invariant is a value that never changes"
> The variables change at every iteration; what stays true is a relation between them, and only at the top of the loop. Inside the body it may be temporarily false: in insertion sort, the array holds a duplicated element while the inner loop shifts.

> [!warning] "Initialization and maintenance are enough"
> They prove only that *if* the loop stops, the result is right. `while i != n: i += 2`, started at `i = 0` with odd `n`, preserves "`i` is even" forever and never stops. A termination argument (a variant) is the third, independent part.

> [!warning] "Any true property will do"
> "$0 \le g \le n$" is a valid invariant of the GC loop and proves nothing. The invariant must be strong enough to imply the postcondition at exit, and weak enough to be true initially: finding that balance is the actual work.

## Exercises

> [!question] Exercise 1 (L1)
> `best = scores[0]`, then `for i in range(1, n): if scores[i] > best: best = scores[i]`. State the invariant, prove the three parts, and give the precondition the proof needs.

> [!success]- Solution
> Invariant: before the iteration with index $i$, `best` $= \max(\texttt{scores}[0..i-1])$. Initialization ($i = 1$): `best = scores[0]` is the maximum of a one-element prefix. Maintenance: the new maximum of $\texttt{scores}[0..i]$ is either the old one or `scores[i]`, and the `if` picks the larger. Termination: the loop exits with $i = n$, so `best` is the maximum of the whole list. Precondition: $n \ge 1$, otherwise `scores[0]` does not exist; the proof makes this hidden assumption visible.

> [!question] Exercise 2 (L1)
> A GC counter reads `g = 0`, then `for i in range(1, len(s)): if s[i] in "GC": g += 1`. Which part of the invariant proof fails, and how do you fix the code?

> [!success]- Solution
> The intended invariant is "before iteration $i$, $g = \mathrm{GC}(s[0..i-1])$". At the first iteration $i = 1$ it requires $g = [s_0 \in \{G, C\}]$, but $g = 0$: **initialization** fails whenever the sequence starts with G or C, so the first base is never counted. Fix: `range(0, len(s))` (or initialize `g = int(s[0] in "GC")` for non-empty `s`). Maintenance and termination were fine, which is why the bug survives tests that start with A or T.

> [!question] Exercise 3 (L2, Python)
> Write `gc_windows(seq, w)`, the GC count of every window of width $w$, updated in $O(1)$ per window. State the invariant and test against recounting.

> [!success]- Solution
> Invariant at the top of the iteration with index $i$: $g$ is the GC count of `seq[i - 1 : i - 1 + w]`. Moving the window adds base `seq[i + w - 1]` and drops `seq[i - 1]`, which maintains it.
> ```python
> import random
>
> def gc_windows(seq: str, w: int) -> list[int]:
>     g = sum(b in "GC" for b in seq[:w])                # GC count of the first window
>     counts = [g]
>     for i in range(1, len(seq) - w + 1):
>         # invariant: g is the GC count of seq[i - 1 : i - 1 + w]
>         g += (seq[i + w - 1] in "GC") - (seq[i - 1] in "GC")
>         counts.append(g)
>     return counts
>
> random.seed(1)
> for _ in range(500):
>     s = "".join(random.choices("ACGT", k=random.randint(5, 50)))
>     w = random.randint(1, 5)
>     assert gc_windows(s, w) == [sum(b in "GC" for b in s[i:i + w]) for i in range(len(s) - w + 1)]
> print(gc_windows("GGCATTACGC", 4))
> ```
> Output: `[3, 2, 1, 0, 1, 2, 3]`. Total cost $\Theta(n)$ instead of $\Theta(nw)$ for recounting every window ([[GC Content]] uses such windows along a genome).

> [!question] Exercise 4 (L2)
> `lo, hi = 0, n`, then `while lo < hi: mid = (lo + hi) // 2; if a[mid] < x: lo = mid + 1 else: hi = mid`, on a sorted list `a`. Give the invariant and a variant. What goes wrong if `lo = mid + 1` is replaced by `lo = mid`?

> [!success]- Solution
> Invariant: every element of `a[:lo]` is $< x$ and every element of `a[hi:]` is $\ge x$; it holds initially (both slices empty) and each branch preserves it because `a` is sorted. Variant: `hi - lo`. Since `lo <= mid < hi`, both `lo = mid + 1` and `hi = mid` decrease it. At exit `lo == hi` is the first index with `a[lo] >= x`, the insertion point. With `lo = mid`, when `hi = lo + 1` and `a[lo] < x`, `mid = lo` and nothing changes: the variant does not decrease, and the loop runs forever ([[Binary Search]]).

> [!question] Exercise 5 (L3, Python)
> Reverse-complement a `bytearray` in place with two indices moving toward each other. Write the invariant and variant as comments, handle odd lengths, and test against slicing.

> [!success]- Solution
> ```python
> import random
>
> COMP = bytes.maketrans(b"ACGT", b"TGCA")
>
> def rc_in_place(buf: bytearray) -> None:
>     i, j = 0, len(buf) - 1
>     while i < j:
>         # invariant: i + j == n - 1; buf[:i] and buf[j + 1:] hold their final bases;
>         # buf[i : j + 1] is still the original middle
>         buf[i], buf[j] = COMP[buf[j]], COMP[buf[i]]
>         i, j = i + 1, j - 1                         # variant j - i drops by 2
>     if i == j:                                      # odd length: complement the middle base
>         buf[i] = COMP[buf[i]]
>
> random.seed(2)
> for n in list(range(0, 6)) + [random.randint(6, 60) for _ in range(300)]:
>     s = "".join(random.choices("ACGT", k=n))
>     buf = bytearray(s, "ascii")
>     rc_in_place(buf)
>     assert buf.decode() == s.translate(str.maketrans("ACGT", "TGCA"))[::-1]
> buf = bytearray(b"GATTACA")
> rc_in_place(buf)
> print(buf.decode())
> ```
> Output: `TGTAATC`. At exit $i > j$ (even length: everything placed) or $i = j$ (odd length: only the middle base, its own mirror, remains to be complemented). Memory: $O(1)$ beyond the input, against $O(n)$ for slicing ([[Reverse Complement]], [[Space Complexity]]).

## Mastery checklist

- [ ] 1 Recognized: I can state the three parts of a loop-invariant proof.
- [ ] 2 Understood: I can explain why initialization and maintenance form an induction, and why termination needs a separate argument (a variant).
- [ ] 3 Practiced: I can write and prove invariants for scans, insertion sort (both loops) and binary search, and assert them in tests.
- [ ] 4 Applied: the scanning functions of [[01-dna-engine]] and the routines of [[bio-algorithms]] carry their invariants as comments and assertions in randomized tests.
- [ ] 5 Explained: I can teach how invariants extend to data structures and dynamic programming tables, and diagnose a buggy loop by finding which part of the proof fails.

## References

[^clrs2]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 2 "Getting Started" (insertion sort; loop invariants with initialization, maintenance and termination; the analogy with induction).
[^lehman]: [[Mathematics for Computer Science (Lehman)]], treatment of state machines (preserved invariants and the Invariant Principle, partial correctness and termination, strictly decreasing derived variables).
[^mit6042]: [[MIT 6.042J - Mathematics for Computer Science]], proofs and state machines.
