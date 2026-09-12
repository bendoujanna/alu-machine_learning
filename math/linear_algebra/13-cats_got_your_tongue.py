#!/usr/bin/env python3
"""Module for concatenating numpy ndarrays along a specific axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two numpy ndarrays along a specific axis and return a new ndarray."""
    return np.concatenate((mat1, mat2), axis=axis)
