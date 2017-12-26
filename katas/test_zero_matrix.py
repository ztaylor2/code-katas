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
