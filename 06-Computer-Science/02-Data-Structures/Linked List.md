---
aliases:
  - Singly Linked List
  - Doubly Linked List
  - Liste chaînée
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
  - "[[Python Object Model]]"
related:
  - "[[Queue]]"
  - "[[Hash Table]]"
  - "[[Memory Hierarchy]]"
  - "[[Tree (Data Structure)]]"
projects: []
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Linked List

> [!abstract]
> A linked list chains elements together with references instead of placing them side by side: inserting or removing at a node you already hold is $O(1)$, but reaching the $i$-th element means following $i$ references, and scattered nodes make it slower than an array for almost everything else.

## Definition

A **linked list** is a sequence whose elements are separate objects (**nodes**), each holding a value and a reference to the next node; the list keeps a reference to the first node, the **head**. In a **doubly linked** list each node also references its predecessor. A **circular** list with a **sentinel** (a dummy node between the tail and the head) removes every special case at the ends.[^clrs10] As an implementation of the sequence interface, a list inserts and deletes at the head in $O(1)$ but needs $O(i)$ to reach position $i$.[^6006-l2]

## Why it matters

- **Know when not to use it.** Random access, scans and memory all favor arrays. In Python the sensible defaults are `list` for a [[Stack]] and `collections.deque`, a double-ended queue optimized for insertion at both ends, for a [[Queue]].[^mck3]
- **The pattern is everywhere.** Hash tables with chaining keep a list per slot ([[Hash Table]]);[^clrs11] graphs are stored as adjacency lists ([[Graph Representation]]); a phylogeny or a taxonomy stored with parent pointers is a family of linked lists that merge toward the root ([[Tree (Data Structure)]]).
- **$O(1)$ removal through a handle** suits some bookkeeping: an LRU cache (a hash map from key to node, plus a doubly linked list ordered by recency), or the "active" intervals of a sweep along a chromosome, which leave in arbitrary order.

## Core (L1)

![[linked-list-singly-doubly.svg]]

| Operation | Singly linked (head) | Doubly linked, sentinel | Dynamic array |
|---|---|---|---|
| `get_at(i)` | $O(i)$ | $O(\min(i, n - i))$ | $O(1)$ |
| insert/delete at the front | $O(1)$ | $O(1)$ | $O(n)$ |
| insert/delete at the back | $O(n)$ | $O(1)$ | $O(1)$ amortized |
| insert after a held node | $O(1)$ | $O(1)$ | $O(n)$ |
| delete a held node | $O(n)$ (needs its predecessor) | $O(1)$ | $O(n)$ |

## Deeper (L2)

**Why arrays usually win**:
1. **The $O(1)$ needs a handle.** Inserting "at position $i$" first walks $i$ nodes, so it is $O(n)$ like the array's shift, and the array shifts one contiguous block.
2. **Memory.** In CPython, a node with `__slots__` takes 48 bytes (singly) or 56 bytes (doubly) according to `sys.getsizeof`, against 8 bytes per `list` slot, both pointing to the same value objects.
3. **Locality.** Hardware caches favor accesses to nearby addresses; for this reason the 4th edition of CLRS emphasizes linear probing for hash tables.[^clrs11] An array scan reads consecutive addresses. A list walk is a chain of dependent loads: the address of node $k + 1$ is known only once node $k$ has been read, and nodes can be anywhere in memory ([[Memory Hierarchy]]).

The last point shows even in Python. Summing $10^6$ values (`timeit`, best of 5, CPython 3.11; indicative) took 22.8 ms with `for x in xs` over a `list`, 61.5 ms along a linked list whose nodes were allocated and linked in order, and 208.8 ms along the same nodes linked in a shuffled order: identical instructions and the same $\Theta(n)$, yet 3.4 times slower, only because of where the nodes sit in memory.

**Where linked lists still win.** Inserting $m = 10^4$ and $10^5$ items at the front took 15.9 and 1558.8 ms with `list.insert(0, x)` (quadratic), 1.9 and 24.2 ms with a linked list (linear), and 0.3 and 4.1 ms with `deque.appendleft` (linear and faster still: in Python it is the answer). Hand-written linked lists earn their place when you need $O(1)$ splicing or removal through handles.

## Advanced (L3)

- **Persistence and shared tails.** An immutable singly linked list grows at the front without copying: the new node `(x, rest)` shares `rest`. A tree stored with parent pointers is exactly a family of such lists: each node's lineage (its path to the root) is one list, and siblings share everything above them, so lineages cost one node per tree node instead of the sum of all path lengths (Exercise 3) ([[Functional Programming]], [[Phylogenetic Tree]]). The same constant-space pointer style reverses a list (Worked example) or detects a cycle (Exercise 2).

## Mathematical representation

- Nodes $N$ with $\mathrm{next} : N \to N \cup \{\mathrm{nil}\}$. The list from head $h$ is $h, \mathrm{next}(h), \mathrm{next}^2(h), \dots$, well formed if $\mathrm{next}^n(h) = \mathrm{nil}$ for some $n$ (the smallest is its length); $\mathrm{get\_at}(i) = \mathrm{next}^i(h)$ costs exactly $i$ dereferences.
- Doubly linked invariant: $\mathrm{prev}(\mathrm{next}(x)) = x$ and $\mathrm{next}(\mathrm{prev}(x)) = x$ for every node $x$, sentinel included. Removing $x$ sets $\mathrm{next}(\mathrm{prev}(x)) \leftarrow \mathrm{next}(x)$ and $\mathrm{prev}(\mathrm{next}(x)) \leftarrow \mathrm{prev}(x)$, which restores the invariant on the remaining nodes.

## Computational representation

