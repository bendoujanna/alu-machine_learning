#!/usr/bin/env python3
"""Module to calculate the cofactor matrix."""


def det_helper(matrix):
    """Helper function to calculate the determinant."""
    n = len(matrix)
    if n == 1: return matrix[0][0]
    if n == 2: return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        sub = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * det_helper(sub)
    return det


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or (len(matrix) == 1 and len(matrix[0]) == 0):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cof_mat = []
    for r in range(n):
        cof_row = []
        for c in range(n):
            sub = [row[:c] + row[c + 1:] for i, row in enumerate(matrix) if i != r]
            sign = (-1) ** (r + c)
            cof_row.append(sign * det_helper(sub))
        cof_mat.append(cof_row)

    return cof_mat
