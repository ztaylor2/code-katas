"""Longest substring in python."""


def max_substring(input_string):
    """."""
    longest_substring = ''
    seen_chars = set()
    current_substring = ''
    for char in input_string:
        if char in seen_chars:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            seen_chars = set()
            current_substring = ''
        else:
            current_substring += char
            seen_chars.add(char)

    return longest_substring
