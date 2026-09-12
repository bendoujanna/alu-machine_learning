#!/usr/bin/env python3
"""Module for element-wise addition of two arrays."""


def add_arrays(arr1, arr2):
    """Add two arrays element-wise and return a new list, or None if shapes differ."""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]