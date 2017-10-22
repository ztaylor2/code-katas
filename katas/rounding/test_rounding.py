"""Test rounding nums."""

import pytest


ROUND_TABLE = [(1.2, 1), (1.4, 1.5), (1.6, 1.5), (1.7, 1.5),
               (4.2, 4), (4.26, 4.5), (4.4, 4.5), (4.6, 4.5),
               (4.75, 5), (4.8, 5)]


@pytest.mark.parametrize('n, result', ROUND_TABLE)
def test_rounding(n, result):
    """Testing roudning nums funciton."""
    from rounding import solution
    assert solution(n) == result
