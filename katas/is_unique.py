"""
Implement an algorithm that determines if a string has all unique charactors.

Solution: O(n)
"""


def is_unique(a_string):
    """."""
    charactors = {}
    for x in a_string:
        if x in charactors:
            return False
        else:
            charactors[x] = True
    return True
