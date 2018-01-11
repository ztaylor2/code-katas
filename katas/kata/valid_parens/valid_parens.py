"""Seeing is we have valid parens in a string.

#1 Best Practices Solution:

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

"""


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
