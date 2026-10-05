---
aliases:
  - Research Article
  - Journal Article
  - Research Paper
  - IMRaD
  - Article scientifique
tags:
  - type/concept
  - domain/scientific-practice
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Primary Literature]]"
related:
  - "[[Reading a Scientific Paper]]"
  - "[[Review Article]]"
  - "[[Peer Review]]"
  - "[[Scientific Writing]]"
  - "[[Data Visualization]]"
  - "[[Reporting Guideline]]"
  - "[[Accession Number]]"
  - "[[Reference Management]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Coursera Stanford - Writing in the Sciences]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Meselson 1958 - The Replication of DNA in Escherichia coli]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
  - "[[European Nucleotide Archive]]"
  - "[[DOI Handbook]]"
  - "[[PubMed]]"
---

# Scientific Paper

> [!abstract]
> A research paper is a fixed set of parts, each answering one question (what, who, why, how, what was found, what it means), so a reader can find the claim, the evidence and the method without reading every word.

## Definition

A **scientific paper** (research article) is the formal, citable report of a piece of [[Primary Literature|primary research]] in a journal. Its body usually follows the **IMRaD** structure (Introduction, Methods, Results, Discussion), framed by a title, authors and affiliations, an abstract, figures and tables, and references.[^sciwrite] Modern papers add **supplementary material** (details that do not fit the main text) and a **data availability statement** giving the accessions of the deposited data.[^jumper][^ena] The paper is identified by a DOI, a persistent, case-insensitive identifier.[^doi]

## Why it matters

- **The unit of citation.** Databases, tools and results are cited through papers; PubMed indexes their citations and abstracts and links to the full text.[^pubmed]
- **Reproducing an analysis.** The parameters, software versions and accessions needed to rerun an analysis are in the methods, the supplementary material and the data availability statement, not in the abstract ([[Computational Reproducibility]]).
- **Raw data.** An accession in a data availability statement leads to the archive (for sequencing data, ENA or SRA) and from there to the files.[^ena]
- **Your own reports.** The report of [[10-genomic-pipeline]] is written like the methods and results of a paper: the same anatomy, at small scale.

## Core (L1)

![[scientific-paper-anatomy.svg]]

| Part | Question it answers | Look for |
|---|---|---|
| Title | What is the paper about? | the object studied, often the main claim |
| Authors, affiliations | Who is responsible? | corresponding author ([[Authorship]]) |
| Abstract | What was done and found, in one paragraph? | the claim, the system, the key number |
| Introduction | Why ask, what was known, what is missing? | the gap and the [[Hypothesis]] |
| Methods | How was it done? | design, samples, controls, software and versions, statistics |
| Results | What was found? | the figures and tables, one message each |
| Discussion | What does it mean, what are the limits? | interpretation versus evidence, stated limitations |
| References | What does it build on? | the primary source of each background claim |
| Supplementary material | What did not fit? | full methods, extra figures and tables |
| Data availability | Where are the data and code? | accessions, repository DOIs ([[Accession Number]]) |

The manuscript sections, figures and tables are what the writing side of the field teaches as "the manuscript".[^sciwrite] Names and order vary between journals; identify each part by its function, not by its heading.

**Formats.** A full article has all the parts above. A **letter** is a short report: Watson and Crick's 1953 paper is about one page with one figure.[^watson] A **review** has a different structure, organized by topic ([[Review Article]]).

## Deeper (L2)

- **Order of the argument, not of the work.** IMRaD reconstructs the reasoning (question, method, evidence, interpretation); it is not a lab diary, and it is not the best reading order either ([[Reading a Scientific Paper]]).
- **Figures are the evidence.** Each results paragraph points to a figure or table; the legend states what was measured, on how many samples, with which test ([[Data Visualization]], [[P-Value]]).
- **The supplementary material can be the method.** In the AlphaFold 2 paper, the main text gives the architecture overview and the supplementary information holds the algorithmic detail.[^jumper] For a bioinformatician reproducing a method, the supplement is required reading.
- **Bibliographic record.** A paper's metadata (authors, title, journal, volume, issue, pages, year, DOI) is what search engines index and reference managers store: Watson 1953 is *Nature* 171(4356):737-738, doi:10.1038/171737a0.[^watson] See [[Reference Management]].
- **What the methods must contain** is increasingly fixed by checklists ([[Reporting Guideline]]), and whether the paper was checked by experts before publication is a separate question ([[Peer Review]], [[Preprint]]).

## Computational representation

A paper is text for humans plus a structured record for machines (authors, journal, year, DOI): retrieving those records is shown in [[Literature Search]], validating and formatting them in [[Reference Management]].

## Worked example

