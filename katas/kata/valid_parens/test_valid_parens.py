"""Tests for valid parens."""

import pytest

PAREN_TABLE = [('(())', True), ('asdf()0)', False),
               ('lkdjf()lsdkjf', True), ('()())(()())())()()9(((((', False),
               ("  (", False), (")test", False), ("hi())(", False),
               ("hi(hi)()", True)]


@pytest.mark.parametrize('n, result', PAREN_TABLE)
def test_paren(n, result):
    """Testing our fibonacci() funciton."""
    from valid_parens import valid_parentheses
    assert valid_parentheses(n) == result
