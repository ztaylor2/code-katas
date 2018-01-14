"""."""


def test_two_sum():
    """."""
    from two_sum import two_sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_more():
    """."""
    from two_sum import two_sum
    assert two_sum([1, 2, 11, 4, 5, 6, 7, 8], 8) == [0, 6]


def test_two_sum_n():
    """."""
    from two_sum import two_sum_n
    assert two_sum_n([2, 7, 11, 15], 9) == [0, 1]
