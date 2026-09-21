#!/usr/bin/env python3
"""Module to evaluate the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    # Symmetry check: a matrix must be symmetric to have a valid definiteness
    if not np.array_equal(matrix, matrix.T):
        return None

    # Round to avoid floating-point precision errors near zero
    eigenvalues = np.round(np.linalg.eigvals(matrix), 10)

    pos = np.all(eigenvalues > 0)
    pos_semi = np.all(eigenvalues >= 0) and not pos
    neg = np.all(eigenvalues < 0)
    neg_semi = np.all(eigenvalues <= 0) and not neg

    if pos:
        return "Positive definite"
    if pos_semi:
        return "Positive semi-definite"
    if neg:
        return "Negative definite"
    if neg_semi:
        return "Negative semi-definite"
    if np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"

    return None
