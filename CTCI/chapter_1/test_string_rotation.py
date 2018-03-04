"""Test the string rotation method."""


def test_string_rotration_false():
    """Test string rotation returns false."""
    from string_rotation import string_rotation
    assert string_rotation('hello', 'nothello') is False


def test_string_rotation_true():
    """Test string rotation returns true."""
    from string_rotation import string_rotation
    assert string_rotation('hello', 'elloh') is True
