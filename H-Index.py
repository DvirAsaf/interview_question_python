"""
274. H-Index
Given an array of integer citations where citations[i] is the number of citations a researcher received for
their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h
such that the given researcher has published at least h papers that have each been cited at least h times.
Example 1:

Input: citations = [3,0,6,1,5]
Output: Three
Explanation: [3,0,6,1,5] means the researcher has five papers in total and each of them had received
 three, 0, 6, 1, 5 citations respectively.
Since the researcher has three papers with at least three citations each and the remaining two with
no more than three citations each, their h-index is 3.
"""
from typing import List


def h_index(self, citations: List[int]) -> int:
    """
    Intuition
    The problem asks for the h-index of a researcher based on the number of citations received for their papers.
    The h-index is the maximum value of h such that the researcher has published at least h papers that have each
    been cited at least h times.
    To find the h-index, we need to sort the array of citations in descending order and identify the largest h-value
    that satisfies the given condition.

    Approach
    The solution begins by sorting the array of citations in reverse order,
    ensuring that the papers with the highest citation counts are at the beginning.
    Next, several conditions are checked to determine the h-index.
    First, if the array contains only one element, and it is greater than zero, the h-index is 1.
    If the smallest value in the sorted array is greater than or equal to the length of the array,
    the h-index is equal to the array length.
    Otherwise, the array is traversed, and for each index i, the value at that index is compared to i+1.
    If the value is less than i+1, 'i' is returned as the h-index.
    If none of the conditions are met, the h-index is 0.
    """
    n = len(citations)
    citations.sort(reverse=True)
    if n == 1 and citations[0] > 0:
        return 1
    if citations[-1] >= n:
        return n
    for i in range(n):
        if citations[i] < i + 1:
            return i
    return 0
