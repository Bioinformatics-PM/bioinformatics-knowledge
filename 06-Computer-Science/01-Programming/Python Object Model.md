---
aliases:
  - Python Data Model
  - Object Identity
  - Mutability
  - Boxed Number
  - Aliasing
  - Modèle objet de Python
tags:
  - type/concept
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Python Programming]]"
  - "[[Array]]"
related:
  - "[[Object-Oriented Programming]]"
  - "[[Functional Programming]]"
  - "[[N-Dimensional Array]]"
  - "[[Vectorization]]"
  - "[[Space Complexity]]"
  - "[[Hash Table]]"
  - "[[Memory Hierarchy]]"
  - "[[Floating-Point Arithmetic]]"
projects:
  - "[[bio-core]]"
  - "[[07-evolution-simulator]]"
sources:
  - "[[Python Documentation]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Python Object Model

> [!abstract]
> In Python every value is an object reached through a reference: names and containers hold references, assignment copies references and never objects, and each number in a list is a separate boxed object, which is why a list of a million floats takes four times the memory of a packed array and why looping over it is slow.

## Definition

In Python, all data is represented by **objects**. Every object has an **identity**, a **type** and a **value**. The identity never changes once the object exists (`is` compares identities, `id()` returns one; in CPython it is the memory address); the type fixes the operations the object supports; an object whose value can change is **mutable**, otherwise **immutable**. Containers (lists, tuples, dicts) hold **references** to other objects, so an immutable container can refer to mutable objects.[^datamodel] A **name** is bound to an object by assignment, and a function receives references to its arguments' objects ("call by object reference").[^tutorial][^mck2]

## Why it matters

- **Aliasing bugs.** Two names or two rows that share one list change together: a coverage matrix built with `[[0] * n] * m`, a mutable default argument, a shallow copy of nested records. These bugs corrupt results silently.
- **Hashing.** Only immutable values (strings, tuples, frozen dataclasses) can be dictionary keys: k-mers, `(chrom, pos)` pairs ([[Hash Table]], [[Object-Oriented Programming]]).
- **Memory.** A Python `list` of floats costs about 32 bytes per value against 8 in a packed array (measured below): the difference between fitting per-base coverage or a population state in RAM or not ([[Space Complexity]], [[07-evolution-simulator]]).
- **Speed.** Looping over boxed numbers runs the interpreter once per element; NumPy runs one compiled loop over raw doubles, the reason [[N-Dimensional Array|arrays]] and [[Vectorization]] exist.[^mck4]

## Core (L1)

![[python-names-references-boxed-floats.svg]]

1. **Assignment binds, it never copies.** After `b = a`, both names refer to one object; mutating it through `b` is visible through `a` (panel A).
2. **`==` compares values, `is` compares identities.** Use `is` only for singletons such as `None`. For immutable types, the interpreter may or may not reuse an existing object with the same value, so `is` on numbers or strings gives implementation-dependent answers.[^datamodel]
3. **Mutable versus immutable.** Mutable: `list`, `dict`, `set`, `bytearray`, most class instances. Immutable: `int`, `float`, `str`, `bytes`, `tuple`, `frozenset`, frozen dataclasses. A tuple holding a list is immutable as a tuple but its value still changes when the list does.[^datamodel]
4. **Augmented assignment** `x += y` works in place when the object supports it (lists) and rebinds the name otherwise (ints, strings, tuples).[^assign]
5. **Copies.** `list(a)`, `a[:]` and `copy.copy(a)` are **shallow**: a new container holding the same element objects. `copy.deepcopy` copies recursively.[^copy]
6. **Default arguments** are evaluated once, when the `def` runs, so a mutable default is shared by every call.[^funcdef]

