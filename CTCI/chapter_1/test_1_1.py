"""Test problem 1.1."""


def test_each_char_unique_true():
    """Test each char unique returns true."""
    from CTCI_1_1 import each_char_unique
    assert each_char_unique('abcdefghijklmnop') is True


def test_each_char_unique_false():
    """Test each char unique returns false."""
    from CTCI_1_1 import each_char_unique
    assert each_char_unique('abcdeffghijklm') is False


def test_each_char_no_db():
    """."""
    from CTCI_1_1 import each_char_unique_no_ds
    assert each_char_unique_no_ds('abcdefghijklmnop') is True
    assert each_char_unique_no_ds('abcdeffghijklm') is False
