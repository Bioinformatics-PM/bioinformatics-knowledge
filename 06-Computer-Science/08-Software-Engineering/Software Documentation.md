---
aliases:
  - Docstring
  - README
  - API Documentation
  - NumPy-Style Docstring
  - Documentation logicielle
tags:
  - type/concept
  - domain/computer-science
  - domain/scientific-practice
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Python Programming]]"
  - "[[Unit Testing]]"
  - "[[Defensive Programming]]"
related:
  - "[[Python Packaging]]"
  - "[[Software Release]]"
  - "[[Research Software]]"
  - "[[Static Analysis]]"
  - "[[Type Hint]]"
projects:
  - "[[Bioinformatics Lab]]"
  - "[[01-dna-engine]]"
sources:
  - "[[numpydoc Style Guide]]"
  - "[[Python Documentation]]"
  - "[[Wilson 2014 - Best Practices for Scientific Computing]]"
---

# Software Documentation

> [!abstract]
> Software documentation tells users how to call and run your code and tells readers why it is built the way it is; in Python it lives in docstrings next to the code, in a README at the root of the repository, and in reference pages generated from the docstrings.

## Definition

**Software documentation** is the text that explains what code does, how to use it and why it was designed that way. It has layers: **comments** explain a non-obvious line; **docstrings** (string literals at the start of a module, class or function, stored in `__doc__` and shown by `help()`) state the contract of an object;[^tutorial] the **README** presents the project; **API documentation** is generated from the docstrings. Wilson et al. recommend documenting design and purpose rather than mechanics: the code already shows *how*, the documentation must say *what for* and *why*.[^wilson14]

## Why it matters

- A function's contract is part of the science: which alphabet it accepts, whether lowercase counts, how `N` is handled, whether coordinates are 0- or 1-based. Without it, users guess, and wrong guesses produce plausible wrong results ([[Defensive Programming]]).
- The NumPy docstring format is specified by the NumPy project's numpydoc guide and rendered by its Sphinx extension;[^numpydoc] it is the format you meet when reading the reference pages of the scientific Python libraries, so your own library reads the same way.
- Every [[Bioinformatics Lab]] repository has a README with fixed sections, and a published tool is only reusable if someone else can install and call it ([[Research Software]], [[Software Release]]).

## Core (L1)

| Layer | Audience | Answers | Example |
|---|---|---|---|
| Comment | maintainer | why this line | `# reverse first: k-mers are read 5'->3' on the minus strand` |
| Docstring | caller | what it takes, returns, raises | `gc_content` below |
| README | newcomer | what the project is, how to install and run it | Lab sections below |
| API reference | user | every public object, generated | `pydoc`, Sphinx with numpydoc |
| Changelog | upgrader | what changed between versions | [[Software Release]] |

### A NumPy-style docstring

The first line is a one-line summary; the sections follow a fixed order: Parameters, Returns, Raises, See Also, Notes, Examples. Raises lists only non-obvious errors, Notes may hold the formula or algorithm, and Examples use the doctest format to illustrate usage.[^numpydoc] Toy `src/dna_engine/sequence.py`:

```python
"""Composition statistics of DNA sequences."""


def gc_content(seq: str) -> float:
    """
    Fraction of G and C among the unambiguous bases of a DNA sequence.

    Lowercase (soft-masked) bases are counted like uppercase ones. IUPAC
    ambiguity codes such as N are excluded from numerator and denominator.

    Parameters
    ----------
    seq : str
        DNA sequence over the IUPAC alphabet, in any case.

    Returns
    -------
    float
        GC fraction in [0, 1].

    Raises
    ------
    ValueError
        If `seq` contains no A, C, G or T, since the fraction is undefined.

    See Also
    --------
    gc_skew : (G - C) / (G + C), the strand-asymmetry statistic.

    Notes
    -----
    GC = (n_G + n_C) / (n_A + n_C + n_G + n_T), with n_X the count of base X.

    Examples
    --------
    >>> gc_content("ACGT")
    0.5
    >>> gc_content("acgtNN")
    0.5
    >>> round(gc_content("GGA"), 3)
    0.667
    """
    s = seq.upper()
    n = sum(s.count(b) for b in "ACGT")
    if n == 0:
        raise ValueError("GC content is undefined: no unambiguous base (A, C, G, T)")
    return (s.count("G") + s.count("C")) / n
```

Types are in the signature ([[Type Hint]]) and repeated in Parameters for readers of the rendered page; the docstring carries what types cannot: alphabet, case, ambiguity policy, range, and the undefined case.

### The README

Every repository of the [[Bioinformatics Lab]] uses the same sections, so a reader knows where to look:

```markdown
# 01-dna-engine
## Objective              what question the project answers, in two sentences
## Biological concepts    DNA, GC content, reverse complement (links)
## Technical concepts     value objects, validation, property-based tests
## Architecture           package layout, layers
## Algorithms             each algorithm with its complexity
## Usage                  install (uv sync) and run (uv run dna-engine gc seqs.fa)
## Examples               one copy-paste session with real output
## Benchmarks             what was measured, on which machine
## Tests                  how to run them, what they cover
## Limitations            what the tool does not do, and known biases
## What I learned
## Next step
```

## Deeper (L2)

**Examples that are tests.** The `doctest` module finds text that looks like interactive Python sessions in docstrings and checks that they run exactly as shown.[^doctest] `pytest --doctest-modules` runs them with the unit tests, so CI fails when documentation and code disagree ([[Unit Testing]]). Keep float examples robust (`round(..., 3)`), since doctest compares printed text.

```text
$ python -m doctest -v src/dna_engine/sequence.py | tail -3
3 tests in 3 items.
3 passed.
Test passed.
```

