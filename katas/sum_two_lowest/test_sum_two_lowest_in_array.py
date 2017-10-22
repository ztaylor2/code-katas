"""Test of sum two lowest numbers in an array."""


import pytest


SUM_TABLE = [([0, 1, 2, 3, 4, 5, 6], 1), ([-4, -10, 10, 11], -14),
             ([40, 30, 55], 70), ([5, 8, 12, 18, 22], 13),
             ([7, 15, 12, 18, 22], 19), ([25, 42, 12, 18, 22], 30)]


@pytest.mark.parametrize('n, result', SUM_TABLE)
def test_sum_two_lowest_in_array(n, result):
    """."""
    from sum_two_lowest_in_array import sum_two_smallest_numbers
    assert sum_two_smallest_numbers(n) == result
