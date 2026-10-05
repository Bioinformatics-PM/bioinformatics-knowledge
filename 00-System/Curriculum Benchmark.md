---
aliases:
  - Benchmark of Bachelor Programs
  - Comparaison des licences
tags:
  - type/system
sources:
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Stanford University - BS Biomedical Computation]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Mathématiques Sciences de la Vie]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]"
  - "[[Université Paris Cité - Licence Sciences de la Vie]]"
  - "[[Sorbonne Université - Licence Sciences de la Vie]]"
  - "[[ISCB - Bioinformatics Core Competencies]]"
---

# Curriculum Benchmark

> [!abstract]
> A comparison of thirteen bachelor programs (France, United States, Europe, China) and one competency framework, used to decide which subjects the vault's L1 to L3 syllabus must contain, in which order, and with which weight.

## Why it matters for bioinformatics

Bioinformatics sits on four legs (biology, mathematics and statistics, computer science, and some chemistry and physics). Real degrees show how much of each leg is needed and when. The vault copies what (almost) every program agrees on and makes explicit choices where they disagree.

## Programs compared

Legend: **Y1, Y2, Y3** = year verified; **LD / UD** = US lower division (years 1-2) / upper division (years 3-4); **req** = required, year not published; **opt** = one option among several; **elec** = elective only; **none** = absent from a fully verified required list; **n.v.** = not verified.

| Program | Intro bio | Genetics | Biochem. | Gen. chem. | Org. chem. | Physics | Maths | Prob./stats | Programming | Algorithms | Bioinformatics starts |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MIT 6-7[^mit67] | Y1 | req | req | Y1 | req | Y1 | Y1 + req | elec | req | req | elec (6.8701) |
| MIT 7[^mit7] | Y1 | req | req | Y1 | req | Y1 | Y1 | none | none | none | none |
| CMU Comp. Bio.[^cmu] | Y1 | req | req | req | n.v. | req | req | req | req | req | Y1 survey, then req |
| UCSD Bioinformatics[^ucsd] | LD | UD | UD | LD | LD | LD | LD | UD | LD | LD + UD | UD (4 courses) |
| Stanford BMC[^stanford] | req | n.v. | n.v. | req | n.v. | req | req | req | req | n.v. | track |
| Cambridge NST[^cam] | Y1 opt | n.v. | Y2 opt | Y1 opt | n.v. | Y1 opt | Y1 | Y1 opt | Y1 opt (R) | n.v. | Y1 practicals (opt) |
| ETH Biology[^eth] | Y1 | Y2 | Y1-Y2 | Y1-Y2 | n.v. | Y1 | Y1 | Y1-Y2 | Y1 or Y2 | n.v. | Y2 practical |
| Tsinghua Biology[^thu] | req | req | req | req | req | req | req | req | req | n.v. | elec (2 credits) |
| SJTU Bioinformatics[^sjtu] | n.v. | req | req | n.v. | n.v. | n.v. | n.v. | req | req | req | Y2 (semester 4) |
| Paris-Saclay LDD Maths-SV[^psmsv] | Y1 | n.v. | n.v. | n.v. | n.v. | n.v. | Y1 | n.v. | n.v. | n.v. | Y1 bio-maths project |
| Paris-Saclay LDD Info-SV[^psisv] | Y1 | n.v. | n.v. | Y1 | n.v. | Y1 | n.v. | n.v. | Y1 | n.v. | Y1 intro |
| Paris Cité SV[^upc] | Y1-Y2 | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | Y3 parcours |
| Sorbonne SV[^su] | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | n.v. | none verified |

The [[ISCB - Bioinformatics Core Competencies|ISCB competencies]][^iscb] are not a program; they serve as the outcome check for the whole table.

## Conclusions

