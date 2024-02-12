
"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""


def find_median_sorted_arrays(self, nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    m1 = 0
    m2 = 0
    for count in range(0, (n + m) // 2 + 1):
        m2 = m1
        if i < n and j < m:
            if nums1[i] > nums2[j]:
                m1 = nums2[j]
                j += 1
            else:
                m1 = nums1[i]
                i += 1
        elif i < n:
            m1 = nums1[i]
            i += 1
        else:
            m1 = nums2[j]
            j += 1

    # Check if the sum of n and m is odd.
    if (n + m) % 2 == 1:
        return float(m1)
    else:
        ans = float(m1) + float(m2)
        return ans / 2.0
