
"""
https://www.geeksforgeeks.org/maximize-count-of-non-overlapping-subarrays-with-sum-k/
Given an array arr[] and an integer K, the task is to print the maximum number of non-overlapping subarrays with a sum equal to K.


Input: arr[] = {-2, 6, 6, 3, 5, 4, 1, 2, 8}, K = 10
Output: 3
Explanation: All possible non-overlapping subarrays with sum K(= 10) are {-2, 6, 6}, {5, 4, 1}, {2, 8}. Therefore, the required count is 3.

Input: arr[] = {1, 1, 1}, K = 2
Output: 1
"""


def CtSubarr(arr, N, K, m):
    st = set()
    prefixSum = 0
    st.add(prefixSum)
    res = 0
    count = 0

    for i in range(N):
        x = arr[i]
        prefixSum += x

        if ((prefixSum - K) in st):
            if count + 1 == m:
                res += 1
                prefixSum = 0
                st.clear()
                st.add(0)
                count = 0
            else:
                st.add(prefixSum)
                count += 1
        elif count == m:
            prefixSum -= arr[i - m]
            count -= 1
            st.remove(prefixSum - arr[i - m])
        else:

            st.add(prefixSum)
            count += 1

    return res


arr = [1,3,1,1,1,1]
arr = [1,3,1,1,1,1,4,0]
# arr = [1,3,4,0]
N = len(arr)
K = 4
m = 2

print(CtSubarr(arr, N, K, m))