```python
import copy

a = [0.5, 0.25]
b = a                          # a second name for the same list
c = list(a)                    # a new list holding the same float objects
b.append(0.125)
print(a, c, a is b, a is c, a[0] is c[0])
t = ("chr1", [100, 200])       # immutable tuple, mutable list inside
t[1].append(300)
print(t, copy.deepcopy(t)[1] is t[1])
x = 1000
y = x
y += 1                         # ints are immutable: += rebinds y
lst = a
lst += [1.0]                   # lists are mutable: += extends in place
print(x, y, a)
grid_bad = [[0] * 3] * 2       # two references to ONE row
grid_ok = [[0] * 3 for _ in range(2)]
grid_bad[0][0] = grid_ok[0][0] = 7
print(grid_bad, grid_ok)

def add_read(name, batch=[]):  # the default list is created once, at definition
    batch.append(name)
    return batch

print(add_read("r1"), add_read("r2"))
print(int("256") is int("256"), int("257") is int("257"))
```

```text
[0.5, 0.25, 0.125] [0.5, 0.25] True False True
('chr1', [100, 200, 300]) False
1000 1001 [0.5, 0.25, 0.125, 1.0]
[[7, 0, 0], [7, 0, 0]] [[7, 0, 0], [0, 0, 0]]
['r1', 'r2'] ['r1', 'r2']
True False
```

The last line is a CPython detail: integers from −5 to 256 are preallocated and shared, larger ones are created on demand.[^capi-long] Never rely on it.

## Deeper (L2)

**Boxed numbers.** In the default CPython build, every object starts with a header holding its **reference count** and a pointer to its **type object**.[^capi-obj] A `float` adds one C `double`,[^types] so `sys.getsizeof(1.0)` is 24 bytes on a 64-bit machine: 16 of header, 8 of value. A `list` stores an 8-byte pointer per element (plus spare capacity, see [[Array]]) and each pointer leads to a separate float object (panel B). `sys.getsizeof` reports only the object itself, not the objects it refers to, so measure whole structures with `tracemalloc`.[^sys][^tracemalloc]

**Why loops over a list are slow.** `sum(values)` executes interpreted bytecode per element: follow the pointer, check the type, add, allocate a new float for the running total. An `array('d')` stores raw doubles, which saves memory, but every access in Python **boxes** the value into a fresh float object (`packed[0] is packed[0]` is `False` below), so a Python loop over it is barely faster, if at all. NumPy's `sum` runs one loop in C over the contiguous doubles, with no objects created: about 25 times faster on this machine for the sum, 80 times for an element-wise product (measured below; timings vary with hardware, ratios are stable in order of magnitude).[^mck4] Contiguity also keeps the data in cache lines instead of scattered across the heap ([[Memory Hierarchy]]).

**Lifetime.** CPython frees an object when its reference count drops to zero, and a cyclic garbage collector reclaims reference cycles; other implementations may differ.[^datamodel] Deleting the last reference to a large list frees its floats immediately.

## Advanced (L3)

- **Per-record overhead.** For record types held by the million (variants, reads, intervals), the instance layout matters. Measured with CPython 3.13 for 100,000 four-field records (including the 8-byte list slot): plain class 112 B, `@dataclass(slots=True)` 72 B, tuple 80 B per record (Exercise 5). `__slots__` also forbids adding attributes not declared, which catches typos. Beyond tens of millions of records, switch from objects to columns: one array per field ([[Columnar Storage]], [[Data Frame]]).
- **Zero-copy views.** Slicing `bytes` copies; a `memoryview` accesses the buffer of a `bytes`, `bytearray` or `array` without copying.[^types] On an invented 10 Mb genome, the 8 Mb slice `genome[1_000_000:9_000_000]` allocated 8,000,033 bytes, `memoryview(genome)[1_000_000:9_000_000]` 312 bytes, for the same data. NumPy slices are views for the same reason ([[Array Indexing]]).
- **Processes copy.** Arguments sent to worker processes are pickled, that is, copied ([[Functional Programming]]); sharing large arrays between processes needs shared memory, not shared objects ([[Parallel Computing]]).
- **Free threading.** Python 3.13 ships an experimental build without the global interpreter lock (PEP 703), which changes how reference counts are maintained across threads.[^new]

