"""
Largest element in the array that is repeated exactly k times
Given an array of integers and an integer ‘k’, the task is to find the largest element from the array that
is repeated exactly ‘k’ times.

Examples:
Input: arr = {1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6}, k = 2
Output: 5
The elements that exactly occur 2 times are 1, 3 and 5
And, the largest element among them is 5.
Input: arr = {1, 2, 3, 4, 5, 6}, k = 2
Output: No such element
There isn't any element in the array
that occurs exactly 2 times.
"""


def largest_elem_repeated_k_times(arr, k):
    if k == 1:
        return max(arr)
    dic = {}

    for val in arr:
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] += 1
    maxi = float('-inf')
    for key in dic:
        if dic[key] == k and maxi < key:
            maxi = key

    return maxi


if __name__ == '__main__':
    print(largest_elem_repeated_k_times([1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6],2))
    print(largest_elem_repeated_k_times([1, 2, 3, 4, 5, 6], 2))
