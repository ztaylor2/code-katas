"""Test zero matrix."""


def test_zero_simple():
    """Test simple zero matrix."""
    from zero_matrix import zero_matrix
    a_matrix = [
        [1, 2, 3],
        [1, 2, 0],
        [1, 2, 3]
    ]

    assert zero_matrix(a_matrix) == [[1, 2, 0], [0, 0, 0], [1, 2, 0]]


def test_bigger_matrix():
    """Test a bigger matrix."""
    from zero_matrix import zero_matrix
    a_matrix = [
        [1, 2, 3, 4, 5],
        [0, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 0],
        [1, 2, 3, 4, 5]
    ]

    assert zero_matrix(a_matrix) == [
        [0, 2, 3, 4, 0],
        [0, 0, 0, 0, 0],
        [0, 2, 3, 4, 0],
        [0, 0, 0, 0, 0],
        [0, 2, 3, 4, 0]
    ]
