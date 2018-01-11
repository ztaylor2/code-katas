"""Test the is unique method."""


def test_is_unique_true():
    """Test if is unique returns true."""
    from is_unique import is_unique
    assert is_unique('abcdefghijklmnop')


def test_is_unique_false():
    """Test if is uneque returns false."""
    from is_unique import is_unique
    assert not is_unique('aa')


def test_is_unique_false_longer_string():
    """Test is unique returns false with a longer stirng."""
    from is_unique import is_unique
    assert not is_unique('abcdefghijklmnoprstwxyzz')
