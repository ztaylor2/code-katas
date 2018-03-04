"""Test problem 1.3."""


def test_urlify():
    """Test urlify."""
    from CTCI_1_3 import urlify
    assert urlify('this will be a url') == 'this%20will%20be%20a%20url'
