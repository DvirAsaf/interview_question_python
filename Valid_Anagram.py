
"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


def is_anagram(self, s: str, t: str) -> bool:
    """
    Dvir's Work:
    first, if the length of the given strings are different -> return FALSE.
    set a new array the going to containe each letter and the number of time she appear in string s.
    in the same logic we now remove each letter that appear in string t.
    if in the end, the array of 26 letters contain only zeros values, that mean we got anagram.
    else this is NOT the case and we return FALSE.
    """
    # the first try:
    if len(s) != len(t):
        return False
    letters = [0] * 26
    for letter in s:
        letters[ord(letter) - ord('a')] += 1
    for letter in t:
        letters[ord(letter) - ord('a')] -= 1
    for letter in letters:
        if letter != 0:
            return False

    return True
