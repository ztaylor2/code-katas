"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""


def two_sum(nums, target):
    """Big O(n^2)."""
    for i, num in enumerate(nums):
        for x, add_num in enumerate(nums[i + 1:], start=i + 1):
            if num + add_num == target:
                return [i, x]


def two_sum_n(nums, target):
    """Big O(n)."""
    nums_seen = {}
    for i, num in enumerate(nums):
        nums_seen[num] = i
        if target - num in nums_seen:
            return [nums_seen[target - num], i]
    return []
