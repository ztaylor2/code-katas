"""Seeing is we have valid parens in a string."""


def valid_parentheses(string):
    """Test parens in string."""
    num_open = 0
    num_close = 0
    for char in string:
        if char == "(":
            num_open += 1
        elif char == ")":
            num_close += 1
        if num_close > num_open:
            return False
    if num_close != num_open:
        return False
    return True
