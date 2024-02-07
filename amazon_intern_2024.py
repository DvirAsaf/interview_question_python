"""
Given a log entry s and target word t, the target word can be obtained by selecting some subset of characters from s
that can be rearranged to form string t and removing them from s.
Determine the maximum number of times the target word can be removed from the given log entry.
*** My understanding is each char cannot use more than once
"""
import collections


def log_entry(s, t):
    if len(t) > len(s):
        return 0

    counter_s = collections.Counter(s)
    counter_t = collections.Counter(t)
    answer = float('inf')

    for elem in counter_t:
        answer = min(answer, counter_s[elem] // counter_t[elem])

    return answer


if __name__ == '__main__':
    s = 'mononom'
    t = 'mon'
    print(log_entry(s, t))
    s = 'abacbc'
    t = 'bca'
    print(log_entry(s, t))
    print("Enter log entry:")
    s = input()
    print("Enter target:")
    t = input()
    print("Output:")
    print(log_entry(s, t))
