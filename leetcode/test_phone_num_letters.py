"""Test phone num letters."""


def test_phone_nums():
    """."""
    from phone_num_letters import phone_num_letters
    assert phone_num_letters('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def test_inerative_nums():
    """."""
    from phone_num_letters import phone_letters
    assert phone_letters('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
