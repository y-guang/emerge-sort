# Emerge Sort: A Locality-Minimising Variant of Merge Sort

This technical note introduces a family of merge sort variants collectively referred to as **Emerge Sort**, designed to explicitly *minimise locality* in element comparisons. Uniquely, each pairwise comparison is treated as a **cold start** — that is, no cached elements are reused across adjacent trials. This locality suppression is intended to better reflect human cognitive constraints in sorting tasks.

The name *Emerge Sort* serves a dual purpose. First, it denotes an *enhanced* merge sort designed for behavioural contexts. Second, it anticipates the algorithm’s ability to support **group-level ranking emergence** from individual judgments—a property to be detailed in subsequent work. This note serves as a technical note accompanying the formal manuscript.

## Background: Human as Low-Cache Processing Unit

In most sorting problems, human decision-makers can be metaphorically described as single-core processors equipped with an extremely small *fully associative cache*. Foundational research supports this: Miller (1956) famously estimated working memory capacity at **7±2 items**, while Cowan (2001) proposed a more conservative estimate of **4 items**.

Given that each comparison involves two items, a repeated item is likely to be retained in working memory if it reappears within approximately $\left\lceil \frac{7}{2} \right\rceil = 4$ consecutive trials. In particular, if an item reoccurs in **immediate succession**, a cache hit is almost certain.

However, in **cognitively mediated comparison tasks**, locality is not a virtue. While locality boosts speed in computational circuits, it may introduce **bias** in human decision-making. For instance, repeated exposure to a single item may reduce attentional resources through **practice effects** or **habituation**. Thus, *minimising locality*—ensuring that comparisons remain novel—may yield more **stable and fair** judgments.

This motivates the core principle of Emerge Sort: given a small sliding window of size $w$, each of the $w$ most recent comparisons must involve **distinct items**.

## Algorithmic Design

To achieve this, we slightly modify the standard merge sort procedure:

1. **Maintain a queue of subsequence pairs** to be merged, implemented as a FIFO buffer.
2. **Track last-access time** for each element to monitor recency.
3. **Alternate merges** between subsequence pairs, ensuring distinctiveness in a rolling window of size $w$.
4. When the number of eligible pairs falls below $w$, and a repeat access is imminent:

   * sample comparisons **outside the window** using a defined strategy.

This deferred sampling becomes essential when local distinctiveness constraints conflict with available comparisons. The sampling strategy itself is a design axis worth exploring. Options at least include:

* **uniform sampling**: select any available pair uniformly at random.
* **Recency-weighted selection**: prioritise long-unseen pairs.
* **Consensus-prioritised sampling**: prioritise pairs under-represented across participants.

Such strategies may help **maximise information reuse**, particularly in **multi-judge** scenarios where group consensus is inferred from sparse comparisons.

An pseudocode is provided [here](./pseudo-code.pdf).

## Algorithmic Properties

### Property 1: Bounded Error Propagation

The effect of a **single judgment error** is **bounded** in scope. This can be shown recursively.

### Property 2: Complexity Comparable to Merge Sort

When the window size $w$ is much smaller than the total number of elements, the **asymptotic complexity** of Emerge Sort remains.

