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


def rotate_matrix(input_matrix):
    """Rotate an image by 90 degrees."""
    output_matrix = input_matrix
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            output_matrix[j][3 - i] = input_matrix[i][j]
    return output_matrix
