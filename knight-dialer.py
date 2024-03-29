"""
935. knight-dialer
The chess knight has a unique movement, it may move two squares vertically and one square horizontally,
or two squares horizontally and one square vertically (with both forming the shape of an L).
The possible movements of chess knight are shown in this diagram:
A chess knight can move as indicated in the chess diagram below:
Given an integer n, return how many distinct phone numbers of length n we can dial.
You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial
a number of length n. All jumps should be valid knight jumps.
As the answer may be very large, return the answer modulo 10^9 + 7.
Example 1:
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1,
so placing the knight over any numeric cell of the 10 cells is sufficient.
Example 2:
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are
[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
Example 3:
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
"""


class Solution:
    def knight_dialer(self, n: int) -> int:
        if n == 1:
            return 10

        def multiply(A, B):
            result = [[0] * len(B[0]) for _ in range(len(A))]

            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD

            return result

        A = [
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
        ]

        v = [[1] * 10]
        MOD = 10 ** 9 + 7

        n -= 1
        while n:
            if n & 1:
                v = multiply(v, A)

            A = multiply(A, A)
            n >>= 1

        return sum(v[0]) % MOD