## Mathematical representation

Let $n$ be the number of values, $p = 8$ bytes a pointer, $s_f = 24$ bytes a float object, $h_L$ and $h_A$ the fixed headers of a list and of an array, and $c(n) \ge n$ the list capacity. Then

$$M_{\text{list}}(n) = h_L + p\,c(n) + n\,s_f, \qquad M_{\text{array}}(n) = h_A + 8n,$$

and for large $n$ with $c(n) \approx n$, $M_{\text{list}} / M_{\text{array}} \to (8 + 24)/8 = 4$; the measurement gives $32.4 / 8.0 \approx 4.05$, the excess being spare capacity. If the elements are shared objects (cached small integers, repeated interned strings), the $n\,s_f$ term disappears and $M_{\text{list}}(n) \approx p\,c(n)$: about 8 bytes per element (Exercise 3).

## Computational representation

Measured with CPython 3.13.12 and NumPy 2.5.3 on one machine; `traced` reports the bytes still allocated by the structure.

```python
import random
import sys
import timeit
import tracemalloc
from array import array

import numpy as np

def traced(build):
    """Bytes allocated by build() and still held by its result (tracemalloc)."""
    tracemalloc.start()
    obj = build()
    held = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    return obj, held

print(sys.version.split()[0], np.__version__)
print(sys.getsizeof(1.0), sys.getsizeof([]), sys.getsizeof(array("d")), sys.getsizeof(np.empty(0)))
n = 1_000_000
rng = random.Random(0)
values, list_bytes = traced(lambda: [rng.random() for _ in range(n)])
packed, array_bytes = traced(lambda: array("d", values))
vec, numpy_bytes = traced(lambda: np.array(values))
print(f"bytes per value: list {list_bytes / n:.1f}, array {array_bytes / n:.1f}, numpy {numpy_bytes / n:.1f}")
print(values[0] is values[0], packed[0] is packed[0])

def best(stmt):
    return min(timeit.repeat(stmt, number=5, repeat=5)) / 5 * 1e3   # ms per call

print(f"sum: list {best(lambda: sum(values)):.2f} ms, array {best(lambda: sum(packed)):.2f} ms, numpy {best(lambda: vec.sum()):.2f} ms")
print(f"x*2: list {best(lambda: [v * 2 for v in values]):.2f} ms, numpy {best(lambda: vec * 2):.2f} ms")
```

```text
3.13.12 2.5.3
24 56 80 112
bytes per value: list 32.4, array 8.0, numpy 8.0
True False
sum: list 8.60 ms, array 6.91 ms, numpy 0.30 ms
x*2: list 48.12 ms, numpy 0.60 ms
```

## Worked example

> [!example] The coverage matrix that counts everything twice (invented data)
> A script tracks per-position coverage for 3 samples over 4 positions: `cov = [[0] * 4] * 3`, then `cov[0][2] += 1` for one read of sample 0.
> 1. **Symptom**: `cov` prints `[[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]`: every sample received the read.
> 2. **Diagnosis**: `[row] * 3` repeats the *reference*; `id(cov[0]) == id(cov[1])` is `True`, as in panel A where `a` and `b` share one list. The inner `[0] * 4` was harmless because ints are immutable: `+=` rebinds the slot instead of mutating the int.[^faq]
> 3. **Fix**: build each row separately, `cov = [[0] * 4 for _ in range(3)]`, or use a 2-D NumPy array `np.zeros((3, 4), dtype=np.uint32)`, which is also 4 bytes per cell instead of 8 ([[N-Dimensional Array]]).
> 4. **Test**: after one increment, `sum(map(sum, cov)) == 1`. A one-line invariant catches the bug ([[Unit Testing]]).

## Common misconceptions

> [!warning] "Python passes arguments by reference" (or "by value")
> Neither: the function receives a reference to the same object. Mutating it (`lst.append`) is visible to the caller; rebinding the parameter (`lst = []`) is not.[^tutorial]

