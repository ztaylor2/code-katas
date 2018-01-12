"""Add two ints together that are input as strings.

#1 Best Practices Solution:

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
"""


def sum_str(a, b):
    """Add two strings."""
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    return str(int(a) + int(b))
