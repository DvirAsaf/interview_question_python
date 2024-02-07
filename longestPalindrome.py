"""
5. The longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
"""


def longest_palindrome(self, s: str) -> str:
    def expand_from_middle(string, left, right):
        if not string or left > right:
            return 0
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1

    if not s or len(s) < 1:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_from_middle(s, i, i)
        len2 = expand_from_middle(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = i - ((length - 1) // 2)
            end = i + (length // 2)
    max_string = s[start: end + 1]
    return max_string
