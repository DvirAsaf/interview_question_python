"""

Given an array of integer arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr. Length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""
from typing import List


def valid_mountain_array(self, arr: List[int]) -> bool:
    if len(arr) < 3:
        return False

    left = 0
    right = len(arr) - 1

    mid = -1
    while left < right:
        if arr[left] == arr[left + 1]:
            return False
        if arr[left] > arr[left + 1]:
            mid = left
            break
        left += 1
    if left == right or left == 0:
        return False
    left = 0
    while right > mid:
        if arr[right] == arr[right - 1]:
            return False

        if arr[right] > arr[right - 1]:
            return False
        right -= 1
    if right == mid:
        return True
