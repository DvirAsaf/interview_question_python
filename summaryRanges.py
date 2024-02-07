"""
228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"A->b" if a != b
"a" if a == b
"""


def summary_ranges(self, nums):
    if not nums:
        return []

    ranges = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(nums[i - 1]))
            start = nums[i]

    # Handle the last range
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(str(start) + "->" + str(nums[-1]))

    return ranges
