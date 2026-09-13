#!/usr/bin/env python3
"""Module for element-wise operations on numpy ndarrays."""
import numpy as np


def np_elementwise(mat1, mat2):
    """Return a tuple of element-wise sum, difference,
    product, and quotient."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
