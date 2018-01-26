"""Map the indexes of one anagram to another.

ex:

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

returns:
[1, 4, 3, 2, 0]

"""


def anagram_map(A, B):
    """Map the indexes of one anagram to another."""
    b_locations = {}
    mapping = []

    for index, val in enumerate(B):
        b_locations[val] = index

    for val in A:
        mapping.append(b_locations[val])

    return mapping
