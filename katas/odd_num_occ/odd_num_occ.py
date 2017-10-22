"""Kata: Find the odd int.

#1 Best Practices Solution:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

"""


def find_it(seq):
    """Find the odd int in seq."""
    num_of_occurances = {}
    for num in seq:
        if num in num_of_occurances:
            num_of_occurances[num] = num_of_occurances[num] + 1
        else:
            num_of_occurances[num] = 1

    for key in num_of_occurances:
        if num_of_occurances[key] % 2 == 1:
            return key
    return None
