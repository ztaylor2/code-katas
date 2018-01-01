"""Implement a method to perfom a string compressoin using counts of repeated charactors.

CTCI 1.6

ex: input: aabcccccaaa
    output: a2b1c5a3

if compressed string is not smaller than original string return original string.
"""


def string_compression(uncompressed_string):
    """Simple string compression of repeated chars."""
    # return original string if length not improved
    if len(uncompressed_string) <= len(compressed_string):
        return uncompressed_string
