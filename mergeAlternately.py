"""
1768. Merge Strings Alternately,
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.
"""


def merge_alternately(self, word1: str, word2: str) -> str:
    len1 = len(word1)
    len2 = len(word2)
    merged_word = ''
    smaller = min(len1, len2)
    j = 0
    for i in range(smaller):
        merged_word += word1[i]
        j += 1
        merged_word += word2[i]
        j += 1
    if len1 < len2:
        for i in range(len2 - len1):
            merged_word += word2[smaller + i]
            j += 1
    elif len1 > len2:
        for i in range(len1 - len2):
            merged_word += word1[smaller + i]
            j += 1

    return merged_word
