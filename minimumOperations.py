"""
2357. Make Array Zero by Subtracting Equal Amounts
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.
"""
from typing import List


def minimum_operations(self, nums: List[int]) -> int:
    nums = set(nums)
    nums = sorted(nums)
    steps = 0
    total = 0
    for x in nums:
        if x == 0:
            continue
        total = x - total
        steps += 1
    return steps
