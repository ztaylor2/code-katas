"""Test CTCI problem 1.2."""


def test_is_permutation():
    """Test to see if permutation returns true and false."""
    from CTCI_1_2 import is_permutation
    assert is_permutation('abcdef', 'fedcba') is True
    assert is_permutation('input1', 'input2') is False
