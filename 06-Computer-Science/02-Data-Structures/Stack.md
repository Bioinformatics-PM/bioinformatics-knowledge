---
aliases:
  - LIFO
  - Pushdown Stack
  - Pile (structure de données)
tags:
  - type/concept
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Abstract Data Type]]"
  - "[[Array]]"
  - "[[Recursion]]"
related:
  - "[[Newick Format]]"
  - "[[RNA Secondary Structure]]"
projects:
  - "[[08-phylogenetic-engine]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Cardona 2008 - Extended Newick]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
---

# Stack

> [!abstract]
> A stack hands back the most recently added item first (last in, first out). That single rule is what nested structures need, from brackets and Newick trees to the call stack of a recursive function, which an explicit stack can replace.

## Definition

A **stack** is a dynamic set in which the element removed is the one most recently inserted: **last in, first out (LIFO)**. Insertion is called **push** and removal **pop**; with an array and an index to the top element, both take $O(1)$ time.[^clrs10]

## Why it matters

- **Nested formats.** Phylogenetic trees are exchanged in the Newick format, which writes a rooted tree as nested parentheses: a node's children are listed inside parentheses, separated by commas, followed by the node's label, and a semicolon ends the tree.[^cardona] Parsing it means remembering which internal nodes are still open ([[Newick Format]], [[08-phylogenetic-engine]]).
- **Trees deeper than the call stack.** Recursive tree code uses one Python frame per level, and CPython stops at its recursion limit (1000 here, `sys.getrecursionlimit()`). A fully unbalanced (caterpillar) tree of 5,000 leaves breaks a recursive parser; an explicit stack has no such limit (Computational representation). Depth-first traversals are stack disciplines too ([[Graph Traversal]]), and nested base-pair notations for RNA structures are brackets (Exercise 2, [[RNA Secondary Structure]]).

## Core (L1)

In Python, use a `list`: `append` pushes and `pop()` pops at the end, both $O(1)$ amortized ([[Array]]). Bracket matching is the canonical use. Invariant: the stack holds the openers not yet closed, most recent on top; a closer must match the top, otherwise two pairs would cross. Each character costs $O(1)$: $O(n)$ time and $O(d)$ space for a maximal nesting depth $d$.

```python
PAIRS = {")": "(", "]": "[", "}": "{"}

def balanced(text: str) -> bool:
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)                    # push the opener
        elif ch in PAIRS and (not stack or stack.pop() != PAIRS[ch]):
            return False                        # closer without its matching opener
    return not stack                            # every opener was closed

print([balanced(t) for t in ("([]{})", "([)]", "((", "())")])   # [True, False, False, False]
```

## Deeper (L2)

**Parsing Newick.** The parser below keeps on its stack the internal nodes whose child lists are still open. `(` pushes the current node and creates its first child; `,` creates a sibling under the node on top; `)` pops back to that node, so the label and length that follow describe it. It handles unquoted labels and reads a `:length` suffix as the branch length; [[Newick Format]] covers the full syntax. One pass, $O(1)$ per token; the stack depth is the nesting depth.

**Recursion is a stack.** Each recursive call pushes a frame (arguments, locals, return point) on the call stack and pops it on return, so any recursion can be rewritten with an explicit stack of "work still to do", which lives on the heap and is bounded by memory instead of by the recursion limit. Pre-order work is done when an item is popped; post-order work either pushes each item twice (to expand it, then to finish it after its children) or reuses a pre-order scanned backwards, as `leaf_counts` below does with the parser's numbering.

## Advanced (L3)

- **Why a stack, formally.** Balanced brackets form a context-free language: no finite automaton, hence no regular expression in the formal sense, recognizes them (Exercise 3), but a finite automaton with a stack, a pushdown automaton, does. Durbin et al. place biological sequences in this hierarchy: RNA secondary structures whose base pairs do not cross are nested like brackets and are modeled with context-free grammars, while crossing pairs (pseudoknots) fall outside that model ([[Stochastic Context-Free Grammar]], [[Regular Expression]]).[^durbin] Extended Newick keeps the parenthesized syntax for phylogenetic networks, tagging nodes with several parents, so the same stack parser carries over ([[Phylogenetic Network]]).[^cardona]

## Mathematical representation

A stack over a set $X$ is a word $s \in X^*$: $\mathrm{push}(s, x) = sx$, $\mathrm{pop}(sx) = (s, x)$, $\mathrm{pop}(\varepsilon)$ undefined. For one bracket type, with $h(w) = \#_{(}(w) - \#_{)}(w)$, a word is balanced iff $h(p) \ge 0$ for every prefix $p$ and $h(w) = 0$. With several types, counters are not enough: `([)]` meets both conditions for each type yet is not balanced, because pairs must nest, which checking against the top of a stack enforces.

## Computational representation

```python
import re, sys

TOKEN = re.compile(r"[(),:;]|[^(),:;\s]+")

def parse_newick(text: str):
    """Unquoted Newick -> parent, name, length lists, nodes numbered in pre-order (0 = root)."""
    parent, name, length = [-1], [""], [None]
    def new_node(p):
        parent.append(p); name.append(""); length.append(None)
        return len(parent) - 1
    stack, current, after_colon = [], 0, False
    for tok in TOKEN.findall(text):
        if tok == "(":                          # current node gets children: remember it
            stack.append(current)
            current = new_node(current)
        elif tok == ",":                        # next sibling under the node on top
            current = new_node(stack[-1])       # IndexError if outside parentheses
        elif tok == ")":                        # back to the parent: what follows labels it
            current = stack.pop()               # IndexError if unbalanced
        elif tok == ":":
            after_colon = True
        elif tok == ";":
            break
        elif after_colon:
            length[current], after_colon = float(tok), False
        else:
            name[current] = tok
    if stack:
        raise ValueError("unclosed '('")
    return parent, name, length

def leaf_counts(parent):
    """Post-order result without recursion: scan the pre-order backwards, children before parents."""
    counts = [0] * len(parent)
    for v in range(len(parent) - 1, -1, -1):
        counts[v] = counts[v] or 1              # a node with no children is a leaf
        if parent[v] >= 0:
            counts[parent[v]] += counts[v]
    return counts

toy = parse_newick("((A:0.1,B:0.2)AB:0.3,C:0.4)root;")      # toy tree (invented)
print(toy, leaf_counts(toy[0]))
n = 5000                                        # caterpillar ((((L0,L1),L2),L3)...);
deep = "(" * (n - 1) + "L0" + "".join(f",L{i})" for i in range(1, n)) + ";"
parent = parse_newick(deep)[0]
print(sys.getrecursionlimit(), len(parent), "nodes,", leaf_counts(parent)[0], "leaves")
```

