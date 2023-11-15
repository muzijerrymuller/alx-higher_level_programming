#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1] for _ in range(n)]
    for i in range(1, n):
        row = triangles[i]
        prev_row = triangles[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
    return triangles
