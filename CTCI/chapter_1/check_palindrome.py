"""Check if a string is a palindrome."""


def is_palindrome(input_string):
    """Check if a string is a palindrome."""
    input_string = input_string.lower()
    for i in range(len(input_string) // 2):
        if input_string[i] != input_string[-(i + 1)]:
            return False
    return True
