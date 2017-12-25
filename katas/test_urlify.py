"""Test urlify."""


def test_urlify():
    """Test urlify."""
    from urlify import urlify
    string = 'This is a url'
    assert urlify(string) == 'This%20is%20a%20url'
