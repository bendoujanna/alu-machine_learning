#!/usr/bin/env python3
"""Module for transposing a 2D matrix."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix as a new matrix."""
    return [[matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))]
