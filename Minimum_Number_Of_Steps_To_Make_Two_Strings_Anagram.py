"""
1347.Minimum_Number_Of_Steps_To_Make_Two_Strings_Anagram
You are given two strings of the same length s and t.
In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.
"""
import collections


def min_steps(self, s: str, t: str) -> int:
    # first, we counter the number of each letter.
    counter = collections.Counter(s)
    # second, we initialize variable
    answer = 0
    # third, we traversal over string 't' if we see a letter that appears in s we're decreasing by 1
    # else, this means that we're missing letter -> we need to add replace a letter
    for c in t:
        if counter[c] > 0:
            counter[c] -= 1
        else:
            answer += 1
    return answer
