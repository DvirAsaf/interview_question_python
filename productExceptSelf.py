"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List


def product_except_self(self, nums: List[int]) -> List[int]:
    """
    the qeustion is like that:
    given an integers array name nums, the assignment is to return integer array answer that conrain,
    the multiple of all numbers in array exept the index i in nums, like that,
    we need to do for all the indexes of answer.
    we cant multiple everything and divided by nums[i] for 2 reasons:
    1. nums[i] could be equal to 0, and we cant divide by zero
    2. nums[i] could be equal to 0, and the multiple could be wrong,
    if this is the only zero, so the answer is not zero.

    solution 1:
                creating 3 array in length of nums. left, right and answer.
                for every index we have 2 sliding windows(left and right)
                we traverse from left to right and multiply the nums[i] with the previous index from array left
                [i] = nums[i - 1] * left[i - 1]
                and we do the same thing from right to left
                right[i] = nums[i + 1] * right[i + 1]
                and finally we travers over both array:
                answer[i] = left[i] * right[i]
                for example: nums[1, 2, 3, 4]
                             left[1, 1, 2, 6]
                             right[24, 12, 4, 1]
                             answer[24, 12, 8, 6]
                and return array answer
    solution 2:
                insted of using 3 extara array (left, right and aswer) we yse only one(answer).
                for the first traversal (instead of a left array), we travers over an answer array. (left to right)
                answer[i] = nums[i - 1] * answer[i - 1]
                after which we use reversed function for traversal from right to left. and multiply by varible r.
                in every interval we multiply r by the value in nums[i]
                answer[i] = answer[i] * r
                r = r * nums[i]
                for example: nums[1, 2, 3, 4]
                             answer[1, 1, 2, 6]
                             answer[ , , , 6*r] r=1 nums[i] = 4 -> r=1*4 answer[i] = 6
                             answer[ , , 2*r, 6] r=4 nums[i] = 3 -> r=4*3 answer[i] = 2
                             answer[ , 1*r, 8, 6] r=12 nums[i] = 2 -> r=12*2 answer[i] = 1
                             answer[1*r, 12, 8, 6] r=24 nums[i]= 1 -> r=24*1 answer[i] = 1
                             answer[24, 12, 8, 6]

    """
    length = len(nums)
    answer = [0] * length
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
    r = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * r
        r = r * nums[i]
    return answer