> [!warning] "`is` is a faster `==`"
> `int("257") is int("257")` is `False` in CPython although the values are equal. `is` tests identity; use it for `None`, never for numbers or strings.[^datamodel]

> [!warning] "`array.array` makes Python loops fast"
> It cuts memory by four, but each element read in Python is boxed into a new float: `sum` over it took 6.9 ms against 8.6 ms for the list in the run above (a rerun gave equal times), and 0.30 ms with NumPy. Speed comes from loops that run in compiled code ([[Vectorization]]).

> [!warning] "A tuple can never change"
> The tuple's references cannot change; the objects they point to can (`('chr1', [100, 200, 300])` above). Such a tuple is not hashable either.

## Exercises

> [!question] Exercise 1 (L1)
> Predict the output: `x = [1, 2]; y = x; y = y + [3]; z = x; z += [4]; print(x, y)`.

> [!success]- Solution
> `[1, 2, 4] [1, 2, 3]`. `y + [3]` builds a new list and rebinds `y`; `z += [4]` extends in place the list that `x` also names.

> [!question] Exercise 2 (L1)
> Fix `def add_read(name, batch=[])` so that each call without `batch` starts a new list.

> [!success]- Solution
> Use `None` as the sentinel: `def add_read(name, batch=None): batch = [] if batch is None else batch; batch.append(name); return batch`. The default expression `None` is still evaluated once, but it is immutable.[^funcdef]

> [!question] Exercise 3 (L2, Python)
> Store a million Phred quality scores (integers 2 to 41) as a `list` and as `bytes` (Phred+33, [[FASTQ Format]]). Predict the bytes per score of each, then measure with `tracemalloc`.

> [!success]- Solution
> ```python
> import random, tracemalloc
>
> def traced(build):
>     tracemalloc.start()
>     obj = build()
>     held = tracemalloc.get_traced_memory()[0]
>     tracemalloc.stop()
>     return obj, held
>
> rng, n = random.Random(0), 1_000_000
> quals, list_bytes = traced(lambda: [rng.randrange(2, 42) for _ in range(n)])
> raw, raw_bytes = traced(lambda: bytes(q + 33 for q in quals))
> print(f"list of ints {list_bytes / n:.2f} B/score, bytes {raw_bytes / n:.2f} B/score")
> # list of ints 8.45 B/score, bytes 1.00 B/score
> ```
> Not 36 bytes per score but about 8: all values are small cached integers, so the list holds 8-byte pointers to shared objects and the $n\,s_f$ term vanishes (Mathematical representation). `bytes` stores one byte per score, as the FASTQ file does.

> [!question] Exercise 4 (L2)
> A per-base coverage track covers $2.5 \times 10^8$ positions (invented length), with depths below 60,000. Estimate the memory as a `list` of ints (most depths below 257) and as `array('H')`.

> [!success]- Solution
> List: about $8 \times 2.5 \times 10^8 = 2 \times 10^9$ bytes (2 GB) of pointers, more if many depths exceed 256 and need their own 28-byte int objects. `array('H')` (unsigned 16-bit, maximum 65,535): $2 \times 2.5 \times 10^8 = 5 \times 10^8$ bytes (0.5 GB), four times less, and NumPy `uint16` gives the same with fast arithmetic ([[Integer Representation]]).

> [!question] Exercise 5 (L3, Python)
> Measure the bytes per record of 100,000 variants `(chrom, pos, ref, alt)` stored as a plain class, a `@dataclass(slots=True)` and a tuple. Explain the ranking.

