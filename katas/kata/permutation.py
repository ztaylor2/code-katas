"""
Check is a string is a permutation of another.
"""


def permutation(string1, string2):
    """Check if permutations."""
    if sorted(string1) == sorted(string2):
        return True
    return False


def permutation_without_sorted(string1, string2):
    """Check if permutation without using pythons sorted method."""
    charactors = {}
    for char in string1:
        if char in charactors:
            charactors[char] += 1
        else:
            charactors[char] == 0

    charactors2 = {}
    for char in string2:
        if char in charactors2:
            charactors2 += 1
        else:
            charactors2 == 0

    for key in charactors:
        if charactors[key] != charactors2[key]:
            return False

    for key in charactors2:
        if charactors2[key] != charactors[key]:
            return False

    return True
