"""Test urlify."""


def test_urilfy():
    """Test urlify."""
    from urlify import urlify
    assert urlify('a string') == 'a%20string'
