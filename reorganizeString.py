"""
767. Reorganize String
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""
import collections


def reorganize_string(self, s: str) -> str:
    # firsr we find the length of s
    n = len(s)
    # second, we use Counter function to get dictionary of unique values and the numbers that each value appears in s.
    dic = collections.Counter(s)
    # third, we sort the dictionary by the number of appearince in s, in reverse order.
    # the dictionary will start from the char that appears the most of the time, to the char that appears the least.
    sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    # now we check if there is a case of one char appear more than half of the length of s, if we found char like that,
    # we can return "", because it is not possible to arrange them.
    for c in dic:
        if dic[c] > ((n + 1) // 2):
            return ""
    # if we do not find char like that, we can arrange the chars.
    # first, we make empty staring in size of n, (length of s).
    result = [""] * n
    # now we iterate over the dictionary, for that we use another variable.
    p = n
    while p > 0:
        i = 0
        # now we search for empty space in a result, this is for entered the correct place the values.
        while result[i] != "":
            i += 1
        # we start with a key that appears most of the time (most frequent).
        for key in sorted_dic:
            while i < n and dic[key] > 0:
                # for each key we remove from the dictionary and put in a result,
                # we need to decrease the number of appearances
                result[i] = key
                dic[key] -= 1
                # we jump in 2 because we cant put the same key adjacent to each other
                i += 2
                # because result get new key, we left p - 1 keys to enter, so we decrease p by 1
                p -= 1
    # finally, we return the rearranged string
    return ''.join(result)
