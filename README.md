# Anatomy of Breakthroughs

[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

![](frontpage.png)

A scholarly monograph examining the foundational ideas that shaped modern computer science, information theory, and computational complexity.

## Overview

Sixteen chapters explore breakthroughs spanning:

- **Computability** — Turing machines, λ-calculus, the Church--Turing Thesis
- **Undecidability** — The halting problem, Gödel's incompleteness theorems, Rice's Theorem
- **Information theory** — Shannon entropy, channel capacity, error-correcting codes
- **Algorithmic information** — Kolmogorov complexity, algorithmic randomness
- **Computational complexity** — P vs. NP, NP-completeness, the PCP theorem
- **Cryptography** — Public-key systems, zero-knowledge proofs, post-quantum schemes
- **Distributed computing** — Consensus protocols, the FLP impossibility theorem
- **Interactive proofs** — IP = PSPACE, multi-prover systems
- **Randomized computation** — Probabilistic algorithms, the polynomial hierarchy of randomness
- **Privacy** — Differential privacy and its information-theoretic foundations

Each chapter develops the relevant mathematics rigorously, situating results within their historical and conceptual context.

## Structure

| Part | Title | Chapters |
|------|-------|----------|
| I | The Nature of Computation | 1--4 |
| II | Information | 5--7 |
| III | Difficulty and Coordination | 8--15 |
| IV | Epilogue | 16 |

Six appendices follow: the Mind Map (reading paths and the science of learning), a historical timeline, biographical sketches, mathematical prerequisites, further reading, and selected exercise solutions.

## Intended Audience

Graduate students and researchers in theoretical computer science, mathematics, and related fields.

### Prerequisites

- Discrete mathematics (sets, functions, relations, induction, combinatorics)
- Linear algebra (vector spaces, matrices, eigenvalues, determinants)
- Probability theory (random variables, expectation, variance, concentration inequalities)
- Basic programming (algorithmic correctness)

A self-contained review of mathematical prerequisites is provided in the appendix.

## Building the Book

```bash
make pdf        # Build the PDF
make clean      # Remove build artifacts
make check      # Verify compilation
```

A pre-built PDF is available from the [latest release](https://github.com/csv610/deep_ideas_book/releases/latest).

## Citation

```bibtex
@book{deepideas2026,
  author = {Author Name},
  title = {Anatomy of Breakthroughs: The Deep Ideas Behind the Digital Age},
  year = {2026},
  note = {Unpublished monograph}
}
```

## License

[MIT License](LICENSE)
