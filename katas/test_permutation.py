"""Test permutation."""


def test_permutation_false():
    """Test permutation returns false."""
    from permutation import permutation
    assert permutation('hi', 'hello') is False


def test_permutation_true():
    """Test permutation returns true."""
    from permutation import permutation
    assert permutation('abcdefg', 'gfedcba') is True
