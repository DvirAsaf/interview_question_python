"""
Count of different numbers divisible by 3 that can be obtained by changing at most one digit.
Given a string str representing a number having N digits,
the task is to calculate the number of ways to make the given number divisible by 3 by changing
at most one digit of the number.

Examples:
Input: str[] = “23”
Output: 7
Explanation: Below are the numbers that can be made from the string which are divisible by 3 –03, 21, 24, 27, 33, 63, 93
1.Change 2 to 0 (0+3)=3 divisible by 3
2.Change 3 to 1 (2+1)=3 divisible by 3
3 change 3 to 4 (2+4)=6 divisible by 3
4 change 2 to 3 sum is 6 divisible by 3
Similarly there are total 7 number of ways to make the given number divisible by 3

Input: str[] = “235”
Output: 9
"""


def divisible_by_3(s):
    n = len(s)
    total = 0

    for i in range(n):
        total += int(s[i])

    count = 0
    if (total % 3) == 0:
        count += 1

    for i in range(n):
        remaining = total - (int(s[i]) - 48)
        for j in range(10):
            if ((remaining + j) % 3 == 0) and j != (int(s[i]) - 48):
                count += 1

    return count


if __name__ == '__main__':
    print(divisible_by_3(('23')))
    print(divisible_by_3(('235')))
    print(divisible_by_3(('0081')))
    print(divisible_by_3(('022')))
