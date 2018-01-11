"""URLify, CTCI problem 1.3."""


def urlify(string):
    """URLify a string."""
    urlify = '%20'
    return urlify.join(string.split())
