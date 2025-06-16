# emerge-sort

🛠️ Under Active Development

**Emerge Sort** is a sorting algorithm designed for scenarios where **human judgment** and **error** are part of the process. It focuses on three key principles:

- ✅ **Fault-Tolerance** – Errors in pairwise comparisons shouldn't catastrophically affect the final ranking.
- 🎯 **Unbiasedness** – Average estimate converges to the true ranking.
- 🌐 **Emergent Cohesion** – Enables global order to **emerge** from noisy, local judgments by individuals.

This makes Emergence Sort especially suited for **psychological experiments**, **crowdsourced ranking**, and any case where sorting is performed by **fallible human observers**.

## Status

- ✅Algorithm finalized.
- 🚧 Production-ready implementation under development.
  - Python  - implementation coming soon.
  - JavaScript - implementation coming soon.
  - Matlab - based on community needs.
- 🚧 Preprint paper in preparation.

Contributions in other languages are welcome!

## Algorithm Details

A technical description of the algorithm is available in the [technical note.md](./docs/technical%20note.md)

A pseudo-code is provided in [pseudo-code.pdf](./docs/pseudo-code.pdf).

## Citation

If you use this algorithm in your work, please cite it as:

> Yang, G., Rodrigues, R., Yu, D., & Verstraten, F. A. J. (2025, June). Taking the human decision maker into account: A critical evaluation of sorting algorithms for large stimuli sets and guidelines for improvement. [Poster presentation]. *The Australasian Experimental Psychology Conference, Singapore*.
