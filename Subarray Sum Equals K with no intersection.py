"""
https://www.geeksforgeeks.org/maximize-count-of-non-overlapping-subarrays-with-sum-k/
Given an array arr[] and an integer K, the task is to print the maximum number of non-overlapping subarrays with a sum equal to K.


Input: arr[] = {-2, 6, 6, 3, 5, 4, 1, 2, 8}, K = 10
Output: 3
Explanation: All possible non-overlapping subarrays with sum K(= 10) are {-2, 6, 6}, {5, 4, 1}, {2, 8}. Therefore, the required count is 3.

Input: arr[] = {1, 1, 1}, K = 2
Output: 1
"""


# Function to count the maximum
# number of subarrays with sum K
def subarraySum(arr, N, K):
    # Stores all the distinct
    # prefixSums obtained
    st = set()

    # Stores the prefix sum
    # of the current subarray
    prefixSum = 0

    st.add(prefixSum)

    # Stores the count of
    # subarrays with sum K
    res = 0

    for i in range(N):
        prefixSum += arr[i]

        # If a subarray with sum K
        # is already found
        if ((prefixSum - K) in st):
            # Increase count
            res += 1

            # Reset prefix sum
            prefixSum = 0

            # Clear the set
            st.clear()
            st.add(0)

            # Insert the prefix sum
        st.add(prefixSum)

    return res


# Driver Code
arr = [-2, 6, 6, 3, 5, 4, 1, 2, 8]
arr = [1,1,1,1,1]
N = len(arr)
K = 2

# Function call
print(subarraySum(arr, N, K))