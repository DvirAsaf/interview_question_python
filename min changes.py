def min_changes(arr):
    arr.sort()
    n = len(arr)
    pos = n // 2
    mid = arr[pos]
    elem = mid - pos
    total = 0
    for i in range(n):
        total += abs(arr[i] - elem)
        elem += 1

    return total


if __name__ == '__main__':
    print(min_changes([6,6,6,6,3,2,1,9,4]))
