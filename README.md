# Discrete Fréchet Distance Visualization

Generates two random polygonal curves and computes their Discrete Fréchet Distance

The visualization shows:
- Both curves in 2D
- The optimal coupling path
- Pairwise distances along the path

## The Discrete Frechet Distance

A measure of similarity between two curves that respects the ordering of points

In other words, the minimum leash length required for a person and a dog to walk along two curves without backtracking.

The result is computed with dynamic programming, then backtracking is used to recover the optimal path

## How to run

Install dependencies:
`pip install numpy matplotlib`

Run:
`python frechet.py`

