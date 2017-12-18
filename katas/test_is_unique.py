"""Test is unique function."""


def test_is_unique_false():
    """Test is unique returns false."""
    from is_unique import is_unique
    assert is_unique('hello') is False


def test_is_unique_true():
    """Test is unique returns true."""
    from is_unique import is_unique
    assert is_unique('asdfjkl;') is True
