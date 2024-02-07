# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums, k):
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break
        start += 1
    print(nums)


if __name__ == '__main__':
    # input 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