```text
([-1, 0, 1, 1, 0], ['root', 'AB', 'A', 'B', 'C'], [None, 0.3, 0.1, 0.2, 0.4]) [3, 2, 1, 1, 1]
1000 9999 nodes, 5000 leaves
```

The caterpillar nests 4,999 levels deep, five times the recursion limit: a recursive-descent parser (one call per nested node) would fail on it.

## Worked example

> [!example] Tracing `((A:0.1,B:0.2)AB:0.3,C:0.4)root;` (toy tree, invented; nodes numbered as created, 0 is the root)
> | Tokens | Effect | Stack after | Current |
> |---|---|---|---|
> | `(` `(` | push 0, create 1; push 1, create 2 | [0, 1] | 2 |
> | `A:0.1` `,` | label node 2; create sibling 3 under the top (1) | [0, 1] | 3 |
> | `B:0.2` `)` | label node 3; pop back to 1 | [0] | 1 |
> | `AB:0.3` `,` | label node 1; create sibling 4 under the top (0) | [0] | 4 |
> | `C:0.4` `)` | label node 4; pop back to 0 | [] | 0 |
> | `root` `;` | label node 0; the stack is empty, so the string is balanced | [] | 0 |
>
> Parents `[-1, 0, 1, 1, 0]`: the tree ((A, B)AB, C)root. The stack never holds more than the nesting depth, 2.

## Common misconceptions

> [!warning] "Counting brackets is enough"
> Only for a single bracket type. `([)]` has matching counts and never closes more than it opened, yet its pairs cross. A stack checks that each closer matches the most recent unclosed opener.

> [!warning] "A regular expression can validate a Newick string"
> Nesting is unbounded, and no finite automaton can track unbounded depth (Exercise 3). Use regular expressions for tokens, a stack for structure; and do not rely on recursion for deep trees, since each level costs a frame and CPython stops at its recursion limit.

## Exercises

> [!question] Exercise 1 (L1)
> Push A, B, C; pop; push D; pop; pop: what comes out, and what remains? Then, which of `(()[])`, `([)]`, `)(`, `((]` are balanced, and what is on the stack when each error is detected?

> [!success]- Solution
> Out: C, D, B; remaining: A. `(()[])` is balanced. `([)]`: at `)` the top is `[`, error with stack `([`. `)(`: at `)` the stack is empty. `((]`: at `]` the top is `(`, error with stack `((`.

> [!question] Exercise 2 (L2, Python)
> In a structure string, `(` and `)` mark paired positions and `.` unpaired ones. Return the 0-based base pairs of `((..((...))..))` (assume balanced input).

> [!success]- Solution
> ```python
> def base_pairs(structure: str) -> list[tuple[int, int]]:
>     stack, pairs = [], []
>     for i, ch in enumerate(structure):
>         if ch == "(":
>             stack.append(i)
>         elif ch == ")":
>             pairs.append((stack.pop(), i))       # pairs with the most recent open position
>     return sorted(pairs)
>
> print(base_pairs("((..((...))..))"))
> # [(0, 14), (1, 13), (4, 10), (5, 9)]
> ```
> Each `)` pairs with the most recent unpaired `(`, so the pairs are nested by construction: the stack cannot represent crossing pairs.

> [!question] Exercise 3 (L3)
> Prove that no deterministic finite automaton accepts exactly the balanced strings over `(` and `)`.

> [!success]- Solution
> Suppose a DFA with $q$ states does. Among the $q + 1$ prefixes $(^0, (^1, \dots, (^q$, two, say $(^i$ and $(^j$ with $i < j$, end in the same state (pigeonhole). The automaton accepts $(^i )^i$, so from that shared state it accepts $)^i$; hence it also accepts $(^j )^i$, which is unbalanced. Contradiction: recognizing nesting needs unbounded memory, which a stack provides.

## Mastery checklist

- [ ] 1 Recognized: I can define LIFO, push and pop, and give their cost in a Python `list`.
- [ ] 2 Understood: I can explain why bracket matching and Newick parsing need a stack, and how recursion uses the call stack.
- [ ] 3 Practiced: I can write an iterative Newick parser and an explicit-stack post-order traversal.
- [ ] 4 Applied: my [[08-phylogenetic-engine]] parser reads trees of tens of thousands of leaves without recursion.
- [ ] 5 Explained: I can teach the link between stacks, context-free languages and nested RNA structures, and its limit (crossing pairs).

## References

[^clrs10]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 10 "Elementary Data Structures": stacks and queues.
[^cardona]: [[Cardona 2008 - Extended Newick]], *BMC Bioinformatics* 9:532: Newick as the parenthesized format of phylogenetic trees, and its extension to networks.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 9 "Transformational grammars" (the Chomsky hierarchy of grammars and their automata) and ch. 10 "RNA structure analysis".
