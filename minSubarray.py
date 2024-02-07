"""
1590. Make Sum Divisible by P
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that
the sum of the remaining elements is divisible by p.
It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.
"""
from typing import List


def min_subarray(self, nums: List[int], p: int) -> int:
    remainder = sum(nums) % p
    if remainder == 0:
        return 0
    n = len(nums)
    result = n
    current = 0
    dic = {0: -1}
    for i, num in enumerate(nums):
        current = (current + num) % p
        if dic.get((current - remainder) % p) is not None:
            result = min(result, i - dic.get((current - remainder) % p))
        dic[current] = i
    return result if result < n else -1
