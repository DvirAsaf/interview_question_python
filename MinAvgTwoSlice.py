"""
Task description
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N,
is called a slice of array A (notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:
slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.
Write a function:
def solution (A)
that, given a non-empty array A consisting of N integers,
returns the starting position of the slice with the minimal average.
If there is more than one slice with a minimal average,
you should return the smallest starting position of such a slice.

"""


def solution(A):
    # Implement your solution here
    # The trick to this problem is
    # that the min average slice has "the length of 2 or 3"
    # So, we only need to calculate the avg of the slices of length 2 and 3
    min_avg = float('inf')
    min_idx = 0
    n = len(A)

    for i in range(n - 2):
        avg_1 = float((A[i] + A[i + 1]) / 2)
        avg_2 = float((A[i] + A[i + 1] + A[i + 2]) / 3)
        curr_avg = min(avg_1, avg_2)
        if curr_avg < min_avg:
            min_avg = curr_avg
            min_idx = i
    # note: for the last missing case
    # case: avg of length of 2 "A[ len(A)-2 ] + A[ len(A)-1 ]"
    last_avg = float((A[n - 2] + A[n - 1]) / 2)
    if last_avg < min_avg:
        min_avg = last_avg
        min_idx = n - 2

    return min_idx
