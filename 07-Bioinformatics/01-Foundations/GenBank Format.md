---
aliases:
  - GenBank Flat File
  - GenBank Record
  - Flat File Format
  - Feature Table
  - Format GenBank
tags:
  - type/concept
  - domain/bioinformatics
  - domain/biology
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[FASTA Format]]"
  - "[[Accession Number]]"
  - "[[Gene]]"
  - "[[Genetic Code]]"
  - "[[Reverse Complement]]"
related:
  - "[[Gene Annotation]]"
  - "[[GFF Format]]"
  - "[[Open Reading Frame]]"
  - "[[Codon]]"
  - "[[Messenger RNA]]"
  - "[[Genomic Coordinate System]]"
  - "[[Genomic Interval Arithmetic]]"
  - "[[Biological Database]]"
  - "[[State Machine]]"
projects:
  - "[[02-sequence-translation]]"
  - "[[bio-core]]"
  - "[[01-dna-engine]]"
sources:
  - "[[NCBI GenBank]]"
  - "[[INSDC Feature Table Definition]]"
  - "[[NCBI Genetic Codes]]"
  - "[[Biopython]]"
---

# GenBank Format

> [!abstract]
> A GenBank record is a text file that tells the whole story of a sequence: who it comes from, how to cite it, where its genes, exons and coding sequences lie (the feature table), and finally the sequence itself.

## Definition

The **GenBank flat file** is the text format in which NCBI distributes GenBank records. A record is a header of keyword lines (`LOCUS`, `DEFINITION`, `ACCESSION`, `VERSION`, `SOURCE`, `REFERENCE`...), a `FEATURES` table, the sequence after `ORIGIN`, and a terminating `//`; its structure is specified in the GenBank release notes.[^gbrel] The feature table follows the **INSDC Feature Table Definition** shared by DDBJ, ENA and GenBank, in which every feature is a **feature key** (what it is), a **location** (where it is on the sequence) and **qualifiers** (what else is known).[^ft]

## Why it matters

- **Annotation in one file.** Reading a GenBank record (organism, references, feature table, sequence) is the fastest way to see what a [[Gene Annotation]] looks like in practice.[^genbank] Unlike [[FASTA Format]], the record says where the genes and coding sequences are.
- **Checkable biology.** A `CDS` feature carries its own `/translation`; recomputing it from the location and the [[Genetic Code]] is the core exercise of [[02-sequence-translation]], and a test of every piece of the pipeline: coordinates, strands, splicing, reading frame and translation table.[^genbank]
- **A shared model.** The same feature table is used by the three INSDC partners,[^ft] and its ideas (typed features, intervals on a strand, key-value attributes) reappear in [[GFF Format]] and in the typed feature objects of [[bio-core]].

## Core (L1)

### Anatomy of a record

An invented record of 100 bp with two genes, one spliced on the `+` strand and one on the `-` strand, laid out like a real flat file:

```text
LOCUS       XX000100                 100 bp    DNA     linear   SYN 30-SEP-2026
DEFINITION  Toy organism toyA and toyB genes, complete cds (invented record).
ACCESSION   XX000100
VERSION     XX000100.1
KEYWORDS    .
SOURCE      Toy organism
  ORGANISM  Toy organism
            Eukaryota; Toy lineage.
FEATURES             Location/Qualifiers
     source          1..100
                     /organism="Toy organism"
                     /mol_type="genomic DNA"
     gene            5..45
                     /gene="toyA"
     exon            5..19
                     /gene="toyA"
                     /number=1
     CDS             join(5..19,31..45)
                     /gene="toyA"
                     /codon_start=1
                     /transl_table=1
                     /product="toy protein A, with a product name long enough to
                     continue on a second line"
                     /translation="MAKEVLGRW"
     exon            31..45
                     /gene="toyA"
                     /number=2
     gene            complement(60..83)
                     /gene="toyB"
     CDS             complement(60..83)
                     /gene="toyB"
                     /codon_start=1
                     /product="toy protein B"
                     /translation="MSHKRDF"
ORIGIN
        1 cgatatggct aaagaagttg taagtttcag ctgggccgtt ggtaaccgat tacggatccc
       61 taaaaatcac gtttgtgaga catggcatta cgctagcatg
//
```

