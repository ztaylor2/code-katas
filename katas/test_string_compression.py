"""Test string compression."""


def test_compression_simple():
    """."""
    from string_compression import string_compression
    assert string_compression('aaaa') == 'a4'


def test_compression_multiple_chars():
    """."""
    from string_compression import string_compression
    assert string_compression('aaabbb') == 'a3b3'
