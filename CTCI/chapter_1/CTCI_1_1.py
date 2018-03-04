"""Problem 1.1 in CTCI 6th Edition.

Implement an algorithm to determine if a string has all unique charactors. 

What if you can not use additional data structures?

ex: 

'abcd'

 """


# with data structure

def each_char_unique(input_string):
    """Check to see if each charactor is unique."""
    seen_chars = set()

    if not isinstance(input_string, str):
        raise TypeError('Input must be string.')

    if len(input_string) == 0:
        raise ValueError('Input string can\'t be empty.')

    for char in input_string:
        if char in seen_chars:
            return False
        seen_chars.add(char)

    return True


def each_char_unique_no_ds(input_string):
    """Test if each car is unique without using any data structures."""
    for index, char in enumerate(input_string):
        for second_char in input_string[index + 1:]:
            if char == second_char:
                return False

    return True
