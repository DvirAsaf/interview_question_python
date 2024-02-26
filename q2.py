"""
given an array, we need to find the number of pairs with the maximum sum that do not overlap

input: [9,9,9,9]
output: 2

input: [0,3,1,3]
output: 1 ---> 1+3 = 4, can't take both (3,1) and (1,3) since they overlap

"""


def max_non_overlapping_pairs(arr):
    # Find the pair with a maximum sum
    max_sum = float('-inf')
    for i in range(len(arr) - 1):
        if arr[i] + arr[i + 1] > max_sum:
            max_sum = arr[i] + arr[i + 1]

    # Count the number of non-overlapping pairs with the maximum sum
    count = 0
    i = 0
    while i < len(arr) - 1:
        x = arr[i]
        y = arr[i + 1]
        if (x + y) == max_sum:
            count += 1
            i += 2
        else:
            i += 1

    return count

# Test the function
# Edge case: empty array
print(max_non_overlapping_pairs([]))  # Output: 0

# Edge case: array with one element
print(max_non_overlapping_pairs([5]))  # Output: 0

# Edge case: array with two elements
print(max_non_overlapping_pairs([3, 7]))  # Output: 1

# Edge case: array with three elements
print(max_non_overlapping_pairs([1, 5, 2]))  # Output: 1

# General case: array with multiple pairs with maximum sum
print(max_non_overlapping_pairs([4, 2, 5, 5, 3, 7, 7, 3]))  # Output: 1


# General case: array with multiple pairs with maximum sum
print(max_non_overlapping_pairs([4, 2, 5, 5, 3, 7, 3, 7]))  # Output: 3


print(max_non_overlapping_pairs([1, 2, 3, 4, 5]))  # Output: 1

# General case: array with multiple pairs with maximum sum but with overlap
print(max_non_overlapping_pairs([1, 3, 2, 3, 4, 2, 4, 3]))  # Output: 2


# print(max_non_overlapping_pairs([9, 9, 9, 9]))  # Output: 2
# print(max_non_overlapping_pairs([0, 3, 1, 3]))  # Output: 1
print(max_non_overlapping_pairs([1, 3, 1, 1,3]))  # Output: 2