> [!success]- Solution
> ```python
> import random, tracemalloc
> from dataclasses import dataclass
>
> def traced(build):
>     tracemalloc.start()
>     obj = build()
>     held = tracemalloc.get_traced_memory()[0]
>     tracemalloc.stop()
>     return obj, held
>
> class Variant:
>     def __init__(self, chrom, pos, ref, alt):
>         self.chrom, self.pos, self.ref, self.alt = chrom, pos, ref, alt
>
> @dataclass(slots=True)
> class SlottedVariant:
>     chrom: str
>     pos: int
>     ref: str
>     alt: str
>
> m, rng = 100_000, random.Random(0)
> positions = [rng.randrange(1, 10**8) for _ in range(m)]   # built first: measure the records only
> makers = {"Variant": lambda p: Variant("chr1", p, "A", "G"),
>           "SlottedVariant": lambda p: SlottedVariant("chr1", p, "A", "G"),
>           "tuple": lambda p: ("chr1", p, "A", "G")}
> for name, make in makers.items():
>     _, held = traced(lambda: [make(p) for p in positions])
>     print(f"{name:15} {held / m:.1f} B/record")
> # Variant         112.0 B/record
> # SlottedVariant  72.0 B/record
> # tuple           80.0 B/record
> ```
> Each figure includes the 8-byte list slot; the strings and integers are shared, so only the records are counted. A slotted instance stores its four references in fixed slots after the header; a plain instance also carries the machinery for a per-instance attribute dictionary. These are CPython 3.13 figures: instance layouts changed in recent versions, so measure on your interpreter.

## Mastery checklist

- [ ] 1 Recognized: I can state identity, type and value, and list the mutable and immutable built-in types.
- [ ] 2 Understood: I can explain aliasing, shallow versus deep copies, augmented assignment and call by object reference.
- [ ] 3 Practiced: I can predict the output of aliasing puzzles and measure structures with `sys.getsizeof` and `tracemalloc`.
- [ ] 4 Applied: I sized the in-memory state of a Lab project ([[07-evolution-simulator]], [[bio-core]]) and chose objects, slots or arrays from the measurement.
- [ ] 5 Explained: I can explain boxing, why `array.array` saves memory but not time, and when to switch from objects to columns.

## References

[^datamodel]: [[Python Documentation]], 3.13, Language Reference, "Data model", section "Objects, values and types": identity, type, value, mutability, containers, CPython reference counting with delayed cycle detection, possible reuse of immutable objects.
[^tutorial]: [[Python Documentation]], 3.13, "The Python Tutorial", "Defining Functions": arguments are passed by value where the value is always an object reference ("call by object reference").
[^assign]: [[Python Documentation]], 3.13, Language Reference, "Simple statements", augmented assignment statements: in-place operation when possible.
[^funcdef]: [[Python Documentation]], 3.13, Language Reference, "Compound statements", function definitions: default parameter values are evaluated once, when the definition is executed.
[^copy]: [[Python Documentation]], 3.13, Library Reference, `copy`: shallow and deep copy.
[^faq]: [[Python Documentation]], 3.13, Programming FAQ, "How do I create a multidimensional list?".
[^capi-obj]: [[Python Documentation]], 3.13, Python/C API Reference, "Common Object Structures": `PyObject` holds the reference count and a pointer to the type object.
[^capi-long]: [[Python Documentation]], 3.13, Python/C API Reference, "Integer Objects": the current implementation keeps an array of integer objects for all integers between −5 and 256.
[^types]: [[Python Documentation]], 3.13, Library Reference, "Built-in Types": floats implemented as C doubles; memory views access an object's buffer without copying.
[^sys]: [[Python Documentation]], 3.13, Library Reference, `sys.getsizeof`: only the memory directly attributed to the object is counted.
[^tracemalloc]: [[Python Documentation]], 3.13, Library Reference, `tracemalloc`: tracing memory blocks allocated by Python.
[^new]: [[Python Documentation]], "What's New in Python 3.13": experimental free-threaded build (PEP 703).
[^mck2]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 2 "Python Language Basics, IPython, and Jupyter Notebooks": variables as references, argument passing, mutable and immutable objects.
[^mck4]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 4 "NumPy Basics: Arrays and Vectorized Computation": contiguous storage, lower memory use and faster array computation than Python lists.
