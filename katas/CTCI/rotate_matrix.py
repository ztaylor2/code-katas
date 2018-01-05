"""
CTCI 1.7

Rotate Matrix

Given an image represented by an NxN matrix where each pizel in the
image is 4 bytes, write a method to rotate the image by 90 degrees.

ex:

input: [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

output: [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
"""

from copy import deepcopy


def rotate_matrix(input_matrix):
    """Rotate an matrix by 90 degrees."""
    n = len(input_matrix) - 1
    output_matrix = deepcopy(input_matrix)
    for i in range(n + 1):
        for j in range(n + 1):
            output_matrix[j][n - i] = input_matrix[i][j]
    return output_matrix
