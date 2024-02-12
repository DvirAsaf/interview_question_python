"""
616. Add Bold Tag in String
You are given a string s and an array of strings words.
You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words.
If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
If two substrings wrapped by bold tags are consecutive, you should combine them.
Return s after adding the bold tags.

Example 1:
Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
Explanation: The two strings of words are substrings of s as following: "abcxyz123".
We add <b> before each substring and </b> after each substring.

Example 2:
Input: s = "aaabbb", words = ["aa","b"]
Output: "<b>aaabbb</b>"
Explanation:
"aa" appears as a substring two times: "aaabbb" and "aaabbb".
"b" appears as a substring three times: "aaabbb", "aaabbb", and "aaabbb".
We add <b> before each substring and </b> after each substring: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>".
Since the first two <b>'s overlap, we merge them: "<b>aaa</b><b>b</b><b>b</b><b>b</b>".
Since now the four <b>'s are consecutive, we merge them: "<b>aaabbb</b>".
"""
from typing import List


class Solution:
    def add_bold_tag(self, s: str, words: List[str]) -> str:
        # first, match occurances of each word in s and mark start and end tags
        # reduction to merge intervals problem
        # then merge tags together (removing nested tags)
        # apply the merged tags to the string s

        # build list of intervals -- start (inclusive) to end (exlusive) (no regex)
        intervals = []
        windows = set([len(word) for word in words])  # removing duplicate window lengths
        words = set(words)  # hash words for quick lookup
        n = len(s)
        for window in windows:
            for i in range(n - window + 1):
                if s[i:i + window] in words:
                    intervals.append([i, i + window])

        # reduction to merge intervals
        intervals.sort(key=lambda x: (x[0], x[1]))  # O(n log n)
        merged = []
        for itv in intervals:
            if not merged or merged[-1][1] < itv[0]:
                merged.append(itv)
            else:
                merged[-1][1] = max(merged[-1][1], itv[1])

        # convert merged itvs to bold tags
        s_arr = list(s)
        for itv in merged[::-1]:  # reverse to allow multiple insertions on the same list
            s_arr.insert(itv[1], '</b>')
            s_arr.insert(itv[0], '<b>')

        return ''.join(s_arr)