```python
class Node:
    __slots__ = ("value", "next")
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def values(head):                               # O(n) walk
    while head is not None:
        yield head.value
        head = head.next

def reverse(head):                              # O(n) time, O(1) extra space
    prev = None
    while head is not None:
        head.next, prev, head = prev, head, head.next
    return prev

class DNode:
    __slots__ = ("value", "prev", "next")
    def __init__(self, value=None):
        self.value, self.prev, self.next = value, self, self

class DoublyLinkedList:                         # circular, with a sentinel: no special cases
    def __init__(self):
        self.nil = DNode()
    def insert_after(self, node, value):        # O(1) given the node
        new = DNode(value)
        new.prev, new.next = node, node.next
        node.next.prev = new
        node.next = new
        return new
    def remove(self, node):                     # O(1) given the node
        node.prev.next, node.next.prev = node.next, node.prev
    def __iter__(self):
        node = self.nil.next
        while node is not self.nil:
            yield node.value
            node = node.next

head = Node("N", Node("A", Node("C", Node("G", Node("T")))))   # built by pushes at the front
print(list(values(head)), list(values(reverse(head))))
d = DoublyLinkedList()
handles = [d.insert_after(d.nil.prev, name) for name in ("read1", "read2", "read3")]
d.remove(handles[1])                            # no search
print(list(d))
```

```text
['N', 'A', 'C', 'G', 'T'] ['T', 'G', 'C', 'A', 'N']
['read1', 'read3']
```

## Worked example

> [!example] Reversing `A → C → G` in place
> Invariant: the list from `prev`, reversed, followed by the list from `head`, equals the original sequence.
>
> | Step | `prev` heads | `head` heads | reverse(prev list) + head list |
> |---|---|---|---|
> | start | (empty) | A → C → G | A C G |
> | 1 | A | C → G | A + C G |
> | 2 | C → A | G | A C + G |
> | 3 | G → C → A | (empty) | A C G |
>
> Each step redirects one reference and advances both pointers: $n$ steps, no new node. At the end `head` is empty, so `prev` heads the reversed list. The tuple assignment `head.next, prev, head = prev, head, head.next` evaluates its right side first, so the old `head.next` is not lost.

## Common misconceptions

> [!warning] "Insertion into a linked list is O(1)"
> Only next to a node you already hold. Finding position $i$ costs $O(i)$, so "insert in the middle" is $O(n)$, as for an array.

> [!warning] "Linked lists save memory because they never over-allocate"
> Per-node overhead dominates: 48 to 56 bytes per node in CPython versus 8 bytes per `list` slot plus a modest growth slack ([[Array]]).

## Exercises

> [!question] Exercise 1 (L1)
> In a doubly linked list, write the reference updates that insert a new node `x` after node `p`. How many references change? Why can a singly linked list not delete a node it holds in $O(1)$?

> [!success]- Solution
> `x.prev = p; x.next = p.next; p.next.prev = x; p.next = x`: four assignments, two of them in existing nodes, in this order (`p.next` must be read before it is overwritten). Deleting node `q` from a singly linked list requires updating its predecessor's `next`, and the predecessor can only be found by walking from the head: $O(n)$.

> [!question] Exercise 2 (L2, Python)
> Detect whether a singly linked list contains a cycle in $O(n)$ time and $O(1)$ extra space with two pointers, one moving twice as fast. Argue why they meet.

> [!success]- Solution
> ```python
> def has_cycle(head):
>     slow = fast = head
>     while fast is not None and fast.next is not None:
>         slow, fast = slow.next, fast.next.next
>         if slow is fast:
>             return True
>     return False
>
> h = Node(0, Node(1, Node(2, Node(3))))
> print(has_cycle(h), end=" ")
> h.next.next.next.next = h.next                  # last node -> second node
> print(has_cycle(h))
> # False True
> ```
> Without a cycle, `fast` reaches `None`. With a cycle of length $\lambda$, once both pointers are on it the gap between them shrinks by one node per step modulo $\lambda$, so they meet within $\lambda$ steps after `slow` enters: $O(n)$ in total.

> [!question] Exercise 3 (L3)
> A complete binary tree of height $h$ has $2^h$ leaves. Compare the node entries needed to store every root-to-leaf lineage explicitly with the number needed when lineages share tails (parent pointers). Evaluate for $h = 20$.

> [!success]- Solution
> Explicit: each of the $2^h$ lineages has $h + 1$ nodes, so $2^h (h + 1)$ entries. Shared: one node per tree node, $2^{h+1} - 1$. For $h = 20$: $22{,}020{,}096$ versus $2{,}097{,}151$, a factor of 10.5 that grows like $h/2$. Trees stored with parent pointers get this sharing for free.

## Mastery checklist

- [ ] 1 Recognized: I can draw singly and doubly linked lists and give the cost of `get_at`, front insertion and deletion through a handle.
- [ ] 2 Understood: I can explain why arrays usually beat linked lists (handles, memory overhead, locality).
- [ ] 3 Practiced: I can implement both lists with a sentinel, reverse in place and detect cycles.
- [ ] 4 Applied: I measured a linked structure against `list` and `deque` on a real workload and chose with the numbers.
- [ ] 5 Explained: I can teach when linked structures are the right tool (handles, splicing, shared tails) and when they are not.

## References

[^clrs10]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 10 "Elementary Data Structures": singly and doubly linked lists, sentinels.
[^clrs11]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 11 "Hash Tables": chaining with linked lists; linear probing presented as efficient when the hardware's caching favors local accesses.
[^6006-l2]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 2 "Data Structures": linked lists as a sequence implementation.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": `collections.deque` for insertion at both ends.
