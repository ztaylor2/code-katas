"""Kata: Sum of two lowest positive integers.

#1 Best Practices Solution:

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


def sum_two_smallest_numbers(numbers):
    """Sum of two smallest numbers in an array."""
    nums = sorted(numbers)
    return nums[0] + nums[1]
