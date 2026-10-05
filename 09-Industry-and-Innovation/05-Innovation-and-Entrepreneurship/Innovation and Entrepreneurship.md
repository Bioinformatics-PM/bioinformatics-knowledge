---
aliases:
  - Biotech Entrepreneurship
  - Innovation et entrepreneuriat
tags:
  - type/moc
  - domain/industry
  - domain/bioinformatics
  - level/L3
  - level/M1
prerequisites:
  - "[[Industry Landscape]]"
  - "[[Regulation and Standards]]"
  - "[[Research Data Management]]"
projects:
  - "[[Bioinformatics Lab]]"
  - "[[biolab-web]]"
sources:
  - "[[NHGRI DNA Sequencing Costs]]"
  - "[[Scannell 2012 - Diagnosing the Decline in Pharmaceutical R&D Efficiency]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
---

# Innovation and Entrepreneurship

> [!abstract]
> How a discovery or a tool becomes a product: intellectual property on sequences and software, technology transfer from universities, business models and funding of biotech and bioinformatics companies, and the long-term trends (sequencing cost, R&D productivity, AI) that shape the market, read from data rather than from hype.

## Why it matters for bioinformatics

Bioinformaticians write code and analyze data that may be patentable, licensable or the core of a company, and they choose a license every time they publish a repository. Market trends are measurable: NHGRI tracks the cost of sequencing since 2001, the decline in drugs approved per R&D dollar has been quantified, and AI results such as AlphaFold have peer-reviewed benchmarks.[^nhgri][^scannell][^jumper] Reading those sources correctly is the antidote to hype.

## Before you start

- [[Industry Landscape]]: sectors and roles.
- [[Regulation and Standards]]: the regulatory path that any health product must follow.
- [[Research Data Management]]: [[Software License]], [[Data License]].

## Learning path

### Stage 3 - Advanced (L3)

1. [[Intellectual Property]] (L3): distinguish patents, copyright, trade secrets and trademarks, and what each protects in biotech and software.
2. [[Patent]] (L3): state the patentability criteria (novelty, inventive step, industrial application), the term, the claims and the EPO, USPTO and PCT routes.
3. [[Gene Patent]] (L3): explain what can be patented about sequences in the US after the 2013 Myriad decision and in Europe under the Biotech Directive.
4. [[Software Patent]] (L3): know when algorithms and software can be patented (computer-implemented inventions in Europe, the Alice test in the US) and why copyright protects the code itself.
5. [[Freedom to Operate]] (L3): tell patentability from freedom to operate and read the claims of a patent.
6. [[Technology Transfer]] (L3): explain how universities protect, license or spin out inventions (the Bayh-Dole Act in the US, SATTs in France).
7. [[Licensing Agreement]] (L3): read the terms of a license (field, exclusivity, upfront payment, milestones, royalties).
8. [[Technology Readiness Level]] (L3): place a technology on the TRL scale that funders use to judge maturity.
9. [[Spin-Off Company]] (L3): know how an academic spin-off is founded (team, IP license, first funding).
10. [[Startup Funding]] (L3): compare non-dilutive funding (grants, innovation programs) with equity rounds, and compute dilution.
11. [[Biotech Business Model]] (L3): compare asset-centric, platform, tools, diagnostics and service models and how each earns revenue.
12. [[Open-Source Business Model]] (L3): explain how open-source bioinformatics software is sustained (grants, support, hosted services, open core, dual licensing).
13. [[Sequencing Cost Trend]] (L3): read the NHGRI cost data and explain what cheap sequencing changed, and what it did not (interpretation, storage, clinical validation).[^nhgri]
14. [[Eroom's Law]] (L3): explain the long-term decline in new drugs per R&D dollar and its proposed causes.[^scannell]

### Stage 4 - Frontier (M1)

15. [[Artificial Intelligence in Biology]] (M1): assess AI in biology as a market trend (structure prediction, protein and genomic language models, AI-designed molecules), separating benchmarked results from claims.[^jumper]

> [!tip]
> Choose the license of each [[Bioinformatics Lab]] repository deliberately after items 1, 4 and 12: it is the one entrepreneurial decision you make on every project.

## Uses from other domains

- [[Software License]] and [[Data License]] ([[Research Data Management]]): the legal basis of open source and open data.
- [[Open Science]] ([[Reproducibility]]): the academic norm that open-source models build on.
- [[Next-Generation Sequencing]] and [[Long-Read Sequencing]] ([[Biotechnology]]): the technologies behind the cost curve.
- [[Drug Development]] ([[Drug Discovery]]): the value chain that biotech business models sit in.
- [[Neural Network]] ([[Statistical Learning]]), [[Protein Structure Prediction]] and [[Protein Language Model]] ([[Structural Bioinformatics]]): the technical basis of the AI trend.
- [[AI-Driven Drug Design]] ([[Drug Discovery]]): where AI meets a product pipeline.
- [[Software as a Medical Device]] and [[Health Technology Assessment]] ([[Regulation and Standards]]): regulation and reimbursement decide whether a health product has a market.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| No verified course note yet | | | Use the data sources below for market trends |

## Reference books

No textbook: primary data and landmark papers.

- [[NHGRI DNA Sequencing Costs]]: cost per megabase and per genome (item 13).[^nhgri]
- [[Scannell 2012 - Diagnosing the Decline in Pharmaceutical R&D Efficiency]]: the paper that named Eroom's law (item 14).[^scannell]
- [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]: the reference result behind the AI-in-biology trend (item 15).[^jumper]

## Lab projects

- [[Bioinformatics Lab]]: open repositories with an explicit LICENSE; the choice of license is a small [[Intellectual Property]] decision.
- [[biolab-web]]: the product layer, where a scientific engine becomes a usable tool.

## References

[^nhgri]: [[NHGRI DNA Sequencing Costs]], National Human Genome Research Institute.
[^scannell]: [[Scannell 2012 - Diagnosing the Decline in Pharmaceutical R&D Efficiency]], *Nature Reviews Drug Discovery*.
[^jumper]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]], *Nature*.
