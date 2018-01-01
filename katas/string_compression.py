"""Implement a method to perfom a string compressoin using counts of repeated charactors.

CTCI 1.6

ex: input: aabcccccaaa
    output: a2b1c5a3

if compressed string is not smaller than original string return original string.
"""


def string_compression(uncompressed_string):
    """Simple string compression of repeated chars."""
    compressed_string = ''
    for i, char in enumerate(uncompressed_string):
        compressed_string += char
        while True:
            x = 0
            if (char == uncompressed_string[i + x]):
                x += 1
            else:
                break
        uncompressed_string += str(x)
        i += x
    # return original string if length not improved
    if len(uncompressed_string) <= len(compressed_string):
        return uncompressed_string
