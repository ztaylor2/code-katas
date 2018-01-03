"""Implement a method to perfom a string compressoin using counts of repeated charactors.

CTCI 1.6

ex: input: aabcccccaaa
    output: a2b1c5a3

if compressed string is not smaller than original string return original string.
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
