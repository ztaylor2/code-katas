"""Check is a a sting is a permutation of another string."""


def check_permutation(string1, string2):
    """Check if a string is a permutation of another string."""
    if sorted(string1) == sorted(string2):
        return True
    return False