| Line | Content |
|---|---|
| `LOCUS` | locus name, sequence length, molecule type, GenBank division and modification date[^sample] |
| `DEFINITION` | one-line description of the record |
| `ACCESSION`, `VERSION` | the [[Accession Number]] and accession.version |
| `SOURCE`, `ORGANISM` | organism name, then its taxonomic lineage |
| `REFERENCE` | citations (none in this toy) |
| `FEATURES` | the feature table: one block per feature |
| `ORIGIN` ... `//` | the sequence, 60 bases per line in blocks of 10, each line starting with the position of its first base; `//` ends the record |

**Layout.** Header keywords start in column 1 and their values in column 13, with sub-keywords such as `ORGANISM` indented; in the feature table, keys start in column 6 and locations and qualifiers in column 22, as in NCBI's annotated sample record.[^sample][^gbrel] A parser can therefore decide what a line is from its columns.

### Features, locations and qualifiers

Feature keys in the toy: `source` (the whole sequence and its organism), `gene`, `exon` and `CDS` (the coding sequence, whose location includes the stop codon).[^ft] Each qualifier is `/name=value`:[^ft]

| Qualifier | Meaning |
|---|---|
| `/gene` | gene symbol, linking `gene`, `exon` and `CDS` features |
| `/product` | name of the product, here the protein |
| `/codon_start` | offset (1, 2 or 3) of the first complete codon within the feature |
| `/transl_table` | NCBI genetic code table used for translation ([[Genetic Code]])[^gc] |
| `/translation` | amino acid sequence of the CDS, one-letter codes, without the stop |
| `/number` | order of an exon (or intron) along the gene |

Locations use 1-based positions with both ends included:[^ft]

![[genbank-feature-locations.svg]]

- `5..19`: bases 5 to 19 of the record's sequence (15 bases).
- `join(5..19,31..45)`: the pieces placed end to end, in the order written: the two exons of the CDS, intron removed.
- `complement(60..83)`: the feature lies on the other strand; its sequence is the [[Reverse Complement|reverse complement]] of bases 60 to 83.
- `<1..30` or `100..>150`: the feature extends beyond the first or last base given (a **partial** feature).

## Deeper (L2)

### Reading a CDS from a record

1. **Extract**: follow the location, slicing each segment (1-based, inclusive: Python `seq[a-1:b]`), reverse-complementing segments on the `-` strand, and concatenating in reading order.
2. **Frame**: start at `/codon_start` (default 1); a CDS that is partial at its 5' end may start its first complete codon at base 2 or 3.
3. **Table**: translate with `/transl_table` (default: the standard code, table 1); a mitochondrial or bacterial CDS needs its own table.[^gc]
4. **Compare** with `/translation` (which omits the stop codon).[^ft] A mismatch means a bug in steps 1 to 3, or a sequence that changed (check the `VERSION`).

### Location algebra

