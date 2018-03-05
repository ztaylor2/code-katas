"""Test check permutation method."""


def test_permutation_false():
    """Test check permutation returns false."""
    from check_permutation import check_permutation
    assert not check_permutation('string1', 'string2')


def test_permutation_true():
    """Test check permutation returns true."""
    from check_permutation import check_permutation
    assert check_permutation('abcdefg', 'gfedcba') is True
