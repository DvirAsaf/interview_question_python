"""
Min Moves to Make String Without 3 Identical Consecutive Letters
Solution:
To solve this task we need to find sequences of the same letters and if the sequence is longer than 3 divide length of
this sequence to 3 and add result of the division to counters of needed moves.

Example of work:
3 consecutive: baaab, replace the middle a (3 / 3 == 1)
4 consecutive: baaaab, replace the third a (4 / 3 == 1)
5 consecutive: baaaaab, replace the third a (5 / 3 == 1)
6 consecutive: baaaaaab -> baabaaab -> baaab -> bab with 2 replacements (6 / 3 == 2)
10 consecutive: baaaaaaaaaab -> baabaaaaaaab -> baaaaaaab -> baaaab -> baab with 3 replacements (10 / 3 == 3)
"""


def min_moves_to_obtain_str_without_3_idebtical_consecutive_letters(s):
    result = 0
    size_s = len(s)
    i = 0
    while i < size_s:
        next = i + 1

        while (next < size_s) and (s[i] == s[next]):
            next += 1

        result += (next - i) // 3
        i = next

    return result


if __name__ == '__main__':
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('baaaaab'))
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('baaab'))
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('baaaab'))
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('baaaaaaaaaab'))
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('ababababababababababa'))
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('aabbaabbaabbaabbaabb'))
    print(min_moves_to_obtain_str_without_3_idebtical_consecutive_letters('baaaaaab'))
