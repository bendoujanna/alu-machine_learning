#!/usr/bin/env python3
"""Module to calculate the adjugate matrix."""


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


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or (len(matrix) == 1 and len(matrix[0]) == 0):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    adj_mat = []
    for r in range(n):
        adj_row = []
        for c in range(n):
            # Direct transposition by swapping r and c in the sub-matrix construction
            sub = [row[:r] + row[r + 1:] for i, row in enumerate(matrix) if i != c]
            sign = (-1) ** (r + c)
            adj_row.append(sign * det_helper(sub))
        adj_mat.append(adj_row)

    return adj_mat
