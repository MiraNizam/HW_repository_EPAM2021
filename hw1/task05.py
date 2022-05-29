"""
Given a list of integers numbers "nums".

You need to find a sub-array with length <= to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """It finds max sum of a sub-array considering k, max sum <= k"""
    if not nums:
        return None
    sum_nums = []
    while k > 0:
        for index in range(len(nums) - k + 1):
            sum_nums.append(sum(nums[index: index + k]))
        k -= 1
    return max(sum_nums)

