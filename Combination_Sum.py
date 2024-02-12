"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency
 of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""
from typing import List
"""
first we initialize empty list, named result
second we create backtracking function that word similarly as dfs.
the trick for not repeat the same combination more then once is,
in every interation we divide the 'tree' to 2, left and right.
the left side contained the value in candidates[index] (we can use it as mach as we wont, until total = > target)
the right side can not us the values in left side at all, he have only the rimeining values.
                                                    [2,3,6,7]
                                                    /     \
                                        [2]                                []
                                        /  \                         /          \
                                   [2,2]         [2]                [3]            []
                      /         \                /  \               / \          /    \
                [2,2,2]         [2,2]         [2,3]   [2]        [3,6] [3]      [6]     []
            /    \              /   \          /   \     \         |     \       /         \
     [2,2,2,2] [2,2,2,3]    [2,2,3] [2,2]  [2,3,6] [2,3]  [2]      9     [3,7]   [6,7]      [7]
     |             |         |       /   \     |    \     / \             |        |        |   \        
     8             9         7   [2,2,6] [2,2] 11 [2,3] [2,6] [2]         10       13       7   [7,7]
                                 |       /  \      /     |     \                                 |
                                10  [2,2,7] [2,2][2,3,7] 8     [2,7]                            14
                                     |        |     |           |
                                     11       4     12          9
                            
    Time Complexity: O(N^((T/M)+1))
    Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
    Time Complexity: O(T/M)
"""


def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(index, current, total):
        if total == target:
            result.append(current.copy())
            return

        if index >= len(candidates) or total > target:
            return

        current.append(candidates[index])
        dfs(index, current, total + candidates[index])
        current.pop()
        dfs(index + 1, current, total)

    dfs(0, [], 0)
    return result
