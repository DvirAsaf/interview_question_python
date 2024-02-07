"""
275. H-Index II
Given an array of integer citations where citations[i] is the number of citations a researcher received
 for their ith paper and citations are sorted in ascending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h
such that the given researcher has published at least h papers that have each been cited at least h times.

You must write an algorithm that runs in logarithmic time.



Example 1:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received
 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than
3 citations each, their h-index is 3.
"""
from typing import List


def h_index(self, citations: List[int]) -> int:
    """
    Since the list of citation numbers is sorted in ascending order, we can solve the problem in a single pass.
    Consider a paper with citation number citations[i].
    The number of papers with a citation number larger than citations[i] is n - i - 1.
    Hence, including the current paper, there are n - 'i' papers that are cited at least citations[i] times.

    Per the definition of H-Index,
    we need to find the first paper at index i were citation number citation[i] is greater than or equal to n - i,
    Since all papers after paper 'i' are cited at least citations[i] times,
    there are n - 'i' papers (including paper i) that are cited at least citations[i] times.
    In other words, the H-Index is n - i.
    """
    n = len(citations)
    if n == 1 and citations[0] > 0:
        return 1
    if citations[0] >= n:
        return n
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0
    # Time complexity: O(N)
    # Space complexity: O(1)
