"""Test string compression."""


def test_compression_simple():
    """Test compression with only one repeated charactor."""
    from string_compression import string_compression
    assert string_compression('aaaa') == 'a4'


def test_compression_multiple_chars():
    """Test compression with multiple charactors."""
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


def test_refactored_comp():
    """Test refactored compression."""
    from string_compression import string_comp_refactored
    assert string_comp_refactored('aaaabbbcdddeefffff') == 'a4b3c1d3e2f5'