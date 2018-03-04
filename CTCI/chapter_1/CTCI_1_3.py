"""CTCI problem 1.3 URLify.

replace all spaces with %20 in a string

"""


def urlify(input_string):
    """Turn a string into a url."""
    return '%20'.join(input_string.split())
