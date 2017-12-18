"""
Check is a string is a permutation of another.
"""


def permutation(string1, string2):
    """Check if permutations."""
    if sorted(string1) == sorted(string2):
        return True
    return False
