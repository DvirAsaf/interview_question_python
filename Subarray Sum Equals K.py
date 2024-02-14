"""
560. Subarray Sum Equals K

iven an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

def subarraySum(nums, k):
    # Dictionary to store cumulative sums and their counts
    d = {0: 1}
    sums = 0  # Cumulative sum
    count = 0  # Result counter

    # Iterate through the array
    for i in range(len(nums)):
        sums += nums[i]  # Update cumulative sum

        # If (current cumulative sum - k) exists in the dictionary, add its count to the result
        if sums - k in d:
            count += d[sums - k]

        # Update the dictionary with the current cumulative sum
        if sums in d:
            d[sums] += 1
        else:
            d[sums] = 1

    return count

if __name__ == '__main__':
    print(subarraySum([1,1,1], 2))