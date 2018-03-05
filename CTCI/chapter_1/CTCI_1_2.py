"""CTCI chapter 1 problem 2.

Given two strings, write a method to determine if one string is
a permutation of another."""


def is_permutation(input1, input2):
    """Check if input strigs are permuntations of eachother."""
    if len(input1) != len(input2):
        return False
    if build_permutation_dictionary(input1) == build_permutation_dictionary(input2):
        return True
    return False


def build_permutation_dictionary(input_string):
    """Build a dictionary of an input string."""
    string_contents = {}

    for char in input_string:
        if char not in string_contents:
            string_contents[char] = 0
        else:
            string_contents[char] += 1

    return string_contents


"""
other solutions: 

if sorted(a) == sorted(b):
    return True
return False
"""