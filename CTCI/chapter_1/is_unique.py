"""Determine if a sting has all unique charactors."""


def is_unique(a_string):
    """Test if a string has all unique charactors."""
    charactors = {}
    for char in a_string:
        if char in charactors:
            return False
        charactors[char] = True
    return True
