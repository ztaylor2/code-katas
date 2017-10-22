"""Add two ints together that are input as strings."""


def sum_str(a, b):
    """Add two strings."""
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    return str(int(a) + int(b))
