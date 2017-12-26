"""Zero matrix: Write an algorithm such that if an element in an MxN
matrix is 0, its entire row and column are set to 0.

CTCI 1.8.
"""


def zero_matrix(a_matrix):
    """Zero matrix."""
    rows = len(a_matrix)
    cols = len(a_matrix[0])
    zeros = []

    # locate and store all zeros in dict
    for i in range(rows):
        for j in range(cols):
            if a_matrix[i][j] == 0:
                zeros.append((i, j))

    # make rows zeros
    for zero in zeros:
        for x in range(cols):
            a_matrix[zero[0]][x] = 0

    # make cols zeros
    for zero in zeros:
        for x in range(rows):
            a_matrix[x][zero[1]] = 0

    return a_matrix

if __name__ == '__main__':
    a_matrix = [
        [1, 2, 3],
        [1, 2, 0],
        [1, 2, 3]
    ]

    print(zero_matrix(a_matrix))