1. **Subjects in (almost) all programs.** Every program with a verified course list requires introductory cell and molecular biology, [[Genetics]], [[Biochemistry]], university mathematics (calculus wherever titles were verified) and [[General Chemistry]].[^mit67][^mit7][^cmu][^ucsd][^eth][^thu] Physics is required in every program whose foundations were verified, except Cambridge where it is one option among the experimental sciences.[^mit7][^cmu][^ucsd][^eth][^psisv][^cam] Probability and statistics are required in the computational programs[^cmu][^ucsd][^stanford][^sjtu] (statistics is only an elective in MIT 6-7)[^mit67] and in the European and Chinese biology degrees,[^eth][^thu] but not in MIT's pure biology major.[^mit7]
2. **Typical order.** Year 1: introductory biology, general chemistry, calculus and physics,[^mit7][^eth] with introductory biology placed in the first semester even in the most computational program,[^cmu] plus a first programming course where computing is part of the program.[^eth][^cam][^psisv] Year 2: genetics, biochemistry and more statistics; a bioinformatics major or practical can branch off here.[^eth][^sjtu][^cam] Year 3 (or US upper division): algorithms-based bioinformatics (sequence analysis, databases, genomics), systems biology and specialization.[^ucsd][^upc][^sjtu] Standard French licences keep L1 and L2 common and specialize in L3.[^upc][^su][^psmsv]
3. **Weight of chemistry and physics.** Chemistry weighs at least as much as physics wherever it was verified, and usually more. In ETH's first two years, chemistry (lectures and practicals) takes 30 of 116 ECTS against 6 for physics.[^eth] Computational programs shrink both to about one course each (CMU: one chemistry and one physics course, 22 of 360 units),[^cmu] yet MIT 6-7 and UCSD still require [[Organic Chemistry]] in their computational degrees.[^mit67][^ucsd]
4. **Where bioinformatics starts.** Three models: a first-year hook (CMU's survey course, Paris-Saclay's L1 introduction, Cambridge's first-year practicals);[^cmu][^psisv][^cam] a second-year branch (ETH practical and systems biology, SJTU's choice of major in semester 4);[^eth][^sjtu] or third-year specialization (UCSD's upper-division sequence, Paris Cité's L3 parcours, MIT's elective).[^ucsd][^upc][^mit67] In every model, the substantial courses (sequence analysis, genomics, databases) belong to the **final stage**, alongside or after [[Algorithms]], [[Data Structures]] and the molecular core; first-year exposure is always a survey, a project or a practical.[^cmu][^ucsd][^sjtu]
5. **Balance.** In the most explicit computational program, the mathematics and statistics core (48 to 49 units) and the biology core (36 to 37 units) are of the same order, next to separate computer science and computational biology cores.[^cmu]

## Learning path implied for the vault

### Stage 1: Foundations (L1)

1. [[Cell Biology]], [[Molecular Biology]], [[Evolution]]: the shared first-year biology.
2. [[General Chemistry]] and a light [[Physics]] base: support, not a goal.
3. [[Calculus]] and first [[Probability]] on biological data.
4. [[Programming]] in Python, with a first look at [[Sequence Analysis]] as motivation.

### Stage 2: Mechanisms (L2)

1. [[Genetics]], [[Biochemistry]], targeted [[Organic Chemistry]].
2. [[Linear Algebra]], [[Statistical Inference]].
3. [[Data Structures]] and [[Algorithms]].

### Stage 3: Advanced (L3)

1. [[Sequence Analysis]] and [[Genomics]], then [[Phylogenetics]] and [[Population Genomics]].
2. [[Structural Bioinformatics]] and [[Systems Biology]].
3. A Lab project as the equivalent of directed research or a bioinformatics laboratory course.

## Caveats

- Many cells are **n.v.**: several French and Chinese maquettes could only be verified at the level of their structure. The conclusions rely on the programs with complete lists.
- US programs publish requirements, not year plans; "req" means only that the course is required.

## References

[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]].
[^mit7]: [[MIT - Course 7 Biology]].
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]].
[^ucsd]: [[UC San Diego - BS Bioinformatics]].
[^stanford]: [[Stanford University - BS Biomedical Computation]].
[^cam]: [[University of Cambridge - Natural Sciences Tripos]].
[^eth]: [[ETH Zurich - BSc Biology]].
[^thu]: [[Tsinghua University - BS Biological Sciences]].
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]].
[^psmsv]: [[Université Paris-Saclay - Licence Double Diplôme Mathématiques Sciences de la Vie]].
[^psisv]: [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]].
[^upc]: [[Université Paris Cité - Licence Sciences de la Vie]].
[^su]: [[Sorbonne Université - Licence Sciences de la Vie]].
[^iscb]: [[ISCB - Bioinformatics Core Competencies]].
