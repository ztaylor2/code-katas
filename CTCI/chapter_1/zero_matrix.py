"""Problem 1.8 in CTCI."""


def zero_matrix(input_matrix):
    """Convert rows and cols of a matrix to zero if zero in that row/col."""
    zeros = []
    rows = len(input_matrix)
    cols = len(input_matrix[0])

    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j] == 0:
                zeros.append((i, j))

    for zero in zeros:
        for x in range(rows):
            input_matrix[x][zero[1]] = 0
        for n in range(cols):
            input_matrix[zero[0]][n] = 0

    return input_matrix