**Reference pages generated from code.** The standard library's `pydoc` generates documentation from modules, as console text, a local web server or HTML files (`python -m pydoc -w dna_engine.sequence` wrote `dna_engine.sequence.html`; `python -m pydoc dna_engine.sequence` prints the docstring above under `FUNCTIONS`, after the module summary line).[^pydoc] Sphinx, with the numpydoc extension, renders the same docstrings as a searchable website.[^numpydoc]

**Enforce it.** Ruff's pydocstyle rules (`select = ["D"]` with `convention = "numpy"` under `[tool.ruff.lint.pydocstyle]`) flag missing or malformed docstrings ([[Static Analysis]]). On the module above plus an undocumented `gc_skew`, it reported `D103 Missing docstring in public function` at `gc_skew`'s line.

**Document the science, not the syntax.** The comment `# loop over bases` is noise; `# N is excluded: an unknown base is not evidence of A or T` is the decision a reviewer must check. Coordinates, units, reference genome version, alphabet and random seeds belong in docstrings or the README, because they change results.

## Mathematical representation

Documentation is not mathematical; its one mathematical duty is to state each formula with every symbol defined, as the Notes section above does for GC content.

## Worked example

> [!example] The example that caught a wrong document
> 1. A first draft of the docstring above showed `>>> gc_content("GGC")` with the result `0.6666666666666666`, typed from memory.
> 2. `python -m doctest src/dna_engine/sequence.py` failed (real output, excerpt):
>
> ```text
> Failed example:
>     gc_content("GGC")
> Expected:
>     0.6666666666666666
> Got:
>     1.0
> ```
>
> `GGC` has three G or C out of three bases: the code was right and the documentation wrong.
> 3. Fix: `>>> round(gc_content("GGA"), 3)` giving `0.667`, which also avoids comparing 16 printed digits. Without executable examples, the wrong example would have shipped to every reader of the reference page.

## Common misconceptions

> [!warning] "Good code documents itself"
> Names and types show *how*; they cannot say that `N` is excluded, that coordinates are half-open, or why a threshold is 0.05. Those decisions need words.

> [!warning] "A docstring paraphrases the code"
> "Loops over the bases and counts G and C" adds nothing. State the contract (inputs, outputs, errors, conventions) and the purpose.

## Exercises

> [!question] Exercise 1 (L1)
> Where does each item belong (comment, docstring, README)? (a) "Coordinates are 0-based, half-open." (b) "Install with `uv sync`." (c) "We iterate from the end because the minus strand is read 3'->5' here." (d) "Raises ValueError if the sequence has no A, C, G or T."

> [!success]- Solution
> (a) Docstring of every function taking coordinates, and the README if the whole tool uses them. (b) README, Usage. (c) Comment, at that line: it explains a non-obvious choice. (d) Docstring, Raises section.

> [!question] Exercise 2 (L1)
> Write the summary line, Parameters and Returns of a NumPy-style docstring for `reverse_complement(seq: str) -> str` ([[Reverse Complement]]), which keeps case and IUPAC codes.

> [!success]- Solution
> Summary: `Reverse complement of a DNA sequence, read 5' to 3'.` Parameters: `seq : str`, `DNA sequence over the IUPAC alphabet; case is preserved base by base.` Returns: `str`, `The complementary strand, reversed; ambiguity codes are complemented (R <-> Y, N -> N).` An Examples section with `>>> reverse_complement("ACgt")` and `'acGT'` makes the case rule executable.

> [!question] Exercise 3 (L2, Python)
> With `ast`, list the public functions and classes of a module that have no docstring. Test it on the module above plus an undocumented `gc_skew`.

> [!success]- Solution
> ```python
> import ast
> from pathlib import Path
>
>
> def undocumented(path: Path) -> list[str]:
>     """Public functions and classes of a module that have no docstring."""
>     tree = ast.parse(path.read_text())
>     return [node.name for node in ast.walk(tree)
>             if isinstance(node, (ast.FunctionDef, ast.ClassDef))
>             and not node.name.startswith("_")
>             and ast.get_docstring(node) is None]
>
>
> print(undocumented(Path("src/dna_engine/sequence.py")))   # ['gc_skew']
> ```
>
> The leading underscore marks private names, which the check skips. Ruff's D rules do the same job, with many more checks.

## Mastery checklist

- [ ] 1 Recognized: I can name the layers of documentation and the sections of a NumPy-style docstring.
- [ ] 2 Understood: I can explain why documentation states purpose and conventions rather than mechanics.
- [ ] 3 Practiced: I can write a NumPy-style docstring with runnable examples and run them with doctest.
- [ ] 4 Applied: every Lab repository has the standard README, docstrings on all public functions checked by Ruff, and doctests in CI.
- [ ] 5 Explained: I can teach which scientific decisions must be documented and how to keep documentation from drifting.

## References

[^tutorial]: [[Python Documentation]], Tutorial, "Documentation Strings" (conventions for the first line and the blank second line), and the `__doc__` attribute read by `help()`.
[^wilson14]: [[Wilson 2014 - Best Practices for Scientific Computing]], "Document design and purpose, not mechanics".
[^numpydoc]: [[numpydoc Style Guide]]: section order and content (short summary, extended summary, Parameters, Returns, Raises, See Also, Notes, Examples in doctest format); numpydoc as the Sphinx extension that renders them.
[^doctest]: [[Python Documentation]], Library Reference, `doctest`: searches docstrings for text that looks like interactive sessions and executes it to verify it works exactly as shown.
[^pydoc]: [[Python Documentation]], Library Reference, `pydoc`: generates documentation from modules, shown as console text, served to a browser, or saved as HTML files.
