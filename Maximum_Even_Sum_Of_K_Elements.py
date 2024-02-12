"""
Maximum Even Sum Of K Elements
This is a popular algorithm problem that can be solved with the Greedy Algorithm approach.
This is an excellent example to learn how to think in the Greedy Way.
In layman’s terms, the greedy way takes the advantage of a locally optimal solution to scale out to
a globally optimal solution.
Now, let’s take a look at the problem statement.
The Problem Statement:
We are given a list (sticking with the Python tongue cause I cannot stop loving it!)
of positive integers and we have to find the maximum even sum for K elements from the list.
If we can’t find one, we return -1.
Notice the emphasis on the word even.

Sample I/O:
Input: [4, 2, 6, 7, 8], k = 3
Output: 18
Explanation:
Since k = 3, we have to take 3 elements from this list. Don’t forget we have to make it an even sum.
So, even if the sum of [8,7,6] = 21 is the max sum we can get but we can’t take it since it’s an odd number.
So, the maximum even sum would be the sum of [8,6,4] = 18, which is the maximum even sum we can get.
Let’s try a couple of more:
Input: [5,5,1,1,3], k = 3
Output: -1
Explanation:
Take a look here, we need 3 elements to make the maximum even sum. But notice we don’t have any even number at all.
Also, it’s impossible that 3 odd numbers will ever add up to an even sum.
Consider: 1 + 3 + 5 = 9, so it’s always an odd sum. So, we just return -1.
"""


def get_max_even_sum(input_arr, k):
    size_input_arr = len(input_arr)

    if k > size_input_arr or size_input_arr == 0:
        return -1

    even_arr = []
    odd_arr = []
    input_arr.sort(reverse=True)

    for i in range(size_input_arr):
        if input_arr[i] % 2 == 0:
            even_arr.append(input_arr[i])
        else:
            odd_arr.append(input_arr[i])
    size_even_arr = len(even_arr)
    size_odd_arr = len(odd_arr)
    even_index = 0
    odd_index = 0
    max_sum = 0

    while k > 0:
        if k % 2 == 1:
            if size_even_arr > 0:
                max_sum += even_arr[even_index]
                even_index += 1
                k -= 1
            else:
                return -1
        else:
            if (even_index < size_even_arr - 2) and (odd_index < size_odd_arr - 2):
                if even_arr[even_index] + even_arr[even_index + 1] > odd_arr[odd_index] + odd_arr[odd_index + 1]:
                    max_sum += even_arr[even_index] + even_arr[even_index + 1]
                    even_index += 2
                else:
                    max_sum += odd_arr[odd_index] + odd_arr[odd_index + 1]
                    odd_index += 2

                # max_sum += max(even_arr[even_index] + even_arr[even_index + 1],
                #                odd_arr[odd_index] + odd_arr[odd_index + 1])
                # even_index += 2
                # odd_index += 2
            elif even_index < size_even_arr - 2:
                max_sum += even_arr[even_index] + even_arr[even_index + 1]
                even_index += 2
            elif odd_index < size_odd_arr - 2:
                max_sum += odd_arr[odd_index] + odd_arr[odd_index + 1]
                odd_index += 2
            k -= 2

    return max_sum


if __name__ == '__main__':
    print(get_max_even_sum([4, 2, 6, 7, 8], 3))
    print(get_max_even_sum([5, 5, 1, 1, 3], 3))
