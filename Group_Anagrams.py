
"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict
from typing import List


def group_anagrams(self, strs: List[str]) -> List[List[str]]:
# We start by initializing an empty unordered map called anagram_map, which will store the groups of anagrams.
    anagram_map = defaultdict(list)
# We iterate through each word in the input vector strs.
# We create a string variable called sorted_word and assign it the value of the current word.
# Next, we sort the characters in word using the sorted() function.
# We insert word as the key into the anagram_map unordered map using anagram_map[sorted_word],
# and we push the original word into the vector associated with that key using anagram_map[sorted_word].append(word),
# where word is the current word.
# Since sorted_word is a unique-sorted representation of all the anagrams, it serves as the key in the anagram_map map,
# and the associated vector holds all the anagrams.
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
# For the given example, the anagram_map map would look like this after processing all the words:
# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }
# We return the list, which contains the groups of anagrams.
    return list(anagram_map.values())
