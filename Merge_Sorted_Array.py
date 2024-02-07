# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n,representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged
# and the last n elements are set to 0 and should be ignored. Nums2 has a length of n.
def merge(nums1, m, nums2, n):
    # Set p1 and p2 to point to the end of their respective arrays.
    p1 = m - 1
    p2 = n - 1
    # And move p backward through the array, each time writing
    # the smallest value pointed at by p1 or p2.
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    print(nums1)


if __name__ == '__main__':
    # input1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    # input 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1,m,nums2,n)
    # input 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1,m,nums2,n)

