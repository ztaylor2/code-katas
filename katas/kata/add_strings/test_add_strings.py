"""Tests for adding string."""

import pytest

STRING_TABLE = [('1', '2', '3'), ('5', '4', '9'),
                ('11', '12', '23'), ('5', '5', '10'),
                ("4", "5", "9"), ("34", "5", "39")]


@pytest.mark.parametrize('a, b, result', STRING_TABLE)
def test_paren(a, b, result):
    """Testing add_strings funciton."""
    from add_strings import sum_str
    assert sum_str(a, b) == result