- `complement(join(A,B))` reads `rc(B) + rc(A)`: complementing reverses the order of the pieces as well as each piece (because $\mathrm{rc}(uv) = \mathrm{rc}(v)\,\mathrm{rc}(u)$, see [[DNA#Mathematical representation]]). It is equivalent to `join(complement(B),complement(A))`.
- The `gene` span (`5..45`) includes the intron; only the `CDS` (or `mRNA`) location lists the exons. Using the gene span as a coding sequence is a classic error.
- The Feature Table Definition also defines single-base locations, sites between two bases and other operators; a parser should reject what it does not implement rather than guess.[^ft]

### Pitfalls checklist

| Pitfall | Consequence | Fix |
|---|---|---|
| 1-based inclusive read as 0-based half-open | every feature shifted by one base | slice `seq[a-1:b]` ([[Genomic Coordinate System]]) |
| `complement()` ignored, or pieces not reversed | nonsense protein for `-` strand genes | recurse: reverse the segment list, flip strands |
| Gene span used as CDS | intron translated | extract from the `CDS` location |
| `/codon_start` or `/transl_table` ignored | frameshifted or wrong protein | read both, with defaults 1 and table 1 |
| Qualifier values over several lines | truncated products and translations | join continuation lines; no spaces inside `/translation` |
| A continuation line that starts with `/` inside an open quote | spurious qualifier | track open quotes |
| One value per qualifier assumed | repeated qualifiers overwritten | store a list per qualifier name |
| Long `join(...)` wrapped over several lines | unparsable location | append continuation lines before parsing |
| Lowercase sequence, digits and spaces in `ORIGIN` | wrong lengths and counts | keep letters only, normalize case |
| One record per file assumed | only the first record read | stream records up to each `//` |

## Advanced (L3)

- **One model, several layouts.** ENA and DDBJ carry the same feature table in their own flat files; the EMBL-style layout prefixes feature lines with `FT` and starts feature keys in column 6.[^ft] A parser should separate the **layout** (columns, line prefixes) from the **model** (features, locations, qualifiers), so that only the first changes between formats. [[GFF Format]] expresses a similar model as tab-separated rows with parent-child links.
- **Features are intervals.** A location is a list of oriented intervals, so overlaps, exon unions or intron sets are interval operations ([[Genomic Interval Arithmetic]]), and mapping a CDS position to a genome position (for variants) is a walk along the segments (Exercise 3).
- **A living specification.** The Feature Table Definition is versioned (11.3 in October 2024);[^ft] parsers should keep unknown keys and qualifiers instead of failing, record the version they were tested against, and can compare their output with `Bio.SeqIO` from [[Biopython]] in tests.[^biopython]
- **Archive annotations vary.** GenBank records reflect what submitters provided, so annotation quality varies;[^genbank] checking every `/translation` against the sequence is a cheap, systematic quality test (Exercise 4).

## Mathematical representation

A record is a triple $(H, F, s)$: header fields $H$, features $F$, sequence $s \in \Sigma^n$. A feature is $f = (k, \lambda, Q)$ with key $k$, qualifiers $Q$ (a multimap from names to values) and location

$$\lambda = \big((a_1, b_1, \sigma_1), \dots, (a_m, b_m, \sigma_m)\big), \qquad 1 \le a_j \le b_j \le n,\ \sigma_j \in \{+1, -1\},$$

listed in reading order. Its sequence is the concatenation $x(\lambda) = x_1 x_2 \cdots x_m$ with $x_j = s[a_j..b_j]$ if $\sigma_j = +1$ and $x_j = \mathrm{rc}(s[a_j..b_j])$ otherwise. Complementing a location reverses the list and flips every strand, and $x(\mathrm{complement}(\lambda)) = \mathrm{rc}(x(\lambda))$.

For a complete CDS, $\ell = \sum_j (b_j - a_j + 1) \equiv 0 \pmod 3$, and translating $x(\lambda)$ from offset $\texttt{codon\_start} - 1$ with table $\texttt{transl\_table}$ gives `/translation` followed by a stop.

**Position mapping.** With cumulative lengths $L_0 = 0$, $L_j = \sum_{i \le j} (b_i - a_i + 1)$, CDS position $c$ (1-based) lies in the segment $j$ with $L_{j-1} < c \le L_j$, and maps to the record position

$$p(c) = \begin{cases} a_j + (c - L_{j-1} - 1) & \sigma_j = +1 \\ b_j - (c - L_{j-1} - 1) & \sigma_j = -1. \end{cases}$$

## Computational representation

A streaming parser (records up to each `//`, columns as in the layout above), a location parser for ranges, `join`, `complement` and partial ends, and the CDS check, standard library only. Save the record of Core (L1) as `toy.gb` first.

```python
from collections import defaultdict
from itertools import product
from typing import Iterator, TextIO


def _finish_qualifiers(raw: list[list[str]]) -> dict[str, list[str]]:
    """['/gene="toyA"'] -> {'gene': ['toyA']}; values are lists because a qualifier may repeat."""
    out = defaultdict(list)
    for fragments in raw:
        key, _, first = fragments[0][1:].partition("=")
        sep = "" if key == "translation" else " "          # protein text wraps without spaces
        value = sep.join([first, *fragments[1:]])
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1]
        out[key].append(value)                              # flag qualifiers get ""
    return dict(out)


def read_genbank(handle: TextIO) -> Iterator[dict]:
    """Stream GenBank flat-file records (terminated by '//') as dictionaries."""
    rec, section, last_key = None, None, None
    for line in handle:
        line = line.rstrip("\r\n")
        if line.startswith("//"):                           # end of record
            for f in rec["features"]:
                f["qualifiers"] = _finish_qualifiers(f["qualifiers"])
            rec["sequence"] = "".join(rec["sequence"]).upper()
            yield rec
            rec, section = None, None
            continue
        if rec is None:
            if not line.strip():
                continue
            rec = {"header": {}, "features": [], "sequence": []}
        if line[:1].strip():                                # keyword in column 1 opens a section
            section = line[:12].strip()
            if section not in ("FEATURES", "ORIGIN"):
                rec["header"][section] = line[12:].strip()
                last_key = section
        elif section == "FEATURES":
            key, text = line[5:21].strip(), line[21:].strip()
            if key:                                         # feature key in columns 6-20
                rec["features"].append({"key": key, "location": text, "qualifiers": []})
                continue
            quals = rec["features"][-1]["qualifiers"]
            open_quote = bool(quals) and "".join(quals[-1]).count('"') % 2 == 1
            if text.startswith("/") and not open_quote:     # new qualifier
                quals.append([text])
            elif quals:                                     # continuation of a qualifier value
                quals[-1].append(text)
            else:                                           # continuation of a long location
                rec["features"][-1]["location"] += text
        elif section == "ORIGIN":
            rec["sequence"].append("".join(c for c in line if c.isalpha()))
        else:                                               # sub-keyword (col 3) or continuation
            sub = line[:12].strip()
            if sub:
                last_key = f"{section}.{sub}"
                rec["header"][last_key] = line[12:].strip()
            else:
                rec["header"][last_key] += " " + line[12:].strip()


COMPLEMENT = str.maketrans("ACGTN", "TGCAN")
STANDARD = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"   # NCBI table 1
CODON = {"".join(c): aa for c, aa in zip(product("TCAG", repeat=3), STANDARD)}


def split_top_level(text: str) -> list[str]:
    """Split on commas that are not inside parentheses."""
    parts, depth, start = [], 0, 0
    for i, ch in enumerate(text):
        depth += (ch == "(") - (ch == ")")
        if ch == "," and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    return parts + [text[start:]]


def parse_location(loc: str) -> list[tuple[int, int, int]]:
    """Location string -> ordered segments (start, end, strand), 1-based inclusive, in reading order."""
    loc = loc.replace(" ", "")
    if loc.startswith("complement(") and loc.endswith(")"):
        return [(s, e, -strand) for s, e, strand in reversed(parse_location(loc[11:-1]))]
    if loc.startswith("join(") and loc.endswith(")"):
        inner = loc[5:-1]
        return [seg for part in split_top_level(inner) for seg in parse_location(part)]
    first, _, last = loc.partition("..")
    start, end = int(first.lstrip("<")), int((last or first).lstrip(">"))   # '<' / '>' mark partial ends
    return [(start, end, 1)]


def extract(sequence: str, loc: str) -> str:
    """Feature sequence read 5'->3' on its own strand."""
    out = []
    for s, e, strand in parse_location(loc):
        piece = sequence[s - 1:e]
        out.append(piece if strand == 1 else piece.translate(COMPLEMENT)[::-1])
    return "".join(out)


def translate(cds: str, codon_start: int = 1) -> str:
    """Translate from the /codon_start offset; unknown codons give X; a final stop is dropped."""
    protein = "".join(CODON.get(cds[i:i + 3], "X") for i in range(codon_start - 1, len(cds) - 2, 3))
    return protein[:-1] if protein.endswith("*") else protein


with open("toy.gb") as handle:                              # the record of Core (L1), saved to a file
    for record in read_genbank(handle):
        print(record["header"]["VERSION"], record["header"]["SOURCE.ORGANISM"], len(record["sequence"]), "bp")
        for f in (f for f in record["features"] if f["key"] == "CDS"):
            q = f["qualifiers"]
            cds = extract(record["sequence"], f["location"])
            mine = translate(cds, int(q.get("codon_start", ["1"])[0]))
            print(f"  {q['gene'][0]} {parse_location(f['location'])}: {cds} -> {mine}, matches: {mine == q['translation'][0]}")
```

```text
XX000100.1 Toy organism Eukaryota; Toy lineage. 100 bp
  toyA [(5, 19, 1), (31, 45, 1)]: ATGGCTAAAGAAGTTCTGGGCCGTTGGTAA -> MAKEVLGRW, matches: True
  toyB [(60, 83, -1)]: ATGTCTCACAAACGTGATTTTTAG -> MSHKRDF, matches: True
```

Both coding sequences reproduce their annotated `/translation`. The parser keeps qualifier values as lists, joins `/translation` lines without spaces and other values with one space, and raises on location syntax it does not implement (a `ValueError` from `int()`), instead of guessing.

## Worked example

> [!example] The minus-strand gene of the toy record
> Feature: `CDS complement(60..83)`, `/codon_start=1`, `/translation="MSHKRDF"`.
> 1. **Slice** positions 60 to 83 (24 bases) from the `ORIGIN` lines: line 1 ends at 60 with `c`, line 2 gives the rest: `CTAAAAATCACGTTTGTGAGACAT`.
> 2. **Reverse complement**: `ATGTCTCACAAACGTGATTTTTAG`, which now reads 5' → 3' on the gene's strand and starts with `ATG`.
> 3. **Codons** from offset 0: `ATG TCT CAC AAA CGT GAT TTT TAG` → M S H K R D F stop.
> 4. **Compare**: `MSHKRDF` = `/translation`; the stop codon `TAG` is inside the location (60..62 on the `+` strand, read backwards) but not in the translation.
> 5. **Coordinates**: the start codon is at 81..83 on the record, not at 60: on the `-` strand the gene begins at the higher coordinate.

## Common misconceptions

> [!warning] "A feature's location is one start and one end"
> A location can be a `join` of several segments and can sit on the complementary strand.[^ft] Storing only (start, end) loses the exon structure and the strand.

> [!warning] "`complement(60..83)` means read bases 60 to 83 and complement them"
> It means the reverse complement: complement each base **and** reverse the order, so that the result reads 5' → 3' on the feature's strand.

> [!warning] "The /translation is the ground truth"
> It is the translation of the annotated CDS with the stated table,[^ft] provided by the submitter or computed at submission; records in an archive reflect what submitters provided.[^genbank] Recompute it: agreement is a test, not an assumption.

## Exercises

> [!question] Exercise 1 (L1)
> In the toy record, give: the record's accession and version, its length, the organism, the number of genes, and the strand and length of each CDS.

> [!success]- Solution
> `XX000100`, version 1 (`XX000100.1`); 100 bp; "Toy organism"; two genes, `toyA` and `toyB`. The toyA CDS is on the `+` strand, 15 + 15 = 30 nt (9 amino acids and a stop); the toyB CDS is on the `-` strand (`complement`), 24 nt (7 amino acids and a stop).

> [!question] Exercise 2 (L1)
> NCBI's annotated sample record `U49845` is described as "*Saccharomyces cerevisiae* TCP1-beta gene, partial cds, and Axl2p (AXL2) and Rev7p (REV7) genes, complete cds".[^sample] Before opening it, predict what marks the partial CDS in its location, and which qualifier you must read before translating it. Then open the record and check.

> [!success]- Solution
> A partial feature has `<` before its first position or `>` before its last,[^ft] and a CDS that is partial at its 5' end may not start with a complete codon, so `/codon_start` (1, 2 or 3) says where the first complete codon begins. The two complete CDS need neither mark.

> [!question] Exercise 3 (L2, Python)
> Using `parse_location`, write `cds_to_genome(loc, c)` that maps a 1-based CDS position to a record position, and test it on `join(5..19,31..45)` (positions 1, 15, 16, 30), `complement(60..83)` (1, 24) and `complement(join(1..10,20..30))` (1, 11, 12, 21).

> [!success]- Solution
> ```python
> def cds_to_genome(loc: str, c: int) -> int:
>     """1-based CDS position c -> 1-based position on the record's sequence."""
>     for s, e, strand in parse_location(loc):
>         length = e - s + 1
>         if c <= length:
>             return s + c - 1 if strand == 1 else e - c + 1
>         c -= length
>     raise ValueError("position beyond the end of the feature")
>
>
> print([cds_to_genome("join(5..19,31..45)", c) for c in (1, 15, 16, 30)])
> print([cds_to_genome("complement(60..83)", c) for c in (1, 24)])
> print([cds_to_genome("complement(join(1..10,20..30))", c) for c in (1, 11, 12, 21)])
> ```
> Output: `[5, 19, 31, 45]`, `[83, 60]`, `[30, 20, 10, 1]`. CDS position 16 jumps over the intron to 31; on the `-` strand the first CDS base is the highest coordinate. This is the mapping a variant annotator needs to turn a genome position into a codon ([[Variant Annotation]]).

> [!question] Exercise 4 (L3, Python)
> Build a two-record file from `toy.gb` and a copy (`XX000101`) in which base 7 is changed from G to A. Stream both records through `read_genbank` and report every CDS whose recomputed translation disagrees with `/translation`, refusing translation tables you have not implemented.

> [!success]- Solution
> ```python
> import io
>
> text = open("toy.gb").read()
> mutant = text.replace("XX000100", "XX000101").replace("cgatatggct", "cgatatagct")   # base 7: G -> A
>
>
> def check_cds(handle) -> list[tuple[str, str, str, str]]:
>     """(version, gene, own translation, annotated translation) for every mismatching CDS."""
>     problems = []
>     for record in read_genbank(handle):
>         for f in record["features"]:
>             if f["key"] != "CDS":
>                 continue
>             q = f["qualifiers"]
>             table = q.get("transl_table", ["1"])[0]
>             if table != "1":
>                 raise NotImplementedError(f"translation table {table}")
>             mine = translate(extract(record["sequence"], f["location"]), int(q.get("codon_start", ["1"])[0]))
>             if mine != q["translation"][0]:
>                 problems.append((record["header"]["VERSION"], q["gene"][0], mine, q["translation"][0]))
>     return problems
>
>
> print(check_cds(io.StringIO(text + mutant)))
> ```
> Output: `[('XX000101.1', 'toyA', 'IAKEVLGRW', 'MAKEVLGRW')]`. Base 7 is the third base of the start codon (5..7): `ATG` became `ATA`, isoleucine. The check runs in one pass and constant memory per record, so it scales to whole-genome files; refusing unknown tables avoids reporting false mismatches for mitochondrial genes.[^gc]

## Mastery checklist

- [ ] 1 Recognized: I can name the sections of a GenBank record and find its accession, organism, features and sequence.
- [ ] 2 Understood: I can read feature locations (`..`, `join`, `complement`, `<`, `>`) and the main qualifiers of a `CDS`.
- [ ] 3 Practiced: I can write a streaming parser and extract, translate and verify every CDS of a record.
- [ ] 4 Applied: [[02-sequence-translation]] checks the CDS translations of real GenBank records (including a `-` strand, a spliced and a partial CDS), and [[bio-core]] stores features without loss.
- [ ] 5 Explained: I can explain the separation of layout and model across GenBank, ENA and GFF, and every pitfall in the checklist.

## References

[^gbrel]: [[NCBI GenBank]], GenBank release notes (gbrel.txt), section 3.4 on the structure of an entry, including the FEATURES format (3.4.12).
[^sample]: [[NCBI GenBank]], "Sample GenBank Record" (annotated record U49845, *Saccharomyces cerevisiae*).
[^ft]: [[INSDC Feature Table Definition]], version 11.3 (October 2024): feature keys, qualifiers, and location syntax (section 3.4).
[^gc]: [[NCBI Genetic Codes]], "The Genetic Codes", numbered translation tables.
[^genbank]: [[NCBI GenBank]], GenBank 2025 update (*Nucleic Acids Research*); the source note's reading of a record and its caveat on archive annotation.
[^biopython]: [[Biopython]], `Bio.SeqIO` (reading GenBank files); tier C, used only as a test oracle.
