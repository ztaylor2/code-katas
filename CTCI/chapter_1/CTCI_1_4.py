"""CTCI 1.4 solution in python.

Given a string, write a function to see if it is a permutation of a palindrome.

ex:

input: 'Tact Coa'

output: True (permutation 'taco cat', 'atco cta')

ex: 

input: 'aabbc'

output: True (abcba)

if even number of every char except one char odd number it is a palindrome

ignore spaces

"""


def is_palindrome_permutation(input_string):
    """Determine if the input is a permutation of a palindrome."""
    input_string = input_string.lower()
    input_string = ''.join(input_string.split())

    number_chars = {}
    number_even_chars = 0

    for char in input_string:
        if char in number_chars:
            number_chars[char] += 1
        else:
            number_chars[char] = 1

    for char in number_chars:
        if number_chars[char] % 2 != 0:
            number_even_chars += 1
        if number_even_chars >= 2:
            return False

    return True
