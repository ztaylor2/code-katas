"""Testing the sum on nth terms algo."""


import pytest


SUM_TABLE = [(1, '1.00'),
             (2, '1.25'),
             (3, '1.39')]


@pytest.mark.parametrize('n, result', SUM_TABLE)
def test_sum(n, result):
    """Testing sum funciton."""
    from sum_of_nth_terms import series_sum
    assert series_sum(n) == result
