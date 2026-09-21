#!/usr/bin/env python3
"""Module to calculate the inverse of a matrix."""


def det_helper(matrix):
    """Helper function to calculate the determinant."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])
    det = 0
    for c in range(n):
        sub = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * det_helper(sub)
    return det


def inverse(matrix):
    """Calculates the inverse of a matrix."""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or (len(matrix) == 1 and len(matrix[0]) == 0):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = det_helper(matrix)
    if det == 0:
        return None

    if n == 1:
        return [[1 / matrix[0][0]]]

    inv_mat = []
    for r in range(n):
        inv_row = []
        for c in range(n):
            sub = [row[:r] + row[r+1:]
                   for i, row in enumerate(matrix) if i != c]
            adjugate_val = ((-1) ** (r + c)) * det_helper(sub)
            inv_row.append(adjugate_val / det)
        inv_mat.append(inv_row)

    return inv_mat
