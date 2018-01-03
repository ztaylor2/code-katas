"""Implement a method to perfom a string compression using counts of repeated charactors.

CTCI 1.6

ex: input: aabcccccaaa
    output: a2b1c5a3

if compressed string not smaller than original string return original string.
"""


def string_compression(uncompressed_string):
    """Simple string compression of repeated chars."""
    compressed_string = ''
    i = 0
    x = 0
    while i < len(uncompressed_string):
        compressed_string += uncompressed_string[i]
        x = 0
        while i + x < len(uncompressed_string):
            if (uncompressed_string[i] == uncompressed_string[i + x]):
                x += 1
            else:
                break
        compressed_string += str(x)
        i += x
    if len(uncompressed_string) <= len(compressed_string):
        return uncompressed_string
    return compressed_string

"""
Python solution from http://rosettacode.org/wiki/Run-length_encoding#Python:

Note: this output is not exactly what CTCI is looking for.

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character,count)
        lst.append(entry)
    return lst
"""

def string_comp_refactored(uncompressed_string):
    """Refactor of string compression method."""
    count = 1
    prev = ''
    compressed_string = ''
    for char in uncompressed_string:
        if char != prev:
            