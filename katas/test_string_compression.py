"""Test string compression."""


def test_compression_simple():
    """."""
    from string_compression import string_compression
    assert string_compression('aaaa') == 'a4'
