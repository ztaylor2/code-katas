"""Test string compression."""


def test_compression_simple():
    """."""
    from string_compression import string_compression
    assert string_compression('aaaa') == 'a4'


def test_compression_multiple_chars():
    """."""
    from string_compression import string_compression
    assert string_compression('aaabbb') == 'a3b3'


def test_shorter_without_compression():
    """Test that the original string is returned if the compression doesn't make it shorter."""
    from string_compression import string_compression
    assert string_compression('abcd') == 'abcd'


def test_verbose_compression():
    """Test many charactor compression."""
    from string_compression import string_compression
    assert string_compression('aaaabbbcdddeefffff') == 'a4b3c1d3e2f5'
