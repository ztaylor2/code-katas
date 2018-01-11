"""Test sum odd in sequence."""

import pytest


SEQ_TABLE = [([1, 1, 2, 2, 3, 3, 4, 4, 2], 2),
             ([5, 5, 3, 3, 2, 2, 3, 4, 4, 5, 3], 5),
             ([4, 5, 645, 3, 45, 34, 645, 4, 5, 3, 34], 45),
             ([1, 2, 3, 1, 2], 3),
             ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5)]


@pytest.mark.parametrize('n, result', SEQ_TABLE)
def test_odd_num_occ(n, result):
    """Testing odd num finder funciton."""
    from odd_num_occ import find_it
    assert find_it(n) == result