> [!example] Dissecting Watson 1953, a paper without headings
> *Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid*, Watson JD, Crick FHC, *Nature* 171(4356):737-738 (1953).[^watson] The letter has no section headings, but every IMRaD function is there.
>
> | Function | Where it is in the letter |
> |---|---|
> | Abstract | The opening sentences: "We wish to suggest a structure for the salt of deoxyribose nucleic acid (D.N.A.). This structure has novel features which are of considerable biological interest." |
> | Introduction | Why earlier proposed structures, including Pauling and Corey's three-chain model, are unsatisfactory |
> | Methods | Model building from stereochemistry and published X-ray data; no experiment of their own |
> | Results | Two helical chains running in opposite directions, bases inside paired A-T and G-C, 3.4 Å between bases, a repeat every 10 residues; one figure |
> | Discussion | "It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material." |
> | Acknowledgments | The X-ray results of Franklin, Wilkins and co-workers |
>
> **What a modern reader misses:** a methods section, supplementary material, a data availability statement. The evidence lives in companion papers of the same issue, and the copying hypothesis was tested five years later by [[Meselson 1958 - The Replication of DNA in Escherichia coli]], a full article free at PMC528642.[^meselson] Compare with [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]] (free at PMC8371605), where the method needs a long supplement.[^jumper]

## Common misconceptions

> [!warning] "The abstract summarizes the evidence"
> The abstract is the authors' own framing of their claim. The evidence is in the figures and the methods, and the claim must be checked against them.

> [!warning] "Supplementary material is optional"
> For computational papers the parameters, algorithms and full benchmarks often live in the supplement.[^jumper] Skipping it means not knowing what was done.

> [!warning] "A data availability statement means the data are available"
> The statement is a pointer, not a check. Follow the accession to the archive before planning a reanalysis ([[Accession Number]]).

## Exercises

> [!question] Exercise 1 (L1)
> Assign each sentence (invented) to a section: (a) "Reads were aligned with aligner X version 2.1 using default parameters." (b) "Expression of gene A increased threefold after heat shock (Fig. 2b)." (c) "Whether gene A responds to heat in yeast is unknown." (d) "Gene A may therefore protect cells from stress, although our sample size was small."

> [!success]- Solution
> (a) Methods: a procedure with a software version. (b) Results: a finding pointing to a figure. (c) Introduction: the gap. (d) Discussion: interpretation ("may therefore") plus a stated limitation.

> [!question] Exercise 2 (L1)
> Where in a paper do you look for: the software version used; the accession of the raw reads; the main claim; why the authors think it matters; what the authors admit they could not show?

> [!success]- Solution
> Methods (or supplementary methods); data availability statement; abstract, then the figure that supports it; introduction and the end of the discussion; the limitations paragraph of the discussion.

> [!question] Exercise 3 (L2)
> Open Meselson 1958 (free at PMC528642). List its parts as in the table above and find the figure that carries the decisive result.

> [!success]- Solution
> Map each block of the article to a function, whatever its heading. The decisive figure is the one showing DNA band positions in the density gradient across generations after the shift from heavy to light nitrogen: one hybrid band after one generation, hybrid and light bands after two.[^meselson] Everything else in the paper serves to make that figure trustworthy.

> [!question] Exercise 4 (L2)
> Why could nobody reproduce the evidence for the double helix from Watson 1953 alone, and what does that teach about letters?

> [!success]- Solution
> The letter states a model and cites X-ray data published by others; it gives no data or procedure of its own.[^watson] A short format trades completeness for speed: to evaluate it, read the companion papers that hold the evidence.

## Mastery checklist

- [ ] 1 Recognized: I can name the parts of a research paper, including IMRaD.
- [ ] 2 Understood: I can say which question each part answers and where the evidence is.
- [ ] 3 Practiced: I can map an unfamiliar paper, even one without headings, onto the IMRaD functions.
- [ ] 4 Applied: I found the software versions and data accessions of a real paper and wrote the [[10-genomic-pipeline]] report with the same anatomy.
- [ ] 5 Explained: I can explain why figures, supplementary material and data statements matter for reproducing a bioinformatics result.

## References

[^sciwrite]: [[Coursera Stanford - Writing in the Sciences]], module "The manuscript" (tables and figures; results, methods, introduction and discussion sections).
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature* 171(4356):737-738.
[^meselson]: [[Meselson 1958 - The Replication of DNA in Escherichia coli]], *PNAS* 44(7):671-682.
[^jumper]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]], *Nature* 596:583-589, main text and supplementary information.
[^ena]: [[European Nucleotide Archive]], accessions in data availability statements.
[^doi]: [[DOI Handbook]], section 2.2 "DOI name syntax".
[^pubmed]: [[PubMed]], About page.
